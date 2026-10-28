#!/usr/bin/env python3
"""Gap (ii) Part A probe on map (a), exhaustive: T(u,v) = (v,u).
  G1 T F T = F^{-1} on all states (SM 5 identity)            G2 E(T z) = E(z) on all states (A symmetric)
  G3 hence rho_shell o T = rho_shell for the uniform shell measure (follows from G2, no ergodicity used)
  G4 per cycle C: is T(C) = C ?  (rho_C o T = rho_C iff T(C) = C); count self-conjugate cycles per shell."""
import itertools, math
import numpy as np

def adjacency(d, L):
    N = L**d; A = np.zeros((N, N), dtype=np.int64)
    coords = list(itertools.product(range(L), repeat=d)); ix = {c: i for i, c in enumerate(coords)}
    for c in coords:
        for k in range(d):
            for s in (1, -1):
                c2 = list(c); c2[k] = (c2[k] + s) % L; A[ix[c], ix[tuple(c2)]] += 1
    return A
def digits(idx, n, q):
    out = np.empty((n, idx.size), np.int64); t = idx.copy()
    for i in range(n): out[i] = t % q; t //= q
    return out
def index_of(z, q): return (z * (q ** np.arange(z.shape[0], dtype=np.int64))[:, None]).sum(0)
def cycle_labels(P):
    lab = np.arange(P.size); Q = P.copy()
    for _ in range(int(math.ceil(math.log2(P.size))) + 1): lab = np.minimum(lab, lab[Q]); Q = Q[Q]
    return lab

for d, L, q in ((1, 5, 3), (1, 4, 5)):
    N = L**d; n = 2 * N; S = q**n; A = adjacency(d, L)
    z = digits(np.arange(S, dtype=np.int64), n, q); u, v = z[:N], z[N:]
    P = index_of(np.vstack([v, (A @ v - u) % q]), q)
    Tm = index_of(np.vstack([v, u]), q)
    Pinv = np.empty_like(P); Pinv[P] = np.arange(S)
    g1 = bool(np.all(Tm[P[Tm]] == Pinv))
    E = ((u * u).sum(0) + (v * v).sum(0) - (u * (A @ v)).sum(0)) % q
    g2 = bool(np.all(E[Tm] == E))
    lab = cycle_labels(P); reps = np.unique(lab)
    selfc = lab[Tm] == lab                       # T maps x's cycle to the cycle of T x
    print(f"map (a) d={d} L={L} q={q}: G1 TFT=F^-1 {g1}; G2 E o T = E {g2} (=> uniform shell measure T-invariant)")
    for e in range(q):
        r = reps[E[reps] == e]
        sc = int(np.sum(selfc[r]))
        print(f"  shell E={e}: cycles {r.size}, T-self-conjugate cycles {sc}, cycles with T(C) != C {r.size - sc}")
