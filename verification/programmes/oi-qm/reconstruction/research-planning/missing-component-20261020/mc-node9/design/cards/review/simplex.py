import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from collections import defaultdict
from rep import *
bad = 0; tot = 0; states = 0; prodwit = 0
for n in range(2, 7):
    for r in range(n + 1):
        for na, nb in [(1,1),(1,2),(2,1),(2,2)]:
            if n < na + nb: continue
            res = realization(r, n - r, na, nb); tot += 1
            ext = [c for c in res['PABl'] if extreme(c, res['PABl'])]
            cnts = [{k.count('R') for k in c} for c in ext]
            assert all(len(s) == 1 for s in cnts)
            vert = {next(iter(s)): c for s, c in zip(cnts, ext)}
            for c in res['PABl']:
                states += 1
                w = defaultdict(F)
                for k, v in c.items(): w[k.count('R')] += v
                rec = defaultdict(F)
                ok = all(m in vert for m in w)
                if ok:
                    for m, wm in w.items():
                        for k, v in vert[m].items(): rec[k] += wm * v
                    ok = dict(rec) == c
                bad += not ok
            # products among preparable AB states with non-monochrome factors
            for c in res['PABl']:
                ma = defaultdict(F); mb = defaultdict(F)
                for k, v in c.items(): ma[k[:na]] += v; mb[k[na:]] += v
                if all(c.get(a + b, 0) == ma[a] * mb[b] for a in ma for b in mb) and not (len(ma) == 1 and len(mb) == 1 and len(set(next(iter(ma)) + next(iter(mb)))) == 1):
                    prodwit += 1
print(f'realizations={tot} preparable AB states={states}: not the unique count-mixture of preparable E(M) vertices: {bad}; '
      f'preparable AB states that are products and not monochrome: {prodwit}')
