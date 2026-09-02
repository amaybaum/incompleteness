/-
  OIBridge/PhysicalCharacterization.lean — the characterization theorem: exact finite
  operational quantum mechanics IS the five physical completion conditions.

  ROUND FORTY-THREE, PART ONE. Rounds thirty-seven to forty-two produced a SUFFICIENT
  package — valid probabilities, inert spectators, full reversible control, iterated ancilla
  closure, trivial-ancilla consistency — for exact finite endomorphic quantum operations on
  the visible system and every positive composite, against finite isometry extension at the
  composite carriers. This file proves the package NECESSARY, with no external boundary at
  all, and freezes the equivalence.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `PhysicalCompletionConditions T` := validity ∧ inert spectators ∧ control    │
      │    ∧ iterated ancilla closure ∧ system-to-level-one.                          │
      │  `physical_of_exactAll` (kernel-internal, any nonempty system):               │
      │    ExactAllFiniteEndomorphicQuantumOps T ⟹ PhysicalCompletionConditions T.    │
      │    Each clause for its own simple reason: exact families are Kraus, hence      │
      │    positive and trace-preserving (validity); the untouched-spectator extension  │
      │    of a Kraus family is Kraus, hence available (inert spectators); a unitary    │
      │    is a one-operator normalized instrument (control); attach-run-discard of a   │
      │    Kraus family is Kraus (closure); Kraus form transports to level one          │
      │    (system-to-level-one).                                                      │
      │  `exactAll_iff_physical` (qubit system):                                       │
      │    [∀ k, FiniteIsometryExtensionSF (Fin 2 × Fin (k+1))] ⟹                       │
      │      (ExactAllFiniteEndomorphicQuantumOps T ⟺ PhysicalCompletionConditions T). │
      │    Boundary item 2 enters ONLY the constructive direction.                      │
      │  MINIMALITY (part one): validity is independent of the other four and of OI   │
      │    realization (`everywhereAvailable`); inert spectators likewise               │
      │    (`countermodel`, now with `countermodel_systemToLevelOne`); trivial-ancilla  │
      │    consistency likewise (`systemLoose`, round forty-two). The control cell is    │
      │    part two (`DiagonalTheory.lean`). The closure cell against ALL four others   │
      │    is recorded OPEN: the round-38 admissible theory fails system-to-level-one  │
      │    (`admissible_not_systemToLevelOne`, proved), so it does not close that cell; │
      │    bare finite OI ⇏ closure (round forty) is unaffected.                         │
      └──────────────────────────────────────────────────────────────────────────────┘

  HOW EXACTNESS AT `Fin m` REACHES GENERAL OUTCOME TYPES. Both exactness predicates are
  stated on `Fin m` families. `krausFamily_of_exact_fin` and `avail_of_krausFamily_fin` move
  between an arbitrary finite outcome type and `Fin (card O)` by coarse-graining along
  `Fintype.equivFin O` in each direction — the structure's own coarse-graining rule, with
  singleton fibres. Level zero is handled once by `availExt_zero`: the carrier is empty,
  every map is zero, and coarse-graining the level-zero readout gives every family.

  THE THREE KINDS OF ASSUMPTION, made explicit. (1) Semantic validity — that the things
  called available actually produce nonnegative probabilities summing to one; additional to
  the formalized OI/operational structure (`everywhereAvailable` is a counter-witness), but
  best read as part of what "physically available" means. (2) Trivial-ancilla coherence —
  a bookkeeping law of the formalism (`systemLoose`). (3) Genuine composition and richness
  principles — inert spectators, iterated closure, full control — each provably additional
  (this file and part two).

  WHAT IS AND IS NOT CLAIMED. Proved: everything above. NOT claimed: that the five
  conditions are mutually independent in every cell (one cell is open and named); that any
  condition follows from OI; OI ⟺ QM. No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.LevelOneSeam

namespace OIBridge
namespace PhysicalCharacterization

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam HiddenCoherence

open scoped ComplexOrder

/-! ### Section A — general outcome types from `Fin m` exactness -/

section Coarse

variable {S : Type} [Fintype S] [DecidableEq S]

/-- A `Fin m`-exact availability predicate closed under coarse-graining makes every
available family on any finite outcome type a Kraus family. -/
theorem krausFamily_of_exact_fin
    (P : ∀ (O : Type) [Fintype O] [DecidableEq O], (O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop)
    (hco : ∀ (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O'] [DecidableEq O']
      (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (f : O → O'), P O F →
      P O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j))
    (hex : ∀ (m : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ),
      P (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F)
    {O : Type} [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (hF : P O F) : IsKrausFamily F := by
  let f : O ≃ Fin (Fintype.card O) := Fintype.equivFin O
  have hG := hco O (Fin (Fintype.card O)) F f hF
  have hfun : (fun j => ∑ i ∈ Finset.univ.filter (fun i => f i = j), F i) = fun j => F (f.symm j) := by
    funext j
    have hfil : Finset.univ.filter (fun i => f i = j) = {f.symm j} := by
      ext i
      simp [Equiv.apply_eq_iff_eq_symm_apply]
    rw [hfil, Finset.sum_singleton]
  rw [hfun] at hG
  obtain ⟨r, K, out, hnorm, hKF⟩ := (hex _ _).mp hG
  refine ⟨r, K, fun k => f.symm (out k), hnorm, fun a => ?_⟩
  have h1 : F a = instrumentBranch K out (f a) := by
    rw [← hKF]
    simp
  rw [h1]
  unfold instrumentBranch
  refine Finset.sum_congr ?_ fun _ _ => rfl
  ext k
  simp [Equiv.symm_apply_eq]

/-- Conversely, every Kraus family on any finite outcome type is available. -/
theorem avail_of_krausFamily_fin
    (P : ∀ (O : Type) [Fintype O] [DecidableEq O], (O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop)
    (hco : ∀ (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O'] [DecidableEq O']
      (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (f : O → O'), P O F →
      P O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j))
    (hex : ∀ (m : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ),
      P (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F)
    {O : Type} [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (hK : IsKrausFamily F) : P O F := by
  let f : O ≃ Fin (Fintype.card O) := Fintype.equivFin O
  obtain ⟨r, K, out, hnorm, hKF⟩ := hK
  have hG : P (Fin (Fintype.card O)) (instrumentBranch K (fun k => f (out k))) :=
    (hex _ _).mpr ⟨r, K, _, hnorm, rfl⟩
  have h := hco _ O _ f.symm hG
  have hfun : (fun a => ∑ j ∈ Finset.univ.filter (fun j => f.symm j = a),
      instrumentBranch K (fun k => f (out k)) j) = F := by
    funext a
    have hfil : Finset.univ.filter (fun j => f.symm j = a) = {f a} := by
      ext j
      simp [Equiv.symm_apply_eq]
    rw [hfil, Finset.sum_singleton, hKF a]
    unfold instrumentBranch
    refine Finset.sum_congr ?_ fun _ _ => rfl
    ext k
    simp [f.injective.eq_iff]
  rw [hfun] at h
  exact h

/-- A Kraus family is branchwise CP and aggregate trace preserving. -/
theorem krausFamily_cp_tr {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (hK : IsKrausFamily F) :
    (∀ a, IsCompletelyPositive (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace := by
  refine ⟨fun a => krausFamily_cp hK a, fun X => ?_⟩
  obtain ⟨m, K, out, hnorm, hKF⟩ := hK
  rw [Finset.sum_congr rfl fun a _ => by rw [hKF a, LinearMap.sum_apply, Matrix.trace_sum],
    Finset.sum_fiberwise_of_maps_to (fun k _ => Finset.mem_univ (out k))
      (fun k => ((conjChannel (K k)) X).trace)]
  rw [Finset.sum_congr rfl fun k _ => by
    rw [conjChannel_apply, Matrix.trace_mul_cycle (K k) X (K k)ᴴ]]
  rw [← Matrix.trace_sum, ← Finset.sum_mul, hnorm, Matrix.one_mul]

end Coarse

/-! ### Section B — level zero and the exactness instances -/

section Exact

variable {A : Type} [Fintype A] [DecidableEq A]

/-- Every family is available at level zero: the carrier is empty and every map is the
zero map, which coarse-graining the level-zero readout supplies. -/
theorem availExt_zero (T : FiniteOperationalTheory A) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin 0) (A × Fin 0) ℂ →ₗ[ℂ] Matrix (A × Fin 0) (A × Fin 0) ℂ) :
    T.availExt 0 O F := by
  have h := T.availExt_coarse 0 (Fin 0) O (T.readout 0) (fun k => k.elim0) (T.readout_avail 0)
  have hfun : (fun a : O => ∑ j ∈ Finset.univ.filter (fun j : Fin 0 => (j.elim0 : O) = a),
      T.readout 0 j) = F := by
    funext a
    refine LinearMap.ext fun X => ?_
    ext p q
    exact p.2.elim0
  rw [hfun] at h
  exact h

/-- Exact composite operations: every available family at a positive level, on any finite
outcome type, is a Kraus family. -/
theorem krausFamily_of_exactComposite (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) (N : ℕ) (hN : 0 < N) {O : Type} [Fintype O]
    [DecidableEq O] (F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ)
    (hF : T.availExt N O F) : IsKrausFamily F := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hN.ne'
  exact krausFamily_of_exact_fin (fun O _ _ G => T.availExt (k + 1) O G)
    (fun O O' _ _ _ _ G f hG => T.availExt_coarse (k + 1) O O' G f hG) (hc k) F hF

/-- Exact composite operations: every Kraus family at a positive level is available. -/
theorem availExt_of_krausFamily (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) (N : ℕ) (hN : 0 < N) {O : Type} [Fintype O]
    [DecidableEq O] (F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ)
    (hK : IsKrausFamily F) : T.availExt N O F := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hN.ne'
  exact avail_of_krausFamily_fin (fun O _ _ G => T.availExt (k + 1) O G)
    (fun O O' _ _ _ _ G f hG => T.availExt_coarse (k + 1) O O' G f hG) (hc k) F hK

/-- Exact system operations on any finite outcome type. -/
theorem krausFamily_of_exactSystem (T : FiniteOperationalTheory A)
    (hs : ExactFiniteEndomorphicQuantumOps T) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) (hF : T.avail O F) : IsKrausFamily F :=
  krausFamily_of_exact_fin (fun O _ _ G => T.avail O G)
    (fun O O' _ _ _ _ G f hG => T.avail_coarse O O' G f hG) hs F hF

/-- An available family at a positive level of an exact theory is available iff it is
CP and aggregate trace preserving. -/
theorem availExt_pos_iff [Nonempty A] (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) (N : ℕ) (hN : 0 < N) {O : Type} [Fintype O]
    [DecidableEq O] (F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ) :
    T.availExt N O F
      ↔ (∀ a, IsCompletelyPositive (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hN.ne'
  constructor
  · intro hF
    exact krausFamily_cp_tr (krausFamily_of_exactComposite T hc (k + 1) k.succ_pos F hF)
  · rintro ⟨hcp, htr⟩
    exact availExt_of_krausFamily T hc (k + 1) k.succ_pos F
      (isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F hcp htr)

end Exact

/-! ### Section C — necessity of each condition -/

section Necessity

variable {A : Type} [Fintype A] [DecidableEq A] [Nonempty A]

theorem krausSoundExt_of_exactComposite (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) : KrausSoundExt T :=
  fun n O _ _ F hF => krausFamily_of_exactComposite T hc (n + 1) n.succ_pos F hF

/-- **VALIDITY IS NECESSARY.** -/
theorem validity_of_exactComposite (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) : CompositeOperationalValidity T :=
  validity_of_krausSoundExt T (krausSoundExt_of_exactComposite T hc)

/-- **CONTROL IS NECESSARY**: a unitary is a one-operator normalized instrument. -/
theorem control_of_exactComposite (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) : HasCompositeUnitaryControl T := by
  intro n U hU
  rcases n with _ | k
  · exact availExt_zero T _
  refine availExt_of_krausFamily T hc (k + 1) k.succ_pos _ ⟨0, ![U], fun _ => (), ?_, fun _ => ?_⟩
  · simp [hU]
  · rw [Finset.filter_true_of_mem (fun _ _ => rfl), Fin.sum_univ_one]
    rfl

/-- **INERT SPECTATORS ARE NECESSARY**: the untouched-spectator extension of a Kraus family
is Kraus, hence available. -/
theorem inert_of_exactComposite (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) : InertSpectatorCompositionality T := by
  refine (inertSpectator_iff_parallelReferenceExtension T).mpr ?_
  intro R _ _ n m e O _ _ F hF
  rcases m with _ | m'
  · exact availExt_zero T _
  rcases n with _ | k
  · exfalso
    have hc' := Fintype.card_congr e
    simp only [Fintype.card_prod, Fintype.card_fin, mul_zero] at hc'
    exact absurd hc'.symm (Nat.mul_pos Fintype.card_pos m'.succ_pos).ne'
  obtain ⟨hcp, htr⟩ := krausFamily_cp_tr (krausFamily_of_exactComposite T hc (k + 1) k.succ_pos F hF)
  refine (availExt_pos_iff T hc (m' + 1) m'.succ_pos _).mpr
    ⟨fun a => withSpectator_cp e (hcp a), fun X => ?_⟩
  simp only [withSpectator_apply, trace_reindex, trace_amplRef]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun i _ => htr (refBlockR (Matrix.reindex e.symm e.symm X) i i),
    ← trace_eq_sum_refBlockR, trace_reindex e.symm]

/-- **ITERATED ANCILLA CLOSURE IS NECESSARY**: attach-run-discard of a Kraus family is Kraus,
hence available. -/
theorem closure_of_exactComposite (T : FiniteOperationalTheory A)
    (hc : ExactCompositeQuantumOps T) : IteratedAncillaClosure T := by
  intro n m O _ _ F hF
  rcases n with _ | k
  · exact availExt_zero T _
  obtain ⟨hcp, htr⟩ := krausFamily_cp_tr
    (krausFamily_of_exactComposite T hc ((k + 1) * (m + 1)) (Nat.mul_pos k.succ_pos m.succ_pos) _ hF)
  refine (availExt_pos_iff T hc (k + 1) k.succ_pos _).mpr
    ⟨fun a => discardWith_uniform_cp (cp_of_transport_cp _ (hcp a)), fun X => ?_⟩
  rw [Finset.sum_congr rfl fun a _ => discardWith_trace (m + 1) _ (F a) X]
  have h := htr (Matrix.reindex (shiftIdx A (k + 1) (m + 1)) (shiftIdx A (k + 1) (m + 1))
    (uniformAttach (m + 1) X))
  simp only [transport_reindex, trace_reindex] at h
  rw [h, uniformAttach_trace (m + 1) m.succ_ne_zero]

/-- **SYSTEM-TO-LEVEL-ONE IS NECESSARY**: the Kraus form transports to level one. -/
theorem levelOne_of_exactAll (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : SystemToLevelOne T := by
  intro O _ _ F hF
  obtain ⟨hcp, htr⟩ := krausFamily_cp_tr (krausFamily_of_exactSystem T h.1 F hF)
  refine (availExt_pos_iff T h.2 1 Nat.one_pos _).mpr
    ⟨fun a => transport_cp _ (hcp a), fun X => ?_⟩
  simp only [trace_transport]
  rw [htr, trace_reindex]

/-- **THE FIVE PHYSICAL COMPLETION CONDITIONS**, bundled. -/
def PhysicalCompletionConditions (T : FiniteOperationalTheory A) : Prop :=
  CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
    ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T

/-- **NECESSITY**, kernel-internal: exact finite endomorphic QM on the system and every
composite forces all five conditions. -/
theorem physical_of_exactAll (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : PhysicalCompletionConditions T :=
  ⟨validity_of_exactComposite T h.2, inert_of_exactComposite T h.2,
    control_of_exactComposite T h.2, closure_of_exactComposite T h.2, levelOne_of_exactAll T h⟩

end Necessity

/-! ### Section D — the characterization -/

/-- **SUFFICIENCY**, restated on the bundle (qubit system, boundary item 2 at the composite
carriers). -/
theorem exactAll_of_physical (T : FiniteOperationalTheory (Fin 2))
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
    (h : PhysicalCompletionConditions T) : ExactAllFiniteEndomorphicQuantumOps T :=
  exactAll_of_conditions T hext h.1 h.2.1 h.2.2.1 h.2.2.2.1 h.2.2.2.2

/-- **THE CHARACTERIZATION THEOREM.** For a qubit system, against finite isometry extension
at the composite carriers (used only constructively): exact finite endomorphic quantum
mechanics on the system and every positive composite holds EXACTLY when the five physical
completion conditions hold. -/
theorem exactAll_iff_physical (T : FiniteOperationalTheory (Fin 2))
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T :=
  ⟨physical_of_exactAll T, exactAll_of_physical T hext⟩

/-! ### Section E — minimality, part one -/

/-- **VALIDITY IS INDEPENDENT** of the other four conditions and of OI realization: the
everywhere-available theory has all of them trivially and admits the trace amplifier at
level one. -/
theorem everywhereAvailable_not_validity :
    ¬ CompositeOperationalValidity (everywhereAvailable (Fin 2)) := by
  intro h
  have h1 := (h 1 Unit (fun _ => (2 : ℂ) • LinearMap.id) trivial).2 1
  rw [Fintype.sum_unique] at h1
  simp only [LinearMap.smul_apply, LinearMap.id_apply, Matrix.trace_smul, Matrix.trace_one,
    Fintype.card_prod, Fintype.card_fin, smul_eq_mul] at h1
  norm_num at h1

theorem everywhereAvailable_control : HasCompositeUnitaryControl (everywhereAvailable (Fin 2)) :=
  fun _ _ _ => trivial

theorem validity_independent :
    ∃ T : FiniteOperationalTheory (Fin 2),
      InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ CompositeOperationalValidity T :=
  ⟨everywhereAvailable (Fin 2),
    (inertSpectator_iff_parallelReferenceExtension _).mpr fun _ _ _ _ _ _ _ _ _ _ _ => trivial,
    everywhereAvailable_control, fun _ _ _ _ _ _ _ => trivial, fun _ _ _ _ _ => trivial,
    realizesSealedOICore_of_control _ everywhereAvailable_control,
    everywhereAvailable_not_validity⟩

/-- The round-34 countermodel has system-to-level-one consistency: a system Kraus family
transported to level one is CP, hence 2-positive, with the aggregate trace preserved. -/
theorem countermodel_systemToLevelOne : SystemToLevelOne countermodel := by
  intro O _ _ F hF
  obtain ⟨hcp, htr⟩ := krausFamily_cp_tr hF
  refine ⟨fun a => cp_referencePositive (Fin 2) _ (transport_cp _ (hcp a)), fun X => ?_⟩
  simp only [trace_transport]
  rw [htr, trace_reindex]

/-- **INERT SPECTATORS ARE INDEPENDENT** of the other four conditions and of OI realization. -/
theorem inert_independent :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ InertSpectatorCompositionality T :=
  ⟨countermodel, countermodel_validity, countermodel_control,
    countermodel_iteratedAncillaClosure, countermodel_systemToLevelOne,
    countermodel_realizesSealedOICore, countermodel_not_inert⟩

/-- **TRIVIAL-ANCILLA CONSISTENCY IS INDEPENDENT** of the other four and of OI realization
(round forty-two's loose theory). -/
theorem levelOne_independent' :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ RealizesSealedOICore T
        ∧ ¬ SystemToLevelOne T :=
  ⟨systemLoose, systemLoose_validity, systemLoose_inert, systemLoose_control,
    systemLoose_iteratedAncillaClosure, systemLoose_realizesSealedOICore,
    systemLoose_not_systemToLevelOne⟩

/-! ### Section F — the closure cell: the admissible theory fails system-to-level-one -/

section AdmissibleLevelOne

/-- Amplitude damping on the qubit itself, as a system family. -/
noncomputable def qubitDamping : Fin 1 → Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ :=
  fun _ => conjChannel D₀ + conjChannel E₀

theorem qubitDamping_isKraus : IsKrausFamily qubitDamping := by
  refine ⟨1, ![D₀, E₀], fun _ => 0, ?_, fun a => ?_⟩
  · rw [Fin.sum_univ_two]
    exact qubit_gram
  · show conjChannel D₀ + conjChannel E₀
      = ∑ k ∈ Finset.univ.filter (fun _ : Fin 2 => (0 : Fin 1) = a), conjChannel (![D₀, E₀] k)
    rw [Finset.filter_true_of_mem (fun _ _ => Subsingleton.elim _ _), Fin.sum_univ_two]
    rfl

theorem transport_add {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l] [DecidableEq l']
    (e : l ≃ l') (Φ Ψ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    transport e (Φ + Ψ) = transport e Φ + transport e Ψ := by
  refine LinearMap.ext fun N => ?_
  ext p q
  simp only [transport_apply, LinearMap.add_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    Matrix.add_apply]

/-- The level-one carrier's coordinates: `(a, 0)`. -/
theorem levelOne_eq (p : Fin 2 × Fin 1) : p = (p.1, 0) :=
  Prod.ext rfl (Subsingleton.elim _ _)

/-- The damping operators lifted to the level-one carrier. -/
noncomputable def L₀ : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  Matrix.reindex (levelOneIdx (Fin 2)).symm (levelOneIdx (Fin 2)).symm D₀
noncomputable def L₁ : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  Matrix.reindex (levelOneIdx (Fin 2)).symm (levelOneIdx (Fin 2)).symm E₀

theorem L₀_apply (p q : Fin 2 × Fin 1) :
    L₀ p q = if p.1 = q.1 then (if p.1 = 0 then 1 else (rD : ℂ)) else 0 := rfl

theorem L₁_apply (p q : Fin 2 × Fin 1) :
    L₁ p q = if p.1 = 0 ∧ q.1 = 1 then (sD : ℂ) else 0 := rfl

theorem transport_qubitDamping :
    transport (levelOneIdx (Fin 2)).symm (qubitDamping 0) = conjChannel L₀ + conjChannel L₁ := by
  show transport (levelOneIdx (Fin 2)).symm (conjChannel D₀ + conjChannel E₀) = _
  rw [transport_add, transport_conjChannel, transport_conjChannel]
  rfl

theorem levelOne_gram : L₀ᴴ * L₀ + L₁ᴴ * L₁ = 1 := by
  ext ⟨x, i⟩ ⟨y, j⟩
  fin_cases x <;> fin_cases y <;> fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      L₀_apply, L₁_apply, Matrix.one_apply, Complex.conj_ofReal] <;>
    norm_num [rD, sD]

theorem levelOneDamping_trace (X : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) :
    ((conjChannel L₀ + conjChannel L₁) X).trace = X.trace := by
  show (L₀ * X * L₀ᴴ + L₁ * X * L₁ᴴ).trace = X.trace
  rw [Matrix.trace_add, Matrix.trace_mul_cycle L₀ X L₀ᴴ, Matrix.trace_mul_cycle L₁ X L₁ᴴ,
    ← Matrix.trace_add, ← Matrix.add_mul, levelOne_gram, Matrix.one_mul]

theorem vecOf_L₀_ne : vecOf L₀ ≠ 0 := by
  intro h
  have := congrFun h ((0, 0), (0, 0))
  simp [vecOf, L₀_apply] at this

theorem vecOf_L₁_ne : vecOf L₁ ≠ 0 := by
  intro h
  have := congrFun h ((1, 0), (0, 0))
  simp [vecOf, L₁_apply, sD] at this

theorem vecOf_L_orth : star (vecOf L₀) ⬝ᵥ vecOf L₁ = 0 := by
  simp [dotProduct, vecOf, L₀_apply, L₁_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
    Fin.sum_univ_one]

theorem kraus_of_levelOneDamping {ι : Type} [Fintype ι]
    (K : ι → Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ)
    (hK : conjChannel L₀ + conjChannel L₁ = ∑ i, conjChannel (K i)) (i : ι) :
    ∃ a b : ℂ, K i = a • L₀ + b • L₁ := by
  have hchoi : ∑ j, Matrix.vecMulVec (vecOf (K j)) (star (vecOf (K j)))
      = Matrix.vecMulVec (vecOf L₀) (star (vecOf L₀))
        + Matrix.vecMulVec (vecOf L₁) (star (vecOf L₁)) := by
    have h := congrArg choiMatrix hK
    rw [choiMatrix_add, choiMatrix_conjChannel, choiMatrix_conjChannel, choiMatrix_finsum] at h
    simp only [choiMatrix_conjChannel] at h
    exact h.symm
  obtain ⟨a, b, hab⟩ := dyad_sum_span (fun j => vecOf (K j)) (vecOf L₀) (vecOf L₁)
    vecOf_L₀_ne vecOf_L₁_ne vecOf_L_orth hchoi i
  refine ⟨a, b, ?_⟩
  ext p q
  have := congrFun hab (q, p)
  simpa [vecOf] using this

theorem levelOne_gram_entries (a b : ℂ) :
    ((a • L₀ + b • L₁)ᴴ * (a • L₀ + b • L₁)) (0, 0) (1, 0) = star a * b * (sD : ℂ)
    ∧ ((a • L₀ + b • L₁)ᴴ * (a • L₀ + b • L₁)) (0, 0) (0, 0) = star a * a
    ∧ ((a • L₀ + b • L₁)ᴴ * (a • L₀ + b • L₁)) (1, 0) (1, 0)
        = star a * a * ((rD : ℂ) * rD) + star b * b * ((sD : ℂ) * sD) := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Fin.sum_univ_one, L₀_apply, L₁_apply, Complex.conj_ofReal] <;> ring

/-- The explicit inverse of `a L₀ + b L₁` for `a ≠ 0`, on the level-one carrier. -/
noncomputable def levelOneInv (a b : ℂ) : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  Matrix.of fun p q =>
    if p.1 = 0 ∧ q.1 = 0 then a⁻¹ else if p.1 = 0 ∧ q.1 = 1 then -(b * (sD : ℂ)) / (a * a * rD)
      else if p.1 = 1 ∧ q.1 = 1 then (a * rD)⁻¹ else 0

theorem levelOneInv_mul (a b : ℂ) (ha : a ≠ 0) : levelOneInv a b * (a • L₀ + b • L₁) = 1 := by
  have hr : (rD : ℂ) ≠ 0 := by
    rw [Ne, Complex.ofReal_eq_zero]
    norm_num [rD]
  ext ⟨x, i⟩ ⟨y, j⟩
  fin_cases x <;> fin_cases y <;> fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_one,
      levelOneInv, L₀_apply, L₁_apply, Matrix.one_apply] <;>
    field_simp <;> ring

/-- **AMPLITUDE DAMPING ON THE QUBIT, LIFTED TO LEVEL ONE, IS INADMISSIBLE AT LEVEL ONE**: the
admissible bound there is rank one, and every decomposition contains an invertible
operator that is not a unitary multiple. -/
theorem levelOneDamping_not_adm : ¬ Adm 1 (conjChannel L₀ + conjChannel L₁) := by
  rintro ⟨ι, _, K, hK, hadm⟩
  choose a b hab using kraus_of_levelOneDamping K hK
  have hnorm : ∑ i, (K i)ᴴ * K i = 1 := by
    refine sum_conjTranspose_mul_eq_one_of_trace K fun X => ?_
    have h := congrArg (fun Φ => (Φ X).trace) hK
    simp only [LinearMap.sum_apply, Matrix.trace_sum] at h
    rw [levelOneDamping_trace] at h
    exact h.symm
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
        Fin.sum_univ_two, Fin.sum_univ_one, L₁_apply]
    simp only [Finset.sum_congr rfl fun i _ => hz i, Finset.sum_const_zero, zero_ne_one] at h00
  obtain ⟨i, hai⟩ := hex
  have hs : (sD : ℂ) ≠ 0 := by
    rw [Ne, Complex.ofReal_eq_zero]
    norm_num [sD]
  obtain ⟨h01, h00, h11⟩ := levelOne_gram_entries (a i) (b i)
  rcases hadm i with ⟨c, U, hU, hcU⟩ | ⟨ι', _, P, Q, hι', hPQ⟩
  · have hgram : (K i)ᴴ * K i = (star c * c) • (1 : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) := by
      rw [hcU, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, hU, smul_smul]
    rw [hab i] at hgram
    have e01 := congrFun (congrFun hgram (0, 0)) (1, 0)
    have e00 := congrFun (congrFun hgram (0, 0)) (0, 0)
    have e11 := congrFun (congrFun hgram (1, 0)) (1, 0)
    rw [h01] at e01
    rw [h00] at e00
    rw [h11] at e11
    simp only [Matrix.smul_apply, Matrix.one_apply, smul_eq_mul, Prod.mk.injEq,
      Fin.zero_eq_one_iff, Fin.one_eq_zero_iff, OfNat.ofNat_ne_one, one_ne_zero, and_false,
      false_and, and_true, true_and, and_self, if_false, if_true, mul_zero, mul_one] at e01 e00 e11
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
  · have hone : (1 : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) = levelOneInv (a i) (b i) * P * Q := by
      rw [Matrix.mul_assoc, ← hPQ, hab i, levelOneInv_mul _ _ hai]
    have hrank : (levelOneInv (a i) (b i) * P * Q).rank ≤ 1 :=
      ((Matrix.rank_mul_le_left _ _).trans (Matrix.rank_le_card_width _)).trans hι'
    rw [← hone, Matrix.rank_one] at hrank
    simp at hrank

/-- **THE ADMISSIBLE THEORY FAILS SYSTEM-TO-LEVEL-ONE**: its system sector is fully quantum,
its level-one sector admits only rank-one or unitary-multiple operators, and qubit amplitude
damping separates them. So the round-38 witness does not close the closure cell against all
four other conditions; that cell is recorded open. -/
theorem admissible_not_systemToLevelOne : ¬ SystemToLevelOne admissibleTheory := by
  intro h
  have h1 : Adm 1 (transport (levelOneIdx (Fin 2)).symm (qubitDamping 0)) :=
    (h (Fin 1) qubitDamping qubitDamping_isKraus).1 0
  rw [transport_qubitDamping] at h1
  exact levelOneDamping_not_adm h1

end AdmissibleLevelOne

#print axioms krausFamily_of_exact_fin
#print axioms avail_of_krausFamily_fin
#print axioms krausFamily_cp_tr
#print axioms availExt_zero
#print axioms krausFamily_of_exactComposite
#print axioms availExt_of_krausFamily
#print axioms krausFamily_of_exactSystem
#print axioms availExt_pos_iff
#print axioms krausSoundExt_of_exactComposite
#print axioms validity_of_exactComposite
#print axioms control_of_exactComposite
#print axioms inert_of_exactComposite
#print axioms closure_of_exactComposite
#print axioms levelOne_of_exactAll
#print axioms physical_of_exactAll
#print axioms exactAll_of_physical
#print axioms exactAll_iff_physical
#print axioms everywhereAvailable_not_validity
#print axioms everywhereAvailable_control
#print axioms validity_independent
#print axioms countermodel_systemToLevelOne
#print axioms inert_independent
#print axioms levelOne_independent'
#print axioms qubitDamping_isKraus
#print axioms transport_add
#print axioms levelOne_eq
#print axioms L₀_apply
#print axioms L₁_apply
#print axioms transport_qubitDamping
#print axioms levelOne_gram
#print axioms levelOneDamping_trace
#print axioms vecOf_L₀_ne
#print axioms vecOf_L₁_ne
#print axioms vecOf_L_orth
#print axioms kraus_of_levelOneDamping
#print axioms levelOne_gram_entries
#print axioms levelOneInv_mul
#print axioms levelOneDamping_not_adm
#print axioms admissible_not_systemToLevelOne

end PhysicalCharacterization
end OIBridge
