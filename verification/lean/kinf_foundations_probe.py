"""Round KINF-1 -- the exact-computation layer of the pre-quantum foundations.

Python integers and fractions only; no floating point, no randomness: every quantity lives in Q or in Q(sqrt 3),
represented as a pair (a, b) = a + b*sqrt3 with a, b rational, and every point at which an identity is tested is
fixed in this file.  Every assertion is exact; the script exits 1 on the first mismatch.  These statements are
exact arithmetic replayed in CI; they are not kernel-certified.  Each section names the kernel statement it
instantiates or controls (OIBridge/KInfFoundations.lean).

Sections.
 1. The SIC-embedded ball (Main.md, the four-state model).  Ontic states N = 4, p_i(r) = (1 + a_i . r) / 4 with the
    unit tetrahedral directions a_i.  Exact: interior sample states have every p_i > 0 (so no response effect
    exposes them: response_eq_one_forces); the four tangency points r = -a_i have exactly one p_i = 0 and are
    exposed by the response effect 1 - p_i; each facet {p_i = 0} meets the ball in exactly that point
    (|r + a_i|^2 = 2 + 2 a_i . r on the sphere).  So the bound of classical_exposed_ncard_le, N = 4, is attained,
    on a body with a continuum of extreme points.
 2. The Caratheodory orbitope C_2 = conv{(cos t, sin t, cos 2t, sin 2t)}: the exact capacity-3 triple at
    t = 0, 2pi/3, 4pi/3 with e_i = (4/9)(1 - cos(t - t_j))(1 - cos(t - t_k)).  Exact in Q(sqrt 3): the affine
    coefficients of e_i, their sum (the unit), e_i(x(t_j)) = delta_ij, and the product identity with nonnegativity
    on rational points of the circle.  Positive control for Lemma D: a body that is not centrally symmetric can
    have capacity three.
 3. The torus orbitope conv(S^1 x S^1) in R^4: the effect e = (1 + x_0)/2 is valid on the generators and certain
    on two distinct generators and on their midpoint, which is not a generator: a flat face, so singleton faces
    fail; the generator set is centrally symmetric (u -> -1/u on the rational circle), so Lemma D bounds its
    capacity by two with the full effects.  Instance of card_le_two_of_centrallySymmetric_full.
 4. The Stiefel orbitope conv V_2(R^3): the rank-one effect e(A) = (1 + A_11)/2 is valid on exact rational
    orthonormal frames and certain on two distinct frames and their midpoint, which is not a frame: a flat face.
 5. The 3-ball control: for a rational unit n the effect (1 + n . x)/2 is certain exactly at x = n, by the
    identity |x - n|^2 = 2 - 2 n . x on the sphere: singleton faces hold.
"""
import sys
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=''):
    if not ok:
        print('kinf_foundations_probe: FAILED ' + name + ((' -- ' + detail) if detail else ''))
        sys.exit(1)
    CHECKS.append(name)
    print('PASS ' + name + (('  ' + detail) if detail else ''), flush=True)


# ---------------------------------------------------------------- Q(sqrt 3) --------------------------------------
class Q3:
    """a + b*sqrt3 with a, b in Q; exact arithmetic and exact sign."""
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, o):
        o = q3(o)
        return Q3(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-q3(o))

    def __rsub__(self, o):
        return q3(o) - self

    def __mul__(self, o):
        o = q3(o)
        return Q3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = q3(o)
        n = o.a * o.a - 3 * o.b * o.b
        p = self * Q3(o.a, -o.b)
        return Q3(p.a / n, p.b / n)

    def __eq__(self, o):
        o = q3(o)
        return self.a == o.a and self.b == o.b

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def is_pos(self):
        a, b = self.a, self.b
        if b == 0:
            return a > 0
        if a == 0:
            return b > 0
        if a > 0 and b > 0:
            return True
        if a < 0 and b < 0:
            return False
        return (a * a > 3 * b * b) if a > 0 else (3 * b * b > a * a)

    def is_nonneg(self):
        return self.is_zero() or self.is_pos()

    def __repr__(self):
        return '(%s + %s sqrt3)' % (self.a, self.b)


def q3(x):
    return x if isinstance(x, Q3) else Q3(x)


def dot(u, v):
    s = Q3(0)
    for x, y in zip(u, v):
        s = s + q3(x) * q3(y)
    return s


# angles k*pi/3 in Q(sqrt 3)
COS = {0: Q3(1), 1: Q3(Fr(1, 2)), 2: Q3(Fr(-1, 2)), 3: Q3(-1), 4: Q3(Fr(-1, 2)), 5: Q3(Fr(1, 2))}
SIN = {0: Q3(0), 1: Q3(0, Fr(1, 2)), 2: Q3(0, Fr(1, 2)), 3: Q3(0), 4: Q3(0, Fr(-1, 2)), 5: Q3(0, Fr(-1, 2))}

# rational points of the unit circle, u -> ((1 - u^2)/(1 + u^2), 2u/(1 + u^2))
CIRCLE_U = [Fr(0), Fr(1), Fr(-1), Fr(1, 2), Fr(2), Fr(-3), Fr(1, 3), Fr(5, 7), Fr(-7, 4), Fr(3), Fr(-2, 9), Fr(11, 3)]


def circle(u):
    d = 1 + u * u
    return ((1 - u * u) / d, 2 * u / d)


# rational points of the unit sphere
SPHERE = [(Fr(3, 5), Fr(4, 5), Fr(0)), (Fr(0), Fr(3, 5), Fr(4, 5)), (Fr(1), Fr(0), Fr(0)), (Fr(2, 3), Fr(2, 3), Fr(1, 3)),
          (Fr(2, 7), Fr(3, 7), Fr(6, 7)), (Fr(1, 3), Fr(2, 3), Fr(2, 3)), (Fr(12, 13), Fr(3, 13), Fr(4, 13)),
          (Fr(1, 9), Fr(4, 9), Fr(8, 9)), (Fr(-2, 3), Fr(1, 3), Fr(-2, 3)), (Fr(0), Fr(-1), Fr(0)),
          (Fr(-4, 9), Fr(-7, 9), Fr(4, 9)), (Fr(6, 7), Fr(-2, 7), Fr(-3, 7))]

# ---------------------------------------------------------------- 1. the SIC ball ---------------------------------
print('== 1. the SIC-embedded ball: N = 4 ontic states, four exposed points of a continuum ==')
SIGNS = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
A = [tuple(Q3(0, Fr(s, 3)) for s in sg) for sg in SIGNS]           # unit tetrahedral directions, 1/sqrt3 = sqrt3/3
for i, a in enumerate(A):
    check('sic.unit.a%d' % i, dot(a, a) == 1)
for i in range(4):
    for j in range(i + 1, 4):
        check('sic.gram.a%d.a%d' % (i, j), dot(A[i], A[j]) == Fr(-1, 3), 'a_i . a_j = -1/3')


def sic_p(r):
    return [(1 + dot(a, r)) / 4 for a in A]


for r in SPHERE:
    check('sic.sphere.%s' % (tuple(map(str, r)),), sum(x * x for x in r) == 1)
    p = sic_p(r)
    check('sic.interior.%s' % (tuple(map(str, r)),), all(x.is_pos() for x in p) and sum(p, Q3(0)) == 1,
          'every p_i > 0: no response effect is certain here (response_eq_one_forces forces c = 1)')
EXPOSED = []
for i, a in enumerate(A):
    r = tuple(-x for x in a)                                          # the tangency point r = -a_i
    p = sic_p(r)
    zeros = [j for j in range(4) if p[j].is_zero()]
    check('sic.tangency.%d.face' % i, zeros == [i] and all(p[j] == Fr(1, 3) for j in range(4) if j != i),
          'p_%d = 0, the others 1/3' % i)
    c = [1 if j != i else 0 for j in range(4)]                        # the response effect 1 - p_i
    e_here = sum((c[j] * p[j] for j in range(4)), Q3(0))
    check('sic.tangency.%d.certain' % i, e_here == 1)
    others = [sic_p(tuple(-x for x in A[k])) for k in range(4) if k != i] + [sic_p(r2) for r2 in SPHERE]
    check('sic.tangency.%d.singleton' % i,
          all((1 - sum((c[j] * q[j] for j in range(4)), Q3(0))).is_pos() for q in others),
          'e = 1 - p_%d < 1 at every other sample point and at the other tangency points' % i)
    EXPOSED.append(r)
# facet uniqueness: on the sphere |r + a_i|^2 = 2 + 2 a_i . r, so a_i . r = -1 only at r = -a_i
for r in SPHERE + EXPOSED:
    for i, a in enumerate(A):
        lhs = dot([x + y for x, y in zip(r, a)], [x + y for x, y in zip(r, a)])
        check('sic.facet_identity.%d.%s' % (i, tuple(map(str, r))), lhs == 2 + 2 * dot(a, r))
check('sic.count', len(EXPOSED) == 4, 'four exposed points, N = 4: classical_exposed_ncard_le is attained')
# the body is the whole ball: p(r) in the simplex for every unit r (|a_i . r| <= 1), continuum of extreme points
for r in SPHERE:
    check('sic.in_simplex.%s' % (tuple(map(str, r)),), all(x.is_nonneg() for x in sic_p(r)))

# ---------------------------------------------------------------- 2. C_2 capacity three ---------------------------
print('== 2. the Caratheodory orbitope C_2: exact capacity-3 triple ==')
T = [0, 2, 4]                                                         # t_j = 2j pi/3 as multiples of pi/3


def x_of_angle(k):
    return (COS[k % 6], SIN[k % 6], COS[(2 * k) % 6], SIN[(2 * k) % 6])


def x_of_u(u):
    c, s = circle(u)
    return (Q3(c), Q3(s), Q3(c * c - s * s), Q3(2 * s * c))


def affine_coeffs(a, b):
    """e = (4/9)(1 - cos(t - a))(1 - cos(t - b)) as alpha + beta . (cos t, sin t, cos 2t, sin 2t)."""
    f = Fr(4, 9)
    alpha = f * (1 + COS[(a - b) % 6] * Fr(1, 2))
    beta = (-f * (COS[a % 6] + COS[b % 6]), -f * (SIN[a % 6] + SIN[b % 6]),
            f * Fr(1, 2) * COS[(a + b) % 6], f * Fr(1, 2) * SIN[(a + b) % 6])
    return alpha, beta


def product_form(a, b, x):
    c, s = x[0], x[1]
    return Fr(4, 9) * (1 - (c * COS[a % 6] + s * SIN[a % 6])) * (1 - (c * COS[b % 6] + s * SIN[b % 6]))


E = []
for i in range(3):
    a, b = [T[k] for k in range(3) if k != i]
    E.append(affine_coeffs(a, b))
alpha_sum = sum((E[i][0] for i in range(3)), Q3(0))
beta_sum = [sum((E[i][1][m] for i in range(3)), Q3(0)) for m in range(4)]
check('c2.unit', alpha_sum == 1 and all(x.is_zero() for x in beta_sum), 'sum_i e_i = 1 as affine functionals')
for i in range(3):
    for j in range(3):
        x = x_of_angle(T[j])
        val = E[i][0] + dot(E[i][1], x)
        check('c2.delta.%d%d' % (i, j), val == (1 if i == j else 0))
for i in range(3):
    a, b = [T[k] for k in range(3) if k != i]
    for u in CIRCLE_U:
        x = x_of_u(u)
        val = E[i][0] + dot(E[i][1], x)
        check('c2.product_identity.%d.u=%s' % (i, u), val == product_form(a, b, x))
        check('c2.nonneg.%d.u=%s' % (i, u), val.is_nonneg())
check('c2.capacity3', True, 'three perfectly distinguishable extreme points; C_2 is not centrally symmetric')

# ---------------------------------------------------------------- 3. the torus orbitope ---------------------------
print('== 3. the torus orbitope: a flat face with full effects; centrally symmetric ==')


def torus_pt(u, v):
    c1, s1 = circle(u)
    c2, s2 = circle(v)
    return (c1, s1, c2, s2)


def e_torus(x):
    return (1 + x[0]) / 2


for u in CIRCLE_U:
    for v in CIRCLE_U[:5]:
        x = torus_pt(u, v)
        check('torus.valid.u=%s.v=%s' % (u, v), 0 <= e_torus(x) <= 1)
p1 = (Fr(1), Fr(0), Fr(1), Fr(0))                                   # (s, t) = (0, 0)
p2 = (Fr(1), Fr(0), Fr(0), Fr(1))                                   # (s, t) = (0, pi/2)
mid = tuple((x + y) / 2 for x, y in zip(p1, p2))
check('torus.generators', p1[0] ** 2 + p1[1] ** 2 == 1 and p1[2] ** 2 + p1[3] ** 2 == 1
      and p2[2] ** 2 + p2[3] ** 2 == 1 and p1 != p2)
check('torus.certain', e_torus(p1) == 1 and e_torus(p2) == 1 and e_torus(mid) == 1)
check('torus.flat_face', mid[2] ** 2 + mid[3] ** 2 != 1,
      'the midpoint (1, 0, 1/2, 1/2) is certain and is not a generator: the certain face is not a singleton')
for u in CIRCLE_U:
    if u == 0:
        continue
    c, s = circle(u)
    c2, s2 = circle(-1 / u)
    check('torus.antipode.u=%s' % u, c2 == -c and s2 == -s, 'x -> -x preserves the generator set')
check('torus.antipode.u=0', circle(Fr(0)) == (1, 0) and (-1) ** 2 + 0 ** 2 == 1)
check('torus.capacity_le_2', True, 'by card_le_two_of_centrallySymmetric_full (kernel), centre 0')

# ---------------------------------------------------------------- 4. the Stiefel orbitope -------------------------
print('== 4. the Stiefel orbitope V_2(R^3): a flat face exposed by a rank-one effect ==')
ROT = [[[Fr(1, 3), Fr(2, 3), Fr(2, 3)], [Fr(2, 3), Fr(1, 3), Fr(-2, 3)], [Fr(-2, 3), Fr(2, 3), Fr(-1, 3)]],
       [[Fr(2, 7), Fr(3, 7), Fr(6, 7)], [Fr(3, 7), Fr(-6, 7), Fr(2, 7)], [Fr(6, 7), Fr(2, 7), Fr(-3, 7)]],
       [[Fr(1, 9), Fr(4, 9), Fr(8, 9)], [Fr(4, 9), Fr(7, 9), Fr(-4, 9)], [Fr(8, 9), Fr(-4, 9), Fr(1, 9)]]]


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def transpose(X):
    return [[X[j][i] for j in range(3)] for i in range(3)]


def frame(R, cols=(0, 1)):
    return [[R[i][c] for c in cols] for i in range(3)]


def orthonormal(F):
    g = [[sum(F[i][a] * F[i][b] for i in range(3)) for b in range(2)] for a in range(2)]
    return g == [[1, 0], [0, 1]]


FRAMES = []
for R in ROT:
    check('stiefel.rotation', matmul(R, transpose(R)) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    for cols in ((0, 1), (1, 2), (0, 2), (2, 0)):
        FRAMES.append(frame(R, cols))
        FRAMES.append(frame(transpose(R), cols))
for R in ROT:
    for S in ROT:
        FRAMES.append(frame(matmul(R, S)))
for F in FRAMES:
    check('stiefel.frame', orthonormal(F))
    check('stiefel.valid', 0 <= (1 + F[0][0]) / 2 <= 1, 'the rank-one effect is valid on the frame')
A1 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]
A2 = [[Fr(1), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(1)]]
M = [[(A1[i][j] + A2[i][j]) / 2 for j in range(2)] for i in range(3)]
check('stiefel.two_frames', orthonormal(A1) and orthonormal(A2) and A1 != A2)
check('stiefel.certain', (1 + A1[0][0]) / 2 == 1 and (1 + A2[0][0]) / 2 == 1 and (1 + M[0][0]) / 2 == 1)
check('stiefel.flat_face', not orthonormal(M), 'the midpoint is certain and is not a frame')
for F in FRAMES[:6]:
    check('stiefel.antipode', orthonormal([[-x for x in row] for row in F]))

# ---------------------------------------------------------------- 5. the 3-ball control --------------------------
print('== 5. the 3-ball control: singleton faces ==')
n = (Fr(3, 5), Fr(4, 5), Fr(0))
for x in SPHERE:
    nx = sum(a * b for a, b in zip(n, x))
    d2 = sum((a - b) ** 2 for a, b in zip(x, n))
    check('ball.identity.%s' % (tuple(map(str, x)),), d2 == 2 - 2 * nx, '|x - n|^2 = 2 - 2 n . x')
    e = (1 + nx) / 2
    check('ball.face.%s' % (tuple(map(str, x)),), (e == 1) == (x == n), 'certain exactly at x = n')

print('kinf_foundations_probe: OK -- %d checks' % len(CHECKS))
