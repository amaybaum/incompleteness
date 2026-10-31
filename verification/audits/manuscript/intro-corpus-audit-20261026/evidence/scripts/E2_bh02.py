#!/usr/bin/env python3
"""E2: independent checks of the BH-02 results the Introduction (L162) cites.
(1) C1: under a permutation of configurations, the orbit of a configuration basis state is a
    configuration basis state, so every aligned bipartition has Schmidt rank 1 (S(R) = 0).
    Exhaustive at (q,n) = (2,2), (2,3): for every permutation and configuration, the state is
    held as a dense integer amplitude vector, evolved by the permutation matrix, and every
    orbit state's amplitude matrix at every aligned cut is given its exact rank.
    Countercontrols, which must fire: CC-a, the same evolution from the entangled vector
    e_0 + e_last, must reach rank 2 for some permutation; CC-b, the rank of a Bell vector and
    of H-then-CNOT and of a rational rotation then CNOT applied to e_0 (not permutations) must be 2,
    and of CNOT alone (a permutation) 1; CC-c, the orbits of length 1 over all permutations and
    configurations must number N!, the total count of fixed points, so the permutation is applied.
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
def exact_rank(M):
    A = [[F(x) for x in row] for row in M]
    rank, cols = 0, len(A[0]) if A else 0
    for c in range(cols):
        piv = next((r for r in range(rank, len(A)) if A[r][c] != 0), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(len(A)):
            if r != rank and A[r][c] != 0:
                f = A[r][c] / A[rank][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[rank])]
        rank += 1
    return rank

def cut_rank(vec, confs, cut, q, n):
    rest = [i for i in range(n) if i not in cut]
    rows = list(itertools.product(range(q), repeat=len(cut)))
    cols = list(itertools.product(range(q), repeat=len(rest)))
    M = [[0] * len(cols) for _ in rows]
    for x, amp in enumerate(vec):
        M[rows.index(tuple(confs[x][i] for i in cut))][cols.index(tuple(confs[x][i] for i in rest))] += amp
    return exact_rank(M)

def c1_sweep(q, n, start):
    """Number of (permutation, orbit state, cut) with rank > 1, evolving the dense vector start."""
    confs = list(itertools.product(range(q), repeat=n))
    cuts = [c for r in range(1, n) for c in itertools.combinations(range(n), r)]
    bad = perms = fixed = 0
    cache = {}
    for img in itertools.permutations(range(len(confs))):
        perms += 1
        vec = tuple(start)
        steps = 0
        for _ in range(len(confs) + 1):         # an orbit returns within the permutation's order
            if vec not in cache:
                cache[vec] = sum(cut_rank(vec, confs, c, q, n) > 1 for c in cuts)
            bad += cache[vec]
            nxt = [0] * len(vec)
            for x, amp in enumerate(vec):      # (P_pi v)[img[x]] = v[x]
                nxt[img[x]] += amp
            vec = tuple(nxt)
            steps += 1
            if vec == tuple(start):
                break
        fixed += steps == 1
    return perms, bad, fixed

for q, n in ((2, 2), (2, 3)):
    N = q ** n
    bad_total = fixed_total = 0
    for s0 in range(N):
        p, b, f = c1_sweep(q, n, [int(x == s0) for x in range(N)])
        bad_total += b; fixed_total += f
    _, cc_a, _ = c1_sweep(q, n, [int(x in (0, N - 1)) for x in range(N)])
    # Control that the evolution is applied: the (permutation, configuration) pairs whose orbit has length 1 are the
    # fixed points, and the fixed points of all N! permutations number N! (each configuration is fixed by (N-1)!).
    out["C1_q%d_n%d" % (q, n)] = {"permutations": p, "starting_configurations": N,
                                  "rank_gt_1_from_configuration_states": bad_total,
                                  "CC-a_rank_gt_1_from_e0_plus_elast": cc_a,
                                  "CC-c_orbit_length_1_pairs": fixed_total, "CC-c_equals_N!": fixed_total == p}
confs22 = list(itertools.product(range(2), repeat=2))
def apply(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]
def on_site0(g):                                 # g (x) I on {0,1}^2, configuration index 2*x0 + x1
    return [[g[a // 2][b // 2] * (a % 2 == b % 2) for b in range(4)] for a in range(4)]
CNOT = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
e00 = [1, 0, 0, 0]
out["C1_CC-b"] = {"bell_rank": cut_rank([1, 0, 0, 1], confs22, (0,), 2, 2),
                  "h_then_cnot_rank": cut_rank(apply(CNOT, apply(on_site0([[1, 1], [1, -1]]), e00)), confs22, (0,), 2, 2),
                  "rotation_then_cnot_rank": cut_rank(apply(CNOT, apply(on_site0([[3, -4], [4, 3]]), e00)),
                                                      confs22, (0,), 2, 2),
                  "cnot_alone_rank": cut_rank(apply(CNOT, e00), confs22, (0,), 2, 2)}

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
c1 = [out["C1_q2_n2"], out["C1_q2_n3"]]
out["C1_controls_fire"] = (all(v["CC-a_rank_gt_1_from_e0_plus_elast"] > 0 and v["CC-c_equals_N!"] for v in c1)
                           and all(out["C1_CC-b"][k] == 2 for k in ("bell_rank", "h_then_cnot_rank", "rotation_then_cnot_rank"))
                           and out["C1_CC-b"]["cnot_alone_rank"] == 1)
out["all_as_reported"] = (out["C1_controls_fire"] and all(v["rank_gt_1_from_configuration_states"] == 0 for v in c1)
                          and all(d["matches_report"] and d["above_S_Page_exact"] for d in diag.values())
                          and all(ham[k]["certified_below"] for k in ("(8,2,4)", "(10,2,5)", "(12,3,6)"))
                          and all(ham[k]["upper_bound_above_S_Page"] for k in ("(6,3,3)", "(8,4,4)", "(10,5,5)")))
js = json.dumps(out, indent=1)
if len(sys.argv) > 1:
    if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
        sys.exit("refusing to overwrite this script")
    open(sys.argv[1], "w").write(js + "\n")
print(js)
