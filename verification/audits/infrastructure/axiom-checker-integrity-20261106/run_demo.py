#!/usr/bin/env python3
"""Run the #1162 synthetic demonstration.

For every fixture under fixtures/ this script
  1. checks that a mutated fixture is exactly its parent with the stated
     mutation applied to the log, and has the parent's sources;
  2. materializes a synthetic root in a temporary directory
     (<tmp>/<ID>/tree/verification/lean-mathlib/OIBridge/*.lean, from the
     fixture's *.lean.in files, and <tmp>/<ID>/build.log);
  3. runs the unmodified production checker as a subprocess,
         python3 -I tools/lean_axiom_check.py --root <tree> --log <log>
     and records its exit status and output;
  4. runs reference_checker.py on the same inputs;
  5. compares both with the hand-written expectations in fixtures/expected.json.

It writes results.json (schema oi-axiom-checker-demo-results, version 1) and
exits 0 only when every control is green. The verdict on the production
checker is generated from the recorded exit statuses, and only over green
controls. Nothing outside the temporary directory and results.json is written.

Usage: python3 -I run_demo.py [--out FILE]
"""
import hashlib, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
FIX = os.path.join(HERE, 'fixtures')
REF = os.path.join(HERE, 'reference_checker.py')
TAG = re.compile(r'^  (SORRY|BUILD|AXIOM|SILENT|EMPTY) ', re.M)
OK = re.compile(r'^lean_axiom_check: OK \((\d+) named result', re.M)


def git_blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def read_fixture(fid):
    base = os.path.join(FIX, fid)
    sources = {}
    src = os.path.join(base, 'lean-mathlib')
    for dp, dns, fs in os.walk(src):
        dns.sort()
        for f in sorted(fs):
            p = os.path.join(dp, f)
            sources[os.path.relpath(p, src).replace(os.sep, '/')] = \
                open(p, 'rb').read()
    log = open(os.path.join(base, 'build.log'), 'rb').read()
    return sources, log


def apply_mutation(log, mutation):
    text = log.decode('utf-8')
    for op in mutation:
        if op['op'] == 'drop':
            lines = text.split('\n')
            if lines.count(op['line']) != 1:
                return None
            lines.remove(op['line'])
            text = '\n'.join(lines)
        elif op['op'] == 'replace':
            if text.count(op['old']) != 1:
                return None
            text = text.replace(op['old'], op['new'])
        else:
            return None
    return text.encode('utf-8')


def run(argv, cwd):
    env = {'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'LC_ALL': 'C.UTF-8'}
    r = subprocess.run(argv, cwd=cwd, env=env, capture_output=True)
    return r.returncode, r.stdout.decode('utf-8'), r.stderr.decode('utf-8')


def main():
    out = os.path.join(HERE, 'results.json')
    if '--out' in sys.argv:
        out = os.path.abspath(sys.argv[sys.argv.index('--out') + 1])
    expected = json.load(open(os.path.join(FIX, 'expected.json'), encoding='utf-8'))
    tool = os.path.join(REPO, expected['tool']['path'])
    tool_bytes = open(tool, 'rb').read()
    controls = {'tool_blob_matches_pin':
                git_blob(tool_bytes) == expected['tool']['git_blob']}

    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for fid, exp in expected['fixtures'].items():
            sources, log = read_fixture(fid)
            row = {'id': fid, 'purpose': exp['purpose'], 'parent': exp['parent']}
            h = hashlib.sha256()
            for rel in sorted(sources):
                h.update(rel.encode() + b'\0' + sources[rel] + b'\0')
            h.update(b'build.log\0' + log)
            row['inputs_sha256'] = h.hexdigest()
            if exp['parent']:
                psrc, plog = read_fixture(exp['parent'])
                row['mutation_verified'] = (
                    psrc == sources
                    and apply_mutation(plog, exp['mutation']) == log)
            root = os.path.join(tmp, fid, 'tree')
            for rel, data in sources.items():
                assert rel.endswith('.lean.in')
                dst = os.path.join(root, 'verification', 'lean-mathlib',
                                   rel[:-len('.in')])
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                open(dst, 'wb').write(data)
            logp = os.path.join(tmp, fid, 'build.log')
            open(logp, 'wb').write(log)

            rc, so, se = run([sys.executable, '-I', tool, '--root', root,
                              '--log', logp], tmp)
            tags = sorted(set(TAG.findall(so)))
            okm = OK.search(so)
            row['tool'] = {'exit': rc, 'stdout': so, 'stderr': se, 'tags': tags,
                           'reported_count': int(okm.group(1)) if okm else None,
                           'self_test_passed': 'self-test:' not in so}
            rrc, rso, rse = run([sys.executable, '-I', REF, '--root', root,
                                 '--log', logp], tmp)
            ref = json.loads(rso) if rso.strip() else {}
            row['reference'] = {'exit': rrc, 'verdict': ref.get('verdict'),
                                'findings': ref.get('findings'), 'stderr': rse}

            tp = exp['tool_predicted']
            row['checks'] = {
                'reference_equals_expected':
                    ref.get('verdict') == exp['correct']
                    and ref.get('findings') == sorted(exp['correct_findings'])
                    and rrc == (0 if exp['correct'] == 'PASS' else 1),
                'tool_exit_equals_prediction': rc == tp['exit'],
                'tool_tags_equal_prediction': tags == sorted(tp['tags']),
                'tool_count_equals_prediction':
                    tp['reported_count'] is None
                    or row['tool']['reported_count'] == tp['reported_count'],
            }
            tool_pass = rc == 0
            if tool_pass == (exp['correct'] == 'PASS'):
                row['tool_vs_correct'] = 'matches'
            else:
                row['tool_vs_correct'] = 'false PASS' if tool_pass else 'false FAIL'
            rows.append(row)

    controls['tool_self_test_passed_every_run'] = all(
        r['tool']['self_test_passed'] for r in rows)
    controls['mutations_verified'] = all(
        r.get('mutation_verified', True) for r in rows)
    for k in ('reference_equals_expected', 'tool_exit_equals_prediction',
              'tool_tags_equal_prediction', 'tool_count_equals_prediction'):
        controls[k] = all(r['checks'][k] for r in rows)
    by = {r['id']: r for r in rows}
    controls['clean_fixtures_pass_both'] = all(
        by[i]['reference']['verdict'] == 'PASS' and by[i]['tool']['exit'] == 0
        for i in by if expected['fixtures'][i]['correct'] == 'PASS')
    controls['every_defect_fixture_fails_reference'] = all(
        by[i]['reference']['verdict'] == 'FAIL'
        for i in by if expected['fixtures'][i]['correct'] == 'FAIL')
    green = all(controls.values())

    false_pass = [r['id'] for r in rows if r['tool_vs_correct'] == 'false PASS']
    false_fail = [r['id'] for r in rows if r['tool_vs_correct'] == 'false FAIL']
    result = {
        'schema': 'oi-axiom-checker-demo-results',
        'version': 1,
        'tool': {'path': expected['tool']['path'], 'git_blob': git_blob(tool_bytes),
                 'sha256': hashlib.sha256(tool_bytes).hexdigest()},
        'reference_checker_sha256':
            hashlib.sha256(open(REF, 'rb').read()).hexdigest(),
        'expected_sha256': hashlib.sha256(
            open(os.path.join(FIX, 'expected.json'), 'rb').read()).hexdigest(),
        'controls': controls,
        'controls_green': green,
        'false_pass': false_pass,
        'false_fail': false_fail,
        'fixtures': rows,
    }
    with open(out, 'w', encoding='utf-8', newline='\n') as h:
        h.write(json.dumps(result, ensure_ascii=False, indent=2) + '\n')

    for r in rows:
        print(f"  {r['id']:4s} tool exit {r['tool']['exit']}  reference "
              f"{r['reference']['verdict']:4s}  {r['tool_vs_correct']}")
    for k, v in controls.items():
        print(f"  control {k}: {'green' if v else 'RED'}")
    if not green:
        print('run_demo: controls not green; no verdict.')
        return 1
    if false_pass:
        print(f"run_demo: verdict: the production checker exits 0 on "
              f"{len(false_pass)} fixture(s) whose correct outcome is FAIL: "
              f"{', '.join(false_pass)}.")
    else:
        print('run_demo: verdict: no false PASS on any fixture.')
    if false_fail:
        print(f"run_demo: false FAIL on: {', '.join(false_fail)}.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
