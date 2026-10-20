"""A6: instrumented replay of the generator's first vertex step on omegah (start 0), bounded by a budget."""
import json, os, sys, time
import numpy as np
PRE, WORK, budget = sys.argv[1], sys.argv[2], float(sys.argv[3])
sys.path.insert(0, PRE)
import controls_gen as cg
pool = json.load(open(os.path.join(WORK, 'pool-omegah.json')))
t0 = time.monotonic()
prob = cg.Problem(pool)
print('Problem built in %.1f s; dim F %d; quadruples %d' % (time.monotonic() - t0, prob.nv, prob.ns**2 * prob.ne**2), flush=True)
rng = np.random.RandomState(1000)
t1 = time.monotonic()
cuts = cg.Cuts(prob, rng)
print('initial cuts %d built in %.1f s' % (len(cuts.quads), time.monotonic() - t1), flush=True)
cobj = rng.randn(prob.nv)
deadline = time.monotonic() + budget
k = 0
while time.monotonic() < deadline:
    t2 = time.monotonic()
    res = cg.solve_lp(cobj, -cuts.R, cuts.C, None, None, [(-cg.BOX, cg.BOX)] * prob.nv, deadline)
    tl = time.monotonic() - t2
    if res is None:
        print('LP %d: no solution within budget (%.1f s)' % (k, tl), flush=True); break
    vals = prob.values(prob.G(res.x))
    nviol = int((vals < -cg.SEP_TOL).sum())
    atbox = int((np.abs(np.abs(res.x) - cg.BOX) < 1e-9).sum())
    t3 = time.monotonic()
    more = cuts.separate(res.x)
    print('LP %d: %.1f s, rows %d, min value %.3e, violated %d, coords at box %d, separation %.1f s'
          % (k, tl, len(cuts.C), vals.min(), nviol, atbox, time.monotonic() - t3), flush=True)
    k += 1
    if not more:
        print('vertex reached'); break
