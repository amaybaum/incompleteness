"""Coordinator's independent audit of EQ4-SOURCE (research only; own code, imports nothing from the thread).

Usage:  python3 -I -B audit_source.py <base>/verification/lean-mathlib/OIBridge

DECISION RULE (fixed before the first run; rules, not expected numbers).  Print `VERDICT SOURCE-AUDIT-EXACT` iff every
check passes; otherwise `VERDICT NOT RENDERED`.  Exact arithmetic only (sympy Rational, I).
  K0  sgn, pc, pt parsed from CompositeDimension.lean equal the transcription; chainW parsed from K2Guard equals
      cnot idW computed here.
  AS  anchor sum (KT4 minus tok, any bodies): with pState x y = hom x hom y^T on 17 x 17 arrays and pEff e f w =
      coeff(e)^T w coeff(f), (a) pEff e f (pState x y) = e(x) f(y); (b) PA's product effect at PB's anchored product
      equals e(x0) f(y0) and PB's at PA's equals E(L0) F(L0'); (c) the unit pairing is 1 at both product kinds;
      (d) tok fails at some index (random rational data).  Control: with zero anchors (c) fails.
  MR  M_rho: (a) Q3 != twin (pauliW phiW = v v^H with v = (1,0,0,1)/sqrt2; singlet value of pauliW idW < 0);
      (b) the witnesses X = Y = phiW (in Q3), E = phiW/4 (in Q3*, through pauliW phiW PSD and the pairing identity),
      F = dg(1,-1,1,-1)/4 with actT reflY F = dg(1,-1,-1,-1)/4 PSD (so F is in twin*); (c) family (i) value
      ipW X (E Y F^T) is negative; (d) rho = flat . actT reflY . unflat is an involution, so PB's evaluation law holds;
      (e) tok fails in M_rho at a PA product state.
  G   landed gate countermodels: (a) idW pairs nonnegatively with 200 random Lorentz pairs and chainW = cnot idW
      takes -1/2 at sharp b = -e_x, c = -e_z; (b) F(prodState x y) = 1/2|x - Dy|^2 + 1/2(1-|x|^2) + 1/2(1-|y|^2)
      symbolically (D = diag(1,-1,1)), and F(phiW) < 0 with phiW = cnot(prodState xplus z3).
"""
import random
import re
import sys

import sympy as sp
from sympy import I, Matrix, Rational as Q

BASE = sys.argv[1]
rng = random.Random(20261009 + 7)
RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""), flush=True)


src_cd = open(BASE + "/CompositeDimension.lean").read()
src_k2 = open(BASE + "/K2Guard.lean").read()
SGN = lambda m, n: -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1  # noqa: E731
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def parse_table(name):
    m = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})" % name, src_cd)
    return [[int(v) for v in re.findall(r"=> (\d)", ln)] for ln in m.group(1).strip().splitlines()]


def cnot(om):
    return Matrix(4, 4, lambda m, n: SGN(m, n) * om[PC[m][n], PT[m][n]])


idW = sp.eye(4)
mch = re.search(r"def chainW : W 3 := (!\[.*\])", src_k2).group(1)
rows = re.findall(r"!\[([^\[\]]*)\]", mch)
chainW = Matrix([[sp.sympify(v.strip()) for v in r.split(",")] for r in rows])
sgn_line = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := (.*)", src_cd).group(1).strip()
check("K0 sgn, pc, pt transcription; chainW (K2G) = cnot idW",
      parse_table("pc") == PC and parse_table("pt") == PT
      and sgn_line == "if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1" and chainW == cnot(idW))


def rq():
    return Q(rng.randint(-5, 5), rng.randint(1, 4))


# ---------------------------------------------------------------------------------------------- AS anchor sum
def hom(x):
    return Matrix([1] + list(x))


def pState(x, y):
    return hom(x) * hom(y).T


def pEff(e, f, w):          # e, f given as coefficient vectors (e0, e_1..e_16); value coeff(e)^T w coeff(f)
    return (e.T * w * f)[0, 0]


def ev(e, x):
    return e[0] + sum(e[i + 1] * x[i] for i in range(len(x)))


def rvec(n):
    return [rq() for _ in range(n)]


ok_a = ok_b = ok_c = True
tok_diff = []
for _ in range(4):
    x, y, L, Lp, x0, y0, L0, L0p = (rvec(16) for _ in range(8))
    e, f, E, F = (Matrix(rvec(17)) for _ in range(4))
    a0, b0 = pState(L0, L0p), pState(x0, y0)
    # PA.prodState x y = (pState x y, a0), PA.prodEff e f = pEff e f . fst; PB symmetric with b0, snd
    PAst, PBst = (pState(x, y), a0), (b0, pState(L, Lp))
    ok_a &= pEff(e, f, PAst[0]) == ev(e, x) * ev(f, y) and pEff(E, F, PBst[1]) == ev(E, L) * ev(F, Lp)
    ok_b &= pEff(e, f, PBst[0]) == ev(e, x0) * ev(f, y0) and pEff(E, F, PAst[1]) == ev(E, L0) * ev(F, L0p)
    u = Matrix([1] + [0] * 16)
    ok_c &= pEff(u, u, PAst[0]) == 1 and pEff(u, u, PBst[0]) == 1 and pEff(u, u, PBst[1]) == 1 \
        and pEff(u, u, PAst[1]) == 1
# tok at the body point PAst for one index: PA-side coordinate product vs PB-side
x, y = rvec(16), rvec(16)
L0, L0p = rvec(16), rvec(16)
PAst = (pState(x, y), pState(L0, L0p))


def coordvec(k):            # coefficient vector of the k-th coordinate functional of the chart (Fin 16)
    v = [0] * 17
    v[k + 1] = 1
    return Matrix(v)


def tabIdx(m, n):
    return 4 * m + n


diffs = []
for (a, b, c, d) in [(1, 1, 0, 0), (0, 1, 2, 3), (2, 0, 1, 3)]:
    lhs = pEff(coordvec(tabIdx(a, b)), coordvec(tabIdx(c, d)), PAst[0])
    rhs = pEff(coordvec(tabIdx(a, c)), coordvec(tabIdx(b, d)), PAst[1])
    diffs.append(lhs - rhs)
zero_anchor_unit = pEff(Matrix([1] + [0] * 16), Matrix([1] + [0] * 16), sp.zeros(17, 17))
check("AS anchor sum: evaluation laws, cross values e(x0)f(y0) and E(L0)F(L0'), unit pairing 1, tok fails;"
      " control: zero anchor gives unit pairing 0", ok_a and ok_b and ok_c and any(dd != 0 for dd in diffs)
      and zero_anchor_unit == 0, "tok differences %s" % [str(dd) for dd in diffs])

# ---------------------------------------------------------------------------------------------- MR  M_rho
SIG = [sp.eye(2), Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]


def kron(A, B):
    return Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


def pauliW(om):
    out = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if om[m, n] != 0:
                out += om[m, n] * kron(SIG[m], SIG[n])
    return (out / 4).applyfunc(sp.expand)


def psd_minors(Hm):
    from itertools import combinations
    vals = [sp.simplify(Hm.extract(list(s), list(s)).det()) for r in range(1, 5) for s in combinations(range(4), r)]
    return all(sp.im(v) == 0 and sp.re(v) >= 0 for v in vals)


def H(N):
    out = sp.zeros(4, 4)
    out[0, 0] = 1
    out[1:, 1:] = N
    return out


reflY = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 1]])


def actT(N, om):
    return om * H(N).T


def dg(*v):
    return sp.diag(*v)


phiW = dg(1, 1, -1, 1)
v = Matrix([1, 0, 0, 1])
s = Matrix([0, 1, -1, 0])
q3_ne_twin = (pauliW(phiW) == v * v.H / 2) and sp.simplify((s.H * pauliW(idW) * s)[0, 0]) < 0 \
    and actT(reflY, phiW) == idW
Xw, Yw, Ew, Fw = phiW, phiW, phiW / 4, dg(1, -1, 1, -1) / 4
Gw = actT(reflY, Fw)
memb = psd_minors(pauliW(Xw)) and psd_minors(pauliW(Ew)) and Gw == dg(1, -1, -1, -1) / 4 and psd_minors(pauliW(Gw))
# pairing identity at the witnesses (E against a Q3 element; G against a Q3 element) -- spot: ipW = 4 Re tr
spot = all(sp.simplify(4 * sp.re((pauliW(A) * pauliW(B)).trace()) - sum(A[i, j] * B[i, j] for i in range(4)
                                                                         for j in range(4))) == 0
           for A, B in [(Ew, phiW), (Gw, phiW), (Ew, Gw)])
val = sum(Xw[m, n] * (Ew * Yw * Fw.T)[m, n] for m in range(4) for n in range(4))


def flat(om):
    return [om[m, n] for m in range(4) for n in range(4)]


def unflat(vv):
    return Matrix(4, 4, lambda m, n: vv[4 * m + n])


def rho(vv):
    return flat(actT(reflY, unflat(vv)))


samples = [rvec(16) for _ in range(3)]
invol = all(rho(rho(sv)) == sv for sv in samples)
# PB law: PB.prodEff E F (PB.prodState L L') = pEff E (F . rho) (pState L (rho L')) = E(L) F(rho rho L') = E(L) F(L')
Ec, Fc = Matrix(rvec(17)), Matrix(rvec(17))
L, Lp = rvec(16), rvec(16)


def compose_rho(Fv):        # coefficient vector of F . rho (rho linear, fixes the unit entry)
    lin = [Fv[k + 1] for k in range(16)]
    new = [0] * 16
    for k in range(16):     # (F . rho)(x) = F0 + sum_k F_k rho(x)_k ; rho(x)_k = sign_k x_k
        sgn = rho([1 if j == k else 0 for j in range(16)])[k]
        new[k] = lin[k] * sgn
    return Matrix([Fv[0]] + new)


pb_law = pEff(Ec, compose_rho(Fc), pState(L, rho(Lp))) == ev(Ec, L) * ev(Fc, Lp)
# tok in M_rho at a PA product state pState x y (x = flat phiW, y = flat prodState 0 e_y)
xr = flat(phiW)
yr = flat(Matrix(4, 4, lambda m, n: hom([0, 0, 0])[m] * hom([0, 1, 0])[n]))   # prodState 0 e_y
st = pState(xr, yr)
pa_side = pEff(coordvec(tabIdx(0, 0)), coordvec(tabIdx(0, 2)), st)
pb_side = pEff(coordvec(tabIdx(0, 0)), compose_rho(coordvec(tabIdx(0, 2))), st)
check("MR M_rho: Q3 != twin; witnesses in Q3, Q3*, twin*; family (i) value negative; rho involution and PB's"
      " evaluation law; tok fails", q3_ne_twin and memb and spot and val < 0 and invol and pb_law and
      pa_side != pb_side, "value %s, tok difference %s" % (val, pa_side - pb_side))

# ---------------------------------------------------------------------------------------------- G gate countermodels
def lor_rand():
    a0 = Q(rng.randint(1, 6))
    vec = [rq() for _ in range(3)]
    n2 = sum(t * t for t in vec)
    if n2 > a0 * a0:
        vec = [t * a0 / (abs(t) + abs(vec[0]) + abs(vec[1]) + abs(vec[2]) + 1) for t in vec]
    return Matrix([a0] + vec)


def pairVal(a, b, om):
    return (a.T * om * b)[0, 0]


ok_id = all(pairVal(lor_rand(), lor_rand(), idW) >= 0 for _ in range(200))
sh = lambda vv: Matrix([Q(1, 2)] + [Q(t, 2) for t in vv])  # noqa: E731
chain_val = pairVal(sh([-1, 0, 0]), sh([0, 0, -1]), chainW)
x1, x2, x3, y1, y2, y3 = sp.symbols("x1 x2 x3 y1 y2 y3", real=True)
P = Matrix(4, 4, lambda m, n: hom([x1, x2, x3])[m] * hom([y1, y2, y3])[n])
Ffun = lambda om: om[0, 0] - om[1, 1] + om[2, 2] - om[3, 3]  # noqa: E731
xv, yv = Matrix([x1, x2, x3]), Matrix([y1, y2, y3])
Dm = sp.diag(1, -1, 1)
ident = sp.expand(Ffun(P) - (Q(1, 2) * ((xv - Dm * yv).T * (xv - Dm * yv))[0, 0]
                             + Q(1, 2) * (1 - (xv.T * xv)[0, 0]) + Q(1, 2) * (1 - (yv.T * yv)[0, 0]))) == 0
phi_from = cnot(Matrix(4, 4, lambda m, n: hom([1, 0, 0])[m] * hom([0, 0, 1])[n]))
check("G landed gate countermodels: idW nonnegative on 200 Lorentz pairs, chainW = cnot idW at -1/2; F >= 0 on"
      " products (identity) and F(cnot(prodState xplus z3)) < 0", ok_id and chain_val == Q(-1, 2) and ident
      and phi_from == phiW and Ffun(phi_from) < 0, "chainW value %s, F(phiW) %s" % (chain_val, Ffun(phi_from)))
print("--- audit_source: %d/%d checks pass" % (sum(RES), len(RES)))
print("VERDICT SOURCE-AUDIT-EXACT" if all(RES) else "VERDICT NOT RENDERED")
