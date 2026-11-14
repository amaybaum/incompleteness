# Response to REVIEW-r3 and the confirmed coverage-audit findings (ledger r4)

Paper-only, under #914 comments 6877420015, 6877871344, 6877908458 and 6878781541. No repository file
was edited, no computation was run on OI rules and nothing was posted. Sources were read on `main` at
`dfeec843`, re-fetched when r4 was written. `LEDGER-r3.md` and `REVIEW-r3.md` are unchanged: their
SHA-256 digests begin `d8cad733` and `71f6c421`. `LEDGER-r4.md` carries the result and is marked
UNREVIEWED.

**Owner guidance relied on**, #914 comment 6878781541 (`amaybaum`, 2026-11-14; recorded at
2026-11-14T14:26:48Z), quoted verbatim:
- "Ledger r4 should incorporate confirmed findings and retain unresolved ones explicitly."
- "The subsequent queue proposal should distinguish manuscript corrections, missing ledger coverage,
  and scientific research obligations—they require different work and authorization."
- "The audit does not yet justify promoting QCD or another downstream branch ahead of the shared
  foundational gaps."
- "Each confirmed finding needs paired source passages and the supporting proof's actual scope."

**Counts.**
- **New rows: 51.**
  - 45 are the audit's proposals, as its reviews accepted them; they are marked "(audit)".
  - 5 are r4's own rows for confirmed uncovered entries the audit proposed no row for: B-GR-12,
    B-SM-17, B-STR-4, C-STR-6 and C-EARLY-6. They are marked "(r4)", and their classes are unreviewed.
  - 1 is B-QM-28, split from B-QM-13 per REVIEW-r3 N3.
- **Corrected rows: 26.**
  - 21 from REVIEW-r3: B-QM-5, B-QM-13, B-SM-3, B-SM-6, B-SM-FLAV-1, B-SM-FLAV-3, B-SM-BARY-2,
    B-SM-BARY-3, B-SM-BARY-4, B-SM-NP-3, B-QCD-11, B-COS-3, B-P4-QCB-1, C-PRED-1, C-PRED-4, C-PRED-5,
    C-PRED-7, C-PRED-8, C-PRED-9, C-TOPO and C-ANOM.
  - 5 from audit findings: B-SM-FLAV-5, B-SM-NU-2 (F-7), B-SM-GAUGE-3 and B-QCD-6 (F-22), and B-COS-5
    (F-14). B-SM-FLAV-1 and B-SM-FLAV-3 also carry F-25, F-26 and F-30, and are counted once each.
- **Unresolved findings: 10**, listed U-1 to U-10 in §U.
- **Other changes.**
  - The DM definition, the identifier grammar, a work-kind vocabulary and §1 are revised.
  - D11 is new, and D7–D10 cite their FULL mirrors.
  - §F (findings register) and §U (unresolved list) are new.

## A. REVIEW-r3

Each finding was checked at its source before it was applied.

| Finding | Disposition | Check at source and change |
|---|---|---|
| S1 (DM and finite carriers) | Applied | #914 comment 6875046763: "cannot assume one fixed finite total carrier". The DM definition now says a DM result holds in a common model only if that model is in the bare finite class, and that transfer to an admitted carrier is open (Q5, Q13). This also scopes the DM rows the audit proposed (B-QM-17, -18, -21, -22, -23, B-SUB-2, B-STR-3), as the audit's §7 itself flags. |
| S2 (entries with no class) | Applied | B-SM-6, B-SM-BARY-2, C-PRED-5, C-PRED-7, C-PRED-8, C-PRED-9, C-TOPO and C-ANOM take the proposed classes. C-PRED-1 and C-PRED-4 state the mapping: S → CD[cubic commitment, B-SM-4 (EF)], not DM; C, L, M → CD; R, E, P → EF. B-SM-FLAV-5 states it too. |
| S3 (B-SM-3 conditions) | Applied | `papers/SM.md`:374, "under H-link + H-cust"; `papers/Substratum.md`:163. The class is as proposed, with SM:374 added to the source. |
| S4 (B-P4-QCB-1) | Applied | `book/ch18-beyond.md`:72, "the framework's identification applies". DM covers the two results; PE covers the identification. |
| S5 (baryogenesis codes; D11) | Applied | `papers/SM.md`:1526 ("open work") and :1496–1506; `book/ch19-open-problems.md`:180–188. B-SM-BARY-3 and B-SM-BARY-4 now carry BK. B-SM-NP-3 now carries P, citing SM:1496–1506. D11 is added. B-SM-BARY-2 cites SM:1526, and Q11 includes D11. |
| S6 (appendix-a grouping) | Applied in modified form | `book/appendix-a-prediction-status.md`:170–196 has rows F1–F4, F6–F13 and no row F5 (:170–173, :179–181, :187–190, :196). The review's "F1–F5: quantum engineering" therefore reads F1–F4. The rest is as proposed: F6, F7 and F8 are mapped, F9–F12 are biology and F13 is boost-LV. The paragraph beneath §L.C now maps all 64 rows. The B and F biology and engineering rows are carried by C-BIO, the audit's proposal. |
| N1 (B-QCD-11) | Applied | `book/ch10-chemistry.md`:88, "The mechanism is derived". The class is now UO, noting that the book asserts a derivation without support (D8). |
| N2 (B-QM-5 converse) | Applied | `OIBridge/StructuralClosure.lean`:419–429 (`fullClass_extendsSubstratum` and its use) is cited. |
| N3 (B-QM-13) | Applied in modified form | OA-2 STATUS:56–57 ("for every rule"). Theorem C is the new row B-QM-28. The review says "classed RR", but RR is a support code in this ledger, so the row is class DM, support RR. B-QM-13 adds OA-1 Gap 2 (STATUS:48–51). |
| N4 (B-COS-3) | Applied | The brackets are as proposed (GR:418–452; D5). |
| N5 (identifiers) | Applied | The grammar is as proposed, with sub-identifiers for C-PRED-1, C-PRED-4 and B-SM-FLAV-5. It is extended to the new groups B-SUB and B-STR, and to the finding series D, F, K, J and M. |
| N6 (FULL mirrors) | Applied | The mirror lines were confirmed: FULL:5062, :2894, :5235 and :2886–2888. D10 adds SM:1486–1490 and :1496–1506. |
| N7 (§1 list) | Applied | `papers/SM.md`:60 includes the site factorization; H-link is added. §1 now lists (vii)–(xiii) and H-link. |
| N8 (line numbers) | Applied | B-SM-FLAV-1 cites SM:859–867, 871, 881 and 911. B-SM-FLAV-3 cites SM:1130–1160, 1172, 1196, 1215–1219, 1229 and 1257. |

## B. Coverage-audit findings

**What counts.** `COVERAGE-AUDIT-r3.md`, as confirmed by `REVIEW-AUDIT-r3.md` (ACCEPT WITH CHANGES).
Earlier reviews' corrections are taken as they appear in audit r3, which REVIEW-AUDIT-r2 and -r3
confirmed applied:
- REVIEW-AUDIT-r1: S1 (F-10 withdrawn), S2 (F-7 re-anchored), S4 (Theorem 22 removed from F-2), S7
  (CD in place of DM) and S8 (classes for every proposed row);
- REVIEW-AUDIT-r2: S1 (Cond 2 block), S2 (S mapping) and S3 (status terms).

r4 uses only those confirmed forms. Before carrying the findings, I spot-checked these passages at
`main`:
- `papers/Main.md`:151;
- `papers/Structure.md`:417, 717, 733 and 813;
- `papers/SM.md`:448, 468, 567, 1006, 1108, 1396 and 1526;
- `book/ch19-open-problems.md`:106, 118, 196, 244 and 356;
- `papers/GR.md`:104, 512 and 524;
- `book/ch18-beyond.md`:56–58.

All read as quoted.

**REVIEW-AUDIT-r3 nits.**
- **N1 (F-37's open question).** Applied, as the coordinator directed: there are ten unresolved
  findings, and F-37 is U-8.
- **N2 (SM:1229).** Reflected in B-SM-FLAV-3's sources.
- **N3 (SM:1285–1286).** Not used in the ledger.
- **N4 (owner-guidance record).** r4 quotes #914 comment 6878781541. Whether that record closes the
  audit's own acceptance condition is for the audit's revision, not this ledger.

**How the findings enter r4.**
1. **Confirmed findings.** They enter through:
   - **New rows:** the 45 proposals and 5 r4 rows above.
   - **Corrected statuses and classes:**
     - B-SM-FLAV-1: Koide EF element, F-25 and F-26.
     - B-SM-FLAV-3: K by data, F-30.
     - B-SM-NU-2: GR:410, F-7.
     - B-QCD-6 and B-SM-GAUGE-3: F-22.
     - B-COS-5: F-14.
   - **Sub-rows:**
     - C-PRED-1/1: F-35.
     - /6: F-25.
     - /22: F-6.
     - /N5: F-36.
     - and the others listed in that row.
   - **The register §F.** Every D, F (F-1 to F-38, F-10 kept as withdrawn), §3.2, K, J and M finding
     appears there, with its conflict class and status in the audit's terms.

   The audit's §7 proposed adding the F findings to §11 as questions. That is applied in modified
   form: they are carried once, in §F, rather than duplicated in §11, and Q11 points to §F's MC column.
2. **Unresolved findings.** All ten are in §U:
   - U-1: F-1;
   - U-2: F-2, the C2–C4 clauses;
   - U-3: F-22;
   - U-4 to U-7: F-26, F-27, F-28 and F-30;
   - U-8: F-37;
   - U-9: K-9;
   - U-10: Main's independence.

   Each has passage A, passage B, the proof's scope and what is open. Adding a covering row does not
   resolve a finding. U-1 stays unresolved although r4 adds Structure rows, because completeness needs
   a re-audit.
3. **Work kinds.** §F gives MC, LC and RO in three separate columns.
   - The J (joint-satisfiability) and M (mechanism) findings are RO only.
   - The D7–D11 entries and every MC entry are candidates only. Each names an unchanged passage, and
     no manuscript is changed.
4. **No promotion.**
   - The header states that the ledger records status and does not rank, and §U closes by repeating
     that.
   - No section is reordered.
   - The QCD rows are unchanged, apart from the class corrections B-QCD-6 and B-QCD-11.
   - The new QM, Substratum and Structure rows are recorded at the evidence class their sources
     support, and are not marked as priorities.

**Left as missing coverage, stated in §F.** T-6, Structure's level hierarchy and Born test
(`papers/Structure.md`:98–198, 892–954). The audit proposed no row. Its content mixes a
classification scheme with a test whose form the audit traces to Q_fb's definition, so r4 adds none.

**r4's own rows, for review.** Each class is r4's reading of the cited line. None is audit-reviewed.
- **B-GR-12** (`papers/GR.md`:104): CD[H-link].
- **B-SM-17** (`papers/SM.md`:418–426): CD[cubic lattice; roles under H-link and Theorem 11's input].
- **B-STR-4** (`papers/Structure.md`:829–862, 978–1062): UO.
- **C-STR-6** (`papers/Structure.md`:761–825, against `papers/SM.md`:1396, 1440): PE.
- **C-EARLY-6** (`book/ch18-beyond.md`:56–58): PE.

## C. Read for r4, beyond RESPONSE-r2

- **Review and audit files.** `REVIEW-r3.md`, `COVERAGE-AUDIT-r3.md`, and `REVIEW-AUDIT-r1.md` to
  `REVIEW-AUDIT-r3.md`, in full.
- **`papers/SM.md`.** 60, 418–426, 1006–1008, 1108, 1496–1506 and 1526, plus the anchor lines of
  §7.1, §7.2 and §7.5 listed in N8.
- **`papers/Main.md`.** 76, 151 and 704.
- **`papers/GR.md`.** 104, 512 and 524.
- **`papers/Structure.md`.** 417, 717, 733, 813 and the §11 heading at 829.
- **`book/`.**
  - `book/ch19-open-problems.md`:106, 118, 196, 232, 244 and 356.
  - `book/ch18-beyond.md`:56–58.
  - `book/appendix-a-prediction-status.md`:160–196.
  - FULL:2886–2894, 5062 and 5235.
- **Lean.** `verification/lean-mathlib/OIBridge/StructuralClosure.lean`:419–429.
- **Owner record.** #914 comment 6878781541, through the API.

Not done: no Lean build, no script run, no re-audit, no reading of book chapters 13–17.
