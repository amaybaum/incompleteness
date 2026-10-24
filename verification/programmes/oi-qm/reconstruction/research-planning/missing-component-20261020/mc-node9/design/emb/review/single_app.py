"""Single-apparatus (exactly one visible site adjacent to the hidden sector) FULL learning cases,
n <= 6 (graph representatives from the reviewed iso_graphs, algebra from indep): the maximum,
over learning times in one period, of the toy's own-content rank; split by hidden neighbour."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from emb_core import iso_graphs
from itertools import combinations
from collections import Counter
from indep import *
c = Counter(); ex = {}
for n in range(3, 7):
    for edges in iso_graphs(n):
        M = upd(n, adj_from_edges(n, edges)); per = period(M)
        pw = [ident(2 * n)]
        for t in range(1, per): pw.append(mul(M, pw[-1]))
        for r in range(2, n):
            for R in combinations(range(n), r):
                Rs = set(R)
                inner = {a for e in edges for a in e if a in Rs and not set(e) <= Rs}
                if len(inner) != 1: continue
                um = (1 << 2 * n) - 1
                for x in R: um &= ~((1 << x) | (1 << (n + x)))
                for toy in range(n):
                    if toy in Rs: continue
                    bath = any((toy in e) and (set(e) - {toy}).isdisjoint(Rs) for e in edges)
                    best = None
                    for t in range(1, per):
                        P = pw[t]; F = [P[x] for x in R] + [P[n + x] for x in R]; T = [P[toy], P[n + toy]]
                        if prior_exp(T, um) == 2 and support_exp(F, T, um) == 0:
                            own = rk([g & ((1 << toy) | (1 << (n + toy))) for g in T])
                            best = own if best is None else max(best, own)
                    if best is not None:
                        c[(n, bath, best)] += 1
                        ex.setdefault((bath, best), (n, edges, R, toy))
for k in sorted(c): print(f"n={k[0]} toy-has-hidden-neighbour={k[1]} max own-content rank over learning times {k[2]}: {c[k]}")
print({k: v for k, v in ex.items()})
