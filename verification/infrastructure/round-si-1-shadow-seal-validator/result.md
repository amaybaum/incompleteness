# Seal infrastructure round 1 — the shadow validator and the equivalence census: RESULT

Executed from the mandated base `B` = `99ab6370470ed9d9e4005551581c6c8c18e54bd2`, the merge commit
of the control plane (PR #667), and from no other commit. The freeze read out of that base carries
the blob `4a5f183a52b2720e0714049ecf34911c55c1ef61` the guard names.

**This round is NON-SEALING and NON-AUTHORITATIVE.** The existing per-round machinery remains
authoritative for every check that gates. The generic validator built here runs, reports, and is
compared against it; it decides nothing. **Presence is not authority** — the new code being in the
tree does not make it the instrument, and `SI1-6` establishes that mechanically rather than
asserting it. The instant this validator decides anything, that is `SI-2`.

## The first reviewed candidate, and why this is not it

The first immutable candidate was **`3b28fdeaa044e2cd28c3139e436ffe35209ee8af`**. It was reviewed
and **was not accepted as `E`**. It is preserved unchanged — **no amend and no force-push** — and
this execution continues on the same branch so that the review finding stays in the chronology
rather than being erased by the commit that answers it.

Four things were wrong with it, all inside the target accounting rather than the ancestry or the
file scope:

1. **`SI1-5` claimed `CENSUS-EXACT` without earning it.** The census covered the twenty-two real
   records only. The freeze requires old-versus-new verdicts for every synthetic control as well,
   and those records sit in the one configuration where the two implementations were built to
   agree — so a census over them alone cannot see where they were built to differ. Completed here,
   and the outcome changes.
2. **`#141` was reported as holding when the round's own finding shows it failing.**
3. **`#140` was reported as holding when the frozen question had not been asked at all.**
4. **Two provenance inaccuracies**: the note and the guard narration claimed set *equality* of the
   seal-assignment sets where the executable check correctly allows exactly one addition, and the
   commit message said "FOUR FILES" where the verified diff is 26 files.

## The second reviewed candidate, and why this is not it either

The second immutable candidate was **`b62ee49fa23995947083afdc480b903d20d979ff`**, the corrective
commit answering those four findings. It was reviewed and **was also not accepted as `E`**, on two
findings, and it is preserved unchanged for the same reason — **no amend and no force-push** — so
that **both prior reviews and their corrective answers** stand in the chronology:

1. **`SI1-5` still did not perform the frozen old-versus-`O2` comparison on controls 10, 11 and
   12.** The rows existed and the totals counted them, but both columns were filled from the *same*
   shared visibility helper, so the comparison could not diverge; and the old archive path, where it
   was called, was handed an **explicit target**, which switches off exactly the resolution through the
   head or the base-branch tip that those three controls exist to exercise. Corrected here, and **the outcome
   sharpens**: the literal comparison yields **four** divergences, not three, and the new one is
   control 10.
2. **Stale `CENSUS-EXACT` prose survived in the note** — the sentence that the two implementations
   "do not differ on the cases presented", which four divergences falsify. Replaced with the narrow
   claim the evidence supports.

## The third review, and the two findings and one provenance error it produced

The second corrective commit, **`2752886344af3be9479460792417f42622fc14f9`**, was reviewed and
**was not accepted as `E`** either. It is preserved unchanged. Three things were found:

1. **`SI1-5` adjudicated a divergence, which the freeze forbids.** The note said that on control 10
   "the old machinery is right and the new model is wrong" and later called it "the correct one";
   `census.json` carried a key naming the implementation held correct; and the guard *required* that
   wording. The measurement was right and is kept exactly as measured — `old=PASS`, `new=FAIL` — but
   the correctness claim is removed from `SI1-5` in all four places. `#141` remains
   **`RESTATED-AND-FAILS`**: that target is the one the freeze permits to decide whether the model
   has the property, and it decides it under `#141`'s own requirement.
2. **Mutation control 9 was tautological.** It built a copy of the census document, changed one
   total, and asserted the two differed — which tests Python, not the artifact check. It now runs
   the mutated bytes through **the same predicate the recorded file goes through**.
3. **A commit-message provenance error, recorded and not editable.** `2752886`'s message says
   "three reviews and three answers" stand in the chronology. At the time it was written there were
   **two** completed reviews and two corrective answers, and `2752886` was itself the candidate for
   the third. The commit is reviewed and is not amended, so the error stays in the history and is
   recorded here; the live text now says "both prior reviews and their corrective answers", which
   does not go stale as reviews accumulate.

**The fourth divergence was predicted by the owner before it was measured**, in the review that
required the literal comparison: that the target-scope defect breaking `#141` should also surface
independently in the control census as case 10. It did, exactly there. That is the **owner's**
prediction and not the freeze's, so it is recorded here rather than scored in the predictions table
— where `SI1-5` remains a **miss**, the freeze having predicted `CENSUS-EXACT`.

## Outcomes

| target | outcome | decided by |
|---|---|---|
| `SI1-0` | locating controls hold | the six pinned blobs and eight preconditions, checked at `B` |
| `SI1-1` | **`SCHEMA-BUILT`** | 22 records under `verification/seals/`, every value byte-identical to the freeze's table |
| `SI1-2` | **`VALIDATOR-BUILT`** | the three states, `base-only` held out of the machine, no stem in the validator region |
| `SI1-3` | **`DERIVE-EXACT`** | 18 of 18, exactly one candidate each, agreeing with the pin |
| `SI1-4` | **`NEGATIVES-COMPLETE`** | all **20 frozen negative cases** satisfy their required outcomes, in 21 case rows |
| `SI1-5` | **`CENSUS-DIVERGENT`** | records agree 22 of 22; **controls diverge in 4 of 12 comparable**, and 9 have no analogue |
| `SI1-6` | **`SHADOW-ONLY`** | the base's guard file re-run: 90 check tags, all PASS, map identical to the persisted one |
| `SI1-7` | delivered | the `SI-2` specification below |
| `SI1-8` | **`RESTATED-ONLY`** for `#140`; **`RESTATED-AND-FAILS`** for `#141` | the mandate was never compared; the model fails `#141`'s own requirement |

## `SI1-1` — the manifest

Twenty-two records, one file per round: eighteen of `kind: "sealed"` and four of
`kind: "base-only"` — `ABR`, `CLG`, `RBR`, `TSG`. Every value was taken from **the freeze's own
table**, not from the execution's parse of the guard source, and each was checked against the first
module-level assignment in the guard file at `B`: **22 of 22 agree**.

The schema is the discriminated union the owner settled. `base-only` requires `base` and forbids
`sealed_head` and `merge`; `sealed` requires all three; forbidden means a hard failure and not a
tolerated null. Those four rounds are not seals waiting for fields — they are rounds for which no
seal exists, and the schema says so structurally.

### The double-assignment hazard, reported more precisely than the freeze states it

The freeze records that `_RNT_SEALED_HEAD` and `_RNT_MERGE` are each assigned twice at module level
and that a transcription taking the last assignment returns the probe's synthetic values. **That is
true, and it is conditional on the parser, which is worth stating exactly.**

- A parser accepting **any right-hand side** sees two assignments of each name and, taking the last,
  returns `'f' * 40` and `'e' * 40` for exactly one round while producing a manifest that looks
  entirely well-formed. Measured: duplicates reported for `('RNT', 'SEALED_HEAD')` and
  `('RNT', 'MERGE')`, last values at lines 23602 and 23603 of the guard file at `B`.
- A parser restricted to **40-hex literals** never sees the second assignment at all, so it is
  immune by accident rather than by design.

The first class is not hypothetical: the pre-freeze census script written while preparing this
round's control plane was of exactly that kind, and it did return the probe values for `RNT`. The
shipped transcriber takes the **first** assignment and reports the duplicate rather than silently
resolving it. Negative case 18 pins both halves.

## `SI1-2` — the validator

Four definition slots, and four were fired: the record schema `O1`, the generic validator `O2` with
its three states, the derivation function, and the shadow harness `O3`. The negative suite is test
code and is not a slot.

`O2` returns a verdict for every record and **either** a lifecycle state **or**
`lifecycle = not-applicable`. It does not return a state for every record, because not every record
has one.

**The three states are the lifecycle of a seal-producing round, not of every manifest record.** A
`base-only` record does not enter the state machine: its schema, its pinned base and its record
integrity are validated, and it is not classified `EXECUTION`, `LANDED-PENDING-PIN` or `ARCHIVED`.
`BASE-ONLY` is not a fourth lifecycle state and none was invented; no lifecycle value is stored for
any record.

The no-stem condition is checked mechanically over the region between the `SI1-VALIDATOR-BEGIN` and
`SI1-VALIDATOR-END` markers: no round stem and no `R7-` tag other than this round's own appears
anywhere in it.

## `SI1-3` — the derivation, and a finding about its frozen scope

Measured by the shipped function over all eighteen `sealed` records, at the execution head:

| scope | result |
|---|---|
| **reachable history** (the frozen rule) | exactly one candidate, equal to the pin, for **18 of 18** |
| **first-parent spine** (retained regression) | **6 agree, 12 zero-candidate, 0 other** |

Both historical landing shapes are in the corpus and were reproduced rather than assumed. Shape A,
`L` on the first-parent spine: `A12P`, `A6D`, `HYA`, `RNT`, `SGT`, `XTS`. Shape B, `L` one step off
it: `A6I`, `A6P`, `CTI`, `HYB`, `HYE`, `PC4`, `PC4S`, `PQT`, `RNC`, `TCF`, `TRJ`, `WTS`. The
first-parent scope reports exactly the 6/12 split the freeze names, so a later narrowing of the
scope is caught rather than accepted.

**The two scopes are kept apart and are not two acceptable implementations.** The reachable-history
result is the round's measurement of the frozen rule. The first-parent result is a **regression
control**: the narrower algorithm's failure on twelve of eighteen rounds is the thing being held in
place, not an alternative anyone may select. A future change that made the first-parent scope pass
would have moved the corpus, not improved the algorithm.

The four `base-only` records are **not derived over**: there is no sealed head to derive from.

### DISCREPANCY 1 — the frozen derivation scope reintroduces the base-age false negative

**Recorded, not repaired. This is evidence about the preregistered rule, not an execution defect,
and it is not the kind of thing an implementation may absorb.**

**The frozen sentence it bears on**, quoted from the preregistration:

> **The derived `L` is the unique merge commit in the resolved target's reachable history whose
> non-first parent is exactly `E`.**

**Does it change a target verdict? Yes — one, and not the one it looks like.** Precisely: **it does
not change `SI1-3`; it does change `SI1-8`/`#141`.**

`SI1-3` is `DERIVE-EXACT` and stays so: at this execution head, on a push, the frozen rule does
agree with the pin for 18 of 18 with exactly one candidate each, and that measurement is not
weakened by the finding. Softening it because the validator has a limit elsewhere would misreport
what was measured.

`SI1-8`/`#141` is a different question. `#141` is the requirement that **prior seals be evaluated
against the landing topology rather than the pull-request head.** Discrepancy 1 exhibits the built
model failing for exactly that reason: a landing that exists on the live base branch, and is
therefore present in the landing topology, is refused because it is absent from a historical pull
request's head. So the frozen `#141` is **`RESTATED-AND-FAILS`**, and **the prediction for `#141` was
wrong**. That is a legitimate result of a shadow round — it is the kind of thing the round exists to
find before `SI-2` makes anything authoritative — and it is recorded as a miss rather than
softened.

The freeze scopes derivation to *the resolved target*. On a push, and on
a pull request whose base already carries a round's landing, that is exactly right — and it is why
all eighteen agree above. But under `A.37` an execution branches from its own control plane and from
nothing else, so **a pull request opened from a historical base does not reach landings that arrived
on `main` afterwards**, and for those rounds the derivation finds zero candidates and fails closed
although nothing has been rewritten and the landing is sitting on the base branch.

This is the same base-age false negative the archive-visibility repair removed from the reachability
leg, arriving again through the derivation leg. It is measured on a synthetic topology rather than
argued: from a head cut from the root, **0 candidates**; from `refs/remotes/origin/main`, which
carries the landing, **1 candidate**.

It is not hypothetical for this repository either. On the four control-plane branches landed on
2026-09-17, `R7-HYE`, `R7-RNC`, `R7-TRJ` and `R7-XTS` re-certified **through
`refs/remotes/origin/main` and not through the head**. Under the frozen derivation rule those same
four rounds would find zero candidates on those same pull requests.

The remedy this round would propose, and does not apply, is to derive over the **union of the
visibility targets** — the resolved head and the base-branch tip — which is the set the reachability
leg already uses, leaving every other part of the rule untouched. **Altering the frozen rule is not
this round's to do.** It is put to the owner as a result requiring adjudication, and `SI-2` should
not be frozen until it is adjudicated, because the cutover would make this the gating behaviour.

## `SI1-4` — the negative suite

**All twenty frozen negative cases satisfy their required outcomes**, each failing or passing for
its **named reason** and not merely coming out the right colour.

The suite emits **22 rows**, and the arithmetic is worth stating exactly so the chronology stays
exact. **Twenty preregistered cases** occupy **21 case rows**, case 4 having two legs — a forbidden
field present as a value and the same field present as `null`. The **22nd row is an OBSERVATION**,
not a preregistered case: it is the derivation-scope measurement reported under Discrepancy 1. This
round is a 20-case frozen suite with one additional observation row, and it is **not** a 21-case or
22-case frozen suite; nothing added during execution is retroactively counted as preregistered.

| # | case | verdict |
|---|---|---|
| 1 | malformed hash | FAIL, `is not 40 lowercase hex` |
| 2 | missing required key | FAIL, `requires merge and it is missing` |
| 3 | unknown extra key | FAIL, `unknown key(s) note` |
| 4a | `base-only` carrying a `sealed_head` value | FAIL, `forbids sealed_head` |
| 4b | the same field present as `null` | FAIL, `a forbidden field is a failure even as null` |
| 5 | rewritten sealed head | FAIL, `unreachable` |
| 6 | wrong `L` — a real merge, not this head's landing | FAIL, `disagreement` |
| 7 | two candidate landings for one `E` | FAIL, `multiple candidates` |
| 8 | zero candidate landings | FAIL, `zero candidates` |
| 9 | sibling history, in `EXECUTION` | FAIL, `does not descend` |
| 10 | stale `base.sha`, base branch carries the landing | PASS via `refs/remotes/origin/main` |
| 11 | base branch rewound off the landing, `base.sha` still carrying it | FAIL, failing closed |
| 12 | unresolved base ref with a local branch of that name | FAIL, `does not resolve` |
| 13 | a descendant of an unpinned `L` | FAIL, `seal pending` |
| 14 | the unpinned `L` itself | PASS, `LANDED-PENDING-PIN` |
| 15 | mutation of a record present at the base | FAIL, `mutated` alone |
| 16 | removal of a record present at the base | FAIL, `removed` alone |
| 17 | unauthorized addition | FAIL, `added` alone |
| 18 | a stem assigned twice with different values | first assignment taken, duplicate reported |
| 19 | a reading consulting the synthetic merge `HEAD` | resolved target FAILS, synthetic merge would PASS |
| 20 | `base-only` where an `EXECUTION`-style check would fail | PASS, `not-applicable`; `EXECUTION` fails the case |

And, separately and **not** as a frozen case:

| row | observation | measured |
|---|---|---|
| 22 | derivation scope, reported under Discrepancy 1 | from a historical head **0 candidates**; from the base-branch tip **1** |

Case 20 is the one the freeze was amended to add before its head was fixed, and it is the direct
regression on the corrected reading: the strong check does fail on that state, and the record passes
anyway because it is out of the machine.

### DISCREPANCY 2 — NEGATIVE CASES 10, 11 and 12 are exercised on the visibility layer, and had to be

**Recorded, not repaired.** This entry is about the **`O4` negative cases** numbered 10 to 12, the
retained stale-base / live-base controls, and **not** about the identically numbered rows of the
`SI1-5` control census, which do run through both implementations end to end. The three negative
cases are exercised against the base-branch-tip resolution plus reachability, **not** against `O2`'s
derivation, because under the frozen scope the derivation answers first: with the landing absent
from the head, derivation reports zero candidates and the visibility leg never speaks. Case 11 as
worded — a visibility failure — is therefore **unsatisfiable through the derivation path**, and
routing it through the layer where the behaviour actually lives is a reading this round took rather
than a freeze change. It is the same defect as Discrepancy 1 seen from the test side, and the same
adjudication settles both.

The census rows of the same numbers are the complementary measurement: there each side resolves the
synthetic event for itself, the derivation does answer first for `O2`, and that is exactly what
**divergence 10** records.

## `SI1-5` — the agreement census

**Outcome `CENSUS-DIVERGENT`.** `census.json` carries both tables. Its reason strings name **the resolved target** by a fixed
token rather than by the object a particular run resolved, because that name is the event's — `HEAD`
on a push, `pull_request.head.sha <sha>` on a pull request — and a recorded census naming either is
stale under the other on the very same commit. The verdicts are recorded as measured.

### Over the twenty-two real records: agreement, on the axis each is on

| axis | records | new lifecycle | agreement |
|---|---|---|---|
| lifecycle | 18 `sealed` | `ARCHIVED` ×18 | 18 of 18 |
| schema + pinned base + record integrity | 4 `base-only` | `not-applicable` ×4 | 4 of 4 |

The old machinery's verdict was taken from the generic helpers the per-round clauses themselves
call — the archive-mode certificate for a sealed round, the strengthened execution check for a
non-sealing one — run in the same process and on the same repository state, so the census compares
like with like rather than comparing the new validator against a paraphrase of the old one.

### Over the twenty-one synthetic controls: four divergences, and nine questions the old machinery cannot answer

This is the half the first candidate omitted, and it is where the outcome is decided. Each side
**resolves the event payload for itself**, exactly as the per-round clauses do: the old archive path
through `_rbr_archive_ancestry` with the event and no explicit target, `O2` through its own target
resolution. Handing either side a target, or comparing a shared helper to itself, is not a
comparison — earlier candidates did both, and both are recorded below as execution defects.

| | controls | |
|---|---|---|
| comparable | **12** | an old-machinery answer exists |
| no analogue | **9** | **nine controls have no old-machinery analogue**: the old machinery holds no records, so nothing in it answers a schema question (5), a manifest-integrity question (3) or a transcription question (1) |
| **divergent** | **4** | of the twelve comparable |

The four divergences, both verdicts recorded and **none adjudicated**:

| control | old | new | what differs |
|---|---|---|---|
| **10 stale `base.sha`, base branch carrying the landing** | **PASS** | **FAIL** | the old archive path resolves **head or base-branch tip** and finds the landing on the tip; `O2`, under the frozen target-only derivation scope, sees only the historical head, derives **zero candidates**, and fails before the visibility leg can speak. **This is Discrepancy 1 arriving independently, through the census** |
| 7 two candidate landings for one `E` | PASS | FAIL | the archive certificate checks the pinned merge's second parent and reachability, so it does not notice a **second** merge carrying the same sealed head; the new model refuses it as `multiple candidates` |
| 13 a descendant of an unpinned `L` | PASS | FAIL | the old machinery has **no pending-seal notion**, so it answers the execution question and admits the descendant; the new model refuses it as `seal pending` |
| 20 `base-only` on a state where an `EXECUTION`-style check fails | FAIL | PASS | the old machinery applies **execution ancestry semantics to a completed non-sealing round** and refuses it; the new model does not classify it at all |

**The four are not of one kind, and the difference is the round's most important result — stated
without adjudicating any of them.** On 7, 13 and 20 the **new** implementation is the stricter one,
which is the direction the freeze says it was built in. On **10 the direction is reversed**: the old
archive path returns `PASS` and `O2` returns `FAIL`. Both verdicts are recorded, and **`SI1-5`
declares neither implementation correct**, here or anywhere.

What divergence 10 does carry is a **behavioural identification, not a verdict**: it is the
target-only derivation scope producing a zero-candidate failure on a pull request from a historical
base — **the same behaviour Discrepancy 1 records**, reached by an entirely separate route, and the
behaviour that `SI1-8` decides `#141` against under `#141`'s own requirement. That decision is
`SI1-8`'s to make and is made there. This is why the control half of `SI1-5` could not be skipped:
had the census stopped at the twenty-two real records, that behaviour would appear once as a
reasoned argument instead of twice as a measurement.

Controls 11 and 12 agree, both sides failing, for different reasons — on 11 neither the head nor the
rewound branch tip carries the landing; on 12 the old path fails when the base ref will not resolve
while `O2` fails one step earlier on zero candidates. `O2` returning no verdict is recorded as a
**failure**, explicitly, rather than left to `bool(None)` to mean the right thing by accident.

**Non-comparability is a result and not a reason to narrow the target.**

This round **does not adjudicate which implementation is right** on any of the four, and the
prohibition is the freeze's, not a preference: *"A divergence in `SI1-5` is recorded with both
verdicts and the round stops short of adjudicating which is right. Adjudication is the owner's, and
if the old machinery is the one in error that is a finding about the existing record which `SI-1` has
no authority to act on."* The frozen list of what no outcome licenses says the same thing twice over,
forbidding "any claim that the new validator is *correct*, as distinct from *in agreement*" and "any
adjudication of a census divergence".

So: on 13 and 20 the freeze **describes** the new reading as the intended one — 13 is the purpose of
`LANDED-PENDING-PIN`, 20 is the correction the freeze was amended to require — and a statement about
what the freeze intends is not a statement about which implementation is right. On 10 nothing is
said about correctness at all; the two verdicts stand side by side. **`SI-2` is where all four
decisions belong**, and Discrepancy 1 is the one of the four already put to the owner as requiring
adjudication.

**The frozen sentence for this outcome, carried verbatim:** *"The two implementations disagreed on
the records named below. Both verdicts are recorded. This round does not adjudicate which is correct
and changed neither implementation to remove the disagreement."* Read against the controls rather
than the records, which is where this round's disagreements are: no implementation was changed to
remove any of the four.

**This is an agreement census and not a proof of correctness**, and with four divergences on the
record the point has to be put narrowly: **agreement where it occurs is not evidence of correctness,
because a shared error survives every case both sides get wrong together.** The stronger sentence
the first two candidates carried — that the implementations "do not differ on the cases presented" —
is false here and has been removed: they differ on four controls. Both implementations were written
in one round from one specification, which is exactly the circumstance in which a shared misreading
is possible, and the twenty negative cases exist because agreement on agreeing cases is the weaker
half of the evidence.

### An observation, recorded and not a divergence

On the four `base-only` rounds the two implementations agree on the verdict and differ in **why**.
The old machinery applies the strengthened *execution* ancestry check to them and passes today. The
new validator does not classify them at all. Verdicts therefore agree, and the census records
agreement; but the old reading is the one that would fail if sibling history ever appeared in their
targets — which is precisely the condition that reddened `main` over act 20's `L` before its pin.
The new reading is immune to it by construction. Nothing is claimed beyond this, and no verdict
changed.

## `SI1-6` — non-authority, checked mechanically

- No seal constant and no prior-seal comparison was removed. Stated exactly: every
  `_*_(BASE|SEALED_HEAD|MERGE)` assignment present at `B` is **still present and unchanged**, and
  the **only** addition is this round's own `_SI1_BASE`. That is **containment plus one named
  addition, not set equality** — the first candidate's note and guard narration both claimed
  equality, which this round's own base falsifies, and which is also how a round that quietly
  re-pinned another round's seal would be caught.
- **90 pre-existing check tags** at `B`, **90** at the execution head, **none removed**, and **no
  pre-existing tag's verdict changed**.

  **What was compared, stated so it cannot later be misread.** The unit is a **check tag** — the
  `R7-*`, `R8`, `R9` and numbered identifiers that `check()` prints one `PASS`/`FAIL` line for. Not
  ninety files, not ninety seal records, not ninety assertions.

  **And it is now performed inside the shipped guard, not merely described here.** `R7-SI1` takes
  the guard file from `B` with `git show`, **runs it**, parses its verdict lines into a
  tag-to-verdict map, and requires that map to be identical to the one this round persisted in
  `si1-tagmap.json`. Measured fresh on every run: **90 tags, all `PASS`**, map identical to the
  persisted one.

  **The claim is a conditional, and is stated as one.** In process, `CHECKS` is incomplete when this
  guard runs, because checks declared after it have not executed yet — so verdict equality for every
  pre-existing tag cannot be read off this run directly. What follows from *every base tag passing*
  is: **if this run ends `ALL CHECKS PASS`, then no pre-existing tag's verdict differs from the
  base.** The probe's own exit status discharges the antecedent. Both runs do report
  `edge_rigidity_probe: ALL CHECKS PASS`, and the head declares one further tag, `R7-SI1` — 91 at
  the head in total.
- No existing check consults the new validator: every `_si1_` reference lies inside this round's own
  guard section.

The one tag added is `R7-SI1` itself.

## `SI1-7` — what `SI-2` would have to do

A specification, not an implementation. Type P: it is not evidence about the repository and is out
of any table of certified results.

**It creates no `SI-2` implications beyond what `SI-1` measured.** The items below are inputs to
`SI-2`'s freeze, available to be adopted, amended or rejected when that freeze is written. Nothing
here is authority to redesign `SI-2` now, and nothing here is a decision.

1. **Adjudicate Discrepancy 1 first.** The derivation scope is the gating behaviour after cutover.
   Whatever is decided, the frozen rule or the union-of-visibility-targets remedy, must be settled
   before `SI-2`'s control plane is written, because `SI-2` cannot both cut over and change the rule
   it cuts over to.
2. **Move authority.** Replace each round's per-round ancestry clause with a call to the generic
   validator keyed on that round's manifest record. Evidence: `SI-1`'s certified census, plus a
   re-run of it at `SI-2`'s own head showing the same agreement.
3. **Remove the duplicated state.** Delete the `_*_BASE`, `_*_SEALED_HEAD` and `_*_MERGE` constants
   and the hand-written prior-seal comparisons. Evidence: the seal constants' disappearance from the
   guard file together with an unchanged set of verdicts.
4. **Replace the per-round seal-integrity clauses** with the one data-driven rule over the manifest —
   mutated, removed, added, against the record set at `SI-2`'s base. This is what removes the
   quadratic growth: eighteen hand-written comparisons per round today, and one loop afterwards.
5. **Keep both implementations for one round** if the owner wants a stronger bootstrap: run the
   generic validator as authoritative and the old machinery as the shadow, inverting `SI-1`, before
   the constants are deleted.
6. **Do not retrofit.** Every historical `B`, `E`, `L`, `P` stays exactly where it is.

## Execution defects, corrected — held apart from the findings

Twelve defects were in **this round's own implementation**, not in the freeze. They were execution
errors, they were corrected, and they are recorded here so that the distinction between *a defect
the implementation may fix* and *evidence about the preregistered rule* is on the record rather than
left to a reader to infer.

| # | defect | how it showed | corrected by |
|---|---|---|---|
| 1 | the schema checked **unknown keys before forbidden fields**, so a `base-only` record carrying `sealed_head` was reported as a stray key rather than as a seal asserted for a round that has none | negative cases 4a and 4b failed on the reason, not the colour | checking forbidden before unknown; the diagnosis is the value of the check |
| 2 | the record reader was passed **absolute paths**, which `_artifact` resolves relative to `verification/`, yielding a path under `verification/` and a missing file | all 22 records loaded as `unreadable` while the directory listing found them | listing absolutely, reading by relative name |
| 3 | four content contracts matched **substrings that crossed line breaks**, so a true claim in the note read as absent | three contracts false against a correct note | matching on collapsed whitespace: the words are the claim, the wrapping is not |
| 4 | the seal-constant check asserted **set equality** between head and base, which this round's own `_SI1_BASE` necessarily breaks | the check failed while no other round's seal had moved | containment plus an exact allowance for this round's own base — which is also how a round that re-pinned another round's seal is caught |
| 5 | the synthetic **event payloads were named by head alone**, so two payloads differing only in their base ref overwrote each other before either was read | the stale-base control silently became a second copy of the rewound-branch control, and reported a value that could not be right | naming the payload by head **and** base ref; found because the value was impossible, not because a test failed |
| 6 | **census controls 10–12 compared the shared visibility helper to itself**, storing one value in both the `old_ok` and `new_ok` columns | a comparison that cannot diverge; and case 12's fields read `True/True` to mean "the resolver correctly refused", the opposite of what the field names and the frozen verdict say | invoking the actual old archive path and the actual `O2` path under the same synthetic event |
| 7 | the old archive path was handed an **explicit target**, which replaces its candidate list with that one commit and so **switches off** the head-or-base-branch-tip resolution those controls exist to exercise | case 10 came back agreeing, which could not be right | letting each side resolve the event payload for itself, as the per-round clauses do |
| 8 | `census.json` was written by a **side script** rather than emitted by `O3`, although the freeze says `O3` emits it | after defects 6 and 7 were corrected the census measured **four** divergences while the recorded file still carried three: a hand-kept record of a measurement drifts silently | `O3` now rebuilds the document from the rows measured in the run and the guard **requires the file on disk to equal it**, so a stale census fails the check instead of being read |
| 9 | `O2` passed a **`None` target list onward** when the base-branch-tip resolver had already failed closed, and only the order of the checks after it kept that `None` from being iterated | invisible until control 12 became a real comparison, which is the one case that produces it | returning `None` at the point the resolver refuses, so the refusal is `O2`'s answer rather than a value it carries |
| 10 | **`SI1-5` adjudicated a divergence**, saying on control 10 that the old machinery was right and the new model wrong, with a `census.json` key and a *required* guard phrase to match | the freeze forbids it twice over: `SI1-5` "stops short of adjudicating which is right", and no outcome licenses "any claim that the new validator is correct, as distinct from in agreement". The measurement was right; the verdict was not mine to give | the measured direction is kept and the correctness claim removed in all four places, with the guard now requiring the direction and the refusal instead |
| 11 | the artifact check's **mutation control was tautological**: it copied the measured document, altered one total, and asserted the two differed | it tested that Python dictionaries with different values are unequal, and would have passed however the artifact check behaved | the check is now ONE predicate over the recorded bytes, and both controls -- one total altered, and unparseable bytes -- run the mutation through that same predicate |
| 12 | the census document was **event-dependent**: its reason strings name the resolved target, which is `HEAD` locally and on a push and `pull_request.head.sha <sha>` in pull-request CI, where the sha changes with every commit | the artifact check passed on a `workflow_dispatch` run and **failed on the pull request for the same commit**, with every verdict and every total identical — the check was right and the artifact was wrong | normalizing the resolved target's NAME to a fixed token before the document is built, with a control that the substitution happened; the VERDICTS are not normalized, so a target at which either implementation genuinely answers differently still fails the comparison |

None of the twelve is a finding about the freeze, and none of them is counted among the discrepancies
below. Defects 1, 4, 5, 6, 7, 8, 9, 11 and 12 also improved the checks they were in, which is recorded as what it is and
not as a discovery.

## Discrepancies, recorded and not repaired

These are **evidence about the preregistered contract**, not implementation errors, and none was
repaired.

1. **The frozen derivation scope reintroduces the base-age false negative** on a pull request from a
   historical base. Measured. Remedy proposed, not applied. Requires adjudication before `SI-2`.
   **It changes `SI1-8`/`#141` to `RESTATED-AND-FAILS`** and leaves `SI1-3` at `DERIVE-EXACT`. It is
   **reproduced independently** by control 10 of the `SI1-5` census, where the old archive path
   returns `PASS` through the base-branch tip and `O2` returns `FAIL` with zero candidates. The
   census records both verdicts and adjudicates neither; the decision against `#141` is `SI1-8`'s,
   taken under `#141`'s own requirement and not from the census.
2. **Negative cases 10, 11 and 12 are exercised on the visibility layer**, case 11 being
   unsatisfiable through the derivation path under the frozen scope. This concerns the `O4` cases,
   not the identically numbered census controls, which do run both paths in full. The same
   adjudication settles it.
3. **The double-assignment hazard is parser-conditional**, and the freeze's statement of it is true
   for the parser class that matters. Reported precisely above rather than repeated as written.

**No frozen definition, target, negative case or authority rule was altered.** Each of the three is
a result put to the owner.

## Predictions against outcomes

| target | predicted | outcome | scored |
|---|---|---|---|
| `SI1-0` | hold, HIGH | hold | as predicted |
| `SI1-1` | `SCHEMA-BUILT`, HIGH | `SCHEMA-BUILT` | as predicted |
| `SI1-2` | `VALIDATOR-BUILT`, MEDIUM | `VALIDATOR-BUILT` | as predicted |
| `SI1-3` | `DERIVE-EXACT`, HIGH, on a measurement already taken | `DERIVE-EXACT` | as predicted, and the freeze recorded that this rested on a prior measurement rather than on a forecast |
| `SI1-4` | `NEGATIVES-COMPLETE`, MEDIUM | `NEGATIVES-COMPLETE` | as predicted |
| `SI1-5` | `CENSUS-EXACT`, MEDIUM | **`CENSUS-DIVERGENT`** | **MISSED.** The freeze predicted exact agreement at MEDIUM and the round found four divergences among the controls. Reported as a miss |
| `SI1-6` | `SHADOW-ONLY`, MEDIUM | `SHADOW-ONLY` | as predicted |
| `SI1-7` | delivered, HIGH | delivered | as predicted |
| `SI1-8` `#141` | `RESTATED-AND-HOLDS` | **`RESTATED-AND-FAILS`** | **MISSED.** The freeze predicted it would hold; the round's own finding shows the model failing `#141`'s requirement. Reported as a miss |
| `SI1-8` `#140` | **NOT PREDICTED** | `RESTATED-ONLY` | **not scored.** The freeze put nothing at risk here and nothing is scored |

### `#140` — `RESTATED-ONLY`, because the frozen question was never asked

The frozen question is whether **each of the twenty-two recorded `base` values equals that round's
historically mandated base** — the merge commit of that round's own control plane. Answering it
needs an **independent source for each mandate**, and this round has **no independent source for the
mandate**: the manifest was transcribed from the guard constants, so comparing the manifest to those
constants establishes nothing about the mandate. **Recorded bases compared to an independent
mandate: 0 of 22**, and the guard asserts that count at zero so the claim cannot drift upward by
accident.

Two weaker structural facts *are* measured, both executable in the guard, and both labelled
observations rather than the frozen question:

| observation | result |
|---|---|
| every recorded base is a merge commit | **22 of 22** |
| for each `sealed` round, exactly one execution-history commit has the recorded base as its **sole parent** — `A.37`'s branch-root invariant | **18 of 18** |

Neither compares a manifest value to a mandate, and **the four `base-only` rounds receive no
analogous check at all**, having no execution history to walk. The first candidate reported these two
facts as `RESTATED-AND-HOLDS`; that was wrong, and `#140` remains open for the round that can supply
the mandates.

### `#141` — `RESTATED-AND-FAILS`

Reported under Discrepancy 1. `#141` requires prior seals to be evaluated against the landing
topology rather than the pull-request head, and the built model fails that requirement in the
configuration the discrepancy exhibits. **The prediction for `#141` was wrong.**

**Two predictions were missed** — `SI1-5`, which the freeze predicted `CENSUS-EXACT` at MEDIUM,
and `SI1-8`/`#141`, which the freeze predicted would hold. Both are reported as misses rather than
reinterpreted, and neither outcome was softened to preserve a forecast. `#140` was the one question
the freeze declined to predict, and it comes back `RESTATED-ONLY`: not a confirmation of anything,
and not scored.

## Chronology

The property certified is: **no commit reachable from the execution head lies outside `B`'s
descendants.** Asked of the real `pull_request.head.sha`, never of the synthetic merge commit; every
commit of `git rev-list H ^B` required to descend from `B`; recovery included; fail-closed.

This round is **NON-SEALING**. It lands `E` → `L`. There is no pin commit, and `_SI1_SEALED_HEAD`
and `_SI1_MERGE` do not exist — not as `None`, not at all. Every seal constant in the guard file is
left exactly as `B` carries it, and the only change to the record set is this round's own
twenty-two additions.

The claim is scoped to the repository record.
