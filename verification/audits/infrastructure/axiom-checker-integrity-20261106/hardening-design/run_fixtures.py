#!/usr/bin/env python3
"""Check the hardening-design fixtures for #1162 (design only).

No hardened checker exists; this script does not implement one. It checks
what can be checked mechanically before an implementation is authorized:

  1. every mutated fixture is its parent with the stated log mutation and the
     parent's sources;
  2. fixtures/expected.json is well formed: every P fixture is PASS with no
     findings, every F fixture is FAIL with findings, every finding kind is in
     the vocabulary, every kind except BUILD is the sole kind of at least one F
     fixture, and every mutant names killing fixtures whose hardened verdict it
     flips;
  3. the unmodified production checker, run as
         python3 -I tools/lean_axiom_check.py --root <tree> --log <log>
     on each fixture (materialized in a temporary directory), returns the exit
     status, problem tags and reported count predicted by hand.

The hardened column of expected.json is a hand derivation from
HARDENING-DESIGN.md, checked by review. It writes results.json (schema
oi-axiom-checker-hardening-fixtures, version 1) and exits 0 only when every
control is green.

Usage: python3 -I run_fixtures.py [--out FILE]
"""
import hashlib, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
FIX = os.path.join(HERE, 'fixtures')
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
    lines = log.decode('utf-8').split('\n')
    for op in mutation:
        kind = op['op']
        if kind in ('drop', 'duplicate'):
            if lines.count(op['line']) != 1:
                return None
            i = lines.index(op['line'])
            if kind == 'drop':
                del lines[i]
            else:
                lines.insert(i + 1, op['line'])
        elif kind == 'replace':
            text = '\n'.join(lines)
            if text.count(op['old']) != 1:
                return None
            lines = text.replace(op['old'], op['new']).split('\n')
        elif kind == 'append':
            if lines[-1] != '':
                return None
            lines.insert(len(lines) - 1, op['line'])
        elif kind == 'clear':
            lines = ['']
        else:
            return None
    return '\n'.join(lines).encode('utf-8')


def run(argv, cwd):
    env = {'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'LC_ALL': 'C.UTF-8'}
    r = subprocess.run(argv, cwd=cwd, env=env, capture_output=True)
    return r.returncode, r.stdout.decode('utf-8'), r.stderr.decode('utf-8')


def structure(expected):
    """Checks on the hand-written expectations that need no checker."""
    kinds = set(expected['kinds'])
    fx = expected['fixtures']
    ok = {}
    ok['p_fixtures_pass_without_findings'] = all(
        v['hardened'] == {'verdict': 'PASS', 'findings': []}
        for k, v in fx.items() if k.startswith('P'))
    ok['f_fixtures_fail_with_findings'] = all(
        v['hardened']['verdict'] == 'FAIL' and v['hardened']['findings']
        for k, v in fx.items() if k.startswith('F'))
    ok['findings_sorted_and_known'] = all(
        v['hardened']['findings'] == sorted(v['hardened']['findings'])
        and all(f.split('@')[0] in kinds for f in v['hardened']['findings'])
        for v in fx.values())
    sole = {f['findings'][0].split('@')[0] for f in
            (v['hardened'] for v in fx.values())
            if f['findings'] and len({x.split('@')[0] for x in f['findings']}) == 1}
    ok['every_kind_but_build_has_a_sole_kind_fixture'] = kinds - {'BUILD'} <= sole
    ok['mutants_flip_their_killers'] = all(
        m['killed_by'] and all(
            fid in fx and out in ('PASS', 'FAIL')
            and out != fx[fid]['hardened']['verdict']
            for fid, out in m['killed_by'].items())
        for m in expected['mutants'].values())
    return ok, sorted(sole)


def main():
    out = os.path.join(HERE, 'results.json')
    if '--out' in sys.argv:
        out = os.path.abspath(sys.argv[sys.argv.index('--out') + 1])
    expected = json.load(open(os.path.join(FIX, 'expected.json'), encoding='utf-8'))
    tool = os.path.join(REPO, expected['tool']['path'])
    tool_bytes = open(tool, 'rb').read()
    controls = {'tool_blob_matches_pin':
                git_blob(tool_bytes) == expected['tool']['git_blob']}
    struct, sole = structure(expected)
    controls.update(struct)

    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for fid, exp in expected['fixtures'].items():
            sources, log = read_fixture(fid)
            row = {'id': fid, 'purpose': exp['purpose'], 'parent': exp['parent'],
                   'hardened': exp['hardened']}
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
            tree = os.path.join(tmp, fid, 'tree')
            os.makedirs(os.path.join(tree, 'verification', 'lean-mathlib'))
            for rel, data in sources.items():
                assert rel.endswith('.lean.in')
                dst = os.path.join(tree, 'verification', 'lean-mathlib',
                                   rel[:-len('.in')])
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                open(dst, 'wb').write(data)
            logp = os.path.join(tmp, fid, 'build.log')
            open(logp, 'wb').write(log)
            rc, so, se = run([sys.executable, '-I', tool, '--root', tree,
                              '--log', logp], tmp)
            okm = OK.search(so)
            row['current'] = {'exit': rc, 'stdout': so, 'stderr': se,
                              'tags': sorted(set(TAG.findall(so))),
                              'reported_count': int(okm.group(1)) if okm else None,
                              'self_test_passed': 'self-test:' not in so}
            tp = exp['current_predicted']
            row['current_matches_prediction'] = (
                rc == tp['exit'] and row['current']['tags'] == sorted(tp['tags'])
                and (tp['reported_count'] is None
                     or row['current']['reported_count'] == tp['reported_count']))
            design_pass = exp['hardened']['verdict'] == 'PASS'
            if (rc == 0) == design_pass:
                row['current_vs_design'] = 'agrees'
            else:
                row['current_vs_design'] = ('current PASS, design FAIL' if rc == 0
                                            else 'current FAIL, design PASS')
            rows.append(row)

    controls['tool_self_test_passed_every_run'] = all(
        r['current']['self_test_passed'] for r in rows)
    controls['mutations_verified'] = all(r.get('mutation_verified', True) for r in rows)
    controls['current_matches_prediction'] = all(
        r['current_matches_prediction'] for r in rows)
    green = all(controls.values())
    cur_pass = [r['id'] for r in rows if r['current_vs_design'] == 'current PASS, design FAIL']
    cur_fail = [r['id'] for r in rows if r['current_vs_design'] == 'current FAIL, design PASS']
    result = {
        'schema': 'oi-axiom-checker-hardening-fixtures',
        'version': 1,
        'tool': {'path': expected['tool']['path'], 'git_blob': git_blob(tool_bytes),
                 'sha256': hashlib.sha256(tool_bytes).hexdigest()},
        'expected_sha256': hashlib.sha256(
            open(os.path.join(FIX, 'expected.json'), 'rb').read()).hexdigest(),
        'controls': controls,
        'controls_green': green,
        'sole_kind_fixtures_cover': sole,
        'current_pass_design_fail': cur_pass,
        'current_fail_design_pass': cur_fail,
        'fixtures': rows,
    }
    with open(out, 'w', encoding='utf-8', newline='\n') as h:
        h.write(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for r in rows:
        print(f"  {r['id']}  design {r['hardened']['verdict']:4s}  current exit "
              f"{r['current']['exit']}  {r['current_vs_design']}")
    for k, v in controls.items():
        print(f"  control {k}: {'green' if v else 'RED'}")
    if not green:
        print('run_fixtures: controls not green; no verdict.')
        return 1
    print(f"run_fixtures: the production checker exits 0 on {len(cur_pass)} fixture(s) "
          f"the design fails: {', '.join(cur_pass) or 'none'}; it exits nonzero on "
          f"{len(cur_fail)} fixture(s) the design passes: {', '.join(cur_fail) or 'none'}.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
