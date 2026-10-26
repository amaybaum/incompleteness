# Independent recomputation of the PE-01 witness, written from PLAN.md alone.
# Imports nothing from the package.
import sys, itertools, math
from fractions import Fraction as Fr

POLY = {  # coefficient sets of p_n = z^n + sum_{i in S} z^i  (primary) and p'_n
 3:({1,0},{2,0}), 4:({1,0},{3,0}), 5:({2,0},{3,0}), 6:({1,0},{5,0}), 7:({1,0},{6,0}), 8:({4,3,2,0},{6,5,4,0})}

def companion(n, taps):
    # Fibonacci companion map (h0..h_{n-1}) -> (h1..h_{n-1}, sum_i c_i h_i); h as int, bit i = h_i
    def L(h):
        fb = 0
        for i in taps: fb ^= (h >> i) & 1
        return (h >> 1) | (fb << (n - 1))
    return [L(h) for h in range(1 << n)]

def order_of_z(n, taps):
    # order of z modulo p: iterate polynomial multiplication by z
    mask = (1 << n); p = mask | sum(1 << i for i in taps)
    r = 1; k = 0
    while True:
        r <<= 1; k += 1
        if r & mask: r ^= p
        if r == 1: return k

def gen(name, n, primary=True):
    taps = POLY[n][0 if primary else 1]
    L = companion(n, taps)
    L2 = [L[L[h]] for h in range(1 << n)]
    ell = lambda h: h & 1
    g = lambda h: (h & 1) ^ (((h >> 1) & 1) & ((h >> 2) & 1))
    if name == 'lin':  s0, s1, f = L, L, ell
    elif name == 'filt': s0, s1, f = L, L, g
    elif name == 'clk': s0, s1, f = L, L2, ell
    elif name == 'dec': s0, s1, f = L, L, (lambda h: 0)
    sig = (s0, s1)
    def phi(x, h):  # phi = tau_f o kappa_sigma
        h2 = sig[x][h]
        return x ^ f(h2), h2
    return phi, sig, f

def Z_of(n, sig, f, kmax=12):
    # largest k with joint uniformity of first k increments for every control sequence
    N = 1 << n
    best = 0
    for k in range(1, kmax + 1):
        ok = True
        for cs in itertools.product((0, 1), repeat=k):
            cnt = {}
            for h in range(N):
                hh = h; z = []
                for c in cs:
                    hh = sig[c][hh]; z.append(f(hh))
                z = tuple(z); cnt[z] = cnt.get(z, 0) + 1
            if len(cnt) != 2 ** k or len(set(cnt.values())) != 1:
                ok = False; break
        if not ok: return best
        best = k
    return best

def orbit_lengths(n, phi):
    N = 2 << n
    lens = {}
    for x in (0, 1):
        for h in range(1 << n):
            s = (x, h); t = phi(*s); l = 1
            while t != s: t = phi(*t); l += 1
            lens[(x, h)] = l
    return lens

def adv_curve(n, phi, m, rho0, rho1, a, chi, Kmax):
    # exact Pr[chi(v_K') = x_K'] for K'=0..Kmax by full enumeration of (x0,h), v0=0
    N = 1 << n
    hits = [0] * (Kmax + 1)
    for x0 in (0, 1):
        for h0 in range(N):
            x, h, v = x0, h0, 0
            for t in range(Kmax + 1):
                if chi[v] == x: hits[t] += 1
                if t == Kmax: break
                v = (rho0, rho1)[x][v]
                x ^= a[v]
                x, h = phi(x, h)
    return [Fr(c, 2 * N) for c in hits]

if __name__ == '__main__':
    n = 5
    for prim in (True, False):
        phi, sig, f = gen('clk', n, prim)
        rho0 = [1, 0, 2, 3]; rho1 = [0, 2, 3, 1]; a = [1, 0, 0, 1]; chi = [0, 0, 0, 0]
        cur = adv_curve(n, phi, 2, rho0, rho1, a, chi, 10)
        print('primary' if prim else 'reciprocal', [str(c - Fr(1, 2)) for c in cur])
