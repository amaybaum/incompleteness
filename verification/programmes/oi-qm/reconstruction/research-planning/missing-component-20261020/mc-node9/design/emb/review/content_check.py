"""For every FULL learning-type point mass (posterior 1, prior 4) at its first time: how much of
the toy's OWN initial content is in its current state?  own = rank of the current toy functionals
restricted to the toy's initial coordinates (2: own content intact up to invertible mixing; 0: the
toy has been replaced by other unknown content).  Labelled simple graphs, n <= 5; also split by
whether the toy has a hidden neighbour."""
from itertools import combinations
from collections import Counter
from indep import *
c = Counter(); ex = {}
for n in (3, 4, 5):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if (mask >> i) & 1]
        M = upd(n, adj_from_edges(n, edges)); per = period(M)
        pw = [ident(2 * n)]
        for t in range(1, per): pw.append(mul(M, pw[-1]))
        for r in range(1, n):
            for R in combinations(range(n), r):
                um = (1 << 2 * n) - 1
                for x in R: um &= ~((1 << x) | (1 << (n + x)))
                for toy in range(n):
                    if toy in R: continue
                    bath = any((toy in e) and (set(e) - {toy}).isdisjoint(R) for e in edges)
                    for t in range(1, per):
                        P = pw[t]; F = [P[x] for x in R] + [P[n + x] for x in R]; T = [P[toy], P[n + toy]]
                        if prior_exp(T, um) == 2 and support_exp(F, T, um) == 0:
                            own = rk([g & ((1 << toy) | (1 << (n + toy))) for g in T])
                            c[(r, bath, own)] += 1
                            ex.setdefault((r, bath, own), (n, edges, R, toy, t))
                            break
for k in sorted(c): print(f"|R|={k[0]} toy-has-hidden-neighbour={k[1]} own-content rank {k[2]}: {c[k]} cases; e.g. {ex[k]}")
