"""controls for the SAT encoding: known straight matrices satisfy it; a known non-straight matrix violates it;
free solve with support <= 16 returns a straight matrix (checked exactly)."""
import time
from pysat.solvers import Cadical153
from sat42 import Enc
from lib42 import A38, B38, C38, WIT38, straight_direct, support
t0 = time.time()
e = Enc(); e.straight(); base = e.cnf
print('clauses', len(base.clauses), 'vars', e.pool.top, '%.0fs' % (time.time() - t0), flush=True)
def solve_with(extra_fix=None, extra=None):
    s = Cadical153(bootstrap_with=base.clauses)
    assum = []
    if extra_fix is not None:
        for i in range(16):
            for j in range(16):
                v = extra_fix[i][j]; assum.append(e.p[i][j] if v == 1 else (e.n[i][j] if v == -1 else e.z[i][j]))
    ok = s.solve(assumptions=assum); m = s.get_model() if ok else None; s.delete(); return ok, m
for nm, E in (('A', A38), ('B', B38), ('C', C38), ('A+B+C', WIT38), ('-A', [[-x for x in r] for r in A38])):
    print(nm, 'accepted', solve_with(E)[0])
bad = [r[:] for r in A38]; assert bad[7][4] == 1; bad[7][4] = 0
print('A with one entry removed: straight_direct', straight_direct(bad), 'accepted', solve_with(bad)[0])
