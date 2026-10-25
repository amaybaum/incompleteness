"""Exact T(h) for RS(2,k) at small h (own block-law code, as in round 1). Usage: python3 -I -B rs25_exact.py"""
from fractions import Fraction as F
Q45 = F(4, 5)
def block_law(B, k):
    out = {}
    def rec(t, a, b, lo, hi, r):
        if t == k:
            out[r] = b - a; return
        a2, b2 = a << B, b << B
        cut = lo + Q45 * (hi - lo)
        x = cut * (1 << ((t + 1) * B)); m = -((-x.numerator) // x.denominator)
        m1 = min(max(m, a2), b2)
        rec(t + 1, a2, m1, lo, cut, r + (1,)); rec(t + 1, m1, b2, cut, hi, r + (0,))
    rec(0, 0, 1, F(0), F(1), ())
    return {r: F(c, 1 << (B * k)) for r, c in out.items() if c}
def tv(B, k, h):
    full, rem = divmod(h, k); P = {(): F(1)}
    for _ in range(full):
        bl = block_law(B, k); P = {a + b: x * y for a, x in P.items() for b, y in bl.items()}
    if rem:
        tl = block_law(B, rem); P = {a + b: x * y for a, x in P.items() for b, y in tl.items()}
    s = qs = F(0)
    for r, p in P.items():
        a = sum(r); q = Q45 ** a * (1 - Q45) ** (h - a); s += abs(p - q); qs += q
    return (s + 1 - qs) / 2
for k, h in ((5, 10), (5, 11), (4, 8), (3, 6), (2, 6)):
    t = tv(2, k, h); print(f'RS(2,{k}) exact T({h}) = {float(t):.6f} > 1/2: {t > F(1, 2)}')
