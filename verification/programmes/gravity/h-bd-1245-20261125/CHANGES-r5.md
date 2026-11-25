# #1245 H-BD report: change map r4 -> r5

Base: r4 at `0d08c7f445d390eff018be97ae4003d8ec627150` (`verification/programmes/gravity/h-bd-1245-20261125/REPORT-r4.md`). Delta review of r4, verdict line verbatim: "**Delta review of r4 (#1245 report, PR #1564) at 0d08c7f4, compared with r3 at 44e98188. Verdict: REVISE.**"

Owner decision (amaybaum, 2026-11-25T16:29:44Z, coordinating session; record #1169 comment 7169907126), quoted: "#1245 — H-BD | Correct the overstated replacement for "jointly", add the missing timestamp, and preserve the four supporting statements with their provenance in the landing package." "Resolve the identified findings directly. Preserve the necessary supporting evidence and provenance." "Earlier revisions should carry a short superseded notice identifying the authoritative report. No elaborate historical annotation is needed." "Do not create additional tracking documents, verification mechanisms or governance requirements where existing ones suffice." "do not turn minor editorial preferences into additional revision cycles."

Scope kept: REPORT-r5.md is REPORT-r4.md with only the changes below. No mathematical result, proof, number, condition or output class is changed; P3-EVIDENCE.md and the earlier change maps are unchanged. Each earlier report revision (REPORT.md, REPORT-r2.md, REPORT-r3.md, REPORT-r4.md) gains only the one-paragraph superseded notice below, prepended; none carried a notice before. No new file other than this change map and REPORT-r5.md.

Superseded notice prepended to each earlier revision:

```text
> **Superseded.** This revision of the #1245 H-BD report is superseded. The authoritative report is `REPORT-r5.md` in this directory; its change map is `CHANGES-r5.md`.
```

***

## Changes to REPORT-r4.md, with old and new text

### Change 1. Title

- *Reason:* Revision label.

Old:

```text
revision r4

## Status
```

New:

```text
revision r5

## Status
```

### Change 2. Status: resumption decision quoted

- *Reason:* Closes the support-off-`main` gap for the resumption statement by quoting its operative text with author and time (sec. A.42 items 2, 7 and 8; r4 delta review finding 3).

Old:

```text
resumed by owner decision 2026-11-25 (#1245 comment 7163939634).
```

New:

```text
resumed by owner decision (amaybaum, 2026-11-25, coordinating session; recorded at #1245 comment 7163939634, record time 2026-11-25T13:33:04Z), quoted: "Lift the pause and resume paper-only research under the existing authorization. Build on the previous findings without repeating completed investigations. Confirm High tier."
```

### Change 3. Review status: r2 decision time labelled as record time

- *Reason:* The comment dates the decision only to 2026-11-25; 15:24:39Z is the time the record was posted (r4 delta review finding 3).

Old:

```text
(amaybaum, #1245 comment 7166798992, 2026-11-25T15:24:39Z:
```

New:

```text
(amaybaum, #1245 comment 7166798992, record time 2026-11-25T15:24:39Z:
```

### Change 4. Revision r3: decision time and record

- *Reason:* Owner nit 3 and r4 delta review finding 2: the time is given (as the record time of the decision's GitHub record), "GitHub record pending" and the nested parentheses are dropped.

Old:

```text
r3 applies the owner's decision (amaybaum, 2026-11-25 (coordinating session; GitHub record pending)), quoted:
```

New:

```text
r3 applies the owner's decision (amaybaum, 2026-11-25, coordinating session; record #1169 comment 7169905383, record time 2026-11-25T17:43:18Z), quoted:
```

### Change 5. Revision r4: r3 delta review, decision time, wording

- *Reason:* r4 delta review findings 2 and 3: the r3 delta review is cited by its comment id, the r4 decision by its time and record; "GitHub record pending" and the nested parentheses are dropped.

Old:

```text
Revision r3 (commit `44e98188`) was independently delta-reviewed (verdict ACCEPT-WITH-NITS; for record on PR #1564, where no comment id was found by a read-only GET at r4's writing); the statement above that the r3 changes are not yet independently reviewed describes r3 before that review. r4 applies the owner's decision (amaybaum, 2026-11-25 (coordinating session; GitHub record pending)), quoted:
```

New:

```text
Revision r3 (commit `44e98188`) was independently delta-reviewed at PR #1564 comment 7169924204 (verdict ACCEPT-WITH-NITS); the statement above that the r3 changes are not yet independently reviewed describes r3 before that review. r4 applies the owner's decision (amaybaum, 2026-11-25T16:17:51Z, coordinating session; record #1169 comment 7169906297), quoted:
```

### Change 6. Revision r4: description of the r3-decision change

- *Reason:* r4 delta review finding 2 (r4 changed the citation of the r3 decision, not its time); new r5 status line with the owner decision and the r4 delta review verdict quoted.

Old:

```text
and the time of the r3 owner decision; no mathematical result is changed. The r4 changes are not yet independently reviewed.
```

New:

```text
and the citation of the r3 owner decision; no mathematical result is changed. The r4 changes are not yet independently reviewed.
- **Revision r5.** Revision r4 (commit `0d08c7f4`) was independently delta-reviewed; its verdict line, verbatim: "**Delta review of r4 (#1245 report, PR #1564) at 0d08c7f4, compared with r3 at 44e98188. Verdict: REVISE.**" The statement above that the r4 changes are not yet independently reviewed describes r4 before that review. r5 applies the owner's decision (amaybaum, 2026-11-25T16:29:44Z, coordinating session; record #1169 comment 7169907126), quoted: "#1245 — H-BD | Correct the overstated replacement for "jointly", add the missing timestamp, and preserve the four supporting statements with their provenance in the landing package." "Resolve the identified findings directly. Preserve the necessary supporting evidence and provenance." "Earlier revisions should carry a short superseded notice identifying the authoritative report. No elaborate historical annotation is needed." "Do not create additional tracking documents, verification mechanisms or governance requirements where existing ones suffice." "do not turn minor editorial preferences into additional revision cycles." r5 changes only the R1 contribution clause (sec. 3), the times and records of the owner decisions in this section, the quotation of the resumption decision in Status, and the classification of the status-block references (sec. 1, off-`main` references), which now quotes the cited review verdicts; no mathematical result is changed. The r5 changes are not yet independently reviewed.
```

### Change 7. Sec. 1: status-block references

- *Reason:* r4 delta review finding 3: the four support-off-`main` gaps are closed by quoting the operative texts in the record; the closing sentence cites sec. A.42 items 2 and 8 and states closure no later than landing.

Old:

```text
  - #1245 comment 7163939634 (owner decision resuming the round; Status): **support off `main`** for the statement that the round was resumed by owner decision on 2026-11-25; the report cites it by id and does not quote it.
  - #1245 comment 7166798992 (owner decision on r2; Review status, Sources): **support on `main`** for the statement of that decision, through the quotation of its operative text with author and time in Review status, which is on `main` once this report lands.
  - PR #1564 comment 7166704115, in its review-verdict uses (Review status: verdict REVISE; sec. 7: R1 (r1 form), R2(a) and R2(c) independently reviewed): **support off `main`** for those review-history statements. Its credit use for R2(d) and the terrace proof is classified above.
  - PR #1564 comment 7167216051 (delta review of r2; Revision r3): **support off `main`** for the statement that r2 was delta-reviewed with verdict ACCEPT-WITH-NITS.
  - The delta review of r3 (Revision r4; for record on PR #1564): **support off `main`** for the statement that r3 was delta-reviewed with verdict ACCEPT-WITH-NITS.
  - The owner decisions quoted for r3 and r4 (coordinating session; GitHub record pending): **support on `main`** for the statements of those decisions, through their verbatim quotation with author and date in Revision r3 and Revision r4.

  The four references classed as support off `main` are gaps under sec. A.42 item 8 for review-history and authorization statements only. They close if the landing carries the cited decision and review texts (sec. A.46 item 8) or by a recorded owner decision; r4 does not close them.
```

New:

```text
  - #1245 comment 7163939634 (owner decision resuming the round; Status): **support on `main`** for the statement that the round was resumed by owner decision on 2026-11-25, through the quotation of its operative text with author and record time in Status.
  - #1245 comment 7166798992 (owner decision on r2; Review status, Sources): **support on `main`** for the statement of that decision, through the quotation of its operative text with author and record time in Review status.
  - PR #1564 comment 7166704115, in its review-verdict uses (Review status: verdict REVISE; sec. 7: R1 (r1 form), R2(a) and R2(c) independently reviewed): **support on `main`** for those review-history statements, through this quotation. The comment was posted by amaybaum at 2026-11-25T15:21:04Z as reviewer text, verbatim, of "a Claude reviewer agent started with a fresh context" that "wrote none of the reviewed work and made no GitHub or repository writes"; its operative verdict line reads, verbatim: "**Verdict: REVISE.** The mathematics I re-derived holds: the R1 single-site step, the R2(a) bound, the R2(c) one-step hybrid bound with its constant 4, and the cone-form arithmetic." Its credit use for R2(d) and the terrace proof is classified above.
  - PR #1564 comment 7167216051 (delta review of r2; Revision r3): **support on `main`** for the statement that r2 was delta-reviewed with verdict ACCEPT-WITH-NITS, through this quotation. The comment was posted by amaybaum at 2026-11-25T15:40:52Z as reviewer text, verbatim, of "a Claude reviewer agent started with a fresh context" that "wrote none of the reviewed work and made no GitHub or repository writes"; its operative verdict line reads, verbatim: "**Verdict for REPORT-r2.md: ACCEPT-WITH-NITS.**"
  - The delta review of r3 (Revision r4): **support on `main`** for the statement that r3 was delta-reviewed with verdict ACCEPT-WITH-NITS, through this quotation. It is PR #1564 comment 7169924204, posted 2026-11-25T17:44:06Z; its operative verdict line reads, verbatim: "**Verdict for REPORT-r3.md with P3-EVIDENCE.md: ACCEPT-WITH-NITS.**"
  - The delta review of r4 (Revision r5): **support on `main`** for the statement that r4 was delta-reviewed with verdict REVISE, through the verbatim quotation of its verdict line in Revision r5.
  - The owner decisions quoted for r3, r4 and r5 (coordinating session; records #1169 comments 7169905383, 7169906297 and 7169907126): **support on `main`** for the statements of those decisions, through their verbatim quotation with author and time in Revision r3 (record time), Revision r4 and Revision r5.

  No status-block reference is support off `main`: each statement it supports rests on text quoted in this record, which is on `main` no later than the record lands (sec. A.42 items 2 and 8).
```

### Change 8. Sec. 3, R1 contribution relative to P3

- *Reason:* r4 delta review finding 1: the replaced clause was broader than the preserved P3 text; the reviewer's wording is used.

Old:

```text
; it lists the four items together, and the only derivation it records is under (vii). The derivations
```

New:

```text
; it lists the four items together and does not state whether the conflict holds for each item separately or only for their conjunction. The derivations
```
