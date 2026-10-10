#!/usr/bin/env python3
"""Apply K1-SHARP-TESTS-1's execution edits to a worktree at D: the module, the import line and the census family.
usage: apply_exec.py <worktree>"""
import json, os, shutil, sys
WT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(WT, 'verification/lean-mathlib/OIBridge/SharpTests.lean')
IMPORTS = os.path.join(WT, 'verification/lean-mathlib/OIBridge.lean')
CENSUS = os.path.join(WT, 'verification/lean-manuscript-census.json')
shutil.copyfile(os.path.join(HERE, 'SharpTests.lean'), MOD)
t = open(IMPORTS, encoding='utf-8').read()
anchor = 'import OIBridge.K2Guard\n'
assert t.count(anchor) == 1 and 'import OIBridge.SharpTests' not in t
open(IMPORTS, 'w', encoding='utf-8').write(t.replace(anchor, anchor + 'import OIBridge.SharpTests\n', 1))
c = json.loads(open(CENSUS, encoding='utf-8').read())
fam = c['families']
k = [i for i, f in enumerate(fam) if f['modules'] == ['K2Guard']]
assert len(k) == 1 and not any(f['modules'] == ['SharpTests'] for f in fam)
new = {
    'name': "the premise 2 <= d of the dimension selector at the elementary ball as two sharp binary tests distinct modulo complementation, and its independence from the selector's other relative hypotheses (round K1-SHARP-TESTS-1, reconstruction)",
    'modules': ['SharpTests'],
    'status': 'kernel-only',
    'manuscript': [],
    'note': "Round K1-SHARP-TESTS-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/preregistration.md. HasTwoSharpTests Ω: two sharp seeds e, f of Ω (OG-1's SharpSeed) with some state of Ω separating f from e and some state separating f from 1 - e. Cell 1: sharpEff (-b) x = 1 - sharpEff b x (sharpEff_neg_apply); the sharp seeds of eball d are the sharp effects along unit vectors (sharpSeed_iff, through sharp_eq_of_certain); eball 0 has no sharp seed (not_sharpSeed_zero); on eball 1 two sharp seeds agree or are complementary on every state (eq_or_compl_one); the first two axes witness the predicate for 2 <= d (hasTwoSharpTests_of_two_le); HasTwoSharpTests (eball d) <-> 2 <= d (hasTwoSharpTests_iff); verdict k1sharp_classified. Cell 2: at d = 1, fullEffects (eball 1), fullAut 1, sharpEff z1, neg1 and cnot1 satisfy EffectsOn, PreservesBody, SharpSeed, BoundaryTransitive, SeedOrbitAvailable, IsNot and NativeGateOf while 2 <= 1 fails (two_le_load_bearing_relative, nativeGateOf_cnot1), so those hypotheses do not imply 2 <= d (two_le_not_implied); verdict k1sharp_two_le_not_implied. Carried by no manuscript. The classification is proved for eball d only; nothing here sources HasTwoSharpTests or 2 <= d, or relates the predicate to entanglement."
}
fam.insert(k[0] + 1, new)
open(CENSUS, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
print('applied')
