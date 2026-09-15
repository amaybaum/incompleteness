# Physical realization — the C4 preparation-scope cleanup: a publication-record repair. CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no Lean, no probe, no guard block, no
`ROADMAP` edit, no README edit, no census edit, no manuscript edit and no outcome label. It does
carry, deliberately, the located coordinates, the frozen targets with their predictions and signs,
the frozen post-round sentences for every outcome, and the frozen character-for-character manuscript
sentences the execution would insert — recording them before merge is what makes them auditable
rather than retrospective. It is merged **alone**, before any execution object of this round exists,
and the execution branches from exactly the commit that merges it. **Blob identity is
authoritative.**

**This round is a publication-record repair, not new mathematics.** It proves nothing, formalizes
nothing, and adds no predicate to the kernel. It determines what the merged record already says
about the data the C1–C4 verdicts are a function of, determines what the manuscripts say about the
same question, and — if the manuscripts are found short of the record — inserts the frozen sentences
below. Every mathematical fact it uses is consumed as merged from a round that proved it.

## The round's shape, declared under `AGENTS.md` §A.37

**This is a NON-SEALING round.** Its landing shape is `E` → `L`, with **no pin commit `P`**.

§A.37 fixes the split on what a round's preregistration **prospectively owns**: a sealing round
either creates new seal and pin state or explicitly takes ownership of changing existing seal state,
and lands `E` → `L` → `P` with `P` mandatory; a non-sealing round owns no seal state, **may** modify
other contracts inside an existing guard, **may not** alter existing seal constants, and lands
`E` → `L` with no archive pin, because it has nothing to pin and a pin commit added there would pin
nothing.

**The seal constants this round would own.** None of the archive triple. The execution adds one new
guard tag, `R7-PC4P` — a tag absent from `verification/lean/edge_rigidity_probe.py` at the
start-state blob — carrying exactly two kinds of state:

| constant or contract | what it holds | when it is set |
| --- | --- | --- |
| `_PC4P_BASE` | the merge commit of **this** control-plane pull request — the mandated execution base, as a literal | in the execution commit `E` |
| the blob pin of this file | `git hash-object` of this path compared against a literal, with a drift control that fails the guard if one byte is appended | in the execution commit `E` |
| the manuscript content contracts | the inserted sentences of `PS3` checked present at their coordinates, each with its mutation control | in the execution commit `E` |

**No constant named `_PC4P_SEALED_HEAD` and no constant named `_PC4P_MERGE` is created by this
round**, so `R7-PC4P` has no archive mode, there is no sealed head to pin, and `P` does not exist.
A `_BASE` literal is the mandated-base record, not a seal of a head and not a pin of a merge; the
merged record already carries guards of exactly this shape — `_RBR_BASE`, `_ABR_BASE`, `_CLG_BASE`
and `_TSG_BASE` each stand without a `_SEALED_HEAD` or a `_MERGE` — and `R7-AUDB`, the manuscript
guard nearest this round's subject matter, carries content contracts and no base literal at all.

**The seal constants this round would NOT own, stated in terms.** `_PC4_BASE`, `_PC4_SEALED_HEAD`
and `_PC4_MERGE` belong to *Physical C4 discharge, round 1*, which set them. `_PC4S_BASE`,
`_PC4S_SEALED_HEAD` and `_PC4S_MERGE` belong to *Physical C4, round 2 — the storage-time reading of
the store clause*, which set them. This freeze does not take ownership of either triple and **the
execution may not write, move, unset or re-pin any of the six**. The same holds for every other
`_*_BASE`, `_*_SEALED_HEAD` and `_*_MERGE` in `edge_rigidity_probe.py`: an archive seal belongs to
the round that set it and stays immutable afterwards, and a later round does not acquire a pin
commit merely by touching the file that carries it.

**The one existing guard this round may touch, and the rule governing it.** `R7-AUDB` carries
manuscript content contracts over `[GR]` §2.2 and both book sources. §A.37 permits a non-sealing
round to modify other contracts inside an existing guard. The prediction of this freeze is that no
`R7-AUDB` contract is touched, because every `PS3` insertion is an append at a coordinate `R7-AUDB`
does not pin. **The execution leaves `R7-AUDB` green.** If and only if one of the frozen insertions
moves a string `R7-AUDB` pins, the execution updates that contract, states the change in the result
note under its own heading, and records it as a discrepancy against this prediction; it does not
weaken or delete a contract, and it does not touch `R7-AUDB`'s mutation controls.

**Recorded for the owner, not decided here.** If the owner directs that the inserted manuscript
wording be archive-sealed rather than content-pinned, this freeze must be **amended to a sealing
shape before execution**, naming `_PC4P_SEALED_HEAD` and `_PC4P_MERGE` and the `E` → `L` → `P`
landing. That is an amendment, merged before the work it affects; it is not a discrepancy the
execution may record its way past.

## The anti-conflation clause, FROZEN VERBATIM

Two C4 rounds have landed. Round 1 put the manuscripts' realization clause in the kernel as
`RoutedReadback`. Round 2 established that the seed-conditioned reading and the storage-time reading
of the store clause are **incomparable as predicates**. The consequence for a round that writes
about what C1–C4 depend on is immediate and is frozen here: *"the C4 reading"* does not name one
thing — and because that is exactly the phrasing a publication-record repair reaches for, the clause
below is **THE CLAUSE**, and it is carried as a block quote **at every prose mention** of what
C1–C4 depend on, in this file and in every artifact of this round.

**How each carriage is written, and why.** Each carriage opens with one line, inside the quote,
naming where it is being carried, and then states the clause word for word. The naming line is there
so that the carriages read as distinguishable copies of one clause rather than as one paragraph
pasted repeatedly — a defect `tools/duplicate_check.py` exists to catch, and which it catches at 200
characters on whole `\n\n`-separated paragraphs — and it changes nothing about the clause it
introduces.

**Three kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the **frozen manuscript
sentences** of `PS3`, which are manuscript voice and cannot carry a repository clause inside them,
and which instead carry the indexing in their own frozen words; the **byte-fixed post-round
sentences** of the status rule, which cannot admit a quotation inside a quotation; and the bare
table rows and list entries that do nothing but name a predicate among those this round does not
touch.

**THE CLAUSE:**

> **THE CLAUSE — the C4 reading index.** *"The C4 reading"* does not name one predicate. The merged
> record carries at least four distinct C4-level objects: the manuscripts' operational history-level
> condition, whose discovery-round form is `C4w`; the marginal signatures `C4e` and `C4r`, with
> `PDivisible` and `PIndivisibleWithin`; `RoutedReadback`, the seed-conditioned reading of the store
> clause; and `RoutedReadbackAtStorage`, the storage-time reading. The last two are **incomparable as
> predicates** — neither implies the other, neither is stronger than the other, and neither is the
> correct reading of C4. **Therefore every statement this round writes about what C1–C4 depend on
> names the predicate it is about.** The prior-dependence half of the backlog item is a statement
> about **P-divisibility**; the visible-root half is a statement about **`C4w`**; neither is a
> statement about `RoutedReadback` and neither is a statement about `RoutedReadbackAtStorage`, and
> no statement about either routed reading is derived from either half. An unindexed sentence of the
> form *"C4 depends on preparation"* is a **defect of this round**, whatever its sign.

## Locating controls: the governing passages at the base, quoted with coordinates

Every passage below is quoted verbatim from a blob pinned in the start state. The coordinates are
the coordinates at those blobs. Nothing here is a finding of this round; these are the passages that
assign the task and bound it.

### `L1` — the backlog item, at its three record coordinates

**The prior-dependence half.** `verification/programmes/oi-qm/track-i/causal-readback-discovery/preregistration.md`,
line 215, stated as the required theorem-level conclusion of the prior-dependence control:

> P-divisibility is not a property of `(φ, partition)` alone; the fixed preparation prior `μ_H` can
> change the verdict.

with its control at the same round's `amendments/amendment-1.md`, line 76:

> 4. Prior-dependence pair `φ(x,h) = (x XOR h, h)` under uniform versus `δ₀`: proves the divisibility
>    verdict is not a property of `(φ, partition)` alone.

**The visible-root half.** The same round's `amendments/result-amendment-1.md`, line 46:

> A parent-positive rooted realization does **not** force C4w under every standalone visible initial
> preparation. C4w is preparation-support sensitive even when the rooted transition family and hidden
> prior are held fixed.

with the sentence immediately following it, line 48, which fixes what varies:

> This is distinct from the hidden-prior dependence already recorded in the round. Here `mu_H` and the
> entire rooted family are unchanged; only the standalone visible root law `p_0` changes.

### `L2` — the assignment of this task, quoted verbatim

`verification/programmes/oi-qm/track-i/recurrence-tightness/result.md`, line 200, the second of the
two directions in which that round's *Publication boundary* sharpens the publication backlog:

> the already-identified preparation-scope issue for manuscript C4 remains separate and should be
> repaired in its own publication-record task.

**This round is that task.** The record assigns it; this freeze does not invent it. The same
sentence is quoted again at `round-c4-2-storage-readback/preregistration.md` line 152 and at that
round's `result.md` line 119, in both cases as the reason that round does **not** act on the item.

### `L3` — what the two C4 rounds settled, and the constraint it puts on this round's prose

`round-c4-2-storage-readback/result.md`, the one-line outcome at lines 45–52, in the clause that
governs here:

> **the two readings are incomparable as predicates**, by two exhibited carriers with exact
> certificates (`CS5`)

and, from the same note's *What these outcomes do NOT license*:

> **No claim that `RoutedReadbackAtStorage` is the correct reading of C4.** The round determines what
> the record says and what each predicate carries on each carrier. Which reading the manuscripts
> intend is the question `CS0-d` asked of them, and they are silent.

> **THE CLAUSE, carried at this mention — the locating control that establishes the incomparability.**
> *"The C4 reading"* does not name one predicate. The merged record carries at least four distinct
> C4-level objects: the manuscripts' operational history-level condition, whose discovery-round form
> is `C4w`; the marginal signatures `C4e` and `C4r`, with `PDivisible` and `PIndivisibleWithin`;
> `RoutedReadback`, the seed-conditioned reading of the store clause; and `RoutedReadbackAtStorage`,
> the storage-time reading. The last two are **incomparable as predicates** — neither implies the
> other, neither is stronger than the other, and neither is the correct reading of C4. **Therefore
> every statement this round writes about what C1–C4 depend on names the predicate it is about.** The
> prior-dependence half of the backlog item is a statement about **P-divisibility**; the visible-root
> half is a statement about **`C4w`**; neither is a statement about `RoutedReadback` and neither is a
> statement about `RoutedReadbackAtStorage`, and no statement about either routed reading is derived
> from either half. An unindexed sentence of the form *"C4 depends on preparation"* is a **defect of
> this round**, whatever its sign.

### `L4` — what the manuscripts already carry, at the base

`papers/Main.md`, §1.2, line 60, *Remark (the measure as a realization datum)*, in the clause that
bears on the prior-dependence half:

> It does not preclude structured preparations: a realization in the sense of §3.4 carries its own
> fixed hidden prior $\mu_H$ as part of the realization datum, and the emergent law is a function of
> $(\varphi, \text{partition}, \mu_H)$ — the same bijection and partition under different priors
> generally yield different visible laws (trivially: the two-state swap under uniform versus
> point-mass hidden priors).

`papers/Main.md`, §1.3, line 72, the *Companions and independence* paragraph, in the clause that
names what the conditions are checked of:

> They are stated and used because they are what one can check of a candidate partition — a
> cosmological horizon, a laboratory apparatus, an equilibrium fluctuation — where the bare existence
> claim cannot be checked directly.

`papers/Main.md`, §1.3, line 80, the **(C4)** entry, in the clause whose verdict the visible-root
half bears on:

> at some order, two visible histories with the same current state induce different next-step laws,
> mediated through the hidden state

**These passages are locating controls and not findings.** Whether `[Main]` §1.2 line 60 discharges
the prior-dependence half at the level the backlog item asks about — the level of the **verdicts of
the conditions**, rather than the level of the **emergent law** — is target `PS2`, and it is
permitted to return against this freeze's prediction.

### `L5` — the residues and the record-level errors, located and quoted

`round-c4-1-physical-discharge/result.md`, the `RS` table, the two entries classed **(b)**:

> | **`[GR]` §8.1 line 561** | **(b)** | **residue, confirmed verbatim**: "the horizon complement is such a system, and its coupling reads the boundary degrees it writes, which is (C4)'s realization — so the equivalence applies in our universe" |

> | **`book/ch01` §1.10 line 257** | **(b)** | **residue, confirmed verbatim**: "not blind to our own past records (C4 holds)", with "the gravitational coupling enforcing C1, the cosmological timescale enforcing C2, the cosmological horizon enforcing C3" and **nothing named for C4** |

> | `book/The-Incompleteness-of-Observation-FULL.md` line 601 | **(b)** | **the parallel source carries the same sentence, character for character**; the residue is present in both book sources, not one |

and that round's own disposition of them, from the paragraph immediately below the table:

> **Both residues are recorded and left for a separate owner call.**

The three record-level errors in round 1's immutable freeze, from the same note's *Discrepancies
between the preregistration and the execution, recorded and NOT repaired*, items 2 and 5:

> 2. **`partIdx` and `partIdx_fst` are located in `OIBridge/OIRealization.lean`, not in
>    `OIBridge/IndependenceCensus.lean`** as the freeze's start-state table states. Both blobs are the
>    blobs the freeze pins and neither moved; the attribution is the error, and the objects consumed
>    are the ones named.

> 5. **Two line attributions in the freeze's RS table are approximate.** The sentence "The theorem does
>    not identify which physical systems satisfy the conditions; this is an empirical question",
>    attributed to `[Main]` §4.2 line 678, sits in `[GR]` §8.1 line 561's continuation at the pinned
>    blobs; `[Main]` line 678 states the equivalence under (C1)–(C4) and is classified (a) on what it
>    actually says. The classification at both coordinates is the freeze's.

## The scope decision on the residues and the record-level errors, SETTLED HERE

Leaving this ambiguous is the failure mode, so it is settled in terms, in both directions, before
any target is written.

**The two inference residues are OUT OF SCOPE for repair, and IN SCOPE for one bounded
non-action.** `[GR]` §8.1 line 561 and `book/ch01` §1.10 line 257 with its FULL mirror at line 601
are *inference-to-C4-at-a-physical-cut* residues: sentences that infer C4's realization holds in our
universe. That is a different defect from preparation scope. Preparation scope is a question about
**which data a verdict is a function of**; a residue is a question about **whether a verdict has been
reached at a cut**. Repairing a residue is a claim change about the cosmological cut and needs the
owner call round 1's result note reserves for it; folding it into a scope repair would let a
publication-record cleanup decide a discharge question by side effect. **The bounded non-action that
is in scope:** target `PS5` requires the execution to verify all three residue coordinates
byte-identical at the base and byte-identical on the head, and to record that verification, so that
whichever round takes the owner call finds them exactly as round 1 left them. Verifying is not
repairing, and `PS5` returns no verdict on the residues.

**Round 1's three record-level errors are OUT OF SCOPE for repair, and IN SCOPE for propagation.**
The `partIdx` location misattribution and the two approximate `RS` line attributions are errors
inside round 1's **merged preregistration**, which §A.37 makes immutable: *"once merged the
preregistration is immutable, and an execution that diverges from it records the discrepancy rather
than repairing the freeze."* They are already recorded, correctly and at the proper place, as items
2 and 5 of round 1's result-note discrepancies. Re-recording them in a third artifact would
duplicate the record without correcting anything, and editing round 1's freeze is forbidden. **The
propagation that is in scope:** this round's own start-state table locates `partIdx` and
`partIdx_fst` in `OIBridge/OIRealization.lean`, which is where they are; and every coordinate this
round quotes from `[GR]` §8.1 and `[Main]` §4.2 is taken from round 1's **corrected** attribution in
discrepancy 5, never from its freeze's table. An execution that re-imports an attribution round 1's
result note already corrected is a defect of this round.

**Neither decision is reopened by an outcome.** Whatever `PS0`–`PS4` return, the residues are not
repaired here and round 1's freeze is not edited here.

## Start state

Pinned **by blob**, read at `b78eac870ba3ee9ef9e98659ac933bf97dc62226`, the commit this control
plane is written against and the first parent of its merge. Blob identity is authoritative: the
commit locates the tree, the blob is what is compared. The execution compares each blob at its
**mandated base** — the merge commit of this control plane, which may carry sibling rounds merged in
between — and records every difference it finds.

### Table A — read and never written

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/preregistration.md` | `1d649101fa5013d1f484711e8d7deaab188424f8` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/result.md` | `9dfc5a4785045c69f8daccff69168159a3c7ec6f` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/amendments/amendment-1.md` | `69b68f82f60eb6f3717b8f6be91a4423b4d06bba` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/amendments/result-amendment-1.md` | `f748b16cdf52f21f2d7a2d52deaf5ee5ecddc638` |
| `verification/programmes/oi-qm/track-i/recurrence-tightness/result.md` | `3afddf47c72bf70415876f4b729c3ed47ccb6163` |
| `verification/programmes/physical-realization/round-c4-1-physical-discharge/preregistration.md` | `a80334a5d5f19125b69459523acf723b607f97e1` |
| `verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md` | `64a610859e834663cf1d5cc73d0ab9a2ab9dd882` |
| `verification/programmes/physical-realization/round-c4-2-storage-readback/preregistration.md` | `16cfd1303e7c279c8d6bab68b7112c3f25a7460e` |
| `verification/programmes/physical-realization/round-c4-2-storage-readback/result.md` | `db94942843bd806df3c5e6ba80b77b9445488d4e` |
| `verification/audits/physical-realization/c4-causal-readback/preregistration.md` | `62204a099b81841e2eb5c71e460a676b0d0960e9` |
| `verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean` | `832eeac3ee5f8df770b478b272842729183c7e48` |
| `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean` | `8bdf3c77acf51f074c4f05dc440e3511137cdf9c` |
| `verification/lean-mathlib/OIBridge/CausalReadback.lean` | `d7b71cf56aaddb24724653caa0d96b525134f95e` |
| `verification/lean-mathlib/OIBridge/IndependenceCensus.lean` | `b31f8ea03736af2b3dfedd316ecd85ae363e1d27` |
| `verification/lean-mathlib/OIBridge/OIRealization.lean` | `4df632b73d3cfefc5923958a802319a552150afc` |
| `papers/GR.md` | `0258ccb7a5ef02877a01638428ae7ab8ba91bf71` |
| `papers/SM.md` | `26d6cbfb230c105eb00a979c2b69c363568455dd` |
| `papers/Substratum.md` | `9ac6b732e8786897cade416b67c3f7f1df81ab84` |
| `book/ch07-gravity.md` | `344509fd16cf950cfe0aecd51cf357496be48b76` |
| `build.sh` | `cd612dee7c9eac6d0b4aad29d3ca820460d5bb8d` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

`OIBridge/IndependenceCensus.lean` and `OIBridge/OIRealization.lean` are pinned together and named
together for the reason given in the scope decision: the sealed core's `Core`, `vis`, `swapFn`,
`histTriple`, `core_history_readback`, `CoreC1C4` and `core_isC1C4` are in the first; **`partIdx`
and `partIdx_fst` are in the second**, which is where round 1's result note locates them.

### Table B — read for anchors and written by the execution

Each of these is pinned by blob for the same reason Table A is: the frozen anchor strings of `PS3`
must be found byte-identical before anything is inserted. The rule differs — these are **written** —
and it is stated separately below the table so that Table A's clause is not read as covering them.

| path | blob | what the execution writes |
| --- | --- | --- |
| `papers/Main.md` | `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` | the two `PS3` insertions, at §1.3 lines 72 and 80 |
| `book/ch01-observation.md` | `355d1c58dc09c4b6128fde2de55475aa673e4315` | the `PS3` insertion at §1.3 line 61 |
| `book/glossary.md` | `e811a2cc00b39d03b1a7adf263e31e63d4bcf957` | the `PS3` insertion at the **C4** entry, line 31 |
| `book/The-Incompleteness-of-Observation-FULL.md` | `9674614cbb55b58b7492f1e4b65a4f09e82e91b5` | the two mirrored lines, at 405 and 6593 |
| `papers/Main.tex` | `3e8637f03c91f2c5c7ffdb0beb4a661d90594a60` | regenerated by `./build.sh Main`, stamp included |
| `book/The-Incompleteness-of-Observation-FULL.tex` | `77800e0f2f8796e3236f348bf183262850708238` | regenerated by `./build.sh --book`, stamp included |
| `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` | the new `R7-PC4P` guard block, appended; no other region touched |
| `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` | this round's own paragraph in the `P1` physical-C4 section, alongside the two rounds already there |
| `verification/README.md` | `d25eb2d44d0aa324c095930f40174296fd0f2279` | this round's own paragraph |

**The rule for Table B.** The execution verifies each blob at the mandated base before writing. A
difference in `papers/Main.md`, `book/ch01-observation.md`, `book/glossary.md` or
`book/The-Incompleteness-of-Observation-FULL.md` is a **stop**: the frozen anchors of `PS3` are
re-located by search, and if an anchor string is absent or is not unique the insertion at that
coordinate is **not made**, the discrepancy is recorded, and the freeze is not repaired. A
difference in the other five is expected — sibling rounds move all of them — and the execution adds
its own region and leaves every other region byte-identical.

### The anti-contamination invariant, FROZEN VERBATIM

> A start-state discrepancy does not license the execution to consume the newer sibling result merely
> because it happens to be present at its mandated base. The round consumes only what its freeze says
> it consumes.

**The `§A.37` justification, beneath it.** §A.37 makes the control plane's merge commit the mandated
execution base and makes the preregistration immutable from that merge onward: *"once merged the
preregistration is immutable, and an execution that diverges from it records the discrepancy rather
than repairing the freeze. A freeze that can be edited after the outcome is known is not a freeze."*
The base is therefore a **chronological** fact and not an **evidential** one. It is the commit the
execution must descend from, so that the round's work is provably later than its own predictions; it
is not a licence to consume whatever a sibling lane happened to land in the interval, because
consuming that would let evidence enter the round after its predictions were fixed, which is the
single thing the freeze exists to prevent. The set of inputs is fixed by Table A and Table B, and by
nothing else that is present at the base. **Several lanes are drafting and executing in parallel
with this control plane**, and their results will be present at this round's mandated base; none of
them is an input here, and none is consumed.

## The targets, FROZEN

Six targets, `PS0` through `PS5`. **Every one is settled by locating, quoting, or a mechanical check
of the repository's own gate — never by proof, and never by argument.** No target of this round is
settled in the kernel, no target adds a Lean declaration, and the definition budget is **zero
slots**: this round defines nothing, in Lean or in prose.

### What settles a target, and what evidence counts — the governing evidence rule

**The evidence rule, FROZEN.** Every determination of this round is carried by one of:

1. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
2. a **verbatim quotation** from a merged result note, preregistration or amendment, with its
   coordinate; or
3. an explicit recorded statement that **the passage sought does not exist** on the record searched,
   with the search named and bounded; or
4. for `PS3` and `PS4` only, the **mechanical outcome** of a named repository check run on the edited
   tree, reported with the check's own name and its own output line.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the manuscripts
must mean X, because otherwise Y would fail" may appear only in a paragraph labelled as analysis
that states it is not evidence and that no target rests on it. **Where the record is silent, the
finding is that it is silent, and the silence is the finding.** A determination carried by a passage
that names a thing without displaying it is at most `medium`. A determination that a passage is
absent is worth nothing unless the search that failed to find it is named and bounded in the result
note — the files searched, at which blobs, and the strings searched for.

### `PS0` — the assignment and the two halves, located and quoted (type P)

Settled by locating and quoting. Record, each with its coordinate at a pinned blob:

- **`PS0-a`** — the prior-dependence half at `causal-readback-discovery/preregistration.md` line 215,
  with its control at `amendments/amendment-1.md` line 76.
- **`PS0-b`** — the visible-root half at `amendments/result-amendment-1.md` line 46, with line 48,
  which fixes that `mu_H` and the rooted family are held constant and only `p_0` varies.
- **`PS0-c`** — the assignment at `recurrence-tightness/result.md` line 200, and the two places round
  2 quotes it as its reason for not acting.
- **`PS0-d`** — round 2's incomparability finding, and its refusal to call either reading correct.

**Prediction: positive, high strength.** All four carry the text recorded here, verbatim, at the
pinned blobs. This freeze has already read each of them at `b78eac87`; the target exists so that the
execution re-verifies them at its own mandated base, where a sibling landing could have moved a line
number.

### `PS1` — the predicate index of each half, determined and not assumed (type P)

Settled by reading the two halves against the merged predicate definitions. The determination has
exactly two parts and neither is an inference from the other:

- **`PS1-a`** — the prior-dependence half is a statement about **P-divisibility**. Its own frozen
  conclusion says so in terms: *"P-divisibility is not a property of `(φ, partition)` alone."* It is
  not a statement about `C4w`, about `RoutedReadback`, or about `RoutedReadbackAtStorage`.
- **`PS1-b`** — the visible-root half is a statement about **`C4w`**, the maintained history-sensitive
  condition. Its own frozen conclusion says so in terms: *"C4w is preparation-support sensitive."* It
  is not a statement about P-divisibility, about `RoutedReadback`, or about `RoutedReadbackAtStorage`.
- **`PS1-c`** — **neither half indexes to either routed reading**, and this round derives no statement
  about either routed reading from either half. The record searched for such a statement is named and
  bounded in the result note: the two C4 rounds' preregistrations and result notes, and the discovery
  round's preregistration, result and both amendments, at the pinned blobs.

> **THE CLAUSE, carried at this mention — the target that fixes the index.** *"The C4 reading"* does
> not name one predicate. The merged record carries at least four distinct C4-level objects: the
> manuscripts' operational history-level condition, whose discovery-round form is `C4w`; the marginal
> signatures `C4e` and `C4r`, with `PDivisible` and `PIndivisibleWithin`; `RoutedReadback`, the
> seed-conditioned reading of the store clause; and `RoutedReadbackAtStorage`, the storage-time
> reading. The last two are **incomparable as predicates** — neither implies the other, neither is
> stronger than the other, and neither is the correct reading of C4. **Therefore every statement this
> round writes about what C1–C4 depend on names the predicate it is about.** The prior-dependence half
> of the backlog item is a statement about **P-divisibility**; the visible-root half is a statement
> about **`C4w`**; neither is a statement about `RoutedReadback` and neither is a statement about
> `RoutedReadbackAtStorage`, and no statement about either routed reading is derived from either half.
> An unindexed sentence of the form *"C4 depends on preparation"* is a **defect of this round**,
> whatever its sign.

**Prediction: positive, high strength** for `PS1-a` and `PS1-b`; **positive, medium strength** for
`PS1-c`, since it is a bounded absence rather than a quotation, and an absence is worth at most
medium under the evidence rule.

### `PS2` — the manuscript audit, bounded (type P)

The one question this round asks of the manuscripts, in three parts, each answerable by quotation or
by recorded silence.

- **`PS2-a`** — does any pinned manuscript surface carry the **hidden prior** as part of the datum?
  **Prediction: positive, high strength, and partial in extent.** `[Main]` §1.2 line 60 carries it at
  the level of the **emergent law** — *"the emergent law is a function of `(φ, partition, μ_H)`"* —
  and this freeze predicts that no surface carries it at the level of the **verdicts of the
  conditions**, which is the level `PS2-c` asks about.
- **`PS2-b`** — does any pinned manuscript surface name the **standalone initial visible law** as part
  of the datum a C1–C4 verdict is a function of? **Prediction: SILENT, medium strength.** The bounded
  search is named here and is re-stated in the result note with its outcome: `papers/Main.md`,
  `papers/GR.md`, `papers/SM.md`, `papers/Substratum.md`, `book/ch01-observation.md`,
  `book/ch07-gravity.md`, `book/glossary.md` and `book/The-Incompleteness-of-Observation-FULL.md`, at
  the pinned blobs, at every C4 coordinate round 1's `RS` table enumerates — taken with the
  corrections of that round's result-note discrepancy 5 — and then corpus-wide across those eight
  files for *initial visible*, *visible initial*, *initial distribution*, *root law*, *rooted
  preparation*, *initial state of the visible*, *standalone*, *support of the initial*, *preparation
  of the visible*, *initial visible configuration*, *p_0* and *preparation-relative*.
- **`PS2-c`** — does any pinned manuscript surface state that the **verdicts of C1–C4** are relative
  to a preparation, as distinct from the emergent law being a function of one? **Prediction: SILENT,
  medium strength**, on the same bounded search.

> **THE CLAUSE, carried at this mention — the manuscript audit.** *"The C4 reading"* does not name one
> predicate. The merged record carries at least four distinct C4-level objects: the manuscripts'
> operational history-level condition, whose discovery-round form is `C4w`; the marginal signatures
> `C4e` and `C4r`, with `PDivisible` and `PIndivisibleWithin`; `RoutedReadback`, the seed-conditioned
> reading of the store clause; and `RoutedReadbackAtStorage`, the storage-time reading. The last two
> are **incomparable as predicates** — neither implies the other, neither is stronger than the other,
> and neither is the correct reading of C4. **Therefore every statement this round writes about what
> C1–C4 depend on names the predicate it is about.** The prior-dependence half of the backlog item is
> a statement about **P-divisibility**; the visible-root half is a statement about **`C4w`**; neither
> is a statement about `RoutedReadback` and neither is a statement about `RoutedReadbackAtStorage`, and
> no statement about either routed reading is derived from either half. An unindexed sentence of the
> form *"C4 depends on preparation"* is a **defect of this round**, whatever its sign.

**What `PS2` does not ask.** It does not ask which reading of the store clause the manuscripts
intend. Round 2 asked that question, bounded it, and recorded the manuscripts silent; that
determination is consumed as merged and is not re-run here.

### `PS3` — the frozen manuscript sentences

**Conditional on `PS2`.** An insertion is made at a coordinate **only if** `PS2` returns the
prediction above at that coordinate — that is, only if the surface is silent on what the inserted
sentence says. If `PS2-b` or `PS2-c` returns *found* at a coordinate, the insertion at that
coordinate is **not made**, the passage found is quoted in the result note with its coordinate, and
the outcome is reported under the frozen sentence for that branch.

**The sentences below are frozen character for character.** They are manuscript voice: present
tense, no round numbers, no narration of any prior state, no repository vocabulary, no predicate
name that is not already in the manuscripts. Each is inserted by **appending to the end of the
anchor line**, separated from the anchor by a single space; no existing character is deleted or
reordered at any of the four coordinates.

> **THE CLAUSE, carried at this mention — the frozen manuscript sentences.** *"The C4 reading"* does
> not name one predicate. The merged record carries at least four distinct C4-level objects: the
> manuscripts' operational history-level condition, whose discovery-round form is `C4w`; the marginal
> signatures `C4e` and `C4r`, with `PDivisible` and `PIndivisibleWithin`; `RoutedReadback`, the
> seed-conditioned reading of the store clause; and `RoutedReadbackAtStorage`, the storage-time
> reading. The last two are **incomparable as predicates** — neither implies the other, neither is
> stronger than the other, and neither is the correct reading of C4. **Therefore every statement this
> round writes about what C1–C4 depend on names the predicate it is about.** The prior-dependence half
> of the backlog item is a statement about **P-divisibility**; the visible-root half is a statement
> about **`C4w`**; neither is a statement about `RoutedReadback` and neither is a statement about
> `RoutedReadbackAtStorage`, and no statement about either routed reading is derived from either half.
> An unindexed sentence of the form *"C4 depends on preparation"* is a **defect of this round**,
> whatever its sign.

**How the four sentences carry the index, since they cannot carry THE CLAUSE.** Each names the
predicate whose verdict it is about in the manuscripts' own words — *the condition as stated here*,
*(C4) as stated below*, *C4 as stated above*, *C4* in the glossary's own entry — and each of those is
the operational history-level condition, which is `C4w`. Where P-indivisibility is named it is named
separately, as its own object, because the prior-dependence half is about that and not about the
condition. **No sentence attributes both dependences to one datum or to one pair of preparations.**
Where a sentence states both, it states them as two statements, each with its own held-fixed list:
the condition's verdict varies with the standalone initial visible law, with the bijection or
dynamics, the partition **and the hidden prior** held fixed; P-indivisibility's verdict varies with
the hidden prior, with the map and the partition held fixed. **No sentence says that one pair of
preparations moves both verdicts**, because the record exhibits no such pair. **No inserted sentence mentions a routed read-write cycle as bearing on preparation
scope**, and `PS3-b` says in terms that the realization clause's routed cycle is a separate property
about which the scope remark asserts nothing.

#### `PS3-a` — `papers/Main.md` §1.3, line 72

**Anchor, frozen**, the tail of line 72, required present and unique in the file:

```text
work and is nowhere consumed by a proof here; the realization clauses below are physical statements of that picture, not premises.
```

**Inserted sentence, frozen character for character:**

```text
Checking them requires the preparation as well as the bijection and the partition: the fixed hidden prior is part of the realization datum (§1.2, *Remark (the measure as a realization datum)*), and the standalone initial visible law is a further datum. With the bijection, the partition and the hidden prior all held fixed, two standalone initial visible laws can give (C4) as stated below different verdicts. Separately, with the bijection and the partition held fixed, two hidden priors can give the P-indivisibility of §2.3 different verdicts.
```

#### `PS3-b` — `papers/Main.md` §1.3, line 80, the **(C4)** entry

**Anchor, frozen**, the tail of line 80, required present and unique in the file:

```text
fair coin satisfies all three with identically zero backflow on arbitrarily long accessible horizons (`review3_probes.py`; §2.3).)
```

**Inserted sentence, frozen character for character:**

```text
(Scope: the condition is preparation-relative. With the bijection, the partition and the hidden prior all held fixed, the standalone initial visible law decides which visible histories carry positive probability, and two such laws can give the condition different verdicts; the routed read-write cycle named above under Realization is a separate property, about which this scope remark asserts nothing.)
```

#### `PS3-c` — `book/ch01-observation.md` §1.3, line 61, mirrored at `book/The-Incompleteness-of-Observation-FULL.md` line 405

**Anchor, frozen**, the tail of line 61 in the chapter and of line 405 in the assembled book,
required present and unique in each file:

```text
erified structurally, C2 and C3 are verified with enormous margins, and C4 is named but not presently discharged (Chapter 7 §7.2).
```

**Inserted sentence, frozen character for character:**

```text
C4 as stated above is relative to a preparation and not to the dynamics and the partition alone: with the dynamics, the partition and the hidden prior all held fixed, two initial visible laws can give it different verdicts. Separately, the indivisibility of the visible process is relative to the hidden prior: with the dynamics and the partition held fixed, two hidden priors can give it different verdicts.
```

#### `PS3-d` — `book/glossary.md`, the **C4** entry, line 31, mirrored at `book/The-Incompleteness-of-Observation-FULL.md` line 6593

**Anchor, frozen**, the tail of line 31 in the glossary and of line 6593 in the assembled book,
required present and unique in each file:

```text
a quantitative lower bound on observable conditional memory inside an accessible window (Main §2.3). Discussed in Chapter 1 §1.3.
```

**Inserted sentence, frozen character for character:**

```text
The verdict is relative to the initial visible law: C4 is checked of that law alongside the dynamics and the partition, and two such laws can give it different verdicts.
```

**Prediction: positive, medium strength.** Each anchor is present and unique at the start-state blobs
and each insertion is an append. Medium rather than high because the anchors are pinned at
`b78eac87` and four sibling lanes may move a manuscript line before the mandated base.

### `PS4` — the FULL-mirror discipline and the gate, mechanically

**The FULL-mirror discipline, stated in the freeze because the round touches book chapters.** The
book is maintained as chapter sources **plus** an assembled `book/The-Incompleteness-of-Observation-FULL.md`
mirror, and `papers/oi_lattice_code/mirror_check.py` enforces the rule that **every nonblank line of
every chapter appears verbatim in `FULL.md`**. A chapter edit therefore has a mirrored line in the
assembled book, and this round has two of them: `PS3-c`'s edited line 61 of `book/ch01-observation.md`
must appear verbatim as `FULL.md` line 405, and `PS3-d`'s edited line 31 of `book/glossary.md` must
appear verbatim as `FULL.md` line 6593. **The mirrored line is replaced, not added.** Appending the
edited line while leaving the anchor line in place would satisfy `mirror_check` and leave the corpus
with two wordings for one passage, which is the defect the mirror rule exists to prevent; the
execution replaces each mirrored line in place and the result note records both mirror coordinates
explicitly.

- **`PS4-a`** — `mirror_check` reports zero divergences on the edited tree.
- **`PS4-b`** — `duplicate_check` reports OK on the edited tree, including on this round's own
  artifacts. Each carriage of THE CLAUSE differs from every other by its naming line, which is inside
  the quote, and every heading in every artifact of this round is unique within its file.
- **`PS4-c`** — `voice_check` reports OK. The inserted sentences narrate no revision history; they
  state a scope in present tense.
- **`PS4-d`** — `claims_check`, `dependency_label_check --strict`, `citation_check` and
  `architecture_check` report OK on the edited tree.
- **`PS4-e`** — `staleness_check` reports OK, which requires `papers/Main.tex` and
  `book/The-Incompleteness-of-Observation-FULL.tex` regenerated from the edited sources by `./build.sh`
  so that each carries the `% source-sha256:` stamp of its own source.
- **`PS4-f`** — `python3 verification/lean/edge_rigidity_probe.py` prints `ALL CHECKS PASS` with the
  new `R7-PC4P` block present and every existing guard, `R7-PC4`, `R7-PC4S` and `R7-AUDB` among them,
  unchanged and passing.

**The build rule, frozen, because it can stop this round.** `./build.sh` requires `pandoc` and
`xelatex`. **The manuscript edits and the regenerated stamped artifacts land together or not at
all.** If the execution environment cannot run `./build.sh`, the execution does **not** ship a
manuscript edit with a stale artifact: it records that the build was unavailable, makes no insertion,
and the round returns `UNDECIDED` at `PS3` and `PS4` with its located determinations `PS0`–`PS2` and
`PS5` intact. A publication-record repair that leaves the built corpus inconsistent with its sources
is a worse record than the one it set out to repair.

**Prediction: positive, medium strength**, with `PS4-e` the weakest link and named as such.

### `PS5` — the scope boundary, verified and recorded

Settled by comparison, not by judgement.

- **`PS5-a`** — the three residue coordinates — `papers/GR.md` line 561, `book/ch01-observation.md`
  line 257, `book/The-Incompleteness-of-Observation-FULL.md` line 601 — carry at the mandated base the
  text round 1's `RS` table records, and carry it byte-identical on this round's head. Reported by
  quotation at the base and by an empty diff at those coordinates on the head.
- **`PS5-b`** — round 1's preregistration, result note, module and guard block are byte-identical
  between the base and this round's head, as are round 2's. Reported by empty `git diff` over
  `round-c4-1-physical-discharge/`, `round-c4-2-storage-readback/`, `OIBridge/PhysicalC4Discharge.lean`,
  `OIBridge/PhysicalC4StorageReadback.lean`, and by the absence of any change to `R7-PC4`'s and
  `R7-PC4S`'s blocks in `edge_rigidity_probe.py`.
- **`PS5-c`** — every coordinate this round quotes from `[GR]` §8.1 and `[Main]` §4.2 is taken from
  round 1's **corrected** attribution in its result-note discrepancy 5, and `partIdx` and
  `partIdx_fst` are located in `OIBridge/OIRealization.lean`. Reported by naming the source of each
  attribution.

**Prediction: positive, high strength.** All three are mechanical comparisons.

## The preregistered predictions, and their strengths

| target | prediction | sign | strength |
| --- | --- | --- | --- |
| `PS0-a` | the prior-dependence half and its control carry the recorded text verbatim | positive | high |
| `PS0-b` | the visible-root half and its constancy sentence carry the recorded text verbatim | positive | high |
| `PS0-c` | the assignment sentence carries the recorded text verbatim | positive | high |
| `PS0-d` | round 2's incomparability finding and its refusal to call either reading correct are on the record verbatim | positive | high |
| `PS1-a` | the prior-dependence half indexes to **P-divisibility** | positive | high |
| `PS1-b` | the visible-root half indexes to **`C4w`** | positive | high |
| `PS1-c` | neither half indexes to either routed reading, on a named bounded search | positive | medium |
| `PS2-a` | `[Main]` §1.2 line 60 carries the hidden prior as a datum, at the level of the emergent law | positive | high |
| `PS2-b` | no pinned manuscript surface names the standalone initial visible law as a datum: **SILENT** | silent | medium |
| `PS2-c` | no pinned manuscript surface states the conditions' verdicts are preparation-relative: **SILENT** | silent | medium |
| `PS3-a` | the `[Main]` §1.3 line 72 anchor is present and unique, and the sentence appends cleanly | positive | medium |
| `PS3-b` | the `[Main]` §1.3 line 80 anchor is present and unique, and the sentence appends cleanly | positive | medium |
| `PS3-c` | the `ch01` line 61 anchor and its FULL mirror are present and unique, and the sentence appends cleanly to both | positive | medium |
| `PS3-d` | the glossary line 31 anchor and its FULL mirror are present and unique, and the sentence appends cleanly to both | positive | medium |
| `PS4-a` | `mirror_check` zero divergences | positive | high |
| `PS4-b` | `duplicate_check` OK, this round's artifacts included | positive | high |
| `PS4-c` | `voice_check` OK | positive | high |
| `PS4-d` | `claims_check`, `dependency_label_check --strict`, `citation_check`, `architecture_check` OK | positive | high |
| `PS4-e` | `staleness_check` OK, on regenerated stamped artifacts | positive | **low** |
| `PS4-f` | `edge_rigidity_probe.py` prints `ALL CHECKS PASS`, with `R7-PC4`, `R7-PC4S` and `R7-AUDB` unchanged | positive | high |
| `PS5-a` | the three residue coordinates are byte-identical at the base and on the head | positive | high |
| `PS5-b` | rounds 1 and 2 are byte-identical between the base and the head | positive | high |
| `PS5-c` | every reused attribution is the corrected one | positive | high |

`PS4-e` is rated **low** deliberately: it is the one prediction of this round that depends on
software the execution environment may not carry, and rating it low now means an `UNDECIDED` there is
a recorded outcome rather than a surprise.

## The status rule — every outcome, with its FROZEN post-round sentence

Each sentence below is the result note's wording for that outcome, fixed here. The execution selects
one per target and changes no word of it. These sentences are governed by the anti-conflation
section rather than carrying THE CLAUSE inside them, for the reason stated there.

### `PS0` — outcomes: located / partly located / UNDECIDED

**All four located:**

> The backlog item is on the record at its three coordinates and the record itself assigns its repair
> to a publication-record task of its own; both halves and the assignment are quoted verbatim in this
> note with their coordinates, together with the finding that the seed-conditioned and storage-time
> readings of the store clause are incomparable as predicates.

**Any coordinate moved or absent:**

> The backlog item is on the record and is quoted verbatim in this note at the coordinates found at
> the mandated base; the coordinates that moved are named with their base positions, the freeze is not
> edited, and the discrepancy is recorded.

**UNDECIDED:**

> The coordinates named in the freeze could not be verified at the mandated base on the search this
> note records, and no determination about what the record assigns is made here.

### `PS1` — outcomes: both indexed / one indexed / UNDECIDED

**Both halves indexed:**

> The two recorded halves of the item index to different predicates: the prior-dependence half is a
> statement about P-divisibility and the visible-root half is a statement about the maintained
> history-sensitive condition. Neither is a statement about either reading of the store clause, and no
> statement about either reading is derived from either half in this note.

**One half indexed, the other not:**

> One recorded half of the item is indexed to its predicate by its own frozen conclusion; the other is
> reported unindexed on the record searched, with the search named and bounded, and no predicate is
> attributed to it here.

**UNDECIDED:**

> Neither half is indexed to a predicate on the record searched, the search is named and bounded in
> this note, and no statement about what C1–C4 depend on is written under any predicate name.

### `PS2` — outcomes: silent as predicted / found / partly found / UNDECIDED

**Silent as predicted:**

> The manuscripts carry the hidden prior as part of the realization datum at the level of the emergent
> law, at the coordinate quoted in this note. No passage at the pinned blobs names the standalone
> initial visible law as part of the datum a condition's verdict is a function of, and no passage
> states that the verdicts of the conditions are relative to a preparation, on the search named and
> bounded in this note. The finding is that the manuscripts are silent on both, and the silence is the
> finding.

**Found, at either part:**

> The manuscripts already carry the determination this round asked them for, at the coordinate quoted
> verbatim in this note; no sentence is inserted at that coordinate and none is needed there.

**Partly found:**

> The manuscripts carry part of the determination at the coordinates quoted verbatim in this note and
> are silent on the remainder, on the search named and bounded here; a sentence is inserted only where
> the surface is silent, and the coordinates left untouched are named.

**UNDECIDED:**

> The bounded search this note names could not be completed at the mandated base, and no determination
> about what the manuscripts carry is made here; no sentence is inserted.

### `PS3` — outcomes: all four inserted / a subset inserted / none inserted / UNDECIDED

**All four inserted:**

> The manuscripts state at four coordinates that a verdict on the history-readback condition varies
> with the standalone initial visible law, the dynamics, the partition and the hidden prior held
> fixed; and, separately, that a verdict on the indivisibility of the visible process varies with the
> hidden prior, the dynamics and the partition held fixed. Neither dependence is stated of the other's
> datum, and no pair of preparations is said to move both verdicts. The sentences are the sentences
> frozen in the control plane, character for character, and each was appended to the anchor line the
> freeze pins.

**A subset inserted:**

> The manuscripts state at the coordinates named in this note that a verdict on the history-readback
> condition varies with the standalone initial visible law, the dynamics, the partition and the hidden
> prior held fixed. The sentences are
> the sentences frozen in the control plane, character for character; the coordinates at which no
> sentence was inserted are named here with the reason, and the freeze is not edited.

**None inserted:**

> No sentence was inserted. The reason is recorded in this note against the frozen anchors, the
> located determinations of this round stand on their own, and the freeze is not edited.

**UNDECIDED:**

> Whether the frozen sentences insert at their anchors is not determined by this round; the anchors as
> found at the mandated base are recorded against the freeze, no manuscript is written, and no
> determination about the manuscripts' wording is made.

### `PS4` — outcomes: gate green / gate red / build unavailable / UNDECIDED

**Gate green:**

> Every chapter line this round edits has its mirrored line in the assembled book, `mirror_check`
> reports zero divergences, the duplicate, voice, claims, dependency-label, citation and architecture
> checks report OK, the built artifacts carry the stamps of their own sources, and
> `edge_rigidity_probe.py` prints ALL CHECKS PASS with every existing guard unchanged.

**Gate red at any check:**

> The named check is red on this head and the round does not land: the failing check, its output and
> the coordinate it names are recorded here, the freeze is not edited, and no manuscript edit is
> shipped past a red gate.

**Build unavailable:**

> The manuscript build could not be run in this environment, so no manuscript edit is shipped and no
> built artifact is regenerated; the located determinations of this round stand and the manuscript
> insertion is left for a round that can rebuild the corpus it edits.

**UNDECIDED:**

> Whether the edited corpus passes the gate is not determined by this round: the checks that could be
> run are reported here with their own output lines, the checks that could not be run are named with
> the reason, and no manuscript edit is shipped on a gate this note cannot report green.

### `PS5` — outcomes: boundary held / boundary crossed / UNDECIDED

**Boundary held:**

> The two inference residues stand exactly as recorded, byte-identical at the mandated base and on
> this head, and are neither repaired nor given a verdict here; rounds 1 and 2 are byte-identical
> between the base and this head, no seal constant of either is written, and every attribution reused
> from round 1 is the corrected one its result note records.

**Boundary crossed:**

> A file this round's freeze places out of scope differs on this head; the file, the difference and
> the cause are recorded here, the freeze is not edited, and the round does not land until the
> difference is reverted.

**UNDECIDED:**

> The comparisons this target names could not be completed at the mandated base, and no statement that
> the scope boundary held is made here; what was compared and what was not is recorded, and the round
> does not land while the boundary is unverified.

### The `ROADMAP` row

**Whatever lands, the `P1` physical-C4 row stays OPEN and its status label does not move.** This
round discharges nothing at either cut and narrows no residual. Its `ROADMAP` paragraph is written
**alongside** the paragraphs of rounds 1 and 2, never over them, and every string `R7-PC4` and
`R7-PC4S` pin in `verification/ROADMAP.md` is left present and byte-identical. A different label
needs owner direction.

## What no outcome of this round licenses

- **No claim that C4 holds, or fails, at either physical cut.** This round proves nothing about any
  realization. The physical premise is untouched in both directions.
- **No claim that either reading of the store clause is the correct one**, and no ordering of the two.
  Round 2's incomparability finding is consumed as merged and is neither reopened nor extended.
- **No new condition, and nothing numbered beyond C4.** No condition is named or adopted beyond the
  four the manuscripts state, and this round adds none.
- **No claim that the preparation-scope facts bear on either routed reading.**

  > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.** *"The C4 reading"*
  > does not name one predicate. The merged record carries at least four distinct C4-level objects: the
  > manuscripts' operational history-level condition, whose discovery-round form is `C4w`; the marginal
  > signatures `C4e` and `C4r`, with `PDivisible` and `PIndivisibleWithin`; `RoutedReadback`, the
  > seed-conditioned reading of the store clause; and `RoutedReadbackAtStorage`, the storage-time
  > reading. The last two are **incomparable as predicates** — neither implies the other, neither is
  > stronger than the other, and neither is the correct reading of C4. **Therefore every statement this
  > round writes about what C1–C4 depend on names the predicate it is about.** The prior-dependence half
  > of the backlog item is a statement about **P-divisibility**; the visible-root half is a statement
  > about **`C4w`**; neither is a statement about `RoutedReadback` and neither is a statement about
  > `RoutedReadbackAtStorage`, and no statement about either routed reading is derived from either half.
  > An unindexed sentence of the form *"C4 depends on preparation"* is a **defect of this round**,
  > whatever its sign.

- **No verdict on the two inference residues**, in either direction. They are verified untouched and
  left for the owner call round 1's result note reserves.
- **No repair of round 1's or round 2's freeze**, and no statement that either round was wrong. Each
  executed its freeze and recorded its discrepancies, which is what a freeze is for.
- **Nothing about the discovery round's T1, its same-window bridge, or its negatives.** They are
  consumed as merged.
- **Nothing about accessibility.** No horizon is called accessible and no clock is attached to
  anything.
- **Nothing about H-Bell, Track B, `P0`, A6, Lemma 24.1, H-B, hydrodynamics or the substratum
  ensemble**, in either direction.
- **No movement of any `ROADMAP` status label.**
- **No claim that the manuscripts' realization clause changes meaning.** The inserted sentences state
  the datum a verdict is a function of; they restate no condition and they retract nothing.

## Numbered hazards

1. **Reading conflation — the round's primary hazard.** Writing *"C4 depends on preparation"* without
   naming which predicate. This is the natural phrasing of the backlog item itself, so it will present
   itself at every sentence. THE CLAUSE is carried at every prose mention for exactly this reason, and
   the four frozen manuscript sentences each carry the index in their own words. An unindexed sentence
   anywhere in this round's artifacts is a defect and is checked for in the final report.
2. **Scope creep into new mathematics.** The temptation to prove the preparation-dependence facts
   again, in the kernel, under one of the routed readings — a sentence of the form "and the same holds
   for `RoutedReadbackAtStorage`" would need a proof this round does not have and is not permitted to
   acquire. **The definition budget is zero slots and the kernel is not touched.** Anything that needs
   a proof belongs to a later round with its own freeze.
3. **The repair read as a discharge claim.** A sentence saying what a verdict depends on is close in
   shape to a sentence saying what the verdict is. None of the four frozen sentences states a verdict
   at any cut, and `PS3-b` says in terms that the routed cycle is a separate property.
4. **Forbidden vocabulary — revision narration.** `AGENTS.md` line 299 states the rule: *"The
   document never narrates its own history."* The vocabulary it forbids is exactly the vocabulary a
   publication-record repair reaches for first — the adverbs of supersession, the verbs of retraction,
   the comparatives that set a present wording against an unnamed prior one. **No artifact of this
   round contains any of them**, in manuscript voice or in the round's own voice. `voice_check`
   enforces the rule over `papers/` and `book/` and does not scan `verification/`, so the final report
   scans this round's own artifacts by hand against the list the owner directs, and reports the scan
   as done with its outcome.
5. **A half-edited mirror.** Editing a chapter line and not its `FULL.md` line, or adding the edited
   line to `FULL.md` while leaving the anchor line in place. The first is caught by `mirror_check`;
   **the second is not**, and is the one the execution must avoid by replacing in place.
6. **The stale built artifact.** Editing a manuscript source and shipping the `.tex` unrebuilt.
   `staleness_check` catches it; the build rule of `PS4` fixes what happens when the build cannot be
   run, so that the answer is never "ship it anyway".
7. **Consuming a sibling lane.** Several lanes are drafting and executing in parallel, and their
   results will be present at this round's mandated base. The anti-contamination invariant governs;
   the inputs are Table A and Table B and nothing else.
8. **Treating `[Main]` §1.2 line 60 as already carrying the whole item.** It carries the hidden prior
   as a datum of the **emergent law**. The backlog item is about the **verdicts of the conditions**,
   and it has a second half — the standalone visible root law — that line 60 does not touch. `PS2`
   asks the three questions separately for this reason, and an execution that collapses them has
   answered a question nobody asked.
9. **Repairing round 1's immutable freeze.** Its `partIdx` misattribution and its two approximate
   `RS` line attributions are recorded errors in a merged preregistration. §A.37 forbids editing it,
   and the scope decision above forbids re-recording them here. What is required is the opposite:
   never to reuse the uncorrected attribution.
10. **Widening into the residues.** They sit in the same files, at nearby coordinates, and will be
    read during `PS2`'s search. Reading them is required by `PS5-a`; repairing them is forbidden.
11. **`duplicate_check` on the carried clause.** THE CLAUSE is carried five times in this file and
    will be carried again in the result note. Each carriage differs by its naming line, inside the
    quote; every heading in every artifact is unique within its file. An execution that pastes a
    carriage without its naming line reddens the gate.
12. **Naming a further condition.** Absolutely forbidden: no condition is named or adopted beyond the
    four, under any name, in any artifact of this round.
13. **Overclaiming from a freeze.** This file predicts; it establishes nothing. Every sign and
    strength above is a prediction, and the result note reports each against it, including where it
    lands below.

## Definition budget: ZERO slots

**This round defines nothing.** No Lean declaration, no probe, no new predicate, no new term of art
in prose. Every object it names — `C4w`, `C4e`, `C4r`, `PDivisible`, `PIndivisibleWithin`,
`RoutedReadback`, `RoutedReadbackAtStorage`, `rootedPosterior`, `rootedStatePosterior`,
`RootedRealization`, `partIdx` — is the merged kernel's or the merged record's, named and never
redefined. An execution that introduces a definition has exceeded the budget and must say so as a
discrepancy; no amendment can be made after the outcome is known.

## Evidence level

**Type P throughout — prose and source audit.** No target of this round is in an axiom table, no
target carries a `#print axioms` line, and **the result note carries no axiom table**, because it
reports no kernel result. `PS4`'s determinations are mechanical outcomes of named repository checks,
reported with each check's own output line; they are not kernel evidence and are not labelled at any
evidence level. **No floating-point evidence, and no arithmetic of any kind, enters any label of this
round.**

## The chronology control

Phrased so that an auditor can check each clause mechanically.

1. **This preregistration blob is merged into `main` alone**, before any execution object of this
   round enters the repository tree — before any manuscript edit, any guard block, any `ROADMAP`,
   README or built artifact, any result artifact. *Check:* the control-plane pull request's diff adds
   exactly one file, this one, and changes nothing else. **The single permitted exception is the
   analysis recorded inside this blob** — the located coordinates, the quoted passages and the frozen
   sentences — merged *as* the freeze.
2. **The mandated execution base is exactly the merge commit of this control-plane pull request**, and
   the execution branches from that commit and from nothing else. *Check:*
   `git merge-base --is-ancestor <base> <E>`, and `_PC4P_BASE` in the execution's guard block equals
   that merge commit, as a literal.
3. **The execution's first act is to verify this file's blob at that base**, before any target is
   executed and before any manuscript byte is written. *Check:* `git hash-object` of this path at the
   base equals the blob the execution's guard pins, and the guard fails closed if it does not.
4. **Guard `R7-PC4P` pins this file by content and pins the inserted sentences by content**,
   fail-closed, each with a mutation control. *Check:* the guard's blob-pin function compares
   `git hash-object` of this path against a literal, and a drift control fails the guard if one byte
   is appended.
5. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit `refs/pull/<n>/merge`. An unresolvable
   head **fails closed**, with no fallback.
6. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and `H`
   the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a
   descendant of `B`**, fail-closed. A guard that checks only the head does not discharge this clause.
7. **The guard recovers whatever history it needs itself** — deepening a shallow clone, fetching an
   absent commit — and **fails** if recovery fails, for `B`, for `H`, and for every enumerated commit
   alike.
8. **The landing is `E` → `L`, with no pin commit**, this being a non-sealing round. `L`'s first
   parent is current green main and its second parent is exactly `E`; conflicts are resolved in `L`
   and never in `E`, which stays byte-identical. *Check:* `git rev-parse L^2` equals `E`, and the
   branch carries no third commit after `L`.
9. **`R7-PC4P` has no archive mode**, because the round creates no `_SEALED_HEAD` and no `_MERGE`.
   *Check:* neither string appears in the guard block, and the block's ancestry check is the
   execution-mode check of clause 6 alone.
10. **Rounds 1 and 2 are untouched.** *Check:*
    `git diff <base> <L> -- verification/lean/edge_rigidity_probe.py` contains no change to
    `_PC4_BASE`, `_PC4_SEALED_HEAD`, `_PC4_MERGE`, `_PC4S_BASE`, `_PC4S_SEALED_HEAD`, `_PC4S_MERGE`,
    or to any line of the `R7-PC4` or `R7-PC4S` blocks; and
    `git diff <base> <L> -- verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean`,
    `-- verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean`,
    `-- verification/programmes/physical-realization/round-c4-1-physical-discharge/` and
    `-- verification/programmes/physical-realization/round-c4-2-storage-readback/` are each empty.
11. **The residue coordinates are untouched.** *Check:* the three coordinates of `PS5-a` are
    byte-identical between `<base>` and `<L>`.
12. **What must have merged before this execution begins:** this control plane, and nothing else.
    *Check:* clause 2. No sibling control plane, no sibling execution and no sibling landing is a
    precondition of this round, and none is consumed as evidence by it — see the anti-contamination
    invariant.
13. **The residue repair and the fifth-coordinate question are downstream and are NOT scoped here.**
    *Check:* no artifact of this round writes at `papers/GR.md` line 561, `book/ch01-observation.md`
    line 257 or `book/The-Incompleteness-of-Observation-FULL.md` line 601, and no target, hazard or
    post-round sentence above states a verdict on either residue.

**The claim is scoped to the repository record.** Commit SHAs locate; **blob SHAs are what is
pinned**, and the two are named as such wherever both appear.

## Immutable inputs

Consumed as merged and unrevised: the discovery round's W/S/R clauses and timing, its T1 with the
preparation-scoped amendment, T2, T3, T4, and both halves of the preparation-dependence record;
round 1's `RD0`–`RD6`, its type-P `RS` determination with the corrections its result note records,
its definition-budget report and its axiom table; round 2's `CS0`–`CS6`, in particular `CS5`'s
incomparability and `CS0-d`'s recorded manuscript silence on the storage-surface distinction; the
recurrence-tightness round's `Publication boundary`; the causal-readback audit's verdict and its rule
that no further condition is created. Every Lean object either C4 round defines is named here and
redefined nowhere. The manuscripts are read at Table A and written only at the four `PS3` coordinates
of Table B.

## Non-doings

The round does not: run any part of the execution before this file is merged; introduce any
execution-specific object before then; write Lean; write a probe; alter any existing seal constant;
take a pin commit; edit round 1's or round 2's preregistration, result note, module or guard block;
repair either inference residue or state a verdict on either; repair the record-level errors in round
1's freeze; edit `papers/GR.md`, `papers/SM.md`, `papers/Substratum.md` or `book/ch07-gravity.md`;
move any `ROADMAP` status label; name or adopt any condition beyond the four; formalize `τ_return`,
connectedness or any accessibility clock; quantify anything over priors or over standalone visible
root laws in the kernel; derive any statement about `RoutedReadback` or `RoutedReadbackAtStorage`
from either half of the backlog item; say anything about H-Bell, Track B, `P0`, A6, Lemma 24.1, H-B,
hydrodynamics or the substratum ensemble; or consume any sibling lane's result.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once merged, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect. **An execution records discrepancies; it never edits
  the freeze.**
- **This pull request carries this file alone.** No Lean, no probe, no guard, no manuscript edit, no
  `ROADMAP`, README, census or built-artifact edit.
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying the
  four manuscript insertions with their two FULL mirrors, the two regenerated stamped artifacts, the
  guard block `R7-PC4P`, the result note, this round's own `ROADMAP` paragraph and README paragraph.
- Exact-head review after execution is complete, with full CI green on `E`.
- After certification the same pull request carries `L`, and nothing after it.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**

## Allowed final report

1. **`PS0`** — each coordinate with its verbatim quotation, and the statement that the round is type P
   with no axiom line anywhere;
2. **`PS1`** — the index of each half, each carried by that half's own frozen conclusion, and the
   bounded absence for `PS1-c` with its search named;
3. **`PS2`** — the quotation at `[Main]` §1.2 line 60, the two silences or the passages found, and the
   bounded search restated with its outcome;
4. **`PS3`** — each insertion with its coordinate, its anchor as found, and the inserted sentence
   quoted, together with the statement that each is the frozen sentence character for character;
5. **`PS4`** — the mirror coordinates named explicitly, and each named check with its own output line;
6. **`PS5`** — the residue quotations at the base, the empty diffs, and the statement that no verdict
   on either residue is given here;
7. the post-round sentences, one per target, verbatim from the status rule, with the `P1` row **OPEN**;
8. what no outcome licenses, in this file's wording, with THE CLAUSE carried at its mention there;
9. the definition count against the zero-slot budget;
10. the chronology certification, naming the property certified — no commit reachable from the
    execution head lies outside the control-plane merge's descendants — and the statement that this is
    a non-sealing round with no pin;
11. the anti-contamination invariant verbatim, with the start-state comparison at the base and any
    discrepancy recorded and not repaired;
12. a hand scan of this round's own artifacts for the forbidden vocabulary and for any unindexed
    sentence about what C1–C4 depend on, reported as done and with its outcome.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **Non-sealing rather than sealing.** The round pins its inserted wording by content, as `R7-AUDB`
   does for the manuscript wording nearest this subject, rather than sealing an execution head. An
   alternative would give it the archive triple and an `E` → `L` → `P` landing. This freeze chooses
   content pinning because the round owns no kernel object whose provenance a sealed head would
   protect, and because a pin commit on a round that creates no `_SEALED_HEAD` pins nothing. **The
   owner may direct otherwise, and that is an amendment before execution, not a discrepancy.**
2. **Four insertion coordinates rather than one.** One sentence in `[Main]` §1.3 would carry the
   determination for the papers alone and leave the book and the glossary saying less than the papers.
   The freeze chooses the four surfaces that state what the conditions are checked of, and leaves
   `[GR]`, `[SM]`, `[Substratum]` and `book/ch07` untouched because none of them states the datum.
3. **Appending rather than rewriting.** Every insertion appends to an anchor line and deletes nothing.
   An alternative would rewrite `[Main]` §1.3 line 72's final clause to name the preparation inline.
   The freeze chooses appending because it makes each edit a single reviewable sentence and keeps
   every existing pinned string intact.
4. **`PS2-a` predicted positive rather than silent.** `[Main]` §1.2 line 60 does carry the hidden
   prior as a realization datum, and a freeze that predicted silence there would be predicting against
   a passage it has read. The freeze predicts positive and confines the silence prediction to the two
   parts the record does not appear to carry.
5. **The residues verified rather than ignored.** Scoping them out for repair leaves the question of
   whether this round's edits disturb them. The freeze answers it with a verification obligation in
   `PS5-a`, so that the next round to take the owner call finds them exactly as round 1 left them.
6. **`PS4-e` rated low.** The build dependency is real and outside this round's control. Rating it low
   now, and freezing the build rule that governs its failure, keeps an unavailable toolchain from
   becoming a reason to ship an inconsistent corpus.

## Settled by the owner before this freeze merges

Each decision below is settled, and the freeze carries it. Amendment happens **before the merge and
only then**; after the merge this file is immutable and an execution records a discrepancy rather
than repairing it.

1. **NON-SEALING**, `E` → `L`, no `P`, with `R7-PC4P` carrying `_PC4P_BASE`, the blob pin of this
   file and the manuscript content contracts, and no `_SEALED_HEAD` and no `_MERGE`. Content pinning
   is the right instrument for a prose-only publication repair: no kernel object is created here, so
   there is nothing an archive seal would seal.
2. **The manuscripts are edited. `PS3` and `PS4` stay.** The record carries stable preparation-scope
   facts the publication surfaces do not state, and this round is chartered to propagate them without
   changing the mathematics. A determine-and-record round would leave the backlog item standing.
3. **The four coordinates stand; three of the four sentences are sharpened.** The coordinates are
   unchanged. `PS3-a`, `PS3-c` and `PS3-d` state the two dependences as two statements, each with its
   own held-fixed list, because the record establishes one fact about the standalone initial visible
   law and the condition's verdict, and a separate fact about the hidden prior and P-indivisibility's
   verdict. It establishes no pair of preparations that moves both. `PS3-d` names only the visible-law
   dependence, the hidden prior not being established here as a dependence of the condition's verdict.
   `PS3-b` already carried the index in this form and stands as drafted. **An unindexed collective —
   "each verdict is relative to a preparation" over C1–C4, or over the C4-level predicates — is
   forbidden by THE CLAUSE and appears in no sentence.**
4. **The two inference residues stay out of scope for repair and in scope for a byte-identity
   verification only.** Repairing one is a claim change at the cosmological cut and belongs to a round
   with its own freeze.
5. **Round 1's preregistration errors stay out of scope for repair and in scope for propagation.**
   This round consumes only the corrected result-note attributions, so that no third correction
   surface is created.
6. **A dedicated `R7-PC4P`**, rather than extending `R7-AUDB`. This round owns a coherent new
   contract — its freeze blob, its base and its four insertion contracts — and keeping that ownership
   separate keeps a later audit clean.
7. **The all-or-nothing build rule stands.** Source edits without regenerated stamped artifacts are
   not an acceptable publication repair, and an unavailable `pandoc` or `xelatex` returns `PS3`/`PS4`
   UNDECIDED rather than shipping an inconsistent corpus.
8. **`PS2`'s bounded search stands as frozen** — eight files, the `RS` coordinate list, twelve search
   strings. It is broad enough to falsify the silence predictions and is frozen independently of the
   outcome.
