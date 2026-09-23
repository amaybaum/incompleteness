# Act 18 — the intermediate regime: what extra structure supplies cross-time information: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
`fd3fa1359188966cae006deba4944a14aab5f3dd`, from the merge commit of that control plane,
`d7a9931befeb942db8ebc7b07014f9020c6663d0`, which the freeze fixes as this round's mandated base.

**The base-blob verification was this execution's first act, before any target was executed.** At
`d7a9931befeb942db8ebc7b07014f9020c6663d0`,
`git rev-parse d7a9931b:verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/preregistration.md`
returns `fd3fa1359188966cae006deba4944a14aab5f3dd`, which is the blob the freeze names. **The freeze
is intact and was consumed, never edited.**

**The headline is the ORDERED PAIR of two co-equal axis outcomes:** **(`D-MID`, `L-PROP`)**. The
`D`-axis reached its middle line and the `L`-axis reached its top line. **Neither axis is above the
other**, they answer different questions, an affirmative on one is not evidence about the other in
either direction, and no sentence of this note ranks them.

---

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`. It creates new seal state: a new Lean module
with new named results, and a new guard clause in `verification/lean/edge_rigidity_probe.py` under
the reserved tag **`R7-XTS`**, carrying the archive-mode constants this round owns. It lands
**`E` → `L` → `P`, with `P` mandatory**.

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_XTS_BASE` | the mandated execution base — the merge commit of the control plane | **set** to `d7a9931befeb942db8ebc7b07014f9020c6663d0` |
| `_XTS_SEALED_HEAD` | the sealed execution commit `E` | **present and unset**; set by `P` |
| `_XTS_MERGE` | the landing merge `L` carrying `E` as its second parent | **present and unset**; set by `P` |

**`_XTS_SEALED_HEAD` and `_XTS_MERGE` are unset at execution.** That is a statement about this
execution and stays true as one after the pin commit sets them. **No existing seal constant is
altered.** `_TRJ_*`, `_RNC_*`, `_TCF_*`, `_PQT_*`, `_CTI_*`, `_A12P_*`, `_SGT_*`, `_TSG_BASE` and
`_CLG_BASE` are **read and never written**: an archive seal belongs to the round that set it, and
touching the file that carries those constants does not make this round their owner. The execution's
diff against `edge_rigidity_probe.py` **adds** the `R7-XTS` clause and changes nothing else.

**Before certification this execution absorbed no later `main`.** No merge from `main`, no rebase,
no amend, no force-push; the branch is cut from the mandated base and from nothing else.

## 2. The frozen items, as honoured

- **The two candidate lists are unchanged and closed.** Three Type D candidates — `DF1`, `DF2`,
  `DF3` — and four Type L candidates — `LC0`, `LC1`, `LC2`, `LC3`. **No candidate discovered during
  execution was executed**, and none was added.
- **No candidate changed type.** Cross-time anchor coherence is reported as **two separate
  candidates**, `DF3` on the `D`-axis and `LC1` on the `L`-axis, and a verdict on one is not a
  verdict on the other in either direction.
- **Act 17's `GramTrajEquiv` was used and no other relation.** Raw Gram equality, uniform-phase
  equality and act 13's level-2 and level-3 relations were **not adopted**, and no relation of this
  round's own was defined.
- **Each countercontrol is either reached at the configuration this freeze names, or recorded as
  not reached with the obstruction named.** Section 13 records the one divergence of provenance.
- **No configuration was chosen after an outcome was known.** Every witness lives at the frozen
  configuration — act 12's Hadamard objects at `|V| = 4`, `a₀ = 0`, `Γ ≡ ¼` — at `|A| = 1`, or at
  `|A| = 2` where the countercontrol table places the obligation.

## 3. `XS0` — the bounded search, recorded in full

**Outcome reached: `XS0`-silent.**

> On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
> `verification/lean/`, every `preregistration.md` and `result.md` under
> `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
> the merged record decides nothing about a datum strictly between the anchored readback and act
> 13's level-2 datum, and nothing about whether a constraint writable from the anchor and the
> visible family alone is proper, non-trivial or propagating. **The finding is that the record is
> silent on the point.** It is not a finding that any such statement is false, not a finding that
> one is unprovable, and not a bound on what a later round could prove.

**`XS0` is a type-P target and carries no evidence level.** **No Lean was written for `XS0`**, no
outcome of it is a theorem of this round, and **this round's own theorems are not treated as
retro-evidence about it.**

**The file set, taken from `git ls-tree -r --name-only B`**: **226 files** — **170** `*.lean` under
`verification/lean-mathlib/`, **6** `*.lean` under `verification/lean/`, **49** `preregistration.md`
and `result.md` files under `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`.
Untracked package trees are outside the set by construction.

**The question asked of each hit**: does this declaration decide, for any datum strictly between the
anchored readback and act 13's level-2 datum, whether it determines the Gram/orbit trajectory — or
does it decide, for any constraint writable from `(a₀, Γ)` alone, whether that constraint is proper,
non-trivial or propagating?

| term | hits | files | recorded answer |
| --- | --- | --- | --- |
| `FibreCrossGram` | 52 | 10 | **Does not supply it.** Act 13's level-2 datum itself and its transformation laws; `fibreCrossGram_diag` fixes level 0 as its diagonal and `sum_fibreCrossGram` fixes level 1 as its fibre sum. Both are identifications of data, neither a determination verdict about anything between the two poles. |
| `CrossGram` | 204 | 13 | **Does not supply it.** The column cross-Gram and its anchored block — act 13's level 3 and level 1. Act 13 records which pairs *share* level 1, in the threading context; no statement says whether level 1 determines the Gram/orbit trajectory. |
| `GramTrajEquiv` | 75 | 5 | **Does not supply it.** Act 17's relation and its equivalence-relation lemmas, `TJ1`, `TJ3` and the `SP4` containment. `tj2f_sp4_containment` decides act 13's **level-2** datum, which is a pole and not an intermediate datum. |
| `RealizableGram` | 34 | 10 | **Does not supply it.** Act 12's per-slice characterization and its rank bound, pointwise in time. |
| `CoherentLift` | 357 | 91 | **Does not supply it.** The lift notion itself, `ℕ`-indexed and pointwise in time by definition. |
| `propagat` | 207 | 58 | **Does not supply it.** Every occurrence is corpus propagation under `§A.25`, or the propagation of a refutation along act 17's selector chain. **No occurrence is a cross-time law propagating one time from another.** |
| `transition` | 357 | 49 | **Does not supply it.** Act 17's `SP3` is a **transition rule read off a lift** and is refuted as a selector at one configuration; it is not a law written from `(a₀, Γ)` before any lift exists, and no properness, non-triviality or propagation verdict is recorded for it. |
| `generator` | 106 | 30 | **Does not supply it.** Generators of groups and of algebras elsewhere in the tree; no law of evolution on Gram/orbit trajectories. |
| `regular` | 51 | 21 | **Does not supply it.** Regularity of measures, of representations and of graphs; no regularity constraint on a trajectory. |
| `metric` | 197 | 62 | **Does not supply it.** Metrics on other objects entirely; no pseudometric on per-slice orbit classes and no bound on its steps. |
| `coarse` | 200 | 39 | **Does not supply it.** Coarseness of **quotients** — act 12's and act 13's relations compared with one another — never coarseness of **data**, and never an order on functionals of the lift. |
| `refine` | 1589 | 165 | **Not relevant to the question.** Overwhelmingly the Lean `refine` tactic. The prose uses are the same quotient-refinement comparisons as `coarse`. |
| `intermediate` | 87 | 26 | **Not relevant to the question.** Every occurrence is the **intermediate propagator / intermediate candidate** of acts 1 through 7 — a source-level object at an intermediate *time* — or `ROADMAP` text about an executable intermediate layer. **None is a datum between two data.** |
| `TJ1` | 116 | 5 | **Does not supply it.** The admissible set is the product over time of the per-slice realizable sets; the statement is about the **ambient set**, not about any datum inside the interval and not about any law. |
| `TJ3` | 80 | 5 | **Does not supply it.** Impossibility within a frozen four-member selector class at one configuration; the members read a lift and are not law data. |
| `CT2` | 105 | 16 | **Does not supply it.** Act 13's level-2 determination, at the far pole. |
| `CT3` | 233 | 18 | **Does not supply it.** The transformation laws and act 13's undecided fork `CT3` (d), which is about threading. |
| `SH1` | 210 | 19 | **Does not supply it.** The per-slice characterization at the near pole, pointwise in time. |
| `TG2` | 96 | 20 | **Does not supply it.** The per-slice two-sided orbit criterion. |
| `TG3` | 101 | 20 | **Does not supply it.** The Hadamard witness, existential about its own exhibited dilations. |
| `GL2` | 216 | 23 | **Does not supply it.** The threading mechanism, invisible to this round's relation by construction. |

**A search that finds a decision is a finding, and a search that does not is equally a finding.**
The second is what happened, and the finding is that the record is silent. **Reconstructive
inference is refused as a finding here**: no sentence of this note argues that the record must
contain something because otherwise something else would not have been written. **Searching and not
finding is never a settling outcome** for any Lean target of this round either.

**One property of the frozen file set is recorded rather than repaired.** The set is defined as
`git ls-tree -r --name-only B` restricted to the named paths, and **this round's own control plane
is inside it** by construction, being a `preregistration.md` under `verification/programmes/oi-qm/`
at `B`. Its hits are recorded as **not relevant to the question**: the freeze is this round's own
specification and is not a decision of the merged record. The boundary was fixed before the search,
and it is not moved now.

## 4. `XS1` — the factorization theorem for pointwise laws, which ran first

**Outcome reached: `XS1`-landed.**

> A law that is pointwise in this freeze's sense has a solution set equal to the **product over
> time** of its per-time solution sets, at evidence level 2, the ambient admissible set being a
> product by act 17's merged `TJ1`. **Any uniqueness such a law produces is slice-by-slice
> uniqueness and never a relation propagating one time from another**, and whenever two different
> allowed orbits survive at some later time, fixing the initial orbit cannot select between them
> through a pointwise law. **This is not the statement that no pointwise constraint yields
> cross-time determination**, which is false: a pointwise condition with a unique solution at every
> time determines the trajectory slice by slice, and what fails is propagation, not determination.
> **Every pointwise candidate is thereby ruled out as a route to the top line of the `L`-axis, as a
> theorem of this round and not as a failed search.** The exclusion is bounded to the notion of law
> this freeze defines and is not a statement about every conceivable pointwise condition, not a
> statement about laws on any other object, and not a bound on what a later round could prove under
> a different notion of law.

**The kernel carries three statements.** `xs1_pointwise_factors` is the factorization itself: the
per-time family is recovered, and an **arbitrary time-wise recombination** of solutions is a
solution, the value at each time drawn from a different solution. That is the product statement.
`xs1_splice` is the corollary. `xs1_pointwise_not_propagates` is the consequence:
`PointwiseLaw Law → ¬ PropagatesFrom a₀ Γ Law`, at every configuration.

**The `TJ1` dependence is named at the step and not in a footnote.** Intersecting a product
constraint with a **non-product** ambient set need not factor. The splice of two solutions is a
solution **of the law** immediately, by pointwiseness; it has to be **admissible** as well, and that
is exactly what act 17's `TJ1` supplies. In `xs1_splice` the two hypotheses are given as *coherent
lifts'* trajectories; `tj1_trajectory_set` converts them into the product form, the splice is formed
there, and `tj1_trajectory_set` converts back to produce a coherent lift of the spliced trajectory.
`xs1_pointwise_not_propagates` routes through `tj1_sufficiency` for the same reason. **Without `TJ1`
the corollary does not follow.** `TJ1` is consumed at merged strength and is neither enlarged nor
re-proved.

**The exhaustive argument over the two cases, and why one splice closes both.** The freeze's
argument splits on clause (ii) of propagation. If clause (ii) holds, two inequivalent orbit classes
survive at a time `t ≥ 1`, the splice is a pointwise realizable solution agreeing at time `0` and
inequivalent, and clause (i) fails. If clause (ii) fails, the law's later slices are fixed by the
per-time conditions alone and the initial orbit contributes nothing, so the law does not propagate
in the frozen sense. **Both cases are closed**, and the kernel statement closes them together:
`PropagatesFrom` is the **conjunction** of the two clauses, so refuting the conjunction by the
splice refutes exactly what the freeze's case split refutes, case by case.

**What `XS1` is NOT.** **"No pointwise constraint yields cross-time determination" is FALSE and is
not said here.** A pointwise `c_t` whose solution set at every `t` is a single orbit class
determines the trajectory outright, slice by slice, with no initial condition needed. **What fails
is propagation, not determination.** And `XS1` is **not** a no-go about this round's other
candidates: `LC1`, `LC2` and `LC3` are not pointwise, and `XS1` says nothing about them in either
direction. For `LC3` that is recorded as a kernel conjunct — `¬ PointwiseLaw Law` — obtained from
`XS1` itself against `LC3`'s propagation.

**And the pointwise law that determines slice by slice earns no line of the `L`-axis either**, for a
different reason: its solution set is a single class modulo `GramTrajEquiv`, so the
one-configuration non-triviality witness fails at its non-singleton clause. **That is a failure of
non-triviality and not a failure of determination.**

## 5. The well-posedness check, as it stood at execution

**`D₀` still factors through `D₂`, unconditionally, on the merged results the freeze names.** The
chain is the two merged steps the freeze records and it was re-run in the kernel as
`xs2_readback_factors_through_level2`:

1. act 13's `fibreCrossGram_diag` is a **definitional identity** — `Ξ_i^{(t,t)}(U) = G^{(i)}(U_t)`
   by `rfl` — so the level-2 datum contains the per-slice Gram tuple at every time;
2. act 12's `fibreGram_diag` gives the anchored readback from that tuple's diagonal **with no
   admissibility hypothesis at all**, so the readback is a function of the diagonal.

Composing: `D₂(U) = D₂(U') ⟹ D₀(U) = D₀(U')`, for arbitrary lifts, at any fixed anchor, with no
hypothesis on `Γ` and no appeal to coherence. **So obligation 1 is stated for the full pair
`D_F = (D₀, F)`**, both components at once, exactly as the freeze froze it; the fallback of stating
obligation 1 of `F` alone was not used. `df_bounded_above` carries obligation 1 for **all three**
Type D candidates in one theorem.

## 6. `XS2` — the three Type D parts, each with its frozen label

**Obligation 3 is stated against act 13's level-2 datum and NEVER against the trajectory.** A pair
with equal augmented datum and inequivalent trajectories is precisely a counterexample to the
determination target, so the trajectory phrasing is unsatisfiable exactly when the axis succeeds and
would make the top line unreachable **by construction, and silently**. What obligation 3 asks is
that the candidate be a **strict coarsening of act 13's datum** — that some level-2 difference be
invisible to it — which is a statement about the two data and not about the trajectories they
determine. **No statement of this round writes obligation 3 in the trajectory form.**

### `XS2` (a) — `DF1`, the adjacent-pair cross-Gram. Outcome: `DF1-SANDWICH`

> The candidate named `DF1` in this round's frozen list is a **genuine intermediate datum** at
> evidence level 2: equality of act 13's level-2 datum implies equality of the augmented datum,
> universally; two exhibited lifts share the anchored readback and differ in the augmented datum;
> and two exhibited lifts share the augmented datum and differ in the level-2 datum, the separating
> index and quantity named in each case. **So `DF1` sits strictly between act 17's visible data and
> act 13's datum.** This is a statement about the exact functional frozen under the label `DF1`, and
> **it does not endorse `DF1`, does not say the programme needs a datum of this shape, and does not
> adopt `DF1` as the physical carrier of cross-time information.**

- **Obligation 1** holds universally, by congruence on a restriction of act 13's datum together with
  the well-posedness chain (`df_bounded_above`). No countercontrol was needed and none is claimed.
- **Obligation 2** holds at the frozen configuration (`df1_above_visible`): the two **constant**
  coherent lifts `U ≡ H(1)` and `U' ≡ H(i)` of `Γ ≡ ¼` share the anchored readback, both being
  coherent lifts of the same visible family, and for a constant lift `Ξ_i^{(t,t+1)}` **is** the
  fibre-Gram tuple, which act 12's merged `hadamard_slices_not_twoSided` proves not even
  phase-equivalent — hence not equal.
- **Obligation 3** holds at `|A| = 2` (`df1_below_level2`), which is where the countercontrol table
  places it. Two coherent lifts of `Γ ≡ ¼` share the anchored readback and **every** adjacent-pair
  fibre cross-Gram — every adjacent cross-Gram is the **zero matrix** for both — while their
  level-2 data differ at the **non-adjacent** pair `(0, 2)`: at fibre `0` and column pair `(0,0)`
  the value is `¼` for one and `−¼` for the other. **The separating index and the separating
  quantity are named in the statement.** Section 13 records the divergence of provenance.
- **The determination target is UNDECIDED for `DF1`**, and neither label is claimed:
  > The obligation asked of `DF1` is undecided in this round, with the obstruction named
  > specifically — the candidate, the obligation, the step at which the proof stopped, and what
  > would settle it. Neither label is claimed, and no sentence of this round treats the absence of a
  > decision as a decision. In particular the absence of a counterexample is **not** reported as the
  > obligation holding, and the absence of a witness is **not** reported as there being none.

  **The obstruction, named.** The target is universal over **every** finite carrier, anchor, visible
  family and pair of lifts. At `|A| = 1` the adjacent-pair data recover the per-slice Gram tuple up
  to a positive scalar and the target would go through; at `|A| ≥ 2` the recovery argument fails and
  the merged record supplies no substitute, and no counterexample was constructed. **What would
  settle it** is either a universal proof of the recovery at arbitrary `|A|`, or an exhibited pair
  of lifts with equal anchored readback and equal adjacent-pair data whose trajectories are
  `GramTrajEquiv`-inequivalent. **The pair exhibited for obligation 3 is not such a pair**: its two
  lifts have **identical** fibre-Gram tuples at every time, so their trajectories are equal and it
  says nothing about determination.

### `XS2` (b) — `DF2`, the diagonal cross-time overlaps. Outcome: `DF2-SANDWICH` and `DF2-RESID`

> The candidate named `DF2` in this round's frozen list is a **genuine intermediate datum** at
> evidence level 2: equality of act 13's level-2 datum implies equality of the augmented datum,
> universally; two exhibited lifts share the anchored readback and differ in the augmented datum;
> and two exhibited lifts share the augmented datum and differ in the level-2 datum, the separating
> index and quantity named in each case. **So `DF2` sits strictly between act 17's visible data and
> act 13's datum.** This is a statement about the exact functional frozen under the label `DF2`, and
> **it does not endorse `DF2`, does not say the programme needs a datum of this shape, and does not
> adopt `DF2` as the physical carrier of cross-time information.**

> Two exhibited lifts share the augmented datum for `DF2` and their trajectories are **inequivalent
> under `GramTrajEquiv`**, at a named time and through a named invariant, at evidence level 2. **So
> `DF2` leaves residual trajectory freedom.** This settles the datum, not a neighbourhood of it, and
> it is not a statement that no datum of Type D determines the trajectory.

- **Obligation 1** holds universally (`df_bounded_above`), `F₂` being a restriction of act 13's
  datum.
- **Obligation 2** holds at the frozen configuration (`df2_above_visible`), at the entry the freeze
  names: the piecewise pair `U ≡ H(1)` against `U'` equal to `H(1)` at time `0` and `H(i)`
  afterwards, at fibre `1`, time pair `(0,1)`, column `1`, where the diagonal overlap is **`¼`** for
  the first lift and **`¼ i`** for the second.
- **Obligation 3** holds at the frozen configuration (`df2_below_level2_and_resid`): every anchored
  entry of `H(1)` and of `H(i)` has modulus `½`, so the diagonal cross-time overlap is the constant
  **`¼`** at every fibre, every time pair and every column for **both**, and the augmented datum
  agrees; while act 13's level-2 datum differs already at the time pair `(0,0)`, where
  `fibreCrossGram_diag` returns the fibre-Gram tuples act 12 proves inequivalent. **Stated against
  act 13's level-2 datum.**
- **The determination target fails at the same exhibited pair**: `¬ DeterminesTraj (0 : Fin 1) F₂`
  on that carrier, the separating time being `t = 0` and the separating invariant act 12's merged
  `∼_D`-invariant `G^{(0)}_{10} · G^{(1)}_{01}`, which is `1/16` for one and `i/16` for the other.
  **Withholding the off-diagonal entries withholds exactly the residual act 12's `SH1` identifies as
  the whole of the freedom after the two-sided gauge**, so the datum is informative across time and
  still does not determine the trajectory.

### `XS2` (c) — `DF3`, cross-time anchor coherence. Obligations 1 and 2 hold; obligation 3 UNDECIDED

- **Obligation 1** holds universally (`df_bounded_above`), `F₃` being the fibre sum of act 13's
  datum, which act 13's `sum_fibreCrossGram` identifies with the anchored block of the column
  cross-Gram.
- **Obligation 2** holds at the frozen configuration (`df3_above_visible`): the piecewise pair
  shares the anchored readback, and the anchored block at the time pair `(0,1)` is **`1`** at the
  entry `(1,1)` for the first lift and **`(1 + i)/2`** for the second. The separating index and
  quantity are named in the statement.
- **Obligation 3 is UNDECIDED**, which the freeze rates as an allowed outcome and expects:
  > The obligation asked of `DF3` is undecided in this round, with the obstruction named
  > specifically — the candidate, the obligation, the step at which the proof stopped, and what
  > would settle it. Neither label is claimed, and no sentence of this round treats the absence of a
  > decision as a decision. In particular the absence of a counterexample is **not** reported as the
  > obligation holding, and the absence of a witness is **not** reported as there being none.

  **The obstruction, named.** Obligation 3 needs a pair of lifts agreeing on the **fibre sum** of
  act 13's datum while differing **fibre by fibre**, with the visible family held equal. **The
  freeze names no construction for it and the merged record supplies none**: the fibre sum is
  constrained by unitarity of the anchored columns — it is the anchored block of `U_tᴴ U_s` — and
  nothing merged bounds how much per-fibre freedom survives at a fixed fibre sum. **What would
  settle it** is either such an exhibited pair, or a universal proof that the fibre sum recovers the
  per-fibre data at equal visible family, which would be `DF3-NOT-BELOW`. Neither was reached and
  neither is claimed. **The determination target for `DF3` is likewise UNDECIDED**, on the same
  obstruction.
- **No outcome of `DF3` resolves, reopens or narrows act 10's anchor-axis reclassification**, in
  either direction. The datum is defined only relative to the anchoring convention and its very
  statement moves if the convention moves; freezing it as a candidate is how this round asks whether
  cross-time anchor coherence is the intermediate datum, **without** asserting anything about the
  anchor axis.

### What no `XS2` verdict establishes

**A verdict on one candidate is not a verdict on another.** An `X-SANDWICH` is **not** an
endorsement: it says the datum sits in the interval, and says nothing about whether it is the right
datum. An `X-RESID` settles the exact frozen functional and nothing in its neighbourhood.
**Naming a candidate is not endorsing it.**

## 7. `XS3` — the four Type L parts, each with its frozen label

**Every non-triviality witness below is at ONE COMMON CONFIGURATION and carries all four conjuncts
together**: `Law(C, G₁) ∧ Law(C, G₂) ∧ G₁ ≉_O G₂ ∧ ¬Law(C, H)`, with `G₁`, `G₂` and `H` **all three
pointwise realizable there**. Split-configuration witnesses were refused, and the reason is the one
the freeze records: a law permitting everything at one configuration and exactly one trajectory at
another passes both separated tests while being **vacuous at the first** and **the answer in
disguise at the second**, and neither failure is visible to either separated test.

**`H`'s pointwise realizability is load-bearing and is available only because of act 17's `TJ1`.**
The properness clause has to exhibit a trajectory the law excludes **from inside** the admissible
set; a trajectory excluded because it is not admissible at all would prove nothing about the law.

**Both propagation clauses are reported separately, and the two non-propagation mechanisms are kept
apart.** `Y-RESID` — two solutions agree at time `0` and are `≈_O`-inequivalent — and
`Y-DEGENERATE` — the law fixes every slice from `t = 1` on by itself, so the initial orbit
contributes nothing — are **distinct outcomes**, and reporting one as the other is a defect of this
round. **No `Y-DEGENERATE` was reached by any candidate**, and none is claimed.

### `XS3` (a) — `LC0`, the pointwise admissibility law. Outcome: `LC0-WELLDEF`, `LC0-PROPER`, `LC0-RESID`, and EXCLUDED from `L-PROP` by `XS1`

> At one exhibited configuration the law `LC0` prescribes has a solution set that is **nonempty**,
> **non-singleton modulo `GramTrajEquiv`** and **proper**, all three witnessed together by three
> pointwise realizable trajectories named in the statement, at evidence level 2. **So `LC0` is a
> genuine proper constraint there**, neither vacuous nor the trajectory in disguise. This settles
> **one configuration** and is not a statement about every configuration, and it does **not** endorse
> `LC0`, does **not** say a law of this shape is required, and does **not** adopt it.

> Two exhibited pointwise realizable solutions of the law `LC0` prescribes agree at time `0` and
> their trajectories are **inequivalent under `GramTrajEquiv`**, at a named time and through a named
> invariant, at evidence level 2. **So residual histories remain after the initial orbit is fixed**
> and the law plus one initial orbit does not propagate uniquely. It settles that law and nothing in
> its neighbourhood, and it is **not** the outcome in which the initial orbit does no work; the two
> mechanisms are kept apart.

**The law datum** is the pair of per-slice orbit classes `[G(H(1))]`, `[G(H(i))]` at the frozen
configuration, and the law admits a trajectory iff each of its slices lies in one of the two. **It
consults no lift at any point.** Orbit-level well-definedness is discharged in the kernel:
`GramPhaseEquiv` is an equivalence relation, so membership in a class is invariant.

**The one-configuration witness**: `G₁` constant at `[G(H(1))]`, `G₂` constant at `[G(H(i))]`, both
pointwise realizable by act 12's merged `sh1_necessity`, both solutions, inequivalent by act 12's
merged `∼_D`-invariant; and `H` constant at `[G(H(−1))]`, the **third member of act 12's own frozen
family `H(z)`**, pointwise realizable and excluded. The three classes are separated by that same
invariant, whose value on `H(z)` is `z/16`: `1/16`, `i/16` and `−1/16`.

**`LC0` is excluded from the top line of the `L`-axis as a theorem of this round**, under `XS1` and
under `XS3` (a), and **never as an undecided line**: `xs1_pointwise_not_propagates` applied to the
pointwise law `LC0` prescribes gives `¬ PropagatesFrom`. **The exclusion does not by itself earn
`L-NOGO`**, which quantifies over the whole four-member list.

**And the mechanism is exhibited rather than only derived**: the splice of the two constant
solutions at time `1` is a pointwise realizable solution agreeing with `G₁` at time `0` and
inequivalent to it, which is clause (i) failing, exhibited. Clause (ii) holds at the same
configuration, both constant classes being solutions at every time. **So `LC0` earns the middle rung
`L-PROPER` on its own merits**, by the `Y-RESID` mechanism and not by the `Y-DEGENERATE` one.

### `XS3` (b) — `LC1`, cross-time anchor coherence as a law. Outcome: UNDECIDED

> The obligation asked of `LC1` is undecided in this round, with the obstruction named specifically
> — the candidate, the obligation, the step at which the proof stopped, and what would settle it.
> For the generator law the descent obligation is named where it is the obstruction, and **no verdict
> about propagation is recorded where the descent is not discharged.** Neither label is claimed, and
> no sentence of this round treats the absence of a decision as a decision.

**The obstruction, named.** The countercontrol the freeze names takes `C_t := 1` at every `t`, with
`G₁` and `G₂` the two constant Hadamard trajectories, each realized by a constant lift whose
anchored coherence is the identity; and `H` the alternating trajectory, **excluded if no admissible
representatives give the identity**. That conditional is the obstruction and the freeze names it as
one. **The properness clause requires a universal statement over all admissible dilations realizing
the alternating classes** — that none of them has anchored cross-time coherence equal to the
identity — and **no merged result decides it**. Nothing was proved and nothing is claimed: no
`LC1-PROPER`, no `LC1-VACUOUS`, no `LC1-SINGLE`, and **no propagation verdict whatever**. **No Lean
was written for `LC1`**, so it carries no line in the axiom table. **What would settle it** is a
universal kernel proof over the admissible representatives at that configuration, in either
direction.

**No outcome of `LC1` resolves, reopens or narrows act 10's anchor-axis reclassification**, in
either direction, and **the `LC1` verdict is not a verdict on `DF3`** — they are different
propositions with different obligations on different ladders, and neither is evidence about the
other.

### `XS3` (c) — `LC2`, regularity in a named Gram pseudometric. Outcome: `LC2-WELLDEF`, `LC2-PROPER`, `LC2-RESID`

The two frozen sentences for `Y-PROPER` and `Y-RESID` are carried for `LC2` exactly as they are
carried for `LC0` above, with `LC2` in place of `LC0`.

**The pseudometric is named explicitly in the statement** and is written from the Gram data alone:
`d(G, G') = ‖G⁰₁₀ · G¹₀₁ − G'⁰₁₀ · G'¹₀₁‖`, the modulus of the difference of act 12's merged
`∼_D`-invariant. Its three pseudometric properties are proved, and its **`∼_D`-invariance** is
proved from `gramPhaseEquiv_cross_invariant`, which is what makes it a pseudometric on **orbit
classes** rather than on representatives. The bound is `ε_t = 0`, which is below the distance
between the two classes the countercontrol names. **The verdict is about that named `d`**, not about
regularity in general: a failure of `LC2` as stated would not be a refutation of regularity in
general, and no such sentence appears.

**Nothing here imports continuity, differentiability or a limit.** `ℕ` carries successor and order
and nothing else, and `d` is a pseudometric on the **value** space, never on the index.

**The one-configuration witness**: `G₁` and `G₂` the two constant Hadamard trajectories, both with
zero steps, inequivalent; `H` the alternating trajectory, pointwise realizable, whose first step has
positive length and is excluded.

**Propagation clause (i) fails, exhibited**: the constant trajectory at `[G(H(1))]` against the
trajectory that stays at `[G(H(1))]` at time `0` and moves at the first step to the class of
`H(1)` **with its last two columns interchanged** — a fourth admissible dilation of the same visible
family, with the **same** value of the named pseudometric's invariant, so every step has length `0`
and the law is satisfied, while the two classes are `∼_D`-inequivalent, certified through the same
merged invariant read at the fibre pair `(0,2)` instead of `(0,1)`, where the values are `1/16` and
`−1/16`. **Propagation clause (ii) holds**, exhibited at `t = 1` by the two constant trajectories.
**So residual histories remain after the initial orbit is fixed**, and this is the `Y-RESID`
mechanism and **not** the `Y-DEGENERATE` one.

### `XS3` (d) — `LC3`, the generator law. Outcome: descent DISCHARGED, `LC3-WELLDEF`, `LC3-PROPER`, `LC3-PROPAGATES`

> Given the non-triviality witness, **both** propagation clauses hold at evidence level 2: two
> pointwise realizable solutions of the law `LC3` prescribes that agree at time `0` have the same
> trajectory under `GramTrajEquiv`, proved universally; and the law without the initial orbit fixed
> leaves two inequivalent orbit classes at an exhibited time after the initial one, so **the initial
> orbit does work**. **So the law plus one initial orbit propagates uniquely.** That is what a law of
> evolution does and it is not a cheat here, the law datum being writable from the anchor and the
> visible family before any lift exists. **This is a statement about the exact law frozen under the
> label `LC3`**: it does **not** endorse it, does **not** say such a law obtains, does **not** adopt
> any carrier or principle as the physical one, and does **not** close `P0` or either of its parts.

**The descent obligation is DISCHARGED, by the first of the two routes the freeze permits.** The
candidate is **written directly as an orbit-level transition** `[G_{t+1}] = Φ([G_t])`, with `Φ` the
identity on per-slice orbit classes, rather than as a representative-level `V_t` that would then
have to be proved gauge-natural. The kernel carries the descent as its own conjunct: the transition
relation is invariant under `∼_D` in **both** arguments, so it is a relation on classes and not on
representatives. **A representative-level generator that did not descend would "select" by fixing an
unphysical frame**, which is the failure the obligation exists to prevent; the route taken avoids it
by construction, so the gauge-naturality machinery of acts 11 and 12 — `fibreGram_left_mul`,
`fibreGram_mul_weak_apply` and act 11's orbit theorem — was **not** rebuilt and **not** needed, and
nothing of it is restated here.

**The one-configuration witness**: `G₁` and `G₂` the two constant Hadamard trajectories, both
solutions of `[G_{t+1}] = [G_t]`, inequivalent; `H` the trajectory that changes class at the first
step, pointwise realizable and excluded because the identity transition forbids a change of class.

**Propagation clause (i)**, proved **universally** over the pointwise realizable solutions: a
solution's class is constant in time by induction along the transition, so two solutions agreeing at
time `0` agree at every time. **Propagation clause (ii)**, exhibited: at `t = 1` the solutions taken
without the initial orbit fixed occupy the two inequivalent constant classes, **so the initial orbit
does work** and what is reported is propagation and not slice-by-slice determination.

**`LC3` is not pointwise**, and the kernel records it: `¬ PointwiseLaw Law`, obtained from this
round's own `XS1` against `LC3`'s propagation. **So `XS1` says nothing about `LC3` in either
direction.**

**This candidate's stationary instance is the same proposition act 17 refuted as a SELECTOR**
(`SP2-ADD`, `SP2-NOSEL`), **and the two verdicts are consistent**: act 17 showed it is additional
structure that does not select from the visible family alone, and this round asks what it does as
additional structure **with an initial orbit supplied**. Act 17's verdicts are neither weakened,
qualified nor revised by this.

### What no `XS3` verdict establishes

**A verdict on one candidate is not a verdict on another.** A `Y-PROPAGATES` is **not** an adoption
and is **not** a claim that the law obtains: it says what imposing that law leaves. A `Y-VACUOUS` or
`Y-SINGLE` would be a verdict at the **named** configuration and not a statement about every
configuration; **neither was reached by any candidate here**, and neither is claimed.

## 8. `XS4` and `XS5` — the two axis outcomes, reported as an ORDERED PAIR

**The outcome of this round is the ordered pair `(D-MID, L-PROP)`.** The two axes answer different
questions and **neither is above the other**; an affirmative on one is not evidence about the other
in either direction; neither element is "the" answer and neither is a fallback for the other. The
two clauses appear in the order readback-then-law throughout, **which is an ordering of the sentence
and not a ranking of the axes**.

### `XS4` — the `D`-axis. Outcome: `D-MID`

> **A genuine intermediate readback datum exists, and residual trajectory freedom remains.** The
> named datum satisfies all three frozen obligations, and two exhibited lifts share it while their
> trajectories are inequivalent under `GramTrajEquiv`, at evidence level 2. **So the interval
> between act 17's visible data and act 13's datum is inhabited, and what inhabits it there does
> not determine the trajectory.** This settles the named datum and is not a statement that no
> intermediate datum determines it. **The `L`-axis outcome is reported beside it and neither is
> above the other.** `P0` stays **OPEN** and two-part.

**Earned by `DF2`**, which carries `DF2-SANDWICH` and `DF2-RESID`, both at evidence level 2, and
assembled as one object in `xs4_d_axis_mid`. `DF1` also reached `DF1-SANDWICH`, which is a second
inhabitant of the interval; its determination target is UNDECIDED, so it does not by itself settle
the axis in either direction, and the axis line is stated from `DF2`. **`D-DET` was not reached and
is not claimed. `D-NOGO` was not reached and is not claimed** — it would require an exhibited
failure of obligation 2 or of obligation 3 for **every** member of the three-member list, and the
round exhibits failures for none.

### `XS5` — the `L`-axis. Outcome: `L-PROP`

> **A genuine proper structural law, together with one initial orbit, propagates uniquely.** The
> named law is written from the anchor and the visible family alone, before any lift is chosen;
> it respects `GramTrajEquiv`; its solution set at one exhibited configuration is nonempty,
> non-singleton modulo `GramTrajEquiv` and proper, all three witnessed together; two solutions
> agreeing at time `0` have the same trajectory; and the law without the initial orbit fixed leaves
> two inequivalent orbit classes at an exhibited time after the initial one, **so the initial orbit
> does work and what is reported is propagation and not slice-by-slice determination**. At evidence
> level 2. **That a law of evolution
> determines a history given an initial condition is what such a law is**, and it is legitimate here
> because the law datum is writable before any lift exists. **This is a statement about the exact
> law this freeze names and about nothing else**: it does not say the law obtains, does not adopt
> it, does not say the programme requires one, and does not close `P0` or either of its parts.
> **The `D`-axis outcome is reported beside it and neither is above the other.** `P0` stays
> **OPEN** and two-part, its threading part is untouched, and no carrier is adopted as the physical
> one.

**Earned by `LC3`**, with `LC3-WELLDEF`, `LC3-PROPER` and `LC3-PROPAGATES` all at evidence level 2
and with the descent obligation discharged, assembled as one object in `xs5_l_axis_prop`. `LC0` and
`LC2` each reached the middle rung `L-PROPER` on their own merits, by the `Y-RESID` mechanism;
neither is reported as the axis outcome and neither is a fallback. **`L-NOGO` was not reached and is
not claimed** — it quantifies over the whole closed four-member list, and `LC0`, `LC2` and `LC3` are
each proper there.

## 9. `P-D` — the frozen structural prediction, reported against

**`P-D` predicts that any `F` reaching the top line of the `D`-axis discards, relative to act 13's
datum, precisely threading and representative information and nothing else.**

**No candidate reached the top line of the `D`-axis.** `D-DET` requires a named candidate with
`X-SANDWICH` **and** `X-DET`, and no `X-DET` was proved: `DF2`'s determination target **fails**
(`DF2-RESID`), and `DF1`'s and `DF3`'s are **UNDECIDED**. **So `P-D`'s antecedent is not instantiated
by anything in this round, and the prediction is neither confirmed nor falsified.** It is reported
as **not exercised**, and no sentence here treats a vacuous antecedent as a confirmation.

**The falsification condition was not met, and is restated so the record is complete.** `P-D` is
falsified by an exhibited `F` on this freeze's list that reaches the top line of the `D`-axis
**together with** an exhibited obligation 3 witness pair whose two lifts are **not** two-sided
related at every time. **No such `F` was exhibited**, so no such pair was sought and none is
reported. Had one been found, the result note would have said in terms which merged statement the
freeze misread — the pair would contradict act 12's merged `twoSidedRelated_iff` — and **would not
have presented the falsification as a finding about nature.**

**One observation is recorded and is explicitly not evidence for `P-D`.** For `DF2`, the exhibited
obligation 3 pair is the two constant Hadamard lifts, which act 12's merged
`hadamard_slices_not_twoSided` proves are **not** two-sided related. That is not a falsification of
`P-D`, because `DF2` does **not** reach the top line — its determination target fails — and `P-D`
speaks only of candidates that do. **The two are not conflated.**

## 10. The non-adoption clause, carried verbatim at each mention

**THE CLAUSE is carried at every place where a candidate's survival could be read as its adoption.**
**Five carriages in all**: **four** in this result note and **one** in the module docstring. Each
carriage opens with **its own naming line, distinct per carriage and placed as the first line inside
the block quote**, contiguous with the body, so that the carriages read as distinguishable copies of
one clause rather than as one paragraph pasted repeatedly.

**Two kinds of mention do not admit an inserted block quote and are governed by the freeze's section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed post-round
sentences of the status rule and of the `P0` row, which carry the clause's substance in their own
frozen wording and cannot admit a quotation inside a quotation; and the bare list entries that do
nothing but name a candidate among the candidates this round tests.

**The `ROADMAP` carries no inserted carriage, and that is the freeze's own rule and not an
omission.** The freeze writes the `ROADMAP` **only** by appending the frozen post-round sentence for
the case reached, with the `P0` row's label unchanged, and that sentence is one of the two kinds of
mention just named: it is byte-fixed, it carries the clause's substance in its own frozen wording —
*"it is not an assertion that the law obtains, not an adoption of it, and not a claim that the
programme requires one"*, and *"no carrier is adopted as the physical one"* — and it cannot admit a
quotation inside a quotation.

**The `L`-axis reached its top line, which is the place the hazard is strongest.**
> **THE CLAUSE, carried at this mention — the result note's report of the `L`-axis top line.**
> Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
> either axis is a statement about the exact structure this freeze names, on the data grant frozen
> for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
> programme requires it, and **not** an adoption of it as the physical carrier of cross-time
> information. A datum that determines the trajectory does not thereby become the right datum, and a
> law whose solutions at a configuration are one history is not thereby the law of evolution: the
> refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
> `L`-axis exist because a structure can reach a top line by containing the answer rather than by
> supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
> adopted as the physical one, and no candidate changes type during execution.**

**Two Type D candidates survived the refinement sandwich, and surviving is not standing.**
> **THE CLAUSE, carried at this mention — the result note's report of the surviving readback data.**
> Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
> either axis is a statement about the exact structure this freeze names, on the data grant frozen
> for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
> programme requires it, and **not** an adoption of it as the physical carrier of cross-time
> information. A datum that determines the trajectory does not thereby become the right datum, and a
> law whose solutions at a configuration are one history is not thereby the law of evolution: the
> refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
> `L`-axis exist because a structure can reach a top line by containing the answer rather than by
> supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
> adopted as the physical one, and no candidate changes type during execution.**

**The strongest hazard the freeze names is a candidate that reaches a top line by containing the
answer**, and the two obligations that exist to catch it were discharged before either axis line was
stated.
> **THE CLAUSE, carried at this mention — the result note's account of the freeze's strongest hazard.**
> Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
> either axis is a statement about the exact structure this freeze names, on the data grant frozen
> for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
> programme requires it, and **not** an adoption of it as the physical carrier of cross-time
> information. A datum that determines the trajectory does not thereby become the right datum, and a
> law whose solutions at a configuration are one history is not thereby the law of evolution: the
> refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
> `L`-axis exist because a structure can reach a top line by containing the answer rather than by
> supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
> adopted as the physical one, and no candidate changes type during execution.**

**No candidate is adopted, endorsed or given physical status by surviving.** Nothing in this round
says that extra cross-time structure is required, on any carrier or carrier-free.

## 11. What no outcome licenses, in the freeze's own wording

1. **"The trajectory freedom is gauge", or "the trajectory freedom is physical."** Not written. Act
   14's status rule that there is no carrier-free verdict binds this round too; this round adopts no
   carrier and defines none of its own.
2. **"The datum that works is the physical one", or "this is the law of nature."** Not written. THE
   CLAUSE governs and is carried at four places in this note.
3. **"No pointwise constraint yields cross-time determination."** Not written, and the sentence is
   **false**. `XS1` does not say it: a pointwise condition with a unique solution at every time
   determines the trajectory slice by slice. **What fails is propagation, not determination.**
4. **"`XS1` rules out cross-time laws."** Not written. `XS1` is bounded to pointwise laws in this
   freeze's sense, and `LC1`, `LC2` and `LC3` are not pointwise.
5. **"Same augmented datum, inequivalent trajectories" reported as obligation 3.** Not written.
   Obligation 3 is *same augmented datum, different level-2 datum*, everywhere in this note and in
   the module.
6. **"The candidate list is exhaustive", or "these are the intermediate structures."** Not written.
   Three Type D and four Type L propositions were tested and the lists are closed, not exhaustive.
7. **"The coarsest determining datum is …", or any lattice statement about the space of data.** Not
   written. The question is explicitly out of scope by the freeze's own non-doing, and **no
   comparison between the intermediate data this round found was undertaken**: `DF1` and `DF2` both
   reached `X-SANDWICH` and **neither is reported as finer, coarser, better or preferable to the
   other**.
8. **"One axis answers the other", or any ranking of the two axes.** Not written. The outcome is the
   ordered pair and neither element is a fallback for the other.
9. **"The bounded no-go shows no such structure exists."** Not written; no bounded no-go was earned
   on either axis, and none is claimed.
10. **"A witness was sought and not found, so there is none."** Not written. Every UNDECIDED here is
    reported as UNDECIDED with the obstruction named, and no search is presented as exhaustive.
11. **Any statement about the threading, the cross-time representative, the relative evolution or
    the relative candidate.** Not written. These are invisible to `GramTrajEquiv` by construction,
    and a round that cannot see a distinction may not report one.
12. **Any statement about act 16's cancellation cell**, in either direction, and any reading of act
    16's `RN3⁺` or act 15's `PQ3-d⁺` as bearing on trajectory freedom. Not written; **neither is
    consumed anywhere in this round, in any proof or in any determination.**
13. **Any statement about act 14's four carriers**, or any adoption of a carrier. Not written. This
    round defines no carrier and reads none.
14. **"Act 10's anchor axis is resolved", or "reopened", or "narrowed."** Not written. `DF3` and
    `LC1` are grounded in act 10's reclassification and bear on it in neither direction.
15. **"`P0` is closed", or "`P0`'s trajectory part is closed."** Not written. The row stays **OPEN**
    and two-part.
16. **"Act 13's level-2 result is strengthened", or "act 17's `TJ1` is enlarged."** Not written.
    Both are consumed at merged strength; **a merged statement is not enlarged by being consumed.**
17. **"The trajectory is continuous", "smooth", "generated by a Hamiltonian".** Not written.
    `CoherentLift` is `ℕ`-indexed and this round does not change that; `LC2`'s pseudometric is on the
    value space and never on the index.
18. **"OI and QM are inequivalent."** Not written. Two lifts differing is not two theories
    differing, and every visibility statement here is under act 7's own readback convention with
    `D4b` **negative**.
19. **Any sentence about Track I**, or about Source B or Source C. Not written. **Only Source A is
    adjudicated**, and Track I is not touched in either direction.
20. **Any import from the substratum Lemma 24.1 rounds.** Not written; nothing is consumed or
    compared, and a shared word is not a bridge.

> **THE CLAUSE, carried at this mention — the result note's list of what no outcome licenses.**
> Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
> either axis is a statement about the exact structure this freeze names, on the data grant frozen
> for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
> programme requires it, and **not** an adoption of it as the physical carrier of cross-time
> information. A datum that determines the trajectory does not thereby become the right datum, and a
> law whose solutions at a configuration are one history is not thereby the law of evolution: the
> refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
> `L`-axis exist because a structure can reach a top line by containing the answer rather than by
> supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
> adopted as the physical one, and no candidate changes type during execution.**

**No outcome chose its own wording, and no target is reported at a strength the kernel does not
carry.** Every target above is reported in the sentence the freeze fixes for the outcome reached.
**The anti-contamination invariant is honoured**: sibling results present at the mandated base are
not inputs, and nothing outside the freeze's start-state table is read, cited, compared or waited
for by any target of this round.

### The freeze's thirty named hazards, each checked

1. **A candidate that reaches a top line by containing the answer.** Did not occur; THE CLAUSE is
   carried at four places in this note, once in the module docstring and once in the `ROADMAP`.
2. **Obligation 3 restated against the trajectory.** Did not occur; it is stated against act 13's
   level-2 datum everywhere.
3. **A candidate changing type mid-execution.** Did not occur; `DF3` and `LC1` are reported as two
   separate candidates on two separate ladders.
4. **Split-configuration non-triviality.** Did not occur; every witness carries all four conjuncts
   at one configuration.
5. **A properness witness outside the admissible set.** Did not occur; `H`'s pointwise realizability
   is a conjunct of `ProperAt` in every instance.
6. **A generator law that does not descend.** Did not occur; `LC3` is written at orbit level and the
   descent is a kernel conjunct.
7. **Reading `XS1` as a no-go about determination.** Did not occur; the false sentence is refused in
   terms, in the module docstring and here.
8. **Reporting a degenerate propagation as propagation.** Did not occur; clause (ii) is proved
   separately in every propagation verdict, and no `Y-DEGENERATE` is reported anywhere.
9. **Forgetting that `XS1` needs `TJ1`.** Did not occur; `TJ1` is applied at the admissibility step
   in `xs1_splice` and again in `xs1_pointwise_not_propagates`.
10. **Ranking the two axes.** Did not occur; the headline is the ordered pair.
11. **Treating an undischarged obligation as discharged because no counterexample was found.** Did
    not occur; `DF3`'s obligation 3 and `LC1`'s properness are reported UNDECIDED.
12. **Enlarging a bounded no-go.** Did not occur; no no-go was earned and none is claimed.
13. **Letting the lattice question creep in.** Did not occur; the two surviving Type D data are not
    compared with each other in any respect.
14. **Consuming act 13's level-2 result at more than merged strength.** Did not occur; `CT2` (b) is
    cited only as the far pole of the interval and is applied in no proof.
15. **Consuming act 17's `TJ1` or `TJ3` at more than their strength.** Did not occur; `TJ1` is
    applied as the product characterization it is, and `TJ3` is not applied at all.
16. **Seeing the threading.** Did not occur; act 11's `GL2` pair is **one** trajectory here and this
    round says nothing about the difference.
17. **Reading raw Gram equality or act 13's relation as this round's relation.** Did not occur;
    `GramTrajEquiv` is consumed and not redefined and is the only relation any quotient is over.
18. **Touching act 16's cancellation cell or the threading question.** Did not occur.
19. **Reading a `DF3` or `LC1` outcome as an anchor-axis finding.** Did not occur.
20. **Importing time structure the index type does not have.** Did not occur.
21. **Choosing a configuration after an outcome is known.** Did not occur; section 13 records the
    one divergence of **provenance** within a named configuration, and no alternative witness was
    substituted for a named one.
22. **Treating the `|A| = 1` case as automatically the right one for a cross-time statement.** Did
    not occur; `DF1`'s obligation 3 was executed at `|A| = 2` exactly because of the collapse the
    freeze records.
23. **A reader supplying a missing theorem from background knowledge.** Did not occur; every step is
    a merged result or a theorem of this module.
24. **Forgetting the anchor, and forgetting the rank bound.** Did not occur; the anchor is carried in
    every statement and act 12's rank bound is consumed inside `RealizableGram` and never dropped.
25. **Consuming a sibling round's result because it is present at the mandated base.** Did not occur.
26. **Importing the substratum Lemma 24.1 rounds' vocabulary.** Did not occur.
27. **A landing without `P`.** Not applicable at execution; the round is declared SEALING and `P` is
    mandatory, and the guard clause is written so that it passes both before and after `P`.
28. **A chronology guard that certifies only the head.** Did not occur; the strong predicate
    enumerates `git rev-list H ^B` and requires every commit to descend from `B`.
29. **A chronology guard that fixes this round's own pins at `None` for all time.** Did not occur;
    clause 9 is honoured **by exclusion**, and the exclusion was verified empirically — section 14.
30. **Editing this freeze after an outcome is known.** Did not occur; the preregistration is
    byte-identical to the blob the freeze names and nothing in this round writes to it.

## 12. The relation to acts 7, 10, 11, 12, 13, 14, 15, 16 and 17 — every merged label consumed, none revised

`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`, `AB0`,
`AB1`, `AB2`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`–`PQ4`, `CF0`–`CF5`, `RN0`–`RN4` and
`TJ0`–`TJ3` are consumed and **none is revised**. Act 13's fork `CT3` (d) stays UNDECIDED and is
untouched.

**The merged results actually applied in the module**, by reading the proof of every named result:
act 12's `sh1_necessity`, `fibreGram_apply`, `fibreGram_diag`, `gramPhaseEquiv_cross_invariant`,
`hadamard_slices_not_twoSided`, `left_preserves_admissible` and `star_mul_self_eq_norm_sq`; act 13's
`fibreCrossGram_apply` and `fibreCrossGram_diag`; and act 17's `GramTrajEquiv`,
`gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans`, `tj1_sufficiency` and
`tj1_trajectory_set`. **Nothing from acts 14, 15 or 16 is applied in any proof here.**

**Act 13's level-2 result is consumed at merged strength**: `CT2` (b) is a both-directions statement
about the fibre cross-Gram trajectory and the threading residual, and it is cited as the far pole of
the interval and as the reason obligation 1 bounds every Type D candidate from above. It is **not
re-proved and not strengthened**, and it is not cited as though it quantified over data it does not
mention.

**Act 17's `TJ1` and `TJ3` are consumed at merged strength.** `TJ1` is about `CoherentLift` as the
programme defines it; `TJ3-IMP` is impossibility within a four-member class at one configuration.
Neither is a universal statement about structures, and neither is read as one. **Act 17's
`GramTrajEquiv` is consumed and not redefined**, and act 12 supplies the per-slice `GramPhaseEquiv`
it is built on.

## 13. Discrepancies — recorded and NOT repaired

**The preregistration is immutable once merged.** An execution that diverges records the discrepancy
and does not repair the freeze. **Four items are recorded. None is repaired, and the freeze is not
edited.**

**No start-state discrepancy arose.** All **twenty-eight** blobs the freeze pins at the mandated base
— the twenty-four read-only entries and the four writable ones — were verified and **every one
matches**, including `verification/ROADMAP.md` at `c69987e9eb8080efce0d2a61120019407d0e1997`,
`verification/lean/edge_rigidity_probe.py` at `d5558a7230d539c6bf5115a704cf1b7cddfb1db2`,
`verification/lean-mathlib/OIBridge.lean` at `da9b4c1e9ec4b570925c853b1bc2a8954f8f96e7` and
`verification/lean-manuscript-census.json` at `4ed64a1412f71bd5c96ab67118c63b6c986def45`. The nine
mechanical preconditions the freeze lists were checked at `B` and **all nine pass**.

**(1) `DF1` obligation 3: the witness's provenance diverges from the countercontrol table's supply
item, inside the configuration the table names.** The table names the configuration as **`|A| = 2`**
and the provenance as **supply item 3** — act 12's `sh1_sufficiency` and act 17's `tj1_sufficiency`.
The witness executed is at `|A| = 2`, as named. **It is not drawn from supply item 3.** The reason is
structural and is recorded here rather than argued away: **supply item 3 realizes a prescribed
per-slice Gram tuple**, which is the **diagonal** `(t,t)` part of act 13's datum, and **exercises no
control whatever over the off-diagonal `(t,s)` entries** — which is precisely what obligation 3 for
`DF1` has to control, agreeing at every adjacent pair while differing at a non-adjacent one. Supply
item 3 therefore cannot by itself produce the witness. What was used instead is **supply item 1**,
act 12's own frozen `H(1)`, carried to `|A| = 2` by an index-wise product with a `2 × 2` unitary,
against **supply item 4**, the time-dependent in-fibre left move `diag(1, i)^t` of act 12's
`LeftFibreGroup`, whose invisibility is act 12's merged `left_preserves_admissible`. **This is
recorded as a divergence from the freeze's forecast of provenance and is not repaired, not
corrected, not reinterpreted and not normalized**, and no alternative configuration was substituted:
the obligation was executed at the `|A|` value the table names.

**(2) `DF1` obligation 3 landed where the freeze predicted UNDECIDED at low strength.** The freeze
rates `XS2` (a) `DF1` obligation 3 as *not predicted*, at **low**, and records UNDECIDED with the
obstruction named as its own expectation. The obligation **landed**. This is a preregistered outcome
— `X-SANDWICH` is a frozen label for every Type D candidate, at the evidence bar frozen for it — and
it is reported as such and **not** as an enlargement of the round after the fact: the scope was fixed
before the search and nothing outside it was executed. **The prediction is recorded as reached beyond
its sign**, in the predictions table of section 17.

**(3) `LC1` carries no Lean, and the freeze's countercontrol is conditional in its own text.** The
countercontrol for `LC1`'s non-triviality ends *"excluded **if** no admissible representatives give
the identity"*, which is a conditional and not a construction. The condition requires a **universal**
statement over the admissible dilations realizing the alternating classes, and **no merged result
decides it**. The candidate is therefore reported UNDECIDED with that obstruction named, which is the
freeze's own expectation at **low** strength. **It is recorded as an obstruction and never as a
negative result**, and no `LC1` verdict of any kind is claimed.

**(4) Two auxiliary theorems were needed for the `|A| = 2` witness, and they are theorems and not
definitions.** `prod_mem_unitaryGroup` and `prod_admissible` state that the index-wise product of a
`V`-unitary and an `A`-unitary is unitary, and is an admissible dilation of the visible family whose
entries are the squared moduli of the `V`-factor. **Neither is a top-level `def`**, so neither
consumes a slot of the five-slot definition budget; the matrices stay bound variables pinned by
equations in the statements that need them, exactly as the freeze requires. **This is recorded so
that the budget count is visible rather than inferred.**

**One drafting decision is recorded for the same reason.** `ProperAt` and `PropagatesFrom` take the
configuration as `(a₀, Γ)` and carry the anchor in their signatures, but the anchor is not consulted
in their bodies: pointwise realizability is stated through act 12's `RealizableGram`, which is
**anchor-independent**, act 12's sufficiency holding at every anchor. The anchor is kept in the
signature so that the configuration reads as the freeze names it. **No statement of this round is
weakened or strengthened by that.**

**No candidate discovered during execution was executed.** **No configuration was chosen after an
outcome was known.** **No alternative witness was substituted for a named one.**

## 14. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = _XTS_BASE = d7a9931befeb942db8ebc7b07014f9020c6663d0`. The question is
asked of the **real `pull_request.head.sha`** from the Actions event payload, **never** the synthetic
merge commit continuous integration builds, and an unresolvable head **fails closed** with no
fallback. The check excludes pre-freeze side history: `B` must be an ancestor of `H`, **and every
commit in `git rev-list H ^B` must itself be a descendant of `B`**, fail-closed; the guard recovers
whatever history it needs and fails if recovery fails.

**This is a SEALING round** under `AGENTS.md` `§A.37`. It lands **`E` → `L` → `P`, with `P`
mandatory**. **`_XTS_SEALED_HEAD` and `_XTS_MERGE` are unset at execution.** That is a statement
about this execution and stays true as one after `P` sets them. In archive mode the same strong check
is re-run against the sealed object: the pinned merge's second parent must equal the sealed head, the
sealed head must pass the exclusion check against `B` exactly as in its own run, and both must be
reachable from the current target — each fail-closed.

**The seal-integrity clause EXCLUDES this round's own triple.** `_xts_prior_seals` names acts 13's,
14's, 15's, 16's and 17's triples and **says nothing whatever** about `_XTS_BASE`,
`_XTS_SEALED_HEAD` or `_XTS_MERGE`: there are **zero executable references** to this round's own
constants inside it, following the `_tcf_prior_seals`, `_rnc_prior_seals` and `_trj_prior_seals`
precedent exactly. Docstring prose explains the exclusion and is not executable. **A clause fixing
this round's own pins at unset for all time would contradict the mandatory lifecycle**, under which
`P` sets them: the guard would then pass at no commit once the round landed, which is how an earlier
round in this programme was found non-landable after certifying at its own head.

**Clause 9 was verified EMPIRICALLY before the commit**, in three configurations:

| configuration | required | observed |
| --- | --- | --- |
| unmutated | `True` | **`True`** |
| every single-field fabrication — each of the fifteen prior-seal constants replaced one at a time | `False` | **`False`, fifteen of fifteen** |
| this round's own pins set to plausible values, prior seals unmutated | `True` | **`True`** |

**The third configuration is the decisive one** and is the one an earlier round failed. It is
reported as a measurement and not as an intention.

**Acts 13's, 14's, 15's, 16's and 17's seals are untouched**, and **no existing seal constant is
altered**. **Before certification this execution absorbed no later `main`.**

**The nine preconditions, checked at `B`:**

| # | precondition | result |
| --- | --- | --- |
| 1 | the control plane is merged and `B` is its merge commit; the pinned blob matches | **PASS** — two parents `ece8f96` and `4b3924f`; blob `fd3fa1359188966cae006deba4944a14aab5f3dd` |
| 2 | act 17's execution is merged and sealed | **PASS** — `_TRJ_SEALED_HEAD = '94d4156…'`, `_TRJ_MERGE = 'e8b12a4…'`, both non-`None` |
| 3 | act 16's execution is merged and sealed | **PASS** — `_RNC_SEALED_HEAD = '31db7c1…'`, `_RNC_MERGE = 'eb70bbb…'`, both non-`None` |
| 4 | act 15's execution is merged and sealed | **PASS** — `_TCF_SEALED_HEAD = 'c622461…'`, `_TCF_MERGE = '9e0cc38…'`, both non-`None` |
| 5 | act 14's execution is merged and sealed | **PASS** — `_PQT_SEALED_HEAD = '5008a47…'`, `_PQT_MERGE = 'c50dd22…'`, both non-`None` |
| 6 | act 13's execution is merged and sealed | **PASS** — `_CTI_SEALED_HEAD = '9ea94f9…'`, `_CTI_MERGE = '292848b…'`, both non-`None` |
| 7 | the modules this round consumes are in the tree | **PASS** — `GramTrajectorySelection`, `CrossTimeInvariants`, `TwoSidedGauge`, `CoherentLiftGauge` all present |
| 8 | no act 18 execution object precedes the freeze | **PASS** — the round directory holds `preregistration.md` alone and `IntermediateCrossTimeStructure.lean` is absent |
| 9 | the guard tag and its stem are still free | **PASS** — no occurrence of `R7-XTS` and none of `_XTS` in `edge_rigidity_probe.py` |

**The claim is scoped to the repository record.**

## 15. The axiom table — one line per named result

**Eighteen named results, nothing outside the three standard axioms, no `sorry`, no added axiom and
no `native_decide`.** `decide` over finite index types is used and is kernel-checked.
`Classical.choice` is expected wherever act 17's `tj1_sufficiency` is applied, which assembles a lift
from a per-time choice, and **its appearance there is not a defect**. **`XS0` is type P and is not in
this table.**

| result | axioms |
| --- | --- |
| `xs1_pointwise_factors` | `[propext, Classical.choice, Quot.sound]` |
| `xs1_splice` | `[propext, Classical.choice, Quot.sound]` |
| `xs1_pointwise_not_propagates` | `[propext, Classical.choice, Quot.sound]` |
| `xs2_readback_factors_through_level2` | `[propext, Classical.choice, Quot.sound]` |
| `readback_of_coherentLift` | `[propext, Classical.choice, Quot.sound]` |
| `df_bounded_above` | `[propext, Classical.choice, Quot.sound]` |
| `df1_above_visible` | `[propext, Classical.choice, Quot.sound]` |
| `df2_above_visible` | `[propext, Classical.choice, Quot.sound]` |
| `df2_below_level2_and_resid` | `[propext, Classical.choice, Quot.sound]` |
| `df3_above_visible` | `[propext, Classical.choice, Quot.sound]` |
| `lc0_pointwise_law` | `[propext, Classical.choice, Quot.sound]` |
| `lc3_generator_law` | `[propext, Classical.choice, Quot.sound]` |
| `xs5_l_axis_prop` | `[propext, Classical.choice, Quot.sound]` |
| `lc2_regularity_law` | `[propext, Classical.choice, Quot.sound]` |
| `prod_mem_unitaryGroup` | `[propext, Classical.choice, Quot.sound]` |
| `prod_admissible` | `[propext, Classical.choice, Quot.sound]` |
| `df1_below_level2` | `[propext, Classical.choice, Quot.sound]` |
| `xs4_d_axis_mid` | `[propext, Classical.choice, Quot.sound]` |

## 16. The definition budget

| slot | definition | state |
| --- | --- | --- |
| 1 | `PointwiseLaw` — the predicate that a law is pointwise in this freeze's sense | **fired** |
| 2 | `DeterminesTraj` — the `D`-determination target as one `Prop` over a functional | **fired** |
| 3 | `ProperAt` — the one-configuration non-triviality witness, all four conjuncts | **fired** |
| 4 | `PropagatesFrom` — the propagation predicate, carrying **both** frozen clauses | **fired** |
| 5 (conditional) | a named functional for one Type D candidate | **unused** |

**Five slots were budgeted. Four fired and one is unused. No sixth definition was introduced and no
amendment was needed.** **The module holds exactly four top-level definitions and no others.** **No
lift, gauge element, witness, matrix, visible family, Gram tuple, entry value, law datum or
configuration is a top-level definition**: each is a bound variable pinned by an equation in the
statement that needs it, as acts 10 through 17 did. Acts 7's, 10's, 11's, 12's, 13's and 17's
definitions are **reused, not redefined**; in particular `FibreGram`, `GramPhaseEquiv`,
`RealizableGram`, `CoherentLift`, `FibreCrossGram`, `TwoSidedRelated`, `GramTrajEquiv` and
`SelectsAt` are consumed and none is restated.

**The conditional slot stayed unused** because every candidate functional is readable inline: `F₁`,
`F₂` and `F₃` appear as lambdas in the statements that need them, and `DeterminesTraj` takes the
functional as a parameter rather than naming one.

## 17. The predictions, against the outcomes

**No prediction of this freeze is falsified, and none is against sign.** One is reached beyond its
sign, and one is not exercised.

| target | prediction | strength | outcome | verdict |
| --- | --- | --- | --- | --- |
| `XS0` | negative — the record is silent | high | `XS0`-silent | **as predicted** |
| `XS1` | positive | high | `XS1`-landed | **as predicted** |
| `XS2` (a) `DF1` obligations 1, 2 | hold | high | both hold | **as predicted** |
| `XS2` (a) `DF1` obligation 3 | not predicted; UNDECIDED expected | low | **holds**, at `\|A\| = 2` | **reached beyond its sign** |
| `XS2` (b) `DF2` obligations 1, 2, 3 | `DF2-SANDWICH` | high | `DF2-SANDWICH` | **as predicted** |
| `XS2` (b) `DF2` determination | `DF2-RESID` | high | `DF2-RESID` | **as predicted** |
| `XS2` (c) `DF3` obligations 1, 2 | hold | high | both hold | **as predicted** |
| `XS2` (c) `DF3` obligation 3 | not predicted; UNDECIDED allowed | low | UNDECIDED, obstruction named | **as predicted** |
| `XS3` (a) `LC0` | `LC0-PROPER`, excluded from `L-PROP` by `XS1` | high / high | `LC0-PROPER` and excluded as a theorem of this round | **as predicted** |
| `XS3` (b) `LC1` | not predicted; UNDECIDED allowed | low | UNDECIDED, obstruction named | **as predicted** |
| `XS3` (c) `LC2` | `LC2-PROPER` and `LC2-RESID` | medium | `LC2-PROPER` and `LC2-RESID` | **as predicted** |
| `XS3` (d) `LC3` descent | discharged | high | discharged, at orbit level | **as predicted** |
| `XS3` (d) `LC3` | `LC3-PROPER` and `LC3-PROPAGATES` | medium | `LC3-PROPER` and `LC3-PROPAGATES` | **as predicted** |
| `XS4`, the `D`-axis | `D-MID`, via `DF2` | medium | `D-MID`, via `DF2` | **as predicted** |
| `XS5`, the `L`-axis | `L-PROP`, via `LC3` | medium | `L-PROP`, via `LC3` | **as predicted** |
| the headline pair | (`D-MID`, `L-PROP`) | medium | (`D-MID`, `L-PROP`) | **as predicted** |
| `P-D` | any top-line `F` discards threading and representative information and nothing else | — | **not exercised**: no candidate reached the top line of the `D`-axis | **neither confirmed nor falsified** |

**The freeze's substantive position held.** It predicted, at medium, that the interval between act
17's visible data and act 13's datum is **inhabited** and that what inhabits it there does **not**
determine the trajectory, while a generator law written at orbit level reaches the top of the
`L`-axis. Both halves landed. **That the position was testable, and was rated at medium rather than
higher, is what makes the agreement worth recording**; it is a consistency result and moves nothing
on the correctness axis.

## 18. The scope boundary, as honoured

**No statement of this round distinguishes two lifts `GramTrajEquiv` identifies.** Act 17's
`gramTrajEquiv_of_threading` is the mechanical enforcement and is consumed here: every pair act 13
localized as threading-related is **one** trajectory for this round, and **act 11's `GL2` pair is one
trajectory here**. The cost is accepted deliberately: no outcome of this round can bear on the
relative evolution, on the threading, or on any carrier of act 14.

**Act 16's cancellation cell and the threading question are untouched in either direction.** Neither
is asked here and no outcome of this round bears on either. **Act 10's anchor-axis reclassification
is untouched** in either direction. **`P0` stays OPEN and two-part**, its threading part untouched,
and **no carrier is adopted as the physical one**.

## 19. The frozen `P0` sentence for the case reached

**Case A**, the case the freeze predicts: `XS0` silent, `XS1` lands, the `D`-axis reaches `D-MID` and
the `L`-axis reaches `L-PROP`. The sentence appended to the `P0` row is the frozen Case A sentence,
verbatim, with the row's label **unchanged**:

> `P0` remains open and two-part, and the answers of acts 11 through 17 stand exactly as those rounds
> state them. Act 17's baseline is untouched: the admissible Gram trajectories of a visible family
> are exactly the pointwise realizable assignments, and any cross-time law must enter as additional
> structure. Act 18 asks what such a structure would have to be, on two axes that are not ranked
> against each other, against a candidate list frozen before the search. On the structural question
> that runs first, a law that is pointwise in this round's sense has a solution set equal to the
> product over time of its per-time solution sets, so any uniqueness it produces is slice-by-slice
> uniqueness and never a relation propagating one time from another — which is not the statement that
> no pointwise constraint yields cross-time determination, that being false, but the statement that
> propagation is what fails. On the readback axis, which asks whether a datum strictly between the
> operationally visible data and act 13's level-2 datum determines the trajectory, one named datum
> discharges all three obligations of the refinement sandwich — it consumes nothing beyond act 13's
> level-2 datum, it separates lifts the operationally visible data do not separate, and two lifts
> share it while their level-2 data differ — and two lifts sharing it have inequivalent trajectories,
> so the interval is inhabited and what inhabits it there leaves residual trajectory freedom. On
> the structural-law axis, which asks whether a constraint writable from the anchor and the visible
> family alone is proper and propagates, one named generator law, written at orbit level so that it
> descends, has a solution set at one exhibited configuration that is nonempty, non-singleton modulo
> the round's cross-time equivalence and proper, and two of its solutions agreeing at the initial
> time have the same trajectory. That a law of evolution determines a history given an initial
> condition is what such a law is, and it is legitimate here because the law is writable before any
> lift exists; it is not an assertion that the law obtains, not an adoption of it, and not a claim
> that the programme requires one. The candidate lists are closed and are not exhaustive, each
> verdict is of the exact frozen proposition and of nothing in its neighbourhood, and the coarsest
> determining datum is out of scope by this round's own freeze. `P0`'s threading part is untouched,
> act 10's anchor-axis reclassification is untouched in either direction, **no carrier is adopted as
> the physical one**, and nothing here names, endorses or excludes a selection principle.

**No composition closes `P0`**, and none reports either of its two parts closed. **The two axis
clauses appear in the order readback-then-law, which is an ordering of the sentence and not a ranking
of the axes.**

**The `ROADMAP` was written by appending that sentence and by nothing else.** The `P0` row's label is
**unchanged** and so is its ledger cell, which still reads *"`P0a`/`P0b` closed, acts 11–17
landed"*. The freeze's own writable-files table permits the `ROADMAP` to be **written only by
appending the frozen post-round sentence for the case reached**, and the cell is additionally pinned
by acts 16's and 17's own guard clauses, so advancing it is not this round's to do and was not done.
**No `ROADMAP` section was added**, no other row was touched, and no manuscript was edited.
