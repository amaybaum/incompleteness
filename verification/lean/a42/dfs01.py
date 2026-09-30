"""{0,1} representatives (any gauge representative with entries in {0,1}, no mode condition): exhaustive
enumeration of straight lines with support <= BUDGET, in two cases.
 (i)  a zero row exists: per exact nonzero-row set R, rows are nonempty common-vanishing sets (Lemma CV).
 (ii) every row nonzero and every row of support >= 2: DFS over rows with the exact pair tables.
 (Rows of support 1 are handled by Lemma G1: a {0,1} straight line with a row e_k has column k equal to all ones,
  so it is gauge-equivalent to a {0,1} straight line of support s - 16 with a zero row, covered by (i) at BUDGET-16.)
Every leaf is classified against the 18 relaxed census subspaces and its support and exact rank(SIG o E) recorded."""
import sys, time, pickle, collections
import numpy as np
from dfs42 import VT, PC, FULL
from classify42 import member_masks
BUDGET = int(sys.argv[1]); mode = sys.argv[2]; out = sys.argv[3]
msize = np.load('msize.npy')
def compat01(X, y, i, i2):
    V = VT[i, i2]; return V[X & ~y & FULL] & V[y & ~X & FULL]
def dfs(rows, C, budget):
    leaves = []
    def rec(cand, assigned, used):
        free = list(cand)
        mins = {r: int(PC[C[r][cand[r]]].min()) for r in free}
        slack = budget - used - sum(mins.values())
        if slack < 0: return
        i = min(free, key=lambda r: len(cand[r]))
        ci = cand[i]; ci = ci[PC[C[i][ci]] <= mins[i] + slack]
        rest = [r for r in free if r != i]
        for n in ci.tolist():
            y = int(C[i][n])
            if not rest: assigned[i] = y; leaves.append(dict(assigned)); del assigned[i]; continue
            new = {}; ok = True
            for r in rest:
                c = cand[r]; c = c[compat01(C[r][c], y, r, i)]
                if not len(c): ok = False; break
                new[r] = c
            if not ok: continue
            assigned[i] = y; rec(new, assigned, used + int(PC[y])); del assigned[i]
    rec({r: np.arange(len(C[r])) for r in rows}, {}, 0)
    return leaves
t0 = time.time(); allleaves = []
if mode == 'zero':
    for R in range(1, FULL):
        r = bin(R).count('1')
        if r < 2: continue
        Z = FULL ^ R; rows = [i for i in range(16) if (R >> i) & 1]
        lb = sum(int(msize[i, Z]) for i in rows)
        if lb > BUDGET: continue
        C = {}
        for i in rows:
            V = np.ones(1 << 16, dtype=bool)
            for z in range(16):
                if (Z >> z) & 1: V &= VT[i, z]
            L = np.flatnonzero(V); L = L[(L > 0) & (PC[L] <= BUDGET - (lb - int(msize[i, Z])))]
            C[i] = L
        if any(len(C[i]) == 0 for i in rows): continue
        allleaves += dfs(rows, C, BUDGET)
else:
    allm = np.arange(1 << 16)
    C = {i: allm[(PC[allm] >= 2) & (PC[allm] <= BUDGET - 30)] for i in range(16)}
    allleaves = dfs(list(range(16)), C, BUDGET)
X = np.zeros((len(allleaves), 256), dtype=np.int64)
for n, a in enumerate(allleaves):
    for i, m in a.items():
        for k in range(16): X[n, i * 16 + k] = (m >> k) & 1
ms, mr = member_masks(X) if len(X) else (np.zeros(0, int), np.zeros(0, int))
sup = (X != 0).sum(axis=1)
hist = collections.Counter((int(s), bool(r)) for s, r in zip(sup, mr))
print(mode, 'budget', BUDGET, 'leaves', len(X), 'hist (support, in some census subspace):', sorted(hist.items()), '%.0fs' % (time.time() - t0), flush=True)
pickle.dump({'X': X, 'mr': mr, 'ms': ms}, open(out, 'wb'))
