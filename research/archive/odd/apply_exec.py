#!/usr/bin/env python3
"""Apply ODD-CHAR-1's execution edits to a worktree at D: the module, the import line and the census family.
usage: apply_exec.py <worktree>"""
import json, os, shutil, sys
WT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(WT, 'verification/lean-mathlib/OIBridge/OddChar.lean')
IMPORTS = os.path.join(WT, 'verification/lean-mathlib/OIBridge.lean')
CENSUS = os.path.join(WT, 'verification/lean-manuscript-census.json')
assert not os.path.exists(MOD)
shutil.copyfile(os.path.join(HERE, 'OddChar.ref.lean'), MOD)
t = open(IMPORTS, encoding='utf-8').read()
anchor = 'import OIBridge.ParityNot\n'
assert t.count(anchor) == 1 and 'import OIBridge.OddChar' not in t
open(IMPORTS, 'w', encoding='utf-8').write(t.replace(anchor, anchor + 'import OIBridge.OddChar\n', 1))
c = json.loads(open(CENSUS, encoding='utf-8').read())
fam = c['families']
k = [i for i, f in enumerate(fam) if f['modules'] == ['ParityNot']]
assert len(k) == 1 and not any(f['modules'] == ['OddChar'] for f in fam)
fam.insert(k[0] + 1, json.load(open(os.path.join(HERE, 'ctl', 'family.json'), encoding='utf-8')))
open(CENSUS, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
print('applied')
