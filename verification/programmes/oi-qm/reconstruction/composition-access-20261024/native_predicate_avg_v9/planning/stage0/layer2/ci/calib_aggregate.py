"""NP-AVG-1 Stage 0 Layer 2: aggregate the CI calibrations in the workflow (PROPOSAL). Reads every
calib-*.json in a directory, requires at least 20 (the owner: "at least 20 independent timing
calibrations on the relevant CI runner class") from one commit (every calibration's GITHUB_SHA equal),
and reports, on a v8-free aggregate (each calibration's four tables summed over the calibrated sizes):
the per-CPU-model counts and medians, and the spread (sigma of the log aggregates, max/min).

It does not compute u_cal. u_cal's preregistered statistic (CI-CALIBRATION-PROPOSAL.md section 4) is
on the v8-weighted known terms, which need the v8 dry run's context-size histogram; ci/postrun.py
computes it locally from the retained artifact, after checking the run's identity. It imports nothing
from Layer 2 and reads no v8 configuration. Run with `if: always()`: when calibration jobs failed it
still runs and prints VOID with the number found (CI-7).

Usage: python3 -I -B calib_aggregate.py <dir> --out FILE. Exit 2 (VOID) with fewer than 20
calibrations, a malformed file or calibrations from different commits."""
import json
import math
import os
import statistics
import sys

d = sys.argv[1]
out_path = sys.argv[sys.argv.index('--out') + 1]
TABLES = ('closure_ns_A', 'closure_ns_G', 'ref_c7_ns_A', 'ref_c7_ns_G')
files = sorted(f for f in os.listdir(d) if f.startswith('calib-') and f.endswith('.json')) if os.path.isdir(d) else []
agg, cpus, shas = [], [], set()


def void(reason):
    res = {'label': 'VOID', 'reason': reason, 'calibrations_found': len(files)}
    with open(out_path, 'w') as f:
        f.write(json.dumps(res, indent=1, sort_keys=True) + '\n')
    print(json.dumps(res, sort_keys=True))
    sys.exit(2)


for fn in files:
    try:
        with open(os.path.join(d, fn)) as f:
            c = json.load(f)
        agg.append(sum(int(v) for tb in TABLES for v in c[tb].values()))
        cpus.append(c['runner'].get('cpu_model'))
        shas.add(c['run_identity'].get('GITHUB_SHA'))
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        void('malformed %s' % fn)
if len(agg) < 20:
    void('%d calibrations; at least 20 are required' % len(agg))
if len(shas) != 1:
    void('calibrations from %d commits' % len(shas))
per_cpu = {}
for a, c in zip(agg, cpus):
    per_cpu.setdefault(str(c), []).append(a)
sig = statistics.stdev(math.log(x) for x in agg)
res = {'schema': 'np-avg-1/stage0/layer2/ci-calib-aggregate/2', 'calibrations': len(agg), 'aggregates_ns': agg,
       'head_sha': shas.pop(), 'sigma_log_unweighted': round(sig, 4),
       'max_over_min_unweighted': round(max(agg)/min(agg), 4),
       'per_cpu_model': {k: {'calibrations': len(v), 'median_aggregate_ns': int(statistics.median(v))}
                         for k, v in sorted(per_cpu.items())},
       'note': 'a v8-free summary; u_cal is computed by ci/postrun.py on the v8-weighted known terms '
               '(CI-CALIBRATION-PROPOSAL.md section 4); kappa is fixed by the owner'}
with open(out_path, 'w') as f:
    f.write(json.dumps(res, indent=1, sort_keys=True) + '\n')
print(json.dumps({k: res[k] for k in ('calibrations', 'sigma_log_unweighted', 'max_over_min_unweighted')},
                 sort_keys=True))
