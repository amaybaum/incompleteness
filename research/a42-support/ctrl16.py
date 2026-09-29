"""C2 in the D1 search: budget 16, every row set; all leaves returned, A/B/C/-A present, all support-16 leaves in N18."""
import numpy as np, pickle
from dfsR2 import RSearch2, to_flat
from classify42 import member_masks
from lib42 import A38, B38, C38
FULL = (1 << 16) - 1
msize = np.load('msize.npy')
leaves = []
for R in range(1, FULL):
    if bin(R).count('1') < 2: continue
    Z = FULL ^ R
    if sum(int(msize[i, Z]) for i in range(16) if (R >> i) & 1) > 16: continue
    S = RSearch2(R, 16, prune=False); S.run(); leaves += [to_flat(a) for a in S.leaves]
X = np.array(leaves); ms, mr = member_masks(X)
print('leaves', len(X), 'all in N18', bool((mr != 0).all()))
for nm, E in (('A', A38), ('B', B38), ('C', C38), ('-A', [[-x for x in r] for r in A38])):
    v = np.array(E).reshape(256); print(nm, 'present', bool((X == v).all(axis=1).any()))
