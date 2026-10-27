"""Exact check bearing on Intro L106 ("no unconditional implication holds among" (1)-(3)).

Claim tested: P-indivisible rooted populations (notion (2)) => M_t > 0 for some t (notion (1)),
M_t = I(X_<t; X_{t+1} | X_t), with X_0 uniform (full support) and the realization's prior mu.
Exact criterion: M_t > 0 iff two positive-probability histories with the same X_t have
different next-step laws.  Exhaustive over the cp_search instances (t < 2L).
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import cp_search as c
from exact_lp import stochastic_divisor


def has_memory(perm, nV, nH, mu, horizon):
    # path measure over (x0, h0); history = visible sequence
    for t in range(1, horizon):
        laws = {}  # (history up to t) -> dict next -> prob
        for x0 in range(nV):
            for h in range(nH):
                if mu[h] == 0:
                    continue
                s = x0 * nH + h
                hist = [x0]
                for _ in range(t):
                    s = perm[s]
                    hist.append(s // nH)
                nxt = perm[s] // nH
                key = tuple(hist)
                d = laws.setdefault(key, {})
                d[nxt] = d.get(nxt, F(0)) + mu[h]
        bypresent = {}
        for key, d in laws.items():
            tot = sum(d.values())
            law = tuple(sorted((k, v / tot) for k, v in d.items()))
            bypresent.setdefault(key[-1], set()).add(law)
        if any(len(v) > 1 for v in bypresent.values()):
            return True
    return False


n_indiv = n_ok = 0
for (nV, nH) in [(2, 2), (2, 3), (3, 2)]:
    for perm in itertools.permutations(range(nV * nH)):
        perm = list(perm)
        L = c.order(perm)
        for mu in c.priors(nH):
            Ts = {t: c.classical_T(c.perm_power(perm, t), nV, nH, mu) for t in range(L)}
            indiv = any(not stochastic_divisor(Ts[s], Ts[t])[0]
                        for s in range(1, L) for t in range(L) if t != s)
            if indiv:
                n_indiv += 1
                n_ok += has_memory(perm, nV, nH, mu, 2 * L + 1)
print(f"P-indivisible instances: {n_indiv}; with M_t > 0 for some t: {n_ok}")
assert n_ok == n_indiv
print("PASS: (2) => exists t, M_t > 0 on every instance")
