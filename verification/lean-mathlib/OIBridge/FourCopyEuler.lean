/-
  OIBridge/FourCopyEuler.lean — design (EQ4-F), not adopted: O39, Euler generation of the
  rotations of one ball by the rotations about the third and first axes. Every proof in this file
  is complete. No complex number is used: the angle of a unit vector of the plane is read off with
  `Real.arccos`.

  Route: the third column of a rotation is a unit vector, reached from the pole by the word
  `rot3 ψ ∘ rotX θ` (`exists_euler_angles`, landed); the remaining factor fixes the pole and is a
  rotation about the third axis (`stab_matrix`).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyCore

namespace OIBridge
namespace FourCopy

open Set KInfFoundations OrbitNormalization
open scoped Matrix

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-! ### §A — the matrices of the generators -/

/-- The rotation by `t` about the third axis. -/
def Rz (t : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![Real.cos t, -Real.sin t, 0; Real.sin t, Real.cos t, 0; 0, 0, 1]

/-- The rotation by `t` about the first axis. -/
def Rx (t : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, 0, 0; 0, Real.cos t, -Real.sin t; 0, Real.sin t, Real.cos t]

theorem rot3_linear_apply (t : ℝ) (v : Fin 3 → ℝ) : ((rot3 t).linear : E3) v = rotFun t v := rfl

theorem rotX_linear_apply (t : ℝ) (v : Fin 3 → ℝ) :
    ((rotX t).linear : E3) v = cycEquiv (rotFun t (cycEquiv.symm v)) := rfl

theorem cycEquiv_apply' (v : Fin 3 → ℝ) : cycEquiv v = ![v 2, v 0, v 1] := rfl

theorem cycEquiv_symm_apply' (v : Fin 3 → ℝ) : cycEquiv.symm v = ![v 1, v 2, v 0] := rfl

theorem toMatrix'_rot3 (t : ℝ) : LinearMap.toMatrix' ((rot3 t).linear : E3) = Rz t := by
  ext i j
  rw [LinearMap.toMatrix'_apply, rot3_linear_apply]
  fin_cases i <;> fin_cases j <;> simp +decide [rotFun, Rz]

theorem toMatrix'_rotX (t : ℝ) : LinearMap.toMatrix' ((rotX t).linear : E3) = Rx t := by
  ext i j
  rw [LinearMap.toMatrix'_apply, rotX_linear_apply, cycEquiv_apply', cycEquiv_symm_apply']
  fin_cases i <;> fin_cases j <;> simp +decide [rotFun, Rx]

theorem Rz_mem (t : ℝ) : Rz t ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ := by
  rw [Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff]
  refine ⟨?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp +decide [Rz, Matrix.mul_apply, Fin.sum_univ_three, Matrix.transpose_apply] <;>
      nlinarith [Real.sin_sq_add_cos_sq t]
  · rw [Matrix.det_fin_three]
    simp [Rz] <;> nlinarith [Real.sin_sq_add_cos_sq t]

theorem Rx_mem (t : ℝ) : Rx t ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ := by
  rw [Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff]
  refine ⟨?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp +decide [Rx, Matrix.mul_apply, Fin.sum_univ_three, Matrix.transpose_apply] <;>
      nlinarith [Real.sin_sq_add_cos_sq t]
  · rw [Matrix.det_fin_three]
    simp [Rx] <;> nlinarith [Real.sin_sq_add_cos_sq t]

/-! ### §B — the stabilizer of the pole -/

/-- The angle of a unit vector of the plane. -/
theorem exists_angle {c s : ℝ} (h : c ^ 2 + s ^ 2 = 1) :
    ∃ φ : ℝ, Real.cos φ = c ∧ Real.sin φ = s := by
  have hc2 : c ^ 2 ≤ 1 := by nlinarith [sq_nonneg s]
  have hc := abs_le.mp ((sq_le_one_iff_abs_le_one c).mp hc2)
  have hcos : Real.cos (Real.arccos c) = c := Real.cos_arccos hc.1 hc.2
  have hsin : Real.sin (Real.arccos c) = |s| := by
    rw [Real.sin_arccos, show 1 - c ^ 2 = s ^ 2 by linarith, Real.sqrt_sq_eq_abs]
  rcases le_or_gt 0 s with hs | hs
  · exact ⟨Real.arccos c, hcos, by rw [hsin, abs_of_nonneg hs]⟩
  · exact ⟨-Real.arccos c, by rw [Real.cos_neg, hcos],
      by rw [Real.sin_neg, hsin, abs_of_neg hs, neg_neg]⟩

/-- **Stabilizer lemma.** A rotation matrix fixing the pole is a rotation about the third axis. -/
theorem stab_matrix {S : Matrix (Fin 3) (Fin 3) ℝ}
    (hS : S ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ)
    (h02 : S 0 2 = 0) (h12 : S 1 2 = 0) (h22 : S 2 2 = 1) : ∃ φ : ℝ, S = Rz φ := by
  obtain ⟨hO, hdet⟩ := Matrix.mem_specialOrthogonalGroup_iff.1 hS
  have hr := (Matrix.mem_orthogonalGroup_iff _ _).1 hO
  have hc := (Matrix.mem_orthogonalGroup_iff' _ _).1 hO
  have r22 := congrFun (congrFun hr 2) 2
  have k00 := congrFun (congrFun hc 0) 0
  have k11 := congrFun (congrFun hc 1) 1
  simp only [Matrix.mul_apply, Matrix.transpose_apply, Fin.sum_univ_three, Matrix.one_apply_eq]
    at r22 k00 k11
  rw [h22] at r22
  have hq0 : S 2 0 ^ 2 = 0 := by nlinarith [sq_nonneg (S 2 0), sq_nonneg (S 2 1)]
  have hq1 : S 2 1 ^ 2 = 0 := by nlinarith [sq_nonneg (S 2 0), sq_nonneg (S 2 1)]
  have h20 : S 2 0 = 0 := (pow_eq_zero_iff two_ne_zero).mp hq0
  have h21 : S 2 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp hq1
  rw [Matrix.det_fin_three, h02, h12, h22, h20, h21] at hdet
  rw [h20] at k00
  rw [h21] at k11
  have hsum : (S 1 1 - S 0 0) ^ 2 + (S 0 1 + S 1 0) ^ 2 = 0 := by
    linear_combination k00 + k11 - 2 * hdet
  have hd0 : (S 1 1 - S 0 0) ^ 2 = 0 := by
    nlinarith [sq_nonneg (S 1 1 - S 0 0), sq_nonneg (S 0 1 + S 1 0)]
  have hb0 : (S 0 1 + S 1 0) ^ 2 = 0 := by
    nlinarith [sq_nonneg (S 1 1 - S 0 0), sq_nonneg (S 0 1 + S 1 0)]
  have e1 : S 1 1 = S 0 0 := by
    have := (pow_eq_zero_iff two_ne_zero).mp hd0
    linarith
  have e2 : S 0 1 = -S 1 0 := by
    have := (pow_eq_zero_iff two_ne_zero).mp hb0
    linarith
  have hcs : S 0 0 ^ 2 + S 1 0 ^ 2 = 1 := by linear_combination k00
  obtain ⟨φ, hc', hs'⟩ := exists_angle hcs
  refine ⟨φ, ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Rz, hc', hs', h02, h12, h22, h20, h21, e1, e2]

/-! ### §C — O39 -/

/-- **O39 (Euler generation).** Every rotation of one ball is `rot3 ψ ∘ rotX θ ∘ rot3 φ`. -/
theorem so3_euler {R : E3} (hR : IsRot3 R) :
    ∃ ψ θ φ : ℝ,
      R = ((rot3 ψ).linear : E3) ∘ₗ ((rotX θ).linear : E3) ∘ₗ ((rot3 φ).linear : E3) := by
  obtain ⟨A, hA⟩ : ∃ A, LinearMap.toMatrix' R = A := ⟨_, rfl⟩
  have hAmem : A ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ := by
    rw [← hA]
    exact hR
  obtain ⟨hAO, -⟩ := Matrix.mem_specialOrthogonalGroup_iff.1 hAmem
  have hAtA := (Matrix.mem_orthogonalGroup_iff' _ _).1 hAO
  have hcol : A 0 2 ^ 2 + A 1 2 ^ 2 + A 2 2 ^ 2 = 1 := by
    have h := congrFun (congrFun hAtA 2) 2
    simp only [Matrix.mul_apply, Matrix.transpose_apply, Fin.sum_univ_three,
      Matrix.one_apply_eq] at h
    linear_combination h
  obtain ⟨ψ, θ, h0, h1, h2⟩ := exists_euler_angles (b := fun i => A i 2) hcol
  have h0' : Real.sin ψ * Real.sin θ = A 0 2 := h0
  have h1' : -(Real.cos ψ * Real.sin θ) = A 1 2 := h1
  have h2' : Real.cos θ = A 2 2 := h2
  obtain ⟨G, hG⟩ : ∃ G, Rz ψ * Rx θ = G := ⟨_, rfl⟩
  have hGmem : G ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ := by
    rw [← hG]
    exact Submonoid.mul_mem _ (Rz_mem ψ) (Rx_mem θ)
  obtain ⟨hGO, hGdet⟩ := Matrix.mem_specialOrthogonalGroup_iff.1 hGmem
  have hGGt := (Matrix.mem_orthogonalGroup_iff _ _).1 hGO
  have hGtG := (Matrix.mem_orthogonalGroup_iff' _ _).1 hGO
  have hGcol : ∀ k, G k 2 = A k 2 := by
    intro k
    rw [← hG]
    fin_cases k <;> simp [Rz, Rx, Matrix.mul_apply, Fin.sum_univ_three] <;> linarith
  obtain ⟨S, hS⟩ : ∃ S, Gᵀ * A = S := ⟨_, rfl⟩
  have hSmem : S ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ := by
    rw [← hS]
    refine Submonoid.mul_mem _ ?_ hAmem
    rw [Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff,
      Matrix.transpose_transpose, Matrix.det_transpose]
    exact ⟨hGtG, hGdet⟩
  have hS2 : ∀ i, S i 2 = (1 : Matrix (Fin 3) (Fin 3) ℝ) i 2 := by
    intro i
    rw [← hGtG, ← hS]
    simp only [Matrix.mul_apply, Matrix.transpose_apply, hGcol]
  obtain ⟨φ, hφ⟩ := stab_matrix hSmem (by simp [hS2]) (by simp [hS2]) (by simp [hS2])
  refine ⟨ψ, θ, φ, ?_⟩
  apply LinearMap.toMatrix'.injective
  rw [LinearMap.toMatrix'_comp, LinearMap.toMatrix'_comp, toMatrix'_rot3, toMatrix'_rotX,
    toMatrix'_rot3, hA, ← hφ, ← Matrix.mul_assoc, hG, ← hS, ← Matrix.mul_assoc, hGGt,
    Matrix.one_mul]

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.toMatrix'_rot3
#print axioms OIBridge.FourCopy.toMatrix'_rotX
#print axioms OIBridge.FourCopy.Rz_mem
#print axioms OIBridge.FourCopy.Rx_mem
#print axioms OIBridge.FourCopy.exists_angle
#print axioms OIBridge.FourCopy.stab_matrix
#print axioms OIBridge.FourCopy.so3_euler
