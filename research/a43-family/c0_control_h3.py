"""Control 0: the d-parameter harness reproduces act 40 on H3 exactly, and agrees key-by-key with the frozen 3-dim classifier."""
import time, sys
from lib43 import *
t0 = time.time()
fails = []
def chk(name, got, want):
    ok = got == want; print('  %s  %-80s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)), flush=True)
    if not ok: fails.append(name)
S = summarize([PA, PB, PC])
chk('H3 candidates', S['ncand'], 46)
chk('H3 nonempty strict loci', S['n_nonempty'], 30)
chk('strict == relaxed per candidate', S['strict_eq_relaxed'], True)
chk('all loci coordinate', S['all_coordinate'], True)
chk('maximal loci', sorted(F.show() for F in S['maximal']), ['u1 = -1', 'u1 = 1', 'u2 = 1', 'u3 = -1', 'u3 = 1'])
chk('covered', S['covered'], True)
print('  (%.0fs)' % (time.time() - t0), flush=True)
# key-by-key agreement with the frozen 3-dim classifier
OR3, C3, ST3, L3 = P40['classify'](PA, PB, PC)
chk('frozen classifier: same candidate keys', set(C3) == set(S['loci']), True)
chk('frozen classifier: same strict and relaxed loci (canonical bases)', all(((L3[k][0] is None) == (S['loci'][k][0] is None)) and (L3[k][0] is None or L3[k][0].B == S['loci'][k][0].B) and ((L3[k][1] is None) == (S['loci'][k][1] is None)) and (L3[k][1] is None or L3[k][1].B == S['loci'][k][1].B) for k in C3), True)
chk('joint realizability of (A, B, C): level sets over unordered pairs, bad', joint_realizable([PA, PB, PC])[1], 0)
chk('census hulls of A, B, C, A+B, A+C, B+C, A+B+C (spans)', [census_hulls(x) for x in ([PA], [PB], [PC], [PA, PB], [PA, PC], [PB, PC], [PA, PB, PC])],
    [[('k2', 'row'), ('k4', 'row'), ('e2', 'row'), ('t1', 'column'), ('t1', 'row'), ('t2', 'row'), ('t3', 'row')],
     [('k1', 'row'), ('k4', 'column'), ('t1', 'row'), ('t2', 'column')],
     [('k2', 'column'), ('t1', 'column'), ('t2', 'column'), ('t3', 'column'), ('t3', 'row')],
     [('t1', 'row')], [('t1', 'column'), ('t3', 'row')], [('t2', 'column')], []])
# the d = 0 classifier on SIG: act 37's census, 18 structures
chk('d = 0 classifier at SIG: 18 structures', len(all_structures_of_base(None)), 18)
print('  (%.0fs)' % (time.time() - t0))
print('c0:', 'FAILED %s' % fails if fails else 'OK')
