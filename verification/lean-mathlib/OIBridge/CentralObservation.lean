import OIBridge.PassiveObservation
import OIBridge.BoundaryAudit

/-!
# Passive observation on a finite-dimensional C*-algebra reads only the center (OI-N3)

A finite-dimensional C*-algebra is, up to isomorphism, a direct sum `⊕ᵢ M_{dᵢ}` of full matrix
algebras. This file works with that algebra concretely, as the **block-diagonal** matrices for a
labelling `blk : S → I` of the basis states by blocks: the block `i` is the full matrix algebra on
the fibre `{s // blk s = i}`, and the center is spanned by the block projectors.

**OI-N1** (`PassiveObservation`) treats a single block: every branch of a passive instrument on a
full matrix algebra is a scalar. **OI-N3** is the general case, and its content is a
classification rather than a bare impossibility:

* **Block preservation** (`branch_preserves_block`). Each branch of a passive instrument sends
  block `i` into block `i`. This is derived, not assumed: passivity on the block projector `Pᵢ`
  forces every Kraus operator to vanish between distinct blocks.
* **Blockwise scalars** (`branch_scalar_on_block`). Restricted to block `i`, each branch is a
  scalar `c a i` — N1 applied on the fibre, through the restriction `restrictMap` whose Choi
  matrix is a principal submatrix of the original.
* **The classification** (`central_classification`). For every block-diagonal state `ρ`,
  `tr (F a ρ) = ∑ᵢ c a i · tr (Pᵢ ρ Pᵢ)`, with `c a i ≥ 0` from complete positivity and
  `∑ₐ c a i = 1` from passivity. Every passive instrument on `⊕ᵢ M_{dᵢ}` induces a classical
  stochastic observation of the center: it reads the block weights through a stochastic matrix,
  and nothing inside any block. The converse — that every stochastic matrix arises from some
  passive instrument — is not stated or proved here.
* **The control** (`blockPinch`). The instrument that keeps block `i` and discards the others is
  completely positive, passive on the algebra, and reads the block weights exactly.
* **The boundary** (`no_complete_passive_of_block`, `blockPinch_separates`,
  `complete_passive_iff_injective`, `injective_iff_commutative`). Complete passive observation of
  the algebra is possible if and only if each block contains at most one basis state, equivalently
  if and only if the labelling is injective — every nonempty block has dimension one — if and
  only if the algebra is commutative.

**Definitions.** A passive instrument on the algebra (`IsBlockPassiveInstrument`) is a finite
family of maps on the ambient matrix algebra, completely positive there, whose nonselective channel
fixes every block-diagonal matrix. Intrinsic completely positive instruments on the block-diagonal
algebra admit the corresponding ambient extension by the standard block conditional expectation
`X ↦ ∑ᵢ Pᵢ X Pᵢ`; that transport is not formalized here, and the kernel statements below are
stated for `IsBlockPassiveInstrument` as defined. Block preservation is a theorem here, not a
hypothesis.

**Not claimed.** Nothing here relates passive incompleteness to `OICore` (OI-N4), and nothing here
says that a passive instrument's silence is an observer. The C*-algebra is taken in its
block-diagonal matrix form; the Wedderburn–Artin identification of an abstract finite-dimensional
C*-algebra with such a form is standard and is not formalized here.
-/

namespace OIBridge
namespace CentralObservation

open Matrix CoherentExtension MonoidalCompletion DimensionalCountermodel
open CompositeSoundness AncillaClosure ClosureObstruction ReferenceSufficiency
open BoundaryAudit PassiveObservation
open scoped ComplexOrder

/-! ### Section A — the block structure -/

section Blocks

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {I : Type*} [DecidableEq I]

/-- **Block-diagonal**: no entry links two distinct blocks. These matrices form the algebra
`⊕ᵢ M_{dᵢ}`. -/
def BlockDiag (blk : S → I) (X : Matrix S S ℂ) : Prop :=
  ∀ s t, blk s ≠ blk t → X s t = 0

/-- **Supported in block `i`**: every entry outside the `i`-th diagonal block vanishes. -/
def InBlock (blk : S → I) (i : I) (X : Matrix S S ℂ) : Prop :=
  ∀ s t, ¬ (blk s = i ∧ blk t = i) → X s t = 0

/-- The projector `Pᵢ` onto block `i`; the block projectors span the center. -/
def blockProj (blk : S → I) (i : I) : Matrix S S ℂ :=
  Matrix.diagonal fun s => if blk s = i then 1 else 0

/-- The `i`-th diagonal block of `X`, `Pᵢ X Pᵢ`. -/
def blockPart (blk : S → I) (i : I) (X : Matrix S S ℂ) : Matrix S S ℂ :=
  Matrix.of fun s t => if blk s = i ∧ blk t = i then X s t else 0

variable (blk : S → I)

omit [Fintype S] [DecidableEq S] in
theorem blockPart_apply (i : I) (X : Matrix S S ℂ) (s t : S) :
    blockPart blk i X s t = if blk s = i ∧ blk t = i then X s t else 0 := rfl

omit [Fintype S] in
theorem blockProj_apply (i : I) (s t : S) :
    blockProj blk i s t = if s = t then (if blk s = i then 1 else 0) else 0 := by
  simp [blockProj, diagonal_apply]

omit [Fintype S] [DecidableEq S] [DecidableEq I] in
theorem inBlock_blockDiag {i : I} {X : Matrix S S ℂ} (hX : InBlock blk i X) : BlockDiag blk X := by
  intro s t hst
  apply hX
  rintro ⟨h1, h2⟩
  exact hst (h1.trans h2.symm)

omit [Fintype S] [DecidableEq S] in
theorem blockPart_inBlock (i : I) (X : Matrix S S ℂ) : InBlock blk i (blockPart blk i X) := by
  intro s t h
  simp [blockPart_apply, h]

omit [Fintype S] [DecidableEq S] in
theorem blockPart_eq_of_inBlock {i : I} {X : Matrix S S ℂ} (hX : InBlock blk i X) :
    blockPart blk i X = X := by
  ext s t
  by_cases h : blk s = i ∧ blk t = i
  · simp [blockPart_apply, h]
  · rw [blockPart_apply, if_neg h, hX s t h]

omit [Fintype S] in
theorem blockProj_inBlock (i : I) : InBlock blk i (blockProj blk i) := by
  intro s t h
  rw [blockProj_apply]
  by_cases hst : s = t
  · subst hst
    have : ¬ blk s = i := fun hs => h ⟨hs, hs⟩
    simp [this]
  · simp [hst]

omit [Fintype S] in
theorem blockProj_blockDiag (i : I) : BlockDiag blk (blockProj blk i) :=
  inBlock_blockDiag blk (blockProj_inBlock blk i)

omit [Fintype S] in
theorem blockProj_posSemidef (i : I) : (blockProj blk i).PosSemidef := by
  refine PosSemidef.diagonal fun s => ?_
  by_cases h : blk s = i <;> simp [h]

omit [Fintype S] in
theorem blockProj_diag_of_ne (i : I) (t : S) (ht : blk t ≠ i) : blockProj blk i t t = 0 := by
  simp [blockProj_apply, ht]

omit [Fintype S] [DecidableEq S] in
/-- A block-diagonal matrix is the sum of its diagonal blocks. -/
theorem sum_blockPart [Fintype I] (X : Matrix S S ℂ) (hX : BlockDiag blk X) :
    ∑ i, blockPart blk i X = X := by
  ext s t
  rw [Matrix.sum_apply]
  simp only [blockPart_apply]
  by_cases hst : blk s = blk t
  · rw [Finset.sum_eq_single (blk s)]
    · simp [hst]
    · intro i _ hi
      have : ¬ (blk s = i ∧ blk t = i) := fun ⟨h1, _⟩ => hi h1.symm
      simp [this]
    · intro h
      exact absurd (Finset.mem_univ _) h
  · rw [hX s t hst]
    refine Finset.sum_eq_zero fun i _ => ?_
    have : ¬ (blk s = i ∧ blk t = i) := fun ⟨h1, h2⟩ => hst (h1.trans h2.symm)
    simp [this]

omit [DecidableEq S] in
/-- The trace of the `i`-th block is the block weight. -/
theorem blockPart_trace (i : I) (X : Matrix S S ℂ) :
    (blockPart blk i X).trace = ∑ s, if blk s = i then X s s else 0 := by
  simp [Matrix.trace, Matrix.diag, blockPart_apply]

/-- **A passive instrument on the algebra `⊕ᵢ M_{dᵢ}`**: finitely many completely positive maps
on the ambient matrix algebra whose nonselective channel fixes every block-diagonal matrix. -/
def IsBlockPassiveInstrument {O : Type*} [Fintype O]
    (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  (∀ a, IsCompletelyPositive (F a)) ∧ ∀ X, BlockDiag blk X → ∑ a, (F a) X = X

end Blocks

/-! ### Section B — block preservation, from the Kraus form -/

section Preservation

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {I : Type*} [DecidableEq I]
variable {O : Type*} [Fintype O] [DecidableEq O]
variable (blk : S → I)

/-- A completely positive map has a Kraus form, by the kernel's positive semidefinite
factorization of its Choi matrix. -/
theorem exists_kraus {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (hΦ : IsCompletelyPositive Φ) :
    ∃ K : S × S → Matrix S S ℂ, Φ = ∑ k, conjChannel (K k) := by
  obtain ⟨B, hB⟩ := psdFactorization_discharged (S × S) _ hΦ
  exact ⟨fun k => Matrix.of fun a s => B (s, a) k, kraus_of_choi_factor Φ B hB⟩

/-- The diagonal of `K Pᵢ K†` is the block-`i` row weight of `K`. -/
theorem conjChannel_blockProj_diag (K : Matrix S S ℂ) (i : I) (t : S) :
    conjChannel K (blockProj blk i) t t
      = ∑ s, if blk s = i then ((Complex.normSq (K t s) : ℝ) : ℂ) else 0 := by
  rw [conjChannel_apply, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [blockProj, mul_diagonal, conjTranspose_apply, Complex.star_def]
  by_cases h : blk s = i
  · simp [h, Complex.mul_conj]
  · simp [h]

/-- Nonnegative complex summands with zero sum are each zero. -/
theorem eq_zero_of_sum_eq_zero_of_nonneg {ι : Type*} (s : Finset ι) (f : ι → ℂ)
    (hf : ∀ j ∈ s, 0 ≤ f j) (h : ∑ j ∈ s, f j = 0) : ∀ j ∈ s, f j = 0 :=
  (Finset.sum_eq_zero_iff_of_nonneg hf).mp h

omit [DecidableEq O] in
/-- **Every Kraus operator of every branch vanishes between distinct blocks.** Passivity on the
block projector `Pᵢ` says the branches' images of `Pᵢ` sum to `Pᵢ`, whose diagonal vanishes off
block `i`; each image is positive semidefinite, so each has zero diagonal there; and the diagonal
of `K Pᵢ K†` at `t` is the squared norm of the block-`i` part of row `t` of `K`. -/
theorem kraus_block_vanish {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsBlockPassiveInstrument blk F) (a : O) (K : S × S → Matrix S S ℂ)
    (hK : F a = ∑ k, conjChannel (K k)) (i : I) (k : S × S) (t s : S)
    (hs : blk s = i) (ht : blk t ≠ i) : K k t s = 0 := by
  -- Step 1: the `a`-th image of `Pᵢ` has zero diagonal at `t`.
  have h1 : (F a) (blockProj blk i) t t = 0 := by
    have hsum := congrFun (congrFun (hF.2 _ (blockProj_blockDiag blk i)) t) t
    rw [Matrix.sum_apply, blockProj_diag_of_ne blk i t ht] at hsum
    exact eq_zero_of_sum_eq_zero_of_nonneg _ _
      (fun b _ => (cp_apply_posSemidef (hF.1 b) (blockProj_posSemidef blk i)).diag_nonneg)
      hsum a (Finset.mem_univ a)
  -- Step 2: each Kraus term's image of `Pᵢ` has zero diagonal at `t`.
  have h2 : conjChannel (K k) (blockProj blk i) t t = 0 := by
    rw [hK, LinearMap.sum_apply, Matrix.sum_apply] at h1
    exact eq_zero_of_sum_eq_zero_of_nonneg _ _
      (fun k' _ => ((blockProj_posSemidef blk i).mul_mul_conjTranspose_same (K k')).diag_nonneg)
      h1 k (Finset.mem_univ k)
  -- Step 3: the block-`i` row weight vanishes termwise.
  rw [conjChannel_blockProj_diag] at h2
  have h3 := eq_zero_of_sum_eq_zero_of_nonneg _ _
    (fun s' _ => by
      by_cases h : blk s' = i
      · simp only [h, if_true]
        exact Complex.zero_le_real.mpr (Complex.normSq_nonneg _)
      · simp [h])
    h2 s (Finset.mem_univ s)
  rw [if_pos hs] at h3
  exact Complex.normSq_eq_zero.mp (by exact_mod_cast h3)

/-- A conjugation whose operator vanishes between blocks preserves block `i`. -/
theorem conjChannel_inBlock (K : Matrix S S ℂ) (i : I)
    (hK : ∀ t s, blk s = i → blk t ≠ i → K t s = 0)
    (X : Matrix S S ℂ) (hX : InBlock blk i X) : InBlock blk i (conjChannel K X) := by
  intro t u htu
  rw [conjChannel_apply, Matrix.mul_apply]
  refine Finset.sum_eq_zero fun s' _ => ?_
  rw [Matrix.mul_apply, conjTranspose_apply, Finset.sum_mul]
  refine Finset.sum_eq_zero fun s _ => ?_
  by_cases hs : blk s = i ∧ blk s' = i
  · rcases not_and_or.mp htu with ht | hu
    · rw [hK t s hs.1 ht]; ring
    · rw [hK u s' hs.2 hu, star_zero]; ring
  · rw [hX s s' hs]; ring

omit [Fintype S] [DecidableEq S] [DecidableEq I] in
theorem inBlock_sum {ι : Type*} (s : Finset ι) (i : I) (M : ι → Matrix S S ℂ)
    (h : ∀ j ∈ s, InBlock blk i (M j)) : InBlock blk i (∑ j ∈ s, M j) := by
  intro t u htu
  rw [Matrix.sum_apply]
  exact Finset.sum_eq_zero fun j hj => h j hj t u htu

omit [DecidableEq O] in
/-- **OI-N3, block preservation.** Every branch of a passive instrument on `⊕ᵢ M_{dᵢ}` sends
block `i` into block `i`. -/
theorem branch_preserves_block {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsBlockPassiveInstrument blk F) (a : O) (i : I) (X : Matrix S S ℂ)
    (hX : InBlock blk i X) : InBlock blk i ((F a) X) := by
  obtain ⟨K, hK⟩ := exists_kraus (hF.1 a)
  rw [hK, LinearMap.sum_apply]
  exact inBlock_sum blk _ i _ fun k _ =>
    conjChannel_inBlock blk (K k) i (fun t s hs ht => kraus_block_vanish blk hF a K hK i k t s hs ht)
      X hX

end Preservation

/-! ### Section C — restriction to a block, and the blockwise scalar -/

section Restriction

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {I : Type*} [DecidableEq I]
variable {O : Type*} [Fintype O] [DecidableEq O]
variable (blk : S → I) (i : I)

/-- The fibre of block `i`: the basis states it contains. -/
abbrev fib : Type _ := {s : S // blk s = i}

/-- Extension by zero from the fibre of block `i` to the ambient algebra. -/
def extendₗ : Matrix (fib blk i) (fib blk i) ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun Y := Matrix.of fun s t =>
    if h : blk s = i ∧ blk t = i then Y ⟨s, h.1⟩ ⟨t, h.2⟩ else 0
  map_add' Y Z := by
    ext s t
    by_cases h : blk s = i ∧ blk t = i
    · simp only [Matrix.of_apply, Matrix.add_apply, dif_pos h]
    · simp [h]
  map_smul' c Y := by
    ext s t
    by_cases h : blk s = i ∧ blk t = i
    · simp only [Matrix.of_apply, Matrix.smul_apply, dif_pos h, RingHom.id_apply]
    · simp [h]

/-- Restriction of an ambient matrix to the fibre of block `i`: the principal submatrix. -/
def restrictₗ : Matrix S S ℂ →ₗ[ℂ] Matrix (fib blk i) (fib blk i) ℂ where
  toFun X := X.submatrix Subtype.val Subtype.val
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

/-- A map on the ambient algebra, restricted to block `i`. -/
def restrictMap (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    Matrix (fib blk i) (fib blk i) ℂ →ₗ[ℂ] Matrix (fib blk i) (fib blk i) ℂ :=
  restrictₗ blk i ∘ₗ Φ ∘ₗ extendₗ blk i

omit [Fintype S] [DecidableEq S] in
theorem extendₗ_apply (Y : Matrix (fib blk i) (fib blk i) ℂ) (s t : S) :
    extendₗ blk i Y s t = if h : blk s = i ∧ blk t = i then Y ⟨s, h.1⟩ ⟨t, h.2⟩ else 0 := rfl

omit [Fintype S] [DecidableEq S] [DecidableEq I] in
theorem restrictₗ_apply (X : Matrix S S ℂ) (x y : fib blk i) :
    restrictₗ blk i X x y = X x.val y.val := rfl

omit [Fintype S] [DecidableEq S] in
theorem extendₗ_inBlock (Y : Matrix (fib blk i) (fib blk i) ℂ) : InBlock blk i (extendₗ blk i Y) := by
  intro s t h
  simp [extendₗ_apply, h]

omit [Fintype S] [DecidableEq S] in
theorem restrict_extend (Y : Matrix (fib blk i) (fib blk i) ℂ) :
    restrictₗ blk i (extendₗ blk i Y) = Y := by
  ext x y
  obtain ⟨s, hs⟩ := x
  obtain ⟨t, ht⟩ := y
  rw [restrictₗ_apply, extendₗ_apply, dif_pos ⟨hs, ht⟩]

omit [Fintype S] [DecidableEq S] in
theorem extend_restrict_of_inBlock {X : Matrix S S ℂ} (hX : InBlock blk i X) :
    extendₗ blk i (restrictₗ blk i X) = X := by
  ext s t
  by_cases h : blk s = i ∧ blk t = i
  · rw [extendₗ_apply, dif_pos h]
    rfl
  · rw [extendₗ_apply, dif_neg h, hX s t h]

omit [Fintype S] in
/-- Extension carries matrix units of the fibre to matrix units of the ambient algebra. -/
theorem extend_single (x y : fib blk i) :
    extendₗ blk i (Matrix.single x y (1 : ℂ)) = Matrix.single x.val y.val 1 := by
  ext s t
  rw [extendₗ_apply]
  by_cases h : blk s = i ∧ blk t = i
  · rw [dif_pos h]
    simp only [Matrix.single, Matrix.of_apply]
    simp [Subtype.ext_iff]
  · rw [dif_neg h]
    have : ¬ (x.val = s ∧ y.val = t) := by
      rintro ⟨rfl, rfl⟩
      exact h ⟨x.property, y.property⟩
    simp [Matrix.single, this]

/-- The reindexing of `S × S` by the fibre. -/
def fibPair : fib blk i × fib blk i → S × S := fun p => (p.1.val, p.2.val)

omit [Fintype S] in
/-- **The Choi matrix of a restricted map is a principal submatrix** of the original Choi
matrix. -/
theorem choiMatrix_restrictMap (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    choiMatrix (restrictMap blk i Φ) = (choiMatrix Φ).submatrix (fibPair blk i) (fibPair blk i) := by
  ext p q
  show restrictMap blk i Φ (Matrix.single p.1 q.1 1) p.2 q.2 = _
  simp only [restrictMap, LinearMap.comp_apply, restrictₗ_apply, extend_single, submatrix_apply,
    fibPair, choiMatrix, Matrix.of_apply]

omit [Fintype S] in
/-- Restriction to a block preserves complete positivity. -/
theorem restrictMap_cp {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (hΦ : IsCompletelyPositive Φ) :
    IsCompletelyPositive (restrictMap blk i Φ) := by
  show (choiMatrix _).PosSemidef
  rw [choiMatrix_restrictMap]
  exact hΦ.submatrix _

omit [Fintype S] [DecidableEq O] in
/-- **The restriction of a passive instrument to a block is a passive instrument on the block**,
in the sense of N1. -/
theorem restricted_passive {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsBlockPassiveInstrument blk F) :
    IsPassiveInstrument fun a => restrictMap blk i (F a) := by
  refine ⟨fun a => restrictMap_cp blk i (hF.1 a), ?_⟩
  apply LinearMap.ext
  intro Y
  rw [LinearMap.sum_apply, LinearMap.id_apply]
  simp only [restrictMap, LinearMap.comp_apply]
  rw [← map_sum, hF.2 _ (inBlock_blockDiag blk (extendₗ_inBlock blk i Y)), restrict_extend]

/-- **OI-N3, blockwise scalars.** On block `i` every branch of a passive instrument is a scalar:
N1 on the fibre, transported back through the block. -/
theorem branch_scalar_on_block {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsBlockPassiveInstrument blk F) (a : O) :
    ∃ c : ℂ, ∀ X, InBlock blk i X → (F a) X = c • X := by
  obtain ⟨c, hc⟩ := passive_branch_scalar (restricted_passive blk i hF) a
  refine ⟨c, fun X hX => ?_⟩
  have h1 : restrictMap blk i (F a) (restrictₗ blk i X) = c • restrictₗ blk i X := by
    rw [hc, LinearMap.smul_apply, LinearMap.id_apply]
  simp only [restrictMap, LinearMap.comp_apply, extend_restrict_of_inBlock blk i hX] at h1
  calc (F a) X = extendₗ blk i (restrictₗ blk i ((F a) X)) :=
        (extend_restrict_of_inBlock blk i (branch_preserves_block blk hF a i X hX)).symm
    _ = extendₗ blk i (c • restrictₗ blk i X) := by rw [h1]
    _ = c • X := by rw [map_smul, extend_restrict_of_inBlock blk i hX]

end Restriction

/-! ### Section D — OI-N3: the classification -/

section Classification

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {I : Type*} [DecidableEq I]
variable {O : Type*} [Fintype O] [DecidableEq O]
variable (blk : S → I)

omit [DecidableEq I] in
theorem pureState_inBlock (s : S) : InBlock blk (blk s) (pureState s) := by
  intro t u h
  rw [pureState_apply]
  have : ¬ (t = s ∧ u = s) := by
    rintro ⟨rfl, rfl⟩
    exact h ⟨rfl, rfl⟩
  rcases not_and_or.mp this with ht | hu
  · simp [ht]
  · simp [hu]

/-- **OI-N3, the classification.** Every passive instrument on `⊕ᵢ M_{dᵢ}` induces a classical
stochastic observation of the center: there is a matrix `c` with `c a i ≥ 0` (from complete
positivity) and `∑ₐ c a i = 1` (from passivity) on every nonempty block, such that the outcome law
on any block-diagonal state is `tr (F a ρ) = ∑ᵢ c a i · tr (Pᵢ ρ Pᵢ)`. Nothing inside a block is
read. One direction only: no converse constructing an instrument from a stochastic matrix is
stated. -/
theorem central_classification [Fintype I] {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsBlockPassiveInstrument blk F) :
    ∃ c : O → I → ℂ,
      (∀ a (ρ : Matrix S S ℂ), BlockDiag blk ρ →
        ((F a) ρ).trace = ∑ i, c a i * (blockPart blk i ρ).trace) ∧
      (∀ a i, (∃ s, blk s = i) → 0 ≤ c a i) ∧
      (∀ i, (∃ s, blk s = i) → ∑ a, c a i = 1) := by
  classical
  choose c hc using fun a i => branch_scalar_on_block blk i hF a
  refine ⟨c, ?_, ?_, ?_⟩
  · intro a ρ hρ
    conv_lhs => rw [← sum_blockPart blk ρ hρ, map_sum, trace_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [hc a i _ (blockPart_inBlock blk i ρ), trace_smul, smul_eq_mul]
  · rintro a i ⟨s, rfl⟩
    have hpsd := cp_apply_posSemidef (hF.1 a) (pure_posSemidef s)
    have hdiag := hpsd.diag_nonneg (i := s)
    rw [hc a (blk s) _ (pureState_inBlock blk s), Matrix.smul_apply, pureState_apply] at hdiag
    simpa using hdiag
  · rintro i ⟨s, rfl⟩
    have hsum := congrFun (congrFun (hF.2 _ (inBlock_blockDiag blk (pureState_inBlock blk s))) s) s
    rw [Matrix.sum_apply] at hsum
    have hp : pureState s s s = 1 := by simp [pureState_apply]
    simp only [hc _ (blk s) _ (pureState_inBlock blk s), Matrix.smul_apply, hp, smul_eq_mul,
      mul_one] at hsum
    exact hsum

end Classification

/-! ### Section E — the control: reading the center, and nothing else -/

section Control

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {I : Type*} [DecidableEq I]
variable (blk : S → I)

/-- The branch that keeps block `i` and discards every other block: `X ↦ Pᵢ X Pᵢ`. -/
def blockPinch (i : I) : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ :=
  conjChannel (blockProj blk i)

theorem blockPinch_cp (i : I) : IsCompletelyPositive (blockPinch blk i) := by
  show (choiMatrix (conjChannel _)).PosSemidef
  rw [choiMatrix_conjChannel]
  exact posSemidef_vecMulVec_self_star _

theorem blockPinch_apply (i : I) (X : Matrix S S ℂ) : blockPinch blk i X = blockPart blk i X := by
  ext s t
  simp only [blockPinch, conjChannel_apply, blockProj, blockPart_apply]
  rw [diagonal_conjTranspose, mul_diagonal, diagonal_mul]
  by_cases hs : blk s = i <;> by_cases ht : blk t = i <;> simp [hs, ht]

/-- **The control is passive on the algebra.** -/
theorem blockPinch_passive [Fintype I] : IsBlockPassiveInstrument blk (blockPinch blk) := by
  refine ⟨blockPinch_cp blk, fun X hX => ?_⟩
  simp only [blockPinch_apply]
  exact sum_blockPart blk X hX

/-- **The control reads the block weights.** -/
theorem blockPinch_trace (i : I) (X : Matrix S S ℂ) :
    (blockPinch blk i X).trace = ∑ s, if blk s = i then X s s else 0 := by
  rw [blockPinch_apply, blockPart_trace]

end Control

/-! ### Section F — the boundary: complete passive observation iff commutative -/

section Boundary

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {I : Type*} [DecidableEq I]
variable {O : Type*} [Fintype O] [DecidableEq O]
variable (blk : S → I)

/-- **State-separating on the algebra**: distinct block-diagonal density matrices produce distinct
outcome laws. -/
def SeparatesBlockStates (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ ρ σ : Matrix S S ℂ, ρ.PosSemidef → σ.PosSemidef → ρ.trace = 1 → σ.trace = 1 →
    BlockDiag blk ρ → BlockDiag blk σ →
    (∀ a, ((F a) ρ).trace = ((F a) σ).trace) → ρ = σ

/-- **OI-N3, the obstruction.** A block with two basis states carries two pure states that every
passive instrument confuses. -/
theorem no_complete_passive_of_block {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hF : IsBlockPassiveInstrument blk F) (s t : S) (hst : s ≠ t) (hb : blk s = blk t) :
    ¬ SeparatesBlockStates blk F := by
  intro hsep
  apply pure_ne s t hst
  apply hsep _ _ (pure_posSemidef s) (pure_posSemidef t) (pure_trace s) (pure_trace t)
    (inBlock_blockDiag blk (pureState_inBlock blk s))
    (inBlock_blockDiag blk (pureState_inBlock blk t))
  intro a
  obtain ⟨c, hc⟩ := branch_scalar_on_block blk (blk s) hF a
  have ht : InBlock blk (blk s) (pureState t) := hb ▸ pureState_inBlock blk t
  rw [hc _ (pureState_inBlock blk s), hc _ ht, trace_smul, trace_smul, pure_trace, pure_trace]

omit [Fintype S] [DecidableEq S] [DecidableEq I] in
/-- When the blocks are singletons, block-diagonal is diagonal. -/
theorem blockDiag_isDiagonal (hinj : Function.Injective blk) {X : Matrix S S ℂ}
    (hX : BlockDiag blk X) : IsDiagonal X :=
  fun s t hst => hX s t fun h => hst (hinj h)

/-- **OI-N3, the commutative side.** When every block is a singleton the control separates
states: it reads the diagonal. -/
theorem blockPinch_separates (hinj : Function.Injective blk) :
    SeparatesBlockStates blk (blockPinch blk) := by
  intro ρ σ _ _ _ _ hρ hσ h
  have key : ∀ (X : Matrix S S ℂ) (s : S), (blockPinch blk (blk s) X).trace = X s s := by
    intro X s
    rw [blockPinch_trace, Finset.sum_eq_single s]
    · simp
    · intro t _ hts
      have : blk t ≠ blk s := fun h => hts (hinj h)
      simp [this]
    · intro h
      exact absurd (Finset.mem_univ _) h
  ext s t
  by_cases hst : s = t
  · subst hst
    have := h (blk s)
    rwa [key, key] at this
  · rw [blockDiag_isDiagonal blk hinj hρ s t hst, blockDiag_isDiagonal blk hinj hσ s t hst]

end Boundary

section Iff

variable {S : Type} [Fintype S] [DecidableEq S]
variable {I : Type} [Fintype I] [DecidableEq I]
variable (blk : S → I)

/-- **OI-N3, the boundary.** Some passive instrument observes the algebra `⊕ᵢ M_{dᵢ}` completely
if and only if each block contains at most one basis state, i.e. the labelling is injective:
every nonempty block has dimension one, and empty labels are allowed. -/
theorem complete_passive_iff_injective :
    (∃ (O : Type) (_ : Fintype O) (_ : DecidableEq O) (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ),
      IsBlockPassiveInstrument blk F ∧ SeparatesBlockStates blk F) ↔ Function.Injective blk := by
  constructor
  · rintro ⟨O, _, _, F, hF, hsep⟩ s t hb
    by_contra hst
    exact no_complete_passive_of_block blk hF s t hst hb hsep
  · intro hinj
    exact ⟨I, inferInstance, inferInstance, blockPinch blk, blockPinch_passive blk,
      blockPinch_separates blk hinj⟩

omit [Fintype I] [DecidableEq I] in
/-- **Singleton blocks are exactly commutativity** of the block-diagonal algebra. -/
theorem injective_iff_commutative :
    Function.Injective blk ↔
      ∀ X Y : Matrix S S ℂ, BlockDiag blk X → BlockDiag blk Y → X * Y = Y * X := by
  constructor
  · intro hinj X Y hX hY
    have dX : X = Matrix.diagonal fun s => X s s := by
      ext s t
      by_cases hst : s = t
      · subst hst; simp
      · rw [blockDiag_isDiagonal blk hinj hX s t hst, diagonal_apply_ne _ hst]
    have dY : Y = Matrix.diagonal fun s => Y s s := by
      ext s t
      by_cases hst : s = t
      · subst hst; simp
      · rw [blockDiag_isDiagonal blk hinj hY s t hst, diagonal_apply_ne _ hst]
    rw [dX, dY, diagonal_mul_diagonal, diagonal_mul_diagonal]
    congr 1
    funext s
    ring
  · intro hcomm s t hb
    by_contra hst
    have hX : BlockDiag blk (Matrix.single s t (1 : ℂ)) := by
      intro u v huv
      have : ¬ (s = u ∧ t = v) := by
        rintro ⟨rfl, rfl⟩
        exact huv hb
      simp [Matrix.single, this]
    have hY : BlockDiag blk (Matrix.single t s (1 : ℂ)) := by
      intro u v huv
      have : ¬ (t = u ∧ s = v) := by
        rintro ⟨rfl, rfl⟩
        exact huv hb.symm
      simp [Matrix.single, this]
    have h := congrFun (congrFun (hcomm _ _ hX hY) s) s
    rw [single_mul_single_same, single_mul_single_same] at h
    simp [Matrix.single] at h
    exact hst h.symm

/-- **OI-N3.** Complete passive observation of the algebra `⊕ᵢ M_{dᵢ}` is possible if and only
if the algebra is commutative. -/
theorem complete_passive_iff_commutative :
    (∃ (O : Type) (_ : Fintype O) (_ : DecidableEq O) (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ),
      IsBlockPassiveInstrument blk F ∧ SeparatesBlockStates blk F) ↔
      ∀ X Y : Matrix S S ℂ, BlockDiag blk X → BlockDiag blk Y → X * Y = Y * X :=
  (complete_passive_iff_injective blk).trans (injective_iff_commutative blk)

end Iff

#print axioms exists_kraus
#print axioms kraus_block_vanish
#print axioms branch_preserves_block
#print axioms choiMatrix_restrictMap
#print axioms restricted_passive
#print axioms branch_scalar_on_block
#print axioms central_classification
#print axioms blockPinch_passive
#print axioms no_complete_passive_of_block
#print axioms blockPinch_separates
#print axioms complete_passive_iff_injective
#print axioms injective_iff_commutative
#print axioms complete_passive_iff_commutative

end CentralObservation
end OIBridge
