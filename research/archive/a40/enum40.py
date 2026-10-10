"""A40 completeness, second method (no closure): a Dita structure (column blocks cp, row classes P, shape m x n) admitted at u
has every within-class row pair proportional at u on every block, so u lies in the pair-block locus of each such pair; hence
(cp, P) has a nonempty joint proportionality locus. Enumerate: per block S, the partitions P of the 16 rows into classes of
size m all of whose within-class pairs have a common point on S; per P, the exact covers of the 16 columns by m blocks with a
common point. Every admitted structure is among the results; the exact strict / relaxed loci then decide."""
import itertools, time, pickle
from named40 import SIGE, EA, EB, EC
from flats import Flat, Empty, TORUS, V0, vsub, vadd
t0 = time.time()
K = [[(EA(i, j), EB(i, j), EC(i, j)) for j in range(16)] for i in range(16)]
CST = [[SIGE[i][j] for j in range(16)] for i in range(16)]
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def kadd(a, b): return tuple(x + y for x, y in zip(a, b))
ORIENT = {'column': (K, CST), 'row': ([list(c) for c in zip(*K)], [list(c) for c in zip(*CST)])}
PAIRS = list(itertools.combinations(range(16), 2))
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
def meet(F, G):
    try: return F.meet(G)
    except Empty: return None
def clique_partitions(m, loc):
    """loc: dict pair -> flat (only pairs with a nonempty locus); partitions of range(16) into classes of size m with all
    within-class pairs in loc and a common point; returns list of (classes, flat)"""
    out = []
    def rec(rem, classes, F):
        if not rem: out.append((tuple(classes), F)); return
        i = min(rem)
        nb = sorted(j for j in rem if j != i and (i, j) in loc)
        for rest in itertools.combinations(nb, m - 1):
            cl = (i,) + rest
            G = F
            for a, b in itertools.combinations(cl, 2):
                G = meet(G, loc[(a, b)])
                if G is None: break
            if G is None: continue
            rec(rem - set(cl), classes + [cl], G)
    rec(frozenset(range(16)), [], TORUS)
    return out
cands = {}
timing = {}
for form, (Km, Cm) in ORIENT.items():
    de = {p: [(ksub(Km[p[0]][j], Km[p[1]][j]), vsub(Cm[p[0]][j], Cm[p[1]][j])) for j in range(16)] for p in PAIRS}
    for m, n in ((4, 4), (8, 2), (2, 8)):
        t1 = time.time()
        good = {}   # P -> list of (S, flat)
        for S in itertools.combinations(range(16), n):
            loc = {}
            for p in PAIRS:
                F = pbf(tuple(sorted(set(de[p][j] for j in S))))
                if F is not None: loc[p] = F
            for P, F in clique_partitions(m, loc):
                good.setdefault(P, []).append((S, F))
        nblocks = sum(len(v) for v in good.values())
        found = 0
        for P, blocks in good.items():
            def rec(rem, chosen, F):
                global found
                if not rem:
                    cp = tuple(sorted(chosen)); cands[(form, (m, n), cp, P)] = F; return
                first = min(rem)
                for S, G in blocks:
                    if S[0] == first and set(S) <= rem:
                        H = meet(F, G)
                        if H is not None: rec(rem - set(S), chosen + [S], H)
            rec(frozenset(range(16)), [], TORUS)
        timing[(form, m, n)] = time.time() - t1
        print(form, (m, n), 'row partitions', len(good), 'good blocks', nblocks, 'candidates so far', len(cands), '%.1fs' % timing[(form, m, n)], flush=True)
print('enumeration: %d candidate structures (joint proportionality locus nonempty)  %.1fs' % (len(cands), time.time() - t0), flush=True)
pickle.dump({k: v.B for k, v in cands.items()}, open('enum40.pkl', 'wb'))
