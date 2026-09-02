/-
  OIBridge/RankGapTheory.lean — the closure cell is CLOSED: a theory with validity, inert
  spectators, full composite control and system-to-level-one, realizing the sealed OI core,
  that fails iterated ancilla closure. With it the minimality audit is five-way.

  ROUND FORTY-FOUR. Round forty-three left one cell of the minimality audit open: the
  round-38 admissible theory (Kraus operators that are unitary multiples or factor through
  half the composite dimension) fails system-to-level-one, because qubit amplitude damping
  has an invertible non-unitary-multiple operator at level one. The repair is the RANK-GAP
  theory: widen "scalar multiple of a unitary" to "invertible". At level `N` the composite
  carrier has dimension `2N`, and the admitted Kraus operators are those that are invertible
  or factor through at most `N` dimensions — the intermediate ranks `N < rank < 2N` are
  excluded. Every unitary is invertible, every native Lüders selector is low-rank, products
  and spectator extensions stay in the class, so validity, inert spectators and control hold
  exactly as in round thirty-eight. At level one the carrier is two-dimensional, and EVERY
  `2 × 2` matrix is invertible or factors through one dimension (`twoByTwo_dichotomy`,
  kernelized by explicit inverse and explicit factorizations): so with all Kraus families on
  the system, system-to-level-one holds (`gap_systemToLevelOne`) — exactly the defect that
  killed the round-38 witness.

  THE OBSTRUCTION, at level three (six-dimensional carrier `Fin 2 × Fin 3`, bound `N = 3`).
  `G₀ = 1 ⊗ diag(1,1,0)` (rank four) and `G₁ = 1 ⊗ |0⟩⟨2|` (rank two) are a normalized Kraus
  pair. By the round-38 two-dyad span lemma every Kraus decomposition of `gapChannel` has
  operators `a G₀ + b G₁`, and normalization forces some `a ≠ 0`. Such an operator has the
  nonzero kernel vector `b e₍₀,₀₎ − a e₍₀,₂₎` (so it is not invertible) and compresses on the
  first four basis vectors to `a · 1₄` (so it cannot factor through three dimensions, by
  `Matrix.rank_one` against `rank_mul_le_left` and `rank_le_card_width`): rank four lies in
  the gap `3 < 4 < 6`. Yet the channel has a TWO-dimensional environment with an explicit
  PERMUTATION dilation `wG` (a single transposition on `Fin 3 × Fin 2`): under iterated
  ancilla closure the shifted theory at base level three exists, has control, and the
  round-25 circuit with `WG` produces `gapChannel` at level three. No finite-isometry
  boundary is used anywhere in the obstruction.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `gapTheory : FiniteOperationalTheory (Fin 2)` with `gap_validity`,           │
      │    `gap_inert`, `gap_control`, `gap_systemToLevelOne`,                       │
      │    `gap_realizesSealedOICore`, and `gap_not_iteratedAncillaClosure`.         │
      │  `closure_cell_closed`: the ∃-statement for the closure cell.                 │
      │  `five_way_minimality`: for EACH of the five physical completion conditions,  │
      │    the same finite OI framework admits a theory satisfying the other four,    │
      │    realizing the sealed OI core, and failing exactly that one.               │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHAT IS AND IS NOT CLAIMED. Proved: everything above; the round-43 characterization
  `exactAll_iff_physical` is untouched and is now minimal in every cell. NOT claimed: that
  any condition follows from OI; OI ⟺ QM; anything about boundary item 2 (finite isometry
  extension), which still enters the constructive direction of the characterization
  [DISCHARGED IN ROUND FORTY-FIVE: `IsometryExtension.lean`]. No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DiagonalTheory

namespace OIBridge
namespace RankGapTheory

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence

open scoped ComplexOrder Kronecker

/-! ### Section A — invertibility and the gap class -/

section Gap

theorem isUnit_of_left_inverse {S : Type*} [Fintype S] [DecidableEq S] {L K : Matrix S S ℂ}
    (h : L * K = 1) : IsUnit K := by
  have hd : L.det * K.det = 1 := by rw [← Matrix.det_mul, h, Matrix.det_one]
  refine (Matrix.isUnit_iff_isUnit_det K).mpr (isUnit_iff_ne_zero.mpr fun h0 => ?_)
  rw [h0, mul_zero] at hd
  exact zero_ne_one hd

theorem inv_mul_of_isUnit {S : Type*} [Fintype S] [DecidableEq S] {K : Matrix S S ℂ}
    (h : IsUnit K) : K⁻¹ * K = 1 :=
  Matrix.nonsing_inv_mul K ((Matrix.isUnit_iff_isUnit_det K).mp h)

/-- **A GAP-ADMISSIBLE KRAUS OPERATOR AT LEVEL `N`**: invertible, or factoring through a
finite type of cardinality at most `N` — half the dimension `2N` of the composite carrier.
The intermediate ranks `N < rank < 2N` are excluded. -/
def GapOp (N : ℕ) (K : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  IsUnit K
    ∨ (∃ (ι : Type) (_ : Fintype ι) (P : Matrix (Fin 2 × Fin N) ι ℂ)
        (Q : Matrix ι (Fin 2 × Fin N) ℂ), Fintype.card ι ≤ N ∧ K = P * Q)

/-- **A GAP-ADMISSIBLE MAP**: a Kraus sum of gap-admissible operators. -/
def Gap (N : ℕ)
    (Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) :
    Prop :=
  ∃ (ι : Type) (_ : Fintype ι) (K : ι → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ),
    Φ = ∑ i, conjChannel (K i) ∧ ∀ i, GapOp N (K i)

/-- The composite sector of the rank-gap theory: gap-admissible branches, aggregate trace. -/
def IsGapInstrument (N : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  (∀ a, Gap N (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace

variable {N : ℕ}

theorem gapOp_mul {K K' : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (h : GapOp N K)
    (h' : GapOp N K') : GapOp N (K * K') := by
  rcases h with hK | ⟨ι, _, P, Q, hι, rfl⟩
  · rcases h' with hK' | ⟨ι', _, P', Q', hι', rfl⟩
    · exact Or.inl (hK.mul hK')
    · refine Or.inr ⟨ι', inferInstance, K * P', Q', hι', ?_⟩
      rw [Matrix.mul_assoc]
  · refine Or.inr ⟨ι, inferInstance, P, Q * K', hι, ?_⟩
    rw [Matrix.mul_assoc]

theorem gapOp_unitary {U : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (hU : Uᴴ * U = 1) :
    GapOp N U :=
  Or.inl (isUnit_of_left_inverse hU)

theorem gap_conjChannel {K : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (hK : GapOp N K) :
    Gap N (conjChannel K) :=
  ⟨Unit, inferInstance, fun _ => K, by rw [Fintype.sum_unique], fun _ => hK⟩

theorem gap_zero : Gap N 0 :=
  ⟨Empty, inferInstance, fun i : Empty => (i.elim : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ),
    by simp, fun i => i.elim⟩

theorem gap_add {Φ Ψ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (hΦ : Gap N Φ) (hΨ : Gap N Ψ) : Gap N (Φ + Ψ) := by
  obtain ⟨ι, _, K, rfl, hK⟩ := hΦ
  obtain ⟨ι', _, K', rfl, hK'⟩ := hΨ
  refine ⟨ι ⊕ ι', inferInstance, Sum.elim K K', ?_, ?_⟩
  · rw [Fintype.sum_sum_type]
    rfl
  · rintro (i | i)
    · exact hK i
    · exact hK' i

theorem gap_sum {ι' : Type*} (s : Finset ι')
    (Φ : ι' → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ)
    (h : ∀ j ∈ s, Gap N (Φ j)) : Gap N (∑ j ∈ s, Φ j) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using gap_zero
  | insert a s ha ih =>
    rw [Finset.sum_insert ha]
    exact gap_add (h a (Finset.mem_insert_self a s))
      (ih fun j hj => h j (Finset.mem_insert_of_mem hj))

theorem gap_comp {Φ Ψ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (hΦ : Gap N Φ) (hΨ : Gap N Ψ) :
    Gap N (Φ.comp Ψ) := by
  obtain ⟨ι, _, K, rfl, hK⟩ := hΦ
  obtain ⟨ι', _, K', rfl, hK'⟩ := hΨ
  refine ⟨ι × ι', inferInstance, fun c => K c.1 * K' c.2, ?_, fun c => gapOp_mul (hK c.1) (hK' c.2)⟩
  refine LinearMap.ext fun X => ?_
  simp only [LinearMap.comp_apply, LinearMap.sum_apply]
  rw [Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [map_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← conjChannel_mul]
  rfl

theorem gap_cp {Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ} (h : Gap N Φ) : IsCompletelyPositive Φ := by
  obtain ⟨ι, _, K, rfl, -⟩ := h
  exact cp_sum _ _ fun i _ => conjChannel_cp _

end Gap

/-! ### Section B — the level-one dichotomy -/

section LevelOne

/-- The explicit inverse of a `2 × 2` matrix on `Fin 2 × Fin 1` with determinant `δ`. -/
noncomputable def inv2 (δ : ℂ) (K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) :
    Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  Matrix.of fun p q => δ⁻¹ *
    (if p.1 = 0 then (if q.1 = 0 then K (1, 0) (1, 0) else -K (0, 0) (1, 0))
      else (if q.1 = 0 then -K (1, 0) (0, 0) else K (0, 0) (0, 0)))

theorem inv2_mul (K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) (δ : ℂ)
    (hδ : δ = K (0, 0) (0, 0) * K (1, 0) (1, 0) - K (0, 0) (1, 0) * K (1, 0) (0, 0))
    (h : δ ≠ 0) : inv2 δ K * K = 1 := by
  ext ⟨x, j⟩ ⟨y, l⟩
  fin_cases x <;> fin_cases y <;> fin_cases j <;> fin_cases l <;>
    simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, inv2] <;>
    field_simp <;> subst hδ <;> ring

/-- Entrywise extensionality on the level-one carrier. -/
theorem ext_two_one {M N : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ}
    (h00 : M (0, 0) (0, 0) = N (0, 0) (0, 0)) (h01 : M (0, 0) (1, 0) = N (0, 0) (1, 0))
    (h10 : M (1, 0) (0, 0) = N (1, 0) (0, 0)) (h11 : M (1, 0) (1, 0) = N (1, 0) (1, 0)) :
    M = N := by
  ext ⟨x, j⟩ ⟨y, l⟩
  obtain rfl := Fin.eq_zero j
  obtain rfl := Fin.eq_zero l
  fin_cases x <;> fin_cases y <;> assumption

/-- **A SINGULAR `2 × 2` MATRIX FACTORS THROUGH ONE DIMENSION**, by explicit column-row
factorizations in the three cases `a ≠ 0`; `a = 0, b ≠ 0`; `a = b = 0`. -/
theorem factor_of_singular (K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ)
    (hδ : K (0, 0) (0, 0) * K (1, 0) (1, 0) - K (0, 0) (1, 0) * K (1, 0) (0, 0) = 0) :
    ∃ (P : Matrix (Fin 2 × Fin 1) Unit ℂ) (Q : Matrix Unit (Fin 2 × Fin 1) ℂ), K = P * Q := by
  by_cases ha : K (0, 0) (0, 0) = 0
  · by_cases hb : K (0, 0) (1, 0) = 0
    · -- first row zero: `K = col(0, 1) · row(K₁₀, K₁₁)`
      refine ⟨Matrix.of fun p _ => if p.1 = 0 then 0 else 1,
        Matrix.of fun _ q => K (1, 0) q, ?_⟩
      ext ⟨x, j⟩ ⟨y, l⟩
      fin_cases x <;> fin_cases y <;> fin_cases j <;> fin_cases l <;>
        simp [Matrix.mul_apply, ha, hb]
    · -- `a = 0`, `b ≠ 0` forces `c = 0`: `K = col(b, d) · row(0, 1)`
      have hc : K (1, 0) (0, 0) = 0 := by
        rw [ha, zero_mul, zero_sub, neg_eq_zero] at hδ
        rcases mul_eq_zero.mp hδ with h | h
        · exact absurd h hb
        · exact h
      refine ⟨Matrix.of fun p _ => K p (1, 0),
        Matrix.of fun _ q => if q.1 = 0 then 0 else 1, ?_⟩
      ext ⟨x, j⟩ ⟨y, l⟩
      fin_cases x <;> fin_cases y <;> fin_cases j <;> fin_cases l <;>
        simp [Matrix.mul_apply, ha, hc]
  · -- `a ≠ 0`: `K = col(a, c) · row(1, b/a)`, using `a d = b c`
    have ha' : K (0, 0) (0, 0) ≠ 0 := ha
    have hd : K (1, 0) (1, 0) = K (1, 0) (0, 0) * (K (0, 0) (1, 0) / K (0, 0) (0, 0)) := by
      rw [← mul_div_assoc, eq_div_iff ha']
      linear_combination hδ
    have hb : K (0, 0) (1, 0) = K (0, 0) (0, 0) * (K (0, 0) (1, 0) / K (0, 0) (0, 0)) := by
      rw [mul_div_assoc', mul_div_cancel_left₀ _ ha']
    refine ⟨Matrix.of fun p _ => K p (0, 0),
      Matrix.of fun _ q => if q.1 = 0 then 1 else K (0, 0) (1, 0) / K (0, 0) (0, 0), ?_⟩
    refine ext_two_one ?_ ?_ ?_ ?_ <;>
      simp only [Matrix.mul_apply, Fintype.sum_unique, Matrix.of_apply, Fin.isValue, one_ne_zero,
        if_true, if_false, mul_one]
    · exact hb
    · exact hd

/-- **THE LEVEL-ONE DICHOTOMY**: every `2 × 2` complex matrix is invertible or factors
through a one-dimensional space. Kernelized explicitly: explicit inverse when the
determinant is nonzero, explicit factorization otherwise. -/
theorem twoByTwo_dichotomy (K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) :
    IsUnit K ∨ ∃ (P : Matrix (Fin 2 × Fin 1) Unit ℂ) (Q : Matrix Unit (Fin 2 × Fin 1) ℂ),
      K = P * Q := by
  by_cases hδ : K (0, 0) (0, 0) * K (1, 0) (1, 0) - K (0, 0) (1, 0) * K (1, 0) (0, 0) = 0
  · exact Or.inr (factor_of_singular K hδ)
  · exact Or.inl (isUnit_of_left_inverse (inv2_mul K _ rfl hδ))

/-- Every operator on the level-one carrier is gap-admissible. -/
theorem gapOp_one (K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) : GapOp 1 K := by
  rcases twoByTwo_dichotomy K with h | ⟨P, Q, hPQ⟩
  · exact Or.inl h
  · exact Or.inr ⟨Unit, inferInstance, P, Q, by simp, hPQ⟩

end LevelOne

/-! ### Section C — the readout is gap-admissible -/

theorem gap_localLuders (N : ℕ) (k : Fin N) : Gap N (localLuders (A := Fin 2) k) := by
  rw [localLuders_eq_conjChannel]
  refine gap_conjChannel ?_
  rcases N with _ | _ | N
  · exact k.elim0
  · exact gapOp_one _
  · refine Or.inr ⟨Fin 2, inferInstance, Esf k, (Esf k)ᴴ, by simp, ?_⟩
    rw [esf_mul_conjTranspose]

/-! ### Section D — the rank-gap theory -/

/-- **THE RANK-GAP THEORY.** All Kraus families on the system, gap-admissible
aggregate-trace-preserving families on every composite, reference-tested preparations,
Lüders readout. -/
noncomputable def gapTheory : FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ F => IsKrausFamily F
  availExt := fun N _ _ _ F => IsGapInstrument N F
  avail_id := scalarAvail_isKraus
    ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
      rw [Complex.ofReal_one, one_smul]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f hF
    exact isKrausFamily_coarse hF f
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => gap_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => gap_comp ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
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
      exact cp_referencePositive (Fin 2) _ (gap_cp (hΦ2 ())) _ hPpsd
  readout := fun _ k => localLuders k
  readout_avail := fun n => ⟨fun k => gap_localLuders n k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hPtr, hPpsd⟩ ⟨hF2, hFtr⟩
    refine isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) _
      (fun a => ?_) (fun X => ?_)
    · show (choiMatrix (discardWith n P (F a))).PosSemidef
      rw [choiMatrix_eq_ampl2, ← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp]
      exact amplR_ptraceAncL_posSemidef
        (cp_referencePositive (Fin 2) _ (gap_cp (hF2 a)) _ hPpsd)
    · rw [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) X, hFtr (P X), hPtr X]

theorem gap_exact : ExactFiniteEndomorphicQuantumOps gapTheory :=
  fun _ F => isKrausFamily_iff F

theorem gap_control : HasCompositeUnitaryControl gapTheory :=
  fun _ U hU => ⟨fun _ => gap_conjChannel (gapOp_unitary hU), fun X => by
    rw [Fintype.sum_unique]
    exact conjChannel_trace U hU X⟩

theorem gap_krausSoundExt : KrausSoundExt gapTheory :=
  fun _ _ _ _ F ⟨hgap, htr⟩ =>
    isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F
      (fun a => gap_cp (hgap a)) htr

theorem gap_validity : CompositeOperationalValidity gapTheory :=
  validity_of_krausSoundExt _ gap_krausSoundExt

theorem gap_realizesSealedOICore : RealizesSealedOICore gapTheory :=
  realizesSealedOICore_of_control _ gap_control

/-- **SYSTEM-TO-LEVEL-ONE HOLDS**: Kraus form transports to level one, and every level-one
operator is gap-admissible by the dichotomy. -/
theorem gap_systemToLevelOne : SystemToLevelOne gapTheory := by
  intro O _ _ F hF
  refine ⟨fun a => ?_, fun X => ?_⟩
  · obtain ⟨n, K, out, -, hKF⟩ := (hF : IsKrausFamily F)
    show Gap 1 (transport (levelOneIdx (Fin 2)).symm (F a))
    rw [hKF a, transport_sum]
    refine gap_sum _ _ fun k _ => ?_
    rw [transport_conjChannel]
    exact gap_conjChannel (gapOp_one _)
  · simp only [trace_transport]
    rw [(krausFamily_cp_tr (hF : IsKrausFamily F)).2, trace_reindex]

/-! ### Section E — spectator extension preserves the gap class -/

section Spectator

variable {R : Type} [Fintype R] [DecidableEq R]

/-- A spectator extension of a gap-admissible operator is gap-admissible at the extended
level: invertibility is preserved by `1 ⊗ ·` and reindexing, and the factorization bound
scales with the spectator. -/
theorem gapOp_withSpectator {n m : ℕ} (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    {K : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ} (h : GapOp n K) :
    GapOp m (Matrix.reindex e e (tensorOf (1 : Matrix R R ℂ) K)) := by
  have hcard : Fintype.card R * n = m := by
    have hc := Fintype.card_congr e
    simp only [Fintype.card_prod, Fintype.card_fin] at hc
    have : 2 * (Fintype.card R * n) = 2 * m := by rw [← hc]; ring
    exact Nat.eq_of_mul_eq_mul_left (by norm_num) this
  rw [tensorOf_one_eq_kronecker]
  rcases h with hK | ⟨ι, _, P, Q, hι, rfl⟩
  · refine Or.inl (isUnit_of_left_inverse
      (L := Matrix.reindex e e ((1 : Matrix R R ℂ) ⊗ₖ K⁻¹)) ?_)
    rw [← reindex_mul, ← Matrix.mul_kronecker_mul, Matrix.one_mul, inv_mul_of_isUnit hK,
      Matrix.one_kronecker_one, Matrix.reindex_apply, Matrix.submatrix_one_equiv]
  · refine Or.inr ⟨R × ι, inferInstance,
      ((1 : Matrix R R ℂ) ⊗ₖ P).submatrix e.symm (Equiv.refl (R × ι)),
      ((1 : Matrix R R ℂ) ⊗ₖ Q).submatrix (Equiv.refl (R × ι)) e.symm, ?_, ?_⟩
    · rw [Fintype.card_prod, ← hcard]
      exact Nat.mul_le_mul_left _ hι
    · rw [Matrix.submatrix_mul_equiv, Matrix.reindex_apply, ← Matrix.mul_kronecker_mul,
        Matrix.one_mul]

theorem gap_withSpectator {n m : ℕ} (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    {Φ : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (h : Gap n Φ) : Gap m (withSpectator R e Φ) := by
  obtain ⟨ι, _, K, rfl, hK⟩ := h
  refine ⟨ι, inferInstance, fun i => Matrix.reindex e e (tensorOf 1 (K i)), ?_,
    fun i => gapOp_withSpectator e (hK i)⟩
  rw [withSpectator_sum]
  exact Finset.sum_congr rfl fun i _ => withSpectator_conjChannel e (K i)

end Spectator

theorem gap_parallelReferenceExtension : HasParallelReferenceExtension gapTheory := by
  intro R _ _ n m e O _ _ F ⟨hgap, htr⟩
  refine ⟨fun a => gap_withSpectator e (hgap a), fun X => ?_⟩
  simp only [withSpectator_apply, trace_reindex, trace_amplRef]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun i _ => htr (refBlockR (Matrix.reindex e.symm e.symm X) i i),
    ← trace_eq_sum_refBlockR, trace_reindex]

theorem gap_inert : InertSpectatorCompositionality gapTheory :=
  (inertSpectator_iff_parallelReferenceExtension _).mpr gap_parallelReferenceExtension

/-! ### Section F — the level-three channel with a rank-four operator -/

section Obstruction

/-- `diag(1, 1, 0)` on the qutrit ancilla. -/
def D3 : Matrix (Fin 3) (Fin 3) ℂ := Matrix.of fun i j => if i = j ∧ i ≠ 2 then 1 else 0

/-- `|0⟩⟨2|` on the qutrit ancilla. -/
def E3 : Matrix (Fin 3) (Fin 3) ℂ := Matrix.of fun i j => if i = 0 ∧ j = 2 then 1 else 0

/-- The Kraus operators on the level-three carrier: identity on the system, `D3`/`E3` on the
ancilla. `G₀` has rank four, `G₁` rank two. -/
def G₀ : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ := (1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ D3
def G₁ : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ := (1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ E3

/-- **THE GAP CHANNEL** at level three. -/
def gapChannel :
    Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ :=
  conjChannel G₀ + conjChannel G₁

theorem qutrit_gram : D3ᴴ * D3 + E3ᴴ * E3 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [D3, E3, Matrix.mul_apply, Fin.sum_univ_three]

theorem gap_gram : G₀ᴴ * G₀ + G₁ᴴ * G₁ = 1 := by
  simp only [G₀, G₁, Matrix.conjTranspose_kronecker, ← Matrix.mul_kronecker_mul,
    Matrix.conjTranspose_one, Matrix.one_mul, ← Matrix.kronecker_add, qutrit_gram,
    Matrix.one_kronecker_one]

theorem gapChannel_trace (X : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ) :
    (gapChannel X).trace = X.trace := by
  show (G₀ * X * G₀ᴴ + G₁ * X * G₁ᴴ).trace = X.trace
  rw [Matrix.trace_add, Matrix.trace_mul_cycle G₀ X G₀ᴴ, Matrix.trace_mul_cycle G₁ X G₁ᴴ,
    ← Matrix.trace_add, ← Matrix.add_mul, gap_gram, Matrix.one_mul]

theorem gapChannel_isKraus :
    IsFiniteEndomorphicKrausInstrument (fun _ : Fin 1 => gapChannel) := by
  refine ⟨1, ![G₀, G₁], fun _ => 0, ?_, ?_⟩
  · rw [Fin.sum_univ_two]
    exact gap_gram
  · funext a
    show gapChannel = ∑ k ∈ Finset.univ.filter (fun _ : Fin 2 => (0 : Fin 1) = a),
      conjChannel (![G₀, G₁] k)
    rw [Finset.filter_true_of_mem (fun _ _ => Subsingleton.elim _ _), Fin.sum_univ_two]
    rfl

theorem G₀_apply (p q : Fin 2 × Fin 3) :
    G₀ p q = if p.1 = q.1 then (if p.2 = q.2 ∧ p.2 ≠ 2 then (1 : ℂ) else 0) else 0 := by
  obtain ⟨a, j⟩ := p
  obtain ⟨b, l⟩ := q
  simp only [G₀, Matrix.kronecker_apply, Matrix.one_apply, D3, Matrix.of_apply, ite_mul, one_mul,
    zero_mul]

theorem G₁_apply (p q : Fin 2 × Fin 3) :
    G₁ p q = if p.1 = q.1 then (if p.2 = 0 ∧ q.2 = 2 then (1 : ℂ) else 0) else 0 := by
  obtain ⟨a, j⟩ := p
  obtain ⟨b, l⟩ := q
  simp only [G₁, Matrix.kronecker_apply, Matrix.one_apply, E3, Matrix.of_apply, ite_mul, one_mul,
    zero_mul]

theorem vecOf_G₀_ne : vecOf G₀ ≠ 0 := by
  intro h
  have := congrFun h ((0, 0), (0, 0))
  simp [vecOf, G₀_apply] at this

theorem vecOf_G₁_ne : vecOf G₁ ≠ 0 := by
  intro h
  have := congrFun h ((0, 2), (0, 0))
  simp [vecOf, G₁_apply] at this

theorem vecOf_G_orth : star (vecOf G₀) ⬝ᵥ vecOf G₁ = 0 := by
  simp [dotProduct, vecOf, G₀_apply, G₁_apply, Fintype.sum_prod_type, Fin.sum_univ_three]

/-- Every Kraus operator of a Kraus decomposition of the gap channel is a combination of
`G₀` and `G₁` — the round-38 two-dyad span lemma, reused unchanged. -/
theorem kraus_of_gapChannel {ι : Type} [Fintype ι]
    (K : ι → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ)
    (hK : gapChannel = ∑ i, conjChannel (K i)) (i : ι) :
    ∃ a b : ℂ, K i = a • G₀ + b • G₁ := by
  have hchoi : ∑ j, Matrix.vecMulVec (vecOf (K j)) (star (vecOf (K j)))
      = Matrix.vecMulVec (vecOf G₀) (star (vecOf G₀))
        + Matrix.vecMulVec (vecOf G₁) (star (vecOf G₁)) := by
    have h := congrArg choiMatrix hK
    rw [gapChannel, choiMatrix_add, choiMatrix_conjChannel, choiMatrix_conjChannel,
      choiMatrix_finsum] at h
    simp only [choiMatrix_conjChannel] at h
    exact h.symm
  obtain ⟨a, b, hab⟩ := dyad_sum_span (fun j => vecOf (K j)) (vecOf G₀) (vecOf G₁)
    vecOf_G₀_ne vecOf_G₁_ne vecOf_G_orth hchoi i
  refine ⟨a, b, ?_⟩
  ext p q
  have := congrFun hab (q, p)
  simpa [vecOf] using this

/-- The kernel vector `b e₍₀,₀₎ − a e₍₀,₂₎` of `a G₀ + b G₁`. -/
def kerVec (a b : ℂ) : Fin 2 × Fin 3 → ℂ :=
  fun p => if p.1 = 0 then (if p.2 = 0 then b else if p.2 = 2 then -a else 0) else 0

theorem gap_mulVec_kerVec (a b : ℂ) : (a • G₀ + b • G₁) *ᵥ kerVec a b = 0 := by
  ext ⟨x, j⟩
  fin_cases x <;> fin_cases j <;>
    simp [Matrix.mulVec, dotProduct, Fintype.sum_prod_type, Fin.sum_univ_three, kerVec, G₀_apply,
      G₁_apply]
  ring

/-- **`a G₀ + b G₁` IS NOT INVERTIBLE** for `a ≠ 0`: it kills a nonzero vector. -/
theorem gap_not_isUnit {a b : ℂ} (ha : a ≠ 0) : ¬ IsUnit (a • G₀ + b • G₁) := by
  intro h
  have h1 := inv_mul_of_isUnit h
  have hv : kerVec a b = 0 := by
    have h2 : ((a • G₀ + b • G₁)⁻¹ * (a • G₀ + b • G₁)) *ᵥ kerVec a b
        = (1 : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ) *ᵥ kerVec a b := by rw [h1]
    rw [← Matrix.mulVec_mulVec, gap_mulVec_kerVec, Matrix.mulVec_zero, Matrix.one_mulVec] at h2
    exact h2.symm
  have := congrFun hv (0, 2)
  simp [kerVec] at this
  exact ha this

/-- The embedding of the first four basis vectors (`j < 2`) into the level-three carrier. -/
def inc : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 2) ℂ :=
  Matrix.of fun p q => if p.1 = q.1 ∧ p.2.val = q.2.val then 1 else 0

/-- **COMPRESSION**: on the first four basis vectors `a G₀ + b G₁` acts as `a · 1`. -/
theorem inc_compress (a b : ℂ) (ha : a ≠ 0) :
    (a⁻¹ • incᴴ) * (a • G₀ + b • G₁) * inc = 1 := by
  ext ⟨x, j⟩ ⟨y, l⟩
  fin_cases x <;> fin_cases y <;> fin_cases j <;> fin_cases l <;>
    simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_three, inc, G₀_apply, G₁_apply] <;>
    field_simp

/-- **THE GAP CHANNEL IS NOT GAP-ADMISSIBLE AT LEVEL THREE.** -/
theorem gapChannel_not_gap : ¬ Gap 3 gapChannel := by
  rintro ⟨ι, _, K, hK, hgap⟩
  choose a b hab using kraus_of_gapChannel K hK
  -- normalization
  have hnorm : ∑ i, (K i)ᴴ * K i = 1 := by
    refine sum_conjTranspose_mul_eq_one_of_trace K fun X => ?_
    have h := congrArg (fun Φ => (Φ X).trace) hK
    simp only [LinearMap.sum_apply, Matrix.trace_sum] at h
    rw [gapChannel_trace] at h
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
      simp [Matrix.mul_apply, Matrix.conjTranspose_apply, G₁_apply]
    simp only [Finset.sum_congr rfl fun i _ => hz i, Finset.sum_const_zero, zero_ne_one] at h00
  obtain ⟨i, hai⟩ := hex
  rcases hgap i with hu | ⟨ι', _, P, Q, hι', hPQ⟩
  · -- the invertible case: a kernel vector
    rw [hab i] at hu
    exact gap_not_isUnit hai hu
  · -- the factor case: rank four cannot factor through three dimensions
    have hPQ' : a i • G₀ + b i • G₁ = P * Q := (hab i).symm.trans hPQ
    have hone : (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        = ((a i)⁻¹ • incᴴ * P) * (Q * inc) := by
      rw [← inc_compress (a i) (b i) hai, hPQ']
      simp only [Matrix.mul_assoc]
    have hrank : (((a i)⁻¹ • incᴴ * P) * (Q * inc)).rank ≤ 3 :=
      ((Matrix.rank_mul_le_left _ _).trans (Matrix.rank_le_card_width _)).trans hι'
    rw [← hone, Matrix.rank_one, card_carrier] at hrank
    norm_num at hrank

end Obstruction

/-! ### Section G — the permutation dilation and the obstruction -/

section Dilation

/-- The `6 × 6` dilation on (qutrit ancilla, fresh qubit): the single transposition
`|2, 0⟩ ↔ |0, 1⟩`, identity elsewhere. -/
def wG : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ :=
  Matrix.of fun x y =>
    if y = (2, 0) then (if x = (0, 1) then 1 else 0)
    else if y = (0, 1) then (if x = (2, 0) then 1 else 0)
    else if x = y then 1 else 0

theorem wG_isometry : wGᴴ * wG = 1 := by
  ext ⟨x1, x2⟩ ⟨y1, y2⟩
  fin_cases x1 <;> fin_cases x2 <;> fin_cases y1 <;> fin_cases y2 <;>
    simp [Matrix.mul_apply, Matrix.conjTranspose_apply, wG]

/-- The reindexing that puts the system slot first. -/
def dilIdx3 : Fin 2 × (Fin 3 × Fin 2) ≃ (Fin 2 × Fin 3) × Fin 2 :=
  (Equiv.prodAssoc (Fin 2) (Fin 3) (Fin 2)).symm

/-- The dilation on `(Fin 2 × Fin 3) × Fin 2`: identity on the system, `wG` on the two
ancillas. A permutation matrix — no isometry extension is invoked. -/
def WG : Matrix ((Fin 2 × Fin 3) × Fin 2) ((Fin 2 × Fin 3) × Fin 2) ℂ :=
  Matrix.reindex dilIdx3 dilIdx3 ((1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ wG)

theorem WG_isometry : WGᴴ * WG = 1 :=
  reindex_isometry dilIdx3 _ (one_kronecker_isometry wG_isometry)

theorem WG_apply (a b : Fin 2) (j l : Fin 3) (k f : Fin 2) :
    WG ((a, j), k) ((b, l), f) = if a = b then wG (j, k) (l, f) else 0 := by
  simp only [WG, Matrix.reindex_apply, Matrix.submatrix_apply, dilIdx3, Equiv.symm_symm,
    Equiv.prodAssoc_apply, Matrix.kronecker_apply, Matrix.one_apply, ite_mul, one_mul, zero_mul]

/-- **THE CIRCUIT IDENTITY**: `WG · E_0 = V_{![G₀, G₁]}`. -/
theorem WG_esf : WG * Esf (0 : Fin 2) = Vsf ![G₀, G₁] := by
  ext ⟨⟨a, j⟩, k⟩ ⟨b, l⟩
  rw [Matrix.mul_apply, Fintype.sum_prod_type]
  simp only [Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_three, Esf, Matrix.of_apply,
    Vsf, WG_apply]
  fin_cases a <;> fin_cases b <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [wG, G₀_apply, G₁_apply]

end Dilation

/-- **NO SHIFTED THEORY AT LEVEL THREE.** There is no operational theory on the composite
carrier `Fin 2 × Fin 3` whose system families are the rank-gap theory's level-three families
and which has composite unitary control: the round-25 circuit with the permutation dilation
`WG` would make the gap channel available. -/
theorem gap_no_shift :
    ¬ ∃ T' : FiniteOperationalTheory (Fin 2 × Fin 3),
      (∀ (O : Type) [Fintype O] [DecidableEq O]
        (F : O → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ →ₗ[ℂ]
          Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ),
        T'.avail O F ↔ gapTheory.availExt 3 O F)
        ∧ HasCompositeUnitaryControl T' := by
  rintro ⟨T', hav, hctrl⟩
  have hcirc := circuit_available_pureSeed T' hctrl 1 0 WG WG_isometry
  rw [show (fun k => discardMap (1 + 1) (0 : Fin (1 + 1))
        ((localLuders k).comp (conjChannel WG)))
      = fun k => conjChannel (![G₀, G₁] k) from by
    funext k
    exact LinearMap.ext fun ρ => stinespringCircuit_branch ![G₀, G₁] 0 k WG WG_esf ρ] at hcirc
  have hco := T'.avail_coarse (Fin (1 + 1)) Unit _ (fun _ => ()) hcirc
  have hfun : (fun a : Unit => ∑ j ∈ Finset.univ.filter (fun _ : Fin (1 + 1) => () = a),
      conjChannel (![G₀, G₁] j)) = fun _ => gapChannel := by
    funext a
    rw [Finset.filter_true_of_mem (fun _ _ => rfl), Fin.sum_univ_two]
    rfl
  rw [hfun] at hco
  exact gapChannel_not_gap (((hav Unit _).mp hco).1 ())

/-- **THE CLOSURE RULE FAILS IN THE RANK-GAP THEORY.** -/
theorem gap_not_iteratedAncillaClosure : ¬ IteratedAncillaClosure gapTheory :=
  fun h => gap_no_shift
    ⟨shift gapTheory gap_control gap_inert h 3,
      fun _ _ _ _ => Iff.rfl, shift_control gapTheory gap_control gap_inert h 3⟩

/-- **COMPOSITE COMPLETENESS FAILS**: the gap channel is a normalized Kraus instrument on the
level-three carrier that is not available. -/
theorem gap_not_fullComposite : ¬ HasFullCompositeInstruments gapTheory := by
  intro h
  have hav := h 2 1 1 ![G₀, G₁] (fun _ => 0) (by rw [Fin.sum_univ_two]; exact gap_gram)
  have hfun : instrumentBranch ![G₀, G₁] (fun _ : Fin 2 => (0 : Fin 1))
      = fun _ => gapChannel := by
    funext a
    show ∑ k ∈ Finset.univ.filter (fun _ : Fin 2 => (0 : Fin 1) = a), conjChannel (![G₀, G₁] k)
      = gapChannel
    rw [Finset.filter_true_of_mem (fun _ _ => Subsingleton.elim _ _), Fin.sum_univ_two]
    rfl
  rw [hfun] at hav
  exact gapChannel_not_gap (hav.1 0)

theorem gap_not_exactComposite : ¬ ExactCompositeQuantumOps gapTheory :=
  fun h => gap_not_fullComposite ((exactComposite_iff _).mp h).2

theorem gap_not_exactAll : ¬ ExactAllFiniteEndomorphicQuantumOps gapTheory :=
  fun h => gap_not_exactComposite h.2

theorem gap_not_physical : ¬ PhysicalCompletionConditions gapTheory :=
  fun h => gap_not_iteratedAncillaClosure h.2.2.2.1

/-! ### Section H — the closure cell and the five-way minimality theorem -/

/-- **THE CLOSURE CELL IS CLOSED.** A theory with validity, inert spectators, full composite
control and system-to-level-one, realizing the sealed OI core, that fails iterated ancilla
closure. -/
theorem closure_cell_closed :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ IteratedAncillaClosure T :=
  ⟨gapTheory, gap_validity, gap_inert, gap_control, gap_systemToLevelOne,
    gap_realizesSealedOICore, gap_not_iteratedAncillaClosure⟩

/-- **FIVE-WAY MINIMALITY.** For each of the five physical completion conditions, the same
finite OI framework admits a theory satisfying the other four, realizing the sealed OI core,
and failing exactly that one: validity (`everywhereAvailable`), inert spectators (the
round-34 countermodel), full control (`diagTheory`), iterated ancilla closure (`gapTheory`),
system-to-level-one (`systemLoose`). With `exactAll_iff_physical`, the characterization of
exact finite operational QM by the five conditions is minimal in every cell. -/
theorem five_way_minimality :
    (∃ T : FiniteOperationalTheory (Fin 2),
      InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ CompositeOperationalValidity T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ InertSpectatorCompositionality T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ HasCompositeUnitaryControl T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ IteratedAncillaClosure T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ RealizesSealedOICore T
        ∧ ¬ SystemToLevelOne T) :=
  ⟨validity_independent, inert_independent, control_independent, closure_cell_closed,
    levelOne_independent'⟩

#print axioms isUnit_of_left_inverse
#print axioms inv_mul_of_isUnit
#print axioms gapOp_mul
#print axioms gapOp_unitary
#print axioms gap_conjChannel
#print axioms gap_zero
#print axioms gap_add
#print axioms gap_sum
#print axioms gap_comp
#print axioms gap_cp
#print axioms inv2_mul
#print axioms ext_two_one
#print axioms factor_of_singular
#print axioms twoByTwo_dichotomy
#print axioms gapOp_one
#print axioms gap_localLuders
#print axioms gap_exact
#print axioms gap_control
#print axioms gap_krausSoundExt
#print axioms gap_validity
#print axioms gap_realizesSealedOICore
#print axioms gap_systemToLevelOne
#print axioms gapOp_withSpectator
#print axioms gap_withSpectator
#print axioms gap_parallelReferenceExtension
#print axioms gap_inert
#print axioms qutrit_gram
#print axioms gap_gram
#print axioms gapChannel_trace
#print axioms gapChannel_isKraus
#print axioms G₀_apply
#print axioms G₁_apply
#print axioms vecOf_G₀_ne
#print axioms vecOf_G₁_ne
#print axioms vecOf_G_orth
#print axioms kraus_of_gapChannel
#print axioms gap_mulVec_kerVec
#print axioms gap_not_isUnit
#print axioms inc_compress
#print axioms gapChannel_not_gap
#print axioms wG_isometry
#print axioms WG_isometry
#print axioms WG_apply
#print axioms WG_esf
#print axioms gap_no_shift
#print axioms gap_not_iteratedAncillaClosure
#print axioms gap_not_fullComposite
#print axioms gap_not_exactComposite
#print axioms gap_not_exactAll
#print axioms gap_not_physical
#print axioms closure_cell_closed
#print axioms five_way_minimality

end RankGapTheory
end OIBridge
