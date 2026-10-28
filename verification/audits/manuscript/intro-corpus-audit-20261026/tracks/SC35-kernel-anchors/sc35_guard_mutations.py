#!/usr/bin/env python3
"""SC-35 guard mutation test: each pinned text, altered one at a time, must make its guard FAIL.

Run from the repository root:  python3 -I <this file>
Each mutation edits one manuscript in place, runs verification/lean/edge_rigidity_probe.py, records the
R7-RCH and R7-RCL verdicts, and restores the file byte for byte before the next mutation.
"""
import re
import subprocess
import sys

MUTATIONS = [
    ('module named outside Main (RecurrenceHorizon)', 'papers/GR.md', None, '\nSee `OIBridge/RecurrenceHorizon.lean`.\n', 'R7-RCH'),
    ('module named outside Main (RootedClassification)', 'papers/GR.md', None, '\nSee `OIBridge/RootedClassification.lean`.\n', 'R7-RCL'),
    ('routed readback: return-horizon scope dropped', 'papers/Main.md', 'not an accessible window', 'not a window', 'R7-RCH'),
    ('routed readback: physical status dropped', 'papers/Main.md', 'in either reading, is not established', 'in either reading, is open', 'R7-RCH'),
    ('overlap theorem: support hypothesis dropped', 'papers/Main.md', 'not required to have full support, from which', 'from which', 'R7-RCH'),
    ('classification: support hypothesis dropped', 'papers/Main.md', 'shared by every root, not required to have full support, if and only if', 'shared by every root, if and only if', 'R7-RCL'),
]


def run():
    out = subprocess.run([sys.executable, 'verification/lean/edge_rigidity_probe.py'],
                         capture_output=True, text=True).stdout
    return {g: re.search(r'^\s*(PASS|FAIL)\s+' + g + ':', out, re.M).group(1) for g in ('R7-RCH', 'R7-RCL')}


ok = True
base = run()
print('unmutated:', base)
ok &= base == {'R7-RCH': 'PASS', 'R7-RCL': 'PASS'}
for label, path, old, new, guard in MUTATIONS:
    orig = open(path, encoding='utf-8').read()
    try:
        if old is None:
            mut = orig + new
        else:
            assert orig.count(old) == 1, label
            mut = orig.replace(old, new)
        open(path, 'w', encoding='utf-8').write(mut)
        v = run()
    finally:
        open(path, 'w', encoding='utf-8').write(orig)
    hit = v[guard] == 'FAIL'
    ok &= hit
    print(('  PASS  ' if hit else '  FAIL  ') + f'{label}: {guard} {v[guard]} ({v})')
print('sc35_guard_mutations: ' + ('OK' if ok else 'FAILED'))
sys.exit(0 if ok else 1)
