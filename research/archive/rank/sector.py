"""Sector dimensions: rank of [pasts of length <= p] x [futures of length <= k] (exact counts, n = 8 window).
dim of the sector body = rank - 1 (R0 applied to the sub-tower).  Lower bounds over Q via F_p."""
import sys
from itertools import product
sys.path.insert(0, '.')
from lattice_rank import record_counts, rank_mod, P1
rule = sys.argv[1]
n = 8
arr = record_counts(n, rule).reshape([2] * (2 * n))
def joint(h, f):
    sl = [slice(None)] * (2 * n)
    for i, b in enumerate(h): sl[n - len(h) + i] = b
    for i, b in enumerate(f): sl[n + i] = b
    return int(arr[tuple(sl)].sum())
S = lambda L: [s for l in range(L + 1) for s in product((0, 1), repeat=l)]
for k in (1, 2, 3, 4):
    row = [rank_mod([[joint(h, f) for f in S(k)] for h in S(p)], P1) - 1 for p in range(0, 9)]
    print(f'SECTOR {rule} effects <= {k}: dim for pasts <= 0..8:', row)
