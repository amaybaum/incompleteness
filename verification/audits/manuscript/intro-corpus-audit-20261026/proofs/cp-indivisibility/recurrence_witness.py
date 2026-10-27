"""Exact check of the characterization used in the review:

For a permutation dilation with diagonal prior mu, the rooted populations Gamma_t = T(t)
are P-indivisible (some pair s<t has no stochastic divisor)  <=>  some Gamma_k (1<=k<L,
L = order of phi) is not a permutation matrix; and then (k, L) is an indivisible pair
(Gamma_L = I).  Combined with the theorem this gives CP-indivisibility at (k, L).
Exhaustive at (|V|,|H|) in {(2,2),(2,3),(3,2)} with the priors of cp_search.py.
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cp_search as c
from exact_lp import stochastic_divisor


def is_perm(T):
    return all(sorted(r) == [0] * (len(r) - 1) + [1] for r in T) and \
        all(sum(T[i][j] for i in range(len(T))) == 1 for j in range(len(T)))


tot = agree = 0
for (nV, nH) in [(2, 2), (2, 3), (3, 2)]:
    N = nV * nH
    for perm in itertools.permutations(range(N)):
        perm = list(perm)
        L = c.order(perm)
        for mu in c.priors(nH):
            Ts = {t: c.classical_T(c.perm_power(perm, t), nV, nH, mu) for t in range(L)}
            nonperm = [k for k in range(1, L) if not is_perm(Ts[k])]
            # all ordered times s < t within two cycles (residues), s not = 0 mod L
            indiv = any(not stochastic_divisor(Ts[s], Ts[t])[0]
                        for s in range(1, L) for t in range(L) if t != s)
            witness_ok = all(not stochastic_divisor(Ts[k], Ts[0])[0] for k in nonperm)
            tot += 1
            agree += (indiv == bool(nonperm)) and witness_ok
print(f"(perm, prior) instances: {tot}; characterization + (k, L) witness hold in {agree}")
assert agree == tot
print("PASS")
