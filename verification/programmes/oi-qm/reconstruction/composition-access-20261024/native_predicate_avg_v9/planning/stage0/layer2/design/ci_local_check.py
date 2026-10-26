"""Layer-2 design evidence: local checks of the proposed CI calibration (stage0/layer2/ci/), run
here, never in CI. (1) --check-equivalence: the closure executed from the hash-checked engine
source equals s0geom.closure on every planted set (3 sets per size). (2) --tripwire-selftest: a
planted v8-keyed object makes the script exit 2 with VOID and write no file. (3) An ordinary run
(1 set per size) passes the tripwire. (4) The aggregator refuses 19 calibrations and accepts 20
(the ordinary run's file and 19 copies with a deterministic +-k% scaling), and refuses 20 from two
commits. (5) The workflow file: one push trigger on the dedicated branch only, permissions contents:
read, concurrency set, 20 calibrations with max-parallel 4 and timeouts on every job, no
workflow_dispatch, pull_request or schedule trigger, no self-pin, the three file pins equal to
the files' SHA-256, every action pinned to a 40-hex
commit SHA, the aggregate job under always() and the guard's success. (6) r5: each calibration records
its CPU model, wall-clock start and end and run identity; FORBIDDEN names V8_KEY, V8_REF and NO_V8.
(7) r5: ci/postrun.py on a synthetic launch (20 calibrations, a run record and job records written
here) holds with a u_cal, and is VOID when the authorized SHA differs or a calibration names another
run. Usage: python3 -I -B ci_local_check.py <layer2/ci> <scratch>. Prints JSON; exit 0 iff every check
holds."""
import hashlib
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
SHA, RUN = 'a'*40, 123
for i in range(1, 20):
    p = os.path.join(d, 'calib-%d.json' % i)
    with open(p) as f:
        c = json.load(f)
    c['index'] = str(i)
    c['run_identity'] = {'GITHUB_SHA': SHA, 'GITHUB_RUN_ID': str(RUN), 'GITHUB_RUN_ATTEMPT': '1',
                         'GITHUB_JOB': 'calibrate', 'GITHUB_REF': 'refs/heads/ci-calibration/np-avg-1-stage0'}
    c['wall_clock_utc'] = {'script_start': '2026-10-26T10:00:00Z', 'script_end': '2026-10-26T10:00:%02dZ' % (10 + i)}
    with open(p, 'w') as f:
        json.dump(c, f)
res['calibration_records'] = {k: k in base for k in ('wall_clock_utc', 'run_identity')}
res['calibration_records']['cpu_model'] = 'cpu_model' in base['runner']
code19, _ = run(os.path.join(ci, 'calib_aggregate.py'), d, '--out', os.path.join(d, 'agg.json'))
shutil.copy(os.path.join(d, 'calib-2.json'), os.path.join(d, 'calib-20.json'))
with open(os.path.join(d, 'calib-20.json')) as f:
    c = json.load(f)
c['index'] = '20'
with open(os.path.join(d, 'calib-20.json'), 'w') as f:
    json.dump(c, f)
code20, o = run(os.path.join(ci, 'calib_aggregate.py'), d, '--out', os.path.join(d, 'agg.json'))
c2 = dict(c, run_identity=dict(c['run_identity'], GITHUB_SHA='b'*40))
with open(os.path.join(d, 'calib-20.json'), 'w') as f:
    json.dump(c2, f)
code_mixed, _ = run(os.path.join(ci, 'calib_aggregate.py'), d, '--out', os.path.join(d, 'agg.json'))
with open(os.path.join(d, 'calib-20.json'), 'w') as f:
    json.dump(c, f)
res['aggregate'] = {'exit_with_19': code19, 'exit_with_20': code20, 'calibrations': (o or {}).get('calibrations'),
                    'exit_two_commits': code_mixed}
runj = {'id': RUN, 'head_sha': SHA, 'head_branch': 'ci-calibration/np-avg-1-stage0', 'event': 'push'}
jobsj = {'jobs': [{'name': 'calibrate (%d)' % i, 'started_at': '2026-10-26T09:59:00Z',
                   'completed_at': '2026-10-26T10:01:%02dZ' % (10 + i)} for i in range(1, 21)] +
         [{'name': 'guard', 'started_at': '2026-10-26T09:58:00Z', 'completed_at': '2026-10-26T09:58:20Z'}]}
for nm, obj in (('run.json', runj), ('jobs.json', jobsj)):
    with open(os.path.join(d, nm), 'w') as f:
        json.dump(obj, f)
code_dir = os.path.join(os.path.dirname(os.path.abspath(ci)), 'code')
post = [os.path.join(ci, 'postrun.py'), '--code', code_dir, '--out', os.path.join(d, 'post.json'),
        '--launch', os.path.join(d, 'run.json'), os.path.join(d, 'jobs.json'), d]
cp, op = run(*(post + ['--authorized-sha', SHA]))
cw, ow = run(*(post + ['--authorized-sha', 'c'*40]))
res['postrun'] = {'holds_exit': cp, 'verdict': (op or {}).get('verdict'), 'u_cal': (op or {}).get('u_cal'),
                  'wrong_sha_exit': cw, 'wrong_sha_verdict': (ow or {}).get('verdict')}
with open(os.path.join(ci, 'np-avg-1-stage0-planted-calibration.yml')) as f:
    y = f.read()
on = y[y.index('\non:'):y.index('\npermissions:')]
res['workflow'] = {'push_branch_only': "branches:\n      - 'ci-calibration/np-avg-1-stage0'" in on and 'push:' in on,
                   'no_other_trigger': all(t not in on for t in ('workflow_dispatch', 'pull_request', 'schedule',
                                                                  'workflow_run')),
                   'read_only': 'permissions:\n  contents: read' in y, 'concurrency': 'concurrency:' in y,
                   'twenty_calibrations': 'index: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]' in y,
                   'max_parallel_4': 'max-parallel: 4' in y,
                   'every_job_has_timeout': y.count('timeout-minutes:') == y.count('runs-on:') == 3,
                   'no_self_pin': 'PIN_WORKFLOW' not in y,
                   'actions_pinned_to_commits': all(len(u.split('@')[1].split()[0]) == 40 for u in
                                                    [ln.strip() for ln in y.splitlines() if ln.strip().startswith('- uses:')]),
                   'aggregate_always_after_guard': "if: ${{ always() && needs.guard.result == 'success' }}" in y,
                   'pins_match_files': all(
                       ("%s: '%s'" % (k, hashlib.sha256(open(os.path.join(os.path.dirname(os.path.abspath(ci)), pth),
                                                              'rb').read()).hexdigest())) in y
                       for k, pth in (('PIN_CALIB_CI', 'ci/calib_ci.py'), ('PIN_CALIB_AGGREGATE', 'ci/calib_aggregate.py'),
                                      ('PIN_MANIFEST', 'code/LAYER2-MANIFEST.json')))}
with open(os.path.join(ci, 'calib_ci.py')) as f:
    src = f.read()
res['forbidden_names'] = all("'%s'" % n in src[src.index('FORBIDDEN = {'):src.index('FORBIDDEN_MODULES')]
                             for n in ('V8_KEY', 'V8_REF', 'NO_V8'))
ok = res['equivalence_mismatches'] == 0 and res['equivalence_exit'] == 0 and res['tripwire']['exit'] == 2 and \
    res['tripwire']['label'] == 'VOID' and not res['tripwire']['file_written'] and res['ordinary_exit'] == 0 and \
    code19 == 2 and code20 == 0 and res['aggregate']['calibrations'] == 20 and all(res['workflow'].values()) and \
    code_mixed == 2 and all(res['calibration_records'].values()) and res['forbidden_names'] and cp == 0 and \
    res['postrun']['verdict'] == 'HOLDS' and res['postrun']['u_cal'] is not None and cw == 2 and \
    res['postrun']['wrong_sha_verdict'] == 'VOID'
res['pass'] = ok
shutil.rmtree(d, ignore_errors=True)
print(json.dumps(res, indent=1, sort_keys=True))
sys.exit(0 if ok else 2)
