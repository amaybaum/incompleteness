"""Memory budget for complete learning (E1/E2, exact).  Pressure test of the one-pair lemma.

Lemma (report §3.2).  If the final map is symplectic, the memory is r visible sites with both
coordinates clean, every other coordinate uniform, and the target is m hidden sites whose current
state is a priori uniform (prior rank 2m), then the target is determined by the final memory
only if the form v -> omega(v, (I + B*B) v') is non-degenerate (B: memory -> target the
read-off map); for r = m = 1 this is impossible.
Here: for every graph up to isomorphism on n <= NMAX sites, every region R with |R| = r, every
set S of m hidden sites (the target), every t in one period: is S completely learnt (posterior
support 1 with prior support 2^(2m))?  Tabulated by (r, m).
"""
import sys
from itertools import combinations
from collections import Counter
from emb_core import lattice_update, vis_coords, mask_of, post_rank, prior_rank, iso_graphs, order
from f2 import compose, identity

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
tab = Counter()
first = {}
for n in range(2, NMAX + 1):
    for edges in iso_graphs(n):
        M = lattice_update(n, edges)
        om = order(M)
        pw = [identity(2 * n)]
        for t in range(1, om):
            pw.append(compose(M, pw[-1]))
        for r in range(1, n):
            for R in combinations(range(n), r):
                vc = vis_coords(n, R)
                um = ((1 << (2 * n)) - 1) & ~mask_of(vc)
                H = [x for x in range(n) if x not in R]
                for m in range(1, len(H) + 1):
                    for S in combinations(H, m):
                        hit = None
                        for t in range(1, om):
                            P = pw[t]
                            F = [P[c] for c in vc]
                            T = [P[x] for x in S] + [P[n + x] for x in S]
                            if prior_rank(T, um) == 2 * m and post_rank(F, T, um) == 0:
                                hit = t
                                break
                        tab[(r, m, "cases")] += 1
                        if hit is not None:
                            tab[(r, m, "learnt")] += 1
                            if (r, m) not in first or (n, hit) < first[(r, m)][:2]:
                                first[(r, m)] = (n, hit, edges, R, S)
    print(f"n <= {n} done", flush=True)
for r in range(1, NMAX):
    for m in range(1, NMAX):
        if tab[(r, m, "cases")]:
            f = first.get((r, m))
            print(f"memory pairs r={r} target pairs m={m}: cases {tab[(r, m, 'cases')]}, completely learnt with uniform prior: "
                  f"{tab[(r, m, 'learnt')]}" + (f"   first: n={f[0]} t={f[1]} edges={f[2]} R={f[3]} target={f[4]}" if f else ""))
