# Independent review of DESIGN-v5.5.4 (DI-1 option B, DI-2 option A narrow)

Reviewer: independent; not the writer of v5.5.4. Read-only; paper review; no code run, no git or
GitHub activity. Criteria: the brief, sharpened by the owner's acceptance criteria relayed by the
coordinator (ACCEPT only if all hold; otherwise REVISE with the smallest text correction).

## Verdict: REVISE

Two BLOCKING findings, both with concrete counterexamples and both fixable by small text additions
(sec. 4). Everything else in the amendment is in scope, closes the demonstrated cases and is
consistent with unchanged v5.5.3 text.

## 0. Inputs verified

| File | sha256 | Expected | |
|---|---|---|---|
| DESIGN-v5.5.3.md | 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379 | same | OK |
| DESIGN-v5.5.4.md | 1ade8b8f43d6259c50ac9847c59e09ce71a645ba0cb8eabe7e1deb84bb4c5e34 | same | OK |
| CHANGES-v5.5.4.md | 76d4a41312bd2f4df18f0c50251a4e4a89aa465c06e9bbce043815671953434c | 76d4a413…434c | OK |
| CHANGES-v5.5.4.diff | 8b139ca8a5555ec1da70d2142a8ba455a68f2ab9cda1b5846a6dcde7a9a05962 | 8b139ca8…5962 | OK |

A fresh `diff -u DESIGN-v5.5.3.md DESIGN-v5.5.4.md` is identical to `CHANGES-v5.5.4.diff` apart
from the two header lines (timestamps). 14 hunks; 3027 -> 3123 lines.

Note: the brief speaks of "nine judgement calls" numbered (1), (2), (4), (9); CHANGES-v5.5.4.md
lists eleven. Mapping used here: brief (1) = CHANGES 7 (`record_id`); brief (2) = CHANGES 1
(TR59); brief (4) = CHANGES 3 ("completed"); brief (9) = CHANGES 11 (authorization records).

## 1. Scope and ids (check 1): CONFIRMED

- Each of the 14 hunks is DI-1, DI-2 or a direct consequence (title, status bullet, snapshot field,
  merge-time trust attestation, S13 acceptance list). No unrelated rewording or reflow. Hunk 9
  leaves a short line ("by the forms") rather than reflowing the next unchanged line; acceptable.
- Every hunk is listed in CHANGES with its header and old/new lines. For hunks 8, 9 and 11 the
  "old"/"new" text is the changed lines only, not a contiguous passage (hunk 9's "old text" joins
  two non-adjacent lines of points 4 and 5). The `.diff` is exact; see N2.
- TR54-TR64 and LN1-LN8 occur in no DESIGN*.md or CHANGES*.md other than v5.5.4 (grep, each id,
  word-bounded). No id reused.

## 2. Rules and demonstrated cases (check 2)

| Owner rule | v5.5.4 text | Control | Holds |
|---|---|---|---|
| no authority from becoming/regaining owner | "Owner at creation" lead sentence; owner comment defined by version in force at creation | TR56, TR58, TR59 | yes for comment forms; **not for authorization records (B1)** |
| withdrawals valid if owner when posted; survive owner change | Withdrawals bullet; point 5 | TR55, TR61 | yes |
| designations: owner when posted and current owner when evaluated | Designations bullet (+ no owner change since creation) | TR54, TR56, TR59, TR61 | yes |
| approvals: no owner change between approval and merge; away-and-back does not restore | Approvals bullet; authority changes; N3 | TR57, TR58, TR64 | yes for `oi-authority`/`oi-freeze-ledger` comments; **not for authorization records (B1)** |
| completed actions stay valid | Completed actions bullet (evaluated at merge against the `A` in force at merge) | TR60 | yes for authority/ledger changes; **broken for superseded records by the DI-2 predecessor lint (B2)** |
| DI-2 same `record_id`, immutable | lineage bullet | LN1, LN8 | yes |
| no valid id cannot supersede / be superseded | lineage bullet 1 | LN3 | yes |
| actual, independently verified predecessor | lineage bullet 3 | LN4 | yes, but see B2 |
| cycles, unrelated chains, ambiguous ancestry | lineage bullets 2, 4, 5 | LN5-LN8 | yes |
| consistent across record types incl. `A` | `A.supersedes` | TR63 | yes |

Demonstrated cases: D1 (TR54), D2 (TR55), D3 (TR56), L5 (TR57), L6 (TR58), E6 (LN1) are closed by
the text as written; each traced against the new paragraphs and admission points 3-5.

**K1.** Still holds. The Designations bullet states that a supersession recorded in the ledger or a
committed snapshot only revokes; reconciliation ("a ledger entry alone never designates") is
unchanged; point 5 processes only halves that count. A forged bound `supersede` cannot designate
F2. Point 5's generic list ("a supersession ... designates F2") still reads literally for bound
events; the three overriding statements make it unambiguous (N3).

**"Completed actions remain valid" loophole check.** A completed authority/ledger change is judged
at its merge against the version of `A` in force at that merge, never against today's owner; a
designation is explicitly not completed for a later admission; an acceptance landing's appended
events bind only as reconciliation allows (never designate). No path found by which a completed
action authorizes a new admission. Criterion "validity established at the time it completed, never
retroactively by today's owner" holds for authority and ledger changes; it fails for record
predecessors (B2).

### Enumeration of every path by which an owner comment or owner identity confers authority

| # | Path | Checked by v5.5.4 against owner-at-creation + current + no intervening change? |
|---|---|---|
| 1 | `oi-freeze/1 designate` | yes (Designations) |
| 2 | `oi-freeze/1 supersede`, designating half | yes |
| 3 | `oi-freeze/1 withdraw`, revoking half of supersede | owner at creation; survives change (decision) |
| 4 | bound ledger / snapshot events | revoke only; counted by recorded author/time (point 5) |
| 5 | `oi-authority/1 approve` for `A` changes | yes (Approvals; governing = replaced version) |
| 6 | `oi-authority/1 approve` for ledger changes | yes (governing = in force at merge) |
| 7 | `oi-freeze-ledger/1 append` (N3) | yes |
| 8 | first `A`; new id of an owner-id change | authenticated as pinned id; before merge; no owner change between (TR62) |
| 9 | `oi-owner-authorization/1` records (records, reviews, widening reviews, the configuration) | **no: compared only to current `A.owner.id` / configuration owner (lint; point 7). B1, B2** |
| 10 | configuration `retirement.owner` | data field compared to current `A.owner.id`; carries no comment authority; covered once 9 is fixed |
| 11 | PR merged-by id | provenance only (unchanged) |
| 12 | edit / hide / delete of owner comments (point 3) | refuse-only; now also former owners' comments (N1) |

## 3. Internal consistency (check 3)

No contradiction found with unchanged text: TR32-TR36 and TR47 (now read through "Owner at
creation"); N3 (authored-by replaced, still "verified exactly like a designation"); authority-change
procedure ("Its author numeric id is the previous `A`'s `owner.id`" agrees with governing = replaced
version); "Every change to `A` on main ... must satisfy this procedure" (evaluated per change at its
merge); admission points 1-7; reconciliation; the forms; residual trust (merge time added). The
only inconsistency is between the new DI-2 predecessor rule and the unchanged lint bullet "an
authorization whose `owner` differs from the configuration's owner" (B2).

## 4. Findings

### B1 (BLOCKING): owner authorization records still accept a comment written before its author became owner (D3 analogue)

Rule violated: DI-1 option B ("A comment must not acquire authority merely because its author becomes
the owner later"; approvals require owner when posted), as sharpened by the owner ("ALL
authorization paths").

Text: sec. 6.3 lint "an authorization whose `owner` differs from the configuration's owner" and
admission point 7 "and so must the owner of the configuration's authorization record" compare the
`oi-owner-authorization/1` record's `owner` only with the current `A.owner.id`. Nothing evaluates
the quoted comment's `time` against the owner history. CHANGES judgement call 11 leaves this
deliberately.

Counterexample. 4242 is owner. 5555 posts a comment authorizing configuration C (and records R).
An authorization record quotes it: `owner` 5555, `time` t0 (4242 in force), `comment_id`.
4242 -> 5555 merges. 5555 designates `F`, whose pin table lists C, its review and that
authorization. Lint: `owner` 5555 = configuration owner 5555, pass. Point 7: 5555 = `A.owner.id`,
pass. The authorization requirement for C and R is met by a comment posted before 5555 was owner,
only because 5555 became owner later. Away-and-back variant: 4242 authorizes R, 4242 -> 5555 ->
4242, the old authorization counts again (L5 analogue). The subsequent designation does not cure
this: the design requires an owner authorization in addition to the designation, and that
requirement is satisfied by a pre-ownership comment. For a record added after `F` (sec. 13.3), the
authorization is the only owner act binding its content.

Correction (smallest): see sec. 5, C1 and C3.

### B2 (BLOCKING): the DI-2 predecessor rule invalidates a predecessor's completed authorization after an owner change

Rule violated: DI-1 "Historical decisions: previously completed, valid actions remain valid;
ownership changes do not retroactively invalidate them"; owner criterion "validity of a completed
action is established at the time it completed".

Text: new lineage bullet "a `supersedes` naming a predecessor that does not itself pass this lint
... (its own review and authorization)". "This lint" includes the unchanged bullet "an
authorization whose `owner` differs from the configuration's owner".

Counterexample. R1 (lineage L) is reviewed and authorized by 4242 while 4242 is owner. 4242 -> 5555
merges, approved by both. 5555's writer prepares correction R2 (`supersedes` R1, same kind, schema,
`record_id`), reviewed, authorized by 5555. The configuration (owner 5555) references R2. Lint of
R2 -> predecessor R1 -> R1's authorization `owner` 4242 differs from the configuration owner 5555 ->
R1 fails -> R2 FAIL `record-invalid`. A valid authorization given by the owner of the time is
retroactively treated as invalid; no correction of any pre-change record is possible unless the new
owner re-authorizes the superseded record. v5.5.3 did not require the predecessor to pass the lint,
so this is introduced by v5.5.4.

Correction (smallest): see sec. 5, C1 and C2.

### Coverage gap tied to B1/B2 and an owner criterion (NON-BLOCKING on its own; include with the revision)

- No control for B1 or B2 (C4: TR65, LN9).
- No positive control that an existing record with `supersedes: null` and no `record_id`, named by
  no `supersedes`, remains usable. The text allows it (the id is required only in a chain), but the
  owner's criterion names it (C4: LN10).

### NON-BLOCKING

- **N1.** Point 3 now edit-checks every owner comment at creation, including a former owner's. A
  former owner can therefore make every later admission of the plan refuse by editing one old
  comment into an `oi-freeze/` line. Fail-closed, consistent with withdrawals binding, and the
  moderators' hide power already gives a similar veto. No control covers the extended point-3 set;
  recommend one (a former owner's old comment edited after the change: ERROR).
- **N2.** CHANGES hunks 8, 9, 11 give only changed lines as "old/new text"; hunk 9's "old text" joins
  two non-adjacent lines. The `.diff` is exact and authoritative; consider quoting the full hunk.
- **N3.** Point 5's generic list still says a supersession "designates `F2`" for bound events; the
  Designations bullet, reconciliation and the "does not count ... is not processed" sentence
  override it. A cross-reference in point 5 would remove any implementer doubt. Not a bypass.
- **N4.** Fork detection over the audit and plan record directories at `F` makes a stray or rejected
  draft superseding the same predecessor block the lineage until removed before `F`. Fail-closed;
  within "ambiguous ancestry rejected".
- **N5.** The authorization record's `time` is writer-asserted and reviewer-checked (existing
  "Residual limit"). C1 relies on it. A stronger, larger option is for the tool to read the quoted
  comment by `comment_id` from the host and take author id and creation time from there; not
  required by the decision.

## 5. Corrections (exact text)

**C1** — in sec. 6.3, "Owner at creation", insert after the "Approvals" bullet:

```text
- **Owner authorizations.** An `oi-owner-authorization/1` record counts for a record the run uses
  only if the version of `A` in force at its `time` has `owner.id` equal to its `owner`, its `owner`
  equals the `owner.id` of the authority record governing the admission, and no owner change merged
  between its `time` and the admission. The authorization of a predecessor named by a `supersedes`
  is a completed action: it counts if the version of `A` in force at its `time` has `owner.id` equal
  to its `owner`.
```

**C2** — in the DI-2 lineage bullet, replace

`and verified independently of the superseding record (its own review and authorization);`

by

`and verified independently of the superseding record (its own review and authorization, the
authorization checked as "Owner at creation" states for a predecessor, in place of the comparison
with the configuration's owner);`

**C3** — in admission point 7, after "and so must the owner of the configuration's authorization
record." append: `Every authorization record the run uses must also count under "Owner at
creation" above; otherwise FAIL `record-invalid`, or ERROR `CONFIG_UNREVIEWED` for the
configuration's own.`

**C4** — controls (new ids, unused anywhere):

```text
| TR65 | (authorization analogue of D3 and L5) an authorization record whose `time` falls while 4242 is owner and whose `owner` is 5555; 4242 -> 5555; 5555 designates `F`, whose configuration uses it. Separately, 4242's authorization with `time` before 4242 -> 5555 -> 4242. Separately (positive), 5555's authorization with `time` after 4242 -> 5555 | the first two: ERROR `CONFIG_UNREVIEWED` for the configuration's authorization, FAIL `record-invalid` for any other record's; the third: admitted | DI-1 |
| LN9 | a predecessor R1 authorized by 4242 while owner; 4242 -> 5555; R2 superseding R1, reviewed and authorized by 5555, used by the run. Separately, R1's authorization `time` before 4242 was owner | the first: no `record-invalid`, the run uses R2; the second: FAIL `record-invalid` | DI-1, DI-2 |
| LN10 | (positive) a record with `supersedes: null` and no `record_id`, named by no `supersedes` | no `record-invalid` | DI-2 |
```

and the consequential updates: status bullet "controls TR54-TR62 and TR64" -> "controls TR54-TR62,
TR64 and TR65"; "controls LN1-LN8 and TR63" -> "controls LN1-LN10 and TR63"; S13 "LN1-LN8" ->
"LN1-LN10", "TR1-TR64" -> "TR1-TR65"; CHANGES list updated.

## 6. Judgement calls (CHANGES numbering)

1. TR59 (brief 2): required by "or regains ownership"; the owner confirmed it. Agree.
2. Owner change vs any `A` change: agree; TR64 is the right positive.
3. "Completed" (brief 4): agree for authority and ledger changes, judged at merge against the `A`
   in force then, never today's owner. No pre-adoption history exists. B2 is the one place where the
   amendment's DI-2 text reintroduces a today's-owner check; C1/C2 fix it.
4. Point 3 both sets: agree (refuses no less than v5.5.3); see N1.
5. First `A` / new id: agree; TR62 adequate.
6. Snapshot field and merge-time trust: necessary consequences. Agree.
7. `record_id` (brief 1): minimal and within DI-2 (the decision itself names `record_id`; the
   implementation's records already carry it; no per-kind schema edited; required only of records
   in a chain; existing `supersedes: null` records without it remain usable). Agree; add LN10.
8. `A` lineage by fixed path + first-parent predecessor (TR63): within "applies consistently";
   agree.
9. Fork detection domain: reasonable; N4.
10. Cycle control in a synthetic store: agree.
11. Authorization records out of scope (brief 9): disagree. Owner authorizations are approvals of
    exact content and are within "Designations and approvals"; B1 shows a concrete D3/L5 analogue.
