# RESPONSE-U2A-r2: dispositions of CONFIRM-U2A-r2 for G3 unit 2(a) r3

**Target of the delta check.** `G3-UNIT2A-r2.md`, `NOTES-U2A-r2.md` and `RESPONSE-U2A-r1.md` at
`43cd2cad5a7b153ed0a9079bd0983d02070ed093`.

**Delta check.** `CONFIRM-U2A-r2.md`: CONFIRMED, with Y-1 (should-fix) and Y-2 to Y-5 (nits). It is
committed unchanged at `c6d1dd1530aa178db392b772ab6a49e647af0140`.

**r3 files.** `G3-UNIT2A-r3.md`, `NOTES-U2A-r3.md` and this file. r1 and r2 are unchanged. The verdict (C)
and its gap are unchanged.

**Rule for this revision.** Apply the reviewer's text for each item, and change nothing else except the
title and the revision lines.

## 1. Dispositions

"r3:n" means a line of `G3-UNIT2A-r3.md`.

| Item | Disposition | r3 location | Text applied |
|---|---|---|---|
| Y-1 | Accepted. | A9, r3:617–620 | The reviewer's replacement for r2:613–615, verbatim, as the A9 bullet. |
| Y-1, AW-ground | Accepted. | r3:763–766 | CONFIRM gives no separate verbatim text for AW-ground ("Update the AW-ground entry … to match"). The entry keeps its r2 text and appends the reviewer's Y-1 sentences, without the closing "Recorded under AW-ground and not adjudicated", which would be circular inside the AW-ground entry. |
| Y-2, §0 | Accepted. | r3:73–74 | "On Readings D, S and G, (ii) excludes them itself." is replaced with the reviewer's sentence, verbatim. |
| Y-2, C1′ row | Accepted. | r3:489 | The reviewer's sentence, with "them" changed to "it" to fit the row's singular subject ("a boundary metric whose law feeds back …"). That subject clause is r2's own, moved to the front. |
| Y-3, (ii-G) cell | Accepted. | r3:469 | "(take R₀ = R*: the realized value is absolute)" inserted after "`ρ_Z(R₀)`", verbatim. |
| Y-3, (ii-S) row | Accepted. | r3:472 | "excludes Reading 1 unless §8.3 makes its piece classical", verbatim, added to the "§8.3 in force" cell, whose text covers both branches ("in either branch"). |
| Y-4 | Accepted. | NOTES-U2A-r3 §1 | The reviewer's wording for r2 ("Written in the working area by the writer; committed to the branch at `43cd2cad` by the coordinator."), plus a revision line for r3. |
| Y-5 | Accepted. | r3:731 | "and §8.3 not in force" inserted, verbatim. |

**Revision lines.**

- In `G3-UNIT2A-r3.md`: the title (r2 → r3), and the three-line r2/CONFIRM provenance bullet (r3:17–19).
- In `NOTES-U2A-r3.md`: the title, and the r3 bullet in §1.

Nothing else changed. In particular, NOTES §1's pull record ("Already up to date" at `a87c410d`) is r2's
record and is left as it stands.

## 2. Size

| Comparison | Hunks | Lines |
|---|---|---|
| `G3-UNIT2A-r2.md` → `G3-UNIT2A-r3.md` | 9 | 18 insertions, 10 deletions |
| `NOTES-U2A-r2.md` → `NOTES-U2A-r3.md` | 2 | 5 insertions, 3 deletions |

The record has nine hunks:

- title;
- provenance bullet;
- Y-2 in §0;
- Y-3 (two cells);
- Y-2 in the C1′ row;
- Y-1 in A9;
- Y-5;
- Y-1 in AW-ground.

The notes have two:

- title;
- the Y-4 and r3 bullets.

No other hunk exists.

## 3. Full diff, record

```diff
--- G3-UNIT2A-r2.md
+++ G3-UNIT2A-r3.md
@@ -1,4 +1,4 @@
-# G3 unit 2(a) (r2): does GR:346's non-circularity argument exclude a self-consistent fixed point?
+# G3 unit 2(a) (r3): does GR:346's non-circularity argument exclude a self-consistent fixed point?
 
 **Scope.** This is a paper-only test under Issue #873, continuing unit 1 (PR #1275).
 
@@ -14,6 +14,9 @@
   GR:346's *order-of-derivation argument*. It is not a demonstrated no-fixed-point theorem."
 - This revision: r1 is `G3-UNIT2A-r1.md` at `46a548fb19f3b5846ed62878c182c22e715d6735`. Its independent
   review is `REVIEW-U2A-r1.md` (REVISE) at `a87c410d`. Dispositions are in `RESPONSE-U2A-r1.md`.
+- r2 is `G3-UNIT2A-r2.md` at `43cd2cad5a7b153ed0a9079bd0983d02070ed093`. Its delta check is
+  `CONFIRM-U2A-r2.md` (CONFIRMED) at `c6d1dd15`. r3 applies its Y-1 to Y-5. Dispositions are in
+  `RESPONSE-U2A-r2.md`.
 
 This record proves no theorem in Lean, runs no computation, changes no manuscript and adopts no premise.
 
@@ -67,7 +70,8 @@
   - The witness satisfies (i), (iii), (Adm1)–(Adm3) on its solution set, and (ii) on Reading E [A], [P].
 - **Controls.** C1–C4 (§1.4) are green on every reading (§4.3). C1′ (added at review; not part of the
   rule as first written) shows that on Reading E requirement (ii) adds nothing to (i) against the
-  completions GR:350 contrasts. On Readings D, S and G, (ii) excludes them itself.
+  completions GR:350 contrasts. On Reading S (ii) excludes them itself; on Reading G it does so given a
+  B_G-type premise; on Reading D only through N5-D, which is false (§2.2).
 
 **Scope.** The model is restricted to exact de Sitter metrics and to assumption M1 (`n` and `ε`
 independent of `R`). It does not show that K_cpl^conv is admissible outside de Sitter. It does not show
@@ -462,10 +466,10 @@
 |---|---|---|
 | (ii-L) on the witness | Not excluded. `Δρ_Z` is a classical microstate difference, so the loop runs through no post-partition datum, and `ρ_Z(R₀)` carries no loop. | Excluded: the loop runs through `Δρ_Z`, a post-partition datum. |
 | (ii-L) on GR:400 Reading 1 | Admitted (C2(c)). | Excluded. |
-| (ii-G) with B_G on the witness | Excluded through the absolute part `ρ_Z(R₀)`, which is emergent (GR:575). `Δρ_Z` is classical and admitted. | Excluded through both parts. |
+| (ii-G) with B_G on the witness | Excluded through the absolute part `ρ_Z(R₀)` (take R₀ = R*: the realized value is absolute), which is emergent (GR:575). `Δρ_Z` is classical and admitted. | Excluded through both parts. |
 | (ii-G) with B_G on GR:400 Reading 1 | Admitted: its piece is classical. | Excluded. |
 | (ii-W) | Excludes neither, in either branch. | Excludes neither. |
-| (ii-S) | Excludes the witness, in either branch. | Excludes the witness. |
+| (ii-S) | Excludes the witness, in either branch; excludes Reading 1 unless §8.3 makes its piece classical. | Excludes the witness. |
 
 [P] for the table, [A] for the loop structure it rests on.
 
@@ -482,7 +486,7 @@
 | C2(c) | GR:400 Reading 1 under §8.3: Readings E and G admit it, and so does (ii-L) (§4.2). The gap equation (GR:154; book/appendix-c-objections.md:259) is an implicit determination in which ħ grounds nothing upstream of the geometry. Readings E and G class it as non-circular, as the corpus does. [P] | green |
 | C3 | `dρ_I/dR > 0`, `dρ_II/dR > 0` (§3.4). Z_0 fails and is not used as a witness. [A] | green |
 | C4 | Z_I: an open interval of `Λ_c`. Z_II: an open half-line. [A] | green |
-| C1′ (added at review) | GR:350: (i)–(iii) "fix the metric at the partition boundary" and not laboratory fields. **Reading E:** (ii) excludes only C1's configuration, which no completion in the corpus or unit 1 has. A semiclassical boundary metric, an implicit fixed point, is admitted by (ii). The boundary/laboratory contrast then rests on (i) alone, and (ii) adds nothing to (i) against the completions GR:350 and GR:340 contrast. **Readings D, S, G:** (ii) itself excludes a boundary metric whose law feeds back the emergent description through the partition, while a laboratory field does not define the partition, so no cycle arises. [P] | reported per reading |
+| C1′ (added at review) | GR:350: (i)–(iii) "fix the metric at the partition boundary" and not laboratory fields. **Reading E:** (ii) excludes only C1's configuration, which no completion in the corpus or unit 1 has. A semiclassical boundary metric, an implicit fixed point, is admitted by (ii). The boundary/laboratory contrast then rests on (i) alone, and (ii) adds nothing to (i) against the completions GR:350 and GR:340 contrast. **Readings D, S, G:** for a boundary metric whose law feeds back the emergent description through the partition, on Reading S (ii) excludes it itself; on Reading G it does so given a B_G-type premise; on Reading D only through N5-D, which is false (§2.2). A laboratory field does not define the partition, so no cycle arises. [P] | reported per reading |
 
 C1–C4 are green on every reading, so the verdict is written. C1′ is not a pass/fail control of §1.4. It
 records that Reading E leaves requirement (ii) idle against every completion its text is aimed at,
@@ -610,9 +614,10 @@
     restricted to terms that are functions of the emergent class.
   - That restriction is therefore load-bearing for Reading G. Substratum.md:385–389, which treats both
     descriptions as projections of `(S, φ)`, supports co-constraint rather than grounding (Attempt 1).
-  - Whether "the metric exists prior to the partition" (GR:346 s.4), read in ⊳_G, agrees with
-    Substratum.md:389 depends on whether "GR" there means the gravitational description or the metric.
-    Substratum.md:385 does not fix this. It is recorded under AW-ground and not adjudicated.
+  - Substratum.md:385 names the metric: it is "a property of the classical dynamics of the partition
+    boundary". Read in ⊳_G, that sentence and N1–N2 give a ⊳_G-cycle independent of B_G. Reading G is
+    consistent with Substratum.md:385 only if "property of" there is co-constraint, not grounding, which
+    is the stance Attempt 1 needs. Recorded under AW-ground and not adjudicated.
 
   Verdict: weighs against B_G and does not settle it. [P]
 
@@ -723,7 +728,7 @@
    - On Readings E and D, GR:346 does not settle (DZ), which is consistent with GR:352.
    - On Reading G, GR:346 settles (DZ) for the convention-fixed offset given B_G.
    - The optional note proposed in CONFIRM-r4 D-2 ("GR:346 as argued, in the same section, would settle
-     (DZ) conditionally") holds with (ii-L) added, or on Reading G given B_G.
+     (DZ) conditionally") holds with (ii-L) added and §8.3 not in force, or on Reading G given B_G.
 
 No manuscript change is proposed. This record makes no claim about the magnitude of Λ.
 
@@ -755,7 +760,10 @@
 - **AW-ground (U2A-F6).** Wherever the corpus argues from "QM is emergent" to a constraint on a
   gravitational law, the step needs a statement of whether the law's terms ground the metric. Sites to
   check: GR:342, GR:346, GR:358, and Substratum.md:385–389 (QM and GR "Both depend on the trace-out and
-  the partition"; node A9). No change is proposed.
+  the partition"; node A9). Substratum.md:385 names the metric: it is "a property of the classical
+  dynamics of the partition boundary". Read in ⊳_G, that sentence and N1–N2 give a ⊳_G-cycle independent
+  of B_G. Reading G is consistent with Substratum.md:385 only if "property of" there is co-constraint, not
+  grounding, which is the stance Attempt 1 needs. No change is proposed.
 - **AW-obs (node A5).** A coupling through one observer's partition is consistent only where the
   relevant observers' partitions agree. This is a candidate constraint on K_cpl^conv outside maximal
   symmetry, independent of GR:346, and it is not tested here.
```

## 4. Full diff, notes

```diff
--- NOTES-U2A-r2.md
+++ NOTES-U2A-r3.md
@@ -1,4 +1,4 @@
-# NOTES-U2A-r2: working log for G3 unit 2(a), revision 2
+# NOTES-U2A-r3: working log for G3 unit 2(a), revision 3
 
 ## 1. Pins
 
@@ -13,8 +13,10 @@
   - r1 was written in the working area by the writer and committed to the branch at `46a548fb` by the
     coordinator. `NOTES-U2A-r1.md` §1 says "Nothing was committed, pushed or posted"; that was true when
     it was written, and REVIEW-U2A-r1 U-10 notes it is inaccurate at the head.
-  - r2 (`G3-UNIT2A-r2.md`, this file and `RESPONSE-U2A-r1.md`) was written in the working area. The
-    writer did not commit, push or post it.
+  - r2 (`G3-UNIT2A-r2.md`, `NOTES-U2A-r2.md` and `RESPONSE-U2A-r1.md`): Written in the working area by
+    the writer; committed to the branch at `43cd2cad` by the coordinator.
+  - r3 (`G3-UNIT2A-r3.md`, this file and `RESPONSE-U2A-r2.md`) applies CONFIRM-U2A-r2 (`c6d1dd15`) Y-1 to
+    Y-5 only. It was written in the working area. The writer did not commit, push or post it.
   - r1 is unchanged.
 - **Authority.** #873 c.6863416405 (`amaybaum`, 2026-11-13T19:58:10Z): Q4, unit 2(a), paper-only. The
   coordinator's request for r2 is a session message, not an owner record.
```

No manuscript change is proposed. No premise is adopted.
