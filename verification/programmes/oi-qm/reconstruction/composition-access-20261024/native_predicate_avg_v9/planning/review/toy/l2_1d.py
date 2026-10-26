"""Exhaustive 1D analogue of L2: x_t(c) = x_{t-2}(c) ^ H(x_{t-1}(c-1) ^ x_{t-1}(c+1)).
Pair (1,2) at site 0 depends on x_{-1}(-1..1) and x_0(-2..2): 8 triples, 2^24 worlds.
Fair prior: pair must be uniform on 64 values. Bias-1/4 per bit: must not be."""
import numpy as np
H = np.array([4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1)) for v in range(8)], dtype=np.uint8)
w = np.arange(1 << 24, dtype=np.uint32)
tr = [((w >> (3*i)) & 7).astype(np.uint8) for i in range(8)]
m1 = {-1: tr[0], 0: tr[1], 1: tr[2]}
z0 = {-2: tr[3], -1: tr[4], 0: tr[5], 1: tr[6], 2: tr[7]}
x1 = {c: m1[c] ^ H[z0[c-1] ^ z0[c+1]] for c in (-1, 0, 1)}
x2_0 = z0[0] ^ H[x1[-1] ^ x1[1]]
pair = (x1[0].astype(np.uint32) << 3) | x2_0
cnt = np.bincount(pair, minlength=64)
print('fair: min/max count', cnt.min(), cnt.max(), 'expected', (1 << 24)//64)
# biased prior: weight each world by prod over 24 bits of (1/4 if bit else 3/4) -> use integer weights 1^k 3^(24-k)
pop = np.zeros(1 << 24, dtype=np.int64)
for b in range(24): pop += ((w >> b) & 1).astype(np.int64)
wt = 3 ** (24 - pop)   # exact integer weights (fits int64: 3^24 ~ 2.8e11)
bc = np.bincount(pair, weights=None, minlength=64)
bw = np.zeros(64, dtype=object)
for v in range(64):
    bw[v] = int(wt[pair == v].sum())
print('biased: distinct weights', len(set(bw)), '(1 would mean product-uniform-like; >1 means not uniform)')
