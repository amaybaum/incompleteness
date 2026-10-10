"""AC probe P2 -- a rational protocol-style tower over the 3/5 rotation pair (a reverse
instance built from the ball: it illustrates mechanisms, it sources nothing).

Stage n: preparation labels are ALL words w over {x, X, z, Z} of length <= n (not reduced), with
point p(w) = W e_z; effect labels are 'unit' and (u-word, sign) for words of length <= n, with
value (1 + sign * p(u) . p(w)) / 2.  One global formula, so SC-infinity holds by construction.

Checks
  T1  every table entry is in [0, 1] and the unit reads 1 (FiniteStage laws at stages 0..3)
  T2  SC-infinity: the stage-n table is the restriction of the stage-(n+1) table (n = 0..2)
  T3  FiniteRank: rank of the stage-3 table [p(e | w)] is 4 (affine dimension 3)
  T4  label dual for each letter a: p(e_{u,s} | a.w) = p(e_{a^-1 u, s} | w), all w, u at stage 2
  T5  AffineRespect of tau_a on stage 3: every affine relation among stage-3 preparation vectors
      (computed as an exact nullspace basis) holds among the images (read on stage-4 effects)
  T6  stage raising: tau_x carries some stage-3 preparation outside the stage-3 preparation vectors
      (so not StagePreserving, CompositionOrder.lean:234)
  T7  quotient mechanism: the label map w -> X.x.w is injective and is not the identity on labels,
      yet prepVec(X.x.w) = prepVec(w) for every w at stage 3 (Undoes holds on the body; the
      reversible group acts on the quotient Prep / prepVec, not on labels)
  T8  infinite order of the induced R_z on the body, finite window: R_z^k p(x) != p(x), k = 1..200
  T9  countercontrol for T5: a non-affine relabelling (swap the labels of two preparations whose
      prepVecs are affinely related to a third) violates a relation
"""
from fractions import Fraction as Fr
from itertools import product

c, s = Fr(3, 5), Fr(4, 5)
I3 = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
Rx = [[Fr(1), Fr(0), Fr(0)], [Fr(0), c, -s], [Fr(0), s, c]]
Rz = [[c, -s, Fr(0)], [s, c, Fr(0)], [Fr(0), Fr(0), Fr(1)]]


def T(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def mv(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))


GEN = {'x': Rx, 'X': T(Rx), 'z': Rz, 'Z': T(Rz)}
INV = {'x': 'X', 'X': 'x', 'z': 'Z', 'Z': 'z'}
EZ = (Fr(0), Fr(0), Fr(1))
_cache = {}


def point(w):
    if w not in _cache:
        v = EZ
        for a in reversed(w):  # rightmost letter acts first
            v = mv(GEN[a], v)
        _cache[w] = v
    return _cache[w]


def words(n):
    out = ['']
    for k in range(1, n + 1):
        out += [''.join(t) for t in product('xXzZ', repeat=k)]
    return out


def effects(n):
    return ['unit'] + [(u, sg) for u in words(n) for sg in (1, -1)]


def val(e, w):
    if e == 'unit':
        return Fr(1)
    u, sg = e
    pu, pw = point(u), point(w)
    return (1 + sg * sum(a * b for a, b in zip(pu, pw))) / 2


def rank(M):
    M = [row[:] for row in M]
    r = 0
    cols = len(M[0]) if M else 0
    for cc in range(cols):
        piv = next((i for i in range(r, len(M)) if M[i][cc] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cc]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][cc] != 0:
                f = M[i][cc]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def nullspace(M):
    """exact right nullspace basis of M (rows x cols)."""
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    pivcols = []
    r = 0
    for cc in range(cols):
        piv = next((i for i in range(r, rows) if M[i][cc] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cc]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][cc] != 0:
                f = M[i][cc]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        pivcols.append(cc)
        r += 1
    free = [cc for cc in range(cols) if cc not in pivcols]
    basis = []
    for fcol in free:
        v = [Fr(0)] * cols
        v[fcol] = Fr(1)
        for i, pc in enumerate(pivcols):
            v[pc] = -M[i][fcol]
        basis.append(v)
    return basis


results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + detail) if detail else ''))


# T1
ok = True
for n in range(4):
    for e in effects(n):
        for w in words(n):
            v = val(e, w)
            ok &= (0 <= v <= 1)
    ok &= all(val('unit', w) == 1 for w in words(n))
check('T1 FiniteStage laws (0 <= p <= 1, unit = 1) at stages 0..3', ok)

# T2: the stage-n table is a sub-table of the stage-(n+1) table (inclusion forward maps)
ok = True
for n in range(3):
    En, Pn = effects(n), words(n)
    En1, Pn1 = set(effects(n + 1)), set(words(n + 1))
    ok &= set(En) <= En1 and set(Pn) <= Pn1
    # values are given by one formula, so consistency is the identity of that formula on the subset
    ok &= all(val(e, w) == val(e, w) for e in En for w in Pn)
check('T2 SC-infinity (inclusion maps, one global table) n = 0..2 [VACUOUS by construction: '
      'label inclusion only; recorded, not evidence]', ok)

# T3
E3, P3 = effects(3), words(3)
tab = [[val(e, w) for e in E3] for w in P3]
rk = rank(tab)
check('T3 FiniteRank: rank of stage-3 table = 4', rk == 4, f'rank = {rk}, |P_3| = {len(P3)}, |E_3| = {len(E3)}')

# T4
E2, P2 = effects(2), words(2)
ok = True
cnt = 0
for a in GEN:
    for w in P2:
        for e in E2:
            if e == 'unit':
                lhs, rhs = val(e, a + w), val(e, w)
            else:
                u, sg = e
                lhs = val((u, sg), a + w)
                rhs = val((INV[a] + u, sg), w)
            ok &= (lhs == rhs)
            cnt += 1
check('T4 label dual p(e_{u,s} | a.w) = p(e_{a^-1 u, s} | w)', ok, f'{cnt} instances')

# T5 AffineRespect on stage 3, images read on stage-4 effects (restricted to the effects needed:
# images a.w have length <= 4; read them on the stage-3 effects plus the dual labels, i.e. all
# stage-4 effects whose u-word has length <= 4).  To keep it exact and cheap, read on E3 (which
# already coordinatises: rank 4) -- a relation holds on the body iff it holds on a coordinatising set.
P3pts = P3
M = [[val(e, w) for w in P3pts] for e in E3]  # columns = preparations
M.append([Fr(1)] * len(P3pts))  # sum c = 0
rels = nullspace(M)
viol = 0
for a in GEN:
    img = [[val(e, a + w) for w in P3pts] for e in E3]
    for r_ in rels:
        if any(sum(row[k] * r_[k] for k in range(len(P3pts))) != 0 for row in img):
            viol += 1
check('T5 AffineRespect of tau_a (all four letters) on every stage-3 affine relation', viol == 0,
      f'{len(rels)} basis relations x 4 letters, {viol} violated')

# T6 stage raising
pts3 = {point(w) for w in P3}
outside = [w for w in P3 if point('x' + w) not in pts3]
check('T6 tau_x not StagePreserving: some stage-3 prep goes outside the stage-3 prepVecs', len(outside) > 0,
      f'{len(outside)} of {len(P3)} preparations leave stage 3')

# T7 quotient mechanism
lab_map = {w: 'Xx' + w for w in P3}
inj = len(set(lab_map.values())) == len(P3)
nonid = all(lab_map[w] != w for w in P3)
same = all(point(lab_map[w]) == point(w) for w in P3)
check('T7 label map w -> X.x.w injective, not the identity on labels, identity on prepVecs',
      inj and nonid and same)

# T8 infinite order, finite window
px = point('x')
v = px
hit = []
for k in range(1, 201):
    v = mv(Rz, v)
    if v == px:
        hit.append(k)
check('T8 R_z^k p(x) != p(x) for k = 1..200', not hit, f'returns at {hit}')

# T9 countercontrol: a relabelling that is not induced by an affine map violates a relation.
# Take three preparations with p(w2) = midpoint-type affine relation and swap one image.
# Use the relation basis: pick a relation with support >= 3 and permute two images of distinct points.
viol_cc = 0
for r_ in rels:
    supp = [k for k in range(len(P3pts)) if r_[k] != 0]
    if len(supp) < 3:
        continue
    k1, k2 = supp[0], supp[1]
    if point(P3pts[k1]) == point(P3pts[k2]):
        continue
    perm = list(range(len(P3pts)))
    perm[k1], perm[k2] = perm[k2], perm[k1]
    rows = [[val(e, P3pts[perm[k]]) for k in range(len(P3pts))] for e in E3]
    if any(sum(row[k] * r_[k] for k in range(len(P3pts))) != 0 for row in rows):
        viol_cc += 1
        break
check('T9 countercontrol: a swap of two images (not affine) violates a relation', viol_cc == 1)

nfail = sum(1 for _, ok_ in results if not ok_)
print(f'SUMMARY {len(results) - nfail}/{len(results)} PASS')
print('VERDICT ' + ('tower-mechanisms-hold' if nfail == 0 else 'NOT RENDERED'))
