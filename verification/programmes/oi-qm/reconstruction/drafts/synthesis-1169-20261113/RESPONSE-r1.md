# Response to the independent review of the #1169 synthesis r1

**Object reviewed.** `SYNTHESIS-r1.md` and `NOTES-r1.md` at `4940e8d6` on
`research/synthesis-1169-20261113`. The review is `REVIEW-r1.md` at `71253fd4` (ACCEPT WITH CHANGES;
F1–F5 blocking, F6–F21 medium or low). The committed r1 files and the review are byte-identical to
the working copies (`cmp`). r1 is left unchanged. r2 is `SYNTHESIS-r2.md` and `NOTES-r2.md`.

**Summary.** Every finding is applied. Three are applied with a stated variation (F1, F2, F8), argued
below. F12 changes the ranking: the metric is now explicit, and under it MM-3 ranks first; r1's
order is recovered under one of the two alternative metrics stated beside it. Line numbers "r2:n"
are of `SYNTHESIS-r2.md` unless marked "N2:n" (`NOTES-r2.md`).

***

## Dispositions

| Finding | Disposition | Where in r2 |
|---|---|---|
| F1 | Applied, with one variation. MM-1's ranking reason now reads "blocks every protocol of TUNE-1's initial-condition schema (1a) and, under R-lin and μ-G, selectable preparation of hidden carriers (1b′; OA1:522, :526–529)", followed by the review's text on (b)–(f), μ-O/μ-R and #1143. The variation: the review ties the second clause to "μ-G with C5 … (OA-1 gap 1)". Under F2, gap 1's holding problem is a disjunction (MP-0a or MP-0b), so the necessity that supports "blocks" is the write-unmasking result (1b′). The clause names (1b′) for that reason. | r2:442–451 |
| F2 | Applied. (1b) rewritten as "Not supplied under μ-G", with "unconditionally" restored and "absence, not necessity" stated; (1b′) added verbatim; (1c) rewritten as one disjunct, citing R7:196–200, OA1:522 and R7's own "unreviewed" marks (R7:185, :206); R7's §0 row reads "context; support for MM-1c and MM-2, see §8". Variation in the §1 label cell: the coordinator's instruction is to use only the owner's two labels, so the cell reads "shown necessary in TUNE-1's schema (1a) and for writing a selected value under R-lin and μ-G (1b′); producer: proposed route"; the absence (1b) and disjunct (1c) are stated in the entry's label line, not as labels. §0 now defines absence and disjunction findings as non-labels. | r2:35, :76–80, :108, :129–158, :177–179 |
| F3 | Applied. MM-6's label, missing-ingredient line and label paragraph now name E(b), OBL-SP and the Bell stage-5 ceiling, state that AL (BL:205) and Theorem S (OA3:349–351) do not use it, and note the coset law's role in AL (NOTES-r3:69); "the ceilings" → "these ceilings"; the §3 reason and dependency line are scoped the same way; MM-2's BL bullet reads "with a coset law (AL has no MI hypothesis, BL:205)". | r2:115, :208–212, :341–352, :434, :465–468, :493–494 |
| F4 | Applied verbatim: the §A.31 check of MM-2 is symmetric, lists the three convention-boundary patterns and the three other boundaries, and states that neither side's convention is derived. | r2:217–225 |
| F5 | Applied verbatim: A4 lists the three results with their full hypothesis sets, the record-access clause of each, and their other open exits. NOTES R-c is narrowed to match. | r2:550–560; N2:83–88 |
| F6 | Applied: MM-3a's interface, proof and layer cells as specified, adding `obsTheory_nonnegBounded` (:84) and `nonnegBounded_not_derivedOI` (:111), restricting dense control to NonnegBounded theories on `Fin 2`, and marking D6 as [A] on [K]. | r2:246 |
| F7 | Applied: MM-4's title, §1 row and missing-ingredient line name a non-affine update (outside the gauge-derived affine class; a fortiori outside (vii)), with OA1:523 and OA1:583–584; (4b) cites "L4 needs only the affine form" (OC:441–444); (4c) cites AL1 and names the exit as non-affine; "Hard to vary? No in bare form" is attributed to MP-1 only, and all three §A.29 requirements are listed (OC:502–504); owner Q1's label is stated to apply to (vii), not to the affine form; T6 added to §6; the "same lever" bullet replaced as in F14(b). | r2:109, :275–282, :287–296, :305–309, :600–602, :632–635 |
| F8 | Applied, with one addition. "Not sufficient for MM-3" now states insufficiency only (OA1:524, :573–574) and records that E1 does not make the gap-2 repair necessary for gap 3 outright (OA2:596–599); the dependency list carries "MM-3d (with (H4), (SP), (xiv), H-AR) → MM-4 ∨ supplied control ∨ the OA2:600–604 exits"; the "independent" wording is gone from §3 and the notes. Addition: MM-4 gains a sub-bullet (4d) stating that it is one disjunct of a G3 escape within E1's scope (OA2:587–604). This is the review's own evidence placed in the entry it concerns, so that the §3 count table can cite it; it adds no claim beyond OA2:587–604. | r2:297–304, :489–490; N2:65–66 |
| F9 | Applied: MM-2 is "proposed route (a derivation of the four interface items from the Definition and inclusion); load-bearing role shown by paired results", in the entry and in §1. | r2:112, :200–202 |
| F10 | Applied: MM-5 lists the coset-dependent results and states that E(b) and Corollary E2 need (xiv) instead (OA2:528–537, :752; BL:236–238; the cited sentence runs to BL:238); its interface is now those results; the §3 reason and dependency line are scoped to AL and P0; T7 added to §6. | r2:113, :321–328, :335, :461–464, :491, :603–604 |
| F11 | Applied verbatim: MM-2's scope covers the affine-class classifications and Theorem S for `G_SM` through AW-OA3-2. | r2:456–457, :487–488 |
| F12 | Applied, and the ranking changed. §1 defines eight construction targets T1–T8 and a lexicographic metric (shown necessary on its own; one member of a disjunction; load-bearing role shown), with a stated tie rule and MM-6 listed last as an obstruction premise; §3 gives the count table, the per-entry reasons, the sensitivity to two alternative metrics, and the review's "what the targets separate" paragraph. The new order is MM-3, MM-1, MM-4, MM-7, MM-8, MM-2, MM-5, MM-9, MM-6. Why it moved: after F1 and F2, MM-1 is shown necessary on its own for two targets, and MM-3's sub-rows reach three; after F9, MM-2 has no "shown necessary" role. The metric was fixed before the counts. Under MM-3 unbundled, MM-1 ranks first (r1's top); with any role counted once, MM-2 ranks first. The choice is SQ8. | r2:86–115, :421–483, :690–693; N2:49–73 |
| F13 | Applied: §8 has one row per reference, each classified by the claim it supports; QH's sentence in MM-8 is deleted (no verdict rested on it); BS Theorem N/N′, SB L3, APPROX r4a and 3A each get a gap row; OICORE-1 is marked not used; 5891524305 is added to §0, MM-1c and §8; on-`main` records each get a row. | r2:46–47, :139, :158, :250, :262–266, :398, :409–410, :699–761 |
| F14 | Applied: (a) the collisions are added (H3, H4, E1/E2, G1, the N-labels, D4/D5, B, C3), and this record's questions are renamed SQ1–SQ9, with "§7, SQ2" at MM-1; (b) the "same lever" bullet is replaced verbatim. | r2:163, :187, :594, :632–635, :651–663, :669–695 |
| F15 | Applied verbatim, including AL's standing for the mixed-path unit and owner Q3. | r2:577–580 |
| F16 | Applied: §0 records #1268's head `2a9f10ba` (REC-1-r8 and its ACCEPT review; ChatGPT review pending), that P0 r3 and r7 are byte-unchanged there, an R8 row (`615b7de8`), and that R7 line numbers are r7's; A6 cites r8 (`4b81298f`; review at `2a9f10ba`); MM-2's interface cites R8:297–303 for the L reading. | r2:25–29, :34–42, :227–228, :565–568 |
| F17 | Applied verbatim: A5 is conditional on membership in P0's class, which is not shown for TC-A. | r2:561–564 |
| F18 | Applied verbatim: T5 is carried as P0's record-only marker, and propagation waits on SQ4. | r2:571–572 |
| F19 | Applied: MM-7 separates the diagnostic's necessity from the §A.29 and non-import requirement (OC:494); MM-8 states that its necessity follows from the definition of a selector and that the PR control is generic. | r2:375–378, :393–395 |
| F20 | Applied: S3, S4, P, AF, NPS1 and NIS2 are defined in §0 with paths and blobs (blobs recomputed at `c3b5f37a`) and listed in §8; MM-1a and MM-3b(iii) carry `ε < 1/8`, `K ≥ L + 1` (S4:465). S4:464–474 and P:143, :184–199 were re-read for r2. | r2:62–67, :136–137, :247, :754–758 |
| F21 | Applied verbatim: MM-3c is stated "for `R` injective on `W`", with the G3 target named; MM-3e carries "with their update rule". | r2:248, :250 |

***

## r1→r2 delta table (from `diff SYNTHESIS-r1.md SYNTHESIS-r2.md`)

Every hunk of the diff is listed. No other line differs.

| r1 lines | r2 lines | Change | Finding |
|---|---|---|---|
| 1 | 1 | title "(r1)" → "(r2)" | revision |
| 7–8 | 7–12 | next steps; Revision line | revision |
| 21–22 | 25–29 | #1268 head `2a9f10ba`, r8, unchanged P0/r7 | F16 |
| 27–28 | 34–36 | P0 and R7 rows; R7 "context; support …"; R8 row | F16, F2 |
| (after 31) | 40–42 | R7 line numbers are r7's; r8 offsets | F16 |
| 35–36 | 46–47 | ChatGPT review 5891524305 added | F13 |
| 51 | 62–67 | P, AF, S3, S4, NPS1, NIS2 defined | F20 |
| 60 | 76–80 | two labels only; absence and disjunction are not labels | F9, F2 |
| (after 65) | 86–104 | construction targets and ranking metric | F12 |
| 68–76 | 107–115 | §1 table: new order and revised labels and scopes | F1, F2, F3, F7, F9, F10, F12 |
| 90 | 129–131 | MM-1 label line | F2 |
| 95–109 | 136–158 | MM-1a assumptions and TC-A provenance; (1b′); (1b); (1c) | F20, F13, F2 |
| 114 | 163 | "§7, Q2" → "§7, SQ2" | F14 |
| 128–130 | 177–179 | MM-1 interface and support | F2 |
| 138 | 187 | "§7 Q2" → "§7 SQ2" | F14 |
| 151–152 | 200–202 | MM-2 label | F9 |
| 158–161 | 208–212 | MM-2 BL bullet (no MI hypothesis in AL) | F3 |
| 166–172 | 217–225 | MM-2 §A.31 check, symmetric | F4 |
| 174–175 | 227–228 | MM-2 interface cites R8:297–303 | F16 |
| 193–195 | 246–248 | MM-3 rows 3a, 3b, 3c | F6, F20, F21 |
| 197 | 250 | MM-3 row 3e | F21, F13 |
| 209–211 | 262–266 | MM-3 §A.31 check: 3b–3d classical; E_f class off `main` | F12, F13 |
| 220 | 275 | MM-4 title | F7 |
| 223–225 | 278–282 | MM-4 missing ingredient; label line | F7, F8 |
| 233–234 | 290–291 | MM-4b cites OC:441–444 | F7 |
| 236–238 | 293–300 | MM-4c (AL1, non-affine exit); MM-4d added | F7, F8 |
| 240–244 | 302–309 | insufficiency for MM-3; §A.29 status; Q1 scope | F8, F7 |
| 246–247 | 311–312 | MM-4 support and found-by (4d, E1) | F8 |
| 256–261 | 321–328 | MM-5 coset-dependent results; label; interface | F10 |
| 268–269 | 335–336 | MM-5 next check cites T7 | F10 |
| 274–281 | 341–352 | MM-6 scope: E(b), OBL-SP, stage 5; not AL or Theorem S | F3, F13 |
| 304–305 | 375–378 | MM-7 necessity separated from §A.29 requirement | F19 |
| 320 | 393–395 | MM-8 necessity by definition; PR control generic | F19 |
| 323–324 | 398 | QH sentence deleted | F13 |
| 335–336 | 409–410 | MM-9: SB's L3, off `main` | F13 |
| 347 | 421–422 | §3 opening replaced by the count table heading | F12 |
| 349–356 | 424–447 | count table; tie rule; reasons 1–2 (MM-1 reason per F1) | F12, F1 |
| 358–377 | 449–483 | reasons 3–8; sensitivity; what the targets separate | F12, F8, F10, F11, F3 |
| 380–383 | 486–491 | dependency list | F8, F10, F11 |
| 385 | 493–494 | MM-6 dependency line scoped | F3 |
| 409–410 | 518–520 | §5: affine class; absence and disjunctions not necessity | F2, F7 |
| 422–424 | 532–534 | §5: ranking under the stated metric | F12 |
| 440–452 | 550–568 | A4, A5, A6 replaced | F5, F17, F16 |
| 455 | 571–572 | tensions preface: T5 record-only | F18 |
| 460–461 | 577–580 | T1 dating and AL's standing | F15 |
| 475 | 594 | "§7, Q2" → "§7, SQ2" | F14 |
| (after 480) | 600–604 | T6 and T7 added | F7, F10 |
| 508–510 | 632–635 | non-affine-update proposals, not one object | F14(b), F7 |
| 526–529 | 651–663 | name collisions extended | F14(a) |
| 535–539 | 669–673 | SQ1–SQ3 renamed | F14 |
| 543 | 677 | SQ4 renamed | F14 |
| 548–553 | 682–688 | SQ5 (adds T6 wording), SQ6 | F14, F7 |
| 555–557 | 690–695 | SQ7, SQ8 (metric choice), SQ9 (T7) | F14, F12, F10 |
| 561 | 699–741 | §8 off-`main` table, one row per reference | F13 |
| 565–577 | 745–761 | §8 on-`main` table, one row per reference | F13, F20 |

## Notes changes

`NOTES-r2.md` replaces `NOTES-r1.md` (which stays unchanged). The changes that answer findings: the
ranking section (F12, F8, F3, F9; N2:49–73), R-c narrowed (F5; N2:83–88), and the r2 reading list
(F6, F20; N2:34–45).
