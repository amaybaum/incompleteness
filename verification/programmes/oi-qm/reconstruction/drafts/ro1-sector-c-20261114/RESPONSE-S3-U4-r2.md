# Response to the focused review of S3-U4 r2

**Review answered.** `REVIEW-S3-U4-r2.md` (blob `e377aa5e`), at PR #1294 head `e3245893`, on S3-U4 r2
(blob `d8cced4c`) and `RESPONSE-S3-U4-r1.md` (blob `a1ceebbd`). Verdict: ACCEPT WITH CHANGES, with six
required changes and nine optional items.

**Revision.** `S3-U4-r3.md`. r2 is left unchanged. **Writer:** Claude. This is paper-only work, with no
computation and no commit.

Every item is accepted and none is rejected.

## Required

| # | Finding | Disposition | Where in r3 |
|---|---|---|---|
| R1 | The PK-2 conflict needs its fixed-geometry condition | **Accepted.** PK-2 holds at fixed geometry, tick and background, while Schwindt 1999 and Walborn 2002 Fig. 3 compare apparatus settings. The conflict now arises only if (γ) maps the compared runs to the same carrier transfer `Φ_{DΣ}` and the same background at `D`, differing only in which region is declared a marker. Otherwise PK-2 is silent. Cross-references to §2.1's scope observation and to the routed settings mapping are added. The native-marker part is identified as §4.1's unreachable native-marker miss branch | §6.3; U4-F8; §10 routing |
| R2 | Prop. 2.8(i) holds under H-μ, not under any product law | **Accepted.** The citation is narrowed to H-μ (μ-G background) at §2.1, PK-2 and U4-F3. The quiet-marker branch now rests on U4's own [A-inf] (§2.1, "Beyond H-μ"): under any fixed non-carrier law independent of the carrier, the partition into regions does not change `D`'s law, by S-L1 and S-L5 [NP], in the Theorem 1′ form applied at `D`. A change of the marker's preparation changes the background and is not covered | §§2.1, 6.1 PK-2, 6.3; U4-F3 |
| R3 | QM-4's "It excludes only …" is false | **Accepted.** The bound excludes every pair with `V > √(1 − D_whole²)` (for example `D = V = 0.8`). Under the pure-complement equality it excludes every pair off the circle. The exclusion of any nonzero value of the other quantity is total only at `D_whole = 1` and at `V = 1` | §6.2 QM-4 |
| R4 | PK-6's availability caveat was dropped | **Accepted; restored.** "Per-law realizations are representable, not available (K-4)", and "Whether the K1 step executes such a readback of a which-path record under AD-1 is C-4's trace route, which is undecided" | §6.1 PK-6 |
| R5 | The Case Pk typing of the delayed-choice experiments is unconditional | **Accepted.** §5.4 now uses LIT's word "unread". The Case Pk typing is stated conditionally: it holds if an unread in-flight photon counts as unheld or inaccessible under U1 G4. U4-F6 carries the same condition. Owner question 2 now covers both this typing and the AV-t test | §5.4; U4-F6; §10 owner question 2 |
| R6 | The response's change list is incomplete | **Accepted.** The items r2 did not list are given below. U1's parked-record clause is now quoted verbatim, and the AW-1 doubt is kept in owner question 1 | §6 definition; this table |

**R6, the changes r2 made without listing them, with their r3 disposition:**
1. *New claims in r2.* Each is kept, and each is now listed here:
   - PK-7, the per-tick Case Pk profile from CALC Theorem 1 and Prop. 1.6, with no instance on record;
   - U4-F11, that LIT found no reversal-type eraser among the papers read;
   - routing item 2, a Case Pk profile instance, sent to #866.
2. *R row status change.* §4.3's R row moved from "unsourced" (r1) to "single-tick R1 derived under
   strict μ-G for the partition by `q_t`". The source is CALC §1.7's [A-inf], and a held, retained
   record stays unsourced. Kept; listed here as a change to a U1 outcome.
3. *U1's recurrence clause.* r2 shortened "A return by recurrence (S-L6) is global and lies beyond the
   budget, so it is not retention". r3 quotes the accepted clause verbatim (U1 r5 §4.5). CALC's AW-1
   doubt is raised separately and stays in owner question 1. The three return kinds are marked [P] as a
   refinement that does not change the clause.
4. *PK-6 caveat:* restored (R4).
5. *Other drops in r2*, with their r3 disposition:
   - PK-1's scrambled-return sentence: superseded. PK-1 now states that Sup-3's zero-neighbour
     condition is the condition under which the parked value is not mixed with neighbour content.
     Elsewhere it returns mixed, which is scrambled in C-RET's sense.
   - §3.1's "S-L5 applies only on the reference class": restored.
   - The c.6890079967 decision-A quotation and its "Not authorized" list: restored in the header.
   - The OCP input: dropped, because r2 and r3 rely on nothing from it.
   - §6.3's backflow sentence citing Main:153: restored in the definition of the two processes.
   - M-8's "needs no §A.29 premise": restored.
   - The #1007 row of §9: dropped, because r2 and r3 cite no #1007 record.
6. *New text in r2*, kept and listed here:
   - §2.2's AD-1(f) bullet citing CALC AW-1;
   - §4.5's use of Prop. 2.8(i) and its authorization note (c.6891808569, item 4);
   - §3.3's note on the γ plan (2c, G1).

## Optional

| # | Item | Disposition |
|---|---|---|
| O1 | CALC r2 status is out of date | Applied. Inputs, labels and §9 now record `REVIEW-U4-CALC-r2.md` (blob `70eddf2d`, at `e3245893`), "ACCEPT. r2 is ready for owner acceptance". Owner acceptance is not yet recorded |
| O2 | "r1's coset statement is therefore exact" | Applied: "The PLAN §8.4 sentence is therefore exact at `t ≤ 1`" |
| O3 | Pair-relative masking; "generic" has no defined sense | Applied in §3.2 and U4-F1 |
| O4 | Route 1 heading; μ-G in the T3 bullet | Applied. The heading is labelled [A-inf] and reads "the K1 counterpart considered here", and the T3 bullet names the μ-G background |
| O5 | "and not S-L3's standing" | Applied: "not S-L3's standing alone (the U1 re-check of §2.2 is author-side)". §2.2 notes that the focused review found no gap in that re-check, and that the review is not yet accepted |
| O6 | "Relative to a `μ`-datum" is U4's reading of Sup-3 | Applied: labelled [A-inf] in §2.2, in the §4.3 U row and in U4-F10 |
| O7 | PK-4's "exactly when" is definitional | Applied: scoped to held linear readouts, with the definition stated |
| O8 | Main:326–328 does not state that an available copy is a permutation | Applied in §4.4. The copy is a composition of native bijections (P-L3), so its conjugation is a permutation; Main:326–328 is the diagonal-preservation lemma for such channels |
| O9 | U4-F8's class | Applied: ELABORATING (a correction prompted by review) |

**Unchanged.** Nothing else changed. D-1 is undecided at (γ), and nothing counts under SNR-1. Route M
stays open, and the tier is not reached. The work remains paper-only and adds no new premise. The
C/Q target, AC-1 and the compatibility-versus-support rule stand as in r2.

**Text rules.** Both files were grepped for the banned words, machine-local paths and closing keywords.
There were no hits.
