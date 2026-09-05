import OIBridge.EmbeddedObservation

/-!
# The level-one seam is not supplied by observer recursion

The completion-assumption ledger (`verification/EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md`,
row `SystemToLevelOne`) asks whether the system-to-level-one seam can be derived from embedded
observation or from observer recursion. The first is a theorem of round fifty-six
(`PrimitiveSource.systemToLevelOne_of_embeddedObservation`). This file records the second half
of the row: **observer recursion does not supply the seam**, even together with composite
operational validity, inert spectators, composite unitary control, iterated ancilla closure and
the sealed OI core.

The witness is the round-49 loose theory `systemLoose`: every family is available on the
system, CP instruments on every composite. It has control, inert spectators and closure, which
are exactly what the round-53 construction `observerRecursion_of_closure` consumes, so it has
observer recursion (`systemLoose_observerRecursion`); and it has no level-one seam
(`systemLoose_not_systemToLevelOne`), since the trace amplifier is system-available but not
available at level one.

So the row closes as: derived from embedded observation, independent of observer recursion. The
gap between the two principles is relabelling invariance — embedded observation transports
availability along `A ≃ A × Fin 1`, observer recursion relates level `n` of `T` to level `0` of
a shifted theory and never touches `T`'s own system families.

**Not claimed.** Nothing about the other rows of the ledger; they are recorded in
`verification/COMPLETION-ASSUMPTION-AUDIT.md` with their existing kernel witnesses.
-/

namespace OIBridge
namespace LevelOneRecursion

open OperationalAssembly AncillaClosure SpectatorBridge OperationalValidity LevelOneSeam
open PhysicalCharacterization OIRealization OIHierarchy

/-- **The loose theory has observer recursion**: it has the identity at every level (from
control), the relative readout at every level pair (from inert spectators), and iterated ancilla
closure, which is all the shifted-theory construction consumes. -/
theorem systemLoose_observerRecursion : ObserverRecursion systemLoose :=
  observerRecursion_of_closure systemLoose (availExt_id_of_control _ systemLoose_control)
    (availExt_relativeReadout _ systemLoose_inert) systemLoose_iteratedAncillaClosure

/-- **The level-one seam is independent of observer recursion.** A theory with composite
operational validity, inert spectators, composite unitary control, iterated ancilla closure,
observer recursion and the sealed OI core, and no system-to-level-one seam. -/
theorem levelOne_independent_of_recursion :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ ObserverRecursion T
        ∧ RealizesSealedOICore T ∧ ¬ SystemToLevelOne T :=
  ⟨systemLoose, systemLoose_validity, systemLoose_inert, systemLoose_control,
    systemLoose_iteratedAncillaClosure, systemLoose_observerRecursion,
    systemLoose_realizesSealedOICore, systemLoose_not_systemToLevelOne⟩

/-- **The row, both halves.** The seam is derived from embedded observation and not from
observer recursion. -/
theorem levelOne_row :
    (∀ T : FiniteOperationalTheory (Fin 2), PrimitiveSource.EmbeddedObservation T → SystemToLevelOne T)
    ∧ ¬ ∀ T : FiniteOperationalTheory (Fin 2), ObserverRecursion T → SystemToLevelOne T :=
  ⟨fun _ h => PrimitiveSource.systemToLevelOne_of_embeddedObservation h,
    fun h => systemLoose_not_systemToLevelOne (h _ systemLoose_observerRecursion)⟩

#print axioms systemLoose_observerRecursion
#print axioms levelOne_independent_of_recursion
#print axioms levelOne_row

end LevelOneRecursion
end OIBridge
