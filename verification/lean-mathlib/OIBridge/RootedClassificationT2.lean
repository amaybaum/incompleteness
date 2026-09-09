import OIBridge.RootedClassification

/-!
# Arc B T2 sufficiency — cycle iteration seam

Temporary development module for the all-time response-table construction.  It is kept separate
while the delicate iteration seam is audited; final packaging imports it directly from the bridge
root and removes the temporary `ScalingFamily` hook.
-/

namespace OIBridge
namespace RootedClassification

open Finset Matrix CausalReadback Equivalence

universe u

variable {V : Type u} [Fintype V] [DecidableEq V]

/-- Iterating the abstract cycle permutation changes only the phase coordinate. -/
theorem cyclePerm_iterate (M t : ℕ) (f : ResponseTable V M) (a : V) (k : Fin M) :
    ((⇑(cyclePerm (V := V) M))^[t]) (f, (a, k)) =
      (f, (a, ((⇑(finRotate M))^[t]) k)) := by
  induction t with
  | zero => rfl
  | succ t ih =>
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih]
      rfl

/-- **THE SAME EMBEDDED CYCLE DRIVES EVERY MICROSCOPIC ITERATE.** This is the induction step the
all-time proof will use; it is not a separate recurrence argument. -/
theorem responseStep_iterate_cycle (M t : ℕ) (c : CycleIndex V M) :
    ((⇑(responseStep (V := V) M))^[t]) (cycleState (V := V) c) =
      cycleState (V := V) (((⇑(cyclePerm (V := V) M))^[t]) c) := by
  induction t with
  | zero => rfl
  | succ t ih =>
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih]
      exact responseStep_cycle _

/-- The actual phase-zero coordinate.  Positivity of the declared period enters here, explicitly,
not in the carrier definitions. -/
def phaseZero (M : ℕ) (hM : 0 < M) : Fin M := ⟨0, hM⟩

@[simp] theorem phaseZero_val (M : ℕ) (hM : 0 < M) : (phaseZero M hM).1 = 0 := rfl

/-- A cycle at phase zero is exactly the microscopic state `(root, table)` on which the common
prior is supported. -/
theorem cycleState_phaseZero (M : ℕ) (hM : 0 < M) (f : ResponseTable V M) (a : V) :
    cycleState (V := V) (f, (a, phaseZero M hM)) = (a, Sum.inl f) :=
  cycleState_val_zero f a _ rfl

/-- Rotating phase zero `t < M` times reaches exactly phase `t`. -/
theorem finRotate_iterate_phaseZero_of_lt (M : ℕ) (hM : 0 < M) (t : ℕ) (ht : t < M) :
    ((⇑(finRotate M))^[t]) (phaseZero M hM) = (⟨t, ht⟩ : Fin M) := by
  letI : NeZero M := ⟨Nat.ne_of_gt hM⟩
  have hz : phaseZero M hM = (0 : Fin M) := by
    apply Fin.ext
    rfl
  rw [hz, ← finCycle_eq_finRotate_iterate (k := (⟨t, ht⟩ : Fin M))]
  simp [finCycle]

/-- The abstract response-table cycle reaches the declared phase throughout the first period. -/
theorem cyclePerm_iterate_phaseZero_of_lt (M : ℕ) (hM : 0 < M)
    (f : ResponseTable V M) (a : V) (t : ℕ) (ht : t < M) :
    ((⇑(cyclePerm (V := V) M))^[t]) (f, (a, phaseZero M hM)) =
      (f, (a, (⟨t, ht⟩ : Fin M))) := by
  rw [cyclePerm_iterate, finRotate_iterate_phaseZero_of_lt M hM t ht]

/-- The total reversible microscopic update has the same first-period trajectory from every
prior-carrying phase-zero table state. -/
theorem responseStep_iterate_phaseZero_of_lt (M : ℕ) (hM : 0 < M)
    (f : ResponseTable V M) (a : V) (t : ℕ) (ht : t < M) :
    ((⇑(responseStep (V := V) M))^[t]) (a, Sum.inl f) =
      cycleState (V := V) (f, (a, (⟨t, ht⟩ : Fin M))) := by
  rw [← cycleState_phaseZero M hM f a, responseStep_iterate_cycle,
    cyclePerm_iterate_phaseZero_of_lt M hM f a t ht]

/-- At a positive first-period time, the visible output is exactly the corresponding response-table
entry. -/
theorem responseStep_visible_of_pos_lt (M : ℕ) (hM : 0 < M)
    (f : ResponseTable V M) (a : V) (t : ℕ) (ht0 : 0 < t) (ht : t < M) :
    (((⇑(responseStep (V := V) M))^[t]) (a, Sum.inl f)).1 =
      f (a, (⟨(⟨t, ht⟩ : Fin M), by simpa using Nat.ne_of_gt ht0⟩ : NonzeroPhase M)) := by
  rw [responseStep_iterate_phaseZero_of_lt M hM f a t ht]
  rw [cycleState_nonzero f a (⟨t, ht⟩ : Fin M) (by simpa using Nat.ne_of_gt ht0)]

end RootedClassification
end OIBridge

#print axioms OIBridge.RootedClassification.cyclePerm_iterate
#print axioms OIBridge.RootedClassification.responseStep_iterate_cycle
#print axioms OIBridge.RootedClassification.finRotate_iterate_phaseZero_of_lt
#print axioms OIBridge.RootedClassification.responseStep_iterate_phaseZero_of_lt
#print axioms OIBridge.RootedClassification.responseStep_visible_of_pos_lt
