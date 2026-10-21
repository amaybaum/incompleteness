import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from collections import defaultdict
from rep import *
# H-5 probe: deck composition unknown to the record: RRRR or BBBB with probability 1/2 each (a prior over compositions)
A, B = ['a1', 'a2'], ['b1', 'b2']; menu = Menu(A + B)
start = {('RRRR', ('.',) * 4): F(1, 2), ('BBBB', ('.',) * 4): F(1, 2)}
nodes, depth, bp = closure(menu, start)
PAB, PA = [], []
for d in nodes:
    m = marg(d, A + B, menu.ix)
    if m is not None and m not in PAB: PAB.append(m)
    m = marg(d, A, menu.ix)
    if m is not None and m not in PA: PA.append(m)
print('Prep(AB):', PAB); print('Prep(A):', PA)
for c in PAB:
    ma = defaultdict(F)
    for k, v in c.items(): ma[k[:2]] += v
    print('AB state', dict(c), 'extreme:', extreme(c, PAB), '| A-marginal', dict(ma), 'P(RR) =', ma[('R','R')], 'P(a1=R)^2 =', sum(v for k, v in ma.items() if k[0]=='R')**2)
