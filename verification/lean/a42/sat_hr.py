"""High-r zero-row case, domain {-1,0,1} min representatives: a zero row (WLOG row 0, by row transitivity; existence
only, no Dita test), at most 2 zero rows and at most 2 zero columns (WLOG #zero columns <= #zero rows by
transposition), 0 a mode of every line, support <= B. UNSAT means no straight line at all in this regime."""
import sys, time
from pysat.solvers import Cadical153
from sat42 import Enc
from lib42 import straight_direct, support
B = int(sys.argv[1]); t0 = time.time()
e = Enc(); e.straight(); e.mode0(); e.support_le(B)
for j in range(16): e.cnf.append([e.z[0][j]])
rows_nz = [e.OR([e.nz(i, j) for j in range(16)]) for i in range(16)]
cols_nz = [e.OR([e.nz(i, j) for i in range(16)]) for j in range(16)]
e.card(rows_nz, 14, 'ge'); e.card(cols_nz, 14, 'ge')
print('B', B, 'clauses', len(e.cnf.clauses), flush=True)
s = Cadical153(bootstrap_with=e.cnf.clauses); ok = s.solve()
print('SAT' if ok else 'UNSAT', '%.0fs' % (time.time() - t0), flush=True)
if ok:
    E = e.decode(s.get_model()); print('support', support(E), 'straight_direct', straight_direct(E))
    for r in E: print(' '.join('%2d' % x for x in r))
