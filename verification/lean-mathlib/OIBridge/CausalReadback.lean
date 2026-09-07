import OIBridge.StochasticInterface
import OIBridge.HiddenMemory

/-!
# The C4 causal-readback audit — do the candidate readback forms forbid stochastic divisibility?

The preregistered pass of `C4-CAUSAL-READBACK-AUDIT.md`, read under
`C4-CAUSAL-READBACK-AUDIT-AMENDMENT.md`, which controls where the two conflict.

`C4e` and `C4r` are candidate causal-readback forms on rooted one-time visible marginals. They are
not asserted to strengthen, imply, or be implied by the manuscript's history-level condition; that
relationship is reported in the note, not claimed here. Nothing is named "C5"; no fifth condition is
defined; no correspondence theorem is stated, cited as a premise, or used, and no predicate for one
is defined; the manuscript's own condition is not renamed and no manuscript is edited.

The composition convention is frozen by the amendment: rows are indexed by the rooted preparation,
columns by the visible outcome, and a stochastic propagator acts on the outcome index by RIGHT
multiplication, `Γ t = Γ s * Λ`. Left multiplication mixes over the root index and is not the
divisibility notion audited here.

Total-variation distance is the kernel's existing `HiddenMemory.tv`, not a new definition; the
three elementary facts about it proved below are additions to that existing notion. The kernel's
`tv_marg_le` covers deterministic channels only, so the stochastic-propagator contraction is new.

Section A is layer-independent: every result in it is a fact about a family of matrices, using
neither reversibility, nor a hidden carrier, nor a prior. Only Section B uses the finite
visible/hidden realization, and it uses it solely to construct rooted maps and prove them
stochastic. Later citations must not attribute Section A to hypotheses it does not use.
-/

namespace OIBridge
namespace CausalReadback

open Finset Matrix HiddenMemory

/-! ### Section A — rooted families, divisibility, and the two no-go routes

Layer-independent throughout. -/

section Abstract

variable {V : Type*} [Fintype V]

/-- **ROW-STOCHASTIC**: nonnegative entries, every row summing to one. -/
def IsRowStochastic (M : Matrix V V ℝ) : Prop :=
  (∀ i j, 0 ≤ M i j) ∧ ∀ i, ∑ j, M i j = 1

/-- **P-DIVISIBILITY WITHIN A HORIZON**, at the rooted-map level and in the frozen orientation:
every later rooted map factors through every earlier one by a row-stochastic propagator acting on
the outcome index. -/
def PDivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∀ s t : ℕ, s < t → t ≤ K → ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ

/-- **P-INDIVISIBILITY WITHIN A HORIZON**: the negation. Some pair admits no such propagator. -/
def PIndivisibleWithin (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ¬ PDivisible K Γ

/-- **C4e, EXACT CAUSAL READBACK**: two distinct rooted preparations whose one-time visible
marginals coincide at some time and differ at a later time within the horizon. -/
def C4e (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∃ (a b : V) (s t : ℕ), a ≠ b ∧ s < t ∧ t ≤ K ∧ Γ s a = Γ s b ∧ Γ t a ≠ Γ t b

/-- **C4r, QUANTITATIVE ROOTED REVIVAL**: visible distinguishability of two rooted preparations
strictly increases across some pair of times within the horizon. -/
def C4r (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∃ (a b : V) (s t : ℕ), a ≠ b ∧ s < t ∧ t ≤ K ∧ tv (Γ s a) (Γ s b) < tv (Γ t a) (Γ t b)

/-- **TOTAL VARIATION IS NONNEGATIVE.** -/
theorem tv_nonneg (p q : V → ℝ) : 0 ≤ tv p q := by
  unfold tv
  positivity

/-- **TOTAL VARIATION VANISHES EXACTLY ON EQUAL ROWS.** -/
theorem tv_eq_zero_iff (p q : V → ℝ) : tv p q = 0 ↔ p = q := by
  constructor
  · intro h
    have hs : ∑ j, |p j - q j| = 0 := by
      unfold tv at h
      linarith [h]
    funext j
    have hj := (Finset.sum_eq_zero_iff_of_nonneg
      (fun i (_ : i ∈ Finset.univ) => abs_nonneg (p i - q i))).mp hs j (Finset.mem_univ j)
    have := abs_eq_zero.mp hj
    linarith
  · rintro rfl
    simp [tv]

/-- **DISTINCT ROWS ARE AT POSITIVE TOTAL-VARIATION DISTANCE.** -/
theorem tv_pos_of_ne {p q : V → ℝ} (h : p ≠ q) : 0 < tv p q :=
  lt_of_le_of_ne (tv_nonneg p q) (fun hz => h ((tv_eq_zero_iff p q).mp hz.symm))

/-- **DATA PROCESSING**: right multiplication by a row-stochastic propagator cannot increase the
total-variation distance between two rows. This is the contractivity route's only analytic input. -/
theorem tv_mul_le {Λ : Matrix V V ℝ} (hΛ : IsRowStochastic Λ) (p q : V → ℝ) :
    tv (fun j => ∑ i, p i * Λ i j) (fun j => ∑ i, q i * Λ i j) ≤ tv p q := by
  have key : ∑ j, |(∑ i, p i * Λ i j) - ∑ i, q i * Λ i j| ≤ ∑ i, |p i - q i| := by
    have step1 : ∀ j : V, |(∑ i, p i * Λ i j) - ∑ i, q i * Λ i j| ≤ ∑ i, |p i - q i| * Λ i j := by
      intro j
      have hrw : (∑ i, p i * Λ i j) - ∑ i, q i * Λ i j = ∑ i, (p i - q i) * Λ i j := by
        rw [← Finset.sum_sub_distrib]
        exact Finset.sum_congr rfl fun i _ => by ring
      rw [hrw]
      refine (Finset.abs_sum_le_sum_abs _ _).trans (le_of_eq ?_)
      exact Finset.sum_congr rfl fun i _ => by
        rw [abs_mul, abs_of_nonneg (hΛ.1 i j)]
    refine (Finset.sum_le_sum fun j _ => step1 j).trans (le_of_eq ?_)
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.mul_sum, hΛ.2 i, mul_one]
  unfold tv
  linarith [key]

/-- **THE EXACT OBSTRUCTION**: equal rows survive right multiplication. If two rooted rows agree at
`s`, they agree at `t` under any factorization through `Γ s` — stochasticity of the propagator is
not needed, so this route is independent of the total-variation route. -/
theorem rows_eq_of_factor {Γs Γt Λ : Matrix V V ℝ} (hfac : Γt = Γs * Λ) {a b : V}
    (hrow : Γs a = Γs b) : Γt a = Γt b := by
  funext j
  rw [hfac, Matrix.mul_apply, Matrix.mul_apply]
  exact Finset.sum_congr rfl fun k _ => by rw [congrFun hrow k]

/-- **C4e IMPLIES C4r**: distinguishability is zero at the collision time and positive at the
separation time, so it strictly increases. -/
theorem c4e_implies_c4r (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : C4e K Γ) : C4r K Γ := by
  obtain ⟨a, b, s, t, hab, hst, htK, hcol, hsep⟩ := h
  refine ⟨a, b, s, t, hab, hst, htK, ?_⟩
  rw [(tv_eq_zero_iff (Γ s a) (Γ s b)).mpr hcol]
  exact tv_pos_of_ne hsep

/-- **THE REVIVAL NO-GO**: strictly increasing rooted distinguishability forbids P-divisibility
within the horizon. Proved through the contraction, and not through the row obstruction. -/
theorem c4r_implies_pIndivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : C4r K Γ) :
    PIndivisibleWithin K Γ := by
  obtain ⟨a, b, s, t, -, hst, htK, hgrow⟩ := h
  intro hdiv
  obtain ⟨Λ, hΛ, hfac⟩ := hdiv s t hst htK
  have hrow : ∀ c : V, Γ t c = fun j => ∑ i, Γ s c i * Λ i j := by
    intro c
    funext j
    rw [hfac, Matrix.mul_apply]
  rw [hrow a, hrow b] at hgrow
  exact absurd (tv_mul_le hΛ (Γ s a) (Γ s b)) (not_le.mpr hgrow)

/-- **THE EXACT-READBACK NO-GO, BY THE ROW OBSTRUCTION**: a collision followed by a separation
forbids P-divisibility directly, with no metric and no stochasticity used. -/
theorem c4e_implies_pIndivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : C4e K Γ) :
    PIndivisibleWithin K Γ := by
  obtain ⟨a, b, s, t, -, hst, htK, hcol, hsep⟩ := h
  intro hdiv
  obtain ⟨Λ, -, hfac⟩ := hdiv s t hst htK
  exact hsep (rows_eq_of_factor hfac hcol)

/-- **THE EXACT-READBACK NO-GO, BY THE CONTRACTION**: the same conclusion reached through `C4r`,
so the headline result does not rest on a single formalization of distinguishability. -/
theorem c4e_implies_pIndivisible_via_c4r (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : C4e K Γ) :
    PIndivisibleWithin K Γ :=
  c4r_implies_pIndivisible K Γ (c4e_implies_c4r K Γ h)

/-- **A P-DIVISIBLE FAMILY EXHIBITS NEITHER CANDIDATE**, the contrapositive used by the controls. -/
theorem not_c4e_and_not_c4r_of_pDivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : PDivisible K Γ) :
    ¬ C4e K Γ ∧ ¬ C4r K Γ :=
  ⟨fun hc => c4e_implies_pIndivisible K Γ hc h, fun hc => c4r_implies_pIndivisible K Γ hc h⟩

end Abstract

/-! ### Section B — the finite visible/hidden realization layer

Used only to construct rooted maps and prove them stochastic. -/

section Layer

/-- **A FINITE ROOTED REVERSIBLE REALIZATION**: a deterministic reversible total update on `V × H` and
one fixed hidden prior, common to every rooted visible preparation. This is not the kernel's
`HiddenMemory.Realization`, which carries a joint law over histories for a different theorem; the
two are kept apart deliberately. -/
structure RootedRealization (V H : Type*) [Fintype H] where
  /-- The deterministic reversible total update. -/
  step : V × H ≃ V × H
  /-- The fixed hidden prior, shared by every root. -/
  prior : H → ℝ
  /-- The prior is nonnegative. -/
  prior_nonneg : ∀ h, 0 ≤ prior h
  /-- The prior is normalized. -/
  prior_sum : ∑ h, prior h = 1

/-- **THE ROOTED VISIBLE MAP AT TIME `t`**: draw the hidden state from the fixed prior, evolve the
pair for `t` steps, and project to the visible carrier. -/
noncomputable def rootedMap {V H : Type*} [DecidableEq V] [Fintype H]
    (R : RootedRealization V H) (t : ℕ) : Matrix V V ℝ :=
  fun a j => ∑ h : H, if ((⇑R.step)^[t] (a, h)).1 = j then R.prior h else 0

/-- **THE ROOTED MAPS ARE STOCHASTIC.** This is the round's only use of the realization layer; the
no-go theorems of Section A use none of it. -/
theorem rootedMap_isRowStochastic {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H]
    (R : RootedRealization V H) (t : ℕ) : IsRowStochastic (rootedMap R t) := by
  refine ⟨fun a j => ?_, fun a => ?_⟩
  · show (0 : ℝ) ≤ ∑ h : H, if ((⇑R.step)^[t] (a, h)).1 = j then R.prior h else 0
    refine Finset.sum_nonneg fun h _ => ?_
    split
    · exact R.prior_nonneg h
    · exact le_refl 0
  · show (∑ j : V, ∑ h : H, if ((⇑R.step)^[t] (a, h)).1 = j then R.prior h else 0) = 1
    rw [Finset.sum_comm]
    simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
    exact R.prior_sum

end Layer

/-! ### Section C — the frozen controls on the two-valued carrier -/

section Controls

/-- The fully mixing rooted map on two visible values. -/
noncomputable def J2 : Matrix (Fin 2) (Fin 2) ℝ := fun _ _ => 1 / 2

/-- **N1, THE NEGATIVE CONTROL**: the rooted family of the exclusive-or law, identity at the root
time and fully mixing thereafter. Its history-level memory is maximal, which the exact probe
certifies numerically and this module does not restate. -/
noncomputable def pdFamily : ℕ → Matrix (Fin 2) (Fin 2) ℝ
  | 0 => 1
  | _ + 1 => J2

/-- **P1, THE POSITIVE CONTROL**: the delayed-revival family, identity except at the collision time,
where it is fully mixing. -/
noncomputable def peFamily : ℕ → Matrix (Fin 2) (Fin 2) ℝ
  | 2 => J2
  | _ => 1

/-- **THE MIXING MAP IS STOCHASTIC.** -/
theorem j2_isRowStochastic : IsRowStochastic J2 :=
  ⟨fun _ _ => by norm_num [J2], fun _ => by simp [J2]⟩

/-- **THE IDENTITY IS STOCHASTIC.** -/
theorem one_isRowStochastic {V : Type*} [Fintype V] [DecidableEq V] :
    IsRowStochastic (1 : Matrix V V ℝ) := by
  refine ⟨fun i j => ?_, fun i => ?_⟩
  · rw [Matrix.one_apply]
    split <;> norm_num
  · simp [Matrix.one_apply]

/-- **THE MIXING MAP HAS EQUAL ROWS.** -/
theorem j2_rows_eq (a b : Fin 2) : J2 a = J2 b := rfl

/-- **THE IDENTITY HAS DISTINCT ROWS AT DISTINCT ROOTS.** -/
theorem one_rows_ne {a b : Fin 2} (hab : a ≠ b) :
    (1 : Matrix (Fin 2) (Fin 2) ℝ) a ≠ (1 : Matrix (Fin 2) (Fin 2) ℝ) b := by
  intro h
  have := congrFun h a
  rw [Matrix.one_apply_eq, Matrix.one_apply_ne (Ne.symm hab)] at this
  exact one_ne_zero this

/-- **N1 IS P-DIVISIBLE AT EVERY HORIZON**: the identity witnesses every mixing-to-mixing step and
the mixing map itself witnesses every step out of the root. -/
theorem pdFamily_pDivisible (K : ℕ) : PDivisible K pdFamily := by
  intro s t hst _
  cases s with
  | zero =>
    cases t with
    | zero => omega
    | succ n =>
      refine ⟨J2, j2_isRowStochastic, ?_⟩
      show J2 = (1 : Matrix (Fin 2) (Fin 2) ℝ) * J2
      rw [one_mul]
  | succ m =>
    cases t with
    | zero => omega
    | succ n =>
      refine ⟨1, one_isRowStochastic, ?_⟩
      show J2 = J2 * (1 : Matrix (Fin 2) (Fin 2) ℝ)
      rw [mul_one]

/-- **N1 EXHIBITS NEITHER CANDIDATE.** The negative control stands: a family may carry maximal
history-level memory and still be P-divisible, so that memory alone does not deliver the no-go. -/
theorem pdFamily_not_c4e_not_c4r (K : ℕ) : ¬ C4e K pdFamily ∧ ¬ C4r K pdFamily :=
  not_c4e_and_not_c4r_of_pDivisible K pdFamily (pdFamily_pDivisible K)

/-- **P1 EXHIBITS EXACT CAUSAL READBACK**: the rooted rows collide at the mixing time and separate
one step later. -/
theorem peFamily_c4e : C4e 3 peFamily := by
  refine ⟨0, 1, 2, 3, by decide, by norm_num, by norm_num, ?_, ?_⟩
  · show J2 0 = J2 1
    rfl
  · show (1 : Matrix (Fin 2) (Fin 2) ℝ) 0 ≠ (1 : Matrix (Fin 2) (Fin 2) ℝ) 1
    exact one_rows_ne (by decide)

/-- **P1 IS P-INDIVISIBLE**, by both routes. -/
theorem peFamily_pIndivisible : PIndivisibleWithin 3 peFamily :=
  c4e_implies_pIndivisible 3 peFamily peFamily_c4e

/-- **THE WEAK/STRONG SEPARATION AT THE MARGINAL LEVEL**: one family is P-divisible and exhibits
neither candidate, the other exhibits exact readback and is P-indivisible. The history-level memory
of the first is certified by the exact probe and is not restated here. -/
theorem control_separation :
    (PDivisible 3 pdFamily ∧ ¬ C4e 3 pdFamily ∧ ¬ C4r 3 pdFamily) ∧
      (C4e 3 peFamily ∧ PIndivisibleWithin 3 peFamily) :=
  ⟨⟨pdFamily_pDivisible 3, (pdFamily_not_c4e_not_c4r 3).1, (pdFamily_not_c4e_not_c4r 3).2⟩,
    ⟨peFamily_c4e, peFamily_pIndivisible⟩⟩

end Controls

/-! ### Section D — the verdict -/

section Verdict

variable {V : Type*} [Fintype V]

/-- **THE MATHEMATICAL VERDICT**: the frozen chain, with the two routes to the endpoint kept apart.

Nothing here says that either candidate is necessary for P-indivisibility, that either is implied by
or implies the manuscript's history-level condition, that the architecture supplies either, or that
marginal revival by itself exhibits a causal hidden write-then-read mechanism. -/
theorem causal_readback_verdict (K : ℕ) (Γ : ℕ → Matrix V V ℝ) :
    (C4e K Γ → C4r K Γ) ∧ (C4r K Γ → PIndivisibleWithin K Γ) ∧
      (C4e K Γ → PIndivisibleWithin K Γ) :=
  ⟨c4e_implies_c4r K Γ, c4r_implies_pIndivisible K Γ, c4e_implies_pIndivisible K Γ⟩

end Verdict

end CausalReadback
end OIBridge

#print axioms OIBridge.CausalReadback.tv_nonneg
#print axioms OIBridge.CausalReadback.tv_eq_zero_iff
#print axioms OIBridge.CausalReadback.tv_pos_of_ne
#print axioms OIBridge.CausalReadback.tv_mul_le
#print axioms OIBridge.CausalReadback.rows_eq_of_factor
#print axioms OIBridge.CausalReadback.c4e_implies_c4r
#print axioms OIBridge.CausalReadback.c4r_implies_pIndivisible
#print axioms OIBridge.CausalReadback.c4e_implies_pIndivisible
#print axioms OIBridge.CausalReadback.c4e_implies_pIndivisible_via_c4r
#print axioms OIBridge.CausalReadback.not_c4e_and_not_c4r_of_pDivisible
#print axioms OIBridge.CausalReadback.rootedMap_isRowStochastic
#print axioms OIBridge.CausalReadback.j2_isRowStochastic
#print axioms OIBridge.CausalReadback.one_isRowStochastic
#print axioms OIBridge.CausalReadback.j2_rows_eq
#print axioms OIBridge.CausalReadback.one_rows_ne
#print axioms OIBridge.CausalReadback.pdFamily_pDivisible
#print axioms OIBridge.CausalReadback.pdFamily_not_c4e_not_c4r
#print axioms OIBridge.CausalReadback.peFamily_c4e
#print axioms OIBridge.CausalReadback.peFamily_pIndivisible
#print axioms OIBridge.CausalReadback.control_separation
#print axioms OIBridge.CausalReadback.causal_readback_verdict
