# Seal infrastructure round 1 — the shadow validator and the equivalence census: RESULT

Executed from the mandated base `B` = `99ab6370470ed9d9e4005551581c6c8c18e54bd2`, the merge commit
of the control plane (PR #667), and from no other commit. The freeze read out of that base carries
the blob `4a5f183a52b2720e0714049ecf34911c55c1ef61` the guard names.

**This round is NON-SEALING and NON-AUTHORITATIVE.** The existing per-round machinery remains
authoritative for every check that gates. The generic validator built here runs, reports, and is
compared against it; it decides nothing. **Presence is not authority** — the new code being in the
tree does not make it the instrument, and `SI1-6` establishes that mechanically rather than
asserting it. The instant this validator decides anything, that is `SI-2`.

## Outcomes

| target | outcome | decided by |
|---|---|---|
| `SI1-0` | locating controls hold | the six pinned blobs and eight preconditions, checked at `B` |
| `SI1-1` | **`SCHEMA-BUILT`** | 22 records under `verification/seals/`, every value byte-identical to the freeze's table |
| `SI1-2` | **`VALIDATOR-BUILT`** | the three states, `base-only` held out of the machine, no stem in the validator region |
| `SI1-3` | **`DERIVE-EXACT`** | 18 of 18, exactly one candidate each, agreeing with the pin |
| `SI1-4` | **`NEGATIVES-COMPLETE`** | all **20 frozen negative cases** satisfy their required outcomes, in 21 case rows |
| `SI1-5` | **`CENSUS-EXACT`** | 22 of 22 records agree, on the axis each is on |
| `SI1-6` | **`SHADOW-ONLY`** | 90 pre-existing tags, identical verdicts, none removed |
| `SI1-7` | delivered | the `SI-2` specification below |
| `SI1-8` | **`RESTATED-AND-HOLDS`** for `#140` and for `#141` | 18 of 18 and 22 of 22, measured |

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

**Does it change a target verdict? No.** `SI1-3` is `DERIVE-EXACT` and stays `DERIVE-EXACT`: at this
execution head, on a push, the frozen rule does agree with the pin for 18 of 18 with exactly one
candidate each, and that measurement is not weakened by the finding. This is a **scope and
interpretation finding** about a configuration this head does not occupy, and softening a target
because the validator has a limit elsewhere would misreport what was measured. The target passes and
the finding stands, separately.

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

### DISCREPANCY 2 — cases 10, 11 and 12 are exercised on the visibility layer, and had to be

**Recorded, not repaired.** These three are the retained stale-base / live-base controls. They are
exercised against the base-branch-tip resolution plus reachability, **not** against `O2`'s
derivation, because under the frozen scope the derivation answers first: with the landing absent
from the head, derivation reports zero candidates and the visibility leg never speaks. Case 11 as
worded — a visibility failure — is therefore **unsatisfiable through the derivation path**, and
routing it through the layer where the behaviour actually lives is a reading this round took rather
than a freeze change. It is the same defect as Discrepancy 1 seen from the test side, and the same
adjudication settles both.

## `SI1-5` — the agreement census

`census.json` carries the machine-readable table. **22 of 22 records agree**, and the axes are
distinguished:

| axis | records | new lifecycle | agreement |
|---|---|---|---|
| lifecycle | 18 `sealed` | `ARCHIVED` ×18 | 18 of 18 |
| schema + pinned base + record integrity | 4 `base-only` | `not-applicable` ×4 | 4 of 4 |

The old machinery's verdict was taken from the generic helpers the per-round clauses themselves
call — the archive-mode certificate for a sealed round, the strengthened execution check for a
non-sealing one — run in the same process and on the same repository state, so the census compares
like with like rather than comparing the new validator against a paraphrase of the old one.

**This is an agreement census and not a proof of correctness.** It shows the two implementations do
not differ on the cases presented, and it would not detect an error both share. Both were written in
one round from one specification, which is exactly the circumstance in which a shared misreading is
possible; the twenty negative cases exist because agreement on the positive cases is the weaker half
of the evidence.

### An observation, recorded and not a divergence

On the four `base-only` rounds the two implementations agree on the verdict and differ in **why**.
The old machinery applies the strengthened *execution* ancestry check to them and passes today. The
new validator does not classify them at all. Verdicts therefore agree, and the census records
agreement; but the old reading is the one that would fail if sibling history ever appeared in their
targets — which is precisely the condition that reddened `main` over act 20's `L` before its pin.
The new reading is immune to it by construction. Nothing is claimed beyond this, and no verdict
changed.

## `SI1-6` — non-authority, checked mechanically

- No seal constant and no prior-seal comparison was removed: the set of
  `_*_(BASE|SEALED_HEAD|MERGE)` assignments at the execution head equals the set at `B`.
- **90 pre-existing check tags** at `B`, **90** at the execution head, **none removed**, and **no
  pre-existing tag's verdict changed**.

  **What was compared, stated so it cannot later be misread.** The unit is a **check tag** — the
  `R7-*`, `R8`, `R9` and numbered identifiers that `check()` prints one `PASS`/`FAIL` line for. Not
  ninety files, not ninety seal records, not ninety assertions. The guard file was taken from `B`
  with `git show` and run; the guard file at the execution head was run; every `PASS`/`FAIL` line
  was parsed into a tag-to-verdict map, and the two maps were compared key by key. Result: 90 keys
  each side, zero keys removed, zero verdicts changed, and the one key added is `R7-SI1` itself
  (91 at the head in total). Both runs report `edge_rigidity_probe: ALL CHECKS PASS`.
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

Four defects were in **this round's own implementation**, not in the freeze. They were execution
errors, they were corrected, and they are recorded here so that the distinction between *a defect
the implementation may fix* and *evidence about the preregistered rule* is on the record rather than
left to a reader to infer.

| # | defect | how it showed | corrected by |
|---|---|---|---|
| 1 | the schema checked **unknown keys before forbidden fields**, so a `base-only` record carrying `sealed_head` was reported as a stray key rather than as a seal asserted for a round that has none | negative cases 4a and 4b failed on the reason, not the colour | checking forbidden before unknown; the diagnosis is the value of the check |
| 2 | the record reader was passed **absolute paths**, which `_artifact` resolves relative to `verification/`, yielding a path under `verification/` and a missing file | all 22 records loaded as `unreadable` while the directory listing found them | listing absolutely, reading by relative name |
| 3 | four content contracts matched **substrings that crossed line breaks**, so a true claim in the note read as absent | three contracts false against a correct note | matching on collapsed whitespace: the words are the claim, the wrapping is not |
| 4 | the seal-constant check asserted **set equality** between head and base, which this round's own `_SI1_BASE` necessarily breaks | the check failed while no other round's seal had moved | containment plus an exact allowance for this round's own base — which is also how a round that re-pinned another round's seal is caught |

None of the four is a finding about the freeze, and none of them is counted among the discrepancies
below. Defects 1 and 4 also improved the checks they were in, which is recorded as what it is and
not as a discovery.

## Discrepancies, recorded and not repaired

These are **evidence about the preregistered contract**, not implementation errors, and none was
repaired.

1. **The frozen derivation scope reintroduces the base-age false negative** on a pull request from a
   historical base. Measured. Remedy proposed, not applied. Requires adjudication before `SI-2`.
2. **Cases 10, 11 and 12 are exercised on the visibility layer**, case 11 being unsatisfiable
   through the derivation path under the frozen scope. The same adjudication settles it.
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
| `SI1-5` | `CENSUS-EXACT`, MEDIUM | `CENSUS-EXACT` | as predicted |
| `SI1-6` | `SHADOW-ONLY`, MEDIUM | `SHADOW-ONLY` | as predicted |
| `SI1-7` | delivered, HIGH | delivered | as predicted |
| `SI1-8` `#141` | `RESTATED-AND-HOLDS` | `RESTATED-AND-HOLDS` | as predicted |
| `SI1-8` `#140` | **NOT PREDICTED** | `RESTATED-AND-HOLDS` | **not scored.** The freeze put nothing at risk here and nothing is scored |

`#140` is restated as a schema and global invariant over the manifest and then **measured**: for
every one of the eighteen `sealed` rounds, the execution branch root's single parent is exactly the
pinned base, and all twenty-two pinned bases are merge commits. That is `A.37`'s own invariant asked
generically of the data rather than of eighteen hand-written constants. **18 of 18 and 22 of 22.**
The freeze declined to predict this and the round does not treat the clean result as a confirmation
of anything the freeze said.

## Chronology

The property certified is: **no commit reachable from the execution head lies outside `B`'s
descendants.** Asked of the real `pull_request.head.sha`, never of the synthetic merge commit; every
commit of `git rev-list H ^B` required to descend from `B`; recovery included; fail-closed.

This round is **NON-SEALING**. It lands `E` → `L`. There is no pin commit, and `_SI1_SEALED_HEAD`
and `_SI1_MERGE` do not exist — not as `None`, not at all. Every seal constant in the guard file is
left exactly as `B` carries it, and the only change to the record set is this round's own
twenty-two additions.

The claim is scoped to the repository record.
