# Seal infrastructure round SI-2 — the bootstrap cutover: RESULT

Executed from the mandated base `B` = `df54b99dba99dc043b11752163d8d348c9e54472`, the certified
merge commit of Amendment 2 (#672, push run 35351379664), and from no other commit. The base is the
third the round has had, and the other two are recorded as what they became: the preregistration
merge `da9d69d60b19482abfeb27b16af5aaebebba0e83` (#669) is the certified freeze from which nothing
resumes, and the Amendment 1 merge `9ca82958cfaa3ff926d8a80baf2ee22eb468a917` (#671) is the
certified pre-Amendment-2 base from which nothing resumes. The execution's first act verified the
**three frozen blobs** at `B`: the preregistration `bfcd43831d887c006eab64c9a4b8b5f35ff41c9a`,
Amendment 1 `9d05509d8fb84d9007c73b40a062bbdb7b6c36ea`, Amendment 2
`c57d1dc9a3b370c86a91fcb01f7209ef5da782d5`. `R7-SI2` pins all three, each with its own drift
control.

This round is **NON-SEALING**. It lands `E` → `L`. It owns no seal state, creates none and alters
none: it carries `_SI2_BASE` and act 10's strengthened ancestry check, and
`_SI2_SEALED_HEAD` and `_SI2_MERGE` do not exist — not as `None`, not at all. Its own guard is
the one guard in the file that is **not** cut over, because `SI-2` has no manifest record by design.

**What the round did.** It made the adjudicated union-of-visibility-targets derivation rule
executable, moved every prior-round ancestry and archive clause onto the generic validator with the
old machinery kept as a shadow, made the data-driven integrity rule authoritative with the per-round
comparisons kept as a shadow, and amended the process protocol so that future rounds seal through
the manifest. It deleted nothing: the sixty-one legacy seal-constant assignment statements are at
the head exactly as they were at `B0`. Their retirement is the separate, sealing, follow-up round
the freeze names.

## Two control-plane collisions, adjudicated before execution and not during it

Both were found by uncommitted dry runs and put to the owner; neither was absorbed by the
implementation, and each produced an append-only amendment before a single execution commit
existed.

1. **Amendment 1.** With `SI1.json` present, `R7-SI1` failed on its own frozen manifest-cardinality
   contracts while every validator agreed. Adjudicated as path D: the contracts are scoped to the
   twenty-two records `SI-1` transcribed, and **the `R7-SI1` scoping is Amendment 1's single
   allowance**, bounded to the named contracts — the cardinality counts, the record-axis counts,
   the twenty-two census rows, the `#140` probe and the no-stem check, read extensionally as
   Amendment 2 confirms. `SI-1`'s `census.json` is not regenerated and not repinned.
2. **Amendment 2.** With `_SI2_BASE` present, `R7-SI1`'s N13 seal-constant containment contract
   failed, being written to admit exactly one addition. Adjudicated as exactly the N13 delta: the
   allowed-addition set is **exactly `{_SI1_BASE, _SI2_BASE}`**, containment stands, no `SI-2`
   seal triple may exist, any third legacy-style assignment still fails, and the retirement round's
   deletions are not admitted. That is Amendment 2's single allowance to `R7-SI1`. Amendment 2 also
   confirmed that `SI2-3` reaches `SI-1`'s own clause, permitted the validator relocation and the
   two-line O2 hook, accepted the nested base-guard cost, and read frozen precondition 6 as a
   provenance fact about `B0`.

## Outcomes

| target | outcome | decided by |
|---|---|---|
| `SI2-0` | **`HOLD`** | six pins and twelve preconditions, read from git at `B` |
| `SI2-1` | **`MANIFEST-AS-AUTHORIZED`** | 23 records, 18 `sealed`, 5 `base-only`; `SI1.json` exactly as authorized; U5 reports nothing mutated, removed or added since stage 1; the two `R7-SI1` edits bounded |
| `SI2-2` | **`DERIVE-UNION-BUILT`** | the eleven executable negative cases, each for its named reason |
| `SI2-3` | **`AUTHORITY-MOVED`** | 23 of 23 clauses gate on `U3`, 0 on a legacy constant; two dynamic controls |
| `SI2-4` | **`DELTA-AS-ADJUDICATED`** | the census at the final head: 23 of 23 records agree; controls diverge on exactly 7, 13, 20; control 10 agrees |
| `SI2-5` | **`INTEGRITY-DATA-DRIVEN`** | U5 gates; 0 live per-round prior-seal gates; 8 comparator verdicts recorded as shadows |
| `SI2-6` | **`MAP-PRESERVED`** and **`LEGACY-INTACT`** | the base's guard file run, 91 tags all `PASS` and identical at the head; sixty-one statements identical as text |
| `SI2-7` | **`PROTOCOL-UPDATED`** | `AGENTS.md` §A.37's closing subsection and the qualified landing-shape sentence |
| `SI2-8` | **`RESTATED-AND-HOLDS`** for `#141`; **`RESTATED-ONLY`** for `#140` | `U3` passes the historical-head case; no independent source for the mandate |

**The stages were run in the frozen order, and the order was gating**: stage 1 was committed
before anything else, stage 2's regressions were measured on the committed stage-2 tree before
stage 3 began, and stages 4 and 5 followed stage 3. Each stage is its own commit on the execution
branch, and **the final head `E` is the checkpoint**: the census that certifies the cutover is
measured at the same commit that carries the cutover, by `R7-SI2` on every run, and not by a
local measurement taken earlier.

## `SI2-0` — locating controls

All six pinned blobs are at `B` as the freeze recorded them at `B0`, and the guard file at `B` is
byte-identical to the guard file at `B0`. The twelve preconditions hold, read from git at `B` and
not from the working tree: no `R7-SI2` and no `_SI2` in the base's guard; twenty-two records,
eighteen sealed and four base-only, with no `SI1` and no `SI2`; sixty-one statements over
fifty-nine names; `B0`'s parents `99ab6370…` and `d75427ae…`, with `B0` on `B`'s first-parent
spine (the provenance reading of precondition 6); the sentence `SI2-7` supersedes present at `B`;
the cardinality contracts unscoped at `B`; N13 unamended at `B`; and `B` itself a merge whose
first parent is the Amendment 1 merge and whose second parent carries Amendment 2 at its frozen
blob. Precondition 4 was measured by running `B`'s own guard file: 91 tags, all `PASS`.

## `SI2-1` — the authorized addition, first and then fixed

Stage 1 did what the freeze required, **exactly one record was added, first**:
`verification/seals/SI1.json`, `kind: "base-only"`,
`base` = `99ab6370470ed9d9e4005551581c6c8c18e54bd2`, in the first execution commit. The record set
from that commit is twenty-three records, eighteen `sealed` and five `base-only`, and at the final
head U5 reports it unchanged — nothing else added, nothing mutated, nothing removed. `SI-2` adds no
record for itself; its record belongs to the retirement round.

Stage 1 also carried the two authorized edits to `R7-SI1`, and `R7-SI2` checks that they reach no
further: the scoping names exactly twenty-two transcribed stems and one authorized addition, N13's
allowance is the two-element set and no other form, and no `_SI2_SEALED_HEAD` or `_SI2_MERGE`
exists. A scoping reaching beyond the named contracts, or an N13 allowance wider than the two, is
`MANIFEST-DEVIATED`, and both are mutation-tested.

**The mandated pre-commit dry run**, on exactly the stage-1 tree: `ALL CHECKS PASS`, 91 tags, all
91 pre-existing tags `PASS` with `R7-SI1` among them, the verdict map identical to the pristine
base's. The one-verdict allowance Amendment 1 granted was used and nothing else changed.

## `SI2-2` — the union rule is executable

`U1`, the union resolver, is `_rbr_archive_visibility_targets`'s semantics stated once: `HEAD` on a
push; on a pull request the real `pull_request.head.sha` **and** the live
`refs/remotes/origin/<base ref>`, never `pull_request.base.sha`, never a local branch, never the
synthetic merge, failing closed. `U2`, the union derivation, returns the merges whose non-first
parent is exactly the sealed head over the set union of the targets' reachable histories,
deduplicated by SHA, and `None` when any target is missing or git cannot answer. `U3` is `SI-1`'s
O2 handed `U1`'s targets for its visibility leg and `U2` as its derivation.

The eleven executable cases of the negative suite, each satisfying its named outcome for its named
reason:

| # | case | verdict |
|---|---|---|
| 1 | landing on the live base branch, unreachable from the head | **PASS** under `U3`; targets `[head, origin/main]`, one candidate derived — `SI-1`'s control 10 made executable |
| 2 | the same, base branch rewound off the landing | FAIL, `zero candidates` |
| 3 | unresolvable remote base ref | `U1` returns `None`, `U3` fails closed; `base.sha` (well-formed, carrying the landing) and a local branch of the same name are both refused |
| 4 | head and base carrying **different** landings of one `E` | FAIL, `multiple candidates`, the union holding both |
| 5 | head and base carrying the **same** landing | PASS with **exactly one** candidate after deduplication |
| 6 | the synthetic merge offered as a target | refused: `U1` never returns it; the resolved event FAILS where the synthetic merge would PASS |
| 7 | pin rewritten to a real merge in the union | FAIL, `disagreement` — derivation alone is not enough |
| 8 | a record added beyond `SI2-1`'s authorization | FAIL under U5, `added` alone |
| 11 | the bootstrap guard keyed on a manifest record | no verdict: `SI-2` has no record, and the bootstrap guard reads `_SI2_BASE` instead |
| 12 | a twenty-fourth record | FAILS the scoped `R7-SI1` integrity contract **and** U5 |
| 13 | a third legacy-style assignment | FAILS N13 as amended: the head's set minus the base's is exactly the two-element allowance, and a `_SI2_SEALED_HEAD` or a `_ZZ_BASE` makes it three |

Cases 9 and 10 are text and static controls and are reported under `SI2-6`(b) and `SI2-3`.
`SI-1`'s twenty cases run through O2's default route unchanged: 22 rows, 22 good, measured by
`R7-SI1` on every run.

### The validator relocation, and the hook

`U3` has to be defined before the first prior-round clause that calls it, and the marker-bounded
`SI1-VALIDATOR` region sat after the last. The region was **relocated verbatim** to just after
`_SI2_BASE`, with the record reader's two constants, and `R7-SI2` measures that the region at the
head equals the region at `B` after reverting **exactly the two-line** O2 hook: `derive=None`
added to `_si1_validate`'s signature, and the candidate line taking the injected derivation when
one is given. The **default route is still the target-only** `_si1_derive`, which is why `SI-1`'s
suite and census reproduce byte-for-byte.

## `SI2-3` — authority moved, and the old machinery became the shadow

Every ancestry and archive clause of a round represented in the manifest — the eighteen sealed
rounds, the four base-only rounds, and `SI-1`, which `SI2-1` made a manifested round — is now
exactly

    return _si2_authority('<STEM>', tag='R7-<STEM>', shadow=_<stem>_legacy_ancestry)

with the round's original clause kept verbatim under the `_legacy_ancestry` name, its diagnostics
retagged `/shadow`, computed on every run, recorded and printed beside `U3`'s verdict, and gating
nothing. `R7-SI2`'s own chronology guard is excluded by design.

Measured at the final head:

| measurement | value |
|---|---|
| clauses that gate on `U3` (static: the body is exactly the keyed call and references no legacy constant) | **23 of 23** |
| clauses that still gate on a legacy constant | **0** |
| surviving *shadow* reads of legacy constants inside the legacy bodies, reported and not bounded | 116 |
| shadow-forcing control: `_si2_authority` returns `U3`'s verdict when the shadow is forced to the opposite value | 23 of 23 unchanged |
| in vivo control: every sealed round's `_<STEM>_MERGE` rebound to its sealed head, the clause re-run | 18 of 18 verdicts unchanged, 18 of 18 shadows flipped to `FAIL` |
| the live ledger at the head | 23 clauses, `U3` `PASS` 23, legacy shadow `PASS` 23 |

Negative case 10: a clause rewritten to `return _hya_legacy_ancestry()` fails the static test; the
same function passed as the `shadow=` argument does not. Hazard H1, the shadow that gates, is the
thing both dynamic controls exist to exclude.

## `SI2-4` — the census at the final head

`U4` is `SI-1`'s O3 with the roles inverted: `U3` authoritative, the old machinery the shadow, over
every manifest record and over the synthetic control suite, emitting `census.json` for this round.
The old side is the legacy machinery as the per-round clauses ran it — the archive certificate on
the round's first-assignment constants for a sealed round, resolving the event for itself; the
strengthened execution check against the round's `_<STEM>_BASE` for a base-only round — and a row is
admitted only if the constants and the record name the same objects. The twenty-third row, `SI1`,
takes its shadow from `R7-SI1`'s own check against `_SI1_BASE`, exactly as the four other base-only
rows take theirs, and it was admitted: `_SI1_BASE` and `SI1.json`'s `base` are the same commit.

| axis | records | `U3` lifecycle | agreement |
|---|---|---|---|
| lifecycle | 18 `sealed` | `ARCHIVED` ×18 | 18 of 18 |
| schema + pinned base + record integrity | 5 `base-only` | `not-applicable` ×5 | 5 of 5 |

Over the twenty-one synthetic controls: nine no-analogue, twelve comparable, and **exactly three
diverge — 7, 13 and 20 — each in `U3`'s adjudicated direction**: a second merge carrying the same
sealed head is refused as multiple candidates, a descendant of an unpinned landing is refused as
seal pending, and a completed non-sealing round is held out of the state machine. **Control 10
agrees**, both sides passing: the divergence `SI-1` measured reversed has disappeared, because `U3`
now sees the base-branch tip. Controls 11 and 12 agree, both sides failing. So 7, 13 and 20 diverge in `U3`'s adjudicated
direction and control 10 agrees, which is the frozen profile to the row. The outcome is
**`DELTA-AS-ADJUDICATED`**, and it is not called equivalence, because the profile it accepts
contains three intentional behavioural deltas.

The four divergences are carried as **adjudicated behaviour and not correctness**. The owner's
disposition selected which behaviour gates on each control; no outcome of this round may be read as
a holding that either implementation is generally correct, and agreement where it occurs is
agreement and not correctness, for the reason `SI-1` gave: a shared error survives every case both
sides get wrong together.

`census.json` is rebuilt by `U4` from the rows each run measures and required to equal the recorded
bytes; the resolved targets' names are normalized to a fixed token first, because those names are
the event's and not the round's, and the verdicts are not normalized. A total altered and
unparseable bytes are both rejected by the same predicate.

## `SI2-5` — integrity data-driven, the comparisons as shadow

`U5` is `SI-1`'s `_si1_integrity` over the record set fixed at stage 1 — read from git at `B` plus
the one authorized record, never from the working tree — against the manifest now, reporting
mutated, removed and added as three distinct conditions. It gates, in `R7-SI2` and in place of every
per-round seal-integrity comparison: the eight live gates on the five comparators (`TCF`, `RNC`,
`TRJ`, `XTS` twice, `RNT` three times, the clause-9 controls included) each became the comparator's
verdict recorded through `_si2_shadow_integrity`, gating nothing, followed by
`ok_<stem> &= _si2_integrity_ok()`. Zero live prior-seal gates remain; the eight shadow verdicts
are all `PASS`; the comparators' own mutation controls stay as they were. `U5`'s controls: a
mutated, a removed and an added record are each reported alone. `U5` fires no slot: it is `SI-1`'s
definition applied.

## `SI2-6` — the verdict map and the legacy state

**(a) `MAP-PRESERVED`.** `B`'s own guard file was run in a subprocess in a detached worktree at
`B`, so at `B`'s tree and with `HEAD` the base commit, its verdict lines parsed into a
tag-to-verdict map: 91 tags, all `PASS`. The head's map over the same tags, read in process
from the tag registry beside `CHECKS`, is identical, and it is checked directly rather than as a
conditional because `R7-SI2` sits after every other check in the file. The fresh base map is also
required to equal the one persisted in `si2-tagmap.json`. Nested cost accepted, as Amendment 2
records: the base's file runs its own base's file.

**(b) `LEGACY-INTACT`.** The sixty-one legacy assignment statements at the head are, as text and
in the same relative order, the sixty-one at `B0`: **sixty-one statements over fifty-nine names, identical as text and in the same relative order**,
`_SI2_BASE` excluded by stem, and statement count alone cannot establish this and is not what is
measured. Negative case 9: removing either half of the double-assigned `_RNT_MERGE` pair, swapping
two statements, or re-valuing one each fails the comparison.

## `SI2-7` — the protocol

`AGENTS.md` §A.37 is amended prospectively, for rounds begun after `SI-2`'s landing. The
landing-shape sentence precondition 8 named now reads that `P` writes the round's own manifest
record, `sealed_head` = `E` and `merge` = `L` under `verification/seals/`, and not a legacy
constant, with the pre-`SI-2` form recorded in the past tense. The closing subsection, *Sealing
through the manifest, from `SI-2`'s landing*, states what a sealing round's `P` writes; how a new
`sealed` record is created; how a completed non-sealing round's `base-only` record is created —
afterwards, as an authorized addition named in the preregistration of the round that adds it, never
during its own execution; and the legacy constants' status in two halves, quoted:

> From `SI-2`'s landing the sixty-one legacy seal-constant assignments in the guard file
> **cease to GATE**: no check's verdict depends on them, they are read only as shadows of the manifest, and a
> round that writes a new one has recreated the representation `SI-2` retired. And until the
> retirement round they remain **PROTECTED HISTORICAL SEAL STATE**: altering or removing any of
> them constitutes taking ownership of existing seal state under this section, and makes the round
> that does it *sealing*.

> **The retirement round is sealing.** It follows that the round which deletes the fifty-nine names
> and sixty-one statements against `SI-2`'s frozen inventory, and removes the per-round
> seal-integrity comparisons the data-driven rule shadows, is **sealing** under this section, and
> its `P` writes its own `sealed` manifest record under this protocol — `sealed_head` = its `E`,
> `merge` = its `L` — and writes no legacy constant.

Outcome `PROTOCOL-UPDATED`; `R7-SI2` requires each statement and the absence of the superseded
sentence, with mutation controls on both halves.

## `SI2-8` — `#140` and `#141` restated under `U3`

`#141` asks whether prior seals are evaluated against the landing topology rather than the
pull-request head. Under `U3` a pull request opened from a historical head whose base branch
carries the landing **passes** — negative case 1, `SI-1`'s control 10 — so `#141` is
**`RESTATED-AND-HOLDS`**. **`SI-1`'s recorded `#141` result is not edited**: `RESTATED-AND-FAILS`
stands there as the measurement of the model `SI-1` built under the target-only rule, and a later
verdict is a later verdict.

`#140` is **`RESTATED-ONLY`**. The two structural observations hold over all twenty-three records —
23 of 23 recorded bases are merge commits, 18 of 18 sealed rounds have exactly one execution-history
commit whose sole parent is the recorded base — and 0 of 23 recorded bases were compared to an
independent mandate, this round having no such source and not undertaking one.

## Predictions against outcomes

| target | predicted | outcome | scored |
|---|---|---|---|
| `SI2-0` | `HOLD`, HIGH | `HOLD` | as predicted |
| `SI2-1` | `MANIFEST-AS-AUTHORIZED`, HIGH | `MANIFEST-AS-AUTHORIZED` | as predicted |
| `SI2-2` | `DERIVE-UNION-BUILT`, HIGH | `DERIVE-UNION-BUILT` | as predicted |
| `SI2-3` | `AUTHORITY-MOVED`, MEDIUM | `AUTHORITY-MOVED` | as predicted |
| `SI2-4` | **`DELTA-AS-ADJUDICATED`**, MEDIUM | **`DELTA-AS-ADJUDICATED`** | as predicted; `SI2-4` was the round's sharpest claim, and the control-10 divergence disappeared exactly as the union rule predicts while 7, 13 and 20 persisted in `U3`'s direction |
| `SI2-5` | `INTEGRITY-DATA-DRIVEN`, MEDIUM | `INTEGRITY-DATA-DRIVEN` | as predicted |
| `SI2-6` | `MAP-PRESERVED` and `LEGACY-INTACT`, MEDIUM | both | as predicted |
| `SI2-7` | `PROTOCOL-UPDATED`, HIGH | `PROTOCOL-UPDATED` | as predicted |
| `SI2-8` `#141` | `RESTATED-AND-HOLDS`, LOW | `RESTATED-AND-HOLDS` | as predicted, at the freeze's deliberately low strength: it failed in `SI-1` for exactly the reason the adjudication addresses |
| `SI2-8` `#140` | `RESTATED-ONLY` | `RESTATED-ONLY` | as predicted |

No prediction was missed. The freeze put its sharpest claim at MEDIUM and it held.

## Execution defects, corrected — held apart from the findings

Eight were in this round's own implementation, not in the freeze, and none is counted as a
discrepancy. The last three were found by the first complete run of the finished guard, which
reported every target's outcome as predicted and still failed `R7-SI2` on three clauses that print
nothing when they hold; each was a defect in the measurement and none in what it measured.

| # | defect | how it showed | corrected by |
|---|---|---|---|
| 1 | the stage-4 patch asserted **four** live `RNT` prior-seal gates where the file carries **three** | the patch's own assertion stopped it before any edit | the count corrected to eight in total; stage 4 then applied and was committed separately |
| 2 | two region checks in `R7-SI2` counted the marker strings in the file and required exactly one occurrence, while their own source contains the same strings | caught by reading the count before the first run | the region is taken between the markers' first occurrences, as `SI-1`'s check does |
| 3 | a first local release-gate run in a fresh worktree reported `lean-axioms` as "could not run" | a cold Mathlib bridge build exceeded the gate's subprocess limit, with the check itself idle | environmental; recorded in Amendment 2, the same commit passing 17 of 17 with the complete cache and in CI |
| 4 | `SI2-6`(a)'s first form ran the base's guard file against the **head's** working tree, as `SI-1`'s comparison had, and reported `MAP-CHANGED` on `R7-SI1` | the base's unscoped `R7-SI1` fails on the twenty-three-record manifest — the dry run Amendment 1 recorded, not a verdict change; the two maps being compared were not the base's and the head's | the base's file is run **at the base** |
| 5 | its second form exported the base's tree and pointed the subprocess at this repository's git directory through `GIT_DIR`, and reported `MAP-CHANGED` on `R7-VIS`, `R7-ARCH` and `R7-SI1` | an environment variable redirects every git call, including those the base's guard makes in the synthetic repositories its own regressions build, which then broke for a reason unrelated to the base — **and wrote into this repository**: the synthetic builders' `commit`, `checkout -b` and `update-ref` calls moved the local execution branch, the local `main`, the remote-tracking `origin/main`, created three synthetic branches and one synthetic remote-tracking ref, and set the repository's user identity, all locally and nothing pushed | every ref was restored from its reflog and `origin/main` refetched from the remote before the next run, the synthetic refs deleted and the identity restored; the base is now checked out as a **detached worktree** in a temporary directory, registered for the run and removed after it, with every git and pull-request environment variable removed so the base's guard resolves `HEAD` as the base commit and can reach nothing else |
| 6 | the stem-freedom check on the `SI2-AUTHORITY` region found the stem `SI1` in the region's own header comment, which named `SI-1`'s second target as `SI1-2` | the complete run: every printed outcome as predicted, `R7-SI2` failing | the comment reworded; the region carries no round stem, which is what the target states and the check now measures without an exception |
| 7 | the bound on the two authorized `R7-SI1` edits counted three literal strings over the whole file, and its own source carried each of them verbatim — the two-element `N13` allowance twice more, the one-element form once, the `_SI2_BASE` assignment once | the same run | the three literals are assembled from fragments at the top of the guard and never written out in it, so the file carries the two-element allowance exactly once, the one-element form nowhere, and the assignment exactly once, as the bound requires |
| 8 | the mutation control on the chronology contract replaced its phrase in the note as written, while the predicate reads the note with line breaks collapsed; the note carries the phrase twice and one copy wraps across a line, so the mutation left that copy standing and the predicate did not fail | the same run | every mutation is now applied to the collapsed text the predicates read; all twelve contracts and their controls were re-measured in isolation before the confirming run |

## Discrepancies

None during execution. The two control-plane collisions were found by uncommitted dry runs, put to
the owner, and adjudicated by Amendments 1 and 2 before any execution commit existed; the amendments
record them. One observation is carried forward rather than recorded as a discrepancy: N13's
containment half will refuse the retirement round's deletions, which Amendment 2 already assigns to
that round to own and supersede.

**No frozen definition, target, negative case or authority rule was altered.**

## Definition slots

**Four definition slots, and four were fired**: `U1` the union resolver, `U2` the union derivation,
`U3` the authoritative validator with its keyed entry point `_si2_authority`, and `U4` the census
harness. `U5` fires no slot: it is `SI-1`'s `_si1_integrity` applied over the record set fixed at
stage 1. The synthetic repository and the negative suite are test code.

## Chronology

The property certified is the bootstrap one: **no commit reachable from the execution head lies
outside `B`'s descendants**, asked of the real `pull_request.head.sha`, never of the synthetic
merge, every commit of `git rev-list H ^B` required to descend from `B`, recovery included,
fail-closed — and not a call to `U3`, because `SI-2` has no record. The execution is five stage
commits and one final commit on `claude/si2-execution`, in the frozen order, each named in the
landing.

Every seal constant in the guard file is left exactly as `B` carries it, and the only change to the
record set is the one authorized addition. The three frozen blobs are unchanged. Act 21 remains
closed throughout and is not opened by any outcome here.

The claim is scoped to the repository record.
