"""Direct SAT formulation, min-rep domain {-1,0,1}: straight, 0 a mode of every line, support <= B, and outside all 18
relaxed census subspaces (N18): for each structure, some equation of its relaxed system is nonzero. 'eq != 0' is
encoded by forbidding, under a selector, every zero-sum assignment of the entries the equation involves. No symmetry
reduction (N18 is not stabilizer-invariant). Independent of the DFS and of every pruning lemma except the pair tables
(VS) inside the straightness encoding."""
import sys, time, itertools
from pysat.solvers import Cadical153
from sat42 import Enc
from lib42 import SMAT, STRUCTS, straight_direct, support
from classify42 import member_masks
import numpy as np
B = int(sys.argv[1]); t0 = time.time()
e = Enc(); e.straight(); e.mode0(); e.support_le(B)
lit = lambda i, j, v: e.p[i][j] if v == 1 else (e.n[i][j] if v == -1 else e.z[i][j])
nsel = 0
for nm, tr, s in STRUCTS:
    M = SMAT[(nm, tr, True)]; sels = []
    for row in M:
        vars_ = [(int(k), int(row[k])) for k in np.flatnonzero(row)]
        a = e.pool.id(('neq', nm, tr, nsel)); nsel += 1; sels.append(a)
        for vals in itertools.product((-1, 0, 1), repeat=len(vars_)):
            if sum(c * v for (k, c), v in zip(vars_, vals)) == 0:
                e.cnf.append([-a] + [-lit(k // 16, k % 16, v) for (k, c), v in zip(vars_, vals)])
    e.cnf.append(sels)
print('B', B, 'clauses', len(e.cnf.clauses), '%.0fs' % (time.time() - t0), flush=True)
s = Cadical153(bootstrap_with=e.cnf.clauses); ok = s.solve()
print('SAT' if ok else 'UNSAT', '%.0fs' % (time.time() - t0), flush=True)
if ok:
    E = e.decode(s.get_model()); X = np.array(E).reshape(1, 256); ms, mr = member_masks(X)
    print('support', support(E), 'straight_direct', straight_direct(E), 'N18 relaxed mask', int(mr[0]))
    for r in E: print(' '.join('%2d' % x for x in r))
