#!/usr/bin/env python3
"""job_outputs.py -- extracts, reproduces and compares the job-output expected results of tranche 3.

Tranche 3 retains CI runs that no receipt or certificate attests, cited by frozen records for what one job of the
run printed. Two outputs are read, by the same code from a served GitHub job log (timestamped lines) and from a
fresh run of the same command at the same commit, so an expected result and a reproduction are compared on equal
terms. Standard library only.

  base-check   tools/control_plane_base_check.py --mode M|B --ref REF: every SKIP, PASS and FAIL line, the
               header line with REF replaced by "<REF>" (the ref is the commit checked, kept as provenance: a
               pull-request run's REF is GitHub's synthetic merge, which a reproduction rebuilds from its two
               parents under a new id), and the summary line;
  guard        verification/lean/edge_rigidity_probe.py: every check line as its status, tag and the sha256 of
               its message, the verdict line, and the lines a citing claim quotes, each of which must occur.

    python3 -I job_outputs.py extract base-check|guard LOG       # prints the extraction as JSON
    python3 -I job_outputs.py reproduce --run <run_id> --work <dir>      # from the root of a full-history clone
    python3 -I job_outputs.py --self-test

reproduce reads runs/<run_id>/expected.json from this archive, and for each recorded output: checks out the commit
as a detached worktree (for a pull-request run, the recorded base, merged with the recorded head as GitHub's
synthetic merge was), runs the recorded command in the recorded directory with the recorded environment, extracts
the output and compares it with the expectation. It fails closed: a missing or extra line, a changed status,
message digest, summary or verdict, a quoted line absent, an extraction that finds no summary or verdict, a failed
checkout or merge, or an exception fails it. It writes verdict.json in --work on every exit once that directory is
writable, and the verdict holds only with exit code 0. The verifier is this checkout; the historical commit
supplies only the script it runs. What is compared is deterministic output; timestamps, durations and the order
of the guard's checks are not compared.
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
KINDS = ('base-check', 'guard')


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


EXTRACT = {'base-check': extract_base_check, 'guard': extract_guard}


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
    else:
        f.append('unknown output kind %r' % kind)
    return f


def git(args, cwd=None):
    return subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True)


def reproduce(run_id, work):
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
        doc = json.load(open(path, encoding='utf-8'))
        if not doc.get('outputs'):
            raise ValueError('the entry records no job output')
        ok = True
        for n, o in enumerate(doc['outputs']):
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
    if bc is None or gd is None:
        print('FAIL self: the self-test needs a base-check output and a guard output with a quoted line')
        return 1

    def as_got(o):
        e = o['expected']
        if o['kind'] == 'base-check':
            head = next(l for l in e['lines'] if l.startswith('control_plane_base_check: mode'))
            return {'lines': list(e['lines']), 'header': head, 'ref': 'x', 'summary': e['summary']}
        return {'checks': [dict(c) for c in e['checks']], 'verdict': e['verdict'], 'text': list(e['quoted'])}

    def case(name, o, mutate, msg=None):
        nonlocal ok
        got = as_got(o)
        mutate(got)
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
    if len(a) == 5 and a[0] == 'reproduce' and a[1] == '--run' and a[3] == '--work':
        sys.exit(reproduce(a[2], a[4]))
    print(__doc__)
    sys.exit(2)
