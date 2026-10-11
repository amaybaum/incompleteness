"""E13 probe -- a self-dual, drivable, strictly convex body in chart dimension 4 that is not boundary transitive.

Written 2026-10-11T00:47Z (date -u read at 00:45:34Z before NOTES-E13's S0), before the first run.

THE BODY.  Omega* = {(X, S) in R^3 x R : |X|^3 <= (1 + S)(1 - S)^2, |S| <= 1}.  Its state cone is
C = {(T, X, S) : T >= |S|, |X|^3 <= (T + S)(T - S)^2}, i.e. with u = T + S, v = T - S the generalized power cone
P = {(u, v, X) : u, v >= 0, u^(1/3) v^(2/3) >= |X|}.  Claim: C is self-dual for the inner product
<z, w>_M = (1/3) u u' + (2/3) v v' + X.X' = T T' + S S' - (1/3)(T S' + S T') + X.X'.
Membership of a rational point is decided exactly: u, v >= 0 and (X.X)^3 <= (u v^2)^2.

CHECKS.
  A1  C is a cone whose T = 1 section is Omega* (degree-3 homogeneity of both sides, symbolic).
  A2  the inner product: M_TXS = P^T diag(1/3, 2/3, 1, 1, 1) P for the coordinate change P, positive definite; the
      weighted AM-GM step as the exact factorization a^3 + 2 b^3 - 3 a b^2 = (a - b)^2 (a + 2 b) (with a = (uu')^(1/3),
      b = (vv')^(1/3): (1/3) uu' + (2/3) vv' >= (uu')^(1/3) (vv')^(2/3)).
  A3  C <= C^{*M}: <z, w>_M >= 0 for 60 pairs of exact rational cone points.
  A4  C^{*M} <= C: for 60 exact rational points w outside C, an explicit rational z in C (membership checked exactly)
      with <z, w>_M < 0.
  A5  drivability with Omega_4's drive: the rotation of (X0, X1) at cos t = 3/5 preserves the membership polynomial
      identically; the half-turn is an involution moving e1; the cyclic permutation J of X preserves it; J_off_axis:
      J rot(pi) J^-1 sends the state (X, S) = ((0,0,1), 0) of Omega* to ((0,0,-1), 0), which every rotation of (X0, X1)
      fixes.
  A6  the sharp seed (1 + S)/2: values in [0, 1] on Omega* (|S| <= 1), value 1 at the state (0, 1), 0 at (0, -1).
  A7  strict convexity: the profile f(S) = (1+S)^(1/3) (1-S)^(2/3) satisfies f''/f = -(2/9)(p + q)^2 with
      p = 1/(1+S), q = 1/(1-S) (symbolic), so f is strictly concave on (-1, 1); exact instances: midpoints of 30 pairs
      of distinct boundary points lie strictly inside.
  A8  capacity: the seed and its complement distinguish the two poles (two perfectly distinguishable states).
  A9  not an ellipsoid: the section {X1 = X2 = 0} has the rational boundary points (+-u, S) with
      u = 2m/(m^3+1), S = (m^3-1)/(m^3+1) (m = 0, 1/3, 1/2, 1, 2, 3, and m -> oo); the 14 x 6 conic system has rank 6,
      so no conic contains them.
  A10 non-transitivity by an affine invariant: along the meridian, (1 - S)^2 * 2 m^3 = u^3 (m^3 + 1) and
      4 (1 + S) = u^3 (m^3 + 1)^2 identically in m, so the contact order of the boundary with its tangent hyperplane is
      3/2 at the pole S = 1 ((1-S)^2 ~ u^3/2) and 3 at the pole S = -1 ((1+S) ~ u^3/4); at the regular point
      m = 1 the meridian has finite nonzero second derivative (order 2).
  A11 control, the Euclidean ball (alpha = 1/2, the Lorentz cone): the AM-GM step is (a - b)^2 >= 0, the inner product
      has no cross term, A3 holds on 30 pairs, and its meridian section points lie on a conic (rank 5).
COUNTERCONTROLS (each must fail as stated).
  XS1 the inner product without its cross term, TT' + SS' + X.X', does not satisfy C <= C^*: the cone points
      z = (1, (21/20, 0, 0), -3/10) and w = (1, (-21/20, 0, 0), -3/10) pair to -1/80.
  XS2 the opposite cross term, + (1/3)(TS' + ST'), fails on the same pair (-17/80).

DECISION RULE (fixed before the first run).  VERDICT E13-SELFDUAL-DRIVABLE-NOT-TRANS iff A1 ... A11 all pass and XS1
and XS2 both fail as stated; otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says that the
identities and instances hold exactly; the general statements (self-duality of C for all points, strict convexity of
the body of revolution, affine invariance of contact order, capacity <= 2 from relative strict convexity) are the
written arguments of NOTES-E13, and the non-transitivity for every family follows from A10 (or from A9 with the kernel
theorems TransitiveBody.lean:602 and DenseOrbit.lean:174).
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


def in_cone(T, X, S, alpha_third=True):
    u, v = T + S, T - S
    if u < 0 or v < 0:
        return False
    xx = sum(c * c for c in X)
    if alpha_third:
        return xx ** 3 <= (u * v * v) ** 2
    return xx <= u * v          # alpha = 1/2: |X|^2 <= u v (Lorentz cone)


def pair_M(z, w, cross=Fr(-1, 3)):
    (T, X, S), (T2, X2, S2) = z, w
    return T * T2 + S * S2 + cross * (T * S2 + S * T2) + sum(a * b for a, b in zip(X, X2))


def rnd(k, mod, den):
    return Fr((k * 7919) % mod - mod // 2, den)


def cone_point(k, alpha_third=True):
    T = Fr(1 + (k % 5), 2)
    S = T * Fr((k * 37) % 19 - 9, 10)
    direction = (rnd(k + 1, 13, 3), rnd(k + 2, 11, 4), rnd(k + 3, 7, 2))
    scale = Fr(2)
    while not in_cone(T, tuple(scale * d for d in direction), S, alpha_third):
        scale /= 2
        if scale < Fr(1, 2 ** 40):
            return (T, (Fr(0), Fr(0), Fr(0)), S)
    return (T, tuple(scale * d for d in direction), S)


# ---------------------------------------------------------------- A1
Ts, Ss, lam = sp.symbols('T S lam', positive=True)
X0, X1, X2 = sp.symbols('X0 X1 X2', real=True)
lhs = sp.expand(((lam * Ts + lam * Ss) * (lam * Ts - lam * Ss) ** 2) - lam ** 3 * (Ts + Ss) * (Ts - Ss) ** 2)
rhs = sp.expand((lam ** 2 * (X0 ** 2 + X1 ** 2 + X2 ** 2)) ** 3 - lam ** 6 * (X0 ** 2 + X1 ** 2 + X2 ** 2) ** 3)
sec = sp.expand(((1 + Ss) * (1 - Ss) ** 2) - ((Ts + Ss) * (Ts - Ss) ** 2).subs(Ts, 1))
check('A1 cone homogeneity and the T = 1 section', lhs == 0 and rhs == 0 and sec == 0)

# ---------------------------------------------------------------- A2
Pm = sp.Matrix([[1, 0, 0, 0, 1], [1, 0, 0, 0, -1], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0]])  # (T,X0,X1,X2,S)->(u,v,X)
Dm = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3), 1, 1, 1)
MT = Pm.T * Dm * Pm
expected = sp.Matrix([[1, 0, 0, 0, -sp.Rational(1, 3)], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0],
                      [-sp.Rational(1, 3), 0, 0, 0, 1]])
pd = all(MT[:k, :k].det() > 0 for k in range(1, 6))
a, b = sp.symbols('a b', nonnegative=True)
amgm = sp.expand(a ** 3 + 2 * b ** 3 - 3 * a * b ** 2 - (a - b) ** 2 * (a + 2 * b)) == 0
check('A2 inner product M = P^T diag(1/3,2/3,1,1,1) P, positive definite; AM-GM factorization',
      MT == expected and pd and amgm)

# ---------------------------------------------------------------- A3
pts = [cone_point(k) for k in range(120)]
ok3 = all(in_cone(*p) for p in pts) and all(pair_M(pts[2 * i], pts[2 * i + 1]) >= 0 for i in range(60))
check('A3 C <= C^{*M} on 60 exact pairs', ok3)


# ---------------------------------------------------------------- A4
def witness_outside(w):
    T2, Xw, S2 = w
    u2, v2 = T2 + S2, T2 - S2
    if u2 < 0:
        return (Fr(1, 2), (Fr(0), Fr(0), Fr(0)), Fr(1, 2))         # u = 1, v = 0
    if v2 < 0:
        return (Fr(1, 2), (Fr(0), Fr(0), Fr(0)), Fr(-1, 2))        # u = 0, v = 1
    xx = sum(c * c for c in Xw)
    if u2 == 0:
        # u' = 0, v' > 0, X' != 0: z = (u, v, -X') with v = (X'.X')/(2 v'), u v^2 = ((X'.X') + 1)^2 >= |X'|^3
        vv = xx / (2 * v2)
        uu = (xx + 1) ** 2 / vv ** 2
        return ((uu + vv) / 2, tuple(-c for c in Xw), (uu - vv) / 2)
    if v2 == 0:
        # v' = 0, u' > 0, X' != 0: z = (u, v, -X') with u = (X'.X')/u', v = ((X'.X') + 1)(1 + 1/u)
        uu = xx / u2
        vv = (xx + 1) * (1 + 1 / uu)
        return ((uu + vv) / 2, tuple(-c for c in Xw), (uu - vv) / 2)
    k = Fr(1)
    base = k / xx
    for j in range(1, 80):
        c = base * (1 + Fr(1, 2 ** j))
        z_u, z_v = k / u2, k / v2
        z = ((z_u + z_v) / 2, tuple(-c * cc for cc in Xw), (z_u - z_v) / 2)
        if in_cone(*z) and pair_M(z, w) < 0:
            return z
    return None


def outside_point(k):
    T = Fr(1 + (k % 4), 3)
    S = T * Fr((k * 29) % 23 - 11, 10)
    X = (rnd(k + 5, 17, 2), rnd(k + 6, 13, 3), rnd(k + 7, 9, 2))
    if all(c == 0 for c in X):
        X = (Fr(1), Fr(0), Fr(0))
    m = Fr(1)
    while in_cone(T, tuple(m * x for x in X), S):
        m *= 2
    return (T, tuple(m * x for x in X), S)


outs = [outside_point(k) for k in range(60)]
wit = [witness_outside(w) for w in outs]
ok4 = all(not in_cone(*w) for w in outs) and all(z is not None and in_cone(*z) and pair_M(z, w) < 0
                                                  for z, w in zip(wit, outs))
check('A4 C^{*M} <= C: 60 outside points, each with an exact separating cone point', ok4)

# ---------------------------------------------------------------- A5
cs, sn = sp.Rational(3, 5), sp.Rational(4, 5)
Sv = sp.symbols('Sv', real=True)
memb = lambda x0, x1, x2, s: (x0 ** 2 + x1 ** 2 + x2 ** 2) ** 3 - ((1 + s) * (1 - s) ** 2) ** 2
rot = memb(cs * X0 - sn * X1, sn * X0 + cs * X1, X2, Sv)
cyc = memb(X2, X0, X1, Sv)
base_m = memb(X0, X1, X2, Sv)
ok5 = sp.expand(rot - base_m) == 0 and sp.expand(cyc - base_m) == 0


def rotpi(x):
    return (-x[0], -x[1], x[2])


def J(x):
    return (x[2], x[0], x[1])


def Jinv(x):
    return (x[1], x[2], x[0])


e1 = (Fr(1), Fr(0), Fr(0))
ok5 &= rotpi(rotpi(e1)) == e1 and rotpi(e1) != e1
x = (Fr(0), Fr(0), Fr(1))
img = J(rotpi(Jinv(x)))
ok5 &= in_cone(Fr(1), x, Fr(0)) and img == (Fr(0), Fr(0), Fr(-1))
check('A5 drive: rotation and J preserve the body; N involutive and moving; J off axis', ok5,
      'J rot(pi) J^-1 (0,0,1) = %s' % (img,))

# ---------------------------------------------------------------- A6
ok6 = in_cone(Fr(1), (0, 0, 0), Fr(1)) and in_cone(Fr(1), (0, 0, 0), Fr(-1))
ok6 &= all(0 <= (1 + p[2] / p[0]) / 2 <= 1 for p in pts)
check('A6 sharp seed (1 + S)/2', ok6)

# ---------------------------------------------------------------- A7
f = (1 + Sv) ** sp.Rational(1, 3) * (1 - Sv) ** sp.Rational(2, 3)
g = sp.log(f)
gp = sp.diff(sp.expand_log(g, force=True), Sv)
gpp = sp.diff(gp, Sv)
p_, q_ = 1 / (1 + Sv), 1 / (1 - Sv)
ok7 = sp.cancel(gpp + gp ** 2 + sp.Rational(2, 9) * (p_ + q_) ** 2) == 0


def meridian(m):
    m = Fr(m)
    return (2 * m / (m ** 3 + 1), (m ** 3 - 1) / (m ** 3 + 1))


ms = [Fr(1, 3), Fr(1, 2), Fr(1), Fr(2), Fr(3), Fr(2, 3), Fr(3, 2), Fr(5, 4)]
bpts = []
for m in ms:
    uu, ss = meridian(m)
    ok7 &= (uu ** 2) ** 3 == ((1 + ss) * (1 - ss) ** 2) ** 2       # on the boundary
    for rotq in [(Fr(1), Fr(0)), (Fr(3, 5), Fr(4, 5)), (Fr(-5, 13), Fr(12, 13))]:
        bpts.append(((uu * rotq[0], uu * rotq[1], Fr(0)), ss))
mid_ok = True
cnt = 0
for (Xa, Sa), (Xb, Sb) in itertools.combinations(bpts, 2):
    if cnt >= 30:
        break
    if (Xa, Sa) == (Xb, Sb):
        continue
    Xm = tuple((p + q) / 2 for p, q in zip(Xa, Xb))
    Sm = (Sa + Sb) / 2
    um, vm = 1 + Sm, 1 - Sm
    mid_ok &= sum(c * c for c in Xm) ** 3 < (um * vm * vm) ** 2
    cnt += 1
check('A7 strict concavity of the profile (symbolic) and 30 strict midpoints', ok7 and mid_ok and cnt == 30)

# ---------------------------------------------------------------- A8
seed = lambda s: (1 + s) / 2
ok8 = seed(Fr(1)) == 1 and seed(Fr(-1)) == 0 and (1 - seed(Fr(-1))) == 1 and (1 - seed(Fr(1))) == 0
check('A8 two perfectly distinguishable states (the poles)', ok8)

# ---------------------------------------------------------------- A9
sec_pts = [(Fr(0), Fr(-1)), (Fr(0), Fr(1))]
for m in [Fr(1, 3), Fr(1, 2), Fr(1), Fr(2), Fr(3), Fr(3, 2)]:
    uu, ss = meridian(m)
    sec_pts += [(uu, ss), (-uu, ss)]
rows = [[u0 ** 2, u0 * s0, s0 ** 2, u0, s0, 1] for u0, s0 in sec_pts]
rank9 = sp.Matrix(rows).rank()
check('A9 the meridian section lies on no conic (14 points, rank 6)', rank9 == 6 and len(sec_pts) == 14,
      'rank %d' % rank9)

# ---------------------------------------------------------------- A10
msym = sp.symbols('m', positive=True)
U = 2 * msym / (msym ** 3 + 1)
Sm_ = (msym ** 3 - 1) / (msym ** 3 + 1)
id_top = sp.cancel((1 - Sm_) ** 2 * 2 * msym ** 3 - U ** 3 * (msym ** 3 + 1)) == 0
id_bot = sp.cancel(4 * (1 + Sm_) - U ** 3 * (msym ** 3 + 1) ** 2) == 0
lim_top = sp.limit((msym ** 3 + 1) / (2 * msym ** 3), msym, sp.oo)
lim_bot = sp.limit((msym ** 3 + 1) ** 2 / 4, msym, 0)
dS = sp.diff(Sm_, msym) / sp.diff(U, msym)
d2S = sp.diff(dS, msym) / sp.diff(U, msym)
d2_at_1 = sp.nsimplify(sp.cancel(d2S).subs(msym, 1))
ok10 = id_top and id_bot and lim_top == sp.Rational(1, 2) and lim_bot == sp.Rational(1, 4) and d2_at_1 != 0 \
    and d2_at_1.is_finite
check('A10 contact orders 3/2 (S = 1), 3 (S = -1), 2 (regular point)', ok10,
      'lim (1-S)^2/u^3 = %s, lim (1+S)/u^3 = %s, d2S/du2 at m=1: %s' % (lim_top, lim_bot, d2_at_1))

# ---------------------------------------------------------------- A11
pts_ball = [cone_point(k, alpha_third=False) for k in range(60)]
ok11 = all(in_cone(*p, alpha_third=False) for p in pts_ball)
ok11 &= all(pair_M(pts_ball[2 * i], pts_ball[2 * i + 1], cross=Fr(0)) >= 0 for i in range(30))
ok11 &= sp.expand(a ** 2 + b ** 2 - 2 * a * b - (a - b) ** 2) == 0
circ = [(Fr(3, 5), Fr(4, 5)), (Fr(-3, 5), Fr(4, 5)), (Fr(5, 13), Fr(-12, 13)), (Fr(1), Fr(0)), (Fr(0), Fr(-1)),
        (Fr(-8, 17), Fr(-15, 17)), (Fr(7, 25), Fr(24, 25))]
rank_c = sp.Matrix([[u0 ** 2, u0 * s0, s0 ** 2, u0, s0, 1] for u0, s0 in circ]).rank()
ok11 &= rank_c == 5
check('A11 control: the Euclidean ball (Lorentz cone, no cross term; conic section)', ok11, 'rank %d' % rank_c)

# ---------------------------------------------------------------- countercontrols
zc = (Fr(1), (Fr(21, 20), Fr(0), Fr(0)), Fr(-3, 10))
wc = (Fr(1), (Fr(-21, 20), Fr(0), Fr(0)), Fr(-3, 10))
memb_ok = in_cone(*zc) and in_cone(*wc)
xs1 = pair_M(zc, wc, cross=Fr(0))
xs2 = pair_M(zc, wc, cross=Fr(1, 3))
true_pair = pair_M(zc, wc)
print('COUNTER XS1 ' + ('fails as stated' if memb_ok and xs1 < 0 else 'DID NOT FAIL') + ' -- pairing %s' % xs1,
      flush=True)
print('COUNTER XS2 ' + ('fails as stated' if memb_ok and xs2 < 0 else 'DID NOT FAIL') + ' -- pairing %s' % xs2,
      flush=True)
print('true inner product on the same pair: %s' % true_pair, flush=True)

failures = [n for n, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(failures)), flush=True)
if not failures and memb_ok and xs1 < 0 and xs2 < 0:
    print('VERDICT E13-SELFDUAL-DRIVABLE-NOT-TRANS', flush=True)
else:
    print('VERDICT NOT RENDERED -- failing: %s' % failures, flush=True)
sys.exit(0)
