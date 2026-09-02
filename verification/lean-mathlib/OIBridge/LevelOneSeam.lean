/-
  OIBridge/LevelOneSeam.lean — the visible system and level one: which direction is
  structural, which is a principle, and the endpoint that covers the system itself.

  ROUND FORTY-TWO. `FiniteOperationalTheory` carries two availability notions with no rule
  relating them: `avail` on the visible system `A`, and `availExt 1` on `A × Fin 1`, the
  system with a ONE-STATE ancilla adjoined. Every endpoint so far started at level one, so
  it was silent about the system's own operations. This file audits the seam.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  STRUCTURAL (no assumption). `avail_of_availExt_one`: a level-one family is    │
      │    available on the system after transport along `A × Fin 1 ≃ A` — because   │
      │    uniform attachment of the one-state ancilla IS the canonical embedding and  │
      │    the discard IS its inverse (`discardWith_uniform_one_eq_transport`), so the  │
      │    structure's own attach-then-discard rule reduces to transport.              │
      │  THE PRINCIPLE. `SystemToLevelOne T`: an operation available on the system     │
      │    remains available after adjoining the one-state ancilla. Only this          │
      │    direction is missing; `avail_iff_availExt_one` shows the equivalence costs  │
      │    exactly it.                                                                 │
      │  TRANSPORT OF KRAUS FORM. `isKraus_transport`: the normalized Kraus form is     │
      │    invariant under any finite reindexing of the carrier (each operator is       │
      │    reindexed; `Σ Kᴴ K = 1` survives).                                            │
      │  INHERITANCE. `exactSystem_of_levelOne`: with the principle, exact composite    │
      │    operations (which begin at level one) give exact SYSTEM operations.         │
      │  THE ENDPOINT. `ExactAllFiniteEndomorphicQuantumOps` = system ∧ every positive  │
      │    composite; `exactAll_of_conditions`: validity ∧ inert spectators ∧ control   │
      │    ∧ iterated ancilla closure ∧ system-to-level-one ⟹ exact finite endomorphic  │
      │    QM on the system and every composite, against boundary item 2 at the         │
      │    composite carriers only. No quantum-formal soundness premise anywhere.       │
      │    [ITEM 2 DISCHARGED IN ROUND FORTY-FIVE: `IsometryExtension.lean`.]        │
      │  THE COUNTERMODEL. `systemLoose`: `fullQuantum`'s composite sector, preparations │
      │    and readouts with an UNRESTRICTED system predicate. It has every round-41    │
      │    condition, exact composite operations, and realizes the sealed OI core; its  │
      │    system sector contains the trace amplifier `X ↦ 2X`, so it is not exactly    │
      │    quantum on the system and cannot satisfy the principle                        │
      │    (`levelOne_independent`, `levelOne_not_deletable`).                         │
      └──────────────────────────────────────────────────────────────────────────────┘

  THE THREE COMPOSITION PRINCIPLES, side by side. Inert spectators: adding a genuine
  independent system does not alter an intervention. Iterated ancilla closure: a composite
  may itself become the working system of a larger experiment. System-to-level-one
  consistency: adjoining nothing but a one-state factor cannot change which operations
  exist. The last is a bookkeeping law rather than physics, which is exactly why it is
  isolated here instead of hidden in the structure.

  WHAT IS AND IS NOT CLAIMED. Proved: everything in the box. NOT claimed: that any of the
  five conditions follows from OI (round forty bounds two of them; the others are the
  subject of the round-43 minimality audit); OI ⟺ QM; anything beyond the finite
  endomorphic instrument scope. No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.OperationalValidity

namespace OIBridge
namespace LevelOneSeam

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity HiddenCoherence

open scoped ComplexOrder

/-! ### Section A — the level-one equivalence and the structural direction -/

section Seam

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- `A × Fin 1 ≃ A`: the one-state ancilla carries nothing. -/
def levelOneIdx (A : Type*) : A × Fin 1 ≃ A where
  toFun p := p.1
  invFun a := (a, 0)
  left_inv p := by
    obtain ⟨a, i⟩ := p
    exact Prod.ext rfl (Subsingleton.elim _ _)
  right_inv _ := rfl

/-- Uniform attachment of the one-state ancilla is the canonical embedding. -/
theorem uniformAttach_one_eq (ρ : Matrix A A ℂ) :
    uniformAttach (A := A) 1 ρ = Matrix.reindex (levelOneIdx A).symm (levelOneIdx A).symm ρ := by
  ext ⟨a, i⟩ ⟨b, j⟩
  rw [uniformAttach_apply, tensorOf_apply, Matrix.reindex_apply, Matrix.submatrix_apply]
  simp only [Nat.cast_one, inv_one, one_smul, Matrix.one_apply, Subsingleton.elim i j, if_true,
    mul_one]
  rfl

/-- Discarding the one-state ancilla is the canonical inverse. -/
theorem ptraceAnc_one_eq (M : Matrix (A × Fin 1) (A × Fin 1) ℂ) :
    ptraceAnc 1 M = Matrix.reindex (levelOneIdx A) (levelOneIdx A) M := by
  ext s t
  rw [ptraceAnc_apply, Fintype.sum_unique, Matrix.reindex_apply, Matrix.submatrix_apply]
  rfl

/-- **ATTACH-RUN-DISCARD AT LEVEL ONE IS TRANSPORT.** -/
theorem discardWith_uniform_one_eq_transport
    (Φ : Matrix (A × Fin 1) (A × Fin 1) ℂ →ₗ[ℂ] Matrix (A × Fin 1) (A × Fin 1) ℂ) :
    discardWith (A := A) 1 (uniformAttach 1) Φ = transport (levelOneIdx A) Φ := by
  refine LinearMap.ext fun ρ => ?_
  show ptraceAnc 1 (Φ (uniformAttach 1 ρ)) = _
  rw [uniformAttach_one_eq, ptraceAnc_one_eq, transport_apply]

/-- **THE STRUCTURAL DIRECTION**: a level-one family is available on the system after
transport — from `prepAvail_uniform` and `prepAvail_discard` alone. -/
theorem avail_of_availExt_one (T : FiniteOperationalTheory A) {O : Type} [Fintype O]
    [DecidableEq O]
    (F : O → Matrix (A × Fin 1) (A × Fin 1) ℂ →ₗ[ℂ] Matrix (A × Fin 1) (A × Fin 1) ℂ)
    (hF : T.availExt 1 O F) : T.avail O (fun a => transport (levelOneIdx A) (F a)) := by
  have h := T.prepAvail_discard 1 (uniformAttach 1) O F (T.prepAvail_uniform 0) hF
  simp only [discardWith_uniform_one_eq_transport] at h
  exact h

/-- **THE PRINCIPLE**: an operation available on the system remains available after
adjoining the one-state ancilla. -/
def SystemToLevelOne (T : FiniteOperationalTheory A) : Prop :=
  ∀ (O : Type) [Fintype O] [DecidableEq O] (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail O F → T.availExt 1 O (fun a => transport (levelOneIdx A).symm (F a))

theorem transport_transport_symm {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l]
    [DecidableEq l'] (e : l ≃ l') (Φ : Matrix l' l' ℂ →ₗ[ℂ] Matrix l' l' ℂ) :
    transport e (transport e.symm Φ) = Φ := by
  have := transport_symm_transport e.symm Φ
  rwa [Equiv.symm_symm] at this

/-- **THE EQUIVALENCE COSTS EXACTLY THE PRINCIPLE.** -/
theorem avail_iff_availExt_one (T : FiniteOperationalTheory A) (h : SystemToLevelOne T)
    {O : Type} [Fintype O] [DecidableEq O] (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) :
    T.avail O F ↔ T.availExt 1 O (fun a => transport (levelOneIdx A).symm (F a)) := by
  refine ⟨h O F, fun hF => ?_⟩
  have h' := avail_of_availExt_one T _ hF
  simp only [transport_transport_symm] at h'
  exact h'

end Seam

/-! ### Section B — the Kraus form transports along any reindexing -/

section KrausTransport

variable {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l] [DecidableEq l']

theorem reindex_sum (e : l ≃ l') {ι : Type*} (s : Finset ι) (M : ι → Matrix l l ℂ) :
    Matrix.reindex e e (∑ i ∈ s, M i) = ∑ i ∈ s, Matrix.reindex e e (M i) := by
  ext p q
  simp only [Matrix.reindex_apply, Matrix.submatrix_apply, Matrix.sum_apply]

theorem transport_instrumentBranch (e : l ≃ l') {n m : ℕ} (K : Fin n → Matrix l l ℂ)
    (out : Fin n → Fin m) (a : Fin m) :
    transport e (instrumentBranch K out a)
      = instrumentBranch (fun k => Matrix.reindex e e (K k)) out a := by
  unfold instrumentBranch
  rw [transport_sum]
  exact Finset.sum_congr rfl fun k _ => transport_conjChannel e (K k)

/-- **THE KRAUS FORM IS INVARIANT UNDER REINDEXING** (one direction). -/
theorem isKraus_transport_of (e : l ≃ l') {m : ℕ} (F : Fin m → Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ)
    (h : IsFiniteEndomorphicKrausInstrument F) :
    IsFiniteEndomorphicKrausInstrument (fun a => transport e (F a)) := by
  obtain ⟨n, K, out, hnorm, rfl⟩ := h
  refine ⟨n, fun k => Matrix.reindex e e (K k), out, ?_, ?_⟩
  · rw [Finset.sum_congr rfl fun k _ => by
      rw [Matrix.conjTranspose_reindex, ← reindex_mul], ← reindex_sum, hnorm,
      Matrix.reindex_apply, Matrix.submatrix_one_equiv]
  · funext a
    exact transport_instrumentBranch e K out a

/-- **THE KRAUS FORM IS INVARIANT UNDER REINDEXING** (both directions). -/
theorem isKraus_transport (e : l ≃ l') {m : ℕ} (F : Fin m → Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    IsFiniteEndomorphicKrausInstrument F
      ↔ IsFiniteEndomorphicKrausInstrument (fun a => transport e (F a)) := by
  refine ⟨isKraus_transport_of e F, fun h => ?_⟩
  have := isKraus_transport_of e.symm _ h
  simpa only [transport_symm_transport] using this

end KrausTransport

/-! ### Section C — inheritance and the endpoint -/

section Endpoint

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- **EXACT FINITE ENDOMORPHIC QM ON THE SYSTEM AND EVERY POSITIVE COMPOSITE.** -/
def ExactAllFiniteEndomorphicQuantumOps (T : FiniteOperationalTheory A) : Prop :=
  ExactFiniteEndomorphicQuantumOps T ∧ ExactCompositeQuantumOps T

/-- **SYSTEM EXACTNESS IS INHERITED FROM LEVEL ONE** under the principle. -/
theorem exactSystem_of_levelOne (T : FiniteOperationalTheory A) (h1 : SystemToLevelOne T)
    (hc : ExactCompositeQuantumOps T) : ExactFiniteEndomorphicQuantumOps T := by
  intro m F
  rw [avail_iff_availExt_one T h1 F, isKraus_transport (levelOneIdx A).symm F]
  exact hc 0 m _

theorem exactAll_of_levelOne (T : FiniteOperationalTheory A) (h1 : SystemToLevelOne T)
    (hc : ExactCompositeQuantumOps T) : ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨exactSystem_of_levelOne T h1 hc, hc⟩

end Endpoint

/-- **THE ENDPOINT COVERING THE SYSTEM.** Valid probabilities, inert spectators, composite
unitary control, iterated ancilla closure and system-to-level-one consistency give exact
finite endomorphic quantum operations on the visible system and on every positive
composite, against finite isometry extension at the composite carriers only. -/
theorem exactAll_of_conditions (T : FiniteOperationalTheory (Fin 2))
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
    (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T)
    (hctrl : HasCompositeUnitaryControl T) (hclos : IteratedAncillaClosure T)
    (h1 : SystemToLevelOne T) : ExactAllFiniteEndomorphicQuantumOps T :=
  exactAll_of_levelOne T h1 (exactComposite_of_validity T hext hval hin hctrl hclos)

/-! ### Section D — the full theory satisfies the principle -/

theorem trace_transport {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l] [DecidableEq l']
    (e : l ≃ l') (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) (X : Matrix l' l' ℂ) :
    (transport e Φ X).trace = (Φ (Matrix.reindex e.symm e.symm X)).trace := by
  rw [transport_apply, trace_reindex]

theorem fullQuantum_systemToLevelOne : SystemToLevelOne fullQuantum := by
  intro O _ _ F hF
  refine ⟨fun a => transport_cp _ (krausFamily_cp hF a), fun X => ?_⟩
  simp only [trace_transport]
  obtain ⟨n, K, out, hnorm, hKF⟩ := hF
  rw [Finset.sum_congr rfl fun a _ => by rw [hKF a, LinearMap.sum_apply, Matrix.trace_sum],
    Finset.sum_fiberwise_of_maps_to (fun k _ => Finset.mem_univ (out k))
      (fun k => ((conjChannel (K k)) (Matrix.reindex (levelOneIdx (Fin 2)).symm.symm
        (levelOneIdx (Fin 2)).symm.symm X)).trace)]
  rw [Finset.sum_congr rfl fun k _ => by
    rw [conjChannel_apply, Matrix.trace_mul_cycle (K k) _ (K k)ᴴ]]
  rw [← Matrix.trace_sum, ← Finset.sum_mul, hnorm, Matrix.one_mul, trace_reindex]

/-- **ALL FIVE CONDITIONS ARE JOINTLY SATISFIABLE.** -/
theorem all_conditions_satisfiable :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T :=
  ⟨fullQuantum, fullQuantum_validity, fullQuantum_inert, fullQuantum_control,
    fullQuantum_iteratedAncillaClosure, fullQuantum_systemToLevelOne⟩

/-! ### Section E — the countermodel: an unrestricted system sector -/

/-- **THE LOOSE THEORY**: the full quantum composite sector, preparations and readouts, with
an UNRESTRICTED system predicate. -/
noncomputable def systemLoose : FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ _ => True
  availExt := fun _ _ _ _ F => IsCPInstrument F
  avail_id := trivial
  avail_coarse := fun _ _ _ _ _ _ _ _ _ => trivial
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => cp_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => cp_comp ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
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
      exact cp_referencePositive (Fin 2) _ (hΦ2 ()) _ hPpsd
  readout := fun _ k => localLuders k
  readout_avail := fun n => ⟨fun k => localLuders_cp k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := fun _ _ _ _ _ _ _ _ => trivial

theorem systemLoose_control : HasCompositeUnitaryControl systemLoose :=
  fun _ U hU => ⟨fun _ => conjChannel_cp U, fun X => by
    rw [Fintype.sum_unique]
    exact conjChannel_trace U hU X⟩

theorem systemLoose_krausSoundExt : KrausSoundExt systemLoose :=
  fun _ _ _ _ F ⟨hcp, htr⟩ =>
    isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F hcp htr

theorem systemLoose_validity : CompositeOperationalValidity systemLoose :=
  validity_of_krausSoundExt _ systemLoose_krausSoundExt

theorem systemLoose_parallelReferenceExtension : HasParallelReferenceExtension systemLoose := by
  intro R _ _ n m e O _ _ F ⟨hcp, htr⟩
  refine ⟨fun a => withSpectator_cp e (hcp a), fun X => ?_⟩
  simp only [withSpectator_apply, trace_reindex, trace_amplRef]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun i _ => htr (refBlockR (Matrix.reindex e.symm e.symm X) i i),
    ← trace_eq_sum_refBlockR, trace_reindex e.symm]

theorem systemLoose_inert : InertSpectatorCompositionality systemLoose :=
  (inertSpectator_iff_parallelReferenceExtension _).mpr systemLoose_parallelReferenceExtension

theorem systemLoose_iteratedAncillaClosure : IteratedAncillaClosure systemLoose := by
  intro n m O _ _ F ⟨hcp, htr⟩
  refine ⟨fun a => discardWith_uniform_cp (cp_of_transport_cp _ (hcp a)), fun X => ?_⟩
  rw [Finset.sum_congr rfl fun a _ => discardWith_trace (m + 1) _ (F a) X]
  have h := htr (Matrix.reindex (shiftIdx (Fin 2) n (m + 1)) (shiftIdx (Fin 2) n (m + 1))
    (uniformAttach (m + 1) X))
  simp only [transport_reindex, trace_reindex] at h
  rw [h, uniformAttach_trace (m + 1) m.succ_ne_zero]

theorem systemLoose_exactComposite
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))) :
    ExactCompositeQuantumOps systemLoose :=
  exactComposite_of_validity _ hext systemLoose_validity systemLoose_inert systemLoose_control
    systemLoose_iteratedAncillaClosure

theorem systemLoose_realizesSealedOICore : RealizesSealedOICore systemLoose :=
  realizesSealedOICore_of_control _ systemLoose_control

/-- The trace amplifier is a system-available family of the loose theory. -/
theorem systemLoose_amplifier_available :
    systemLoose.avail (Fin 1) (fun _ => (2 : ℂ) • LinearMap.id) := trivial

/-- **THE LOOSE THEORY IS NOT EXACTLY QUANTUM ON THE SYSTEM.** -/
theorem systemLoose_not_exact : ¬ ExactFiniteEndomorphicQuantumOps systemLoose := by
  intro h
  have hk := (h 1 _).mp systemLoose_amplifier_available
  refine not_kraus_of_trace_ne _ (1 : Matrix (Fin 2) (Fin 2) ℂ) ?_ hk
  simp [Matrix.trace_smul, Matrix.trace_one]

theorem transport_amplifier {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l]
    [DecidableEq l'] (e : l ≃ l') :
    transport e ((2 : ℂ) • LinearMap.id) = (2 : ℂ) • LinearMap.id := by
  rw [transport_smul, transport_id]

/-- **THE LOOSE THEORY FAILS THE PRINCIPLE** — directly, with no isometry hypothesis: the
transported amplifier would have to preserve the aggregate trace at level one. -/
theorem systemLoose_not_systemToLevelOne : ¬ SystemToLevelOne systemLoose := by
  intro h
  have h1 := (h (Fin 1) (fun _ => (2 : ℂ) • LinearMap.id) systemLoose_amplifier_available).2 1
  rw [Fintype.sum_unique] at h1
  simp only [transport_amplifier, LinearMap.smul_apply, LinearMap.id_apply, Matrix.trace_smul,
    Matrix.trace_one, Fintype.card_prod, Fintype.card_fin, smul_eq_mul] at h1
  norm_num at h1

/-- **SYSTEM-TO-LEVEL-ONE IS INDEPENDENT OF EVERY ROUND-41 CONDITION.** The loose theory has
valid probabilities, inert spectators, every composite unitary, iterated ancilla closure,
exact composite operations (against item 2), and realizes the sealed OI core — and is not
exactly quantum on the system, hence fails the principle. -/
theorem levelOne_independent :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ RealizesSealedOICore T
        ∧ ((∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
            → ExactCompositeQuantumOps T)
        ∧ ¬ ExactFiniteEndomorphicQuantumOps T ∧ ¬ SystemToLevelOne T :=
  ⟨systemLoose, systemLoose_validity, systemLoose_inert, systemLoose_control,
    systemLoose_iteratedAncillaClosure, systemLoose_realizesSealedOICore,
    systemLoose_exactComposite, systemLoose_not_exact, systemLoose_not_systemToLevelOne⟩

/-- **THE NEW CLAUSE CANNOT BE DELETED** from the endpoint covering the system. -/
theorem levelOne_not_deletable :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T → InertSpectatorCompositionality T
        → HasCompositeUnitaryControl T → IteratedAncillaClosure T
        → ExactAllFiniteEndomorphicQuantumOps T :=
  fun h => systemLoose_not_exact
    (h systemLoose systemLoose_validity systemLoose_inert systemLoose_control
      systemLoose_iteratedAncillaClosure).1

/-- **THE FINAL CONDITIONAL PACKAGE**: the endpoint implication covering the system, the
joint satisfiability of the five conditions, and the loose witness for the new clause. -/
theorem final_classification :
    (∀ T : FiniteOperationalTheory (Fin 2),
      (∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
        → CompositeOperationalValidity T → InertSpectatorCompositionality T
        → HasCompositeUnitaryControl T → IteratedAncillaClosure T → SystemToLevelOne T
        → ExactAllFiniteEndomorphicQuantumOps T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ ¬ SystemToLevelOne T ∧ ¬ ExactFiniteEndomorphicQuantumOps T) :=
  ⟨fun T hext hval hin hctrl hclos h1 => exactAll_of_conditions T hext hval hin hctrl hclos h1,
    all_conditions_satisfiable,
    ⟨systemLoose, systemLoose_validity, systemLoose_inert, systemLoose_control,
      systemLoose_iteratedAncillaClosure, systemLoose_not_systemToLevelOne,
      systemLoose_not_exact⟩⟩

#print axioms uniformAttach_one_eq
#print axioms ptraceAnc_one_eq
#print axioms discardWith_uniform_one_eq_transport
#print axioms avail_of_availExt_one
#print axioms transport_transport_symm
#print axioms avail_iff_availExt_one
#print axioms reindex_sum
#print axioms transport_instrumentBranch
#print axioms isKraus_transport_of
#print axioms isKraus_transport
#print axioms exactSystem_of_levelOne
#print axioms exactAll_of_levelOne
#print axioms exactAll_of_conditions
#print axioms trace_transport
#print axioms fullQuantum_systemToLevelOne
#print axioms all_conditions_satisfiable
#print axioms systemLoose_control
#print axioms systemLoose_krausSoundExt
#print axioms systemLoose_validity
#print axioms systemLoose_parallelReferenceExtension
#print axioms systemLoose_inert
#print axioms systemLoose_iteratedAncillaClosure
#print axioms systemLoose_exactComposite
#print axioms systemLoose_realizesSealedOICore
#print axioms systemLoose_amplifier_available
#print axioms systemLoose_not_exact
#print axioms transport_amplifier
#print axioms systemLoose_not_systemToLevelOne
#print axioms levelOne_independent
#print axioms levelOne_not_deletable
#print axioms final_classification

end LevelOneSeam
end OIBridge
