"""Independent reviewer re-implementation of the native realization (report18 rule) and of Q6(c).
Does not import the author's checker. Neighbour sums by explicit index gathering (not np.roll)."""
import sys
import numpy as np
from fractions import Fraction as Fr
from itertools import product

NAMES = ['X', 'Y', 'Z', 'R']
AX = {'X': (1, 0, 0), 'Y': (0, 1, 0), 'Z': (0, 0, 1), 'R': (Fr(4, 5), Fr(3, 5), 0)}
STATIONS = [(sg, n) for n in NAMES for sg in (+1, -1)]
def bloch(st): return tuple(st[0] * Fr(x) for x in AX[st[1]])
def ip(u, v): return sum(Fr(x) * Fr(y) for x, y in zip(u, v))
def born(c, w): return (1 + ip(AX[c], w)) / 2
def prodlaw(w):
    out = {}
    for l in product((0, 1), repeat=4):
        p = Fr(1)
        for i, c in enumerate(NAMES): p *= born(c, w) if l[i] else 1 - born(c, w)
        out[l] = p
    return out

class Torus:
    def __init__(s, L):
        s.L = L
        idx = np.arange(L ** 3).reshape(L, L, L)
        s.nb = [np.roll(idx, sh, ax).reshape(-1) for ax in range(3) for sh in (1, -1)]  # index tables only
    def S(s, F):  # F: (N, L^3) -> XOR of six neighbours (gather)
        o = np.zeros_like(F)
        for t in s.nb: o ^= F[:, t]
        return o
    def step(s, old, cur):
        A, B, D = cur
        sA, sB, sD = s.S(A), s.S(B), s.S(D)
        H = (sB, sD, sA ^ (sB & sD))   # H(a,b,d) = (b, d, a xor bd)
        return tuple(o ^ h for o, h in zip(old, H))

def flat(L, x): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
def dist(L, c):
    g = np.indices((L, L, L)).reshape(3, -1)
    return sum(np.minimum((g[i] - c[i]) % L, (c[i] - g[i]) % L) for i in range(3))

def run(a, inputs, seed, L=44, T=2, rad0=2, order=NAMES, release=None, sp=8, off=6):
    """inputs: list of (lam(4-tuple by NAMES), r(4-tuple by NAMES)). Returns rec[k] : (N, T+1, 3)."""
    tor = Torus(L); N = len(inputs); rng = np.random.default_rng(seed)
    cur = [np.repeat(rng.integers(0, 2, (1, L ** 3), dtype=np.uint8), N, 0) for _ in range(3)]
    old = [np.repeat(rng.integers(0, 2, (1, L ** 3), dtype=np.uint8), N, 0) for _ in range(3)]
    ia = NAMES.index(a)
    row = {c: order.index(c) for c in NAMES}             # copy-row of each component
    copy = lambda c, k: (sp * k + off, sp * row[c] + off, off)
    recv = [(copy(a, k)[0] - 2, copy(a, k)[1], copy(a, k)[2]) for k in range(5)]
    lam = np.array([i[0] for i in inputs], np.uint8); r = np.array([i[1] for i in inputs], np.uint8)
    for k in range(5):
        d = dist(L, recv[k]); R = rad0 if k == 0 else 2
        for f in range(3): cur[f][:, d <= R] = 0; old[f][:, d <= R - 1] = 0
    for c in NAMES:
        for k in range(5):
            j = flat(L, copy(c, k))
            for f in range(3): cur[f][:, j] = 0; old[f][:, j] = 0
            cur[0][:, j] = lam[:, NAMES.index(c)]
    for k in range(1, 5):
        rc = recv[k]
        cur[0][:, flat(L, (rc[0], rc[1] + 2, rc[2]))] = r[:, k - 1]      # fresh r for component NAMES[k-1]
        cur[0][:, flat(L, (rc[0], rc[1], rc[2] + 2))] = 1
    if release is not None:
        f, pos = release; cur[f][:, flat(L, pos)] ^= 1
    rec = {k: np.zeros((N, T + 1, 3), np.uint8) for k in range(5)}
    jr = [flat(L, x) for x in recv]
    def snap(t):
        for k in range(5): rec[k][:, t, :] = np.stack([cur[f][:, jr[k]] for f in range(3)], 1)
    snap(0)
    for t in range(1, T + 1):
        old, cur = cur, tor.step(old, cur); snap(t)
    return rec, recv

def inputs_for(a):
    ia = NAMES.index(a); out = []
    for l in product((0, 1), repeat=4):
        for rb in product((0, 1), repeat=3):
            rr = list(rb); rr.insert(ia, 1); out.append((l, tuple(rr)))
    return out

def native_check(L, seeds):
    ok = True; n = 0
    for a in NAMES:
        ia = NAMES.index(a); inp = inputs_for(a)
        for sd in seeds:
            rec, _ = run(a, inp, sd, L=L)
            for i, (l, r) in enumerate(inp):
                ok &= rec[0][i, 2].tolist() == [0, l[ia], 0]
                lp = [l[ia] ^ 1 ^ x for x in r]
                for k in range(1, 5): ok &= rec[k][i, 2].tolist() == [0, lp[k - 1], 0]
                ok &= int(rec[0][i, :2].sum() + sum(rec[k][i, :2].sum() for k in range(1, 5))) == 0
                n += 1
    return ok, n

def affine_ok(vals):
    pX, mX, pY, pZ = vals[(1, 'X')], vals[(-1, 'X')], vals[(1, 'Y')], vals[(1, 'Z')]
    c0 = (pX + mX) / 2; c = ((pX - mX) / 2, pY - c0, pZ - c0)
    return all(vals[s] == c0 + ip(c, bloch(s)) for s in STATIONS)
WA = {(1, 'R'): Fr(13, 16), (-1, 'R'): Fr(3, 16)}
WB = {(1, 'X'): Fr(1, 2), (1, 'Y'): Fr(3, 8), (1, 'Z'): Fr(1, 16), (-1, 'Z'): Fr(1, 16)}

def q6c(a, seed, order=NAMES, TT=12):
    inp = inputs_for(a); rec, _ = run(a, inp, seed, T=TT, rad0=TT, order=order)
    fr = prodlaw(AX[a]); mus = {s: prodlaw(bloch(s)) for s in STATIONS}
    first = None; tvs = {}
    for D in range(0, TT - 1):
        K = {}
        for s in STATIONS:
            law = {}
            for i, (l, r) in enumerate(inp):
                at = tuple(rec[0][i, 2:3 + D].reshape(-1).tolist())
                law[at] = law.get(at, 0) + mus[s][l] * fr[r]
            K[s] = law
        atoms = set().union(*[set(K[s]) for s in STATIONS])
        hold = all(affine_ok({s: K[s].get(at, 0) for s in STATIONS}) for at in atoms)
        tvs[D] = sum(abs(sum(WA[s] * K[s].get(at, 0) for s in WA) - sum(WB[s] * K[s].get(at, 0) for s in WB)) for at in atoms) / 2
        if not hold and first is None: first = D
    # dependence on each unread lambda_b
    dep = {}
    for b in range(4):
        if b == NAMES.index(a): continue
        for D in range(0, TT - 1):
            seen = {}; v = False
            for i, (l, r) in enumerate(inp):
                key = tuple(x for j, x in enumerate(l) if j != b) + r
                val = tuple(rec[0][i, 2:3 + D].reshape(-1).tolist())
                if seen.setdefault(key, val) != val: v = True
            if v: dep[NAMES[b]] = D; break
    return first, tvs, dep

if __name__ == '__main__':
    ok, n = native_check(44, (11, 12)); print('native L=44 seeds 11,12: ok', ok, 'cases', n)
    ok, n = native_check(40, (13,)); print('native L=40 seed 13: ok', ok, 'cases', n)
    # zero-background sanity: rec should still match
    # C-NAT-like: release an even-distance pin (current A at receiver+2y) and an odd-distance one (current B at +y)
    inp = [(l, (1, 1, 1, 1)) for l in product((0, 1), repeat=4)]
    base, recv = run('X', inp, 11); rc = recv[0]
    e, _ = run('X', inp, 11, release=(0, (rc[0], rc[1] + 2, rc[2])))
    o, _ = run('X', inp, 11, release=(1, (rc[0], rc[1] + 1, rc[2])))
    p0, _ = run('X', inp, 11, release=None)
    print('C-NAT even pin changes record:', not np.array_equal(base[0][:, 2], e[0][:, 2]),
          '; odd pin leaves record:', np.array_equal(base[0][:, 2], o[0][:, 2]))
    for seed in (303, 404):
        for a in NAMES:
            first, tvs, dep = q6c(a, seed)
            print('Q6c seed', seed, a, 'first D violation', first, 'TV@10 %.6f' % float(tvs[10]), 'dep', dep)
    # layout permutation: put R's copy row next to X
    order = ['Z', 'X', 'R', 'Y']
    for a in NAMES:
        first, tvs, dep = q6c(a, 303, order=order)
        print('Q6c permuted rows', order, a, 'first D violation', first, 'TV@10 %.6f' % float(tvs[10]), 'dep', dep)
