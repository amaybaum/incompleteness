/-
  OIBridge/SharpTests.lean — round K1-SHARP-TESTS-1: the premise `2 ≤ d` of the dimension selector,
  on the coordinate ball, as the existence of two sharp binary tests distinct modulo complementation.

  `HasTwoSharpTests Ω` asks for two sharp seeds `e`, `f` of `Ω` (OG-1's `SharpSeed`: an effect with a
  certain state and a zero state) such that some state of `Ω` separates `f` from `e` and some state
  separates `f` from the complement `1 - e`. Test identity is agreement on the states of `Ω`.

  (A) On `eball d`: the complement of the sharp effect along `b` is the sharp effect along `-b`
  (`sharpEff_neg_apply`); the sharp seeds are exactly the sharp effects along unit vectors
  (`sharpSeed_iff`, through EFF-1's `sharp_eq_of_certain`); `eball 0` has no sharp seed
  (`not_sharpSeed_zero`); on `eball 1` any two sharp seeds agree on every state or are complementary
  on every state (`eq_or_compl_one`); for `2 ≤ d` the sharp tests along the first two axes witness the
  predicate (`hasTwoSharpTests_of_two_le`). Hence `HasTwoSharpTests (eball d) ↔ 2 ≤ d`
  (`hasTwoSharpTests_iff`): the forward direction from the cases `d = 0` and `d = 1`, the converse
  from the axis witness.

  (B) At `d = 1`, the full effect family, the full automorphism family, the sharp seed along `z1`,
  DIM-1's NOT `neg1` and the gate `cnot1` satisfy effect soundness, body preservation, K∞-Seed,
  K∞-Trans, K∞-V4, `IsNot` and `NativeGateOf` (`two_le_load_bearing_relative`). So those hypotheses
  together do not imply `2 ≤ d` (`two_le_not_implied`).

  The two cells are independent. `HasTwoSharpTests` is stated for any body; the classification is
  proved for `eball d` only. Nothing here sources the predicate, `2 ≤ d` or any hypothesis of the
  selector from any construction.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.K1Bridge

namespace OIBridge
namespace SharpTests

open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface
open EffectSpace K1Bridge

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ}

/-- Two sharp binary tests of `Ω`, separated on `Ω` from each other and from each other's
complement. -/
def HasTwoSharpTests (Ω : Set V) : Prop :=
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

theorem not_hasTwoSharpTests_zero : ¬ HasTwoSharpTests (eball 0) := by
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

theorem not_hasTwoSharpTests_one : ¬ HasTwoSharpTests (eball 1) := by
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

/-- For `2 ≤ d` the sharp tests along the first two axes witness `HasTwoSharpTests`. -/
theorem hasTwoSharpTests_of_two_le (hd : 2 ≤ d) : HasTwoSharpTests (eball d) := by
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

/-- **The equivalence.** On `eball d`, two sharp binary tests distinct modulo complementation exist
exactly when `2 ≤ d`: the forward direction from the cases `d = 0` and `d = 1`, the converse from the
axis witness. -/
theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) ↔ 2 ≤ d := by
  constructor
  · intro h
    by_contra hlt
    have : d = 0 ∨ d = 1 := by omega
    rcases this with rfl | rfl
    · exact not_hasTwoSharpTests_zero h
    · exact not_hasTwoSharpTests_one h
  · exact hasTwoSharpTests_of_two_le

/-! ### §D — the selector's other hypotheses at `d = 1` -/

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

/-- The selector's hypotheses other than `2 ≤ d` do not imply `2 ≤ d`. -/
theorem two_le_not_implied :
    ¬ (∀ (d : ℕ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))
        (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
        (T : W d ≃ₗ[ℝ] W d),
        EffectsOn (eball d) avail → PreservesBody (eball d) G → SharpSeed (eball d) r →
          BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail → IsNot (eball d) z N →
          NativeGateOf (eball d) avail z N T → 2 ≤ d) := by
  intro h
  obtain ⟨hE, hG, hP1, hK, hV4, hN, hT, h2⟩ := two_le_load_bearing_relative
  exact h2 (h 1 _ _ _ _ _ _ hE hG hP1 hK hV4 hN hT)

/-! ### The verdicts -/

theorem k1sharp_classified :
    (∀ (d : ℕ) (b x : Fin d → ℝ), sharpEff (-b) x = 1 - sharpEff b x) ∧
      (∀ (d : ℕ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ),
        SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u) ∧
      (∀ e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ, ¬ SharpSeed (eball 0) e) ∧
      (∀ e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ, SharpSeed (eball 1) e → SharpSeed (eball 1) f →
        (∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)) ∧
      (∀ d : ℕ, 2 ≤ d → HasTwoSharpTests (eball d)) ∧
      (∀ d : ℕ, HasTwoSharpTests (eball d) ↔ 2 ≤ d) :=
  ⟨fun _ b x => sharpEff_neg_apply b x, fun _ e => sharpSeed_iff e, not_sharpSeed_zero,
    fun _ _ he hf => eq_or_compl_one he hf, fun _ hd => hasTwoSharpTests_of_two_le hd,
    fun _ => hasTwoSharpTests_iff⟩

theorem k1sharp_two_le_not_implied :
    (EffectsOn (eball 1) (fullEffects (eball 1)) ∧ PreservesBody (eball 1) (fullAut 1) ∧
      SharpSeed (eball 1) (sharpEff z1) ∧ BoundaryTransitive (eball 1) (fullAut 1) ∧
      SeedOrbitAvailable (fullAut 1) (sharpEff z1) (fullEffects (eball 1)) ∧
      IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧
      ¬ (2 ≤ 1)) ∧
    ¬ (∀ (d : ℕ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))
        (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
        (T : W d ≃ₗ[ℝ] W d),
        EffectsOn (eball d) avail → PreservesBody (eball d) G → SharpSeed (eball d) r →
          BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail → IsNot (eball d) z N →
          NativeGateOf (eball d) avail z N T → 2 ≤ d) :=
  ⟨two_le_load_bearing_relative, two_le_not_implied⟩

end SharpTests
end OIBridge

#print axioms OIBridge.SharpTests.sharpEff_neg_apply
#print axioms OIBridge.SharpTests.sharpSeed_iff
#print axioms OIBridge.SharpTests.not_sharpSeed_zero
#print axioms OIBridge.SharpTests.not_hasTwoSharpTests_zero
#print axioms OIBridge.SharpTests.eq_or_compl_one
#print axioms OIBridge.SharpTests.not_hasTwoSharpTests_one
#print axioms OIBridge.SharpTests.hasTwoSharpTests_of_two_le
#print axioms OIBridge.SharpTests.hasTwoSharpTests_iff
#print axioms OIBridge.SharpTests.nativeGateOf_cnot1
#print axioms OIBridge.SharpTests.two_le_load_bearing_relative
#print axioms OIBridge.SharpTests.two_le_not_implied
#print axioms OIBridge.SharpTests.k1sharp_classified
#print axioms OIBridge.SharpTests.k1sharp_two_le_not_implied
