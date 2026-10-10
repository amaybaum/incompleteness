#!/usr/bin/env python3
"""EQ-A, QA2 -- K-inf-Seed and K-inf-V4 against the QA1 package plus K-inf-Stage.  Exact arithmetic only.

Two stage towers over the Bloch ball written in SIC (tetrahedral) coordinates, both rational:
  s in Q^4, sum s = 0, (3/4) sum s_i^2 <= 1        (s_i = a_i . r for the tetrahedral unit vectors a_i, |r| <= 1)
  p_i(s) = (1 + s_i)/4                              (the four SIC response probabilities)
  * SIC tower        : stage effects = response effects e_c = sum c_i p_i, c in [0,1]^4 (unit: c = 1111)
  * SIC+axis tower   : the same plus r = 2 p_1 = (1 + s_1)/2 and its complement 1 - r
Everything is a single global formula, so SC-inf holds by construction; the body is affinely the Euclidean 3-ball.
Run:  PYTHONDONTWRITEBYTECODE=1 python3 -I qa2_towers.py
"""
from fractions import Fraction as Fr
from itertools import product, permutations
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


# ------------------------------------------------------------------------------------------ the SIC coordinates ---
B = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]          # b_i = sqrt3 a_i, integer
section('A. SIC coordinates: an exact rational chart of the Bloch ball')
G = [[Fr(sum(B[i][k] * B[j][k] for k in range(3)), 3) for j in range(4)] for i in range(4)]
chk('gram', all(G[i][j] == (1 if i == j else Fr(-1, 3)) for i in range(4) for j in range(4)), 'identity',
    'a_i . a_j = b_i . b_j / 3 = 1 (i = j), -1/3 (i != j)')
frame = [[sum(B[i][a] * B[i][b] for i in range(4)) for b in range(3)] for a in range(3)]
chk('frame_sum', frame == [[4, 0, 0], [0, 4, 0], [0, 0, 4]] and all(sum(B[i][a] for i in range(4)) == 0 for a in range(3)),
    'identity', 'sum_i b_i b_i^T = 4 I and sum_i b_i = 0: sum_i a_i a_i^T = (4/3) I, sum_i a_i = 0')
r1, r2, r3 = sp.symbols('r1 r2 r3', real=True)
svec = [sp.Rational(1, 1) * (B[i][0] * r1 + B[i][1] * r2 + B[i][2] * r3) / sp.sqrt(3) for i in range(4)]
chk('chart_identity', sp.simplify(sum(svec)) == 0 and
    sp.simplify(sp.Rational(3, 4) * sum(x ** 2 for x in svec) - (r1 ** 2 + r2 ** 2 + r3 ** 2)) == 0, 'identity',
    's_i = a_i . r satisfies sum s = 0 and (3/4) sum s_i^2 = |r|^2: the s-chart carries the unit ball onto the body')
note('A.ball', 'so the completed body of either tower is affinely the Euclidean 3-ball: ELEM2 (centrally symmetric '
     'about s = 0) and GEOM2 (strictly convex) hold; it carries the landed transitive families fullAut 3 '
     '(boundaryTransitive_fullAut, EffectSpace.lean:337) and ratRefl 3 (denseBoundaryOrbit_ratRefl, DenseOrbit.lean:359)')

# ------------------------------------------------------------------------------------- no response effect is sharp ---
section('B. SIC tower: no available effect is a sharp seed (K-inf-Seed with an available seed fails)')
c = sp.symbols('c1:5', real=True)
Csum = sum(c)
cGc = sum(c[i] * c[j] * sp.Rational(G[i][j].numerator, G[i][j].denominator) for i in range(4) for j in range(4))
pairsum = sum(c[i] * c[j] for i in range(4) for j in range(i + 1, 4))
chk('sharp_identity', sp.expand(Csum ** 2 - cGc - sp.Rational(8, 3) * pairsum) == 0, 'identity',
    '(sum c)^2 - |sum c_i a_i|^2 = (8/3) sum_{i<j} c_i c_j')
note('B.no_sharp', 'on the ball, e_c = sum c/4 + (sum c_i a_i).r/4 has max (sum c + |sum c a|)/4 and min '
     '(sum c - |sum c a|)/4.  A sharp seed needs max = 1 and min = 0, i.e. sum c = 2 and |sum c a| = 2; by the identity '
     'sum_{i<j} c_i c_j = 0, so with c >= 0 at most one c_i is nonzero and sum c <= 1 < 2.  No response effect, and so '
     'no available effect of the SIC tower or of its pointwise closure (the response set is closed), is a sharp seed.')

# finite stages, exhaustive
def stage_preps(n):
    # rational points with denominators <= n: nested under <= (stage n is contained in stage n+1)
    grid = sorted({Fr(k, q) for q in range(1, n + 1) for k in range(-q, q + 1)})
    out = []
    for s1, s2, s3 in product(grid, repeat=3):
        s4 = -(s1 + s2 + s3)
        if -1 <= s4 <= 1 and Fr(3, 4) * (s1 * s1 + s2 * s2 + s3 * s3 + s4 * s4) <= 1:
            out.append((s1, s2, s3, s4))
    return out


def ev(cv, s):
    return sum(cv[i] * (1 + s[i]) / 4 for i in range(4))


CSET = list(product([Fr(0), Fr(1, 2), Fr(1)], repeat=4))
for n in (2, 3, 6):
    P_n = stage_preps(n)
    vals_ok = all(0 <= ev(cv, s) <= 1 for cv in CSET for s in P_n)
    unit_ok = all(ev((1, 1, 1, 1), s) == 1 for s in P_n)
    vis_ok = all(ev((1, 1, 0, 0), s) + ev((0, 0, 1, 1), s) == 1 for s in P_n)
    no_sharp_stage = all(not (any(ev(cv, s) == 1 for s in P_n) and any(ev(cv, s) == 0 for s in P_n)) for cv in CSET)
    rk = rank([[ev(cv, s) for s in P_n] for cv in CSET])
    chk('sic.stage%d' % n, vals_ok and unit_ok and vis_ok and no_sharp_stage and rk == 4, 'enumerate',
        '%d preparations x %d effects: table in [0,1], unit row 1, BinaryVisible test (p1+p2, p3+p4) sums to 1, no '
        'stage effect is certain at one stage preparation and impossible at another, table rank %d (affine dim 3)'
        % (len(P_n), len(CSET), rk))
chk('sic.nested_SCinf', set(stage_preps(2)) <= set(stage_preps(3)) <= set(stage_preps(6)), 'enumerate',
    'stage n is contained in stage m for n <= m and every table entry is the one global formula: the forward maps are '
    'inclusions and SC-inf holds by construction')
tang = (Fr(1, 3), Fr(1, 3), Fr(1, 3), Fr(-1))
chk('sic.tangency_certain_not_sharp', ev((1, 1, 1, 0), tang) == 1 and
    min(ev((1, 1, 1, 0), s) for s in stage_preps(6)) == Fr(1, 2), 'witness',
    'e_(1110) = 1 - p_4 is certain at the tangency point -a_4 (a stage preparation) but never below 1/2: certain, not sharp')

# ------------------------------------------------------------------------- SIC+axis tower: Seed holds, V4 fails ---
section('C. SIC+axis tower: an available sharp seed (ElemVis holds), V4 fails for every transitive or dense G')
sp_plus = (Fr(1), Fr(-1, 3), Fr(-1, 3), Fr(-1, 3))
sp_minus = tuple(-x for x in sp_plus)
r_axis = lambda s: (1 + s[0]) / 2
on_sphere = lambda s: sum(s) == 0 and Fr(3, 4) * sum(x * x for x in s) == 1
chk('axis.stage_sharp_pair', on_sphere(sp_plus) and on_sphere(sp_minus) and r_axis(sp_plus) == 1 and
    r_axis(sp_minus) == 0 and sp_plus in stage_preps(3), 'witness',
    's+ = a_1 and s- = -a_1 are stage preparations (n = 3) on the sphere with r = 1, 0: SC-inf + this stage pair give '
    'K-inf-Seed on the completion (sharpSeed_completion, StageCompletion.lean:224); s+, s- are pure with midpoint 0 '
    'interior: ElemVis holds with the visible test (r, 1 - r)')
chk('axis.r_effect', all(0 <= r_axis(s) <= 1 for s in stage_preps(6)), 'enumerate', 'r is an effect on every preparation')


# exact identity of affine functionals on the body: values at the four tangency points t_k = -a_k
TANG = [tuple(Fr(-1) if i == k else Fr(1, 3) for i in range(4)) for k in range(4)]
chk('tangency_affinely_independent', rank([[Fr(1)] + list(t[:3]) for t in TANG]) == 4, 'identity',
    'the four tangency points are affinely independent in the 3-dim body: an affine functional on the body is fixed '
    'by its four values there')


def response_member(t):
    """is the value vector t = (e(t_1),...,e(t_4)) that of a response effect e_c, c in [0,1]^4?
    e_c(t_k) = (sum c - c_k)/3, so c_k = sum t - 3 t_k (unique); feasible iff every c_k in [0,1]."""
    S = sum(t)
    cv = [S - 3 * tk for tk in t]
    return all(0 <= x <= 1 for x in cv) and all(ev(cv, TANG[k]) == t[k] for k in range(4))


val = lambda f: tuple(f(tk) for tk in TANG)
avail_axis_extra = [val(r_axis), val(lambda s: 1 - r_axis(s))]
two_p2 = val(lambda s: (1 + s[1]) / 2)
chk('axis.transport_unavailable', not response_member(two_p2) and two_p2 not in avail_axis_extra, 'witness',
    'the transport of r along the tetrahedral reflection that swaps a_1 and a_2 is 2 p_2 = (1 + s_2)/2, value vector '
    '%s: not a response effect (forced c_2 = 2 > 1) and not r, 1 - r: V4 fails' % (two_p2,))
note('C.V4_fails_dense', 'the sharp seeds available in the SIC+axis tower are exactly r and 1 - r (section B plus the '
     'two additions); on the ball a sharp seed is fixed by its certain point (sharp_eq_of_certain, EFF-1), and the '
     'transport of r along g is certain at g(a_1).  Any G with a dense (a fortiori transitive) boundary orbit has g '
     'with g(a_1) not in {a_1, -a_1}, so SeedOrbitAvailable fails for every such G, while SC-inf, BinaryVisible with a '
     'sharp pair, FiniteRank, ElemVis, GEOM2, K-inf-Seed, K-inf-Trans (fullAut 3) and the dense form (ratRefl 3) hold.')

# the tetrahedral reflection in r-space acts on s-coordinates by a rational matrix A_ij = (1/4) b_i^T H b_j
def refl(nv):
    nn = sum(x * x for x in nv)
    return [[Fr(1 if i == j else 0) - Fr(2 * nv[i] * nv[j], nn) for j in range(3)] for i in range(3)]


def s_action(H):
    return [[Fr(sum(B[i][a] * sum(H[a][b] * B[j][b] for b in range(3)) for a in range(3)), 4) for j in range(4)]
            for i in range(4)]


H12 = refl((0, 1, 1))
A12 = s_action(H12)
# the chart lives on the hyperplane sum s = 0, where a 4x4 matrix is fixed only up to adding a multiple of the
# all-ones row; compare actions on the preparations, not matrices
swap12 = lambda s: (s[1], s[0], s[2], s[3])
act = lambda A, s: tuple(sum(A[i][j] * s[j] for j in range(4)) for i in range(4))
chk('tet_reflection_swaps', all(act(A12, s) == swap12(s) for s in stage_preps(3)), 'enumerate',
    'the reflection in the plane orthogonal to b_1 - b_2 acts on every stage-3 preparation as s_1 <-> s_2 (a symmetry '
    'of the tetrahedron)')
Hx = refl((1, 0, 0))
Ax = s_action(Hx)
sample = stage_preps(3)
img = [tuple(sum(Ax[i][j] * s[j] for j in range(4)) for i in range(4)) for s in sample]
chk('ratrefl_rational_action', all(sum(t) == 0 and Fr(3, 4) * sum(x * x for x in t) == Fr(3, 4) * sum(x * x for x in s)
                                   for t, s in zip(img, sample)), 'enumerate',
    'a rational reflection (normal (1,0,0), not a tetrahedral symmetry) acts on s by a rational matrix preserving the '
    'body: the landed ratRefl family is Prep-valued on this tower (maps rational preparations to rational points)')
pull_p1 = val(lambda s: (1 + sum(Ax[0][j] * s[j] for j in range(4))) / 4)
chk('ratrefl_not_label_dual', not response_member(pull_p1), 'witness',
    'the pullback of p_1 along that reflection is not a response effect (value vector %s): the ratRefl operations '
    'carry no label dual on the SIC family, which is why V4 can fail with a dense G' % (pull_p1,))

# ------------------------------------------------------------------- positive control: label dual => V4 (finite G) ---
section('D. Positive control for "label-dual inverses => V4": the tetrahedral group on the all-axes tower')
avail_all_extra = [val(lambda s, j=j: (1 + s[j]) / 2) for j in range(4)] + \
                  [val(lambda s, j=j: (1 - s[j]) / 2) for j in range(4)]


def in_avail_all(t):
    return response_member(t) or t in avail_all_extra


ok_dual = True; ok_v4 = True
for perm in permutations(range(4)):
    # g acts on s by permuting coordinates; the pullback of an effect f is f o g^{-1} on value vectors at the
    # tangency points: tangency points are permuted the same way
    inv = [perm.index(k) for k in range(4)]
    for cv in CSET:
        t = val(lambda s, cv=cv: ev(cv, s))
        tp = tuple(t[inv[k]] for k in range(4))
        ok_dual = ok_dual and in_avail_all(tp)
    for t in avail_all_extra:
        tp = tuple(t[inv[k]] for k in range(4))
        ok_dual = ok_dual and in_avail_all(tp)
    t_r = avail_all_extra[0]
    ok_v4 = ok_v4 and in_avail_all(tuple(t_r[inv[k]] for k in range(4)))
chk('tet.label_dual', ok_dual, 'enumerate', 'each of the 24 tetrahedral symmetries maps every sampled available effect '
    'to an available effect (pullback = a permutation of the labels): a label dual')
chk('tet.V4', ok_v4, 'enumerate', 'hence every transport of r = 2 p_1 is available: V4 holds for this G (finite, so '
    'neither transitive nor dense on the boundary: consistent with not_boundaryTransitive_of_countable)')

total = sum(N_CHECKS.values())
print('\nsummary: ' + ', '.join('%s %d' % kv for kv in N_CHECKS.items()))
if FAILED:
    print('qa2_towers: FAIL -- %d of %d: %s' % (len(FAILED), total, ', '.join(FAILED)))
    sys.exit(1)
print('qa2_towers: OK -- %d exact checks' % total)
