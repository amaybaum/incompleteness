# ---- A37: the exact monomial calculus on the arc ---------------------------------------------
# Every entry of SIG is i^p z^q w^r, so every entry of H(u) = SIG o u^W is i^p z^q w^r u^k with k = W(i, j). A Dita
# structure (column blocks, row classes) is admitted at u iff finitely many monomial equations hold: the row
# proportionality on every block and the rank-one condition on the block ratios. Each equation u^k = i^p z^q w^r has,
# for k != 0, exactly |k| unit solutions u = zeta z^(-q/k) w^(-r/k), zeta a root of unity; z = (2+i)/(2-i) and
# w = (3+2i)/(3-2i) are multiplicatively independent modulo roots of unity (distinct Gaussian primes), so the triple
# (angle of zeta in turns mod 1, s, t) with u = zeta z^s w^t names a point exactly, and monomials at a point are
# compared exactly as such triples.
F4E = [[(0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 1), (2, 0), (2, 1)], [(0, 0), (2, 0), (0, 0), (2, 0)], [(0, 0), (2, 1), (2, 0), (0, 1)]]
SIGE = [[None] * 16 for _ in range(16)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                (p1, q), (p2, r) = F4E[a][c], F4E[b][d]
                SIGE[4 * a + b][4 * c + d] = ((p1 + p2) % 4, q, r)
def val(p, q, r):
    out = ONE
    for _ in range(p): out = out * I_
    for _ in range(q): out = out * z
    for _ in range(r): out = out * w
    return out
WE = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
GEN_ONE = (0, 0, 0, 0)
def gen_entry(i, j): p, q, r = SIGE[i][j]; return (WE[i][j], p, q, r)
def gen_div(m1, m2): return (m1[0] - m2[0], (m1[1] - m2[1]) % 4, m1[2] - m2[2], m1[3] - m2[3])
def gen_mul(m1, m2): return (m1[0] + m2[0], (m1[1] + m2[1]) % 4, m1[2] + m2[2], m1[3] + m2[3])
def solutions(m):
    """the unit solutions of u^k i^p z^q w^r = 1 as canonical points, or 'all' / 'none'"""
    k, p, q, r = m
    if k == 0: return 'all' if (p % 4 == 0 and q == 0 and r == 0) else 'none'
    return frozenset(((Fr(-p, 4) + n_) / k % 1, Fr(-q, k), Fr(-r, k)) for n_ in range(abs(k)))
def at_point(m, pt):
    k, p, q, r = m; ang, s, t = pt
    return ((Fr(p, 4) + k * ang) % 1, q + k * s, r + k * t)
PT_ONE = (Fr(0), Fr(0), Fr(0))
def show_pt(pt): return 'zeta(%s) z^%s w^%s' % (pt[0], pt[1], pt[2])
def gaussian_value(pt):
    """the Gaussian-rational value of a canonical point, when it has one: integer s, t and an angle in quarter turns"""
    ang, s, t = pt
    if s.denominator != 1 or t.denominator != 1 or (ang * 4).denominator != 1: return None
    v = ONE
    for _ in range(int(ang * 4) % 4): v = v * I_
    zz = z if s >= 0 else z.conj(); ww = w if t >= 0 else w.conj()
    for _ in range(abs(int(s))): v = v * zz
    for _ in range(abs(int(t))): v = v * ww
    return v

def structures(ent, div, mul, is_one, m, n, ratio):
    """the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials: ent(i, j) the entry, ratio[i][s0][s]
    = ent(i, s) / ent(i, s0) precomputed, div/mul/is_one the monomial operations; returns (candidates, exact) as lists of
    (column blocks, row classes); unitarity of the factors is not tested here (it follows from that of H(u)) and is
    checked separately by the numeric control"""
    good = {}
    for S in itertools.combinations(range(16), n):
        keys = {}
        for i in range(16):
            r0 = ratio[i][S[0]]
            keys.setdefault(tuple(r0[s] for s in S), []).append(i)
        Pp = sorted(tuple(v) for v in keys.values())
        if all(len(cl) == m for cl in Pp): good[S] = Pp
    parts = []
    def rec(rem, chosen):
        if not rem: parts.append(tuple(chosen)); return
        first = min(rem)
        for S in good:
            if first in S and set(S) <= rem: rec(rem - set(S), chosen + [S])
    rec(set(range(16)), [])
    cands, exact = [], []
    for cp in parts:
        cls = {i: tuple(next(ci for ci, cl in enumerate(good[S]) if i in cl) for S in cp) for i in range(16)}
        groups = {}
        for i in range(16): groups.setdefault(cls[i], []).append(i)
        rows = sorted(tuple(v) for v in groups.values())
        if not all(len(g) == m for g in rows): continue
        cands.append((cp, rows))
        col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
        lam = {(a, b, c): div(ent(row[(a, b)], col[(c, 0)]), ent(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
        if all(is_one(div(lam[(a, b, c)], mul(lam[(a, 0, c)], lam[(0, b, c)]))) for a in range(m) for b in range(n) for c in range(m)):
            exact.append((cp, rows))
    return cands, exact
def gen_search(m, n):
    ratio = [[[gen_div(gen_entry(i, s), gen_entry(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(gen_entry, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
def point_search(pt, m, n):
    ent = [[at_point(gen_entry(i, j), pt) for j in range(16)] for i in range(16)]
    def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
    def mul3(a, b): return ((a[0] + b[0]) % 1, a[1] + b[1], a[2] + b[2])
    ratio = [[[div3(ent[i][s], ent[i][s0]) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(lambda i, j: ent[i][j], div3, mul3, lambda x: x == PT_ONE, m, n, ratio)
SHAPES = ((4, 4), (8, 2), (2, 8))
FROZEN_BLOCKS = ((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15))
FROZEN_CLASSES = ((0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15))
def exact_set(res):
    """the exact structures of a search result over the three shapes, as a set of (shape, blocks, classes)"""
    return set((mn, cp, tuple(rows)) for mn, (cands, exact) in res.items() for cp, rows in exact)
FROZEN_ONLY = {((2, 8), FROZEN_BLOCKS, FROZEN_CLASSES)}

print('== 1. the census: every Diţă structure of the stratum point, and its classes modulo the stabilizer ==')
check('symbolic SIG equals the numeric SIG entrywise (i^p z^q w^r)', all(val(*SIGE[i][j]) == SIG[i][j] for i in range(16) for j in range(16)), True)
check('SIG is symmetric; W is symmetric', (SIG == [list(c) for c in zip(*SIG)], WE == [list(c) for c in zip(*WE)]), (True, True))
SIGT = [list(c) for c in zip(*SIG)]
def twist(H, cp, rows, X, Y, m, n):
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    D = [[None] * n for _ in range(m)]
    for c in range(m):
        for b in range(n):
            x = X[0][c] * Y[c][b][0]; h = H[row[(0, b)]][col[(c, 0)]]; nx = x.norm2(); q = h * x.conj(); D[c][b] = G(q.a / nx, q.b / nx)
    ok = all(H[row[(a, b)]][col[(c, d)]] == X[a][c] * D[c][b] * Y[c][b][d] for a in range(m) for b in range(n) for c in range(m) for d in range(n))
    return D, ok
facts = []
for (m, n) in SHAPES:
    for kind, H in (('column', SIG), ('row', SIGT)):
        for cp, rows, ok, X, Y in dita_orientations(H, m, n):
            if not ok: continue
            D, dok = twist(H, cp, rows, X, Y, m, n)
            facts.append((kind, (m, n), tuple(cp), tuple(rows), dok, all(x == ONE for r in D for x in r)))
check('exact structures of SIG by shape and form: 4x4, 8x2, 2x8, each column and row', tuple(sum(1 for f in facts if f[1] == mn and f[0] == k) for mn in SHAPES for k in ('column', 'row')), (4, 4, 2, 2, 3, 3))
check('every structure reconstructs SIG exactly from its factors, with trivial twist', all(f[4] and f[5] for f in facts), True)
check('the column-form and row-form structures coincide as index sets (SIG symmetric)', sorted((mn, cp, rows) for k, mn, cp, rows, _, _ in facts if k == 'column') == sorted((mn, cp, rows) for k, mn, cp, rows, _, _ in facts if k == 'row'), True)
def perm_pair(e):
    p, s_ = e
    rp = [p[i * 16] // 16 for i in range(16)]; cq = [p[j] % 16 for j in range(16)]
    if all(p[i * 16 + j] == rp[i] * 16 + cq[j] for i in range(16) for j in range(16)): return 'product', tuple(rp), tuple(cq)
    psi = [p[i * 16] % 16 for i in range(16)]; phi = [p[j] // 16 for j in range(16)]
    assert all(p[i * 16 + j] == phi[j] * 16 + psi[i] for i in range(16) for j in range(16))
    return 'transposed', tuple(psi), tuple(phi)
def canon(kind, mn, cp, rows):
    return (kind, mn, tuple(sorted(tuple(sorted(b)) for b in cp)), tuple(sorted(tuple(sorted(r)) for r in rows)))
def transport(kind, mn, cp, rows, e):
    """a structure carried through a stabilizer element: a product element sends entry (i, j) to (rp i, cq j), a transposed
    one to (phi j, psi i) and exchanges the column and row forms"""
    form, f1, f2 = perm_pair(e)
    if form == 'product':
        rp, cq = f1, f2
        if kind == 'column': return canon('column', mn, [[cq[j] for j in b] for b in cp], [[rp[i] for i in r] for r in rows])
        return canon('row', mn, [[rp[i] for i in b] for b in cp], [[cq[j] for j in r] for r in rows])
    psi, phi = f1, f2
    if kind == 'column': return canon('row', mn, [[phi[j] for j in b] for b in cp], [[psi[i] for i in r] for r in rows])
    return canon('column', mn, [[psi[i] for i in b] for b in cp], [[phi[j] for j in r] for r in rows])
keyset = {canon(k, mn, cp, rows): idx for idx, (k, mn, cp, rows, _, _) in enumerate(facts)}
orbits = []; seen = set()
for idx, (k, mn, cp, rows, _, _) in enumerate(facts):
    if idx in seen: continue
    orb = set(keyset[transport(k, mn, cp, rows, e)] for e in elems); seen |= orb; orbits.append(sorted(orb))
check('the stabilizer (order 1024, with transposition) permutes the 18 structures; orbit count and sizes', (len(orbits), sorted(len(o) for o in orbits)), (9, [2] * 9))
check('each orbit pairs a structure with its own transpose and identifies nothing else', all(len(set(facts[i][1:4] for i in o)) == 1 and set(facts[i][0] for i in o) == {'column', 'row'} for o in orbits), True)
fro = [i for i, f in enumerate(facts) if f[1] == (2, 8) and f[2] == FROZEN_BLOCKS and f[3] == FROZEN_CLASSES]
check('the frozen 2x8 class is one orbit: column and row forms of the frozen blocks and classes', sorted(fro) in orbits, True)
OTHERS = sorted(set((f[1], f[2], f[3]) for f in facts if f[0] == 'column' and not (f[1] == (2, 8) and f[2] == FROZEN_BLOCKS)), key=lambda x: (SHAPES.index(x[0]), x[1]))
check('the other classes: four 4x4, two 8x2, two 2x8', [mn for mn, _, _ in OTHERS], [(4, 4)] * 4 + [(8, 2)] * 2 + [(2, 8)] * 2)
print('  (%.0fs)' % (time.time() - t0))

print('== 2. the arc: symmetric, and the frozen class persistent; the named point and the second point ==')
U5 = G(Fr(3, 5), Fr(4, 5))
def Pu(u): return [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
P5 = Pu(U5)
check('Pu(1) = SIG; P = Pu(u60); both P and Pu(u5) unitary and symmetric', (Pu(ONE) == SIG, Pu(U60) == P, is_unitary16(P), is_unitary16(P5), P == [list(c) for c in zip(*P)], P5 == [list(c) for c in zip(*P5)]), (True, True, True, True, True, True))
def numeric_exact(H):
    return {mn: [(tuple(cp), tuple(rows)) for cp, rows, ok, X, Y in dita_orientations(H, *mn) if ok] for mn in SHAPES}
NE_P, NE_P5 = numeric_exact(P), numeric_exact(P5)
check('P admits exactly the frozen class (column form; the row form is the same by symmetry)', NE_P, {(4, 4): [], (8, 2): [], (2, 8): [(FROZEN_BLOCKS, FROZEN_CLASSES)]})
check('Pu(u5) admits exactly the frozen class', NE_P5, {(4, 4): [], (8, 2): [], (2, 8): [(FROZEN_BLOCKS, FROZEN_CLASSES)]})
print('  (%.0fs)' % (time.time() - t0))

print('== 3. the generic arc point, and the obstruction monomial of each other class ==')
gen = {mn: gen_search(*mn) for mn in SHAPES}
check('structures at a generic u (u a free symbol): (candidates, exact) by shape', tuple((len(c), len(e)) for c, e in gen.values()), ((1, 0), (1, 0), (1, 1)))
check('the one exact generic structure is the frozen 2x8 class', exact_set(gen), FROZEN_ONLY)
def conditions(m, n, cp, rows):
    """every monomial condition the structure imposes: (kind, positions, monomial); 'prop' rows (a,b),(0,b) on columns
    (c,d),(c,0); 'rank1' the rank-one identity at (a, b, c)"""
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    out = []
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    out.append(('prop', (i, i2, j, j0), gen_div(gen_div(gen_entry(i, j), gen_entry(i2, j)), gen_div(gen_entry(i, j0), gen_entry(i2, j0)))))
    lam = {(a, b, c): gen_div(gen_entry(row[(a, b)], col[(c, 0)]), gen_entry(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                out.append(('rank1', (a, b, c), gen_div(lam[(a, b, c)], gen_mul(lam[(a, 0, c)], lam[(0, b, c)]))))
    return out
obs = []
for mn, cp, rows in OTHERS:
    nonid = [x for x in conditions(mn[0], mn[1], cp, rows) if x[2] != GEN_ONE]
    obs.append((len(nonid), sorted(set(x[2][0] for x in nonid)), sorted(set(x[2][1:] for x in nonid))))
check('each other class imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}', all(nn > 0 and set(ks) <= {-1, 1} and cs == [(0, 0, 0)] for nn, ks, cs in obs), True)
check('their counts of non-identity conditions', [nn for nn, _, _ in obs], [20, 4, 36, 24, 40, 8, 20, 20])
check('the frozen class imposes no non-identity condition (persistence, replayed)', sum(1 for x in conditions(2, 8, FROZEN_BLOCKS, FROZEN_CLASSES) if x[2] != GEN_ONE), 0)
# the kernel's witness identities: four positions with H p1 H p2 = H p3 H p4 forced by the Dita form, all four SIG
# entries in {1, -1} and u-exponent sums {0, 1}
WIT = @@WITNESSES@@
def witness_ok(mn, cp, rows, wit):
    m, n = mn; col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    p1, p2, p3, p4 = [tuple(x) for x in wit['p']]
    # the identity is forced: same class/block pairing (prop) or the rank-one quadruple (rank1)
    rc = {v: k for k, v in row.items()}; cc = {v: k for k, v in col.items()}
    if wit['kind'] == 'prop':
        forced = rc[p1[0]][1] == rc[p2[0]][1] == rc[p3[0]][1] == rc[p4[0]][1] and cc[p1[1]][0] == cc[p2[1]][0] == cc[p3[1]][0] == cc[p4[1]][0] and p3 == (p1[0], p2[1]) and p4 == (p2[0], p1[1])
    else:
        (a, b), (a0, b0) = rc[p1[0]], rc[p2[0]]
        forced = a0 == 0 and b0 == 0 and rc[p3[0]] == (a, 0) and rc[p4[0]] == (0, b) and p1[1] == p2[1] == p3[1] == p4[1] and cc[p1[1]][1] == 0
    rational = all(SIGE[i][j][1] == 0 and SIGE[i][j][2] == 0 and SIGE[i][j][0] % 2 == 0 for i, j in (p1, p2, p3, p4))
    sgn = lambda i, j: 1 if SIGE[i][j][0] == 0 else -1
    e1 = WE[p1[0]][p1[1]] + WE[p2[0]][p2[1]]; e2 = WE[p3[0]][p3[1]] + WE[p4[0]][p4[1]]
    return forced and rational and sgn(*p1) * sgn(*p2) == sgn(*p3) * sgn(*p4) and {e1, e2} == {0, 1} and [e1, e2] == wit['e']
check('the kernel witness identity of each other class is forced by its Diţă form, has rational entries and exponent sums {0, 1}', all(witness_ok(mn, cp, rows, WIT[nm]) for (mn, cp, rows), nm in zip(OTHERS, ('k1', 'k2', 'k3', 'k4', 'e1', 'e2', 't2', 't3'))), True)
print('  (%.0fs)' % (time.time() - t0))

print('== 4. the candidate exceptional set: every point where an extra proportionality or the rank-one condition of a generic candidate appears ==')
def cond(i, i2, j, j0): return gen_div(gen_div(gen_entry(i, j), gen_entry(i2, j)), gen_div(gen_entry(i, j0), gen_entry(i2, j0)))
E_cand = {}
for n in (4, 2, 8):
    for B in itertools.combinations(range(16), n):
        j0 = B[0]
        for i, i2 in itertools.combinations(range(16), 2):
            sets = None; generic = True
            for j in B[1:]:
                s_ = solutions(cond(i, i2, j, j0))
                if s_ == 'all': continue
                generic = False
                if s_ == 'none': sets = frozenset(); break
                sets = s_ if sets is None else (sets & s_)
                if not sets: break
            if not generic and sets:
                for pt in sets: E_cand[pt] = E_cand.get(pt, 0) + 1
def rank1_points(m, n, cp, rows):
    pts = None
    for kind, idx, mm in conditions(m, n, cp, rows):
        if kind != 'rank1': continue
        s_ = solutions(mm)
        if s_ == 'all': continue
        if s_ == 'none': return frozenset()
        pts = s_ if pts is None else pts & s_
    return pts if pts is not None else 'all'
E_rank = set()
for mn, (cands, exact) in gen.items():
    for cp, rows in cands:
        if (cp, rows) in exact: continue
        pts = rank1_points(mn[0], mn[1], cp, rows)
        E_rank |= set(pts)
E_all = sorted(set(E_cand) | E_rank, key=lambda p: (p[1], p[2], p[0]))
check('the generic 4x4 and 8x2 candidates satisfy the rank-one condition at u = 1 only', E_rank, {PT_ONE})
EXPECTED_E = @@E_CAND@@
check('the candidate exceptional set, exactly (twenty points)', [show_pt(p) for p in E_all], EXPECTED_E)
check('twelve of the candidates are Gaussian rational, eight are square roots outside Q(i)', sum(1 for p in E_all if gaussian_value(p) is not None), 12)
print('  (%.0fs)' % (time.time() - t0))

print('== 5. the exhaustive search at every candidate point: the exact exceptional set ==')
sym = {}
for pt in E_all:
    sym[pt] = {mn: point_search(pt, *mn) for mn in SHAPES}
exact_E = [pt for pt in E_all if exact_set(sym[pt]) != FROZEN_ONLY]
check('at u = 1 the search returns the eighteen structures: (candidates, exact) by shape', tuple((len(c), len(e)) for c, e in sym[PT_ONE].values()), ((5, 4), (3, 2), (3, 3)))
check('at u = -1 the proportionality candidates are those of u = 1, but only the frozen class is exact', (tuple((len(c), len(e)) for c, e in sym[(Fr(1, 2), Fr(0), Fr(0))].values()), exact_set(sym[(Fr(1, 2), Fr(0), Fr(0))]) == FROZEN_ONLY), (((5, 0), (3, 0), (3, 1)), True))
check('at every candidate point other than u = 1, exactly the frozen class is admitted', [show_pt(p) for p in exact_E], ['zeta(0) z^0 w^0'])
check('THE EXACT EXCEPTIONAL SET IS {1}: outside the candidates the structure is the generic one, at the candidates the search decides', exact_E, [PT_ONE])
print('  (%.0fs)' % (time.time() - t0))

print('== 6. controls ==')
agree = []
for pt in E_all:
    uv = gaussian_value(pt)
    if uv is None: continue
    Hu = Pu(uv)
    if not is_unitary16(Hu): agree.append((show_pt(pt), 'not unitary')); continue
    num = {mn: (len(o), sum(1 for x in o if x[2])) for mn in SHAPES for o in [dita_orientations(Hu, *mn)]}
    if any(num[mn] != (len(sym[pt][mn][0]), len(sym[pt][mn][1])) for mn in SHAPES): agree.append((show_pt(pt), num))
check('the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates', agree, [])
# genuine deformations: each other class, with one twist phase moved off 1, is a point of that class's hull off SIG
def hull_point(mn, cp, rows, phase):
    m, n = mn
    for f in facts:
        if f[0] == 'column' and f[1] == mn and f[2] == cp and f[3] == rows: break
    for cp_, rows_, ok, X, Y in dita_orientations(SIG, m, n):
        if ok and tuple(cp_) == cp and tuple(rows_) == rows: break
    D = [[ONE] * n for _ in range(m)]; D[m - 1][n - 1] = phase
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    H = [[None] * 16 for _ in range(16)]
    for a in range(m):
        for b in range(n):
            for c in range(m):
                for d in range(n): H[row[(a, b)]][col[(c, d)]] = X[a][c] * D[c][b] * Y[c][b][d]
    return H
deform = []
for mn, cp, rows in OTHERS:
    H = hull_point(mn, cp, rows, U5)
    found = [(tuple(cp_), tuple(rows_)) for cp_, rows_, ok, X, Y in dita_orientations(H, *mn) if ok]
    deform.append((is_unitary16(H), H != SIG, (cp, rows) in found))
check('a genuine deformation inside each other class (one twist phase u5): unitary, off SIG, and found by the search in its own class', deform, [(True, True, True)] * 8)
check('the row-form search on P^T = P returns the column-form result (transpose invariance)', numeric_exact([list(c) for c in zip(*P)]) == NE_P, True)
# equivalence invariance: transport P by three stabilizer elements and compare the search with the transported structure
def apply_matrix(e, H):
    p, s_ = e; out = [[None] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            i2, j2 = divmod(p[i * 16 + j], 16); out[i2][j2] = H[i][j] if s_ == 1 else H[i][j].conj()
    return out
picks = [elems[k] for k in (1, len(elems) // 3, len(elems) - 1)]
equiv = []
for e in picks:
    HP = apply_matrix(e, P); found = numeric_exact(HP)
    want = transport('column', (2, 8), FROZEN_BLOCKS, FROZEN_CLASSES, e)
    got = set(canon('column', mn, cp, rows) for mn, lst in found.items() for cp, rows in lst)
    # a transposed element sends the column form to the row form of the image, whose column-form search sees the same index sets
    equiv.append((len(got), canon('column', want[1], want[2], want[3]) in got))
check('the membership classifier commutes with three stabilizer elements (product, transposed, conjugating): the transported frozen class is the one structure found', equiv, [(1, True)] * 3)
# a deliberately perturbed index map: the frozen blocks with one column moved between blocks are not admitted at generic u nor at P
pb = ((0, 1, 2, 3, 8, 9, 10, 12), (4, 5, 6, 7, 11, 13, 14, 15))
def admitted_generic(m, n, cp, rows): return all(x[2] == GEN_ONE for x in conditions(m, n, cp, rows))
check('a perturbed index map (columns 11 and 12 exchanged between the frozen blocks) is admitted neither at generic u nor at P', (admitted_generic(2, 8, pb, FROZEN_CLASSES), (pb, FROZEN_CLASSES) in NE_P[(2, 8)]), (False, False))
check('the frozen index maps themselves are admitted at generic u (control of the control)', admitted_generic(2, 8, FROZEN_BLOCKS, FROZEN_CLASSES), True)
print('  (%.0fs)' % (time.time() - t0))

print()
if fails:
    print('dita_arc_exclusivity_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG the eighteen Diţă structures form nine classes modulo the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 class persists identically, each of the eight other classes is admitted only where u = 1, the candidate exceptional set of the monomial calculus has twenty points, and the exhaustive search at each of them finds only the frozen class away from u = 1: the exact exceptional set is {1}')
