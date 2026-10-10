#!/usr/bin/env python3
"""Release-gate checks of a Mathlib-bridge job log window.
usage: check_gate_log.py <raw.log> <expected lean-axioms count> <expected receipt count>"""
import re, sys

path, n_ax, n_rc = sys.argv[1], sys.argv[2], sys.argv[3]
L = open(path, encoding='utf-8').read().split('\n')
body = [l[29:] if re.match(r'^\d{4}-\d\d-\d\dT', l) else l for l in L]
ok = True


def check(cond, msg):
    global ok
    ok &= bool(cond)
    print(('  PASS  ' if cond else '  FAIL  ') + msg)


print('window: %d lines, %s .. %s' % (len(L), L[0][:28], (L[-1] or L[-2])[:28]))
done = [b for b in body if 'Build completed successfully' in b]
check(len(done) == 1, 'lake: %s' % done)
check(sum('sorryAx' in b for b in body) == 0, 'no line mentions sorryAx')
check(sum(bool(re.match(r'\s*error:', b)) for b in body) == 0 and sum('##[error]' in b for b in body) == 0
      and sum('✖' in b for b in body) == 0, 'no error:, ##[error] or failed-build line')
gate = [b.replace('\x1b', '') for b in body if re.match(r'^\s+(PASS|FAIL)\s+\S', b)]
check(len(gate) == 21 and all(g.lstrip().startswith('PASS') for g in gate),
      'release gate rows: %d, PASS %d' % (len(gate), sum(g.lstrip().startswith('PASS') for g in gate)))
for key, pat in (('lean-axioms', '(%s named result(s) reported' % n_ax), ('lean-manuscript', 'OK'),
                 ('v3-receipts', '%s receipt(s), all hold' % n_rc), ('legacy-records', '303 record(s)'),
                 ('artifact-placement', 'OK'), ('manifest-drift', 'OK')):
    row = [g for g in gate if key in g]
    check(row and pat in row[0], '%s: %s' % (key, row[0].strip()[:100] if row else None))
rel = [b.strip() for b in body if 'RELC-SELECT-1' in b]
print('  info  lines naming RELC-SELECT-1 in window: %d %s' % (len(rel), rel[:3]))
verdict = [b for b in body if b.startswith('release gate:')]
check(verdict and verdict[0].startswith('release gate: PASS'), 'verdict: %s' % verdict)
print('gate log: %s' % ('OK' if ok else 'FAILED'))
sys.exit(0 if ok else 1)
