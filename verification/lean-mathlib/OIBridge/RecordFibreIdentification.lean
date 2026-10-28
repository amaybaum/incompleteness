import OIBridge.ObservabilityQuotient

/-!
# Known-model record fibres: the set-theoretic core of Substratum P24.5(i)

An exact retained record determines a quantity when that quantity has one value
on its nonempty preparation-supported fibre. This module constructs the value
and proves the state/current-hidden criteria for actual powers of a permutation.
Words have length `n + 1`, so the last visible readout is present.

This does not formalize the Bayesian support calculation, the N-1 partition
refinement bound, unknown-model reconstruction, physical storage/interventions,
or P24.5 as a whole. No capacity/opacity implication is assumed.
-/

namespace OIBridge.RecordFibreIdentification

variable {S V H Q W : Type*}

/-- A finite word of passive readouts, including the time-zero readout. -/
def record (φ : Equiv.Perm S) (r : S → V) (k : ℕ) (s : S) : Fin k → V :=
  fun j => r ((φ ^ j.val) s)

/-- The preparation-supported fibre of the exact retained word. -/
def recordFibre (φ : Equiv.Perm S) (r : S → V) (A : Set S)
    (k : ℕ) (w : Fin k → V) : Set S :=
  {s | s ∈ A ∧ record φ r k s = w}

/-- A quantity has one determined value on the specified compatible-state set. -/
def Determined (F : Set S) (q : S → Q) : Prop :=
  ∃ value : Q, ∀ s ∈ F, q s = value

/-- Nonemptiness is the precise set-theoretic consequence needed from a
positive-probability record on the preparation support. -/
theorem determined_iff_constant {F : Set S} (hne : F.Nonempty) (q : S → Q) :
    Determined F q ↔ ∀ s ∈ F, ∀ t ∈ F, q s = q t := by
  constructor
  · rintro ⟨value, hvalue⟩ s hs t ht
    exact (hvalue s hs).trans (hvalue t ht).symm
  · intro h
    rcases hne with ⟨s, hs⟩
    exact ⟨q s, fun t ht => h t ht s hs⟩

/-- The actual initial state is determined exactly on a nonempty singleton
fibre, expressed without a cardinality convention for infinite carriers. -/
theorem initial_determined_iff_subsingleton {F : Set S} (hne : F.Nonempty) :
    Determined F (fun s => s) ↔ F.Subsingleton := by
  rw [determined_iff_constant hne]
  rfl

/-- Transport by an injective map does not erase compatible distinctions. -/
theorem determined_injective_iff {F : Set S} (hne : F.Nonempty)
    (f : S → Q) (hf : Function.Injective f) :
    Determined F f ↔ F.Subsingleton := by
  rw [determined_iff_constant hne]
  constructor
  · intro h s hs t ht
    exact hf (h s hs t ht)
  · intro h s hs t ht
    exact congrArg f (h hs ht)

/-- Invertibility is used on the actual microscopic current-state map. -/
theorem current_determined_iff {F : Set S} (hne : F.Nonempty)
    (φ : Equiv.Perm S) (n : ℕ) :
    Determined F (fun s => (φ ^ n) s) ↔ F.Subsingleton :=
  determined_injective_iff hne (φ ^ n) (φ ^ n).injective

/-- Equal nonempty visible records fix the current visible coordinate. -/
theorem current_visible_eq (φ : Equiv.Perm (V × H)) (n : ℕ)
    {s t : V × H} (h : record φ Prod.fst (n + 1) s = record φ Prod.fst (n + 1) t) :
    ((φ ^ n) s).1 = ((φ ^ n) t).1 := by
  have hlast := congrFun h ⟨n, Nat.lt_succ_self n⟩
  simpa only [record] using hlast

/-- For a product carrier and its visible projection, the last retained
readout plus the current hidden coordinate fixes the entire current state.
Permutation injectivity transports this back to the initial state. -/
theorem current_hidden_determined_iff (φ : Equiv.Perm (V × H))
    (A : Set (V × H)) (n : ℕ) (w : Fin (n + 1) → V)
    (hne : (recordFibre φ Prod.fst A (n + 1) w).Nonempty) :
    Determined (recordFibre φ Prod.fst A (n + 1) w) (fun s => ((φ ^ n) s).2) ↔
      (recordFibre φ Prod.fst A (n + 1) w).Subsingleton := by
  rw [determined_iff_constant hne]
  constructor
  · intro h s hs t ht
    have hrecord : record φ Prod.fst (n + 1) s = record φ Prod.fst (n + 1) t :=
      hs.2.trans ht.2.symm
    apply (φ ^ n).injective
    exact Prod.ext (current_visible_eq φ n hrecord) (h s hs t ht)
  · intro h s hs t ht
    exact congrArg (fun u => ((φ ^ n) u).2) (h hs ht)

/-- A proper instantaneous readout can identify the entire initial state
through two retained records: the arbitrary-alphabet swap example. -/
theorem swap_two_records_injective :
    Function.Injective (record (Equiv.prodComm V V) Prod.fst 2) := by
  intro s t h
  apply Prod.ext
  · have hzero := congrFun h ⟨0, by decide⟩
    simpa [record] using hzero
  · have hone := congrFun h ⟨1, by decide⟩
    simpa [record] using hone

/-- The empty word cannot identify even the two visible Boolean states.
This protects the nonempty-record hypothesis of the hidden-state criterion. -/
theorem empty_record_counterexample :
    ∃ s t : Bool × Bool, s ≠ t ∧
      record (Equiv.prodComm Bool Bool) Prod.fst 0 s =
        record (Equiv.prodComm Bool Bool) Prod.fst 0 t := by
  refine ⟨(false, false), (true, false), ?_, ?_⟩
  · intro h
    have hfst := congrArg Prod.fst h
    cases hfst
  · funext j
    exact Fin.elim0 j

#print axioms determined_iff_constant
#print axioms initial_determined_iff_subsingleton
#print axioms determined_injective_iff
#print axioms current_determined_iff
#print axioms current_visible_eq
#print axioms current_hidden_determined_iff
#print axioms swap_two_records_injective
#print axioms empty_record_counterexample

end OIBridge.RecordFibreIdentification
