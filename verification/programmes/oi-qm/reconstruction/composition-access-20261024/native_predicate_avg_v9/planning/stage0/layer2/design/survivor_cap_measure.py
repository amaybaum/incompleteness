"""Layer-2 design evidence for SURVIVOR-CAP-PROPOSAL.md (advisory; the v8 survivor cap is an owner
placeholder). Toy geometry and planted records only; nothing on v8.

1. Per retained survivor, measured on planted survivor orbits of the toy setup (constraint
   blocks at several centres, some with extra items to enlarge the context): the residue detail's
   size (canonical JSON bytes), the memory the shard keeps after the orbit (tracemalloc, current
   after minus before, the detail kept), the peak transient memory during the orbit's gates, and
   the time of one gated survivor orbit.
2. The per-shard distribution model: X survivor orbits fall on the shards with weights w_s (the
   share of representatives each shard processes). With uniform weights over S = 32 shards, the
   probability that some shard exceeds a cap c is computed exactly:
     P(no shard > c) = X! [z^X] (sum_{k <= c} z^k / k!)^S / S^X.
   A concentrated case (every survivor orbit in one shard) exceeds the cap iff X > c. The v8
   representatives per shard are not computed here (§3 of the proposal).
3. Cost per unit of cap on v8, read from design/kappa/calibration-repeats.json (the estimate's
   survivor-gate term per unit of cap, median of the calibrations), and per replica job.
Timing and memory data, not deterministic. Usage: python3 -I -B survivor_cap_measure.py
<layer2/code> <kappa calibration json> <out.json>"""
import json
import statistics
import sys
import time
import tracemalloc
from fractions import Fraction
from math import factorial

code, kap, outp = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, code)
import s0geom as G        # noqa: E402
import l2config as CFG    # noqa: E402
import l2analysis as AN   # noqa: E402
import l2enum as ENUM     # noqa: E402

setup = CFG.make_setup(G, 'toy')
if setup.key() == (3, 6, (0, 0, -3)):
    raise SystemExit('refusing: v8 configuration class')
grp = AN.group(setup)
prof = dict(CFG.profile('toy'), survivor_cap_per_shard=10**6)
L = G.Pair(setup.n + 1).L
recs = []
for c0 in ((5, 0, 0), (6, 0, 0), (5, 1, 0), (5, 1, 1), (6, 2, 0), (7, 0, 0), (6, 1, 1), (8, 0, 0)):
    for extra in ((), (((0, 0, 1), 5),), (((1, 0, 0), 6), ((0, 1, 0), 4))):
        recs.append(tuple(sorted([(c0, L + 1)] + [(G.vadd(c0, e), L) for e in G.axes(3)] + list(extra))))
rows = []
for r in recs:
    orb = AN.orbit(r, grp)
    bound = {}
    for c in ('A', 'G'):
        q = set()
        for m in orb:
            q |= G.Context(setup, m, c).quants
        bound[(c, 'L3prime')] = bound[(c, 'L3')] = q
    base = {c: set(G.Context(setup, (), c).run()) for c in ('A', 'G')}
    sh = ENUM.Shard(setup, prof, bound, base, None, None)
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()[0]
    tracemalloc.reset_peak()
    t0 = time.perf_counter_ns()
    sh.rep(-1, r, orb)
    dt = time.perf_counter_ns() - t0
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    if not sh.survivors:
        continue
    rows.append({'context_quantities': len(G.Context(setup, r, 'A').quants), 'orbit_size': len(orb),
                 'detail_bytes': len(CFG.canonical(sh.survivors[-1])), 'kept_bytes': cur - before,
                 'peak_transient_bytes': peak - before, 'ns': dt})


def med(k):
    return statistics.median(x[k] for x in rows)


meas = {'survivor_orbits': len(rows), 'max_context_quantities': max(x['context_quantities'] for x in rows),
        'detail_bytes': {'median': med('detail_bytes'), 'max': max(x['detail_bytes'] for x in rows)},
        'kept_bytes': {'median': med('kept_bytes'), 'max': max(x['kept_bytes'] for x in rows)},
        'peak_transient_bytes': {'median': med('peak_transient_bytes'), 'max': max(x['peak_transient_bytes'] for x in rows)},
        'seconds_per_gated_orbit_toy': {'median': round(med('ns')/1e9, 4), 'max': round(max(x['ns'] for x in rows)/1e9, 4)}}

S = CFG.profile('v8')['shards']


def p_exceed_uniform(X, c, S=S):
    """Exact P(some shard receives more than c of X orbits), X orbits placed uniformly and
    independently on S shards."""
    if X <= c:
        return Fraction(0)
    poly = [Fraction(1, factorial(k)) for k in range(c + 1)]
    acc = [Fraction(1)]
    for _ in range(S):
        nxt = [Fraction(0)]*min(len(acc) + c, X + 1)
        for i, a in enumerate(acc):
            if a == 0:
                continue
            for k, b in enumerate(poly):
                if i + k <= X:
                    nxt[i + k] += a*b
        acc = nxt
    ok = acc[X]*factorial(X)/Fraction(S)**X if X < len(acc) else Fraction(0)
    return 1 - ok


caps = (4, 8, 12, 16, 24, 32)
Xs = (1, 8, 16, 32, 64, 128, 256)
table = {c: {X: float('%.3g' % float(p_exceed_uniform(X, c))) for X in Xs} for c in caps}
with open(kap) as f:
    k = json.load(f)
per_cap_unit = statistics.median(x['survivor_gates_seconds_per_cap_unit'] for x in k['v8_estimate_spread']['per_calibration'])
cost = {c: {'survivor_term_runner_seconds': c*per_cap_unit,
            'per_shard_job_seconds_both_copies': round(c*per_cap_unit/S, 1),
            'per_replica_job_seconds': round(c*per_cap_unit/S/2, 1),
            'kept_memory_bytes_at_max': c*meas['kept_bytes']['max']} for c in caps}
out = {'schema': 'np-avg-1/stage0/layer2/survivor-cap/1', 'deterministic': False, 'python': sys.version.split()[0],
       'measured_planted': meas, 'rows': rows,
       'model': {'shards': S, 'weights': 'uniform (1/S); a concentrated case exceeds iff X > c',
                 'P_some_shard_exceeds_cap_uniform': {str(c): {str(X): v for X, v in d.items()} for c, d in table.items()},
                 'v8_survivor_term_per_cap_unit_runner_seconds_median': per_cap_unit, 'cost_by_cap': cost},
       'note': 'planted toy-geometry records; the time per orbit at v8 sizes is the estimate\'s, from the planted '
               'calibration at m_max; nothing on v8'}
with open(outp, 'w') as f:
    json.dump(out, f, indent=1, sort_keys=True)
    f.write('\n')
print(json.dumps({k2: v for k2, v in out.items() if k2 != 'rows'}, indent=1, sort_keys=True))
