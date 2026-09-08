import OIBridge.CausalReadback

/-!
# The recurrence-horizon route to rooted P-indivisibility

Targets 1 and 2 of `RECURRENCE-TIGHTNESS-AUDIT.md`, read under
`RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md`, which controls the horizon symbol.

The frozen route runs: a rooted family whose map returns to the identity at some time `n`, together
with a strictly earlier time `s` at which two distinct rooted rows overlap, exhibits a `C4r n`
witness on the pair `(s, n)`; the already-merged `c4r_implies_pIndivisible` then supplies
`PIndivisibleWithin n`. The identity rows of two distinct roots are at total-variation distance
exactly one, while two overlapping probability rows are at distance strictly below one, so the pair
is a strict increase.

The hypotheses are deliberately weaker than the realization-level parent. Only the store clause's
consequence is used — a visible value carrying positive probability under both rooted preparations —
and the write clause, the causal read leg and the rooted-reappearance leg play no part. Section A is
therefore a fact about a family of matrices: it uses neither reversibility, nor a hidden carrier,
nor a prior, and later citations must not attribute it to hypotheses it does not use. Section B
instantiates the same statement on the existing finite rooted realization layer, which supplies the
row-stochasticity that Section A takes as a hypothesis.

Nothing here defines the realization-level readback parent, and nothing here claims a result for any
horizon below `n`: the audit's tightness question is separate and is not touched by this module. No
manuscript condition is renamed and no manuscript is edited.

Total-variation distance is the kernel's existing `HiddenMemory.tv`, and the identity
`tv p q = 1 - ∑ min` proved below is an addition to that existing notion, not a redefinition.
-/

namespace OIBridge
namespace RecurrenceHorizon

open Finset Matrix HiddenMemory CausalReadback

/-! ### Section A — the horizon route, layer-independent

Every result in this section is a fact about a family of matrices. -/

section Abstract

variable {V : Type*} [Fintype V]

/-- **TOTAL VARIATION AS ONE MINUS THE OVERLAP MASS.** For two probability rows the distance is
exactly the mass not shared between them. The pointwise identity is
`|u - v| = u + v - 2 * min u v`, summed against the two normalisations. -/
theorem tv_eq_one_sub_sum_min {p q : V → ℝ} (hp : ∑ j, p j = 1) (hq : ∑ j, q j = 1) :
    tv p q = 1 - ∑ j, min (p j) (q j) := by
  have hpt : ∀ j : V, |p j - q j| = (p j + q j) - 2 * min (p j) (q j) := by
    intro j
    rcases le_total (p j) (q j) with h | h
    · rw [min_eq_left h, abs_of_nonpos (by linarith)]; ring
    · rw [min_eq_right h, abs_of_nonneg (by linarith)]; ring
  have hsum : ∑ j, |p j - q j| = ∑ j, ((p j + q j) - 2 * min (p j) (q j)) :=
    Finset.sum_congr rfl fun j _ => hpt j
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, hp, hq] at hsum
  unfold tv
  rw [hsum]
  ring

/-- **THE OVERLAP BOUND.** A single shared coordinate already caps the distance, because every
overlap term of two nonnegative rows is nonnegative. -/
theorem tv_le_one_sub_min {p q : V → ℝ} (hp0 : ∀ j, 0 ≤ p j) (hq0 : ∀ j, 0 ≤ q j)
    (hp : ∑ j, p j = 1) (hq : ∑ j, q j = 1) (x : V) :
    tv p q ≤ 1 - min (p x) (q x) := by
  rw [tv_eq_one_sub_sum_min hp hq]
  have hle : min (p x) (q x) ≤ ∑ j, min (p j) (q j) :=
    Finset.single_le_sum (f := fun j => min (p j) (q j))
      (fun j _ => le_min (hp0 j) (hq0 j)) (Finset.mem_univ x)
  linarith

/-- **OVERLAPPING ROWS ARE NOT MAXIMALLY DISTINGUISHABLE.** One visible value carrying positive
probability under both rows forces the distance strictly below one. This is the only consequence of
the store clause that the horizon route uses. -/
theorem tv_lt_one_of_overlap {p q : V → ℝ} (hp0 : ∀ j, 0 ≤ p j) (hq0 : ∀ j, 0 ≤ q j)
    (hp : ∑ j, p j = 1) (hq : ∑ j, q j = 1) {x : V} (hpx : 0 < p x) (hqx : 0 < q x) :
    tv p q < 1 := by
  have hb := tv_le_one_sub_min hp0 hq0 hp hq x
  have hpos : 0 < min (p x) (q x) := lt_min hpx hqx
  linarith

variable [DecidableEq V]

/-- **DISTINCT IDENTITY ROWS ARE MAXIMALLY DISTINGUISHABLE.** Two distinct point masses share no
overlap mass at all, so the distance is exactly one. -/
theorem tv_one_rows {a b : V} (hab : a ≠ b) :
    tv ((1 : Matrix V V ℝ) a) ((1 : Matrix V V ℝ) b) = 1 := by
  obtain ⟨hnn, hsum⟩ := one_isRowStochastic (V := V)
  have hmin : ∀ j : V, min ((1 : Matrix V V ℝ) a j) ((1 : Matrix V V ℝ) b j) = 0 := by
    intro j
    rcases eq_or_ne a j with rfl | haj
    · rw [Matrix.one_apply_ne (Ne.symm hab), min_eq_right (hnn a a)]
    · rw [Matrix.one_apply_ne haj, min_eq_left (hnn b j)]
  rw [tv_eq_one_sub_sum_min (hsum a) (hsum b)]
  simp [hmin]

/-- **TARGET 1, AT THE MATRIX LEVEL**: an identity return at `n` together with an overlap at some
strictly earlier `s` is a `C4r n` witness on the pair `(s, n)`.

The overlap caps the earlier distance strictly below one and the identity return puts the later
distance exactly at one, so distinguishability strictly increases. No claim is made for any horizon
below `n`. -/
theorem c4r_of_identity_return_of_overlap {Γ : ℕ → Matrix V V ℝ} {n s : ℕ} (hsn : s < n)
    (hstoch : IsRowStochastic (Γ s)) (hI : Γ n = 1) {a b : V} (hab : a ≠ b) {x : V}
    (hax : 0 < Γ s a x) (hbx : 0 < Γ s b x) :
    C4r n Γ := by
  obtain ⟨hnn, hsum⟩ := hstoch
  refine ⟨a, b, s, n, hab, hsn, le_rfl, ?_⟩
  have hlt : tv (Γ s a) (Γ s b) < 1 :=
    tv_lt_one_of_overlap (fun j => hnn a j) (fun j => hnn b j) (hsum a) (hsum b) hax hbx
  rw [hI, tv_one_rows hab]
  exact hlt

/-- **TARGET 2, AT THE MATRIX LEVEL**: the same hypotheses forbid P-divisibility within `n`.

The second arrow is the already-merged revival no-go, reused rather than reproved; no
stochastic-inverse rigidity lemma is introduced. The conclusion is about the horizon `n` only. -/
theorem pIndivisible_of_identity_return_of_overlap {Γ : ℕ → Matrix V V ℝ} {n s : ℕ} (hsn : s < n)
    (hstoch : IsRowStochastic (Γ s)) (hI : Γ n = 1) {a b : V} (hab : a ≠ b) {x : V}
    (hax : 0 < Γ s a x) (hbx : 0 < Γ s b x) :
    PIndivisibleWithin n Γ :=
  c4r_implies_pIndivisible n Γ
    (c4r_of_identity_return_of_overlap hsn hstoch hI hab hax hbx)

end Abstract

/-! ### Section B — the same statement on the finite rooted realization layer

The realization is used only to supply row-stochasticity; it contributes nothing else. -/

section Layer

variable {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H]

/-- **TARGET 1 ON A ROOTED REALIZATION.** The hypotheses are an identity return of the rooted map at
`n` and an overlap of two distinct rooted rows at some strictly earlier `s`. The realization's
reversibility is not used, and neither the write clause nor either read leg of the frozen parent
appears. -/
theorem c4r_of_rooted_identity_return_of_overlap (R : RootedRealization V H) {n s : ℕ} (hsn : s < n)
    (hI : rootedMap R n = 1) {a b : V} (hab : a ≠ b) {x : V}
    (hax : 0 < rootedMap R s a x) (hbx : 0 < rootedMap R s b x) :
    C4r n (rootedMap R) :=
  c4r_of_identity_return_of_overlap hsn (rootedMap_isRowStochastic R s) hI hab hax hbx

/-- **TARGET 2 ON A ROOTED REALIZATION**: identity return plus a strictly earlier overlap forbids
P-divisibility within that horizon. -/
theorem pIndivisible_of_rooted_identity_return_of_overlap (R : RootedRealization V H) {n s : ℕ}
    (hsn : s < n) (hI : rootedMap R n = 1) {a b : V} (hab : a ≠ b) {x : V}
    (hax : 0 < rootedMap R s a x) (hbx : 0 < rootedMap R s b x) :
    PIndivisibleWithin n (rootedMap R) :=
  pIndivisible_of_identity_return_of_overlap hsn (rootedMap_isRowStochastic R s) hI hab hax hbx

end Layer

/-! ### The recorded horizon verdict

The two targets, stated together at the level actually proved. -/

section Verdict

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- **THE HORIZON VERDICT.** For a rooted family with a stochastic row at `s`, an identity return at
`n > s` and an overlap at `s`: distinguishability revives across `(s, n)`, and P-divisibility fails
within `n`.

What the audit's storage clause supplies is exactly the overlap hypothesis, so the recurrence-scale
obstruction does not require the full causal-readback parent. Nothing here is claimed for a horizon
below `n`. -/
theorem horizon_verdict {Γ : ℕ → Matrix V V ℝ} {n s : ℕ} (hsn : s < n)
    (hstoch : IsRowStochastic (Γ s)) (hI : Γ n = 1) {a b : V} (hab : a ≠ b) {x : V}
    (hax : 0 < Γ s a x) (hbx : 0 < Γ s b x) :
    C4r n Γ ∧ PIndivisibleWithin n Γ :=
  ⟨c4r_of_identity_return_of_overlap hsn hstoch hI hab hax hbx,
    pIndivisible_of_identity_return_of_overlap hsn hstoch hI hab hax hbx⟩

end Verdict

end RecurrenceHorizon
end OIBridge

#print axioms OIBridge.RecurrenceHorizon.tv_eq_one_sub_sum_min
#print axioms OIBridge.RecurrenceHorizon.tv_le_one_sub_min
#print axioms OIBridge.RecurrenceHorizon.tv_lt_one_of_overlap
#print axioms OIBridge.RecurrenceHorizon.tv_one_rows
#print axioms OIBridge.RecurrenceHorizon.c4r_of_identity_return_of_overlap
#print axioms OIBridge.RecurrenceHorizon.pIndivisible_of_identity_return_of_overlap
#print axioms OIBridge.RecurrenceHorizon.c4r_of_rooted_identity_return_of_overlap
#print axioms OIBridge.RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap
#print axioms OIBridge.RecurrenceHorizon.horizon_verdict
