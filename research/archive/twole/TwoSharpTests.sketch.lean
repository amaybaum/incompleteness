/- Uncompiled sketch (thread TWO-LE, read-only). Statements are the target; proofs are plans. -/
import OIBridge.K2Guard

namespace OIBridge
namespace TwoLe
open KInfFoundations OrbitGeneration TransitiveBody CompositeDimension EffectSpace

variable {V : Type*} [AddCommGroup V] [Module ℝ V] {d : ℕ}

/-- Two sharp binary tests of `Ω`, distinct on `Ω` from each other and from each other's
complement. Test identity is agreement on the states of `Ω`. -/
def TwoSharpTests (Ω : Set V) : Prop :=
  ∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧
    (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)

/-- T1: the complement of the sharp effect along `b` is the sharp effect along `-b`. -/
theorem sharpEff_neg_apply (b x : Fin d → ℝ) : sharpEff (-b) x = 1 - sharpEff b x := by
  rw [sharpEff_apply, sharpEff_apply]
  have : ∑ j, (-b) j / 2 * x j = -∑ j, b j / 2 * x j := by
    rw [← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun j _ => by rw [Pi.neg_apply]; ring
  rw [this]; ring

/-- T2: every sharp seed of `eball d` is a sharp directional effect along a unit vector. -/
theorem sharpSeed_eq_sharpEff {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (h : SharpSeed (eball d) e) :
    ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u := by
  obtain ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ := h
  obtain ⟨hs, heq⟩ := sharp_eq_of_certain he hu hw h1 h0
  exact ⟨u, hs, heq⟩

/-- T3: `eball 0` has no sharp seed. -/
theorem not_sharpSeed_zero (e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ) : ¬ SharpSeed (eball 0) e := by
  rintro ⟨-, ⟨x, -, h1⟩, ⟨y, -, h0⟩⟩
  have : x = y := Subsingleton.elim x y
  rw [this] at h1; rw [h1] at h0; norm_num at h0

/-- T4: on `eball 1` every two sharp seeds agree or are complementary on every state. -/
theorem not_twoSharpTests_one : ¬ TwoSharpTests (eball 1) := by
  rintro ⟨e, f, he, hf, ⟨x, -, hx⟩, ⟨y, -, hy⟩⟩
  obtain ⟨u, hu, rfl⟩ := sharpSeed_eq_sharpEff he
  obtain ⟨v, hv, rfl⟩ := sharpSeed_eq_sharpEff hf
  -- u 0 ^ 2 = 1 and v 0 ^ 2 = 1, so v = u or v = -u
  sorry

/-- T5: for `2 ≤ d`, the first two coordinate directions give two inequivalent tests. -/
theorem twoSharpTests_of_two_le (hd : 2 ≤ d) : TwoSharpTests (eball d) := by
  sorry

/-- T6. -/
theorem twoSharpTests_iff : TwoSharpTests (eball d) ↔ 2 ≤ d := by
  sorry

end TwoLe
end OIBridge
