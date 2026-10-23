#!/usr/bin/env python3
"""Assemble PRESERVE-INDUCT-1's E results from the WHOLE bridge-job log, in CI, and print them. Python 3 stdlib and git.

  python3 -I assemble_e.py --objects O --history H --host HOST --logs LOGS --download-record REC --work W --python PY
  python3 -I assemble_e.py --window-control --repo REPO --api API --expect EDIR --work W
  python3 -I assemble_e.py --self-test

The extractor is the round's pinned one: D's (ec36234c) verification/audits/evidence-retention/extract_result.py (blob
05c41bce) and build_archive.py (blob 860ec868), the code that built the round's f-run, predicted-tree and window-based
e-run results. Its results_for() and dumps() are loaded from those blobs, after their ids are checked, exactly as the
window-based builder loaded them, so a whole-log result differs from the window result only where the extra lines do.

CI mode reads E's run record and jobs (fetch_records.py), the downloaded whole bridge and probe logs and their download
record (download_job_logs.py), D's blobs from O and E's history to D from H (fetch_sources.py). It builds:
  results.json  results_for() over the whole bridge log (source: the whole log, downloaded in CI);
  cells-ci.json the final bridge step's block and the probe job's lines, read from the whole logs, and the round's
                frozen controls.py (blob 208801fc) run in CI as `verdict E --freeze F --axioms <whole bridge log>` in a
                worktree of H at E, labelled verdict_ci: a CI run, distinct from the verdict the session ran over the
                served window, which the e-run record keeps separately.
Each is printed between workflow-command stop markers as numbered lines `R <name> <i>/<n> <text>` with '#' written as
\\u0023, after a `RESULT <name> bytes=<b> sha256=<h> lines=<n>` header, so a reader of the served job log can rebuild
the exact bytes and check them. The whole raw logs are never printed or committed: only their digests and line counts.
It ends with one line: EXTRACT HOLDS (exit 0), EXTRACT FAILS (exit 1) or EXTRACT UNVERIFIED (exit 2).

--window-control rebuilds results.json from the session's served window exactly as the window-based builder did and
compares it, byte for byte, with the committed one (the #904 head's evidence/e-run/results.json), and compares the
final-step block and the probe lines with the committed cells.json: the control that the same code path is used.
"""
import argparse
import ast
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import types

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
D = 'ec36234cb98a30ecb4681e118ff9ccb82e19aa6d'
F = '46781818f8d8da53153dbe62c9e88c61488960ff'
E = '46e6f3196d425a7c7d797a9667d53a9e628f7d6a'
RUN_ID, BRIDGE_JOB, PROBE_JOB = '39940811486', '120371493729', '120371494151'
JOBS_TOTAL = 38
RD = 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/'
A = 'verification/audits/evidence-retention/'
PINNED_BLOBS = {A + 'extract_result.py': '05c41bce610b8d02ccbaca8e69377b771bef4a35',
                A + 'build_archive.py': '860ec8682981081e1cd196056989a6903e03d966'}
CONTROLS_BLOB = '208801fcb4b96808c8f9a3d5c7175bcf79d38981'
WANT_TOKENS = {'Q-CORE': 'PRESERVE-INDUCT-CORE-PROVED', 'Q-COR': 'PRESERVE-INDUCT-COROLLARIES-PROVED',
               'Q-EXACT': 'PRESERVE-INDUCT-EXACT-CHECKED'}
TS = re.compile(r'^\ufeff?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ?')
PROBE_WANT = re.compile(r'^(SYMPY |REJECTED |mutations: |SAMPLE-MANIFEST-SHA256 |checks: |'
                        r'preserve_induct1_(probe|indep_check): |PASS self|controls: )')
SHA = lambda b: hashlib.sha256(b).hexdigest()


def _targets():
    import importlib.util
    spec = importlib.util.spec_from_file_location('evidence_targets', os.path.join(HERE, 'targets.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git(gitdir, *args, cwd=None):
    cmd = ['git'] + (['--git-dir', gitdir] if gitdir else []) + list(args)
    return subprocess.run(cmd, capture_output=True, cwd=cwd)


def blob(gitdir, rev, path):
    r = git(gitdir, 'cat-file', 'blob', '%s:%s' % (rev, path))
    if r.returncode:
        raise SystemExit('missing %s:%s' % (rev[:12], path))
    return r.stdout


def load_extractor(gitdir):
    """D's extract() and the build_archive.py functions the window builder used; blob ids checked first."""
    for path, want in PINNED_BLOBS.items():
        got = git(gitdir, 'rev-parse', '%s:%s' % (D, path)).stdout.decode().strip()
        if got != want:
            raise SystemExit('pinned blob mismatch for %s: %s, want %s' % (path, got, want))
    ext = types.ModuleType('extract_result')
    exec(compile(blob(gitdir, D, A + 'extract_result.py'), 'extract_result.py', 'exec'), ext.__dict__)
    tree = ast.parse(blob(gitdir, D, A + 'build_archive.py').decode())
    keep = {'show', 'git', 'blob_id', 'sha256', 'lines_of', 'dumps', 'spans', 'results_for', 'secret_hits'}
    consts = {'PRINT', 'PERMITTED', 'EXTRACTOR', 'RECIPE', 'SOURCE_NOTE', 'SECRET'}
    body = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in keep) or
            (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in consts for t in n.targets)) or
            (isinstance(n, (ast.Import, ast.ImportFrom)) and not (isinstance(n, ast.ImportFrom) and n.module == 'extract_result'))]
    g = {'__name__': 'ba', 'extract': ext.extract, 'problems': [], 'BASE': D}
    exec(compile(ast.Module(body=body, type_ignores=[]), 'build_archive.py', 'exec'), g)
    return g


def governed_mods(prereg):
    m = re.search(r'```v3-governed-paths\n(.*?)```', prereg, re.S)
    return sorted({l.split()[2].split('verification/lean-mathlib/', 1)[-1] for l in m.group(1).split('\n')
                   if len(l.split()) == 3 and l.split()[0] == 'execution' and l.split()[2].endswith('.lean')})


def build_results(g, text, run, source, window_note, first=1, original=None):
    """results_for() over text, with the window field the window builder added; returns (res, gaps)."""
    n = len(g['lines_of'](text))
    original = original if original is not None else n
    res, gaps = g['results_for'](text, E, run['mods'], run['run'], source, tool=False)
    res['gaps'] = gaps
    res['window'] = {'first_original_line': first, 'last_original_line': original, 'original_lines': original,
                     'note': window_note}
    return res, gaps


def final_block(g, text):
    wl = g['lines_of'](text)
    marker = [i for i, l in enumerate(wl) if 'preserve_induct1 axioms: step at ' in l and 'echo' not in l]
    okl = [i for i, l in enumerate(wl) if 'preserve_induct1 axioms: OK -- ' in l]
    if len(marker) != 1 or len(okl) != 1 or marker[0] > okl[0]:
        return None
    block = [TS.sub('', l) for l in wl[marker[0]:okl[0] + 1]]
    return block if ('preserve_induct1 axioms: step at ' + E) in block[0] else None


def probe_lines(g, ptext):
    return [l for l in (TS.sub('', x) for x in g['lines_of'](ptext)) if PROBE_WANT.match(l)]


# The printed files are JSON text written by dumps(), which never writes an escape for '#'. Each '#' is printed as the
# JSON escape \u0023, because the served log drops what precedes '##[' on a line; the reverse replaces only an escape
# preceded by an even run of backslashes, so a string that itself contains a backslash before u0023 survives.
UNESC = re.compile(r'(?<!\\)((?:\\\\)*)\\u0023')


def emit_numbered(name, data, out=sys.stdout):
    text = data.decode('utf-8')
    lines = text.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]
    print('RESULT %s bytes=%d sha256=%s lines=%d' % (name, len(data), SHA(data), len(lines)), file=out)
    for i, l in enumerate(lines, 1):
        print('R %s %d/%d %s' % (name, i, len(lines), l.replace('#', '\\u0023')), file=out)


def parse_numbered(log_text):
    """Inverse of emit_numbered over a served job log: {name: bytes}, each checked against its header."""
    heads, parts = {}, {}
    for raw in log_text.split('\n'):
        l = TS.sub('', raw.rstrip('\r'))
        m = re.match(r'RESULT (\S+) bytes=(\d+) sha256=([0-9a-f]{64}) lines=(\d+)$', l)
        if m:
            heads[m.group(1)] = (int(m.group(2)), m.group(3), int(m.group(4)))
            parts[m.group(1)] = {}
            continue
        m = re.match(r'R (\S+) (\d+)/(\d+) (.*)$', l) or re.match(r'R (\S+) (\d+)/(\d+)$', l)
        if m and m.group(1) in parts:
            parts[m.group(1)][int(m.group(2))] = UNESC.sub(r'\1#', m.group(4) if m.lastindex >= 4 else '')
    out = {}
    for name, (nb, h, nl) in heads.items():
        p = parts[name]
        if sorted(p) != list(range(1, nl + 1)):
            raise ValueError('%s: %d of %d numbered lines served' % (name, len(p), nl))
        data = ('\n'.join(p[i] for i in range(1, nl + 1)) + '\n').encode('utf-8')
        if len(data) != nb or SHA(data) != h:
            raise ValueError('%s: rebuilt bytes do not match the printed header' % name)
        out[name] = data
    return out


def decide(c):
    """c: named booleans or None (not measured). FAILS on any False, UNVERIFIED on any None, HOLDS otherwise."""
    if any(v is False for v in c.values()):
        return 'FAILS', 1
    if any(v is None for v in c.values()):
        return 'UNVERIFIED', 2
    return 'HOLDS', 0


def ci(a):
    T = _targets()
    tg = T.load()['targets']
    checks = {}
    t = tg[0]
    checks['targets name E\'s run, bridge job and probe job'] = (len(tg) == 1 and t['run_id'] == RUN_ID and t['commit'] == E
                                                                 and t['bridge_job'] == BRIDGE_JOB and t['cells']['probe_job'] == PROBE_JOB)
    # host records
    try:
        run_raw = open(os.path.join(a.host, 'run-%s.json' % RUN_ID), 'rb').read()
        r = json.loads(run_raw)
        jl = json.load(open(os.path.join(a.host, 'jobs-%s.json' % RUN_ID)))['jobs']
        bj = json.load(open(os.path.join(a.host, 'job-%s.json' % BRIDGE_JOB)))
        pj = json.load(open(os.path.join(a.host, 'job-%s.json' % PROBE_JOB)))
        checks['run record: id, head E, attempt 1, workflow_dispatch, success'] = (
            str(r['id']) == RUN_ID and r['head_sha'] == E and r['run_attempt'] == 1 and r['event'] == 'workflow_dispatch'
            and r['conclusion'] == 'success')
        checks['jobs: %d, all success at E' % JOBS_TOTAL] = (len(jl) == JOBS_TOTAL and all(
            x['conclusion'] == 'success' and x['head_sha'] == E for x in jl))
        checks['bridge job is the run\'s Mathlib bridge, success'] = (bj['name'] == 'Mathlib bridge' and bj['conclusion'] == 'success'
                                                                      and str(bj['run_id']) == RUN_ID and bj['head_sha'] == E)
        checks['probe job is the round\'s probe shard, success'] = (
            pj['name'] == 'Numerical probes / PRESERVE-INDUCT-1 preservation induction' and pj['conclusion'] == 'success'
            and str(pj['run_id']) == RUN_ID and pj['head_sha'] == E)
        print('host run=%s head=%s attempt=%s event=%s conclusion=%s jobs=%d bridge_job=%s probe_job=%s'
              % (r['id'], r['head_sha'], r['run_attempt'], r['event'], r['conclusion'], len(jl), bj['id'], pj['id']))
    except (OSError, ValueError, KeyError) as e:
        print('host records unreadable: %s' % type(e).__name__)
        r = None
        for k in ('run record: id, head E, attempt 1, workflow_dispatch, success', 'jobs: %d, all success at E' % JOBS_TOTAL):
            checks[k] = None
    # downloads
    texts = {}
    try:
        rec = {str(x['job_id']): x for x in json.load(open(a.download_record))['logs']}
    except (OSError, ValueError, KeyError, TypeError) as e:
        print('download record unreadable: %s' % type(e).__name__)
        rec = {}
    for jid in (BRIDGE_JOB, PROBE_JOB):
        x = rec.get(jid)
        path = os.path.join(a.logs, '%s.log' % jid)
        if not x or x.get('outcome') != 'ok' or not os.path.exists(path):
            checks['log %s downloaded whole' % jid] = None
            continue
        data = open(path, 'rb').read()
        ok = SHA(data) == x['sha256'] and len(data) == x['bytes']
        checks['log %s matches its download record' % jid] = ok
        try:
            texts[jid] = data.decode('utf-8')
        except UnicodeDecodeError:
            checks['log %s is UTF-8' % jid] = False
            continue
        print('log job=%s bytes=%d lines=%d sha256=%s' % (jid, len(data), len(texts[jid].split('\n')) - (texts[jid].endswith('\n')),
                                                          SHA(data)))
    if BRIDGE_JOB not in texts or PROBE_JOB not in texts or r is None:
        checks['inputs complete'] = None
        verdict, code = decide(checks)
        for k, v in checks.items():
            print('check %s %s' % ({True: 'ok', False: 'FAIL', None: 'unmeasured'}[v], k))
        print('EXTRACT %s' % verdict)
        return code
    # assemble in a worktree of the history repository at E
    wt = os.path.join(a.work, 'e-wt')
    w = git(a.history, 'worktree', 'add', '--detach', wt, E)
    if w.returncode:
        print('worktree at E failed: %s' % w.stderr.decode()[-200:])
        print('EXTRACT UNVERIFIED')
        return 2
    os.chdir(wt)
    g = load_extractor(a.objects)
    prereg = blob(a.history, F, RD + 'preregistration.md').decode()
    btext, ptext = texts[BRIDGE_JOB], texts[PROBE_JOB]
    bbytes = btext.encode('utf-8')
    n = len(g['lines_of'](btext))
    runinfo = {'mods': governed_mods(prereg),
               'run': {'id': RUN_ID, 'head_sha': E, 'event': r['event'], 'conclusion': r['conclusion'],
                       'attempt': r['run_attempt'], 'workflow': 'verify.yml', 'job_id': BRIDGE_JOB, 'job_name': 'Mathlib bridge'}}
    ci_run = os.environ.get('GITHUB_RUN_ID', 'local')
    source = {'kind': 'GitHub Actions job log, downloaded whole in CI by the extraction workflow (run %s, attempt %s, '
                      'commit %s) through the jobs/<id>/logs endpoint' % (ci_run, os.environ.get('GITHUB_RUN_ATTEMPT', '?'),
                                                                         os.environ.get('GITHUB_SHA', '?')),
              'served_sha256': SHA(bbytes), 'served_lines': n, 'original_lines': n}
    res, gaps = build_results(g, btext, runinfo, source,
                              'the served text is the whole log, downloaded in CI; the reports and markers above are read from all of it')
    rdata = g['dumps'](res)
    exp = res['expected']
    checks['whole log: build success'] = exp['build_success']
    checks['whole log: release gate PASS, every step PASS'] = (exp['gate']['verdict'] is not None and 'PASS' in exp['gate']['verdict']
                                                               and exp['gate']['steps_pass'] == exp['gate']['steps_total'] > 0)
    checks['whole log: every governed module complete, every report within the permitted axioms'] = all(
        m['status'] == 'complete' and all(set(x['axioms']) <= set(exp['permitted_axioms']) for x in m['reports'])
        for m in exp['modules'].values())
    checks['whole log: every failure marker counted zero'] = bool(exp['markers']) and not any(exp['markers'].values())
    checks['whole log: no gaps'] = not gaps
    checks['extractor reported no problems'] = not g['problems']
    checks['no secret pattern in the results'] = not g['secret_hits'](rdata.decode())
    # the frozen verdict in CI over the whole log
    cblob = git(None, 'rev-parse', 'HEAD:' + RD + 'controls.py', cwd=wt).stdout.decode().strip()
    checks['controls.py at E is the frozen blob'] = cblob == CONTROLS_BLOB
    logpath = os.path.join(a.work, 'bridge-whole.log')
    open(logpath, 'wb').write(bbytes)
    if not os.path.exists(a.python):
        raise SystemExit('the verdict interpreter %s is absent' % a.python)
    vp = subprocess.run([a.python, '-I', '-B', os.path.join(wt, RD + 'controls.py'), 'verdict', E, '--freeze', F,
                         '--axioms', logpath], cwd=wt, capture_output=True, text=True,
                        env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    vout = vp.stdout.rstrip('\n').split('\n')
    tokens = {l.split()[1]: l.split()[2] for l in vout if l.startswith('TOKEN ')}
    rnd = next((l for l in vout if l.startswith('PRESERVE-INDUCT-1-')), None)
    checks['CI verdict over the whole log: exit 0, every cell positive, PRESERVE-INDUCT-1-READ'] = (
        vp.returncode == 0 and tokens == WANT_TOKENS and rnd == 'PRESERVE-INDUCT-1-READ')
    block = final_block(g, btext)
    checks['final bridge step block found once, marker names E'] = block is not None
    plines = probe_lines(g, ptext)
    checks['probe job lines read'] = bool(plines)
    pbytes = ptext.encode('utf-8')
    cells_ci = {
        'schema': 'oi-evidence-cells-ci', 'version': 1, 'round': 'PRESERVE-INDUCT-1', 'commit': E, 'form': 'derived',
        'expected': {'bridge_final_step_block': block, 'probe_job_lines': plines},
        'verdict_ci': {'controls_blob': cblob, 'python': subprocess.run([a.python, '--version'], capture_output=True, text=True).stdout.strip(),
                       'command': 'python3 -I -B controls.py verdict %s --freeze %s --axioms <whole bridge log, as downloaded>' % (E, F),
                       'exit': vp.returncode, 'stdout_lines': vout, 'stderr_lines': [l for l in vp.stderr.split('\n') if l],
                       'tokens': tokens, 'round': rnd, 'log_sha256': SHA(bbytes), 'log_lines': n,
                       'note': 'run in CI by the extraction workflow (run %s), in a worktree at E, over the whole bridge log as '
                               'downloaded (timestamps kept). Distinct from the verdict the session ran over the served window, '
                               'which the e-run record keeps as verdict_session' % ci_run},
        'source': {'bridge_log': {'job_id': BRIDGE_JOB, 'lines': n, 'sha256': SHA(bbytes), 'whole': True},
                   'probe_log': {'job_id': PROBE_JOB, 'lines': len(g['lines_of'](ptext)), 'sha256': SHA(pbytes), 'whole': True},
                   'extraction_run': {'run_id': ci_run, 'attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
                                      'commit': os.environ.get('GITHUB_SHA'), 'workflow': os.environ.get('GITHUB_WORKFLOW_REF')},
                   'stripped_lines': 'the lines recorded above have the leading timestamp removed (extract_result.py\'s form)'},
    }
    cdata = g['dumps'](cells_ci)
    checks['no secret pattern in cells-ci'] = not g['secret_hits'](cdata.decode())
    # session cross-check: the last tail_lines lines, joined, against what the session's tool served (never decisive)
    obs = t.get('session_observation')
    if obs:
        tail = '\n'.join(g['lines_of'](btext)[-obs['tail_lines']:])
        print('cross-check session window: original_lines %s vs %d; last %d lines sha256 %s vs session %s'
              % (obs['original_lines'], n, obs['tail_lines'], SHA(tail.encode('utf-8')), obs['tail_sha256']))
    token = secrets.token_hex(16)
    print('::stop-commands::%s' % token)
    emit_numbered('results.json', rdata)
    emit_numbered('cells-ci.json', cdata)
    print('::%s::' % token)
    print('summary reports %s gate %s %s/%s markers %s gaps %d' % (
        {k: len(v['reports']) for k, v in exp['modules'].items()}, exp['gate']['verdict'], exp['gate']['steps_pass'],
        exp['gate']['steps_total'], exp['markers'], len(gaps)))
    print('summary verdict_ci exit=%d tokens=%s round=%s' % (vp.returncode, json.dumps(tokens, sort_keys=True), rnd))
    verdict, code = decide(checks)
    for k, v in checks.items():
        print('check %s %s' % ({True: 'ok', False: 'FAIL', None: 'unmeasured'}[v], k))
    print('EXTRACT %s' % verdict)
    return code


def window_control(a):
    """Rebuild results.json from the served window exactly as the window builder did; compare with the committed file."""
    api, edir = a.api, a.expect
    os.chdir(a.repo)
    g = load_extractor(os.path.join(a.repo, '.git') if os.path.isdir(os.path.join(a.repo, '.git')) else None)
    prereg = blob(None, F, RD + 'preregistration.md').decode()
    r = json.load(open(os.path.join(api, 'run.json')))
    sv = json.load(open(os.path.join(api, 'bridge-served.json')))
    text = sv['logs_content']
    n_served, n_orig = len(g['lines_of'](text)), sv.get('original_length')
    first = n_orig - n_served + 1
    runinfo = {'mods': governed_mods(prereg),
               'run': {'id': str(r['id']), 'head_sha': E, 'event': r['event'], 'conclusion': r['conclusion'],
                       'attempt': r['run_attempt'], 'workflow': 'verify.yml', 'job_id': str(sv['job_id']), 'job_name': 'Mathlib bridge'}}
    source = {'kind': 'GitHub Actions job log, read through the session\'s job-log tool, which returns at most the last 5000 lines',
              'served_sha256': SHA(text.encode('utf-8')), 'served_lines': n_served, 'original_lines': n_orig}
    res, _ = build_results(g, text, runinfo, source,
                           'the served text is the last %d lines of the log; the reports and markers above are read from it alone'
                           % n_served, first, n_orig)
    data = g['dumps'](res)
    want = open(os.path.join(edir, 'results.json'), 'rb').read()
    same = data == want
    print('window control: results.json rebuilt %s (%d bytes) vs committed %s (%d bytes): %s'
          % (SHA(data)[:16], len(data), SHA(want)[:16], len(want), 'BYTE-IDENTICAL' if same else 'DIFFERENT'))
    cells = json.load(open(os.path.join(edir, 'cells.json')))
    ps = json.load(open(os.path.join(api, 'probe-served.json')))
    blk, pl = final_block(g, text), probe_lines(g, ps['logs_content'])
    b_ok = blk == cells['expected']['bridge_final_step_block']
    p_ok = pl == cells['expected']['probe_job_lines']
    print('window control: final-step block %s; probe lines %s' % ('identical' if b_ok else 'DIFFERENT', 'identical' if p_ok else 'DIFFERENT'))
    # the numbered print round-trips the committed bytes
    import io
    buf = io.StringIO()
    emit_numbered('results.json', want, buf)
    emit_numbered('cells.json', open(os.path.join(edir, 'cells.json'), 'rb').read(), buf)
    served = '\n'.join('2026-10-23T00:00:00.0000000Z ' + l for l in buf.getvalue().split('\n'))
    back = parse_numbered(served)
    rt = back['results.json'] == want and back['cells.json'] == open(os.path.join(edir, 'cells.json'), 'rb').read()
    print('window control: numbered print round-trips both committed files through a timestamped served log: %s' % rt)
    return 0 if same and b_ok and p_ok and rt else 1


def self_test():
    fails = 0

    def case(name, ok):
        nonlocal fails
        fails += not ok
        print('  %s  %s' % ('ok  ' if ok else 'FAIL', name))
    import io
    data = json.dumps({'a': '##[error] x', 'b': 'π #print axioms', 'c': ['\\u0023 literal?'], 'd': '\\#\\\\#'}, indent=1).encode() + b'\n'
    buf = io.StringIO()
    emit_numbered('x.json', data, buf)
    printed = buf.getvalue()
    case('no printed line carries a raw #', '#' not in printed)
    served = '\n'.join('\ufeff2026-10-23T10:00:00.1234567Z ' + l if i == 0 else '2026-10-23T10:00:00.1234567Z ' + l
                       for i, l in enumerate(printed.split('\n')))
    try:
        got = parse_numbered(served)['x.json']
        case('a numbered result round-trips through a timestamped served log', got == data)
    except ValueError:
        case('a numbered result round-trips through a timestamped served log', False)
    lines = printed.split('\n')
    cut = '\n'.join(lines[:2] + lines[3:])
    try:
        parse_numbered(cut)
        case('a missing numbered line is refused', False)
    except ValueError:
        case('a missing numbered line is refused', True)
    tampered = printed.replace('"a"', '"z"', 1)
    try:
        parse_numbered(tampered)
        case('an altered line fails the digest check', False)
    except ValueError:
        case('an altered line fails the digest check', True)
    case('decide: all True holds', decide({'a': True, 'b': True}) == ('HOLDS', 0))
    case('decide: any None is unverified', decide({'a': True, 'b': None}) == ('UNVERIFIED', 2))
    case('decide: any False fails, even with None', decide({'a': False, 'b': None}) == ('FAILS', 1))
    case('governed modules parse from a v3-governed-paths block',
         governed_mods('x\n```v3-governed-paths\nexecution A verification/lean-mathlib/OIBridge/X.lean\n'
                       'execution M verification/lean-mathlib/OIBridge.lean\nrecord AM a/\n```\n') == ['OIBridge.lean', 'OIBridge/X.lean'])
    g = {'lines_of': lambda t: t[:-1].split('\n') if t.endswith('\n') else t.split('\n')}
    blk = final_block(g, 'a\n2026-10-23T10:51:18.06Z preserve_induct1 axioms: step at %s\nr1\n'
                         '2026-10-23T10:51:24.5Z preserve_induct1 axioms: OK -- 10 reports\nz\n' % E)
    case('the final-step block is read with timestamps stripped and names E', blk is not None and blk[0].endswith(E) and len(blk) == 3)
    case('a block naming another commit is refused',
         final_block(g, 'preserve_induct1 axioms: step at %s\npreserve_induct1 axioms: OK -- 10 reports\n' % ('0' * 40)) is None)
    case('two marker lines are refused', final_block(g, ('preserve_induct1 axioms: step at %s\n' % E) * 2
                                                     + 'preserve_induct1 axioms: OK -- 10 reports\n') is None)
    print('assemble self-test: %d failure(s)' % fails)
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for k in ('--objects', '--history', '--host', '--logs', '--download-record', '--work', '--repo', '--api', '--expect'):
        ap.add_argument(k)
    ap.add_argument('--python', default=sys.executable)
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--window-control', action='store_true')
    a = ap.parse_args(argv)
    if a.self_test:
        return 1 if self_test() else 0
    if a.window_control:
        return window_control(a)
    for k in ('objects', 'history', 'host', 'logs', 'download_record', 'work'):
        if not getattr(a, k):
            ap.error('--%s is required' % k.replace('_', '-'))
    try:
        return ci(a)
    except SystemExit as e:   # a missing or mismatched source: say so and end on the verdict line
        print('assembly stopped: %s' % e)
        print('EXTRACT UNVERIFIED')
        return 2


if __name__ == '__main__':
    sys.exit(main())
