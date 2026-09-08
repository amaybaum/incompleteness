import OIBridge.CausalReadback
import OIBridge.Equivalence
import Mathlib.Logic.Equiv.Fintype
import Mathlib.Logic.Equiv.Fin.Rotate

/-!
# Finite-visible intrinsic rooted-family classification

Arc B, task #64.  The visible predicate `PPer`, the inherited-interface necessity direction, and
the common-response-table probability lemma used by the T2 sufficiency construction.

`PPer` is a visible predicate, not a renamed hidden-realizability predicate.  The response-table
lemmas below are finite probability identities: they put any finite collection of categorical
marginals on one common finite seed without assuming rational probabilities.
-/

namespace OIBridge
namespace RootedClassification

open Finset Matrix CausalReadback Equivalence

universe u v

variable {V : Type u} [Fintype V] [DecidableEq V]

/-- **FINITE VISIBLE TEMPORAL PERIODICITY.** -/
def PeriodicFamily (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∃ M : ℕ, 0 < M ∧ ∀ t : ℕ, Γ (t + M) = Γ t

/-- **THE FIRST FALSIFIABLE VISIBLE CLASS `P_per`.** Root identity, row stochasticity at every
 time, and a positive finite visible period. -/
def PPer (Γ : ℕ → Matrix V V ℝ) : Prop :=
  Γ 0 = 1 ∧ (∀ t : ℕ, IsRowStochastic (Γ t)) ∧ PeriodicFamily Γ

/-! ### A common finite response-table prior -/

section ResponsePrior

variable {I : Type v} [Fintype I] [DecidableEq I]

/-- The product weight of one complete response table. -/
def responseWeight (w : I → V → ℝ) (r : I → V) : ℝ :=
  ∏ i : I, w i (r i)

/-- Product response-table weights are nonnegative when every local weight is nonnegative. -/
theorem responseWeight_nonneg {w : I → V → ℝ} (hw : ∀ i j, 0 ≤ w i j) (r : I → V) :
    0 ≤ responseWeight w r := by
  unfold responseWeight
  exact Finset.prod_nonneg fun i _ => hw i (r i)

/-- **ONE COMMON PRIOR.** If every local row sums to one, the product weights on all response
 tables sum to one.  This is the finite product identity `Fintype.prod_sum`; no rationality or
 approximation is used. -/
theorem responseWeight_sum {w : I → V → ℝ} (hsum : ∀ i, ∑ j : V, w i j = 1) :
    ∑ r : I → V, responseWeight w r = 1 := by
  unfold responseWeight
  rw [← Fintype.prod_sum]
  simp [hsum]

/-- **THE COMMON PRIOR HAS THE DECLARED MARGINAL.** Summing product-table weights over all tables
 whose response at one coordinate is `j` gives exactly that coordinate's categorical weight. -/
theorem responseWeight_marginal {w : I → V → ℝ} (hsum : ∀ i, ∑ j : V, w i j = 1)
    (i0 : I) (j0 : V) :
    ∑ r : I → V, (if r i0 = j0 then responseWeight w r else 0) = w i0 j0 := by
  classical
  let w' : I → V → ℝ := fun i j => if i = i0 then (if j = j0 then w i j else 0) else w i j
  calc
    ∑ r : I → V, (if r i0 = j0 then responseWeight w r else 0) =
        ∑ r : I → V, ∏ i : I, w' i (r i) := by
      apply Finset.sum_congr rfl
      intro r _
      by_cases hr : r i0 = j0
      · rw [if_pos hr]
        unfold responseWeight
        rw [Fintype.prod_eq_mul_prod_subtype_ne, Fintype.prod_eq_mul_prod_subtype_ne]
        simp [w', hr]
      · rw [if_neg hr]
        rw [Fintype.prod_eq_mul_prod_subtype_ne]
        simp [w', hr]
    _ = ∏ i : I, ∑ j : V, w' i j := by
      rw [Fintype.prod_sum]
    _ = w i0 j0 := by
      rw [Fintype.prod_eq_mul_prod_subtype_ne]
      simp [w', hsum]

end ResponsePrior

/-! ### T1 necessity -/

/-- **ROOT TIME IS THE IDENTITY.** This uses only the common hidden prior normalization and the
 canonical visible projection. -/
theorem rootedMap_zero {H : Type*} [Fintype H] (R : RootedRealization V H) :
    rootedMap R 0 = (1 : Matrix V V ℝ) := by
  classical
  ext a j
  by_cases h : a = j
  · subst j
    simp [rootedMap, R.prior_sum]
  · simp [rootedMap, Matrix.one_apply, h]

/-- **FINITE REVERSIBILITY FORCES A FINITE VISIBLE PERIOD.** The witness used here is the cardinality
 of the finite permutation group on the microscopic carrier.  It is intentionally coarse and is
 not asserted to be the minimal visible period or the microscopic order. -/
theorem rootedMap_periodic {H : Type*} [Fintype H] (R : RootedRealization V H) :
    PeriodicFamily (fun t => rootedMap R t) := by
  classical
  let M : ℕ := Fintype.card (Equiv.Perm (V × H))
  have hM : 0 < M := by
    dsimp [M]
    exact Fintype.card_pos
  have hpow : R.step ^ M = 1 := by
    dsimp [M]
    exact pow_card_eq_one
  refine ⟨M, hM, ?_⟩
  intro t
  ext a j
  simp only [rootedMap]
  apply Finset.sum_congr rfl
  intro h _
  congr 1
  rw [R.step.iterate_eq_pow, R.step.iterate_eq_pow, pow_add, hpow, mul_one]

/-- **T1 NECESSITY, AT THE MERGED ROOTED INTERFACE.** Every inherited realization on a finite visible
 carrier lies in the visible class `PPer`.  The three conjuncts expose their dependencies: root
 identity from the normalized common prior and canonical projection, row stochasticity from the
 existing rooted-map theorem, and periodicity from finiteness plus reversibility. -/
theorem rootedMap_mem_PPer {H : Type*} [Fintype H] (R : RootedRealization V H) :
    PPer (fun t => rootedMap R t) :=
  ⟨rootedMap_zero R, fun t => rootedMap_isRowStochastic R t, rootedMap_periodic R⟩

/-! ### T2 sufficiency — the reversible response-table cycle

The cycle representation below deliberately does **not** put phase zero into the random response
table.  A table only stores responses at nonzero phases.  Hence phase zero is definitionally the
visible root, rather than a property inferred later from positive support.  The same embedded cycle
therefore drives both reversibility and the eventual all-time agreement proof.
-/

/-- Nonzero phases of a declared visible period, expressed on `Fin.val` so this carrier remains
well-typed even before the positive-period witness is introduced. -/
abbrev NonzeroPhase (M : ℕ) := {k : Fin M // k.1 ≠ 0}

/-- One response-table coordinate: a visible root and a nonzero phase. -/
abbrev ResponseIndex (V : Type u) (M : ℕ) := V × NonzeroPhase M

/-- A complete table of visible responses at all nonzero phases and all roots. -/
abbrev ResponseTable (V : Type u) (M : ℕ) := ResponseIndex V M → V

/-- Zero-prior padding states carry the table, the stored root, and a nonzero phase. -/
abbrev PadIndex (V : Type u) (M : ℕ) := ResponseTable V M × (V × NonzeroPhase M)

/-- The hidden carrier: one phase-zero table state plus root-labelled zero-prior padding states. -/
abbrev ResponseHidden (V : Type u) (M : ℕ) := ResponseTable V M ⊕ PadIndex V M

/-- Abstract cycle coordinates before embedding into the microscopic `V × H` carrier. -/
abbrev CycleIndex (V : Type u) (M : ℕ) := ResponseTable V M × (V × Fin M)

/-- Embed one response-table cycle into the microscopic state space.  A phase whose value is zero
uses the visible root; every nonzero phase remembers that root in the hidden padding label. -/
def cycleState {M : ℕ} (c : CycleIndex V M) : V × ResponseHidden V M :=
  if hk : c.2.2.1 = 0 then
    (c.2.1, Sum.inl c.1)
  else
    (c.1 (c.2.1, ⟨c.2.2, hk⟩), Sum.inr (c.1, (c.2.1, ⟨c.2.2, hk⟩)))

/-- Any phase with value zero is represented by the root/table state. -/
theorem cycleState_val_zero {M : ℕ} (f : ResponseTable V M) (a : V) (k : Fin M)
    (hk : k.1 = 0) :
    cycleState (V := V) (f, (a, k)) = (a, Sum.inl f) := by
  simp [cycleState, hk]

/-- At a nonzero phase, the visible state is exactly the table response at that root/phase. -/
theorem cycleState_nonzero {M : ℕ} (f : ResponseTable V M) (a : V) (k : Fin M)
    (hk : k.1 ≠ 0) :
    cycleState (V := V) (f, (a, k)) =
      (f (a, ⟨k, hk⟩), Sum.inr (f, (a, ⟨k, hk⟩))) := by
  simp [cycleState, hk]

/-- The cycle coordinates are embedded injectively.  This is the exact structural point that
prevents the closing-arrow collision: phase zero records the root in the visible coordinate, while
nonzero phases record it in the hidden padding coordinate. -/
theorem cycleState_injective {M : ℕ} :
    Function.Injective (cycleState (V := V) (M := M)) := by
  intro x y hxy
  rcases x with ⟨f, a, k⟩
  rcases y with ⟨g, b, l⟩
  by_cases hk : k.1 = 0 <;> by_cases hl : l.1 = 0
  · have hkl : k = l := Fin.ext (hk.trans hl.symm)
    subst l
    have hv : a = b := by
      simpa [cycleState, hk] using congrArg Prod.fst hxy
    have hh : f = g := by
      have hs := congrArg Prod.snd hxy
      simpa [cycleState, hk] using hs
    subst b
    subst g
    rfl
  · exfalso
    have hs := congrArg Prod.snd hxy
    simpa [cycleState, hk, hl] using hs
  · exfalso
    have hs := congrArg Prod.snd hxy
    simpa [cycleState, hk, hl] using hs
  · have hs := congrArg Prod.snd hxy
    have hp : (f, (a, ⟨k, hk⟩)) = (g, (b, ⟨l, hl⟩)) := by
      simpa [cycleState, hk, hl] using hs
    have hfg : f = g := congrArg Prod.fst hp
    have habphase : (a, ⟨k, hk⟩) = (b, ⟨l, hl⟩) := congrArg Prod.snd hp
    have hab : a = b := congrArg Prod.fst habphase
    have hphase : (⟨k, hk⟩ : NonzeroPhase M) = ⟨l, hl⟩ := congrArg Prod.snd habphase
    have hkl : k = l := congrArg Subtype.val hphase
    subst g
    subst b
    subst l
    rfl

/-- The corresponding embedding, used to extend the cycle permutation by the identity off-cycle. -/
def cycleEmbedding (M : ℕ) : CycleIndex V M ↪ V × ResponseHidden V M where
  toFun := cycleState
  inj' := cycleState_injective

/-- Rotate only the phase coordinate of a response-table cycle. -/
def cyclePerm (M : ℕ) : Equiv.Perm (CycleIndex V M) :=
  Equiv.prodCongr (Equiv.refl _) (Equiv.prodCongr (Equiv.refl _) (finRotate M))

@[simp] theorem cyclePerm_apply {M : ℕ} (f : ResponseTable V M) (a : V) (k : Fin M) :
    cyclePerm (V := V) M (f, (a, k)) = (f, (a, finRotate M k)) := rfl

/-- **ONE TOTAL REVERSIBLE MICROSCOPIC UPDATE.** Rotate every embedded response-table cycle by one
phase and fix the entire complement.  `viaFintypeEmbedding` supplies a genuine permutation of the
whole product carrier, not merely a partial map on prior-supported states. -/
noncomputable def responseStep (M : ℕ) : Equiv.Perm (V × ResponseHidden V M) :=
  (cyclePerm (V := V) M).viaFintypeEmbedding (cycleEmbedding (V := V) M)

/-- On an embedded cycle the total update is exactly the declared phase rotation. -/
@[simp] theorem responseStep_cycle {M : ℕ} (c : CycleIndex V M) :
    responseStep (V := V) M (cycleState (V := V) c) =
      cycleState (V := V) (cyclePerm (V := V) M c) := by
  simpa [responseStep, cycleEmbedding] using
    (Equiv.Perm.viaFintypeEmbedding_apply_image
      (cyclePerm (V := V) M) (cycleEmbedding (V := V) M) c)

/-! #### The one common prior -/

/-- The categorical weight assigned to a response-table coordinate. -/
def responseLocalWeight (Γ : ℕ → Matrix V V ℝ) {M : ℕ} (i : ResponseIndex V M) (j : V) : ℝ :=
  Γ (i.2.1 : ℕ) i.1 j

/-- Product weight of a complete nonzero-phase response table. -/
def tableWeight (Γ : ℕ → Matrix V V ℝ) {M : ℕ} (f : ResponseTable V M) : ℝ :=
  responseWeight (responseLocalWeight Γ) f

/-- Table weights are nonnegative whenever the target family is row-stochastic. -/
theorem tableWeight_nonneg {Γ : ℕ → Matrix V V ℝ} {M : ℕ}
    (hstoch : ∀ t, IsRowStochastic (Γ t)) (f : ResponseTable V M) :
    0 ≤ tableWeight Γ f := by
  apply responseWeight_nonneg
  intro i j
  exact (hstoch (i.2.1 : ℕ)).1 i.1 j

/-- The table weights sum to one.  This is the product construction that makes one prior serve all
roots and all nonzero phases simultaneously. -/
theorem tableWeight_sum {Γ : ℕ → Matrix V V ℝ} {M : ℕ}
    (hstoch : ∀ t, IsRowStochastic (Γ t)) :
    ∑ f : ResponseTable V M, tableWeight Γ f = 1 := by
  apply responseWeight_sum
  intro i
  exact (hstoch (i.2.1 : ℕ)).2 i.1

/-- The prior lives on the phase-zero table states.  Every padding state has exactly zero mass. -/
def responsePrior (Γ : ℕ → Matrix V V ℝ) {M : ℕ} : ResponseHidden V M → ℝ
  | Sum.inl f => tableWeight Γ f
  | Sum.inr _ => 0

/-- Nonnegativity of the one common prior. -/
theorem responsePrior_nonneg {Γ : ℕ → Matrix V V ℝ} {M : ℕ}
    (hstoch : ∀ t, IsRowStochastic (Γ t)) :
    ∀ h : ResponseHidden V M, 0 ≤ responsePrior Γ h := by
  intro h
  cases h with
  | inl f => exact tableWeight_nonneg hstoch f
  | inr _ => simp [responsePrior]

/-- Normalization of the one common prior. -/
theorem responsePrior_sum {Γ : ℕ → Matrix V V ℝ} {M : ℕ}
    (hstoch : ∀ t, IsRowStochastic (Γ t)) :
    ∑ h : ResponseHidden V M, responsePrior Γ h = 1 := by
  rw [Fintype.sum_sum_type]
  simp only [responsePrior, Finset.sum_const_zero, add_zero]
  exact tableWeight_sum hstoch

/-- The concrete inherited-interface realization attached to a target family and a declared
period.  It uses one total reversible update and one fixed prior shared by every root. -/
noncomputable def responseRealization (Γ : ℕ → Matrix V V ℝ) (M : ℕ)
    (hstoch : ∀ t, IsRowStochastic (Γ t)) : RootedRealization V (ResponseHidden V M) where
  step := responseStep (V := V) M
  prior := responsePrior Γ
  prior_nonneg := responsePrior_nonneg hstoch
  prior_sum := responsePrior_sum hstoch

end RootedClassification
end OIBridge

#print axioms OIBridge.RootedClassification.responseWeight_nonneg
#print axioms OIBridge.RootedClassification.responseWeight_sum
#print axioms OIBridge.RootedClassification.responseWeight_marginal
#print axioms OIBridge.RootedClassification.rootedMap_zero
#print axioms OIBridge.RootedClassification.rootedMap_periodic
#print axioms OIBridge.RootedClassification.rootedMap_mem_PPer
#print axioms OIBridge.RootedClassification.cycleState_injective
#print axioms OIBridge.RootedClassification.responseStep_cycle
#print axioms OIBridge.RootedClassification.tableWeight_nonneg
#print axioms OIBridge.RootedClassification.tableWeight_sum
#print axioms OIBridge.RootedClassification.responsePrior_nonneg
#print axioms OIBridge.RootedClassification.responsePrior_sum
