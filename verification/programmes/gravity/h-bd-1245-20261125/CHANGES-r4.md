# #1245 H-BD report: change map r3 -> r4

Base: r3 at `44e981885516715d3b1b267135c5b199b07f41e1` (`verification/programmes/gravity/h-bd-1245-20261125/REPORT-r3.md`). Delta review of r3: verdict ACCEPT-WITH-NITS, nits 1-3, for record on PR #1564 (no comment id was found by a read-only GET at r4's writing).

Owner decision (amaybaum, 2026-11-25 (coordinating session; GitHub record pending)), quoted: "Apply the three remaining nits: * Remove the unsupported implication of "jointly". * Classify status-block references individually. * Add the decision timestamp. Include these in a minimal final correction with a short delta review. The underlying mathematical results are accepted in substance."

Scope kept: only the five changes below are made to the report. No mathematical result, proof, number, condition or output class is changed, and P3-EVIDENCE.md and the earlier revisions and change maps are unchanged. No manuscript, Lean, premise, git or GitHub change. The wording "a conflict with the four items jointly" occurs once in REPORT-r3.md; CHANGES-r3.md, which also uses it, is a record of r3 and is not edited.

GitHub reads for r4 (read-only GETs): #1245 comments since 2026-11-25T00:00Z (ids 7163939634, 7164442366, 7164513272, 7166798992; none records the r3 or r4 decision); PR #1564 comments since 2026-11-25T15:00Z (ids 7166704115, 7167216051; no record of the r3 delta review) and PR #1564 reviews (none).

***

## Changes, with old and new text

### Change 1. Title

- *Reason:* Revision label.

Old:

```text
revision r3
```

New:

```text
revision r4
```

### Change 2. Status, pin, sources: r3 owner-decision time

- *Reason:* Owner nit 3 (sec. A.42 item 7). No GitHub record of the decision was found on #1245 by a read-only GET at r4's writing.

Old:

```text
r3 applies the owner's decision (amaybaum, 2026-11-25, coordinating session), quoted:
```

New:

```text
r3 applies the owner's decision (amaybaum, 2026-11-25 (coordinating session; GitHub record pending)), quoted:
```

### Change 3. Status, pin, sources: new r4 bullet after "Revision r3"

- *Reason:* Status record of r4 with the owner decision quoted.

Old:

```text
The r3 changes are not yet independently reviewed.
- **Pin.**
```

New:

```text
The r3 changes are not yet independently reviewed.
- **Revision r4.** Revision r3 (commit `44e98188`) was independently delta-reviewed (verdict ACCEPT-WITH-NITS; for record on PR #1564, where no comment id was found by a read-only GET at r4's writing); the statement above that the r3 changes are not yet independently reviewed describes r3 before that review. r4 applies the owner's decision (amaybaum, 2026-11-25 (coordinating session; GitHub record pending)), quoted: "Apply the three remaining nits: * Remove the unsupported implication of "jointly". * Classify status-block references individually. * Add the decision timestamp. Include these in a minimal final correction with a short delta review. The underlying mathematical results are accepted in substance." r4 changes only the R1 contribution wording (sec. 3), the classification of the status-block references (sec. 1, off-`main` references) and the time of the r3 owner decision; no mathematical result is changed. The r4 changes are not yet independently reviewed.
- **Pin.**
```

### Change 4. Sec. 1, off-`main` references: status-block references classified individually

- *Reason:* Owner nit 2 (sec. A.42 item 8).

Old:

```text
R1 does not rest on it.

**Routes in the Issue body already closed:**
```

New:

```text
R1 does not rest on it.
- Status-block references, each classified by the statement it is attached to; no result, derivation or output class of this report uses any of them:
  - #1245 comment 7163939634 (owner decision resuming the round; Status): **support off `main`** for the statement that the round was resumed by owner decision on 2026-11-25; the report cites it by id and does not quote it.
  - #1245 comment 7166798992 (owner decision on r2; Review status, Sources): **support on `main`** for the statement of that decision, through the quotation of its operative text with author and time in Review status, which is on `main` once this report lands.
  - PR #1564 comment 7166704115, in its review-verdict uses (Review status: verdict REVISE; sec. 7: R1 (r1 form), R2(a) and R2(c) independently reviewed): **support off `main`** for those review-history statements. Its credit use for R2(d) and the terrace proof is classified above.
  - PR #1564 comment 7167216051 (delta review of r2; Revision r3): **support off `main`** for the statement that r2 was delta-reviewed with verdict ACCEPT-WITH-NITS.
  - The delta review of r3 (Revision r4; for record on PR #1564): **support off `main`** for the statement that r3 was delta-reviewed with verdict ACCEPT-WITH-NITS.
  - The owner decisions quoted for r3 and r4 (coordinating session; GitHub record pending): **support on `main`** for the statements of those decisions, through their verbatim quotation with author and date in Revision r3 and Revision r4.

  The four references classed as support off `main` are gaps under sec. A.42 item 8 for review-history and authorization statements only. They close if the landing carries the cited decision and review texts (sec. A.46 item 8) or by a recorded owner decision; r4 does not close them.

**Routes in the Issue body already closed:**
```

### Change 5. Sec. 3, R1, contribution relative to P3

- *Reason:* Owner nit 1: the preserved text lists the four items without saying whether the conflict is joint.

Old:

```text
at site-local cuts with D→B dependence": a conflict with the four items jointly. The derivations
```

New:

```text
at site-local cuts with D→B dependence"; it lists the four items together, and the only derivation it records is under (vii). The derivations
```

***

## Status-block references now classified (Change 4)

| Reference | Statement it supports | Class |
|---|---|---|
| #1245 c.7163939634 | round resumed by owner decision (Status) | support off `main` |
| #1245 c.7166798992 | owner decision on r2 (Review status, Sources) | support on `main` (quoted in the report) |
| PR #1564 c.7166704115, verdict uses | r1 reviewed, verdict REVISE (Review status; sec. 7) | support off `main` |
| PR #1564 c.7167216051 | r2 delta-reviewed, ACCEPT-WITH-NITS (Revision r3) | support off `main` |
| r3 delta review, for record on PR #1564 | r3 delta-reviewed, ACCEPT-WITH-NITS (Revision r4) | support off `main` |
| owner decisions for r3 and r4 | the decisions quoted (Revision r3, Revision r4) | support on `main` (quoted in the report) |

The four off-`main` supports concern review-history and authorization statements only; no result, derivation or output class uses them. They remain gaps under sec. A.42 item 8 until the landing carries the cited texts (sec. A.46 item 8) or a recorded owner decision closes them.