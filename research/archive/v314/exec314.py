#!/usr/bin/env python3
"""Scratch: execute V3-14's five stages from exact F in the repository, every expected value read
back from the preregistration as it stands at F. Refuses on any mismatch. Never landed.

Usage: exec314.py <F>"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get('EXEC_REPO', '/home/user/incompleteness')
F = sys.argv[1]
RD = 'verification/infrastructure/round-v3-14-retirement/'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/infrastructure/round-v3-12-retirement-census/census.json'
TRAILER = ('\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
           'Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1\n')
V313_S2 = '0811754da89dd5e3674ec913c0c89a24462a88fd'
RETIRE_LINES = (
    'retire: 1616 predicates retired, 1610 as the census classes them and 6 by the amendment; '
    '2486 retained',
    'retire: structural rows: 15 removed with the emptied checks, 85 kept',
    'retire: 2 statement(s) kept inside surviving module-level blocks',
    'retire: 91 checks remain; emptied: R7-ABR, R7-ARCH, R7-BRIDGE, R7-CV1, R7-DILCH, R7-DILMAP, '
    'R7-GR1, R7-GR2, R7-RBR, R7-SI1, R7-SI2, R7-SI3, R7-SRCA, R7-VIS',
    'retire: retained predicates missing: 0')
LOG = open(os.path.join(HERE, 'exec.log'), 'w')


def out(s):
    print(s)
    LOG.write(s + '\n')
    LOG.flush()


def git(*a):
    r = subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True)
    if r.returncode:
        raise SystemExit('git %s: %s' % (a, r.stderr.decode()))
    return r.stdout.decode()


def py(*a):
    r = subprocess.run([sys.executable] + list(a), cwd=REPO, capture_output=True)
    return r.returncode, (r.stdout.decode() + r.stderr.decode()).rstrip('\n')


def refuse(msg):
    out('REFUSED  ' + msg)
    raise SystemExit(1)


def blob(path):
    return git('hash-object', '--no-filters', path).strip()


def write(path, data):
    full = os.path.join(REPO, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'wb') as fh:
        fh.write(data)


def commit(msg, add=(), rm=()):
    for p in add:
        git('add', p)
    for p in rm:
        git('rm', '-r', '-q', p)
    parent = git('rev-parse', 'HEAD').strip()
    git('commit', '-q', '-m', msg + TRAILER)
    c = git('rev-parse', 'HEAD').strip()
    if git('rev-list', '--parents', '-n', '1', c).split()[1:] != [parent]:
        refuse('%s does not have the one parent %s' % (c, parent))
    return c


def check(label, cond, detail=''):
    out('%s  %s%s' % ('PASS' if cond else 'FAIL', label, ('  ' + detail) if detail else ''))
    if not cond:
        refuse(label)


if git('rev-parse', 'HEAD').strip() != F or git('status', '--porcelain').strip():
    refuse('the repository is not clean at F')
text = git('show', F + ':' + RD + 'preregistration.md')
FB = {m.group(1): m.group(2) for m in re.finditer(r'^\| `([^`]+)` \| `([0-9a-f]{40})` \|', text, re.M)}
out('F %s; %d frozen stage-file blobs read from the preregistration at F' % (F, len(FB)))
D = git('rev-parse', F + '^').strip()

# stage 1
names = ('retire.py', 'messages.json', 'headers.json', 'controls.py', 'preserve.py', 'ledger.json')
for n in names:
    write(RD + n, open(os.path.join(HERE, 'rd', n), 'rb').read())
    check('C1 %s has its frozen blob' % n, blob(RD + n) == FB[RD + n], blob(RD + n))
S1 = commit('V3-14 stage 1: the guard transformation, its ledger, the preservation checker and the\n'
            'retirement controls',
            add=[RD + n for n in names])
out('stage 1 = %s' % S1)
rc, o = py(RD + 'controls.py', '--self-test')
check('C1 controls.py --self-test', rc == 0, o.split('\n')[-1])

# stage 2
dguard = os.path.join(HERE, 'exec-d-guard.py')
with open(dguard, 'w', encoding='utf-8') as fh:
    fh.write(git('show', D + ':' + GUARD))
led = os.path.join(HERE, 'exec-ledger.json')
rc, o = py(RD + 'retire.py', GUARD, CENSUS, GUARD, RD + 'messages.json', RD + 'headers.json',
           '--ledger', led)
out('  ' + o.replace('\n', '\n  '))
check('C2 retire.py prints the five frozen lines', rc == 0 and all(x in o.split('\n') for x in RETIRE_LINES))
check('C2 the ledger it writes is ledger.json byte for byte',
      open(led, 'rb').read() == open(os.path.join(REPO, RD + 'ledger.json'), 'rb').read())
check('C2 the guard has its frozen blob', blob(GUARD) == FB[GUARD], blob(GUARD))
rc, _o = py('-m', 'py_compile', GUARD)
check('C2 the guard compiles', rc == 0)
S2 = commit('V3-14 stage 2: the guard, 1,616 predicates retired', add=[GUARD])
out('stage 2 = %s' % S2)
pargs = (dguard, CENSUS, RD + 'ledger.json', GUARD)
rc, o = py(RD + 'preserve.py', *pargs)
out('  ' + o.replace('\n', '\n  '))
check('C2 preserve', rc == 0 and o.split('\n')[-1] == 'preserve: all hold', o.split('\n')[-1])
rc, o = py(RD + 'preserve.py', '--self-test', *pargs)
check('C2 preserve --self-test', rc == 0 and o.split('\n')[-1] == 'preserve: self-test OK'
      and o.count('as required') == 16 and 'NOT AS REQUIRED' not in o, o.split('\n')[-1])
rc, o = py(RD + 'controls.py', 'v313', '.', V313_S2, D)
out('  ' + o.replace('\n', '\n  '))
check('C2 controls v313', rc == 0 and o.split('\n')[-1] ==
      "v313: the checker rejects V3-13's guard, naming all ten sites", o.split('\n')[-1])
for args, want in ((('history', '.', S2), 'history: 56 file(s) run by the probes job (56 named), '
                    '0 history site(s)'),
                   (('history', '.', D), 'history: 56 file(s) run by the probes job (56 named), '
                    '213 history site(s)'),
                   (('pc4s', '.', D), 'pc4s: 4 predicate(s) all hold; 35 file(s) read, 34 legacy '
                    'record(s); 1 directory listing(s); legacy bytes only'),
                   (('vacuity', '.', S2, D), 'vacuity: both predicates hold whatever the rest of '
                    'the 1,610 guard says')):
    rc, o = py(RD + 'controls.py', *args)
    if args[0] in ('pc4s', 'vacuity'):
        out('  ' + o.replace('\n', '\n  '))
    ok = o.split('\n')[-1] == want
    if args[0] == 'pc4s':
        ok &= 'COUNTERCONTROL  one byte of verification/seals/PC4.json changed: line 17854 FAILS' in o
    if args[0] == 'vacuity':
        ok &= o.count('COUNTERCONTROL') == 3 and ': FAILS' in o and o.count(': 0 occurrence(s)') == 2
    check('C2 controls %s %s' % (args[0], ' '.join(a[:8] for a in args[2:])), ok,
          o.split('\n')[-1])

# stage 3
s3 = ('verification/infrastructure/legacy-records.json', 'tools/legacy_records_check.py',
      'tools/release_gate.py', '.github/workflows/verify.yml')
for p in s3:
    write(p, open(os.path.join(HERE, 'payload', p), 'rb').read())
    check('C3 %s has its frozen blob' % p, blob(p) == FB[p], blob(p))
S3 = commit('V3-14 stage 3: legacy-records in, V2 and the control-plane tools out', add=s3,
            rm=('tools/certificate_verifier.py', 'tools/control_plane_base_check.py',
                'tools/control_plane_lint.py', 'verification/certificates/conformance'))
out('stage 3 = %s' % S3)
check('C3 the manifest is byte-identical to V3-12\'s',
      git('rev-parse', S3 + ':' + s3[0]).strip() ==
      git('rev-parse', D + ':verification/infrastructure/round-v3-12-retirement-census/'
          'legacy-records.json').strip())
rc, o = py('tools/legacy_records_check.py', S3)
check('C3 legacy-records at stage 3', rc == 0, o.split('\n')[-1])
rc, o = py('tools/legacy_records_check.py', S2)
check('C3 legacy-records at stage 2 fails, the manifest absent', rc == 1, o.split('\n')[-1])
rc, o = py(RD + 'controls.py', 'callers', '.', S3, D)
check('C3 callers at stage 3', o.split('\n')[-1] == 'callers: 0', o.split('\n')[-1])
for a in ('--self-test', '--corpus'):
    rc, o = py('tools/v3_verifier.py', a)
    check('C3 v3_verifier %s' % a, rc == 0, o.split('\n')[-1])

# stage 4
vd = 'verification/infrastructure/v3/conformance/'
s4 = ['tools/v3_verifier.py', 'verification/infrastructure/v3/architecture.md'] + \
    [vd + v for v in sorted(os.listdir(os.path.join(HERE, 'payload', vd)))]
for p in s4:
    write(p, open(os.path.join(HERE, 'payload', p), 'rb').read())
    check('C4 %s has its frozen blob' % p.split('/')[-1], blob(p) == FB[p], blob(p))
S4 = commit('V3-14 stage 4: G12 restated, G13, the projection retired', add=s4,
            rm=(vd + 'g12-reject-execution-changes-legacy-seal-namespace.json',))
out('stage 4 = %s' % S4)
rc, o = py('tools/v3_verifier.py', '--self-test')
check('C4 v3_verifier --self-test', rc == 0, o.split('\n')[-1])
rc, o = py('tools/v3_verifier.py', '--corpus')
check('C4 v3_verifier --corpus', rc == 0 and 'CORPUS  140 vector(s)' in o, o.split('\n')[-1])
rc, o = py(RD + 'controls.py', 'callers', '.', S4, D)
out('  ' + o.replace('\n', '\n  '))
check('C4 callers at stage 4', o.split('\n')[-1] == 'callers: 0', o.split('\n')[-1])

# stage 5
s5 = ('AGENTS.md', 'verification/README.md')
for p in s5:
    write(p, open(os.path.join(HERE, 'payload', p), 'rb').read())
    check('C5 %s has its frozen blob' % p, blob(p) == FB[p], blob(p))
S5 = commit('V3-14 stage 5: AGENTS.md and the verification README', add=s5)
out('stage 5 = %s' % S5)

# C6 at every stage commit
for label, c in (('stage 1', S1), ('stage 2', S2), ('stage 3', S3), ('stage 4', S4), ('stage 5', S5)):
    rc, o = py('tools/v3_verifier.py', '--receipts', c)
    check('C6 receipts at %s' % label, rc == 0 and o.split('\n')[-1] ==
          'RECEIPTS  4 receipt(s), all hold', o.split('\n')[-1])
    if label in ('stage 3', 'stage 4', 'stage 5'):
        rc, o = py('tools/legacy_records_check.py', c)
        check('C6 legacy-records at %s' % label, rc == 0, o.split('\n')[-1])
for t in ('duplicate_check', 'claims_check', 'artifact_placement_check', 'baseline_label_check',
          'ci_gate_presence_test', 'voice_scope_test'):
    rc, o = py('tools/%s.py' % t)
    check('stage 5 %s' % t, rc == 0, o.split('\n')[-1][:70])
out('STAGES  %s %s %s %s %s' % (S1, S2, S3, S4, S5))
