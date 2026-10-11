"""E13 probe b -- a centrally symmetric, self-dual, drivable, strictly convex body in chart dimension 4, no ellipsoid.

Written 2026-10-11T01:15Z (date -u read at 01:15:11Z), after NOTES-E13 S0-b and before the first run.

COORDINATES.  On the state cone in R^5 write u = T + S, v = T - S and X in R^3.  The inner product is
<z, w>_M = (4/5) u u' + (1/5) v v' + X.X'  =  T T' + S S' + (3/5)(T S' + S T') + X.X'.
The cone is C = {(u, v, X) : u, v >= 0, |X| <= F(u, v)} with F concave and 1-homogeneous; U = {F >= 1} is the region
on and above the curve Gamma, so C^{*M} = C iff U equals its M-antipolar {y : <Mx, y> >= 1 for all x in U}, i.e. iff
Gamma is its own M-polar curve (the envelope of the polar lines {y : <Mx, y> = 1}, x on Gamma).
Gamma = union over j of g^j(B0 u E0), g(u, v) = (u/4, 4v):
  J0 = (11/13, 19/13), on the ellipse <Mx, x> = 1 (4u^2 + v^2 = 5);
  B0 = the arc from swap J0 = (19/13, 11/13) to J0 of the circle  u^2 + v^2 - (1254/325)(u + v) + 5114/845 = 0
       (centre (627/325, 627/325); swap symmetric; tangent at J0 to the polar line of J0);
  E0 = the arc from J0 to g swap J0 = (19/52, 44/13) of the M-polar conic of that circle, A_E = Mt adj(A_B) Mt with
       Mt = diag(4/5, 1/5, -1) (homogeneous coordinates (u, v, 1)).
The body: Omega_cs = {(X, S) in R^3 x R : |X| <= F(1 + S, 1 - S)}; central symmetry (X, S) -> (-X, -S) is the cone map
Z(u, v, X) = (v, u, -X).

CHECKS (exact rational arithmetic; sympy only for exact matrix identities, ranks and root counts).
  B1  J0 on the ellipse; the circle is swap symmetric, passes through J0 and swap J0, and its tangent at J0 is the polar
      line of J0 (normal parallel to M J0).
  B2  C^1 closure: A_E passes through J0 with the same tangent, and through g swap J0 with the tangent of g(B0) there.
  B3  the arcs: both conics non-degenerate; endpoint slopes -19/44 -> -44/19 on B0 and -44/19 -> -76/11 on E0 (one
      slope sequence along the chain); E0's upper root is real on all of [19/52, 11/13] (no root of the discriminant
      there, exact Sturm count); v'' > 0 at the exact points used below (the arc is convex towards U).
  B4  symmetries: A_B swap invariant; swap(A_E) = g^-1(A_E) as conics (P A_E P proportional to G^T A_E G); the lemma's
      filter: M is not Z-invariant and M^-1 Z M Z = g (5 x 5, exact).
  B5  self-positivity: <Mx, y> >= 1 for every pair of the exact points (six on B0, six on E0, J0, swap J0, g swap J0,
      their images under g^-1, g^0, g^1 and swap); the equality pairs are counted.
  B6  polar partners: for each exact point p of B0 (resp. E0) the pole of the tangent line at p lies on E0 (resp. B0),
      pairs with p to exactly 1, and the polar line of p is tangent to that conic there.
  B7  C^{*M} <= C on instances: for w = (lambda p, X), |X| = 1, lambda in {1/2, 9/10, 999/1000} (outside C since
      F(lambda p) = lambda < 1), the cone point z = (partner(p), -X) has <z, w>_M = lambda - 1 < 0.
  B8  no ellipsoid: three exact points of B0 and three of E0 lie on no common conic (6 x 6 rank 6).
  B9  seams of Omega_cs: rotation (cos 3/5) and the cyclic permutation preserve |X|^2; J rot(pi) J^-1 moves the state
      ((0, 0, 1/2), 0), which lies in Omega_cs since (2, 2) is in U; the seed (1 + S)/2 is 1 and 0 at the poles; the
      central symmetry: swap maps the exact points of Gamma to points of Gamma.
  B10 strict convexity instances: midpoints of 15 pairs on B0 and 15 pairs on E0 lie strictly inside U.
  P1  control, the polygon with vertices (4^-j, 4^j), |j| <= 6: each edge line is {y : <M w_{-j}, y> = 1}, so the
      polygonal region is M-self-dual too (vertex/edge duality with j -> -j).
COUNTERCONTROLS (each must fail as stated).
  XB1 "some inner product invariant under Z and the rotations, [[a, b], [b, a]] + c I in (u, v, X), makes the circle its
      own polar" -- the 2 x 2 minors of (A_B, its polar matrix) have no common zero with a > |b|.
  XB2 "the polar conic of the circle through J0 and swap J0 with centre (2, 2) passes through J0" -- its tangent at J0
      is not the polar line of J0.

DECISION RULE (fixed before the first run).  VERDICT E13-CS-SELFDUAL-DRIVABLE-NOT-TRANS iff B1 ... B10 and P1 all pass
and XB1 and XB2 both fail as stated; otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says that
the identities and instances hold exactly; the general statements (Gamma is a C^1 strictly convex self-polar chain,
hence C^{*M} = C; strict convexity of the body of revolution; the lemma L-a/L-b) are the written arguments of
NOTES-E13, and non-transitivity for every body-preserving family follows from B8 with TransitiveBody.lean:602 and
DenseOrbit.lean:174.
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


def R(x):
    return sp.Rational(x.numerator, x.denominator)


def Fq(x):
    x = sp.Rational(x)
    return Fr(int(x.p), int(x.q))


m1, m2 = Fr(4, 5), Fr(1, 5)


def pairM(x, y):
    return m1 * x[0] * y[0] + m2 * x[1] * y[1]


def g(p, j=1):
    f = Fr(4) ** j
    return (p[0] / f, p[1] * f)


def swap(p):
    return (p[1], p[0])


J0 = (Fr(11, 13), Fr(19, 13))
sJ0 = swap(J0)
gsJ0 = g(sJ0)
cc = sp.Rational(627, 325)
AB = sp.Matrix([[1, 0, -cc], [0, 1, -cc], [-cc, -cc, sp.Rational(5114, 845)]])
Mt = sp.diag(sp.Rational(4, 5), sp.Rational(1, 5), -1)
AE = Mt * AB.adjugate() * Mt
ABf = [[Fq(AB[i, k]) for k in range(3)] for i in range(3)]
AEf = [[Fq(AE[i, k]) for k in range(3)] for i in range(3)]


def Q(A, p):
    x = (p[0], p[1], Fr(1))
    return sum(A[i][k] * x[i] * x[k] for i in range(3) for k in range(3))


def grad(A, p):
    x = (p[0], p[1], Fr(1))
    return tuple(2 * sum(A[i][k] * x[k] for k in range(3)) for i in range(2))


def parallel(a, b):
    return a[0] * b[1] - a[1] * b[0] == 0


def same_dir(a, b):
    return parallel(a, b) and a[0] * b[0] + a[1] * b[1] > 0


def slope(A, p):
    gq = grad(A, p)
    return -gq[0] / gq[1]


def second_point(A, p0, k):
    d = (Fr(1), Fr(k))
    gq = grad(A, p0)
    q2 = sum(A[i][j] * d[i] * d[j] for i in range(2) for j in range(2))
    t = -(gq[0] * d[0] + gq[1] * d[1]) / q2
    return (p0[0] + t * d[0], p0[1] + t * d[1])


ccf = Fq(cc)


def on_B0(p):
    return Q(ABf, p) == 0 and p[0] < ccf and p[1] < ccf and J0[0] <= p[0] <= sJ0[0]


def on_E0(p):
    return Q(AEf, p) == 0 and gsJ0[0] <= p[0] <= J0[0] and grad(AEf, p)[1] > 0


def partner(A, p):
    gq = grad(A, p)
    s = gq[0] * p[0] + gq[1] * p[1]
    ell = (gq[0] / s, gq[1] / s)          # tangent line at p is {y : ell . y = 1}
    return (ell[0] / m1, ell[1] / m2)      # its pole: M q = ell


Mvec = lambda p: (m1 * p[0], m2 * p[1])

# ---------------------------------------------------------------- B1
ok1 = pairM(J0, J0) == 1
ok1 &= AB == sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]) * AB * sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
ok1 &= Q(ABf, J0) == 0 and Q(ABf, sJ0) == 0
ok1 &= parallel(grad(ABf, J0), Mvec(J0))
check('B1 J0 self-polar; the circle symmetric, through J0 and swap J0, tangent there to the polar line of J0', ok1)

# ---------------------------------------------------------------- B2
gB_tan = (grad(ABf, sJ0)[0] * 4, grad(ABf, sJ0)[1] / 4)   # normal of g(B0) at g swap J0: g^-T applied
ok2 = Q(AEf, J0) == 0 and parallel(grad(AEf, J0), grad(ABf, J0))
ok2 &= Q(AEf, gsJ0) == 0 and parallel(grad(AEf, gsJ0), gB_tan)
check('B2 C^1 closure at J0 and at g swap J0', ok2,
      'g swap J0 = %s' % (gsJ0,))

# ---------------------------------------------------------------- B3
ok3 = AB.det() != 0 and AE.det() != 0
sl = [slope(ABf, sJ0), slope(ABf, J0), slope(AEf, J0), slope(AEf, gsJ0)]
ok3 &= sl == [Fr(-19, 44), Fr(-44, 19), Fr(-44, 19), Fr(-76, 11)]
uu, vv = sp.symbols('uu vv')
QE = sp.expand((sp.Matrix([uu, vv, 1]).T * AE * sp.Matrix([uu, vv, 1]))[0])
pv = sp.Poly(QE, vv)
a2, a1, a0 = pv.all_coeffs()
disc = sp.Poly(sp.expand(a1 ** 2 - 4 * a2 * a0), uu)
nroots = disc.count_roots(R(gsJ0[0]), R(J0[0]))
ok3 &= nroots == 0 and disc.eval(R(gsJ0[0])) > 0 and a2.is_positive
check('B3 non-degenerate conics; endpoint slopes; E0 a single real arc over [19/52, 11/13]', ok3,
      'slopes %s, discriminant roots in the interval: %d' % ([str(s) for s in sl], nroots))

# ---------------------------------------------------------------- points on the arcs
kB = [Fr(-2), Fr(-3, 2), Fr(-5, 4), Fr(-7, 4), Fr(-9, 8), Fr(-17, 8)]
kE = [Fr(-5, 2), Fr(-3), Fr(-7, 2), Fr(-11, 4), Fr(-13, 4), Fr(-15, 4)]
PB = [second_point(ABf, J0, k) for k in kB]
PE = [second_point(AEf, J0, k) for k in kE]
arc_ok = all(on_B0(p) for p in PB) and all(on_E0(p) for p in PE)


def vpp(A, p):
    # v'' along the conic (implicit differentiation), sign only
    Au, Av = grad(A, p)
    Auu, Auv, Avv = 2 * A[0][0], 2 * A[0][1], 2 * A[1][1]
    return -(Auu * Av ** 2 - 2 * Auv * Au * Av + Avv * Au ** 2) / Av ** 3


conv_ok = all(vpp(ABf, p) > 0 for p in PB) and all(vpp(AEf, p) > 0 for p in PE)

# ---------------------------------------------------------------- B4
P3 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
G3 = sp.diag(sp.Rational(1, 4), 4, 1)
L, Rm = P3 * AE * P3, G3.T * AE * G3
ratio = L[2, 2] / Rm[2, 2]
ok4 = L == ratio * Rm and ratio != 0
M5 = sp.diag(sp.Rational(4, 5), sp.Rational(1, 5), 1, 1, 1)
Z5 = sp.Matrix([[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, -1]])
g5 = sp.diag(sp.Rational(1, 4), 4, 1, 1, 1)
ok4 &= Z5.T * M5 * Z5 != M5 and M5.inv() * Z5 * M5 * Z5 == g5
check('B4 symmetries: circle swap invariant; swap(E0) = g^-1(E0); M not Z-invariant, M^-1 Z M Z = g', ok4 and ok1,
      'proportionality factor %s' % ratio)

# ---------------------------------------------------------------- B5
base = PB + PE + [J0, sJ0, gsJ0]
pts = []
for p in base:
    for j in (-1, 0, 1):
        for q in (g(p, j), swap(g(p, j))):
            if q not in pts:
                pts.append(q)
pairs = list(itertools.product(pts, pts))
vals = [pairM(x, y) for x, y in pairs]
n_eq = sum(1 for t in vals if t == 1)
ok5 = arc_ok and all(t >= 1 for t in vals)
check('B5 self-positivity <Mx, y> >= 1 on all pairs of %d exact points of Gamma' % len(pts), ok5,
      '%d pairs, %d with equality, min %s' % (len(pairs), n_eq, min(vals)))

# ---------------------------------------------------------------- B6
ok6 = arc_ok
for p in PB + [J0]:
    q = partner(ABf, p)
    ok6 &= on_E0(q) and pairM(p, q) == 1 and parallel(grad(AEf, q), Mvec(p))
for p in PE + [J0]:
    q = partner(AEf, p)
    ok6 &= on_B0(q) and pairM(p, q) == 1 and parallel(grad(ABf, q), Mvec(p))
check('B6 polar partners: B0 <-> E0 with pairing exactly 1 and tangency', ok6,
      'partner(J0) = %s' % (partner(ABf, J0),))

# ---------------------------------------------------------------- B7
ok7 = ok6
for p in PB + PE:
    A = ABf if p in PB else AEf
    q = partner(A, p)
    for lam in (Fr(1, 2), Fr(9, 10), Fr(999, 1000)):
        Xw = (Fr(3, 5), Fr(4, 5), Fr(0))           # |X| = 1
        Xz = tuple(-c for c in Xw)
        val = pairM(q, (lam * p[0], lam * p[1])) + sum(a * b for a, b in zip(Xz, Xw))
        ok7 &= val == lam - 1 and val < 0
check('B7 C^{*M} <= C: 36 outside points, each with an exact separating cone point', ok7)

# ---------------------------------------------------------------- B8
six = PB[:3] + PE[:3]
rank8 = sp.Matrix([[R(a) ** 2, R(a) * R(b), R(b) ** 2, R(a), R(b), 1] for a, b in six]).rank()
check('B8 Gamma lies on no conic (3 + 3 exact points, rank 6)', rank8 == 6, 'rank %d' % rank8)

# ---------------------------------------------------------------- B9
X0, X1, X2 = sp.symbols('X0 X1 X2', real=True)
cs, sn = sp.Rational(3, 5), sp.Rational(4, 5)
n2 = X0 ** 2 + X1 ** 2 + X2 ** 2
ok9 = sp.expand((cs * X0 - sn * X1) ** 2 + (sn * X0 + cs * X1) ** 2 + X2 ** 2 - n2) == 0
ok9 &= sp.expand(X2 ** 2 + X0 ** 2 + X1 ** 2 - n2) == 0
x = (Fr(0), Fr(0), Fr(1, 2))
img = (x[1], x[2], x[0])                           # J^-1 (cyc3.symm), then rot(pi), then J (cyc3), as in ball3Drive
img = (-img[0], -img[1], img[2])
img = (img[2], img[0], img[1])
ok9 &= img == (Fr(0), Fr(0), Fr(-1, 2))
two = (Fr(2), Fr(2))
ok9 &= Q(ABf, two) < 0                             # (2, 2) inside the circle on the diagonal beyond B0: in U
seed = lambda s: (1 + s) / 2
ok9 &= seed(Fr(1)) == 1 and seed(Fr(-1)) == 0
ok9 &= all(on_B0(swap(p)) for p in PB) and all(on_E0(g(swap(p))) for p in PE)
check('B9 drive on X, J off axis at ((0,0,1/2),0) in Omega_cs, seed, central symmetry on the exact points', ok9,
      'J rot(pi) J^-1 (0,0,1/2) = %s' % (img,))

# ---------------------------------------------------------------- B10
ok10 = conv_ok
cnt = 0
for p, q in itertools.combinations(PB, 2):
    mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    ok10 &= Q(ABf, mid) < 0
    cnt += 1
for p, q in itertools.combinations(PE, 2):
    mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    ok10 &= Q(AEf, mid) > 0 and grad(AEf, mid)[1] > 0 and gsJ0[0] <= mid[0] <= J0[0]
    cnt += 1
check('B10 strict convexity: %d midpoints strictly inside U; v\'\' > 0 at the 12 exact points' % cnt,
      ok10 and cnt == 30)

# ---------------------------------------------------------------- P1
okP = True
w = {j: (Fr(1, 4 ** j) if j >= 0 else Fr(4 ** (-j)), Fr(4 ** j) if j >= 0 else Fr(1, 4 ** (-j))) for j in range(-6, 7)}
for j in range(-5, 6):
    a_, b_ = w[j], w[j + 1]
    ell = Mvec(w[-j])
    okP &= ell[0] * a_[0] + ell[1] * a_[1] == 1 and ell[0] * b_[0] + ell[1] * b_[1] == 1
okP &= all(pairM(w[i], w[k]) >= 1 for i in w for k in w)
check('P1 control: the polygon with vertices (4^-j, 4^j) is M-self-dual (edge j = polar line of vertex -j)', okP)

# ---------------------------------------------------------------- countercontrols
a_s, b_s = sp.symbols('a_s b_s', real=True)
Mt0 = sp.Matrix([[a_s, b_s, 0], [b_s, a_s, 0], [0, 0, -1]])
AD = Mt0 * AB.adjugate() * Mt0
ent = lambda A: [A[0, 0], A[0, 1], A[0, 2], A[1, 1], A[1, 2], A[2, 2]]
e1, e2 = ent(AB), ent(AD)
minors = [sp.expand(e1[i] * e2[k] - e1[k] * e2[i]) for i in range(6) for k in range(i + 1, 6)]
minors = [mm for mm in minors if mm != 0]
sols = sp.solve(minors, [a_s, b_s], dict=True)
admissible = []
for s_ in sols:
    av, bv = s_.get(a_s, a_s), s_.get(b_s, b_s)
    if av.free_symbols or bv.free_symbols:
        admissible.append(s_)          # a family: counted as admissible (would make the countercontrol hold)
    elif av.is_real and bv.is_real and av > abs(bv):
        admissible.append(s_)
xb1_holds = len(admissible) > 0
print('COUNTER XB1 ' + ('DID NOT FAIL' if xb1_holds else 'fails as stated') +
      ' -- solutions of the minors: %s' % sols, flush=True)
Aalt = sp.Matrix([[1, 0, -2], [0, 1, -2], [-2, -2, 8 - sp.Rational(274, 169)]])
Aaltf = [[Fq(Aalt[i, k]) for k in range(3)] for i in range(3)]
AaltE = Mt * Aalt.adjugate() * Mt
AaltEf = [[Fq(AaltE[i, k]) for k in range(3)] for i in range(3)]
alt_ok = Q(Aaltf, J0) == 0 and Q(Aaltf, sJ0) == 0
xb2_holds = Q(AaltEf, J0) == 0
print('COUNTER XB2 ' + ('DID NOT FAIL' if (xb2_holds or not alt_ok) else 'fails as stated') +
      ' -- polar conic of the (2,2)-circle at J0: %s' % Q(AaltEf, J0), flush=True)

failures = [n for n, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(failures)), flush=True)
if not failures and not xb1_holds and alt_ok and not xb2_holds:
    print('VERDICT E13-CS-SELFDUAL-DRIVABLE-NOT-TRANS', flush=True)
else:
    print('VERDICT NOT RENDERED -- failing: %s' % failures, flush=True)
sys.exit(0)
