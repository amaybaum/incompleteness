# Independent exhaustive search of m<=2 embedded observers (all rho0,rho1,a; every chi) for prediction windows.
import sys, os, math, itertools, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from indep import gen, Z_of, orbit_lengths, POLY, companion

def observers(m):
    M = 1 << m
    perms = list(itertools.permutations(range(M)))
    obs = []
    for r0 in perms:
        for r1 in perms:
            for a in itertools.product((0, 1), repeat=M):
                obs.append((r0, r1, a))
    return obs

def tables(name, n, taps=None):
    if taps is None: taps = POLY[n][0]
    L = companion(n, taps)
    L = np.array(L); L2 = L[L]
    hs = np.arange(1 << n)
    ell = hs & 1; g = (hs & 1) ^ ((hs >> 1) & 1 & (hs >> 2) & 1)
    if name == 'lin': return L, L, ell
    if name == 'filt': return L, L, g
    if name == 'clk': return L, L2, ell

def counts(m, obs, s0, s1, f, n, Kmax):
    M = 1 << m; O = len(obs); N = 2 << n
    R = np.array([[o[0], o[1]] for o in obs])          # (O,2,M)
    A = np.array([o[2] for o in obs])                   # (O,M)
    x = np.tile(np.repeat([0, 1], 1 << n), (O, 1))
    h = np.tile(np.tile(np.arange(1 << n), 2), (O, 1))
    v = np.zeros((O, N), dtype=np.int64)
    oi = np.arange(O)[:, None]
    out = np.zeros((Kmax + 1, O, M, 2), dtype=np.int64)
    def rec(t):
        idx = (oi * M + v) * 2 + x
        out[t] = np.bincount(idx.ravel(), minlength=O * M * 2).reshape(O, M, 2)
    rec(0)
    for t in range(Kmax):
        v = R[oi, x, v]
        c = x ^ A[oi, v]
        h = np.where(c == 1, s1[h], s0[h])
        x = c ^ f[h]
        rec(t + 1)
    return out  # out[t, o, v, xbit]

def chi_hits(out, m):
    M = 1 << m
    chis = list(itertools.product((0, 1), repeat=M))
    H = np.stack([sum(out[:, :, vv, ch[vv]] for vv in range(M)) for ch in chis], axis=-1)  # (T,O,nchi)
    return H, chis

def windows(H, N, K):
    w = H[K - 3:K + 1]                       # (4,O,nchi)
    absok = (np.abs(8 * w - 4 * N) >= N).all(axis=0)
    sigok = (8 * w >= 5 * N).all(axis=0)
    return absok, sigok

if __name__ == '__main__':
    report = {}
    for n in range(3, 9):
        for name in ('lin', 'filt', 'clk'):
            s0, s1, f = tables(name, n)
            phi, sig, ff = gen(name, n, True)
            Z = Z_of(n, sig, ff)
            ol = sorted(orbit_lengths(n, phi).values())
            lmed = (ol[len(ol)//2 - 1], ol[len(ol)//2])
            Kcx = lmed[0] // 2
            for m in (1, 2):
                Kfp = 2 ** (n + 1 - m - 1) - 1   # largest K with m + ceil(log2(K+1)) + 1 <= n+1
                lo, hi = max(Z + 4, 3), min(Kcx, Kfp)
                key = f'{name} n={n} m={m}'
                if lo > hi:
                    report[key] = dict(Z=Z, lmed=lmed, Kcx=Kcx, region=None); continue
                obs = observers(m)
                out = counts(m, obs, s0, s1, f, n, hi)
                H, chis = chi_hits(out, m)
                N = 2 << n
                found = {}
                for K in range(lo, hi + 1):
                    ab, sg = windows(H, N, K)
                    if ab.any() or sg.any():
                        oi, ci = np.nonzero(ab)
                        found[K] = dict(abs_pairs=int(ab.sum()), signed_pairs=int(sg.sum()),
                                        abs_observers=int(ab.any(axis=1).sum()),
                                        first=[int(oi[0]), int(ci[0])] if len(oi) else None)
                report[key] = dict(Z=Z, lmed=lmed, Kcx=Kcx, region=[lo, hi], windows=found)
                print(key, report[key], flush=True)
    json.dump(report, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'search_out.json'), 'w'), indent=1)
    for k, v in report.items():
        if v['region'] is None: print(k, 'region empty', v)
