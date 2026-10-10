/-! ### §E — a NOT of the ball is an isometry and is self-adjoint -/

theorem sumsq_smul (c : ℝ) (x : Fin d → ℝ) : ∑ j, (c • x) j ^ 2 = c ^ 2 * ∑ j, x j ^ 2 := by
  simp only [Pi.smul_apply, smul_eq_mul, mul_pow, Finset.mul_sum]

theorem sumsq_apply_le_of_preserves {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x : Fin d → ℝ) : ∑ j, (N x) j ^ 2 ≤ ∑ j, x j ^ 2 := by
  have hs0 : 0 ≤ ∑ j, x j ^ 2 := Finset.sum_nonneg fun j _ => sq_nonneg _
  rcases eq_or_lt_of_le hs0 with h0 | hpos
  · have hx : x = 0 := by
      funext j
      have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (x j))).1 h0.symm j
        (Finset.mem_univ _)
      exact (pow_eq_zero_iff two_ne_zero).mp this
    rw [hx, map_zero]
  · have hsq : Real.sqrt (∑ j, x j ^ 2) ^ 2 = ∑ j, x j ^ 2 := Real.sq_sqrt hs0
    have hsqpos : 0 < Real.sqrt (∑ j, x j ^ 2) := Real.sqrt_pos.2 hpos
    set c : ℝ := 1 / Real.sqrt (∑ j, x j ^ 2) with hc
    have hcpos : 0 < c := by rw [hc]; exact div_pos one_pos hsqpos
    have hc2 : c ^ 2 * ∑ j, x j ^ 2 = 1 := by
      rw [hc, div_pow, one_pow, hsq]
      exact one_div_mul_cancel (ne_of_gt hpos)
    have hmem : c • x ∈ eball d := by
      rw [mem_eball, sumsq_smul, hc2]
    have h1 := hN.preserves _ hmem
    rw [mem_eball, map_smul, sumsq_smul] at h1
    by_contra hlt
    have hlt' := not_le.mp hlt
    have := mul_lt_mul_of_pos_left hlt' (pow_pos hcpos 2)
    linarith

/-- A NOT of the ball preserves the sum of squares. -/
theorem sumsq_apply_eq {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x : Fin d → ℝ) : ∑ j, (N x) j ^ 2 = ∑ j, x j ^ 2 := by
  refine le_antisymm (sumsq_apply_le_of_preserves hN x) ?_
  have := sumsq_apply_le_of_preserves hN (N x)
  rwa [hN.invol] at this

theorem sumsq_add (u v : Fin d → ℝ) :
    ∑ j, (u + v) j ^ 2 = ∑ j, u j ^ 2 + 2 * ∑ j, u j * v j + ∑ j, v j ^ 2 := by
  rw [Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun j _ => by simp only [Pi.add_apply]; ring

/-- Polarization: a NOT of the ball preserves the dot product. -/
theorem dot_apply_apply {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x y : Fin d → ℝ) :
    ∑ j, (N x) j * (N y) j = ∑ j, x j * y j := by
  have h := sumsq_apply_eq hN (x + y)
  have hx := sumsq_apply_eq hN x
  have hy := sumsq_apply_eq hN y
  rw [map_add, sumsq_add, sumsq_add] at h
  linarith

/-- A NOT of the ball is self-adjoint for the dot product. -/
theorem dot_apply {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x y : Fin d → ℝ) :
    ∑ j, (N x) j * y j = ∑ j, x j * (N y) j := by
  have := dot_apply_apply hN x (N y)
  rwa [hN.invol] at this

/-- The homogenized NOT is self-adjoint for the dot product of the control space. -/
theorem homMap_dot {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (u v : HVec d) :
    ∑ μ, homMap N u μ * v μ = ∑ μ, u μ * homMap N v μ := by
  rw [Fin.sum_univ_succ, Fin.sum_univ_succ, homMap_zero, homMap_zero]
  congr 1
  simp only [homMap_succ]
  exact dot_apply hN (Matrix.vecTail u) (Matrix.vecTail v)

/-! ### §F — joint vectors as operators on the control space -/

/-- A joint vector as the operator `v ↦ ω *ᵥ v` on the control space. -/
def toOp (ω : W d) : HVec d →ₗ[ℝ] HVec d := Matrix.toLin' (Matrix.of ω)

/-- The joint vector of an operator (its matrix). -/
def fromOp (F : HVec d →ₗ[ℝ] HVec d) : W d := Matrix.of.symm (Matrix.toLin'.symm F)

theorem toOp_fromOp (F : HVec d →ₗ[ℝ] HVec d) : toOp (fromOp F) = F := by
  simp only [toOp, fromOp, Equiv.apply_symm_apply, LinearEquiv.apply_symm_apply]

theorem fromOp_toOp (ω : W d) : fromOp (toOp ω) = ω := by
  simp only [toOp, fromOp, LinearEquiv.symm_apply_apply, Equiv.symm_apply_apply]

theorem toOp_injective : Function.Injective (toOp : W d → HVec d →ₗ[ℝ] HVec d) :=
  fun ω₁ ω₂ h => by rw [← fromOp_toOp ω₁, h, fromOp_toOp]

theorem toOp_apply (ω : W d) (v : HVec d) (μ : Fin (d + 1)) :
    toOp ω v μ = ∑ ν, ω μ ν * v ν := by
  simp only [toOp, Matrix.toLin'_apply, Matrix.mulVec, dotProduct, Matrix.of_apply]

/-- `toOp` as a linear map. -/
def toOpLin : W d →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) where
  toFun := toOp
  map_add' ω₁ ω₂ := by
    apply LinearMap.ext; intro v; funext μ
    simp only [toOp_apply, LinearMap.add_apply, Pi.add_apply, add_mul, Finset.sum_add_distrib]
  map_smul' c ω := by
    apply LinearMap.ext; intro v; funext μ
    simp only [toOp_apply, LinearMap.smul_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply,
      Finset.mul_sum, mul_assoc]

theorem toOpLin_apply (ω : W d) : toOpLin ω = toOp ω := rfl

/-- `fromOp` as a linear map. -/
def fromOpLin : (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] W d where
  toFun := fromOp
  map_add' F₁ F₂ := by
    apply toOp_injective
    rw [toOp_fromOp, ← toOpLin_apply, map_add, toOpLin_apply, toOpLin_apply, toOp_fromOp,
      toOp_fromOp]
  map_smul' c F := by
    apply toOp_injective
    rw [toOp_fromOp, ← toOpLin_apply, map_smul, toOpLin_apply, toOp_fromOp, RingHom.id_apply]

theorem fromOpLin_apply (F : HVec d →ₗ[ℝ] HVec d) : fromOpLin F = fromOp F := rfl

/-- The control action in operator form: left composition with the homogenized NOT. -/
theorem toOp_actC (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :
    toOp (actC N ω) = homMap N ∘ₗ toOp ω := by
  apply LinearMap.ext; intro v
  have hcol : toOp ω v = ∑ ν, v ν • (fun κ => ω κ ν) := by
    funext κ
    simp only [toOp_apply, Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
    exact Finset.sum_congr rfl fun ν _ => mul_comm _ _
  rw [LinearMap.comp_apply, hcol, map_sum]
  funext μ
  simp only [toOp_apply, actC, Finset.sum_apply, map_smul, Pi.smul_apply, smul_eq_mul]
  exact Finset.sum_congr rfl fun ν _ => mul_comm _ _

/-- The target action in operator form: right composition with the homogenized NOT. -/
theorem toOp_actT {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (ω : W d) : toOp (actT N ω) = toOp ω ∘ₗ homMap N := by
  apply LinearMap.ext; intro v
  funext μ
  simp only [toOp_apply, LinearMap.comp_apply, actT]
  exact homMap_dot hN (ω μ) v

theorem actT_actT {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (ω : W d) :
    actT N (actT N ω) = ω := by
  funext μ
  simp only [actT, homMap_homMap hN]

theorem actC_actC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (ω : W d) :
    actC N (actC N ω) = ω := by
  funext μ ν
  have : (fun κ => actC N ω κ ν) = homMap N (fun κ => ω κ ν) := rfl
  simp only [actC]
  rw [this, homMap_homMap hN]
