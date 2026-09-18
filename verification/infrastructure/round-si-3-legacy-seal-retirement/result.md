# Seal infrastructure round SI-3 — the legacy seal retirement: RESULT

Executed from the mandated base `B` = `220827b89c038d98dbe643a53c72a8fd00ed8480`, the certified
merge commit of the preregistration pull request (#675, push run 35377254073), and from no other
commit. The execution's first act verified the **frozen preregistration blob** at `B`:
`e8e9be66de3a63963418a40189accfbb2c046a92`. `R7-SI3` pins it with its own drift control. The freeze
was measured against `B0` = `d89fff8abb20e2c63a33949b79947650bf47df6a`, `SI-2`'s landing, and the
guard file is the same blob at `B0` and at `B` — `163d3e1b6bd859d5c4eebafcbf37d4eaa9005b46` — so the
inventory the freeze measured is the inventory the execution deleted.

This round is **SEALING**. It lands `E` → `L` → `P`. It took ownership of the legacy seal state in
its freeze, for exactly the frozen inventory, and removed it; its `P` writes
`verification/seals/SI3.json` — `kind: "sealed"`, `base` = `B`, `sealed_head` = `E`, `merge` = `L` —
and writes no legacy constant: no `_SI3_BASE`, no `_SI3_SEALED_HEAD`, no `_SI3_MERGE`, not as `None`,
not at all, at any commit of the round. It installs no new authority. It is certified by `U3` as
`SI-2` left it, through the validator's prospective path, and by nothing it builds itself.

**What the round did.** It added `SI-2`'s `base-only` record and scoped the two closed rounds'
contracts to the records they manifested; built the one manifest accessor and rebound every
surviving read of a legacy constant through it; deleted the twenty-three shadow-ancestry functions,
the five per-round seal-integrity comparators and their recordings; deleted every legacy seal
assignment statement, so that the guard file carries zero and keeps the detector as a standing
contract; replaced the two live census re-measurements whose old side no longer exists with pinned
historical artifacts; and amended §A.37 so that the protocol states what the retirement left in
force. **`SI-1`'s and `SI-2`'s recorded outcomes are not edited**: their preregistrations,
amendments, result notes and censuses are byte-identical at the head, pinned by `R7-SI3`.

**`SI-3` is not Act 21**. It is the third seal-infrastructure round, after `SI-1` and `SI-2`, and it
states nothing about Act 21's targets, attestation span, ladder or rungs; Act 21's status is the
owner's and is unaffected by any outcome here. The first draft of this control plane, preserved
unmerged as #674, is not freeze evidence for `SI-3`.

## The inventory, reported against the freeze

The freeze fixed the deletion target as counts, and the execution reports the same counts by the
same measurements — `SI2-6`(b)'s statement extraction and the `tokenize`-based read census — at
each stage commit and at the final head.

| where | statements / names | genuine reads | shadow defs | comparators | `shadow=` calls | recordings |
|---|---|---|---|---|---|---|
| `B` (= `B0`'s guard blob) | **62 statements over 60 names** | **228 genuine identifier reads** | 23 | 5 | 23 | 8 |
| stage 1 | 62 / 60 | 222 | 23 | 5 | 23 | 8 |
| stage 2 | 62 / 60 | 182 | 23 | 5 | 23 | 8 |
| stage 3 | 62 / 60 | 6 | 0 | 0 | 0 | 0 |
| stage 4 | **0 / 0** | **0** | 0 | 0 | 0 | 0 |
| stages 5, 6 and `E` | 0 / 0 | 0 | 0 | 0 | 0 | 0 |

The 228 reads at `B` partition as the freeze said: 116 shadow-ancestry, 60 comparator, 52 other.
The 182 at stage 2 are the 116 and the 60 the shadow and comparator functions still carried, plus
six in `R7-RNT`'s clause-9 block; the six at stage 3 are that block's remaining reads, deleted with
it at stage 4 (see *Discrepancies*). Of the 52 *other* reads, forty-six were rebound through the
accessor or retired with their superseded contract at stages 1 and 2, and six were the clause-9
block's. String literals were left as they were: the freeze's non-gating count of `(STRING,
name)` pairs over the sixty names, 78 over 25 names at `B`, reproduces exactly by this round's
tokenization, and is 56 pairs over 23 names at the head; counting every legacy-shaped name rather
than the sixty gives 87 at `B` and 61 at the head. Neither count gates.

## Outcomes

| target | outcome | decided by |
|---|---|---|
| `SI3-0` | **`HOLD`** | fourteen pins and nine preconditions, read from git at `B` |
| `SI3-1` | **`RECORD-AS-AUTHORIZED`** | `SI2.json` exactly as authorized, in the byte shape of `SI1.json`; 24 records, 18 `sealed`, 6 `base-only`, fixed from stage 1 until `P`; `R7-SI2`'s chronology clause a keyed call to `U3` on `SI2.json`, `not-applicable` with the pinned base reachable |
| `SI3-2` | **`REBOUND`** | zero genuine identifier reads of any of the sixty names at the head, by the freeze's tokenization; every rebound read goes through `_seal_field` |
| `SI3-3` | **`SHADOWS-RETIRED`** | zero shadow functions, zero comparators, zero recordings, zero `shadow=` arguments; every keyed wrapper body the shadowless form; the stage-3 dry run every pre-existing tag `PASS` |
| `SI3-4` | **`RETIRED`** | zero legacy assignment statements by `SI2-6`(b)'s extraction, zero reads, the detector kept as a standing contract |
| `SI3-5` | **`ARCHIVED-AS-PINNED`** | `SI-1`'s `census.json` at `7a3e6288…` and `SI-2`'s at `d6b2e505…`, each pinned by its existing blob identity with a one-byte drift control, labelled in the guard a certified historical measurement |
| `SI3-6` | **`PROTOCOL-UPDATED`** | §A.37's amended subsection and its new closing subsection; `SI2-7` still holds on the amended text |
| `SI3-7` | **`MAP-PRESERVED`** | the base's guard file run at `B` in a detached temporary worktree: 92 tags, all `PASS`, and the head returns the same verdict on every one |

**The stages were run in the frozen order, and the order was gating**: stage 1 was one commit,
atomic, and its dry run was all-`PASS` before stage 2 existed; stage 2's dry run was all-`PASS`
before stage 3 was committed; stage 3's dry run was all-`PASS` before stage 4 was committed; stage 4's
dry run was taken before stage 5, and stages 5 and 6 followed with all-`PASS` dry runs of their own.
Each stage is its own commit on the execution branch, and **the final head `E` is the checkpoint**:
`SI3-7` is measured by `R7-SI3` on every run at the commit that carries the whole retirement.

## `SI3-0` — locating controls

The fourteen blobs of the freeze's start-state table hold at `B`, including the guard file at
`163d3e1b…`, `AGENTS.md` at `a28449d1…`, `SI1.json` at `9cefa200…` and the seals tree at
`e4fb69db…`. The nine preconditions hold at `B`: no `R7-SI3` and no `_SI3` in the guard file;
twenty-three records, eighteen `sealed`, five `base-only`, no `SI2` and no `SI3`; 62 statements over
60 names, 23 shadow definitions, 5 comparators, 23 keyed `shadow=` calls, 8 recordings; the base's
guard file passing 92 tags; `B0`'s parents `df54b99d…` and `df2fab57…` with `B0` on `B`'s
first-parent spine; §A.37 still saying the constants "remain **PROTECTED HISTORICAL SEAL
STATE**"; `_si1_validate` accepting `prospective` and `_si2_validate` passing it through, neither
edited by this round; `SI2.json` absent and `_SI2_BASE` exactly `df54b99d…`. Outcome `HOLD`.

## `SI3-1` — `SI-2`'s record, first and then fixed

Stage 1 is one commit, `bbf68e495b3362c1f9bbfced96dc77239a9505b8`. It added
`verification/seals/SI2.json` — `{"round": "SI2", "kind": "base-only", "base":
"df54b99dba99dc043b11752163d8d348c9e54472"}`, transcribing the constant it retires — and, in the
same commit, everything the freeze said a twenty-fourth record requires: `R3`, the round-declared
baseline, with `B`'s seals tree and the authorized stems `SI2` and `SI3`; the second authorized
wiring edit, `_si2_manifest_at_stage1` reading `R3`; `R7-SI1`'s scoped-integrity contract
generalized to the closed-round rule, so that records outside the twenty-two it transcribed are
reported and gate nothing there; `R7-SI2`'s record-count contracts, its census input and its `#140`
probe scoped to `_SI2_MANIFESTED`; `_si2_guard_edits_bounded` retired with its three call lines;
`R7-SI2`'s chronology clause rewritten as `return _si2_authority('SI2', tag='R7-SI2')`; and `SI-2`'s
negative cases 11 and 13 retired, leaving cases 1–8 and 12, nine, in force.

The stage's first dry run failed `R7-SI2` on two clauses this round's own patch had missed —
`SI2-4`'s census input and `SI2-8`'s `#140` probe were still handed all twenty-four records — both
named in the supersession table's "twenty-three-record contracts" row; the scoping was added to the
same uncommitted stage and the rerun was all-`PASS`, 92 tags. Recorded as an execution defect, not a
discrepancy: the table authorized it and the patch had omitted it. From stage 1 to `E` the record set
is twenty-four and `U5` under `R3` reports nothing mutated, removed or added. Outcome
`RECORD-AS-AUTHORIZED`.

## `SI3-2` — every remaining read goes through the accessor

Stage 2, `124ccc66810e1728915f18be49e79f3c8dbe23c4`, built `R1` — `_seal_field(stem, field)`, one
function returning one field of one record read through `_si1_load` and nothing else, failing
closed on a missing record, a missing field or a schema failure with a sentinel that equals no
literal, and `_seal_triple(stem)` over it — and declared `R2`, `_MANIFEST_PROSPECTIVE`, holding
exactly `{'SI3': B}`, outside both marker-bounded regions, with the first authorized wiring edit
handing it to `_si2_validate` as `prospective`. Every *other*-class read was then rebound or
retired per the table: `R7-HYE`'s seal-state function, its untouched-seals contract and its two
mutation controls read `_seal_triple('HYA')`, `_seal_triple('HYB')`, `_seal_triple('HYE')` and
`_seal_field('HYE', 'base')` against the same literals; `R7-PC4S`'s round-1 seal reads
`_seal_field('PC4', …)`; `R7-SI1`'s tag-map comparison and forbidden-paths control read
`_seal_field('SI1', 'base')`, its `SI1` record literal carries `99ab6370…` as the record does, and
N13 — `_si1_seal_constants_intact`, as Amendment 2 of `SI-2` said this round must own — is retired
with its gate line and its two-element allowance fragment; `R7-SI2`'s fifteen reads of `_SI2_BASE`
as a revision read `_seal_field('SI2', 'base')`. The stage's dry run was all-`PASS`, 92 tags, which
is the rebinding rule holding: the same literals, the same verdicts.

At the stage-2 commit six genuine reads remained outside the shadow and comparator functions, all
inside `R7-RNT`'s clause-9 block, whose disposition in the table is deletion and not rebinding;
they went with the block (see *Discrepancies*). At the head the tokenization finds zero reads of
any of the sixty names. Outcome `REBOUND`.

## `SI3-3` — the shadows are gone and nothing gated on them

Stage 3, `e08bf0f0550af19ee48435c9d58bd3b330ff871e`, deleted the twenty-three
`_<stem>_legacy_ancestry` functions, the five `_<stem>_prior_seals` comparators, the eight
`_si2_shadow_integrity` recording lines, the `TCF`/`RNC`/`TRJ` fabrication controls and the
`XTS`/`RNT` comparison loops, and made the twenty-three keyed calls shadowless: each wrapper body is
exactly `return _si2_authority('<STEM>', tag='R7-<STEM>')`, and `_si2_clause_gates_on_u3` now
requires that form. `SI2-3`'s measurement was replaced by its shadowless form as the table says —
twenty-three clauses gate on `U3`, zero on a legacy constant, zero shadow reads, the shadow-forced
controls unchanged on all twenty-three, eighteen `sealed` verdicts — and `SI2-5`'s eight recorded
comparator verdicts became a requirement that the recording list be empty.

**The verdict map was unchanged by the removal.** The stage's dry run was all-`PASS`, 92 tags,
every pre-existing tag returning the verdict it returned at `B`; no tag was gating on a shadow,
which is what `SI2-3` claimed and what this stage proves. Outcome `SHADOWS-RETIRED`, the freeze's
MEDIUM-strength prediction.

## `SI3-4` — the representation is gone

Stage 4, `a10a6cfd58e92379a0748500a16058b4cd4b1d4d`, deleted the sixty-two statements, asserting the
count before the edit and zero after it, `R7-RNT`'s clause-9 block going with them as a block (its
two rebindings were two of the sixty-two). `SI2-6`(b), `LEGACY-INTACT`, is retired per the table and
prints the head's statement count; its extraction is `R7-SI3`'s standing detector, mutation-tested
by re-adding one statement of each shape. The stage's dry run, taken before stage 5 as the freeze
orders and not required to be all-`PASS`, was 91 `PASS` and one `FAIL`: `R7-SI2` on `SI2-4` alone —
`DELTA-BROKEN`, 0 of 23 records agreeing and the census artifact `STALE` — because `U4`'s old side
transcribes the head's guard text and the head now carries no constant. That is the failure the
freeze assigned to stage 5 to replace. Every other clause of `R7-SI2` held, `SI2-6`(a) included:
`MAP-PRESERVED`, the base's 91 tags identical at the stage-4 head.

`R7-SI1` passed entire at stage 4, `SI1-5` included. The freeze's reason for retiring `SI1-5` was
that its old side read the constants; the measurement shows it did not — `SI-1`'s census harness
ran the generic archive-mode and quiet-ancestry helpers on each record's own fields, and its
control census ran them on synthetic repositories — so the `SI-1` census still reproduced after
every constant was gone. The disposition the table fixed is executed unchanged at stage 5, because
the table is the authorization and the design it records — a pinned historical artifact, never
re-measured — was adjudicated on its own terms; the mechanism is recorded here as a finding about
the freeze's reasoning, not as a discrepancy in what was done. Outcome `RETIRED`.

## `SI3-5` — the archived measurements

Stage 5, `03e94be29c911fcd1a0408b7236dd043a5de8e79`, replaced — not silently deleted — `SI1-5` and
`SI2-4`. Each is now an artifact-integrity check: `SI-1`'s `census.json` pinned at
`7a3e6288c5f532a849a07beb9a8e5757cdf79d04` and `SI-2`'s at `d6b2e505da8bb816179a822258d6672b79670155`,
the blob identities they have carried since their rounds landed, each with a one-byte drift control
that must reject, each labelled in its guard as a certified historical measurement of that round's
checkpoint under that round's rule, whose retired side no longer exists and which is not
re-measured. The four harness functions that ran the retired side — `_si1_census`,
`_si1_control_census`, `_si2_census`, `_si2_control_census` — are deleted with the clauses that
called them. Every `U3`-side measurement keeps running: the schema, the three states, `SI-1`'s
twenty negative cases and `SI-2`'s nine, the tag-map comparisons that run historical guard files
from git, `#140` and `#141`'s restatements over the scoped record set. Only the retired-side
comparison ceases to be reproducible.

The two censuses are **certified historical measurements of their rounds' checkpoints** — `SI-1`'s
`CENSUS-DIVERGENT` agreement census over twenty-two records and twenty-one controls, `SI-2`'s
`DELTA-AS-ADJUDICATED` profile over twenty-three — and they are never read as current evidence
about any later head; no old/new equivalence is claimed after retirement, because the old side can
no longer be run to say anything. The stage's dry run was all-`PASS`, 92 tags. Outcome
`ARCHIVED-AS-PINNED`.

## `SI3-6` — the protocol

Stage 6, `962fdce606335605da2aaf7c117586166f7e0d8c`, amended `AGENTS.md` §A.37's *Sealing through the
manifest* subsection prospectively. `SI2-7`'s two halves are kept as history in the past tense —
every phrase `R7-SI2`'s protocol contract reads is still present, and the contract still passes —
and the sentence precondition 7 names, that the constants *remain* protected historical seal state,
is superseded in place: they *remained* so until `SI-3`'s landing, and `SI-3` took that ownership
prospectively and removed them. A new closing subsection, *The representation retired, from
`SI-3`'s landing*, governs rounds begun after that landing and states: that the legacy
representation is retired — no constant, no shadow, no per-round comparison — and that a round
writing any of them fails the zero-statement standing contract and has recreated the representation
that was retired, every seal-state read going through the manifest accessor; how a sealing round
carries its base while it executes, through the prospective declaration, classified `EXECUTION`
and then `LANDED-PENDING-PIN`, with `P` removing the entry when it writes the record and a stem both
declared and recorded a failure; how manifest integrity is declared, each round's guard declaring
its own baseline and no round's hard-coding another's; that a closed round's contracts are read
over the records it manifested, stated once for every round after; and that the censuses are
history. Outcome `PROTOCOL-UPDATED`.

## `SI3-7` — the verdict map is preserved

`R7-SI3` runs the base's guard file — the blob `163d3e1b…` — at `B` in a detached temporary
worktree with every git and pull-request environment variable removed, exactly as `SI2-6`(a) runs
its base, and compares its tag-to-verdict map in process with the head's: 92 tags at the base, all
`PASS`, and the head returns the same verdict on every one of them. The head adds one tag,
`R7-SI3`, and changes no pre-existing verdict. The map is persisted as `si3-tagmap.json` beside this
note and compared with the recorded bytes on every run. Outcome `MAP-PRESERVED`, the freeze's other
MEDIUM-strength prediction; no changed verdict was seen at any stage on any pre-existing tag, so
nothing was ever a candidate for being adopted as an improvement.

**The nested cost, counted.** One run of the guard file at `E` is **eight executions of the guard
file per run**: the head; `R7-SI1`'s base; `R7-SI2`'s base and, inside it, its `SI-1` base; and
`R7-SI3`'s base and, inside it, that base's `SI-1` run and its `SI-2` run with its own `SI-1` run.
None is optimized away. The wall-clock cost of one complete run at `E` on the execution machine is
recorded in the *Chronology* section.

## The chronology, and the prospective path in vivo

`R7-SI3`'s chronology clause is `_si2_authority('SI3', tag='R7-SI3')`: a keyed call to `U3` on stem
`SI3`, which has no record while the round executes. `R2` supplies the base, and **the prospective
path classified this round in vivo** — the path `SI-1` built and no live round had used. At every
execution commit `U3` classified `SI3` as `EXECUTION` against `B` by act 10's strengthened check,
asked of the real head: the base an ancestor, every commit of `rev-list HEAD ^B` a descendant of
the base, recovery included, fail-closed. At `L` the same path classifies the round
`LANDED-PENDING-PIN`, permitted, "the seal record is still owed", the resolved target being `L`
itself; a head descending from `L` before `P` fails as seal pending. At `P`, with `SI3.json`
written and the `SI3` entry removed from `R2`, `U3` classifies the round `ARCHIVED` from its record
alone, re-derives `L` from `E` over the union of the event's visibility targets, and requires the
derived landing to equal the pinned one; a stem both declared and recorded fails. Negative cases 8
and 9 exercise exactly these two transitions on a synthetic repository in every run, and the
exact-`L` and exact-`P` CI runs are the live record of them.

## The supersession table, and what stands in its place

Under §A.37's ownership rule, **the supersession table is the authorization**: every frozen `SI-1`
and `SI-2` contract the retirement fails is named there with its disposition, and nothing outside
the table was touched in
`R7-SI1`, `R7-SI2` or the `SI2-AUTHORITY` region. Executed row by row: `R7-SI1`'s N2 shadow deleted
with the keyed call unchanged; N13 retired, as Amendment 2 assigned; `SI1-5` replaced by the pin;
`SI1-6` and the forbidden-paths control rebound; the `SI1` record literal; `R7-SI2`'s chronology
clause a keyed call with case 11 retired; `R7-SI1`'s scoped-integrity contract generalized at stage
1; `_si2_guard_edits_bounded` retired at stage 1; the twenty-three-record contracts scoped to
`_SI2_MANIFESTED`; case 13 retired with N13; the two authorized wiring edits inside
`SI2-AUTHORITY`, bounded by negative case 14 — the region at the head with exactly those two edits
reverted equals the region at `B`, differs before reverting, and carries no round stem;
`SI2-3` replaced by its shadowless form; `SI2-4` replaced by the pin; `SI2-5`'s recorded shadows
retired; `SI2-6`(b) retired with its extraction kept; every `_SI2_BASE` revision read rebound;
`R7-RNT`'s clause-9 block deleted; `R7-HYE` and `R7-PC4S` rebound with the same literals and the
same verdicts; the eight `ok_<x> &= _si2_integrity_ok()` lines unchanged in text with `U5` reading
`R3`. No failure outside the table occurred at any stage: the only failures seen — stage 1's first
run, stage 3's first run, stage 4's expected `SI2-4` — were each inside a named row.

## The negative suite

`SI-1`'s twenty cases and `SI-2`'s cases 1–8 and 12 run in every run, unchanged. Of this round's
fourteen, each is executable in `R7-SI3` and satisfies its named outcome for its named reason: one
statement of any shape re-added fails `SI3-4`'s detector (1); a shadow function retained or a
`shadow=` argument re-added fails `SI3-3` (2); a comparator or a recording call retained fails
`SI3-3` (3); a genuine read of any of the sixty names fails `SI3-2`, and the same name inside a
string literal does not (4); `SI2.json` absent, or carrying `sealed_head` or `merge` even as null,
fails `SI3-1` (5); a twenty-fifth record before `P` fails `U5` under `R3` as an unauthorized
addition (6); the declaration present beside `SI3.json` fails as declared-and-recorded (7); a
synthetic head descending from an unpinned landing fails as seal pending while the landing itself
is `LANDED-PENDING-PIN` (8); at a synthetic `P`, `sealed_head` not the landing's second parent, or
`merge` not the derived landing, fails (9); a rebinding that changed a pre-existing verdict is
`MAP-CHANGED`, measured by `SI3-7` (10); one byte changed in a pinned census fails the drift control
(11); §A.37 still saying the constants "remain" protected fails `SI3-6` (12); `R1` asked for a
missing record's field or a `base-only` record's `sealed_head` returns the fail-closed sentinel,
never a default (13); the `SI2-AUTHORITY` region differing from `B`'s by anything beyond the two
wiring edits fails, and a round stem in the region fails `_si2_region_no_stem` (14).

## Predictions against outcomes

| target | predicted | outcome | scored |
|---|---|---|---|
| `SI3-0` | `HOLD`, HIGH | `HOLD` | as predicted |
| `SI3-1` | `RECORD-AS-AUTHORIZED`, HIGH | `RECORD-AS-AUTHORIZED` | as predicted |
| `SI3-2` | `REBOUND`, HIGH | `REBOUND` | as predicted at the head; six reads outlived the stage inside the block the table deletes |
| `SI3-3` | **`SHADOWS-RETIRED`**, MEDIUM | **`SHADOWS-RETIRED`** | as predicted; no tag moved when the shadows went, so `SI-2`'s measurement missed no read |
| `SI3-4` | `RETIRED`, HIGH | **`RETIRED`** | as predicted; a count |
| `SI3-5` | `ARCHIVED-AS-PINNED`, HIGH | `ARCHIVED-AS-PINNED` | as predicted |
| `SI3-6` | `PROTOCOL-UPDATED`, HIGH | `PROTOCOL-UPDATED` | as predicted |
| `SI3-7` | **`MAP-PRESERVED`**, MEDIUM | **`MAP-PRESERVED`** | as predicted; no pre-existing verdict changed at any stage |

No prediction was missed. The freeze put its two sharpest claims at MEDIUM and both held.

## Execution defects, corrected — held apart from the findings

Five were in this round's own implementation, not in the freeze, and none is counted as a
discrepancy. The last was found by the first complete run of the finished guard, which reported
every other target's outcome as predicted.

| # | defect | how it showed | corrected by |
|---|---|---|---|
| 1 | the stage-1 patch scoped `R7-SI2`'s record-count contracts and `_si2_manifest_now` to `_SI2_MANIFESTED` but not `SI2-4`'s census input or `SI2-8`'s `#140` probe, both twenty-three-record contracts the table's row names | the stage's first dry run: `SI2-4` `DELTA-BROKEN` with 24 of 24 agreeing, `SI2-8` over 24 records | the scoping added to the same uncommitted stage; rerun all-`PASS`, then committed |
| 2 | the stage-3 patch deleted `R7-RNT`'s clause-9 block whole, its two rebindings included, while `SI2-6`(b) — retired only at stage 4 — still required sixty-one statements identical to `B0`'s | the stage's first dry run: `SI2-6`(b) `LEGACY-ALTERED`, 59 statements | the two rebindings, probe and restore lines restored without the comparator; rerun all-`PASS`; the remainder deleted at stage 4 — the sequencing is recorded under *Discrepancies* |
| 3 | the guard-insertion script held the guard's text inside a triple-single-quoted string, and the guard's own region-edit tuple uses the same delimiter | the script failed to parse before touching the file | the guard text carried in its own file and inserted verbatim |
| 4 | the note's discrepancy contract was first written for one discrepancy before the stage-3/4 sequencing was recognized as a second | caught while writing this note, before the guard's first run | the contract reads the count this section states |
| 5 | `SI3-3`'s negative case 2 re-adds a `shadow=` argument by writing the keyed call's shadowed form as one string literal, and the check that the file carries no `shadow=` argument is a regular expression over the whole file, which then matched the guard's own source — `SI-2`'s defect 7 in a new place | the first complete run: every other outcome as predicted, `SI3-3` reporting `SHADOWS-PARTIAL` with zero shadow functions, zero comparators, zero recordings and every clause shadowless | the literal is assembled from two fragments so the file carries the form nowhere; the check is unchanged |

## Discrepancies

There are **two discrepancies** between the freeze and the execution, both recorded and neither
adjudicated away:

1. `_si2_shadow_integrity` and `_SI2_SHADOW_INTEGRITY` are **retained inside the region with no
   caller**. The freeze's function table lists them for deletion, but both are defined inside the
   `SI2-AUTHORITY` region, and negative case 14 bounds that region to exactly the two authorized
   wiring edits. The two rules conflict on this one function and one list; the bound was kept and
   the deletion was not made. Every one of the eight call sites is deleted, `SI3-3` requires zero
   calls and `SI2-5` requires the list empty, so the retained definition records nothing and gates
   nothing; it is dead text inside a region this round was told not to edit further.
2. `R7-RNT`'s clause-9 block was deleted **across stages 3 and 4**, not as a block at stage 3. The
   stage table puts the block's deletion at stage 3, and stage 4 may not begin until stage 3's dry
   run has every pre-existing tag `PASS`; but `SI2-6`(b), retired only at stage 4, holds the
   sixty-one statements identical to `B0`'s, and two of them are the block's rebindings. The
   freeze's stage table and its gating condition cannot both be satisfied by a stage-3 deletion of
   the whole block. The comparator-bearing lines went at stage 3 and the two rebindings, the probe
   and the restore lines went at stage 4 with the other sixty statements; H1's trap — a pin removed
   with the rebinding kept — did not arise, because at no commit was a rebinding present without its
   pin, and the statement count was 62 at every commit before stage 4 and 0 from it.

Two further observations are findings, not discrepancies, because the frozen disposition was
executed unchanged: `SI1-5` still reproduced at stage 4, its old side never having read a constant
(recorded under `SI3-4`); and six *other*-class reads outlived stage 2 inside the block the table
assigns to deletion (recorded under `SI3-2`).

**No frozen definition, target, negative case or authority rule was altered.** `U1`–`U5` are
unchanged in semantics; the `SI1-VALIDATOR` region is unedited and `_si2_region_relocated_verbatim`
still holds against it; the `SI2-AUTHORITY` region differs from `B`'s by the two wiring edits and
nothing else.

## Definition slots

**Three definition slots, and three were fired**: `R1` the manifest accessor, `_seal_field` with
`_seal_triple` over it; `R2` the prospective declaration, `_MANIFEST_PROSPECTIVE`; `R3` the
round-declared baseline, `_MANIFEST_BASELINE`. All three are declared outside both marker-bounded
regions, before the first keyed clause runs, and none carries a round stem in its name. The
`R7-SI3` guard, its negative suite and the base run are test code.

## Chronology

The execution is six stage commits and one final commit on `claude/si3-execution`, in the frozen
order, each named above, branching from `B` and from nothing else. The property certified is act
10's strengthened one, asked of the real pull-request head and reached through `U3`'s prospective
path: `EXECUTION` at every commit of the round, `LANDED-PENDING-PIN` at `L`, `ARCHIVED` at `P`. One
complete run of the guard file at `E` on the execution machine, eight executions counted, took
about 164 seconds of wall-clock time, against about 82 seconds for a run at the stage-6 commit
before `R7-SI3` existed; the base's guard file was also run at `SI-2`'s base on every one of the
round's dry runs from stage 1 on, by `SI2-6`(a).

The record set is twenty-four from stage 1 to `E`, and the only change `P` makes is the one
authorized addition and the removal of the declaration. The fourteen frozen blobs are unchanged.
Act 21 is neither opened nor closed by any outcome here.

The claim is scoped to the repository record.
