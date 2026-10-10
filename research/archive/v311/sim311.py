#!/usr/bin/env python3
"""Scratch: rehearse V3-11 at D in a throwaway worktree, with every control the preregistration
names. Never landed. Usage: sim311.py <D> <preregistration file>"""
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edits311 as ed  # noqa: E402

REPO = '/home/user/incompleteness'
D, PRE = sys.argv[1], sys.argv[2]
WT = os.path.join(HERE, 'wt')
RD = 'verification/infrastructure/round-v3-11-authority-cutover/'
P, RECEIPT = RD + 'preregistration.md', 'verification/receipts/V3-11.json'
Q10 = '4a6e67e4cb097ae49d4e2d9f303b29c3b66ea952'
ENV = dict(os.environ, GIT_AUTHOR_NAME='sim', GIT_AUTHOR_EMAIL='sim@invalid', GIT_COMMITTER_NAME='sim',
           GIT_COMMITTER_EMAIL='sim@invalid', GIT_AUTHOR_DATE='1700000000 +0000',
           GIT_COMMITTER_DATE='1700000000 +0000')
ok = True


def git(*a, cwd=WT, data=None, check=True):
    r = subprocess.run(['git'] + list(a), cwd=cwd, env=ENV, input=data, capture_output=True)
    if check and r.returncode:
        raise SystemExit('git %s: %s' % (a, r.stderr.decode()))
    return r.stdout.decode()


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


def gate_step(cwd, name='v3-receipts'):
    """Run the release gate with every step but `name` stubbed out; (exit, gate line)."""
    code = ('import sys; sys.path.insert(0, "tools"); import release_gate as g; real = g.run\n'
            'g.run = lambda n, a, cwd=g.ROOT: real(n, a, cwd) if n == %r else (n, True, "stub")\n'
            'sys.argv = ["release_gate.py"]; rc = g.main(); sys.exit(rc)' % name)
    r = subprocess.run([sys.executable, '-c', code], cwd=cwd, capture_output=True)
    line = [x for x in r.stdout.decode().split('\n') if ' %s ' % name in x]
    return r.returncode, (line[0].strip() if line else '(no line)')


if os.path.exists(WT):
    subprocess.run(['git', 'worktree', 'remove', '--force', WT], cwd=REPO)
    shutil.rmtree(WT, ignore_errors=True)
subprocess.run(['git', 'worktree', 'prune'], cwd=REPO, check=True)
git('worktree', 'add', '--detach', WT, D, cwd=REPO)
texts = {p: git('show', '%s:%s' % (D, p)) for p in sorted({e[0] for e in ed.EDITS})}

F = commit('F', {P: open(PRE, encoding='utf-8').read()})
cur = dict(texts)
stage_commit = {}
for n in (1, 2, 3):
    cur = ed.apply(cur, n)
    stage_commit[n] = commit('stage %d' % n, {p: cur[p] for p in ed.STAGES[n]})
    for p in ed.STAGES[n]:
        report('stage %d: %s blob %s' % (n, p, ed.blob(cur[p])[:8]),
               git('rev-parse', 'HEAD:' + p).strip() == ed.blob(cur[p]))
    if n == 1:
        E1 = stage_commit[1]
        rc, out = py('tools/v3_verifier.py', '--self-test')
        report('C1 self-test: %s' % out.split('\n')[-1], rc == 0)
        rc, out = py('tools/v3_verifier.py', '--corpus')
        report('C1 corpus: %s' % out.split('\n')[-1],
               rc == 0 and out.split('\n')[-1] == 'CORPUS  135 vector(s), exact and as expected')
        rc, out = py('tools/v3_verifier.py', '--receipts', E1)
        report('C2 --receipts E1: exit %d, %r' % (rc, out.split('\n')), rc == 0 and out.split('\n') == [
            'RECEIPT  verification/receipts/V3-10.json  Q %s  HOLDS' % Q10,
            'RECEIPTS  1 receipt(s), all hold'])
        rc, out = py('tools/v3_verifier.py', '--receipts', '92683262a67190d7468a31a0c2f1dfdbc391778e')
        report('C3 --receipts at a tree with no receipt: exit %d, %r' % (rc, out),
               rc == 0 and out == 'RECEIPTS  0 receipt(s), all hold')
        rc, out = py('tools/v3_verifier.py', '--receipts', 'HEAD')
        report('C4 a ref name: exit %d, %r' % (rc, out), rc == 2 and out == 'v3_verifier: refused (input:not-an-object-id)')
        # negatives on children of E1, never kept
        r10 = json.loads(git('show', '%s:verification/receipts/V3-10.json' % E1))
        r10['execution_delta_digest'] = '0' * 64
        bad = commit('corrupt', {'verification/receipts/V3-10.json': json.dumps(r10, indent=1) + '\n'})
        rc, out = py('tools/v3_verifier.py', '--receipts', bad)
        report('C5 a receipt rewritten after its Q: exit %d, %s' % (rc, out.split('\n')[-1]),
               rc == 1 and ('Q %s  FAILS' % bad) in out and out.endswith('NOT ALL HOLD'))
        git('checkout', '-q', '--detach', E1)
        stray = commit('stray', {'verification/receipts/notes.txt': 'x\n'})
        rc, out = py('tools/v3_verifier.py', '--receipts', stray)
        report('C6 a non-receipt path in receipts/: exit %d, %r' % (rc, out.split('\n')[0]),
               rc == 1 and 'verification/receipts/notes.txt  FAILS  s10:receipt-path' in out)
        git('checkout', '-q', '--detach', E1)
        sh = os.path.join(HERE, 'shallow')
        shutil.rmtree(sh, ignore_errors=True)
        git('clone', '-q', '--depth', '1', '--no-local', 'file://' + WT, sh, cwd=HERE)
        rc, out = py('tools/v3_verifier.py', '--receipts', git('rev-parse', 'HEAD', cwd=sh).strip(), cwd=sh)
        report('C7 a shallow repository: exit %d, %r' % (rc, out),
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
            caught = []
            for c in (bad, stray):
                rc, out = py('tools/v3_mutant.py', '--receipts', c)
                caught.append(rc == 1)
            os.remove(mp)
            report('C8 mutant "%s" is caught by C5 or C6' % label, not all(caught))
    if n == 2:
        rc, line = gate_step(WT)
        report('C9 the gate\'s v3-receipts step at stage 2: exit %d, %s' % (rc, line),
               rc == 0 and line.startswith('PASS  v3-receipts') and 'RECEIPTS  1 receipt(s), all hold' in line)
        rc, out = py('tools/ci_gate_presence_test.py')
        report('C9 ci-gate-presence: %s' % out.split('\n')[-1], rc == 0)
        wf = open(os.path.join(WT, ed.W), encoding='utf-8').read()
        gs = open(os.path.join(WT, ed.G), encoding='utf-8').read()
        report('C9 the guard\'s CV-1 workflow and gate conditions still hold',
               'name: Certificate verifier' in wf and 'certificate_verifier.py --mode shadow' in wf
               and 'certificate_verifier.py --mode authoritative' not in wf
               and '"certificate-verifier"' in gs and '"--mode", "authoritative"' in gs
               and '"lean-manuscript"' in gs and 'repertoire_lie' in wf)
        bridge = wf[wf.index('  bridge:'):wf.index('  probes:') if '  probes:' in wf else None]
        report('C9 the Mathlib bridge job checks out with fetch-depth: 0',
               re.search(r'uses: actions/checkout@v4\n\s+with:\n\s+fetch-depth: 0', bridge) is not None)
        report('C9 the diagnostics job is renamed and still not in the gate',
               'name: V3 verifier diagnostics' in wf and 'name: V3 shadow verifier' not in wf)
        git('checkout', '-q', '--detach', bad)
        git('checkout', stage_commit[2], '--', ed.G, ed.W, 'tools/v3_verifier.py')
        git('commit', '-q', '-m', 'bad with stage 2')
        rc, line = gate_step(WT)
        report('C10 the gate fails on a receipt rewritten after its Q: exit %d, %s' % (rc, line),
               rc == 1 and line.startswith('FAIL  v3-receipts'))
        git('checkout', '-q', '--detach', stage_commit[2])
    if n == 3:
        for t in ('voice_check', 'claims_check', 'duplicate_check', 'artifact_placement_check',
                  'control_plane_lint'):
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
        report('C12 the guard\'s R7-MSP phrases', '## §A.35 Registry contract for the Lean-to-manuscript census' in flat
               and 'updates the registry in the same commit' in flat)
        report('C13 one "## §A.39 " heading, the pilot wording gone',
               ag.count('## §A.39 ') == 1 and 'provisional V3 pilot' not in ag and 'Provisional native' not in ag)

E = commit('E', {RD + 'result.md': '# V3-11 result (rehearsal placeholder)\n'})
LAM = git('commit-tree', E + '^{tree}', '-p', D, '-p', E, '-m', 'reconcile').strip()
git('checkout', '-q', '--detach', LAM)
att = []
for s in ('F', 'E'):
    att += ['--attest', 'owner-designation', s, 'rehearsal', '--attest', 'check-run', s, 'rehearsal']
rc, receipt = py('tools/v3_receipt.py', '--status', 'complete', '--d', D, '--f', F, '--e', E,
                 '--reconciliation', LAM, *att)
report('the builder exits 0', rc == 0)
Q = commit('Q', {RECEIPT: receipt + '\n'})
rc, out = py('tools/v3_verifier.py', '--verify-round', Q)
report('--verify-round Q: %s' % out.split('\n')[-1], out.split('\n')[-1] == 'VERDICT  HOLDS')
rc, out = py('tools/v3_verifier.py', '--receipts', Q)
report('--receipts Q: exit %d, %s' % (rc, out.split('\n')[-1]),
       rc == 0 and out.split('\n')[-1] == 'RECEIPTS  2 receipt(s), all hold' and ('Q %s  HOLDS' % Q) in out)
M = git('commit-tree', Q + '^{tree}', '-p', D, '-p', Q, '-m', 'synthetic merge').strip()
git('checkout', '-q', '--detach', M)
rc, line = gate_step(WT)
report('the gate at a synthetic merge of Q into D: %s' % line,
       rc == 0 and 'RECEIPTS  2 receipt(s), all hold' in line)
git('checkout', '-q', '--detach', LAM)
r = json.loads(receipt)
r['execution_delta_digest'] = '0' * 64
Q2 = commit('Q corrupted', {RECEIPT: json.dumps(r, indent=1) + '\n'})
rc, out = py('tools/v3_verifier.py', '--verify-round', Q2)
report('control, execution delta digest zeroed: %s' % out.split('\n')[-1],
       out.split('\n')[-1].startswith('VERDICT  FAILS'))
rc, line = gate_step(WT)
report('control, the gate at that commit: exit %d, %s' % (rc, line), rc == 1 and line.startswith('FAIL  v3-receipts'))
d = sorted(x for x in git('diff', '--no-renames', '--name-status', D, Q).split('\n') if x)
want = sorted(['A\t' + P, 'A\t' + RD + 'result.md', 'A\t' + RECEIPT] +
              ['M\t' + p for p in sorted({e[0] for e in ed.EDITS})])
report('delta(D, Q) is the governed set: %d paths' % len(d), d == want)
subprocess.run(['git', 'worktree', 'remove', '--force', WT], cwd=REPO)
print('ALL REHEARSAL CHECKS PASS' if ok else 'A REHEARSAL CHECK FAILED')
