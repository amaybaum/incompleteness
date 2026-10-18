#!/usr/bin/env python3
"""reproduce.py -- reproduces one archived expected result at its attested commit, and fails closed.

    python3 -I verification/audits/evidence-retention/reproduce.py --run RUN_ID --work DIR
    python3 -I verification/audits/evidence-retention/reproduce.py --run RUN_ID --work DIR \\
        --override-sha SHA --expect-scientific-mismatch [--expect-failure TEXT ...]

A flag that takes a value takes it as the next argument or after '=' (--expect-failure=TEXT): the two forms are
parsed identically and give the same verdict.

    python3 -I verification/audits/evidence-retention/reproduce.py --self-test     # needs history

Run from the repository root of a clone with full history and a Lean toolchain manager (elan) on PATH. The
verifier is this checkout: the manifest and results.json read here, and compare_result.py beside this file. The
extractor is the version the expected result names (its manifest file's extractor_blob, or the manifest's
extractor_blobs map), read from the repository's objects (its history, or retained objects materialized into it), never the checkout's
extract_result.py, which a later change or pin may have moved. The historical commit supplies only its sources,
its toolchain pin and its own tools/release_gate.py. The steps:
  1. validate the arguments: each a known flag or a flag's value, no value missing, empty or whitespace-only, no
     flag but --expect-failure given twice, RUN_ID decimal, SHA a full 40-hex commit id;
  2. find the entry ci-RUN_ID and its results.json; load the extractor blob the result names, which must be an
     object of the repository and define extract(); record it and the verifier commit;
  3. check that the commit to build is in the repository (a shallow clone fails here);
  4. check it out as a detached worktree under DIR;
  5. in its verification/lean-mathlib: `lean --version`, `lake exe cache get`, `lake --rehash build`; then, at its
     root, `python3 tools/release_gate.py`; everything captured to DIR/build-and-gate.log;
  6. extract the structured result from the captured output with that extractor (DIR/reproduced.json);
  7. compare it with the expected result (compare_result.py), reading each governed module's #print axioms
     lines from its source at the built commit; write DIR/verdict.json and DIR/verdict.txt.
Reproduction holds, and the exit code is 0, only if every command succeeded and the comparison found nothing.

DIR/verdict.json is written on every exit path once --work names a directory that can be written: a rejected
argument, a missing entry, a failed checkout, and an exception raised by any step, extraction and comparison
included. Its 'holds' is true only with exit code 0. A stop records its reason under 'stopped'; rejected
arguments list each problem under 'argument_problems'; an exception records its type and message under 'stopped'
({"exception": TYPE, "message": MESSAGE}), and the exit code is 1. Without a --work value the usage text is
printed, no verdict is written, and the exit code is 2; if the verdict cannot be written, the exit code is
nonzero.

Negative controls (--override-sha with --expect-scientific-mismatch) build another commit against the same
expected result. They pass only if the build and the gate ran to completion and passed there, so that the
failure cannot be an infrastructure or build failure, and the comparison then failed on scientific results
alone (rules C2-C4, never C1), including each --expect-failure text. Anything else fails the control. An empty
or whitespace-only --expect-failure, in either form, or one given without a value, is rejected: the empty text
is contained in every failure, so it would expect nothing. So is an unknown argument, such as --expect-failures,
which would otherwise drop the expectation it was meant to state.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
from compare_result import compare  # noqa: E402

RUN_ID = re.compile(r'^[0-9]{1,20}$')
SHA = re.compile(r'^[0-9a-f]{40}$')
VALUED = ('--run', '--work', '--override-sha', '--expect-failure')
SWITCHES = ('--expect-scientific-mismatch',)
EXTRACTOR = 'verification/audits/evidence-retention/extract_result.py'
HEX40 = re.compile(r'^[0-9a-f]{40}$')
EMPTY_TEXT = '--expect-failure needs a non-empty text: the empty text is contained in every failure, so it expects nothing'


def named_blob(man, file_entry):
    """The extractor blob an expected result names: its manifest file's extractor_blob, else the manifest's
    extractor_blobs map's (as check_retention.py R15 reads it). Returns (blob, problem)."""
    own, mapped = file_entry.get('extractor_blob'), (man.get('extractor_blobs') or {}).get(file_entry.get('path'))
    if own is not None and mapped is not None and own != mapped:
        return None, 'the expected result names two extractor blobs, %s and %s' % (str(own)[:12], str(mapped)[:12])
    b = own if own is not None else mapped
    if not (isinstance(b, str) and HEX40.match(b)):
        return None, 'the expected result names no extractor blob'
    return b, None


def named_extractor(man, file_entry, root=ROOT):
    """The extract() of the extractor an expected result names, read from the repository's objects and never from
    the checkout. Returns (extract, blob, problem); problem is None on success."""
    b, why = named_blob(man, file_entry)
    if why:
        return None, b, why
    p = subprocess.run(['git', 'cat-file', 'blob', b], cwd=root, capture_output=True)
    if p.returncode != 0:
        return None, b, 'extractor blob %s is not in this repository (its history or retained objects)' % b[:12]
    data = p.stdout  # git cat-file returns exactly the object named b
    ns = {'__name__': 'extract_result_%s' % b[:12]}
    try:
        exec(compile(data, '%s@%s' % (EXTRACTOR, b[:12]), 'exec'), ns)
    except Exception as exc:  # a blob that is not Python, or fails on load
        return None, b, 'extractor blob %s does not load: %s: %s' % (b[:12], type(exc).__name__, exc)
    if not callable(ns.get('extract')):
        return None, b, 'extractor blob %s defines no extract()' % b[:12]
    return ns['extract'], b, None


def sh(args, cwd, log):
    log.write('\n$ %s   (cwd %s)\n' % (' '.join(args), os.path.relpath(cwd, ROOT)))
    log.flush()
    try:
        rc = subprocess.run(args, cwd=cwd, stdout=log, stderr=subprocess.STDOUT).returncode
    except OSError as exc:
        log.write('could not run: %s\n' % exc)
        rc = 127
    log.write('\n[exit %d]\n' % rc)
    log.flush()
    return rc


def parse(a):
    """Strict arguments: each is a known flag, or the value of one. Before anything else is read, every argument
    FLAG=VALUE, for a flag that takes a value, becomes the two arguments FLAG VALUE, and VALUE is read the same way,
    so the two forms are one token stream: the same values, the same problems, the same verdict. Returns
    ({flag: value}, problems), with --expect-failure's values as a list; any problem rejects the arguments. The
    next argument is never taken as a value when it is itself a flag, so a flag without a value is a problem."""
    flag = lambda x: x.partition('=')[0] in VALUED + SWITCHES
    toks = []
    for x in a:
        name, eq, val = x.partition('=')
        while eq and name in VALUED:
            toks.append(name)
            x = val
            name, eq, val = x.partition('=')
        toks.append(x)
    opts, problems, i = {'--expect-failure': []}, [], 0
    while i < len(toks):
        tok = toks[i]
        name = tok.partition('=')[0]
        i += 1
        if name in SWITCHES:
            if tok != name:
                problems.append('%s takes no value' % name)
            elif name in opts:
                problems.append('%s is given twice' % name)
            opts[name] = True
            continue
        if tok not in VALUED:
            problems.append('%r is not an argument of this tool' % tok)
            continue
        if i >= len(toks) or flag(toks[i]):
            problems.append('%s needs a value' % tok)
            continue
        val, i = toks[i], i + 1
        if not val.strip():
            problems.append(EMPTY_TEXT if tok == '--expect-failure' else '%s needs a non-empty value' % tok)
        elif tok == '--expect-failure':
            opts[tok].append(val)
        elif tok in opts:
            problems.append('%s is given twice' % tok)
        else:
            opts[tok] = val
    return opts, problems


def main():
    opts, problems = parse(sys.argv[1:])
    run_id, work, override = opts.get('--run'), opts.get('--work'), opts.get('--override-sha')
    negative, expect = opts.get('--expect-scientific-mismatch', False), opts['--expect-failure']
    if not work:
        # the one exit that writes no verdict: there is no directory to hold it
        for p_ in problems:
            print('FAIL  %s' % p_)
        print(__doc__)
        return 2
    work = os.path.abspath(work)
    record = {'run_id': run_id, 'negative_control': negative, 'expect_failures': expect, 'commands': [], 'failures': []}
    txt = []

    def out(msg):
        print(msg)
        try:
            if txt:
                txt[0].write(msg + '\n')
                txt[0].flush()
        except (OSError, ValueError):
            pass

    def finish(ok, why=None, code=1):
        """Writes verdict.json; the exit code is 0 only if the reproduction holds and its verdict was written."""
        record['holds'] = ok
        if why:
            record['stopped'] = why
        try:
            text = json.dumps(record, indent=1, sort_keys=True)
        except (TypeError, ValueError) as exc:
            ok = False
            text = json.dumps({'run_id': str(run_id), 'holds': False,
                               'stopped': {'exception': type(exc).__name__, 'message': str(exc)}}, indent=1, sort_keys=True)
        try:
            with open(os.path.join(work, 'verdict.json'), 'w', encoding='utf-8') as fh:
                fh.write(text)
        except OSError as exc:
            print('FAIL  could not write %s: %s' % (os.path.join(work, 'verdict.json'), exc))
            return code
        return 0 if ok else code

    try:
        os.makedirs(work, exist_ok=True)
        txt.append(open(os.path.join(work, 'verdict.txt'), 'w', encoding='utf-8'))
        return reproduce(problems, run_id, work, override, negative, expect, record, out, finish)
    except (Exception, KeyboardInterrupt) as exc:
        out('FAIL  stopped by %s: %s' % (type(exc).__name__, exc))
        return finish(False, {'exception': type(exc).__name__, 'message': str(exc)})
    finally:
        if txt:
            txt[0].close()


def reproduce(problems, run_id, work, override, negative, expect, record, out, finish):
    """The steps of the docstring, from parse()'s problems and values; every return goes through finish, which
    writes verdict.json."""
    problems = list(problems)
    if not run_id:
        if not problems:
            out('FAIL  --run is required')
            print(__doc__)
            return finish(False, 'usage', code=2)
        problems.append('--run is required')
    elif not RUN_ID.match(run_id):
        problems.append('--run must be a decimal run id, got %r' % run_id)
    if override is not None and not SHA.match(override):
        problems.append('--override-sha must be a full 40-hex commit id, got %r' % override)
    if negative != (override is not None):
        problems.append('--override-sha and --expect-scientific-mismatch go together: a control at another commit must '
                        'state that it expects a scientific mismatch, and only such a control may expect one')
    if expect and not negative:
        problems.append('--expect-failure needs --expect-scientific-mismatch')
    if problems:
        for p_ in problems:
            out('FAIL  %s' % p_)
        record['argument_problems'] = problems
        return finish(False, 'arguments')
    man = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
    ent = next((e for e in man['entries'] if e.get('id') == 'ci-' + run_id), None)
    if ent is None:
        out('FAIL  no entry ci-%s in the manifest' % run_id)
        return finish(False, 'no entry')
    fe = next((f for f in ent['files'] if f['path'].endswith('/results.json')), None)
    if fe is None:
        out('FAIL  entry ci-%s has no results.json' % run_id)
        return finish(False, 'no results.json')
    rp = fe['path']
    extract, xblob, xproblem = named_extractor(man, fe)
    record['extractor_blob'] = xblob
    if xproblem:
        out('FAIL  %s' % xproblem)
        return finish(False, 'extractor')
    expected = json.load(open(os.path.join(HERE, rp), encoding='utf-8'))
    if expected.get('kind') != 'bridge':
        out('FAIL  results of kind %r are not reproduced by this tool' % expected.get('kind'))
        return finish(False, 'kind')
    attested = expected['run']['head_sha']
    sha = override or attested
    verifier = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    record.update(expected_head=attested, built=sha, verifier=verifier)
    out('REPRODUCE  run %s: expected result at %s; verifier at %s; extractor blob %s%s' % (
        run_id, attested[:12], verifier[:12], xblob[:12], '; NEGATIVE CONTROL built at %s' % sha[:12] if negative else ''))
    if subprocess.run(['git', 'cat-file', '-e', sha + '^{commit}'], cwd=ROOT).returncode != 0:
        out('FAIL  commit %s is not in this repository (shallow clone, or the commit is not retained)' % sha)
        return finish(False, 'commit not in repository')
    tree = os.path.join(work, 'tree')
    log = open(os.path.join(work, 'build-and-gate.log'), 'w', encoding='utf-8', errors='replace')
    try:
        if sh(['git', 'worktree', 'add', '--detach', tree, sha], ROOT, log) != 0:
            out('FAIL  could not check out %s' % sha)
            return finish(False, 'checkout')
        at = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tree, capture_output=True, text=True).stdout.strip()
        if at != sha:
            out('FAIL  the worktree is at %s, not %s' % (at[:12], sha[:12]))
            return finish(False, 'checkout')
        lean = os.path.join(tree, 'verification', 'lean-mathlib')
        t0 = time.time()
        for args, cwd in ((['lean', '--version'], lean), (['lake', 'exe', 'cache', 'get'], lean),
                          (['lake', '--rehash', 'build'], lean), ([sys.executable, 'tools/release_gate.py'], tree)):
            rc = sh(args, cwd, log)
            record['commands'].append({'command': ' '.join(args), 'exit': rc})
            if rc != 0:
                out('FAIL  `%s` exited %d' % (' '.join(args), rc))
        log.write('\nTIMING reproduce-build-and-gate %ds\n' % (time.time() - t0))
    finally:
        log.close()
        subprocess.run(['git', 'worktree', 'remove', '--force', tree], cwd=ROOT, capture_output=True)
    rep = extract(open(os.path.join(work, 'build-and-gate.log'), encoding='utf-8', errors='replace').read())
    json.dump(rep, open(os.path.join(work, 'reproduced.json'), 'w'), indent=1, sort_keys=True)

    def source(mod):
        p = subprocess.run(['git', 'show', '%s:verification/lean-mathlib/%s' % (sha, mod)], cwd=ROOT, capture_output=True)
        return p.stdout.decode('utf-8') if p.returncode == 0 else None

    fails = compare(expected, rep, source)
    commands_ok = len(record['commands']) == 4 and all(c['exit'] == 0 for c in record['commands'])
    built_ok = bool(rep.get('build') and rep['build'].get('success'))
    gate_ok = bool(rep.get('gate') and rep['gate'].get('verdict') and rep['gate']['verdict'].get('pass'))
    record.update(failures=fails, commands_ok=commands_ok, build_success=built_ok, gate_pass=gate_ok)
    for f in fails:
        out('FAIL  %s' % f)
    if not negative:
        ok = commands_ok and not fails
        out('REPRODUCTION  %s (%d comparison failure(s), commands %s) for run %s at %s, verifier %s' % (
            'HOLDS' if ok else 'FAILS', len(fails), 'ok' if commands_ok else 'FAILED', run_id, sha[:12], verifier[:12]))
        return finish(ok)
    # a negative control: the failure must be scientific, after a complete and passing build and gate
    problems = []
    if not commands_ok:
        problems.append('a command failed, so the mismatch could be an infrastructure or build failure')
    if not built_ok or not gate_ok:
        problems.append('the build or the gate did not pass at the built commit')
    if not fails:
        problems.append('the comparison found no mismatch: the control did not discriminate')
    if any(not f.startswith(('C2 ', 'C3 ', 'C4 ')) for f in fails):
        problems.append('a failure is not scientific (only C2-C4 are): %s' % [f for f in fails if not f.startswith(('C2 ', 'C3 ', 'C4 '))])
    for t in expect:
        if not any(t in f for f in fails):
            problems.append('no failure contains the expected text %r' % t)
    for p_ in problems:
        out('CONTROL-FAIL  %s' % p_)
    record['control_problems'] = problems
    ok = not problems
    out('NEGATIVE-CONTROL  %s (%d comparison failure(s), %s) for run %s built at %s, verifier %s' % (
        'HOLDS' if ok else 'FAILS', len(fails), 'all scientific' if fails and all(f.startswith(('C2 ', 'C3 ', 'C4 ')) for f in fails)
        else 'not all scientific', run_id, sha[:12], verifier[:12]))
    return finish(ok)


def self_test():
    """The extractor a reproduction runs is the one each expected result names, not the checkout's."""
    man = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
    ok = True

    def case(name, good, detail=''):
        nonlocal ok
        ok &= bool(good)
        print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if good or not detail else '\n      %s' % detail))

    def blob(data):
        return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()
    current = blob(open(os.path.join(HERE, 'extract_result.py'), 'rb').read())
    ci = [(e, next(f for f in e['files'] if f['path'].endswith('/results.json'))) for e in man['entries']
          if str(e.get('id', '')).startswith('ci-') and any(f['path'].endswith('/results.json') for f in e['files'])]
    loaded, bad = {}, []
    for e, fe in ci:
        b = named_blob(man, fe)[0]
        if b not in loaded:
            loaded[b] = named_extractor(man, fe)
        if loaded[b][2] or loaded[b][1] != b:
            bad.append((e['id'], loaded[b][2]))
    case('each of the %d CI expected results loads the extractor blob it names' % len(ci), ci and not bad, bad[:3])
    # a primed report: the extractor before fdf3ec80 does not read it, the later one does, so the outcome shows
    # which version ran
    probe = "info: OIBridge/Probe.lean:1:0: 'OIBridge.Probe.p'' depends on axioms: [propext]"
    sys.path.insert(0, HERE)
    import extract_result as checkout
    differ = [(e['id'], fe) for e, fe in ci if named_blob(man, fe)[0] != current]
    if differ:
        eid, fe = differ[0]
        ex, b, _ = named_extractor(man, fe)
        case('%s names %s, not the checkout\'s %s, and its reproduction runs the named one' % (eid, str(b)[:12], current[:12]),
             ex is not None and ex(probe)['reports'] != checkout.extract(probe)['reports'], 'the probe reads alike')
    else:
        case('every CI expected result names the checkout\'s extractor %s' % current[:12], True)
    tail = open(os.path.join(HERE, 'bg3', 'bridge-116826161407-tail.log'), encoding='utf-8').read()
    e38 = next(((e, fe) for e, fe in ci if e['id'] == 'ci-38855576525'), None)
    if e38 is None:
        case('ci-38855576525 is in the manifest', False)
    else:
        res = json.load(open(os.path.join(HERE, e38[1]['path']), encoding='utf-8'))
        ex, _, prob = named_extractor(man, e38[1])
        x = ex(tail) if ex else {'reports': {}, 'markers': {}, 'gate': None}
        mods = res['expected']['modules']
        case('ci-38855576525\'s named extractor reads its retained log as the expected result records it',
             not prob and {m: [{'line': r['line'], 'name': r['name'], 'axioms': r['axioms']} for r in x['reports'].get(m, [])] for m in mods}
             == {m: em['reports'] for m, em in mods.items()} and x['markers'] == res['expected']['markers']
             and sum(len(v) for v in x['reports'].values()) == res['observed']['reports_in_served_text']
             and (x['gate'] or {}).get('verdict', {}).get('text') == res['expected']['gate']['verdict'], prob)
    fe0 = ci[0][1] if ci else {}
    at_head = lambda f: subprocess.run(['git', 'rev-parse', 'HEAD:verification/audits/evidence-retention/' + f], cwd=ROOT,
                                       capture_output=True, text=True).stdout.strip()
    for name, b, msg in (('a result naming no extractor blob', None, 'names no extractor blob'),
                         ('a result naming one blob in its file and another in extractor_blobs', 'b' * 40, 'two extractor blobs'),
                         ('a result naming a malformed blob', 'x' * 40, 'names no extractor blob'),
                         ('a named blob absent from the repository', '0' * 40, 'not in this repository'),
                         ('a named blob that is not Python (the README)', at_head('README.md'), 'does not load'),
                         ('a named blob that defines no extract() (the comparator)', at_head('compare_result.py'), 'defines no extract()')):
        # a path the map does not name, except where the case is the disagreement with the map
        fx = {k: v for k, v in fe0.items() if k != 'extractor_blob'}
        if msg != 'two extractor blobs':
            fx['path'] = 'ci/0/results.json'
        if b is not None:
            fx['extractor_blob'] = b
        r = named_extractor(man, fx)
        case('%s fails closed' % name, r[0] is None and r[2] and msg in r[2], r[2])
    print('reproduce self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if sys.argv[1:] == ['--self-test']:
        sys.exit(self_test())
    sys.exit(main())
