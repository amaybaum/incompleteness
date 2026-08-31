/-
  OIBridge/JordanClassification.lean — phase three, round seven: PSD self-duality, the
  C3b.3 assembly, and the kernel matrix-unit classification (milestone C3b closed).

  THE ARC. Round six delivered the three legs — separation, the data-defined linear map,
  and the Kadison theorem. This file closes C3b: (i) the one missing order fact, PSD
  self-duality, so positivity of the data-defined map is inferred in BOTH directions;
  (ii) the assembly: two completions with identical complete operational data induce a
  two-sided order isomorphism, constructed symmetrically (`Φ₁₂`, `Φ₂₁`) with bijectivity
  from the operational construction itself, hence a Jordan ∗-isomorphism; (iii) the
  matrix-unit classification: every such Jordan isomorphism of `M_D(ℂ)` is
  `X ↦ WXW†` or `X ↦ WX^TW†` for a unitary `W`. Chained:

    ANY TWO EXISTING OI-COMPATIBLE COHERENT COMPLETIONS WITH THE SAME COMPLETE
    OPERATIONAL DATA ARE UNITARY OR ANTIUNITARY EQUIVALENT (`sameData_unitary_or_transpose`).

  Section A — self-duality of the PSD cone.
    * `trace_mul_vecMulVec`, `psd_iff_trace_nonneg` — `A ⪰ 0` iff it pairs nonnegatively
      with every positive matrix: the missing converse to round six's
      `psd_trace_mul_nonneg`, by testing against rank-one dyads. This is what upgrades
      "Φ preserves the pairing data" to "Φ preserves positivity" without a one-sided gap.

  Section B — the C3b.3 assembly.
    * `sameData_orderIso` — two completions with identical pairing data, Hermitian
      spanning contexts (the trivial context included), separating accessible states,
      and full accessible cones induce ℂ-linear maps `Φ`, `Ψ` matching every context,
      mutually inverse BY CONSTRUCTION (each is data-defined, so their composite fixes a
      spanning family), unital, star-preserving (span induction over Hermitian
      generators), and positive in both directions (transfer + cone + self-duality):
      the full `OrderIsoHyp` package, so `orderIso_jordan` fires.
    * `jordan_complexify` — the Hermitian Jordan identity extends to ALL pairs for a
      ℂ-linear map, by decomposing into Hermitian parts; needed because the matrix-unit
      analysis probes non-Hermitian units.

  Section C — the matrix-unit classification.
    * `orthogonal_resolution_rank_one` — a family of nonzero pairwise-orthogonal
      projections indexed by the dimension and summing to `1` is a rank-one resolution:
      each is a dyad on an orthonormal frame. The counting is exact: traces are natural
      numbers summing to `D` with `D` terms each at least one.
    * `corner_form` / `corner_nilpotent` / `corner_unimodular` / `corner_cocycle` — the
      image of each off-diagonal matrix unit lives in a two-dimensional corner spanned
      by the direct and transposed frame dyads, with coefficients `(α, β)` satisfying
      `αβ = 0`, `|α|² + |β|² = 1`, and the multiplicative cocycle across triples.
    * `orientation_dichotomy` — TRIPLE COHERENCE: mixed orientations cannot coexist; a
      single transposed corner forces every corner transposed. (Probe F19: a map mixing
      orientations violates the Jordan identity at the triple exactly.)
    * `matrixJordan_unitary_or_transpose` — THE CLASSIFICATION: a ℂ-linear unital
      star-preserving injective Jordan homomorphism of `M_D(ℂ)` is `X ↦ WXW†` or
      `X ↦ WX^TW†` with `W` unitary, the phases absorbed by the coboundary
      `α_ij = d_i·conj d_j` — the same local-pair → triple-consistency → global
      orientation → phase-coboundary architecture as the Hamiltonian reconstruction.

  WHAT THIS DOES NOT ESTABLISH. Which of the two branches is physical: that is C3c, and
  round five already located the lever — the real/native accessible structure is stable
  under the transpose branch while an oriented complex reference is not. The remaining
  research question is whether OI derives that oriented reference; nothing here assumes
  it. Existence also remains governed by the no-go: the classification is of the
  completions that exist.
-/
import OIBridge.OperationalRigidity

namespace OIBridge
namespace JordanClassification

open Complex Matrix OperationalRigidity
open scoped ComplexOrder

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ### Section A — self-duality of the PSD cone -/

omit [DecidableEq n] in
/-- The trace against a rank-one dyad is the quadratic form. -/
theorem trace_mul_vecMulVec (A : Matrix n n ℂ) (v : n → ℂ) :
    Matrix.trace (A * Matrix.vecMulVec v (star v)) = star v ⬝ᵥ (A *ᵥ v) := by
  rw [Matrix.mul_vecMulVec, Matrix.trace, dotProduct]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [Matrix.diag_apply, Matrix.vecMulVec_apply, Pi.star_apply]
  ring

/-- **Self-duality of the PSD cone**: a Hermitian matrix pairing nonnegatively with
every positive matrix is positive — test against the rank-one dyads. Together with
`psd_trace_mul_nonneg` this is the exact two-sided duality the assembly consumes. -/
theorem psd_iff_trace_nonneg {A : Matrix n n ℂ} (hAh : A.IsHermitian) :
    A.PosSemidef ↔ ∀ X : Matrix n n ℂ, X.PosSemidef → 0 ≤ Matrix.trace (A * X) := by
  constructor
  · exact fun hA X hX => psd_trace_mul_nonneg hA hX
  · intro h
    refine Matrix.posSemidef_iff_dotProduct_mulVec.mpr ⟨hAh, fun v => ?_⟩
    have hd := h (Matrix.vecMulVec v (star v)) (Matrix.posSemidef_vecMulVec_self_star v)
    rwa [trace_mul_vecMulVec] at hd

/-! ### Section B₀ — matrix units and complexification -/

/-- The matrix unit `E_ij`. -/
def Eu (i j : n) : Matrix n n ℂ := Matrix.single i j 1

omit [Fintype n] in
theorem Eu_conjTranspose (i j : n) : (Eu i j)ᴴ = Eu j i := by
  ext a b
  rw [Matrix.conjTranspose_apply, Eu, Eu, Matrix.single_apply, Matrix.single_apply]
  by_cases hc : i = b ∧ j = a
  · rw [if_pos hc, if_pos ⟨hc.2, hc.1⟩, star_one]
  · rw [if_neg hc, if_neg (fun h => hc ⟨h.2, h.1⟩), star_zero]

theorem Eu_mul_same (i j k : n) : Eu i j * Eu j k = Eu i k := by
  show Matrix.single i j (1 : ℂ) * Matrix.single j k 1 = Matrix.single i k 1
  rw [Matrix.single_mul_single_same, one_mul]

theorem Eu_mul_of_ne (i : n) {j k : n} (h : j ≠ k) (l : n) : Eu i j * Eu k l = 0 :=
  Matrix.single_mul_single_of_ne _ _ _ _ h _

theorem sum_Eu_diag : ∑ i, Eu i i = (1 : Matrix n n ℂ) := by
  ext a b
  rw [Matrix.sum_apply, Matrix.one_apply]
  by_cases hab : a = b
  · subst hab
    rw [if_pos rfl]
    rw [Finset.sum_eq_single a (fun i _ hia => by
        rw [Eu, Matrix.single_apply, if_neg (fun hc => hia hc.1)])
      (fun ha => absurd (Finset.mem_univ a) ha)]
    rw [Eu, Matrix.single_apply, if_pos ⟨rfl, rfl⟩]
  · rw [if_neg hab]
    refine Finset.sum_eq_zero fun i _ => ?_
    rw [Eu, Matrix.single_apply, if_neg (fun hc => hab (hc.1.symm.trans hc.2))]

omit [Fintype n] in
theorem Eu_ne_zero (i j : n) : Eu i j ≠ 0 := by
  intro h
  have := congrFun (congrFun h i) j
  rw [Eu, Matrix.single_apply_same, Matrix.zero_apply] at this
  exact one_ne_zero this

omit [Fintype n] [DecidableEq n] in
/-- Every matrix splits into Hermitian real and imaginary parts. -/
theorem herm_decomp (A : Matrix n n ℂ) :
    ∃ H K : Matrix n n ℂ, H.IsHermitian ∧ K.IsHermitian ∧ A = H + Complex.I • K := by
  refine ⟨(1/2 : ℂ) • (A + Aᴴ), (Complex.I / 2) • (Aᴴ - A), ?_, ?_, ?_⟩
  · show ((1/2 : ℂ) • (A + Aᴴ))ᴴ = _
    rw [Matrix.conjTranspose_smul, Matrix.conjTranspose_add,
      Matrix.conjTranspose_conjTranspose]
    rw [show star (1/2 : ℂ) = (1/2 : ℂ) from by norm_num]
    rw [add_comm]
  · show ((Complex.I / 2 : ℂ) • (Aᴴ - A))ᴴ = _
    rw [Matrix.conjTranspose_smul, Matrix.conjTranspose_sub,
      Matrix.conjTranspose_conjTranspose]
    rw [show star (Complex.I / 2 : ℂ) = -(Complex.I / 2) from by
      simp [Complex.ext_iff]
      norm_num]
    rw [neg_smul, ← smul_neg, neg_sub]
  · rw [smul_smul]
    rw [show Complex.I * (Complex.I / 2) = (-(1/2) : ℂ) from by
      rw [← mul_div_assoc, Complex.I_mul_I]
      norm_num]
    module

/-- **Complexification of the Jordan identity**: a ℂ-linear map satisfying the Jordan
identity on Hermitian pairs satisfies it on ALL pairs, by Hermitian decomposition and
bilinearity of the anticommutator. -/
theorem jordan_complexify (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (h : ∀ A B : Matrix n n ℂ, A.IsHermitian → B.IsHermitian →
      Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (A B : Matrix n n ℂ) :
    Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A := by
  obtain ⟨HA, KA, hH, hK, rfl⟩ := herm_decomp A
  obtain ⟨HB, KB, hH', hK', rfl⟩ := herm_decomp B
  have e1 := h HA HB hH hH'
  have e2 := h HA KB hH hK'
  have e3 := h KA HB hK hH'
  have e4 := h KA KB hK hK'
  have hexp : (HA + Complex.I • KA) * (HB + Complex.I • KB)
      + (HB + Complex.I • KB) * (HA + Complex.I • KA)
      = (HA * HB + HB * HA) + Complex.I • (HA * KB + KB * HA)
        + Complex.I • (KA * HB + HB * KA) + (-1 : ℂ) • (KA * KB + KB * KA) := by
    simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_smul,
      Complex.I_mul_I, smul_add]
    module
  rw [hexp, map_add, map_add, map_add, map_smul, map_smul, map_smul,
    e1, e2, e3, e4, map_add, map_add, map_smul, map_smul]
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_smul,
    Complex.I_mul_I, smul_add]
  module

omit [DecidableEq n] in
/-- The Jordan identity preserves squares. -/
theorem jordan_sq (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (A : Matrix n n ℂ) : Φ (A * A) = Φ A * Φ A := by
  have h := hj A A
  rw [map_add] at h
  have h2 : (2 : ℂ) • Φ (A * A) = (2 : ℂ) • (Φ A * Φ A) := by
    rw [two_smul, two_smul]
    exact h
  exact smul_right_injective _ (by norm_num : (2 : ℂ) ≠ 0) h2

omit [DecidableEq n] in
/-- Idempotents with vanishing anticommutator have vanishing products. -/
theorem proj_anticommute {p q : Matrix n n ℂ} (hp : p * p = p) (_hq : q * q = q)
    (h : p * q + q * p = 0) : p * q = 0 := by
  have h3 : p * (p * q + q * p) = p * q + p * q * p := by
    rw [Matrix.mul_add, ← Matrix.mul_assoc, hp, ← Matrix.mul_assoc]
  have h4 : (p * q + q * p) * p = p * q * p + q * p := by
    rw [Matrix.add_mul, Matrix.mul_assoc q p p, hp]
  have h5 : p * q + p * q * p = 0 := by
    rw [← h3, h, Matrix.mul_zero]
  have h6 : p * q * p + q * p = 0 := by
    rw [← h4, h, Matrix.zero_mul]
  have h7 : p * q - q * p = (p * q + p * q * p) - (p * q * p + q * p) := by abel
  rw [h5, h6, sub_zero] at h7
  have h8 : (2 : ℂ) • (p * q) = 0 := by
    rw [two_smul]
    calc p * q + p * q = p * q + q * p := by rw [sub_eq_zero.mp h7]
      _ = 0 := h
  exact (smul_eq_zero.mp h8).resolve_left (by norm_num)

/-- The images of the diagonal units: Hermitian projections. -/
theorem image_diag_proj (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hstar : ∀ X : Matrix n n ℂ, Φ Xᴴ = (Φ X)ᴴ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A) (i : n) :
    (Φ (Eu i i)).IsHermitian ∧ Φ (Eu i i) * Φ (Eu i i) = Φ (Eu i i) := by
  constructor
  · show (Φ (Eu i i))ᴴ = Φ (Eu i i)
    rw [← hstar, Eu_conjTranspose]
  · rw [← jordan_sq Φ hj, Eu_mul_same]

/-- The images of distinct diagonal units are orthogonal. -/
theorem image_diag_orth (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hstar : ∀ X : Matrix n n ℂ, Φ Xᴴ = (Φ X)ᴴ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    {i j : n} (hij : i ≠ j) :
    Φ (Eu i i) * Φ (Eu j j) = 0 := by
  have h0 : Eu i i * Eu j j + Eu j j * Eu i i = 0 := by
    rw [Eu_mul_of_ne i hij j, Eu_mul_of_ne j (Ne.symm hij) i, add_zero]
  have h := hj (Eu i i) (Eu j j)
  rw [h0, map_zero] at h
  exact proj_anticommute (image_diag_proj Φ hstar hj i).2
    (image_diag_proj Φ hstar hj j).2 h.symm

/-- The images of the diagonal units resolve the identity. -/
theorem image_diag_sum (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (hone : Φ 1 = 1) :
    ∑ i, Φ (Eu i i) = 1 := by
  rw [← map_sum, sum_Eu_diag, hone]

omit [Fintype n] in
/-- The images of the diagonal units are nonzero. -/
theorem image_diag_ne (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hinj : Function.Injective Φ) (i : n) : Φ (Eu i i) ≠ 0 := by
  intro h
  exact Eu_ne_zero i i (hinj (by rw [h, map_zero]))

/-! ### Section C₀ — frame helpers -/

omit [Fintype n] [DecidableEq n] in
theorem real_smul_matrix (r : ℝ) (M : Matrix n n ℂ) : r • M = ((r : ℝ) : ℂ) • M := by
  ext x y
  rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul]
  exact Complex.real_smul

omit [DecidableEq n] in
theorem col_dotProduct (U : Matrix n n ℂ) (k l : n) :
    (star fun x => U x k) ⬝ᵥ (fun x => U x l) = (Uᴴ * U) k l := by
  rw [dotProduct, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [Pi.star_apply, Matrix.conjTranspose_apply]

omit [DecidableEq n] in
theorem trace_edyad (U : Matrix n n ℂ) (k : n) :
    Matrix.trace (edyad U k) = (Uᴴ * U) k k := by
  rw [Matrix.trace, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [Matrix.diag_apply, edyad_apply, Matrix.conjTranspose_apply]
  ring

omit [DecidableEq n] in
theorem edyad_mulVec (U : Matrix n n ℂ) (k : n) (w : n → ℂ) :
    edyad U k *ᵥ w = ((star fun x => U x k) ⬝ᵥ w) • (fun x => U x k) := by
  ext x
  rw [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul, dotProduct, Finset.sum_mul]
  refine Finset.sum_congr rfl fun y _ => ?_
  rw [edyad_apply, Pi.star_apply]
  ring

omit [DecidableEq n] in
theorem dot_shift (M : Matrix n n ℂ) (x w : n → ℂ) :
    star (M *ᵥ x) ⬝ᵥ w = star x ⬝ᵥ (Mᴴ *ᵥ w) := by
  rw [dotProduct, dotProduct]
  rw [Finset.sum_congr rfl fun p _ => by
    rw [Pi.star_apply, Matrix.mulVec, dotProduct, star_sum, Finset.sum_mul]]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun q _ => ?_
  rw [Pi.star_apply, Matrix.mulVec, dotProduct, Finset.mul_sum]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [star_mul', Matrix.conjTranspose_apply]
  ring

/-! ### Section C₁ — the rank-one resolution -/

/-- A Hermitian idempotent is a partial sum of frame dyads: its eigenvalues are `0` or
`1`, so the spectral resolution truncates to the eigenvalue-one block. -/
theorem proj_dyad_decomp {p : Matrix n n ℂ} (hph : p.IsHermitian) (hp2 : p * p = p) :
    ∃ (U : Matrix n n ℂ) (S : Finset n), Uᴴ * U = 1 ∧ p = ∑ k ∈ S, edyad U k := by
  obtain ⟨U, hU1, hspec⟩ := hermitian_spectral_edyad hph
  have hdiag : p = U * Matrix.diagonal (fun k => ((hph.eigenvalues k : ℝ) : ℂ)) * Uᴴ := by
    conv_lhs => rw [hspec]
    rw [conj_diagonal_eq_sum_edyad]
    exact Finset.sum_congr rfl fun k _ => real_smul_matrix _ _
  have hid : ∀ k, hph.eigenvalues k * hph.eigenvalues k = hph.eigenvalues k := by
    intro k
    have h := hp2
    rw [hdiag, conj_diag_mul hU1] at h
    have h0 : U * Matrix.diagonal (fun i =>
        ((hph.eigenvalues i * hph.eigenvalues i - hph.eigenvalues i : ℝ) : ℂ)) * Uᴴ
        = 0 := by
      rw [← conj_diag_sub, h, sub_self]
    have := conj_diag_eq_zero hU1 h0 k
    linarith
  refine ⟨U, Finset.univ.filter (fun k => hph.eigenvalues k = 1), hU1, ?_⟩
  conv_lhs => rw [hspec]
  rw [← Finset.sum_filter_add_sum_filter_not Finset.univ (fun k => hph.eigenvalues k = 1)]
  rw [show ∑ k ∈ Finset.univ.filter (fun k => ¬hph.eigenvalues k = 1),
      hph.eigenvalues k • edyad U k = 0 from Finset.sum_eq_zero fun k hk => by
    have hk1 := (Finset.mem_filter.mp hk).2
    have hk0 : hph.eigenvalues k = 0 := by
      rcases mul_eq_zero.mp (show hph.eigenvalues k * (hph.eigenvalues k - 1) = 0 from
        by nlinarith [hid k]) with h | h
      · exact h
      · exact absurd (by linarith : hph.eigenvalues k = 1) hk1
    rw [hk0, zero_smul]]
  rw [add_zero]
  refine Finset.sum_congr rfl fun k hk => ?_
  rw [(Finset.mem_filter.mp hk).2, one_smul]

/-- **The rank-one resolution.** Nonzero pairwise-orthogonal Hermitian projections,
indexed by the dimension and summing to the identity, are dyads on an orthonormal frame:
the traces are naturals summing to `D` with `D` terms each at least one. -/
theorem orthogonal_resolution_rank_one (P : n → Matrix n n ℂ)
    (hh : ∀ i, (P i).IsHermitian) (hp2 : ∀ i, P i * P i = P i)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1) (hne : ∀ i, P i ≠ 0) :
    ∃ v : n → n → ℂ,
      (∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
      ∧ ∀ i, P i = Matrix.vecMulVec (v i) (star (v i)) := by
  choose U S hU1 hdecomp using fun i => proj_dyad_decomp (hh i) (hp2 i)
  have htr : ∀ i, Matrix.trace (P i) = ((S i).card : ℂ) := by
    intro i
    rw [hdecomp i, Matrix.trace_sum]
    rw [Finset.sum_congr rfl fun k _ => by rw [trace_edyad, hU1 i, Matrix.one_apply_eq]]
    rw [Finset.sum_const]
    simp
  have hcards : ∑ i, (S i).card = Fintype.card n := by
    have h1 : ∑ i, Matrix.trace (P i) = ((Fintype.card n : ℕ) : ℂ) := by
      rw [← Matrix.trace_sum, hsum, Matrix.trace_one]
    rw [Finset.sum_congr rfl fun i _ => htr i] at h1
    exact_mod_cast h1
  have hpos : ∀ i, 1 ≤ (S i).card := by
    intro i
    by_contra hlt
    push Not at hlt
    have hS : S i = ∅ := Finset.card_eq_zero.mp (Nat.lt_one_iff.mp hlt)
    exact hne i (by rw [hdecomp i, hS, Finset.sum_empty])
  have hone' : ∀ i, (S i).card = 1 := by
    intro i
    by_contra hne1
    have h2 : 1 < (S i).card := lt_of_le_of_ne (hpos i) (Ne.symm hne1)
    have hgt : Fintype.card n < ∑ j, (S j).card := by
      calc Fintype.card n = ∑ _j : n, 1 := by
            rw [Finset.sum_const, smul_eq_mul, mul_one, Finset.card_univ]
        _ < ∑ j, (S j).card := Finset.sum_lt_sum (fun j _ => hpos j)
            ⟨i, Finset.mem_univ i, h2⟩
    rw [hcards] at hgt
    exact lt_irrefl _ hgt
  choose k hk using fun i => Finset.card_eq_one.mp (hone' i)
  have hPsingle : ∀ i, P i = edyad (U i) (k i) := by
    intro i
    rw [hdecomp i, hk i, Finset.sum_singleton]
  have hPv : ∀ i, P i *ᵥ (fun x => U i x (k i)) = fun x => U i x (k i) := by
    intro i
    rw [hPsingle i, edyad_mulVec, col_dotProduct, hU1 i, Matrix.one_apply_eq, one_smul]
  refine ⟨fun i x => U i x (k i), fun i j => ?_, fun i => ?_⟩
  · dsimp only
    by_cases hij : i = j
    · subst hij
      rw [if_pos rfl, col_dotProduct, hU1 i, Matrix.one_apply_eq]
    · rw [if_neg hij, ← hPv i, ← hPv j, dot_shift, Matrix.mulVec_mulVec,
        (hh i).eq, horth i j hij, Matrix.zero_mulVec, dotProduct_zero]
  · dsimp only
    rw [hPsingle i]
    ext x y
    rw [edyad_apply, Matrix.vecMulVec_apply, Pi.star_apply]

/-! ### Section C₂ — the frame dyad calculus -/

/-- The frame dyad `|v_i⟩⟨v_j|`. -/
def qd (v : n → n → ℂ) (i j : n) : Matrix n n ℂ :=
  Matrix.vecMulVec (v i) (star (v j))

theorem qd_mul_qd (v : n → n → ℂ)
    (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0) (i j k l : n) :
    qd v i j * qd v k l = (if j = k then (1 : ℂ) else 0) • qd v i l := by
  rw [qd, qd, qd, Matrix.vecMulVec_mul_vecMulVec, horm j k, Matrix.vecMulVec_smul]

omit [Fintype n] [DecidableEq n] in
theorem qd_conjTranspose (v : n → n → ℂ) (i j : n) : (qd v i j)ᴴ = qd v j i := by
  ext x y
  rw [Matrix.conjTranspose_apply, qd, qd, Matrix.vecMulVec_apply, Matrix.vecMulVec_apply,
    Pi.star_apply, Pi.star_apply, star_mul', star_star]
  ring

theorem qd_mulVec (v : n → n → ℂ)
    (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0) (i j k : n) :
    qd v i j *ᵥ v k = (if j = k then (1 : ℂ) else 0) • v i := by
  rw [qd, Matrix.vecMulVec_mulVec, horm]
  rw [op_smul_eq_smul]

theorem quad_qd (v : n → n → ℂ)
    (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0) (x i j y : n) :
    star (v x) ⬝ᵥ (qd v i j *ᵥ v y)
      = (if x = i then (1 : ℂ) else 0) * (if j = y then 1 else 0) := by
  rw [qd_mulVec v horm, dotProduct_smul, horm, smul_eq_mul]
  ring

theorem quad_two (v : n → n → ℂ)
    (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (a b : ℂ) (i j k l x y : n) :
    star (v x) ⬝ᵥ ((a • qd v i j + b • qd v k l) *ᵥ v y)
      = a * ((if x = i then (1 : ℂ) else 0) * (if j = y then 1 else 0))
        + b * ((if x = k then (1 : ℂ) else 0) * (if l = y then 1 else 0)) := by
  rw [Matrix.add_mulVec, Matrix.smul_mulVec, Matrix.smul_mulVec,
    dotProduct_add, dotProduct_smul, dotProduct_smul, quad_qd v horm, quad_qd v horm,
    smul_eq_mul, smul_eq_mul]

/-! ### Section C₃ — the corner analysis -/

/-- The direct corner coefficient of the image of a matrix unit. -/
def cA (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (v : n → n → ℂ) (i j : n) : ℂ :=
  star (v i) ⬝ᵥ (Φ (Eu i j) *ᵥ v j)

/-- The transposed corner coefficient. -/
def cB (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (v : n → n → ℂ) (i j : n) : ℂ :=
  star (v j) ⬝ᵥ (Φ (Eu i j) *ᵥ v i)

/-- **Corner localization**: the image of an off-diagonal matrix unit lives in the
two-dimensional span of the direct and transposed frame dyads. -/
theorem corner_form (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (hone : Φ 1 = 1)
    (v : n → n → ℂ) (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (hP : ∀ i, Φ (Eu i i) = qd v i i) {i j : n} (hij : i ≠ j) :
    Φ (Eu i j) = cA Φ v i j • qd v i j + cB Φ v i j • qd v j i := by
  have hqidem : ∀ a : n, qd v a a * qd v a a = qd v a a := fun a => by
    rw [qd_mul_qd v horm, if_pos rfl, one_smul]
  have hanti : ∀ k, k ≠ i → k ≠ j →
      qd v k k * Φ (Eu i j) + Φ (Eu i j) * qd v k k = 0 := by
    intro k hki hkj
    have h0 : Eu k k * Eu i j + Eu i j * Eu k k = 0 := by
      rw [Eu_mul_of_ne k hki j, Eu_mul_of_ne i (Ne.symm hkj) k, add_zero]
    have h := hj (Eu k k) (Eu i j)
    rw [h0, map_zero, hP k] at h
    exact h.symm
  have hkill : ∀ k, k ≠ i → k ≠ j →
      qd v k k * Φ (Eu i j) = 0 ∧ Φ (Eu i j) * qd v k k = 0 := by
    intro k hki hkj
    have h := hanti k hki hkj
    have h1 : qd v k k * Φ (Eu i j) + qd v k k * Φ (Eu i j) * qd v k k = 0 := by
      calc qd v k k * Φ (Eu i j) + qd v k k * Φ (Eu i j) * qd v k k
          = qd v k k * (qd v k k * Φ (Eu i j) + Φ (Eu i j) * qd v k k) := by
            rw [Matrix.mul_add, ← Matrix.mul_assoc, hqidem k, ← Matrix.mul_assoc]
        _ = 0 := by rw [h, Matrix.mul_zero]
    have h2 : qd v k k * Φ (Eu i j) * qd v k k + Φ (Eu i j) * qd v k k = 0 := by
      calc qd v k k * Φ (Eu i j) * qd v k k + Φ (Eu i j) * qd v k k
          = (qd v k k * Φ (Eu i j) + Φ (Eu i j) * qd v k k) * qd v k k := by
            rw [Matrix.add_mul, Matrix.mul_assoc (Φ (Eu i j)), hqidem k]
        _ = 0 := by rw [h, Matrix.zero_mul]
    have h3 : qd v k k * Φ (Eu i j) - Φ (Eu i j) * qd v k k = 0 := by
      have hd : qd v k k * Φ (Eu i j) - Φ (Eu i j) * qd v k k
          = (qd v k k * Φ (Eu i j) + qd v k k * Φ (Eu i j) * qd v k k)
            - (qd v k k * Φ (Eu i j) * qd v k k + Φ (Eu i j) * qd v k k) := by abel
      rw [hd, h1, h2, sub_zero]
    have h4 : (2 : ℂ) • (qd v k k * Φ (Eu i j)) = 0 := by
      rw [two_smul]
      calc qd v k k * Φ (Eu i j) + qd v k k * Φ (Eu i j)
          = qd v k k * Φ (Eu i j) + Φ (Eu i j) * qd v k k := by rw [sub_eq_zero.mp h3]
        _ = 0 := h
    have hL : qd v k k * Φ (Eu i j) = 0 :=
      (smul_eq_zero.mp h4).resolve_left (by norm_num)
    refine ⟨hL, ?_⟩
    have h5 := h
    rw [hL, zero_add] at h5
    exact h5
  have hdiag0 : ∀ a : n,
      qd v a a * Φ (Eu i j) + Φ (Eu i j) * qd v a a = Φ (Eu i j) →
      qd v a a * Φ (Eu i j) * qd v a a = 0 := by
    intro a hrel
    have h1 : qd v a a * Φ (Eu i j) * qd v a a + qd v a a * Φ (Eu i j) * qd v a a
        = qd v a a * Φ (Eu i j) * qd v a a := by
      calc qd v a a * Φ (Eu i j) * qd v a a + qd v a a * Φ (Eu i j) * qd v a a
          = qd v a a * (qd v a a * Φ (Eu i j) + Φ (Eu i j) * qd v a a) * qd v a a := by
            rw [Matrix.mul_add, Matrix.add_mul,
              ← Matrix.mul_assoc (qd v a a) (qd v a a) (Φ (Eu i j)), hqidem a,
              ← Matrix.mul_assoc (qd v a a) (Φ (Eu i j)) (qd v a a),
              Matrix.mul_assoc (qd v a a * Φ (Eu i j)) (qd v a a) (qd v a a), hqidem a]
        _ = qd v a a * Φ (Eu i j) * qd v a a := by rw [hrel]
    have h2 : qd v a a * Φ (Eu i j) * qd v a a + qd v a a * Φ (Eu i j) * qd v a a
        = qd v a a * Φ (Eu i j) * qd v a a + 0 := by
      rw [add_zero]
      exact h1
    exact add_left_cancel h2
  have hrel_i : qd v i i * Φ (Eu i j) + Φ (Eu i j) * qd v i i = Φ (Eu i j) := by
    have h0 : Eu i i * Eu i j + Eu i j * Eu i i = Eu i j := by
      rw [Eu_mul_same, Eu_mul_of_ne i (Ne.symm hij) i, add_zero]
    have h := hj (Eu i i) (Eu i j)
    rw [h0, hP i] at h
    exact h.symm
  have hrel_j : qd v j j * Φ (Eu i j) + Φ (Eu i j) * qd v j j = Φ (Eu i j) := by
    have h0 : Eu j j * Eu i j + Eu i j * Eu j j = Eu i j := by
      rw [Eu_mul_of_ne j (Ne.symm hij) j, Eu_mul_same, zero_add]
    have h := hj (Eu j j) (Eu i j)
    rw [h0, hP j] at h
    exact h.symm
  have hrow : Φ (Eu i j) = qd v i i * Φ (Eu i j) + qd v j j * Φ (Eu i j) := by
    have hsum1 : (∑ a, qd v a a) = (1 : Matrix n n ℂ) := by
      rw [← image_diag_sum Φ hone]
      exact Finset.sum_congr rfl fun a _ => (hP a).symm
    have h1 : Φ (Eu i j) = ∑ a, qd v a a * Φ (Eu i j) := by
      rw [← Finset.sum_mul, hsum1, Matrix.one_mul]
    conv_lhs => rw [h1]
    rw [← Finset.sum_subset (Finset.subset_univ {i, j})
      (fun x _ hx => (hkill x (fun h => hx (by rw [h]; exact Finset.mem_insert_self i _))
        (fun h => hx (by rw [h]; exact Finset.mem_insert_of_mem (Finset.mem_singleton_self j)))).1),
      Finset.sum_pair hij]
  have hcol : Φ (Eu i j) = Φ (Eu i j) * qd v i i + Φ (Eu i j) * qd v j j := by
    have hsum1 : (∑ a, qd v a a) = (1 : Matrix n n ℂ) := by
      rw [← image_diag_sum Φ hone]
      exact Finset.sum_congr rfl fun a _ => (hP a).symm
    have h1 : Φ (Eu i j) = ∑ a, Φ (Eu i j) * qd v a a := by
      rw [← Finset.mul_sum, hsum1, Matrix.mul_one]
    conv_lhs => rw [h1]
    rw [← Finset.sum_subset (Finset.subset_univ {i, j})
      (fun x _ hx => (hkill x (fun h => hx (by rw [h]; exact Finset.mem_insert_self i _))
        (fun h => hx (by rw [h]; exact Finset.mem_insert_of_mem (Finset.mem_singleton_self j)))).2),
      Finset.sum_pair hij]
  have hquad : Φ (Eu i j) = qd v i i * Φ (Eu i j) * qd v j j
      + qd v j j * Φ (Eu i j) * qd v i i := by
    calc Φ (Eu i j) = qd v i i * Φ (Eu i j) + qd v j j * Φ (Eu i j) := hrow
      _ = qd v i i * (Φ (Eu i j) * qd v i i + Φ (Eu i j) * qd v j j)
          + qd v j j * (Φ (Eu i j) * qd v i i + Φ (Eu i j) * qd v j j) := by rw [← hcol]
      _ = qd v i i * Φ (Eu i j) * qd v i i + qd v i i * Φ (Eu i j) * qd v j j
          + (qd v j j * Φ (Eu i j) * qd v i i + qd v j j * Φ (Eu i j) * qd v j j) := by
          rw [Matrix.mul_add, Matrix.mul_add,
            ← Matrix.mul_assoc (qd v i i) (Φ (Eu i j)) (qd v i i),
            ← Matrix.mul_assoc (qd v i i) (Φ (Eu i j)) (qd v j j),
            ← Matrix.mul_assoc (qd v j j) (Φ (Eu i j)) (qd v i i),
            ← Matrix.mul_assoc (qd v j j) (Φ (Eu i j)) (qd v j j)]
      _ = qd v i i * Φ (Eu i j) * qd v j j + qd v j j * Φ (Eu i j) * qd v i i := by
          rw [hdiag0 i hrel_i, hdiag0 j hrel_j, zero_add, add_zero]
  have hsand : ∀ a b : n, qd v a a * Φ (Eu i j) * qd v b b
      = (star (v a) ⬝ᵥ (Φ (Eu i j) *ᵥ v b)) • qd v a b := by
    intro a b
    rw [qd, qd, qd, Matrix.vecMulVec_mul, Matrix.vecMulVec_mul_vecMulVec,
      Matrix.vecMulVec_smul, ← dotProduct_mulVec]
  rw [hquad, hsand i j, hsand j i]
  rfl

/-- The images of matrix units act on the frame by the corner coefficients. -/
theorem corner_mulVec (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (hone : Φ 1 = 1)
    (v : n → n → ℂ) (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (hP : ∀ i, Φ (Eu i i) = qd v i i) {i j : n} (hij : i ≠ j) :
    Φ (Eu i j) *ᵥ v j = cA Φ v i j • v i
      ∧ Φ (Eu i j) *ᵥ v i = cB Φ v i j • v j
      ∧ ∀ k, k ≠ i → k ≠ j → Φ (Eu i j) *ᵥ v k = 0 := by
  have hform := corner_form Φ hj hone v horm hP hij
  have hev : ∀ k, Φ (Eu i j) *ᵥ v k
      = (cA Φ v i j * if j = k then 1 else 0) • v i
        + (cB Φ v i j * if i = k then 1 else 0) • v j := by
    intro k
    rw [hform, Matrix.add_mulVec, Matrix.smul_mulVec, Matrix.smul_mulVec,
      qd_mulVec v horm, qd_mulVec v horm, smul_smul, smul_smul]
  refine ⟨?_, ?_, ?_⟩
  · rw [hev j, if_pos rfl, if_neg hij, mul_one, mul_zero, zero_smul, add_zero]
  · rw [hev i, if_neg (Ne.symm hij), if_pos rfl, mul_one, mul_zero, zero_smul, zero_add]
  · intro k hki hkj
    rw [hev k, if_neg (fun h => hkj (h.symm)), if_neg (fun h => hki (h.symm)),
      mul_zero, mul_zero, zero_smul, zero_smul, add_zero]

omit [DecidableEq n] in
/-- Adjoint transport of the quadratic pairing. -/
theorem dot_conj (M : Matrix n n ℂ) (x y : n → ℂ) :
    star x ⬝ᵥ (Mᴴ *ᵥ y) = star (star y ⬝ᵥ (M *ᵥ x)) := by
  rw [dotProduct, dotProduct, star_sum]
  rw [Finset.sum_congr rfl fun q _ => by
    rw [Pi.star_apply, Matrix.mulVec, dotProduct, Finset.mul_sum]]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [star_mul', Pi.star_apply, star_star, Matrix.mulVec, dotProduct, star_sum,
    Finset.mul_sum]
  refine Finset.sum_congr rfl fun q _ => ?_
  rw [star_mul', Matrix.conjTranspose_apply]
  ring

/-- Star-preservation turns index swap into conjugation of both corner coefficients. -/
theorem corner_conj (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hstar : ∀ X : Matrix n n ℂ, Φ Xᴴ = (Φ X)ᴴ) (v : n → n → ℂ) (i j : n) :
    cA Φ v j i = star (cA Φ v i j) ∧ cB Φ v j i = star (cB Φ v i j) := by
  have hF : Φ (Eu j i) = (Φ (Eu i j))ᴴ := by
    rw [← hstar, Eu_conjTranspose]
  constructor
  · rw [cA, cA, hF, dot_conj]
  · rw [cB, cB, hF, dot_conj]

/-- **Corner nilpotency**: the direct and transposed coefficients cannot both live. -/
theorem corner_nilpotent (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (hone : Φ 1 = 1)
    (v : n → n → ℂ) (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (hP : ∀ i, Φ (Eu i i) = qd v i i) {i j : n} (hij : i ≠ j) :
    cA Φ v i j * cB Φ v i j = 0 := by
  obtain ⟨hA, hB, _⟩ := corner_mulVec Φ hj hone v horm hP hij
  have h0 : Eu i j * Eu i j + Eu i j * Eu i j = 0 := by
    rw [Eu_mul_of_ne i (Ne.symm hij) j, add_zero]
  have h := hj (Eu i j) (Eu i j)
  rw [h0, map_zero] at h
  have hFF : Φ (Eu i j) * Φ (Eu i j) = 0 := by
    have h4 : (2 : ℂ) • (Φ (Eu i j) * Φ (Eu i j)) = 0 := by
      rw [two_smul]
      exact h.symm
    exact (smul_eq_zero.mp h4).resolve_left (by norm_num)
  have hval : star (v i) ⬝ᵥ ((Φ (Eu i j) * Φ (Eu i j)) *ᵥ v i)
      = cB Φ v i j * cA Φ v i j := by
    rw [← Matrix.mulVec_mulVec, hB, Matrix.mulVec_smul, hA, smul_smul,
      dotProduct_smul, horm, if_pos rfl, smul_eq_mul, mul_one]
  rw [hFF, Matrix.zero_mulVec, dotProduct_zero] at hval
  rw [mul_comm]
  exact hval.symm

/-- **Corner unimodularity**: `|α|² + |β|² = 1` at every corner. -/
theorem corner_unimodular (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hstar : ∀ X : Matrix n n ℂ, Φ Xᴴ = (Φ X)ᴴ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (hone : Φ 1 = 1)
    (v : n → n → ℂ) (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (hP : ∀ i, Φ (Eu i i) = qd v i i) {i j : n} (hij : i ≠ j) :
    cA Φ v i j * star (cA Φ v i j) + cB Φ v i j * star (cB Φ v i j) = 1 := by
  obtain ⟨hAij, hBij, _⟩ := corner_mulVec Φ hj hone v horm hP hij
  obtain ⟨hAji, hBji, _⟩ := corner_mulVec Φ hj hone v horm hP (Ne.symm hij)
  have h0 : Eu i j * Eu j i + Eu j i * Eu i j = Eu i i + Eu j j := by
    rw [Eu_mul_same, Eu_mul_same]
  have h := hj (Eu i j) (Eu j i)
  rw [h0, map_add, hP i, hP j] at h
  have hval : star (v i) ⬝ᵥ ((Φ (Eu i j) * Φ (Eu j i) + Φ (Eu j i) * Φ (Eu i j)) *ᵥ v i)
      = cA Φ v j i * cA Φ v i j + cB Φ v i j * cB Φ v j i := by
    rw [Matrix.add_mulVec, ← Matrix.mulVec_mulVec, ← Matrix.mulVec_mulVec,
      hAji, Matrix.mulVec_smul, hAij, hBij, Matrix.mulVec_smul, hBji,
      smul_smul, smul_smul, dotProduct_add, dotProduct_smul, dotProduct_smul,
      horm, if_pos rfl, smul_eq_mul, smul_eq_mul, mul_one, mul_one]
  have hrhs : star (v i) ⬝ᵥ ((qd v i i + qd v j j) *ᵥ v i) = 1 := by
    rw [Matrix.add_mulVec, qd_mulVec v horm, qd_mulVec v horm, if_pos rfl,
      if_neg (Ne.symm hij), one_smul, zero_smul, add_zero, horm, if_pos rfl]
  rw [h, hval] at hrhs
  obtain ⟨hcA, hcB⟩ := corner_conj Φ hstar v i j
  rw [hcA, hcB] at hrhs
  calc cA Φ v i j * star (cA Φ v i j) + cB Φ v i j * star (cB Φ v i j)
      = star (cA Φ v i j) * cA Φ v i j + cB Φ v i j * star (cB Φ v i j) := by ring
    _ = 1 := hrhs

/-- **The corner cocycle** across a triple. -/
theorem corner_cocycle (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (hone : Φ 1 = 1)
    (v : n → n → ℂ) (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (hP : ∀ i, Φ (Eu i i) = qd v i i) {i j k : n}
    (hij : i ≠ j) (hjk : j ≠ k) (hik : i ≠ k) :
    cA Φ v i k = cA Φ v i j * cA Φ v j k ∧ cB Φ v i k = cB Φ v i j * cB Φ v j k := by
  obtain ⟨hAij, hBij, hZij⟩ := corner_mulVec Φ hj hone v horm hP hij
  obtain ⟨hAjk, hBjk, hZjk⟩ := corner_mulVec Φ hj hone v horm hP hjk
  have h0 : Eu i j * Eu j k + Eu j k * Eu i j = Eu i k := by
    rw [Eu_mul_same, Eu_mul_of_ne j (Ne.symm hik) j, add_zero]
  have h := hj (Eu i j) (Eu j k)
  rw [h0] at h
  constructor
  · have hval : star (v i) ⬝ᵥ (Φ (Eu i k) *ᵥ v k) = cA Φ v i j * cA Φ v j k := by
      rw [h, Matrix.add_mulVec, ← Matrix.mulVec_mulVec, ← Matrix.mulVec_mulVec,
        hAjk, Matrix.mulVec_smul, hAij, hZij k (Ne.symm hik) (Ne.symm hjk),
        Matrix.mulVec_zero, smul_smul, add_zero, dotProduct_smul, horm, if_pos rfl,
        smul_eq_mul, mul_one, mul_comm]
    exact hval
  · have hval : star (v k) ⬝ᵥ (Φ (Eu i k) *ᵥ v i) = cB Φ v i j * cB Φ v j k := by
      rw [h, Matrix.add_mulVec, ← Matrix.mulVec_mulVec, ← Matrix.mulVec_mulVec,
        hZjk i hij hik, Matrix.mulVec_zero, zero_add,
        hBij, Matrix.mulVec_smul, hBjk, smul_smul, dotProduct_smul, horm, if_pos rfl,
        smul_eq_mul, mul_one]
    exact hval

/-- **TRIPLE COHERENCE — the global orientation dichotomy.** A single transposed corner
forces every corner transposed: mixed orientations would make some corner carry neither
coefficient, contradicting unimodularity. Probe F19's mixed-orientation map violates the
Jordan identity at the triple, exactly as this propagation demands. -/
theorem orientation_dichotomy (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hstar : ∀ X : Matrix n n ℂ, Φ Xᴴ = (Φ X)ᴴ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A)
    (hone : Φ 1 = 1)
    (v : n → n → ℂ) (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (hP : ∀ i, Φ (Eu i i) = qd v i i) :
    (∀ i j, i ≠ j → cB Φ v i j = 0) ∨ (∀ i j, i ≠ j → cA Φ v i j = 0) := by
  by_cases hall : ∀ i j, i ≠ j → cB Φ v i j = 0
  · exact Or.inl hall
  · push Not at hall
    obtain ⟨i, j, hij, hB⟩ := hall
    have hAij : cA Φ v i j = 0 :=
      (mul_eq_zero.mp (corner_nilpotent Φ hj hone v horm hP hij)).resolve_right hB
    refine Or.inr ?_
    have hconj0 : ∀ a b, cA Φ v a b = 0 → cA Φ v b a = 0 := by
      intro a b h0
      rw [(corner_conj Φ hstar v a b).1, h0, star_zero]
    have hprop : ∀ a b c, a ≠ b → b ≠ c → a ≠ c → cA Φ v a b = 0 → cA Φ v b c = 0 := by
      intro a b c hab hbc hac h0
      by_contra hbc0
      have hBbc : cB Φ v b c = 0 :=
        (mul_eq_zero.mp (corner_nilpotent Φ hj hone v horm hP hbc)).resolve_left hbc0
      obtain ⟨hcA, hcB⟩ := corner_cocycle Φ hj hone v horm hP hab hbc hac
      have huni := corner_unimodular Φ hstar hj hone v horm hP hac
      rw [hcA, hcB, h0, hBbc, zero_mul, mul_zero] at huni
      simp at huni
    have hprop' : ∀ a b c, a ≠ b → a ≠ c → b ≠ c → cA Φ v a b = 0 → cA Φ v a c = 0 := by
      intro a b c hab hac hbc h0
      exact hprop b a c (Ne.symm hab) hac hbc (hconj0 a b h0)
    intro k l hkl
    by_cases hki : k = i
    · by_cases hlj : l = j
      · rw [hki, hlj]
        exact hAij
      · rw [hki]
        refine hprop' i j l hij ?_ (Ne.symm hlj) hAij
        rw [← hki]
        exact hkl
    · by_cases hkj : k = j
      · by_cases hli : l = i
        · rw [hkj, hli]
          exact hconj0 i j hAij
        · rw [hkj]
          refine hprop i j l hij ?_ (Ne.symm hli) hAij
          rw [← hkj]
          exact hkl
      · have hAik : cA Φ v i k = 0 :=
          hprop' i j k hij (Ne.symm hki) (Ne.symm hkj) hAij
        by_cases hli : l = i
        · rw [hli]
          exact hconj0 i k hAik
        · exact hprop i k l (Ne.symm hki) hkl (Ne.symm hli) hAik

/-! ### Section C₄ — the unitary assembly -/

omit [Fintype n] in
theorem Eu_transpose (i j : n) : (Eu i j)ᵀ = Eu j i := by
  ext a b
  rw [Matrix.transpose_apply, Eu, Eu, Matrix.single_apply, Matrix.single_apply]
  by_cases hc : i = b ∧ j = a
  · rw [if_pos hc, if_pos ⟨hc.2, hc.1⟩]
  · rw [if_neg hc, if_neg (fun h => hc ⟨h.2, h.1⟩)]

theorem matrix_eq_sum_units (X : Matrix n n ℂ) : X = ∑ i, ∑ j, X i j • Eu i j := by
  conv_lhs => rw [Matrix.matrix_eq_sum_single X]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
  rw [Eu, Matrix.smul_single, smul_eq_mul, mul_one]

omit [DecidableEq n] in
theorem W_col (v : n → n → ℂ) (c : n → ℂ) (i : n) [DecidableEq n] :
    (Matrix.of fun x k => c k * v k x) *ᵥ Pi.single i 1 = c i • v i := by
  ext x
  rw [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul]
  rw [Finset.sum_eq_single i (fun b _ hb => by rw [Pi.single_eq_of_ne hb, mul_zero])
    (fun hi => absurd (Finset.mem_univ i) hi)]
  rw [Pi.single_eq_same, mul_one, Matrix.of_apply]

omit [DecidableEq n] in
theorem W_row (v : n → n → ℂ) (c : n → ℂ) (j : n) [DecidableEq n] :
    Pi.single j (1 : ℂ) ᵥ* (Matrix.of fun x k => c k * v k x)ᴴ
      = star (c j) • star (v j) := by
  ext y
  rw [Matrix.vecMul, dotProduct, Pi.smul_apply, smul_eq_mul]
  rw [Finset.sum_eq_single j (fun b _ hb => by rw [Pi.single_eq_of_ne hb, zero_mul])
    (fun hj => absurd (Finset.mem_univ j) hj)]
  rw [Pi.single_eq_same, one_mul, Matrix.conjTranspose_apply, Matrix.of_apply,
    star_mul', Pi.star_apply]

/-- Conjugating a matrix unit by the phased frame matrix. -/
theorem conj_unit (v : n → n → ℂ) (c : n → ℂ) (i j : n) :
    (Matrix.of fun x k => c k * v k x) * Eu i j * (Matrix.of fun x k => c k * v k x)ᴴ
      = (c i * star (c j)) • qd v i j := by
  rw [show Eu i j = Matrix.vecMulVec (Pi.single i 1) (Pi.single j 1) from
    Matrix.single_eq_single_vecMulVec_single i j]
  rw [Matrix.mul_vecMulVec, Matrix.vecMulVec_mul, W_col, W_row]
  rw [Matrix.smul_vecMulVec, Matrix.vecMulVec_smul, smul_smul, qd]

/-- The phased frame matrix is a coisometry when the phases are unimodular. -/
theorem W_unitary (v : n → n → ℂ)
    (horm : ∀ i j, star (v i) ⬝ᵥ v j = if i = j then 1 else 0)
    (c : n → ℂ) (hc : ∀ i, c i * star (c i) = 1) :
    (Matrix.of fun x k => c k * v k x)ᴴ * (Matrix.of fun x k => c k * v k x) = 1 := by
  ext k l
  rw [Matrix.mul_apply, Matrix.one_apply]
  rw [show ∑ x, ((Matrix.of fun x k => c k * v k x)ᴴ) k x
      * (Matrix.of fun x k => c k * v k x) x l
      = star (c k) * c l * (star (v k) ⬝ᵥ v l) from by
    rw [dotProduct, Finset.mul_sum]
    refine Finset.sum_congr rfl fun x _ => ?_
    rw [Matrix.conjTranspose_apply, Matrix.of_apply, Matrix.of_apply, star_mul',
      Pi.star_apply]
    ring]
  rw [horm]
  by_cases hkl : k = l
  · subst hkl
    rw [if_pos rfl, mul_one, mul_comm]
    exact hc k
  · rw [if_neg hkl, mul_zero]

/-- **THE MATRIX-UNIT CLASSIFICATION (C3b).** A ℂ-linear, unital, star-preserving,
injective Jordan homomorphism of `M_D(ℂ)` is conjugation by a unitary, or transpose
followed by conjugation by a unitary: `Φ(X) = WXW†` or `Φ(X) = WX^TW†`. The frame comes
from the rank-one resolution of the diagonal images, the orientation from triple
coherence, and the phases from the corner coboundary `α_ij = d_i · conj d_j` — the same
local-freedom → triple-consistency → global-orientation → phase-coboundary architecture
as the Hamiltonian reconstruction. -/
theorem matrixJordan_unitary_or_transpose
    (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ)
    (hstar : ∀ X : Matrix n n ℂ, Φ Xᴴ = (Φ X)ᴴ)
    (hone : Φ 1 = 1) (hinj : Function.Injective Φ)
    (hj : ∀ A B : Matrix n n ℂ, Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A) :
    ∃ W : Matrix n n ℂ, Wᴴ * W = 1 ∧
      ((∀ X, Φ X = W * X * Wᴴ) ∨ (∀ X, Φ X = W * Xᵀ * Wᴴ)) := by
  by_cases hne : Nonempty n
  · obtain ⟨i₀⟩ := hne
    obtain ⟨v, horm, hPvec⟩ := orthogonal_resolution_rank_one (fun i => Φ (Eu i i))
      (fun i => (image_diag_proj Φ hstar hj i).1)
      (fun i => (image_diag_proj Φ hstar hj i).2)
      (fun i j hij => image_diag_orth Φ hstar hj hij)
      (image_diag_sum Φ hone) (fun i => image_diag_ne Φ hinj i)
    have hP : ∀ i, Φ (Eu i i) = qd v i i := fun i => hPvec i
    rcases orientation_dichotomy Φ hstar hj hone v horm hP with hbr | hbr
    · -- the unitary branch
      have hc : ∀ i, (if i = i₀ then (1 : ℂ) else cA Φ v i i₀)
          * star (if i = i₀ then (1 : ℂ) else cA Φ v i i₀) = 1 := by
        intro i
        by_cases hi : i = i₀
        · rw [if_pos hi]
          norm_num
        · rw [if_neg hi]
          have huni := corner_unimodular Φ hstar hj hone v horm hP hi
          rw [hbr i i₀ hi, star_zero, mul_zero, add_zero] at huni
          exact huni
      refine ⟨Matrix.of fun x k => (if k = i₀ then (1 : ℂ) else cA Φ v k i₀) * v k x,
        W_unitary v horm _ hc, Or.inl ?_⟩
      have hunit : ∀ i j, Φ (Eu i j)
          = (Matrix.of fun x k => (if k = i₀ then (1 : ℂ) else cA Φ v k i₀) * v k x)
            * Eu i j
            * (Matrix.of fun x k => (if k = i₀ then (1 : ℂ) else cA Φ v k i₀) * v k x)ᴴ := by
        intro i j
        rw [conj_unit]
        by_cases hij : i = j
        · rw [hij, hP j, hc j, one_smul]
        · rw [corner_form Φ hj hone v horm hP hij, hbr i j hij, zero_smul, add_zero]
          congr 1
          by_cases hi : i = i₀
          · rw [hi, if_pos rfl, one_mul, if_neg (fun h => hij (hi.trans h.symm)),
              (corner_conj Φ hstar v i₀ j).1, star_star]
          · by_cases hjq : j = i₀
            · rw [hjq, if_neg hi, if_pos rfl, star_one, mul_one]
            · rw [if_neg hi, if_neg hjq, (corner_conj Φ hstar v i₀ j).1, star_star]
              exact (corner_cocycle Φ hj hone v horm hP hi (Ne.symm hjq) hij).1
      intro X
      trans (∑ i, ∑ j, X i j • Φ (Eu i j))
      · conv_lhs => rw [matrix_eq_sum_units X]
        rw [map_sum]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [map_sum]
        exact Finset.sum_congr rfl fun j _ => map_smul Φ _ _
      · conv_rhs => rw [matrix_eq_sum_units X]
        rw [Matrix.mul_sum, Finset.sum_mul]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Matrix.mul_sum, Finset.sum_mul]
        refine Finset.sum_congr rfl fun j _ => ?_
        rw [Matrix.mul_smul, Matrix.smul_mul, hunit i j]
    · -- the transpose branch
      have hc : ∀ i, (if i = i₀ then (1 : ℂ) else star (cB Φ v i i₀))
          * star (if i = i₀ then (1 : ℂ) else star (cB Φ v i i₀)) = 1 := by
        intro i
        by_cases hi : i = i₀
        · rw [if_pos hi]
          norm_num
        · rw [if_neg hi, star_star]
          have huni := corner_unimodular Φ hstar hj hone v horm hP hi
          rw [hbr i i₀ hi, star_zero, mul_zero, zero_add] at huni
          rw [mul_comm]
          exact huni
      refine ⟨Matrix.of fun x k => (if k = i₀ then (1 : ℂ) else star (cB Φ v k i₀)) * v k x,
        W_unitary v horm _ hc, Or.inr ?_⟩
      have hunit : ∀ i j, Φ (Eu i j)
          = (Matrix.of fun x k => (if k = i₀ then (1 : ℂ) else star (cB Φ v k i₀)) * v k x)
            * Eu j i
            * (Matrix.of fun x k =>
                (if k = i₀ then (1 : ℂ) else star (cB Φ v k i₀)) * v k x)ᴴ := by
        intro i j
        rw [conj_unit]
        by_cases hij : i = j
        · rw [hij, hP j, hc j, one_smul]
        · rw [corner_form Φ hj hone v horm hP hij, hbr i j hij, zero_smul, zero_add]
          congr 1
          by_cases hi : i = i₀
          · rw [hi, if_pos rfl, star_one, mul_one,
              if_neg (fun h => hij (hi.trans h.symm)),
              (corner_conj Φ hstar v i₀ j).2, star_star]
          · by_cases hjq : j = i₀
            · rw [hjq, if_pos rfl, if_neg hi, one_mul, star_star]
            · rw [if_neg hi, if_neg hjq, star_star,
                (show star (cB Φ v j i₀) = cB Φ v i₀ j from by
                  rw [(corner_conj Φ hstar v i₀ j).2, star_star]), mul_comm]
              exact (corner_cocycle Φ hj hone v horm hP hi (Ne.symm hjq) hij).2
      intro X
      have hXt : Xᵀ = ∑ i, ∑ j, X i j • Eu j i := by
        conv_lhs => rw [matrix_eq_sum_units X]
        rw [Matrix.transpose_sum]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Matrix.transpose_sum]
        refine Finset.sum_congr rfl fun j _ => ?_
        rw [Matrix.transpose_smul, Eu_transpose]
      trans (∑ i, ∑ j, X i j • Φ (Eu i j))
      · conv_lhs => rw [matrix_eq_sum_units X]
        rw [map_sum]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [map_sum]
        exact Finset.sum_congr rfl fun j _ => map_smul Φ _ _
      · rw [hXt, Matrix.mul_sum, Finset.sum_mul]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Matrix.mul_sum, Finset.sum_mul]
        refine Finset.sum_congr rfl fun j _ => ?_
        rw [Matrix.mul_smul, Matrix.smul_mul, hunit i j]
  · have hIE : IsEmpty n := not_nonempty_iff.mp hne
    refine ⟨1, by rw [Matrix.conjTranspose_one, Matrix.one_mul], Or.inl fun X => ?_⟩
    ext i j
    exact (hIE.false i).elim

/-! ### Section D — the C3b.3 assembly -/

/-- **THE ASSEMBLY (C3b.3).** Two completions with identical pairing data, Hermitian
spanning contexts including the trivial one, separating accessible states, and full
accessible cones induce mutually inverse ℂ-linear maps matching every context — the
full two-sided order-isomorphism package. Bijectivity comes from the symmetric
operational construction, positivity from transfer + cone + self-duality, star
preservation by span induction over the Hermitian contexts. -/
theorem sameData_orderIso {ι κ : Type*}
    (G₁ G₂ : ι → Matrix n n ℂ) (σ₁ σ₂ : κ → Matrix n n ℂ)
    (hdata : ∀ i k, Matrix.trace (G₁ i * σ₁ k) = Matrix.trace (G₂ i * σ₂ k))
    (hG₁h : ∀ i, (G₁ i).IsHermitian) (hG₂h : ∀ i, (G₂ i).IsHermitian)
    (hσ₁p : ∀ k, (σ₁ k).PosSemidef) (hσ₂p : ∀ k, (σ₂ k).PosSemidef)
    (hspan₁ : Submodule.span ℂ (Set.range G₁) = ⊤)
    (hspan₂ : Submodule.span ℂ (Set.range G₂) = ⊤)
    (hsep₁ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₁ k) = 0) → M = 0)
    (hsep₂ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₂ k) = 0) → M = 0)
    (i₀ : ι) (hone₁ : G₁ i₀ = 1) (hone₂ : G₂ i₀ = 1)
    (hcone₁ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₁ k)
    (hcone₂ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₂ k) :
    ∃ Φ Ψ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ,
      (∀ i, Φ (G₁ i) = G₂ i) ∧ (∀ i, Ψ (G₂ i) = G₁ i)
        ∧ OrderIsoHyp (⇑Φ) (⇑Ψ) := by
  have htrans₁ : ∀ l : ι →₀ ℂ, Finsupp.linearCombination ℂ G₁ l = 0 →
      Finsupp.linearCombination ℂ G₂ l = 0 := by
    intro l hl
    rw [Finsupp.linearCombination_apply, Finsupp.sum] at hl ⊢
    exact sameData_combination_transfer G₁ G₂ σ₁ σ₂ hdata hsep₂ l.support l hl
  have htrans₂ : ∀ l : ι →₀ ℂ, Finsupp.linearCombination ℂ G₂ l = 0 →
      Finsupp.linearCombination ℂ G₁ l = 0 := by
    intro l hl
    rw [Finsupp.linearCombination_apply, Finsupp.sum] at hl ⊢
    exact sameData_combination_transfer G₂ G₁ σ₂ σ₁ (fun i k => (hdata i k).symm)
      hsep₁ l.support l hl
  obtain ⟨Φ, hΦ⟩ := sameData_linear_extension G₁ G₂ hspan₁ htrans₁
  obtain ⟨Ψ, hΨ⟩ := sameData_linear_extension G₂ G₁ hspan₂ htrans₂
  have hmem₁ : ∀ X : Matrix n n ℂ, X ∈ Submodule.span ℂ (Set.range G₁) := by
    intro X
    rw [hspan₁]
    exact Submodule.mem_top
  have hmem₂ : ∀ X : Matrix n n ℂ, X ∈ Submodule.span ℂ (Set.range G₂) := by
    intro X
    rw [hspan₂]
    exact Submodule.mem_top
  have hΨΦ : ∀ X, Ψ (Φ X) = X := by
    intro X
    induction hmem₁ X using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [hΦ i, hΨ i]
    | zero => rw [map_zero, map_zero]
    | add x y _ _ ihx ihy => rw [map_add, map_add, ihx, ihy]
    | smul c x _ ih => rw [map_smul, map_smul, ih]
  have hΦΨ : ∀ X, Φ (Ψ X) = X := by
    intro X
    induction hmem₂ X using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [hΨ i, hΦ i]
    | zero => rw [map_zero, map_zero]
    | add x y _ _ ihx ihy => rw [map_add, map_add, ihx, ihy]
    | smul c x _ ih => rw [map_smul, map_smul, ih]
  have hstarΦ : ∀ X : Matrix n n ℂ, Φ Xᴴ = (Φ X)ᴴ := by
    intro X
    induction hmem₁ X using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [hG₁h i, hΦ i]
      exact (hG₂h i).symm
    | zero => rw [Matrix.conjTranspose_zero, map_zero, Matrix.conjTranspose_zero]
    | add x y _ _ ihx ihy =>
      rw [Matrix.conjTranspose_add, map_add, ihx, ihy, map_add,
        Matrix.conjTranspose_add]
    | smul c x _ ih =>
      rw [Matrix.conjTranspose_smul, map_smul, ih, map_smul, Matrix.conjTranspose_smul]
  have hstarΨ : ∀ X : Matrix n n ℂ, Ψ Xᴴ = (Ψ X)ᴴ := by
    intro X
    induction hmem₂ X using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [hG₂h i, hΨ i]
      exact (hG₁h i).symm
    | zero => rw [Matrix.conjTranspose_zero, map_zero, Matrix.conjTranspose_zero]
    | add x y _ _ ihx ihy =>
      rw [Matrix.conjTranspose_add, map_add, ihx, ihy, map_add,
        Matrix.conjTranspose_add]
    | smul c x _ ih =>
      rw [Matrix.conjTranspose_smul, map_smul, ih, map_smul, Matrix.conjTranspose_smul]
  have hpair₁ : ∀ (X : Matrix n n ℂ) (k : κ),
      Matrix.trace (Φ X * σ₂ k) = Matrix.trace (X * σ₁ k) := by
    intro X k
    induction hmem₁ X using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [hΦ i]
      exact (hdata i k).symm
    | zero => rw [map_zero, Matrix.zero_mul, Matrix.zero_mul]
    | add x y _ _ ihx ihy =>
      rw [map_add, Matrix.add_mul, Matrix.add_mul, Matrix.trace_add, Matrix.trace_add,
        ihx, ihy]
    | smul c x _ ih =>
      rw [map_smul, Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul,
        Matrix.trace_smul, ih]
  have hpair₂ : ∀ (Y : Matrix n n ℂ) (k : κ),
      Matrix.trace (Ψ Y * σ₁ k) = Matrix.trace (Y * σ₂ k) := by
    intro Y k
    induction hmem₂ Y using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [hΨ i]
      exact hdata i k
    | zero => rw [map_zero, Matrix.zero_mul, Matrix.zero_mul]
    | add x y _ _ ihx ihy =>
      rw [map_add, Matrix.add_mul, Matrix.add_mul, Matrix.trace_add, Matrix.trace_add,
        ihx, ihy]
    | smul c x _ ih =>
      rw [map_smul, Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul,
        Matrix.trace_smul, ih]
  have hposΦ : ∀ X : Matrix n n ℂ, X.PosSemidef → (Φ X).PosSemidef := by
    intro X hX
    have hherm : (Φ X).IsHermitian := by
      show (Φ X)ᴴ = Φ X
      rw [← hstarΦ X, hX.1]
    rw [psd_iff_trace_nonneg hherm]
    intro τ hτ
    obtain ⟨s, cc, hcc, rfl⟩ := hcone₂ τ hτ
    rw [Matrix.mul_sum, Matrix.trace_sum]
    refine Finset.sum_nonneg fun k _ => ?_
    rw [Matrix.mul_smul, Matrix.trace_smul, hpair₁ X k, Complex.real_smul]
    exact cx_mul_nonneg (Complex.zero_le_real.mpr (hcc k))
      (psd_trace_mul_nonneg hX (hσ₁p k))
  have hposΨ : ∀ Y : Matrix n n ℂ, Y.PosSemidef → (Ψ Y).PosSemidef := by
    intro Y hY
    have hherm : (Ψ Y).IsHermitian := by
      show (Ψ Y)ᴴ = Ψ Y
      rw [← hstarΨ Y, hY.1]
    rw [psd_iff_trace_nonneg hherm]
    intro τ hτ
    obtain ⟨s, cc, hcc, rfl⟩ := hcone₁ τ hτ
    rw [Matrix.mul_sum, Matrix.trace_sum]
    refine Finset.sum_nonneg fun k _ => ?_
    rw [Matrix.mul_smul, Matrix.trace_smul, hpair₂ Y k, Complex.real_smul]
    exact cx_mul_nonneg (Complex.zero_le_real.mpr (hcc k))
      (psd_trace_mul_nonneg hY (hσ₂p k))
  refine ⟨Φ, Ψ, hΦ, hΨ, ?_⟩
  exact
    { add := fun X Y => map_add Φ X Y
      smul := fun r X => by
        rw [real_smul_matrix, map_smul, ← real_smul_matrix]
      star := hstarΦ
      one := by
        conv_lhs => rw [← hone₁]
        rw [hΦ i₀, hone₂]
      pos := hposΦ
      posInv := hposΨ
      left := hΨΦ
      right := hΦΨ }

/-- **THE C3b CLASSIFICATION.** Any two existing OI-compatible coherent completions with
the same complete operational data are unitary or antiunitary equivalent: the
data-defined map exists, is a two-sided order isomorphism, hence Jordan (round six),
hence — by the matrix-unit classification — conjugation by a unitary `W`, directly or
through the transpose. Which branch is physical is C3c: phase two's oriented complex
reference is the lever that removes the transpose. -/
theorem sameData_unitary_or_transpose {ι κ : Type*}
    (G₁ G₂ : ι → Matrix n n ℂ) (σ₁ σ₂ : κ → Matrix n n ℂ)
    (hdata : ∀ i k, Matrix.trace (G₁ i * σ₁ k) = Matrix.trace (G₂ i * σ₂ k))
    (hG₁h : ∀ i, (G₁ i).IsHermitian) (hG₂h : ∀ i, (G₂ i).IsHermitian)
    (hσ₁p : ∀ k, (σ₁ k).PosSemidef) (hσ₂p : ∀ k, (σ₂ k).PosSemidef)
    (hspan₁ : Submodule.span ℂ (Set.range G₁) = ⊤)
    (hspan₂ : Submodule.span ℂ (Set.range G₂) = ⊤)
    (hsep₁ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₁ k) = 0) → M = 0)
    (hsep₂ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₂ k) = 0) → M = 0)
    (i₀ : ι) (hone₁ : G₁ i₀ = 1) (hone₂ : G₂ i₀ = 1)
    (hcone₁ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₁ k)
    (hcone₂ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₂ k) :
    ∃ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
      (∀ i, Φ (G₁ i) = G₂ i) ∧ Wᴴ * W = 1 ∧
      ((∀ X, Φ X = W * X * Wᴴ) ∨ (∀ X, Φ X = W * Xᵀ * Wᴴ)) := by
  obtain ⟨Φ, Ψ, hΦ, hΨ, hiso⟩ := sameData_orderIso G₁ G₂ σ₁ σ₂ hdata hG₁h hG₂h
    hσ₁p hσ₂p hspan₁ hspan₂ hsep₁ hsep₂ i₀ hone₁ hone₂ hcone₁ hcone₂
  have hjall := jordan_complexify Φ (fun A B hA hB => orderIso_jordan hiso hA hB)
  have hinj : Function.Injective Φ :=
    Function.LeftInverse.injective (g := ⇑Ψ) hiso.left
  obtain ⟨W, hW, hbr⟩ := matrixJordan_unitary_or_transpose Φ hiso.star hiso.one hinj hjall
  exact ⟨Φ, W, hΦ, hW, hbr⟩

#print axioms psd_iff_trace_nonneg
#print axioms jordan_complexify
#print axioms orthogonal_resolution_rank_one
#print axioms corner_form
#print axioms corner_nilpotent
#print axioms corner_unimodular
#print axioms corner_cocycle
#print axioms orientation_dichotomy
#print axioms matrixJordan_unitary_or_transpose
#print axioms sameData_orderIso
#print axioms sameData_unitary_or_transpose

end JordanClassification
end OIBridge
