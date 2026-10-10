#!/usr/bin/env python3
"""Apply PARITY-NOT-1's execution edits to a worktree at D: the module, the import line and the census family.
usage: apply_exec.py <worktree>"""
import json, os, shutil, sys
WT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(WT, 'verification/lean-mathlib/OIBridge/ParityNot.lean')
IMPORTS = os.path.join(WT, 'verification/lean-mathlib/OIBridge.lean')
CENSUS = os.path.join(WT, 'verification/lean-manuscript-census.json')
shutil.copyfile(os.path.join(HERE, 'ParityNot.ref.lean'), MOD)
t = open(IMPORTS, encoding='utf-8').read()
anchor = 'import OIBridge.DenseOrbit\n'
assert t.count(anchor) == 1 and 'import OIBridge.ParityNot' not in t
open(IMPORTS, 'w', encoding='utf-8').write(t.replace(anchor, anchor + 'import OIBridge.ParityNot\n', 1))
c = json.loads(open(CENSUS, encoding='utf-8').read())
fam = c['families']
k = [i for i, f in enumerate(fam) if f['modules'] == ['DenseOrbit']]
assert len(k) == 1 and not any(f['modules'] == ['ParityNot'] for f in fam)
fam.insert(k[0] + 1, json.load(open(os.path.join(HERE, 'ctl', 'family.json'), encoding='utf-8')))
open(CENSUS, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
print('applied')
