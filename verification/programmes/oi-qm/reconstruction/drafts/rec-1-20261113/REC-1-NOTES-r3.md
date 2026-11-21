# REC-1 notes (r3): items not located, not read, or not resolved

Companion to REC-1 r3. Sources read are pinned there (`main` `c3b5f37a`; off-main
`8228b3c2` and `77226128`).

## Located, with a caveat

- **"#1139 records".** Located as `verification/programmes/oi-qm/reconstruction/bsel-2-q2a-ce-20261105/`
  (PREREG.md, RESULT.md), merged by `c987b890` ("Merge pull request #1139 …"). The GitHub API reports
  #1139 as `closed`; the merge commit is an ancestor of `c3b5f37a`. Only RESULT.md was read.
- **MECH-1, MECH-2.** `mechanism-1-20261107/DESIGN.md` (merge `1287748d`, #1191) and
  `mechanism-2-20261108/DESIGN.md` (merge `9facdf03`, #1195). Read: result sections, outcome, the
  theorem statements cited; proofs not re-read.
- **TUNE-1 Step 2.** On `main` (merge `c03a5764`, #1237). Only Sessions 3 and 4 were read, at the cited
  lines; for r2 also S3:100–110 (Node L5.1), S3:196–212 (Node L5.4) and the proposal's P:143–146
  (H-μ). The rest of the proposal and the amendment files (`AF:` in Step 3A) were not read directly.
- **Scope wording.** c.6848080209 lists OA-1/OA-2/OA-3/W1-1 as off `main`; they are on `main` at
  `c3b5f37a` (#1265), as c.6850732002 records. REC-1 treats them as [R] on `main`.
- **#1214.** Head `77226128` fetched by branch name `research/oicore1-record-20261109`; only
  `OICORE-1.md` was read (§0, §2, §3.1, §3.3, §4, §5, §8.5–8.6). Its `review/` files were not read.

## Not read

- `papers/SM.md` directly (SM:104, :112 enter only through OA-3 and Step 3A quotations).
- apparatus-1, obsmu, minacc-1, mathcon1-polc, ARP-1-MARC, operational-quotient v3, the M-2 record
  (`oiqmsel-m2-cpers-20261105`), and the Q2A and M-1 preregistrations. They enter only through the
  records that cite them, with those records' labels.
- `TUNE-1-STEP3A-REVIEW.md` beyond its blob id; Step 3A r1/r2.
- Lean proofs. Only theorem names and their line positions were read
  (`Equivalence.lean:245, :294, :422, :462`; `GeneralCarrier.lean:93, :100, :160`;
  `PhysicalCharacterization.lean:301`; `StructuralClosure.lean:348`; `RankGapTheory.lean:702`). The
  configuration-level ceiling lines are cited through OA1:408–422, not re-read one by one.
- #1169 comments before 2026-11-12; #1236 comments other than c.6847314661.

## Not resolved

1. **MP-0b's standing.** OA-1 lists it among missing premises as an "interface convention"
   (OA1:563–564); Step 3A r3 types the same record convention as "imported" (3A:501). REC-1 marks it
   undetermined (C6) and does not choose.
2. **Herald typing** (held at use vs ensemble conditioning) is an open interface premise in OA-3
   (OA3:124–128, :628). REC-1 §3.2 and OBL-SP fix held-at-use typing as a hypothesis; neither settles it.
3. **REC-1 §3.2** is an unreviewed reading [W, REC-1] of OA-1 D2 and D4. Its partial-record case rests
   on D8, which OA-1 marks as an unreviewed candidate.
4. **Row 5 and C14.** Row 5 is classified Q1-D + Q1-I + Q1-μ: Main:558 names its factorization
   interface as assumed, and the factorization needs the ontic law of a preparation to be independent
   of the measurement choice, which inclusion does not supply. Whether Main:558's extension to finite
   shared coordination ([55]) covers every embedded correlation is not checked. C14 carries a REC-1
   hand reading (the causal cone bounds influence as well as access), not checked by a reviewer.
5. **OBL-SP instances.** Whether faithful records can be formed inside `S` under R-lin for laws in
   `D_0` (OA-1 gap 1: writes are masked by neighbours unless known or isolated, OA1:522) is part of the
   obligation, not checked here.
6. **Q2-F versus Q2-A for rows 6, 17, 20, 42.** Classified Q2-F, each with the map's standing stated
   (designed map, or proposal rule). For every definable finite target some designed map reaches it (Main:580–582), so
   Q2-F for a designed map differs from Q2-A only by the stated standing; 3A:295–297 reads row 6 as definable only.
   None is Q2-P.
7. **P0 is not carried out.** OBL-SP's first step (§4) is stated with its pass and fail conditions
   only. S3:206–207 [R] and the r1 review's unreviewed sketch point to O-C for the unheralded and
   same-length-heralded fragment; neither is used as a result.
8. **Herald typing in OBL-SP's residual.** If P0 passes on its main fragment, the residual depends
   on which heralds are available under held-at-use typing with records formed inside `S` (C6, C7),
   which the stated premises do not fix (OA3:474–475: "Under held-at-use herald typing that class
   is itself retention-type").
9. **Review.** The process in c.6850732002 requires a fresh non-author review, then ChatGPT review at
   the exact head of a draft PR linked to #1169, #1143 and #1236. The draft is on PR #1268; this
   revision answers the r1 review.
