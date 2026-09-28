"""C5: the D-solutions with two rows fixed, by an enumeration independent of census41 (direct exact Gaussian-integer
pair sums by matrix products, no subset tables, no compatibility bitsets, fixed row order, no MRV), compared as a SET
with census41's dump of the same sub-domain; every solution also passes the direct exact Laurent identity.
usage: ctrl_subdomain.py r1 m1 r2 m2 dumpfile"""
import sys, time, json
from lib41 import *
r1, m1, r2, m2, dumpf = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
t0 = time.time()
BITS = ((np.arange(1 << 16)[:, None] >> np.arange(16)[None, :]) & 1).astype(np.int64)     # (65536, 16)
CR = np.array(CRE, dtype=np.int64); CI = np.array(CIM, dtype=np.int64)
def vanish(i, i2, masks):
    b = BITS[masks]; return ((b @ CR[i, i2]) == 0) & ((b @ CI[i, i2]) == 0)
FULL = 0xFFFF
allm = np.arange(1 << 16, dtype=np.int64)
cand = {}
for r in range(1, 16):
    ms = allm if r not in (r1, r2) else np.array([m1 if r == r1 else m2], dtype=np.int64)
    ok = vanish(0, r, ms) & vanish(0, r, FULL ^ ms)
    cand[r] = ms[ok]
def compat(i, a, r, ms):
    x = ms & ~a & FULL; y = ~ms & a & FULL
    return vanish(i, r, x) & vanish(i, r, y)
assert len(cand[r1]) == 1 and len(cand[r2]) == 1, 'fixed masks not admissible'
for r in range(1, 16):
    if r in (r1, r2): continue
    for i, a in ((r1, m1), (r2, m2)):
        cand[r] = cand[r][compat(i, a, r, cand[r])]
assert compat(r1, m1, r2, np.array([m2]))[0]
order = [r for r in range(1, 16) if r not in (r1, r2)]
print('candidate sizes after fixing', {r: len(cand[r]) for r in order}, flush=True)
sols = []
def rec(k, assign, doms):
    if k == len(order):
        sols.append(tuple(assign[r] if r not in (r1, r2) else (m1 if r == r1 else m2) for r in range(1, 16))); return
    r = order[k]
    for a in doms[r].tolist():
        nd = {}; ok = True
        for r2_ in order[k + 1:]:
            d = doms[r2_]; d = d[compat(r, a, r2_, d)]
            if len(d) == 0: ok = False; break
            nd[r2_] = d
        if not ok: continue
        assign[r] = a; rec(k + 1, assign, nd)
rec(0, {}, cand)
py = set(sols)
cs = set(tuple(int(x) for x in line.split()) for line in open(dumpf) if line.strip() and not line.startswith("DONE"))
print('python solutions', len(sols), 'distinct', len(py), '| census41 dump', len(cs), '| sets equal', py == cs, '%.0fs' % (time.time() - t0), flush=True)
bad = 0
for s_ in sorted(py):
    E = [[0] * 16] + [[(s_[i - 1] >> j) & 1 for j in range(16)] for i in range(1, 16)]
    if not straight_line_direct(E): bad += 1
print('direct exact Laurent identity failures', bad, '%.0fs' % (time.time() - t0))
json.dump({'fixed': [[r1, m1], [r2, m2]], 'python': len(py), 'census41': len(cs), 'sets_equal': py == cs, 'direct_failures': bad},
          open('ctrl_subdomain_%d_%d_%d_%d.json' % (r1, m1, r2, m2), 'w'))
