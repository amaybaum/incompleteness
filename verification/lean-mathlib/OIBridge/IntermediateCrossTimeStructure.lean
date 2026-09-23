import OIBridge.GramTrajectorySelection

/-!
# Act 18 — the intermediate regime: what extra structure supplies cross-time information

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/preregistration.md`,
blob `fd3fa1359188966cae006deba4944a14aab5f3dd`, from the merge commit of that control plane,
`d7a9931befeb942db8ebc7b07014f9020c6663d0`, which the freeze fixes as this round's mandated base.

## What this round is

Act 17 established that the admissible Gram trajectories of a visible family are **exactly** the
pointwise realizable assignments, so the admissible set is the **product over time** of the
per-slice realizable sets and every cross-time constraint on the trajectory is additional structure.
Act 13 established that the fibre cross-Gram trajectory determines the lift up to one constant
in-fibre left move and one time-dependent strong right gauge. **The subject here is the interval
between those two poles**, on **two axes that are not ranked against each other**:

* the **`D`-axis** asks whether a **readback datum** — a functional of the lift — can be strictly
  more informative than act 17's visible data, strictly less informative than act 13's level-2
  datum, and still determine the Gram/orbit trajectory;
* the **`L`-axis** asks whether a **structural law** — a constraint writable from `(a₀, Γ)` alone,
  before any lift is chosen — can be genuinely proper and non-trivial, and propagate one time from
  another given an initial orbit.

**The outcome of this round is the ordered pair of those two axis outcomes.** Neither is above the
other, an affirmative on one is not evidence about the other in either direction, and no statement
of this module ranks them.

## What is proved

* `xs1_pointwise_factors` — **`XS1`**: a law that is pointwise in this round's sense has a solution
  set equal to the **product over time** of its per-time solution sets, so an arbitrary time-wise
  recombination of solutions is a solution.
* `xs1_splice` — the splicing corollary. **Act 17's `TJ1` is cited at exactly the step where the
  ambient admissible set has to be a product**: intersecting a product constraint with a
  non-product ambient set need not factor, and it is `tj1_trajectory_set` that proves the ambient
  set **is** the product, so the splice of two admissible solutions stays admissible.
* `xs1_pointwise_not_propagates` — the consequence, routed through `tj1_sufficiency` and
  `tj1_trajectory_set`: **no pointwise law propagates in this round's frozen sense**, at any
  configuration. The two cases of the freeze's argument are closed at once by a single splice.
* `xs2_readback_factors_through_level2` — the well-posedness check, as it stands at execution: the
  anchored readback factors through act 13's level-2 datum, unconditionally, by act 13's
  `fibreCrossGram_diag` and act 12's `fibreGram_diag`.
* `df_bounded_above` — obligation 1 for all three Type D candidates at once, universally and for
  the full pair `D_F = (D₀, F)`; `df1_above_visible`, `df1_below_level2`, `df2_above_visible`,
  `df2_below_level2_and_resid` and `df3_above_visible` — the per-candidate obligations of the
  refinement sandwich this round reaches. **Obligation 3 is stated against act 13's level-2 datum
  and never against the trajectory**: the trajectory phrasing is unsatisfiable exactly when the axis
  succeeds, so writing it that way would make the top line unreachable by construction.
* `lc0_pointwise_law`, `lc2_regularity_law`, `lc3_generator_law` — the Type L candidates this round
  reaches, each with the orbit-level well-definedness obligation, the **one-configuration**
  non-triviality witness carrying all four conjuncts together, and the propagation question with
  **both** frozen clauses reported separately.
* `xs4_d_axis_mid` and `xs5_l_axis_prop` — the two axis outcomes, stated as two theorems and
  reported as an ordered pair.

## What none of this licenses

**THE CLAUSE, carried at this mention — the module docstring's statement of what is not licensed.**
Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
either axis is a statement about the exact structure this freeze names, on the data grant frozen
for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
programme requires it, and **not** an adoption of it as the physical carrier of cross-time
information. A datum that determines the trajectory does not thereby become the right datum, and a
law whose solutions at a configuration are one history is not thereby the law of evolution: the
refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
`L`-axis exist because a structure can reach a top line by containing the answer rather than by
supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
adopted as the physical one, and no candidate changes type during execution.**

**`XS1` is about propagation and not about determination.** The sentence "no pointwise constraint
yields cross-time determination" is **false** and is not said here: a pointwise condition whose
solution set at every time is a single orbit class determines the trajectory outright, slice by
slice, with no initial condition needed. What a pointwise law cannot do is let one time's value
constrain another's. `XS1` is further bounded to the notion of law this round defines — a law datum
written from the anchor, the visible family and the index alone, an orbit-level predicate on
trajectories, pointwise in the frozen sense — and says nothing about `LC1`, `LC2` or `LC3`, which
are not pointwise.

**The candidate lists are closed and are not exhaustive.** Three Type D and four Type L
propositions are frozen for testing; a candidate outside them is neither refuted nor endorsed here.
Each bounded no-go quantifies over its own closed list and over nothing else, and no sentence here
turns one into a general impossibility.

**Nothing here is about the threading, the cross-time representative, the relative evolution or the
relative candidate.** These are invisible to `GramTrajEquiv` by construction, and a round that
cannot see a distinction may not report one, in either direction: act 11's `GL2` pair is **one**
trajectory here. Act 16's cancellation cell and act 15's fork are untouched in either direction, no
carrier of act 14 is read, defined or adopted, and act 10's anchor-axis reclassification is
untouched — the anchor-coherence candidates `DF3` and `LC1` are grounded in it and bear on it in
neither direction. `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`,
`SH1-C1`, `SH1-C2`, `AB0`–`AB2`, `CT1`–`CT4`, `CL1`, `PQ0`–`PQ4`, `CF0`–`CF5`, `RN0`–`RN4` and
`TJ0`–`TJ3` are consumed and none is revised. **Act 13's level-2 result and act 17's `TJ1` and
`TJ3` are consumed at merged strength**, and act 17's `GramTrajEquiv` is consumed and not
redefined: it is the only relation any quotient here is taken over, and neither raw Gram equality
nor the uniform-phase relation nor act 13's level-2 or level-3 relations is adopted.

**The coarsest determining datum is out of scope** by this round's own freeze, and no statement
here is a lattice statement about the space of data. `P0` stays **OPEN** and two-part and its
threading part is untouched. `CoherentLift` is `ℕ`-indexed and this round does not change that: no
continuity, smoothness, derivative or continuum limit is introduced or used, and `LC2`'s
pseudometric is on the value space and never on the index. Nothing here says OI and QM are
inequivalent, and every visibility statement is under act 7's own readback convention with `D4b`
**negative**. Nothing is imported from the substratum Lemma 24.1 rounds, and nothing here is about
Track I.
-/

namespace OIBridge
namespace IntermediateCrossTimeStructure

set_option linter.unusedSectionVars false

open Finset Matrix DilationChoice CoherentLiftGauge TwoSidedGauge CrossTimeInvariants
  GramTrajectorySelection

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the budgeted definitions

Four of the five budgeted slots are used; the conditional fifth — a named functional for one Type D
candidate — is **unused**, every candidate functional being written inline in the statement that
needs it. **No lift, gauge element, witness, matrix, visible family, Gram tuple, entry value, law
datum or configuration is a top-level definition** here: each is a bound variable pinned by an
equation in the statement that needs it, exactly as acts 10 through 17 did. -/

/-- **A POINTWISE LAW** (definition slot 1) — a predicate on Gram trajectories that is equivalent to
a per-time condition applied slice by slice, the family `c` being existentially quantified so that
being pointwise is a property of the law and not extra data carried with it.

`XS1` is stated over this and cannot be stated readably without it. -/
def PointwiseLaw (Law : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  ∃ c : ℕ → (V → Matrix V V ℂ) → Prop, ∀ 𝔾, Law 𝔾 ↔ ∀ t, c t (𝔾 t)

/-- **THE `D`-DETERMINATION TARGET** (definition slot 2) — the augmented datum `D_F = (D₀, F)`
determines the Gram/orbit trajectory: two lifts with the same anchored readback at every time and
the same value of `F` have the same trajectory under act 17's `GramTrajEquiv`.

`D₀` is act 17's visible datum, `D₀(U) = fun t i j => ∑ a, ‖U t (i,a) (j,a₀)‖²`, written inline
under act 7's convention with `D4b` **negative**. The quotient is taken over `GramTrajEquiv` and
over **no other relation**. -/
def DeterminesTraj {β : Type} (a₀ : A) (F : (ℕ → Matrix (V × A) (V × A) ℂ) → β) : Prop :=
  ∀ U U' : ℕ → Matrix (V × A) (V × A) ℂ,
    (fun (t : ℕ) (i j : V) => ∑ a : A, ‖U t (i, a) (j, a₀)‖ ^ 2)
        = (fun (t : ℕ) (i j : V) => ∑ a : A, ‖U' t (i, a) (j, a₀)‖ ^ 2) →
      F U = F U' →
      GramTrajEquiv (fun t => FibreGram a₀ (U t)) (fun t => FibreGram a₀ (U' t))

set_option linter.unusedVariables false in
/-- **THE ONE-CONFIGURATION NON-TRIVIALITY WITNESS** (definition slot 3) — at the configuration
`(a₀, Γ)` the law's solution set is **nonempty** (`G₁` is in it), **non-singleton modulo
`GramTrajEquiv`** (`G₂` is in it and is inequivalent to `G₁`) and **proper** (`H` is pointwise
realizable and is not in it). Three properties, **one configuration, one witness**, with all three
trajectories pointwise realizable there.

**Split configurations would fail**, and the freeze records why: a law permitting everything at one
configuration and exactly one trajectory at another passes both separated tests while being vacuous
at the first and the answer in disguise at the second. Neither failure is visible to either
separated test.

**`H`'s pointwise realizability is load-bearing and is available only because of act 17's `TJ1`**:
the properness clause has to exhibit a trajectory the law excludes **from inside** the admissible
set, and `tj1_sufficiency` is what makes "pointwise realizable" and "is some coherent lift's
trajectory" the same thing. The anchor is carried in the configuration; realizability itself is
anchor-independent, act 12's sufficiency holding at every anchor. -/
def ProperAt (a₀ : A) (Γ : ℕ → Matrix V V ℝ) (Law : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  ∃ G₁ G₂ H : ℕ → V → Matrix V V ℂ,
    (∀ t, RealizableGram A (Γ t) (G₁ t)) ∧ (∀ t, RealizableGram A (Γ t) (G₂ t))
      ∧ (∀ t, RealizableGram A (Γ t) (H t))
      ∧ Law G₁ ∧ Law G₂ ∧ ¬ GramTrajEquiv G₁ G₂ ∧ ¬ Law H

set_option linter.unusedVariables false in
/-- **PROPAGATION, WITH BOTH FROZEN CLAUSES** (definition slot 4) — a law propagates at a
configuration iff **(i)** any two pointwise realizable solutions whose per-slice orbit classes agree
at time `0` have the same trajectory under `GramTrajEquiv`, **and (ii)** there is a time `t ≥ 1` at
which the solutions, taken **without** fixing the initial orbit, include two inequivalent per-slice
orbit classes.

**Clause (ii) is part of what "propagates" means and is not an extra rung.** "A law plus one
initial orbit propagates uniquely" says the initial orbit **does work**. A law that fixes every
later slice on its own satisfies clause (i) while the initial orbit contributes nothing, and
calling that propagation would report a slice-by-slice determination as a cross-time relation —
which is the distinction this round exists to keep. The two non-propagation mechanisms are
therefore kept apart and named separately wherever one is reported. -/
def PropagatesFrom (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (Law : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  (∀ G₁ G₂ : ℕ → V → Matrix V V ℂ,
      (∀ t, RealizableGram A (Γ t) (G₁ t)) → (∀ t, RealizableGram A (Γ t) (G₂ t)) →
        Law G₁ → Law G₂ → GramPhaseEquiv (G₁ 0) (G₂ 0) → GramTrajEquiv G₁ G₂)
    ∧ ∃ (t : ℕ) (G₁ G₂ : ℕ → V → Matrix V V ℂ), 1 ≤ t
        ∧ (∀ s, RealizableGram A (Γ s) (G₁ s)) ∧ (∀ s, RealizableGram A (Γ s) (G₂ s))
        ∧ Law G₁ ∧ Law G₂ ∧ ¬ GramPhaseEquiv (G₁ t) (G₂ t)

/-! ### Section B — `XS1`, the factorization theorem for pointwise laws, which runs first -/

/-- **`XS1` — POINTWISE LAWS FACTOR.** The solution set of a law that is pointwise in this round's
sense is the **product over time** of its per-time solution sets: a trajectory solves the law iff
each of its slices solves the corresponding per-time condition, and — the substantive half — an
**arbitrary time-wise recombination** of solutions is a solution, the value at each time being
drawn from a different solution.

**This is about propagation and not about determination.** A pointwise law whose per-time solution
set is a single orbit class at every time determines the trajectory, and `XS1` says so rather than
denying it. -/
theorem xs1_pointwise_factors {Law : (ℕ → V → Matrix V V ℂ) → Prop} (h : PointwiseLaw Law) :
    ∃ c : ℕ → (V → Matrix V V ℂ) → Prop,
      (∀ 𝔾, Law 𝔾 ↔ ∀ t, c t (𝔾 t))
        ∧ ∀ (𝔾 : ℕ → ℕ → V → Matrix V V ℂ) (σ : ℕ → ℕ),
            (∀ n, Law (𝔾 n)) → Law (fun t => 𝔾 (σ t) t) := by
  obtain ⟨c, hc⟩ := h
  exact ⟨c, hc, fun 𝔾 σ hall => (hc _).2 fun t => (hc _).1 (hall (σ t)) t⟩

/-- **THE SPLICING COROLLARY.** Two pointwise realizable solutions of a pointwise law whose
per-slice orbit classes differ at some time `tstar ≥ 1` can be spliced: there is a pointwise realizable
solution agreeing with the first everywhere except at `tstar`, agreeing with the second at `tstar`, hence
agreeing with the first at time `0` while being inequivalent to it.

**Act 17's `TJ1` is what makes the splice admissible, and the citation is at that step.**
Intersecting a product constraint with a **non-product** ambient set need not factor: the splice is
a solution **of the law** immediately, by pointwiseness, but it has to be **admissible** as well.
`tj1_trajectory_set` proves the admissible set **is** the product of the per-slice realizable sets,
so the intersection of two products is a product and the splice stays inside it. Without `TJ1` the
corollary does not follow. `TJ1` is consumed at merged strength and is neither enlarged nor
re-proved here. -/
theorem xs1_splice {a₀ : A} {Γ : ℕ → Matrix V V ℝ} {Law : (ℕ → V → Matrix V V ℂ) → Prop}
    (hLaw : PointwiseLaw Law) {G₁ G₂ : ℕ → V → Matrix V V ℂ}
    (hA₁ : ∃ U : ℕ → Matrix (V × A) (V × A) ℂ,
        CoherentLift a₀ Γ U ∧ ∀ t, FibreGram a₀ (U t) = G₁ t)
    (hA₂ : ∃ U : ℕ → Matrix (V × A) (V × A) ℂ,
        CoherentLift a₀ Γ U ∧ ∀ t, FibreGram a₀ (U t) = G₂ t)
    (h₁ : Law G₁) (h₂ : Law G₂) {tstar : ℕ} (htstar : 1 ≤ tstar)
    (hne : ¬ GramPhaseEquiv (G₁ tstar) (G₂ tstar)) :
    ∃ (G' : ℕ → V → Matrix V V ℂ) (U' : ℕ → Matrix (V × A) (V × A) ℂ),
      CoherentLift a₀ Γ U' ∧ (∀ t, FibreGram a₀ (U' t) = G' t)
        ∧ Law G' ∧ G' tstar = G₂ tstar ∧ (∀ t, t ≠ tstar → G' t = G₁ t)
        ∧ G' 0 = G₁ 0 ∧ ¬ GramTrajEquiv G' G₁ := by
  classical
  obtain ⟨c, hc⟩ := hLaw
  -- `TJ1`, necessity direction: the two solutions are pointwise realizable.
  have hr₁ : ∀ t, RealizableGram A (Γ t) (G₁ t) := (tj1_trajectory_set a₀ G₁).1 hA₁
  have hr₂ : ∀ t, RealizableGram A (Γ t) (G₂ t) := (tj1_trajectory_set a₀ G₂).1 hA₂
  refine ⟨fun t => if t = tstar then G₂ t else G₁ t, ?_⟩
  have hrG' : ∀ t, RealizableGram A (Γ t) (if t = tstar then G₂ t else G₁ t) := by
    intro t
    by_cases ht : t = tstar
    · rw [if_pos ht]; exact hr₂ t
    · rw [if_neg ht]; exact hr₁ t
  -- `TJ1`, sufficiency direction: the spliced product point is **admissible**, which is the step
  -- the freeze names. The ambient set is the product, so the splice stays inside it.
  obtain ⟨U', hU'c, hU'g⟩ := (tj1_trajectory_set a₀ (fun t => if t = tstar then G₂ t else G₁ t)).2 hrG'
  have hzero_ne : (0 : ℕ) ≠ tstar := fun h => absurd (h ▸ htstar) (by decide)
  refine ⟨U', hU'c, hU'g, (hc _).2 fun t => ?_, by simp, fun t ht => by simp [ht],
    by simp [hzero_ne], fun hEq => hne ?_⟩
  · by_cases ht : t = tstar
    · subst ht; simpa using (hc G₂).1 h₂ t
    · simpa [ht] using (hc G₁).1 h₁ t
  · have h := hEq tstar
    simp only [if_pos] at h
    exact gramPhaseEquiv_symm h

/-- **NO POINTWISE LAW PROPAGATES, AT ANY CONFIGURATION.** The two cases the freeze names are closed
at once by a single splice: if clause (ii) holds, two inequivalent orbit classes survive at a time
`t ≥ 1`, the splice is a pointwise realizable solution agreeing at time `0` and inequivalent, and
clause (i) fails; and if clause (ii) fails there is nothing to prove, the conjunction being false
already.

**So every pointwise candidate is ruled out as a route to the top line of the `L`-axis, as a theorem
of this round and not as a failed search.** The exclusion is bounded to the notion of law this round
defines and is **not** a statement about every conceivable pointwise condition, **not** a statement
about laws on any other object, and **not** a bound on what a later round could prove under a
different notion of law. **It is not the false sentence "no pointwise constraint yields cross-time
determination"**: what fails here is propagation. -/
theorem xs1_pointwise_not_propagates {a₀ : A} {Γ : ℕ → Matrix V V ℝ}
    {Law : (ℕ → V → Matrix V V ℂ) → Prop} (hLaw : PointwiseLaw Law) :
    ¬ PropagatesFrom a₀ Γ Law := by
  rintro ⟨huniq, tstar, G₁, G₂, htstar, hr₁, hr₂, h₁, h₂, hne⟩
  obtain ⟨U₁, hU₁c, hU₁g⟩ := tj1_sufficiency a₀ hr₁
  obtain ⟨U₂, hU₂c, hU₂g⟩ := tj1_sufficiency a₀ hr₂
  obtain ⟨G', U', hU'c, hU'g, hLG', _, _, h0, htraj⟩ :=
    xs1_splice (a₀ := a₀) (Γ := Γ) hLaw ⟨U₁, hU₁c, hU₁g⟩ ⟨U₂, hU₂c, hU₂g⟩ h₁ h₂ htstar hne
  exact htraj (huniq G' G₁ ((tj1_trajectory_set a₀ G').1 ⟨U', hU'c, hU'g⟩) hr₁ hLG' h₁
    (by rw [h0]; exact gramPhaseEquiv_refl _))

/-! ### Section C — the well-posedness check, as it stands at execution -/

/-- **THE ANCHORED READBACK FACTORS THROUGH ACT 13'S LEVEL-2 DATUM, UNCONDITIONALLY.** The chain is
two merged steps and neither carries an admissibility hypothesis: act 13's `fibreCrossGram_diag` is
a definitional identity, so the level-2 datum contains the per-slice Gram tuple at every time, and
act 12's `fibreGram_diag` reads the anchored readback off that tuple's diagonal with **no**
hypothesis on the visible family and no appeal to coherence.

**This is why obligation 1 of the refinement sandwich is frozen for the full pair `D_F = (D₀, F)`**
rather than for `F` alone: equality of the level-2 datum already forces equality of `D₀`, so the
whole content of obligation 1 falls on `F`. -/
theorem xs2_readback_factors_through_level2 (a₀ : A) (U U' : ℕ → Matrix (V × A) (V × A) ℂ)
    (h : ∀ (i : V) (t s : ℕ), FibreCrossGram a₀ U i t s = FibreCrossGram a₀ U' i t s) :
    (fun (t : ℕ) (i j : V) => ∑ a : A, ‖U t (i, a) (j, a₀)‖ ^ 2)
      = fun (t : ℕ) (i j : V) => ∑ a : A, ‖U' t (i, a) (j, a₀)‖ ^ 2 := by
  funext t i j
  have h1 := congrFun (congrFun (h i t t) j) j
  rw [fibreCrossGram_diag, fibreCrossGram_diag, fibreGram_diag, fibreGram_diag] at h1
  exact_mod_cast h1

/-- The anchored readback of a coherent lift is the visible family, at every time. Act 7's
convention throughout, with `D4b` **negative**. -/
theorem readback_of_coherentLift {a₀ : A} {Γ : ℕ → Matrix V V ℝ}
    {U : ℕ → Matrix (V × A) (V × A) ℂ} (hU : CoherentLift a₀ Γ U) :
    (fun (t : ℕ) (i j : V) => ∑ a : A, ‖U t (i, a) (j, a₀)‖ ^ 2) = fun t i j => Γ t i j :=
  funext fun t => funext fun i => funext fun j => ((hU t).2 i j).symm

/-! ### Section D — the Type D ladder: the three readback candidates

Every countercontrol below is at the configuration the freeze names for the obligation it
discharges. **Obligation 3 is stated against act 13's level-2 datum and never against the
trajectory.** A pair with equal augmented datum and inequivalent trajectories is precisely a
counterexample to the determination target, so the trajectory phrasing is unsatisfiable exactly
when the axis succeeds and would make the top line unreachable by construction; what obligation 3
actually asks is that the candidate be a **strict coarsening of act 13's datum**, which is a
statement about the two data and not about the trajectories they determine. -/

/-- **OBLIGATION 1 FOR ALL THREE TYPE D CANDIDATES AT ONCE, UNIVERSALLY.** Equality of act 13's
level-2 datum implies equality of the augmented datum `D_F = (D₀, F)` for each of the three frozen
functionals — the adjacent-pair cross-Gram `F₁`, the diagonal cross-time overlaps `F₂`, and the
anchored block `F₃` — **both components at once**.

Each is a restriction or a fibre sum of act 13's datum, so the `F` component is congruence; the
`D₀` component is `xs2_readback_factors_through_level2`. **So none of the three consumes
information beyond act 13's level-2 datum**, and the whole substantive content of the refinement
sandwich falls on obligations 2 and 3. -/
theorem df_bounded_above (a₀ : A) (U U' : ℕ → Matrix (V × A) (V × A) ℂ)
    (h : ∀ (i : V) (t s : ℕ), FibreCrossGram a₀ U i t s = FibreCrossGram a₀ U' i t s) :
    ((fun (t : ℕ) (i j : V) => ∑ a : A, ‖U t (i, a) (j, a₀)‖ ^ 2)
        = fun (t : ℕ) (i j : V) => ∑ a : A, ‖U' t (i, a) (j, a₀)‖ ^ 2)
      ∧ ((fun (i : V) (t : ℕ) => FibreCrossGram a₀ U i t (t + 1))
          = fun (i : V) (t : ℕ) => FibreCrossGram a₀ U' i t (t + 1))
      ∧ ((fun (i : V) (t s : ℕ) (j : V) => FibreCrossGram a₀ U i t s j j)
          = fun (i : V) (t s : ℕ) (j : V) => FibreCrossGram a₀ U' i t s j j)
      ∧ ((fun t s : ℕ => ∑ i : V, FibreCrossGram a₀ U i t s)
          = fun t s : ℕ => ∑ i : V, FibreCrossGram a₀ U' i t s) := by
  refine ⟨xs2_readback_factors_through_level2 a₀ U U' h, ?_, ?_, ?_⟩
  · funext i t; exact h i t (t + 1)
  · funext i t s j; rw [h i t s]
  · funext t s; exact Finset.sum_congr rfl fun i _ => h i t s

/-- **`DF1`, OBLIGATION 2 — the adjacent-pair cross-Gram is strictly above act 17's visible data.**
At the frozen configuration — act 12's Hadamard objects at `|V| = 4`, `|A| = 1`, anchor `0`,
`Γ ≡ ¼` — the two **constant** coherent lifts `U ≡ H(1)` and `U' ≡ H(i)` share the anchored
readback, both being coherent lifts of the same visible family, and their adjacent-pair cross-Grams
differ: for a constant lift `Ξ_i^{(t,t+1)}` **is** the fibre-Gram tuple, and act 12's merged
`hadamard_slices_not_twoSided` proves those two tuples are not even phase-equivalent.

**One merged witness family, one consequence drawn from it here.** This is act 12's own exhibited
pair, consumed at its own existential strength and neither enlarged nor re-proved. -/
theorem df1_above_visible :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ CoherentLift (0 : Fin 1) Γ U ∧ CoherentLift (0 : Fin 1) Γ U'
        ∧ ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U t (i, a) (j, 0)‖ ^ 2)
            = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U' t (i, a) (j, 0)‖ ^ 2)
        ∧ (fun (i : Fin 4) (t : ℕ) => FibreCrossGram (0 : Fin 1) U i t (t + 1))
            ≠ fun (i : Fin 4) (t : ℕ) => FibreCrossGram (0 : Fin 1) U' i t (t + 1) := by
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, _hH₁, _hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hcU : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun _ => H₁) := fun _ => hadm₁
  have hcU' : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun _ => Hᵢ) := fun _ => hadmᵢ
  refine ⟨fun _ => Γ₀, fun _ => H₁, fun _ => Hᵢ, fun _ i j => by rw [hΓ₀]; rfl, hcU, hcU',
    (readback_of_coherentLift hcU).trans (readback_of_coherentLift hcU').symm, fun hEq => ?_⟩
  refine hnotG ?_
  have : FibreGram (0 : Fin 1) H₁ = FibreGram (0 : Fin 1) Hᵢ :=
    funext fun i => congrFun (congrFun hEq i) 0
  rw [this]
  exact gramPhaseEquiv_refl _

/-- **`DF2`, OBLIGATION 2 — the diagonal cross-time overlaps are strictly above act 17's visible
data.** At the frozen configuration, the piecewise pair `U ≡ H(1)` against `U'` equal to `H(1)` at
time `0` and `H(i)` afterwards shares the anchored readback and separates at the entry the freeze
names: fibre `1`, time pair `(0,1)`, column `1`, where the diagonal overlap is `¼` for the first
lift and `¼ i` for the second. **The separating index and quantity are named in the statement.** -/
theorem df2_above_visible :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ CoherentLift (0 : Fin 1) Γ U ∧ CoherentLift (0 : Fin 1) Γ U'
        ∧ ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U t (i, a) (j, 0)‖ ^ 2)
            = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U' t (i, a) (j, 0)‖ ^ 2)
        ∧ FibreCrossGram (0 : Fin 1) U 1 0 1 1 1 = 1 / 4
        ∧ FibreCrossGram (0 : Fin 1) U' 1 0 1 1 1 = Complex.I / 4 := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, _hnotG, _⟩ := hadamard_slices_not_twoSided
  have hcU : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun _ => H₁) := fun _ => hadm₁
  have hcU' : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun t => if t = 0 then H₁ else Hᵢ) := by
    intro t; by_cases ht : t = 0
    · simp only [if_pos ht]; exact hadm₁
    · simp only [if_neg ht]; exact hadmᵢ
  refine ⟨fun _ => Γ₀, fun _ => H₁, fun t => if t = 0 then H₁ else Hᵢ,
    fun _ i j => by rw [hΓ₀]; rfl, hcU, hcU',
    (readback_of_coherentLift hcU).trans (readback_of_coherentLift hcU').symm, ?_, ?_⟩
  · rw [fibreCrossGram_apply, Fin.sum_univ_one, hH₁]
    norm_num [Matrix.of_apply]
  · rw [fibreCrossGram_apply, Fin.sum_univ_one, if_neg one_ne_zero, hH₁, hHᵢ]
    norm_num [Matrix.of_apply]
    ring

/-- **`DF2`, OBLIGATION 3 AND THE DETERMINATION TARGET — `DF2-SANDWICH`'s third obligation together
with `DF2-RESID`.** At the frozen configuration the two **constant** coherent lifts `U ≡ H(1)` and
`U' ≡ H(i)` have every anchored entry of modulus `½`, so the **diagonal** cross-time overlap is the
constant `¼` at every fibre, every time pair and every column for both — the augmented datum agrees
— while act 13's level-2 datum differs already at the time pair `(0,0)`, where act 13's
`fibreCrossGram_diag` returns the fibre-Gram tuples act 12 proves inequivalent.

**Obligation 3 is witnessed against act 13's level-2 datum**, and the trajectory statement is the
separate determination target: the same pair has `GramTrajEquiv`-inequivalent trajectories, so
`DeterminesTraj` fails for `F₂` on this carrier. Withholding the off-diagonal entries withholds
exactly the residual act 12's `SH1` identifies as the whole of the freedom after the two-sided
gauge, so the datum is informative across time and still does not determine the trajectory. -/
theorem df2_below_level2_and_resid :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ CoherentLift (0 : Fin 1) Γ U ∧ CoherentLift (0 : Fin 1) Γ U'
        ∧ ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U t (i, a) (j, 0)‖ ^ 2)
            = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U' t (i, a) (j, 0)‖ ^ 2)
        ∧ (∀ i t s j, FibreCrossGram (0 : Fin 1) U i t s j j = 1 / 4)
        ∧ (∀ i t s j, FibreCrossGram (0 : Fin 1) U' i t s j j = 1 / 4)
        ∧ ((fun i : Fin 4 => FibreCrossGram (0 : Fin 1) U i 0 0)
            ≠ fun i : Fin 4 => FibreCrossGram (0 : Fin 1) U' i 0 0)
        ∧ ¬ GramTrajEquiv (fun t => FibreGram (0 : Fin 1) (U t))
            (fun t => FibreGram (0 : Fin 1) (U' t))
        ∧ ¬ DeterminesTraj (0 : Fin 1)
            (fun U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ =>
              fun (i : Fin 4) (t s : ℕ) (j : Fin 4) => FibreCrossGram (0 : Fin 1) U i t s j j) := by
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hcU : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun _ => H₁) := fun _ => hadm₁
  have hcU' : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun _ => Hᵢ) := fun _ => hadmᵢ
  have hd₁ : ∀ (i : Fin 4) (t s : ℕ) (j : Fin 4),
      FibreCrossGram (0 : Fin 1) (fun _ : ℕ => H₁) i t s j j = 1 / 4 := by
    intro i t s j
    rw [fibreCrossGram_apply, Fin.sum_univ_one, hH₁]
    fin_cases i <;> fin_cases j <;> norm_num [Matrix.of_apply]
  have hdᵢ : ∀ (i : Fin 4) (t s : ℕ) (j : Fin 4),
      FibreCrossGram (0 : Fin 1) (fun _ : ℕ => Hᵢ) i t s j j = 1 / 4 := by
    intro i t s j
    rw [fibreCrossGram_apply, Fin.sum_univ_one, hHᵢ]
    fin_cases i <;> fin_cases j <;>
      norm_num [Matrix.of_apply, Complex.ext_iff]
  have hD₀ := (readback_of_coherentLift hcU).trans (readback_of_coherentLift hcU').symm
  have htraj : ¬ GramTrajEquiv (fun _ : ℕ => FibreGram (0 : Fin 1) H₁)
      (fun _ : ℕ => FibreGram (0 : Fin 1) Hᵢ) := fun h => hnotG (h 0)
  refine ⟨fun _ => Γ₀, fun _ => H₁, fun _ => Hᵢ, fun _ i j => by rw [hΓ₀]; rfl, hcU, hcU', hD₀,
    hd₁, hdᵢ, fun hEq => hnotG ?_, htraj, fun hdet => htraj ?_⟩
  · have : FibreGram (0 : Fin 1) H₁ = FibreGram (0 : Fin 1) Hᵢ := funext fun i => congrFun hEq i
    rw [this]; exact gramPhaseEquiv_refl _
  · exact hdet _ _ hD₀
      (funext fun i => funext fun t => funext fun s => funext fun j =>
        (hd₁ i t s j).trans (hdᵢ i t s j).symm)

/-- **`DF3`, OBLIGATION 2 — cross-time anchor coherence is strictly above act 17's visible data.**
At the frozen configuration the piecewise pair shares the anchored readback, and the anchored block
of the column cross-Gram at the time pair `(0,1)` — act 13's level 1, the fibre sum of level 2 by
`sum_fibreCrossGram` — is `1` at the entry `(1,1)` for the first lift and `(1 + i)/2` for the
second. **The separating index and quantity are named in the statement.**

**No outcome of `DF3` resolves, reopens or narrows act 10's anchor-axis reclassification**, in
either direction. The datum is defined relative to the anchoring convention and its very statement
moves if the convention moves; freezing it as a candidate is how this round asks whether cross-time
anchor coherence is the intermediate datum, without asserting anything about the anchor axis. -/
theorem df3_above_visible :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ CoherentLift (0 : Fin 1) Γ U ∧ CoherentLift (0 : Fin 1) Γ U'
        ∧ ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U t (i, a) (j, 0)‖ ^ 2)
            = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U' t (i, a) (j, 0)‖ ^ 2)
        ∧ (∑ i : Fin 4, FibreCrossGram (0 : Fin 1) U i 0 1) 1 1 = 1
        ∧ (∑ i : Fin 4, FibreCrossGram (0 : Fin 1) U' i 0 1) 1 1 = (1 + Complex.I) / 2 := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, _hnotG, _⟩ := hadamard_slices_not_twoSided
  have hcU : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun _ => H₁) := fun _ => hadm₁
  have hcU' : CoherentLift (0 : Fin 1) (fun _ => Γ₀) (fun t => if t = 0 then H₁ else Hᵢ) := by
    intro t; by_cases ht : t = 0
    · simp only [if_pos ht]; exact hadm₁
    · simp only [if_neg ht]; exact hadmᵢ
  refine ⟨fun _ => Γ₀, fun _ => H₁, fun t => if t = 0 then H₁ else Hᵢ,
    fun _ i j => by rw [hΓ₀]; rfl, hcU, hcU',
    (readback_of_coherentLift hcU).trans (readback_of_coherentLift hcU').symm, ?_, ?_⟩
  · rw [Matrix.sum_apply]
    simp only [fibreCrossGram_apply, Fin.sum_univ_one, hH₁]
    rw [Fin.sum_univ_four]
    norm_num [Matrix.of_apply, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  · rw [Matrix.sum_apply]
    simp only [fibreCrossGram_apply, Fin.sum_univ_one, if_neg one_ne_zero, hH₁, hHᵢ]
    rw [Fin.sum_univ_four]
    norm_num [Matrix.of_apply, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]

/-! ### Section E — the Type L ladder: the structural-law candidates

A **law datum** is an object written from the anchor, the visible family and the index alone,
constructed before any lift exists and consulting no lift at any point; the law it induces is a
predicate on Gram/orbit trajectories required to be `GramTrajEquiv`-invariant, which is the
orbit-level well-definedness obligation and binds every candidate here. A constraint stated on
representatives that is not invariant under the per-time phase and frame freedom is not a
constraint on the Gram/orbit trajectory at all: it would "select" by fixing an unphysical frame.

**The non-triviality witness is at ONE COMMON CONFIGURATION** and carries all four conjuncts
together, and **propagation carries BOTH frozen clauses**, reported separately. -/

/-- **`LC0` — THE POINTWISE ADMISSIBILITY LAW.** The law datum is the pair of per-slice orbit
classes `[G(H(1))]`, `[G(H(i))]` at the frozen configuration `Γ ≡ ¼`, `|V| = 4`, `|A| = 1`, anchor
`0`, and the law admits a trajectory iff each of its slices lies in one of the two. **It consults no
lift**: it is a condition on per-slice orbit classes, fixed before any lift is chosen.

Four things are proved together at that one configuration. The law respects `GramTrajEquiv`; its
solution set is **nonempty, non-singleton modulo `GramTrajEquiv` and proper**, the excluded
trajectory being the constant trajectory at `[G(H(−1))]`, the third member of act 12's own frozen
family `H(z)`, **pointwise realizable** and excluded — realizability available from inside the
admissible set because of act 12's `sh1_necessity`; it **does not propagate**, which is this round's
`XS1` applied to a named candidate and is therefore a **theorem of this round rather than a failed
search**; and the mechanism is exhibited — two pointwise realizable solutions agreeing at time `0`
whose trajectories are inequivalent, which is clause (i) failing and **not** the outcome in which
the initial orbit does no work.

The three classes are separated by act 12's merged `∼_D`-invariant `G^{(0)}_{10} G^{(1)}_{01}`,
whose values on the frozen family `H(z)` are `z/16`: `1/16`, `i/16` and `−1/16`. -/
theorem lc0_pointwise_law :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (c : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop)
      (Law : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ Law = (fun 𝔾 => ∀ t, c t (𝔾 t))
        ∧ PointwiseLaw Law
        ∧ (∀ 𝔾 𝔾', GramTrajEquiv 𝔾 𝔾' → (Law 𝔾 ↔ Law 𝔾'))
        ∧ ProperAt (0 : Fin 1) Γ Law
        ∧ ¬ PropagatesFrom (0 : Fin 1) Γ Law
        ∧ (∃ G₁ G₂ : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
            (∀ t, RealizableGram (Fin 1) (Γ t) (G₁ t))
              ∧ (∀ t, RealizableGram (Fin 1) (Γ t) (G₂ t))
              ∧ Law G₁ ∧ Law G₂ ∧ GramPhaseEquiv (G₁ 0) (G₂ 0) ∧ ¬ GramTrajEquiv G₁ G₂) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hunit : (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1))
      ∈ Matrix.unitaryGroup (Fin 4 × Fin 1) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_four,
        Matrix.conjTranspose_apply] <;> norm_num [Complex.ext_iff]
  have hadmNeg : AdmissibleDilationAt Γ₀ (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)) := by
    refine ⟨hunit, fun i j => ?_⟩
    rw [hΓ₀]
    fin_cases i <;> fin_cases j <;> simp <;> norm_num
  have hne₁ : ¬ GramPhaseEquiv (FibreGram (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)))
      (FibreGram (0 : Fin 1) H₁) := by
    intro hG
    have hinv := gramPhaseEquiv_cross_invariant hG 0 1
    rw [hH₁] at hinv
    simp [fibreGram_apply] at hinv
    norm_num [Complex.ext_iff] at hinv
  have hneᵢ : ¬ GramPhaseEquiv (FibreGram (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)))
      (FibreGram (0 : Fin 1) Hᵢ) := by
    intro hG
    have hinv := gramPhaseEquiv_cross_invariant hG 0 1
    rw [hHᵢ] at hinv
    simp [fibreGram_apply] at hinv
    norm_num [Complex.ext_iff] at hinv
  have hpw : PointwiseLaw (fun 𝔾 : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ =>
      ∀ t, GramPhaseEquiv (𝔾 t) (FibreGram (0 : Fin 1) H₁)
        ∨ GramPhaseEquiv (𝔾 t) (FibreGram (0 : Fin 1) Hᵢ)) :=
    ⟨fun _ G => GramPhaseEquiv G (FibreGram (0 : Fin 1) H₁)
      ∨ GramPhaseEquiv G (FibreGram (0 : Fin 1) Hᵢ), fun _ => Iff.rfl⟩
  refine ⟨fun _ => Γ₀,
    fun _ G => GramPhaseEquiv G (FibreGram (0 : Fin 1) H₁)
      ∨ GramPhaseEquiv G (FibreGram (0 : Fin 1) Hᵢ),
    fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 t) (FibreGram (0 : Fin 1) H₁)
      ∨ GramPhaseEquiv (𝔾 t) (FibreGram (0 : Fin 1) Hᵢ),
    fun _ i j => by rw [hΓ₀]; rfl, rfl, hpw, ?_, ?_,
    xs1_pointwise_not_propagates (a₀ := (0 : Fin 1)) (Γ := fun _ => Γ₀) hpw, ?_⟩
  · exact fun 𝔾 𝔾' hEq =>
      ⟨fun h t => (h t).imp (gramPhaseEquiv_trans (gramPhaseEquiv_symm (hEq t)))
        (gramPhaseEquiv_trans (gramPhaseEquiv_symm (hEq t))),
       fun h t => (h t).imp (gramPhaseEquiv_trans (hEq t)) (gramPhaseEquiv_trans (hEq t))⟩
  · exact ⟨fun _ => FibreGram (0 : Fin 1) H₁, fun _ => FibreGram (0 : Fin 1) Hᵢ,
      fun _ => FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)),
      fun _ => sh1_necessity hadm₁, fun _ => sh1_necessity hadmᵢ, fun _ => sh1_necessity hadmNeg,
      fun _ => Or.inl (gramPhaseEquiv_refl _), fun _ => Or.inr (gramPhaseEquiv_refl _),
      fun h => hnotG (h 0), fun h => (h 0).elim hne₁ hneᵢ⟩
  · refine ⟨fun _ => FibreGram (0 : Fin 1) H₁,
      fun t => if t = 1 then FibreGram (0 : Fin 1) Hᵢ else FibreGram (0 : Fin 1) H₁,
      fun _ => sh1_necessity hadm₁, fun t => ?_, fun _ => Or.inl (gramPhaseEquiv_refl _),
      fun t => ?_, ?_, fun h => hnotG ?_⟩
    · by_cases ht : t = 1
      · simp only [if_pos ht]; exact sh1_necessity hadmᵢ
      · simp only [if_neg ht]; exact sh1_necessity hadm₁
    · by_cases ht : t = 1
      · simp only [if_pos ht]; exact Or.inr (gramPhaseEquiv_refl _)
      · simp only [if_neg ht]; exact Or.inl (gramPhaseEquiv_refl _)
    · simp only [if_neg (by decide : ¬ ((0 : ℕ) = 1))]
      exact gramPhaseEquiv_refl _
    · have hh := h 1
      simp only [if_pos rfl] at hh
      exact hh

/-- **`LC3` — THE GENERATOR LAW, WRITTEN AT ORBIT LEVEL, SO THE DESCENT OBLIGATION IS DISCHARGED BY
CONSTRUCTION.** The transition `Φ` is the identity on per-slice orbit classes and the law is
`[𝔾(t+1)] = Φ([𝔾 t])`, a law of evolution written from the visible family before any lift exists.
The descent obligation is part of the candidate and is discharged here by the first of the two
routes the freeze permits — **writing the candidate directly as an orbit-level transition** —
rather than by a gauge-naturality argument on a representative-level `V_t`. A representative-level
generator that did not descend would "select" by fixing an unphysical frame.

At the frozen configuration the law is **proper**: nonempty and non-singleton modulo
`GramTrajEquiv` — both constant Hadamard trajectories solve it and they are inequivalent — and it
**excludes** the pointwise realizable trajectory that changes class at the first step. And it
**propagates**, with both frozen clauses: two solutions agreeing at time `0` have the same
trajectory, by induction along the transition; **and** the solutions, taken without the initial
orbit fixed, occupy two inequivalent orbit classes at time `1`, so **the initial orbit does work**
and what is reported is propagation and not slice-by-slice determination.

**That a law of evolution determines a history given an initial condition is what such a law is**,
and it is legitimate here because the law datum is writable from the anchor and the visible family
before any lift exists. **It is not an assertion that the law obtains, not an adoption of it, and
not a claim that the programme requires one.** The final conjunct records that this candidate is
**not** pointwise, so `XS1` says nothing about it in either direction. -/
theorem lc3_generator_law :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (Φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop)
      (Law : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ Φ = (fun G G' => GramPhaseEquiv G G')
        ∧ Law = (fun 𝔾 => ∀ t, Φ (𝔾 t) (𝔾 (t + 1)))
        ∧ (∀ G₁ G₁' G₂ G₂', GramPhaseEquiv G₁ G₁' → GramPhaseEquiv G₂ G₂' →
            (Φ G₁ G₂ ↔ Φ G₁' G₂'))
        ∧ (∀ 𝔾 𝔾', GramTrajEquiv 𝔾 𝔾' → (Law 𝔾 ↔ Law 𝔾'))
        ∧ ProperAt (0 : Fin 1) Γ Law
        ∧ PropagatesFrom (0 : Fin 1) Γ Law
        ∧ ¬ PointwiseLaw Law := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, _hH₁, _hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hstep : ∀ G : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      (∀ t, GramPhaseEquiv (G t) (G (t + 1))) → ∀ t, GramPhaseEquiv (G 0) (G t) := by
    intro G hG t
    induction t with
    | zero => exact gramPhaseEquiv_refl _
    | succ n ih => exact gramPhaseEquiv_trans ih (hG n)
  have hprop : PropagatesFrom (0 : Fin 1) (fun _ => Γ₀)
      (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 t) (𝔾 (t + 1))) := by
    refine ⟨fun G₁ G₂ _ _ h₁ h₂ h0 t =>
      gramPhaseEquiv_trans (gramPhaseEquiv_symm (hstep G₁ h₁ t))
        (gramPhaseEquiv_trans h0 (hstep G₂ h₂ t)),
      1, fun _ => FibreGram (0 : Fin 1) H₁, fun _ => FibreGram (0 : Fin 1) Hᵢ, le_refl 1,
      fun _ => sh1_necessity hadm₁, fun _ => sh1_necessity hadmᵢ,
      fun _ => gramPhaseEquiv_refl _, fun _ => gramPhaseEquiv_refl _, hnotG⟩
  refine ⟨fun _ => Γ₀, fun G G' => GramPhaseEquiv G G',
    fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 t) (𝔾 (t + 1)),
    fun _ i j => by rw [hΓ₀]; rfl, rfl, rfl, ?_, ?_, ?_, hprop,
    fun hp => xs1_pointwise_not_propagates hp hprop⟩
  · exact fun G₁ G₁' G₂ G₂' h1 h2 =>
      ⟨fun h => gramPhaseEquiv_trans (gramPhaseEquiv_symm h1) (gramPhaseEquiv_trans h h2),
       fun h => gramPhaseEquiv_trans h1 (gramPhaseEquiv_trans h (gramPhaseEquiv_symm h2))⟩
  · exact fun 𝔾 𝔾' hEq =>
      ⟨fun h t => gramPhaseEquiv_trans (gramPhaseEquiv_symm (hEq t))
        (gramPhaseEquiv_trans (h t) (hEq (t + 1))),
       fun h t => gramPhaseEquiv_trans (hEq t)
        (gramPhaseEquiv_trans (h t) (gramPhaseEquiv_symm (hEq (t + 1))))⟩
  · refine ⟨fun _ => FibreGram (0 : Fin 1) H₁, fun _ => FibreGram (0 : Fin 1) Hᵢ,
      fun t => if t = 0 then FibreGram (0 : Fin 1) H₁ else FibreGram (0 : Fin 1) Hᵢ,
      fun _ => sh1_necessity hadm₁, fun _ => sh1_necessity hadmᵢ, fun t => ?_,
      fun _ => gramPhaseEquiv_refl _, fun _ => gramPhaseEquiv_refl _, fun h => hnotG (h 0),
      fun h => hnotG ?_⟩
    · by_cases ht : t = 0
      · simp only [if_pos ht]; exact sh1_necessity hadm₁
      · simp only [if_neg ht]; exact sh1_necessity hadmᵢ
    · have hh := h 0
      simp only [if_neg (by decide : ¬ ((0 : ℕ) + 1 = 0))] at hh
      exact hh

/-- **`XS5` — THE `L`-AXIS OUTCOME IS `L-PROP`.** A genuine proper structural law, together with one
initial orbit, propagates uniquely: the named law is written from the anchor and the visible family
alone, before any lift is chosen; it respects `GramTrajEquiv`; its solution set at one exhibited
configuration is nonempty, non-singleton modulo `GramTrajEquiv` and proper, **all three witnessed
together at that one configuration**; two solutions agreeing at time `0` have the same trajectory;
and the law without the initial orbit fixed leaves two inequivalent orbit classes at an exhibited
time after the initial one, **so the initial orbit does work and what is reported is propagation and
not slice-by-slice determination**.

**The `D`-axis outcome is reported beside it and neither is above the other.** This is a statement
about the exact law this round names and about nothing else: it does not say the law obtains, does
not adopt it, does not say the programme requires one, and does not close `P0` or either of its
parts. -/
theorem xs5_l_axis_prop :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (Law : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ (∀ 𝔾 𝔾', GramTrajEquiv 𝔾 𝔾' → (Law 𝔾 ↔ Law 𝔾'))
        ∧ ProperAt (0 : Fin 1) Γ Law
        ∧ PropagatesFrom (0 : Fin 1) Γ Law
        ∧ ¬ PointwiseLaw Law := by
  obtain ⟨Γ, _Φ, Law, hΓ, _, _, _, hwd, hproper, hprop, hnp⟩ := lc3_generator_law
  exact ⟨Γ, Law, hΓ, hwd, hproper, hprop, hnp⟩

/-- **`LC2` — REGULARITY IN A NAMED GRAM PSEUDOMETRIC.** The pseudometric `d` is **named explicitly
in the statement** and is written from the Gram data alone: the distance between two per-slice
tuples is the modulus of the difference of act 12's merged `∼_D`-invariant
`G^{(0)}_{10} G^{(1)}_{01}`. Its three pseudometric properties are proved, and its
`∼_D`-invariance — which is what makes it a pseudometric on **orbit classes** rather than on
representatives — is proved from `gramPhaseEquiv_cross_invariant`. The bound `ε_t` is `0`, which is
below the distance between the two classes the countercontrol names.

**Nothing here imports continuity, differentiability or a limit.** `ℕ` carries successor and order
and nothing else, and `d` is a pseudometric on the **value** space, never on the index. And nothing
here imports a canonical `d`: the pseudometric is named in the statement and every verdict below is
about **that named `d`**, not about regularity in general. A failure of `LC2` as stated would not be
a refutation of regularity in general.

The law is **proper** at the frozen configuration, with all four conjuncts at one configuration; and
**propagation clause (i) fails while clause (ii) holds**, the two being reported separately. Clause
(i) fails at an exhibited pair: the constant trajectory at `[G(H(1))]` and the trajectory that moves
at the first step to `[G(H(1))]`'s column-swapped partner, which has the **same** value of the named
pseudometric's invariant — so the step has length `0` and the law is satisfied — while being
`∼_D`-inequivalent, certified through the same invariant read at the fibre pair `(0,2)` instead of
`(0,1)`. **So residual histories remain after the initial orbit is fixed**, which is not the outcome
in which the initial orbit does no work; clause (ii) holds and is exhibited, so the two mechanisms
are kept apart. -/
theorem lc2_regularity_law :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ)
      (ε : ℕ → ℝ) (Law : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ d = (fun G G' => ‖G 0 1 0 * G 1 0 1 - G' 0 1 0 * G' 1 0 1‖)
        ∧ ε = (fun _ => 0)
        ∧ Law = (fun 𝔾 => ∀ t, d (𝔾 t) (𝔾 (t + 1)) ≤ ε t)
        ∧ (∀ G, d G G = 0) ∧ (∀ G G', d G G' = d G' G)
        ∧ (∀ G G' G'', d G G'' ≤ d G G' + d G' G'')
        ∧ (∀ G G' H H', GramPhaseEquiv G G' → GramPhaseEquiv H H' → d G H = d G' H')
        ∧ (∀ 𝔾 𝔾', GramTrajEquiv 𝔾 𝔾' → (Law 𝔾 ↔ Law 𝔾'))
        ∧ ProperAt (0 : Fin 1) Γ Law
        ∧ (∃ G₁ G₂ : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
            (∀ t, RealizableGram (Fin 1) (Γ t) (G₁ t))
              ∧ (∀ t, RealizableGram (Fin 1) (Γ t) (G₂ t))
              ∧ Law G₁ ∧ Law G₂ ∧ GramPhaseEquiv (G₁ 0) (G₂ 0) ∧ ¬ GramTrajEquiv G₁ G₂)
        ∧ (∃ (t : ℕ) (G₁ G₂ : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), 1 ≤ t
            ∧ (∀ s, RealizableGram (Fin 1) (Γ s) (G₁ s))
            ∧ (∀ s, RealizableGram (Fin 1) (Γ s) (G₂ s))
            ∧ Law G₁ ∧ Law G₂ ∧ ¬ GramPhaseEquiv (G₁ t) (G₂ t)) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  -- act 12's `H(1)` with its last two columns interchanged: unitary, admissible for the same
  -- visible family, sharing the named pseudometric's invariant and inequivalent to it.
  have hunitS : (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, -1, 1; 1, -1, 1, -1] p.1 q.1))
      ∈ Matrix.unitaryGroup (Fin 4 × Fin 1) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_four,
        Matrix.conjTranspose_apply] <;> norm_num [Complex.ext_iff]
  have hadmS : AdmissibleDilationAt Γ₀ (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, -1, 1; 1, -1, 1, -1] p.1 q.1)) := by
    refine ⟨hunitS, fun i j => ?_⟩
    rw [hΓ₀]
    fin_cases i <;> fin_cases j <;> simp <;> norm_num
  -- the named invariant, computed on the three tuples
  have v₁ : FibreGram (0 : Fin 1) H₁ 0 1 0 * FibreGram (0 : Fin 1) H₁ 1 0 1 = 1 / 16 := by
    rw [fibreGram_apply, fibreGram_apply, Fin.sum_univ_one, Fin.sum_univ_one, hH₁]
    norm_num [Matrix.of_apply]
  have vᵢ : FibreGram (0 : Fin 1) Hᵢ 0 1 0 * FibreGram (0 : Fin 1) Hᵢ 1 0 1
      = Complex.I / 16 := by
    rw [fibreGram_apply, fibreGram_apply, Fin.sum_univ_one, Fin.sum_univ_one, hHᵢ]
    norm_num [Matrix.of_apply]
    ring
  have vS : FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, -1, 1; 1, -1, 1, -1] p.1 q.1)) 0 1 0
      * FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, -1, 1; 1, -1, 1, -1] p.1 q.1)) 1 0 1
      = 1 / 16 := by
    rw [fibreGram_apply, fibreGram_apply, Fin.sum_univ_one, Fin.sum_univ_one]
    norm_num [Matrix.of_apply]
  have hneS : ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) H₁)
      (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, -1, 1; 1, -1, 1, -1] p.1 q.1))) := by
    intro hG
    have hinv := gramPhaseEquiv_cross_invariant hG 0 2
    rw [hH₁] at hinv
    simp [fibreGram_apply, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons] at hinv
    norm_num [Complex.ext_iff] at hinv
  have hdinv : ∀ G G' H H' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      GramPhaseEquiv G G' → GramPhaseEquiv H H' →
      ‖G 0 1 0 * G 1 0 1 - H 0 1 0 * H 1 0 1‖ = ‖G' 0 1 0 * G' 1 0 1 - H' 0 1 0 * H' 1 0 1‖ := by
    intro G G' H H' h1 h2
    rw [gramPhaseEquiv_cross_invariant h1 0 1, gramPhaseEquiv_cross_invariant h2 0 1]
  have hgap : ¬ (‖FibreGram (0 : Fin 1) H₁ 0 1 0 * FibreGram (0 : Fin 1) H₁ 1 0 1
      - FibreGram (0 : Fin 1) Hᵢ 0 1 0 * FibreGram (0 : Fin 1) Hᵢ 1 0 1‖ ≤ 0) := by
    rw [v₁, vᵢ, norm_le_zero_iff, sub_eq_zero]
    norm_num [Complex.ext_iff]
  refine ⟨fun _ => Γ₀, fun G G' => ‖G 0 1 0 * G 1 0 1 - G' 0 1 0 * G' 1 0 1‖, fun _ => 0,
    fun 𝔾 => ∀ t, ‖𝔾 t 0 1 0 * 𝔾 t 1 0 1 - 𝔾 (t + 1) 0 1 0 * 𝔾 (t + 1) 1 0 1‖ ≤ 0,
    fun _ i j => by rw [hΓ₀]; rfl, rfl, rfl, rfl,
    fun G => by simp, fun G G' => norm_sub_rev _ _, fun G G' G'' => ?_, hdinv, ?_, ?_, ?_, ?_⟩
  · calc ‖G 0 1 0 * G 1 0 1 - G'' 0 1 0 * G'' 1 0 1‖
        = ‖(G 0 1 0 * G 1 0 1 - G' 0 1 0 * G' 1 0 1)
            + (G' 0 1 0 * G' 1 0 1 - G'' 0 1 0 * G'' 1 0 1)‖ := by rw [sub_add_sub_cancel]
      _ ≤ _ := norm_add_le _ _
  · exact fun 𝔾 𝔾' hEq =>
      ⟨fun h t => by rw [← hdinv _ _ _ _ (hEq t) (hEq (t + 1))]; exact h t,
       fun h t => by rw [hdinv _ _ _ _ (hEq t) (hEq (t + 1))]; exact h t⟩
  · refine ⟨fun _ => FibreGram (0 : Fin 1) H₁, fun _ => FibreGram (0 : Fin 1) Hᵢ,
      fun t => if t = 0 then FibreGram (0 : Fin 1) H₁ else FibreGram (0 : Fin 1) Hᵢ,
      fun _ => sh1_necessity hadm₁, fun _ => sh1_necessity hadmᵢ, fun t => ?_,
      fun _ => by simp, fun _ => by simp, fun h => hnotG (h 0), fun h => hgap ?_⟩
    · by_cases ht : t = 0
      · simp only [if_pos ht]; exact sh1_necessity hadm₁
      · simp only [if_neg ht]; exact sh1_necessity hadmᵢ
    · have hh := h 0
      simp only [if_neg (by decide : ¬ ((0 : ℕ) + 1 = 0))] at hh
      exact hh
  · refine ⟨fun _ => FibreGram (0 : Fin 1) H₁,
      fun t => if t = 0 then FibreGram (0 : Fin 1) H₁
        else FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, -1, 1; 1, -1, 1, -1] p.1 q.1)),
      fun _ => sh1_necessity hadm₁, fun t => ?_, fun _ => by simp, fun t => ?_, ?_, fun h => ?_⟩
    · by_cases ht : t = 0
      · simp only [if_pos ht]; exact sh1_necessity hadm₁
      · simp only [if_neg ht]; exact sh1_necessity hadmS
    · by_cases ht : t = 0
      · simp only [if_pos ht, if_neg (by omega : ¬ (t + 1 = 0))]
        rw [ht] at *
        rw [v₁, vS]
        simp
      · simp only [if_neg ht, if_neg (by omega : ¬ (t + 1 = 0))]
        simp
    · simp only [if_pos rfl]
      exact gramPhaseEquiv_refl _
    · have hh := h 1
      simp only [if_neg (by decide : ¬ ((1 : ℕ) = 0))] at hh
      exact hneS hh
  · exact ⟨1, fun _ => FibreGram (0 : Fin 1) H₁, fun _ => FibreGram (0 : Fin 1) Hᵢ, le_refl 1,
      fun _ => sh1_necessity hadm₁, fun _ => sh1_necessity hadmᵢ,
      fun _ => by simp, fun _ => by simp, hnotG⟩

/-- Auxiliary, and **not a definition**: the index-wise product of a `V`-unitary and an `A`-unitary,
placed on `V × A`, is unitary. The matrices stay bound variables pinned by equations in the
statements that need them. -/
theorem prod_mem_unitaryGroup (P : Matrix V V ℂ) (W : Matrix A A ℂ)
    (hP : Pᴴ * P = 1) (hW : Wᴴ * W = 1) :
    (Matrix.of fun p q : V × A => P p.1 q.1 * W p.2 q.2) ∈ Matrix.unitaryGroup (V × A) ℂ := by
  rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose]
  ext p q
  rw [Matrix.mul_apply, Fintype.sum_prod_type]
  have hstep : ∀ i : V,
      (∑ a : A, (Matrix.of fun p q : V × A => P p.1 q.1 * W p.2 q.2)ᴴ p (i, a)
          * (Matrix.of fun p q : V × A => P p.1 q.1 * W p.2 q.2) (i, a) q)
        = (star (P i p.1) * P i q.1) * ∑ a : A, star (W a p.2) * W a q.2 := by
    intro i
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun a _ => ?_
    simp only [Matrix.conjTranspose_apply, Matrix.of_apply, star_mul']
    ring
  rw [Finset.sum_congr rfl fun i _ => hstep i, ← Finset.sum_mul]
  have hPe : (∑ i : V, star (P i p.1) * P i q.1) = (1 : Matrix V V ℂ) p.1 q.1 := by
    rw [← hP, Matrix.mul_apply]
    exact Finset.sum_congr rfl fun i _ => by rw [Matrix.conjTranspose_apply]
  have hWe : (∑ a : A, star (W a p.2) * W a q.2) = (1 : Matrix A A ℂ) p.2 q.2 := by
    rw [← hW, Matrix.mul_apply]
    exact Finset.sum_congr rfl fun a _ => by rw [Matrix.conjTranspose_apply]
  rw [hPe, hWe]
  by_cases h1 : p.1 = q.1 <;> by_cases h2 : p.2 = q.2 <;>
    simp [Matrix.one_apply, Prod.ext_iff, h1, h2]

/-- Auxiliary. The same product is an **admissible dilation** of the visible family whose entries
are the squared moduli of the `V`-factor, at every anchor: the `A`-factor's anchored column has
unit squared-norm, so it contributes nothing to the anchored readback. Act 7's convention
throughout, with `D4b` **negative**. -/
theorem prod_admissible {Γ : Matrix V V ℝ} (a₀ : A) (P : Matrix V V ℂ) (W : Matrix A A ℂ)
    (hP : Pᴴ * P = 1) (hW : Wᴴ * W = 1) (hΓ : ∀ i j, Γ i j = ‖P i j‖ ^ 2) :
    AdmissibleDilationAt Γ a₀ (Matrix.of fun p q : V × A => P p.1 q.1 * W p.2 q.2) := by
  refine ⟨prod_mem_unitaryGroup P W hP hW, fun i j => ?_⟩
  have hcol : (∑ a : A, ‖W a a₀‖ ^ 2) = 1 := by
    have h1 := congrFun (congrFun hW a₀) a₀
    rw [Matrix.mul_apply, Matrix.one_apply_eq] at h1
    have h2 : (∑ a : A, ((‖W a a₀‖ ^ 2 : ℝ) : ℂ)) = 1 := by
      rw [← h1]
      exact Finset.sum_congr rfl fun a _ => by
        rw [Matrix.conjTranspose_apply, star_mul_self_eq_norm_sq]
    rw [← Complex.ofReal_sum] at h2
    exact_mod_cast h2
  rw [hΓ i j]
  calc ‖P i j‖ ^ 2 = ‖P i j‖ ^ 2 * ∑ a : A, ‖W a a₀‖ ^ 2 := by rw [hcol, mul_one]
    _ = ∑ a : A, ‖P i j * W a a₀‖ ^ 2 := by
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun a _ => by rw [norm_mul, mul_pow]
    _ = ∑ a : A, ‖(Matrix.of fun p q : V × A => P p.1 q.1 * W p.2 q.2) (i, a) (j, a₀)‖ ^ 2 := rfl

/-- **`DF1`, OBLIGATION 3 — the adjacent-pair cross-Gram is strictly below act 13's level-2 datum.**
At `|A| = 2`, which is where the countercontrol table places this obligation, two coherent lifts of
the frozen visible family `Γ ≡ ¼` share the anchored readback and **every adjacent-pair** fibre
cross-Gram, while their level-2 data differ at the non-adjacent pair `(0, 2)`: the value there is
`¼` for one and `−¼` for the other, at fibre `0` and column pair `(0,0)`. **The separating index and
quantity are named in the statement.**

The construction is act 12's own frozen `H(1)` carried to `|A| = 2` in two ways — once with its
anchored weight in the second ancilla slot and once in the first — alternating in time, against the
**time-dependent in-fibre left move** `diag(1, i)^t` of act 12's `LeftFibreGroup`, whose invisibility
is act 12's merged `left_preserves_admissible`. Alternation is what makes every adjacent pair place
one lift's anchored weight in a slot where the other's vanishes, so every adjacent cross-Gram is the
zero matrix for both lifts, while the pair `(0, 2)` sees the same slot twice and the left move
contributes `i² = −1`.

**Obligation 3 is stated against act 13's level-2 datum and never against the trajectory.** -/
theorem df1_below_level2 :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 2) (Fin 4 × Fin 2) ℂ),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 2, ‖U t (i, a) (j, 0)‖ ^ 2)
            = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 2, ‖U' t (i, a) (j, 0)‖ ^ 2)
        ∧ ((fun (i : Fin 4) (t : ℕ) => FibreCrossGram (0 : Fin 2) U i t (t + 1))
            = fun (i : Fin 4) (t : ℕ) => FibreCrossGram (0 : Fin 2) U' i t (t + 1))
        ∧ FibreCrossGram (0 : Fin 2) U 0 0 2 0 0 = 1 / 4
        ∧ FibreCrossGram (0 : Fin 2) U' 0 0 2 0 0 = -(1 / 4) := by
  classical
  set P : Matrix (Fin 4) (Fin 4) ℂ := Matrix.of (fun i j : Fin 4 =>
    (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] i j) with hPdef
  set SW : Matrix (Fin 2) (Fin 2) ℂ := !![0, 1; 1, 0] with hSWdef
  set M : Matrix (Fin 4 × Fin 2) (Fin 4 × Fin 2) ℂ :=
    Matrix.of (fun p q : Fin 4 × Fin 2 => P p.1 q.1 * SW p.2 q.2) with hMdef
  set N : Matrix (Fin 4 × Fin 2) (Fin 4 × Fin 2) ℂ :=
    Matrix.of (fun p q : Fin 4 × Fin 2 =>
      P p.1 q.1 * (1 : Matrix (Fin 2) (Fin 2) ℂ) p.2 q.2) with hNdef
  set dd : Fin 4 × Fin 2 → ℂ := fun p => if p.2 = 0 then 1 else Complex.I with hdddef
  have hPu : Pᴴ * P = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [hPdef, Matrix.mul_apply, Fin.sum_univ_four, Matrix.conjTranspose_apply] <;>
      norm_num [Complex.ext_iff]
  have hSWu : SWᴴ * SW = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [hSWdef, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply]
  have hIu : (1 : Matrix (Fin 2) (Fin 2) ℂ)ᴴ * 1 = 1 := by simp
  have hΓn : ∀ i j : Fin 4,
      (Matrix.of (fun _ _ : Fin 4 => (1 / 4 : ℝ))) i j = ‖P i j‖ ^ 2 := by
    intro i j
    fin_cases i <;> fin_cases j <;> simp [hPdef] <;> norm_num
  have hMadm : AdmissibleDilationAt (Matrix.of (fun _ _ : Fin 4 => (1 / 4 : ℝ))) (0 : Fin 2) M :=
    prod_admissible 0 P SW hPu hSWu hΓn
  have hNadm : AdmissibleDilationAt (Matrix.of (fun _ _ : Fin 4 => (1 / 4 : ℝ))) (0 : Fin 2) N :=
    prod_admissible 0 P 1 hPu hIu hΓn
  have hUadm : ∀ t : ℕ, AdmissibleDilationAt (Matrix.of (fun _ _ : Fin 4 => (1 / 4 : ℝ)))
      (0 : Fin 2) (if t % 2 = 0 then M else N) := by
    intro t
    by_cases ht : t % 2 = 0
    · simp only [if_pos ht]; exact hMadm
    · simp only [if_neg ht]; exact hNadm
  have hunitpow : ∀ (z : ℂ), ‖z‖ = 1 → ∀ n : ℕ, star (z ^ n) * z ^ n = 1 := by
    intro z hz n
    rw [star_pow, ← mul_pow, star_mul_self_eq_norm_sq, hz]
    norm_num
  have hddnorm : ∀ p : Fin 4 × Fin 2, ‖dd p‖ = 1 := by
    intro p
    by_cases hp : p.2 = 0 <;> simp [hdddef, hp]
  have hL : ∀ t : ℕ, LeftFibreGroup (Matrix.diagonal (fun p : Fin 4 × Fin 2 => dd p ^ t)) := by
    intro t
    refine ⟨?_, fun p q hpq => Matrix.diagonal_apply_ne _ (fun h => hpq (by rw [h]))⟩
    rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose,
      Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
    congr 1
    funext p
    exact hunitpow (dd p) (hddnorm p) t
  have hcU : CoherentLift (0 : Fin 2) (fun _ => Matrix.of (fun _ _ : Fin 4 => (1 / 4 : ℝ)))
      (fun t => if t % 2 = 0 then M else N) := hUadm
  have hcU' : CoherentLift (0 : Fin 2) (fun _ => Matrix.of (fun _ _ : Fin 4 => (1 / 4 : ℝ)))
      (fun t => Matrix.diagonal (fun p : Fin 4 × Fin 2 => dd p ^ t)
        * (if t % 2 = 0 then M else N)) :=
    fun t => left_preserves_admissible (hL t) (hUadm t)
  have hMa0 : ∀ i j : Fin 4, M (i, 0) (j, 0) = 0 := by
    intro i j; simp [hMdef, hSWdef]
  have hMa1 : ∀ i j : Fin 4, M (i, 1) (j, 0) = P i j := by
    intro i j; simp [hMdef, hSWdef]
  have hNa0 : ∀ i j : Fin 4, N (i, 0) (j, 0) = P i j := by
    intro i j; simp [hNdef]
  have hNa1 : ∀ i j : Fin 4, N (i, 1) (j, 0) = 0 := by
    intro i j; simp [hNdef]
  have hent : ∀ (t : ℕ) (p : Fin 4 × Fin 2) (j : Fin 4),
      (Matrix.diagonal (fun q : Fin 4 × Fin 2 => dd q ^ t)
          * (if t % 2 = 0 then M else N)) p (j, 0)
        = dd p ^ t * (if t % 2 = 0 then M else N) p (j, 0) := by
    intro t p j; rw [Matrix.diagonal_mul]
  refine ⟨fun _ => Matrix.of (fun _ _ : Fin 4 => (1 / 4 : ℝ)),
    fun t => if t % 2 = 0 then M else N,
    fun t => Matrix.diagonal (fun p : Fin 4 × Fin 2 => dd p ^ t) * (if t % 2 = 0 then M else N),
    fun _ i j => rfl, hcU, hcU',
    (readback_of_coherentLift hcU).trans (readback_of_coherentLift hcU').symm, ?_, ?_, ?_⟩
  · funext i t
    ext j k
    rw [fibreCrossGram_apply, fibreCrossGram_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      hent t (i, 0) j, hent t (i, 1) j, hent (t + 1) (i, 0) k, hent (t + 1) (i, 1) k]
    rcases Nat.mod_two_eq_zero_or_one t with ht | ht
    · have ht1 : ¬ ((t + 1) % 2 = 0) := by omega
      simp only [if_pos ht, if_neg ht1, hMa0, hNa1, mul_zero, zero_mul, star_zero, add_zero,
        zero_add]
    · have ht0 : ¬ (t % 2 = 0) := by omega
      have ht1 : (t + 1) % 2 = 0 := by omega
      simp only [if_neg ht0, if_pos ht1, hMa0, hNa1, mul_zero, zero_mul, star_zero, add_zero,
        zero_add]
  · have h0 : (if (0 : ℕ) % 2 = 0 then M else N) = M := by norm_num
    rw [fibreCrossGram_apply, Fin.sum_univ_two, h0, hMa0, hMa1, hPdef]
    norm_num [Matrix.of_apply]
  · have h0 : (if (0 : ℕ) % 2 = 0 then M else N) = M := by norm_num
    rw [fibreCrossGram_apply, Fin.sum_univ_two, hent 0 (0, 0) 0, hent 0 (0, 1) 0,
      hent 2 (0, 0) 0, hent 2 (0, 1) 0, h0, hMa0, hMa1, hdddef, hPdef]
    norm_num [Matrix.of_apply, Complex.ext_iff]


/-! ### Section F — the two axis outcomes, reported as an ordered pair -/

/-- **`XS4` — THE `D`-AXIS OUTCOME IS `D-MID`.** A genuine intermediate readback datum exists, and
residual trajectory freedom remains at it. The named datum `F` — the **diagonal** entries of act
13's fibre cross-Gram at every time pair, the off-diagonal entries withheld — satisfies all three
frozen obligations of the refinement sandwich:

* **bounded above by act 13's level-2 datum**, universally on this carrier and anchor, for the full
  pair `D_F = (D₀, F)` and both components at once;
* **strictly above act 17's visible data**: two exhibited coherent lifts share the anchored readback
  and differ in `F`;
* **strictly below act 13's datum**: two exhibited coherent lifts share the anchored readback and
  `F`, while their level-2 data differ — **stated against act 13's level-2 datum and never against
  the trajectory**.

And the determination target **fails** at the same exhibited pair: the two lifts share the augmented
datum while their trajectories are inequivalent under `GramTrajEquiv`. **So the interval between act
17's visible data and act 13's datum is inhabited, and what inhabits it there does not determine the
trajectory.** This settles the named datum and is **not** a statement that no intermediate datum
determines it.

**The `L`-axis outcome is reported beside it and neither is above the other.** `P0` stays **OPEN**
and two-part. -/
theorem xs4_d_axis_mid :
    ∃ (F : (ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) → Fin 4 → ℕ → ℕ → Fin 4 → ℂ)
      (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (U₂ U₂' U₃ U₃' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      F = (fun U i t s j => FibreCrossGram (0 : Fin 1) U i t s j j)
        ∧ (∀ t i j, Γ t i j = 1 / 4)
        ∧ (∀ U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
            (∀ (i : Fin 4) (t s : ℕ),
                FibreCrossGram (0 : Fin 1) U i t s = FibreCrossGram (0 : Fin 1) U' i t s) →
            ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U t (i, a) (j, 0)‖ ^ 2)
                = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U' t (i, a) (j, 0)‖ ^ 2)
              ∧ F U = F U')
        ∧ CoherentLift (0 : Fin 1) Γ U₂ ∧ CoherentLift (0 : Fin 1) Γ U₂'
        ∧ ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U₂ t (i, a) (j, 0)‖ ^ 2)
            = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U₂' t (i, a) (j, 0)‖ ^ 2)
        ∧ F U₂ ≠ F U₂'
        ∧ CoherentLift (0 : Fin 1) Γ U₃ ∧ CoherentLift (0 : Fin 1) Γ U₃'
        ∧ ((fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U₃ t (i, a) (j, 0)‖ ^ 2)
            = fun (t : ℕ) (i j : Fin 4) => ∑ a : Fin 1, ‖U₃' t (i, a) (j, 0)‖ ^ 2)
        ∧ F U₃ = F U₃'
        ∧ ((fun i : Fin 4 => FibreCrossGram (0 : Fin 1) U₃ i 0 0)
            ≠ fun i : Fin 4 => FibreCrossGram (0 : Fin 1) U₃' i 0 0)
        ∧ ¬ GramTrajEquiv (fun t => FibreGram (0 : Fin 1) (U₃ t))
            (fun t => FibreGram (0 : Fin 1) (U₃' t))
        ∧ ¬ DeterminesTraj (0 : Fin 1) F := by
  obtain ⟨Γa, U₂, U₂', hΓa, hc₂, hc₂', hD₂, he₁, heᵢ⟩ := df2_above_visible
  obtain ⟨Γb, U₃, U₃', hΓb, hc₃, hc₃', hD₃, hf₃, hf₃', hne₃, htraj₃, hdet₃⟩ :=
    df2_below_level2_and_resid
  have hΓeq : Γa = Γb := by
    funext t; ext i j; rw [hΓa t i j, hΓb t i j]
  subst hΓeq
  refine ⟨_, Γa, U₂, U₂', U₃, U₃', rfl, hΓa, fun U U' h => ?_, hc₂, hc₂', hD₂, ?_,
    hc₃, hc₃', hD₃, ?_, hne₃, htraj₃, hdet₃⟩
  · exact ⟨(df_bounded_above (0 : Fin 1) U U' h).1, (df_bounded_above (0 : Fin 1) U U' h).2.2.1⟩
  · intro hEq
    have hent := congrFun (congrFun (congrFun (congrFun hEq 1) 0) 1) 1
    rw [he₁, heᵢ] at hent
    norm_num [Complex.ext_iff] at hent
  · exact funext fun i => funext fun t => funext fun s => funext fun j =>
      (hf₃ i t s j).trans (hf₃' i t s j).symm

end IntermediateCrossTimeStructure
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.IntermediateCrossTimeStructure.xs1_pointwise_factors
#print axioms OIBridge.IntermediateCrossTimeStructure.xs1_splice
#print axioms OIBridge.IntermediateCrossTimeStructure.xs1_pointwise_not_propagates
#print axioms OIBridge.IntermediateCrossTimeStructure.xs2_readback_factors_through_level2
#print axioms OIBridge.IntermediateCrossTimeStructure.readback_of_coherentLift
#print axioms OIBridge.IntermediateCrossTimeStructure.df_bounded_above
#print axioms OIBridge.IntermediateCrossTimeStructure.df1_above_visible
#print axioms OIBridge.IntermediateCrossTimeStructure.df2_above_visible
#print axioms OIBridge.IntermediateCrossTimeStructure.df2_below_level2_and_resid
#print axioms OIBridge.IntermediateCrossTimeStructure.df3_above_visible
#print axioms OIBridge.IntermediateCrossTimeStructure.lc0_pointwise_law
#print axioms OIBridge.IntermediateCrossTimeStructure.lc3_generator_law
#print axioms OIBridge.IntermediateCrossTimeStructure.xs5_l_axis_prop
#print axioms OIBridge.IntermediateCrossTimeStructure.lc2_regularity_law
#print axioms OIBridge.IntermediateCrossTimeStructure.prod_mem_unitaryGroup
#print axioms OIBridge.IntermediateCrossTimeStructure.prod_admissible
#print axioms OIBridge.IntermediateCrossTimeStructure.df1_below_level2
#print axioms OIBridge.IntermediateCrossTimeStructure.xs4_d_axis_mid
