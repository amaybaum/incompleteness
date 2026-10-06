/-
  OIBridge/TwoSharpTests.lean — design check (thread TWO-LE): `2 ≤ d` on the coordinate ball as the
  existence of two sharp binary tests inequivalent modulo complementation.

  `TwoSharpTests Ω` asks for two sharp seeds `e`, `f` of `Ω` (OG-1's `SharpSeed`: an effect with a
  certain state and a zero state) such that some state of `Ω` separates `f` from `e` and some state
  separates `f` from the complement `1 - e`. Test identity is agreement on the states of `Ω`.

  On `eball d`: the complement of the sharp effect along `b` is the sharp effect along `-b`
  (`sharpEff_neg_apply`); every sharp seed is a sharp directional effect along a unit vector
  (`sharpSeed_iff`); at `d = 0` there is no sharp seed (`not_sharpSeed_zero`); at `d = 1` any two
  sharp seeds agree or are complementary on every state (`eq_or_compl_one`); at `2 ≤ d` two axis
  tests witness the predicate (`twoSharpTests_of_two_le`); hence `TwoSharpTests (eball d) ↔ 2 ≤ d`
  (`twoSharpTests_iff`), one direction from the `d ≤ 1` cases and one from the witness.

  Control: at `d = 1` every hypothesis of the relative dimension selector except `2 ≤ d` holds, with
  the full effect family, the full automorphism family, the sharp seed along `z1`, DIM-1's NOT and
  the classical gate `cnot1` (`two_le_load_bearing_relative`).

  The predicate is a statement about the derived ball; nothing here sources it from any
  construction.
-/
import OIBridge.K1Bridge

namespace OIBridge
namespace TwoSharpTests

open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface
open EffectSpace K1Bridge

variable {V : Type*} [AddCommGroup V] [Module ℝ V] {d : ℕ}

/-- Two sharp binary tests of `Ω`, separated on `Ω` from each other and from each other's
complement. -/
def TwoSharpTests (Ω : Set V) : Prop :=
  ∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧
    (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)

/-! ### §A — complement and classification -/

/-- The complement of the sharp effect along `b` is the sharp effect along `-b`. -/
theorem sharpEff_neg_apply (b x : Fin d → ℝ) : sharpEff (-b) x = 1 - sharpEff b x := by
  rw [sharpEff_apply, sharpEff_apply]
  have h : ∑ j, (-b) j / 2 * x j = -∑ j, b j / 2 * x j := by
    rw [← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun j _ => by rw [Pi.neg_apply]; ring
  rw [h]
  ring

/-- Every sharp seed of `eball d` is the sharp effect along a unit vector. -/
theorem sharpSeed_eq_sharpEff {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (h : SharpSeed (eball d) e) :
    ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u := by
  obtain ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ := h
  exact ⟨u, sharp_eq_of_certain he hu hw h1 h0⟩

/-- The sharp seeds of `eball d` are exactly the sharp effects along unit vectors. -/
theorem sharpSeed_iff (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) :
    SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u := by
  constructor
  · exact sharpSeed_eq_sharpEff
  · rintro ⟨u, hu, rfl⟩
    exact sharpEff_sharpSeed hu

/-! ### §B — `d = 0` and `d = 1` -/

/-- `eball 0` has no sharp seed. -/
theorem not_sharpSeed_zero (e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ) : ¬ SharpSeed (eball 0) e := by
  rintro ⟨-, ⟨x, -, h1⟩, ⟨y, -, h0⟩⟩
  have hxy : x = y := Subsingleton.elim x y
  rw [hxy, h0] at h1
  norm_num at h1

theorem not_twoSharpTests_zero : ¬ TwoSharpTests (eball 0) := by
  rintro ⟨e, -, he, -⟩
  exact not_sharpSeed_zero e he

/-- On `eball 1` any two sharp seeds agree on every state or are complementary on every state. -/
theorem eq_or_compl_one {e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ} (he : SharpSeed (eball 1) e)
    (hf : SharpSeed (eball 1) f) :
    (∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x) := by
  obtain ⟨u, hu, rfl⟩ := sharpSeed_eq_sharpEff he
  obtain ⟨v, hv, rfl⟩ := sharpSeed_eq_sharpEff hf
  rw [Fin.sum_univ_one] at hu hv
  have hprod : (v 0 - u 0) * (v 0 + u 0) = 0 := by
    have : (v 0 - u 0) * (v 0 + u 0) = v 0 ^ 2 - u 0 ^ 2 := by ring
    rw [this, hu, hv]
    ring
  rcases mul_eq_zero.1 hprod with h | h
  · left
    intro x _
    rw [sharpEff_apply, sharpEff_apply, Fin.sum_univ_one, Fin.sum_univ_one]
    have : v 0 = u 0 := by linarith
    rw [this]
  · right
    intro x _
    rw [sharpEff_apply, sharpEff_apply, Fin.sum_univ_one, Fin.sum_univ_one]
    have : v 0 = -u 0 := by linarith
    rw [this]
    ring

theorem not_twoSharpTests_one : ¬ TwoSharpTests (eball 1) := by
  rintro ⟨e, f, he, hf, ⟨x, hx, hne⟩, ⟨y, hy, hnc⟩⟩
  rcases eq_or_compl_one he hf with h | h
  · exact hne (h x hx)
  · exact hnc (h y hy)

/-! ### §C — the witness at `2 ≤ d` and the equivalence -/

theorem single_sq (i : Fin d) : ∑ j, (Pi.single i (1 : ℝ) : Fin d → ℝ) j ^ 2 = 1 := by
  rw [Finset.sum_eq_single i]
  · simp
  · intro j _ hj
    simp [hj]
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem sharpEff_single_single {i k : Fin d} (hik : i ≠ k) :
    sharpEff (Pi.single k (1 : ℝ)) (Pi.single i (1 : ℝ)) = 1 / 2 := by
  rw [sharpEff_apply]
  have h : ∑ j, (Pi.single k (1 : ℝ) : Fin d → ℝ) j / 2 * (Pi.single i (1 : ℝ) : Fin d → ℝ) j
      = 0 := by
    refine Finset.sum_eq_zero fun j _ => ?_
    by_cases hj : j = i
    · subst hj
      simp [hik]
    · simp [hj]
  rw [h]
  ring

/-- At `2 ≤ d` the sharp tests along the first two axes witness `TwoSharpTests`. -/
theorem twoSharpTests_of_two_le (hd : 2 ≤ d) : TwoSharpTests (eball d) := by
  let i : Fin d := ⟨0, by omega⟩
  let k : Fin d := ⟨1, by omega⟩
  have hik : i ≠ k := by
    intro h
    have := congrArg Fin.val h
    simp [i, k] at this
  refine ⟨sharpEff (Pi.single i 1), sharpEff (Pi.single k 1), sharpEff_sharpSeed (single_sq i),
    sharpEff_sharpSeed (single_sq k), ⟨Pi.single i 1, mem_eball_of_sphere (single_sq i), ?_⟩,
    ⟨Pi.single i 1, mem_eball_of_sphere (single_sq i), ?_⟩⟩
  · rw [sharpEff_single_single hik, sharpEff_self (single_sq i)]
    norm_num
  · rw [sharpEff_single_single hik, sharpEff_self (single_sq i)]
    norm_num

/-- **The equivalence.** On `eball d`, two sharp binary tests inequivalent modulo complementation
exist exactly when `2 ≤ d`: one direction from the cases `d = 0` and `d = 1`, the other from the
axis witness. -/
theorem twoSharpTests_iff : TwoSharpTests (eball d) ↔ 2 ≤ d := by
  constructor
  · intro h
    by_contra hlt
    have : d = 0 ∨ d = 1 := by omega
    rcases this with rfl | rfl
    · exact not_twoSharpTests_zero h
    · exact not_twoSharpTests_one h
  · exact twoSharpTests_of_two_le

/-! ### §D — control: `2 ≤ d` is load-bearing for the relative selector -/

theorem z1_sq : ∑ j, z1 j ^ 2 = 1 := by
  rw [Fin.sum_univ_one]
  simp

theorem nativeGateOf_cnot1 : NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 where
  frame := nativeGate_cnot1.frame
  posFwd x hx y hy := by
    rw [maxConeOf_fullEffects]
    exact nativeGate_cnot1.posFwd x hx y hy
  posInv x hx y hy := by
    rw [maxConeOf_fullEffects]
    exact nativeGate_cnot1.posInv x hx y hy
  relT := nativeGate_cnot1.relT
  relC := nativeGate_cnot1.relC

/-- At `d = 1` every hypothesis of the relative selector other than `2 ≤ d` holds: effect
soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, DIM-1's NOT and the relative native-gate
hypotheses, for the full effect family and the full automorphism family. -/
theorem two_le_load_bearing_relative :
    EffectsOn (eball 1) (fullEffects (eball 1)) ∧ PreservesBody (eball 1) (fullAut 1) ∧
      SharpSeed (eball 1) (sharpEff z1) ∧ BoundaryTransitive (eball 1) (fullAut 1) ∧
      SeedOrbitAvailable (fullAut 1) (sharpEff z1) (fullEffects (eball 1)) ∧
      IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧
      ¬ (2 ≤ 1) :=
  ⟨fun _ he => he, preservesBody_fullAut, sharpEff_sharpSeed z1_sq, boundaryTransitive_fullAut,
    fun g hg => isEffectOn_seedTransport (sharpEff_isEffectOn z1_sq)
      fun x hx => (preservesBody_fullAut g hg x hx).2,
    isNot_neg1, nativeGateOf_cnot1, by norm_num⟩

end TwoSharpTests
end OIBridge

#print axioms OIBridge.TwoSharpTests.sharpEff_neg_apply
#print axioms OIBridge.TwoSharpTests.sharpSeed_iff
#print axioms OIBridge.TwoSharpTests.not_sharpSeed_zero
#print axioms OIBridge.TwoSharpTests.not_twoSharpTests_zero
#print axioms OIBridge.TwoSharpTests.eq_or_compl_one
#print axioms OIBridge.TwoSharpTests.not_twoSharpTests_one
#print axioms OIBridge.TwoSharpTests.twoSharpTests_of_two_le
#print axioms OIBridge.TwoSharpTests.twoSharpTests_iff
#print axioms OIBridge.TwoSharpTests.nativeGateOf_cnot1
#print axioms OIBridge.TwoSharpTests.two_le_load_bearing_relative
