#!/usr/bin/env python3
"""Scratch: simulate the V3-9 execution from a base commit in a throwaway worktree, measuring the
controls. Never landed; nothing pushed. Usage: sim39.py <base> [<builder file> <a39 file>
<preamble old> <preamble new>]; the defaults are the drafts beside this script."""
import hashlib
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/incompleteness'
BASE = sys.argv[1]
BUILDER, A39, PRE_OLD, PRE_NEW = (sys.argv[2:6] if len(sys.argv) > 2 else
                                   [os.path.join(HERE, x) for x in
                                    ('v3_receipt.py', 'a39.md', 'pre_old.txt', 'pre_new.txt')])
WT = os.path.join(HERE, 'wt')
TOOL, ARCH, AG = 'tools/v3_receipt.py', 'verification/infrastructure/v3/architecture.md', 'AGENTS.md'
ENV = dict(os.environ, GIT_AUTHOR_NAME='sim', GIT_AUTHOR_EMAIL='sim@invalid', GIT_COMMITTER_NAME='sim',
           GIT_COMMITTER_EMAIL='sim@invalid', GIT_AUTHOR_DATE='1700000000 +0000',
           GIT_COMMITTER_DATE='1700000000 +0000')
ok = True

# one derivation wrong each; the self-test must fail on every one
VARIANTS = {
    'execution delta from D': ("v3.delta_digest(repo.delta(f, e), fmt)", "v3.delta_digest(repo.delta(d, e), fmt)"),
    'landing base is the second parent': ("r['landing'] = {'base': lp[0],", "r['landing'] = {'base': lp[1],"),
    'control-plane blobs in reverse order': ("for p in sorted(cp_files)]", "for p in sorted(cp_files, reverse=True)]"),
    'no withdrawal reason when none exists': ("        if withdrawal is None:\n            absent['withdrawal'] = 'no-execution-commits'\n", ""),
    'seal blob without the object header': ("return h(b'blob %d\\0' % len(data) + data).hexdigest()", "return h(data).hexdigest()"),
    'every attestation on F': ("subj = {'F': f, 'E': e}", "subj = {'F': f, 'E': f}"),
}


def git(*a, cwd=WT):
    return subprocess.run(['git'] + list(a), cwd=cwd, env=ENV, capture_output=True, check=True).stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def run(*a, cwd=WT):
    p = subprocess.run([sys.executable] + list(a), cwd=cwd, capture_output=True)
    return p.returncode, p.stdout.decode().rstrip('\n')


if os.path.exists(WT):
    subprocess.run(['git', 'worktree', 'remove', '--force', WT], cwd=REPO)
    shutil.rmtree(WT, ignore_errors=True)
subprocess.run(['git', 'worktree', 'prune'], cwd=REPO, check=True)
git('worktree', 'add', '--detach', WT, BASE, cwd=REPO)
blobs = {}
v3b = git('rev-parse', 'HEAD:tools/v3_verifier.py').strip()

# stage 1: the builder
shutil.copy(BUILDER, os.path.join(WT, TOOL))
git('add', TOOL); git('commit', '-q', '-m', 'stage 1')
blobs['builder'] = git('rev-parse', 'HEAD:' + TOOL).strip()
report('stage 1 changes only %s' % TOOL, git('diff', '--name-status', 'HEAD^', 'HEAD').split() == ['A', TOOL])
rc, out = run(TOOL, '--self-test')
print('\n'.join('      ' + x for x in out.split('\n')))
report('C1 self-test exit %d, last line %r' % (rc, out.split('\n')[-1]), rc == 0 and out.endswith('v3_receipt: self-test OK'))
src = open(BUILDER, encoding='utf-8').read()
procs = {}
for name, (old, new) in VARIANTS.items():
    assert src.count(old) == 1, name
    path = os.path.join(WT, 'tools', 'v3_receipt_variant_%d.py' % len(procs))
    open(path, 'w', encoding='utf-8').write(src.replace(old, new))
    procs[name] = (path, subprocess.Popen([sys.executable, path, '--self-test'], cwd=WT,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT))
for name, (path, p) in procs.items():
    out = p.communicate()[0].decode()
    fails = [x for x in out.split('\n') if x.startswith('FAIL')]
    report('C2 variant %-40s self-test exit %d, %d FAIL line(s)' % (name, p.returncode, len(fails)),
           p.returncode == 1 and 'self-test FAILED' in out and fails)
    os.remove(path)
rc1, o1 = run(TOOL, '--status', 'complete', '--d', 'HEAD', '--f', 'HEAD')
rc2, o2 = run(TOOL)
report('C3 a ref name refused: exit %d, %r' % (rc1, o1), rc1 == 2 and o1 == 'v3_receipt: refused (input:not-an-object-id)')
report('C3 no arguments: exit %d, usage' % rc2, rc2 == 2 and o2.startswith('usage: v3_receipt.py'))
rc, out = run('tools/v3_verifier.py', '--corpus')
report('C4 %s' % out.split('\n')[-1], rc == 0 and out.split('\n')[-1] == 'CORPUS  135 vector(s), exact and as expected')
rc, out = run('tools/v3_verifier.py', '--self-test')
report('C4 %s' % out, rc == 0)
report('C4 tools/v3_verifier.py blob unchanged', git('rev-parse', 'HEAD:tools/v3_verifier.py').strip() == v3b)

# stage 2: the rule and the preamble
ag0 = open(os.path.join(WT, AG), encoding='utf-8').read()
a39 = open(A39, encoding='utf-8').read()
open(os.path.join(WT, AG), 'w', encoding='utf-8').write(ag0 + a39)
ar0 = open(os.path.join(WT, ARCH), encoding='utf-8').read()
po, pn = open(PRE_OLD, encoding='utf-8').read(), open(PRE_NEW, encoding='utf-8').read()
assert ar0.count(po) == 1
open(os.path.join(WT, ARCH), 'w', encoding='utf-8').write(ar0.replace(po, pn))
git('add', AG, ARCH); git('commit', '-q', '-m', 'stage 2')
blobs['agents'] = git('rev-parse', 'HEAD:' + AG).strip()
blobs['arch'] = git('rev-parse', 'HEAD:' + ARCH).strip()
report('stage 2 changes only AGENTS.md and architecture.md',
       sorted(git('diff', '--name-only', 'HEAD^', 'HEAD').split()) == sorted([AG, ARCH]))
ag1 = git('show', 'HEAD:' + AG)
report('C5 AGENTS.md at stage 2 is AGENTS.md at the base followed by the frozen text',
       ag1.startswith(ag0) and ag1[len(ag0):] == a39)
report('C5 AGENTS.md carries one §A.39 heading and no §A.38', ag1.count('## §A.39 ') == 1 and '§A.38' not in ag1)
ar1 = git('show', 'HEAD:' + ARCH)
report('C5 architecture.md differs from the base by the preamble sentence alone', ar1 == ar0.replace(po, pn))
report('C5 architecture.md no longer says the specification is not operative', 'is not operative' not in ar1)
rc, out = run('tools/v3_verifier.py', '--corpus')
report('C4 stage 2 %s' % out.split('\n')[-1], rc == 0 and out.split('\n')[-1] == 'CORPUS  135 vector(s), exact and as expected')
print('blobs:', blobs)
print('sha256 builder:', hashlib.sha256(open(BUILDER, 'rb').read()).hexdigest())
print('stage-2 commit:', git('rev-parse', 'HEAD').strip())
print('ALL CONTROLS PASS' if ok else 'A CONTROL FAILED')
