"""Enumerate bijections at small (n_V, n_H), uniform priors; window W = {0..r-1}, r = first t>=1 with Gamma_t = I.
Count: (a) models with a gap at some order <= r-2 inside W (C4 on W);
       (b) among (a), models with peak revival R_W > 0 (Lean C4r on W => P-indivisible on W);
       (c) among (a), R_W = 0 (memory-bearing on W, BLP-type revival zero on W).
Also: max R_W over all models, and whether R_W > 0 ever occurs with NO gap in W (should be 0 by the
full-support converse, Track B item 3)."""
import sys
from itertools import permutations
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1])
from regime_exact import rooted, revival, law, gap_orders, perm_model
for nV, nH in [(2, 2), (2, 3), (3, 2)]:
    a = b = c = noGapRev = 0; maxR = Fr(0); total = 0
    for perm in permutations(range(nV * nH)):
        phi = perm_model(perm, nV, nH)
        G = rooted(phi, nV, nH, 1)
        # first visible return r
        t = 1; I = [[Fr(int(i == j)) for j in range(nV)] for i in range(nV)]
        Gs = rooted(phi, nV, nH, 60)
        r = next((t for t in range(1, 61) if Gs[t] == I), None)
        if r is None or r < 3: total += 1; continue
        W = r - 1
        P = law(phi, nV, nH, W)
        gaps = [k for k in gap_orders(P, W)]
        R, B = revival(Gs, W)
        total += 1
        maxR = max(maxR, R)
        if gaps:
            a += 1
            if R > 0: b += 1
            else: c += 1
        elif R > 0:
            noGapRev += 1
    print(f"(n_V,n_H)=({nV},{nH}): bijections {total}; C4-gap inside W: {a}; of these R_W>0: {b}, R_W=0: {c}; "
          f"R_W>0 without a gap in W: {noGapRev}; max R_W = {maxR}")
