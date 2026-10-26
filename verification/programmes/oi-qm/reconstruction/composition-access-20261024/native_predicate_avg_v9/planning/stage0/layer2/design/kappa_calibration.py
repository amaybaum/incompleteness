"""Layer-2 design evidence for the kappa proposal (KAPPA-PROPOSAL.md; advisory, sets nothing):
the spread of the timing calibration and of the cost estimate built from it. Timing data, not
deterministic. Toy and planted instances only; v8 enters only through l2plan's combinatorial
estimate (counts and context-size histogram, no context, no closure), exactly as the dry run's
v8 estimate step does.

1. Calibration repeats: l2calib.py (planted quantity sets, sizes 8-40) is run R times normally and
   R times under -O, each in a fresh process. Per table and size: median, coefficient of variation
   (CV), max/median and min/median across the normal runs; the paired -O/normal ratio.
2. Estimate spread: l2plan.estimate on the v8 profile (pops = None: the C7 inputs are not
   computed; the survivor cap is an owner placeholder, so the survivor-gate term is reported per
   unit of cap) for each of the 2R calibrations: the known terms, the C7 set-4 term, the per-record
   C7 coefficients; their CV and max/median; and the statistic LAYER2-R3-REVIEW section 6 asks for,
   the ratio between two independent calibrations: every ordered pair i != j, its empirical 99th
   percentile and maximum (max/min), and the normal-approximation 99th percentile
   exp(2.326 x sqrt(2) x sigma_log).
3. Toy records: on every record of the toy class, the production L3prime closure and the full
   s0ref reference closure under A and G are timed, three passes in one process. Pass 1 against
   passes 2-3 measures the in-process cache effect (eligibility memo, explicit cones); the measured
   totals against the totals the median calibration predicts at each record's context size give
   the planted-to-record model ratio on the toy class (toy contexts have at most 10 quantities,
   below most calibrated sizes, so this ratio is a weak proxy for v8).
Usage: python3 -I -B kappa_calibration.py <layer2/code> <out.json> [--repeats R]
Writes out.json; prints a summary JSON; exit 0 when every step ran."""
import json
import os
import statistics
import subprocess
import sys
import tempfile
import time

code, outp = sys.argv[1], sys.argv[2]
R = int(sys.argv[sys.argv.index('--repeats') + 1]) if '--repeats' in sys.argv else 5
sys.path.insert(0, code)
import l2config as CFG   # noqa: E402
import l2plan as PLAN    # noqa: E402


def r4(x):
    return round(x, 4)


def spread(xs):
    med = statistics.median(xs)
    mean = statistics.fmean(xs)
    return {'n': len(xs), 'median': med, 'cv': r4(statistics.pstdev(xs)/mean) if mean else None,
            'max_over_median': r4(max(xs)/med) if med else None, 'min_over_median': r4(min(xs)/med) if med else None}


tmp = tempfile.mkdtemp(prefix='kappa-')
cal = {'normal': [], 'O': []}
t0 = time.time()
for i in range(R):
    for mode in ('normal', 'O'):
        p = os.path.join(tmp, 'calib-%s-%d.json' % (mode, i))
        cmd = [sys.executable, '-I', '-B'] + (['-O'] if mode == 'O' else []) + [os.path.join(code, 'l2calib.py'),
                                                                                  '--out', p]
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        with open(p) as f:
            cal[mode].append(json.load(f))
tables = ('closure_ns_A', 'closure_ns_G', 'ref_c7_ns_A', 'ref_c7_ns_G')
per_size = {}
for tb in tables:
    per_size[tb] = {}
    for m in sorted(cal['normal'][0][tb], key=int):
        xs = [c[tb][m] for c in cal['normal']]
        o = [c[tb][m] for c in cal['O']]
        per_size[tb][m] = dict(spread(xs), O_over_normal_paired=[r4(b/a) for a, b in zip(xs, o)])
cv_all = {tb: [v['cv'] for v in per_size[tb].values()] for tb in tables}
mm_all = {tb: [v['max_over_median'] for v in per_size[tb].values()] for tb in tables}
O_all = [x for tb in tables for v in per_size[tb].values() for x in v['O_over_normal_paired']]
# 2. estimate spread on v8 (combinatorics only; no context, no closure)
prof = CFG.profile('v8')
sp = PLAN.Space(prof)
N = sp.n_records()
_, so, po = sp.orbits_burnside()
hist = PLAN.context_histogram(sp)
est = []
for mode in ('normal', 'O'):
    for c in cal[mode]:
        e = PLAN.estimate(sp, hist, so + po, N, c, prof, None)
        est.append({'mode': mode, 'known_terms': e['known_terms_runner_seconds'],
                    'known_plus_C7_set4': e['known_terms_plus_C7_set4_runner_seconds'],
                    'terms': {k: v for k, v in e['terms_runner_seconds'].items() if isinstance(v, int)},
                    'c7_per_record_central': e['C7']['per_record_seconds'],
                    'c7_FG_coefficient': e['C7']['coefficients_seconds_per_record_central']['F_G'],
                    'survivor_gates_seconds_per_cap_unit': e['survivor_gates_seconds_per_cap_unit'],
                    's1a': e['per_job_seconds']['s1a']})
known = [x['known_plus_C7_set4'] for x in est]
import math    # noqa: E402
pairs = sorted(a/b for i, a in enumerate(known) for j, b in enumerate(known) if i != j)
sig = statistics.stdev([math.log(x) for x in known])
ratio_stat = {'ordered_pairs': len(pairs), 'empirical_p99': r4(pairs[min(len(pairs) - 1, math.ceil(0.99*len(pairs)) - 1)]),
              'max_over_min': r4(max(known)/min(known)), 'sigma_log': r4(sig),
              'normal_p99_of_ratio': r4(math.exp(2.326*math.sqrt(2)*sig))}
fg = [x['c7_FG_coefficient'] for x in est]
closures = [x['terms']['closures'] for x in est]
# 3. toy records: production closure and full reference, A and G, three passes in one process
import s0geom as G       # noqa: E402
import s0ref as REF      # noqa: E402
setup = CFG.make_setup(G, 'toy')
if setup.key() == (3, 6, (0, 0, -3)):
    raise SystemExit('refusing: v8 configuration class')
recs = [tuple(sorted(G.record_at(setup, i))) for i in range(G.num_records(setup))]
med_cal = {tb: {int(m): statistics.median(c[tb][m] for c in cal['normal']) for m in cal['normal'][0][tb]}
           for tb in tables}
passes = []
pred = {'A': 0, 'G': 0, 'refA': 0, 'refG': 0}
for k in range(3):
    tot = {'A': 0, 'G': 0, 'refA': 0, 'refG': 0}
    for r in recs:
        for conv in ('A', 'G'):
            ctx = G.Context(setup, r, conv)
            a = time.perf_counter_ns()
            ctx.run()
            b = time.perf_counter_ns()
            fixed, quants, geo, elig = REF.ref_context(setup.dim, setup.n, tuple(setup.port), r, conv)
            c = time.perf_counter_ns()
            REF.greatest(fixed, quants, geo, elig, 8)
            d = time.perf_counter_ns()
            tot[conv] += b - a
            tot['ref' + conv] += d - c
            if k == 0:
                m = len(ctx.quants)
                pred[conv] += PLAN._t(med_cal['closure_ns_' + conv], m)
                pred['ref' + conv] += PLAN._t(med_cal['ref_c7_ns_' + conv], m)
    passes.append(tot)
toy = {'records': len(recs), 'passes_ns': passes,
       'cache_effect_pass1_over_mean_pass2_3': {k: r4(passes[0][k]/statistics.fmean([passes[1][k], passes[2][k]]))
                                               for k in passes[0]},
       'pass2_3_spread': {k: r4(abs(passes[1][k] - passes[2][k])/statistics.fmean([passes[1][k], passes[2][k]]))
                          for k in passes[0]},
       'measured_over_calibration_prediction': {k: r4(statistics.fmean([p[k] for p in passes[1:]])/pred[k])
                                                for k in pred},
       'max_context_quantities': max(len(G.Context(setup, r, 'A').quants) for r in recs)}
out = {'schema': 'np-avg-1/stage0/layer2/kappa-calibration/1', 'deterministic': False, 'repeats': R,
       'python': sys.version.split()[0], 'seconds': round(time.time() - t0),
       'calibration_per_size': per_size,
       'calibration_summary': {'cv_by_table': {tb: {'median': statistics.median(v), 'max': max(v)}
                                               for tb, v in cv_all.items()},
                               'max_over_median_by_table': {tb: max(v) for tb, v in mm_all.items()},
                               'O_over_normal': spread(O_all)},
       'v8_estimate_spread': {'per_calibration': est, 'known_plus_C7_set4': spread(known),
                              'ratio_of_independent_calibrations': ratio_stat,
                              'survivor_gates_seconds_per_cap_unit': spread([x['survivor_gates_seconds_per_cap_unit']
                                                                             for x in est]),
                              'closures_term': spread(closures), 'C7_F_G_coefficient_seconds_per_record': spread(fg)},
       'toy_records': toy}
with open(outp, 'w') as f:
    json.dump(out, f, indent=1, sort_keys=True)
    f.write('\n')
print(json.dumps({'written': os.path.basename(outp), 'repeats': R,
                  'calibration_summary': out['calibration_summary'],
                  'v8_known_plus_C7_set4': out['v8_estimate_spread']['known_plus_C7_set4'],
                  'ratio_of_independent_calibrations': ratio_stat,
                  'C7_F_G_coefficient': out['v8_estimate_spread']['C7_F_G_coefficient_seconds_per_record'],
                  'toy': {k: toy[k] for k in ('cache_effect_pass1_over_mean_pass2_3', 'pass2_3_spread',
                                              'measured_over_calibration_prediction')}}, indent=1, sort_keys=True))
