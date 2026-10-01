#!/usr/bin/env python3
"""controls.py -- round KINF-2's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against: the module's frozen header and declarations (every structure and definition
whole, every theorem statement), the census family, the workflow edit, the import line, the probe blob, the outcome
sentences and the clause.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F and F = D plus the preregistration alone)
  controls.py --self-test                   constants against the preregistration beside this file; two synthetic
                                            rows (FOUNDATIONS-PROVED, UNDECIDED) that must hold; mutation controls
                                            that must fail with their named codes
"""
import hashlib, json, os, re, subprocess, sys

D = 'd6b6458010a6d2812bd3215a8bb6f8a1bab37f00'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-kinf-2-foundations/'
MODULE = 'verification/lean-mathlib/OIBridge/KInfFoundations.lean'
PROBE = 'verification/lean/kinf2_foundations_probe.py'
PROBE_BLOB = '3634e3d3b86405f90f7eecc7674d45442b235e7e'
REFERENCE_BLOB = '3b8290838f1ee7006996db53a2f1d1a228249a08'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
LABELS = ('KINF-2-FOUNDATIONS-PROVED', 'KINF-2-UNDECIDED')
VERDICT = 'kinf2_kernel_core'
FROZEN = {'header': '/-\n  OIBridge/KInfFoundations.lean — round KINF-2: the field-neutral vocabulary of the pre-quantum\n  operational completion, corrected, and the elementary lemmas that vocabulary supports.\n\n  Nothing in this module mentions ℂ, a matrix carrier, or the substratum, except §F, which is a\n  statement of the imported qubit kinematics. It fixes definitions over a real normed space `V`\n  and proves small logical facts. It sources nothing: the module does not derive drivability,\n  supporting effects, singleton faces or copy naturality from any OI construction, and it\n  contains no reconstruction theorem.\n\n  The corrections to the vocabulary of round KINF-1, which halted:\n    * an effect is *proper* on `Ω` when some state gives it a value below one, tested on `Ω`;\n      supporting-effect completeness and singleton faces quantify over proper effects only, so the\n      unit effect may stay available and changes neither (§B′, `…_insert_iff`);\n    * the boundary is read in `Ω` alone (`IsBoundaryState`), not in the topology of `V`, so a body\n      that is not full-dimensional in `V` is not excluded for a reason of dimension; an open body\n      has no boundary state, so K∞-1 is stated for compact convex bodies;\n    * elementary drivability is a group flow of automorphisms of `Ω`, with `J` an automorphism of\n      `Ω` and the off-axis clause compared on `Ω` (§C).\n\n  Proved here.\n    §A  the state body of a finite observer stage is compact and lies on the unit hyperplane;\n    §B′ L1–L3: non-proper effects, and the boundary states certain effects pick out;\n    §C′ the semantic controls for drivability: the unit ball of `ℝ³` is drivable (rotations about\n        one axis, the half-turn, the cyclic permutation of the axes); the classical bit `[-1, 1]`\n        and a one-point body are not;\n    §D  Lemma C, `relStrictConvex_of_supporting_singleton`, and its converse,\n        `singletonFaces_of_relStrictConvex`: given (SEC), singleton faces are equivalent to\n        relative strict convexity of the body, each direction proved separately;\n        `relStrictConvex_of_strictConvex`; Lemma D;\n    §D′ the semantic controls for (SF) and (SEC): singleton faces hold on every closed ball of a\n        strictly convex space with any effect family, and fail on the sup-norm square with its\n        full effects; (SEC) holds on the segment `[-1, 1]` with its full effects and fails with\n        the unit alone;\n    §E  Lemma B and the finite-preparation bound; §E′ Theorem F2;\n    §F  the qubit certain face, a theorem of the imported matrix kinematics;\n    §G  `KInf1`, hypothesis K∞-1, stated as a definition; it holds for the ball with its full\n        effects and fails for the ball with the unit effect alone, so it is a proposition about\n        the effect family. It is proved for no physical family.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/\nimport Mathlib.Analysis.Convex.Gauge\nimport Mathlib.Analysis.Convex.Strict\nimport Mathlib.Analysis.Convex.StrictConvexSpace\nimport Mathlib.Analysis.Convex.Topology\nimport Mathlib.Analysis.Normed.Module.Basic\nimport Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic\nimport Mathlib.Data.Set.Card\nimport Mathlib.LinearAlgebra.Matrix.PosDef\nimport Mathlib.LinearAlgebra.Matrix.Trace\nimport OIBridge.CoherentExtension\n\n', 'declarations': {'FiniteStage': ('structure', 'structure FiniteStage where\n  P : Type\n  E : Type\n  [fP : Fintype P]\n  [fE : Fintype E]\n  p : E → P → ℝ\n  unit : E\n  nonneg : ∀ e x, 0 ≤ p e x\n  le_one : ∀ e x, p e x ≤ 1\n  unit_eq : ∀ x, p unit x = 1'), 'vec': ('def', 'def vec (x : S.P) : S.E → ℝ := fun e => S.p e x'), 'states': ('def', 'def states : Set (S.E → ℝ) := convexHull ℝ (Set.range S.vec)'), 'states_isCompact': ('theorem', 'theorem states_isCompact : IsCompact S.states :='), 'states_isClosed': ('theorem', 'theorem states_isClosed : IsClosed S.states :='), 'states_convex': ('theorem', 'theorem states_convex : Convex ℝ S.states :='), 'states_unit': ('theorem', 'theorem states_unit : ∀ v ∈ S.states, v S.unit = 1 :='), 'IsEffectOn': ('def', 'def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=\n  ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1'), 'certainFace': ('def', 'def certainFace (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Set V :=\n  {x ∈ Ω | e x = 1}'), 'IsProperOn': ('def', 'def IsProperOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=\n  ∃ y ∈ Ω, e y < 1'), 'IsBoundaryState': ('def', 'def IsBoundaryState (Ω : Set V) (x : V) : Prop :=\n  x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε : ℝ, 0 < ε → x + ε • (x - y) ∉ Ω'), 'SupportingEffectComplete': ('def', 'def SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n  ∀ x, IsBoundaryState Ω x → ∃ e ∈ avail, IsEffectOn Ω e ∧ IsProperOn Ω e ∧ e x = 1'), 'SingletonFaces': ('def', 'def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n  ∀ e ∈ avail, IsEffectOn Ω e → IsProperOn Ω e → (certainFace Ω e).Subsingleton'), 'RelStrictConvex': ('def', 'def RelStrictConvex (Ω : Set V) : Prop :=\n  ∀ x ∈ Ω, ∀ y ∈ Ω, x ≠ y → ∀ a b : ℝ, 0 < a → 0 < b → a + b = 1 →\n    a • x + b • y ∈ Ω ∧ ¬ IsBoundaryState Ω (a • x + b • y)'), 'fullEffects': ('def', 'def fullEffects (Ω : Set V) : Set (V →ᵃ[ℝ] ℝ) :=\n  {e | IsEffectOn Ω e}'), 'PerfectlyDistinguishable': ('def', 'def PerfectlyDistinguishable (Ω : Set V) {ι : Type} [Fintype ι]\n    (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ) : Prop :=\n  (∀ i, x i ∈ Ω) ∧ (∀ i, IsEffectOn Ω (e i)) ∧ (∀ y ∈ Ω, ∑ i, e i y = 1) ∧\n    (∀ i, e i (x i) = 1)'), 'CentrallySymmetric': ('def', 'def CentrallySymmetric (Ω : Set V) (c : V) : Prop :=\n  ∀ x ∈ Ω, c + (c - x) ∈ Ω'), 'affine_combo': ('theorem', 'theorem affine_combo (e : V →ᵃ[ℝ] ℝ) (x y : V) (a b : ℝ) (hab : a + b = 1) :\n    e (a • x + b • y) = a * e x + b * e y :='), 'affine_reflect': ('theorem', 'theorem affine_reflect (e : V →ᵃ[ℝ] ℝ) (c x : V) :\n    e (c + (c - x)) = 2 * e c - e x :='), 'convex_affine_le': ('theorem', 'theorem convex_affine_le (e : V →ᵃ[ℝ] ℝ) (m : ℝ) : Convex ℝ {y : V | e y ≤ m} :='), 'extension_eq': ('theorem', 'theorem extension_eq (x y : V) (ε : ℝ) : x + ε • (x - y) = (1 + ε) • x + (-ε) • y :='), 'not_isProperOn_of_eq_one': ('theorem', 'theorem not_isProperOn_of_eq_one {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} (h : ∀ y ∈ Ω, e y = 1) :\n    ¬ IsProperOn Ω e :='), 'not_isProperOn_const_one': ('theorem', 'theorem not_isProperOn_const_one (Ω : Set V) : ¬ IsProperOn Ω (AffineMap.const ℝ V (1 : ℝ)) :='), 'eq_one_of_certain_of_not_boundary': ('theorem', 'theorem eq_one_of_certain_of_not_boundary {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {x : V}\n    (he : IsEffectOn Ω e) (hx : x ∈ Ω) (hnb : ¬ IsBoundaryState Ω x) (hone : e x = 1) :\n    ∀ y ∈ Ω, e y = 1 :='), 'isBoundaryState_of_certain_proper': ('theorem', 'theorem isBoundaryState_of_certain_proper {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {x : V}\n    (he : IsEffectOn Ω e) (hp : IsProperOn Ω e) (hx : x ∈ Ω) (hone : e x = 1) :\n    IsBoundaryState Ω x :='), 'supportingEffectComplete_insert_iff': ('theorem', 'theorem supportingEffectComplete_insert_iff {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}\n    {u : V →ᵃ[ℝ] ℝ} (hu : ¬ IsProperOn Ω u) :\n    SupportingEffectComplete Ω (insert u avail) ↔ SupportingEffectComplete Ω avail :='), 'singletonFaces_insert_iff': ('theorem', 'theorem singletonFaces_insert_iff {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}\n    {u : V →ᵃ[ℝ] ℝ} (hu : ¬ IsProperOn Ω u) :\n    SingletonFaces Ω (insert u avail) ↔ SingletonFaces Ω avail :='), 'ElementaryDrivability': ('structure', 'structure ElementaryDrivability (Ω : Set V) where\n  flow : ℝ → V ≃ᵃ[ℝ] V\n  flow_zero : flow 0 = AffineEquiv.refl ℝ V\n  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)\n  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2\n  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω\n  t₀ : ℝ\n  N_involutive : ∀ x ∈ Ω, flow t₀ (flow t₀ x) = x\n  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x\n  J : V ≃ᵃ[ℝ] V\n  J_preserves : ∀ x ∈ Ω, J x ∈ Ω\n  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω\n  J_off_axis : ∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x'), 'ElementaryDrivability.N': ('def', 'def ElementaryDrivability.N {Ω : Set V} (D : ElementaryDrivability Ω) : V ≃ᵃ[ℝ] V :=\n  D.flow D.t₀'), 'CopyNatural': ('def', 'def CopyNatural (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) : Prop :=\n  N_B = (e.symm.trans N_A).trans e'), 'copyNatural_refl_iff': ('theorem', 'theorem copyNatural_refl_iff (N_A N_B : V ≃ᵃ[ℝ] V) :\n    CopyNatural N_A N_B (AffineEquiv.refl ℝ V) ↔ N_B = N_A :='), 'copyNatural_iff_apply': ('theorem', 'theorem copyNatural_iff_apply (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) :\n    CopyNatural N_A N_B e ↔ ∀ x, N_B (e x) = e (N_A x) :='), 'ball3': ('def', 'def ball3 : Set (Fin 3 → ℝ) := {v | v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}'), 'mem_ball3': ('theorem', 'theorem mem_ball3 (v : Fin 3 → ℝ) : v ∈ ball3 ↔ v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1 :='), 'vec3_ext': ('theorem', 'theorem vec3_ext {v w : Fin 3 → ℝ} (h0 : v 0 = w 0) (h1 : v 1 = w 1) (h2 : v 2 = w 2) :\n    v = w :='), 'ball3_convex': ('theorem', 'theorem ball3_convex : Convex ℝ ball3 :='), 'ball3_isCompact': ('theorem', 'theorem ball3_isCompact : IsCompact ball3 :='), 'rotFun': ('noncomputable def', 'noncomputable def rotFun (t : ℝ) (v : Fin 3 → ℝ) : Fin 3 → ℝ :=\n  ![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2]'), 'rotFun_apply': ('theorem', 'theorem rotFun_apply (t : ℝ) (v : Fin 3 → ℝ) :\n    rotFun t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧\n      rotFun t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun t v 2 = v 2 :='), 'rotFun_zero': ('theorem', 'theorem rotFun_zero (v : Fin 3 → ℝ) : rotFun 0 v = v :='), 'rotFun_add': ('theorem', 'theorem rotFun_add (s t : ℝ) (v : Fin 3 → ℝ) : rotFun s (rotFun t v) = rotFun (s + t) v :='), 'rotFun_mem_ball3': ('theorem', 'theorem rotFun_mem_ball3 (t : ℝ) {v : Fin 3 → ℝ} (hv : v ∈ ball3) : rotFun t v ∈ ball3 :='), 'rotLin': ('noncomputable def', "noncomputable def rotLin (t : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where\n  toFun := rotFun t\n  map_add' v w := by\n    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (v + w)\n    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v\n    obtain ⟨c0, c1, c2⟩ := rotFun_apply t w\n    apply vec3_ext <;> simp only [Pi.add_apply, a0, a1, a2, b0, b1, b2, c0, c1, c2] <;> ring\n  map_smul' r v := by\n    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (r • v)\n    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v\n    apply vec3_ext <;>\n      simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, a0, a1, a2, b0, b1, b2] <;> ring"), 'rotEquiv': ('noncomputable def', 'noncomputable def rotEquiv (t : ℝ) : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) :=\n  { rotLin t with\n    invFun := rotFun (-t)\n    left_inv := fun v => by\n      show rotFun (-t) (rotFun t v) = v\n      rw [rotFun_add, neg_add_cancel, rotFun_zero]\n    right_inv := fun v => by\n      show rotFun t (rotFun (-t) v) = v\n      rw [rotFun_add, add_neg_cancel, rotFun_zero] }'), 'rot3': ('noncomputable def', 'noncomputable def rot3 (t : ℝ) : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := (rotEquiv t).toAffineEquiv'), 'rot3_apply': ('theorem', 'theorem rot3_apply (t : ℝ) (v : Fin 3 → ℝ) : rot3 t v = rotFun t v :='), 'cycEquiv': ('noncomputable def', "noncomputable def cycEquiv : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) where\n  toFun v := ![v 2, v 0, v 1]\n  invFun v := ![v 1, v 2, v 0]\n  map_add' v w := by apply vec3_ext <;> rfl\n  map_smul' r v := by apply vec3_ext <;> rfl\n  left_inv v := by apply vec3_ext <;> rfl\n  right_inv v := by apply vec3_ext <;> rfl"), 'cyc3': ('noncomputable def', 'noncomputable def cyc3 : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cycEquiv.toAffineEquiv'), 'cyc3_apply': ('theorem', 'theorem cyc3_apply (v : Fin 3 → ℝ) : cyc3 v 0 = v 2 ∧ cyc3 v 1 = v 0 ∧ cyc3 v 2 = v 1 :='), 'cyc3_symm_apply': ('theorem', 'theorem cyc3_symm_apply (v : Fin 3 → ℝ) :\n    cyc3.symm v 0 = v 1 ∧ cyc3.symm v 1 = v 2 ∧ cyc3.symm v 2 = v 0 :='), 'cyc3_mem_ball3': ('theorem', 'theorem cyc3_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3 v ∈ ball3 :='), 'cyc3_symm_mem_ball3': ('theorem', 'theorem cyc3_symm_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3.symm v ∈ ball3 :='), 'ball3Drive': ('noncomputable def', 'noncomputable def ball3Drive : ElementaryDrivability ball3 where\n  flow := rot3\n  flow_zero := AffineEquiv.ext fun v => by rw [rot3_apply, rotFun_zero, AffineEquiv.refl_apply]\n  flow_add s t := AffineEquiv.ext fun v => by\n    simp only [AffineEquiv.trans_apply, rot3_apply, rotFun_add]\n  flow_continuous := by\n    refine continuous_pi fun i => ?_\n    fin_cases i\n    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.cos q.1 * q.2 0 - Real.sin q.1 * q.2 1\n      fun_prop\n    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.sin q.1 * q.2 0 + Real.cos q.1 * q.2 1\n      fun_prop\n    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => q.2 2\n      fun_prop\n  flow_preserves t _ hv := rotFun_mem_ball3 t hv\n  t₀ := Real.pi\n  N_involutive x _ := by\n    simp only [rot3_apply]\n    obtain ⟨a0, a1, a2⟩ := rotFun_apply Real.pi (rotFun Real.pi x)\n    obtain ⟨b0, b1, b2⟩ := rotFun_apply Real.pi x\n    apply vec3_ext\n    · rw [a0, b0, b1, Real.cos_pi, Real.sin_pi]; ring\n    · rw [a1, b0, b1, Real.cos_pi, Real.sin_pi]; ring\n    · rw [a2, b2]\n  N_moves := ⟨![1, 0, 0], by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun h => by\n    have h0 : rot3 Real.pi ![1, 0, 0] 0 = (![1, 0, 0] : Fin 3 → ℝ) 0 := congrFun h 0\n    change Real.cos Real.pi * 1 - Real.sin Real.pi * 0 = 1 at h0\n    rw [Real.cos_pi, Real.sin_pi] at h0\n    norm_num at h0⟩\n  J := cyc3\n  J_preserves _ hv := cyc3_mem_ball3 hv\n  J_symm_preserves _ hv := cyc3_symm_mem_ball3 hv\n  J_off_axis := ⟨Real.pi, fun s => ⟨![0, 0, 1],\n    by show (0 : ℝ) ^ 2 + 0 ^ 2 + 1 ^ 2 ≤ 1; norm_num, fun h => by\n      have h2 : cyc3 (rot3 Real.pi (cyc3.symm ![0, 0, 1])) 2 = rot3 s ![0, 0, 1] 2 :=\n        congrFun h 2\n      change Real.sin Real.pi * 0 + Real.cos Real.pi * 1 = 1 at h2\n      rw [Real.sin_pi, Real.cos_pi] at h2\n      norm_num at h2⟩⟩'), 'ball3_drivable': ('theorem', 'theorem ball3_drivable : Nonempty (ElementaryDrivability ball3) :='), 'affineEquiv_real_apply': ('theorem', 'theorem affineEquiv_real_apply (g : ℝ ≃ᵃ[ℝ] ℝ) (x : ℝ) : g x = g 0 + g.linear 1 * x :='), 'bit_aux': ('theorem', 'theorem bit_aux {a b c d : ℝ} (h1 : -1 ≤ a + b * 1 ∧ a + b * 1 ≤ 1)\n    (h2 : -1 ≤ a + b * -1 ∧ a + b * -1 ≤ 1) (h3 : -1 ≤ c + d * 1 ∧ c + d * 1 ≤ 1)\n    (h4 : -1 ≤ c + d * -1 ∧ c + d * -1 ≤ 1) (h5 : a + b * (c + d * 0) = 0)\n    (h6 : a + b * (c + d * 1) = 1) : a = 0 ∧ b * b = 1 :='), 'not_drivable_Icc': ('theorem', 'theorem not_drivable_Icc : IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) :='), 'not_drivable_singleton': ('theorem', 'theorem not_drivable_singleton (x : V) : IsEmpty (ElementaryDrivability ({x} : Set V)) :='), 'relStrictConvex_of_supporting_singleton': ('theorem', 'theorem relStrictConvex_of_supporting_singleton {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}\n    (hconv : Convex ℝ Ω) (hSEC : SupportingEffectComplete Ω avail)\n    (hSF : SingletonFaces Ω avail) : RelStrictConvex Ω :='), 'singletonFaces_of_relStrictConvex': ('theorem', 'theorem singletonFaces_of_relStrictConvex {Ω : Set V} (avail : Set (V →ᵃ[ℝ] ℝ))\n    (h : RelStrictConvex Ω) : SingletonFaces Ω avail :='), 'not_isBoundaryState_of_mem_interior': ('theorem', 'theorem not_isBoundaryState_of_mem_interior {Ω : Set V} {z : V} (hint : z ∈ interior Ω) :\n    ¬ IsBoundaryState Ω z :='), 'relStrictConvex_of_strictConvex': ('theorem', 'theorem relStrictConvex_of_strictConvex {Ω : Set V} (h : StrictConvex ℝ Ω) :\n    RelStrictConvex Ω :='), 'supportingEffectComplete_of_isOpen': ('theorem', 'theorem supportingEffectComplete_of_isOpen {Ω : Set V} (hΩ : IsOpen Ω)\n    (avail : Set (V →ᵃ[ℝ] ℝ)) : SupportingEffectComplete Ω avail :='), 'card_le_two_of_centrallySymmetric': ('theorem', 'theorem card_le_two_of_centrallySymmetric {Ω : Set V} {c : V} (hΩ : CentrallySymmetric Ω c)\n    (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ)\n    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 :='), 'card_le_two_of_centrallySymmetric_full': ('theorem', 'theorem card_le_two_of_centrallySymmetric_full {Ω : Set V} {c : V}\n    (hΩ : CentrallySymmetric Ω c) (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V)\n    (e : ι → V →ᵃ[ℝ] ℝ) (_ : ∀ i, e i ∈ fullEffects Ω)\n    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 :='), 'singletonFaces_closedBall': ('theorem', 'theorem singletonFaces_closedBall [StrictConvexSpace ℝ V] (x : V) (r : ℝ)\n    (avail : Set (V →ᵃ[ℝ] ℝ)) : SingletonFaces (Metric.closedBall x r) avail :='), 'affR': ('noncomputable def', 'noncomputable def affR (a b : ℝ) : ℝ →ᵃ[ℝ] ℝ :=\n  AffineMap.const ℝ ℝ a + (b • LinearMap.id : ℝ →ₗ[ℝ] ℝ).toAffineMap'), 'affR_apply': ('theorem', 'theorem affR_apply (a b t : ℝ) : affR a b t = a + b * t :='), 'isBoundaryState_Icc_one': ('theorem', 'theorem isBoundaryState_Icc_one : IsBoundaryState (Set.Icc (-1 : ℝ) 1) 1 :='), 'not_supportingEffectComplete_unit': ('theorem', 'theorem not_supportingEffectComplete_unit :\n    ¬ SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) {AffineMap.const ℝ ℝ (1 : ℝ)} :='), 'supportingEffectComplete_Icc': ('theorem', 'theorem supportingEffectComplete_Icc :\n    SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) (fullEffects (Set.Icc (-1 : ℝ) 1)) :='), 'squareEdgeEffect': ('noncomputable def', 'noncomputable def squareEdgeEffect : (Fin 2 → ℝ) →ᵃ[ℝ] ℝ :=\n  AffineMap.const ℝ (Fin 2 → ℝ) (1 / 2 : ℝ) +\n    ((1 / 2 : ℝ) • (LinearMap.proj 0 : (Fin 2 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap'), 'squareEdgeEffect_apply': ('theorem', 'theorem squareEdgeEffect_apply (v : Fin 2 → ℝ) : squareEdgeEffect v = 1 / 2 + v 0 / 2 :='), 'not_singletonFaces_square': ('theorem', 'theorem not_singletonFaces_square :\n    ¬ SingletonFaces (Metric.closedBall (0 : Fin 2 → ℝ) 1)\n      (fullEffects (Metric.closedBall (0 : Fin 2 → ℝ) 1)) :='), 'not_relStrictConvex_square': ('theorem', 'theorem not_relStrictConvex_square :\n    ¬ RelStrictConvex (Metric.closedBall (0 : Fin 2 → ℝ) 1) :='), 'eq_closedBall_of_frontier_subset_sphere': ('theorem', 'theorem eq_closedBall_of_frontier_subset_sphere {Ω : Set V} (hconv : Convex ℝ Ω)\n    (hcomp : IsCompact Ω) (h0 : (0 : V) ∈ interior Ω)\n    (hfr : frontier Ω ⊆ Metric.sphere (0 : V) 1) : Ω = Metric.closedBall (0 : V) 1 :='), 'exists_vertex_of_certain': ('theorem', 'theorem exists_vertex_of_certain {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)\n    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)\n    (hx : x ∈ convexHull ℝ (Set.range v)) (hone : e x = 1) : ∃ k, e (v k) = 1 :='), 'exposed_mem_range': ('theorem', 'theorem exposed_mem_range {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)\n    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)\n    (hface : certainFace (convexHull ℝ (Set.range v)) e = {x}) : x ∈ Set.range v :='), 'exposedPoints': ('def', 'def exposedPoints (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Set V :=\n  {x | ∃ e ∈ avail, IsEffectOn Ω e ∧ certainFace Ω e = {x}}'), 'exposed_ncard_le': ('theorem', 'theorem exposed_ncard_le {ι : Type} [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)) :\n    (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι :='), 'FiniteStage.exposed_le_card': ('theorem', 'theorem FiniteStage.exposed_le_card (S : FiniteStage)\n    (avail : Set ((S.E → ℝ) →ᵃ[ℝ] ℝ)) :\n    (exposedPoints S.states avail).ncard ≤ Fintype.card S.P :='), 'simplex': ('def', 'def simplex (N : ℕ) : Set (Fin N → ℝ) :=\n  {p | (∀ i, 0 ≤ p i) ∧ ∑ i, p i = 1}'), 'ClassicallyExposed': ('def', 'def ClassicallyExposed (Ω : Set (Fin N → ℝ)) (x : Fin N → ℝ) : Prop :=\n  ∃ c : Fin N → ℝ, (∀ i, 0 ≤ c i ∧ c i ≤ 1) ∧ {p ∈ Ω | ∑ i, c i * p i = 1} = {x}'), 'response_eq_one_forces': ('theorem', 'theorem response_eq_one_forces {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N) {c : Fin N → ℝ}\n    (hc : ∀ i, 0 ≤ c i ∧ c i ≤ 1) {x : Fin N → ℝ} (hx : x ∈ Ω)\n    (hone : ∑ i, c i * x i = 1) : ∀ i, 0 < x i → c i = 1 :='), 'mem_of_classicallyExposed': ('theorem', 'theorem mem_of_classicallyExposed {Ω : Set (Fin N → ℝ)} {x : Fin N → ℝ}\n    (hx : ClassicallyExposed Ω x) : x ∈ Ω :='), 'exists_zero_of_classicallyExposed': ('theorem', 'theorem exists_zero_of_classicallyExposed {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)\n    (hnt : ¬ Ω.Subsingleton) {x : Fin N → ℝ} (hx : ClassicallyExposed Ω x) :\n    ∃ i, x i = 0 :='), 'classical_exposed_ncard_le': ('theorem', 'theorem classical_exposed_ncard_le {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)\n    (hfacet : ∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) :\n    {x | ClassicallyExposed Ω x}.ncard ≤ N :='), 'qubit_certain_face': ('theorem', 'theorem qubit_certain_face (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hρ : ρ.PosSemidef)\n    (htr : ρ.trace = 1) (h00 : ρ 0 0 = 1) :\n    ρ = Matrix.of fun i j => if i = 0 ∧ j = 0 then (1 : ℂ) else 0 :='), 'KInf1': ('def', 'def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n  IsCompact Ω → Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) →\n    SupportingEffectComplete Ω avail'), 'relStrictConvex_of_kInf1': ('theorem', 'theorem relStrictConvex_of_kInf1 {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}\n    (hcomp : IsCompact Ω) (hconv : Convex ℝ Ω) (hK : KInf1 Ω avail)\n    (hD : Nonempty (ElementaryDrivability Ω)) (hSF : SingletonFaces Ω avail) :\n    RelStrictConvex Ω :='), 'ballEffect': ('noncomputable def', 'noncomputable def ballEffect (u : Fin 3 → ℝ) : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ :=\n  AffineMap.const ℝ (Fin 3 → ℝ) (1 / 2 : ℝ) +\n    ((1 / 2 : ℝ) • (u 0 • LinearMap.proj 0 + u 1 • LinearMap.proj 1 + u 2 • LinearMap.proj 2 :\n      (Fin 3 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap'), 'ballEffect_apply': ('theorem', 'theorem ballEffect_apply (u v : Fin 3 → ℝ) :\n    ballEffect u v = 1 / 2 + (u 0 * v 0 + u 1 * v 1 + u 2 * v 2) / 2 :='), 'ball3_extend': ('theorem', "theorem ball3_extend {x0 x1 x2 y0 y1 y2 ε : ℝ} (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 ≤ 1)\n    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 ≤ 1) (hε : 0 < ε)\n    (hε' : 16 * ε = 1 - (x0 ^ 2 + x1 ^ 2 + x2 ^ 2)) :\n    (x0 + ε * (x0 - y0)) ^ 2 + (x1 + ε * (x1 - y1)) ^ 2 + (x2 + ε * (x2 - y2)) ^ 2 ≤ 1 :="), 'supportingEffectComplete_ball3': ('theorem', 'theorem supportingEffectComplete_ball3 : SupportingEffectComplete ball3 (fullEffects ball3) :='), 'kInf1_ball3_full': ('theorem', 'theorem kInf1_ball3_full : KInf1 ball3 (fullEffects ball3) :='), 'isBoundaryState_ball3': ('theorem', 'theorem isBoundaryState_ball3 : IsBoundaryState ball3 ![1, 0, 0] :='), 'not_kInf1_ball3_unit': ('theorem', 'theorem not_kInf1_ball3_unit : ¬ KInf1 ball3 {AffineMap.const ℝ (Fin 3 → ℝ) (1 : ℝ)} :='), 'kinf2_kernel_core': ('theorem', 'theorem kinf2_kernel_core :\n    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)), Convex ℝ Ω →\n      SupportingEffectComplete Ω avail → SingletonFaces Ω avail → RelStrictConvex Ω) ∧\n    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)), RelStrictConvex Ω → SingletonFaces Ω avail) ∧\n    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) (u : V →ᵃ[ℝ] ℝ), ¬ IsProperOn Ω u →\n      (SupportingEffectComplete Ω (insert u avail) ↔ SupportingEffectComplete Ω avail) ∧\n      (SingletonFaces Ω (insert u avail) ↔ SingletonFaces Ω avail)) ∧\n    SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) (fullEffects (Set.Icc (-1 : ℝ) 1)) ∧\n    ¬ SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) {AffineMap.const ℝ ℝ (1 : ℝ)} ∧\n    ¬ SingletonFaces (Metric.closedBall (0 : Fin 2 → ℝ) 1)\n      (fullEffects (Metric.closedBall (0 : Fin 2 → ℝ) 1)) ∧\n    Nonempty (ElementaryDrivability ball3) ∧\n    IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) ∧\n    KInf1 ball3 (fullEffects ball3) ∧\n    ¬ KInf1 ball3 {AffineMap.const ℝ (Fin 3 → ℝ) (1 : ℝ)} ∧\n    (∀ (Ω : Set V) (c : V), CentrallySymmetric Ω c → c ∈ Ω →\n      ∀ (ι : Type) [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ),\n        PerfectlyDistinguishable Ω x e → Fintype.card ι ≤ 2) ∧\n    (∀ Ω : Set V, Convex ℝ Ω → IsCompact Ω → (0 : V) ∈ interior Ω →\n      frontier Ω ⊆ Metric.sphere (0 : V) 1 → Ω = Metric.closedBall (0 : V) 1) ∧\n    (∀ (ι : Type) [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)),\n      (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι) ∧\n    (∀ (N : ℕ) (Ω : Set (Fin N → ℝ)), Ω ⊆ simplex N →\n      (∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) → {x | ClassicallyExposed Ω x}.ncard ≤ N) :=')}}
PRINT = {'states_isCompact': 'OIBridge.KInfFoundations.FiniteStage.states_isCompact', 'states_isClosed': 'OIBridge.KInfFoundations.FiniteStage.states_isClosed', 'states_convex': 'OIBridge.KInfFoundations.FiniteStage.states_convex', 'states_unit': 'OIBridge.KInfFoundations.FiniteStage.states_unit', 'affine_combo': 'OIBridge.KInfFoundations.affine_combo', 'affine_reflect': 'OIBridge.KInfFoundations.affine_reflect', 'convex_affine_le': 'OIBridge.KInfFoundations.convex_affine_le', 'extension_eq': 'OIBridge.KInfFoundations.extension_eq', 'not_isProperOn_of_eq_one': 'OIBridge.KInfFoundations.not_isProperOn_of_eq_one', 'not_isProperOn_const_one': 'OIBridge.KInfFoundations.not_isProperOn_const_one', 'eq_one_of_certain_of_not_boundary': 'OIBridge.KInfFoundations.eq_one_of_certain_of_not_boundary', 'isBoundaryState_of_certain_proper': 'OIBridge.KInfFoundations.isBoundaryState_of_certain_proper', 'supportingEffectComplete_insert_iff': 'OIBridge.KInfFoundations.supportingEffectComplete_insert_iff', 'singletonFaces_insert_iff': 'OIBridge.KInfFoundations.singletonFaces_insert_iff', 'copyNatural_refl_iff': 'OIBridge.KInfFoundations.copyNatural_refl_iff', 'copyNatural_iff_apply': 'OIBridge.KInfFoundations.copyNatural_iff_apply', 'mem_ball3': 'OIBridge.KInfFoundations.mem_ball3', 'vec3_ext': 'OIBridge.KInfFoundations.vec3_ext', 'ball3_convex': 'OIBridge.KInfFoundations.ball3_convex', 'ball3_isCompact': 'OIBridge.KInfFoundations.ball3_isCompact', 'rotFun_apply': 'OIBridge.KInfFoundations.rotFun_apply', 'rotFun_zero': 'OIBridge.KInfFoundations.rotFun_zero', 'rotFun_add': 'OIBridge.KInfFoundations.rotFun_add', 'rotFun_mem_ball3': 'OIBridge.KInfFoundations.rotFun_mem_ball3', 'rot3_apply': 'OIBridge.KInfFoundations.rot3_apply', 'cyc3_apply': 'OIBridge.KInfFoundations.cyc3_apply', 'cyc3_symm_apply': 'OIBridge.KInfFoundations.cyc3_symm_apply', 'cyc3_mem_ball3': 'OIBridge.KInfFoundations.cyc3_mem_ball3', 'cyc3_symm_mem_ball3': 'OIBridge.KInfFoundations.cyc3_symm_mem_ball3', 'ball3_drivable': 'OIBridge.KInfFoundations.ball3_drivable', 'affineEquiv_real_apply': 'OIBridge.KInfFoundations.affineEquiv_real_apply', 'bit_aux': 'OIBridge.KInfFoundations.bit_aux', 'not_drivable_Icc': 'OIBridge.KInfFoundations.not_drivable_Icc', 'not_drivable_singleton': 'OIBridge.KInfFoundations.not_drivable_singleton', 'relStrictConvex_of_supporting_singleton': 'OIBridge.KInfFoundations.relStrictConvex_of_supporting_singleton', 'singletonFaces_of_relStrictConvex': 'OIBridge.KInfFoundations.singletonFaces_of_relStrictConvex', 'not_isBoundaryState_of_mem_interior': 'OIBridge.KInfFoundations.not_isBoundaryState_of_mem_interior', 'relStrictConvex_of_strictConvex': 'OIBridge.KInfFoundations.relStrictConvex_of_strictConvex', 'supportingEffectComplete_of_isOpen': 'OIBridge.KInfFoundations.supportingEffectComplete_of_isOpen', 'card_le_two_of_centrallySymmetric': 'OIBridge.KInfFoundations.card_le_two_of_centrallySymmetric', 'card_le_two_of_centrallySymmetric_full': 'OIBridge.KInfFoundations.card_le_two_of_centrallySymmetric_full', 'singletonFaces_closedBall': 'OIBridge.KInfFoundations.singletonFaces_closedBall', 'affR_apply': 'OIBridge.KInfFoundations.affR_apply', 'isBoundaryState_Icc_one': 'OIBridge.KInfFoundations.isBoundaryState_Icc_one', 'not_supportingEffectComplete_unit': 'OIBridge.KInfFoundations.not_supportingEffectComplete_unit', 'supportingEffectComplete_Icc': 'OIBridge.KInfFoundations.supportingEffectComplete_Icc', 'squareEdgeEffect_apply': 'OIBridge.KInfFoundations.squareEdgeEffect_apply', 'not_singletonFaces_square': 'OIBridge.KInfFoundations.not_singletonFaces_square', 'not_relStrictConvex_square': 'OIBridge.KInfFoundations.not_relStrictConvex_square', 'eq_closedBall_of_frontier_subset_sphere': 'OIBridge.KInfFoundations.eq_closedBall_of_frontier_subset_sphere', 'exists_vertex_of_certain': 'OIBridge.KInfFoundations.exists_vertex_of_certain', 'exposed_mem_range': 'OIBridge.KInfFoundations.exposed_mem_range', 'exposed_ncard_le': 'OIBridge.KInfFoundations.exposed_ncard_le', 'FiniteStage.exposed_le_card': 'OIBridge.KInfFoundations.FiniteStage.exposed_le_card', 'response_eq_one_forces': 'OIBridge.KInfFoundations.response_eq_one_forces', 'mem_of_classicallyExposed': 'OIBridge.KInfFoundations.mem_of_classicallyExposed', 'exists_zero_of_classicallyExposed': 'OIBridge.KInfFoundations.exists_zero_of_classicallyExposed', 'classical_exposed_ncard_le': 'OIBridge.KInfFoundations.classical_exposed_ncard_le', 'qubit_certain_face': 'OIBridge.KInfFoundations.qubit_certain_face', 'relStrictConvex_of_kInf1': 'OIBridge.KInfFoundations.relStrictConvex_of_kInf1', 'ballEffect_apply': 'OIBridge.KInfFoundations.ballEffect_apply', 'ball3_extend': 'OIBridge.KInfFoundations.ball3_extend', 'supportingEffectComplete_ball3': 'OIBridge.KInfFoundations.supportingEffectComplete_ball3', 'kInf1_ball3_full': 'OIBridge.KInfFoundations.kInf1_ball3_full', 'isBoundaryState_ball3': 'OIBridge.KInfFoundations.isBoundaryState_ball3', 'not_kInf1_ball3_unit': 'OIBridge.KInfFoundations.not_kInf1_ball3_unit', 'kinf2_kernel_core': 'OIBridge.KInfFoundations.kinf2_kernel_core'}
WORKFLOW_JOB = '  probes_kinf2:\n    name: Numerical probes / KINF-2 foundations\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: Install the exact-algebra dependency\n        run: pip install sympy==1.14.0\n\n      - name: KINF-2 foundations probe\n        working-directory: verification/lean\n        run: |\n          echo "=== kinf2_foundations_probe.py ==="\n          python3 kinf2_foundations_probe.py\n'
WORKFLOW_EDITS = [('          python3 native_gate_ball_probe.py\n\n', '          python3 native_gate_ball_probe.py\n\n  probes_kinf2:\n    name: Numerical probes / KINF-2 foundations\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: Install the exact-algebra dependency\n        run: pip install sympy==1.14.0\n\n      - name: KINF-2 foundations probe\n        working-directory: verification/lean\n        run: |\n          echo "=== kinf2_foundations_probe.py ==="\n          python3 kinf2_foundations_probe.py\n\n'), ('probes_nb1, probes_a42_witness', 'probes_nb1, probes_kinf2, probes_a42_witness'), ('          NB1_RESULT: ${{ needs.probes_nb1.result }}\n', '          NB1_RESULT: ${{ needs.probes_nb1.result }}\n          KINF2_RESULT: ${{ needs.probes_kinf2.result }}\n'), ('          echo "nb1=${NB1_RESULT}"\n', '          echo "nb1=${NB1_RESULT}"\n          echo "kinf2=${KINF2_RESULT}"\n'), ('          test "${NB1_RESULT}" = success\n', '          test "${NB1_RESULT}" = success\n          test "${KINF2_RESULT}" = success\n')]
IMPORT_EDIT = ('import OIBridge.NativeGateBall\n', 'import OIBridge.NativeGateBall\nimport OIBridge.KInfFoundations\n')
FAMILY = {'name': 'the corrected field-neutral vocabulary of the pre-quantum completion — proper effects, boundary states read in the body, relative strict convexity, group-flow drivability — with Lemma C and its converse, the semantic controls, Lemmas B and D and the finite-exposure bounds (round KINF-2, reconstruction)', 'modules': ['KInfFoundations'], 'status': 'kernel-only', 'manuscript': [], 'note': 'Round KINF-2, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-kinf-2-foundations/preregistration.md, which records what it replaces in the halted round KINF-1. The kernel layer: given supporting-effect completeness, singleton faces are equivalent to relative strict convexity, each direction proved separately (relStrictConvex_of_supporting_singleton, singletonFaces_of_relStrictConvex); a non-proper effect changes neither premise; the semantic controls show each premise holding and failing on named bodies, drivability holding on the unit ball of R^3 and failing on the classical bit, and K∞-1 holding for the ball with its full effects and failing with the unit alone. Carried by no manuscript. The round sources none of its premises: drivability, supporting effects, singleton faces and copy naturality are discharged by no OI construction, and K∞-1 is proved for no physical family. That corrected drivability excludes the square gbit and the rebit disk is a written argument, not a kernel statement.'}
SENTENCES = {'KINF-2-FOUNDATIONS-PROVED': "In the kernel, at evidence level 2, over a real normed space and with no field, matrix carrier or substratum object, for the corrected vocabulary in which an effect is proper when some state gives it a value below one and a boundary state is read in the body alone: a non-proper effect, the unit among them, changes neither supporting-effect completeness nor singleton faces (`supportingEffectComplete_insert_iff`, `singletonFaces_insert_iff`); a convex body with supporting-effect completeness and singleton faces is relatively strictly convex (Lemma C, `relStrictConvex_of_supporting_singleton`), and a relatively strictly convex body has singleton faces for every effect family (`singletonFaces_of_relStrictConvex`), the two directions proved separately; each premise holds and fails on named bodies — singleton faces on every closed ball of a strictly convex space and not on the sup-norm square with its full effects, supporting-effect completeness on the segment `[-1, 1]` with its full effects and not with the unit alone, elementary drivability on the unit ball of `ℝ³` and not on the classical bit, and hypothesis K∞-1 for that ball with its full effects and not with the unit alone (`kInf1_ball3_full`, `not_kInf1_ball3_unit`); a centrally symmetric body admits at most two perfectly distinguishable states with any effects (Lemma D); a compact convex body with `0` in its interior whose frontier lies on the unit sphere is the closed unit ball (Lemma B); a finite stage exposes at most as many states as it has preparations, and a body on `N` ontic states meeting each coordinate facet in at most one point exposes at most `N` states by response effects (Theorem F2); joined in the verdict `kinf2_kernel_core`. The qubit certain face is a theorem of the imported matrix kinematics (`qubit_certain_face`), and hypothesis K∞-1 is the definition `KInf1`, proved for no physical family. In exact arithmetic replayed in CI, and not in the kernel, the round's probe instantiates the controls: the square gbit, the torus and Stiefel orbitopes and the regular pentagon violate singleton faces, the pentagon while strongly self-dual, transitive on ordered frames and of capacity two; the 3-ball satisfies every premise together; the SIC ball fails supporting-effect completeness with its response effects; the Carathéodory orbitope `C₂` has capacity three. Nothing here derives drivability, supporting effects, singleton faces or copy naturality from any OI construction; that corrected drivability excludes the square gbit and the rebit disk is a written argument and not a kernel statement; and nothing here is a reconstruction theorem.", 'KINF-2-UNDECIDED': 'The kernel verdict `kinf2_kernel_core` was not obtained. The statement at which the proof stopped is named, with what would settle it; the definitions stand as frozen, the exact layer stands as computed, and no lemma is stated as a result of this round beyond those the kernel checked.'}
CLAUSE = 'Round KINF-2 fixes the corrected field-neutral vocabulary of the pre-quantum operational completion — finite stages, effects, proper effects and certain faces, boundary states read in the body, supporting-effect completeness and singleton faces over proper effects, relative strict convexity, full effects, perfect distinguishability, central symmetry, elementary drivability as a group flow of automorphisms of the body, and copy naturality — in place of the vocabulary of the halted round KINF-1, and proves the lemmas that vocabulary supports together with a holding and a failing instance of each premise. It states hypothesis K∞-1 as a definition over compact convex bodies and proves it for no physical family. It sources none of its premises: it does not derive drivability, supporting effects, singleton faces or copy naturality from any OI construction, it does not decide which effects the completion makes available, it does not prove in the kernel that corrected drivability excludes the square gbit or the rebit disk, it freezes no self-duality or homogeneity premise, and it contains no reconstruction theorem. It edits no manuscript and no roadmap row.'
CLAUSE_MENTION = '**THE CLAUSE, carried at this mention — the result.**'
PROBE_OK_PREFIX = 'kinf2_foundations_probe: OK -- 192 checks'
FORBIDDEN_NOTE = ('OI supplies', 'OI derives', 'OI sources', 'sourced from OI', 'derived from the substratum', 'K∞-1 holds for the completion', 'K∞-1 is proved', 'proves K∞-1', 'reconstruction theorem for', 'the completion is a ball', 'full effects hold', 'excludes the square gbit in the kernel', 'kernel-certified exclusion', 'self-duality is excluded', 'self-duality is required')
SYNTHETIC_PROBE = b'# synthetic probe for the self-test\n'
FORBIDDEN = ('sorry', 'admit', 'native_decide', 'axiom ', 'unsafe', 'opaque ', 'implemented_by', 'extern')
ALLOWED_OPTION = 'set_option linter.unusedSectionVars false'
SHARED_PREFIX = 'kinf2_shared_'
KINF1_RECORD = 'verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/'


def blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


# ---- the expected tree ------------------------------------------------------------------------------------------
def expected_census(d_census):
    c = json.loads(d_census)
    c['families'].append(json.loads(json.dumps(FAMILY)))
    return (json.dumps(c, indent=2, ensure_ascii=False) + '\n').encode()


def expected_text(d_files, path):
    text = d_files[path].decode()
    if path == WORKFLOW:
        for old, new in WORKFLOW_EDITS:
            if text.count(old) != 1:
                raise ValueError('workflow anchor')
            text = text.replace(old, new)
        return text.encode()
    if path == IMPORTS:
        if text.count(IMPORT_EDIT[0]) != 1:
            raise ValueError('import anchor')
        return text.replace(*IMPORT_EDIT).encode()
    if path == CENSUS:
        return expected_census(d_files[path])
    return d_files[path]


# ---- the checks -------------------------------------------------------------------------------------------------
DECL_RE = re.compile(r'^(theorem|structure|def|noncomputable def|abbrev|instance|class|inductive) (\S+)', re.M)


def declaration(module, kind, name):
    """The frozen text of a declaration: a theorem from its keyword to the `:=` that opens its proof; a structure or
    a definition from its keyword to the blank line that ends it."""
    for sep in (' ', '\n'):
        k = module.find(kind + ' ' + name + sep)
        if k >= 0 and (k == 0 or module[k - 1] == '\n'):
            if kind == 'theorem':
                return module[k:module.index(':=', k) + 2]
            end = module.find('\n\n', k)
            return module[k:end if end >= 0 else len(module)]
    return None


def check_module(module, label):
    codes = []
    if not module.startswith(FROZEN['header']):
        codes.append('module:header')
    for tok in FORBIDDEN:
        if re.search(r'(?<![A-Za-z_])' + re.escape(tok) + ('' if tok.endswith(' ') else r'(?![A-Za-z_])'), module):
            codes.append('module:forbidden:' + tok.strip())
    for opt in re.findall(r'^set_option .*$', module, re.M):
        if opt != ALLOWED_OPTION:
            codes.append('module:set_option')
    found = DECL_RE.findall(module)
    theorems = [n for k, n in found if k == 'theorem']
    for kind, n in found:
        if kind == 'theorem':
            if n not in FROZEN['declarations'] and not n.startswith(SHARED_PREFIX):
                codes.append('module:unknown-name:' + n)
            line = PRINT.get(n, 'OIBridge.KInfFoundations.' + n)
            if module.count('#print axioms ' + line + '\n') != 1:
                codes.append('module:print-axioms:' + n)
        elif n not in FROZEN['declarations'] or FROZEN['declarations'][n][0] != kind:
            codes.append('module:unknown-definition:' + n)
    for n, (kind, text) in FROZEN['declarations'].items():
        if n == VERDICT and label != LABELS[0]:
            if n in theorems:
                codes.append('module:verdict-under-undecided')
            continue
        if declaration(module, kind, n) != text:
            codes.append('module:declaration:' + n)
    return codes


def check_note(note, label, module_blob):
    codes = []
    lines = note.split('\n')
    outs = [l for l in lines if l.startswith('**Outcome:**')]
    if outs != ['**Outcome:** `%s`' % label]:
        codes.append('note:outcome-line')
    for lab in LABELS:
        if note.count(SENTENCES[lab]) != (1 if lab == label else 0):
            codes.append('note:sentence:' + lab)
    if note.count(CLAUSE_MENTION) != 1 or note.count(CLAUSE) != 1 \
            or note.index(CLAUSE) < note.index(CLAUSE_MENTION):
        codes.append('note:clause')
    if sum(1 for l in lines if l.strip().strip('`').startswith(PROBE_OK_PREFIX)) != 1:
        codes.append('note:probe-line')
    if '`%s`' % REFERENCE_BLOB not in note or '`%s`' % module_blob not in note:
        codes.append('note:blobs')
    if module_blob != REFERENCE_BLOB and 'departure from the reference implementation' not in note:
        codes.append('note:departure')
    rest = note
    for t in list(SENTENCES.values()) + [CLAUSE]:
        rest = rest.replace(t, '')
    if any(ph.lower() in rest.lower() for ph in FORBIDDEN_NOTE):
        codes.append('note:forbidden-claim')
    return codes


def check_tree(d_files, e_files, changed, probe_blob=PROBE_BLOB):
    """d_files/e_files: path -> bytes (None if absent) for every path consulted; changed: {path: 'A'|'M'|'D'}."""
    codes = []
    note = e_files.get(RDIR + 'result.md')
    if note is None:
        return ['note:absent']
    note = note.decode()
    m = re.search(r'^\*\*Outcome:\*\* `([^`]*)`', note, re.M)
    label = m.group(1) if m and m.group(1) in LABELS else None
    if label is None:
        return ['note:outcome-line']
    module = e_files.get(MODULE)
    if module is None:
        return ['module:absent']
    codes += check_module(module.decode(), label)
    codes += check_note(note, label, blob(module))
    if e_files.get(PROBE) is None or blob(e_files[PROBE]) != probe_blob:
        codes.append('probe:blob')
    for path in (WORKFLOW, IMPORTS, CENSUS):
        try:
            exp = expected_text(d_files, path)
        except ValueError:
            exp = None
        if e_files.get(path) != exp:
            codes.append('surface:' + path)
    want = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
            MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    if changed != want:
        codes.append('paths')
    return codes


# ---- git access -------------------------------------------------------------------------------------------------
def git(*args):
    return subprocess.run(('git',) + args, capture_output=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def consulted():
    return [RDIR + 'result.md', RDIR + 'preregistration.md', MODULE, PROBE, WORKFLOW, IMPORTS, CENSUS]


def cmd_check(commit, freeze=None):
    d_files = {p: show(D, p) for p in consulted()}
    e_files = {p: show(commit, p) for p in consulted()}
    changed = {}
    for line in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, path = line.split('\t', 1)
        changed[path] = st
    codes = check_tree(d_files, e_files, changed)
    if freeze:
        fdiff = git('diff', '--no-renames', '--name-status', D, freeze).decode().split()
        if fdiff != ['A', RDIR + 'preregistration.md']:
            codes.append('freeze:delta')
        if show(freeze, RDIR + 'preregistration.md') != e_files[RDIR + 'preregistration.md']:
            codes.append('freeze:preregistration')
    if codes:
        print('controls: check FAILED: ' + '; '.join(codes))
        return 1
    print('controls: check OK')
    return 0


# ---- self-test --------------------------------------------------------------------------------------------------
def synthetic_module(label):
    parts = [FROZEN['header'], 'namespace OIBridge\nnamespace KInfFoundations\n\n']
    names = []
    for n, (kind, text) in FROZEN['declarations'].items():
        if n == VERDICT and label != LABELS[0]:
            continue
        if kind == 'theorem':
            parts.append(text + ' by\n  exact placeholder\n\n')
            names.append(n)
        else:
            parts.append(text + '\n\n')
    parts.append('end KInfFoundations\nend OIBridge\n\n')
    for n in names:
        parts.append('#print axioms %s\n' % PRINT[n])
    return ''.join(parts).encode()


def synthetic_row(d_files, label):
    e = dict(d_files)
    module = synthetic_module(label)
    e[MODULE] = module
    e[PROBE] = SYNTHETIC_PROBE
    for path in (WORKFLOW, IMPORTS, CENSUS):
        e[path] = expected_text(d_files, path)
    e[RDIR + 'preregistration.md'] = b'frozen'
    note = ['# result', '', '**Outcome:** `%s`' % label, '', SENTENCES[label], '', CLAUSE_MENTION, '', CLAUSE, '',
            '`' + PROBE_OK_PREFIX + ' (synthetic)`', '',
            'reference `%s`, module at E `%s`, departure from the reference implementation' % (REFERENCE_BLOB, blob(module))]
    e[RDIR + 'result.md'] = '\n'.join(note).encode()
    changed = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
               MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    return e, changed


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    bad = []
    for lab in LABELS:
        if prereg.count(SENTENCES[lab]) != 1:
            bad.append('prereg:sentence:' + lab)
    if prereg.count(CLAUSE) < 1:
        bad.append('prereg:clause')
    if FROZEN['header'].rstrip('\n') not in prereg:
        bad.append('prereg:header')
    for n, (kind, text) in FROZEN['declarations'].items():
        if text not in prereg:
            bad.append('prereg:declaration:' + n)
    if WORKFLOW_JOB not in prereg:
        bad.append('prereg:workflow')
    if FAMILY['name'] not in prereg or FAMILY['note'] not in prereg:
        bad.append('prereg:census-family')
    for b in (PROBE_BLOB, REFERENCE_BLOB):
        if b not in prereg:
            bad.append('prereg:blob:' + b)
    if prereg.count(PROBE_OK_PREFIX) < 1:
        bad.append('prereg:probe-line')
    if bad:
        print('controls: self-test FAILED (constants): ' + '; '.join(bad))
        return 1
    print('controls: the frozen constants match the preregistration beside this file')

    d_files = {p: show(D, p) for p in consulted()}
    rows = {}
    for lab in LABELS:
        e, ch = synthetic_row(d_files, lab)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if codes:
            print('controls: self-test FAILED: synthetic row %s: %s' % (lab, codes))
            return 1
        rows[lab] = (e, ch)
    print('controls: 2 rows hold as frozen')

    muts = []
    def mut(name, code, label, fn):
        muts.append((name, code, label, fn))
    P, U = LABELS
    def edit_file(path, old, new):
        def f(e, ch):
            if old.encode() not in e[path]:
                raise AssertionError('mutation anchor absent: ' + old)
            e[path] = e[path].replace(old.encode(), new.encode(), 1)
        return f
    def append_note(text):
        return lambda e, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + text.encode())
    mut('verdict removed under FOUNDATIONS-PROVED', 'module:declaration:' + VERDICT, P,
        edit_file(MODULE, 'theorem ' + VERDICT, 'theorem kinf2_other'))
    mut('verdict present under UNDECIDED', 'module:verdict-under-undecided', U,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE] + FROZEN['declarations'][VERDICT][1].encode()
                                    + b' by\n  x\n#print axioms ' + PRINT[VERDICT].encode() + b'\n'))
    mut('K-infinity-1 made trivially true', 'module:declaration:KInf1', P,
        edit_file(MODULE, 'def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n',
                  'def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop := True ∨\n'))
    mut('K-infinity-1 without compactness', 'module:declaration:KInf1', P,
        edit_file(MODULE, 'IsCompact Ω → Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) →',
                  'Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) →'))
    mut('properness made syntactic (the KINF-1 defect on finite stages)', 'module:declaration:IsProperOn', P,
        edit_file(MODULE, '  ∃ y ∈ Ω, e y < 1', '  e ≠ AffineMap.const ℝ V 1'))
    mut('the boundary read in V (the KINF-1 frontier)', 'module:declaration:IsBoundaryState', P,
        edit_file(MODULE, '  x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε : ℝ, 0 < ε → x + ε • (x - y) ∉ Ω', '  x ∈ frontier Ω'))
    mut('supporting-effect completeness without properness (the unit trivializes it)',
        'module:declaration:SupportingEffectComplete', P,
        edit_file(MODULE, 'IsEffectOn Ω e ∧ IsProperOn Ω e ∧ e x = 1', 'IsEffectOn Ω e ∧ e x = 1'))
    mut('singleton faces without properness (the unit falsifies it)', 'module:declaration:SingletonFaces', P,
        edit_file(MODULE, 'IsEffectOn Ω e → IsProperOn Ω e → (certainFace Ω e).Subsingleton',
                  'IsEffectOn Ω e → (certainFace Ω e).Subsingleton'))
    mut('relative strict convexity without the boundary clause', 'module:declaration:RelStrictConvex', P,
        edit_file(MODULE, 'a • x + b • y ∈ Ω ∧ ¬ IsBoundaryState Ω (a • x + b • y)', 'a • x + b • y ∈ Ω'))
    mut('drivability without the group law', 'module:declaration:ElementaryDrivability', P,
        edit_file(MODULE, '  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)\n', ''))
    mut('drivability with J mapping into the body only', 'module:declaration:ElementaryDrivability', P,
        edit_file(MODULE, '  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω\n', ''))
    mut('the off-axis clause compared on V', 'module:declaration:ElementaryDrivability', P,
        edit_file(MODULE, '∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x',
                  '∃ t, ∀ s, ∃ x, J (flow t (J.symm x)) ≠ flow s x'))
    mut('Lemma C without singleton faces', 'module:declaration:relStrictConvex_of_supporting_singleton', P,
        edit_file(MODULE, '(hSF : SingletonFaces Ω avail) : RelStrictConvex Ω :=', ': RelStrictConvex Ω :='))
    mut('the converse restricted to one family', 'module:declaration:singletonFaces_of_relStrictConvex', P,
        edit_file(MODULE, '(h : RelStrictConvex Ω) : SingletonFaces Ω avail :=',
                  '(h : RelStrictConvex Ω) : SingletonFaces Ω (fullEffects Ω) :='))
    mut('the square control turned positive', 'module:declaration:not_singletonFaces_square', P,
        edit_file(MODULE, 'theorem not_singletonFaces_square :\n    ¬ SingletonFaces',
                  'theorem not_singletonFaces_square :\n    SingletonFaces'))
    mut('the bit control moved to a point', 'module:declaration:not_drivable_Icc', P,
        edit_file(MODULE, 'theorem not_drivable_Icc : IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) :=',
                  'theorem not_drivable_Icc : IsEmpty (ElementaryDrivability (Set.Icc (0 : ℝ) 0)) :='))
    mut('the ball redefined', 'module:declaration:ball3', P,
        edit_file(MODULE, '{v | v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}', '{v | v 0 ^ 2 + v 1 ^ 2 ≤ 1}'))
    mut('the unit control on K-infinity-1 turned positive', 'module:declaration:not_kInf1_ball3_unit', P,
        edit_file(MODULE, 'theorem not_kInf1_ball3_unit : ¬ KInf1 ball3', 'theorem not_kInf1_ball3_unit : KInf1 ball3'))
    mut('Lemma D loosened', 'module:declaration:card_le_two_of_centrallySymmetric', P,
        edit_file(MODULE, '(hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 :=',
                  '(hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 3 :='))
    mut('Lemma B without the interior hypothesis', 'module:declaration:eq_closedBall_of_frontier_subset_sphere', P,
        edit_file(MODULE, '(hcomp : IsCompact Ω) (h0 : (0 : V) ∈ interior Ω)', '(hcomp : IsCompact Ω)'))
    mut('Theorem F2 without the facet hypothesis', 'module:declaration:classical_exposed_ncard_le', P,
        edit_file(MODULE, '    (hfacet : ∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) :\n    {x | ClassicallyExposed Ω x}.ncard ≤ N :=',
                  '    {x | ClassicallyExposed Ω x}.ncard ≤ N :='))
    mut('the header claims a sourcing', 'module:header', P,
        edit_file(MODULE, 'It sources nothing', 'It sources drivability'))
    mut('an import added to the header', 'module:header', P,
        edit_file(MODULE, 'import OIBridge.CoherentExtension\n',
                  'import OIBridge.CoherentExtension\nimport OIBridge.SubstratumSource\n'))
    mut('a definition added', 'module:unknown-definition:extra', P,
        edit_file(MODULE, 'end KInfFoundations', 'def extra : Nat := 0\n\nend KInfFoundations'))
    mut('a missing #print axioms', 'module:print-axioms:relStrictConvex_of_supporting_singleton', P,
        edit_file(MODULE, '#print axioms OIBridge.KInfFoundations.relStrictConvex_of_supporting_singleton\n', ''))
    mut('sorry in the module', 'module:forbidden:sorry', P, edit_file(MODULE, 'exact placeholder', 'sorry'))
    mut('an axiom declared', 'module:forbidden:axiom', P,
        edit_file(MODULE, 'end KInfFoundations', 'axiom kinf : True\n\nend KInfFoundations'))
    mut('an unlisted theorem name', 'module:unknown-name:helper', P,
        edit_file(MODULE, 'end KInfFoundations', 'theorem helper : True := trivial\n\nend KInfFoundations'))
    mut('a set_option', 'module:set_option', P,
        edit_file(MODULE, 'namespace KInfFoundations\n', 'namespace KInfFoundations\nset_option maxHeartbeats 0\n'))
    mut('the probe changed', 'probe:blob', P, lambda e, ch: e.__setitem__(PROBE, b'# not the frozen probe\n'))
    mut('the workflow edited beyond the frozen edit', 'surface:' + WORKFLOW, P,
        lambda e, ch: e.__setitem__(WORKFLOW, e[WORKFLOW] + b'# extra\n'))
    mut('the probe shard left out of the aggregate', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, '          test "${KINF2_RESULT}" = success\n', ''))
    mut('the exact-algebra dependency unpinned', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, 'pip install sympy==1.14.0', 'pip install sympy'))
    mut('the import misplaced', 'surface:' + IMPORTS, P,
        lambda e, ch: e.__setitem__(IMPORTS, d_files[IMPORTS] + b'import OIBridge.KInfFoundations\n'))
    mut('the census family made current', 'surface:' + CENSUS, P,
        lambda e, ch: e.__setitem__(CENSUS, b'"status": "current"'.join(e[CENSUS].rsplit(b'"status": "kernel-only"', 1))))
    mut('a manuscript touched', 'paths', P, lambda e, ch: ch.__setitem__('papers/Main.md', 'M'))
    mut('the roadmap touched', 'paths', P, lambda e, ch: ch.__setitem__('verification/ROADMAP.md', 'M'))
    mut('the halted round KINF-1 record touched', 'paths', P,
        lambda e, ch: ch.__setitem__(KINF1_RECORD + 'result.md', 'M'))
    mut('a governed path missing', 'paths', P, lambda e, ch: ch.pop(WORKFLOW))
    mut('two outcome lines', 'note:outcome-line', P, append_note('\n**Outcome:** `%s`\n' % U))
    mut("the other label's sentence", 'note:sentence:' + U, P, append_note('\n' + SENTENCES[U]))
    mut('the clause missing', 'note:clause', P, edit_file(RDIR + 'result.md', CLAUSE, ''))
    mut('the clause before its mention', 'note:clause', P,
        lambda e, ch: e.__setitem__(RDIR + 'result.md', CLAUSE.encode() + b'\n' + e[RDIR + 'result.md'].replace(CLAUSE.encode(), b'')))
    mut('the probe line missing', 'note:probe-line', P, edit_file(RDIR + 'result.md', PROBE_OK_PREFIX, 'probe'))
    mut('the blobs missing', 'note:blobs', P, edit_file(RDIR + 'result.md', REFERENCE_BLOB, 'x'))
    mut('the departure unreported', 'note:departure', P,
        edit_file(RDIR + 'result.md', 'departure from the reference implementation', ''))
    mut('the note claims OI supplies the premises', 'note:forbidden-claim', P,
        append_note('\nHence OI supplies drivability.\n'))
    mut('the note claims K-infinity-1 holds for the completion', 'note:forbidden-claim', U,
        append_note('\nSo K∞-1 holds for the completion.\n'))
    mut('no result note', 'note:absent', P, lambda e, ch: e.__setitem__(RDIR + 'result.md', None))
    failed = 0
    for name, code, lab, fn in muts:
        e, ch = synthetic_row(d_files, lab)
        fn(e, ch)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if code not in codes:
            print('controls: self-test FAILED: mutation "%s" did not fail with %s (got %s)' % (name, code, codes))
            failed += 1
    if failed:
        return 1
    print('controls: %d mutation controls fail as required' % len(muts))
    print('controls: self-test OK')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--self-test']:
        sys.exit(self_test())
    if len(a) in (2, 4) and a[0] == 'check' and (len(a) == 2 or a[2] == '--freeze'):
        sys.exit(cmd_check(a[1], a[3] if len(a) == 4 else None))
    print(__doc__)
    sys.exit(2)
