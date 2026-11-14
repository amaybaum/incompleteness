ACCEPT WITH CHANGES
1. Coverage boundary: NOT MET. The appendix-a rows and the eight intermediate findings meet it, but the SM §7 sample is not adequate. It skips the Cond 2 block (SM:1062–1112), on which r2's own PMNS findings rest, and so misses a negative result stated in lines it did read (SM:1026) and an overstatement at SM:1110 (S1).
2. Counting: MET. C and CB are reported separately, and both cross-tabulations reconcile with the tables and with appendix-a rows that the reviewer recounted.
3. Contradictions: MET. Every conflict is classed and has paired passages, and the nine unresolved items are named. The status term "resolved as stated" needs a definition, and the scope line is explicit in 11 of 36 entries (S3).

# Independent review of COVERAGE-AUDIT-r2 and RESPONSE-AUDIT-r1

This review is read-only, paper-only and non-author. Papers and book chapters were read from `main` at
`dfeec843`. Both files were confirmed byte-identical to their copies on PR #1292 at `70748aad`. No file
other than this review was written, no computation was run and nothing was posted.

References of the form "A2:n" are lines of `COVERAGE-AUDIT-r2.md`, and "R:n" lines of
`RESPONSE-AUDIT-r1.md`. Paper and book references are physical lines at `dfeec843`.

## Dispositions of REVIEW-AUDIT-r1

Every item was checked against r2.
- **Applied as proposed:** S1, S3–S7, S9, S10 and N1–N9.
- **Corrected against this reviewer:** the N7 citation. The response is right that the line is
  appendix-a:135, not :133.

The two items applied in modified form are accepted.
- **S2: SM:1464 against :1468, recorded as a difference in assumptions.** SM:1464 relates the overall
  scale to the splittings under a hierarchy heuristic, and the splittings are measured inputs. SM:1468
  concerns the derivation of the absolute scale. The two can both hold. This review's r1 phrase "real
  internal tension" overstated the case. F-7 keeps the O flag for GR:410, which is the part that needed
  it.
- **S8: B-SM-FLAV-8 classed PE.** The claim being classified is SM:1339's explanatory one ("strong
  evidence for the underlying C₂/d identity"), and none of the table's values is fitted. One addition:
  the 1/d normalization behind that identity is selected by match (F-26), and B-SM-FLAV-9 records it as
  EF. Cross-reference B-SM-FLAV-9 from B-SM-FLAV-8.

## Should-fix

**S1. The SM §7 sample omits the Cond 2 block and misses a negative result and an overstatement.**
(A2:883–905; point 1)

SM:1062–1112 is read only "at heading or status level" (A2:890). Yet that block carries the derivation
behind F-8, F-27, F-28 and B-SM-FLAV-6. It contains two items the audit does not record.

- **A negative result missing from the ledger and from r2** (condition 3).
  - SM:1108: "the substrate dressing chain is retired"; "The second-order route is thereby closed in the
    negative"; "the geometric second-order route is excluded by monomial orthogonality".
  - The same exclusion is stated at SM:1026, which lies inside the range r2 read in full ("excluded the
    second-order route — demoting it to Layer 2(b)").
  - It is stated again at SM:1076 and :1084, and in appendix-a footnote ᶠ (:96).
  - r3 records it nowhere: no row cites SM:1026–1112.

  Add a proposed row, for example in B-SM-FLAV-6 or as its own entry: "second-order substrate route to
  Cond 2 excluded (monomial orthogonality); one O(λ³) route recorded, not pursued". Its class is NEG,
  with P support, and the work label is LC.

- **An unsupported intermediate inference.** SM:1110 reads the sum-rule match as indicating "that the
  substrate-level mechanism producing the 4(d−1)/(2d) amplitude ratio is realized in the bijection".
  - SM:1108 has just excluded the mechanisms it examined and leaves Cond 2 "a stated condition".
  - The match is a retrodiction (SM:1349).
  - Record this as a single-source overstatement, with work label MC.

Reading the roughly 50 lines of SM:1062–1112 closes point 1. In the remaining unread §7.5 lines
(SM:1162–1205), the reviewer found only material already covered by F-30, for example the closure claim at
SM:1196.

**S2. §7's S/C/L mapping misstates REVIEW-r3 S2.** (A2:915)

r2 says the labels "map as REVIEW-r3 S2 proposes: S → EF (lattice selected by the observed group)". But
REVIEW-r3 S2 maps "S rows → CD under the cubic commitment (B-SM-4), not DM", and EF is reserved for R, E
and P rows. Under r2's mapping, every S row (Wolfenstein A, λ(M_Pl) = 0) would be read as empirically
fitted, which would misstate the status of rows the audit does not reclassify.

Change the S mapping to "S → CD[cubic commitment, B-SM-4 (EF)]". No proposed row currently uses the S
mapping, so only this line changes.

**S3. Status and scope wording in the register.** (A2:140, §3.1; point 3)

- **"Resolved as stated".** This status appears on 28 findings and is not defined. On 10 of them it sits
  under a direct contradiction that is still in the manuscript: F-3, F-17, F-18, F-21, F-24, F-31 to F-34
  and F-36. A
  reader can take it to mean the conflict is resolved, which is exactly the "silently resolving" that
  condition 6 forbids. Define it in §1, for example: "classified; finding stands; correction not made
  (see Work)". Alternatively, rename it to "classified".
- **"Unresolved findings: 9 (§3, status column)" (A2:140).** The count is right, but two of the nine are
  K-9 (§8) and the Main-independence observation (after §4.5). Point to §3, §4.5 and §8, as §10 already
  does.
- **The proof's actual scope.** The guidance asks each finding for this. An explicit "Scope" line appears
  in F-2 to F-8 and F-24, F-25 and F-30, which is 11 of 36. In most of the rest, passage B is itself the
  proof's own scope statement: for example SM:448 (F-21), SM:468 (F-32), SM:458 (F-31) and SM:1396
  (F-18). Say so once in §3's preamble, or add the line. Findings with no proof involved (F-1, F-9,
  F-10, F-29) can say "not applicable".

## Nits

- **N1. F-34 and B3.** The twelve S-labelled biology rows include B3 (ch13 §13.6). Chapter 13 carries no
  "conjectural extension" notice (ch13:1–8). The conjecture at ch13:140 concerns distinguishability
  revival (§13.7), not B3's non-Markovian enzyme kinetics. The ch16:6 and ch17:6 anchors cover eleven
  rows: B1, B2 and B6–B14. Either give B3 its own anchor or move it out of F-34. The 17-row count in §2
  (A2:136) follows whichever is chosen.
- **N2. B-SM-FLAV-6 and F-8: the sum rule does not need b₂₃ = 1.** SM:1026 and :1066–1068 make the sum
  rule equivalent to Cond 2 alone. The normalization b₂₃ = 1 (SM:1048) fixes θ₁₂ and θ₂₃ individually.
  Write "CD[Cond 2] for the sum rule; CD[Cond 2; b₂₃ = 1] for θ₁₂ and θ₂₃" (A2:966), and correct
  F-8's "the sum rule and θ₂₃ rest on Cond 2 … and on the normalization choice".
- **N3. F-16's list of other equivalence displays is incomplete.** The list omits:
  - GR:222, the boxed "(i)–(v) ⟺ finite operational QM", which is B-QM-3;
  - GR:236, the boxed "OI⁺ ⟺ …", which is B-QM-6;
  - Main:586, a display of the same equivalence;
  - Main:617, "accessible non-Markovianity ⟺ a per-horizon … realization exists".

  The text is also silent on SM and Structure, which contain no displayed equivalence, though SM has
  inline theorem biconditionals such as Theorems 3 and 16 that ledger rows already carry. None of this
  changes S-24.
- **N4. F-17.** Add Structure:191 ("[SM]: Level D × Levels G1–G2"). It conflicts with :179's placement of
  Cabibbo and Koide at G3 × D in the same way that :192 conflicts over the dark sector.
- **N5. F-26 and §6.** F-26 quotes SM:936 ("Only 2/9 matches"), which §6 lists as read only at heading
  level (:921–936). Adjust the read list to say that :936 was read.
- **N6. The owner guidance record.** r2's expanded scope, the appendix-a row audit and the §6 sample rest on
  guidance that is only paraphrased (A2:25–35; R:10–11). Before acceptance, quote it with author and time
  once the coordinating session supplies the record (§A.42 item 7).

## Checks requested

- **At least 15 new or changed entries, at source.** Twenty-four were checked:
  - F-2 (Main:147–151; Structure:717, :733; ch03:26), F-3 (SM:448, :468, :543; Substratum:161, :201,
    :203), F-5 (Substratum:506, :513–514), F-6 (SM:1116, :1293; appendix-a:28, :91), F-7 (SM:1456–1468;
    appendix-a:87, :112, :130), F-8 (SM:1026, :1048, :1290–1291, :1353, :1360);
  - F-9 (SM:1118, :1126, :1294), F-14 (GR:524–532), F-16 (Substratum:112, :127, :231–233; Main:97,
    :586, :617, :628; GR:222–274), F-17 (Structure:179, :191–192), F-18 (Structure:417; SM:1396), F-19
    (Structure:403, :1317; SM:1452);
  - F-22 (SM:801, :1448), F-23 (SM:887, :971, :989, :1215), F-24 (SM:863, :887), F-25 (SM:865, :871,
    :881, :1279), F-26 (SM:936, :940, :944), F-27 (SM:1026, :1034, :1036);
  - F-28 (SM:1048, :1056; appendix-a:96), F-29 (SM:981, :1289, :1335; appendix-a:86), F-30 (SM:1152,
    :1160, :1215, :1219), F-34 (appendix-a:28, :145–158; ch13:1–8, :138–140; ch16:6; ch17:6, :170–174),
    F-35 (appendix-a:70; SM:793), F-36 (appendix-a:131, :135).

  All are accurately quoted and located. The exceptions are N1–N5.
- **Classification.** Every class checked is right as given, apart from N1. This includes:
  - the direct contradictions F-17, F-18, F-21, F-24, F-31, F-32 and F-33, and the C1 clause of F-2;
  - the differences in assumptions F-3 (generations, Higgs), F-6, F-25 and F-35;
  - the differences in scope F-4, F-5, F-11 and F-12;
  - the manuscript-revision differences F-9 and F-29.

  F-27 is a real finding: SM:1036 uses the sin²θ₁₃ coefficient as one of the constraints that determine
  A₁, while SM:1034 derives that coefficient from α.
- **Counts.** The five tables give 154 claims: 50 C, 30 CB, 23 CM and 51 U, with O = 36 and T = 13. They
  reproduce every cell of A2:105–124. The O cross-tabulation (0/2/20/14), the T cross-tabulation
  (4/1/1/7) and the O-and-T counts (six U) match. On appendix-a, 64 rows = 23 + 8 + 7 + 14 + 4 + 3 + 4 + 1;
  40 have a ledger row and 24 do not; the class and placement findings number 17 and the T rows number 6,
  all as stated. The r1 to r2 count changes (R:56–79) reconcile entry by entry.
- **Work labels.** Every F-entry carries a Work line (MC, LC or RO; F-10 "none"), as does every U and CM
  table entry and every K-entry.
- **No ranking or promotion.** r2 removes r1's "most important findings" list, states that it ranks no
  branch (A2:39, :911), and contains no comparative or priority language about branches. Its proposals do
  not promote: they apply CD where r1 had DM (S7), and their only remaining misstatement (S2) runs the
  other way.
- **Not done.** No Lean or census check, no script run, and no reading of the book chapters 13–17 beyond
  the lines listed.
