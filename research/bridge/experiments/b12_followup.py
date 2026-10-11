#!/usr/bin/env python3
"""b12_followup.py -- node B12 of research/bridge (round 3), follow-up to b12_stagecross.py: the rest of S0-5's
registered range (m = 17..24) with controls for the minimal-polynomial test, and the icosahedral group that holds
J and R_z(pi) (the check that decides a draft sentence of NOTES-B12 Sec. 3).

DECISION RULE (fixed 2026-10-11T00:56:10Z, from `date -u` immediately before writing; before run 1).

Conventions as in b12_stagecross.py: J = cyc3 = [[0,0,1],[1,0,0],[0,1,0]] (J e_z = e_x), R_z(t) the rotation about
the third axis, rotations act on column vectors. phi = (1 + sqrt 5)/2. Arithmetic in Q(sqrt 5) is exact: a pair
(a, b) of Fractions stands for a + b sqrt 5.

CHECKS
  V1  For m = 17..24: tr(J R_z(2 pi/m)) + sin(2 pi/m) simplifies to 0, and the minimal polynomial of
      -1 - sin(2 pi/m) (sympy, primitive over Z) has leading coefficient different from +-1 (not an algebraic
      integer). Positive control: the minimal polynomial of 2 cos(2 pi/m) has leading coefficient +-1 for every
      m = 1..24. Countercontrol: the minimal polynomial of cos(2 pi/m) has leading coefficient +-1 exactly for
      m in {1, 2, 4} among m = 1..24.
  V2  u = (phi - 1, phi, 1)/2 is a unit vector; R_u = 2 u u^T - 1 has R_u R_u^T = 1, det R_u = 1, R_u^2 = 1,
      R_u != 1. The closure G = <J, R_z(pi), R_u> (BFS, capped at 1000 elements) has exactly 60 elements, contains
      J and R_z(pi), and exactly 2 of its elements fix e_z (1 and R_z(pi)).
  V3  In the same Q(sqrt 5) arithmetic: |<J, R_z(pi)>| = 12 and |<J, R_z(pi/2)>| = 24.

VERDICT B12F-EXACT iff V1-V3 all PASS; otherwise VERDICT B12F-FAILED followed by the failing ids.
"""
from fractions import Fraction as F

import sympy as sp

PASS, FAIL = [], []


def check(cid, ok, msg=""):
    print(f"{cid:4s} {'PASS' if ok else 'FAIL'}  {msg}")
    (PASS if ok else FAIL).append(cid)


# ---------------- V1 ----------------
x = sp.symbols("x")
Jm = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def lc_is_unit(expr):
    mp = sp.Poly(sp.minimal_polynomial(expr, x), x)
    return abs(mp.LC()) == 1


trace_ok = True
nonint = []
for m in range(17, 25):
    ang = 2 * sp.pi / m
    R = sp.Matrix([[sp.cos(ang), -sp.sin(ang), 0], [sp.sin(ang), sp.cos(ang), 0], [0, 0, 1]])
    trace_ok &= sp.simplify((Jm * R).trace() + sp.sin(ang)) == 0
    if not lc_is_unit(-1 - sp.sin(ang)):
        nonint.append(m)
pos = [m for m in range(1, 25) if lc_is_unit(2 * sp.cos(2 * sp.pi / m))]
neg = [m for m in range(1, 25) if lc_is_unit(sp.cos(2 * sp.pi / m))]
check("V1", trace_ok and nonint == list(range(17, 25)) and pos == list(range(1, 25)) and neg == [1, 2, 4],
      f"tr(J R_z(2pi/m)) = -sin(2pi/m) for m = 17..24: {trace_ok}; -1 - sin(2pi/m) not an algebraic integer for "
      f"m in {nonint}; control 2cos(2pi/m) integral for m in 1..24: {pos == list(range(1, 25))}; "
      f"countercontrol cos(2pi/m) integral exactly for m in {neg}")


# ---------------- Q(sqrt 5) ----------------
def q(a, b=0): return (F(a), F(b))
def qadd(p, r): return (p[0] + r[0], p[1] + r[1])
def qsub(p, r): return (p[0] - r[0], p[1] - r[1])
def qmul(p, r): return (p[0] * r[0] + 5 * p[1] * r[1], p[0] * r[1] + p[1] * r[0])
ZERO, ONE = q(0), q(1)
PHI = (F(1, 2), F(1, 2))


def M(rows): return tuple(tuple(q(c) if not isinstance(c, tuple) else c for c in r) for r in rows)
def mmul(A, B):
    return tuple(tuple(
        qadd(qadd(qmul(A[i][0], B[0][j]), qmul(A[i][1], B[1][j])), qmul(A[i][2], B[2][j]))
        for j in range(3)) for i in range(3))
def mT(A): return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))
def mdet(A):
    t1 = qmul(A[0][0], qsub(qmul(A[1][1], A[2][2]), qmul(A[1][2], A[2][1])))
    t2 = qmul(A[0][1], qsub(qmul(A[1][0], A[2][2]), qmul(A[1][2], A[2][0])))
    t3 = qmul(A[0][2], qsub(qmul(A[1][0], A[2][1]), qmul(A[1][1], A[2][0])))
    return qadd(qsub(t1, t2), t3)


I3 = M([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
J = M([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
RZPI = M([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
RZHALF = M([[0, -1, 0], [1, 0, 0], [0, 0, 1]])


def closure(gens, cap=1000):
    seen = {I3}
    frontier = [I3]
    while frontier and len(seen) <= cap:
        nxt = []
        for A in frontier:
            for g in gens:
                B = mmul(g, A)
                if B not in seen:
                    seen.add(B)
                    nxt.append(B)
        frontier = nxt
    return seen


# ---------------- V2 ----------------
half = q(F(1, 2))
u = (qmul(qsub(PHI, ONE), half), qmul(PHI, half), half)
unorm = qadd(qadd(qmul(u[0], u[0]), qmul(u[1], u[1])), qmul(u[2], u[2]))
Ru = tuple(tuple(qsub(qmul(q(2), qmul(u[i], u[j])), ONE if i == j else ZERO) for j in range(3)) for i in range(3))
rot_ok = (unorm == ONE and mmul(Ru, mT(Ru)) == I3 and mdet(Ru) == ONE and mmul(Ru, Ru) == I3 and Ru != I3)
G = closure([J, RZPI, Ru])
ez_fix = [g for g in G if (g[0][2], g[1][2], g[2][2]) == (ZERO, ZERO, ONE)]
check("V2", rot_ok and len(G) == 60 and J in G and RZPI in G and len(ez_fix) == 2 and RZPI in ez_fix,
      f"R_u a half-turn with entries in Q(sqrt5): {rot_ok}; |<J, R_z(pi), R_u>| = {len(G)}; contains J and "
      f"R_z(pi): {J in G and RZPI in G}; elements fixing e_z: {len(ez_fix)}")

# ---------------- V3 ----------------
oT, oO = len(closure([J, RZPI])), len(closure([J, RZHALF]))
check("V3", (oT, oO) == (12, 24), f"|<J, R_z(pi)>| = {oT}; |<J, R_z(pi/2)>| = {oO}")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B12F-EXACT" if not FAIL else "VERDICT B12F-FAILED " + " ".join(FAIL))
