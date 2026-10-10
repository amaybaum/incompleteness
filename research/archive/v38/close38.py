#!/usr/bin/env python3
"""Scratch: V3-8 closing controls at the stage-3 commit (C3, C4, C5, C6, scope, chronology).
Never landed. Every tool run is the committed repository tool, run from the repository.

Usage: close38.py <B> <stage-3 commit>"""
import hashlib
import json
import os
import re
import subprocess
import sys
import types

REPO = os.environ.get('EXEC_REPO', '/home/user/incompleteness')
HERE = os.path.dirname(os.path.abspath(__file__))
B, S3 = sys.argv[1], sys.argv[2]
P = 'verification/infrastructure/round-v3-8-publication-removal/preregistration.md'
TOOL, README = 'tools/v3_verifier.py', 'verification/README.md'
CONF = 'verification/infrastructure/v3/conformance/'
CONVERTED = 'mc2-pass-base-drift'
BUDGET = {('M', 'verification/infrastructure/v3/architecture.md'), ('M', 'tools/v3_verifier.py'),
          ('M', 'verification/README.md'), ('M', CONF + 'mc2-pass-base-drift.json'),
          ('A', CONF + 'reach-true-host-merge-contains-q.json'), ('A', CONF + 'reach-false-moved-base-lacks-q.json'),
          ('A', CONF + 'reach-undecidable-shallow-history.json'),
          ('D', CONF + 'mc2-counter-host-merge.json')}
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


def tool(*a):
    p = subprocess.run([sys.executable, TOOL] + list(a), cwd=REPO, capture_output=True)
    return p.returncode, p.stdout.decode().rstrip('\n')


src = git('show', '%s:%s' % (S3, TOOL))
assert src == open(os.path.join(REPO, TOOL), encoding='utf-8').read()
names = sorted(n for n in os.listdir(os.path.join(REPO, CONF)) if n.endswith('.json'))
ALL = {n[:-5]: json.load(open(os.path.join(REPO, CONF, n), encoding='utf-8')) for n in names}


def run(t):
    return {v: t.run_vector(x, REPO)[0] for v, x in ALL.items()}


base = run(load('e', src))
report('C1 at the stage-3 tool: %d vectors, all as expected' % len(ALL), len(ALL) == 135 and all(base.values()))

# C3: three wrong diagnostics, each running exactly its own vectors not as expected
BODY = """    try:
        return ('true' if repo.is_ancestor(q, c) else 'false'), None
    except Undecidable as u:
        return 'undecidable', u.code"""
WRONG = {'always true': ("    return 'true', None",
                         ['reach-false-moved-base-lacks-q', 'reach-undecidable-shallow-history']),
         'always false': ("    return 'false', None",
                          ['reach-true-host-merge-contains-q', CONVERTED, 'reach-undecidable-shallow-history']),
         'reversed': (BODY.replace('is_ancestor(q, c)', 'is_ancestor(c, q)'),
                      ['reach-true-host-merge-contains-q', CONVERTED])}
for name, (body, own) in WRONG.items():
    r = run(load(name, sub(src, BODY, body)))
    report('C3 %-12s: its %d vector(s) not as expected, the other %d as expected' % (name, len(own), len(ALL) - len(own)),
           not any(r[v] for v in own) and all(r[v] for v in ALL if v not in own))

# C4: the census over B, unchanged
btool = os.path.join(HERE, 'v3_verifier_at_B.py')
open(btool, 'w', encoding='utf-8').write(git('show', '%s:%s' % (B, TOOL)))
pb = subprocess.run([sys.executable, btool, '--project', B], cwd=REPO, capture_output=True).stdout
pe = subprocess.run([sys.executable, TOOL, '--project', B], cwd=REPO, capture_output=True).stdout
report('C4 --project over B: identical to the tool at B (%d lines, sha256 %s)'
       % (pe.count(b'\n'), hashlib.sha256(pe).hexdigest()), pe == pb and pe)

# C5: the shadow report, the diagnostic and the self-description, by their outputs
rc, out = tool('--mode', 'shadow', '--subject', S3)
lines = out.split('\n')
rules = [ln[2:6].strip() for ln in lines if ln.startswith('  ') and ln[2:3] in 'KG']
report('C5 shadow exit 0', rc == 0)
report('C5 banner', lines[0] == 'v3_verifier shadow report -- SHADOW ONLY: this report gates nothing; '
       'V1 and V2 remain authoritative')
report('C5 rules %s' % ' '.join(rules),
       rules == ['K1', 'K2', 'K3', 'K4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12'])
report('C5 corpus line', 'CORPUS  135 vector(s), exact and as expected' in lines)
report('C5 projection line', 'PROJECTION  cells 126' in lines)
report('C5 last line', lines[-1] == 'v3_verifier: shadow report complete (corpus as expected)')
bp = git('rev-parse', B + '^1').strip()
r1, r2, r3 = tool('--reachable', B, bp), tool('--reachable', bp, B), tool('--publication', B, B)
report('C5 --reachable <B> <B^1>: %r exit %d' % (r1[1], r1[0]), r1 == (0, 'REACHABLE true'))
report('C5 --reachable <B^1> <B>: %r exit %d' % (r2[1], r2[0]), r2 == (0, 'REACHABLE false'))
report('C5 --publication refused: exit %d, no verdict' % r3[0], r3[0] != 0 and 'VERDICT' not in r3[1])
readme = git('show', '%s:%s' % (S3, README))
report('C5 no --publication or not-q-itself in the tool or the README',
       '--publication' not in src and 'not-q-itself' not in src and '--publication' not in readme
       and 'not-q-itself' not in readme)
pre = git('show', '%s:%s' % (B, P))
new_para = re.search(r'The paragraph at `E`:\n\n```text\n(.*?)```', pre, re.S).group(1)
report('C5 README paragraph is the frozen text', readme.count(new_para) == 1)
rc, out = tool('--self-test')
report('C6 %s' % out, rc == 0)

# chronology and scope from B
revs = git('rev-list', '--reverse', '%s..%s' % (B, S3)).split()
chron = all(len(git('rev-list', '--parents', '-n', '1', c).split()) == 2 for c in revs) \
    and git('rev-list', '--parents', '-n', '1', revs[0]).split()[1] == B
report('chronology: %d commits after B, each one parent, the oldest on B' % len(revs), chron)
for path in ('.github/workflows/verify.yml', 'tools/release_gate.py', 'tools/certificate_verifier.py',
             'verification/lean/edge_rigidity_probe.py', 'AGENTS.md', P):
    report('unchanged from B: %s' % path, git('rev-parse', '%s:%s' % (B, path)) == git('rev-parse', '%s:%s' % (S3, path)))
report('no verification/receipts/ or verification/v3-seals/; verification/seals/ unchanged',
       not git('ls-tree', '-d', '--name-only', S3, 'verification/receipts', 'verification/v3-seals').strip()
       and not git('diff', '--name-only', B, S3, '--', 'verification/seals/').strip())
delta = {tuple(l.split('\t')) for l in git('diff', '--no-renames', '--name-status', B, S3).strip().split('\n')}
report('scope: delta(B, stage 3) is the budget less result.md (%d paths)' % len(delta), delta == BUDGET)
print('ALL CLOSING CONTROLS PASS' if ok else 'A CLOSING CONTROL FAILED')
sys.exit(0 if ok else 1)
