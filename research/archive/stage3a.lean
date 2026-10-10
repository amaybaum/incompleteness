/-! ### §K — extreme points of the ball, and the `d = 1` exclusion -/

theorem sumsq_sub (u v : Fin d → ℝ) :
    ∑ j, (u - v) j ^ 2 = ∑ j, u j ^ 2 - 2 * ∑ j, u j * v j + ∑ j, v j ^ 2 := by
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun j _ => by simp only [Pi.sub_apply]; ring

theorem sumsq_smul_add_smul (a b : ℝ) (u v : Fin d → ℝ) :
    ∑ j, (a • u + b • v) j ^ 2
      = a ^ 2 * ∑ j, u j ^ 2 + 2 * a * b * ∑ j, u j * v j + b ^ 2 * ∑ j, v j ^ 2 := by
  rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib,
    ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun j _ => by
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]; ring

/-- Every unit vector is an extreme point of the ball. -/
theorem unit_mem_extremePoints_eball {x : Fin d → ℝ} (hx : ∑ j, x j ^ 2 = 1) :
    x ∈ (eball d).extremePoints ℝ := by
  refine ⟨hx.le, ?_⟩
  intro x₁ hx₁ x₂ hx₂ hseg
  obtain ⟨a, b, ha, hb, hab, hsum⟩ := hseg
  rw [mem_eball] at hx₁ hx₂
  have h1 : ∑ j, (a • x₁ + b • x₂) j ^ 2 = 1 := by rw [hsum]; exact hx
  rw [sumsq_smul_add_smul] at h1
  have hsq : (a + b) ^ 2 = 1 := by rw [hab]; norm_num
  have hC : 1 ≤ ∑ j, x₁ j * x₂ j := by
    have hab2 : a * b * 1 ≤ a * b * ∑ j, x₁ j * x₂ j := by
      nlinarith [mul_nonneg (sq_nonneg a) (sub_nonneg.mpr hx₁),
        mul_nonneg (sq_nonneg b) (sub_nonneg.mpr hx₂)]
    exact le_of_mul_le_mul_left hab2 (mul_pos ha hb)
  have hD : ∑ j, (x₁ - x₂) j ^ 2 ≤ 0 := by rw [sumsq_sub]; linarith
  have hD0 : ∑ j, (x₁ - x₂) j ^ 2 = 0 :=
    le_antisymm hD (Finset.sum_nonneg fun j _ => sq_nonneg _)
  have heq : x₁ = x₂ := by
    funext j
    have h := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg ((x₁ - x₂) j))).1 hD0 j
      (Finset.mem_univ _)
    have h' := (pow_eq_zero_iff two_ne_zero).mp h
    rw [Pi.sub_apply, sub_eq_zero] at h'
    exact h'
  rw [← hsum, ← heq, ← add_smul, hab, one_smul]

/-- The corners lie in the ball. -/
theorem corner_mem_eball {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot Ω z N) (a : Fin 2) : corner z a ∈ eball d := by
  fin_cases a
  · exact hN.unit.le
  · show ∑ j, (-z) j ^ 2 ≤ 1
    simp only [Pi.neg_apply, neg_sq]
    exact hN.unit.le

/-- An extreme point of the segment `eball 1` is an endpoint. -/
theorem sq_eq_one_of_extreme_eball_one {x : Fin 1 → ℝ} (hx : x ∈ (eball 1).extremePoints ℝ) :
    x 0 ^ 2 = 1 := by
  have hle : x 0 ^ 2 ≤ 1 := by
    have := hx.1
    rwa [mem_eball, Fin.sum_univ_one] at this
  by_contra hne
  have hlt : x 0 ^ 2 < 1 := lt_of_le_of_ne hle hne
  set ε : ℝ := (1 - x 0 ^ 2) / 2 with hε
  have hεpos : 0 < ε := by rw [hε]; linarith
  have hb : -1 ≤ x 0 ∧ x 0 ≤ 1 := by constructor <;> nlinarith
  let e : Fin 1 → ℝ := fun _ => 1
  have hu : x + ε • e ∈ eball 1 := by
    rw [mem_eball, Fin.sum_univ_one]
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, e, mul_one]
    nlinarith
  have hw : x - ε • e ∈ eball 1 := by
    rw [mem_eball, Fin.sum_univ_one]
    simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul, e, mul_one]
    nlinarith
  have hseg : x ∈ openSegment ℝ (x + ε • e) (x - ε • e) :=
    ⟨1 / 2, 1 / 2, by norm_num, by norm_num, by norm_num, by module⟩
  have h := hx.2 hu hw hseg
  have h0 := congrFun h 0
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, e, mul_one, add_eq_left] at h0
  linarith

/-- In dimension one every extreme point of the ball is a corner. -/
theorem eq_corner_of_extreme_eball_one {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ)}
    (hN : IsNot (eball 1) z N) {x : Fin 1 → ℝ} (hx : x ∈ (eball 1).extremePoints ℝ) :
    x = corner z 0 ∨ x = corner z 1 := by
  have hx1 := sq_eq_one_of_extreme_eball_one hx
  have hz1 : z 0 ^ 2 = 1 := by
    have := hN.unit
    rwa [Fin.sum_univ_one] at this
  have hprod : (x 0 - z 0) * (x 0 + z 0) = 0 := by nlinarith
  rcases mul_eq_zero.mp hprod with h | h
  · left
    funext i
    rw [Fin.fin_one_eq_zero i]
    show x 0 = z 0
    linarith
  · right
    funext i
    rw [Fin.fin_one_eq_zero i]
    show x 0 = (-z) 0
    rw [Pi.neg_apply]
    linarith

/-- **The `d = 1` exclusion.** A native gate on the segment maps every pure product input to a
product, so it is not entangling. -/
theorem ne_one_of_entangling {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hE : Entangling (eball d) G) : d ≠ 1 := by
  intro hd
  subst hd
  obtain ⟨x, hx, y, hy, _, hnp⟩ := hE
  apply hnp
  rcases eq_corner_of_extreme_eball_one hN hx with rfl | rfl <;>
    rcases eq_corner_of_extreme_eball_one hN hy with rfl | rfl
  · exact ⟨corner z 0, corner_mem_eball hN 0, corner z (0 + 0), corner_mem_eball hN _, hG.frame 0 0⟩
  · exact ⟨corner z 0, corner_mem_eball hN 0, corner z (0 + 1), corner_mem_eball hN _, hG.frame 0 1⟩
  · exact ⟨corner z 1, corner_mem_eball hN 1, corner z (1 + 0), corner_mem_eball hN _, hG.frame 1 0⟩
  · exact ⟨corner z 1, corner_mem_eball hN 1, corner z (1 + 1), corner_mem_eball hN _, hG.frame 1 1⟩
