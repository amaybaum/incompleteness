#!/usr/bin/env python3
"""Scratch: run V3-11's frozen checkpoint for one stage at its stage commit. Negative controls run on
children built in a throwaway worktree and never pushed. Never landed.

Usage: ctl311.py <stage 1|2|3> <stage commit> [<stage 1 commit>]   (stage 2 needs stage 1's commit)"""
import json
import os
import re
import shutil
import subprocess
import sys

REPO = '/home/user/incompleteness'
HERE = os.path.dirname(os.path.abspath(__file__))
N, C = int(sys.argv[1]), sys.argv[2]
C1 = sys.argv[3] if len(sys.argv) > 3 else C
Q10 = '4a6e67e4cb097ae49d4e2d9f303b29c3b66ea952'
WT = os.path.join(HERE, 'ctlwt')
ENV = dict(os.environ, GIT_AUTHOR_NAME='ctl', GIT_AUTHOR_EMAIL='ctl@invalid', GIT_COMMITTER_NAME='ctl',
           GIT_COMMITTER_EMAIL='ctl@invalid')
ok = True


def git(*a, cwd=WT):
    return subprocess.run(['git'] + list(a), cwd=cwd, env=ENV, capture_output=True, check=True).stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def py(*a, cwd=WT):
    r = subprocess.run([sys.executable] + list(a), cwd=cwd, capture_output=True)
    return r.returncode, r.stdout.decode().rstrip('\n')


def commit(msg, files):
    for path, text in files.items():
        full = os.path.join(WT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, 'w', encoding='utf-8').write(text)
        git('add', path)
    git('commit', '-q', '-m', msg)
    return git('rev-parse', 'HEAD').strip()


def gate_step(name='v3-receipts'):
    code = ('import sys; sys.path.insert(0, "tools"); import release_gate as g; real = g.run\n'
            'g.run = lambda n, a, cwd=g.ROOT: real(n, a, cwd) if n == %r else (n, True, "stub")\n'
            'sys.argv = ["release_gate.py"]; rc = g.main(); sys.exit(rc)' % name)
    r = subprocess.run([sys.executable, '-c', code], cwd=WT, capture_output=True)
    line = [x for x in r.stdout.decode().split('\n') if ' %s ' % name in x]
    return r.returncode, (line[0].strip() if line else '(no line)')


def corrupt_child(base):
    git('checkout', '-q', '--detach', base)
    r10 = json.loads(git('show', '%s:verification/receipts/V3-10.json' % base))
    r10['execution_delta_digest'] = '0' * 64
    return commit('corrupt', {'verification/receipts/V3-10.json': json.dumps(r10, indent=1) + '\n'})


if os.path.exists(WT):
    subprocess.run(['git', 'worktree', 'remove', '--force', WT], cwd=REPO)
    shutil.rmtree(WT, ignore_errors=True)
subprocess.run(['git', 'worktree', 'prune'], cwd=REPO, check=True)
git('worktree', 'add', '--detach', WT, C, cwd=REPO)

if N == 1:
    rc, out = py('tools/v3_verifier.py', '--self-test')
    report('C1 self-test: %s' % out.split('\n')[-1], rc == 0)
    rc, out = py('tools/v3_verifier.py', '--corpus')
    report('C1 corpus: %s' % out.split('\n')[-1],
           rc == 0 and out.split('\n')[-1] == 'CORPUS  135 vector(s), exact and as expected')
    rc, out = py('tools/v3_verifier.py', '--receipts', C)
    report('C2 --receipts <stage 1>: exit %d, %r' % (rc, out.split('\n')), rc == 0 and out.split('\n') == [
        'RECEIPT  verification/receipts/V3-10.json  Q %s  HOLDS' % Q10, 'RECEIPTS  1 receipt(s), all hold'])
    rc, out = py('tools/v3_verifier.py', '--receipts', '92683262a67190d7468a31a0c2f1dfdbc391778e')
    report('C3 a tree with no receipt: exit %d, %r' % (rc, out), rc == 0 and out == 'RECEIPTS  0 receipt(s), all hold')
    rc, out = py('tools/v3_verifier.py', '--receipts', 'HEAD')
    report('C4 a ref name: exit %d, %r' % (rc, out), rc == 2 and out == 'v3_verifier: refused (input:not-an-object-id)')
    bad = corrupt_child(C)
    rc, out = py('tools/v3_verifier.py', '--receipts', bad)
    report('C5 a receipt rewritten after its Q: exit %d, %r' % (rc, out.split('\n')),
           rc == 1 and ('Q %s  FAILS' % bad) in out and out.endswith('NOT ALL HOLD'))
    git('checkout', '-q', '--detach', C)
    stray = commit('stray', {'verification/receipts/notes.txt': 'x\n'})
    rc, out = py('tools/v3_verifier.py', '--receipts', stray)
    report('C6 a non-receipt path in receipts/: exit %d, %r' % (rc, [x for x in out.split('\n') if 'notes' in x]),
           rc == 1 and 'verification/receipts/notes.txt  FAILS  s10:receipt-path' in out)
    git('checkout', '-q', '--detach', C)
    sh = os.path.join(HERE, 'ctlshallow')
    shutil.rmtree(sh, ignore_errors=True)
    git('clone', '-q', '--depth', '1', '--no-local', 'file://' + WT, sh, cwd=HERE)
    rc, out = py('tools/v3_verifier.py', '--receipts', git('rev-parse', 'HEAD', cwd=sh).strip(), cwd=sh)
    report('C7 a depth-1 clone: exit %d, %r' % (rc, out),
           rc == 1 and out == 'RECEIPTS  UNDECIDABLE  undecidable:shallow-repository')
    shutil.rmtree(sh)
    src = open(os.path.join(WT, 'tools/v3_verifier.py'), encoding='utf-8').read()
    for label, old, new in (
            ('verdict ignored', "        ok = ok and verdict == 'HOLDS'\n", ''),
            ('non-receipt path accepted', "            ok = False\n            continue\n        out = repo",
             "            continue\n        out = repo"),
            ('exit status dropped', "receipts(Repo(cwd), c)\n            print('\\n'.join(lines))\n            return 0 if ok else 1\n",
             "receipts(Repo(cwd), c)\n            print('\\n'.join(lines))\n            return 0\n")):
        assert src.count(old) == 1, label
        mp = os.path.join(WT, 'tools', 'v3_mutant.py')
        open(mp, 'w', encoding='utf-8').write(src.replace(old, new))
        rcs = [py('tools/v3_mutant.py', '--receipts', c)[0] for c in (bad, stray)]
        os.remove(mp)
        report('C8 mutant "%s": exits %s on C5\'s and C6\'s commits, caught' % (label, rcs), 0 in rcs)
elif N == 2:
    rc, line = gate_step()
    report('C9 the gate\'s v3-receipts step: exit %d, %s' % (rc, line),
           rc == 0 and line.startswith('PASS  v3-receipts') and 'RECEIPTS  1 receipt(s), all hold' in line)
    rc, out = py('tools/ci_gate_presence_test.py')
    report('C9 ci-gate-presence: %s' % out.split('\n')[-1], rc == 0)
    wf = open(os.path.join(WT, '.github/workflows/verify.yml'), encoding='utf-8').read()
    gs = open(os.path.join(WT, 'tools/release_gate.py'), encoding='utf-8').read()
    report('C9 the guard\'s conditions on the workflow and the gate hold',
           'name: Certificate verifier' in wf and 'certificate_verifier.py --mode shadow' in wf
           and 'certificate_verifier.py --mode authoritative' not in wf
           and '"certificate-verifier"' in gs and '"--mode", "authoritative"' in gs
           and '"lean-manuscript"' in gs and 'repertoire_lie' in wf)
    bridge = wf[wf.index('  bridge:'):]
    bridge = bridge[:bridge.index('\n  probes:')] if '\n  probes:' in bridge else bridge
    report('C9 the Mathlib bridge job checks out with fetch-depth: 0',
           re.search(r'uses: actions/checkout@v4\n\s+with:\n\s+fetch-depth: 0', bridge) is not None)
    report('C9 the diagnostics job carries its new name and the old one is gone',
           'name: V3 verifier diagnostics' in wf and 'name: V3 shadow verifier' not in wf)
    bad = corrupt_child(C1)
    git('checkout', C, '--', 'tools/release_gate.py', '.github/workflows/verify.yml')
    git('commit', '-q', '-m', 'C5 child with the stage 2 files')
    rc, line = gate_step()
    report('C10 the gate on C5\'s child with the stage 2 files: exit %d, %s' % (rc, line),
           rc == 1 and line.startswith('FAIL  v3-receipts'))
else:
    for t in ('voice_check', 'claims_check', 'duplicate_check', 'artifact_placement_check', 'control_plane_lint'):
        rc, out = py('tools/%s.py' % t)
        report('C11 %s' % out.split('\n')[-1], rc == 0)
    ag = open(os.path.join(WT, 'AGENTS.md'), encoding='utf-8').read()
    g = open(os.path.join(WT, 'verification/lean/edge_rigidity_probe.py'), encoding='utf-8').read()
    ns = {'os': os, 're': re, 'VERIFICATION': os.path.join(WT, 'verification')}
    for fn in ('_si2_agents_updated', '_si3_agents_updated'):
        m = re.search(r'^def %s\(.*?(?=^\S)' % fn, g, re.S | re.M)
        exec(m.group(0), ns)
        report('C12 the guard\'s %s holds on the new AGENTS.md' % fn, ns[fn](ag))
    flat = ' '.join(ag.split())
    report('C12 the R7-MSP phrases are present',
           '## §A.35 Registry contract for the Lean-to-manuscript census' in flat
           and 'updates the registry in the same commit' in flat)
    report('C13 one "## §A.39 " heading; "provisional V3 pilot" and "Provisional native" absent',
           ag.count('## §A.39 ') == 1 and 'provisional V3 pilot' not in ag and 'Provisional native' not in ag)
subprocess.run(['git', 'worktree', 'remove', '--force', WT], cwd=REPO)
print('STAGE %d CHECKPOINT %s' % (N, 'PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
