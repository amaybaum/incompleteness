# #1062 OBS-EMERGE: change map, r1 to r2

- **r1.** `verification/programmes/oi-qm/interface/obs-emerge-1062-20261125/REPORT.md` at `6e2caec0acccc4efd060d335dfd1ff3b3bc204af` (PR #1562).
- **Review.** Independent non-author review, PR #1562 comment 7166647951 (verdict REVISE).
- **Authority.** Owner decision quoted in #1169 comment 7166845267 (2026-11-25T15:26:25Z): "#1562 | Resolve the five observer-emergence findings." (amaybaum, 2026-11-25, coordinating session). The decision covers the five blocking findings R1–R5. Non-blocking findings and nits are applied only where they are factual corrections inside the text of R1–R5; otherwise they are not applied, as outside the owner's bounded scope.
- **Pin.** Sources checked at `main` `e2e2a623265187a28ebec604ab8bcc672742888f`. No computation was run; the R2 counterexample uses the review's hand argument.
- **Line numbers.** The review cites Lemma 3 as Main:50 and §1.4 as Main:83–89. At the pin, Lemma 3 is Main:54 and the §1.4 marginalization is Main:84–90; r2 uses the pinned lines.

## Blocking findings

| Finding | r2 change | r2 location |
|---|---|---|
| R1: cone is KC, not PP; negative search claim false | Verified at the pin: `iterate_dependsOnlyOn_ball` (`RegionTower.lean`:283), `site_iterate_dependsOnlyOn` (:297), `readout_unaffected_outside_ball` (:304), `heis_iterate_emb` (`QuasilocalAlgebra.lean`:1330), each with `#print axioms` and no `sorry` in `RegionTower.lean`. Class changed to KC, with those four identifiers cited; "No kernel cone theorem was found" removed; scope relative to (viii) kept, since the site set and coupling graph are data of the theorem. Propagated to the Q3 three-way split. The two modules added to the source list. The classification table has no cone row, so no row changed. | §1.2 "Causal cone"; §2 Q3 "Causal boundaries"; Sources |
| R2: C4 cycle-type conjecture false | Conjecture removed. Replaced by the statement that not every non-trivial cycle type admits C4, with the hand argument: no product identification when the number of states is prime; on 2×2 with cycle type (2,2) the three conjugates (perfect matchings) give a visible next state that is a fixed function of the visible present, so C4 and C1 fail under any preparation (Main:72). The reviewer's enumeration is reported as the reviewer's check, not reproduced. Which cycle types admit C4 is stated as open. Table row 12 restated (PP-here hand argument / OP). | §2 Q3 G3, last bullet; §3 row 12 |
| R3: G1 pressure test false | Citation corrected: the record-preservation sentence is at Main:36 and ledger item (iii) (Main:736); Lemma 3 (Main:54) has no record-preservation clause. Claim corrected: every result on `(S, φ, V)` uses a time-independent partition (§1.4 `T_ij` at Main:84–90; C2/C4 across windows; `cutRealization` with fixed `Vs`). Added: a moving `V_t` meeting (E0)–(E5) does not by itself inherit Main's fixed-partition results (#914 O-ACC row). G1 reclassified NEW to ELABORATING, with the reason (Main:36; rooted audit). One scope line added after the criteria. | §2 Q1 G1; §2 Q1 after "Exclusions" |
| R4: G5 conflates O-REC readout with C2/C4 readback | The `V → H → V` identification and the attached C4-realization clause dropped. Replaced by a statement that the O-REC readout records a property of the carrier, while C2-structural and C4 (Main:74, :78) concern a hidden record of visible history read back into `V`, and that the report does not identify them. Label POSITIVE replaced by PP-here (definitional), matching table row 15. The R1-correlation qualifier stated in R4 (a preparation with positive mass on differing hidden states) added. | §2 Q4 G5 |
| R5: S1 support overstated; §1.2 sentence on maps out of `Conf` false | §1.2 sentence replaced: maps out of `Substratum.Conf` exist only parameterized by a declared region (`cutRealization`, RD5-a, with `Vs`); none is selected; the census records the observation-map leg by census, not a nonexistence claim (census note verified at the pin). `readWriteFamily_exists(_two)` restated as concerning pairs of states, witness the constant coupling, not region choice. Rooted audit scope (result.md:158) added. §4 support restated as the corpus search (§A.19 negative claim) plus `V` being a kernel parameter, not a kernel result. The chain S0–S6 marked as the report's construct (review's earliest-step verdict, inside R5's text). Propagated to §1.2 heading and class line, Q3 "Layer 0", table row 5. | §1.2; §2 Q3 "Layer 0"; §3 row 5; §4 |

## Non-blocking findings

| Finding | r2 change | Reason |
|---|---|---|
| R6: NP1 sparse instance at ρ = 0.0005 does not fill | not changed | Outside the five findings' text (§1.2, G4) |
| R7: G4 elementary fact holds under every preparation; Q not a product dynamics; heading scope; NEW to ELABORATING | not changed | Outside the five findings' text (G4) |
| R8: thresholds for (E2), (E5) | not changed | Outside the five findings' text (criteria) |
| R9: bare observer is not a CONSC-2 admitted observer | not changed | Outside the five findings' text (Q2 header) |
| R10: only the readback clause is named at the lattice cut; "informationally complete" is attribution | not changed | Outside the five findings' text (Q2 "Fixed regions"; §1.2 restricted-access bullet) |
| R11: GR:40 has the same wording as Substratum:22 | not changed | Outside the five findings' text (§7 item 2) |

## Per-argument verdicts

| Verdict | r2 change | Reason |
|---|---|---|
| G1: conclusion holds; pressure test fails | Applied via R3 | R3 |
| G2: holds; on a torus a single selected region is ∅ or Λ | not changed | Holds as written; the sharper form is outside the five findings |
| G3: holds with qualifiers (given the sizes of `C_V`, `C_H`; composite number of states; coarse-graining as identified data); conjecture refuted | Conjecture: applied via R2. The composite-size condition enters the R2 replacement text. Other qualifiers not changed | Qualifiers outside R2's text |
| G4: holds within scope; correct R6, R7 | not changed | R6, R7 not applied |
| G5: partly holds; identification is a conflation | Applied via R4 | R4 |
| (E0)–(E5): no insertion; (E2), (E5) need thresholds | not changed | R8 not applied |
| Earliest unsupported step: S1 defensible; support is the corpus search; mark the chain as the report's construct | Applied via R5 | R5 |

## Manuscript-candidate verdicts

| Candidate (§7) | Review verdict | r2 change | Reason |
|---|---|---|---|
| 1. Main:768 | not an inaccuracy; optional clarity | not changed | Outside the five findings |
| 2. Substratum:22 | valid, mild; GR:40 same wording | not changed | Outside the five findings (R11) |
| 3. Main:48 | valid, mild; "lemma without proof" weak | not changed | Outside the five findings |
| 4. Main:34 | not an inaccuracy | not changed | Outside the five findings |
| 5. Main:368 | valid, notational | not changed | Outside the five findings |

## Nits

| Nit | r2 change | Reason |
|---|---|---|
| Standing line describes the authoring agent's mode | not changed | Outside the five findings |
| §A.42 item 8: trace each #1558 reference; cite on-main modules directly | not changed | Outside the five findings |
| MEAS-Q: MQ1–MQ3 hold at every `c` | not changed | Outside the five findings |
| §5: selector undefined during a breach; background still prepared | not changed | Outside the five findings |
| Table row 6: SM:68 counterexample is exact algebra | not changed | Outside the five findings |

## Text added beyond the findings

- The "Revision r2" line in the status section, recording the authority and this change map.
