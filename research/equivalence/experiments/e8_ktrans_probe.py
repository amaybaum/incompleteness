"""E8 design probe for draft S4 (KTRANS-SEP-1): the exact layer as the round would freeze it  (exact: sympy symbolic
identities, rationals, and one quadratic-surd sign decided in rationals)

ORIGIN.  Checks D1-D9 and C1, with their code, are copied without change from experiments/e2_drive_trans.py (sha256
394850c8..., round 1: 10/10, `VERDICT DRIVE-SEED-GEOM-CAP2-NOT-TRANS`); its header (written steps W1-W4, checks D1-D9,
control C1) applies here unchanged.  This file adds W5 (supporting-effect completeness for the full effects), the
positive control C2 and the countercontrols XW1, XW2.  e2_drive_trans.py itself is not edited.

THE BODY.  Omega4 = {(x, s) in R^3 x R : F(x, s) <= 1},  F(x, s) = (x0^2 + x1^2 + x2^2)^2 + s^4; drive data as in
e2_drive_trans.py.

W5.  For p, y in R^4 put l_p(y) = grad F(p) . y / 4 and e_p = (1 + l_p)/2.
  W5(i)   Euler: grad F(p) . p = 4 F(p), identically in p.
  W5(ii)  the gradient gap is an explicit sum of squares, identically in (y, p):
              F(y) - F(p) - grad F(p) . (y - p)
                = (|y_x|^2 - |p_x|^2)^2 + 2 |p_x|^2 |y_x - p_x|^2 + (y_s - p_s)^2 ((y_s + p_s)^2 + 2 p_s^2).
  W5(iii) at the nine exact boundary points of D8 and at the two irrational boundary points
              p1 = (sqrt(15)/5, 0, 0, 2 sqrt(5)/5)   (|x|^2 = 3/5, s^2 = 4/5)   and   p2 = (2^(-1/4), 0, 0, 2^(-1/4)),
          F(p) = 1, e_p(p) = 1 and e_p(-p) = 0, exactly.
  W5(iv)  on the exact grid G = {y in {k/4 : -4 <= k <= 4}^4 : F(y) <= 1}, the effect e_p of each of the nine rational
          points of D8 takes values in [0, 1].
  W5 passes iff (i)-(iv) all hold.
  Written step [W] (not checked here).  The boundary states of Omega4 in the kernel's sense (`IsBoundaryState`,
  KInfFoundations.lean:130) are exactly the points with F = 1: a point with F < 1 is interior (F is continuous); at
  F(p) = 1 the witness y = 0 gives F((1 + eps) p) = (1 + eps)^4 > 1.  For F(p) = 1 and F(y) <= 1, (i) and (ii) give
  grad F(p) . y = F(y) + 3 - gap <= 4, so e_p <= 1 on Omega4; central symmetry (D7) gives e_p >= 0; e_p(-p) = 0 < 1
  makes e_p proper.  So every boundary state is certain for a proper full effect:
  `SupportingEffectComplete Omega4 (fullEffects Omega4)` (KInfFoundations.lean:135, :149).  This is an explicit
  instance of the supporting-hyperplane theorem [L], under which every compact convex body in R^n has supporting-effect
  completeness with its full effects; the content of K-inf-1 lies in the available family (`not_kInf1_ball3_unit`),
  which this probe does not touch.
CONTROL C2.  The same two identities on the Euclidean 4-ball: grad F(p) . p = 2 F(p) and the gap equals |y - p|^2 --
  the form of the kernel's positive control `supportingEffectComplete_ball3` (KInfFoundations.lean:1053) at d = 3.
COUNTERCONTROLS (each must fail as stated).
  XW1  W5(ii) with the term 2 |p_x|^2 |y_x - p_x|^2 omitted is not an identity (the identity check is not vacuous).
  XW2  at p1 the Euclidean-normal functional e'(y) = (1 + p1 . y / |p1|^2)/2 has e'(p1) = 1 and is not an effect on
       Omega4: the exact state y* = (21/25, 0, 0, 21/25), with F(y*) = 388962/390625 <= 1, has e'(y*) > 1.  The
       comparison p1 . y* / |p1|^2 = (3/25)(sqrt 15 + 2 sqrt 5) > 1 is decided in rationals: sqrt 15 + 2 sqrt 5 =
       sqrt 5 (2 + sqrt 3) (checked); with c = (3/25)(2 + sqrt 3) > 0 both sides of sqrt 5 c > 1 are positive, so it is
       5 c^2 - 1 > 0, i.e. a + b sqrt 3 > 0 with a = -62/125, b = 36/125 (checked), which holds iff 3 b^2 > a^2
       (a < 0 < b).  So the effect check separates the body's supporting effect from the ball's at a curved point.
DECISION RULE (fixed before run 1).  VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS iff D1-D9, W5, C1 and C2 all pass
(checks: 12, failures: 0) and XW1 and XW2 each fail as stated.  Otherwise "VERDICT NOT RENDERED" followed by every
failing check and every countercontrol that did not fail as stated.  Beyond e2_drive_trans's verdict this adds only
supporting-effect completeness for the full effects on Omega4 (with the written step); it says nothing about chart
dimension 3, about any available effect family of OI, or about OI's sourcing of any premise.
"""
import sys
import sympy as sp
from fractions import Fraction as Fr

RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print('%s %s%s' % ('PASS' if ok else 'FAIL', name, (' -- ' + detail) if detail else ''))


t, u, x0, x1, x2, s = sp.symbols('t u x0 x1 x2 s', real=True)
v = sp.Matrix([x0, x1, x2, s])


def F4(w):
    return sp.expand((w[0] ** 2 + w[1] ** 2 + w[2] ** 2) ** 2 + w[3] ** 4)


def Fball(w):
    return sp.expand(w[0] ** 2 + w[1] ** 2 + w[2] ** 2 + w[3] ** 2)


def Rz(a):
    return sp.Matrix([[sp.cos(a), -sp.sin(a), 0, 0], [sp.sin(a), sp.cos(a), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


J = sp.Matrix([[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])   # (x0,x1,x2,s) -> (x2,x0,x1,s)
Jinv = J.inv()
E = [sp.Matrix([1 if i == k else 0 for i in range(4)]) for k in range(4)]


def drive_checks(Fn, label):
    ok1 = sp.simplify(sp.expand_trig(Fn(Rz(t) * v) - Fn(v))) == 0
    ok2 = sp.simplify((Rz(t) * Rz(u) - Rz(t + u)).applyfunc(sp.expand_trig)) == sp.zeros(4) and Rz(0) == sp.eye(4)
    N = Rz(sp.pi)
    ok3 = (N * N == sp.eye(4)) and (N * E[0] == -E[0]) and Fn(E[0]) <= 1
    ok4 = sp.expand(Fn(J * v) - Fn(v)) == 0 and sp.expand(Fn(Jinv * v) - Fn(v)) == 0
    lhs = J * (Rz(sp.pi / 2) * (Jinv * E[1]))
    ok5 = lhs == E[2] and (Rz(u) * E[1])[2] == 0 and Fn(E[1]) <= 1
    return ok1, ok2, ok3, ok4, ok5


print('== Omega4 = {(|x|^2)^2 + s^4 <= 1}')
o1, o2, o3, o4, o5 = drive_checks(F4, 'Omega4')
check('D1 the flow preserves F identically', o1)
check('D2 flow_zero and flow_add (R_z(t) R_z(u) = R_z(t+u))', o2)
check('D3 N = flow(pi) is an involution and moves e0 in Omega4', o3)
check('D4 J and J^-1 preserve F identically', o4)
check('D5 J_off_axis at t = pi/2, x = e1: J flow(pi/2) J^-1 e1 = e2, flow(s) e1 has zero third coordinate', o5)

# D6: the seed
p_top, p_bot = sp.Matrix([0, 0, 0, 1]), sp.Matrix([0, 0, 0, -1])
r = lambda w: (1 + w[3]) / sp.Integer(2)
s_bound = sp.simplify(F4(v) - v[3] ** 4 - (v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** 2) == 0   # F = |x|^4 + s^4
check('D6 seed (1+s)/2: s^4 <= F gives |s| <= 1 on Omega4; values 1 and 0 at (0,0,0,+-1) in Omega4',
      s_bound and r(p_top) == 1 and r(p_bot) == 0 and F4(p_top) == 1 and F4(p_bot) == 1)

# D7: central symmetry
check('D7 F(-v) = F(v) (central symmetry; capacity <= 2 by Lemma D)', sp.expand(F4(-v) - F4(v)) == 0)

# D8: strict-convexity instances on exact rational boundary points
pts = [(Fr(1), Fr(0), Fr(0), Fr(0)), (Fr(-1), Fr(0), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0), Fr(0)),
       (Fr(1, 3), Fr(2, 3), Fr(2, 3), Fr(0)), (Fr(-2, 3), Fr(1, 3), Fr(2, 3), Fr(0)), (Fr(3, 5), Fr(0), Fr(4, 5), Fr(0)),
       (Fr(0), Fr(0), Fr(0), Fr(1)), (Fr(0), Fr(0), Fr(0), Fr(-1)), (Fr(0), Fr(0), Fr(-1), Fr(0))]
Fq = lambda w: (w[0] ** 2 + w[1] ** 2 + w[2] ** 2) ** 2 + w[3] ** 4
on_bd = all(Fq(p) == 1 for p in pts)
worst = max(Fq(tuple((a + b) / 2 for a, b in zip(p, q))) for i, p in enumerate(pts) for q in pts[i + 1:])
check('D8 %d exact boundary points; every midpoint of a distinct pair has F < 1 (max %s)' % (len(pts), worst),
      on_bd and worst < 1)

# D9: the (x0, s) section is not an ellipse
A, B, C, tau = sp.symbols('A B C tau', real=True)
eqs = [sp.Eq(A, 1), sp.Eq(C, 1), sp.Eq(tau * (A + 2 * B + C), 1), sp.Eq(tau * (A - 2 * B + C), 1), sp.Eq(tau ** 2, sp.Rational(1, 2))]
sol = sp.solve(eqs, [A, B, C, tau], dict=True)
check('D9 the section {u^4 + v^4 <= 1} is not {A u^2 + 2 B u v + C v^2 <= 1}: the boundary-point system has no solution',
      sol == [])

# CONTROL C1: the Euclidean 4-ball
print('== control: the Euclidean 4-ball')
b1, b2, b3, b4, b5 = drive_checks(Fball, 'ball4')
eqsb = [sp.Eq(A, 1), sp.Eq(C, 1), sp.Eq(tau * (A + 2 * B + C), 1), sp.Eq(tau * (A - 2 * B + C), 1), sp.Eq(tau, sp.Rational(1, 2))]
solb = sp.solve(eqsb, [A, B, C, tau], dict=True)
check('C1 ball4: D1-D5 hold and the section system is consistent (B = 0)', all([b1, b2, b3, b4, b5]) and
      solb == [{A: 1, B: 0, C: 1, tau: sp.Rational(1, 2)}], 'solution %s' % solb)


# W5: supporting-effect completeness for the full effects
import itertools

print('== W5 and its controls')
y0, y1, y2, y3, q0, q1, q2, q3 = sp.symbols('y0 y1 y2 y3 q0 q1 q2 q3', real=True)
Ys, Ps = [y0, y1, y2, y3], [q0, q1, q2, q3]
VARS = [x0, x1, x2, s]


def grad_at(Fn, w):
    sub = dict(zip(VARS, w))
    return [sp.expand(sp.diff(Fn(v), z).subs(sub, simultaneous=True)) for z in VARS]


def nx(w):
    return w[0] ** 2 + w[1] ** 2 + w[2] ** 2


def ell(gp, w):
    return sp.expand(sum(g * wi for g, wi in zip(gp, w)) / 4)


gP = grad_at(F4, Ps)
w5_euler = sp.expand(sum(g * p for g, p in zip(gP, Ps)) - 4 * F4(Ps)) == 0
gap = sp.expand(F4(Ys) - F4(Ps) - sum(g * (yi - pi) for g, yi, pi in zip(gP, Ys, Ps)))
dxx = (y0 - q0) ** 2 + (y1 - q1) ** 2 + (y2 - q2) ** 2
sos = (nx(Ys) - nx(Ps)) ** 2 + 2 * nx(Ps) * dxx + (y3 - q3) ** 2 * ((y3 + q3) ** 2 + 2 * q3 ** 2)
w5_sos = sp.expand(gap - sos) == 0

p1 = [sp.sqrt(15) / 5, sp.Integer(0), sp.Integer(0), 2 * sp.sqrt(5) / 5]
p2 = [2 ** sp.Rational(-1, 4), sp.Integer(0), sp.Integer(0), 2 ** sp.Rational(-1, 4)]
rat_pts = [[sp.Rational(c.numerator, c.denominator) for c in p] for p in pts]
w5_inst = True
for p in rat_pts + [p1, p2]:
    gp = grad_at(F4, p)
    vals = (sp.expand(F4(p)), sp.expand((1 + ell(gp, p)) / 2), sp.expand((1 + ell(gp, [-c for c in p])) / 2))
    print('   boundary point %s: F = %s, e_p(p) = %s, e_p(-p) = %s' % (p, vals[0], vals[1], vals[2]))
    w5_inst = w5_inst and vals == (1, 1, 0)

grid_axis = [Fr(k, 4) for k in range(-4, 5)]
G = [w for w in itertools.product(grid_axis, repeat=4) if Fq(w) <= 1]
w5_grid = True
lo, hi = Fr(1), Fr(0)
for p in rat_pts:
    gq = [Fr(int(g.p), int(g.q)) for g in grad_at(F4, p)]
    for w in G:
        e = (1 + sum(g * wi for g, wi in zip(gq, w)) / 4) / 2
        lo, hi = min(lo, e), max(hi, e)
        w5_grid = w5_grid and 0 <= e <= 1
print('   grid: %d exact states with F <= 1; over the nine rational e_p the values range over [%s, %s]' % (len(G), lo, hi))
check('W5 SEC for the full effects: Euler identity, gradient gap = explicit sum of squares, 11 exact boundary points, '
      'grid of %d states' % len(G), w5_euler and w5_sos and w5_inst and w5_grid,
      'euler %s, sos %s, points %s, grid %s' % (w5_euler, w5_sos, w5_inst, w5_grid))

# CONTROL C2: the Euclidean 4-ball
gPb = grad_at(Fball, Ps)
c2_euler = sp.expand(sum(g * p for g, p in zip(gPb, Ps)) - 2 * Fball(Ps)) == 0
gap_b = sp.expand(Fball(Ys) - Fball(Ps) - sum(g * (yi - pi) for g, yi, pi in zip(gPb, Ys, Ps)))
c2_gap = sp.expand(gap_b - sum((yi - pi) ** 2 for yi, pi in zip(Ys, Ps))) == 0
check('C2 ball4: grad F(p).p = 2 F(p) and the gradient gap is |y - p|^2', c2_euler and c2_gap)

# COUNTERCONTROLS
COUNTER = []
sos_mut = (nx(Ys) - nx(Ps)) ** 2 + (y3 - q3) ** 2 * ((y3 + q3) ** 2 + 2 * q3 ** 2)
xw1 = sp.expand(gap - sos_mut) != 0
COUNTER.append(('XW1', xw1))
print('COUNTER XW1 %s -- the sum of squares without 2|p_x|^2|y_x - p_x|^2 is not an identity'
      % ('fails as stated' if xw1 else 'DID NOT FAIL'))

ystar = [Fr(21, 25), Fr(0), Fr(0), Fr(21, 25)]
in_body = Fq(ystar) <= 1
n1 = sp.expand(sum(c ** 2 for c in p1))
eprime_p1 = sp.expand((1 + sum(c * c for c in p1) / n1) / 2) == 1
val = sp.expand(sum(c * sp.Rational(w.numerator, w.denominator) for c, w in zip(p1, ystar)) / n1)
st0 = sp.expand(val - sp.Rational(3, 25) * (sp.sqrt(15) + 2 * sp.sqrt(5))) == 0
st1 = sp.expand(sp.sqrt(15) + 2 * sp.sqrt(5) - sp.sqrt(5) * (2 + sp.sqrt(3))) == 0
cc = sp.Rational(3, 25) * (2 + sp.sqrt(3))
st2 = sp.expand(5 * cc ** 2 - 1 - (sp.Rational(-62, 125) + sp.Rational(36, 125) * sp.sqrt(3))) == 0
a_, b_ = Fr(-62, 125), Fr(36, 125)
st3 = a_ < 0 < b_ and 3 * b_ * b_ > a_ * a_
xw2 = in_body and eprime_p1 and st0 and st1 and st2 and st3
COUNTER.append(('XW2', xw2))
print('COUNTER XW2 %s -- |p1|^2 = %s, F(y*) = %s, e\'(p1) = 1: %s, p1.y*/|p1|^2 = %s > 1 (3 b^2 = %s > a^2 = %s)'
      % ('fails as stated' if xw2 else 'DID NOT FAIL', n1, Fq(ystar), eprime_p1, val, 3 * b_ * b_, a_ * a_))

fails = [nm for nm, ok in RESULTS if not ok] + [nm + ' (did not fail)' for nm, ok in COUNTER if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len([nm for nm, ok in RESULTS if not ok])))
if not fails and len(RESULTS) == 12:
    print('VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS')
else:
    print('VERDICT NOT RENDERED: ' + '; '.join(fails))
sys.exit(0)
