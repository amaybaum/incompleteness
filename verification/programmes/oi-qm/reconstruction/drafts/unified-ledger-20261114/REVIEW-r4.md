ACCEPT WITH CHANGES

# Independent review of LEDGER-r4 and RESPONSE-r3

This review is read-only, paper-only and non-author. `main` is `dfeec843`. No file was edited, no
computation was run and nothing was posted. The owner guidance, #914 comment 6878781541 (`amaybaum`,
2026-11-14T14:26:48Z), was read through the API. "r4:n" means a line of `LEDGER-r4.md`.

## 1. Dispositions of REVIEW-r3

All 21 row corrections were applied. A script compared every row identifier in r3 and r4:
- exactly the 26 rows RESPONSE-r3 lists changed;
- no other row changed;
- no identifier was removed;
- 51 identifiers are new: 45 marked "(audit)", 5 marked "(r4)", and B-QM-28.

The two findings applied in modified form:

- **S6.** The modification is sound, and my finding was wrong on one point. Appendix-a §A.5 has
  rows F1–F4 and F6–F13 and no row F5 (`book/appendix-a-prediction-status.md`:170–173, 179–181,
  187–190, 196; F5 does not occur anywhere in the file).
  The 64-row mapping beneath §L.C is correct:
  - 23 numbered rows;
  - 7 N rows;
  - 8 G rows;
  - 14 B rows;
  - 12 F rows.
- **N3.** The modification is sound. "Classed RR" in my review was ill-formed, because RR is a
  support code. B-QM-28 is DM with support RR, scoped to "every rule, at a fixed finite carrier"
  (OA-2 STATUS:56–57). That matches the source, and the support code shows that the result is not
  established.

The other findings were applied as proposed:
- S1 to S5, including D11.
- N1 and N2. The converse is cited at `StructuralClosure.lean`:419–429.
- N4 to N8.

## 2. The coverage-audit findings

- **Which record.** r4 carries the findings in their confirmed forms. COVERAGE-AUDIT-r4 differs
  from r3 only in its header, the unresolved count (9 → 10, adding F-37), the SM-35 note, one §6
  location and the §9 row. REVIEW-AUDIT-r4 confirms this (ACCEPT). The confirmed content r4 uses is
  therefore the same. But r4 cites the wrong record: see S4.
- **Only confirmed findings.** The checks:
  - F-10 is kept as withdrawn.
  - Every F, K and §3.2 item in §F names the audit's conflict class.
  - No finding is resolved by narration. U-1 stays unresolved although Structure rows were added,
    and r4 says explicitly that adding a covering row does not resolve a finding (r4:1028–1029).
- **All 10 unresolved findings.** U-1 to U-10 are listed with passage A, passage B, the proof's
  scope and what is open. I checked the passages of U-2, U-3, U-4, U-7, U-8 and U-9 at source
  (Structure:733; Main:147–151; SM:801, 1448; Substratum:225; SM:936, 940, 944; SM:1152, 1215;
  SM:1076, 1108; ch19:244). U-10's passage B is weaker (N7).
- **New rows.** I checked all five "(r4)" rows and 24 "(audit)" rows at source.
  - B-GR-12 (GR:104): correct, apart from one missing hypothesis (N2).
  - B-SM-17 (SM:418–426), B-STR-4 (Structure:829–862, 998–1012, where the protocol is stated and
    "Executing it requires …"), C-STR-6 (Structure:813 against SM:1396, 1440) and C-EARLY-6
    (ch18:56–58): correct.
  - The 24 audit rows checked:
    - B-QM-17, B-QM-18, B-QM-21, B-QM-22, B-QM-23, B-QM-26 and B-QM-27;
    - B-GR-10, at GR:615, which labels part (a) "Unconditional";
    - B-SM-FLAV-6, B-SM-FLAV-7, B-SM-FLAV-9 and B-SM-FLAV-10, including the quotes at SM:1112,
      1108 and 936;
    - B-BH-8 (GR:755–767) and B-SUB-1 (Substratum:231–235);
    - B-STR-1, B-STR-2 and B-STR-3 (Structure:13, 656–660, 1028–1042);
    - B-BELL-9 (ch18:104);
    - C-PRED-10, C-PRED-11 and C-PRED-12 (GR:512, 524, 528–530);
    - C-ERP (Substratum:237–243), C-STR-1 (Structure:733) and C-STR-3 (Structure:453).

    Classes and quotes match the sources, apart from N1 and N6.
- **Corrected rows.** I checked 12 at source:
  - B-QM-5;
  - B-SM-3;
  - B-SM-6 (SM:448);
  - B-SM-FLAV-1 (SM:1279, for F-25);
  - B-SM-FLAV-3 (SM:1215, "empirical fitting on a moderately-restricted set");
  - B-SM-BARY-2, B-SM-BARY-3 and B-SM-BARY-4 (SM:1526; ch19:180–188);
  - B-SM-NP-3 (SM:1496–1506);
  - B-QCD-6 and B-SM-GAUGE-3 (SM:801, 1448);
  - B-SM-NU-2 (GR:410).
- **Paired passages.** I spot-checked F-21 (SM:567), F-31 (ch19:106) and F-18 (Structure:417) at
  their paired passages; each reads as the register states.
- **T-6.** It is stated as uncovered, in §F ("Missing coverage still outstanding") and in U-1.

## 3. The owner guidance (#914 comment 6878781541)

- **MC, LC and RO.** They are three separate columns in every §F table. The J and M findings are
  RO only. Every MC entry, D7–D11 included, is a candidate, and the manuscript passage is unchanged
  (r4:884–885; the §F preamble).
- **No ranking.** The header and the close of §U state that the ledger ranks nothing. The QCD rows
  change only where classes were corrected (B-QCD-6, B-QCD-11), and no section is reordered.
- **No common model.** §1, the DM definition and Q13 keep this, with one stale sentence in Q13
  (S2).

## Should-fix

**S1. Level A cross-reference ranges are stale.**
Location: r4:117–120.

The "What exists" ranges stop at the r3 row counts:
- A-QM gives "B-QM-1 to B-QM-16"; the rows now run to B-QM-28.
- A-BELL gives "B-BELL-1 to B-BELL-8"; B-BELL-9 exists.
- A-GR gives "B-GR-1 to B-GR-9"; B-GR-10 to B-GR-12 exist.

This is the stale-count hazard named in the lessons register. Replace the ranges with "B-QM-1 to
B-QM-28", "B-BELL-1 to B-BELL-9" and "B-GR-1 to B-GR-12". Add B-SUB-1 and B-SUB-2 to A-QM and
A-REAL, since they state Substratum's reconstruction and invariance results.

**S2. Q13 contradicts the revised DM definition.**
Location: §12, Q13.

Q13 still ends "The registry's DM class is scoped so that it does not depend on the answer". The
revised definition (r4:67–74) says the opposite: whether a DM result transfers depends on whether
the common model lies in the bare finite class (Q5, Q13). Q13 also still says "items (vii) and
(ix)–(xiii)", while §1 now gives "(vii)–(xiii) … and H-link".

Replace the last sentence with: "Whether each DM result holds in the answer depends on whether that
model is a member of the bare finite class (§L evidence classes; Q5)." Replace "§1, items (vii) and
(ix)–(xiii)" with "§1, items (vii)–(xiii) and H-link".

**S3. J-3 and J-4 drop the conditions of their conflicts.**
Location: §F.5.

§9 states both conflicts under the factorization interface of `papers/Main.md`:558, whose
unboundedness is imported. §9 also marks QM–BH undetermined on a completion. The register says only
"known not to, as stated". Read alone, the register states the conflicts without their conditions.

Replace the status of J-3 with "known not to, on one fixed finite carrier, under the factorization
interface of Main:558 (unboundedness imported)". Replace the status of J-4 with "known not to, on one
fixed finite S under that interface; undetermined on a completion".

**S4. r4 cites the audit version that was not accepted.**
Locations: the header (r4:3–6), the §F preamble, §U U-1 and §13.

r4 names `COVERAGE-AUDIT-r3.md`, "as confirmed by" REVIEW-AUDIT-r1 to r3. The accepted record is
`COVERAGE-AUDIT-r4.md`, accepted by `REVIEW-AUDIT-r4.md` (ACCEPT). REVIEW-AUDIT-r3 was ACCEPT WITH
CHANGES, and U-8 (F-37) comes from the r4 correction.

Cite `COVERAGE-AUDIT-r4.md` as accepted by `REVIEW-AUDIT-r4.md`, with r3 and REVIEW-AUDIT-r1 to r3
as its history. Add both files to §13 as provenance.

## Nits

- **N1. B-QM-22.** The support code is P, but Main:590 cites kernel results:
  `complete_passive_iff_commutative`, `central_classification` and
  `no_complete_passive_observation`. Use K.
- **N2. B-GR-12.** GR:104's consistency also uses "the minimal-coupling factorization δ = 1". Make
  the class "CD[H-link; minimal-coupling factorization δ = 1]".
- **N3. B-QCD-9 and B-QCD-10.** Their class cells are cross-references only. The header says every
  entry carries a class, so write "class per the cross-referenced rows".
- **N4. §5.1.** "2 S, 5 C" is quoted without pointing to the confirmed label findings F-6, F-25 and
  F-35. Add "(see C-PRED-1 sub-rows; F-6, F-25, F-35)".
- **N5. C-EARLY-6.** It records late-time corrections under the EARLY group. Identifiers are stable
  and need not change; a group note would avoid misreading.
- **N6. B-STR-2.** The source calls its conclusions "preliminary" (Structure:1030). Carry the word.
- **N7. U-10.** Passage B is the audit's observation, not a source passage. State that the paired
  companion passage is to be fixed by the trace.

## 4. Standing rules and new errors

- **Inclusion and derivation.** No inclusion reads as a derivation. The new PE rows carry their
  source's proposal wording: C-STR-1 to C-STR-5, C-ERP, B-SUB-3, C-QG-1 and C-BIO.
- **Fits and imports.** These are classed as EF, XC or imported, not as predictions:
  - B-SM-FLAV-3 (K = 1/2);
  - B-SM-FLAV-9 (2/9);
  - C-PRED-12 (the Ω_CDM input; the reproduction is XC);
  - B-SM-FLAV-7 (m_t a retrodiction).
- **One-direction results.** These are kept as one direction:
  - B-SUB-1: the displayed bidirectional correspondence, with the converse UO (§A.34).
  - B-GR-10: part (a)'s "Unconditional", classed CD[S1–S4].
- **Errors found.** The only conditional-to-unconditional errors are S2 and S3. I found no witness
  presented as a theorem and no fit presented as a prediction.
- **Sources and identifiers.** Every status cell sampled cites a source line on `main`. Identifiers
  are stable and follow the stated grammar, with sub-identifiers for the aggregate rows.

## Checked by the reviewer

- **Ledger and audit files.** RESPONSE-r3, read in full. REVIEW-AUDIT-r4 and RESPONSE-AUDIT-r3. The
  diff of COVERAGE-AUDIT-r3 against r4.
- **LEDGER-r4.** Lines 1–440 and 875–1063 in full. The diff of §0–§10 against r3, which shows only
  the §1 and preamble changes. A script comparison of every row in r3 and r4.
- **Owner record.** #914 comment 6878781541, through the API.
- **`papers/Main.md`.** Lines 76, 147–151, 159, 478, 496, 590–592, 620–622, 638, 660 and 674.
- **`papers/GR.md`.** Lines 104, 512, 524, 528–530, 587, 609, 615 and 753–767.
- **`papers/SM.md`.** Lines 418–426, 448, 567, 936–944, 1006–1008, 1076, 1108, 1112, 1215, 1279,
  1396, 1440 and 1448.
- **`papers/Substratum.md`.** Lines 231–243.
- **`papers/Structure.md`.** Lines 13, 120–122, 417, 453, 656–660, 733, 813, 829–834, 998–1012 and
  1028–1042.
- **`book/` chapters.** `ch18-beyond.md`:56–58 and 104; `ch19-open-problems.md`:106 and 244.
- **`book/appendix-a-prediction-status.md`.** Lines 70, 131 and 168–198, plus a search for "F5".
- **Not done.** No Lean build, no script run on OI rules, and no re-audit.
