"""Independent recount of the multi-target table (own algebra; graph representatives from the
reviewed iso_graphs) and a check of the r = m necessary condition in every learnt r = m case:
with g = psi(g) + kappa(g) (psi(g) in the current visible span, kappa(g) in the clean span),
the form omega(kappa g, kappa g') must equal omega(g, g') + omega(psi g, psi g') and be
non-degenerate."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from emb_core import iso_graphs
from itertools import combinations
from collections import Counter
from indep import *


def solve(target, basis):
    piv = {}
    for i, b in enumerate(basis):
        v, c = b, 1 << i
        while v:
            h = v.bit_length() - 1
            if h in piv:
                pv, pc = piv[h]; v ^= pv; c ^= pc
            else:
                piv[h] = (v, c); break
    v, c = target, 0
    while v:
        h = v.bit_length() - 1
        if h not in piv: return None
        pv, pc = piv[h]; v ^= pv; c ^= pc
    return c


tab = Counter(); bad = 0; chk = 0
for n in range(2, 7):
    for edges in iso_graphs(n):
        M = upd(n, adj_from_edges(n, edges)); per = period(M)
        pw = [ident(2 * n)]
        for t in range(1, per): pw.append(mul(M, pw[-1]))
        for r in range(1, n):
            for R in combinations(range(n), r):
                Kv = [1 << x for x in R] + [1 << (n + x) for x in R]
                um = (1 << 2 * n) - 1
                for k in Kv: um &= ~k
                H = [x for x in range(n) if x not in R]
                for m in range(1, len(H) + 1):
                    for S in combinations(H, m):
                        tab[(r, m, "cases")] += 1
                        for t in range(1, per):
                            P = pw[t]; F = [P[x] for x in R] + [P[n + x] for x in R]
                            T = [P[x] for x in S] + [P[n + x] for x in S]
                            if prior_exp(T, um) == 2 * m and support_exp(F, T, um) == 0:
                                tab[(r, m, "learnt")] += 1
                                if r == m:
                                    chk += 1
                                    ks, ps = [], []
                                    for g in T:
                                        c = solve(g, F + Kv)
                                        k = 0; p = 0
                                        for i in range(len(F)):
                                            if (c >> i) & 1: p ^= F[i]
                                        for i in range(len(Kv)):
                                            if (c >> (len(F) + i)) & 1: k ^= Kv[i]
                                        assert p ^ k == g
                                        ks.append(k); ps.append(p)
                                    N = 2 * m
                                    G = [[om(ks[i], ks[j], n) for j in range(N)] for i in range(N)]
                                    A = [[om(T[i], T[j], n) for j in range(N)] for i in range(N)]
                                    B = [[om(ps[i], ps[j], n) for j in range(N)] for i in range(N)]
                                    same = all(G[i][j] == (A[i][j] ^ B[i][j]) for i in range(N) for j in range(N))
                                    nondeg = rk([sum(G[i][j] << j for j in range(N)) for i in range(N)]) == N
                                    if not (same and nondeg): bad += 1
                                break
for r in range(1, 6):
    for m in range(1, 6):
        if tab[(r, m, "cases")]:
            print(f"r={r} m={m}: cases {tab[(r, m, 'cases')]}, learnt {tab[(r, m, 'learnt')]}")
print(f"r = m learnt cases checked for omega(kg,kg') = omega(g,g') + omega(pg,pg') and non-degeneracy: {chk}, failures {bad}")
