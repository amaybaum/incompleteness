#!/usr/bin/env python3
"""controls.py -- round IIP-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition, abbreviation
                  and structure is the frozen text whole; the preamble and every context line (`variable`, `open`,
                  `namespace`, `section`, `end`, `attribute`) is the frozen text, in order -- a proof may change, a
                  statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  span        `invariant_inner_product_span` is relative to the affine span: its hypotheses are the injective
                  chart of the span, its conclusion is about `bodyR L p0 Ω` (compactness, nonempty interior, and
                  `invMatrix` of the restricted body) and never about the ambient `Ω`'s moment
  S2  interior    every theorem other than the span theorem and the verdict that concludes positivity of `moment` or
                  `invMatrix` has a nonempty-interior hypothesis; the verdict states it before positivity
  S3  lower-dim   the ambient-nullity controls are present as kernel theorems with axiom prints:
                  `momentMatrix_eq_zero_of_subset` (a body in a proper affine subspace has zero ambient second
                  moment) and `segment2_moment`; no theorem concludes positivity of a form on `segment2`
  S4  scope       no declaration name, theorem conclusion or header claim of an ellipsoid, transitivity, a rotation
                  group, a drive or a dimension; the header disclaimer is present
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.OrbitNormalization`
  C   census      the census is D's with exactly the frozen family inserted after the OG-1 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib, io, json, re, subprocess, sys

D = 'f7f5c3b0c621cc3e4b57e3709d11d9d580c81149'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-iip-1-invariant-inner-product/'
PREREG = RDIR + 'preregistration.md'
MOD = 'verification/lean-mathlib/OIBridge/InvariantInnerProduct.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '282b32f8954365c72581aad7486300375283311e'
ANCHOR_IMPORT = 'import OIBridge.OrbitNormalization\n'
NEW_IMPORT = 'import OIBridge.InvariantInnerProduct\n'
OG1_FAMILY_PREFIX = 'conditional orbit-generation infrastructure'
CENSUS_FAMILY = json.loads(r'''{
 "name": "the common fixed point and invariant inner product of the affine automorphisms of a compact convex body, on the translation space of its affine span — centroid and second-moment form (round IIP-1, reconstruction)",
 "modules": [
  "InvariantInnerProduct"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round IIP-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-iip-1-invariant-inner-product/preregistration.md. The kernel layer is premise-free: for a compact body with nonempty interior in coordinates Fin n → ℝ, every affine automorphism g with g '' Ω = Ω has |det| = 1 and fixes the centroid (centroid_fixed); the second-moment matrix S is symmetric and positive definite and satisfies A S Aᵀ = S for the linear part A (momentMatrix_conj); the inverse S⁻¹ is symmetric, positive definite and invariant under A (invariant_inner_product); through an injective affine chart of the affine span of a compact convex body the same holds on the translation space, where the body has nonempty interior, for every restriction of every automorphism of the body (invariant_inner_product_span). A body contained in a proper affine subspace has a vanishing ambient second moment (momentMatrix_eq_zero_of_subset, segment2_moment). No group, compactness of a group or Haar measure is used. Carried by no manuscript. Nothing here claims an ellipsoid, transitivity or a dimension, and nothing sources a drive."
}''')
DECLS = json.loads(r'''[
 [
  "noncomputable def",
  "linMatrix"
 ],
 [
  "theorem",
  "mulVec_apply_eq"
 ],
 [
  "theorem",
  "affine_apply_eq"
 ],
 [
  "theorem",
  "affine_sub_eq"
 ],
 [
  "theorem",
  "hasFDerivWithinAt_affine"
 ],
 [
  "theorem",
  "setIntegral_comp"
 ],
 [
  "theorem",
  "abs_det_eq_one"
 ],
 [
  "theorem",
  "setIntegral_comp_eq"
 ],
 [
  "theorem",
  "det_linMatrix_ne_zero"
 ],
 [
  "noncomputable def",
  "centroid"
 ],
 [
  "theorem",
  "integrableOn_coord"
 ],
 [
  "theorem",
  "setIntegral_mulVec_coord"
 ],
 [
  "theorem",
  "centroid_fixed"
 ],
 [
  "noncomputable def",
  "moment"
 ],
 [
  "noncomputable def",
  "momentMatrix"
 ],
 [
  "theorem",
  "moment_symm"
 ],
 [
  "theorem",
  "continuous_dot_sub"
 ],
 [
  "theorem",
  "integrableOn_moment"
 ],
 [
  "theorem",
  "dot_eq_sum_single"
 ],
 [
  "theorem",
  "moment_eq_dotProduct"
 ],
 [
  "theorem",
  "momentMatrix_transpose"
 ],
 [
  "theorem",
  "moment_pos"
 ],
 [
  "theorem",
  "momentMatrix_det_ne_zero"
 ],
 [
  "theorem",
  "dot_mulVec_transpose"
 ],
 [
  "theorem",
  "moment_transpose_invariant"
 ],
 [
  "theorem",
  "momentMatrix_conj"
 ],
 [
  "noncomputable def",
  "invMatrix"
 ],
 [
  "theorem",
  "invMatrix_transpose"
 ],
 [
  "theorem",
  "invMatrix_pos"
 ],
 [
  "theorem",
  "invariant_inner_product"
 ],
 [
  "theorem",
  "interior_bodyR_nonempty"
 ],
 [
  "theorem",
  "isCompact_bodyR"
 ],
 [
  "theorem",
  "image_bodyR_eq"
 ],
 [
  "theorem",
  "invariant_inner_product_span"
 ],
 [
  "theorem",
  "momentMatrix_eq_zero_of_null"
 ],
 [
  "theorem",
  "momentMatrix_eq_zero_of_subset"
 ],
 [
  "def",
  "segment2"
 ],
 [
  "theorem",
  "volume_segment2"
 ],
 [
  "theorem",
  "segment2_moment"
 ],
 [
  "theorem",
  "iip1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "linMatrix": "noncomputable def linMatrix (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) : Matrix (Fin n) (Fin n) ℝ :=\n  LinearMap.toMatrix' g.toAffineMap.linear",
 "mulVec_apply_eq": "theorem mulVec_apply_eq (M : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (i : Fin n) :\n    (M *ᵥ v) i = ∑ k, M i k * v k",
 "affine_apply_eq": "theorem affine_apply_eq (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (x : Fin n → ℝ) :\n    g x = linMatrix g *ᵥ x + g 0",
 "affine_sub_eq": "theorem affine_sub_eq (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (x y : Fin n → ℝ) :\n    g x - g y = linMatrix g *ᵥ (x - y)",
 "hasFDerivWithinAt_affine": "theorem hasFDerivWithinAt_affine (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (s : Set (Fin n → ℝ))\n    (x : Fin n → ℝ) :\n    HasFDerivWithinAt (g : (Fin n → ℝ) → (Fin n → ℝ))\n      (LinearMap.toContinuousLinearMap g.toAffineMap.linear) s x",
 "setIntegral_comp": "theorem setIntegral_comp {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω)\n    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) (h : (Fin n → ℝ) → ℝ) :\n    ∫ x in Ω, h x = |LinearMap.det g.toAffineMap.linear| * ∫ x in Ω, h (g x)",
 "abs_det_eq_one": "theorem abs_det_eq_one {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω) (hpos : 0 < volume.real Ω)\n    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :\n    |LinearMap.det g.toAffineMap.linear| = 1",
 "setIntegral_comp_eq": "theorem setIntegral_comp_eq {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω)\n    (hpos : 0 < volume.real Ω) (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω)\n    (h : (Fin n → ℝ) → ℝ) :\n    ∫ x in Ω, h (g x) = ∫ x in Ω, h x",
 "det_linMatrix_ne_zero": "theorem det_linMatrix_ne_zero {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω)\n    (hpos : 0 < volume.real Ω) (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :\n    (linMatrix g).det ≠ 0",
 "centroid": "noncomputable def centroid (Ω : Set (Fin n → ℝ)) : Fin n → ℝ :=\n  fun i => (volume.real Ω)⁻¹ * ∫ x in Ω, x i",
 "integrableOn_coord": "theorem integrableOn_coord {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (i : Fin n) :\n    IntegrableOn (fun x : Fin n → ℝ => x i) Ω",
 "setIntegral_mulVec_coord": "theorem setIntegral_mulVec_coord {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)\n    (M : Matrix (Fin n) (Fin n) ℝ) (b : Fin n → ℝ) (i : Fin n) :\n    ∫ x in Ω, (M *ᵥ x + b) i = (∑ k, M i k * ∫ x in Ω, x k) + volume.real Ω * b i",
 "centroid_fixed": "theorem centroid_fixed {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hpos : 0 < volume.real Ω)\n    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :\n    g (centroid Ω) = centroid Ω",
 "moment": "noncomputable def moment (Ω : Set (Fin n → ℝ)) (u v : Fin n → ℝ) : ℝ :=\n  ∫ x in Ω, ((x - centroid Ω) ⬝ᵥ u) * ((x - centroid Ω) ⬝ᵥ v)",
 "momentMatrix": "noncomputable def momentMatrix (Ω : Set (Fin n → ℝ)) : Matrix (Fin n) (Fin n) ℝ :=\n  fun i j => moment Ω (Pi.single i 1) (Pi.single j 1)",
 "moment_symm": "theorem moment_symm (Ω : Set (Fin n → ℝ)) (u v : Fin n → ℝ) : moment Ω u v = moment Ω v u",
 "continuous_dot_sub": "theorem continuous_dot_sub (c u : Fin n → ℝ) :\n    Continuous fun x : Fin n → ℝ => (x - c) ⬝ᵥ u",
 "integrableOn_moment": "theorem integrableOn_moment {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (c u v : Fin n → ℝ) :\n    IntegrableOn (fun x : Fin n → ℝ => ((x - c) ⬝ᵥ u) * ((x - c) ⬝ᵥ v)) Ω",
 "dot_eq_sum_single": "theorem dot_eq_sum_single (w u : Fin n → ℝ) : w ⬝ᵥ u = ∑ i, u i * (w ⬝ᵥ Pi.single i 1)",
 "moment_eq_dotProduct": "theorem moment_eq_dotProduct {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (u v : Fin n → ℝ) :\n    moment Ω u v = u ⬝ᵥ (momentMatrix Ω *ᵥ v)",
 "momentMatrix_transpose": "theorem momentMatrix_transpose {Ω : Set (Fin n → ℝ)} : (momentMatrix Ω)ᵀ = momentMatrix Ω",
 "moment_pos": "theorem moment_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)\n    {u : Fin n → ℝ} (hu : u ≠ 0) : 0 < moment Ω u u",
 "momentMatrix_det_ne_zero": "theorem momentMatrix_det_ne_zero {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)\n    (hi : (interior Ω).Nonempty) : (momentMatrix Ω).det ≠ 0",
 "dot_mulVec_transpose": "theorem dot_mulVec_transpose (A : Matrix (Fin n) (Fin n) ℝ) (x y : Fin n → ℝ) :\n    (A *ᵥ x) ⬝ᵥ y = x ⬝ᵥ (Aᵀ *ᵥ y)",
 "moment_transpose_invariant": "theorem moment_transpose_invariant {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)\n    (hpos : 0 < volume.real Ω) (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω)\n    (u v : Fin n → ℝ) :\n    moment Ω ((linMatrix g)ᵀ *ᵥ u) ((linMatrix g)ᵀ *ᵥ v) = moment Ω u v",
 "momentMatrix_conj": "theorem momentMatrix_conj {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hpos : 0 < volume.real Ω)\n    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :\n    linMatrix g * momentMatrix Ω * (linMatrix g)ᵀ = momentMatrix Ω",
 "invMatrix": "noncomputable def invMatrix (Ω : Set (Fin n → ℝ)) : Matrix (Fin n) (Fin n) ℝ :=\n  (momentMatrix Ω)⁻¹",
 "invMatrix_transpose": "theorem invMatrix_transpose (Ω : Set (Fin n → ℝ)) : (invMatrix Ω)ᵀ = invMatrix Ω",
 "invMatrix_pos": "theorem invMatrix_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)\n    {u : Fin n → ℝ} (hu : u ≠ 0) : 0 < u ⬝ᵥ (invMatrix Ω *ᵥ u)",
 "invariant_inner_product": "theorem invariant_inner_product {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)\n    (hi : (interior Ω).Nonempty) :\n    (invMatrix Ω)ᵀ = invMatrix Ω ∧ (∀ u, u ≠ 0 → 0 < u ⬝ᵥ (invMatrix Ω *ᵥ u)) ∧\n      ∀ g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ), g '' Ω = Ω →\n        g (centroid Ω) = centroid Ω ∧\n          ∀ u v, (linMatrix g *ᵥ u) ⬝ᵥ (invMatrix Ω *ᵥ (linMatrix g *ᵥ v)) =\n            u ⬝ᵥ (invMatrix Ω *ᵥ v)",
 "interior_bodyR_nonempty": "theorem interior_bodyR_nonempty [FiniteDimensional ℝ V] {d : ℕ}\n    {L : (Fin d → ℝ) →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) {p0 : V} {Ω : Set V}\n    (hconv : Convex ℝ Ω)\n    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) :\n    (interior (bodyR L p0 Ω)).Nonempty",
 "isCompact_bodyR": "theorem isCompact_bodyR [FiniteDimensional ℝ V] {d : ℕ} {L : (Fin d → ℝ) →ₗ[ℝ] V}\n    (hL : LinearMap.ker L = ⊥) {p0 : V} {Ω : Set V} (hcomp : IsCompact Ω)\n    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) :\n    IsCompact (bodyR L p0 Ω)",
 "image_bodyR_eq": "theorem image_bodyR_eq {d : ℕ} {L : (Fin d → ℝ) →ₗ[ℝ] V} {p0 : V} {Ω : Set V}\n    {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω)\n    {g' : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hgg : ∀ w, chart L p0 (g' w) = g (chart L p0 w)) :\n    g' '' bodyR L p0 Ω = bodyR L p0 Ω",
 "invariant_inner_product_span": "theorem invariant_inner_product_span [FiniteDimensional ℝ V] {d : ℕ}\n    {L : (Fin d → ℝ) →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) {p0 : V} {Ω : Set V}\n    (hconv : Convex ℝ Ω) (hcomp : IsCompact Ω)\n    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) :\n    IsCompact (bodyR L p0 Ω) ∧ (interior (bodyR L p0 Ω)).Nonempty ∧\n      (invMatrix (bodyR L p0 Ω))ᵀ = invMatrix (bodyR L p0 Ω) ∧\n      (∀ u, u ≠ 0 → 0 < u ⬝ᵥ (invMatrix (bodyR L p0 Ω) *ᵥ u)) ∧\n      ∀ g : V ≃ᵃ[ℝ] V, (∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω) →\n        ∀ g' : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), (∀ w, chart L p0 (g' w) = g (chart L p0 w)) →\n          g' (centroid (bodyR L p0 Ω)) = centroid (bodyR L p0 Ω) ∧\n            ∀ u v, (linMatrix g' *ᵥ u) ⬝ᵥ (invMatrix (bodyR L p0 Ω) *ᵥ (linMatrix g' *ᵥ v)) =\n              u ⬝ᵥ (invMatrix (bodyR L p0 Ω) *ᵥ v)",
 "momentMatrix_eq_zero_of_null": "theorem momentMatrix_eq_zero_of_null {Ω : Set (Fin n → ℝ)} (h0 : volume Ω = 0) :\n    momentMatrix Ω = 0",
 "momentMatrix_eq_zero_of_subset": "theorem momentMatrix_eq_zero_of_subset {Ω : Set (Fin n → ℝ)} {s : AffineSubspace ℝ (Fin n → ℝ)}\n    (hs : s ≠ ⊤) (hΩ : Ω ⊆ (s : Set (Fin n → ℝ))) : momentMatrix Ω = 0",
 "segment2": "def segment2 : Set (Fin 2 → ℝ) := {x | x 1 = 0 ∧ 0 ≤ x 0 ∧ x 0 ≤ 1}",
 "volume_segment2": "theorem volume_segment2 : volume segment2 = 0",
 "segment2_moment": "theorem segment2_moment :\n    momentMatrix segment2 = 0 ∧ (Pi.single 1 1 : Fin 2 → ℝ) ≠ 0 ∧\n      moment segment2 (Pi.single 1 1) (Pi.single 1 1) = 0",
 "iip1_core": "theorem iip1_core :\n    (∀ (Ω : Set (Fin n → ℝ)), IsCompact Ω → (interior Ω).Nonempty →\n      ∀ g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ), g '' Ω = Ω →\n        g (centroid Ω) = centroid Ω ∧\n          ∀ u v, (linMatrix g *ᵥ u) ⬝ᵥ (invMatrix Ω *ᵥ (linMatrix g *ᵥ v)) =\n            u ⬝ᵥ (invMatrix Ω *ᵥ v)) ∧\n    (∀ (Ω : Set (Fin n → ℝ)), IsCompact Ω → (interior Ω).Nonempty →\n      (invMatrix Ω)ᵀ = invMatrix Ω ∧ ∀ u, u ≠ 0 → 0 < u ⬝ᵥ (invMatrix Ω *ᵥ u)) ∧\n    (∀ (Ω : Set (Fin n → ℝ)) (s : AffineSubspace ℝ (Fin n → ℝ)), s ≠ ⊤ →\n      Ω ⊆ (s : Set (Fin n → ℝ)) → momentMatrix Ω = 0) ∧\n    momentMatrix segment2 = 0"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.InvariantInnerProduct.affine_apply_eq",
 "OIBridge.InvariantInnerProduct.setIntegral_comp",
 "OIBridge.InvariantInnerProduct.abs_det_eq_one",
 "OIBridge.InvariantInnerProduct.setIntegral_comp_eq",
 "OIBridge.InvariantInnerProduct.centroid_fixed",
 "OIBridge.InvariantInnerProduct.moment_eq_dotProduct",
 "OIBridge.InvariantInnerProduct.moment_pos",
 "OIBridge.InvariantInnerProduct.momentMatrix_det_ne_zero",
 "OIBridge.InvariantInnerProduct.moment_transpose_invariant",
 "OIBridge.InvariantInnerProduct.momentMatrix_conj",
 "OIBridge.InvariantInnerProduct.invMatrix_pos",
 "OIBridge.InvariantInnerProduct.invariant_inner_product",
 "OIBridge.InvariantInnerProduct.interior_bodyR_nonempty",
 "OIBridge.InvariantInnerProduct.isCompact_bodyR",
 "OIBridge.InvariantInnerProduct.image_bodyR_eq",
 "OIBridge.InvariantInnerProduct.invariant_inner_product_span",
 "OIBridge.InvariantInnerProduct.momentMatrix_eq_zero_of_null",
 "OIBridge.InvariantInnerProduct.momentMatrix_eq_zero_of_subset",
 "OIBridge.InvariantInnerProduct.volume_segment2",
 "OIBridge.InvariantInnerProduct.segment2_moment",
 "OIBridge.InvariantInnerProduct.iip1_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.OrbitNormalization\nimport Mathlib.MeasureTheory.Function.Jacobian\nimport Mathlib.Analysis.Calculus.FDeriv.Linear\nimport Mathlib.Analysis.Calculus.FDeriv.Add\nimport Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar\nimport Mathlib.Analysis.Normed.Affine.AddTorsorBases\nimport Mathlib.LinearAlgebra.Matrix.ToLinearEquiv\n\nnamespace OIBridge\nnamespace InvariantInnerProduct\n\nopen MeasureTheory Set Matrix KInfFoundations OrbitGeneration OrbitNormalization\n\nvariable {n : ℕ}\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace InvariantInnerProduct",
 "open MeasureTheory Set Matrix KInfFoundations OrbitGeneration OrbitNormalization",
 "variable {n : ℕ}",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]",
 "end InvariantInnerProduct",
 "end OIBridge"
]''')

DECL = re.compile(r'^(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)',
                  re.M)
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


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def context_lines(text):
    return [m.group(0) for m in CTX.finditer(text)]


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def decl_texts(text):
    """theorem/lemma: signature up to the first ' :=' ; others: the declaration whole, up to the next doc comment,
    section marker, declaration, '#print', context line or 'end'."""
    out = {}
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
        if m.group(1) in ('theorem', 'lemma'):
            j = chunk.find(' :=')
            chunk = chunk[:j] if j != -1 else chunk
        out[m.group(2)] = chunk
    return out


def split_statement(stmt):
    """(binders, conclusion) at the first colon at bracket depth 0 after the name."""
    parts = stmt.split(None, 2)
    i = len(parts[0]) + 1 + len(parts[1])
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in '({[⦃':
            depth += 1
        elif c in ')}]⦄':
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return stmt[i:j], stmt[j + 1:]
    return stmt[i:], ''


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def header(text):
    return text[:text.index('-/')]


def norm(s):
    return ' '.join(s.split())


SPAN = 'invariant_inner_product_span'
VERDICT = 'iip1_core'
FORBIDDEN_NAME = re.compile(r'(llipsoid|ransitiv|ball3|finrank|SO3|otation|losureGen|rive|dim3|Dim3)')
FORBIDDEN_CONCL = ('BoundaryTransitive', 'ElementaryDrivability', 'ball3', 'finrank', 'driveWords')
FORBIDDEN_PROSE = re.compile(r'(is an ellipsoid|boundary[- ]transitive (on|under)|dimension (three|3) (is|follows)|'
                             r'generates SO)', re.I)
DISCLAIMER = 'No ellipsoid, no transitivity and no dimension is claimed.'
LOWDIM = ('momentMatrix_eq_zero_of_null', 'momentMatrix_eq_zero_of_subset', 'volume_segment2', 'segment2_moment')
PREFIX = 'OIBridge.InvariantInnerProduct.'


def semantic_checks(mod, texts, kinds, prints, tag):
    st = texts.get(SPAN, '')
    b, c = split_statement(st) if st else ('', '')
    check('S1', 'the span theorem is relative to the affine span' + tag,
          kinds.get(SPAN) == 'theorem' and 'LinearMap.ker L = ⊥' in b
          and 'x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)' in b
          and '(interior (bodyR L p0 Ω)).Nonempty' in c and 'invMatrix (bodyR L p0 Ω)' in c
          and not re.search(r'(invMatrix|momentMatrix|moment) Ω\b', c))
    bad = []
    for n, t in texts.items():
        if kinds.get(n) not in ('theorem', 'lemma') or n in (SPAN, VERDICT):
            continue
        bb, cc = split_statement(t)
        if '0 <' in cc and re.search(r'invMatrix|moment ', cc) and '(interior' not in bb:
            bad.append(n)
    vt = texts.get(VERDICT, '')
    check('S2', 'positivity only under a nonempty-interior hypothesis%s%s' % (tag, (' %s' % bad[:3]) if bad else ''),
          not bad and vt.count('IsCompact Ω → (interior Ω).Nonempty →') == 2)
    sub = texts.get('momentMatrix_eq_zero_of_subset', '')
    sb, sc = split_statement(sub) if sub else ('', '')
    check('S3', 'the ambient-nullity controls are kernel theorems with prints' + tag,
          all(kinds.get(n) == 'theorem' and PREFIX + n in prints for n in LOWDIM)
          and 's ≠ ⊤' in sb and 'Ω ⊆ (s : Set (Fin n → ℝ))' in sb and sc.strip() == 'momentMatrix Ω = 0'
          and 'momentMatrix segment2 = 0' in texts.get('segment2_moment', '')
          and 'momentMatrix segment2 = 0' in vt
          and not any(re.search(r'0 <[^∧→]*segment2', split_statement(t)[1])
                      for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')))
    hdr = header(mod)
    names = [n for _, n in decls(mod)]
    concl = [split_statement(t)[1] for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')]
    check('S4', 'no ellipsoid, transitivity, rotation, drive or dimension claim' + tag,
          not any(FORBIDDEN_NAME.search(n) for n in names)
          and not any(f in cc for cc in concl for f in FORBIDDEN_CONCL)
          and not FORBIDDEN_PROSE.search(hdr) and DISCLAIMER in norm(hdr))


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context line unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    texts = decl_texts(mod)
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s' % (tag, (' (changed: %s)' % ', '.join(bad[:4]))
                                                                        if bad else ''), not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in PRINTS))
    semantic_checks(mod, texts, dict((n, k) for k, n in decls(mod)), prints, tag)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_ok(d_text, e_text):
    try:
        d, e = json.loads(d_text), json.loads(e_text)
    except Exception:
        return False
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['name'].startswith(OG1_FAMILY_PREFIX)]
    if len(k) != 1:
        return False
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return e == want


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    module_checks(show(commit, MOD))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family', census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


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
    assert text.count(a) >= 1, a
    return text.replace(a, b, 1)


def append_decl(text, decl):
    i = text.rindex('\nend ')
    i = text.rindex('\nend ', 0, i)
    return text[:i] + '\n' + decl + '\n' + text[i:]


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    must_fail('N1', 'a removed declaration', replace_once(mod, '\n' + DECLS[-1][0] + ' ' + DECLS[-1][1],
                                                          '\n' + DECLS[-1][0] + ' ' + DECLS[-1][1] + 'X'))
    must_fail('N2', 'a changed binder context', replace_once(mod, CONTEXT[-3], CONTEXT[-3] + ' -- x\nopen Real'))
    must_fail('N3', 'a sorry', append_decl(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('S1', 'the span theorem strengthened to the ambient body',
              replace_once(mod, '(invMatrix (bodyR L p0 Ω))ᵀ = invMatrix (bodyR L p0 Ω)', '(invMatrix Ω)ᵀ = invMatrix Ω'))
    must_fail('S2', 'positivity without interior',
              append_decl(mod, 'theorem ambient_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) {u : Fin n → ℝ}\n'
                               '    (hu : u ≠ 0) : 0 < moment Ω u u := by\n  exact absurd hu hu'))
    must_fail('S2', 'the interior hypothesis dropped from invMatrix_pos',
              replace_once(mod, 'theorem invMatrix_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)',
                           'theorem invMatrix_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)'))
    must_fail('S3', 'the segment control removed', replace_once(mod, 'theorem segment2_moment', 'theorem segment2_moment2'))
    must_fail('S3', 'positivity claimed for the segment',
              append_decl(mod, 'theorem segment2_pos : 0 < moment segment2 (Pi.single 1 1) (Pi.single 1 1) := by\n'
                               '  exact absurd rfl rfl'))
    must_fail('S4', 'an ellipsoid name', append_decl(mod, 'theorem ellipsoid_of_moment : True := trivial'))
    must_fail('S4', 'a transitivity conclusion',
              append_decl(mod, 'theorem bt_of_moment (Ω : Set (Fin 3 → ℝ)) : BoundaryTransitive Ω ∅ := by\n'
                               '  exact absurd rfl rfl'))
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['name'].startswith(OG1_FAMILY_PREFIX)][0]
    good = dict(dd)
    good['families'] = dd['families'][:k + 1] + [CENSUS_FAMILY] + dd['families'][k + 1:]
    bad = json.loads(json.dumps(good))
    bad['families'][k + 1]['status'] = 'carried'
    check('M', 'census: the frozen family passes and a changed status fails',
          census_ok(d_cen, json.dumps(good)) and not census_ok(d_cen, json.dumps(bad)))


def main(argv):
    if argv == ['--self-test']:
        self_test()
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
