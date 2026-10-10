#!/usr/bin/env python3
"""controls.py -- round KTRANS-DENSE-1's own contracts, FROZEN with the preregistration beside it.

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
  S1  definition  `DenseBoundaryOrbit` has the effective header of the landed `BoundaryTransitive` read from D and the
                  same body with exactly its last clause `∃ g ∈ G, g x = y` replaced by membership of `y` in the
                  closure of the orbit `(fun g => g x) '' G`
  S2  pairing     for each of the eleven frozen pairs, the landed theorem read from D has exactly one
                  `BoundaryTransitive` in its effective statement (its section variables that the statement uses,
                  then its own binders and conclusion), and the dense theorem's effective statement is that text with
                  `BoundaryTransitive` replaced by `DenseBoundaryOrbit` and nothing else; the dense statement does not
                  mention `BoundaryTransitive`
  S3  resolution  every identifier of a paired effective statement that names an OIBridge declaration resolves, in
                  the dense module's namespace context, to the same unique declaration as in the landed module's
                  context (inventory read from D and the module under check)
  S4  strict      the weakening `denseBoundaryOrbit_of_boundaryTransitive` and the strictness witness have their
                  frozen binders and conclusions; `ratRefl` is the frozen definition; the non-transitivity is proved
                  through EFF-1's `not_boundaryTransitive_of_countable`, read from D with its frozen statement
  S5  scope       no statement mentions an exact-existence or uncovered object (the sharp family, the full effect set,
                  the mixing closure, supporting-effect completeness, K-infinity-1, the Lorentz bridge, extreme points);
                  `ratRefl` occurs only in §D
  S6  reuse       no declaration of the module shares its name with an OIBridge declaration visible to it; the only
                  import is `OIBridge.K2Guard`
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  separation  no declaration of §B mentions a cone or selector object; no declaration of §B or §C mentions
                  `ratRefl`
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements and the landed statements at D by its own frozen
                  rule, independently of the others; at a commit carrying the result note, the note states exactly the
                  computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.SharpTests`
  C   census      the census is D's with exactly the frozen family inserted after the K1-SHARP-TESTS-1 family, byte for
                  byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '06b6f94e479bc19a28979c72316823cbdd0fb62b'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-ktrans-dense-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = LEAN + 'DenseOrbit.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '466a80f7ec2fa8089be59760f5c26e5d37a09973'
ANCHOR_IMPORT = 'import OIBridge.SharpTests\n'
NEW_IMPORT = 'import OIBridge.DenseOrbit\n'
PREV_FAMILY_MODULES = ['SharpTests']
CENSUS_FAMILY = json.loads(r'''{
 "name": "the ball, cone and selector consumers of K∞-Trans under a dense boundary orbit: TRB-1's ball identification, EFF-1's cone equality and the relative selectors of K1-BRIDGE-1 and K2-GUARD-1 hold with DenseBoundaryOrbit in place of BoundaryTransitive, a strictly weaker hypothesis (round KTRANS-DENSE-1, reconstruction)",
 "modules": [
  "DenseOrbit"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round KTRANS-DENSE-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-ktrans-dense-1/preregistration.md. DenseBoundaryOrbit Ω G is OG-1's BoundaryTransitive with its last clause, a member of G carrying x to y, replaced by y lying in the closure of the orbit of x under G. Q-BALL: TRB-1's boundary_qnorm_const, centroid_mem_interior, eq_qBall_of_boundaryTransitive, exists_affine_image_eq_eball and chartBody_eq_eball hold with DenseBoundaryOrbit in place of BoundaryTransitive and no other change (the *_of_dense theorems). Q-CONE: EFF-1's maxConeOf_avail_eq, K1-BRIDGE-1's nativeGate_of_avail, entangling_of_avail, dim_of_nativeGateOf and three_of_nativeGateOf, and K2-GUARD-1's three_of_nativeGateOf_of_two_le hold with the same single replacement (maxConeOf_avail_eq_of_dense and the *_dense theorems). Q-STRICT: boundary transitivity implies a dense boundary orbit (denseBoundaryOrbit_of_boundaryTransitive); the identity with the reflections in hyperplanes orthogonal to nonzero rational vectors (ratRefl) is countable, preserves eball d and has a dense boundary orbit on it (denseBoundaryOrbit_ratRefl), is not boundary transitive on eball 3 by EFF-1's not_boundaryTransitive_of_countable (not_boundaryTransitive_ratRefl), and its countable seed orbit determines maxCone (eball 3) (countable_seedOrbit_cone). Carried by no manuscript. The statements that need a specific effect to exist exactly (EFF-1's sharpFamily_subset_avail, seedOrbit_eq_sharpFamily, fullEffects_subset_avail and avail_eq_fullEffects; OG-1's supporting-effect completeness, seedOrbit_ball3_eq and kInf1_ball3_of_orbit), OG-1's lorentz_of_seedOrbit and lorentz_of_available, and TRB-1's extreme_of_isBoundaryState_of_transitive keep exact boundary transitivity. ratRefl is a control and not a family of operations; nothing here sources a dense boundary orbit, K∞-Trans or any other hypothesis, or concerns whether the composite cone is closed."
}''')
DECLS = json.loads(r'''[
 [
  "def",
  "DenseBoundaryOrbit"
 ],
 [
  "theorem",
  "denseBoundaryOrbit_of_boundaryTransitive"
 ],
 [
  "theorem",
  "continuous_qnorm_sub"
 ],
 [
  "theorem",
  "boundary_qnorm_const_of_dense"
 ],
 [
  "theorem",
  "centroid_mem_interior_of_dense"
 ],
 [
  "theorem",
  "eq_qBall_of_dense"
 ],
 [
  "theorem",
  "exists_affine_image_eq_eball_of_dense"
 ],
 [
  "theorem",
  "chartBody_eq_eball_of_dense"
 ],
 [
  "theorem",
  "continuous_sharpVec_apply"
 ],
 [
  "theorem",
  "continuous_pairVal_sharp"
 ],
 [
  "theorem",
  "maxConeOf_avail_eq_of_dense"
 ],
 [
  "theorem",
  "nativeGate_of_avail_dense"
 ],
 [
  "theorem",
  "entangling_of_avail_dense"
 ],
 [
  "theorem",
  "dim_of_nativeGateOf_dense"
 ],
 [
  "theorem",
  "three_of_nativeGateOf_dense"
 ],
 [
  "theorem",
  "three_of_nativeGateOf_of_two_le_dense"
 ],
 [
  "theorem",
  "exists_rat_near"
 ],
 [
  "noncomputable def",
  "ratRefl"
 ],
 [
  "theorem",
  "countable_ratRefl"
 ],
 [
  "theorem",
  "ratRefl_subset_fullAut"
 ],
 [
  "theorem",
  "preservesBody_ratRefl"
 ],
 [
  "theorem",
  "denseBoundaryOrbit_ratRefl"
 ],
 [
  "theorem",
  "not_boundaryTransitive_ratRefl"
 ],
 [
  "theorem",
  "countable_seedOrbit_cone"
 ]
]''')
TEXTS = json.loads(r'''{
 "DenseBoundaryOrbit": "def DenseBoundaryOrbit {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (Ω : Set V)\n    (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=\n  ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) '' G)",
 "denseBoundaryOrbit_of_boundaryTransitive": "theorem denseBoundaryOrbit_of_boundaryTransitive {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]\n    {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hT : BoundaryTransitive Ω G) : DenseBoundaryOrbit Ω G",
 "continuous_qnorm_sub": "theorem continuous_qnorm_sub (Ω : Set (Fin d → ℝ)) (c : Fin d → ℝ) :\n    Continuous fun z : Fin d → ℝ => qnorm Ω (z - c)",
 "boundary_qnorm_const_of_dense": "theorem boundary_qnorm_const_of_dense {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) :\n    ∃ R : ℝ, 0 ≤ R ∧ ∀ x, IsBoundaryState Ω x → qnorm Ω (x - centroid Ω) = R ^ 2",
 "centroid_mem_interior_of_dense": "theorem centroid_mem_interior_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) : centroid Ω ∈ interior Ω",
 "eq_qBall_of_dense": "theorem eq_qBall_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R",
 "exists_affine_image_eq_eball_of_dense": "theorem exists_affine_image_eq_eball_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) :\n    ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d",
 "chartBody_eq_eball_of_dense": "theorem chartBody_eq_eball_of_dense {D : DirectedStages} (C : CompletionChart D) (hd : 0 < C.d)\n    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) :\n    ∃ A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ), A '' chartBody C = eball C.d",
 "continuous_sharpVec_apply": "theorem continuous_sharpVec_apply (μ : Fin (d + 1)) :\n    Continuous fun x : Fin d → ℝ => sharpVec x μ",
 "continuous_pairVal_sharp": "theorem continuous_pairVal_sharp (ω : W d) :\n    Continuous fun p : (Fin d → ℝ) × (Fin d → ℝ) => pairVal (sharpVec p.1) (sharpVec p.2) ω",
 "maxConeOf_avail_eq_of_dense": "theorem maxConeOf_avail_eq_of_dense (hd : 0 < d) (hG : PreservesBody (eball d) G)\n    (hP1 : SharpSeed (eball d) r) (hK : DenseBoundaryOrbit (eball d) G)\n    (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) :\n    maxConeOf avail = maxCone (eball d)",
 "nativeGate_of_avail_dense": "theorem nativeGate_of_avail_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hT : NativeGateOf (eball d) avail z N T) : NativeGate (eball d) z N T",
 "entangling_of_avail_dense": "theorem entangling_of_avail_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {T : W d ≃ₗ[ℝ] W d} (hEnt : EntanglingOf (eball d) avail T) : Entangling (eball d) T",
 "dim_of_nativeGateOf_dense": "theorem dim_of_nativeGateOf_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3",
 "three_of_nativeGateOf_dense": "theorem three_of_nativeGateOf_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)\n    (hEnt : EntanglingOf (eball d) avail T) : d = 3",
 "three_of_nativeGateOf_of_two_le_dense": "theorem three_of_nativeGateOf_of_two_le_dense (hd : 2 ≤ d) (hE : EffectsOn (eball d) avail)\n    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3",
 "exists_rat_near": "theorem exists_rat_near (m : Fin d → ℝ) {δ : ℝ} (hδ : 0 < δ) :\n    ∃ q : Fin d → ℚ, dist (fun j => (q j : ℝ)) m < δ",
 "ratRefl": "noncomputable def ratRefl (d : ℕ) : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)) :=\n  insert (AffineEquiv.refl ℝ (Fin d → ℝ))\n    (Set.range fun q : {q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0} =>\n      @reflAff d (fun j => (q.1 j : ℝ)) q.2)",
 "countable_ratRefl": "theorem countable_ratRefl : (ratRefl d).Countable",
 "ratRefl_subset_fullAut": "theorem ratRefl_subset_fullAut : ratRefl d ⊆ fullAut d",
 "preservesBody_ratRefl": "theorem preservesBody_ratRefl : PreservesBody (eball d) (ratRefl d)",
 "denseBoundaryOrbit_ratRefl": "theorem denseBoundaryOrbit_ratRefl : DenseBoundaryOrbit (eball d) (ratRefl d)",
 "not_boundaryTransitive_ratRefl": "theorem not_boundaryTransitive_ratRefl : ¬ BoundaryTransitive (eball 3) (ratRefl 3)",
 "countable_seedOrbit_cone": "theorem countable_seedOrbit_cone :\n    (seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))).Countable ∧\n      maxConeOf (seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))) =\n        maxCone (eball 3)"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.DenseOrbit.denseBoundaryOrbit_of_boundaryTransitive",
 "OIBridge.DenseOrbit.boundary_qnorm_const_of_dense",
 "OIBridge.DenseOrbit.centroid_mem_interior_of_dense",
 "OIBridge.DenseOrbit.eq_qBall_of_dense",
 "OIBridge.DenseOrbit.exists_affine_image_eq_eball_of_dense",
 "OIBridge.DenseOrbit.chartBody_eq_eball_of_dense",
 "OIBridge.DenseOrbit.maxConeOf_avail_eq_of_dense",
 "OIBridge.DenseOrbit.nativeGate_of_avail_dense",
 "OIBridge.DenseOrbit.entangling_of_avail_dense",
 "OIBridge.DenseOrbit.dim_of_nativeGateOf_dense",
 "OIBridge.DenseOrbit.three_of_nativeGateOf_dense",
 "OIBridge.DenseOrbit.three_of_nativeGateOf_of_two_le_dense",
 "OIBridge.DenseOrbit.denseBoundaryOrbit_ratRefl",
 "OIBridge.DenseOrbit.not_boundaryTransitive_ratRefl",
 "OIBridge.DenseOrbit.countable_seedOrbit_cone"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.K2Guard\n\nnamespace OIBridge\nnamespace DenseOrbit\n\nopen Set Topology Matrix KInfFoundations OrbitGeneration OrbitNormalization StageCompletion\n  CompletionAction InvariantInnerProduct TransitiveBody CompositeDimension CompositeInterface\nopen EffectSpace K1Bridge K2Guard\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace DenseOrbit",
 "open Set Topology Matrix KInfFoundations OrbitGeneration OrbitNormalization StageCompletion",
 "open EffectSpace K1Bridge K2Guard",
 "section Ball",
 "variable {d : ℕ}",
 "end Ball",
 "section Cone",
 "variable {d : ℕ}",
 "variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}\n  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}",
 "end Cone",
 "section Strict",
 "variable {d : ℕ}",
 "end Strict",
 "end DenseOrbit",
 "end OIBridge"
]''')
LANDED = json.loads(r'''{
 "boundary_qnorm_const": "{d : ℕ} {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ R : ℝ, 0 ≤ R ∧ ∀ x, IsBoundaryState Ω x → qnorm Ω (x - centroid Ω) = R ^ 2",
 "centroid_mem_interior": "{d : ℕ} (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : centroid Ω ∈ interior Ω",
 "eq_qBall_of_boundaryTransitive": "{d : ℕ} (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R",
 "exists_affine_image_eq_eball": "{d : ℕ} (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d",
 "chartBody_eq_eball": "{D : DirectedStages} (C : CompletionChart D) (hd : 0 < C.d) {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))} (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) : ∃ A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ), A '' chartBody C = eball C.d",
 "maxConeOf_avail_eq": "{d : ℕ} {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 0 < d) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) : maxConeOf avail = maxCone (eball d)",
 "nativeGate_of_avail": "{d : ℕ} {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 0 < d) (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d} (hT : NativeGateOf (eball d) avail z N T) : NativeGate (eball d) z N T",
 "entangling_of_avail": "{d : ℕ} {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 0 < d) (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) {T : W d ≃ₗ[ℝ] W d} (hEnt : EntanglingOf (eball d) avail T) : Entangling (eball d) T",
 "dim_of_nativeGateOf": "{d : ℕ} {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 0 < d) (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3",
 "three_of_nativeGateOf": "{d : ℕ} {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 0 < d) (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) (hEnt : EntanglingOf (eball d) avail T) : d = 3",
 "three_of_nativeGateOf_of_two_le": "{d : ℕ} {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 2 ≤ d) (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3",
 "not_boundaryTransitive_of_countable": "{G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} (hG : G.Countable) : ¬ BoundaryTransitive (eball 3) G",
 "BoundaryTransitive#head": "{V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop",
 "BoundaryTransitive#body": "∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y"
}''')
N_PRINTS = 15
DECL = re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure'
                  r'|instance)\s+(\S+)', re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
FAILS, COUNT = [], [0]

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

PREFIX = 'OIBridge.DenseOrbit.'
DEF = 'DenseBoundaryOrbit'
LANDED_DEF = ('OrbitGeneration', 'BoundaryTransitive')
LAST_CLAUSE = '∃ g ∈ G, g x = y'
DENSE_CLAUSE = 'y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)'
# S2 -- the frozen pairs: dense name -> (landed module, landed name)
BALL_PAIRS = {
    'boundary_qnorm_const_of_dense': ('TransitiveBody', 'boundary_qnorm_const'),
    'centroid_mem_interior_of_dense': ('TransitiveBody', 'centroid_mem_interior'),
    'eq_qBall_of_dense': ('TransitiveBody', 'eq_qBall_of_boundaryTransitive'),
    'exists_affine_image_eq_eball_of_dense': ('TransitiveBody', 'exists_affine_image_eq_eball'),
    'chartBody_eq_eball_of_dense': ('TransitiveBody', 'chartBody_eq_eball'),
}
CONE_PAIRS = {
    'maxConeOf_avail_eq_of_dense': ('EffectSpace', 'maxConeOf_avail_eq'),
    'nativeGate_of_avail_dense': ('K1Bridge', 'nativeGate_of_avail'),
    'entangling_of_avail_dense': ('K1Bridge', 'entangling_of_avail'),
    'dim_of_nativeGateOf_dense': ('K1Bridge', 'dim_of_nativeGateOf'),
    'three_of_nativeGateOf_dense': ('K1Bridge', 'three_of_nativeGateOf'),
    'three_of_nativeGateOf_of_two_le_dense': ('K2Guard', 'three_of_nativeGateOf_of_two_le'),
}
PAIRS = dict(BALL_PAIRS, **CONE_PAIRS)
BALL_PRINTED = ('boundary_qnorm_const_of_dense', 'centroid_mem_interior_of_dense', 'eq_qBall_of_dense',
                'exists_affine_image_eq_eball_of_dense', 'chartBody_eq_eball_of_dense')
CONE_PRINTED = tuple(CONE_PAIRS)
# S4 -- the weakening and the strictness witness
WEAK = 'denseBoundaryOrbit_of_boundaryTransitive'
WEAK_BINDERS = ('{V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} '
                '(hT : BoundaryTransitive Ω G)')
WEAK_CONCL = 'DenseBoundaryOrbit Ω G'
FAMILY = 'ratRefl'
FAMILY_BODY = ('insert (AffineEquiv.refl ℝ (Fin d → ℝ)) (Set.range fun q : {q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0} '
               '=> @reflAff d (fun j => (q.1 j : ℝ)) q.2)')
STRICT = {
    'countable_ratRefl': ('', '(ratRefl d).Countable', ()),
    'ratRefl_subset_fullAut': ('', 'ratRefl d ⊆ fullAut d', ()),
    'preservesBody_ratRefl': ('', 'PreservesBody (eball d) (ratRefl d)', ()),
    'denseBoundaryOrbit_ratRefl': ('', 'DenseBoundaryOrbit (eball d) (ratRefl d)', ()),
    'not_boundaryTransitive_ratRefl': ('', '¬ BoundaryTransitive (eball 3) (ratRefl 3)',
                                       ('not_boundaryTransitive_of_countable', 'countable_ratRefl')),
    'countable_seedOrbit_cone': ('', '(seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))).Countable ∧ '
                                     'maxConeOf (seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))) = '
                                     'maxCone (eball 3)', ('countable_ratRefl', 'denseBoundaryOrbit_ratRefl')),
}
STRICT_PRINTED = (WEAK, 'denseBoundaryOrbit_ratRefl', 'not_boundaryTransitive_ratRefl', 'countable_seedOrbit_cone')
NOGO = ('EffectSpace', 'not_boundaryTransitive_of_countable')
NOGO_STMT = ('{G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} (hG : G.Countable) : ¬ BoundaryTransitive (eball 3) G')
# S5 -- scope
SCOPE_TOKENS = ('sharpFamily', 'sharpUnitFamily', 'fullEffects', 'MixingClosed', 'unitEff', 'SupportingEffectComplete',
                'KInf1', 'CoversBoundaryFrom', 'conePair', 'ballEffect', 'ball3', 'extremePoints', 'Lorentz',
                'lorentz_of_effects', 'lorentz_of_seedOrbit', 'lorentz_of_available',
                'extreme_of_isBoundaryState_of_transitive')
# S6 -- reuse
IMPORT_ONLY = 'import OIBridge.K2Guard'
# S7 -- phrases
PHRASES = ('closure of operations', 'operation closure', 'closed under operations', 'operationally closed',
           'closedness of operations', 'closed set of operations', 'OI supplies', 'supplied by OI', 'OI provides',
           'provided by OI', 'derived from OI', 'sourced from OI', 'StageCompletion supplies',
           'the observer architecture supplies', 'K∞-Trans is derived', 'K∞-Trans is sourced', 'replaces K∞-Trans',
           'K∞-Trans is not needed', 'K∞-Trans is unnecessary', 'eliminates K∞-Trans', 'K∞-Trans is redundant',
           'every consumer', 'all consumers', 'all of K∞-Trans', 'composite closedness', 'closedness of the composite',
           'closed composite', 'adopted operation', 'operations are rational', 'physical operations',
           'premise adopted', 'adopts a premise', 'qubit', 'design (round', 'not for landing')
# S8 -- separation
CONE_OBJECTS = ('maxCone', 'maxConeOf', 'NativeGate', 'NativeGateOf', 'Entangling', 'EntanglingOf', 'IsNot',
                'SeedOrbitAvailable', 'SharpSeed', 'EffectsOn', 'sharpEff', 'seedOrbit', 'W')
# V -- the frozen decision rule
BALL_TOKENS = ('KTRANS-DENSE-BALL-PROVED', 'KTRANS-DENSE-BALL-NOT-ESTABLISHED')
CONE_TOKENS = ('KTRANS-DENSE-CONE-PROVED', 'KTRANS-DENSE-CONE-NOT-ESTABLISHED')
STRICT_TOKENS = ('KTRANS-DENSE-STRICTLY-WEAKER', 'KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED')
ALL_TOKENS = BALL_TOKENS + CONE_TOKENS + STRICT_TOKENS
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


def pair_ok(mod, landed, dname, lname):
    """The dense effective statement is the landed one with BoundaryTransitive replaced, and nothing else."""
    de = effective(mod, dname)
    le = landed.get(lname)
    if de is None or le is None:
        return False
    if len(re.findall(r'(?<![\w.\'])BoundaryTransitive(?![\w\'])', le)) != 1 or token('BoundaryTransitive', de):
        return False
    return de == re.sub(r'(?<![\w.\'])BoundaryTransitive(?![\w\'])', DEF, le)


def resolution_bad(mod, dname, lmod_text, lname, names, spaces):
    """The OIBridge identifiers of the pair resolving differently in the two contexts, or ambiguously."""
    bad = []
    de = effective(mod, dname)
    if de is None:
        return [dname]
    dsc = scopes_at(mod).get(dname, ([], [], []))
    lsc = scopes_at(lmod_text).get(lname, ([], [], [])) if lmod_text else ([], [], [])
    dvis, lvis = visible(dsc[1], dsc[2], spaces), visible(lsc[1], lsc[2], spaces)
    le = effective(lmod_text, lname) if lmod_text else None
    if le is None or resolve('BoundaryTransitive', lvis, names) != ['OIBridge.%s.BoundaryTransitive' % LANDED_DEF[0]]:
        bad.append('BoundaryTransitive')
    for t in sorted(set(strip_binders(de))):
        a, b = resolve(t, dvis, names), resolve(t, lvis, names)
        if t == DEF:
            if a != [PREFIX + DEF]:
                bad.append(t)
            continue
        if len(a) > 1 or a != b:
            bad.append(t)
    return bad


def def_ok(mod, landed):
    """DenseBoundaryOrbit: the landed BoundaryTransitive's effective header, its body with the last clause replaced."""
    eff = effective(mod, DEF)
    chunks = decl_chunks(mod)
    if eff is None or chunks.get(DEF, ('',))[0] != 'def':
        return False
    lhead, lbody = landed.get(LANDED_DEF[1] + '#head'), landed.get(LANDED_DEF[1] + '#body')
    body = def_body(chunks[DEF][1])
    hd = norm(def_header(chunks[DEF][1]))
    hd = hd[hd.index(DEF) + len(DEF):]
    return lhead is not None and lbody is not None and norm(hd) == lhead and lbody.endswith(LAST_CLAUSE) and \
        body == lbody[:-len(LAST_CLAUSE)] + DENSE_CLAUSE


def weak_ok(texts, kinds):
    bb, cc = stmt_parts(texts, WEAK)
    return kinds.get(WEAK) == 'theorem' and bb == norm(WEAK_BINDERS) and cc == norm(WEAK_CONCL)


def strict_bad(chunks, landed):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    bad = []
    if kinds.get(FAMILY) != 'noncomputable def' or def_body(texts.get(FAMILY, '')) != norm(FAMILY_BODY):
        bad.append(FAMILY)
    for n, (b, c, deps) in STRICT.items():
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or re.sub(r'\{[^{}]*\}', ' ', bb).strip() != b or cc != norm(c) or \
                not all(token(m, proofs.get(n, '')) for m in deps):
            bad.append(n)
    if landed.get(NOGO[1]) != norm(NOGO_STMT):
        bad.append(NOGO[1] + ' at D')
    return bad


def landed_texts(show_d):
    """The landed effective statements the rules read, from D."""
    out = {}
    cache = {}
    for m, n in list(PAIRS.values()) + [NOGO]:
        if m not in cache:
            cache[m] = show_d(LEAN + m + '.lean')
        t = cache[m]
        e = effective(t, n) if t else None
        if e is not None:
            out[n] = e
    t = show_d(LEAN + LANDED_DEF[0] + '.lean')
    if t:
        ch = decl_chunks(t).get(LANDED_DEF[1])
        if ch and ch[0] == 'def':
            vs = scopes_at(t).get(LANDED_DEF[1], ([], [], []))[0]
            hd = norm(def_header(ch[1]))
            hd = hd[hd.index(LANDED_DEF[1]) + len(LANDED_DEF[1]):]
            inst = [g for g in vs]
            out[LANDED_DEF[1] + '#head'] = norm(' '.join(inst) + ' ' + hd)
            out[LANDED_DEF[1] + '#body'] = def_body(ch[1])
    return out


def ball_cell(mod, landed):
    """KTRANS-DENSE-BALL-PROVED iff: `DenseBoundaryOrbit` is the landed `BoundaryTransitive` with its last clause
    replaced by orbit-closure membership (S1); the weakening has its frozen binders and conclusion; and each of the
    five TRB-1 pairs pairs with its landed theorem read from D (S2). Otherwise KTRANS-DENSE-BALL-NOT-ESTABLISHED.
    Reads no cone or strictness statement."""
    chunks = decl_chunks(mod)
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = def_ok(mod, landed) and weak_ok(texts, kinds)
    for d, (m, l) in BALL_PAIRS.items():
        ok = ok and kinds.get(d) == 'theorem' and pair_ok(mod, landed, d, l)
    return [BALL_TOKENS[0] if ok else BALL_TOKENS[1]]


def cone_cell(mod, landed):
    """KTRANS-DENSE-CONE-PROVED iff: `DenseBoundaryOrbit` passes S1, and each of the six cone and selector pairs pairs
    with its landed theorem read from D (S2). Otherwise KTRANS-DENSE-CONE-NOT-ESTABLISHED. Reads no ball or strictness
    statement."""
    chunks = decl_chunks(mod)
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    ok = def_ok(mod, landed)
    for d, (m, l) in CONE_PAIRS.items():
        ok = ok and kinds.get(d) == 'theorem' and pair_ok(mod, landed, d, l)
    return [CONE_TOKENS[0] if ok else CONE_TOKENS[1]]


def strict_cell(mod, landed):
    """KTRANS-DENSE-STRICTLY-WEAKER iff: `DenseBoundaryOrbit` passes S1; the weakening (boundary transitivity implies a
    dense boundary orbit) has its frozen binders and conclusion; `ratRefl` is the frozen definition; and the
    strictness theorems have their frozen conclusions, the non-transitivity proved through EFF-1's
    `not_boundaryTransitive_of_countable` with its frozen statement at D. Otherwise
    KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED. Reads no paired statement."""
    chunks = decl_chunks(mod)
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = def_ok(mod, landed) and weak_ok(texts, kinds) and not strict_bad(chunks, landed)
    return [STRICT_TOKENS[0] if ok else STRICT_TOKENS[1]]


def verdicts(mod, landed):
    return ball_cell(mod, landed), cone_cell(mod, landed), strict_cell(mod, landed)


def semantic_checks(mod, chunks, prints, tag, landed, inv_files):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    check('S1', 'DenseBoundaryOrbit is the landed BoundaryTransitive with its last clause replaced by orbit-closure '
                'membership' + tag, def_ok(mod, landed))
    # S2
    bad2 = [d for d, (m, l) in PAIRS.items() if kinds.get(d) != 'theorem' or not pair_ok(mod, landed, d, l)]
    bad2 += [d for d in BALL_PRINTED + CONE_PRINTED if PREFIX + d not in prints]
    check('S2', 'each of the %d frozen pairs is its landed theorem with BoundaryTransitive replaced and nothing else%s%s'
          % (len(PAIRS), tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    names, spaces = inventory(inv_files + [mod])
    bad3 = []
    for d, (m, l) in PAIRS.items():
        lt = [t for t in inv_files if ('\nnamespace %s\n' % m) in t]
        bad3 += ['%s:%s' % (d, t) for t in resolution_bad(mod, d, lt[0] if len(lt) == 1 else None, l, names, spaces)]
    check('S3', 'every OIBridge identifier of every pair resolves to the same unique declaration in both contexts%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = ([] if weak_ok(texts, kinds) else [WEAK]) + strict_bad(chunks, landed)
    bad4 += [n for n in STRICT_PRINTED if PREFIX + n not in prints]
    check('S4', 'the weakening and the strictness witness with their frozen statements, through EFF-1\'s countable '
                'no-go%s%s' % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    secs = sections(mod)
    stmts = ' '.join(code_only(t) for t in texts.values())
    bad5 = [t for t in SCOPE_TOKENS if token(t, stmts)]
    for kind, name, start, se, nxt, cend in spans(mod):
        if section_at(secs, start) != '§D' and token(FAMILY, code_only(mod[start:nxt])):
            bad5.append(name)
    check('S5', 'no exact-existence or uncovered object; ratRefl only in §D%s%s'
          % (tag, (' %s' % bad5[:3]) if bad5 else ''), not bad5)
    # S6
    vis_clash = []
    others = inventory(inv_files)[0]
    msc = scopes_at(mod)
    for kind, name in decls(mod):
        sc = msc.get(name, ([], [], []))
        hits = resolve(name, visible(sc[1], sc[2], spaces), others)
        if hits:
            vis_clash.append(name)
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S6', 'no declaration shares a name with a visible OIBridge declaration; the only import is OIBridge.K2Guard'
          '%s%s' % (tag, (' %s' % vis_clash[:3]) if vis_clash else ''), not vis_clash and imports == [IMPORT_ONLY])
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    bad8 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        sec = section_at(secs, start)
        body = code_only(mod[start:nxt])
        if sec == '§B' and any(token(t, body) for t in CONE_OBJECTS):
            bad8.append(name)
        if sec in ('§A', '§B', '§C') and token(FAMILY, body):
            bad8.append(name)
    check('S8', 'no cone or selector object in §B; ratRefl in no consumer section%s%s'
          % (tag, (' %s' % bad8[:3]) if bad8 else ''), not bad8)
    # S9
    local = {n for _, n in decls(mod)}
    pnames = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(pnames) == N_PRINTS
          and all(n in local for n in pnames))
    # V
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
    check('S2', 'the landed statements read from D are the frozen ones', landed == LANDED)
    mod = show(commit, MOD)
    module_checks(mod, landed=landed)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (a + b + c, toks), len(a) == 1 and len(b) == 1 and len(c) == 1 and sorted(toks) == sorted(a + b + c))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the K1-SHARP-TESTS-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    landed = landed_at_d()
    a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
    print('VERDICT  BALL    %s' % ('/'.join(a) or 'none'))
    print('VERDICT  CONE    %s' % ('/'.join(b) or 'none'))
    print('VERDICT  STRICT  %s' % ('/'.join(c) or 'none'))
    check('V', 'the landed statements read from D are the frozen ones', landed == LANDED)
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


def append_strict(text, decl):
    """Insert a declaration at the end of §D, before its `end Strict`."""
    return replace_once(text, '\nend Strict\n', '\n' + decl + '\n\nend Strict\n')


def verdict_of(mod2, landed=None):
    return verdicts(mod2, LANDED if landed is None else landed)

DEF_TAIL = 'y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n'
QN_HEAD = ('theorem boundary_qnorm_const_of_dense {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n'
           '    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
           '    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) :\n'
           '    ∃ R : ℝ, 0 ≤ R ∧ ∀ x, IsBoundaryState Ω x → qnorm Ω (x - centroid Ω) = R ^ 2 := by')
CONE_HEAD = ('theorem maxConeOf_avail_eq_of_dense (hd : 0 < d) (hG : PreservesBody (eball d) G)\n'
             '    (hP1 : SharpSeed (eball d) r) (hK : DenseBoundaryOrbit (eball d) G)\n'
             '    (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) :\n'
             '    maxConeOf avail = maxCone (eball d) := by')
ENT_HEAD = ('    {T : W d ≃ₗ[ℝ] W d} (hEnt : EntanglingOf (eball d) avail T) : Entangling (eball d) T :=\n')
WEAK_HEAD = '    {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hT : BoundaryTransitive Ω G) : DenseBoundaryOrbit Ω G := by'
NOGO_PROOF = '  not_boundaryTransitive_of_countable countable_ratRefl\n'
CHART_HEAD = 'theorem chartBody_eq_eball_of_dense {D : DirectedStages} (C : CompletionChart D) (hd : 0 < C.d)'
CONE_VARS = '  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n\n/-- **The available family'
OPEN_LINE = '  CompletionAction InvariantInnerProduct TransitiveBody CompositeDimension CompositeInterface\n'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    landed = landed_at_d()
    check('T', 'the landed statements read from D are the frozen ones', landed == LANDED and len(LANDED) == 14)
    module_checks(mod, ' [reference]')
    a, b, c = verdict_of(mod)
    check('T', 'the reference module reads %s, %s and %s' % (a, b, c),
          a == [BALL_TOKENS[0]] and b == [CONE_TOKENS[0]] and c == [STRICT_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration',
              replace_once(mod, '\ntheorem countable_ratRefl :', '\ntheorem countable_ratRefl\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, CONE_VARS, '  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {x : ℕ}\n\n/-- **The available family'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace K1Bridge K2Guard\n',
                                                       '\nopen EffectSpace K1Bridge\n'))
    must_fail('N3', 'a sorry', append_strict(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed',
              replace_once(mod, '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n', ''))
    # S1
    must_fail('S1', 'the orbit closure replaced by the orbit itself',
              replace_once(mod, DEF_TAIL, 'y ∈ ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n'))
    must_fail('S1', 'the orbit closure replaced by the orbit\'s interior',
              replace_once(mod, DEF_TAIL, 'y ∈ interior ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n'))
    # S2 -- the pairing, load-bearing
    must_fail('S2', 'a ball conclusion changed (0 ≤ R to 0 < R)',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('0 ≤ R ∧', '0 < R ∧')))
    must_fail('S2', 'a ball hypothesis added',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('(hc : IsCompact Ω)', '(hc : IsCompact Ω) (hconv : Convex ℝ Ω)')))
    must_fail('S2', 'a dense theorem keeping exact transitivity',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('DenseBoundaryOrbit Ω G', 'BoundaryTransitive Ω G')))
    must_fail('S2', 'both hypotheses carried',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('(hT : DenseBoundaryOrbit Ω G)',
                                                         '(hT : DenseBoundaryOrbit Ω G) (hB : BoundaryTransitive Ω G)')))
    must_fail('S2', 'a cone hypothesis dropped',
              replace_once(mod, CONE_HEAD, CONE_HEAD.replace(' (hE : EffectsOn (eball d) avail)', '')))
    must_fail('S2', 'a cone conclusion weakened to an inclusion',
              replace_once(mod, CONE_HEAD, CONE_HEAD.replace('maxConeOf avail = maxCone', 'maxConeOf avail ⊆ maxCone')))
    must_fail('S2', 'a selector conclusion changed',
              replace_once(mod, ENT_HEAD, ENT_HEAD.replace(': Entangling (eball d) T', ': True')))
    must_fail('S2', 'a section variable changed under the cone theorems',
              replace_once(mod, CONE_VARS, '  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {d : ℕ}\n\n/-- **The available family'))
    must_fail('S2', 'the chart theorem\'s completion data made implicit',
              replace_once(mod, CHART_HEAD, CHART_HEAD.replace('(C : CompletionChart D)', '{C : CompletionChart D}')))
    lm = dict(LANDED)
    lm['maxConeOf_avail_eq'] = lm['maxConeOf_avail_eq'].replace('(hd : 0 < d)', '(hd : 1 < d)')
    check('M', 'pairing: a landed statement that differs from the dense one fails the pair and only the cone cell',
          not pair_ok(mod, lm, 'maxConeOf_avail_eq_of_dense', 'maxConeOf_avail_eq')
          and verdict_of(mod, lm) == ([BALL_TOKENS[0]], [CONE_TOKENS[1]], [STRICT_TOKENS[0]]))
    lm2 = dict(LANDED)
    lm2['eq_qBall_of_boundaryTransitive'] = lm2['eq_qBall_of_boundaryTransitive'].replace('BoundaryTransitive Ω G',
                                                                                        'BoundaryTransitive Ω G ∧ True')
    check('M', 'pairing: a landed statement differing outside the hypothesis fails the pair',
          not pair_ok(mod, lm2, 'eq_qBall_of_dense', 'eq_qBall_of_boundaryTransitive'))
    # S3 -- resolution
    must_fail('S3', 'an opened namespace dropped (qnorm, centroid and qBall no longer resolve as in TRB-1)',
              replace_once(mod, OPEN_LINE, OPEN_LINE.replace('InvariantInnerProduct ', '').replace('TransitiveBody ', '')))
    must_fail('S3', 'a local declaration shadowing a landed object of a paired statement',
              insert_in_section(mod, '/-! ### §B', 'def eball (d : ℕ) : Set (Fin d → ℝ) := Set.univ'))
    # S4 -- strictness
    must_fail('S4', 'the weakening reversed',
              replace_once(mod, WEAK_HEAD, '    {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hT : DenseBoundaryOrbit Ω G) : '
                                           'BoundaryTransitive Ω G := by'))
    must_fail('S4', 'the non-transitivity proved without EFF-1\'s countable no-go',
              replace_once(mod, NOGO_PROOF, '  fun h => absurd h (by exact?)\n'))
    must_fail('S4', 'the family enlarged to all reflections',
              replace_once(mod, '{q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0}',
                           '{q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0 ∨ True}'))
    must_fail('S4', 'the strictness witness moved to d = 2',
              replace_once(mod, 'theorem not_boundaryTransitive_ratRefl : ¬ BoundaryTransitive (eball 3) (ratRefl 3) :=',
                           'theorem not_boundaryTransitive_ratRefl : ¬ BoundaryTransitive (eball 2) (ratRefl 2) :='))
    lm3 = dict(LANDED)
    lm3['not_boundaryTransitive_of_countable'] = lm3['not_boundaryTransitive_of_countable'].replace('G.Countable',
                                                                                                    'G.Finite')
    check('M', 'strictness: a different landed no-go fails only the strictness cell',
          verdict_of(mod, lm3) == ([BALL_TOKENS[0]], [CONE_TOKENS[0]], [STRICT_TOKENS[1]]))
    # S5
    must_fail('S5', 'an exact-existence object stated',
              append_strict(mod, 'theorem sf_free : sharpFamily 3 ⊆ sharpFamily 3 := le_rfl'))
    must_fail('S5', 'the Lorentz bridge restated',
              append_strict(mod, 'theorem lz (x0 : ℝ) (v : Fin 3 → ℝ) (h : 0 ≤ conePair (sharpEff v) x0 v) : True := '
                                 'trivial'))
    must_fail('S5', 'the control family in a consumer section',
              insert_in_section(mod, '/-! ### §D', 'theorem rr_c : ratRefl 1 = ratRefl 1 := rfl'))
    # S6
    must_fail('S6', 'a landed definition re-declared', append_strict(mod, 'def fullAut : ℕ := 0'))
    must_fail('S6', 'a second import',
              replace_once(mod, 'import OIBridge.K2Guard\n', 'import OIBridge.K2Guard\nimport OIBridge.SharpTests\n'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  (A) The ball.', '  This replaces K∞-Trans. (A) The ball.'))
    must_fail('S7', 'the design header', replace_once(mod, 'round KTRANS-DENSE-1:', 'design (round C):'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('A dense boundary orbit suffices for the listed consumers; the round does not derive one, '
                          'and ratRefl is a control.')
          and phrase_hits('The operations are\nclosed under operations.') == ['closed under operations'])
    # S8
    must_fail('S8', 'a cone object in the ball section',
              insert_in_section(mod, '/-! ### §C', 'theorem mc_b : maxCone (eball 1) = maxCone (eball 1) := rfl'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.DenseOrbit.countable_seedOrbit_cone\n',
                           '#print axioms OIBridge.DenseOrbit.countable_seedOrbit_cone\n'
                           '#print axioms OIBridge.DenseOrbit.countable_ratRefl\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n',
                           '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n'
                           '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n'))
    # V -- each cell reads its alternative, independently of the others
    m = replace_once(mod, QN_HEAD, QN_HEAD.replace('0 ≤ R ∧', '0 < R ∧'))
    check('M', 'decision rule: a broken ball pair reads BALL-NOT-ESTABLISHED and leaves the other cells unchanged',
          verdict_of(m) == ([BALL_TOKENS[1]], [CONE_TOKENS[0]], [STRICT_TOKENS[0]]))
    m = replace_once(mod, CONE_HEAD, CONE_HEAD.replace(' (hE : EffectsOn (eball d) avail)', ''))
    check('M', 'decision rule: a broken cone pair reads CONE-NOT-ESTABLISHED and leaves the other cells unchanged',
          verdict_of(m) == ([BALL_TOKENS[0]], [CONE_TOKENS[1]], [STRICT_TOKENS[0]]))
    m = replace_once(mod, NOGO_PROOF, '  fun h => absurd h (by exact?)\n')
    check('M', 'decision rule: a broken strictness witness reads STRICTLY-WEAKER-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([BALL_TOKENS[0]], [CONE_TOKENS[0]], [STRICT_TOKENS[1]]))
    m = replace_once(mod, WEAK_HEAD, WEAK_HEAD.replace('(hT : BoundaryTransitive Ω G)', '(hT : True)'))
    check('M', 'decision rule: the weakening broken reads NOT-ESTABLISHED in the two cells that read it, and leaves '
               'the cone cell unchanged', verdict_of(m) == ([BALL_TOKENS[1]], [CONE_TOKENS[0]], [STRICT_TOKENS[1]]))
    m = replace_once(mod, DEF_TAIL, 'y ∈ ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n')
    check('M', 'decision rule: the definition broken reads NOT-ESTABLISHED in all three cells',
          verdict_of(m) == ([BALL_TOKENS[1]], [CONE_TOKENS[1]], [STRICT_TOKENS[1]]))
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('KTRANS-DENSE-BALL-PROVED, KTRANS-DENSE-CONE-PROVED and KTRANS-DENSE-STRICTLY-WEAKER.')
          == ['KTRANS-DENSE-BALL-PROVED', 'KTRANS-DENSE-CONE-PROVED', 'KTRANS-DENSE-STRICTLY-WEAKER']
          and note_tokens('KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED') == ['KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED'])
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
