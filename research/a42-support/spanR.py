"""R-span lemma check: W_R = span{ e_i (x) 1_K : i in R, K a minimal common-vanishing set of row i against Z }.
If W_R lies in one relaxed census subspace, every straight line whose zero-row set is exactly Z (any integer values)
is Dita."""
import numpy as np, collections, sys
from dfs42 import VT, PC
from mincv import cv_table, minimal_sets
from classify42 import KEYS
from lib42 import STRUCTS, SMAT
FULL = (1 << 16) - 1
Rs = [int(x) for x in open(sys.argv[1]).read().split()]
msize = np.load('msize.npy')
dead = 0; alive = []
for R in Rs:
    Z = FULL ^ R; gens = []
    for i in range(16):
        if not (R >> i) & 1: continue
        for K in minimal_sets(cv_table(i, Z)):
            v = np.zeros(256, dtype=np.int64)
            for k in range(16):
                if (K >> k) & 1: v[i * 16 + k] = 1
            gens.append(v)
    Gm = np.array(gens)
    inS = [KEYS[k] for k, (nm, tr, s) in enumerate(STRUCTS) if not (SMAT[(nm, tr, True)] @ Gm.T).any()]
    if inS: dead += 1
    else: alive.append(R)
    lb = sum(int(msize[i, Z]) for i in range(16) if (R >> i) & 1)
    print(hex(R), 'r', bin(R).count('1'), 'LB', lb, 'gens', len(gens), 'W_R in', inS[:3], flush=True)
print('dead', dead, 'alive', len(alive))
open(sys.argv[2], 'w').write('\n'.join(map(str, alive)))
