# RESPONSE-CORR-r1: dispositions of CONFIRM-CORR-r1 for G3-UNIT1-CORR-r2

**Review.** `CONFIRM-CORR-r1.md` (CONFIRMED, with K-1 to K-3 should-fix and K-4 nit), of
`G3-UNIT1-CORR-r1.md` at `2c25b544399630023d4af0c3f908416f4e0a1345`.

r2 is a new file. r1 is unchanged. r2 applies the reviewer's text for K-1 to K-4 and changes nothing
else apart from the title line and one added revision line in the header.

## 1. Dispositions

| Finding | Disposition | Where in r2 |
|---|---|---|
| K-1 | Applied as X-21, with the reviewer's proposed text as the corrected statement. The NOTES-r5 quotations are those of CONFIRM-CORR-r1 K-1; the inner quotation marks of NOTES-r5:44 are rendered as single quotes. | X-21 |
| K-2 | Applied. The reviewer's qualifier, "with §8.3 in force, for the absolute part `ρ_Z(R₀)`; the configuration-differential part `Δρ_Z` is then admitted (U2Ar3:469)", is appended to the Reading G clause in §1 row 2, the X-1 Reading G bullet, X-14 and X-15. In X-15 it follows "on Reading G given B_G (open)", ahead of the (ii-L) branch, so that it attaches to the Reading G clause. A §4 line records that U2Ar3:729 is read with this qualifier. | §1 row 2; X-1; X-14; X-15; §4 |
| K-3 | Applied. The reviewer's sentence is appended to §1 row 1 and to the Part 1 bullet of §3. | §1 row 1; §3 |
| K-4 | Applied. The reviewer's clause, "or on (ii-L) as an added premise, for configuration-varying `ρ_Z` with §8.3 not in force", is inserted at the end of the exclusion sentence of X-3's last bullet, before the sentence "It does not rest on GR:346 on Readings E and D". X-10 reuses that bullet and so carries the clause. | X-3 |
| Title and revision | The title reads "(r2)". One header line names r1, CONFIRM-CORR-r1 and this file. | lines 1, 19–20 |

No line was reflowed: the qualifier and sentences added for K-2 and K-3 lengthen the lines that carry
them, and no other line changed.

## 2. Diff size

`diff -u G3-UNIT1-CORR-r1.md G3-UNIT1-CORR-r2.md`: 10 hunks, 8 lines removed, 26 lines added. r1 has
404 lines and r2 has 422.

## 3. Full diff

```diff
--- G3-UNIT1-CORR-r1.md	2026-11-13 21:26:54.665604190 +0000
+++ G3-UNIT1-CORR-r2.md	2026-11-13 21:32:12.713039384 +0000
@@ -1,4 +1,4 @@
-# G3 unit 1, forward correction (r1): Part 2 and requirement (ii) on the evidence of unit 2(a)
+# G3 unit 1, forward correction (r2): Part 2 and requirement (ii) on the evidence of unit 2(a)
 
 **Scope.** This is a paper-only correction record under Issue #873, for PR #1275.
 
@@ -16,6 +16,8 @@
 - Supporting record: `G3-UNIT2A-r3.md`, outcome (C), with `REVIEW-U2A-r1.md` and `CONFIRM-U2A-r2.md`
   (CONFIRMED). All are on branch `research/g3-offset-873-20261113` at
   `1ad01923efda24323217f3a5d9dd30a5c506fd3c`, and they land with this record.
+- This revision: r1 is `G3-UNIT1-CORR-r1.md`. Its check is `CONFIRM-CORR-r1.md` (CONFIRMED). r2 applies
+  its K-1 to K-4. Dispositions are in `RESPONSE-CORR-r1.md`.
 
 This record derives nothing new. Each corrected statement is scoped exactly as unit 2(a) r3 establishes
 it. It adopts no premise, changes no manuscript, runs no computation and makes no claim about the
@@ -44,8 +46,8 @@
 
 | Part | Category | Statement | Support |
 |---|---|---|---|
-| 1 | Counterexample, for source maps | As U1r5:43–47. Unaffected. | U2Ar3:726 |
-| 2 | Conditional on Reading G of GR:346 and B_G (open), for the coupling with physical content | K_cpl^conv violates (DZ) [A]. On Readings E and D, GR:346's argument does not establish (ii-L) and does not exclude a self-consistent fixed point of K_cpl^conv; (ii-L) is then an added premise. On Reading G it excludes the convention-fixed coupling if and only if B_G holds. As an added premise, (ii-L) excludes a K_cpl^conv member only when `ρ_Z` varies with the configuration through the partition and §8.3 is not in force; it is silent under Z_0. | U2Ar3:39–59, :82–90, :495–515, :672–689 |
+| 1 | Counterexample, for source maps | As U1r5:43–47. Unaffected. Part 1 is stated on (ii-W), (ii-L) and (ii-S). Whether (ii-G) with B_G excludes K_cpl^free is not examined in unit 2(a) (U2Ar3:543). | U2Ar3:726 |
+| 2 | Conditional on Reading G of GR:346 and B_G (open), for the coupling with physical content | K_cpl^conv violates (DZ) [A]. On Readings E and D, GR:346's argument does not establish (ii-L) and does not exclude a self-consistent fixed point of K_cpl^conv; (ii-L) is then an added premise. On Reading G it excludes the convention-fixed coupling if and only if B_G holds, with §8.3 in force, for the absolute part `ρ_Z(R₀)`; the configuration-differential part `Δρ_Z` is then admitted (U2Ar3:469). As an added premise, (ii-L) excludes a K_cpl^conv member only when `ρ_Z` varies with the configuration through the partition and §8.3 is not in force; it is silent under Z_0. | U2Ar3:39–59, :82–90, :495–515, :672–689 |
 
 The category "conditional on (ii-L)" is accurate for Part 2 only in the branch named in the last
 sentence of row 2. GR:346 supplies an exclusion of K_cpl^conv only on Reading G, given B_G, and that exclusion is
@@ -69,7 +71,7 @@
     self-consistent fixed point of K_cpl^conv[Z_I] or K_cpl^conv[Z_II]. On those readings (ii-L) is an
     added premise, and (DZ) for the convention-fixed offset receives no support from GR:346 [A], [P].
   - On Reading G the argument is valid. It excludes the convention-fixed coupling if and only if B_G
-    holds, whether or not §8.3 is in force [P].
+    holds, whether or not §8.3 is in force: with §8.3 in force, for the absolute part `ρ_Z(R₀)`; the configuration-differential part `Δρ_Z` is then admitted (U2Ar3:469) [P].
   - B_G is open. It fails, conditionally, if the boundary law is a coarse-grained consequence of `φ` in
     which the realized metric is grounded in `(S, φ)` directly, and if a derived law's terms do not
     ground its solutions. The first condition is G3 (open); the corpus states no view on the second [P].
@@ -104,7 +106,8 @@
     difference, and the corpus's use and (ii-L) admit it. Whether such a part gravitates is the
     question GR:579 leaves open.
   - The exclusion of K_cpl^conv therefore rests on (ii-S), P11 or GR:575, each a posit or a reading the
-    corpus does not adjudicate, or on GR:346 on Reading G given B_G. It does not rest on GR:346 on
+    corpus does not adjudicate, or on GR:346 on Reading G given B_G, or on (ii-L) as an added premise,
+    for configuration-varying `ρ_Z` with §8.3 not in force. It does not rest on GR:346 on
     Readings E and D. On Reading E requirement (ii) is (ii-W), and it admits the fixed point."
 - **Support.** U2Ar3:43–45, :76–78, :94–98, :459–477, :489, :682–683, :690–693, :703–714. The
   Reading 1 stipulation on the constant part is r5's own (U1r5:513–515) and is unaffected.
@@ -284,7 +287,7 @@
   ordering requirements of the same section (GR:342–348) included, it holds for source maps on (ii-W)
   and (ii-L). For the coupling with physical content, on the de Sitter class under M1, GR:346 does not
   settle (DZ) on Readings E and D, which is consistent with GR:352; on Reading G it settles (DZ) for the
-  convention-fixed offset given B_G (open). The λ-families are natural and conserved and share every
+  convention-fixed offset given B_G (open), with §8.3 in force, for the absolute part `ρ_Z(R₀)`; the configuration-differential part `Δρ_Z` is then admitted (U2Ar3:469). The λ-families are natural and conserved and share every
   listed datum at `r₀` (B5: K_cpl^free on (ii-W) and (ii-L), excluded by (ii-S); K_cpl^conv excluded by
   (ii-S), P11 or GR:575, and by GR:346 on Reading G given B_G)." The rest of F1, its class and its
   support are unchanged.
@@ -295,7 +298,7 @@
 - **CONFIRM-r4.** CONFIRM-r4:92: "GR:352 calls decoupling open at G3, while GR:346 as argued, in the
   same section, would settle (DZ) conditionally." r5 does not carry it (RESPONSE-r4:20).
 - **Corrected.** "GR:352 calls decoupling open at G3. GR:346, in the same section, settles (DZ) for the
-  convention-fixed offset on Reading G given B_G (open), or with (ii-L) added, `ρ_Z` varying with the
+  convention-fixed offset on Reading G given B_G (open), with §8.3 in force, for the absolute part `ρ_Z(R₀)`; the configuration-differential part `Δρ_Z` is then admitted (U2Ar3:469), or with (ii-L) added, `ρ_Z` varying with the
   configuration through the partition, and §8.3 not in force. On Readings E and D it does not settle
   (DZ)."
 - **Support.** U2Ar3:685–689, :727–731.
@@ -371,6 +374,18 @@
   GR:346 is chosen yet. Q8's correction stays deferred."
 - **Support.** U2Ar3:715–720, :833–840.
 
+### X-21. NOTES-r5 §3 decisions 1 and 3, and owner question Q4(a)
+
+- **NOTES-r5.** NOTES-r5:43–44 (decision 1): "Part 2 is therefore 'conditional on (ii-L)', not
+  'counterexample'". NOTES-r5:47–49 (decision 3): "Whether (ii-L) holds against self-consistent fixed
+  points is an open proof question". NOTES-r5:73–74 (Q4(a)): "whether GR:346's argument (ii-L) holds
+  against self-consistent fixed points. This is the smallest proof question that remains for Part 2".
+- **Corrected.** "NOTES-r5:43–44, :47–49 and :73–74: Part 2's category is that of §1 of this record. On
+  Readings E and D, GR:346's argument does not exclude a self-consistent fixed point (U2Ar3:721–724).
+  The question that remains for Part 2 is B_G, which the owner authorized as the next unit (#873
+  c.6865179466, QU5). Q4 was answered by the selection of unit 2(a) (#873 c.6863416405)."
+- **Support.** U2Ar3:721–724.
+
 ***
 
 ## 3. Statements of r5 that stand
@@ -379,7 +394,7 @@
 
 - **Part 1** (U1r5:43–47, :562–564) and every statement about K_cpl^free: it survives (ii-W) and
   (ii-L), (ii-S) excludes it, and it is world-equivalent to K_dec with Λ₀ left undetermined
-  (U2Ar3:726).
+  (U2Ar3:726). Part 1 is stated on (ii-W), (ii-L) and (ii-S). Whether (ii-G) with B_G excludes K_cpl^free is not examined in unit 2(a) (U2Ar3:543).
 - **The fine-tuning statement** of U1r5:356–359 (§3.1 (b)). Unit 2(a) extends world-equivalence with
   K_dec to K_cpl^conv[Z_I] and K_cpl^conv[Z_II] on the de Sitter class with the constant left free
   (U2A-F3), and leaves unit 1's statement on the split of the constant unchanged (U2Ar3:91–93,
@@ -401,4 +416,7 @@
   claim is made, and the corpus has not established a coupling across general metrics.
 - No zero-point convention is selected. Z_I and Z_II are constructed conventions, and no OI premise
   selects Z_0 over them (U2Ar3:654–656).
+- U2Ar3:729 ("On Reading G, GR:346 settles (DZ) for the convention-fixed offset given B_G") is read
+  with the §8.3 qualifier of U2Ar3:469: with §8.3 in force, it holds for the absolute part `ρ_Z(R₀)`
+  only, and the configuration-differential part `Δρ_Z` is then admitted.
 - The owner decisions quoted in X-19 and X-20 are cited as records; this record does not change them.
```
