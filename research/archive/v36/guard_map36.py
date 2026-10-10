#!/usr/bin/env python3
"""Scratch: the guard's verdict map from a Numerical-probes job log. Never landed.
Usage: guard_map36.py <saved log> <outprefix>. Writes <outprefix>.ids (one 'VERDICT ID' per check)
and <outprefix>.full (each check line without its timestamp); prints the counts and the summary."""
import json, re, sys
raw = open(sys.argv[1]).read()
try:
    t = json.loads(raw)['logs_content']
except Exception:
    t = raw
lines = [re.sub(r'^\S+Z ', '', l) for l in t.split('\n')]
a = lines.index('=== edge_rigidity_probe.py ===')
b = next(i for i in range(a, len(lines)) if lines[i].startswith('edge_rigidity_probe: '))
checks = [l for l in lines[a:b] if re.match(r'  (PASS|FAIL)  \S+?:', l)]
ids = [re.match(r'  (PASS|FAIL)  (\S+?):', l).groups() for l in checks]
open(sys.argv[2] + '.ids', 'w').write(''.join('%s %s\n' % x for x in ids))
open(sys.argv[2] + '.full', 'w').write(''.join(l + '\n' for l in checks))
print('summary:', lines[b])
print('PASS %d FAIL %d' % (sum(v == 'PASS' for v, _ in ids), sum(v == 'FAIL' for v, _ in ids)))
