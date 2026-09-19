# Seal infrastructure round SI-3 — the legacy seal retirement: RESULT

Executed from the mandated base `B` = `b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5`, the certified
merge commit of Amendment 1 (#676, push run 35407019610), and from no other commit. The execution's
first act verified **both frozen blobs** at `B`: the preregistration
`e8e9be66de3a63963418a40189accfbb2c046a92` and Amendment 1 `0087dceddc2c8d7f497c38937d659e78de59a1f6`.
`R7-SI3` pins both, each with its own drift control. The freeze was measured against `B0` =
`d89fff8abb20e2c63a33949b79947650bf47df6a`, `SI-2`'s landing, and the guard file is the same blob at
`B0`, at the preregistration merge `220827b8` and at `B` — `163d3e1b6bd859d5c4eebafcbf37d4eaa9005b46` —
so the inventory the freeze measured is the inventory this execution deleted.

This round is **SEALING**. It lands `E` → `L` → `P`. It took ownership of the legacy seal state in
its freeze, for exactly the frozen inventory, and removed it; its `P` writes
`verification/seals/SI3.json` — `kind: "sealed"`, `base` = `B`, `sealed_head` = `E`, `merge` = `L` —
and writes no legacy constant: no `_SI3_BASE`, no `_SI3_SEALED_HEAD`, no `_SI3_MERGE`, not as `None`,
not at all, at any commit of the round. It installs no new authority. It is certified by `U3` as
`SI-2` left it, through the validator's prospective path, and by nothing it builds itself.

**This is execution attempt 2.** Attempt 1, `76bf328a19c7354cbb0a120b4a374c16369aa1a1` on
`claude/si3-execution`, ran the six frozen stages from the preregistration merge `220827b8` and
ended green at 93 tags, and is **non-certifying**: it exposed three contradictions inside the freeze
that it had resolved implicitly, and a green guard does not prove conformity to a control plane that
contradicts itself. Amendment 1 records it and resolves the three contradictions prospectively;
nothing from attempt 1 is result evidence here, no commit of it is reachable from this branch, and
every measurement below was taken afresh on this branch.

**What the round did.** It added `SI-2`'s `base-only` record and scoped the two closed rounds'
contracts to the records they manifested; built the one manifest accessor and rebound every read of
a legacy constant through it; deleted the twenty-three shadow-ancestry functions, the five
per-round seal-integrity comparators, their recordings and, under Amendment 1, the recorder and its
list inside the generic region; deleted every legacy seal assignment statement, so that the guard
file carries zero and keeps the detector as a standing contract; replaced the two live census
re-measurements whose old side no longer exists with pinned historical artifacts; and amended §A.37
so that the protocol states what the retirement left in force. **`SI-1`'s and `SI-2`'s recorded
outcomes are not edited**: their preregistrations, amendments, result notes and censuses are
byte-identical at the head, pinned by `R7-SI3`.

**`SI-3` is not Act 21**. It is the third seal-infrastructure round, after `SI-1` and `SI-2`, and it
states nothing about Act 21's targets, attestation span, ladder or rungs; Act 21's status is the
owner's and is unaffected by any outcome here.

## The stage commits

| commit | content |
|---|---|
| `35b0555eeadf3de133d0231e510d84444abc12d9` | stage 1 |
| `11a80ee8f0c7e88be08c4e3955c5d4f4f967a80a` | stage 2 |
| `c7901683ce5018efbc9471c393de8809c86831ce` | stage 3 |
| `f3279450af9df7512792921af1ba9cf08d24ffd8` | stage 4 |
| `a0887379a76700c946e0820cd17e738c56e5b01f` | stage 5 |
| `81aa7acb4f743b0302f9dee9ea0213828d9b572f` | stage 6 |

`R7-SI3` reads this table and measures Amendment 1's residue bound at each commit from git, so the
table is a contract and not a narrative.

## The inventory, reported against the freeze

The freeze fixed the deletion target as counts, and the execution reports the same counts by the
same measurements — `SI2-6`(b)'s statement extraction and the `tokenize`-based read census — at
each stage commit and at the final head. The last two columns are Amendment 1 point 3's bound:
genuine reads **outside** the shadow and comparator functions, and whether every such read lies on
the enumerated residue's lines.

| where | statements / names | genuine reads | shadow defs | comparators | recordings | reads outside the machinery | on residue lines only |
|---|---|---|---|---|---|---|---|
| `B` (guard blob `163d3e1b…`) | **62 statements over 60 names** | **228 genuine identifier reads** | 23 | 5 | 8 | 52 | no (unbounded here) |
| stage 1 | 62 / 60 | 222 | 23 | 5 | 8 | 46 | no (unbounded here) |
| stage 2 | 62 / 60 | 182 | 23 | 5 | 8 | **6** | **yes** |
| stage 3 | 62 / 60 | 6 | 0 | 0 | 0 | **6** | **yes** |
| stage 4 | **0 / 0** | **0** | 0 | 0 | 0 | 0 | — |
| stages 5, 6 and `E` | 0 / 0 | 0 | 0 | 0 | 0 | 0 | — |

The 228 reads at `B` partition as the freeze said: 116 shadow-ancestry, 60 comparator, 52 other. Of
the 52 *other* reads, forty-six were rebound through the accessor or retired with their superseded
contract at stages 1 and 2, and six are the enumerated residue of `R7-RNT`'s clause-9 block, which
Amendment 1 schedules for deletion at stage 4. At the stage-2 and stage-3 commits the reads outside
the machinery number **exactly six**, all on the residue's seven lines and nowhere else, and they
are not counted as rebound; from stage 4 they number zero. String literals were left as they were:
the freeze's non-gating count of `(STRING, name)` pairs over the sixty names, 78 over 25 names at
`B`, reproduces exactly by this round's tokenization, and is 72 pairs over 24 names at the head,
the guard now quoting the residue's lines; counting every legacy-shaped name rather than the sixty
gives 87 at `B` and 77 at the head. Neither count gates.

## Outcomes

| target | outcome | decided by |
|---|---|---|
| `SI3-0` | **`HOLD`** | the fourteen pins, both frozen blobs, and the twelve preconditions, read from git at `B` |
| `SI3-1` | **`RECORD-AS-AUTHORIZED`** | `SI2.json` exactly as authorized, in the byte shape of `SI1.json`; 24 records, 18 `sealed`, 6 `base-only`, fixed from stage 1 until `P`; `R7-SI2`'s chronology clause a keyed call to `U3` on `SI2.json` |
| `SI3-2` | **`REBOUND`** | zero genuine reads at the head, and Amendment 1's residue bound holding at every stage commit: six on the residue lines at stages 2 and 3, zero from stage 4 |
| `SI3-3` | **`SHADOWS-RETIRED`** | zero shadow functions, zero comparators, zero recordings, no recorder, zero `shadow=` arguments; every keyed wrapper body the shadowless form; the stage-3 dry run every pre-existing tag `PASS` |
| `SI3-4` | **`RETIRED`** | zero legacy assignment statements by `SI2-6`(b)'s extraction, zero reads, the detector kept as a standing contract |
| `SI3-5` | **`ARCHIVED-AS-PINNED`** | `SI-1`'s `census.json` at `7a3e6288…` and `SI-2`'s at `d6b2e505…`, each pinned by its existing blob identity with a one-byte drift control |
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
`e4fb69db…`; both frozen blobs hold. The nine frozen preconditions hold at `B`, and so do Amendment
1's three: `B`'s parents are `220827b8` and `51f9d63d`, the preregistration merge and the
amendment's reviewed head; the two dead objects and the seven residue lines are present at `B`
exactly as enumerated; and attempt 1's head is not reachable from this branch. Outcome `HOLD`.

## `SI3-1` — `SI-2`'s record, first and then fixed

Stage 1 is one commit. It added `verification/seals/SI2.json` — `{"round": "SI2", "kind":
"base-only", "base": "df54b99dba99dc043b11752163d8d348c9e54472"}`, transcribing the constant it
retires — and, in the same commit, everything the freeze said a twenty-fourth record requires: `R3`,
the round-declared baseline, with `B`'s seals tree and the authorized stems `SI2` and `SI3`; the
second authorized wiring edit, `_si2_manifest_at_stage1` reading `R3`; `R7-SI1`'s scoped-integrity
contract generalized to the closed-round rule; `R7-SI2`'s record-count contracts, its census input
and its `#140` probe scoped to `_SI2_MANIFESTED`; `_si2_guard_edits_bounded` retired with its three
call lines; `R7-SI2`'s chronology clause rewritten as `return _si2_authority('SI2', tag='R7-SI2')`;
and `SI-2`'s negative cases 11 and 13 retired, leaving cases 1–8 and 12 in force. From stage 1 to
`E` the record set is twenty-four and `U5` under `R3` reports nothing mutated, removed or added.
Outcome `RECORD-AS-AUTHORIZED`.

## `SI3-2` — every remaining read goes through the accessor

Stage 2 built `R1` — `_seal_field(stem, field)`, one function returning one field of one record
read through `_si1_load` and nothing else, failing closed on a missing record, a missing field or a
schema failure with a sentinel that equals no literal, and `_seal_triple(stem)` over it — and
declared `R2`, `_MANIFEST_PROSPECTIVE`, holding exactly `{'SI3': B}`, outside both marker-bounded
regions, with the first authorized wiring edit handing it to `_si2_validate` as `prospective`. Every
*other*-class read whose disposition at stage 2 is rebinding or retirement was then rebound or
retired per the table: `R7-HYE`'s seal-state function, its untouched-seals contract and its two
mutation controls read `_seal_triple('HYA')`, `_seal_triple('HYB')`, `_seal_triple('HYE')` and
`_seal_field('HYE', 'base')` against the same literals; `R7-PC4S`'s round-1 seal reads
`_seal_field('PC4', …)`; `R7-SI1`'s tag-map comparison and forbidden-paths control read
`_seal_field('SI1', 'base')`, its `SI1` record literal carries `99ab6370…` as the record does, and
N13 — `_si1_seal_constants_intact`, as Amendment 2 of `SI-2` said this round must own — is retired
with its gate line and its allowance fragments; `R7-SI2`'s fifteen reads of `_SI2_BASE` as a
revision read `_seal_field('SI2', 'base')`. The stage's dry run was all-`PASS`, 92 tags, which is
the rebinding rule holding: the same literals, the same verdicts.

Under Amendment 1 point 3 the six residue reads are the whole of the exception: **exactly six**
reads outside the shadow and comparator functions at the stage-2 commit and again at the stage-3
commit, all on the residue's lines, not counted as rebound, and zero from the stage-4 commit on.
`R7-SI3` measures that bound from git at each stage commit named above, and its negative case 16
shows that a seventh read, or a read off the residue's lines, fails it. Outcome `REBOUND`.

## `SI3-3` — the shadows are gone and nothing gated on them

Stage 3 deleted the twenty-three `_<stem>_legacy_ancestry` functions, the five
`_<stem>_prior_seals` comparators, the eight `_si2_shadow_integrity` recording lines, the
`TCF`/`RNC`/`TRJ` fabrication controls and the `XTS`/`RNT` comparison loops, and made the
twenty-three keyed calls shadowless: each wrapper body is exactly
`return _si2_authority('<STEM>', tag='R7-<STEM>')`, and `_si2_clause_gates_on_u3` now requires that
form. Under Amendment 1 point 1 it also deleted the two dead objects inside the `SI2-AUTHORITY`
region, `_SI2_SHADOW_INTEGRITY` and `def _si2_shadow_integrity`, so that the function inventory's
row is executed as written; the region at the head, with the two wiring edits reverted, equals the
base's region with exactly those two definitions excised, and negative case 15 shows that
reinstating either fails the bound. Under point 2, `R7-RNT`'s clause-9 block lost its
comparator-bearing logic and calls and kept the enumerated residue. `SI2-3`'s measurement was
replaced by its shadowless form as the table says — twenty-three clauses gate on `U3`, zero on a
legacy constant, zero shadow reads, the shadow-forced controls unchanged on all twenty-three,
eighteen `sealed` verdicts — and `SI2-5`'s eight recorded comparator verdicts became a requirement
that no recording call and no recorder remain.

**The verdict map was unchanged by the removal.** The stage's dry run was all-`PASS`, 92 tags,
`SI2-6`(b) `LEGACY-INTACT` at 61, every pre-existing tag returning the verdict it returned at `B`;
no tag was gating on a shadow, which is what `SI2-3` claimed and what this stage proves. Outcome
`SHADOWS-RETIRED`, the freeze's MEDIUM-strength prediction.

## `SI3-4` — the representation is gone

Stage 4 deleted the sixty-two statements, asserting the count before the edit and zero after it,
and with them the residue, its two rebindings among the sixty-two; at no commit of the round was a
rebinding present without its pin, and the statement count was 62 at every commit before stage 4
and 0 from it. `SI2-6`(b), `LEGACY-INTACT`, is retired per the table and prints the head's
statement count; its extraction is `R7-SI3`'s standing detector, mutation-tested by re-adding one
statement. The stage's dry run, taken before stage 5 as the freeze orders and not required to be
all-`PASS`, was 91 `PASS` and one `FAIL`: `R7-SI2` on `SI2-4` alone — `DELTA-BROKEN`, 0 of 23
records agreeing and the census artifact `STALE` — because `U4`'s old side transcribes the head's
guard text and the head now carries no constant. That is the failure the freeze assigned to stage 5
to replace. Every other clause of `R7-SI2` held, `SI2-6`(a) included: `MAP-PRESERVED`, the base's
91 tags identical at the stage-4 head. `R7-SI1` passed entire, `SI1-5` included: as Amendment 1
records, `SI-1`'s census harness ran the generic helpers on each record's own fields and never read
a constant, so the freeze's stated reason for retiring `SI1-5` was wrong in mechanism while its
disposition, executed unchanged at stage 5, stands as adjudicated. Outcome `RETIRED`.

## `SI3-5` — the archived measurements

Stage 5 replaced — not silently deleted — `SI1-5` and `SI2-4`. Each is now an artifact-integrity
check: `SI-1`'s `census.json` pinned at `7a3e6288c5f532a849a07beb9a8e5757cdf79d04` and `SI-2`'s at
`d6b2e505da8bb816179a822258d6672b79670155`, the blob identities they have carried since their rounds
landed, each with a one-byte drift control that must reject, each labelled in its guard as a
certified historical measurement of that round's checkpoint under that round's rule, whose retired
side no longer exists and which is not re-measured. The four harness functions that ran the retired
side — `_si1_census`, `_si1_control_census`, `_si2_census`, `_si2_control_census` — are deleted with
the clauses that called them. Every `U3`-side measurement keeps running: the schema, the three
states, `SI-1`'s twenty negative cases and `SI-2`'s nine, the tag-map comparisons that run
historical guard files from git, `#140` and `#141`'s restatements over the scoped record set. Only
the retired-side comparison ceases to be reproducible.

The two censuses are **certified historical measurements of their rounds' checkpoints** — `SI-1`'s
`CENSUS-DIVERGENT` agreement census over twenty-two records and twenty-one controls, `SI-2`'s
`DELTA-AS-ADJUDICATED` profile over twenty-three — and they are never read as current evidence
about any later head; no old/new equivalence is claimed after retirement, because the old side can
no longer be run to say anything. The stage's dry run was all-`PASS`, 92 tags. Outcome
`ARCHIVED-AS-PINNED`.

## `SI3-6` — the protocol

Stage 6 amended `AGENTS.md` §A.37's *Sealing through the manifest* subsection prospectively.
`SI2-7`'s two halves are kept as history in the past tense — every phrase `R7-SI2`'s protocol
contract reads is still present, and the contract still passes — and the sentence precondition 7
names, that the constants *remain* protected historical seal state, is superseded in place: they
*remained* so until `SI-3`'s landing, and `SI-3` took that ownership prospectively and removed them.
A new closing subsection, *The representation retired, from `SI-3`'s landing*, governs rounds begun
after that landing and states: that the legacy representation is retired — no constant, no shadow,
no per-round comparison — and that a round writing any of them fails the zero-statement standing
contract and has recreated the representation that was retired, every seal-state read going through
the manifest accessor; how a sealing round carries its base while it executes, through the
prospective declaration, classified `EXECUTION` and then `LANDED-PENDING-PIN`, with `P` removing the
entry when it writes the record and a stem both declared and recorded a failure; how manifest
integrity is declared, each round's guard declaring its own baseline and no round's hard-coding
another's; that a closed round's contracts are read over the records it manifested, stated once for
every round after; and that the censuses are history. Outcome `PROTOCOL-UPDATED`.

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
None is optimized away. The wall-clock cost of one complete run at `E` is recorded under
*Chronology*.

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

Under §A.37's ownership rule, **the supersession table is the authorization**, as Amendment 1
amended it: every frozen `SI-1` and `SI-2` contract the retirement fails is named there with its
disposition, and nothing outside the table was touched in `R7-SI1`, `R7-SI2` or the `SI2-AUTHORITY`
region. Executed row by row: `R7-SI1`'s N2 shadow deleted with the keyed call unchanged; N13
retired, as Amendment 2 assigned; `SI1-5` replaced by the pin; `SI1-6` and the forbidden-paths
control rebound; the `SI1` record literal; `R7-SI2`'s chronology clause a keyed call with case 11
retired; `R7-SI1`'s scoped-integrity contract generalized at stage 1; `_si2_guard_edits_bounded`
retired at stage 1; the twenty-three-record contracts scoped to `_SI2_MANIFESTED`; case 13 retired
with N13; the two authorized wiring edits and the two authorized dead-object deletions inside
`SI2-AUTHORITY`, bounded by negative cases 14 and 15 — the region at the head with exactly the two
edits reverted equals the region at `B` with exactly the two definitions excised, differs before
reverting, and carries no round stem; `SI2-3` replaced by its shadowless form; `SI2-4` replaced by
the pin; `SI2-5`'s recorded shadows retired; `SI2-6`(b) retired with its extraction kept; every
`_SI2_BASE` revision read rebound; `R7-RNT`'s clause-9 block retired across stages 3 and 4 as
Amendment 1 orders; `R7-HYE` and `R7-PC4S` rebound with the same literals and the same verdicts; the
eight `ok_<x> &= _si2_integrity_ok()` lines unchanged in text with `U5` reading `R3`. No failure
outside the table occurred at any stage: the only failures seen — stage 1's first run and stage 4's
expected `SI2-4` — were each inside a named row.

## The negative suite

`SI-1`'s twenty cases and `SI-2`'s cases 1–8 and 12 run in every run, unchanged. Of this round's
sixteen, each is executable in `R7-SI3` and satisfies its named outcome for its named reason: one
statement of any shape re-added fails `SI3-4`'s detector (1); a shadow function retained or a
`shadow=` argument re-added fails `SI3-3` (2); a comparator, a recording call or the recorder
retained fails `SI3-3` (3); a genuine read of any of the sixty names fails `SI3-2`, and the same
name inside a string literal does not (4); `SI2.json` absent, or carrying `sealed_head` even as
null, fails `SI3-1` (5); a twenty-fifth record before `P` fails `U5` under `R3` as an unauthorized
addition (6); the declaration present beside `SI3.json` fails as declared-and-recorded (7); a
synthetic head descending from an unpinned landing fails as seal pending while the landing itself
is `LANDED-PENDING-PIN` (8); at a synthetic `P`, `sealed_head` not the landing's second parent, or
`merge` not the derived landing, fails (9); a rebinding that changed a pre-existing verdict is
`MAP-CHANGED`, measured by `SI3-7` (10); one byte changed in a pinned census fails the drift control
(11); §A.37 still saying the constants "remain" protected fails `SI3-6` (12); `R1` asked for a
missing record's field or a `base-only` record's `sealed_head` returns the fail-closed sentinel,
never a default (13); the `SI2-AUTHORITY` region differing from `B`'s by anything beyond the two
wiring edits and the two named deletions fails, and a round stem in the region fails
`_si2_region_no_stem` (14); reinstating either deleted definition fails the amended bound (15); a
seventh read outside the machinery, or a read off the residue's lines, fails the residue bound (16).

## Predictions against outcomes

| target | predicted | outcome | scored |
|---|---|---|---|
| `SI3-0` | `HOLD`, HIGH | `HOLD` | as predicted |
| `SI3-1` | `RECORD-AS-AUTHORIZED`, HIGH | `RECORD-AS-AUTHORIZED` | as predicted |
| `SI3-2` | `REBOUND`, HIGH | `REBOUND` | as predicted, under Amendment 1's bound: six residue reads at stages 2 and 3, zero after |
| `SI3-3` | **`SHADOWS-RETIRED`**, MEDIUM | **`SHADOWS-RETIRED`** | as predicted; no tag moved when the shadows went, so `SI-2`'s measurement missed no read |
| `SI3-4` | `RETIRED`, HIGH | **`RETIRED`** | as predicted; a count |
| `SI3-5` | `ARCHIVED-AS-PINNED`, HIGH | `ARCHIVED-AS-PINNED` | as predicted |
| `SI3-6` | `PROTOCOL-UPDATED`, HIGH | `PROTOCOL-UPDATED` | as predicted |
| `SI3-7` | **`MAP-PRESERVED`**, MEDIUM | **`MAP-PRESERVED`** | as predicted; no pre-existing verdict changed at any stage |

No prediction was missed under the freeze as amended. The freeze put its two sharpest claims at
MEDIUM and both held.

## Execution defects, corrected — held apart from the findings

Two were in this attempt's own implementation, not in the control plane, and neither is counted
as a discrepancy. The second was found by the first complete run of the finished guard, which
reported every target's outcome as predicted and still failed `R7-SI3` on one clause that prints
nothing when it holds; it was a defect in a control, not in what the control measures.

| # | defect | how it showed | corrected by |
|---|---|---|---|
| 1 | the stage-1 patch, reused from attempt 1, still lacked the scoping of `SI2-4`'s census input and `SI2-8`'s `#140` probe to `_SI2_MANIFESTED` — attempt 1 had added those lines by hand rather than to its patch, and Amendment 1 said the re-execution would carry the fix from the start | the stage's first dry run: `SI2-4` `DELTA-BROKEN` with 24 of 24 agreeing, `SI2-8` over 24 records, `R7-SI2` failing | the scoping added to the same uncommitted stage, inside the table's twenty-three-record row, and folded into the patch; rerun all-`PASS`, then committed |
| 2 | the residue-bound measurement strips the shadow and comparator function bodies before counting reads, and its stripper required a following top-level line, so negative case 16's last control — a synthetic shadow function appended at the end of the text, whose read must not count — was not stripped and counted one read | the first complete run: every outcome as predicted, `R7-SI3` failing; each `ok_si3` conjunct instrumented in a scratch copy and exactly one reported false | the stripper accepts end-of-text; the measurement at every stage commit and at the head is unchanged by it, since no such function ends the real file |

Attempt 1's other implementation defects — the guard's self-referential `shadow=` literal, the
guard-insertion script's quoting — were carried as fixed and did not recur.

## Discrepancies

There is **no discrepancy** between the freeze as amended by Amendment 1 and the execution. The two
discrepancies attempt 1 reported are resolved prospectively by the amendment and did not arise:
`_si2_shadow_integrity` and its list were deleted under point 1 inside the bound negative cases 14
and 15 measure, and the clause-9 block was retired across stages 3 and 4 under point 2 with the
residue bound of point 3 holding at every stage commit. The `SI1-5` mechanism is a finding about the
freeze's reasoning, recorded in Amendment 1, with the disposition executed unchanged.

**No frozen definition, target, negative case or authority rule was altered.** `U1`–`U5` are
unchanged in semantics; the `SI1-VALIDATOR` region is unedited and `_si2_region_relocated_verbatim`
still holds against it; the `SI2-AUTHORITY` region differs from `B`'s by the two wiring edits and the
two named deletions and nothing else.

## Definition slots

**Three definition slots, and three were fired**: `R1` the manifest accessor, `_seal_field` with
`_seal_triple` over it; `R2` the prospective declaration, `_MANIFEST_PROSPECTIVE`; `R3` the
round-declared baseline, `_MANIFEST_BASELINE`. All three are declared outside both marker-bounded
regions, before the first keyed clause runs, and none carries a round stem in its name. The
`R7-SI3` guard, its negative suite and the base run are test code.

## Chronology

The execution is six stage commits and one final commit on `claude/si3-execution-2`, in the frozen
order, each named above, branching from `B` and from nothing else, with no commit of attempt 1
reachable. The property certified is act 10's strengthened one, asked of the real pull-request head
and reached through `U3`'s prospective path: `EXECUTION` at every commit of the round,
`LANDED-PENDING-PIN` at `L`, `ARCHIVED` at `P`. One complete run of the guard file at `E` on the
execution machine, eight executions counted, took about 178 seconds of wall-clock time, against
about 100 seconds for a run at the stage-5 commit before `R7-SI3` existed; the base's guard file
was also run at `SI-2`'s base on every one of the round's dry runs from stage 1 on, by `SI2-6`(a).

The record set is twenty-four from stage 1 to `E`, and the only change `P` makes is the one
authorized addition and the removal of the declaration. The fourteen frozen pins and both frozen
blobs are unchanged. Attempt 1's head `76bf328a19c7354cbb0a120b4a374c16369aa1a1` is history and not
result evidence. Act 21 is neither opened nor closed by any outcome here.

The claim is scoped to the repository record.
