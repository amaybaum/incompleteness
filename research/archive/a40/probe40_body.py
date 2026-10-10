
# ---- A40: the Dita locus of H3(u1, u2, u3) = SIG o u1^A u2^B u3^C in the three-torus --------------------------------
# Entry (i, j) of 4 H3 is the monomial u^k i^p z^q w^r, k = (A, B, C)[i][j], (p, q, r) = SIGE[i][j]. Every condition a Dita
# structure imposes (proportionality within a class on a block, rank one of the block ratios) is a character equation
# u^k = c with k in Z^3 and c in G = <i, z, w> = Z/4 x Z^2 (z, w independent modulo roots of unity), written additively.

# ---- the flat calculus, embedded (no imported helper) -----------------------------------------------------------------
def vadd(a, b): return ((a[0] + b[0]) % 4, a[1] + b[1], a[2] + b[2])
def vsub(a, b): return ((a[0] - b[0]) % 4, a[1] - b[1], a[2] - b[2])
def vmul(n, a): return ((n * a[0]) % 4, n * a[1], n * a[2])
V0 = (0, 0, 0)
class Empty(Exception):
    pass
def _hnf(rows):
    """the canonical row Hermite normal form (positive pivots, entries above pivots reduced) of the system {u^k = v}, values
    carried along; raises Empty on an inconsistent system (a zero character with a nonzero value)"""
    R = [[list(k), v] for k, v in rows]
    basis = []
    for col in range(3):
        while True:
            idx = [t for t in range(len(R)) if R[t][0][col] != 0]
            if len(idx) <= 1: break
            idx.sort(key=lambda t: abs(R[t][0][col]))
            pk, pv = R[idx[0]]
            for t in idx[1:]:
                f = R[t][0][col] // pk[col]
                R[t] = [[a - f * b for a, b in zip(R[t][0], pk)], vsub(R[t][1], vmul(f, pv))]
        idx = [t for t in range(len(R)) if R[t][0][col] != 0]
        if idx:
            k, v = R.pop(idx[0])
            if k[col] < 0: k = [-a for a in k]; v = vmul(-1, v)
            basis.append([k, v])
    for k, v in R:
        if any(k): raise AssertionError('reduction incomplete')
        if v != V0: raise Empty()
    piv = [next(c for c in range(3) if k[c] != 0) for k, v in basis]
    for a in range(len(basis)):
        pc = piv[a]; h = basis[a][0][pc]
        for b in range(a):
            f = basis[b][0][pc] // h
            if f:
                basis[b] = [[x - f * y for x, y in zip(basis[b][0], basis[a][0])], vsub(basis[b][1], vmul(f, basis[a][1]))]
    return tuple((tuple(k), v) for k, v in basis)
class Flat:
    """the solution set in T^3 of a finite consistent character system, stored canonically"""
    __slots__ = ('B',)
    def __init__(self, rows=()): self.B = _hnf(list(rows))
    @staticmethod
    def of(B):
        f = Flat.__new__(Flat); f.B = B; return f
    def __eq__(self, o): return isinstance(o, Flat) and self.B == o.B
    def __hash__(self): return hash(self.B)
    def rank(self): return len(self.B)
    def dim(self): return 3 - len(self.B)
    def meet(self, other): return Flat.of(_hnf(list(self.B) + list(other.B)))
    def add(self, k, v): return Flat.of(_hnf(list(self.B) + [(tuple(k), v)]))
    def reduce(self, k, v):
        k = list(k)
        for bk, bv in self.B:
            pc = next(c for c in range(3) if bk[c] != 0)
            f = k[pc] // bk[pc]
            if f: k = [a - f * b for a, b in zip(k, bk)]; v = vsub(v, vmul(f, bv))
        return (tuple(k), v)
    def holds(self, k, v):
        rk, rv = self.reduce(k, v)
        return not any(rk) and rv == V0
    def contains(self, other): return all(other.holds(k, v) for k, v in self.B)
    def show(self):
        nm = ('u1', 'u2', 'u3')
        def val(v):
            p, q, r = v; s = {0: '1', 1: 'i', 2: '-1', 3: '-i'}[p]
            return s + ('' if not q else ' z^%d' % q) + ('' if not r else ' w^%d' % r)
        return ', '.join('%s = %s' % ('*'.join(('%s^%d' % (nm[t], k[t]) if k[t] != 1 else nm[t]) for t in range(3) if k[t]), val(v)) for k, v in self.B) or 'T^3'
TORUS = Flat()
def meet_or_none(F, G):
    try: return F.meet(G)
    except Empty: return None
def gval(v):
    p, q, r = v; out = ONE
    for _ in range(p % 4): out = out * I_
    for _ in range(abs(q)): out = out * (z if q > 0 else z.conj())
    for _ in range(abs(r)): out = out * (w if r > 0 else w.conj())
    return out
def upow(u, k):
    out = ONE
    for x, e in zip(u, k):
        for _ in range(abs(e)): out = out * (x if e > 0 else x.conj())
    return out
def on_flat(F, u): return F is not None and all(upow(u, k) == gval(v) for k, v in F.B)

print('== 1. the flat calculus: exactness controls ==')
import random
rng = random.Random(40)
def rand_eq(): return (tuple(rng.randint(-2, 2) for _ in range(3)), (rng.randint(0, 3), rng.randint(-2, 2), rng.randint(-2, 2)))
def rand_one():
    while True:
        k, v = rand_eq()
        if any(k): return Flat([(k, v)])
trials = cons = idem = order = sym = assoc = contain = holds_ok = 0
for _ in range(400):
    eqs = [rand_eq() for _ in range(rng.randint(1, 4))]
    try: F = Flat(eqs)
    except Empty: continue
    cons += 1
    idem += Flat(F.B) == F and Flat.of(_hnf(list(F.B) + list(F.B))) == F
    sh = eqs[:]; rng.shuffle(sh); order += Flat(sh) == F
    holds_ok += all(F.holds(k, v) for k, v in eqs)
    Gf = rand_one() if rng.random() < 0.5 else TORUS
    Hf = rand_one() if rng.random() < 0.5 else TORUS
    FG, GF = meet_or_none(F, Gf), meet_or_none(Gf, F)
    sym += FG == GF
    A1 = None if FG is None else meet_or_none(FG, Hf); GH = meet_or_none(Gf, Hf); A2 = None if GH is None else meet_or_none(F, GH)
    assoc += A1 == A2
    contain += FG is None or (F.contains(FG) and Gf.contains(FG) and (FG == F) == Gf.contains(F))
    trials += 1
check('random systems: canonical form idempotent, independent of generator order, every generator holds; meet symmetric and associative; the meet contained in both, and equal to F exactly when G contains F', (idem, order, holds_ok, sym, assoc, contain) == (trials,) * 6 and trials > 200, True)
hand = []
try: Flat([((2, 0, 0), (0, 1, 0)), ((4, 0, 0), (0, 3, 0))]); hand.append('sat')
except Empty: hand.append('empty')
try: Flat([((2, 0, 0), (0, 1, 0)), ((4, 0, 0), (0, 2, 0))]); hand.append('sat')
except Empty: hand.append('empty')
try: Flat([((1, 1, 0), (2, 0, 0)), ((1, 1, 0), V0)]); hand.append('sat')
except Empty: hand.append('empty')
fa = Flat([((1, 1, 0), (1, 0, 0)), ((0, 1, -1), (0, 0, 1))]); fb = Flat([((1, 0, 1), (1, 0, -1)), ((1, 1, 0), (1, 0, 0))])
hand += [fa == fb, fa.holds((1, 0, 1), (1, 0, -1)), fa.holds((1, 0, 1), (1, 0, 1)), Flat([((2, 0, 0), V0)]).contains(Flat([((1, 0, 0), V0)])), Flat([((1, 0, 0), V0)]).contains(Flat([((2, 0, 0), V0)]))]
check('hand systems: u1^2 = z with u1^4 = z^3 empty, with u1^4 = z^2 satisfiable, u1 u2 = -1 with u1 u2 = 1 empty; two presentations of one flat equal; a derived character holds, a wrong one does not; u1^2 = 1 contains u1 = 1 and not conversely', hand, ['empty', 'sat', 'empty', True, True, False, True, False])
# independent reconstruction: flats whose pivots are 1 have explicit Gaussian-rational points (free coordinates chosen as
# Gaussian-rational units, pivots solved); every original equation is re-evaluated in exact arithmetic
UNITS_Q = [G(Fr(3, 5), Fr(4, 5)), G(Fr(8, 17), Fr(15, 17)), G(Fr(20, 29), Fr(21, 29)), G(Fr(7, 25), Fr(24, 25)), I_, G(-1)]
recon = rejected = tested = 0
for _ in range(3000):
    eqs = [rand_eq() for _ in range(rng.randint(1, 3))]
    try: F = Flat(eqs)
    except Empty: continue
    piv = [next(c for c in range(3) if k[c]) for k, v in F.B]
    if any(k[p] != 1 for (k, v), p in zip(F.B, piv)): continue
    u = [rng.choice(UNITS_Q) if c not in piv else None for c in range(3)]
    for (k, v), p in reversed(list(zip(F.B, piv))):
        rest = upow([u[c] if (c > p and k[c]) else ONE for c in range(3)], [k[c] if c > p else 0 for c in range(3)])
        u[p] = gval(v) * rest.conj()
    tested += 1
    recon += all(upow(u, k) == gval(v) for k, v in eqs) and on_flat(F, u)
    if any(k[0] for k, v in F.B):
        bad = [u[0] * G(Fr(3, 5), Fr(4, 5)), u[1], u[2]]
        rejected += not on_flat(F, bad)
    else:
        rejected += 1
check('explicit points reconstructed on the unit-pivot flats among 3000 random systems satisfy every original equation exactly, and moving u1 off the flat is detected whenever the flat constrains u1', (tested > 100, recon == tested, rejected == tested), (True, True, True))
print('  (%.0fs)' % (time.time() - t0))

# ---- act 37's census of SIG's Dita structures and act 38's two exceptional index maps, verbatim from act 38's probe
CLASSES = [(nm, m, n, tuple(tuple(b) for b in cp), tuple(tuple(r) for r in rows)) for nm, m, n, cp, rows in [["k1", 4, 4, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]], ["k2", 4, 4, [[0, 2, 8, 10], [1, 3, 9, 11], [4, 6, 12, 14], [5, 7, 13, 15]], [[0, 2, 8, 10], [1, 3, 9, 11], [4, 6, 12, 14], [5, 7, 13, 15]]], ["k3", 4, 4, [[0, 2, 9, 11], [1, 3, 8, 10], [4, 6, 13, 15], [5, 7, 12, 14]], [[0, 6, 8, 14], [1, 7, 9, 15], [2, 4, 10, 12], [3, 5, 11, 13]]], ["k4", 4, 4, [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]], [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]], ["e1", 8, 2, [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15]], [[0, 2, 4, 6, 8, 10, 12, 14], [1, 3, 5, 7, 9, 11, 13, 15]]], ["e2", 8, 2, [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]], [[0, 1, 2, 3, 8, 9, 10, 11], [4, 5, 6, 7, 12, 13, 14, 15]]], ["t1", 2, 8, [[0, 1, 2, 3, 8, 9, 10, 11], [4, 5, 6, 7, 12, 13, 14, 15]], [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]]], ["t2", 2, 8, [[0, 2, 4, 6, 8, 10, 12, 14], [1, 3, 5, 7, 9, 11, 13, 15]], [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15]]], ["t3", 2, 8, [[0, 2, 5, 7, 8, 10, 13, 15], [1, 3, 4, 6, 9, 11, 12, 14]], [[0, 10], [1, 11], [2, 8], [3, 9], [4, 14], [5, 15], [6, 12], [7, 13]]]]]
M_COL = (((0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)), ((0, 2), (1, 3), (4, 6), (5, 15), (7, 13), (8, 10), (9, 11), (12, 14)))
M_ROW = (((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)), ((0, 2), (1, 9), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 10)))
STRUCT_OF = {nm: ((m, n), cp, rows) for nm, m, n, cp, rows in CLASSES}

# ---- the family and its structures ---------------------------------------------------------------------------------
def EA_(i, j): return EA(i, j)
PA = [[EA(i, j) for j in range(16)] for i in range(16)]
PB = [[EB(i, j) for j in range(16)] for i in range(16)]
PC = [[EC(i, j) for j in range(16)] for i in range(16)]
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def kadd(a, b): return tuple(x + y for x, y in zip(a, b))
import itertools
PAIRS = list(itertools.combinations(range(16), 2))
SHAPES3 = ((4, 4), (8, 2), (2, 8))
def orientations(KA, KB, KC):
    K = [[(KA[i][j], KB[i][j], KC[i][j]) for j in range(16)] for i in range(16)]
    C = [[SIGE[i][j] for j in range(16)] for i in range(16)]
    return {'column': (K, C), 'row': ([list(c) for c in zip(*K)], [list(c) for c in zip(*C)])}
def enumerate_candidates(OR):
    """every (orientation, shape, column blocks, row classes) whose within-class pairs have, on every block, a common point
    of their proportionality loci; a structure admitted anywhere on T^3 is among them (see the preregistration)"""
    cache = {}
    def pbf(vals):
        if vals in cache: return cache[vals]
        d0, e0 = vals[0]
        try:
            F = TORUS
            for d, e in vals[1:]: F = F.add(ksub(d, d0), vsub(e0, e))
            r = F
        except Empty: r = None
        cache[vals] = r; return r
    cands = {}; stats = {}
    for form, (Km, Cm) in OR.items():
        de = {p: [(ksub(Km[p[0]][j], Km[p[1]][j]), vsub(Cm[p[0]][j], Cm[p[1]][j])) for j in range(16)] for p in PAIRS}
        for m, n in SHAPES3:
            good = {}
            for Sb in itertools.combinations(range(16), n):
                loc = {}
                for p in PAIRS:
                    F = pbf(tuple(sorted(set(de[p][j] for j in Sb))))
                    if F is not None: loc[p] = F
                def rec(rem, classes, F):
                    if not rem: good.setdefault(tuple(classes), []).append((Sb, F)); return
                    i = min(rem)
                    nb = sorted(j for j in rem if j != i and (i, j) in loc)
                    for rest in itertools.combinations(nb, m - 1):
                        cl = (i,) + rest; Gf = F
                        for a, b in itertools.combinations(cl, 2):
                            Gf = meet_or_none(Gf, loc[(a, b)])
                            if Gf is None: break
                        if Gf is None: continue
                        rec(rem - set(cl), classes + [cl], Gf)
                rec(frozenset(range(16)), [], TORUS)
            nb0 = len(cands)
            for P, blocks in good.items():
                def cover(rem, chosen, F):
                    if not rem: cands[(form, (m, n), tuple(sorted(chosen)), P)] = F; return
                    first = min(rem)
                    for Sb, Gf in blocks:
                        if Sb[0] == first and set(Sb) <= rem:
                            Hf = meet_or_none(F, Gf)
                            if Hf is not None: cover(rem - set(Sb), chosen + [Sb], Hf)
                cover(frozenset(range(16)), [], TORUS)
            stats[(form, (m, n))] = len(cands) - nb0
    return cands, stats
def conditions(OR, form, mn, cp, rows, relaxed):
    Km, Cm = OR[form]; m, n = mn
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    def ent(i, j): return (Km[i][j], Cm[i][j])
    def div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
    def mul(x, y): return (kadd(x[0], y[0]), vadd(x[1], y[1]))
    out = []
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    out.append(div(div(ent(i, j), ent(i2, j)), div(ent(i, j0), ent(i2, j0))))
    lam = {(a, b, c): div(ent(row[(a, b)], col[(c, 0)]), ent(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                if not relaxed: out.append(div(lam[(a, b, c)], mul(lam[(a, 0, c)], lam[(0, b, c)])))
                elif c > 0: out.append(div(div(lam[(a, b, c)], lam[(a, 0, c)]), div(lam[(a, b, 0)], lam[(a, 0, 0)])))
    return out
def solve(conds):
    """the exact solution flat of {u^k c = 1}, or None"""
    try:
        F = TORUS
        for k, c in conds:
            if not any(k):
                if c != V0: return None
                continue
            F = F.add(k, vsub(V0, c))
        return F
    except Empty:
        return None
def classify(KA, KB, KC):
    OR = orientations(KA, KB, KC)
    cands, stats = enumerate_candidates(OR)
    loci = {}
    for key in cands:
        form, mn, cp, rows = key
        loci[key] = (solve(conditions(OR, form, mn, cp, rows, False)), solve(conditions(OR, form, mn, cp, rows, True)))
    return OR, cands, stats, loci
def union_faces(loci):
    """the maximal nonempty strict loci, and whether every nonempty locus lies in one of them"""
    ne = set(F for F in loci.values() if F is not None)
    maximal = sorted((F for F in ne if not any(M2 != F and M2.contains(F) for M2 in ne)), key=lambda F: F.B)
    return maximal, all(any(M.contains(F) for M in maximal) for F in ne)

print('== 2. completeness: every Dita structure admitted anywhere is among the enumerated candidates ==')
OR, CANDS, STATS, LOCI = classify(PA, PB, PC)
check('candidate structures (a common point of the proportionality loci on every block), by orientation and shape', sorted((f, mn, k) for (f, mn), k in STATS.items()), sorted([('column', (4, 4), 13), ('column', (8, 2), 5), ('column', (2, 8), 5), ('row', (4, 4), 13), ('row', (8, 2), 5), ('row', (2, 8), 5)]))
check('in all', len(CANDS), 46)
print('  (%.0fs)' % (time.time() - t0))

print('== 3. locus exactness: each candidate strictly and up to diagonal equivalence ==')
strict = {k: v[0] for k, v in LOCI.items()}; relax = {k: v[1] for k, v in LOCI.items()}
check('the relaxed locus equals the strict locus for every candidate', all(strict[k] == relax[k] for k in LOCI), True)
check('empty and nonempty strict loci', (sum(1 for v in strict.values() if v is None), sum(1 for v in strict.values() if v is not None)), (16, 30))
check('every nonempty locus is cut out by coordinate characters u_k = +-1 alone', all(all(sorted(map(abs, k)) == [0, 0, 1] and v in (V0, (2, 0, 0)) for k, v in F.B) for F in strict.values() if F is not None), True)
print('  (%.0fs)' % (time.time() - t0))

print('== 4. union reduction: the union of the loci is five coordinate 2-subtori ==')
FACES = union_faces(strict)
check('the maximal loci', sorted(F.show() for F in FACES[0]), ['u1 = -1', 'u1 = 1', 'u2 = 1', 'u3 = -1', 'u3 = 1'])
check('every nonempty locus lies in one of them, and each of them is itself a locus', (FACES[1], all(any(strict[k] == F for k in strict) for F in FACES[0])), (True, True))
print('  (%.0fs)' % (time.time() - t0))

print('== 5. controls ==')
DIAG = Flat([((1, -1, 0), V0), ((0, 1, -1), V0)])
dpts = sorted(set(G_.show() for G_ in (meet_or_none(F, DIAG) for F in FACES[0]) if G_ is not None))
check("the union restricted to the diagonal u1 = u2 = u3 = u: the points u = 1 and u = -1, act 38's exceptional set", dpts, ['u1 = -1, u2 = -1, u3 = -1', 'u1 = 1, u2 = 1, u3 = 1'])
def at(u): return sorted(k for k, F in strict.items() if on_flat(F, u))
P1 = (ONE, ONE, ONE); PM = (G(-1), G(-1), G(-1))
i0c = CLASSES
census = set((f, mn, tuple(sorted(tuple(b) for b in cp)), tuple(sorted(tuple(r) for r in rows))) for nm, m, n, cp, rows in i0c for f, mn in (('column', (m, n)), ('row', (m, n))))
check('at (1, 1, 1): eighteen structures, exactly act 37 census in both orientations', (len(at(P1)), set((k[0], k[1], tuple(sorted(k[2])), tuple(sorted(k[3]))) for k in at(P1)) == census), (18, True))
check('at (-1, -1, -1): one 2 x 8 structure per orientation, act 38 M_COL and M_ROW', [(k[0], k[1], tuple(sorted(k[2])), tuple(sorted(k[3]))) for k in at(PM)], [('column', (2, 8), M_COL[0], tuple(sorted(M_COL[1]))), ('row', (2, 8), M_ROW[0], tuple(sorted(M_ROW[1])))])
NEG = Flat([((0, 1, 0), (2, 0, 0))])
check('the absent face u2 = -1 (negative control): contained in no locus, and its intersection with the union is the union of its intersections with the other four faces, of dimension 1', (any(F.contains(NEG) for F in strict.values() if F is not None), sorted(G_.dim() for G_ in (meet_or_none(F, NEG) for F in FACES[0]) if G_ is not None)), (False, [1, 1, 1, 1]))
def joint_gate(mats):
    bad = 0; nsets = 0
    for r in range(16):
        for s in range(16):
            groups = {}
            for j in range(16): groups.setdefault(tuple(M[r][j] - M[s][j] for M in mats), []).append(j)
            for t, js in groups.items():
                nsets += 1
                tot = ZERO
                for j in js: tot = tot + SIG[r][j] * SIG[s][j].conj()
                if tot != (G(16) if (r == s and not any(t)) else ZERO): bad += 1
    return nsets, bad
check("the three +1 faces are act 39's pair subfamilies (B, C), (A, C), (A, B), realizable with the joint level-set counts act 39 recorded", [joint_gate(ms) for ms in ([PB, PC], [PA, PC], [PA, PB])], [(480, 0), (440, 0), (424, 0)])
print('  (%.0fs)' % (time.time() - t0))

print('== 6. the kernel layer, replayed: named exclusions and whole-face factorizations ==')
def witnesses(form, cp, rows):
    Km, Cm = OR[form]; out = []
    for cl in rows:
        for i, i2 in itertools.combinations(cl, 2):
            for bl in cp:
                for j0, j in itertools.combinations(bl, 2):
                    e = lambda a, b: (Km[a][b], Cm[a][b])
                    k = ksub(ksub(e(i, j)[0], e(i2, j)[0]), ksub(e(i, j0)[0], e(i2, j0)[0]))
                    c = vsub(vsub(e(i, j)[1], e(i2, j)[1]), vsub(e(i, j0)[1], e(i2, j0)[1]))
                    out.append((k, c))
    return out
NAMED = [(nm, f, (m, n), tuple(map(tuple, cp)), tuple(map(tuple, rows))) for nm, m, n, cp, rows in i0c for f in ('column', 'row')]
NAMED += [('M_COL', 'column', (2, 8)) + M_COL, ('M_ROW', 'row', (2, 8)) + M_ROW]
wit_ok = []
for nm, f, mn, cp, rows in NAMED:
    ws = witnesses(f, cp, rows)
    prop = solve(ws)
    cw = [(k, c) for k, c in ws if sorted(map(abs, k)) == [0, 0, 1]]
    coordflat = solve(cw) if cw else None
    key = next(k for k in strict if k[0] == f and k[1] == mn and set(map(frozenset, k[2])) == set(map(frozenset, cp)) and set(map(frozenset, k[3])) == set(map(frozenset, rows)))
    wit_ok.append(prop is not None and coordflat == prop and prop.contains(strict[key]) and all(v in (V0, (2, 0, 0)) for k, v in prop.B))
check('for each of the twenty named structures (the census in both orientations, M_COL, M_ROW), single four-position witnesses with coordinate characters generate its proportionality locus exactly, which contains its strict locus', (len(wit_ok), all(wit_ok)), (20, True))
# whole-face factorizations: X = (1+i)/2 [[1, 1], [1, -1]], D = 2/(1+i)^2 = -i, Y_c = (1+i)/4 (class representatives of 4 H3 on block c)
def H3(u1, u2, u3): return [[SIG[i][j] * gp(u1, PA[i][j]) * gp(u2, PB[i][j]) * gp(u3, PC[i][j]) for j in range(16)] for i in range(16)]
def gp(u, k):
    out = ONE
    for _ in range(k): out = out * u
    return out
K2, K8, DD = G(Fr(1, 2), Fr(1, 2)), G(Fr(1, 4), Fr(1, 4)), G(0, -1)
XF = [[K2, K2], [K2, -K2]]
FACEDEF = [('u1 = 1', 0, ONE, 'column', STRUCT_OF['t2']), ('u1 = -1', 0, G(-1), 'column', ((2, 8),) + M_COL), ('u2 = 1', 1, ONE, 'column', STRUCT_OF['t1']),
           ('u3 = 1', 2, ONE, 'row', STRUCT_OF['t1']), ('u3 = -1', 2, G(-1), 'row', ((2, 8),) + M_ROW)]
TESTU = [G(Fr(3, 5), Fr(4, 5)), G(Fr(8, 17), Fr(15, 17)), G(Fr(20, 29), Fr(21, 29)), I_, G(Fr(7, 25), Fr(24, 25))]
face_ok = []
for name, coord, val, f, ((m, n), cp, rows) in FACEDEF:
    for s in range(3):
        u = [TESTU[s], TESTU[s + 1], TESTU[s + 2]]; u[coord] = val
        H = H3(*u); M = H if f == 'column' else [list(c) for c in zip(*H)]
        rinv = {(a, b): rows[b][a] for b in range(n) for a in range(m)}; cinv = {(c, d): cp[c][d] for c in range(m) for d in range(n)}
        Y = [[[K8 * M[rinv[(0, b)]][cinv[(c, d)]] for d in range(n)] for b in range(n)] for c in range(m)]   # M = 4 H3 (unimodular)
        ident = all(M[rinv[(a, b)]][cinv[(c, d)]] == G(4) * XF[a][c] * DD * Y[c][b][d] for a in range(m) for b in range(n) for c in range(m) for d in range(n))
        yflat = all(is_unitary_s(Y[c], 1) and all(y.norm2() == Fr(1, 8) for row in Y[c] for y in row) for c in range(m))
        xflat = is_unitary_s(XF, 1) and all(x.norm2() == Fr(1, 2) for row in XF for x in row) and DD.norm2() == 1
        face_ok.append((ident, yflat, xflat))
check('the whole-face factorizations: at three Gaussian-rational points of each of the five faces, H3 (or its transpose) equals dita(X, Y, D) at the face structure, with X and every Y_c flat unitary and |D| = 1', (len(face_ok), all(all(x) for x in face_ok)), (15, True))
check('and the factor identities: (1+i)/2 * (1+i)/4 * 2/(1+i)^2 = 1/4, |(1+i)/2|^2 = 1/2, |(1+i)/4|^2 = 1/8, 2/(1+i)^2 = -i', (K2 * K8 * DD == G(Fr(1, 4)), K2.norm2(), K8.norm2(), DD * G(1, 1) * G(1, 1) == G(2)), (True, Fr(1, 2), Fr(1, 8), True))
print('  (%.0fs)' % (time.time() - t0))

print('== 7. an independent control: act 36\'s exhaustive structure search, with factor unitarity, at exact points ==')
PTS = [('generic', (TESTU[0], TESTU[1], TESTU[2])), ('generic', (TESTU[4], I_, TESTU[0])), ('u1 = 1', (ONE, TESTU[0], TESTU[1])),
       ('u1 = -1', (G(-1), TESTU[0], TESTU[1])), ('u2 = 1', (TESTU[0], ONE, TESTU[1])), ('u2 = -1, absent', (TESTU[0], G(-1), TESTU[1])),
       ('u3 = 1', (TESTU[0], TESTU[1], ONE)), ('u3 = -1', (TESTU[0], TESTU[1], G(-1))), ('u1 = i, absent', (I_, TESTU[0], TESTU[1])),
       ('(1, u, -1)', (ONE, TESTU[2], G(-1))), ('(u, 1, 1)', (TESTU[2], ONE, ONE)), ('(-1, 1, u)', (G(-1), ONE, TESTU[4])),
       ('(1, 1, 1)', (ONE, ONE, ONE)), ('(-1, -1, -1)', (G(-1), G(-1), G(-1))), ('(-1, 1, 1)', (G(-1), ONE, ONE)),
       ('(1, 1, -1)', (ONE, ONE, G(-1))), ('(1, -1, 1)', (ONE, G(-1), ONE))]
agree = []; counts = []
for nm_, u in PTS:
    H = H3(*u); HT = [list(c) for c in zip(*H)]
    got = set()
    for f, M in (('column', H), ('row', HT)):
        for mn in SHAPES3:
            for cp, rows, ok, X_, Y_ in dita_orientations(M, *mn):
                if ok: got.add((f, mn, frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows))))
    pred = set((k[0], k[1], frozenset(map(frozenset, k[2])), frozenset(map(frozenset, k[3]))) for k in at(u))
    agree.append(got == pred); counts.append(len(got))
check('at seventeen exact points (two generic, the five faces, two absent directions, three lines, five special points) the search finds exactly the predicted structures', (all(agree), counts), (True, [0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4]))
print('  (%.0fs)' % (time.time() - t0))

print('== 8. a countercontrol: one entry of C cleared ==')
Cp = [r[:] for r in PC]; Cp[1][2] = 0
_, CANDS2, _, LOCI2 = classify(PA, PB, Cp)
F2 = union_faces({k: v[0] for k, v in LOCI2.items()})
check('the classifier applied to the perturbed pieces: candidates, nonempty loci and the union, which collapses to the one face where C drops out', (len(CANDS2), sum(1 for v in LOCI2.values() if v[0] is not None), sorted(F.show() for F in F2[0]), F2[1]), (30, 23, ['u3 = 1'], True))
print('  (%.0fs)' % (time.time() - t0))

print()
if fails:
    print('dita_torus_locus_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted '
      'anywhere is among 46 enumerated candidates; their strict and relaxed loci are computed exactly and agree; the union of the '
      '30 nonempty loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so H3 admits a Dita '
      'structure of some shape, index map and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 '
      'or u3 = +-1')
