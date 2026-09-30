/-
  OIBridge/NativeGateBall.lean — round NB-1: the dimension-free core of the finite native-gate
  ball no-go.

  The theorem this module serves. For two locally tomographic d-ball systems with their full
  self-dual effect cones and one common NOT involution `N`, an invertible linear map `G` with the
  classical CNOT action on the corners, the two native relations `(I⊗N) G (I⊗N) = G` and
  `(N⊗I) G (N⊗I) = (I⊗N) G`, and `G`, `G⁻¹` both sending product states into the maximal tensor
  cone, force `d ∈ {1, 3}`. That theorem is not a kernel theorem: its proof is layered, and this
  module certifies one layer of it.

  Proved here, the steps whose reasoning does not depend on `d`:
    §A  the averaging bound (S3) and its consequence for `p ≥ 2`;
    §B  the Lorentz test: a vector every unit effect keeps nonnegative lies in the cone;
    §C  the E₊ block vanishes for `p ≥ 2` (S4, entrywise), hence `p ≤ 1` given a nonzero block;
    §D  parity (S5): an injective map anticommuting with a linear map equates its ±1 eigenspaces;
    §E  a contraction with a contracting left inverse is an isometry (the last step of S1);
    §F  the count: `p ≤ 1`, `p = q`, `p + q + 1 = d` give `d = 1 ∨ d = 3`;
    `nb1_kernel_core`, the conjunction of `p_le_one`, `parity` and `dim_of_bounds`.

  Not proved here. The controlled form (S1), the block structure (S2) and the value identity that
  turns positivity of `G` into the hypothesis of `blocks_vanish` (S4) are proved by hand for every
  `d`; the round's probe checks the S1 and S2 solution spaces in exact arithmetic for `d = 2,…,7`
  and the value identity for `d = 5, 7`. Nothing here concerns whether OI supplies the common `N`
  on both factors (identical-copy covariance).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace OIBridge
namespace NativeGateBall

open Finset

/-! ### §A — the averaging bound (S3) -/

/-- The column sum of squares of `I + K`, column `i`. -/
theorem col_sq (p : ℕ) (K : Matrix (Fin p) (Fin p) ℝ) (i : Fin p) :
    (∑ j, ((if j = i then (1:ℝ) else 0) + K j i) ^ 2) = 1 + 2 * K i i + ∑ j, K j i ^ 2 := by
  have h : ∀ j, ((if j = i then (1:ℝ) else 0) + K j i) ^ 2
      = (if j = i then (1 + 2 * K i i) else 0) + K j i ^ 2 := by
    intro j
    by_cases hj : j = i
    · subst hj; simp only [if_true]; ring
    · simp only [hj, if_false]; ring
  rw [Finset.sum_congr rfl (fun j _ => h j), Finset.sum_add_distrib, Finset.sum_ite_eq']
  simp

/-- **S3.** If `I + K` (with `K` antisymmetric) and the vector `g` pass the Lorentz test at the `2p`
points `t = ±eᵢ`, squared, then `(p − 1)|g|² + ‖K‖²_F ≤ 0`. -/
theorem averaging_bound (p : ℕ) (g : Fin p → ℝ) (K : Matrix (Fin p) (Fin p) ℝ)
    (hK : ∀ i j, K i j = - K j i)
    (h : ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      (∑ j, (g j + s * ((if j = i then (1:ℝ) else 0) + K j i)) ^ 2) ≤ (1 + s * g i) ^ 2) :
    ((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0 := by
  have hdiag : ∀ i, K i i = 0 := by
    intro i; have := hK i i; linarith
  have per : ∀ i : Fin p, (∑ j, g j ^ 2) + (∑ j, K j i ^ 2) ≤ g i ^ 2 := by
    intro i
    have h1 := h i 1 (Or.inl rfl)
    have h2 := h i (-1) (Or.inr rfl)
    have e : (∑ j, (g j + 1 * ((if j = i then (1:ℝ) else 0) + K j i)) ^ 2)
          + (∑ j, (g j + (-1) * ((if j = i then (1:ℝ) else 0) + K j i)) ^ 2)
        = 2 * (∑ j, g j ^ 2) + 2 * (∑ j, ((if j = i then (1:ℝ) else 0) + K j i) ^ 2) := by
      rw [← Finset.sum_add_distrib, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl (fun j _ => by ring)
    rw [col_sq p K i, hdiag i] at e
    nlinarith [e, h1, h2]
  have hs := Finset.sum_le_sum (fun i (_ : i ∈ (Finset.univ : Finset (Fin p))) => per i)
  rw [Finset.sum_add_distrib] at hs
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul] at hs
  nlinarith [hs]

/-- For `p ≥ 2` the bound forces `g = 0` and `K = 0`. -/
theorem vanish_of_bound (p : ℕ) (hp : 2 ≤ p) (g : Fin p → ℝ) (K : Matrix (Fin p) (Fin p) ℝ)
    (h : ((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0) :
    (∀ j, g j = 0) ∧ (∀ i j, K j i = 0) := by
  have hp' : (1:ℝ) ≤ (p:ℝ) - 1 := by
    have : (2:ℝ) ≤ p := by exact_mod_cast hp
    linarith
  have hG : 0 ≤ ∑ j, g j ^ 2 := Finset.sum_nonneg (fun j _ => sq_nonneg _)
  have hKK : 0 ≤ ∑ i, ∑ j, K j i ^ 2 :=
    Finset.sum_nonneg (fun i _ => Finset.sum_nonneg (fun j _ => sq_nonneg _))
  have hG0 : ∑ j, g j ^ 2 = 0 := by nlinarith
  have hK0 : ∑ i, ∑ j, K j i ^ 2 = 0 := by nlinarith
  constructor
  · intro j
    have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (g j))).1 hG0 j
      (Finset.mem_univ _)
    exact (pow_eq_zero_iff two_ne_zero).mp this
  · intro i j
    have hi := (Finset.sum_eq_zero_iff_of_nonneg
      (fun i _ => Finset.sum_nonneg (fun j _ => sq_nonneg (K j i)))).1 hK0 i (Finset.mem_univ _)
    have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (K j i))).1 hi j
      (Finset.mem_univ _)
    exact (pow_eq_zero_iff two_ne_zero).mp this

/-! ### §B — the Lorentz test -/

/-- If every unit effect direction `b` keeps `x₀ + b·v ≥ 0`, then `x₀ ≥ 0` and `|v|² ≤ x₀²`. -/
theorem lorentz_of_effects (p : ℕ) (hp : 1 ≤ p) (x0 : ℝ) (v : Fin p → ℝ)
    (h : ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 → 0 ≤ x0 + ∑ j, b j * v j) :
    0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2 := by
  have hN0 : 0 ≤ ∑ j, v j ^ 2 := Finset.sum_nonneg (fun j _ => sq_nonneg _)
  rcases eq_or_lt_of_le hN0 with h0 | hpos
  · have hv : ∀ j, v j = 0 := by
      intro j
      have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (v j))).1 h0.symm j
        (Finset.mem_univ _)
      exact (pow_eq_zero_iff two_ne_zero).mp this
    let j0 : Fin p := ⟨0, hp⟩
    let e0 : Fin p → ℝ := fun j => if j = j0 then 1 else 0
    have he : (∑ j, e0 j ^ 2) = 1 := by
      have : ∀ j, e0 j ^ 2 = if j = j0 then 1 else 0 := by
        intro j; by_cases hj : j = j0 <;> simp [e0, hj]
      rw [Finset.sum_congr rfl (fun j _ => this j), Finset.sum_ite_eq']
      simp
    have := h e0 he
    simp only [hv, mul_zero, Finset.sum_const_zero, add_zero] at this
    exact ⟨this, by rw [← h0]; positivity⟩
  · set r := Real.sqrt (∑ j, v j ^ 2) with hrdef
    have hr : 0 < r := Real.sqrt_pos.2 hpos
    have hr2 : r ^ 2 = ∑ j, v j ^ 2 := Real.sq_sqrt hN0
    have hrne : r ≠ 0 := ne_of_gt hr
    let b : Fin p → ℝ := fun j => - v j / r
    have hb : (∑ j, b j ^ 2) = 1 := by
      have : ∀ j, b j ^ 2 = v j ^ 2 * (r ^ 2)⁻¹ := fun j => by simp only [b]; ring
      rw [Finset.sum_congr rfl (fun j _ => this j), ← Finset.sum_mul, ← hr2]
      exact mul_inv_cancel₀ (pow_ne_zero 2 hrne)
    have hbv : (∑ j, b j * v j) = - r := by
      have : ∀ j, b j * v j = - (v j ^ 2 * r⁻¹) := fun j => by simp only [b]; ring
      rw [Finset.sum_congr rfl (fun j _ => this j), Finset.sum_neg_distrib, ← Finset.sum_mul,
        ← hr2, sq, mul_assoc, mul_inv_cancel₀ hrne, mul_one]
    have := h b hb
    rw [hbv] at this
    refine ⟨by linarith, ?_⟩
    rw [← hr2]
    nlinarith

/-! ### §C — the E₊ block vanishes for `p ≥ 2` (S4) -/

/-- **S4, entrywise.** With `Γ_{kl} = [[0, gᵀ],[g, K]]`, `g_r = (A r) k l`, `K_{ji} = (B j i) k l`
antisymmetric, and `I + Γ_{kl}` passing the Lorentz test at `t = ±eᵢ` against every unit effect,
`p ≥ 2` forces every `A r` and every `B r s` to vanish. -/
theorem blocks_vanish (p m : ℕ) (hp : 2 ≤ p)
    (A : Fin p → Matrix (Fin m) (Fin m) ℝ) (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ)
    (hB : ∀ r s, B r s = - B s r)
    (hpos : ∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →
        0 ≤ (1 + s * A i k l)
          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) :
    (∀ r, A r = 0) ∧ (∀ r s, B r s = 0) := by
  have key : ∀ k l, (∀ j, A j k l = 0) ∧ (∀ i j, B j i k l = 0) := by
    intro k l
    have hb := vanish_of_bound p hp (fun j => A j k l) (Matrix.of fun j i => B j i k l)
      (averaging_bound p (fun j => A j k l) (Matrix.of fun j i => B j i k l)
        (by intro i j; simp only [Matrix.of_apply]; rw [hB i j]; simp)
        (by
          intro i s hs
          have hl := lorentz_of_effects p (by omega) (1 + s * A i k l)
            (fun j => A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))
            (hpos k l i s hs)
          simpa only [Matrix.of_apply] using hl.2))
    refine ⟨hb.1, fun i j => ?_⟩
    simpa only [Matrix.of_apply] using hb.2 i j
  refine ⟨fun r => ?_, fun r s => ?_⟩
  · ext k l; simpa using (key k l).1 r
  · ext k l; simpa using (key k l).2 s r

/-- **S4, conclusion.** If some entry of the E₊ block is nonzero (as invertibility requires), then
`p ≤ 1`. -/
theorem p_le_one (p m : ℕ)
    (A : Fin p → Matrix (Fin m) (Fin m) ℝ) (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ)
    (hB : ∀ r s, B r s = - B s r)
    (hpos : ∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →
        0 ≤ (1 + s * A i k l)
          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l)))
    (hne : ∃ r k l, A r k l ≠ 0) : p ≤ 1 := by
  by_contra hlt
  have hp : 2 ≤ p := by omega
  obtain ⟨r, k, l, hrkl⟩ := hne
  have := (blocks_vanish p m hp A B hB hpos).1 r
  exact hrkl (by rw [this]; rfl)

/-! ### §D — parity (S5) -/

/-- **S5.** An injective linear map anticommuting with `P` maps the `+1` eigenspace of `P` injectively
into the `−1` eigenspace and back, so the two have equal dimension. -/
theorem parity {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]
    (P L : V →ₗ[ℝ] V) (hL : Function.Injective L)
    (hanti : ∀ v, L (P v) = - P (L v)) :
    Module.finrank ℝ (LinearMap.ker (P - LinearMap.id))
      = Module.finrank ℝ (LinearMap.ker (P + LinearMap.id)) := by
  have h1 : ∀ v ∈ LinearMap.ker (P - LinearMap.id), L v ∈ LinearMap.ker (P + LinearMap.id) := by
    intro v hv
    simp only [LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.id_apply, sub_eq_zero] at hv
    simp only [LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply]
    have h0 := hanti v
    rw [hv] at h0
    have hPL : P (L v) = - L v := by
      have h' := congrArg Neg.neg h0
      simpa using h'.symm
    rw [hPL]
    simp
  have h2 : ∀ v ∈ LinearMap.ker (P + LinearMap.id), L v ∈ LinearMap.ker (P - LinearMap.id) := by
    intro v hv
    simp only [LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply] at hv
    have hv' : P v = - v := eq_neg_of_add_eq_zero_left hv
    simp only [LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.id_apply, sub_eq_zero]
    have := hanti v
    rw [hv', map_neg] at this
    have : P (L v) = L v := by
      have h3 : - L v = - P (L v) := this
      exact (neg_inj.mp h3).symm
    exact this
  have inj1 : Function.Injective (L.restrict h1) := by
    intro x y hxy
    apply Subtype.ext
    apply hL
    have := congrArg Subtype.val hxy
    simpa [LinearMap.restrict_apply] using this
  have inj2 : Function.Injective (L.restrict h2) := by
    intro x y hxy
    apply Subtype.ext
    apply hL
    have := congrArg Subtype.val hxy
    simpa [LinearMap.restrict_apply] using this
  exact le_antisymm (LinearMap.finrank_le_finrank_of_injective inj1)
    (LinearMap.finrank_le_finrank_of_injective inj2)

/-! ### §E — contractions with a contracting left inverse are isometries (S1) -/

theorem isometry_of_contractions {E : Type*} [SeminormedAddCommGroup E] (M M' : E → E)
    (hM : ∀ v, ‖M v‖ ≤ ‖v‖) (hM' : ∀ v, ‖M' v‖ ≤ ‖v‖) (hinv : ∀ v, M' (M v) = v) :
    ∀ v, ‖M v‖ = ‖v‖ := by
  intro v
  apply le_antisymm (hM v)
  calc ‖v‖ = ‖M' (M v)‖ := by rw [hinv v]
    _ ≤ ‖M v‖ := hM' (M v)

/-! ### §F — the count -/

theorem dim_of_bounds (p q d : ℕ) (hp : p ≤ 1) (hpq : p = q) (hd : p + q + 1 = d) :
    d = 1 ∨ d = 3 := by
  omega

end NativeGateBall
end OIBridge

#print axioms OIBridge.NativeGateBall.col_sq
#print axioms OIBridge.NativeGateBall.averaging_bound
#print axioms OIBridge.NativeGateBall.vanish_of_bound
#print axioms OIBridge.NativeGateBall.lorentz_of_effects
#print axioms OIBridge.NativeGateBall.blocks_vanish
#print axioms OIBridge.NativeGateBall.p_le_one
#print axioms OIBridge.NativeGateBall.parity
#print axioms OIBridge.NativeGateBall.isometry_of_contractions
#print axioms OIBridge.NativeGateBall.dim_of_bounds
