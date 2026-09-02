/-
  OIBridge/DimensionalObstruction.lean — qubit-level positivity tests do not characterize
  complete positivity on a four-dimensional composite.

  PHASE THREE, ROUND THIRTY-THREE. Round thirty-two showed that one factor exchange routes
  the ancilla-side surplus onto a qubit system, where round twenty-seven refutes it. That
  suggests a sharper question than the next ad-hoc surplus: can exact system QM plus even
  very rich routing and control still fail to force composite complete positivity, simply
  because the VISIBLE system is too small to test complete positivity of the larger
  composite? This round establishes the mathematical obstruction that question rests on. It
  does not build an operational countermodel; that is the next round's question, and it is
  named below as not answered.

  THE MAP. On the two-qubit composite `Fin 2 × Fin 2` (four levels),

      Φ₂(X) = (2·tr(X)·I₄ − X) / 7 .

  §A — THE CHEAP PROPERTIES.  `reduction2_trace` (trace preserving, because 2·4 − 1 = 7),
  `reduction2_unital` (Φ₂(I) = I), and `reduction2_covariant`:

      Φ₂(U X Uᴴ) = U Φ₂(X) Uᴴ    for every unitary U,

  so conjugating by composite unitaries before or after does not move the map at all
  (`reduction2_commutes_conj`): the obstruction below is not removed by throwing composite
  unitaries around it.

  §B — NOT COMPLETELY POSITIVE, by the same explicit Choi witness round twenty-seven used for
  the transpose. `reduction2_choi` computes the Choi matrix exactly as

      J(Φ₂) = (2·I₁₆ − |Ω₄⟩⟨Ω₄|) / 7 ,   |Ω₄⟩ = Σ_i |i⟩|i⟩ (unnormalized),

  and `reduction2_choi_maxEnt` evaluates its quadratic form on |Ω₄⟩ to exactly −8/7. No
  CP ⟺ Kraus classification is used; `reduction2_not_cp` is a computation.

  §C — 2-POSITIVE: THE SUBSTANTIVE RESULT.  `ampl2 Φ` is `id₂ ⊗ Φ` on `Fin 2 × S`, and
  `IsTwoPositive Φ` says `ampl2 Φ` carries positive semidefinite matrices to positive
  semidefinite matrices — i.e. every test whose untouched quantum reference is ONE QUBIT
  passes. For a pure input `|ψ⟩⟨ψ|` with `ψ ∈ ℂ² ⊗ ℂ⁴`,

      (id₂ ⊗ Φ₂)(|ψ⟩⟨ψ|)  =  (2·ρ₂ ⊗ I₄ − |ψ⟩⟨ψ|) / 7 ,   ρ₂ = tr₄ |ψ⟩⟨ψ| ,

  and the key inequality `|ψ⟩⟨ψ| ≤ 2·ρ₂ ⊗ I₄` is the rank-two trace bound
  `rankTwo_trace_bound`: for a matrix of rank at most two, `|tr M|² ≤ 2‖M‖²_F`. It is proved
  by an explicit Gram–Schmidt step on the two reference rows (no eigenvalue, no square root:
  the orthogonalized row is `‖v₀‖²·v₁ − ⟪v₀,v₁⟫·v₀`, and the scale `‖v₀‖⁴` is cancelled at
  the end), then two applications of Cauchy–Schwarz. The Schmidt rank being at most two is
  exactly the reference qubit's dimension: this is where "the visible system is too small"
  enters the mathematics.

  THE EXTENSION FROM PURE TO ARBITRARY PSD INPUTS uses the rank-one spectral resolution
  `hermitian_spectral_edyad` — Mathlib's spectral theorem, which the Kadison round already
  treats as kernel-internal — together with eigenvalue nonnegativity. NO PSD SQUARE ROOT IS
  TAKEN: boundary item 3 (PSD square-root/factorization) is NOT consumed, and the rank-one
  theorem `ampl2_reduction2_rankOne` is stated separately so the dependency is visible.

  §D — THE BOXED STATEMENT.

      ┌──────────────────────────────────────────────────────────────────────────┐
      │  `qubit_tests_do_not_characterize_cp`: there is a trace-preserving,       │
      │  unital, 2-positive, NOT completely positive map on the two-qubit          │
      │  composite. Qubit-level positivity tests do not characterize CP on a 4D   │
      │  composite.                                                                │
      └──────────────────────────────────────────────────────────────────────────┘

  WHAT THIS ROUND DOES NOT DO, stated so the lint can hold it to it. It does NOT exhibit a
  `FiniteOperationalTheory (Fin 2)` containing `Φ₂` as an available composite operation
  while satisfying exact system QM, factor exchange, ancilla interference or composite
  unitary control; no operational countermodel is claimed, and nothing here says
  `KrausSoundExt` fails for any theory. It does NOT prove that `Φ₂` fails 3-positivity, and
  it does NOT add a structure field. The next question, recorded and not answered: whether
  the present architecture admits such a countermodel, and if it does, whether the missing
  ingredient is not more control but a reference-extension or parallel-composition principle
  that lets a composite operation be tested against a sufficiently large untouched reference.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FactorExchange
import OIBridge.OperationalRigidity

namespace OIBridge
namespace DimensionalObstruction

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open OperationalRigidity

open scoped ComplexOrder InnerProductSpace

/-! ### Section A — the reduction map and its cheap properties -/

section ReductionMap

variable (S : Type*) [Fintype S] [DecidableEq S]

/-- **THE REDUCTION-TYPE MAP** `Φ₂(X) = (2·tr(X)·I − X)/7`, on any finite carrier. -/
noncomputable def reduction2 : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun X := (7 : ℂ)⁻¹ • ((2 * X.trace) • (1 : Matrix S S ℂ) - X)
  map_add' X Y := by
    ext i j
    simp only [Matrix.trace_add, Matrix.smul_apply, Matrix.sub_apply, Matrix.add_apply,
      smul_eq_mul]
    ring
  map_smul' c X := by
    ext i j
    simp only [Matrix.trace_smul, Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul,
      RingHom.id_apply]
    ring

variable {S}

theorem reduction2_apply (X : Matrix S S ℂ) :
    reduction2 S X = (7 : ℂ)⁻¹ • ((2 * X.trace) • (1 : Matrix S S ℂ) - X) := rfl

/-- The two-qubit composite has four levels. -/
theorem card_two_two : Fintype.card (Fin 2 × Fin 2) = 4 := by simp

/-- **TRACE PRESERVING** on the two-qubit composite: `2·4 − 1 = 7`. -/
theorem reduction2_trace (X : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    (reduction2 (Fin 2 × Fin 2) X).trace = X.trace := by
  rw [reduction2_apply, Matrix.trace_smul, Matrix.trace_sub, Matrix.trace_smul,
    Matrix.trace_one, card_two_two]
  simp only [smul_eq_mul]
  push_cast
  ring

/-- **UNITAL** on the two-qubit composite. -/
theorem reduction2_unital : reduction2 (Fin 2 × Fin 2) 1 = 1 := by
  ext p q
  rw [reduction2_apply, Matrix.trace_one, card_two_two]
  simp only [Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul]
  push_cast
  ring

/-- **UNITARY COVARIANCE**: `Φ₂(U X Uᴴ) = U Φ₂(X) Uᴴ`. -/
theorem reduction2_covariant (U : Matrix S S ℂ) (hU : Uᴴ * U = 1) (X : Matrix S S ℂ) :
    reduction2 S (U * X * Uᴴ) = U * reduction2 S X * Uᴴ := by
  have hU' : U * Uᴴ = 1 := mul_eq_one_comm.mp hU
  have htr : (U * X * Uᴴ).trace = X.trace := by
    rw [Matrix.trace_mul_cycle, hU, Matrix.one_mul]
  rw [reduction2_apply, reduction2_apply, htr, Matrix.mul_smul, Matrix.smul_mul,
    Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one, hU']

/-- **COMPOSITE UNITARIES DO NOT MOVE IT**: as maps, conjugation commutes with `Φ₂`. -/
theorem reduction2_commutes_conj (U : Matrix S S ℂ) (hU : Uᴴ * U = 1) :
    (conjChannel U).comp (reduction2 S) = (reduction2 S).comp (conjChannel U) :=
  LinearMap.ext fun X => (reduction2_covariant U hU X).symm

end ReductionMap

/-! ### Section B — not completely positive, by the maximally entangled witness -/

section Choi

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The unnormalized maximally entangled vector `Σ_i |i⟩|i⟩` on `S × S`. -/
def maxEntVec : S × S → ℂ := fun p => if p.1 = p.2 then 1 else 0

theorem maxEntVec_star : star (maxEntVec (S := S)) = maxEntVec := by
  funext p
  simp only [Pi.star_apply, maxEntVec]
  split_ifs <;> simp

/-- Its squared norm is the number of levels. -/
theorem maxEntVec_norm : star (maxEntVec (S := S)) ⬝ᵥ maxEntVec = Fintype.card S := by
  rw [maxEntVec_star]
  have hterm : ∀ p : S × S, maxEntVec p * maxEntVec p = if p.1 = p.2 then (1 : ℂ) else 0 := by
    intro p
    simp only [maxEntVec]
    split_ifs <;> simp
  simp only [dotProduct, hterm, Fintype.sum_prod_type, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]

omit [DecidableEq S] in
theorem ite_and_one_zero (a b : Prop) [Decidable a] [Decidable b] :
    (if a ∧ b then (1 : ℂ) else 0) = (if a then 1 else 0) * (if b then 1 else 0) := by
  by_cases ha : a <;> by_cases hb : b <;> simp [ha, hb]

/-- The trace of a matrix unit is the diagonal indicator. -/
theorem trace_single_one (i j : S) :
    (Matrix.single i j (1 : ℂ)).trace = if i = j then 1 else 0 := by
  split_ifs with h
  · subst h
    exact Matrix.trace_single_eq_same _ _
  · exact Matrix.trace_single_eq_of_ne _ _ _ h

/-- **THE CHOI MATRIX, EXACTLY**: `J(Φ₂) = (2·I − |Ω⟩⟨Ω|)/7`. -/
theorem reduction2_choi :
    choiMatrix (reduction2 S)
      = (7 : ℂ)⁻¹ • ((2 : ℂ) • (1 : Matrix (S × S) (S × S) ℂ)
          - Matrix.vecMulVec maxEntVec (star maxEntVec)) := by
  ext p q
  rw [maxEntVec_star]
  show (reduction2 S (Matrix.single p.1 q.1 1)) p.2 q.2 = _
  rw [reduction2_apply, trace_single_one]
  obtain ⟨p1, p2⟩ := p
  obtain ⟨q1, q2⟩ := q
  simp only [Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul, Matrix.vecMulVec_apply,
    single_entry, maxEntVec, Matrix.one_apply, Prod.mk.injEq, ite_and_one_zero]
  ring

theorem vecMulVec_mulVec' (u v w : S → ℂ) :
    Matrix.vecMulVec u v *ᵥ w = (v ⬝ᵥ w) • u := by
  ext i
  simp [Matrix.vecMulVec, Matrix.mulVec, dotProduct, Finset.mul_sum, mul_comm, mul_left_comm]

/-- The quadratic form of the Choi matrix on the maximally entangled direction, on any
carrier: `(2d − d²)/7` for `d` levels. -/
theorem reduction2_choi_form :
    star (maxEntVec (S := S)) ⬝ᵥ (choiMatrix (reduction2 S) *ᵥ maxEntVec)
      = (7 : ℂ)⁻¹ * (2 * Fintype.card S - Fintype.card S * Fintype.card S) := by
  have hN := maxEntVec_norm (S := S)
  rw [reduction2_choi, Matrix.smul_mulVec, Matrix.sub_mulVec, Matrix.smul_mulVec,
    Matrix.one_mulVec, vecMulVec_mulVec', dotProduct_smul, dotProduct_sub, dotProduct_smul,
    dotProduct_smul, hN, smul_eq_mul, smul_eq_mul, smul_eq_mul]

/-- On the two-qubit composite the witness value is exactly `−8/7`. -/
theorem reduction2_choi_maxEnt :
    star (maxEntVec (S := Fin 2 × Fin 2)) ⬝ᵥ
        (choiMatrix (reduction2 (Fin 2 × Fin 2)) *ᵥ maxEntVec) = -8 / 7 := by
  rw [reduction2_choi_form, card_two_two]
  push_cast
  ring

/-- **NOT COMPLETELY POSITIVE.** The maximally entangled direction is negative. -/
theorem reduction2_not_cp : ¬ IsCompletelyPositive (reduction2 (Fin 2 × Fin 2)) := by
  intro h
  have hq := h.dotProduct_mulVec_nonneg maxEntVec
  rw [reduction2_choi_maxEnt] at hq
  have hcast : ((-8 / 7 : ℝ) : ℂ) = -8 / 7 := by push_cast; ring
  rw [← hcast, ← Complex.ofReal_zero, Complex.real_le_real] at hq
  norm_num at hq

end Choi

/-! ### Section C — 2-positivity -/

section RankTwoBound

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]

/-- `Σ_{ij} ⟪u_i,u_j⟫ ⟪v_j,v_i⟫`, the squared Frobenius norm of `Σ_i |u_i⟩⟨v_i|`. -/
def pairForm (u₀ u₁ v₀ v₁ : E) : ℂ :=
  ⟪u₀, u₀⟫_ℂ * ⟪v₀, v₀⟫_ℂ + ⟪u₀, u₁⟫_ℂ * ⟪v₁, v₀⟫_ℂ
    + ⟪u₁, u₀⟫_ℂ * ⟪v₀, v₁⟫_ℂ + ⟪u₁, u₁⟫_ℂ * ⟪v₁, v₁⟫_ℂ

/-- `⟪x, x⟫ = ‖x‖²`, with the real number cast by `Complex.ofReal`. -/
theorem inner_self_ofReal (x : E) : ⟪x, x⟫_ℂ = ((‖x‖ ^ 2 : ℝ) : ℂ) := by
  rw [inner_self_eq_norm_sq_to_K]
  norm_cast

/-- With orthogonal second rows the form is a sum of two products of squared norms. -/
theorem pairForm_of_orth (u₀ u₁ v₀ v₁ : E) (h : ⟪v₀, v₁⟫_ℂ = 0) :
    pairForm u₀ u₁ v₀ v₁ = ((‖u₀‖ ^ 2 * ‖v₀‖ ^ 2 + ‖u₁‖ ^ 2 * ‖v₁‖ ^ 2 : ℝ) : ℂ) := by
  have h' : ⟪v₁, v₀⟫_ℂ = 0 := by rw [← inner_conj_symm, h, map_zero]
  rw [pairForm, h, h', inner_self_ofReal, inner_self_ofReal, inner_self_ofReal,
    inner_self_ofReal]
  push_cast
  ring

/-- **THE ORTHOGONAL CASE** of the rank-two trace bound: two Cauchy–Schwarz steps. -/
theorem rankTwo_bound_of_orth (u₀ u₁ v₀ v₁ : E) (h : ⟪v₀, v₁⟫_ℂ = 0) :
    ‖⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ‖ ^ 2 ≤ 2 * (pairForm u₀ u₁ v₀ v₁).re := by
  rw [pairForm_of_orth _ _ _ _ h, Complex.ofReal_re]
  have h1 : ‖⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ‖ ≤ ‖u₀‖ * ‖v₀‖ + ‖u₁‖ * ‖v₁‖ :=
    (norm_add_le _ _).trans (add_le_add (norm_inner_le_norm _ _) (norm_inner_le_norm _ _))
  have h2 : ‖⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ‖ ^ 2 ≤ (‖u₀‖ * ‖v₀‖ + ‖u₁‖ * ‖v₁‖) ^ 2 :=
    pow_le_pow_left₀ (norm_nonneg _) h1 2
  nlinarith [h2, sq_nonneg (‖u₀‖ * ‖v₀‖ - ‖u₁‖ * ‖v₁‖)]

/-- **THE RANK-TWO TRACE BOUND**, real form: `‖tr M‖² ≤ 2‖M‖²_F` for
`M = |u₀⟩⟨v₀| + |u₁⟩⟨v₁|`, with the form's imaginary part zero. Gram–Schmidt on the second
rows, with the scale `‖v₀‖⁴` cancelled at the end; no eigenvalue and no square root. -/
theorem rankTwo_bound_re (u₀ u₁ v₀ v₁ : E) :
    ‖⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ‖ ^ 2 ≤ 2 * (pairForm u₀ u₁ v₀ v₁).re
      ∧ (pairForm u₀ u₁ v₀ v₁).im = 0 := by
  by_cases hv : v₀ = 0
  · subst hv
    refine ⟨rankTwo_bound_of_orth _ _ _ _ (inner_zero_left _), ?_⟩
    rw [pairForm_of_orth _ _ _ _ (inner_zero_left _), Complex.ofReal_im]
  · set g : ℝ := ‖v₀‖ ^ 2 with hg
    have hgpos : 0 < g := by
      rw [hg]
      exact pow_pos (norm_pos_iff.mpr hv) 2
    have hGv : ⟪v₀, v₀⟫_ℂ = (g : ℂ) := by
      rw [inner_self_ofReal, hg]
    -- the Gram–Schmidt data
    have horth : ⟪v₀, (g : ℂ) • v₁ - ⟪v₀, v₁⟫_ℂ • v₀⟫_ℂ = 0 := by
      rw [inner_sub_right, inner_smul_right, inner_smul_right, hGv]
      ring
    have hb := rankTwo_bound_of_orth ((g : ℂ) • u₀ + ⟪v₁, v₀⟫_ℂ • u₁) u₁ v₀
      ((g : ℂ) • v₁ - ⟪v₀, v₁⟫_ℂ • v₀) horth
    have hc : ⟪(g : ℂ) • u₀ + ⟪v₁, v₀⟫_ℂ • u₁, v₀⟫_ℂ
        + ⟪u₁, (g : ℂ) • v₁ - ⟪v₀, v₁⟫_ℂ • v₀⟫_ℂ
        = (g : ℂ) * (⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ) := by
      rw [inner_add_left, inner_smul_left, inner_smul_left, inner_sub_right, inner_smul_right,
        inner_smul_right, Complex.conj_ofReal, inner_conj_symm]
      ring
    have hpf : pairForm ((g : ℂ) • u₀ + ⟪v₁, v₀⟫_ℂ • u₁) u₁ v₀
        ((g : ℂ) • v₁ - ⟪v₀, v₁⟫_ℂ • v₀)
        = ((g * g : ℝ) : ℂ) * pairForm u₀ u₁ v₀ v₁ := by
      simp only [pairForm, inner_add_left, inner_add_right, inner_sub_left, inner_sub_right,
        inner_smul_left, inner_smul_right, Complex.conj_ofReal, inner_conj_symm, hGv]
      push_cast
      ring
    rw [hc, hpf] at hb
    have hnorm : ‖(g : ℂ) * (⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ)‖ ^ 2
        = g ^ 2 * ‖⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ‖ ^ 2 := by
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hgpos, mul_pow]
    rw [hnorm, Complex.re_ofReal_mul] at hb
    have hpfo := pairForm_of_orth ((g : ℂ) • u₀ + ⟪v₁, v₀⟫_ℂ • u₁) u₁ v₀
      ((g : ℂ) • v₁ - ⟪v₀, v₁⟫_ℂ • v₀) horth
    rw [hpf] at hpfo
    have him : g * g * (pairForm u₀ u₁ v₀ v₁).im = 0 := by
      have := congrArg Complex.im hpfo
      rwa [Complex.im_ofReal_mul, Complex.ofReal_im] at this
    have hg2 : 0 < g * g := mul_pos hgpos hgpos
    refine ⟨?_, ?_⟩
    · have : g * g * ‖⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ‖ ^ 2
          ≤ g * g * (2 * (pairForm u₀ u₁ v₀ v₁).re) := by nlinarith [hb]
      exact le_of_mul_le_mul_left this hg2
    · rcases mul_eq_zero.mp him with h0 | h0
      · exact absurd h0 hg2.ne'
      · exact h0

/-- **THE RANK-TWO TRACE BOUND** in the complex order: `(tr M)† (tr M) ≤ 2 ‖M‖²_F`. -/
theorem rankTwo_trace_bound (u₀ u₁ v₀ v₁ : E) :
    star (⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ) * (⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ)
      ≤ 2 * pairForm u₀ u₁ v₀ v₁ := by
  obtain ⟨hre, him⟩ := rankTwo_bound_re u₀ u₁ v₀ v₁
  have hsc : star (⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ) * (⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ)
      = ((‖⟪u₀, v₀⟫_ℂ + ⟪u₁, v₁⟫_ℂ‖ ^ 2 : ℝ) : ℂ) := by
    rw [Complex.sq_norm, Complex.normSq_eq_conj_mul_self]
    rfl
  have hpf : pairForm u₀ u₁ v₀ v₁ = (((pairForm u₀ u₁ v₀ v₁).re : ℝ) : ℂ) :=
    Complex.ext (by simp) (by simp [him])
  rw [hsc, hpf, show (2 : ℂ) * (((pairForm u₀ u₁ v₀ v₁).re : ℝ) : ℂ)
      = ((2 * (pairForm u₀ u₁ v₀ v₁).re : ℝ) : ℂ) by push_cast; ring]
  exact Complex.real_le_real.mpr hre

end RankTwoBound

section Amplification

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The rank-two trace bound in dot-product form, on `S → ℂ`. -/
theorem dot_rankTwo_bound (u₀ u₁ v₀ v₁ : S → ℂ) :
    star (star u₀ ⬝ᵥ v₀ + star u₁ ⬝ᵥ v₁) * (star u₀ ⬝ᵥ v₀ + star u₁ ⬝ᵥ v₁)
      ≤ 2 * ((star u₀ ⬝ᵥ u₀) * (star v₀ ⬝ᵥ v₀) + (star u₀ ⬝ᵥ u₁) * (star v₁ ⬝ᵥ v₀)
          + (star u₁ ⬝ᵥ u₀) * (star v₀ ⬝ᵥ v₁) + (star u₁ ⬝ᵥ u₁) * (star v₁ ⬝ᵥ v₁)) := by
  have key : ∀ x y : S → ℂ, ⟪WithLp.toLp 2 x, WithLp.toLp 2 y⟫_ℂ = star x ⬝ᵥ y := by
    intro x y
    rw [EuclideanSpace.inner_toLp_toLp, dotProduct_comm]
  have := rankTwo_trace_bound (E := EuclideanSpace ℂ S) (WithLp.toLp 2 u₀) (WithLp.toLp 2 u₁)
    (WithLp.toLp 2 v₀) (WithLp.toLp 2 v₁)
  simpa only [pairForm, key] using this

/-- The `(i, j)` reference block of a matrix on `Fin 2 × S`. -/
def refBlock (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) (i j : Fin 2) : Matrix S S ℂ :=
  Matrix.of fun k l => M (i, k) (j, l)

/-- **THE QUBIT AMPLIFICATION** `id₂ ⊗ Φ`, acting on the second factor of `Fin 2 × S`. -/
def ampl2 (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    Matrix (Fin 2 × S) (Fin 2 × S) ℂ :=
  Matrix.of fun p q => Φ (refBlock M p.1 q.1) p.2 q.2

/-- **2-POSITIVITY**: `id₂ ⊗ Φ` carries positive semidefinite matrices to positive
semidefinite matrices — every test with a one-qubit untouched reference passes. -/
def IsTwoPositive (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ, M.PosSemidef → (ampl2 Φ M).PosSemidef

/-- The reference marginal `tr_S M`. -/
def refMarginal (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.of fun i j => ∑ m, M (i, m) (j, m)

theorem refBlock_add (M N : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) (i j : Fin 2) :
    refBlock (M + N) i j = refBlock M i j + refBlock N i j := by
  ext k l
  rfl

theorem refBlock_smul (c : ℂ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) (i j : Fin 2) :
    refBlock (c • M) i j = c • refBlock M i j := by
  ext k l
  rfl

theorem ampl2_add (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (M N : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    ampl2 Φ (M + N) = ampl2 Φ M + ampl2 Φ N := by
  ext p q
  simp only [ampl2, Matrix.of_apply, refBlock_add, map_add, Matrix.add_apply]

theorem ampl2_smul (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (c : ℂ)
    (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    ampl2 Φ (c • M) = c • ampl2 Φ M := by
  ext p q
  simp only [ampl2, Matrix.of_apply, refBlock_smul, map_smul, Matrix.smul_apply]

theorem ampl2_zero (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : ampl2 Φ 0 = 0 := by
  have h0 : ∀ i j : Fin 2, refBlock (0 : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) i j = 0 := by
    intro i j
    ext k l
    rfl
  ext p q
  simp only [ampl2, Matrix.of_apply, h0, map_zero, Matrix.zero_apply]

theorem ampl2_sum (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) {ι : Type*} (s : Finset ι)
    (M : ι → Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    ampl2 Φ (∑ i ∈ s, M i) = ∑ i ∈ s, ampl2 Φ (M i) := by
  classical
  induction s using Finset.induction with
  | empty => rw [Finset.sum_empty, Finset.sum_empty, ampl2_zero]
  | insert x s hx ih => rw [Finset.sum_insert hx, Finset.sum_insert hx, ampl2_add, ih]

theorem real_smul_eq_smul (r : ℝ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    r • M = (r : ℂ) • M := by
  ext i j
  simp [Matrix.smul_apply, Complex.real_smul]

theorem ampl2_real_smul (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (r : ℝ)
    (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    ampl2 Φ (r • M) = (r : ℂ) • ampl2 Φ M := by
  rw [real_smul_eq_smul, ampl2_smul]

/-- **THE AMPLIFIED REDUCTION MAP**: `(id₂ ⊗ Φ₂)(M) = (2·tr_S M ⊗ I − M)/7`. -/
theorem ampl2_reduction2 (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    ampl2 (reduction2 S) M
      = (7 : ℂ)⁻¹ • ((2 : ℂ) • tensorOf (refMarginal M) (1 : Matrix S S ℂ) - M) := by
  ext p q
  obtain ⟨i, k⟩ := p
  obtain ⟨j, l⟩ := q
  simp only [ampl2, Matrix.of_apply, reduction2_apply, Matrix.smul_apply, Matrix.sub_apply,
    smul_eq_mul, tensorOf_apply, refMarginal, refBlock, Matrix.trace, Matrix.diag_apply]
  ring

theorem refMarginal_isHermitian {M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ} (hM : M.IsHermitian) :
    (refMarginal M).IsHermitian := by
  ext i j
  simp only [Matrix.conjTranspose_apply, refMarginal, Matrix.of_apply, star_sum]
  exact Finset.sum_congr rfl fun m _ => hM.apply _ _

theorem tensorOf_one_isHermitian {R : Matrix (Fin 2) (Fin 2) ℂ} (hR : R.IsHermitian) :
    (tensorOf R (1 : Matrix S S ℂ)).IsHermitian := by
  ext p q
  rw [Matrix.conjTranspose_apply, tensorOf_apply, tensorOf_apply, star_mul', hR.apply,
    Matrix.isHermitian_one.apply]

/-- The quadratic form of `R ⊗ I` on `Fin 2 × S`, in terms of the reference rows. -/
theorem form_tensor_one (R : Matrix (Fin 2) (Fin 2) ℂ) (x : Fin 2 × S → ℂ) :
    star x ⬝ᵥ (tensorOf R (1 : Matrix S S ℂ) *ᵥ x)
      = R 0 0 * (star (fun k => x (0, k)) ⬝ᵥ fun k => x (0, k))
        + R 0 1 * (star (fun k => x (0, k)) ⬝ᵥ fun k => x (1, k))
        + R 1 0 * (star (fun k => x (1, k)) ⬝ᵥ fun k => x (0, k))
        + R 1 1 * (star (fun k => x (1, k)) ⬝ᵥ fun k => x (1, k)) := by
  simp only [dotProduct, Matrix.mulVec, tensorOf_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
    Pi.star_apply, Matrix.one_apply, mul_ite, mul_one, mul_zero, ite_mul, zero_mul,
    Finset.sum_ite_eq, Finset.mem_univ, if_true, Finset.mul_sum]
  simp only [← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun k _ => by ring

theorem seven_inv_nonneg : (0 : ℂ) ≤ (7 : ℂ)⁻¹ := by
  rw [show (7 : ℂ)⁻¹ = ((7⁻¹ : ℝ) : ℂ) by push_cast; rfl]
  exact Complex.zero_le_real.mpr (by norm_num)

/-- **THE PURE CASE**: `(id₂ ⊗ Φ₂)(|ψ⟩⟨ψ|) ⪰ 0` for every `ψ ∈ ℂ² ⊗ ℂ^S`, by the rank-two
trace bound. No spectral input: the two reference rows are orthogonalized by hand. -/
theorem ampl2_reduction2_rankOne (ψ : Fin 2 × S → ℂ) :
    (ampl2 (reduction2 S) (Matrix.vecMulVec ψ (star ψ))).PosSemidef := by
  rw [ampl2_reduction2]
  refine Matrix.PosSemidef.smul ?_ seven_inv_nonneg
  have hP := Matrix.posSemidef_vecMulVec_self_star ψ
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg ?_ ?_
  · exact ((tensorOf_one_isHermitian (refMarginal_isHermitian hP.1)).smul
      (isSelfAdjoint_iff.mpr (by simp))).sub hP.1
  · intro x
    rw [Matrix.sub_mulVec, Matrix.smul_mulVec, dotProduct_sub, dotProduct_smul,
      vecMulVec_mulVec', dotProduct_smul, form_tensor_one, smul_eq_mul, smul_eq_mul,
      star_dotProduct ψ x, sub_nonneg]
    have hR : ∀ i j : Fin 2, refMarginal (Matrix.vecMulVec ψ (star ψ)) i j
        = star (fun m => ψ (j, m)) ⬝ᵥ fun m => ψ (i, m) := by
      intro i j
      simp only [refMarginal, Matrix.of_apply, Matrix.vecMulVec_apply, dotProduct, Pi.star_apply]
      exact Finset.sum_congr rfl fun m _ => mul_comm _ _
    have hc : star x ⬝ᵥ ψ
        = star (fun k => x (0, k)) ⬝ᵥ (fun k => ψ (0, k))
          + star (fun k => x (1, k)) ⬝ᵥ (fun k => ψ (1, k)) := by
      simp only [dotProduct, Fintype.sum_prod_type, Fin.sum_univ_two, Pi.star_apply]
    rw [hc, hR, hR, hR, hR]
    calc _ ≤ _ := dot_rankTwo_bound (fun k => x (0, k)) (fun k => x (1, k))
          (fun k => ψ (0, k)) (fun k => ψ (1, k))
      _ = _ := by ring

theorem edyad_eq_vecMulVec {n : Type*} (U : Matrix n n ℂ) (i : n) :
    edyad U i = Matrix.vecMulVec (fun x => U x i) (star fun x => U x i) := by
  ext x y
  rfl

/-- **Φ₂ IS 2-POSITIVE.** The pure case, extended to every positive semidefinite input by
the rank-one spectral resolution (Mathlib's spectral theorem, kernel-internal since the
Kadison round) and eigenvalue nonnegativity. No PSD square root is taken; boundary item 3
is not consumed. -/
theorem reduction2_twoPositive : IsTwoPositive (reduction2 S) := by
  intro M hM
  obtain ⟨U, -, hspec⟩ := hermitian_spectral_edyad hM.1
  rw [hspec, ampl2_sum]
  refine posSemidef_sum _ _ fun i _ => ?_
  rw [ampl2_real_smul, edyad_eq_vecMulVec]
  exact (ampl2_reduction2_rankOne _).smul (Complex.zero_le_real.mpr (hM.eigenvalues_nonneg i))

end Amplification

/-! ### Section D — the boxed statement -/

/-- **QUBIT-LEVEL POSITIVITY TESTS DO NOT CHARACTERIZE CP ON A 4D COMPOSITE.** There is a
trace-preserving, unital, 2-positive map on the two-qubit composite that is not completely
positive. -/
theorem qubit_tests_do_not_characterize_cp :
    ∃ Φ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ,
      IsTracePreserving Φ ∧ Φ 1 = 1 ∧ IsTwoPositive Φ ∧ ¬ IsCompletelyPositive Φ :=
  ⟨reduction2 _, reduction2_trace, reduction2_unital, reduction2_twoPositive, reduction2_not_cp⟩

#print axioms reduction2_trace
#print axioms reduction2_unital
#print axioms reduction2_covariant
#print axioms reduction2_commutes_conj
#print axioms maxEntVec_norm
#print axioms reduction2_choi
#print axioms reduction2_choi_form
#print axioms reduction2_choi_maxEnt
#print axioms reduction2_not_cp
#print axioms pairForm_of_orth
#print axioms rankTwo_bound_of_orth
#print axioms rankTwo_bound_re
#print axioms rankTwo_trace_bound
#print axioms dot_rankTwo_bound
#print axioms ampl2_sum
#print axioms ampl2_reduction2
#print axioms form_tensor_one
#print axioms ampl2_reduction2_rankOne
#print axioms reduction2_twoPositive
#print axioms qubit_tests_do_not_characterize_cp

end DimensionalObstruction
end OIBridge
