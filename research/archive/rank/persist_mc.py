"""Monte Carlo (evidence only): persistence of a period-3 visible pattern, x_t = x_{t-3}, at one site.
S(m) = P(x_t = x_{t-3} for t = 3..m+2 | x_3 != x_0 at the previous position), i.e. survival of a fresh
period-3 stretch.  Exponential tail <=> consistent with finite rank; a power law contradicts it (R2)."""
import sys
import numpy as np
from runs_mc import run
rule, T, reps = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
N = 200000
cnt = np.zeros(T + 1, dtype=np.int64)
for s in range(reps):
    rec = run(rule, N, T + 4, 5000 + s).astype(np.int8)
    same = rec[3:] == rec[:-3]                 # same[k] : x_{k+3} == x_k
    start = ~same[0]                            # the stretch begins after a break at k = 0
    alive = start.copy()
    cnt[0] += start.sum()
    for m in range(1, T + 1):
        alive &= same[m]
        cnt[m] += alive.sum()
for m in (8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192):
    if m <= T:
        print(f'PERSIST {rule} S({m}) = {cnt[m] / cnt[0]:.3e}  (count {cnt[m]})')
