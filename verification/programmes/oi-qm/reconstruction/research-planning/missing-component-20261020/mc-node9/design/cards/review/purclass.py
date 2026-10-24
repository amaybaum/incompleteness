import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from collections import defaultdict, Counter
from rep import *
C = Counter()
def any_size(s, na):
    """exact: smallest n >= na+1 (nonempty purifier) with an E(M) on n slots whose na-slot marginal is s, else None"""
    p = sum(v for k, v in s.items() if k[0] == 'R')
    if na == 1:
        return max(p.denominator, 2)  # n = multiple of denominator, at least 2 slots
    prr = s.get(('R', 'R'), F(0)); sym = s.get(('R', 'B'), F(0)) == s.get(('B', 'R'), F(0))
    if not sym: return None
    if p in (0, 1): return 3
    if p * p == prr: return None
    n = (p - prr) / (p * p - prr)
    if n.denominator != 1 or n < 3 or (p * n).denominator != 1: return None
    n = int(n); r = int(p * n)
    return n if E(r, n) and all(sum(v for k, v in E(r, n).items() if k[:2] == key) == s.get(key, 0) for key in [('R','R'),('R','B'),('B','R'),('B','B')]) else None
for n in range(2, 7):
    for r in range(1, n):
        for na, nb in [(1,1),(1,2),(1,3),(2,1),(2,2)]:
            if n < na + nb: continue
            res = realization(r, n - r, na, nb)
            pure = [c for c in res['PABl'] if extreme(c, res['PABl'])]
            margs = []
            for c in pure:
                m = defaultdict(F)
                for k, v in c.items(): m[k[:na]] += v
                margs.append({k: v for k, v in m.items() if v})
            pureA = [s for s in res['PAl'] if extreme(s, res['PAl'])]
            for s in res['PAl']:
                if s in margs: continue
                mono = len(s) == 1 and len(set(next(iter(s)))) == 1
                tag = 'pure A' if s in pureA else 'mixed A'
                if s in pureA and not mono: C[(tag, 'non-monochrome pure: no purification at any size')] += 1; continue
                ns = any_size(s, na)
                if ns is None:
                    pr = sum(v for k, v in s.items() if k[0] == 'R')
                    why = 'positive dependence' if na == 2 and s.get(('R','R'),0) >= pr*pr else 'no E(M) at any size (other)'
                    C[(tag, why)] += 1
                elif ns <= na + nb: C[(tag, 'scarcity: E(M) on |AB| slots exists, not preparable here')] += 1
                else: C[(tag, f'size: needs |AB| >= {ns}')] += 1
for k, v in sorted(C.items()): print(v, k)
