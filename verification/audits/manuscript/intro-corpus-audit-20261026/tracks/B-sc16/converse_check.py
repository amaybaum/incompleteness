"""Exhaustive check of the true converse (Proposition C) and of Proposition B.
 C: full-support visible prior, window {0..n}: R1 fails on {0..n}  =>  a C4 gap at some order k <= n-1.
 B: hidden prior a point mass: a C4 gap at order k  =>  R1 fails on {0..k+1}, witnessed by the pair (k, k+1).
python3 -I -B converse_check.py nV nH prior"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from itertools import permutations
from oi_exact import Model, divisor
from enumerate_all import prior

nV, nH, label = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
viol_C = viol_B = checked_C = checked_B = 0
for p in permutations(range(nV * nH)):
    M = Model(nV, nH, list(p), prior(nH, label))
    top = M.L            # every window, accessible or not, up to the order of phi
    gaps = [M.gap(k)[0] > 0 for k in range(0, top + 1)]
    pair = {}
    def dv(s, t):
        if (s, t) not in pair:
            pair[(s, t)] = divisor(M.Gamma(s), M.Gamma(t))[0]
        return pair[(s, t)]
    for n in range(2, top + 1):
        r1 = all(dv(s, t) for t in range(2, n + 1) for s in range(1, t))
        if not r1:
            checked_C += 1
            if not any(gaps[1:n]):
                viol_C += 1
    if label == 'pure':
        for k in range(1, top):
            if gaps[k]:
                checked_B += 1
                if dv(k, k + 1):
                    viol_B += 1
print(f'({nV},{nH}) prior={label}: Prop C windows with R1 failing: {checked_C}, without a gap at order <= n-1: {viol_C} '
      f'[{"GREEN" if viol_C == 0 else "RED"}]'
      + (f'; Prop B gap orders checked: {checked_B}, pair (k,k+1) divisible: {viol_B} [{"GREEN" if viol_B == 0 else "RED"}]' if label == 'pure' else ''))
