# RESPONSE-r4: disposition of CONFIRM-r4 for G3 unit 1

**Review.** `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/CONFIRM-r4.md`, on
branch `research/g3-offset-873-20261113` at `60f6cc23`. It is a delta check of r4 at `e0383e50`. Its
verdict is CONFIRMED, with should-fix items D-1 and D-2 and nit D-3. Nothing is blocking.

**Files.** New: `G3-UNIT1-r5.md`, `NOTES-r5.md` and this file. Every earlier file is unchanged.

**Scope of r5.** r5 applies exactly the three replacements CONFIRM-r4 gives. The only other changes
are the title and revision lines:

- in G3-UNIT1, the title, and the review and disposition list in the header;
- in NOTES, the title, two pin rows and the files line.

## Dispositions

| Finding | Disposition | r5 location |
|---|---|---|
| D-1 | Applied. CONFIRM-r4's replacement text replaces the second and third sentences of the caveat. The same text is used in AW-loop and in NOTES §3 item 2. AUDIT.md:371–378 is cited in place of AUDIT.md:55. | G3-UNIT1-r5.md:506; :695. NOTES-r5.md:45 |
| D-2 | Applied. CONFIRM-r4's sentence replaces F1's first sentence. The optional one-line note to AW-loop or Q1 is not added, because r5 applies only the three replacements. | G3-UNIT1-r5.md:663 |
| D-3 | Applied. "(P11, W1-0)" becomes "(the classical stress-energy of the total microstate, GR:340; W1-0)". | G3-UNIT1-r5.md:227 |

AUDIT.md:371–378 (item 2.9) and GR:340 were re-read at `c3b5f37a`.

**Diff size.**

- G3-UNIT1, r4 → r5: 6 hunks. Two are the title and revision lines; four are D-1 (two places), D-2 and
  D-3.
- NOTES, r4 → r5: 4 hunks. Three are the title and revision lines; one is D-1.

No other line changed.

## Full diffs

### G3-UNIT1-r4.md → G3-UNIT1-r5.md

```diff
--- G3-UNIT1-r4.md
+++ G3-UNIT1-r5.md
@@ -1,4 +1,4 @@
-# G3 unit 1 (r4): the emergent energy origin and the covariant gravitational source
+# G3 unit 1 (r5): the emergent energy origin and the covariant gravitational source
 
 **Scope.** This is a paper-only audit under Issue #873.
 
@@ -8,8 +8,9 @@
 - Reviews on branch `research/g3-offset-873-20261113`:
   - `REVIEW-r1.md` (REVISE, of r1 at `e64b9a3c`), at `5fe230cd`;
   - `REVIEW-r2.md` (REVISE, of r2 at `1aaf87a2`), at `25257ae5`;
-  - `CONFIRM-r3.md` (NOT CONFIRMED, delta check of r3 at `b207fbaa`), at `95681321`.
-- Dispositions are in `RESPONSE-r1.md`, `RESPONSE-r2.md` and `RESPONSE-r3.md`.
+  - `CONFIRM-r3.md` (NOT CONFIRMED, delta check of r3 at `b207fbaa`), at `95681321`;
+  - `CONFIRM-r4.md` (CONFIRMED with D-1 to D-3, delta check of r4 at `e0383e50`), at `60f6cc23`.
+- Dispositions are in `RESPONSE-r1.md`, `RESPONSE-r2.md`, `RESPONSE-r3.md` and `RESPONSE-r4.md`.
 
 This record does not prove a theorem in Lean, does not run a computation, does not change a
 manuscript and does not adopt a premise.
@@ -223,7 +224,7 @@
   cutoff. (TL) does not supply `Z`, because K6 leaves the origin free. Any `Z` is therefore an added
   normalization ([K] for K6; [P] for the reading).
 - **(DZ) Zero-point decoupling of a completion.** The source minus `T^cl` contains no dependence on
-  `e_Z([r])`, with `T^cl` given by the classical assignment (P11, W1-0). (DZ) is a property of the
+  `e_Z([r])`, with `T^cl` given by the classical assignment (the classical stress-energy of the total microstate, GR:340; W1-0). (DZ) is a property of the
   source map, and it does not require `e_Z` to vary independently of `T^cl` in κ-space. A completion whose source reads the origin only
   through `e_Z([r])` satisfies (SI) trivially, because `σ_C` leaves `[r]` unchanged [A]. For such
   completions, (DZ) and not (SI) carries the content of the contrast at GR:352.
@@ -502,10 +503,7 @@
     reconciled.
   - This account is conditional on §8.3's identification of relative emergent effects with classical
     microstate differences, which is part of the geometry-first proposal (GR:573–579; P17).
-  - A further caveat [P]: the piece Reading 1 feeds back is relative between epochs. GR:579 records
-    that the relative/absolute rule does not fix how energy changes between epochs couple (the
-    electroweak and QCD transitions; AUDIT.md:55, item 2.9). By analogy, classing an epoch-differential
-    vacuum term as relative in §8.3's sense rests on GR:400's statement and not on a derivation.
+  - A further caveat [P]: the piece Reading 1 feeds back is relative between epochs. GR:579 records that the relative/absolute rule does not fix how the energy of the electroweak and QCD transitions couples. AUDIT item 2.9 (AUDIT.md:371–378) notes that, by the rule's wording, such between-epoch differences are relative. By analogy, the step from an epoch-differential vacuum term being relative to its being a classical microstate difference that gravitates, which §8.3 asserts for relative effects, rests on GR:400's statement and not on a derivation.
   - K_cpl^conv's `e_Z` is the absolute ground eigenvalue (GR:332, GR:358), which GR:575 classes as
     having no classical counterpart. The corpus's use therefore does not admit K_cpl^conv. K_cpl^conv
     survives only under (ii-W) applied to absolute emergent quantities, and no corpus text adopts that
@@ -662,7 +660,7 @@
 
 | ID | Finding | Class | Support |
 |---|---|---|---|
-| F1 | The non-implication at GR:352 holds, in the two-part form of §0. The λ-families are natural and conserved and share every listed datum at `r₀` (B5: K_cpl^free on (ii-W) and (ii-L), excluded by (ii-S); K_cpl^conv only under (ii-W) applied to absolute emergent quantities). On the oriented branch, K_cpl^free differs only in how it responds to the shift. K_cpl^conv differs only by the term `−ρ_Z g` in the source minus `T^cl`. | POSITIVE | [A] §3.1–3.2, §3.4 |
+| F1 | The non-implication at GR:352 holds relative to the data GR:352 lists. With the ordering requirements of the same section (GR:342–348) included, it holds in the two-part form of §0: for source maps on (ii-W) and (ii-L), and for the coupling with physical content only if (ii-L) lacks force against self-consistent fixed points (open). The λ-families are natural and conserved and share every listed datum at `r₀` (B5: K_cpl^free on (ii-W) and (ii-L), excluded by (ii-S); K_cpl^conv only under (ii-W) applied to absolute emergent quantities). On the oriented branch, K_cpl^free differs only in how it responds to the shift. K_cpl^conv differs only by the term `−ρ_Z g` in the source minus `T^cl`. | POSITIVE | [A] §3.1–3.2, §3.4 |
 | F2 | GR:352's pair shares the partition only with a free constant in `𝒢` or with a classical-origin relabelling of `T^cl` (the relabelling conditional, as in B2(c), on a covariant continuum limit in which a uniform classical energy has vacuum stress). Under `ρ_C = 0` the claim is empty. | ELABORATING | [A] §3.3 |
 | F3 | The shared data extend beyond GR:352's list to the operational content of the emergent generator (K10–K14, channels). Oriented thermal structure fixes the orientation; it does not fix the origin. The corpus's absolute emergent quantities (GR:332–336, :358) depend on the representative. | POSITIVE | [K], [A] |
 | F4 | Offset provenance. A shift at fixed classical data, and a shift induced by a change of hidden state (the frozen-bath mechanism of Main:340), are both invisible to (TL). P11 treats them differently. (SI) is therefore stated at fixed `κ`. Extends GR:579 and AUDIT item 2.9. | ELABORATING (mechanism and target form) | [A] §2 |
@@ -694,8 +692,7 @@
     identification of relative emergent effects with classical microstate differences (GR:573). That
     identification is part of the geometry-first proposal.
   - The reconciliation is not stated at GR:346.
-  - The epoch-differential character of the fed-back piece adds the caveat recorded at GR:579 and in
-    AUDIT item 2.9.
+  - The epoch-differential character of the fed-back piece adds a caveat. GR:579 records that the relative/absolute rule does not fix how the energy of the electroweak and QCD transitions couples. AUDIT item 2.9 (AUDIT.md:371–378) notes that, by the rule's wording, such between-epoch differences are relative. By analogy, the step from an epoch-differential vacuum term being relative to its being a classical microstate difference that gravitates, which §8.3 asserts for relative effects, rests on GR:400's statement and not on a derivation.
   - This unit proposes no manuscript change.
 - **AW-G12 (F6).** GR:12's clause "under which the distinct-descriptions argument becomes a theorem of
   the dynamics" holds only for an equivariant `(E, ℱ)` pair. The printed target form does not supply
```

### NOTES-r4.md → NOTES-r5.md

```diff
--- NOTES-r4.md
+++ NOTES-r5.md
@@ -1,4 +1,4 @@
-# NOTES-r4: working log for G3 unit 1, revision 4
+# NOTES-r5: working log for G3 unit 1, revision 5
 
 ## 1. Pins
 
@@ -13,12 +13,15 @@
   | `25257ae5` | REVIEW-r2 |
   | `b207fbaa` | r3 |
   | `95681321` | CONFIRM-r3: NOT CONFIRMED (C-1 and C-2 blocking) |
+  | `e0383e50` | r4 |
+  | `60f6cc23` | CONFIRM-r4: CONFIRMED with D-1 to D-3 |
 
 - **Authority.**
   - #873 c.6859060590 (`amaybaum`, 2026-11-13T16:40:09Z).
   - #873 c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z): unit 1, paper-only.
   - The coordinator's instructions are session messages, not owner records.
-- **Files.** All r1–r3 files and RESPONSE-r1 and RESPONSE-r2 are unchanged. The r4 files are new.
+- **Files.** All r1–r4 files and RESPONSE-r1 to RESPONSE-r3 are unchanged. The r5 files are new. r5
+  applies only CONFIRM-r4's D-1 to D-3 (RESPONSE-r4).
 
 ## 2. Reading for r4
 
@@ -39,9 +42,7 @@
 
 1. **C-2 is accepted.** The corpus's use reconciles GR:400 Reading 1 with GR:346 through §8.3, and it
    does not admit K_cpl^conv. Part 2 is therefore "conditional on (ii-L)", not "counterexample".
-2. **Added caveat [P].** The piece that Reading 1 feeds back is relative between epochs. GR:579 and
-   AUDIT item 2.9 record that the relative/absolute rule does not decide how energy changes between
-   epochs couple. The §8.3 classification of that piece therefore rests on GR:400's statement. This
+2. **Added caveat [P].** The piece that Reading 1 feeds back is relative between epochs. GR:579 records that the relative/absolute rule does not fix how the energy of the electroweak and QCD transitions couples. AUDIT item 2.9 (AUDIT.md:371–378) notes that, by the rule's wording, such between-epoch differences are relative. By analogy, the step from an epoch-differential vacuum term being relative to its being a classical microstate difference that gravitates, which §8.3 asserts for relative effects, rests on GR:400's statement and not on a derivation. This
    strengthens the conditionality of the reconciliation and does not change C-2's conclusion.
 3. **Two items are separated in O0.**
    - Whether (ii-L) holds against self-consistent fixed points is an open proof question.
```

## Checks

- No computation, build or script was run.
- Each new file was scanned by hand for the barred path strings and words.
