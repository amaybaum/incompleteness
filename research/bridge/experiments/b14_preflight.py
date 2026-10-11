#!/usr/bin/env python3
"""b14_preflight.py -- node B14 of research/bridge (round 4): exact preflight of the availability module
BridgeAvail.lean ((A) at level H in the kernel's vocabulary: genTheory / InstAvail on the pair carrier).

DECISION RULE (fixed 2026-10-11T03:10:16Z, from `date -u` immediately before writing; before run 1).

Conventions (kernel at L; this tree's verification/ is identical to L). Token operators are 2 x 2 complex matrices.
w = 3/5 + (4/5)i, zPhase = diag(1, w) (the operator of R_z(th0), cos th0 = 3/5); X = [[0,1],[1,0]] (the NOT);
S = diag(1, i) (the quarter phase); U_J = (1 - i(X + Y + Z))/2 (the lift of the kernel's cycEquiv,
KInfFoundations.lean:416, (x, y, z) -> (z, x, y)). pairOp(U, n) = (1 (x) U) (x) 1_n on ((Fin 2 x Fin 2) x Fin n),
index ((a, b), k) -> (2a + b) n + k (the kernel's tensorOf, Prod order); tokOp(U, n) = U (x) 1_n on Fin 2 x Fin n.
The dictionary M(w) = (1/4) sum w_mn s_m (x) s_n, actT N w = w Hom(N)^T, is a comparison tool, never a premise.

CHECKS
  P1  w: |w|^2 = 1, w != 1, w^4 = (-527 - 336 i)/625 != 1; the polynomial certificate used by the module,
      (a + b j)^4 - (A + B j) = e(j) (j^2 + 1) with a = 3/5, b = 4/5, A = -527/625, B = -336/625,
      e = 6 a^2 b^2 + 4 a b^3 j + b^4 (j^2 - 1), holds identically in a formal variable j.
  P2  U_J equals [[(1-i)/2, (-1-i)/2], [(1-i)/2, (1+i)/2]], is unitary, has both first-row entries nonzero; zPhase is
      unitary; U_J = ((1 - i)/sqrt 2) X rot(pi/4) S^3 exactly, rot(t) = [[cos t, -sin t], [sin t, cos t]] (the kernel's
      StateMixingCoupling.rot), so U_J is a unit multiple of a product of members of MixR {pi/4}.
  P3  Through the dictionary, on all 16 basis tables: (1 (x) U_J) M(E) (1 (x) U_J)^* = M(actT cycEquiv E) and
      (1 (x) zPhase) M(E) (1 (x) zPhase)^* = M(actT R_z(th0) E).
  P4  For n = 1, 2, 3: pairOp(U, n) and tokOp(U, n) are unitary for U in {zPhase, X, U_J}; pairOp(zPhase, n) is diagonal
      with diagonal entries in {1, w}, both occurring; the row ((0,0),0) of pairOp(U_J, n) has nonzero entries exactly
      at ((0,0),0) and ((0,1),0); the row (0,0) of tokOp(U_J, n) exactly at (0,0) and (1,0).
  P5  Class invariants on instances, n = 1, 2, 3, a in {1, i, 1/2, (3 - 4i)/5}: a pairOp(zPhase, n) and
      a tokOp(zPhase, n) are not scaled partial permutations (two unequal nonzero entries) and fail QuartEq (two
      nonzero entries with unequal fourth powers); a pairOp(U_J, n) and a tokOp(U_J, n) are not submonomial.
      Countercontrol: pairOp(S, n) is submonomial and satisfies QuartEq. Sampled closure of the MixR {} invariant:
      300 deterministic words (length 1..6) in the generators at the carrier Fin 2 x Fin 2 (the four quarter phases,
      the 24 permutation matrices scaled by c in {1, 1/2, (3+4i)/5}, the two ancilla projectors, the scalars i and
      1/2), and 100 ancilla blocks of words at the carrier (Fin 2 x Fin 2) x Fin 2: every sample is submonomial and
      satisfies QuartEq.
  P6  Product behaviour, exact: pairOp(U, 2) (rho (x) sigma (x) tau) pairOp(U, 2)^* = rho (x) (U sigma U^*) (x) tau for
      U in {zPhase, X, U_J} and fixed non-Hermitian Gaussian-rational rho, sigma, tau.
  P7  NOT control: for n = 1, 2, 3, pairOp(X, n) is the permutation matrix of ((a, b), k) -> ((a, 1 - b), k): entries
      0/1, one nonzero per row and column.
  P8  Monomial interface: for n = 1, 2, 3, pairOp(zPhase, n) has one nonzero entry per row and column (monomial);
      pairOp(U_J, n) does not.

VERDICT B14-PREFLIGHT-OK iff P1-P8 all PASS; otherwise VERDICT B14-PREFLIGHT-FAILED followed by the failing ids.

Pre-run edit 2026-10-11T03:11:13Z (before run 1; rule text unchanged): P1 compares w^4 with (-527 - 336 i)/625 by
expanding the difference, instead of a structural equality of two sympy expressions.
"""
import sys
from itertools import product

import sympy as sp

PASS, FAIL = [], []


def check(cid, ok, msg=""):
    print(f"{cid:4s} {'PASS' if ok else 'FAIL'}  {msg}")
    (PASS if ok else FAIL).append(cid)


I = sp.I
R = sp.Rational
w = R(3, 5) + R(4, 5) * I
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
E2 = sp.eye(2)
zPh = sp.diag(1, w)
S = sp.diag(1, I)
UJ = (E2 - I * (X + Y + Z)) / 2
SIG = [E2, X, Y, Z]


def ex(M):
    return M.applyfunc(lambda z: sp.expand(z))


def iszero(M):
    return all(sp.expand(z) == 0 for z in M)


def dag(M):
    return M.conjugate().T


def kron(A, B):
    return sp.kronecker_product(A, B)


# ---------------- P1 ----------------
w4 = sp.expand(w ** 4)
j = sp.Symbol("j")
a_, b_ = R(3, 5), R(4, 5)
A_, B_ = R(-527, 625), R(-336, 625)
e_ = 6 * a_**2 * b_**2 + 4 * a_ * b_**3 * j + b_**4 * (j**2 - 1)
cert = sp.expand((a_ + b_ * j) ** 4 - (A_ + B_ * j) - e_ * (j**2 + 1))
ok1 = (sp.expand(w * sp.conjugate(w)) == 1 and sp.expand(w - 1) != 0 and sp.expand(w4 - (A_ + B_ * I)) == 0
       and sp.expand(w4 - 1) != 0 and cert == 0)
check("P1", ok1, f"|w|^2 = {sp.expand(w * sp.conjugate(w))}, w^4 = {w4}, certificate residue = {cert}")

# ---------------- P2 ----------------
UJ_lit = sp.Matrix([[(1 - I) / 2, (-1 - I) / 2], [(1 - I) / 2, (1 + I) / 2]])
c4 = sp.cos(sp.pi / 4)
s4 = sp.sin(sp.pi / 4)
rot4 = sp.Matrix([[c4, -s4], [s4, c4]])
fac = ex(((1 - I) / sp.sqrt(2)) * X * rot4 * S ** 3)
ok2 = (iszero(UJ - UJ_lit) and iszero(dag(UJ) * UJ - E2) and UJ[0, 0] != 0 and UJ[0, 1] != 0
       and iszero(dag(zPh) * zPh - E2) and iszero(fac - UJ))
check("P2", ok2, f"U_J = {list(UJ_lit)}, ((1-i)/sqrt2) X rot(pi/4) S^3 = {list(fac)}")


# ---------------- P3 ----------------
def M_of(wt):
    out = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if wt[m][n] != 0:
                out += R(1, 4) * wt[m][n] * kron(SIG[m], SIG[n])
    return out


def Hom(N):
    H = sp.zeros(4, 4)
    H[0, 0] = 1
    for i in range(3):
        for k in range(3):
            H[i + 1, k + 1] = N[i][k]
    return H


def actT(N, wt):
    W = sp.Matrix(wt) * Hom(N).T
    return [[W[i, k] for k in range(4)] for i in range(4)]


cyc = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
Rth = [[R(3, 5), R(-4, 5), 0], [R(4, 5), R(3, 5), 0], [0, 0, 1]]
okJ = okR = True
for m in range(4):
    for n in range(4):
        Et = [[1 if (r, c) == (m, n) else 0 for c in range(4)] for r in range(4)]
        VJ = kron(E2, UJ)
        VR = kron(E2, zPh)
        okJ &= iszero(VJ * M_of(Et) * dag(VJ) - M_of(actT(cyc, Et)))
        okR &= iszero(VR * M_of(Et) * dag(VR) - M_of(actT(Rth, Et)))
check("P3", okJ and okR, f"Ad(1 x U_J) = actT cycEquiv: {okJ}; Ad(1 x diag(1,w)) = actT R_z(th0): {okR}")


# ---------------- P4 ----------------
def pairOp(U, n):
    return kron(kron(E2, U), sp.eye(n))


def tokOp(U, n):
    return kron(U, sp.eye(n))


def pidx(a, b, k, n):
    return (2 * a + b) * n + k


ok4 = True
for n in (1, 2, 3):
    for U in (zPh, X, UJ):
        for V in (pairOp(U, n), tokOp(U, n)):
            ok4 &= iszero(dag(V) * V - sp.eye(V.shape[0]))
    P = pairOp(zPh, n)
    offd = all(P[r, c] == 0 for r in range(P.shape[0]) for c in range(P.shape[0]) if r != c)
    dg = set(sp.expand(P[r, r]) for r in range(P.shape[0]))
    ok4 &= offd and dg == {1, w}
    PJ = pairOp(UJ, n)
    row = [c for c in range(PJ.shape[0]) if PJ[pidx(0, 0, 0, n), c] != 0]
    ok4 &= row == sorted([pidx(0, 0, 0, n), pidx(0, 1, 0, n)])
    TJ = tokOp(UJ, n)
    rowt = [c for c in range(TJ.shape[0]) if TJ[0, c] != 0]
    ok4 &= rowt == sorted([0 * n + 0, 1 * n + 0])
check("P4", ok4, "unitarity, the diagonal of pairOp(zPhase, n), the two nonzero entries of the U_J rows (n = 1, 2, 3)")


# ---------------- P5 ----------------
def nonzero(M):
    return [(r, c) for r in range(M.shape[0]) for c in range(M.shape[1]) if sp.expand(M[r, c]) != 0]


def submonomial(M):
    nz = nonzero(M)
    rows = [r for r, _ in nz]
    cols = [c for _, c in nz]
    return len(set(rows)) == len(rows) and len(set(cols)) == len(cols)


def scaled_pp(M):
    vals = set(sp.expand(M[r, c]) for r, c in nonzero(M))
    return submonomial(M) and len(vals) <= 1


def quart(M):
    vals = set(sp.expand(M[r, c] ** 4) for r, c in nonzero(M))
    return len(vals) <= 1


ok5 = True
for n in (1, 2, 3):
    for a in (1, I, R(1, 2), (3 - 4 * I) / 5):
        for V in (pairOp(zPh, n), tokOp(zPh, n)):
            aV = ex(a * V)
            ok5 &= (not scaled_pp(aV)) and (not quart(aV))
        for V in (pairOp(UJ, n), tokOp(UJ, n)):
            ok5 &= not submonomial(ex(a * V))
    PS = pairOp(S, n)
    ok5 &= submonomial(PS) and quart(PS)


def phaseGate(p, dim):
    return sp.diag(*[I if q == p else 1 for q in range(dim)])


def permM(perm, c):
    M = sp.zeros(len(perm), len(perm))
    for j_, i_ in enumerate(perm):
        M[i_, j_] = c
    return M


def projAnc(k, dim):  # carrier T x Fin 2, index 2t + r: the projector onto r = k
    return sp.diag(*[1 if (q % 2) == k else 0 for q in range(dim)])


def gens(dim):
    g = [phaseGate(p, dim) for p in range(dim)]
    from itertools import permutations
    perms = list(permutations(range(dim))) if dim <= 4 else [tuple((i + s) % dim for i in range(dim)) for s in range(dim)] + [tuple(dim - 1 - i for i in range(dim))]
    for pm in perms:
        for c in (1, R(1, 2), (3 + 4 * I) / 5):
            g.append(permM(pm, c))
    g.append(projAnc(0, dim))
    g.append(projAnc(1, dim))
    g.append(I * sp.eye(dim))
    g.append(R(1, 2) * sp.eye(dim))
    return g


state = 20261011


def rnd(m):
    global state
    state = (1103515245 * state + 12345) % (2 ** 31)
    return state % m


G4 = gens(4)
G8 = gens(8)
samples_ok = True
for t in range(300):
    L = 1 + rnd(6)
    M = sp.eye(4)
    for _ in range(L):
        M = ex(M * G4[rnd(len(G4))])
    samples_ok &= submonomial(M) and quart(M)
for t in range(100):
    L = 1 + rnd(6)
    M = sp.eye(8)
    for _ in range(L):
        M = ex(M * G8[rnd(len(G8))])
    f, e_ = rnd(2), rnd(2)
    B = sp.Matrix(4, 4, lambda s, u: M[2 * s + f, 2 * u + e_])
    samples_ok &= submonomial(B) and quart(B)
check("P5", ok5 and samples_ok,
      f"refutation instances: {ok5}; 300 words at Fin 2 x Fin 2 and 100 blocks from (Fin 2 x Fin 2) x Fin 2: {samples_ok}")

# ---------------- P6 ----------------
rho = sp.Matrix([[1, 2 + I], [3 - I, R(1, 2)]])
sig = sp.Matrix([[2, I], [-3 * I, R(5, 7)]])
tau = sp.Matrix([[1, R(2, 3)], [-1, 4 + I]])
ok6 = True
for U in (zPh, X, UJ):
    V = pairOp(U, 2)
    lhs = ex(V * kron(kron(rho, sig), tau) * dag(V))
    rhs = ex(kron(kron(rho, U * sig * dag(U)), tau))
    ok6 &= iszero(lhs - rhs)
check("P6", ok6, "conj((1 x U) x 1)(rho x sigma x tau) = rho x (U sigma U*) x tau for zPhase, X, U_J")

# ---------------- P7 ----------------
ok7 = True
for n in (1, 2, 3):
    P = pairOp(X, n)
    dim = P.shape[0]
    target = sp.zeros(dim, dim)
    for a, b, k in product(range(2), range(2), range(n)):
        target[pidx(a, 1 - b, k, n), pidx(a, b, k, n)] = 1
    vals = set(P[r, c] for r in range(dim) for c in range(dim))
    ok7 &= iszero(P - target) and vals <= {0, 1} and submonomial(P)
check("P7", ok7, "pairOp(X, n) is the permutation ((a, b), k) -> ((a, 1 - b), k), n = 1, 2, 3")

# ---------------- P8 ----------------
ok8 = True
for n in (1, 2, 3):
    ok8 &= submonomial(pairOp(zPh, n)) and len(nonzero(pairOp(zPh, n))) == 4 * n
    ok8 &= not submonomial(pairOp(UJ, n))
check("P8", ok8, "pairOp(zPhase, n) monomial (4n nonzero entries, one per row and column); pairOp(U_J, n) not")

if FAIL:
    print("VERDICT B14-PREFLIGHT-FAILED " + " ".join(FAIL))
    sys.exit(1)
print("VERDICT B14-PREFLIGHT-OK")
