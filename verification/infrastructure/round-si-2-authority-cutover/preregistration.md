# Seal infrastructure round SI-2 — the bootstrap cutover: PREREGISTRATION

**Control plane only.** This document fixes what `SI-2` will do, what would count as each outcome,
and what no outcome licenses, before any of it is implemented. One file, added. No Lean, no guard
clause, no manifest change, no ROADMAP edit, no manuscript edit.

**The mandated execution base is the merge commit of this pull request**, once that merge and its
`main` push run are themselves certified. The execution branches from exactly that commit and from
nothing else, and its first act is to verify this preregistration's blob at that base.

The base this freeze is written against is `B0` = `66eea646fcbf242df89b168bcce3336ff1b77802`, the
landing merge of `SI-1` (#668), certified by push run 35317349625.

**This document was amended once before execution began.** Its first landing,
`da9d69d60b19482abfeb27b16af5aaebebba0e83` (#669, certified by push run 35321848352), was the
mandated base until a pre-execution dry run at that commit found an interaction between two frozen
contracts, recorded in the amendment section below. **`SI-2` does not resume from `da9d69d6`.** The
mandated execution base is the merge commit of *this* amendment, once it and its `main` push run are
certified through the normal exact-head gates. Every pin and precondition below was re-verified at
`da9d69d6` and is unchanged from `B0`.

## What `SI-2` is, and what it deliberately is not

`SI-1` built a generic seal validator and a per-round seal manifest and proved they agreed with the
existing machinery, while that machinery stayed authoritative for everything that gates. **`SI-2` is
the bootstrap cutover**: it makes the adjudicated derivation rule executable, moves prior-round
authority to the generic validator while keeping the old machinery as a shadow, makes the
data-driven integrity rule authoritative while keeping the per-round comparisons as a shadow, and
rewrites the process protocol so that future rounds seal through the manifest.

**`SI-2` deletes nothing.** Every one of the sixty-one legacy seal-constant assignment statements at
`B0` is present at `SI-2`'s head as exactly the same statement text, in the same relative order —
which `SI2-6`(b) measures as text equality, not as a count. Their retirement is a **separate follow-up
round**, begun from a world in which the generic validator and the new protocol are already
authoritative.

That narrowing is forced by the process rule and is not a stylistic choice. `AGENTS.md` at `B0`
says a non-sealing round "**may not** alter existing seal constants", and says a round that
prospectively takes ownership of changing existing seal state is *sealing*. A round that deleted the
constants while calling itself non-sealing would not be avoiding that rule; it would be contradicting
it. And a round that deleted them while calling itself sealing would enter the circularity `SI-1`'s
freeze named — *sealed by the new mechanism, the mechanism certifies itself; sealed by the old, the
round adds a fresh instance of the pattern it deletes.* Splitting cutover from retirement is what
removes the circularity rather than legislating around it inside one round.

**`SI-2` IS THEREFORE NON-SEALING, `E` → `L`, NO PIN.** It owns no seal state: it creates none and
alters none. It carries a `_SI2_BASE` and act 10's strengthened ancestry check, and **no
`_SI2_SEALED_HEAD`, no `_SI2_MERGE`, no seal triple** — not as `None`, not at all.

## What `SI-2` inherits, and only this

1. `SI-1`'s **certified measurements and artifacts**, at the blobs pinned below.
2. The **adjudicated six-clause derivation rule**, quoted verbatim in the next section.
3. The **owner's disposition of all four `SI-1` census divergences**, quoted in the section after
   it — a policy adjudication of *behaviour*, and not a proof that either implementation is
   generally correct.
4. `#141`'s historical `SI-1` result, which stands at **`RESTATED-AND-FAILS`** and is not rewritten
   by anything this round does.

It inherits no cleanup about `SI-1`'s commit-message bookkeeping: the three prose-only provenance
errors are recorded in `SI-1`'s landing merge and are closed there.

`SI1-7`'s specification is an **input available to be adopted, amended or rejected**, not a mandate.
Its items 3 and 4 — deleting the constants and replacing the comparisons — are **deferred to the
retirement round**, for the reason above. Its item 5 — keep both implementations for one round with
the roles inverted — is **adopted**: that is what this round is.

## THE DERIVATION RULE, ADJUDICATED AND FROZEN

Discrepancy 1 was adjudicated by the owner after `SI-1`'s execution and review and before its
landing, in favour of the union of the visibility targets. The rule, as adjudicated:

- On `push`, derive over the reachable history of `HEAD`.
- On `pull_request`, resolve the real `pull_request.head.sha` **and** the live
  `refs/remotes/origin/<base ref>`, and derive over the **set union** of their reachable histories.
- **Never** substitute `pull_request.base.sha`, a local branch, or the synthetic PR merge.
- If a required target cannot be resolved, **fail closed**.
- Deduplicate commits by SHA. `L` is the unique merge in that union whose non-first parent is
  exactly `E`.
- Zero candidates, multiple candidates, or a unique candidate unequal to the pinned `L` remain
  failures exactly as before.

**This round implements that rule and does not reopen it.** A need to alter it is a result requiring
adjudication, not permission to edit this freeze.

Uniqueness is now tested across a larger set, which is a strengthening and not a weakening. The
pinned `L` remains the independent datum; where the head side and the base side expose two different
candidate landings, the union yields **multiple candidates** and fails rather than choosing one.

## THE FOUR DIVERGENCES, ADJUDICATED AND FROZEN

`SI-1` measured four controls on which the old machinery and the generic validator disagreed. The
owner has now disposed of all four, and `SI-1`'s own frozen semantics decide three of them:

| control | old | `U3` | adjudicated behaviour | ground |
|---|---|---|---|---|
| 10 stale `base.sha`, live base branch carrying `L` | PASS | FAIL under target-only scope | **the old target scope** — `U3` under the union rule must **PASS** | the derivation rule above |
| 7 two candidate landings for one `E` | PASS | FAIL | **`U3`'s** — multiple candidates is a **hard failure** | frozen by `SI-1` as one of three distinct failures |
| 13 a descendant of an unpinned `L` | PASS | FAIL, seal pending | **`U3`'s** — a descendant of an unpinned landing **fails** | frozen by `SI-1` in terms |
| 20 `base-only` where an `EXECUTION`-style check fails | FAIL | PASS, not-applicable | **`U3`'s** — `base-only` is **outside** the lifecycle state machine | frozen by `SI-1` as a first-class kind |

**This is a policy adjudication of behaviour.** It selects which behaviour gates on each control. It
does not hold that either implementation is generally correct, and no outcome of this round may be
read as such a holding.

## The objects `SI-2` builds

**`U1` — the union resolver.** Returns the ordered list of visibility targets for the current event,
each with the reason it was selected, or `None` if a required target does not resolve. It is the
existing `_rbr_archive_visibility_targets` semantics stated once, and both the derivation and the
visibility leg consume it.

**`U2` — the union derivation.** Given `E` and the targets, returns the deduplicated set of merges
whose non-first parent is exactly `E`, over the union of the targets' reachable histories. Zero,
multiple, and unequal-to-pin remain three distinct hard failures with three distinct reasons.

**`U3` — the authoritative validator.** `SI-1`'s `O2` with `U2` in place of the target-only
derivation. After the cutover it is what the **prior-round** clauses call.

**`U4` — the census harness, roles inverted.** `SI-1`'s `O3` with `U3` as the authoritative side and
the old machinery as the shadow. It runs both over every manifest record — twenty-three, the
`SI1` row's shadow comparator being frozen under `SI2-4` — and over the synthetic control suite at
`SI-2`'s **final head**, and emits `census.json` for this round.

**`U5` — the data-driven integrity rule.** One loop over the manifest reporting mutated, removed and
added as three distinct conditions against the record set fixed at `SI2-1`. After the cutover it is
authoritative; the per-round seal-integrity comparisons keep running as a shadow and gate nothing.

## THE ORDER IS PART OF THE CONTRACT, AND THE FINAL HEAD IS THE CHECKPOINT

The stages are ordered, and the order is **gating**, not advisory:

| stage | what it does | may not begin until |
|---|---|---|
| 1 | `SI2-1`: the `SI1` manifest record is added; the record set is **fixed** from here | — |
| 2 | `U1`/`U2` executable and regression-tested | stage 1 |
| 3 | prior-round authority moves to `U3`; old machinery retained as shadow | stage 2's regressions pass |
| 4 | `U5` authoritative; per-round comparisons retained as shadow | stage 3 |
| 5 | the process protocol is updated | stage 3 |
| — | `U4` runs at the **final head** | everything above |

**Durability.** Because nothing is deleted, `SI-2`'s final head `E` *is* the checkpoint: the census
that certifies the cutover is measured at the same commit that carries the cutover, and the
retirement round begins from a world in which that measurement is in the tree. A local measurement
taken before some later commit is not evidence of anything and is not what `SI2-4` accepts.

**Why stage 1 is first.** If the `SI1` record entered the manifest after `U4` ran, the census would
have certified one manifest and the landing would make a different one authoritative. The record set
is fixed at stage 1 and `SI2-1` checks it is unchanged at the final head.

## AMENDMENT BEFORE EXECUTION — the interaction with `R7-SI1`'s frozen manifest contracts

**What was measured, at `da9d69d6`, uncommitted.** `SI1.json` was written in the base-only record
format and the guard file run once. `R7-SI1` **failed**, with `edge_rigidity_probe: FAILURE`, while
every validator agreed: the census reported 23 of 23 records agreeing — 18 `sealed` on lifecycle, 5
`base-only` on schema, pinned base and record integrity — and the four control divergences were
unchanged. What failed were `SI-1`'s **frozen manifest-cardinality contracts in its own guard**:
`len(records) == 22`, `base-only == 4`, the 18/4 record-axis counts, the integrity rule that treats
any record beyond `SI-1`'s twenty-two transcriptions as an unauthorized addition, and the
census-artifact equality, which saw 23 measured rows against a recorded 22. The file was removed;
nothing was committed.

**Why it is an adjudication and not a repair.** `SI2-1` requires the record; `R7-SI1` as frozen
refuses any 23rd record; and `SI2-6`(a) says a changed pre-existing verdict is a result requiring
adjudication that stops the cutover. The owner adjudicated **path D** — amend the control plane
before executing, rather than adjudicate in the record or relax a prior guard unrecorded — and
fixed the amendment's scope as the six points that follow. They are carried into `SI2-1` and
`SI2-6`(a) below and are not widened anywhere else in this document.

1. `R7-SI1`'s twenty-two-record, eighteen-`sealed`, four-`base-only` cardinality contracts and its
   integrity contract are **scoped to the twenty-two records `SI-1` transcribed**.
2. `SI-1`'s existing twenty-two-row `census.json` stays **byte-for-byte unchanged** — not
   regenerated, not repinned. Its blob `7a3e6288c5f532a849a07beb9a8e5757cdf79d04` remains pinned
   below and `R7-SI1`'s artifact check keeps comparing against it.
3. `SI1.json` is **the single addition authorized by `SI2-1`**, outside `SI-1`'s frozen census and
   inside `SI-2`'s `U4` census, where its shadow comparator is already frozen under `SI2-4`.
4. `R7-SI1` is **not otherwise weakened**: all twenty-two original records, their contents, the four
   divergences, and the resulting `PASS` verdict remain frozen.
5. After the amendment lands, the new `main` merge commit is certified through the normal exact-head
   gates, and **`SI-2` resumes only from that newly certified base**, not from `da9d69d6`.
6. On the first post-amendment dry run, `R7-SI1` must be `PASS` on the scoped twenty-two-record set
   and `SI-2`'s comparator must account for the new row. **Any other changed pre-existing verdict is
   still `MAP-CHANGED` and stops execution.**

The scoping edit is permitted to a non-sealing round by §A.37 — it modifies a contract inside an
existing guard and touches no seal constant — and it is permitted to *this* round only because this
amendment says so in advance.

## The targets, FROZEN

Each target names the artifact that decides it. **A target is decided only by that artifact** — a
rule by an executed test, an agreement by the census, a count by the file, a protocol by its text.

**`SI2-0` — locating controls.** The pinned blobs and the preconditions below hold at the mandated
base. Outcomes: `HOLD` / `DRIFTED`. `DRIFTED` stops the round.

**`SI2-1` — the authorized manifest addition, first and then fixed.** Exactly **one** record is
added: `SI1`, `kind: "base-only"`, `base` = `99ab6370470ed9d9e4005551581c6c8c18e54bd2`. It is
added before any other stage, and the record set — twenty-three records, eighteen `sealed` and five
`base-only` — is unchanged at the final head: nothing else added, nothing mutated, nothing removed.
Outcomes: `MANIFEST-AS-AUTHORIZED` / `MANIFEST-DEVIATED`.

**Stage 1 also carries the one authorized edit to a prior round's guard**, per the amendment above:
`R7-SI1`'s cardinality contracts (22 records, 18 `sealed`, 4 `base-only`, and the 18/4 record-axis
counts) and its integrity contract are scoped to **the twenty-two records `SI-1` transcribed**, so
that `R7-SI1` continues to validate exactly the manifest `SI-1` created and reports `SI1.json` as
*the addition `SI2-1` authorizes* rather than as unauthorized. `SI-1`'s `census.json` is **not
regenerated and not repinned**; `R7-SI1`'s artifact check keeps comparing its twenty-two-row census
against the pinned blob. `SI1.json` is outside `SI-1`'s census and inside `U4`. Nothing else in
`R7-SI1` changes: all twenty-two original records, their contents, the four divergences and the
`PASS` verdict remain frozen, and `SI2-6`(a) checks that verdict. `MANIFEST-DEVIATED` also covers a
scoping that reaches beyond these named contracts.

**`SI-2` adds no record for itself.** A prospective round with no manifest record is `EXECUTION`
under the frozen state machine, and that is exactly what `SI-2` is while it runs; a `base-only`
record for `SI-2` written during `SI-2` would report `not-applicable` and quietly switch off this
round's own chronology check. `SI-2`'s record belongs to the retirement round.

**`SI2-2` — the union rule is executable.** `U1` and `U2` exist and are exercised by a regression
suite covering, at minimum: a push event; a pull request whose landing is reachable only from the
head; a pull request whose landing is reachable only from the live base-branch tip; a pull request
where both sides carry the same landing, which must **deduplicate to one candidate** and pass; a
pull request where the two sides carry **different** landings, which must fail as multiple
candidates; an unresolvable base ref, which must fail closed; and `pull_request.base.sha` and the
synthetic merge each offered as a substitute and each **refused**. Outcomes: `DERIVE-UNION-BUILT` /
`DERIVE-UNION-PARTIAL` / `DERIVE-UNION-ABSENT`.

**`SI2-3` — prior-round authority moves, and the old machinery becomes the shadow.** Every ancestry
and archive clause **of a round represented in the manifest** is a call to `U3` keyed on that
round's record, and the old machinery's verdict for that clause is computed alongside and gates
nothing. **Explicitly excluded:** `R7-SI2`'s own bootstrap chronology guard, which reads `_SI2_BASE`
and runs act 10's strengthened check exactly as `SI-1`'s did, because `SI-2` has no manifest record
by design. Measured as: the count of prior-round clauses that gate on `U3`, the count that still gate
on a legacy constant (required zero), and the count of surviving *shadow* reads of legacy constants
(reported, not bounded). Outcomes: `AUTHORITY-MOVED` / `AUTHORITY-PARTIAL`.

**`SI2-4` — the census at the final head matches the adjudicated delta profile.** `U4` runs at
`SI-2`'s final head. The frozen expectation, stated so it can fail:

- **records:** all twenty-three agree — eighteen `sealed` on lifecycle, five `base-only` on schema,
  pinned base and record integrity. **The twenty-third row is the `SI1` record added at `SI2-1`, and
  its old-side comparator is frozen here rather than left to the execution:** the shadow verdict is
  the strengthened execution ancestry check that `R7-SI1` itself runs against `_SI1_BASE`, which is
  exactly how the four existing `base-only` rows take theirs from their rounds' `_*_BASE` checks; it
  is compared on the `base-only` axis and on no other; and the row is admitted to the census only if
  `_SI1_BASE` and `SI1.json`'s `base` are the same commit, so that the two sides are answering about
  one object. If that transcription check fails, the row is reported as `no-analogue` and `SI2-4`
  counts twenty-two agreeing records and one unresolved row, which is `DELTA-UNEXPECTED`;
- **controls:** the nine no-analogue rows remain no-analogue; of the twelve comparable rows,
  **exactly three diverge — 7, 13 and 20 — each in `U3`'s adjudicated direction**, and **control 10
  agrees** with both sides passing; 11 and 12 agree with both sides failing.

Outcomes: `DELTA-AS-ADJUDICATED` / `DELTA-UNEXPECTED` / `DELTA-BROKEN`. **`DELTA-UNEXPECTED`** is any
comparable row diverging that is not one of 7, 13, 20, or control 10 still diverging, or one of 7,
13, 20 diverging in the other direction; it is reported, not repaired, and stops the round.
**`DELTA-BROKEN`** is a record-axis disagreement. This target is **not** called equivalence, because
the profile it accepts contains three intentional behavioural deltas.

**`SI2-5` — integrity becomes data-driven, with the comparisons as shadow.** `U5` gates; mutated,
removed and added are reported separately; the per-round seal-integrity comparisons still run and
their verdicts are recorded alongside `U5`'s. Outcomes: `INTEGRITY-DATA-DRIVEN` /
`INTEGRITY-PARTIAL`.

**`SI2-6` — the verdict map and the legacy state are preserved.** Two measurements. (a) The base's
guard file is run, its check tags and verdicts measured, and compared with the tags and verdicts at
`SI-2`'s head: `MAP-PRESERVED` / `MAP-CHANGED`. A changed verdict on any pre-existing tag is a
**result requiring adjudication**; `MAP-CHANGED` stops the cutover and reports rather than failing
silently or being adopted. **The first post-amendment dry run is part of this target**: with
`SI1.json` present and `R7-SI1` scoped as `SI2-1` authorizes, `R7-SI1` must be `PASS` on its
twenty-two-record set and `SI-2`'s comparator must account for the twenty-third row; that one
verdict is the amendment's whole allowance, and **any other changed pre-existing verdict is
`MAP-CHANGED` and stops execution**, the amendment notwithstanding. (b) The **sixty-one** legacy assignment statements — **fifty-nine
distinct names** — at the head are, **as text, exactly the sixty-one at `B0`, in the same relative
order**: the check extracts the module-level `_<STEM>_(BASE|SEALED_HEAD|MERGE) = ...` lines from
both revisions and requires the two sequences to be equal, per the inventory below. Statement count
alone cannot establish this and is not what is measured. `LEGACY-INTACT` / `LEGACY-ALTERED`. `LEGACY-ALTERED` **fails the round**, because a
non-sealing round may not alter existing seal constants.

**`SI2-7` — the process protocol is updated for the manifest.** `AGENTS.md` §A.37 is amended,
prospectively and for rounds begun after the amendment, so that it states: what a sealing round's
`P` writes — **its round's manifest record**, `sealed_head` = `E` and `merge` = `L`, under
`verification/seals/`, and **not** a legacy constant; how a new `sealed` record is created and how a
completed non-sealing round's `base-only` record is created; and the status of the legacy constants
after this round, stated in two halves that must both appear: **from `SI-2`'s landing they cease to
GATE** — no check's verdict depends on them, and a round that writes a new one has recreated the
representation this round retired — **and until the retirement round they remain PROTECTED
HISTORICAL SEAL STATE**, so altering or removing any of them constitutes taking ownership of existing
seal state under §A.37 and makes the round that does it *sealing*. It follows, and the amendment
says so, that **the retirement round is sealing and its `P` writes its own `sealed` manifest record
under the new protocol** — `sealed_head` = its `E`, `merge` = its `L` — and writes no legacy
constant. The amendment is quoted in the result note.
Outcomes: `PROTOCOL-UPDATED` / `PROTOCOL-PARTIAL` / `PROTOCOL-ABSENT`. **Without this target, the
standing text at `B0` instructs the next sealing round to do exactly what `SI-2` retires.**

**`SI2-8` — `#140` and `#141` restated under `U3`.** `#141` is re-evaluated against `U3`: does the
authoritative model now evaluate prior seals against the landing topology rather than the
pull-request head? Outcomes: `RESTATED-AND-HOLDS` / `RESTATED-AND-FAILS` / `RESTATED-ONLY`. `#140`
remains `RESTATED-ONLY` unless an independent source for each round's mandated base is produced,
which this round does not undertake. **`SI-1`'s recorded `#141` result is not edited** whatever
`SI2-8` finds; a later verdict is a later verdict.

## Predictions, with strength

| target | predicted | strength |
|---|---|---|
| `SI2-0` | `HOLD` | HIGH |
| `SI2-1` | `MANIFEST-AS-AUTHORIZED` | HIGH |
| `SI2-2` | `DERIVE-UNION-BUILT` | HIGH |
| `SI2-3` | `AUTHORITY-MOVED` | MEDIUM |
| `SI2-4` | **`DELTA-AS-ADJUDICATED`**: 7, 13, 20 diverge in `U3`'s direction; 10 agrees | MEDIUM |
| `SI2-5` | `INTEGRITY-DATA-DRIVEN` | MEDIUM |
| `SI2-6` | `MAP-PRESERVED` and `LEGACY-INTACT` | MEDIUM |
| `SI2-7` | `PROTOCOL-UPDATED` | HIGH |
| `SI2-8` | `RESTATED-AND-HOLDS` for `#141`; `RESTATED-ONLY` for `#140` | LOW for `#141` |

**`SI2-4` is the round's sharpest claim.** Under the union rule the `SI-1` divergence on control 10
should **disappear**, because `U3` now sees the base-branch tip; the other three should **persist,
in `U3`'s direction**, because nothing in this round touches the behaviours that produce them. A
still-divergent control 10 means the rule was not implemented as adjudicated. A newly divergent
control, or one of 7, 13, 20 flipping direction, means the implementation changed something the
adjudication did not authorize. Either is reported, not repaired.

`#141` is predicted to hold at LOW strength deliberately: it failed in `SI-1` for exactly the reason
the adjudication addresses, so holding is the expected outcome and a weak prediction. A failure
would be the informative result, and would mean the union rule does not deliver what `#141`
requires.

## The negative suite

`SI-1`'s twenty cases remain in force. These are added, and **each must satisfy its named outcome for
its named reason** — some are `PASS` controls:

1. A pull request whose landing is on the live base branch and not reachable from the head —
   **passes** under `U3`. This is `SI-1`'s control 10 and it is the adjudication made executable.
2. The same, with the base branch rewound off the landing — **fails**.
3. An unresolvable remote base ref — **fails closed**, and `pull_request.base.sha` is not accepted
   in its place even when present and well-formed.
4. Head and base each carrying a **different** merge with `E` as non-first parent — **fails as
   multiple candidates**, not resolved in favour of either.
5. Head and base carrying the **same** landing — **passes with exactly one candidate** after
   deduplication; a validator that reports two has not deduplicated.
6. The synthetic PR merge offered as a target — **refused**.
7. A manifest record whose `merge` is rewritten to a merge that genuinely exists in the union —
   **fails on pin-versus-derived disagreement**, the case that proves derivation alone is not enough.
8. A manifest record added beyond `SI2-1`'s single authorization — **fails** as an unauthorized
   addition under `U5`.
9. Any one of the sixty-one legacy assignment statements removed, re-valued, or reordered relative
   to the others at the head — **fails `SI2-6`(b)**. `_RNT_SEALED_HEAD` and `_RNT_MERGE` are each
   assigned twice; removing **either** of a pair must fail, so the check counts statements and not
   names.
10. A prior-round clause found still gating on a legacy constant — **fails `SI2-3`**; a *shadow*
    read of the same constant does not.
11. `R7-SI2`'s own chronology guard rewritten to key on a manifest record — **fails**, because
    `SI-2` has none and the bootstrap guard is excluded from the cutover by design.
12. A **twenty-fourth** record present beyond `SI1.json` — **fails both** the scoped `R7-SI1`
    integrity contract and `U5`, as an unauthorized addition: the scoping admits the one record
    `SI2-1` authorizes and nothing else, which is what "not otherwise weakened" means mechanically.

## What no outcome of this round licenses

1. Any change to a historical `B`, `E`, `L` or `P`, or to any preregistration or result note,
   `SI-1`'s included.
2. Any claim that the generic validator is *correct*, as distinct from *in agreement where it
   agrees, adjudicated where it differs, and now authoritative*. Authority is a decision;
   correctness is not conferred by it.
3. Any re-opening of the adjudicated derivation rule or of the four adjudicated divergences.
4. Any deletion, re-valuing or renaming of a legacy seal constant.
5. Any statement about Act 21's targets, or that Act 21 may open.
6. Any claim that a `MAP-CHANGED` verdict is acceptable because the new mechanism is better.
7. Any retrofit. Every historical `B`, `E`, `L`, `P` stays exactly where it is.
8. Any claim that the retirement round is safe because `SI-2` was green: it carries its own evidence
   obligations.

## Hazards

**H1 — the shadow that gates.** After the cutover the old machinery still runs. A clause that
consults its verdict, or a `check()` whose truth depends on it, has quietly kept the old authority.
`SI2-3` counts gating reads and requires zero; negative case 10 exists for this.

**H2 — the double assignment.** `RNT`'s sealed head and merge are each assigned twice at `B0` — the
pin, and the clause-9 self-test rebinding to `('f' * 40, 'e' * 40)`. Any accounting by *names* sees
fifty-nine and misses a removed statement; `SI2-6`(b) counts **statements**. Negative case 9 exists
for this, and the inventory below keeps both numbers.

**H3 — self-certification.** `SI-2` takes authority and then lands. It is non-sealing, so the landing
is certified the way `SI-1`'s was — the bootstrap chronology guard, the exact-head CI, the `main`
push run — and not by the validator it installed.

**H4 — a moved verdict read as an improvement.** After the cutover a pre-existing tag may change
verdict because `U3` genuinely answers differently. That is a finding about the record and requires
adjudication; `SI2-6`(a) reports it and the round stops rather than adopting it.

**H5 — the manifest that moves under the census.** If a record entered or changed after `U4` ran,
the certified census and the authoritative manifest would differ. Stage 1 fixes the record set first
and `SI2-1` checks it at the final head.

**H6 — the census that is not re-measured.** `SI-1`'s census is evidence about `SI-1`'s head under
the target-only rule. It is not evidence about `SI-2`'s head under the union rule. `SI2-4`
re-measures; quoting `SI-1`'s numbers would be quoting the wrong experiment.

**H7 — the protocol left behind.** Code that is manifest-driven under a process text that still says
"`P` sets the constants" produces a next sealing round that does both, or the wrong one. `SI2-7`
exists for this and is not optional.

**H8 — inheriting more than was certified.** `SI1-7` is a specification of type P, and the owner's
adjudications are of behaviour. Neither licenses redesigning the model beyond the union rule, the
cutover, and the protocol.

## The legacy seal-constant inventory at `B0`, FROZEN

Sixty-one module-level assignment **statements** over fifty-nine distinct **names** across
twenty-three stems, measured at `B0`. `SI-2` preserves all of them; the retirement round consumes
this table.

| stems | shape | names | statements |
|---|---|---|---|
| `A12P` `A6D` `A6I` `A6P` `CTI` `HYA` `HYB` `HYE` `PC4` `PC4S` `PQT` `RNC` `SGT` `TCF` `TRJ` `WTS` `XTS` | `BASE` + `SEALED_HEAD` + `MERGE` | 51 | 51 |
| `RNT` | `BASE` + `SEALED_HEAD` ×2 + `MERGE` ×2 | 3 | 5 |
| `ABR` `CLG` `RBR` `TSG` | `BASE` only | 4 | 4 |
| *(the twenty-two manifested rounds)* | | **58** | **60** |
| `SI1` | `BASE` only | 1 | 1 |
| **total** | | **59** | **61** |

Once `SI1` has its manifest record — which `SI2-1` adds — every one of the fifty-nine names and
sixty-one statements is legacy data for a manifested round, and the retirement round's deletion
target is **59 names / 61 statements**, not a smaller number remembered from before the record was
added. The execution reports against this table and not against prose.

## Start state, pinned

| path | blob at `B0` |
|---|---|
| `verification/infrastructure/round-si-1-shadow-seal-validator/preregistration.md` | `4a5f183a52b2720e0714049ecf34911c55c1ef61` |
| `verification/infrastructure/round-si-1-shadow-seal-validator/result.md` | `3e034dfd4b74978adf8b9a8e4bc4339885a4b65d` |
| `verification/infrastructure/round-si-1-shadow-seal-validator/census.json` | `7a3e6288c5f532a849a07beb9a8e5757cdf79d04` |
| `verification/infrastructure/round-si-1-shadow-seal-validator/si1-tagmap.json` | `057cdf90ed9d9f0e129a076a327dcc6f089f53df` |
| `AGENTS.md` | `3e3f00454db033b4fc519fd1123cd3f9b7f7cf24` |
| `verification/seals/` (tree) | `97faa0e6b1eae3079b90ed57d6dda45e6d1e71d6` |

**Preconditions, each checkable mechanically at the mandated base:**

1. `R7-SI2` does not appear in `verification/lean/edge_rigidity_probe.py`. Verified at `B0`: 0
   occurrences.
2. `_SI2` does not appear in that file. Verified at `B0`: 0 occurrences.
3. `verification/seals/` holds exactly 22 records, 18 `sealed` and 4 `base-only`, and no `SI1`
   record.
4. `R7-SI1` passes at the base and its census reconstructs identically.
5. The guard file carries exactly 61 legacy assignment statements over 59 distinct names, per the
   inventory. Verified at `B0`.
6. `main` is exactly `66eea646fcbf242df89b168bcce3336ff1b77802` and that commit's second parent is
   `d75427aece402e1629d56d1ca96fbc8d3c8101e8`.
7. No `SI-2` record exists in the manifest.
8. `AGENTS.md` §A.37 at `B0` still says "`P` sets the constants it owns to `E` and to `L`" — the
   sentence `SI2-7` supersedes prospectively.
9. `R7-SI1`'s cardinality and integrity contracts are **unscoped** at the mandated base — they still
   read `== 22`, `== 18`, `== 4` over the whole manifest — so that the scoping is this round's own
   recorded edit and not something already present. Verified at `da9d69d6`.
10. The mandated base is the merge commit of this amendment and not `da9d69d6`; that commit is
    recorded as the certified pre-amendment base from which nothing resumes.

## The guard

Fresh tag **`R7-SI2`**, stem **`_SI2_`**. It carries `_SI2_BASE`, act 10's strengthened ancestry
check asked of the real `pull_request.head.sha` and never of the synthetic merge, fail-closed, this
preregistration pinned **by blob** with a one-byte drift control, and **no seal triple of its own**.
It is the one guard in the file that is **not** cut over, and it says so.

Content contracts hold the result note to the distinctions this freeze makes: the ordered stages and
the final head as checkpoint, the four divergences carried as adjudicated behaviour and never as
correctness, `SI-1`'s `#141` result not rewritten, the authorized addition being exactly one and
first, the `R7-SI1` scoping recorded as the amendment's single allowance and bounded to the named
contracts, the legacy inventory intact by statement text, and the protocol amendment quoted. Each
contract is mutation-tested against the exact failure it exists to catch.

**Four definition slots** are budgeted for the round's own new definitions, as `SI-1` had; unused
slots are recorded as unused.

## The retirement round, named and not begun

A follow-up round, begun only from a certified `SI-2` landing, adds `SI-2`'s own `base-only`
record, deletes the fifty-nine names and sixty-one statements against the inventory above, removes
the per-round seal-integrity comparisons that `U5` shadows, and lands under the protocol `SI2-7`
wrote. Because it alters and removes protected historical seal state it is **sealing** under §A.37 as
amended by `SI2-7`, and its `P` writes its own `sealed` manifest record — `sealed_head` = its `E`,
`merge` = its `L` — and no legacy constant. Nothing here freezes it; this section exists so the deferral is
recorded as a plan and not as an omission.

## Chronology

The execution branches from the mandated base and from no other commit, and certifies that ancestry
in act 10's strengthened form: the base an ancestor of the head, and every commit of
`rev-list HEAD ^base` a descendant of the base, recovery included, fail-closed, asked of the real
pull-request head.

Act 21 remains closed throughout `SI-2` and is not opened by any outcome here.
