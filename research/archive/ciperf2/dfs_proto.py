"""Scratch prototype (diagnosis only, not landed code): RSearch2Fast, a data-structure rewrite of a42/dfsR2.RSearch2
with the same search order, the same Lemma NS test and the same leaves. Run old and new on the same row sets and
compare (nodes, pruned, leaves) per R exactly; time both.

usage: python3 dfs_proto.py <shard k> <tools dir> [limit] [mode: both|old|new]
"""
import sys, os, time, json
k = int(sys.argv[1]); TOOLS = sys.argv[2]
LIMIT = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != 'all' else None
MODE = sys.argv[4] if len(sys.argv) > 4 else 'both'
sys.path.insert(0, TOOLS); os.chdir(TOOLS); sys.argv[1:] = ['39']
import numpy as np
from dfs42 import compat, FULL
from dfsR import row_cands, msize
from dfsR2 import RSearch2, AR, vals_matrix, to_flat

NK = len(AR)
SEG = np.cumsum([0] + [a.shape[0] for a in AR])           # segment k of the concatenated equation vector
ACAT = np.vstack(AR)                                      # (2726, 256) int64, all 18 relaxed structures stacked
NZ = [np.flatnonzero(ACAT[:, i * 16:(i + 1) * 16].any(axis=1)) for i in range(16)]


class RSearch2Fast:
    def __init__(self, R, budget, prune=True):
        self.R = R; self.Z = FULL ^ R; self.budget = budget; self.prune = prune
        self.rows = [i for i in range(16) if (R >> i) & 1]
        self.ms = {i: int(msize[i, self.Z]) for i in self.rows}
        lb = sum(self.ms.values())
        self.C = {i: row_cands(i, self.Z, self.ms[i], budget - (lb - self.ms[i])) for i in self.rows}
        # per row i: the full (2726,) contribution of each candidate, as one table (exact int64, one matmul per row);
        # ids[i] is (ncand, 18): candidate equivalence classes per structure, as dfsR2 computes them (int8 byte keys)
        self.T = {}; self.ids = {}
        for i in self.rows:
            X = vals_matrix(self.C[i][0], self.C[i][1])
            nz = NZ[i]; Mi = ACAT[nz, i * 16:(i + 1) * 16]          # only the equations that involve row i
            T = X @ Mi.T
            self.T[i] = T
            ids = np.zeros((len(X), NK), dtype=np.int32)
            if len(X):
                for kk in range(NK):
                    lo, hi = np.searchsorted(nz, SEG[kk]), np.searchsorted(nz, SEG[kk + 1])
                    if lo == hi: continue                            # row i does not enter structure kk: one class
                    c8 = np.ascontiguousarray(T[:, lo:hi].astype(np.int8))
                    keys = c8.view(np.dtype((np.void, c8.shape[1]))).reshape(-1)
                    _, inv = np.unique(keys, return_inverse=True)
                    ids[:, kk] = inv.reshape(-1)
            self.ids[i] = ids
        self.nodes = 0; self.pruned = 0; self.leaves = []

    def run(self):
        if any(len(self.C[i][0]) == 0 for i in self.rows): return
        self._rec({i: np.arange(len(self.C[i][0])) for i in self.rows}, {}, 0, np.zeros(ACAT.shape[0], dtype=np.int64))

    def _dita_subtree(self, cand, fixedsum):
        const = np.ones(NK, dtype=bool); tot = fixedsum.copy()
        for r, c in cand.items():
            sub = self.ids[r][c]
            const &= sub.min(axis=0) == sub.max(axis=0)
            if not const.any(): return None
            tot[NZ[r]] += self.T[r][c[0]]
        for kk in np.flatnonzero(const).tolist():
            if not tot[SEG[kk]:SEG[kk + 1]].any(): return kk
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
            nf = fixedsum.copy(); nf[NZ[i]] += self.T[i][n]
            self._rec(new, assigned, used + int(CS[n]), nf)
            del assigned[i]


def leafkey(S):
    return sorted(tuple(to_flat(a).tolist()) for a in S.leaves)


Rall = [int(x) for x in open('Rle13_39.txt').read().split()]
mine = Rall[k::6][:LIMIT]
agg = {'old': [0.0, 0, 0, 0], 'new': [0.0, 0, 0, 0]}
mism = 0; per = []
for R in mine:
    rec = {'R': R}
    res = {}
    for nm, cls in (('old', RSearch2), ('new', RSearch2Fast)):
        if MODE != 'both' and MODE != nm: continue
        t = time.perf_counter(); S = cls(R, 39, True); S.run(); dt = time.perf_counter() - t
        res[nm] = (S.nodes, S.pruned, len(S.leaves), leafkey(S))
        a = agg[nm]; a[0] += dt; a[1] += S.nodes; a[2] += S.pruned; a[3] += len(S.leaves)
        rec[nm] = [round(dt, 4), S.nodes, S.pruned, len(S.leaves)]
    if MODE == 'both' and res['old'] != res['new']:
        mism += 1; print('MISMATCH', R, rec, flush=True)
    per.append(rec)
print(json.dumps({'shard': k, 'n': len(mine), 'mode': MODE, 'agg': agg, 'mismatches': mism}), flush=True)
json.dump(per, open(os.environ.get('PER_OUT', '/dev/null'), 'w'))
