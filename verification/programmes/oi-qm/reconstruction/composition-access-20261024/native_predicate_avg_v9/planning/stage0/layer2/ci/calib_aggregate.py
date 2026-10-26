"""NP-AVG-1 Stage 0 Layer 2: aggregate the CI calibrations (PROPOSAL). Reads every calib-*.json in a
directory, requires at least 20 (the owner: "at least 20 independent timing calibrations on the
relevant CI runner class"), and computes u_cal's statistic on a v8-free aggregate: for each
calibration, the sum of its four tables over the calibrated sizes; over every ordered pair of
distinct calibrations, the ratio of aggregates; its empirical 99th percentile, its maximum
(max/min), sigma of the log aggregates and the normal approximation exp(2.326 x sqrt(2) x sigma).
It imports nothing from Layer 2 and reads no v8 configuration. The v8-weighted statistic (each
calibration's v8 estimate, as design/kappa_calibration.py computes it) is computed afterwards,
locally, from the retained artifact. Usage: python3 -I -B calib_aggregate.py <dir> --out FILE.
Fails closed (exit 2) with fewer than 20 calibrations or any malformed file."""
import json
import math
import os
import statistics
import sys

d = sys.argv[1]
out_path = sys.argv[sys.argv.index('--out') + 1]
TABLES = ('closure_ns_A', 'closure_ns_G', 'ref_c7_ns_A', 'ref_c7_ns_G')
files = sorted(f for f in os.listdir(d) if f.startswith('calib-') and f.endswith('.json'))
agg, runners = [], []
for fn in files:
    try:
        with open(os.path.join(d, fn)) as f:
            c = json.load(f)
        agg.append(sum(int(v) for tb in TABLES for v in c[tb].values()))
        runners.append(c.get('runner'))
    except (OSError, ValueError, KeyError):
        print(json.dumps({'label': 'VOID', 'reason': 'malformed %s' % fn}))
        sys.exit(2)
if len(agg) < 20:
    print(json.dumps({'label': 'VOID', 'reason': '%d calibrations; at least 20 are required' % len(agg)}))
    sys.exit(2)
pairs = sorted(a/b for i, a in enumerate(agg) for j, b in enumerate(agg) if i != j)
sig = statistics.stdev(math.log(x) for x in agg)
res = {'schema': 'np-avg-1/stage0/layer2/ci-calib-aggregate/1', 'calibrations': len(agg), 'aggregates_ns': agg,
       'ordered_pairs': len(pairs), 'empirical_p99': round(pairs[math.ceil(0.99*len(pairs)) - 1], 4),
       'max_over_min': round(max(agg)/min(agg), 4), 'sigma_log': round(sig, 4),
       'normal_p99_of_ratio': round(math.exp(2.326*math.sqrt(2)*sig), 4), 'runners': runners,
       'note': 'u_cal candidate statistic on a v8-free aggregate; kappa is fixed by the owner'}
with open(out_path, 'w') as f:
    f.write(json.dumps(res, indent=1, sort_keys=True) + '\n')
print(json.dumps({k: res[k] for k in ('calibrations', 'empirical_p99', 'max_over_min', 'normal_p99_of_ratio')},
                 sort_keys=True))
