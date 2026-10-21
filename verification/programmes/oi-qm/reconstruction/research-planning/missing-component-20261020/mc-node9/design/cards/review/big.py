import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sys
from fractions import Fraction as F
from rep import *
tot = 0; withw = 0; w34 = 0; nonex = 0; nonE = 0
for n in (7, 8):
    for r in range(n + 1):
        for na, nb in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            res = realization(r, n - r, na, nb)
            ps = sorted({sum(v for k, v in ma.items() if k[0] == 'R') for c, ma in res['wit']})
            tot += 1; withw += bool(res['wit']); w34 += F(3, 4) in ps; nonex += res['nonex']; nonE += res['nonE']
            print(f'{r}R{n-r}B A{na}B{nb}: nodes={res["nodes"]} nonexch={res["nonex"]} extAB={res["extAB"]} nonE={res["nonE"]} M1wit={len(res["wit"])} P={[str(x) for x in ps]}', flush=True)
print('TOTAL n=7,8', dict(real=tot, withwit=withw, with34=w34, nonex=nonex, nonE=nonE))
