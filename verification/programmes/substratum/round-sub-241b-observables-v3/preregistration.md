# Substratum round SUB-241B-OBS — Lemma 24.1B taken up: does Theorem 24's observables-preserving hypothesis fix every block-word trace?: PREREGISTRATION (candidate `F` for owner review)

**Status: candidate control plane, native V3, presented for `F` designation review; `F` is not designated.**
This file is the control plane of a native round under `AGENTS.md` §A.39, drafted on one pull request from `D`.
Only the owner designates `F`; an instruction to proceed is not a designation. `F` has the preconditions listed
under *Preconditions of `F`*. Nothing is executed.

```v3-round
round SUB-241B-OBS
kind non-sealing
record-directory verification/programmes/substratum/round-sub-241b-observables-v3/
```

```v3-governed-paths
record AM verification/programmes/substratum/round-sub-241b-observables-v3/
record AM verification/receipts/SUB-241B-OBS.json
execution M verification/ROADMAP.md
execution M verification/README.md
```

`D`: `0d917665d32287e5d0ce649012175f2c7bf75b09` (`main`, the merge of #959; its `verify` run 40535620231 was green,
cited as provenance). `delta(D, F)` is this preregistration and any amendments under the round's `amendments/`
directory. The record directory holds this preregistration, the frozen controls `controls.py` (added at stage 1 at
the blob frozen below), any amendments and the result note `result.md`. The receipt path is
`verification/receipts/SUB-241B-OBS.json`. The two execution paths carry only the pointers the frozen execution
discipline names (*Readings*, R3). At `D` the round id, the record directory and the receipt path occur nowhere in
the tree.

**No manuscript, built artifact, Lean module, guard clause, seal record, round certificate or
`control-plane-preconditions` block is part of this round under any outcome, and no other round's record
changes.** The legacy directory `verification/programmes/substratum/lemma-24-1b-framework-data/` is not a governed
path and stays byte for byte as it stands.

## Provenance: the frozen, never-executed round 24.1B

The legacy control plane `verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md`, blob
`f614b666ad9098f866969c4c524e47f504e5d71c`, was merged by #631 as `445701c764245d17a55b4c401b41f3333a9c4b02`
(first parent `4beac05c68920af2de6ebe2ba8746bdb0cfb2356`, second parent
`95adaeb9492ef4c97d07c790c344439402f70caa`). Its chronology control made that merge the mandated execution base.
It was never executed: at `D` its directory holds that one file, at the same blob as at `445701c7`, and
`verification/infrastructure/legacy-records.json` closes the directory (:77) and pins the file at that blob (:349).

`AGENTS.md` at `D`, §A.37 (:822–823): "A question one of those rounds left open, or froze and never executed, is
taken up by a new native round, which cites the old freeze as provenance and leaves the old record as it stands."
This round is that native round. The legacy record is provenance. Its targets, rules, predictions, sentences and
non-licences are adopted below; its protocol mechanics are replaced by §A.39's (*The protocol*).

## Owner decisions

Planning issue #985, opened by `amaybaum` at 2026-10-28T07:14:11Z, records the owner's approval of this round on
2026-10-28 and these decisions, quoted:

> **Owner decisions for the control plane**
> - **Round id:** `SUB-241B-OBS`. Record directory: `verification/programmes/substratum/round-sub-241b-observables-v3/`. Receipt: `verification/receipts/SUB-241B-OBS.json`. The round is non-sealing.
> - **Evidence base:** the frozen pinned blobs, exactly as 24.1B pinned them. SC-44 (#980), SC-45 (#981) and the current manuscripts are not substituted. How the historical findings bear on the corrected contemporary theory is recorded separately and does not change the frozen verdict.
> - **WD1** examines four distinct statements, as its detailed specification says. The conflicting reference to "three" (legacy prereg :390, :421) is recorded as a discrepancy.
> - **Independence:** this round and SUB-241C-SPAN must not use each other's results as premises.

A comment on #985 (id 6463778359), posted by `amaybaum` at 2026-10-28T07:58:09Z, records word for word the owner's
decisions 5 and 6, given that day in the coordinating session, for this round and SUB-241C-SPAN. Quoted in part:

> 5. Writing permission — approved. […] Before `F`, only the respective round's control-plane files may change on its native PR branch. Keep research calculations and exploratory work on separately linked branches. Neither old freeze may be edited.
>
> 6. Branch-local reconciliation `Λ` — approved as a specific exception. The standing no merges rule continues to prohibit merging either PR into `main`. It does not prohibit the V3-required reconciliation merge on that round's own branch after a designated `E`. […] This approval does not authorize arbitrary branch merges, force-pushes, or merging `Q` to `main`.
>
> The approvals above authorize preparation and drafting, not `F` designation, `E` designation or any `workflow_dispatch`. […]
>
> Most importantly, 24.1B and 24.1C must not contaminate each other's evidence. They may proceed in parallel, but neither result may become an unstated premise of the other's frozen decision.

Three requirements are carried with them: governed paths limited to the record directory, the receipt and the
`ROADMAP`/`README` pointers, with no Lean, guard clause, seal record, certificate or `control-plane-preconditions`
block (§A.39); a checkpoint for every stated invariant (§A.41); and a start-state note that the quoted objects have
drifted at `main`. Where each is encoded:

| decision | encoded in |
| --- | --- |
| 1. round id, record directory, receipt, non-sealing | the `v3-round` and `v3-governed-paths` blocks; the paragraph after them |
| 2. provenance; the frozen targets adopted by citation and quotation, not reinterpreted | *Provenance*; *The frozen round, quoted*; *The protocol* |
| 3. the nine pins as the evidence base; the separate non-verdict section; the drift note | *Evidence base and start state*; *The non-verdict section*; checks `T4`, `N4`, `N16` |
| 4. four statements under `WD1`; "three" recorded as a discrepancy | *Discrepancies*, X1; checks `N7`, `N17` |
| 5. independence from SUB-241C-SPAN and any 24.1C result | *Independence*; checks `N4`, `N14` |
| 6. governed paths | the `v3-governed-paths` block; checks `T5`, `T6`; the verifier at `Q` |
| 7. every invariant measured | *Invariants and their checkpoints* |
| no merge into `main`; `Λ` branch-local only (comment 6463778359, decision 6) | *The protocol*; the invariant row on the round's records |

## The frozen round, quoted

The legacy freeze is adopted completely, in its own words. Three blocks below quote blob `f614b666` from line 3 to
line 438, every line after its title except the blank lines 350 and 366. Its targets `WD0`, `WD1`, `WD1-q`,
`WD2`, `WD2-q`, `WD3` (with its gate) and `WD4`, its evidence rule, its act 14 clause, its predictions and
strengths, its three post-round sentences, its non-licences, its immutable inputs, its definition budget, its
evidence level, its hazards, its non-doings and its points of reading are this round's, unamended and not
reinterpreted. Two passages
describe the §A.37 lifecycle — the paragraph headed **Unguarded round** (:8–11) and *The chronology control*
(:351–365), with the execution discipline's second and third sentences (:415–416) — and *The protocol* states what
replaces them. Where the freeze says "this round", it names round 24.1B, which this round executes. Each block is
checked against the blob by `T7`.

Lines 3–349: the type, the owner's framing, the charter, the start state, the objects, the evidence rule, the act
14 clause, the targets, the predictions, the post-round sentences, the non-licences and the immutable inputs.

```quote f614b666ad9098f866969c4c524e47f504e5d71c 3-349
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
```

Lines 351–365: the chronology control (replaced; *The protocol*).

```quote f614b666ad9098f866969c4c524e47f504e5d71c 351-365
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
```

Lines 367–438: the definition budget, the evidence level, the named hazards, the non-doings, the execution
discipline, the allowed final report and the points of reading.

```quote f614b666ad9098f866969c4c524e47f504e5d71c 367-438
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
```

## The protocol

The round runs under §A.39 and `verification/infrastructure/v3/architecture.md`. What the freeze's §A.37 passages
required, and what carries each requirement here:

| the freeze (§A.37) | this round (§A.39) |
| --- | --- |
| unguarded; no guard file added or modified; landing the merge alone, no archive-pin commit (:8–11, :358–364) | non-sealing; no guard clause, seal record, certificate or `control-plane-preconditions` block; the lifecycle `F` → `E` → `Λ` → `Q`, the receipt the round's protocol record |
| the preregistration merged alone before any execution object, then immutable (:353–354) | the control plane drafted on one pull request from `D`; immutable from the designated `F` (`G7`); checked by `T2` and by the verifier at `Q` |
| the mandated execution base, the merge commit of the control plane (:355–357) | execution anchored at `F` (`S3`); the nine pins stay located at `445701c764245d17a55b4c401b41f3333a9c4b02`, where the freeze pinned them (`T4`) |
| verify this file's blob at that base before executing any target (:356–357) | `T3`: the legacy file at blob `f614b666` at `445701c7`, at `F` and at `E` |
| the certification of record, the run whose `head_sha` is the sealed head (:365) | the exact-head `check-run` attestations at `F` and at `E`, recorded in the receipt (§A.39) |
| one pull request from the mandated base, then the landing merge (:415–416) | one pull request from `D`; reconciliation after `E` (§A.39 item 3); the receipt commit `Q` |

The freeze's definition budget (zero), its evidence level (type P, no axiom table) and its non-doings stand
unchanged, and they agree with the governed-path block: no Lean module, guard, probe or manuscript path is
governed. Issue #985 lists the owner's touchpoints: the exact-head dispatch and the designation at `F` and at `E`,
and the branch-local reconciliation `Λ` after `E`; and it records that the pull request is not merged into `main`.
How the round's commits reach `main` is outside its validity (`S10`): `tools/v3_verifier.py --verify-round Q`
decides the round wherever `Q` lies. Until a commit reachable from `main` reaches `Q`, the round's record, receipt
and pointers exist only on the round's branch: its finding is provenance and not an enduring claim (§A.42 items
1–3), so no manuscript, round or record on `main` rests on it; the release gate on `main` does not verify its
receipt, and `G13` does not protect its record there; and the branch `v3/sub-241b-obs` is not deleted (§A.42 item
5). Making the record durable is a separate publication of `Q` to `main`, authorized by the owner and not part of
this round: a merge whose tree keeps the record directory and the receipt exactly as at `Q`, or a further
reconciliation and receipt commit (`G11`) followed by a fast-forward.

## Evidence base and start state

**The evidence base is the nine blobs the freeze pinned, exactly** (owner decision 3). The freeze's table (:50–60)
names five manuscripts by path and four records by a shortened path. Each blob lies at exactly one path in the tree
of `445701c7`, resolved here by blob:

| path at `445701c7` | pinned blob | state at `D` |
| --- | --- | --- |
| `papers/Substratum.md` | `9ac6b732e8786897cade416b67c3f7f1df81ab84` | `ef43bd61d546eac3ff8f09c8b867a5d24a4cc6fe`; 45 commits of `445701c7..D` touch the path |
| `papers/Explainer.md` | `b0926875346305ef053995fc10695353df64de68` | `c1a57ec5e18a653649737d32afe8ce31409efec5`; 47 commits |
| `papers/Methodology.md` | `1d332b0c9256e33861af0ce3b5598091b63d30a1` | `54112e5118ccb7e90f69246489831d8c49353e24`; 13 commits |
| `papers/Structure.md` | `84a7ede451a917513dd488477c93180f5f8c0486` | `71550d6ed0a311c5e2e21fb87fef2d9e89a94830`; 28 commits |
| `papers/Complexity.md` | `dd38c5b39797433b6f5de469f5711fd38b116441` | `e71182d187509c0ea6b0f6ab74c2943ef5b78d85`; 15 commits |
| `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/preregistration.md` | `98cfcfdc0e74ffe0186c502517a842bfeb25d351` | identical |
| `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md` | `124a02c9d2b17c0cf280f15a00ab269f68e33a24` | identical |
| `verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md` | `b5822febb2626af48c29f6198fd6d74637ef9896` | identical |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md` | `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` | identical |

`445701c7` lies on `D`'s first-parent chain, so every pinned blob is reachable from `main`. The freeze's rule that
blob identity is authoritative (:46–48) governs: a quotation is read from the pinned blob at its own line numbers,
and the state of a path at `D` or later is not evidence for any target. Under the freeze's evidence rule, item 1
draws on the five manuscript blobs and item 2 on the four pinned records, plus the freeze's own blob `f614b666`
where the result note quotes the freeze itself (*Readings*, R1). Act 14's blob enters only as analysis (the act 14
clause, :126–142). `T4` and `N4` measure this.

**Start-state note: the quoted objects have drifted at `main`.** At `D` the five manuscript paths hold other blobs
(table above), so a coordinate in a pinned blob need not hold at `D`. Two open draft pull requests would change the
quoted objects further. SC-44 (#980; head `87d0b03f4aff` when measured on 2026-10-28) changes
`papers/Substratum.md`: its diff removes 14 lines that contain `Lemma 24.1` (all 14 at `D`) and adds none, removes
the line that contains `Scope of the completeness claim`, and removes 5 lines that contain `observables-preserving`
while adding 2. SC-45 (#981; head `6aff07d452c0`) removes the line that contains `for all partitions of the same
structural class`. This note records the start state. It does not change the evidence base, no target reads it, and
neither pull request's content is a premise here.

## Independence

No premise of this round comes from SUB-241C-SPAN or from any 24.1C result. The evidence base was fixed at
`445701c7`, whose tree holds no 24.1C object, and no evidence quotation or search may cite anything outside it
(`N4`). No section of the result note other than its start state names 24.1C or SUB-241C-SPAN, in its text or in
any block (`N14`), and the start state carries the sentence that opens this section, verbatim (`N14`). The
non-verdict section quotes no path of a 24.1C record (`N4`). This control plane was drafted without reading the
sibling round's record.

## Discrepancies of the freeze, recorded and not repaired

- **X1 — four statements or three.** `WD1` (:160–164) and `WD1-q` (:166–178) name **four** statements: the
  equivalence relation `∼`, Theorem 24's own statement, Step 1 and the *Scope* paragraph. Named hazard 4 (:390)
  speaks of "the three statements of the hypothesis", and the allowed final report (:420–421) of "the three
  statements of the hypothesis reported separately". The owner's issue places the second at :421; the phrase begins
  at the end of :420. By owner decision 4, `WD1`'s detailed specification governs: the result note reports the four
  statements separately (`N7`), which also reports separately every statement the two shorter passages count. A
  related site, *Points at which this freeze chose a reading*, item 2 (:431–433), speaks of "the union of the
  three": there the three are the *Scope* paragraph, Theorem 24's statement and Step 1, the sources of the observable
  set, and the passage is consistent with `WD1` as written. The result note quotes :160, :390, :420–421 and :433 in
  its discrepancy section (`N17`).
- **X2 — "Nothing else".** The allowed final report ends "Nothing else." (:423). The result note carries three
  sections that report does not list: its start state, which records the pin and freeze checks the chronology
  control asked the execution to make (:356–357); the non-verdict section the owner directed (decision 3); and a
  checks section stating the command and expected result of its controls (§A.42 item 1). None of them carries a
  target, an outcome or a strength (`N4`, `N6`, `N16`).
- **X3 — the protocol passages.** :8–11, :351–365 and :415–416 describe the §A.37 lifecycle; §A.37's own provision
  (:822–823 of `AGENTS.md`) routes the frozen question to a native round, and *The protocol* states what replaces
  each passage.
- **X4 — "at the mandated execution base".** The freeze pins its blobs "at the mandated execution base" (:46). The
  pins are located at `445701c7`, where all nine match; five of the nine paths hold other blobs at `D`. Blob
  identity being authoritative (:46–48), this is not a differing pin under :62–63. It is the drift recorded in the
  start-state note.
- **X5 — shortened paths.** The freeze's table gives four paths without their directory prefix (:57–60). Each is
  resolved by its blob at `445701c7` to one full path (*Evidence base*).

## Readings this control plane chooses, recorded rather than resolved

- **R1 — merged records under the evidence rule.** Item 2 of the evidence rule (:114) admits "a merged result
  note or preregistration". Owner decision 3 fixes the evidence base as the nine pins; item 2 therefore draws on the
  four pinned records, and on the freeze's own blob where the result note quotes the freeze. A passage of any other
  record is outside the evidence base and is not quoted as evidence.
- **R2 — "No census entry".** The non-doings (:408) say "No census entry"; `WD4` (:258) calls its list "a census".
  The first is read as the Lean-to-manuscript census registry (`verification/lean-manuscript-census.json`, §A.35),
  which this round does not govern; the second is the list in the result note.
- **R3 — the pointers.** The execution discipline (:414–415) allows "the `ROADMAP` and `README` pointers the
  round's own section needs", and the non-doings say "No `ROADMAP` label moved" (:408). The pointers are realized
  as added lines only, in `verification/ROADMAP.md` and `verification/README.md`, with no line removed or changed,
  so no label moves; and the post-round sentence is not among them, since it is written "in the result note and
  nowhere else" (:285). `T6` measures both. Adding no pointer is allowed.
- **R4 — the result note's form.** The freeze fixes what the final report contains, not its layout. This control
  plane fixes a layout (*The result note*) so that the controls can read it: named sections, one field line per
  recorded determination, and quotations and searches in fenced blocks that name their blob and lines. The field
  lines restate the freeze's own determinations in its words; `N9` checks only the necessary conditions the freeze
  states for `WD3-yes` and `WD3-no` and the second sentence of its gate. Whether the frozen requirements are met in
  substance — that a quotation carries the determination it is cited for, that `H_obs` is established no stronger
  than the `ST3`/`ST4` family — stays the executor's determination under the frozen text, checked by the reviewer.
- **R5 — act 14 at each mention.** The clause is carried "verbatim wherever act 14 is named" (:128–129). This is
  measured per section: a section of the result note that names act 14, or cites its blob, contains the clause
  verbatim (`N11`).
- **R6 — strength per determination.** The freeze records strength per determination (:123), not per target. Each
  determination in the result note carries its own strength line, so each target section carries at least one, each
  with one of the frozen four values (`N6`). That every determination has its strength, and that a passage naming a
  thing without displaying it is at most `medium` (:124), is checked by the reviewer at `E`.

## The non-verdict section

Owner decision 3 directs that how the historical findings bear on the corrected contemporary theory be recorded
separately, without changing the frozen verdict. The result note's section **Bearing on the contemporary theory
(not a verdict)** does that, under these limits:

1. It opens with the sentence: "This section is not a verdict: no target, outcome or strength rests on it, and it
   does not change the frozen verdict above." (`N16`)
2. It carries no outcome, evidence, strength, quantifier or field line, and no evidence quotation or search
   (`N4`, `N16`). It may carry analysis quotations from the evidence base and context quotations.
3. A context quotation names a commit that descends from `D`, a path and lines, and is checked verbatim there
   (`N3`); the commit is reachable from `main` when `E` is designated (§A.42 item 3; the reviewer at `E`). It never
   quotes a path of a 24.1C record (`N4`).
4. SC-44 (#980), SC-45 (#981) and any later manuscript change enter only as context: by number, or by a context
   quotation of a commit on `main`. None is a premise of any target.
5. Nothing in it moves a target's outcome or strength, the post-round sentence, or the `P1` label.

## The result note, its frozen form

`result.md`, LF line ends. Outside fenced blocks, a line beginning `# ` is the title (exactly one, before the first
section), a line beginning `## ` opens a section and a line beginning `### ` a subsection. The sections are exactly
these, in this order:

1. `## Start state` — the pin and freeze checks, the start-state note, and the independence sentence
   (*Independence*). A start state that names act 14's pin by its path (`act-14-threading-observability`) or its
   blob names act 14, and so carries the act 14 clause as well (`N11`).
2. `## WD0`, `## WD1`, `## WD1-q`, `## WD2`, `## WD2-q`, `## WD3`, `## WD4` — the targets.
3. `## Discrepancies` — the freeze's discrepancies (X1 among them) and any the execution finds.
4. `## Post-round sentence` — the one frozen sentence, verbatim (blockquote markers and line breaks are
   immaterial).
5. `## Bearing on the contemporary theory (not a verdict)` — *The non-verdict section*.
6. `## Checks` — the command and expected result of the controls (§A.42 item 1).

**Target sections.** Each carries exactly one line `Outcome: …`, at least one line `Evidence: P`, at least one line
`Strength: full|high|medium|UNDECIDED`, and at least one evidence quotation or search. The `WD3` outcome line is
exactly `Outcome: WD3-yes`, `Outcome: WD3-no` or `Outcome: WD3-UNDECIDED`, optionally followed by a space and
further text. `WD1` and `WD1-q` each carry the subsections `### The equivalence relation ∼`,
`### Theorem 24's statement`, `### Step 1` and `### The Scope paragraph`, in that order, each with at least one
quotation (a search is also admitted under `WD1`); each `WD1-q` subsection carries one line
`Quantifier: fixed-partition|all-partitions|unstated` (:172–174). The field lines, each exactly once in its section:

| section | field line | values | the freeze's words |
| --- | --- | --- | --- |
| `WD1` | `Enumeration complete:` | `yes`, `no` | "the enumeration of `WD1` to be complete on the record searched" (:222–223) |
| `WD2` | `(b) in O_set:` | `yes`, `no` | "whether (b) appears in `O_set`" (:193) |
| `WD2` | `(b) determined by (a), asserted:` | `yes`, `no` | "whether any passage asserts (b) is determined by (a)" (:193–194) |
| `WD2` | `(b) not determined by (a), asserted:` | `yes`, `no` | "whether any passage asserts it is not" (:194) |
| `WD2` | `Question posed:` | `yes`, `no` | "whether the question is posed at all" (:194) |
| `WD2-q` | `ST3/ST4 partitions:` | `fixed-partition`, `all-partitions`, `unsettled` | part 1 (:206–207) |
| `WD2-q` | `All-partitions family settled:` | `yes`, `no` | whether the record establishes whether the all-partitions family fixes the block-word traces (:208–213, :233–235) |
| `WD3` | `Gate:` | `established`, `not-established` | the gating condition on `WD3-no` (:228–235) |

A value may be followed by a space or punctuation and further text.

**Fenced blocks.** An opener is a line of three backticks followed by an info string; the block ends at the next
line of exactly three backticks. The info strings admitted:

- `quote <blob> <a>-<b>` — an evidence quotation: lines `a`–`b` of the blob, 1-based. The body is a non-empty
  substring of those lines joined by LF, and of neither lines `a+1`–`b` nor `a`–`b-1`, so the coordinates are
  tight (`N3`). The blob is one of the nine pins or `f614b666`, never act 14's, and the block lies in the start
  state, a target section or the discrepancies (`N4`).
- `analysis-quote <blob> <a>-<b>` — a quotation in an analysis paragraph: the same verbatim rule, a blob of the
  evidence base (act 14's included), any section but the post-round sentence and the checks; a section that holds
  one carries the label "Analysis, not evidence; no target rests on it." (`N12`).
- `search <n> <blob> [<blob> …]` — a named, bounded search (evidence rule item 3): the body's non-blank lines are
  Python regular expressions, and `n` is the number of lines of the listed blobs that match at least one of them
  (`N5`). Blobs of the evidence base other than act 14's; the same sections as `quote`.
- `context-quote <commit> <path> <a>-<b>` — only in the non-verdict section (*The non-verdict section*).
- `text` — command output and other literal text; not evidence.

**Sentences.** The type-P statement the freeze requires (:375–377) is written exactly as "This round is type P
throughout: no Lean is written, no target is at evidence level 2, there is no axiom table and there is no
`#print axioms` line." (`N15`). Exactly one of the three frozen post-round sentences (:289–298, :302–306,
:310–313) occurs outside fenced blocks, once, in the post-round section, and it is the one for the `WD3` outcome
(`N10`). Outside fenced blocks and that sentence, no forbidden sentence of the non-licences (:325–328, :340) occurs
(`N13`). The act 14 clause (:131–134) occurs verbatim in every section that names act 14 (`N11`).

## The frozen controls

`controls.py`, committed at stage 1 at
`verification/programmes/substratum/round-sub-241b-observables-v3/controls.py`. Its text is the body of the one
fenced block of this file whose opener is three backticks followed by `python` (*The frozen `controls.py`*),
followed by one LF. The frozen blob of `controls.py` is `ddf80e63dcef87f15ceb9e47b70543940df5cd0b`.

Extraction, from the repository root, with `F` the designated commit:

    git show F:verification/programmes/substratum/round-sub-241b-observables-v3/preregistration.md \
      | python3 -I -c "import sys; t = sys.stdin.read().split(chr(10)); i = t.index(chr(96) * 3 + 'python'); j = t.index(chr(96) * 3, i + 1); sys.stdout.write(chr(10).join(t[i + 1:j]) + chr(10))" \
      > controls.py && git hash-object controls.py

It reads git objects and its own file only, standard library, run with `python3 -I` from the repository root:
`--self-test`; `check <E> --freeze <F>`, every checkpoint below at `E`; `note <C>`, the note checks alone, a
drafting aid that is never an acceptance. The three post-round sentences, the act 14 clause and the forbidden
sentences are read from blob `f614b666` itself, at the lines named above, not from a copy.

| check | measures |
| --- | --- |
| `T1` | `D` is an ancestor of `F`, `F` of `E`, `E` ≠ `F`, and every commit of `F..E` has one parent, `F` or another of them |
| `T2` | the control-plane files at `E` are exactly those at `F`; the preregistration at `F` names the controls blob once; `controls.py` at `E` and the running file are that blob |
| `T3` | the legacy file is blob `f614b666` at `445701c7`, at `F` and at `E` |
| `T4` | `445701c7` is an ancestor of `D`, and each of the nine paths holds its pinned blob there |
| `T5` | every path of `delta(F, E)` lies in the record directory or is one of the two execution paths; the record directory at `E` holds no file other than the control-plane files at `F`, `result.md` and `controls.py`, and the last two are present |
| `T6` | in `delta(F, E)` the two execution paths only gain lines, and the added text carries no post-round sentence |
| `T7` | the preregistration at `F` carries exactly three `quote` blocks, of `f614b666` lines 3–349, 351–365 and 367–438 in that order, and each block's body is exactly those lines |
| `N1` | the title and the twelve sections, in order |
| `N2` | every fence closed and every info string well formed |
| `N3` | every quotation verbatim with tight coordinates; context commits descend from `D` |
| `N4` | evidence quotations and searches from the evidence base only, act 14 never as evidence, each kind in its sections |
| `N5` | every search's count reproduces |
| `N6` | each target's outcome, evidence, strength lines and its quotation or search |
| `N7` | the four statements under `WD1` and `WD1-q`, in order, quoted, with one quantifier each under `WD1-q` |
| `N8` | the field lines and the `WD3` outcome token |
| `N9` | `WD3-yes` only with (b) in `O_set` or (a) asserted to determine (b) (:219–221); `WD3-no` only with the enumeration complete, (b) absent, no such assertion and the gate established (:222–225); the gate not established when a quantifier is all-partitions and the all-partitions family is not settled (:233–235) |
| `N10` | exactly one frozen post-round sentence, once, in its section, the one for the outcome |
| `N11` | the act 14 clause in each section naming act 14 |
| `N12` | the analysis label beside each analysis quotation |
| `N13` | no forbidden sentence outside quotation and the frozen sentence |
| `N14` | no 24.1C or SUB-241C-SPAN reference outside the start state, in text or in any block's info string or body; the independence sentence in the start state |
| `N15` | the type-P sentence |
| `N16` | the non-verdict section's disclaimer and no structural line in it, list and quote markers ignored |
| `N17` | the discrepancy section quotes the freeze at :160, :390, :420, :421 and :433 |

**The self-test** builds a valid note for each of the three outcomes from the real frozen blobs, and 37 mutations
of the `WD3-no` note, each of which must fail at exactly its named checks: an altered, shifted or widened
quotation, a quotation from outside the evidence base, act 14 as evidence or searched, a search count off by one, a
missing strength, an extra outcome, a non-P evidence line, reordered statements, a quantifier outside the three, a
`WD3` outcome outside the three tokens, `WD3-no` over each missing requirement and over an unsettled all-partitions
quantifier, `WD3-yes` without its requirement, the sentence twice, misplaced or for another outcome, act 14 named
without the clause, a forbidden sentence, a 24.1C premise in text or inside a block, a missing independence,
type-P, disclaimer or analysis label, a structural line in the non-verdict section, plain or list-marked, a target
with no quotation, an unquoted discrepancy line, an extra section, an unclosed fence and a misplaced context
quotation. In scratch repositories it builds `D`, `F` and `E`, with `F` quoting the three frozen spans in full, and
15 mutations of `E` or `F`: a manuscript changed, a pointer line removed, the preregistration changed or an
amendment added after `F`, a merge in `F..E`, `E` not descending from `F`, the legacy file changed, `controls.py`
not the frozen blob, the result note absent, an extra file in the record directory, the post-round sentence in the
`ROADMAP`, a pin that does not match, and the quotation of the freeze not verbatim, truncated or missing a frozen
span. It prints `controls: self-test OK (59 cases)`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane, and no control-plane file changes after `F` | `T2` at `E`; `v3_verifier.py --verify-round Q` (`G7`) |
| execution is linear from `F` | `T1` at `E`; the verifier at `Q` (`S3`) |
| every change lies inside the governed paths: no manuscript, Lean, guard, seal, certificate or other round's record | `T5` at `E`; the verifier at `Q` (`S7`, `G12`) |
| the legacy freeze stays byte for byte | `T3` at `E`; `tools/legacy_records_check.py` at every stage commit and at `Q` |
| the controls that run are the frozen ones and detect what they claim | stage 1's acceptance (`git rev-parse` of `controls.py` equal to the frozen blob); `T2`; `--self-test` OK at stage 1 and at `E` |
| the freeze is quoted verbatim in this control plane | `T7` at `E`; precondition 1 at candidate `F` |
| the evidence base is the nine pins, located at `445701c7` | `T4`, `N4` at `E` |
| every quotation is verbatim, with tight coordinates | `N3` at `E` |
| a finding of silence rests on a named, bounded search that reproduces | `N5` at `E` |
| act 14 enters as analysis only, with its clause at each mention | `N4`, `N11`, `N12` at `E` |
| each target records outcome, evidence type, strength and its quotation; the four statements reported separately, each with its quantifier | `N6`, `N7` at `E` |
| the `WD3` outcome meets the freeze's stated requirements | `N8`, `N9` at `E` for the necessary conditions; the reviewer at `E` for the rest (R4) |
| a determination rests on its quotation, not on reconstructive inference (hazard 1, :381–384) | the reviewer at `E`, reading each determination against the quotation the note names for it |
| exactly one frozen post-round sentence, verbatim, in the result note and nowhere else | `N10`, `T6` at `E` |
| no forbidden sentence | `N13` at `E` |
| no premise from SUB-241C-SPAN or any 24.1C result | `N4`, `N14` at `E` |
| the type-P statement | `N15` at `E` |
| the non-verdict section changes no verdict | `N4`, `N16` at `E` |
| the "three"/"four" discrepancy recorded | `N17` at `E` |
| the pointers only add lines; no label moves | `T6` at `E` |
| predictions are not amended | `T2` (this file unchanged after `F`) |
| the freeze's reviewer-checked requirements: strength recorded per determination, at most `medium` for a passage that names a thing without displaying it (:123–124); no act 14 carrier written as a candidate for `O_set`, nor `O_set` as such a carrier (:141–142); the `WD4` candidates checked, not assumed (:253–256); `ST3`/`ST4` consumed as established and unrevised (:197–199); a partition-quantifier obstruction named in the frozen terms and no others (:315–320); any landing above a predicted strength recorded with its reason (:277–278); and the checks the final report owes for hazards 1, 2 and 7 (:142, :383–384, :399–400) | the reviewer at `E`, item by item against the frozen text, with a verdict per item on the pull request |
| every stage requirement can be met from `F` (no checkpoint `F` cannot satisfy) | precondition 2 at candidate `F` |
| the round's records hold | `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`; `--receipts` in the release gate of the pull request's run at its head; on `main` only once `Q` is published there (*The protocol*) |
| a reconciliation adds exactly the execution's own changes | the verifier at `Q` (`S9`); the reviewer compares the landing with `delta(F, E)` (§A.39 item 3) |
| no push starts a governed launch | before each push, the push-triggered workflows and their filters are read against the branch and paths, with the result on the pull request (§A.43 item 4) |

## Stages and outcomes

`F` is given to `--freeze` as its full 40-character id; each stage commit has one parent.

1. **C1** adds `controls.py`, extracted from `F` by the recipe above. Acceptance: `git rev-parse
   C1:verification/programmes/substratum/round-sub-241b-observables-v3/controls.py` is the frozen blob, and
   `--self-test` prints OK; `legacy_records_check.py` passes.
2. **Drafting commits**, zero or more, add or revise `result.md` and the pointers. Each passes
   `legacy_records_check.py`.
3. **Candidate `E`**, the last of them. Acceptance: `controls.py --self-test` prints OK and
   `controls.py check E --freeze F` prints `controls: OK`, both run from the file at `E`; the exact-head run of
   `verify.yml` at `E` is green on every job; and the owner designates `E`.

**Outcomes.**

- **`SUB-241B-OBS-READ`** when stage 3's acceptance holds. The round's finding is then the `WD3` outcome the note
  records — `WD3-yes`, `WD3-no` or `WD3-UNDECIDED` — with its frozen sentence, and each target's outcome at its
  recorded strength.
- **`SUB-241B-OBS-HALTED`** otherwise (`S12`): when execution commits exist, a withdrawal commit restores both
  execution paths to their state at `F`; when none exist, a single-parent child of `F` that changes only record
  paths takes its place. Either carries the result note, which names the failing check or job.

No outcome edits a manuscript, the legacy record or another round's record, or moves the `P1` label. The round is
consistency-axis work: correctness bands are unchanged by either outcome.

## Preconditions of `F`

`F` is not designated until all four hold:

1. **The controls, as frozen.** At candidate `F`, `controls.py` extracted by the recipe has the frozen blob, and its
   `--self-test` prints `controls: self-test OK (59 cases)`. `T7` holds at candidate `F`. Run locally; the commands
   and output are recorded on the pull request.
2. **A mock execution.** A mock `C1` and a mock `E` are built from candidate `F` in a temporary object directory,
   with no ref: `E` adds the extracted `controls.py`, a result note built by the self-test's valid-note generator
   and one added `ROADMAP` line. `controls.py check <mock E> --freeze <candidate F>` prints `controls: OK`, and the
   same check on a mock `E` with one `ROADMAP` line removed fails at `T6` alone. The controls build their own git
   environment, so the mock run extends it in process with the temporary object directory, the repository's
   objects serving as a read-only alternate. This runs every stage-3 check against `F`'s own tree, so that a
   requirement `F` cannot meet fails before the freeze. Run locally; command and output recorded on the pull
   request.
3. **The exact-head run at candidate `F`.** `verify.yml` dispatched on exactly candidate `F`, green on every job: its
   `check-run` attestation. The dispatch needs the owner's authorization.
4. **The owner's designation of `F`.**

Preconditions 1 and 2 are design evidence for the executor and reviewers, not `check-run` attestations.

## The frozen `controls.py`

```python
#!/usr/bin/env python3
"""controls.py -- the frozen controls of round SUB-241B-OBS (type P, non-sealing).

Usage, from the repository root:

    python3 -I <record directory>controls.py --self-test
    python3 -I <record directory>controls.py check <E> --freeze <F>
    python3 -I <record directory>controls.py note <C>

--self-test        result notes built from the real frozen blobs, and scratch repositories; the
                   valid cases must pass and every mutation must fail at exactly its named checks.
check E --freeze F every checkpoint the preregistration assigns to E: T1-T6 on the commits, N1-N17
                   on the result note at E. One line per check, then 'controls: OK' or
                   'controls: FAILED' (exit 1).
note C             N1-N17 on the result note at commit C, a drafting aid and never an acceptance.

Commit arguments are full 40-digit lowercase object ids. The tool reads git objects and its own
file, and nothing else: no ref, branch, other working-tree file, network or clock. Standard library
only.
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile

RDIR = 'verification/programmes/substratum/round-sub-241b-observables-v3/'
PREREG = RDIR + 'preregistration.md'
NOTE = RDIR + 'result.md'
CONTROLS = RDIR + 'controls.py'
D = '0d917665d32287e5d0ce649012175f2c7bf75b09'
B0 = '445701c764245d17a55b4c401b41f3333a9c4b02'
LEGACY_PATH = 'verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md'
LEGACY = 'f614b666ad9098f866969c4c524e47f504e5d71c'
ACT14 = 'd4815d56b1cea2ed42540a7d6262c3c4201ac9b7'
PINS = (
    ('papers/Substratum.md', '9ac6b732e8786897cade416b67c3f7f1df81ab84'),
    ('papers/Explainer.md', 'b0926875346305ef053995fc10695353df64de68'),
    ('papers/Methodology.md', '1d332b0c9256e33861af0ce3b5598091b63d30a1'),
    ('papers/Structure.md', '84a7ede451a917513dd488477c93180f5f8c0486'),
    ('papers/Complexity.md', 'dd38c5b39797433b6f5de469f5711fd38b116441'),
    ('verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/preregistration.md',
     '98cfcfdc0e74ffe0186c502517a842bfeb25d351'),
    ('verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md',
     '124a02c9d2b17c0cf280f15a00ab269f68e33a24'),
    ('verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md',
     'b5822febb2626af48c29f6198fd6d74637ef9896'),
    ('verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md', ACT14),
)
ADMITTED = frozenset([b for _, b in PINS] + [LEGACY])
EXEC_PATHS = ('verification/README.md', 'verification/ROADMAP.md')

SECTIONS = ('Start state', 'WD0', 'WD1', 'WD1-q', 'WD2', 'WD2-q', 'WD3', 'WD4', 'Discrepancies',
            'Post-round sentence', 'Bearing on the contemporary theory (not a verdict)', 'Checks')
TARGETS = SECTIONS[1:8]
EVIDENCE_SECTIONS = SECTIONS[:9]
POST = SECTIONS[9]
CONTEMPORARY = SECTIONS[10]
STATEMENTS = ('The equivalence relation ∼', "Theorem 24's statement", 'Step 1',
              'The Scope paragraph')
TAIL = r'(?:[ ;,.(—–].*)?'
FIELDS = (
    ('WD1', 'Enumeration complete', ('yes', 'no')),
    ('WD2', '(b) in O_set', ('yes', 'no')),
    ('WD2', '(b) determined by (a), asserted', ('yes', 'no')),
    ('WD2', '(b) not determined by (a), asserted', ('yes', 'no')),
    ('WD2', 'Question posed', ('yes', 'no')),
    ('WD2-q', 'ST3/ST4 partitions', ('fixed-partition', 'all-partitions', 'unsettled')),
    ('WD2-q', 'All-partitions family settled', ('yes', 'no')),
    ('WD3', 'Gate', ('established', 'not-established')),
)
QUANTIFIERS = ('fixed-partition', 'all-partitions', 'unstated')
WD3_TOKENS = ('WD3-no', 'WD3-yes', 'WD3-UNDECIDED')
SENTENCE_LINES = {'WD3-no': (289, 298), 'WD3-yes': (302, 306), 'WD3-UNDECIDED': (310, 313)}
CLAUSE_LINES = (131, 134)
FORBIDDEN_LINES = ((325, 328), (340, 340))
DISCREPANCY_LINES = (160, 390, 420, 421, 433)
ADOPTED_SPANS = ((3, 349), (351, 365), (367, 438))
TYPE_P = ('This round is type P throughout: no Lean is written, no target is at evidence level 2, '
          'there is no axiom table and there is no `#print axioms` line.')
INDEPENDENCE = 'No premise of this round comes from SUB-241C-SPAN or from any 24.1C result.'
DISCLAIMER = ('This section is not a verdict: no target, outcome or strength rests on it, and it '
              'does not change the frozen verdict above.')
ANALYSIS_LABEL = 'Analysis, not evidence; no target rests on it.'
INDEP = re.compile(r'24\.1c|24-1c|sub-241c|#986', re.I)
ACT14_MENTION = re.compile(r'\bact[ -]?14\b|' + ACT14[:8], re.I)
FENCE = '`' * 3
HEX40 = re.compile(r'[0-9a-f]{40}')
CONTROLS_PIN = re.compile(r'The frozen blob of `controls\.py` is `([0-9a-f]{40})`\.')
STRUCTURAL_PREFIXES = ('Outcome:', 'Evidence:', 'Strength:', 'Quantifier:') + tuple(
    k + ':' for _, k, _ in FIELDS)

ENV = {'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'LC_ALL': 'C', 'LANG': 'C',
       'HOME': '/nonexistent-sub241b', 'GIT_CONFIG_NOSYSTEM': '1',
       'GIT_CONFIG_GLOBAL': '/dev/null', 'GIT_TERMINAL_PROMPT': '0', 'GIT_OPTIONAL_LOCKS': '0'}
COMMIT_ENV = dict(ENV, GIT_AUTHOR_NAME='s', GIT_AUTHOR_EMAIL='s@invalid',
                  GIT_AUTHOR_DATE='1700000000 +0000', GIT_COMMITTER_NAME='s',
                  GIT_COMMITTER_EMAIL='s@invalid', GIT_COMMITTER_DATE='1700000000 +0000')


# ---------------------------------------------------------------------------------------------
# git objects
# ---------------------------------------------------------------------------------------------
class Git:
    def __init__(self, cwd='.'):
        self.cwd = cwd
        self.cache = {}

    def run(self, args, data=None, env=None):
        r = subprocess.run(['git'] + args, cwd=self.cwd, input=data, capture_output=True,
                           env=env or ENV)
        return r.stdout if r.returncode == 0 else None

    def blob(self, oid):
        if oid not in self.cache:
            out = self.run(['cat-file', 'blob', oid]) if HEX40.fullmatch(oid or '') else None
            try:
                self.cache[oid] = None if out is None else out.decode('utf-8')
            except UnicodeDecodeError:
                self.cache[oid] = None
        return self.cache[oid]

    def lines(self, oid):
        t = self.blob(oid)
        if t is None:
            return None
        ls = t.split('\n')
        return ls[:-1] if ls and ls[-1] == '' else ls

    def commit(self, oid):
        return bool(HEX40.fullmatch(oid or '')) and \
            self.run(['cat-file', '-e', oid + '^{commit}']) is not None

    def at(self, commit, path):
        out = self.run(['ls-tree', '--full-tree', commit, '--', path])
        if not out:
            return None
        meta = out.decode('utf-8', 'replace').split('\t', 1)[0].split()
        return meta[2] if meta[1] == 'blob' else None

    def files(self, commit, prefix):
        out = self.run(['ls-tree', '-r', '--full-tree', '-z', commit])
        res = {}
        for rec in (out or b'').split(b'\0'):
            if rec:
                meta, path = rec.decode('utf-8', 'replace').split('\t', 1)
                if path.startswith(prefix):
                    res[path] = tuple(meta.split())
        return res

    def ancestor(self, a, b):
        return subprocess.run(['git', 'merge-base', '--is-ancestor', a, b], cwd=self.cwd,
                              capture_output=True, env=ENV).returncode == 0

    def parents(self, c):
        out = self.run(['rev-list', '--parents', '-n', '1', c])
        return out.decode().split()[1:] if out else None

    def revlist(self, head, exclude):
        out = self.run(['rev-list', head, '^' + exclude])
        return out.decode().split() if out is not None else None

    def changed(self, a, b):
        out = self.run(['diff-tree', '-r', '--no-renames', '--name-only', '-z', a, b])
        return [p.decode('utf-8', 'replace') for p in (out or b'').split(b'\0') if p]

    def patch(self, a, b, path):
        out = self.run(['diff-tree', '-p', '--no-renames', '--unified=0', a, b, '--', path])
        return (out or b'').decode('utf-8', 'replace').split('\n')


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def norm(text):
    """Blockquote markers removed line by line, whitespace runs collapsed, ends trimmed."""
    return re.sub(r'\s+', ' ', ' '.join(re.sub(r'^\s*(?:>\s?)+', '', ln)
                                        for ln in text.split('\n'))).strip()


# ---------------------------------------------------------------------------------------------
# the frozen text, read from the legacy blob itself
# ---------------------------------------------------------------------------------------------
def frozen(git):
    ls = git.lines(LEGACY)
    if ls is None:
        raise SystemExit('controls: the legacy blob %s is absent' % LEGACY)

    def span(a, b):
        return norm('\n'.join(ls[a - 1:b]))
    phrases = []
    for a, b in FORBIDDEN_LINES:
        phrases += re.findall(r'"([^"]+)"', span(a, b))
    return {'sentences': {t: span(a, b) for t, (a, b) in SENTENCE_LINES.items()},
            'clause': span(*CLAUSE_LINES), 'forbidden': phrases}


# ---------------------------------------------------------------------------------------------
# the result note
# ---------------------------------------------------------------------------------------------
class Note:
    """Sections ('## '), subsections ('### '), plain lines and fenced blocks, without Markdown
    semantics beyond these."""

    def __init__(self, text):
        self.errors = []
        self.titles = 0
        self.order = []
        self.plain = {'': []}
        self.blocks = []
        sec, sub = '', None
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            ln = lines[i]
            if ln.startswith(FENCE):
                info = ln[3:]
                j = i + 1
                while j < len(lines) and lines[j] != FENCE:
                    j += 1
                if j == len(lines):
                    self.errors.append('unclosed fence at line %d' % (i + 1))
                    break
                self.blocks.append({'info': info, 'body': lines[i + 1:j], 'section': sec,
                                    'sub': sub, 'line': i + 1})
                i = j + 1
                continue
            if ln.startswith('## '):
                sec, sub = ln[3:], None
                self.order.append(sec)
                self.plain.setdefault(sec, [])
            elif ln.startswith('### '):
                sub = ln[4:]
                self.plain[sec].append((sub, ln, True))
                i += 1
                continue
            elif ln.startswith('# '):
                if sec == '':
                    self.titles += 1
                else:
                    self.errors.append('a title line inside section %s' % sec)
            if not ln.startswith('## '):
                self.plain[sec].append((sub, ln, False))
            i += 1

    def text(self, sec):
        return '\n'.join(ln for _, ln, _ in self.plain.get(sec, []))

    def all_text(self):
        return '\n'.join(self.text(s) for s in [''] + self.order)

    def lines(self, sec):
        return [ln for _, ln, h in self.plain.get(sec, []) if not h]

    def subs(self, sec):
        return [s for s, _, h in self.plain.get(sec, []) if h]

    def sub_lines(self, sec, sub):
        return [ln for s, ln, h in self.plain.get(sec, []) if s == sub and not h]

    def in_section(self, sec, kinds, sub=None):
        return [b for b in self.blocks if b['section'] == sec and kind(b) in kinds
                and (sub is None or b['sub'] == sub)]


def kind(b):
    return b['info'].split(' ', 1)[0]


def block_args(b):
    """(kind, args) or (kind, None) when the info string is malformed."""
    k, parts = kind(b), b['info'].split(' ')
    rng = re.compile(r'([1-9][0-9]*)-([1-9][0-9]*)')
    if k in ('quote', 'analysis-quote') and len(parts) == 3 and HEX40.fullmatch(parts[1]):
        m = rng.fullmatch(parts[2])
        if m and int(m.group(1)) <= int(m.group(2)):
            return k, (parts[1], int(m.group(1)), int(m.group(2)))
    if k == 'context-quote' and len(parts) == 4 and HEX40.fullmatch(parts[1]) and parts[2]:
        m = rng.fullmatch(parts[3])
        if m and int(m.group(1)) <= int(m.group(2)):
            return k, (parts[1], parts[2], int(m.group(1)), int(m.group(2)))
    if k == 'search' and len(parts) >= 3 and re.fullmatch(r'0|[1-9][0-9]*', parts[1]) \
            and all(HEX40.fullmatch(p) for p in parts[2:]):
        body = [x for x in b['body'] if x.strip()]
        try:
            pats = [re.compile(x) for x in body]
        except re.error:
            return k, None
        if pats:
            return k, (int(parts[1]), parts[2:], pats)
    if k == 'text':
        return k, ()
    return k, None


def verbatim(lines, a, b, body):
    """The body is a non-empty substring of lines a..b that neither lines a+1..b nor a..b-1
    contain."""
    if lines is None or b > len(lines):
        return False
    s = '\n'.join(body)
    if not s.strip() or s not in '\n'.join(lines[a - 1:b]):
        return False
    return a == b or (s not in '\n'.join(lines[a:b]) and s not in '\n'.join(lines[a - 1:b - 1]))


def field(lines, key, values):
    """The value of the one line '<key>: <value>', or None with a reason."""
    hits = [ln for ln in lines if ln.startswith(key + ':')]
    if len(hits) != 1:
        return None, '%d line(s) %r' % (len(hits), key + ':')
    m = re.fullmatch(re.escape(key) + ': (' + '|'.join(map(re.escape, values)) + ')' + TAIL,
                     hits[0])
    return (m.group(1), None) if m else (None, 'value of %r' % key)


def note_checks(git, text, fz):
    """[(check id, [failure details])] for N1-N17."""
    n = Note(text)
    res = []

    def put(cid, fails):
        res.append((cid, fails))

    # N1 sections
    f = []
    if tuple(n.order) != SECTIONS:
        f.append('sections %r' % (n.order,))
    if n.titles != 1:
        f.append('%d title line(s)' % n.titles)
    f += [e for e in n.errors if e.startswith('a title')]
    put('N1', f)
    # N2 fences
    f = [e for e in n.errors if e.startswith('unclosed')]
    for b in n.blocks:
        k, args = block_args(b)
        if args is None:
            f.append('malformed block at line %d: %r' % (b['line'], b['info']))
    put('N2', f)
    good = [(b,) + block_args(b) for b in n.blocks if block_args(b)[1] is not None]
    # N3 verbatim
    f = []
    for b, k, args in good:
        if k in ('quote', 'analysis-quote'):
            if not verbatim(git.lines(args[0]), args[1], args[2], b['body']):
                f.append('line %d: not verbatim at %s %d-%d' % ((b['line'],) + args))
        elif k == 'context-quote':
            c, path, a, z = args
            if not git.commit(c) or not git.ancestor(D, c):
                f.append('line %d: %s is not a commit descending from D' % (b['line'], c))
                continue
            oid = git.at(c, path)
            if oid is None or not verbatim(git.lines(oid), a, z, b['body']):
                f.append('line %d: not verbatim at %s:%s %d-%d' % (b['line'], c, path, a, z))
    put('N3', f)
    # N4 evidence base and placement
    f = []
    for b, k, args in good:
        where = b['section']
        if k == 'quote' and (args[0] not in ADMITTED or args[0] == ACT14
                             or where not in EVIDENCE_SECTIONS):
            f.append('line %d: quote of %s in %r' % (b['line'], args[0], where))
        if k == 'analysis-quote' and (args[0] not in ADMITTED
                                      or where not in EVIDENCE_SECTIONS + (CONTEMPORARY,)):
            f.append('line %d: analysis-quote of %s in %r' % (b['line'], args[0], where))
        if k == 'context-quote' and (where != CONTEMPORARY or INDEP.search(args[1])):
            f.append('line %d: context-quote of %s in %r' % (b['line'], args[1], where))
        if k == 'search' and (not set(args[1]) <= ADMITTED or ACT14 in args[1]
                              or where not in EVIDENCE_SECTIONS):
            f.append('line %d: search over %s in %r' % (b['line'], args[1], where))
    put('N4', f)
    # N5 searches reproduce
    f = []
    for b, k, args in good:
        if k == 'search':
            got = 0
            for oid in args[1]:
                got += sum(1 for ln in (git.lines(oid) or []) if any(p.search(ln) for p in args[2]))
            if got != args[0]:
                f.append('line %d: %d line(s) match, %d recorded' % (b['line'], got, args[0]))
    put('N5', f)
    # N6 targets
    f = []
    for t in TARGETS:
        ls = n.lines(t)
        out = [ln for ln in ls if ln.startswith('Outcome:')]
        if len(out) != 1 or not out[0][len('Outcome:'):].strip():
            f.append('%s: %d outcome line(s)' % (t, len(out)))
        ev = [ln for ln in ls if ln.startswith('Evidence:')]
        if not ev or not all(re.fullmatch('Evidence: P' + TAIL, ln) for ln in ev):
            f.append('%s: evidence lines' % t)
        st = [ln for ln in ls if ln.startswith('Strength:')]
        if not st or not all(re.fullmatch('Strength: (full|high|medium|UNDECIDED)' + TAIL, ln)
                             for ln in st):
            f.append('%s: strength lines' % t)
        if not n.in_section(t, ('quote', 'search')):
            f.append('%s: no quote or search' % t)
    put('N6', f)
    # N7 the four statements
    f = []
    quants = []
    for t in ('WD1', 'WD1-q'):
        if tuple(n.subs(t)) != STATEMENTS:
            f.append('%s: subsections %r' % (t, n.subs(t)))
            continue
        for s in STATEMENTS:
            kinds = ('quote',) if t == 'WD1-q' else ('quote', 'search')
            if not n.in_section(t, kinds, s):
                f.append('%s / %s: no quotation' % (t, s))
            if t == 'WD1-q':
                v, why = field(n.sub_lines(t, s), 'Quantifier', QUANTIFIERS)
                if v is None:
                    f.append('%s / %s: %s' % (t, s, why))
                quants.append(v)
    put('N7', f)
    # N8 fields
    f = []
    vals = {}
    for t, key, values in FIELDS:
        v, why = field(n.lines(t), key, values)
        if v is None:
            f.append('%s: %s' % (t, why))
        vals[key] = v
    out = [ln for ln in n.lines('WD3') if ln.startswith('Outcome:')]
    m = re.fullmatch('Outcome: (' + '|'.join(WD3_TOKENS) + ')' + TAIL, out[0]) \
        if len(out) == 1 else None
    tok = m.group(1) if m else None
    if tok is None:
        f.append('WD3: outcome token')
    put('N8', f)
    # N9 the frozen WD3 decision rule, as consistency
    f = []
    if tok is None or None in vals.values() or len(quants) != 4 or None in quants:
        f.append('inputs unavailable')
    else:
        if 'all-partitions' in quants and vals['All-partitions family settled'] == 'no' \
                and vals['Gate'] == 'established':
            f.append('gate established over an unsettled all-partitions quantifier')
        if tok == 'WD3-no' and not (vals['Gate'] == 'established'
                                    and vals['Enumeration complete'] == 'yes'
                                    and vals['(b) in O_set'] == 'no'
                                    and vals['(b) determined by (a), asserted'] == 'no'):
            f.append('WD3-no without its requirements')
        if tok == 'WD3-yes' and not (vals['(b) in O_set'] == 'yes'
                                     or vals['(b) determined by (a), asserted'] == 'yes'):
            f.append('WD3-yes without its requirement')
    put('N9', f)
    # N10 the post-round sentence
    f = []
    whole = norm(n.all_text())
    counts = {t: whole.count(s) for t, s in fz['sentences'].items()}
    if tok is None or sum(counts.values()) != 1 or counts.get(tok) != 1 \
            or fz['sentences'][tok] not in norm(n.text(POST)):
        f.append('sentence counts %r for %r' % (counts, tok))
    put('N10', f)
    # N11 the act 14 clause wherever act 14 is named
    f = []
    for s in [''] + n.order:
        named = ACT14_MENTION.search(n.text(s)) or any(
            b['section'] == s and ACT14 in b['info'] for b in n.blocks)
        if named and fz['clause'] not in norm(n.text(s)):
            f.append('section %r names act 14 without the clause' % s)
    put('N11', f)
    # N12 analysis label
    f = [s for s in n.order if n.in_section(s, ('analysis-quote',))
         and ANALYSIS_LABEL not in norm(n.text(s))]
    put('N12', ['section %r: analysis-quote without the label' % s for s in f])
    # N13 forbidden sentences, outside quotation and the frozen sentence
    scan = whole
    for s in fz['sentences'].values():
        scan = scan.replace(s, ' ')
    scan = scan.lower()
    put('N13', [p for p in fz['forbidden'] if norm(p).lower() in scan])
    # N14 independence
    f = ['section %r' % s for s in [''] + n.order if s != 'Start state'
         and INDEP.search(n.text(s))]
    f += ['block at line %d' % b['line'] for b in n.blocks if b['section'] != 'Start state'
          and INDEP.search(b['info'] + '\n' + '\n'.join(b['body']))]
    if INDEPENDENCE not in norm(n.text('Start state')):
        f.append('the independence sentence is absent from the start state')
    put('N14', f)
    # N15 type P
    put('N15', [] if TYPE_P in whole else ['the type-P sentence is absent'])
    # N16 the contemporary section
    f = [] if DISCLAIMER in norm(n.text(CONTEMPORARY)) else ['the disclaimer is absent']
    f += ['structural line %r' % ln for ln in n.lines(CONTEMPORARY)
          if ln.lstrip('-*> \t').startswith(STRUCTURAL_PREFIXES)]
    put('N16', f)
    # N17 discrepancies quote both counts
    cov = [args for b, k, args in good if k == 'quote' and b['section'] == 'Discrepancies'
           and args[0] == LEGACY]
    put('N17', ['legacy line %d not quoted' % x for x in DISCREPANCY_LINES
                if not any(a <= x <= z for _, a, z in cov)])
    return res


# ---------------------------------------------------------------------------------------------
# the commits
# ---------------------------------------------------------------------------------------------
def tree_checks(git, e, f, own, d=D, b0=B0, pins=PINS):
    """[(check id, [failure details])] for T1-T6. `own` is the running file's bytes."""
    res = []
    # T1 linear from F, F from D
    fl = []
    if not (git.commit(e) and git.commit(f) and git.commit(d)):
        return [('T1', ['a commit is absent'])]
    if e == f or not git.ancestor(f, e) or not git.ancestor(d, f):
        fl.append('ancestry')
    else:
        listed = git.revlist(e, f) or []
        for c in listed:
            ps = git.parents(c)
            if ps is None or len(ps) != 1 or (ps[0] != f and ps[0] not in listed):
                fl.append('%s is not a single-parent link' % c)
    res.append(('T1', fl))
    # T2 the control plane and the frozen controls
    fl = []

    def cp(c):
        return {p: v for p, v in git.files(c, RDIR).items()
                if p == PREREG or p.startswith(RDIR + 'amendments/')}
    if cp(e) != cp(f) or PREREG not in cp(f):
        fl.append('control plane differs between F and E')
    pins_found = CONTROLS_PIN.findall(git.blob(git.at(f, PREREG) or '') or '')
    if len(pins_found) != 1:
        fl.append('%d controls pin(s) in the preregistration at F' % len(pins_found))
    elif git.at(e, CONTROLS) != pins_found[0] or blob_id(own) != pins_found[0]:
        fl.append('controls.py at E or the running file is not the frozen blob')
    res.append(('T2', fl))
    # T3 the legacy freeze
    res.append(('T3', [c for c in (b0, f, e) if git.at(c, LEGACY_PATH) != LEGACY]))
    # T4 the evidence base at the original base
    fl = [] if git.commit(b0) and git.ancestor(b0, d) else ['the original base is not under D']
    fl += [p for p, oid in pins if git.at(b0, p) != oid]
    res.append(('T4', fl))
    # T5 scope
    fl = [p for p in git.changed(f, e) if not (p.startswith(RDIR) or p in EXEC_PATHS)]
    fl += [p for p in (NOTE, CONTROLS) if git.at(e, p) is None]
    allowed = set(cp(f)) | {NOTE, CONTROLS}
    fl += ['%s: not a file of the record directory' % p for p in git.files(e, RDIR)
           if p not in allowed]
    res.append(('T5', fl))
    # T6 pointers: additions only, and never the post-round sentence
    fl = []
    fz = frozen(git)
    for p in EXEC_PATHS:
        lines, hunk = [], False
        for ln in git.patch(f, e, p):
            hunk = hunk or ln.startswith('@@')
            if hunk and not ln.startswith('@@'):
                lines.append(ln)
        if any(ln.startswith('-') for ln in lines):
            fl.append('%s: a line removed or changed' % p)
        added = norm('\n'.join(ln[1:] for ln in lines if ln.startswith('+')))
        if any(s in added for s in fz['sentences'].values()):
            fl.append('%s: carries a post-round sentence' % p)
    res.append(('T6', fl))
    # T7 the preregistration quotes the legacy freeze completely: exactly the frozen spans, each
    # block's body equal to those lines
    pre = Note(git.blob(git.at(f, PREREG) or '') or '')
    quotes = [b for b in pre.blocks if kind(b) == 'quote']
    spans = [block_args(b)[1] for b in quotes]
    fl = []
    if None in spans or [s[0] for s in spans] != [LEGACY] * len(spans) \
            or [(s[1], s[2]) for s in spans] != list(ADOPTED_SPANS):
        fl.append('quote spans %r' % ([s[1:] if s else None for s in spans],))
    else:
        legacy = git.lines(LEGACY) or []
        fl += ['preregistration line %d: body is not lines %d-%d' % (b['line'], s[1], s[2])
               for b, s in zip(quotes, spans) if b['body'] != legacy[s[1] - 1:s[2]]]
    res.append(('T7', fl))
    return res


def report(results):
    ok = True
    for cid, fails in results:
        print('%s  %s%s' % ('PASS' if not fails else 'FAIL', cid,
                            '' if not fails else '  ' + '; '.join(fails)))
        ok = ok and not fails
    print('controls: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


# ---------------------------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------------------------
EXPECTED_FORBIDDEN = ['Theorem 24 is false', 'Theorem 24 is repaired', 'completeness holds',
                      'completeness fails', 'the generators are complete',
                      'the generators are incomplete', 'Lemma 24.1 is repaired',
                      "the manuscripts' route is restored", 'the selection principle is']


def first_line(git, oid, pat, after=1):
    ls = git.lines(oid)
    for i in range(after - 1, len(ls)):
        if re.search(pat, ls[i]) and ls[i].strip():
            return i + 1
    raise SystemExit('self-test: %r not found in %s' % (pat, oid))


def qb(git, oid, a, b=None, k='quote'):
    b = b or a
    return '%s%s %s %d-%d\n%s\n%s\n' % (FENCE, k, oid, a, b,
                                        '\n'.join(git.lines(oid)[a - 1:b]), FENCE)


def valid_note(git, tok='WD3-no'):
    sub = PINS[0][1]
    l24 = first_line(git, sub, r'Theorem 24')
    lobs = first_line(git, sub, r'observables-preserving')
    lst = first_line(git, PINS[7][1], r'ST3')
    pat = r'interleav'
    cnt = sum(1 for ln in git.lines(sub) if re.search(pat, ln))
    dsub = git.at(D, 'papers/Substratum.md')
    dl = first_line(git, dsub, r'Theorem 24')
    sent = '\n'.join(git.lines(LEGACY)[SENTENCE_LINES[tok][0] - 1:SENTENCE_LINES[tok][1]])
    clause = '\n'.join(git.lines(LEGACY)[CLAUSE_LINES[0] - 1:CLAUSE_LINES[1]])
    fields = {'WD3-no': ('yes', 'no', 'no', 'fixed-partition', 'yes', 'established'),
              'WD3-yes': ('yes', 'yes', 'no', 'fixed-partition', 'yes', 'not-established'),
              'WD3-UNDECIDED': ('no', 'no', 'no', 'all-partitions', 'no', 'not-established')}[tok]
    tgt = 'Evidence: P\nStrength: medium\n\n'
    p = ['# SUB-241B-OBS (synthetic note)\n', '## Start state\n', INDEPENDENCE + '\n',
         '## WD0\n', 'Outcome: located\n' + tgt + qb(git, sub, l24),
         '## WD1\n', 'Outcome: four statements\n' + tgt,
         'Enumeration complete: %s\n' % fields[0]]
    for s in STATEMENTS:
        p.append('### %s\n' % s + qb(git, sub, lobs))
    p += ['## WD1-q\n', 'Outcome: quantifiers\n' + tgt]
    for s in STATEMENTS:
        p.append('### %s\nQuantifier: %s\n' % (s, fields[3]) + qb(git, sub, l24))
    p += ['## WD2\n', 'Outcome: read\n' + tgt,
          '(b) in O_set: %s\n(b) determined by (a), asserted: %s\n' % fields[1:3],
          '(b) not determined by (a), asserted: no\nQuestion posed: no\n',
          '%ssearch %d %s\n%s\n%s\n' % (FENCE, cnt, sub, pat, FENCE),
          '## WD2-q\n', 'Outcome: read\n' + tgt,
          'ST3/ST4 partitions: fixed-partition\nAll-partitions family settled: %s\n' % fields[4],
          qb(git, PINS[7][1], lst),
          '## WD3\n', 'Outcome: %s\n' % tok + tgt + 'Gate: %s\n' % fields[5],
          qb(git, sub, lobs),
          '## WD4\n', 'Outcome: census\n' + tgt + qb(git, sub, l24),
          '## Discrepancies\n', qb(git, LEGACY, 160) + qb(git, LEGACY, 390)
          + qb(git, LEGACY, 420, 421) + qb(git, LEGACY, 433),
          '## Post-round sentence\n', sent + '\n',
          '## ' + CONTEMPORARY + '\n', DISCLAIMER + '\n\n' + ANALYSIS_LABEL + '\n\n' + clause
          + '\n\n' + qb(git, ACT14, 1, None, 'analysis-quote')
          + '%scontext-quote %s papers/Substratum.md %d-%d\n%s\n%s\n'
          % (FENCE, D, dl, dl, git.lines(dsub)[dl - 1], FENCE),
          '## Checks\n', TYPE_P + '\n' + FENCE + 'text\ncontrols: OK\n' + FENCE + '\n']
    return ''.join(p)


def first_block(text, info_prefix):
    i = text.index(FENCE + info_prefix)
    j = text.index('\n' + FENCE + '\n', i)
    return i, j


def note_mutations(git):
    """(label, transform, failing checks)."""
    sub = PINS[0][1]
    dsub = git.at(D, 'papers/Substratum.md')
    dl = first_line(git, dsub, r'Theorem 24')

    def alter(t):
        i, j = first_block(t, 'quote ' + sub)
        k = t.index('\n', i) + 1
        return t[:k] + ('X' if t[k] != 'X' else 'Y') + t[k + 1:]

    def shift(t, da, db):
        m = re.search(FENCE + r'quote ' + sub + r' (\d+)-(\d+)', t)
        a, b = int(m.group(1)), int(m.group(2))
        return t[:m.start()] + '%squote %s %d-%d' % (FENCE, sub, a + da, b + db) + t[m.end():]

    def insert(t, sec, s):
        k = t.index('## %s\n' % sec) + len('## %s\n' % sec)
        return t[:k] + s + t[k:]

    def ctx(t):
        i = t.index(FENCE + 'context-quote')
        j = t.index('\n' + FENCE + '\n', i) + len(FENCE) + 2
        return insert(t[:i] + t[j:], 'WD2', t[i:j])

    def swap_subs(t):
        k = t.index('## WD1\n')
        a, b = '### %s\n' % STATEMENTS[0], '### %s\n' % STATEMENTS[1]
        head, rest = t[:k], t[k:]
        rest = rest.replace(a, '\0', 1).replace(b, a, 1).replace('\0', b, 1)
        return head + rest

    def quant(t, v):
        k = t.index('## WD1-q\n')
        return t[:k] + t[k:].replace('Quantifier: fixed-partition', 'Quantifier: ' + v, 1)

    def unquoted_wd4(t):
        k = t.index('## WD4\n')
        i = t.index(FENCE + 'quote', k)
        j = t.index('\n' + FENCE + '\n', i) + len(FENCE) + 2
        return t[:i] + t[j:]

    def drop_line(t, sec, line):
        k = t.index('## %s\n' % sec)
        return t[:k] + t[k:].replace(line + '\n', '', 1)

    sent_no = '\n'.join(git.lines(LEGACY)[288:298])
    sent_yes = '\n'.join(git.lines(LEGACY)[301:306])
    clause = '\n'.join(git.lines(LEGACY)[130:134])
    q421 = qb(git, LEGACY, 420, 421)
    return [
        ('quote body altered', alter, {'N3'}),
        ('quote coordinates shifted', lambda t: shift(t, 1, 1), {'N3'}),
        ('quote range widened', lambda t: shift(t, -1, 0), {'N3'}),
        ('quote of a blob outside the evidence base',
         lambda t: insert(t, 'WD2', qb(git, dsub, dl)), {'N4'}),
        ('act 14 quoted as evidence', lambda t: insert(t, 'WD2', qb(git, ACT14, 1)),
         {'N4', 'N11'}),
        ('search count off by one', lambda t: re.sub(
            FENCE + r'search (\d+)', lambda m: FENCE + 'search %d' % (int(m.group(1)) + 1), t),
         {'N5'}),
        ('search over act 14', lambda t: insert(
            t, 'WD2', '%ssearch 0 %s\nzzzqqq\n%s\n' % (FENCE, ACT14, FENCE)), {'N4', 'N11'}),
        ('strength line missing', lambda t: drop_line(t, 'WD2', 'Strength: medium'), {'N6'}),
        ('two outcome lines', lambda t: insert(t, 'WD0', 'Outcome: again\n'), {'N6'}),
        ('evidence other than type P', lambda t: insert(t, 'WD0', 'Evidence: L2\n'), {'N6'}),
        ('statements reordered', swap_subs, {'N7'}),
        ('quantifier outside the frozen three', lambda t: quant(t, 'some-partitions'),
         {'N7', 'N9'}),
        ('WD3-no over an unsettled all-partitions quantifier',
         lambda t: quant(t, 'all-partitions').replace(
             'All-partitions family settled: yes', 'All-partitions family settled: no'), {'N9'}),
        ('WD3-no with (b) in O_set',
         lambda t: t.replace('(b) in O_set: no', '(b) in O_set: yes'), {'N9'}),
        ('WD3-no with (a) asserted to determine (b)',
         lambda t: t.replace('(b) determined by (a), asserted: no',
                             '(b) determined by (a), asserted: yes'), {'N9'}),
        ('WD3-no with the enumeration incomplete',
         lambda t: t.replace('Enumeration complete: yes', 'Enumeration complete: no'), {'N9'}),
        ('WD3-no with the gate not established',
         lambda t: t.replace('Gate: established', 'Gate: not-established'), {'N9'}),
        ('WD3-yes without its requirement',
         lambda t: t.replace('Outcome: WD3-no', 'Outcome: WD3-yes').replace(sent_no, sent_yes),
         {'N9'}),
        ('post-round sentence twice', lambda t: insert(t, 'Post-round sentence', sent_no + '\n\n'),
         {'N10'}),
        ('sentence for another outcome', lambda t: t.replace('Outcome: WD3-no',
                                                             'Outcome: WD3-UNDECIDED'), {'N10'}),
        ('act 14 named without the clause', lambda t: t.replace(clause, 'Act 14, briefly.'),
         {'N11'}),
        ('forbidden sentence', lambda t: insert(t, 'WD3', 'Thus Theorem 24 is false.\n'), {'N13'}),
        ('a 24.1C premise', lambda t: insert(t, 'WD2', 'By the 24.1C result, so.\n'), {'N14'}),
        ('a 24.1C reference inside a block', lambda t: insert(
            t, 'WD2', '%stext\nper the 24.1C result\n%s\n' % (FENCE, FENCE)), {'N14'}),
        ('WD3 outcome outside the three tokens',
         lambda t: t.replace('Outcome: WD3-no', 'Outcome: WD3-maybe'), {'N8', 'N9', 'N10'}),
        ('independence sentence missing', lambda t: t.replace(INDEPENDENCE, ''), {'N14'}),
        ('post-round sentence outside its section',
         lambda t: insert(t.replace(sent_no + '\n', '', 1), 'WD3', sent_no + '\n\n'), {'N10'}),
        ('type-P sentence missing', lambda t: t.replace(TYPE_P, ''), {'N15'}),
        ('structural line in the contemporary section',
         lambda t: insert(t, CONTEMPORARY, 'Strength: high\n'), {'N16'}),
        ('listed structural line in the contemporary section',
         lambda t: insert(t, CONTEMPORARY, '- **Outcome:** read\n'), {'N16'}),
        ('discrepancy line 421 not quoted', lambda t: t.replace(q421, ''), {'N17'}),
        ('disclaimer missing', lambda t: t.replace(DISCLAIMER, ''), {'N16'}),
        ('a target carried by no quotation', unquoted_wd4, {'N6'}),
        ('an extra section', lambda t: t + '## Extra\n', {'N1'}),
        ('unclosed fence', lambda t: t + FENCE + 'text\nopen\n', {'N2'}),
        ('context-quote outside its section', ctx, {'N4'}),
        ('analysis label missing', lambda t: t.replace(ANALYSIS_LABEL, ''), {'N12'}),
    ]


def scratch(td):
    g = Git(td)
    subprocess.run(['git', 'init', '-q', td], capture_output=True, env=ENV, check=True)

    def tree(files):
        node = {}
        for path, data in files.items():
            parts = path.split('/')
            cur = node
            for x in parts[:-1]:
                cur = cur.setdefault(x, {})
            cur[parts[-1]] = data

        def write(nd):
            ents = b''
            for name in sorted(nd, key=lambda x: x.encode() + (b'/' if isinstance(nd[x], dict)
                                                               else b'')):
                v = nd[name]
                if isinstance(v, dict):
                    ents += b'040000 tree ' + write(v).encode() + b'\t' + name.encode() + b'\0'
                else:
                    oid = g.run(['hash-object', '-w', '--stdin'], data=v).decode().strip()
                    ents += b'100644 blob ' + oid.encode() + b'\t' + name.encode() + b'\0'
            return g.run(['mktree', '-z'], data=ents).decode().strip()
        return write(node)

    def commit(files, parents):
        args = ['commit-tree', tree(files), '-m', 'c']
        for p in parents:
            args += ['-p', p]
        return g.run(args, env=COMMIT_ENV).decode().strip()
    return g, commit


def tree_cases(real, own):
    """(label, ok, detail) for the scratch-repository cases."""
    out = []
    legacy = real.blob(LEGACY).encode('utf-8')
    with tempfile.TemporaryDirectory() as td:
        g, commit = scratch(td)
        pins = (('papers/P.md', blob_id(b'pinned\n')),)
        base = {'papers/P.md': b'pinned\n', LEGACY_PATH: legacy,
                'verification/ROADMAP.md': b'a\nb\n', 'verification/README.md': b'r\n'}
        b0 = commit(base, [])
        d = commit(dict(base, **{'papers/P.md': b'drifted\n'}), [b0])
        third = qb(real, LEGACY, *ADOPTED_SPANS[2])
        quotes = ''.join(qb(real, LEGACY, a, b) for a, b in ADOPTED_SPANS[:2]) + third
        head = '# p\n\nThe frozen blob of `controls.py` is `%s`.\n\n' % blob_id(own)
        pre = (head + quotes).encode()
        bad = pre.replace(b'four', b'three', 1)
        cut = third.split('\n')
        truncated = (head + quotes.replace(third, '\n'.join(cut[:-3] + cut[-2:]))).encode()
        missing = (head + quotes.replace(third, '')).encode()
        fc = dict(base, **{'papers/P.md': b'drifted\n', PREREG: pre})
        f = commit(fc, [d])
        ec = dict(fc, **{CONTROLS: own, NOTE: b'note\n', 'verification/ROADMAP.md': b'a\nb\nc\n'})
        e = commit(ec, [f])
        sent = '\n'.join(real.lines(LEGACY)[288:298]).encode()
        cases = [
            ('positive', e, set()),
            ('a manuscript changed', commit(dict(ec, **{'papers/P.md': b'x\n'}), [f]), {'T5'}),
            ('a ROADMAP line removed', commit(dict(ec, **{'verification/ROADMAP.md': b'a\nc\n'}),
                                              [f]), {'T6'}),
            ('preregistration changed after F', commit(dict(ec, **{PREREG: pre + b'x\n'}), [f]),
             {'T2'}),
            ('an amendment after F', commit(dict(ec, **{RDIR + 'amendments/a.md': b'a\n'}), [f]),
             {'T2', 'T5'}),
            ('a merge in F..E', commit(ec, [f, d]), {'T1'}),
            ('E not a descendant of F', commit(ec, [d]), {'T1'}),
            ('the legacy freeze changed', commit(dict(ec, **{LEGACY_PATH: b'x\n'}), [f]),
             {'T3', 'T5'}),
            ('controls.py not the frozen blob', commit(dict(ec, **{CONTROLS: own + b'#\n'}), [f]),
             {'T2'}),
            ('the result note absent', commit({k: v for k, v in ec.items() if k != NOTE}, [f]),
             {'T5'}),
            ('an extra file in the record directory',
             commit(dict(ec, **{RDIR + 'scratch.txt': b'x\n'}), [f]), {'T5'}),
            ('the post-round sentence in the ROADMAP',
             commit(dict(ec, **{'verification/ROADMAP.md': b'a\nb\n' + sent + b'\n'}), [f]),
             {'T6'}),
        ]
        for label, ec_, want in cases:
            got = {c for c, fl in tree_checks(g, ec_, f, own, d, b0, pins) if fl}
            out.append(('tree: ' + label, got == want, got))
        got = {c for c, fl in tree_checks(g, e, f, own, d, b0, (('papers/P.md', '0' * 40),))
               if fl}
        out.append(('tree: a pin that does not match', got == {'T4'}, got))
        f2 = commit(dict(fc, **{PREREG: bad}), [d])
        e2 = commit(dict(ec, **{PREREG: bad}), [f2])
        got = {c for c, fl in tree_checks(g, e2, f2, own, d, b0, pins) if fl}
        out.append(('tree: a quotation of the freeze not verbatim', bad != pre and got == {'T7'},
                    got))
        for label, alt in (('truncated', truncated), ('missing a frozen span', missing)):
            f3 = commit(dict(fc, **{PREREG: alt}), [d])
            e3 = commit(dict(ec, **{PREREG: alt}), [f3])
            got = {c for c, fl in tree_checks(g, e3, f3, own, d, b0, pins) if fl}
            out.append(('tree: the quotation of the freeze ' + label,
                        alt != pre and got == {'T7'}, got))
    return out


def self_test():
    git = Git('.')
    with open(os.path.abspath(__file__), 'rb') as fh:
        own = fh.read()
    fz = frozen(git)
    results = []
    results.append(('frozen: forbidden phrases', fz['forbidden'] == EXPECTED_FORBIDDEN,
                    fz['forbidden']))
    results.append(('frozen: three distinct sentences',
                    len(set(fz['sentences'].values())) == 3 and all(
                        s.startswith('The reconstruction') or s.startswith('Whether')
                        for s in fz['sentences'].values()), ''))
    results.append(('frozen: the act 14 clause', fz['clause'].startswith('Act 14 is cited only')
                    and fz['clause'].endswith('either direction.'), fz['clause'][:40]))
    for tok in WD3_TOKENS:
        got = {c for c, fl in note_checks(git, valid_note(git, tok), fz) if fl}
        results.append(('note: valid, %s' % tok, not got, got))
    base = valid_note(git)
    for label, fn, want in note_mutations(git):
        t = fn(base)
        got = {c for c, fl in note_checks(git, t, fz) if fl}
        results.append(('note: ' + label, t != base and got == want, got))
    results += tree_cases(git, own)
    ok = True
    for label, good, detail in results:
        if not good:
            print('SELF-TEST  FAIL  %s  %s' % (label, detail))
        ok = ok and good
    print('controls: self-test %s (%d cases)' % ('OK' if ok else 'FAILED', len(results)))
    return 0 if ok else 1


def main(argv):
    if argv == ['--self-test']:
        return self_test()
    git = Git('.')
    if len(argv) == 4 and argv[0] == 'check' and argv[2] == '--freeze' \
            and HEX40.fullmatch(argv[1]) and HEX40.fullmatch(argv[3]):
        e, f = argv[1], argv[3]
        with open(os.path.abspath(__file__), 'rb') as fh:
            own = fh.read()
        res = tree_checks(git, e, f, own)
        oid = git.at(e, NOTE)
        if oid is None or git.blob(oid) is None:
            res.append(('N', ['the result note is absent or unreadable at E']))
        else:
            res += note_checks(git, git.blob(oid), frozen(git))
        return report(res)
    if len(argv) == 2 and argv[0] == 'note' and HEX40.fullmatch(argv[1]):
        oid = git.at(argv[1], NOTE)
        if oid is None or git.blob(oid) is None:
            print('controls: the result note is absent at %s' % argv[1])
            return 1
        return report(note_checks(git, git.blob(oid), frozen(git)))
    print(__doc__.split('\n\n')[1])
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
```
