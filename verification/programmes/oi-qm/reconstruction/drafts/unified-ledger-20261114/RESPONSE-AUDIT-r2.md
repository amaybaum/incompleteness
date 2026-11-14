# Response to REVIEW-AUDIT-r2

**UNREVIEWED.** This note gives a disposition for each item of `REVIEW-AUDIT-r2.md` (verdict ACCEPT
WITH CHANGES) and for each of the coordinator's four instructions for r3. The changes are in
`COVERAGE-AUDIT-r3.md`. r1, r2 and `RESPONSE-AUDIT-r1.md` are unchanged.

Every item was checked at source on `main` at `dfeec843` before it was applied. The work was
paper-only: no computation was run and nothing was posted. No manuscript or record file was edited.
The changes are kept minimal.

## Coordinator instructions

| Instruction | Checked at source | Disposition | Where in r3 |
|---|---|---|---|
| 1. Read the SM Cond 2 block (SM:1062–1112) with SM:1026. Record the excluded second-order route, propose a ledger row with an honest status, and record the overstatement at SM:1110. Read or account for other unsampled §7 blocks | SM:1026, :1062–1112 read in full. The exclusion is stated at :1026, :1076, :1084 and :1108; the natural-form failure at :1088–1094; the λ→0 scope caveat at :1108. SM:1092 and :1100 repeat the inference made at :1110 | **Applied.** New entry SM-47 (U), finding F-37 and proposed row B-SM-FLAV-10 (NEG, P support, scoped to the hop model and the strict second-order extraction; UO for Cond 2 and the O(λ³) route). F-38 records SM:1110, with :1092 and :1100, as a single-source overstatement (MC). The other unread §7 blocks have now been read: SM:922–935, :1162–1205 and :1228–1267. Only SM:960–966, data rows, remain unread. Reading :1228–1267 added a note to SM-35 on γ₀ | §3.1 F-37, F-38; §4.4; §6; §7 |
| 2. Define "resolved as stated" or rename it; label the ten direct contradictions as manuscript-correction candidates | The ten listed by the review: F-3, F-17, F-18, F-21, F-24, F-31 to F-34, F-36 | **Applied.** Renamed to "classified; stands (no correction made)" and defined in §1 so that it cannot be read as "fixed". MC is redefined as "manuscript-correction candidate". Each of the ten carries an explicit line that the contradiction is still in the manuscript as quoted. F-3 and F-17 also contain a difference-in-assumptions part; the candidate label is for their direct-contradiction part | §1; §3.1 |
| 3. Fix the S mapping in r2 §7 | REVIEW-r3 S2: "S rows → CD under the cubic commitment (B-SM-4), not DM" | **Applied.** "S → CD[cubic commitment, B-SM-4 (EF)]". No proposed row used the S mapping, so no row changes | §7 |
| 4. Apply the other review findings, with dispositions | below | below | |

## Review items

| Item | Checked at source | Disposition | Where in r3 |
|---|---|---|---|
| S1 | as instruction 1 | **Applied** | as above |
| S2 | as instruction 3 | **Applied** | §7 |
| S3: status term | as instruction 2 | **Applied** | §1; §3.1 |
| S3: unresolved pointer | §2 pointed only to §3 | **Applied.** It now points to §3, the observation after §4.5, and §8 (K-9) | §2 |
| S3: scope lines | — | **Applied.** §3 preamble: where no Scope line is given, passage B is the proof's own scope statement; "not applicable" for F-1, F-9, F-10 and F-29. Scope lines were added to F-37 and F-38 | §3 |
| Dispositions note on B-SM-FLAV-8 | — | **Applied.** Cross-reference to B-SM-FLAV-9 (EF) | §7 |
| N1: B3 | ch13 carries no "conjectural extension" notice (checked against the ch13 lines read; ch13 §13.6 not read); ch13:140's conjecture concerns revival | **Applied.** B3 is moved out of F-34. The appendix-a class and placement count goes from 17 to 16 rows. B3's label is recorded as unchecked | F-34; §2; §5; §10 |
| N2: sum rule | SM:1026 and :1068: the sum rule is equivalent to Cond 2 | **Applied.** F-8 and B-SM-FLAV-6 now read "CD[Cond 2] for the sum rule; CD[Cond 2; b₂₃ = 1] for θ₁₂ and θ₂₃". SM:1112's lower-octant falsifier is added | F-8; SM-37; §7 |
| N3: other equivalence displays | GR:222 and :236 boxed; Main:586; Main:617, which Main:618 declares false | **Applied.** All four added. Main:617 is noted as displayed in order to be rejected. SM and Structure have no displayed equivalence; SM's inline theorem biconditionals are carried by B-SM-10 and B-SM-11. S-24 is unchanged | F-16 |
| N4: Structure:191 | ":191 *[SM]:* Level D × Levels G1–G2" | **Applied** | F-17 |
| N5: read list | — | **Applied.** :936 is listed as read | §6 |
| N6: owner guidance record | not supplied | **Applied as far as possible.** The header states that the record is still missing and must be quoted with author and time before acceptance. Until then this remains open | header |

No item is declined.

## Count changes from r2 to r3

| Count | r2 | r3 |
|---|---|---|
| Claims found | 154 | 155 |
| C | 50 | 50 |
| CB | 30 | 30 |
| CM | 23 | 23 |
| U | 51 | 52 |
| Flag O | 36 | 36 |
| Flag T | 13 | 13 |
| Unresolved findings | 9 | 9 |

- The only new claim entry is SM-47 (U).
- F-37 and F-38 are new register entries. F-38 attaches to SM-33, which was already CM, O, so its O
  count does not change.
- Appendix-a class and placement rows: 17 to 16.
- The cross-tabulations are unchanged except that the U column now holds 52 entries. SM-47 carries no
  flag.
