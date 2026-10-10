-- Moved out of the TRB-1 design module (claude/trb1-dev 6932516f) by the owner's scope cut of 2026-10-04:
-- order predicates and order controls belong to round ORD-1. Proofs compiled with standard axioms in run 37221769686.

/-- Infinite order on the body: every positive power moves some state. -/
def InfiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop :=
  ∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x

/-- **ORD∞.** `G` has a member of infinite order on `Ω`. Stated apart from `TransBody`. -/
def OrdInf (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∃ g ∈ G, InfiniteOrderOn Ω g

theorem rot3_mem_fullAut3 (t : ℝ) : rot3 t ∈ fullAut3 := fun x hx =>
  preservesBody_flow (rot3 t) ⟨t, rfl⟩ x hx

theorem iterate_rot3_one (m : ℕ) (v : Fin 3 → ℝ) : (⇑(rot3 1))^[m] v = rotFun (m : ℝ) v := by
  induction m with
  | zero => simp [rotFun_zero]
  | succ k ih =>
    rw [Function.iterate_succ_apply', ih, rot3_apply, rotFun_add]
    congr 1
    push_cast
    ring

/-- The rotation by one radian has infinite order on the ball: `cos m ≠ 1` for every integer
`m ≥ 1`, since `π` is irrational. -/
theorem infiniteOrderOn_rot3_one : InfiniteOrderOn ball3 (rot3 1) := by
  intro m hm
  refine ⟨![1, 0, 0], by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun h => ?_⟩
  rw [iterate_rot3_one] at h
  have h0 := congrFun h 0
  obtain ⟨a0, -, -⟩ := rotFun_apply (m : ℝ) ![1, 0, 0]
  rw [a0] at h0
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, mul_one, mul_zero, sub_zero] at h0
  obtain ⟨n, hn⟩ := (Real.cos_eq_one_iff _).mp h0
  have hmpos : (0 : ℝ) < m := by exact_mod_cast hm
  have hn0 : (n : ℝ) ≠ 0 := by
    intro hz
    rw [hz, zero_mul] at hn
    linarith
  apply irrational_pi.ne_rat ((m : ℚ) / (2 * n))
  push_cast
  field_simp
  linear_combination hn

/-- **Control (TRANS, ORD∞) = (holds, holds), the order half.** -/
theorem ordInf_fullAut3 : OrdInf ball3 fullAut3 := ⟨rot3 1, rot3_mem_fullAut3 1, infiniteOrderOn_rot3_one⟩

/-- **Control (TRANS, ORD∞) = (fails, holds): the rotation flow alone.** -/
theorem not_transBody_flow : ¬ TransBody ball3 (Set.range rot3) := fun h => not_boundaryTransitive_flow h.2

theorem ordInf_flow : OrdInf ball3 (Set.range rot3) := ⟨rot3 1, ⟨1, rfl⟩, infiniteOrderOn_rot3_one⟩

/-- Every member of the reflection family is an involution. -/
theorem refls3_involutive : ∀ g ∈ refls3, ∀ x, g (g x) = x := by
  rintro g (⟨dv, k, hk, rfl⟩ | rfl) x
  · rw [hh3_apply, hh3_apply]
    exact hhFun_hhFun dv k hk x
  · rfl

/-- **Control (TRANS as a set property, ORD∞) = (holds, fails), the order half.** -/
theorem not_ordInf_refls3 : ¬ OrdInf ball3 refls3 := by
  rintro ⟨g, hg, h⟩
  obtain ⟨x, -, hne⟩ := h 2 (by norm_num)
  apply hne
  show g (g x) = x
  exact refls3_involutive g hg x
