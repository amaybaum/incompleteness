#!/usr/bin/env python3
"""job_outputs.py -- extracts, reproduces and compares the job-output expected results of tranche 3.

Tranche 3 retains CI runs that no receipt or certificate attests, cited by frozen records for what one job of the
run printed. Three outputs are read, by the same code from a served GitHub job log (timestamped lines) and from a
fresh run of the same command at the same commit, so an expected result and a reproduction are compared on equal
terms. Standard library only.

  base-check   tools/control_plane_base_check.py --mode M|B --ref REF: every SKIP, PASS and FAIL line, the
               header line with REF replaced by "<REF>" (the ref is the commit checked, kept as provenance: a
               pull-request run's REF is GitHub's synthetic merge, which a reproduction rebuilds from its two
               parents under a new id), and the summary line;
  guard        verification/lean/edge_rigidity_probe.py: every check line as its status, tag and the sha256 of
               its message, the verdict line, and the lines a citing claim quotes, each of which must occur;
  gate         tools/release_gate.py in the Mathlib bridge job: each step's status, name and summary, the verdict
               line, and the claim-bearing counts its summaries state (named results of lean-axioms, receipts of
               v3-receipts, records of legacy-records), read by extract_result.py, tranche 1's extractor, so that
               both tranches read a release gate alike. Its lean-axioms step runs `lake build` itself; a recipe may
               name steps to run before the command (`before`), such as fetching Mathlib's cache.

    python3 -I job_outputs.py extract base-check|guard|gate LOG  # prints the extraction as JSON
    python3 -I job_outputs.py reproduce --run <run_id> --work <dir> [--kind K]   # from a full-history clone's root
    python3 -I job_outputs.py --self-test

reproduce reads runs/<run_id>/expected.json from this archive and first validates it: its bytes must have the
size and sha256 the manifest's entry run-<run_id> records, and a gate's recorded counts must be the counts its
recorded steps state. That validation trusts a self-consistent manifest and expectation; the independent anchor
of a priority run, check_retention.py's PRIORITY_ALLOWLIST pins, is applied by check_retention.py, which the
`reproduce evidence` workflow runs first. Then, for each recorded output, it checks out the commit
as a detached worktree (for a pull-request run, the recorded base, merged with the recorded head as GitHub's
synthetic merge was), checks the recipe's recorded `environment` (the Python version and the package versions the
original job ran with), asking the recipe's own interpreter, so that a missing or different package fails closed
with its name before anything runs, runs the recipe's `before` steps, each of which must exit 0, then runs the
recorded command
in the recorded directory with the recorded environment, extracts the output and compares it with the
expectation. It fails closed: an expectation that does not validate, a missing or extra line, a changed status,
message digest, summary, count or verdict, a quoted line absent, a missing, repeated or extra gate step, an
extraction that finds no summary or verdict, a
failed checkout, merge or `before` step, or an exception fails it. It writes verdict.json in --work on every exit
once that directory is writable, and the verdict holds only with exit code 0. The verifier is this checkout; the
historical commit supplies only the script it runs. What is compared is deterministic output; timestamps,
durations, the order of the guard's checks and the order of the gate's steps are not compared.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TS = re.compile(r'^\ufeff?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ')
BC_LINE = re.compile(r'^  (PASS|FAIL|SKIP)  (.*)$')
BC_HEAD = re.compile(r'^control_plane_base_check: mode ([MB]), REF=([0-9a-f]+|\S+), (.*)$')
BC_SUM = re.compile(r'^control_plane_base_check: (OK|FAIL)\b(.*)$')
G_START = '=== edge_rigidity_probe.py ==='
G_CHECK = re.compile(r'^  (PASS|FAIL)  ([^:\s]+): (.*)$')
G_VERDICT = re.compile(r'^edge_rigidity_probe: (.*)$')
KINDS = ('base-check', 'guard', 'gate')


def lines_of(text):
    raw = text.split('\n')
    if raw and raw[-1] == '':
        raw.pop()
    return [TS.sub('', l.lstrip('\ufeff'), count=1) for l in raw]


def extract_base_check(text):
    """The base check's output: the lines after its self-test (a served log carries the self-test first)."""
    ls = lines_of(text)
    start = 0
    for i, l in enumerate(ls):
        if l.startswith('control_plane_base_check: self-test'):
            start = i + 1
    out = {'lines': [], 'header': None, 'ref': None, 'summary': None}
    for l in ls[start:]:
        h = BC_HEAD.match(l)
        if h:
            out['header'] = 'control_plane_base_check: mode %s, REF=<REF>, %s' % (h.group(1), h.group(3))
            out['ref'] = h.group(2)
            out['lines'].append(out['header'])
            continue
        if BC_LINE.match(l):
            out['lines'].append(l)
            continue
        s = BC_SUM.match(l)
        if s:
            out['summary'] = l
            out['lines'].append(l)
            break
    return out


def extract_guard(text):
    """The guard's output: its segment of a probes-job log, or the whole text of a run of the guard alone."""
    ls = lines_of(text)
    if G_START in ls:
        ls = ls[ls.index(G_START) + 1:]
    out = {'checks': [], 'verdict': None, 'text': []}
    for l in ls:
        m = G_CHECK.match(l)
        if m:
            out['checks'].append({'status': m.group(1), 'tag': m.group(2),
                                  'message_sha256': hashlib.sha256(m.group(3).encode('utf-8')).hexdigest()})
        v = G_VERDICT.match(l)
        if v:
            out['verdict'] = l
            break
        out['text'].append(l)
    return out


def tranche1_extractor():
    """extract_result.py, beside this file, loaded by path (an isolated interpreter does not put this directory on
    sys.path)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location('extract_result', os.path.join(HERE, 'extract_result.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# the counts a gate's summaries state, by step: the claims a citing record makes of a gate rest on these
GATE_COUNTS = {'lean-axioms': re.compile(r'\((\d+) named result'), 'v3-receipts': re.compile(r'RECEIPTS\s+(\d+) receipt'),
               'legacy-records': re.compile(r'LEGACY\s+(\d+) record')}


def gate_counts(steps):
    """{step name: the count its summary states}, for each step of GATE_COUNTS present with a count."""
    out = {}
    for s in steps:
        rx = GATE_COUNTS.get(s.get('name'))
        m = rx.search(str(s.get('summary'))) if rx else None
        if m:
            out[s['name']] = int(m.group(1))
    return out


def extract_gate(text):
    """The release gate's block: each step's status, name and summary, the verdict line and the counts the
    summaries state, as extract_result.py reads them from a served Mathlib bridge log or from a fresh run of the
    gate."""
    g = tranche1_extractor().extract(text).get('gate') or {}
    v = g.get('verdict') or {}
    steps = [{'status': s['status'], 'name': s['name'], 'summary': s['summary']} for s in g.get('steps', [])]
    return {'steps': steps, 'counts': gate_counts(steps),
            'verdict': 'release gate: %s' % v['text'] if v.get('text') is not None else None}


EXTRACT = {'base-check': extract_base_check, 'guard': extract_guard, 'gate': extract_gate}


def compare(exp, got):
    """The failures of one reproduced output against its expectation; empty when it matches."""
    f = []
    kind = exp.get('kind')
    if kind == 'base-check':
        if not got.get('summary'):
            return ['extraction found no base-check summary line']
        if got.get('header') is None:
            f.append('extraction found no base-check header line')
        want, have = exp['expected']['lines'], got['lines']
        for l in want:
            if l not in have:
                f.append('missing line: %s' % l[:160])
        for l in have:
            if l not in want:
                f.append('unexpected line: %s' % l[:160])
        if len(want) != len(have) and not f:
            f.append('line count %d, expected %d' % (len(have), len(want)))
        if got['summary'] != exp['expected']['summary']:
            f.append('summary %r, expected %r' % (got['summary'], exp['expected']['summary']))
    elif kind == 'guard':
        if not got.get('verdict'):
            return ['extraction found no guard verdict line']
        key = lambda c: (c['tag'], c['status'], c['message_sha256'])
        want = sorted(key(c) for c in exp['expected']['checks'])
        have = sorted(key(c) for c in got['checks'])
        for c in sorted(set(want) - set(have)):
            f.append('expected check absent: %s %s (message %s)' % (c[1], c[0], c[2][:12]))
        for c in sorted(set(have) - set(want)):
            f.append('unexpected check: %s %s (message %s)' % (c[1], c[0], c[2][:12]))
        if len(want) != len(have) and not f:
            f.append('check count %d, expected %d' % (len(have), len(want)))
        if got['verdict'] != exp['expected']['verdict']:
            f.append('verdict %r, expected %r' % (got['verdict'], exp['expected']['verdict']))
        for q in exp['expected'].get('quoted', []):
            if q not in got['text']:
                f.append('quoted line absent: %s' % q[:160])
    elif kind == 'gate':
        if not got.get('verdict'):
            return ['extraction found no release-gate verdict line']
        want = {s['name']: (s['status'], s['summary']) for s in exp['expected']['steps']}
        have = {}
        for s in got['steps']:
            if s['name'] in have:
                f.append('gate step repeated: %s' % s['name'])
            have[s['name']] = (s['status'], s['summary'])
        for n, w in sorted(want.items()):
            if n not in have:
                f.append('gate step absent: %s' % n)
            elif have[n] != w:
                f.append('gate step %s: %s %r, expected %s %r' % (n, have[n][0], have[n][1][:80], w[0], w[1][:80]))
        for n in sorted(set(have) - set(want)):
            f.append('unexpected gate step: %s' % n)
        wc, hc = exp['expected'].get('counts') or {}, got.get('counts') or {}
        for n in sorted(set(wc) | set(hc)):
            if wc.get(n) != hc.get(n):
                f.append('gate count %s: %s, expected %s' % (n, hc.get(n), wc.get(n)))
        if got['verdict'] != exp['expected']['verdict']:
            f.append('verdict %r, expected %r' % (got['verdict'], exp['expected']['verdict']))
    else:
        f.append('unknown output kind %r' % kind)
    return f


def git(args, cwd=None):
    return subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True)


def validate_expected(run_id, data, man):
    """The expectation a reproduction compares against, validated before anything runs: its bytes are the ones the
    manifest's entry run-<run_id> records (size and sha256), it names that run, and each gate output's counts are
    the counts its own steps state. Returns the parsed document; raises ValueError otherwise."""
    ent = next((e for e in man.get('entries', []) if e.get('id') == 'run-%s' % run_id), None)
    rec = next((f for f in (ent or {}).get('files', []) if f.get('path') == 'runs/%s/expected.json' % run_id), None)
    if rec is None:
        raise ValueError('the manifest records no expected.json for run-%s' % run_id)
    if len(data) != rec.get('bytes') or hashlib.sha256(data).hexdigest() != rec.get('sha256'):
        raise ValueError('expected.json is not the file the manifest records')
    doc = json.loads(data)
    if (doc.get('run') or {}).get('id') != run_id or not doc.get('outputs'):
        raise ValueError('expected.json names another run or records no job output')
    for o in doc['outputs']:
        if o.get('kind') == 'gate' and gate_counts(o['expected']['steps']) != o['expected'].get('counts'):
            raise ValueError('expected.json: the gate counts are not the counts its steps state')
        if o.get('kind') == 'guard':
            cs, ct = o['expected']['checks'], o['expected'].get('counts') or {}
            if ct != {'checks': len(cs), 'R7': sum(1 for c in cs if c['tag'].startswith('R7-')),
                      'PASS': sum(1 for c in cs if c['status'] == 'PASS')}:
                raise ValueError('expected.json: the guard counts are not the counts its checks state')
    return doc


ENV_PROBE = ('import sys, json, importlib.metadata as m\n'
             'out = {"python": "%d.%d.%d" % sys.version_info[:3], "modules": {}}\n'
             'for n in json.loads(sys.argv[1]):\n'
             '    try:\n'
             '        out["modules"][n] = m.version(n)\n'
             '    except m.PackageNotFoundError:\n'
             '        out["modules"][n] = None\n'
             'print(json.dumps(out))\n')


def environment_failures(recipe, env, cwd):
    """The recipe's recorded environment against what its own interpreter (argv[0]) reports: the Python version and
    each recorded package's installed version. Empty when it matches or none is recorded."""
    want = recipe.get('environment')
    if not want:
        return []
    mods = want.get('modules') or {}
    try:
        p = subprocess.run([recipe['argv'][0], '-c', ENV_PROBE, json.dumps(sorted(mods))], cwd=cwd, env=env,
                           capture_output=True, text=True)
        got = json.loads(p.stdout) if p.returncode == 0 else None
    except (OSError, ValueError):
        got = None
    if got is None:
        return ['environment: %s could not report its versions' % recipe['argv'][0]]
    f = []
    if want.get('python') and got['python'] != want['python']:
        f.append('environment: Python %s, recorded %s' % (got['python'], want['python']))
    for n, v in sorted(mods.items()):
        g = got['modules'].get(n)
        if g is None:
            f.append('environment: %s is not installed (recorded %s)' % (n, v))
        elif g != v:
            f.append('environment: %s %s, recorded %s' % (n, g, v))
    return f


def reproduce(run_id, work, kind=None):
    os.makedirs(work, exist_ok=True)
    verdict = {'run': run_id, 'outputs': [], 'holds': False, 'stopped': None}
    vpath = os.path.join(work, 'verdict.json')

    def write():
        open(vpath, 'w', encoding='utf-8').write(json.dumps(verdict, indent=1, sort_keys=True) + '\n')
    code = 1
    try:
        if not re.fullmatch(r'[0-9]{1,20}', str(run_id)):
            raise ValueError('run id must be decimal')
        path = os.path.join(HERE, 'runs', run_id, 'expected.json')
        man = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
        doc = validate_expected(run_id, open(path, 'rb').read(), man)
        if kind is not None and kind not in KINDS:
            raise ValueError('--kind must be one of %s' % ', '.join(KINDS))
        outs = [(n, o) for n, o in enumerate(doc['outputs']) if kind is None or o['kind'] == kind]
        if not outs:
            raise ValueError('run-%s records no %s output' % (run_id, kind))
        verdict['kind'] = kind
        ok = True
        for n, o in outs:
            at = o['at']
            d = os.path.join(work, 'tree-%d' % n)
            if os.path.exists(d):
                raise ValueError('%s exists; give a fresh --work' % d)
            base = at.get('base') or at.get('commit')
            for c in (base, at.get('head')):
                if c is not None and not re.fullmatch(r'[0-9a-f]{40}', c):
                    raise ValueError('commit %r is not a full id' % c)
            r = git(['worktree', 'add', '--detach', d, base])
            rec = {'job_id': o['job_id'], 'kind': o['kind'], 'checkout': r.returncode}
            if r.returncode == 0 and at.get('head'):
                m = git(['-c', 'user.name=reproduce', '-c', 'user.email=reproduce', 'merge', '--no-ff', '--no-edit',
                         at['head']], cwd=d)
                rec['merge'] = m.returncode
            if rec['checkout'] != 0 or rec.get('merge', 0) != 0:
                rec['failures'] = ['checkout or merge failed']
                ok = False
            else:
                env = {k: v for k, v in os.environ.items() if not k.startswith('GITHUB_')}
                env.update(o['recipe']['env'])
                early = environment_failures(o['recipe'], env, os.path.join(d, o['recipe']['cwd']))
                rec['before'] = []
                for b in (o['recipe'].get('before', []) if not early else []):
                    q = subprocess.run(list(b['argv']), cwd=os.path.join(d, b['cwd']), env=env, capture_output=True,
                                       text=True)
                    open(os.path.join(work, 'before-%d-%d.txt' % (n, len(rec['before']))), 'w',
                         encoding='utf-8').write(q.stdout + q.stderr)
                    rec['before'].append(q.returncode)
                    if q.returncode != 0:
                        early.append('before step %s exited %d' % (' '.join(b['argv']), q.returncode))
                        break
                if early:
                    rec['failures'] = early
                    ok = False
                    verdict['outputs'].append(rec)
                    git(['worktree', 'remove', '--force', d])
                    continue
                cmd = list(o['recipe']['argv'])
                p = subprocess.run(cmd, cwd=os.path.join(d, o['recipe']['cwd']), env=env, capture_output=True,
                                   text=True)
                log = os.path.join(work, 'output-%d.txt' % n)
                open(log, 'w', encoding='utf-8').write(p.stdout + p.stderr)
                rec['exit'] = p.returncode
                got = EXTRACT[o['kind']](p.stdout)
                rec['failures'] = compare(o, got)
                if p.returncode != o['recipe']['exit']:
                    rec['failures'].append('exit %d, expected %d' % (p.returncode, o['recipe']['exit']))
                ok &= not rec['failures']
            verdict['outputs'].append(rec)
            git(['worktree', 'remove', '--force', d])
        code = 0 if ok else 1
    except Exception as exc:  # recorded, and the verdict fails closed
        verdict['stopped'] = '%s: %s' % (type(exc).__name__, exc)
        code = 1
    verdict['holds'] = code == 0
    write()
    print('JOB-OUTPUTS  run %s: %s%s' % (run_id, 'HOLDS' if code == 0 else 'FAILS',
                                         '' if not verdict['stopped'] else ' (%s)' % verdict['stopped']))
    for o in verdict['outputs']:
        for x in o.get('failures', []):
            print('FAIL  job %s %s: %s' % (o['job_id'], o['kind'], x))
    return code


def self_test():
    """Each mutation of a real expected result must fail the comparison with its own message; the expectation
    compared with itself, as a reproduction would extract it, must pass."""
    ok = True
    docs = []
    rd = os.path.join(HERE, 'runs')
    for r in sorted(os.listdir(rd)) if os.path.isdir(rd) else []:
        p = os.path.join(rd, r, 'expected.json')
        if os.path.isfile(p):
            docs.append(json.load(open(p, encoding='utf-8')))
    outs = [o for d in docs for o in d.get('outputs', [])]
    bc = next((o for o in outs if o['kind'] == 'base-check'), None)
    gd = next((o for o in outs if o['kind'] == 'guard' and o['expected'].get('quoted')), None)
    gt = next((o for o in outs if o['kind'] == 'gate'), None)
    if bc is None or gd is None or gt is None:
        print('FAIL self: the self-test needs a base-check output, a guard output with a quoted line and a gate output')
        return 1

    def as_got(o):
        e = o['expected']
        if o['kind'] == 'base-check':
            head = next(l for l in e['lines'] if l.startswith('control_plane_base_check: mode'))
            return {'lines': list(e['lines']), 'header': head, 'ref': 'x', 'summary': e['summary']}
        if o['kind'] == 'gate':
            return {'steps': [dict(s) for s in e['steps']], 'verdict': e['verdict']}
        return {'checks': [dict(c) for c in e['checks']], 'verdict': e['verdict'], 'text': list(e['quoted'])}

    def case(name, o, mutate, msg=None):
        nonlocal ok
        got = as_got(o)
        mutate(got)
        if o['kind'] == 'gate' and 'counts' not in got:
            got['counts'] = gate_counts(got['steps'])       # as extract_gate derives them from the steps
        fails = compare(o, got)
        good = (not fails) if msg is None else any(msg in x for x in fails)
        ok &= good
        print('%s self: %s' % ('PASS' if good else 'FAIL', name))
        if not good:
            print('      got: %s' % fails[:3])

    row = next(i for i, l in enumerate(bc['expected']['lines']) if l.startswith('  PASS  '))
    case('a base check equal to its expectation passes', bc, lambda g: None)
    case('a row turned FAIL', bc, lambda g: g['lines'].__setitem__(row, g['lines'][row].replace('  PASS  ', '  FAIL  ', 1)),
         'missing line')
    case('a row dropped', bc, lambda g: g['lines'].pop(row), 'missing line')
    case('an extra row', bc, lambda g: g['lines'].insert(row, '  PASS  x :: row extra  -- y'), 'unexpected line')
    case('a duplicated row', bc, lambda g: g['lines'].insert(row, g['lines'][row]), 'line count')
    case('another summary', bc, lambda g: g.__setitem__('summary', 'control_plane_base_check: FAIL (mode B, 1 row(s))'),
         'summary')
    case('no summary extracted', bc, lambda g: g.__setitem__('summary', None), 'no base-check summary')
    case('no header extracted', bc, lambda g: g.__setitem__('header', None), 'no base-check header')
    case('a guard equal to its expectation passes', gd, lambda g: None)
    case('a guard check turned FAIL', gd, lambda g: g['checks'][0].__setitem__('status', 'FAIL'), 'expected check absent')
    case('a guard check with another message', gd, lambda g: g['checks'][0].__setitem__('message_sha256', '0' * 64),
         'unexpected check')
    case('a guard check dropped', gd, lambda g: g['checks'].pop(0), 'expected check absent')
    case('a guard check duplicated', gd, lambda g: g['checks'].append(dict(g['checks'][0])), 'check count')
    case('another guard verdict', gd, lambda g: g.__setitem__('verdict', 'edge_rigidity_probe: FAILURE'), 'verdict')
    case('no guard verdict extracted', gd, lambda g: g.__setitem__('verdict', None), 'no guard verdict')
    case('a quoted line absent', gd, lambda g: g.__setitem__('text', []), 'quoted line absent')
    ax = next(i for i, s in enumerate(gt['expected']['steps']) if s['name'] == 'lean-axioms')
    case('a gate equal to its expectation passes', gt, lambda g: None)
    case('a gate in another step order passes', gt, lambda g: g['steps'].reverse())
    case('a gate step turned FAIL', gt, lambda g: g['steps'][ax].__setitem__('status', 'FAIL'), 'gate step lean-axioms')
    plus26 = lambda g: g['steps'][ax].__setitem__('summary', re.sub(
        r'\(\d+ named', '(%d named' % (int(re.search(r'\((\d+) named', g['steps'][ax]['summary']).group(1)) + 26),
        g['steps'][ax]['summary']))
    case('a gate step with another count in its summary (4803 read as 4829)', gt, plus26, 'gate step lean-axioms')
    case('the same: the claim-bearing count differs', gt, plus26, 'gate count lean-axioms')
    case('a gate count alone changed', gt, lambda g: g.__setitem__('counts', dict(gate_counts(g['steps']), **{'v3-receipts': 13})),
         'gate count v3-receipts')
    case('a gate count missing', gt, lambda g: g.__setitem__('counts', {}), 'gate count legacy-records')
    case('a gate step dropped', gt, lambda g: g['steps'].pop(ax), 'gate step absent')
    case('an extra gate step', gt, lambda g: g['steps'].append({'status': 'PASS', 'name': 'extra', 'summary': 'x'}),
         'unexpected gate step')
    case('a gate step repeated', gt, lambda g: g['steps'].append(dict(g['steps'][ax])), 'gate step repeated')
    case('another gate verdict', gt, lambda g: g.__setitem__('verdict', 'release gate: FAILED -> lean-axioms'), 'verdict')
    case('no gate verdict extracted', gt, lambda g: g.__setitem__('verdict', None), 'no release-gate verdict')
    fails = compare(dict(bc, kind='other'), as_got(bc))
    good = any('unknown output kind' in x for x in fails)
    ok &= good
    print('%s self: an unknown output kind' % ('PASS' if good else 'FAIL'))
    # the extractors on synthetic logs, served form and fresh form alike
    served = ('\ufeff2026-01-01T00:00:00.0000000Z control_plane_base_check: self-test OK\n'
              '2026-01-01T00:00:00.0000000Z   SKIP  a.md :: unchanged\n'
              '2026-01-01T00:00:00.0000000Z control_plane_base_check: mode B, REF=%s, 1 control-plane file(s)\n'
              '2026-01-01T00:00:00.0000000Z   PASS  b.md :: row r1  -- fine\n'
              '2026-01-01T00:00:00.0000000Z control_plane_base_check: OK (mode B, 1 row(s), no failure)\n'
              '2026-01-01T00:00:00.0000000Z Post job cleanup.\n') % ('a' * 40)
    fresh = '\n'.join(TS.sub('', l.lstrip('\ufeff')) for l in served.split('\n')[1:]).replace('a' * 40, 'b' * 40)
    e1, e2 = extract_base_check(served), extract_base_check(fresh)
    good = e1['lines'] == e2['lines'] and e1['ref'] == 'a' * 40 and e2['ref'] == 'b' * 40 and len(e1['lines']) == 4
    ok &= good
    print('%s self: the base-check extraction reads a served log and a fresh run alike, REF aside' % ('PASS' if good else 'FAIL'))
    g1 = extract_guard('x\n=== edge_rigidity_probe.py ===\n  PASS  R1: m\n    R7-Q detail\n  FAIL  R7-Z: n\n'
                       'edge_rigidity_probe: FAILURE\n=== next_probe.py ===\n  PASS  R9: z\n')
    good = [c['tag'] for c in g1['checks']] == ['R1', 'R7-Z'] and g1['verdict'] == 'edge_rigidity_probe: FAILURE' \
        and '    R7-Q detail' in g1['text']
    ok &= good
    print('%s self: the guard extraction stops at its verdict and keeps detail lines' % ('PASS' if good else 'FAIL'))
    gate_served = ('2026-01-01T00:00:00.0000000Z Build completed successfully (3 jobs).\n'
                   '2026-01-01T00:00:00.0000000Z release gate\n'
                   '2026-01-01T00:00:00.0000000Z ' + '=' * 68 + '\n'
                   '2026-01-01T00:00:00.0000000Z   PASS  lean-axioms      lean_axiom_check: OK (7 named result(s) reported, no sorr\n'
                   '2026-01-01T00:00:00.0000000Z   FAIL  voice            voice_check: FAILED\n'
                   '2026-01-01T00:00:00.0000000Z ' + '=' * 68 + '\n'
                   '2026-01-01T00:00:00.0000000Z release gate: FAILED -> voice\n'
                   '2026-01-01T00:00:00.0000000Z Post job cleanup.')
    gate_fresh = '\n'.join(TS.sub('', l) for l in gate_served.split('\n')[1:-1]) + '\n'
    x1, x2 = extract_gate(gate_served), extract_gate(gate_fresh)
    good = x1 == x2 and x1['verdict'] == 'release gate: FAILED -> voice' and \
        [(s['status'], s['name']) for s in x1['steps']] == [('PASS', 'lean-axioms'), ('FAIL', 'voice')] and \
        x1['steps'][0]['summary'] == 'lean_axiom_check: OK (7 named result(s) reported, no sorr' and \
        extract_gate('no gate here\n')['verdict'] is None
    ok &= good
    print('%s self: the gate extraction reads a served log and a fresh run alike' % ('PASS' if good else 'FAIL'))
    good = x1['counts'] == {'lean-axioms': 7} and gate_counts([{'name': 'v3-receipts', 'summary': 'RECEIPTS  12 receipt(s), all hold'},
                                                                {'name': 'legacy-records', 'summary': 'LEGACY  303 record(s) in 75'}]) \
        == {'v3-receipts': 12, 'legacy-records': 303}
    ok &= good
    print('%s self: the gate counts are read from the summaries' % ('PASS' if good else 'FAIL'))
    # the expectation is validated before a reproduction runs
    gdoc = next(d for d in docs if any(o['kind'] == 'gate' for o in d['outputs']))
    grun = gdoc['run']['id']
    gdata = open(os.path.join(rd, grun, 'expected.json'), 'rb').read()
    gman = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))

    def vcase(name, data, man, msg):
        nonlocal ok
        try:
            validate_expected(grun, data, man)
            got = None
        except ValueError as exc:
            got = str(exc)
        good = (got is None) if msg is None else (got is not None and msg in got)
        ok &= good
        print('%s self: %s' % ('PASS' if good else 'FAIL', name))
    vcase('the archived gate expectation validates', gdata, gman, None)
    vcase('an expectation whose bytes are not the manifest\'s', gdata.replace(b'4803', b'4829'), gman, 'not the file')
    tampered = json.loads(gdata)
    tampered['outputs'][0]['expected']['counts']['lean-axioms'] += 26
    tb = json.dumps(tampered).encode('utf-8')
    tman = json.loads(json.dumps(gman))
    for e in tman['entries']:
        for f in e.get('files', []):
            if f['path'] == 'runs/%s/expected.json' % grun:
                f['bytes'], f['sha256'] = len(tb), hashlib.sha256(tb).hexdigest()
    vcase('an expectation whose counts its steps do not state, the manifest following it', tb, tman, 'gate counts')
    vcase('a run the manifest has no entry for', gdata, {'entries': []}, 'records no expected.json')
    # the recorded environment, asked of the recipe's own interpreter
    here = '%d.%d.%d' % sys.version_info[:3]

    def ecase(name, want, msg):
        nonlocal ok
        fails = environment_failures({'argv': [sys.executable], 'environment': want}, dict(os.environ), HERE)
        good = (not fails) if msg is None else any(msg in x for x in fails)
        ok &= good
        print('%s self: %s' % ('PASS' if good else 'FAIL', name))
        if not good:
            print('      got: %s' % fails[:3])
    ecase('an environment the interpreter matches passes', {'python': here, 'modules': {}}, None)
    ecase('a recorded package not installed fails closed by name', {'python': here, 'modules': {'numpy-absent-xyz': '2.4.6'}},
          'numpy-absent-xyz is not installed (recorded 2.4.6)')
    ecase('another Python version fails', {'python': '0.0.1'}, 'Python %s, recorded 0.0.1' % here)
    bad = environment_failures({'argv': ['/nonexistent/python3'], 'environment': {'python': here}}, dict(os.environ), HERE)
    good = any('could not report its versions' in x for x in bad)
    ok &= good
    print('%s self: an interpreter that cannot run fails closed' % ('PASS' if good else 'FAIL'))
    with tempfile.TemporaryDirectory() as tmp:
        code = reproduce(grun, tmp, 'base-check')
        v = json.load(open(os.path.join(tmp, 'verdict.json')))
        good = code == 1 and v['holds'] is False and 'records no base-check output' in (v['stopped'] or '')
        ok &= good
        print('%s self: a kind the entry does not record fails' % ('PASS' if good else 'FAIL'))
    with tempfile.TemporaryDirectory() as tmp:
        code = reproduce(grun, tmp, 'bridge')
        v = json.load(open(os.path.join(tmp, 'verdict.json')))
        good = code == 1 and v['holds'] is False and '--kind must be one of' in (v['stopped'] or '')
        ok &= good
        print('%s self: an unknown kind fails' % ('PASS' if good else 'FAIL'))
    with tempfile.TemporaryDirectory() as tmp:
        code = reproduce('not-a-run', tmp)
        v = json.load(open(os.path.join(tmp, 'verdict.json')))
        good = code == 1 and v['holds'] is False and 'decimal' in (v['stopped'] or '')
        ok &= good
        print('%s self: a rejected argument writes a failing verdict' % ('PASS' if good else 'FAIL'))
    print('self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--self-test']:
        sys.exit(self_test())
    if len(a) == 3 and a[0] == 'extract' and a[1] in EXTRACT:
        print(json.dumps(EXTRACT[a[1]](open(a[2], encoding='utf-8', errors='replace').read()), indent=1, sort_keys=True))
        sys.exit(0)
    if len(a) in (5, 7) and a[0] == 'reproduce' and a[1] == '--run' and a[3] == '--work' and \
            (len(a) == 5 or a[5] == '--kind'):
        sys.exit(reproduce(a[2], a[4], a[6] if len(a) == 7 else None))
    print(__doc__)
    sys.exit(2)
