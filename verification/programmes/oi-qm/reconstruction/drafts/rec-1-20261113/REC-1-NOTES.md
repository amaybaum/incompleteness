# REC-1 notes: items not located, not read, or not resolved

Companion to `REC-1.md` in this directory. Sources read are pinned there (`main` `c3b5f37a`; off-main
`8228b3c2` and `77226128`).

## Located, with a caveat

- **"#1139 records".** Located as `verification/programmes/oi-qm/reconstruction/bsel-2-q2a-ce-20261105/`
  (PREREG.md, RESULT.md), merged by `c987b890` ("Merge pull request #1139 …"). The GitHub API reports
  #1139 as `closed`; the merge commit is an ancestor of `c3b5f37a`. Only RESULT.md was read.
- **MECH-1, MECH-2.** `mechanism-1-20261107/DESIGN.md` (merge `1287748d`, #1191) and
  `mechanism-2-20261108/DESIGN.md` (merge `9facdf03`, #1195). Read: result sections, outcome, the
  theorem statements cited; proofs not re-read.
- **TUNE-1 Step 2.** On `main` (merge `c03a5764`, #1237). Only Sessions 3 and 4 were read, at the cited
  lines. The proposal and amendment files (`P:`, `AF:` in Step 3A) were not read directly; REC-1 cites
  none of their lines.
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
4. **Row 5 and C14** carry REC-1 readings (factorization through the finite ontic state for every
   embedded interface; the causal cone bounding influence as well as access). Both are hand readings,
   not checked by a reviewer.
5. **OBL-SP instances.** Whether faithful records can be formed inside `S` under R-lin for laws in
   `D_0` (OA-1 gap 1: writes are masked by neighbours unless known or isolated, OA1:522) is part of the
   obligation, not checked here.
6. **Q2-F versus Q2-P for rows 6, 17, 20, 42.** Classified Q2-F because each uses one fixed map from
   stated initial conditions; none has a sourced map and boundary condition, so none is Q2-P. Whether a
   reviewer reads the designed maps of rows 6 and 20 as Q2-A instead is open.
7. **Review.** REC-1 has had no independent review. The process in c.6850732002 requires a fresh
   non-author review, then ChatGPT review at the exact head of a draft PR linked to #1169, #1143 and
   #1236. Nothing has been committed, pushed or posted.
