#!/usr/bin/env python3
"""Scratch: rehearse V3-14 at D in a throwaway worktree, with every control the preregistration
names that can run locally. Never landed.

Usage: sim314.py <D> <preregistration file>

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
sys.path.insert(0, os.path.join(REPO, 'tools'))
import v3_verifier as v3  # noqa: E402

D, PRE = sys.argv[1], sys.argv[2]
WT = os.path.join(HERE, 'simwt')
RD = 'verification/infrastructure/round-v3-14-retirement/'
P, RECEIPT = RD + 'preregistration.md', 'verification/receipts/V3-14.json'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/infrastructure/round-v3-12-retirement-census/census.json'
V313_S2 = '0811754da89dd5e3674ec913c0c89a24462a88fd'
REHEARSAL_TREE = 'a31642acd97065d990c28d2b5a01e30501da452b'
RDFILES = ('retire.py', 'messages.json', 'headers.json', 'controls.py', 'preserve.py', 'ledger.json')
RETIRE_LINES = (
    'retire: 1616 predicates retired, 1610 as the census classes them and 6 by the amendment; '
    '2486 retained',
    'retire: structural rows: 15 removed with the emptied checks, 85 kept',
    'retire: 2 statement(s) kept inside surviving module-level blocks',
    'retire: 91 checks remain; emptied: R7-ABR, R7-ARCH, R7-BRIDGE, R7-CV1, R7-DILCH, R7-DILMAP, '
    'R7-GR1, R7-GR2, R7-RBR, R7-SI1, R7-SI2, R7-SI3, R7-SRCA, R7-VIS',
    'retire: retained predicates missing: 0')
ENV = dict(os.environ, GIT_AUTHOR_NAME='sim', GIT_AUTHOR_EMAIL='sim@invalid', GIT_COMMITTER_NAME='sim',
           GIT_COMMITTER_EMAIL='sim@invalid', GIT_AUTHOR_DATE='1700000000 +0000',
           GIT_COMMITTER_DATE='1700000000 +0000')
ok = True


def git(*a, cwd=WT, check=True, env=None):
    r = subprocess.run(['git'] + list(a), cwd=cwd, env=env or ENV, capture_output=True)
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
    return {m.group(1): m.group(2) for m in re.finditer(
        r'^\| `([^`]+)` \| `([0-9a-f]{40})` \|', text, re.M)}


def receipts(c, want):
    rc, out = py('tools/v3_verifier.py', '--receipts', c)
    report('C6 receipts at %s: %s' % (c[:8], last(out)),
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


def tree_without(c, paths):
    idx = os.path.join(HERE, 'sim.index')
    env = dict(ENV, GIT_INDEX_FILE=idx)
    git('read-tree', c, env=env)
    git('rm', '-q', '--cached', *paths, env=env)
    t = git('write-tree', env=env).strip()
    os.unlink(idx)
    return t


text = open(PRE, encoding='utf-8').read()
pre = text.encode('utf-8')
FB = frozen_blobs(text)
print('frozen: %d stage-file blobs' % len(FB))
report('the preregistration has no unfilled placeholder', '{{' not in text)

if os.path.exists(WT):
    git('worktree', 'remove', '--force', WT, cwd=REPO, check=False)
    shutil.rmtree(WT, ignore_errors=True)
git('worktree', 'add', '-q', '--detach', WT, D, cwd=REPO)
try:
    F = commit('F', {P: pre})
    report('F has one parent, D, and adds the preregistration alone',
           git('rev-parse', F + '^').strip() == D and
           git('diff', '--no-renames', '--name-status', D, F).split() == ['A', P])
    receipts(F, 4)
    entries = v3.parse_governed_text(text)

    # stage 1: the method, the ledger, the checker and the controls, into the record directory
    S1 = commit('stage 1', {RD + n: open(os.path.join(HERE, 'rd', n), 'rb').read() for n in RDFILES})
    for n in RDFILES:
        report('C1 %s has its frozen blob' % n, blob(RD + n) == FB[RD + n])
    rc, out = py(RD + 'controls.py', '--self-test')
    report('C1 controls self-test: %s' % last(out), rc == 0)
    controls('history', S1, want=213)
    controls('callers', S1, D, want=1)

    # stage 2: the guard
    led = os.path.join(HERE, 'sim-ledger.json')
    rc, out = py(RD + 'retire.py', GUARD, CENSUS, GUARD, RD + 'messages.json', RD + 'headers.json',
                 '--ledger', led)
    print('  ' + out.replace('\n', '\n  '))
    lines = out.split('\n')
    report('C2 retire.py exits 0 printing the five frozen lines',
           rc == 0 and all(x in lines for x in RETIRE_LINES))
    report('C2 the ledger it writes is ledger.json byte for byte',
           open(led, 'rb').read() == open(os.path.join(WT, RD + 'ledger.json'), 'rb').read())
    report('C2 the guard has its frozen blob: %s' % blob(GUARD), blob(GUARD) == FB[GUARD])
    rc, out = py('-m', 'py_compile', GUARD)
    report('C2 the guard compiles', rc == 0)
    git('add', GUARD)
    S2 = commit('stage 2 guard')
    report('C2 stage 2 changes the guard alone',
           git('diff', '--no-renames', '--name-status', S1, S2).split() == ['M', GUARD])
    d_guard = os.path.join(HERE, 'sim-d-guard.py')
    with open(d_guard, 'wb') as fh:
        fh.write(subprocess.run(['git', 'show', D + ':' + GUARD], cwd=WT, capture_output=True).stdout)
    args = (d_guard, CENSUS, RD + 'ledger.json', GUARD)
    rc, out = py(RD + 'preserve.py', *args)
    print('  ' + out.replace('\n', '\n  '))
    report('C2 preserve: %s' % last(out), rc == 0 and last(out) == 'preserve: all hold')
    rc, out = py(RD + 'preserve.py', '--self-test', *args)
    report('C2 preserve --self-test: %s (%d mutants as required)'
           % (last(out), out.count('as required')),
           rc == 0 and last(out) == 'preserve: self-test OK' and out.count('as required') == 16)
    rc, out = py(RD + 'controls.py', 'v313', '.', V313_S2, D)
    print('  ' + out.replace('\n', '\n  '))
    report('C2 v313: %s' % last(out), rc == 0 and
           last(out) == 'v313: the checker rejects V3-13\'s guard, naming all ten sites')
    controls('history', S2, want=0)
    controls('history', D, want=213)
    rc, out = py(RD + 'controls.py', 'pc4s', '.', D)
    report('C2 pc4s: %s' % last(out), rc == 0 and last(out) == 'pc4s: 4 predicate(s) all hold; 35 '
           'file(s) read, 34 legacy record(s); 1 directory listing(s); legacy bytes only'
           and 'COUNTERCONTROL  one byte of verification/seals/PC4.json changed: line 17854 FAILS' in out)
    rc, out = py(RD + 'controls.py', 'vacuity', '.', S2, D)
    print('  ' + out.replace('\n', '\n  '))
    report('C2 vacuity: %s' % last(out), rc == 0 and last(out) == 'vacuity: both predicates hold '
           'whatever the rest of the 1,610 guard says' and out.count('COUNTERCONTROL') == 3
           and out.count(': 0 occurrence(s)') == 2)
    receipts(S2, 4)

    # stage 3
    s3 = ('verification/infrastructure/legacy-records.json', 'tools/legacy_records_check.py',
          'tools/release_gate.py', '.github/workflows/verify.yml')
    S3 = commit('stage 3 authority', {p: payload(p) for p in s3},
                delete=('tools/certificate_verifier.py', 'tools/control_plane_base_check.py',
                        'tools/control_plane_lint.py', 'verification/certificates/conformance'))
    for p in s3:
        report('C3 %s has its frozen blob' % p, blob(p) == FB[p])
    report('C3 the manifest is byte-identical to V3-12\'s',
           git('rev-parse', S3 + ':' + s3[0]).strip() ==
           git('rev-parse', D + ':verification/infrastructure/round-v3-12-retirement-census/'
               'legacy-records.json').strip())
    legacy(S3)
    legacy(S2, want_ok=False)
    controls('callers', S3, D, want=0)
    controls('history', S3, want=0)
    for a in ('--self-test', '--corpus'):
        rc, out = py('tools/v3_verifier.py', a)
        report('C3 v3 %s: %s' % (a, last(out)), rc == 0)
    receipts(S3, 4)
    cheap_checks('S3')

    # stage 4
    vd = 'verification/infrastructure/v3/conformance/'
    files = {p: payload(p) for p in ('tools/v3_verifier.py',
                                     'verification/infrastructure/v3/architecture.md')}
    files.update({vd + v: payload(vd + v)
                  for v in sorted(os.listdir(os.path.join(HERE, 'payload', vd)))})
    S4 = commit('stage 4 verifier', files,
                delete=(vd + 'g12-reject-execution-changes-legacy-seal-namespace.json',))
    for p in files:
        report('C4 %s has its frozen blob' % p.split('/')[-1], blob(p) == FB[p])
    rc, out = py('tools/v3_verifier.py', '--self-test')
    report('C4 v3 self-test: %s' % last(out), rc == 0)
    rc, out = py('tools/v3_verifier.py', '--corpus')
    report('C4 v3 corpus: %s' % last(out), rc == 0 and 'CORPUS  140 vector(s)' in out)
    rc, out = py('tools/legacy_records_check.py', '--self-test')
    report('S4 legacy self-test: %s' % last(out), rc == 0)
    controls('callers', S4, D, want=0)
    receipts(S4, 4)
    legacy(S4)

    # stage 5
    s5 = ('AGENTS.md', 'verification/README.md')
    S5 = commit('stage 5 docs', {p: payload(p) for p in s5})
    for p in s5:
        report('C5 %s has its frozen blob' % p, blob(p) == FB[p])
    rc, out = py(os.path.join(HERE, 'readme_control.py'), GUARD,
                 os.path.join(WT, 'verification/README.md'), 'verification/README.md')
    report('C9 the README surfaces the guard reads: %s' % out.replace('\n', ' | '),
           out.count('affirms=False') == 4)
    receipts(S5, 4)
    legacy(S5)
    cheap_checks('S5')

    E = commit('E', {RD + 'result.md': b'# V3-14 result (rehearsal placeholder)\n'})
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
    receipts(E, 4)
    # C7: every path of delta(D, E) governed, and none in the legacy population
    man = json.loads(git('show', D + ':verification/infrastructure/round-v3-12-retirement-census/'
                         'legacy-records.json'))
    delta = [l.split('\t') for l in git('diff', '--no-renames', '--name-status', D, E).strip().split('\n')]
    ungoverned = [p for _s, p in delta if v3.governing(entries, p.encode()) is None]
    legacy_hit = [p for _s, p in delta if p in man['records']]
    report('C7 delta(D, E): %d path(s), %d ungoverned, %d in the legacy population'
           % (len(delta), len(ungoverned), len(legacy_hit)), not ungoverned and not legacy_hit)
    # C11: E is the rehearsal tree plus the preregistration and the result note
    t = tree_without(E, [P, RD + 'result.md'])
    report('C11 tree(E) less the preregistration and the result note: %s' % t, t == REHEARSAL_TREE)

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
    report('C10 --verify-round Q: %s' % last(out), last(out) == 'VERDICT  HOLDS')
    receipts(Q, 5)
    legacy(Q)
    X1 = commit('rewrite a native record', {
        'verification/infrastructure/round-v3-13-retirement/result.md': b'rewritten\n'})
    rc, out = py('tools/v3_verifier.py', '--receipts', X1)
    report('countercontrol G13 (V3-13 record rewritten): %s' % last(out),
           rc == 1 and 'g13:record-directory-changed' in out)
    legacy(X1)
    git('checkout', '-q', '--detach', Q)
    X2 = commit('rewrite a legacy record', {'verification/seals/PC4.json': b'{}\n'})
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
