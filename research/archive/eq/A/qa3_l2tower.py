#!/usr/bin/env python3
"""EQ-A, QA3 -- FiniteRank against the whole single-system package.  Exact arithmetic only.

The l2 tower (a DirectedStages in the kernel's sense, stages indexed by n = 1, 2, ...):
  stage n preparations : rational points x of the unit ball of Q^n (|x|^2 <= 1) with denominators <= n
  stage n effects      : the unit, and  e_u(x) = (1 + <u, x>)/2  for rational unit vectors u of Q^n with denominators <= n
  table                : one global formula, forward maps are inclusions (Q^n in Q^m by zero padding) => SC-inf
The map x -> (e_u(x))_u is, up to the factor 1/2, an isometry from l2 onto the completed body in l^inf(Label) (the
rational unit vectors are dense in the unit sphere of l2), so the completed body is the infinite-dimensional Hilbert
ball.  Checked here on finite stages; the infinite statements are written.
Run:  PYTHONDONTWRITEBYTECODE=1 python3 -I qa3_l2tower.py
"""
from fractions import Fraction as Fr
from itertools import product
import sys
import sympy as sp

N_CHECKS = {'witness': 0, 'identity': 0, 'enumerate': 0, 'sample': 0}
FAILED = []


def chk(name, ok, kind, detail=''):
    N_CHECKS[kind] += 1
    if not ok:
        FAILED.append(name)
    print('%s [%s] %s%s' % ('PASS' if ok else 'FAIL', kind, name, ('  -- ' + detail) if detail else ''))


def note(name, detail):
    print('NOTE [written] %s  -- %s' % (name, detail))


def section(t):
    print('\n=== %s ===' % t)


def rank(M):
    A = [list(r) for r in M]; rows = len(A); cols = len(A[0]); r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [A[i][k] - f * A[r][k] for k in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def dot(u, x):
    return sum(a * b for a, b in zip(u, x))


def pad(v, n):
    return tuple(v) + (Fr(0),) * (n - len(v))


def grid(n):
    return [Fr(k, q) for q in range(1, n + 1) for k in range(-q, q + 1)]


def stage(n, cap_dim=None):
    """preparations and effect directions of stage n, embedded in Q^n.  To keep the exact tables small the
    enumeration is over vectors with at most two nonzero coordinates (still finite, nested, and spanning)."""
    vals = sorted(set(grid(n)))
    preps = set(); dirs = set()
    preps.add(pad((), n))
    for i in range(n):
        for a in vals:
            v = [Fr(0)] * n; v[i] = a
            if a * a <= 1:
                preps.add(tuple(v))
            if a * a == 1:
                dirs.add(tuple(v))
        for j in range(i + 1, n):
            for a in vals:
                for b in vals:
                    if a == 0 or b == 0:
                        continue
                    v = [Fr(0)] * n; v[i] = a; v[j] = b
                    q = a * a + b * b
                    if q <= 1:
                        preps.add(tuple(v))
                    if q == 1:
                        dirs.add(tuple(v))
    return sorted(preps), sorted(dirs)


def eff(u, x):
    return (1 + dot(u, x)) / 2


section('A. Finite stages: SC-inf, BinaryVisible with a sharp pair, values, and unbounded rank')
prev = None
ranks = []
for n in range(1, 6):
    P, U = stage(n)
    table_ok = all(0 <= eff(u, x) <= 1 for u in U for x in P)
    e1 = pad((Fr(1),), n); me1 = tuple(-c for c in e1)
    vis_ok = all(eff(e1, x) + eff(me1, x) == 1 for x in P) and eff(e1, e1) == 1 and eff(e1, me1) == 0
    nested = True
    if prev is not None:
        Pp, Up = prev
        nested = all(pad(x, n) in set(P) for x in Pp) and all(pad(u, n) in set(U) for u in Up) and \
            all(eff(pad(u, n), pad(x, n)) == eff(u, x) for u in Up[:20] for x in Pp[:20])
    T = [[Fr(1)] * len(P)] + [[eff(u, x) for x in P] for u in U]
    rk = rank(T)
    ranks.append(rk)
    chk('stage%d' % n, table_ok and vis_ok and nested and rk == n + 1, 'enumerate',
        '%d preparations, %d sharp directions: table in [0,1]; v0 = e_{e1}, v1 = e_{-e1} sum to one with the sharp pair '
        '(e1, -e1); nested in the next stage with equal values (SC-inf); table rank %d = n + 1' % (len(P), len(U), rk))
    prev = (P, U)
chk('rank_unbounded_witness', ranks == [2, 3, 4, 5, 6], 'enumerate', 'stage ranks %s grow without bound (one new '
    'coordinate per stage): the witness submatrix {unit, e_{e_i}} x {0, e_i} is (1+delta)/2-shaped of rank n+1' % ranks)
note('A.subenumeration', 'the stages above enumerate only vectors with at most two nonzero coordinates (to keep the '
     'exact tables small); the countermodel is the FULL tower (every rational point of the ball of Q^n and every rational '
     'unit vector of Q^n with denominators <= n).  Its stage tables contain the ones above as submatrices (so rank >= '
     'n + 1, values, visible test and sharp pair are inherited) and are affine in x in Q^n (so rank <= n + 1).')


def full_stage(n):
    vals = sorted(set(grid(n)))
    P = [v for v in product(vals, repeat=n) if dot(v, v) <= 1]
    U = [v for v in product(vals, repeat=n) if dot(v, v) == 1]
    return P, U


Pf, Uf = full_stage(3)
full_support = [u for u in Uf if all(c != 0 for c in u)]
Tf = [[Fr(1)] * len(Pf)] + [[eff(u, x) for x in Pf] for u in Uf]
chk('full_stage3', rank(Tf) == 4 and len(full_support) > 0 and all(0 <= v <= 1 for row in Tf for v in row), 'enumerate',
    'the unrestricted stage 3 (%d preparations, %d rational unit directions, %d of full support such as (1/3,2/3,2/3)): '
    'table in [0,1], rank 4 = n + 1' % (len(Pf), len(Uf), len(full_support)))
note('A.not_finiteRank', 'under SC-inf the stage-n table rank is at most dim span(prepVec) = dim affineSpan(body) + 1 '
     '(restriction of the preparation vectors to the stage-n labels is linear, and they lie on the hyperplane unit = 1 '
     'off the origin); unbounded stage ranks therefore give an infinite-dimensional affine span: not FiniteRank.  '
     'Directly: prepVec(e_k) - prepVec(0), k = 1..n, are independent (their e_{e_j} coordinates are delta_jk/2).')

section('B. The elementary package holds on the l2 tower')
x = sp.symbols('x1:4', real=True); u = sp.symbols('u1:4', real=True)
ident = sp.expand((1 - sum(a * b for a, b in zip(u, x))) - (sum((a - b) ** 2 for a, b in zip(x, u)) / 2
                                                            + (1 - sum(a * a for a in x)) / 2)
                  - (1 - sum(a * a for a in u)) / 2)
chk('ball_face_identity', ident == 0, 'identity', '1 - <u,x> = |x-u|^2/2 + (1-|x|^2)/2 + (1-|u|^2)/2 (any dimension, '
    'coordinatewise): for |u| = 1, |x| <= 1, e_u(x) = 1 iff x = u, so every sharp test has one certain state')
note('B.package', 'the Hilbert ball is centrally symmetric about 0 (ELEM2 with e1, -e1, by the CS lemma) and strictly '
     'convex (inner-product space; KF:658 singletonFaces_closedBall, KF:617): GEOM2 and SingletonFaces(full) hold; '
     'capacity 2 (Lemma D, KF:632); HasTwoSharpTests (e_{e1}, e_{e2}); the visible pair (e1, -e1) is sharp at stage 1, '
     'so K-inf-Seed holds with an available seed (sharpSeed_completion)')

# label duals and dense orbits: rational Householder reflections
def householder(v):
    nn = dot(v, v)
    return lambda y: tuple(y[i] - 2 * v[i] * dot(v, y) / nn for i in range(len(y)))


Pn, Un = stage(5)
sampleU = Un[::7][:12]
ok_ld = True; ok_body = True
for u0 in sampleU:
    v = tuple(a - b for a, b in zip(pad((Fr(1),), 5), u0))
    if dot(v, v) == 0:
        continue
    H = householder(v)
    ok_ld = ok_ld and H(pad((Fr(1),), 5)) == u0                       # the orbit of e1 contains every rational u
    for uu in Un[::11][:10]:
        Hu = H(uu)
        ok_ld = ok_ld and dot(Hu, Hu) == 1 and all(eff(uu, H(xx)) == eff(Hu, xx) for xx in Pn[::23][:15])
    ok_body = ok_body and all(dot(H(xx), H(xx)) == dot(xx, xx) for xx in Pn[::17][:15])
chk('householder_label_dual', ok_ld, 'sample',
    'H_v with v = e1 - u maps e1 to u; the pullback of e_u along H is e_{Hu} with Hu a rational unit vector: a label '
    'dual (stage-raising: Hu has a larger denominator, so it sits at a later stage)')
chk('householder_preserves_body', ok_body, 'sample', 'rational reflections preserve |x|: Prep-valued operation data')
note('B.dense_V4', 'rational unit vectors are dense in the unit sphere of l2 (stereographic projection of rational '
     'points, finitely supported); the countable family G of rational reflections H_{e1-u} therefore has a dense orbit '
     'on the boundary (the isometry x -> (e_u(x))_u carries density to the completion in l^inf(Label)), and, being '
     'label dual and self-inverse, satisfies SeedOrbitAvailable with avail = the stage effects.  Exact '
     'BoundaryTransitive holds with all orthogonal maps and avail = the pointwise closure of the stage effects.')

section('C. The completion is not totally bounded in the operational metric')
ok_sep = True
for (j, k) in ((0, 1), (0, 4), (2, 3), (1, 4)):
    ej = pad((Fr(0),) * j + (Fr(1),), 5); ek = pad((Fr(0),) * k + (Fr(1),), 5)
    w = [Fr(0)] * 5; w[j] = Fr(3, 5); w[k] = Fr(-4, 5); w = tuple(w)
    ok_sep = ok_sep and w in set(Un) and abs(eff(w, ej) - eff(w, ek)) == Fr(7, 10)
chk('operational_separation', ok_sep, 'witness', 'for j != k the stage effect along (3/5)e_j - (4/5)e_k separates the '
    'states e_j, e_k by 7/10: infinitely many states pairwise at operational distance >= 7/10 in l^inf(Label)')
note('C.reading', 'so "the completed body is totally bounded in the operational sup-metric" (finite resolution at '
     'every precision) would exclude this tower; whether it implies FiniteRank for every body carrying the package '
     'is OPEN (wall: no infinite-dimensional analogue of TRB-1 / IIP-1 in the kernel; a Riesz-type lemma needs the '
     'available effects to norm the base norm, itself an availability premise).')

section('C2. Countercontrol for Theorem R: a compact infinite-dimensional ellipsoid tower (V4 must fail)')
# E = {x in l2 : sum i^2 x_i^2 <= 1} (semi-axes a_i = 1/i), effects e_u(x) = (1 + <u,x>)/2 for l2-unit rational u.
# The completion is isometric (x 1/2) to (E, l2), which is compact (E lies in the Hilbert cube prod [-1/i, 1/i]).
def a_norm2(x):
    return sum((i + 1) ** 2 * c * c for i, c in enumerate(x))


ok_tab = True; rk_e = []
for n in range(1, 6):
    P, U = stage(n)
    PE = [x for x in P if a_norm2(x) <= 1]
    ok_tab = ok_tab and all(0 <= eff(u, x) <= 1 for u in U for x in PE)
    witness_preps = [pad((), n)] + [pad((Fr(0),) * k + (Fr(1, k + 1),), n) for k in range(n)]
    ok_tab = ok_tab and all(w in set(PE) for w in witness_preps)
    rk_e.append(rank([[Fr(1)] * len(PE)] + [[eff(u, x) for x in PE] for u in U]))
chk('ellipsoid.tables_and_rank', ok_tab and rk_e == [2, 3, 4, 5, 6], 'enumerate',
    'tables in [0,1]; the points e_k/k are stage preparations; stage ranks %s grow: not FiniteRank' % rk_e)
Pn5, Un5 = stage(5)
sharp_dirs = [u for u in Un5 if sum(c * c / (i + 1) ** 2 for i, c in enumerate(u)) == 1]
chk('ellipsoid.only_e1_sharp', sorted(sharp_dirs) == sorted([pad((Fr(1),), 5), pad((Fr(-1),), 5)]), 'enumerate',
    'max over E of <u,x> is (sum u_i^2/i^2)^(1/2); a sharp available effect needs it = 1 = |u|, i.e. u = +-e1: of the '
    '%d stage-5 directions only +-e1 give sharp effects (written for all u: sum u_i^2 (1 - 1/i^2) = 0)' % len(Un5))
v = (Fr(1), Fr(-1, 2))
a_ip = lambda x, y: sum((i + 1) ** 2 * x[i] * y[i] for i in range(len(x)))
Ha = lambda x: tuple(x[i] - 2 * a_ip(v, x) / a_ip(v, v) * v[i] for i in range(2))
ok_h = Ha((Fr(1), Fr(0))) == (Fr(0), Fr(1, 2)) and all(a_ip(Ha(x), Ha(x)) == a_ip(x, x)
                                                       for x in [(Fr(p, 7), Fr(q, 11)) for p in range(-3, 4) for q in range(-2, 3)])
# transported sharp effect along Ha: x -> (1 + <e1, Ha^{-1} x>_a ... ) = (1 + 2 x_2)/2 ; is it some (1 + <u,x>)/2, |u| = 1?
transported = (Fr(0), Fr(2))          # linear part of (1 + 2 x_2)/2 times 2
chk('ellipsoid.V4_fails', ok_h and sum(c * c for c in transported) != 1, 'witness',
    'the a-reflection along v = e1 - e2/2 preserves E (a-isometry, bounded rank-one perturbation), carries e1 to the '
    'a-unit vector e2/2, and transports the sharp seed (1 + x1)/2 to (1 + 2 x2)/2, whose direction (0,2) is not an '
    'l2-unit vector: not available.  The tower is compact, ELEM2 (centre 0), strictly convex (Hilbert a-norm), '
    'BoundaryTransitive under the a-orthogonal group, has a sharp visible pair (+-e1), and is not FiniteRank: V4 is '
    'load-bearing in Theorem R')
note('C2.theorem_R', 'Theorem R (written): let Om be convex and compact in V, RelStrictConvex (e.g. ELEM2 & GEOM2), '
     'G a group of affine automorphisms with PreservesBody and a dense boundary orbit, r a sharp seed with '
     'SeedOrbitAvailable G r avail, every member of avail 1-Lipschitz on V (stage coordinates of l^inf(Label) and their '
     'pointwise limits are).  Then FiniteRank Om.  Proof: N(v) = sup_g |lin(r o g^-1)(v)| is a G-invariant seminorm '
     '<= |.|_V; it separates points (a uniform limit of transports certain at both ends of a chord with N = 0 would be '
     'a proper effect certain at two points, against RelStrictConvex; Arzela-Ascoli); G acts on the N-compact Om by '
     'N-isometries, so it fixes some c0 (Kakutani); c0 is not a boundary state (dense orbits) so kappa = r(c0) < 1 (L2); '
     'for a boundary state z = c0 + t v, 1 - kappa <= sup_g (e_g(z) - e_g(c0)) <= t N(v), so Om contains the N-ball of '
     'radius 1 - kappa about c0 in the direction space D; that ball is N-compact, so dim D < infinity (Riesz).  '
     'Converse: FiniteRank => the closed bounded body in a finite-dimensional affine subspace is compact.')

section('D. The finite-carrier route to FiniteRank is closed by the package')
note('D.finite_carrier', 'on a finite carrier FiniteRank is automatic but the body is a polytope (NG1, oistage note, '
     're-checked in SA P4 C9).  ELEM2 & GEOM2 make the body relatively strictly convex; a relatively strictly convex '
     'polytope has dimension <= 1 (an edge midpoint of a polygon face is a boundary state).  With HasTwoSharpTests '
     '(K1-SHARP-TESTS-1: on eball d it is 2 <= d) that is a contradiction: the observer-native finite-carrier source '
     'of FiniteRank is incompatible with the elementary package beyond the classical bit (exact instances: the square, '
     'hexagon, pentagon and bipyramid controls of qa1_controls.py).')

total = sum(N_CHECKS.values())
print('\nsummary: ' + ', '.join('%s %d' % kv for kv in N_CHECKS.items()))
if FAILED:
    print('qa3_l2tower: FAIL -- %d of %d: %s' % (len(FAILED), total, ', '.join(FAILED)))
    sys.exit(1)
print('qa3_l2tower: OK -- %d exact checks' % total)
