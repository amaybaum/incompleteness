# Substratum — A6 status adjudication: which label does the merged record support for the row `P1 — A6`? CONTROL PLANE

## The round's shape, declared first

**Type-P round.** Every substantive target is a determination about **what the merged record says** —
what the row's label was made conditional on, what the three landed A6 rounds established, and which
entry of the queue's own status vocabulary is true of the row in consequence. Nothing is proved about
matrices, no Lean is written, and no kernel object is produced. The round is settled by locating and
quoting, and its evidence rule is frozen below.

**NON-SEALING round, under `AGENTS.md` `§A.37`.** The rule keys the landing shape to what a round
**owns**, not to what it touches:

> **A non-sealing round — a round that owns no seal state — takes `L` alone.** It **may** modify
> other contracts inside an existing guard; it **may not** alter existing seal constants. It has
> nothing to pin, and a pin commit added there would pin nothing.

and, in the same section:

> **An archive seal belongs to the round that set it, and stays immutable afterwards.** A later
> round does not re-pin it, and does not acquire a pin commit merely by touching the guard file that
> carries it. An existing seal constant changes only in a round whose own preregistration says in
> advance that it changes it — and such a round is *sealing*, because it has taken ownership of that
> state prospectively rather than as a side effect of its diff.

**This round is the exact case that rule was written for, and the statement is made in terms.** The
round edits `verification/lean/edge_rigidity_probe.py`, the file that carries three archive seals. What
it changes there is a **guard contract** — the pinned row text `_A6P_ROW` and the sibling clauses that
pin the same row or the same label cell — and a guard contract is not seal state. Concretely:

- **This round owns, and may change, `_A6P_ROW`**, together with every other clause in that file
  whose assertion is about the **live** `ROADMAP` row or the **live** label cell. Those clauses are
  enumerated as target `AJ8` and their edit is bounded by target `AJ7`.
- **This round owns no seal state and may not touch any.** It **may not** alter
  `_A6P_SEALED_HEAD` (`58100aea15eea8f5808b351d64163f55c9fed1bf`), `_A6D_SEALED_HEAD`
  (`d0b8c6e83c32a01a586f947c0dfd9618a8b42a91`), `_A6I_SEALED_HEAD`
  (`93405f3ff7eb4818a2895b5f5e2861094d9fe757`), any `_*_MERGE` constant, or any `_*_BASE` constant.
  Each of those belongs to the round that set it and stays immutable.
- **Its landing is `E` → `L`, with no archive-pin commit.** It reserves no guard tag, adds no guard
  file, and creates no pin state, so there is nothing for a `P` commit to pin.

**If an outcome would require changing an existing seal constant, that outcome is OUT OF SCOPE for
this round.** It is not reserved as an option here and it is not taken "if needed": it would require
its own control plane, whose preregistration says prospectively that it changes that constant, and
which is therefore sealing. This freeze records that as a boundary. No target below can be satisfied
by editing a sealed head, and an execution that finds itself wanting to is recording a discrepancy,
not exercising a permission.

## The charter, quoted from the merged record

The instantiation round (round 2) closed by naming this decision and declining to take it:

> **The label.** The `ROADMAP` row `P1 — A6` carries `CONDITIONAL` at the start of this round and
> carries `CONDITIONAL` at the end of it. **Whether these outcomes warrant a stronger label is an
> owner decision, taken in a separate propagation round, and this round takes none and recommends
> none.**

and its freeze fixed, in advance, the shape of what such a decision would be deciding:

> The named hypothesis of the row, **as the propagation stated it**, is then discharged in its
> packaging half and discharged **for the covariance statement only** in its lift half.
>
> That outcome would license an owner to consider a stronger label, and the round records, in
> advance, the three things such a label would **not** be entitled to assert […]

This is that separate round. It adjudicates the label and nothing else.

## Start state

Pinned **by blob**, at the mandated execution base. Blob identity is authoritative: the commit
locates the tree, the blob is what is compared. A file that moved is the same file; a file that was
rewritten is not.

### Read-only files

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/substratum/a6-background-independence/preregistration.md` | `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3` |
| `verification/programmes/substratum/a6-background-independence/result.md` | `331b1928adde22d5c716a92adb864b523d0c09b8` |
| `verification/audits/foundations/a6-covariance-propagation-audit.md` | `e7cb7013747f783135c8e166d290ce6670df0ae9` |
| `verification/programmes/substratum/a6-instantiation/preregistration.md` | `6f991c1348e0c568261894c41b129b7f942abee6` |
| `verification/programmes/substratum/a6-instantiation/result.md` | `3d2b4b9ebc24a3a65172ad9384b8da7d8ca03634` |
| `verification/programmes/substratum/interface-audit.md` | `e4e0d02bfa67ea428391c0df77ad36f2689b87a3` |
| `verification/programmes/substratum/manuscript-axiom-audit.md` | `53eb9d646c51475553c3df47caec17077ab5471f` |
| `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean` | `5ec9fe52835642724d0685d9b920f613874279d6` |
| `verification/lean-mathlib/OIBridge/A6Instantiation.lean` | `dc8060f0f4ffe26d3adea7139462430120c4a30c` |
| `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean` | `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| `verification/lean-manuscript-census.json` | `06ad11f4b954f290a5ae523d83a6fb0b142d13e1` |
| `papers/Substratum.md` | `9ac6b732e8786897cade416b67c3f7f1df81ab84` |
| `papers/SM.md` | `26d6cbfb230c105eb00a979c2b69c363568455dd` |
| `book/ch05-gauge-structure.md` | `0f55ef3a7b5fca4172073f330f373f4b16542402` |
| `book/glossary.md` | `e811a2cc00b39d03b1a7adf263e31e63d4bcf957` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

### Files this round reads AND writes

These are **not** covered by the read-only clause above, and are listed separately so that the clause
is exact rather than approximately true.

| path | blob at this freeze's `main` | what this round writes there |
| --- | --- | --- |
| `verification/lean/edge_rigidity_probe.py` | `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e` | guard contracts about the live row and the live label cell, per `AJ7` and `AJ8`; **no seal constant, no merge constant, no base constant** |
| `verification/ROADMAP.md` | `4f9af3d3e8a2d5d66ff063c94a388d2c7c04f218` | the row `P1 — A6` and its section `P1 — A6, and what is and is not already represented`, per `AJ7` and `AJ9`; under `AJ6-derived` alone, also the queue table's loss of that row and the settled record `AJ7` freezes; no other row, section or research status |
| `verification/README.md` | `585dd145186dae654f58e2dc16712550b68ec9e0` | one appended paragraph for this round, per `AJ9`; no existing paragraph is edited |
| `verification/programmes/substratum/a6-status-adjudication/result.md` | absent | this round's result note |

A blob difference in a written file at the base is recorded in the same way as one in a read-only
file, and the execution proceeds from what it finds rather than from what the table says.

### The row text, pinned character-for-character

`verification/ROADMAP.md:65` at this freeze's `main` reads, exactly:

```
| **P1** | A6 — background independence / local gauge covariance | Substratum | **CONDITIONAL** — the adopted meaning is covariance, `A6Cov`, which holds identically on every link-coupled rule of the least interface (`a6cov_all`), so its content is the covariant interface and not a constraint; the named hypothesis is that the manuscripts' substratum instantiates that interface: the `K = 6` link-coupled rule is not packaged as a `Substratum` (the interface's `waveSubstratum` has a singleton internal index) and the complex lift on which `[SM §3.1]` conducts the gauge derivation is outside the interface; `A6-inv` is a separate, stronger fixed-background condition, refuted on the frozen two-site carrier and at the symmetric point `M = μ I_6` (`d3b_not_a6inv`, `d4b_mu_id`); `A6-glob` its global specialization (`a6glob_of_a6inv`); `A6-sd` a different principle under a shared name | the complete A1–A6 formal package |
```

### `_A6P_ROW`, pinned character-for-character

`verification/lean/edge_rigidity_probe.py` carries the constant `_A6P_ROW` as a parenthesised string
literal spanning lines `15468–15478` at blob `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e`. **Its value
is character-identical to the row line quoted immediately above**, and that identity is itself part of
the start state: the execution verifies it before touching either file, and records a discrepancy if
the two have come apart. The clause that consumes it is `_a6p_roadmap`'s first conjunct,
`_A6P_ROW in _r`, at line `15610`, where `_r` is the whitespace-flattened live `ROADMAP`.

## The anti-contamination invariant, FROZEN VERBATIM

> A start-state discrepancy does not license the execution to consume the newer sibling result merely
> because it happens to be present at its mandated base. The round consumes only what its freeze says
> it consumes.

**Why it matters here.** Four sibling control planes are opening concurrently and several will merge
into `main` before this round's execution begins, so the execution's base will in general carry
results this freeze does not name — and a round whose whole business is adjudicating a status label is
exactly the round most tempted to reach for a result that arrived after the freeze.

## The objects, FROZEN

**`ROW` — the row `P1 — A6` of `verification/ROADMAP.md`**, as quoted above, with its five cells: the
priority, the name, the programme, the label-and-reasons cell, and the closing obligation column
(`the complete A1–A6 formal package`).

**`VOCAB` — the queue's status vocabulary**, `verification/ROADMAP.md:22–31`, read **literally**. Its
seven entries are the whole menu; this round adds no label and redefines none.

**`COND` — what the label is conditional on.** The named hypothesis the row carries, **as the
covariance propagation stated it**, in the two halves that propagation keeps apart. Its content is to
be *located*, not reconstructed, and the two halves are reported separately and never merged.

**`DISCHARGE` — what the three landed A6 rounds established about `COND`**, consumed **as merged and
unrevised** from round 1's result, the propagation's control plane, and round 2's result. This round
re-derives nothing, extends nothing, and weakens nothing.

**`RESIDUAL` — what survives every outcome**: the statements the merged record says no round here
discharges. Located by quotation, not assembled by argument.

**`SURFACE` — the guard-contract surface**: every constant, clause and mutation control in
`verification/lean/edge_rigidity_probe.py` whose assertion is about the live `ROW`, the live label
cell, or the live `P1 — A6` section.

The round adds **no** object of its own. Where a distinction is needed that the merged record does not
draw, the execution **records that the record does not draw it** and does not draw it on the record's
behalf.

## The evidence rule, FROZEN

Every substantive determination is **type P** and must be carried by one or more of:

1. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
2. a **verbatim quotation** from a merged result note, preregistration or audit, with its coordinate;
   or
3. an explicit, recorded statement that **the passage sought does not exist** on the record searched,
   with the search named and bounded.

**Reconstructive inference is not evidence.** A determination of the form "the label must be X,
because otherwise Y" is **forbidden as a finding** and may appear only in a clearly labelled analysis
paragraph that states it is not evidence and that no target rests on it. **Where the record is silent,
the finding is that it is silent** — and in particular, silence is not denial: that no row in the
queue carries a given label is a fact about the queue, not an argument that the label is unavailable.

**Strength is recorded per determination**, as `full`, `high`, `medium` or `UNDECIDED`. A
determination carried by a passage that names a thing without displaying it is at most `medium`.

**One exception, bounded.** `AJ6`, the adjudication, is a **judgement against a quoted rule** — it
applies `VOCAB`'s literal text to `COND`, `DISCHARGE` and `RESIDUAL` as those are established by
quotation. Its inputs are all type P; the application itself is stated as the application it is, with
the quoted vocabulary entry and the quoted finding it is matched against set side by side, and it is
never reported as though it were itself a located passage.

## The targets, FROZEN

### `AJ0` — locating controls, cheap and certain

Locate and quote, with coordinates: `ROW`; `VOCAB`'s seven entries; the `ROADMAP` section
`P1 — A6, and what is and is not already represented`; the covariance propagation's section
`The ROADMAP label — the recommendation, with reasons`; round 2's sections `AS2 — the status
determination`, `What these outcomes do NOT license` and `The ROADMAP propagation, and the re-pin that
was NOT performed`; and round 2's freeze section `What each outcome licenses for the row's label, and
what it does not`. Record `_A6P_ROW`'s literal and its value.

**Falsifier.** Any of these absent from the pinned blobs at the base.

### `AJ1` — what the label is conditional ON, quoted

Determine, by quotation, the **exact content** of `COND`: what the covariance propagation named as
the undischarged hypothesis, and in which halves. Report the propagation's statement and the
`ROADMAP` section's statement **separately**, each with its own quotation, and **do not merge them**.
If they differ, the difference is the finding and is reported as a discrepancy of the record, not
repaired.

Report also, by quotation, the propagation's **per-label reasoning** — why `GAP`, `DERIVED`, `OPEN`,
`EXTERNAL`, `INDEPENDENT` and `ACTIVE` were each set aside — and its recorded point of imperfect fit.

**The separation this target must keep, FROZEN.** What the label tracks and what stands **outside
`A6Cov`** are two lists, reported separately and never merged. The named hypothesis is the
**substratum identification** — that the manuscripts' physical substratum is the packaged carrier.
The part of the gauge derivation that consumes the inner product, unitarity as a constraint, the
condensate `Σ`, the stabilizer in `U(6)` or the cubic decomposition, and the complex carrier's
failure of `A1`, stand **outside `A6Cov`** and are **not components of the condition the label
carries**. Writing either list into the other is a defect of the execution: folding the outside
material into the hypothesis makes the assumption conditional on something it never was, and folding
the hypothesis outward empties the label.

### `AJ2` — the packaging half: what the record says about its discharge

Determine, by quotation from round 2's merged result and from the `ROADMAP` section, whether the
finite-alphabet half of `COND` is discharged, at what evidence level, and with which named results
carrying it. Report the **organizing caveat** verbatim wherever a positive is reported:

> Round 1 proved `a6cov_all : ∀ N M, A6Cov N M` — the adopted reading holds **identically** on every
> link-coupled rule of the interface, so its content is the covariant interface itself and not a
> constraint. A full positive therefore says exactly that the manuscripts' rule **is of that form**.
> It does **not** say that a nontrivial condition was tested and survived.

Report the `A4Exact` hypothesis — `∀ v i j, M (i + v) (j + v) = M i j` — **with** the conjunct it
qualifies, every time, and never as a footnote to it.

### `AJ3` — the lift half: what the record says about its discharge, and at what scope

Determine, by quotation, whether the complex-lift half of `COND` is discharged, and **at what scope**,
in exactly the split round 2 froze: the **covariance statement** and the **carrier**. Report the two
separately and never as one. Report `cx3b_complex_not_A1` and its bounded reading with the positive
it accompanies.

**Silence is a finding.** If the record does not say whether a discharge "for the covariance statement
only" discharges the half as the propagation stated it, the finding is that it does not say.

### `AJ4` — the residual, enumerated from the record, in two lists that are never merged

List, each with its own quotation and coordinate, every statement the merged record says survives
every outcome of the landed rounds, **sorted into two lists**:

- **`AJ4-in` — what the record presents as a hypothesis the row tracks.** The candidate, to be
  checked and not assumed, is the **substratum identification**: that the manuscripts' physical
  substratum is the packaged carrier. For it, record by quotation whether the record presents it as
  *this row's* named hypothesis or as a premise ambient to the programme's rows generally. That
  determination is the hinge of `AJ6`'s gate, and it is the only item this list is expected to
  weigh.
- **`AJ4-out` — what the record places outside `A6Cov`.** The part of `[SM §3.1]`'s derivation that
  consumes the inner product, unitarity as a constraint, the condensate `Σ`, the stabilizer in
  `U(6)` or the cubic decomposition; and the complex carrier's failure of `A1`. **These stand
  outside the interface and are no part of the condition the label carries**, and **no outcome of
  this round moves an item from `AJ4-out` into `AJ4-in`.**

Report alongside both, and in neither, the items that qualify a named result rather than the label:
the `A4Exact` translation-invariance hypothesis, reported with the conjunct it qualifies; round 2's
six unsettled points; round 1's three unsettled points; and the manuscript-axiom audit's bare-carrier
finding, which is about a different carrier.

**This is a census, not an adjudication.** No item is judged fatal or harmless here; the two lists
exist so that `AJ6`'s gate is matched against an enumerated hypothesis rather than a remembered one,
and so that material standing outside `A6Cov` cannot reach the gate at all.

### `AJ5` — the current row text, clause by clause, against the merged record

Split `ROW`'s label-and-reasons cell into its semicolon-delimited clauses and determine, for each,
whether the merged record carries it. Report per clause: **carried**, **not carried**, or
**UNDECIDED**, each with its quotation.

**The finding is the collation.** If every clause is carried, the row stands byte-identical and the
status rule's `AJ-stand-asis` branch fires. If any clause is not carried, the row text changes under
every label outcome, and that is what makes the guard-contract edit unavoidable — which is the point
the `§A.37` declaration above turns on.

### `AJ6` — the adjudication

Determine which entry of `VOCAB`, read literally, is true of `ROW` given `AJ1`–`AJ5`. Run **all seven
entries** and record for each whether it is a candidate, so that the determination is a menu applied
and not a pair compared. Exactly one of:

- **`AJ6-conditional`** — `CONDITIONAL`'s stated meaning, "Formally present, carrying a named
  hypothesis this programme has not discharged. The manuscript states the hypothesis; the row tracks
  it", is true of the row. Requires the named, undischarged hypothesis to be identified from
  **`AJ4-in`** and quoted, **and** a recorded statement of whether that hypothesis is one the
  manuscripts state, since the vocabulary's second sentence says it is. **No item of `AJ4-out`
  carries this outcome either**: what stands outside `A6Cov` is not a hypothesis the label tracks.
- **`AJ6-derived`** — `DERIVED`'s stated meaning, "Kernel-proved and propagated to the manuscript.
  Rows reach this state and then leave the queue", is true of the row. Requires `AJ2` and `AJ3` both
  discharged on the record, **and** the gating condition immediately below. **Both sentences of the
  entry bind**: the second is part of the label, so `AJ6-derived` carries the row's **departure from
  the queue**, specified in `AJ7` and not deferred to anyone.
- **`AJ6-UNDECIDED`** — the permitted fallback, with the obstruction named and quoted.

**The gating condition on `AJ6-derived`, FROZEN:**

> `AJ6-derived` may be written only if **the substratum identification is established not to be a
> hypothesis this row tracks** — `AJ4` records, by quotation, whether the record presents "the
> manuscripts' physical substratum is the packaged carrier" as this row's named hypothesis or as a
> premise ambient to the programme's rows generally — and only if `AJ3` establishes, **from the
> propagation's own words for the lift half**, that what those words name is what round 2 proved,
> and not merely that something adjacent to it was proved. If the substratum identification is this
> row's tracked hypothesis, or if the record is silent on whether the propagation's words are
> answered by the covariance statement alone, the outcome is `AJ6-conditional` or `AJ6-UNDECIDED`,
> never `AJ6-derived`.
>
> **What the gate does not test.** The part of the gauge derivation that consumes the inner product,
> unitarity as a constraint, the condensate `Σ`, the stabilizer in `U(6)` or the cubic decomposition
> **does not enter this gate**, and neither does the complex carrier's failure of `A1`. Those lie
> **outside `A6Cov`** and are no part of the condition the label carries; treating one as a gate
> input would block `AJ6-derived` on something the row does not track, which is a defect of the
> execution and is checked for in the final report.

**Both halves of the gate are genuinely open.** The propagation's words for the lift half name the
covariance of `SM.md:112–114` on an interface, and round 2 proves that identity at the complex
six-component carrier; whether those are the same statement is a question about two quoted passages
and is answerable either way. Whether the substratum identification is this row's own hypothesis or
a premise the whole programme carries is likewise a question about quoted passages. The gate exists
to make both answers be read off the passages rather than assumed.

**Why this gate exists.** `AJ2` and `AJ3` landing positive would establish that the hypothesis *as
the propagation named it* is discharged. That is not the same as there being no hypothesis left for
the row to track, and the two are easy to run together. The gate makes the decision rule match the
vocabulary's own wording rather than the easier question underneath it — and it tests exactly one
thing, the substratum identification, so that the decision turns on the condition the label carries
and on nothing standing beside it.

**`AJ6-derived` is not a finding that the A6 result is stronger than the landed rounds made it, and
`AJ6-conditional` is not a finding that they achieved less.** Both are findings about which label
describes the row. See the non-licence section.

### `AJ7` — the replacement row text and, under `AJ6-derived`, the departure

The execution writes the text frozen below for the outcome `AJ6` returns, **character for
character**, into `_A6P_ROW` and into every clause `AJ8` enumerates that pins the same string, and
places it in `verification/ROADMAP.md` at the position this target fixes. It composes no row text of
its own.

**Decision rule, frozen:**

- `AJ6-derived` → **`ROW-derived`** below, **and the departure specified immediately after it**.
- `AJ6-conditional` or `AJ6-UNDECIDED`, **and** `AJ5` found at least one clause not carried →
  **`ROW-conditional`** below, written at `verification/ROADMAP.md:65`, the row staying in the queue.
- `AJ6-conditional` or `AJ6-UNDECIDED`, **and** `AJ5` found every clause carried → the row stays
  **byte-identical** at `verification/ROADMAP.md:65` and `_A6P_ROW` is untouched.

**Only `AJ6-derived` moves the row.** Under `AJ-stand-asis`, `AJ-stand-restate` and `AJ6-UNDECIDED`
the queue keeps the row where it is, in the order it is in, and the queue table is otherwise
byte-identical under all four outcomes.

**`ROW-conditional`, FROZEN:**

```
| **P1** | A6 — background independence / local gauge covariance | Substratum | **CONDITIONAL** — the adopted meaning is covariance, `A6Cov`, which holds identically on every link-coupled rule of the least interface (`a6cov_all`), so its content is the covariant interface and not a constraint; the `K = 6` link-coupled rule is packaged as a `Substratum` with no field added, the packaged carrier's update map is the interface's link-coupled map, `A1`–`A5` hold of it with `A4Exact` under the translation-invariance hypothesis on the link coupling, and the covariance statement of `[SM §3.1]` is proved at the complex six-component carrier with the manuscripts' site-dependent transformation an instance of the interface's transformation class (`pk1_packaging`, `pk2a_bridge`, `pk3a_A1`–`pk3e_A5`, `cx1_complex_covariance`, `cx2_unitary_gaugeLink`); the named hypothesis is that the manuscripts' physical substratum is that packaged carrier, and that identification is the whole of what this row tracks; separately, and outside `A6Cov` rather than a condition on it, the part of the gauge derivation that consumes the inner product, unitarity as a constraint, the condensate `Σ`, the stabilizer in `U(6)` or the cubic decomposition stands outside the interface, as does the complex carrier itself, proved not to satisfy `A1` (`cx3b_complex_not_A1`); `A6-inv` is a separate, stronger fixed-background condition, refuted on the frozen two-site carrier and at the symmetric point `M = μ I_6` (`d3b_not_a6inv`, `d4b_mu_id`); `A6-glob` its global specialization (`a6glob_of_a6inv`); `A6-sd` a different principle under a shared name | the complete A1–A6 formal package |
```

**`ROW-derived`, FROZEN:**

```
| **P1** | A6 — background independence / local gauge covariance | Substratum | **DERIVED** — the adopted meaning is covariance, `A6Cov`, which holds identically on every link-coupled rule of the least interface (`a6cov_all`), so its content is the covariant interface and not a constraint; the `K = 6` link-coupled rule is packaged as a `Substratum` with no field added, the packaged carrier's update map is the interface's link-coupled map, `A1`–`A5` hold of it with `A4Exact` under the translation-invariance hypothesis on the link coupling, the adopted meaning holds of its own link data, and the covariance statement of `[SM §3.1]` is proved at the complex six-component carrier with the manuscripts' site-dependent transformation an instance of the interface's transformation class (`pk1_packaging`, `pk2a_bridge`, `pk3a_A1`–`pk3e_A5`, `pk2b_covariance`, `cx1_complex_covariance`, `cx2_unitary_gaugeLink`); the row asserts that the manuscripts' carrier is an instance of the covariant interface, and asserts neither that a condition was tested and survived, nor that the physical substratum is that carrier, nor that the gauge group is derived; separately, and outside `A6Cov` rather than a condition on it, the part of the gauge derivation that consumes the inner product, unitarity as a constraint, the condensate `Σ`, the stabilizer in `U(6)` or the cubic decomposition stands outside the interface, as does the complex carrier itself, proved not to satisfy `A1` (`cx3b_complex_not_A1`); `A6-inv` is a separate, stronger fixed-background condition, refuted on the frozen two-site carrier and at the symmetric point `M = μ I_6` (`d3b_not_a6inv`, `d4b_mu_id`); `A6-glob` its global specialization (`a6glob_of_a6inv`); `A6-sd` a different principle under a shared name | the complete A1–A6 formal package |
```

**Both are in manuscript voice.** Each states what is; neither narrates a change, cites a round
number, or refers to any state of the row other than the one it writes. That is a requirement of the
target, and a row text that narrates is a defect of the execution.

#### The departure, FROZEN — written only under `AJ6-derived`

`DERIVED`'s vocabulary entry has two sentences and both bind: "Kernel-proved and propagated to the
manuscript. **Rows reach this state and then leave the queue.**" A row written `DERIVED` and left in
the queue is an inconsistent record, so the departure is part of this outcome and is specified here
rather than left to a later call.

**1. What the obligation table becomes.** In `## The queue`, the row `P1 — A6` is removed from the
table. Every remaining row is byte-identical and keeps its order, so the table carries the nine rows
that remain: `P0`; `P1` Substratum Lemma 24.1; `P1` physical C4 discharge; `P1` H-Bell; `P2`
Bekir–Golomb; `P2` H-link; `P2` H-state / H-frame / H-slope; `P2` covariant matter→boundary coupling;
`P3` GR states → Level-III. **No other row's cells change, and no row is reordered.**

**2. Where the departed row goes.** `ROW-derived` is written **verbatim** into a settled-obligation
record carrying the queue's own five columns, placed immediately **before** the section
`## Settled negatively — `INDEPENDENT`, and not queue items`, whose heading, standing note, table and
links are untouched. The record's heading, standing note and table header are frozen exactly as:

```
## Settled — `DERIVED`, and not queue items

**These are obligations closed in the kernel and carried by the manuscripts. They do not belong on
the list above and are recorded here so they are not re-added to it.**

| Priority | Obligation | Track | Status | Unlocks |
| --- | --- | --- | --- | --- |
```

with `ROW-derived` as the single row beneath it. The form follows the `INDEPENDENT` record, which is
the file's own way of holding what has left the queue; the five columns are kept so that the row is
the row, character for character, and not a paraphrase of it.

**3. The row's section stays where it is.** `### P1 — A6, and what is and is not already
represented` keeps its position between `### P1 — Substratum Lemma 24.1, the semigroup-transfer step`
and `### P1 — physical C4 discharge`, so that `_a6p_section` and `_a6i_section` bound the same text,
and it carries one sentence, in manuscript voice, saying where the obligation's row stands.

**4. `_A6P_ROW` is set to `ROW-derived`.** The clause consuming it, `_a6p_roadmap`'s `_A6P_ROW in
_r`, asks membership of the whole flattened `ROADMAP` rather than of the queue table, and is
satisfied by the row in its settled position; the same holds of `_a6d_roadmap_row`'s inline row
string. The execution states that this is why the two clauses need the string updated and not
re-scoped, rather than leaving the reader to check it.

**5. `_a6i_label_unmoved` is re-pointed, not relaxed.** Its label-cell clause and its
`| Substratum | **DERIVED** —` absence clause are both assertions about the live file. Each is
replaced by an assertion of the **same kind** about the settled record — a positive clause naming the
settled row and a negative clause forbidding a queue row for it — and neither is deleted or weakened
to a tautology.

**6. The landing page.** `verification/README.md` gains this round's one appended paragraph, which
records the departure and where the row is recorded.

**The departure is confined to these six items.** No other row leaves, no other section is created,
moved or removed, and the `INDEPENDENT` record is not touched.

### `AJ8` — the guard-contract surface, enumerated and bounded

List every constant, clause and mutation control in `verification/lean/edge_rigidity_probe.py` at the
pinned blob whose assertion is about the live `ROW`, the live label cell, or the live `P1 — A6`
section, with its line coordinate and its exact assertion, and state for each whether `AJ7`'s decision
rule requires it to change. **Under `AJ6-derived` the census covers the departure as well**: every
clause whose assertion would be falsified by the row leaving the queue table, or by the settled
record existing, is listed and its re-pointing stated, and a clause that the departure reaches and
the table below omits is reported under the bounding clause. The known candidates, **to be checked
and not assumed**:

| coordinate | constant / clause | what it asserts about the live file |
| --- | --- | --- |
| `:15468–15478` | `_A6P_ROW` | the row string, character-for-character |
| `:15604–15619` | `_a6p_roadmap` | `_A6P_ROW in _r`; the section's bolded "Why the row is CONDITIONAL, and neither DERIVED nor GAP." heading, with its label names in backticks; `_A6P_ROAD_HYP`; four further section sentences; the propagation link |
| `:15758–15759` | `_a6p_m6` | a mutation control that rewrites the live label cell from `CONDITIONAL` to `DERIVED` and requires `_a6p_roadmap` to reject the result |
| `:17067–17089` | `_a6d_roadmap_row` | the same row string, written out inline, plus two link clauses and a clause about round 1's result note |
| `:17295–17298` | `_a6d_m25` | the same mutation control against `_a6d_roadmap_row` |
| `:17858–17875` | `_a6i_label_unmoved` | the live row's label-cell prefix, and that `\| Substratum \| **DERIVED** —` is absent from the live `ROADMAP` |
| `:18165–18166` | `_a6i_m10` | the same mutation control against `_a6i_label_unmoved` |
| `:17878–17896` | `_a6i_roadmap_section` | ten sentences of the live `P1 — A6` section |

**Three clauses are named as expected NOT to change, and the execution states so or records
otherwise.** `_a6p_readme` (`:15622–…`) and `_a6i_readme` (`:17899–…`) assert sentences inside the
**round records** of the propagation and of round 2 in `verification/README.md`. Those sentences are
statements about what those rounds did, they stay true whatever this round decides, and this round
does not edit them — the same principle `§A.37` states for a result note: "A result note recording
that the pins were unset at execution stays true, being a statement about the execution." The third
is the clause of `_a6d_roadmap_row` asserting round 1's result note still records that round 1 left
the `GAP` label in place.

**Departure note on the census, FROZEN.** Each of the three mutation controls asserts its guarded
clause **rejects** a label overclaim. Under `AJ6-derived` their rewrites target a queue cell the live
file does not carry, so each is re-pointed at an overclaim of the **settled** state — for instance a
settled row whose reasons assert that the assumption was verified, or a queue row re-added for the
departed obligation — and each stays a mutation control that its guarded clause rejects. **None is deleted, and none is weakened to a rewrite the clause would reject trivially.**

**Bounding clause, FROZEN.** `AJ8`'s list is the **whole** edit surface in that file. A constant or
clause outside it is not edited. If the execution finds a clause it must edit that `AJ8` does not
name, it **records the discrepancy, names the clause, and reports the freeze as having under-counted
the surface**, and it does not enlarge the surface silently.

### `AJ9` — the section and the landing page

The `ROADMAP` section `P1 — A6, and what is and is not already represented` carries the label's
reasons in prose and is pinned by `_a6p_roadmap` and `_a6i_roadmap_section`. Determine which of its
sentences the adjudication requires to change, write them in manuscript voice, and append one
paragraph to `verification/README.md` recording this round.

**Under `AJ6-derived`** the section keeps its position and gains the one sentence `AJ7`'s departure
item 3 requires, the settled record of item 2 is created with the frozen heading, standing note and
table header, and the appended `README` paragraph records the departure and where the row is
recorded. The section's prose separates, as the row does, the named hypothesis from what stands
outside `A6Cov`.

**Bounded in terms.** The `ROADMAP` edit is confined to the row `P1 — A6`, its section, and — under
`AJ6-derived` alone — the queue table's loss of that row and the settled record `AJ7` freezes. No
other row, section or research status is touched, and no other row moves, changes cell or changes
order under any outcome. The `README` edit is **one appended paragraph**; no existing paragraph is
edited. **No manuscript is edited**: `papers/` and `book/` are read and never written, and the census
gains no anchor, because no manuscript propagation occurs in this round.

## The preregistered predictions, and their strengths

Recorded before execution, with reasons, so that the outcome can be compared against them.

| target | prediction | strength expected | reason |
| --- | --- | --- | --- |
| `AJ0` | positive | full | every passage was located while drafting this freeze |
| `AJ1` | positive, and **the two statements of the hypothesis are expected to agree** | high | the `ROADMAP` section's named-hypothesis sentence is pinned by `_A6P_ROAD_HYP` and the propagation's own text is its source; whether they agree in the halves as well as the headline is what the target checks |
| `AJ2` | positive — **discharged**, at evidence level 2 | high | round 2's result reports it in terms, and the `ROADMAP` section carries the same finding; this is a quotation, not a judgement |
| `AJ3` | positive, **with the covariance statement discharged and the carrier proved outside** | high | round 2 reports the split in terms; the **scope question** — whether the propagation's own words for this half are answered by the covariance statement alone — is a separate determination against two quoted passages, predicted positive at **medium**, since the propagation's wording names the covariance and round 2's framing names the carrier as well |
| `AJ4` | positive; **`AJ4-in` is expected to hold the substratum identification and nothing else, and `AJ4-out` the §3.1 material and the complex carrier's failure of `A1`** | high on the sorting, **medium** on whether the record presents the substratum identification as this row's own hypothesis | round 2 calls that premise "a premise no round can discharge" and "the residual that survives every outcome", and separately names the §3.1 material as staying outside the interface; whether the first is *this row's* hypothesis or the programme's ambient premise is the one judgement the census must return and the gate's hinge |
| `AJ5` | **at least two clauses not carried** | medium | the row asserts in the present tense that the `K = 6` rule is not packaged as a `Substratum` and that the complex lift is outside the interface, and round 2's `pk1_packaging` and `cx1_complex_covariance` bear directly on both; whether that makes the clauses "not carried" or merely narrower is exactly what the target must settle |
| `AJ6` | **`AJ6-conditional`** | **medium** | the hypothesis *as the propagation named it* looks discharged, but `AJ4-in` is expected to hold the substratum identification, which the record is expected to present as a premise this row still tracks. **The principal falsifier, and the principal escape hatch, is `AJ4-in`**: if the record presents the substratum identification as ambient to the programme's rows rather than as this row's tracked hypothesis, the gate opens and the prediction is wrong. A quoted passage answering the propagation's own words for the lift half with the covariance statement alone would also move it. **Nothing in `AJ4-out` bears on this prediction in either direction.** |
| `AJ7` | positive | high on the row text, **medium** on the departure | the row text is frozen above and is copied, not composed, which is mechanical; the departure is six specified items against a file sibling rounds also move, and the risk is a remaining row disturbed or a clause the departure reaches unlisted |
| `AJ8` | positive, **and the eight-row candidate list is expected to be complete** | medium | the candidates were found by searching the pinned blob for the label token and the row string, and a clause that pins the row by a paraphrase rather than by the string would escape that search |
| `AJ9` | positive | medium | the section's sentences are prose and the rewrite is a judgement about which of them the adjudication reaches |

**The adjudication is deliberately held at medium.** `AJ6` is what the round exists to decide, and a
freeze that predicted it at high would be claiming the answer it is chartered to find. `AJ5` and
`AJ8` are held at medium for their own reasons, recorded above. If any target lands above its
predicted strength, the result note records the promotion and its reason.

**No prediction licenses its own conclusion.** A target that lands against prediction is reported
against prediction, and the prediction is not amended.

## The STATUS RULE, FROZEN

1. **The round decides the label and writes it.** Unlike round 2, this round's charter is the
   decision itself; declining to take it is `AJ6-UNDECIDED`, with the obstruction named and quoted,
   and not a silent pass.
2. **The label written is one of `VOCAB`'s seven entries, read literally.** No new label is coined,
   no entry is redefined, and no qualifier is attached to a label cell beyond the reasons the frozen
   row text carries.
3. **The row text written is the frozen text for the outcome, character for character**, or the
   byte-identical row where `AJ7`'s decision rule says so. The execution composes no row text.
4. **`AJ6-derived` carries the departure, and only `AJ6-derived` does.** The row leaves the queue
   table and is recorded verbatim in the settled record `AJ7` freezes, with the frozen heading,
   standing note and table header. Under `AJ-stand-asis`, `AJ-stand-restate` and `AJ6-UNDECIDED` the
   queue and the row's place in it are left as they are. Under every outcome the other rows are
   byte-identical and keep their order.
5. **What the label tracks and what stands outside `A6Cov` are written as two things.** The named
   hypothesis is the substratum identification. The part of the gauge derivation consuming the inner
   product, unitarity as a constraint, the condensate `Σ`, the stabilizer in `U(6)` or the cubic
   decomposition, and the complex carrier's failure of `A1`, are recorded as standing outside the
   interface and **never as conditions on the assumption**. A row, section or note that folds the
   second into the first is a defect of the execution.
6. **No seal constant, merge constant or base constant is touched.** `_A6P_SEALED_HEAD`,
   `_A6D_SEALED_HEAD`, `_A6I_SEALED_HEAD`, `_A6P_MERGE`, `_A6D_MERGE`, `_A6I_MERGE`, `_A6P_BASE`,
   `_A6D_BASE` and `_A6I_BASE` are read and never written. An outcome requiring otherwise is out of
   scope and is recorded as such.
7. **No merged result note, preregistration or audit is edited**, and no `README` round record is
   edited. Those are statements about their own rounds and stay true.
8. **No manuscript is edited.** `papers/` and `book/` are read and never written.
9. **The round may not identify any two of the four readings.** `A6-inv`, `A6-cov`, `A6-glob` and
   `A6-sd` are four objects on three interfaces. Any sentence using the bare name outside a
   quotation, the row name, or a guard, family, directory or round name is a defect.
10. **The round may not report the gauge-group derivation settled**, in either direction.
11. **The round records UNDECIDED, with the obstruction named and quoted, wherever it cannot settle a
    target**, and reports every negative as a located absence on a named and bounded search rather
    than as a failed search.
12. **The organizing caveat is carried verbatim wherever a positive of `AJ2` or `AJ3` is reported.**

## The post-round sentence, frozen now, one per outcome

Exactly one is written, verbatim, in the result note and nowhere else.

**If `AJ6-conditional` with `AJ5` finding at least one clause not carried — `AJ-stand-restate`:**

> The row `P1 — A6` carries `CONDITIONAL`, and the label is the one the queue's vocabulary supports:
> the predicate is formally present and proved, the hypothesis the covariance propagation named is
> discharged in its packaging half at evidence level 2 and discharged for the covariance statement in
> its lift half, and the hypothesis the row tracks is the one named in the frozen row text — that the
> manuscripts' physical substratum is the packaged carrier, and that identification is the whole of
> it. Separately, and outside `A6Cov` rather than as a condition on it, the part of the gauge
> derivation that consumes the inner product, unitarity as a constraint, the condensate, the
> stabilizer in `U(6)` or the cubic decomposition stands outside the interface, as does the complex
> carrier. The row stays in the queue and its reasons are written to
> the frozen text. Nothing here strengthens or weakens what the three landed A6 rounds established,
> nothing here says the sixth assumption holds of the physical substratum or fails of it, and nothing
> here is a derivation of the gauge group.

**If `AJ6-conditional` with `AJ5` finding every clause carried — `AJ-stand-asis`:**

> The row `P1 — A6` carries `CONDITIONAL` and its text stands byte-identical: every clause of the
> row's reasons is carried by the merged record, and the hypothesis the row names is one the record
> presents as undischarged. The row stays in the queue, `_A6P_ROW` is untouched, and so is every
> clause of `AJ8`'s surface. Nothing here strengthens or weakens what the three landed A6 rounds
> established.

**If `AJ6-derived` — `AJ-move`:**

> The row `P1 — A6` carries `DERIVED`: the hypothesis the covariance propagation named is discharged
> on the merged record in both of its halves, at evidence level 2, the substratum identification is
> not a hypothesis this row tracks, and the adopted meaning is carried by the manuscripts. The row's
> reasons are written to the frozen text, and that text states what the label does and does not
> assert: that the manuscripts' carrier is an instance of the covariant interface, and neither that a
> condition was tested and survived, nor that the physical substratum is that carrier, nor that the
> gauge group is derived. The obligation leaves the queue, as the vocabulary's entry for this label
> states, and the row is recorded verbatim in the settled record, the queue's other rows byte-identical
> and in their order. The part of the gauge derivation that consumes the inner product, unitarity as a
> constraint, the condensate, the stabilizer in `U(6)` or the cubic decomposition stands outside
> `A6Cov`, as does the complex carrier, and neither is a condition on the assumption. Nothing here
> strengthens what the three landed A6 rounds established.

**If `AJ6-UNDECIDED`:**

> Which label the queue's vocabulary supports for the row `P1 — A6` is UNDECIDED, with the obstruction
> named and quoted in the result note. The row keeps `CONDITIONAL` and stays in the queue, its
> reasons written to the frozen `ROW-conditional` text where `AJ5` found a clause not carried and
> byte-identical otherwise. The three landed A6 rounds stand at their own strengths, none is revised,
> and no manuscript claim changes.

## What none of these outcomes licenses

- **Discharging a condition on a label is not a finding about the A6 result's strength.** Whatever
  `AJ6` returns, the kernel content of the row is exactly what round 1 and round 2 proved, at exactly
  the strengths their result notes record. A label is a description of the row's standing in the
  queue; moving one adds no theorem and removes none, and no sentence may treat the adjudication as
  though it had.
- **Nothing here says a condition was tested and survived.** `A6Cov` holds identically on every
  link-coupled rule (`a6cov_all`). A row at any label asserts that the manuscripts' rule is of the
  covariant form and asserts nothing more, and the organizing caveat is carried wherever a positive
  appears.
- **Nothing here says the sixth assumption holds of the physical substratum, or fails of it.** That
  the physical substratum is the packaged carrier is a premise the merged record says no round
  discharges, and this round discharges nothing.
- **Nothing here is a derivation of the gauge group.** Theorems 5 and 7 of `SM`, H-link, H-cust, the
  `(3,2,1)` decomposition, the condensate stabilizer, the reduction to
  `SU(3) × SU(2) × U(1)` and the Wilson action are neither consumed nor judged, in either direction.
  No sentence about the Standard Model is licensed.
- **Nothing here identifies any two of the four readings**, and nothing adopts, revises or ranks a
  reading. The adopted meaning is the propagation's and is consumed, not re-adjudicated.
- **Nothing here reopens round 1's or round 2's targets.** `D1`–`D4`, `PK0`–`PK5`, `CX0`–`CX3`, `AS1`
  and `AS2` are consumed as merged and none is revised, promoted, demoted or re-derived.
- **`AJ6-derived` would not close the obligation column.** The row's closing column names the
  complete A1–A6 formal package; whether that obligation is met is not a target here, and no outcome
  asserts it. **Departing the queue is what the label's own entry says a row at that label does; it
  is not a claim that the closing column is satisfied**, and the settled record carries the column
  unchanged rather than as a discharge.
- **Nothing here makes the §3.1 residual a condition on the assumption.** What stands outside
  `A6Cov` is recorded as standing outside it. No outcome moves an item of `AJ4-out` into the
  hypothesis the label tracks, and no outcome asserts that the material outside is thereby settled,
  in either direction.
- **`AJ6-conditional` is not a verdict that the landed rounds fell short.** It is a finding about
  which vocabulary entry describes a row that carries a named residual.
- **Nothing here weakens `A1`**, adds a field to `Substratum`, defines a predicate for `A6-sd`, or
  introduces a complex-lift interface.
- **Nothing here is about Track B, `P0`, physical C4, the fibre-Gram classification, Lemma 24.1,
  H-Bell or hydrodynamics**, in either direction.
- **The bare-carrier finding stands untouched.** The manuscript-axiom audit's verdict, about the bare
  operational theory, is about a different carrier and is neither consumed nor weakened.
- **No archive seal is re-pinned, and no archive pin is created.** See the chronology control.

## Numbered hazards

1. **A builder reading the diff rather than the freeze and concluding this round owes an archive
   pin.** The sharpest hazard of the round, and the one `§A.37`'s ownership rule was written to
   dissolve. The diff touches `verification/lean/edge_rigidity_probe.py`, the file carrying three
   sealed heads, so a landing built by inspecting which files moved would add a `P` commit. **The
   shape is named by the freeze and not by the diff**: this round owns guard contracts about the live
   row, owns no seal state, and lands `E` → `L`. `§A.37` states it in terms — a later round "does not
   acquire a pin commit merely by touching the guard file that carries it" — and a pin added here
   "would pin nothing". Guarded against by the shape declaration at the head of this file, by status
   rule clause 6, by the chronology control, and by the allowed final report, which requires the
   landing shape to be stated.
2. **Altering a sealed head to make a check pass.** The inverse failure: an execution that finds an
   archive clause red and repairs it at the constant. The three sealed heads belong to their own
   rounds. Guarded against by status rule clause 6 and by `AJ8`'s bounding clause.
3. **Reconstructive inference presented as a finding.** A reader who knows the programme can supply
   an argument for either label that the record does not contain. The evidence rule forbids it; the
   final report states, for each determination, which quotation carries it.
4. **Reading a discharged condition as a strengthened result.** Named first in the non-licence
   section because it is the natural misreading of any status round: the label describes the row, and
   the theorems are what they were. The post-round sentences each close by saying so.
5. **Losing the organizing caveat.** Reporting `AJ2` or `AJ3` positive without it turns an
   instantiation finding into a verification finding. Status rule clause 12 carries it verbatim at
   every positive.
6. **Merging the two halves of the hypothesis, or the two scopes of the lift half.** `AJ1` requires
   the halves reported separately; `AJ3` requires the covariance statement and the carrier reported
   separately. Collapsing either would let `AJ6-derived` fire on a question strictly easier than the
   one the target asks, which is what the gate exists to stop.
7. **Treating silence as denial.** The vocabulary's entry for `DERIVED` says rows reach it and leave
   the queue, so how many rows carry it is a question the execution answers by a bounded search and
   reports as it finds it. Whatever that count is, it is a fact about the queue: neither evidence
   that the label is unavailable nor evidence that it applies.
8. **Repairing a mutation control by deleting it.** `_a6p_m6`, `_a6d_m25` and `_a6i_m10` each rewrite
   the live label cell from `CONDITIONAL` to `DERIVED` and require the guarded clause to reject the
   result. Under `AJ6-derived` those rewrites become no-ops and the controls fail by construction —
   and the departure sharpens this, because the label cell they rewrite is then in the settled record
   and not in the queue at all, so a control left pointed at the queue would rewrite nothing whatever
   the label said. **The repair is to re-point each control at an overclaim of the new state — a
   settled row asserting that the assumption was verified, or a queue row re-added for the departed
   obligation — preserving each as a mutation control its guarded clause rejects**; deleting one, or
   weakening it to a rewrite the clause would reject trivially, is a defect of the execution and is
   checked for in the final report.
9. **Editing a merged record to keep it consistent.** Round 1's result note records that round 1 left
   the `GAP` label in place; the propagation's `README` paragraph and round 2's record say what those
   rounds did with the label. Each is a true statement about its own round under every outcome here.
   Status rule clause 7 forbids editing them, and `AJ8` names the three clauses expected to stand.
10. **Under-counting the guard surface.** A clause that pins the row by paraphrase rather than by the
    string would escape the search that built `AJ8`'s candidate list, and the failure would surface as
    a red landing or, worse, as a clause quietly weakened to pass. `AJ8`'s bounding clause requires
    the discrepancy to be recorded and the freeze reported as having under-counted.
11. **Deleting the departed row instead of recording it.** Under `AJ6-derived` the row leaves the
    queue table; striking it without writing `ROW-derived` verbatim into the settled record would drop
    the obligation's record from the file and would falsify `_A6P_ROW`'s membership clause, which asks
    the whole file and not the queue. The destination, its heading, its standing note and its table
    header are frozen in `AJ7`, and the row is copied, not paraphrased. **A departure that leaves no
    record is not a departure; it is a deletion**, and it is checked for in the final report.
12. **Disturbing a row the departure does not reach.** Removing one row from a table is where a
    neighbouring row's cells or the table's order quietly change. Under `AJ6-derived` the nine
    remaining rows are byte-identical and keep their order, and the execution verifies that against
    the base rather than asserting it.
13. **Resolving the landing conflict by side.** The `ROADMAP` row and its obligation table are shared
    ground that sibling rounds move, and a departure makes the collision likelier, since the table's
    row set changes rather than one cell of it. `§A.37` requires conflicts resolved by merits: this
    round's landing takes its own row, its section and — under `AJ6-derived` — the settled record from
    the execution, and every row a sibling moved from `main`; afterwards the landing is verified to
    add exactly this round's own diff against its own base and nothing else.
14. **Folding what stands outside `A6Cov` into what the label tracks.** The natural compression, and
    the one the owner's ruling forbids: writing the hypothesis and the §3.1 residual into one clause
    makes the assumption conditional on material that was never part of the condition, and would block
    `AJ6-derived` on something the row does not track. `AJ1`'s separation clause, `AJ4`'s two lists,
    the gate's "what the gate does not test" paragraph and status rule clause 5 exist for this
    hazard, and the final report states for the row, the section and the note that the two are
    distinct.
15. **Consuming a sibling result present at the base but absent from this freeze.** Governed by the
    anti-contamination invariant, carried verbatim above.
16. **Reading round 2's "recommends none" as a prohibition.** Round 2 declined to take the decision
    and named it as belonging to a separate round. That is this round's charter, quoted above, and
    not a bar on it.
17. **Scope creep into the gauge derivation or the physical premise.** Both are outside the round in
    terms, and both are material the adjudication is matched against rather than material it may
    advance.

## Definition budget

**ZERO.** No Lean module, no definition, no theorem, no probe function, no new guard tag. The round
writes prose, a row string, and the guard contracts `AJ8` enumerates. If the adjudication uncovers a
precise formal subclaim worth separating, the execution **names it and does not build it**, and it
becomes a candidate for a later round with its own control plane.

## Evidence level

**Type P throughout.** No target is at evidence level 2, there is no axiom table, and there is no
`#print axioms` line, because no Lean is written. The result note says so in terms rather than
leaving the absence to be inferred. **No `sorry`, no `axiom`, no `native_decide`** appears anywhere,
which is trivially true of a round that writes no Lean and is recorded so that it is checked rather
than assumed.

## The chronology control

Phrased so that each clause is checkable mechanically.

1. **This preregistration is merged alone**, before any execution object exists. Once merged it is
   **immutable**; an execution that diverges records the discrepancy rather than repairing it.
2. **The mandated execution base is the merge commit of this control plane's pull request.** The
   execution branches from exactly that commit and from nothing else, and its first act is
   `git hash-object` on this file at that base, compared against the blob this control plane merges
   as, before any target is executed.
3. **The chronology precondition, mechanically checkable at the base.** All three landed A6 rounds
   must have merged before the execution begins. At the base:
   - `git merge-base --is-ancestor 58100aea15eea8f5808b351d64163f55c9fed1bf HEAD` exits `0`
     (the covariance propagation's sealed head);
   - `git merge-base --is-ancestor d0b8c6e83c32a01a586f947c0dfd9618a8b42a91 HEAD` exits `0`
     (round 1's sealed head);
   - `git merge-base --is-ancestor 93405f3ff7eb4818a2895b5f5e2861094d9fe757 HEAD` exits `0`
     (round 2's sealed head);
   - `verification/lean/edge_rigidity_probe.py` at the base contains the three assignments
     `_A6P_SEALED_HEAD = '58100aea15eea8f5808b351d64163f55c9fed1bf'`,
     `_A6D_SEALED_HEAD = 'd0b8c6e83c32a01a586f947c0dfd9618a8b42a91'` and
     `_A6I_SEALED_HEAD = '93405f3ff7eb4818a2895b5f5e2861094d9fe757'`, each character-for-character;
   - `AGENTS.md` at the base contains the heading
     `## §A.37 Round lifecycle: control plane, then execution and landing` and both numbered clauses
     of its landing-shape split.

   A failure of any of these is recorded as a discrepancy and the execution does not repair the
   freeze.
4. **No new guard file is added and no guard tag is reserved.** The definition budget is zero and no
   Lean module is written, so there is no kernel object for an ancestry guard to order.
5. **No seal state is created or altered.** The three sealed heads, the three merge constants and the
   three base constants are read and never written.
6. **Because the round is non-sealing, its landing under `§A.37` is the merge alone**: current green
   `main` as first parent, the sealed execution head as second, and **no archive-pin commit**. The
   sealed execution commit is never modified; conflicts are resolved in the landing merge and never
   in the sealed commit.
7. **The `ROADMAP` row and its obligation table are shared ground**, and sibling rounds may move rows
   in the same table between this freeze and this landing. The landing resolves such collisions **by
   merits per `§A.37`** — this round's own row, its section and, under `AJ6-derived`, the settled
   record from the execution; every other row from `main` — and afterwards the landing is verified to
   add exactly the execution's own diff against its own base and nothing else, by comparing the two
   diffs and accounting for every difference. A clean automatic merge is not treated as evidence of a
   correct one. **Under `AJ6-derived` the collision is over the table's row set rather than over one
   cell**, so the verification names, row by row, which rows `main` has since moved and confirms that
   each survives the landing.
8. **The certification of record is the run whose `head_sha` is the sealed execution head**, and not
   whichever run happens to be latest on the branch.
9. **Full continuous integration passes again on `L`** before the pull request merges, and the
   resulting `main` build is green before the next round's landing is constructed.

## Non-doings

No Lean. No definition. No new guard. No new guard tag. No archive pin. No seal constant touched. No
manuscript edit. No census anchor. No merged result note, preregistration or audit edited. No `README`
round record edited. No other `ROADMAP` row, section or research status touched. **No row but
`P1 — A6` moved, and that row moves only under `AJ6-derived`, into the settled record `AJ7` freezes
rather than out of the file.** No second settled record, and no change to the `INDEPENDENT` one. No
item moved from `AJ4-out` into the hypothesis the label tracks. No reading adopted, revised, ranked or
identified with another. No re-derivation of any landed target. No new object, and no distinction
drawn on the record's behalf.

## Execution discipline

The execution produces **the result note**, the `ROADMAP` row and section, the settled record where
`AJ6-derived` requires it, the appended `README` paragraph, and the guard-contract edits `AJ8` bounds
— and nothing else. One pull request from the mandated base carrying the execution; after
certification the same pull request carries the landing merge, and no pin commit.

## Allowed final report

Every target with its outcome, evidence type, strength and the quotation carrying it; the two halves
of the hypothesis reported separately; the two scopes of the lift half reported separately; `AJ4-in`
and `AJ4-out` reported as two lists; `AJ5`'s clause-by-clause collation; `AJ8`'s surface with, for
each entry, whether it changed; under `AJ6-derived`, the departure's six items each reported done or
recorded otherwise, with the queue's remaining rows verified byte-identical and in order; the
organizing caveat verbatim at every positive of `AJ2` and `AJ3`; the discrepancy section; the single
frozen post-round sentence; an explicit statement that the round is type P with no axiom table; and an
explicit statement that the round is **non-sealing**, that no seal constant was touched, and that the
landing is `E` → `L` with no pin. Nothing else.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **`CONDITIONAL` and `DERIVED` are the only candidates the predictions weigh**, but `AJ6` runs all
   seven entries of `VOCAB` and records the disposition of each. The freeze expects the other five to
   be set aside on the propagation's own quoted grounds and requires them checked rather than assumed.
2. **The row's reasons are treated as adjudicable separately from its label cell.** A different
   reading would treat the row as one atom, so that the label standing means the row standing
   byte-identical. This freeze splits them, which is why `AJ-stand-asis` and `AJ-stand-restate` are
   two outcomes with two post-round sentences, and records the choice here.
3. **The destination of the departed row is the file's own form for what has left the queue.** The
   `INDEPENDENT` record is the precedent, and this freeze follows it with the queue's five columns so
   that the row survives character-for-character rather than as a paraphrase. An alternative would
   record the departure only in the row's section and let the row itself go; this freeze does not,
   because a row recorded nowhere is a row deleted, and records the choice here.
4. **The substratum identification is treated as a candidate tracked hypothesis, not as settled
   background.** Whether the record presents it as this row's hypothesis or as a premise ambient to
   the programme's rows is `AJ4-in`'s business and is the gate's hinge, and the freeze declines to
   settle it in advance in either direction.
5. **The round is non-sealing.** An alternative would give the adjudication its own guard tag and its
   own ancestry seal. This freeze does not, because the definition budget is zero, there is no kernel
   object to order, and the blob pins in the start-state tables carry the immutability the round
   needs — and because taking a seal here would be taking ownership of state the round has no use
   for.

## The owner's rulings, carried into this freeze as its authority

Two questions this control plane put to the owner are settled, and the settlements are written into
the targets, the gate, the status rule, the frozen row texts and the frozen post-round sentences
above rather than left as options.

1. **Queue departure belongs to `AJ6-derived` itself.** `DERIVED`'s vocabulary entry says rows reach
   that state and leave the queue, so a round that writes the label and leaves the row in the queue
   produces an inconsistent record. The departure is therefore part of the outcome, specified in
   `AJ7` in six items, covered by `AJ8`'s census and by hazards 8, 11, 12 and 13, and carried in
   `AJ-move`'s frozen sentence. **The other three outcomes leave the row and the queue as they are.**
2. **`ROW-conditional`'s named hypothesis is the substratum identification.** The part of the gauge
   derivation that consumes the inner product, unitarity as a constraint, the condensate `Σ`, the
   stabilizer in `U(6)` or the cubic decomposition is retained in the record as material standing
   **outside `A6Cov`**, and is no component of the A6 condition. The separation is carried by `AJ1`'s
   separation clause, `AJ4`'s two lists, the gate's "what the gate does not test" paragraph, status
   rule clause 5, both frozen row texts and hazard 14, so that the gate tests the substratum
   identification and is not blocked by material that was never part of the condition.

## Open to the owner before this freeze merges

Recorded so that the amendment happens before the merge, which is the only time a freeze may be
amended.

1. **Whether the section's sentence naming the stronger-label decision as belonging to a separate
   round stays as written** once that round has run. The freeze leaves it standing, since it is
   accurate in manuscript voice; an owner who wants it recast should say so before the merge.
