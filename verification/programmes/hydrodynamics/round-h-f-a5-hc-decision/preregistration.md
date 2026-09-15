# Hydrodynamics round H-F — the A5 / H-C decision: what the programme does next on the H-B axis: CONTROL PLANE

**Type-P round.** Every target is a determination about **what the merged record says**, settled by
locating and quoting passages with coordinates, not by proving anything. No Lean is written, no
theorem is proved, no limit is taken, no manuscript is read and no manuscript is edited. The
evidence rule below is frozen for that reason.

**The round label `H-F` is an identifier, not an ordinal.** It is not a rung of the H1–H7 ladder, it
is not round `H-C`, and its `HF` target prefix is not the programme's `S1`–`S5` continuum-breakdown
branch and not rounds `S-A`/`S-B`. **`H-F` is not a taxonomy value either**: `../PROGRAMME.md` §4's
four outcome labels are `HD`, `HC`, `HI` and `HO`, and this round applies none of them to anything.

**Blob identity is authoritative.** The commit locates the tree; the blob is what is compared. The
result note pins this file by content.

## The round's shape, declared in `AGENTS.md` `§A.37`'s terms

**This is a NON-SEALING round.**

`§A.37` splits the landing shape on **what a round owns, not on what it touches**
(`AGENTS.md:773`). This freeze **owns no seal state**: it creates no seal constant and no pin state,
and it **does not take ownership of changing any existing seal constant**. The definition budget is
zero, no Lean module is written, and no kernel object exists for an ancestry guard to order, so no
guard tag is reserved and none is added.

**The landing shape, therefore: `E` → `L`, with no archive-pin commit `P`.** The landing merge's
first parent is current green `main`, its second parent is exactly the exact-head-certified
execution head `E`,
and conflicts are resolved in `L` and never in `E`. `§A.37` states the non-sealing case in terms
(`AGENTS.md:786–788`): such a round "**may** modify other contracts inside an existing guard; it
**may not** alter existing seal constants. It has nothing to pin, and a pin commit added there would
pin nothing."

### The seal constants this round would own, and the ones it would not

**Would own: none.** The table below is the complete inventory of seal state in scope, and every row
is a row this round reads or leaves alone.

| constant | owned by | this round |
| --- | --- | --- |
| `_HYA_BASE`, `_HYA_SEALED_HEAD`, `_HYA_MERGE` (guard section `R7-HYA`) | round H-A, which set them | **read and never written** |
| `_HYB_BASE`, `_HYB_SEALED_HEAD`, `_HYB_MERGE` (guard section `R7-HYB`) | round H-B, which set them | **read and never written** |
| `_HYE_BASE`, `_HYE_SEALED_HEAD`, `_HYE_MERGE` (guard section `R7-HYE`) | round H-E, whose freeze reserves them | **not touched, present at the base or not** |
| any constant a sibling round sets in `verification/lean/edge_rigidity_probe.py` after this freeze | that round | **not touched** |

`§A.37` fixes the principle this table obeys, quoted at `AGENTS.md:796–799`:

> **An archive seal belongs to the round that set it, and stays immutable afterwards.** A later
> round does not re-pin it, and does not acquire a pin commit merely by touching the guard file that
> carries it. An existing seal constant changes only in a round whose own preregistration says in
> advance that it changes it — and such a round is *sealing*, because it has taken ownership of that
> state prospectively rather than as a side effect of its diff.

**The `R7-HY*` family belongs to the rounds that set it.** This round adds no member to that family
and alters no member of it. Whether the family should be extended to cover prose-only rounds of this
programme is an owner decision round H-D recorded and did not make
(`round-h-d-a5-status-adjudication/result.md:917–918`); it is named again at `HF6` and is made
nowhere here.

## What this round is

Round H-B executed **one candidate** and was not reported closed. Round H-D examined the status of
one condition relative to the hydrodynamic target and returned two of its three answers UNDECIDED.
The question this round freezes is the one those two leave standing: **on the axis H-B opened, what
is the programme's next round — a further round on the A5 axis H-D examined, or round `H-C`?**

The round is an **adjudication over the merged record**. It enumerates, by quotation with
coordinates, what each of the two candidate next steps requires at the base and which of those
requirements the merged record already meets; it determines which axis the record supports as the
next round; and it names, without making, the owner decisions that stand either way.

**It decides which round to write next. It decides no question either round would ask.** In
particular it settles nothing about the condition H-D examined, takes no limit, fixes no scaling map
and moves no obligation.

## THE A5 ANTI-CONFLATION CLAUSE, FROZEN VERBATIM

Two different statements are called A5 in this corpus, and this round touches both. The clause below
is **THE CLAUSE**, and it is carried as a block quote **at every prose mention of A5** in this file
and in every artifact of this round.

**How each carriage is written, and why.** Each carriage opens with one line naming where it is
being carried, and then states the clause word for word. The naming line is there so that the
carriages read as distinguishable copies of one clause rather than as one paragraph pasted
repeatedly — which is a defect the repository's `duplicate_check` exists to catch, and the pattern
is `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md`'s — and
it changes nothing about the clause it introduces.

**Three kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed frozen
post-round sentences, which cannot admit a quotation inside a quotation; table cells and bare list
entries that name `A5-ker` or `A5-ms` under those disambiguated names and do nothing else; and
verbatim quotations of a source, which are reproduced in the source's own words and are governed by
the clause carried in the section they sit in.

**THE CLAUSE:**

> **THE A5 ANTI-CONFLATION CLAUSE.** `A5-ker`, the kernel's A5, is additivity of the substratum rule
> over the alphabet — `∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`, at
> `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:102`. `A5-ms`, the manuscripts'
> A5, is linearity of the wave equation, at [Substratum §3.1]. **These are two statements, and no
> identification theorem between them exists in the tree**; `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean:211`) is an instance result for the one rule where both are in
> play and identifies nothing. **This round builds no identification, assumes none, needs none, and
> writes "A5" unqualified nowhere**: every target, prediction, gate, status sentence and hazard here
> that touches A5 says which of `A5-ker` and `A5-ms` it means, and a sentence that says "A5" without
> saying which is a defect of this round.

**The clause is a bookkeeping discipline of this round, not a finding about the corpus.** Recording
that two statements are two is what round H-D's `A5S-0a` did at full strength
(`round-h-d-a5-status-adjudication/result.md:69–88`), and this round consumes that finding at H-D's
own scope and adds nothing to it.

## The trap this freeze is built around: round H-D-SR's outcome is not available

A sibling round, **H-D-SR**, is frozen on `main` at this round's base and is **executing in
parallel**. Its freeze
(`round-h-d-source-reconciliation/preregistration.md`) states its own subject at lines 25–36: it
establishes "by quotation with coordinates, **exactly what the sources say and exactly where they
disagree**", and it "does not adjudicate the disagreement". The disagreement is the one round H-D
named for the owner at `round-h-d-a5-status-adjudication/result.md:490–494`:

> **The frozen discipline, observed.** This round **adopts neither form over the other**, **edits no
> manuscript**, and **resolves no divergence**. **The propagation question is named here for the
> owner and the round stops**: five statements of the entailment question stand in the corpus, four
> in the open form and one resolved in the negative, and whether the negative resolution should
> propagate to the other four is an owner decision this round records and does not make.

**What this round may consume, and what it may not.** It may consume round H-D's own merged result
note and round H-D-SR's **freeze**, both of which are on `main` at the base and are pinned in the
start-state table. It may **not** consume, anticipate, assume, or state a preference among the
outcomes of H-D-SR's execution, and **no target, prediction, gate or status sentence of this round
is stated in terms of how that reconciliation lands**. `HF4` audits that property explicitly and
`HF1-c` is the target that holds the source-level question at arm's length rather than enumerating
it as an input.

> **THE A5 ANTI-CONFLATION CLAUSE, carried at this mention — the H-D-SR exclusion.** `A5-ker`, the
> kernel's A5, is additivity of the substratum rule over the alphabet — `∀ c c' : 𝒮.ι → 𝒮.V,
> 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`, at
> `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:102`. `A5-ms`, the manuscripts'
> A5, is linearity of the wave equation, at [Substratum §3.1]. **These are two statements, and no
> identification theorem between them exists in the tree**; `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean:211`) is an instance result for the one rule where both are in
> play and identifies nothing. **This round builds no identification, assumes none, needs none, and
> writes "A5" unqualified nowhere**: every target, prediction, gate, status sentence and hazard here
> that touches A5 says which of `A5-ker` and `A5-ms` it means, and a sentence that says "A5" without
> saying which is a defect of this round.

**The entailment question is about `A5-ms`'s warrant** — the amplitude-scale gauge principle
[SM §4.1]'s linearity-equivalence lemma routes to it — and this round records that attribution from
H-D's quoted words at `HF3` rather than asserting it. Round H-D-SR's freeze names both statements
under its own labels at `round-h-d-source-reconciliation/preregistration.md:221–224`, and this
round's `A5-ker`/`A5-ms` are the same two objects under this freeze's own names.

## What this round excludes, in terms

- **No manuscript is read.** `papers/` and `book/` are outside this round's surface entirely. That
  is a deliberate, mechanically auditable boundary: round H-D-SR is sweeping exactly that surface
  concurrently, and a round that re-read it would be running that sweep a second time on a partial
  charter. Where this round needs a manuscript sentence, it quotes **H-D's merged result note**
  quoting it, under rule 2 of the evidence rule, and says so.
- **Round H-D's three answers are not re-decided.** They are consumed as merged, at H-D's own scope
  and strength, and are restated no more strongly.
- **Rounds H-A and H-B are not reopened.** Their findings, labels, scopes and open owner questions
  stand exactly as those rounds state them.
- **Round H-E is not consumed.** Its freeze is read for what it says about its own scope and shape;
  **its result is not an input**, whether or not it has landed by the time this round executes.
- **No obligation of the H1–H7 ladder changes status**, none is closed, and no limit, scaling map,
  closure, PDE or transport coefficient is asserted or denied.
- **A6 is outside this round.** Whatever status the execution base carries for it is consumed
  unchanged and no status for it is asserted here.
- **The OI → QM chain, Track B, Track I, Bell and gravity are outside this round**, in both
  directions — the programme's control 1.

## Start state, pinned by blob

Every file this round reads for content, with its `git hash-object` value at the base
`b78eac870ba3ee9ef9e98659ac933bf97dc62226`, the certified `main` from which this control plane's
branch is cut. This control plane's pull request carries this file alone, so its merge commit — the
mandated execution base — carries the same blobs except where a sibling landing has moved one, which
is a recorded discrepancy and not a repair.

| path | blob at `b78eac87` |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` |
| `verification/README.md` | `d25eb2d44d0aa324c095930f40174296fd0f2279` |
| `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` |
| `../PROGRAMME.md` | `b7b24112a462aee083c3e8f3c2980283b38cd10f` |
| `../round-h-a-source-audit/preregistration.md` | `934cd6aff1cfb07b823c9b131693ee59bb98c632` |
| `../round-h-a-source-audit/result.md` | `56d34463cf6b68bf28d9ab99b6e09f9fa287d826` |
| `../round-h-b-reversible-fluid-substratum/preregistration.md` | `37cc9dae301ee10d55adb73b296aa2fc7d0578e3` |
| `../round-h-b-reversible-fluid-substratum/result.md` | `dc03b582ed718d374c471b27403b282a295d5c85` |
| `../round-h-d-a5-status-adjudication/preregistration.md` | `a2398c3954f13ac458184c70df8f1ec6b321cc9b` |
| `../round-h-d-a5-status-adjudication/result.md` | `f80dd8832955cb7f17e9712ccdafae364a4059e3` |
| `../round-h-d-source-reconciliation/preregistration.md` | `d222e5c6f248bddf8327303523a71b5f82a050d4` |
| `../round-h-e-h3-closure-bridge/preregistration.md` | `9f3f4ff4115c8d95215462acd257b4f6b32c9926` |
| `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean` | `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean` | `fd5f54d8cbba4f68b67335c111d39a2add0c642f` |
| `verification/lean-mathlib/OIBridge/HexLatticeGas.lean` | `374db0387337960888a67f4e98609446c8a1b871` |

**Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.**

**One mechanical sweep runs over a directory rather than over this table** — `HF1-a`'s search of
`verification/lean-mathlib/OIBridge/*.lean` **as that tree stands at this freeze's certified
drafting base `b78eac870ba3ee9ef9e98659ac933bf97dc62226`**, for a carrier of the condition H-D's `A5S-1c`
names. **The surface is fixed at that commit and not at the execution base**, so that no round
landing after this freeze is drafted can enter the sweep: the blindness boundary this freeze draws
around its siblings would otherwise be undone by the search itself. Its surface is named and bounded
in the target itself, and **the boundary of the sweep is recorded with
its finding**, exactly as H-D recorded the boundary of its own enumeration. A sweep's surface is not
a claim that every file on it was quoted; it is a claim about what a named search over a named
surface returned.

**`verification/lean/edge_rigidity_probe.py` is read as context** — for the `R7-HY*` inventory above
and for nothing else — and is **not modified**. The blob at this base differs from the blob rounds
H-D-SR and H-E pinned at theirs, which is the ordinary consequence of sibling landings and is
recorded here rather than treated as a finding.

## The anti-contamination invariant, FROZEN VERBATIM

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

**The `§A.37` justification.** Under `§A.37` "the control plane's **merge commit is the mandated
execution base**. The execution branches from exactly that commit and from nothing else, and its
first act is to verify that the preregistration at that base has the blob the freeze names, before
any target is executed" (`AGENTS.md:697–700`). The base is therefore fixed at the moment this
control plane merges and carries whatever `main` carried at that moment — which is a fact about
*when this file merged*, not a statement about what this round may read. What a round may read is
fixed by its freeze, and by nothing else; `§A.37` also fixes the converse discipline, that "an
execution that diverges from it **records the discrepancy** rather than repairing the freeze"
(`AGENTS.md:693–695`), so a start-state movement is a thing to record, never a licence to widen.

**Why this matters more here than usual.** **Round H-D-SR and round H-E will both have landed by the
time this round executes.** Neither is an input. H-D-SR's result may be present at the base as a new
result note in its own directory, and H-E's may be present as a new Lean module, a new `R7-HYE`
guard section, a refreshed `../PROGRAMME.md` §8 and a new `ROADMAP` section. **Their presence at the
base is a fact about the base and not an input to this round**, and landing position does not enter
the question: a sibling that merged before this control plane is present without thereby being
consumed. Where a pinned blob has moved because of one of them, the execution records the movement,
diffs it against the passages this round quotes, reports whether any quoted passage moved, and
**consumes none of the newer content as evidence**.

## The evidence rule, FROZEN

The round is **type P**. Every determination must be carried by one or more of:

1. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
2. a **verbatim quotation** from a merged result note or preregistration, with its coordinate; or
3. an explicit, recorded statement that **the passage sought does not exist**, on a **named and
   bounded** search whose surface is stated with the finding.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the record must
mean X, because otherwise Y would fail", or "these two passages come to the same thing once one
allows for Z", is **not evidence** and may not carry any target. It may appear only in a clearly
labelled analysis paragraph that states in terms that it is not evidence and that **no target rests
on it**.

**Where the record is silent, the finding is that it is silent.** Silence is neither assent, nor
denial, nor a licence to supply the missing statement.

**Strength is recorded per determination**, as `full`, `high`, `medium` or `UNDECIDED`. A
determination carried by a passage that names a thing without stating it is at most `medium`. A
determination that rests on a bounded search returning nothing is reported as a statement about that
search and about nothing off it.

## The objects, FROZEN

**`axis-A5` — the A5 axis.** The line of work round H-D examined: the logical status of the
condition relative to the programme's objective, its two UNDECIDED answers, and the questions H-D
recorded as what would settle them.

**`axis-HC` — the H-C axis.** Round `H-C` as `../PROGRAMME.md` §6 states it, together with the H4
scaling obligation §3 states and the five-item skeleton round H-A recorded against it.

**`A5-ker` and `A5-ms`** — the two statements THE CLAUSE distinguishes, used under those names
throughout and never merged.

**`carrier-question` — which substratum an `axis-HC` round would run on.** The merged record carries
two exhibited candidates inside the kernel's `Substratum` interface: the manuscripts' wave
representative that round H-A audits, and round H-B's streaming-and-collision gas. This round
enumerates the choice and its recorded consequences and **makes it nowhere**.

**`next-round` — the determination this round reaches**: which of `axis-A5` and `axis-HC` the merged
record supports as the programme's next round on the axis round H-B opened.

The round adds **no object of its own** beyond those five and the bookkeeping labels of THE CLAUSE.
Where a distinction is needed that the sources do not draw, the execution **records that the sources
do not draw it** and does not draw it on their behalf.

## Recorded readings — the one permitted pre-execution object

Located by hand **before this file was written**, recorded here so that no execution-specific
artifact precedes the freeze. **Nothing here is evidence at any level above "recorded reading"**, and
the execution re-reads each at the mandated base and reports what it finds, including any divergence
from what is recorded here.

1. `../PROGRAMME.md` §6's `axis-HC` entry stands at lines 198–200 and requires the scaling and
   convergence topology to be frozen **before execution**; §4's outcome label `HC — Conditional`
   stands at lines 107–109, a different object under the same two characters.
2. Round H-A's `H4a` scaling skeleton stands at `../round-h-a-source-audit/result.md:227–239`, five
   items at lines 232–237 and the statement that none is fixed by the manuscripts or by A1–A6 at
   line 239.
3. Round H-D's two settling conditions for its question (c) stand at
   `../round-h-d-a5-status-adjudication/result.md:626`, `:630` and `:635`, the negative one naming a
   derivation "of the Euler-level limit, the viscous correction or the incompressible limit … **at a
   stated scaling map and convergence topology**".
4. Round H-D's scope statement at `../round-h-d-a5-status-adjudication/result.md:765` reads "**The
   sufficiency question belongs to H3–H7 and to H-C**".
5. Round H-D's `A5S-1c` records the obstruction to its question (a) as an absent carrier, with what
   would change the outcome at `../round-h-d-a5-status-adjudication/result.md:284–286`.
6. Round H-B's open owner question stands at
   `../round-h-b-reversible-fluid-substratum/result.md:58–62`.
7. Round H-D-SR's freeze is present at the base and its execution had not merged when this file was
   written; round H-E's freeze is present and its execution had not merged. `HF4` and the chronology
   control re-determine the state of both at the execution base, where both are expected to have
   landed.

## The targets, FROZEN

Every target is **type P**. `HF1-a` is type P over kernel objects: a name search over a named tree,
not a proof and not a dependency analysis of proof terms.

### `HF0` — locating controls

**What settles it.** Locate and quote, with file and line coordinates at the mandated base:

| # | the passage | where it was located while drafting |
| --- | --- | --- |
| 1 | `../PROGRAMME.md` §1's statement of the ultimate objective and its two acceptable endpoints | `../PROGRAMME.md:11–21` |
| 2 | `../PROGRAMME.md` §3's obligations H3, H4, H5, H6 and H7 as stated | `../PROGRAMME.md:69–95` |
| 3 | `../PROGRAMME.md` §4's four outcome labels, `HD`, `HC`, `HI`, `HO` | `../PROGRAMME.md:99–119` |
| 4 | `../PROGRAMME.md` §6's `axis-HC` entry in full | `../PROGRAMME.md:198–200` |
| 5 | `../PROGRAMME.md` §7's controls 2, 5, 8, 9 and 10 | `../PROGRAMME.md:212–223` |
| 6 | `../PROGRAMME.md` §8's one-line state as it stands at the base | `../PROGRAMME.md:227–229` |
| 7 | `verification/ROADMAP.md`'s section "Hydrodynamics programme — round H-A executed" in full | `verification/ROADMAP.md:819–834` |
| 8 | `verification/ROADMAP.md`'s section "Hydrodynamics programme — round H-B: one candidate executed" in full | `verification/ROADMAP.md:836–858` |
| 9 | round H-D's three answers, `A5S-4a` | `../round-h-d-a5-status-adjudication/result.md:656–678` |
| 10 | round H-D's `A5S-3d`, the boundary and the two settling conditions | `../round-h-d-a5-status-adjudication/result.md:619–638` |
| 11 | round H-D's `A5S-5b` scope statement | `../round-h-d-a5-status-adjudication/result.md:747–767` |
| 12 | round H-D's guardrail on what round H-B supplies | `../round-h-d-a5-status-adjudication/result.md:575–579` |
| 13 | round H-B's post-round programme status, points 1 and 4 | `../round-h-b-reversible-fluid-substratum/result.md:48–64` |
| 14 | round H-A's `H4a` skeleton with its five items and its closing status | `../round-h-a-source-audit/result.md:227–239` |
| 15 | round H-D-SR's declaration of its own subject and its non-adjudication | `../round-h-d-source-reconciliation/preregistration.md:25–36` |
| 16 | round H-E's declaration of its own shape and its exclusion of the A5 lane | `../round-h-e-h3-closure-bridge/preregistration.md:20–53`, `:112–138` |
| 17 | `AGENTS.md` `§A.37`'s shape split and its archive-seal paragraph | `AGENTS.md:773–799` |

**What evidence counts.** Rule 1 or rule 2 of the evidence rule. A passage absent from the pinned
blob at the base is this target's falsifier and is recorded as a discrepancy, not repaired. **The
coordinates in the right-hand column are this freeze's recorded readings and are not evidence**; the
execution re-locates each at the base and reports the coordinate it finds.

### `HF1` — `axis-A5`: what the merged record leaves, and what each item is gated on

> **THE A5 ANTI-CONFLATION CLAUSE, carried at this mention — the `axis-A5` enumeration target.**
> `A5-ker`, the kernel's A5, is additivity of the substratum rule over the alphabet —
> `∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`, at
> `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:102`. `A5-ms`, the manuscripts'
> A5, is linearity of the wave equation, at [Substratum §3.1]. **These are two statements, and no
> identification theorem between them exists in the tree**; `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean:211`) is an instance result for the one rule where both are in
> play and identifies nothing. **This round builds no identification, assumes none, needs none, and
> writes "A5" unqualified nowhere**: every target, prediction, gate, status sentence and hazard here
> that touches A5 says which of `A5-ker` and `A5-ms` it means, and a sentence that says "A5" without
> saying which is a defect of this round.

#### `HF1-a` — question (a)'s obstruction, re-determined at the base

**What settles it.** Quote round H-D's `A5S-1c` obstruction and its "what would change the outcome"
sentence with coordinates; then determine, on a **named and bounded** search of
`verification/lean-mathlib/OIBridge/*.lean` **as that tree stands at `b78eac870ba3ee9ef9e98659ac933bf97dc62226`**, whether it carries a predicate or a result establishing
observer-admission for a concrete substratum — the carrier H-D records as absent. **The search
surface is frozen at that commit.** It is later than the base of H-D's own enumeration, so the
re-check is not a restatement of H-D's; and it is earlier than any sibling landing of this
fan-out, so no sibling round's Lean can enter it. The surface, the search terms and the boundary
are recorded with the finding.

**What evidence counts.** Rule 2 for H-D's statement; rule 1 for any carrier found, quoted with its
coordinate; rule 3 for the absence, with the search named and bounded. **Reconstructive inference is
forbidden here**: a result that could be read as supplying admission, but does not state it, is not
a carrier and may be discussed only in a labelled analysis paragraph.

#### `HF1-b` — question (c)'s two settling conditions, and where each one lives

**What settles it.** Quote both settling conditions from `A5S-3d` with coordinates, and determine,
for each, **which axis the record assigns it to** — carried by quoted words and not by this round's
reading. The positive condition names a derivation of some step of H3–H7 that takes `A5-ker` as a
hypothesis and needs it, or a no-go; the negative condition names a derivation of the Euler-level
limit, the viscous correction or the incompressible limit at a stated scaling map and convergence
topology.

**What evidence counts.** Quotation with coordinate. **An assignment not carried by the quoted words
of a source is not a finding** and is recorded as silence instead.

#### `HF1-c` — the source-level question, held at arm's length

**What settles it.** Record, by quotation with coordinates, that the entailment question and its
propagation stand as round H-D named them for the owner and that round H-D-SR's freeze scopes the
reconciliation, adjudicates nothing, and makes no owner decision. **Record that this round consumes
no outcome of that execution**, and enumerate the sentences of this freeze that would have to exist
for it to do so — there being none.

**What evidence counts.** Quotation with coordinate of the H-D passage and of the H-D-SR freeze. **No
outcome of round H-D-SR is stated, assumed, anticipated, ranked or preferred**, and a result note
that states one is a defect of this round. If round H-D-SR's result note is present at the base, its
presence is recorded as a fact about the base under the anti-contamination invariant and **its
content is not read into any determination**.

#### `HF1-d` — round H-B's open owner question, restated at its own scope

**What settles it.** Quote round H-B's post-round programme status point 4 with its coordinate, and
record that the admissibility of the class its candidate lies in stands open in H-B's own words.

**What evidence counts.** Quotation with coordinate. **Naming the question is not answering it**, and
no sentence of this round answers it or implies an answer.

### `HF2` — `axis-HC`: what the merged record says the next round must fix

#### `HF2-a` — the `axis-HC` entry, quoted, and what it requires before execution

**What settles it.** Quote `../PROGRAMME.md` §6's `axis-HC` entry in full with its coordinate, and
report, from its own words, what it requires to be frozen before execution and what it requires to
be reported separately.

**What evidence counts.** Quotation with coordinate. **The entry is `../PROGRAMME.md`'s, not this
round's**, and the execution neither extends it nor narrows it.

#### `HF2-b` — the five scaling-skeleton items, reported separately

**What settles it.** Report round H-A's five `H4a` items **separately, one row each**, each recorded
as **fixed** on the merged record at the base with the passage that fixes it quoted, or **unfixed**
with the passage that records it unfixed quoted, or **silent** with the named and bounded search that
found no passage. Round H-B's record of which of the five its candidate fixes is quoted where it
bears on a row.

**What evidence counts.** The evidence rule, per row. **A row is not settled by another row**, and
the five are not summarized into a single verdict in place of the table.

#### `HF2-c` — does anything on the merged record block writing the `axis-HC` control plane?

**What settles it.** Determine, on a named and bounded search of the pinned round artifacts and
`../PROGRAMME.md`, whether any passage states that the `axis-HC` control plane cannot be written, or
makes any item `HF2-b` reports unfixed depend on an input the merged record does not carry.

**What evidence counts.** A verbatim quotation, with coordinate, of a passage that says one of those
things in its own words; or the recorded statement that the bounded search returns none. **A passage
that could be read as implying a blockage, but does not say it, is not evidence.**

**Outcome if nothing is found:** the finding is that **the record names no blockage on the search
described** — a statement about that search, and not a statement that the `axis-HC` round is easy,
ready, or likely to succeed.

#### `HF2-d` — the `carrier-question`, enumerated and not decided

> **THE A5 ANTI-CONFLATION CLAUSE, carried at this mention — the carrier enumeration.** `A5-ker`,
> the kernel's A5, is additivity of the substratum rule over the alphabet —
> `∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`, at
> `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:102`. `A5-ms`, the manuscripts'
> A5, is linearity of the wave equation, at [Substratum §3.1]. **These are two statements, and no
> identification theorem between them exists in the tree**; `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean:211`) is an instance result for the one rule where both are in
> play and identifies nothing. **This round builds no identification, assumes none, needs none, and
> writes "A5" unqualified nowhere**: every target, prediction, gate, status sentence and hazard here
> that touches A5 says which of `A5-ker` and `A5-ms` it means, and a sentence that says "A5" without
> saying which is a defect of this round.

**What settles it.** Enumerate, by quotation with coordinates, the exhibited candidates the merged
record carries inside the kernel's `Substratum` interface, and record for each **what the record
already says about it** that an `axis-HC` round would have to carry: for the wave representative,
round H-A's linearity gate and the class of coarse variables it is stated on, and round H-D's
`A5S-3c` reading of it; for round H-B's candidate, its conservation and stencil content, its
recorded `A5-ker` profile, and round H-B's guardrail and open owner question.

**What evidence counts.** Quotation with coordinate, at each cited round's own scope. **The choice
between the carriers is not made here**, no carrier is preferred, ranked or recommended, and each
recorded consequence is reported as the citing round states it and no more broadly.

**The restriction that makes this target safe.** A carrier's recorded `A5-ker` profile is a **fact
about that carrier**, proved by the round that proved it. Reporting it is not an adoption of
`A5-ker`, not an adoption of `A5-ms`, not a status for either, and not a statement that either is
required by or excluded from the hydrodynamic route.

### `HF3` — which A5 does each enumerated item mean?

> **THE A5 ANTI-CONFLATION CLAUSE, carried at this mention — the which-A5 determination.** `A5-ker`,
> the kernel's A5, is additivity of the substratum rule over the alphabet —
> `∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`, at
> `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:102`. `A5-ms`, the manuscripts'
> A5, is linearity of the wave equation, at [Substratum §3.1]. **These are two statements, and no
> identification theorem between them exists in the tree**; `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean:211`) is an instance result for the one rule where both are in
> play and identifies nothing. **This round builds no identification, assumes none, needs none, and
> writes "A5" unqualified nowhere**: every target, prediction, gate, status sentence and hazard here
> that touches A5 says which of `A5-ker` and `A5-ms` it means, and a sentence that says "A5" without
> saying which is a defect of this round.

**What settles it.** For every item enumerated at `HF1-a`–`HF1-d` and `HF2-d`, record, in a table
with one row each, whether the source states it of **`A5-ker`**, of **`A5-ms`**, of **both
separately**, or **does not say** — **carried by the quoted words of that source**.

**What evidence counts.** Quotation with coordinate, with the words that carry the classification
quoted inside the quotation. **A classification not carried by quoted words is not evidence.** Where
a source does not say, **the finding is that it does not say**, and this round does not supply the
answer: it neither reads the kernel statement into a manuscript sentence nor the manuscript
statement into a kernel one.

**`A5-ms` is quoted from round H-D's merged result note, at H-D's coordinate**, and is not located
afresh in `papers/`. That is this freeze's boundary choice, recorded under *Points at which this
freeze chose a reading*, and the execution states it in terms rather than leaving it to be inferred.

### `HF4` — the independence audit: does any determination depend on round H-D-SR's outcome?

**What settles it.** Walk every target, prediction, gate and frozen status sentence of this freeze,
one at a time, and record for each the sentence that shows its determination is reached without any
statement about how the source reconciliation lands. Record also whether round H-D-SR's result and
round H-E's result are present at the execution base, and that neither is read into any
determination.

**What evidence counts.** The targets themselves, cited; and, for each presence record, the fact of
the file at the base. **This target's finding is about this round**, not about the corpus, and it is
reported as such.

**If the walk finds a dependence**, that is this target's falsifier and the outcome is `HF4-dependent`:
the dependent target is reported **UNDECIDED** with the dependence named as its obstruction, this
freeze is **not** amended, and no outcome of round H-D-SR is supplied to rescue it.

### `HF5` — `next-round`: the adjudication

**What settles it.** The outcomes of `HF0`, `HF1`, `HF2` and `HF3` together, read through the two
gates below. **What counts as evidence:** nothing new — `HF5` adds no evidence of its own, is
reported at the strength jointly reached by the targets it rests on, and is labelled as **this
round's adjudication over the merged record** and never as a theorem.

Exactly one of four outcomes:

- **`HF5-H-C`** — the merged record supports round `H-C` as the programme's next round on this axis,
  and what its control plane must fix is enumerated here and fixed nowhere.
- **`HF5-A5`** — the merged record supports a further round on `axis-A5` as the next round, with the
  question named and its enabling condition **met at the base and quoted**.
- **`HF5-OWNER`** — the merged record discriminates in neither direction: both axes' next steps are
  writable, or neither is, on the record searched, and **which to write is an owner decision this
  round names and does not make**. This is a finding, not a failure.
- **`HF5-UNDECIDED`** — the comparison could not be carried out, with the obstruction named.

**The gate on `HF5-H-C`, FROZEN:**

> `HF5-H-C` may be written only if **both** of the following hold: `HF2-a` and `HF2-b` report what
> the `axis-HC` control plane must fix, item by item, **and** `HF2-c` finds no blockage on its named
> and bounded search — so that the next step on that axis is a control plane the programme's own §6
> entry assigns to it; **and** `HF1` reports at least one `axis-A5` item whose enabling condition is
> **unmet at the base**, quoted, and not merely unexamined. **`HF5-H-C` may not be written on
> `HF1`'s blockage alone**: that the other axis is gated is not that this one is ready, and an
> adjudication that rests only on the gating of `axis-A5` is reported `HF5-OWNER` instead.

**The gate on `HF5-A5`, FROZEN:**

> `HF5-A5` may be written only if `HF1` names an `axis-A5` question whose enabling condition is
> **met at the base**, with the meeting quoted. **It may never be written on an anticipated,
> assumed, or preferred outcome of round H-D-SR's execution**, on a carrier this round expects to be
> constructible, or on an owner decision this round expects the owner to take. If the only route to
> the enabling condition passes through one of those three, the outcome is `HF5-OWNER` and the route
> is named there as the owner's to open.

**Neither gate binds the predictions**; they bind the decision rule, so that neither outcome can be
reached on an easier question underneath it.

### `HF6` — the owner decisions, named and not made

**What settles it.** Assemble, in one place, the owner decisions the merged record carries on this
axis, each quoted from the round that recorded it, plus the ones this round's own adjudication
raises:

1. **whether the negative resolution of the entailment question propagates to the statements
   carrying the open form** — round H-D's named propagation question;
2. **whether the class round H-B's candidate lies in is admissible OI physics** — round H-B's open
   owner question;
3. **whether the `R7-HY*` guard family extends to prose-only rounds of this programme** — round
   H-D's chronology control 4;
4. **which later action carries out the refresh of `../PROGRAMME.md` §8** — round H-D's D7, whose
   wording round H-D's status rule 11 already fixes;
5. **the `carrier-question`** — which substratum an `axis-HC` round would run on, enumerated at
   `HF2-d`.

**What evidence counts.** The targets above, cited; and quotation of the recording round for each
named decision. **Naming a decision is not making it**, and the result note makes none of the five.

## The preregistered predictions, with signs, strengths and recorded reasons

| target | prediction | sign | strength | recorded reason |
| --- | --- | --- | --- | --- |
| `HF0` | all seventeen passages located and quoted at the base | positive | high | each was located by hand while drafting this freeze, in the pinned blobs; the risk is a coordinate a sibling landing moved, not a passage that is absent |
| `HF1-a` | the carrier round H-D's `A5S-1c` names is **still absent** on the bounded search | negative | medium | H-D found none on a narrower base at full attention; the search surface is frozen at this freeze's drafting base, which is later than H-D's and carries no sibling landing of this fan-out, so the re-check is meaningful and closed; medium and not higher because a negative on a sweep is a statement about the sweep |
| `HF1-b` | both settling conditions are quoted, and the record assigns the **negative** one to a derivation at a stated scaling map and convergence topology | positive | high | recorded reading 3; the words are H-D's own and the assignment is carried by them |
| `HF1-c` | the source-level question stands as round H-D named it, and round H-D-SR's freeze scopes the reconciliation without adjudicating | positive | full | recorded readings from the two pinned freezes; both passages are quotations and neither requires a judgment |
| `HF1-d` | round H-B's class question stands open in H-B's own words | positive | full | recorded reading 6, quoted from a merged result note |
| `HF2-a` | the `axis-HC` entry requires the scaling and convergence topology frozen before execution, and Euler and Navier–Stokes reported separately | positive | full | recorded reading 1, quoted from `../PROGRAMME.md` §6 |
| `HF2-b` | **at least four of the five items are unfixed or silent** on the merged record | positive | high | recorded reading 2: round H-A records in terms that none of the five is fixed by the manuscripts or by A1–A6, and round H-B fixes one of them for its own candidate |
| `HF2-c` | **no passage blocks writing the `axis-HC` control plane** on the named and bounded search | negative | medium | no such passage was seen in the pre-freeze reading, and `../PROGRAMME.md` §6 assigns the freezing of the scaling map to that round itself; medium because a negative on a bounded search is a statement about the search, and because the base is later than this freeze's |
| `HF2-d` | both carriers are enumerated with their recorded consequences, and neither is chosen | positive | high | both are exhibited in the merged record with theorems attached; the strength is high and not full because the enumeration of "what the record already says" is where a missed passage is the plausible error |
| `HF3` | every enumerated item's A5 is identifiable from quoted words as `A5-ker` or `A5-ms` | positive | medium | round H-D is careful to say which throughout, but the classification must be carried by each source's own words at the base, and **a row where the source does not say is a live outcome reported as silence** |
| `HF4` | **no target, prediction, gate or status sentence depends on round H-D-SR's outcome** | positive | high | the freeze is written so that no determination is stated in terms of the entailment question's resolution; high and not full because the audit is of this file and a missed sentence is the plausible error, which is exactly what the walk is for |
| `HF5` | **`HF5-H-C`** | **medium** | `HF1` and `HF2` point there: `axis-A5`'s live questions are gated on an absent carrier, on an owner decision, and on a reconciliation this round may not consume, while `axis-HC`'s next step is a control plane `../PROGRAMME.md` §6 assigns to that round and whose required fixings the record leaves to it. **The strength is medium and not higher because `HF5` is what the round exists to decide**, and a freeze that predicted its own adjudication at high strength would be claiming the answer it is chartered to find; `HF5-OWNER` is live and its gate is written so that it is reached rather than forced |
| `HF6` | the five decisions are named and all five left open | positive | full, conditional on `HF0`–`HF5` | each is quoted from the round that recorded it, or raised by this round's own enumeration; this round has no licence to make any of them |

**`UNDECIDED` remains a permitted outcome of every target**, reported with the obstruction named.
**It is a live preregistered outcome and it is not a failure of the round**: a round that reaches
UNDECIDED with its obstruction named has delivered a finding about the record, which is what a type-P
round is for.

**No prediction licenses its own conclusion.** A target that lands against prediction is reported
against prediction, with its evidence, and **the prediction is not amended**.

## The status rule, and the frozen post-round sentence for each outcome

Exactly one sentence per target is written, verbatim, in the result note and nowhere else.

### Frozen sentences for `HF0`

- **LOCATED** — every listed passage is present at the base:
  > The governing passages of this round are located and quoted with their coordinates at the
  > mandated base, and every passage this freeze lists is present there.
- **PARTIAL** — one or more passages are absent or moved:
  > The governing passages are located and quoted with their coordinates at the mandated base, and
  > the passages recorded absent or moved are named here with the bounded search that did not find
  > them; the movement is recorded as a discrepancy and is repaired nowhere.
- **UNDECIDED**:
  > Whether the merged record carries the governing passages this freeze lists is UNDECIDED at the
  > mandated base, with the obstruction named here, and no reading of the record is asserted in
  > their place.

### Frozen sentences for `HF1-a`

- **CARRIER STILL ABSENT**:
  > On the named and bounded search of the Lean tree this note describes, no predicate and no result
  > establishing observer-admission for a concrete substratum stands at the mandated base, so the
  > obstruction round H-D named for its question (a) stands unrelieved. That is a statement about
  > the surface searched and about nothing off it, and it is not a proof that no such carrier can be
  > built.
- **CARRIER LOCATED**:
  > The result quoted with its coordinate here establishes observer-admission for a concrete
  > substratum at the scope its own statement carries. It is cited at that scope and is not restated
  > more broadly; nothing in this round promotes it, and what it would mean for round H-D's question
  > (a) is that round's lane and is not decided here.
- **UNDECIDED**:
  > Whether the tree carries a carrier for observer-admission on a concrete substratum is UNDECIDED
  > at the mandated base, with the obstruction named here.

### Frozen sentences for `HF1-b`

- **BOTH CONDITIONS QUOTED AND ASSIGNED**:
  > Round H-D's two settling conditions for its question (c) are quoted here with their coordinates,
  > and the axis each is assigned to is carried by the quoted words of round H-D's own note. Neither
  > condition is met at the mandated base, and nothing here settles that question in either
  > direction.
- **ASSIGNMENT NOT CARRIED**:
  > Round H-D's two settling conditions are quoted here with their coordinates, and the words of the
  > source do not assign one or both of them to an axis. The finding is that the source does not
  > assign it; this round does not assign it on the source's behalf.
- **UNDECIDED**:
  > Whether round H-D's two settling conditions stand at the mandated base as this freeze records
  > them is UNDECIDED, with the obstruction named here.

### Frozen sentences for `HF1-c`

- **HELD AT ARM'S LENGTH** — the predicted outcome:
  > The source-level question stands at the mandated base as round H-D named it for the owner, and
  > round H-D-SR's freeze scopes the reconciliation, adjudicates nothing and makes no owner
  > decision. **No outcome of that execution is consumed, assumed, anticipated, ranked or preferred
  > by any determination of this round**, and where its result note is present at the base its
  > presence is a fact about the base and not an input.
- **THE RECORD MOVED**:
  > What the mandated base carries for the source-level question differs from what this freeze
  > records, in the respects tabulated here; the difference is recorded as a discrepancy, is
  > repaired nowhere, and **is not read into any determination of this round**.
- **UNDECIDED**:
  > Whether the source-level question stands at the mandated base as this freeze records it is
  > UNDECIDED, with the obstruction named here, and no outcome of round H-D-SR is supplied in its
  > place.

### Frozen sentences for `HF1-d`

- **OPEN, IN ROUND H-B'S WORDS**:
  > Whether the class round H-B's candidate lies in is admissible OI physics stands open at the
  > mandated base in round H-B's own words, quoted here with its coordinate. This round names that
  > question and answers it nowhere.
- **UNDECIDED**:
  > Whether round H-B's open owner question stands at the mandated base as this freeze records it is
  > UNDECIDED, with the obstruction named here.

### Frozen sentences for `HF2-a`

- **QUOTED**:
  > The programme's round `H-C` entry is quoted here in full with its coordinate, and what it
  > requires to be frozen before execution and reported separately afterwards is reported from its
  > own words and from nothing else.
- **MOVED OR ABSENT**:
  > The programme's round `H-C` entry at the mandated base differs from what this freeze records, in
  > the respects tabulated here; the difference is recorded as a discrepancy and is repaired
  > nowhere.

### Frozen sentences for `HF2-b`

- **REPORTED PER ITEM**:
  > The five items of round H-A's scaling skeleton are reported here separately, each recorded fixed
  > with the passage that fixes it, unfixed with the passage that records it unfixed, or silent with
  > the named and bounded search that found no passage. **The table is the finding**, and no single
  > verdict is written in place of it.
- **UNDECIDED**:
  > Whether the merged record fixes the items of round H-A's scaling skeleton is UNDECIDED at the
  > mandated base for the items named here, with the obstruction named beside each.

### Frozen sentences for `HF2-c`

- **NO BLOCKAGE FOUND** — the predicted outcome:
  > On the named and bounded search this note describes, no passage of the merged record states that
  > the round `H-C` control plane cannot be written, and none makes an unfixed item of the scaling
  > skeleton depend on an input the merged record does not carry. **That is a statement about the
  > search, which this note names, and about nothing off it**: it is not a finding that the round is
  > ready, that its work is tractable, or that any limit exists.
- **BLOCKAGE LOCATED**:
  > The passage quoted with its coordinate here states, in its own words, that the round `H-C`
  > control plane cannot be written at the mandated base, or makes a required fixing depend on an
  > input the merged record does not carry. It is recorded as what it says, and this round neither
  > endorses nor applies it.
- **UNDECIDED**:
  > Whether the merged record blocks the writing of the round `H-C` control plane is UNDECIDED, with
  > the obstruction named here.

### Frozen sentences for `HF2-d`

- **ENUMERATED, NEITHER CHOSEN**:
  > The exhibited candidates the merged record carries inside the kernel's substratum interface are
  > enumerated here with what each citing round already says about them, each at that round's own
  > scope and no more broadly. **Neither carrier is chosen, preferred, ranked or recommended**, the
  > choice is named at `HF6` as the owner's, and no recorded consequence of either carrier is a
  > status for `A5-ker` or for `A5-ms`.
- **UNDECIDED**:
  > Whether the merged record carries the exhibited candidates this freeze records is UNDECIDED at
  > the mandated base, with the obstruction named here, and no carrier is chosen in either case.

### Frozen sentences for `HF3`

- **EVERY ROW CARRIED BY QUOTED WORDS**:
  > For every item enumerated in this note, the statement of A5 the source means is recorded as
  > `A5-ker` or as `A5-ms`, carried by that source's own quoted words. **The two statements are
  > reported as two**, no identification between them is built, assumed or needed, and neither is
  > adopted by this round as the statement of A5.
- **ONE OR MORE ROWS SILENT**:
  > For the items tabulated here the source does not say which statement of A5 it means, and **the
  > finding is that it does not say**. This round supplies neither statement in the source's place,
  > builds no identification between them, and adopts neither.
- **UNDECIDED**:
  > Which statement of A5 the enumerated items mean is UNDECIDED for the rows named here, with the
  > obstruction named beside each, and neither statement is supplied in place of the determination.

### Frozen sentences for `HF4`

- **`HF4-independent`** — the predicted outcome:
  > The walk recorded in this note reaches every target, prediction, gate and frozen status sentence
  > of the freeze and finds none whose determination is stated in terms of how the source
  > reconciliation lands. **The sibling results present at the mandated base are recorded as present
  > and are read into no determination.**
- **`HF4-dependent`**:
  > The walk recorded in this note finds that the determinations named here are stated in terms of
  > how the source reconciliation lands. Each is reported **UNDECIDED** with that dependence named as
  > its obstruction, the freeze is not amended, and no outcome of the sibling execution is supplied
  > to rescue any of them.
- **UNDECIDED**:
  > Whether any determination of this round depends on the source reconciliation's outcome is
  > UNDECIDED, with the obstruction named here; no such outcome is consumed in either case.

### Frozen sentences for `HF5`

- **`HF5-H-C`**:
  > On the merged record at the mandated base, and as **this round's adjudication over that record
  > rather than as a theorem**, the programme's next round on the axis round H-B opened is round
  > `H-C`: the items its control plane must freeze are enumerated in this note and are **fixed
  > nowhere here**, and the live questions of the other axis are gated at the base by the items named
  > in this note. **What follows is exactly this and no more**: a round is named as the next one to
  > write. No obligation of the H1–H7 ladder moves, none is closed, no limit is taken, no scaling map
  > is fixed, no carrier is chosen, no status is asserted for `A5-ker` or for `A5-ms`, and nothing
  > here says that round `H-C` will succeed or that a hydrodynamic limit exists.
- **`HF5-A5`**:
  > On the merged record at the mandated base, and as **this round's adjudication over that record
  > rather than as a theorem**, the programme's next round on the axis round H-B opened is a further
  > round on the axis round H-D examined, on the question named in this note, whose enabling
  > condition is met at the base and is quoted here. **The enabling condition is quoted and is not
  > anticipated**: no outcome of the concurrent source reconciliation, no carrier expected to be
  > constructible and no owner decision expected to be taken carries this outcome. No status is
  > asserted for `A5-ker` or for `A5-ms`, and nothing here answers the question that round would ask.
- **`HF5-OWNER`**:
  > On the merged record at the mandated base, the record does not discriminate between the two
  > candidate next rounds on the search this note describes: what each would require is enumerated
  > here, and **which to write is an owner decision this round names and does not make**. That is a
  > finding about the record and not a failure of the round, and nothing here recommends either axis,
  > ranks them, or writes a sentence from which a ranking follows.
- **`HF5-UNDECIDED`**:
  > Which round the merged record supports as the programme's next round on this axis is UNDECIDED,
  > with the obstruction named in this note. Neither axis is named as next, neither is set aside, and
  > no reading of the record is asserted in place of the determination.

### Frozen sentence for `HF6`

- **NAMED, NONE MADE**:
  > The owner decisions this axis carries are assembled in this note — the propagation of the
  > negative resolution, the admissibility of the class round H-B's candidate lies in, the reach of
  > the `R7-HY*` guard family to prose-only rounds, which later action carries out the refresh of
  > the programme's one-line state, which substratum a round `H-C` would run on, and whether that
  > round is commissioned before or after round H-E's result lands — and every one of them is named
  > here and made nowhere.

### Rules binding every outcome

1. **This freeze predicts; it does not establish.** Every outcome above is a determination about the
   merged record or an adjudication labelled as this round's, and no outcome is a theorem, a status,
   or a claim about the world.
2. **The round adopts neither `A5-ker` nor `A5-ms`**, states no preference between them, builds no
   identification between them, and asserts no status for either — in the note, in a table cell, in
   a summary, or in any propagation line.
3. **The round adopts no answer to the entailment question** and no outcome of the concurrent source
   reconciliation, ranks the forms in no order, and resolves no divergence.
4. **The round edits no source.** No manuscript, no book chapter, no programme file, no roadmap, no
   README, no guard, no Lean module, no census, no merged freeze and no merged result note.
5. **Silence is reported as silence**, never as denial and never as assent.
6. **Rounds H-A's, H-B's and H-D's findings are consumed as merged and restated at their own scopes
   and strengths**, never more strongly. **Round H-B's guardrail is carried wherever round H-B is
   mentioned:** *H-B shows that A5 is not needed to obtain a promising reversible fluid candidate
   with the right microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
   Euler/Navier–Stokes limit.*
7. **No taxonomy label is applied** — not to a condition, not to an obligation, not to a carrier, not
   to a source. `HD`, `HC`, `HI` and `HO` appear in this round only as quotations of
   `../PROGRAMME.md` §4.
8. **No label is written "for OI."** Every finding is a statement about a named object: a passage, a
   file, a coordinate, a round, a carrier, a question.
9. **An analysis paragraph is labelled as such** and states that no target rests on it.

## What no outcome licenses — the forbidden sentences, in terms

> **THE A5 ANTI-CONFLATION CLAUSE, carried at this mention — the list of what no outcome licenses.**
> `A5-ker`, the kernel's A5, is additivity of the substratum rule over the alphabet —
> `∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`, at
> `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:102`. `A5-ms`, the manuscripts'
> A5, is linearity of the wave equation, at [Substratum §3.1]. **These are two statements, and no
> identification theorem between them exists in the tree**; `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean:211`) is an instance result for the one rule where both are in
> play and identifies nothing. **This round builds no identification, assumes none, needs none, and
> writes "A5" unqualified nowhere**: every target, prediction, gate, status sentence and hazard here
> that touches A5 says which of `A5-ker` and `A5-ms` it means, and a sentence that says "A5" without
> saying which is a defect of this round.

- **Nothing here answers the entailment question**, and nothing here states, assumes, anticipates,
  ranks or prefers an outcome of the concurrent source reconciliation. The sentences "the question is
  settled", "the question is open", "the negative resolution propagates", "it does not propagate" —
  as this round's own finding rather than as a quotation of a source — are forbidden in terms.
- **Nothing here is a status for `A5-ker` or for `A5-ms`.** Forbidden in terms: "A5 is not a bare-OI
  requirement", "A5 is QM-specific and not required by the hydrodynamic route", "A5 is required by
  the hydrodynamic route", "the linearity condition is derived", "the linearity condition is
  independent", and every paraphrase. Round H-D's status rules 6 and 7 forbid the first two there,
  and they are forbidden here for the same reasons.
- **Nothing here identifies the two statements of A5 or treats one as standing for the other.** A
  finding about the kernel predicate is not a finding about the manuscripts' condition and a finding
  about the manuscripts' condition is not a finding about the kernel predicate, in either direction.
- **Nothing here rules the class round H-B's candidate lies in admissible or inadmissible as OI
  physics.** That is round H-B's open owner question, named at `HF1-d` and `HF6` and answered
  nowhere.
- **Nothing here closes, discharges, moves or relabels an obligation.** H1–H7 keep the statuses the
  merged record gives them; naming what a round `H-C` control plane must fix is not fixing it, and
  enumerating what an axis requires is not supplying it.
- **Nothing here is a continuum statement.** No limit is taken, no PDE is asserted or denied, no
  scaling map is fixed, no convergence topology is chosen, no closure is asserted, no transport
  coefficient is named, and the `S1`–`S5` continuum-breakdown branch stays closed until H4–H7 exist,
  per the programme's control 5.
- **Nothing here says OI yields Navier–Stokes**, that any candidate has a hydrodynamic limit, or that
  any candidate lacks one. The programme's control 2 applies, and its control 8's outcome asymmetry
  applies to every negative this round reports: a bounded search returning nothing establishes Open,
  never Independent.
- **Nothing here says the axis not named as next is closed, blocked or abandoned.** An axis whose
  live questions are gated at the base is gated at the base, and the gate is named; that is not a
  no-go, not an impossibility, and not a judgment that the axis is unpromising.
- **Nothing here commissions a round.** An adjudication names which round the record supports; the
  owner commissions it, and a round `H-C` control plane is a separate artifact written under its own
  freeze.
- **Nothing here consumes round H-E's result**, in either direction, and no finding of this round is
  evidence for or against the candidate bridge condition that round states.
- **Nothing here characterizes the substratum structure sufficient for hydrodynamics.** That is the
  programme's objective; this round delivers an adjudication over the record and nothing more.
- **Nothing here bears on the OI → QM chain, Track B, Track I, Bell or gravity**, in either
  direction — the programme's control 1.
- **Nothing here promotes a cited result.** Every kernel statement cited keeps the evidence level of
  the round that proved it and is restated no more broadly than the theorem carrying it.
- **Nothing here makes an owner decision.** `HF6` names five and makes none.
- **No manuscript is edited and none is read.** Publication-facing claims wait, per the programme's
  control 10.

## Named hazards

> **THE A5 ANTI-CONFLATION CLAUSE, carried at this mention — the hazard list.** `A5-ker`, the
> kernel's A5, is additivity of the substratum rule over the alphabet — `∀ c c' : 𝒮.ι → 𝒮.V,
> 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`, at
> `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:102`. `A5-ms`, the manuscripts'
> A5, is linearity of the wave equation, at [Substratum §3.1]. **These are two statements, and no
> identification theorem between them exists in the tree**; `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean:211`) is an instance result for the one rule where both are in
> play and identifies nothing. **This round builds no identification, assumes none, needs none, and
> writes "A5" unqualified nowhere**: every target, prediction, gate, status sentence and hazard here
> that touches A5 says which of `A5-ker` and `A5-ms` it means, and a sentence that says "A5" without
> saying which is a defect of this round.

1. **Assuming an outcome of round H-D-SR — the round's strongest hazard.** The failure it guards
   against: an execution that finds the sibling's result note sitting at its own mandated base,
   reads it, and lets a determination turn on how the reconciliation landed; or, without reading it
   at all, writes a sentence that presupposes one form of the entailment question prevailed. The
   anti-contamination invariant governs, `HF1-c` holds the question at arm's length by construction,
   `HF4` walks the whole freeze looking for exactly this, and the gate on `HF5-A5` forbids reaching
   that outcome through an anticipated reconciliation in terms.
2. **Conflating the two statements of A5.** The failure: writing "A5" unqualified and letting a
   finding about the kernel predicate carry a sentence about the manuscripts' condition, or the
   reverse; or treating `waveSubstratum_A5` as an identification. THE CLAUSE is carried at every
   prose mention, `HF3` makes the which-A5 question a target with its own evidence rule, and a
   sentence that says "A5" without saying which is a defect of this round.
3. **Confusing round `H-C` with the taxonomy label `HC`.** Two objects under the same two
   characters: `../PROGRAMME.md` §6's round entry and §4's `HC — Conditional` outcome label. They
   are different namespaces, no sentence of this round reads across them, and no outcome of this
   round applies the label to anything.
4. **Confusing this round's `HF` target prefix with the programme's `S1`–`S5` branch, or the round
   label `H-F` with an ordinal of the H1–H7 ladder, or with a taxonomy value.** Three namespaces
   and no sentence reads across them.
5. **Reading a gated axis as a no-go.** The failure: reporting "the other axis's live questions are
   gated at the base" as "that axis is closed", "that line of work is refuted", or "the programme
   has ruled it out". The programme's control 8 applies: failure to find an enabling condition
   establishes Open, never Independent.
6. **Treating an adjudication as a theorem, or as a commission.** `HF5` is this round's reading of
   the merged record, labelled as such wherever it appears. It proves nothing, it moves no
   obligation, and it does not itself commission the round it names — the owner does that, under a
   separate freeze.
7. **Reconstructive inference presented as a finding.** The failure: a reader who knows the
   programme supplying the bridging sentence the record does not carry — "the record must intend
   H-C next, because otherwise the ladder stalls". The evidence rule forbids it as evidence, and the
   final report states which quotation carries each determination.
8. **Treating silence as an answer.** The failure: reading a source that names a condition without
   saying which statement of it is meant as evidence that it means one of them; or reading a record
   that does not block the writing of a control plane as a record that endorses it. Every silence is
   reported as silence and every negative names its surface.
9. **Converting a bounded search into a universal claim.** The failure: writing "no carrier exists"
   where the evidence is "no carrier was found on this named surface", or "nothing blocks round
   `H-C`" where the evidence is a bounded search. Every negative is reported with its surface named
   and is not a claim about what lies off it.
10. **Making an owner decision by describing it.** The failure: `HF6` naming the carrier question and
    then recommending a carrier, or writing a sentence from which a recommendation follows. Naming
    is not making, and `HF2-d`'s restriction says so in terms.
11. **Restating round H-D's answers, or round H-B's guardrail, more strongly than their own rounds
    state them.** The failure: compressing "no derivation was found on the record searched" into the
    stronger sentence round H-D's status rule 7 reserves to two grounds, or compressing round H-B's
    guardrail into its second half. Both are carried in their own words wherever they are cited.
12. **Consuming round H-E's result.** The failure: an execution that finds the sibling's Lean module
    and result note at its base and lets a determination turn on whether the candidate bridge
    condition held. Round H-E's freeze is read for its scope and shape; its result is not an input,
    and the anti-contamination invariant governs.
13. **Building a Lean statement to settle a target.** The definition budget is zero. Where a target
    cannot be settled without a kernel statement — `HF1-a`'s carrier is the live case — the frozen
    response is to record that target's outcome with the obstruction named, **not** to write the
    statement under this freeze.
14. **Naming a new condition, or renumbering a list.** The round adds nothing to any list of
    conditions, renumbers nothing, and names no further condition of the framework.
15. **Speaking about singularities.** The `S1`–`S5` branch stays closed until a continuum map exists,
    per the programme's control 5.

## Definition budget

**Zero.** The execution introduces **no** top-level definition, adds **no** Lean module, and edits
**no** existing one. It cites kernel results and re-proves none. In particular it does **not**
construct an identification between the two statements of A5, does **not** define a predicate for
observer-admission or for anything else, and does **not** supply the carrier `HF1-a` searches for.

**No proof placeholder, no postulated statement and no decision-procedure escape hatch appears
anywhere in this round**, for the plain reason that no Lean is written at all; the result note states
this rather than leaving it to be inferred, and carries no printed-dependency line and no
kernel-dependency table.

**A single definition requires its own append-only amendment**, separately frozen and merged before
the work it affects, naming the definition and the target it serves. **Such an amendment would make
the round sealing**, since a new Lean module brings a guard section and its own seal constants; the
amendment would have to say so and restate the landing shape, and this freeze's non-sealing
declaration would stand as the record of what was frozen first.

## The chronology control — checkable mechanically

1. **This preregistration is merged alone**, before any execution-specific `H-F` object enters the
   repository tree. *Check:* the control-plane pull request's diff contains exactly one added file,
   this one. The single permitted exception is the recorded readings inside this control-plane blob
   itself, merged *as* the freeze; they are evidence at no level and the execution re-reads each at
   the base.
2. **This control plane's branch is cut from exactly `b78eac870ba3ee9ef9e98659ac933bf97dc62226`**,
   the certified `main` whose blobs the start-state table pins, and from nothing else; it absorbs no
   later `main` before merging. *Check:* the branch's merge-base with `main` is that commit and its
   first-parent chain reaches it without an intervening merge.
3. **Rounds H-A, H-B and H-D must have merged before this execution begins.** *Check:* round H-A's
   sealed head `6a8675efca5e5ceeab0195036af1a658b49ace80` and round H-B's sealed head
   `54b33c4304bdbda52a09dfe0a06f3e7ff350d832` are ancestors of the mandated base, and round H-D's
   preregistration and result note are both present there
   (`git merge-base --is-ancestor <sealed head> <base>` for each of the two).
4. **Nothing else is required to have merged, and nothing else is required to be absent.** In
   particular **no artifact of round H-D-SR's execution and no artifact of round H-E's execution is
   required to be present or absent at the base**, and the presence of either licenses nothing: the
   anti-contamination invariant governs.
5. **The mandated execution base is exactly the merge commit of this control plane's pull request.**
   The execution branches from that commit and from nothing else. *Check:* the execution branch's
   merge-base with `main` is that commit, and its first-parent chain reaches it without an
   intervening merge from later `main`.
6. **The execution's first act is to verify this file's blob at that base**, before any target is
   executed. *Check:* the result note records the blob and it equals this file's `git hash-object`
   value at the control plane's merge.
7. **The result note pins this file by content** and records the base it executed on. *Check:* both
   values appear in the result note's start-state table.
8. **No new guard file is added by this round, and no existing guard is modified.** *Check:* the
   execution's diff touches no file under `verification/lean/`, no `.lean` file, and no seal
   constant of the `R7-HY*` family.
9. **Before certification the execution never absorbs later main.** No merge from main, no rebase, no
   amend, no force-push. *Check:* the execution head's ancestry contains no merge whose second parent
   postdates the base.
10. **Under `§A.37` the landing is `E` → `L` with no archive pin**, the round being non-sealing.
    *Check:* the landing merge's second parent equals the execution head `E`, and no pin commit
    follows it.
11. **The claim is scoped to the repository record** at the execution base.

## Evidence level

**Type P throughout.** No target is at evidence level 2 and none is a kernel target. The kernel
statements cited at `HF1-a`, `HF2-d` and inside THE CLAUSE carry their own evidence level from the
rounds that proved them, and **citing them here promotes nothing**: each is reported at its own scope
and is not restated more broadly than the theorem carrying it. The result note says in terms that the
round is type P, and that neither a kernel-dependency table nor a printed-dependency line appears,
rather than leaving the absence to be inferred.

## Immutable inputs

Consumed as merged and unrevised: round H-A's `H0`–`H4a` findings, their labels and the five-item
scaling skeleton; round H-B's candidate, its A-profile, its conservation and stencil results, its
labels, its guardrail and its open owner question; round H-D's targets `A5S-0a`–`A5S-5b`, its three
answers, its two disqualification rules, its status rules, its discrepancies and its chronology
certification; round H-D-SR's freeze, as a statement of that round's own scope and shape and as
nothing else; round H-E's freeze, on the same terms; `../PROGRAMME.md` §1, §3, §4, §6, §7 and §8;
`verification/ROADMAP.md`'s two hydrodynamics sections; the `Substratum` interface as the kernel
states it; `AGENTS.md` `§A.37` and `§A.36`.

## Non-doings

The round does not: read or edit any manuscript or book chapter; edit any programme file, roadmap,
README, guard, Lean module, census, merged freeze or merged result note; write or edit any Lean;
re-prove any cited result; construct an identification between the two statements of A5; define any
predicate; adopt either statement of A5 or assert any status for either; answer the entailment
question or adopt, rank or prefer either form of it; consume, assume, anticipate or state an outcome
of round H-D-SR's execution or of round H-E's execution; reopen rounds H-A, H-B or H-D, or re-decide
any of round H-D's three answers; choose a carrier; fix a scaling map, a convergence topology, a
normalization or a norm; take any limit or assert any PDE, closure or transport coefficient; move,
close, discharge or relabel any obligation; apply any taxonomy label; assert any status for A6; carry
out any propagation or refresh any one-line state; commission any round; make any of the five owner
decisions it names; say anything about Track B, Track I, Bell, gravity or singularities.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once merged, this file is **immutable**. An execution that diverges from it **records the
  discrepancy** and does not repair the freeze. Execution-affecting corrections are append-only
  amendments, separately frozen and merged before the work they affect.
- **This pull request carries this file alone.**
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying **the
  result note alone**. No Lean, no guard, no manuscript change, no propagation, no roadmap section.
- Exact-head certification after execution is complete, with full continuous integration green; the
  certification of record is the run whose `head_sha` is the execution commit `E`. A red badge
  arising solely from an archive clause that entered `main` after the base is not a research failure;
  `§A.37`'s exact-head rule applies, and `workflow_dispatch` on the branch is the fallback for that
  case and not the routine.
- **Then the landing on the same pull request:** `L` alone, no pin, the round being non-sealing.
  Conflicts are resolved in `L`, by merits and never by side, and never in `E`.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. `HF0`, the seventeen governing passages located and quoted with coordinates;
2. `HF1-a`–`HF1-d`, the `axis-A5` enumeration, each item with its quotation, its gate and the
   bounded search where one was run;
3. `HF2-a`–`HF2-d`, the `axis-HC` enumeration, the five scaling items reported separately, the
   blockage determination with its search named and bounded, and the carrier enumeration with
   neither carrier chosen;
4. `HF3`, the which-A5 table, one row per enumerated item, each classification carried by quoted
   words and every silence reported as silence;
5. `HF4`, the independence walk, with the presence of the sibling results at the base recorded and
   read into nothing;
6. `HF5`, the adjudication, with each gate requirement reported satisfied or unmet, and the single
   frozen sentence for the outcome reached;
7. `HF6`, the five owner decisions named and made nowhere;
8. what the outcomes do **not** license, in this file's wording, round H-B's guardrail and THE CLAUSE
   among them;
9. the discrepancy section — every divergence between this freeze and what the execution finds at
   the base, recorded and repaired nowhere;
10. the definition budget, recorded as zero, with the statement that no Lean is written and that no
    kernel-dependency table exists;
11. the chronology certification, clause by clause, including this file's blob by content, the
    execution base, the record that no guard was added or modified, and the round's shape recorded as
    non-sealing with `E` → `L` and no pin.

Nothing else.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **The round is scoped to a decision between the two axes, not to either axis's work.** The
   alternative was to write the `axis-HC` control plane directly. This freeze does not, because
   `../PROGRAMME.md` §6 assigns the freezing of the scaling map and the convergence topology to that
   round's own control plane, and writing it here would both pre-empt that freeze and settle the
   carrier question this round is chartered to enumerate. The choice is recorded here and `HF5`'s
   `HF5-OWNER` outcome is where it is put at risk.
2. **No manuscript is read, and `A5-ms` is quoted from round H-D's merged result note.** The
   alternative was to quote it from its own home in `papers/`. This freeze does not, because the
   concurrent source reconciliation is sweeping exactly that corpus, and a mechanically auditable
   boundary — `papers/` and `book/` absent from the start-state table entirely — is a stronger
   guarantee against entering that lane than a rule about which sentences may be read. The cost is
   that `A5-ms` is carried at one remove, and the execution says so in terms.
3. **`HF5` is an adjudication the round reaches, not an owner decision it names.** The alternative
   was to enumerate both axes and leave the choice entirely to the owner. This freeze reaches a
   determination because the programme's rounds are chosen from the record and the record is what a
   type-P round can read; but the determination is labelled as this round's adjudication wherever it
   appears, `HF5-OWNER` is a live outcome with its own frozen sentence, and commissioning stays the
   owner's act either way.
4. **The round is non-sealing.** An alternative would add a guard pinning the quoted coordinates.
   This freeze does not, because the definition budget is zero and there is no kernel object to
   order; the blob pins in the start-state table carry the immutability the round needs, and whether
   the `R7-HY*` family should reach prose-only rounds is one of the owner decisions `HF6` names and
   does not make.
5. **`HF1-a` re-runs a search round H-D already ran, on a surface frozen at this freeze's drafting
   base.** The alternative was to consume round H-D's finding and stop. This freeze re-runs it
   because that base is later than H-D's and because the whole weight of the `axis-A5` gate rests on
   that carrier's absence — a gate that rests on a stale search is not a gate. The surface is fixed
   at the drafting base rather than at the execution base so that the sweep cannot reach a sibling
   round of this fan-out, whose results this freeze excludes from its evidence in terms.
6. **`HF2-d` enumerates the carrier question rather than deciding it.** The alternative was to fold
   the carrier into the adjudication, so that `HF5-H-C` named both the round and the substratum it
   would run on. This freeze separates them, because the carrier choice carries recorded consequences
   about `A5-ker` for one candidate and about the linearity gate for the other, and a round that
   decided it would be taking a position on the axis it is chartered to compare.

## Settled by the owner before this freeze merges

Recorded so that the settlement happens before the merge, which is the only time a freeze may be
amended. Each item below is settled, and the freeze carries it.

1. **The round's question is the choice between the two named candidates**, and no third candidate
   enters. A round continuing round H-E's closure work is not enabled while the scaling and
   convergence structure it would need stands unfixed; the three-dimensional construction and the
   observer-admission carrier are likewise not presently enabled. **This is an owner scope judgement
   and nothing more**: no outcome of round H-E is evidence inside this round, and none is consulted
   by any target here.
2. **`HF5` reaches an adjudication, with `HF5-OWNER` live.** The alternative — enumerating both axes
   and leaving the comparison to be made informally — is a smaller round that leaves the record
   without a written determination. The gates stay strict: `HF5-H-C` requires both a writable `H-C`
   control plane and an `axis-A5` enabling condition actually unmet.
3. **`papers/` stays excluded**, and `A5-ms` continues to be carried at one remove through round
   H-D's merged quotation. The source surface is swept by the concurrent source-reconciliation round;
   reopening it here would duplicate that lane and weaken the mechanical blindness boundary.
4. **`HF2-d` stays**, enumerating the two exhibited carrier candidates and their recorded properties.
   Enumeration is input to comparing the axes; **choosing** the carrier remains the later `axis-HC`
   control plane's act, and the wording keeps enumeration and adoption apart.
5. **`HF1-a`'s sweep surface is the `OIBridge` modules, frozen at this freeze's certified drafting
   base** `b78eac870ba3ee9ef9e98659ac933bf97dc62226` — not the whole Lean tree, and not the
   execution base. That base is later than round H-D's own enumeration base, so the re-check is
   meaningful; and it precedes every sibling landing of this fan-out, so no sibling round's Lean can
   enter the sweep. Fixing it at the execution base would have let the search reach results this
   freeze excludes from its evidence in terms.
6. **`HF6` names five decisions, not six.** The five are the propagation question, the admissibility
   of round H-B's class, the reach of the `R7-HY*` guard family to prose-only rounds, the actor for
   the `../PROGRAMME.md` §8 refresh, and the `carrier-question`. Whether an `axis-HC` control plane
   is commissioned before or after round H-E's result lands is **not** among them: this round's own
   preconditions put that landing before this execution, so the question does not stand open at the
   time the note is written.
7. **The execution produces the result note alone**, with no `ROADMAP` and no `README` pointer. For a
   zero-Lean, non-sealing adjudication that is the cleaner provenance object; pointer propagation is
   a separately owned action and not this round's to absorb.
8. **The completed sibling outcomes do not change this round's charter.** The source-reconciliation
   and closure-bridge rounds were both considered, before this freeze merged, for whether either
   would change which axis the programme compares next. The answer recorded here is that neither
   does. **Their contents remain excluded from this round's evidence**: no target, prediction, gate
   or frozen sentence consults them, and an execution that finds the record moved records the
   discrepancy and does not repair it.
