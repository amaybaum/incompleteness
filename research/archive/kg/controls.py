#!/usr/bin/env python3
"""controls.py -- round K2-GUARD-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the two cells computed from the module's statements at <commit>

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  obstruction `reflY`, `CandidateCone`, `productSet`, `cnotOrbit` are the frozen texts whole; the obstruction theorem
                  has exactly the frozen binders and conclusion `False`, and its proof names `chain_eq` and `chain_value`
  S2  controls    the orientation controls are theorems with their frozen conclusions and prints: the native gate, the
                  ball map and the two determinants, the two non-vacuity families, the chain value and the rotation
                  value
  S3  selectors   the two `2 ≤ d` selectors have exactly the frozen explicit binders and conclusion `d = 3`, their proofs
                  name `dim_of_nativeGate` / `dim_of_nativeGateOf`, and neither statement mentions `Entangling`;
                  `two_le_of_entangling` concludes `2 ≤ d` from the entangling clause and nothing else does
  S4  premises    no theorem concludes `Entangling`, `NativeGateOf`, `EffectsOn`, `SharpSeed`, `PreservesBody`,
                  `BoundaryTransitive` or `SeedOrbitAvailable`; `NativeGate`, `IsNot` and `CandidateCone` are concluded
                  only of the named witnesses by the named control theorems and the verdicts
  S5  reuse       no declaration shares a name with a landed object it reads; the only import is `OIBridge.K1Bridge`
  S6  neutral     no complex, conjugate-transpose, positive-semidefinite, trace, qubit, Bloch, Pauli, density, drive,
                  flow, limit, closure, density-of-subgroup, tensor-product or Hilbert token
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  scope       the selector section (§E) mentions no dimension-three object; `2 ≤ d` occurs only in §E, §F and the
                  verdicts
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements by its own frozen rule, independently of the
                  other; at a commit carrying the result note, the note states exactly the computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.K1Bridge`
  C   census      the census is D's with exactly the frozen family inserted after the K1-BRIDGE-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '8daf2bc0ad9c4fe4e9ae422b3a9a010a80ab9e53'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-k2-guard-1-interface/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/K2Guard.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = 'ec8ba57b178561c81b082404ceb02241ada1fe1e'
ANCHOR_IMPORT = 'import OIBridge.K1Bridge\n'
NEW_IMPORT = 'import OIBridge.K2Guard\n'
PREV_FAMILY_MODULES = ['K1Bridge']
CENSUS_FAMILY = json.loads(r'''{
 "name": "two interface facts of the composite route at the elementary ball: no candidate cone of two copies of eball 3 is invariant under DIM-1's gate and the one-copy reflection diag(1, -1, 1), and DIM-1's dimension selector, absolute and relative, gives d = 3 from 2 <= d in place of the entangling clause (round K2-GUARD-1, reconstruction)",
 "modules": [
  "K2Guard"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round K2-GUARD-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-k2-guard-1-interface/preregistration.md. Target A: CandidateCone K means every product state of eball 3 lies in K and K lies in maxCone (eball 3); no such K is invariant under both cnot and actT reflY, reflY = diag(1, -1, 1) on the second copy (no_candidateCone_cnot_reflY), by the exact chain prodState xplus z3, cnot, actT reflY, cnot, on which the product of the sharp effects along -e1 and -e3 is -1/2 (chain_eq, chain_value). Controls: nativeGate_cnot; reflY maps the ball into itself with determinant -1 and nflip has determinant 1 (reflY_mem_eball, det_reflY, det_nflip); the products with their cnot images form a cnot-invariant candidate cone and the products alone a reflY-invariant one (candidateCone_cnotOrbit, cnot_mem_cnotOrbit, candidateCone_productSet, reflY_mem_productSet); with nflip in place of reflY the chain value is 0 (rotation_chain_value). Target B: three_of_nativeGate_of_two_le and three_of_nativeGateOf_of_two_le give d = 3 from 2 <= d with DIM-1's and K1-BRIDGE-1's hypotheses; two_le_of_entangling gives 2 <= d from the entangling clause, with no converse stated; two_le_load_bearing is the classical interval at d = 1. The verdicts are k2guard_orientation and k2guard_entangling, independently. Carried by no manuscript. Nothing here identifies the physical composite cone, derives local tomography or the product form of the composite tests, sources a local action, a dense or continuous family of reversible operations, K∞-Copy or 2 <= d, or states that reflections are excluded in every theory."
}''')
DECLS = json.loads(r'''[
 [
  "def",
  "reflY"
 ],
 [
  "theorem",
  "reflY_apply"
 ],
 [
  "theorem",
  "reflY_zero'"
 ],
 [
  "theorem",
  "reflY_one"
 ],
 [
  "theorem",
  "reflY_two"
 ],
 [
  "theorem",
  "homMap_reflY_zero"
 ],
 [
  "theorem",
  "homMap_reflY_one"
 ],
 [
  "theorem",
  "homMap_reflY_two"
 ],
 [
  "theorem",
  "homMap_reflY_three"
 ],
 [
  "theorem",
  "reflY_mem_eball"
 ],
 [
  "theorem",
  "reflY_reflY"
 ],
 [
  "theorem",
  "det_reflY"
 ],
 [
  "theorem",
  "det_nflip"
 ],
 [
  "def",
  "CandidateCone"
 ],
 [
  "def",
  "idW"
 ],
 [
  "def",
  "chainW"
 ],
 [
  "theorem",
  "actT_reflY_phiW"
 ],
 [
  "theorem",
  "cnot_idW"
 ],
 [
  "theorem",
  "chain_eq"
 ],
 [
  "theorem",
  "sharpVec_negX"
 ],
 [
  "theorem",
  "sharpVec_negZ"
 ],
 [
  "theorem",
  "sharpEff_negX_isEffectOn"
 ],
 [
  "theorem",
  "sharpEff_negZ_isEffectOn"
 ],
 [
  "theorem",
  "chain_value"
 ],
 [
  "theorem",
  "no_candidateCone_cnot_reflY"
 ],
 [
  "theorem",
  "prodEffVal_prodState"
 ],
 [
  "theorem",
  "prodState_mem_maxCone"
 ],
 [
  "theorem",
  "actT_prodState"
 ],
 [
  "def",
  "productSet"
 ],
 [
  "def",
  "cnotOrbit"
 ],
 [
  "theorem",
  "candidateCone_productSet"
 ],
 [
  "theorem",
  "reflY_mem_productSet"
 ],
 [
  "theorem",
  "candidateCone_cnotOrbit"
 ],
 [
  "theorem",
  "cnot_mem_cnotOrbit"
 ],
 [
  "def",
  "rotW"
 ],
 [
  "def",
  "rotChainW"
 ],
 [
  "theorem",
  "actT_nflip_phiW"
 ],
 [
  "theorem",
  "cnot_rotW"
 ],
 [
  "theorem",
  "rotation_chain_value"
 ],
 [
  "theorem",
  "three_of_nativeGate_of_two_le"
 ],
 [
  "theorem",
  "two_le_of_entangling"
 ],
 [
  "theorem",
  "three_of_nativeGateOf_of_two_le"
 ],
 [
  "theorem",
  "two_le_load_bearing"
 ],
 [
  "theorem",
  "two_le_satisfiable"
 ],
 [
  "theorem",
  "k2guard_orientation"
 ],
 [
  "theorem",
  "k2guard_entangling"
 ]
]''')
TEXTS = json.loads(r'''{
 "reflY": "def reflY : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where\n  toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i\n  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]\n  map_smul' c x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring",
 "reflY_apply": "theorem reflY_apply (x : Fin 3 → ℝ) (i : Fin 3) : reflY x i = (![1, -1, 1] : Fin 3 → ℝ) i * x i",
 "reflY_zero'": "@[simp] theorem reflY_zero' (x : Fin 3 → ℝ) : reflY x 0 = x 0",
 "reflY_one": "@[simp] theorem reflY_one (x : Fin 3 → ℝ) : reflY x 1 = -x 1",
 "reflY_two": "@[simp] theorem reflY_two (x : Fin 3 → ℝ) : reflY x 2 = x 2",
 "homMap_reflY_zero": "@[simp] theorem homMap_reflY_zero (v : HVec 3) : homMap reflY v 0 = v 0",
 "homMap_reflY_one": "@[simp] theorem homMap_reflY_one (v : HVec 3) : homMap reflY v 1 = v 1",
 "homMap_reflY_two": "@[simp] theorem homMap_reflY_two (v : HVec 3) : homMap reflY v 2 = -v 2",
 "homMap_reflY_three": "@[simp] theorem homMap_reflY_three (v : HVec 3) : homMap reflY v 3 = v 3",
 "reflY_mem_eball": "theorem reflY_mem_eball {x : Fin 3 → ℝ} (hx : x ∈ eball 3) : reflY x ∈ eball 3",
 "reflY_reflY": "theorem reflY_reflY (x : Fin 3 → ℝ) : reflY (reflY x) = x",
 "det_reflY": "theorem det_reflY : LinearMap.det reflY = -1",
 "det_nflip": "theorem det_nflip : LinearMap.det nflip = 1",
 "CandidateCone": "def CandidateCone (K : Set (W 3)) : Prop :=\n  (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)",
 "idW": "def idW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 1]]",
 "chainW": "def chainW : W 3 := ![![1, 0, 0, 1], ![1, 0, 0, -1], ![0, 0, 0, 0], ![0, 0, 0, 0]]",
 "actT_reflY_phiW": "theorem actT_reflY_phiW : actT reflY phiW = idW",
 "cnot_idW": "theorem cnot_idW : cnot idW = chainW",
 "chain_eq": "theorem chain_eq : cnot (actT reflY (cnot (prodState xplus z3))) = chainW",
 "sharpVec_negX": "theorem sharpVec_negX : sharpVec (![-1, 0, 0] : Fin 3 → ℝ) = ![1 / 2, -1 / 2, 0, 0]",
 "sharpVec_negZ": "theorem sharpVec_negZ : sharpVec (![0, 0, -1] : Fin 3 → ℝ) = ![1 / 2, 0, 0, -1 / 2]",
 "sharpEff_negX_isEffectOn": "theorem sharpEff_negX_isEffectOn : IsEffectOn (eball 3) (sharpEff ![-1, 0, 0])",
 "sharpEff_negZ_isEffectOn": "theorem sharpEff_negZ_isEffectOn : IsEffectOn (eball 3) (sharpEff ![0, 0, -1])",
 "chain_value": "theorem chain_value :\n    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1]) chainW = -1 / 2",
 "no_candidateCone_cnot_reflY": "theorem no_candidateCone_cnot_reflY {K : Set (W 3)} (hK : CandidateCone K)\n    (hC : ∀ ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K) : False",
 "prodEffVal_prodState": "theorem prodEffVal_prodState (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin d → ℝ) :\n    prodEffVal e f (prodState x y) = e x * f y",
 "prodState_mem_maxCone": "theorem prodState_mem_maxCone {Ω : Set (Fin d → ℝ)} {x y : Fin d → ℝ} (hx : x ∈ Ω) (hy : y ∈ Ω) :\n    prodState x y ∈ maxCone Ω",
 "actT_prodState": "theorem actT_prodState (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x y : Fin d → ℝ) :\n    actT N (prodState x y) = prodState x (N y)",
 "productSet": "def productSet : Set (W 3) := {ω | ∃ x ∈ eball 3, ∃ y ∈ eball 3, ω = prodState x y}",
 "cnotOrbit": "def cnotOrbit : Set (W 3) :=\n  {ω | ∃ x ∈ eball 3, ∃ y ∈ eball 3, ω = prodState x y ∨ ω = cnot (prodState x y)}",
 "candidateCone_productSet": "theorem candidateCone_productSet : CandidateCone productSet",
 "reflY_mem_productSet": "theorem reflY_mem_productSet {ω : W 3} (hω : ω ∈ productSet) : actT reflY ω ∈ productSet",
 "candidateCone_cnotOrbit": "theorem candidateCone_cnotOrbit : CandidateCone cnotOrbit",
 "cnot_mem_cnotOrbit": "theorem cnot_mem_cnotOrbit {ω : W 3} (hω : ω ∈ cnotOrbit) : cnot ω ∈ cnotOrbit",
 "rotW": "def rotW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, -1]]",
 "rotChainW": "def rotChainW : W 3 := ![![1, 0, 0, -1], ![1, 0, 0, -1], ![0, 0, 0, 0], ![0, 0, 0, 0]]",
 "actT_nflip_phiW": "theorem actT_nflip_phiW : actT nflip phiW = rotW",
 "cnot_rotW": "theorem cnot_rotW : cnot rotW = rotChainW",
 "rotation_chain_value": "theorem rotation_chain_value :\n    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])\n      (cnot (actT nflip (cnot (prodState xplus z3)))) = 0",
 "three_of_nativeGate_of_two_le": "theorem three_of_nativeGate_of_two_le {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    d = 3",
 "two_le_of_entangling": "theorem two_le_of_entangling {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    (hE : Entangling (eball d) G) : 2 ≤ d",
 "three_of_nativeGateOf_of_two_le": "theorem three_of_nativeGateOf_of_two_le (hd : 2 ≤ d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3",
 "two_le_load_bearing": "theorem two_le_load_bearing :\n    IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1)",
 "two_le_satisfiable": "theorem two_le_satisfiable : 2 ≤ 3 ∧ IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot",
 "k2guard_orientation": "theorem k2guard_orientation :\n    (∀ K : Set (W 3), CandidateCone K → (∀ ω ∈ K, cnot ω ∈ K) →\n        (∀ ω ∈ K, actT reflY ω ∈ K) → False) ∧\n    NativeGate (eball 3) z3 nflip cnot ∧\n    (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det reflY = -1 ∧ LinearMap.det nflip = 1 ∧\n    (CandidateCone cnotOrbit ∧ ∀ ω ∈ cnotOrbit, cnot ω ∈ cnotOrbit) ∧\n    (CandidateCone productSet ∧ ∀ ω ∈ productSet, actT reflY ω ∈ productSet) ∧\n    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])\n      (cnot (actT reflY (cnot (prodState xplus z3)))) = -1 / 2 ∧\n    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])\n      (cnot (actT nflip (cnot (prodState xplus z3)))) = 0",
 "k2guard_entangling": "theorem k2guard_entangling :\n    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),\n        2 ≤ d → IsNot (eball d) z N → NativeGate (eball d) z N G → d = 3) ∧\n    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n        (T : W d ≃ₗ[ℝ] W d), 2 ≤ d → EffectsOn (eball d) avail → PreservesBody (eball d) G →\n        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →\n        IsNot (eball d) z N → NativeGateOf (eball d) avail z N T → d = 3) ∧\n    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),\n        IsNot (eball d) z N → NativeGate (eball d) z N G → Entangling (eball d) G → 2 ≤ d) ∧\n    (IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1)) ∧\n    (2 ≤ 3 ∧ IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot)"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.K2Guard.reflY_mem_eball",
 "OIBridge.K2Guard.det_reflY",
 "OIBridge.K2Guard.det_nflip",
 "OIBridge.K2Guard.chain_eq",
 "OIBridge.K2Guard.chain_value",
 "OIBridge.K2Guard.no_candidateCone_cnot_reflY",
 "OIBridge.K2Guard.prodState_mem_maxCone",
 "OIBridge.K2Guard.candidateCone_productSet",
 "OIBridge.K2Guard.reflY_mem_productSet",
 "OIBridge.K2Guard.candidateCone_cnotOrbit",
 "OIBridge.K2Guard.cnot_mem_cnotOrbit",
 "OIBridge.K2Guard.rotation_chain_value",
 "OIBridge.K2Guard.three_of_nativeGate_of_two_le",
 "OIBridge.K2Guard.two_le_of_entangling",
 "OIBridge.K2Guard.three_of_nativeGateOf_of_two_le",
 "OIBridge.K2Guard.two_le_load_bearing",
 "OIBridge.K2Guard.two_le_satisfiable",
 "OIBridge.K2Guard.k2guard_orientation",
 "OIBridge.K2Guard.k2guard_entangling"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.K1Bridge\n\nnamespace OIBridge\nnamespace K2Guard\n\nopen Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface\nopen EffectSpace K1Bridge\n\nvariable {d : ℕ}\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace K2Guard",
 "open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface",
 "open EffectSpace K1Bridge",
 "variable {d : ℕ}",
 "section Relative",
 "variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}\n  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}",
 "end Relative",
 "end K2Guard",
 "end OIBridge"
]''')
N_PRINTS = 19

DECL = re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure'
                  r'|instance)\s+(\S+)', re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
FAILS, COUNT = [], [0]


def check(code, name, cond):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + code + ' ' + name, flush=True)
    if not cond:
        FAILS.append(code)


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True)


def show(commit, path):
    r = git('show', '%s:%s' % (commit, path))
    return r.stdout if r.returncode == 0 else None


def header(text):
    i = text.find('\nimport ')
    return text[:i] if i != -1 else text


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def context_lines(text):
    """Each context line with its indented continuation lines (a `variable` block spanning several lines)."""
    lines = text.split('\n')
    out = []
    for k, line in enumerate(lines):
        if CTX.match(line):
            block = [line]
            j = k + 1
            while j < len(lines) and lines[j].startswith('  ') and line.startswith('variable'):
                block.append(lines[j])
                j += 1
            out.append('\n'.join(block))
    return out


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def stmt_end(chunk):
    """End of a theorem's statement: the first ` :=`, or a ` where` closing a line, whichever is earlier."""
    ends = [j for j in (chunk.find(' :='),) if j != -1]
    m = re.search(r' where\n', chunk)
    if m:
        ends.append(m.start())
    return min(ends) if ends else -1


def spans(text):
    """[(kind, name, start, statement end or -1, end)] for every declaration, in order."""
    out = []
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        se = -1
        if m.group(1) in ('theorem', 'lemma'):
            j = stmt_end(chunk)
            if j != -1:
                se = start + j
        out.append((m.group(1), m.group(2), start, se if se != -1 else start + len(chunk), nxt, start + len(chunk)))
    return out


def decl_chunks(text):
    """name -> (kind, statement or whole text, proof text after the statement for theorems)."""
    out = {}
    for kind, name, start, se, nxt, cend in spans(text):
        if kind in ('theorem', 'lemma'):
            out[name] = (kind, text[start:se], text[se:nxt])
        else:
            out[name] = (kind, text[start:cend], '')
    return out


def colon_index(stmt):
    """Index of the colon separating binders from the conclusion: the first at bracket depth 0 after the name."""
    m = DECL.match(stmt)
    i = m.end() if m else 0
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in '({[⦃':
            depth += 1
        elif c in ')}]⦄':
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return j
    return -1


def split_statement(stmt):
    """(binders, conclusion) of a declaration header."""
    m = DECL.match(stmt)
    i = m.end() if m else 0
    j = colon_index(stmt)
    if j == -1:
        return stmt[i:], ''
    return stmt[i:j], stmt[j + 1:]


def def_header(text):
    """A definition's header: up to ` :=` or a ` where` closing a line."""
    j = stmt_end(text)
    return text[:j] if j != -1 else text


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def norm(s):
    return ' '.join(s.split())


def fields(structure_text):
    """The field names of a structure chunk: the two-space-indented `name :` lines after `where`."""
    body = structure_text.split(' where', 1)[1] if ' where' in structure_text else ''
    return [m.group(1) for m in re.finditer(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M)]


def field_line(structure_text, name):
    body = structure_text.split(' where', 1)[1] if ' where' in structure_text else ''
    ms = list(re.finditer(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M))
    for k, m in enumerate(ms):
        if m.group(1) == name:
            return norm(body[m.start():ms[k + 1].start() if k + 1 < len(ms) else len(body)])
    return None


def token(name, text):
    return re.search(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(name), text) is not None


def sections(text):
    """[(position, label)] of the section markers, label `§A` ... or `verdict`."""
    out = []
    for m in re.finditer(r'^/-! ### (§[A-Z]|The verdict)', text, re.M):
        out.append((m.start(), 'verdict' if m.group(1) == 'The verdict' else m.group(1)))
    return out


def section_at(secs, pos):
    lab = None
    for p, l in secs:
        if p <= pos:
            lab = l
    return lab

PREFIX = 'OIBridge.K2Guard.'
# S1 -- the obstruction
FROZEN_WHOLE = ['reflY', 'CandidateCone', 'productSet', 'cnotOrbit', 'idW', 'chainW', 'rotW', 'rotChainW']
REFLY_BODY = 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i'
CANDIDATE_BODY = '(∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)'
OBSTRUCTION = ('no_candidateCone_cnot_reflY',
               '(hK : CandidateCone K) (hC : ∀ ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K)', 'False')
OBSTRUCTION_PROOF_NAMES = ('chain_eq', 'chain_value')
# S2 -- orientation controls: name -> frozen conclusion
CHAIN = 'cnot (actT reflY (cnot (prodState xplus z3)))'
ROTCHAIN = 'cnot (actT nflip (cnot (prodState xplus z3)))'
PAIR = 'prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])'
CONTROLS_A = {
    'reflY_mem_eball': 'reflY x ∈ eball 3',
    'det_reflY': 'LinearMap.det reflY = -1',
    'det_nflip': 'LinearMap.det nflip = 1',
    'chain_eq': CHAIN + ' = chainW',
    'chain_value': PAIR + ' chainW = -1 / 2',
    'candidateCone_productSet': 'CandidateCone productSet',
    'reflY_mem_productSet': 'actT reflY ω ∈ productSet',
    'candidateCone_cnotOrbit': 'CandidateCone cnotOrbit',
    'cnot_mem_cnotOrbit': 'cnot ω ∈ cnotOrbit',
    'rotation_chain_value': PAIR + ' (' + ROTCHAIN + ') = 0',
}
ORIENT_VERDICT = 'k2guard_orientation'
ORIENT_CONCL = ('(∀ K : Set (W 3), CandidateCone K → (∀ ω ∈ K, cnot ω ∈ K) → (∀ ω ∈ K, actT reflY ω ∈ K) → False) ∧ '
                'NativeGate (eball 3) z3 nflip cnot ∧ (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det reflY = -1 ∧ '
                'LinearMap.det nflip = 1 ∧ (CandidateCone cnotOrbit ∧ ∀ ω ∈ cnotOrbit, cnot ω ∈ cnotOrbit) ∧ '
                '(CandidateCone productSet ∧ ∀ ω ∈ productSet, actT reflY ω ∈ productSet) ∧ '
                + PAIR + ' (' + CHAIN + ') = -1 / 2 ∧ ' + PAIR + ' (' + ROTCHAIN + ') = 0')
# S3 -- the selectors
OG4 = ('(hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) '
       '(hV4 : SeedOrbitAvailable G r avail)')
SELECTORS = {
    'three_of_nativeGate_of_two_le': ('(hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)',
                                      'd = 3', 'dim_of_nativeGate'),
    'three_of_nativeGateOf_of_two_le': ('(hd : 2 ≤ d) (hE : EffectsOn (eball d) avail) ' + OG4 +
                                        ' (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)',
                                        'd = 3', 'dim_of_nativeGateOf'),
}
TWO_LE = ('two_le_of_entangling', '(hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) '
          '(hE : Entangling (eball d) G)', '2 ≤ d')
LOAD = ('two_le_load_bearing', 'IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1)')
SATIS = ('two_le_satisfiable', '2 ≤ 3 ∧ IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot')
ENT_VERDICT = 'k2guard_entangling'
# S4 -- premises
NEVER = ('Entangling', 'NativeGateOf', 'EffectsOn', 'SharpSeed', 'PreservesBody', 'BoundaryTransitive',
         'SeedOrbitAvailable')
WITNESS = ('NativeGate', 'IsNot', 'CandidateCone')
WITNESS_OK = {'two_le_load_bearing', 'two_le_satisfiable', 'candidateCone_productSet', 'candidateCone_cnotOrbit',
              ORIENT_VERDICT, ENT_VERDICT}
# S5 -- reuse
REUSED = ('maxCone', 'maxConeOf', 'EffectsOn', 'NativeGate', 'NativeGateOf', 'Entangling', 'EntanglingOf', 'IsNot',
          'prodState', 'actT', 'actC', 'W', 'HVec', 'eball', 'cnot', 'cnotFun', 'nflip', 'phiW', 'xplus', 'z3', 'z1',
          'neg1', 'cnot1', 'sharpEff', 'sharpVec', 'prodEffVal', 'pairVal', 'ehom', 'hom', 'homMap', 'tens',
          'dim_of_nativeGate', 'three_of_nativeGate', 'dim_of_nativeGateOf', 'three_of_nativeGateOf',
          'nativeGate_cnot', 'nativeGate_cnot1', 'isNot_nflip', 'isNot_neg1', 'cnot_prodState_mem_maxCone',
          'cnot_prodState_xplus_z3', 'sharpEff_isEffectOn', 'maxConeOf_avail_eq', 'IsEffectOn', 'pairVal_tens',
          'actT_tens', 'homMap_hom', 'ehom_dot', 'ehom_affOf')
IMPORT_ONLY = 'import OIBridge.K1Bridge'
# S6 -- neutral
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'ElementaryDrivability', 'flow', 'Flow', 'LimitClosed', 'closure', 'Tendsto', 'Filter',
                  'Dense', 'TensorProduct', 'Hilbert', 'MixingClosed', 'unitSpan')
# S7 -- phrases
PHRASES = ('OI supplies', 'derived from OI', 'sourced from OI', 'local tomography is derived',
           'physical composite cone is identified', 'physical cone is identified', 'the physical cone is',
           'reflections are forbidden', 'reflections are excluded in every', 'reflections are physically forbidden',
           'K2 is discharged', 'K∞-Act is sourced', 'K∞-Copy is derived', 'is derived from 2 ≤ d',
           '2 ≤ d implies entangl', 'equivalent to the entangling', 'every composite must preserve orientation',
           'all composites must preserve orientation', 'qubit')
# S8 -- scope
SELECTOR_SECTION = '§E'
DIM3 = re.compile(r'(?<![\w\'.])(Fin|eball|W|HVec|maxCone)\s+3(?![\w\'])|(?<![\w\'.])(cnot|nflip|reflY|z3|xplus)'
                  r'(?![\w\'])')
TWO_LE_RE = re.compile(r'2\s*≤\s*d(?![\w\'])')
TWO_LE_SECTIONS = ('§E', '§F', 'verdict')
# V -- the frozen decision rule
ORIENT_TOKENS = ('K2-ORIENTATION-OBSTRUCTION-PROVED', 'K2-ORIENTATION-NOT-ESTABLISHED')
ENT_TOKENS = ('K1-ENTANGLING-WEAKENED', 'K1-ENTANGLING-NOT-WEAKENED')


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def explicit_binders(b):
    """The binders with every implicit `{...}` group removed: the classification ignores how the variables bind."""
    return norm(re.sub(r'\{[^{}]*\}', ' ', b))


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def orientation_cell(chunks):
    """K2-ORIENTATION-OBSTRUCTION-PROVED iff: `reflY` is the frozen diag(1, -1, 1) map and `CandidateCone` the frozen
    family; `no_candidateCone_cnot_reflY` is a theorem with exactly the frozen explicit binders and conclusion `False`;
    and every orientation control is a theorem with its frozen conclusion. Otherwise K2-ORIENTATION-NOT-ESTABLISHED.
    Reads no selector statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = kinds.get('reflY') == 'def' and REFLY_BODY in norm(texts.get('reflY', ''))
    ok = ok and kinds.get('CandidateCone') == 'def' and def_body(texts.get('CandidateCone', '')) == norm(CANDIDATE_BODY)
    n, b, c = OBSTRUCTION
    bb, cc = stmt_parts(texts, n)
    ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == norm(b) and cc == norm(c)
    for m, concl in CONTROLS_A.items():
        ok = ok and kinds.get(m) == 'theorem' and stmt_parts(texts, m)[1] == norm(concl)
    return [ORIENT_TOKENS[0] if ok else ORIENT_TOKENS[1]]


def entangling_cell(chunks):
    """K1-ENTANGLING-WEAKENED iff: both selectors are theorems with exactly the frozen explicit binders and conclusion
    `d = 3`, neither statement mentions `Entangling`; and the load-bearing control `two_le_load_bearing` has its
    frozen conclusion. Otherwise K1-ENTANGLING-NOT-WEAKENED. Reads no orientation statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = True
    for n, (b, c, _) in SELECTORS.items():
        bb, cc = stmt_parts(texts, n)
        ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == norm(b) and cc == norm(c) and \
            not token('Entangling', texts.get(n, ''))
    ok = ok and kinds.get(LOAD[0]) == 'theorem' and stmt_parts(texts, LOAD[0])[1] == norm(LOAD[1])
    return [ENT_TOKENS[0] if ok else ENT_TOKENS[1]]


def verdicts(chunks):
    return orientation_cell(chunks), entangling_cell(chunks)


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    bad1 = [n for n in FROZEN_WHOLE if texts.get(n) != TEXTS.get(n) or kinds.get(n) not in ('def', 'noncomputable def')]
    if REFLY_BODY not in norm(texts.get('reflY', '')):
        bad1.append('reflY body')
    if def_body(texts.get('CandidateCone', '')) != norm(CANDIDATE_BODY):
        bad1.append('CandidateCone body')
    n, b, c = OBSTRUCTION
    bb, cc = stmt_parts(texts, n)
    if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c) or PREFIX + n not in prints or \
            not all(token(m, proofs.get(n, '')) for m in OBSTRUCTION_PROOF_NAMES):
        bad1.append(n)
    check('S1', 'the obstruction over the frozen family with the frozen binders, conclusion False, proved through the '
                'chain%s%s' % (tag, (' %s' % bad1[:3]) if bad1 else ''), not bad1)
    # S2
    bad2 = [m for m, concl in CONTROLS_A.items()
            if kinds.get(m) != 'theorem' or stmt_parts(texts, m)[1] != norm(concl) or PREFIX + m not in prints]
    if stmt_parts(texts, ORIENT_VERDICT)[1] != norm(ORIENT_CONCL):
        bad2.append(ORIENT_VERDICT)
    check('S2', 'the orientation controls with their frozen conclusions and prints%s%s'
          % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    bad3 = []
    for n, (b, c, dep) in SELECTORS.items():
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c) or \
                not token(dep, proofs.get(n, '')) or token('Entangling', texts.get(n, '')) or PREFIX + n not in prints:
            bad3.append(n)
    n, b, c = TWO_LE
    bb, cc = stmt_parts(texts, n)
    if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c):
        bad3.append(n)
    for m, (k, t, _) in chunks.items():
        if k == 'theorem' and m != n and stmt_parts(texts, m)[1] == norm('2 ≤ d'):
            bad3.append(m)
    for m, concl in (LOAD, SATIS):
        if kinds.get(m) != 'theorem' or stmt_parts(texts, m)[1] != norm(concl):
            bad3.append(m)
    check('S3', 'the two 2 ≤ d selectors with the frozen binders, conclusion d = 3, DIM-1 / K1-BRIDGE-1 by name, no '
                'Entangling; 2 ≤ d from the entangling clause only in two_le_of_entangling%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = []
    for m, (k, t, _) in chunks.items():
        if k in ('theorem', 'lemma'):
            concl = norm(split_statement(t)[1])
        else:
            concl = norm(split_statement(def_header(t))[1])
        if m == ENT_VERDICT:
            for p in NEVER:
                for mm in re.finditer(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(p), concl):
                    rest = concl[mm.end():]
                    j = rest.find(' →')
                    if j == -1 or any(s in rest[:j] for s in (' ∧ ', ' ∨ ', ') ∧', ') ∨')):
                        bad4.append(m)
            continue
        if any(token(p, concl) for p in NEVER):
            bad4.append(m)
        if m not in WITNESS_OK and any(token(p, concl) for p in WITNESS):
            bad4.append(m)
    check('S4', 'no premise concluded of a hypothesis-bound object; witnesses only by the named controls%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S5', 'landed objects reused, not re-declared; the only import is OIBridge.K1Bridge%s%s'
          % (tag, (' %s' % clash[:3]) if clash else ''), not clash and imports == [IMPORT_ONLY])
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no drive, flow, limit, closure or density token%s%s' % (tag, (' %s' % hits) if hits else ''),
          not hits)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    secs = sections(mod)
    bad8 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        sec = section_at(secs, start)
        body = code_only(mod[start:nxt])
        if sec == SELECTOR_SECTION and DIM3.search(body):
            bad8.append(name)
        if sec not in TWO_LE_SECTIONS and TWO_LE_RE.search(body):
            bad8.append(name)
    check('S8', 'the selector section is dimension-generic; 2 ≤ d only in §E, §F and the verdicts%s%s'
          % (tag, (' %s' % bad8[:3]) if bad8 else ''), not bad8)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    o, e = verdicts(chunks)
    check('V', 'one outcome per cell by the frozen rules: %s, %s%s' % (o, e, tag), len(o) == 1 and len(e) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in ORIENT_TOKENS + ENT_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context block unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    chunks = decl_chunks(mod)
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s'
          % (tag, (' (changed: %s)' % ', '.join(bad[:4])) if bad else ''), not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in PRINTS))
    semantic_checks(mod, chunks, prints, tag)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_want(d_text):
    d = json.loads(d_text)
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['modules'] == PREV_FAMILY_MODULES]
    if len(k) != 1:
        return None
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return json.dumps(want, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, e_text):
    try:
        want = census_want(d_text)
    except Exception:
        return False
    return want is not None and e_text == want


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    mod = show(commit, MOD)
    module_checks(mod)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        o, e = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (o + e, toks), len(o) == 1 and len(e) == 1 and sorted(toks) == sorted(o + e))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the K1-BRIDGE-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    o, e = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
    print('VERDICT  ORIENTATION  %s' % ('/'.join(o) or 'none'))
    print('VERDICT  ENTANGLING   %s' % ('/'.join(e) or 'none'))
    check('V', 'exactly one outcome per cell', len(o) == 1 and len(e) == 1)

def must_fail(code, label, mod2):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mod2)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def append_decl(text, decl):
    """Insert a declaration just before the verdict section (inside §P)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_before(text, anchor, decl):
    i = text.index(anchor)
    return text[:i] + decl + '\n\n' + text[i:]

def append_control(text, decl):
    """Insert a declaration just before the verdict section."""
    i = text.index('\n/-! ### The verdicts')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_in_section(text, marker, decl):
    """Insert a declaration just before the section marker that follows `marker`."""
    i = text.index(marker)
    return text[:i] + decl + '\n\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


OBS_HEAD = ('theorem no_candidateCone_cnot_reflY {K : Set (W 3)} (hK : CandidateCone K)\n'
            '    (hC : ∀ ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K) : False := by')
SEL_HEAD = ('    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n'
            '    d = 3 := by')
REL_TAIL = '    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3 := by'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    o, e = verdict_of(mod)
    check('T', 'the reference module reads %s and %s' % (o, e), o == [ORIENT_TOKENS[0]] and e == [ENT_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration',
              replace_once(mod, '\ntheorem k2guard_entangling :', '\ntheorem k2guard_entangling\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {Ω : Set (Fin d → ℝ)}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace K1Bridge\n', '\nopen EffectSpace\n'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem reflY_reflY (x : Fin 3 → ℝ) : reflY (reflY x) = x := by',
                           'theorem reflY_reflY (x : Fin 3 → ℝ) : reflY (reflY (reflY x)) = reflY x := by'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.K2Guard.chain_eq\n', ''))
    # S1
    must_fail('S1', 'the reflection replaced by a rotation',
              replace_once(mod, 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i',
                           'toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i'))
    must_fail('S1', 'the candidate family narrowed by an extra condition',
              replace_once(mod, '  (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)\n',
                           '  (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3) ∧ '
                           'K.Countable\n'))
    must_fail('S1', 'an extra hypothesis on the obstruction',
              replace_once(mod, OBS_HEAD, OBS_HEAD.replace('(hR : ∀ ω ∈ K, actT reflY ω ∈ K) : False',
                                                           '(hR : ∀ ω ∈ K, actT reflY ω ∈ K) (hP : K.Nonempty) : '
                                                           'False')))
    must_fail('S1', 'the obstruction proved without the chain',
              replace_once(replace_once(mod, '  rw [chain_value] at hv\n  norm_num at hv',
                                        '  exact absurd hv (by norm_num)'),
                           ':= by rw [← chain_eq]; exact hK.2 h2', ':= hK.2 (by simpa using h2)'))
    # S2
    must_fail('S2', 'the rotation control weakened',
              replace_once(mod, '      (cnot (actT nflip (cnot (prodState xplus z3)))) = 0 := by',
                           '      (cnot (actT nflip (cnot (prodState xplus z3)))) ≤ 0 := by'))
    must_fail('S2', 'the determinant control dropped from the verdict',
              replace_once(mod, '    (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det reflY = -1 ∧ '
                                'LinearMap.det nflip = 1 ∧\n',
                           '    (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det nflip = 1 ∧\n'))
    # S3
    must_fail('S3', 'the entangling clause added to the selector',
              replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hG : NativeGate (eball d) z N G) :',
                                                           '(hG : NativeGate (eball d) z N G)\n'
                                                           '    (hE : Entangling (eball d) G) :')))
    must_fail('S3', '`2 ≤ d` dropped from the selector',
              replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hd : 2 ≤ d) ', '')))
    must_fail('S3', 'the relative selector with K1-BRIDGE-1\'s `0 < d` only',
              replace_once(mod, 'theorem three_of_nativeGateOf_of_two_le (hd : 2 ≤ d)',
                           'theorem three_of_nativeGateOf_of_two_le (hd : 0 < d)'))
    must_fail('S3', 'a second theorem concluding `2 ≤ d`',
              append_control(mod, 'theorem two_le_free (hd : 3 ≤ d) : 2 ≤ d := by omega'))
    # S4
    must_fail('S4', 'the entangling clause concluded from `2 ≤ d`',
              append_control(mod, 'theorem entangling_of_two_le {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) : '
                                  'Entangling (eball d) G := by\n  exact absurd hd (by omega)'))
    must_fail('S4', 'a native gate concluded for a hypothesis-bound gate',
              append_control(mod, 'theorem gate_free {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n'
                                  '    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) : NativeGate (eball d) z N G := by\n'
                                  '  exact absurd hd (by omega)'))
    # S5
    must_fail('S5', 'a landed definition re-declared', append_control(mod, 'def maxCone : ℕ := 0'))
    must_fail('S5', 'a second import',
              replace_once(mod, 'import OIBridge.K1Bridge\n', 'import OIBridge.K1Bridge\nimport OIBridge.SubstratumSource\n'))
    # S6
    must_fail('S6', 'a complex scalar', append_control(mod, 'def cvec (z : Fin 3 → ℂ) : Fin 3 → ℂ := z'))
    must_fail('S6', 'a closure token',
              append_control(mod, 'def closedFamily (A : Set (W 3)) : Prop := closure A ⊆ A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  (A) The candidate-cone family', '  The physical cone is identified. (A) The '
                                                                     'candidate-cone family'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('No candidate cone is invariant under cnot and the one-copy reflection; 2 ≤ d stays a '
                          'premise.')
          and phrase_hits('Hence reflections are\nphysically forbidden.') == ['reflections are physically forbidden'])
    # S8
    must_fail('S8', 'a dimension-three object in the selector section',
              insert_in_section(mod, '/-! ### §F', 'theorem three_ball_sel : eball 3 = eball 3 := rfl'))
    must_fail('S8', '`2 ≤ d` in the orientation section',
              insert_in_section(mod, '/-! ### §B', 'theorem two_le_A (hd : 2 ≤ d) : 1 ≤ d := by omega'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.K2Guard.k2guard_entangling\n',
                           '#print axioms OIBridge.K2Guard.k2guard_entangling\n'
                           '#print axioms OIBridge.K2Guard.reflY_reflY\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.K2Guard.chain_value\n',
                           '#print axioms OIBridge.K2Guard.chain_value\n#print axioms OIBridge.K2Guard.chain_value\n'))
    # V -- each cell reads its alternative, independently of the other
    m_rot = replace_once(mod, 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i',
                         'toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i')
    check('M', 'decision rule: the reflection replaced by a rotation reads ORIENTATION-NOT-ESTABLISHED and leaves the '
               'entangling cell unchanged', verdict_of(m_rot) == ([ORIENT_TOKENS[1]], [ENT_TOKENS[0]]))
    m_ent = replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hG : NativeGate (eball d) z N G) :',
                                                         '(hG : NativeGate (eball d) z N G)\n'
                                                         '    (hE : Entangling (eball d) G) :'))
    check('M', 'decision rule: the entangling clause in the selector reads ENTANGLING-NOT-WEAKENED and leaves the '
               'orientation cell unchanged', verdict_of(m_ent) == ([ORIENT_TOKENS[0]], [ENT_TOKENS[1]]))
    m_rel = replace_once(mod, REL_TAIL, REL_TAIL.replace(' : d = 3 := by', ' : d = 1 ∨ d = 3 := by'))
    check('M', 'decision rule: the relative selector concluding only d ∈ {1, 3} reads ENTANGLING-NOT-WEAKENED',
          verdict_of(m_rel)[1] == [ENT_TOKENS[1]])
    m_ctl = replace_once(mod, 'theorem candidateCone_cnotOrbit : CandidateCone cnotOrbit := by',
                         'theorem candidateCone_cnotOrbit : CandidateCone productSet := by')
    check('M', 'decision rule: a weakened non-vacuity control reads ORIENTATION-NOT-ESTABLISHED',
          verdict_of(m_ctl)[0] == [ORIENT_TOKENS[1]])
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('K2-ORIENTATION-OBSTRUCTION-PROVED and K1-ENTANGLING-WEAKENED.')
          == ['K2-ORIENTATION-OBSTRUCTION-PROVED', 'K1-ENTANGLING-WEAKENED']
          and note_tokens('K1-ENTANGLING-WEAKENED, not K1-ENTANGLING-NOT-WEAKENED.')
          == ['K1-ENTANGLING-WEAKENED', 'K1-ENTANGLING-NOT-WEAKENED'])
    # I, C
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    good = census_want(d_cen)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['modules'] == PREV_FAMILY_MODULES][0]
    bad_status = json.loads(good)
    bad_status['families'][k + 1]['status'] = 'carried'
    bad_status = json.dumps(bad_status, indent=2, ensure_ascii=False) + '\n'
    moved = json.loads(good)
    moved['families'].insert(k, moved['families'].pop(k + 1))
    moved = json.dumps(moved, indent=2, ensure_ascii=False) + '\n'
    check('M', 'census: the frozen edit passes; a changed status, a moved family, a whitespace change and the '
               'unchanged file fail',
          census_ok(d_cen, good) and not census_ok(d_cen, bad_status) and moved != good
          and not census_ok(d_cen, moved) and not census_ok(d_cen, good.replace('\n', '\n ', 1))
          and not census_ok(d_cen, d_cen))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) == 2 and argv[0] == 'verdict':
        print_verdicts(argv[1])
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
