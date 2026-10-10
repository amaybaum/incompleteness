/-
  DRAFT — UNBUILT (EQ4-F proof development, design only; not adopted, not for any branch as is).

  O39 `so3_euler`: every rotation of one ball is `rot3 ψ * rotX θ * rot3 φ`. Route:
  1. the pole `e₃ = ![0, 0, 1]` is carried to the unit vector `b = R e₃`;
  2. the base supplies `ψ, θ` with `(rot3 ψ * rotX θ) e₃ = b` (`exists_euler_angles`, ON:614;
     `euler_apply_pole`, ON:589);
  3. `S = G⁻¹ ∘ R` (`G = rot3 ψ * rotX θ`) is a rotation fixing the pole;
  4. the stabilizer lemma: a rotation fixing the pole is `rot3 φ` (orthogonality forces the third
     row and column to be `e₃`, the `2×2` block is in SO(2), and `(cos φ, sin φ)` is read off with
     `Complex.arg`).
  No Lean toolchain was available; nothing here has been elaborated. Points likely to need iteration
  are marked `-- ITER:`.
-/
import OIBridge.FourCopyPackage

namespace OIBridge
namespace FourCopy

open Set KInfFoundations OrbitNormalization

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-! ### Affine automorphisms fixing the origin act by their linear parts -/

theorem apply_eq_linear_of_fix {g : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)} (h0 : g 0 = 0) (x : Fin 3 → ℝ) :
    g x = g.linear x := by
  have h := g.map_vadd 0 x
  -- ITER: `x +ᵥ 0 = x` and `g.linear x +ᵥ 0 = g.linear x` on a vector space.
  simpa [vadd_eq_add, h0] using h

theorem rot3_zero (t : ℝ) : rot3 t 0 = 0 := by
  rw [rot3_apply]
  apply vec3_ext <;> simp [rotFun]

theorem cyc3_zero : cyc3 0 = 0 := by
  apply vec3_ext <;> rfl

theorem cyc3_inv_zero : cyc3⁻¹ 0 = 0 := by
  rw [inv_apply']
  -- ITER: `cyc3.symm 0 = 0` from `cyc3 0 = 0`.
  rw [AffineEquiv.symm_apply_eq, cyc3_zero]

theorem rotX_zero (θ : ℝ) : rotX θ 0 = 0 := by
  rw [rotX, mul_apply', mul_apply', cyc3_inv_zero, rot3_zero, cyc3_zero]

/-! ### Matrices of the generators -/

/-- The matrix of a linear map of `ℝ³`, entrywise. -/
theorem toMatrix'_entry (f : E3) (i j : Fin 3) :
    LinearMap.toMatrix' f i j = f (Pi.single j 1) i :=
  LinearMap.toMatrix'_apply f i j

/-- `rot3 t` is a rotation. -/
theorem isRot3_rot3 (t : ℝ) : IsRot3 ((rot3 t).linear : E3) := by
  rw [IsRot3, Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff]
  -- ITER: compute the matrix `!![cos t, -sin t, 0; sin t, cos t, 0; 0, 0, 1]` from `rotFun`, then
  -- `A * Aᵀ = 1` and `det A = 1` by `Real.sin_sq_add_cos_sq`.
  have hM : LinearMap.toMatrix' ((rot3 t).linear : E3) =
      !![Real.cos t, -Real.sin t, 0; Real.sin t, Real.cos t, 0; 0, 0, 1] := by
    ext i j
    rw [toMatrix'_entry]
    fin_cases i <;> fin_cases j <;> simp [rot3, rotEquiv, rotLin, rotFun, Pi.single_apply]
  rw [hM]
  refine ⟨?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_three] <;> nlinarith [Real.sin_sq_add_cos_sq t]
  · rw [Matrix.det_fin_three]
    simp
    nlinarith [Real.sin_sq_add_cos_sq t]

/-- `cyc3` is a rotation (a cyclic permutation matrix, determinant `1`). -/
theorem isRot3_cyc3 : IsRot3 (cyc3.linear : E3) := by
  rw [IsRot3, Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff]
  have hM : LinearMap.toMatrix' (cyc3.linear : E3) = !![0, 0, 1; 1, 0, 0; 0, 1, 0] := by
    ext i j
    rw [toMatrix'_entry]
    fin_cases i <;> fin_cases j <;> simp [cyc3, cycEquiv, Pi.single_apply]
  rw [hM]
  refine ⟨?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_three]
  · rw [Matrix.det_fin_three]; simp

/-! ### Closure of `IsRot3` -/

theorem isRot3_comp {f g : E3} (hf : IsRot3 f) (hg : IsRot3 g) : IsRot3 (f ∘ₗ g) := by
  rw [IsRot3, LinearMap.toMatrix'_comp]
  exact Submonoid.mul_mem _ hf hg

theorem isRot3_symm {f : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ)} (hf : IsRot3 (f : E3)) :
    IsRot3 (f.symm : E3) := by
  -- ITER: the matrix of `f.symm` is the inverse of the matrix of `f`, which for an element of the
  -- special orthogonal group is its transpose, again in the group.
  rw [IsRot3]
  have hinv : LinearMap.toMatrix' (f.symm : E3) * LinearMap.toMatrix' (f : E3) = 1 := by
    rw [← LinearMap.toMatrix'_comp]
    simp
  have hmem := hf
  rw [IsRot3, Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff'] at hmem
  have heq : LinearMap.toMatrix' (f.symm : E3) = (LinearMap.toMatrix' (f : E3))ᵀ := by
    have := congrArg (· * (LinearMap.toMatrix' (f : E3))ᵀ) hinv
    simp only [Matrix.mul_assoc, Matrix.mem_orthogonalGroup_iff.1 hmem.1, Matrix.mul_one,
      Matrix.one_mul] at this
    exact this
  rw [heq, Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff,
    Matrix.transpose_transpose, Matrix.det_transpose]
  exact ⟨Matrix.mem_orthogonalGroup_iff'.1 hmem.1, hmem.2⟩

theorem isRot3_rotX (θ : ℝ) : IsRot3 ((rotX θ).linear : E3) := by
  -- `(cyc3 * rot3 θ * cyc3⁻¹).linear = cyc3.linear ∘ (rot3 θ).linear ∘ cyc3.linear.symm`
  -- ITER: through `AffineEquiv.linearHom` (a monoid hom) and `map_mul`, `map_inv`.
  have h : ((rotX θ).linear : E3) =
      (cyc3.linear : E3) ∘ₗ ((rot3 θ).linear : E3) ∘ₗ (cyc3.linear.symm : E3) := by
    rw [rotX]
    rfl
  rw [h]
  exact isRot3_comp isRot3_cyc3 (isRot3_comp (isRot3_rot3 θ) (isRot3_symm isRot3_cyc3))

/-! ### The stabilizer of the pole -/

/-- **Stabilizer lemma.** A rotation fixing `e₃` is a rotation about the third axis. -/
theorem stab_pole {S : E3} (hS : IsRot3 S) (h3 : S ![0, 0, 1] = ![0, 0, 1]) :
    ∃ φ : ℝ, S = ((rot3 φ).linear : E3) := by
  set A := LinearMap.toMatrix' S with hA
  have hmem := hS
  rw [IsRot3, Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff] at hmem
  obtain ⟨hO, hdet⟩ := hmem
  have hO' : Aᵀ * A = 1 := Matrix.mem_orthogonalGroup_iff'.1 (Matrix.mem_orthogonalGroup_iff.2 hO)
  -- the third column is `e₃`
  have hpole : Pi.single (2 : Fin 3) (1 : ℝ) = ![0, 0, 1] := by
    funext i; fin_cases i <;> rfl
  have c0 : A 0 2 = 0 := by rw [hA, toMatrix'_entry, hpole, h3]; rfl
  have c1 : A 1 2 = 0 := by rw [hA, toMatrix'_entry, hpole, h3]; rfl
  have c2 : A 2 2 = 1 := by rw [hA, toMatrix'_entry, hpole, h3]; rfl
  -- the third row is `e₃` (row 2 of `A Aᵀ = 1`)
  have r22 := congrFun (congrFun hO 2) 2
  simp [Matrix.mul_apply, Fin.sum_univ_three, c2] at r22
  have a20 : A 2 0 = 0 := by nlinarith [sq_nonneg (A 2 0), sq_nonneg (A 2 1)]
  have a21 : A 2 1 = 0 := by nlinarith [sq_nonneg (A 2 0), sq_nonneg (A 2 1)]
  -- the `2×2` block: unit columns, orthogonal, determinant `1`
  have k00 := congrFun (congrFun hO' 0) 0
  have k11 := congrFun (congrFun hO' 1) 1
  have k01 := congrFun (congrFun hO' 0) 1
  simp [Matrix.mul_apply, Fin.sum_univ_three, Matrix.transpose_apply, a20, a21] at k00 k11 k01
  rw [Matrix.det_fin_three, c0, c1, c2, a20, a21] at hdet
  simp at hdet
  -- `(A11 - A00)² + (A01 + A10)² = 0`
  have hd : A 1 1 = A 0 0 := by nlinarith [sq_nonneg (A 1 1 - A 0 0), sq_nonneg (A 0 1 + A 1 0)]
  have hb : A 0 1 = -A 1 0 := by nlinarith [sq_nonneg (A 1 1 - A 0 0), sq_nonneg (A 0 1 + A 1 0)]
  -- an angle with `cos φ = A 0 0`, `sin φ = A 1 0`
  set z : ℂ := ⟨A 0 0, A 1 0⟩
  have hz : ‖z‖ = 1 := by
    -- ITER: `Complex.norm_def`/`Complex.abs_apply` and `k00 : A 0 0 ^ 2 + A 1 0 ^ 2 = 1`.
    rw [Complex.norm_def, Complex.normSq_mk]
    rw [show A 0 0 * A 0 0 + A 1 0 * A 1 0 = 1 by nlinarith]
    simp
  have hz0 : z ≠ 0 := by
    intro h; rw [h, norm_zero] at hz; exact zero_ne_one hz
  refine ⟨Complex.arg z, ?_⟩
  have hc : Real.cos (Complex.arg z) = A 0 0 := by rw [Complex.cos_arg hz0, hz, div_one]
  have hs : Real.sin (Complex.arg z) = A 1 0 := by rw [Complex.sin_arg, hz, div_one]
  apply LinearMap.toMatrix'.injective
  ext i j
  rw [← hA]
  -- ITER: the matrix of `rot3 φ`, as in `isRot3_rot3`.
  fin_cases i <;> fin_cases j <;>
    simp [toMatrix'_entry, rot3, rotEquiv, rotLin, rotFun, Pi.single_apply, hc, hs, c0, c1, c2,
      a20, a21, hd, hb] <;> rfl

/-! ### O39 -/

/-- **O39 (Euler generation).** Every rotation of one ball is `rot3 ψ * rotX θ * rot3 φ`. -/
theorem so3_euler {R : E3} (hR : IsRot3 R) :
    ∃ ψ θ φ : ℝ, R = ((rot3 ψ * rotX θ * rot3 φ).linear : E3) := by
  set b := R ![0, 0, 1] with hbdef
  -- `b` is a unit vector: the third column of an orthogonal matrix
  have hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1 := by
    have hmem := hR
    rw [IsRot3, Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff'] at hmem
    have k22 := congrFun (congrFun hmem.1 2) 2
    -- ITER: `(Aᵀ A) 2 2 = Σ i, A i 2 ^ 2` and `A i 2 = b i` (`toMatrix'_entry`, `Pi.single 2 1 = e₃`).
    have hpole : Pi.single (2 : Fin 3) (1 : ℝ) = ![0, 0, 1] := by
      funext i; fin_cases i <;> rfl
    simp only [Matrix.mul_apply, Matrix.transpose_apply, Fin.sum_univ_three, toMatrix'_entry,
      hpole, Matrix.one_apply_eq] at k22
    nlinarith [k22]
  obtain ⟨ψ, θ, h0, h1, h2⟩ := exists_euler_angles hb
  set G := rot3 ψ * rotX θ with hG
  have hG0 : G 0 = 0 := by rw [hG, mul_apply', rotX_zero, rot3_zero]
  have hGb : G ![0, 0, 1] = b := by
    rw [hG, euler_apply_pole]
    exact vec3_ext h0 h1 h2
  -- `S = G⁻¹ ∘ R` fixes the pole and is a rotation
  set S : E3 := (G.linear.symm : E3) ∘ₗ R with hS
  have hS3 : S ![0, 0, 1] = ![0, 0, 1] := by
    show G.linear.symm (R ![0, 0, 1]) = _
    rw [← hbdef, ← hGb, apply_eq_linear_of_fix hG0, LinearEquiv.symm_apply_apply]
  have hGrot : IsRot3 (G.linear : E3) := by
    -- ITER: `(rot3 ψ * rotX θ).linear = (rot3 ψ).linear ∘ (rotX θ).linear` via `linearHom`.
    have : (G.linear : E3) = ((rot3 ψ).linear : E3) ∘ₗ ((rotX θ).linear : E3) := by
      rw [hG]; rfl
    rw [this]
    exact isRot3_comp (isRot3_rot3 ψ) (isRot3_rotX θ)
  have hSrot : IsRot3 S := isRot3_comp (isRot3_symm hGrot) hR
  obtain ⟨φ, hφ⟩ := stab_pole hSrot hS3
  refine ⟨ψ, θ, φ, ?_⟩
  -- `R = G.linear ∘ S`
  have hR' : R = (G.linear : E3) ∘ₗ S := by
    rw [hS]
    ext x
    simp
  rw [hR', hφ]
  -- ITER: `(G * rot3 φ).linear = G.linear ∘ (rot3 φ).linear`.
  rfl

end

end FourCopy
end OIBridge
