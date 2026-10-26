"""Exact first T>1/2 depth for RS(2,k), k=2..5, by explicit product of own block laws (h<=20).
Usage: python3 -I -B rs_exact_small.py   (imports indep.py's block_law by path argument-free exec)"""
import sys
from fractions import Fraction as F
from itertools import product
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
    return {r: F(c, 1 << (B * k)) for r, c in out.items()}
def law_h(B, k, h):
    full, rem = divmod(h, k)
    bl = block_law(B, k); pred = {(): F(1)}
    for _ in range(full):
        pred = {a + b: x * y for a, x in pred.items() for b, y in bl.items() if y}
    if rem:
        tl = block_law(B, rem)
        pred = {a + b: x * y for a, x in pred.items() for b, y in tl.items() if y}
    return pred
def tv(B, k, h):
    P = law_h(B, k, h)
    # sum over records with P>0 of |P-Q| plus quantum mass of P-null records
    s = F(0); qs = F(0)
    for r, p in P.items():
        a = sum(r); q = Q45 ** a * (1 - Q45) ** (h - a)
        s += abs(p - q); qs += q
    return (s + (1 - qs)) / 2
for k, (lo, hi) in {2: (4, 12), 3: (6, 15), 4: (4, 16), 5: (5, 15)}.items():
    first = next((h for h in range(1, 21) if tv(2, k, h) > F(1, 2)), None)
    print(f'RS(2,{k}) exact first h with T>1/2: {first}; certified window ({lo}, {hi}]; inside: {first is not None and lo < first <= hi}')
