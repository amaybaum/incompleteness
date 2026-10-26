# Spot-check: passive linear-filter observers rho_x(v) = A v + x b, m=3, every chi, in admissible cells.
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from search import tables, counts, chi_hits, windows
from indep import gen, Z_of
def gl(m):
    M = 1 << m; mats = []
    for cols in itertools.product(range(1, M), repeat=m):
        span = {0}
        ok = True
        for c in cols:
            if c in span: ok = False; break
            span |= {s ^ c for s in span}
        if ok: mats.append(cols)
    return mats
def apply(cols, v):
    r = 0
    for i, c in enumerate(cols):
        if (v >> i) & 1: r ^= c
    return r
def plin_obs(m):
    M = 1 << m; obs = []
    for A in gl(m):
        for b in range(M):
            r0 = tuple(apply(A, v) for v in range(M)); r1 = tuple(apply(A, v) ^ b for v in range(M))
            obs.append((r0, r1, (0,) * M))
    return obs
m = 3; obs = plin_obs(m); print('plin m=3 observers', len(obs))
cells = [('clk', 5, 7, 7), ('lin', 7, 11, 15), ('filt', 7, 9, 15), ('clk', 7, 8, 15), ('lin', 8, 12, 31), ('filt', 8, 10, 31), ('clk', 8, 9, 31)]
for name, n, lo, hi in cells:
    s0, s1, f = tables(name, n); N = 2 << n
    out = counts(m, obs, s0, s1, f, n, hi)
    H, chis = chi_hits(out, m)
    res = {}
    for K in range(lo, hi + 1):
        ab, sg = windows(H, N, K)
        if ab.any(): res[K] = (int(ab.sum()), int(sg.sum()))
    print(name, n, 'K in', [lo, hi], 'windows (abs, signed):', res, flush=True)
