#!/usr/bin/env python3
"""Coordinator's independent check of the decisive exact step in the research/equivalence thread's separation of
K-inf-Trans (R-E2.5; branch head 8c67c7fb).  Own code; reads nothing.  Run: python3 -I -B indep_checkE.py
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-E-FIXED iff all CONFIRMED.
Run 2 (run 1 kept as indep_checkE.run1.*): run 1 stated the ellipse control's curvatures backwards (1/2 at the
vertices on the long axis, 2 on the short axis); the correct values for x^2/4 + s^2 = 1 are a/b^2 = 2 and b/a^2 = 1/4.
The quartic's four zero curvatures and the circle control were already as predicted in run 1.
 X1 Omega_4 = {(x, s) in R^3 x R : |x|^4 + s^4 <= 1} is not an affine image of a Euclidean ball.  Reason: a central
    plane section of an affine image of a ball is an ellipse, and an ellipse has positive curvature at every point;
    the central section of Omega_4 by the plane x1 = x2 = 0 is bounded by the curve x^4 + s^4 = 1, whose curvature at
    (1, 0) is 0.  Checked exactly with the level-curve curvature formula; controls: the unit circle has curvature 1
    everywhere, and the ellipse x^2/4 + s^2 = 1 has curvature a/b^2 = 2 at (+-2, 0) and b/a^2 = 1/4 at (0, +-1), both positive.
    With the certified theorems TransitiveBody.lean:602 (a compact convex body carried by a boundary-transitive affine
    family is an affine image of the ball) and DenseOrbit.lean:174 (the same for a dense boundary orbit) this is the
    content of the thread's negative half: no family of affine automorphisms of Omega_4 is boundary transitive or has
    a dense boundary orbit.  (The positive half -- drivable, sharp seed, K-inf-V4, K-inf-Geom, capacity 2 -- is the
    thread's own exact record, replayed byte-identically; X2 re-checks the drivability data.)
 X2 Omega_4 is centrally symmetric about 0 and convex (the defining function is convex: |x|^4 = (x.x)^2 has Hessian
    4|x|^2 I + 8 x x^T, positive semidefinite, and s^4 is convex), and the flow R_z(t) (+) 1 and J = cyc3 (+) 1 map it
    onto itself (the function depends on |x| and s only; cyc3 permutes the x-coordinates).  J R_z(t) J^-1 = R_x(t),
    J^3 = 1, nflip = R_x(pi): the drivability pattern of KInfFoundations ball3Drive, on the quartic body.
"""
import sympy as sp
from sympy import Matrix, eye, zeros, symbols, cos, sin, pi, simplify, Rational as Q, diff, sqrt, Abs
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
x, s = symbols('x s', real=True)
def curvature(f, pt):
    fx, fs = diff(f, x), diff(f, s); fxx, fxs, fss = diff(f, x, 2), diff(f, x, s), diff(f, s, 2)
    num = fxx * fs ** 2 - 2 * fxs * fx * fs + fss * fx ** 2; den = (fx ** 2 + fs ** 2) ** Q(3, 2)
    return simplify((Abs(num) / den).subs({x: pt[0], s: pt[1]}))
print("== X1 the central section x^4 + s^4 = 1 has a flat point")
quartic = x ** 4 + s ** 4 - 1; circle = x ** 2 + s ** 2 - 1; ellipse = x ** 2 / 4 + s ** 2 - 1
k_q = [curvature(quartic, p) for p in ((1, 0), (0, 1), (-1, 0), (0, -1))]
k_c = [curvature(circle, p) for p in ((1, 0), (0, 1), (Q(3, 5), Q(4, 5)))]
k_e = [curvature(ellipse, p) for p in ((2, 0), (-2, 0), (0, 1), (0, -1))]
rec('X1', all(k == 0 for k in k_q) and all(k == 1 for k in k_c) and k_e == [2, 2, Q(1, 4), Q(1, 4)],
    'curvature 0 at the four axis points of x^4 + s^4 = 1; controls: circle 1, ellipse 2 and 1/4 (positive)', 'quartic %s, circle %s, ellipse %s' % (k_q, k_c, k_e))
print("== X2 convexity, symmetry, drivability data")
x1, x2, x3 = symbols('x1 x2 x3', real=True)
g = (x1 ** 2 + x2 ** 2 + x3 ** 2) ** 2
Hg = sp.hessian(g, (x1, x2, x3))
v = Matrix(symbols('v1 v2 v3', real=True))
quad = sp.expand((v.T * Hg * v)[0])
# Hessian of |x|^4 is 4|x|^2 I + 8 x x^T; v^T H v = 4|x|^2|v|^2 + 8 (x.v)^2 >= 0
Hform = 4 * (x1 ** 2 + x2 ** 2 + x3 ** 2) * eye(3) + 8 * Matrix([x1, x2, x3]) * Matrix([x1, x2, x3]).T
hess_ok = sp.expand(Hg - Hform) == zeros(3, 3)
t = symbols('t', real=True)
def Rz(u): return Matrix([[cos(u), -sin(u), 0], [sin(u), cos(u), 0], [0, 0, 1]])
def Rx(u): return Matrix([[1, 0, 0], [0, cos(u), -sin(u)], [0, sin(u), cos(u)]])
cyc3 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
X = Matrix([x1, x2, x3])
norm_inv_flow = simplify(((Rz(t) * X).T * (Rz(t) * X))[0] - (X.T * X)[0]) == 0
norm_inv_J = simplify(((cyc3 * X).T * (cyc3 * X))[0] - (X.T * X)[0]) == 0
conj_ok = simplify(cyc3 * Rz(t) * cyc3.T - Rx(t)) == zeros(3, 3) and cyc3 ** 3 == eye(3) and simplify(Rx(pi) - Matrix.diag(1, -1, -1)) == zeros(3, 3)
central = sp.expand((x1 ** 2 + x2 ** 2 + x3 ** 2) ** 2 + s ** 4 - ((-x1) ** 2 + (-x2) ** 2 + (-x3) ** 2) ** 2 - (-s) ** 4) == 0
rec('X2', hess_ok and norm_inv_flow and norm_inv_J and conj_ok and central,
    'Hessian of |x|^4 is 4|x|^2 I + 8 x x^T (PSD), the body is centrally symmetric, R_z(t) and cyc3 preserve |x| (hence Omega_4), cyc3 R_z cyc3^-1 = R_x, cyc3^3 = 1, R_x(pi) = nflip')
print("SUMMARY %d/%d CONFIRMED" % (sum(R), len(R)))
print("INDEP-E-FIXED" if all(R) else "INDEP-E-MISMATCH")
