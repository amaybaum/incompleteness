/-
  OIBridge/EqvK2Converse.lean — design module of the research thread `research/equivalence` (node E15,
  draft S6 §G). Not adopted, not certified, not a round: the necessity direction of the pair-level K2
  schema of `EqvK2Schema`, on the same definitions.

  §G.1  The dictionary split along the control index, `dict ω = Σ_μ (½ σ_μ) ⊗ tokMat (ω μ)`, and the
        conjugation law `tensorOf A (U B Uᴴ) = (1 ⊗ U)(A ⊗ B)(1 ⊗ U)ᴴ`.
  §G.2  One token: the homogenized rotation about the third axis acts on `tokMat` as conjugation by
        `diag(1, cos t + i sin t)` (`tokMat_rot`), the cyclic permutation as conjugation by
        `(I − i(X + Y + Z))/2` (`tokMat_cyc`).
  §G.3  The two intertwining lemmas: the dictionary carries `actT (rotLin t)` to conjugation by
        `1 ⊗ diag(1, cos t + i sin t)` (`dict_actT_rotLin`) and `actT cycEquiv` to conjugation by
        `1 ⊗ (I − i(X + Y + Z))/2` (`dict_actT_cyc`).
  §G.4  `Q3` is invariant under both, because unitary conjugation preserves positive semidefiniteness
        (`Q3_aMiss`); with `EqvK2Schema.pairCone_eq_Q3_of_drive`, given H1, H2, H3 and `ReachPure`,
        `K = Q3` exactly when `K` is invariant under both (`pairCone_eq_Q3_iff_drive`). The direction
        `→` is `Q3_aMiss`, the direction `←` is `pairCone_eq_Q3_of_drive`.

  Every hypothesis is a premise. Nothing here sources H2, H3, A_miss or `ReachPure`, and nothing here
  concerns more than two tokens.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.EqvK2Schema

namespace OIBridge
namespace EqvK2Converse

open Matrix CompositeDimension MonoidalCompletion EqvK2Schema
open scoped ComplexOrder

noncomputable section

/-! ### §G.1 — the dictionary along the control index -/

/-- The dictionary split along the control index. -/
theorem dict_eq_sum_tensorOf (ω : W 3) :
    dict ω = ∑ μ : Fin 4, tensorOf (((1 : ℂ) / 2) • pauli μ) (tokMat (ω μ)) := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [dict, tokMat, Matrix.sum_apply, Matrix.add_apply, Matrix.smul_apply, tensorOf_apply,
    smul_eq_mul, Fin.sum_univ_four]
  ring

/-- The dictionary of a target action, through the split. -/
theorem dict_actT (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (ω : W 3) :
    dict (actT N ω) =
      ∑ μ : Fin 4, tensorOf (((1 : ℂ) / 2) • pauli μ) (tokMat (homMap N (ω μ))) :=
  dict_eq_sum_tensorOf (actT N ω)

/-- Conjugating the target factor of a Kronecker product. -/
theorem tensorOf_conj (A B U : Matrix (Fin 2) (Fin 2) ℂ) :
    tensorOf A (U * B * Uᴴ) = tensorOf 1 U * tensorOf A B * (tensorOf 1 U)ᴴ := by
  rw [tensorOf_conjTranspose, Matrix.conjTranspose_one, tensorOf_mul, tensorOf_mul, one_mul,
    mul_one]

/-! ### §G.2 — one token -/

/-- One token's matrix, entrywise. -/
theorem tokMat_eq (v : HVec 3) : tokMat v =
    !![((v 0 : ℂ) + (v 3 : ℂ)) / 2, ((v 1 : ℂ) - (v 2 : ℂ) * Complex.I) / 2;
      ((v 1 : ℂ) + (v 2 : ℂ) * Complex.I) / 2, ((v 0 : ℂ) - (v 3 : ℂ)) / 2] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    first
      | (simp [tokMat, pauli, Matrix.sum_apply, Matrix.smul_apply, Fin.sum_univ_four,
          Matrix.one_apply]; done)
      | (simp [tokMat, pauli, Matrix.sum_apply, Matrix.smul_apply, Fin.sum_univ_four,
          Matrix.one_apply]; ring)
      | (apply Complex.ext <;>
          simp [tokMat, pauli, Matrix.sum_apply, Matrix.smul_apply, Fin.sum_univ_four,
            Matrix.one_apply] <;> ring)

/-- Two `2 × 2` literals agree when their entries do. -/
theorem mat2_ext {a b c d e f g h : ℂ} (h1 : a = e) (h2 : b = f) (h3 : c = g) (h4 : d = h) :
    !![a, b; c, d] = !![e, f; g, h] := by
  rw [h1, h2, h3, h4]

/-- The phase matrix `diag(1, c + i s)`. -/
def phaseMat (c s : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![1, 0; 0, (c : ℂ) + (s : ℂ) * Complex.I]

theorem phaseMat_conjTranspose (c s : ℝ) : (phaseMat c s)ᴴ = phaseMat c (-s) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    first
      | (simp [phaseMat, Matrix.conjTranspose_apply]; done)
      | (simp [phaseMat, Matrix.conjTranspose_apply]; ring)
      | (simp [phaseMat, Matrix.conjTranspose_apply, Complex.star_def]; done)
      | (simp [phaseMat, Matrix.conjTranspose_apply, Complex.star_def]; ring)
      | (simp [phaseMat, Matrix.conjTranspose_apply]; apply Complex.ext <;> simp [Complex.star_def])

/-- The homogenized rotation about the third axis, coordinatewise. -/
theorem homMap_rotLin (t : ℝ) (v : HVec 3) :
    homMap (KInfFoundations.rotLin t) v 0 = v 0 ∧
      homMap (KInfFoundations.rotLin t) v 1 = Real.cos t * v 1 - Real.sin t * v 2 ∧
      homMap (KInfFoundations.rotLin t) v 2 = Real.sin t * v 1 + Real.cos t * v 2 ∧
      homMap (KInfFoundations.rotLin t) v 3 = v 3 :=
  ⟨rfl, rfl, rfl, rfl⟩

/-- **One token, rotation**: conjugation by `diag(1, cos t + i sin t)`. -/
theorem tokMat_rot (t : ℝ) (v : HVec 3) :
    tokMat (homMap (KInfFoundations.rotLin t) v) =
      phaseMat (Real.cos t) (Real.sin t) * tokMat v * (phaseMat (Real.cos t) (Real.sin t))ᴴ := by
  obtain ⟨h0, h1, h2, h3⟩ := homMap_rotLin t v
  have hcs := Real.sin_sq_add_cos_sq t
  have e0 : (Real.sin t ^ 2 + Real.cos t ^ 2) * v 0 = v 0 := by rw [hcs, one_mul]
  have e3 : (Real.sin t ^ 2 + Real.cos t ^ 2) * v 3 = v 3 := by rw [hcs, one_mul]
  rw [phaseMat_conjTranspose, tokMat_eq (homMap (KInfFoundations.rotLin t) v), tokMat_eq v,
    h0, h1, h2, h3]
  simp only [phaseMat]
  rw [Matrix.mul_fin_two, Matrix.mul_fin_two]
  refine mat2_ext ?_ ?_ ?_ ?_ <;> apply Complex.ext <;>
    simp only [Complex.add_re, Complex.add_im, Complex.sub_re, Complex.sub_im, Complex.mul_re,
      Complex.mul_im, Complex.neg_re, Complex.neg_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.I_re, Complex.I_im, Complex.one_re, Complex.one_im, Complex.zero_re, Complex.zero_im,
      Complex.div_ofNat_re, Complex.div_ofNat_im] <;>
    linarith [e0, e3]

/-- The matrix `(I − i(X + Y + Z))/2`. -/
def cycMat : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(1 - Complex.I) / 2, (-1 - Complex.I) / 2; (1 - Complex.I) / 2, (1 + Complex.I) / 2]

/-- Its conjugate transpose. -/
def cycMatH : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(1 + Complex.I) / 2, (1 + Complex.I) / 2; (-1 + Complex.I) / 2, (1 - Complex.I) / 2]

theorem cycMat_conjTranspose : cycMatᴴ = cycMatH := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    first
      | (simp [cycMat, cycMatH, Matrix.conjTranspose_apply]; done)
      | (simp [cycMat, cycMatH, Matrix.conjTranspose_apply]; ring)
      | (simp [cycMat, cycMatH, Matrix.conjTranspose_apply, Complex.star_def]; done)
      | (simp [cycMat, cycMatH, Matrix.conjTranspose_apply, Complex.star_def]; ring)
      | (simp [cycMat, cycMatH, Matrix.conjTranspose_apply]; apply Complex.ext <;>
          simp [Complex.star_def] <;> ring)

/-- The homogenized cyclic permutation, coordinatewise: `(v₀, v₁, v₂, v₃) ↦ (v₀, v₃, v₁, v₂)`. -/
theorem homMap_cyc (v : HVec 3) :
    homMap (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) v 0 = v 0 ∧
      homMap (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) v 1 = v 3 ∧
      homMap (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) v 2 = v 1 ∧
      homMap (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) v 3 = v 2 :=
  ⟨rfl, rfl, rfl, rfl⟩

/-- **One token, cyclic permutation**: conjugation by `(I − i(X + Y + Z))/2`. -/
theorem tokMat_cyc (v : HVec 3) :
    tokMat (homMap (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) v) =
      cycMat * tokMat v * cycMatᴴ := by
  obtain ⟨h0, h1, h2, h3⟩ := homMap_cyc v
  rw [cycMat_conjTranspose,
    tokMat_eq (homMap (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) v), tokMat_eq v,
    h0, h1, h2, h3]
  simp only [cycMat, cycMatH]
  rw [Matrix.mul_fin_two, Matrix.mul_fin_two]
  refine mat2_ext ?_ ?_ ?_ ?_ <;> apply Complex.ext <;>
    simp only [Complex.add_re, Complex.add_im, Complex.sub_re, Complex.sub_im, Complex.mul_re,
      Complex.mul_im, Complex.neg_re, Complex.neg_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.I_re, Complex.I_im, Complex.one_re, Complex.one_im, Complex.zero_re, Complex.zero_im,
      Complex.div_ofNat_re, Complex.div_ofNat_im] <;>
    linarith

/-! ### §G.3 — the two intertwining lemmas -/

/-- **Intertwining, rotation**: the dictionary carries `actT (rotLin t)` to conjugation by
`1 ⊗ diag(1, cos t + i sin t)`. -/
theorem dict_actT_rotLin (t : ℝ) (ω : W 3) :
    dict (actT (KInfFoundations.rotLin t) ω) =
      tensorOf 1 (phaseMat (Real.cos t) (Real.sin t)) * dict ω *
        (tensorOf 1 (phaseMat (Real.cos t) (Real.sin t)))ᴴ := by
  rw [dict_actT, dict_eq_sum_tensorOf ω, Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [tokMat_rot, tensorOf_conj]

/-- **Intertwining, cyclic permutation**: the dictionary carries `actT cycEquiv` to conjugation by
`1 ⊗ (I − i(X + Y + Z))/2`. -/
theorem dict_actT_cyc (ω : W 3) :
    dict (actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω) =
      tensorOf 1 cycMat * dict ω * (tensorOf 1 cycMat)ᴴ := by
  rw [dict_actT, dict_eq_sum_tensorOf ω, Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [tokMat_cyc, tensorOf_conj]

/-! ### §G.4 — the necessity direction and the equivalence -/

/-- **`Q3` is invariant under one token's rotations about the third axis and its cyclic
permutation** (the necessity direction: the full-flow form of A_miss holds for `Q3`). -/
theorem Q3_aMiss : ∀ t : ℝ, ∀ ω ∈ Q3, actT (KInfFoundations.rotLin t) ω ∈ Q3 ∧
    actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ Q3 := by
  intro t ω hω
  have hω' : (dict ω).PosSemidef := hω
  refine ⟨?_, ?_⟩
  · show (dict (actT (KInfFoundations.rotLin t) ω)).PosSemidef
    rw [dict_actT_rotLin]
    first
      | exact hω'.mul_mul_conjTranspose_same _
      | simpa using hω'.conjTranspose_mul_mul_same
          (tensorOf 1 (phaseMat (Real.cos t) (Real.sin t)))ᴴ
  · show (dict (actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω)).PosSemidef
    rw [dict_actT_cyc]
    first
      | exact hω'.mul_mul_conjTranspose_same _
      | simpa using hω'.conjTranspose_mul_mul_same (tensorOf 1 cycMat)ᴴ

/-- **The pair-level K2 schema as an equivalence.** Given products of ball states (H1),
`cnot`-invariance (H2), self-duality (H3) and the reachability statement `ReachPure`, the pair cone is
`Q3` exactly when it is invariant under one token's rotations about the third axis and its cyclic
permutation (A_miss). The direction `→` is `Q3_aMiss`; the direction `←` is
`EqvK2Schema.pairCone_eq_Q3_of_drive`. -/
theorem pairCone_eq_Q3_iff_drive {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K) (hH3 : K = dualW K) (hreach : ReachPure) :
    K = Q3 ↔ ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K := by
  constructor
  · rintro rfl
    exact Q3_aMiss
  · intro hA
    exact pairCone_eq_Q3_of_drive hH1 hH2 hH3 hA hreach

end

end EqvK2Converse
end OIBridge

#print axioms OIBridge.EqvK2Converse.dict_eq_sum_tensorOf
#print axioms OIBridge.EqvK2Converse.tensorOf_conj
#print axioms OIBridge.EqvK2Converse.tokMat_eq
#print axioms OIBridge.EqvK2Converse.tokMat_rot
#print axioms OIBridge.EqvK2Converse.tokMat_cyc
#print axioms OIBridge.EqvK2Converse.dict_actT_rotLin
#print axioms OIBridge.EqvK2Converse.dict_actT_cyc
#print axioms OIBridge.EqvK2Converse.Q3_aMiss
#print axioms OIBridge.EqvK2Converse.pairCone_eq_Q3_iff_drive
