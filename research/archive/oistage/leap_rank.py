"""Exact Hankel ranks of the visible process of a 1-D second-order (leap) substratum.

Sites -R..R, Q = Z2 x Z2 per site (u, v); leap: (u_i, v_i) -> (v_i, F(v)_i + u_i) mod 2, the
reversible second-order form of the corpus (SecondOrderCircuit.leap).  Uniform (counting) measure
on the cone region, which every bijective cellular automaton preserves.  The visible readout is
v_0.  The record over h + f steps depends only on the radius-(h+f) ball (the causal cone,
RegionTower.iterate_dependsOnlyOn_ball), so counting on that ball is exact for the infinite lattice.
Counts are integers; ranks are exact (fractions).
"""
import sys
from fractions import Fraction as Fr
from itertools import product
import numpy as np

sys.path.insert(0, '.')
from oistage_checks import rank  # noqa: E402  (exact rank; importing runs the checks once)


def joint_counts(n, rule):
    R = 2 * n
    W = 2 * R + 1
    mask = (1 << W) - 1
    N = 1 << (2 * W)
    idx = np.arange(N, dtype=np.uint64)
    u = (idx & np.uint64(mask)).astype(np.uint32)
    v = (idx >> np.uint64(W)).astype(np.uint32)
    del idx
    rec = np.zeros(N, dtype=np.uint32)
    m = np.uint32(mask)
    for t in range(2 * n):
        left, right = (v << np.uint32(1)) & m, v >> np.uint32(1)
        if rule == 'linear':
            F = left ^ right
        else:
            F = (left & right) ^ v
        u, v = v, (F ^ u) & m
        bit = (v >> np.uint32(R)) & np.uint32(1)
        rec = (rec << np.uint32(1)) | bit
    cnt = np.bincount(rec.astype(np.int64), minlength=1 << (2 * n))
    return cnt, N


def hankel(n, rule):
    cnt, N = joint_counts(n, rule)
    # string s of length 2n (first n = past, last n = future), counts cnt[s]
    def P(bits):  # probability of a contiguous string ending at the past/future boundary layout
        return bits
    full = {}
    for s in range(1 << (2 * n)):
        full[tuple((s >> (2 * n - 1 - k)) & 1 for k in range(2 * n))] = int(cnt[s])

    def prob(past, fut):
        # past occupies the last len(past) slots before the boundary, fut the first len(fut) after
        tot = 0
        for full_s, c in full.items():
            if full_s[n - len(past):n] == past and full_s[n:n + len(fut)] == fut:
                tot += c
        return Fr(tot, N)
    strings = [s for L in range(n + 1) for s in product((0, 1), repeat=L)]
    return rank([[prob(h, f) for f in strings] for h in strings])


if __name__ == '__main__':
    for rule in ('linear', 'nonlinear'):
        rs = [hankel(n, rule) for n in (1, 2, 3)]
        print('LEAP', rule, 'Hankel ranks n = 1, 2, 3:', rs)
