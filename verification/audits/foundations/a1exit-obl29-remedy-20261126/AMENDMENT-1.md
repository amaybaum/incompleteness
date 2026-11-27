# OBL-29 remedy r9, amendment 1: provisional blocks and genuine findings (paper draft a1)

## 0. Status, authority and goal link

**Status.** Clarifying amendment to the adopted OBL-29 remedy r9 (`DESIGN.md` in this directory at
`77a73c022091f598cf807fcf89d66c3cf43208de`, adopted at #1601 comment 7197486426). Paper draft,
pending independent review and the owner's adoption. It changes no predicate of r9 that decides a
genuine finding; it states how r9 and the r13 Form (i) clause treat a second-kind review whose
reviewer's independence cannot yet be established.

**Authority.** Owner decision (amaybaum, received 2026-11-27, coordinating session; recorded at
#1169 comment 7207734407, 2026-11-27T01:59:03Z), item 4, quoted:

> Confirm the self-review reading. Authorize drafting the r9 clarifying amendment distinguishing provisional blocks from genuine historical findings. Obtain independent review and return for adoption.

Item 5 of the same decision, which bears on the outcome of a provisional block, quoted:

> Malformed findings shall produce run-level `FAIL retirement-blocked`, preserving evidence and provenance. Reserve `ERROR` for cases where reliable evaluation is impossible.

**Goal link (AGENTS.md §A.47).** Serves A1 retirement (#1169) through OBL-29 (#1598): it would decide
whether r9's monotonicity property (I) is consistent with the self-review reading the owner
confirmed. It authorizes no implementation, freeze, trial, dispatch or merge.

***

## 1. The two kinds of block

r13 R6.RECON.26, Form (i) (Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e`, as amended
by r9 R6.OBL29.3 to read "the scan" as `R*`), says of a second-kind review: "Only such an
independence failure disqualifies it; a review whose `reviewed` names no record the scan finds, so
that its independence cannot be established, counts, as a form failure."

That clause covers two different states, which r9 §1.2 does not separate:

- **Genuine finding.** A review carrying `invalidates` or `invalidated` whose `reviewed` names an exact
  `{path, blob_sha256}` present in `R*`, and whose `reviewer` differs, as an identity string
  (R6.RECON.29), from that record's `author` and is not a run, check or Issue. Its independence is
  established. Its form failures, if any, still bind (Form (i)).
- **Provisional block.** A review carrying `invalidates` or `invalidated` whose `reviewed` names an
  exact reference absent from `R*`. Its independence cannot be established. It binds as a form
  failure, so a run fails closed, but it is not yet a finding.

Because the reference is exact, the named record's bytes, and so its `author`, are fixed. When the
record enters `R*` (it is in some tree reachable from the run's roots), the provisional block resolves
once, and the resolution is permanent, because `R*` is monotone under ancestry extension (r9 §2.3):

- if the record's `author` equals the review's `reviewer`, the review is disqualified by the
  independence failure of Form (i). No finding existed. The provisional block is **resolved**, not
  discharged;
- otherwise the review is a genuine finding from then on.

A provisional block whose record never enters `R*` keeps blocking.

***

## 2. Amended statements

**A1.1 Obligation monotonicity (r9 §1.2).** `Obl(t)` is the set of genuine findings established up to
time `t`. Requirement (I), `Obl(t) ⊆ Obl(t')` for `t' >= t` with every member binding until a
discharge lifts it, applies to genuine findings. A provisional block is not a member of `Obl(t)`. It
binds while its named record is absent from `R*`, and leaves the blocking set only by a discharge or
by resolution to a disqualified review. Resolution to a genuine finding adds it to `Obl` permanently.

**A1.2 Resolution is not removal (r9 R6.OBL29.6, §2.3).** Resolving a provisional block by later
evidence that establishes a same-author review is a determination from the evidence, as r9 §2.3
already states for a lack of independence, not a removal and not a discharge. It applies only where
the named record, by exact reference, is in `R*` and shows `author` equal to `reviewer`. It never
applies to a genuine finding: no later record, review or rewrite can disqualify a review whose
independence `R*` has established, since the named record's bytes are fixed and stay in `R*`.
Deleting, moving or rewriting the named record after it entered `R*` changes nothing (R6.OBL29.6).

**A1.3 Outcome of a provisional block.** While it binds without an applying discharge, the run reports
FAIL `record-invalid` for the form failure and `retirement-blocked` for the block, as Form (i) and
owner decision item 5 require. It is not ERROR: evaluation is reliable, and the absence of the record
is the evaluated fact. A discharge of it uses the existing route, including `repair: null` where
R6.RECON.27 Keys (b) admits it, read over `R*`.

**A1.4 Effect on r13 Form (i).** On adoption, R6.RECON.26 Form (i)'s last clause reads: "a review whose
`reviewed` names no record in `R*`, so that its independence cannot be established, counts, as a
form failure, while that record is absent from `R*` (a provisional block); once the record is in
`R*`, the review is disqualified if its `reviewer` equals that record's `author`, and is otherwise a
finding." Keys (b) and the other Forms keep their text.

***

## 3. Controls

| Id | Setup | Expected |
|---|---|---|
| SELF-REVIEW-RECORD-LANDS-LATER (existing; expectation changed) | The invalidating review lands first with its named record absent; then the record lands with `author` equal to the review's `reviewer` | before the record lands: FAIL `record-invalid` and `retirement-blocked` (A1.3), replacing the tool's current ERROR `DESIGN_UNSETTLED` stop; after: no second-kind finding and no block from that review (A1.2) |
| INDEPENDENT-RECORD-LANDS-LATER (new) | As above, but the record's `author` differs from the reviewer | before: as above; after: a genuine finding that binds |
| INDEPENDENT-RECORD-THEN-DELETED (new) | Continue the previous case: the record and the review are deleted from later trees | the genuine finding still binds (A1.1, R6.OBL29.6) |
| PROVISIONAL-RECORD-NEVER-LANDS (new) | The named record never enters `R*` | FAIL `record-invalid` and `retirement-blocked` at every later `M` |
| SELF-REVIEW-COPY-ELSEWHERE (new, countercase) | The genuine finding of INDEPENDENT-RECORD-LANDS-LATER, then a byte-different record at the same path naming the reviewer as `author` lands | the genuine finding still binds: the exact reference names the first record, whose author is fixed (A1.2) |

Each new row is a specification with runner null until implemented. The tool control at
`tools/ledger_coverage/adapters/obl29_controls.py` (PR #1577 at `7db52f380f1e51d4af52b84f0a7e728827ac5a60`)
pins the "after" half of SELF-REVIEW-RECORD-LANDS-LATER already and expects `DESIGN_UNSETTLED`
before; on adoption its "before" half changes to A1.3.

***

## 4. What this amendment does not do

It does not change which reviews are genuine findings, the independence rule, Keys, the reliance and
clearance predicates of r9 §2.2, the custody design, or any discharge route. It authorizes no
implementation.

## 5. References (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7207734407, items 4 and 5 | authority and outcome rule, quoted in §0 | provenance |
| r9 `DESIGN.md` at `77a73c022091f598cf807fcf89d66c3cf43208de` | the text amended | support off `main` until #1601 lands |
| Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e`, R6.RECON.26 Form (i) | the clause clarified | support on `main` (landed by #1604) |
| PR #1577 at `7db52f380f1e51d4af52b84f0a7e728827ac5a60` | the existing control | provenance |
