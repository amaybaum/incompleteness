"""Independent recount of 'persist' (visible cells at t determine the toy's INITIAL state while the
current toy has posterior support >= 2), all labelled simple graphs n <= 5, every region, toy, t."""
from itertools import combinations
from collections import Counter
from indep import *
c = Counter(); first = {}
for n in (2, 3, 4, 5):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if (mask >> i) & 1]
        M = upd(n, adj_from_edges(n, edges)); per = period(M)
        pw = [ident(2 * n)]
        for t in range(1, per): pw.append(mul(M, pw[-1]))
        for r in range(1, n):
            for R in combinations(range(n), r):
                for decl in ("FULL", "U", "V", "NONE"):
                    K = {"FULL": list(R) + [n + x for x in R], "U": list(R), "V": [n + x for x in R], "NONE": []}[decl]
                    um = (1 << 2 * n) - 1
                    for k in K: um &= ~(1 << k)
                    for toy in range(n):
                        if toy in R: continue
                        hit = None
                        for t in range(1, per):
                            P = pw[t]; F = [P[x] for x in R] + [P[n + x] for x in R]
                            if support_exp(F, [1 << toy, 1 << (n + toy)], um) == 0 and support_exp(F, [P[toy], P[n + toy]], um) > 0:
                                hit = t; break
                        c[(n, decl, r, "cases")] += 1
                        if hit:
                            c[(n, decl, r, "persist")] += 1
                            first.setdefault((decl,), (n, r, edges, R, toy, hit))
for k in sorted(c):
    if k[3] == "persist": print(k[:3], "persist", c[k], "of", c[k[:3] + ("cases",)])
print("FULL persist total:", sum(v for k, v in c.items() if k[1] == "FULL" and k[3] == "persist"))
print("first:", first)
# the case the published output names as the first FULL persist instance
n = 5; edges = [(0, 1), (0, 3), (0, 4), (1, 2)]; R = (2, 3); toy = 1
M = upd(n, adj_from_edges(n, edges)); P = ident(2 * n)
um = (1 << 2 * n) - 1
for k in list(R) + [n + x for x in R]: um &= ~(1 << k)
for t in range(1, 8):
    P = mul(M, P); F = [P[x] for x in R] + [P[n + x] for x in R]
    print(f"  named case t={t}: initial-toy support 2^{support_exp(F, [1 << toy, 1 << (n + toy)], um)}, current-toy support 2^{support_exp(F, [P[toy], P[n + toy]], um)}, prior 2^{prior_exp([P[toy], P[n + toy]], um)}")
