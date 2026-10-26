"""Reviewer probes: (1) retained-register counterexample to the class hypothesis as worded;
(2) attribution of the controller's discrepancy to M vs W."""
from fractions import Fraction as F
from itertools import product
from math import comb
q = F(4, 5)

def retention_sampler_tv(B, h):
    """Per slot exactly B fresh fair bits; the reset decision for slot t reads ALL bits drawn so far
    (retained private registers). Interval decoding of the quantum agreement law.
    Returns exact TV of the agreement record vs Bern(4/5)^h, and the conditional P(agree_2|agree_1)."""
    N = B * h; law = {}
    for k in range(1 << N):
        lo, hi = F(0), F(1); rec = []
        for t in range(1, h + 1):
            cell = F(k >> (N - t * B), 1 << (t * B))   # left endpoint of the known dyadic cell
            m = lo + q * (hi - lo)
            g = 1 if cell < m else 0
            rec.append(g)
            lo, hi = (lo, m) if g else (m, hi)
        law[tuple(rec)] = law.get(tuple(rec), 0) + 1
    tot = F(0)
    for rec in product((1, 0), repeat=h):
        P = F(law.get(rec, 0), 1 << N)
        Qv = F(1)
        for g in rec: Qv *= q if g else 1 - q
        tot += abs(P - Qv)
    p1 = sum(c for r, c in law.items() if r[0] == 1)
    p11 = sum(c for r, c in law.items() if len(r) > 1 and r[0] == 1 and r[1] == 1)
    return tot / 2, (F(p11, p1) if h > 1 else None)

def memoryless_tv(B, h):
    k = (q * 2 ** B); k = min((k.numerator // k.denominator, k.numerator // k.denominator + 1), key=lambda x: abs(F(x, 2 ** B) - q))
    p = F(k, 2 ** B)
    return sum(comb(h, i) * abs(p ** i * (1 - p) ** (h - i) - q ** i * (1 - q) ** (h - i)) for i in range(h + 1)) / 2

print('retention counterexample (B fresh bits/slot, reset reads retained earlier bits):')
for B, h in ((1, 14), (2, 8), (3, 6), (4, 4)):
    tv, c = retention_sampler_tv(B, h)
    print(f' B={B} h={h}: T={float(tv):.6g} (union bound sum_t 2^(t-1-tB) <= {0.5/(2**(B-1)-1) if B>1 else float('inf'):.6g}); P(agree2|agree1)={c} '
          f'in 2^-B Z: {(c * 2**B).denominator == 1 if c is not None else None}; memoryless best-B sampler T={float(memoryless_tv(B, h)):.6g}')
    if B > 1: assert tv <= F(1, 2 * (2 ** (B - 1) - 1))
print(' plateau, B=4 (retention) vs memoryless nearest-dyadic 4-bit sampler:')
for h in range(1, 6):
    tv, _ = retention_sampler_tv(4, h)
    print(f'  h={h}: retention T={float(tv):.6g}  memoryless T={float(memoryless_tv(4, h)):.6g}')
print(' memoryless B=4: T(64)=%.4f T(4096)=%.4f' % (float(memoryless_tv(4, 64)), float(memoryless_tv(4, 4096))))
print(' memoryless B=1: T(14)=%.4f T(200)=%.4f ; retention keeps T<=(1/2)/(2^(B-1)-1) for all h, B>=2'
      % (float(memoryless_tv(1, 14)), float(memoryless_tv(1, 200))))

# (2) attribution M vs W
from math import lcm
def AB(M, W, Bb=24):
    K = 1 << Bb
    Z = []
    for face in range(3):
        free = [j for j in range(3) if j != face]
        for s in (-1, 1):
            for u in range(-M + 1, M, 2):
                for v in range(-M + 1, M, 2):
                    z = [0, 0, 0]; z[face] = s * M; z[free[0]] = u; z[free[1]] = v; Z.append(tuple(z))
    def cnt(num, den):
        fac = (1 << W) * M ** 3; w = []
        for z in Z:
            a = sum(x * y for x, y in zip(num, z)); qq = sum(x * x for x in z)
            w.append(0 if a <= 0 else fac * a // (den * qq * qq))
        tot = sum(w); cum = last = 0; c = []
        for x in w: cum += x; cut = K * cum // tot; c.append(cut - last); last = cut
        return c
    cX, ca = cnt((1, 0, 0), 1), cnt((3, 4, 0), 5)
    A = F(sum(c for c, z in zip(ca, Z) if z[0] >= 0), K)
    Bv = F(sum(c for c, z in zip(cX, Z) if 3 * z[0] + 4 * z[1] >= 0), K)
    return A, Bv
print('discrepancy attribution (dA, dB) x 1e4:')
for M, W in ((16, 16), (16, 40), (32, 16), (32, 40), (64, 40)):
    A, Bv = AB(M, W)
    print(f' M={M} W={W}: dA={float(abs(A-q))*1e4:.4f} dB={float(abs(Bv-q))*1e4:.4f}')
