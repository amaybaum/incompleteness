"""Certain continuations: pasts of length n after which the next m outputs are determined."""
import sys
sys.path.insert(0, '.')
import numpy as np
from lattice_rank import record_counts
n = int(sys.argv[1]); rule = sys.argv[2]
cnt = record_counts(n, rule).reshape(1 << n, 1 << n)    # rows: past (times -n+1..0), cols: future (1..n)
for m in range(1, n + 1):
    fut = cnt.reshape(1 << n, 1 << m, 1 << (n - m)).sum(axis=2)   # future prefix of length m
    tot = fut.sum(axis=1)
    certain = set()
    for h in range(1 << n):
        if tot[h] and np.count_nonzero(fut[h]) == 1:
            certain.add(int(np.nonzero(fut[h])[0][0]))
    print(f'CERTAIN {rule} n={n} m={m}: {len(certain)} distinct certain futures', sorted(format(f, f"0{m}b") for f in certain)[:12])
