# Ledger follow-up LC-2 to LC-6, and the review of r6: ledger r7

This is paper-only, read-only work under #914 comment 6880010243 (`amaybaum`, 2026-11-14T15:45:43Z,
"I adopt these, with Option A and r4's specific homes"). That record authorizes LC-1 to LC-7 as one
bounded follow-up with independent review.

- No repository file was edited, nothing was built or run on OI rules, and nothing was posted.
- `main` is `dfeec843`. r6 is unchanged; its SHA-256 begins `d9549dd7`.
- `LEDGER-r7.md` is marked UNREVIEWED. Every finding r7 adds is a candidate until it is reviewed.

## Part A. REVIEW-r6

| Item | Disposition | Check at source and change |
|---|---|---|
| S1, §H.4 | Applied | Each home was verified. **D4:** #1234 body, item 2, "**Companions and book.** … The book has not been swept for this". **M2:** ledger §2.4, "Accountable Issues: #1169, #1236". **M5:** §H.3 and #1055 comment 6880024537. **M6:** ledger §4.1, "Accountable Issue: #873". **U-3:** #914 comment 6877908458, "Gauge dynamics, action selection and the mass gap are linked to #1063". The replacement text follows the review's. For U-3 it adds that the queue proposal, not an owner assignment, places it there as RO-10. |
| N1, C-STR-8 | Applied | The class reads "DM only as part of B-QM-1 … not a derivation of the Born rule; exponent UO (B-QM-11)". The quote is from Main:18. |
| N2, inputs for LC-2 | Applied through LC-2 | Structure:168 and :178 carry "Forced uniquely in OI, conditionally on H-link and H-cust". They become further F-17 locations, for the difference in assumptions. :913 is D15. Both are in §R.1 and the Missing-coverage note. |
| N3, D2 | Applied | Introduction:179 cites "[Main §3.3; Substratum §3.2]". It is added in §11 and §F.1. |
| N4, §H.3 M1 | Applied | The row reads "assigned in #914 comment 6880010243; no separate authorization recorded". |
| N5, §H.4 | Applied | "any QB5(a) execution" and "any merge" are added, from #914 comment 6880010243. |

## Part B. LC-2 to LC-6

All results are in the new §R. In summary:

- **LC-2 (§R.1), the Structure re-audit.**
  - Every T-1 to T-17 entry now has a row.
  - The stretches the audit's T entries did not map were read in full: §1, §3–§5, §8, §9.4–§9.5,
    §9.7–§9.8, §10.1–§10.3, §12.1–§12.3 and §13.5. So were §13.1.1.1 and §14.7–§14.9.
  - New row: **B-STR-6 (r7)**, for Structure:886–890's claim that the partial-trace features are
    derived "from 'observation occurs' alone". It is UO as stated.
  - New candidates:
    - **D12:** Structure:872 and :886–890, against Structure:120 and :166 and Main:18.
    - **D13:** :775 and :783 call Cabibbo and Koide "real features".
    - **D14:** A/4 is placed at Level 1 at :904 and at Level 3 at :926.
    - **D15:** "Three chiral generations" at :913.
    - Further F-17 locations: :198 for the direct contradiction, and :168 and :178 for the
      difference in assumptions.
- **LC-3 (§R.2), the Main-independence trace.**
  - **The rule applied.** It is AGENTS.md as it stands on `main`, after PR #1240: "may mention
    downstream results but must not depend on them", with a removal test.
  - **The copy in this session differs.** Its rule reads "must not reference or cite downstream
    results". I applied `main`'s, because it is the current text (`git log -S` on `main`).
  - **Results.** No passage is a dependency.
    - Main:20 is a forward pointer; LC.
    - Main:660–674 is a stated input; LC.
    - Main:76 (D18) and Main:704 (M-33) are mentions not identified as downstream. They are MC-5
      candidates.
  - **Paired passages.** Each passage's companion passage is given in §R.2.
  - **T2 (#1238 comment 6800989329).** It is reconciled as far as `main` allows: its item list is in
    session files, so item-by-item mapping is not possible.
- **LC-4 (§R.3), the R ≈ ε record.** No record of the position-space width computation exists on
  `main`.
  - **The nearest script.** `papers/oi_lattice_code/trace_out_fractional/grr_spectral_measure.py`
    computes the spectral exponent (SM:130), not R.
  - **The claim also stands at SM:134.** Recorded as **D17**, with an MC candidate and an RO. Nothing
    was run.
- **LC-5 (§R.4), the reduced-depth passes.** This pass stopped partway, as the brief allows.
  - **ch13 §13.6, read in full.** It decides B3: the S label conflicts with :118, :124 and :128
    (**D16**). C-BIO/B3 is classed PE, with T.
  - **SM:960–966.** No finding.
  - **Structure §13.1.1.1 and §14.7–§14.9.** No new claim.
  - **Remaining:**
    - ch13 §13.4, §13.5 and §13.7;
    - the ch14–ch17 derivations behind B1, B2, B6–B14, F1–F4 and F9–F12;
    - the paper arguments of Main §3.4 (:429–658) and GR §3.3 (:164–298).
- **LC-6 (§R.5), the census lookup.**
  - **Identifiers.** All 22 kernel identifiers the ledger cites are declared in OIBridge, in a census
    family whose status is "current". The exception is `frozen_sourcing_verdict`, which is
    "kernel-only", as already recorded. None is superseded.
  - **Superseded citations.** Two superseded identifiers the manuscripts cite appear beside their
    successors, as the census rule requires.
  - **Displays.** Each kernel-backed equivalence display has witnesses for both directions. The GR:258
    converse is existential, witnessed by `fullClass`. Substratum:231–233 has none, which is F-16.
  - **G-9.** The audit's "question at G-9" is not stated anywhere in the audit. r7 says so, and covers
    G-9's identifier range.
  - **No Lean was built.** The helper `kernel_lookup.py` reads `git show` output only.

**Status of the unresolved findings.** All ten U rows stay listed. U-1, U-9 and U-10 now carry r7
outcomes, marked unreviewed. None is marked resolved.

**Counts.**
- New rows: B-STR-6, plus the C-BIO/B3 sub-row.
- New candidates: D12–D18.
- Corrected cells: §H.4, C-STR-8, D2 (×2), the §H.3 M1 row, F-1, F-17, F-34, K-9, U-1, U-9, U-10,
  Q11 and the Missing-coverage note.
- New section: §R.

Identifiers are stable.
