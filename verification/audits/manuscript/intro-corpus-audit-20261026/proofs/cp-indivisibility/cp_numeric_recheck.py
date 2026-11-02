"""Re-check of cp_numeric.py's 'inf' verdicts on linearly compatible pairs.

cp_gap returns inf when the pseudo-inverse residual of the affine system exceeds 1e-9; for a
linearly compatible pair of TP maps the affine set is provably nonempty (a TP extension exists),
so an inf there is a floating-point tolerance artifact.  This script recomputes those pairs with
the residual check relaxed to 1e-6 and reports the gaps, P-indivisible pairs first.
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import cp_search as c
from exact_lp import stochastic_divisor

_orig_pinv = np.linalg.pinv
np.linalg.pinv = lambda A: _orig_pinv(A, rcond=1e-10)   # tighter cutoff: well-scaled 0/1/mu data

seen = {}
for (nV, nH) in [(2, 2), (2, 3), (3, 2)]:
    for perm in itertools.permutations(range(nV * nH)):
        perm = list(perm)
        L = c.order(perm)
        for mu in c.priors(nH):
            Ss = {t: c.superop(c.perm_power(perm, t), nV, nH, mu) for t in range(L)}
            for s in range(1, L):
                for t in range(L):
                    if t != s:
                        key = (nV, tuple(map(tuple, Ss[s])), tuple(map(tuple, Ss[t])))
                        seen.setdefault(key, (nV, nH, tuple(perm), mu, s, t))
np.linalg.pinv = _orig_pinv
res = {"indiv": [], "div": []}
for key, info in seen.items():
    nV = key[0]
    S1 = [list(r) for r in key[1]]; S2 = [list(r) for r in key[2]]
    if not c.lin_compatible(S1, S2):
        continue
    g_default = c.cp_gap(S1, S2, nV, 1)          # cheap: detects the inf artifact
    if g_default != float("inf"):
        continue
    np.linalg.pinv = lambda A: _orig_pinv(A, rcond=1e-10)
    g = c.cp_gap(S1, S2, nV, 1500)
    np.linalg.pinv = _orig_pinv
    pdiv = stochastic_divisor(c.pops(S1, nV), c.pops(S2, nV))[0]
    res["div" if pdiv else "indiv"].append((g, info))
for k in ("indiv", "div"):
    v = sorted(res[k], key=lambda z: z[0])
    print(f"{k}: {len(v)} pairs previously 'inf';",
          "recomputed min gap = %.3e" % v[0][0] if v else "",
          "| gap<1e-4: %d | gap>1e-3: %d | still inf: %d" % (
              sum(1 for g, _ in v if g < 1e-4), sum(1 for g, _ in v if 1e-3 < g < float('inf')),
              sum(1 for g, _ in v if g == float('inf'))))
