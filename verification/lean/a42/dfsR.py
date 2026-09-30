"""m = 0 case, domain {-1,0,1}: exhaustive DFS per nonzero-row set R (row set Z = complement of R is exactly the set of
zero rows).  Each row i in R is a pair (P, N) of disjoint column sets, each a common-vanishing set for row i against
every zero row (Lemma CV), not both empty, 0 a mode of the row.  Pair compatibility within R by the exact tables.
Budget: total support <= BUDGET."""
import sys, time, pickle, collections
import numpy as np
from dfs42 import VT, PC, compat, FULL
from classify42 import member_masks, KEYS
from lib42 import straight, straight_direct

BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 47
msize = np.load('msize.npy')

def cv_list(i, Z):
    V = np.ones(1 << 16, dtype=bool)
    for r in range(16):
        if (Z >> r) & 1: V &= VT[i, r]
    return np.flatnonzero(V)

def row_cands(i, Z, lo, hi):
    L = cv_list(i, Z)                     # includes 0
    L = L[PC[L] <= min(8, hi)]
    Ps, Ns = [], []
    for P in L.tolist():
        N = L[(L & P) == 0]
        p = PC[P]; n = PC[N]; z = 16 - p - n
        ok = (z >= p) & (z >= n) & (p + n >= max(lo, 1)) & (p + n <= hi)
        Ps.append(np.full(int(ok.sum()), P, dtype=np.int64)); Ns.append(N[ok])
    P = np.concatenate(Ps); N = np.concatenate(Ns)
    return P, N, (PC[P] + PC[N]).astype(np.int64)

class RSearch:
    def __init__(self, R):
        self.R = R; self.Z = FULL ^ R
        self.rows = [i for i in range(16) if (R >> i) & 1]
        self.ms = {i: int(msize[i, self.Z]) for i in self.rows}
        lb = sum(self.ms.values())
        self.C = {}
        for i in self.rows:
            hi = BUDGET - (lb - self.ms[i])
            self.C[i] = row_cands(i, self.Z, self.ms[i], hi)
        self.nodes = 0; self.leaves = []
    def run(self):
        if any(len(self.C[i][0]) == 0 for i in self.rows): return
        cand = {i: np.arange(len(self.C[i][0])) for i in self.rows}
        self._rec(cand, {}, 0)
    def _rec(self, cand, assigned, used):
        self.nodes += 1
        free = list(cand)
        mins = {r: int(self.C[r][2][cand[r]].min()) for r in free}
        slack = BUDGET - used - sum(mins.values())
        if slack < 0: return
        i = min(free, key=lambda r: len(cand[r]))
        ci = cand[i]; CP, CN, CS = self.C[i]
        ci = ci[CS[ci] <= mins[i] + slack]
        rest = [r for r in free if r != i]
        for n in ci.tolist():
            y = (int(CP[n]), int(CN[n]))
            if not rest:
                assigned[i] = y; self.leaves.append(dict(assigned)); del assigned[i]; continue
            new = {}; ok = True
            for r in rest:
                c = cand[r]; RP, RN, RS = self.C[r]
                c = c[compat(RP[c], RN[c], y, r, i)]
                if not len(c): ok = False; break
                new[r] = c
            if not ok: continue
            assigned[i] = y
            self._rec(new, assigned, used + int(CS[n]))
            del assigned[i]

def to_flat(assigned):
    E = np.zeros(256, dtype=np.int64)
    for i, (P, N) in assigned.items():
        for k in range(16):
            if (P >> k) & 1: E[i * 16 + k] = 1
            elif (N >> k) & 1: E[i * 16 + k] = -1
    return E

if __name__ == '__main__':
    Rlist = [int(x) for x in open(sys.argv[2]).read().split()]
    out = sys.argv[3]
    t0 = time.time(); hist = collections.Counter(); nond = []; tot = 0
    for n, R in enumerate(Rlist):
        S = RSearch(R); S.run()
        if S.leaves:
            X = np.array([to_flat(a) for a in S.leaves])
            ms, mr = member_masks(X)
            sup = (X != 0).sum(axis=1)
            for k in range(len(X)):
                hist[(int(sup[k]), mr[k] != 0)] += 1
                if mr[k] == 0 and ms[k] == 0: nond.append((R, X[k].copy()))
            tot += len(X)
        if n % 20 == 0 or S.nodes > 100000:
            print('R#%d %s r=%d nodes %d leaves %d | total leaves %d nonDita %d  %.0fs' % (n, hex(R), bin(R).count('1'), S.nodes, len(S.leaves), tot, len(nond), time.time() - t0), flush=True)
    pickle.dump({'hist': hist, 'nond': nond, 'total': tot, 'Rs': Rlist}, open(out, 'wb'))
    print('DONE total leaves', tot, 'nonDita', len(nond), '%.0fs' % (time.time() - t0), flush=True)
