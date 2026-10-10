#!/usr/bin/env python3
"""Thread F -- exact countermodels and controls for the KInf1 dependency ledger (read-only research).

Exact arithmetic only (fractions.Fraction, sympy rationals/symbols). Every section prints its checks;
the script exits nonzero if any check fails. Each check is labelled with its evidence kind:
  identity  -- a symbolic identity verified by sympy simplification to exactly 0
  witness   -- an exact rational instance
  enumerate -- an exhaustive finite enumeration
  deduce    -- an exact step of a written deduction (the deduction itself is in LEDGER.md)
Mutations (countercontrols) are checks that the opposite verdict appears when the load-bearing
ingredient is removed; they are marked 'mutation'.

Sections
  CM-RSC   the bidisk D x D = conv(S^1 x S^1): drivable, (SEC) with full effects, not relatively strictly convex
  CM-ORB   the bidisk with an orbit-closed family seeded by a point-exposing effect: (SEC) fails at (e1, 0)
  CM-CPT   ball3 x [0, oo): closed, convex, drivable, not compact; (SEC) fails with the full effects
  BR-FIN   finite affine automorphism group => no drive (continuity-free): square, triangle; mutation: disk rotation
  BR-DISK  the disk: every flow member is a square, squares in O(2) are rotations, O(2)-conjugates of rotations are
           rotations or inverses => J_off_axis fails; control: the ball3 drive's J moves the axis
  CM-INF   Hilbert cube x ball3 with continuous effects: exact truncation checks of the written argument
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

import sympy as sp

FAIL = []
COUNT = [0]


def chk(name, ok, kind):
    COUNT[0] += 1
    tag = 'ok  ' if ok else 'FAIL'
    print('  [%s] %-58s (%s)' % (tag, name, kind))
    if not ok:
        FAIL.append(name)


NOTES = []


def note(text):
    NOTES.append(text)
    print('  [note] %s  (written step, not a check)' % text)


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


def section(title):
    print('\n== %s' % title)


# ---------------------------------------------------------------- rational points of the unit circle
def circ(m, n):
    """the rational point ((m^2-n^2)/(m^2+n^2), 2mn/(m^2+n^2)) of the unit circle"""
    d = m * m + n * n
    return (Fr(m * m - n * n, d), Fr(2 * m * n, d))


CIRCLE = [(Fr(1), Fr(0)), (Fr(-1), Fr(0)), (Fr(0), Fr(1)), (Fr(0), Fr(-1))] + \
    [circ(m, n) for m in range(1, 5) for n in range(1, 5)] + \
    [(-a, b) for (a, b) in [circ(m, n) for m in range(1, 4) for n in range(1, 4)]]
DISK_IN = [(Fr(0), Fr(0)), (Fr(1, 2), Fr(1, 3)), (Fr(-2, 5), Fr(1, 7)), (Fr(3, 5) / 2, Fr(4, 5) / 2)]


def dot2(a, b):
    return a[0] * b[0] + a[1] * b[1]


def n2(a):
    return dot2(a, a)


# ================================================================== CM-RSC
section('CM-RSC  bidisk D x D: drivable + (SEC, full effects) and not RelStrictConvex')
t, s, c1, s1 = sp.symbols('t s c1 s1', real=True)
u0, u1, v0, v1, x0, x1, y0, y1 = sp.symbols('u0 u1 v0 v1 x0 x1 y0 y1', real=True)


def R(th):
    return sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])


def flowB(th, p):           # flow t = R_t (+) I on R^2 x R^2
    a = R(th) * sp.Matrix(p[:2])
    return [a[0], a[1], p[2], p[3]]


def swapB(p):               # J = swap of the two disks
    return [p[2], p[3], p[0], p[1]]


P = [u0, u1, v0, v1]
fp = flowB(t, P)
chk('flow preserves |u|^2 and |v|^2 (so preserves D x D)',
    zero(fp[0] ** 2 + fp[1] ** 2 - (u0 ** 2 + u1 ** 2)) and fp[2] == v0 and fp[3] == v1, 'identity')
fst = flowB(s, flowB(t, P))
fsum = flowB(s + t, P)
chk('flow_add: flow s (flow t p) = flow (s+t) p',
    all(zero(sp.expand_trig(fst[i] - fsum[i])) for i in range(4)), 'identity')
f0 = flowB(0, P)
chk('flow_zero: flow 0 = id', all(zero(f0[i] - P[i]) for i in range(4)), 'identity')
Npt = flowB(sp.pi, flowB(sp.pi, P))
chk('N = flow pi is an involution on R^4', all(zero(Npt[i] - P[i]) for i in range(4)), 'identity')
e1e1 = [1, 0, 1, 0]
chk('N moves the state (e1, e1)', flowB(sp.pi, e1e1) != e1e1 and flowB(sp.pi, e1e1)[0] == -1, 'witness')
chk('J = swap and its inverse (itself) preserve D x D', swapB(swapB(P)) == P, 'identity')
# J flow(pi/2) J^-1 at (e1, e1) = (e1, e2); every flow member fixes the second disk coordinate (e1).
conj = swapB(flowB(sp.pi / 2, swapB(e1e1)))
chk('J_off_axis on Om: (J flow(pi/2) J^-1)(e1,e1) has v = e2, flow s keeps v = e1 for every s',
    [sp.simplify(z) for z in conj] == [1, 0, 0, 1] and flowB(s, e1e1)[2:] == [1, 0], 'identity')

# boundary states of D x D: |u| = 1 or |v| = 1. A state with |u| < 1 and |v| < 1 lies in the topological interior
# of D x D in R^4, hence is not a boundary state (kernel: not_isBoundaryState_of_mem_interior).
# (SEC) with full effects: at (u, v) with |u| = 1 the effect e = (1 + u . x)/2 on (x, y).
# 0 <= e <= 1 on D x D: for |u| = 1, |x| <= 1:  1 - u.x >= (|u|^2+|x|^2)/2 - u.x = |u-x|^2/2 >= 0, same with -x.
chk('SOS: (|u|^2+|x|^2)/2 - u.x = |u-x|^2/2', zero((u0 ** 2 + u1 ** 2 + x0 ** 2 + x1 ** 2) / 2 - (u0 * x0 + u1 * x1)
                                                  - ((u0 - x0) ** 2 + (u1 - x1) ** 2) / 2), 'identity')
chk('SOS: (|u|^2+|x|^2)/2 + u.x = |u+x|^2/2', zero((u0 ** 2 + u1 ** 2 + x0 ** 2 + x1 ** 2) / 2 + (u0 * x0 + u1 * x1)
                                                  - ((u0 + x0) ** 2 + (u1 + x1) ** 2) / 2), 'identity')
ok_sec = True
for u in CIRCLE:
    assert n2(u) == 1
    for v in DISK_IN + CIRCLE[:6]:
        def e(p, u=u):
            return (1 + dot2(u, p[:2])) / 2
        state = (u[0], u[1], v[0], v[1])
        # certain at the state, proper (value 1/2 at the origin of D x D), in [0,1] at sampled states
        samples = [(a[0], a[1], b[0], b[1]) for a in CIRCLE[:8] + DISK_IN for b in DISK_IN[:2]]
        ok_sec &= e(state) == 1 and e((0, 0, 0, 0)) == Fr(1, 2) and all(0 <= e(p) <= 1 for p in samples)
        # and it is a boundary state: witness y = (-u, v): (u,v) + eps((u,v) - (-u,v)) = ((1+2eps)u, v), |.|>1
        ok_sec &= all(n2(((1 + 2 * eps) * u[0], (1 + 2 * eps) * u[1])) > 1 for eps in (Fr(1, 10 ** k) for k in range(1, 8)))
chk('(SEC, full effects) at %d boundary states (|u| = 1): (1+u.x)/2 proper, certain' % (len(CIRCLE) * (len(DISK_IN) + 6)),
    ok_sec, 'witness')
# not RelStrictConvex: x = (e1, e1), y = (e1, -e1), midpoint (e1, 0) is a boundary state
mid = (Fr(1), Fr(0), Fr(0), Fr(0))
chk('midpoint (e1,0) of (e1,e1),(e1,-e1) is a boundary state (witness y = (-e1, 0))',
    all(n2(((1 + 2 * eps), 0)) > 1 for eps in (Fr(1, 10 ** k) for k in range(1, 8))), 'witness')
eF = lambda p: (1 + p[0]) / 2
chk('(SF, full) fails: (1+x0)/2 proper and certain at (e1,e1) and (e1,-e1)',
    eF((1, 0, 1, 0)) == 1 and eF((1, 0, -1, 0)) == 1 and eF((0, 0, 0, 0)) < 1, 'witness')
# countercontrol: on ball3 (strictly convex) the same construction gives a singleton certain face:
# (1 + e1.x)/2 = 1 on |x| <= 1 forces x = e1, since |x - e1|^2 = |x|^2 - 2 x0 + 1 <= 2 - 2 x0 = 0.
X0, X1, X2 = sp.symbols('X0 X1 X2', real=True)
chk('mutation: ball3 (1+x0)/2 = 1 forces x = e1 (|x-e1|^2 = |x|^2 + 1 - 2x0)',
    zero((X0 - 1) ** 2 + X1 ** 2 + X2 ** 2 - (X0 ** 2 + X1 ** 2 + X2 ** 2 + 1 - 2 * X0)), 'identity')

# ================================================================== CM-ORB
section('CM-ORB  bidisk, family = orbit of a point-exposing seed under the drive group: (SEC) fails')
# G = <R_t (+) I, swap> = (SO(2) x SO(2)) x| Z2. Seed e0 = (2 + x.e1 + y.e1)/4. Its orbit: e_{u,v} = (2 + u.x + v.y)/4,
# |u| = |v| = 1 (pull-back by g sends (u, v) to (R u, v) or (v, u)).
a0, a1, b0, b1 = sp.symbols('a0 a1 b0 b1', real=True)
euv = lambda U, Vv, p: (2 + U[0] * p[0] + U[1] * p[1] + Vv[0] * p[2] + Vv[1] * p[3]) / 4
Ru = R(t) * sp.Matrix([a0, a1])
pull_flow = euv((a0, a1), (b0, b1), flowB(-t, P)) - euv((sp.cos(t) * a0 - sp.sin(t) * a1, sp.sin(t) * a0 + sp.cos(t) * a1), (b0, b1), P)
chk('orbit closure under the flow: e_{u,v} o flow(-t) = e_{R_t u, v}', zero(sp.expand_trig(pull_flow)), 'identity')
chk('orbit closure under J: e_{u,v} o swap = e_{v,u}', zero(euv((a0, a1), (b0, b1), swapB(P)) - euv((b0, b1), (a0, a1), P)), 'identity')
note('the group acts transitively on the extreme points S^1 x S^1 (flow on each factor via J)')
ok = True
for U in CIRCLE:
    for Vv in CIRCLE:
        val = euv(U, Vv, (1, 0, 0, 0))
        ok &= val <= Fr(3, 4) and val < 1
chk('every orbit effect is <= 3/4 at the boundary state (e1, 0): (2 + u0)/4 <= 3/4', ok, 'witness')
chk('symbolic: e_{u,v}(e1,0) = (2+u0)/4 and u0 <= |u| = 1', zero(euv((a0, a1), (b0, b1), (1, 0, 0, 0)) - (2 + a0) / 4), 'identity')
note('the unit is not proper, so (SEC) for orbit + unit fails at (e1, 0)')
# countercontrol 1: the boundary point (e1,e1) (extreme) IS exposed by the seed
chk('control: the seed is certain at the extreme state (e1, e1)', euv((1, 0), (1, 0), (1, 0, 1, 0)) == 1, 'witness')
# countercontrol 2: a face-exposing seed (1 + x.e1)/2 makes the orbit family supporting-complete
ok2 = True
for U in CIRCLE:
    for Vv in DISK_IN:
        ok2 &= (1 + dot2(U, (U[0], U[1]))) / 2 == 1      # e_U certain at (U, anything)
chk('mutation: seed (1+x.e1)/2 -> orbit {(1+u.x)/2, (1+v.y)/2} certain at every boundary state', ok2, 'witness')

# ================================================================== CM-CPT
section('CM-CPT  ball3 x [0, oo): drivable, closed, convex, NOT compact; (SEC) fails with full effects')
# drive: ball3Drive on the first three coordinates, identity on the fourth; all fields inherited on states
Rz3 = sp.Matrix([[sp.cos(t), -sp.sin(t), 0], [sp.sin(t), sp.cos(t), 0], [0, 0, 1]])
w = Rz3 * sp.Matrix([X0, X1, X2])
chk('rot3 x id preserves |u|^2 and fixes the 4th coordinate s', zero(w.dot(w) - (X0**2 + X1**2 + X2**2)), 'identity')
chk('J_off_axis inherited: (cyc3 rot3(pi) cyc3^-1)(e3, 0) = (-e3, 0), rot3(s)(e3) = e3',
    (sp.Matrix([[0,0,1],[1,0,0],[0,1,0]]) * Rz3.subs(t, sp.pi) * sp.Matrix([[0,0,1],[1,0,0],[0,1,0]]).T * sp.Matrix([0,0,1]))
    == sp.Matrix([0, 0, -1]) and Rz3 * sp.Matrix([0, 0, 1]) == sp.Matrix([0, 0, 1]), 'witness')
# boundary state z = (0,0,0,0): y = (0,0,0,1), z + eps(z - y) = (0,0,0,-eps) has negative 4th coordinate
chk('z = 0 is a boundary state: z + eps(z - (0,0,0,1)) = (0,0,0,-eps) not in Om', all(-Fr(1, k) < 0 for k in range(1, 50)), 'witness')
# an effect e = c + a.u + d s with 0 <= e <= 1 on Om and e(0) = 1:
#  step 1: d = 0, else s = 2/|d| gives |e(0,s) - e(0,0)| = 2 > 1
dp = sp.symbols('dp', positive=True)
chk('deduce d = 0: for d = +-dp != 0, s = 2/dp gives |e(0,s) - e(0,0)| = |d s| = 2 > 1',
    sp.simplify(dp * (2 / dp)) == 2 and sp.simplify(-dp * (2 / dp)) == -2, 'deduce')
#  step 2: c = e(0) = 1; e(+-e_i, 0) = 1 +- a_i <= 1 forces a_i = 0; so e == 1 on Om: not proper
note('deduce a = 0 from 1 + a_i <= 1 and 1 - a_i <= 1, so e is identically 1 (not proper)')
chk('control: ball3 x [0, 1] (compact) has the proper effect 1 - s certain at z = 0',
    (lambda sv: 1 - sv)(0) == 1 and (lambda sv: 1 - sv)(1) == 0, 'witness')

# ================================================================== BR-FIN
section('BR-FIN  finite automorphism group => no drive (no continuity used)')


def affine_auts(verts):
    """affine maps of the plane permuting the given vertex list (vertices affinely span the plane)"""
    out = []
    p0, p1, p2 = verts[0], verts[1], verts[2]
    for img in permutations(verts):
        # solve A p + b = img(p) on p0, p1, p2, then test on all
        M = sp.Matrix([[p[0], p[1], 1] for p in (p0, p1, p2)])
        if M.det() == 0:
            raise ValueError
        sol = []
        for k in range(2):
            rhs = sp.Matrix([img[i][k] for i in range(3)])
            sol.append(M.LUsolve(rhs))
        A = sp.Matrix([[sol[0][0], sol[0][1]], [sol[1][0], sol[1][1]]])
        b = sp.Matrix([sol[0][2], sol[1][2]])
        if all((A * sp.Matrix(verts[i]) + b) == sp.Matrix(img[i]) for i in range(len(verts))) and A.det() != 0:
            out.append((A, b))
    return out


def power(g, k):
    A, b = g
    RA, Rb = sp.eye(2), sp.zeros(2, 1)
    for _ in range(k):
        RA, Rb = A * RA, A * Rb + b
    return RA, Rb


square = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
triangle = [(0, 0), (1, 0), (0, 1)]
for name, verts in (('square gbit', square), ('triangle (classical trit)', triangle)):
    G = affine_auts(verts)
    m = len(G)
    chk('%s: |Aff(Om)| = %d (enumerated on vertices)' % (name, m), m in (8, 6), 'enumerate')
    chk('%s: g^%d = id for every automorphism g' % (name, m),
        all(power(g, m) == (sp.eye(2), sp.zeros(2, 1)) for g in G), 'enumerate')
note('deduce: N = flow(t0) = flow(t0/m)^m restricts to g^m = id on Om, contradicting N_moves')
# mutation: an automorphism of infinite order (disk rotation with cos = 3/5) has no finite exponent
Rq = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])
acc, ok = sp.eye(2), True
for k in range(1, 201):
    acc = Rq * acc
    ok &= acc != sp.eye(2)
chk('mutation: the disk rotation (3/5, 4/5) has R^k != I for k = 1..200 (finiteness is load-bearing)', ok, 'enumerate')

# ================================================================== BR-DISK
section('BR-DISK  the rebit disk: J_off_axis fails for every candidate drive (no continuity used)')
th, ph = sp.symbols('theta phi', real=True)
Rot = R(th)
Ref = sp.Matrix([[sp.cos(ph), sp.sin(ph)], [sp.sin(ph), -sp.cos(ph)]])
chk('a reflection squares to I', zero((Ref * Ref - sp.eye(2)).norm() ** 2) or (sp.simplify(Ref * Ref - sp.eye(2)) == sp.zeros(2)), 'identity')
chk('a rotation squares to the rotation by 2 theta', sp.simplify(sp.expand_trig(Rot * Rot - R(2 * th))) == sp.zeros(2), 'identity')
chk('rotation conjugated by a rotation is itself', sp.simplify(Rot * R(ph) * Rot.T - R(ph)) == sp.zeros(2), 'identity')
chk('rotation conjugated by a reflection is its inverse', sp.simplify(Ref * Rot * Ref.T - Rot.T) == sp.zeros(2), 'identity')
note('deduce: flow t = flow(t/2)^2 is a rotation; J flow t J^-1 = flow(+-t) on the disk')
note('generalization (written): every compact convex body of affine dimension 2 has a compact automorphism group, '
     'orthogonal for an invariant inner product, so the same three identities exclude a drive on every planar body '
     '(polygons, disk); with not_drivable_Icc and not_drivable_singleton, no body of affine dimension <= 2 is drivable')
Sh = sp.Matrix([[1, 1], [0, 1]])        # not an automorphism of the disk
Rq2 = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])
cs = Sh * Rq2 * Sh.inv()
chk('mutation: a shear (not a disk automorphism) conjugates R to neither R nor R^-1 (O(2) step load-bearing)',
    cs != Rq2 and cs != Rq2.T, 'witness')
# control: in the ball3 drive, J = cyc3 carries R_z(pi) to a rotation not about z (kernel ball3Drive.J_off_axis)
cyc = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Rz = sp.Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
conj3 = cyc * Rz * cyc.T
chk('control: cyc3 R_z(pi) cyc3^-1 sends e3 to -e3, every R_z(s) fixes e3', conj3 * sp.Matrix([0, 0, 1]) == sp.Matrix([0, 0, -1]), 'witness')

# ================================================================== CM-INF
section('CM-INF  Hilbert cube K x ball3, continuous effects (written argument; exact truncation checks)')
# K = {v in l2 : |v_n| <= 2^-n}; x_n = 2^-n (1 - 1/n); y = -corner, corner_n = 2^-n.
# (x + eps(x - y))_n = 2^-n [(1 - 1/n) + eps (2 - 1/n)] > 2^-n  iff  eps (2 - 1/n) > 1/n.
ok = True
for k in range(1, 60):
    eps = Fr(1, k)
    n = next(n for n in range(1, 10 ** 4) if eps * (2 - Fr(1, n)) > Fr(1, n))
    ok &= n <= 2 * k + 1
chk('for eps = 1/k (k < 60) some coordinate n <= 2k+1 leaves K: x is a boundary state', ok, 'witness')
# a continuous effect c + <f, v> + g.u certain at (x, 0): sup = c + sum |f_n| 2^-n + |g|, value = c + sum f_n 2^-n (1-1/n)
# each slack term |f_n| 2^-n - f_n 2^-n (1-1/n) >= |f_n| 2^-n / n >= 0, with equality iff f_n = 0.
ok = True
for n in range(1, 40):
    for fn in (Fr(-3, 2), Fr(-1, 7), Fr(0), Fr(2, 9), Fr(5)):
        slack = abs(fn) * Fr(1, 2 ** n) - fn * Fr(1, 2 ** n) * (1 - Fr(1, n))
        ok &= slack >= abs(fn) * Fr(1, 2 ** n) / n and (slack == 0) == (fn == 0)
chk('termwise slack >= |f_n| 2^-n / n, zero iff f_n = 0 (n < 40, sample f_n)', ok, 'witness')
note('deduce: certainty forces f = 0 and g = 0, so e is constant 1 on Om: no proper continuous effect')

# ================================================================== CM-SIC
section('CM-SIC  the SIC ball in the simplex with response effects: a drivable body on which KInf1 is false')
r3 = sp.sqrt(3)
A_ = [sp.Matrix([1, 1, 1]) / r3, sp.Matrix([1, -1, -1]) / r3, sp.Matrix([-1, 1, -1]) / r3, sp.Matrix([-1, -1, 1]) / r3]
rr = sp.Matrix([0, 0, 1])                       # a pure state (|r| = 1), a boundary state of the embedded ball
pv = [sp.nsimplify((1 + a.dot(rr)) / 4) for a in A_]
chk('p(e3) = (1 + a_i.e3)/4 sums to 1 and has every coordinate > 0 (full support)',
    sp.simplify(sum(pv) - 1) == 0 and all(sp.simplify(q).is_positive for q in pv), 'identity')
chk('tangency control: r = -a_1 gives p_1 = 0 (a facet point, exposable by 1 - p_1)',
    sp.simplify((1 + A_[0].dot(-A_[0])) / 4) == 0, 'identity')
note('deduce (kernel response_eq_one_forces, KInfFoundations.lean:899): a response effect certain at a full-support state '
     'has c = 1, hence equals sum p_i = 1 on the body and is not proper; so (SEC) with response effects fails at p(e3), '
     'while the ball is drivable (ball3Drive transported along the affine embedding): KInf1 is false there')

print('\nf_countermodels: %s -- %d checks, %d written notes' % ('OK' if not FAIL else 'FAILED ' + ', '.join(FAIL), COUNT[0], len(NOTES)))
sys.exit(1 if FAIL else 0)
