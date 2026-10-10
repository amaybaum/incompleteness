"""Scratch instrumentation of part_cubes(k): same cube list, same encoding, same solver; times encode vs solve and
records CaDiCaL statistics. Diagnosis only."""
import sys, time, itertools, os, json
TOOLS = sys.argv[2]; k = int(sys.argv[1]); sys.path.insert(0, TOOLS)
from pysat.solvers import Cadical153
from sat42 import Enc
from lib42 import elems
fix0 = [(p, s_) for p, s_ in elems if all(p[j] // 16 == 0 for j in range(16))]
def act(e, y):
    p, s_ = e; out = [0] * 16
    for j in range(16): out[p[j] % 16] = s_ * y[j]
    return tuple(out)
cubes = []
for m in (1, 2):
    reps = []; seen = set()
    for supp in itertools.combinations(range(16), m):
        for signs in itertools.product((1, -1), repeat=m):
            y = [0] * 16
            for kk, s in zip(supp, signs): y[kk] = s
            y = tuple(y)
            if y in seen: continue
            orb = set()
            for e in fix0:
                a = act(e, y); orb.add(a); orb.add(tuple(-x for x in a))
            seen |= orb; reps.append(y)
    cubes += [(m, y) for y in reps]
only = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
for idx, (m, y) in enumerate(cubes):
    if idx % 3 != k: continue
    if only is not None and idx not in only: continue
    t0 = time.perf_counter()
    e = Enc(); e.straight(); t1 = time.perf_counter(); e.mode0(); e.lines_ge(m); e.support_le(39)
    for j in range(16):
        e.cnf.append([e.p[0][j] if y[j] == 1 else (e.n[0][j] if y[j] == -1 else e.z[0][j])])
    t2 = time.perf_counter()
    s = Cadical153(bootstrap_with=e.cnf.clauses); t3 = time.perf_counter()
    ok = s.solve(); t4 = time.perf_counter(); st = s.accum_stats(); s.delete()
    print(json.dumps({'cube': idx, 'm': m, 'sat': ok, 'nv': e.pool.top, 'ncl': len(e.cnf.clauses), 'enc_straight': round(t1-t0,2),
                      'enc_rest': round(t2-t1,2), 'load': round(t3-t2,2), 'solve': round(t4-t3,2), 'stats': st}), flush=True)
