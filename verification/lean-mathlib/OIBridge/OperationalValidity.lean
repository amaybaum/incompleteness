/-
  OIBridge/OperationalValidity.lean — the quantum-shaped premise removed: valid probabilities
  plus inert spectators give complete positivity, and the exact-composite endpoint needs
  neither system Kraus soundness nor the one-dimensional isometry hypothesis.

  ROUND FORTY-ONE. The frozen classification (rounds 38–39) still assumed `KrausSound T`,
  "everything the theory allows on the system already has Kraus form" — a quantum-shaped
  restriction that round twenty-six showed cannot come from richness (`everywhereAvailable`
  admits `X ↦ 2X`). This file replaces it by a condition with an observer-level reading:

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `CompositeOperationalValidity T`: every available family at every positive     │
      │    composite level PRODUCES VALID PROBABILITIES — each branch carries positive   │
      │    semidefinite states to positive semidefinite states, and the outcomes sum to  │
      │    a trace-preserving map. No CP, no Choi matrix, no Kraus form in the definition.│
      │  `krausSoundExt_of_validity_inert`:                                             │
      │    CompositeOperationalValidity T ∧ InertSpectatorCompositionality T             │
      │      ⟹ KrausSoundExt T.                                                          │
      │    Inert spectators promote positivity to complete positivity: adjoin an          │
      │    untouched copy of the composite as the reference, the extended branch is      │
      │    available and therefore positive, its value on the maximally entangled dyad   │
      │    IS the Choi matrix (`choiMatrix_eq_amplRef`), so the Choi matrix is PSD; the   │
      │    aggregate trace supplies normalization; the factorization is kernel-internal. │
      │    No system soundness, no unitary control, no isometry extension.              │
      │  `exactComposite_of_validity` (qubit system):                                    │
      │    CompositeOperationalValidity ∧ InertSpectatorCompositionality                 │
      │      ∧ HasCompositeUnitaryControl ∧ IteratedAncillaClosure                       │
      │      ⟹ ExactCompositeQuantumOps, against boundary item 2 at the COMPOSITE       │
      │    carriers only — the `Unit` isometry hypothesis of rounds 36–39 is gone.        │
      │  `validity_not_implies_krausSoundExt`: validity is strictly weaker than          │
      │    composite soundness (the round-34 countermodel is valid), so the spectator     │
      │    clause does real work; `krausSoundExt_iff_validity_of_inert`: under inert      │
      │    spectators the two coincide.                                                  │
      │  `physical_classification`: the frozen classification restated with validity in  │
      │    place of system soundness, with the three witnesses.                          │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHAT THE REMAINING CONDITIONS SAY, in physical words. Valid probabilities (positive
  outcomes summing to one); sufficient reversible control (every composite unitary);
  inert spectators (adjoining an untouched system changes nothing an intervention does);
  the ability to reuse a composite as a working system (iterated ancilla closure). Under
  these, and finite isometry extension at the composite carriers, the available finite
  outcome families at every positive level are EXACTLY the normalized finite Kraus
  instruments. Complete positivity is not assumed anywhere: it is what inert spectators make
  of ordinary positivity.

  WHAT ROUND FORTY MEANS FOR THE READING OF THE ENDPOINT, recorded here as directed.
  `realizesSealedOICore_of_control` shows that full composite unitary control by itself
  realizes the sealed OI core; so in the conditional endpoint the OI premise does no
  additional logical work once control is assumed. The theorem is therefore a CLASSIFICATION
  OF OPERATIONAL COMPLETIONS COMPATIBLE WITH OI — which completions of an OI process are
  exactly quantum on every composite — and not yet a derivation of the quantum structure
  from OI alone. This round improves the situation by making the remaining conditions
  observer-level rather than quantum-formal; it does not change that reading.

  NOT claimed: that validity or inert spectators follow from OI (round forty's countermodels
  bound both); OI ⟺ QM; anything about the visible-system sector `avail` itself, whose
  consistency with level-one `availExt` is a separate architectural seam (round forty-two).
  No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.OIRealization

namespace OIBridge
namespace OperationalValidity

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization

open scoped ComplexOrder

/-! ### Section A — operational validity -/

section Validity

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **COMPOSITE OPERATIONAL VALIDITY**: every available family at every composite level
produces valid probabilities — each branch carries positive semidefinite matrices to
positive semidefinite matrices, and the outcomes sum to a trace-preserving map. (At level
zero the carrier is empty and the clause is vacuous, so quantifying over every level costs
nothing and spares a successor bookkeeping.) -/
def CompositeOperationalValidity (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F →
      (∀ a (X : Matrix (A × Fin n) (A × Fin n) ℂ), X.PosSemidef → ((F a) X).PosSemidef)
        ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace

/-- The reindexing that adjoins an untouched copy of the composite as the reference:
`R × (A × Fin (n+1)) ≃ A × Fin (card R · (n+1))`. -/
noncomputable def selfRefIdx (R : Type) [Fintype R] (n : ℕ) :
    R × (A × Fin (n + 1)) ≃ A × Fin (Fintype.card R * (n + 1)) :=
  (Equiv.prodCongr (Fintype.equivFin R) (Equiv.refl (A × Fin (n + 1)))).trans
    (specIdx A (Fintype.card R) (n + 1))

/-- **INERT SPECTATORS PROMOTE POSITIVITY TO COMPLETE POSITIVITY.** An available branch whose
spectator extension by an untouched copy of the composite is positive has a positive
semidefinite Choi matrix. -/
theorem cp_of_valid_inert (T : FiniteOperationalTheory A) (hval : CompositeOperationalValidity T)
    (hin : InertSpectatorCompositionality T) {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin (n + 1)) (A × Fin (n + 1)) ℂ →ₗ[ℂ]
      Matrix (A × Fin (n + 1)) (A × Fin (n + 1)) ℂ)
    (hF : T.availExt (n + 1) O F) (a : O) : IsCompletelyPositive (F a) := by
  -- the spectator extension by an untouched copy of the composite is available ...
  have hext := (inertSpectator_iff_parallelReferenceExtension T).mp hin (A × Fin (n + 1))
    (n + 1) _ (selfRefIdx (A := A) (A × Fin (n + 1)) n) O F hF
  -- ... hence positive, in particular on the reindexed maximally entangled dyad
  have hpos := (hval _ O _ hext).1 a
    (Matrix.reindex (selfRefIdx (A := A) (A × Fin (n + 1)) n) (selfRefIdx (A := A) (A × Fin (n + 1)) n)
      (Matrix.vecMulVec (maxEntVec (S := A × Fin (n + 1))) (star maxEntVec)))
    (posSemidef_reindex _ (Matrix.posSemidef_vecMulVec_self_star _))
  rw [withSpectator_reindex] at hpos
  show (choiMatrix (F a)).PosSemidef
  rw [choiMatrix_eq_amplRef]
  exact posSemidef_of_reindex _ hpos

/-- **COMPOSITE SOUNDNESS FROM VALID PROBABILITIES AND INERT SPECTATORS.** -/
theorem krausSoundExt_of_validity_inert [Nonempty A] (T : FiniteOperationalTheory A)
    (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T) :
    KrausSoundExt T :=
  fun n O _ _ F hF =>
    isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F
      (fun a => cp_of_valid_inert T hval hin F hF a) (hval (n + 1) O F hF).2

/-- Composite soundness implies validity (CP maps are positive). -/
theorem validity_of_krausSoundExt (T : FiniteOperationalTheory A) (hs : KrausSoundExt T) :
    CompositeOperationalValidity T := by
  intro n O _ _ F hF
  rcases n with _ | n
  · -- level zero: the carrier is empty, every matrix is zero and every trace vanishes
    refine ⟨fun a X _ => ?_, fun X => ?_⟩
    · have h0 : (F a) X = 0 := by
        ext p q
        exact p.2.elim0
      rw [h0]
      exact Matrix.PosSemidef.zero
    · have h0 : ∀ Y : Matrix (A × Fin 0) (A × Fin 0) ℂ, Y.trace = 0 := fun Y => by
        simp only [Matrix.trace, Matrix.diag_apply]
        exact Finset.sum_eq_zero fun p _ => p.2.elim0
      simp only [h0, Finset.sum_const_zero]
  have hK := hs n O F hF
  refine ⟨fun a X hX => cp_apply_posSemidef (krausFamily_cp hK a) hX, fun X => ?_⟩
  obtain ⟨m, K, out, hnorm, hKF⟩ := hK
  rw [Finset.sum_congr rfl fun a _ => by rw [hKF a, LinearMap.sum_apply, Matrix.trace_sum],
    Finset.sum_fiberwise_of_maps_to (fun k _ => Finset.mem_univ (out k))
      (fun k => ((conjChannel (K k)) X).trace)]
  rw [Finset.sum_congr rfl fun k _ => by
    rw [conjChannel_apply, Matrix.trace_mul_cycle (K k) X (K k)ᴴ]]
  rw [← Matrix.trace_sum, ← Finset.sum_mul, hnorm, Matrix.one_mul]

/-- **UNDER INERT SPECTATORS, VALIDITY IS SOUNDNESS.** -/
theorem krausSoundExt_iff_validity_of_inert [Nonempty A] (T : FiniteOperationalTheory A)
    (hin : InertSpectatorCompositionality T) :
    KrausSoundExt T ↔ CompositeOperationalValidity T :=
  ⟨validity_of_krausSoundExt T, fun hval => krausSoundExt_of_validity_inert T hval hin⟩

end Validity

/-! ### Section B — validity is strictly weaker than soundness -/

theorem countermodel_validity : CompositeOperationalValidity countermodel := by
  intro n O _ _ F ⟨h2, htr⟩
  exact ⟨fun a X hX => positive_of_twoPositive (h2 a) hX, htr⟩

theorem admissible_validity : CompositeOperationalValidity admissibleTheory :=
  validity_of_krausSoundExt _ admissible_krausSoundExt

theorem fullQuantum_validity : CompositeOperationalValidity fullQuantum :=
  validity_of_krausSoundExt _ fullQuantum_krausSoundExt

/-- **VALIDITY DOES NOT IMPLY SOUNDNESS**: the round-34 countermodel produces valid
probabilities at every level and is not composite-sound. The spectator clause of
`krausSoundExt_of_validity_inert` is doing real work. -/
theorem validity_not_implies_krausSoundExt :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ ExactFiniteEndomorphicQuantumOps T
        ∧ HasCompositeUnitaryControl T ∧ ¬ KrausSoundExt T :=
  ⟨countermodel, countermodel_validity, countermodel_exact, countermodel_control,
    countermodel_not_krausSoundExt⟩

/-! ### Section C — the endpoint without the quantum-shaped premise -/

/-- **THE EXACT-COMPOSITE ENDPOINT FROM PHYSICAL CONDITIONS.** Valid probabilities, inert
spectators, composite unitary control and iterated ancilla closure give exact finite Kraus
operations at every positive level, against finite isometry extension at the composite
carriers only. No system Kraus soundness; no `Unit` isometry hypothesis. -/
theorem exactComposite_of_validity (T : FiniteOperationalTheory (Fin 2))
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
    (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T)
    (hctrl : HasCompositeUnitaryControl T) (hclos : IteratedAncillaClosure T) :
    ExactCompositeQuantumOps T :=
  exactComposite_of_soundExt_full T (krausSoundExt_of_validity_inert T hval hin)
    (compositeCompleteness T hext hctrl hin hclos)

/-- **THE PHYSICAL CLASSIFICATION**: the endpoint implication with validity in place of
system soundness, together with the three witnesses (valid probabilities in each). -/
theorem physical_classification :
    (∀ T : FiniteOperationalTheory (Fin 2),
      (∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
        → CompositeOperationalValidity T → InertSpectatorCompositionality T
        → HasCompositeUnitaryControl T → IteratedAncillaClosure T → ExactCompositeQuantumOps T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ ¬ InertSpectatorCompositionality T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T
        ∧ InertSpectatorCompositionality T ∧ ¬ IteratedAncillaClosure T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T
        ∧ InertSpectatorCompositionality T ∧ IteratedAncillaClosure T) :=
  ⟨fun T hext hval hin hctrl hclos => exactComposite_of_validity T hext hval hin hctrl hclos,
    ⟨countermodel, countermodel_validity, countermodel_control,
      countermodel_iteratedAncillaClosure, countermodel_not_inert⟩,
    ⟨admissibleTheory, admissible_validity, admissible_control, admissible_inert,
      admissible_not_iteratedAncillaClosure⟩,
    ⟨fullQuantum, fullQuantum_validity, fullQuantum_control, fullQuantum_inert,
      fullQuantum_iteratedAncillaClosure⟩⟩

/-- Neither compositional clause can be deleted from the physical endpoint either. -/
theorem physical_inert_not_deletable :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T → HasCompositeUnitaryControl T → IteratedAncillaClosure T
        → ExactCompositeQuantumOps T :=
  fun h => countermodel_not_exactComposite
    (h countermodel countermodel_validity countermodel_control
      countermodel_iteratedAncillaClosure)

theorem physical_closure_not_deletable :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T → HasCompositeUnitaryControl T
        → InertSpectatorCompositionality T → ExactCompositeQuantumOps T :=
  fun h => admissible_not_exactComposite
    (h admissibleTheory admissible_validity admissible_control admissible_inert)

#print axioms cp_of_valid_inert
#print axioms krausSoundExt_of_validity_inert
#print axioms validity_of_krausSoundExt
#print axioms krausSoundExt_iff_validity_of_inert
#print axioms countermodel_validity
#print axioms admissible_validity
#print axioms fullQuantum_validity
#print axioms validity_not_implies_krausSoundExt
#print axioms exactComposite_of_validity
#print axioms physical_classification
#print axioms physical_inert_not_deletable
#print axioms physical_closure_not_deletable

end OperationalValidity
end OIBridge
