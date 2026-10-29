#!/usr/bin/env python3
"""Hidden-assumption probe for SM :292 / :795 ("Gaussian on energy shell", sphere-Gaussian projection).
Map (a) conserves E only mod q. Exhaustively, for each mod-q shell {E = e}, compare the uniform-on-shell
marginal law of (x_0(t)) and of the pair (x_0(t), x_1(t)) with the independent-uniform law (TV distance),
and report whether the integer (lifted) energy E_Z = u.u + v.v - alpha u.A v on representatives [0,q)
is conserved by map (a).
Control: on a planted real-valued sphere-like shell (states with E_Z in a narrow band, integers, centred
representatives, large q), the marginal is far from uniform -- shows the TV statistic can detect shape."""
import itertools
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

for d, L, q in ((1, 5, 3), (1, 4, 5), (1, 4, 7)):
    N = L**d; n = 2 * N; S = q**n; A = adjacency(d, L); alpha = 1
    z = digits(np.arange(S, dtype=np.int64), n, q); u, v = z[:N], z[N:]
    EZ = (u * u).sum(0) + (v * v).sum(0) - alpha * (u * (A @ v)).sum(0)
    E = EZ % q
    z2 = np.vstack([v, (alpha * (A @ v) - u) % q]); u2, v2 = z2[:N], z2[N:]
    EZ2 = (u2 * u2).sum(0) + (v2 * v2).sum(0) - alpha * (u2 * (A @ v2)).sum(0)
    print(f"\nmap (a) d={d} L={L} q={q}: E mod q conserved {bool(np.all(EZ2 % q == E))}; "
          f"integer E_Z conserved at {100*np.mean(EZ2 == EZ):.1f}% of states")
    for e in range(q):
        m = E == e
        h1 = np.bincount(v[0][m], minlength=q) / m.sum()
        h2 = np.bincount((v[0] * q + v[1])[m], minlength=q * q) / m.sum()
        tv1 = 0.5 * np.abs(h1 - 1 / q).sum(); tv2 = 0.5 * np.abs(h2 - 1 / q**2).sum()
        print(f"  shell E={e}: size {int(m.sum())}; TV(one-site marginal, uniform) = {tv1:.4f}; "
              f"TV(two-site marginal, uniform) = {tv2:.4f}")

# control: real-valued thin shell, centred representatives, q = 41, N = 6 single time slice, |x|^2 band
rng = np.random.default_rng(0); q = 41; N = 6
x = rng.integers(-(q // 2), q // 2 + 1, (2_000_000, N))
r2 = (x * x).sum(1); band = (r2 >= 280) & (r2 <= 300)
h = np.bincount(x[band, 0] + q // 2, minlength=q) / band.sum()
print(f"\ncontrol: thin real shell |x|^2 in [280,300], q=41, N=6: TV(one-site marginal, uniform) = "
      f"{0.5*np.abs(h - 1/q).sum():.3f}  (large => statistic detects non-uniform shell shape)")
