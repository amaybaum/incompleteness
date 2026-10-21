import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from collections import defaultdict
from rep import *
tot = fail = same = samefail = 0; purUpairs = 0; lackpure = 0
for n in range(2, 7):
    for r in range(1, n):
        for na, nb in [(1,1),(1,2),(1,3),(2,1),(2,2)]:
            if n < na + nb: continue
            res = realization(r, n - r, na, nb)
            pure = [c for c in res['PABl'] if extreme(c, res['PABl'])]
            def mA(c):
                m = defaultdict(F)
                for k, v in c.items(): m[k[:na]] += v
                return {k: v for k, v in m.items() if v}
            margs = [mA(c) for c in pure]
            lack = [s for s in res['PAl'] if s not in margs]
            pureA = [s for s in res['PAl'] if extreme(s, res['PAl'])]
            lackpure += sum(1 for s in lack if s in pureA)
            # Pur-U pairs: distinct pure AB states with equal A-marginal
            purUpairs += sum(1 for i in range(len(pure)) for j in range(i) if margs[i] == margs[j])
            tot += 1; fail += bool(lack)
            if na == nb: same += 1; samefail += bool(lack)
print(f'Pur-E: realizations={tot} with a preparable A-state lacking a purification={fail}; same-type {samefail}/{same}; '
      f'pure A-states lacking a purification (summed)={lackpure}; Pur-U pairs with equal A-marginal={purUpairs}')
