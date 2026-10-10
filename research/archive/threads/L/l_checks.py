#!/usr/bin/env python3
"""Thread L exact checks: every concrete identity, every linear_combination certificate in
OrbitGeneration.lean (draft), and every countermodel of the omitted-premise list.

Exact arithmetic only: sympy polynomial identities over Q, and fractions.Fraction instances.
Run:  PYTHONDONTWRITEBYTECODE=1 python3 l_checks.py
"""
import itertools
from fractions import Fraction as Fr

import sympy as sp

CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))
    print(('OK   ' if cond else 'FAIL ') + name)


def zero_poly(expr):
    return sp.expand(expr) == 0


# ---------------------------------------------------------------- symbols
u0, u1, u2, w0, w1, w2, v0, v1, v2, d0, d1, d2 = sp.symbols('u0 u1 u2 w0 w1 w2 v0 v1 v2 d0 d1 d2')
a0, a1, a2, c, k, A, D, x0, b0, b1, b2, t = sp.symbols('a0 a1 a2 c k A D x0 b0 b1 b2 t')
u = [u0, u1, u2]
w = [w0, w1, w2]
v = [v0, v1, v2]
d = [d0, d1, d2]
a = [a0, a1, a2]
b = [b0, b1, b2]


def dot(p, q):
    return sum(pi * qi for pi, qi in zip(p, q))


def ballEffect(bb, vv):
    return sp.Rational(1, 2) + dot(bb, vv) / 2


S_b = dot(b, b)

# ------------------------------------------------- A. ballEffect normalisation
# ballEffect_self: goal ballEffect b b = 1 ; certificate (1/2) * (S - 1)
check('A1 ballEffect_self: 1/2+S/2-1 - (1/2)(S-1) == 0',
      zero_poly(ballEffect(b, b) - 1 - sp.Rational(1, 2) * (S_b - 1)))
# ballEffect_neg_self: goal ballEffect b (-b) = 0 ; certificate (-1/2) * (S - 1)
check('A2 ballEffect_neg_self: 1/2-S/2-0 - (-1/2)(S-1) == 0',
      zero_poly(ballEffect(b, [-bi for bi in b]) - 0 - sp.Rational(-1, 2) * (S_b - 1)))
# conePair_ballEffect: x0*e(0) + (e(v) - e(0)) = (x0 + b.v)/2
e0 = ballEffect(b, [0, 0, 0])
check('A3 conePair_ballEffect identity',
      zero_poly(x0 * e0 + (ballEffect(b, v) - e0) - (x0 + dot(b, v)) / 2))

# ------------------------------------------------- B. Householder certificates
q_d = dot(d, d)


def hh(dd, kk, vv):
    s = dot(dd, vv)
    return [vv[i] - 2 * kk * s * dd[i] for i in range(3)]


Hv = hh(d, k, v)
hk_expr = q_d * k - 1           # hk : q * k = 1
check('B1 hhFun_dot: d.Hv + d.v - (-2 d.v) * (q k - 1) == 0',
      zero_poly(dot(d, Hv) + dot(d, v) - (-2 * dot(d, v)) * hk_expr))
check('B2 hhFun_normSq: |Hv|^2 - |v|^2 - (4 k (d.v)^2) * (q k - 1) == 0',
      zero_poly(dot(Hv, Hv) - dot(v, v) - (4 * k * dot(d, v) ** 2) * hk_expr))
# B3 involution after rw key: H(Hv)_i with d.Hv replaced by -(d.v)
s = dot(d, v)
for i in range(3):
    expr = (Hv[i] - 2 * k * (-s) * d[i]) - v[i]
    check(f'B3.{i} hhFun_hhFun coordinate {i} (ring after rw key)', zero_poly(expr))
# B4 swap: d = u - w, hu : |u|^2 = 1, hw : |w|^2 = 1, hk : q k = 1
dd = [u[i] - w[i] for i in range(3)]
Hu = hh(dd, k, u)
hk2 = dot(dd, dd) * k - 1
hu_e = dot(u, u) - 1
hw_e = dot(w, w) - 1
for i in range(3):
    di = u[i] - w[i]
    expr = (Hu[i] - w[i]) - ((-di) * hk2 + (-di * k) * hu_e + (di * k) * hw_e)
    check(f'B4.{i} hhFun_swap coordinate {i} certificate', zero_poly(expr))
# B5 linearity of hhFun
v_ = sp.symbols('y0 y1 y2')
r_ = sp.Symbol('r')
lin_ok = all(zero_poly(hh(d, k, [v[i] + v_[i] for i in range(3)])[j]
                       - hh(d, k, v)[j] - hh(d, k, list(v_))[j]) for j in range(3))
smul_ok = all(zero_poly(hh(d, k, [r_ * vi for vi in v])[j] - r_ * hh(d, k, v)[j]) for j in range(3))
check('B5 hhLin map_add and map_smul', lin_ok and smul_ok)

# ------------------------------------------------- C. the sharp-form lemma (ball3_sharp_eq)
# r v = c + v.a.  Facts: F1 c + u.a = 1, F2 c - u.a >= 0, F3 c + w.a = 0, F4 c - w.a <= 1.
# c = 1/2 by linarith: F1 + F2 give 2c >= 1, F3 + F4 give 2c <= 1.
# The test point p = 4 k a, k = 1/D, D = 1 + 4A, A = |a|^2.
check('C1 D^2 - 16A == (1 - 4A)^2', zero_poly((1 + 4 * A) ** 2 - 16 * A - (1 - 4 * A) ** 2))
pa = [4 * a[i] * k for i in range(3)]
check('C2 |p|^2 == 16 A k^2 (A = |a|^2)', zero_poly(dot(pa, pa) - 16 * dot(a, a) * k ** 2))
check('C3 r(p) == c + 4 k A', zero_poly(c + dot(pa, a) - (c + 4 * k * dot(a, a))))
# with c = 1/2, r(p) <= 1 gives 4 k A <= 1/2; times D (D k = 1): 4A <= D/2 = (1+4A)/2, A <= 1/4
check('C4 (4 k A) * D == 4 A when D k = 1 : 4kA*D - 4A - 4A*(D k - 1) == 0',
      zero_poly(4 * k * A * D - 4 * A - 4 * A * (D * k - 1)))
check('C5 |2a - u|^2 == 4A - 4 u.a + |u|^2',
      zero_poly(sum((2 * a[i] - u[i]) ** 2 for i in range(3)) - (4 * dot(a, a) - 4 * dot(u, a) + dot(u, u))))
# final: with c = 1/2, a_i = u_i/2:  c + v.a == ballEffect u v
check('C6 c + v.a == ballEffect u v at c = 1/2, a = u/2',
      zero_poly((sp.Rational(1, 2) + dot(v, [ui / 2 for ui in u])) - ballEffect(u, v)))
# c = 1/2 from F1..F4 (linarith certificate): (F1 - F2-slack) and (F3, F4)
# 2c - 1 = (c - u.a) - (1 - (c + u.a))  >= 0  and  1 - 2c = (1 - (c - w.a)) - (c + w.a) >= 0
check('C7 linarith certificate for c = 1/2: 2c-1 == (c-u.a) - (1-(c+u.a)), 1-2c == (1-(c-w.a)) - (c+w.a)',
      zero_poly(2 * c - 1 - ((c - dot(u, a)) - (1 - (c + dot(u, a)))))
      and zero_poly(1 - 2 * c - ((1 - (c - dot(w, a))) - (c + dot(w, a)))))

# exact instance: a perturbed functional with A > 1/4 violates r(p) <= 1 at p in the ball
for aa in ([Fr(1, 3), Fr(1, 3), Fr(1, 3)], [Fr(3, 5), 0, 0], [Fr(1, 2), Fr(1, 10), 0]):
    AA = sum(x * x for x in aa)
    DD = 1 + 4 * AA
    p = [4 * x / DD for x in aa]
    inball = sum(x * x for x in p) <= 1
    rp = Fr(1, 2) + sum(x * y for x, y in zip(aa, p))
    check(f'C8 A={AA} > 1/4: p in ball and r(p) = {rp} > 1', AA > Fr(1, 4) and inball and rp > 1)
aa = [Fr(1, 6), Fr(1, 3), Fr(1, 3)]   # |a| = 1/2 exactly
AA = sum(x * x for x in aa)
DD = 1 + 4 * AA
p = [4 * x / DD for x in aa]
check('C9 A = 1/4: r(p) == 1 exactly, p on the sphere',
      AA == Fr(1, 4) and sum(x * x for x in p) == 1 and Fr(1, 2) + sum(x * y for x, y in zip(aa, p)) == 1)

# ------------------------------------------------- D. rational rotations: transport identity
def quat_rot(qa, qb, qc, qd):
    n = qa * qa + qb * qb + qc * qc + qd * qd
    M = [[qa*qa+qb*qb-qc*qc-qd*qd, 2*(qb*qc-qa*qd), 2*(qb*qd+qa*qc)],
         [2*(qb*qc+qa*qd), qa*qa-qb*qb+qc*qc-qd*qd, 2*(qc*qd-qa*qb)],
         [2*(qb*qd-qa*qc), 2*(qc*qd+qa*qb), qa*qa-qb*qb-qc*qc+qd*qd]]
    return [[Fr(x, n) for x in row] for row in M]


def mv(M, x):
    return [sum(M[i][j] * x[j] for j in range(3)) for i in range(3)]


def tr(M):
    return [[M[j][i] for j in range(3)] for i in range(3)]


def bE(bb, vv):
    return Fr(1, 2) + sum(x * y for x, y in zip(bb, vv)) / 2


units = [[Fr(1, 3), Fr(2, 3), Fr(2, 3)], [Fr(2, 7), Fr(3, 7), Fr(6, 7)], [Fr(0), Fr(0), Fr(1)],
         [Fr(-4, 9), Fr(4, 9), Fr(7, 9)]]
samples = [[Fr(1, 2), Fr(-1, 3), Fr(1, 5)], [Fr(0), Fr(3, 5), Fr(-4, 5)], [Fr(2), Fr(7), Fr(-3)]]
rots = [quat_rot(1, 2, 3, 4), quat_rot(1, 1, 1, 1), quat_rot(2, 0, 0, 1), quat_rot(3, -1, 2, 5)]
ok = True
for R in rots:
    Rt = tr(R)   # R^{-1}
    orth = all(sum(R[i][m] * R[j][m] for m in range(3)) == (1 if i == j else 0) for i in range(3) for j in range(3))
    ok &= orth
    for bb in units:
        for vv in samples:
            ok &= bE(bb, mv(Rt, vv)) == bE(mv(R, bb), vv)
check('D1 ballEffect b o R^-1 == ballEffect (R b) for 4 rational rotations x 4 units x 3 points', ok)
check('D2 quaternion (1,1,1,1) is cyc3: (x,y,z) -> (z,x,y)',
      mv(quat_rot(1, 1, 1, 1), [Fr(1), Fr(2), Fr(3)]) == [3, 1, 2])
ok = all(bE(bb, bb) == 1 and bE(bb, [-x for x in bb]) == 0 for bb in units)
check('D3 normalisation (1+b.x)/2 = 1 at b and 0 at -b for rational unit b', ok)

# ------------------------------------------------- E. Householder transitivity, exact instances
def hhR(dd, vv):
    q = sum(x * x for x in dd)
    s = sum(x * y for x, y in zip(dd, vv))
    return [vv[i] - 2 * s / q * dd[i] for i in range(3)]


ok = True
for uu, ww in itertools.permutations(units, 2):
    dd = [uu[i] - ww[i] for i in range(3)]
    ok &= hhR(dd, uu) == ww
    for vv in samples:
        Hv_ = hhR(dd, vv)
        ok &= sum(x * x for x in Hv_) == sum(x * x for x in vv)
        ok &= hhR(dd, Hv_) == vv
check('E1 Householder maps u->w, preserves |.|^2, involutive (12 ordered unit pairs)', ok)

# ------------------------------------------------- F. countermodels
ez = [Fr(0), Fr(0), Fr(1)]
ex = [Fr(1), Fr(0), Fr(0)]
# N1: flow alone (rotations about z) fixes the seed (1+z)/2
cs, sn = Fr(3, 5), Fr(4, 5)
Rz = [[cs, -sn, 0], [sn, cs, 0], [0, 0, 1]]
ok = all(bE(ez, mv(tr(Rz), vv)) == bE(ez, vv) for vv in samples)
check('F1 N1 rotation about z (cos 3/5) fixes ballEffect e_z: orbit = {ballEffect e_z}', ok)
check('F1b N1 ballEffect e_x differs from ballEffect e_z at e_x: 1 vs 1/2', bE(ex, ex) == 1 and bE(ez, ex) == Fr(1, 2))
# N1 symbolic: invariance for every angle, using cos^2+sin^2 = 1 is not even needed (z untouched)
check('F1c N1 z-coordinate of R_z(-t) v is v2 (symbolic)',
      zero_poly((sp.Matrix([[sp.cos(-t), -sp.sin(-t), 0], [sp.sin(-t), sp.cos(-t), 0], [0, 0, 1]]) * sp.Matrix(v))[2] - v2))

# N2: unsharp seed r = 3/4 + z/4
def unsharp(vv):
    return Fr(3, 4) + vv[2] / 4


bdry = units + [[-x for x in uu] for uu in units] + [ex, [Fr(0), Fr(1), Fr(0)], [Fr(3, 5), Fr(4, 5), Fr(0)]]
check('F2 N2 unsharp seed: effect on boundary samples, certain at e_z, >= 1/2 everywhere on ball (|z|<=1)',
      all(Fr(1, 2) <= unsharp(x) <= 1 for x in bdry) and unsharp(ez) == 1 and unsharp([0, 0, -1]) == Fr(1, 2))
# its orbit under SO(3): 3/4 + (b.v)/4 ; disjoint from directional: directional takes 0 at -b, orbit >= 1/2
check('F2b N2 orbit member at -b >= 1/2 while ballEffect b (-b) = 0',
      all(Fr(3, 4) + sum(x * y for x, y in zip(bb, [-z for z in bb])) / 4 == Fr(1, 2) for bb in units))
# consumer failure: (x0, v) = (1, (0,0,2)) : cone pairing with 3/4 + b.v/4 is >= 3/4 - 2/4 = 1/4 > 0
# for every unit b (|b.v| <= |b||v| = 2, attained at b = -e_z), yet |v|^2 = 4 > 1 = x0^2.
vv = [Fr(0), Fr(0), Fr(2)]
minpair = Fr(3, 4) - Fr(2, 4)
check('F2c N2 consumer: min_b pairing = 1/4 > 0 (at b=-e_z: %s) but |v|^2=4 > x0^2=1'
      % (Fr(3, 4) + sum(x * y for x, y in zip([0, 0, -1], vv)) / 4),
      minpair > 0 and Fr(3, 4) + sum(x * y for x, y in zip([0, 0, -1], vv)) / 4 == minpair
      and sum(x * x for x in vv) > 1)
check('F2d N2 the directional family rejects the same vector: (1 + (-e_z).v)/2 = -1/2 < 0',
      (1 + sum(x * y for x, y in zip([0, 0, -1], vv))) / Fr(2) == Fr(-1, 2))

# N3: one-sided preservation (dilation g = v/2, g^-1 = 2v): transport of (1+z)/2 is 1/2 + z
check('F3 N3 g = (1/2)id: (r o g^-1)(e_z) = ballEffect e_z (2 e_z) = 3/2 > 1, not an effect',
      bE(ez, [0, 0, 2]) == Fr(3, 2))

# N4: sup-norm sphere trap
check('F4 N4 b=(1,1,1) has sup norm 1 but ballEffect b (3/5,4/5,0) = 6/5 > 1, (3/5,4/5,0) in ball3',
      max(abs(x) for x in [1, 1, 1]) == 1 and bE([1, 1, 1], [Fr(3, 5), Fr(4, 5), 0]) == Fr(6, 5)
      and Fr(9, 25) + Fr(16, 25) == 1)

# N5: finite axis-moving group: generated by cyc3 (= J of ball3Drive) and the half-turn about z (= N)
def mm(M, N):
    return tuple(tuple(sum(M[i][m] * N[m][j] for m in range(3)) for j in range(3)) for i in range(3))


I3 = tuple(tuple(Fr(1) if i == j else Fr(0) for j in range(3)) for i in range(3))
C3 = tuple(tuple(x for x in row) for row in quat_rot(1, 1, 1, 1))
Nz = ((Fr(-1), 0, 0), (0, Fr(-1), 0), (0, 0, Fr(1)))
Nz = tuple(tuple(Fr(x) for x in row) for row in Nz)
grp = {I3}
frontier = [I3]
while frontier:
    new = []
    for g in frontier:
        for h in (C3, Nz):
            gh = mm(g, h)
            if gh not in grp:
                grp.add(gh)
                new.append(gh)
    frontier = new
orbit = {tuple(mv(g, ez)) for g in grp}
conj = mm(mm(C3, Nz), tuple(tuple(r) for r in tr(C3)))
check('F5 N5 <cyc3, N_z> is finite (order %d), moves the axis (cyc3 N cyc3^-1 != N, != I), orbit of e_z has %d points'
      % (len(grp), len(orbit)), len(grp) == 12 and len(orbit) == 6 and conj != Nz and conj != I3)

# N6: ellipsoid body {x^2/4 + y^2 + z^2 <= 1}: seed (1 + x/2)/2 sharp, but (1+x)/2 = 3/2 at (2,0,0)
def inE(p):
    return p[0] ** 2 / 4 + p[1] ** 2 + p[2] ** 2 <= 1


seedE = lambda p: Fr(1, 2) + p[0] / 4
check('F6 N6 ellipsoid: seed (1+x/2)/2 sharp (1 at (2,0,0), 0 at (-2,0,0)); ballEffect e_x = 3/2 at (2,0,0)',
      inE([2, 0, 0]) and inE([-2, 0, 0]) and seedE([2, 0, 0]) == 1 and seedE([-2, 0, 0]) == 0
      and bE(ex, [2, 0, 0]) == Fr(3, 2))
# the conjugated group A R A^-1 (A = diag(2,1,1)) preserves the ellipsoid and transports the seed to (1 + b.A^-1 x)/2
A_ = [[Fr(2), 0, 0], [0, Fr(1), 0], [0, 0, Fr(1)]]
Ai = [[Fr(1, 2), 0, 0], [0, Fr(1), 0], [0, 0, Fr(1)]]
R = rots[0]
g = [[sum(A_[i][m] * sum(R[m][n] * Ai[n][j] for n in range(3)) for m in range(3)) for j in range(3)] for i in range(3)]
pts = [[Fr(2), 0, 0], [0, Fr(1), 0], [Fr(6, 5), Fr(4, 5), 0]]
check('F6b N6 A R A^-1 preserves the ellipsoid boundary on samples', all(
    sum(x for x in [mv(g, p)[0] ** 2 / 4, mv(g, p)[1] ** 2, mv(g, p)[2] ** 2]) == 1 for p in pts))

# N7: square (gbit): D4 maps vertices to vertices, so not transitive on the boundary
D4 = [((1, 0), (0, 1)), ((0, -1), (1, 0)), ((-1, 0), (0, -1)), ((0, 1), (-1, 0)),
      ((1, 0), (0, -1)), ((-1, 0), (0, 1)), ((0, 1), (1, 0)), ((0, -1), (-1, 0))]
imgs = {tuple(sum(M[i][j] * p[j] for j in range(2)) for i in range(2)) for M in D4 for p in [(1, 1)]}
check('F7 N7 square: D4-orbit of the vertex (1,1) is the 4 vertices; edge midpoint (1,0) not reached',
      imgs == {(1, 1), (1, -1), (-1, 1), (-1, -1)} and (1, 0) not in imgs)

# ------------------------------------------------- G. what lorentz_of_effects consumes
# hypothesis: for all b with sum b_j^2 = 1, 0 <= x0 + sum b_j v_j ; the directional family gives
# 2*conePair = x0 + b.v, so the hypothesis holds iff every directional effect pairs nonnegatively.
# Exact sample: a Lorentz-cone vector passes, an outside vector fails at b = -v/|v|.
inside = (Fr(5), [Fr(3), Fr(4), Fr(0)])
outside = (Fr(4), [Fr(3), Fr(4), Fr(0)])
bneg = [Fr(-3, 5), Fr(-4, 5), Fr(0)]
check('G1 (5;3,4,0) boundary of Lorentz cone: x0 + b.v = 0 at b = -v/|v|; (4;3,4,0) gives -1 < 0',
      inside[0] + sum(x * y for x, y in zip(bneg, inside[1])) == 0
      and outside[0] + sum(x * y for x, y in zip(bneg, outside[1])) == -1)

nfail = sum(1 for _, okk in CHECKS if not okk)
print(f'{"OK" if nfail == 0 else "FAIL"} -- {len(CHECKS)} checks, {nfail} failed')
raise SystemExit(1 if nfail else 0)
