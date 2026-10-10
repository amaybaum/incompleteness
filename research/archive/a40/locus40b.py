"""A39 Dita-locus measurement, step 3 (read-only, exact). Reuses step 1's pair-block loci and step 2's closure.

For every (orientation, block size n, column subset S, row pair) the pair-block locus is an id: -1 empty, 0 the whole torus,
or 1 + the index of one of the proper base loci. At a generic point of a flat F of the closure, a pair is proportional on S
exactly when its locus is T^3 or contains F; the containment pattern of F (the set of base loci containing it) therefore
determines every candidate structure at F. Candidates are found once per distinct pattern; each distinct candidate is then
given its exact locus: the intersection of all its proportionality and rank-one characters (strict), and of its
proportionality and relaxed rank-one characters (up to diagonal equivalence)."""
import itertools, json, os, pickle, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flats import Flat, Empty, TORUS, V0, vadd, vsub
S_ = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(S_, 'probe38_landed.py'), encoding='utf-8').read()
NS = {'__name__': 'h'}; exec(compile(src[:src.index("print('== 1. realizability")], 'h', 'exec'), NS)
SIGE, EA, EB, EC, SHAPES = NS['SIGE'], NS['EA'], NS['EB'], NS['EC'], NS['SHAPES']
t0 = time.time()
K = [[(EA(i, j), EB(i, j), EC(i, j)) for j in range(16)] for i in range(16)]
CST = [[SIGE[i][j] for j in range(16)] for i in range(16)]
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def kadd(a, b): return tuple(x + y for x, y in zip(a, b))
ORIENT = {'column': (K, CST), 'row': ([list(c) for c in zip(*K)], [list(c) for c in zip(*CST)])}
PAIRS = list(itertools.combinations(range(16), 2))
PIDX = {p: t for t, p in enumerate(PAIRS)}

# ---- the pair-block locus table ---------------------------------------------------------------------------------
cache = {}
def pair_block_flat(vals):
    if vals in cache: return cache[vals]
    d0, e0 = vals[0]
    try:
        F = TORUS
        for d, e in vals[1:]: F = F.add(ksub(d, d0), vsub(e0, e))
        r = F
    except Empty:
        r = None
    cache[vals] = r
    return r
BASE = {}          # flat -> id (>= 1)
SUBSETS = {n: list(itertools.combinations(range(16), n)) for n in (2, 4, 8)}
TABLE = {}         # (form, n) -> int32 array [numS, 120]
for form, (Km, Cm) in ORIENT.items():
    de = {p: [(ksub(Km[p[0]][j], Km[p[1]][j]), vsub(Cm[p[0]][j], Cm[p[1]][j])) for j in range(16)] for p in PAIRS}
    for n in (2, 4, 8):
        T = np.full((len(SUBSETS[n]), 120), -1, dtype=np.int32)
        for s, Sb in enumerate(SUBSETS[n]):
            for t, p in enumerate(PAIRS):
                F = pair_block_flat(tuple(sorted(set(de[p][j] for j in Sb))))
                if F is None: continue
                if F.rank() == 0: T[s, t] = 0; continue
                if F not in BASE: BASE[F] = len(BASE) + 1
                T[s, t] = BASE[F]
        TABLE[(form, n)] = T
BASEL = [None] * (len(BASE) + 1)
for F, i in BASE.items(): BASEL[i] = F
print('table built: %d base loci  %.0fs' % (len(BASE), time.time() - t0), flush=True)

# ---- the closure and the containment patterns ---------------------------------------------------------------------
closure = [Flat.of(B) for B in pickle.load(open(os.path.join(S_, 'closure40.pkl'), 'rb'))]
assert set(closure) >= set(BASE), 'closure does not contain the base loci'
patterns = {}
for F in [TORUS] + closure:
    pat = frozenset(i for i in range(1, len(BASEL)) if BASEL[i].contains(F))
    patterns.setdefault(pat, []).append(F)
print('patterns: %d distinct over %d flats (with T^3)  %.0fs' % (len(patterns), len(closure) + 1, time.time() - t0), flush=True)

# ---- candidate search per pattern ---------------------------------------------------------------------------------
PI = np.array([p[0] for p in PAIRS]); PJ = np.array([p[1] for p in PAIRS])
def good_subsets(form, n, prop):
    """prop: bool [numS, 120]; returns {S: sorted classes} for subsets whose proportionality classes all have size m"""
    m = 16 // n
    deg = np.zeros((prop.shape[0], 16), dtype=np.int32)
    np.add.at(deg, (slice(None), PI), prop.astype(np.int32)) if False else None
    deg = prop.astype(np.int32) @ INC            # [numS, 16] number of proportional partners of each row
    ok = np.all(deg == m - 1, axis=1)
    out = {}
    for s in np.flatnonzero(ok):
        # classes by union of partners (transitive generically on a flat)
        cls = {}
        seen = set()
        pr = prop[s]
        adj = {i: [i] for i in range(16)}
        for t in np.flatnonzero(pr):
            a, b = PAIRS[t]; adj[a].append(b)
        for i in range(16):
            if i in seen: continue
            c = tuple(sorted(adj[i])); seen |= set(c); cls[c] = 1
        if all(len(c) == m for c in cls):
            out[SUBSETS[n][s]] = sorted(cls)
    return out
INC = np.zeros((120, 16), dtype=np.int32)
for t, (a, b) in enumerate(PAIRS): INC[t, a] = 1; INC[t, b] = 1
def tilings(good, m, n):
    parts = []
    keys = list(good)
    def rec(rem, chosen):
        if not rem: parts.append(tuple(chosen)); return
        first = min(rem)
        for Sb in keys:
            if first in Sb and set(Sb) <= rem: rec(rem - set(Sb), chosen + [Sb])
    rec(set(range(16)), [])
    out = []
    for cp in parts:
        cls = {i: tuple(next(ci for ci, cl in enumerate(good[Sb]) if i in cl) for Sb in cp) for i in range(16)}
        groups = {}
        for i in range(16): groups.setdefault(cls[i], []).append(i)
        rows = sorted(tuple(v) for v in groups.values())
        if all(len(g) == m for g in rows): out.append((cp, tuple(rows)))
    return out
PATS = list(patterns)
def search_pattern(pat):
    ids = np.array(sorted(pat | {0}), dtype=np.int32)
    found = set()
    for form in ORIENT:
        for (m, n) in SHAPES:
            prop = np.isin(TABLE[(form, n)], ids)
            good = good_subsets(form, n, prop)
            if not good: continue
            for cp, rows in tilings(good, m, n):
                found.add((form, (m, n), cp, rows))
    return found
def worker(lo_hi):
    lo, hi = lo_hi
    out = set()
    for k in range(lo, hi):
        out |= search_pattern(PATS[k])
    return out
if __name__ == '__main__':
    cands = set()
    for d, k in enumerate(range(0, len(PATS), 100)):
        cands |= worker((k, min(k + 100, len(PATS))))
        if d % 10 == 0: print('  chunks %d, candidates so far %d  %.0fs' % (d + 1, len(cands), time.time() - t0), flush=True)
    print('candidates: %d distinct structures over all patterns  %.0fs' % (len(cands), time.time() - t0), flush=True)

    # ---- exact loci -------------------------------------------------------------------------------------------------------
    def conditions(form, mn, cp, rows, relaxed=False):
        Km, Cm = ORIENT[form]; m, n = mn
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
                    if not relaxed:
                        out.append(div(lam[(a, b, c)], mul(lam[(a, 0, c)], lam[(0, b, c)])))
                    elif c > 0:
                        out.append(div(div(lam[(a, b, c)], lam[(a, 0, c)]), div(lam[(a, b, 0)], lam[(a, 0, 0)])))
        return out
    def locus(conds):
        """the flat where every character u^k c equals 1, i.e. u^k = -c additively; None if empty"""
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
    print('search done  %.0fs' % (time.time() - t0), flush=True)
    res = []
    for cand in sorted(cands):
        form, mn, cp, rows = cand
        Fs = locus(conditions(form, mn, cp, rows)); Fr = locus(conditions(form, mn, cp, rows, relaxed=True))
        res.append((cand, None if Fs is None else Fs.B, None if Fr is None else Fr.B))
    pickle.dump({'res': res, 'npatterns': len(patterns), 'nbase': len(BASE), 'nclosure': len(closure)}, open(os.path.join(S_, 'locus40.pkl'), 'wb'))
    print('loci computed for %d candidates  %.0fs' % (len(res), time.time() - t0), flush=True)
