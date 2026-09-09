/-
  OIBridge/OperationalSourcing.lean — targets of `OI-OPERATIONAL-SOURCING-AUDIT.md`.

  Frozen preregistration: commit `15e29b25f97319303738031b1bc87a364bb9c714`, blob
  `e9ca45351b58354564552471aa8fe81537a8e557`, merged to `main` by PR #551.

  This module carries **S3b, the stability theorem**, and nothing else.  S1, S2 and S3a live in
  their own sections of the round and are not attempted here.

  WHAT S3b IS, AND WHAT IT IS NOT.  The disposition of relative-phase control at the stated access
  is settled and merged: `permClass` is ones-fixing and no ones-fixing architecture's theory has a
  quarter phase at a carrier with two or more states (`permClass_onesFixing`,
  `onesFixing_not_phasesAvailable`, `permTheory_not_phasesAvailable_onesFixing`).  That verdict is
  **inherited**, and nothing here re-proves it, restates it more strongly, or counts it as this
  round's adjudication.

  What is this round's is the reconciliation of that merged verdict with the layer Arc C added:
  `Q*` membership, the inclusion `C_OI ⊆ Q*`, and facts about a representing datum add no available
  operation under the stated access, so the inherited verdict is unchanged against Arc C.

  THE ROUTE, AS FROZEN.  Availability in `genTheory 𝓘 arch A` *is* `InstAvail 𝓘`, whose five
  constructors draw operator content only from the admissible class `𝓘` and from protocols built
  from it.  A `QfbData` is not a class, `QStar Γ` is a proposition about a rooted family, and
  neither is a constructor or an admissible protocol.  So the stability theorems below carry their
  Arc C data as hypotheses and discharge them by not using them: `instAvail_congr` is the positive
  content — availability is a function of the class alone — and the unused Arc C hypotheses are the
  statement that the representation layer is not among its inputs.

  WHAT IS AND IS NOT PROVED.  This package proves class-extensionality of availability, together
  with stability when Arc C facts are carried as extra hypotheses under the **fixed stated access**.
  It does **not** prove that an arbitrary newly defined access constructed out of Arc C data would
  equal `permClass`; that is the augmentation question, and it is S3a's, not this module's.  The
  inert-hypothesis statements are provenance-quarantine certificates and may not be promoted into a
  theorem about every imaginable Arc-C-derived augmented access.

  This is a **definitional** stability result, and the module says so rather than dressing it up.
  Its value is that it closes an inference route, not that it is deep.  It is also why RD3 of the
  frozen taxonomy is a real outcome class: S3b rests on the access semantics, not on S1 or S2.

  Kernel check:  cd verification/lean-mathlib && lake build
-/
import OIBridge.PhaseSource
import OIBridge.QuantumRepresentationT3

namespace OIBridge

namespace OperationalSourcing

open Matrix InterventionLocality LieRankSource RouteB
open SubstratumInterfaceAudit InstrumentRealization PhaseSource
open OIBridge.QuantumRepresentation

set_option linter.unusedSectionVars false

/-! ### Availability is a function of the admissible class

`instAvail_mono` is merged.  Applying it in both directions gives the congruence that carries the
positive half of S3b: two classes with the same members generate the same availability, so nothing
outside the class can enter through a constructor. -/

/-- **THE ACCESS DETERMINES AVAILABILITY**: classes with the same admissible operators have the
same available families, at every carrier and outcome set. -/
theorem instAvail_congr {𝓘 𝓙 : ImplementationClass}
    (h : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K ↔ 𝓙 S K)
    {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} :
    InstAvail 𝓘 T O F ↔ InstAvail 𝓙 T O F :=
  ⟨instAvail_mono (fun S _ _ K hK => (h S K).1 hK),
   instAvail_mono (fun S _ _ K hK => (h S K).2 hK)⟩

/-- The same statement for the theory a class generates, at the level the resource predicates of
`RouteB` are stated at: an extended-level family available for one class is available for any class
with the same members. -/
theorem availExt_congr {𝓘 𝓙 : ImplementationClass} (arch : Architecture 𝓘) (arch' : Architecture 𝓙)
    (h : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K ↔ 𝓙 S K)
    {A : Type} [Fintype A] [DecidableEq A] (n : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (genTheory 𝓘 arch A).availExt n O F ↔ (genTheory 𝓙 arch' A).availExt n O F :=
  instAvail_congr h

/-! ### S3b — the stability theorem

Each statement below carries the Arc C layer as hypotheses and does not use them.  That is the
content: the representation layer is not an input to availability, so it cannot move a verdict the
stated access has already settled. -/

variable {V : Type} [Fintype V] [DecidableEq V]

/-- **S3b, GENERAL FORM.**  A resource available under the stated access stays available in the
presence of the whole Arc C layer: a rooted family, its `Q*` membership, and a datum that
represents **that** family, with its law and positive root mass.  The Arc C hypotheses are inert.

`_hRep` is what makes `Q` a representing datum of `Γ` rather than an unrelated datum carried
alongside it: `QStar Γ` asserts only that *some* datum represents `Γ`, and does not make this `Q`
the witness. -/
theorem availExt_stable_under_arcC {A : Type} [Fintype A] [DecidableEq A]
    (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V) (_hQ : Q.IsLaw)
    (_hQr : Q.PositiveRootMass) (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j)
    {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (h : (permTheory A).availExt n O F) :
    (permTheory A).availExt n O F :=
  h

/-- **S3b, THE UNAVAILABILITY DIRECTION.**  The same for what the stated access does *not* supply:
an unavailable family stays unavailable in the presence of the Arc C layer, with `Q` linked to `Γ`
by `_hRep` as above. -/
theorem availExt_unavailable_stable_under_arcC {A : Type} [Fintype A] [DecidableEq A]
    (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V) (_hQ : Q.IsLaw)
    (_hQr : Q.PositiveRootMass) (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j)
    {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (h : ¬ (permTheory A).availExt n O F) :
    ¬ (permTheory A).availExt n O F :=
  h

/-- **S3b AT THE PHASE RESOURCE.**  The inherited *Additional* disposition of relative-phase
control is unchanged against the Arc C layer.

The verdict itself is **inherited**, from `permTheory_not_phasesAvailable_onesFixing` (PR #515) and
the phase-source adjudication (PR #521).  What this statement adds is only that the Arc C
hypotheses do not disturb it — they appear and are not used, with `Q` linked to `Γ` by `_hRep`. -/
theorem phasesUnavailable_stable_under_arcC {A : Type} [Fintype A] [DecidableEq A]
    (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V) (_hQ : Q.IsLaw)
    (_hQr : Q.PositiveRootMass) (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j)
    (h2 : 2 ≤ Fintype.card A) :
    ¬ PhasesAvailable (permTheory A) :=
  permTheory_not_phasesAvailable_onesFixing h2

/-- The route stated as a class fact rather than as an inert hypothesis: whatever the Arc C layer
contains, the stated access is still exactly `permClass`, and `instAvail_congr` then says the
generated availability is exactly the merged one.  This is the lemma the two statements above are
shorthand for. -/
theorem permClass_unchanged_by_arcC (Γ : ℕ → Matrix V V ℝ) (_hΓ : QStar Γ) (Q : QfbData V)
    (_hQ : Q.IsLaw) (_hQr : Q.PositiveRootMass)
    (_hRep : ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j) :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
      permClass S K ↔ IsScaledPartialPerm K :=
  fun _ _ _ _ => Iff.rfl

end OperationalSourcing

end OIBridge

#print axioms OIBridge.OperationalSourcing.instAvail_congr
#print axioms OIBridge.OperationalSourcing.availExt_congr
#print axioms OIBridge.OperationalSourcing.availExt_stable_under_arcC
#print axioms OIBridge.OperationalSourcing.availExt_unavailable_stable_under_arcC
#print axioms OIBridge.OperationalSourcing.phasesUnavailable_stable_under_arcC
#print axioms OIBridge.OperationalSourcing.permClass_unchanged_by_arcC
