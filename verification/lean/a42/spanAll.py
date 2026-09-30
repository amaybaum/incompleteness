"""R-span lemma over every nonzero-row set R (r >= 2) with LB(R) <= BMAX, no symmetry reduction.
W_R = span of e_i (x) 1_K (i in R, K common-vanishing for row i against Z = complement of R). R is dead if W_R lies in
one of the 18 relaxed census subspaces (then every straight line, any integer values, whose zero-row set is exactly Z
is Dita). Output: per R: r, LB, dead flag, structure."""
import sys, time, numpy as np, collections, pickle
from dfs42 import VT, PC, FULL
from lib42 import STRUCTS, SMAT
BMAX = int(sys.argv[1])
msize = np.load('msize.npy')
AR = [SMAT[(nm, tr, True)] for nm, tr, s in STRUCTS]
names = [(nm, 'row' if tr else 'col') for nm, tr, s in STRUCTS]
BITS = ((np.arange(1 << 16)[:, None] >> np.arange(16)[None, :]) & 1).astype(np.int64)
t0 = time.time(); res = []
for R in range(1, FULL):
    r = bin(R).count('1')
    if r < 2: continue
    Z = FULL ^ R; rows = [i for i in range(16) if (R >> i) & 1]
    lb = sum(int(msize[i, Z]) for i in rows)
    if lb > BMAX: continue
    gens = {}
    for i in rows:
        V = np.ones(1 << 16, dtype=bool)
        for z in range(16):
            if (Z >> z) & 1: V &= VT[i, z]
        gens[i] = BITS[np.flatnonzero(V)]
    dead = None
    for k in range(18):
        if all(not (AR[k][:, i * 16:(i + 1) * 16] @ gens[i].T).any() for i in rows): dead = names[k]; break
    res.append((R, r, lb, dead))
alive = [x for x in res if x[3] is None]
print('R sets', len(res), 'dead', len(res) - len(alive), 'alive', len(alive), '%.0fs' % (time.time() - t0))
print('min LB among alive:', min(x[2] for x in alive) if alive else None)
print('alive by LB:', sorted(collections.Counter(x[2] for x in alive).items()))
print('dead by LB:', sorted(collections.Counter(x[2] for x in res if x[3]).items()))
pickle.dump(res, open('spanAll_%d.pkl' % BMAX, 'wb'))
