"""Sufficient condition for window indivisibility: Dobrushin revival.
delta(G) = max_{a,b} TV(G(a,.), G(b,.)). If G_t = G_s Lam with Lam stochastic then delta(G_t) <= delta(G_s).
Check over every bijection at (2,2),(2,3),(3,2),(2,4) and every pair s < t <= L: whenever
delta(G_t) > delta(G_s), the exact LP must report no divisor (consistency control).
Also count gap-bearing bijections that are P-divisible on the whole pre-recurrence window {0..L-1}."""
import importlib.util, sys, os
from fractions import Fraction as Fr
from itertools import permutations
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('trackd_lib', os.path.join(HERE, 'trackd_lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

def dob(G):
    n = len(G)
    return max(sum(abs(G[a][j] - G[b][j]) for j in range(n)) / 2 for a in range(n) for b in range(n))

green = True
for (nV, nH) in [(2, 2), (2, 3), (3, 2), (2, 4)]:
    rev_pairs = rev_violations = 0
    gap_bij = full_window = 0
    for perm in permutations(range(nV * nH)):
        perm = list(perm)
        Lo = L.perm_order(perm)
        G = L.rooted_family(perm, nV, nH, Lo)
        for t in range(1, Lo + 1):
            for s in range(t):
                if dob(G[t]) > dob(G[s]):
                    rev_pairs += 1
                    if L.divisor(G[s], G[t])[0]:
                        rev_violations += 1
        P = L.law_from_trajs(L.trajectories(perm, nV, nH, Lo))
        if any(L.gap_at(P, k, nV)[0] for k in range(1, Lo)):
            gap_bij += 1
            if L.p_divisible_window(G, Lo - 1)[0]:
                full_window += 1
    green &= rev_violations == 0
    print(f'({nV},{nH}): revival pairs={rev_pairs}, revival pairs with a stochastic divisor={rev_violations}; '
          f'bijections with a gap at some order < L: {gap_bij}, of which P-divisible on all of {{0..L-1}}: {full_window}')
print('REVIVAL CHECK', 'GREEN' if green else 'RED')
