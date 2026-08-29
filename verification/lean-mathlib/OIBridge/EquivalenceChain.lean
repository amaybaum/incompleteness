/-
  OIBridge/EquivalenceChain.lean — b447's first closure wave on the central chain.

  Four statements from `papers/Main.md` §2.3, §3.1 and §3.2, formalized as the manuscript states
  them rather than as representative instances. They are ranks 1-4 of the kernel backlog in
  `verification/coverage/LEDGER.json`, taken in order, and together they are the computational
  core of the central equivalence chain.

  THE STOCHASTIC-INVERSE LEMMA (Main §2.3):

      If a finite square stochastic matrix has a stochastic left or right inverse,
      then it is a permutation matrix.

  It is the step that turns "the marginal process is not a permutation" into "the process is
  P-indivisible", so the whole indivisibility argument rests on it. The proof below is the
  manuscript's own, step for step: the vanishing off-diagonal entries of `A * B` force every row of
  `B` indexed by the support of a row of `A` to be a basis vector; two such rows would coincide,
  which a nonzero determinant forbids; so each row of `A` carries a single unit entry, and the
  occupied columns are distinct.

  PERMUTATION UNITARITY (Main §3.2):

      Any bijection φ : C_V × C_H → C_V × C_H defines a unitary U_φ on H = H_V ⊗ H_H.

  Stated over the index type `V × H`, which is what "on the tensor product" means once the bases
  are fixed — the manuscript's own reading, since its proof is that `U_φ` permutes the product
  orthonormal basis.

  DIAGONAL PRESERVATION (Main §3.2):

      The channels Φ_t(ρ) = Tr_H[U^t (ρ ⊗ μ_H) U^{-t}] with U a permutation unitary map
      computational-diagonal states to computational-diagonal states.

  Derived from permutation unitarity rather than recomputed. The hidden prior enters as a STATE
  built from a distribution — which is what `μ_H` is in the framework, §3.4 writing it out as
  `ρ_anc = Σ_h μ_H(h)|h⟩⟨h|` — so its diagonality is definitional and no hypothesis is smuggled in.

  THE ONE-STEP ANCILLA DILATION (Main §3.1):

      For any stochastic T on n states, W|i⟩ = Σ_j √(T_ij) |j⟩ ⊗ |i⟩ is an isometry
      ℂⁿ → ℂⁿ ⊗ ℂⁿ whose ancilla-marginal is T, and it extends to a unitary on ℂⁿ ⊗ ℂⁿ.

  All three clauses are proved. The third is where Mathlib earns its place rather than being
  incidental: extending an isometry to a unitary is orthonormal-basis extension, a real theorem
  and not bookkeeping.

  ALL FOUR ARE `K3` IN THE LEDGER'S SENSE: the exact manuscript statement, no weakening, no
  representative instance, and no premise imported beyond finiteness. The companion probes stay:
  `equivalence_recovery_probes.py`, `sdq_probes.py` and `tdilate_probes.py` remain independent
  executable evidence, and PROBED IS NOT FORMALLY PROVED runs in both directions — neither layer
  replaces the other.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.LinearAlgebra.Matrix.Stochastic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.Analysis.InnerProductSpace.PiL2

namespace OIBridge

namespace EquivalenceChain

open Matrix Finset

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The manuscript's first step. If `A * B = 1` and both are row-stochastic, then every row of `B`
whose index carries positive weight in row `i` of `A` is the `i`-th basis vector.

The argument is entirely about signs: an off-diagonal entry of `A * B` is a sum of nonnegative
terms equal to zero, so every term vanishes, so `B k j = 0` wherever `A i k` does not; the row sum
of `B` then has nowhere to live but the `i`-th column. -/
theorem row_eq_basis_of_mem_support {A B : Matrix n n ℝ}
    (hA : ∀ i j, 0 ≤ A i j) (hB : ∀ i j, 0 ≤ B i j) (hBrow : ∀ k, ∑ j, B k j = 1)
    (h : A * B = 1) {i k : n} (hik : 0 < A i k) :
    ∀ j, B k j = if j = i then 1 else 0 := by
  have hzero : ∀ j, j ≠ i → B k j = 0 := by
    intro j hji
    have hsum : ∑ m, A i m * B m j = 0 := by
      have hij := congrFun (congrFun h i) j
      rw [Matrix.mul_apply] at hij
      rw [hij]
      exact Matrix.one_apply_ne (Ne.symm hji)
    have hterm : ∀ m ∈ (univ : Finset n), A i m * B m j = 0 :=
      (Finset.sum_eq_zero_iff_of_nonneg
        (fun m _ => mul_nonneg (hA i m) (hB m j))).1 hsum
    rcases mul_eq_zero.1 (hterm k (mem_univ k)) with hc | hc
    · exact absurd hc (ne_of_gt hik)
    · exact hc
  have hi : B k i = 1 := by
    have := hBrow k
    rw [Finset.sum_eq_single i (fun j _ hji => hzero j hji) (fun hj => absurd (mem_univ i) hj)]
      at this
    exact this
  intro j
  by_cases hj : j = i
  · subst hj; simpa using hi
  · simpa [hj] using hzero j hj

/-- **Lemma (stochastic inverse), Main §2.3.**

*If a finite square stochastic matrix has a stochastic left or right inverse, then it is a
permutation matrix.*

The two sides are not proved separately: over a commutative ring a one-sided inverse of a square
matrix is two-sided, so the left-inverse case is the right-inverse case with the factors named the
other way round — which is exactly the manuscript's "the right-inverse case is symmetric". -/
theorem isPermMatrix_of_stochastic_inverse {A B : Matrix n n ℝ}
    (hA : A ∈ rowStochastic ℝ n) (hB : B ∈ rowStochastic ℝ n)
    (h : A * B = 1 ∨ B * A = 1) :
    ∃ σ : Equiv.Perm n, A = σ.permMatrix ℝ := by
  have hab : A * B = 1 := h.elim id (fun hba => _root_.mul_eq_one_comm.mpr hba)
  have hAnn : ∀ i j, 0 ≤ A i j := (mem_rowStochastic_iff_sum.1 hA).1
  have hBnn : ∀ i j, 0 ≤ B i j := (mem_rowStochastic_iff_sum.1 hB).1
  have hArow : ∀ i, ∑ j, A i j = 1 := (mem_rowStochastic_iff_sum.1 hA).2
  have hBrow : ∀ k, ∑ j, B k j = 1 := (mem_rowStochastic_iff_sum.1 hB).2
  -- `B` is invertible, so it has no repeated row.
  have hdetB : B.det ≠ 0 := by
    intro hd
    have h01 : (0 : ℝ) = 1 := by
      have hdm := congrArg Matrix.det hab
      rwa [Matrix.det_mul, hd, mul_zero, Matrix.det_one] at hdm
    exact zero_ne_one h01
  -- Every row of `A` has a positive entry, because it sums to one.
  have hexists : ∀ i, ∃ k, 0 < A i k := by
    intro i
    by_contra hcon
    have hall : ∀ k, A i k = 0 := fun k => by
      by_contra hk
      exact hcon ⟨k, lt_of_le_of_ne (hAnn i k) (Ne.symm hk)⟩
    have hz : ∑ j, A i j = 0 := Finset.sum_eq_zero fun j _ => hall j
    rw [hArow i] at hz
    exact one_ne_zero hz
  -- and at most one, since two would repeat a row of `B`.
  have hunique : ∀ i k k', 0 < A i k → 0 < A i k' → k = k' := by
    intro i k k' hk hk'
    by_contra hne
    exact hdetB (Matrix.det_zero_of_row_eq hne
      (funext fun j => by
        rw [row_eq_basis_of_mem_support hAnn hBnn hBrow hab hk j,
            row_eq_basis_of_mem_support hAnn hBnn hBrow hab hk' j]))
  choose f hf using hexists
  -- Distinct rows of `A` occupy distinct columns: row `f i` of `B` is the `i`-th basis vector.
  have hinj : Function.Injective f := by
    intro i i' hii
    by_contra hne
    have h1 : B (f i) i = 1 := by
      simpa using row_eq_basis_of_mem_support hAnn hBnn hBrow hab (hf i) i
    have h0 : B (f i') i = 0 := by
      simpa [hne] using row_eq_basis_of_mem_support hAnn hBnn hBrow hab (hf i') i
    rw [hii] at h1
    exact one_ne_zero (h1.symm.trans h0)
  -- Off the occupied column every entry is zero, so the occupied one is the whole row sum.
  have hoff : ∀ i j, j ≠ f i → A i j = 0 := fun i j hj =>
    le_antisymm (not_lt.1 fun hpos => hj (hunique i j (f i) hpos (hf i))) (hAnn i j)
  have hon : ∀ i, A i (f i) = 1 := by
    intro i
    have := hArow i
    rwa [Finset.sum_eq_single (f i) (fun j _ hj => hoff i j hj)
      (fun hj => absurd (mem_univ (f i)) hj)] at this
  refine ⟨Equiv.ofBijective f (Finite.injective_iff_bijective.1 hinj), ?_⟩
  ext i j
  by_cases hj : j = f i
  · subst hj
    simp [Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply, hon i]
  · simp [Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply,
      hoff i j hj, Ne.symm hj]

/-- **Lemma (permutation unitarity), Main §3.2.**

*Any bijection `φ : C_V × C_H → C_V × C_H` defines a unitary `U_φ` on `H = H_V ⊗ H_H`.*

The index type is the product, which is what "on the tensor product" says once the product basis
is fixed; the manuscript's proof is that `U_φ` permutes that orthonormal basis, and permuting an
orthonormal basis is precisely the statement below. Nothing about the two factors is used, so the
lemma is stated for the product and holds for any finite index type. -/
theorem permMatrix_mem_unitaryGroup {V H : Type*} [Fintype V] [DecidableEq V]
    [Fintype H] [DecidableEq H] (φ : Equiv.Perm (V × H)) :
    φ.permMatrix ℂ ∈ Matrix.unitaryGroup (V × H) ℂ := by
  rw [Matrix.mem_unitaryGroup_iff]
  show φ.permMatrix ℂ * (φ.permMatrix ℂ)ᴴ = 1
  rw [Matrix.conjTranspose_permMatrix, ← Matrix.permMatrix_mul, inv_mul_cancel,
    Matrix.permMatrix_one]

/-! ## Diagonal preservation (Main §3.2)

Rank 3 of the coverage backlog, and it is DERIVED from permutation unitarity above rather than
recomputed: the only new mathematical content is that conjugating by a permutation matrix is a
RELABELLING of indices, after which diagonality survives because a permutation is injective. -/

section DiagonalPreservation

variable {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]

/-- Computational-diagonal: zero off the diagonal. -/
def IsDiag {α : Type*} (M : Matrix α α ℂ) : Prop := ∀ i j, i ≠ j → M i j = 0

/-- The partial trace over the hidden factor, `Tr_H`. -/
def ptraceH (M : Matrix (V × H) (V × H) ℂ) : Matrix V V ℂ :=
  fun i j => ∑ h : H, M (i, h) (j, h)

/-- `ρ ⊗ σ` on the product index type, which is what the product basis makes of a tensor product. -/
def tensorH (ρ : Matrix V V ℂ) (σ : Matrix H H ℂ) : Matrix (V × H) (V × H) ℂ :=
  fun p q => ρ p.1 q.1 * σ p.2 q.2

/-- A hidden prior AS A STATE. This is what `μ_H` is in the framework — Main §3.4's fixed-`Ĥ`
lemma writes it out as `ρ_anc = Σ_h μ_H(h) |h⟩⟨h|` — so its diagonality is DEFINITIONAL and not an
extra hypothesis smuggled into the statement. -/
def priorState (μ : H → ℂ) : Matrix H H ℂ := Matrix.diagonal μ

/-- Powers of a permutation matrix are the permutation matrices of the powers, so writing the
channel with `(φ ^ t).permMatrix` really is writing it with `U ^ t`. -/
theorem permMatrix_pow {α : Type*} [Fintype α] [DecidableEq α] (ψ : Equiv.Perm α) (t : ℕ) :
    (ψ ^ t).permMatrix ℂ = (ψ.permMatrix ℂ) ^ t := by
  induction t with
  | zero => simp
  | succ k ih =>
      rw [pow_succ, pow_succ, ← ih, ← Matrix.permMatrix_mul, ← pow_succ, ← pow_succ']

/-- `U⁻¹` really is the inverse, and this is exactly rank 2: unitarity gives `star U = U⁻¹`, and
`star` of a permutation matrix is the permutation matrix of the inverse. -/
theorem permMatrix_mul_inv {α : Type*} [Fintype α] [DecidableEq α] (ψ : Equiv.Perm α) :
    ψ.permMatrix ℂ * (ψ⁻¹).permMatrix ℂ = 1 ∧
    (ψ⁻¹).permMatrix ℂ * ψ.permMatrix ℂ = 1 := by
  constructor
  · rw [← Matrix.permMatrix_mul, inv_mul_cancel, Matrix.permMatrix_one]
  · rw [← Matrix.permMatrix_mul, mul_inv_cancel, Matrix.permMatrix_one]

/-- **Conjugation by a permutation unitary is a relabelling.** The whole of diagonal preservation
follows from this one identity. -/
theorem permConj_apply {α : Type*} [Fintype α] [DecidableEq α] (ψ : Equiv.Perm α)
    (M : Matrix α α ℂ) (p q : α) :
    (ψ.permMatrix ℂ * M * (ψ⁻¹).permMatrix ℂ) p q = M (ψ p) (ψ q) := by
  rw [Equiv.Perm.permMatrix, Equiv.Perm.permMatrix, PEquiv.toMatrix_toPEquiv_mul,
    PEquiv.mul_toMatrix_toPEquiv]
  simp [Matrix.submatrix_apply, Equiv.Perm.inv_def]

/-- The channel of Main §3.2: `Φ_t(ρ) = Tr_H[ U^t (ρ ⊗ μ_H) U^{-t} ]` with `U` the permutation
unitary of a bijection `φ` on `C_V × C_H`. -/
def Phi (φ : Equiv.Perm (V × H)) (μ : H → ℂ) (t : ℕ) (ρ : Matrix V V ℂ) : Matrix V V ℂ :=
  ptraceH ((φ ^ t).permMatrix ℂ * tensorH ρ (priorState μ) * ((φ ^ t)⁻¹).permMatrix ℂ)

/-- **Lemma (diagonal preservation), Main §3.2.**

*The channels `Φ_t(ρ) = Tr_H[U^t (ρ ⊗ μ_H) U^{-t}]` with `U` a permutation unitary map
computational-diagonal states to computational-diagonal states.*

The manuscript's proof, in the manuscript's two steps: a permutation unitary conjugates a diagonal
state to a diagonal state — because conjugation is a relabelling and the relabelling is injective —
and the partial trace of a diagonal state is diagonal. -/
theorem isDiag_Phi (φ : Equiv.Perm (V × H)) (μ : H → ℂ) (t : ℕ) (ρ : Matrix V V ℂ)
    (hρ : IsDiag ρ) : IsDiag (Phi φ μ t ρ) := by
  intro i j hij
  have hstep : ∀ h : H,
      ((φ ^ t).permMatrix ℂ * tensorH ρ (priorState μ) * ((φ ^ t)⁻¹).permMatrix ℂ) (i, h) (j, h)
        = 0 := by
    intro h
    rw [permConj_apply]
    -- `(i, h) ≠ (j, h)` and `φ ^ t` is injective, so the two relabelled indices differ.
    have hne : (φ ^ t) (i, h) ≠ (φ ^ t) (j, h) := by
      intro hc
      exact hij (congrArg Prod.fst ((φ ^ t).injective hc))
    -- A tensor of a diagonal state with a diagonal prior is diagonal.
    rcases Prod.ext_iff.not.1 hne with hne'
    by_cases h1 : ((φ ^ t) (i, h)).1 = ((φ ^ t) (j, h)).1
    · have h2 : ((φ ^ t) (i, h)).2 ≠ ((φ ^ t) (j, h)).2 := fun hc => hne' ⟨h1, hc⟩
      simp [tensorH, priorState, Matrix.diagonal_apply_ne _ h2]
    · simp [tensorH, hρ _ _ h1]
  simp only [Phi, ptraceH]
  exact Finset.sum_eq_zero fun h _ => hstep h

end DiagonalPreservation

/-! ## The one-step ancilla dilation (Main §3.1)

Rank 4 of the coverage backlog. Three clauses, and all three are proved: the map is an isometry,
its ancilla-marginal is `T`, and it extends to a unitary. The third is where Mathlib earns its
place rather than being incidental — extending an isometry to a unitary is orthonormal-basis
extension, which is a real theorem and not bookkeeping. -/

section AncillaDilation

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The dilation of Main §3.1: `W|i⟩ = Σ_j √(T_ij) |j⟩ ⊗ |i⟩`, written as a matrix whose rows are
indexed by the product basis `|j⟩ ⊗ |α⟩` and whose columns are indexed by `|i⟩`. -/
noncomputable def dilation (T : Matrix n n ℝ) : Matrix (n × n) n ℂ :=
  fun p i => if p.2 = i then (Real.sqrt (T i p.1) : ℂ) else 0

/-- **Clause 1: `W` is an isometry.** `⟨W i | W i'⟩ = δ_{ii'} Σ_j T_ij = δ_{ii'}`. -/
theorem dilation_isometry (T : Matrix n n ℝ) (hT : T ∈ rowStochastic ℝ n) :
    (dilation T)ᴴ * (dilation T) = 1 := by
  have hnn : ∀ i j, 0 ≤ T i j := (mem_rowStochastic_iff_sum.1 hT).1
  have hrow : ∀ i, ∑ j, T i j = 1 := (mem_rowStochastic_iff_sum.1 hT).2
  ext i i'
  rw [Matrix.mul_apply]
  by_cases h : i = i'
  · subst h
    rw [Matrix.one_apply_eq, Fintype.sum_prod_type]
    have key : ∀ j : n, ∑ α : n, (dilation T)ᴴ i (j, α) * dilation T (j, α) i
        = ((T i j : ℝ) : ℂ) := by
      intro j
      rw [Finset.sum_eq_single i]
      · simp [dilation, Matrix.conjTranspose_apply, ← Complex.ofReal_mul,
          Real.mul_self_sqrt (hnn i j)]
      · intro α _ hα
        simp [dilation, Matrix.conjTranspose_apply, hα]
      · intro hi; exact absurd (Finset.mem_univ i) hi
    rw [Finset.sum_congr rfl fun j _ => key j, ← Complex.ofReal_sum, hrow i,
      Complex.ofReal_one]
  · rw [Matrix.one_apply_ne h]
    refine Finset.sum_eq_zero fun p _ => ?_
    by_cases hp : p.2 = i
    · have hz : dilation T p i' = 0 := by
        simp only [dilation, if_neg (fun hc => h (hp.symm.trans hc))]
      rw [hz, mul_zero]
    · have hz : dilation T p i = 0 := by simp [dilation, hp]
      rw [Matrix.conjTranspose_apply, hz, star_zero, zero_mul]

/-- **Clause 2: the ancilla-marginal is `T`.** `Σ_α |⟨j, α| W |i⟩|² = T_ij`. -/
theorem dilation_marginal (T : Matrix n n ℝ) (hT : T ∈ rowStochastic ℝ n) (i j : n) :
    ∑ α : n, ‖dilation T (j, α) i‖ ^ 2 = T i j := by
  have hnn : ∀ i j, 0 ≤ T i j := (mem_rowStochastic_iff_sum.1 hT).1
  rw [Finset.sum_eq_single i]
  · simp only [dilation, if_true, Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (Real.sqrt_nonneg _)]
    exact Real.sq_sqrt (hnn i j)
  · intro α _ hα; simp [dilation, hα]
  · intro hi; exact absurd (Finset.mem_univ i) hi

/-- **Clause 3: `W` extends to a unitary on `ℂⁿ ⊗ ℂⁿ`.** An isometry onto an `n`-dimensional
subspace of an `n²`-dimensional space extends to a unitary — which in Mathlib is the extension of
an orthonormal family to an orthonormal basis. -/
theorem dilation_extends (T : Matrix n n ℝ) (hT : T ∈ rowStochastic ℝ n) :
    ∃ (U : Matrix (n × n) (n × n) ℂ) (f : n → n × n),
      Function.Injective f ∧ U ∈ Matrix.unitaryGroup (n × n) ℂ ∧
        U.submatrix id f = dilation T := by
  classical
  set E := EuclideanSpace ℂ (n × n)
  -- the columns of `W`, spread over the diagonal copies of the index set
  set v : (n × n) → E := fun p => WithLp.toLp 2 (fun q => dilation T q p.1) with hv
  set f : n → n × n := fun i => (i, i) with hf
  have hfinj : Function.Injective f := fun a b hab => (Prod.ext_iff.1 hab).1
  have hiso := dilation_isometry T hT
  -- orthonormality of the columns is exactly `Wᴴ W = 1`
  have horth : Orthonormal ℂ ((Set.range f).domRestrict v) := by
    rw [orthonormal_iff_ite]
    rintro ⟨p, hp⟩ ⟨q, hq⟩
    obtain ⟨a, rfl⟩ := hp
    obtain ⟨b, rfl⟩ := hq
    have hinner : (inner ℂ (v (f a)) (v (f b)) : ℂ)
        = ((dilation T)ᴴ * dilation T) a b := by
      rw [PiLp.inner_apply, Matrix.mul_apply]
      refine Finset.sum_congr rfl fun q _ => ?_
      simp [hv, hf, RCLike.inner_apply, Matrix.conjTranspose_apply, mul_comm]
    simp only [Set.domRestrict, hinner, hiso]
    by_cases hab : a = b
    · subst hab; simp
    · rw [Matrix.one_apply_ne hab]
      simp [hf, Subtype.ext_iff, Prod.ext_iff, hab]
  have hcard : Module.finrank ℂ E = Fintype.card (n × n) := by
    simp [E, finrank_euclideanSpace]
  obtain ⟨b, hb⟩ := horth.exists_orthonormalBasis_extension_of_card_eq hcard
  set U : Matrix (n × n) (n × n) ℂ := Matrix.of (fun p q => b q p) with hU
  refine ⟨U, f, hfinj, ?_, ?_⟩
  · -- the matrix whose columns are an orthonormal basis is unitary
    refine (Matrix.mem_unitaryGroup_iff').mpr ?_
    have hbo := b.orthonormal
    rw [orthonormal_iff_ite] at hbo
    ext p q
    have hpq := hbo p q
    rw [PiLp.inner_apply] at hpq
    rw [Matrix.mul_apply, Matrix.one_apply]
    rw [← hpq]
    refine Finset.sum_congr rfl fun r _ => ?_
    simp [hU, RCLike.inner_apply, mul_comm]
  · ext p i
    have hbi : b (i, i) = v (i, i) := hb (f i) ⟨i, rfl⟩
    simp [Matrix.submatrix_apply, hU, hf, hbi, hv]

end AncillaDilation

/-! ### What these proofs rest on

Printed at build time so the kernel's own answer, not a claim in a comment, is what the log
carries. `sorryAx` in any of these lines would mean a hole. -/

#print axioms row_eq_basis_of_mem_support
#print axioms isPermMatrix_of_stochastic_inverse
#print axioms permMatrix_mem_unitaryGroup
#print axioms permConj_apply
#print axioms isDiag_Phi
#print axioms dilation_isometry
#print axioms dilation_marginal
#print axioms dilation_extends

end EquivalenceChain

end OIBridge
