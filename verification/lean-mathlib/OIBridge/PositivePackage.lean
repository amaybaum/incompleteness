/-
  OIBridge/PositivePackage.lean — the theory-level consequence of positive reachability: the
  package without dagger stability, `OIPlusPos`, and its equivalence with finite operational
  quantum mechanics.

  The positive-reachability development itself (`PositiveReachability.lean`, Sections A–G) is
  stated on the reachable monoid alone and sits upstream of the implementation-locality stack,
  so that `control_of_lieRank` and `inverseAccessibility_of_lieRank`
  (`MicroscopicReversibility.lean`) can supply the inverse clause of reversible richness to the
  compressed sets without consuming dagger stability. This module holds the package that needs
  the elementary transitions of `LieRankSource`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.PositiveReachability
import OIBridge.LieRankSource

namespace OIBridge
namespace PositiveReachability

open Complex Matrix ControlLie MonoidalCompletion ReachabilitySeam OrbitReachability
open OperationalAssembly AncillaClosure OIHierarchyGeneral MicroReversibility InterventionLocality
open PrimitiveSource LieRankSource GeneralCarrier PhysicalCharacterization LevelOneSeam

open scoped ComplexOrder

/-! ### The theory-level consequence: dagger stability leaves the package -/

section Theory

variable {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A)

/-- **THE PACKAGE WITHOUT DAGGER STABILITY**: implementation locality, elementary transition
richness, embedded observation. -/
def OIPlusPos : Prop :=
  ImplementationLocality T ∧ ElementaryTransitionRichness T ∧ EmbeddedObservation T

variable [Nonempty A]

theorem qm_of_oiPlusPos (h : OIPlusPos T) : ExactAllFiniteEndomorphicQuantumOps T := by
  obtain ⟨hloc, helem, hemb⟩ := h
  have hwf : WellFormed T :=
    ⟨validity_of_implementationLocality hloc, systemToLevelOne_of_embeddedObservation hemb⟩
  rw [exactAll_iff_substantive T hwf]
  exact ⟨(observationalIndependence_iff_inert T).mp
      (observationalIndependence_of_implementationLocality hloc),
    control_of_lieRank T (lieRank_of_elementary T helem), closure_of_embeddedObservation hemb⟩

theorem oiPlusPos_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlusPos T :=
  ⟨implementationLocality_of_qm T h, elementary_of_control T (physical_of_exactAll T h).2.2.1,
    embeddedObservation_of_qm T h⟩

/-- **THE PACKAGE WITHOUT DAGGER STABILITY ⟺ FINITE OPERATIONAL QM**, on any nonempty finite
carrier. -/
theorem oiPlusPos_iff_qm : OIPlusPos T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlusPos T, oiPlusPos_of_qm T⟩

omit [Nonempty A] in
theorem oiPlusPos_of_oiPlusElem (h : OIPlusElem T) : OIPlusPos T :=
  ⟨implementationLocality_of_reversible h.1, h.2.1, h.2.2⟩

theorem oiPlusPos_iff_oiPlusElem : OIPlusPos T ↔ OIPlusElem T := by
  rw [oiPlusPos_iff_qm, oiPlusElem_iff_qm]

end Theory

/-- **THE CARRIER-GENERAL STATEMENT**, quantified over the carrier. -/
theorem carrier_general_oiPlusPos :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A]
      (T : OperationalAssembly.FiniteOperationalTheory A),
      OIPlusPos T ↔ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps T :=
  fun _ _ _ _ T => oiPlusPos_iff_qm T

#print axioms oiPlusPos_iff_qm
#print axioms oiPlusPos_iff_oiPlusElem
#print axioms carrier_general_oiPlusPos

end PositiveReachability
end OIBridge
