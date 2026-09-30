"""msize[i][Zmask] = the least size of a nonempty column set K with sum_{k in K} SIG_ik conj(SIG_i0k) = 0 for every
row i0 in Z (Z a set of rows not containing i); 17 if none (K = all columns always qualifies: size 16)."""
import time, numpy as np, pickle
from dfs42 import VT, PC
t0 = time.time()
PCm = PC.copy(); PCm[0] = 99
msize = np.full((16, 1 << 16), 99, dtype=np.int16)
for i in range(16):
    others = [r for r in range(16) if r != i]
    # DFS over subsets of others, incremental AND
    stack = [(0, np.ones(1 << 16, dtype=bool), 0)]
    while stack:
        pos, V, Z = stack.pop()
        if pos == len(others):
            msize[i, Z] = PCm[V].min(); continue
        r = others[pos]
        stack.append((pos + 1, V, Z))
        stack.append((pos + 1, V & VT[i, r], Z | (1 << r)))
    print('row', i, '%.0fs' % (time.time() - t0), flush=True)
np.save('msize.npy', msize)
