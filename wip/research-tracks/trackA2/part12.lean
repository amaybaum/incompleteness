/-! ### §12 — product-vector tests give the effect form of the product bound -/

/-- The Bloch vector of `(a, p + i q)` for real `a`, `p`, `q`. -/
theorem blochH_real (a p q : ℝ) :
    blochH ![(a : ℂ), (p : ℂ) + (q : ℂ) * Complex.I] =
      ![a ^ 2 + p ^ 2 + q ^ 2, 2 * a * p, 2 * a * q, a ^ 2 - p ^ 2 - q ^ 2] := by
  funext μ
  fin_cases μ <;>
    simp [blochH, Complex.normSq_apply, Complex.mul_re, Complex.mul_im, Complex.star_def] <;>
    ring

/-- The Bloch vector of `|1⟩`. -/
theorem blochH_down : blochH ![(0 : ℂ), 1] = ![1, 0, 0, -1] := by
  funext μ
  fin_cases μ <;> simp [blochH, Complex.normSq_apply]

/-- **Forward-cone vectors are nonnegative combinations of two Bloch vectors.** -/
theorem lor_blochH_decomp {v : HVec 3} (hv : Lor v) : ∃ α β : ℝ, 0 ≤ α ∧ 0 ≤ β ∧
    ∃ u u' : Fin 2 → ℂ, v = α • blochH u + β • blochH u' := by
  have h0 : 0 ≤ v 0 := hv.1
  have h2' : v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 ≤ v 0 ^ 2 := by
    have h := hv.2
    rw [Fin.sum_univ_three] at h
    first
    | exact h
    | simpa using h
  by_cases hz : v 0 + v 3 = 0
  · have hv3 : v 3 = -v 0 := by linarith
    have h33 : v 3 ^ 2 = v 0 ^ 2 := by rw [hv3]; ring
    have h12 : v 1 ^ 2 + v 2 ^ 2 ≤ 0 := by linarith
    have hv1 : v 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp
      (le_antisymm (by linarith [sq_nonneg (v 2)]) (sq_nonneg _))
    have hv2 : v 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp
      (le_antisymm (by linarith [sq_nonneg (v 1)]) (sq_nonneg _))
    refine ⟨0, v 0, le_rfl, h0, ![(0 : ℂ), 1], ![(0 : ℂ), 1], ?_⟩
    rw [blochH_down, zero_smul, zero_add]
    funext μ
    fin_cases μ
    · show v 0 = v 0 * 1
      rw [mul_one]
    · show v 1 = v 0 * 0
      rw [mul_zero, hv1]
    · show v 2 = v 0 * 0
      rw [mul_zero, hv2]
    · show v 3 = v 0 * -1
      rw [hv3, mul_neg_one]
  · have hne : v 0 + v 3 ≠ 0 := hz
    have h33 : v 3 ^ 2 ≤ v 0 ^ 2 := by linarith [sq_nonneg (v 1), sq_nonneg (v 2)]
    have hpos : 0 < v 0 + v 3 :=
      lt_of_le_of_ne (by linarith [(abs_le_of_sq_le_sq' h33 h0).1]) (Ne.symm hne)
    have hc : (0 : ℝ) < 2 * (v 0 + v 3) := by linarith
    have hc0 : 2 * (v 0 + v 3) ≠ 0 := ne_of_gt hc
    have hβ : 0 ≤ v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2 := by linarith
    have key : (2 * (v 0 + v 3)) • v =
        (4 : ℝ) • blochH ![(((v 0 + v 3) / 2 : ℝ) : ℂ),
          ((v 1 / 2 : ℝ) : ℂ) + ((v 2 / 2 : ℝ) : ℂ) * Complex.I] +
          (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) • blochH ![(0 : ℂ), 1] := by
      rw [blochH_real, blochH_down]
      funext μ
      fin_cases μ
      · show 2 * (v 0 + v 3) * v 0 =
          4 * (((v 0 + v 3) / 2) ^ 2 + (v 1 / 2) ^ 2 + (v 2 / 2) ^ 2) +
            (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * 1
        ring
      · show 2 * (v 0 + v 3) * v 1 = 4 * (2 * ((v 0 + v 3) / 2) * (v 1 / 2)) +
          (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * 0
        ring
      · show 2 * (v 0 + v 3) * v 2 = 4 * (2 * ((v 0 + v 3) / 2) * (v 2 / 2)) +
          (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * 0
        ring
      · show 2 * (v 0 + v 3) * v 3 =
          4 * (((v 0 + v 3) / 2) ^ 2 - (v 1 / 2) ^ 2 - (v 2 / 2) ^ 2) +
            (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * -1
        ring
    refine ⟨(2 * (v 0 + v 3))⁻¹ * 4,
      (2 * (v 0 + v 3))⁻¹ * (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2),
      mul_nonneg (inv_nonneg.mpr hc.le) (by norm_num), mul_nonneg (inv_nonneg.mpr hc.le) hβ,
      ![(((v 0 + v 3) / 2 : ℝ) : ℂ), ((v 1 / 2 : ℝ) : ℂ) + ((v 2 / 2 : ℝ) : ℂ) * Complex.I],
      ![(0 : ℂ), 1], ?_⟩
    calc v = (2 * (v 0 + v 3))⁻¹ • (2 * (v 0 + v 3)) • v := (inv_smul_smul₀ hc0 v).symm
      _ = _ := by rw [key, smul_add, smul_smul, smul_smul]

/-- The slice of a table along a homogeneous vector on the last token. -/
def tokSlice {n : ℕ} (u : HVec 3) (w : Labels (n + 1) → ℝ) : Labels n → ℝ :=
  fun ν => ∑ m : Fin 4, u m * w (ν, m)

theorem sum_prodTab_succ (n : ℕ) (v : ℕ → HVec 3) (w : Labels (n + 1) → ℝ) :
    ∑ μ, prodTab (n + 1) v μ * w μ = ∑ ν, prodTab n v ν * tokSlice (v n) w ν := by
  simp only [Fintype.sum_prod_type, prodTab_succ, tokSlice, Finset.mul_sum]
  refine Finset.sum_congr rfl fun ν _ => Finset.sum_congr rfl fun m _ => ?_
  ring

theorem tokSlice_add {n : ℕ} (u u' : HVec 3) (w : Labels (n + 1) → ℝ) :
    tokSlice (u + u') w = tokSlice u w + tokSlice u' w := by
  funext ν
  simp only [tokSlice, Pi.add_apply, add_mul, Finset.sum_add_distrib]

theorem tokSlice_smul {n : ℕ} (c : ℝ) (u : HVec 3) (w : Labels (n + 1) → ℝ) :
    tokSlice (c • u) w = c • tokSlice u w := by
  funext ν
  simp only [tokSlice, Pi.smul_apply, smul_eq_mul, Finset.mul_sum, mul_assoc]

/-- Nonnegativity on every product of Bloch vectors gives nonnegativity on every product of
forward-cone vectors. -/
theorem lorTests_of_blochTests : ∀ (n : ℕ) (w : Labels n → ℝ),
    (∀ a : ℕ → Fin 2 → ℂ, 0 ≤ ∑ μ, prodTab n (fun i => blochH (a i)) μ * w μ) →
    ∀ v : ℕ → HVec 3, (∀ i, i < n → Lor (v i)) → 0 ≤ ∑ μ, prodTab n v μ * w μ
  | 0, _, hw, _, _ => hw (fun _ => ket0)
  | n + 1, w, hw, v, hv => by
    obtain ⟨α, β, hα, hβ, u, u', hvn⟩ := lor_blochH_decomp (hv n (Nat.lt_succ_self n))
    have hslice : ∀ u0 : Fin 2 → ℂ, 0 ≤ ∑ ν, prodTab n v ν * tokSlice (blochH u0) w ν := by
      intro u0
      refine lorTests_of_blochTests n (tokSlice (blochH u0) w) (fun a => ?_) v
        (fun i hi => hv i (Nat.lt_succ_of_lt hi))
      have h := hw (fun i => if i = n then u0 else a i)
      rw [sum_prodTab_succ] at h
      have hp : prodTab n (fun i => blochH (if i = n then u0 else a i)) =
          prodTab n (fun i => blochH (a i)) :=
        prodTab_congr n fun i hi => congrArg blochH (if_neg (Nat.ne_of_lt hi))
      rw [hp, if_pos (rfl : n = n)] at h
      exact h
    have key : ∀ (x y : HVec 3) (c e : ℝ),
        ∑ ν, prodTab n v ν * tokSlice (c • x + e • y) w ν =
          c * ∑ ν, prodTab n v ν * tokSlice x w ν + e * ∑ ν, prodTab n v ν * tokSlice y w ν := by
      intro x y c e
      rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun ν _ => ?_
      simp only [tokSlice_add, tokSlice_smul, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
      ring
    rw [sum_prodTab_succ, hvn, key]
    exact add_nonneg (mul_nonneg hα (hslice u)) (mul_nonneg hβ (hslice u'))

/-- **Product-vector tests give the effect form**, on tables. -/
theorem maxConeTab_of_blochTests {k : ℕ} {w : Labels k → ℝ}
    (hw : ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ ∑ μ, prodTab k (fun i => blochH (a i)) μ * w μ) :
    w ∈ maxConeTab k := by
  intro e he
  exact lorTests_of_blochTests k w hw (fun i => ehom (e i)) fun i hi => lor_ehom (he i hi)

/-- **Product-vector tests give the effect form**, on Hermitian matrices: the converse of
`prodVec_nonneg_of_maxConeTab`. -/
theorem maxConeTab_of_prodVec_nonneg {k : ℕ} {A : Mat k} (hA : A.IsHermitian)
    (h : ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a)) :
    coordinates k A ∈ maxConeTab k := by
  refine maxConeTab_of_blochTests fun a => ?_
  have ha := h a
  rw [← dictionary_coordinates_real k A hA, quad_dictionary_prodVec,
    show ((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ : ℝ) : ℂ) /
        (2 : ℂ) ^ k = (((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ) /
          2 ^ k : ℝ) : ℂ) by push_cast; ring,
    Complex.zero_le_real] at ha
  by_contra hneg
  exact absurd ha (not_le.mpr (div_neg_of_neg_of_pos (not_le.mp hneg)
    (pow_pos (by norm_num) k)))

/-- The effect form gives the product-vector tests, on Hermitian matrices. -/
theorem prodVec_nonneg_of_maxConeTab {k : ℕ} {A : Mat k} (hA : A.IsHermitian)
    (h : coordinates k A ∈ maxConeTab k) (a : ℕ → Fin 2 → ℂ) :
    0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a) := by
  rw [← dictionary_coordinates_real k A hA, quad_dictionary_prodVec]
  have hS := lorPair_nonneg_of_maxConeTab (v := fun i => blochH (a i)) h
    fun i _ => lor_blochH (a i)
  rw [show ((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ : ℝ) : ℂ) /
      (2 : ℂ) ^ k = (((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ) /
        2 ^ k : ℝ) : ℂ) by push_cast; ring,
    Complex.zero_le_real]
  exact div_nonneg hS (pow_nonneg (by norm_num) k)

/-- **The "equivalently" of the product bound.** For a Hermitian matrix, nonnegativity on every
product of ball effects is equivalent to nonnegative expectation on every product vector.
Witnesses: `prodVec_nonneg_of_maxConeTab` (→) and `maxConeTab_of_prodVec_nonneg` (←). -/
theorem maxConeTab_iff_prodVec_nonneg {k : ℕ} {A : Mat k} (hA : A.IsHermitian) :
    coordinates k A ∈ maxConeTab k ↔
      ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a) :=
  ⟨fun h => prodVec_nonneg_of_maxConeTab hA h, maxConeTab_of_prodVec_nonneg hA⟩

#print axioms blochH_real
#print axioms lor_blochH_decomp
#print axioms lorTests_of_blochTests
#print axioms maxConeTab_of_blochTests
#print axioms maxConeTab_of_prodVec_nonneg
#print axioms prodVec_nonneg_of_maxConeTab
#print axioms maxConeTab_iff_prodVec_nonneg
