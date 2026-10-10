"""E2 probe 2 -- K-inf-Trans vs K-inf-Drive on a general body  (exact: sympy symbolic identities and rationals)

QUESTION (ROADMAP.md:1018-1022 at L).  The kernel shows that one drive's flow is not boundary transitive on the ball
(`not_boundaryTransitive_flow`, OrbitGeneration.lean:620) and records that "no theorem derives transitivity from
ElementaryDrivability on a general body".  Is there a body on which ElementaryDrivability holds and NO body-preserving
family is boundary transitive -- even with the seed, singleton faces / relative strict convexity and capacity two?

THE BODY.  Omega4 = {(x, s) in R^3 x R : F(x, s) <= 1},  F(x, s) = (x0^2 + x1^2 + x2^2)^2 + s^4  (the l4-sum of the
Euclidean 3-ball and the segment).  Data:  flow t = R_z(t) (+) 1 (rotation of (x0, x1));  N = flow pi;
J = cyc3 (+) 1, (x0, x1, x2, s) -> (x2, x0, x1, s) (KInfFoundations.lean:425 on the first three coordinates);
seed r(x, s) = (1 + s)/2.

WRITTEN STEPS [W] (not checked by this script).
  W1 strict convexity: for p = (x, s) != q = (y, sg) in Omega4 and a, b > 0, a + b = 1:
     |a x + b y|^2 <= a|x|^2 + b|y|^2 (equality iff x = y), u -> u^2 strictly increasing and convex on [0, inf), and
     t -> t^4 strictly convex, so F(a p + b q) < a F(p) + b F(q) <= 1; F continuous, so a p + b q is not a boundary
     state (IsBoundaryState, KInfFoundations.lean): RelStrictConvex Omega4, hence SingletonFaces for every effect
     family (`singletonFaces_of_relStrictConvex`, KInfFoundations.lean:590 [K]).
  W2 Omega4 is compact, convex (F convex), with interior (F(0) = 0); continuity of (t, v) -> flow t v.
  W3 an affine image of a ball is {p : (p - c)^T Q (p - c) <= 1} with Q positive definite and c its unique centre of
     symmetry; Omega4 is symmetric about 0 (check D7), so c = 0 and every plane section through 0 is the sublevel set
     of a quadratic form.
  W4 with W2 and the kernel's TRB-1 `exists_affine_image_eq_eball` (TransitiveBody.lean:602) and KTRANS-DENSE-1's
     `exists_affine_image_eq_eball_of_dense` (DenseOrbit.lean:174), check D9 gives: no body-preserving G is boundary
     transitive on Omega4, and none has a dense boundary orbit.
CHECKS (exact).
  D1 F(R_z(t) x, s) = F(x, s) identically in t, x, s;  D2 R_z(t) R_z(u) = R_z(t + u), R_z(0) = I (flow_zero, flow_add);
  D3 N o N = I on R^4 and N e0 = -e0 != e0 with e0 in Omega4 (N_involutive, N_moves);
  D4 F(J v) = F(v) and F(J^-1 v) = F(v) identically (J_preserves, J_symm_preserves);
  D5 J (flow(pi/2) (J^-1 e1)) = e2 while flow(s) e1 has third coordinate 0 for every s (J_off_axis, t = pi/2, x = e1);
  D6 r is an effect on Omega4 given |s| <= 1 there (s^4 <= F), r(0,0,0,1) = 1, r(0,0,0,-1) = 0 (SharpSeed);
  D7 F(-v) = F(v) (central symmetry, hence capacity <= 2 by Lemma D, KInfFoundations.lean:632 [K]);
  D8 strict-convexity instances: F at the midpoint of every pair of distinct exact boundary points of a list
     (rational points on {s = 0, |x| = 1} and {x = 0, s = +-1}) is < 1;
  D9 the section {x1 = x2 = 0} is {u^4 + v^4 <= 1}; if it were {A u^2 + 2 B u v + C v^2 <= 1}, the boundary points
     (1, 0), (0, 1), (t, t), (t, -t) with t^4 = 1/2 force A = C = 1 and two incompatible values of B -- an exact
     contradiction (with tau = t^2, tau^2 = 1/2: both equations give 1/tau = 2, i.e. tau^2 = 1/4 != 1/2).
  CONTROL C1: the same checks D1-D5 hold for the Euclidean 4-ball {|x|^2 + s^2 <= 1} and D9's contradiction does NOT
     arise there (the section is the unit disk, A = C = 1, B = 0 consistent) -- the non-ellipse step is not vacuous.
DECISION RULE (fixed before the first run).  VERDICT DRIVE-SEED-GEOM-CAP2-NOT-TRANS iff D1-D9 and C1 all pass.  The
verdict means: on Omega4 (chart dimension 4) ElementaryDrivability, a sharp seed, relative strict convexity (W1) and
capacity <= 2 hold, and no body-preserving family is boundary transitive or has a dense boundary orbit (W3, W4 with the
kernel theorems).  It says nothing about chart dimension 3, and nothing about OI's sourcing of any of these premises.
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

fails = [nm for nm, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(fails)))
if not fails:
    print('VERDICT DRIVE-SEED-GEOM-CAP2-NOT-TRANS')
else:
    print('VERDICT NOT RENDERED: ' + '; '.join(fails))
sys.exit(0)
