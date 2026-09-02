/-
  OIBridge/GeneralCarrier.lean — the qubit restriction removed: for EVERY nonempty finite
  observable system, exact finite endomorphic quantum mechanics is characterized exactly by
  the five physical completion conditions. The main research result, frozen.

  ROUND FORTY-SIX. The round-43 characterization and its round-45 unconditional form were
  stated for a qubit system, `FiniteOperationalTheory (Fin 2)`, because the OI countermodels
  live there. The restriction was historical: every link of the chain is already
  carrier-general — `krausSoundExt_of_validity_inert` (validity + inert spectators ⟹ composite
  soundness, any nonempty `A`), `compositeCompleteness` (control + inert spectators + closure
  ⟹ composite completeness, any `A`, unconditional since round forty-five),
  `exactComposite_of_soundExt_full`, `exactAll_of_levelOne` (system-to-level-one ⟹ system
  exactness) and `physical_of_exactAll` (necessity, any nonempty `A`). This file assembles
  them. No new mathematics, no new boundary.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `exactAll_iff_physical_general (T : FiniteOperationalTheory A)` [Nonempty A]: │
      │      ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T.   │
      │  `general_characterization`: the same, closed over every nonempty finite `A`.  │
      │  `exactAll_iff_substantive`: for WELL-FORMED theories (valid probabilities and  │
      │    trivial-ancilla consistency) the characterization is by the THREE            │
      │    substantive principles — inert spectators, sufficient reversible control,    │
      │    iterated composition.                                                       │
      │  `main_result`: the general characterization, joint satisfiability, the qubit  │
      │    five-way minimality audit, and OI alone ≠ QM, in one statement.             │
      └──────────────────────────────────────────────────────────────────────────────┘

  THE INTERPRETATION, made precise. Two of the five conditions are well-formedness
  requirements of any operational theory: valid probabilities (`CompositeOperationalValidity`)
  and consistency under a trivial one-state ancilla (`SystemToLevelOne`). The genuinely
  substantive selection principles are three: (1) INERT SPECTATORS — an independent system
  can be adjoined without changing an intervention; (2) SUFFICIENT REVERSIBLE CONTROL — every
  finite unitary is operationally available; (3) ITERATED COMPOSITION — a composite can itself
  be treated as the working system of a larger experiment. Bare finite OI supplies none of
  them: the round-44 five-way audit exhibits, for each, an OI-realizing qubit theory with the
  other four and without it. Hence OI ALONE ≠ QM (`oi_alone_not_qm`), while an OI-COMPATIBLE
  operational theory satisfying the five conditions IS finite operational QM
  (`oi_compatible_classification`). The theorem is a classification of OI-compatible
  completions; it is not "OI derives QM" — with full control assumed, the OI-realization
  clause is redundant for the sealed core (`realizesSealedOICore_of_control`), and that is
  said explicitly rather than hidden.

  THE EMPTY SYSTEM. `Nonempty A` is used in both directions (necessity through
  `availExt_pos_iff`, sufficiency through `krausSoundExt_of_validity_inert`); the empty
  carrier is excluded from the statement, not silently.

  WHAT IS AND IS NOT CLAIMED. Proved: everything above, with the usual axiom footprint.
  NOT claimed: minimality of the five conditions on carriers other than the qubit (a single
  qubit witness per cell proves logical independence of the conditions, which is what
  minimality means; carrier-specific witnesses are not needed and not built); that any
  condition follows from OI; OI ⟺ QM; anything about the two remaining boundary items.
  No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.IsometryExtension

namespace OIBridge
namespace GeneralCarrier

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open RankGapTheory IsometryExtension HiddenCoherence

open scoped ComplexOrder

/-! ### Section A — the chain, for every nonempty finite system -/

section General

variable {A : Type} [Fintype A] [DecidableEq A] [Nonempty A]

/-- Validity + inert spectators give composite soundness; control + inert spectators +
closure give composite completeness; together, exact composite operations — for any
nonempty finite system. -/
theorem exactComposite_of_validity_general (T : FiniteOperationalTheory A)
    (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T)
    (hctrl : HasCompositeUnitaryControl T) (hclos : IteratedAncillaClosure T) :
    ExactCompositeQuantumOps T :=
  exactComposite_of_soundExt_full T (krausSoundExt_of_validity_inert T hval hin)
    (compositeCompleteness_unconditional T hctrl hin hclos)

/-- With trivial-ancilla consistency, system exactness is inherited from level one. -/
theorem exactAll_of_conditions_general (T : FiniteOperationalTheory A)
    (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T)
    (hctrl : HasCompositeUnitaryControl T) (hclos : IteratedAncillaClosure T)
    (h1 : SystemToLevelOne T) : ExactAllFiniteEndomorphicQuantumOps T :=
  exactAll_of_levelOne T h1 (exactComposite_of_validity_general T hval hin hctrl hclos)

theorem exactAll_of_physical_general (T : FiniteOperationalTheory A)
    (h : PhysicalCompletionConditions T) : ExactAllFiniteEndomorphicQuantumOps T :=
  exactAll_of_conditions_general T h.1 h.2.1 h.2.2.1 h.2.2.2.1 h.2.2.2.2

/-- **THE CHARACTERIZATION, FOR EVERY NONEMPTY FINITE SYSTEM.** Exact finite endomorphic
quantum operations on the system and every positive composite hold if and only if the five
physical completion conditions hold. No isometry hypothesis, no qubit restriction. -/
theorem exactAll_iff_physical_general (T : FiniteOperationalTheory A) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T :=
  ⟨physical_of_exactAll T, exactAll_of_physical_general T⟩

end General

/-- The characterization, closed over every nonempty finite carrier. -/
theorem general_characterization :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A),
      ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T :=
  fun _ _ _ _ T => exactAll_iff_physical_general T

/-- The qubit statement of round forty-five is the special case `A = Fin 2`. -/
theorem exactAll_iff_physical_unconditional_of_general (T : FiniteOperationalTheory (Fin 2)) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T :=
  exactAll_iff_physical_general T

/-! ### Section B — well-formedness and the three substantive principles -/

section Substantive

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **WELL-FORMEDNESS**: valid probabilities and consistency under a trivial one-state
ancilla — basic requirements of any operational theory, not selection principles. -/
def WellFormed (T : FiniteOperationalTheory A) : Prop :=
  CompositeOperationalValidity T ∧ SystemToLevelOne T

/-- **THE THREE SUBSTANTIVE SELECTION PRINCIPLES**: inert spectators, sufficient reversible
control, iterated composition. -/
def SubstantiveCompletion (T : FiniteOperationalTheory A) : Prop :=
  InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T

/-- The five conditions are exactly well-formedness plus the three substantive principles
(a propositional regrouping). -/
theorem physical_iff_wellFormed_substantive (T : FiniteOperationalTheory A) :
    PhysicalCompletionConditions T ↔ WellFormed T ∧ SubstantiveCompletion T :=
  ⟨fun h => ⟨⟨h.1, h.2.2.2.2⟩, ⟨h.2.1, h.2.2.1, h.2.2.2.1⟩⟩,
    fun h => ⟨h.1.1, h.2.1, h.2.2.1, h.2.2.2, h.1.2⟩⟩

variable [Nonempty A]

/-- **THE CHARACTERIZATION FOR WELL-FORMED THEORIES**: exact finite operational QM iff the
three substantive principles. -/
theorem exactAll_iff_substantive (T : FiniteOperationalTheory A) (hwf : WellFormed T) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ SubstantiveCompletion T := by
  rw [exactAll_iff_physical_general, physical_iff_wellFormed_substantive]
  exact ⟨fun h => h.2, fun h => ⟨hwf, h⟩⟩

theorem exactAll_iff_wellFormed_substantive (T : FiniteOperationalTheory A) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ WellFormed T ∧ SubstantiveCompletion T := by
  rw [exactAll_iff_physical_general, physical_iff_wellFormed_substantive]

end Substantive

/-! ### Section C — OI alone is not QM; OI-compatible completions are classified -/

/-- **OI ALONE ≠ QM**: a theory realizing the sealed OI core that is not exactly quantum
(the diagonal-preserving theory; the round-34 countermodel and the rank-gap theory are
further witnesses). -/
theorem oi_alone_not_qm :
    ∃ T : FiniteOperationalTheory (Fin 2),
      RealizesSealedOICore T ∧ ¬ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨diagTheory, diag_realizesSealedOICore, diag_not_exactAll⟩

/-- **THE CLASSIFICATION OF OI-COMPATIBLE COMPLETIONS**: among theories realizing the sealed
OI core, exact finite operational QM is exactly the five conditions; and OI realization is
not what does the work — every theory with full composite control realizes the core. -/
theorem oi_compatible_classification :
    (∀ T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T →
      (ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T))
    ∧ (∀ T : FiniteOperationalTheory (Fin 2), HasCompositeUnitaryControl T →
      RealizesSealedOICore T) :=
  ⟨fun T _ => exactAll_iff_physical_general T, fun T hctrl => realizesSealedOICore_of_control T hctrl⟩

/-- Every OI-realizing theory satisfying the three substantive principles and the two
well-formedness requirements is exactly finite operational QM; the converse holds as well. -/
theorem oi_compatible_iff (T : FiniteOperationalTheory (Fin 2)) (_hoi : RealizesSealedOICore T) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ WellFormed T ∧ SubstantiveCompletion T :=
  exactAll_iff_wellFormed_substantive T

/-! ### Section D — the main research result, frozen -/

/-- **THE MAIN RESULT.** (i) For every nonempty finite observable system, exact finite
endomorphic quantum mechanics is characterized exactly by the five physical completion
conditions; (ii) the conditions are jointly satisfiable; (iii) on the qubit, each condition
is independent of the other four and of OI realization (the five-way audit); (iv) OI alone
does not select QM. No external boundary item enters any clause. -/
theorem main_result :
    (∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A),
      ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), PhysicalCompletionConditions T)
    ∧ ((∃ T : FiniteOperationalTheory (Fin 2),
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
        ∧ ¬ SystemToLevelOne T))
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      RealizesSealedOICore T ∧ ¬ ExactAllFiniteEndomorphicQuantumOps T) :=
  ⟨general_characterization,
    ⟨fullQuantum, physical_of_exactAll fullQuantum fullQuantum_exactAll⟩,
    five_way_minimality, oi_alone_not_qm⟩

#print axioms exactComposite_of_validity_general
#print axioms exactAll_of_conditions_general
#print axioms exactAll_of_physical_general
#print axioms exactAll_iff_physical_general
#print axioms general_characterization
#print axioms exactAll_iff_physical_unconditional_of_general
#print axioms physical_iff_wellFormed_substantive
#print axioms exactAll_iff_substantive
#print axioms exactAll_iff_wellFormed_substantive
#print axioms oi_alone_not_qm
#print axioms oi_compatible_classification
#print axioms oi_compatible_iff
#print axioms main_result

end GeneralCarrier
end OIBridge
