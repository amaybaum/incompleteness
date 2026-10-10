#!/usr/bin/env python3
"""Scratch: rehearse V3-12 at D in a throwaway worktree, with every control the preregistration
names that can run locally. Never landed. Usage: sim312.py <D> <preregistration file> <census.py>"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/incompleteness'
D, PRE, TOOL = sys.argv[1], sys.argv[2], sys.argv[3]
WT = os.path.join(HERE, 'wt')
RD = 'verification/infrastructure/round-v3-12-retirement-census/'
P, RECEIPT = RD + 'preregistration.md', 'verification/receipts/V3-12.json'
ENV = dict(os.environ, GIT_AUTHOR_NAME='sim', GIT_AUTHOR_EMAIL='sim@invalid', GIT_COMMITTER_NAME='sim',
           GIT_COMMITTER_EMAIL='sim@invalid', GIT_AUTHOR_DATE='1700000000 +0000',
           GIT_COMMITTER_DATE='1700000000 +0000')
ok = True


def git(*a, cwd=WT, check=True):
    r = subprocess.run(['git'] + list(a), cwd=cwd, env=ENV, capture_output=True)
    if check and r.returncode:
        raise SystemExit('git %s: %s' % (a, r.stderr.decode()))
    return r.stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def py(*a, cwd=WT):
    r = subprocess.run([sys.executable] + list(a), cwd=cwd, capture_output=True)
    return r.returncode, (r.stdout.decode() + r.stderr.decode()).rstrip('\n')


def commit(msg, files):
    for path, data in files.items():
        full = os.path.join(WT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'wb') as fh:
            fh.write(data)
        git('add', path)
    git('commit', '-q', '-m', msg)
    return git('rev-parse', 'HEAD').strip()


def blob(path):
    return git('hash-object', '--no-filters', path).strip()


def cheap_checks(stage):
    for t in ('control_plane_lint', 'duplicate_check', 'claims_check', 'artifact_placement_check',
              'baseline_label_check'):
        rc, out = py('tools/%s.py' % t)
        report('%s %s: exit %d  %s' % (stage, t, rc, out.split('\n')[-1][:70]), rc == 0)


pre = open(PRE, 'rb').read()
text = pre.decode('utf-8')
# the frozen values, read back from the preregistration
tool_blob = re.search(r'adds `census\.py` to the record directory, blob\s+`([0-9a-f]{40})`', text).group(1)
tool_sha = re.search(r'SHA-256\s+`([0-9a-f]{64})`', text).group(1)
cen_blob = re.search(r'`census\.json`, blob `([0-9a-f]{40})`', text).group(1)
leg_blob = re.search(r'`legacy-records\.json`, blob\s+`([0-9a-f]{40})`', text).group(1)
selftest = re.search(r'`census\.py --self-test` prints `([^`]+)`', text).group(1)
print('frozen: tool %s / %s, census %s, records %s, self-test %r' % (tool_blob[:12], tool_sha[:12],
                                                                     cen_blob[:12], leg_blob[:12], selftest))

if os.path.exists(WT):
    git('worktree', 'remove', '--force', WT, cwd=REPO, check=False)
    shutil.rmtree(WT, ignore_errors=True)
git('worktree', 'add', '-q', '--detach', WT, D, cwd=REPO)
try:
    F = commit('F', {P: pre})
    report('F has one parent, D, and adds the preregistration alone',
           git('rev-parse', F + '^') .strip() == D and
           git('diff', '--no-renames', '--name-status', D, F).split() == ['A', P])
    cheap_checks('F')

    tool = open(TOOL, 'rb').read()
    S1 = commit('stage 1', {RD + 'census.py': tool})
    report('C1 census.py has the frozen blob and SHA-256',
           blob(RD + 'census.py') == tool_blob and hashlib.sha256(tool).hexdigest() == tool_sha)
    rc, out = py(RD + 'census.py', '--self-test')
    report('C2 self-test: %s' % out.split('\n')[-1], rc == 0 and out.split('\n')[-1] == selftest)

    rc, out = py(RD + 'census.py', '.', D, RD)
    report('the census runs at the stage 1 commit: exit %d' % rc, rc == 0)
    print(out)
    report('C3 the outputs have the predicted blobs',
           blob(RD + 'census.json') == cen_blob and blob(RD + 'legacy-records.json') == leg_blob)
    scratch = os.path.join(HERE, 'sim-rerun')
    shutil.rmtree(scratch, ignore_errors=True)
    rc2, _ = py(RD + 'census.py', '.', D, scratch)
    same = all(open(os.path.join(scratch, n), 'rb').read() == open(os.path.join(WT, RD, n), 'rb').read()
               for n in ('census.json', 'legacy-records.json'))
    report('C3 a second run at D gives the same bytes', rc2 == 0 and same)
    c = json.load(open(os.path.join(WT, RD, 'census.json')))
    lr = json.load(open(os.path.join(WT, RD, 'legacy-records.json')))
    report('C4 figures: %d predicates %s %s, %d writes, %d V2 pins; %d records, %d namespaces'
           % (len(c['predicates']), c['guard']['totals'], c['guard']['dispositions'],
              c['guard']['accumulator_writes'], c['legacy_records']['v2_pins_agreeing'],
              len(lr['records']), len(lr['closed_namespaces'])),
           len(c['predicates']) == 4202 and c['guard']['accumulator_writes'] == 4199
           and c['legacy_records']['v2_pins_agreeing'] == 199 and len(lr['records']) == 303
           and len(lr['closed_namespaces']) == 75
           and c['guard']['dispositions'] == {'removed whole': 14, 'retained whole': 50, 'split': 41}
           and c['guard']['totals'] == {'redundant': 1268, 'retain': 2492, 'retire-history': 291,
                                        'retire-machinery': 49, 'retire-whole': 2, 'structural': 100})
    git('add', RD + 'census.json', RD + 'legacy-records.json')
    git('commit', '-q', '-m', 'stage 2')
    S2 = git('rev-parse', 'HEAD').strip()

    E = commit('E', {RD + 'result.md': b'# V3-12 result (rehearsal placeholder)\n'})
    st = git('diff', '--no-renames', '--name-status', D, E).split('\n')
    st = [x.split('\t') for x in st if x]
    report('C5 delta(D, E) is %d additions under the record directory' % len(st),
           all(s == 'A' and p.startswith(RD) for s, p in st) and len(st) == 5)
    cheap_checks('E')
    for c1, c2 in ((D, F), (F, S1), (S1, S2), (S2, E)):
        report('linear: %s is the one parent of %s' % (c1[:8], c2[:8]),
               git('rev-list', '--parents', '-n', '1', c2).split()[1:] == [c1])

    LAM = git('commit-tree', E + '^{tree}', '-p', D, '-p', E, '-m', 'reconcile').strip()
    git('checkout', '-q', '--detach', LAM)
    att = []
    for s in ('F', 'E'):
        att += ['--attest', 'owner-designation', s, 'rehearsal', '--attest', 'check-run', s, 'rehearsal']
    rc, receipt = py('tools/v3_receipt.py', '--status', 'complete', '--d', D, '--f', F, '--e', E,
                     '--reconciliation', LAM, *att)
    report('the builder exits 0', rc == 0)
    Q = commit('Q', {RECEIPT: (receipt + '\n').encode()})
    rc, out = py('tools/v3_verifier.py', '--verify-round', Q)
    report('C7 --verify-round Q: %s' % out.split('\n')[-1], out.split('\n')[-1] == 'VERDICT  HOLDS')
    rc, out = py('tools/v3_verifier.py', '--receipts', Q)
    report('C7 --receipts Q: exit %d, %s' % (rc, out.split('\n')[-1]),
           rc == 0 and out.split('\n')[-1] == 'RECEIPTS  3 receipt(s), all hold')
    git('checkout', '-q', '--detach', LAM)
    r = json.loads(receipt)
    r['execution_delta_digest'] = '0' * 64
    Q2 = commit('Q corrupted', {RECEIPT: (json.dumps(r, indent=1) + '\n').encode()})
    rc, out = py('tools/v3_verifier.py', '--verify-round', Q2)
    report('countercontrol: a corrupted receipt does not hold: %s' % out.split('\n')[-1],
           out.split('\n')[-1] != 'VERDICT  HOLDS')
finally:
    git('checkout', '-q', '--detach', D, check=False)
    git('worktree', 'remove', '--force', WT, cwd=REPO, check=False)
print('SIMULATION  %s' % ('all as predicted' if ok else 'FAILED'))
sys.exit(0 if ok else 1)
