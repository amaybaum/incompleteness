"""Layer-2 design evidence (r5; LAYER2-R4-REVIEW section 5 item 3, A3, A4): a bounded test of the cost
model on the mid-size analogue profile 'mid' (dim 3, n 6, ball(2), slices -1..23, port (0, 0, -2):
v8's dim, n, slices, sources and gate rates, a smaller region and another port, so its (dim, n, port)
is not v8's and it is not v8's configuration class).

1. The dry run on 'mid' at 128 shards (the deterministic subdivision; 128 rather than 32 so that each
   real shard takes about half a minute here), with the C7 populations counted closure-free (A4: the
   population count is timed) and the cost model's per-shard prediction (l2plan.estimate, the planted
   calibration of design/toyrun/calib.json, the one the v8 estimate uses).
2. Four real shards through l2enum.Shard, normal mode only (the -O copy is the model's factor 2):
   shard 0 (the single-item records), the model's heaviest, its lightest and its median shard. Each
   is timed and compared with the model's single-copy prediction of its shared terms (closures,
   sampled gates, C7); the survivor allowance is a per-shard maximum, not an expectation, and is not
   in the comparison. Survivor orbits per shard and per site pair are recorded (for the cap).
3. The overhead factor at v8-like context sizes: Shard.rep on 24 representatives of the heaviest shard
   with the sampled gates off and C7's closures stubbed (as design/overhead_measure.py), against their
   four bare closures.
4. A3: on every 97th record of 'mid', l2plan's Q0 equals the production context's quantities and
   I_A, I_G equal the production shared-near-tip test; the frame check of l2preflight (l2plan's frame
   equals the production frame on the C12 box) holds on 'mid'.
Timing data, not deterministic. Usage: python3 -I -B midsize_validation.py <layer2/code> <calib.json>
<out.json>."""
import json
import statistics
import sys
import time
from fractions import Fraction

code, calibp, outp = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, code)
import s0geom as G        # noqa: E402
import l2config as CFG    # noqa: E402
import l2analysis as AN   # noqa: E402
import l2enum as ENUM     # noqa: E402
import l2plan as PLAN     # noqa: E402
import l2s1a as S1A       # noqa: E402
import l2preflight as PF  # noqa: E402

PNAME, S = 'mid', 128
prof = dict(CFG.profile(PNAME), shards=S)
setup = CFG.make_setup(G, PNAME)
if setup.key() == (3, 6, (0, 0, -3)) or PLAN.Space(prof).key == PLAN.V8_KEY_LITERAL:
    raise SystemExit('refusing: v8 configuration class')
out = {'profile': PNAME, 'setup': CFG.profile(PNAME)['setup'], 'shards': S}
T0 = time.time()

# 1. dry run, populations (A4), prediction
sp = PLAN.Space(prof)
N = sp.n_records()
_, so, po = sp.orbits_burnside()
plan, reps, _, info = PLAN.dry_shard_plan(sp, S)
ri = PLAN.RepIndex(PLAN.site_pair_counts(sp))
t = time.time()
pops = PLAN.c7_populations(sp)
out['A4_population_count'] = {'seconds': round(time.time() - t, 1), 'records': N, 'populations': pops,
                              'seconds_per_million_records': round((time.time() - t)/N*1e6, 1)}
with open(calibp) as f:
    calib = json.load(f)
hist = PLAN.context_histogram(sp)
est = PLAN.estimate(sp, hist, so + po, N, calib, prof, pops, reps, ri, plan)
terms = est['terms_runner_seconds']
shared_both = terms['closures'] + terms['sampled_gates'] + terms['C7_scope']
tA = {int(k): v for k, v in calib['closure_ns_A'].items()}
tG = {int(k): v for k, v in calib['closure_ns_G'].items()}
weights = PLAN.shard_context_weights(sp, ri, plan, lambda m: PLAN._t(tA, m) + PLAN._t(tG, m))
W = sum(weights)
pred1 = [float(Fraction(shared_both, 2)*w/W) for w in weights]       # single copy (normal mode)
out['dry_run'] = {'records': N, 'representatives': so + po, 'plan_kind': info['kind'], 'accounting': info['accounting'],
                  'model_terms_both_copies_seconds': {k: terms[k] for k in ('closures', 'sampled_gates', 'C7_scope')},
                  'model_heaviest_over_mean_cost': round(max(weights)*S/W, 3),
                  'C7_populations_fraction_of_N': {k: round(v['records']/N, 4) for k, v in pops.items()}}

# 2. four real shards
s1a = S1A.run(PNAME, None, None)
bound = ENUM.load_bound(s1a, setup, None)
base = {c: set(G.Context(setup, (), c).run()) for c in ('A', 'G')}
order = sorted(range(S), key=lambda k: weights[k])
pick = [0, order[-1], order[0] if order[0] != 0 else order[1], order[S//2]]
pick = list(dict.fromkeys(pick))
pair_sites = [(i, j) for i in range(len(sp.region)) for j in range(i + 1, len(sp.region))]
ns, nt = len(sp.region), len(sp.slices)


def site_pair_of(idx):
    if idx < ns*nt:
        return 'single:%d' % (idx//nt)
    return 'pair:%d-%d' % pair_sites[(idx - ns*nt)//(nt*nt)]


runs = []
for k in pick:
    sh = ENUM.Shard(setup, prof, bound, base, None, None)
    t = time.time()
    scanned, rr = ENUM.scan(setup, plan[k]['lo'], plan[k]['hi'], sh.grp, None)
    for i, r, o in rr:
        sh.rep(i, r, o)
    dt = time.time() - t
    o = sh.output()
    surv = [d['index'] for d in o['survivors']]
    by_pair = {}
    for i in surv:
        by_pair[site_pair_of(i)] = by_pair.get(site_pair_of(i), 0) + 1
    runs.append({'shard': k, 'representatives': len(rr), 'planned_representatives': plan[k]['representatives'],
                 'scanned': scanned, 'seconds_actual_normal_mode': round(dt, 1),
                 'seconds_predicted_single_copy': round(pred1[k], 1),
                 'actual_over_predicted': round(dt/pred1[k], 2) if pred1[k] else None,
                 'survivor_orbits': o['survivor_representatives'], 'survivor_orbits_by_site_pair': by_pair})
out['real_shards'] = runs
acts = [r['seconds_actual_normal_mode'] for r in runs]
out['real_shards_summary'] = {
    'actual_over_predicted': [r['actual_over_predicted'] for r in runs],
    'heaviest_actual_over_mean_actual_of_these': round(max(acts)/statistics.mean(acts), 2),
    'note': 'predicted: the cost model on the planted calibration, shared terms only, normal copy; actual: this '
            'machine, normal mode, every gate at the mid profile\'s (v8\'s) rates'}

# 3. overhead at v8-like sizes
off = 10**12
q_prof = dict(prof, sampling={'C8_orbits': off, 'C11i': off, 'C17': off, 'C18': off}, survivor_cap_per_shard=10**6)
orig_c7 = ENUM.Shard.c7_record
ENUM.Shard.c7_record = lambda self, idx, m, conv, carried, dcache: True
L3 = G.Rule(far=False)
hk = order[-1]
_, rr = ENUM.scan(setup, plan[hk]['lo'], plan[hk]['hi'], AN.group(setup), None)
step = max(1, len(rr)//24)
ratios, sizes = [], []
for i, r, o in rr[::step][:24]:
    sh = ENUM.Shard(setup, q_prof, bound, base, None, None)
    t = time.time()
    sh.rep(i, r, o)
    t_rep = time.time() - t
    t = time.time()
    for conv in ('A', 'G'):
        for rule in (G.FROZEN, L3):
            G.Context(setup, r, conv, rule).run()
    t_bare = time.time() - t
    ratios.append(t_rep/t_bare)
    sizes.append(len(G.Context(setup, r, 'A').quants))
ENUM.Shard.c7_record = orig_c7
out['overhead_at_mid_sizes'] = {'representatives': len(ratios), 'context_quantities': [min(sizes), max(sizes)],
                                'ratio_median': round(statistics.median(ratios), 2),
                                'ratio_p90': round(sorted(ratios)[int(0.9*(len(ratios) - 1))], 2),
                                'configured_factor': CFG.CONFIG['budget']['gate_overhead_factor']}

# 4. A3: l2plan's closure-free predicates against the production contexts on a sample; the frame
bad, n = [], 0
for i in range(0, N, 97):
    r = tuple(sorted(G.record_at(setup, i)))
    f = sp.c7_flags(r)
    prod = {}
    for conv in ('A', 'G'):
        ctx = G.Context(setup, r, conv)
        prod['I_' + conv] = AN.shared_near_tip(ctx.quants, ctx.pair, setup.dim)
    if any(f[k] != v for k, v in prod.items()) or sp.q0(r) != G.Context(setup, r, 'A').quants:
        bad.append(i)
    n += 1
fr = PF.c12_universe(setup, None, prof)
out['A3_crosscheck'] = {'records_checked': n, 'disagreeing_indices': bad[:5], 'disagreements': len(bad),
                        'frame_equals_production_frame': fr['l2plan_frame_equals_production_frame'],
                        'scope': 'Q0 and I_A, I_G against the production context; the frame against the production '
                                 'frame on the C12 box (F_G and E_G use that frame and the same tip code; their '
                                 'reference check is L2-SCOPE on the toy class)'}
out['seconds_total'] = round(time.time() - T0, 1)
with open(outp, 'w') as f:
    json.dump(out, f, sort_keys=True, indent=1)
    f.write('\n')
print(json.dumps({'real_shards': out['real_shards_summary'], 'A4_seconds': out['A4_population_count']['seconds'],
                  'overhead': out['overhead_at_mid_sizes'], 'A3_disagreements': len(bad),
                  'frame_ok': fr['l2plan_frame_equals_production_frame'], 'seconds_total': out['seconds_total']},
                 sort_keys=True))
