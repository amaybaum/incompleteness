# confirmatory (not a verdict): delta_k == 2*eps_coarse exactly on all E'/G cells; BB envelope size
import sys, itertools
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 60
src1 = open(sys.argv[1]).read().split("fail = 0")[0]; ns1 = {}; exec(src1, ns1)
src2 = open(sys.argv[2]).read().split("fail = 0")[0]; ns2 = {}; exec(src2, ns2)
bad = 0; n = 0
for d in (2, 3):
    for r in (F(1, 10**12), F(1, 1000), F(1, 2)):
        law, eg = ns1['hmm_law'](d, r, 7, True); g = ns1['gaps'](law, 7)
        for k in g:
            ec, ef = ns1['eps_values'](eg, d, k); n += 1; bad += g[k][0] != 2 * ec
        law, rg = ns2['hmm_G'](d, r, 7); g = ns2['gaps'](law, 7)
        for k in g:
            ec = max(abs(v[1] / (v[0] + v[1]) - F(1, 2)) for h, v in rg.items() if len(h) == k + 1)
            n += 1; bad += g[k][0] != 2 * ec
print(f"delta_k == 2*eps_coarse exactly: {n-bad}/{n} cells")
x = Decimal(10)**6
for nv in (2, 10**80):
    env = 2 / Decimal(2).ln() * (-x).exp() * (x + 1 + Decimal(nv - 1).ln())
    print(f"n_V={nv}: envelope (2/ln2) e^-x (x+1+ln(nV-1)) at x=1e6: 10^{env.log10():.3f}")
