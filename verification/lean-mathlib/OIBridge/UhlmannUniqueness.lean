/-
  OIBridge/UhlmannUniqueness.lean — the finite right-unitary (Uhlmann / Schmidt) uniqueness
  theorem, kernel-internal: `A Aᴴ = B Bᴴ ⟹ B = A U` for a unitary `U` on a common finite
  environment. The remaining external boundary drops from two items to one.

  ROUND FORTY-EIGHT. `Purification.lean` (round twenty-one) proved purification existence and
  recorded purifier uniqueness — for amplitude matrices `A, B : Matrix S E ℂ` with equal
  environment `E`, `A Aᴴ = B Bᴴ` forces `B = A U` with `U` unitary — as the standard finite
  Schmidt/Uhlmann theorem, cited rather than reproved; the round-35 and round-45 boundary
  audits carried it as an unresolved external item. This file proves it, with the isometry
  machinery of round forty-five, in the six steps the owner laid out:

      1. Rows as vectors: `a_s = A s ·`, `b_s = B s ·` in the Euclidean space on `E`; the Gram
         identity `A Aᴴ = B Bᴴ` says `⟪a_s, a_t⟫ = ⟪b_s, b_t⟫` (`inner_rowVec`), hence every
         pair of linear combinations has the same inner product under `a ↦ b`
         (`inner_comb`, the Gram transfer).
      2. Choose an orthonormal basis `u` of the span of the `a_s` (Mathlib's
         `stdOrthonormalBasis`) and write each `u i` as a combination of the `a_s`.
      3. Transport: `v i` is the same combination of the `b_s`; by Gram transfer `v` is
         orthonormal (`transported_orthonormal`).
      4. The partial isometry `L : span a → E`, `L x = Σ_i ⟪u i, x⟫ v i`, preserves inner
         products (`partialIso_inner`) and sends `a_s ↦ b_s` (`partialIso_rowVec`, by Gram
         transfer: the defect `b_s − L a_s` has the same norm as `a_s − Σ ⟪u i, a_s⟫ u i = 0`).
      5. Extend `L` to a full isometry of `E` (Mathlib's `LinearIsometry.extend`).
      6. Read off the matrix `W` of the extension; `Wᴴ W = 1` entrywise from inner-product
         preservation, `W Wᴴ = 1` by the square-matrix inverse, and `U = Wᵀ` gives
         `B = A U` entrywise (`rightUnitary_of_gram`).

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `rightUnitary_of_gram (A B : Matrix S E ℂ) : A * Aᴴ = B * Bᴴ →                 │
      │      ∃ U : Matrix E E ℂ, Uᴴ * U = 1 ∧ B = A * U`.                              │
      │  `purifier_uniqueness`: two purifications on `S × E` of the same state are      │
      │      related by `1 ⊗ Uᵀ`, `U` unitary on the environment.                       │
      │  `boundary_one_item`: the three discharged items in one statement.              │
      └──────────────────────────────────────────────────────────────────────────────┘

  THE BOUNDARY AUDIT, UPDATED (superseding the round-45 two-item statement in
  `IsometryExtension.lean`, preserved and labelled). THE CURRENT UNRESOLVED EXTERNAL
  BOUNDARY: ONE ITEM — compact Lie integration / reachability (the analytic closed-subgroup
  step that `ControlLie.lean` records and does not claim). DISCHARGED INTERNALLY: PSD
  square-root / factorization (round thirty-four); finite isometry extension (round
  forty-five); finite right-unitary uniqueness (this round). The one remaining item is not a
  dependency of the OI → finite-QM characterization.

  WHAT IS AND IS NOT CLAIMED. Proved: the equal-environment theorem exactly as the corpus
  records it, with the usual axiom footprint. NOT claimed: the unequal-environment form
  (`B = A V` with `V` an isometry between environments of different dimension), which nothing
  in the development consumes; anything about compact Lie reachability. No structure field
  is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.GeneralCarrier

namespace OIBridge
namespace UhlmannUniqueness

open Complex Matrix Purification BoundaryAudit IsometryExtension RankGapTheory
open scoped ComplexOrder Kronecker

section Rows

variable {S E : Type} [Fintype S] [DecidableEq S] [Fintype E] [DecidableEq E]

/-- The `s`-th row of `A` as a vector of the Euclidean space on `E`. -/
noncomputable def rowVec (A : Matrix S E ℂ) (s : S) : EuclideanSpace ℂ E :=
  WithLp.toLp 2 (fun e => A s e)

omit [Fintype S] [DecidableEq S] [DecidableEq E] in
/-- **STEP 1 — GRAM**: the inner product of two rows is the Gram entry. -/
theorem inner_rowVec (A : Matrix S E ℂ) (s t : S) :
    inner ℂ (rowVec A s) (rowVec A t) = (A * Aᴴ) t s := by
  rw [EuclideanSpace.inner_eq_star_dotProduct, Matrix.mul_apply, dotProduct]
  simp only [rowVec, WithLp.ofLp_toLp, Matrix.conjTranspose_apply, Pi.star_apply]

omit [DecidableEq S] [DecidableEq E] in
/-- **GRAM TRANSFER**: under `A Aᴴ = B Bᴴ`, every pair of linear combinations of the rows
has the same inner product for `A` and for `B`. -/
theorem inner_comb {A B : Matrix S E ℂ} (hG : A * Aᴴ = B * Bᴴ) (c d : S → ℂ) :
    inner ℂ (∑ s, c s • rowVec B s) (∑ t, d t • rowVec B t)
      = inner ℂ (∑ s, c s • rowVec A s) (∑ t, d t • rowVec A t) := by
  simp only [sum_inner, inner_sum, inner_smul_left, inner_smul_right, inner_rowVec, hG]

omit [DecidableEq S] [DecidableEq E] in
/-- A vanishing Gram norm on the `A`-side forces the `B`-side combination to vanish. -/
theorem comb_eq_zero_of_transfer {A B : Matrix S E ℂ} (hG : A * Aᴴ = B * Bᴴ) (d : S → ℂ)
    (h : ∑ t, d t • rowVec A t = 0) : ∑ t, d t • rowVec B t = 0 := by
  have := inner_comb hG d d
  rw [h, inner_zero_left] at this
  exact inner_self_eq_zero.mp this

end Rows

section Construction

variable {S E : Type} [Fintype S] [DecidableEq S] [Fintype E] [DecidableEq E]
variable (A B : Matrix S E ℂ)

/-- The span of the rows of `A`. -/
noncomputable abbrev rowSpan : Submodule ℂ (EuclideanSpace ℂ E) :=
  Submodule.span ℂ (Set.range (rowVec A))

/-- **STEP 2** — an orthonormal basis of the row span. -/
noncomputable abbrev rowBasis :
    OrthonormalBasis (Fin (Module.finrank ℂ (rowSpan A))) ℂ (rowSpan A) :=
  stdOrthonormalBasis ℂ (rowSpan A)

omit [DecidableEq S] [DecidableEq E] in
theorem rowBasis_mem (i : Fin (Module.finrank ℂ (rowSpan A))) :
    ∃ c : S → ℂ, ∑ s, c s • rowVec A s = ((rowBasis A i : rowSpan A) : EuclideanSpace ℂ E) :=
  (Submodule.mem_span_range_iff_exists_fun ℂ).mp (rowBasis A i).2

/-- The coefficients expressing each basis vector as a combination of the rows. -/
noncomputable def coeff (i : Fin (Module.finrank ℂ (rowSpan A))) : S → ℂ :=
  Classical.choose (rowBasis_mem A i)

omit [DecidableEq S] [DecidableEq E] in
theorem coeff_spec (i : Fin (Module.finrank ℂ (rowSpan A))) :
    ∑ s, coeff A i s • rowVec A s = ((rowBasis A i : rowSpan A) : EuclideanSpace ℂ E) :=
  Classical.choose_spec (rowBasis_mem A i)

/-- **STEP 3** — the transported family: the same combinations of the rows of `B`. -/
noncomputable def transported (i : Fin (Module.finrank ℂ (rowSpan A))) : EuclideanSpace ℂ E :=
  ∑ s, coeff A i s • rowVec B s

omit [DecidableEq S] [DecidableEq E] in
theorem inner_transported (hG : A * Aᴴ = B * Bᴴ) (i j : Fin (Module.finrank ℂ (rowSpan A))) :
    inner ℂ (transported A B i) (transported A B j)
      = inner ℂ ((rowBasis A i : rowSpan A) : EuclideanSpace ℂ E)
          ((rowBasis A j : rowSpan A) : EuclideanSpace ℂ E) := by
  rw [transported, transported, inner_comb hG, coeff_spec, coeff_spec]

omit [DecidableEq S] [DecidableEq E] in
theorem transported_orthonormal (hG : A * Aᴴ = B * Bᴴ) : Orthonormal ℂ (transported A B) := by
  rw [orthonormal_iff_ite]
  intro i j
  rw [inner_transported A B hG, ← Submodule.coe_inner]
  exact (orthonormal_iff_ite.mp (rowBasis A).orthonormal) i j

omit [Fintype S] [DecidableEq S] [DecidableEq E] in
/-- The basis vectors, as an orthonormal family of the ambient space. -/
theorem rowBasis_orthonormal_ambient :
    Orthonormal ℂ (fun i => ((rowBasis A i : rowSpan A) : EuclideanSpace ℂ E)) := by
  rw [orthonormal_iff_ite]
  intro i j
  rw [← Submodule.coe_inner]
  exact (orthonormal_iff_ite.mp (rowBasis A).orthonormal) i j

/-- The coordinates of `x ∈ span a` in the basis `u`. -/
noncomputable def coord (x : rowSpan A) (i : Fin (Module.finrank ℂ (rowSpan A))) : ℂ :=
  inner ℂ ((rowBasis A i : rowSpan A) : EuclideanSpace ℂ E) (x : EuclideanSpace ℂ E)

omit [Fintype S] [DecidableEq S] [DecidableEq E] in
/-- `x = Σ_i ⟪u i, x⟫ u i` in the ambient space. -/
theorem coord_expansion (x : rowSpan A) :
    ∑ i, coord A x i • ((rowBasis A i : rowSpan A) : EuclideanSpace ℂ E)
      = (x : EuclideanSpace ℂ E) := by
  have h := (rowBasis A).sum_repr' x
  have h' := congrArg (fun y : rowSpan A => (y : EuclideanSpace ℂ E)) h
  simp only [Submodule.coe_sum, Submodule.coe_smul, Submodule.coe_inner] at h'
  exact h'

/-- **STEP 4** — the partial isometry `L x = Σ_i ⟪u i, x⟫ v i` on the row span. -/
noncomputable def partialIso : rowSpan A →ₗ[ℂ] EuclideanSpace ℂ E where
  toFun x := ∑ i, coord A x i • transported A B i
  map_add' x y := by
    simp only [coord, Submodule.coe_add, inner_add_right, add_smul, Finset.sum_add_distrib]
  map_smul' a x := by
    simp only [coord, Submodule.coe_smul, inner_smul_right, RingHom.id_apply, Finset.smul_sum,
      smul_smul]

omit [DecidableEq S] [DecidableEq E] in
theorem partialIso_apply (x : rowSpan A) :
    partialIso A B x = ∑ i, coord A x i • transported A B i := rfl

omit [DecidableEq S] [DecidableEq E] in
/-- Inner products of combinations of an orthonormal family. -/
theorem inner_comb_orthonormal {ι : Type} [Fintype ι] {v : ι → EuclideanSpace ℂ E}
    (hv : Orthonormal ℂ v) (α β : ι → ℂ) :
    inner ℂ (∑ i, α i • v i) (∑ j, β j • v j) = ∑ j, star (α j) * β j := by
  rw [inner_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [inner_smul_right, hv.inner_left_fintype, mul_comm]
  rfl

omit [DecidableEq S] [DecidableEq E] in
/-- **THE PARTIAL ISOMETRY PRESERVES INNER PRODUCTS.** -/
theorem partialIso_inner (hG : A * Aᴴ = B * Bᴴ) (x y : rowSpan A) :
    inner ℂ (partialIso A B x) (partialIso A B y)
      = inner ℂ (x : EuclideanSpace ℂ E) (y : EuclideanSpace ℂ E) := by
  rw [partialIso_apply, partialIso_apply,
    inner_comb_orthonormal (transported_orthonormal A B hG), ← coord_expansion A x,
    ← coord_expansion A y, inner_comb_orthonormal (rowBasis_orthonormal_ambient A)]

omit [DecidableEq S] [DecidableEq E] in
theorem partialIso_norm (hG : A * Aᴴ = B * Bᴴ) (x : rowSpan A) : ‖partialIso A B x‖ = ‖x‖ := by
  have h := partialIso_inner A B hG x x
  rw [inner_self_eq_norm_sq_to_K, inner_self_eq_norm_sq_to_K] at h
  have h' : ‖partialIso A B x‖ ^ 2 = ‖(x : EuclideanSpace ℂ E)‖ ^ 2 := by exact_mod_cast h
  rw [Submodule.norm_coe] at h'
  exact (pow_left_inj₀ (norm_nonneg _) (norm_nonneg _) two_ne_zero).mp h'

/-- The partial isometry, packaged. -/
noncomputable def partialIsometry (hG : A * Aᴴ = B * Bᴴ) : rowSpan A →ₗᵢ[ℂ] EuclideanSpace ℂ E :=
  ⟨partialIso A B, partialIso_norm A B hG⟩

/-- The rows of `A` as elements of their span. -/
noncomputable def rowIn (s : S) : rowSpan A :=
  ⟨rowVec A s, Submodule.subset_span (Set.mem_range_self s)⟩

omit [DecidableEq E] in
/-- **THE PARTIAL ISOMETRY SENDS `a_s` TO `b_s`**, by Gram transfer on the defect. -/
theorem partialIso_rowVec (hG : A * Aᴴ = B * Bᴴ) (s : S) :
    partialIso A B (rowIn A s) = rowVec B s := by
  -- the defect coefficients `d t = δ_{st} − Σ_i coord_i · coeff_i t`
  set d : S → ℂ := fun t => (if t = s then 1 else 0) - ∑ i, coord A (rowIn A s) i * coeff A i t
    with hd
  have hA : ∑ t, d t • rowVec A t = 0 := by
    simp only [hd, sub_smul, Finset.sum_sub_distrib, ite_smul, one_smul, zero_smul,
      Finset.sum_ite_eq', Finset.mem_univ, if_true, Finset.sum_smul, mul_smul]
    rw [Finset.sum_comm]
    simp only [← Finset.smul_sum, coeff_spec]
    rw [coord_expansion A (rowIn A s)]
    simp [rowIn]
  have hB := comb_eq_zero_of_transfer hG d hA
  simp only [hd, sub_smul, Finset.sum_sub_distrib, ite_smul, one_smul, zero_smul,
    Finset.sum_ite_eq', Finset.mem_univ, if_true, Finset.sum_smul, mul_smul] at hB
  rw [Finset.sum_comm] at hB
  simp only [← Finset.smul_sum] at hB
  rw [sub_eq_zero] at hB
  rw [partialIso_apply, hB]
  rfl

end Construction

/-! ### Section C — the extension and the matrix -/

section Matrix

variable {S E : Type} [Fintype S] [DecidableEq S] [Fintype E] [DecidableEq E]

/-- Every vector is the combination of the standard basis vectors by its coordinates. -/
theorem eq_sum_single (x : EuclideanSpace ℂ E) :
    x = ∑ f, x.ofLp f • EuclideanSpace.single f (1 : ℂ) := by
  ext e
  simp only [WithLp.ofLp_sum, WithLp.ofLp_smul, Finset.sum_apply, Pi.smul_apply, smul_eq_mul,
    PiLp.single_apply, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq, Finset.mem_univ, if_true]

/-- The matrix of a linear map of the Euclidean space, `M e f = (T e_f) e`. -/
noncomputable def matrixOf (T : EuclideanSpace ℂ E →ₗ[ℂ] EuclideanSpace ℂ E) : Matrix E E ℂ :=
  Matrix.of fun e f => (T (EuclideanSpace.single f 1)).ofLp e

theorem matrixOf_apply (T : EuclideanSpace ℂ E →ₗ[ℂ] EuclideanSpace ℂ E) (x : EuclideanSpace ℂ E)
    (e : E) : (T x).ofLp e = ∑ f, matrixOf T e f * x.ofLp f := by
  conv_lhs => rw [eq_sum_single x]
  simp only [map_sum, map_smul, WithLp.ofLp_sum, WithLp.ofLp_smul, Finset.sum_apply,
    Pi.smul_apply, smul_eq_mul, matrixOf, Matrix.of_apply]
  exact Finset.sum_congr rfl fun f _ => mul_comm _ _

/-- **THE MATRIX OF AN ISOMETRY HAS ORTHONORMAL COLUMNS**: `Mᴴ M = 1`. -/
theorem matrixOf_isometry (T : EuclideanSpace ℂ E →ₗᵢ[ℂ] EuclideanSpace ℂ E) :
    (matrixOf T.toLinearMap)ᴴ * matrixOf T.toLinearMap = 1 := by
  ext f g
  have h := T.inner_map_map (EuclideanSpace.single f (1 : ℂ)) (EuclideanSpace.single g 1)
  rw [EuclideanSpace.inner_eq_star_dotProduct, EuclideanSpace.inner_single_left] at h
  simp only [PiLp.single_apply, map_one, one_mul] at h
  rw [Matrix.mul_apply, Matrix.one_apply, ← h, dotProduct]
  simp only [Matrix.conjTranspose_apply, matrixOf, Matrix.of_apply, Pi.star_apply,
    LinearIsometry.coe_toLinearMap]
  refine Finset.sum_congr rfl fun e _ => ?_
  rw [mul_comm]

/-- A square matrix with `Mᴴ M = 1` also has `M Mᴴ = 1`. -/
theorem mul_conjTranspose_of_conjTranspose_mul {M : Matrix E E ℂ} (h : Mᴴ * M = 1) :
    M * Mᴴ = 1 := by
  have hu : IsUnit M := isUnit_of_left_inverse h
  have hdet := (Matrix.isUnit_iff_isUnit_det M).mp hu
  have hinv : Mᴴ = M⁻¹ := by
    calc Mᴴ = Mᴴ * (M * M⁻¹) := by rw [Matrix.mul_nonsing_inv M hdet, Matrix.mul_one]
      _ = (Mᴴ * M) * M⁻¹ := by rw [Matrix.mul_assoc]
      _ = M⁻¹ := by rw [h, Matrix.one_mul]
  rw [hinv]
  exact Matrix.mul_nonsing_inv M hdet

/-- **STEPS 5–6 — THE THEOREM.** Equal Gram matrices force a right unitary. -/
theorem rightUnitary_of_gram (A B : Matrix S E ℂ) (hG : A * Aᴴ = B * Bᴴ) :
    ∃ U : Matrix E E ℂ, Uᴴ * U = 1 ∧ B = A * U := by
  classical
  -- the full isometry extending the partial one
  let T : EuclideanSpace ℂ E →ₗᵢ[ℂ] EuclideanSpace ℂ E :=
    LinearIsometry.extend (partialIsometry A B hG)
  have hT : ∀ s, T (rowVec A s) = rowVec B s := fun s => by
    have := LinearIsometry.extend_apply (partialIsometry A B hG) (rowIn A s)
    simp only [rowIn] at this
    rw [this]
    exact partialIso_rowVec A B hG s
  let M := matrixOf T.toLinearMap
  have hM : Mᴴ * M = 1 := matrixOf_isometry T
  refine ⟨Mᵀ, ?_, ?_⟩
  · -- `(Mᵀ)ᴴ Mᵀ = (M Mᴴ)ᵀ = 1`
    have h2 := mul_conjTranspose_of_conjTranspose_mul hM
    have h3 := congrArg Matrix.transpose h2
    rw [Matrix.transpose_mul, Matrix.transpose_one] at h3
    rw [← h3, Matrix.conjTranspose_transpose]
    rfl
  · ext s e
    have h := congrArg (fun x => x.ofLp e) (hT s)
    have h' : (T.toLinearMap (rowVec A s)).ofLp e = (rowVec B s).ofLp e := h
    rw [matrixOf_apply] at h'
    simp only [rowVec, WithLp.ofLp_toLp] at h'
    rw [Matrix.mul_apply, ← h']
    refine Finset.sum_congr rfl fun f _ => ?_
    rw [Matrix.transpose_apply, mul_comm]

end Matrix

/-! ### Section D — purifier uniqueness and the boundary -/

section Purifier

variable {S E : Type} [Fintype S] [DecidableEq S] [Fintype E] [DecidableEq E]

omit [DecidableEq E] in
/-- The environment unitary acting on the purification: `(1 ⊗ Uᵀ) |Ψ_A⟩ = |Ψ_{A U}⟩`. -/
theorem kronecker_mulVec_purifVec (A : Matrix S E ℂ) (U : Matrix E E ℂ) :
    ((1 : Matrix S S ℂ) ⊗ₖ Uᵀ) *ᵥ purifVec A = purifVec (A * U) := by
  ext ⟨s, e⟩
  simp only [Matrix.mulVec, dotProduct, Fintype.sum_prod_type, Matrix.kronecker_apply,
    Matrix.one_apply, Matrix.transpose_apply, purifVec, Matrix.mul_apply, ite_mul, one_mul,
    zero_mul]
  rw [Finset.sum_comm]
  simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
  exact Finset.sum_congr rfl fun f _ => mul_comm _ _

/-- **PURIFIER UNIQUENESS**: two purifications on `S × E` of the same state are related by a
unitary on the environment. -/
theorem purifier_uniqueness (A B : Matrix S E ℂ)
    (h : ptraceB (Matrix.vecMulVec (purifVec A) (star (purifVec A)))
      = ptraceB (Matrix.vecMulVec (purifVec B) (star (purifVec B)))) :
    ∃ U : Matrix E E ℂ, Uᴴ * U = 1
      ∧ purifVec B = ((1 : Matrix S S ℂ) ⊗ₖ Uᵀ) *ᵥ purifVec A := by
  rw [purification_partialTrace, purification_partialTrace] at h
  obtain ⟨U, hU, hB⟩ := rightUnitary_of_gram A B h
  exact ⟨U, hU, by rw [kronecker_mulVec_purifVec, ← hB]⟩

end Purifier

/-- **THE THREE DISCHARGED ITEMS**, as one statement: PSD factorization (round thirty-four),
finite isometry extension (round forty-five), finite right-unitary uniqueness (this round),
for every finite carrier. One external item remains: compact Lie integration / reachability. -/
theorem boundary_one_item :
    (∀ (R : Type) [Fintype R] [DecidableEq R] (ρ : Matrix R R ℂ), ρ.PosSemidef →
      ∃ B : Matrix R R ℂ, ρ = B * Bᴴ)
    ∧ (∀ (A : Type) [Fintype A] [DecidableEq A], StinespringAssembly.FiniteIsometryExtensionSF A)
    ∧ ∀ (S E : Type) [Fintype S] [DecidableEq S] [Fintype E] [DecidableEq E]
        (A B : Matrix S E ℂ), A * Aᴴ = B * Bᴴ → ∃ U : Matrix E E ℂ, Uᴴ * U = 1 ∧ B = A * U :=
  ⟨fun R _ _ => psdFactorization_discharged R,
    fun A _ _ => finiteIsometryExtensionSF_discharged A,
    fun _ _ _ _ _ _ A B hG => rightUnitary_of_gram A B hG⟩

#print axioms inner_rowVec
#print axioms inner_comb
#print axioms comb_eq_zero_of_transfer
#print axioms rowBasis_mem
#print axioms coeff_spec
#print axioms inner_transported
#print axioms transported_orthonormal
#print axioms rowBasis_orthonormal_ambient
#print axioms coord_expansion
#print axioms partialIso_apply
#print axioms inner_comb_orthonormal
#print axioms partialIso_inner
#print axioms partialIso_norm
#print axioms partialIso_rowVec
#print axioms eq_sum_single
#print axioms matrixOf_apply
#print axioms matrixOf_isometry
#print axioms mul_conjTranspose_of_conjTranspose_mul
#print axioms rightUnitary_of_gram
#print axioms kronecker_mulVec_purifVec
#print axioms purifier_uniqueness
#print axioms boundary_one_item

end UhlmannUniqueness
end OIBridge
