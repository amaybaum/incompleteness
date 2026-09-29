"""m = 0 case in the min-rep domain {-K..K} (K = 2 by default): as dfsR2.py, rows are value vectors whose nonzero level
sets are common-vanishing sets for the row against every zero row (Lemma CV), 0 a mode, support >= msize. Pair
compatibility: every nonzero level set of x - y vanishes for the pair (exact tables). Subtree pruning by Lemma NS
(18 census subspaces). Leaves outside the 18 subspaces are stored."""
import sys, os, time, pickle, collections, itertools
import numpy as np
from dfs42 import VT, PC, FULL
from classify42 import member_masks
from lib42 import STRUCTS, SMAT
from dfsR import msize

AR = [SMAT[(nm, tr, True)] for nm, tr, s in STRUCTS]
K = int(os.environ.get('KMAX', '2'))
LABELS = [v for k in range(1, K + 1) for v in (k, -k)]
POW = (1 << np.arange(16)).astype(np.int64)

def cv_list(i, Z):
    V = np.ones(1 << 16, dtype=bool)
    for r in range(16):
        if (Z >> r) & 1: V &= VT[i, r]
    return np.flatnonzero(V)

def row_cands(i, Z, lo, hi):
    """vectorised: every assignment of disjoint common-vanishing level sets to the labels +-1..+-K (each possibly
    empty), support in [max(lo,1), hi], 0 a mode (every label's count <= number of zeros)"""
    L = cv_list(i, Z); L = L[(L > 0) & (PC[L] <= min(8, hi))]
    used = np.zeros(1, dtype=np.int64); parts = [np.zeros(1, dtype=np.int64)]   # masks per label so far
    masks = []
    for li in range(len(LABELS)):
        new_used = [used]; new_m = [np.zeros(len(used), dtype=np.int64)]; src = [np.arange(len(used))]
        for m in L.tolist():
            ok = ((used & m) == 0) & (PC[used] + PC[m] <= hi)
            idx = np.flatnonzero(ok)
            if len(idx): new_used.append(used[idx] | m); new_m.append(np.full(len(idx), m, dtype=np.int64)); src.append(idx)
        srcs = np.concatenate(src); used = np.concatenate(new_used); mm = np.concatenate(new_m)
        masks = [x[srcs] for x in masks] + [mm]
    sup = PC[used].astype(np.int64); z = 16 - sup
    ok = (sup >= max(lo, 1)) & (sup <= hi)
    for x in masks: ok &= PC[x] <= z
    X = np.zeros((int(ok.sum()), 16), dtype=np.int64)
    for lab, x in zip(LABELS, masks):
        xs = x[ok]
        for k in range(16): X[:, k] += lab * ((xs >> k) & 1)
    return X

def compat(X, y, i, i2):
    """rows X (n,16) at index i against the fixed row y at index i2"""
    D = X - y[None, :]; V = VT[i, i2]; ok = np.ones(len(X), dtype=bool)
    for d in range(-2 * K, 2 * K + 1):
        if d == 0: continue
        m = ((D == d).astype(np.int64) * POW).sum(axis=1)
        ok &= V[m]
    return ok

class RSearch3:
    def __init__(self, R, budget):
        self.R = R; self.Z = FULL ^ R; self.budget = budget
        self.rows = [i for i in range(16) if (R >> i) & 1]
        self.ms = {i: int(msize[i, self.Z]) for i in self.rows}
        lb = sum(self.ms.values())
        self.C = {i: row_cands(i, self.Z, self.ms[i], budget - (lb - self.ms[i])) for i in self.rows}
        self.S = {i: (self.C[i] != 0).sum(axis=1) for i in self.rows}
        self.M = {}; self.ids = {}
        for i in self.rows:
            X = self.C[i]
            for k in range(18):
                M = AR[k][:, i * 16:(i + 1) * 16]; self.M[(k, i)] = M
                if len(X) == 0: self.ids[(k, i)] = np.zeros(0, dtype=np.int32); continue
                c8 = np.ascontiguousarray((X @ M.T).astype(np.int8))
                keys = c8.view(np.dtype((np.void, c8.shape[1]))).reshape(-1)
                _, inv = np.unique(keys, return_inverse=True); self.ids[(k, i)] = inv.reshape(-1).astype(np.int32)
        self.nodes = 0; self.pruned = 0; self.leaves = []
    def run(self):
        if any(len(self.C[i]) == 0 for i in self.rows): return
        self._rec({i: np.arange(len(self.C[i])) for i in self.rows}, {}, 0, {k: 0 for k in range(18)})
    def _dita(self, cand, fixedsum):
        for k in range(18):
            tot = fixedsum[k]; ok = True
            for r, c in cand.items():
                ids = self.ids[(k, r)][c]
                if ids.min() != ids.max(): ok = False; break
                tot = tot + self.M[(k, r)] @ self.C[r][c[0]]
            if ok and not np.any(tot): return k
        return None
    def _rec(self, cand, assigned, used, fixedsum):
        self.nodes += 1
        if self._dita(cand, fixedsum) is not None: self.pruned += 1; return
        free = list(cand)
        mins = {r: int(self.S[r][cand[r]].min()) for r in free}
        slack = self.budget - used - sum(mins.values())
        if slack < 0: return
        i = min(free, key=lambda r: len(cand[r]))
        ci = cand[i]; ci = ci[self.S[i][ci] <= mins[i] + slack]
        rest = [r for r in free if r != i]
        for n in ci.tolist():
            y = self.C[i][n]
            nf = {k: fixedsum[k] + self.M[(k, i)] @ y for k in range(18)}
            if not rest:
                assigned[i] = y; self.leaves.append(dict(assigned)); del assigned[i]; continue
            new = {}; ok = True
            for r in rest:
                c = cand[r]; c = c[compat(self.C[r][c], y, r, i)]
                if not len(c): ok = False; break
                new[r] = c
            if not ok: continue
            assigned[i] = y; self._rec(new, assigned, used + int(self.S[i][n]), nf); del assigned[i]

def to_flat(assigned):
    E = np.zeros(256, dtype=np.int64)
    for i, y in assigned.items(): E[i * 16:(i + 1) * 16] = y
    return E

if __name__ == '__main__':
    budget = int(sys.argv[1]); Rlist = [int(x) for x in open(sys.argv[2]).read().split()]; out = sys.argv[3]
    START = int(os.environ.get('START', '0')); Rlist = Rlist[START:]
    t0 = time.time(); hist = collections.Counter(); nond = []; tot = 0
    for n, R in enumerate(Rlist):
        t1 = time.time(); S = RSearch3(R, budget); S.run(); newnd = []
        if S.leaves:
            X = np.array([to_flat(a) for a in S.leaves]); ms, mr = member_masks(X); sup = (X != 0).sum(axis=1)
            for k in range(len(X)):
                hist[(int(sup[k]), bool(mr[k] != 0))] += 1
                if mr[k] == 0: newnd.append((R, X[k].copy()))
            tot += len(X)
        nond += newnd
        if newnd:
            with open(out + '.partial', 'ab') as fh: pickle.dump(newnd, fh)
        print('R#%d %s r=%d cands %s nodes %d pruned %d leaves %d (%.1fs) | total leaves %d nonDita %d  %.0fs' % (n + START, hex(R), len(S.rows), max(len(S.C[i]) for i in S.rows), S.nodes, S.pruned, len(S.leaves), time.time() - t1, tot, len(nond), time.time() - t0), flush=True)
    pickle.dump({'hist': hist, 'nond': nond, 'total': tot}, open(out, 'wb'))
    print('DONE total leaves', tot, 'nonDita', len(nond), '%.0fs' % (time.time() - t0), flush=True)
