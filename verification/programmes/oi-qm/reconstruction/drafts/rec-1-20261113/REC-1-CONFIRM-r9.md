# Focused confirmation of REC-1 r9 (housekeeping: §6 rows and P5)

**Verdict: ACCEPT.** No changes are required. The r8→r9 diff contains exactly the stated changes.

- All 30 new §6 rows are classified correctly against the claims that cite them. None is
  mislabelled support or a hidden off-`main` gap.
- P5 is accurate, and it is the owner's chosen wording verbatim.
- Every cited id resolves, with the stated author and time.
- The two consistency edits the writer chose are justified.

There is one optional Low suggestion (finding 4) and two Info notes.

**Object.** Branch `research/rec-1-1169-20261113`, fetched by name with full history.

- **Commit.** Head `2594d4743a6184c3e21d5d8ff916b34e03bb48bb`, a single-parent child of
  `2a9f10ba`. I checked it out detached in my review worktree and confirmed HEAD.
- **Added files.** `git diff --stat 2a9f10ba 2594d474` shows exactly two:
  `REC-1-r9.md` and `REC-1-NOTES-r9.md`. `REC-1-r8.md` is unchanged.

**Authority read.**
- #1268 c.6863418087 (`amaybaum`, 2026-11-13T19:58:15Z), "Authorize both (Recommended)".
- #1268 c.6863753317 (`amaybaum`, 2026-11-13T20:14:06Z), "Name both (Recommended)". Its P5 block
  quote is the r9 P5 text verbatim.
- #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z).
- #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z).
- #1268 review 5896999901, at `2a9f10ba`, 19:41:57Z.

**Checks run at the head:**
- `tools/claims_check.py`: OK.
- `tools/staleness_check.py`: OK.
- `tools/voice_check.py`: OK.
- `tools/artifact_placement_check.py`: OK, self-test passed.
- `tools/legacy_records_check.py 2594d474…`: 303 records intact.

All five exit 0.

***

## Findings

### 1. Diff scope (no defect)

**Evidence.**
- `diff -u REC-1-r8.md REC-1-r9.md` has 4 hunks, 3 lines removed and 37 added, 67 lines in all.
  - Hunk 1 changes the title.
  - Hunk 2 adds one sentence to the Revision paragraph, at r9:18–22.
  - Hunk 3 changes P5, at r9:371.
  - Hunk 4 adds the 30 rows at r9:465–494, between the r1 row and the unchanged closing paragraph
    at r9:496–497.
- NOTES-r9's embedded diff equals the actual diff line for line.
- r9 has 497 lines, sha256 `c0a99912…` and blob `945b7982`. All three are as NOTES states.
- §5 item 1 at r9:414–419 is byte-identical to r8:410–415.
- No result, verdict, classification, decision rule, control or bearing changes.

**Fix.** None.

### 2. Classification of the 30 rows (no defect; one Info note)

**Evidence: completeness.**
- I listed every reference in the r2–r9 Revision sentences, by revision:

  | Revision | References |
  |---|---|
  | r2 | 1 |
  | r3 | 3 |
  | r4 | 4 |
  | r5 | 3 |
  | r6 | 4 |
  | r7 | 3 |
  | r8 | 5 |
  | r9 | 4 |

- Add C12 (1) and P5 (2). The total is 30, one row each, and no reference lacks a row.

**Evidence: git objects.**
- Every cited commit resolves and is an ancestor of `2a9f10ba` that is not on `main`:
  `b39e40ff`, `94816172`, `1fd0c241`, `d5496ba8`, `c73e855f`, `6de32c95`, `1ab6371b`, `f0757fdb`,
  `cd38655c`, `2a9f10ba`, `4b81298f`.
- Every cited blob matches its file at the cited commit and is unchanged at `2a9f10ba`:

  | File | Blob |
  |---|---|
  | r2 | `59f862d9` |
  | r3 | `b93d3e45` |
  | r4 | `177778cd` |
  | r5 | `6f85a38f` |
  | r6 | `6febde7a` |
  | r7 | `f1ffac0e` |
  | P0-r3 | `611a4d9a` |
  | r8 | `615b7de8` |

- Every "last written at" commit is the file's last change on the branch, per `git log`.
- "The re-check of r2" is `REC-1-REVIEW-r2.md`, and "the confirmation of r4" is
  `REC-1-CONFIRM-r4.md`. I confirmed both from the file headers.

**Evidence: reviews and comments, read through the API.**
- Each has the stated author, time and `commit_id`:
  - review 5890763675: `1fd0c241`, 12:12:46Z;
  - review 5890968976: `6de32c95`, 12:27:37Z;
  - review 5892912758: `cd38655c`, 14:39:31Z;
  - review 5896999901: `2a9f10ba`, 19:41:57Z;
  - c.6852814589: 12:24:56Z;
  - c.6853268285: 12:43:15Z.
- c.6852814589 and c.6853268285 are checkpoint comments that record the in-session owner decisions
  "(a) Explicit hypothesis (Recommended)" and "Proceed with all (Recommended)". Rows 471 and 478
  correctly say "recorded at".
- The quotations in rows 493 and 494 match #1169 c.6854241002 and c.6863414487, emphasis removed.

**Evidence: support vs provenance.**
- **Row 469.** Review 5890763675 asked for three things, and none of them gives the record support
  off `main`:
  - H-xiv, which is carried as a hypothesis on Main:724 and OA2:102–104;
  - C8's μ-G wording, on OA1:103–105;
  - the P0 implementation checks, which are preregistered requirements.
- **Row 476.** Review 5890968976 asked for P0's three-way rule, a preregistered decision rule.
- **Row 484.** The §4 L reading (r9:301–307) cites only OA2:502 and OA3:120–123, :474–475 on
  `main`. I confirmed this in REVIEW-r8 finding 2.
- **Row 485.** No body passage of r9 cites P0-r3. `grep` finds it only at r9:16 and in §6.
- **Row 488.** I read review 5890763675's "Required clarification" paragraph. It gives the same two
  points C12 states and no further derivation. The procedure class is OA2:102–104, on `main`.
  - The content the C12 sentence uses is therefore carried in the record itself.
  - H-xiv is carried as a hypothesis, so no result depends on whether it is underivable.
  - "Provenance" is therefore correct.
- **Rows 471, 478, 483, 489, 493 and 494.** These owner records are the sources of governance
  statements, quoted with author and time as §A.42 item 7 provides. Their classification follows
  the existing r8:456 precedent.

**Info note.** C12's claim "It is not a consequence of C11 or of φ" is a negative claim. It is
supported by two stated points rather than by an exhibited instance. NOTES-r9 §4 point 3 records
this. Nothing rests on the claim, and it is outside items (a) and (b). No action is needed here.

**Fix.** None.

### 3. P5 (no defect; one Info note)

**Location.** r9:371.

**Evidence.**
- P5 names P0, authorized by #1169 c.6854241002 at 13:24:47Z.
- It names the C3 check of the R-lin update with (xiii), authorized by #1169 c.6863414487 at
  19:58:05Z ("C3 check (SQ3). A bounded, paper-only check of the actual R-lin update with (xiii)").
- Both ids resolve, and the author and time match.
- The text is the wording the owner chose at #1268 c.6863753317, verbatim.

**Info note on scope.** "No other unit is authorized" is accurate when read, as P5's place in
OBL-SP's prerequisites implies, as concerning OBL-SP units.
- c.6863414487 also authorizes "G3 unit 2(a)" (#873) and an "Integration assessment".
- c.6854241002 also authorizes a TUNE-1 sourcing unit and the #1230/#1232 reconcile.
- None of these is an OBL-SP unit. The owner chose this exact wording, so no change is needed.

**Fix.** None.

### 4. The two consistency edits the writer chose (justified; one optional suggestion)

**Locations.** r9:21–22 and r9:490.

**Evidence.**
- r9:21–22 says "P5 names the authorized units". This matches P5 as the owner fixed it. A literal
  echo of c.6863418087 item (b), "no other unit was", would have contradicted P5.
- Row 490 says "P5's statement rests on #1169 c.6854241002 and c.6863414487, not on the review".
  It names both authorizations, as P5 now does. Both edits are needed to keep the record consistent
  with change 4, and both are justified.

**Optional suggestion (Low).**
- r9's Revision sentence cites c.6863418087 as the authority for r9. That comment's item (b) reads
  "P0 was authorized at #1169 c.6854241002, and no other unit was".
- The P5 text departs from that reading, and the decision that departs from it is #1268
  c.6863753317. That decision is cited only in NOTES-r9, not in r9.
- r9 is accurate as it stands, because P5 rests on the two #1169 records. Citing c.6863753317 in r9
  would make the governance trail complete inside the record.
- **Exact change, if the owner wants it.**
  1. Append to r9:22, after "names the authorized units", the text: `, in the wording the owner
     chose at #1268 c.6863753317 (`amaybaum`, 2026-11-13T20:14:06Z)`.
  2. Add a §6 row after r9:489:
     `| #1268 c.6863753317 (owner decision on P5's wording, quoted with author and time) | revision line (header), r9 | Governance provenance, quoted. |`

  This is not required for acceptance.

### 5. Register and barred strings (no defect)

**Evidence.**
- The 37 added lines contain none of these phrases: "formerly", "no longer", "is now",
  "now settled", "current form", "corrected", "redefined", "withdrawn", "earlier revision",
  "should not", "reader".
- The only runs of four or more capitals are the file names RESPONSE, REVIEW, CONFIRM and NOTES, in
  code spans.
- Neither r9 nor NOTES-r9 contains a local path or scratch-area string.
- The rows use the established idiom of §6.

**Fix.** None.
