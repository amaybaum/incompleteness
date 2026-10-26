"""Layer-2 design evidence: local checks of the proposed CI calibration (stage0/layer2/ci/), run
here, never in CI. (1) --check-equivalence: the closure executed from the hash-checked engine
source equals s0geom.closure on every planted set (3 sets per size). (2) --tripwire-selftest: a
planted v8-keyed object makes the script exit 2 with VOID and write no file. (3) An ordinary run
(1 set per size) passes the tripwire. (4) The aggregator refuses 19 calibrations and accepts 20
(the ordinary run's file and 19 copies with a deterministic +-k% scaling). (5) The workflow
file: one push trigger on the dedicated branch only, permissions contents: read, concurrency set,
20 calibrations with max-parallel 4 and timeouts on every job, and no workflow_dispatch,
pull_request or schedule trigger. Usage: python3 -I -B ci_local_check.py <layer2/ci> <scratch>.
Prints JSON; exit 0 iff every check holds."""
import json
import os
import shutil
import subprocess
import sys

ci, scratch = sys.argv[1], sys.argv[2]
py = sys.executable
res = {}


def run(*a):
    p = subprocess.run([py, '-I', '-B'] + list(a), capture_output=True, text=True)
    try:
        return p.returncode, json.loads(p.stdout)
    except ValueError:
        return p.returncode, None


d = os.path.join(scratch, 'ci-local')
shutil.rmtree(d, ignore_errors=True)
os.makedirs(d)
code, _ = run(os.path.join(ci, 'calib_ci.py'), '--out', os.path.join(d, 'eq.json'), '--sets', '3', '--check-equivalence')
with open(os.path.join(d, 'eq.json')) as f:
    res['equivalence_mismatches'] = json.load(f)['equivalence_with_engine']['mismatches']
res['equivalence_exit'] = code
code, o = run(os.path.join(ci, 'calib_ci.py'), '--out', os.path.join(d, 'trip.json'), '--sets', '1',
              '--tripwire-selftest')
res['tripwire'] = {'exit': code, 'label': (o or {}).get('label'), 'file_written': os.path.exists(os.path.join(d, 'trip.json'))}
code, o = run(os.path.join(ci, 'calib_ci.py'), '--out', os.path.join(d, 'calib-1.json'), '--sets', '1', '--index', '1')
res['ordinary_exit'] = code
with open(os.path.join(d, 'calib-1.json')) as f:
    base = json.load(f)
for i in range(2, 20):
    c = dict(base)
    for tb in ('closure_ns_A', 'closure_ns_G', 'ref_c7_ns_A', 'ref_c7_ns_G'):
        c[tb] = {m: v*(100 + (i % 7) - 3)//100 for m, v in base[tb].items()}
    with open(os.path.join(d, 'calib-%d.json' % i), 'w') as f:
        json.dump(c, f)
code19, _ = run(os.path.join(ci, 'calib_aggregate.py'), d, '--out', os.path.join(d, 'agg.json'))
shutil.copy(os.path.join(d, 'calib-2.json'), os.path.join(d, 'calib-20.json'))
code20, o = run(os.path.join(ci, 'calib_aggregate.py'), d, '--out', os.path.join(d, 'agg.json'))
res['aggregate'] = {'exit_with_19': code19, 'exit_with_20': code20, 'calibrations': (o or {}).get('calibrations')}
with open(os.path.join(ci, 'np-avg-1-stage0-planted-calibration.yml')) as f:
    y = f.read()
on = y[y.index('\non:'):y.index('\npermissions:')]
res['workflow'] = {'push_branch_only': "branches:\n      - 'ci-calibration/np-avg-1-stage0'" in on and 'push:' in on,
                   'no_other_trigger': all(t not in on for t in ('workflow_dispatch', 'pull_request', 'schedule',
                                                                  'workflow_run')),
                   'read_only': 'permissions:\n  contents: read' in y, 'concurrency': 'concurrency:' in y,
                   'twenty_calibrations': 'index: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]' in y,
                   'max_parallel_4': 'max-parallel: 4' in y,
                   'every_job_has_timeout': y.count('timeout-minutes:') == y.count('runs-on:') == 3}
ok = res['equivalence_mismatches'] == 0 and res['equivalence_exit'] == 0 and res['tripwire']['exit'] == 2 and \
    res['tripwire']['label'] == 'VOID' and not res['tripwire']['file_written'] and res['ordinary_exit'] == 0 and \
    code19 == 2 and code20 == 0 and res['aggregate']['calibrations'] == 20 and all(res['workflow'].values())
res['pass'] = ok
shutil.rmtree(d, ignore_errors=True)
print(json.dumps(res, indent=1, sort_keys=True))
sys.exit(0 if ok else 2)
