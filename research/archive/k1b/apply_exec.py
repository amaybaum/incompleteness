#!/usr/bin/env python3
"""Apply K1-BRIDGE-1's execution edits to a worktree at D: the module, the import line and the census family.
usage: apply_exec.py <worktree>"""
import json, os, shutil, sys
WT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(WT, 'verification/lean-mathlib/OIBridge/K1Bridge.lean')
IMPORTS = os.path.join(WT, 'verification/lean-mathlib/OIBridge.lean')
CENSUS = os.path.join(WT, 'verification/lean-manuscript-census.json')
shutil.copyfile(os.path.join(HERE, 'K1Bridge.lean'), MOD)
t = open(IMPORTS, encoding='utf-8').read()
anchor = 'import OIBridge.EffectSpace\n'
assert t.count(anchor) == 1 and 'import OIBridge.K1Bridge' not in t
open(IMPORTS, 'w', encoding='utf-8').write(t.replace(anchor, anchor + 'import OIBridge.K1Bridge\n', 1))
c = json.loads(open(CENSUS, encoding='utf-8').read())
fam = c['families']
k = [i for i, f in enumerate(fam) if f['modules'] == ['EffectSpace']]
assert len(k) == 1 and not any(f['modules'] == ['K1Bridge'] for f in fam)
new = {
    'name': "DIM-1's dimension selectors relative to a family of available test functionals: for every d >= 1, effect soundness with body preservation, K∞-Seed, K∞-Trans and K∞-V4 carry the native-gate and entangling hypotheses stated on the available family's product cone to DIM-1's, so d in {1, 3} and, with the entangling clause, d = 3 (round K1-BRIDGE-1, reconstruction)",
    'modules': ['K1Bridge'],
    'status': 'kernel-only',
    'manuscript': [],
    'note': "Round K1-BRIDGE-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/preregistration.md. NativeGateOf Ω avail z N T is DIM-1's NativeGate with maxCone Ω replaced by maxConeOf avail in the two positivity clauses; EntanglingOf Ω avail T is Entangling with the joint states of maxConeOf avail. The cone equality carries the relative hypotheses to DIM-1's (nativeGate_of_cone_eq, entangling_of_cone_eq), and on eball d, 0 < d, EffectsOn (eball d) avail with OG-1's four named hypotheses (PreservesBody, SharpSeed, BoundaryTransitive, SeedOrbitAvailable; in the ROADMAP's labels body preservation, K∞-Seed, K∞-Trans and K∞-V4) give that equality by EFF-1's maxConeOf_avail_eq, so the relative selectors dim_of_nativeGateOf (d = 1 or d = 3) and three_of_nativeGateOf (d = 3) are EFF-1's cone equality, the transport and DIM-1's dim_of_nativeGate and three_of_nativeGate, with no new dimension argument and no mixing closure or unit premise. Controls carried from EFF-1: at d = 0 the cone equality fails (cone_eq_fails_zero); at d = 3 the one-axis family with the unit consists of effects and its cone is not maxCone (eball 3) (cone_eq_fails_axis). The verdict is k1b_core. Carried by no manuscript. Nothing here sources effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, IsNot or the relative native-gate and entangling hypotheses; the product form of the composite tests (DIM-1's carrier W d) is a premise of both rounds and is not addressed; nothing here concerns K2, K∞-Stage, K∞-Act, K∞-Drive, K∞-Copy, K∞-Geom, Kₙ or K3."
}
fam.insert(k[0] + 1, new)
open(CENSUS, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
print('applied')
