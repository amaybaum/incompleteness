"""Independent reviewer re-derivation for native_predicate_v8 (no import of checks.py).
Usage: python3 -I -B rederive.py <result.json> seed [seed ...]
"""
import json, sys
from collections import Counter

M64 = (1 << 64) - 1
def rng(seed):
    x = (seed * 0x9E3779B97F4A7C15 + 0x1234567) & M64 or 1
    while True:
        x ^= (x << 13) & M64; x ^= x >> 7; x ^= (x << 17) & M64
        yield x

def H(v):  # (A,B,D) -> (B, D, A^(B&D)), v = 4A+2B+D
    A, B, D = v >> 2 & 1, v >> 1 & 1, v & 1
    return 4*B + 2*D + (A ^ (B & D))

n = 6; rho = 4; tend = n + 1 + 16; R0 = rho + tend
src = [(-(n+1), 0, -1), (-(n+1), 0, 1), (-(n+2), 0, 0)]
def l1(a, b): return sum(abs(p-q) for p, q in zip(a, b))
def ball(r):
    return [(x, y, z) for x in range(-r, r+1) for y in range(-r, r+1) for z in range(-r, r+1)
            if abs(x)+abs(y)+abs(z) <= r]
init = sorted(ball(R0))
region = ball(rho)
nbr = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def background(seed):
    if seed == 0: return {}, {}
    g = rng(seed); prev, cur = {}, {}
    for c in init:   # same generation order: sorted ball, prev then cur per cell
        prev[c] = next(g) & 7; cur[c] = next(g) & 7
    return prev, cur

import numpy as np
HT = np.array([H(v) for v in range(8)], dtype=np.uint8)
SIDE = 2*R0 + 3; C = R0 + 1
def evolve_all(prev, cur):
    """Numpy, periodic cube large enough that wrap cannot reach any read cone."""
    P = np.zeros((SIDE, SIDE, SIDE, 512), dtype=np.uint8)
    Q = np.zeros((SIDE, SIDE, SIDE, 512), dtype=np.uint8)
    for c, v in prev.items(): P[c[0]+C, c[1]+C, c[2]+C, :] = v
    for c, v in cur.items(): Q[c[0]+C, c[1]+C, c[2]+C, :] = v
    G = np.arange(512)
    for i, f in enumerate(src):
        Q[f[0]+C, f[1]+C, f[2]+C, :] = (G >> (3*i)) & 7
    sl = lambda A: A[C-rho:C+rho+1, C-rho:C+rho+1, C-rho:C+rho+1, :].copy()
    out = {-1: sl(P), 0: sl(Q)}
    for t in range(1, tend+1):
        acc = np.zeros_like(Q)
        for ax in range(3):
            acc ^= np.roll(Q, 1, axis=ax); acc ^= np.roll(Q, -1, axis=ax)
        Nw = P ^ HT[acc]
        P, Q = Q, Nw
        out[t] = sl(Q)
    return out

def bit(v, i): return v >> (2-i) & 1   # 0=A,1=B,2=D

def run(seed):
    prev, cur = background(seed)
    for f in src: cur.pop(f, None)
    F = evolve_all(prev, cur)
    get = lambda t, x: F[t][x[0]+rho, x[1]+rho, x[2]+rho, :].tolist()
    p = set(get(n, (0,0,0))); assert len(p) == 1; p = p.pop()
    s = bit(p, 1)
    V = get(n+2, (0,0,0))
    q8 = get(n+1, (0,0,-1)); q10 = get(n+1, (0,0,1))
    J = [4*bit(a,1) + 2*bit(b,2) + bit(b,1) for a, b in zip(q8, q10)]   # Y=Q8.B, R=Q10.D, Z=Q10.B
    nn = {(0,0):5,(0,1):0,(1,0):4,(1,1):1}
    t1 = [nn[(y^s, r^s)] for y in (0,1) for r in (0,1) for z in (0,1)]
    t0 = [8-c for c in t1]
    assert sum(t1) == 20 and sum(t0) == 44
    byv = {v: [l for l in range(512) if V[l] == v] for v in range(8)}
    assert all(len(byv[v]) == 64 for v in range(8))
    hist = Counter(); heralded = 0; law_good_any = 0; twoblock = []
    const = 0
    for t in range(-1, tend+1):
        for x in sorted(region):
            vals = get(t, x)
            if len(set(vals)) == 1: const += 1
            mb = 0; her = False; good = False
            for v in range(8):
                cls = {}
                for l in byv[v]:
                    cls.setdefault(vals[l], [0]*8)[J[l]] += 1
                mb = max(mb, len(cls))
                for c in cls.values():
                    tot = sum(c)
                    if all(ci*20 == ti*tot for ci, ti in zip(c, t1)): her = True
                if len(cls) == 2:
                    cs = list(cls.values())
                    if (cs[0] == t1 and cs[1] == t0) or (cs[1] == t1 and cs[0] == t0): good = True
            hist[mb] += 1; heralded += her; law_good_any += good
            if mb == 2:
                sizes = sorted(Counter(vals[l] for l in byv[0]).values())
                twoblock.append((x, t, sizes))
    # parity/cone count of possibly G-dependent site-times
    dep = sum(1 for t in range(-1, tend+1) for x in region
              if t >= min(l1(x, f) for f in src) and (t - min(l1(x, f) for f in src)) % 2 == 0)
    return {'p': p, 's': s, 'hist': dict(sorted(hist.items())), 'heralded': heralded,
            'law_good_cells': law_good_any, 'const': const, 'cone_parity_dep': dep,
            'twoblock_v0_sizes': twoblock}

if __name__ == '__main__':
    res = json.load(open(sys.argv[1]))
    rows = {r['seed']: r for r in res['families']}
    rows[0] = res['zero_background_diagnostic']
    for sd in map(int, sys.argv[2:]):
        out = run(sd)
        theirs = {int(k): v for k, v in rows[sd]['max_blocks_given_V_histogram'].items()}
        print(sd, 'old_q9', out['p'], 'sign', out['s'], 'hist_match', out['hist'] == theirs,
              'heralded', out['heralded'], 'law_good_cells', out['law_good_cells'],
              'const', out['const'], 'cone_parity_dep', out['cone_parity_dep'], 'twoblock', out['twoblock_v0_sizes'])
        print('  mine', out['hist']); print('  theirs', theirs)
