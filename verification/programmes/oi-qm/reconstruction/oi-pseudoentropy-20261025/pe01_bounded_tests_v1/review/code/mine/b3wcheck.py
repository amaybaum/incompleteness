"""Independent brute force of the B3 window K0 average: max over every test D on a window of
mean_phi |P_phi(D) - Q(D)|, against b3_window_k0's sign-pattern value."""
import sys, itertools
from fractions import Fraction
sys.path.insert(0, sys.argv[1])
import numpy as np
from pe01 import bclasses as B, generators as G, laws as LW

def window_law(X, w):
    cnt = {}
    for row in X:
        z = sum(int(row[t]) << t for t in range(w))
        cnt[z] = cnt.get(z, 0) + 1
    return cnt

def brute_avg(Xs, w):
    """exhaustive over tests (w <= 4) or meet-in-the-middle (w = 5, F = 2)."""
    F = len(Xs); M = Xs[0].shape[0]; P = 1 << w
    # integer deltas: (count * 2^w - M) per point, units 1/(M 2^w)
    D = np.zeros((F, P), dtype=np.int64)
    for f, X in enumerate(Xs):
        c = window_law(X, w)
        for z in range(P):
            D[f, z] = c.get(z, 0) * P - M
    if w <= 4:
        best = 0
        for T in range(1 << P):
            sel = [(T >> z) & 1 for z in range(P)]
            tot = sum(abs(sum(int(D[f, z]) for z in range(P) if sel[z])) for f in range(F))
            best = max(best, tot)
        return Fraction(best, F * M * P)
    assert F == 2 and w == 5
    h = P // 2
    def ssum(rows):  # all subset sums of the first/second half, per phi
        out = np.zeros((F, 1), dtype=np.int64)
        for z in rows:
            out = np.concatenate([out, out + D[:, z:z + 1]], axis=1)
        return out
    A, Bm = ssum(range(h)), ssum(range(h, P))
    best = 0
    for st in range(0, A.shape[1], 2048):
        a0 = A[0, st:st + 2048, None]; a1 = A[1, st:st + 2048, None]
        v = np.abs((a0 + Bm[0][None, :]).astype(np.int32)) + np.abs((a1 + Bm[1][None, :]).astype(np.int32))
        best = max(best, int(v.max()))
    return Fraction(best, F * M * P)

class FakeLaw:
    def __init__(self, X):
        self.X = X; self.M = X.shape[0]; self.kcap = X.shape[1] - 1; self.w = np.ones(X.shape[0], dtype=np.int64)

bad = 0; tot = 0
# (1) synthetic families with small supports: the outside term and F >= 3 Gray walk are exercised
rs = np.random.RandomState(11)
for trial in range(40):
    F = rs.randint(3, 6); S = [4, 8][trial % 2]; L = 6
    Xs = [rs.randint(0, 2, size=(S, L)).astype(np.uint8) for _ in range(F)]
    r = B.b3_window_k0([FakeLaw(X) for X in Xs])
    for w in range(1, 5):
        tot += 1
        mine = brute_avg(Xs, w)
        if r["per_w"][w]["avg"] != mine:
            bad += 1; print("synthetic mismatch", trial, F, S, w, r["per_w"][w]["avg"], mine)
print("synthetic (F=3..5, small supports, outside term active): %d cases, %d mismatches" % (tot, bad))
# (2) real families
for n, fam, ws in ((3, "clk", (1, 2, 3, 4, 5)), (3, "filt", (4,)), (4, "clk", (4, 5)), (4, "filt", (4,)), (5, "filt", (3, 4)), (5, "clk", (4,)), (6, "clk", (4,))):
    gens = G.family(fam, n)
    laws = [LW.Law(g, 20) for g in gens]
    r = B.b3_window_k0(laws)
    for w in ws:
        if w == 5 and len(gens) != 2:
            continue
        mine = brute_avg([l.X for l in laws], w)
        ok = r["per_w"][w]["avg"] == mine
        print("real n=%d %s F=%d w=%d: theirs %s mine %s %s" % (n, fam, len(gens), w, r["per_w"][w]["avg"], mine, "OK" if ok else "MISMATCH"))
    print("   stationary:", r["stationary"])
