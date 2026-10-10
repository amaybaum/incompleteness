#!/usr/bin/env python3
"""Scratch: rehearse pilot round PILOT-SB1 locally, with no host. Never landed; nothing pushed.

Usage: sim37.py <base commit standing in for B>
Builds F, E, R1, Q1, the sandbox advance T2, R2 and Q2 as local objects only, and runs the committed
shadow tool's --verify-round and --publication on them."""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import receipt37  # noqa

REPO = '/home/user/incompleteness'
FILES = os.path.join(HERE, 'files')
B = sys.argv[1]
RDIR = receipt37.RDIR
RECEIPT = 'verification/receipts/PILOT-SB1.json'
EXEC = 'verification/infrastructure/v3/pilots/PILOT-SB1-execution.md'
ADV = 'verification/infrastructure/v3/pilots/SANDBOX-ADVANCE.md'
ENV = dict(os.environ, GIT_AUTHOR_NAME='sim', GIT_AUTHOR_EMAIL='sim@invalid', GIT_COMMITTER_NAME='sim',
           GIT_COMMITTER_EMAIL='sim@invalid', GIT_AUTHOR_DATE='1700000000 +0000',
           GIT_COMMITTER_DATE='1700000000 +0000')
ok = True


def git(*a, inp=None, env=None):
    p = subprocess.run(['git'] + list(a), cwd=REPO, input=inp, capture_output=True, env=env or ENV)
    if p.returncode:
        raise RuntimeError(' '.join(a) + ': ' + p.stderr.decode())
    return p.stdout.decode().strip()


def blob(path_or_text, text=False):
    return git('hash-object', '-w', '--stdin', inp=(path_or_text if text else open(path_or_text, 'rb').read()))


def tree_with(base_tree, adds):
    with tempfile.TemporaryDirectory() as td:
        env = dict(ENV, GIT_INDEX_FILE=os.path.join(td, 'index'))
        git('read-tree', base_tree, env=env)
        for path, b in adds.items():
            git('update-index', '--add', '--cacheinfo', '100644,%s,%s' % (b, path), env=env)
        return git('write-tree', env=env)


def commit(tree, parents, msg):
    args = ['commit-tree', tree]
    for p in parents:
        args += ['-p', p]
    return git(*args, '-m', msg)


def merge(first, second, msg):
    t = git('merge-tree', '--write-tree', first, second).split('\n')[0]
    return commit(t, [first, second], msg)


def tool(*a):
    p = subprocess.run([sys.executable, 'tools/v3_verifier.py'] + list(a), cwd=REPO, capture_output=True)
    return p.returncode, p.stdout.decode().strip()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


pre = blob(os.path.join(FILES, 'pilot-prereg.md'))
F = commit(tree_with(B + '^{tree}', {RDIR + 'preregistration.md': pre}), [B], 'PILOT-SB1 control plane')
E = commit(tree_with(F + '^{tree}', {EXEC: blob(os.path.join(FILES, 'pilot-execution.md')),
                                     RDIR + 'result.md': blob(os.path.join(FILES, 'pilot-result.md'))}),
           [F], 'PILOT-SB1 execution')
tip0 = B
R1 = merge(tip0, E, 'PILOT-SB1 reconciliation 1')
att = [('owner-designation', 'F', F, 'sim: owner comment designating F'),
       ('check-run', 'F', F, 'sim: workflow run on F'),
       ('owner-designation', 'E', E, 'sim: owner comment designating E'),
       ('check-run', 'E', E, 'sim: workflow run on E')]
r1 = receipt37.build_receipt(REPO, B, F, E, tip0, R1, [R1], att)
Q1 = commit(tree_with(R1 + '^{tree}', {RECEIPT: blob(r1.encode(), text=True)}), [R1], 'PILOT-SB1 receipt 1')
A = commit(tree_with(tip0 + '^{tree}', {ADV: blob(os.path.join(FILES, 'sandbox-advance.md'))}), [tip0],
           'sandbox advance')
T2 = merge(tip0, A, 'Merge sandbox advance')
R2 = merge(T2, Q1, 'PILOT-SB1 reconciliation 2')
r2 = receipt37.build_receipt(REPO, B, F, E, T2, R2, [R1, R2], att)
Q2 = commit(tree_with(R2 + '^{tree}', {RECEIPT: blob(r2.encode(), text=True)}), [R2], 'PILOT-SB1 receipt 2')
for n, v in (('F', F), ('E', E), ('R1', R1), ('Q1', Q1), ('T2', T2), ('R2', R2), ('Q2', Q2)):
    print('      %-3s %s' % (n, v))
print('      receipt blobs: Q1 %s, Q2 %s' % (git('rev-parse', Q1 + ':' + RECEIPT), git('rev-parse', Q2 + ':' + RECEIPT)))

rc, out = tool('--verify-round', Q2)
report('--verify-round Q2: %s' % out.split('\n')[-1], out.split('\n')[-1] == 'VERDICT  HOLDS')
print('\n'.join('      ' + x for x in out.split('\n')[:6]))
rc, out = tool('--verify-round', Q1)
report('--verify-round Q1 (as it stood before the advance): %s' % out.split('\n')[-1], out.split('\n')[-1] == 'VERDICT  HOLDS')
rc, out = tool('--publication', Q2, Q2)
report('--publication Q2 Q2: %s' % out.split('\n')[-1], out.split('\n')[-1] == 'VERDICT  HOLDS')
rc, out = tool('--publication', T2, Q2)
report('--publication T2 Q2 FAILS s10:not-q-itself: %s' % out.split('\n')[0], 'FAILS' in out and 's10:not-q-itself' in out)
rc, out = tool('--publication', Q2, Q1)
report('--publication Q2 Q1 FAILS: %s' % out.split('\n')[0], 'FAILS' in out)
report('Q1 is not an ancestor-free fast-forward of T2 (stale)',
       subprocess.run(['git', 'merge-base', '--is-ancestor', T2, Q1], cwd=REPO).returncode != 0)
report('Q2 fast-forwards T2', subprocess.run(['git', 'merge-base', '--is-ancestor', T2, Q2], cwd=REPO).returncode == 0)
# a countercontrol: a host merge of Q2 into T2 is not a publication
M = merge(T2, Q2, 'host merge')
rc, out = tool('--publication', M, Q2)
report('--publication <host merge of Q2> Q2 FAILS', 'FAILS' in out)
print('ALL SIM CONTROLS PASS' if ok else 'A SIM CONTROL FAILED')
