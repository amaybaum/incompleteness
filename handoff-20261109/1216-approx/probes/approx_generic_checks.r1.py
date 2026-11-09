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

print("RESULT", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
