/-
  OIBridge/EqvK2Block.lean — design module of the research thread `research/equivalence` (node E19,
  draft S6 §H). Not adopted, not certified, not a round: Theorem C19-1 of the countermodels thread
  (handoff HO-31 item 1) in the vocabulary of the pair-level K2 schema of `EqvK2Schema`, on the same
  dictionary.

  §H.1  The block-diagonal matrices `P₀ ⊗ U₀ + P₁ ⊗ U₁` (`blockMat`), their action on tables through the
        dictionary (`blockAct`), and the invariance hypothesis `BlockInvariant K`: invariance under every
        pair of special unitaries — the (b)-instances for the operations of the block group
        `H = SU(2) × SU(2)`, the identity component of the group the clause's operations generate.
  §H.2  One token: every vector of `ℂ²` is carried to `(‖a‖, 0)` by a special unitary (`suTo`).
  §H.3  Reachability (C19-1 (a)): every rank-one positive matrix is a block conjugate of the dictionary
        image of a nonnegative multiple of a product state of the ball (`reach_block`).
  §H.4  The forcing (C19-1 (b)): products (H1), self-duality (H3) and block invariance give `K = Q3`
        (`pairCone_eq_Q3_of_block`) — with no reachability hypothesis and no gate hypothesis; `Q3` is
        block-invariant (`Q3_blockInvariant`); given H1 and H3, `K = Q3` exactly when `K` is block-invariant
        (`pairCone_eq_Q3_iff_block`; the two directions are the two theorems).
  §H.5  Block invariance gives the full-flow form of A_miss (`aMiss_of_blockInvariant`): the flow through
        the half-angle phase `diag(e^{−it/2}, e^{it/2})`, the cyclic permutation through `cycMat`, both
        special unitaries.

  Every hypothesis is a premise. Nothing here sources H1, H3 or the block invariance; nothing here shows
  that the block invariance follows from the gate and the flow (the written generation step of
  NOTES-E19, `blockInvariant_of_driveWords`, open); nothing here concerns availability or more than two
  tokens.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.EqvK2Converse

namespace OIBridge
namespace EqvK2Block

open Matrix CompositeDimension MonoidalCompletion EqvK2Schema EqvK2Converse
open scoped ComplexOrder

noncomputable section

/-! ### §H.1 — the block group and its action on tables -/

/-- The projector `|0⟩⟨0|` of the control. -/
def P0 : Matrix (Fin 2) (Fin 2) ℂ := !![1, 0; 0, 0]

/-- The projector `|1⟩⟨1|` of the control. -/
def P1 : Matrix (Fin 2) (Fin 2) ℂ := !![0, 0; 0, 1]

/-- The block-diagonal matrix `P₀ ⊗ U₀ + P₁ ⊗ U₁`. -/
def blockMat (U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  tensorOf P0 U₀ + tensorOf P1 U₁

/-- The table carried by a block-diagonal conjugation, read back through the coordinates. -/
def blockAct (U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) : W 3 :=
  coordOf (blockMat U₀ U₁ * dict ω * (blockMat U₀ U₁)ᴴ)

/-- A special unitary: a unitary matrix of determinant one. -/
def IsSU (U : Matrix (Fin 2) (Fin 2) ℂ) : Prop := U ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ U.det = 1

/-- **Block invariance**: `K` is carried into itself by every pair of special unitaries acting
blockwise — the (b)-instances for the operations of the group `H = SU(2) × SU(2)` of HO-31 item 1. -/
def BlockInvariant (K : Set (W 3)) : Prop :=
  ∀ U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ, IsSU U₀ → IsSU U₁ → ∀ ω ∈ K, blockAct U₀ U₁ ω ∈ K

/-- The dictionary image of the carried table is the conjugate. -/
theorem dict_blockAct (U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) :
    dict (blockAct U₀ U₁ ω) = blockMat U₀ U₁ * dict ω * (blockMat U₀ U₁)ᴴ :=
  dict_coordOf _ (Matrix.isHermitian_mul_mul_conjTranspose _ (dict_isHermitian ω))

/-- A pair vector from its two control blocks. -/
def blockVec (u v : Fin 2 → ℂ) : Fin 2 × Fin 2 → ℂ := fun p => ![u, v] p.1 p.2

theorem blockVec_eq (x : Fin 2 × Fin 2 → ℂ) :
    blockVec (fun j => x (0, j)) (fun j => x (1, j)) = x := by
  funext p
  obtain ⟨i, j⟩ := p
  fin_cases i <;> rfl

/-- The block matrix acts blockwise on block vectors. -/
theorem blockMat_mulVec (U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ) (u v : Fin 2 → ℂ) :
    blockMat U₀ U₁ *ᵥ blockVec u v = blockVec (U₀ *ᵥ u) (U₁ *ᵥ v) := by
  funext p
  obtain ⟨i, j⟩ := p
  fin_cases i <;> fin_cases j <;>
    simp [blockMat, blockVec, P0, P1, Matrix.mulVec, dotProduct, Fintype.sum_prod_type,
      Fin.sum_univ_two, Matrix.add_apply, tensorOf_apply] <;> ring

/-- Conjugating a rank-one matrix. -/
theorem conj_vecMulVec (B : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (y : Fin 2 × Fin 2 → ℂ) :
    B * Matrix.vecMulVec y (star y) * Bᴴ = Matrix.vecMulVec (B *ᵥ y) (star (B *ᵥ y)) := by
  rw [Matrix.mul_vecMulVec, Matrix.vecMulVec_mul, Matrix.star_mulVec]

/-! ### §H.2 — one token: a special unitary to the north pole -/

/-- The squared norm of a one-token vector. -/
def nrm2 (a : Fin 2 → ℂ) : ℝ := Complex.normSq (a 0) + Complex.normSq (a 1)

theorem nrm2_nonneg (a : Fin 2 → ℂ) : 0 ≤ nrm2 a :=
  add_nonneg (Complex.normSq_nonneg _) (Complex.normSq_nonneg _)

/-- The norm. -/
def nrm (a : Fin 2 → ℂ) : ℝ := Real.sqrt (nrm2 a)

theorem nrm_sq (a : Fin 2 → ℂ) : nrm a ^ 2 = nrm2 a := Real.sq_sqrt (nrm2_nonneg a)

theorem nrm_nonneg (a : Fin 2 → ℂ) : 0 ≤ nrm a := Real.sqrt_nonneg _

theorem nrm2_eq_conj (a : Fin 2 → ℂ) :
    ((nrm2 a : ℝ) : ℂ) = star (a 0) * a 0 + star (a 1) * a 1 := by
  simp only [nrm2, Complex.ofReal_add, Complex.normSq_eq_conj_mul_self, Complex.star_def]

theorem eq_zero_of_nrm_eq_zero {a : Fin 2 → ℂ} (h : nrm a = 0) : a = 0 := by
  have h2 : nrm2 a = 0 := by rw [← nrm_sq a, h]; ring
  have h0 : Complex.normSq (a 0) = 0 := by
    have := Complex.normSq_nonneg (a 0)
    have := Complex.normSq_nonneg (a 1)
    unfold nrm2 at h2
    linarith
  have h1 : Complex.normSq (a 1) = 0 := by
    have := Complex.normSq_nonneg (a 0)
    have := Complex.normSq_nonneg (a 1)
    unfold nrm2 at h2
    linarith
  funext i
  fin_cases i
  · simpa using Complex.normSq_eq_zero.mp h0
  · simpa using Complex.normSq_eq_zero.mp h1

/-- The unnormalised rotation `[[ā₀, ā₁], [−a₁, a₀]]`. -/
def rotTo (a : Fin 2 → ℂ) : Matrix (Fin 2) (Fin 2) ℂ := !![star (a 0), star (a 1); -(a 1), a 0]

theorem rotTo_mulVec (a : Fin 2 → ℂ) : rotTo a *ᵥ a = ![((nrm2 a : ℝ) : ℂ), 0] := by
  rw [nrm2_eq_conj]
  funext i
  fin_cases i <;>
    simp [rotTo, Matrix.mulVec, dotProduct, Fin.sum_univ_two] <;> ring

theorem rotTo_mul_star (a : Fin 2 → ℂ) :
    rotTo a * star (rotTo a) = ((nrm2 a : ℝ) : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  rw [nrm2_eq_conj, Matrix.star_eq_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rotTo, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Matrix.one_apply] <;>
    ring

theorem rotTo_det (a : Fin 2 → ℂ) : (rotTo a).det = ((nrm2 a : ℝ) : ℂ) := by
  rw [nrm2_eq_conj, Matrix.det_fin_two]
  first
    | (simp [rotTo]; ring)
    | (simp [rotTo]; done)
    | (simp only [rotTo, Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
        Matrix.head_cons, Matrix.empty_val', Matrix.cons_val_fin_one]; ring)

/-- The special unitary carrying `a` to `(‖a‖, 0)`: the normalised rotation, or `1` when `a = 0`. -/
def suTo (a : Fin 2 → ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  if nrm a = 0 then 1 else ((nrm a : ℂ)⁻¹) • rotTo a

theorem star_inv_ofReal (r : ℝ) : star ((r : ℂ)⁻¹) = (r : ℂ)⁻¹ := by
  first
    | (rw [star_inv₀, Complex.star_def, Complex.conj_ofReal])
    | (simp [Complex.star_def])

theorem suTo_isSU (a : Fin 2 → ℂ) : IsSU (suTo a) := by
  unfold suTo
  split_ifs with h
  · exact ⟨Matrix.mem_unitaryGroup_iff.mpr (by simp), Matrix.det_one⟩
  · have hr : (nrm a : ℂ) ≠ 0 := by exact_mod_cast h
    have hr2 : (nrm a : ℂ) ^ 2 = ((nrm2 a : ℝ) : ℂ) := by exact_mod_cast nrm_sq a
    constructor
    · rw [Matrix.mem_unitaryGroup_iff, star_smul, star_inv_ofReal, Matrix.smul_mul, Matrix.mul_smul,
        rotTo_mul_star, smul_smul, smul_smul, ← hr2]
      have hone : (nrm a : ℂ)⁻¹ * (nrm a : ℂ)⁻¹ * (nrm a : ℂ) ^ 2 = 1 := by
        field_simp
      first
        | (rw [hone, one_smul])
        | (rw [show (nrm a : ℂ)⁻¹ * ((nrm a : ℂ)⁻¹ * (nrm a : ℂ) ^ 2) = 1 by field_simp, one_smul])
        | (simp only [smul_smul]; rw [show (nrm a : ℂ)⁻¹ * (nrm a : ℂ)⁻¹ * (nrm a : ℂ) ^ 2 = 1 by
            field_simp, one_smul])
    · rw [Matrix.det_smul, rotTo_det, Fintype.card_fin, ← hr2]
      field_simp

theorem suTo_mulVec (a : Fin 2 → ℂ) : suTo a *ᵥ a = ![(nrm a : ℂ), 0] := by
  unfold suTo
  split_ifs with h
  · have ha := eq_zero_of_nrm_eq_zero h
    rw [h, ha, Matrix.mulVec_zero]
    funext i
    fin_cases i <;> simp
  · have hr : (nrm a : ℂ) ≠ 0 := by exact_mod_cast h
    have hr2 : (nrm a : ℂ) ^ 2 = ((nrm2 a : ℝ) : ℂ) := by exact_mod_cast nrm_sq a
    rw [Matrix.smul_mulVec, rotTo_mulVec, ← hr2]
    funext i
    fin_cases i
    · first
        | (simp; field_simp; ring)
        | (simp; field_simp)
        | (simp; done)
        | (simp [pow_two]; field_simp; ring)
    · simp

/-- The conjugate transpose of a special unitary is a special unitary. -/
theorem isSU_conjTranspose {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : IsSU U) : IsSU Uᴴ := by
  refine ⟨?_, ?_⟩
  · rw [← Matrix.star_eq_conjTranspose, Matrix.mem_unitaryGroup_iff, star_star]
    exact Matrix.mem_unitaryGroup_iff'.mp hU.1
  · rw [Matrix.det_conjTranspose, hU.2, star_one]

/-! ### §H.3 — reachability: C19-1 (a) in dictionary form -/

/-- The ball state with Bloch vector `(2αβ, 0, α² − β²)/(α² + β²)` (the zero vector when `α = β = 0`). -/
def bloch (α β : ℝ) : Fin 3 → ℝ :=
  ![2 * α * β / (α ^ 2 + β ^ 2), 0, (α ^ 2 - β ^ 2) / (α ^ 2 + β ^ 2)]

theorem bloch_mem_eball (α β : ℝ) : bloch α β ∈ TransitiveBody.eball 3 := by
  rw [TransitiveBody.mem_eball, Fin.sum_univ_three]
  have e0 : bloch α β 0 = 2 * α * β / (α ^ 2 + β ^ 2) := rfl
  have e1 : bloch α β 1 = 0 := rfl
  have e2 : bloch α β 2 = (α ^ 2 - β ^ 2) / (α ^ 2 + β ^ 2) := rfl
  rw [e0, e1, e2]
  by_cases h : α ^ 2 + β ^ 2 = 0
  · simp [h]
  · have key : (2 * α * β / (α ^ 2 + β ^ 2)) ^ 2 + (0 : ℝ) ^ 2 + ((α ^ 2 - β ^ 2) / (α ^ 2 + β ^ 2)) ^ 2
        = 1 := by
      field_simp
      ring
    rw [key]

theorem z3_mem_eball : z3 ∈ TransitiveBody.eball 3 := by
  rw [TransitiveBody.mem_eball, Fin.sum_univ_three]
  simp [z3]

/-- The Kronecker vector of two one-token vectors. -/
def tensVec (u v : Fin 2 → ℂ) : Fin 2 × Fin 2 → ℂ := fun p => u p.1 * v p.2

theorem tensVec_eq_blockVec (α β : ℝ) :
    tensVec ![(α : ℂ), (β : ℂ)] ![1, 0] = blockVec ![(α : ℂ), 0] ![(β : ℂ), 0] := by
  funext p
  obtain ⟨i, j⟩ := p
  fin_cases i <;> fin_cases j <;> simp [tensVec, blockVec]

/-- The Kronecker product of two rank-one matrices is the rank-one matrix of the Kronecker vector. -/
theorem tensorOf_vecMulVec (u v : Fin 2 → ℂ) :
    tensorOf (Matrix.vecMulVec u (star u)) (Matrix.vecMulVec v (star v)) =
      Matrix.vecMulVec (tensVec u v) (star (tensVec u v)) := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [tensorOf_apply, Matrix.vecMulVec_apply, tensVec, Pi.star_apply, star_mul']
  ring

theorem tensorOf_smul_left (c : ℂ) (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    tensorOf (c • A) B = c • tensorOf A B := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [tensorOf_apply, Matrix.smul_apply, smul_eq_mul]
  ring

theorem tensorOf_smul_right (c : ℂ) (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    tensorOf A (c • B) = c • tensorOf A B := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [tensorOf_apply, Matrix.smul_apply, smul_eq_mul]
  ring

/-- The one-token matrix of the north pole is `|0⟩⟨0|`. -/
theorem tokMat_hom_z3 : tokMat (hom z3) = Matrix.vecMulVec ![(1 : ℂ), 0] (star ![(1 : ℂ), 0]) := by
  rw [tokMat_eq]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.vecMulVec_apply, z3]

/-- The one-token matrix of the Bloch state is the normalised rank-one matrix of `(α, β)`. -/
theorem tokMat_hom_bloch (α β : ℝ) (h : α ^ 2 + β ^ 2 ≠ 0) :
    tokMat (hom (bloch α β)) =
      (((α ^ 2 + β ^ 2 : ℝ) : ℂ)⁻¹) • Matrix.vecMulVec ![(α : ℂ), (β : ℂ)] (star ![(α : ℂ), (β : ℂ)]) := by
  have hc' : (α : ℂ) ^ 2 + (β : ℂ) ^ 2 ≠ 0 := by exact_mod_cast h
  have h0 : hom (bloch α β) 0 = 1 := rfl
  have h1 : hom (bloch α β) 1 = 2 * α * β / (α ^ 2 + β ^ 2) := rfl
  have h2 : hom (bloch α β) 2 = 0 := rfl
  have h3 : hom (bloch α β) 3 = (α ^ 2 - β ^ 2) / (α ^ 2 + β ^ 2) := rfl
  rw [tokMat_eq, h0, h1, h2, h3]
  ext i j
  -- the scalar and the rank-one matrix are applied before any `simp` (which would otherwise unfold
  -- `vecMulVec` of a literal into rows by `cons_vecMulVec` and leave the scalar unapplied)
  rw [Matrix.smul_apply, Matrix.vecMulVec_apply, smul_eq_mul]
  fin_cases i <;> fin_cases j <;>
    simp <;>
    first
      | (field_simp; ring1)
      | (field_simp; done)
      | ring1
      | (field_simp [hc']; ring1)
      | (field_simp [hc']; done)

/-- The dictionary image of the scaled product state is the rank-one matrix of the block vector. -/
theorem dict_prod_bloch (α β : ℝ) :
    dict ((α ^ 2 + β ^ 2) • prodState (bloch α β) z3) =
      Matrix.vecMulVec (blockVec ![(α : ℂ), 0] ![(β : ℂ), 0])
        (star (blockVec ![(α : ℂ), 0] ![(β : ℂ), 0])) := by
  rw [← tensVec_eq_blockVec, ← tensorOf_vecMulVec, dict_smul, dict_prodState, tokMat_hom_z3]
  by_cases h : α ^ 2 + β ^ 2 = 0
  · have hα : α = 0 := by nlinarith [sq_nonneg α, sq_nonneg β]
    have hβ : β = 0 := by nlinarith [sq_nonneg α, sq_nonneg β]
    subst hα
    subst hβ
    have hz : ∀ i : Fin 2, (![((0 : ℝ) : ℂ), ((0 : ℝ) : ℂ)] : Fin 2 → ℂ) i = 0 := by
      intro i
      fin_cases i <;> simp
    ext ⟨i, j⟩ ⟨k, l⟩
    -- the entries are applied before any `simp` (as in `tensorOf_vecMulVec`)
    simp only [Matrix.smul_apply, tensorOf_apply, Matrix.vecMulVec_apply, Complex.real_smul, hz]
    simp
  · rw [tokMat_hom_bloch α β h, tensorOf_smul_left]
    have hc : ((α ^ 2 + β ^ 2 : ℝ) : ℂ) ≠ 0 := by exact_mod_cast h
    have hone : ((α ^ 2 + β ^ 2 : ℝ) : ℂ) * ((α ^ 2 + β ^ 2 : ℝ) : ℂ)⁻¹ = 1 := mul_inv_cancel₀ hc
    ext p q
    simp only [Matrix.smul_apply, Complex.real_smul, smul_eq_mul]
    first
      | (rw [← mul_assoc, hone, one_mul])
      | (field_simp)
      | (rw [← mul_assoc, mul_inv_cancel₀ hc, one_mul])

/-- **Reachability (C19-1 (a)) in dictionary form.** Every rank-one positive matrix is a block
conjugate, by a pair of special unitaries, of the dictionary image of a nonnegative multiple of a
product state of the ball. -/
theorem reach_block (x : Fin 2 × Fin 2 → ℂ) :
    ∃ U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ, IsSU U₀ ∧ IsSU U₁ ∧
      ∃ x₀ ∈ TransitiveBody.eball 3, ∃ c : ℝ, 0 ≤ c ∧
        blockMat U₀ U₁ * dict (c • prodState x₀ z3) * (blockMat U₀ U₁)ᴴ =
          Matrix.vecMulVec x (star x) := by
  set a : Fin 2 → ℂ := fun j => x (0, j) with ha
  set b : Fin 2 → ℂ := fun j => x (1, j) with hb
  refine ⟨(suTo a)ᴴ, (suTo b)ᴴ, isSU_conjTranspose (suTo_isSU a), isSU_conjTranspose (suTo_isSU b),
    bloch (nrm a) (nrm b), bloch_mem_eball _ _, nrm a ^ 2 + nrm b ^ 2, by positivity, ?_⟩
  rw [dict_prod_bloch, conj_vecMulVec]
  have hx : blockMat (suTo a)ᴴ (suTo b)ᴴ *ᵥ blockVec ![(nrm a : ℂ), 0] ![(nrm b : ℂ), 0] = x := by
    rw [blockMat_mulVec, ← suTo_mulVec a, ← suTo_mulVec b, Matrix.mulVec_mulVec, Matrix.mulVec_mulVec]
    have hu : (suTo a)ᴴ * suTo a = 1 := by
      rw [← Matrix.star_eq_conjTranspose]
      exact Matrix.mem_unitaryGroup_iff'.mp (suTo_isSU a).1
    have hv : (suTo b)ᴴ * suTo b = 1 := by
      rw [← Matrix.star_eq_conjTranspose]
      exact Matrix.mem_unitaryGroup_iff'.mp (suTo_isSU b).1
    rw [hu, hv, Matrix.one_mulVec, Matrix.one_mulVec]
    exact blockVec_eq x
  rw [hx]

/-! ### §H.4 — the forcing: C19-1 (b) in the schema's vocabulary -/

/-- **Theorem C19-1 (b) in the schema's vocabulary.** Products of ball states (H1), self-duality (H3)
and block invariance force the pair cone to be `Q3` — with no reachability hypothesis and no gate
hypothesis. -/
theorem pairCone_eq_Q3_of_block {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH3 : K = dualW K) (hB : BlockInvariant K) : K = Q3 := by
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
    obtain ⟨U₀, U₁, hU₀, hU₁, x₀, hx₀, c, hc, h⟩ := reach_block x
    refine ⟨blockAct U₀ U₁ (c • prodState x₀ z3),
      hB U₀ U₁ hU₀ hU₁ _ (hsmul c hc _ (hH1 x₀ hx₀ z3 z3_mem_eball)), ?_⟩
    rw [dict_blockAct, h]
  apply Set.Subset.antisymm
  · exact subset_Q3_of_pure_dual hpure fun ω hω => (hK ω).mp hω
  · exact Q3_subset_of_pure hadd hpure

/-- **`Q3` is block-invariant** (the necessity direction in the block form: invariance only). -/
theorem Q3_blockInvariant : BlockInvariant Q3 := by
  intro U₀ U₁ _ _ ω hω
  have hω' : (dict ω).PosSemidef := hω
  show (dict (blockAct U₀ U₁ ω)).PosSemidef
  rw [dict_blockAct]
  exact hω'.mul_mul_conjTranspose_same _

/-- **The block form as an equivalence.** Given H1 and H3, the pair cone is `Q3` exactly when it is
block-invariant. The direction `→` is `Q3_blockInvariant`; the direction `←` is
`pairCone_eq_Q3_of_block`. -/
theorem pairCone_eq_Q3_iff_block {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH3 : K = dualW K) : K = Q3 ↔ BlockInvariant K := by
  constructor
  · rintro rfl
    exact Q3_blockInvariant
  · intro hB
    exact pairCone_eq_Q3_of_block hH1 hH3 hB

/-! ### §H.5 — block invariance gives the full-flow form of A_miss -/

/-- The diagonal block pair is the idle extension. -/
theorem blockMat_same (U : Matrix (Fin 2) (Fin 2) ℂ) :
    blockMat U U = tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U := by
  ext ⟨i, j⟩ ⟨k, l⟩
  fin_cases i <;> fin_cases k <;>
    simp [blockMat, P0, P1, tensorOf_apply, Matrix.add_apply, Matrix.one_apply]

/-- A common unit scalar does not change the conjugation. -/
theorem conj_smul (z : ℂ) (hz : star z * z = 1) (A M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    (z • A) * M * (z • A)ᴴ = A * M * Aᴴ := by
  rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, smul_smul, hz,
    one_smul]

/-- The diagonal phase pair `diag(c − i s, c + i s)`, for real `c`, `s` (kept opaque, so that no
`simp` lemma about the cosine or the sine of a real number can rewrite them). -/
def dphase (c s : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(c : ℂ) - (s : ℂ) * Complex.I, 0; 0, (c : ℂ) + (s : ℂ) * Complex.I]

theorem dphase_isSU (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) : IsSU (dphase c s) := by
  have hC : (c : ℂ) ^ 2 + (s : ℂ) ^ 2 = 1 := by exact_mod_cast h
  constructor
  · rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [dphase, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply,
        Matrix.one_apply] <;>
      first
        | ring1
        | linear_combination hC - (s : ℂ) ^ 2 * Complex.I_sq
        | linear_combination hC + (s : ℂ) ^ 2 * Complex.I_sq
        | linear_combination hC
        | (apply Complex.ext <;> simp <;> nlinarith [h])
  · rw [dphase, Matrix.det_fin_two_of]
    first
      | linear_combination hC - (s : ℂ) ^ 2 * Complex.I_sq
      | linear_combination hC + (s : ℂ) ^ 2 * Complex.I_sq
      | (apply Complex.ext <;> simp <;> nlinarith [h])

/-- The diagonal phase pair is a unit multiple of `phaseMat c s` when `(c₂, s₂)` is the half angle of
`(c, s)`, stated through the two subtraction identities. -/
theorem dphase_eq (c₂ s₂ c s : ℝ) (hc : c₂ = c * c₂ + s * s₂) (hs : s₂ = s * c₂ - c * s₂) :
    dphase c₂ s₂ = ((c₂ : ℂ) - (s₂ : ℂ) * Complex.I) • phaseMat c s := by
  have hcC : (c₂ : ℂ) = (c : ℂ) * c₂ + (s : ℂ) * s₂ := by exact_mod_cast hc
  have hsC : (s₂ : ℂ) = (s : ℂ) * c₂ - (c : ℂ) * s₂ := by exact_mod_cast hs
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [dphase, phaseMat] <;>
    first
      | ring1
      | linear_combination hcC + Complex.I * hsC + ((s₂ : ℂ) * (s : ℂ)) * Complex.I_sq
      | linear_combination (-1 : ℂ) * hcC - Complex.I * hsC - ((s₂ : ℂ) * (s : ℂ)) * Complex.I_sq
      | (apply Complex.ext <;> simp <;> nlinarith [hc, hs])

theorem dphase_unit (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    star ((c : ℂ) - (s : ℂ) * Complex.I) * ((c : ℂ) - (s : ℂ) * Complex.I) = 1 := by
  have hC : (c : ℂ) ^ 2 + (s : ℂ) ^ 2 = 1 := by exact_mod_cast h
  simp only [Complex.star_def, map_sub, map_mul, Complex.conj_ofReal, Complex.conj_I]
  first
    | linear_combination hC - (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination hC + (s : ℂ) ^ 2 * Complex.I_sq
    | (apply Complex.ext <;> simp <;> nlinarith [h])

/-- The half-angle phase `diag(e^{−it/2}, e^{it/2})`. -/
def hphase (t : ℝ) : Matrix (Fin 2) (Fin 2) ℂ := dphase (Real.cos (t / 2)) (Real.sin (t / 2))

theorem hphase_isSU (t : ℝ) : IsSU (hphase t) :=
  dphase_isSU _ _ (Real.cos_sq_add_sin_sq _)

/-- The half-angle phase is a unit multiple of the phase matrix of the flow. -/
theorem hphase_eq (t : ℝ) :
    hphase t = ((Real.cos (t / 2) : ℂ) - (Real.sin (t / 2) : ℂ) * Complex.I) •
      phaseMat (Real.cos t) (Real.sin t) := by
  have hc : Real.cos (t / 2) = Real.cos t * Real.cos (t / 2) + Real.sin t * Real.sin (t / 2) := by
    rw [← Real.cos_sub]
    congr 1
    ring
  have hs : Real.sin (t / 2) = Real.sin t * Real.cos (t / 2) - Real.cos t * Real.sin (t / 2) := by
    rw [← Real.sin_sub]
    congr 1
    ring
  exact dphase_eq _ _ _ _ hc hs

theorem hphase_unit (t : ℝ) :
    star ((Real.cos (t / 2) : ℂ) - (Real.sin (t / 2) : ℂ) * Complex.I) *
      ((Real.cos (t / 2) : ℂ) - (Real.sin (t / 2) : ℂ) * Complex.I) = 1 :=
  dphase_unit _ _ (Real.cos_sq_add_sin_sq _)

/-- The cyclic permutation's lift is a special unitary. -/
theorem cycMat_isSU : IsSU cycMat := by
  constructor
  · rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, cycMat_conjTranspose]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [cycMat, cycMatH, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
      first
        | ring1
        | linear_combination (-1 / 2 : ℂ) * Complex.I_sq
        | linear_combination (1 / 2 : ℂ) * Complex.I_sq
        | linear_combination (-1 / 4 : ℂ) * Complex.I_sq
        | linear_combination (1 / 4 : ℂ) * Complex.I_sq
        | (apply Complex.ext <;> simp <;> norm_num)
  · rw [cycMat, Matrix.det_fin_two_of]
    first
      | ring1
      | linear_combination (-1 / 2 : ℂ) * Complex.I_sq
      | linear_combination (1 / 2 : ℂ) * Complex.I_sq
      | (apply Complex.ext <;> simp <;> norm_num)

/-- **Block invariance gives the full-flow form of A_miss** (the flow and the cyclic permutation on
one token are block pairs of special unitaries). -/
theorem aMiss_of_blockInvariant {K : Set (W 3)} (hB : BlockInvariant K) :
    ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K := by
  intro t ω hω
  refine ⟨?_, ?_⟩
  · have h := hB (hphase t) (hphase t) (hphase_isSU t) (hphase_isSU t) ω hω
    have heq : blockAct (hphase t) (hphase t) ω = actT (KInfFoundations.rotLin t) ω := by
      apply dict_injective
      rw [dict_blockAct, blockMat_same, dict_actT_rotLin, hphase_eq, tensorOf_smul_right,
        conj_smul _ (hphase_unit t)]
    rw [heq] at h
    exact h
  · have h := hB cycMat cycMat cycMat_isSU cycMat_isSU ω hω
    have heq : blockAct cycMat cycMat ω =
        actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω := by
      apply dict_injective
      rw [dict_blockAct, blockMat_same, dict_actT_cyc]
    rw [heq] at h
    exact h

end

end EqvK2Block
end OIBridge

#print axioms OIBridge.EqvK2Block.dict_blockAct
#print axioms OIBridge.EqvK2Block.blockMat_mulVec
#print axioms OIBridge.EqvK2Block.conj_vecMulVec
#print axioms OIBridge.EqvK2Block.suTo_isSU
#print axioms OIBridge.EqvK2Block.suTo_mulVec
#print axioms OIBridge.EqvK2Block.dict_prod_bloch
#print axioms OIBridge.EqvK2Block.reach_block
#print axioms OIBridge.EqvK2Block.pairCone_eq_Q3_of_block
#print axioms OIBridge.EqvK2Block.Q3_blockInvariant
#print axioms OIBridge.EqvK2Block.pairCone_eq_Q3_iff_block
#print axioms OIBridge.EqvK2Block.aMiss_of_blockInvariant
