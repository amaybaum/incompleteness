# ---- A38: the witness exponent matrix and its arc ---------------------------------------------
# The exponent matrix E = A + B + C on the entry ((a,b),(c,d)), rows i = 4a+b and columns j = 4c+d:
#   A = [a odd][b = 3][c odd],  B = [a = 2][d = 1],  C = [a+b odd][(c,d) in {(0,2),(2,0)}]
# and the arc H(u) = SIG o u^E. Every entry of H(u) is i^p z^q w^r u^k with k = E(i, j) in {0, 1}; the monomial calculus
# of act 37 applies verbatim with E in place of W.
def EA(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a % 2 == 1 and b == 3 and c % 2 == 1) else 0
def EB(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a == 2 and d == 1) else 0
def EC(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if ((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))) else 0
EE = [[EA(i, j) + EB(i, j) + EC(i, j) for j in range(16)] for i in range(16)]
EW = @@E_TABLE@@
ET = [list(c) for c in zip(*EE)]
SIGT = [list(c) for c in zip(*SIG)]
def Hu(u, E=EE): return [[SIG[i][j] * gpow(u, E[i][j]) for j in range(16)] for i in range(16)]
def ent_of(E):
    def ent(i, j): p, q, r = SIGE[i][j]; return (E[i][j], p, q, r)
    return ent
def gen_search_E(E, m, n):
    ent = ent_of(E)
    ratio = [[[gen_div(ent(i, s), ent(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(ent, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
def point_search_E(E, pt, m, n):
    ent0 = ent_of(E)
    ent = [[at_point(ent0(i, j), pt) for j in range(16)] for i in range(16)]
    def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
    def mul3(a, b): return ((a[0] + b[0]) % 1, a[1] + b[1], a[2] + b[2])
    return structures(lambda i, j: ent[i][j], div3, mul3, lambda x: x == PT_ONE, m, n, ratio=[[[div3(ent[i][s], ent[i][s0]) for s in range(16)] for s0 in range(16)] for i in range(16)]), ent
def relaxed_at_point(ent, m, n, cp, rows):
    """the diagonal-equivalence form of a proportionality candidate at a point: lambda(a,b,c)/lambda(a,0,c) independent of c"""
    def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    lam = {(a, b, c): div3(ent[row[(a, b)]][col[(c, 0)]], ent[row[(0, b)]][col[(c, 0)]]) for a in range(m) for b in range(n) for c in range(m)}
    return all(div3(lam[(a, b, c)], lam[(a, 0, c)]) == div3(lam[(a, b, 0)], lam[(a, 0, 0)]) for a in range(m) for b in range(n) for c in range(m))
def level_sets(v):
    out = {}
    for k, x in enumerate(v): out.setdefault(x, []).append(k)
    return out

print('== 1. realizability: the arc is a complex Hadamard family through SIG ==')
check('symbolic SIG equals the numeric SIG entrywise (i^p z^q w^r)', all(val(*SIGE[i][j]) == SIG[i][j] for i in range(16) for j in range(16)), True)
check('E = A + B + C equals the frozen table; entries in {0, 1}; the three pieces are disjoint', (EE == EW, set(x for r in EE for x in r) == {0, 1}, all(EA(i, j) + EB(i, j) + EC(i, j) <= 1 for i in range(16) for j in range(16))), (True, True, True))
check('supports of A, B, C and E', (sum(EA(i, j) for i in range(16) for j in range(16)), sum(EB(i, j) for i in range(16) for j in range(16)), sum(EC(i, j) for i in range(16) for j in range(16)), sum(x for r in EE for x in r)), (16, 16, 16, 48))
gn = [[EE[i][j] - EE[i][0] - EE[0][j] + EE[0][0] for j in range(16)] for i in range(16)]
check('E is not a row-and-column shift (its gauge normal form is not zero): the arc is not a diagonal rephasing of SIG', any(x for r in gn for x in r), True)
nlev = 0; bad = []; balanced = True
for i in range(16):
    for i2 in range(i + 1, 16):
        for d, ks in level_sets([EE[i][k] - EE[i2][k] for k in range(16)]).items():
            nlev += 1
            s = ZERO
            for k in ks: s = s + SIG[i][k] * SIG[i2][k].conj()
            if s != ZERO: bad.append((i, i2, d))
            cnt = {}
            for k in ks:
                a1, q1, r1 = SIGE[i][k]; a2, q2, r2 = SIGE[i2][k]
                cnt[(q1 - q2, r1 - r2)] = cnt.get((q1 - q2, r1 - r2), 0) + (1 if (a1 - a2) % 4 == 0 else -1)
            if any(cnt.values()): balanced = False
check('the Laurent identity H(u) H(u)^* = 16 I: every level set of every row-pair difference has vanishing pair sum (exact)', bad, [])
check('the number of level sets over the 120 row pairs, and the differences taken', (nlev, sorted(set(EE[i][k] - EE[i2][k] for i in range(16) for i2 in range(16) for k in range(16)))), (@@NLEV@@, [-1, 0, 1]))
check('every level-set sum vanishes monomial by monomial: the identity holds with z and w symbolic units, as the kernel states it', balanced, True)
U5 = G(Fr(3, 5), Fr(4, 5)); MINUS = G(-1); IU = I_
check('H(1) = SIG; H(u) unitary at u = u5, u60, -1 and i', (Hu(ONE) == SIG, is_unitary16(Hu(U5)), is_unitary16(Hu(U60)), is_unitary16(Hu(MINUS)), is_unitary16(Hu(IU))), (True, True, True, True, True))
check('H(u5) differs from SIG in exactly the 48 support entries, each by the unit u5', sum(1 for i in range(16) for j in range(16) if Hu(U5)[i][j] != SIG[i][j]), 48)
print('  (%.0fs)' % (time.time() - t0))

print('== 2. class exclusions: the eighteen census structures, each admitted only at u = 1 ==')
CLASSES = [(nm, m, n, tuple(tuple(b) for b in cp), tuple(tuple(r) for r in rows)) for nm, m, n, cp, rows in @@CLASSES@@]
NAMES = [c[0] for c in CLASSES]
cen = {}
for (m, n) in SHAPES:
    for cp, rows, ok, X, Y in dita_orientations(SIG, m, n):
        if ok: cen[(tuple(cp), tuple(rows))] = (m, n)
check("act 37's census replayed: the nine column-form structures of SIG are exactly the frozen classes' index sets", sorted(cen), sorted((cp, rows) for nm, m, n, cp, rows in CLASSES))
check('the row-form structures are the same index sets (SIG symmetric)', sorted((tuple(cp), tuple(rows)) for (m, n) in SHAPES for cp, rows, ok, X, Y in dita_orientations(SIGT, m, n) if ok), sorted(cen))
def conditions_E(E, m, n, cp, rows, transpose):
    ent0 = ent_of(E); ent = (lambda i, j: ent0(j, i)) if transpose else ent0
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    out = []
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    out.append(('prop', (i, i2, j, j0), gen_div(gen_div(ent(i, j), ent(i2, j)), gen_div(ent(i, j0), ent(i2, j0)))))
    lam = {(a, b, c): gen_div(ent(row[(a, b)], col[(c, 0)]), ent(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                out.append(('rank1', (a, b, c), gen_div(lam[(a, b, c)], gen_mul(lam[(a, 0, c)], lam[(0, b, c)]))))
    return out
def admitted_points(conds):
    pts = None
    for kind, idx, mm in conds:
        s_ = solutions(mm)
        if s_ == 'all': continue
        if s_ == 'none': return frozenset()
        pts = s_ if pts is None else pts & s_
    return 'all' if pts is None else pts
obs = {}
for nm, m, n, cp, rows in CLASSES:
    for tr in (False, True):
        conds = conditions_E(EE, m, n, cp, rows, tr)
        nonid = [x for x in conds if x[2] != GEN_ONE]
        obs[(nm, 'row' if tr else 'column')] = (len(nonid), sorted(set(x[2][0] for x in nonid)), sorted(set(x[2][1:] for x in nonid)), admitted_points(conds))
check('each of the eighteen structures imposes non-identity conditions, all of the form u^k = 1 with trivial constant part', all(v[0] > 0 and v[2] == [(0, 0, 0)] for v in obs.values()), True)
check('their exponents k lie in {-2, -1, 1, 2}, and the counts of non-identity conditions by structure', (all(set(v[1]) <= {-2, -1, 1, 2} for v in obs.values()), [obs[(nm, f)][0] for nm in NAMES for f in ('column', 'row')]), (True, @@NONID@@))
check('each structure is admitted at u = 1 alone (the intersection of its condition solution sets)', all(v[3] == frozenset([PT_ONE]) for v in obs.values()), True)
WIT = @@WITNESSES@@
def witness_ok(nm, m, n, cp, rows, tr, w):
    """the four-position identity H p1 H p2 = H p3 H p4 is forced by the structure's Dita form: a proportionality witness pairs
    two rows of one class with two columns of one block; a rectangle witness pairs rows (a,b),(a',b') against (a,b'),(a',b) in one
    column; in the row form the roles of rows and columns are exchanged"""
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    rc = {v: k for k, v in row.items()}; cc = {v: k for k, v in col.items()}
    P = [tuple(x) for x in w['p']]
    if tr: P = [(j, i) for i, j in P]
    p1, p2, p3, p4 = P
    if w['kind'] == 'prop':
        forced = rc[p1[0]][1] == rc[p2[0]][1] and cc[p1[1]][0] == cc[p2[1]][0] and p3 == (p1[0], p2[1]) and p4 == (p2[0], p1[1])
    else:
        (a, b), (a2, b2) = rc[p1[0]], rc[p2[0]]
        forced = a != a2 and b != b2 and rc[p3[0]] == (a, b2) and rc[p4[0]] == (a2, b) and p1[1] == p2[1] == p3[1] == p4[1]
    PH = [tuple(x) for x in w['p']]
    ent = ent_of(EE)
    l = gen_mul(ent(*PH[0]), ent(*PH[1])); r = gen_mul(ent(*PH[2]), ent(*PH[3]))
    rational = all(SIGE[i][j][1] == 0 and SIGE[i][j][2] == 0 and SIGE[i][j][0] % 2 == 0 for i, j in PH)
    return forced and l[1:] == r[1:] and [l[0], r[0]] == w['e'] and abs(l[0] - r[0]) == 1 and rational == w['rational'] and (not rational or (l[1] == 0 and l[2] == 0 and l[3] == 0)) and (rational or list(l[1:]) == w['monomial'])
check('the kernel witness identity of every structure is forced by its Diţă form, has the frozen exponent sums differing by one, and rational constants for seventeen of the eighteen', all(witness_ok(nm, m, n, cp, rows, tr, WIT[nm + ('_row' if tr else '_col')]) for nm, m, n, cp, rows in CLASSES for tr in (False, True)), True)
check("the one non-rational witness, class t2 in the column form, reads (z/16) u = z/16", (WIT['t2_col']['rational'], WIT['t2_col']['monomial'], WIT['t2_col']['e']), (False, [0, 1, 0], [1, 0]))
print('  (%.0fs)' % (time.time() - t0))

print('== 3. all-index exhaustion: at a generic u no index maps whatever pass the proportionality test ==')
gen = {(form, mn): gen_search_E(E, *mn) for form, E in (('column', EE), ('row', ET)) for mn in SHAPES}
check('structures at a generic u (u a free symbol), (candidates, exact) by form and shape', {k: (len(c), len(e)) for k, (c, e) in gen.items()}, {(f, mn): (0, 0) for f in ('column', 'row') for mn in SHAPES})
print('  (%.0fs)' % (time.time() - t0))

print('== 4. the exceptional set: every point at which any structure could appear, decided by the exhaustive search ==')
def cond_E(ent, i, i2, j, j0): return gen_div(gen_div(ent(i, j), ent(i2, j)), gen_div(ent(i, j0), ent(i2, j0)))
E_cand = {}
for form, E in (('column', EE), ('row', ET)):
    ent = ent_of(E)
    for n in (4, 2, 8):
        for Bk in itertools.combinations(range(16), n):
            j0 = Bk[0]
            for i, i2 in itertools.combinations(range(16), 2):
                sets = None; generic = True
                for j in Bk[1:]:
                    s_ = solutions(cond_E(ent, i, i2, j, j0))
                    if s_ == 'all': continue
                    generic = False
                    if s_ == 'none': sets = frozenset(); break
                    sets = s_ if sets is None else (sets & s_)
                    if not sets: break
                if not generic and sets:
                    for pt in sets: E_cand[pt] = E_cand.get(pt, 0) + 1
E_all = sorted(E_cand, key=lambda p: (p[1], p[2], p[0]))
EXPECTED_E = @@E_CAND@@
check('the candidate exceptional set, exactly (forty points), both forms together', [show_pt(p) for p in E_all], EXPECTED_E)
check('twenty of the candidates are Gaussian rational, twenty are square roots outside Q(i)', sum(1 for p in E_all if gaussian_value(p) is not None), 20)
print('  (%.0fs)' % (time.time() - t0))
sym = {}; relaxed = {}
for pt in E_all:
    for form, E in (('column', EE), ('row', ET)):
        for mn in SHAPES:
            (c_, x_), ent = point_search_E(E, pt, *mn)
            sym[(pt, form, mn)] = (c_, x_)
            relaxed[(pt, form, mn)] = [(cp, rows) for cp, rows in c_ if relaxed_at_point(ent, mn[0], mn[1], cp, rows)]
def exact_at(pt): return {(f, mn): (len(sym[(pt, f, mn)][0]), len(sym[(pt, f, mn)][1])) for f in ('column', 'row') for mn in SHAPES}
exact_E = [pt for pt in E_all if any(sym[(pt, f, mn)][1] for f in ('column', 'row') for mn in SHAPES)]
relaxed_E = [pt for pt in E_all if any(relaxed[(pt, f, mn)] for f in ('column', 'row') for mn in SHAPES)]
PT_MINUS = (Fr(1, 2), Fr(0), Fr(0))
check('at u = 1 the search returns the eighteen structures: (candidates, exact) by form and shape', exact_at(PT_ONE), {(f, mn): v for f in ('column', 'row') for mn, v in zip(SHAPES, ((5, 4), (3, 2), (3, 3)))})
check('at u = -1 exactly one 2x8 structure per form is admitted: (candidates, exact) by form and shape', exact_at(PT_MINUS), {(f, mn): v for f in ('column', 'row') for mn, v in zip(SHAPES, ((1, 0), (1, 0), (1, 1)))})
M_COL = (((0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)), ((0, 2), (1, 3), (4, 6), (5, 15), (7, 13), (8, 10), (9, 11), (12, 14)))
M_ROW = (((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)), ((0, 2), (1, 9), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 10)))
check('the two structures at u = -1: index maps outside the census, blocks by column parity in the column form', ([(tuple(cp), tuple(rows)) for cp, rows in sym[(PT_MINUS, 'column', (2, 8))][1]], [(tuple(cp), tuple(rows)) for cp, rows in sym[(PT_MINUS, 'row', (2, 8))][1]], M_COL in cen or M_ROW in cen), ([M_COL], [M_ROW], False))
check('THE EXACT EXCEPTIONAL SET IS {1, -1}: the units at which some index maps admit a Diţă form of H(u) in some orientation', [show_pt(p) for p in exact_E], ['zeta(0) z^0 w^0', 'zeta(1/2) z^0 w^0'])
check('and the same up to diagonal equivalence: the units at which a proportionality candidate satisfies the relaxed rank-one condition', [show_pt(p) for p in relaxed_E], ['zeta(0) z^0 w^0', 'zeta(1/2) z^0 w^0'])
check('at u = 1 and u = -1 the relaxed structures are the strict ones', all(sorted(relaxed[(pt, f, mn)]) == sorted(sym[(pt, f, mn)][1]) for pt in (PT_ONE, PT_MINUS) for f in ('column', 'row') for mn in SHAPES), True)
print('  (%.0fs)' % (time.time() - t0))

print('== 5. sharpness: the structures at u = 1 and u = -1 are certified by exact reconstruction ==')
def reconstruct(H, m, n, cp, rows):
    """the Dita form at the index maps, with X, Y read off H and the twist solved for: True iff H = dita(X, Y, D) exactly with
    flat unitary factors and unit twists"""
    for cp_, rows_, ok, X, Y in dita_orientations(H, m, n):
        if tuple(cp_) == tuple(cp) and tuple(rows_) == tuple(rows):
            if not ok: return False
            col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
            D = {}
            for c in range(m):
                for b in range(n):
                    x = X[0][c] * Y[c][b][0]; h = H[row[(0, b)]][col[(c, 0)]]; nx = x.norm2(); q = h * x.conj(); D[(c, b)] = G(q.a / nx, q.b / nx)
            return all(D[(c, b)].norm2() == 1 for c in range(m) for b in range(n)) and all(H[row[(a, b)]][col[(c, d)]] == X[a][c] * D[(c, b)] * Y[c][b][d] for a in range(m) for b in range(n) for c in range(m) for d in range(n))
    return False
HM = Hu(MINUS); HMT = [list(c) for c in zip(*HM)]
check('at u = -1: H(-1) is reconstructed exactly from flat unitary factors and unit twists at the column-form maps, and H(-1)^T at the row-form maps', (reconstruct(HM, 2, 8, *M_COL), reconstruct(HMT, 2, 8, *M_ROW)), (True, True))
check('at u = -1 the numeric exhaustive search with factor unitarity finds exactly these two structures and nothing of the other shapes', ([(tuple(cp), tuple(rows)) for mn in SHAPES for cp, rows, ok, X, Y in dita_orientations(HM, *mn) if ok], [(tuple(cp), tuple(rows)) for mn in SHAPES for cp, rows, ok, X, Y in dita_orientations(HMT, *mn) if ok]), ([M_COL], [M_ROW]))
check('at u = 1: SIG is reconstructed exactly at every one of the nine census structures, and H(1) = SIG', (all(reconstruct(SIG, m, n, cp, rows) for nm, m, n, cp, rows in CLASSES), Hu(ONE) == SIG), (True, True))
check('the structures at u = -1 are not admitted at generic u nor at u = 1 (the exceptional structures are isolated)', (any(x[2] == GEN_ONE for x in []) , all(x[2] == GEN_ONE for x in conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)), all(x[2] == GEN_ONE for x in conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)), admitted_points(conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)) == frozenset([PT_MINUS]), admitted_points(conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)) == frozenset([PT_MINUS])), (False, False, False, True, True))
print('  (%.0fs)' % (time.time() - t0))

print('== 6. generic non-Diţă: the combination ==')
admit = set(exact_E) | set(relaxed_E)
check('the set of units at which H(u) admits any Diţă structure, of any shape, index map or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}; every other unit is a realizable non-Diţă point', sorted(show_pt(p) for p in admit), ['zeta(0) z^0 w^0', 'zeta(1/2) z^0 w^0'])
check('at generic u: no candidates at all (section 3), so no structure is admitted identically and none outside the candidate set', all(v == (0, 0) for v in [(len(c), len(e)) for (c, e) in gen.values()]), True)
print('  (%.0fs)' % (time.time() - t0))

print('== 7. controls ==')
agree = []
for pt in E_all:
    uv = gaussian_value(pt)
    if uv is None: continue
    H = Hu(uv); HT_ = [list(c) for c in zip(*H)]
    if not is_unitary16(H): agree.append((show_pt(pt), 'not unitary')); continue
    for form, M in (('column', H), ('row', HT_)):
        num = {mn: (len(o), sum(1 for x in o if x[2])) for mn in SHAPES for o in [dita_orientations(M, *mn)]}
        if any(num[mn] != (len(sym[(pt, form, mn)][0]), len(sym[(pt, form, mn)][1])) for mn in SHAPES): agree.append((show_pt(pt), form, num))
check('the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twenty Gaussian-rational candidates, both forms', agree, [])
def hull_point(m, n, cp, rows, phase):
    for cp_, rows_, ok, X, Y in dita_orientations(SIG, m, n):
        if ok and tuple(cp_) == tuple(cp) and tuple(rows_) == tuple(rows): break
    D = [[ONE] * n for _ in range(m)]; D[m - 1][n - 1] = phase
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    H = [[None] * 16 for _ in range(16)]
    for a in range(m):
        for b in range(n):
            for c in range(m):
                for d in range(n): H[row[(a, b)]][col[(c, d)]] = X[a][c] * D[c][b] * Y[c][b][d]
    return H
deform = []
for nm, m, n, cp, rows in CLASSES:
    H = hull_point(m, n, cp, rows, U5)
    found = [(tuple(cp_), tuple(rows_)) for cp_, rows_, ok, X, Y in dita_orientations(H, m, n) if ok]
    deform.append((is_unitary16(H), H != SIG, (tuple(cp), tuple(rows)) in found))
check('a genuine deformation inside each of the nine classes (one twist phase u5): unitary, off SIG, and found by the search in its own class', deform, [(True, True, True)] * 9)
# equivalence invariance: the stabilizer fixes SIG up to a diagonal rephasing (its pairs are matched on dephased keys), so the
# transported arc is apply(e, H(u)), which differs from SIG o u^E' by unit diagonal factors; E' is straight and admits no
# proportionality candidate at a generic u (both diagonal-invariant), and the transported matrices at u = -1 and u5 are
# searched directly, as act 37's control does: two structures at u = -1 (one per orientation), none at u5
def apply_matrix(e, H):
    p, s_ = e; out = [[None] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            i2, j2 = divmod(p[i * 16 + j], 16); out[i2][j2] = H[i][j] if s_ == 1 else H[i][j].conj()
    return out
def perm_pair(e):
    p, s_ = e
    rp = [p[i * 16] // 16 for i in range(16)]; cq = [p[j] % 16 for j in range(16)]
    if all(p[i * 16 + j] == rp[i] * 16 + cq[j] for i in range(16) for j in range(16)): return 'product', tuple(rp), tuple(cq)
    psi = [p[i * 16] % 16 for i in range(16)]; phi = [p[j] // 16 for j in range(16)]
    assert all(p[i * 16 + j] == phi[j] * 16 + psi[i] for i in range(16) for j in range(16))
    return 'transposed', tuple(psi), tuple(phi)
def transport_E(e, E):
    p, s_ = e; out = [[None] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            i2, j2 = divmod(p[i * 16 + j], 16); out[i2][j2] = E[i][j]
    return out
def straight(E):
    for i in range(16):
        for i2 in range(i + 1, 16):
            for d, ks in level_sets([E[i][k] - E[i2][k] for k in range(16)]).items():
                s = ZERO
                for k in ks: s = s + SIG[i][k] * SIG[i2][k].conj()
                if s != ZERO: return False
    return True
picks = [elems[k] for k in (1, len(elems) // 3, len(elems) - 1)]
equiv = []
for e in picks:
    E2 = transport_E(e, EE); E2T = [list(c) for c in zip(*E2)]
    g = all((len(c), len(x)) == (0, 0) for M in (E2, E2T) for mn in SHAPES for (c, x) in [gen_search_E(M, *mn)])
    HM2 = apply_matrix(e, HM); H52 = apply_matrix(e, Hu(U5))
    at_m = sum(1 for M in (HM2, [list(c) for c in zip(*HM2)]) for mn in SHAPES for cp, rows, ok, X, Y in dita_orientations(M, *mn) if ok)
    at_5 = sum(1 for M in (H52, [list(c) for c in zip(*H52)]) for mn in SHAPES for cp, rows, ok, X, Y in dita_orientations(M, *mn) if ok)
    equiv.append((perm_pair(e)[0], straight(E2), g, at_m, at_5, apply_matrix(e, SIG) == SIG))
check('the exponent matrix transported by three stabilizer elements (product, transposed, conjugating) is straight and admits no candidate at generic u; the transported matrices admit exactly two structures at u = -1 and none at u5', [(x[1], x[2], x[3], x[4]) for x in equiv], [(True, True, 2, 0)] * 3)
check('the three elements fix SIG only up to a diagonal rephasing, which is why the matrices and not the exponent matrix are searched', [x[5] for x in equiv], [False] * 3)
check('the three elements are of the kinds intended', sorted(set(x[0] for x in equiv)), ['product', 'transposed'])
Ep = [r[:] for r in EE]; Ep[1][2] = 0
check('a perturbed exponent matrix (the entry at ((0,1),(0,2)) cleared) is not straight: H(u) is not unitary at u5 and the Laurent identity fails', (straight(Ep), is_unitary16(Hu(U5, Ep))), (False, False))
def identical_in(E):
    return sorted((nm, 'row' if tr else 'column') for nm, m, n, cp, rows in CLASSES for tr in (False, True) if all(x[2] == GEN_ONE for x in conditions_E(E, m, n, cp, rows, tr)))
PA = [[EA(i, j) for j in range(16)] for i in range(16)]; PB = [[EB(i, j) for j in range(16)] for i in range(16)]; PC = [[EC(i, j) for j in range(16)] for i in range(16)]
def add(*Ms): return [[sum(M[i][j] for M in Ms) for j in range(16)] for i in range(16)]
pieces = {'A': PA, 'B': PB, 'C': PC, 'A+B': add(PA, PB), 'A+C': add(PA, PC), 'B+C': add(PB, PC), 'A+B+C': EE}
check('the three pieces and their pairwise sums are straight lines, each admitting some census structure identically; the triple admits none (interpretation: three Diţă directions whose sum is not Diţă)', {k: (straight(M), identical_in(M)) for k, M in pieces.items()}, @@PIECES@@)
WM = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
check("act 37's arc W is straight and identically in the frozen 2x8 class t1 in both orientations and in no other structure (control of the classifier)", (straight(WM), identical_in(WM)), (True, [('t1', 'column'), ('t1', 'row')]))
print('  (%.0fs)' % (time.time() - t0))

print('== 8. the tangent space at SIG (interpretation, exact integer ranks) ==')
def unit_row(*terms):
    v = [0] * 256
    for coef, i, j in terms: v[i * 16 + j] += coef
    return v
def struct_eqs(m, n, cp, rows, transpose):
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    T = (lambda i, j: (j, i)) if transpose else (lambda i, j: (i, j))
    eqs = []
    for c in range(m):
        for b in range(n):
            for a in range(1, m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    eqs.append(unit_row((1,) + T(i, j), (-1,) + T(i2, j), (-1,) + T(i, j0), (1,) + T(i2, j0)))
    def lam(a, b, c): return [(1,) + T(row[(a, b)], col[(c, 0)]), (-1,) + T(row[(0, b)], col[(c, 0)])]
    for a in range(1, m):
        for b in range(1, n):
            for c in range(m):
                eqs.append(unit_row(*(lam(a, b, c) + [(-k, i, j) for k, i, j in lam(a, 0, c)])))
    return eqs
TQ = defect_rows(SIG)
rT = rank_int(TQ)
check('the tangent space of unitary deformations SIG o exp(iR) at SIG: rank of the first-moment equations, its dimension with the 31 gauge directions, and the defect', (rT, 256 - rT, 256 - rT - 31), (176, 80, 49))
dims = {}
for nm, m, n, cp, rows in CLASSES:
    for tr in (False, True):
        dims[(nm, 'row' if tr else 'column')] = 256 - rank_int(TQ + struct_eqs(m, n, cp, rows, tr))
check('the dimension of the tangent directions along which each structure is admitted identically (with gauge), by class: column and row forms agree', ([dims[(nm, 'column')] for nm in NAMES], all(dims[(nm, 'column')] == dims[(nm, 'row')] for nm in NAMES)), (@@TDIMS@@, True))
check('the witness exponent matrix is tangent (it is straight) and lies in none of the eighteen subspaces, while the tangent space is the sum of all eighteen: the obstruction is nonlinear compatibility, not a missing tangent direction', (all(sum(r[k] * EE[k // 16][k % 16] for k in range(256)) == 0 for r in TQ), all(any(sum(r[k] * EE[k // 16][k % 16] for k in range(256)) != 0 for r in struct_eqs(m, n, cp, rows, tr)) for nm, m, n, cp, rows in CLASSES for tr in (False, True)), rank_int([v for nm, m, n, cp, rows in CLASSES for tr in (False, True) for v in nullspace_int(TQ + struct_eqs(m, n, cp, rows, tr))])), (True, True, 80))
print('  (%.0fs)' % (time.time() - t0))

print()
if fails:
    print('dita_local_escape_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print(@@OKLINE@@)
