/-
  UNCOMPILED SKETCH (thread SS, read-only research). No Lean toolchain was available; nothing here is
  kernel-checked, frozen or proposed for landing. Vocabulary: base 68b6df06 plus SharpTests.lean from the
  K1-SHARP-TESTS-1 worktree (e0cf9151). Names marked † do not exist.

  Part 1 — the uniform single-system instance (mirrors the landed d = 1 template
  `SharpTests.two_le_load_bearing_relative`, SharpTests.lean:185, at every d ≥ 2).
  Part 2 — the candidate composite-free selector UE (a named proposal, not a premise of anything).
-/
import OIBridge.SharpTests

namespace OIBridge
namespace SSSketch

open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension EffectSpace K1Bridge
open SharpTests

variable {d : ℕ}

/-! ### Part 1 -/

-- † the reflection along the first axis flips it: reflLin m m = -m when m ≠ 0
theorem reflLin_self {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) : reflLin m m = -m := by
  funext i
  simp only [reflLin_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul, Pi.neg_apply]
  have : (∑ j, m j * m j) = ∑ j, m j ^ 2 := Finset.sum_congr rfl fun j _ => by ring
  rw [this, mul_div_assoc, div_self hm]; ring

-- † IsNot for the axis reflection, every d > 0
theorem isNot_reflAxis (hd : 0 < d) : IsNot (eball d) (axisVec hd) (reflLin (axisVec hd)) where
  unit := axisVec_sq hd
  invol := reflLin_reflLin (by rw [axisVec_sq hd]; norm_num)
  preserves := fun x hx => by
    rw [mem_eball] at hx ⊢; rw [reflLin_sq (by rw [axisVec_sq hd]; norm_num)]; exact hx
  flips := reflLin_self (by rw [axisVec_sq hd]; norm_num)

/-- † Every single-system hypothesis of `K2Guard.three_of_nativeGateOf_of_two_le` holds at every
`d ≥ 2`, with one uniform instance. -/
theorem singleSystem_uniform (hd : 2 ≤ d) :
    EffectsOn (eball d) (fullEffects (eball d)) ∧ PreservesBody (eball d) (fullAut d) ∧
      SharpSeed (eball d) (sharpEff (axisVec (by omega : 0 < d))) ∧
      BoundaryTransitive (eball d) (fullAut d) ∧
      SeedOrbitAvailable (fullAut d) (sharpEff (axisVec (by omega : 0 < d))) (fullEffects (eball d)) ∧
      IsNot (eball d) (axisVec (by omega : 0 < d)) (reflLin (axisVec (by omega : 0 < d))) ∧
      HasTwoSharpTests (eball d) :=
  ⟨fun _ he => he, preservesBody_fullAut, sharpEff_sharpSeed (axisVec_sq _),
    boundaryTransitive_fullAut,
    fun g hg => isEffectOn_seedTransport (sharpEff_isEffectOn (axisVec_sq _))
      fun x hx => (preservesBody_fullAut g hg x hx).2,
    isNot_reflAxis _, hasTwoSharpTests_of_two_le hd⟩

/-- † Corollary: the single-system hypotheses do not select `d = 3` (instance `d = 4`). The number 3 is
carried by `NativeGateOf` alone in the current chain. -/
theorem singleSystem_not_select :
    ¬ (∀ d : ℕ, 2 ≤ d → (∃ (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))
        (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)),
        EffectsOn (eball d) avail ∧ PreservesBody (eball d) G ∧ SharpSeed (eball d) r ∧
        BoundaryTransitive (eball d) G ∧ SeedOrbitAvailable G r avail ∧ IsNot (eball d) z N ∧
        HasTwoSharpTests (eball d)) → d = 3) := by
  intro h
  obtain ⟨h1, h2, h3, h4, h5, h6, h7⟩ := singleSystem_uniform (d := 4) (by norm_num)
  exact absurd (h 4 (by norm_num) ⟨_, _, _, _, _, h1, h2, h3, h4, h5, h6, h7⟩) (by norm_num)

/-! ### Part 2 — candidate UE (proposal) -/

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

-- † a continuous flow of body automorphisms (the flow fields of `ElementaryDrivability`, KF:264)
structure BodyFlow (Ω : Set V) where
  flow : ℝ → V ≃ᵃ[ℝ] V
  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)
  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2
  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω

-- † a test conserved by the flow
def Conserved {Ω : Set V} (φ : BodyFlow Ω) (e : V →ᵃ[ℝ] ℝ) : Prop := ∀ t x, e (φ.flow t x) = e x

-- † UE: every nontrivial body flow conserves exactly one sharp test, up to complementation, with test
-- identity read as agreement on Ω (TWO-LE G1). Quantifies over ALL body flows: this is where the
-- flow no-restriction premise (FNR) sits.
def UniqueEnergyTest (Ω : Set V) : Prop :=
  ∀ φ : BodyFlow Ω, (∃ t, ∃ x ∈ Ω, φ.flow t x ≠ x) →
    ∃ e, SharpSeed Ω e ∧ Conserved φ e ∧
      ∀ f, SharpSeed Ω f → Conserved φ f → (∀ x ∈ Ω, f x = e x) ∨ (∀ x ∈ Ω, f x = 1 - e x)

/-- † Candidate theorem. Proof plan (written in SS-LEDGER §4):
  (→) d = 2: the rotation flow conserves no sharp test (at t = π/2, Rᵀu = u forces u = 0);
      d ≥ 4: the rotation flow in the plane (0,1) conserves sharpEff e₂ and sharpEff e₃, separated
      modulo complementation at x = e₂ (values 1, 1/2, 0). Both kernel-cheap given a d-dimensional
      plane-rotation flow (generalizing `rot3`).
  (←) d ≤ 1: no nontrivial body flow (finite automorphism orbits, `isEmpty_drivability_of_finite_orbits`
      style, ON:124); d = 3: body automorphisms are orthogonal (centroid fixed, TB:356; sum of squares),
      flow members have det 1 (continuity), each nontrivial member fixes an axis, commuting members share
      it (choose a member that is not a half-turn), the sign along the axis is continuous, so the axis
      ±w is conserved; a second conserved non-complementary test would fix a plane pointwise, forcing
      the identity. No Lie structure theory is used. -/
theorem uniqueEnergyTest_eball_iff : UniqueEnergyTest (eball d) ↔ d ≤ 1 ∨ d = 3 := by
  sorry

/-- † With K1-SHARP-TESTS-1's predicate: two sharp tests and UE give d = 3, with no composite. -/
theorem three_of_twoSharp_uniqueEnergy (h2 : HasTwoSharpTests (eball d))
    (hUE : UniqueEnergyTest (eball d)) : d = 3 := by
  have := hasTwoSharpTests_iff.mp h2
  rcases uniqueEnergyTest_eball_iff.mp hUE with h | h <;> omega

end SSSketch
end OIBridge
