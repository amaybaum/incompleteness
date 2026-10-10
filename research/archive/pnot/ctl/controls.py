#!/usr/bin/env python3
"""controls.py -- round PARITY-NOT-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the three cells computed from the module's statements at <commit> and the
                                            landed statements at D

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  relations   `GateRel` is a structure with exactly the two fields `relT` and `relC`, each the landed
                  `NativeGate` field read from D, and the frozen header
  S2  parity      each of the two parity theorems is its landed `NativeGate` partner read from D with the hypothesis
                  `(hG : NativeGate (eball d) z N G)` replaced by `(hR : GateRel N G)` and nothing else; every
                  OIBridge identifier of the pair resolves to the same unique declaration in both contexts; no
                  declaration of §A except `gateRel_of_nativeGate` mentions the native gate, the frame or positivity
  S3  the NOT     the four `d = 3` theorems take exactly `IsNot (eball 3) z N` and `GateRel N G` and have their frozen
                  conclusions; no declaration of §B except the three `NativeGate` corollaries mentions the native gate,
                  the frame or positivity, and each corollary is its `GateRel` theorem with the hypothesis
                  `(hG : NativeGate (eball 3) z N G)` and is proved through `gateRel_of_nativeGate`
  S4  controls    `refl3` and `negId3` are the frozen diagonal maps, NOTs of `eball 3` with axis `z3`, of
                  determinant `-1`, for which no gate satisfies the relations; `cnot` with `nflip` satisfies them,
                  through the landed `cnot_relT` and `cnot_relC` read from D
  S5  separation  for `d = 3` and `d = 5`: the gate and the witness are the frozen definitions; the frame theorem is the
                  landed `NativeGate` frame field read from D at the gate; the gate satisfies `GateRel`; the image of
                  the frozen product pairs to `-1 / 10` with the two frozen sharp effects; the forward-positivity
                  failure is the negation of the landed `posFwd` field at the gate, proved through that value; no
                  declaration of §D-§F names a landed dimension corollary of the native gate
  S6  scope       no declaration mentions a complex field, the landed `d = 1` gate or a landed dimension selector, no
                  statement mentions the landed `d = 1` NOT or axis, and no theorem concludes an equation or inequation
                  on `d`
  S7  reuse       no declaration of the module shares its name with an OIBridge declaration visible to it; the only
                  import is `OIBridge.EffectSpace`
  S8  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements and the landed statements at D by its own frozen
                  rule, independently of the others; at a commit carrying the result note, the note states exactly the
                  computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.DenseOrbit`
  C   census      the census is D's with exactly the frozen family inserted after the KTRANS-DENSE-1 family, byte for
                  byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = 'e26493394f388a891c2dd03be2696286a89293f7'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-parity-not-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = LEAN + 'ParityNot.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '44b30d27dcd388e001fbee9adec589b602130a59'
ANCHOR_IMPORT = 'import OIBridge.DenseOrbit\n'
NEW_IMPORT = 'import OIBridge.ParityNot\n'
PREV_FAMILY_MODULES = ['DenseOrbit']
CENSUS_FAMILY = json.loads(r'''{
 "name": "DIM-1's parity count from the target and control relations alone, the π-rotation NOT those relations force at d = 3, and forward positivity as a separate condition on the gate at d = 3 and d = 5 (round PARITY-NOT-1, reconstruction)",
 "modules": [
  "ParityNot"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round PARITY-NOT-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-parity-not-1/preregistration.md. GateRel N G is the target relation relT and the control relation relC of DIM-1's NativeGate, without the frame or positivity. Q-REL: with IsNot (eball d) z N and GateRel N G the +1 and −1 eigenspaces of the homogenized NOT have equal dimension and d is odd (finrank_plus_eq_finrank_minus_rel, not_even_of_gateRel), DIM-1's finrank_plus_eq_finrank_minus and not_even_of_nativeGate with NativeGate replaced by GateRel. Q-NOT: at d = 3, with IsNot (eball 3) z N and GateRel N G, both eigenspaces have dimension two, tangentPlus N = 1, N x = 2 (u · x) u − x for a unit u, and det N = 1 (finrank_plus_minus_three, tangentPlus_three, piRotation_three, det_three), with NativeGate corollaries; the reflection diag(1, 1, −1) and −id are NOTs of eball 3 for which no gate satisfies the relations, both of determinant −1 (not_gateRel_refl3, not_gateRel_negId3, det_refl3, det_negId3), and cnot with nflip satisfies them (gateRel_cnot). Q-SEP: the permutation gates gJ3 (with nflip on eball 3) and gJ5 (with n5 = diag(1, 1, −1, −1, −1) on eball 5) satisfy NativeGate's frame and GateRel, and the image of an explicit pure product pairs to −1/10 with two sharp effects, so forward positivity fails (gJ3_frame, gateRel_gJ3, gJ3_value, not_posFwd_gJ3; gJ5_frame, gateRel_gJ5, gJ5_value, not_posFwd_gJ5). Carried by no manuscript. The round selects no dimension, concerns no complex structure and no NOT of a physical theory, and does not claim that d = 5 is the only dimension at which the relations hold without positivity."
}''')
DECLS = json.loads(r'''[
 [
  "structure",
  "GateRel"
 ],
 [
  "theorem",
  "gateRel_of_nativeGate"
 ],
 [
  "theorem",
  "opGate_comp_homMap_rel"
 ],
 [
  "theorem",
  "opGate_homMap_comp_rel"
 ],
 [
  "theorem",
  "Lop_anti_rel"
 ],
 [
  "theorem",
  "Lop_eq_zero_rel"
 ],
 [
  "theorem",
  "Lop_injective_rel"
 ],
 [
  "theorem",
  "finrank_plus_eq_finrank_minus_rel"
 ],
 [
  "theorem",
  "not_even_of_gateRel"
 ],
 [
  "theorem",
  "finrank_plus_minus_three"
 ],
 [
  "theorem",
  "tangentPlus_three"
 ],
 [
  "theorem",
  "piRotation_three"
 ],
 [
  "theorem",
  "det_eq_one_of_piRotation"
 ],
 [
  "theorem",
  "det_three"
 ],
 [
  "theorem",
  "tangentPlus_of_nativeGate_three"
 ],
 [
  "theorem",
  "piRotation_of_nativeGate_three"
 ],
 [
  "theorem",
  "det_of_nativeGate_three"
 ],
 [
  "def",
  "diagSign"
 ],
 [
  "theorem",
  "diagSign_apply"
 ],
 [
  "theorem",
  "homMap_diagSign"
 ],
 [
  "def",
  "refl3"
 ],
 [
  "def",
  "negId3"
 ],
 [
  "theorem",
  "negId3_eq"
 ],
 [
  "theorem",
  "isNot_refl3"
 ],
 [
  "theorem",
  "isNot_negId3"
 ],
 [
  "theorem",
  "minusSpace_refl3_le"
 ],
 [
  "theorem",
  "plusSpace_negId3_le"
 ],
 [
  "theorem",
  "finrank_minusSpace_refl3_le"
 ],
 [
  "theorem",
  "finrank_plusSpace_negId3_le"
 ],
 [
  "theorem",
  "not_gateRel_refl3"
 ],
 [
  "theorem",
  "not_gateRel_negId3"
 ],
 [
  "theorem",
  "det_refl3"
 ],
 [
  "theorem",
  "det_negId3"
 ],
 [
  "theorem",
  "gateRel_cnot"
 ],
 [
  "theorem",
  "tangentPlus_nflip"
 ],
 [
  "theorem",
  "det_nflip_rel"
 ],
 [
  "def",
  "sgate"
 ],
 [
  "theorem",
  "sgate_sgate"
 ],
 [
  "def",
  "sgateEquiv"
 ],
 [
  "theorem",
  "sgateEquiv_apply"
 ],
 [
  "theorem",
  "sgate_relT"
 ],
 [
  "theorem",
  "sgate_relC"
 ],
 [
  "def",
  "odd3"
 ],
 [
  "def",
  "perm3"
 ],
 [
  "theorem",
  "perm3_perm3"
 ],
 [
  "theorem",
  "odd3_perm3"
 ],
 [
  "def",
  "gJ3"
 ],
 [
  "theorem",
  "gJ3_apply"
 ],
 [
  "theorem",
  "homMap_nflip_sign"
 ],
 [
  "theorem",
  "gJ3_frame"
 ],
 [
  "theorem",
  "gateRel_gJ3"
 ],
 [
  "noncomputable def",
  "w3"
 ],
 [
  "theorem",
  "w3_unit"
 ],
 [
  "theorem",
  "sharpVec_w3"
 ],
 [
  "theorem",
  "sharpVec_z3"
 ],
 [
  "theorem",
  "gJ3_value"
 ],
 [
  "theorem",
  "gJ3_not_mem_maxCone"
 ],
 [
  "theorem",
  "not_posFwd_gJ3"
 ],
 [
  "theorem",
  "not_nativeGate_gJ3"
 ],
 [
  "def",
  "odd5"
 ],
 [
  "def",
  "perm5"
 ],
 [
  "theorem",
  "perm5_perm5"
 ],
 [
  "theorem",
  "odd5_perm5"
 ],
 [
  "def",
  "c5"
 ],
 [
  "def",
  "n5"
 ],
 [
  "def",
  "z5"
 ],
 [
  "def",
  "x5"
 ],
 [
  "theorem",
  "c5_sq"
 ],
 [
  "theorem",
  "homMap_n5_sign"
 ],
 [
  "theorem",
  "isNot_n5"
 ],
 [
  "theorem",
  "x5_mem"
 ],
 [
  "theorem",
  "z5_mem"
 ],
 [
  "def",
  "gJ5"
 ],
 [
  "theorem",
  "gJ5_apply"
 ],
 [
  "theorem",
  "hom5_one"
 ],
 [
  "theorem",
  "hom5_two"
 ],
 [
  "theorem",
  "hom5_three"
 ],
 [
  "theorem",
  "hom5_four"
 ],
 [
  "theorem",
  "hom5_five"
 ],
 [
  "theorem",
  "gJ5_frame"
 ],
 [
  "theorem",
  "gateRel_gJ5"
 ],
 [
  "theorem",
  "finrank_plus_eq_finrank_minus_n5"
 ],
 [
  "noncomputable def",
  "w5"
 ],
 [
  "theorem",
  "w5_unit"
 ],
 [
  "theorem",
  "z5_unit"
 ],
 [
  "theorem",
  "sharpVec_w5"
 ],
 [
  "theorem",
  "sharpVec_z5"
 ],
 [
  "theorem",
  "sum_univ_six'"
 ],
 [
  "theorem",
  "gJ5_value"
 ],
 [
  "theorem",
  "gJ5_not_mem_maxCone"
 ],
 [
  "theorem",
  "not_posFwd_gJ5"
 ],
 [
  "theorem",
  "not_nativeGate_gJ5"
 ]
]''')
TEXTS = json.loads(r'''{
 "GateRel": "structure GateRel (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where\n  relT : ∀ ω, actT N (G (actT N ω)) = G ω\n  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
 "gateRel_of_nativeGate": "theorem gateRel_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) :\n    GateRel N G",
 "opGate_comp_homMap_rel": "theorem opGate_comp_homMap_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G)\n    (F : HVec d →ₗ[ℝ] HVec d) : opGate G (F ∘ₗ homMap N) = opGate G F ∘ₗ homMap N",
 "opGate_homMap_comp_rel": "theorem opGate_homMap_comp_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G)\n    (F : HVec d →ₗ[ℝ] HVec d) :\n    opGate G (homMap N ∘ₗ F) = homMap N ∘ₗ opGate G F ∘ₗ homMap N",
 "Lop_anti_rel": "theorem Lop_anti_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hR : GateRel N G) (f : OpSpace N) :\n    Lop G hN.invol (Pop N f) = - Pop N (Lop G hN.invol f)",
 "Lop_eq_zero_rel": "theorem Lop_eq_zero_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hR : GateRel N G) (f : OpSpace N)\n    (hf : Lop G hN.invol f = 0) : f = 0",
 "Lop_injective_rel": "theorem Lop_injective_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) :\n    Function.Injective (Lop G hN.invol)",
 "finrank_plus_eq_finrank_minus_rel": "theorem finrank_plus_eq_finrank_minus_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) :\n    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)",
 "not_even_of_gateRel": "theorem not_even_of_gateRel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d",
 "finrank_plus_minus_three": "theorem finrank_plus_minus_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}\n    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) :\n    Module.finrank ℝ (plusSpace N) = 2 ∧ Module.finrank ℝ (minusSpace N) = 2",
 "tangentPlus_three": "theorem tangentPlus_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}\n    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) : tangentPlus N = 1",
 "piRotation_three": "theorem piRotation_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}\n    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) :\n    ∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x",
 "det_eq_one_of_piRotation": "theorem det_eq_one_of_piRotation {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {u : Fin 3 → ℝ}\n    (hu : ∑ j, u j ^ 2 = 1) (hN : ∀ x, N x = (2 * ∑ j, u j * x j) • u - x) :\n    LinearMap.det N = 1",
 "det_three": "theorem det_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G : W 3 ≃ₗ[ℝ] W 3}\n    (hN : IsNot (eball 3) z N) (hR : GateRel N G) : LinearMap.det N = 1",
 "tangentPlus_of_nativeGate_three": "theorem tangentPlus_of_nativeGate_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}\n    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) :\n    tangentPlus N = 1",
 "piRotation_of_nativeGate_three": "theorem piRotation_of_nativeGate_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}\n    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) :\n    ∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x",
 "det_of_nativeGate_three": "theorem det_of_nativeGate_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}\n    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) :\n    LinearMap.det N = 1",
 "diagSign": "def diagSign (c : Fin d → ℝ) : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ) where\n  toFun x := fun i => c i * x i\n  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]\n  map_smul' a x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring",
 "diagSign_apply": "theorem diagSign_apply (c x : Fin d → ℝ) (i : Fin d) : diagSign c x i = c i * x i",
 "homMap_diagSign": "theorem homMap_diagSign (c : Fin d → ℝ) (v : HVec d) (μ : Fin (d + 1)) :\n    homMap (diagSign c) v μ = Matrix.vecCons 1 c μ * v μ",
 "refl3": "def refl3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![1, 1, -1]",
 "negId3": "def negId3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![-1, -1, -1]",
 "negId3_eq": "theorem negId3_eq : negId3 = -LinearMap.id",
 "isNot_refl3": "theorem isNot_refl3 : IsNot (eball 3) z3 refl3",
 "isNot_negId3": "theorem isNot_negId3 : IsNot (eball 3) z3 negId3",
 "minusSpace_refl3_le": "theorem minusSpace_refl3_le :\n    minusSpace refl3 ≤ Submodule.span ℝ {(Pi.single 3 1 : HVec 3)}",
 "plusSpace_negId3_le": "theorem plusSpace_negId3_le :\n    plusSpace negId3 ≤ Submodule.span ℝ {(Pi.single 0 1 : HVec 3)}",
 "finrank_minusSpace_refl3_le": "theorem finrank_minusSpace_refl3_le : Module.finrank ℝ (minusSpace refl3) ≤ 1",
 "finrank_plusSpace_negId3_le": "theorem finrank_plusSpace_negId3_le : Module.finrank ℝ (plusSpace negId3) ≤ 1",
 "not_gateRel_refl3": "theorem not_gateRel_refl3 (G : W 3 ≃ₗ[ℝ] W 3) : ¬ GateRel refl3 G",
 "not_gateRel_negId3": "theorem not_gateRel_negId3 (G : W 3 ≃ₗ[ℝ] W 3) : ¬ GateRel negId3 G",
 "det_refl3": "theorem det_refl3 : LinearMap.det refl3 = -1",
 "det_negId3": "theorem det_negId3 : LinearMap.det negId3 = -1",
 "gateRel_cnot": "theorem gateRel_cnot : GateRel nflip cnot",
 "tangentPlus_nflip": "theorem tangentPlus_nflip : tangentPlus nflip = 1",
 "det_nflip_rel": "theorem det_nflip_rel : LinearMap.det nflip = 1",
 "sgate": "def sgate (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1)) (ω : W d) : W d :=\n  fun μ ν => if odd ν then ω (p μ) ν else ω μ ν",
 "sgate_sgate": "theorem sgate_sgate (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1))\n    (hp : ∀ μ, p (p μ) = μ) (ω : W d) : sgate odd p (sgate odd p ω) = ω",
 "sgateEquiv": "def sgateEquiv (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1))\n    (hp : ∀ μ, p (p μ) = μ) : W d ≃ₗ[ℝ] W d where\n  toFun := sgate odd p\n  invFun := sgate odd p\n  map_add' ω ω' := by\n    funext μ ν\n    simp only [sgate, Pi.add_apply]\n    split_ifs <;> rfl\n  map_smul' c ω := by\n    funext μ ν\n    simp only [sgate, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]\n    split_ifs <;> rfl\n  left_inv := sgate_sgate odd p hp\n  right_inv := sgate_sgate odd p hp",
 "sgateEquiv_apply": "theorem sgateEquiv_apply (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1))\n    (hp : ∀ μ, p (p μ) = μ) (ω : W d) : sgateEquiv odd p hp ω = sgate odd p ω",
 "sgate_relT": "theorem sgate_relT {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool}\n    {p : Fin (d + 1) → Fin (d + 1)}\n    (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) * v μ) (ω : W d) :\n    actT N (sgate odd p (actT N ω)) = sgate odd p ω",
 "sgate_relC": "theorem sgate_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool}\n    {p : Fin (d + 1) → Fin (d + 1)}\n    (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) * v μ)\n    (hodd : ∀ μ, odd (p μ) = !odd μ) (ω : W d) :\n    actC N (sgate odd p (actC N ω)) = actT N (sgate odd p ω)",
 "odd3": "def odd3 : Fin 4 → Bool\n  | 0 => false | 1 => false | 2 => true | 3 => true",
 "perm3": "def perm3 : Fin 4 → Fin 4\n  | 0 => 3 | 1 => 2 | 2 => 1 | 3 => 0",
 "perm3_perm3": "theorem perm3_perm3 : ∀ μ, perm3 (perm3 μ) = μ",
 "odd3_perm3": "theorem odd3_perm3 : ∀ μ, odd3 (perm3 μ) = !odd3 μ",
 "gJ3": "def gJ3 : W 3 ≃ₗ[ℝ] W 3 := sgateEquiv odd3 perm3 perm3_perm3",
 "gJ3_apply": "theorem gJ3_apply (ω : W 3) : gJ3 ω = sgate odd3 perm3 ω",
 "homMap_nflip_sign": "theorem homMap_nflip_sign (v : HVec 3) (μ : Fin (3 + 1)) :\n    homMap nflip v μ = (if odd3 μ then -1 else 1) * v μ",
 "gJ3_frame": "theorem gJ3_frame (a b : Fin 2) :\n    gJ3 (prodState (corner z3 a) (corner z3 b)) = prodState (corner z3 a) (corner z3 (a + b))",
 "gateRel_gJ3": "theorem gateRel_gJ3 : GateRel nflip gJ3",
 "w3": "noncomputable def w3 : Fin 3 → ℝ := ![0, -3 / 5, -4 / 5]",
 "w3_unit": "theorem w3_unit : ∑ j, w3 j ^ 2 = 1",
 "sharpVec_w3": "theorem sharpVec_w3 : sharpVec w3 = ![1 / 2, 0, -3 / 10, -2 / 5]",
 "sharpVec_z3": "theorem sharpVec_z3 : sharpVec z3 = ![1 / 2, 0, 0, 1 / 2]",
 "gJ3_value": "theorem gJ3_value :\n    prodEffVal (sharpEff w3) (sharpEff z3) (gJ3 (prodState xplus z3)) = -1 / 10",
 "gJ3_not_mem_maxCone": "theorem gJ3_not_mem_maxCone : gJ3 (prodState xplus z3) ∉ maxCone (eball 3)",
 "not_posFwd_gJ3": "theorem not_posFwd_gJ3 :\n    ¬ ∀ x ∈ eball 3, ∀ y ∈ eball 3, gJ3 (prodState x y) ∈ maxCone (eball 3)",
 "not_nativeGate_gJ3": "theorem not_nativeGate_gJ3 : ¬ NativeGate (eball 3) z3 nflip gJ3",
 "odd5": "def odd5 : Fin 6 → Bool\n  | 0 => false | 1 => false | 2 => false | 3 => true | 4 => true | 5 => true",
 "perm5": "def perm5 : Fin 6 → Fin 6\n  | 0 => 5 | 1 => 3 | 2 => 4 | 3 => 1 | 4 => 2 | 5 => 0",
 "perm5_perm5": "theorem perm5_perm5 : ∀ μ, perm5 (perm5 μ) = μ",
 "odd5_perm5": "theorem odd5_perm5 : ∀ μ, odd5 (perm5 μ) = !odd5 μ",
 "c5": "def c5 (j : Fin 5) : ℝ := if odd5 j.succ then -1 else 1",
 "n5": "def n5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign c5",
 "z5": "def z5 : Fin 5 → ℝ := fun i => if i = 4 then 1 else 0",
 "x5": "def x5 : Fin 5 → ℝ := fun i => if i = 0 then 1 else 0",
 "c5_sq": "theorem c5_sq (j : Fin 5) : c5 j ^ 2 = 1",
 "homMap_n5_sign": "theorem homMap_n5_sign (v : HVec 5) (μ : Fin (5 + 1)) :\n    homMap n5 v μ = (if odd5 μ then -1 else 1) * v μ",
 "isNot_n5": "theorem isNot_n5 : IsNot (eball 5) z5 n5",
 "x5_mem": "theorem x5_mem : x5 ∈ eball 5",
 "z5_mem": "theorem z5_mem : z5 ∈ eball 5",
 "gJ5": "def gJ5 : W 5 ≃ₗ[ℝ] W 5 := sgateEquiv odd5 perm5 perm5_perm5",
 "gJ5_apply": "theorem gJ5_apply (ω : W 5) : gJ5 ω = sgate odd5 perm5 ω",
 "hom5_one": "@[simp] theorem hom5_one (x : Fin 5 → ℝ) : hom x (1 : Fin (5 + 1)) = x 0",
 "hom5_two": "@[simp] theorem hom5_two (x : Fin 5 → ℝ) : hom x (2 : Fin (5 + 1)) = x 1",
 "hom5_three": "@[simp] theorem hom5_three (x : Fin 5 → ℝ) : hom x (3 : Fin (5 + 1)) = x 2",
 "hom5_four": "@[simp] theorem hom5_four (x : Fin 5 → ℝ) : hom x (4 : Fin (5 + 1)) = x 3",
 "hom5_five": "@[simp] theorem hom5_five (x : Fin 5 → ℝ) : hom x (5 : Fin (5 + 1)) = x 4",
 "gJ5_frame": "theorem gJ5_frame (a b : Fin 2) :\n    gJ5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))",
 "gateRel_gJ5": "theorem gateRel_gJ5 : GateRel n5 gJ5",
 "finrank_plus_eq_finrank_minus_n5": "theorem finrank_plus_eq_finrank_minus_n5 :\n    Module.finrank ℝ (plusSpace n5) = Module.finrank ℝ (minusSpace n5)",
 "w5": "noncomputable def w5 : Fin 5 → ℝ := fun i => if i = 2 then -3 / 5 else if i = 4 then -4 / 5 else 0",
 "w5_unit": "theorem w5_unit : ∑ j, w5 j ^ 2 = 1",
 "z5_unit": "theorem z5_unit : ∑ j, z5 j ^ 2 = 1",
 "sharpVec_w5": "theorem sharpVec_w5 : sharpVec w5 = fun μ : Fin (5 + 1) =>\n    if μ = 0 then 1 / 2 else if μ = 3 then -3 / 10 else if μ = 5 then -2 / 5 else 0",
 "sharpVec_z5": "theorem sharpVec_z5 : sharpVec z5 = fun μ : Fin (5 + 1) =>\n    if μ = 0 then 1 / 2 else if μ = 5 then 1 / 2 else 0",
 "sum_univ_six'": "theorem sum_univ_six' (f : Fin (5 + 1) → ℝ) :\n    ∑ i, f i = f 0 + f 1 + f 2 + f 3 + f 4 + f 5",
 "gJ5_value": "theorem gJ5_value :\n    prodEffVal (sharpEff w5) (sharpEff z5) (gJ5 (prodState x5 z5)) = -1 / 10",
 "gJ5_not_mem_maxCone": "theorem gJ5_not_mem_maxCone : gJ5 (prodState x5 z5) ∉ maxCone (eball 5)",
 "not_posFwd_gJ5": "theorem not_posFwd_gJ5 :\n    ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gJ5 (prodState x y) ∈ maxCone (eball 5)",
 "not_nativeGate_gJ5": "theorem not_nativeGate_gJ5 : ¬ NativeGate (eball 5) z5 n5 gJ5"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.ParityNot.finrank_plus_eq_finrank_minus_rel",
 "OIBridge.ParityNot.not_even_of_gateRel",
 "OIBridge.ParityNot.finrank_plus_minus_three",
 "OIBridge.ParityNot.tangentPlus_three",
 "OIBridge.ParityNot.piRotation_three",
 "OIBridge.ParityNot.det_three",
 "OIBridge.ParityNot.piRotation_of_nativeGate_three",
 "OIBridge.ParityNot.det_of_nativeGate_three",
 "OIBridge.ParityNot.not_gateRel_refl3",
 "OIBridge.ParityNot.not_gateRel_negId3",
 "OIBridge.ParityNot.det_refl3",
 "OIBridge.ParityNot.det_negId3",
 "OIBridge.ParityNot.gateRel_cnot",
 "OIBridge.ParityNot.det_nflip_rel",
 "OIBridge.ParityNot.gJ3_frame",
 "OIBridge.ParityNot.gateRel_gJ3",
 "OIBridge.ParityNot.gJ3_value",
 "OIBridge.ParityNot.not_posFwd_gJ3",
 "OIBridge.ParityNot.isNot_n5",
 "OIBridge.ParityNot.gJ5_frame",
 "OIBridge.ParityNot.gateRel_gJ5",
 "OIBridge.ParityNot.finrank_plus_eq_finrank_minus_n5",
 "OIBridge.ParityNot.gJ5_value",
 "OIBridge.ParityNot.not_posFwd_gJ5"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.EffectSpace\n\nnamespace OIBridge\nnamespace ParityNot\n\nopen KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace Finset\n\nvariable {d : ℕ}\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace ParityNot",
 "open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace Finset",
 "variable {d : ℕ}",
 "end ParityNot",
 "end OIBridge"
]''')
LANDED = json.loads(r'''{
 "NativeGate#relT": "relT : ∀ ω, actT N (G (actT N ω)) = G ω",
 "NativeGate#relC": "relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
 "NativeGate#frame": "frame : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))",
 "NativeGate#posFwd": "posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω",
 "finrank_plus_eq_finrank_minus": "{d : ℕ} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)",
 "not_even_of_nativeGate": "{d : ℕ} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : ¬ Even d",
 "cnot_relT": "(ω : W 3) : actT nflip (cnot (actT nflip ω)) = cnot ω",
 "cnot_relC": "(ω : W 3) : actC nflip (cnot (actC nflip ω)) = actT nflip (cnot ω)"
}''')
N_PRINTS = 24

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

IDENT = re.compile(r'(?<![\w.\'@])[A-Za-z_][\w\'.]*')
BINDER_OPEN, BINDER_CLOSE = '({[⦃', ')}]⦄'


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def groups(b):
    """The top-level bracketed binder groups of a binder string, in order."""
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c in BINDER_OPEN:
            if depth == 0:
                start = i
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(norm(b[start:i + 1]))
                start = None
    return out


def group_names(g):
    """The bound names of a binder group (none for an anonymous instance group)."""
    inner = g[1:-1]
    j = inner.find(' : ')
    if j == -1:
        return []
    return inner[:j].split()


def scopes_at(text):
    """[(position, variable groups in scope, namespaces in scope, opened namespaces in scope)] at each declaration."""
    stack = [([], [], [])]
    out = {}
    lines = text.split('\n')
    pos = 0
    k = 0
    decl_at = {m.start(): m.group(2) for m in DECL.finditer(text)}
    while k < len(lines):
        line = lines[k]
        block = [line]
        j = k + 1
        if line.startswith('variable') or line.startswith('open '):
            while j < len(lines) and lines[j].startswith('  '):
                block.append(lines[j])
                j += 1
        whole = '\n'.join(block)
        m = re.match(r'^(namespace|section|noncomputable section)\b\s*(\S*)', line)
        if m:
            stack.append(([], [m.group(2)] if m.group(1) == 'namespace' else [], []))
        elif re.match(r'^end\b', line):
            if len(stack) > 1:
                stack.pop()
        elif line.startswith('variable'):
            stack[-1][0].extend(groups(whole[len('variable'):]))
        elif line.startswith('open '):
            stack[-1][2].extend(whole[len('open '):].split())
        if pos in decl_at:
            vs = [g for s in stack for g in s[0]]
            nss = [n for s in stack for n in s[1]]
            ops = [o for s in stack for o in s[2]]
            out[decl_at[pos]] = (vs, nss, ops)
        for l in block:
            pos += len(l) + 1
        k = j
    return out


def effective(text, name):
    """The effective statement of a declaration: the section variables its statement uses (closed under use by the
    included groups, an instance group included with a variable it mentions), in declared order, then its own binders
    and conclusion. None when the declaration is absent."""
    chunks = decl_chunks(text)
    if name not in chunks:
        return None
    stmt = chunks[name][1]
    vs = scopes_at(text).get(name, ([], [], []))[0]
    b, c = split_statement(stmt)
    used = norm(b) + ' : ' + norm(c)
    inc = [False] * len(vs)
    changed = True
    while changed:
        changed = False
        hay = used + ' ' + ' '.join(g for g, i in zip(vs, inc) if i)
        for n, g in enumerate(vs):
            if inc[n]:
                continue
            names = group_names(g)
            if names and any(token(x, hay) for x in names):
                inc[n] = True
                changed = True
            elif not names and g.startswith('[') and any(token(x, g) for gg, i in zip(vs, inc) if i
                                                          for x in group_names(gg)):
                inc[n] = True
                changed = True
    pre = ' '.join(g for g, i in zip(vs, inc) if i)
    return norm(pre + ' ' + norm(b) + ' : ' + norm(c))


_INV_CACHE = {}


def inventory(files):
    """{fully qualified name} of every declaration in the given module texts, with the namespaces they declare."""
    names, spaces = set(), set()
    for text in files:
        if text in _INV_CACHE:
            n, sp = _INV_CACHE[text]
            names |= n
            spaces |= sp
            continue
        n, sp = inventory_one(text)
        if len(_INV_CACHE) < 4096:
            _INV_CACHE[text] = (n, sp)
        names |= n
        spaces |= sp
    return names, spaces


def inventory_one(text):
    names, spaces = set(), set()
    for text in [text]:
        sc = scopes_at(text)
        for kind, name in decls(text):
            nss = sc.get(name, ([], [], []))[1]
            prefix = '.'.join(nss)
            names.add((prefix + '.' if prefix else '') + name)
            for i in range(1, len(nss) + 1):
                spaces.add('.'.join(nss[:i]))
    return names, spaces


def visible(nss, ops, spaces):
    """The namespaces whose members are in scope: every prefix of the current namespace, and each opened namespace,
    resolved against the current namespace prefixes when that names an OIBridge namespace."""
    out = [''] + ['.'.join(nss[:i]) for i in range(1, len(nss) + 1)]
    for o in ops:
        hit = [p + '.' + o for p in ['.'.join(nss[:i]) for i in range(len(nss), 0, -1)] if p + '.' + o in spaces]
        out.append(hit[0] if hit else o)
    return out


def resolve(tok, vis, names):
    return sorted({(v + '.' if v else '') + tok for v in vis} & names)


def top_colon(s):
    """Index of the first colon at bracket depth 0 that is not part of `:=`."""
    depth = 0
    for j, c in enumerate(s):
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and s[j:j + 2] != ':=':
            return j
    return len(s)


def strip_binders(eff):
    """The identifiers of an effective statement, without the names it binds: the names of its binder groups and the
    names bound by `∃`, `∀` and `fun` in its conclusion."""
    k = top_colon(eff)
    bound = set()
    for g in groups(eff[:k]):
        bound.update(group_names(g))
    for m in re.finditer(r'(?:∃|∀|fun)\s+([^,:=]+?)\s*(?::|,|=>)', eff[k:]):
        bound.update(x for x in m.group(1).split() if re.match(r"^[A-Za-zΩ_][\w']*$", x))
    return [t for t in IDENT.findall(eff) if t not in bound]

PREFIX = 'OIBridge.ParityNot.'
REL = 'GateRel'
REL_HEADER = '(N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop'
LANDED_GATE = ('CompositeDimension', 'NativeGate')
GATE_HYP = '(hG : NativeGate (eball d) z N G)'
REL_HYP = '(hR : GateRel N G)'
# S2 -- the parity pairs: theorem -> landed partner in CompositeDimension
PARITY_PAIRS = {
    'finrank_plus_eq_finrank_minus_rel': 'finrank_plus_eq_finrank_minus',
    'not_even_of_gateRel': 'not_even_of_nativeGate',
}
FREE_OF_GATE = ('NativeGate', 'posFwd', 'posInv', 'frame', 'maxCone', 'prodEffVal', 'IsEffectOn', 'prodState',
                'corner')
# S3 -- the NOT at d = 3
NOT_BINDERS = ('{z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G : W 3 ≃ₗ[ℝ] W 3} '
               '(hN : IsNot (eball 3) z N) (hR : GateRel N G)')
NOT_GATE_BINDERS = NOT_BINDERS.replace('(hR : GateRel N G)', '(hG : NativeGate (eball 3) z N G)')
PI_FORM = '∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x'
NOT_THEOREMS = {
    'finrank_plus_minus_three': 'Module.finrank ℝ (plusSpace N) = 2 ∧ Module.finrank ℝ (minusSpace N) = 2',
    'tangentPlus_three': 'tangentPlus N = 1',
    'piRotation_three': PI_FORM,
    'det_three': 'LinearMap.det N = 1',
}
NOT_COROLLARIES = {
    'tangentPlus_of_nativeGate_three': 'tangentPlus_three',
    'piRotation_of_nativeGate_three': 'piRotation_three',
    'det_of_nativeGate_three': 'det_three',
}
PI_DET = ('det_eq_one_of_piRotation', '{N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {u : Fin 3 → ℝ} '
          '(hu : ∑ j, u j ^ 2 = 1) (hN : ∀ x, N x = (2 * ∑ j, u j * x j) • u - x)', 'LinearMap.det N = 1')
# S4 -- the controls at d = 3
CONTROL_DEFS = {
    'diagSign': 'fun i => c i * x i',
    'refl3': 'diagSign ![1, 1, -1]',
    'negId3': 'diagSign ![-1, -1, -1]',
}
CONTROL_THEOREMS = {
    'negId3_eq': ('', 'negId3 = -LinearMap.id', ()),
    'isNot_refl3': ('', 'IsNot (eball 3) z3 refl3', ()),
    'isNot_negId3': ('', 'IsNot (eball 3) z3 negId3', ()),
    'not_gateRel_refl3': ('(G : W 3 ≃ₗ[ℝ] W 3)', '¬ GateRel refl3 G', ('finrank_plus_minus_three',)),
    'not_gateRel_negId3': ('(G : W 3 ≃ₗ[ℝ] W 3)', '¬ GateRel negId3 G', ('finrank_plus_minus_three',)),
    'det_refl3': ('', 'LinearMap.det refl3 = -1', ()),
    'det_negId3': ('', 'LinearMap.det negId3 = -1', ()),
    'gateRel_cnot': ('', 'GateRel nflip cnot', ('cnot_relT', 'cnot_relC')),
}
LANDED_CNOT = ('cnot_relT', 'cnot_relC')
# S5 -- the separation witnesses
GATE_DEFS = {
    'sgate': 'fun μ ν => if odd ν then ω (p μ) ν else ω μ ν',
    'odd3': None, 'perm3': None, 'odd5': None, 'perm5': None,
    'gJ3': 'sgateEquiv odd3 perm3 perm3_perm3',
    'gJ5': 'sgateEquiv odd5 perm5 perm5_perm5',
    'w3': '![0, -3 / 5, -4 / 5]',
    'w5': 'fun i => if i = 2 then -3 / 5 else if i = 4 then -4 / 5 else 0',
    'z5': 'fun i => if i = 4 then 1 else 0',
    'x5': 'fun i => if i = 0 then 1 else 0',
    'c5': 'if odd5 j.succ then -1 else 1',
    'n5': 'diagSign c5',
}
WITNESS = {
    3: dict(gate='gJ3', nott='nflip', axis='z3', first='xplus', w='w3', body='eball 3', isnot=None),
    5: dict(gate='gJ5', nott='n5', axis='z5', first='x5', w='w5', body='eball 5', isnot='isNot_n5'),
}
VALUE = '-1 / 10'
SELECTORS = re.compile(r'(?<![\w.\'])\w*_of_nativeGate\w*|(?<![\w.\'])three_of_\w+|(?<![\w.\'])dim_of_\w+')
# S6 -- scope
SCOPE_TOKENS = ('Complex', 'ℂ', 'cnot1', 'nativeGate_cnot1', 'dim_of_nativeGate', 'ne_five_of_nativeGate',
                'dim_of_nativeGateOf', 'three_of_nativeGateOf', 'three_of_nativeGateOf_of_two_le')
SCOPE_STMT_TOKENS = ('neg1', 'z1')
D_EQ = re.compile(r'(?<![\w.\'])d\s*(=|≠)\s*\d')
# S7 -- reuse
IMPORT_ONLY = 'import OIBridge.EffectSpace'
# S8 -- phrases
PHRASES = ('selects d = 3', 'selects `d = 3`', 'selector for d = 3', 'forces d = 3', 'forces `d = 3`',
           'd = 3 is forced', 'd = 3 is selected', 'selects the dimension', 'dimension selection',
           'the relations select', 'positivity selects', 'complex structure is', 'yields a complex structure',
           'gives a complex structure', 'reconstructs ℂ', 'reconstructs the complex', 'J² = −1', 'J^2 = -1',
           'J² = -1', 'only higher-dimensional', 'only obstruction', 'the only counterexample', 'every odd dimension',
           'all odd dimensions', 'physically carried', 'physical NOT', 'positivity follows from',
           'positivity is derived', 'implies positivity', 'OI supplies', 'OI provides', 'derived from OI',
           'sourced from OI', 'premise adopted', 'adopts a premise', 'qubit', 'design (round', 'not for landing')
# V -- the frozen decision rule
REL_TOKENS = ('PARITY-FROM-RELATIONS-PROVED', 'PARITY-FROM-RELATIONS-NOT-ESTABLISHED')
NOT_TOKENS = ('D3-NOT-PI-ROTATION-PROVED', 'D3-NOT-PI-ROTATION-NOT-ESTABLISHED')
SEP_TOKENS = ('POSITIVITY-SEPARATION-PROVED', 'POSITIVITY-SEPARATION-NOT-ESTABLISHED')
ALL_TOKENS = REL_TOKENS + NOT_TOKENS + SEP_TOKENS


def tsub(text, mapping):
    """Token-bounded simultaneous substitution."""
    pat = re.compile(r'(?<![\w.\'])(%s)(?![\w\'])' % '|'.join(re.escape(k) for k in mapping))
    return pat.sub(lambda m: mapping[m.group(1)], text)


def kinds_texts_proofs(mod):
    chunks = decl_chunks(mod)
    return ({n: k for n, (k, _, _) in chunks.items()}, {n: c for n, (_, c, _) in chunks.items()},
            {n: p for n, (_, _, p) in chunks.items()})


def rel_ok(mod, landed):
    """GateRel: a structure with the frozen header and exactly the fields relT and relC, each the landed field."""
    kinds, texts, _ = kinds_texts_proofs(mod)
    t = texts.get(REL, '')
    if kinds.get(REL) != 'structure' or fields(t) != ['relT', 'relC']:
        return False
    hd = norm(t.split(' where', 1)[0])
    if not hd.startswith('structure %s ' % REL) or hd[len('structure %s ' % REL):] != norm(REL_HEADER):
        return False
    return all(landed.get('%s#%s' % (LANDED_GATE[1], f)) == field_line(t, f) for f in ('relT', 'relC'))


def section_decls(mod, labels):
    secs = sections(mod)
    return [(name, mod[start:nxt]) for kind, name, start, se, nxt, cend in spans(mod)
            if section_at(secs, start) in labels]


def mentions(text, toks):
    c = code_only(text)
    return [t for t in toks if token(t, c)]


def parity_bad(mod, landed, names=None, spaces=None, inv_files=None):
    """S2: each parity theorem is its landed partner with the native-gate hypothesis replaced by GateRel; §A free of
    the native gate, the frame and positivity outside gateRel_of_nativeGate; resolution when an inventory is given."""
    bad = []
    for n, l in PARITY_PAIRS.items():
        de, le = effective(mod, n), landed.get(l)
        if de is None or le is None or le.count(GATE_HYP) != 1 or token('NativeGate', de) or \
                de != le.replace(GATE_HYP, REL_HYP):
            bad.append(n)
    for name, body in section_decls(mod, ('§A',)):
        if name != 'gateRel_of_nativeGate' and name != REL and mentions(body, FREE_OF_GATE):
            bad.append(name)
    if names is not None:
        lt = [t for t in inv_files if '\nnamespace %s\n' % LANDED_GATE[0] in t]
        lt = lt[0] if len(lt) == 1 else None
        for n, l in PARITY_PAIRS.items():
            de = effective(mod, n)
            if de is None or lt is None:
                bad.append(n)
                continue
            dsc = scopes_at(mod).get(n, ([], [], []))
            lsc = scopes_at(lt).get(l, ([], [], []))
            dvis, lvis = visible(dsc[1], dsc[2], spaces), visible(lsc[1], lsc[2], spaces)
            if resolve('NativeGate', lvis, names) != ['OIBridge.%s.NativeGate' % LANDED_GATE[0]]:
                bad.append(n + ':NativeGate')
            for t in sorted(set(strip_binders(de))):
                a, b = resolve(t, dvis, names), resolve(t, lvis, names)
                if t == REL:
                    if a != [PREFIX + REL]:
                        bad.append(n + ':' + t)
                elif len(a) > 1 or a != b:
                    bad.append(n + ':' + t)
    return bad


def not_bad(mod):
    """S3: the four d = 3 theorems on IsNot and GateRel alone; §B free of the native gate, the frame and positivity
    outside the three corollaries, each the GateRel theorem with the native-gate hypothesis, through
    gateRel_of_nativeGate."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, c in NOT_THEOREMS.items():
        b, cc = split_statement(texts.get(n, ''))
        if kinds.get(n) != 'theorem' or norm(b) != norm(NOT_BINDERS) or norm(cc) != norm(c):
            bad.append(n)
    b, cc = split_statement(texts.get(PI_DET[0], ''))
    if kinds.get(PI_DET[0]) != 'theorem' or norm(b) != norm(PI_DET[1]) or norm(cc) != norm(PI_DET[2]):
        bad.append(PI_DET[0])
    if not token('det_eq_one_of_piRotation', proofs.get('det_three', '')) or \
            not token('piRotation_three', proofs.get('det_three', '')):
        bad.append('det_three')
    for n, base in NOT_COROLLARIES.items():
        b, cc = split_statement(texts.get(n, ''))
        _, bc = split_statement(texts.get(base, ''))
        if kinds.get(n) != 'theorem' or norm(b) != norm(NOT_GATE_BINDERS) or norm(cc) != norm(bc) or \
                norm(bc) != norm(NOT_THEOREMS[base]) or not token('gateRel_of_nativeGate', proofs.get(n, '')) or \
                not token(base, proofs.get(n, '')):
            bad.append(n)
    for name, body in section_decls(mod, ('§B',)):
        if name not in NOT_COROLLARIES and mentions(body, FREE_OF_GATE):
            bad.append(name)
    return bad


def controls_bad(mod, landed):
    """S4: the two NOT controls without the relations, and cnot with nflip with them."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, body in CONTROL_DEFS.items():
        t = texts.get(n, '')
        got = norm(t.split('toFun x :=', 1)[1].split('\n')[0]) if n == 'diagSign' and 'toFun x :=' in t else \
            def_body(t)
        if kinds.get(n) != 'def' or got != norm(body):
            bad.append(n)
    for n, (b, c, deps) in CONTROL_THEOREMS.items():
        bb, cc = split_statement(texts.get(n, ''))
        if kinds.get(n) != 'theorem' or norm(bb) != norm(b) or norm(cc) != norm(c) or \
                not all(token(m, proofs.get(n, '')) for m in deps):
            bad.append(n)
    for n in LANDED_CNOT:
        if landed.get(n) is None:
            bad.append(n + ' at D')
    if landed.get('cnot_relT') != '(ω : W 3) : actT nflip (cnot (actT nflip ω)) = cnot ω' or \
            landed.get('cnot_relC') != '(ω : W 3) : actC nflip (cnot (actC nflip ω)) = actT nflip (cnot ω)':
        bad.append('cnot relations at D')
    return bad


def sep_bad(mod, landed):
    """S5: for d = 3 and d = 5, the frozen gate and witness; the landed frame field at the gate; GateRel; the value
    -1 / 10; the negation of the landed posFwd field at the gate, through the value; no dimension corollary."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, body in GATE_DEFS.items():
        if n not in texts:
            bad.append(n)
        elif body is not None and def_body(texts[n]) != norm(body):
            bad.append(n)
    frame = landed.get('%s#frame' % LANDED_GATE[1])
    posfwd = landed.get('%s#posFwd' % LANDED_GATE[1])
    if frame is None or posfwd is None or not frame.startswith('frame : ∀ a b : Fin 2, ') or \
            not posfwd.startswith('posFwd : '):
        return bad + ['NativeGate fields at D']
    frame = frame[len('frame : ∀ a b : Fin 2, '):]
    posfwd = posfwd[len('posFwd : '):]
    for k, w in WITNESS.items():
        g = w['gate']
        want_frame = tsub(frame, {'G': g, 'z': w['axis']})
        b, c = split_statement(texts.get(g + '_frame', ''))
        if kinds.get(g + '_frame') != 'theorem' or norm(b) != '(a b : Fin 2)' or norm(c) != want_frame:
            bad.append(g + '_frame')
        b, c = split_statement(texts.get('gateRel_' + g, ''))
        if kinds.get('gateRel_' + g) != 'theorem' or norm(b) != '' or norm(c) != 'GateRel %s %s' % (w['nott'], g):
            bad.append('gateRel_' + g)
        val = g + '_value'
        b, c = split_statement(texts.get(val, ''))
        want_val = 'prodEffVal (sharpEff %s) (sharpEff %s) (%s (prodState %s %s)) = %s' % (
            w['w'], w['axis'], g, w['first'], w['axis'], VALUE)
        if kinds.get(val) != 'theorem' or norm(b) != '' or norm(c) != want_val:
            bad.append(val)
        mem = g + '_not_mem_maxCone'
        b, c = split_statement(texts.get(mem, ''))
        if kinds.get(mem) != 'theorem' or norm(c) != '%s (prodState %s %s) ∉ maxCone (%s)' % (
                g, w['first'], w['axis'], w['body']) or not token(val, proofs.get(mem, '')) or \
                not token('sharpEff_isEffectOn', proofs.get(mem, '')):
            bad.append(mem)
        pf = 'not_posFwd_' + g
        want_pf = '¬ ' + tsub(posfwd, {'G': g, 'Ω': '(%s)' % w['body']}).replace('∈ (%s),' % w['body'],
                                                                            '∈ %s,' % w['body'])
        b, c = split_statement(texts.get(pf, ''))
        if kinds.get(pf) != 'theorem' or norm(b) != '' or norm(c) != want_pf or not token(mem, proofs.get(pf, '')):
            bad.append(pf)
        ng = 'not_nativeGate_' + g
        b, c = split_statement(texts.get(ng, ''))
        if kinds.get(ng) != 'theorem' or norm(c) != '¬ NativeGate (%s) %s %s %s' % (
                w['body'], w['axis'], w['nott'], g) or not token(pf, proofs.get(ng, '')):
            bad.append(ng)
        if w['isnot']:
            b, c = split_statement(texts.get(w['isnot'], ''))
            if kinds.get(w['isnot']) != 'theorem' or norm(c) != 'IsNot (%s) %s %s' % (w['body'], w['axis'],
                                                                                        w['nott']):
                bad.append(w['isnot'])
    b, c = split_statement(texts.get('finrank_plus_eq_finrank_minus_n5', ''))
    if norm(c) != 'Module.finrank ℝ (plusSpace n5) = Module.finrank ℝ (minusSpace n5)' or \
            not token('finrank_plus_eq_finrank_minus_rel', proofs.get('finrank_plus_eq_finrank_minus_n5', '')):
        bad.append('finrank_plus_eq_finrank_minus_n5')
    for name, body in section_decls(mod, ('§D', '§E', '§F')):
        if SELECTORS.search(code_only(body)):
            bad.append(name)
    return bad


def rel_cell(mod, landed):
    """PARITY-FROM-RELATIONS-PROVED iff: GateRel is the landed relT and relC and nothing else (S1); each of the two
    parity theorems is its landed NativeGate partner read from D with the native-gate hypothesis replaced by
    GateRel and nothing else, and §A reads neither the native gate, the frame nor positivity (S2). Otherwise
    PARITY-FROM-RELATIONS-NOT-ESTABLISHED. Reads no §B-§F statement."""
    ok = rel_ok(mod, landed) and not parity_bad(mod, landed)
    return [REL_TOKENS[0] if ok else REL_TOKENS[1]]


def not_cell(mod, landed):
    """D3-NOT-PI-ROTATION-PROVED iff: GateRel passes S1; the four d = 3 theorems take IsNot (eball 3) and GateRel alone
    with their frozen conclusions, and §B reads neither the native gate, the frame nor positivity outside the three
    corollaries (S3); and the controls hold (S4). Otherwise D3-NOT-PI-ROTATION-NOT-ESTABLISHED. Reads no §D-§F
    statement."""
    ok = rel_ok(mod, landed) and not not_bad(mod) and not controls_bad(mod, landed)
    return [NOT_TOKENS[0] if ok else NOT_TOKENS[1]]


def sep_cell(mod, landed):
    """POSITIVITY-SEPARATION-PROVED iff: GateRel passes S1, and for each of d = 3 and d = 5 the frozen gate satisfies
    the landed frame field and GateRel, and the negation of the landed posFwd field is proved through the frozen
    value -1 / 10 (S5). Otherwise POSITIVITY-SEPARATION-NOT-ESTABLISHED. Reads no §A-§C statement."""
    ok = rel_ok(mod, landed) and not sep_bad(mod, landed)
    return [SEP_TOKENS[0] if ok else SEP_TOKENS[1]]


def verdicts(mod, landed):
    return rel_cell(mod, landed), not_cell(mod, landed), sep_cell(mod, landed)


def semantic_checks(mod, chunks, prints, tag, landed, inv_files):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    check('S1', 'GateRel is the landed relT and relC and nothing else' + tag, rel_ok(mod, landed))
    names, spaces = inventory(inv_files + [mod])
    bad2 = parity_bad(mod, landed, names, spaces, inv_files)
    check('S2', 'each parity theorem is its landed partner with NativeGate replaced by GateRel; §A free of the gate '
                'conditions%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    bad3 = not_bad(mod)
    check('S3', 'the d = 3 theorems on IsNot and GateRel alone; §B free of the gate conditions%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    bad4 = controls_bad(mod, landed)
    check('S4', 'the reflection and -id carry no relations; cnot with nflip does%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    bad5 = sep_bad(mod, landed)
    check('S5', 'gJ3 and gJ5: landed frame, GateRel, value -1 / 10, landed posFwd negated%s%s'
          % (tag, (' %s' % bad5[:3]) if bad5 else ''), not bad5)
    bad6 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        body = mod[start:nxt]
        if mentions(body, SCOPE_TOKENS) or mentions(texts.get(name, ''), SCOPE_STMT_TOKENS):
            bad6.append(name)
        if kind in ('theorem', 'lemma'):
            _, c = split_statement(texts.get(name, ''))
            if D_EQ.search(c):
                bad6.append(name)
    check('S6', 'no complex field, d = 1 object or dimension selector; no conclusion on d%s%s'
          % (tag, (' %s' % bad6[:3]) if bad6 else ''), not bad6)
    others = inventory(inv_files)[0]
    msc = scopes_at(mod)
    clash = []
    for kind, name in decls(mod):
        sc = msc.get(name, ([], [], []))
        if resolve(name, visible(sc[1], sc[2], spaces), others):
            clash.append(name)
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S7', 'no declaration shares a name with a visible OIBridge declaration; the only import is '
                'OIBridge.EffectSpace%s%s' % (tag, (' %s' % clash[:3]) if clash else ''),
          not clash and imports == [IMPORT_ONLY])
    ph = phrase_hits(header(mod))
    check('S8', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    local = {n for _, n in decls(mod)}
    pnames = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(pnames) == N_PRINTS
          and all(n in local for n in pnames))
    a, b, c = verdicts(mod, landed)
    check('V', 'one outcome per cell by the frozen rules: %s, %s, %s%s' % (a, b, c, tag),
          len(a) == 1 and len(b) == 1 and len(c) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in ALL_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


_INV = []


def d_inventory_files():
    """Every OIBridge module at D (read once)."""
    if not _INV:
        r = git('ls-tree', '--name-only', D, LEAN)
        _INV.extend(show(D, p) for p in r.stdout.split() if p.endswith('.lean'))
    return list(_INV)


def module_checks(mod, tag='', landed=None, inv_files=None):
    if landed is None:
        landed = LANDED
    if inv_files is None:
        inv_files = d_inventory_files()
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
    semantic_checks(mod, chunks, prints, tag, landed, inv_files)


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


def landed_texts(show_d):
    """The landed texts the rules read, from D: the NativeGate fields, the two parity theorems and the two cnot
    relations, as effective statements."""
    out = {}
    t = show_d(LEAN + LANDED_GATE[0] + '.lean')
    if not t:
        return out
    ch = decl_chunks(t).get(LANDED_GATE[1])
    if ch and ch[0] == 'structure':
        for f in ('relT', 'relC', 'frame', 'posFwd'):
            v = field_line(ch[1], f)
            if v is not None:
                out['%s#%s' % (LANDED_GATE[1], f)] = v
    for n in list(PARITY_PAIRS.values()) + list(LANDED_CNOT):
        e = effective(t, n)
        if e is not None:
            out[n] = e
    return out


def landed_at_d():
    return landed_texts(lambda p: show(D, p))


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    landed = landed_at_d()
    check('S1', 'the landed texts read from D are the frozen ones', landed == LANDED)
    mod = show(commit, MOD)
    module_checks(mod, landed=landed)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S8', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (a + b + c, toks), len(a) == 1 and len(b) == 1 and len(c) == 1 and sorted(toks) == sorted(a + b + c))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the KTRANS-DENSE-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    landed = landed_at_d()
    a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
    print('VERDICT  REL  %s' % ('/'.join(a) or 'none'))
    print('VERDICT  NOT  %s' % ('/'.join(b) or 'none'))
    print('VERDICT  SEP  %s' % ('/'.join(c) or 'none'))
    check('V', 'the landed texts read from D are the frozen ones', landed == LANDED)
    check('V', 'exactly one outcome per cell', len(a) == 1 and len(b) == 1 and len(c) == 1)

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


def insert_in_section(text, marker, decl):
    """Insert a declaration just before the section marker `marker`."""
    i = text.index(marker)
    return text[:i] + decl + '\n\n' + text[i:]


def append_end(text, decl):
    """Insert a declaration at the end of §F, before `end ParityNot`."""
    return replace_once(text, '\nend ParityNot\n', '\n' + decl + '\n\nend ParityNot\n')


def verdict_of(mod2, landed=None):
    return verdicts(mod2, LANDED if landed is None else landed)

REL_RELC = '  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)\n'
PAR_HEAD = ('    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) :\n'
            '    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by')
EVEN_HEAD = '    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d :='
PI_HEAD = ('    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) :\n'
           '    ∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x := by')
DET_HEAD = ('    (hN : IsNot (eball 3) z N) (hR : GateRel N G) : LinearMap.det N = 1 := by\n'
            '  obtain ⟨u, hu, hform⟩ := piRotation_three hN hR')
COR_PROOF = '  det_three hN (gateRel_of_nativeGate hG)\n'
REFL_DEF = 'def refl3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![1, 1, -1]'
CNOT_PROOF = 'theorem gateRel_cnot : GateRel nflip cnot := ⟨cnot_relT, cnot_relC⟩'
W5_DEF = 'noncomputable def w5 : Fin 5 → ℝ := fun i => if i = 2 then -3 / 5 else if i = 4 then -4 / 5 else 0'
V5_HEAD = ('theorem gJ5_value :\n'
           '    prodEffVal (sharpEff w5) (sharpEff z5) (gJ5 (prodState x5 z5)) = -1 / 10 := by')
V3_HEAD = ('theorem gJ3_value :\n'
           '    prodEffVal (sharpEff w3) (sharpEff z3) (gJ3 (prodState xplus z3)) = -1 / 10 := by')
PF5 = ('theorem not_posFwd_gJ5 :\n'
       '    ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gJ5 (prodState x y) ∈ maxCone (eball 5) :=\n'
       '  fun h => gJ5_not_mem_maxCone (h _ x5_mem _ z5_mem)')
FR5 = ('theorem gJ5_frame (a b : Fin 2) :\n'
       '    gJ5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)) := by')
G5_DEF = 'def gJ5 : W 5 ≃ₗ[ℝ] W 5 := sgateEquiv odd5 perm5 perm5_perm5'
NG5 = 'theorem not_nativeGate_gJ5 : ¬ NativeGate (eball 5) z5 n5 gJ5 :=\n  fun hG => not_posFwd_gJ5 hG.posFwd'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    landed = landed_at_d()
    check('T', 'the landed texts read from D are the frozen ones', landed == LANDED and len(LANDED) == 8)
    module_checks(mod, ' [reference]')
    a, b, c = verdict_of(mod)
    check('T', 'the reference module reads %s, %s and %s' % (a, b, c),
          a == [REL_TOKENS[0]] and b == [NOT_TOKENS[0]] and c == [SEP_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem w3_unit :', '\ntheorem w3_unit\' :'))
    must_fail('N2', 'a changed binder context', replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {k : ℕ}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, 'NativeGateBall CompositeDimension EffectSpace Finset',
                                                       'NativeGateBall CompositeDimension Finset'))
    must_fail('N3', 'a sorry', append_end(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.ParityNot.det_three\n', ''))
    # S1 -- the relations
    must_fail('S1', 'the frame added to GateRel',
              replace_once(mod, REL_RELC, REL_RELC + '  frame : ∀ ω, G ω = G ω\n'))
    must_fail('S1', 'the control relation changed',
              replace_once(mod, REL_RELC, '  relC : ∀ ω, actC N (G (actC N ω)) = G ω\n'))
    lm = dict(LANDED)
    lm['NativeGate#relC'] = lm['NativeGate#relC'].replace('actT N (G ω)', 'G ω')
    check('M', 'relations: a landed relC that differs fails S1 and all three cells',
          not rel_ok(mod, lm) and verdict_of(mod, lm) == ([REL_TOKENS[1]], [NOT_TOKENS[1]], [SEP_TOKENS[1]]))
    # S2 -- the parity pairing
    must_fail('S2', 'the parity theorem with the native gate kept',
              replace_once(mod, PAR_HEAD, PAR_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball d) z N G)')))
    must_fail('S2', 'the parity theorem with positivity added',
              replace_once(mod, PAR_HEAD, PAR_HEAD.replace(
                  '(hR : GateRel N G)', '(hR : GateRel N G)\n    (hP : ∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d))')))
    must_fail('S2', 'the parity conclusion weakened to an inequality',
              replace_once(mod, PAR_HEAD, PAR_HEAD.replace('Module.finrank ℝ (plusSpace N) = Module', 'Module.finrank ℝ (plusSpace N) ≤ Module')))
    must_fail('S2', 'the oddness theorem with the frame added',
              replace_once(mod, EVEN_HEAD, EVEN_HEAD.replace(
                  '(hR : GateRel N G)', '(hR : GateRel N G)\n    (hF : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)))')))
    must_fail('S2', 'a §A proof reading positivity',
              replace_once(mod, '  apply LinearMap.ext; intro u\n  rw [LinearMap.neg_apply, Lop_apply, Pop_apply, Lop_apply]',
                           '  have _hp : maxCone (eball d) = maxCone (eball d) := rfl\n'
                           '  apply LinearMap.ext; intro u\n  rw [LinearMap.neg_apply, Lop_apply, Pop_apply, Lop_apply]'))
    must_fail('S2', 'a local declaration shadowing a landed object of a paired statement (eball)',
              insert_in_section(mod, '/-! ### §A', 'def eball (d : ℕ) : Set (Fin d → ℝ) := Set.univ'))
    lm = dict(LANDED)
    lm['finrank_plus_eq_finrank_minus'] = lm['finrank_plus_eq_finrank_minus'].replace('= Module.finrank', '≤ Module.finrank')
    check('M', 'pairing: a landed parity statement that differs fails the pair and only the relation cell',
          verdict_of(mod, lm) == ([REL_TOKENS[1]], [NOT_TOKENS[0]], [SEP_TOKENS[0]]))
    # S3 -- the NOT at d = 3
    must_fail('S3', 'the π-rotation with the native gate in place of GateRel',
              replace_once(mod, PI_HEAD, PI_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball 3) z N G)')))
    must_fail('S3', 'the π-rotation with the frame added',
              replace_once(mod, PI_HEAD, PI_HEAD.replace(
                  '(hR : GateRel N G)', '(hR : GateRel N G)\n    (hF : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)))')))
    must_fail('S3', 'the π-rotation conclusion weakened (unit axis dropped)',
              replace_once(mod, PI_HEAD, PI_HEAD.replace('∑ j, u j ^ 2 = 1 ∧ ', '')))
    must_fail('S3', 'the determinant conclusion changed to ±1',
              replace_once(mod, DET_HEAD, DET_HEAD.replace('LinearMap.det N = 1 :=', 'LinearMap.det N = 1 ∨ LinearMap.det N = -1 :=')))
    must_fail('S3', 'a §B proof reading positivity',
              replace_once(mod, '  have ht : Module.finrank ℝ (tangentSpace N) = 1 := by',
                           '  have _hp : maxCone (eball 3) = maxCone (eball 3) := rfl\n'
                           '  have ht : Module.finrank ℝ (tangentSpace N) = 1 := by'))
    must_fail('S3', 'a corollary proved without gateRel_of_nativeGate',
              replace_once(mod, COR_PROOF, '  det_three hN ⟨hG.relT, hG.relC⟩\n'))
    m = replace_once(mod, PI_HEAD, PI_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball 3) z N G)'))
    check('M', 'decision rule: a broken π-rotation reads D3-NOT-PI-ROTATION-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([REL_TOKENS[0]], [NOT_TOKENS[1]], [SEP_TOKENS[0]]))
    # S4 -- the controls
    must_fail('S4', 'the reflection control replaced by a rotation',
              replace_once(mod, REFL_DEF, REFL_DEF.replace('![1, 1, -1]', '![-1, -1, 1]')))
    must_fail('S4', 'the positive control proved without the landed cnot relations',
              replace_once(mod, CNOT_PROOF, 'theorem gateRel_cnot : GateRel nflip cnot := gateRel_of_nativeGate nativeGate_cnot'))
    lm = dict(LANDED)
    lm['cnot_relC'] = lm['cnot_relC'].replace('actT nflip (cnot ω)', 'cnot ω')
    check('M', 'controls: a different landed cnot relation fails only the NOT cell',
          verdict_of(mod, lm) == ([REL_TOKENS[0]], [NOT_TOKENS[1]], [SEP_TOKENS[0]]))
    # S5 -- the separation witnesses, both dimensions, the d = 5 witness load-bearing
    must_fail('S5', 'the d = 5 witness replaced by the landed dimension exclusion',
              replace_once(mod, NG5, 'theorem not_nativeGate_gJ5 : ¬ NativeGate (eball 5) z5 n5 gJ5 :=\n'
                                     '  fun hG => ne_five_of_nativeGate isNot_n5 hG rfl'))
    must_fail('S5', 'the d = 5 value changed', replace_once(mod, V5_HEAD, V5_HEAD.replace('= -1 / 10', '< 0')))
    must_fail('S5', 'the d = 3 value changed', replace_once(mod, V3_HEAD, V3_HEAD.replace('= -1 / 10', '= -1 / 5')))
    must_fail('S5', 'the d = 5 witness direction changed',
              replace_once(mod, W5_DEF, W5_DEF.replace('-4 / 5', '4 / 5')))
    must_fail('S5', 'the d = 5 positivity failure weakened to one input',
              replace_once(mod, PF5, PF5.replace('¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gJ5 (prodState x y) ∈ maxCone (eball 5)',
                                                  '¬ gJ5 (prodState x5 z5) ∈ maxCone (eball 5)')
                           .replace('fun h => gJ5_not_mem_maxCone (h _ x5_mem _ z5_mem)', 'gJ5_not_mem_maxCone')))
    must_fail('S5', 'the d = 5 frame changed', replace_once(mod, FR5, FR5.replace('(corner z5 (a + b))', '(corner z5 b)')))
    must_fail('S5', 'the d = 5 gate changed', replace_once(mod, G5_DEF, G5_DEF.replace('sgateEquiv odd5 perm5', 'sgateEquiv odd5 (perm5 ∘ perm5)')))
    lm = dict(LANDED)
    lm['NativeGate#posFwd'] = lm['NativeGate#posFwd'].replace('maxCone Ω', 'jointStates Ω')
    check('M', 'separation: a landed posFwd that differs fails only the separation cell',
          verdict_of(mod, lm) == ([REL_TOKENS[0]], [NOT_TOKENS[0]], [SEP_TOKENS[1]]))
    m = replace_once(mod, V5_HEAD, V5_HEAD.replace('= -1 / 10', '< 0'))
    check('M', 'decision rule: a broken d = 5 witness reads POSITIVITY-SEPARATION-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([REL_TOKENS[0]], [NOT_TOKENS[0]], [SEP_TOKENS[1]]))
    m = replace_once(mod, REL_RELC, REL_RELC + '  frame : ∀ ω, G ω = G ω\n')
    check('M', 'decision rule: GateRel broken reads NOT-ESTABLISHED in all three cells',
          verdict_of(m) == ([REL_TOKENS[1]], [NOT_TOKENS[1]], [SEP_TOKENS[1]]))
    # S6 -- scope
    must_fail('S6', 'a dimension conclusion', append_end(mod, 'theorem d_sel {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} '
                                                           '{G : W d ≃ₗ[ℝ] W d} (h : GateRel N G) : d ≠ 2 := sorry'))
    must_fail('S6', 'a complex field', append_end(mod, 'theorem cplx : (Complex.I : ℂ) = Complex.I := rfl'))
    must_fail('S6', 'the landed d = 1 gate', append_end(mod, 'theorem c1 : GateRel neg1 cnot1 := sorry'))
    # S7 -- reuse
    must_fail('S7', 'a landed definition re-declared', append_end(mod, 'def nflip : ℕ := 0'))
    must_fail('S7', 'a second import',
              replace_once(mod, 'import OIBridge.EffectSpace\n', 'import OIBridge.EffectSpace\nimport OIBridge.K2Guard\n'))
    # S8 -- phrases
    must_fail('S8', 'a forbidden phrase in the header',
              replace_once(mod, '  (A) Parity.', '  The relations select d = 3. (A) Parity.'))
    must_fail('S8', 'the design header', replace_once(mod, 'round PARITY-NOT-1:', 'design (round PARITY-NOT-1, not for landing):'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('The two relations give parity; gJ5 satisfies the frame and the relations and fails forward '
                          'positivity at an explicit product state.')
          and phrase_hits('Hence J² = −1\nholds.') == ['J² = −1'])
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.ParityNot.not_posFwd_gJ5\n',
                           '#print axioms OIBridge.ParityNot.not_posFwd_gJ5\n'
                           '#print axioms OIBridge.ParityNot.w5_unit\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.ParityNot.det_three\n',
                           '#print axioms OIBridge.ParityNot.det_three\n#print axioms OIBridge.ParityNot.det_three\n'))
    # V
    m = replace_once(mod, PAR_HEAD, PAR_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball d) z N G)'))
    check('M', 'decision rule: a broken parity pair reads PARITY-FROM-RELATIONS-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([REL_TOKENS[1]], [NOT_TOKENS[0]], [SEP_TOKENS[0]]))
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('PARITY-FROM-RELATIONS-PROVED, D3-NOT-PI-ROTATION-PROVED and POSITIVITY-SEPARATION-PROVED.')
          == ['PARITY-FROM-RELATIONS-PROVED', 'D3-NOT-PI-ROTATION-PROVED', 'POSITIVITY-SEPARATION-PROVED']
          and note_tokens('POSITIVITY-SEPARATION-NOT-ESTABLISHED') == ['POSITIVITY-SEPARATION-NOT-ESTABLISHED'])
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
