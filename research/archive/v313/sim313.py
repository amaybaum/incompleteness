#!/usr/bin/env python3
"""Scratch: rehearse V3-13 at D in a throwaway worktree, with every control the preregistration
names that can run locally. Never landed.

Usage: sim313.py <D> <preregistration file>

The stage contents come from the scratch record directory rd/ and payload/; every expected blob is
read back from the preregistration, and a stage whose file does not have its frozen blob fails."""
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/incompleteness'
D, PRE = sys.argv[1], sys.argv[2]
WT = os.path.join(HERE, 'simwt')
RD = 'verification/infrastructure/round-v3-13-retirement/'
P, RECEIPT = RD + 'preregistration.md', 'verification/receipts/V3-13.json'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/infrastructure/round-v3-12-retirement-census/census.json'
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


def last(out):
    return out.split('\n')[-1]


def commit(msg, files=None, delete=()):
    for path, data in (files or {}).items():
        full = os.path.join(WT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'wb') as fh:
            fh.write(data)
        git('add', path)
    for path in delete:
        git('rm', '-r', '-q', path)
    git('commit', '-q', '--allow-empty', '-m', msg)
    return git('rev-parse', 'HEAD').strip()


def blob(path):
    return git('hash-object', '--no-filters', path).strip()


def payload(path):
    return open(os.path.join(HERE, 'payload', path), 'rb').read()


def frozen_blobs(text):
    """Every `path` | `blob` row of the preregistration's tables of stage files."""
    return {m.group(1): m.group(2) for m in re.finditer(
        r'^\| `([^`]+)` \| `([0-9a-f]{40})` \|', text, re.M)}


def receipts(c, want):
    rc, out = py('tools/v3_verifier.py', '--receipts', c)
    report('receipts at %s: %s' % (c[:8], last(out)),
           rc == 0 and last(out) == 'RECEIPTS  %d receipt(s), all hold' % want)


def legacy(c, want_ok=True):
    rc, out = py('tools/legacy_records_check.py', c)
    report('legacy-records at %s: %s' % (c[:8], last(out)), (rc == 0) == want_ok)


def controls(kind, *args, want=0):
    rc, out = py(RD + 'controls.py', kind, '.', *args)
    report('controls %s %s: %s' % (kind, ' '.join(a[:8] for a in args), last(out)),
           last(out).endswith(' %d history site(s)' % want) if kind == 'history'
           else last(out) == 'callers: %d' % want)
    return out


def cheap_checks(stage):
    for t in ('duplicate_check', 'claims_check', 'artifact_placement_check', 'baseline_label_check',
              'ci_gate_presence_test', 'voice_scope_test'):
        rc, out = py('tools/%s.py' % t)
        report('%s %s: exit %d  %s' % (stage, t, rc, last(out)[:60]), rc == 0)


text = open(PRE, encoding='utf-8').read()
pre = text.encode('utf-8')
FB = frozen_blobs(text)
print('frozen: %d stage-file blobs' % len(FB))

if os.path.exists(WT):
    git('worktree', 'remove', '--force', WT, cwd=REPO, check=False)
    shutil.rmtree(WT, ignore_errors=True)
git('worktree', 'add', '-q', '--detach', WT, D, cwd=REPO)
try:
    F = commit('F', {P: pre})
    report('F has one parent, D, and adds the preregistration alone',
           git('rev-parse', F + '^').strip() == D and
           git('diff', '--no-renames', '--name-status', D, F).split() == ['A', P])
    receipts(F, 3)

    # stage 1: the method and the controls, into the record directory
    S1 = commit('stage 1', {RD + n: open(os.path.join(HERE, 'rd', n), 'rb').read()
                            for n in ('retire.py', 'messages.json', 'headers.json', 'controls.py')})
    for n in ('retire.py', 'messages.json', 'headers.json', 'controls.py'):
        report('C1 %s has its frozen blob' % n, blob(RD + n) == FB[RD + n])
    rc, out = py(RD + 'controls.py', '--self-test')
    report('C1 controls self-test: %s' % last(out), rc == 0)
    out = controls('history', S1, want=213)
    out = controls('callers', S1, D, want=1)
    rc, out = py(RD + 'controls.py', 'pc4s', '.', D)
    report('C2 pc4s: %s' % last(out), rc == 0 and last(out) == 'pc4s: 4 predicate(s) all hold; 35 '
           'file(s) read, 34 legacy record(s); 1 directory listing(s); legacy bytes only'
           and 'COUNTERCONTROL  one byte of verification/seals/PC4.json changed: line 17854 FAILS' in out)
    rc, out = py(RD + 'controls.py', 'vacuity', '.', S1, D)
    print('  ' + out.replace('\n', '\n  '))
    report('C2 vacuity: %s' % last(out), rc == 0 and out.count('COUNTERCONTROL') == 3
           and out.count(': 0 occurrence(s)') == 2)

    # stage 2: the guard
    rc, out = py(RD + 'retire.py', GUARD, CENSUS, GUARD, RD + 'messages.json', RD + 'headers.json')
    print('  ' + out.replace('\n', '\n  '))
    report('C2 retire.py exits 0 with no retained predicate missing',
           rc == 0 and 'retained predicates missing: 0' in out and '91 checks remain' in out
           and '1616 predicates retired, 1610 as the census classes them and 6 by the amendment; '
               '2486 retained' in out)
    report('C2 the guard has its frozen blob: %s' % blob(GUARD), blob(GUARD) == FB[GUARD])
    rc, out = py('-m', 'py_compile', GUARD)
    report('C2 the guard compiles', rc == 0)
    git('add', GUARD)
    S2 = commit('stage 2 guard')
    report('C2 stage 2 changes the guard alone',
           git('diff', '--no-renames', '--name-status', S1, S2).split() == ['M', GUARD])
    controls('history', S2, want=0)
    receipts(S2, 3)
    rc, out = py('tools/certificate_verifier.py', '--mode', 'authoritative')
    report('S2 V2 authoritative (still wired): %s' % last(out)[:70], rc == 0)

    # stage 3: legacy-records in, V2 and the control-plane tools out, V3 steps in, one commit
    S3 = commit('stage 3 authority', {p: payload(p) for p in (
        'verification/infrastructure/legacy-records.json', 'tools/legacy_records_check.py',
        'tools/release_gate.py', '.github/workflows/verify.yml')},
        delete=('tools/certificate_verifier.py', 'tools/control_plane_base_check.py',
                'tools/control_plane_lint.py', 'verification/certificates/conformance'))
    for p in ('verification/infrastructure/legacy-records.json', 'tools/legacy_records_check.py',
              'tools/release_gate.py', '.github/workflows/verify.yml'):
        report('C3 %s has its frozen blob' % p, blob(p) == FB[p])
    report('C3 the manifest is byte-identical to V3-12\'s',
           git('rev-parse', S3 + ':verification/infrastructure/legacy-records.json').strip() ==
           git('rev-parse', D + ':verification/infrastructure/round-v3-12-retirement-census/'
               'legacy-records.json').strip())
    legacy(S3)
    legacy(S2, want_ok=False)
    controls('callers', S3, D, want=0)
    controls('history', S3, want=0)
    rc, out = py('tools/v3_verifier.py', '--self-test')
    report('S3 v3 self-test: %s' % last(out), rc == 0)
    rc, out = py('tools/v3_verifier.py', '--corpus')
    report('S3 v3 corpus: %s' % last(out), rc == 0)
    receipts(S3, 3)
    cheap_checks('S3')

    # stage 4: the verifier, its corpus and the specification
    vecs = sorted(os.listdir(os.path.join(HERE, 'payload/verification/infrastructure/v3/conformance')))
    files = {'tools/v3_verifier.py': payload('tools/v3_verifier.py'),
             'verification/infrastructure/v3/architecture.md':
                 payload('verification/infrastructure/v3/architecture.md')}
    files.update({'verification/infrastructure/v3/conformance/' + v:
                  payload('verification/infrastructure/v3/conformance/' + v) for v in vecs})
    S4 = commit('stage 4 verifier', files, delete=(
        'verification/infrastructure/v3/conformance/'
        'g12-reject-execution-changes-legacy-seal-namespace.json',))
    for p in files:
        report('C4 %s has its frozen blob' % p.split('/')[-1], blob(p) == FB[p])
    rc, out = py('tools/v3_verifier.py', '--self-test')
    report('S4 v3 self-test: %s' % last(out), rc == 0)
    rc, out = py('tools/v3_verifier.py', '--corpus')
    report('S4 v3 corpus: %s' % last(out), rc == 0 and '140' in last(out))
    rc, out = py('tools/legacy_records_check.py', '--self-test')
    report('S4 legacy self-test: %s' % last(out), rc == 0)
    controls('callers', S4, D, want=0)
    receipts(S4, 3)
    legacy(S4)

    # stage 5: the documents
    S5 = commit('stage 5 docs', {p: payload(p) for p in ('AGENTS.md', 'verification/README.md')})
    for p in ('AGENTS.md', 'verification/README.md'):
        report('C5 %s has its frozen blob' % p, blob(p) == FB[p])
    rc, out = py(os.path.join(HERE, 'readme_control.py'), GUARD, os.path.join(REPO, 'verification/README.md'),
                 'verification/README.md')
    report('C5 the README surfaces the guard reads: %s' % out.replace('\n', ' | '),
           out.count('affirms=False') == 4)
    receipts(S5, 3)
    legacy(S5)
    cheap_checks('S5')

    E = commit('E', {RD + 'result.md': b'# V3-13 result (rehearsal placeholder)\n'})
    # C9: what the retained predicates require of the edited files
    import ast
    g = ast.parse(open(os.path.join(WT, GUARD), encoding='utf-8').read())
    lits = {n.value for n in ast.walk(g) if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and len(n.value) >= 6}
    rd0 = git('show', D + ':verification/README.md')
    rd1 = open(os.path.join(WT, 'verification/README.md'), encoding='utf-8').read()
    f0, f1 = ' '.join(rd0.split()), ' '.join(rd1.split())
    lost = [s for s in lits if (s in rd0 and s not in rd1) or
            (' '.join(s.split()) in f0 and ' '.join(s.split()) not in f1)]
    report('C9 README: %d guard literals lost; anchor present' % len(lost),
           not lost and '`.github/workflows/verify.yml` runs' in rd1)
    wf = open(os.path.join(WT, '.github/workflows/verify.yml'), encoding='utf-8').read()
    report('C9 workflow: repertoire_lie, no lake build or lake env lean of an OIBridge module',
           'repertoire_lie' in wf and not re.search(r'lake build\s+OIBridge\.', wf)
           and not re.search(r'lake env lean\s+OIBridge/', wf))
    ag = ' '.join(open(os.path.join(WT, 'AGENTS.md'), encoding='utf-8').read().split())
    report('C9 AGENTS: the A.35 heading and the registry sentence',
           '## §A.35 Registry contract for the Lean-to-manuscript census' in ag
           and 'updates the registry in the same commit' in ag)
    report('C9 release gate: lean-manuscript',
           '"lean-manuscript"' in open(os.path.join(WT, 'tools/release_gate.py')).read())
    for c1, c2 in ((D, F), (F, S1), (S1, S2), (S2, S3), (S3, S4), (S4, S5), (S5, E)):
        report('linear: %s is the one parent of %s' % (c1[:8], c2[:8]),
               git('rev-list', '--parents', '-n', '1', c2).split()[1:] == [c1])
    controls('history', E, want=0)
    controls('callers', E, D, want=0)
    legacy(E)
    receipts(E, 3)
    print('  delta(D, E):')
    print('  ' + git('diff', '--no-renames', '--name-status', D, E).strip().replace('\n', '\n  ')
          .replace('verification/certificates/conformance/v2/', 'conformance/v2/'))

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
    report('C7 --verify-round Q: %s' % last(out), last(out) == 'VERDICT  HOLDS')
    receipts(Q, 4)
    legacy(Q)
    # the two immutabilities, after the round: a later commit that rewrites a native record, and one
    # that rewrites a legacy record, each fail their own check and only their own
    X1 = commit('rewrite a native record', {
        'verification/infrastructure/round-v3-12-retirement-census/result.md': b'rewritten\n'})
    rc, out = py('tools/v3_verifier.py', '--receipts', X1)
    report('countercontrol G13: %s' % last(out), rc == 1 and 'g13:record-directory-changed' in out)
    legacy(X1)
    git('checkout', '-q', '--detach', Q)
    X2 = commit('rewrite a legacy record', {
        'verification/seals/PC4.json': b'{}\n'})
    rc, out = py('tools/v3_verifier.py', '--receipts', X2)
    report('countercontrol legacy: receipts still hold: %s' % last(out), rc == 0)
    legacy(X2, want_ok=False)
    git('checkout', '-q', '--detach', LAM)
    r = json.loads(receipt)
    r['execution_delta_digest'] = '0' * 64
    Q2 = commit('Q corrupted', {RECEIPT: (json.dumps(r, indent=1) + '\n').encode()})
    rc, out = py('tools/v3_verifier.py', '--verify-round', Q2)
    report('countercontrol: a corrupted receipt does not hold: %s' % last(out),
           last(out) != 'VERDICT  HOLDS')
finally:
    git('checkout', '-q', '--detach', D, check=False)
    git('worktree', 'remove', '--force', WT, cwd=REPO, check=False)
print('SIMULATION  %s' % ('all as predicted' if ok else 'FAILED'))
sys.exit(0 if ok else 1)
