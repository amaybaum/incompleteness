"""R3 on E40, act 38's witness and A; writes r3.json."""
import json, time, numpy as np
import minsupp_exact as M
def piece(f): return np.array([[f(i // 4, i % 4, j // 4, j % 4) for j in range(16)] for i in range(16)], dtype=np.int64)
P = piece(lambda a, b, c, d: int(b == 0 and c == 0)); Q = piece(lambda a, b, c, d: int(a == 2 and b % 2 == 1 and d % 2 == 0))
T = piece(lambda a, b, c, d: int(a % 2 == 0 and c % 2 == 1 and d == 0))
A = piece(lambda a, b, c, d: int(a % 2 == 1 and b == 3 and c % 2 == 1)); B = piece(lambda a, b, c, d: int(a == 2 and d == 1))
C = piece(lambda a, b, c, d: int((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))))
out = {}
for nm, E in (('A', A), ('E40', -P + Q - T), ('act38_E', A + B + C)):
    t = time.time(); sup, al, be, rounds = M.class_support(E)
    rep = (E + np.array(al)[:, None] + np.array(be)[None, :])
    out[nm] = {'given_support': int(np.sum(E != 0)), 'class_support': sup, 'alpha': al, 'beta': be, 'rounds': rounds,
               'rep': rep.tolist(), 'rep_support': int(np.sum(rep != 0)), 'rep_entries': sorted(set(rep.flatten().tolist()))}
    print(nm, 'given', out[nm]['given_support'], 'class support', sup, 'rep entries', out[nm]['rep_entries'], '(%.0fs)' % (time.time() - t), flush=True)
json.dump(out, open('r3.json', 'w'), indent=1)
