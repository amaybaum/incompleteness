/-
  OIBridge/SubstantiveCensus.lean — the alternative-theory census: every failure pattern of
  the three substantive completion principles is realized by a well-formed theory carrying the
  sealed OI core.

  ROUND FIFTY-TWO. `GeneralCarrier.lean` splits the five completion conditions into two
  well-formedness requirements (valid probabilities, trivial-ancilla consistency) and three
  substantive selection principles — inert spectators, sufficient reversible control, iterated
  composition — and proves exact finite operational QM is exactly the three principles on a
  well-formed theory (`exactAll_iff_substantive`). The five-way audit of round forty-four
  separates each principle from the others by a witness failing exactly that one. This file
  asks the next question: which SUBSETS of the three principles can fail together? All of
  them. For every one of the `2³ = 8` failure patterns there is a well-formed theory realizing
  the sealed OI core whose failure set is exactly that pattern (`substantive_census`). Hence
  no Boolean relation whatever holds among the three principles on the class of well-formed
  OI-compatible theories (`no_boolean_relation`): they are three independent axes, and QM is
  the single cell in which none fails.

  THE WITNESSES. Four cells are the existing theories: the exact theory (no failure), the
  round-34 countermodel (inert spectators fail), the diagonal theory (control fails), the
  rank-gap theory (iterated composition fails). The four multi-failure cells are new, and all
  are cut out of one construction (`classTheory`): a theory is specified by a per-level class
  of composite maps closed under composition, coarse-graining and the Lüders readout, whose
  members are 2-positive, together with a system-level class and a preparation class. Then:

      {control, closure}         `diagGapTheory`   — CP, diagonal-preserving, and
                                                     gap-admissible up to level three;
      {inert, control}           `diagTwoPosTheory` — 2-positive and diagonal-preserving;
      {inert, closure}           `cappedTheory`     — 2-positive, completely positive up to
                                                     level three;
      {inert, control, closure}  `cappedDiagTheory` — the last two restrictions together.

  The level cap is the one new device: a class that is strictly smaller at low levels than at
  high levels breaks the closure rule (a high-level map's ancilla discard lands outside the
  low-level class) without touching control, and a class admitting 2-positive non-CP maps at
  high levels breaks inert spectators there. The reduction-type map `(2·tr(X)·I − X)/(2d − 1)`
  on a `d`-level carrier (`redMap`) is 2-positive for every `d`, not 3-positive for `d ≥ 3`
  (`amplRef_redMap_ent3_not_posSemidef`), and its ancilla discard is `(4·tr(X)·I − X)/23`,
  not completely positive on six levels (`traceShift_not_cp`); the level-six gap channel of
  round forty-four, tensored with an untouched ancilla, is CP and diagonal-preserving at level
  six and discards to a map that is not gap-admissible at level three (`gapChannel_not_gap`).

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `substantive_census (fI fC fK : Bool)`: a well-formed theory realizing the     │
      │      sealed OI core fails inert spectators iff `fI`, control iff `fC`, and     │
      │      iterated composition iff `fK`.                                            │
      │  `no_boolean_relation`: no Boolean relation among the three principles holds  │
      │      on all well-formed OI-compatible theories.                                │
      │  `qm_is_the_top_cell`: the no-failure cell is exactly finite operational QM.   │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHAT IS AND IS NOT CLAIMED. Proved: everything above, on the qubit carrier, with the usual
  axiom footprint. NOT claimed: that any cell is physically realized; that the witnesses are
  canonical representatives of their cells (they are existence witnesses, chosen for the
  shortest proofs); anything about the two well-formedness conditions failing together with
  substantive ones; that OI selects any cell. The completion classification is unchanged.
  No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.OrbitReachability

namespace OIBridge
namespace SubstantiveCensus

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier

open scoped ComplexOrder Kronecker

/-! ### Section A — the reduction-type map on a general carrier -/

section Reduction

variable (S : Type) [Fintype S] [DecidableEq S]

/-- The trace of `Φ₂` on `d` levels is `(2d − 1)/7` times the trace. -/
theorem reduction2_trace_card (X : Matrix S S ℂ) :
    (reduction2 S X).trace = (7 : ℂ)⁻¹ * (2 * Fintype.card S - 1) * X.trace := by
  rw [reduction2_apply, Matrix.trace_smul, Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_one]
  simp only [smul_eq_mul]
  ring

/-- The normalizing constant `7/(2d − 1)`. -/
noncomputable def kappa : ℝ := 7 / (2 * (Fintype.card S : ℝ) - 1)

omit [DecidableEq S] in
theorem two_card_sub_one_ne_zero : (2 * (Fintype.card S : ℝ) - 1) ≠ 0 := by
  intro h
  have h2 : (2 * Fintype.card S : ℝ) = 1 := by linarith
  norm_cast at h2
  omega

omit [DecidableEq S] in
theorem kappa_pos [Nonempty S] : 0 < kappa S := by
  have : (1 : ℝ) ≤ Fintype.card S := by exact_mod_cast Fintype.card_pos
  have h : 0 < 2 * (Fintype.card S : ℝ) - 1 := by linarith
  exact div_pos (by norm_num) h

/-- **THE NORMALIZED REDUCTION MAP** `(2·tr(X)·I − X)/(2d − 1)`, trace preserving on every
carrier. -/
noncomputable def redMap : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ :=
  ((kappa S : ℝ) : ℂ) • reduction2 S

variable {S}

theorem redMap_apply (X : Matrix S S ℂ) : redMap S X = ((kappa S : ℝ) : ℂ) • reduction2 S X := rfl

theorem redMap_trace (X : Matrix S S ℂ) : (redMap S X).trace = X.trace := by
  rw [redMap_apply, Matrix.trace_smul, reduction2_trace_card, smul_eq_mul, kappa]
  have h := two_card_sub_one_ne_zero S
  have h' : (2 * (Fintype.card S : ℂ) - 1) ≠ 0 := by
    intro hc
    apply h
    have := congrArg Complex.re hc
    simpa using this
  push_cast
  field_simp

omit [Fintype S] [DecidableEq S] in
theorem ampl2_smul_map (c : ℂ) (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) : ampl2 (c • Φ) M = c • ampl2 Φ M := by
  ext p q
  simp only [ampl2, Matrix.of_apply, LinearMap.smul_apply, Matrix.smul_apply]

omit [Fintype S] [DecidableEq S] in
theorem amplRef_smul_map (R : Type) [Fintype R] [DecidableEq R] (c : ℂ)
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (M : Matrix (R × S) (R × S) ℂ) :
    amplRef R (c • Φ) M = c • amplRef R Φ M := by
  ext p q
  simp only [amplRef, Matrix.of_apply, LinearMap.smul_apply, Matrix.smul_apply]

theorem redMap_twoPositive [Nonempty S] : IsTwoPositive (redMap S) := by
  intro M hM
  rw [redMap, ampl2_smul_map]
  exact (reduction2_twoPositive M hM).smul (Complex.zero_le_real.mpr (kappa_pos S).le)

theorem reduction2_preservesDiag : PreservesDiag (reduction2 S) := by
  intro w
  refine ⟨fun i => (7 : ℂ)⁻¹ * (2 * ∑ j, w j - w i), ?_⟩
  ext i j
  by_cases h : i = j
  · subst h
    simp [reduction2_apply, Matrix.trace_diagonal]
  · simp [reduction2_apply, h]

theorem redMap_preservesDiag : PreservesDiag (redMap S) := by
  intro w
  obtain ⟨w', hw'⟩ := reduction2_preservesDiag (S := S) w
  exact ⟨((kappa S : ℝ) : ℂ) • w', by rw [redMap_apply, hw', Matrix.diagonal_smul]⟩

/-- The rank-three entangled vector `Σ_{i<3} |i⟩|ι i⟩` along an injection `ι : Fin 3 → S`. -/
def ent3 (ι : Fin 3 → S) : Fin 3 × S → ℂ := fun p => if ι p.1 = p.2 then 1 else 0

variable (ι : Fin 3 → S)

omit [Fintype S] in
theorem ent3_star : star (ent3 ι) = ent3 ι := by
  funext p
  simp only [Pi.star_apply, ent3]
  split_ifs <;> simp

theorem ent3_norm : star (ent3 ι) ⬝ᵥ ent3 ι = 3 := by
  rw [ent3_star]
  have hterm : ∀ p : Fin 3 × S, ent3 ι p * ent3 ι p = if ι p.1 = p.2 then (1 : ℂ) else 0 := by
    intro p
    simp only [ent3]
    split_ifs <;> simp
  simp only [dotProduct, hterm, Fintype.sum_prod_type, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, mul_one]
  norm_num

theorem refMarginalR_ent3 (hι : Function.Injective ι) :
    refMarginalR (Matrix.vecMulVec (ent3 ι) (star (ent3 ι))) = 1 := by
  ext i j
  rw [ent3_star]
  simp only [refMarginalR, Matrix.of_apply, Matrix.vecMulVec_apply, ent3]
  rw [Finset.sum_eq_single (ι i)]
  · rw [if_pos rfl, one_mul, Matrix.one_apply]
    by_cases h : i = j
    · rw [if_pos (by rw [h]), if_pos h]
    · rw [if_neg (fun hh => h (hι hh).symm), if_neg h]
  · intro m _ hm
    rw [if_neg (Ne.symm hm), zero_mul]
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem amplRef_reduction2_ent3 (hι : Function.Injective ι) :
    amplRef (Fin 3) (reduction2 S) (Matrix.vecMulVec (ent3 ι) (star (ent3 ι)))
      = (7 : ℂ)⁻¹ • ((2 : ℂ) • (1 : Matrix (Fin 3 × S) (Fin 3 × S) ℂ)
          - Matrix.vecMulVec (ent3 ι) (star (ent3 ι))) := by
  rw [amplRef_reduction2, refMarginalR_ent3 ι hι, tensorOf_one_one]

/-- **THE QUTRIT WITNESS ON ANY CARRIER**: exactly `−3/7`. -/
theorem amplRef_reduction2_ent3_form (hι : Function.Injective ι) :
    star (ent3 ι) ⬝ᵥ (amplRef (Fin 3) (reduction2 S)
      (Matrix.vecMulVec (ent3 ι) (star (ent3 ι))) *ᵥ ent3 ι) = -3 / 7 := by
  have hN := ent3_norm ι
  rw [amplRef_reduction2_ent3 ι hι, Matrix.smul_mulVec, Matrix.sub_mulVec, Matrix.smul_mulVec,
    Matrix.one_mulVec, vecMulVec_mulVec', dotProduct_smul, dotProduct_sub, dotProduct_smul,
    dotProduct_smul, hN, smul_eq_mul, smul_eq_mul, smul_eq_mul]
  ring

/-- **`redMap` IS NOT 3-POSITIVE** on any carrier with three levels. -/
theorem amplRef_redMap_ent3_not_posSemidef [Nonempty S] (hι : Function.Injective ι) :
    ¬ (amplRef (Fin 3) (redMap S) (Matrix.vecMulVec (ent3 ι) (star (ent3 ι)))).PosSemidef := by
  intro h
  have hq := h.dotProduct_mulVec_nonneg (ent3 ι)
  rw [redMap, amplRef_smul_map, Matrix.smul_mulVec, dotProduct_smul,
    amplRef_reduction2_ent3_form ι hι, smul_eq_mul] at hq
  have hcast : ((kappa S : ℝ) : ℂ) * (-3 / 7) = ((kappa S * (-3 / 7) : ℝ) : ℂ) := by push_cast; ring
  rw [hcast, ← Complex.ofReal_zero, Complex.real_le_real] at hq
  have := kappa_pos S
  nlinarith

variable (S) in
/-- **THE TRACE-SHIFT MAP** `X ↦ a·tr(X)·I − X`. -/
noncomputable def traceShift (a : ℂ) : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun X := (a * X.trace) • (1 : Matrix S S ℂ) - X
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

theorem traceShift_apply (a : ℂ) (X : Matrix S S ℂ) :
    traceShift S a X = (a * X.trace) • (1 : Matrix S S ℂ) - X := rfl

theorem choiMatrix_traceShift (a : ℂ) :
    choiMatrix (traceShift S a)
      = a • (1 : Matrix (S × S) (S × S) ℂ) - Matrix.vecMulVec maxEntVec (star maxEntVec) := by
  ext p q
  rw [maxEntVec_star]
  show (traceShift S a (Matrix.single p.1 q.1 1)) p.2 q.2 = _
  rw [traceShift_apply, trace_single_one]
  obtain ⟨p1, p2⟩ := p
  obtain ⟨q1, q2⟩ := q
  simp only [Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul, Matrix.vecMulVec_apply,
    single_entry, maxEntVec, Matrix.one_apply, Prod.mk.injEq, ite_and_one_zero]
  ring

theorem traceShift_choi_form (a : ℂ) :
    star (maxEntVec (S := S)) ⬝ᵥ (choiMatrix (traceShift S a) *ᵥ maxEntVec)
      = a * Fintype.card S - Fintype.card S * Fintype.card S := by
  have hN := maxEntVec_norm (S := S)
  rw [choiMatrix_traceShift, Matrix.sub_mulVec, Matrix.smul_mulVec, Matrix.one_mulVec,
    vecMulVec_mulVec', dotProduct_sub, dotProduct_smul, dotProduct_smul, hN, smul_eq_mul,
    smul_eq_mul]

/-- **NOT COMPLETELY POSITIVE** when `0 ≤ a < d`. -/
theorem traceShift_not_cp (a : ℝ) (ha0 : 0 ≤ a) (ha : a < Fintype.card S) :
    ¬ IsCompletelyPositive (traceShift S (a : ℂ)) := by
  intro h
  have hq := h.dotProduct_mulVec_nonneg maxEntVec
  rw [traceShift_choi_form] at hq
  have hcast : (a : ℂ) * (Fintype.card S : ℂ) - (Fintype.card S : ℂ) * (Fintype.card S : ℂ)
      = ((a * Fintype.card S - Fintype.card S * Fintype.card S : ℝ) : ℂ) := by push_cast; ring
  rw [hcast, ← Complex.ofReal_zero, Complex.real_le_real] at hq
  nlinarith

end Reduction

/-! ### Section B — theories cut out by a per-level class of composite maps -/

section Builder

/-- **A CLASS SPECIFICATION**: a per-level class `P` of composite maps, a system-level class
`Q`, a preparation class `QP`, and the closure properties a finite operational theory
consumes. Every member of `P` is 2-positive, so validity, reference-tested preparations and
the Kraus form of ancilla discards come for free. -/
structure ClassData where
  P : ∀ N : ℕ, (Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) → Prop
  Q : (Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ) → Prop
  QP : ∀ n : ℕ, (Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) → Prop
  twoPos : ∀ N Φ, P N Φ → IsTwoPositive Φ
  comp : ∀ N Φ Ψ, P N Φ → P N Ψ → P N (Φ.comp Ψ)
  sum : ∀ N (ι : Type) [Fintype ι] (s : Finset ι)
    (Φ : ι → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ),
    (∀ i ∈ s, P N (Φ i)) → P N (∑ i ∈ s, Φ i)
  luders : ∀ N (k : Fin N), P N (localLuders k)
  Q_id : Q LinearMap.id
  Q_sum : ∀ (ι : Type) [Fintype ι] (s : Finset ι)
    (Φ : ι → Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ),
    (∀ i ∈ s, Q (Φ i)) → Q (∑ i ∈ s, Φ i)
  QP_uniform : ∀ n, QP (n + 1) (uniformAttach (n + 1))
  QP_post : ∀ n P' Φ, QP n P' → P n Φ → QP n (Φ.comp P')
  Q_discard : ∀ n P' Φ, QP n P' → P n Φ → Q (discardWith n P' Φ)

/-- **THE THEORY CUT OUT BY A CLASS**: Kraus families in `Q` on the system, `P`-families with
aggregate trace on every composite, reference-tested preparations in `QP`, Lüders readout. -/
noncomputable def classTheory (C : ClassData) : FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ F => IsKrausFamily F ∧ ∀ a, C.Q (F a)
  availExt := fun N _ _ _ F => (∀ a, C.P N (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace
  avail_id := ⟨scalarAvail_isKraus
    ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
      rw [Complex.ofReal_one, one_smul]⟩, fun _ => C.Q_id⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f ⟨hF, hQ⟩
    exact ⟨isKrausFamily_coarse hF f, fun a' => C.Q_sum _ _ _ fun j _ => hQ j⟩
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => C.sum _ _ _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => C.comp _ _ _ ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => RefTestedPrep n P ∧ C.QP n P
  prepAvail_uniform := fun n =>
    ⟨⟨uniformAttach_trace (n + 1) n.succ_ne_zero,
      amplR_uniformAttach_posSemidef (Matrix.posSemidef_vecMulVec_self_star _) _⟩,
      C.QP_uniform n⟩
  prepAvail_post := by
    rintro n P Φ ⟨⟨hPtr, hPpsd⟩, hPQ⟩ ⟨hΦ2, hΦtr⟩
    refine ⟨⟨fun ρ => ?_, ?_⟩, C.QP_post _ _ _ hPQ (hΦ2 ())⟩
    · show (Φ (P ρ)).trace = ρ.trace
      have h := hΦtr (P ρ)
      rw [Fintype.sum_unique] at h
      rw [h, hPtr]
    · rw [amplR_comp]
      exact C.twoPos _ _ (hΦ2 ()) _ hPpsd
  readout := fun _ k => localLuders k
  readout_avail := fun n => ⟨fun k => C.luders n k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨⟨hPtr, hPpsd⟩, hPQ⟩ ⟨hF2, hFtr⟩
    refine ⟨isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) _
      (fun a => ?_) (fun X => ?_), fun a => C.Q_discard _ _ _ hPQ (hF2 a)⟩
    · show (choiMatrix (discardWith n P (F a))).PosSemidef
      rw [choiMatrix_eq_ampl2, ← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp]
      exact amplR_ptraceAncL_posSemidef (C.twoPos _ _ (hF2 a) _ hPpsd)
    · rw [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) X, hFtr (P X), hPtr X]

variable (C : ClassData)

theorem classTheory_availExt_iff (N : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) :
    (classTheory C).availExt N O F ↔
      (∀ a, C.P N (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace := Iff.rfl

/-- **VALIDITY**, from 2-positivity. -/
theorem classTheory_validity : CompositeOperationalValidity (classTheory C) := by
  intro n O _ _ F ⟨hP, htr⟩
  exact ⟨fun a X hX => positive_of_twoPositive (C.twoPos _ _ (hP a)) hX, htr⟩

/-- **TRIVIAL-ANCILLA CONSISTENCY**, given that the level-one class receives the transported
system families. -/
theorem classTheory_systemToLevelOne
    (h1 : ∀ (O : Type) [Fintype O] [DecidableEq O]
      (F : O → Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ),
      IsKrausFamily F → (∀ a, C.Q (F a)) →
        ∀ a, C.P 1 (transport (levelOneIdx (Fin 2)).symm (F a))) :
    SystemToLevelOne (classTheory C) := by
  rintro O _ _ F ⟨hK, hQ⟩
  refine ⟨h1 O F hK hQ, fun X => ?_⟩
  simp only [trace_transport]
  rw [(krausFamily_cp_tr hK).2, trace_reindex]

theorem classTheory_wellFormed
    (h1 : ∀ (O : Type) [Fintype O] [DecidableEq O]
      (F : O → Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ),
      IsKrausFamily F → (∀ a, C.Q (F a)) →
        ∀ a, C.P 1 (transport (levelOneIdx (Fin 2)).symm (F a))) :
    WellFormed (classTheory C) :=
  ⟨classTheory_validity C, classTheory_systemToLevelOne C h1⟩

theorem classTheory_relabel
    (hperm : ∀ g : Equiv.Perm Core,
      C.P 4 (transport coreIdx (correlationExtension g (onesCorr Core)))) (g : Equiv.Perm Core) :
    (classTheory C).availExt 4 Unit
      (fun _ => transport coreIdx (correlationExtension g (onesCorr Core))) := by
  refine ⟨fun _ => hperm g, fun X => ?_⟩
  rw [Fintype.sum_unique, correlationExtension_ones_eq_conjChannel, transport_conjChannel]
  exact conjChannel_trace _ (reindex_isometry _ _ (permMatrix_isometry g)) X

/-- **THE SEALED OI CORE IS REALIZED** once the level-four class contains the core
relabellings. -/
theorem classTheory_realizes
    (hperm : ∀ g : Equiv.Perm Core,
      C.P 4 (transport coreIdx (correlationExtension g (onesCorr Core)))) :
    RealizesSealedOICore (classTheory C) := by
  refine ⟨core_isC1C4, classTheory_relabel C hperm sigmaPerm, classTheory_relabel C hperm tauPerm,
    fun r => ?_, ?_, realizedFold_diagonal⟩
  · rw [readVisible_eq_localLuders, readout_is_localLuders]
  · rw [readVisible_family_eq (classTheory C)]
    exact readout_relabel_available (classTheory C)

/-- **INERT SPECTATORS** hold when the class is closed under spectator extension. -/
theorem classTheory_inert
    (hspec : ∀ (R : Type) [Fintype R] [DecidableEq R] (n m : ℕ)
      (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
      (Φ : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ),
      C.P n Φ → C.P m (withSpectator R e Φ)) :
    InertSpectatorCompositionality (classTheory C) := by
  refine (inertSpectator_iff_parallelReferenceExtension _).mpr ?_
  intro R _ _ n m e O _ _ F ⟨hP, htr⟩
  refine ⟨fun a => hspec R n m e _ (hP a), fun X => ?_⟩
  simp only [withSpectator_apply, trace_reindex, trace_amplRef]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun i _ => htr (refBlockR (Matrix.reindex e.symm e.symm X) i i),
    ← trace_eq_sum_refBlockR, trace_reindex]

/-- **FULL CONTROL** holds when every unitary conjugation is in the class. -/
theorem classTheory_control
    (hU : ∀ N (U : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ), Uᴴ * U = 1 →
      C.P N (conjChannel U)) :
    HasCompositeUnitaryControl (classTheory C) :=
  fun N U h => ⟨fun _ => hU N U h, fun X => by
    rw [Fintype.sum_unique]
    exact conjChannel_trace U h X⟩

/-- **ITERATED COMPOSITION** holds when the class is closed under uniform-ancilla discard. -/
theorem classTheory_closure
    (hdisc : ∀ (n m : ℕ)
      (Φ : Matrix ((Fin 2 × Fin n) × Fin (m + 1)) ((Fin 2 × Fin n) × Fin (m + 1)) ℂ →ₗ[ℂ]
        Matrix ((Fin 2 × Fin n) × Fin (m + 1)) ((Fin 2 × Fin n) × Fin (m + 1)) ℂ),
      C.P (n * (m + 1)) (transport (shiftIdx (Fin 2) n (m + 1)) Φ) →
        C.P n (discardWith (A := Fin 2 × Fin n) (m + 1) (uniformAttach (m + 1)) Φ)) :
    IteratedAncillaClosure (classTheory C) := by
  intro n m O _ _ F ⟨h2, htr⟩
  refine ⟨fun a => hdisc n m (F a) (h2 a), fun X => ?_⟩
  rw [Finset.sum_congr rfl fun a _ => discardWith_trace (m + 1) _ (F a) X]
  have h := htr (Matrix.reindex (shiftIdx (Fin 2) n (m + 1)) (shiftIdx (Fin 2) n (m + 1))
    (uniformAttach (m + 1) X))
  simp only [transport_reindex, trace_reindex] at h
  rw [h, uniformAttach_trace (m + 1) m.succ_ne_zero]

/-- **CONTROL FAILS** at one unitary outside the class. -/
theorem classTheory_not_control {N : ℕ} {U : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ}
    (hU : Uᴴ * U = 1) (h : ¬ C.P N (conjChannel U)) :
    ¬ HasCompositeUnitaryControl (classTheory C) :=
  fun hc => h ((hc N U hU).1 ())

/-- **ITERATED COMPOSITION FAILS** at one available map whose discard leaves the class. -/
theorem classTheory_not_closure {n m : ℕ}
    {Φ : Matrix ((Fin 2 × Fin n) × Fin (m + 1)) ((Fin 2 × Fin n) × Fin (m + 1)) ℂ →ₗ[ℂ]
      Matrix ((Fin 2 × Fin n) × Fin (m + 1)) ((Fin 2 × Fin n) × Fin (m + 1)) ℂ}
    (hP : C.P (n * (m + 1)) (transport (shiftIdx (Fin 2) n (m + 1)) Φ))
    (htr : ∀ X, (transport (shiftIdx (Fin 2) n (m + 1)) Φ X).trace = X.trace)
    (h : ¬ C.P n (discardWith (A := Fin 2 × Fin n) (m + 1) (uniformAttach (m + 1)) Φ)) :
    ¬ IteratedAncillaClosure (classTheory C) :=
  fun hc => h ((hc n m Unit (fun _ => Φ)
    ⟨fun _ => hP, fun X => by rw [Fintype.sum_unique]; exact htr X⟩).1 ())

/-- **INERT SPECTATORS FAIL** at one available map whose spectator extension leaves the
class. -/
theorem classTheory_not_inert {R : Type} [Fintype R] [DecidableEq R] {n m : ℕ}
    (e : R × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    {Φ : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (hP : C.P n Φ) (htr : ∀ X, (Φ X).trace = X.trace) (h : ¬ C.P m (withSpectator R e Φ)) :
    ¬ InertSpectatorCompositionality (classTheory C) :=
  fun hi => h (((inertSpectator_iff_parallelReferenceExtension _).mp hi R n m e Unit (fun _ => Φ)
    ⟨fun _ => hP, fun X => by rw [Fintype.sum_unique]; exact htr X⟩).1 ())

end Builder

/-! ### Section C — the two system profiles and the four classes -/

section Classes

/-- Class data with no system-level restriction. -/
def plainData (P : ∀ N : ℕ, (Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) → Prop)
    (twoPos : ∀ N Φ, P N Φ → IsTwoPositive Φ)
    (comp : ∀ N Φ Ψ, P N Φ → P N Ψ → P N (Φ.comp Ψ))
    (sum : ∀ N (ι : Type) [Fintype ι] (s : Finset ι)
      (Φ : ι → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ),
      (∀ i ∈ s, P N (Φ i)) → P N (∑ i ∈ s, Φ i))
    (luders : ∀ N (k : Fin N), P N (localLuders k)) : ClassData where
  P := P
  Q := fun _ => True
  QP := fun _ _ => True
  twoPos := twoPos
  comp := comp
  sum := sum
  luders := luders
  Q_id := trivial
  Q_sum := fun _ _ _ _ _ => trivial
  QP_uniform := fun _ => trivial
  QP_post := fun _ _ _ _ _ => trivial
  Q_discard := fun _ _ _ _ _ => trivial

/-- Class data whose maps preserve diagonal states at every level. -/
def diagData (P : ∀ N : ℕ, (Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) → Prop)
    (twoPos : ∀ N Φ, P N Φ → IsTwoPositive Φ)
    (comp : ∀ N Φ Ψ, P N Φ → P N Ψ → P N (Φ.comp Ψ))
    (sum : ∀ N (ι : Type) [Fintype ι] (s : Finset ι)
      (Φ : ι → Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ),
      (∀ i ∈ s, P N (Φ i)) → P N (∑ i ∈ s, Φ i))
    (luders : ∀ N (k : Fin N), P N (localLuders k))
    (hdiag : ∀ N Φ, P N Φ → PreservesDiag Φ) : ClassData where
  P := P
  Q := PreservesDiag
  QP := fun _ => PreservesDiagP
  twoPos := twoPos
  comp := comp
  sum := sum
  luders := luders
  Q_id := preservesDiag_id
  Q_sum := fun _ _ s Φ h => preservesDiag_sum s Φ h
  QP_uniform := fun _ => preservesDiagP_uniform _
  QP_post := fun _ P' Φ hP' hΦ w => by
    obtain ⟨u, hu⟩ := hP' w
    obtain ⟨v, hv⟩ := hdiag _ _ hΦ u
    exact ⟨v, by rw [LinearMap.comp_apply, hu, hv]⟩
  Q_discard := fun _ _ _ hP' hΦ => preservesDiag_discardWith hP' (hdiag _ _ hΦ)

/-- Cell {control, closure}: completely positive, diagonal-preserving, gap-admissible up to
level three. -/
def ckP (N : ℕ) (Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  IsCompletelyPositive Φ ∧ PreservesDiag Φ ∧ (N ≤ 3 → Gap N Φ)

/-- Cell {inert, control}: 2-positive and diagonal-preserving. -/
def icP (N : ℕ) (Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  IsTwoPositive Φ ∧ PreservesDiag Φ

/-- Cell {inert, closure}: 2-positive, completely positive up to level three. -/
def ikP (N : ℕ) (Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  IsTwoPositive Φ ∧ (N ≤ 3 → IsCompletelyPositive Φ)

/-- Cell {inert, control, closure}: 2-positive, diagonal-preserving, completely positive up
to level three. -/
def ickP (N : ℕ) (Φ : Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ →ₗ[ℂ]
    Matrix (Fin 2 × Fin N) (Fin 2 × Fin N) ℂ) : Prop :=
  IsTwoPositive Φ ∧ PreservesDiag Φ ∧ (N ≤ 3 → IsCompletelyPositive Φ)

def ckData : ClassData :=
  diagData ckP (fun _ Φ h => cp_referencePositive (Fin 2) Φ h.1)
    (fun _ _ _ hΦ hΨ => ⟨cp_comp hΦ.1 hΨ.1, preservesDiag_comp hΦ.2.1 hΨ.2.1,
      fun hN => gap_comp (hΦ.2.2 hN) (hΨ.2.2 hN)⟩)
    (fun _ _ _ s Φ h => ⟨cp_sum s Φ fun i hi => (h i hi).1,
      preservesDiag_sum s Φ fun i hi => (h i hi).2.1,
      fun hN => gap_sum s Φ fun i hi => (h i hi).2.2 hN⟩)
    (fun N k => ⟨localLuders_cp k, preservesDiag_localLuders k, fun _ => gap_localLuders N k⟩)
    (fun _ _ h => h.2.1)

def icData : ClassData :=
  diagData icP (fun _ _ h => h.1)
    (fun _ _ _ hΦ hΨ => ⟨isTwoPositive_comp hΦ.1 hΨ.1, preservesDiag_comp hΦ.2 hΨ.2⟩)
    (fun _ _ _ s Φ h => ⟨isTwoPositive_sum s Φ fun i hi => (h i hi).1,
      preservesDiag_sum s Φ fun i hi => (h i hi).2⟩)
    (fun _ k => ⟨localLuders_twoPositive k, preservesDiag_localLuders k⟩)
    (fun _ _ h => h.2)

def ikData : ClassData :=
  plainData ikP (fun _ _ h => h.1)
    (fun _ _ _ hΦ hΨ => ⟨isTwoPositive_comp hΦ.1 hΨ.1, fun hN => cp_comp (hΦ.2 hN) (hΨ.2 hN)⟩)
    (fun _ _ _ s Φ h => ⟨isTwoPositive_sum s Φ fun i hi => (h i hi).1,
      fun hN => cp_sum s Φ fun i hi => (h i hi).2 hN⟩)
    (fun _ k => ⟨localLuders_twoPositive k, fun _ => localLuders_cp k⟩)

def ickData : ClassData :=
  diagData ickP (fun _ _ h => h.1)
    (fun _ _ _ hΦ hΨ => ⟨isTwoPositive_comp hΦ.1 hΨ.1, preservesDiag_comp hΦ.2.1 hΨ.2.1,
      fun hN => cp_comp (hΦ.2.2 hN) (hΨ.2.2 hN)⟩)
    (fun _ _ _ s Φ h => ⟨isTwoPositive_sum s Φ fun i hi => (h i hi).1,
      preservesDiag_sum s Φ fun i hi => (h i hi).2.1,
      fun hN => cp_sum s Φ fun i hi => (h i hi).2.2 hN⟩)
    (fun _ k => ⟨localLuders_twoPositive k, preservesDiag_localLuders k, fun _ => localLuders_cp k⟩)
    (fun _ _ h => h.2.1)

/-- **THE DIAGONAL RANK-GAP THEORY** (cell {control, closure}). -/
noncomputable def diagGapTheory : FiniteOperationalTheory (Fin 2) := classTheory ckData
/-- **THE DIAGONAL TWO-POSITIVE THEORY** (cell {inert, control}). -/
noncomputable def diagTwoPosTheory : FiniteOperationalTheory (Fin 2) := classTheory icData
/-- **THE CAPPED TWO-POSITIVE THEORY** (cell {inert, closure}). -/
noncomputable def cappedTheory : FiniteOperationalTheory (Fin 2) := classTheory ikData
/-- **THE CAPPED DIAGONAL TWO-POSITIVE THEORY** (cell {inert, control, closure}). -/
noncomputable def cappedDiagTheory : FiniteOperationalTheory (Fin 2) := classTheory ickData

end Classes

/-! ### Section D — the witnesses for the four multi-failure cells -/

section Witnesses

theorem reindex_reindex {l l' l'' : Type} [Fintype l] [Fintype l'] [Fintype l'']
    (e₁ : l ≃ l') (e₂ : l' ≃ l'') (Y : Matrix l l ℂ) :
    Matrix.reindex e₂ e₂ (Matrix.reindex e₁ e₁ Y) = Matrix.reindex (e₁.trans e₂) (e₁.trans e₂) Y := by
  ext i j
  simp [Matrix.reindex_apply]

theorem transport_trans {l l' l'' : Type} [Fintype l] [Fintype l'] [Fintype l''] [DecidableEq l]
    [DecidableEq l'] [DecidableEq l''] (e₁ : l ≃ l') (e₂ : l' ≃ l'')
    (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    transport e₂ (transport e₁ Φ) = transport (e₁.trans e₂) Φ := by
  refine LinearMap.ext fun N => ?_
  simp only [transport_apply]
  rw [reindex_reindex, reindex_reindex]
  rfl

/-- `Ψ ⊗ id` with the untouched factor in the ancilla slot. -/
def spectatorLast {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    Matrix (S × Fin m) (S × Fin m) ℂ →ₗ[ℂ] Matrix (S × Fin m) (S × Fin m) ℂ :=
  transport (Equiv.prodComm (Fin m) S) (amplRefL (Fin m) Ψ)

theorem transport_spectatorLast (n m : ℕ)
    (Ψ : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) :
    transport (shiftIdx (Fin 2) n m) (spectatorLast m Ψ)
      = withSpectator (Fin m) ((Equiv.prodComm (Fin m) (Fin 2 × Fin n)).trans (shiftIdx (Fin 2) n m)) Ψ := by
  rw [spectatorLast, transport_trans]
  rfl

/-- **DISCARDING AN UNTOUCHED UNIFORM ANCILLA IS THE IDENTITY.** -/
theorem discardWith_uniform_spectatorLast {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (hm : m ≠ 0) (Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    discardWith (A := S) m (uniformAttach m) (spectatorLast m Ψ) = Ψ := by
  refine LinearMap.ext fun X => ?_
  have hblock : ∀ e f : Fin m,
      refBlockR ((uniformAttach m X).submatrix (Equiv.prodComm (Fin m) S)
        (Equiv.prodComm (Fin m) S)) e f = ((((m : ℂ))⁻¹ * if e = f then 1 else 0) : ℂ) • X := by
    intro e f
    ext k l
    simp only [refBlockR, Matrix.of_apply, Matrix.submatrix_apply, Equiv.prodComm_apply,
      Prod.swap_prod_mk, uniformAttach_apply, tensorOf_apply, Matrix.smul_apply, Matrix.one_apply,
      smul_eq_mul]
    ring
  ext s t
  show ptraceAnc m (spectatorLast m Ψ (uniformAttach m X)) s t = Ψ X s t
  rw [ptraceAnc_apply]
  simp only [spectatorLast, transport_apply, amplRefL_apply, amplRef, Matrix.reindex_apply,
    Matrix.submatrix_apply, Matrix.of_apply, Equiv.prodComm_symm, Equiv.prodComm_apply,
    Prod.swap_prod_mk]
  rw [Finset.sum_congr rfl fun e _ => by
    rw [hblock e e, map_smul, Matrix.smul_apply, if_pos rfl, mul_one, smul_eq_mul]]
  rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, ← mul_assoc,
    mul_inv_cancel₀ (Nat.cast_ne_zero.mpr hm), one_mul]

/-- A matrix with at most one nonzero entry in each column. -/
def ColMonomial {l : Type} (K : Matrix l l ℂ) : Prop :=
  ∀ p q r, K p r ≠ 0 → K q r ≠ 0 → p = q

theorem preservesDiag_conjChannel_of_colMonomial {l : Type} [Fintype l] [DecidableEq l]
    {K : Matrix l l ℂ} (hK : ColMonomial K) : PreservesDiag (conjChannel K) := by
  intro w
  refine ⟨fun p => ∑ r, K p r * w r * star (K p r), ?_⟩
  ext p q
  show (K * Matrix.diagonal w * Kᴴ) p q = _
  by_cases hpq : p = q
  · subst hpq
    rw [Matrix.diagonal_apply_eq, Matrix.mul_apply]
    exact Finset.sum_congr rfl fun r _ => by rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply]
  · rw [Matrix.diagonal_apply_ne _ hpq, Matrix.mul_apply]
    refine Finset.sum_eq_zero fun r _ => ?_
    rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply]
    by_cases h1 : K p r = 0
    · rw [h1, zero_mul, zero_mul]
    · by_cases h2 : K q r = 0
      · rw [h2, star_zero, mul_zero]
      · exact absurd (hK p q r h1 h2) hpq

theorem colMonomial_one_kronecker {M : Matrix (Fin 3) (Fin 3) ℂ} (hM : ColMonomial M) :
    ColMonomial ((1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ M) := by
  rintro ⟨a, j⟩ ⟨b, l⟩ ⟨c, k⟩ h1 h2
  simp only [Matrix.kronecker_apply, ne_eq, mul_eq_zero, not_or, Matrix.one_apply] at h1 h2
  obtain ⟨h1a, h1M⟩ := h1
  obtain ⟨h2a, h2M⟩ := h2
  have hac : a = c := by
    by_contra h
    exact h1a (if_neg h)
  have hbc : b = c := by
    by_contra h
    exact h2a (if_neg h)
  rw [hac, hbc, hM j l k h1M h2M]

theorem D3_colMonomial : ColMonomial D3 := by
  intro p q r h1 h2
  fin_cases p <;> fin_cases q <;> fin_cases r <;> simp [D3] at h1 h2 ⊢

theorem E3_colMonomial : ColMonomial E3 := by
  intro p q r h1 h2
  fin_cases p <;> fin_cases q <;> fin_cases r <;> simp [E3] at h1 h2 ⊢

theorem gapChannel_eq_sum : gapChannel = ∑ k : Fin 2, conjChannel (![G₀, G₁] k) := by
  rw [Fin.sum_univ_two]
  rfl

theorem gapChannel_cp : IsCompletelyPositive gapChannel := by
  rw [gapChannel_eq_sum]
  exact cp_sum _ _ fun k _ => conjChannel_cp _

theorem gapChannel_preservesDiag : PreservesDiag gapChannel := by
  rw [gapChannel_eq_sum]
  refine preservesDiag_sum _ _ fun k _ => ?_
  fin_cases k
  · exact preservesDiag_conjChannel_of_colMonomial (colMonomial_one_kronecker D3_colMonomial)
  · exact preservesDiag_conjChannel_of_colMonomial (colMonomial_one_kronecker E3_colMonomial)

/-- The spectator reindexing `Fin 3 × (Fin 2 × Fin 6) ≃ Fin 2 × Fin 18`. -/
def idx18 : Fin 3 × (Fin 2 × Fin 6) ≃ Fin 2 × Fin 18 :=
  (Equiv.prodAssoc _ _ _).symm.trans
    ((Equiv.prodCongr (Equiv.prodComm _ _) (Equiv.refl _)).trans
      ((Equiv.prodAssoc _ _ _).trans (Equiv.prodCongr (Equiv.refl _) finProdFinEquiv)))

/-- Three levels of the level-six carrier. -/
def iota6 : Fin 3 → Fin 2 × Fin 6 := fun i => (0, Fin.castLE (by norm_num) i)

theorem iota6_injective : Function.Injective iota6 :=
  fun _ _ h => Fin.castLE_injective (by norm_num : 3 ≤ 6) (Prod.ext_iff.mp h).2

/-- **THE ANCILLA DISCARD OF THE LEVEL-SIX REDUCTION MAP** is `(4·tr(X)·I − X)/23`. -/
theorem discard_redMap :
    discardWith (A := Fin 2 × Fin 3) 2 (uniformAttach 2) (redMap ((Fin 2 × Fin 3) × Fin 2))
      = ((1 / 23 : ℝ) : ℂ) • traceShift (Fin 2 × Fin 3) ((4 : ℝ) : ℂ) := by
  refine LinearMap.ext fun X => ?_
  have htr : (uniformAttach (A := Fin 2 × Fin 3) 2 X).trace = X.trace :=
    uniformAttach_trace 2 two_ne_zero X
  have hk : kappa ((Fin 2 × Fin 3) × Fin 2) = 7 / 23 := by
    simp only [kappa, Fintype.card_prod, Fintype.card_fin]
    norm_num
  ext s t
  show ptraceAnc 2 (redMap _ (uniformAttach 2 X)) s t = _
  rw [ptraceAnc_apply]
  simp only [redMap_apply, reduction2_apply, htr, hk]
  simp only [LinearMap.smul_apply, Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply,
    uniformAttach_apply, tensorOf_apply, traceShift_apply, smul_eq_mul, Fin.sum_univ_two,
    Prod.mk.injEq, and_true]
  by_cases hst : s = t
  · subst hst
    simp only [if_true]
    push_cast
    ring
  · simp only [hst, if_false]
    push_cast
    ring

theorem discard_redMap_not_cp :
    ¬ IsCompletelyPositive
      (discardWith (A := Fin 2 × Fin 3) 2 (uniformAttach 2) (redMap ((Fin 2 × Fin 3) × Fin 2))) := by
  rw [discard_redMap]
  intro h
  have h1 : (choiMatrix (((1 / 23 : ℝ) : ℂ) • traceShift (Fin 2 × Fin 3) ((4 : ℝ) : ℂ))).PosSemidef := h
  rw [choiMatrix_smul] at h1
  have h2 := h1.smul (Complex.zero_le_real.mpr (show (0 : ℝ) ≤ 23 by norm_num))
  rw [smul_smul] at h2
  have h3 : ((23 : ℝ) : ℂ) * ((1 / 23 : ℝ) : ℂ) = 1 := by push_cast; norm_num
  rw [h3, one_smul] at h2
  exact traceShift_not_cp (S := Fin 2 × Fin 3) 4 (by norm_num)
    (by simp only [Fintype.card_prod, Fintype.card_fin]; norm_num) h2

/-! #### Cell {control, closure}: the diagonal rank-gap theory -/

theorem diagGap_wellFormed : WellFormed diagGapTheory :=
  classTheory_wellFormed ckData (by
    intro O _ _ F hK hQ a
    refine ⟨transport_cp _ ((krausFamily_cp_tr hK).1 a), preservesDiag_transport _ (hQ a),
      fun _ => ?_⟩
    obtain ⟨n, K, out, -, hKF⟩ := hK
    show Gap 1 (transport (levelOneIdx (Fin 2)).symm (F a))
    rw [hKF a, transport_sum]
    refine gap_sum _ _ fun k _ => ?_
    rw [transport_conjChannel]
    exact gap_conjChannel (gapOp_one _))

theorem diagGap_realizes : RealizesSealedOICore diagGapTheory :=
  classTheory_realizes ckData fun g =>
    ⟨by
      rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
      exact conjChannel_cp _,
      preservesDiag_transport _ (preservesDiag_relabel g), fun h => absurd h (by norm_num)⟩

theorem diagGap_inert : InertSpectatorCompositionality diagGapTheory :=
  classTheory_inert ckData (by
    intro R _ _ n m e Φ h
    refine ⟨withSpectator_cp e h.1, preservesDiag_withSpectator R e h.2.1, fun hm => ?_⟩
    have hcard := Fintype.card_congr e
    simp only [Fintype.card_prod, Fintype.card_fin] at hcard
    rcases isEmpty_or_nonempty R with hR | hR
    · rw [Fintype.card_eq_zero, zero_mul] at hcard
      obtain rfl : m = 0 := by omega
      rw [show withSpectator R e Φ = 0 from LinearMap.ext fun X => by
        ext i j
        exact isEmptyElim i]
      exact gap_zero
    · have hR1 : 1 ≤ Fintype.card R := Fintype.card_pos
      have hnm : n ≤ m := by nlinarith
      exact gap_withSpectator e (h.2.2 (le_trans hnm hm)))

theorem diagGap_not_control : ¬ HasCompositeUnitaryControl diagGapTheory :=
  classTheory_not_control ckData rot_isometry fun h => rot_not_preservesDiag h.2.1

theorem diagGap_not_closure : ¬ IteratedAncillaClosure diagGapTheory := by
  refine classTheory_not_closure ckData (n := 3) (m := 1) (Φ := spectatorLast 2 gapChannel)
    ?_ ?_ ?_
  · show ckP (3 * (1 + 1)) (transport (shiftIdx (Fin 2) 3 2) (spectatorLast 2 gapChannel))
    rw [transport_spectatorLast]
    exact ⟨withSpectator_cp _ gapChannel_cp, preservesDiag_withSpectator _ _ gapChannel_preservesDiag,
      fun h => absurd h (by norm_num)⟩
  · intro X
    show (transport (shiftIdx (Fin 2) 3 2) (spectatorLast 2 gapChannel) X).trace = X.trace
    rw [transport_spectatorLast]
    simp only [withSpectator_apply, trace_reindex, trace_amplRef]
    rw [Finset.sum_congr rfl fun i _ => gapChannel_trace (refBlockR (Matrix.reindex _ _ X) i i),
      ← trace_eq_sum_refBlockR, trace_reindex]
  · show ¬ ckP 3 (discardWith (A := Fin 2 × Fin 3) 2 (uniformAttach 2) (spectatorLast 2 gapChannel))
    rw [discardWith_uniform_spectatorLast 2 two_ne_zero]
    exact fun h => gapChannel_not_gap (h.2.2 le_rfl)

/-! #### Cell {inert, control}: the diagonal two-positive theory -/

theorem diagTwoPos_wellFormed : WellFormed diagTwoPosTheory :=
  classTheory_wellFormed icData (by
    intro O _ _ F hK hQ a
    exact ⟨cp_referencePositive (Fin 2) _ (transport_cp _ ((krausFamily_cp_tr hK).1 a)),
      preservesDiag_transport _ (hQ a)⟩)

theorem diagTwoPos_realizes : RealizesSealedOICore diagTwoPosTheory :=
  classTheory_realizes icData fun g =>
    ⟨by
      rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
      exact conjChannel_twoPositive _,
      preservesDiag_transport _ (preservesDiag_relabel g)⟩

theorem diagTwoPos_closure : IteratedAncillaClosure diagTwoPosTheory :=
  classTheory_closure icData fun _ _ _ h =>
    ⟨discardWith_uniform_twoPositive (twoPositive_of_transport _ h.1),
      preservesDiag_discardWith (preservesDiagP_uniform _) (preservesDiag_of_transport _ h.2)⟩

theorem diagTwoPos_not_control : ¬ HasCompositeUnitaryControl diagTwoPosTheory :=
  classTheory_not_control icData rot_isometry fun h => rot_not_preservesDiag h.2

theorem diagTwoPos_not_inert : ¬ InertSpectatorCompositionality diagTwoPosTheory :=
  classTheory_not_inert icData qutritIdx (Φ := reduction2 (Fin 2 × Fin 2))
    ⟨reduction2_twoPositive, reduction2_preservesDiag⟩ reduction2_trace fun h => by
    have hpos := positive_of_twoPositive h.1
      (posSemidef_reindex qutritIdx (Matrix.posSemidef_vecMulVec_self_star maxEnt3))
    rw [withSpectator_reindex] at hpos
    exact amplRef_reduction2_maxEnt3_not_posSemidef (posSemidef_of_reindex qutritIdx hpos)

/-! #### Cell {inert, closure}: the capped two-positive theory -/

theorem capped_wellFormed : WellFormed cappedTheory :=
  classTheory_wellFormed ikData (by
    intro O _ _ F hK _ a
    have hc := transport_cp (levelOneIdx (Fin 2)).symm ((krausFamily_cp_tr hK).1 a)
    exact ⟨cp_referencePositive (Fin 2) _ hc, fun _ => hc⟩)

theorem capped_control : HasCompositeUnitaryControl cappedTheory :=
  classTheory_control ikData fun _ U _ => ⟨conjChannel_twoPositive U, fun _ => conjChannel_cp U⟩

theorem capped_realizes : RealizesSealedOICore cappedTheory :=
  realizesSealedOICore_of_control _ capped_control

theorem capped_not_inert : ¬ InertSpectatorCompositionality cappedTheory :=
  classTheory_not_inert ikData idx18 (Φ := redMap (Fin 2 × Fin 6))
    ⟨redMap_twoPositive (S := Fin 2 × Fin 6), fun h => absurd h (by norm_num)⟩
    (redMap_trace (S := Fin 2 × Fin 6)) fun h => by
    have hpos := positive_of_twoPositive h.1
      (posSemidef_reindex idx18 (Matrix.posSemidef_vecMulVec_self_star (ent3 iota6)))
    rw [withSpectator_reindex] at hpos
    exact amplRef_redMap_ent3_not_posSemidef iota6 iota6_injective (posSemidef_of_reindex idx18 hpos)

theorem capped_not_closure : ¬ IteratedAncillaClosure cappedTheory :=
  classTheory_not_closure ikData (n := 3) (m := 1) (Φ := redMap ((Fin 2 × Fin 3) × Fin 2))
    ⟨twoPositive_transport _ (redMap_twoPositive (S := (Fin 2 × Fin 3) × Fin 2)),
      fun h => absurd h (by norm_num)⟩
    (fun X => by
      simp only [trace_transport]
      rw [redMap_trace, trace_reindex])
    fun h => discard_redMap_not_cp (h.2 le_rfl)

/-! #### Cell {inert, control, closure}: the capped diagonal two-positive theory -/

theorem cappedDiag_wellFormed : WellFormed cappedDiagTheory :=
  classTheory_wellFormed ickData (by
    intro O _ _ F hK hQ a
    have hc := transport_cp (levelOneIdx (Fin 2)).symm ((krausFamily_cp_tr hK).1 a)
    exact ⟨cp_referencePositive (Fin 2) _ hc, preservesDiag_transport _ (hQ a), fun _ => hc⟩)

theorem cappedDiag_realizes : RealizesSealedOICore cappedDiagTheory :=
  classTheory_realizes ickData fun g =>
    ⟨by
      rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
      exact conjChannel_twoPositive _,
      preservesDiag_transport _ (preservesDiag_relabel g), fun h => absurd h (by norm_num)⟩

theorem cappedDiag_not_control : ¬ HasCompositeUnitaryControl cappedDiagTheory :=
  classTheory_not_control ickData rot_isometry fun h => rot_not_preservesDiag h.2.1

theorem cappedDiag_not_inert : ¬ InertSpectatorCompositionality cappedDiagTheory :=
  classTheory_not_inert ickData idx18 (Φ := redMap (Fin 2 × Fin 6))
    ⟨redMap_twoPositive (S := Fin 2 × Fin 6), redMap_preservesDiag (S := Fin 2 × Fin 6),
      fun h => absurd h (by norm_num)⟩ (redMap_trace (S := Fin 2 × Fin 6)) fun h => by
    have hpos := positive_of_twoPositive h.1
      (posSemidef_reindex idx18 (Matrix.posSemidef_vecMulVec_self_star (ent3 iota6)))
    rw [withSpectator_reindex] at hpos
    exact amplRef_redMap_ent3_not_posSemidef iota6 iota6_injective (posSemidef_of_reindex idx18 hpos)

theorem cappedDiag_not_closure : ¬ IteratedAncillaClosure cappedDiagTheory :=
  classTheory_not_closure ickData (n := 3) (m := 1) (Φ := redMap ((Fin 2 × Fin 3) × Fin 2))
    ⟨twoPositive_transport _ (redMap_twoPositive (S := (Fin 2 × Fin 3) × Fin 2)),
      preservesDiag_transport _ (redMap_preservesDiag (S := (Fin 2 × Fin 3) × Fin 2)),
      fun h => absurd h (by norm_num)⟩
    (fun X => by
      simp only [trace_transport]
      rw [redMap_trace, trace_reindex])
    fun h => discard_redMap_not_cp (h.2.2 le_rfl)

end Witnesses

/-! ### Section E — the eight cells and the census -/

section Census

/-- Cell ∅: exact finite operational QM. -/
theorem cell_none : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
    ∧ IteratedAncillaClosure T := by
  obtain ⟨T, hT⟩ := main_result.2.1
  exact ⟨T, ⟨hT.1, hT.2.2.2.2⟩, realizesSealedOICore_of_control T hT.2.2.1, hT.2.1, hT.2.2.1,
    hT.2.2.2.1⟩

/-- Cell {inert}: the round-34 countermodel. -/
theorem cell_I : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ ¬ InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
    ∧ IteratedAncillaClosure T :=
  ⟨countermodel, ⟨countermodel_validity, countermodel_systemToLevelOne⟩,
    countermodel_realizesSealedOICore, countermodel_not_inert, countermodel_control,
    countermodel_iteratedAncillaClosure⟩

/-- Cell {control}: the diagonal theory. -/
theorem cell_C : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ InertSpectatorCompositionality T ∧ ¬ HasCompositeUnitaryControl T
    ∧ IteratedAncillaClosure T :=
  ⟨diagTheory, ⟨diag_validity, diag_systemToLevelOne⟩, diag_realizesSealedOICore, diag_inert,
    diag_not_control, diag_iteratedAncillaClosure⟩

/-- Cell {closure}: the rank-gap theory. -/
theorem cell_K : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
    ∧ ¬ IteratedAncillaClosure T :=
  ⟨gapTheory, ⟨gap_validity, gap_systemToLevelOne⟩, gap_realizesSealedOICore, gap_inert,
    gap_control, gap_not_iteratedAncillaClosure⟩

/-- Cell {inert, control}: the diagonal two-positive theory. -/
theorem cell_IC : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ ¬ InertSpectatorCompositionality T ∧ ¬ HasCompositeUnitaryControl T
    ∧ IteratedAncillaClosure T :=
  ⟨diagTwoPosTheory, diagTwoPos_wellFormed, diagTwoPos_realizes, diagTwoPos_not_inert,
    diagTwoPos_not_control, diagTwoPos_closure⟩

/-- Cell {inert, closure}: the capped two-positive theory. -/
theorem cell_IK : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ ¬ InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
    ∧ ¬ IteratedAncillaClosure T :=
  ⟨cappedTheory, capped_wellFormed, capped_realizes, capped_not_inert, capped_control,
    capped_not_closure⟩

/-- Cell {control, closure}: the diagonal rank-gap theory. -/
theorem cell_CK : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ InertSpectatorCompositionality T ∧ ¬ HasCompositeUnitaryControl T
    ∧ ¬ IteratedAncillaClosure T :=
  ⟨diagGapTheory, diagGap_wellFormed, diagGap_realizes, diagGap_inert, diagGap_not_control,
    diagGap_not_closure⟩

/-- Cell {inert, control, closure}: the capped diagonal two-positive theory. -/
theorem cell_ICK : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
    ∧ ¬ InertSpectatorCompositionality T ∧ ¬ HasCompositeUnitaryControl T
    ∧ ¬ IteratedAncillaClosure T :=
  ⟨cappedDiagTheory, cappedDiag_wellFormed, cappedDiag_realizes, cappedDiag_not_inert,
    cappedDiag_not_control, cappedDiag_not_closure⟩

/-- **THE CENSUS**: every failure pattern of the three substantive principles is realized by a
well-formed theory carrying the sealed OI core. `gI`, `gC`, `gK` say which principles HOLD. -/
theorem substantive_census (gI gC gK : Bool) :
    ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T
      ∧ (InertSpectatorCompositionality T ↔ gI = true)
      ∧ (HasCompositeUnitaryControl T ↔ gC = true)
      ∧ (IteratedAncillaClosure T ↔ gK = true) := by
  cases gI <;> cases gC <;> cases gK
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_ICK
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_IC
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_IK
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_I
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_CK
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_C
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_K
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩
  · obtain ⟨T, hw, hr, hI, hC, hK⟩ := cell_none
    exact ⟨T, hw, hr, by simp [hI], by simp [hC], by simp [hK]⟩

/-- **NO BOOLEAN RELATION** holds among the three substantive principles on the class of
well-formed theories realizing the sealed OI core: whatever holds of the triple
(inert, control, closure) on every such theory holds of every triple of truth values. -/
theorem no_boolean_relation (Rel : Prop → Prop → Prop → Prop)
    (h : ∀ T : FiniteOperationalTheory (Fin 2), WellFormed T → RealizesSealedOICore T →
      Rel (InertSpectatorCompositionality T) (HasCompositeUnitaryControl T)
        (IteratedAncillaClosure T)) :
    ∀ x y z : Bool, Rel (x = true) (y = true) (z = true) := by
  intro x y z
  obtain ⟨T, hw, hr, hI, hC, hK⟩ := substantive_census x y z
  have := h T hw hr
  rwa [hI, hC, hK] at this

/-- **QM IS THE TOP CELL**: on a well-formed theory, no failure is exactly finite operational
QM. -/
theorem qm_is_the_top_cell (T : FiniteOperationalTheory (Fin 2)) (hwf : WellFormed T) :
    ExactAllFiniteEndomorphicQuantumOps T ↔
      InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T :=
  exactAll_iff_substantive T hwf

end Census

#print axioms reduction2_trace_card
#print axioms two_card_sub_one_ne_zero
#print axioms kappa_pos
#print axioms redMap_apply
#print axioms redMap_trace
#print axioms ampl2_smul_map
#print axioms amplRef_smul_map
#print axioms redMap_twoPositive
#print axioms reduction2_preservesDiag
#print axioms redMap_preservesDiag
#print axioms ent3_star
#print axioms ent3_norm
#print axioms refMarginalR_ent3
#print axioms amplRef_reduction2_ent3
#print axioms amplRef_reduction2_ent3_form
#print axioms amplRef_redMap_ent3_not_posSemidef
#print axioms traceShift_apply
#print axioms choiMatrix_traceShift
#print axioms traceShift_choi_form
#print axioms traceShift_not_cp
#print axioms classTheory_availExt_iff
#print axioms classTheory_validity
#print axioms classTheory_systemToLevelOne
#print axioms classTheory_wellFormed
#print axioms classTheory_relabel
#print axioms classTheory_realizes
#print axioms classTheory_inert
#print axioms classTheory_control
#print axioms classTheory_closure
#print axioms classTheory_not_control
#print axioms classTheory_not_closure
#print axioms classTheory_not_inert
#print axioms reindex_reindex
#print axioms transport_trans
#print axioms transport_spectatorLast
#print axioms discardWith_uniform_spectatorLast
#print axioms preservesDiag_conjChannel_of_colMonomial
#print axioms colMonomial_one_kronecker
#print axioms D3_colMonomial
#print axioms E3_colMonomial
#print axioms gapChannel_eq_sum
#print axioms gapChannel_cp
#print axioms gapChannel_preservesDiag
#print axioms iota6_injective
#print axioms discard_redMap
#print axioms discard_redMap_not_cp
#print axioms diagGap_wellFormed
#print axioms diagGap_realizes
#print axioms diagGap_inert
#print axioms diagGap_not_control
#print axioms diagGap_not_closure
#print axioms diagTwoPos_wellFormed
#print axioms diagTwoPos_realizes
#print axioms diagTwoPos_closure
#print axioms diagTwoPos_not_control
#print axioms diagTwoPos_not_inert
#print axioms capped_wellFormed
#print axioms capped_control
#print axioms capped_realizes
#print axioms capped_not_inert
#print axioms capped_not_closure
#print axioms cappedDiag_wellFormed
#print axioms cappedDiag_realizes
#print axioms cappedDiag_not_control
#print axioms cappedDiag_not_inert
#print axioms cappedDiag_not_closure
#print axioms cell_none
#print axioms cell_I
#print axioms cell_C
#print axioms cell_K
#print axioms cell_IC
#print axioms cell_IK
#print axioms cell_CK
#print axioms cell_ICK
#print axioms substantive_census
#print axioms no_boolean_relation
#print axioms qm_is_the_top_cell

end SubstantiveCensus
end OIBridge
