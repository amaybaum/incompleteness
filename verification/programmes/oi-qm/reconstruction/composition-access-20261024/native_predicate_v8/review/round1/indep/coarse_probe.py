"""Reviewer probe (outside the v8 class): could a COARSER read of one native cell
(a predicate g(V, w) of a single whole triple, or one fixed linear bit of it)
carry the accepted law? Usage: python3 -I -B coarse_probe.py <rederive.py> seed..."""
import sys, importlib.util
from itertools import combinations
spec = importlib.util.spec_from_file_location('rd', sys.argv[1]); rd = importlib.util.module_from_spec(spec); spec.loader.exec_module(rd)
def fam(seed):
    prev, cur = rd.background(seed)
    for f in rd.src: cur.pop(f, None)
    F = rd.evolve_all(prev, cur)
    get = lambda t, x: F[t][x[0]+4, x[1]+4, x[2]+4, :].tolist()
    p = get(rd.n, (0,0,0))[0]; s = p >> 1 & 1
    V = get(rd.n+2, (0,0,0)); q8 = get(rd.n+1, (0,0,-1)); q10 = get(rd.n+1, (0,0,1))
    J = [4*(a>>1&1) + 2*(b&1) + (b>>1&1) for a, b in zip(q8, q10)]
    nn = {(0,0):5,(0,1):0,(1,0):4,(1,1):1}
    t1 = tuple(nn[(y^s, r^s)] for y in (0,1) for r in (0,1) for z in (0,1))
    byv = {v: [l for l in range(512) if V[l] == v] for v in range(8)}
    return get, J, t1, byv
for seed in map(int, sys.argv[2:]):
    get, J, t1, byv = fam(seed)
    per_cell_all_v = 0; cells_some_v = 0; linear_bit_cells = 0; total = 0
    for t in range(-1, rd.tend+1):
        for x in rd.region:
            vals = get(t, x)
            if len(set(vals)) == 1: continue
            total += 1
            okv = []
            for v in range(8):
                cls = {}
                for l in byv[v]:
                    cls.setdefault(vals[l], [0]*8)[J[l]] += 1
                cs = list(cls.values()); found = False
                for k in range(1, len(cs)):
                    for sub in combinations(range(len(cs)), k):
                        if tuple(sum(cs[i][j] for i in sub) for j in range(8)) == t1:
                            found = True; break
                    if found: break
                okv.append(found)
            per_cell_all_v += all(okv); cells_some_v += any(okv)
            # one fixed linear bit c.w (c in 1..7), predicate may flip with V
            for c in range(1, 8):
                good = True
                for v in range(8):
                    cnt = [[0]*8, [0]*8]
                    for l in byv[v]:
                        cnt[bin(vals[l] & c).count('1') & 1][J[l]] += 1
                    if tuple(cnt[0]) != t1 and tuple(cnt[1]) != t1: good = False; break
                if good: linear_bit_cells += 1; break
    print(seed, 'G-dependent cells', total, 'cells with a law-good coarsening for every V', per_cell_all_v,
          'for some V', cells_some_v, 'cells with a law-good fixed linear bit', linear_bit_cells)
