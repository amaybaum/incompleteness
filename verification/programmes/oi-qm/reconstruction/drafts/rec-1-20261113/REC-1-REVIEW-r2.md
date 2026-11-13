# REC-1 r2: focused re-check by the r1 reviewer

**Object.** Draft PR #1268 at exact head `b39e40ff1f5af89af736f7eb7ad7b4a5cb14ee0f`, a single
child of `d7f7aac1`. It adds `REC-1-r2.md`, `REC-1-NOTES-r2.md`, `REC-1-REVIEW-r1.md` and
`REC-1-RESPONSE-r1.md`. The r1 files are unchanged. `REC-1-REVIEW-r1.md` is byte-identical to the
r1 review (checked with `diff`). This check was read-only and paper-only, and P0 was not carried out.

## Verdict: **ACCEPT WITH CHANGES** (5 required changes, all small text edits)

### 1. RC-1 to RC-16, checked against the r1→r2 diff

All sixteen are applied, and the review's old→new texts are used verbatim. I checked the new
citations at `c3b5f37a`:
- S3:107 and S3:198–201.
- S3:206–207 ("The restricted record theory is a classical simplex theory…").
- P:143–146 (H-μ, `TUNE-1-STEP2-PROPOSAL.md` on `main`).
- OA2:75 and :626.
- OA2:874 (Corollary E1 labelled "[W] + [RW]").
- OA3:228–232, :410–416 and :474–475.

All match.

**The writer's additions under RC-1, checked as new text:**
- *P0 pass/fail sentence.* It is correct and consistent with P4 ("subject to P4").
- *Comparison with AW-OA2-1.*
  - It correctly says that dropping H-AR adds no premise.
  - It correctly says the two classes are incomparable.
  - It then calls the post-P0 residual "a smaller class than AW-OA2-1's". That contradicts
    "incomparable" (RC-r2-2).
  - "Read-side route of N2.1 (OA2:75)" is a REC-1 reading: OA2:75 does not name AW-OA2-1. It is
    acceptable, and optional suggestion 1 asks for it to be tagged.
- *Ordering rule.* It is sound in structure, but it drops two things:
  - P4's controls, including non-vacuity (v), which P0's own sentence keeps.
  - The herald typing and C-PM from the scope carried to AW-OA2-1 (RC-r2-3).
- *Scope of S3:206–207.* r2 attributes the statement to "the fragment of unheralded preparations
  and of heralds on prefixes of one length". S3's object is narrower: continuation-record laws under
  R-lin with a coset-uniform law, in initial-condition mode, after heralds on a complete prefix. It
  is not OBL-SP's E3 prepare–measure fragment under C-PM (RC-r2-1). The hedged uses "points to O-C"
  in §5 and NOTES item 7 are acceptable once §4 states the scope.

**RC-13: the per-reference §A.42 item 8 table, checked as new text.**
- Every reference is now classified individually.
- The off-main support rows are named as gaps: the Q1/Q2 terms, rows 36 and 37, §3.1, C6, C16,
  C17, rows 46 and 47, and the C3 attribution.
- The provenance rows are justified: 3A:295–297, 3A:212–214, 3A:613–617, OC1:359–363 and the PR
  #1268 line.
- The landing sentence is present.
- C12 is moved to P:145 on `main`, which I verified.

No misclassification found.

### 2. The writer's non-applications of optional suggestions

- **Suggestion 4: accepted.** OA2:874 labels Corollary E1 "[W] + [RW]", so row 22's label has a
  source, and r2 now cites it. My suggestion read only the label at OA2:577.
- **Suggestion 6: accepted.** It was a reviewer conjecture with no record behind it. Keeping it out
  of the record and leaving it to the P0 unit, scoped to finite rings, is the correct handling.

### 3. New overclaims

None in the classification table:
- §A.34 handling is unchanged and correct.
- [R] and [R-off] tags are kept, and the new S3 uses are tagged [R].
- OA-3 stays finite-ring scoped (rows 12, 27 and 28).
- NL-C keeps its form (rows 33 and C18).
- The P0 sketch is explicitly not used as a result.

One quantifier swap was introduced in NOTES r2 item 6 (RC-r2-4). It came from my own r1 wording
under RC-12, so I correct it here.

### 4. RC-16 tier change

The high→supporting change is stated as a proposal ("proposed tier", "authorization: not
authorized"). Its justification cites S3:206–207 and P0 on `main`, which is sourced. Accepted,
subject to RC-r2-1's scope wording.

***

## Required changes

**RC-r2-1 (scope of S3:206–207).** In `REC-1-r2.md` §4, *What P0 may settle*, first bullet:
- Old: "S3:206–207 [R] states that this restricted record theory is a classical simplex
  theory, and the r1 review sketches"
- New: "S3:206–207 [R] states that the record theory of continuation laws under R-lin with a
  coset-uniform law, in initial-condition mode, after heralds on a complete prefix, is a classical
  simplex theory (it is not stated for the E3 prepare–measure fragment under C-PM), and the r1
  review sketches"

**RC-r2-2 (incomparable vs "smaller").** Same section, third bullet:
- Old: "and because a P0 pass narrows it to the herald-retention residual, a smaller class than
  AW-OA2-1's (every non-additive read map)."
- New: "and because a P0 pass narrows it to the herald-retention residual, a subset of OBL-SP's own
  preparations. The ordering is by cost, not by the size of the two classes, which are not nested."

**RC-r2-3 (ordering rule keeps the controls and the full scope).** Fourth bullet:
- Old: "OBL-SP closes as O-C, and the next obligation is AW-OA2-1 with the same φ, `D_0`, (H3),
  record class, (xiv) and (SP) and a non-additive read map; no premise enters."
- New: "OBL-SP closes as O-C, subject to P4 (O-V if (v) fails), and the next obligation is
  AW-OA2-1 with the same φ, `D_0`, (H3), record class, herald typing, C-PM, (xiv) and (SP) and a
  non-additive read map; no premise enters."

**RC-r2-4 (quantifier order; the error came from the r1 review's wording).** In
`REC-1-NOTES-r2.md`, item 6:
- Old: "For a designed map every definable operation is reachable, so Q2-F there differs from Q2-A
  only by the stated standing;"
- New: "For every definable finite target some designed map reaches it (Main:580–582), so Q2-F
  for a designed map differs from Q2-A only by the stated standing;"

**RC-r2-5 (file name and punctuation).** In `REC-1-r2.md`:
- Line 4, old: "`RESPONSE-r1.md`". New: "`REC-1-RESPONSE-r1.md`".
- Line 39, old: "`c3b5f37a354bb26437e2e0165c576a347a63c153` blobs by". New:
  "`c3b5f37a354bb26437e2e0165c576a347a63c153`, blobs by".

## Optional suggestions

1. Tag "It is the read-side route of N2.1 (OA2:75)" as "[W, REC-1]". OA2:75 names the two sides
   of N2.1 but not AW-OA2-1.
2. NOTES item 8 could cite OA3:474–475 ("Under held-at-use herald typing that class is itself
   retention-type") as its source.
