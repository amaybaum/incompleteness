# #1062 OBS-EMERGE report r5: change map

- **Base.** `REPORT-r4.md` at commit `18867ffc17ce7f06f8c89c38c0a0914f3e9164e6`. `REPORT-r5.md` is r4 with exactly the changes below. `REPORT-r3.md` and `REPORT-r4.md` each receive one prepended superseded notice; the notices on `REPORT.md` and `REPORT-r2.md` name r5 in place of r4. Those files are otherwise unchanged.
- **Owner decision.** #1169 comment 7169907126 (amaybaum, 2026-11-25T16:29:44Z), quoted: "#1062 — Observer emergence | Narrow the cycle-type result to what the hand argument establishes. Apply all four body corrections, correct the R10 labels, complete the reference trace, tighten the search-scope wording and add the superseded notice to REPORT-r3.md." "For #1062, correct the unsupported statements directly in the report. A later qualification does not repair an earlier false assertion." "Resolve the identified findings directly. Preserve the necessary supporting evidence and provenance." "Earlier revisions should carry a short superseded notice identifying the authoritative report. No elaborate historical annotation is needed."
- **Trigger.** The independent delta review of r4 (REVISE), findings 1–5.
- **Checks.** Each corrected statement was checked against `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`: NP1 `RESULT.md`:359–362; `ObservabilityQuotient.lean`:53; `PhysicalC4Discharge.lean`:633; GR:40; #914 comment 6563412926 rows 1, 3 and 3′ and ordering item 3; #1169 comment 7166418469.

## Applied

Each item gives the r4 text and the r5 text. Long cells are abbreviated with "…"; the full text is in `REPORT-r5.md`.

### 1. Finding 1: G3 enumeration (§2 Q3) and §9.6 row 6, with T11 (b)

- Old: "The independent review reports an exact enumeration that agrees: for 2×2 the cycle types without C4 are exactly the identity and (2,2); for 2×3 and 3×2 only the identity. That enumeration is the reviewer's check and is not reproduced here."
- New: "The review reports an exact enumeration for 2×2, 2×3 and 3×2. It is not reproduced on `main`, and no conclusion uses it."
- Old: "Open, apart from the 2×2 case. The reviewer's enumeration for 2×2, 2×3 and 3×2 is not reproduced on `main`."
- New: "Open; (2,2) on 2×2 fails C4 (§2 Q3)."

T11 (b) now reads: "the sentence noting that the review reports an enumeration"; check: "The sentence states only that the review reports an enumeration and gives none of its results. No conclusion uses it, including row 12 and §9.6 row 6, …".

### 2. R6: noise instances (§1.2; G4; §3 row 8; §4)

- Old: "in every checked instance, giving one class (NP1 [EC T2b])"
- New: "in each of the 14 seeded instances checked, at the stated densities: eight at (ρ, n) = (0.06, 16) and three each at (0.02, 24) and (0.01, 32), giving one class in each. A sparse instance at ρ = 0.0005 does not fill (NP1 `RESULT.md`:359–362 [EC T2b])"
- Old: "under an untuned i.i.d. law on U₂ the selection returned the whole torus, so there is no proper part"
- New: "in the 14 seeded instances of an untuned i.i.d. law on U₂ checked at the stated densities (§1.2), the selection returned the whole torus, so they have no proper part"
- Old: "untuned U₂ gives one class (G4)"
- New: "untuned U₂ gives one class in the 14 seeded instances at the stated densities (G4)"
- Old: "one class under noise"
- New: "one class in the 14 seeded noise instances at the stated densities"

The G4 bullet carries the same R6 statement as the three lines the review named, so it is corrected with them.

### 3. R10: labels (§1.2; §2 Q2)

- Old: "Whether a physical cut is informationally complete is explicitly undecided. **KC.**"
- New: "**KC**. The module's header comment lists as undecided whether the actual SM/GR cut is informationally complete (`ObservabilityQuotient.lean`:53); that is a statement of scope, not a theorem."
- Old: "C1–C4 at a lattice cut are a named open residual (KC for the cut and its periodicity; C4 OP)."
- New: "At a lattice cut the kernel names only C4's readback clause as an open residual (`LatticeCutReadback`, `PhysicalC4Discharge.lean`:633); it does not name C1–C3 at the cut (KC for the cut and its periodicity; C4 OP)."

### 4. R11: GR:40 (§7 item 2; §9.5 manuscript row)

- Old: "GR:40 uses the causal cut with a separate boundary layer; Main:26 says only that degrees of freedom beyond reach are hidden."
- New: "GR:40 carries the same wording ("Γ_V is the region in causal reach and Γ_H its complement"), with no boundary layer; Main:26 says that degrees of freedom beyond causal reach are hidden."
- Old: "For item 2, R11 applies."
- New: "Item 2 covers GR:40 as well (R11)."

### 5. Review status of G1–G5 (§6; support-class legend; §9.5 PP-here row)

- Old: "**Unreviewed arguments.** G1–G5 are unreviewed arguments written here. G2 and G3 are elementary but not checked by a non-author."
- New: "**Model-reviewed arguments.** G1–G5 are arguments written here, reviewed by two model reviews (§9.3); no author-independent verification exists. G2 and G3 are elementary."
- Old: "PP-here = an elementary argument written in this report, not reviewed."
- New: "PP-here = an elementary argument written in this report, model-reviewed, with no author-independent verification."
- Old: "The words "unreviewed" and "not checked by a non-author" in §6 and in the PP-here definition describe this absence of independent verification."
- New: deleted.

The legend carried the same false statement as §6, and the §9.5 sentence was the relabel the review identified.

### 6. T17 (§2 Q4; §8 T17)

- Old: "So O-REC is downstream of bare formation, as #914 records."
- New: "So O-REC is downstream of bare formation. #914 records that bare formation has no prerequisite, that a recording observer needs O-REC, and that O-REC's prerequisite O-ACC presupposes a declared `V`."

The T17 row now states where #914 records each of these (rows 1, 3 and 3′; ordering item 3) and that the downstream conclusion is drawn from MR-1.

### 7. §9.5 and §9.6

- Old: "Statements known to be overstated or incorrect, … (four bullets) … None of these changes a conclusion's status: …"
- New: deleted.
- Old: "| 2 | R6, R7, R10, R11 and T17 (9.5) | Statements known to be overstated or misattributed | Correction of the text | … |"
- New: "| 2 | R7 (scope wording of G4's heading and of the row 7 fact) | Non-blocking review finding; the statements hold within the scope stated beside them | — | #1062 | A bounded revision, or an owner decision to leave it |"

The deleted list's statements are all corrected in the body.

### 8. Finding 2: trace completed (§8)

T10 adds the r5 decision, #1169 comment 7169907126. New rows, all provenance: T21, #1169 comment 7166418469; T22, the r1–r4 head commits, reachable from `main` only on a merge-commit landing of PR #1562; T23, the same commits as named in the superseded notices; T24, the delta review of r4.

### 9. Nit 5: T16

- Old: "cite Breuer's 1995 bound (GR, Computation, book chapters 7 and 12, FULL), not the label."
- New: "cite Breuer's 1995 bound (GR, Computation, book chapters 7 and 12, FULL), or are audit records of those passages, not the label."

### 10. r3 delta-review record (§8 T13; §9.3)

- Old: "PR #1562 comment [comment id of the r3 delta review]"
- New: "PR #1562 comment 7169920809"
- Old: "[poster and time]"
- New: "amaybaum, 2026-11-25T17:43:58Z"

### 11. Status line, §9.3 closing paragraph, §9.7 last bullet

A "Revision r5" bullet follows "Revision r4" and quotes the owner decision. §9.3's closing paragraph records the r4 delta review (REVISE) and that r5 goes to a bounded review. §9.7 names the four superseded files and `CHANGES-r5.md`.

## Superseded notices

`REPORT-r3.md` and `REPORT-r4.md` each receive one prepended paragraph naming `REPORT-r5.md` as the authoritative revision and `CHANGES-r5.md` as its correction record. In the notices on `REPORT.md` and `REPORT-r2.md`, `REPORT-r4.md` and `CHANGES-r4.md` become `REPORT-r5.md` and `CHANGES-r5.md`.

## Not changed

R7, R8, R9, nits 4–5 of the r2 delta review and the r1 review's other nits stay open in §9.6 rows 2 and 3. No result, conclusion or support class changes beyond the scoping of R6 and the corrected attributions.
