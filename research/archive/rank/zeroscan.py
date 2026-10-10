"""Exact scan of zero sets Z(u,w,v) = {k : P(u w^k v) = 0} from the n = 8 record counts (window 16).
Finite rank => every Z is eventually periodic (Skolem-Mahler-Lech).  We list the zero patterns that are
not periodic within the observable range, as candidates only (a finite window cannot certify)."""
import sys
from itertools import product
import numpy as np
sys.path.insert(0, '.')
from lattice_rank import record_counts
rule = sys.argv[1]
n = 8
arr = record_counts(n, rule).reshape([2] * (2 * n))
def P(word):
    sl = tuple(list(word) + [slice(None)] * (2 * n - len(word)))
    return int(arr[sl].sum())
words = [w for l in range(0, 3) for w in product((0, 1), repeat=l)]
cands = 0
for w in [w for w in words if len(w) >= 1]:
    for u in words:
        for v in words:
            K = (2 * n - len(u) - len(v)) // len(w)
            pat = ''.join('0' if P(u + w * k + v) == 0 else '+' for k in range(K + 1))
            # eventually periodic within the window with period <= 3 and preperiod <= 2?
            ok = any(all(pat[i] == pat[i + p] for i in range(pre, len(pat) - p))
                     for p in (1, 2, 3) for pre in range(0, max(1, len(pat) - 2 * p)))
            if not ok:
                cands += 1
                print(f'ZERO {rule} u={u} w={w} v={v}: {pat}')
print(f'ZERO {rule}: {cands} non-periodic-looking patterns (window-limited)')
