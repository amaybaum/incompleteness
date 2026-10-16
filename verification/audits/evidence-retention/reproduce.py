#!/usr/bin/env python3
"""reproduce.py -- reproduces one archived expected result at its attested commit, and fails closed.

    python3 -I verification/audits/evidence-retention/reproduce.py --run RUN_ID --work DIR [--override-sha SHA]

Run from the repository root of a clone with full history and a Lean toolchain manager (elan) on PATH. The
verifier is this checkout: the manifest and results.json read here, and extract_result.py and compare_result.py
beside this file. The historical commit supplies only the sources, the toolchain pin and its own
tools/release_gate.py. The steps:
  1. find the entry ci-RUN_ID and its results.json; record the verifier commit;
  2. check that the attested commit is in the repository (a shallow clone fails here);
  3. check it out as a detached worktree under DIR;
  4. in its verification/lean-mathlib: `lean --version`, `lake exe cache get`, `lake --rehash build`; then, at its
     root, `python3 tools/release_gate.py`; everything captured to DIR/build-and-gate.log;
  5. extract the structured result from the captured output (DIR/reproduced.json);
  6. compare it with the expected result (compare_result.py); write DIR/verdict.txt.
Any failure (missing entry, unreachable commit, failed command, extraction without a build line or gate,
or a comparison failure) exits 1. --override-sha checks out another commit instead and is for negative
controls only: a result at the wrong commit must fail the comparison.
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
from extract_result import extract  # noqa: E402
from compare_result import compare, tree_module_exists  # noqa: E402


def sh(args, cwd, log, env=None):
    log.write('\n$ %s   (cwd %s)\n' % (' '.join(args), os.path.relpath(cwd, ROOT)))
    log.flush()
    p = subprocess.run(args, cwd=cwd, stdout=log, stderr=subprocess.STDOUT, env=env)
    log.write('\n[exit %d]\n' % p.returncode)
    log.flush()
    return p.returncode


def main():
    a = sys.argv[1:]
    if '--run' not in a or '--work' not in a:
        print(__doc__)
        return 2
    run_id = a[a.index('--run') + 1]
    work = os.path.abspath(a[a.index('--work') + 1])
    override = a[a.index('--override-sha') + 1] if '--override-sha' in a else None
    os.makedirs(work, exist_ok=True)
    verdict = open(os.path.join(work, 'verdict.txt'), 'w')

    def out(msg):
        print(msg)
        verdict.write(msg + '\n')
        verdict.flush()

    man = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
    ent = next((e for e in man['entries'] if e.get('id') == 'ci-' + run_id), None)
    if ent is None:
        out('FAIL  no entry ci-%s in the manifest' % run_id)
        return 1
    rp = next((f['path'] for f in ent['files'] if f['path'].endswith('/results.json')), None)
    if rp is None:
        out('FAIL  entry ci-%s has no results.json' % run_id)
        return 1
    expected = json.load(open(os.path.join(HERE, rp), encoding='utf-8'))
    if expected.get('kind') != 'bridge':
        out('FAIL  results of kind %r are not reproduced by this tool' % expected.get('kind'))
        return 1
    sha = override or expected['run']['head_sha']
    verifier = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    out('REPRODUCE  run %s: expected result at %s; verifier at %s%s' % (
        run_id, expected['run']['head_sha'][:12], verifier[:12], '; NEGATIVE CONTROL at %s' % sha[:12] if override else ''))
    if subprocess.run(['git', 'cat-file', '-e', sha + '^{commit}'], cwd=ROOT).returncode != 0:
        out('FAIL  commit %s is not in this repository (shallow clone, or the commit is not retained)' % sha)
        return 1
    tree = os.path.join(work, 'tree')
    log = open(os.path.join(work, 'build-and-gate.log'), 'w', encoding='utf-8', errors='replace')
    rc_all = 0
    try:
        if sh(['git', 'worktree', 'add', '--detach', tree, sha], ROOT, log) != 0:
            out('FAIL  could not check out %s' % sha)
            return 1
        at = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tree, capture_output=True, text=True).stdout.strip()
        if at != subprocess.run(['git', 'rev-parse', sha + '^{commit}'], cwd=ROOT, capture_output=True, text=True).stdout.strip():
            out('FAIL  the worktree is at %s, not %s' % (at[:12], sha[:12]))
            return 1
        lean = os.path.join(tree, 'verification', 'lean-mathlib')
        t0 = time.time()
        for args, cwd in ((['lean', '--version'], lean), (['lake', 'exe', 'cache', 'get'], lean),
                          (['lake', '--rehash', 'build'], lean), ([sys.executable, 'tools/release_gate.py'], tree)):
            rc = sh(args, cwd, log)
            if rc != 0:
                out('FAIL  `%s` exited %d' % (' '.join(args), rc))
                rc_all = 1
        log.write('\nTIMING reproduce-build-and-gate %ds\n' % (time.time() - t0))
    finally:
        log.close()
        subprocess.run(['git', 'worktree', 'remove', '--force', tree], cwd=ROOT, capture_output=True)
    rep = extract(open(os.path.join(work, 'build-and-gate.log'), encoding='utf-8', errors='replace').read())
    json.dump(rep, open(os.path.join(work, 'reproduced.json'), 'w'), indent=1, sort_keys=True)
    # the tree is removed; module existence is decided from the commit itself
    exists = lambda mod: subprocess.run(['git', 'cat-file', '-e', '%s:verification/lean-mathlib/%s' % (sha, mod)],
                                        cwd=ROOT, capture_output=True).returncode == 0
    fails = compare(expected, rep, exists)
    for f in fails:
        out('FAIL  %s' % f)
    ok = not fails and rc_all == 0
    out('REPRODUCTION  %s (%d comparison failure(s), commands %s) for run %s at %s, verifier %s' % (
        'HOLDS' if ok else 'FAILS', len(fails), 'ok' if rc_all == 0 else 'FAILED', run_id, sha[:12], verifier[:12]))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
