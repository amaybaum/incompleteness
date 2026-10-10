"""Exact pre-check of the convention-sensitive heavy-layer STATEMENTS of the preflight package (their proofs
stay open).  Research only, base bcbc516f.  Definitions mirror the Lean text of FourCopyPackage.lean:
  pauli1 = (1, X, Y, Z) with Y = [[0,-i],[i,0]];  pauliW w = 1/4 sum w_{mn} pauli1 m (x) pauli1 n  (first token = row);
  Q3 = {w | pauliW w PSD};  twin = actT reflY '' Q3;  pureTab C = Re tr(C^H pauli1 m C (pauli1 n)^T);
  blochOf a = (Re tr(a a^* pauli1 (j+1)) / Re tr(a a^*))_j;  kernel cnot tables as in precheck_parity.py.
Usage: python3 -I -B precheck_heavy.py
DECISION RULE: VERDICT `PREFLIGHT-HEAVY-EXACT` iff every check passes.
"""
import itertools
import random
import sys

import sympy as sp
from sympy import I, Matrix, Rational as R, eye, zeros

sys.path.insert(0, __file__.rsplit("/", 1)[0])
checks = []


def check(name, cond):
    checks.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


R4 = range(4)
PC = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
      (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
      (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}


def sgn(m, n):
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


def cnot(w):
    return {(m, n): sgn(m, n) * w[PC[(m, n)], PT[(m, n)]] for m in R4 for n in R4}


def hom(x):
    return [sp.Integer(1)] + list(x)


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return {(m, n): hx[m] * hy[n] for m in R4 for n in R4}


def sharpVec(b):
    return [R(1, 2)] + [sp.S(c) / 2 for c in b]


def tens(X, Y):
    return {(m, n): X[m] * Y[n] for m in R4 for n in R4}


def tabMul(A, B):
    return {(m, n): sp.expand(sum(A[m, k] * B[k, n] for k in R4)) for m in R4 for n in R4}


def tabT(A):
    return {(m, n): A[n, m] for m in R4 for n in R4}


def homMap(N, v):
    return [v[0]] + list(N * Matrix(v[1:]))


def actT(N, w):
    out = {}
    for m in R4:
        row = homMap(N, [w[m, n] for n in R4])
        for n in R4:
            out[m, n] = row[n]
    return out


def actC(N, w):
    out = {}
    for n in R4:
        col = homMap(N, [w[k, n] for k in R4])
        for m in R4:
            out[m, n] = col[m]
    return out


PAULI = [eye(2), Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]


def pauliW(w):
    out = zeros(4, 4)
    for m in R4:
        for n in R4:
            out += w[m, n] * sp.kronecker_product(PAULI[m], PAULI[n])   # (Fin 2 x Fin 2) lex = kron order
    return out / 4


def pureTab(C):
    return {(m, n): sp.re(sp.expand((C.H * PAULI[m] * C * PAULI[n].T).trace())) for m in R4 for n in R4}


def blochOf(a):
    a = Matrix(a)
    P = a * a.H
    nrm = sp.re(sp.expand(P.trace()))
    return [sp.simplify(sp.re(sp.expand((P * PAULI[j + 1]).trace())) / nrm) for j in range(3)]


def is_psd(M):
    M = M.applyfunc(sp.nsimplify)
    if not (M - M.H).applyfunc(sp.simplify).is_zero_matrix:
        return False
    return all(sp.re(sp.N(ev, 30)) >= -1e-20 for ev in M.eigenvals())


REFLY = sp.diag(1, -1, 1)
z3 = [0, 0, 1]
xplus = [1, 0, 0]

# --- the pure-table dictionary and the Bell tables
phiW = {(m, n): ((-1 if m == 2 else 1) if m == n else 0) for m in R4 for n in R4}
idW = {(m, n): (1 if m == n else 0) for m in R4 for n in R4}
P_phi = pauliW(phiW)
check("H1 pauliW phiW is the projector onto (|00>+|11>)/sqrt2 (phiW in Q3, pure)",
      P_phi == (Matrix([1, 0, 0, 1]) * Matrix([1, 0, 0, 1]).T) / 2)
check("H2 idW is not in Q3 (pauliW idW has eigenvalue -1/2)", R(-1, 2) in pauliW(idW).eigenvals())
check("H3 idW = actT reflY phiW, so idW in twin; phiW not in twin (actT reflY phiW = idW is not PSD and "
      "actT reflY is an involution)", actT(REFLY, phiW) == idW)
C_bell = Matrix([[1, 0], [0, 1]]) / sp.sqrt(2)
check("H4 pureTab of the Bell coefficient matrix diag(1,1)/sqrt2 is phiW", pureTab(C_bell) == phiW)
rng = random.Random(20261009)


def rc():
    return R(rng.randint(-4, 4), rng.randint(1, 3)) + I * R(rng.randint(-4, 4), rng.randint(1, 3))


ok = True
for _ in range(3):
    C = Matrix(2, 2, lambda i, j: rc())
    T = pureTab(C)
    v = Matrix([C[0, 0], C[0, 1], C[1, 0], C[1, 1]])                   # row index = first token
    ok &= (pauliW(T) - v * v.H).applyfunc(sp.simplify).is_zero_matrix
check("H5 pauliW (pureTab C) = vec(C) vec(C)^H for random exact C (pureTab_mem_Q3 statement, first token = row)",
      ok)

# --- link_conditional, exactly as stated in the Lean file
ok, ratios = True, []
for _ in range(3):
    u, u2 = rc(), rc()
    b = [rc(), rc()]
    S1 = cnot(prodState(blochOf([1, u]), z3))
    S2 = cnot(prodState(blochOf([1, u2]), z3))
    Eff = cnot(tens(sharpVec(xplus), sharpVec(blochOf(b))))
    lhs = tabMul(tabMul(S1, Eff), tabT(S2))
    Cmat = sp.diag(1, u) * Matrix([[b[0], b[1]], [b[1], b[0]]]).applyfunc(sp.conjugate) * sp.diag(1, u2)
    rhs = pureTab(Cmat)
    # find c with lhs = c * rhs
    c = None
    for key in rhs:
        if sp.simplify(rhs[key]) != 0:
            c = sp.simplify(lhs[key] / rhs[key])
            break
    prop = c is not None and all(sp.simplify(lhs[k] - c * rhs[k]) == 0 for k in rhs)
    ok &= prop and sp.N(c) > 0
    ratios.append(str(sp.N(c, 6)) if c is not None else "none")
check("H6 link_conditional as stated: (cnot S(u)) . (cnot Eff(b)) . (cnot S(u'))^T = c pureTab(diag(1,u) conj(Circ b) "
      "diag(1,u')) with c > 0  [c = " + ", ".join(ratios) + "]", ok)

# countercontrol for H6: without the conjugation the identity must fail for generic complex b
ok_cc = False
for _ in range(2):
    u, u2 = rc(), rc()
    b = [rc(), rc()]
    S1 = cnot(prodState(blochOf([1, u]), z3))
    S2 = cnot(prodState(blochOf([1, u2]), z3))
    Eff = cnot(tens(sharpVec(xplus), sharpVec(blochOf(b))))
    lhs = tabMul(tabMul(S1, Eff), tabT(S2))
    rhs = pureTab(sp.diag(1, u) * Matrix([[b[0], b[1]], [b[1], b[0]]]) * sp.diag(1, u2))
    c = None
    for key in rhs:
        if sp.simplify(rhs[key]) != 0:
            c = sp.simplify(lhs[key] / rhs[key])
            break
    prop = c is not None and all(sp.simplify(lhs[k] - c * rhs[k]) == 0 for k in rhs)
    ok_cc |= not prop
check("H6c countercontrol: dropping the conjugation breaks the identity for generic complex b", ok_cc)

# --- coverage: explicit solution for random generic C
ok = True
for _ in range(3):
    C = Matrix(2, 2, lambda i, j: rc())
    w = sp.sqrt(C[0, 1] * C[1, 0] / (C[0, 0] * C[1, 1]))
    s = C[0, 0]
    b = [sp.Integer(1), sp.conjugate(w)]
    up = C[0, 1] / (s * w)
    u = C[1, 0] / (s * w)
    M = s * (sp.diag(1, u) * Matrix([[b[0], b[1]], [b[1], b[0]]]).applyfunc(sp.conjugate) * sp.diag(1, up))
    ok &= (M - C).applyfunc(lambda z: sp.simplify(sp.expand_complex(z))).is_zero_matrix
check("H7 coverage: every C with four nonzero entries is s diag(1,u) conj(Circ b) diag(1,u') (explicit solution)", ok)

# --- chart rule / orientation on the Bell table, and the reflection pairs
def orth_rat(k):
    a, b2, c = (R(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(3))
    S = Matrix([[0, -a, -b2], [a, 0, -c], [b2, c, 0]])
    Q = ((eye(3) - S) * (eye(3) + S).inv()).applyfunc(sp.expand)
    return Q * (REFLY if k else eye(3))


ok = True
for kA, kB in itertools.product([0, 1], repeat=2):
    A, B = orth_rat(kA), orth_rat(kB)
    bell = actC(A, actT(B, phiW))
    q3 = is_psd(pauliW(bell))
    tw = is_psd(pauliW(actT(REFLY, bell)))              # bell in twin  <=>  actT reflY bell in Q3
    orient = (A.det() * B.det() == -1)
    ok &= (tw and not q3) if orient else (q3 and not tw)
check("H8 bellOf A B lies in twistQ3 (orient A B) for the four determinant classes (orient = det A det B = -1)", ok)

# --- self-duality scale: ipW E X = 4 tr(pauliW E pauliW X)
E = {(m, n): sp.Symbol("e%d%d" % (m, n)) for m in R4 for n in R4}
X = {(m, n): sp.Symbol("x%d%d" % (m, n)) for m in R4 for n in R4}
ipw = sum(E[k] * X[k] for k in E)
check("H9 ipW E X = 4 tr(pauliW E . pauliW X) (the Euclidean dual of Q3 is Q3)",
      sp.expand(4 * (pauliW(E) * pauliW(X)).trace() - ipw) == 0)
print("--- precheck_heavy: %d/%d" % (sum(checks), len(checks)))
print("VERDICT PREFLIGHT-HEAVY-EXACT" if all(checks) else "VERDICT NOT RENDERED")
