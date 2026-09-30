"""m = 0 case, min-rep domain {-1,0,1}, per nonzero-row set R: exhaustive DFS as dfsR.py, plus the exact
subtree-Dita pruning (Lemma NS): at a node, if for some census structure S (relaxed) every free row's candidates give
the same value of S's equation vector, and fixed + those values sum to zero, then every leaf below lies in L_S and the
subtree is Dita (it is skipped and counted). Leaves are classified exactly; non-members are stored."""
import sys, os, time, pickle, collections
import numpy as np
from dfs42 import VT, PC, compat, FULL
from classify42 import member_masks, KEYS
from lib42 import STRUCTS, SMAT
from dfsR import row_cands, msize

BROKEN = False
AR = [SMAT[(nm, tr, True)] for nm, tr, s in STRUCTS]

def vals_matrix(P, N):
    X = np.zeros((len(P), 16), dtype=np.int64)
    for k in range(16):
        X[:, k] = ((P >> k) & 1) - ((N >> k) & 1)
    return X

class RSearch2:
    def __init__(self, R, budget, prune=True):
        self.R = R; self.Z = FULL ^ R; self.budget = budget; self.prune = prune
        self.rows = [i for i in range(16) if (R >> i) & 1]
        self.ms = {i: int(msize[i, self.Z]) for i in self.rows}
        lb = sum(self.ms.values())
        self.C = {i: row_cands(i, self.Z, self.ms[i], budget - (lb - self.ms[i])) for i in self.rows}
        # per structure, per row: id of each candidate's equation contribution (exact, via byte keys); vectors are
        # recomputed on demand from a representative candidate
        self.X = {}; self.M = {}; self.ids = {}
        for i in self.rows:
            X = vals_matrix(self.C[i][0], self.C[i][1]); self.X[i] = X
            for k in range(18):
                M = AR[k][:, i * 16:(i + 1) * 16]; self.M[(k, i)] = M
                if len(X) == 0: self.ids[(k, i)] = np.zeros(0, dtype=np.int32); continue
                c8 = np.ascontiguousarray((X @ M.T).astype(np.int8))
                keys = c8.view(np.dtype((np.void, c8.shape[1]))).reshape(-1)
                _, inv = np.unique(keys, return_inverse=True)
                self.ids[(k, i)] = inv.reshape(-1).astype(np.int32)
                del c8, keys
        self.nodes = 0; self.pruned = 0; self.leaves = []
    def run(self):
        if any(len(self.C[i][0]) == 0 for i in self.rows): return
        self._rec({i: np.arange(len(self.C[i][0])) for i in self.rows}, {}, 0, {k: 0 for k in range(18)})
    def _dita_subtree(self, cand, fixedsum):
        for k in range(18):
            tot = fixedsum[k]; ok = True
            for r, c in cand.items():
                ids = self.ids[(k, r)][c]
                if ids.min() != ids.max(): ok = False; break
                tot = tot + self.M[(k, r)] @ self.X[r][c[0]]
            if ok and (BROKEN or not np.any(tot)): return k
        return None
    def _rec(self, cand, assigned, used, fixedsum):
        self.nodes += 1
        free = list(cand)
        if self.prune and self._dita_subtree(cand, fixedsum) is not None:
            self.pruned += 1; return
        mins = {r: int(self.C[r][2][cand[r]].min()) for r in free}
        slack = self.budget - used - sum(mins.values())
        if slack < 0: return
        i = min(free, key=lambda r: len(cand[r]))
        ci = cand[i]; CP, CN, CS = self.C[i]
        ci = ci[CS[ci] <= mins[i] + slack]
        rest = [r for r in free if r != i]
        for n in ci.tolist():
            y = (int(CP[n]), int(CN[n]))
            nf = {k: fixedsum[k] + self.M[(k, i)] @ self.X[i][n] for k in range(18)}
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
            self._rec(new, assigned, used + int(CS[n]), nf)
            del assigned[i]

def to_flat(assigned):
    E = np.zeros(256, dtype=np.int64)
    for i, (P, N) in assigned.items():
        for k in range(16):
            if (P >> k) & 1: E[i * 16 + k] = 1
            elif (N >> k) & 1: E[i * 16 + k] = -1
    return E

if __name__ == '__main__':
    budget = int(sys.argv[1]); Rlist = [int(x) for x in open(sys.argv[2]).read().split()]; out = sys.argv[3]
    START = int(os.environ.get('START', '0')); Rlist = Rlist[START:]
    prune = not (len(sys.argv) > 4 and sys.argv[4] == 'noprune')
    if len(sys.argv) > 4 and sys.argv[4] == 'broken': BROKEN = True
    t0 = time.time(); hist = collections.Counter(); nond = []; tot = 0; stats = []
    for n, R in enumerate(Rlist):
        t1 = time.time(); S = RSearch2(R, budget, prune); S.run()
        if S.leaves:
            X = np.array([to_flat(a) for a in S.leaves]); ms, mr = member_masks(X); sup = (X != 0).sum(axis=1)
            for k in range(len(X)):
                hist[(int(sup[k]), bool(mr[k] != 0))] += 1
                if mr[k] == 0: nond.append((R, X[k].copy()))
            tot += len(X)
        stats.append((R, S.nodes, S.pruned, len(S.leaves), time.time() - t1))
        if S.leaves and any(x[0] == R for x in nond):
            with open(out + '.partial', 'ab') as fh: pickle.dump([x for x in nond if x[0] == R], fh)
        print('R#%d %s r=%d nodes %d pruned %d leaves %d (%.1fs) | total leaves %d nonDita %d  %.0fs' % (n, hex(R), len(S.rows), S.nodes, S.pruned, len(S.leaves), time.time() - t1, tot, len(nond), time.time() - t0), flush=True)
    pickle.dump({'hist': hist, 'nond': nond, 'total': tot, 'stats': stats}, open(out, 'wb'))
    print('DONE total leaves', tot, 'nonDita', len(nond), '%.0fs' % (time.time() - t0), flush=True)
