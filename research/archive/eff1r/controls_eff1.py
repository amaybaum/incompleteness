#!/usr/bin/env python3
"""controls.py -- round EFF-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the two verdicts computed from the module's statements at <commit>

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  cone        the two inclusions of Q-CONE are theorems with their frozen statements; the equality is proved from
                  both by name; `cone_of_orbit` and `sharpFamily_subset_avail` carry exactly OG-1's four hypotheses
                  (and `0 < d` for the former), with no unit, mixing or effect premise
  S2  set         the upper bound in both directions, the decomposition in both directions with the equality proved
                  from both by name, `fullEffects_subset_avail` with exactly OG-1's four hypotheses, the unit and
                  `MixingClosed`, and the countermodel `not_fullEffects_of_orbit` with its frozen conclusion
  S3  definitions `maxConeOf`, `MixingClosed`, `EffectsOn`, `unitSpan`, `sharpFamily` are the frozen texts whole;
                  `maxConeOf` quantifies over the family it is given and nothing else
  S4  premises    no theorem concludes `SharpSeed`, `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`,
                  `MixingClosed` or `EffectsOn` of a hypothesis-bound family, map or seed; those predicates are concluded
                  only of the named witnesses (`fullAut d`, `sharpEff`, `sharpUnitFamily d`) by the named control
                  theorems and the verdict; `MixingClosed` is never concluded positively
  S5  reuse       no declaration shares a name with a landed object it reads; every import is
                  `OIBridge.CompositeDimension`, `OIBridge.CompositeInterface` or a Mathlib module
  S6  neutral     no complex, matrix-trace, qubit, Bloch, Pauli, density, drive, flow or limit-closure token
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  dimension   `0 < d` occurs in exactly the frozen set of statements; outside the control section and the verdict no
                  numeral 3 occurs
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each question's verdict is computed from the module's statements by the frozen rule, and exactly one
                  outcome holds per question; at a commit carrying the result note, the note states exactly the
                  computed verdicts and no other outcome token
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.CompositeDimension`
  C   census      the census is D's with exactly the frozen family inserted after the DIM-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = 'e9882f968522c178b6ed55f954535ce77305d2e6'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-eff-1-effect-space/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/EffectSpace.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '5fad51a773310ac053e4c1952e72a9c941daa8c2'
ANCHOR_IMPORT = 'import OIBridge.CompositeDimension\n'
NEW_IMPORT = 'import OIBridge.EffectSpace\n'
PREV_FAMILY_MODULES = ['CompositeDimension']
CENSUS_FAMILY = json.loads(r'''{
 "name": "the effect set and the product-test cone of the coordinate ball eball d for every d >= 1: the sharp directional effects determine the maximal product cone of round DIM-1, OG-1's named hypotheses make them available without a mixing closure, and the full effect set follows only with the unit and the named mixing closure (round EFF-1, reconstruction)",
 "modules": [
  "EffectSpace"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round EFF-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-eff-1-effect-space/preregistration.md. Two separate questions. Q-CONE: for every d >= 1 the cone of joint vectors nonnegative on every product of two sharp directional effects sharpEff b, b a unit vector, is DIM-1's maximal cone maxCone (eball d), one theorem per inclusion (maxCone_subset_maxConeOf_sharp, maxConeOf_sharp_subset_maxCone); under OG-1's four named hypotheses on eball d (PreservesBody, SharpSeed, BoundaryTransitive, SeedOrbitAvailable; in the ROADMAP's labels body preservation, K∞-Seed, K∞-Trans and K∞-V4) every sharp effect is available (sharpFamily_subset_avail, cone_of_orbit), with no mixing closure and no unit premise. Q-SET: every effect on eball d is r -> a + v . r with sqrt(v . v) <= min a (1 - a), and conversely (effect_eq_affine, isEffectOn_of_affine); every effect is a sub-convex combination of the unit with one sharp effect (fullEffects_eq_unitSpan); the four hypotheses with the unit available and the named mixing closure MixingClosed make every effect available (fullEffects_subset_avail), and without the mixing closure they do not (not_fullEffects_of_orbit). Controls: d = 0 (maxConeOf_sharpFamily_zero_ne), one axis at d = 3 (maxConeOf_axis_ne), a countable family (not_boundaryTransitive_of_countable); the verdict is eff1_core. Carried by no manuscript. The cone statement concerns which test functionals determine the dual product cone and does not assert that every affine effect is available; nothing here sources body preservation, K∞-Seed, K∞-Trans, K∞-V4, the unit or the mixing closure, and nothing here concerns K∞-Stage or K∞-Act."
}''')
DECLS = json.loads(r'''[
 [
  "noncomputable def",
  "sharpVec"
 ],
 [
  "theorem",
  "sharpVec_zero"
 ],
 [
  "theorem",
  "sharpVec_succ"
 ],
 [
  "noncomputable def",
  "sharpEff"
 ],
 [
  "theorem",
  "sharpEff_apply"
 ],
 [
  "def",
  "sharpFamily"
 ],
 [
  "theorem",
  "sum_neg_sq"
 ],
 [
  "theorem",
  "mem_eball_of_sphere"
 ],
 [
  "theorem",
  "neg_mem_eball"
 ],
 [
  "theorem",
  "zero_mem_eball"
 ],
 [
  "theorem",
  "lor_sharpVec"
 ],
 [
  "theorem",
  "sharpEff_isEffectOn"
 ],
 [
  "theorem",
  "sharpEff_self"
 ],
 [
  "theorem",
  "sharpEff_neg_self"
 ],
 [
  "theorem",
  "sharpEff_sharpSeed"
 ],
 [
  "theorem",
  "isBoundaryState_eball_of_sphere"
 ],
 [
  "theorem",
  "sphere_of_isBoundaryState_eball"
 ],
 [
  "theorem",
  "ehom_apply"
 ],
 [
  "theorem",
  "sharp_eq_of_certain"
 ],
 [
  "def",
  "fullAut"
 ],
 [
  "theorem",
  "preservesBody_fullAut"
 ],
 [
  "noncomputable def",
  "reflLin"
 ],
 [
  "theorem",
  "reflLin_apply"
 ],
 [
  "theorem",
  "reflLin_dot"
 ],
 [
  "theorem",
  "reflLin_reflLin"
 ],
 [
  "theorem",
  "reflLin_sq"
 ],
 [
  "noncomputable def",
  "reflAff"
 ],
 [
  "theorem",
  "reflAff_apply"
 ],
 [
  "theorem",
  "reflAff_symm_apply"
 ],
 [
  "theorem",
  "reflAff_mem_fullAut"
 ],
 [
  "theorem",
  "refl_mem_fullAut"
 ],
 [
  "theorem",
  "reflLin_swap"
 ],
 [
  "theorem",
  "boundaryTransitive_fullAut"
 ],
 [
  "theorem",
  "seedTransport_mem_sharpFamily"
 ],
 [
  "theorem",
  "sharpFamily_subset_avail"
 ],
 [
  "theorem",
  "seedOrbit_subset_sharpFamily"
 ],
 [
  "theorem",
  "sharpFamily_subset_seedOrbit"
 ],
 [
  "theorem",
  "seedOrbit_eq_sharpFamily"
 ],
 [
  "def",
  "maxConeOf"
 ],
 [
  "theorem",
  "maxConeOf_fullEffects"
 ],
 [
  "theorem",
  "maxConeOf_anti"
 ],
 [
  "noncomputable def",
  "axisVec"
 ],
 [
  "theorem",
  "axisVec_sq"
 ],
 [
  "theorem",
  "hom_zero_eq_sharp"
 ],
 [
  "theorem",
  "lor_decomp"
 ],
 [
  "theorem",
  "nonneg_of_sharp"
 ],
 [
  "def",
  "pvRight"
 ],
 [
  "theorem",
  "pvRight_apply"
 ],
 [
  "theorem",
  "prodEffVal_sharp"
 ],
 [
  "theorem",
  "maxCone_subset_maxConeOf_sharp"
 ],
 [
  "theorem",
  "maxConeOf_sharp_subset_maxCone"
 ],
 [
  "theorem",
  "maxConeOf_sharpFamily"
 ],
 [
  "theorem",
  "cone_of_orbit"
 ],
 [
  "def",
  "EffectsOn"
 ],
 [
  "theorem",
  "maxConeOf_avail_eq"
 ],
 [
  "def",
  "unitSpan"
 ],
 [
  "def",
  "MixingClosed"
 ],
 [
  "theorem",
  "mix_apply"
 ],
 [
  "theorem",
  "effect_eq_affine"
 ],
 [
  "theorem",
  "isEffectOn_of_affine"
 ],
 [
  "theorem",
  "fullEffects_subset_unitSpan"
 ],
 [
  "theorem",
  "unitSpan_subset_fullEffects"
 ],
 [
  "theorem",
  "fullEffects_eq_unitSpan"
 ],
 [
  "theorem",
  "fullEffects_subset_avail"
 ],
 [
  "theorem",
  "avail_eq_fullEffects"
 ],
 [
  "def",
  "sharpUnitFamily"
 ],
 [
  "noncomputable def",
  "halfEff"
 ],
 [
  "theorem",
  "halfEff_apply"
 ],
 [
  "theorem",
  "halfEff_mem_fullEffects"
 ],
 [
  "theorem",
  "halfEff_not_mem_sharpUnitFamily"
 ],
 [
  "theorem",
  "not_fullEffects_of_orbit"
 ],
 [
  "theorem",
  "maxConeOf_sharpFamily_zero_ne"
 ],
 [
  "def",
  "axisFamily"
 ],
 [
  "noncomputable def",
  "outVec"
 ],
 [
  "theorem",
  "ehom_unitEff"
 ],
 [
  "theorem",
  "maxConeOf_axis_ne"
 ],
 [
  "theorem",
  "not_boundaryTransitive_of_countable"
 ],
 [
  "theorem",
  "eff1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "sharpVec": "noncomputable def sharpVec (b : Fin d → ℝ) : HVec d := Matrix.vecCons (1 / 2) fun j => b j / 2",
 "sharpVec_zero": "theorem sharpVec_zero (b : Fin d → ℝ) : sharpVec b 0 = 1 / 2",
 "sharpVec_succ": "theorem sharpVec_succ (b : Fin d → ℝ) (j : Fin d) : sharpVec b j.succ = b j / 2",
 "sharpEff": "noncomputable def sharpEff (b : Fin d → ℝ) : (Fin d → ℝ) →ᵃ[ℝ] ℝ := affOf (sharpVec b)",
 "sharpEff_apply": "theorem sharpEff_apply (b x : Fin d → ℝ) : sharpEff b x = 1 / 2 + ∑ j, b j / 2 * x j",
 "sharpFamily": "def sharpFamily (d : ℕ) : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ) :=\n  {e | ∃ b : Fin d → ℝ, ∑ j, b j ^ 2 = 1 ∧ e = sharpEff b}",
 "sum_neg_sq": "theorem sum_neg_sq (b : Fin d → ℝ) : ∑ j, (-b) j ^ 2 = ∑ j, b j ^ 2",
 "mem_eball_of_sphere": "theorem mem_eball_of_sphere {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : b ∈ eball d",
 "neg_mem_eball": "theorem neg_mem_eball {x : Fin d → ℝ} (hx : x ∈ eball d) : -x ∈ eball d",
 "zero_mem_eball": "theorem zero_mem_eball : (0 : Fin d → ℝ) ∈ eball d",
 "lor_sharpVec": "theorem lor_sharpVec {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : Lor (sharpVec b)",
 "sharpEff_isEffectOn": "theorem sharpEff_isEffectOn {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) :\n    IsEffectOn (eball d) (sharpEff b)",
 "sharpEff_self": "theorem sharpEff_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : sharpEff b b = 1",
 "sharpEff_neg_self": "theorem sharpEff_neg_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : sharpEff b (-b) = 0",
 "sharpEff_sharpSeed": "theorem sharpEff_sharpSeed {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) :\n    SharpSeed (eball d) (sharpEff b)",
 "isBoundaryState_eball_of_sphere": "theorem isBoundaryState_eball_of_sphere {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) :\n    IsBoundaryState (eball d) b",
 "sphere_of_isBoundaryState_eball": "theorem sphere_of_isBoundaryState_eball {x : Fin d → ℝ} (h : IsBoundaryState (eball d) x) :\n    ∑ j, x j ^ 2 = 1",
 "ehom_apply": "theorem ehom_apply (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :\n    e x = ehom e 0 + ∑ j, ehom e j.succ * x j",
 "sharp_eq_of_certain": "theorem sharp_eq_of_certain {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) r)\n    {u w : Fin d → ℝ} (hu : u ∈ eball d) (hw : w ∈ eball d) (h1 : r u = 1) (h0 : r w = 0) :\n    ∑ j : Fin d, u j ^ 2 = 1 ∧ r = sharpEff u",
 "fullAut": "def fullAut (d : ℕ) : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)) :=\n  {g | ∀ x ∈ eball d, g x ∈ eball d ∧ g.symm x ∈ eball d}",
 "preservesBody_fullAut": "theorem preservesBody_fullAut : PreservesBody (eball d) (fullAut d)",
 "reflLin": "noncomputable def reflLin (m : Fin d → ℝ) : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ) where\n  toFun x := x - (2 * (∑ j, x j * m j) / ∑ j, m j ^ 2) • m\n  map_add' x y := by\n    have h : ∑ j, (x + y) j * m j = ∑ j, x j * m j + ∑ j, y j * m j := by\n      rw [← Finset.sum_add_distrib]\n      exact Finset.sum_congr rfl fun j _ => by rw [Pi.add_apply]; ring\n    funext i\n    show (x + y) i - (2 * (∑ j, (x + y) j * m j) / ∑ j, m j ^ 2) * m i =\n      (x i - (2 * (∑ j, x j * m j) / ∑ j, m j ^ 2) * m i) +\n        (y i - (2 * (∑ j, y j * m j) / ∑ j, m j ^ 2) * m i)\n    rw [h, Pi.add_apply]\n    ring\n  map_smul' c x := by\n    have h : ∑ j, (c • x) j * m j = c * ∑ j, x j * m j := by\n      rw [Finset.mul_sum]\n      exact Finset.sum_congr rfl fun j _ => by rw [Pi.smul_apply, smul_eq_mul]; ring\n    funext i\n    show (c • x) i - (2 * (∑ j, (c • x) j * m j) / ∑ j, m j ^ 2) * m i =\n      c * (x i - (2 * (∑ j, x j * m j) / ∑ j, m j ^ 2) * m i)\n    rw [h, Pi.smul_apply, smul_eq_mul]\n    ring",
 "reflLin_apply": "theorem reflLin_apply (m x : Fin d → ℝ) :\n    reflLin m x = x - (2 * (∑ j, x j * m j) / ∑ j, m j ^ 2) • m",
 "reflLin_dot": "theorem reflLin_dot {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :\n    ∑ j, reflLin m x j * m j = -∑ j, x j * m j",
 "reflLin_reflLin": "theorem reflLin_reflLin {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :\n    reflLin m (reflLin m x) = x",
 "reflLin_sq": "theorem reflLin_sq {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :\n    ∑ j, reflLin m x j ^ 2 = ∑ j, x j ^ 2",
 "reflAff": "noncomputable def reflAff {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) :\n    (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) :=\n  (LinearEquiv.ofInvolutive (reflLin m) (reflLin_reflLin hm)).toAffineEquiv",
 "reflAff_apply": "theorem reflAff_apply {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :\n    reflAff hm x = reflLin m x",
 "reflAff_symm_apply": "theorem reflAff_symm_apply {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :\n    (reflAff hm).symm x = reflLin m x",
 "reflAff_mem_fullAut": "theorem reflAff_mem_fullAut {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) : reflAff hm ∈ fullAut d",
 "refl_mem_fullAut": "theorem refl_mem_fullAut : AffineEquiv.refl ℝ (Fin d → ℝ) ∈ fullAut d",
 "reflLin_swap": "theorem reflLin_swap {u v : Fin d → ℝ} (hu : ∑ j, u j ^ 2 = 1) (hv : ∑ j, v j ^ 2 = 1)\n    (hm : ∑ j, (u - v) j ^ 2 ≠ 0) : reflLin (u - v) u = v",
 "boundaryTransitive_fullAut": "theorem boundaryTransitive_fullAut : BoundaryTransitive (eball d) (fullAut d)",
 "seedTransport_mem_sharpFamily": "theorem seedTransport_mem_sharpFamily (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) {g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hg : g ∈ G) :\n    seedTransport r g ∈ sharpFamily d",
 "sharpFamily_subset_avail": "theorem sharpFamily_subset_avail (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) :\n    sharpFamily d ⊆ avail",
 "seedOrbit_subset_sharpFamily": "theorem seedOrbit_subset_sharpFamily (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) : seedOrbit G r ⊆ sharpFamily d",
 "sharpFamily_subset_seedOrbit": "theorem sharpFamily_subset_seedOrbit (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) :\n    sharpFamily d ⊆ seedOrbit G r",
 "seedOrbit_eq_sharpFamily": "theorem seedOrbit_eq_sharpFamily (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : BoundaryTransitive (eball d) G) : seedOrbit G r = sharpFamily d",
 "maxConeOf": "def maxConeOf (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Set (W d) :=\n  {ω | ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}",
 "maxConeOf_fullEffects": "theorem maxConeOf_fullEffects (Ω : Set (Fin d → ℝ)) : maxConeOf (fullEffects Ω) = maxCone Ω",
 "maxConeOf_anti": "theorem maxConeOf_anti {A B : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (h : A ⊆ B) :\n    maxConeOf B ⊆ maxConeOf A",
 "axisVec": "noncomputable def axisVec (hd : 0 < d) : Fin d → ℝ := Pi.single (⟨0, hd⟩ : Fin d) 1",
 "axisVec_sq": "theorem axisVec_sq (hd : 0 < d) : ∑ j, axisVec hd j ^ 2 = 1",
 "hom_zero_eq_sharp": "theorem hom_zero_eq_sharp (b : Fin d → ℝ) : hom (0 : Fin d → ℝ) = sharpVec b + sharpVec (-b)",
 "lor_decomp": "theorem lor_decomp (hd : 0 < d) {v : HVec d} (hv : Lor v) :\n    ∃ α β : ℝ, ∃ b : Fin d → ℝ, 0 ≤ α ∧ 0 ≤ β ∧ ∑ j, b j ^ 2 = 1 ∧\n      v = α • hom (0 : Fin d → ℝ) + β • sharpVec b",
 "nonneg_of_sharp": "theorem nonneg_of_sharp (hd : 0 < d) (L : HVec d →ₗ[ℝ] ℝ)\n    (h : ∀ b : Fin d → ℝ, ∑ j, b j ^ 2 = 1 → 0 ≤ L (sharpVec b)) {v : HVec d} (hv : Lor v) :\n    0 ≤ L v",
 "pvRight": "def pvRight (a : HVec d) (ω : W d) : HVec d →ₗ[ℝ] ℝ where\n  toFun b := pairVal a b ω\n  map_add' b b' := pairVal_add_right a b b' ω\n  map_smul' c b := pairVal_smul_right c a b ω",
 "pvRight_apply": "theorem pvRight_apply (a b : HVec d) (ω : W d) : pvRight a ω b = pairVal a b ω",
 "prodEffVal_sharp": "theorem prodEffVal_sharp (x y : Fin d → ℝ) (ω : W d) :\n    prodEffVal (sharpEff x) (sharpEff y) ω = pairVal (sharpVec x) (sharpVec y) ω",
 "maxCone_subset_maxConeOf_sharp": "theorem maxCone_subset_maxConeOf_sharp : maxCone (eball d) ⊆ maxConeOf (sharpFamily d)",
 "maxConeOf_sharp_subset_maxCone": "theorem maxConeOf_sharp_subset_maxCone (hd : 0 < d) :\n    maxConeOf (sharpFamily d) ⊆ maxCone (eball d)",
 "maxConeOf_sharpFamily": "theorem maxConeOf_sharpFamily (hd : 0 < d) : maxConeOf (sharpFamily d) = maxCone (eball d)",
 "cone_of_orbit": "theorem cone_of_orbit (hd : 0 < d) (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)\n    (hV4 : SeedOrbitAvailable G r avail) :\n    sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)",
 "EffectsOn": "def EffectsOn (Ω : Set (Fin d → ℝ)) (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop :=\n  ∀ e ∈ A, IsEffectOn Ω e",
 "maxConeOf_avail_eq": "theorem maxConeOf_avail_eq (hd : 0 < d) (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)\n    (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) :\n    maxConeOf avail = maxCone (eball d)",
 "unitSpan": "def unitSpan (S : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ) :=\n  {e | ∃ f ∈ S, ∃ α β : ℝ, 0 ≤ α ∧ 0 ≤ β ∧ α + β ≤ 1 ∧ e = α • unitEff d + β • f}",
 "MixingClosed": "def MixingClosed (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop :=\n  ∀ e ∈ A, ∀ f ∈ A, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ A",
 "mix_apply": "theorem mix_apply (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (α β : ℝ) (x : Fin d → ℝ) :\n    (α • e + β • f) x = α * e x + β * f x",
 "effect_eq_affine": "theorem effect_eq_affine {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e) :\n    ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧\n      ∀ x, e x = a + ∑ j, v j * x j",
 "isEffectOn_of_affine": "theorem isEffectOn_of_affine {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {a : ℝ} {v : Fin d → ℝ}\n    (hv : Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a)) (he : ∀ x, e x = a + ∑ j, v j * x j) :\n    IsEffectOn (eball d) e",
 "fullEffects_subset_unitSpan": "theorem fullEffects_subset_unitSpan (hd : 0 < d) :\n    fullEffects (eball d) ⊆ unitSpan (sharpFamily d)",
 "unitSpan_subset_fullEffects": "theorem unitSpan_subset_fullEffects : unitSpan (sharpFamily d) ⊆ fullEffects (eball d)",
 "fullEffects_eq_unitSpan": "theorem fullEffects_eq_unitSpan (hd : 0 < d) :\n    fullEffects (eball d) = unitSpan (sharpFamily d)",
 "fullEffects_subset_avail": "theorem fullEffects_subset_avail (hd : 0 < d) (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)\n    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) (hM : MixingClosed avail) :\n    fullEffects (eball d) ⊆ avail",
 "avail_eq_fullEffects": "theorem avail_eq_fullEffects (hd : 0 < d) (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)\n    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) (hM : MixingClosed avail)\n    (hE : EffectsOn (eball d) avail) : avail = fullEffects (eball d)",
 "sharpUnitFamily": "def sharpUnitFamily (d : ℕ) : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ) := insert (unitEff d) (sharpFamily d)",
 "halfEff": "noncomputable def halfEff (d : ℕ) : (Fin d → ℝ) →ᵃ[ℝ] ℝ := (1 / 2 : ℝ) • unitEff d",
 "halfEff_apply": "theorem halfEff_apply (x : Fin d → ℝ) : halfEff d x = 1 / 2",
 "halfEff_mem_fullEffects": "theorem halfEff_mem_fullEffects : halfEff d ∈ fullEffects (eball d)",
 "halfEff_not_mem_sharpUnitFamily": "theorem halfEff_not_mem_sharpUnitFamily : halfEff d ∉ sharpUnitFamily d",
 "not_fullEffects_of_orbit": "theorem not_fullEffects_of_orbit (hd : 0 < d) :\n    PreservesBody (eball d) (fullAut d) ∧ SharpSeed (eball d) (sharpEff (axisVec hd)) ∧\n      BoundaryTransitive (eball d) (fullAut d) ∧\n      SeedOrbitAvailable (fullAut d) (sharpEff (axisVec hd)) (sharpUnitFamily d) ∧\n      unitEff d ∈ sharpUnitFamily d ∧ EffectsOn (eball d) (sharpUnitFamily d) ∧\n      ¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d",
 "maxConeOf_sharpFamily_zero_ne": "theorem maxConeOf_sharpFamily_zero_ne : maxConeOf (sharpFamily 0) ≠ maxCone (eball 0)",
 "axisFamily": "def axisFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ) :=\n  {unitEff 3, sharpEff ![0, 0, 1], sharpEff ![0, 0, -1]}",
 "outVec": "noncomputable def outVec : W 3 := tens ![1, 2, 0, 0] ![1, 2, 0, 0]",
 "ehom_unitEff": "theorem ehom_unitEff (d : ℕ) : ehom (unitEff d) = hom (0 : Fin d → ℝ)",
 "maxConeOf_axis_ne": "theorem maxConeOf_axis_ne : maxConeOf axisFamily ≠ maxCone (eball 3)",
 "not_boundaryTransitive_of_countable": "theorem not_boundaryTransitive_of_countable {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}\n    (hG : G.Countable) : ¬ BoundaryTransitive (eball 3) G",
 "eff1_core": "theorem eff1_core :\n    (∀ d : ℕ, 0 < d → maxConeOf (sharpFamily d) = maxCone (eball d)) ∧\n    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), 0 < d → PreservesBody (eball d) G →\n        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →\n        sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)) ∧\n    (∀ (d : ℕ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ), IsEffectOn (eball d) e →\n        ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧\n          ∀ x, e x = a + ∑ j, v j * x j) ∧\n    (∀ d : ℕ, 0 < d → fullEffects (eball d) = unitSpan (sharpFamily d)) ∧\n    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), 0 < d → PreservesBody (eball d) G →\n        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →\n        unitEff d ∈ avail → MixingClosed avail → fullEffects (eball d) ⊆ avail) ∧\n    (∀ d : ℕ, 0 < d → ∃ (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), PreservesBody (eball d) G ∧\n        SharpSeed (eball d) r ∧ BoundaryTransitive (eball d) G ∧ SeedOrbitAvailable G r avail ∧\n        unitEff d ∈ avail ∧ EffectsOn (eball d) avail ∧ ¬ MixingClosed avail ∧\n        ¬ fullEffects (eball d) ⊆ avail) ∧\n    maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) ∧\n    maxConeOf axisFamily ≠ maxCone (eball 3) ∧\n    (∀ G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)), G.Countable → ¬ BoundaryTransitive (eball 3) G)"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.EffectSpace.sharpEff_isEffectOn",
 "OIBridge.EffectSpace.sharpEff_sharpSeed",
 "OIBridge.EffectSpace.isBoundaryState_eball_of_sphere",
 "OIBridge.EffectSpace.sphere_of_isBoundaryState_eball",
 "OIBridge.EffectSpace.sharp_eq_of_certain",
 "OIBridge.EffectSpace.preservesBody_fullAut",
 "OIBridge.EffectSpace.reflLin_swap",
 "OIBridge.EffectSpace.boundaryTransitive_fullAut",
 "OIBridge.EffectSpace.seedTransport_mem_sharpFamily",
 "OIBridge.EffectSpace.sharpFamily_subset_avail",
 "OIBridge.EffectSpace.seedOrbit_eq_sharpFamily",
 "OIBridge.EffectSpace.maxConeOf_fullEffects",
 "OIBridge.EffectSpace.lor_decomp",
 "OIBridge.EffectSpace.nonneg_of_sharp",
 "OIBridge.EffectSpace.maxCone_subset_maxConeOf_sharp",
 "OIBridge.EffectSpace.maxConeOf_sharp_subset_maxCone",
 "OIBridge.EffectSpace.maxConeOf_sharpFamily",
 "OIBridge.EffectSpace.cone_of_orbit",
 "OIBridge.EffectSpace.maxConeOf_avail_eq",
 "OIBridge.EffectSpace.effect_eq_affine",
 "OIBridge.EffectSpace.isEffectOn_of_affine",
 "OIBridge.EffectSpace.fullEffects_subset_unitSpan",
 "OIBridge.EffectSpace.unitSpan_subset_fullEffects",
 "OIBridge.EffectSpace.fullEffects_eq_unitSpan",
 "OIBridge.EffectSpace.fullEffects_subset_avail",
 "OIBridge.EffectSpace.avail_eq_fullEffects",
 "OIBridge.EffectSpace.not_fullEffects_of_orbit",
 "OIBridge.EffectSpace.maxConeOf_sharpFamily_zero_ne",
 "OIBridge.EffectSpace.maxConeOf_axis_ne",
 "OIBridge.EffectSpace.not_boundaryTransitive_of_countable",
 "OIBridge.EffectSpace.eff1_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.CompositeDimension\nimport OIBridge.CompositeInterface\nimport Mathlib.Analysis.Real.Cardinality\n\nnamespace OIBridge\nnamespace EffectSpace\n\nopen Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface\n\nvariable {d : ℕ}\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace EffectSpace",
 "open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface",
 "variable {d : ℕ}",
 "section Generation",
 "variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}\n  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}",
 "end Generation",
 "section ConeGeneration",
 "variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}\n  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}",
 "end ConeGeneration",
 "section SetGeneration",
 "variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}\n  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}",
 "end SetGeneration",
 "end EffectSpace",
 "end OIBridge"
]''')
N_PRINTS = 31

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



PREFIX = 'OIBridge.EffectSpace.'
# OG-1's four named hypotheses, as they bind in the module (G, r, avail from the section `variable`)
OG4 = ('(hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) '
       '(hV4 : SeedOrbitAvailable G r avail)')
HD = '(hd : 0 < d)'
MIX = '(hU : unitEff d ∈ avail) (hM : MixingClosed avail)'
# S1 -- Q-CONE
CONE_INCL = {
    'maxCone_subset_maxConeOf_sharp': ('', 'maxCone (eball d) ⊆ maxConeOf (sharpFamily d)'),
    'maxConeOf_sharp_subset_maxCone': (HD, 'maxConeOf (sharpFamily d) ⊆ maxCone (eball d)'),
}
CONE_EQ = ('maxConeOf_sharpFamily', HD, 'maxConeOf (sharpFamily d) = maxCone (eball d)')
CONE_CONCL = 'sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)'
GEN = ('sharpFamily_subset_avail', OG4, 'sharpFamily d ⊆ avail')
# S2 -- Q-SET
UPPER = {
    'effect_eq_affine': ('{e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e)',
                         '∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧ '
                         '∀ x, e x = a + ∑ j, v j * x j'),
    'isEffectOn_of_affine': ('{e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {a : ℝ} {v : Fin d → ℝ} '
                             '(hv : Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a)) (he : ∀ x, e x = a + ∑ j, v j * x j)',
                             'IsEffectOn (eball d) e'),
}
DECOMP_INCL = {
    'fullEffects_subset_unitSpan': (HD, 'fullEffects (eball d) ⊆ unitSpan (sharpFamily d)'),
    'unitSpan_subset_fullEffects': ('', 'unitSpan (sharpFamily d) ⊆ fullEffects (eball d)'),
}
DECOMP_EQ = ('fullEffects_eq_unitSpan', HD, 'fullEffects (eball d) = unitSpan (sharpFamily d)')
SET_CONCL = 'fullEffects (eball d) ⊆ avail'
COUNTER_CONCL = ('PreservesBody (eball d) (fullAut d) ∧ SharpSeed (eball d) (sharpEff (axisVec hd)) ∧ '
                 'BoundaryTransitive (eball d) (fullAut d) ∧ '
                 'SeedOrbitAvailable (fullAut d) (sharpEff (axisVec hd)) (sharpUnitFamily d) ∧ '
                 'unitEff d ∈ sharpUnitFamily d ∧ EffectsOn (eball d) (sharpUnitFamily d) ∧ '
                 '¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d')
# S3 -- frozen definitions
MAXCONEOF_BODY = '{ω | ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}'
MIXING_BODY = '∀ e ∈ A, ∀ f ∈ A, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ A'
FROZEN_WHOLE = ['maxConeOf', 'MixingClosed', 'EffectsOn', 'unitSpan', 'sharpFamily', 'sharpEff', 'sharpVec',
                'fullAut', 'sharpUnitFamily']
# S4 -- premises concluded only of named witnesses
PREMISES = ('SharpSeed', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable', 'MixingClosed', 'EffectsOn')
WITNESS_THEOREMS = {
    'sharpEff_sharpSeed': 'SharpSeed (eball d) (sharpEff b)',
    'preservesBody_fullAut': 'PreservesBody (eball d) (fullAut d)',
    'boundaryTransitive_fullAut': 'BoundaryTransitive (eball d) (fullAut d)',
    'not_fullEffects_of_orbit': COUNTER_CONCL,
}
VERDICT = 'eff1_core'
# S5 -- reuse
REUSED = ('maxCone', 'Lor', 'ehom', 'affOf', 'IsEffectOn', 'fullEffects', 'eball', 'mem_eball', 'SharpSeed',
          'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable', 'seedTransport', 'seedOrbit', 'unitEff',
          'prodEffVal', 'pairVal', 'ballEffect', 'directionalFamily', 'lor_ehom', 'lor_pair_bound')
IMPORT_OK = re.compile(r'^import (OIBridge\.CompositeDimension|OIBridge\.CompositeInterface|Mathlib\.[\w.]+)$')
# S6 -- field-neutral, no drive, no limit closure
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'ElementaryDrivability', 'flow', 'Flow', 'rot3', 'J_off_axis', 'LimitClosed', 'closure',
                  'Tendsto', 'Filter', 'TensorProduct', 'Hilbert')
# S7 -- phrases
PHRASES = ('OI supplies', 'derived from OI', 'sourced from OI', 'mixing closure is derived',
           'full effect set is derived', 'effect premise is discharged', 'qubit effect space')
# S8 -- dimension
HD_ONLY = sorted(['maxConeOf_sharp_subset_maxCone', 'maxConeOf_sharpFamily', 'cone_of_orbit', 'maxConeOf_avail_eq',
                  'fullEffects_subset_unitSpan', 'fullEffects_eq_unitSpan', 'fullEffects_subset_avail',
                  'avail_eq_fullEffects', 'not_fullEffects_of_orbit', 'axisVec', 'axisVec_sq', 'lor_decomp',
                  'nonneg_of_sharp', 'eff1_core'])
HD_RE = re.compile(r'0\s*<\s*d(?![\w\'])|(?<![\w\'])d\s*>\s*0|1\s*≤\s*d(?![\w\'])|(?<![\w\'])d\s*≥\s*1'
                   r'|d\s*≠\s*0')
CONTROL_SECTIONS = ('§F', 'verdict')
DIM3 = re.compile(r'(?<![\w\'.])(Fin|eball|W|HVec|sharpFamily|fullAut|fullEffects)\s+3(?![\w\'])'
                  r'|(?<![\w\'.])(ball3|eball_three)(?![\w\'])')
NEGATED = ('¬ BoundaryTransitive (eball 3) G',)
# V -- the frozen decision rule
QSET_TOKENS = ('DERIVED-FULL-EFFECTS', 'CONDITIONAL-FULL-EFFECTS', 'INSUFFICIENT-EVEN-WITH-MIXING')
QCONE_TOKENS = ('CONE-DERIVED', 'CONE-CONDITIONAL', 'CONE-INSUFFICIENT')


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def explicit_binders(b):
    """The binders with every implicit `{...}` group removed: the classification ignores how the variables bind."""
    return norm(re.sub(r'\{[^{}]*\}', ' ', b))


def theorems_with(texts, kinds, binders, concl):
    out = []
    for n, t in texts.items():
        if kinds.get(n) != 'theorem':
            continue
        bb, cc = stmt_parts(texts, n)
        if explicit_binders(bb) == norm(binders) and cc == norm(concl):
            out.append(n)
    return sorted(out)


def insufficient_set(concl):
    """A countermodel with the mixing closure: the four hypotheses, the unit and MixingClosed hold positively and
    some effect is missing."""
    c = norm(concl)
    return all(t in c for t in ('PreservesBody', 'SharpSeed', 'BoundaryTransitive', 'SeedOrbitAvailable')) and \
        re.search(r'(?<!¬ )MixingClosed', c) is not None and '¬ fullEffects (eball d) ⊆' in c and \
        '¬ MixingClosed' not in c


def insufficient_cone(concl):
    c = norm(concl)
    return all(t in c for t in ('PreservesBody', 'SharpSeed', 'BoundaryTransitive', 'SeedOrbitAvailable',
                                'EffectsOn')) and \
        re.search(r'(?<!¬ )MixingClosed', c) is not None and '≠ maxCone (eball d)' in c and '¬ MixingClosed' not in c


def verdicts(chunks):
    """The frozen decision rule. Each question's outcome is read from the module's theorem statements alone.

    Q-CONE  CONE-DERIVED       a theorem with binders exactly `(hd : 0 < d)` and OG-1's four hypotheses and
                               conclusion `sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)`,
                               and the two inclusions of S1
            CONE-CONDITIONAL   the same conclusion only with the unit and `MixingClosed` added to the binders
            CONE-INSUFFICIENT  a theorem concluding a family with the four hypotheses, the unit, `MixingClosed` and
                               `EffectsOn` whose cone is not `maxCone (eball d)`
    Q-SET   DERIVED-FULL-EFFECTS          a theorem with binders exactly `(hd : 0 < d)` and OG-1's four hypotheses
                                          and conclusion `fullEffects (eball d) ⊆ avail`
            CONDITIONAL-FULL-EFFECTS      that conclusion only with the unit and `MixingClosed` added, together with
                                          the countermodel `not_fullEffects_of_orbit` with its frozen conclusion
            INSUFFICIENT-EVEN-WITH-MIXING a theorem concluding a family with the four hypotheses, the unit and
                                          `MixingClosed` and some effect missing
    A question with no outcome, or with more than one, has no verdict."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    concls = {n: norm(split_statement(t)[1]) for n, t in texts.items() if kinds.get(n) == 'theorem'}
    incl = all(stmt_parts(texts, n) == (norm(b), norm(c)) and kinds.get(n) == 'theorem'
               for n, (b, c) in CONE_INCL.items())
    cone = []
    if incl and theorems_with(texts, kinds, HD + ' ' + OG4, CONE_CONCL):
        cone.append('CONE-DERIVED')
    if incl and theorems_with(texts, kinds, HD + ' ' + OG4 + ' ' + MIX, CONE_CONCL):
        cone.append('CONE-CONDITIONAL')
    if any(insufficient_cone(c) for c in concls.values()):
        cone.append('CONE-INSUFFICIENT')
    st = []
    if theorems_with(texts, kinds, HD + ' ' + OG4, SET_CONCL):
        st.append('DERIVED-FULL-EFFECTS')
    if theorems_with(texts, kinds, HD + ' ' + OG4 + ' ' + MIX, SET_CONCL) and \
            stmt_parts(texts, 'not_fullEffects_of_orbit') == (HD, norm(COUNTER_CONCL)):
        st.append('CONDITIONAL-FULL-EFFECTS')
    if any(insufficient_set(c) for c in concls.values()):
        st.append('INSUFFICIENT-EVEN-WITH-MIXING')
    return st, cone


def hd_violations(texts):
    return sorted(n for n, t in texts.items() if HD_RE.search(code_only(t)))


def numeral3_violations(mod):
    secs = sections(mod)
    bad = []
    sp = spans(mod)
    first = sp[0][2] if sp else len(mod)
    if DIM3.search(code_only(mod[:first])):
        bad.append('preamble')
    for kind, name, start, se, nxt, cend in sp:
        if section_at(secs, start) in CONTROL_SECTIONS:
            continue
        if DIM3.search(code_only(mod[start:nxt])):
            bad.append(name)
    return bad


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    bad1 = [n for n, (b, c) in CONE_INCL.items()
            if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or PREFIX + n not in prints]
    n, b, c = CONE_EQ
    if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or \
            not all(token(m, proofs.get(n, '')) for m in CONE_INCL):
        bad1.append(n)
    if stmt_parts(texts, 'cone_of_orbit') != (norm(HD + ' ' + OG4), norm(CONE_CONCL)):
        bad1.append('cone_of_orbit')
    if stmt_parts(texts, GEN[0]) != (norm(GEN[1]), norm(GEN[2])):
        bad1.append(GEN[0])
    for m in ('cone_of_orbit', GEN[0]):
        if any(t in texts.get(m, '') for t in ('MixingClosed', 'unitEff', 'EffectsOn')):
            bad1.append(m)
    check('S1', 'Q-CONE: both inclusions with their frozen statements, the equality from both by name, the cone '
                'theorem and the generation theorem on OG-1\'s four hypotheses alone%s%s'
          % (tag, (' %s' % bad1[:3]) if bad1 else ''), not bad1)
    # S2
    bad2 = [n for n, (b, c) in list(UPPER.items()) + list(DECOMP_INCL.items())
            if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or PREFIX + n not in prints]
    n, b, c = DECOMP_EQ
    if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or \
            not all(token(m, proofs.get(n, '')) for m in DECOMP_INCL):
        bad2.append(n)
    if stmt_parts(texts, 'fullEffects_subset_avail') != (norm(HD + ' ' + OG4 + ' ' + MIX), norm(SET_CONCL)):
        bad2.append('fullEffects_subset_avail')
    if stmt_parts(texts, 'not_fullEffects_of_orbit') != (HD, norm(COUNTER_CONCL)) or \
            PREFIX + 'not_fullEffects_of_orbit' not in prints:
        bad2.append('not_fullEffects_of_orbit')
    check('S2', 'Q-SET: the upper bound and the decomposition in both directions, the equality from both by name, '
                'the conditional generation on the four hypotheses, the unit and MixingClosed, and the countermodel'
                '%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    check('S3', 'the frozen definitions whole; maxConeOf over the given family; MixingClosed sub-convex' + tag,
          all(texts.get(n) == TEXTS.get(n) and kinds.get(n) in ('def', 'noncomputable def') for n in FROZEN_WHOLE)
          and norm(texts.get('maxConeOf', '')).endswith(':= ' + MAXCONEOF_BODY)
          and norm(texts.get('MixingClosed', '')).endswith(':= ' + MIXING_BODY))
    # S4
    bad4 = []
    for n, (k, t, _) in chunks.items():
        if k in ('theorem', 'lemma'):
            concl = norm(split_statement(t)[1])
        else:
            concl = norm(split_statement(def_header(t))[1])
        if n in WITNESS_THEOREMS:
            if concl != norm(WITNESS_THEOREMS[n]) or k != 'theorem' or PREFIX + n not in prints:
                bad4.append(n)
            continue
        if n == VERDICT:
            cc = norm(split_statement(t)[1])
            for m in re.finditer(r'MixingClosed (\w+)', cc):
                if not (cc[:m.start()].endswith('¬ ') or cc[m.end():].startswith(' →')):
                    bad4.append(n)
            continue
        for c in NEGATED:
            concl = concl.replace(c, '')
        if any(token(p, concl) for p in PREMISES):
            bad4.append(n)
    check('S4', 'the named premises concluded only of the named witnesses by the named control theorems%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    bad_imp = [l for l in imports if not IMPORT_OK.match(l)]
    check('S5', 'landed objects reused, not re-declared; imports whitelisted%s%s'
          % (tag, (' %s' % (clash + bad_imp)[:3]) if clash or bad_imp else ''),
          not clash and not bad_imp and bool(imports))
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no drive, flow or limit-closure token%s%s' % (tag, (' %s' % hits) if hits else ''),
          not hits)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    hd = hd_violations(texts)
    n3 = numeral3_violations(mod)
    check('S8', '`0 < d` in exactly the frozen statements; no dimension-three object outside the controls and the '
                'verdict%s%s'
          % (tag, (' %s %s' % (hd, n3)) if hd != HD_ONLY or n3 else ''), hd == HD_ONLY and not n3)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    st, cone = verdicts(chunks)
    check('V', 'exactly one outcome per question by the frozen rule: Q-SET %s, Q-CONE %s%s'
          % ('/'.join(st) or 'none', '/'.join(cone) or 'none', tag), len(st) == 1 and len(cone) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in QSET_TOKENS + QCONE_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


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
        st, cone = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed verdicts %s and no other outcome token (found %s)'
              % (st + cone, toks), len(st) == 1 and len(cone) == 1 and sorted(toks) == sorted(st + cone))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the DIM-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    st, cone = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
    print('VERDICT  Q-SET   %s' % ('/'.join(st) or 'none'))
    print('VERDICT  Q-CONE  %s' % ('/'.join(cone) or 'none'))
    check('V', 'exactly one outcome per question', len(st) == 1 and len(cone) == 1)


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



def append_control(text, decl):
    """Insert a declaration just before the verdict section (inside §F)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


CONE_HEAD = ('theorem cone_of_orbit (hd : 0 < d) (hG : PreservesBody (eball d) G)\n'
             '    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)\n'
             '    (hV4 : SeedOrbitAvailable G r avail) :')
SET_HEAD = ('    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) (hM : MixingClosed avail) :\n'
            '    fullEffects (eball d) ⊆ avail := by')
DERIVED_SET = ('theorem fullEffects_of_orbit_alone {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
               '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 0 < d)\n'
               '    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) '
               '(hK : BoundaryTransitive (eball d) G)\n'
               '    (hV4 : SeedOrbitAvailable G r avail) : fullEffects (eball d) ⊆ avail := by\n'
               '  exact absurd hd (by simp)')
INSUFF_SET = ('theorem insufficient_with_mixing (hd : 0 < d) : ∃ (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))\n'
              '    (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), PreservesBody (eball d) G ∧\n'
              '    SharpSeed (eball d) r ∧ BoundaryTransitive (eball d) G ∧ SeedOrbitAvailable G r avail ∧\n'
              '    unitEff d ∈ avail ∧ MixingClosed avail ∧ ¬ fullEffects (eball d) ⊆ avail := by\n'
              '  exact absurd hd (by simp)')
INSUFF_CONE = ('theorem cone_insufficient (hd : 0 < d) : ∃ (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))\n'
               '    (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), PreservesBody (eball d) G ∧\n'
               '    SharpSeed (eball d) r ∧ BoundaryTransitive (eball d) G ∧ SeedOrbitAvailable G r avail ∧\n'
               '    unitEff d ∈ avail ∧ MixingClosed avail ∧ EffectsOn (eball d) avail ∧\n'
               '    maxConeOf avail ≠ maxCone (eball d) := by\n'
               '  exact absurd hd (by simp)')


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    st, cone = verdict_of(mod)
    check('T', 'the reference module reads Q-SET %s and Q-CONE %s' % (st, cone),
          st == ['CONDITIONAL-FULL-EFFECTS'] and cone == ['CONE-DERIVED'])
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem eff1_core :', '\ntheorem eff1_core\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {Ω : Set (Fin d → ℝ)}\n'))
    must_fail('N2', 'a changed preamble',
              replace_once(mod, 'open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension '
                                'CompositeInterface',
                           'open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem sharpEff_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : sharpEff b b = 1',
                           'theorem sharpEff_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 ≤ 1) : sharpEff b b = 1'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed',
              replace_once(mod, '#print axioms OIBridge.EffectSpace.lor_decomp\n', ''))
    # S1
    must_fail('S1', 'the mixing closure added to the cone theorem',
              replace_once(mod, CONE_HEAD, CONE_HEAD[:-2] + ' (hU : unitEff d ∈ avail)\n'
                                                            '    (hM : MixingClosed avail) :'))
    must_fail('S1', 'one inclusion of the cone equality dropped from its proof',
              replace_once(mod, '  Set.Subset.antisymm (maxConeOf_sharp_subset_maxCone hd) '
                                'maxCone_subset_maxConeOf_sharp',
                           '  Set.Subset.antisymm (maxConeOf_sharp_subset_maxCone hd) (fun ω hω => by\n'
                           '    intro e he f hf\n    exact absurd he (by simp))'))
    must_fail('S1', 'an effect premise on the generation theorem',
              replace_once(mod, '    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) :\n'
                                '    sharpFamily d ⊆ avail := by',
                           '    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n'
                           '    (hE : EffectsOn (eball d) avail) : sharpFamily d ⊆ avail := by'))
    must_fail('S1', '`0 < d` added to the free inclusion',
              replace_once(mod, 'theorem maxCone_subset_maxConeOf_sharp :',
                           'theorem maxCone_subset_maxConeOf_sharp (hd : 0 < d) :'))
    # S2
    must_fail('S2', 'the mixing closure dropped from the set generation',
              replace_once(mod, SET_HEAD, '    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) :\n'
                                          '    fullEffects (eball d) ⊆ avail := by'))
    must_fail('S2', 'the countermodel weakened to keep the mixing closure open',
              replace_once(mod, '      ¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d '
                                ':= by',
                           '      ¬ fullEffects (eball d) ⊆ sharpUnitFamily d := by'))
    must_fail('S2', 'the upper bound with a weaker radius',
              replace_once(mod, '    ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧\n'
                                '      ∀ x, e x = a + ∑ j, v j * x j := by',
                           '    ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ 1 ∧\n'
                           '      ∀ x, e x = a + ∑ j, v j * x j := by'))
    # S3
    must_fail('S3', 'the cone restricted to normalized effects',
              replace_once(mod, '  {ω | ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}',
                           '  {ω | ∀ e ∈ A, ∀ f ∈ A, e 0 = 1 / 2 → 0 ≤ prodEffVal e f ω}'))
    must_fail('S3', 'the mixing closure made convex',
              replace_once(mod, '0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ A',
                           '0 ≤ α → 0 ≤ β → α + β = 1 → α • e + β • f ∈ A'))
    # S4
    must_fail('S4', 'the mixing closure concluded from the seed orbit',
              append_control(mod, 'theorem mixing_of_orbit {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
                                  '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n'
                                  '    (hV4 : SeedOrbitAvailable G r avail) : MixingClosed avail := by\n'
                                  '  exact absurd hV4 (by simp)'))
    must_fail('S4', 'seed-orbit availability concluded for a hypothesis-bound family',
              append_control(mod, 'theorem orbit_available {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
                                  '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n'
                                  '    (hP1 : SharpSeed (eball d) r) : SeedOrbitAvailable G r avail := by\n'
                                  '  exact absurd hP1 (by simp)'))
    # S5
    must_fail('S5', 'a landed definition re-declared',
              append_control(mod, 'def maxCone : ℕ := 0'))
    must_fail('S5', 'an import outside the whitelist',
              replace_once(mod, 'import OIBridge.CompositeInterface\n',
                           'import OIBridge.CompositeInterface\nimport OIBridge.SubstratumSource\n'))
    # S6
    must_fail('S6', 'a complex scalar',
              append_control(mod, 'def cvec (z : Fin d → ℂ) : Fin d → ℂ := z'))
    must_fail('S6', 'a limit closure',
              append_control(mod, 'def LimitClosed (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop := '
                                  'closure A ⊆ A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  Two separate questions,', '  OI supplies the effects. Two separate questions,'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('The sharp family determines the cone; the mixing closure is a named premise.')
          and phrase_hits('Hence the mixing closure\nis derived.') == ['mixing closure is derived'])
    # S8
    must_fail('S8', '`0 < d` added to the generation theorem',
              replace_once(mod, 'theorem sharpFamily_subset_avail (hG',
                           'theorem sharpFamily_subset_avail (hd : 0 < d) (hG'))
    must_fail('S8', 'a dimension-three object in the generation section',
              replace_once(mod, '/-! ### §D', 'theorem three_ball : eball 3 = eball 3 := rfl\n\n/-! ### §D'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.EffectSpace.eff1_core\n',
                           '#print axioms OIBridge.EffectSpace.eff1_core\n'
                           '#print axioms OIBridge.EffectSpace.sharpVec_zero\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.EffectSpace.cone_of_orbit\n',
                           '#print axioms OIBridge.EffectSpace.cone_of_orbit\n'
                           '#print axioms OIBridge.EffectSpace.cone_of_orbit\n'))
    # V -- the decision rule reads each alternative
    m_cc = replace_once(mod, CONE_HEAD, CONE_HEAD[:-2] + ' (hU : unitEff d ∈ avail)\n    (hM : MixingClosed avail) :')
    check('M', 'decision rule: the cone theorem with the mixing closure reads CONE-CONDITIONAL',
          verdict_of(m_cc)[1] == ['CONE-CONDITIONAL'])
    m_ds = replace_once(mod, SET_HEAD, '    (hV4 : SeedOrbitAvailable G r avail) :\n    fullEffects (eball d) ⊆ avail '
                                       ':= by')
    check('M', 'decision rule: the set theorem without the unit and the mixing closure reads DERIVED-FULL-EFFECTS',
          verdict_of(m_ds)[0] == ['DERIVED-FULL-EFFECTS'])
    m_nc = replace_once(mod, '      ¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d '
                             ':= by',
                        '      ¬ fullEffects (eball d) ⊆ sharpUnitFamily d := by')
    check('M', 'decision rule: without the frozen countermodel Q-SET has no verdict', verdict_of(m_nc)[0] == [])
    m_is = append_control(mod, INSUFF_SET)
    check('M', 'decision rule: a countermodel with the mixing closure reads INSUFFICIENT-EVEN-WITH-MIXING, and two '
               'outcomes fail V', verdict_of(m_is)[0] == ['CONDITIONAL-FULL-EFFECTS', 'INSUFFICIENT-EVEN-WITH-MIXING'])
    must_fail('V', 'two Q-SET outcomes at once', m_is)
    m_ic = append_control(mod, INSUFF_CONE)
    check('M', 'decision rule: a cone countermodel with the mixing closure reads CONE-INSUFFICIENT',
          'CONE-INSUFFICIENT' in verdict_of(m_ic)[1])
    m_dd = append_control(mod, DERIVED_SET)
    must_fail('V', 'a derived set theorem beside the conditional one', m_dd)
    check('M', 'note tokens: exactly the stated verdicts are found',
          note_tokens('Q-SET: CONDITIONAL-FULL-EFFECTS. Q-CONE: CONE-DERIVED.')
          == ['CONDITIONAL-FULL-EFFECTS', 'CONE-DERIVED']
          and note_tokens('Q-CONE: CONE-DERIVED, not CONE-CONDITIONAL.') == ['CONE-DERIVED', 'CONE-CONDITIONAL'])
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
