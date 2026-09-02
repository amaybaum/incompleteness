/-
  OIBridge/ClosureObstruction.lean — iterated ancilla closure is INDEPENDENT of everything
  established so far: a theory that is exactly quantum on the system, has every composite
  unitary, inert-spectator compositionality and composite Kraus soundness, yet has NO shifted
  theory at level two and fails composite completeness.

  ROUND THIRTY-EIGHT, PART TWO. Part one's audit left two fields of the shifted theory
  unfilled — fresh-ancilla attachment to a composite base and discard back to it — and
  packaged them as `IteratedAncillaClosure`. This file kernelizes the obstruction: those
  fields cannot be filled from the existing rules plus the round-37 conditions. The
  countermodel is `admissibleTheory`, whose composite families are Kraus sums whose every
  operator is either a scalar multiple of a unitary or factors through a space of at most
  HALF the composite dimension. That class contains every unitary, every readout selector
  (rank `|A|` = half of `2N` when `N ≥ 2`... in general rank `|A| ≤ |A|·N/2`), is closed
  under sums, composition and spectator extension (the bound scales with the level), and
  hence satisfies every structure rule, control, inert-spectator compositionality and
  composite soundness. It does NOT contain the amplitude-damping channel on the ancilla
  qubit at level two: its Kraus decompositions all contain an INVERTIBLE operator that is not
  a unitary multiple (rank four, bound two) — and that channel is exactly what a shifted
  theory with composite unitary control would produce by the round-25 circuit with an
  explicit rational dilation unitary.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `admissible_no_shift`: no `T' : FiniteOperationalTheory (Fin 2 × Fin 2)` with   │
      │    `T'.avail = admissibleTheory.availExt 2` and composite unitary control exists. │
      │  `admissible_not_iteratedAncillaClosure`, `admissible_not_fullComposite`:        │
      │    the countermodel refutes the closure rule AND composite completeness, while  │
      │    `admissible_exact`, `admissible_control`, `admissible_inert`,               │
      │    `admissible_krausSoundExt` hold.                                            │
      │  `closure_independent`: the conjunction, as one ∃-statement.                   │
      └──────────────────────────────────────────────────────────────────────────────┘

  THE ARGUMENT THAT AMPLITUDE DAMPING IS INADMISSIBLE (`ad_not_adm`). Its Choi matrix is
  the sum of two orthogonal dyads (`vec K₀`, `vec K₁`); any Kraus decomposition `Σ conj Kᵢ`
  has Choi matrix `Σ |vec Kᵢ⟩⟨vec Kᵢ|`, and a sum of dyads equal to a rank-two PSD matrix
  has every dyad vector in the span (`dyad_sum_span`, elementary: project off the span,
  the quadratic form of the remainder is a sum of squares equal to zero). So every
  `Kᵢ = aᵢK₀ + bᵢK₁`; normalization forces some `aᵢ ≠ 0`; that operator is not a unitary
  multiple (its Gram matrix has an off-diagonal `āᵢbᵢ·3/5` and unequal diagonal), and it
  is invertible with an explicit inverse, so it cannot factor through two dimensions
  (`Matrix.rank_one` = 4 against `rank_mul_le_left` and `rank_le_card_width`). Kraus
  uniqueness is not invoked: only the elementary span lemma.

  WHAT IS AND IS NOT CLAIMED. Proved: the countermodel and its five properties; the
  non-existence of the shifted theory at level two under control; the failure of the closure
  rule and of composite completeness there. NOT claimed: that the closure rule is the only
  possible packaging of the missing fields (part one records why it is the smallest relative
  attach/discard rule); anything about levels other than two for the obstruction (one level
  suffices for independence). No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.AncillaClosure

namespace OIBridge
namespace ClosureObstruction

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalCountermodel DimensionalObstruction ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure HiddenCoherence

open scoped ComplexOrder Kronecker

/-! ### Section A — admissible operators and maps -/

section Adm

/-- **AN ADMISSIBLE KRAUS OPERATOR AT LEVEL `N`**: a scalar multiple of a unitary, or an
operator factoring through a finite type of cardinality at most `N` — half the dimension
`2N` of the qubit-system composite carrier. -/
def AdmOp (N : ℕ) (K : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  (∃ (c : ℂ) (U : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ), Uᴴ * U = 1 ∧ K = c • U)
    ∨ (∃ (ι : Type) (_ : Fintype ι) (P : Matrix (Fin 2 × Fin N) ι ℂ)
        (Q : Matrix ι (Fin 2 × Fin N) ℂ), Fintype.card ι ≤ N ∧ K = P * Q)

/-- **AN ADMISSIBLE MAP**: a Kraus sum of admissible operators. -/
def Adm (N : ℕ)
    (Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) :
    Prop :=
  ∃ (ι : Type) (_ : Fintype ι) (K : ι → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ),
    Φ = ∑ i, conjChannel (K i) ∧ ∀ i, AdmOp N (K i)

/-- The composite sector of the countermodel: admissible branches, aggregate trace. -/
def IsAdmInstrument (N : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  (∀ a, Adm N (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace

variable {N : ℕ}

theorem admOp_mul {K K' : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (h : AdmOp N K)
    (h' : AdmOp N K') : AdmOp N (K * K') := by
  rcases h with ⟨c, U, hU, rfl⟩ | ⟨ι, _, P, Q, hι, rfl⟩
  · rcases h' with ⟨c', U', hU', rfl⟩ | ⟨ι', _, P', Q', hι', rfl⟩
    · refine Or.inl ⟨c * c', U * U', ?_, ?_⟩
      · rw [Matrix.conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc Uᴴ, hU,
          Matrix.one_mul, hU']
      · rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul]
    · refine Or.inr ⟨ι', inferInstance, c • U * P', Q', hι', ?_⟩
      rw [Matrix.mul_assoc]
  · refine Or.inr ⟨ι, inferInstance, P, Q * K', hι, ?_⟩
    rw [Matrix.mul_assoc]

theorem admOp_unitary {U : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (hU : Uᴴ * U = 1) :
    AdmOp N U :=
  Or.inl ⟨1, U, hU, (one_smul _ _).symm⟩

theorem adm_conjChannel_unitary {U : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ}
    (hU : Uᴴ * U = 1) : Adm N (conjChannel U) :=
  ⟨Unit, inferInstance, fun _ => U, by rw [Fintype.sum_unique], fun _ => admOp_unitary hU⟩

theorem adm_zero : Adm N 0 :=
  ⟨Empty, inferInstance, fun i : Empty => (i.elim : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ),
    by simp, fun i => i.elim⟩

theorem adm_add {Φ Ψ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (hΦ : Adm N Φ) (hΨ : Adm N Ψ) : Adm N (Φ + Ψ) := by
  obtain ⟨ι, _, K, rfl, hK⟩ := hΦ
  obtain ⟨ι', _, K', rfl, hK'⟩ := hΨ
  refine ⟨ι ⊕ ι', inferInstance, Sum.elim K K', ?_, ?_⟩
  · rw [Fintype.sum_sum_type]
    rfl
  · rintro (i | i)
    · exact hK i
    · exact hK' i

theorem adm_sum {ι' : Type*} (s : Finset ι')
    (Φ : ι' → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ)
    (h : ∀ j ∈ s, Adm N (Φ j)) : Adm N (∑ j ∈ s, Φ j) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using adm_zero
  | insert a s ha ih =>
    rw [Finset.sum_insert ha]
    exact adm_add (h a (Finset.mem_insert_self a s))
      (ih fun j hj => h j (Finset.mem_insert_of_mem hj))

theorem conjChannel_mul (V W : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) :
    (conjChannel V).comp (conjChannel W) = conjChannel (V * W) := by
  refine LinearMap.ext fun X => ?_
  show V * (W * X * Wᴴ) * Vᴴ = V * W * X * (V * W)ᴴ
  rw [Matrix.conjTranspose_mul]
  simp only [Matrix.mul_assoc]

theorem adm_comp {Φ Ψ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (hΦ : Adm N Φ) (hΨ : Adm N Ψ) :
    Adm N (Φ.comp Ψ) := by
  obtain ⟨ι, _, K, rfl, hK⟩ := hΦ
  obtain ⟨ι', _, K', rfl, hK'⟩ := hΨ
  refine ⟨ι × ι', inferInstance, fun c => K c.1 * K' c.2, ?_, fun c => admOp_mul (hK c.1) (hK' c.2)⟩
  refine LinearMap.ext fun X => ?_
  simp only [LinearMap.comp_apply, LinearMap.sum_apply]
  rw [Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [map_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← conjChannel_mul]
  rfl

theorem adm_cp {Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (h : Adm N Φ) : IsCompletelyPositive Φ := by
  obtain ⟨ι, _, K, rfl, -⟩ := h
  exact cp_sum _ _ fun i _ => conjChannel_cp _

end Adm

/-! ### Section B — the readout is admissible -/

section Readout

theorem esf_mul_conjTranspose {N : ℕ} (k : Fin N) :
    Esf (A := Fin 2) k * (Esf (A := Fin 2) k)ᴴ
      = Matrix.diagonal fun r : Fin 2 × Fin N => if r.2 = k then (1 : ℂ) else 0 := by
  ext p q
  rw [Matrix.mul_apply, Matrix.diagonal_apply]
  by_cases hp : p.2 = k
  · by_cases hq : q.2 = k
    · rw [Finset.sum_eq_single p.1]
      · simp only [Matrix.conjTranspose_apply, Esf, Matrix.of_apply, hp, hq, if_true, one_mul]
        by_cases hpq : p.1 = q.1
        · rw [if_pos hpq.symm, star_one, if_pos (Prod.ext hpq (hp.trans hq.symm))]
        · rw [if_neg (Ne.symm hpq), star_zero, if_neg (fun h => hpq (congrArg Prod.fst h))]
      · intro s _ hs
        simp [Esf, hp, Ne.symm hs]
      · intro h
        exact absurd (Finset.mem_univ _) h
    · have hpq : p ≠ q := fun h => hq (h ▸ hp)
      simp [Esf, hq, hpq]
  · simp [Esf, hp]

theorem adm_localLuders (N : ℕ) (k : Fin N) : Adm N (localLuders (A := Fin 2) k) := by
  rw [localLuders_eq_conjChannel]
  refine ⟨Unit, inferInstance, fun _ => _, by rw [Fintype.sum_unique], fun _ => ?_⟩
  rcases N with _ | _ | N
  · exact k.elim0
  · refine Or.inl ⟨1, 1, by simp, ?_⟩
    ext ⟨a, j⟩ ⟨b, l⟩
    simp only [Matrix.diagonal_apply, one_smul, Matrix.one_apply, Fin.eq_zero k, Fin.eq_zero j,
      if_true]
  · refine Or.inr ⟨Fin 2, inferInstance, Esf k, (Esf k)ᴴ, by simp, ?_⟩
    rw [esf_mul_conjTranspose]

end Readout

/-! ### Section C — the countermodel -/

/-- **THE COUNTERMODEL.** Kraus families on the system, admissible aggregate-trace-preserving
families on every composite, reference-tested preparations, Lüders readout. -/
noncomputable def admissibleTheory : FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ F => IsKrausFamily F
  availExt := fun N _ _ _ F => IsAdmInstrument N F
  avail_id := scalarAvail_isKraus
    ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
      rw [Complex.ofReal_one, one_smul]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f hF
    exact isKrausFamily_coarse hF f
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => adm_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => adm_comp ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => RefTestedPrep n P
  prepAvail_uniform := fun n =>
    ⟨uniformAttach_trace (n + 1) n.succ_ne_zero,
      amplR_uniformAttach_posSemidef (Matrix.posSemidef_vecMulVec_self_star _) _⟩
  prepAvail_post := by
    rintro n P Φ ⟨hPtr, hPpsd⟩ ⟨hΦ2, hΦtr⟩
    refine ⟨fun ρ => ?_, ?_⟩
    · show (Φ (P ρ)).trace = ρ.trace
      have h := hΦtr (P ρ)
      rw [Fintype.sum_unique] at h
      rw [h, hPtr]
    · rw [amplR_comp]
      exact cp_referencePositive (Fin 2) _ (adm_cp (hΦ2 ())) _ hPpsd
  readout := fun _ k => localLuders k
  readout_avail := fun n => ⟨fun k => adm_localLuders n k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hPtr, hPpsd⟩ ⟨hF2, hFtr⟩
    refine isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) _
      (fun a => ?_) (fun X => ?_)
    · show (choiMatrix (discardWith n P (F a))).PosSemidef
      rw [choiMatrix_eq_ampl2, ← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp]
      exact amplR_ptraceAncL_posSemidef
        (cp_referencePositive (Fin 2) _ (adm_cp (hF2 a)) _ hPpsd)
    · rw [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) X, hFtr (P X), hPtr X]

theorem admissible_exact : ExactFiniteEndomorphicQuantumOps admissibleTheory :=
  fun _ F => isKrausFamily_iff F

theorem admissible_control : HasCompositeUnitaryControl admissibleTheory :=
  fun _ U hU => ⟨fun _ => adm_conjChannel_unitary hU, fun X => by
    rw [Fintype.sum_unique]
    exact conjChannel_trace U hU X⟩

theorem admissible_krausSoundExt : KrausSoundExt admissibleTheory :=
  fun _ _ _ _ F ⟨hadm, htr⟩ =>
    isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F
      (fun a => adm_cp (hadm a)) htr

/-! ### Section D — spectator extension preserves admissibility -/

section Spectator

variable {R : Type} [Fintype R] [DecidableEq R]

theorem one_kronecker_isometry {S : Type*} [Fintype S] [DecidableEq S] {U : Matrix S S ℂ}
    (hU : Uᴴ * U = 1) :
    ((1 : Matrix R R ℂ) ⊗ₖ U)ᴴ * ((1 : Matrix R R ℂ) ⊗ₖ U) = 1 := by
  rw [Matrix.conjTranspose_kronecker, ← Matrix.mul_kronecker_mul, Matrix.conjTranspose_one,
    Matrix.one_mul, hU, Matrix.one_kronecker_one]

theorem tensorOf_one_eq_kronecker {S : Type*} (K : Matrix S S ℂ) :
    tensorOf (1 : Matrix R R ℂ) K = (1 : Matrix R R ℂ) ⊗ₖ K := rfl

theorem reindex_smul_matrix {l l' : Type*} (e : l ≃ l') (c : ℂ) (M : Matrix l l ℂ) :
    Matrix.reindex e e (c • M) = c • Matrix.reindex e e M := by
  ext p q
  rfl

/-- A spectator extension of an admissible operator is admissible at the extended level. -/
theorem admOp_withSpectator {n m : ℕ} (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    {K : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ} (h : AdmOp n K) :
    AdmOp m (Matrix.reindex e e (tensorOf (1 : Matrix R R ℂ) K)) := by
  have hcard : Fintype.card R * n = m := by
    have hc := Fintype.card_congr e
    simp only [Fintype.card_prod, Fintype.card_fin] at hc
    have : 2 * (Fintype.card R * n) = 2 * m := by rw [← hc]; ring
    exact Nat.eq_of_mul_eq_mul_left (by norm_num) this
  rw [tensorOf_one_eq_kronecker]
  rcases h with ⟨c, U, hU, rfl⟩ | ⟨ι, _, P, Q, hι, rfl⟩
  · refine Or.inl ⟨c, Matrix.reindex e e ((1 : Matrix R R ℂ) ⊗ₖ U),
      reindex_isometry e _ (one_kronecker_isometry hU), ?_⟩
    rw [Matrix.kronecker_smul, reindex_smul_matrix]
  · refine Or.inr ⟨R × ι, inferInstance,
      ((1 : Matrix R R ℂ) ⊗ₖ P).submatrix e.symm (Equiv.refl (R × ι)),
      ((1 : Matrix R R ℂ) ⊗ₖ Q).submatrix (Equiv.refl (R × ι)) e.symm, ?_, ?_⟩
    · rw [Fintype.card_prod, ← hcard]
      exact Nat.mul_le_mul_left _ hι
    · rw [Matrix.submatrix_mul_equiv, Matrix.reindex_apply, ← Matrix.mul_kronecker_mul,
        Matrix.one_mul]

theorem adm_withSpectator {n m : ℕ} (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    {Φ : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (h : Adm n Φ) : Adm m (withSpectator R e Φ) := by
  obtain ⟨ι, _, K, rfl, hK⟩ := h
  refine ⟨ι, inferInstance, fun i => Matrix.reindex e e (tensorOf 1 (K i)), ?_,
    fun i => admOp_withSpectator e (hK i)⟩
  rw [withSpectator_sum]
  exact Finset.sum_congr rfl fun i _ => withSpectator_conjChannel e (K i)

end Spectator

/-- **THE COUNTERMODEL HAS PARALLEL REFERENCE EXTENSION.** -/
theorem admissible_parallelReferenceExtension :
    HasParallelReferenceExtension admissibleTheory := by
  intro R _ _ n m e O _ _ F ⟨hadm, htr⟩
  refine ⟨fun a => adm_withSpectator e (hadm a), fun X => ?_⟩
  simp only [withSpectator_apply, trace_reindex, trace_amplRef]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun i _ => htr (refBlockR (Matrix.reindex e.symm e.symm X) i i),
    ← trace_eq_sum_refBlockR, trace_reindex]

theorem admissible_inert : InertSpectatorCompositionality admissibleTheory :=
  (inertSpectator_iff_parallelReferenceExtension _).mpr admissible_parallelReferenceExtension

/-! ### Section E — the span lemma for a rank-two dyad sum -/

section Span

variable {C : Type*} [Fintype C] [DecidableEq C]

theorem star_dot_swap (u w : C → ℂ) : star w ⬝ᵥ u = star (star u ⬝ᵥ w) := by
  simp only [dotProduct, star_sum, star_mul', Pi.star_apply, star_star]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

/-- The quadratic form of a dyad is a square. -/
theorem form_vecMulVec (v y : C → ℂ) :
    star y ⬝ᵥ (Matrix.vecMulVec v (star v) *ᵥ y)
      = ((Complex.normSq (star v ⬝ᵥ y) : ℝ) : ℂ) := by
  rw [vecMulVec_mulVec', dotProduct_smul, smul_eq_mul, star_dot_swap v y,
    Complex.star_def, Complex.mul_conj]

/-- **A SUM OF DYADS EQUAL TO A RANK-TWO PSD MATRIX HAS EVERY DYAD IN THE SPAN.** -/
theorem dyad_sum_span {ι : Type*} [Fintype ι] (v : ι → C → ℂ) (w₀ w₁ : C → ℂ)
    (hw₀ : w₀ ≠ 0) (hw₁ : w₁ ≠ 0) (hw : star w₀ ⬝ᵥ w₁ = 0)
    (h : ∑ i, Matrix.vecMulVec (v i) (star (v i))
      = Matrix.vecMulVec w₀ (star w₀) + Matrix.vecMulVec w₁ (star w₁)) (i : ι) :
    ∃ a b : ℂ, v i = a • w₀ + b • w₁ := by
  have hw' : star w₁ ⬝ᵥ w₀ = 0 := by rw [star_dot_swap, hw, star_zero]
  have hn₀ : star w₀ ⬝ᵥ w₀ ≠ 0 := fun h0 => hw₀ (dotProduct_star_self_eq_zero.mp h0)
  have hn₁ : star w₁ ⬝ᵥ w₁ ≠ 0 := fun h0 => hw₁ (dotProduct_star_self_eq_zero.mp h0)
  set a := (star w₀ ⬝ᵥ v i) / (star w₀ ⬝ᵥ w₀) with ha
  set b := (star w₁ ⬝ᵥ v i) / (star w₁ ⬝ᵥ w₁) with hb
  set y := v i - a • w₀ - b • w₁ with hy
  have hy₀ : star w₀ ⬝ᵥ y = 0 := by
    rw [hy, dotProduct_sub, dotProduct_sub, dotProduct_smul, dotProduct_smul, hw, ha,
      smul_eq_mul, smul_eq_mul, div_mul_cancel₀ _ hn₀]
    ring
  have hy₁ : star w₁ ⬝ᵥ y = 0 := by
    rw [hy, dotProduct_sub, dotProduct_sub, dotProduct_smul, dotProduct_smul, hw', hb,
      smul_eq_mul, smul_eq_mul, div_mul_cancel₀ _ hn₁]
    ring
  -- the quadratic form of both sides at `y`
  have hform : ∑ j, ((Complex.normSq (star (v j) ⬝ᵥ y) : ℝ) : ℂ) = 0 := by
    have hl : star y ⬝ᵥ ((∑ j, Matrix.vecMulVec (v j) (star (v j))) *ᵥ y)
        = ∑ j, ((Complex.normSq (star (v j) ⬝ᵥ y) : ℝ) : ℂ) := by
      rw [Matrix.sum_mulVec, dotProduct_sum]
      exact Finset.sum_congr rfl fun j _ => form_vecMulVec (v j) y
    rw [← hl, h, Matrix.add_mulVec, vecMulVec_mulVec', vecMulVec_mulVec', hy₀, hy₁, zero_smul,
      zero_smul, add_zero, dotProduct_zero]
  have hreal : ∑ j, Complex.normSq (star (v j) ⬝ᵥ y) = 0 := by
    have := hform
    rw [← Complex.ofReal_sum] at this
    exact_mod_cast this
  have hzero : star (v i) ⬝ᵥ y = 0 :=
    Complex.normSq_eq_zero.mp
      ((Finset.sum_eq_zero_iff_of_nonneg fun j _ => Complex.normSq_nonneg _).mp hreal i
        (Finset.mem_univ i))
  have hyy : star y ⬝ᵥ y = 0 := by
    have : star y ⬝ᵥ y = star (v i) ⬝ᵥ y - star a * (star w₀ ⬝ᵥ y) - star b * (star w₁ ⬝ᵥ y) := by
      conv_lhs => rw [hy]
      rw [star_sub, star_sub, star_smul, star_smul, sub_dotProduct, sub_dotProduct,
        smul_dotProduct, smul_dotProduct, smul_eq_mul, smul_eq_mul]
    rw [this, hzero, hy₀, hy₁]
    ring
  refine ⟨a, b, ?_⟩
  have := dotProduct_star_self_eq_zero.mp hyy
  rw [hy, sub_sub, sub_eq_zero] at this
  exact this

end Span

/-! ### Section F — amplitude damping on the ancilla qubit is inadmissible -/

section Damping

/-- `√(1 − γ) = 4/5`. -/
noncomputable def rD : ℝ := 4 / 5
/-- `√γ = 3/5`. -/
noncomputable def sD : ℝ := 3 / 5

/-- The no-jump operator on a qubit: `diag(1, 4/5)`. -/
noncomputable def D₀ : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.of fun i j => if i = j then (if i = 0 then 1 else (rD : ℂ)) else 0

/-- The jump operator on a qubit: `(3/5)|0⟩⟨1|`. -/
noncomputable def E₀ : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.of fun i j => if i = 0 ∧ j = 1 then (sD : ℂ) else 0

/-- The Kraus operators on the level-two carrier: identity on the system, damping on the
ancilla. -/
noncomputable def K₀ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ := (1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ D₀
noncomputable def K₁ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ := (1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ E₀

/-- **AMPLITUDE DAMPING ON THE ANCILLA QUBIT**, at level two. -/
noncomputable def ancillaDamping :
    Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  conjChannel K₀ + conjChannel K₁

theorem rD_sq_add_sD_sq : rD * rD + sD * sD = 1 := by
  simp only [rD, sD]
  norm_num

theorem qubit_gram : D₀ᴴ * D₀ + E₀ᴴ * E₀ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [D₀, E₀, Matrix.mul_apply, Matrix.one_apply] <;>
    norm_num [rD, sD]

theorem damping_gram : K₀ᴴ * K₀ + K₁ᴴ * K₁ = 1 := by
  simp only [K₀, K₁, Matrix.conjTranspose_kronecker, ← Matrix.mul_kronecker_mul,
    Matrix.conjTranspose_one, Matrix.one_mul, ← Matrix.kronecker_add, qubit_gram,
    Matrix.one_kronecker_one]

theorem ancillaDamping_trace (X : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    (ancillaDamping X).trace = X.trace := by
  show (K₀ * X * K₀ᴴ + K₁ * X * K₁ᴴ).trace = X.trace
  rw [Matrix.trace_add, Matrix.trace_mul_cycle K₀ X K₀ᴴ, Matrix.trace_mul_cycle K₁ X K₁ᴴ,
    ← Matrix.trace_add, ← Matrix.add_mul, damping_gram, Matrix.one_mul]

theorem ancillaDamping_isKraus :
    IsFiniteEndomorphicKrausInstrument (fun _ : Fin 1 => ancillaDamping) := by
  refine ⟨1, ![K₀, K₁], fun _ => 0, ?_, ?_⟩
  · rw [Fin.sum_univ_two]
    exact damping_gram
  · funext a
    show ancillaDamping = ∑ k ∈ Finset.univ.filter (fun _ : Fin 2 => (0 : Fin 1) = a),
      conjChannel (![K₀, K₁] k)
    rw [Finset.filter_true_of_mem (fun _ _ => Subsingleton.elim _ _), Fin.sum_univ_two]
    rfl

/-- The vectorization used by the Choi matrix of a conjugation. -/
def vecOf {S : Type*} (V : Matrix S S ℂ) : S × S → ℂ := fun p => V p.2 p.1

theorem choiMatrix_add {S : Type*} [Fintype S] [DecidableEq S]
    (Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    choiMatrix (Φ + Ψ) = choiMatrix Φ + choiMatrix Ψ := by
  ext p q
  rfl

theorem vecOf_K₀_ne : vecOf K₀ ≠ 0 := by
  intro h
  have := congrFun h ((0, 0), (0, 0))
  simp [vecOf, K₀, D₀] at this

theorem vecOf_K₁_ne : vecOf K₁ ≠ 0 := by
  intro h
  have := congrFun h ((0, 1), (0, 0))
  simp [vecOf, K₁, E₀, sD] at this

theorem vecOf_orth : star (vecOf K₀) ⬝ᵥ vecOf K₁ = 0 := by
  simp [dotProduct, vecOf, K₀, K₁, D₀, E₀, Fintype.sum_prod_type,
    Fin.sum_univ_two, Matrix.one_apply]

/-- Every Kraus operator of a Kraus decomposition of the damping channel is a combination of
`K₀` and `K₁`. -/
theorem kraus_of_damping {ι : Type} [Fintype ι] (K : ι → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (hK : ancillaDamping = ∑ i, conjChannel (K i)) (i : ι) :
    ∃ a b : ℂ, K i = a • K₀ + b • K₁ := by
  have hchoi : ∑ j, Matrix.vecMulVec (vecOf (K j)) (star (vecOf (K j)))
      = Matrix.vecMulVec (vecOf K₀) (star (vecOf K₀))
        + Matrix.vecMulVec (vecOf K₁) (star (vecOf K₁)) := by
    have h := congrArg choiMatrix hK
    rw [ancillaDamping, choiMatrix_add, choiMatrix_conjChannel, choiMatrix_conjChannel,
      choiMatrix_finsum] at h
    simp only [choiMatrix_conjChannel] at h
    exact h.symm
  obtain ⟨a, b, hab⟩ := dyad_sum_span (fun j => vecOf (K j)) (vecOf K₀) (vecOf K₁)
    vecOf_K₀_ne vecOf_K₁_ne vecOf_orth hchoi i
  refine ⟨a, b, ?_⟩
  ext p q
  have := congrFun hab (q, p)
  simpa [vecOf] using this

theorem K₀_apply (p q : Fin 2 × Fin 2) :
    K₀ p q = if p.1 = q.1 then (if p.2 = q.2 then (if p.2 = 0 then 1 else (rD : ℂ)) else 0)
      else 0 := by
  obtain ⟨a, j⟩ := p
  obtain ⟨b, l⟩ := q
  simp only [K₀, Matrix.kronecker_apply, Matrix.one_apply, D₀, Matrix.of_apply, ite_mul, one_mul,
    zero_mul]

theorem K₁_apply (p q : Fin 2 × Fin 2) :
    K₁ p q = if p.1 = q.1 then (if p.2 = 0 ∧ q.2 = 1 then (sD : ℂ) else 0) else 0 := by
  obtain ⟨a, j⟩ := p
  obtain ⟨b, l⟩ := q
  simp only [K₁, Matrix.kronecker_apply, Matrix.one_apply, E₀, Matrix.of_apply, ite_mul, one_mul,
    zero_mul]

/-- The Gram entries of `a K₀ + b K₁` that decide the unitary case. -/
theorem gram_entries (a b : ℂ) :
    ((a • K₀ + b • K₁)ᴴ * (a • K₀ + b • K₁)) (0, 0) (0, 1) = star a * b * (sD : ℂ)
    ∧ ((a • K₀ + b • K₁)ᴴ * (a • K₀ + b • K₁)) (0, 0) (0, 0) = star a * a
    ∧ ((a • K₀ + b • K₁)ᴴ * (a • K₀ + b • K₁)) (0, 1) (0, 1)
        = star a * a * ((rD : ℂ) * rD) + star b * b * ((sD : ℂ) * sD) := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      K₀_apply, K₁_apply, Complex.conj_ofReal] <;> ring

/-- The explicit inverse of `a K₀ + b K₁` for `a ≠ 0`. -/
noncomputable def dampInv (a b : ℂ) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  Matrix.of fun p q => if p.1 = q.1 then
    (if p.2 = 0 ∧ q.2 = 0 then a⁻¹ else if p.2 = 0 ∧ q.2 = 1 then -(b * (sD : ℂ)) / (a * a * rD)
      else if p.2 = 1 ∧ q.2 = 1 then (a * rD)⁻¹ else 0) else 0

theorem dampInv_mul (a b : ℂ) (ha : a ≠ 0) : dampInv a b * (a • K₀ + b • K₁) = 1 := by
  have hr : (rD : ℂ) ≠ 0 := by
    rw [Ne, Complex.ofReal_eq_zero]
    norm_num [rD]
  ext ⟨x, j⟩ ⟨y, l⟩
  fin_cases x <;> fin_cases y <;> fin_cases j <;> fin_cases l <;>
    simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, dampInv, K₀_apply, K₁_apply,
      Matrix.one_apply] <;>
    field_simp <;> ring

theorem card_carrier : Fintype.card (Fin 2 × Fin 2) = 4 := by simp

/-- **AMPLITUDE DAMPING IS INADMISSIBLE AT LEVEL TWO.** -/
theorem ad_not_adm : ¬ Adm 2 ancillaDamping := by
  rintro ⟨ι, _, K, hK, hadm⟩
  choose a b hab using kraus_of_damping K hK
  -- normalization
  have hnorm : ∑ i, (K i)ᴴ * K i = 1 := by
    refine sum_conjTranspose_mul_eq_one_of_trace K fun X => ?_
    have h := congrArg (fun Φ => (Φ X).trace) hK
    simp only [LinearMap.sum_apply, Matrix.trace_sum] at h
    rw [ancillaDamping_trace] at h
    exact h.symm
  -- some coefficient `a i` is nonzero
  have hex : ∃ i, a i ≠ 0 := by
    by_contra hall
    have h00 := congrFun (congrFun hnorm (0, 0)) (0, 0)
    rw [Matrix.sum_apply, Matrix.one_apply_eq] at h00
    have hz : ∀ i, ((K i)ᴴ * K i) (0, 0) (0, 0) = 0 := by
      intro i
      have hai : a i = 0 := by
        by_contra hne
        exact hall ⟨i, hne⟩
      rw [hab i, hai, zero_smul, zero_add]
      simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type,
        Fin.sum_univ_two, K₁_apply]
    simp only [Finset.sum_congr rfl fun i _ => hz i, Finset.sum_const_zero, zero_ne_one] at h00
  obtain ⟨i, hai⟩ := hex
  have hs : (sD : ℂ) ≠ 0 := by
    rw [Ne, Complex.ofReal_eq_zero]
    norm_num [sD]
  obtain ⟨h01, h00, h11⟩ := gram_entries (a i) (b i)
  rcases hadm i with ⟨c, U, hU, hcU⟩ | ⟨ι', _, P, Q, hι', hPQ⟩
  · -- the unitary case: the Gram matrix is scalar
    have hgram : (K i)ᴴ * K i = (star c * c) • (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) := by
      rw [hcU, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, hU, smul_smul]
    rw [hab i] at hgram
    have e01 := congrFun (congrFun hgram (0, 0)) (0, 1)
    have e00 := congrFun (congrFun hgram (0, 0)) (0, 0)
    have e11 := congrFun (congrFun hgram (0, 1)) (0, 1)
    rw [h01] at e01
    rw [h00] at e00
    rw [h11] at e11
    simp only [Matrix.smul_apply, Matrix.one_apply, smul_eq_mul] at e01 e00 e11
    simp only [Prod.mk.injEq, and_true, Fin.zero_eq_one_iff, OfNat.ofNat_ne_one, and_false,
      if_false, if_true, mul_zero, mul_one, true_and, Fin.one_eq_zero_iff] at e01 e00 e11
    have hb : b i = 0 := by
      rcases mul_eq_zero.mp e01 with h | h
      · rcases mul_eq_zero.mp h with h' | h'
        · exact absurd (star_eq_zero.mp h') hai
        · exact h'
      · exact absurd h hs
    simp only [hb, star_zero, zero_mul, add_zero] at e11
    rw [← e00] at e11
    have hr : (rD : ℂ) * rD ≠ 1 := by
      rw [← Complex.ofReal_mul, Ne, ← Complex.ofReal_one, Complex.ofReal_inj]
      norm_num [rD]
    have : star (a i) * a i * ((rD : ℂ) * rD - 1) = 0 := by
      rw [mul_sub, mul_one, e11, sub_self]
    rcases mul_eq_zero.mp this with h | h
    · rcases mul_eq_zero.mp h with h' | h'
      · exact hai (star_eq_zero.mp h')
      · exact hai h'
    · exact hr (sub_eq_zero.mp h)
  · -- the factor case: an invertible operator cannot factor through two dimensions
    have hone : (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) = dampInv (a i) (b i) * P * Q := by
      rw [Matrix.mul_assoc, ← hPQ, hab i, dampInv_mul _ _ hai]
    have hrank : (dampInv (a i) (b i) * P * Q).rank ≤ 2 :=
      ((Matrix.rank_mul_le_left _ _).trans (Matrix.rank_le_card_width _)).trans hι'
    rw [← hone, Matrix.rank_one, card_carrier] at hrank
    norm_num at hrank

end Damping

/-! ### Section G — the dilation unitary and the obstruction -/

section Dilation

/-- The `4 × 4` dilation unitary on (old ancilla, fresh ancilla): columns
`|0,0⟩ ↦ |0,0⟩`, `|1,0⟩ ↦ (4/5)|1,0⟩ + (3/5)|0,1⟩`, `|0,1⟩ ↦ |1,1⟩`,
`|1,1⟩ ↦ −(3/5)|1,0⟩ + (4/5)|0,1⟩`. -/
noncomputable def wD : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  Matrix.of fun x y =>
    if y = (0, 0) then (if x = (0, 0) then 1 else 0)
    else if y = (1, 0) then (if x = (1, 0) then (rD : ℂ) else if x = (0, 1) then (sD : ℂ) else 0)
    else if y = (0, 1) then (if x = (1, 1) then 1 else 0)
    else (if x = (1, 0) then -(sD : ℂ) else if x = (0, 1) then (rD : ℂ) else 0)

theorem wD_isometry : wDᴴ * wD = 1 := by
  ext ⟨x1, x2⟩ ⟨y1, y2⟩
  fin_cases x1 <;> fin_cases x2 <;> fin_cases y1 <;> fin_cases y2 <;>
    simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      wD, Matrix.one_apply, Complex.conj_ofReal] <;>
    norm_num [rD, sD]

/-- The reindexing that puts the system slot first. -/
def dilIdx : Fin 2 × (Fin 2 × Fin 2) ≃ (Fin 2 × Fin 2) × Fin 2 :=
  (Equiv.prodAssoc (Fin 2) (Fin 2) (Fin 2)).symm

/-- The dilation unitary on `(Fin 2 × Fin 2) × Fin 2`: identity on the system, `wD` on the
two ancillas. -/
noncomputable def WD : Matrix ((Fin 2 × Fin 2) × Fin 2) ((Fin 2 × Fin 2) × Fin 2) ℂ :=
  Matrix.reindex dilIdx dilIdx ((1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ wD)

theorem WD_isometry : WDᴴ * WD = 1 :=
  reindex_isometry dilIdx _ (one_kronecker_isometry wD_isometry)

theorem WD_apply (a b : Fin 2) (j k l f : Fin 2) :
    WD ((a, j), k) ((b, l), f) = if a = b then wD (j, k) (l, f) else 0 := by
  simp only [WD, Matrix.reindex_apply, Matrix.submatrix_apply, dilIdx, Equiv.symm_symm,
    Equiv.prodAssoc_apply, Matrix.kronecker_apply, Matrix.one_apply, ite_mul, one_mul, zero_mul]

/-- **THE CIRCUIT IDENTITY**: `WD · E_0 = V_{![K₀, K₁]}`. -/
theorem WD_esf : WD * Esf (0 : Fin 2) = Vsf ![K₀, K₁] := by
  ext ⟨⟨a, j⟩, k⟩ ⟨b, l⟩
  rw [Matrix.mul_apply, Fintype.sum_prod_type]
  simp only [Fintype.sum_prod_type, Fin.sum_univ_two, Esf, Matrix.of_apply, Vsf, WD_apply]
  fin_cases a <;> fin_cases b <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [wD, K₀_apply, K₁_apply]

end Dilation

/-- **NO SHIFTED THEORY AT LEVEL TWO.** There is no operational theory on the composite
carrier `Fin 2 × Fin 2` whose system families are the countermodel's level-two families and
which has composite unitary control: it would make amplitude damping on the ancilla
available by the round-25 circuit with the explicit dilation `WD`. -/
theorem admissible_no_shift :
    ¬ ∃ T' : FiniteOperationalTheory (Fin 2 × Fin 2),
      (∀ (O : Type) [Fintype O] [DecidableEq O]
        (F : O → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ →ₗ[ℂ]
          Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
        T'.avail O F ↔ admissibleTheory.availExt 2 O F)
        ∧ HasCompositeUnitaryControl T' := by
  rintro ⟨T', hav, hctrl⟩
  have hcirc := circuit_available_pureSeed T' hctrl 1 0 WD WD_isometry
  rw [show (fun k => discardMap (1 + 1) (0 : Fin (1 + 1))
        ((localLuders k).comp (conjChannel WD)))
      = fun k => conjChannel (![K₀, K₁] k) from by
    funext k
    exact LinearMap.ext fun ρ => stinespringCircuit_branch ![K₀, K₁] 0 k WD WD_esf ρ] at hcirc
  have hco := T'.avail_coarse (Fin (1 + 1)) Unit _ (fun _ => ()) hcirc
  have hfun : (fun a : Unit => ∑ j ∈ Finset.univ.filter (fun _ : Fin (1 + 1) => () = a),
      conjChannel (![K₀, K₁] j)) = fun _ => ancillaDamping := by
    funext a
    rw [Finset.filter_true_of_mem (fun _ _ => rfl), Fin.sum_univ_two]
    rfl
  rw [hfun] at hco
  exact ad_not_adm (((hav Unit _).mp hco).1 ())

/-- **THE CLOSURE RULE FAILS IN THE COUNTERMODEL.** -/
theorem admissible_not_iteratedAncillaClosure : ¬ IteratedAncillaClosure admissibleTheory :=
  fun h => admissible_no_shift
    ⟨shift admissibleTheory admissible_control admissible_inert h 2,
      fun _ _ _ _ => Iff.rfl, shift_control admissibleTheory admissible_control admissible_inert h 2⟩

/-- **COMPOSITE COMPLETENESS FAILS IN THE COUNTERMODEL**: amplitude damping is a normalized
Kraus instrument on the level-two carrier that is not available. -/
theorem admissible_not_fullComposite : ¬ HasFullCompositeInstruments admissibleTheory := by
  intro h
  have hav := h 1 1 1 ![K₀, K₁] (fun _ => 0) (by rw [Fin.sum_univ_two]; exact damping_gram)
  have hfun : instrumentBranch ![K₀, K₁] (fun _ : Fin 2 => (0 : Fin 1))
      = fun _ => ancillaDamping := by
    funext a
    show ∑ k ∈ Finset.univ.filter (fun _ : Fin 2 => (0 : Fin 1) = a), conjChannel (![K₀, K₁] k)
      = ancillaDamping
    rw [Finset.filter_true_of_mem (fun _ _ => Subsingleton.elim _ _), Fin.sum_univ_two]
    rfl
  rw [hfun] at hav
  exact ad_not_adm (hav.1 0)

theorem admissible_not_exactComposite : ¬ ExactCompositeQuantumOps admissibleTheory :=
  fun h => admissible_not_fullComposite ((exactComposite_iff _).mp h).2

/-- **ITERATED ANCILLA CLOSURE IS INDEPENDENT.** A theory exactly quantum on the system, with
every composite unitary, inert-spectator compositionality and composite Kraus soundness,
that refutes the closure rule and composite completeness. -/
theorem closure_independent :
    ∃ T : FiniteOperationalTheory (Fin 2),
      ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T
        ∧ InertSpectatorCompositionality T ∧ KrausSoundExt T
        ∧ ¬ IteratedAncillaClosure T ∧ ¬ HasFullCompositeInstruments T :=
  ⟨admissibleTheory, admissible_exact, admissible_control, admissible_inert,
    admissible_krausSoundExt, admissible_not_iteratedAncillaClosure,
    admissible_not_fullComposite⟩

#print axioms admOp_mul
#print axioms admOp_unitary
#print axioms adm_conjChannel_unitary
#print axioms adm_zero
#print axioms adm_add
#print axioms adm_sum
#print axioms conjChannel_mul
#print axioms adm_comp
#print axioms adm_cp
#print axioms esf_mul_conjTranspose
#print axioms adm_localLuders
#print axioms admissible_exact
#print axioms admissible_control
#print axioms admissible_krausSoundExt
#print axioms one_kronecker_isometry
#print axioms tensorOf_one_eq_kronecker
#print axioms reindex_smul_matrix
#print axioms admOp_withSpectator
#print axioms adm_withSpectator
#print axioms admissible_parallelReferenceExtension
#print axioms admissible_inert
#print axioms star_dot_swap
#print axioms form_vecMulVec
#print axioms dyad_sum_span
#print axioms rD_sq_add_sD_sq
#print axioms qubit_gram
#print axioms damping_gram
#print axioms ancillaDamping_trace
#print axioms ancillaDamping_isKraus
#print axioms choiMatrix_add
#print axioms vecOf_K₀_ne
#print axioms vecOf_K₁_ne
#print axioms vecOf_orth
#print axioms kraus_of_damping
#print axioms K₀_apply
#print axioms K₁_apply
#print axioms gram_entries
#print axioms dampInv_mul
#print axioms card_carrier
#print axioms ad_not_adm
#print axioms wD_isometry
#print axioms WD_isometry
#print axioms WD_apply
#print axioms WD_esf
#print axioms admissible_no_shift
#print axioms admissible_not_iteratedAncillaClosure
#print axioms admissible_not_fullComposite
#print axioms admissible_not_exactComposite
#print axioms closure_independent

end ClosureObstruction
end OIBridge
