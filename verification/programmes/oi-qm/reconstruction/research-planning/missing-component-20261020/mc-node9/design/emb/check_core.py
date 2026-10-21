"""Controls for emb_core (exact).  §A.21: the support formula is checked against an independent
forward simulation of explicit states (no matrix powers, no rank algebra), for every graph on
n <= 4 sites, every region, every toy site, every clean declaration, t <= 6, final-memory and
full-history (K-EXTHIST) records, and for every assignment of the clean values at n <= 3 (all-0 and
all-1 at n = 4) (program
independence: the clean values are the embedded controller's 'program' in E2).
Also: isomorphism-class counts against OEIS A000088 (1, 2, 4, 11, 34, 156)."""
from itertools import product, combinations
from emb_core import (lattice_update, vis_coords, clean_coords, mask_of, post_rank, prior_rank,
                      iso_graphs, toy_rows)
from f2 import compose, identity, apply, rank


def brute(n, edges, R, toy, decl, T, clean_vals):
    M = lattice_update(n, edges)
    vc = vis_coords(n, R)
    K = clean_coords(n, R, decl)
    unk = [c for c in range(2 * n) if c not in K]
    fin = [dict() for _ in range(T + 1)]
    his = [dict() for _ in range(T + 1)]
    for vals in product((0, 1), repeat=len(unk)):
        s = 0
        for v, c in zip(vals, unk):
            s |= v << c
        for v, c in zip(clean_vals, K):
            s |= v << c
        hist = [tuple((s >> c) & 1 for c in vc)]
        for t in range(1, T + 1):
            s = apply(M, s)
            vis = tuple((s >> c) & 1 for c in vc)
            hist.append(vis)
            tv = ((s >> toy) & 1, (s >> (n + toy)) & 1)
            fin[t].setdefault(vis, set()).add(tv)
            his[t].setdefault(tuple(hist), set()).add(tv)
    return fin, his


def formula(n, edges, R, toy, decl, T):
    M = lattice_update(n, edges)
    vc = vis_coords(n, R)
    um = ((1 << (2 * n)) - 1) & ~mask_of(clean_coords(n, R, decl))
    P = identity(2 * n)
    hist = [P[c] for c in vc]
    out = []
    for t in range(1, T + 1):
        P = compose(M, P)
        F = [P[c] for c in vc]
        hist = hist + F
        Tt = toy_rows(P, n, toy)
        out.append((post_rank(F, Tt, um), post_rank(hist, Tt, um), rank([f & um for f in F]),
                    rank([f & um for f in hist])))
    return out


cases = 0
bad = 0
for n in (2, 3, 4):
    pairs = list(combinations(range(n), 2))
    for gm in range(1 << len(pairs)):
        edges = tuple(pairs[i] for i in range(len(pairs)) if (gm >> i) & 1)
        for r in range(1, n):
            for R in combinations(range(n), r):
                for toy in [x for x in range(n) if x not in R]:
                    for decl in ("FULL", "U", "V", "NONE"):
                        K = clean_coords(n, R, decl)
                        F = formula(n, edges, R, toy, decl, 6)
                        cvs = list(product((0, 1), repeat=len(K))) if n <= 3 else [tuple(0 for _ in K), tuple(1 for _ in K)]
                        for cv in cvs:
                            fin, his = brute(n, edges, R, toy, decl, 6, cv)
                            for t in range(1, 7):
                                pf, ph, rf, rh = F[t - 1]
                                okf = {len(v) for v in fin[t].values()} == {2 ** pf} and len(fin[t]) == 2 ** rf
                                okh = {len(v) for v in his[t].values()} == {2 ** ph} and len(his[t]) == 2 ** rh
                                cases += 1
                                if not (okf and okh):
                                    bad += 1
print(f"formula vs forward brute force (n=2,3 all clean values; n=4 clean values all-0 and all-1;"
      f" all graphs, regions, toys, declarations, t<=6, final and history): {cases} cases, {bad} mismatches")
counts = [len(iso_graphs(n)) for n in range(1, 7)]
print("isomorphism classes n=1..6:", counts, "expected [1, 2, 4, 11, 34, 156]:",
      "PASS" if counts == [1, 2, 4, 11, 34, 156] else "FAIL")
print("CORE CONTROLS:", "GREEN" if bad == 0 and counts == [1, 2, 4, 11, 34, 156] else "RED")
