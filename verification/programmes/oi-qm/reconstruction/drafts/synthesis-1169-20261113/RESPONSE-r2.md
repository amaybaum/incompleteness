# Response to the focused confirmation of the #1169 synthesis r2

**Object confirmed.** `SYNTHESIS-r2.md`, `NOTES-r2.md` and `RESPONSE-r1.md` at `65b70b2d` on
`research/synthesis-1169-20261113`. The confirmation is `CONFIRM-r2.md` (ACCEPT WITH CHANGES (small);
residual items C1–C4, nits N1–N2). The r2 files and `RESPONSE-r1.md` are left unchanged. r3 is
`SYNTHESIS-r3.md` and `NOTES-r3.md`.

**Summary.** C1, C2, N1 and N2 are applied as specified. C3 and C4 are applied with one variation,
argued below: 3b(i) (exact T-C) is treated like 3b(ii), as an exact variant not counted for T6 at
`(ε, K)`. The §1 order is unchanged: MM-3, MM-1, MM-4, MM-7, MM-8, MM-2, MM-5, MM-9, MM-6. MM-3's key
stays (3, 0, 0). "r3:n" is `SYNTHESIS-r3.md` and "N3:n" is `NOTES-r3.md`.

***

## Dispositions

| Item | Disposition | Where in r3 |
|---|---|---|
| C1 | Applied. "under R-lin and μ-G" is replaced by "under R-lin and μ-G with C5 (held = a function of the present `V`)" in the §1 label and tied-to cells, the (1b′) heading and observer class, the MM-1 rank reason, §5 and N3. After "(OA1:522)" the entry adds "the step uses D2, so C5 is part of the interface (OA1:345–347, :149)", that SA-1(c)'s half-known ready cell is also a ready cell (OA1:346–347), and OA-1's verdict that MP-0a resolves the node "and so does MP-0b" (OA1:353–355). No count changes: within R-lin + μ-G + C5 the write needs a ready cell on its own; MM-2's T1 disjunct concerns the holding step. | r3:110, :144–149, :450–452, :530; N3:64–65 |
| C2 | Applied verbatim: (4d) is "A G3 escape for an H-AR observer of the affine class", with (H1), (H3) assumed only for the translation step and the open exits stated as dropping H-AR, (H4) or (SP) with (H1), (H3) kept; the dependency line is replaced as given. MM-4 stays a disjunct for T5. | r3:302–306, :500–501 |
| C3 | Applied, with a variation. T6 is "OA-1's qubit tier at `(ε, K)`: T-P, T-C, T-M, T-R and D (OA1:488–496)". The MM-3 T6 cell is "T6 (3a; 3e on route E_f for T-M)". Variation: the reviewer's cell also keeps "3b(i) for exact T-C, OA2:351–353". T-C at `(ε, K)` asks for consistency over `j ≤ K` applications (OA1:493), not exactness, and the reviewer's own reason for dropping 3b(ii) (Main:562: finite carriers reach any finite accuracy) applies equally to 3b(i). r3 therefore states both 3b(i) and 3b(ii) as exact variants that T6 at `(ε, K)` does not demand, and counts neither. The key stays (3, 0, 0): T4 (3b(iii)), T5 (3c, 3d), T6 (3a, 3e). | r3:94, :432, :443–445 |
| C4 | Applied. The alternative is now "every entry unbundled": each sub-form of MM-1, MM-3 and MM-4 is counted separately. With C3's treatment of 3b(i), 3b has key (1, 0, 0) (T4 through 3b(iii)), so there is no single top: ten sub-forms tie at (1, 0, 0) (1a, 1b′, 3a, 3b, 3c, 3d, 3e, 4a, MM-7, MM-8); MM-2 (0, 3, 2) follows, then 1c, 4c, 4d and MM-5 at (0, 1, 0). Had 3b(i) been counted for T6, 3b would rank first at (2, 0, 0), as the reviewer computed. "MM-1 then ranks first" and "r1's order is recovered" are removed from §3, SQ8 and the notes; the notes also record that the order of metric and counts cannot be shown from commit history. `RESPONSE-r1.md` (RESP:30) is a committed response to r1 and is left unchanged; this row supersedes its statement. | r3:479–483, :703–704; N3:58–62 |
| N1 | Applied: A6 cites "R7:289–290 (with r8's insertion after R7:293), :299–300 and :320–321", matching r3:41. | r3:578 |
| N2 | Applied: T7 reads "BL:236–238 and OA2:528 list (xiv), and no coset law, among the hypotheses of E2 and E(b)". | r3:616 |
| Revision lines | Title "(r3)"; next steps; one revision sentence pointing to `CONFIRM-r2.md` and this file. | r3:1, :8, :12–14 |

***

## r2→r3 diff of `SYNTHESIS` (`diff -u SYNTHESIS-r2.md SYNTHESIS-r3.md`, complete)

Hunks (normal-format summary): 1c1, 8c8, 12c12–14, 92c94, 108c110, 142–144c144–149, 297–300c302–306,
426c432, 437c443–445, 442–443c450–452, 470–471c479–482, 489c500–501, 518c530, 566c578, 604c616,
691–692c703–704. Each maps to one row above; no other line differs.

```diff
--- SYNTHESIS-r2.md	2026-11-13 18:28:37.022726967 +0000
+++ SYNTHESIS-r3.md	2026-11-13 18:38:30.548006680 +0000
@@ -1,15 +1,17 @@
-# #1169 synthesis (r2): prioritized missing-mechanism list from the four Bell-first paper units
+# #1169 synthesis (r3): prioritized missing-mechanism list from the four Bell-first paper units
 
 **Standing.** WIP / UNVERIFIED author record. Paper-only: source reading and hand reasoning, no
 computation on any OI rule, no script, no Lean build, no manuscript or record edit. It adopts no
 premise, promotes no claim and changes no Issue priority or status. The order in §1 is the ranking
 this deliverable asks for; it is not a planning-record change (§A.45). Every unit result used here
 is a research record, model-reviewed, and not established (§A.46 item 7). The next steps are a
-focused confirmation of r2 and the ChatGPT exact-head review.
+check of the r2→r3 diff and the ChatGPT exact-head review.
 
 **Revision.** r2 applies findings F1–F21 of the independent review of r1 (`REVIEW-r1.md`, ACCEPT
 WITH CHANGES; r1 at `4940e8d6`), with one disposition per finding and an r1→r2 delta table in
-`RESPONSE-r1.md`.
+`RESPONSE-r1.md`. r3 applies items C1–C4 and nits N1–N2 of the focused confirmation of r2
+(`CONFIRM-r2.md`, ACCEPT WITH CHANGES (small); r2 at `65b70b2d`), with the dispositions and the full
+r2→r3 diff in `RESPONSE-r2.md`.
 
 **Authority.** #1169 c.6860584645 (`amaybaum`, 2026-11-13T17:47:40Z), owner answer "Start now
 (Recommended)". Scope, verbatim: "It produces a prioritized list of missing mechanisms. Each entry is
@@ -89,7 +91,7 @@
 - T3, in-world classical setting selection (OA-1 gap 2);
 - T4, TUNE-1's embedded tunable mixing at precision `ε`;
 - T5, a non-simplex-embeddable (G3) prepare–measure fragment (OBL-SP; OA-2 Corollary E1);
-- T6, OA-1's qubit tier: phases and dense control on a qubit;
+- T6, OA-1's qubit tier at `(ε, K)`: T-P, T-C, T-M, T-R and D (OA1:488–496);
 - T7, a Bell violation with complete-history no-signalling and MI kept;
 - T8, the quantum Bell set.
 
@@ -105,7 +107,7 @@
 | Rank | ID | Missing ingredient | Label | Tied to | Layer, location | Found by |
 |---|---|---|---|---|---|---|
 | 1 | MM-3 | An observer operation beyond the configuration-level ceiling (gap 3), with its interface-specific necessary conditions | shown necessary per sub-row; the operation itself: proposed route | per sub-row 3a–3e | [K], [P], [A] on `main`; [A] off `main` (3e) | OA-1, OA-2, OA-3; OC (E2, G1) |
-| 2 | MM-1 | Ready resource: a native producer of known-value cells, renewed per run | shown necessary in TUNE-1's schema (1a) and for writing a selected value under R-lin and μ-G (1b′); producer: proposed route | TUNE-1's initial-condition schema; N1-S of hidden carriers under R-lin and μ-G | [A] off and on `main` | TS (first stop); OA-1; R7 §3.2 |
+| 2 | MM-1 | Ready resource: a native producer of known-value cells, renewed per run | shown necessary in TUNE-1's schema (1a) and for writing a selected value under R-lin and μ-G with C5 (held = a function of the present `V`) (1b′); producer: proposed route | TUNE-1's initial-condition schema; N1-S of hidden carriers under R-lin and μ-G with C5 (held = a function of the present `V`) | [A] off and on `main` | TS (first stop); OA-1; R7 §3.2 |
 | 3 | MM-4 | Setting-selective coupling: a non-affine update (outside the affine class that amplitude-scale gauge invariance yields; a fortiori outside (vii)) | shown necessary for classical setting selection and for route B; one member of a disjunction in AL's class and in Corollary E1; not sufficient for MM-3 | every observer under inclusion (4a); affine updates on products of abelian groups (4b); AL's class (4c) | [A] on `main`; [A] off `main`; [P] | OA-1; TS (N1.5); BL (AL); OC (L4) |
 | 4 | MM-7 | A restricted preparation family with complete-history no-signalling (masking) | shown necessary | parameter-dependence branch with MI kept, finite `Λ` | [A] on `main` | BL (stage 6, §5); OC (N3) |
 | 5 | MM-8 | A selector of the quantum Bell set (CHSH in `(2, 2√2]` and not more) | shown necessary relative to the unrestricted class | the unrestricted OI behaviour class | [P]; [X] off `main` | BL (stage 7); OC (N4) |
@@ -139,9 +141,12 @@
     in TS from Step 3A's candidate A (TS:100–101, off `main`, see §8). Observer class: any embedded
     observer in that schema, any rule and law. Necessity only: that a supply yields the larger
     control region is not shown (TS:340–342).
-  - **(1b′) Writing a selected value under R-lin and μ-G.** For a hidden carrier, unmasking the
-    previous slot needs a ready cell (MP-0a), with the neighbours known or isolated (OA1:522).
-    Observer class: selectable preparation (N1-S) of hidden carriers under R-lin and μ-G.
+  - **(1b′) Writing a selected value under R-lin and μ-G with C5 (held = a function of the present `V`).** For a hidden carrier,
+    unmasking the previous slot needs a ready cell (MP-0a), with the neighbours known or isolated
+    (OA1:522); the step uses D2, so C5 is part of the interface (OA1:345–347, :149). The half-known
+    ready cell of SA-1(c) is also a ready cell (OA1:346–347). OA-1's verdict on the same node is a
+    retention failure that MP-0a resolves classically, "and so does MP-0b" (OA1:353–355).
+    Observer class: selectable preparation (N1-S) of hidden carriers under R-lin and μ-G with C5 (held = a function of the present `V`).
   - **(1b) Not supplied under μ-G.** For a finite abelian `S`, an automorphism `φ` and the uniform
     law, every region is uniform at every time (Lemma P-1, OBS:529–545); point-preparing `M` `q`-ary
     cells by a herald costs `P(E) ≤ q^{−M}` (OA-1 D3, OA1:157–160). So no *unconditionally* ready
@@ -294,10 +299,11 @@
     update outside (vii)" at BL:78–83, see T6), a run law that is not coset-uniform, settings that
     are not cell values, or postselection. Here the non-affine update is one disjunct, not a
     necessary condition on its own.
-  - **(4d) A G3 escape within Corollary E1's scope.** With (H4), (SP), (xiv), H-AR, (H1) and (H3), a
-    G3 escape needs leaving (H1) ∧ (H3): MP-1 (a non-affine rule) or supplied P3/E-iso (OA2:587–592).
-    The other exits are non-additive observers, non-nested reads and non-spanning laws
-    (OA2:600–604). The non-affine update is one disjunct.
+  - **(4d) A G3 escape for an H-AR observer of the affine class.** Under (H1), H-AR and (H3)
+    settings act by translation (Theorem E(a)), so with (H4), (SP) and (xiv) kept a G3 escape needs
+    leaving (H1) ∧ (H3): MP-1 (a non-affine rule) or supplied P3/E-iso (OA2:587–592). Keeping (H1)
+    and (H3) instead and dropping H-AR, (H4) or (SP) leaves the case open (OA2:600–604). The
+    non-affine update is one disjunct.
 - **Not sufficient for MM-3.** Non-affine rules at the configuration level stay inside the kernel
   ceiling (OA-1 D6, row 5b; OA1:524, :539–544). The repair is classical only, and "does not by itself
   bear on gap 3" (OA1:524, :573–574). OA-2 states that E1 does not make the gap-2 repair necessary
@@ -423,7 +429,7 @@
 
 | ID | (i) shown necessary on its own | (ii) one member of a disjunction | (iii) load-bearing role shown | Key | Rank |
 |---|---|---|---|---|---|
-| MM-3 | T4 (3b(iii)), T5 (3c, 3d), T6 (3a, 3b(ii), 3e) | — | — | (3, 0, 0) | 1 |
+| MM-3 | T4 (3b(iii)), T5 (3c, 3d), T6 (3a; 3e on route E_f for T-M) | — | — | (3, 0, 0) | 1 |
 | MM-1 | T1 (1b′), T4 (1a) | T2 (1c) | — | (2, 1, 0) | 2 |
 | MM-4 | T3 (4a) | T5 (4d), T7 (4c) | — | (1, 2, 0) | 3 |
 | MM-7 | T7 | — | — | (1, 0, 0) | 4 |
@@ -434,13 +440,16 @@
 | MM-6 | blocks no construction; a hypothesis of E(b), OBL-SP and the Bell stage-5 ceiling | | | — | 9 |
 
 MM-7 ranks before MM-8 by the tie rule: T8 presupposes a violation (T7). MM-4's route-B necessity
-(4b) is not counted separately because route B is a route to T7, not a target.
+(4b) is not counted separately because route B is a route to T7, not a target. 3b(i) (exact T-C,
+OA2:351–353) and 3b(ii) (exact all-precision reproduction, Main:558) are exact variants that T6 at
+`(ε, K)` does not demand (Main:562); neither is counted for T6.
 
 **Reasons, entry by entry.**
 1. **MM-3** has the most targets for which a sub-condition is shown necessary on its own. Its count
    comes from five sub-rows bundled under one ingredient.
-2. **MM-1 blocks every protocol of TUNE-1's initial-condition schema (1a) and, under R-lin and μ-G,
-   selectable preparation of hidden carriers (1b′; OA1:522, :526–529).** It is TUNE-1's first stop
+2. **MM-1 blocks every protocol of TUNE-1's initial-condition schema (1a) and, under R-lin and μ-G
+   with C5 (held = a function of the present `V`), selectable preparation of hidden carriers (1b′;
+   OA1:522, :526–529).** It is TUNE-1's first stop
    and blocks part (b); parts (c) content, (d) held outcomes and (f) inherit it, and (e) rests on it
    or on MP-0b (TS:380–382). Under μ-O and μ-R it is not shown to block (N1-K can be native; N1-S
    open, OA1:522). O-RDY is a listed prerequisite of #1143.
@@ -467,8 +476,10 @@
    (NOTES-r3:69). It blocks no construction.
 
 **Sensitivity of the order to the metric.**
-- *MM-3 unbundled.* Counted sub-row by sub-row, 3b has key (2, 0, 0) (T4, T6) and each of 3a, 3c,
-  3d, 3e has (1, 0, 0). MM-1 (2, 1, 0) then ranks first, 3b second and MM-4 third.
+- *Every entry unbundled.* Counting each sub-form separately ((1a), (1b′), (1c); 3a–3e; (4a)–(4d))
+  gives no single top. Ten sub-forms tie at (1, 0, 0): 1a (T4), 1b′ (T1), 3a (T6), 3b (T4, through
+  3b(iii)), 3c (T5), 3d (T5), 3e (T6), 4a (T3), MM-7 (T7) and MM-8 (T8). MM-2 (0, 3, 2) follows,
+  then 1c, 4c, 4d and MM-5 at (0, 1, 0).
 - *Any role counted once.* Counting the targets for which an entry has any of the three roles gives
   MM-2 5 (T1, T2, T4, T5, T7); MM-1, MM-3 and MM-4 3 each; MM-5, MM-7 and MM-8 1 each. MM-2 then
   ranks first.
@@ -486,7 +497,8 @@
 - MM-1 ⇄ MM-2 under μ-G (in-`V` retention; the disjunction of 1c).
 - MM-2 → the scope of P0 (OBL-SP), AL, E(b) and OA-1 D4, and of Theorem S for `G_SM` through
   AW-OA3-2; MM-2 → MM-7 (the record region of no-signalling).
-- MM-3d (with (H4), (SP), (xiv), H-AR) → MM-4 ∨ supplied control ∨ the OA2:600–604 exits.
+- MM-3d (with (H4), (SP), (xiv), H-AR kept) → MM-4 ∨ supplied control; with (H1), (H3) kept, the
+  open exits are dropping H-AR, (H4) or (SP) (OA2:600–604).
 - MM-4 is not sufficient for MM-3 (OA1:524).
 - MM-5 → MM-1 (μ-R) and MM-5 → the scope of AL and P0.
 - MM-7 and MM-8 arise only outside AL's class.
@@ -515,7 +527,7 @@
 ## 5. What is not claimed
 
 - **No OI-wide no-go.** Each shown-necessary statement holds for its stated interface, observer
-  class and assumptions only (TUNE-1's schema, R-lin with μ-G, the configuration identification,
+  class and assumptions only (TUNE-1's schema, R-lin with μ-G and C5, the configuration identification,
   the affine class, a finite `Λ`, and so on). Absence results (MM-1b) and disjunctions (MM-1c,
   MM-4c, MM-4d) are not necessity claims.
 - **No native Bell escape.** The PR witnesses of BL stages 0–4 are designed maps. The
@@ -563,7 +575,7 @@
   (e) rests on MP-0b, which places records outside `V`, so membership is not shown, and TC-A has no
   classical pass from E(b) either (TS:296–297).
 - **A6. r8 does not reach the other units.** The three r7 passages that r8 (`4b81298f`; review at
-  `2a9f10ba`) corrects are R7:287–290, :299–300 and :320–321. None of them is cited by TS (which
+  `2a9f10ba`) corrects are R7:289–290 (with r8's insertion after R7:293), :299–300 and :320–321. None of them is cited by TS (which
   cites R7:215, 217, 220, 222, 223), by BL (C9, C10, H-xiv, `D_0`, Q2 levels) or by OC (vocabulary
   R7:94–104).
 
@@ -601,7 +613,7 @@
   "an update outside (vii)". AL (AL1), L4 and D5 hold for every affine update, so the exit each
   proves is a non-affine update.
 - **T7. Coset premise.** NOTES-r3:76–78 lists E(b) and E2 among results that rest on a coset-uniform
-  run law. BL:236–238 and OA2:528 state that E2 and E(b) need (xiv), not a coset law.
+  run law. BL:236–238 and OA2:528 list (xiv), and no coset law, among the hypotheses of E2 and E(b).
 
 **Different names for one ingredient.**
 - **Ready resource.**
@@ -688,8 +700,8 @@
 6. **SQ6. Route C wording (T1).** At any integration of #1274, should the package's route C row
    cross-reference AL's scoped closure, with AL's off-`main` status kept?
 7. **SQ7. W1.** Should W1 stay out of this list (§4) and remain on #1245?
-8. **SQ8. The ranking.** Which metric should order the list: the §1 metric (MM-3 first), MM-3
-   unbundled (MM-1 first), or any role counted once (MM-2 first)? Is the chosen order to be proposed
+8. **SQ8. The ranking.** Which metric should order the list: the §1 metric (MM-3 first), every
+   entry unbundled (ten sub-forms tied, no single top), or any role counted once (MM-2 first)? Is the chosen order to be proposed
    as a planning change? That would be a separate decision (§A.45).
 9. **SQ9. Coset premise (T7).** Should the NOTES-r3:76–78 marker be narrowed to the coset-dependent
    results at the next revision of the Bell ladder?
```

## r2→r3 diff of `NOTES` (`diff -u NOTES-r2.md NOTES-r3.md`, complete)

```diff
--- NOTES-r2.md	2026-11-13 18:29:09.232192505 +0000
+++ NOTES-r3.md	2026-11-13 18:38:43.906665450 +0000
@@ -1,7 +1,8 @@
-# NOTES (r2): #1169 synthesis, writer's working notes (not a record)
+# NOTES (r3): #1169 synthesis, writer's working notes (not a record)
 
-These notes accompany `SYNTHESIS-r2.md`. r2 answers `REVIEW-r1.md` (findings F1–F21); the
-dispositions and the r1→r2 delta table are in `RESPONSE-r1.md`.
+These notes accompany `SYNTHESIS-r3.md`. r2 answered `REVIEW-r1.md` (findings F1–F21; dispositions
+and the r1→r2 delta table in `RESPONSE-r1.md`). r3 answers `CONFIRM-r2.md` (items C1–C4, nits
+N1–N2); dispositions and the full r2→r3 diff are in `RESPONSE-r2.md`.
 
 ## Method and limits
 
@@ -54,12 +55,14 @@
    - The lexicographic order puts strength of support first: shown necessary on its own, then one
      member of a disjunction, then load-bearing role shown. A disjunct can be bypassed by another
      member, and a load-bearing input is not shown to block.
-   - Under this metric MM-3 ranks first. r1's order (MM-1 first) is recovered when MM-3's sub-rows
-     are counted separately. MM-2 ranks first when any role counts once. All three are stated in §3,
-     and the choice is SQ8.
+   - Under this metric MM-3 ranks first. With every entry unbundled, ten single-target sub-forms tie
+     and there is no single top (C4). MM-2 ranks first when any role counts once. All three are
+     stated in §3, and the choice is SQ8.
+   - That the metric preceded the counts cannot be shown from commit history; metric, targets and
+     counts entered together. What can be checked is that the metric is applied uniformly.
 2. **Why MM-1 no longer ranks first under the primary metric.** F1 and F2 narrowed it: (1b) is an
    absence result and (1c) a disjunction, so MM-1 is shown necessary on its own for T1 (1b′, R-lin
-   and μ-G) and T4 (1a, TUNE-1's schema) only.
+   and μ-G with C5, held = a function of the present `V`) and T4 (1a, TUNE-1's schema) only.
 3. **MM-2 is a proposed route with load-bearing role shown** (F9). It ranks sixth because no target
    is shown to fail without a particular derivation of it; it is a disjunct for T1, T2 and T4.
 4. **MM-4 below MM-3 and MM-1.** It is shown necessary on its own for one target (T3) under every
@@ -103,6 +106,13 @@
    text uses as "provenance".
 4. **Names.** "SQ1–SQ9" replace r1's "Q1–Q8" for this record's own questions.
 
+## r3 notes
+
+- T6 is OA-1's qubit tier at `(ε, K)` (OA1:488–496). 3b(i) and 3b(ii) are exact variants and are
+  not counted for T6; the reviewer's C3 text kept 3b(i) in the T6 cell, and RESPONSE-r2 argues the
+  uniform treatment. MM-3's key stays (3, 0, 0).
+- C1 and C2 correct wording that came from the review of r1; no count changes.
+
 ## Not done
 
 - No new derivation beyond the readings above.
```
