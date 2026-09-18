# Seal infrastructure round SI-2 — the authority cutover: PREREGISTRATION

**Control plane only.** This document fixes what `SI-2` will do, what would count as each outcome,
and what no outcome licenses, before any of it is implemented. One file, added. No Lean, no guard
clause, no manifest change, no ROADMAP edit, no manuscript edit.

**The mandated execution base is the merge commit of this pull request**, once that merge and its
`main` push run are themselves certified. The execution branches from exactly that commit and from
nothing else, and its first act is to verify this preregistration's blob at that base.

The base this freeze is written against is `B0` = `66eea646fcbf242df89b168bcce3336ff1b77802`, the
landing merge of `SI-1` (#668), certified by push run 35317349625.

## What `SI-2` is

`SI-1` built a generic seal validator and a per-round seal manifest and proved they agreed with the
existing machinery, while that machinery stayed authoritative for everything that gates. **`SI-2` is
the cutover.** It makes the adjudicated derivation rule executable, moves authority to the generic
validator, and then removes the duplicated per-round state that the validator replaces.

`SI-1`'s freeze named the circularity this round has to avoid:

> sealed by the new mechanism, the mechanism certifies itself; sealed by the old, the round adds a
> fresh instance of the pattern it deletes and reopens the red `L`-to-`P` window it exists to close.

**`SI-2` IS NON-SEALING, `E` → `L`, NO PIN**, for that reason. It carries a `_SI2_BASE` and act 10's
strengthened ancestry check, and **no `_SI2_SEALED_HEAD`, no `_SI2_MERGE`, no seal triple** — not as
`None`, not at all. A round whose purpose is to delete fifty-eight seal constants does not begin by
creating three more, and a round that has just taken authority does not certify its own landing with
the mechanism it just installed. Neither horn is entered because no seal is produced.

This is a settlement, not a derivation from the freeze that precedes it, and it is the first thing
the owner should reject if it is wrong.

## What `SI-2` inherits, and only this

1. `SI-1`'s **certified measurements and artifacts**, at the blobs pinned below.
2. The **adjudicated six-clause derivation rule**, quoted verbatim in the next section.
3. The **narrow adjudication** that on census control 10 the old machinery's target scope is the
   correct one.
4. The fact that **the other three census divergences — 7, 13 and 20 — remain unadjudicated**.
5. `#141`'s historical `SI-1` result, which stands at **`RESTATED-AND-FAILS`** and is not rewritten
   by anything this round does.

It inherits no cleanup about `SI-1`'s commit-message bookkeeping: the three prose-only provenance
errors are recorded in `SI-1`'s landing merge and are closed there.

`SI1-7`'s specification is an **input available to be adopted, amended or rejected**, not a mandate.
Where this freeze departs from it, the departure is stated.

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

**Uniqueness is now tested across a larger set, which is a strengthening and not a weakening.** The
pinned `L` remains the independent datum; where the head side and the base side expose two different
candidate landings, the union yields **multiple candidates** and fails rather than choosing one.

## The objects `SI-2` builds

**`U1` — the union resolver.** Returns the ordered list of visibility targets for the current event,
each with the reason it was selected, or `None` if a required target does not resolve. It is the
existing `_rbr_archive_visibility_targets` semantics stated once, and the derivation and the
visibility leg both consume it.

**`U2` — the union derivation.** Given `E` and the targets, returns the deduplicated set of merges
whose non-first parent is exactly `E`, over the union of the targets' reachable histories. Zero,
multiple, and unequal-to-pin remain three distinct hard failures with three distinct reasons.

**`U3` — the authoritative validator.** `SI-1`'s `O2` with `U2` in place of the target-only
derivation. After the cutover it is what the per-round clauses call.

**`U4` — the equivalence harness.** Runs the old machinery and `U3` over all manifest records and
over the synthetic control suite at `SI-2`'s own head, and emits `census.json` for this round. It
gates `SI2-3` and nothing else.

**`U5` — the data-driven integrity rule.** One loop over the manifest replacing the per-round
seal-integrity comparisons: mutated, removed and added reported as three distinct conditions against
the record set at `SI-2`'s base.

## THE ORDER IS PART OF THE CONTRACT

The three stages are ordered, and the order is **gating**, not advisory:

| stage | what it does | may not begin until |
|---|---|---|
| 1 | `U1`/`U2` executable and regression-tested | — |
| 2 | authority moves to `U3` | stage 1's regressions pass |
| 3 | constants deleted, integrity replaced by `U5` | **`SI2-3` demonstrates equivalence at `SI-2`'s head** |

A single commit performing stage 3 without `SI2-3` having been measured fails the round, whatever
its verdicts. The whole point of the split is that deletion is irreversible in practice: once the
constants are gone, the evidence that they agreed with the manifest cannot be re-derived from the
tree.

## The targets, FROZEN

Each target names the artifact that decides it. **A target is decided only by that artifact** — a
rule by an executed test, an agreement by the census, a count by the file.

**`SI2-0` — locating controls.** The pinned blobs and the preconditions below hold at the mandated
base. Outcomes: `HOLD` / `DRIFTED`. `DRIFTED` stops the round.

**`SI2-1` — the union rule is executable.** `U1` and `U2` exist and are exercised by a regression
suite covering, at minimum: a push event; a pull request whose landing is reachable only from the
head; a pull request whose landing is reachable only from the live base-branch tip; a pull request
where both sides carry the same landing, which must **deduplicate to one candidate** and pass; a
pull request where the two sides carry **different** landings, which must fail as multiple
candidates; an unresolvable base ref, which must fail closed; and `pull_request.base.sha` and the
synthetic merge each offered as a substitute and each **refused**. Outcomes: `DERIVE-UNION-BUILT` /
`DERIVE-UNION-PARTIAL` / `DERIVE-UNION-ABSENT`.

**`SI2-2` — authority moves.** Every per-round ancestry and archive clause is a call to `U3` keyed
on that round's manifest record. Measured as: no per-round clause reads a `_*_BASE`,
`_*_SEALED_HEAD` or `_*_MERGE` constant any longer, and the count of surviving reads is reported.
Outcomes: `AUTHORITY-MOVED` / `AUTHORITY-PARTIAL`.

**`SI2-3` — equivalence at this round's own head.** `U4` runs both implementations over the manifest
and the control suite at `SI-2`'s head. Outcomes: `EQUIV-AS-PREDICTED` / `EQUIV-DIVERGENT-ELSEWHERE`
/ `EQUIV-BROKEN`. The frozen expectation is stated as a prediction below and is **falsifiable**: it
is the one place this round can discover that the adjudicated rule does something nobody expected.

**`SI2-4` — the duplicated state is removed.** The seal constants for the twenty-two recorded rounds
are deleted from the guard file. Measured as a count, against the inventory frozen below. Outcomes:
`CONSTANTS-REMOVED` / `CONSTANTS-PARTIAL`. **`SI-2`'s own `_SI2_BASE` is not among them and is not
deleted.**

**`SI2-5` — integrity becomes data-driven.** `U5` replaces the per-round seal-integrity comparisons,
with mutated, removed and added reported separately. Outcomes: `INTEGRITY-DATA-DRIVEN` /
`INTEGRITY-PARTIAL`.

**`SI2-6` — the verdict map is preserved.** The base's guard file is run, its check tags and verdicts
measured, and compared with the tags and verdicts at `SI-2`'s head. Outcomes: `MAP-PRESERVED` /
`MAP-CHANGED`. A changed verdict on any pre-existing tag is a **result requiring adjudication**, not
a thing to repair silently, and `MAP-CHANGED` does not by itself fail the round — it stops the
cutover and reports.

**`SI2-7` — the authorized manifest addition.** Exactly **one** record is added: `SI1`, `kind:
"base-only"`, `base` = `99ab6370470ed9d9e4005551581c6c8c18e54bd2`. No other record is added,
mutated or removed. Outcomes: `MANIFEST-AS-AUTHORIZED` / `MANIFEST-DEVIATED`.

**`SI-2` adds no record for itself.** A prospective round with no manifest record is `EXECUTION`
under the frozen state machine, and that is exactly what `SI-2` is while it runs; a `base-only`
record for `SI-2` written during `SI-2` would report `not-applicable` and quietly switch off this
round's own chronology check. `SI-2`'s record, if any, belongs to a later round.

**`SI2-8` — `#140` and `#141` restated under the new rule.** `#141` is re-evaluated against `U3`:
does the built model now evaluate prior seals against the landing topology rather than the
pull-request head? Outcomes: `RESTATED-AND-HOLDS` / `RESTATED-AND-FAILS` / `RESTATED-ONLY`. `#140`
remains `RESTATED-ONLY` unless an independent source for each round's mandated base is produced,
which this round does not undertake. **`SI-1`'s recorded `#141` result is not edited** whatever
`SI2-8` finds; a later verdict is a later verdict.

## Predictions, with strength

| target | predicted | strength |
|---|---|---|
| `SI2-0` | `HOLD` | HIGH |
| `SI2-1` | `DERIVE-UNION-BUILT` | HIGH |
| `SI2-2` | `AUTHORITY-MOVED` | MEDIUM |
| `SI2-3` | **the census at this head shows THREE divergences — 7, 13, 20 — and control 10 AGREES** | MEDIUM |
| `SI2-4` | `CONSTANTS-REMOVED`, 58 of 58 | MEDIUM |
| `SI2-5` | `INTEGRITY-DATA-DRIVEN` | MEDIUM |
| `SI2-6` | `MAP-PRESERVED` | MEDIUM |
| `SI2-7` | `MANIFEST-AS-AUTHORIZED` | HIGH |
| `SI2-8` | `RESTATED-AND-HOLDS` for `#141`; `RESTATED-ONLY` for `#140` | LOW for `#141` |

**The `SI2-3` prediction is the round's sharpest claim.** `SI-1` measured four divergent controls —
7, 10, 13 and 20 — where control 10 was the old machinery passing through the base-branch tip while
the target-only derivation failed with zero candidates. Under the adjudicated union rule that
divergence should **disappear**, because `U3` now sees the base-branch tip too. If control 10 still
diverges, the rule was not implemented as adjudicated. If a control that agreed in `SI-1` now
diverges, the implementation changed something the adjudication did not authorize. Either is
`EQUIV-DIVERGENT-ELSEWHERE` and is reported, not repaired.

`#141` is predicted to hold at LOW strength deliberately. It failed in `SI-1` for exactly the reason
the adjudication addresses, so holding is the expected outcome and a weak prediction; what would be
informative is a failure, and a failure would mean the union rule does not deliver what `#141`
requires.

## The negative suite

Carried forward from `SI-1`'s twenty cases, which remain in force, plus these, each of which must
fail **for its named reason**:

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
   **fails on pin-versus-derived disagreement**, which is the case that proves derivation alone is
   not enough.
8. A seal constant deleted while its manifest record is absent — **fails**: the round may not lose a
   round's seal data by deleting both halves.
9. `_RNT_SEALED_HEAD` and `_RNT_MERGE` are assigned **twice** at module level at the base — the pin,
   and the clause-9 self-test rebinding to `('f' * 40, 'e' * 40)`. A deletion that removes one and
   leaves the other must **fail**, in both directions.
10. A manifest record added without authorization — **fails** as an unauthorized addition, with
    `SI2-7`'s single authorized addition the only exception.

## What no outcome of this round licenses

1. Any change to a historical `B`, `E`, `L` or `P`, or to any preregistration or result note,
   `SI-1`'s included.
2. Any claim that the generic validator is *correct*, as distinct from *in agreement* and *now
   authoritative*. Authority is a decision; correctness is not conferred by it.
3. Any adjudication of census divergences 7, 13 or 20, which remain open.
4. Any re-opening of the adjudicated derivation rule.
5. Any statement about Act 21's targets, or that Act 21 may open.
6. Any claim that a `MAP-CHANGED` verdict is acceptable because the new mechanism is better.
7. Any retrofit. Every historical `B`, `E`, `L`, `P` stays exactly where it is.

## Hazards

**H1 — the deletion is irreversible and the evidence is in the tree.** Mitigated by the gating order:
`SI2-3` is measured before stage 3, so the agreement is recorded in this round's own census before
the constants that justified it are removed.

**H2 — the double assignment.** `RNT` carries two assignments of its sealed head and merge. A
deletion pass that reads the *last* assignment, or removes only one of the two, leaves a guard file
that looks clean and is not. Negative case 9 exists for this and the inventory below fixes the count.

**H3 — self-certification.** `SI-2` takes authority and then lands. If `SI-2` sealed itself, the
mechanism it installed would certify its own installation. `SI-2` is non-sealing, so the landing is
certified the way `SI-1`'s was: by the ancestry check, the exact-head CI and the `main` push run.

**H4 — a moved verdict read as an improvement.** After the cutover a pre-existing tag may change
verdict because the new rule genuinely answers differently. That is a finding about the record and
requires adjudication; `SI2-6` reports it and the round stops rather than adopting it.

**H5 — the count that drifts.** Sixty-one seal constants exist at `B0`; fifty-eight are deletable and
three are not (`_SI1_BASE`, and `SI-2`'s own `_SI2_BASE` once it exists — and `_RNT`'s self-test
rebinding, which is a probe value and not seal data, is counted explicitly in the inventory rather
than left to a reader). A deletion measured against a remembered number rather than the inventory is
how a round removes fifty-seven and reports fifty-eight.

**H6 — the census that is not re-measured.** `SI-1`'s census is evidence about `SI-1`'s head. It is
not evidence about `SI-2`'s head, where the derivation rule is different by construction. `SI2-3`
re-measures; quoting `SI-1`'s numbers would be quoting the wrong experiment.

**H7 — inheriting more than was certified.** `SI1-7` is a specification of type P, and the owner's
adjudication is narrow. Neither licenses redesigning the model beyond the union rule and the cutover.

## The seal-constant inventory at `B0`, FROZEN

Sixty-one module-level assignments across twenty-three stems, measured at `B0`:

| stems | shape | count |
|---|---|---|
| `A12P` `A6D` `A6I` `A6P` `CTI` `HYA` `HYB` `HYE` `PC4` `PC4S` `PQT` `RNC` `SGT` `TCF` `TRJ` `WTS` `XTS` | `BASE` + `SEALED_HEAD` + `MERGE` | 17 × 3 = 51 |
| `RNT` | `BASE` + `SEALED_HEAD` ×2 + `MERGE` ×2 | 5 |
| `ABR` `CLG` `RBR` `TSG` | `BASE` only | 4 |
| `SI1` | `BASE` only | 1 |
| **total** | | **61** |

Of these, **58 are deletable** — the 18 sealed rounds' triples including `RNT`'s duplicate pair, and
the 4 base-only rounds' bases — and `_SI1_BASE` is retained until `SI-1` has a manifest record, which
`SI2-7` adds, after which it too is deletable within this round. The execution reports the final
count against this table and not against prose.

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
3. `verification/seals/` holds exactly 22 records, 18 `sealed` and 4 `base-only`.
4. `R7-SI1` passes at the base and its census reconstructs identically.
5. The guard file carries exactly 61 module-level seal-constant assignments, per the inventory.
6. `main` is exactly `66eea646fcbf242df89b168bcce3336ff1b77802` and that commit's second parent is
   `d75427aece402e1629d56d1ca96fbc8d3c8101e8`.
7. No `SI-2` record exists in the manifest.

## The guard

Fresh tag **`R7-SI2`**, stem **`_SI2_`**. It carries `_SI2_BASE`, act 10's strengthened ancestry
check asked of the real `pull_request.head.sha` and never of the synthetic merge, fail-closed, this
preregistration pinned **by blob** with a one-byte drift control, and **no seal triple of its own**.

Content contracts hold the result note to the distinctions this freeze makes: the ordered cutover
and its gating, the three unadjudicated divergences kept open, `SI-1`'s `#141` result not rewritten,
the authorized addition being exactly one, and no claim that authority confers correctness. Each
contract is mutation-tested against the exact failure it exists to catch.

**Four definition slots** are budgeted for the round's own new definitions, as `SI-1` had; unused
slots are recorded as unused.

## Chronology

The execution branches from the mandated base and from no other commit, and certifies that ancestry
in act 10's strengthened form: the base an ancestor of the head, and every commit of
`rev-list HEAD ^base` a descendant of the base, recovery included, fail-closed, asked of the real
pull-request head.

Act 21 remains closed throughout `SI-2` and is not opened by any outcome here.
