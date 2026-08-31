/-
  OIBridge/ControlledQuotient.lean — the interventional quotient: itinerary
  equivalence relative to a finite action menu, and the theorem that closes the
  round-sixteen intervention caveat.

  PHASE THREE, ROUND SEVENTEEN, PART ONE. Round sixteen proved that the minimal
  carrier of the complete PASSIVE observational law is automatically separating, and
  flagged the caveat: passive-itinerary equivalence might cease to be an equivalence
  under interventions. This file replaces the passive quotient by the CONTROLLED
  quotient. For a finite action menu `acts : A → Equiv.Perm S` (the passive step is
  one designated letter), two states are controlled-equivalent when every finite
  action word produces the same visible readout:

      s ∼_ctrl t   ⟺   ∀ w : List A, vis(actWord w s) = vis(actWord w t).

  §A — THE ACTION-WORD MONOID. `actWord` folds a word into a permutation; words
  append contravariantly (`actWord_append`) and single-letter powers are replicates
  (`actWord_replicate`). Because each menu action has finite order, its inverse is
  itself a word, so ∼_ctrl is a congruence in both directions
  (`ctrlRel_evolve`, `ctrlRel_word`, `ctrlRel_symm_evolve`).

  §B — THE CONTROLLED QUOTIENT. `ControlledCarrier = S/∼_ctrl`; every menu action
  descends to a permutation (`ctrlPerm`), the labelling descends (`ctrlVis`), words
  descend (`ctrlWord_mk`), and the quotient is action-separating by construction
  (`controlled_actionSeparating`). `ctrlRel_greatest_congruence`: ∼_ctrl is the
  greatest relation invisible to `vis` and respected by EVERY menu action;
  `controlledMinimal_iff_actionSeparating` is the interventional Nerode minimality.

  §C — CLOSING THE CAVEAT. `ctrlRel_le_itiRelInf`: the controlled relation refines
  the passive relation of every single generator, so the controlled carrier maps
  ONTO the passive carrier (`controlledToPassive_surjective`) — and
  `intervention_separates_passive_fibre` records the caveat exactly: two states glued
  by the passive law but distinguished by one intervention word are equal in the
  passive quotient yet distinct in the controlled quotient. The controlled quotient,
  not the passive one, is the carrier to which an interventional coherent description
  is operationally accountable.

  Probe F30 exercises the 4-cycle countercontrol: the label-symmetric passive carrier
  has two glued fibres, and a single transposition intervention refines the controlled
  classes to singletons.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.PassiveQuotient

namespace OIBridge
namespace ControlledQuotient

open ObservabilityQuotient PassiveQuotient

variable {S I A : Type*} [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I]

/-! ### Section A — the action-word monoid -/

/-- The permutation realized by a finite action word (first letter acts first). -/
def actWord (acts : A → Equiv.Perm S) : List A → Equiv.Perm S
  | [] => 1
  | a :: w => actWord acts w * acts a

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Words compose contravariantly under append. -/
theorem actWord_append (acts : A → Equiv.Perm S) (w w' : List A) :
    actWord acts (w ++ w') = actWord acts w' * actWord acts w := by
  induction w with
  | nil => rw [List.nil_append, actWord, mul_one]
  | cons a w ih =>
      rw [List.cons_append, actWord, actWord, ih, mul_assoc]

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- A constant word is a power of its letter. -/
theorem actWord_replicate (acts : A → Equiv.Perm S) (m : ℕ) (a : A) :
    actWord acts (List.replicate m a) = acts a ^ m := by
  induction m with
  | zero => rw [List.replicate_zero, actWord, pow_zero]
  | succ m ih => rw [List.replicate_succ, actWord, ih, pow_succ]

/-- **The controlled itinerary relation**: agreement of the visible readout under
every finite word of menu actions. -/
def ctrlRel (acts : A → Equiv.Perm S) (vis : S → I) (s t : S) : Prop :=
  ∀ w : List A, vis (actWord acts w s) = vis (actWord acts w t)

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- One forward step of any menu action preserves the relation. -/
theorem ctrlRel_evolve {acts : A → Equiv.Perm S} {vis : S → I} (a : A) {s t : S}
    (h : ctrlRel acts vis s t) : ctrlRel acts vis (acts a s) (acts a t) :=
  fun w => h (a :: w)

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Whole words preserve the relation. -/
theorem ctrlRel_word {acts : A → Equiv.Perm S} {vis : S → I} (w0 : List A) {s t : S}
    (h : ctrlRel acts vis s t) :
    ctrlRel acts vis (actWord acts w0 s) (actWord acts w0 t) := by
  intro w
  have hw := h (w0 ++ w)
  rwa [actWord_append, Equiv.Perm.mul_apply, Equiv.Perm.mul_apply] at hw

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Backward steps too: on a finite carrier every menu action's inverse is itself a
word, so the controlled relation is a two-sided congruence. -/
theorem ctrlRel_symm_evolve {acts : A → Equiv.Perm S} {vis : S → I} (a : A) {s t : S}
    (h : ctrlRel acts vis s t) :
    ctrlRel acts vis ((acts a).symm s) ((acts a).symm t) := by
  have hinv : acts a ^ (orderOf (acts a) - 1) = (acts a)⁻¹ := by
    refine eq_inv_of_mul_eq_one_left ?_
    rw [← pow_succ, Nat.sub_add_cancel (orderOf_pos (acts a)), pow_orderOf_eq_one]
  have h1 := ctrlRel_word (List.replicate (orderOf (acts a) - 1) a) h
  rwa [actWord_replicate, hinv, Equiv.Perm.inv_def] at h1

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **The controlled relation refines the passive relation** of every single menu
generator: whatever the passive law resolves, the controlled law resolves. -/
theorem ctrlRel_le_itiRelInf {acts : A → Equiv.Perm S} {vis : S → I} (a : A)
    {s t : S} (h : ctrlRel acts vis s t) : itiRelInf (acts a) vis s t := by
  intro k
  have hk := h (List.replicate k a)
  rwa [actWord_replicate] at hk

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **THE GREATEST-CONGRUENCE THEOREM, controlled version.** Any relation invisible
to the labelling and respected by every menu action is contained in `∼_ctrl`. -/
theorem ctrlRel_greatest_congruence {acts : A → Equiv.Perm S} {vis : S → I}
    (r : S → S → Prop) (hvis : ∀ s t, r s t → vis s = vis t)
    (hdyn : ∀ a s t, r s t → r (acts a s) (acts a t)) :
    ∀ s t, r s t → ctrlRel acts vis s t := by
  intro s t h w
  induction w generalizing s t with
  | nil => exact hvis s t h
  | cons a w ih => exact ih (acts a s) (acts a t) (hdyn a s t h)

/-! ### Section B — the controlled quotient -/

/-- The controlled itinerary setoid. -/
def ctrlSetoid (acts : A → Equiv.Perm S) (vis : S → I) : Setoid S :=
  ⟨ctrlRel acts vis,
    ⟨fun _ _ => rfl, fun h w => (h w).symm, fun h1 h2 w => (h1 w).trans (h2 w)⟩⟩

/-- **THE CONTROLLED CARRIER**: the interventional quotient `S/∼_ctrl`. -/
abbrev ControlledCarrier (acts : A → Equiv.Perm S) (vis : S → I) : Type _ :=
  Quotient (ctrlSetoid acts vis)

/-- The labelling descends to the controlled quotient. -/
def ctrlVis (acts : A → Equiv.Perm S) (vis : S → I) :
    ControlledCarrier acts vis → I :=
  Quotient.lift vis fun _ _ h => h []

/-- Every menu action descends to a permutation of the controlled carrier. -/
def ctrlPerm (acts : A → Equiv.Perm S) (vis : S → I) (a : A) :
    Equiv.Perm (ControlledCarrier acts vis) where
  toFun := Quotient.lift (fun s => Quotient.mk (ctrlSetoid acts vis) (acts a s))
    fun _ _ h => Quotient.sound (ctrlRel_evolve a h)
  invFun := Quotient.lift
    (fun s => Quotient.mk (ctrlSetoid acts vis) ((acts a).symm s))
    fun _ _ h => Quotient.sound (ctrlRel_symm_evolve a h)
  left_inv := fun q => by
    obtain ⟨s⟩ := q
    show Quotient.mk (ctrlSetoid acts vis) ((acts a).symm (acts a s))
      = Quotient.mk (ctrlSetoid acts vis) s
    rw [Equiv.symm_apply_apply]
  right_inv := fun q => by
    obtain ⟨s⟩ := q
    show Quotient.mk (ctrlSetoid acts vis) (acts a ((acts a).symm s))
      = Quotient.mk (ctrlSetoid acts vis) s
    rw [Equiv.apply_symm_apply]

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Computation rule for descended actions. -/
theorem ctrlPerm_mk (acts : A → Equiv.Perm S) (vis : S → I) (a : A) (s : S) :
    ctrlPerm acts vis a (Quotient.mk (ctrlSetoid acts vis) s)
      = Quotient.mk (ctrlSetoid acts vis) (acts a s) := rfl

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Words of descended actions act as descended words. -/
theorem ctrlWord_mk (acts : A → Equiv.Perm S) (vis : S → I) (w : List A) (s : S) :
    actWord (fun a => ctrlPerm acts vis a) w (Quotient.mk (ctrlSetoid acts vis) s)
      = Quotient.mk (ctrlSetoid acts vis) (actWord acts w s) := by
  induction w generalizing s with
  | nil => rfl
  | cons a w ih =>
      show actWord (fun a => ctrlPerm acts vis a) w
          (ctrlPerm acts vis a (Quotient.mk (ctrlSetoid acts vis) s))
        = Quotient.mk (ctrlSetoid acts vis) (actWord acts w (acts a s))
      rw [ctrlPerm_mk, ih]

/-- **Action separation**: distinct states are distinguished by some action word. -/
def ActionSeparating (acts : A → Equiv.Perm S) (vis : S → I) : Prop :=
  ∀ s t : S, (∀ w : List A, vis (actWord acts w s) = vis (actWord acts w t)) → s = t

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **THE CONTROLLED QUOTIENT IS ACTION-SEPARATING BY CONSTRUCTION.** -/
theorem controlled_actionSeparating (acts : A → Equiv.Perm S) (vis : S → I) :
    ActionSeparating (fun a => ctrlPerm acts vis a) (ctrlVis acts vis) := by
  intro q1 q2
  refine Quotient.inductionOn₂ q1 q2 fun s t h => ?_
  refine Quotient.sound (s := ctrlSetoid acts vis) fun w => ?_
  have hw := h w
  rwa [ctrlWord_mk, ctrlWord_mk] at hw

/-- An observation-preserving congruence for the whole menu. -/
def ActionCongruence (acts : A → Equiv.Perm S) (vis : S → I)
    (r : S → S → Prop) : Prop :=
  (∀ s t, r s t → vis s = vis t) ∧ ∀ a s t, r s t → r (acts a s) (acts a t)

/-- **Controlled minimality**: no nontrivial quotient preserves the complete
interventional visible record. -/
def ControlledMinimal (acts : A → Equiv.Perm S) (vis : S → I) : Prop :=
  ∀ r : S → S → Prop, ActionCongruence acts vis r → ∀ s t, r s t → s = t

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **MINIMALITY IS ACTION SEPARATION.** -/
theorem controlledMinimal_iff_actionSeparating (acts : A → Equiv.Perm S)
    (vis : S → I) : ControlledMinimal acts vis ↔ ActionSeparating acts vis := by
  constructor
  · intro hmin s t hst
    exact hmin (ctrlRel acts vis)
      ⟨fun s t h => h [], fun a _ _ h => ctrlRel_evolve a h⟩ s t hst
  · intro hsep r hr s t hrst
    exact hsep s t (ctrlRel_greatest_congruence r hr.1 hr.2 s t hrst)

/-! ### Section C — closing the intervention caveat -/

/-- The canonical surjection from the controlled carrier onto the passive carrier of
any designated menu generator: the controlled quotient refines the passive one. -/
def controlledToPassive (acts : A → Equiv.Perm S) (vis : S → I) (a0 : A) :
    ControlledCarrier acts vis → MinimalCarrier (acts a0) vis :=
  Quotient.lift (Quotient.mk (itiSetoid (acts a0) vis))
    fun _ _ h => Quotient.sound (s := itiSetoid (acts a0) vis)
      (ctrlRel_le_itiRelInf a0 h)

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- The refinement map is onto: the passive carrier is a quotient of the controlled
carrier, never the other way around. -/
theorem controlledToPassive_surjective (acts : A → Equiv.Perm S) (vis : S → I)
    (a0 : A) : Function.Surjective (controlledToPassive acts vis a0) := by
  intro q
  obtain ⟨s⟩ := q
  exact ⟨Quotient.mk (ctrlSetoid acts vis) s, rfl⟩

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **THE CAVEAT, CLOSED.** Two states glued by the passive law but distinguished by
a single intervention word are equal in the passive quotient yet distinct in the
controlled quotient: the interventional coherent description is accountable to the
controlled carrier, not the passive one. -/
theorem intervention_separates_passive_fibre (acts : A → Equiv.Perm S)
    (vis : S → I) (a0 : A) (W : List A) {s t : S}
    (hpass : itiRelInf (acts a0) vis s t)
    (hW : vis (actWord acts W s) ≠ vis (actWord acts W t)) :
    Quotient.mk (itiSetoid (acts a0) vis) s
        = Quotient.mk (itiSetoid (acts a0) vis) t
      ∧ ¬ctrlRel acts vis s t :=
  ⟨Quotient.sound (s := itiSetoid (acts a0) vis) hpass, fun hc => hW (hc W)⟩

#print axioms actWord_append
#print axioms actWord_replicate
#print axioms ctrlRel_evolve
#print axioms ctrlRel_word
#print axioms ctrlRel_symm_evolve
#print axioms ctrlRel_le_itiRelInf
#print axioms ctrlRel_greatest_congruence
#print axioms ctrlPerm_mk
#print axioms ctrlWord_mk
#print axioms controlled_actionSeparating
#print axioms controlledMinimal_iff_actionSeparating
#print axioms controlledToPassive_surjective
#print axioms intervention_separates_passive_fibre

end ControlledQuotient
end OIBridge
