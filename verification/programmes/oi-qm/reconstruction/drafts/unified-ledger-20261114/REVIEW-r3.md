ACCEPT WITH CHANGES

# Independent review of LEDGER-r3 and RESPONSE-r2

This review is read-only, paper-only and non-author. `main` is `dfeec843`, and r3 was compared
against r2. No file was edited, no computation was run and nothing was posted.

The following are expected and are not findings:
- Level B is not exhaustive.
- The biological entries are unclassified.

The only exception is S6 below, which concerns a statement r3 makes itself.

Line references of the form "r3:n" are lines of `LEDGER-r3.md`.

## 1. Dispositions of REVIEW-r2

The diff against r2 shows that each finding was applied as proposed.

- **S1.** Applied at r3:216–220 and in M9. B-GR-7 records the failure as NEG.
- **N1.** Applied, citing `W1-1-REPORT-r4.md`:301–302.
- **N2.** Applied with the comment number and time (2026-11-14T13:13:09Z).
- **N3.** Applied: "on the two-valued carrier".
- **N4.** Applied: Q9 now leads with the recording question.

## 2. The owner's expansion conditions

Checked at source in #914 comments 6877871344 and 6877908458.

**Met:**
- Levels A, B and C are present.
- Negative results carry a NEG flag.
- No fifth part is created.
- The Part 4 entries are present: arrow of time, measurement, and the quantum–classical boundary.
- All seven SM subquestions are present: strong CP, hierarchy, flavour, neutrinos, baryogenesis,
  gauge dynamics and confinement, and nonperturbative effects.
- The QCD group carries all eleven obligations in the owner's order.
  - Pure Yang–Mills (B-QCD-6) is separate from confinement (B-QCD-5) and the hadron spectrum
    (B-QCD-8).
  - The group is linked to #1063, which is open and titled "LR-YM".
  - #1003 is cited as provenance only; it is a closed pull request.
  - Reproductions of known calculations are marked XC.
  - C-QCDVAC is cross-referenced to GR §6.2 (GR:579, 581).
- Level C contains predictions, phenomenology and scope limits.
- The SM lattice model is not taken as the common model (§1; Q13).

**Not met in full:**
- Two of the evidence-class conditions (S1 and S2 below).

## Should-fix

**S1. The DM class definition says DM results hold in any common model, but the recorded target allows a completed carrier.**
Location: r3:54–58.
Sources:
- #914 comment 6875046763: the target "cannot assume one fixed finite total carrier"; an infinite
  or completed carrier is admissible.
- r3's own Q5 and its QM–A1 entry.
- B-QM-16, which is "DM given A1".

r3 scopes DM to "every model of the bare finite class (finite S …), so that it holds in whichever
common model is later fixed". That transfer holds only if the common model is finite. A common
model on a completed carrier would need each finite-S result restated (Q5). As written, the class
reads as unconditional where it is conditional on finiteness.

Replace "so that it holds in whichever common model is later fixed." with:
"It holds in a common model only if that model is a member of the bare finite class. The recorded
target excludes one fixed finite total carrier (#914 comment 6875046763), so whether each DM result
transfers to an admitted carrier is open (Q5, Q13)."

**S2. Several entries carry no evidence class, although r3:53 says every entry carries one.**
Condition 3 of #914 comment 6877871344 requires a class for every entry. The entries without one
are listed below, each with a replacement from its own source.

- **B-SM-6** (r3:150). The class cell holds the support code "K". Replace it with
  "CD[cubic lattice, ledger (x)] for the decomposition; CD[H-spin′] for generations; NEG for the
  free-kernel and 4D-staggered routes".
- **B-SM-BARY-2** (r3:200). The class cell is prose. Replace it with
  "EF (downstream of the CP phases taken as solution-specific inputs, `book/ch19-open-problems.md`:184–188); UO in SM:1526". See S5.
- **C-PRED-1** and **C-PRED-4** (r3:322, :325). "Per row at source" gives the S/C/L/R/P/M/E
  labels, which belong to another scheme. Add the mapping: S rows → CD under the cubic commitment
  (B-SM-4), not DM; C, L and M rows → CD; R and E rows → EF; P rows → EF. Alternatively, split the
  rows (see N5).
- **C-PRED-5, C-PRED-7, C-PRED-8 and C-PRED-9** (r3:326–330), and **C-TOPO** and **C-ANOM**
  (r3:316, :321). Each describes a test or a scope limit but gives no class. Suggested classes:
  - C-PRED-5: CD[§7.3 split], as the test of B-COS-1 and B-COS-2.
  - C-PRED-7: CD[horizon conditions], with scope limit.
  - C-PRED-8: DM given A1.
  - C-PRED-9: UO.
  - C-TOPO: UO.
  - C-ANOM: CD[(E/M_Pl)² suppression, `papers/SM.md`:1448].

**S3. B-SM-3 omits the gauge group's carrier and lattice conditions.**
Location: r3:147.
Sources: `papers/SM.md`:374 (U(3)×U(2)×U(1) holds "under H-link + H-cust"); `papers/Substratum.md`:163
(amplitude-scale invariance, A6, and a specified charged matter action with anomaly cancellation);
B-SM-4 (the lattice is selected by the observed group).

Read alone, the row presents the gauge group as conditional only on the matter action. Replace the
class with:
"CD[H-link (single-copy), H-cust; amplitude-scale gauge invariance; A6; specified charged matter
action; anomaly cancellation]; the cubic-lattice commitment is EF (B-SM-4)".

**S4. B-P4-QCB-1 classes an identification as a derivation.**
Location: r3:299.
Sources: `book/ch18-beyond.md`:64, 72 ("the framework's identification applies"); `papers/Main.md`:97.

DM is correct for the two underlying results: representability is universal, and C4 ⟺ memory.
The claim that the quantum–classical boundary is drawn by the C1–C4 memory sector is the
framework's identification. Replace the class with:
"DM for the representability and memory results (B-QM-1, B-QM-2); PE for identifying the
quantum–classical boundary with the C1–C4 memory sector".

**S5. The baryogenesis support codes are wrong, and a paper/book disagreement is missing.**
Locations: r3:200–202, 220.
Sources: `papers/SM.md`:1526 (baryogenesis "mechanism is open", and the quantitative prediction
"is open work"); `papers/SM.md`:1496–1506 (sphaleron B + L violation in the emergent EFT);
`book/ch19-open-problems.md`:180–188.

The issues:
- B-SM-BARY-3 and B-SM-BARY-4 rest on ch19 only, so their support code is BK, not P.
- B-SM-NP-3 has paper support at SM:1496–1506, so its code is P, not BK.
- SM:1526 treats the quantitative baryon asymmetry as open work. ch19:184–188 reclassifies it as
  solution-specific and "not an unmet derivation obligation".

Add the disagreement as "D11. `papers/SM.md`:1526 states the baryogenesis mechanism and its
quantitative prediction as open work; `book/ch19-open-problems.md`:184–188 classes η_B as
solution-specific and not a derivation obligation." Cite SM:1526 in B-SM-BARY-2 and add D11 to
Q11.

**S6. r3's description of the appendix-a forward entries is wrong.**
Location: r3:332–334.
Source: `book/appendix-a-prediction-status.md`:145–158 and 168–196.

r3 calls B1–B14 and F1–F9 "biological entries" at :145–158 and :170–187. The actual grouping is:
- F1–F5: quantum engineering.
- F6–F8: cosmology. F6 is C-PRED-5, F7 is C-EARLY-2 and F8 is C-PRED-8.
- F9–F12: biology. F10–F12 are missing from r3's range.
- F13: boost-LV decoupling, at :196.

Replace with: "Appendix-a entries B1–B14 (:145–158; biology) and F1–F5 (quantum engineering),
F9–F12 (biology) and F13 (boost-LV) of §A.5 (:168–196) are Level C items not classified here.
F6, F7 and F8 are C-PRED-5, C-EARLY-2 and C-PRED-8. Their classification belongs to the coverage
audit."

## Nits

- **N1. B-QCD-11** (r3:239). The book source says "The mechanism is derived from the gauge
  structure of SU(3)" (ch10:88). The source asserts a derivation and does not propose one, so PE is
  the wrong class. Replace with "UO; the book asserts a derivation without support (D8)".
- **N2. B-QM-5** (r3:101). The converse `qm_generated_by_substratum_extension` is witnessed by the
  full implementation class (`fullClass`, `OIBridge/StructuralClosure.lean`). Add "(converse
  witnessed by the full class)".
- **N3. B-QM-13** (r3:109).
  - Theorem C holds "for every rule" (OA-2 STATUS:56–57), outside the affine hypotheses. Give it
    its own row, classed RR.
  - The claim cell omits OA-1 Gap 2, which its source cites.
- **N4. B-COS-3** (r3:256). CD without brackets does not name its hypotheses. Use
  "CD[Lemmas 1–3, C1–C4, Jacobson's Clausius relation, H-count via T_cl, geometry-first ordering]
  (D5)".
- **N5. Identifiers** (r3:72). The stated grammar, "A-*, B-<branch>-n and C-n", does not match the
  identifiers used: B-SM-CP-1, B-P4-AOT-1, B-QCD-n, C-QCDVAC, C-PRED-n. State it as "A-<name>;
  B-<branch>[-<group>]-n, with QCD as the branch-level group B-QCD; C-<group>[-n]". For the
  coverage audit, give aggregate rows sub-identifiers keyed to their source rows, for example
  C-PRED-1/12 for appendix-a row 12. The aggregates are C-PRED-1, C-PRED-4 and B-SM-FLAV-5.
- **N6. D7–D10** (r3:793–796). Cite the FULL mirrors (§A.14):
  - D7: FULL:5062.
  - D8: FULL:2894.
  - D9: FULL:5235.
  - D10: FULL:2886–2888.
  D10 can also note that baryon number is conserved at the substratum (SM:1486–1490); its
  violation is emergent (SM:1496–1506).
- **N7. §1** (r3:354–355). SM:60's list for the lattice model also includes site factorization
  (viii) and H-link. Add them.
- **N8. B-SM-FLAV-1 and B-SM-FLAV-3** (r3:181, 183) cite "§7.1–§7.2" and "§7.5" without line
  numbers. Give lines.

## 3. Status cells checked against their sources

The status cells match their sources, with the exceptions in S2–S5 and N1–N4. I found no witness
presented as a theorem, conditional presented as unconditional, or fit presented as prediction,
apart from S1, S3 and S4. In particular:

- **QCD cross-checks.** B-QCD-4 and B-QCD-7 (SM:607, 813, 1144) and B-SM-NP-1 are correctly XC.
  The measure identification is open in each.
- **Gauge sector.**
  - B-SM-GAUGE-2 is EF: δ₀ and (A, B) are fitted (SM:817).
  - B-SM-GAUGE-3 and B-SM-GAUGE-4 match SM:801–811.
  - B-SM-NP-2 matches SM:805.
- **Mass gap.** B-QCD-6 quotes Substratum:225 and SM:1448 exactly.
- **Higgs.** B-SM-HIER-1 is PE, and C-PRED-2 has "4–7 GeV above" (SM:1118, 1570).
- **Strong CP.** B-SM-CP-1 to B-SM-CP-3 match SM:667–671.
- **Neutrinos.** B-SM-NU-1 to B-SM-NU-3 match SM:1452–1468.
- **Arrow of time.** B-P4-AOT-1 to B-P4-AOT-5 match Substratum:56, 401–413. B-P4-AOT-3 quotes
  "not a prediction derived from the substratum" (:405).
- **Measurement.**
  - B-P4-MEAS-2 matches Main:690.
  - B-P4-MEAS-3 carries "the framework's proposal" (Main:688).
  - B-P4-MEAS-4 matches Substratum:465.
- **Observer selection.** C-OBS and B-P4-AOT-2 carry (EM) and τ_mix ≪ τ_S (Main:742–758).
- **Horizon count.** B-GR-1 correctly carries the horizon partition's GR causal-structure input
  (GR:40).

## 4. D7–D10, the four book passages

All four are confirmed at source.

- **D7.** ch18:256 says chirality is "derived from the staggered trace-out". The papers do not
  support that wording:
  - SM:543 certifies the minimal embedding as vector-like.
  - H-χ′ is open (SM:1320; ch19:328).
- **D8.** ch10:86–88 cites ch05 §5.4 for confinement. ch05 contains no occurrence of "confin" in
  any section. In SM:801–811 the Haar-measure confinement is an artifact, and the framework's
  measure is a conjecture.
- **D9.** ch19:88 says the lattice "eliminates the divergence". SM:613 and SM:1570 call the
  mechanism "structurally identified", with the theorem-level derivation deferred.
- **D10.** ch10:78–80 calls baryogenesis's possibility "a theorem". Its ingredients rest on:
  - Theorem 13's conditional chirality (SM:543);
  - H-spin′;
  - CP phases that are solution-specific inputs (Substratum:415).

## 5. Identifiers

The identifiers are stable and not reused, and every registry row has one. They can serve the
coverage audit once the grammar statement and the aggregate rows are fixed (N5). The D, M and Q
series keep the numbering of r2 (D3 is kept and reclassified).

## Checked by the reviewer

- **Ledger files.**
  - RESPONSE-r2, read in full.
  - r3 compared with r2 (`diff`); the registry at r3:53–334 read in full.
- **Owner records and Issues, through the API.**
  - #914 comments 6877871344 and 6877908458.
  - #1063: body and state.
  - #1003: state.
- **`papers/SM.md`.** Lines 60, 302–308, 489, 523–525, 603–613, 667, 671, 793–827, 1116–1118,
  1144, 1448, 1452–1468, 1486–1506, 1526 and 1570.
- **`papers/Substratum.md`.** Lines 56, 225, 401–415, 463 and 465.
- **`papers/Main.md`.** Lines 322, 682–692 and 742–758.
- **`papers/GR.md`.** Lines 577–581 and 739.
- **`book/` chapters.**
  - `ch10-chemistry.md`:76–88.
  - `ch05-gauge-structure.md`: its headings, and a search for "confin".
  - `ch18-beyond.md`:6, 34–36, 64, 72–80, 202, 218–222, 256, 268 and 274.
  - `ch19-open-problems.md`:88, 154–158, 162, 172, 180–188, 196, 208–210, 328, 343, 354 and 356.
- **`book/appendix-a-prediction-status.md`.** Lines 143–196.
- **Book mirrors.** FULL mirrors of D7–D10, by search.
- **Other records.** `verification/ROADMAP.md`:1525–1536, and the W1-1 report at :72–80.
- **Not done.** No Lean build, no script run, and no coverage audit.
