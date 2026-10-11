/-
  OIBridge/EqvK2Schema.lean — design module of the research thread `research/equivalence` (node E11,
  skeleton S6). Not adopted, not certified, not a round: the pair-level K2 schema with its dictionary
  and its cone step as kernel statements and the reachability lemma as a hypothesis, on a disposable
  branch.

  §A–§C  The two-token dictionary of DIM-1's pair carrier `W 3`. The definitions `pauli`, `tokMat`
         and `dict` are those of the bridge thread's draft `BridgeDictionary.lean` (sha256 `e4b60411…`),
         verbatim, so that both threads use one dictionary: `dict ω = ¼ Σ ω_μν σ_μ ⊗ σ_ν` in the kernel's
         tensor `tensorOf`, control token first. Proved: the product law
         `dict (prodState x y) = tensorOf (tokMat (hom x)) (tokMat (hom y))` (`dict_prodState`, with the
         fix the bridge recorded for `dict_tens`: full expansion of the four-element sums, then `ring`);
         real linearity (`dictLin`); Hermiticity; the pairing compatibility
         `ipW ω η = 4 · tr (dict ω * dict η)` (`ipW_eq_trace`) for the Euclidean table pairing `ipW`;
         injectivity through the coordinate functionals (`coordOf_dict`).
  §D     Completeness of the Pauli tensors and the linear equivalence
         `dictEquiv : W 3 ≃ₗ[ℝ] selfAdjoint (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)`.
  §E     The cone step. `Q3` is the set of tables whose dictionary image is positive semidefinite.
         LOWER (`Q3_subset_of_pure`): a set closed under addition that contains a table of every
         rank-one positive matrix `x xᴴ` contains `Q3` (through the kernel's PSD factorization
         `BoundaryAudit.psdFactorization_discharged`). UPPER (`subset_Q3_of_pure_dual`): if such a set
         lies in its own dual under `ipW`, it lies in `Q3`. Positive control: `Q3 = dualW Q3`.
  §F     The assembly `pairCone_eq_Q3_of_drive`: products of ball states (H1), `cnot`-invariance (H2),
         self-duality `K = dualW K` (H3) and invariance under one token's rotations about the third axis
         and the cyclic permutation `cycEquiv` (A_miss, in the form of handoff HO-5) give `K = Q3`, given
         the reachability statement `ReachPure` (lemma L4 of the thread's NOTES-E10) as a hypothesis.

  Every hypothesis is a premise. Nothing here sources H2, H3, A_miss or `ReachPure`, and nothing here
  concerns more than two tokens.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompositeDimension
import OIBridge.BoundaryAudit
import Mathlib.LinearAlgebra.Matrix.PosDef

namespace OIBridge
namespace EqvK2Schema

open Matrix CompositeDimension MonoidalCompletion
open scoped ComplexOrder

noncomputable section

/-! ### §A — the Pauli matrices -/

/-- The Pauli matrices `σ₀ = 1, σ₁ = X, σ₂ = Y, σ₃ = Z` (the bridge draft's `pauli`, verbatim). -/
noncomputable def pauli : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ :=
  ![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]

/-- Each Pauli matrix is Hermitian. -/
theorem pauli_conjTranspose (μ : Fin 4) : (pauli μ)ᴴ = pauli μ := by
  fin_cases μ <;> (ext i j; fin_cases i <;> fin_cases j <;> simp [pauli, Matrix.one_apply])

/-- Orthogonality of the Pauli matrices under the trace pairing. -/
theorem trace_pauli_mul (μ ν : Fin 4) :
    Matrix.trace (pauli μ * pauli ν) = if μ = ν then 2 else 0 := by
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [pauli, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.one_apply] <;> norm_num

/-- Completeness of the Pauli matrices, entrywise. -/
theorem pauli_complete (a b c d : Fin 2) :
    ∑ μ : Fin 4, pauli μ a b * pauli μ c d = if a = d ∧ b = c then 2 else 0 := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp +decide [pauli, Fin.sum_univ_four, Matrix.one_apply] <;> norm_num

/-! ### §B — the kernel tensor on one-token matrices -/

theorem tensorOf_mul (A B C D : Matrix (Fin 2) (Fin 2) ℂ) :
    tensorOf A B * tensorOf C D = tensorOf (A * C) (B * D) := by
  ext ⟨a1, a2⟩ ⟨b1, b2⟩
  simp only [Matrix.mul_apply, tensorOf_apply, Fintype.sum_prod_type, Fin.sum_univ_two]
  ring

theorem trace_tensorOf (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix.trace (tensorOf A B) = Matrix.trace A * Matrix.trace B := by
  simp only [Matrix.trace, Matrix.diag_apply, tensorOf_apply, Fintype.sum_prod_type,
    Fin.sum_univ_two]
  ring

theorem tensorOf_conjTranspose (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    (tensorOf A B)ᴴ = tensorOf Aᴴ Bᴴ := by
  ext ⟨a1, a2⟩ ⟨b1, b2⟩
  simp only [Matrix.conjTranspose_apply, tensorOf_apply]
  exact star_mul' _ _

/-- Orthogonality of the Pauli tensors. -/
theorem trace_T_mul_T (μ ν μ' ν' : Fin 4) :
    Matrix.trace (tensorOf (pauli μ) (pauli ν) * tensorOf (pauli μ') (pauli ν')) =
      (if μ = μ' then 2 else 0) * (if ν = ν' then 2 else 0) := by
  rw [tensorOf_mul, trace_tensorOf, trace_pauli_mul, trace_pauli_mul]

/-! ### §C — the dictionary and its compatibilities -/

/-- One token's homogenized vector as a 2 × 2 complex matrix: `v ↦ ½ Σ v_μ σ_μ` (bridge draft). -/
noncomputable def tokMat (v : HVec 3) : Matrix (Fin 2) (Fin 2) ℂ :=
  ∑ μ : Fin 4, ((v μ : ℂ) / 2) • pauli μ

/-- The two-token dictionary: `ω ↦ ¼ Σ ω_μν σ_μ ⊗ σ_ν` (bridge draft). -/
noncomputable def dict (ω : W 3) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  ∑ μ : Fin 4, ∑ ν : Fin 4, ((ω μ ν : ℂ) / 4) • tensorOf (pauli μ) (pauli ν)

/-- **The product law of the dictionary.** -/
theorem dict_tens (X Y : HVec 3) : dict (tens X Y) = tensorOf (tokMat X) (tokMat Y) := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [dict, tokMat, tens_apply, Matrix.sum_apply, Matrix.add_apply, Matrix.smul_apply,
    tensorOf_apply, smul_eq_mul, Complex.ofReal_mul, Fin.sum_univ_four]
  ring

/-- **First compatibility**: product states of the ball go to Kronecker products. -/
theorem dict_prodState (x y : Fin 3 → ℝ) :
    dict (prodState x y) = tensorOf (tokMat (hom x)) (tokMat (hom y)) :=
  dict_tens (hom x) (hom y)

theorem dict_add (ω η : W 3) : dict (ω + η) = dict ω + dict η := by
  ext a b
  simp only [dict, Matrix.add_apply, Matrix.sum_apply, Matrix.smul_apply, Pi.add_apply,
    smul_eq_mul, Complex.ofReal_add, Fin.sum_univ_four]
  ring

theorem dict_smul (c : ℝ) (ω : W 3) : dict (c • ω) = c • dict ω := by
  ext a b
  simp only [dict, Matrix.sum_apply, Matrix.add_apply, Matrix.smul_apply, Pi.smul_apply,
    smul_eq_mul, Complex.real_smul, Complex.ofReal_mul, Fin.sum_univ_four]
  ring

/-- The dictionary as a real linear map. -/
noncomputable def dictLin : W 3 →ₗ[ℝ] Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ where
  toFun := dict
  map_add' := dict_add
  map_smul' := dict_smul

theorem dict_sum {ι : Type*} (s : Finset ι) (g : ι → W 3) :
    dict (∑ k ∈ s, g k) = ∑ k ∈ s, dict (g k) :=
  map_sum dictLin g s

theorem star_ofReal_div_four (r : ℝ) : star ((r : ℂ) / 4) = (r : ℂ) / 4 := by
  have h : (starRingEnd ℂ) ((r : ℂ) / 4) = (r : ℂ) / 4 :=
    Complex.conj_eq_iff_real.mpr ⟨r / 4, by norm_num⟩
  rwa [starRingEnd_apply] at h

/-- The dictionary image of a table is Hermitian. -/
theorem dict_conjTranspose (ω : W 3) : (dict ω)ᴴ = dict ω := by
  simp only [dict, Matrix.conjTranspose_sum, Matrix.conjTranspose_smul, tensorOf_conjTranspose,
    pauli_conjTranspose, star_ofReal_div_four]

theorem dict_isHermitian (ω : W 3) : (dict ω).IsHermitian :=
  dict_conjTranspose ω

/-- The coordinate functionals read the dictionary back. -/
theorem trace_T_mul_dict (η : W 3) (μ ν : Fin 4) :
    Matrix.trace (tensorOf (pauli μ) (pauli ν) * dict η) = (η μ ν : ℂ) := by
  simp only [dict, Finset.mul_sum, Matrix.mul_smul, Matrix.trace_sum, Matrix.trace_smul,
    trace_T_mul_T, smul_eq_mul]
  fin_cases μ <;> fin_cases ν <;> simp [Fin.sum_univ_four] <;> ring

theorem dict_mul_left (ω : W 3) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    dict ω * M =
      ∑ μ : Fin 4, ∑ ν : Fin 4, ((ω μ ν : ℂ) / 4) • (tensorOf (pauli μ) (pauli ν) * M) := by
  simp only [dict, Finset.sum_mul, Matrix.smul_mul]

/-- The Euclidean table pairing of the joint carrier. -/
def ipW (ω η : W 3) : ℝ := ∑ μ : Fin 4, ∑ ν : Fin 4, ω μ ν * η μ ν

theorem trace_dict_mul (ω η : W 3) :
    Matrix.trace (dict ω * dict η) = ((ipW ω η : ℝ) : ℂ) / 4 := by
  rw [dict_mul_left]
  simp only [Matrix.trace_sum, Matrix.trace_add, Matrix.trace_smul, trace_T_mul_dict, smul_eq_mul,
    ipW, Complex.ofReal_sum, Complex.ofReal_mul, Complex.ofReal_add, Fin.sum_univ_four]
  ring

/-- **Second compatibility**: the table pairing is four times the trace pairing. -/
theorem ipW_eq_trace (ω η : W 3) :
    ((ipW ω η : ℝ) : ℂ) = 4 * Matrix.trace (dict ω * dict η) := by
  rw [trace_dict_mul]
  ring

/-- The coordinates of a matrix in the Pauli tensors. -/
def coordOf (H : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) : Fin 4 → Fin 4 → ℝ :=
  fun μ ν => (Matrix.trace (tensorOf (pauli μ) (pauli ν) * H)).re

theorem coordOf_dict (ω : W 3) : coordOf (dict ω) = ω := by
  funext μ ν
  simp only [coordOf, trace_T_mul_dict, Complex.ofReal_re]

theorem dict_injective : Function.Injective dict := fun ω η h => by
  have h2 := congrArg coordOf h
  rwa [coordOf_dict, coordOf_dict] at h2

/-! ### §D — completeness, and the linear equivalence with the Hermitian matrices -/

set_option maxHeartbeats 2000000 in
theorem sum_T_entry (H : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (a1 a2 b1 b2 : Fin 2) :
    (∑ μ : Fin 4, ∑ ν : Fin 4, Matrix.trace (tensorOf (pauli μ) (pauli ν) * H) *
        tensorOf (pauli μ) (pauli ν) (a1, a2) (b1, b2)) =
      ∑ p1 : Fin 2, ∑ p2 : Fin 2, ∑ q1 : Fin 2, ∑ q2 : Fin 2, H (q1, q2) (p1, p2) *
        ((∑ μ : Fin 4, pauli μ p1 q1 * pauli μ a1 b1) *
          (∑ ν : Fin 4, pauli ν p2 q2 * pauli ν a2 b2)) := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, tensorOf_apply,
    Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_four]
  ring

set_option maxHeartbeats 2000000 in
/-- **Completeness of the Pauli tensors.** -/
theorem dict_complete4 (H : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    ∑ μ : Fin 4, ∑ ν : Fin 4, Matrix.trace (tensorOf (pauli μ) (pauli ν) * H) •
      tensorOf (pauli μ) (pauli ν) = (4 : ℂ) • H := by
  ext ⟨a1, a2⟩ ⟨b1, b2⟩
  simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul]
  rw [sum_T_entry]
  simp only [pauli_complete]
  fin_cases a1 <;> fin_cases a2 <;> fin_cases b1 <;> fin_cases b2 <;>
    simp [Fin.sum_univ_two] <;> ring

/-- The Pauli coordinates of a Hermitian matrix are real. -/
theorem trace_T_mul_real (H : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (hH : H.IsHermitian)
    (μ ν : Fin 4) :
    (((Matrix.trace (tensorOf (pauli μ) (pauli ν) * H)).re : ℝ) : ℂ) =
      Matrix.trace (tensorOf (pauli μ) (pauli ν) * H) := by
  rw [← Complex.conj_eq_iff_re, starRingEnd_apply, ← Matrix.trace_conjTranspose,
    Matrix.conjTranspose_mul, hH.eq, tensorOf_conjTranspose, pauli_conjTranspose,
    pauli_conjTranspose, Matrix.trace_mul_comm]

/-- The dictionary of the coordinates of a Hermitian matrix is the matrix. -/
theorem dict_coordOf (H : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (hH : H.IsHermitian) :
    dict (coordOf H) = H := by
  have h4 := dict_complete4 H
  have hr := trace_T_mul_real H hH
  ext a b
  have hab := congrFun (congrFun h4 a) b
  simp only [Matrix.sum_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul,
    Fin.sum_univ_four] at hab
  simp only [dict, coordOf, hr, Matrix.sum_apply, Matrix.add_apply, Matrix.smul_apply,
    smul_eq_mul, Fin.sum_univ_four]
  linear_combination hab / 4

/-- **The dictionary as a linear equivalence** `W 3 ≃ Herm(ℂ² ⊗ ℂ²)`. -/
noncomputable def dictEquiv :
    W 3 ≃ₗ[ℝ] selfAdjoint (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) where
  toFun ω := ⟨dict ω, selfAdjoint.mem_iff.mpr
    (Matrix.isHermitian_iff_isSelfAdjoint.mp (dict_isHermitian ω))⟩
  map_add' ω η := Subtype.ext (dict_add ω η)
  map_smul' c ω := Subtype.ext (dict_smul c ω)
  invFun H := coordOf H.1
  left_inv ω := coordOf_dict ω
  right_inv H := Subtype.ext (dict_coordOf H.1
    (Matrix.isHermitian_iff_isSelfAdjoint.mpr (selfAdjoint.mem_iff.mp H.2)))

theorem dictEquiv_apply (ω : W 3) : (dictEquiv ω : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) =
    dict ω := rfl

/-! ### §E — the cone step -/

/-- The dual of a set of tables under the table pairing. -/
def dualW (K : Set (W 3)) : Set (W 3) := {η | ∀ ω ∈ K, 0 ≤ ipW ω η}

theorem mem_dualW {K : Set (W 3)} {η : W 3} : η ∈ dualW K ↔ ∀ ω ∈ K, 0 ≤ ipW ω η :=
  Iff.rfl

/-- `Q3`: the tables whose dictionary image is positive semidefinite. -/
def Q3 : Set (W 3) := {ω | (dict ω).PosSemidef}

theorem mem_Q3 {ω : W 3} : ω ∈ Q3 ↔ (dict ω).PosSemidef := Iff.rfl

theorem ipW_add_right (ω η ζ : W 3) : ipW ω (η + ζ) = ipW ω η + ipW ω ζ := by
  simp only [ipW, Pi.add_apply, Fin.sum_univ_four]
  ring

theorem ipW_smul_right (c : ℝ) (ω η : W 3) : ipW ω (c • η) = c * ipW ω η := by
  simp only [ipW, Pi.smul_apply, smul_eq_mul, Fin.sum_univ_four]
  ring

theorem trace_vecMulVec_mul (x : Fin 2 × Fin 2 → ℂ)
    (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    Matrix.trace (Matrix.vecMulVec x (star x) * M) = star x ⬝ᵥ (M *ᵥ x) := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, Matrix.vecMulVec_apply,
    dotProduct, Matrix.mulVec, Pi.star_apply, Fintype.sum_prod_type, Fin.sum_univ_two]
  ring

/-- A table whose pairing with a table of every rank-one positive matrix is nonnegative has a
positive semidefinite dictionary image. -/
theorem posSemidef_dict_of_pure {η : W 3}
    (h : ∀ x : Fin 2 × Fin 2 → ℂ,
      ∃ ω : W 3, dict ω = Matrix.vecMulVec x (star x) ∧ 0 ≤ ipW ω η) :
    (dict η).PosSemidef := by
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg (dict_isHermitian η) fun x => ?_
  obtain ⟨ω, hω, h0⟩ := h x
  have htr : star x ⬝ᵥ (dict η *ᵥ x) = ((ipW ω η : ℝ) : ℂ) / 4 := by
    rw [← trace_vecMulVec_mul, ← hω, trace_dict_mul]
  rw [htr, Complex.nonneg_iff, Complex.div_ofNat_re, Complex.div_ofNat_im, Complex.ofReal_re,
    Complex.ofReal_im]
  exact ⟨div_nonneg h0 (by norm_num), by norm_num⟩

/-- **UPPER.** A set containing a table of every rank-one positive matrix and lying in its own
dual lies in `Q3`. -/
theorem subset_Q3_of_pure_dual {K : Set (W 3)}
    (hpure : ∀ x : Fin 2 × Fin 2 → ℂ, ∃ ω ∈ K, dict ω = Matrix.vecMulVec x (star x))
    (hdual : K ⊆ dualW K) : K ⊆ Q3 := by
  intro η hη
  show (dict η).PosSemidef
  refine posSemidef_dict_of_pure fun x => ?_
  obtain ⟨ω, hωK, hω⟩ := hpure x
  exact ⟨ω, hω, mem_dualW.mp (hdual hη) ω hωK⟩

/-- **LOWER.** A set closed under addition and containing a table of every rank-one positive matrix
contains `Q3`. -/
theorem Q3_subset_of_pure {K : Set (W 3)}
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hpure : ∀ x : Fin 2 × Fin 2 → ℂ, ∃ ω ∈ K, dict ω = Matrix.vecMulVec x (star x)) :
    Q3 ⊆ K := by
  intro ω hω
  have hω' : (dict ω).PosSemidef := hω
  obtain ⟨B, hB⟩ := BoundaryAudit.psdFactorization_discharged (Fin 2 × Fin 2) (dict ω) hω'
  choose f hfK hf using hpure
  have hsum : dict ω = ∑ k : Fin 2 × Fin 2, dict (f (fun i => B i k)) := by
    rw [hB]
    ext i j
    simp only [hf, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.sum_apply,
      Matrix.vecMulVec_apply, Pi.star_apply]
  have heq : ω = ∑ k : Fin 2 × Fin 2, f (fun i => B i k) := by
    apply dict_injective
    rw [hsum, dict_sum]
  rw [heq]
  exact Finset.sum_induction_nonempty (fun k => f (fun i => B i k)) (· ∈ K)
    (fun a b ha hb => hadd a ha b hb) Finset.univ_nonempty (fun k _ => hfK _)

/-- Positive control, first inclusion: `Q3` lies in its dual. -/
theorem Q3_subset_dualW : Q3 ⊆ dualW Q3 := by
  intro η hη
  rw [mem_dualW]
  intro ω hω
  have hη' : (dict η).PosSemidef := hη
  have hω' : (dict ω).PosSemidef := hω
  obtain ⟨B, hB⟩ := BoundaryAudit.psdFactorization_discharged (Fin 2 × Fin 2) (dict ω) hω'
  have hdec : dict ω = ∑ k : Fin 2 × Fin 2,
      Matrix.vecMulVec (fun i => B i k) (star fun i => B i k) := by
    rw [hB]
    ext i j
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.sum_apply,
      Matrix.vecMulVec_apply, Pi.star_apply]
  have htr : Matrix.trace (dict ω * dict η) =
      ∑ k : Fin 2 × Fin 2, star (fun i => B i k) ⬝ᵥ (dict η *ᵥ fun i => B i k) := by
    rw [hdec, Finset.sum_mul, Matrix.trace_sum]
    simp only [trace_vecMulVec_mul]
  have hre : (Matrix.trace (dict ω * dict η)).re = ipW ω η / 4 := by
    rw [trace_dict_mul, Complex.div_ofNat_re, Complex.ofReal_re]
  have hnn : 0 ≤ (Matrix.trace (dict ω * dict η)).re := by
    rw [htr, Complex.re_sum]
    exact Finset.sum_nonneg fun k _ =>
      (Complex.nonneg_iff.mp (hη'.dotProduct_mulVec_nonneg _)).1
  linarith

/-- Positive control, second inclusion: the dual of `Q3` lies in `Q3`. -/
theorem dualW_Q3_subset : dualW Q3 ⊆ Q3 := by
  intro η hη
  show (dict η).PosSemidef
  refine posSemidef_dict_of_pure fun x => ⟨coordOf (Matrix.vecMulVec x (star x)), ?_, ?_⟩
  · exact dict_coordOf _ (Matrix.posSemidef_vecMulVec_self_star x).isHermitian
  · refine mem_dualW.mp hη _ ?_
    show (dict (coordOf (Matrix.vecMulVec x (star x)))).PosSemidef
    rw [dict_coordOf _ (Matrix.posSemidef_vecMulVec_self_star x).isHermitian]
    exact Matrix.posSemidef_vecMulVec_self_star x

/-- **Positive control for H3**: `Q3` is self-dual under the table pairing. -/
theorem Q3_selfDual : Q3 = dualW Q3 :=
  Set.Subset.antisymm Q3_subset_dualW dualW_Q3_subset

/-! ### §F — the drive words and the assembly -/

/-- `N` acting on the target token, as a linear map of the pair carrier. -/
noncomputable def actTLin (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : W 3 →ₗ[ℝ] W 3 where
  toFun := actT N
  map_add' ω η := by
    funext μ ν
    simp only [actT_apply, Pi.add_apply, map_add]
  map_smul' c ω := by
    funext μ ν
    simp only [actT_apply, Pi.smul_apply, map_smul, RingHom.id_apply]

/-- The generators: `cnot`, the target token's rotations about the third axis (the linear part of
`ball3Drive`'s flow) and its cyclic permutation (`ball3Drive`'s `J`). -/
noncomputable def driveGens : Set (Module.End ℝ (W 3)) :=
  {(cnot : W 3 →ₗ[ℝ] W 3)} ∪ Set.range (fun t : ℝ => actTLin (KInfFoundations.rotLin t)) ∪
    {actTLin (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))}

/-- The drive words: the monoid the generators generate. -/
noncomputable def driveWords : Submonoid (Module.End ℝ (W 3)) := Submonoid.closure driveGens

/-- H2 and A_miss make a set invariant under every drive word. -/
theorem driveWords_preserve {K : Set (W 3)} (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)
    {g : Module.End ℝ (W 3)} (hg : g ∈ driveWords) : ∀ ω ∈ K, g ω ∈ K := by
  induction hg using Submonoid.closure_induction with
  | mem g hg =>
    intro ω hω
    simp only [driveGens, Set.mem_union, Set.mem_singleton_iff, Set.mem_range] at hg
    rcases hg with (rfl | ⟨t, rfl⟩) | rfl
    · exact hH2 ω hω
    · exact (hA t ω hω).1
    · exact (hA 0 ω hω).2
  | one => intro ω hω; exact hω
  | mul g h _ _ ihg ihh => intro ω hω; exact ihg _ (ihh _ hω)

/-- **L4, as a hypothesis**: every pure two-token state is, up to a nonnegative scale, the image of a
product state of the ball under a drive word. -/
def ReachPure : Prop :=
  ∀ x : Fin 2 × Fin 2 → ℂ, ∃ g ∈ driveWords, ∃ x₀ ∈ TransitiveBody.eball 3,
    ∃ y₀ ∈ TransitiveBody.eball 3, ∃ c : ℝ, 0 ≤ c ∧
      dict (c • g (prodState x₀ y₀)) = Matrix.vecMulVec x (star x)

/-- **The pair-level K2 schema.** Products (H1), `cnot`-invariance (H2), self-duality (H3) and
invariance under one token's rotations about the third axis and its cyclic permutation (A_miss) force
the pair cone to be `Q3`, given the reachability statement `ReachPure`. -/
theorem pairCone_eq_Q3_of_drive {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hH3 : K = dualW K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)
    (hreach : ReachPure) :
    K = Q3 := by
  have hK : ∀ ω, ω ∈ K ↔ ω ∈ dualW K := fun ω => Set.ext_iff.mp hH3 ω
  have hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K := by
    intro c hc ω hω
    rw [hK] at hω ⊢
    rw [mem_dualW] at hω ⊢
    intro η hη
    rw [ipW_smul_right]
    exact mul_nonneg hc (hω η hη)
  have hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K := by
    intro ω hω η hη
    rw [hK] at hω hη ⊢
    rw [mem_dualW] at hω hη ⊢
    intro ζ hζ
    rw [ipW_add_right]
    exact add_nonneg (hω ζ hζ) (hη ζ hζ)
  have hpure : ∀ x : Fin 2 × Fin 2 → ℂ, ∃ ω ∈ K, dict ω = Matrix.vecMulVec x (star x) := by
    intro x
    obtain ⟨g, hg, x₀, hx₀, y₀, hy₀, c, hc, h⟩ := hreach x
    exact ⟨c • g (prodState x₀ y₀),
      hsmul c hc _ (driveWords_preserve hH2 hA hg _ (hH1 x₀ hx₀ y₀ hy₀)), h⟩
  apply Set.Subset.antisymm
  · exact subset_Q3_of_pure_dual hpure fun ω hω => (hK ω).mp hω
  · exact Q3_subset_of_pure hadd hpure

end

end EqvK2Schema
end OIBridge

#print axioms OIBridge.EqvK2Schema.pauli_conjTranspose
#print axioms OIBridge.EqvK2Schema.trace_pauli_mul
#print axioms OIBridge.EqvK2Schema.pauli_complete
#print axioms OIBridge.EqvK2Schema.trace_T_mul_T
#print axioms OIBridge.EqvK2Schema.dict_tens
#print axioms OIBridge.EqvK2Schema.dict_prodState
#print axioms OIBridge.EqvK2Schema.dict_sum
#print axioms OIBridge.EqvK2Schema.dict_isHermitian
#print axioms OIBridge.EqvK2Schema.trace_T_mul_dict
#print axioms OIBridge.EqvK2Schema.trace_dict_mul
#print axioms OIBridge.EqvK2Schema.ipW_eq_trace
#print axioms OIBridge.EqvK2Schema.dict_injective
#print axioms OIBridge.EqvK2Schema.dict_complete4
#print axioms OIBridge.EqvK2Schema.dict_coordOf
#print axioms OIBridge.EqvK2Schema.dictEquiv
#print axioms OIBridge.EqvK2Schema.trace_vecMulVec_mul
#print axioms OIBridge.EqvK2Schema.posSemidef_dict_of_pure
#print axioms OIBridge.EqvK2Schema.subset_Q3_of_pure_dual
#print axioms OIBridge.EqvK2Schema.Q3_subset_of_pure
#print axioms OIBridge.EqvK2Schema.Q3_selfDual
#print axioms OIBridge.EqvK2Schema.driveWords_preserve
#print axioms OIBridge.EqvK2Schema.pairCone_eq_Q3_of_drive
