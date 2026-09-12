import OIBridge.BarandesTuple
import OIBridge.RegionLimit
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Instances.NNReal.Lemmas

/-!
# Act 8 layer 0 — the extension relation (Track I)

The preregistered layer-0 pass of
`programmes/oi-qm/track-b/act-08-continuous-extension/preregistration.md`, frozen at blob
`6517f4dc7b884cb59223a685d5f3a05d4c291e36`.

**THE TRACK SEPARATION IS VISIBLE IN THE DEFINITIONS, NOT PROMISED IN PROSE.** The two definitions
this file introduces — `restrict` and `Extends` — mention no Source A object and no Track B label:
no `Θ`, no dilation, no Stinespring, no unistochasticity. They are statements about a visible
family and a continuous-time family, and they are readable with Source A absent from the room. The
only Track B object used anywhere here is act 6's merged `IsUnistochastic`, and it appears **solely**
in Section D, which answers the freeze's own screening question E0 — a question, not the relation.

## E1 — the relation, with all five returns fixed

* **(a) time domain `ℝ≥0`.** A choice, and recorded as one. The discrete family is `ℕ`-indexed and
  rooted at `0`; extending to negative times would invent structure the visible data does not carry,
  and indexing by `ℝ` while constraining only `0 ≤ t` would make every two families differing below
  zero count as distinct extensions — a non-uniqueness of bookkeeping rather than of content.
* **(b) the embedding `ι : ℕ → ℝ≥0`, `ι n = (n : ℝ≥0)`** — the unit-step cast, written out in
  `restrict` rather than left as "the obvious inclusion". The unit step is a normalisation: a step
  `δ > 0` gives the same relation after rescaling time by `δ`, and nothing below depends on the
  scale.
* **(c) the agreement condition**, `restrict Γhat = Γ`, an equality of `ℕ`-indexed families — so
  agreement holds at every embedded time simultaneously and on the nose.
* **(d) the restriction map**, `restrict`, in the other direction. `restriction_of_extends` proves
  the restriction of an extension of `Γ` is `Γ` itself, with no "up to" anywhere.
* **(e) away from the embedded times: ROW-STOCHASTICITY, AND NOTHING ELSE.** Continuity is **not**
  part of the relation, and neither is differentiability or continuous-time periodicity. This is the
  load-bearing choice of layer 0 and it is a refusal rather than a preference: continuity is exactly
  what Source A's contract was found to want at act 7's `DC2a`, so building it into a Track I
  relation would be letting a Track B need shape the definition. Regularity is carried by separate
  predicates, conjoined where a theorem needs it — entrywise `Continuous` below — and layer 1 is
  where the source's own demands get transcribed.

**Periodicity is asked, not assumed** (E1(e) again). The relation requires no periodicity of `Γhat`.
`PPer` constrains the *restriction*, and `Section C` exhibits an extension that is in fact periodic
in continuous time; that is a property of the witness, not of the relation.

## What the sections prove

* **A** — the two definitions and the E1 bookkeeping: restriction on the nose, agreement at every
  embedded time, the root condition transported, and stochasticity inherited by the restriction.
* **B** — the convexity toolkit, and `cos_nat_mul_pi`, proved by induction from `Real.cos_add`
  rather than by citing a parity lemma.
* **C** — **E2**: the extension is **not determined**. Two entrywise-continuous extensions of one
  lawful `PPer` family agree at every embedded time and differ at `t = 1/2`
  (`extension_not_unique_visible`). This is a **visible-level** separation, which is what makes it
  new: `RegionLimit.continuous_extension_not_unique` separates two flows at the operator level, and
  `regionLimit_analogue_has_equal_visible_shadows` proves in-round that those two flows have the
  **same** entrywise modulus-squared at every time — so that merged theorem exhibits no visible
  non-uniqueness and is an analogy only, exactly as the freeze requires.
* **D** — **E0**, the screening question, answered positively and cheaply, as the freeze predicted.

Nothing here is a construction for `CE1`. The freeze's triviality control states that a rooted
continuous interpolation is expected and is not `CE1`; Section D is that interpolation and is
labelled a screening result wherever it appears.
-/

namespace OIBridge
namespace ContinuousExtension

open Finset Matrix CausalReadback RootedClassification BarandesTupleRound

universe u

variable {V : Type u} [Fintype V] [DecidableEq V]

/-! ### Section A — the relation (E1) -/

/-- **(d) THE RESTRICTION MAP.** The discrete family a continuous-time family restricts to, along
the embedding `ι : ℕ → ℝ≥0`, `ι n = (n : ℝ≥0)` — written out here, which is where E1(b)'s
"explicitly rather than the obvious inclusion" is discharged. -/
def restrict (Γhat : NNReal → Matrix V V ℝ) : ℕ → Matrix V V ℝ := fun n => Γhat (n : NNReal)

/-- **(c) THE EXTENSION RELATION.** `Γhat` extends `Γ` when it is row-stochastic at **every** time
of the domain and its restriction is `Γ` on the nose.

Both conjuncts are E1 returns: the first is (e) — row-stochasticity away from the embedded times,
and nothing else — and the second is (c) together with (d).

**No Source A object and no Track B label appears in this statement**, which is the structural form
of the round's track-separation control: a clause shaped to make a Source-A obligation succeed could
not be written here in this vocabulary. -/
def Extends (Γhat : NNReal → Matrix V V ℝ) (Γ : ℕ → Matrix V V ℝ) : Prop :=
  (∀ t : NNReal, IsRowStochastic (Γhat t)) ∧ restrict Γhat = Γ

omit [DecidableEq V] in
/-- **THE RESTRICTION OF AN EXTENSION IS THE FAMILY ITSELF**, on the nose — E1(d)'s question
answered with an equality rather than an equivalence. -/
theorem restriction_of_extends {Γhat : NNReal → Matrix V V ℝ} {Γ : ℕ → Matrix V V ℝ}
    (h : Extends Γhat Γ) : restrict Γhat = Γ := h.2

omit [DecidableEq V] in
/-- **AGREEMENT AT EVERY EMBEDDED TIME**, the pointwise form of (c). -/
theorem extends_apply {Γhat : NNReal → Matrix V V ℝ} {Γ : ℕ → Matrix V V ℝ}
    (h : Extends Γhat Γ) (n : ℕ) : Γhat (n : NNReal) = Γ n := congrFun h.2 n

/-- **THE ROOT CONDITION TRANSPORTS.** A `PPer` family has `Γ 0 = 1`, so any extension of it is the
identity at time zero. Nothing continuous is used: this is agreement at the single embedded time
`ι 0`. -/
theorem extends_root {Γhat : NNReal → Matrix V V ℝ} {Γ : ℕ → Matrix V V ℝ}
    (h : Extends Γhat Γ) (h0 : Γ 0 = 1) : Γhat 0 = 1 := by
  have := extends_apply h 0
  simpa [h0] using this

omit [DecidableEq V] in
/-- **THE RESTRICTION INHERITS STOCHASTICITY** from the extension, so the discrete side of the
relation cannot be lawless while the continuous side is lawful. -/
theorem isRowStochastic_restrict {Γhat : NNReal → Matrix V V ℝ} {Γ : ℕ → Matrix V V ℝ}
    (h : Extends Γhat Γ) (n : ℕ) : IsRowStochastic (Γ n) := by
  rw [← extends_apply h n]; exact h.1 _

/-! ### Section B — the toolkit -/

/-- **THE IDENTITY IS ROW-STOCHASTIC.** -/
theorem isRowStochastic_one : IsRowStochastic (1 : Matrix V V ℝ) := by
  refine ⟨fun i j => ?_, fun i => ?_⟩
  · rw [Matrix.one_apply]; split <;> norm_num
  · simp [Matrix.one_apply, Finset.sum_ite_eq]

omit [DecidableEq V] in
/-- **A CONVEX COMBINATION OF ROW-STOCHASTIC MATRICES IS ROW-STOCHASTIC.** The whole of the
freeze's convexity observation, proved rather than cited: the freeze recorded it as a control on
over-reading and said explicitly that the execution proves or refutes it. -/
theorem isRowStochastic_convex {B C : Matrix V V ℝ} (hB : IsRowStochastic B)
    (hC : IsRowStochastic C) {θ : ℝ} (h0 : 0 ≤ θ) (h1 : θ ≤ 1) :
    IsRowStochastic ((1 - θ) • B + θ • C) := by
  have hentry : ∀ i j, ((1 - θ) • B + θ • C) i j = (1 - θ) * B i j + θ * C i j := by
    intro i j; simp
  constructor
  · intro i j
    rw [hentry i j]
    exact add_nonneg (mul_nonneg (by linarith) (hB.1 i j)) (mul_nonneg h0 (hC.1 i j))
  · intro i
    rw [Finset.sum_congr rfl fun j _ => hentry i j, Finset.sum_add_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, hB.2 i, hC.2 i]
    ring

/-- **`cos (n π) = (-1) ^ n`**, by induction from the addition formula. Proved here rather than
cited so that the agreement claims below rest on nothing outside this file's own arithmetic. -/
theorem cos_nat_mul_pi (n : ℕ) : Real.cos ((n : ℝ) * Real.pi) = (-1 : ℝ) ^ n := by
  have hstep : ∀ x : ℝ, Real.cos (x + Real.pi) = -Real.cos x := by
    intro x; rw [Real.cos_add, Real.cos_pi, Real.sin_pi]; ring
  induction n with
  | zero => simp
  | succ k ih =>
      have hcast : ((k + 1 : ℕ) : ℝ) * Real.pi = (k : ℝ) * Real.pi + Real.pi := by
        push_cast; ring
      rw [hcast, hstep, ih, pow_succ]
      ring

/-- The interpolating weight lies in the unit interval at every time. -/
theorem weight_mem_unitInterval (p : ℝ) (t : NNReal) :
    0 ≤ (1 - Real.cos (p * (t : ℝ))) / 2 ∧ (1 - Real.cos (p * (t : ℝ))) / 2 ≤ 1 := by
  have h1 := Real.neg_one_le_cos (p * (t : ℝ))
  have h2 := Real.cos_le_one (p * (t : ℝ))
  constructor <;> linarith

/-- The interpolating weight is continuous in the time variable. -/
theorem weight_continuous (p : ℝ) :
    Continuous fun t : NNReal => (1 - Real.cos (p * (t : ℝ))) / 2 :=
  ((continuous_const.sub
    (Real.continuous_cos.comp (continuous_const.mul NNReal.continuous_coe))).div_const 2)

/-- **THE HALF-PERIOD WEIGHT AT THE EMBEDDED TIMES**: zero at even steps, one at odd steps. -/
theorem weight_pi_nat (n : ℕ) :
    (1 - Real.cos (Real.pi * (((n : NNReal) : ℝ)))) / 2 = if n % 2 = 0 then 0 else 1 := by
  have hcast : Real.pi * (((n : NNReal) : ℝ)) = (n : ℝ) * Real.pi := by push_cast; ring
  rw [hcast, cos_nat_mul_pi]
  rcases Nat.mod_two_eq_zero_or_one n with h | h
  · rw [if_pos h, Even.neg_one_pow (Nat.even_iff.mpr h)]; norm_num
  · rw [if_neg (by omega), Odd.neg_one_pow (Nat.odd_iff.mpr h)]; norm_num

/-- **THE FULL-PERIOD WEIGHT VANISHES AT EVERY EMBEDDED TIME.** -/
theorem weight_twoPi_nat (n : ℕ) :
    (1 - Real.cos (2 * Real.pi * (((n : NNReal) : ℝ)))) / 2 = 0 := by
  have hcast : 2 * Real.pi * (((n : NNReal) : ℝ)) = ((2 * n : ℕ) : ℝ) * Real.pi := by
    push_cast; ring
  rw [hcast, cos_nat_mul_pi, Even.neg_one_pow ⟨n, by ring⟩]
  norm_num

/-- **AND EQUALS ONE HALF A STEP IN**, which is where the two extensions of Section C separate. -/
theorem weight_twoPi_half :
    (1 - Real.cos (2 * Real.pi * (((1 / 2 : NNReal) : ℝ)))) / 2 = 1 := by
  have hhalf : (((1 / 2 : NNReal) : ℝ)) = 1 / 2 := by norm_num
  have hpi : 2 * Real.pi * (1 / 2 : ℝ) = Real.pi := by ring
  rw [hhalf, hpi, Real.cos_pi]
  norm_num

/-- The convex interpolation between the identity and `A` is row-stochastic at every time. -/
theorem interp_rowStochastic {A : Matrix V V ℝ} (hA : IsRowStochastic A) (p : ℝ) (t : NNReal) :
    IsRowStochastic ((1 - (1 - Real.cos (p * (t : ℝ))) / 2) • (1 : Matrix V V ℝ)
      + ((1 - Real.cos (p * (t : ℝ))) / 2) • A) :=
  isRowStochastic_convex isRowStochastic_one hA (weight_mem_unitInterval p t).1
    (weight_mem_unitInterval p t).2

omit [Fintype V] in
/-- The convex interpolation is entrywise continuous. -/
theorem interp_continuous (A : Matrix V V ℝ) (p : ℝ) (i j : V) :
    Continuous fun t : NNReal => ((1 - (1 - Real.cos (p * (t : ℝ))) / 2) • (1 : Matrix V V ℝ)
      + ((1 - Real.cos (p * (t : ℝ))) / 2) • A) i j := by
  have hfun : (fun t : NNReal => ((1 - (1 - Real.cos (p * (t : ℝ))) / 2) • (1 : Matrix V V ℝ)
        + ((1 - Real.cos (p * (t : ℝ))) / 2) • A) i j)
      = fun t : NNReal => (1 - (1 - Real.cos (p * (t : ℝ))) / 2) * (1 : Matrix V V ℝ) i j
          + ((1 - Real.cos (p * (t : ℝ))) / 2) * A i j := by
    funext t; simp
  rw [hfun]
  exact ((continuous_const.sub (weight_continuous p)).mul continuous_const).add
    ((weight_continuous p).mul continuous_const)

/-! ### Section C — E2: the extension is a SELECTION, not a canonical object -/

/-- **E2 — THE EXTENSION RELATION DOES NOT DETERMINE AN EXTENSION.** For any row-stochastic `A`
other than the identity, the constant identity family — a lawful `PPer` member — has **two**
entrywise-continuous extensions that agree at every embedded time and differ half a step in.

**So OI structure admits a CLASS of extensions, not a unique one, and every extension this round
exhibits is a SELECTION rather than a canonical object.**

**The separation is at the VISIBLE level**, which is what distinguishes it from the merged
operator-level precedent; see `regionLimit_analogue_has_equal_visible_shadows`. -/
theorem extension_not_unique_visible (A : Matrix V V ℝ) (hA : IsRowStochastic A) (hAne : A ≠ 1) :
    ∃ (Γ : ℕ → Matrix V V ℝ) (Γ₁ Γ₂ : NNReal → Matrix V V ℝ),
      PPer Γ ∧ Extends Γ₁ Γ ∧ Extends Γ₂ Γ
        ∧ (∀ i j, Continuous fun t : NNReal => Γ₁ t i j)
        ∧ (∀ i j, Continuous fun t : NNReal => Γ₂ t i j)
        ∧ Γ₁ (1 / 2 : NNReal) ≠ Γ₂ (1 / 2 : NNReal) := by
  classical
  refine ⟨fun _ => 1, fun _ => 1,
    fun t => (1 - (1 - Real.cos (2 * Real.pi * (t : ℝ))) / 2) • (1 : Matrix V V ℝ)
      + ((1 - Real.cos (2 * Real.pi * (t : ℝ))) / 2) • A,
    ⟨rfl, fun _ => isRowStochastic_one, 1, one_pos, fun _ => rfl⟩,
    ⟨fun _ => isRowStochastic_one, rfl⟩,
    ⟨fun t => interp_rowStochastic hA _ t, ?_⟩,
    fun i j => continuous_const, fun i j => interp_continuous A _ i j, ?_⟩
  · funext n
    show (1 - (1 - Real.cos (2 * Real.pi * (((n : NNReal) : ℝ)))) / 2) • (1 : Matrix V V ℝ)
      + ((1 - Real.cos (2 * Real.pi * (((n : NNReal) : ℝ)))) / 2) • A = 1
    rw [weight_twoPi_nat n]; simp
  · show (1 : Matrix V V ℝ)
      ≠ (1 - (1 - Real.cos (2 * Real.pi * (((1 / 2 : NNReal) : ℝ)))) / 2) • (1 : Matrix V V ℝ)
        + ((1 - Real.cos (2 * Real.pi * (((1 / 2 : NNReal) : ℝ)))) / 2) • A
    rw [weight_twoPi_half]
    simpa using fun h => hAne h.symm

/-- **THE MERGED OPERATOR-LEVEL PRECEDENT HAS EQUAL VISIBLE SHADOWS**, which is why the freeze
admits it as analogy and control only.

`RegionLimit.continuous_extension_not_unique` separates the flows of `genZero` and `genTwoPi` at
`t = 1/2`. Their entrywise modulus-squared — the visible shadow — is the identity matrix at every
time, for both. So that theorem exhibits **no** visible non-uniqueness, and the visible separation
of `extension_not_unique_visible` is not a restatement of it. The freeze required this arithmetic to
be proved in-round if the precedent was cited at all; it is proved here. -/
theorem regionLimit_analogue_has_equal_visible_shadows (t : ℝ) (i j : Fin 2) :
    ‖ReachabilitySeam.flow RegionLimit.genZero t i j‖ ^ 2
      = ‖ReachabilitySeam.flow RegionLimit.genTwoPi t i j‖ ^ 2 := by
  rw [RegionLimit.flow_genZero, RegionLimit.flow_genTwoPi]
  by_cases h : i = j
  · subst h
    rw [Matrix.one_apply_eq, Matrix.diagonal_apply_eq]
    by_cases h0 : i = 0
    · rw [if_pos h0]
      have harg : -(t : ℂ) * Complex.I * (2 * (Real.pi : ℂ))
          = ((-(2 * Real.pi * t) : ℝ) : ℂ) * Complex.I := by push_cast; ring
      rw [harg, Complex.norm_exp_ofReal_mul_I]
      norm_num
    · rw [if_neg h0]
  · rw [Matrix.one_apply_ne h, Matrix.diagonal_apply_ne _ h]

/-! ### Section D — E0, the screening question -/

/-- **E0 — THE SCREENING QUESTION, ANSWERED POSITIVELY.** For any row-stochastic `A`, the
period-two alternating family `1, A, 1, A, …` is a lawful `PPer` member, and it has an extension
that is entrywise continuous, is the identity at time zero, and agrees with the family at every
embedded time.

**THIS IS A SCREENING RESULT AND IS NOT `CE1`.** The freeze predicted a positive E0 in advance and
recorded the reason: the row-stochastic matrices form a convex set containing the identity, so
continuous paths from `1` are cheap and a path returning to `1` concatenates to match a periodic
family. `isRowStochastic_convex` is that observation and this theorem is that concatenation, in
closed form. `CE1` additionally requires the whole of the contract layer 1 transcribes and
off-directness at the location E5 fixes — neither of which is touched here. -/
theorem screening_continuous_extension (A : Matrix V V ℝ) (hA : IsRowStochastic A) :
    ∃ (Γ : ℕ → Matrix V V ℝ) (Γhat : NNReal → Matrix V V ℝ),
      PPer Γ ∧ Extends Γhat Γ
        ∧ (∀ i j, Continuous fun t : NNReal => Γhat t i j)
        ∧ Γhat 0 = 1 ∧ Γ 1 = A := by
  classical
  refine ⟨fun n => if n % 2 = 0 then 1 else A,
    fun t => (1 - (1 - Real.cos (Real.pi * (t : ℝ))) / 2) • (1 : Matrix V V ℝ)
      + ((1 - Real.cos (Real.pi * (t : ℝ))) / 2) • A,
    ⟨?_, ?_, 2, by norm_num, ?_⟩,
    ⟨fun t => interp_rowStochastic hA _ t, ?_⟩,
    fun i j => interp_continuous A _ i j, ?_, ?_⟩
  · show (if 0 % 2 = 0 then (1 : Matrix V V ℝ) else A) = 1
    norm_num
  · intro n
    show IsRowStochastic (if n % 2 = 0 then (1 : Matrix V V ℝ) else A)
    split
    · exact isRowStochastic_one
    · exact hA
  · intro t
    show (if (t + 2) % 2 = 0 then (1 : Matrix V V ℝ) else A) = if t % 2 = 0 then 1 else A
    rw [Nat.add_mod_right]
  · funext n
    show (1 - (1 - Real.cos (Real.pi * (((n : NNReal) : ℝ)))) / 2) • (1 : Matrix V V ℝ)
      + ((1 - Real.cos (Real.pi * (((n : NNReal) : ℝ)))) / 2) • A
      = if n % 2 = 0 then 1 else A
    rw [weight_pi_nat n]
    split <;> simp
  · show (1 - (1 - Real.cos (Real.pi * (((0 : NNReal) : ℝ)))) / 2) • (1 : Matrix V V ℝ)
      + ((1 - Real.cos (Real.pi * (((0 : NNReal) : ℝ)))) / 2) • A = 1
    have h0 : (((0 : NNReal) : ℝ)) = 0 := by norm_num
    rw [h0]
    simp
  · show (if 1 % 2 = 0 then (1 : Matrix V V ℝ) else A) = A
    norm_num

/-- **E0's SLICE CLAUSE, AT THE EMBEDDED TIME.** The screening extension of act 6's collapsing
slice is non-unistochastic at `t = 1`, in the external orientation act 2's `RT1` licenses — because
agreement at the embedded time hands the slice over unchanged, and act 6 already refuted it there.

The Track B notion `IsUnistochastic` enters **here and nowhere else** in this file, and it enters a
question rather than a definition: E0 is the freeze's own screening question and asks in those
terms. The two definitions of Section A remain free of it. -/
theorem screening_extension_nonunistochastic_slice :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (Γhat : NNReal → Matrix (Fin 2) (Fin 2) ℝ),
      PPer Γ ∧ Extends Γhat Γ
        ∧ (∀ i j, Continuous fun t : NNReal => Γhat t i j)
        ∧ Γhat 0 = 1
        ∧ ¬ IsUnistochastic (Γhat (1 : NNReal))ᵀ := by
  classical
  have hA : IsRowStochastic
      (Matrix.of (fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ) := by
    constructor
    · intro i j
      show (0 : ℝ) ≤ if j = 0 then (1 : ℝ) else 0
      split <;> norm_num
    · intro i
      show (∑ j : Fin 2, if j = 0 then (1 : ℝ) else 0) = 1
      simp
  obtain ⟨Γ, Γhat, hpper, hext, hcont, hroot, hone⟩ := screening_continuous_extension _ hA
  refine ⟨Γ, Γhat, hpper, hext, hcont, hroot, ?_⟩
  have hslice : Γhat (1 : NNReal) = Matrix.of (fun _ j => if j = 0 then (1 : ℝ) else 0) := by
    have h1 : ((1 : ℕ) : NNReal) = (1 : NNReal) := by norm_num
    rw [← h1, extends_apply hext 1, hone]
  exact collapsed_slice_not_unistochastic hslice

end ContinuousExtension
end OIBridge

/-! ### Axiom report — one line per named result, all eighteen -/

#print axioms OIBridge.ContinuousExtension.restriction_of_extends
#print axioms OIBridge.ContinuousExtension.extends_apply
#print axioms OIBridge.ContinuousExtension.extends_root
#print axioms OIBridge.ContinuousExtension.isRowStochastic_restrict
#print axioms OIBridge.ContinuousExtension.isRowStochastic_one
#print axioms OIBridge.ContinuousExtension.isRowStochastic_convex
#print axioms OIBridge.ContinuousExtension.cos_nat_mul_pi
#print axioms OIBridge.ContinuousExtension.weight_mem_unitInterval
#print axioms OIBridge.ContinuousExtension.weight_continuous
#print axioms OIBridge.ContinuousExtension.weight_pi_nat
#print axioms OIBridge.ContinuousExtension.weight_twoPi_nat
#print axioms OIBridge.ContinuousExtension.weight_twoPi_half
#print axioms OIBridge.ContinuousExtension.interp_rowStochastic
#print axioms OIBridge.ContinuousExtension.interp_continuous
#print axioms OIBridge.ContinuousExtension.extension_not_unique_visible
#print axioms OIBridge.ContinuousExtension.regionLimit_analogue_has_equal_visible_shadows
#print axioms OIBridge.ContinuousExtension.screening_continuous_extension
#print axioms OIBridge.ContinuousExtension.screening_extension_nonunistochastic_slice
