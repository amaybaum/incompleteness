# Independent review of DESIGN-v5.5.7 (v5.5.6 + C8, C9)

Reviewer: independent; wrote neither the draft nor any earlier review. Read-only paper review, no
git or GitHub activity. Stopping rule: block only on a demonstrated or concrete counterexample.

## Verdict: REVISE

Scope, placement, quotes and id hygiene are exact, and every control row in TR54-TR69 and
LN1-LN11 states an outcome consistent with the design text. Two amended rules still have no
rejection control; for each, a concrete wrong implementation passes TR1-TR69 and LN1-LN11 while
violating the rule (B-3, B-4). Both corrections are control rows only; no design rule text changes.

## 0. Inputs verified (sha256)

| File | sha256 | |
|---|---|---|
| DESIGN-v5.5.3.md (frozen) | 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379 | OK |
| DESIGN-v5.5.6.md | e19e9406044b4be321074ff935f5978b5ebeb258a637a76545023d3cbeafca77 | OK |
| DESIGN-v5.5.7.md | 0a7efa040af44c4bf1e09b3ba026eb6e2a1a0fecc413516a0c2fcbc629504f6f | OK |
| review-v5.5.6/review.md | 07d5e956b372c641850733ecccdaca69b3d4ae0a7f70e63f85146f0616799fc3 | OK |
| CHANGES-v5.5.7.md | 41df071e1df2922cfbb950c72f380b9e861f8de5c54864480cd1a5e8d08b6dfa | OK (manifest) |
| CHANGES-v5.5.7.diff | 5030aaea3646ae99398f8d738e6d5df19863d9a349cba456eb29cc91c168327f | OK (manifest) |
| CHANGES-v5.5.7-from-v5.5.6.diff | bbd7daabab179ae66d9d49056ad83216a35be97c7373eefe91c363d77ff379e6 | OK (manifest) |

`sha256sum -c v5.5.7-MANIFEST.sha256`: all 4 OK. `diff -u` regenerated for v5.5.6 -> v5.5.7 and
v5.5.3 -> v5.5.7 is identical to the two committed diffs (4 and 14 hunks).

## 1. Scope (check 1): MET

`diff DESIGN-v5.5.6.md DESIGN-v5.5.7.md` changes only: title (line 1); status bullet (version
label, "supersedes the v5.5.6 draft", range TR64-TR69, CHANGES file name); rows TR54, TR60, TR61;
new rows TR68, TR69 directly after TR67; S13 "TR1-TR69". No rule text changed. C8 replacement texts
for TR54 and TR61 and the optional N7 text for TR60 are string-equal to review-v5.5.6 sec. 6; TR68
and TR69 are byte-equal to the review's rows (checked by grep and string comparison).

## 2. Row-by-row consistency (check 2): MET

Traced through "Owner at creation" (definitions, withdrawals, designations, approvals, owner
authorizations, first `A`/new id, completed actions), the authority-change procedure, admission
points 3-7 and the lineage clause.

- Control-harness outcomes are now labelled where a full chain differs: TR54 and TR61 (point 5
  harness; full chain ERROR `CONFIG_UNREVIEWED` at point 7, since the commit was named before the
  owner change and its configuration authorization cannot have the new owner in force at its
  `time`), TR66 (harness). Correct.
- Rows whose ERROR arises at point 5 (TR55, TR56, TR59, TR61 first, TR69) are the same in harness
  and full chain. TR57/TR58 are merge-time outcomes; TR62, TR64, TR68 authority-chain outcomes;
  TR63, TR65 full chain; TR67 scoped to points 3-4. TR60 "an `F` frozen after the change; `F`
  admitted" is a full-chain outcome and holds when its configuration authorization is by 5555
  after the change (see N-2).
- TR68: case 1 not an owner comment (V1 in force); case 2 owner comment but owner changes V1->V2,
  V2->V3 merged between creation and merge; case 3 new-id approval with V1->V2 merged between
  creation and merge. ERROR in each, and "every later admission refuses" follows from "every change
  to `A` on `main` ... must satisfy this procedure".
- TR69: 5555's designation is not an owner comment at creation, so by the C5 parenthetical `F` was
  never designated; the withdrawal (an owner comment) names it: refusal. Correct.
- LN1-LN11 are lint outcomes (FAIL `record-invalid` or none), consistent with the lineage clause;
  LN9 second case fails "in force at its `time`"; LN11 passes as completed actions.

## 3. Coverage (check 3): NOT MET (B-3, B-4)

| Amended rule | Rejection | Acceptance |
|---|---|---|
| designations (former / future / away-and-back) | TR54, TR56, TR59 | TR54 2nd (harness), TR60, TR65 3rd |
| withdrawals | TR66 1st | TR55, TR66 2nd |
| supersession, designating half | TR61 1st | TR12 |
| supersession, revoking half | **none (B-3)** | TR61 ("`F` withdrawn") |
| `oi-authority` approvals, `A` change | TR68 cases 1-2 | TR60, TR62 1st |
| approvals, ledger change; append comments | TR57, TR58 | TR60, TR64 |
| new-id approvals | TR62 2nd, TR68 case 3 | TR62 1st |
| owner authorization records | TR65 1st, 2nd | TR65 3rd |
| predecessor authorizations, own | LN9 2nd, LN4 | LN9 1st |
| predecessor authorizations, widening review | **none (B-4)** | LN11 |
| C5 test | TR69 | TR55, TR61 |
| point 3 extension | TR67 1st | TR67 2nd |
| lineage: record_id / missing id / immutability | LN1, LN3, LN8 | LN2 |
| verified predecessor | LN4, LN9 2nd | LN2, LN9 1st |
| cycle / fork / two heads / unrelated chain | LN5 / LN6 / LN7 / LN8 | LN2 |
| no-record_id record usable | - | LN10 |
| `A` lineage (fixed path) | TR63 | TR60, TR62 |

### B-3 (BLOCKING): no control for the revoking half of a supersession that is not an owner comment

Rule. "Withdrawals and revocations. A withdrawal, and the revoking half of a supersession (the
withdrawal of `F`), counts if it is an owner comment." Point 5: "A form, or half of a supersession,
that does not count under 'Owner at creation' is not processed."

Wrong implementation W1. Applies "Owner at creation" to `withdraw` forms and to designating halves,
but processes the revoking half of every parsed `supersede` form. Point 3/4 parse every comment
whose author is the current `A.owner.id`, including that id's comments from before it was owner, so
W1 processes a future owner's pre-ownership supersession. W1 passes every control: TR66 uses a
`withdraw` form, TR12/TR61 use supersessions that are owner comments, TR32 a ledger supersession,
and no other row has a supersession by a non-owner.

Counterexample. 4242 designates `F`; 5555 posts `oi-freeze/1 supersede ... commit=<F> by=<F2>` while
4242 is the owner; 4242 -> 5555; 5555 designates `F`. Text (harness): neither half of the
supersession counts, 5555's designation counts, `F` is the one designated commit at point 5. W1:
ERROR (designation of a withdrawn commit). W1 gives a pre-ownership comment revoking authority,
which DI-1 option B denies ("a comment never acquires authority merely because its author becomes
the owner later").

Smallest correction (new id, after TR69):

```text
| TR70 | 4242 designates `F`; 5555 posts `oi-freeze/1 supersede` of `F` by `F2` while 4242 is the owner; 4242 -> 5555; 5555 designates `F` (control harness) | `F` is the one designated commit at point 5 (the supersession is not an owner comment; neither half is processed) | DI-1, point 5 |
```

### B-4 (BLOCKING): no rejection control for a predecessor's widening-review authorization

Rule. Lineage clause: a predecessor is "verified independently of the superseding record (its own
review and authorization, each authorization its lint requires, a widening review's included,
checked as 'Owner at creation' states for a predecessor ...)"; "Owner authorizations": each such
authorization "counts if the version of `A` in force at its `time` has `owner.id` equal to its
`owner`". Sec. 6.3 widening: a widening without a widening review listed by an owner authorization
is FAIL `record-invalid`.

Wrong implementation W2. For a predecessor, W2 checks its review and its own authorization at
`time`, and checks that a widening review exists with all verdicts `accept`, but does not check the
widening review's authorization (or checks only that one exists, with any `owner`/`time`). For a
record the run uses, W2 applies the full check. W2 passes every control: LN11 is positive only; LN4
and LN9 test the predecessor's own review/authorization; A12r tests the widening review of the
record in use, not of a predecessor.

Counterexample. R0 -> R1 (an allow rule widening R0) whose widening review is listed only by an
authorization with `owner` 5555 and `time` while 4242 is the owner (or by no authorization);
4242 -> 5555; R2 superseding R1, reviewed and authorized by 5555, used by the run. Text: R1 fails
its lint, so R2 is FAIL `record-invalid`. W2: no `record-invalid`, and the run uses a lineage whose
widening was never authorized by an owner in force at the time.

Smallest correction (new id, after LN11):

```text
| LN12 | as LN11 for an allow rule, each case separately: R1's widening review listed only by an authorization record with `owner` 5555 whose `time` falls while 4242 is the owner; R1's widening review listed by no authorization record | FAIL `record-invalid` for the superseding record R2 in each case | DI-1, DI-2 |
```

Consequential for B-3/B-4: status bullet "TR54-TR62 and TR64-TR69" -> "TR54-TR62, TR64-TR70" and
"LN1-LN11" -> "LN1-LN12"; S13 "LN1-LN11" -> "LN1-LN12" and "TR1-TR69" -> "TR1-TR70"; CHANGES
updated. TR70 and LN12 occur in no DESIGN*.md or CHANGES*.md (word-bounded grep).

## 4. Ids and quotes (check 4): MET

`grep -lw` over every DESIGN*.md and CHANGES*.md: TR68 and TR69 occur only in DESIGN-v5.5.7.md and
CHANGES-v5.5.7.md, once each as a row id; no duplicate row id in v5.5.7's control tables.
CHANGES-v5.5.7.md: all 28 old/new blocks (14 hunks) occur verbatim as contiguous lines of
DESIGN-v5.5.3.md / DESIGN-v5.5.7.md (script check); the hunk tables match the committed diffs.

## 5. Non-blocking

- **N-1.** TR69 (like TR61's "`F` withdrawn") is discriminated from a wrong C5 test only by the
  stated refusal reason: an implementation treating every designation as "has designated" still
  refuses `F` (not designated). Sec. 10.4 requires predicates to test the whole stated expectation,
  so the reason is tested, but adding "then 5555 designates `F'`; admission of `F'`: ERROR" would
  make the row discriminate by outcome.
- **N-2.** TR60 "an `F` frozen after the change" would be exact as "whose configuration
  authorization 5555 made after the change".
- **N-3.** TR68 implicitly assumes every other approval and review in each case is valid; saying so
  isolates the defect each case tests.
- review-v5.5.6 N8-N12 and review-v5.5.5 N2-N6 still apply as stated there.
