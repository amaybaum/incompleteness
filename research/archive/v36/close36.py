#!/usr/bin/env python3
"""Scratch: V3-6 closing controls at the stage-3 commit (C3, C4, C5, C6, scope, chronology).
Never landed. Every tool run is the committed repository tool, run from the repository.

Usage: close36.py <stage-3 commit>"""
import json
import os
import subprocess
import sys
import types

REPO = '/home/user/incompleteness'
B = 'bace2e070c6e621c3314b9363ea56314b414f736'
S3 = sys.argv[1]
TOOL = 'tools/v3_verifier.py'
CONF = 'verification/infrastructure/v3/conformance/'
ok = True


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, check=True).stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def load(name, text):
    m = types.ModuleType(name)
    m.__file__ = os.path.join(REPO, TOOL)
    exec(compile(text, name, 'exec'), m.__dict__)
    return m


def sub(s, old, new):
    assert s.count(old) == 1, (old[:70], s.count(old))
    return s.replace(old, new)


# the smallest change that makes each rule inert, applied to the committed text
REMOVE = {
    'nearmiss': [("""        if has_near_miss(t):
            return None, None, None, None, files, codes + ['t1:near-miss']
""", "")],
    'g12entry': [("""            if kind != 'non-sealing' and p == seal and ops == 'A':
                continue
            codes.append(fam + ':record-entry-outside-own-record')
    if kind == 'sealing' and ('record', 'A', seal) not in entries:
        codes.append(fam + ':seal-record-entry')""", """            if p.endswith('/') or kind == 'non-sealing':
                codes.append(fam + ':record-entry-outside-own-record')""")],
    'g12receipt': [("""        if ok and isinstance(r.get('round'), str):
            ok = ps == [seal_record_path(r['round']).encode()]
""", "")],
    'g12others': [("""    if foreign(own, path):
        return False
""", "")],
    'g12qdelta': [("""
            elif not all(authorized(entries, x[0], x[1], own) for x in repo.delta(rc, prev_q)):
                codes.append('s10:receipt-commit-unauthorized')""", ""),
                  ("""
    elif not all(authorized(entries, x[0], x[1], own) for x in repo.delta(lam, q)):
        codes.append('s10:receipt-commit-unauthorized')""", "")],
}
OWNER = {'nearmiss': ['g10-reject-indented-opener', 'g10-reject-longer-backtick-fence',
                      'g10-reject-near-miss-in-amendment', 'g10-reject-opener-with-cr',
                      'g10-reject-opener-with-trailing-text', 'g10-reject-tilde-fence'],
         'g12entry': ['g12-reject-seal-entry-in-legacy-namespace',
                      'g12-reject-seal-entry-names-another-rounds-receipt',
                      'g12-reject-seal-entry-not-add-only', 'g12-reject-seal-entry-not-at-fixed-path',
                      'g12-reject-sealing-round-without-seal-entry'],
         'g12receipt': ['g12-reject-receipt-names-second-seal-record',
                        'g12-reject-receipt-seal-path-not-fixed'],
         'g12others': ['g12-reject-execution-changes-another-rounds-receipt',
                       'g12-reject-execution-changes-another-rounds-seal-record',
                       'g12-reject-execution-changes-legacy-seal-namespace'],
         'g12qdelta': ['g12-reject-seal-record-path-already-present']}

src = git('show', '%s:%s' % (S3, TOOL))
assert src == open(os.path.join(REPO, TOOL), encoding='utf-8').read()
names = sorted(n for n in os.listdir(os.path.join(REPO, CONF)) if n.endswith('.json'))
ALL = {n[:-5]: json.load(open(os.path.join(REPO, CONF, n), encoding='utf-8')) for n in names}


def run(tool):
    return {v: tool.run_vector(x, REPO)[0] for v, x in ALL.items()}


base = run(load('e', src))
report('C1 at the stage-3 tool: %d vectors, all as expected' % len(ALL), len(ALL) == 133 and all(base.values()))
for rule, edits in REMOVE.items():
    s = src
    for old, new in edits:
        s = sub(s, old, new)
    r = run(load('minus-' + rule, s))
    own = OWNER[rule]
    report('C3 rule %-10s out: its %d vector(s) not as expected, the other %d as expected'
           % (rule, len(own), len(ALL) - len(own)),
           not any(r[v] for v in own) and all(r[v] for v in ALL if v not in own))
# stage granularity: revert each stage's frozen sites, read back from the preregistration at B
import re  # noqa: E402
pre = git('show', '%s:verification/infrastructure/round-v3-6-final-conformance/preregistration.md' % B)
pat = re.compile(r'#### Site `(s(\d)\.\d+)`\n\nThe site:\n\n```text\n(.*?)\n```\n\n'
                 r'The drafting-time replacement \(a prediction\):\n\n```text\n(.*?)\n```', re.S)
sites = pat.findall(pre)
for n, own in ((1, OWNER['nearmiss']), (2, sum((OWNER[k] for k in OWNER if k != 'nearmiss'), []))):
    s = src
    for sid, st, old, new in sites:
        if int(st) == n:
            s = sub(s, new, old)
    r = run(load('minus-stage%d' % n, s))
    report('C3 stage %d reverted: its %d vector(s) not as expected, the other %d as expected'
           % (n, len(own), len(ALL) - len(own)),
           not any(r[v] for v in own) and all(r[v] for v in ALL if v not in own))

btool = os.path.join('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v36',
                     'v3_verifier_at_B.py')
open(btool, 'w', encoding='utf-8').write(git('show', '%s:%s' % (B, TOOL)))
pb = subprocess.run([sys.executable, btool, '--project', B], cwd=REPO, capture_output=True).stdout
pe = subprocess.run([sys.executable, TOOL, '--project', B], cwd=REPO, capture_output=True).stdout
import hashlib  # noqa: E402
report('C4 --project over B: identical to the tool at B (%d lines, sha256 %s)'
       % (pe.count(b'\n'), hashlib.sha256(pe).hexdigest()), pe == pb and pe)

p = subprocess.run([sys.executable, TOOL, '--mode', 'shadow', '--subject', S3], cwd=REPO, capture_output=True)
lines = p.stdout.decode().rstrip('\n').split('\n')
rules = [ln[2:6].strip() for ln in lines if ln.startswith('  ') and ln[2:3] in 'KG']
report('C5 exit 0', p.returncode == 0)
report('C5 banner', lines[0] == 'v3_verifier shadow report -- SHADOW ONLY: this report gates nothing; '
       'V1 and V2 remain authoritative')
report('C5 rules %s' % ' '.join(rules),
       rules == ['K1', 'K2', 'K3', 'K4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12'])
report('C5 corpus line', 'CORPUS  133 vector(s), exact and as expected' in lines)
report('C5 projection line', 'PROJECTION  cells 126' in lines)
report('C5 last line', lines[-1] == 'v3_verifier: shadow report complete (corpus as expected)')
readme = git('show', '%s:verification/README.md' % S3)
for s in ('conformance-pending', 'does not implement', 'remain unsettled'):
    report('C5 %r absent from the tool and the README' % s, s not in src.lower() and s not in readme.lower())
new_para = re.search(r'The paragraph at `E`:\n\n```text\n(.*?)\n```', pre, re.S).group(1)
report('C5 README paragraph is the frozen text', readme.count(new_para + '\n') == 1)
st = subprocess.run([sys.executable, TOOL, '--self-test'], cwd=REPO, capture_output=True)
report('C6 %s' % st.stdout.decode().strip(), st.returncode == 0)

# chronology and scope from B
revs = git('rev-list', '--reverse', '%s..%s' % (B, S3)).split()
chron = all(len(git('rev-list', '--parents', '-n', '1', c).split()) == 2 for c in revs) \
    and git('rev-list', '--parents', '-n', '1', revs[0]).split()[1] == B
report('chronology: %d commits after B, each one parent, the oldest on B' % len(revs), chron)
for path in ('.github/workflows/verify.yml', 'tools/release_gate.py', 'tools/certificate_verifier.py',
             'verification/lean/edge_rigidity_probe.py', 'AGENTS.md',
             'verification/infrastructure/v3/architecture.md',
             'verification/infrastructure/round-v3-6-final-conformance/preregistration.md'):
    report('unchanged from B: %s' % path, git('rev-parse', '%s:%s' % (B, path)) == git('rev-parse', '%s:%s' % (S3, path)))
report('no verification/receipts/, verification/v3-seals/; verification/seals/ unchanged',
       not git('ls-tree', '-d', '--name-only', S3, 'verification/receipts', 'verification/v3-seals').strip()
       and not git('diff', '--name-only', B, S3, '--', 'verification/seals/').strip())
print(git('diff', '--no-renames', '--name-status', B, S3).strip().count('\n') + 1, 'paths in delta(B, stage 3)')
print('ALL CLOSING CONTROLS PASS' if ok else 'A CLOSING CONTROL FAILED')
sys.exit(0 if ok else 1)
