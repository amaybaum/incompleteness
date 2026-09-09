import OIBridge.RootedClassificationT2

/-!
# Arc B T2 sufficiency — all-time agreement

This module completes the response-table realization itself: one-period agreement is proved from
the common product prior, microscopic return after exactly the declared visible period is proved
from the same embedded cycle, and strong induction extends agreement to every time.
-/

namespace OIBridge
namespace RootedClassification

open Finset Matrix CausalReadback Equivalence

universe u

variable {V : Type u} [Fintype V] [DecidableEq V]

/-- One full declared period returns phase zero to itself. -/
theorem finRotate_iterate_phaseZero_period (M : ℕ) (hM : 0 < M) :
    ((⇑(finRotate M))^[M]) (phaseZero M hM) = phaseZero M hM := by
  cases M with
  | zero => exact (Nat.not_lt_zero 0 hM).elim
  | succ n =>
      rw [Function.iterate_succ_apply']
      rw [finRotate_iterate_phaseZero_of_lt (n + 1) hM n (Nat.lt_succ_self n)]
      change finRotate (n + 1) (Fin.last n) = phaseZero (n + 1) hM
      rw [finRotate_last]
      apply Fin.ext
      rfl

/-- The abstract response-table cycle closes after the declared period. -/
theorem cyclePerm_iterate_phaseZero_period (M : ℕ) (hM : 0 < M)
    (f : ResponseTable V M) (a : V) :
    ((⇑(cyclePerm (V := V) M))^[M]) (f, (a, phaseZero M hM)) =
      (f, (a, phaseZero M hM)) := by
  rw [cyclePerm_iterate, finRotate_iterate_phaseZero_period M hM]

/-- **MICROSCOPIC RETURN ON EVERY PRIOR-CARRYING BASE STATE.** This is the same cycle theorem used
for first-period trajectory agreement; no second recurrence argument is introduced. -/
theorem responseStep_iterate_phaseZero_period (M : ℕ) (hM : 0 < M)
    (f : ResponseTable V M) (a : V) :
    ((⇑(responseStep (V := V) M))^[M]) (a, Sum.inl f) = (a, Sum.inl f) := by
  rw [← cycleState_phaseZero M hM f a, responseStep_iterate_cycle,
    cyclePerm_iterate_phaseZero_period M hM f a]

/-- Product-table weights have the required local normalization. -/
theorem responseLocalWeight_sum {Γ : ℕ → Matrix V V ℝ} {M : ℕ}
    (hstoch : ∀ t, IsRowStochastic (Γ t)) :
    ∀ i : ResponseIndex V M, ∑ j : V, responseLocalWeight Γ i j = 1 := by
  intro i
  exact (hstoch (i.2.1 : ℕ)).2 i.1

/-- **THE PADDING HALF CONTRIBUTES NOTHING.** Every `inr` state carries zero prior, so the padding
summand vanishes at every time and every pair of visible values. Both marginal computations below
split the carrier along `Fintype.sum_sum_type` and need this to discard the half that the frozen
interface allows to carry no mass. -/
theorem responseRealization_pad_sum {Γ : ℕ → Matrix V V ℝ} (M : ℕ)
    (hstoch : ∀ t, IsRowStochastic (Γ t)) (s : ℕ) (a j : V) :
    (∑ x : PadIndex V M,
        (if (((⇑(responseRealization (V := V) Γ M hstoch).step)^[s]) (a, Sum.inr x)).1 = j
         then (responseRealization (V := V) Γ M hstoch).prior (Sum.inr x) else 0)) = 0 := by
  refine Finset.sum_eq_zero fun x _ => ?_
  split <;> simp [responseRealization, responsePrior]

/-- **FIRST-PERIOD MARGINAL AGREEMENT.** At every positive `t < M`, summing the common table prior
over responses selected by the microscopic cycle gives exactly `Γ_t`. -/
theorem rootedMap_responseRealization_of_pos_lt {Γ : ℕ → Matrix V V ℝ}
    (M : ℕ) (hM : 0 < M) (hstoch : ∀ t, IsRowStochastic (Γ t))
    (t : ℕ) (ht0 : 0 < t) (ht : t < M) :
    rootedMap (responseRealization (V := V) Γ M hstoch) t = Γ t := by
  classical
  ext a j
  let i0 : ResponseIndex V M :=
    (a, ⟨(⟨t, ht⟩ : Fin M), by simpa using Nat.ne_of_gt ht0⟩)
  calc
    rootedMap (responseRealization (V := V) Γ M hstoch) t a j =
        ∑ f : ResponseTable V M,
          (if (((⇑(responseStep (V := V) M))^[t]) (a, Sum.inl f)).1 = j
           then tableWeight Γ f else 0) := by
      simp only [rootedMap]
      rw [Fintype.sum_sum_type, responseRealization_pad_sum, add_zero]
      simp only [responseRealization, responsePrior]
      rfl
    _ = ∑ f : ResponseTable V M, (if f i0 = j then tableWeight Γ f else 0) := by
      apply Finset.sum_congr rfl
      intro f _
      rw [responseStep_visible_of_pos_lt M hM f a t ht0 ht]
    _ = Γ t a j := by
      simpa [tableWeight, responseLocalWeight, i0] using
        (responseWeight_marginal (V := V)
          (w := responseLocalWeight Γ)
          (responseLocalWeight_sum (V := V) (M := M) hstoch) i0 j)

/-- First-period agreement including `t = 0`; root identity is used only in the zero case. -/
theorem rootedMap_responseRealization_first_period {Γ : ℕ → Matrix V V ℝ}
    (M : ℕ) (hM : 0 < M) (hzero : Γ 0 = 1)
    (hstoch : ∀ t, IsRowStochastic (Γ t)) (t : ℕ) (ht : t < M) :
    rootedMap (responseRealization (V := V) Γ M hstoch) t = Γ t := by
  cases t with
  | zero =>
      rw [hzero]
      exact rootedMap_zero _
  | succ t =>
      exact rootedMap_responseRealization_of_pos_lt M hM hstoch (t + 1)
        (Nat.succ_pos t) ht

/-- **THE CONSTRUCTED ROOTED FAMILY HAS THE DECLARED PERIOD.** Only prior-carrying `inl` states
matter in the sum; every padding state has zero prior.  The period reduction is therefore exactly
the microscopic return theorem above. -/
theorem rootedMap_responseRealization_add_period {Γ : ℕ → Matrix V V ℝ}
    (M : ℕ) (hM : 0 < M) (hstoch : ∀ t, IsRowStochastic (Γ t)) (t : ℕ) :
    rootedMap (responseRealization (V := V) Γ M hstoch) (t + M) =
      rootedMap (responseRealization (V := V) Γ M hstoch) t := by
  classical
  ext a j
  simp only [rootedMap]
  refine Finset.sum_congr rfl fun h _ => ?_
  cases h with
  | inl f =>
      have hret : ((⇑(responseRealization (V := V) Γ M hstoch).step)^[t + M]) (a, Sum.inl f)
          = ((⇑(responseRealization (V := V) Γ M hstoch).step)^[t]) (a, Sum.inl f) := by
        rw [Function.iterate_add_apply]
        show ((⇑(responseStep (V := V) M))^[t]) (((⇑(responseStep (V := V) M))^[M]) (a, Sum.inl f))
            = ((⇑(responseStep (V := V) M))^[t]) (a, Sum.inl f)
        rw [responseStep_iterate_phaseZero_period M hM f a]
      rw [hret]
  | inr x =>
      have h0 : (responseRealization (V := V) Γ M hstoch).prior (Sum.inr x) = 0 := rfl
      rw [h0]
      split <;> split <;> rfl

/-- **ALL-TIME AGREEMENT.** If the target has period `M`, first-period agreement plus the same
microscopic `M`-return extends the one realization to every natural time. -/
theorem responseRealization_agrees_all {Γ : ℕ → Matrix V V ℝ}
    (M : ℕ) (hM : 0 < M) (hzero : Γ 0 = 1)
    (hstoch : ∀ t, IsRowStochastic (Γ t)) (hperiod : ∀ t, Γ (t + M) = Γ t) :
    ∀ t, rootedMap (responseRealization (V := V) Γ M hstoch) t = Γ t := by
  intro t
  induction t using Nat.strong_induction_on with
  | h t ih =>
      by_cases ht : t < M
      · exact rootedMap_responseRealization_first_period M hM hzero hstoch t ht
      · have hMt : M ≤ t := Nat.le_of_not_gt ht
        have htpos : 0 < t := lt_of_lt_of_le hM hMt
        have hslt : t - M < t := Nat.sub_lt htpos hM
        have hdecomp : t - M + M = t := Nat.sub_add_cancel hMt
        calc
          rootedMap (responseRealization (V := V) Γ M hstoch) t =
              rootedMap (responseRealization (V := V) Γ M hstoch) (t - M + M) := by
                rw [hdecomp]
          _ = rootedMap (responseRealization (V := V) Γ M hstoch) (t - M) :=
                rootedMap_responseRealization_add_period M hM hstoch (t - M)
          _ = Γ (t - M) := ih (t - M) hslt
          _ = Γ (t - M + M) := (hperiod (t - M)).symm
          _ = Γ t := by rw [hdecomp]

/-- **T2 SUFFICIENCY, CONSTRUCTIVELY.** Every finite-visible `PPer` family has one concrete finite
hidden carrier, one reversible microscopic update, one common prior, and exact rooted-map agreement
at every time.  The realization is chosen once for the whole family. -/
theorem pper_has_responseRealization {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) :
    ∃ (M : ℕ) (hM : 0 < M),
      ∃ R : RootedRealization V (ResponseHidden V M), ∀ t, rootedMap R t = Γ t := by
  rcases hΓ with ⟨hzero, hstoch, M, hM, hperiod⟩
  refine ⟨M, hM, responseRealization (V := V) Γ M hstoch, ?_⟩
  exact responseRealization_agrees_all M hM hzero hstoch hperiod

/-! ### The classification

One theorem, stating the identification the round was preregistered to obtain. It is assembled from
the two certified directions and adds no mathematics of its own; the point is that the identification
exists as a named result rather than as a reader's inference from two separately typed statements.
-/

/-- **THE FINITE-VISIBLE CLASSIFICATION `C_OI(V) = P_per(V)`.** A complete rooted family over a
finite visible carrier is realizable by the merged inherited interface — some finite hidden carrier,
one reversible update on `V × H`, one prior shared by every visible root, exact agreement at every
time — if and only if it has the identity at the root time, is row-stochastic at every time, and has
a positive finite visible period.

Forward is `pper_of_finiteRootedRealizable`, resting on finiteness of `V × H` and reversibility;
reverse is `pper_has_responseRealization`, which supplies one concrete realization for the whole
family.

**Finite visible carriers only.** `V` carries `Fintype` throughout, and that hypothesis is doing
work rather than decorating the statement: it is what makes the microscopic update a permutation of a
finite set, hence of finite order, hence the visible period that the right-hand side asserts. Over an
infinite visible carrier the update may have infinite order and no period need exist, so this
classifies the finite-visible slice of the interface and nothing beyond it. The inherited
`RootedRealization` itself requires only `Fintype H`. -/
theorem finiteRootedRealizable_iff_pper (Γ : ℕ → Matrix V V ℝ) :
    FiniteRootedRealizable (V := V) Γ ↔ PPer Γ := by
  refine ⟨pper_of_finiteRootedRealizable, fun hΓ => ?_⟩
  obtain ⟨M, _hM, R, hR⟩ := pper_has_responseRealization (V := V) hΓ
  exact ⟨ResponseHidden V M, inferInstance, R, hR⟩

/-- **THE CARRIER UNIVERSE IS NOT A RESTRICTION.** `FiniteRootedRealizable` quantifies its hidden
carrier in `V`'s own universe. Any realization at all, on a finite carrier in any universe, still
yields membership: necessity holds for every universe, and the classification then returns a carrier
in `V`'s. So nothing is lost by the choice, and this is proved rather than assumed. -/
theorem finiteRootedRealizable_of_realization {Γ : ℕ → Matrix V V ℝ} {H : Type*} [Fintype H]
    (R : RootedRealization V H) (hR : ∀ t, rootedMap R t = Γ t) :
    FiniteRootedRealizable (V := V) Γ := by
  have hfun : (fun t => rootedMap R t) = Γ := funext hR
  have hp : PPer Γ := by
    have h := rootedMap_mem_PPer (V := V) R
    rwa [hfun] at h
  exact (finiteRootedRealizable_iff_pper Γ).mpr hp

end RootedClassification
end OIBridge

#print axioms OIBridge.RootedClassification.finRotate_iterate_phaseZero_period
#print axioms OIBridge.RootedClassification.responseStep_iterate_phaseZero_period
#print axioms OIBridge.RootedClassification.rootedMap_responseRealization_of_pos_lt
#print axioms OIBridge.RootedClassification.rootedMap_responseRealization_add_period
#print axioms OIBridge.RootedClassification.responseRealization_agrees_all
#print axioms OIBridge.RootedClassification.pper_has_responseRealization
#print axioms OIBridge.RootedClassification.finiteRootedRealizable_iff_pper
#print axioms OIBridge.RootedClassification.finiteRootedRealizable_of_realization
