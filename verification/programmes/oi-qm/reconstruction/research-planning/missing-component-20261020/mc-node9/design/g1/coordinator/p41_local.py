# Coordinator re-check of a review figure (REVIEW-G1-8d90f77e, F6 and table 1(d), last row): P4_1 (at most one
# coupling, all lengths) over the alphabets without swap_B, with swap lifts supported on their own system.
# Uses the reviewer's engine (../review/eng.py); exact pair-BFS over conditioned states.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review'))
from eng import *
from collections import Counter
C = Cards(); std = QM(lift_tables(0, 0, 0))
def kcouple(k): return (0, lambda op, x: (None if x + 1 > k else x + 1) if op == 'c' else x)
LOC = [t for t in TRIPLES if t[0] % 4 == 0 and t[1] // 4 == 0]
W6 = ['sA', 'c'] * 3; W7 = W6 + ['sA']
def wit(t, word):
    th = QM(lift_tables(*t)); S = th.init()
    for op in word: S = th.gate(op, S)
    return str(th.read('rB', S).get(1, (0,))[0])
for name, A in [('full', FULL), ('{sA,c,rA,rB}', ['sA', 'c', 'rA', 'rB']),
                ('no sB', ['sA', 'c', 'xA', 'zA', 'xB', 'zB', 'rA', 'rB'])]:
    ok = [t for t in LOC if first_disagreement(C, QM(lift_tables(*t)), A, extra=kcouple(1)) is None]
    qm = [t for t in ok if first_disagreement(std, QM(lift_tables(*t)), A) is None]
    print('P4_1, local swap lifts, %s: passing %d of %d; == std QM over alphabet %d; (W6,W7) among passing: %s' % (
        name, len(ok), len(LOC), len(qm), sorted(Counter((wit(t, W6), wit(t, W7)) for t in ok).items())))
