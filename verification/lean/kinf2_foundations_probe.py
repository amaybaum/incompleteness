#!/usr/bin/env python3
"""Round KINF-2 -- the exact-computation layer of the corrected pre-quantum foundations.

Exact arithmetic only: Python Fractions, pairs a + b*sqrt3 (class Q3), pairs a + b*sqrt5 (class Q5), and sympy
polynomial / rational-function identities.  No floating point, no randomness, no time-dependence, no file or network
I/O; every point at which anything is tested is fixed in this file.  The script exits 1 on the first failed check.
These statements are exact arithmetic replayed in CI; they are not kernel-certified.

Each check carries its kind in brackets:
  [witness]   an exact witness for an existential claim (decisive for that claim);
  [identity]  an exact symbolic identity (decisive for the universal claim it encodes);
  [sample]    an exact check at fixed points (evidence only for the universal claim it instantiates);
  [enumerate] an exhaustive exact enumeration of a finite set (decisive).
Lines printed as NOTE [written] record a written argument beside the exact checks; they are not checks and are not
counted.

Vocabulary under test (relative to the body Om, no ambient topology):
  effect on Om     : 0 <= e <= 1 on Om;      proper on Om : exists y in Om with e y < 1;
  boundary state   : x in Om and exists y in Om with x + eps (x - y) notin Om for every eps > 0;
  SEC'(Om, avail)  : every boundary state is certain for some PROPER available effect;
  SF'(Om, avail)   : every PROPER available effect has a subsingleton certain face;
  RSC(Om)          : the open segment between two distinct states contains no boundary state;
  Drive'(Om)       : elementary drivability with a one-parameter GROUP flow of Om-automorphisms, J an
                     Om-automorphism, and the off-axis clause compared ON Om.

Sections.
  1. identities: the line-extension and affine-combination identities behind L1-L3 and Lemma C are exact
     polynomial identities.
  2. unit and non-proper effects: the unit, and an effect identically 1 on a lower-dimensional body but not
     constant on V, are not proper relative to Om; a constant below 1 is proper with an empty certain face.
  3. square gbit: facet effects are proper and certain on an edge (SF' and RSC fail), SEC'(facets) holds on a
     boundary grid, capacity 2; the KINF-1 frozen drivability holds for the square (a defect), while its
     affine automorphism group is the finite D4.
  4. torus orbitope: SF' fails on a flat face while the body is centrally symmetric and Drive' holds.
  5. Stiefel orbitope: SF' fails on a flat face exposed by a rank-one effect; Drive' witnesses N and J.
  6. 3-ball: SEC'(full), SF'(full), RSC and Drive' hold together (non-vacuity); for the disk the frozen J clause
     holds through a contraction, and the corrected clause fails by the reflection conjugation identity.
  7. SIC ball: response effects certain at a generic pure state are the unit, so SEC'(response) fails there,
     while it holds at the four tangency points; in simplex coordinates the ambient frontier is degenerate.
  8. Caratheodory orbitope C_2: an exact capacity-three triple in Q(sqrt3) on a body that is not centrally
     symmetric -- the countercontrol showing that Lemma D's central-symmetry hypothesis is load-bearing.
  9. regular pentagon in Q(sqrt5): capacity 2 with full effects, strongly self-dual, D5 transitive on ordered
     frames, not centrally symmetric, and an edge effect proper and certain on a whole edge (SF' fails).
 10. degenerate bodies: empty, singleton and open bodies satisfy the predicates vacuously; the segment and the
     triangle are separated as stated.
 11. route neutrality: a symmetric cone (the real qutrit) violates SF, so self-duality and homogeneity reach RSC
     only with a rank-two premise; the Lean composition order of the off-axis clause gives the same verdicts.
 12. countercontrols: each mutated predicate, identity or enumeration gives the opposite verdict.

The claim "corrected drivability excludes the square gbit and the disk" is checked here only through the
automorphism enumeration (the square's eight affine automorphisms, and for the disk the conjugation identity of one
reflection); the step from there to the exclusion remains a written argument.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
import sympy as sp

CHECKS = []
KINDS = []


def check(name, ok, detail=''):
    if not ok:
        print('kinf2_foundations_probe: FAILED ' + name + ((' -- ' + detail) if detail else ''), flush=True)
        sys.exit(1)
    CHECKS.append(name)
    print('PASS %s  %s' % (name, detail), flush=True)


SEC = [0]                                           # the current section number, used as the name prefix


def section(n, title):
    SEC[0] = n
    print('== %d. %s ==' % (n, title), flush=True)


def chk(name, ok, kind, detail=''):
    KINDS.append(kind)
    check('s%d.%s' % (SEC[0], name), ok, '[%s]%s' % (kind, (' ' + detail) if detail else ''))


def note(name, detail):                             # a written argument, recorded beside the exact checks; not a check
    print('NOTE [written] s%d.%s  -- %s' % (SEC[0], name, detail), flush=True)


def pt(x):                                          # a space-free rendering of an exact point, for check names
    return '(' + ','.join(str(c) for c in x) + ')'


# ------------------------------------------------------------------ Q(sqrt3) ------------------------------------
class Q3:
    """a + b*sqrt3 with a, b in Q; exact arithmetic and exact sign."""
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = q3(o); return Q3(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-q3(o))

    def __rsub__(self, o):
        return q3(o) - self

    def __mul__(self, o):
        o = q3(o); return Q3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def __truediv__(self, o):
        o = q3(o); n = o.a * o.a - 3 * o.b * o.b; p = self * Q3(o.a, -o.b); return Q3(p.a / n, p.b / n)

    def __eq__(self, o):
        o = q3(o); return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def is_pos(self):
        a, b = self.a, self.b
        if b == 0: return a > 0
        if a == 0: return b > 0
        if a > 0 and b > 0: return True
        if a < 0 and b < 0: return False
        return (a * a > 3 * b * b) if a > 0 else (3 * b * b > a * a)

    def is_nonneg(self):
        return self.is_zero() or self.is_pos()

    def to_sympy(self):
        return sp.Rational(self.a.numerator, self.a.denominator) + \
            sp.Rational(self.b.numerator, self.b.denominator) * sp.sqrt(3)

    def __repr__(self):
        return '(%s+%ssqrt3)' % (self.a, self.b)


def q3(x):
    return x if isinstance(x, Q3) else Q3(x)


def dot(u, v):
    return sum((q3(x) * q3(y) for x, y in zip(u, v)), Q3(0))


# ------------------------------------------------------------------ Q(sqrt5) ------------------------------------
class Q5:
    """a + b*sqrt5 with a, b in Q; exact arithmetic and exact sign."""
    __slots__ = ('a', 'b')

    def __init__(s, a, b=0): s.a, s.b = Fr(a), Fr(b)

    def __add__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __neg__(s): return Q5(-s.a, -s.b)

    def __sub__(s, o): return s + (-(o if isinstance(o, Q5) else Q5(o)))

    def __rsub__(s, o): return Q5(o) - s

    def __mul__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__

    def inv(s):
        d = s.a * s.a - 5 * s.b * s.b; return Q5(s.a / d, -s.b / d)

    def __truediv__(s, o): o = o if isinstance(o, Q5) else Q5(o); return s * o.inv()

    def sign(s):
        a, b = s.a, s.b
        if b == 0: return (a > 0) - (a < 0)
        if a == 0: return (b > 0) - (b < 0)
        if (a > 0) == (b > 0): return 1 if a > 0 else -1
        return ((a * a > 5 * b * b) - (a * a < 5 * b * b)) * (1 if a > 0 else -1)

    def __eq__(s, o): o = o if isinstance(o, Q5) else Q5(o); return s.a == o.a and s.b == o.b

    def __hash__(s): return hash((s.a, s.b))

    def __repr__(s): return '(%s%s%ssqrt5)' % (s.a, '+' if s.b >= 0 else '-', abs(s.b))


def det3(r0, r1, r2):
    return (r0[0] * (r1[1] * r2[2] - r1[2] * r2[1]) - r0[1] * (r1[0] * r2[2] - r1[2] * r2[0])
            + r0[2] * (r1[0] * r2[1] - r1[1] * r2[0]))


def solve3(A, bvec):                                # Cramer's rule: the c with A c = bvec (A given by rows)
    d = det3(*A)
    cols = []
    for k in range(3):
        Ak = [[bvec[i] if j == k else A[i][j] for j in range(3)] for i in range(3)]
        cols.append(det3(*Ak) / d)
    return cols


def poly_affine_auts(V):
    """Every affine automorphism of the polygon conv(V) (vertices V, no three collinear) permutes V and is fixed by
    the images of V[0], V[1], V[2]; so the automorphisms are exactly the affine maps sending (V0, V1, V2) to an
    ordered triple of vertices that permute V.  Returns (vertex permutation, linear part, translation) for each."""
    n = len(V)
    A = [[1, *p] for p in V[:3]]
    out = []
    for tri in permutations(range(n), 3):
        dst = [V[t] for t in tri]
        cx = solve3(A, [d[0] for d in dst]); cy = solve3(A, [d[1] for d in dst])
        img = [(cx[0] + cx[1] * p[0] + cx[2] * p[1], cy[0] + cy[1] * p[0] + cy[2] * p[1]) for p in V]
        if all(any(q == p for p in V) for q in img):
            perm = tuple(next(m for m in range(n) if V[m] == q) for q in img)
            if len(set(perm)) == n:
                out.append((perm, ((cx[1], cx[2]), (cy[1], cy[2])), (cx[0], cy[0])))
    return out


def distinguishable_vertex_triples(V):
    """Unordered vertex triples of conv(V) that are perfectly distinguishable with full effects.  For affinely
    independent v_i, v_j, v_k the effects e_i + e_j + e_k = 1 with e_a(v_b) = delta_ab are forced to be the barycentric
    coordinates of the triangle, so the triple is distinguishable iff every other vertex has nonnegative barycentric
    coordinates.  A collinear triple is never distinguishable (its middle point is a mixture of the other two)."""
    out = []
    for i, j, k in combinations(range(len(V)), 3):
        Mrows = [[1, 1, 1], [V[i][0], V[j][0], V[k][0]], [V[i][1], V[j][1], V[k][1]]]
        if det3(*Mrows).sign() == 0:
            continue
        ok = True
        for m in range(len(V)):
            if m in (i, j, k):
                continue
            lam = solve3(Mrows, [1, V[m][0], V[m][1]])
            if any(c.sign() < 0 for c in lam):
                ok = False
        if ok:
            out.append((i, j, k))
    return out


# ------------------------------------------------------------------ linear algebra and fixed points ------------
def mat_vec(M, v):
    return tuple(sum(M[i][k] * v[k] for k in range(len(v))) for i in range(len(M)))


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def ident(n):
    return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def circle(u):                                      # rational point of the unit circle
    d = 1 + u * u
    return ((1 - u * u) / d, 2 * u / d)


CIRCLE_U = [Fr(0), Fr(1), Fr(-1), Fr(1, 2), Fr(2), Fr(-3), Fr(1, 3), Fr(5, 7), Fr(-7, 4), Fr(3)]
SPHERE = [(Fr(3, 5), Fr(4, 5), Fr(0)), (Fr(0), Fr(3, 5), Fr(4, 5)), (Fr(1), Fr(0), Fr(0)), (Fr(2, 3), Fr(2, 3), Fr(1, 3)),
          (Fr(2, 7), Fr(3, 7), Fr(6, 7)), (Fr(1, 3), Fr(2, 3), Fr(2, 3)), (Fr(12, 13), Fr(3, 13), Fr(4, 13)),
          (Fr(1, 9), Fr(4, 9), Fr(8, 9)), (Fr(-2, 3), Fr(1, 3), Fr(-2, 3)), (Fr(0), Fr(-1), Fr(0)),
          (Fr(-4, 9), Fr(-7, 9), Fr(4, 9)), (Fr(6, 7), Fr(-2, 7), Fr(-3, 7))]


# polytope in H-representation: list of (a, b) meaning a . x <= b; full-dimensional, so no implicit equalities.
def in_poly(H, x):
    return all(sum(ai * xi for ai, xi in zip(a, x)) <= b for a, b in H)


def boundary_poly(H, V, x):
    """Algebraic boundary state of a full-dimensional polytope conv(V) = {H}: x + eps(x - y) leaves for all eps > 0
    iff some inequality is tight at x and strict at some vertex y (then a.(x - y) > 0).  Exact and decisive for
    polytopes (the set of eps keeping x + eps(x - y) inside is an interval [0, eps_max])."""
    if not in_poly(H, x):
        return False
    for a, b in H:
        if sum(ai * xi for ai, xi in zip(a, x)) == b and any(sum(ai * yi for ai, yi in zip(a, y)) < b for y in V):
            return True
    return False


# ==================================================================================================================
section(1, 'identities: the exact algebraic identities behind the corrected lemmas')
d = 3
zs = sp.symbols('z0:3'); ws = sp.symbols('w0:3'); xs = sp.symbols('x0:3'); ys = sp.symbols('y0:3')
al = sp.Symbol('alpha'); be = sp.symbols('b0:3'); eps, a_, t = sp.symbols('epsilon a t')
e = lambda v: al + sum(be[i] * v[i] for i in range(d))                                   # generic affine functional
ext = [zs[i] + eps * (zs[i] - ws[i]) for i in range(d)]
chk('line_extension', sp.expand(e(ext) - (e(zs) + eps * (e(zs) - e(ws)))) == 0, 'identity',
    'e(z + eps(z - w)) = e z + eps (e z - e w): a proper effect certain at z exceeds 1 on the extension, so '
    '(i) certain + proper => boundary state; (ii) certain at a non-boundary state => e = 1 on all of Om')
combo = [a_ * xs[i] + (1 - a_) * ys[i] for i in range(d)]
chk('affine_combo', sp.expand(e(combo) - (a_ * e(xs) + (1 - a_) * e(ys))) == 0, 'identity',
    'Lemma C step: e(a x + b y) = a e x + b e y, so e = 1 at an interior point of [x, y] forces e x = e y = 1')
ext2 = [zs[i] + eps * (zs[i] - ws[i]) for i in range(d)]
chk('extension_is_affine_combo', all(sp.expand(ext2[i] - ((1 + eps) * zs[i] + (-eps) * ws[i])) == 0 for i in range(d)),
    'identity', 'z + eps(z - w) = (1 + eps) z + (-eps) w, so the frozen affine_combo (any a + b = 1) suffices in Lean')

# ==================================================================================================================
section(2, 'unit and non-proper effects: the unit and other non-proper or never-certain effects')
UNIT = lambda x: Fr(1)
SQ_V = [(Fr(s1), Fr(s2)) for s1 in (1, -1) for s2 in (1, -1)]
chk('unit.not_proper.square', all(UNIT(v) == 1 for v in SQ_V), 'identity',
    'the unit is 1 on every vertex, hence on the hull: no y with unit y < 1, so it is not proper')
# an effect that is identically 1 on Om but NOT the constant functional on V (Om lower-dimensional):
# the gbit as a finite stage in R^E, E = (unit, x+, x-, y+, y-), lies on v_unit = 1 and v_x+ + v_x- = 1, ...


def gbit_stage_vec(p):
    x, y = p
    return (Fr(1), (1 + x) / 2, (1 - x) / 2, (1 + y) / 2, (1 - y) / 2)


GV = [gbit_stage_vec(p) for p in SQ_V]
coord_unit = lambda v: v[0]
chk('stage.unit_coordinate.const_on_Om', all(coord_unit(v) == 1 for v in GV), 'identity',
    'v -> v_unit is 1 on the stage body (hull of the four vectors)')
chk('stage.unit_coordinate.nonconst_on_V', coord_unit((Fr(0),) * 5) == 0, 'witness',
    'but it is NOT the constant 1 on V = R^5: a syntactic properness test (e != const 1) would call it proper, '
    'and it is certain on every state -> SEC trivial and SF impossible again.  Properness must be relative to Om')
chk('stage.unit_coordinate.not_proper_relative', not any(coord_unit(v) < 1 for v in GV), 'identity',
    'relative to Om it is not proper, as required')
# constant c < 1 on Om: proper, empty certain face; cannot witness SEC', cannot violate SF'
c_half = lambda x: Fr(1, 2)
chk('const_half.proper_empty_face', all(c_half(v) < 1 for v in SQ_V), 'identity',
    'proper with empty certain face: SF holds for it vacuously and it is certain at no boundary state')

# ==================================================================================================================
section(3, 'square gbit [-1,1]^2: flat faces, capacity 2, frozen vs corrected drivability')
SQ_H = [((Fr(1), Fr(0)), Fr(1)), ((Fr(-1), Fr(0)), Fr(1)), ((Fr(0), Fr(1)), Fr(1)), ((Fr(0), Fr(-1)), Fr(1))]
facet = [lambda p, a=a: (1 + a[0] * p[0] + a[1] * p[1]) / 2 for a, _ in SQ_H]           # the four facet effects
for k, f in enumerate(facet):
    chk('sq.facet%d.effect' % k, all(0 <= f(v) <= 1 for v in SQ_V), 'identity',
        'affine, so [0,1] on the vertices gives [0,1] on the hull')
    chk('sq.facet%d.proper' % k, any(f(v) < 1 for v in SQ_V), 'witness')
f0 = facet[0]
A1, A2 = (Fr(1), Fr(1)), (Fr(1), Fr(-1))
chk('sq.SF_fails', f0(A1) == 1 and f0(A2) == 1 and A1 != A2, 'witness',
    "SF'(full) and SF'(facet effects) fail: the proper facet effect (1+x)/2 is certain on two distinct states")
chk('sq.SF_fails_with_unit_too', f0(A1) == 1 and f0(A2) == 1, 'witness',
    'adding the unit changes nothing: it is not proper, so the verdict is the flat face, not the unit')
mid = (Fr(1), Fr(0))
chk('sq.RSC_fails', boundary_poly(SQ_H, SQ_V, mid), 'witness',
    'the midpoint (1,0) of two distinct states is a boundary state: not relatively strictly convex')
grid = [Fr(k, 4) for k in range(-4, 5)]
bpts = [p for p in product(grid, grid) if boundary_poly(SQ_H, SQ_V, p)]
ipts = [p for p in product(grid, grid) if in_poly(SQ_H, p) and not boundary_poly(SQ_H, SQ_V, p)]
chk('sq.boundary_states_counted', len(bpts) == 32 and len(ipts) == 49, 'enumerate',
    'on the 9x9 grid: 32 boundary states (the perimeter), 49 relative-interior states')
chk('sq.SEC_facets', all(any(f(p) == 1 and any(f(v) < 1 for v in SQ_V) for f in facet) for p in bpts), 'sample',
    "SEC'(facet effects): every boundary grid state is certain for a proper facet effect (decisive for the square "
    'by the H-representation: every boundary state lies on a facet)')
chk('sq.no_proper_certain_inside', all(all(f(p) < 1 for f in facet) for p in ipts), 'sample',
    'no facet effect is certain at a relative-interior state (line-extension lemma, section 1)')
OLD = 'old (KINF-1 frozen)'
chk('sq.old_SEC_trivial', all(UNIT(p) == 1 for p in bpts + ipts), 'identity',
    OLD + ' SEC held at every point via the unit; the corrected SEC needs a proper effect')
# capacity two
chk('sq.central_symmetry', sorted(SQ_V) == sorted((-x, -y) for x, y in SQ_V), 'enumerate',
    'vertex set closed under negation, so the square is centrally symmetric about 0: capacity <= 2 (Lemma D)')
g = lambda p: (1 + (p[0] + p[1]) / 2) / 2
chk('sq.capacity_two_witness', g((Fr(1), Fr(1))) == 1 and 1 - g((Fr(-1), Fr(-1))) == 1
    and all(0 <= g(v) <= 1 for v in SQ_V), 'witness', 'perfectly distinguishable pair (1,1), (-1,-1) by g, 1 - g')

# ---- drivability: the KINF-1 frozen ElementaryDrivability is SATISFIED by the square gbit
print('-- 3b. ElementaryDrivability as frozen in KINF-1 holds for the square gbit (defect) --', flush=True)
I2 = ident(2); R90 = [[Fr(0), Fr(-1)], [Fr(1), Fr(0)]]; NEG = [[Fr(-1), Fr(0)], [Fr(0), Fr(-1)]]
tt = sp.Symbol('t')
seg1 = sp.Matrix([[1 - tt, -tt], [tt, 1 - tt]])                      # I -> R90, t in [0,1]
seg2 = sp.Matrix([[-tt, -(1 - tt)], [1 - tt, -tt]])                  # R90 -> -I, t in [0,1]
chk('sq.frozen.path_endpoints', seg1.subs(tt, 0) == sp.eye(2) and seg1.subs(tt, 1) == sp.Matrix(R90)
    and seg2.subs(tt, 0) == sp.Matrix(R90) and seg2.subs(tt, 1) == -sp.eye(2), 'identity',
    'flow: t<=0 -> I; [0,1] -> (1-t)I + tR90; [1,2] -> (2-t)R90 + (t-1)(-I); t>=2 -> -I: continuous, flow 0 = id')
for nm, S in (('seg1', seg1), ('seg2', seg2)):
    chk('sq.frozen.%s.det_pos' % nm, sp.expand(S.det() - (2 * (tt - sp.Rational(1, 2)) ** 2 + sp.Rational(1, 2))) == 0,
        'identity', 'det = 2(t - 1/2)^2 + 1/2 >= 1/2 > 0: every member is an affine equivalence of V')
    rows_ok = all(sp.simplify(abs(S[i, 0]) + abs(S[i, 1]) - 1).subs(tt, sp.Rational(k, 10)) == 0
                  for i in range(2) for k in range(11))
    chk('sq.frozen.%s.maps_into' % nm, rows_ok, 'sample',
        'max-row-sum norm 1 at t = 0, 1/10, ..., 1; decisive argument: each member is a convex combination of two '
        'square symmetries, so the image of a vertex is a convex combination of two vertices (into, not onto)')
chk('sq.frozen.into_not_onto', sp.Matrix([[1, -1], [1, 1]]) / 2 == seg1.subs(tt, sp.Rational(1, 2))
    and sp.Matrix([[1, -1], [1, 1]]).det() / 4 == sp.Rational(1, 2), 'witness',
    'at t = 1/2 the member has det 1/2 < 1: it maps the square INTO itself, strictly smaller (not an automorphism)')
chk('sq.frozen.N', mat_mul(NEG, NEG) == I2 and mat_vec(NEG, (Fr(1), Fr(1))) != (Fr(1), Fr(1)), 'witness',
    'N = flow 2 = -I is an involution of V that moves the state (1,1)')
J = lambda p: (p[0] / 2 + Fr(1, 2), p[1] / 2)
Jinv = lambda p: (2 * p[0] - 1, 2 * p[1])
chk('sq.frozen.J_into', all(in_poly(SQ_H, J(v)) for v in SQ_V), 'identity', 'J = x/2 + (1/2, 0) maps the square into itself')
conj0 = Jinv(mat_vec(R90, J((Fr(0), Fr(0)))))
chk('sq.frozen.J_off_axis', conj0 == (Fr(-1), Fr(1)), 'witness',
    'J^-1 flow(1) J sends the state 0 to (-1,1); every flow member is linear and fixes 0: J_off_axis holds')
# ---- corrected drivability: Aut(square) is finite
auts = set()
for img in permutations(SQ_V, 3):
    # affine map sending (1,1)->img0, (1,-1)->img1, (-1,1)->img2 ; then check (-1,-1)
    p0, p1, p2 = img
    L = [[(p0[i] - p2[i]) / 2, (p0[i] - p1[i]) / 2] for i in range(2)]          # columns: images of e1, e2
    c = tuple(p0[i] - L[i][0] - L[i][1] for i in range(2))
    f = lambda v: tuple(L[i][0] * v[0] + L[i][1] * v[1] + c[i] for i in range(2))
    if sorted(f(v) for v in SQ_V) == sorted(SQ_V):
        auts.add((tuple(map(tuple, L)), c))
chk('sq.aut_count', len(auts) == 8, 'enumerate',
    'the affine automorphisms of the square are exactly 8 (dihedral D4): an Om-automorphism permutes the vertices')
note('sq.corrected.not_drivable',
     "Drive': a group flow of Om-automorphisms is pointwise continuous with values in a finite set on each vertex, "
     'hence constant, hence the identity; N = id moves nothing.  The square is excluded')

# ==================================================================================================================
section(4, 'torus orbitope conv(S^1 x S^1) in R^4')
TG = [circle(u) + circle(v) for u in CIRCLE_U for v in CIRCLE_U]
eT = lambda x: (1 + x[0]) / 2
chk('torus.effect', all(0 <= eT(x) <= 1 for x in TG), 'identity', '|x0| <= 1 on every generator, hence on the hull')
yT = (Fr(-1), Fr(0), Fr(1), Fr(0))
chk('torus.proper', eT(yT) == 0, 'witness')
p1, p2 = (Fr(1), Fr(0), Fr(1), Fr(0)), (Fr(1), Fr(0), Fr(0), Fr(1))
mT = tuple((a + b) / 2 for a, b in zip(p1, p2))
chk('torus.SF_fails', eT(p1) == 1 and eT(p2) == 1 and p1 != p2, 'witness', "SF'(full) fails: flat face")
chk('torus.RSC_fails', eT(mT) == 1 and eT(yT) < 1, 'witness',
    'the midpoint is certain for a proper effect, so it is a boundary state (section 1 (i)): not RSC')
chk('torus.central_symmetry', all(circle(-1 / u) == tuple(-c for c in circle(u)) for u in CIRCLE_U if u != 0), 'identity',
    'u -> -1/u negates rational circle points: the generator set is centrally symmetric: capacity <= 2')
# corrected drivability: flow = R_t (+) I, N = R_pi (+) I, J = swap


def rot_first(R):
    return lambda x: mat_vec(R, x[:2]) + x[2:]


swap = lambda x: x[2:] + x[:2]
F90, Npi = rot_first(R90), rot_first(NEG)
gen_set = set(TG)
chk('torus.flow_automorphism', all(sum(c * c for c in F90(x)[:2]) == 1 and sum(c * c for c in F90(x)[2:]) == 1
                                   for x in TG), 'sample',
    'R_t (+) I maps generators to generators (rotation of the first circle); group law and onto-ness are the rotation group')
chk('torus.N', Npi(Npi(p1)) == p1 and Npi(p1) != p1, 'witness', 'N = R_pi (+) I is an involution moving p1')
chk('torus.J_automorphism', all(swap(swap(x)) == x for x in TG) and all(swap(x) in gen_set for x in TG), 'enumerate',
    'J = swap of the two circles permutes the sampled generators and is an involution: an Om-automorphism')
conjT = swap(F90(swap(p1)))
chk('torus.J_off_axis_on_Om', conjT[2:] != p1[2:], 'witness',
    'J^-1 flow(pi/2) J moves the last two coordinates of p1; every flow member fixes them: off-axis ON Om')
note('torus.verdict',
     "drivable (Drive'), capacity 2, full effects available, and SF' fails: SF is independent of all three")

# ==================================================================================================================
section(5, 'Stiefel orbitope conv V_2(R^3)')
ROT = [[[Fr(1, 3), Fr(2, 3), Fr(2, 3)], [Fr(2, 3), Fr(1, 3), Fr(-2, 3)], [Fr(-2, 3), Fr(2, 3), Fr(-1, 3)]],
       [[Fr(2, 7), Fr(3, 7), Fr(6, 7)], [Fr(3, 7), Fr(-6, 7), Fr(2, 7)], [Fr(6, 7), Fr(2, 7), Fr(-3, 7)]]]
FR = [[[R[i][c] for c in cols] for i in range(3)] for R in ROT for cols in ((0, 1), (1, 2), (0, 2))]
orth = lambda F: [[sum(F[i][a] * F[i][b] for i in range(3)) for b in range(2)] for a in range(2)] == [[1, 0], [0, 1]]
eS = lambda F: (1 + F[0][0]) / 2
S1 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]
S2 = [[Fr(1), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(1)]]
negS1 = [[-v for v in row] for row in S1]
chk('stiefel.frames', all(orth(F) for F in FR + [S1, S2, negS1]), 'enumerate')
chk('stiefel.effect', all(0 <= eS(F) <= 1 for F in FR + [S1, S2, negS1]), 'sample',
    '|A_11| <= |first column| = 1 on every frame (decisive argument), hence on the hull')
chk('stiefel.proper', eS(negS1) == 0, 'witness')
chk('stiefel.SF_fails', eS(S1) == 1 and eS(S2) == 1 and S1 != S2, 'witness', "SF'(full) fails: flat face")
Rz90 = [[Fr(0), Fr(-1), Fr(0)], [Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
Rzpi = [[Fr(-1), Fr(0), Fr(0)], [Fr(0), Fr(-1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
Rx90 = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(-1)], [Fr(0), Fr(1), Fr(0)]]
Rx90inv = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1)], [Fr(0), Fr(-1), Fr(0)]]
chk('stiefel.N', mat_mul(Rzpi, mat_mul(Rzpi, S1)) == S1 and mat_mul(Rzpi, S1) != S1, 'witness',
    'flow = left multiplication by R_z(t) (Om-automorphisms, a group); N = L_{R_z(pi)} is an involution moving S1')
conjS = mat_mul(Rx90inv, mat_mul(Rz90, mat_mul(Rx90, S1)))
chk('stiefel.J_off_axis_on_Om', conjS[2] != S1[2], 'witness',
    'J = L_{R_x(pi/2)}: the conjugate changes the third row of S1, which every L_{R_z(s)} fixes')

# ==================================================================================================================
section(6, '3-ball (Bloch ball): SF holds with full effects; the disk J clause')
us = sp.symbols('u0:3')
lam = sp.Symbol('lam', positive=True)
nx = sum(us[i] * xs[i] for i in range(3))
id_ball = sp.expand((1 - nx) - (sum((xs[i] - us[i]) ** 2 for i in range(3)) / 2 + (1 - sum(v * v for v in xs)) / 2)
                    - (1 - sum(v * v for v in us)) / 2)
chk('ball.face_identity', id_ball == 0, 'identity',
    '1 - u.x = |x - u|^2/2 + (1 - |x|^2)/2 + (|u|^2 - 1)/2; with |u| = 1 and |x| <= 1, u.x = 1 iff x = u')
note('ball.SF_full',
     "every proper effect with a nonempty certain face is e = 1 - lam(1 - u.x), lam > 0, |u| = 1 (alpha + |beta| = 1, "
     "u = beta/|beta|), so by ball.face_identity its certain face is {u}: SF'(full) holds.  Kernel route: "
     'strictConvex_closedBall -> RSC -> SF for every family (L5, L7)')
n0 = (Fr(3, 5), Fr(4, 5), Fr(0))
for x in SPHERE:
    nxv = sum(a * b for a, b in zip(n0, x))
    chk('ball.face.%s' % pt(x), ((1 + nxv) / 2 == 1) == (x == n0), 'sample')
chk('ball.boundary_is_sphere', all(sum(((1 + 2 * Fr(1, 10 ** k)) * c) ** 2 for c in x) > 1 for x in SPHERE for k in (1, 3, 6)),
    'sample', 'for |x| = 1 the witness y = -x gives x + eps(2x) of norm 1 + 2eps > 1: sphere points are boundary states')
note('ball.SEC_full',
     "at |x| = 1 the effect (1 + x.y)/2 is proper (0 at y = -x) and certain at x: SEC'(full) holds")
chk('ball.old_SF_false', UNIT(n0) == 1 and UNIT(SPHERE[1]) == 1, 'witness',
    OLD + ' SF failed on the ball with full effects via the unit (two distinct certain states); corrected SF holds')
# corrected drivability of the ball
chk('ball.N', mat_vec(Rzpi, mat_vec(Rzpi, (Fr(1), Fr(0), Fr(0)))) == (Fr(1), Fr(0), Fr(0))
    and mat_vec(Rzpi, (Fr(1), Fr(0), Fr(0))) != (Fr(1), Fr(0), Fr(0)), 'witness',
    'flow = R_z(t) (a group of ball automorphisms), N = R_z(pi) involutive and moving (1,0,0)')
e3 = (Fr(0), Fr(0), Fr(1))
chk('ball.J_off_axis_on_Om', mat_vec(Rx90inv, mat_vec(Rz90, mat_vec(Rx90, e3))) != e3, 'witness',
    "J = R_x(pi/2): the conjugate of R_z(pi/2) moves the state e3, which every R_z(s) fixes: Drive'(ball) holds")
note('ball.verdict',
     "SEC'(full), SF'(full), RSC and Drive' all hold: the hypotheses of the corrected Lemma C and of the corrected "
     'strictConvex_of_kInf1 are jointly satisfiable with full effects (non-vacuity; under KINF-1 they were not)')

print('-- 6b. the disk (rebit): the J clause, frozen vs corrected --', flush=True)
Jd = lambda p: (p[0] / 2 + Fr(1, 2), p[1] / 2)
Jdinv = lambda p: (2 * p[0] - 1, 2 * p[1])
DISK = [circle(u) for u in CIRCLE_U]
chk('disk.frozen.J_into', all(sum(c * c for c in Jd(p)) <= 1 for p in DISK), 'sample',
    '|x/2 + (1/2,0)| <= 1/2 + 1/2: the contraction J maps the disk into itself (decisive by the triangle inequality)')
chk('disk.frozen.J_off_axis', Jdinv(mat_vec(R90, Jd((Fr(0), Fr(0))))) == (Fr(-1), Fr(1)), 'witness',
    'J^-1 R90 J moves the centre; every rotation fixes it: the FROZEN clause holds for the rebit with a genuine '
    'rotation group as flow (defect D1b: J need only map Om into Om)')
REF = [[Fr(1), Fr(0)], [Fr(0), Fr(-1)]]
chk('disk.corrected.J_normalizes', mat_mul(REF, mat_mul(R90, REF)) == [[Fr(0), Fr(1)], [Fr(-1), Fr(0)]], 'identity',
    'for J in Aut(disk) = O(2) the conjugate of R_t is R_t or R_-t, on the flow: Drive\'(disk) fails (rebit excluded)')
# defect D3: J an Om-automorphism equal to the identity on Om, off-axis only off the affine span (disk in R^4)
A = [[Fr(1), Fr(0)], [Fr(0), Fr(0)]]


def F4(R):
    return lambda v: mat_vec(R, v[:2]) + mat_vec(R, v[2:])


def J4(v):
    q = v[2:]; Aq = mat_vec(A, q); return (v[0] + Aq[0], v[1] + Aq[1]) + q


def J4inv(v):
    q = v[2:]; Aq = mat_vec(A, q); return (v[0] - Aq[0], v[1] - Aq[1]) + q


DISK4 = [p + (Fr(0), Fr(0)) for p in DISK]
chk('disk4.J_identity_on_Om', all(J4(p) == p for p in DISK4), 'sample', 'J = (p + Aq, q) is the identity on Om = disk x {0}')
w = (Fr(0), Fr(0), Fr(1), Fr(0))
lhs = J4inv(F4(R90)(J4(w)))
chk('disk4.frozen.J_off_axis_on_V', lhs[:2] != (Fr(0), Fr(0)), 'witness',
    'J^-1 (R90 (+) R90) J moves (0,0,1,0) off what any R_s (+) R_s gives there (first block 0): the V-level clause '
    'holds although J is trivial on Om (defect D3); the clause must compare on Om')

# ==================================================================================================================
section(7, 'SIC ball on four ontic states (Main.md four-state model)')
SIGNS = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
AV = [tuple(Q3(0, Fr(s, 3)) for s in sg) for sg in SIGNS]
sic_p = lambda r: [(1 + dot(a, r)) / 4 for a in AV]
resp = lambda c, r: sum((c[i] * sic_p(r)[i] for i in range(4)), Q3(0))
ONE = (1, 1, 1, 1)
chk('sic.unit_response_is_unit', all(resp(ONE, r) == 1 for r in SPHERE), 'sample',
    'c = (1,1,1,1) is the unit on the ball (sum p_i = 1): ' + OLD + ' SEC held at every frontier point via it')
chk('sic.all_positive', all(all(x.is_pos() for x in sic_p(r)) for r in SPHERE), 'sample',
    'at each rational sphere point every p_i > 0')
note('sic.SEC_response_fails',
     "so a response effect certain there has c = (1,1,1,1) (response_eq_one_forces), i.e. it is the unit, not proper: "
     "SEC'(response) FAILS at every such pure state.  The ball is drivable (section 6), so KInf1'(ball, response) is "
     'FALSE, while the frozen KInf1(ball, response) was TRUE via the unit')
TAN = [tuple(-x for x in a) for a in AV]
for i, r in enumerate(TAN):
    c = tuple(0 if j == i else 1 for j in range(4))
    chk('sic.tangency.%d' % i, resp(c, r) == 1 and (1 - resp(c, TAN[(i + 1) % 4])).is_pos(), 'witness',
        'the response effect 1 - p_%d is proper and certain at the tangency point -a_%d: SEC\' holds there' % (i, i))
note('sic.SF_response',
     "SF'(response) holds because the ball is RSC and RSC gives SF' for every family (L5); exposed points "
     'by proper response effects = the four tangency points (F2 attained)')
# ambient-dimension degeneracy: the same body in simplex coordinates p in R^4 lies on sum p = 1
mm = (Fr(1, 4),) * 4
chk('sic.R4.maximally_mixed_not_interior', sum(mm) == 1 and sum(x + Fr(1, 10 ** 6) for x in mm) != 1, 'witness',
    'in R^4 the body lies in the hyperplane sum p = 1, so its V-interior is empty and the maximally mixed state is '
    'a V-frontier point')
note('sic.R4.only_improper_certain',
     'the maximally mixed state is not an algebraic boundary state (in Bloch coordinates 0 - eps y stays in the ball), '
     "so by section 1 (ii) every effect certain there is 1 on the whole body: a V-frontier SEC' FAILS for full effects "
     "and KInf1'(SIC body in R^4, full) would be FALSE, while KInf1'(ball in R^3, full) is TRUE.  The algebraic "
     'boundary removes this dependence on the ambient space')

# ==================================================================================================================
section(8, 'Caratheodory orbitope C_2 = conv{(cos t, sin t, cos 2t, sin 2t)}: exact capacity-three triple in Q(sqrt3)')


def section_c2():
    """The triple t = 0, 2pi/3, 4pi/3 with e_i = (4/9)(1 - cos(t - t_j))(1 - cos(t - t_k)) is perfectly
    distinguishable: a capacity-three body that is not centrally symmetric."""
    # angles k*pi/3 in Q(sqrt 3)
    COS = {0: Q3(1), 1: Q3(Fr(1, 2)), 2: Q3(Fr(-1, 2)), 3: Q3(-1), 4: Q3(Fr(-1, 2)), 5: Q3(Fr(1, 2))}
    SIN = {0: Q3(0), 1: Q3(0, Fr(1, 2)), 2: Q3(0, Fr(1, 2)), 3: Q3(0), 4: Q3(0, Fr(-1, 2)), 5: Q3(0, Fr(-1, 2))}
    C2_CIRCLE_U = [Fr(0), Fr(1), Fr(-1), Fr(1, 2), Fr(2), Fr(-3), Fr(1, 3), Fr(5, 7), Fr(-7, 4), Fr(3), Fr(-2, 9),
                   Fr(11, 3)]
    T = [0, 2, 4]                                                     # t_j = 2j pi/3 as multiples of pi/3

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
    ev = lambda i, x: E[i][0] + dot(E[i][1], x)
    alpha_sum = sum((E[i][0] for i in range(3)), Q3(0))
    beta_sum = [sum((E[i][1][m] for i in range(3)), Q3(0)) for m in range(4)]
    unit_ok = alpha_sum == 1 and all(x.is_zero() for x in beta_sum)
    chk('c2.unit', unit_ok, 'identity', 'sum_i e_i = 1 as affine functionals')
    delta_ok = True
    for i in range(3):
        for j in range(3):
            ok = ev(i, x_of_angle(T[j])) == (1 if i == j else 0)
            delta_ok = delta_ok and ok
            chk('c2.delta.%d%d' % (i, j), ok, 'witness')
    for i in range(3):
        a, b = [T[k] for k in range(3) if k != i]
        for u in C2_CIRCLE_U:
            x = x_of_u(u)
            val = ev(i, x)
            chk('c2.product_identity.%d.u=%s' % (i, u), val == product_form(a, b, x), 'sample')
            chk('c2.nonneg.%d.u=%s' % (i, u), val.is_nonneg(), 'sample')
    # the product identity on the whole circle: rational parametrization (all points but (-1, 0)) plus t = pi
    u = sp.Symbol('u')
    cs, sn = (1 - u ** 2) / (1 + u ** 2), 2 * u / (1 + u ** 2)
    sym_ok = True
    for i in range(3):
        a, b = [T[k] for k in range(3) if k != i]
        al_, be_ = E[i][0].to_sympy(), [q.to_sympy() for q in E[i][1]]
        lhs_ = al_ + be_[0] * cs + be_[1] * sn + be_[2] * (cs ** 2 - sn ** 2) + be_[3] * (2 * sn * cs)
        rhs_ = sp.Rational(4, 9) * (1 - (cs * COS[a % 6].to_sympy() + sn * SIN[a % 6].to_sympy())) \
            * (1 - (cs * COS[b % 6].to_sympy() + sn * SIN[b % 6].to_sympy()))
        ok = sp.expand(sp.numer(sp.together(lhs_ - rhs_))) == 0 and ev(i, x_of_angle(3)) == product_form(a, b, x_of_angle(3))
        sym_ok = sym_ok and ok
        chk('c2.product_identity.symbolic.%d' % i, ok, 'identity',
            'e_%d = (4/9)(1 - cos(t - t_j))(1 - cos(t - t_k)) at every point of the circle (rational parametrization '
            'in u, and t = pi); each factor is >= 0 since |cos(t - s)| <= 1, so e_%d >= 0 on every generator' % (i, i))
    pts = [x_of_angle(k) for k in T]
    distinct = all(pts[i] != pts[j] for i in range(3) for j in range(i + 1, 3))
    chk('c2.capacity3', distinct and unit_ok and delta_ok and sym_ok, 'witness',
        'three distinct extreme points x(0), x(2pi/3), x(4pi/3); e_i >= 0 on C_2 by the identity, sum_i e_i = 1, '
        'hence e_i <= 1; e_i(x(t_j)) = delta_ij: perfectly distinguishable with full effects')
    refl = tuple(-c for c in x_of_angle(0))                            # the reflection of x(0) through 0
    val = ev(0, refl)
    chk('c2.not_centrally_symmetric', val == Fr(-1, 3) and not val.is_nonneg(), 'witness',
        'e_0(-x(0)) = 2 alpha_0 - 1 = -1/3 < 0 while e_0 >= 0 on C_2: -x(0) is not in C_2, so C_2 is not centrally '
        'symmetric about 0')
    note('c2.centre_is_0',
         'a centre of symmetry c is unique (two point reflections compose to a translation by twice their '
         'difference, which preserves no bounded set unless trivial) and so is fixed by the automorphisms '
         '(x0,x1;x2,x3) -> (R_s(x0,x1); R_2s(x2,x3)), whose only common fixed point is 0; with c2.not_centrally_'
         'symmetric, C_2 is centrally symmetric about no point, and Lemma D does not apply: capacity three is '
         'consistent with full effects only because its central-symmetry hypothesis fails')


section_c2()

# ==================================================================================================================
section(9, 'regular pentagon in Q(sqrt5): capacity 2, strongly self-dual, frame-transitive, not centrally symmetric, '
           'SF fails')


def section_pentagon():
    c1 = Q5(Fr(-1, 4), Fr(1, 4)); c2 = Q5(Fr(-1, 4), Fr(-1, 4))       # cos 72, cos 144
    s2r = Q5(Fr(-1, 2), Fr(1, 2))                                    # sin144/sin72 = 2cos72
    P = [(Q5(1), Q5(0)), (c1, Q5(1)), (c2, s2r), (c2, -s2r), (c1, Q5(-1))]   # affine-regular pentagon
    # P is the linear image of the regular pentagon (cos 72k, sin 72k): centroid 0, P_0 and P_1 independent, and
    # the regular recurrence z_{k+1} + z_{k-1} = 2 cos72 z_k holds, which fixes P_2..P_4 from P_0, P_1.
    cen = (sum((p[0] for p in P), Q5(0)) / 5, sum((p[1] for p in P), Q5(0)) / 5)
    rec = all(P[(k + 1) % 5][m] + P[(k - 1) % 5][m] == 2 * c1 * P[k][m] for k in range(5) for m in range(2))
    indep = (P[0][0] * P[1][1] - P[0][1] * P[1][0]).sign() != 0
    chk('pent.affine_regular', cen == (Q5(0), Q5(0)) and rec and indep, 'identity',
        'centroid 0, P_{k+1} + P_{k-1} = 2 cos72 P_k for every k, P_0 and P_1 independent: P is a linear image of the '
        'regular pentagon, so every affine (and cone-linear) invariant below is the regular pentagon\'s')
    turn = [det3([1, *P[i]], [1, *P[(i + 1) % 5]], [1, *P[(i + 2) % 5]]).sign() for i in range(5)]
    chk('pent.convex_position', len(set(turn)) == 1 and turn[0] != 0, 'enumerate',
        'every consecutive vertex triple turns the same way, strictly: five extreme points, no three collinear')

    def dist_interval(i, j):
        # distinguishing effects e = c0 + c1 x + c2 y with e(v_i) = 1, e(v_j) = 0, 0 <= e <= 1 on the vertices;
        # e = base + s * null where null vanishes at v_i and v_j; returns the feasible s-interval or None
        k = next(m for m in range(5) if m not in (i, j))
        A_ = [[1, *P[i]], [1, *P[j]], [1, *P[k]]]
        base = solve3(A_, [Q5(1), Q5(0), Q5(0)]); null = solve3(A_, [Q5(0), Q5(0), Q5(1)])
        ev = lambda c, v: c[0] + c[1] * v[0] + c[2] * v[1]
        lo, hi = None, None
        for v in P:
            b0, n0_ = ev(base, v), ev(null, v)
            if n0_.sign() == 0:
                if (b0.sign() < 0) or ((b0 - 1).sign() > 0): return None
                continue
            bounds = [(-b0) / n0_, (1 - b0) / n0_]
            l, h = (bounds if n0_.sign() > 0 else bounds[::-1])
            lo = l if lo is None or (l - lo).sign() > 0 else lo
            hi = h if hi is None or (h - hi).sign() < 0 else hi
        if (hi - lo).sign() < 0: return None
        return (lo, hi, base, null)

    frames = [(i, j) for i in range(5) for j in range(5) if i != j and dist_interval(i, j)]
    chk('pent.frames', len(frames) == 10 and all((j - i) % 5 in (2, 3) for i, j in frames), 'enumerate',
        'the ordered perfectly distinguishable vertex pairs (frames) are exactly the 10 distance-2 and distance-3 '
        'pairs; adjacent vertices are not distinguishable')
    lo, hi, base, null = dist_interval(0, 2)
    eff = lambda v: base[0] + lo * null[0] + (base[1] + lo * null[1]) * v[0] + (base[2] + lo * null[2]) * v[1]
    vals = [eff(v) for v in P]
    chk('pent.capacity_ge_2', all(x.sign() >= 0 and (x - 1).sign() <= 0 for x in vals) and vals[0] == 1 and vals[2] == 0,
        'witness', 'an affine e with 0 <= e <= 1 on the vertices, e(v0) = 1, e(v2) = 0: v0, v2 perfectly '
        'distinguishable by e, 1 - e')
    chk('pent.capacity_le_2', distinguishable_vertex_triples(P) == [], 'enumerate',
        'none of the 10 vertex triples is perfectly distinguishable with full effects: every triangle of vertices '
        'leaves a vertex with a negative barycentric coordinate')
    note('pent.capacity_reduction',
         'if states w_1, w_2, w_3 are perfectly distinguishable by e_1 + e_2 + e_3 = 1, each w_i is a mixture of '
         'vertices on which e_i = 1, hence e_j = 0 for j != i; one such vertex per i gives three perfectly '
         'distinguishable vertices.  So pent.capacity_le_2 bounds the capacity of the body, not only of its vertices')
    auts = poly_affine_auts(P)
    chk('pent.aut_count', len(auts) == 10, 'enumerate',
        'of the 60 ordered vertex triples exactly 10 extend to affine automorphisms: Aut = D5')
    orbit = {(a[0][0], a[0][2]) for a in auts}                      # images of the ordered frame (0,2)
    chk('pent.frame_transitive', orbit == set(frames), 'enumerate',
        'the D5-orbit of the ordered frame (0,2) is all 10 ordered frames: Aut acts transitively on ordered frames')
    chk('pent.pure_transitive', len({a[0][0] for a in auts}) == 5, 'enumerate', 'Aut is transitive on the vertices')
    minus_id = ((Q5(-1), Q5(0)), (Q5(0), Q5(-1)))
    chk('pent.not_centrally_symmetric', all(a[1] != minus_id for a in auts), 'enumerate',
        'a point reflection x -> 2c - x preserving the body is an affine automorphism with linear part -I; none of '
        'the 10 has it, so the pentagon is centrally symmetric about no point (Lemma D does not apply)')
    # strong self-duality: Gram criterion with <x,y>_G = a x0 y0 + <x',y'>, a = cos 36 = (1+sqrt5)/4, in regular
    # coordinates r_i = (1, cos 72i, sin 72i): M_ij = <r_i, r_j>_G = a + cos(72(i-j)).  K subset K^G iff M >= 0;
    # K^G subset K iff each facet (adjacent pair j, j+1) has a ray i with M_ij = M_i,j+1 = 0.
    a = Q5(Fr(1, 4), Fr(1, 4)); cosd = {0: Q5(1), 1: c1, 2: c2, 3: c2, 4: c1}
    M = [[a + cosd[(i - j) % 5] for j in range(5)] for i in range(5)]
    nonneg = all(M[i][j].sign() >= 0 for i in range(5) for j in range(5))
    cover = all(any(M[i][j] == 0 and M[i][(j + 1) % 5] == 0 for i in range(5)) for j in range(5))
    chk('pent.strongly_self_dual', a.sign() > 0 and nonneg and cover, 'enumerate',
        'G = diag((1+sqrt5)/4, 1, 1) is positive definite, every Gram entry a + cos(72(i-j)) is >= 0 (K in K^G), and '
        'every facet normal is a ray of K (K^G in K): K = K^G')
    # SF: the edge effect, 1 on [v0, v1] and 0 at v3
    ce = solve3([[1, *P[0]], [1, *P[1]], [1, *P[3]]], [Q5(1), Q5(1), Q5(0)])
    evals = [ce[0] + ce[1] * v[0] + ce[2] * v[1] for v in P]
    chk('pent.edge_effect.valid', all(v.sign() >= 0 and (v - 1).sign() <= 0 for v in evals), 'witness',
        'the affine e with e = 1 on v0, v1 and e(v3) = 0 lies in [0,1] at every vertex: an effect with full effects')
    chk('pent.edge_effect.proper', evals[3] == 0, 'witness', 'e(v3) = 0 < 1: proper on the body')
    chk('pent.SF_fails', evals[0] == 1 and evals[1] == 1 and P[0] != P[1], 'witness',
        "e is certain on the two distinct states v0, v1, hence on the whole edge [v0, v1]: SF'(full) fails")
    note('pent.verdict',
         'capacity 2 with full effects, strongly self-dual and transitive on ordered frames, yet SF fails: these '
         'three premises together do not give SF')


section_pentagon()

# ==================================================================================================================
section(10, 'degenerate bodies')
note('degenerate.empty', "Om empty: no boundary state, no proper effect: SEC', SF', RSC vacuous; Drive' "
     'impossible (N_moves). Harmless')
note('degenerate.singleton', "Om = {p}: p is not a boundary state (y = p only), no effect is proper: "
     "SEC', SF', RSC vacuous; Drive' impossible. Harmless (old SEC used the unit at p; old SF held)")
note('degenerate.open_body',
     "Om = open square: no boundary states, and no proper effect is certain on any state (section 1 (ii)): SEC' and SF' "
     'hold VACUOUSLY and RSC holds.  Any premise must carry IsCompact (or closed and bounded); Mathlib likewise makes '
     'every open convex set StrictConvex (Convex.strictConvex_of_isOpen)')
SEG_H = [((Fr(1),), Fr(1)), ((Fr(-1),), Fr(1))]
SEG_V = [(Fr(1),), (Fr(-1),)]
chk('degenerate.segment', boundary_poly(SEG_H, SEG_V, (Fr(1),)) and not boundary_poly(SEG_H, SEG_V, (Fr(0),)), 'witness',
    "classical bit [-1,1]: SEC'(full), SF'(full), RSC hold (a 1-dim body is strictly convex); excluded only by "
    'drivability (a path from 1 to -1 in the injective affine maps of a line crosses 0, frozen and corrected alike)')
TRI_V = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1))]
fy = lambda p: 1 - p[1]
chk('degenerate.triangle', all(0 <= fy(v) <= 1 for v in TRI_V) and fy(TRI_V[2]) == 0 and fy(TRI_V[0]) == 1
    and fy(TRI_V[1]) == 1, 'witness',
    "classical trit: SF'(full) fails (1 - y is proper and certain on the edge y = 0); not drivable in either version "
    '(its involutions reverse orientation on its span)')

# ==================================================================================================================
section(11, 'route neutrality: self-duality and homogeneity do not give RSC without a rank-two premise')
# real qutrit: 3x3 real symmetric PSD trace-1 matrices; the cone is symmetric (homogeneous and self-dual).
P0 = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(0)]]
P1 = [[Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(0)]]
P2 = [[Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
eq3 = lambda rho: 1 - rho[2][2]                       # the effect tr((1 - |2><2|) rho), in [0,1] on density matrices
chk('rqutrit.SF_fails', eq3(P0) == 1 and eq3(P1) == 1 and eq3(P2) == 0 and P0 != P1, 'witness',
    'the real qutrit (symmetric cone) has a proper effect certain on two distinct pure states: SF fails, not RSC; '
    'so a self-duality/homogeneity route reaches RSC only with capacity (rank) two -- the slot must be RSC itself')
note('trit.self_dual_homogeneous_not_RSC',
     'the classical trit (orthant cone, homogeneous and self-dual) is not RSC either (section 10)')
print('-- 11b. Lean convention for the off-axis clause: (J.symm.trans (flow t)).trans J = J o flow t o J^-1 --', flush=True)
Jsq = lambda p: (p[0] / 2 + Fr(1, 2), p[1] / 2); Jsqinv = lambda p: (2 * p[0] - 1, 2 * p[1])
chk('lean_convention.square', Jsq(mat_vec(R90, Jsqinv((Fr(0), Fr(0))))) == (Fr(1, 2), Fr(-1, 2)), 'witness',
    'J o R90 o J^-1 sends the state 0 to (1/2,-1/2): the frozen clause holds in the Lean composition order too')
chk('lean_convention.ball', mat_vec(Rx90, mat_vec(Rz90, mat_vec(Rx90inv, e3))) != e3, 'witness',
    'J o R_z(pi/2) o J^-1 moves e3 as well')

# ==================================================================================================================
section(12, 'countercontrols: each mutated predicate, identity or enumeration must give the opposite verdict')
# (a) syntactic properness (e != const 1 on V) on the finite-stage gbit: the unit coordinate counts as proper,
#     is certain on two distinct states, so SF would fail on EVERY stage body with two preparations.
syn_proper = lambda f: f((Fr(0),) * 5) != 1                              # 'not the constant 1 functional on V'
chk('cc.syntactic_proper_defeats_SF', syn_proper(coord_unit) and coord_unit(GV[0]) == 1 and coord_unit(GV[1]) == 1
    and GV[0] != GV[1], 'witness', 'mutation: properness tested on V instead of Om reproduces the KINF-1 defect')
# (b) the ball identity without the |u| term is false (so the identity check is not vacuous)
bad = sp.expand((1 - nx) - (sum((xs[i] - us[i]) ** 2 for i in range(3)) / 2 + (1 - sum(v * v for v in xs)) / 2))
chk('cc.ball_identity_needs_unit_u', bad != 0, 'witness', 'dropping (|u|^2 - 1)/2 breaks the identity')
# (c) boundary_poly agrees with a direct eps test and says 'not boundary' at the centre
chk('cc.boundary_direct', not boundary_poly(SQ_H, SQ_V, (Fr(0), Fr(0))) and
    all(in_poly(SQ_H, tuple(c + Fr(1, 10) * (c - y) for c, y in zip((Fr(0), Fr(0)), v))) for v in SQ_V) and
    all(not in_poly(SQ_H, tuple(c + Fr(1, 10 ** 9) * (c - y) for c, y in zip(mid, v))) for v in [(Fr(-1), Fr(0))]),
    'witness', 'centre: every extension stays inside (not boundary); (1,0): the extension away from (-1,0) leaves')
# (d) the frozen J_off_axis witness depends on J being a contraction: an automorphism J (a reflection) normalizes
REFL = lambda p: (p[0], -p[1])
conj_R = [REFL(mat_vec(R90, REFL(v))) for v in SQ_V]
chk('cc.automorphism_J_normalizes_square', conj_R == [mat_vec([[Fr(0), Fr(1)], [Fr(-1), Fr(0)]], v) for v in SQ_V], 'witness',
    'with J a square automorphism the conjugate of R90 is R(-90), a symmetry fixing 0 (no translation): the '
    'off-axis witness in 3b exists only because J may be a non-surjective contraction')
# (e) the corrected SEC on the SIC ball is not failing for a trivial reason: at the tangency points it holds (section 7),
#     and with full effects it holds at every sphere point (ball.SEC_full); the failure is specific to response effects
c_full = lambda r, x: (1 + sum(a * b for a, b in zip(r, x))) / 2
chk('cc.sic_full_effect_certain', all(c_full(r, r) == 1 and c_full(r, tuple(-v for v in r)) == 0 for r in SPHERE), 'sample',
    'the full effect (1 + r.x)/2 is proper and certain at each rational sphere point where every response effect fails')
# (f) Aut enumeration is not vacuous: a non-symmetric quadrilateral has fewer automorphisms
KITE = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-2))]
cnt = 0
for img in permutations(KITE, 3):
    P = [KITE[0], KITE[1], KITE[2]]
    # solve affine map P_k -> img_k exactly (2x2 linear system on differences)
    dx1 = (P[0][0] - P[2][0], P[0][1] - P[2][1]); dx2 = (P[1][0] - P[2][0], P[1][1] - P[2][1])
    dy1 = (img[0][0] - img[2][0], img[0][1] - img[2][1]); dy2 = (img[1][0] - img[2][0], img[1][1] - img[2][1])
    Dm = dx1[0] * dx2[1] - dx2[0] * dx1[1]
    inv = [[dx2[1] / Dm, -dx2[0] / Dm], [-dx1[1] / Dm, dx1[0] / Dm]]
    Y = [[dy1[0], dy2[0]], [dy1[1], dy2[1]]]
    L = mat_mul(Y, inv)
    c = (img[2][0] - L[0][0] * P[2][0] - L[0][1] * P[2][1], img[2][1] - L[1][0] * P[2][0] - L[1][1] * P[2][1])
    f = lambda v: (L[0][0] * v[0] + L[0][1] * v[1] + c[0], L[1][0] * v[0] + L[1][1] * v[1] + c[1])
    if sorted(f(v) for v in KITE) == sorted(KITE):
        cnt += 1
chk('cc.kite_aut', cnt == 2, 'enumerate', 'the same enumeration on a kite finds 2 automorphisms (id and the mirror), not 8')
# (g) the polygon automorphism enumeration of section 9 detects a point reflection when there is one
SQ5 = [(Q5(1), Q5(1)), (Q5(1), Q5(-1)), (Q5(-1), Q5(-1)), (Q5(-1), Q5(1))]
sq5_auts = poly_affine_auts(SQ5)
chk('cc.pent_enumeration_finds_point_reflection', len(sq5_auts) == 8
    and sum(1 for a in sq5_auts if a[1] == ((Q5(-1), Q5(0)), (Q5(0), Q5(-1)))) == 1, 'enumerate',
    'run on the square, the enumeration behind pent.aut_count and pent.not_centrally_symmetric finds 8 automorphisms, '
    'one of them x -> -x: the pentagon verdict is not an artifact of the enumeration')
# (h) the vertex-triple capacity test of section 9 detects a distinguishable triple when there is one
TRI5 = [(Q5(0), Q5(0)), (Q5(1), Q5(0)), (Q5(0), Q5(1)), (Q5(Fr(1, 2)), Q5(0)), (Q5(Fr(1, 2)), Q5(Fr(1, 2)))]
chk('cc.capacity_test_detects_simplex', distinguishable_vertex_triples(TRI5) == [(0, 1, 2)], 'enumerate',
    'run on a triangle listed with two edge midpoints, the test behind pent.capacity_le_2 finds the corner triple '
    '(the midpoints get nonnegative barycentric coordinates) and rejects every triple containing a midpoint')

print('kinds: %s' % ', '.join('%s %d' % (k, KINDS.count(k)) for k in ('identity', 'witness', 'enumerate', 'sample')),
      flush=True)
print('kinf2_foundations_probe: OK -- %d checks' % len(CHECKS), flush=True)
