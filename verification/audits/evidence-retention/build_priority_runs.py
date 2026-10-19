#!/usr/bin/env python3
"""build_priority_runs.py -- how runs were retained in tranche 3 ahead of its expiry order (AGENTS §A.42).

Tranche 3 retains cited runs that no receipt attests, earliest log expiry first. A run this script names is
retained ahead of that order: it must be a run of check_retention.py's PRIORITY_ALLOWLIST, the owner-approved
exception, whose record this script copies into the tranche3 section's `priority` list unchanged; the section's
other runs keep their order. For each such run it writes, under runs/<run_id>/, the tranche-3 files
(run.json, jobs.json and expected.json, in build_tranche3.py's form), adds the entry run-<run_id> with every
citing location and its claims, removes the run from tranche3.remaining, and updates the counts.

It cannot be re-run from the tree: its inputs, the API answers and the served job log, are not retained (raw logs
are withheld by AGENTS §A.42 item 1); their digests are. Inputs:
  INPUTS/api-runs/<id>.json, INPUTS/api-jobs/<id>.json   the API answers, as received;
  INPUTS/served/served-<job_id>.txt                       the served job-log text.
Usage: build_priority_runs.py INPUTS ARCHIVE
"""
import datetime
import hashlib
import json
import os
import sys

INP, ARCH = sys.argv[1], sys.argv[2]
ROOT = os.path.abspath(os.path.join(ARCH, '..', '..', '..'))
sys.path.insert(0, ARCH)
import job_outputs  # noqa: E402  (the archive's own extractor)
import check_retention  # noqa: E402  (its PRIORITY_ALLOWLIST)

READ = '2026-10-19'
SOURCE_LOG = ('GitHub Actions job log, read on %s through the session\'s job-log tool, which returns the last '
              'tail_lines lines of a log, at most 5000' % READ)
EXTRACTOR = 'verification/audits/evidence-retention/job_outputs.py'
A37 = 'verification/programmes/oi-qm/track-b/act-37-arc-exclusivity/preregistration.md'
R, J, X = 'run', 'jobs', 'expected'
LEAN = 'verification/lean-mathlib'

GATE_RECIPE = {'cwd': '.', 'argv': ['python3', 'tools/release_gate.py'], 'env': {}, 'exit': 0,
               'before': [{'cwd': LEAN, 'argv': ['lake', 'exe', 'cache', 'get']},
                          {'cwd': LEAN, 'argv': ['lake', '--rehash', 'build']}],
               'requires': 'a full-history clone and a Lean toolchain manager (elan) on PATH: the workflow\'s Build '
                           'step (lake exe cache get, lake --rehash build) and its Release gate step, in that order; '
                           'the gate\'s lean-axioms step runs lake build itself'}

DUR = ('a duration: durations are not part of an expected result (AGENTS §A.42 item 1), and no file of this entry '
       'records one')
RUNS = {
    '36373806246': {
        'served': {'job': 108775417498, 'step': 'Release gate', 'original_lines': 12683, 'served_lines': 1200},
        'cites': [(A37, 63, [
            (62, 'It is certified by', 'retained', [R, J],
             'run.json: event push, head_sha d014bafe…, run_attempt 1, conclusion success; jobs.json: seven jobs at '
             'that head and attempt, each concluding success'),
            (63, 'push run 36373806246', 'retained', [R], 'run.json id 36373806246, event push, head_sha d014bafe…'),
            (63, 'all seven jobs green', 'retained', [J], 'jobs.json: seven jobs, each conclusion success'),
            (63, 'in 3 minutes', 'retained', [R, J],
             'run.json created_at 03:27:42Z; jobs.json: the last job completed at 03:30:42Z, three minutes later '
             '(host metadata, not a job\'s output)'),
            (63, 'the release gate passing', 'retained', [X],
             'expected.json: 21 steps, each PASS, and the verdict line release gate: PASS'),
            (64, 'receipts holding', 'retained', [X],
             'expected.json: v3-receipts "RECEIPTS  12 receipt(s), all hold" (the count on line 63, twelve)'),
            (64, 'the `Mathlib bridge` build green', 'retained', [J, X],
             'jobs.json: job 108775417498 (Mathlib bridge) and its Build step conclude success; expected.json: '
             'lean-axioms PASS, a step that runs lake build and fails on a nonzero exit'),
            (64, '`lean-axioms` at 4829 named results', 'differs', [X],
             'expected.json: lean-axioms "lean_axiom_check: OK (4803 named result(s) reported, no sorr" (job '
             '108775417498, log line 12656 of 12683, served line 1173 of its last 1200). 4829 is the count with act 37\'s module '
             'DitaArcExclusivity.lean, whose 26 #print axioms lines it adds to 4803: this file reports it at line '
             '1339 for design run 36378121576, and act 37\'s result.md at lines 170-171 for stages 2 and 3'),
            (65, 'sorry', 'retained', [X],
             'expected.json: lean-axioms PASS; the check fails on any sorryAx, and its summary, cut at the gate\'s '
             'column width, ends "no sorr"'),
            (65, 'the guard 91 PASS and 0 FAIL', 'not retained', [],
             'the guard prints in job 108775417269 (Numerical probes / core B), whose output this entry does not '
             'retain; jobs.json records that job\'s success'),
            (65, 'act 36\'s probe reporting its `OK` line', 'not retained', [],
             'the probe prints in job 108775417433 (Numerical probes / A36 hierarchy), whose output this entry does '
             'not retain; jobs.json records that job\'s success'),
            (65, 'in 50 seconds', 'not retained', [],
             DUR + '. Observed, not retained: job 108775417433\'s log prints the probe\'s cumulative timer "(85s)" '
                   'at line 224 of 245, its header at 03:27:56.179Z (line 155) and its OK line at 03:29:21.397Z '
                   '(line 226), read on %s from the served text' % READ),
            (66, '35\'s in 45', 'not retained', [],
             DUR + '. Observed, not retained: job 108775417269\'s log prints act 35\'s probe\'s cumulative timer '
                   '"(37s)" at line 1273 of 1294, its header at 03:29:55.148Z (line 1217) and its OK line at '
                   '03:30:32.100Z (line 1275), read on %s from the served text whose sha256 is '
                   '5c62853854d7ac5f07bc1ba37f8d3e8a7d3dde8695edcdf9d474ca78e1170f8a' % READ),
        ])],
    },
}

RUN_FIELDS = ('conclusion', 'created_at', 'display_title', 'event', 'head_branch', 'head_sha', 'id', 'path', 'run_attempt',
              'run_number', 'status', 'updated_at')
JOB_FIELDS = ('completed_at', 'conclusion', 'head_branch', 'head_sha', 'id', 'name', 'run_attempt', 'started_at', 'status',
              'workflow_name')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob_id(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def dump(obj):
    return (json.dumps(obj, indent=1, sort_keys=True) + '\n').encode('utf-8')


def expiry(created):
    return (datetime.datetime.strptime(created, '%Y-%m-%dT%H:%M:%SZ') + datetime.timedelta(days=90)).strftime('%Y-%m-%d')


def file_rec(rel, b, kind, src=None):
    r = {'path': rel, 'bytes': len(b), 'sha256': sha(b), 'kind': kind}
    if src is not None:
        r['source_sha256'] = src
    return r


man_path = os.path.join(ARCH, 'manifest.json')
man = json.load(open(man_path, encoding='utf-8'))
t3 = man['tranche3']
for rid, spec in sorted(RUNS.items()):
    araw = open(os.path.join(INP, 'api-runs', rid + '.json'), 'rb').read()
    jraw = open(os.path.join(INP, 'api-jobs', rid + '.json'), 'rb').read()
    a, jl = json.loads(araw), json.loads(jraw)
    assert str(a['id']) == rid and jl['total_count'] == len(jl['jobs']) and a['conclusion'] == 'success'
    run = {k: a[k] for k in RUN_FIELDS}
    run.update({'run_id': rid, 'source': 'GitHub Actions runs API, GET runs/<run_id>, read %s; selected fields' % READ})
    jobs = {'run_id': rid, 'source': 'GitHub Actions jobs API, GET runs/<run_id>/jobs?filter=all, read %s; selected fields' % READ,
            'jobs': [dict({k: j[k] for k in JOB_FIELDS},
                          steps=[{'number': s['number'], 'name': s['name'], 'conclusion': s['conclusion']} for s in j['steps']])
                     for j in sorted(jl['jobs'], key=lambda j: j['id'])]}
    sv = spec['served']
    job = next(j for j in jl['jobs'] if j['id'] == sv['job'])
    text = open(os.path.join(INP, 'served', 'served-%d.txt' % sv['job']), 'rb').read()
    assert text.decode('utf-8').count('\n') + 1 == sv['served_lines']
    got = job_outputs.extract_gate(text.decode('utf-8'))
    assert got['verdict'] and got['verdict'].startswith('release gate: PASS') and all(s['status'] == 'PASS' for s in got['steps'])
    assert got['counts'] == {'lean-axioms': 4803, 'v3-receipts': 12, 'legacy-records': 303}, got['counts']
    out = {'job_id': str(sv['job']), 'job_name': job['name'], 'step': sv['step'], 'kind': 'gate',
           'at': {'commit': a['head_sha']}, 'recipe': GATE_RECIPE, 'expected': got,
           'source': {'kind': SOURCE_LOG, 'extractor': EXTRACTOR, 'original_lines': sv['original_lines'],
                      'served_lines': sv['served_lines'], 'served_sha256': sha(text),
                      'note': 'the digest identifies the text this result was read from: it is provenance of the '
                              'extraction, not independent proof of the result, which reproduction at the commit '
                              'supplies; the text is not a byte copy of GitHub\'s log archive'}}
    doc = {'schema': 'oi-evidence-job-outputs', 'version': 1,
           'run': {'id': rid, 'head_sha': a['head_sha'], 'event': a['event'], 'attempt': a['run_attempt'], 'workflow': 'verify.yml'},
           'outputs': [out],
           'reproduce': {'tool': 'python3 -I verification/audits/evidence-retention/job_outputs.py reproduce --run %s --work <dir>' % rid,
                         'manual': ['from the root of a full-history clone at a commit that carries this archive, with elan '
                                    'on PATH; <dir> is a new directory',
                                    'git worktree add --detach <dir> <at.commit>',
                                    '(cd <dir>/verification/lean-mathlib && lake exe cache get && lake --rehash build)',
                                    '(cd <dir> && python3 tools/release_gate.py) > <log>',
                                    'python3 -I verification/audits/evidence-retention/job_outputs.py extract gate <log>, '
                                    'and compare it with expected as job_outputs.py compare() does'],
                         'compared': 'gate: every step\'s status, name and summary, the claim-bearing counts and the verdict line; the exit code',
                         'not_compared': 'timestamps, durations, the order of the gate\'s steps, the build output'}}
    d = os.path.join(ARCH, 'runs', rid)
    os.makedirs(d, exist_ok=True)
    files = []
    for name, obj, src in (('run.json', run, araw), ('jobs.json', jobs, jraw), ('expected.json', doc, text)):
        b = dump(obj)
        open(os.path.join(d, name), 'wb').write(b)
        files.append(file_rec('runs/%s/%s' % (rid, name), b, 'derived', sha(src)))
    fmap = {R: 'runs/%s/run.json' % rid, J: 'runs/%s/jobs.json' % rid, X: 'runs/%s/expected.json' % rid}
    citations = []
    for path, line, claims in spec['cites']:
        data = open(os.path.join(ROOT, path), 'rb').read()
        L = data.decode('utf-8').split('\n')
        assert rid in L[line - 1], (rid, path, line)
        cl = []
        for n, t, st, fs, note in claims:
            assert t in L[n - 1], (rid, path, n, t)
            k = {'line': n, 'text': t, 'status': st, 'note': note}
            if fs:
                k['in'] = [fmap[f] for f in fs]
            cl.append(k)
        citations.append({'path': path, 'line': line, 'blob': blob_id(data), 'tokens': [rid], 'claims': cl})
    man['entries'] = [e for e in man['entries'] if e.get('id') != 'run-' + rid]
    man['entries'].append({'id': 'run-' + rid, 'kind': 'derived', 'tranche': 3, 'run_id': rid, 'files': files,
                           'citations': citations, 'expires': expiry(a['created_at'])})
    t3['remaining'] = [r for r in t3['remaining'] if r['run_id'] != rid]
    rec = next(x['record'] for x in check_retention.PRIORITY_ALLOWLIST if x['record']['run_id'] == rid)
    t3['priority'] = [p for p in t3.get('priority', []) if p['run_id'] != rid] + [json.loads(json.dumps(rec))]
t3['retained'] = sum(1 for e in man['entries'] if str(e.get('id', '')).startswith('run-'))
assert t3['uncovered'] == t3['retained'] + len(t3['remaining'])
recs = ('job_outputs.py', 'build_tranche3.py')
for e in man['entries']:
    if e.get('id') == 'tranche3-record':
        e['files'] = [file_rec(p, open(os.path.join(ARCH, p), 'rb').read(), 'complete') for p in recs]
man['entries'] = [e for e in man['entries'] if e.get('id') != 'priority-runs-record']
man['entries'].append({'id': 'priority-runs-record', 'kind': 'complete', 'citations': [], 'files': [
    file_rec('build_priority_runs.py', open(os.path.join(ARCH, 'build_priority_runs.py'), 'rb').read(), 'complete')],
    'provenance': {'source': 'written for this archive: the script that retained the tranche3 section\'s priority runs'}})
open(man_path, 'w', encoding='utf-8').write(json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
print('priority runs: %s; tranche 3 retains %d, %d remaining, earliest %s'
      % (', '.join(sorted(RUNS)), t3['retained'], len(t3['remaining']), t3['remaining'][0]['expires']))
