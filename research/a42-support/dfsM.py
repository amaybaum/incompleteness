"""m in {1,2} case (no zero row and no zero column in the min-support representative), domain {-1,0,1}: row 0 is a
line of minimum support m (WLOG by row-transitivity and transposition), every row has support >= m, total <= BUDGET.
Row 0 runs over orbit representatives of support-m rows under the row-0 stabilizer and global negation."""
import sys, time, pickle, collections
import numpy as np
from dfs42 import *
from classify42 import member_masks
m = int(sys.argv[1]); BUDGET = int(sys.argv[2]); out = sys.argv[3]
fix0 = [(p, s_) for p, s_ in elems if all(divmod(p[0 * 16 + j], 16)[0] == 0 for j in range(16))]
def act_row0(e, P, N):
    p, s_ = e; P2 = N2 = 0
    for j in range(16):
        j2 = p[j] % 16
        if (P >> j) & 1: (P2, N2) = (P2 | (1 << j2), N2) if s_ == 1 else (P2, N2 | (1 << j2))
        if (N >> j) & 1: (P2, N2) = (P2, N2 | (1 << j2)) if s_ == 1 else (P2 | (1 << j2), N2)
    return P2, N2
rows_m = []
for P in range(1 << 16):
    for N in range(1 << 16) if False else []: pass
import itertools
for supp in itertools.combinations(range(16), m):
    for signs in itertools.product((1, -1), repeat=m):
        P = sum(1 << k for k, s in zip(supp, signs) if s == 1); N = sum(1 << k for k, s in zip(supp, signs) if s == -1)
        rows_m.append((P, N))
seen = set(); reps = []
for y in rows_m:
    if y in seen: continue
    orb = set()
    for e in fix0:
        a = act_row0(e, *y); orb.add(a); orb.add((a[1], a[0]))
    seen |= orb; reps.append(y)
print('row-0 stabilizer size', len(fix0), 'support-%d rows' % m, len(rows_m), 'orbit reps', len(reps), flush=True)
t0 = time.time()
G = global_rows()
hist = collections.Counter(); nond = []; tot = 0
for y0 in reps:
    S = Search(G, y0, m, BUDGET)
    leaves = []
    def on_leaf(a, used): leaves.append(dict(a))
    S.run(on_leaf)
    good = 0
    if leaves:
        X = np.array([to_matrix(a).reshape(256) for a in leaves])
        colsup = (X.reshape(-1, 16, 16) != 0).sum(axis=1).min(axis=1)
        X = X[colsup >= m]; good = len(X)
        if len(X):
            ms, mr = member_masks(X); sup = (X != 0).sum(axis=1)
            for k in range(len(X)):
                hist[(int(sup[k]), mr[k] != 0)] += 1
                if mr[k] == 0: nond.append((y0, X[k].copy()))
    tot += good
    print('y0', y0, 'cand sizes', sorted(S.sizes.values())[:4], '... nodes', S.nodes, 'leaves', len(leaves), 'with col support >= m', good, 'nonDita so far', len(nond), '%.0fs' % (time.time() - t0), flush=True)
pickle.dump({'hist': hist, 'nond': nond, 'total': tot, 'reps': reps}, open(out, 'wb'))
print('DONE', tot, len(nond), flush=True)
