"""Amendment r4 copy of mutate_c2.py (adds the set o9, mutants_o9.py); otherwise unchanged. Correction 2 copy of mutate_c1.py: runs the mutant sets named by MUTANT_SETS (default c1, c2, v60e, cache) with one worker; ids are prefixed by their set. Runs every mutant against the engine self-test, the synthetic fixture and the conformance controls
of a copy of the final commit, and compares each control's status with the unmutated base.
Usage: python3 -I mutate.py WORK_DIR SOURCE_TREE [MUTANT_ID ...]
SOURCE_TREE: an extraction of the final commit (git archive), made a fresh git repository by this script."""
import concurrent.futures as cf
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib  # noqa: E402
SETS = {"v60e": "mutants", "cache": "mutants_cache", "c1": "mutants_c1", "c2": "mutants_c2", "o9": "mutants_o9"}
MUTANTS = []
for _k in os.environ.get("MUTANT_SETS", "c1,c2,v60e,cache,o9").split(","):
    MUTANTS += [(_k + ":" + m[0],) + tuple(m[1:]) for m in importlib.import_module(SETS[_k]).MUTANTS]

AUDIT = 'verification/audits/foundations/ledger-coverage-tool-20261123'
WFP = '.github/workflows/ledger-coverage.yml'
ENV = dict(os.environ, GIT_AUTHOR_NAME='m', GIT_AUTHOR_EMAIL='m', GIT_COMMITTER_NAME='m', GIT_COMMITTER_EMAIL='m',
           GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM='1')


def go(argv, cwd=None):
    try:
        p = subprocess.run([sys.executable, '-I', '-B'] + argv, capture_output=True, text=True, timeout=900, cwd=cwd)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 'TIMEOUT', '', ''


def run_all(root, out, wt):
    os.makedirs(out, exist_ok=True)
    res = {}
    t = os.path.join(root, 'tools')
    rc, so, se = go([os.path.join(t, 'ledger_coverage.py'), 'self-test', '--out', os.path.join(out, 'st')])
    try:
        for c in json.load(open(os.path.join(out, 'st', 'result.json')))['controls']:
            res['self-test/' + c['id']] = 'PASS' if c['passed'] else 'FAIL'
    except Exception as exc:
        res['self-test/*'] = 'CRASH %s rc=%s' % (type(exc).__name__, rc)
    rc, so, se = go([os.path.join(t, 'ledger_coverage', 'adapters', 'synthetic_fixture.py'), os.path.join(out, 'syn'), wt])
    try:
        d = json.loads(so)
        for k, v in d.items():
            if not k.startswith('_'):
                res['synthetic/' + k] = 'PASS' if v is True else 'FAIL'
    except Exception as exc:
        res['synthetic/*'] = 'CRASH %s rc=%s %s' % (type(exc).__name__, rc, se[-300:])
    rc, so, se = go([os.path.join(t, 'ledger_coverage', 'adapters', 'conformance_controls.py'), os.path.join(out, 'conf')])
    try:
        d = json.load(open(os.path.join(out, 'conf', 'conformance-controls.json')))
        for c in d['controls']:
            res['conformance/' + c['id']] = c['status']
    except Exception as exc:
        res['conformance/*'] = 'CRASH %s rc=%s %s' % (type(exc).__name__, rc, se[-400:])
    return res


def one(args):
    m, work, wt = args
    mid, f, reps, why = m
    root = os.path.join(work, 'mut', mid.replace(':', '-'))
    if os.path.exists(root):
        shutil.rmtree(root)
    os.makedirs(os.path.join(root, 'tools'))
    shutil.copytree(os.path.join(wt, 'tools', 'ledger_coverage'), os.path.join(root, 'tools', 'ledger_coverage'))
    shutil.copy(os.path.join(wt, 'tools', 'ledger_coverage.py'), os.path.join(root, 'tools', 'ledger_coverage.py'))
    shutil.copytree(os.path.join(wt, AUDIT), os.path.join(root, AUDIT))
    os.makedirs(os.path.join(root, '.github', 'workflows'))
    shutil.copy(os.path.join(wt, WFP), os.path.join(root, WFP))
    p = os.path.join(root, 'tools', f)
    src = open(p).read()
    for old, new in reps:
        n = src.count(old)
        if n != 1:
            return mid, {'_apply': 'old string occurs %d times: %r' % (n, old[:80])}
        src = src.replace(old, new)
    open(p, 'w').write(src)
    r = run_all(root, os.path.join(root, 'out'), wt)
    shutil.rmtree(os.path.join(root, 'tools'))
    return mid, r


def main():
    work, wt = sys.argv[1], sys.argv[2]
    sel = sys.argv[3:]
    if not os.path.isdir(os.path.join(wt, '.git')):
        subprocess.run(['git', 'init', '-q'], cwd=wt, env=ENV, check=True)
        subprocess.run(['git', 'add', '-A'], cwd=wt, env=ENV, check=True)
        subprocess.run(['git', 'commit', '-qm', 'final commit extraction'], cwd=wt, env=ENV, check=True)
    os.makedirs(os.path.join(work, 'mut'), exist_ok=True)
    base = run_all(wt, os.path.join(work, 'base-run'), wt)
    json.dump(base, open(os.path.join(work, 'base.json'), 'w'), indent=1, sort_keys=True)
    ms = [m for m in MUTANTS if not sel or m[0] in sel]
    out = {}
    with cf.ThreadPoolExecutor(1) as ex:
        for mid, r in ex.map(one, [(m, work, wt) for m in ms]):
            out[mid] = r
    summary = []
    for m in ms:
        mid = m[0]
        r = out[mid]
        if '_apply' in r:
            summary.append({'id': mid, 'file': m[1], 'rule': m[3], 'status': 'NOT APPLIED', 'why': r['_apply']})
            continue
        killed = sorted(k for k, v in r.items() if base.get(k) != v)
        summary.append({'id': mid, 'file': m[1], 'rule': m[3], 'status': 'KILLED' if killed else 'SURVIVED',
                        'killed_by': killed})
    counts = {}
    for s in summary:
        counts[s['status']] = counts.get(s['status'], 0) + 1
    json.dump({'base_counts': {s: sum(1 for v in base.values() if v == s) for s in set(base.values())},
               'counts': counts, 'mutants': summary, 'raw': out},
              open(os.path.join(work, 'results.json'), 'w'), indent=1, sort_keys=True)
    for s in summary:
        print(s['id'], s['status'], s.get('why', ''), ' '.join(s.get('killed_by', [])[:6]), '|', s['rule'])
    print(json.dumps(counts))


if __name__ == '__main__':
    main()
