#!/usr/bin/env python3
"""Scratch: render the V3-10 preregistration and rehearse the native lifecycle at D in a throwaway
worktree. Never landed. Usage: pilot10.py <D> <out preregistration path or ->"""
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/incompleteness'
D, OUT = sys.argv[1], sys.argv[2]
WT = os.path.join(HERE, 'wt')
RD = 'verification/infrastructure/round-v3-10-native-pilot/'
P, README, RECEIPT = RD + 'preregistration.md', 'verification/README.md', 'verification/receipts/V3-10.json'
ENV = dict(os.environ, GIT_AUTHOR_NAME='sim', GIT_AUTHOR_EMAIL='sim@invalid', GIT_COMMITTER_NAME='sim',
           GIT_COMMITTER_EMAIL='sim@invalid', GIT_AUTHOR_DATE='1700000000 +0000',
           GIT_COMMITTER_DATE='1700000000 +0000')
ok = True


def git(*a, cwd=WT, data=None):
    return subprocess.run(['git'] + list(a), cwd=cwd, env=ENV, input=data, capture_output=True,
                          check=True).stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def blob(s):
    return git('hash-object', '--stdin', data=s.encode(), cwd=REPO).strip()


rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()
readme_d = git('show', '%s:%s' % (D, README), cwd=REPO)
lines = readme_d.split('\n')
old = '\n'.join(lines[-3:-1]) + '\n'
assert readme_d.endswith(old) and readme_d.count(old) == 1 and lines[-2].startswith('as an exact set;')
new = lines[-3] + '\n\n' + rd('readme_new.txt')
readme_e = readme_d[:-len(old)] + new
t = rd('prereg-template.md')
for k, v in {'{{BLOB:readme_d}}': blob(readme_d), '{{BLOB:readme_e}}': blob(readme_e),
             '{{README_OLD}}': old, '{{README_NEW}}': new}.items():
    t = t.replace(k, v)
assert '{{' not in t
if OUT != '-':
    open(OUT, 'w', encoding='utf-8').write(t)
print('README blob at D %s, after %s' % (blob(readme_d), blob(readme_e)))

if os.path.exists(WT):
    subprocess.run(['git', 'worktree', 'remove', '--force', WT], cwd=REPO)
    shutil.rmtree(WT, ignore_errors=True)
subprocess.run(['git', 'worktree', 'prune'], cwd=REPO, check=True)
git('worktree', 'add', '--detach', WT, D, cwd=REPO)


def commit(msg, files):
    for path, text in files.items():
        full = os.path.join(WT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, 'w', encoding='utf-8').write(text)
        git('add', path)
    git('commit', '-q', '-m', msg)
    return git('rev-parse', 'HEAD').strip()


F = commit('F', {P: t})
E1 = commit('E1', {README: readme_e})
E = commit('E', {RD + 'result.md': '# V3-10 result (rehearsal placeholder)\n'})
report('README blob after the execution is the predicted one',
       git('rev-parse', 'HEAD:' + README).strip() == blob(readme_e))
LAM = git('commit-tree', E + '^{tree}', '-p', D, '-p', E, '-m', 'reconcile').strip()
git('checkout', '-q', '--detach', LAM)
att = ['--attest', 'owner-designation', 'F', 'rehearsal: F designation',
       '--attest', 'check-run', 'F', 'rehearsal: F dispatch run',
       '--attest', 'owner-designation', 'E', 'rehearsal: E designation',
       '--attest', 'check-run', 'E', 'rehearsal: E dispatch run']
cli = subprocess.run([sys.executable, 'tools/v3_receipt.py', '--status', 'complete', '--d', D, '--f', F,
                      '--e', E, '--reconciliation', LAM] + att, cwd=WT, capture_output=True)
report('the builder exits 0', cli.returncode == 0)
receipt = cli.stdout.decode()
r = json.loads(receipt)
print('receipt: round %s kind %s status %s, %d attestation(s)' % (r['round'], r['kind'], r['status'], len(r['attestations'])))
Q = commit('Q', {RECEIPT: receipt})
report('Q is a single-parent child of Λ', git('rev-list', '--parents', '-n', '1', Q).split()[1:] == [LAM])
v = subprocess.run([sys.executable, 'tools/v3_verifier.py', '--verify-round', Q], cwd=WT, capture_output=True)
out = v.stdout.decode().strip().split('\n')
print('\n'.join('      ' + x for x in out))
report('--verify-round Q: %s' % out[-1], out[-1] == 'VERDICT  HOLDS')
git('checkout', '-q', '--detach', LAM)
r['execution_delta_digest'] = '0' * 64
Q2 = commit('Q corrupted', {RECEIPT: json.dumps(r, indent=1) + '\n'})
v = subprocess.run([sys.executable, 'tools/v3_verifier.py', '--verify-round', Q2], cwd=WT, capture_output=True)
last = v.stdout.decode().strip().split('\n')[-1]
report('control, execution delta digest zeroed: %s' % last, last.startswith('VERDICT  FAILS'))
d = git('diff', '--no-renames', '--name-status', D, Q).split('\n')
print('delta(D, Q):', [x for x in d if x])
report('delta(D, Q) is the governed set', sorted(x for x in d if x) == sorted(
    ['A\t' + P, 'M\t' + README, 'A\t' + RD + 'result.md', 'A\t' + RECEIPT]))
print('ALL REHEARSAL CHECKS PASS' if ok else 'A REHEARSAL CHECK FAILED')
