"""EQ4-F proof-completion design: exact pre-check of the constructive route for L7 (`schmidt2`) and of the chain
L6-L8 that turns it into the lower bound (research only; nothing here is kernel-checked).

Usage:  python3 -I -B precheck_schmidt.py <base>/verification/lean-mathlib/OIBridge

The construction is the one a Lean proof would follow, with no SVD and no algebraic closure:
  1. M = C^H C = [[p, q], [conj q, r]] (Hermitian, p and r real).
  2. If q != 0: lam = (p + r + sqrt((p - r)^2 + 4|q|^2)) / 2 (a real square root) and v = (q, lam - p);
     if q = 0: v = e0 when p >= r, else e1.
  3. w = v / |v|, wperp = (-conj w1, conj w0), W = [w | wperp]  (W is in SU(2) by construction).
  4. c1 = C w; if c1 != 0: u = c1 / |c1|, U = [u | (-conj u1, conj u0)]; else U = 1.
  5. D = U^H C W; V = conj W, so that C = U D V^T.
DECISION RULE (fixed before the first run; rules, not expected numbers).  Print `VERDICT SCHMIDT-ROUTE-EXACT` iff every
check passes; otherwise `VERDICT NOT RENDERED`.  Exact arithmetic (sympy: Gaussian rationals and one real square root).
  K0  sgn, pc, pt parsed from the base equal the transcription (cnot).
  T1  for each test matrix C (generic, rank one, q = 0 with p >= r and with p < r, real, zero): v is an eigenvector
      of M (M v = lam v), W and U are in SU(2), D is diagonal, V is in SU(2), and C = U D V^T exactly.
  T2  the lower-bound chain: pureTab C = actC R_U (actT R_V (pureTab D)), and for D != 0,
      pureTab D = (|d0|^2 + |d1|^2) cnot (prodState x z3) with x the Bloch vector of (d0, d1) normalized.
  C1  countercontrol: with V = W (no conjugation), C = U D V^T fails for some test matrix with non-real entries.
"""
import re
import sys

import sympy as sp
from sympy import I, Matrix, Rational as Q

BASE = sys.argv[1]
RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""), flush=True)


src_cd = open(BASE + "/CompositeDimension.lean").read()
SGN = lambda m, n: -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1  # noqa: E731
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def parse_table(name):
    m = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})" % name, src_cd)
    return [[int(v) for v in re.findall(r"=> (\d)", ln)] for ln in m.group(1).strip().splitlines()]


sgn_line = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := (.*)", src_cd).group(1).strip()
check("K0 sgn, pc, pt transcription", parse_table("pc") == PC and parse_table("pt") == PT
      and sgn_line == "if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1")


def zero(e):
    e = sp.expand(e)
    if e == 0:
        return True
    return sp.simplify(sp.radsimp(e)) == 0


def zeroM(Mx):
    return all(zero(v) for v in Mx)


def cj(z):
    return sp.conjugate(z)


def nrm2(vec):
    return sp.expand(sum(sp.expand(v * cj(v)) for v in vec))


SIG = [sp.eye(2), Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]


def pureTab(C):
    return Matrix(4, 4, lambda m, n: sp.re(sp.expand((C.H * SIG[m] * C * SIG[n].T).trace())))


def H(N):
    out = sp.zeros(4, 4)
    out[0, 0] = 1
    out[1:, 1:] = N
    return out


def actC(N, om):
    return H(N) * om


def actT(N, om):
    return om * H(N).T


def prodState(x, y):
    hx = Matrix([1] + list(x))
    hy = Matrix([1] + list(y))
    return hx * hy.T


def cnot(om):
    return Matrix(4, 4, lambda m, n: SGN(m, n) * om[PC[m][n], PT[m][n]])


def spinR(U):
    return Matrix(3, 3, lambda j, k: sp.re(sp.expand((SIG[j + 1] * U * SIG[k + 1] * U.H).trace())) / 2)


def in_su2(U):
    return zeroM(U * U.H - sp.eye(2)) and zero(U.det() - 1)


def schmidt(C):
    M = (C.H * C).applyfunc(sp.expand)
    p, q, r = sp.re(M[0, 0]), M[0, 1], sp.re(M[1, 1])
    if not zero(q):
        lam = (p + r + sp.sqrt((p - r) ** 2 + 4 * sp.expand(q * cj(q)))) / 2
        v = Matrix([q, lam - p])
    else:
        lam = p if (p - r) >= 0 else r
        v = Matrix([1, 0]) if (p - r) >= 0 else Matrix([0, 1])
    eig = zeroM(M * v - lam * v)
    nv = sp.sqrt(nrm2(v))
    w = v / nv
    wp = Matrix([-cj(w[1]), cj(w[0])])
    W = Matrix.hstack(w, wp)
    c1 = C * w
    if not zero(nrm2(c1)):
        u = c1 / sp.sqrt(nrm2(c1))
        U = Matrix.hstack(u, Matrix([-cj(u[1]), cj(u[0])]))
    else:
        U = sp.eye(2)
    D = (U.H * C * W).applyfunc(lambda z: sp.radsimp(sp.expand(z)))
    V = W.applyfunc(cj)
    return eig, W, U, D, V


tests = {
    "generic": Matrix([[1 + 2 * I, Q(-1, 2) + I], [3, 2 - I]]),
    "generic2": Matrix([[Q(1, 3), -I], [2 + I, Q(-3, 2)]]),
    "rank one": Matrix([[1 + I, 2], [Q(1, 2) + Q(1, 2) * I, 1]]),
    "q=0, p>=r": Matrix([[2, 0], [0, 1 + I]]),
    "q=0, p<r": Matrix([[0, 1], [0, 0]]),
    "real": Matrix([[1, 2], [3, 4]]),
    "zero": sp.zeros(2, 2),
}
ok_t1, ok_t2, cc = True, True, False
details = []
for name, C in tests.items():
    eig, W, U, D, V = schmidt(C)
    diag = zero(D[0, 1]) and zero(D[1, 0])
    recon = zeroM(C - U * D * V.T)
    t1 = eig and in_su2(W) and in_su2(U) and diag and in_su2(V) and recon
    ok_t1 &= t1
    if not zeroM(C - U * D * W.T):
        cc = True
    # T2: lower-bound chain
    RU, RV = spinR(U), spinR(V)
    chain = zeroM(pureTab(C) - actC(RU, actT(RV, pureTab(D))))
    d0, d1 = D[0, 0], D[1, 1]
    n = sp.expand(d0 * cj(d0) + d1 * cj(d1))
    if not zero(n):
        z = sp.expand(cj(d0) * d1)
        x = [2 * sp.re(z) / n, 2 * sp.im(z) / n, sp.expand(d0 * cj(d0) - d1 * cj(d1)) / n]
        chain &= zeroM(pureTab(D) - n * cnot(prodState(x, [0, 0, 1])))
    ok_t2 &= chain
    details.append("%s:%s%s" % (name, "ok" if t1 else "T1-FAIL", "" if chain else "/T2-FAIL"))
check("T1 eigenvector, SU(2) factors, diagonal D, exact reconstruction C = U D V^T (7 matrices)", ok_t1,
      ", ".join(details))
check("T2 pureTab C = actC R_U (actT R_V (pureTab D)) and pureTab D = n cnot (prodState x z3)", ok_t2)
check("C1 countercontrol: V = W instead of conj W fails for some matrix", cc)
print("--- precheck_schmidt: %d/%d checks pass" % (sum(RES), len(RES)))
print("VERDICT SCHMIDT-ROUTE-EXACT" if all(RES) else "VERDICT NOT RENDERED")
