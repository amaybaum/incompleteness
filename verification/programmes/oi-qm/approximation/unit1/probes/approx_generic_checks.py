#!/usr/bin/env python3
"""OI-QM-APPROX-1 unit 1 -- labelled EXACT GENERIC CHECKS (paper-only unit, #1216).

Scope: generic mathematical objects only (2x2 / 4x4 matrices, permutations of small
finite sets, signed permutation matrices in SO(3)).  No OI mechanism is constructed,
simulated or evaluated.  Imports nothing from the repository or from earlier probes.
Exact arithmetic throughout (sympy rationals / algebraic numbers, fractions.Fraction).

Run:  python3 -I -B approx_generic_checks.py      (exit 0 iff every check and control holds)

G1  On a two-state carrier, every diagonal trace-one Hermitian D satisfies
    || |+><+| - D ||_1 >= 1, with equality at D = I/2; and every real symmetric trace-one
    R satisfies || |+i><+i| - R ||_1 >= 1.  Countercontrol: an off-diagonal (non-diagonal)
    candidate reaches 0, so the bound is not vacuous.
G2  Any bijection phi of a finite set S has phi^L = id for L = lcm(1..|S|), so the law
    after K applications from any fixed initial law is L-periodic in K (checked on random
    bijections, exact Fractions).  The qubit law p_K = cos^2(K*pi/(2L)) has p_L = 0 and
    p_{2L} = 1 (exact).  Countercontrol: a non-bijective stochastic map gives a law that is
    not L-periodic.
G3  Tetrahedral frame a_i = v_i/sqrt3, v in {(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)}:
    a rotation O acts on frame coordinates p_i = (1 + a_i.r)/4 by M_ij = (1 + v_i.O v_j)/4.
    The 12 rotations of A4 give permutation matrices (nonnegative); every one of the 12
    remaining octahedral (Clifford) rotations, e.g. the Hadamard rotation and the quarter
    turn about z, has an entry -1/2.  Control: the identity map M = I is reproduced.
G4  Composite, configuration carrier: for x+ (x) z+ on C^2 (x) C^2 and EVERY diagonal D,
    tr((rho - D)(X(x)Z)) = 1, so ||rho - D||_1 >= 1; likewise y+ (x) z+ with Y(x)Z.  Control: a
    diagonal state (z+ (x) z+) is at distance 0 from the diagonal set.
G5  Composite, tetrahedral product frame (E_i = (I + a_i.sigma)/4, dual D_k = (I + 3 a_k.sigma)/2):
    (a) frame coordinates of the entangled state Phi+ are all >= 0 (states are representable);
    (b) the frame matrix of CNOT conjugation has a negative entry (exact value printed);
    (c) control: the frame matrix of a local A4 rotation (x) identity is nonnegative;
    (d) a point mass on one ontic pair reconstructs D_k (x) D_l, which is not PSD
        (valid nonnegative frame distribution, outside the quantum state space).
"""
import itertools
import random
import sys
from fractions import Fraction
from math import lcm

import sympy as sp

FAIL = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


# ---------------------------------------------------------------- G1
a, c, r = sp.symbols('a c r', real=True)
plus = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
D = sp.diag(a, 1 - a)
A = plus - D
ev = list(A.eigenvals().keys())
# eigenvalues are +-sqrt((a-1/2)^2 + 1/4): trace norm = 2*sqrt((a-1/2)^2+1/4) >= 1
tn_closed = 2 * sp.sqrt((a - sp.Rational(1, 2)) ** 2 + sp.Rational(1, 4))
# A is Hermitian and traceless, so its eigenvalues are +-sqrt(-det A) and ||A||_1 = 2 sqrt(-det A).
# (r0 of this script tested sympy's Abs-simplification here and failed for that reason only.)
check("G1a |+><+| - diag(a,1-a) is traceless with -det = (a-1/2)^2 + 1/4, so trace norm = 2*sqrt((a-1/2)^2+1/4)",
      sp.simplify(A.trace()) == 0
      and sp.simplify(sp.expand(-A.det()) - ((a - sp.Rational(1, 2)) ** 2 + sp.Rational(1, 4))) == 0)
check("G1b minimum over a is 1, attained at a = 1/2",
      tn_closed.subs(a, sp.Rational(1, 2)) == 1 and sp.solve(sp.Eq(tn_closed, sp.Rational(1, 1) - sp.Rational(1, 10)), a) == [])
plusi = sp.Matrix([[sp.Rational(1, 2), -sp.I / 2], [sp.I / 2, sp.Rational(1, 2)]])
R = sp.Matrix([[a, r], [r, 1 - a]])
B = plusi - R
evB = B.eigenvals()
# B is Hermitian, traceless: eigenvalues +-sqrt(det(-B)); |B|_1 = 2 sqrt(-det B)
negdet = sp.expand(-B.det())
check("G1c -det(|+i><+i| - R) = (a-1/2)^2 + r^2 + 1/4 >= 1/4, so trace norm >= 1",
      sp.simplify(negdet - ((a - sp.Rational(1, 2)) ** 2 + r ** 2 + sp.Rational(1, 4))) == 0)
check("G1d countercontrol: the non-diagonal candidate |+><+| itself is at distance 0",
      (plus - plus).norm() == 0)

# ---------------------------------------------------------------- G2
random.seed(20261109)
ok_period = True
for n in range(2, 8):
    L = lcm(*range(1, n + 1))
    for _ in range(25):
        perm = list(range(n))
        random.shuffle(perm)
        w = [Fraction(random.randint(0, 9)) for _ in range(n)]
        s = sum(w)
        if s == 0:
            w[0] = Fraction(1); s = Fraction(1)
        mu0 = [x / s for x in w]

        def push(mu):
            out = [Fraction(0)] * n
            for i, m in enumerate(mu):
                out[perm[i]] += m
            return out
        laws = [mu0]
        for _k in range(2 * L + 3):
            laws.append(push(laws[-1]))
        ok_period &= all(laws[k] == laws[k + L] for k in range(L + 3))
check("G2a every random bijection on |S|<=7 gives an L-periodic law, L = lcm(1..|S|)", ok_period)
for L in (2, 6, 60, 420):
    pL = sp.cos(L * sp.pi / (2 * L)) ** 2
    p2L = sp.cos(2 * L * sp.pi / (2 * L)) ** 2
    check(f"G2b qubit law cos^2(K pi/(2L)) at L={L}: p_L = 0, p_2L = 1", sp.simplify(pL) == 0 and sp.simplify(p2L) == 1)
# countercontrol: stochastic, non-bijective map on 2 states; law not periodic
T = [[Fraction(3, 4), Fraction(1, 4)], [Fraction(1, 4), Fraction(3, 4)]]
mu = [Fraction(1), Fraction(0)]
seq = [mu]
for _ in range(6):
    m = seq[-1]
    seq.append([m[0] * T[0][0] + m[1] * T[1][0], m[0] * T[0][1] + m[1] * T[1][1]])
check("G2c countercontrol: a non-bijective stochastic map gives a law with no period <= 2 (L=lcm(1,2))",
      seq[0] != seq[2] and seq[1] != seq[3])

# ---------------------------------------------------------------- G3
V = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def apply(O, v):
    return tuple(sum(O[i][j] * v[j] for j in range(3)) for i in range(3))


def frame_matrix(O):
    return [[Fraction(1 + dot(V[i], apply(O, V[j])), 4) for j in range(4)] for i in range(4)]


def det3(O):
    return sp.Matrix(O).det()


rots = []
for p in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        O = [[0] * 3 for _ in range(3)]
        for i in range(3):
            O[i][p[i]] = sg[i]
        if det3(O) == 1:
            rots.append(O)
check("G3a there are 24 signed-permutation rotations (octahedral group)", len(rots) == 24)
nonneg, negs = [], []
for O in rots:
    M = frame_matrix(O)
    mn = min(min(row) for row in M)
    (nonneg if mn >= 0 else negs).append((O, M, mn))
perm_like = all(sorted(sum(row) for row in M) == [1] * 4 and all(x in (0, 1) for row in M for x in row)
                for _, M, _ in nonneg)
check("G3b exactly 12 rotations (A4) give nonnegative frame matrices, each a permutation matrix",
      len(nonneg) == 12 and perm_like)
check("G3c each of the other 12 octahedral (Clifford) rotations has a frame entry -1/2",
      len(negs) == 12 and all(mn == Fraction(-1, 2) for _, _, mn in negs))
H = [[0, 0, 1], [0, -1, 0], [1, 0, 0]]          # Hadamard: x<->z, y->-y
Sz = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]          # quarter turn about z (phase gate S)
check("G3d the Hadamard rotation and the S rotation are among the negative ones",
      min(min(row) for row in frame_matrix(H)) == Fraction(-1, 2)
      and min(min(row) for row in frame_matrix(Sz)) == Fraction(-1, 2))
I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
check("G3e control: identity rotation gives the identity frame matrix",
      frame_matrix(I3) == [[Fraction(int(i == j)) for j in range(4)] for i in range(4)])

# ---------------------------------------------------------------- G4
X2 = sp.Matrix([[0, 1], [1, 0]]); Y2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z2 = sp.diag(1, -1); I2 = sp.eye(2)
kp = sp.kronecker_product
xp = sp.Matrix([1, 1]) / sp.sqrt(2); yp = sp.Matrix([1, sp.I]) / sp.sqrt(2); zp = sp.Matrix([1, 0])
d0, d1, d2, d3 = sp.symbols('d0:4')
Dg = sp.diag(d0, d1, d2, d3)
for name, st, W in (("x+ (x) z+", kp(xp, zp), kp(X2, Z2)), ("y+ (x) z+", kp(yp, zp), kp(Y2, Z2))):
    rho = st * st.H
    val = sp.simplify(((rho - Dg) * W).trace())
    check(f"G4 tr((rho - D) W) = 1 for {name} and every diagonal D (so trace distance >= 1/2)", val == 1)
zz = kp(zp, zp) * kp(zp, zp).H
check("G4 control: z+ (x) z+ is itself diagonal", zz == sp.diag(*[zz[i, i] for i in range(4)]))

# ---------------------------------------------------------------- G5
s3 = sp.sqrt(3)
avec = [sp.Matrix(v) / s3 for v in V]
def sdot(av):
    return av[0] * X2 + av[1] * Y2 + av[2] * Z2
Ef = [(I2 + sdot(av)) / 4 for av in avec]
Df = [(I2 + 3 * sdot(av)) / 2 for av in avec]
check("G5 frame identities: sum E_i = I and tr(E_i D_k) = delta_ik",
      sp.simplify(sum(Ef, sp.zeros(2)) - I2) == sp.zeros(2)
      and all(sp.simplify((Ef[i] * Df[k]).trace() - (1 if i == k else 0)) == 0 for i in range(4) for k in range(4)))
phi = (kp(sp.Matrix([1, 0]), sp.Matrix([1, 0])) + kp(sp.Matrix([0, 1]), sp.Matrix([0, 1]))) / sp.sqrt(2)
rphi = phi * phi.H
pj = [sp.nsimplify(sp.simplify((rphi * kp(Ef[i], Ef[j])).trace())) for i in range(4) for j in range(4)]
check("G5a every joint frame coordinate of Phi+ is >= 0 (and they sum to 1)",
      all(sp.simplify(x) >= 0 for x in pj) and sp.simplify(sum(pj)) == 1)
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
# Frame matrix by Pauli transfer (exact, no simplify): E_i (x) E_j = (1/16) sum_{P,Q} e_i^P e_j^Q P(x)Q,
# D_k (x) D_l = (1/4) sum_{R,S} d_k^R d_l^S R(x)S, tr(P(x)Q . U(R(x)S)U^dag) = 4 * sign if the Clifford image
# of R(x)S is sign * P(x)Q.  e^I = d^I = 1, e^c = a_c = v_c/sqrt3, d^c = 3 a_c = sqrt3 v_c.
PA = {'I': I2, 'x': X2, 'y': Y2, 'z': Z2}
labels = list(PA)
def ecoef(i, P):
    return 1 if P == 'I' else sp.Integer(V[i]['xyz'.index(P)]) / s3
def dcoef(k, R):
    return 1 if R == 'I' else s3 * V[k]['xyz'.index(R)]
def image(U, R, S):
    M = U * kp(PA[R], PA[S]) * U.H
    for P in labels:
        for Q in labels:
            t = sp.expand((M * kp(PA[P], PA[Q])).trace() / 4)
            if t != 0:
                return P, Q, t
    raise ValueError
def frame_mat(U):
    img = {(R, S): image(U, R, S) for R in labels for S in labels}
    assert all(t in (1, -1) for (_, _, t) in img.values())
    M = sp.zeros(16, 16)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    tot = 0
                    for (R, S), (P, Q, t) in img.items():
                        tot += t * dcoef(k, R) * dcoef(l, S) * ecoef(i, P) * ecoef(j, Q)
                    M[4 * i + j, 4 * k + l] = sp.nsimplify(sp.expand(tot / 16))
    return M
Mid = frame_mat(sp.eye(4))
check("G5 control: identity's frame matrix is the 16x16 identity", Mid == sp.eye(16))
Mcn = frame_mat(CN)
mn = min(Mcn, key=lambda e: sp.N(e, 30))
print("     CNOT frame matrix: minimum entry =", mn, "~", sp.N(mn, 8))
check("G5b the CNOT frame matrix has a negative entry", bool(mn < 0))
# local A4 rotation: the qubit unitary of the 3-cycle x->y->z->x is (I - i(X+Y+Z))/2 up to phase
U3 = (I2 - sp.I * (X2 + Y2 + Z2)) / 2
check("G5 control prerequisite: (I - i(X+Y+Z))/2 is unitary", sp.expand(U3 * U3.H - I2) == sp.zeros(2))
Mloc = frame_mat(kp(U3, I2))
check("G5c control: frame matrix of (3-cycle rotation) (x) I is a nonnegative permutation matrix",
      all(x in (0, 1) for x in Mloc) and all(sum(Mloc[r, c] for c in range(16)) == 1 for r in range(16)))
ev = kp(Df[0], Df[0]).eigenvals()
check("G5d point mass on one ontic pair reconstructs D_0 (x) D_0, which has a negative eigenvalue",
      any(sp.N(e) < 0 for e in ev))

print("RESULT", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
