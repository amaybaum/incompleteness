# OBL-29 remedy r9, amendment 1: provisional blocks and genuine findings (paper draft a3)

## 0. Status, authority and goal link

**Status.** Draft a3. a2 answered the independent review of a1 at
`23454e92fa254c9b80a21b65424edd02e670b505`, and a3 the re-review of a2 at
`8567b84147891e49b49d3e8beb8e0f97132ea291` (both posted on PR #1601). Clarifying amendment to the adopted OBL-29 remedy r9 (`DESIGN.md` in this directory at
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

Write `R*_M` for the `M`-derived part of `R*`: the entries of trees reachable from effective `M`,
which r9 §2.3 shows is monotone under ancestry extension; a record there has a durable witness in
`M`'s ancestry. For a predicted `M` (R6.TREE.15, R6.RECON.21), only `M0`'s ancestry is durable, so a
record seen only on the in-memory chain from `M0` gains a durable witness, and the permanence below
takes effect, when that chain lands on `main`. Entries seen only through `F`, `REV` or an explicit
input have the narrower guarantee of r9 R-1. The clause covers two different states, which
r9 §1.2 does not separate:

- **Genuine finding.** A review carrying `invalidates` or `invalidated` whose `reviewed` names an exact
  `{path, blob_sha256}` present in `R*`, and whose `reviewer` differs, as an identity string
  (R6.RECON.29), from that record's `author` and is not a run, check or Issue. Its independence is
  established. Its form failures, if any, still bind (Form (i)).
- **Provisional block.** A review carrying `invalidates` or `invalidated` whose `reviewed` names an
  exact reference absent from `R*`. Its independence cannot be established. It binds as a form
  failure, so a run fails closed, but it is not yet a finding.

The reference is exact, so the named record's bytes, and its `author`, are fixed. Only that exact
reference resolves a provisional block: a record at the same path with other bytes, or a
byte-identical copy at another path, is another reference (R6.RECON.29) and resolves nothing. When the
named record enters `R*`, the provisional block resolves:

- if the record's `author` equals the review's `reviewer`, the review is disqualified by the
  independence failure of Form (i). No finding existed. The provisional block is **resolved**, not
  discharged;
- otherwise the review is a genuine finding.

Each review resolves on its own: two reviews naming the same record resolve separately by their own
reviewers.

The resolution is permanent where the named record has a durable witness in `M`'s ancestry. Where the record
is seen only through `F`, `REV` or an explicit input, the resolution holds for runs whose roots or
inputs still reach it; a later run that does not reach it sees the review as provisional again (r9
R-1). A provisional block whose record never enters `R*` keeps blocking.

***

## 2. Amended statements

**A1.1 Obligation monotonicity (r9 §1.2).** `Obl(t)` is the set of genuine findings established up to
time `t` whose named record has a durable witness in `M`'s ancestry. Requirement (I), `Obl(t) ⊆ Obl(t')` for
`t' >= t` with every member binding until a discharge lifts it, applies to these. A provisional block
is not a member of `Obl(t)`. It binds while its named record is absent from `R*`, and leaves the
blocking set only by a discharge or by resolution to a disqualified review. Resolution to a genuine
finding through a record with a durable witness in `M`'s ancestry adds it to `Obl` permanently; through a record seen only via `F`,
`REV` or an explicit input it carries r9 R-1.

**A1.2 Resolution is not removal (r9 R6.OBL29.6, §2.3).** Resolving a provisional block by later
evidence that establishes a same-author review is a determination from the evidence, as r9 §2.3
already states for a lack of independence, not a removal and not a discharge. It applies only where
the named record, by exact reference, is in `R*` and shows `author` equal to `reviewer`. It never
applies to a genuine finding in `Obl`: the named record's bytes are fixed and stay in `R*_M`, so no
later record, review or rewrite can disqualify it. Deleting, moving or rewriting the named record
after it entered `R*_M` changes nothing (R6.OBL29.6).

**A1.3 Outcome of a provisional block.** While it binds without an applying discharge, the run reports
FAIL `record-invalid` for the form failure and `retirement-blocked` for the block, as Form (i) and
owner decision item 5 require. It is not ERROR: evaluation is reliable, and the absence of the record
is the evaluated fact. A required object that is unreadable or does not verify remains ERROR under
R6.OBL29.7 and R6.REC.17.

**A1.4 Keys (b) and a later record.** R6.RECON.27 Keys (b) admits `repair: null` for "a review whose
`reviewed` names no record the scan finds". It applies only while the named record is absent from
the run's whole `R*`, including entries seen only through `F`, `REV` or an explicit input. Once the
record is in the run's `R*` and the review is a genuine finding, a reassessment that relied on Keys
(b) does not apply in that run: the finding binds and needs a repair (Keys: "A finding of the second
kind by an independent reviewer needs a repair however it is malformed"). Once the record shows a
same-author review, the review is disqualified and the reassessment has nothing to discharge. Whether
the finding stays in `Obl` for later runs is decided by A1.1: permanently where the record has a
durable witness in `M`'s ancestry, otherwise with r9 R-1.

**A1.5 Effect on r13 Form (i).** On adoption, R6.RECON.26 Form (i)'s last clause reads: "a review whose
`reviewed` names no record in `R*` (R6.OBL29.3), so that its independence cannot be established,
counts, as a form failure, while that record is absent from `R*` (a provisional block); once the
record is in `R*`, the review is disqualified if its `reviewer` equals that record's `author`, and
otherwise counts under the preceding rules. Resolution through a record in the `M`-derived part of
`R*` is permanent; through a record seen only via `F`, `REV` or an explicit input it carries r9
R-1." Keys (b) reads with A1.4; the other Forms keep their text.

***

## 3. Controls

SELF-REVIEW-RECORD-LANDS-LATER is a tool control of PR #1577
(`tools/ledger_coverage/adapters/obl29_controls.py` at `7db52f380f1e51d4af52b84f0a7e728827ac5a60`), not a
row of r9's `CONTROLS.json`. It pins the "after" half already and expects ERROR `DESIGN_UNSETTLED`
before; on adoption its "before" half changes to A1.3. The other rows are new specifications, with
runner null until implemented.

| Id | Setup | Expected |
|---|---|---|
| SELF-REVIEW-RECORD-LANDS-LATER (tool control; expectation changed) | The invalidating review lands first with its named record absent; then the record lands on `main` with `author` equal to the review's `reviewer` | before the record lands: FAIL `record-invalid` and `retirement-blocked` (A1.3); after: no second-kind finding and no block from that review (A1.2) |
| INDEPENDENT-RECORD-LANDS-LATER | As above, but the record's `author` differs from the reviewer | before: as above; after: a genuine finding that binds |
| INDEPENDENT-RECORD-THEN-DELETED | Continue the previous case: the record and the review are deleted from later trees | the genuine finding still binds (A1.1, R6.OBL29.6) |
| INDEPENDENT-RECORD-VIA-REV-ONLY | The named record, with an independent author, is seen only in an admitted `REV`, which never reaches `main`; the first run cites a reassessment with `repair: null` under Keys (b); a later run omits that `REV` | the first run: the Keys (b) reassessment does not apply and the genuine finding binds, FAIL `retirement-blocked` (A1.4); the later run: the review is provisional again, FAIL `record-invalid` and `retirement-blocked` (r9 R-1) |
| PROVISIONAL-RECORD-NEVER-LANDS | The named record never enters `R*` | FAIL `record-invalid` and `retirement-blocked` at every later `M` |
| PROVISIONAL-FORGED-SAME-PATH (countercase) | While the block is provisional, a byte-different record at the named path, whose `author` equals the reviewer, lands on `main` before the true record | the block stays provisional: the forged record is another reference and resolves nothing |
| GENUINE-THEN-SAME-PATH-REWRITE (countercase) | After INDEPENDENT-RECORD-LANDS-LATER, a byte-different record at the same path naming the reviewer as `author` lands | the genuine finding still binds (A1.2) |
| PROVISIONAL-COPY-AT-OTHER-PATH | A byte-identical copy of the named record lands at another path, author equal to the reviewer, while the named reference stays absent | the block stays provisional |
| TWO-REVIEWS-ONE-RECORD | Two invalidating reviews name the same record, one by the record's eventual author, one by another reviewer; then the record lands | the first is disqualified; the second is a genuine finding that binds |
| PROVISIONAL-NULL-DISCHARGE-THEN-INDEPENDENT-LANDS | While the block is provisional, a reassessment with `repair: null` under Keys (b) is cited and applies; then the named record lands on `main` with an independent author | the genuine finding binds, the reassessment no longer applies, and the run is FAIL `retirement-blocked` (A1.4) |

***

## 4. What this amendment does not do

It does not change which reviews are genuine findings, the independence rule, Keys other than as A1.4 reads (b), the reliance and
clearance predicates of r9 §2.2, the custody design, or any discharge route. It authorizes no
implementation.

## 5. References (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7207734407, items 4 and 5 | authority and outcome rule, quoted in §0 | provenance |
| r9 `DESIGN.md` at `77a73c022091f598cf807fcf89d66c3cf43208de` | the text amended | support off `main` until #1601 lands |
| Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e`, R6.RECON.26 Form (i) | the clause clarified | support on `main` (landed by #1604) |
| PR #1577 at `7db52f380f1e51d4af52b84f0a7e728827ac5a60` | the existing control | provenance |
