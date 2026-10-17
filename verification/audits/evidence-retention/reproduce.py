#!/usr/bin/env python3
"""reproduce.py -- reproduces one archived expected result at its attested commit, and fails closed.

    python3 -I verification/audits/evidence-retention/reproduce.py --run RUN_ID --work DIR
    python3 -I verification/audits/evidence-retention/reproduce.py --run RUN_ID --work DIR \\
        --override-sha SHA --expect-scientific-mismatch [--expect-failure TEXT ...]

A flag that takes a value takes it as the next argument or after '=' (--expect-failure=TEXT): the two forms are
parsed identically and give the same verdict.

Run from the repository root of a clone with full history and a Lean toolchain manager (elan) on PATH. The
verifier is this checkout: the manifest and results.json read here, and extract_result.py and compare_result.py
beside this file. The historical commit supplies only its sources, its toolchain pin and its own
tools/release_gate.py. The steps:
  1. validate the arguments: each a known flag or a flag's value, no value missing, empty or whitespace-only, no
     flag but --expect-failure given twice, RUN_ID decimal, SHA a full 40-hex commit id;
  2. find the entry ci-RUN_ID and its results.json; record the verifier commit;
  3. check that the commit to build is in the repository (a shallow clone fails here);
  4. check it out as a detached worktree under DIR;
  5. in its verification/lean-mathlib: `lean --version`, `lake exe cache get`, `lake --rehash build`; then, at its
     root, `python3 tools/release_gate.py`; everything captured to DIR/build-and-gate.log;
  6. extract the structured result from the captured output (DIR/reproduced.json);
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
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
from extract_result import extract  # noqa: E402
from compare_result import compare  # noqa: E402

RUN_ID = re.compile(r'^[0-9]{1,20}$')
SHA = re.compile(r'^[0-9a-f]{40}$')
VALUED = ('--run', '--work', '--override-sha', '--expect-failure')
SWITCHES = ('--expect-scientific-mismatch',)
EMPTY_TEXT = '--expect-failure needs a non-empty text: the empty text is contained in every failure, so it expects nothing'


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
    """Strict arguments: each is a known flag, or the value of one, given as the next argument or after '='.
    Returns ({flag: value}, problems), with --expect-failure's values as a list; any problem rejects the arguments.
    The next argument is never taken as a value when it is itself a flag, so a flag without a value is a problem."""
    flag = lambda x: x.partition('=')[0] in VALUED + SWITCHES
    opts, problems, i = {'--expect-failure': []}, [], 0
    while i < len(a):
        tok = a[i]
        name, eq, val = tok.partition('=')
        i += 1
        if name in SWITCHES:
            if eq:
                problems.append('%s takes no value' % name)
            elif name in opts:
                problems.append('%s is given twice' % name)
            opts[name] = True
            continue
        if name not in VALUED:
            problems.append('%r is not an argument of this tool' % tok)
            continue
        if not eq:
            if i >= len(a) or flag(a[i]):
                problems.append('%s needs a value' % name)
                continue
            val, i = a[i], i + 1
        if not val.strip():
            problems.append(EMPTY_TEXT if name == '--expect-failure' else '%s needs a non-empty value' % name)
        elif name == '--expect-failure':
            opts[name].append(val)
        elif name in opts:
            problems.append('%s is given twice' % name)
        else:
            opts[name] = val
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
    rp = next((f['path'] for f in ent['files'] if f['path'].endswith('/results.json')), None)
    if rp is None:
        out('FAIL  entry ci-%s has no results.json' % run_id)
        return finish(False, 'no results.json')
    expected = json.load(open(os.path.join(HERE, rp), encoding='utf-8'))
    if expected.get('kind') != 'bridge':
        out('FAIL  results of kind %r are not reproduced by this tool' % expected.get('kind'))
        return finish(False, 'kind')
    attested = expected['run']['head_sha']
    sha = override or attested
    verifier = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    record.update(expected_head=attested, built=sha, verifier=verifier)
    out('REPRODUCE  run %s: expected result at %s; verifier at %s%s' % (
        run_id, attested[:12], verifier[:12], '; NEGATIVE CONTROL built at %s' % sha[:12] if negative else ''))
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


if __name__ == '__main__':
    sys.exit(main())
