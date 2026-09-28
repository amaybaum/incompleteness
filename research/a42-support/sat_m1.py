"""No-zero-line case (m >= 1) in the min-rep domain {-1,0,1}: is there a straight E with every row and column nonzero,
0 a mode of every row and column, support <= B, row 0 of support <= 2 (WLOG)?"""
import sys, time
from pysat.solvers import Cadical153
from sat42 import Enc
from lib42 import straight_direct, support
B = int(sys.argv[1]); t0 = time.time()
e = Enc(); e.straight(); e.mode0(); e.lines_ge(1); e.row_le(0, 2); e.support_le(B)
print('B', B, 'clauses', len(e.cnf.clauses), flush=True)
s = Cadical153(bootstrap_with=e.cnf.clauses)
ok = s.solve()
print('SAT' if ok else 'UNSAT', '%.0fs' % (time.time() - t0), flush=True)
if ok:
    E = e.decode(s.get_model()); print('support', support(E), 'straight_direct', straight_direct(E))
    for r in E: print(' '.join('%2d' % x for x in r))
