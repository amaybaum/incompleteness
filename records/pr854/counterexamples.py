#!/usr/bin/env python3
"""Independent replay of #854's review counterexamples; no Lean certification.

Archive probes run the real history checks on copied archive bytes. CLI probes
run main() and write its real verdict.json, with declared stand-ins for the
toolchain, extractor and comparator. Those probes test argument/exit handling;
real positive and negative Lean reproductions are still required in CI.
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import types

ROOT = (Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else
        Path(__file__).resolve().parent / 'incompleteness')
ARCHIVE = ROOT / 'verification/audits/evidence-retention'
BASE = '6bf56dc4500770b6c32bc584b32d2198a1916215'
MID = '915ca926ee7d5b17a35001362ca6800c938d3789'
HEAD = 'e3a44e63ebec41fccd109cf1ca945b3b8a200553'
EXPECTED = '194eb3fd0c0a0000000000000000000000000000'
BUILT = '777ddf8dcada759b5f3bcab26a4ff3833ba720bf'
checks = []


def require(name, condition, details=None):
    checks.append({'name': name, 'pass': bool(condition), 'details': details})
    print(('PASS ' if condition else 'FAIL ') + name, flush=True)


def load_at(filename, commit):
    rel = 'verification/audits/evidence-retention/' + filename
    src = subprocess.check_output(['git', 'show', commit + ':' + rel], cwd=ROOT)
    module = types.ModuleType(filename[:-3] + '_' + commit[:8])
    module.__file__ = str(ROOT / rel)
    exec(compile(src, module.__file__, 'exec'), module.__dict__)
    return module


def cli_run(module, args, failures=('C3 required-report missing',), exception=False):
    """Actual main/finish/negative-control logic; external build work is mocked."""
    with tempfile.TemporaryDirectory(prefix='r854-cli-') as td:
        td = Path(td)
        fixture, work = td / 'fixture', td / 'work'
        fixture.mkdir()
        (fixture / 'manifest.json').write_text(json.dumps({'entries': [
            {'id': 'ci-1', 'files': [{'path': 'fixture/results.json'}]}]}))
        (fixture / 'fixture').mkdir()
        (fixture / 'fixture/results.json').write_text(json.dumps({
            'kind': 'bridge', 'run': {'head_sha': EXPECTED}}))
        original = (module.HERE, module.ROOT, module.sh, module.extract,
                    module.compare, module.subprocess.run, sys.argv)

        def fake_git(argv, **kwargs):
            at = BUILT if kwargs.get('cwd') == str(work / 'tree') else HEAD
            return subprocess.CompletedProcess(argv, 0, stdout=at + '\n', stderr='')

        def fake_compare(*args):
            if exception:
                raise RuntimeError('deliberate-comparator-exception')
            return list(failures)

        try:
            module.HERE, module.ROOT = str(fixture), str(ROOT)
            module.sh = lambda *args: 0
            module.extract = lambda text: {'build': {'success': True},
                                          'gate': {'verdict': {'pass': True}}}
            module.compare = fake_compare
            module.subprocess.run = fake_git
            sys.argv = [module.__file__, '--run', '1', '--work', str(work)] + args
            with contextlib.redirect_stdout(io.StringIO()):
                code = module.main()
            vp = work / 'verdict.json'
            verdict = json.loads(vp.read_text()) if vp.exists() else None
            return code, verdict
        finally:
            (module.HERE, module.ROOT, module.sh, module.extract,
             module.compare, module.subprocess.run, sys.argv) = original


def reclassify(archive, relative):
    mp = archive / 'manifest.json'
    man = json.loads(mp.read_text())
    path = archive / relative
    result = json.loads(path.read_text())
    result['kind'] = 'design-diagnostic'
    result['expected']['sha256sum_ok'] = True
    result['expected']['checks'] = ['review-counterexample']
    data = (json.dumps(result, indent=1, sort_keys=True) + '\n').encode()
    path.write_bytes(data)
    for entry in man['entries']:
        for file in entry['files']:
            if file['path'] == relative:
                file['bytes'], file['sha256'] = len(data), hashlib.sha256(data).hexdigest()
    mp.write_text(json.dumps(man, indent=1, sort_keys=True) + '\n')
    return man


def history_checks(module, archive, man):
    """The checks invoked by --gate, excluding its separately run self-test."""
    if hasattr(module, 'history_mode'):
        return module.history_mode(str(archive), str(ROOT), man)[0]
    scope, failures = module.base_scope(man, str(ROOT))
    if scope is not None:
        failures += module.check(str(archive), str(ROOT), scope)[0]
        failures += module.later_provenance(man, str(ROOT))
        failures += module.module_sets(str(archive), str(ROOT), man)[0]
    return failures


current = load_at('reproduce.py', HEAD)
old = load_at('reproduce.py', BASE)
middle = load_at('reproduce.py', MID)
negative = ['--override-sha', BUILT, '--expect-scientific-mismatch']

code, verdict = cli_run(old, negative + ['--expect-failure=NEVER-MATCHES'])
require('old checkpoint demonstrates silently ignored joined expectation',
        code == 0 and verdict['holds'] is True and verdict['expect_failures'] == [])
for form in [['--expect-failure', 'NEVER-MATCHES'], ['--expect-failure=NEVER-MATCHES']]:
    code, verdict = cli_run(current, negative + form)
    require('current rejects unmatched expectation ' + repr(form),
            code != 0 and verdict['holds'] is False and
            any('NEVER-MATCHES' in p for p in verdict.get('control_problems', [])))
for form in [['--expect-failure', 'required-report'], ['--expect-failure=required-report']]:
    code, verdict = cli_run(current, negative + form)
    require('current accepts a matched expectation ' + repr(form),
            code == 0 and verdict['holds'] is True and verdict['expect_failures'] == ['required-report'])

old_space = cli_run(middle, negative + ['--expect-failure', '--run'])[1]
old_joined = cli_run(middle, negative + ['--expect-failure=--run'])[1]
require('915ca926 demonstrates different flag-shaped-value verdicts', old_space != old_joined)
new_space = cli_run(current, negative + ['--expect-failure', '--run'])
new_joined = cli_run(current, negative + ['--expect-failure=--run'])
require('current flag-shaped-value forms give identical rejected verdicts',
        new_space == new_joined and new_space[0] != 0 and new_space[1]['stopped'] == 'arguments')

values = ['', ' ', '\t', '1', BUILT, 'plain text', 'a=b', '--work', '--work=xyz',
          '--run', '--run=1', '--expect-failure', '--expect-failure=abc',
          '--override-sha=' + BUILT, '--expect-scientific-mismatch',
          '--expect-scientific-mismatch=yes', '--unknown']
for flag in current.VALUED:
    same = all(current.parse([flag, value]) == current.parse([flag + '=' + value]) for value in values)
    require('all split/joined parse cases agree for ' + flag, same, {'pairs': len(values)})

invalid = [
    ['--unknown'], ['--expect-failures', 'required-report'],
    ['--expect-failure'], ['--expect-failure', ''], ['--expect-failure='],
    ['--expect-failure', '  '], ['--expect-failure=  '],
    ['--run', '2'], ['--override-sha', BUILT, '--override-sha', BUILT],
    ['--expect-scientific-mismatch=yes'],
]
for args in invalid:
    code, verdict = cli_run(current, negative + args)
    require('argument failure writes a false verdict: ' + repr(args),
            code != 0 and verdict is not None and verdict['holds'] is False and
            verdict.get('stopped') == 'arguments' and bool(verdict.get('argument_problems')))
code, verdict = cli_run(current, negative + ['--expect-failure', 'required-report'], exception=True)
require('a comparator exception writes a false verdict and its cause',
        code != 0 and verdict['holds'] is False and
        verdict.get('stopped') == {'exception': 'RuntimeError', 'message': 'deliberate-comparator-exception'})

checker = load_at('check_retention.py', HEAD)
old_checker = load_at('check_retention.py', BASE)
manifest = json.loads((ARCHIVE / 'manifest.json').read_text())
failures, stats = checker.module_sets(str(ARCHIVE), str(ROOT), manifest)
require('unmodified R11 checks 97 results, 96 runs, 165 modules, 3 exclusions',
        not failures and (stats['checked'], stats['runs'], stats['modules'], len(stats['unscoped'])) == (97, 96, 165, 3),
        stats)

for label, relative in [
    ('CI result', 'ci/38855576525/results.json'),
    ('BG-3 E tail', next(f['path'] for e in manifest['entries'] for f in e['files']
                       if f['path'].startswith('bg3/results-') and
                       json.loads((ARCHIVE / f['path']).read_text())['run']['id'] == '38855576525')),
]:
    with tempfile.TemporaryDirectory(prefix='r854-archive-') as td:
        copy = Path(td) / 'archive'
        shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns('__pycache__'))
        modified = reclassify(copy, relative)
        before = history_checks(old_checker, copy, modified)
        after = history_checks(checker, copy, modified)
        require('old checkpoint demonstrates the ' + label + ' relabel bypass', not before, before)
        require('current rejects the ' + label + ' relabel after size/digest repair',
                bool(after) and any(f.startswith('R11 ') for f in after) and
                all(f.startswith(('R8 ', 'R11 ')) for f in after), after)

with tempfile.TemporaryDirectory(prefix='r854-drop-') as td:
    copy = Path(td) / 'archive'
    shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns('__pycache__'))
    man = json.loads((copy / 'manifest.json').read_text())
    entry = next(e for e in man['entries'] if e.get('id', '').startswith('ci-') and
                 e.get('run_id') != '38855576525')
    run = entry['run_id']
    entry['files'] = [f for f in entry['files'] if not f['path'].endswith('/results.json')]
    failures, st = checker.module_sets(str(copy), str(ROOT), man)
    require('dropping a required result fails attested-versus-checked set equality',
            any('are not the runs attested' in f and run in f for f in failures), failures)

out = Path(__file__).with_suffix('.results.json')
out.write_text(json.dumps({'reviewed_commit': HEAD, 'baseline': BASE,
                          'scope': 'archive checks plus mocked CLI handling; no Lean certification',
                          'checks': checks}, indent=2, sort_keys=True) + '\n')
print('COUNTEREXAMPLES: %d passed, %d failed' % (
    sum(c['pass'] for c in checks), sum(not c['pass'] for c in checks)), flush=True)
sys.exit(0 if all(c['pass'] for c in checks) else 1)
