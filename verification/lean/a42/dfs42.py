"""Exhaustive DFS for straight lines in a bounded domain (rows as (P,N) masks: entries in {-1,0,1}),
with a support budget and the row-0 normalization (row 0 = y0, a line of minimum support)."""
import sys, time, pickle, random
import numpy as np
from lib42 import *

PC = np.array([bin(x).count('1') for x in range(1 << 16)], dtype=np.int16)
VT = np.zeros((16, 16, 1 << 16), dtype=bool)
for _i in range(16):
    for _i2 in range(16):
        if _i != _i2: VT[_i, _i2] = vanishing(_i, _i2)

def global_rows():
    """all rows in {-1,0,1}^16 with 0 a mode (#0 >= #(+1), #0 >= #(-1)), as (P, N, support)"""
    def dec(nd):
        x = np.arange(3 ** nd, dtype=np.int64); P = np.zeros_like(x); N = np.zeros_like(x)
        for d in range(nd):
            dig = x % 3; x //= 3
            P |= (dig == 1).astype(np.int64) << d; N |= (dig == 2).astype(np.int64) << d
        return P, N
    Pl, Nl = dec(10); Ph, Nh = dec(6)
    outP, outN = [], []
    for h in range(len(Ph)):
        P = Pl | (Ph[h] << 10); N = Nl | (Nh[h] << 10)
        p = PC[P]; n = PC[N]; z = 16 - p - n
        ok = (z >= p) & (z >= n)
        outP.append(P[ok]); outN.append(N[ok])
    P = np.concatenate(outP); N = np.concatenate(outN)
    return P, N, (PC[P] + PC[N]).astype(np.int64)

def compat(P, N, y, i, i2):
    """rows (P,N) at index i against the fixed row y = (P', N') at index i2: every nonzero level set of x - y
    vanishes for the pair (i, i2) (then the zero level set vanishes too, the total sum being zero)"""
    P2, N2 = y; Z2 = FULL ^ (P2 | N2); Z = FULL ^ (P | N)
    V = VT[i, i2]
    return V[P & N2] & V[(P & Z2) | (Z & N2)] & V[(N & Z2) | (Z & P2)] & V[N & P2]

class Search:
    def __init__(self, G, y0, m, budget, row_order=None):
        self.budget = budget; self.m = m
        P, N, S = G
        self.CP, self.CN, self.CS = {}, {}, {}
        for i in range(1, 16):
            ok = (S >= m) & (S <= budget - m * 14) & compat(P, N, y0, i, 0)
            self.CP[i], self.CN[i], self.CS[i] = P[ok], N[ok], S[ok]
        self.y0 = y0
        self.sizes = {i: len(self.CP[i]) for i in range(1, 16)}
    def run(self, on_leaf, knuth=False, rng=None):
        self.nodes = 0; self.leaves = 0
        cand = {i: np.arange(len(self.CP[i])) for i in range(1, 16)}
        return self._rec(cand, {0: self.y0}, 0, on_leaf, knuth, rng)
    def _rec(self, cand, assigned, used, on_leaf, knuth, rng):
        self.nodes += 1
        free = list(cand)
        mins = {r: int(self.CS[r][cand[r]].min()) for r in free}
        slack = self.budget - used - sum(mins.values())
        if slack < 0: return 0
        i = min(free, key=lambda r: len(cand[r]))
        ci = cand[i]
        ci = ci[self.CS[i][ci] <= mins[i] + slack]
        rest = [r for r in free if r != i]
        if not rest:
            for n in ci.tolist():
                assigned[i] = (int(self.CP[i][n]), int(self.CN[i][n]))
                on_leaf(assigned, used + int(self.CS[i][n])); self.leaves += 1
            assigned.pop(i, None)
            return len(ci)
        order = ci.tolist()
        if knuth:
            good = []
            for n in order:
                y = (int(self.CP[i][n]), int(self.CN[i][n])); new = {}; ok = True
                for r in rest:
                    c = cand[r]; c = c[compat(self.CP[r][c], self.CN[r][c], y, r, i)]
                    if not len(c): ok = False; break
                    new[r] = c
                if ok: good.append((n, new))
            if not good: return 0
            n, new = good[rng.randrange(len(good))]
            assigned[i] = (int(self.CP[i][n]), int(self.CN[i][n]))
            est = len(good) * self._rec(new, assigned, used + int(self.CS[i][n]), on_leaf, knuth, rng)
            del assigned[i]
            return est
        tot = 0
        for n in order:
            y = (int(self.CP[i][n]), int(self.CN[i][n])); new = {}; ok = True
            for r in rest:
                c = cand[r]; c = c[compat(self.CP[r][c], self.CN[r][c], y, r, i)]
                if not len(c): ok = False; break
                new[r] = c
            if not ok: continue
            assigned[i] = y
            tot += self._rec(new, assigned, used + int(self.CS[i][n]), on_leaf, knuth, rng)
            del assigned[i]
        return tot

def to_matrix(assigned):
    E = np.zeros((16, 16), dtype=np.int64)
    for i, (P, N) in assigned.items():
        for k in range(16):
            if (P >> k) & 1: E[i, k] = 1
            elif (N >> k) & 1: E[i, k] = -1
    return E
