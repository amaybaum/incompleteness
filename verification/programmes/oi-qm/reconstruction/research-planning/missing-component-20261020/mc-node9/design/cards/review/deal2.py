import sys, os, itertools; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from rep import *
# (1) deal-2 statistics on A = 1 slot, B = 2 slots: preparable (mixed) in the base theory?
q = F(1, 4); deal2 = {('R','R','B'): q, ('R','B','R'): q, ('B','R','R'): q, ('R','R','R'): q}
for deck in [(3,1),(3,2),(3,3),(4,2)]:
    res = realization(deck[0], deck[1], 1, 2)
    print('deck', deck, 'A1B2: deal-2 statistics preparable:', deal2 in res['PABl'], '; extreme:', extreme(deal2, res['PABl']) if deal2 in res['PABl'] else None)
# check it is deal 2: B=(b1,b2) labels; prediction of a1 from B; A-marginal
pred = sum(max(sum(v for k, v in deal2.items() if k[1:] == b and k[0] == a) for a in 'RB') for b in {k[1:] for k in deal2})
print('deal-2 stats: P(a1=R) =', sum(v for k, v in deal2.items() if k[0]=='R'), ' B predicts a1 with success', pred)
# (2) M1 witness E(RRRB) on 2+2 split: joint of (a1; b1 b2) and prediction
psi = E(3, 4)
j = defaultdict(F)
for k, v in psi.items(): j[(k[0],) + k[2:]] += v
pred = sum(max(j.get((a,) + b, 0) for a in 'RB') for b in {k[1:] for k in j})
print('M1 witness (2+2): joint (a1; b1 b2) =', dict(j), ' B predicts a1 with success', pred)
predA = sum(max(sum(v for k, v in psi.items() if k[:2] == a and k[2:] == b) for a in {k[:2] for k in psi}) for b in {k[2:] for k in psi})
print('M1 witness (2+2): B predicts A=(a1,a2) with success', predA, '; B predicts A colour count with success',
      sum(max(sum(v for k, v in psi.items() if k[2:] == b and k[:2].count('R') == c) for c in range(3)) for b in {k[2:] for k in psi}))
# (3) any card encoding of the abstract deal 2 (A one slot, B three slots, injective labelling) exchangeable?
arr3 = list(itertools.product('RB', repeat=3)); D2 = [(0,0),(0,1),(0,2),(1,0)]
cnt = 0; ex = 0
for lab in itertools.permutations(arr3, 4):
    for amap in (('R','B'), ('B','R')):
        st = {(amap[a],) + lab[b]: F(1,4) for a, b in D2}
        d = {('', k): v for k, v in st.items()}
        cnt += 1; ex += exchangeable(d)
print('abstract deal 2, A=1 slot, B=3 slots: encodings', cnt, 'exchangeable', ex)
