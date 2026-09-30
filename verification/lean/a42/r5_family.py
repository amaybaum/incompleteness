"""R5: act 38's family xA + yB + zC and this thread's xP + yQ + zT, x, y, z in {+-1, +-2}: straightness (exact),
membership in the 976 realizing triples (path B(i)), and the exact class support (R3) with a representative.
Writes r5.json."""
import itertools, json, time
import numpy as np
import triples as T
import minsupp_exact as M
def piece(f): return [[f(i // 4, i % 4, j // 4, j % 4) for j in range(16)] for i in range(16)]
P = piece(lambda a, b, c, d: int(b == 0 and c == 0)); Q = piece(lambda a, b, c, d: int(a == 2 and b % 2 == 1 and d % 2 == 0))
Tt = piece(lambda a, b, c, d: int(a % 2 == 0 and c % 2 == 1 and d == 0))
A = piece(lambda a, b, c, d: int(a % 2 == 1 and b == 3 and c % 2 == 1)); B = piece(lambda a, b, c, d: int(a == 2 and d == 1))
C = piece(lambda a, b, c, d: int((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))))
def lin(cf, Ms): return [[sum(c * X[i][j] for c, X in zip(cf, Ms)) for j in range(16)] for i in range(16)]
ZERO = (T.Fr(0), T.Fr(0))
def gadd(x, y): return (x[0] + y[0], x[1] + y[1])
def straight(E):
    for i in range(16):
        for i2 in range(i + 1, 16):
            acc = {}
            for k in range(16):
                d = E[i][k] - E[i2][k]; acc[d] = gadd(acc.get(d, ZERO), T.gm(T.SIG[i][k], T.gc(T.SIG[i2][k])))
            if any(v != ZERO for v in acc.values()): return False
    return True
t0 = time.time(); CEN = T.census(); TRI = [(k, th) for k, v in CEN.items() for th in v]
out = {}
for fam, pcs in (('ABC', (A, B, C)), ('PQT', (P, Q, Tt))):
    for cf in itertools.product((-2, -1, 1, 2), repeat=3):
        E = lin(cf, pcs); nm = '%s %+d %+d %+d' % (fam, *cf)
        mem = sum(1 for k, th in TRI if T.member(E, k, th))
        try: sup, al, be, _ = M.class_support(E); exact = True
        except ValueError: sup, al, be, exact = None, None, None, False
        rep = None
        if exact:
            rep = (np.array(E) + np.array(al)[:, None] + np.array(be)[None, :]).tolist()
        out[nm] = {'coef': list(cf), 'family': fam, 'straight': straight(E), 'triples_member': mem, 'given_support': sum(1 for r in E for x in r if x),
                   'class_support': sup, 'exact': exact, 'rep_entries': sorted(set(x for r in rep for x in r)) if rep else None, 'rep': rep}
        print('%-16s straight %s  triples %3d  class support %s  (%.0fs)' % (nm, out[nm]['straight'], mem, sup, time.time() - t0), flush=True)
json.dump(out, open('r5.json', 'w'), indent=1, sort_keys=True)
summ = {}
for v in out.values(): summ.setdefault((v['family'], v['straight'], v['triples_member'] == 0, v['class_support']), 0); summ[(v['family'], v['straight'], v['triples_member'] == 0, v['class_support'])] += 1
print('summary (family, straight, outside all triples, class support): count')
for k in sorted(summ, key=str): print('  ', k, summ[k])
