#!/usr/bin/env python3
"""E2: independent checks of the BH-02 results the Introduction (L162) cites.
(1) C1: under a permutation of configurations, the orbit of a configuration basis state is a
    configuration basis state, so every aligned bipartition has Schmidt rank 1 (S(R) = 0).
    Exhaustive at (q,n) = (2,2), (2,3): for every permutation and configuration, every orbit
    state's amplitude matrix at every aligned cut has exactly one nonzero entry.
(2) C6(c) diagonal shell span{|i>|i>}: exact Haar mean H_m - 1 against the exact Page value
    S_Page(m,m) = sum_{k=m+1}^{m^2} 1/k - (m-1)/(2m), m = 2, 3, 4, 8, 16 (rational comparison).
(3) C6(c) Hamming-weight shells: the concavity bound E[S] <= S(E rho_R), with
    E rho_R = sum_k C(n-r, w-k)/C(n,w) P_k (P_k the weight-k projector of R), compared with
    S_Page(2^r, 2^(n-r)) by mpmath interval arithmetic, for (n,w,r) = (8,2,4), (10,2,5),
    (12,3,6) (claimed below S_Page) and the half-filling cases (6,3,3), (8,4,4), (10,5,5)
    (claimed inconclusive).
The Haar-mean formula H_m - 1 itself is the standard result for the Shannon entropy of
|c_i|^2 of a Haar-random unit vector in C^m (nats); it is taken as input, not re-derived.

Usage: python3 -I E2_bh02.py [out.json]
"""
import itertools, json, os, sys
from fractions import Fraction as F
from math import comb
from mpmath import iv

iv.dps = 50
out = {}

# (1) C1 sweeps
def c1_sweep(q, n):
    confs = list(itertools.product(range(q), repeat=n))
    cuts = [c for r in range(1, n) for c in itertools.combinations(range(n), r)]
    bad = 0; perms = 0
    for img in itertools.permutations(range(len(confs))):
        perms += 1
        for s0 in range(len(confs)):
            state = {s0: 1}                     # amplitude vector, sparse
            seen = set()
            while True:
                (s, a), = state.items() if len(state) == 1 else (None,)
                key = s
                if key in seen:
                    break
                seen.add(key)
                for cut in cuts:
                    nz = {(tuple(confs[x][i] for i in cut), tuple(confs[x][i] for i in range(n) if i not in cut))
                          for x, amp in state.items() if amp}
                    if len(nz) != 1:
                        bad += 1
                state = {img[x]: amp for x, amp in state.items()}
                if len(state) != 1:
                    bad += 1; break
    return perms, bad
for q, n in ((2, 2), (2, 3)):
    p, b = c1_sweep(q, n)
    out["C1_q%d_n%d" % (q, n)] = {"permutations": p, "states_with_rank_gt_1": b}

# (2) diagonal shell
def s_page(m, n):
    if m > n:
        m, n = n, m
    return sum(F(1, k) for k in range(n + 1, m * n + 1)) - F(m - 1, 2 * n)
def harmonic(m):
    return sum(F(1, k) for k in range(1, m + 1))
claimed = {2: F(1, 2), 3: F(5, 6), 4: F(13, 12), 8: F(481, 280), 16: F(1715839, 720720)}
diag = {}
for m in (2, 3, 4, 8, 16):
    hm1 = harmonic(m) - 1
    diag[m] = {"H_m-1": str(hm1), "matches_report": hm1 == claimed[m], "S_Page(m,m)": float(s_page(m, m)),
               "above_S_Page_exact": hm1 > s_page(m, m)}
out["C6c_diagonal_shell"] = diag

# (3) Hamming-weight shells
ham = {}
for n, w, r in ((8, 2, 4), (10, 2, 5), (12, 3, 6), (6, 3, 3), (8, 4, 4), (10, 5, 5)):
    tot = comb(n, w)
    S = iv.mpf(0)
    for k in range(0, min(r, w) + 1):
        lam = F(comb(n - r, w - k), tot)
        if lam:
            S -= comb(r, k) * (lam.numerator / iv.mpf(lam.denominator)) * iv.log(lam.numerator / iv.mpf(lam.denominator))
    sp = s_page(2 ** r, 2 ** (n - r))
    spi = sp.numerator / iv.mpf(sp.denominator)
    ham["(%d,%d,%d)" % (n, w, r)] = {"S(E rho_R)": [float(S.a), float(S.b)], "S_Page": float(sp),
                                     "certified_below": bool(S.b < spi.a), "upper_bound_above_S_Page": bool(S.a > spi.b)}
out["C6c_hamming_shells"] = ham
out["all_as_reported"] = (all(v["states_with_rank_gt_1"] == 0 for k, v in out.items() if k.startswith("C1"))
                          and all(d["matches_report"] and d["above_S_Page_exact"] for d in diag.values())
                          and all(ham[k]["certified_below"] for k in ("(8,2,4)", "(10,2,5)", "(12,3,6)"))
                          and all(ham[k]["upper_bound_above_S_Page"] for k in ("(6,3,3)", "(8,4,4)", "(10,5,5)")))
js = json.dumps(out, indent=1)
if len(sys.argv) > 1:
    if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
        sys.exit("refusing to overwrite this script")
    open(sys.argv[1], "w").write(js + "\n")
print(js)
