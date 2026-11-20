# TUNE-1 Step 3A r3: preservation note

This note covers `TUNE-1-STEP3A-r3.md` and `TUNE-1-STEP3A-REVIEW.md` in this directory and no other
file here. Both are byte-identical copies from draft PR #1267 (branch
`research/tune1-step3a-1236-20261113`, head `8228b3c24e17a17f324b6779b53b04ad296b4308`). They are
preserved because records on `main` use r3 as support (§A.42 items 2 and 8). Preservation establishes
no claim of r3 (§A.46 item 1) and changes no scientific status.

Authority: owner decision of 2026-11-20 (`amaybaum`, #1169 comment 7029588625, item 4): "#1267 ...
land each through narrowly scoped preservation PRs, each with its own independent check." Accountable
Issue: #1236.

## Files

| File | Blob at `8228b3c2` | SHA-256 | Lines |
| --- | --- | --- | --- |
| `TUNE-1-STEP3A-r3.md` | `7bbec04d7bee91673c3241e78a289bba28fb1ea5` | `8b44fe4f9ca2e31a1dfec5a8c485eb1547e8ccd4961c7f79cb614d886d89b385` | 1157 |
| `TUNE-1-STEP3A-REVIEW.md` | `49a5d52a65817d07b24a2dfb114671ab19bde6e0` | `3401e3fae1bf8027e9997f5addae99cee68c2f451ffe88a71f0b2282f41fb83b` | 797 |

`git hash-object` on each file reproduces its blob.

## Citations on `main` that use r3

`native-apparatus-source-20261113/support/tune-confirmed/TUNE-1-SOURCING-r2.md` and its
`tune-published` copy, lines 83, 429 and 434, cite `drafts/tune-1-20261111/TUNE-1-STEP3A-r3.md`, blob
`7bbec04d`. That path and blob are this directory's r3. The uses those rows classify as support off
`main` (candidate A's name, the formulation of statement (i), and "no member is exhibited", 3A:896–905)
are support on `main` at that path. `selection-discriminator-20261113/support/synthesis/SYNTHESIS-r3.md`,
lines 141 and 735, also uses r3 through TS (MM-1a, through TC-A, "support off `main` through TS");
that use resolves on `main` through the same path. The two TS r2 copies are kept unedited, because `RETENTION.json` and
`ARTIFACTS.sha256` there pin their bytes; the trace is recorded in that directory's `RETENTION.md`.

## Review and status

- `TUNE-1-STEP3A-REVIEW.md` holds the internal review trail: review of r1, ACCEPT WITH CHANGES; recheck
  of r2, ACCEPT; review of r3 (§2A), ACCEPT WITH CHANGES; confirmation of r3, ACCEPT. Its reviewer is
  named only as "Independent internal review (same model family)" (REVIEW:6).
- The internal review of r3 and its confirmation checked a session working copy, not the landed
  file. The landed r3 differs from that copy only at line 1068, and the landed review file differs
  from its reviewed copy only at lines 3, 396, 403, 508 and 527: on those lines the name of the
  session's temporary working directory is replaced by the word `working`, and no other byte
  differs. Restoring the directory name reproduces the reviewed copies, whose SHA-256 values are
  `5f38206485a733049f288d7891dae23fa5f3b1e2f1116bfeb23abc6a0c6ea315` (r3) and
  `28029777fabbb211e85b8374a6684bda38fd92a9356e9b948d8c5e2fcbe2ccd0` (review), as recorded in
  `TUNE-1-STEP3A-OBJECTS.md` on #1267's branch. The ChatGPT review below covers the landed r3 blob
  itself.
- ChatGPT review 5887947616 on #1267 (posted under `amaybaum`, 2026-11-13T08:08:27Z) at `8228b3c2`,
  covering the committed r3 blob: "ACCEPT WITH SCOPE QUALIFICATIONS". It states that "no exhibited
  candidate includes a fully specified family, preparation and concrete readout interface, so none
  qualifies for Step 3B. That is a specification gap, not a failure or no-go for all deterministic
  substrata."
- All reviews are model reviews: evidence of review, not independent mathematical verification. r3's
  results are paper derivations and readings on Step 2 records; none is independently verified.
- r3's header (lines 3–14) records its writer-stage standing ("awaiting confirmation", "nothing
  committed"); the confirmation of r3 in the review file is ACCEPT, and the record is committed at
  `8228b3c2`.
- Remediation: the candidate-specification gap (no member of any INCONCLUSIVE class is exhibited)
  remains open under #1236. This note authorizes no work.

## Not landed

r1 (`TUNE-1-STEP3A.md`), r2 (`TUNE-1-STEP3A-r2.md`) and `TUNE-1-STEP3A-OBJECTS.md` remain on #1267's
branch. No record on `main` uses them. The review file and r3 cite lines of r1 and r2 as review
history; those citations are provenance here. `TUNE-1-STEP3A-OBJECTS.md` names five reviewed
working-copy blobs by full id, none of which exists in the repository (§A.42 item 3), so it is not
copied without an owner decision on those ids.
