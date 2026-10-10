#!/usr/bin/env python3
"""controls.py -- round COMP-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition and structure is
                  the frozen text whole; the preamble and every context block is the frozen text, in order -- a proof
                  may change, a statement, definition, structure or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  neutral     no complex, tensor-product, Kronecker, matrix, Hilbert or inner-product token in the module; every
                  import is `OIBridge.CompletionAction` or a Mathlib module; the header states that local tomography is
                  a premise field, not a theorem
  S2  premise     no theorem concludes local tomography or the existence of a composite, other than the verdict's two
                  named-instance clauses; the field `lt` is assigned only in the two coordinate-model composites
  S3  carrier     `Composite` is a structure over an arbitrary carrier `V`; the minimal body is a convex hull of product
                  states and the maximal body a set-builder over the pairing; `prodState` and `prodEff` are assigned only
                  in the coordinate model and the padding control
  S4  scope       outside the model, instance and padding sections no statement names the coordinate model, `Fin 3`,
                  `ball3` or `simplex`; no gate, dimension-selector, transitivity, order, drive or availability token
  S5  operations  attachment, discard, the conditional state, readout and the two extremal bodies are definitions, not
                  structure fields; every law is a kernel theorem with its print
  S6  fields      the three structures carry exactly their frozen fields; `LocallyTomographic` is the body of `lt`
  S7  layering    every law other than the separation clause is stated over `ProductData` or `PreComposite`, never over
                  `Composite`
  S8  conditions  the marginal and conditional-state laws carry compactness and convexity of the factor body; the
                  readout test law takes a `SharpReadout` whose two effects sum to the unit functional
  S9  padding     the padding control is the frozen construction on `V × ℝ`; its two negative theorems and the three
                  instances' nonemptiness theorems are kernel theorems with prints
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.CompositionOrder`
  C   census      the census is D's with exactly the frozen family inserted after the ORD-1 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '00ee70a60cf59d421c0056619709459d704fae99'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-comp-1-composite-interface/'
PREREG = RDIR + 'preregistration.md'
MOD = 'verification/lean-mathlib/OIBridge/CompositeInterface.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '91567f53dbaefd847a5017d3562f536ea5ca47fa'
ANCHOR_IMPORT = 'import OIBridge.CompositionOrder\n'
NEW_IMPORT = 'import OIBridge.CompositeInterface\n'
PREV_FAMILY_PREFIX = 'iterated operation data and finite/infinite order on the com'
CENSUS_FAMILY = json.loads(r'''{
 "name": "the weak field-neutral composite interface: product states and effects, attachment, discard, joint reversible action, sharp readout and no-signalling on products (round COMP-1, reconstruction)",
 "modules": [
  "CompositeInterface"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round COMP-1, the weak field-neutral composite interface, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-comp-1-composite-interface/preregistration.md. The kernel layer defines the composite as a structure over an arbitrary real normed carrier V in three layers: ProductData (a bi-affine product-state map and a bilinear product-effect pairing of affine functionals of the two factor charts into affine functionals of V, with the evaluation law prodEff e f (prodState x y) = e x * f y), PreComposite (a convex body containing the product states on which every product of effects is an effect and the unit pairing is one) and Composite (the one further field lt, local tomography). Attachment, discard in chart coordinates, the conditional state and the sharp register readout are definitions; joint reversible action is OrbitGeneration.PreservesBody of the composite body. The laws are theorems of PreComposite: the marginal of a product is its factor and attach-then-discard is the identity (margA_prodState, margA_attach), pairing with the marginal is the unit pairing (eff_margA), the marginal and the conditional state of a composite state lie in a compact convex factor body (margA_mem, condA_mem), a sharp readout is a two-outcome test that reads the register on products and is certain after attaching the matching register state (readout_sum, isEffectOn_readout, readout_prodState, readout_attach), no signalling on products (condA_prodState), reversible actions compose (jointReversible_words), and the body lies between the minimal and the maximal body (minBody_subset, subset_maxBody) with the product pairing separating it (Composite.pairing_injective). The minimal and maximal bodies of any product data are pre-composites (minPre, maxPre); the instances bitComposite, ball3MinComposite and ball3MaxComposite live on the coordinate model Fin (d+1) → Fin (d+1) → ℝ, where local tomography is a theorem of that model. Local tomography is a premise field of the structure, not a theorem: no theorem derives lt from the other eight fields, and the padding control paddedPre, on V × ℝ, satisfies every other field and is not locally tomographic, so no Composite extends it (not_locallyTomographic_paddedPre, no_composite_over_paddedPre). Carried by no manuscript. No quantum tensor structure, no ℂ, no nonlocal-correlation inequality and no dimension is claimed; nothing here constructs a composite larger than the minimal body, sources local tomography, identifies the quantum composite, or types the stage-level product of two towers."
}''')
DECLS = json.loads(r'''[
 [
  "def",
  "unitEff"
 ],
 [
  "theorem",
  "unitEff_linear"
 ],
 [
  "def",
  "coord"
 ],
 [
  "theorem",
  "coord_linear"
 ],
 [
  "theorem",
  "isEffectOn_unitEff"
 ],
 [
  "theorem",
  "isEffectOn_unitEff_sub"
 ],
 [
  "def",
  "evalAddHom"
 ],
 [
  "theorem",
  "affine_sum_apply"
 ],
 [
  "theorem",
  "affine_eval"
 ],
 [
  "theorem",
  "affine_expand"
 ],
 [
  "def",
  "BoundedAffine"
 ],
 [
  "theorem",
  "boundedAffine_of_isCompact"
 ],
 [
  "theorem",
  "exists_effect_rescale"
 ],
 [
  "theorem",
  "exists_effect_neg"
 ],
 [
  "structure",
  "ProductData"
 ],
 [
  "structure",
  "PreComposite"
 ],
 [
  "def",
  "LocallyTomographic"
 ],
 [
  "structure",
  "Composite"
 ],
 [
  "def",
  "attach"
 ],
 [
  "def",
  "margA"
 ],
 [
  "def",
  "condA"
 ],
 [
  "def",
  "readout"
 ],
 [
  "def",
  "minBody"
 ],
 [
  "def",
  "maxBody"
 ],
 [
  "theorem",
  "attach_combo"
 ],
 [
  "theorem",
  "margA_combo"
 ],
 [
  "theorem",
  "prodEff_expand"
 ],
 [
  "theorem",
  "margA_prodState"
 ],
 [
  "theorem",
  "margA_attach"
 ],
 [
  "theorem",
  "readout_prodState"
 ],
 [
  "theorem",
  "eff_condA"
 ],
 [
  "theorem",
  "condA_prodState"
 ],
 [
  "theorem",
  "prodEff_eq_of_eff_eq"
 ],
 [
  "theorem",
  "nonempty_of"
 ],
 [
  "theorem",
  "eff_margA"
 ],
 [
  "theorem",
  "margA_mem"
 ],
 [
  "structure",
  "SharpReadout"
 ],
 [
  "theorem",
  "sum_eq_unitEff_of_affineSpan"
 ],
 [
  "theorem",
  "readout_sum"
 ],
 [
  "theorem",
  "isEffectOn_readout"
 ],
 [
  "theorem",
  "readout_attach"
 ],
 [
  "theorem",
  "condA_mem"
 ],
 [
  "abbrev",
  "JointReversible"
 ],
 [
  "theorem",
  "jointReversible_words"
 ],
 [
  "theorem",
  "isEffectOn_readout_seedTransport"
 ],
 [
  "theorem",
  "minBody_subset"
 ],
 [
  "theorem",
  "subset_maxBody"
 ],
 [
  "theorem",
  "pairing_injective"
 ],
 [
  "theorem",
  "isEffectOn_minBody"
 ],
 [
  "theorem",
  "unit_eq_one_minBody"
 ],
 [
  "def",
  "minPre"
 ],
 [
  "theorem",
  "maxBody_convex"
 ],
 [
  "theorem",
  "isEffectOn_maxBody"
 ],
 [
  "def",
  "maxPre"
 ],
 [
  "abbrev",
  "Carrier"
 ],
 [
  "def",
  "hom"
 ],
 [
  "theorem",
  "hom_zero"
 ],
 [
  "theorem",
  "hom_succ"
 ],
 [
  "theorem",
  "hom_combo"
 ],
 [
  "def",
  "coeff"
 ],
 [
  "theorem",
  "coeff_zero"
 ],
 [
  "theorem",
  "coeff_succ"
 ],
 [
  "theorem",
  "sum_coeff_hom"
 ],
 [
  "theorem",
  "coeff_add"
 ],
 [
  "theorem",
  "coeff_smul"
 ],
 [
  "def",
  "pState"
 ],
 [
  "def",
  "pEffLin"
 ],
 [
  "def",
  "pEff"
 ],
 [
  "theorem",
  "pEff_apply"
 ],
 [
  "theorem",
  "pEff_pState"
 ],
 [
  "theorem",
  "pEff_add_left"
 ],
 [
  "theorem",
  "pEff_smul_left"
 ],
 [
  "theorem",
  "pEff_add_right"
 ],
 [
  "theorem",
  "pEff_smul_right"
 ],
 [
  "def",
  "modelData"
 ],
 [
  "theorem",
  "modelData_prodEff"
 ],
 [
  "def",
  "basisEff"
 ],
 [
  "theorem",
  "coeff_basisEff"
 ],
 [
  "theorem",
  "pEff_basisEff"
 ],
 [
  "theorem",
  "modelData_ext"
 ],
 [
  "theorem",
  "of"
 ],
 [
  "def",
  "minComposite"
 ],
 [
  "def",
  "maxComposite"
 ],
 [
  "theorem",
  "simplex_isCompact"
 ],
 [
  "theorem",
  "zero_mem_ball3"
 ],
 [
  "def",
  "bitComposite"
 ],
 [
  "def",
  "ball3MinComposite"
 ],
 [
  "def",
  "ball3MaxComposite"
 ],
 [
  "theorem",
  "vec10_mem_simplex"
 ],
 [
  "theorem",
  "bitComposite_nonempty"
 ],
 [
  "theorem",
  "ball3MinComposite_nonempty"
 ],
 [
  "theorem",
  "ball3Min_subset_ball3Max"
 ],
 [
  "def",
  "padEff"
 ],
 [
  "theorem",
  "padEff_apply"
 ],
 [
  "def",
  "paddedPre"
 ],
 [
  "theorem",
  "not_locallyTomographic_paddedPre"
 ],
 [
  "theorem",
  "no_composite_over_paddedPre"
 ],
 [
  "def",
  "paddedBall3"
 ],
 [
  "theorem",
  "not_locallyTomographic_paddedBall3"
 ],
 [
  "theorem",
  "no_composite_over_paddedBall3"
 ],
 [
  "theorem",
  "comp1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "unitEff": "def unitEff (d : ℕ) : (Fin d → ℝ) →ᵃ[ℝ] ℝ := AffineMap.const ℝ (Fin d → ℝ) (1 : ℝ)\n\n@[simp] theorem unitEff_apply (x : Fin d → ℝ) : unitEff d x = 1 := rfl",
 "unitEff_linear": "theorem unitEff_linear : (unitEff d).linear = 0",
 "coord": "def coord (i : Fin d) : (Fin d → ℝ) →ᵃ[ℝ] ℝ :=\n  (LinearMap.proj i : (Fin d → ℝ) →ₗ[ℝ] ℝ).toAffineMap\n\n@[simp] theorem coord_apply (i : Fin d) (x : Fin d → ℝ) : coord i x = x i := rfl",
 "coord_linear": "theorem coord_linear (i : Fin d) : (coord i).linear = LinearMap.proj i",
 "isEffectOn_unitEff": "theorem isEffectOn_unitEff (Ω : Set (Fin d → ℝ)) : IsEffectOn Ω (unitEff d)",
 "isEffectOn_unitEff_sub": "theorem isEffectOn_unitEff_sub {Ω : Set (Fin d → ℝ)} {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ}\n    (he : IsEffectOn Ω e) : IsEffectOn Ω (unitEff d - e)",
 "evalAddHom": "def evalAddHom {P : Type} [AddCommGroup P] [Module ℝ P] (x : P) : (P →ᵃ[ℝ] ℝ) →+ ℝ where\n  toFun e := e x\n  map_zero' := by\n    show (0 : P →ᵃ[ℝ] ℝ) x = 0\n    rw [AffineMap.coe_zero, Pi.zero_apply]\n  map_add' e e' := by\n    show (e + e') x = e x + e' x\n    rw [AffineMap.coe_add, Pi.add_apply]",
 "affine_sum_apply": "theorem affine_sum_apply {P : Type} [AddCommGroup P] [Module ℝ P] {ι : Type} (s : Finset ι)\n    (g : ι → P →ᵃ[ℝ] ℝ) (x : P) : (∑ i ∈ s, g i) x = ∑ i ∈ s, g i x",
 "affine_eval": "theorem affine_eval (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :\n    e x = e 0 + ∑ i, e.linear (fun j => if i = j then 1 else 0) * x i",
 "affine_expand": "theorem affine_expand (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) :\n    e = e 0 • unitEff d + ∑ i, e.linear (fun j => if i = j then 1 else 0) • coord i",
 "BoundedAffine": "def BoundedAffine (Ω : Set (Fin d → ℝ)) : Prop :=\n  ∀ e : (Fin d → ℝ) →ᵃ[ℝ] ℝ, ∃ B : ℝ, ∀ x ∈ Ω, |e x| ≤ B",
 "boundedAffine_of_isCompact": "theorem boundedAffine_of_isCompact {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) : BoundedAffine Ω",
 "exists_effect_rescale": "theorem exists_effect_rescale {Ω : Set (Fin d → ℝ)} (hb : BoundedAffine Ω)\n    (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) :\n    ∃ (e' : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (a c : ℝ), IsEffectOn Ω e' ∧ e = a • e' + c • unitEff d",
 "exists_effect_neg": "theorem exists_effect_neg {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω)\n    {z : Fin d → ℝ} (hz : z ∉ Ω) :\n    ∃ g : (Fin d → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn Ω g ∧ g z < 0",
 "ProductData": "structure ProductData (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] where\n  prodState : (Fin dA → ℝ) → (Fin dB → ℝ) → V\n  prodState_combo_left : ∀ (x x' : Fin dA → ℝ) (y : Fin dB → ℝ) (a b : ℝ), a + b = 1 →\n    prodState (a • x + b • x') y = a • prodState x y + b • prodState x' y\n  prodState_combo_right : ∀ (x : Fin dA → ℝ) (y y' : Fin dB → ℝ) (a b : ℝ), a + b = 1 →\n    prodState x (a • y + b • y') = a • prodState x y + b • prodState x y'\n  prodEff : ((Fin dA → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] ((Fin dB → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] (V →ᵃ[ℝ] ℝ)\n  prodEff_apply : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (x : Fin dA → ℝ)\n    (y : Fin dB → ℝ), prodEff e f (prodState x y) = e x * f y",
 "PreComposite": "structure PreComposite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n    [NormedAddCommGroup V] [NormedSpace ℝ V] extends ProductData dA dB V where\n  Ω : Set V\n  convex : Convex ℝ Ω\n  prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω\n  prodEff_effect : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),\n    IsEffectOn ΩA e → IsEffectOn ΩB f → IsEffectOn Ω (prodEff e f)\n  prodEff_unit : ∀ ω ∈ Ω, prodEff (unitEff dA) (unitEff dB) ω = 1",
 "LocallyTomographic": "def LocallyTomographic {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type}\n    [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V) : Prop :=\n  ∀ ω ∈ P.Ω, ∀ ω' ∈ P.Ω, (∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),\n    IsEffectOn ΩA e → IsEffectOn ΩB f → P.prodEff e f ω = P.prodEff e f ω') → ω = ω'",
 "Composite": "structure Composite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n    [NormedAddCommGroup V] [NormedSpace ℝ V] extends PreComposite ΩA ΩB V where\n  lt : ∀ ω ∈ Ω, ∀ ω' ∈ Ω, (∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),\n    IsEffectOn ΩA e → IsEffectOn ΩB f → prodEff e f ω = prodEff e f ω') → ω = ω'\n\nnamespace ProductData",
 "attach": "def attach (r₀ : Fin dB → ℝ) (x : Fin dA → ℝ) : V := D.prodState x r₀",
 "margA": "def margA (ω : V) : Fin dA → ℝ := fun i => D.prodEff (coord i) (unitEff dB) ω",
 "condA": "def condA (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : V) : Fin dA → ℝ :=\n  fun i => D.prodEff (coord i) f ω / D.prodEff (unitEff dA) f ω",
 "readout": "def readout (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (k : Fin 2) : V →ᵃ[ℝ] ℝ :=\n  D.prodEff (unitEff dA) (f k)",
 "minBody": "def minBody (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) : Set V :=\n  convexHull ℝ (Set.image2 D.prodState ΩA ΩB)",
 "maxBody": "def maxBody (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) : Set V :=\n  {ω | D.prodEff (unitEff dA) (unitEff dB) ω = 1 ∧\n    ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),\n      IsEffectOn ΩA e → IsEffectOn ΩB f → 0 ≤ D.prodEff e f ω}",
 "attach_combo": "theorem attach_combo (r₀ : Fin dB → ℝ) (x x' : Fin dA → ℝ) {a b : ℝ} (hab : a + b = 1) :\n    D.attach r₀ (a • x + b • x') = a • D.attach r₀ x + b • D.attach r₀ x'",
 "margA_combo": "theorem margA_combo (ω ω' : V) {a b : ℝ} (hab : a + b = 1) :\n    D.margA (a • ω + b • ω') = a • D.margA ω + b • D.margA ω'",
 "prodEff_expand": "theorem prodEff_expand (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : V) :\n    D.prodEff e f ω = e 0 * D.prodEff (unitEff dA) f ω +\n      ∑ i, e.linear (fun j => if i = j then 1 else 0) * D.prodEff (coord i) f ω",
 "margA_prodState": "theorem margA_prodState (x : Fin dA → ℝ) (y : Fin dB → ℝ) : D.margA (D.prodState x y) = x",
 "margA_attach": "theorem margA_attach (r₀ : Fin dB → ℝ) (x : Fin dA → ℝ) : D.margA (D.attach r₀ x) = x",
 "readout_prodState": "theorem readout_prodState (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (k : Fin 2) (x : Fin dA → ℝ)\n    (y : Fin dB → ℝ) : D.readout f k (D.prodState x y) = f k y",
 "eff_condA": "theorem eff_condA (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) {ω : V} (hf : D.prodEff (unitEff dA) f ω ≠ 0)\n    (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) :\n    e (D.condA f ω) = D.prodEff e f ω / D.prodEff (unitEff dA) f ω",
 "condA_prodState": "theorem condA_prodState (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) {y : Fin dB → ℝ} (hy : f y ≠ 0)\n    (x : Fin dA → ℝ) : D.condA f (D.prodState x y) = x",
 "prodEff_eq_of_eff_eq": "theorem prodEff_eq_of_eff_eq {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)}\n    (hA : BoundedAffine ΩA) (hB : BoundedAffine ΩB) {ω ω' : V}\n    (H : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),\n      IsEffectOn ΩA e → IsEffectOn ΩB f → D.prodEff e f ω = D.prodEff e f ω')\n    (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :\n    D.prodEff e f ω = D.prodEff e f ω'",
 "nonempty_of": "theorem nonempty_of (hA : ΩA.Nonempty) (hB : ΩB.Nonempty) : P.Ω.Nonempty",
 "eff_margA": "theorem eff_margA {ω : V} (hω : ω ∈ P.Ω) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) :\n    e (P.margA ω) = P.prodEff e (unitEff dB) ω",
 "margA_mem": "theorem margA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) :\n    P.margA ω ∈ ΩA",
 "SharpReadout": "structure SharpReadout (ΩB : Set (Fin dB → ℝ)) where\n  y : Fin 2 → (Fin dB → ℝ)\n  f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ\n  pd : PerfectlyDistinguishable ΩB y f\n  sum_eq : f 0 + f 1 = unitEff dB",
 "sum_eq_unitEff_of_affineSpan": "theorem sum_eq_unitEff_of_affineSpan (hspan : affineSpan ℝ ΩB = ⊤) {y : Fin 2 → (Fin dB → ℝ)}\n    {f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ} (hpd : PerfectlyDistinguishable ΩB y f) :\n    f 0 + f 1 = unitEff dB",
 "readout_sum": "theorem readout_sum (R : SharpReadout ΩB) {ω : V} (hω : ω ∈ P.Ω) :\n    P.readout R.f 0 ω + P.readout R.f 1 ω = 1",
 "isEffectOn_readout": "theorem isEffectOn_readout (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (hf : ∀ k, IsEffectOn ΩB (f k))\n    (k : Fin 2) : IsEffectOn P.Ω (P.readout f k)",
 "readout_attach": "theorem readout_attach (R : SharpReadout ΩB) (k : Fin 2) (x : Fin dA → ℝ) :\n    P.readout R.f k (P.attach (R.y k) x) = 1",
 "condA_mem": "theorem condA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ}\n    (hf : IsEffectOn ΩB f) {ω : V} (hω : ω ∈ P.Ω) (hne : P.prodEff (unitEff dA) f ω ≠ 0) :\n    P.condA f ω ∈ ΩA",
 "JointReversible": "abbrev JointReversible (G : Set (V ≃ᵃ[ℝ] V)) : Prop := PreservesBody P.Ω G",
 "jointReversible_words": "theorem jointReversible_words {G : Set (V ≃ᵃ[ℝ] V)} (hG : P.JointReversible G) :\n    P.JointReversible (words G)",
 "isEffectOn_readout_seedTransport": "theorem isEffectOn_readout_seedTransport {G : Set (V ≃ᵃ[ℝ] V)} (hG : P.JointReversible G)\n    {g : V ≃ᵃ[ℝ] V} (hg : g ∈ G) (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ)\n    (hf : ∀ k, IsEffectOn ΩB (f k)) (k : Fin 2) :\n    IsEffectOn P.Ω (seedTransport (P.readout f k) g)",
 "minBody_subset": "theorem minBody_subset : P.toProductData.minBody ΩA ΩB ⊆ P.Ω",
 "subset_maxBody": "theorem subset_maxBody : P.Ω ⊆ P.toProductData.maxBody ΩA ΩB",
 "pairing_injective": "theorem pairing_injective :\n    Function.Injective fun ω : C.Ω => fun (e : {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩA e})\n      (f : {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩB f}) => C.prodEff e.1 f.1 ω.1",
 "isEffectOn_minBody": "theorem isEffectOn_minBody {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ} {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ}\n    (he : IsEffectOn ΩA e) (hf : IsEffectOn ΩB f) : IsEffectOn (D.minBody ΩA ΩB) (D.prodEff e f)",
 "unit_eq_one_minBody": "theorem unit_eq_one_minBody {ω : V} (hω : ω ∈ D.minBody ΩA ΩB) :\n    D.prodEff (unitEff dA) (unitEff dB) ω = 1",
 "minPre": "def minPre : PreComposite ΩA ΩB V where\n  toProductData := D\n  Ω := D.minBody ΩA ΩB\n  convex := convex_convexHull ℝ _\n  prod_mem _ hx _ hy := subset_convexHull ℝ _ (Set.mem_image2_of_mem hx hy)\n  prodEff_effect _ _ he hf := D.isEffectOn_minBody ΩA ΩB he hf\n  prodEff_unit _ hω := D.unit_eq_one_minBody ΩA ΩB hω",
 "maxBody_convex": "theorem maxBody_convex : Convex ℝ (D.maxBody ΩA ΩB)",
 "isEffectOn_maxBody": "theorem isEffectOn_maxBody {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ} {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ}\n    (he : IsEffectOn ΩA e) (hf : IsEffectOn ΩB f) : IsEffectOn (D.maxBody ΩA ΩB) (D.prodEff e f)",
 "maxPre": "def maxPre : PreComposite ΩA ΩB V where\n  toProductData := D\n  Ω := D.maxBody ΩA ΩB\n  convex := D.maxBody_convex ΩA ΩB\n  prod_mem x hx y hy :=\n    ⟨by rw [D.prodEff_apply, unitEff_apply, unitEff_apply, mul_one],\n      fun e f he hf => by rw [D.prodEff_apply]; exact mul_nonneg (he x hx).1 (hf y hy).1⟩\n  prodEff_effect _ _ he hf := D.isEffectOn_maxBody ΩA ΩB he hf\n  prodEff_unit _ hω := hω.1",
 "Carrier": "abbrev Carrier (dA dB : ℕ) := Fin (dA + 1) → Fin (dB + 1) → ℝ",
 "hom": "def hom (x : Fin d → ℝ) : Fin (d + 1) → ℝ := Fin.cons 1 x",
 "hom_zero": "theorem hom_zero (x : Fin d → ℝ) : hom x 0 = 1",
 "hom_succ": "theorem hom_succ (x : Fin d → ℝ) (i : Fin d) : hom x i.succ = x i",
 "hom_combo": "theorem hom_combo {x x' : Fin d → ℝ} {a b : ℝ} (hab : a + b = 1) :\n    hom (a • x + b • x') = a • hom x + b • hom x'",
 "coeff": "def coeff (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : Fin (d + 1) → ℝ :=\n  Fin.cons (e 0) fun i => e.linear (fun j => if i = j then 1 else 0)",
 "coeff_zero": "theorem coeff_zero (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : coeff e 0 = e 0",
 "coeff_succ": "theorem coeff_succ (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (i : Fin d) :\n    coeff e i.succ = e.linear (fun j => if i = j then 1 else 0)",
 "sum_coeff_hom": "theorem sum_coeff_hom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :\n    ∑ μ, coeff e μ * hom x μ = e x",
 "coeff_add": "theorem coeff_add (e e' : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : coeff (e + e') = coeff e + coeff e'",
 "coeff_smul": "theorem coeff_smul (a : ℝ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : coeff (a • e) = a • coeff e",
 "pState": "def pState (x : Fin dA → ℝ) (y : Fin dB → ℝ) : Carrier dA dB := fun μ ν => hom x μ * hom y ν",
 "pEffLin": "def pEffLin (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) : Carrier dA dB →ₗ[ℝ] ℝ where\n  toFun ω := ∑ μ, ∑ ν, coeff e μ * coeff f ν * ω μ ν\n  map_add' ω ω' := by\n    simp only [Pi.add_apply, mul_add, Finset.sum_add_distrib]\n  map_smul' a ω := by\n    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, Finset.mul_sum]\n    refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_\n    ring",
 "pEff": "def pEff (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) : Carrier dA dB →ᵃ[ℝ] ℝ :=\n  (pEffLin e f).toAffineMap",
 "pEff_apply": "theorem pEff_apply (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : Carrier dA dB) :\n    pEff e f ω = ∑ μ, ∑ ν, coeff e μ * coeff f ν * ω μ ν",
 "pEff_pState": "theorem pEff_pState (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (x : Fin dA → ℝ)\n    (y : Fin dB → ℝ) : pEff e f (pState x y) = e x * f y",
 "pEff_add_left": "theorem pEff_add_left (e e' : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :\n    pEff (e + e') f = pEff e f + pEff e' f",
 "pEff_smul_left": "theorem pEff_smul_left (a : ℝ) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :\n    pEff (a • e) f = a • pEff e f",
 "pEff_add_right": "theorem pEff_add_right (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f f' : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :\n    pEff e (f + f') = pEff e f + pEff e f'",
 "pEff_smul_right": "theorem pEff_smul_right (a : ℝ) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :\n    pEff e (a • f) = a • pEff e f",
 "modelData": "def modelData (dA dB : ℕ) : ProductData dA dB (Carrier dA dB) where\n  prodState := pState\n  prodState_combo_left x x' y a b hab := by\n    funext μ ν\n    simp only [pState, Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_combo hab]\n    ring\n  prodState_combo_right x y y' a b hab := by\n    funext μ ν\n    simp only [pState, Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_combo hab]\n    ring\n  prodEff := LinearMap.mk₂ ℝ pEff pEff_add_left pEff_smul_left pEff_add_right pEff_smul_right\n  prodEff_apply e f x y := by\n    rw [LinearMap.mk₂_apply]\n    exact pEff_pState e f x y",
 "modelData_prodEff": "theorem modelData_prodEff (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :\n    (modelData dA dB).prodEff e f = pEff e f",
 "basisEff": "def basisEff (μ : Fin (d + 1)) : (Fin d → ℝ) →ᵃ[ℝ] ℝ :=\n  (Fin.cons (unitEff d) coord : Fin (d + 1) → (Fin d → ℝ) →ᵃ[ℝ] ℝ) μ",
 "coeff_basisEff": "theorem coeff_basisEff (μ ν : Fin (d + 1)) : coeff (basisEff μ) ν = if μ = ν then 1 else 0",
 "pEff_basisEff": "theorem pEff_basisEff (μ : Fin (dA + 1)) (ν : Fin (dB + 1)) (ω : Carrier dA dB) :\n    pEff (basisEff μ) (basisEff ν) ω = ω μ ν",
 "modelData_ext": "theorem modelData_ext {ω ω' : Carrier dA dB}\n    (h : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),\n      (modelData dA dB).prodEff e f ω = (modelData dA dB).prodEff e f ω') : ω = ω'",
 "of": "theorem of this model: agreement on effect pairs extends to all pairs, which separate points. -/",
 "minComposite": "def minComposite {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} (hA : IsCompact ΩA)\n    (hB : IsCompact ΩB) : Composite ΩA ΩB (Carrier dA dB) where\n  toPreComposite := (modelData dA dB).minPre ΩA ΩB\n  lt _ _ _ _ H := modelData_ext fun e f =>\n    (modelData dA dB).prodEff_eq_of_eff_eq (boundedAffine_of_isCompact hA)\n      (boundedAffine_of_isCompact hB) H e f",
 "maxComposite": "def maxComposite {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} (hA : IsCompact ΩA)\n    (hB : IsCompact ΩB) : Composite ΩA ΩB (Carrier dA dB) where\n  toPreComposite := (modelData dA dB).maxPre ΩA ΩB\n  lt _ _ _ _ H := modelData_ext fun e f =>\n    (modelData dA dB).prodEff_eq_of_eff_eq (boundedAffine_of_isCompact hA)\n      (boundedAffine_of_isCompact hB) H e f",
 "simplex_isCompact": "theorem simplex_isCompact (N : ℕ) : IsCompact (simplex N)",
 "zero_mem_ball3": "theorem zero_mem_ball3 : (0 : Fin 3 → ℝ) ∈ ball3",
 "bitComposite": "def bitComposite : Composite (simplex 2) (simplex 2) (Carrier 2 2) :=\n  minComposite (simplex_isCompact 2) (simplex_isCompact 2)",
 "ball3MinComposite": "def ball3MinComposite : Composite ball3 ball3 (Carrier 3 3) :=\n  minComposite ball3_isCompact ball3_isCompact",
 "ball3MaxComposite": "def ball3MaxComposite : Composite ball3 ball3 (Carrier 3 3) :=\n  maxComposite ball3_isCompact ball3_isCompact",
 "vec10_mem_simplex": "theorem vec10_mem_simplex : (![1, 0] : Fin 2 → ℝ) ∈ simplex 2",
 "bitComposite_nonempty": "theorem bitComposite_nonempty : bitComposite.Ω.Nonempty",
 "ball3MinComposite_nonempty": "theorem ball3MinComposite_nonempty : ball3MinComposite.Ω.Nonempty",
 "ball3Min_subset_ball3Max": "theorem ball3Min_subset_ball3Max : ball3MinComposite.Ω ⊆ ball3MaxComposite.Ω",
 "padEff": "def padEff (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) : V × ℝ →ᵃ[ℝ] ℝ :=\n  (P.prodEff e f).comp (AffineMap.fst : V × ℝ →ᵃ[ℝ] V)",
 "padEff_apply": "theorem padEff_apply (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (p : V × ℝ) :\n    padEff P e f p = P.prodEff e f p.1",
 "paddedPre": "def paddedPre : PreComposite ΩA ΩB (V × ℝ) where\n  prodState x y := (P.prodState x y, 0)\n  prodState_combo_left x x' y a b hab := by\n    rw [P.prodState_combo_left x x' y a b hab]\n    exact Prod.ext (by simp) (by simp)\n  prodState_combo_right x y y' a b hab := by\n    rw [P.prodState_combo_right x y y' a b hab]\n    exact Prod.ext (by simp) (by simp)\n  prodEff := LinearMap.mk₂ ℝ (padEff P)\n    (fun e e' f => by\n      refine AffineMap.ext fun p => ?_\n      simp only [padEff_apply, map_add, LinearMap.add_apply, AffineMap.coe_add, Pi.add_apply])\n    (fun a e f => by\n      refine AffineMap.ext fun p => ?_\n      simp only [padEff_apply, LinearMap.map_smul, LinearMap.smul_apply, AffineMap.coe_smul,\n        Pi.smul_apply])\n    (fun e f f' => by\n      refine AffineMap.ext fun p => ?_\n      simp only [padEff_apply, map_add, AffineMap.coe_add, Pi.add_apply])\n    (fun a e f => by\n      refine AffineMap.ext fun p => ?_\n      simp only [padEff_apply, LinearMap.map_smul, AffineMap.coe_smul, Pi.smul_apply])\n  prodEff_apply e f x y := by\n    rw [LinearMap.mk₂_apply, padEff_apply]\n    exact P.prodEff_apply e f x y\n  Ω := P.Ω ×ˢ Set.Icc (0 : ℝ) 1\n  convex := P.convex.prod (convex_Icc 0 1)\n  prod_mem x hx y hy := ⟨P.prod_mem x hx y hy, le_rfl, zero_le_one⟩\n  prodEff_effect e f he hf p hp := by\n    rw [LinearMap.mk₂_apply, padEff_apply]\n    exact P.prodEff_effect e f he hf p.1 hp.1\n  prodEff_unit p hp := by\n    rw [LinearMap.mk₂_apply, padEff_apply]\n    exact P.prodEff_unit p.1 hp.1",
 "not_locallyTomographic_paddedPre": "theorem not_locallyTomographic_paddedPre (hne : P.Ω.Nonempty) :\n    ¬ LocallyTomographic (paddedPre P)",
 "no_composite_over_paddedPre": "theorem no_composite_over_paddedPre (hne : P.Ω.Nonempty) :\n    ¬ ∃ C : Composite ΩA ΩB (V × ℝ), C.toPreComposite = paddedPre P",
 "paddedBall3": "def paddedBall3 : PreComposite ball3 ball3 (Carrier 3 3 × ℝ) :=\n  paddedPre ball3MinComposite.toPreComposite",
 "not_locallyTomographic_paddedBall3": "theorem not_locallyTomographic_paddedBall3 : ¬ LocallyTomographic paddedBall3",
 "no_composite_over_paddedBall3": "theorem no_composite_over_paddedBall3 :\n    ¬ ∃ C : Composite ball3 ball3 (Carrier 3 3 × ℝ), C.toPreComposite = paddedBall3",
 "comp1_core": "theorem comp1_core :\n    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)\n      (x : Fin dA → ℝ) (y : Fin dB → ℝ), D.margA (D.prodState x y) = x) ∧\n    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)\n      (r₀ : Fin dB → ℝ) (x : Fin dA → ℝ), D.margA (D.attach r₀ x) = x) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V), ∀ ω ∈ P.Ω,\n      ∀ e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ, e (P.margA ω) = P.prodEff e (unitEff dB) ω) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V),\n      IsCompact ΩA → Convex ℝ ΩA → ∀ ω ∈ P.Ω, P.margA ω ∈ ΩA) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)\n      (R : PreComposite.SharpReadout ΩB), ∀ ω ∈ P.Ω,\n      P.readout R.f 0 ω + P.readout R.f 1 ω = 1 ∧ IsEffectOn P.Ω (P.readout R.f 0) ∧\n        IsEffectOn P.Ω (P.readout R.f 1)) ∧\n    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)\n      (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (k : Fin 2) (x : Fin dA → ℝ) (y : Fin dB → ℝ),\n      D.readout f k (D.prodState x y) = f k y) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)\n      (R : PreComposite.SharpReadout ΩB) (k : Fin 2) (x : Fin dA → ℝ),\n      P.readout R.f k (P.attach (R.y k) x) = 1) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V),\n      IsCompact ΩA → Convex ℝ ΩA → ∀ f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn ΩB f →\n      ∀ ω ∈ P.Ω, P.prodEff (unitEff dA) f ω ≠ 0 → P.condA f ω ∈ ΩA) ∧\n    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)\n      (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (y : Fin dB → ℝ), f y ≠ 0 →\n      ∀ x : Fin dA → ℝ, D.condA f (D.prodState x y) = x) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)\n      (G : Set (V ≃ᵃ[ℝ] V)), P.JointReversible G → P.JointReversible (words G)) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V),\n      P.toProductData.minBody ΩA ΩB ⊆ P.Ω ∧ P.Ω ⊆ P.toProductData.maxBody ΩA ΩB) ∧\n    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n      [NormedAddCommGroup V] [NormedSpace ℝ V] (C : Composite ΩA ΩB V),\n      Function.Injective fun ω : C.Ω =>\n        fun (e : {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩA e})\n          (f : {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩB f}) => C.prodEff e.1 f.1 ω.1) ∧\n    Nonempty (Composite (simplex 2) (simplex 2) (Carrier 2 2)) ∧\n    Nonempty (Composite ball3 ball3 (Carrier 3 3)) ∧\n    ball3MinComposite.Ω ⊆ ball3MaxComposite.Ω ∧\n    ¬ LocallyTomographic paddedBall3 ∧\n    ¬ ∃ C : Composite ball3 ball3 (Carrier 3 3 × ℝ), C.toPreComposite = paddedBall3"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.CompositeInterface.isEffectOn_unitEff",
 "OIBridge.CompositeInterface.isEffectOn_unitEff_sub",
 "OIBridge.CompositeInterface.affine_sum_apply",
 "OIBridge.CompositeInterface.affine_eval",
 "OIBridge.CompositeInterface.affine_expand",
 "OIBridge.CompositeInterface.boundedAffine_of_isCompact",
 "OIBridge.CompositeInterface.exists_effect_rescale",
 "OIBridge.CompositeInterface.exists_effect_neg",
 "OIBridge.CompositeInterface.ProductData.attach_combo",
 "OIBridge.CompositeInterface.ProductData.margA_combo",
 "OIBridge.CompositeInterface.ProductData.prodEff_expand",
 "OIBridge.CompositeInterface.ProductData.margA_prodState",
 "OIBridge.CompositeInterface.ProductData.margA_attach",
 "OIBridge.CompositeInterface.ProductData.readout_prodState",
 "OIBridge.CompositeInterface.ProductData.eff_condA",
 "OIBridge.CompositeInterface.ProductData.condA_prodState",
 "OIBridge.CompositeInterface.ProductData.prodEff_eq_of_eff_eq",
 "OIBridge.CompositeInterface.PreComposite.nonempty_of",
 "OIBridge.CompositeInterface.PreComposite.eff_margA",
 "OIBridge.CompositeInterface.PreComposite.margA_mem",
 "OIBridge.CompositeInterface.PreComposite.sum_eq_unitEff_of_affineSpan",
 "OIBridge.CompositeInterface.PreComposite.readout_sum",
 "OIBridge.CompositeInterface.PreComposite.isEffectOn_readout",
 "OIBridge.CompositeInterface.PreComposite.readout_attach",
 "OIBridge.CompositeInterface.PreComposite.condA_mem",
 "OIBridge.CompositeInterface.PreComposite.jointReversible_words",
 "OIBridge.CompositeInterface.PreComposite.isEffectOn_readout_seedTransport",
 "OIBridge.CompositeInterface.PreComposite.minBody_subset",
 "OIBridge.CompositeInterface.PreComposite.subset_maxBody",
 "OIBridge.CompositeInterface.Composite.pairing_injective",
 "OIBridge.CompositeInterface.ProductData.isEffectOn_minBody",
 "OIBridge.CompositeInterface.ProductData.unit_eq_one_minBody",
 "OIBridge.CompositeInterface.ProductData.maxBody_convex",
 "OIBridge.CompositeInterface.ProductData.isEffectOn_maxBody",
 "OIBridge.CompositeInterface.Model.hom_zero",
 "OIBridge.CompositeInterface.Model.hom_succ",
 "OIBridge.CompositeInterface.Model.hom_combo",
 "OIBridge.CompositeInterface.Model.coeff_zero",
 "OIBridge.CompositeInterface.Model.coeff_succ",
 "OIBridge.CompositeInterface.Model.sum_coeff_hom",
 "OIBridge.CompositeInterface.Model.coeff_add",
 "OIBridge.CompositeInterface.Model.coeff_smul",
 "OIBridge.CompositeInterface.Model.pEff_apply",
 "OIBridge.CompositeInterface.Model.pEff_pState",
 "OIBridge.CompositeInterface.Model.pEff_add_left",
 "OIBridge.CompositeInterface.Model.pEff_smul_left",
 "OIBridge.CompositeInterface.Model.pEff_add_right",
 "OIBridge.CompositeInterface.Model.pEff_smul_right",
 "OIBridge.CompositeInterface.Model.modelData_prodEff",
 "OIBridge.CompositeInterface.Model.coeff_basisEff",
 "OIBridge.CompositeInterface.Model.pEff_basisEff",
 "OIBridge.CompositeInterface.Model.modelData_ext",
 "OIBridge.CompositeInterface.simplex_isCompact",
 "OIBridge.CompositeInterface.zero_mem_ball3",
 "OIBridge.CompositeInterface.vec10_mem_simplex",
 "OIBridge.CompositeInterface.bitComposite_nonempty",
 "OIBridge.CompositeInterface.ball3MinComposite_nonempty",
 "OIBridge.CompositeInterface.ball3Min_subset_ball3Max",
 "OIBridge.CompositeInterface.padEff_apply",
 "OIBridge.CompositeInterface.not_locallyTomographic_paddedPre",
 "OIBridge.CompositeInterface.no_composite_over_paddedPre",
 "OIBridge.CompositeInterface.not_locallyTomographic_paddedBall3",
 "OIBridge.CompositeInterface.no_composite_over_paddedBall3",
 "OIBridge.CompositeInterface.comp1_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.CompletionAction\nimport Mathlib.Analysis.LocallyConvex.Separation\nimport Mathlib.Analysis.Normed.Module.FiniteDimension\n\nnamespace OIBridge\nnamespace CompositeInterface\n\nnoncomputable section\n\nopen Set KInfFoundations OrbitGeneration OrbitNormalization\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace CompositeInterface",
 "noncomputable section",
 "open Set KInfFoundations OrbitGeneration OrbitNormalization",
 "section Chart",
 "variable {d : ℕ}",
 "end Chart",
 "section Interface",
 "variable {dA dB : ℕ}",
 "namespace ProductData",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)",
 "end ProductData",
 "namespace PreComposite",
 "variable {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type} [NormedAddCommGroup V]\n  [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)",
 "end PreComposite",
 "namespace Composite",
 "variable {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type} [NormedAddCommGroup V]\n  [NormedSpace ℝ V] (C : Composite ΩA ΩB V)",
 "end Composite",
 "namespace ProductData",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)\n  (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ))",
 "end ProductData",
 "end Interface",
 "namespace Model",
 "variable {d dA dB : ℕ}",
 "end Model",
 "section Instances",
 "open Model",
 "end Instances",
 "section Padding",
 "variable {dA dB : ℕ} {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type}\n  [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)",
 "end Padding",
 "section PaddedInstance",
 "open Model",
 "end PaddedInstance",
 "open Model in",
 "end",
 "end CompositeInterface",
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


def decl_chunks(text):
    """name -> (kind, chunk up to the next declaration or stop marker, proof text after ' :=' for theorems)."""
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
        proof = ''
        if m.group(1) in ('theorem', 'lemma'):
            j = chunk.find(' :=')
            if j != -1:
                proof = text[start + j:nxt]
                chunk = chunk[:j]
        out[m.group(2)] = (m.group(1), chunk, proof)
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


def norm(s):
    return ' '.join(s.split())


def fields(structure_text):
    """The field names of a structure chunk: the two-space-indented `name :` lines after `where`."""
    body = structure_text.split(' where', 1)[1] if ' where' in structure_text else ''
    return [m.group(1) for m in re.finditer(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M)]


PREFIX = 'OIBridge.CompositeInterface.'
LAWS = {  # law theorem -> its namespace inside the module
    'margA_prodState': 'ProductData', 'margA_attach': 'ProductData', 'eff_margA': 'PreComposite',
    'margA_mem': 'PreComposite', 'readout_sum': 'PreComposite', 'isEffectOn_readout': 'PreComposite',
    'readout_prodState': 'ProductData', 'readout_attach': 'PreComposite', 'condA_mem': 'PreComposite',
    'condA_prodState': 'ProductData', 'jointReversible_words': 'PreComposite', 'minBody_subset': 'PreComposite',
    'subset_maxBody': 'PreComposite', 'pairing_injective': 'Composite',
}
OPS = ('attach', 'margA', 'condA', 'readout', 'minBody', 'maxBody')
INSTANCES = ('bitComposite', 'ball3MinComposite', 'ball3MaxComposite')
PAD_THMS = ('not_locallyTomographic_paddedPre', 'no_composite_over_paddedPre', 'not_locallyTomographic_paddedBall3',
            'no_composite_over_paddedBall3', 'bitComposite_nonempty', 'ball3MinComposite_nonempty')
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'TensorProduct', '⊗', 'kronecker', 'Kronecker', 'Matrix', 'Hilbert',
                  'InnerProductSpace', 'Bell')
SCOPE_TOKENS = ('CNOT', 'NativeGate', 'Entangling', 'BlockData', 'BoundaryTransitive', 'TransBody', 'OrdInf',
                'InfiniteOrderOn', 'FiniteOrderOn', 'invMatrix', 'ElementaryDrivability', 'CopyNatural', 'finrank',
                'SCInf', 'FiniteRank', 'LocalExt', 'Drive', 'avail', 'CompletionChart', 'chartBody', 'OpDatum')
IMPORT_OK = re.compile(r'^import (OIBridge\.CompletionAction|Mathlib\.[\w.]+)$')
DISCLAIMER = 'Local tomography is a premise field of the structure, not a theorem'
MODEL_TOKENS = re.compile(r'\bCarrier\b|\bpState\b|\bpEff\b|\bpEffLin\b|\bhom\b|\bcoeff\b|\bmodelData\b|\bbasisEff\b'
                          r'|Fin 3|\bball3\b|\bsimplex\b|\bpaddedBall3\b')
PRODUCTDATA_FIELDS = ['prodState', 'prodState_combo_left', 'prodState_combo_right', 'prodEff', 'prodEff_apply']
PRECOMPOSITE_FIELDS = ['Ω', 'convex', 'prod_mem', 'prodEff_effect', 'prodEff_unit']
COMPOSITE_FIELDS = ['lt']
LT_BODY = ('∀ ω ∈ Ω, ∀ ω\' ∈ Ω, (∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ), IsEffectOn ΩA e → '
           'IsEffectOn ΩB f → prodEff e f ω = prodEff e f ω\') → ω = ω\'')
MINBODY_TEXT = 'convexHull ℝ (Set.image2 D.prodState ΩA ΩB)'
MAXBODY_TEXTS = ('{ω | D.prodEff (unitEff dA) (unitEff dB) ω = 1 ∧', '0 ≤ D.prodEff e f ω}')
PAD_TEXTS = ('prodState x y := (P.prodState x y, 0)', 'Ω := P.Ω ×ˢ Set.Icc (0 : ℝ) 1')
PAD1_CONCL = '¬ LocallyTomographic (paddedPre P)'
PAD2_CONCL = '¬ ∃ C : Composite ΩA ΩB (V × ℝ), C.toPreComposite = paddedPre P'
VERDICT_INSTANCES = ('Nonempty (Composite (simplex 2) (simplex 2) (Carrier 2 2))',
                     'Nonempty (Composite ball3 ball3 (Carrier 3 3))')


def model_section(mod):
    i = mod.find('\n/-! ### §E')
    j = mod.find('\n/-! ### The verdict')
    return (i, j) if i != -1 and j != -1 else (None, None)


def model_names(mod):
    i, j = model_section(mod)
    return {n for _, n in decls(mod[i:j])} if i is not None else set()


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    code = code_only(mod)
    # S1
    hits = [t for t in NEUTRAL_TOKENS if t in mod]
    imports = re.findall(r'^import .*$', mod, re.M)
    bad_imp = [l for l in imports if not IMPORT_OK.match(l)]
    check('S1', 'field-neutral: no complex, tensor, Kronecker, matrix or Hilbert token; imports whitelisted; '
                'disclaimer present%s%s' % (tag, (' %s' % (hits + bad_imp)[:3]) if hits or bad_imp else ''),
          not hits and not bad_imp and bool(imports) and DISCLAIMER in norm(mod))
    # S2
    bad2 = []
    for n, (k, t, _) in chunks.items():
        if k not in ('theorem', 'lemma'):
            continue
        concl = norm(split_statement(t)[1])
        if n == 'comp1_core':
            if concl.count('Nonempty (Composite') != 2 or not all(v in concl for v in VERDICT_INSTANCES):
                bad2.append(n)
            concl = concl.replace(VERDICT_INSTANCES[0], '').replace(VERDICT_INSTANCES[1], '')
        stripped = concl.replace('¬ LocallyTomographic', '').replace('¬ ∃ C : Composite', '')
        if 'LocallyTomographic' in stripped or 'Nonempty (Composite' in stripped \
                or re.search(r'∃ [^,]*: Composite', stripped):
            bad2.append(n)
    lt_assign = [n for n, (k, t, _) in chunks.items() if re.search(r'^\s*lt\b[^:]*:=', t, re.M)]
    check('S2', 'local tomography and composite existence are never concluded; `lt` assigned only in the two model '
                'composites%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''),
          not bad2 and sorted(lt_assign) == ['maxComposite', 'minComposite'])
    # S3
    comp = texts.get('Composite', '')
    assign = [n for n, (k, t, _) in chunks.items()
              if re.search(r'^\s*prodState\b[^:]*:=|^\s*prodEff\b[^:]*:=', t, re.M)]
    check('S3', 'abstract carrier; extremal bodies defined from the fields; product data assigned only in the model '
                'and the padding control' + tag,
          kinds.get('Composite') == 'structure' and '(V : Type)' in norm(comp)
          and 'extends PreComposite ΩA ΩB V' in norm(comp) and 'Carrier' not in comp
          and MINBODY_TEXT in norm(texts.get('minBody', '')) and kinds.get('minBody') == 'def'
          and all(s in norm(texts.get('maxBody', '')) for s in MAXBODY_TEXTS) and kinds.get('maxBody') == 'def'
          and sorted(assign) == ['modelData', 'paddedPre'])
    # S4
    mn = model_names(mod)
    bad4 = [n for n, t in texts.items() if n not in mn and n != 'comp1_core' and MODEL_TOKENS.search(t)]
    shits = [t for t in SCOPE_TOKENS if re.search(r'(?<![\w.])%s(?!\w)' % re.escape(t), code)]
    vt = norm(texts.get('comp1_core', ''))
    check('S4', 'the coordinate model confined to its sections; no gate, selector, transitivity, order, drive or '
                'availability token%s%s' % (tag, (' %s' % (bad4 + shits)[:3]) if bad4 or shits else ''),
          not bad4 and not shits and 'D.margA (D.prodState x y) = x) ∧' in vt)
    # S5
    structs = [texts.get(s, '') for s in ('ProductData', 'PreComposite', 'Composite')]
    op_fields = [o for o in OPS if any(o in fields(s) for s in structs)]
    check('S5', 'the operations are definitions, not fields; every law is a kernel theorem with its print' + tag,
          all(kinds.get(o) == 'def' for o in OPS) and kinds.get('JointReversible') == 'abbrev' and not op_fields
          and all(kinds.get(l) == 'theorem' and PREFIX + ns + '.' + l in prints for l, ns in LAWS.items()))
    # S6
    ltdef = norm(texts.get('LocallyTomographic', ''))
    check('S6', 'the three structures carry exactly their frozen fields; `LocallyTomographic` is the body of `lt`' + tag,
          fields(texts.get('ProductData', '')) == PRODUCTDATA_FIELDS
          and fields(texts.get('PreComposite', '')) == PRECOMPOSITE_FIELDS
          and 'extends ProductData dA dB V' in norm(texts.get('PreComposite', ''))
          and fields(comp) == COMPOSITE_FIELDS and LT_BODY in norm(comp)
          and kinds.get('LocallyTomographic') == 'def'
          and LT_BODY.replace('∀ ω ∈ Ω, ∀ ω\' ∈ Ω', '∀ ω ∈ P.Ω, ∀ ω\' ∈ P.Ω').replace('prodEff e f', 'P.prodEff e f')
          in ltdef)
    # S7
    bad7 = [l for l, ns in LAWS.items() if ns != 'Composite'
            and re.search(r'(?<!Pre)Composite', texts.get(l, '') + ' ' + ns)]
    check('S7', 'every law other than the separation clause is stated over ProductData or PreComposite%s%s'
          % (tag, (' %s' % bad7[:3]) if bad7 else ''), not bad7)
    # S8
    mm, cm = norm(texts.get('margA_mem', '')), norm(texts.get('condA_mem', ''))
    rs = norm(texts.get('readout_sum', ''))
    sr = texts.get('SharpReadout', '')
    check('S8', 'the marginal and conditional-state laws carry compactness and convexity; the readout test takes a '
                'SharpReadout with `sum_eq`' + tag,
          '(hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA)' in mm and norm(split_statement(mm)[1]) == 'P.margA ω ∈ ΩA'
          and '(hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA)' in cm and '(hf : IsEffectOn ΩB f)' in cm
          and '(hne : P.prodEff (unitEff dA) f ω ≠ 0)' in cm and norm(split_statement(cm)[1]) == 'P.condA f ω ∈ ΩA'
          and '(R : SharpReadout ΩB)' in rs and kinds.get('SharpReadout') == 'structure'
          and 'sum_eq : f 0 + f 1 = unitEff dB' in norm(sr) and fields(sr) == ['y', 'f', 'pd', 'sum_eq'])
    # S9
    pp = norm(texts.get('paddedPre', ''))
    p1, p2 = texts.get('not_locallyTomographic_paddedPre', ''), texts.get('no_composite_over_paddedPre', '')
    check('S9', 'the padding control is the frozen construction with its two negative theorems; the instances are '
                'definitions with nonemptiness theorems, all printed' + tag,
          kinds.get('paddedPre') == 'def' and all(s in pp for s in PAD_TEXTS)
          and '(hne : P.Ω.Nonempty)' in norm(p1) and norm(split_statement(p1)[1]) == PAD1_CONCL
          and '(hne : P.Ω.Nonempty)' in norm(p2) and norm(split_statement(p2)[1]) == PAD2_CONCL
          and all(kinds.get(i) == 'def' for i in INSTANCES)
          and all(kinds.get(t) == 'theorem' and PREFIX + t in prints for t in PAD_THMS))


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
    check('N2', 'every frozen statement, definition and structure unchanged%s%s'
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


def census_ok(d_text, e_text):
    try:
        d, e = json.loads(d_text), json.loads(e_text)
    except Exception:
        return False
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['name'].startswith(PREV_FAMILY_PREFIX)]
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
    must_fail('N2', 'a changed binder context', replace_once(mod, 'variable {d dA dB : ℕ}', 'variable {d dA dB : ℕ} {V : Type}'))
    must_fail('N2', 'a changed continuation line of a variable block',
              replace_once(mod, '  [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)\n\n/-- The body is nonempty',
                           '  [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V) (hP : P.Ω.Nonempty)\n\n/-- The body is nonempty'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem margA_prodState (x : Fin dA → ℝ) (y : Fin dB → ℝ) : D.margA (D.prodState x y) = x',
                           'theorem margA_prodState (x : Fin dA → ℝ) (y : Fin dB → ℝ) (hy : y ∈ ΩB) : D.margA (D.prodState x y) = x'))
    must_fail('N3', 'a sorry', append_decl(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('S1', 'a tensor-product import',
              replace_once(mod, 'import OIBridge.CompletionAction\n',
                           'import OIBridge.CompletionAction\nimport Mathlib.LinearAlgebra.TensorProduct.Basic\n'))
    must_fail('S1', 'a complex scalar', replace_once(mod, 'def unitEff (d : ℕ)', 'def unitEffC (d : ℕ) : (Fin d → ℂ) → ℂ := fun _ => 1\n\ndef unitEff (d : ℕ)'))
    must_fail('S2', 'local tomography concluded of a pre-composite',
              append_decl(mod, 'theorem lt_of_pre {dA dB : ℕ} {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type}\n'
                               '    [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V) :\n'
                               '    LocallyTomographic P := by\n  intro ω _ ω\' _ _\n  sorry'))
    must_fail('S2', '`lt` assigned outside the model composites',
              replace_once(mod, 'def paddedPre : PreComposite ΩA ΩB (V × ℝ) where\n',
                           'def paddedPre : PreComposite ΩA ΩB (V × ℝ) where\n  lt := sorry\n'))
    must_fail('S3', 'the composite fixed to the coordinate carrier',
              replace_once(mod, 'structure Composite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)\n    [NormedAddCommGroup V] [NormedSpace ℝ V] extends PreComposite ΩA ΩB V where',
                           'structure Composite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ))\n    extends PreComposite ΩA ΩB (Fin (dA + 1) → Fin (dB + 1) → ℝ) where'))
    must_fail('S4', 'the coordinate model in a law',
              replace_once(mod, 'theorem margA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) :',
                           'theorem margA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) (hd : dA = Fintype.card (Fin 3)) :'))
    must_fail('S4', 'a dimension-selector token',
              append_decl(mod, 'def NativeGate : Prop := True'))
    must_fail('S5', 'discard made a structure field',
              replace_once(mod, '  Ω : Set V\n  convex : Convex ℝ Ω\n', '  Ω : Set V\n  margA : V → Fin dA → ℝ\n  convex : Convex ℝ Ω\n'))
    must_fail('S6', 'a second field beside `lt`',
              replace_once(mod, 'IsEffectOn ΩA e → IsEffectOn ΩB f → prodEff e f ω = prodEff e f ω\') → ω = ω\'\n\nnamespace ProductData',
                           'IsEffectOn ΩA e → IsEffectOn ΩB f → prodEff e f ω = prodEff e f ω\') → ω = ω\'\n  big : minBody ≠ Ω\n\nnamespace ProductData'))
    must_fail('S7', 'a law restated over Composite',
              replace_once(mod, 'theorem eff_margA {ω : V} (hω : ω ∈ P.Ω) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) :',
                           'theorem eff_margA (C : Composite ΩA ΩB V) {ω : V} (hω : ω ∈ P.Ω) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) :'))
    must_fail('S8', 'compactness dropped from the marginal law',
              replace_once(mod, 'theorem margA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) :',
                           'theorem margA_mem (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) :'))
    must_fail('S9', 'the padding print removed',
              replace_once(mod, '#print axioms OIBridge.CompositeInterface.not_locallyTomographic_paddedPre\n', ''))
    must_fail('S9', 'the padded body collapsed to height zero',
              replace_once(mod, 'Ω := P.Ω ×ˢ Set.Icc (0 : ℝ) 1', 'Ω := P.Ω ×ˢ Set.Icc (0 : ℝ) 0'))
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['name'].startswith(PREV_FAMILY_PREFIX)][0]
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
