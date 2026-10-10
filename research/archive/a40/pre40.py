import itertools, time, numpy as np
from named40 import SIGE, EA, EB, EC
from flats import Flat, Empty, TORUS, V0, vsub
t0 = time.time()
K = [[(EA(i, j), EB(i, j), EC(i, j)) for j in range(16)] for i in range(16)]
CST = [[SIGE[i][j] for j in range(16)] for i in range(16)]
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
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
for form, (Km, Cm) in ORIENT.items():
    de = {p: [(ksub(Km[p[0]][j], Km[p[1]][j]), vsub(Cm[p[0]][j], Cm[p[1]][j])) for j in range(16)] for p in PAIRS}
    for m, n in ((4, 4), (8, 2), (2, 8)):
        tot = ok = 0; maxids = 0
        for S in itertools.combinations(range(16), n):
            tot += 1
            deg0 = [0] * 16; ids = 0
            for p in PAIRS:
                F = pbf(tuple(sorted(set(de[p][j] for j in S))))
                if F is None: continue
                if F.rank() == 0: deg0[p[0]] += 1; deg0[p[1]] += 1
                else: ids += 1
            if max(deg0) <= m - 1: ok += 1; maxids = max(maxids, ids)
        print(form, (m, n), 'subsets', tot, 'pass generic-degree filter', ok, 'max nontrivial pairs', maxids, '%.0fs' % (time.time() - t0), flush=True)
