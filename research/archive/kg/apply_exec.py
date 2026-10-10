#!/usr/bin/env python3
"""Apply K2-GUARD-1's execution edits to a worktree at D: the module, the import line and the census family.
usage: apply_exec.py <worktree>"""
import json, os, shutil, sys
WT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(WT, 'verification/lean-mathlib/OIBridge/K2Guard.lean')
IMPORTS = os.path.join(WT, 'verification/lean-mathlib/OIBridge.lean')
CENSUS = os.path.join(WT, 'verification/lean-manuscript-census.json')
shutil.copyfile(os.path.join(HERE, 'K2Guard.lean'), MOD)
t = open(IMPORTS, encoding='utf-8').read()
anchor = 'import OIBridge.K1Bridge\n'
assert t.count(anchor) == 1 and 'import OIBridge.K2Guard' not in t
open(IMPORTS, 'w', encoding='utf-8').write(t.replace(anchor, anchor + 'import OIBridge.K2Guard\n', 1))
c = json.loads(open(CENSUS, encoding='utf-8').read())
fam = c['families']
k = [i for i, f in enumerate(fam) if f['modules'] == ['K1Bridge']]
assert len(k) == 1 and not any(f['modules'] == ['K2Guard'] for f in fam)
new = {
    'name': "two interface facts of the composite route at the elementary ball: no candidate cone of two copies of eball 3 is invariant under DIM-1's gate and the one-copy reflection diag(1, -1, 1), and DIM-1's dimension selector, absolute and relative, gives d = 3 from 2 <= d in place of the entangling clause (round K2-GUARD-1, reconstruction)",
    'modules': ['K2Guard'],
    'status': 'kernel-only',
    'manuscript': [],
    'note': "Round K2-GUARD-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-k2-guard-1-interface/preregistration.md. Target A: CandidateCone K means every product state of eball 3 lies in K and K lies in maxCone (eball 3); no such K is invariant under both cnot and actT reflY, reflY = diag(1, -1, 1) on the second copy (no_candidateCone_cnot_reflY), by the exact chain prodState xplus z3, cnot, actT reflY, cnot, on which the product of the sharp effects along -e1 and -e3 is -1/2 (chain_eq, chain_value). Controls: nativeGate_cnot; reflY maps the ball into itself with determinant -1 and nflip has determinant 1 (reflY_mem_eball, det_reflY, det_nflip); the products with their cnot images form a cnot-invariant candidate cone and the products alone a reflY-invariant one (candidateCone_cnotOrbit, cnot_mem_cnotOrbit, candidateCone_productSet, reflY_mem_productSet); with nflip in place of reflY the chain value is 0 (rotation_chain_value). Target B: three_of_nativeGate_of_two_le and three_of_nativeGateOf_of_two_le give d = 3 from 2 <= d with DIM-1's and K1-BRIDGE-1's hypotheses; two_le_of_entangling gives 2 <= d from the entangling clause, with no converse stated; two_le_load_bearing is the classical interval at d = 1. The verdicts are k2guard_orientation and k2guard_entangling, independently. Carried by no manuscript. Nothing here identifies the physical composite cone, derives local tomography or the product form of the composite tests, sources a local action, a dense or continuous family of reversible operations, K∞-Copy or 2 <= d, or states that reflections are excluded in every theory."
}
fam.insert(k[0] + 1, new)
open(CENSUS, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
print('applied')
