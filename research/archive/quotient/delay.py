"""Delay family from the exact n=8 record counts: effects 'bit at delay k = 1' (k = 1..8), pasts of length <= 8."""
import sys
from itertools import product
sys.path.insert(0, '../rank')
from lattice_rank import record_counts, rank_mod, P1
rule = sys.argv[1]; n = 8
arr = record_counts(n, rule).reshape([2] * (2 * n))
pasts = [h for l in range(n + 1) for h in product((0, 1), repeat=l)]
def w(h):
    sl = [slice(None)] * (2 * n)
    for i, b in enumerate(h): sl[n - len(h) + i] = b
    return int(arr[tuple(sl)].sum())
def delay(h, k):
    sl = [slice(None)] * (2 * n)
    for i, b in enumerate(h): sl[n - len(h) + i] = b
    sl[n + k - 1] = 1
    return int(arr[tuple(sl)].sum())
W = [w(h) for h in pasts]
for kmax in range(1, n + 1):
    cols = [W] + [[delay(h, k) for h in pasts] for k in range(1, kmax + 1)]
    print(f'DELAY8 {rule}: span(unit, W^k r, 1<=k<={kmax}) on pasts<=8: dim = {rank_mod([list(c) for c in zip(*cols)], P1)}')
