# Reconstruction — Lemma 24.1B, framework data: does the observables-preserving hypothesis fix every block-word trace? CONTROL PLANE

**Type-P round.** Every target is a determination about **what the manuscripts say**, settled by
locating and quoting passages, not by proving theorems about matrices. The parent freeze fixed this
shape in terms: 24.1B's question is "a question about the manuscripts' definitions, not about
matrices."

**Unguarded round.** No new guard file is added by this round, and no existing guard is modified.
The definition budget is zero and no Lean module is written, so no kernel object exists for an
ancestry guard to order and no guard tag is reserved. Under `§A.37` this round's landing is
therefore the merge alone: `E` → `L`, with no archive-pin commit.

## The owner's framing, quoted as the authority for this round's scope

> The substantive targets should stay close to the parent question: identify exactly what Theorem
> 24's "observables-preserving" hypothesis fixes; determine whether that includes every block-word
> trace needed by 24.1A; distinguish one-time/channel data from the interleaved multi-time
> correlation data exposed by ST3/ST4; and return a determination with explicit manuscript evidence
> rather than reconstructive inference.

And on `WT2`:

> Crucially, do not reopen WT2 in this round. Its spatial finite-dimensional C*-structure
> obstruction stays recorded as UNDECIDED. 24.1B asks whether the actual reconstruction framework
> supplies enough invariant data to make that theorem relevant, not whether we can formalize the
> missing spatial theorem now.

## The parent's specification of this round, quoted as its charter

From `lemma-24-1a-word-trace-sufficiency/preregistration.md`, section *Round 24.1B, named and not
begun*:

> 24.1B asks whether the reconstruction framework's data — what Theorem 24's
> "observables-preserving" hypothesis actually fixes — determine every block-word trace. `ST3`/`ST4`
> show the uniform-prior channel family alone does not; the interleaved balanced words are
> multi-time visible correlation data, and whether the framework's notion of observables includes
> them is a question about the manuscripts' definitions, not about matrices. This file names 24.1B,
> records that it is OPEN, and freezes nothing about it: no target, no prediction, no reading of the
> manuscripts. It cannot begin before 24.1A's execution has merged, and it needs its own control
> plane.

24.1A's execution has merged. This is that control plane.

## Start state

Pinned **by blob**, at the mandated execution base. Blob identity is authoritative: the commit
locates the tree, the blob is what is compared. A file that moved is the same file; a file that was
rewritten is not.

| path | blob |
| --- | --- |
| `papers/Substratum.md` | `9ac6b732e8786897cade416b67c3f7f1df81ab84` |
| `papers/Explainer.md` | `b0926875346305ef053995fc10695353df64de68` |
| `papers/Methodology.md` | `1d332b0c9256e33861af0ce3b5598091b63d30a1` |
| `papers/Structure.md` | `84a7ede451a917513dd488477c93180f5f8c0486` |
| `papers/Complexity.md` | `dd38c5b39797433b6f5de469f5711fd38b116441` |
| `lemma-24-1a-word-trace-sufficiency/preregistration.md` | `98cfcfdc0e74ffe0186c502517a842bfeb25d351` |
| `lemma-24-1a-word-trace-sufficiency/result.md` | `124a02c9d2b17c0cf280f15a00ab269f68e33a24` |
| `lemma-24-1-semigroup-transfer/result.md` | `b5822febb2626af48c29f6198fd6d74637ef9896` |
| `act-14-threading-observability/result.md` | `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` |

Every one of these is **read and never written** by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

## Why this round exists

24.1A certified `ST5`'s hypothesis sufficient **on the spanning class**: where the visible blocks
span all of `M_m(ℂ)`, equal block-word traces give an exhibited hidden unitary. That is a theorem
about an invariant on finite matrices. It is not a statement that anything in the framework hands
you that invariant.

The gap is named in 24.1A's own first boundary:

> **Lemma 24.1 is not repaired.** A theorem about an invariant on finite matrices is not
> completeness of `𝒢_sub`; whether the reconstruction framework supplies the block-word trace data
> is round 24.1B, which is named here and not begun.

So the live question is whether `ST5`'s hypothesis is one the framework's own observables-preserving
hypothesis entails. If it is, 24.1A's sufficiency result bears directly on the `P1` completeness
obligation on the spanning class. If it is not, 24.1A's result stands as proved and is about data
the framework does not give you — which is a different, and weaker, relationship to Theorem 24.

**Neither reading is preregistered as the expected one.** Both are live, and the predictions below
record what this freeze expects with its reasons and its strengths.

## The objects, FROZEN

**`H_obs` — the observables-preserving hypothesis.** Theorem 24's hypothesis on a transformation
`g`, as the manuscripts state it. Its content is to be *located*, not reconstructed.

**`O_set` — the observable set the completeness argument is relative to**, as the manuscripts state
it.

**`Φ-family` — the time-resolved visible channel family** `{Φ_t}_{t ≥ 0}` and the matrix elements
`T_ij(t)`, as the manuscripts define them.

**`W-data` — the block-word trace data** that `ST5`'s hypothesis quantifies over, as 24.1A's frozen
objects define it. This round does **not** redefine it and does **not** restate it in its own words
except by quotation.

**`interleave` — the interleaving question.** Whether a block-word trace over a word that
interleaves letters is a matrix element, a function, or neither, of the `Φ-family`. This is the
round's crux and is treated as a question, not an assumption.

The round adds **no** object of its own. Where a distinction is needed that the manuscripts do not
draw, the execution **records that the manuscripts do not draw it** and does not draw it on their
behalf.

## The evidence rule, FROZEN

Every determination is **type P** and must be carried by one or more of:

1. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
2. a **verbatim quotation** from a merged result note or preregistration, with its coordinate; or
3. an explicit, recorded statement that **the passage sought does not exist** on the record
   searched, with the search named and bounded.

**Reconstructive inference is not evidence.** A determination of the form "the framework must mean
X, because otherwise Y would fail" is **forbidden as a finding** and may appear only in a clearly
labelled analysis paragraph that states it is not evidence and that no target rests on it. Where the
manuscripts are silent, the finding is that they are silent.

**Strength is recorded per determination**, as `full`, `high`, `medium` or `UNDECIDED`, and a
determination carried by a passage that names a thing without displaying it is at most `medium`.

## The act 14 anti-conflation clause, FROZEN VERBATIM

Act 14 is present in this round under exactly this clause, which the execution carries verbatim
wherever act 14 is named:

> Act 14 is cited only to illustrate a structurally similar distinction between "what is observable"
> and "what is merely representational." Its carriers and conclusions belong to Track B and do not
> instantiate, constrain, or supply evidence for Theorem 24's observables-preserving hypothesis. No
> implication is transferred in either direction.

Act 14 therefore appears in **analysis only**. **No target is carried by act 14**, no target cites
it as evidence, and no determination changes sign or strength because of it. The parent programme's
standing separation — "The substratum programme and the OI→QM programme share the repository and
nothing else" — is preserved in substance: this round borrows a *shape of question*, not a result.

Writing act 14's carriers as if they were candidates for `O_set`, or `O_set` as if it were a carrier
in act 14's sense, is a **defect of this round** and is checked for in the final report.

## The targets, FROZEN

### `WD0` — locating controls, cheap and certain

Locate and quote, with coordinates: Theorem 24's statement; the completeness argument's Steps 1–3;
its *Conclusion*; its *Scope of the completeness claim*; and Lemma 24.1's statement and proof
structure. Record the observable set exactly as written.

**Falsifier.** Any of these passages absent from the pinned blob at the base.

### `WD1` — what `H_obs` fixes, enumerated from the source

Determine, by quotation, the **exact content** of the observables-preserving hypothesis: which data
a transformation `g` is assumed to preserve, quantified how, and over what index set. Report the
enumeration as a list, each entry carried by its own quotation.

Report separately, and do not merge, **four** statements: the **equivalence relation `∼`** as
defined immediately before Theorem 24; what the hypothesis states **in Theorem 24's own statement**;
what the completeness argument's **Step 1** assumes; and what the **Scope** paragraph says the
argument is relative to. If these four differ, **the difference is the finding** and is reported as
a discrepancy of the source, not repaired.

### `WD1-q` — the partition quantifier, reported for each of the four

**A distinct subtarget, because the same observable vocabulary can carry two different amounts of
information.** For each of the four statements above, determine and report **which partitions the
observable data is quantified over**:

- **fixed-partition** — the data of one visible/hidden partition; or
- **all-partitions** — the data of every partition of the structural class; or
- **unstated** — the passage names the observables without fixing the quantifier.

Report the quantifier **per statement, with its own quotation**, and do not carry a quantifier from
one statement to another. If the four disagree, that disagreement is a finding of `WD1` and is
recorded rather than normalized.

This subtarget exists because `ST3`/`ST4` refute a **fixed-partition** claim. Whether they bear on
an **all-partitions** claim is a separate question, which `WD2-q` asks and which this round may
leave open.

### `WD2` — one-time channel data against interleaved multi-time data

Determine whether the manuscripts anywhere distinguish, or collapse, these two:

- **(a)** the time-resolved family `{Φ_t}_{t≥0}` and its matrix elements `T_ij(t)` — one channel per
  time, each a map on the visible factor; and
- **(b)** interleaved multi-time visible correlation data — data whose specification requires more
  than one operator applied in an order that is not a power of a single generator.

Report, with quotation: whether (b) appears in `O_set`; whether any passage asserts (b) is
determined by (a); whether any passage asserts it is not; and whether the question is posed at all.
**Silence is a finding**, reported as silence.

Consume `ST3`/`ST4` from the merged Lemma 24.1 result **as established**, unrevised: they are the
record that the uniform-prior channel family alone does not determine the block-word traces. This
round does not re-derive them, does not extend them, and does not weaken them.

### `WD2-q` — what `ST3`/`ST4` refute, and over which partitions

**A distinct subtarget, because `ST3`/`ST4` refute a claim whose quantifier must be read before it
can be matched against `WD1-q`'s.** Determine and report, by quotation from the merged result:

1. **Over which partitions `ST3`/`ST4`'s refutation runs** — whether their channel family is the
   data of one partition or of every partition of a class.
2. **Whether any passage anywhere on the record addresses the all-partitions family** — whether the
   observable data of *every* partition of the structural class determines the block-word traces.
   Report what is found, or record that nothing is found on a named and bounded search.

**Do not assume the two families coincide, and do not assume they differ.** If the record settles
neither, that is the finding, and it is the finding that gates `WD3` below.

### `WD3` — does `H_obs` entail `ST5`'s hypothesis?

The assembled determination, at the strength jointly reached by `WD1` and `WD2`, in exactly one of:

- **`WD3-yes`** — the framework's observable set includes data that fixes every block-word trace
  `ST5` quantifies over. Requires a quotation that puts (b)-type data in `O_set`, or a quoted
  argument in the manuscripts that (a) determines (b). Absent that, this reading is **not** written.
- **`WD3-no`** — the framework's observable set as stated does not include that data. Requires the
  enumeration of `WD1` to be complete on the record searched, **and** `WD2` to have found (b) absent
  from `O_set`, **and** no quoted passage asserting (a) determines (b), **and** the gating condition
  immediately below.
- **`WD3-UNDECIDED`** — the permitted fallback, with the obstruction named.

**The gating condition on `WD3-no`, FROZEN:**

> `WD3-no` may be written only if `WD1`/`WD2` establish that the full information quantified by
> `H_obs` is no stronger, for the purpose at issue, than the channel-family data separated by
> `ST3`/`ST4` — including resolution of the "for all partitions of the same structural class"
> quantifier. If the manuscripts impose all-partitions data and the record does not establish
> whether that richer family fixes the block-word traces, the outcome is `WD3-UNDECIDED`, not
> `WD3-no`.

**Why this gate exists.** Absence of (b) from a stated observable set is not by itself the
determination the target asks for. The target asks whether `H_obs` **entails** `ST5`'s hypothesis,
and `H_obs` may quantify over strictly more than the family `ST3`/`ST4` separated. Enumerating
`O_set` and finding (b) missing would settle a **fixed-partition** reading and leave an
**all-partitions** reading untouched. The gate makes the decision rule match the target's wording
rather than the easier question underneath it.

**The gate binds the decision rule, not the prediction.** The prediction below leans to `WD3-no`;
the gate is what stops the round from reaching it on insufficient grounds.

**`WD3-no` is a statement about the manuscripts' stated observable set. It is not a statement that
the framework is wrong, that Theorem 24 is false, that completeness fails, or that 24.1A's theorem
is idle.** Those sentences are forbidden; see the non-licence section.

### `WD4` — the downstream consumers, located and listed

List every place in the pinned blobs that consumes Theorem 24's **completeness** claim, with
coordinates and with what each asserts. The known candidates, to be checked and not assumed:
`Complexity.md:198` and `:206`, `Explainer.md:983`, `Methodology.md:353` and `:355`,
`Structure.md:49`, `:154`, `:195`, and `Substratum.md:16`, `:24`, `:270`, `:290`, `:292`.

**This is a census, not a propagation.** No manuscript is edited in this round, and no consumer is
adjudicated as correct or incorrect. The list exists so that a later owner-directed propagation
round has its surface enumerated.

## The preregistered predictions, and their strengths

Recorded before execution, with reasons, so that the outcome can be compared against them.

| target | prediction | strength expected | reason |
| --- | --- | --- | --- |
| `WD0` | positive | full | the passages were located while drafting this freeze |
| `WD1` | positive | high | the *Scope* paragraph states an observable set explicitly |
| `WD1-q` | positive, and **the four statements are expected to disagree on the quantifier** | medium | the `∼` definition carries "for all partitions of the same structural class" while Step 1 is written about one channel family; whether that is a real disagreement or one wording of one thing is what the subtarget must settle |
| `WD2` | positive, and **(b) is expected absent from `O_set` as written** | medium | the located set is written in terms of `T_ij(t)`, `H` up to D-gauge and `ℏ`; whether that wording excludes (b) is a reading this round must settle, not assume |
| `WD2-q` | positive on part 1; **part 2 is expected to find nothing** | medium | `ST3`/`ST4` were proved about a channel family on a fixed carrier; whether anything on the record addresses the all-partitions family is exactly what the search must determine |
| `WD3` | `WD3-no` | medium | follows from `WD1` and `WD2` if both land as predicted. **The principal falsifier, and the principal escape hatch, is the all-partitions quantifier**: if `H_obs` is read as imposing the observable data of every partition of the structural class, that family is strictly richer than the one `ST3`/`ST4` separated, and nothing on the record is expected to say whether the richer family fixes the block-word traces. In that case the gate forces `WD3-UNDECIDED`. A single quoted passage elsewhere asserting (a) determines (b) would also move it. |
| `WD4` | positive | high | a census over pinned blobs |

**Two predictions are deliberately held at medium.** `WD2` and `WD3` are the round's substance, and
a freeze that predicted them at high would be claiming the answer it is chartered to find. If either
lands above its predicted strength, the result note records the promotion and its reason.

**No prediction licenses its own conclusion.** A target that lands against prediction is reported
against prediction, and the prediction is not amended.

## The post-round sentence, frozen now, one per outcome

Exactly one is written, verbatim, in the result note and nowhere else.

**If `WD3-no`:**

> The reconstruction framework's observables-preserving hypothesis, as the manuscripts state it,
> fixes the time-resolved visible channel family and the observable set relative to which Theorem
> 24's completeness argument is stated, **with the partition quantifier resolved as recorded in
> `WD1-q` and the information it carries established no stronger, for the purpose at issue, than the
> family `ST3`/`ST4` separated**. On the record searched, that set does not include the interleaved
> multi-time correlation data over which `ST5`'s hypothesis quantifies, and no passage asserts that
> the channel family determines it. Lemma 24.1A's sufficiency result therefore stands as proved and
> is not, on this record, supplied by the framework's own hypothesis. The `P1` completeness
> obligation remains OPEN, no manuscript claim changes, and nothing here shows that completeness
> fails or that Theorem 24 is false.

**If `WD3-yes`:**

> The reconstruction framework's observables-preserving hypothesis, as the manuscripts state it,
> includes data that fixes every block-word trace over which `ST5`'s hypothesis quantifies, by the
> passage quoted in the result note. Lemma 24.1A's sufficiency result therefore bears on the `P1`
> completeness obligation on the spanning class, and no higher. `WT2` stays UNDECIDED, the general
> case is not reached, and the `P1` obligation remains OPEN.

**If `WD3-UNDECIDED`:**

> Whether the reconstruction framework's observables-preserving hypothesis fixes the block-word
> trace data is UNDECIDED, with the obstruction named in the result note. Lemma 24.1A's sufficiency
> result stands as proved at its own strength. The `P1` completeness obligation remains OPEN and no
> manuscript claim changes.

If the obstruction is the partition quantifier, the result note names it in these terms and no
others: the manuscripts impose observable data over all partitions of the structural class; that
family is strictly richer than the fixed-partition channel family `ST3`/`ST4` separated; and the
record does not establish whether the richer family fixes the block-word traces. **That is a
statement about what the record settles, not a claim that the richer family does or does not fix
them.** Naming it is a finding; resolving it would be a later round.

## What none of these outcomes licenses

- **Nothing about the truth of Theorem 24.** This round reads a hypothesis; it does not evaluate the
  theorem. The forbidden sentences are "Theorem 24 is false", "Theorem 24 is repaired",
  "completeness holds", "completeness fails", "the generators are complete", "the generators are
  incomplete", "Lemma 24.1 is repaired", and "the manuscripts' route is restored".
- **Nothing that promotes or demotes 24.1A's result.** `WT0`–`WT4` are consumed as merged and none
  is revised. In particular a `WD3-no` does **not** make 24.1A's theorem wrong, idle, or absent from
  the record; it is a finding about what supplies its hypothesis.
- **`WT2` is not reopened.** Its obstruction — the spatial form of finite-dimensional C*-structure
  theory, pieces (a)–(f) absent from Mathlib at the pin and from the corpus — stays recorded as
  UNDECIDED. No piece of it is built, attempted, or scoped here.
- **Nothing about Track B, `P0`, act 14's carriers, or the fibre-Gram classification**, in either
  direction. The anti-conflation clause governs.
- **Nothing about Bell or H-Bell**, nothing about A6, nothing about hydrodynamics.
- **No manuscript is edited.** `papers/` and `book/` are read, not written. Whether and how to
  propagate any finding is an owner call in a separate round, and `WD4` exists to enumerate that
  surface, not to act on it.
- **No selection principle is named**, and no sentence beginning "the selection principle is" is
  written.
- **Nothing about the physical substratum**, and nothing about whether the wave rule on the cubic
  lattice satisfies `BlockSpanning`.

## Immutable inputs

Consumed as merged and unrevised: `ST0`–`ST5` from the Lemma 24.1 semigroup-transfer round;
`WT0`, `WT1`, `WT2-gen`, `WT3` on the spanning class and `WT4` from 24.1A, with `WT2` UNDECIDED. The
`P1` row's label is read and not moved.

## The chronology control

1. This preregistration is merged **alone**, before any execution object exists. Once merged it is
   **immutable**; an execution that diverges records the discrepancy rather than repairing it.
2. The **mandated execution base** is the merge commit of this control plane's pull request. The
   execution branches from exactly that commit and from nothing else, and verifies this file's blob
   at that base before executing any target.
3. **No new guard file is added by this round, and no existing guard is modified.** The definition
   budget is zero and no Lean module is written, so there is no kernel object for an ancestry guard
   to order and no guard tag is reserved.
4. Because the round is unguarded, its landing under `§A.37` is the **merge alone**: current green
   main as first parent, the sealed execution head as second, and **no archive-pin commit**. The
   sealed execution commit is never modified; conflicts are resolved in the landing merge and never
   in the sealed commit.
5. The certification of record is the run whose `head_sha` is the sealed execution head.

## Definition budget

**Zero.** No Lean module, no definition, no theorem, no probe. If the audit uncovers a precise
formal subclaim worth separating, the execution **names it and does not build it**, and it becomes a
candidate for a later round with its own control plane.

## Evidence level

**Type P throughout.** No target is at evidence level 2, there is no axiom table, and there is no
`#print axioms` line, because no Lean is written. The result note says so in terms rather than
leaving the absence to be inferred.

## Named hazards

1. **Reconstructive inference presented as a finding.** The strongest hazard of this round. A reader
   who knows the framework can supply a bridging argument the manuscripts do not contain. The
   evidence rule forbids it; the final report states for each determination which quotation carries
   it.
2. **Conflating act 14's carriers with `O_set`.** Governed by the anti-conflation clause, which is
   carried verbatim at every mention.
3. **Reading `WD3-no` as a defect verdict.** `WD3-no` says the stated observable set does not
   include certain data. It does not say the framework is wrong. The post-round sentence is written
   to make the distinction unavoidable, and the forbidden sentences are listed.
4. **Silently repairing a discrepancy between the three statements of the hypothesis.** `WD1`
   requires them reported separately; if they differ, the difference is the finding.
5. **Scope creep into `WT2`.** Excluded in terms by the owner's direction and by the non-licence.
6. **Treating silence as denial.** Where the manuscripts do not pose the question, the finding is
   that they do not pose it — not that they answer it negatively.
7. **Normalizing the partition quantifier.** The sharpest hazard of the round after (1). The same
   observable vocabulary — `T_ij(t)`, the emergent Hamiltonian, `ℏ` — appears with a fixed-partition
   reading in one place and an all-partitions reading in another, and the two carry different
   amounts of information. Reading them as one thing would let `WD3-no` fire on a question strictly
   easier than the one the target asks. `WD1-q`, `WD2-q` and the gate on `WD3-no` exist for this
   hazard and are checked for in the final report.
8. **Answering the quantifier question instead of recording it.** If the record does not settle
   whether the all-partitions family fixes the block-word traces, the round says so. Settling it
   would be a matrix question, which this round is not, and a later round with its own control
   plane.

## Non-doings

No manuscript edit. No Lean. No guard. No probe. No census entry. No `ROADMAP` label moved. No
propagation. No reopening of `WT2`. No re-derivation of `ST3`/`ST4`. No new object, and no
distinction drawn on the manuscripts' behalf.

## Execution discipline

The execution produces **the result note and nothing else**, plus the `ROADMAP` and `README`
pointers the round's own section needs. One pull request from the mandated base, carrying the
execution; after certification the same pull request carries the landing merge.

## Allowed final report

Every target with its outcome, evidence type, strength and the quotation carrying it; the three
statements of the hypothesis reported separately; the `WD4` census; the discrepancy section; the
single frozen post-round sentence; the anti-conflation clause verbatim at each act 14 mention; and
an explicit statement that the round is type P with no axiom table. Nothing else.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **"Interleaved multi-time correlation data" is defined here by its specification**, as data
   requiring more than one operator in an order that is not a power of a single generator. The
   manuscripts may not use this phrase; if they use a different one for the same thing, the
   execution records both and does not merge them.
2. **The observable set is taken to be whatever the *Scope* paragraph names**, with Theorem 24's own
   statement and Step 1 reported alongside it rather than merged into it. A different reading would
   take the union of the three; this freeze does not, and records that choice here.
3. **Act 14 enters as analogy and not as evidence.** The alternative — excluding it entirely — was
   considered and set aside by owner direction, with the anti-conflation clause as the safeguard.
4. **The round is unguarded.** An alternative would write a guard pinning the quoted coordinates.
   This freeze does not, because the definition budget is zero and there is no kernel object to
   order; the blob pins in the start-state table carry the immutability the round needs.
