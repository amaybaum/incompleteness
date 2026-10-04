#!/usr/bin/env python3
"""controls.py -- round TRB-1's own contracts, FROZEN with the preregistration beside it.

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
                  the frozen text whole; the preamble and every context line (`variable`, `open`, `namespace`,
                  `section`, `end`, `attribute`) is the frozen text, in order -- a proof may change, a statement,
                  definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  dimension   no statement outside the controls section, `eball_three` and the verdict names `ball3`, `Fin 3`,
                  `finrank`, `square2`, `oct3` or a bare `3`; the verdict's ball clauses quantify over every `d`
  S2  no order    no order predicate and no TRANS -> ORD-infinity edge: none of the order tokens occurs anywhere in
                  the module and the irrationality import is absent; `TransBody` is `IsBodyGroup ∧ BoundaryTransitive`
  S3  hypotheses  the ball theorem and the Euclidean-ball theorem have exactly the frozen hypothesis set: `0 < d`,
                  compact, convex, nonempty interior, `PreservesBody`, `BoundaryTransitive`; no group, order, flow,
                  seed or drivability hypothesis
  S4  bridge      the two bridge directions are two theorems, each with its frozen hypothesis and conclusion; no
                  biconditional between boundary states and the frontier is stated
  S5  all-boundary the only transitivity predicate is `BoundaryTransitive`; no definition quantifies transitivity over
                  extreme points or a finite set
  S6  normalization the normalization theorem is a kernel theorem with its print and exactly the frozen sum-of-squares
                  conclusion; the factorization row and the Euclidean-ball row carry their frozen conclusions
  S7  controls    the transitivity-side controls and the polytope exclusions are kernel theorems with prints
  S8  no L3B      no text of the module names L3B, a rule, a rank, edge-permutivity or a hidden law
  S9  ray route   the ambient-norm closed-ball identifier occurs nowhere in the module; the ball theorem's proof names
                  the ray lemma and the sphere lemma
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.CompletionAction`
  C   census      the census is D's with exactly the frozen family inserted after the OPACT-1 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '7c821261e2537a97b85ab78ae50c6998600bc019'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-trb-1-transitive-body/'
PREREG = RDIR + 'preregistration.md'
MOD = 'verification/lean-mathlib/OIBridge/TransitiveBody.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '31f63583ec1b6451f77cc519b19914e4bd3ebb51'
ANCHOR_IMPORT = 'import OIBridge.CompletionAction\n'
NEW_IMPORT = 'import OIBridge.TransitiveBody\n'
PREV_FAMILY_PREFIX = 'completion-valued operation data and the affine automorphism'
CENSUS_FAMILY = json.loads(r'''{
 "name": "the completed-chart adapter, the boundary-state bridge, boundary purity, and the invariant-inner-product ball of a boundary-transitive body (round TRB-1, reconstruction)",
 "modules": [
  "TransitiveBody"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round TRB-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-trb-1-transitive-body/preregistration.md. The kernel layer: the chart body of a completion chart is compact, convex and has nonempty interior with no finite-dimensionality of the completion space (chartBody_isCompact, chartBody_interior_nonempty); boundary states and frontier points coincide in a convex body with interior, one theorem per direction (frontier_of_isBoundaryState, isBoundaryState_of_frontier); under body-preserving all-boundary transitivity every boundary state is extreme, so a body with a non-extreme boundary state is boundary transitive for no body-preserving family (extreme_of_isBoundaryState_of_transitive, not_boundaryTransitive_of_nonextreme_boundary); a compact convex body with interior that is boundary transitive under a body-preserving family is the closed ball of its invariant inner product about its centroid (eq_qBall_of_boundaryTransitive) and an affine image of the coordinate Euclidean ball of its dimension (exists_affine_image_eq_eball), through the frozen normalization adapter (exists_factor_invMatrix, qnorm_eq_sum_sq), proved in the invariant form by the ray argument and not through the ambient-norm lemma eq_closedBall_of_frontier_subset_sphere; TRANS (a body group acting transitively on all boundary states) is defined and no order predicate is, so the module carries no edge from transitivity to order; the transitivity-side controls on ball3 (transBody_fullAut3, boundaryTransitive_refls3, not_transBody_flow) and the square and octahedron polytope controls are theorems. Carried by no manuscript. Nothing here claims dimension 3, energy observability, a drive, the order of any map, or any OI sourcing of finite rank, stage consistency or operation data."
}''')
DECLS = json.loads(r'''[
 [
  "theorem",
  "norm_prepVec_le_one"
 ],
 [
  "theorem",
  "body_subset_closedBall"
 ],
 [
  "theorem",
  "continuous_chart"
 ],
 [
  "theorem",
  "chartBody_convex"
 ],
 [
  "theorem",
  "chartBody_isClosed"
 ],
 [
  "theorem",
  "chartBody_isBounded"
 ],
 [
  "theorem",
  "chartBody_isCompact"
 ],
 [
  "theorem",
  "affineSpan_chartBody"
 ],
 [
  "theorem",
  "chartBody_interior_nonempty"
 ],
 [
  "theorem",
  "frontier_of_isBoundaryState"
 ],
 [
  "theorem",
  "isBoundaryState_of_frontier"
 ],
 [
  "theorem",
  "exists_boundary_ray"
 ],
 [
  "structure",
  "IsBodyGroup"
 ],
 [
  "theorem",
  "IsBodyGroup.preservesBody"
 ],
 [
  "def",
  "TransBody"
 ],
 [
  "theorem",
  "extreme_image"
 ],
 [
  "theorem",
  "not_mem_interior_of_extreme"
 ],
 [
  "theorem",
  "isBoundaryState_of_extreme"
 ],
 [
  "theorem",
  "extreme_of_isBoundaryState_of_transitive"
 ],
 [
  "theorem",
  "not_boundaryTransitive_of_nonextreme_boundary"
 ],
 [
  "noncomputable def",
  "qnorm"
 ],
 [
  "def",
  "qBall"
 ],
 [
  "theorem",
  "mem_qBall"
 ],
 [
  "theorem",
  "qnorm_smul"
 ],
 [
  "theorem",
  "qnorm_zero"
 ],
 [
  "theorem",
  "qnorm_pos"
 ],
 [
  "theorem",
  "qnorm_nonneg"
 ],
 [
  "theorem",
  "image_eq_of_preservesBody"
 ],
 [
  "theorem",
  "centroid_fixed_of_preservesBody"
 ],
 [
  "theorem",
  "qnorm_sub_centroid_apply"
 ],
 [
  "theorem",
  "boundary_qnorm_const"
 ],
 [
  "theorem",
  "centroid_mem"
 ],
 [
  "theorem",
  "centroid_mem_interior"
 ],
 [
  "theorem",
  "eq_qBall_of_boundaryTransitive"
 ],
 [
  "def",
  "eball"
 ],
 [
  "theorem",
  "mem_eball"
 ],
 [
  "theorem",
  "finsuppSum_eq_dot"
 ],
 [
  "theorem",
  "invMatrix_posDef"
 ],
 [
  "theorem",
  "exists_factor_invMatrix"
 ],
 [
  "theorem",
  "qnorm_eq_sum_sq"
 ],
 [
  "theorem",
  "exists_affine_image_eq_eball"
 ],
 [
  "theorem",
  "chartBody_eq_qBall"
 ],
 [
  "theorem",
  "chartBody_eq_eball"
 ],
 [
  "theorem",
  "eq_qBall_of_transBody"
 ],
 [
  "theorem",
  "exists_affine_image_eq_eball_of_transBody"
 ],
 [
  "theorem",
  "eball_three"
 ],
 [
  "theorem",
  "isBodyGroup_fullAut3"
 ],
 [
  "theorem",
  "transBody_fullAut3"
 ],
 [
  "theorem",
  "not_transBody_flow"
 ],
 [
  "def",
  "refls3"
 ],
 [
  "theorem",
  "preservesBody_refls3"
 ],
 [
  "theorem",
  "boundaryTransitive_refls3"
 ],
 [
  "def",
  "square2"
 ],
 [
  "theorem",
  "mem_square2"
 ],
 [
  "theorem",
  "edgeMid_mem_square2"
 ],
 [
  "theorem",
  "isBoundaryState_square2_edgeMid"
 ],
 [
  "theorem",
  "edgeMid_not_extreme_square2"
 ],
 [
  "theorem",
  "not_boundaryTransitive_square2"
 ],
 [
  "def",
  "oct3"
 ],
 [
  "theorem",
  "mem_oct3"
 ],
 [
  "theorem",
  "oct3_convex"
 ],
 [
  "theorem",
  "oct3_isClosed"
 ],
 [
  "theorem",
  "oct3_subset_closedBall"
 ],
 [
  "theorem",
  "oct3_isCompact"
 ],
 [
  "theorem",
  "zero_mem_interior_oct3"
 ],
 [
  "theorem",
  "edgeMid_mem_oct3"
 ],
 [
  "theorem",
  "isBoundaryState_oct3_edgeMid"
 ],
 [
  "theorem",
  "edgeMid_not_extreme_oct3"
 ],
 [
  "theorem",
  "not_boundaryTransitive_oct3"
 ],
 [
  "theorem",
  "trb1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "norm_prepVec_le_one": "theorem norm_prepVec_le_one (x : Prep D) : ‖prepVec D x‖ ≤ 1",
 "body_subset_closedBall": "theorem body_subset_closedBall : body D ⊆ Metric.closedBall (0 : CSpace D) 1",
 "continuous_chart": "theorem continuous_chart : Continuous (chart C.L C.p0)",
 "chartBody_convex": "theorem chartBody_convex : Convex ℝ (chartBody C)",
 "chartBody_isClosed": "theorem chartBody_isClosed : IsClosed (chartBody C)",
 "chartBody_isBounded": "theorem chartBody_isBounded : Bornology.IsBounded (chartBody C)",
 "chartBody_isCompact": "theorem chartBody_isCompact : IsCompact (chartBody C)",
 "affineSpan_chartBody": "theorem affineSpan_chartBody : affineSpan ℝ (chartBody C) = ⊤",
 "chartBody_interior_nonempty": "theorem chartBody_interior_nonempty : (interior (chartBody C)).Nonempty",
 "frontier_of_isBoundaryState": "theorem frontier_of_isBoundaryState {Ω : Set V} {x : V} (hx : IsBoundaryState Ω x) :\n    x ∈ frontier Ω",
 "isBoundaryState_of_frontier": "theorem isBoundaryState_of_frontier {Ω : Set V} (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty)\n    {x : V} (hxΩ : x ∈ Ω) (hx : x ∉ interior Ω) : IsBoundaryState Ω x",
 "exists_boundary_ray": "theorem exists_boundary_ray {Ω : Set V} (hc : IsCompact Ω) (hconv : Convex ℝ Ω) {c : V}\n    (hci : c ∈ interior Ω) {u : V} (hu : u ≠ 0) :\n    ∃ t : ℝ, 0 < t ∧ c + t • u ∈ Ω ∧ (∀ s, t < s → c + s • u ∉ Ω) ∧\n      (∀ s, 0 ≤ s → s ≤ t → c + s • u ∈ Ω) ∧ IsBoundaryState Ω (c + t • u)",
 "IsBodyGroup": "structure IsBodyGroup (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop where\n  one_mem : AffineEquiv.refl ℝ V ∈ G\n  mul_mem : ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G\n  inv_mem : ∀ g ∈ G, g.symm ∈ G\n  preserves : ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω",
 "IsBodyGroup.preservesBody": "theorem IsBodyGroup.preservesBody {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (h : IsBodyGroup Ω G) :\n    PreservesBody Ω G",
 "TransBody": "def TransBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := IsBodyGroup Ω G ∧ BoundaryTransitive Ω G",
 "extreme_image": "theorem extreme_image {Ω : Set V} {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω) {x : V}\n    (hx : x ∈ Ω.extremePoints ℝ) : g x ∈ Ω.extremePoints ℝ",
 "not_mem_interior_of_extreme": "theorem not_mem_interior_of_extreme [Nontrivial V] {Ω : Set V} {x : V}\n    (hx : x ∈ Ω.extremePoints ℝ) : x ∉ interior Ω",
 "isBoundaryState_of_extreme": "theorem isBoundaryState_of_extreme [Nontrivial V] {Ω : Set V} (hconv : Convex ℝ Ω)\n    (hi : (interior Ω).Nonempty) {x : V} (hx : x ∈ Ω.extremePoints ℝ) : IsBoundaryState Ω x",
 "extreme_of_isBoundaryState_of_transitive": "theorem extreme_of_isBoundaryState_of_transitive [Nontrivial V] {Ω : Set V} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set (V ≃ᵃ[ℝ] V)}\n    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) {x : V} (hx : IsBoundaryState Ω x) :\n    x ∈ Ω.extremePoints ℝ",
 "not_boundaryTransitive_of_nonextreme_boundary": "theorem not_boundaryTransitive_of_nonextreme_boundary [Nontrivial V] {Ω : Set V} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {x : V} (hx : IsBoundaryState Ω x)\n    (hne : x ∉ Ω.extremePoints ℝ) (G : Set (V ≃ᵃ[ℝ] V)) (hG : PreservesBody Ω G) :\n    ¬ BoundaryTransitive Ω G",
 "qnorm": "noncomputable def qnorm (Ω : Set (Fin d → ℝ)) (v : Fin d → ℝ) : ℝ := v ⬝ᵥ (invMatrix Ω *ᵥ v)",
 "qBall": "def qBall (Ω : Set (Fin d → ℝ)) (R : ℝ) : Set (Fin d → ℝ) :=\n  {x | qnorm Ω (x - centroid Ω) ≤ R ^ 2}",
 "mem_qBall": "theorem mem_qBall {Ω : Set (Fin d → ℝ)} {R : ℝ} {x : Fin d → ℝ} :\n    x ∈ qBall Ω R ↔ qnorm Ω (x - centroid Ω) ≤ R ^ 2",
 "qnorm_smul": "theorem qnorm_smul (Ω : Set (Fin d → ℝ)) (t : ℝ) (v : Fin d → ℝ) :\n    qnorm Ω (t • v) = t ^ 2 * qnorm Ω v",
 "qnorm_zero": "theorem qnorm_zero (Ω : Set (Fin d → ℝ)) : qnorm Ω 0 = 0",
 "qnorm_pos": "theorem qnorm_pos {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)\n    {v : Fin d → ℝ} (hv : v ≠ 0) : 0 < qnorm Ω v",
 "qnorm_nonneg": "theorem qnorm_nonneg {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)\n    (v : Fin d → ℝ) : 0 ≤ qnorm Ω v",
 "image_eq_of_preservesBody": "theorem image_eq_of_preservesBody {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {Ω : Set V}\n    {G : Set (V ≃ᵃ[ℝ] V)} (hG : PreservesBody Ω G) {g : V ≃ᵃ[ℝ] V} (hg : g ∈ G) : g '' Ω = Ω",
 "centroid_fixed_of_preservesBody": "theorem centroid_fixed_of_preservesBody {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G)\n    {g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hg : g ∈ G) : g (centroid Ω) = centroid Ω",
 "qnorm_sub_centroid_apply": "theorem qnorm_sub_centroid_apply {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G)\n    {g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hg : g ∈ G) (x : Fin d → ℝ) :\n    qnorm Ω (g x - centroid Ω) = qnorm Ω (x - centroid Ω)",
 "boundary_qnorm_const": "theorem boundary_qnorm_const {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)\n    {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) :\n    ∃ R : ℝ, 0 ≤ R ∧ ∀ x, IsBoundaryState Ω x → qnorm Ω (x - centroid Ω) = R ^ 2",
 "centroid_mem": "theorem centroid_mem {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω)\n    (hi : (interior Ω).Nonempty) : centroid Ω ∈ Ω",
 "centroid_mem_interior": "theorem centroid_mem_interior (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : centroid Ω ∈ interior Ω",
 "eq_qBall_of_boundaryTransitive": "theorem eq_qBall_of_boundaryTransitive (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R",
 "eball": "def eball (d : ℕ) : Set (Fin d → ℝ) := {x | ∑ j, x j ^ 2 ≤ 1}",
 "mem_eball": "theorem mem_eball {x : Fin d → ℝ} : x ∈ eball d ↔ ∑ j, x j ^ 2 ≤ 1",
 "finsuppSum_eq_dot": "theorem finsuppSum_eq_dot (M : Matrix (Fin d) (Fin d) ℝ) (x : Fin d →₀ ℝ) :\n    (x.sum fun i xi => x.sum fun j xj => star xi * M i j * xj) = (⇑x) ⬝ᵥ (M *ᵥ ⇑x)",
 "invMatrix_posDef": "theorem invMatrix_posDef {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty) :\n    (invMatrix Ω).PosDef",
 "exists_factor_invMatrix": "theorem exists_factor_invMatrix {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hi : (interior Ω).Nonempty) : ∃ B : Matrix (Fin d) (Fin d) ℝ, Bᵀ * B = invMatrix Ω",
 "qnorm_eq_sum_sq": "theorem qnorm_eq_sum_sq {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty) :\n    ∃ T : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ), ∀ v, qnorm Ω v = ∑ j, (T v) j ^ 2",
 "exists_affine_image_eq_eball": "theorem exists_affine_image_eq_eball (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) :\n    ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d",
 "chartBody_eq_qBall": "theorem chartBody_eq_qBall (hd : 0 < C.d) {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :\n    ∃ R : ℝ, 0 < R ∧ chartBody C = qBall (chartBody C) R",
 "chartBody_eq_eball": "theorem chartBody_eq_eball (hd : 0 < C.d) {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :\n    ∃ A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ), A '' chartBody C = eball C.d",
 "eq_qBall_of_transBody": "theorem eq_qBall_of_transBody (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω)\n    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hT : TransBody Ω G) :\n    ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R",
 "exists_affine_image_eq_eball_of_transBody": "theorem exists_affine_image_eq_eball_of_transBody (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hT : TransBody Ω G) : ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d",
 "eball_three": "theorem eball_three : eball 3 = ball3",
 "isBodyGroup_fullAut3": "theorem isBodyGroup_fullAut3 : IsBodyGroup ball3 fullAut3 where\n  one_mem",
 "transBody_fullAut3": "theorem transBody_fullAut3 : TransBody ball3 fullAut3",
 "not_transBody_flow": "theorem not_transBody_flow : ¬ TransBody ball3 (Set.range rot3)",
 "refls3": "def refls3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) :=\n  {g | ∃ (dv : Fin 3 → ℝ) (k : ℝ) (hk : (dv 0 ^ 2 + dv 1 ^ 2 + dv 2 ^ 2) * k = 1), g = hh3 dv k hk} ∪\n    {AffineEquiv.refl ℝ (Fin 3 → ℝ)}",
 "preservesBody_refls3": "theorem preservesBody_refls3 : PreservesBody ball3 refls3",
 "boundaryTransitive_refls3": "theorem boundaryTransitive_refls3 : BoundaryTransitive ball3 refls3",
 "square2": "def square2 : Set (Fin 2 → ℝ) := Metric.closedBall (0 : Fin 2 → ℝ) 1",
 "mem_square2": "theorem mem_square2 {x : Fin 2 → ℝ} : x ∈ square2 ↔ ∀ i, |x i| ≤ 1",
 "edgeMid_mem_square2": "theorem edgeMid_mem_square2 : (![1, 0] : Fin 2 → ℝ) ∈ square2",
 "isBoundaryState_square2_edgeMid": "theorem isBoundaryState_square2_edgeMid : IsBoundaryState square2 ![1, 0]",
 "edgeMid_not_extreme_square2": "theorem edgeMid_not_extreme_square2 : (![1, 0] : Fin 2 → ℝ) ∉ square2.extremePoints ℝ",
 "not_boundaryTransitive_square2": "theorem not_boundaryTransitive_square2 (G : Set ((Fin 2 → ℝ) ≃ᵃ[ℝ] (Fin 2 → ℝ)))\n    (hG : PreservesBody square2 G) : ¬ BoundaryTransitive square2 G",
 "oct3": "def oct3 : Set (Fin 3 → ℝ) := {x | |x 0| + |x 1| + |x 2| ≤ 1}",
 "mem_oct3": "theorem mem_oct3 {x : Fin 3 → ℝ} : x ∈ oct3 ↔ |x 0| + |x 1| + |x 2| ≤ 1",
 "oct3_convex": "theorem oct3_convex : Convex ℝ oct3",
 "oct3_isClosed": "theorem oct3_isClosed : IsClosed oct3",
 "oct3_subset_closedBall": "theorem oct3_subset_closedBall : oct3 ⊆ Metric.closedBall (0 : Fin 3 → ℝ) 1",
 "oct3_isCompact": "theorem oct3_isCompact : IsCompact oct3",
 "zero_mem_interior_oct3": "theorem zero_mem_interior_oct3 : (0 : Fin 3 → ℝ) ∈ interior oct3",
 "edgeMid_mem_oct3": "theorem edgeMid_mem_oct3 : (![1 / 2, 1 / 2, 0] : Fin 3 → ℝ) ∈ oct3",
 "isBoundaryState_oct3_edgeMid": "theorem isBoundaryState_oct3_edgeMid : IsBoundaryState oct3 ![1 / 2, 1 / 2, 0]",
 "edgeMid_not_extreme_oct3": "theorem edgeMid_not_extreme_oct3 : (![1 / 2, 1 / 2, 0] : Fin 3 → ℝ) ∉ oct3.extremePoints ℝ",
 "not_boundaryTransitive_oct3": "theorem not_boundaryTransitive_oct3 (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)))\n    (hG : PreservesBody oct3 G) : ¬ BoundaryTransitive oct3 G",
 "trb1_core": "theorem trb1_core :\n    (∀ (D : DirectedStages) (C : CompletionChart D),\n      IsCompact (chartBody C) ∧ Convex ℝ (chartBody C) ∧ (interior (chartBody C)).Nonempty) ∧\n    (∀ (d : ℕ) (Ω : Set (Fin d → ℝ)) (x : Fin d → ℝ), IsBoundaryState Ω x → x ∈ frontier Ω) ∧\n    (∀ (d : ℕ) (Ω : Set (Fin d → ℝ)), Convex ℝ Ω → (interior Ω).Nonempty →\n      ∀ x, x ∈ Ω → x ∉ interior Ω → IsBoundaryState Ω x) ∧\n    (∀ (d : ℕ), 0 < d → ∀ (Ω : Set (Fin d → ℝ)), IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty →\n      ∀ G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)), PreservesBody Ω G → BoundaryTransitive Ω G →\n        ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R) ∧\n    (∀ (d : ℕ), 0 < d → ∀ (Ω : Set (Fin d → ℝ)), IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty →\n      ∀ G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)), PreservesBody Ω G → BoundaryTransitive Ω G →\n        ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d) ∧\n    TransBody ball3 fullAut3 ∧ BoundaryTransitive ball3 refls3 ∧ ¬ TransBody ball3 (Set.range rot3) ∧\n    (∀ G, PreservesBody square2 G → ¬ BoundaryTransitive square2 G) ∧\n    (∀ G, PreservesBody oct3 G → ¬ BoundaryTransitive oct3 G)"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.TransitiveBody.chartBody_isCompact",
 "OIBridge.TransitiveBody.chartBody_convex",
 "OIBridge.TransitiveBody.chartBody_interior_nonempty",
 "OIBridge.TransitiveBody.frontier_of_isBoundaryState",
 "OIBridge.TransitiveBody.isBoundaryState_of_frontier",
 "OIBridge.TransitiveBody.exists_boundary_ray",
 "OIBridge.TransitiveBody.extreme_of_isBoundaryState_of_transitive",
 "OIBridge.TransitiveBody.not_boundaryTransitive_of_nonextreme_boundary",
 "OIBridge.TransitiveBody.boundary_qnorm_const",
 "OIBridge.TransitiveBody.centroid_mem",
 "OIBridge.TransitiveBody.centroid_mem_interior",
 "OIBridge.TransitiveBody.eq_qBall_of_boundaryTransitive",
 "OIBridge.TransitiveBody.exists_factor_invMatrix",
 "OIBridge.TransitiveBody.qnorm_eq_sum_sq",
 "OIBridge.TransitiveBody.exists_affine_image_eq_eball",
 "OIBridge.TransitiveBody.chartBody_eq_qBall",
 "OIBridge.TransitiveBody.chartBody_eq_eball",
 "OIBridge.TransitiveBody.eq_qBall_of_transBody",
 "OIBridge.TransitiveBody.exists_affine_image_eq_eball_of_transBody",
 "OIBridge.TransitiveBody.eball_three",
 "OIBridge.TransitiveBody.transBody_fullAut3",
 "OIBridge.TransitiveBody.boundaryTransitive_refls3",
 "OIBridge.TransitiveBody.not_transBody_flow",
 "OIBridge.TransitiveBody.not_boundaryTransitive_square2",
 "OIBridge.TransitiveBody.not_boundaryTransitive_oct3",
 "OIBridge.TransitiveBody.trb1_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.CompletionAction\nimport OIBridge.InvariantInnerProduct\nimport Mathlib.Analysis.Convex.KreinMilman\nimport Mathlib.Analysis.Convex.Topology\nimport Mathlib.Analysis.Normed.Module.FiniteDimension\nimport Mathlib.LinearAlgebra.Matrix.PosDef\nimport Mathlib.Analysis.Matrix.LDL\n\nnamespace OIBridge\nnamespace TransitiveBody\n\nopen Set Topology Matrix MeasureTheory KInfFoundations OrbitGeneration OrbitNormalization\n  StageCompletion CompletionAction InvariantInnerProduct\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace TransitiveBody",
 "open Set Topology Matrix MeasureTheory KInfFoundations OrbitGeneration OrbitNormalization",
 "section Chart",
 "variable {D : DirectedStages} (C : CompletionChart D)",
 "end Chart",
 "section Bridge",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]",
 "end Bridge",
 "section Predicates",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]",
 "end Predicates",
 "section Purity",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]",
 "end Purity",
 "section QBall",
 "variable {d : ℕ}",
 "end QBall",
 "section Normalization",
 "variable {d : ℕ}",
 "end Normalization",
 "section Corollaries",
 "variable {D : DirectedStages} (C : CompletionChart D)",
 "variable {d : ℕ}",
 "end Corollaries",
 "section Controls",
 "end Controls",
 "end TransitiveBody",
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


def decl_texts(text):
    return {n: c for n, (_, c, _) in decl_chunks(text).items()}


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


PREFIX = 'OIBridge.TransitiveBody.'
QB, EB, NRM, FAC = ('eq_qBall_of_boundaryTransitive', 'exists_affine_image_eq_eball', 'qnorm_eq_sum_sq',
                    'exists_factor_invMatrix')
BR_TO, BR_FROM, RAY, SPH = ('frontier_of_isBoundaryState', 'isBoundaryState_of_frontier', 'exists_boundary_ray',
                            'boundary_qnorm_const')
TRANS, VERDICT, D3 = 'TransBody', 'trb1_core', 'eball_three'
CONTROL_THMS = ('transBody_fullAut3', 'boundaryTransitive_refls3', 'not_transBody_flow',
                'not_boundaryTransitive_square2', 'not_boundaryTransitive_oct3')
DIM3 = re.compile(r'ball3|Fin 3|finrank|square2|oct3|(?<![\w.])3(?![\w.])')
ORDER_TOKENS = ('InfiniteOrderOn', 'FiniteOrderOn', 'OrdInf', 'MulClosed', 'iterAfter', 'orderOf',
                'Function.iterate', '^[', 'Irrational', 'irrational', 'ordInf', 'infiniteOrder', 'finiteOrder')
BALL_HYPS = ('0 < d', 'IsCompact Ω', 'Convex ℝ Ω', '(interior Ω).Nonempty', 'PreservesBody Ω G',
             'BoundaryTransitive Ω G')
BALL_FORBIDDEN = ('IsBodyGroup', 'OrdInf', 'rot', 'SharpSeed', 'SeedOrbitAvailable', 'Drivab', 'flow', 'Flow',
                  'TransBody')
L3B = re.compile(r'L3B|hidden[- ]law|edge[- ]permutiv|\b[Rr]ank\b|leap[- ]rule|R_5|R_NL|R_LS|R_LL|κ')
AMBIENT = 'eq_closedBall_of_frontier_subset_sphere'


def control_names(mod):
    i = mod.find('\nsection Controls')
    j = mod.find('\nend Controls')
    if i == -1 or j == -1:
        return set()
    return {n for _, n in decls(mod[i:j])}


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ctrl = control_names(mod)
    # S1
    bad = [n for n, t in texts.items() if n not in ctrl and n not in (D3, VERDICT) and DIM3.search(t)]
    vt = texts.get(VERDICT, '')
    check('S1', 'no dimension outside the controls, eball_three and the verdict%s%s'
          % (tag, (' %s' % bad[:3]) if bad else ''),
          not bad and vt.count('(∀ (d : ℕ), 0 < d → ∀ (Ω : Set (Fin d → ℝ)), IsCompact Ω → Convex ℝ Ω →') == 2)
    # S2
    hits = [t for t in ORDER_TOKENS if t in mod]
    check('S2', 'no order predicate, no TRANS → ORD∞ edge%s%s' % (tag, (' %s' % hits[:3]) if hits else ''),
          not hits and 'Mathlib.Analysis.Real.Pi.Irrational' not in mod
          and norm(texts.get(TRANS, '')).endswith(': Prop := IsBodyGroup Ω G ∧ BoundaryTransitive Ω G'))
    # S3
    ok3 = True
    for n in (QB, EB):
        t = texts.get(n, '')
        b, c = split_statement(t) if t else ('', '')
        ok3 = ok3 and kinds.get(n) == 'theorem' and all(h in b for h in BALL_HYPS) \
            and not any(f in b for f in BALL_FORBIDDEN)
    check('S3', 'the ball theorems carry exactly the frozen hypothesis set' + tag, ok3)
    # S4
    t1, t2 = texts.get(BR_TO, ''), texts.get(BR_FROM, '')
    b1, c1 = split_statement(t1) if t1 else ('', '')
    b2, c2 = split_statement(t2) if t2 else ('', '')
    bicond = [n for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma') and '↔' in t
              and 'IsBoundaryState' in t and 'frontier' in t]
    check('S4', 'the bridge is two directional theorems, no biconditional' + tag,
          kinds.get(BR_TO) == 'theorem' and 'IsBoundaryState Ω x' in b1 and norm(c1) == 'x ∈ frontier Ω'
          and kinds.get(BR_FROM) == 'theorem' and 'x ∉ interior Ω' in b2 and '(interior Ω).Nonempty' in b2
          and norm(c2) == 'IsBoundaryState Ω x' and not bicond)
    # S5
    defs = [t for n, t in texts.items() if kinds.get(n) not in ('theorem', 'lemma')]
    trans_tokens = set(tok for t in defs for tok in re.findall(r'\w*Transitive\w*', t))
    check('S5', 'the only transitivity predicate is BoundaryTransitive, over all boundary states' + tag,
          trans_tokens <= {'BoundaryTransitive'} and 'BoundaryTransitive Ω G' in texts.get(TRANS, '')
          and not any(re.search(r'extremePoints|Finset|\bFinite\b|\.Finite', t) for t in defs))
    # S6
    cn = split_statement(texts[NRM])[1] if NRM in texts else ''
    ce = split_statement(texts[EB])[1] if EB in texts else ''
    cf = split_statement(texts[FAC])[1] if FAC in texts else ''
    check('S6', 'the normalization adapter is frozen as statements with prints' + tag,
          kinds.get(NRM) == 'theorem' and PREFIX + NRM in prints
          and norm(cn) == '∃ T : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ), ∀ v, qnorm Ω v = ∑ j, (T v) j ^ 2'
          and kinds.get(EB) == 'theorem' and PREFIX + EB in prints
          and norm(ce) == '∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A \'\' Ω = eball d'
          and kinds.get(FAC) == 'theorem' and PREFIX + FAC in prints
          and norm(cf) == '∃ B : Matrix (Fin d) (Fin d) ℝ, Bᵀ * B = invMatrix Ω')
    # S7
    check('S7', 'the transitivity-side controls and polytope exclusions are kernel theorems with prints' + tag,
          all(kinds.get(n) == 'theorem' and PREFIX + n in prints for n in CONTROL_THMS))
    # S8
    m8 = L3B.search(mod)
    check('S8', 'no L3B vocabulary%s%s' % (tag, (' (%r)' % m8.group(0)) if m8 else ''), m8 is None)
    # S9
    proof = chunks.get(QB, ('', '', ''))[2]
    check('S9', 'the ball theorem goes through the ray argument, not an ambient-norm lemma' + tag,
          AMBIENT not in mod and RAY in proof and SPH in proof)


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context line unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    chunks = decl_chunks(mod)
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s' % (tag, (' (changed: %s)' % ', '.join(bad[:4]))
                                                                        if bad else ''), not bad)
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
    must_fail('N2', 'a changed binder context', replace_once(mod, CONTEXT[-3], CONTEXT[-3] + ' -- x\nopen Real'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, '∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R', '∃ R : ℝ, 0 ≤ R ∧ Ω = qBall Ω R'))
    must_fail('N3', 'a sorry', append_decl(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('S1', 'a 3 in the ball theorem',
              replace_once(mod, 'theorem eq_qBall_of_boundaryTransitive (hd : 0 < d) {Ω : Set (Fin d → ℝ)}',
                           'theorem eq_qBall_of_boundaryTransitive (hd : 0 < d) {Ω : Set (Fin 3 → ℝ)}'))
    must_fail('S2', 'an order predicate and a TRANS → ORD∞ theorem',
              append_decl(mod, 'def OrdInf (Ω : Set (Fin 3 → ℝ)) (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) : Prop :=\n'
                               '  ∃ g ∈ G, ∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x\n'
                               'theorem ordInf_of_transBody (Ω : Set (Fin 3 → ℝ)) (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)))\n'
                               '    (h : TransBody Ω G) : OrdInf Ω G := by\n  exact absurd h h'))
    must_fail('S3', 'a group hypothesis on the ball theorem',
              replace_once(mod, '(hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R',
                           '(hbg : IsBodyGroup Ω G) (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) :\n'
                           '    ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R'))
    must_fail('S4', 'the frontier-to-boundary direction removed',
              replace_once(mod, 'theorem isBoundaryState_of_frontier', 'theorem isBoundaryState_of_frontier2'))
    must_fail('S5', 'transitivity on extreme points',
              replace_once(mod, 'IsBodyGroup Ω G ∧ BoundaryTransitive Ω G',
                           'IsBodyGroup Ω G ∧ ∀ x ∈ Ω.extremePoints ℝ, ∀ y ∈ Ω.extremePoints ℝ, ∃ g ∈ G, g x = y'))
    must_fail('S6', 'the normalization weakened to an inequality',
              replace_once(mod, '∀ v, qnorm Ω v = ∑ j, (T v) j ^ 2', '∀ v, qnorm Ω v ≤ ∑ j, (T v) j ^ 2'))
    must_fail('S7', 'a control print removed',
              replace_once(mod, '#print axioms OIBridge.TransitiveBody.boundaryTransitive_refls3\n', ''))
    must_fail('S8', 'L3B named', append_decl(mod, '-- selector evidence from L3B: rank 4'))
    must_fail('S9', 'the ambient-norm identifier mentioned',
              append_decl(mod, '-- compare KInfFoundations.' + AMBIENT))
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
