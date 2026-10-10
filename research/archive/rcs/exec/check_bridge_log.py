#!/usr/bin/env python3
"""Exact checks of a Mathlib-bridge job log window for round RELC-SELECT-1.
usage: check_bridge_log.py <raw.log> <commit> [<reference raw.log for the Block warnings>]"""
import re, subprocess, sys

log_path, commit = sys.argv[1], sys.argv[2]
ref_path = sys.argv[3] if len(sys.argv) > 3 else None
MODS = ['RelcSelectParity', 'RelcSelectBlock', 'RelcSelectSqueeze', 'RelcSelectC5']
THREE = '[propext, Classical.choice, Quot.sound]'
EXPECTED_BLOCK = [(606, 23), (606, 52), (608, 10), (622, 25), (622, 54), (623, 70), (623, 93)]
L = open(log_path, encoding='utf-8').read().split('\n')
body = [l[29:] if re.match(r'^\d{4}-\d\d-\d\dT', l) else l for l in L]
ok = True


def check(cond, msg):
    global ok
    ok &= bool(cond)
    print(('  PASS  ' if cond else '  FAIL  ') + msg)


print('window: %d lines, %s .. %s' % (len(L), L[0][:28], (L[-1] or L[-2])[:28]))
built = {m: [b for b in body if re.search(r'\] (Built|Replayed) OIBridge\.%s\b' % m, b)] for m in MODS}
for m in MODS:
    check(len(built[m]) == 1 and 'Built' in built[m][0], '%s build line in window: %s' % (m, built[m]))
done = [b for b in body if 'Build completed successfully' in b]
check(len(done) == 1, 'lake: %s' % done)

# declared prints at the commit, per module
declared = {}
for m in MODS:
    src = subprocess.run(['git', 'show', '%s:verification/lean-mathlib/OIBridge/%s.lean' % (commit, m)],
                         capture_output=True, text=True, check=True).stdout.split('\n')
    declared[m] = [(i + 1, re.match(r'^#print axioms (\S+)\s*$', s).group(1))
                   for i, s in enumerate(src) if re.match(r'^#print axioms \S+\s*$', s)]
nd = sum(len(v) for v in declared.values())
check(nd == 34 and [len(declared[m]) for m in MODS] == [2, 5, 15, 12],
      'declared #print axioms at the commit: %d (%s)' % (nd, [len(declared[m]) for m in MODS]))

reports = []
for b in body:
    r = re.search(r"info: OIBridge/(RelcSelect\w+)\.lean:(\d+):\d+: '([^']+)' depends on axioms: (\[[^\]]*\])", b)
    if r:
        reports.append((r.group(1), int(r.group(2)), r.group(3), r.group(4)))
    if re.search(r"OIBridge\.RelcSelect\.[^']+' does not depend on any axioms", b):
        reports.append(('?', 0, b, 'NONE'))
check(len(reports) == 34, 'RelcSelect axiom reports in window: %d' % len(reports))
check(all(r[3] == THREE for r in reports), 'every report is exactly %s' % THREE)
check(len({r[2] for r in reports}) == 34, 'distinct reported names: %d' % len({r[2] for r in reports}))
want = sorted((m, ln, 'OIBridge.RelcSelect.' + n if not n.startswith('OIBridge.') else n)
              for m in MODS for ln, n in declared[m])
got = sorted((r[0], r[1], r[2]) for r in reports)
check(want == got, 'reports match the declared prints file:line:name one for one')

warns = {m: [] for m in MODS}
for i, b in enumerate(body):
    w = re.search(r'warning: OIBridge/(RelcSelect\w+)\.lean:(\d+):(\d+): (.*)$', b)
    if w:
        nxt = body[i + 1].strip() if i + 1 < len(body) else ''
        warns[w.group(1)].append((int(w.group(2)), int(w.group(3)), w.group(4).strip(), nxt))
check([len(warns[m]) for m in MODS] == [0, 7, 0, 0],
      'warnings per module (Parity, Block, Squeeze, C5): %s' % [len(warns[m]) for m in MODS])
check([(a, b) for a, b, _, _ in warns['RelcSelectBlock']] == EXPECTED_BLOCK,
      'Block warnings at %s' % [(a, b) for a, b, _, _ in warns['RelcSelectBlock']])
if ref_path:
    R = open(ref_path, encoding='utf-8').read().split('\n')
    rb = [l[29:] if re.match(r'^\d{4}-\d\d-\d\dT', l) else l for l in R]
    ref = []
    for i, b in enumerate(rb):
        w = re.search(r'warning: OIBridge/RelcSelectBlock\.lean:(\d+):(\d+): (.*)$', b)
        if w:
            ref.append((int(w.group(1)), int(w.group(2)), w.group(3).strip(), rb[i + 1].strip()))
    check(ref == warns['RelcSelectBlock'],
          'Block warnings identical (location, message, flagged argument) to the reference log')

check(sum('sorryAx' in b for b in body) == 0, "no line mentions sorryAx")
check(sum("declaration uses 'sorry'" in b for b in body) == 0, "no 'declaration uses sorry'")
check(sum(bool(re.match(r'\s*error:', b)) for b in body) == 0 and sum('##[error]' in b for b in body) == 0
      and sum('✖' in b for b in body) == 0, 'no error:, ##[error] or failed-build line')
gate = [b.replace('\x1b', '') for b in body if re.match(r'^\s+(PASS|FAIL)\s+\S', b)]
check(len(gate) == 21 and all(g.lstrip().startswith('PASS') for g in gate),
      'release gate rows: %d, PASS %d' % (len(gate), sum(g.lstrip().startswith('PASS') for g in gate)))
la = [g for g in gate if 'lean-axioms' in g]
check(la and '(5860 named result(s) reported' in la[0], 'lean-axioms: %s' % (la[0].strip()[:90] if la else None))
for key, pat in (('lean-manuscript', 'OK'), ('v3-receipts', '41 receipt(s), all hold'),
                 ('legacy-records', '303 record(s)')):
    row = [g for g in gate if key in g]
    check(row and pat in row[0], '%s: %s' % (key, row[0].strip()[:90] if row else None))
verdict = [b for b in body if b.startswith('release gate:')]
check(verdict and verdict[0].startswith('release gate: PASS'), 'verdict: %s' % verdict)
print('bridge log: %s' % ('OK' if ok else 'FAILED'))
sys.exit(0 if ok else 1)
