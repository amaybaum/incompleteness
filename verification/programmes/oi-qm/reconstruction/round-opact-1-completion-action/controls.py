#!/usr/bin/env python3
"""controls.py -- round OPACT-1's own contracts, FROZEN with the preregistration beside it.

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
  S1  premise     every load-bearing theorem and construction of the completion action carries `AffineRespect` among
                  its hypotheses and never `StateRespect`; the extension theorem carries its affine-relation
                  hypothesis; `StateRespect` occurs only in its definition, in `stateRespect_of_affineRespect`, in the
                  separation witness and twice in the verdict
  S2  separation  the witness `midOp_stateRespect : StateRespect midOp` and `midOp_not_affineRespect :
                  ¬ AffineRespect midOp` are kernel theorems with prints, stated exactly; the verdict carries
                  `StateRespect midOp ∧ ¬ AffineRespect midOp` and `AffineRespect T → StateRespect T`
  S3  structure   the inverse equivalence and its `PreservesBody` carry both inverse-availability hypotheses; the
                  chart exists only under `FiniteRank (body D)` and a nonempty body; every chart-level verdict
                  clause quantifies a `CompletionChart`; no theorem concludes `PreservesBody` without `Undoes`
  S4  neutrality  no declaration, conclusion or code mentions a drive, a flow, transitivity, an invariant inner
                  product, a dimension, a ball or ellipsoid, SC∞, countability, a concrete gate or phase, or
                  `stageEffects`; the only concrete `OpDatum` is the countermodel `midOp`
  S5  header      the header carries the downstream-neutrality disclaimer
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.StageCompletion`
  C   census      the census is D's with exactly the frozen family inserted after the CMP-1 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib, io, json, re, subprocess, sys

D = '254ad0a7f19b3cf6f6ce28e1a7b955f18e4337e4'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-opact-1-completion-action/'
PREREG = RDIR + 'preregistration.md'
MOD = 'verification/lean-mathlib/OIBridge/CompletionAction.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '8bcab4a5d1d98acdbc18bdba1fbddb43f370ed0c'
ANCHOR_IMPORT = 'import OIBridge.StageCompletion\n'
NEW_IMPORT = 'import OIBridge.CompletionAction\n'
ANCHOR_FAMILY_PREFIX = 'the stage completion'
CENSUS_FAMILY = json.loads(r'''{
 "name": "completion-valued operation data and the affine automorphisms of the completed body they induce (round OPACT-1, reconstruction)",
 "modules": [
  "CompletionAction"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round OPACT-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-opact-1-completion-action/preregistration.md. The kernel layer defines a completion-valued operation datum, which carries each stage preparation to a point of the completed body, and the two respect conditions StateRespect and AffineRespect; AffineRespect implies StateRespect and not conversely (midOp_stateRespect, midOp_not_affineRespect). Under AffineRespect a datum induces exactly one affine map of the chart of a nonempty completed body of finite rank (existsUnique_induced), an affine extension forces AffineRespect (affineRespect_of_induced), the induced map preserves the completed body (induced_mem) and composes (induced_after), a datum with an inverse datum induces an affine equivalence that preserves the body (preservesBody_inducedEquiv), and stage effects read after the induced map are effects (isEffectOn_pullback). Carried by no manuscript. Nothing here supplies an operation, a flow, transitivity, an invariant inner product, a dimension or a ball, and nothing uses SC∞."
}''')
DECLS = json.loads(r'''[
 [
  "structure",
  "OpDatum"
 ],
 [
  "def",
  "StateRespect"
 ],
 [
  "def",
  "AffineRespect"
 ],
 [
  "theorem",
  "stateRespect_of_affineRespect"
 ],
 [
  "theorem",
  "sum_smul_affine"
 ],
 [
  "theorem",
  "exists_affine_of_relations"
 ],
 [
  "structure",
  "CompletionChart"
 ],
 [
  "theorem",
  "exists_completionChart"
 ],
 [
  "noncomputable def",
  "coordsOf"
 ],
 [
  "def",
  "chartBody"
 ],
 [
  "noncomputable def",
  "gen"
 ],
 [
  "theorem",
  "mem_range_of_mem_body"
 ],
 [
  "theorem",
  "chart_coordsOf"
 ],
 [
  "theorem",
  "coordsOf_chart"
 ],
 [
  "theorem",
  "chart_gen"
 ],
 [
  "theorem",
  "coordsOf_mem_chartBody"
 ],
 [
  "theorem",
  "isClosedEmbedding_chart"
 ],
 [
  "theorem",
  "body_convex"
 ],
 [
  "theorem",
  "body_isClosed"
 ],
 [
  "theorem",
  "chartBody_subset"
 ],
 [
  "theorem",
  "affineSpan_gen"
 ],
 [
  "theorem",
  "gen_relation"
 ],
 [
  "theorem",
  "exists_induced"
 ],
 [
  "theorem",
  "induced_unique"
 ],
 [
  "theorem",
  "existsUnique_induced"
 ],
 [
  "theorem",
  "affineRespect_of_induced"
 ],
 [
  "noncomputable def",
  "induced"
 ],
 [
  "theorem",
  "induced_gen"
 ],
 [
  "theorem",
  "mapsTo_chartBody"
 ],
 [
  "theorem",
  "induced_mem"
 ],
 [
  "noncomputable def",
  "after"
 ],
 [
  "theorem",
  "comp_gen"
 ],
 [
  "theorem",
  "affineRespect_after"
 ],
 [
  "theorem",
  "induced_after"
 ],
 [
  "def",
  "Undoes"
 ],
 [
  "theorem",
  "comp_eq_id"
 ],
 [
  "noncomputable def",
  "inducedEquiv"
 ],
 [
  "theorem",
  "inducedEquiv_apply"
 ],
 [
  "theorem",
  "inducedEquiv_symm_apply"
 ],
 [
  "theorem",
  "preservesBody_inducedEquiv"
 ],
 [
  "theorem",
  "isEffectOn_pullback"
 ],
 [
  "noncomputable def",
  "midStage"
 ],
 [
  "theorem",
  "midStage_true"
 ],
 [
  "theorem",
  "midStage_false"
 ],
 [
  "theorem",
  "midStage_false0"
 ],
 [
  "theorem",
  "midStage_false1"
 ],
 [
  "theorem",
  "midStage_false2"
 ],
 [
  "noncomputable def",
  "midD"
 ],
 [
  "theorem",
  "prepVec_midD_apply"
 ],
 [
  "def",
  "midSwap"
 ],
 [
  "noncomputable def",
  "midOp"
 ],
 [
  "theorem",
  "sum_smul_apply"
 ],
 [
  "def",
  "midIdx"
 ],
 [
  "theorem",
  "midOp_stateRespect"
 ],
 [
  "def",
  "midPrep"
 ],
 [
  "theorem",
  "midPrep_injective"
 ],
 [
  "def",
  "midCoef"
 ],
 [
  "theorem",
  "midCoef0"
 ],
 [
  "theorem",
  "midCoef1"
 ],
 [
  "theorem",
  "midCoef2"
 ],
 [
  "theorem",
  "midOp_not_affineRespect"
 ],
 [
  "theorem",
  "opact1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "OpDatum": "structure OpDatum (D : DirectedStages) where\n  τ : Prep D → CSpace D\n  mem_body : ∀ x, τ x ∈ body D",
 "StateRespect": "def StateRespect (T : OpDatum D) : Prop :=\n  ∀ x y, prepVec D x = prepVec D y → T.τ x = T.τ y",
 "AffineRespect": "def AffineRespect (T : OpDatum D) : Prop :=\n  ∀ (s : Finset (Prep D)) (c : Prep D → ℝ), ∑ x ∈ s, c x = 0 →\n    ∑ x ∈ s, c x • prepVec D x = 0 → ∑ x ∈ s, c x • T.τ x = 0",
 "stateRespect_of_affineRespect": "theorem stateRespect_of_affineRespect {T : OpDatum D} (hT : AffineRespect T) : StateRespect T",
 "sum_smul_affine": "theorem sum_smul_affine (f : E →ᵃ[ℝ] F) (s : Finset ι) (c : ι → ℝ) (v : ι → E)\n    (hc : ∑ i ∈ s, c i = 0) :\n    ∑ i ∈ s, c i • f (v i) = f.linear (∑ i ∈ s, c i • v i)",
 "exists_affine_of_relations": "theorem exists_affine_of_relations (v : ι → E) (u : ι → F)\n    (h : ∀ (s : Finset ι) (c : ι → ℝ), ∑ i ∈ s, c i = 0 → ∑ i ∈ s, c i • v i = 0 →\n      ∑ i ∈ s, c i • u i = 0) :\n    ∃ Φ : E →ᵃ[ℝ] F, ∀ i, Φ (v i) = u i",
 "CompletionChart": "structure CompletionChart (D : DirectedStages) where\n  d : ℕ\n  L : (Fin d → ℝ) →ₗ[ℝ] CSpace D\n  p0 : CSpace D\n  Lg : CSpace D →ₗ[ℝ] (Fin d → ℝ)\n  hL : LinearMap.ker L = ⊥\n  hLg : ∀ w, Lg (L w) = w\n  hspan : ∀ v, v ∈ affineSpan ℝ (body D) ↔ v ∈ Set.range (chart L p0)",
 "exists_completionChart": "theorem exists_completionChart (hne : (body D).Nonempty) (hfr : FiniteRank (body D)) :\n    Nonempty (CompletionChart D)",
 "coordsOf": "noncomputable def coordsOf (v : CSpace D) : Fin C.d → ℝ := chartRetract C.Lg C.p0 v",
 "chartBody": "def chartBody : Set (Fin C.d → ℝ) := bodyR C.L C.p0 (body D)",
 "gen": "noncomputable def gen (x : Prep D) : Fin C.d → ℝ := coordsOf C (prepVec D x)",
 "mem_range_of_mem_body": "theorem mem_range_of_mem_body {v : CSpace D} (hv : v ∈ body D) :\n    v ∈ Set.range (chart C.L C.p0)",
 "chart_coordsOf": "theorem chart_coordsOf {v : CSpace D} (hv : v ∈ body D) : chart C.L C.p0 (coordsOf C v) = v",
 "coordsOf_chart": "theorem coordsOf_chart (w : Fin C.d → ℝ) : coordsOf C (chart C.L C.p0 w) = w",
 "chart_gen": "theorem chart_gen (x : Prep D) : chart C.L C.p0 (gen C x) = prepVec D x",
 "coordsOf_mem_chartBody": "theorem coordsOf_mem_chartBody {v : CSpace D} (hv : v ∈ body D) : coordsOf C v ∈ chartBody C",
 "isClosedEmbedding_chart": "theorem isClosedEmbedding_chart : IsClosedEmbedding (chart C.L C.p0)",
 "body_convex": "theorem body_convex : Convex ℝ (body D)",
 "body_isClosed": "theorem body_isClosed : IsClosed (body D)",
 "chartBody_subset": "theorem chartBody_subset : chartBody C ⊆ closure (convexHull ℝ (Set.range (gen C)))",
 "affineSpan_gen": "theorem affineSpan_gen : affineSpan ℝ (Set.range (gen C)) = ⊤",
 "gen_relation": "theorem gen_relation {T : OpDatum D} (hT : AffineRespect T) (s : Finset (Prep D))\n    (c : Prep D → ℝ) (hc : ∑ x ∈ s, c x = 0) (hv : ∑ x ∈ s, c x • gen C x = 0) :\n    ∑ x ∈ s, c x • coordsOf C (T.τ x) = 0",
 "exists_induced": "theorem exists_induced {T : OpDatum D} (hT : AffineRespect T) :\n    ∃ Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ), ∀ x, Φ (gen C x) = coordsOf C (T.τ x)",
 "induced_unique": "theorem induced_unique {Φ Ψ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ)}\n    (h : ∀ x, Φ (gen C x) = Ψ (gen C x)) : Φ = Ψ",
 "existsUnique_induced": "theorem existsUnique_induced {T : OpDatum D} (hT : AffineRespect T) :\n    ∃! Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ), ∀ x, Φ (gen C x) = coordsOf C (T.τ x)",
 "affineRespect_of_induced": "theorem affineRespect_of_induced {T : OpDatum D} (Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ))\n    (hΦ : ∀ x, Φ (gen C x) = coordsOf C (T.τ x)) : AffineRespect T",
 "induced": "noncomputable def induced (T : OpDatum D) (hT : AffineRespect T) :\n    (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ) :=\n  Classical.choose (exists_induced C hT)",
 "induced_gen": "theorem induced_gen {T : OpDatum D} (hT : AffineRespect T) (x : Prep D) :\n    induced C T hT (gen C x) = coordsOf C (T.τ x)",
 "mapsTo_chartBody": "theorem mapsTo_chartBody {T : OpDatum D} (Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ))\n    (hΦ : ∀ x, Φ (gen C x) = coordsOf C (T.τ x)) :\n    ∀ w ∈ chartBody C, Φ w ∈ chartBody C",
 "induced_mem": "theorem induced_mem {T : OpDatum D} (hT : AffineRespect T) :\n    ∀ w ∈ chartBody C, induced C T hT w ∈ chartBody C",
 "after": "noncomputable def after (S T : OpDatum D) (hS : AffineRespect S) : OpDatum D where\n  τ x := chart C.L C.p0 (induced C S hS (coordsOf C (T.τ x)))\n  mem_body x := induced_mem C hS _ (coordsOf_mem_chartBody C (T.mem_body x))",
 "comp_gen": "theorem comp_gen {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T) (x : Prep D) :\n    ((induced C S hS).comp (induced C T hT)) (gen C x) = coordsOf C ((after C S T hS).τ x)",
 "affineRespect_after": "theorem affineRespect_after {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T) :\n    AffineRespect (after C S T hS)",
 "induced_after": "theorem induced_after {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T) :\n    induced C (after C S T hS) (affineRespect_after C hS hT) =\n      (induced C S hS).comp (induced C T hT)",
 "Undoes": "def Undoes (S T : OpDatum D) (hS : AffineRespect S) : Prop :=\n  ∀ x, (after C S T hS).τ x = prepVec D x",
 "comp_eq_id": "theorem comp_eq_id {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)\n    (h : Undoes C S T hS) : (induced C S hS).comp (induced C T hT) = AffineMap.id ℝ _",
 "inducedEquiv": "noncomputable def inducedEquiv {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)\n    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ) :=\n  AffineEquiv.ofBijective (φ := induced C T hT)\n    ⟨Function.LeftInverse.injective (g := induced C S hS)\n        (fun w => congrFun (congrArg DFunLike.coe (comp_eq_id C hS hT hST)) w),\n      Function.RightInverse.surjective (g := induced C S hS)\n        (fun w => congrFun (congrArg DFunLike.coe (comp_eq_id C hT hS hTS)) w)⟩",
 "inducedEquiv_apply": "theorem inducedEquiv_apply {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)\n    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) (w : Fin C.d → ℝ) :\n    inducedEquiv C hS hT hST hTS w = induced C T hT w",
 "inducedEquiv_symm_apply": "theorem inducedEquiv_symm_apply {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)\n    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) (w : Fin C.d → ℝ) :\n    (inducedEquiv C hS hT hST hTS).symm w = induced C S hS w",
 "preservesBody_inducedEquiv": "theorem preservesBody_inducedEquiv {S T : OpDatum D} (hS : AffineRespect S)\n    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) :\n    PreservesBody (chartBody C) {inducedEquiv C hS hT hST hTS}",
 "isEffectOn_pullback": "theorem isEffectOn_pullback {T : OpDatum D} (hT : AffineRespect T) (a : Label D) :\n    IsEffectOn (chartBody C) ((effR C.L C.p0 (coord D a)).comp (induced C T hT))",
 "midStage": "noncomputable def midStage : FiniteStage where\n  P := Fin 3\n  E := Bool\n  p e x := if e then 1 else ((x : ℕ) : ℝ) / 2\n  unit := true\n  nonneg e x := by\n    split_ifs\n    · norm_num\n    · positivity\n  le_one e x := by\n    split_ifs\n    · norm_num\n    · have hx : (x : ℕ) ≤ 2 := Nat.lt_succ_iff.mp x.isLt\n      have hx' : ((x : ℕ) : ℝ) ≤ 2 := by exact_mod_cast hx\n      linarith\n  unit_eq _ := rfl",
 "midStage_true": "theorem midStage_true (k : Fin 3) : midStage.p true k = 1",
 "midStage_false": "theorem midStage_false (k : Fin 3) : midStage.p false k = ((k : ℕ) : ℝ) / 2",
 "midStage_false0": "theorem midStage_false0 : midStage.p false (0 : Fin 3) = 0",
 "midStage_false1": "theorem midStage_false1 : midStage.p false (1 : Fin 3) = 1 / 2",
 "midStage_false2": "theorem midStage_false2 : midStage.p false (2 : Fin 3) = 1",
 "midD": "noncomputable def midD : DirectedStages where\n  ι := Bool\n  directed _ _ := ⟨true, le_top, le_top⟩\n  stage _ := midStage\n  map _ := ⟨id, id, rfl⟩\n  comp_E _ _ _ := rfl\n  comp_P _ _ _ := rfl",
 "prepVec_midD_apply": "theorem prepVec_midD_apply (x : Prep midD) (a : Label midD) :\n    prepVec midD x a = midStage.p a.2 x.2",
 "midSwap": "def midSwap : Fin 3 → Fin 3 := ![1, 0, 2]",
 "midOp": "noncomputable def midOp : OpDatum midD where\n  τ x := prepVec midD ⟨x.1, midSwap x.2⟩\n  mem_body x := prepVec_mem_body midD _",
 "sum_smul_apply": "theorem sum_smul_apply {D : DirectedStages} (s : Finset (Prep D)) (c : Prep D → ℝ)\n    (f : Prep D → CSpace D) (a : Label D) :\n    (∑ x ∈ s, c x • f x) a = ∑ x ∈ s, c x * f x a",
 "midIdx": "def midIdx (x : Prep midD) : Fin 3 := x.2",
 "midOp_stateRespect": "theorem midOp_stateRespect : StateRespect midOp",
 "midPrep": "def midPrep (k : Fin 3) : Prep midD := ⟨false, k⟩",
 "midPrep_injective": "theorem midPrep_injective : Function.Injective midPrep",
 "midCoef": "def midCoef : Fin 3 → ℝ := ![1, -2, 1]",
 "midCoef0": "theorem midCoef0 : midCoef 0 = 1",
 "midCoef1": "theorem midCoef1 : midCoef 1 = -2",
 "midCoef2": "theorem midCoef2 : midCoef 2 = 1",
 "midOp_not_affineRespect": "theorem midOp_not_affineRespect : ¬ AffineRespect midOp",
 "opact1_core": "theorem opact1_core :\n    (∀ (D : DirectedStages) (T : OpDatum D), AffineRespect T → StateRespect T) ∧\n    (StateRespect midOp ∧ ¬ AffineRespect midOp) ∧\n    (∀ (D : DirectedStages), (body D).Nonempty → FiniteRank (body D) →\n      Nonempty (CompletionChart D)) ∧\n    (∀ (D : DirectedStages) (C : CompletionChart D) (T : OpDatum D), AffineRespect T →\n      ∃! Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ), ∀ x, Φ (gen C x) = coordsOf C (T.τ x)) ∧\n    (∀ (D : DirectedStages) (C : CompletionChart D) (T : OpDatum D)\n      (Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ)), (∀ x, Φ (gen C x) = coordsOf C (T.τ x)) →\n        AffineRespect T) ∧\n    (∀ (D : DirectedStages) (C : CompletionChart D) (T : OpDatum D) (hT : AffineRespect T),\n      ∀ w ∈ chartBody C, induced C T hT w ∈ chartBody C) ∧\n    (∀ (D : DirectedStages) (C : CompletionChart D) (S T : OpDatum D) (hS : AffineRespect S)\n      (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT),\n        PreservesBody (chartBody C) {inducedEquiv C hS hT hST hTS})"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.CompletionAction.stateRespect_of_affineRespect",
 "OIBridge.CompletionAction.sum_smul_affine",
 "OIBridge.CompletionAction.exists_affine_of_relations",
 "OIBridge.CompletionAction.exists_completionChart",
 "OIBridge.CompletionAction.chartBody_subset",
 "OIBridge.CompletionAction.affineSpan_gen",
 "OIBridge.CompletionAction.existsUnique_induced",
 "OIBridge.CompletionAction.affineRespect_of_induced",
 "OIBridge.CompletionAction.induced_mem",
 "OIBridge.CompletionAction.induced_after",
 "OIBridge.CompletionAction.comp_eq_id",
 "OIBridge.CompletionAction.preservesBody_inducedEquiv",
 "OIBridge.CompletionAction.isEffectOn_pullback",
 "OIBridge.CompletionAction.midOp_stateRespect",
 "OIBridge.CompletionAction.midOp_not_affineRespect",
 "OIBridge.CompletionAction.opact1_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.StageCompletion\nimport Mathlib.LinearAlgebra.Isomorphisms\nimport Mathlib.LinearAlgebra.Finsupp.LinearCombination\n\nnamespace OIBridge\nnamespace CompletionAction\n\nopen Set Topology KInfFoundations OrbitGeneration OrbitNormalization StageCompletion\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace CompletionAction",
 "open Set Topology KInfFoundations OrbitGeneration OrbitNormalization StageCompletion",
 "variable {D : DirectedStages}",
 "section Generic",
 "variable {ι E F : Type*} [AddCommGroup E] [Module ℝ E] [AddCommGroup F] [Module ℝ F]",
 "end Generic",
 "variable (C : CompletionChart D)",
 "end CompletionAction",
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


VERDICT = 'opact1_core'
LOAD = ('gen_relation', 'exists_induced', 'existsUnique_induced', 'induced', 'induced_gen', 'induced_mem', 'after',
        'comp_gen', 'affineRespect_after', 'induced_after', 'Undoes', 'comp_eq_id', 'inducedEquiv',
        'inducedEquiv_apply', 'inducedEquiv_symm_apply', 'preservesBody_inducedEquiv', 'isEffectOn_pullback')
STATE_OK = ('StateRespect', 'stateRespect_of_affineRespect', 'midOp_stateRespect', VERDICT)
REL_HYP = ('(h : ∀ (s : Finset ι) (c : ι → ℝ), ∑ i ∈ s, c i = 0 → ∑ i ∈ s, c i • v i = 0 → '
           '∑ i ∈ s, c i • u i = 0)')
INV = ('(hST : Undoes C S T hS)', '(hTS : Undoes C T S hT)')
FORBIDDEN_CODE = re.compile(r'(ElementaryDrivability|OperationalDrive|BoundaryTransitive|SCInf|invMatrix|momentMatrix|'
                            r'ball3|ball4|\bball\b|llipsoid|Countable|ountable|Clifford|Hadamard|gateFlow|rot3|'
                            r'stageEffects|ℝ → OpDatum|finrank)')
FORBIDDEN_NAME = re.compile(r'(rive|[Ff]low|ransitiv|llipsoid|[Bb]all|nnerProduct|[Dd]im3|[Gg]ate|[Pp]hase|lifford|'
                            r'ountab|SCInf|scInf)')
DISCLAIMER = ('Nothing here supplies an operation datum, a flow, transitivity, an invariant inner product, a '
              'dimension or a ball, and nothing uses SC∞.')


def semantic_checks(mod, texts, kinds, prints, tag):
    bad = []
    for n in LOAD:
        t = texts.get(n)
        if t is None:
            bad.append(n + '?')
            continue
        b = split_statement(t)[0] if kinds.get(n) in ('theorem', 'lemma') else t
        if 'AffineRespect' not in b or 'StateRespect' in b:
            bad.append(n)
    stray = sorted(n for n, t in texts.items() if 'StateRespect' in t and n not in STATE_OK)
    vt = texts.get(VERDICT, '')
    check('S1', 'every load-bearing statement requires AffineRespect, never StateRespect%s%s'
          % (tag, (' %s' % (bad + stray)[:4]) if bad or stray else ''),
          not bad and not stray and REL_HYP in norm(texts.get('exists_affine_of_relations', ''))
          and vt.count('StateRespect') == 2)
    check('S2', 'the separation witness StateRespect ∧ ¬ AffineRespect is proved and stated exactly' + tag,
          norm(texts.get('midOp_stateRespect', '')) == 'theorem midOp_stateRespect : StateRespect midOp'
          and norm(texts.get('midOp_not_affineRespect', '')) == 'theorem midOp_not_affineRespect : ¬ AffineRespect midOp'
          and all('OIBridge.CompletionAction.' + n in prints for n in ('midOp_stateRespect', 'midOp_not_affineRespect',
                                                                       'stateRespect_of_affineRespect'))
          and 'StateRespect midOp ∧ ¬ AffineRespect midOp' in norm(vt)
          and 'AffineRespect T → StateRespect T' in norm(vt)
          and split_statement(texts.get('stateRespect_of_affineRespect', 'x x'))[1].strip() == 'StateRespect T')
    cc = norm(texts.get('exists_completionChart', ''))
    pb_bad = [n for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma') and n != VERDICT
              and 'PreservesBody' in split_statement(t)[1] and not all(h in norm(t) for h in INV)]
    check('S3', 'inverse availability, FiniteRank and the chart are required where used%s%s'
          % (tag, (' %s' % pb_bad[:3]) if pb_bad else ''),
          all(h in norm(texts.get(n, '')) for n in ('inducedEquiv', 'inducedEquiv_symm_apply',
                                                    'preservesBody_inducedEquiv') for h in INV)
          and '(hfr : FiniteRank (body D))' in cc and '(hne : (body D).Nonempty)' in cc
          and 'Nonempty (CompletionChart D)' in cc and not pb_bad
          and '(body D).Nonempty → FiniteRank (body D) → Nonempty (CompletionChart D)' in norm(vt)
          and norm(vt).count('(C : CompletionChart D)') == 4 and all(h in norm(vt) for h in INV))
    code = code_only(mod)
    names = [n for _, n in decls(mod)]
    ops = [n for n, t in texts.items() if re.search(r':\s*OpDatum (?!D\b)\w+\s+where', t)]
    check('S4', 'no drive, flow, transitivity, inner product, dimension, ball, SC∞, gate or stageEffects closure%s'
          % tag, not FORBIDDEN_CODE.search(code) and not any(FORBIDDEN_NAME.search(n) for n in names)
          and ops == ['midOp'])
    check('S5', 'the header disclaimer is present' + tag, DISCLAIMER in norm(header(mod)))


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
    k = [i for i, f in enumerate(fam) if f['name'].startswith(ANCHOR_FAMILY_PREFIX)]
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
    must_fail('S1', 'AffineRespect replaced by StateRespect in body preservation',
              replace_once(mod, 'theorem induced_mem {T : OpDatum D} (hT : AffineRespect T)',
                           'theorem induced_mem {T : OpDatum D} (hT : StateRespect T)'))
    must_fail('S1', 'the affine-relation hypothesis removed from the extension theorem',
              replace_once(mod, """    (h : ∀ (s : Finset ι) (c : ι → ℝ), ∑ i ∈ s, c i = 0 → ∑ i ∈ s, c i • v i = 0 →
      ∑ i ∈ s, c i • u i = 0) :
    ∃ Φ""", """    :
    ∃ Φ"""))
    must_fail('S1', 'a load-bearing theorem stated under StateRespect',
              append_decl(mod, 'theorem induced_of_state {T : OpDatum D} (hT : StateRespect T) : True := trivial'))
    must_fail('S2', 'the separation witness weakened',
              replace_once(mod, 'theorem midOp_not_affineRespect : ¬ AffineRespect midOp',
                           'theorem midOp_not_affineRespect : ¬ StateRespect midOp'))
    must_fail('S3', 'inverse availability dropped from PreservesBody',
              replace_once(mod, '(hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) :\n    PreservesBody',
                           '(hT : AffineRespect T) (hST : Undoes C S T hS) :\n    PreservesBody'))
    must_fail('S3', 'FiniteRank removed from the chart theorem',
              replace_once(mod, '(hne : (body D).Nonempty) (hfr : FiniteRank (body D)) :',
                           '(hne : (body D).Nonempty) :'))
    must_fail('S4', 'a one-parameter group of operations',
              append_decl(mod, 'noncomputable def phaseFlow (D : DirectedStages) : ℝ → OpDatum D := by\n'
                               '  exact absurd rfl rfl'))
    must_fail('S4', 'a stage-effect closure claim',
              append_decl(mod, 'theorem closed {T : OpDatum D} (hT : AffineRespect T) (a : Label D) :\n'
                               '    (coord D a).comp (chart C.L C.p0) ∈ stageEffects D := by\n  exact absurd rfl rfl'))
    must_fail('S4', 'a concrete operation datum',
              append_decl(mod, 'noncomputable def gateOp : OpDatum midD where\n'
                               '  τ x := prepVec midD x\n  mem_body x := prepVec_mem_body midD x'))
    must_fail('S5', 'the disclaimer dropped',
              replace_once(mod, 'and nothing uses SC∞.', 'and SC∞ is used.'))
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['name'].startswith(ANCHOR_FAMILY_PREFIX)][0]
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
