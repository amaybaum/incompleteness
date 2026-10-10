"""Pre-freeze measurement for the corrective round: the three counts at each named point (read-only, local)."""
import itertools, math, time, json
exec(open('audit.py', encoding='utf-8').read().split("res = {}")[0])
from collections import Counter
PG = {}
def per_group(OR, key, relaxed):
    ck = (id(OR), key, relaxed)
    if ck in PG: return PG[ck]
    PG[ck] = _per_group(OR, key, relaxed); return PG[ck]
def _per_group(OR, key, relaxed):
    form, mn, cp, rows = key; m, n = mn
    Pf = add_all(TORUS, prop_conds(OR, form, mn, cp, rows))
    if Pf is None: return None, None
    per = []
    for b in range(1, n):
        L = []
        for sb in itertools.permutations(range(m)):
            F = add_all(Pf, group_conds(OR, form, mn, cp, rows, b, sb, relaxed))
            if F is not None: L.append((sb, F))
        per.append(L)
    return Pf, per
def at_point(OR, cands, u):
    out = {}
    for key in cands:
        form, (m, n), cp, rows = key
        rec = {}
        for relaxed in (False, True):
            Pf, per = per_group(OR, key, relaxed)
            if Pf is None or not on_flat(Pf, u): rec[relaxed] = 0; continue
            M = 1
            for L in per: M *= sum(1 for sb, F in L if on_flat(F, u))
            rec[relaxed] = M
        if rec[False] or rec[True]: out[key] = (rec[False], rec[True])
    return out
def literal(m, n, M): return M * math.factorial(n) * math.factorial(m) * math.factorial(m) * math.factorial(n) ** m
def report(name, OR, cands, u):
    t = time.time(); res = at_point(OR, cands, u)
    print('==', name, '(%.0fs)' % (time.time() - t))
    for relaxed, lab in ((False, 'strict'), (True, 'relaxed')):
        ks = [k for k, v in res.items() if v[relaxed]]
        by = Counter((k[0], k[1]) for k in ks)
        print('  %-7s partition structures %d  by (form, shape) %s' % (lab, len(ks), dict(sorted(by.items()))))
        for k in sorted(ks):
            M = res[k][relaxed]
            print('     %-6s %s  valid alignments %6d  of %8d   realizing index maps %d' % (k[0], k[1], M, math.factorial(k[1][0]) ** (k[1][1] - 1), literal(k[1][0], k[1][1], M)))
    return res
H3OR = OR; H3C = CANDS
PT = {'SIG = H3(1,1,1)': (ONE, ONE, ONE), 'H3(-1,-1,-1) = act 38 arc at u = -1': (G(-1), G(-1), G(-1))}
R3 = {nm: report(nm, H3OR, H3C, u) for nm, u in PT.items()}
Z = [[0] * 16 for _ in range(16)]; WM = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
WOR = orientations(WM, Z, Z); WC, _ = enumerate_candidates(WOR)
u60 = G(Fr(3599, 3601), Fr(120, 3601)); u5 = G(Fr(3, 5), Fr(4, 5))
assert u60 * G(60, -1) == G(60, 1)
RW = {}
for nm, u in (('W-arc u = 1', ONE), ('W-arc u = -1', G(-1)), ('W-arc P = Pu(u60)', u60), ('W-arc Pu(u5)', u5)):
    RW[nm] = report(nm, WOR, WC, (u, ONE, ONE))
# factorization classes at SIG under act 36's stabilizer (order 1024), acting by permutation of rows/columns and transposition
def decomp(perm):
    # perm on 256 positions: (i,j) -> (i2,j2) or transposed (i,j) -> (j2', i2')
    rp = {}; cpm = {}; tr = None
    for t in (False, True):
        ok = True; rp = {}; cpm = {}
        for i in range(16):
            for j in range(16):
                q = perm[i * 16 + j]; i2, j2 = divmod(q, 16)
                if t: i2, j2 = j2, i2
                if rp.setdefault(i, i2) != i2 or cpm.setdefault(j, j2) != j2: ok = False; break
            if not ok: break
        if ok: return t, rp, cpm
    raise AssertionError
GRP = [decomp(p) for p, s in elems]
print('stabilizer elements decomposed', len(GRP), 'transposing', sum(1 for t, _, _ in GRP if t))
def realizers(OR, cands, u, relaxed):
    out = set()
    for key in cands:
        form, (m, n), cp, rows = key
        Pf, per = per_group(OR, key, relaxed)
        if Pf is None or not on_flat(Pf, u): continue
        opts = [[sb for sb, F in L if on_flat(F, u)] for L in per]
        for combo in itertools.product(*opts):
            threads = frozenset(frozenset([rows[0][a]] + [rows[b + 1][combo[b][a]] for b in range(n - 1)]) for a in range(m))
            out.add((form, (m, n), frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows)), threads))
    return out
def img(g, x):
    t, rp, cpm = g; form, mn, blocks, classes, threads = x
    # column form: blocks are column sets, classes/threads row sets; row form: the roles on H^T
    if form == 'column': colmap, rowmap = cpm, rp
    else: colmap, rowmap = rp, cpm
    nb = frozenset(frozenset(colmap[j] for j in B) for B in blocks)
    nc = frozenset(frozenset(rowmap[i] for i in C) for C in classes)
    nt = frozenset(frozenset(rowmap[i] for i in T) for T in threads)
    nform = form if not t else ('row' if form == 'column' else 'column')
    return (nform, mn, nb, nc, nt)
SIGU = (ONE, ONE, ONE)
for relaxed, lab in ((False, 'strict'), (True, 'relaxed')):
    X = realizers(H3OR, H3C, SIGU, relaxed)
    closed = all(img(g, x) in X for g in GRP for x in X)
    seen = set(); orbits = []
    for x in X:
        if x in seen: continue
        orb = {img(g, x) for g in GRP}; seen |= orb; orbits.append(orb)
    parts = {(x[0], x[1], x[2], x[3]) for x in X}
    porb = set()
    pseen = set(); pcount = 0
    for p in parts:
        if p in pseen: continue
        o = {img(g, p + (frozenset(),))[:4] for g in GRP}; pseen |= o; pcount += 1
    print('SIG %s: realizing (partition, alignment) pairs %d, closed under the stabilizer %s, factorization classes %d; partition structures %d in %d stabilizer orbits' % (lab, len(X), closed, len(orbits), len(parts), pcount))
    print('   class sizes', sorted(len(o) for o in orbits))
    G0 = [g for g in GRP if not g[0]]
    seen = set(); n0 = 0
    for x in X:
        if x in seen: continue
        seen |= {img(g, x) for g in G0}; n0 += 1
    pseen = set(); p0 = 0
    for p in parts:
        if p in pseen: continue
        pseen |= {img(g, p + (frozenset(),))[:4] for g in G0}; p0 += 1
    print('   under the transpose-free subgroup (order %d): factorization classes %d, partition-structure orbits %d' % (len(G0), n0, p0))
