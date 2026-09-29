"""No-zero-line case (m >= 1) in the min-rep domain {-1,0,1}, split into cubes: row 0 is a line of minimum support m
(WLOG: rows are one orbit under the row-preserving stabilizer, and transposition exchanges rows and columns), fixed to
an orbit representative y0 under the row-0 stabilizer and global sign; every row and column has support >= m;
0 is a mode of every line; total support <= B. m = 1, 2 (m >= 3 forces support >= 48). Each cube is a SAT call."""
import sys, time, itertools
from pysat.solvers import Cadical153
from sat42 import Enc
from lib42 import elems, straight_direct, support
B = int(sys.argv[1]); t0 = time.time()
fix0 = [(p, s_) for p, s_ in elems if all(p[j] // 16 == 0 for j in range(16))]
def act(e, y):
    p, s_ = e; out = [0] * 16
    for j in range(16): out[p[j] % 16] = s_ * y[j]
    return tuple(out)
for m in (1, 2):
    reps = []; seen = set()
    for supp in itertools.combinations(range(16), m):
        for signs in itertools.product((1, -1), repeat=m):
            y = [0] * 16
            for k, s in zip(supp, signs): y[k] = s
            y = tuple(y)
            if y in seen: continue
            orb = set()
            for e in fix0:
                a = act(e, y); orb.add(a); orb.add(tuple(-x for x in a))
            seen |= orb; reps.append(y)
    print('m', m, 'row-0 stabilizer', len(fix0), 'cubes', len(reps), flush=True)
    for y in reps:
        e = Enc(); e.straight(); e.mode0(); e.lines_ge(m); e.support_le(B)
        for j in range(16): e.cnf.append([e.p[0][j] if y[j] == 1 else (e.n[0][j] if y[j] == -1 else e.z[0][j])])
        s = Cadical153(bootstrap_with=e.cnf.clauses); ok = s.solve()
        msg = 'SAT' if ok else 'UNSAT'
        if ok:
            E = e.decode(s.get_model()); msg += ' support %d straight_direct %s' % (support(E), straight_direct(E))
            print(E, flush=True)
        print('  m', m, 'y0', y, msg, '%.0fs' % (time.time() - t0), flush=True)
        s.delete()
print('DONE', flush=True)
