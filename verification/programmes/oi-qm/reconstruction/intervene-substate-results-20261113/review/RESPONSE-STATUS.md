# Response to the focused check of `STATUS.md` (review/CONFIRM-STATUS.md, at `f17020af`)

`STATUS-r2.md` revises `STATUS.md` (as committed at `f4c300bc`). No other file of the package changes.

| Item | Disposition |
|---|---|
| Finding 1 (blocking) | Checked by hand before any change (`NOTES-STATUS-r2.md`, "Finding 1 checked independently"): the zero-probability fifth point makes the frame non-spanning in the record's sense (§0.3: `Span(L(encoded states)) = ℝ^{Ω_enc}`), the first four columns of every representative are the tetrahedral frame matrix, and its entry at σ_j = (1,1,1), σ_k = (−1,1,−1) is −1/2. The counterexample is valid; a variant without a zero-probability point also works. Applied with the reviewer's text: row 3.1, claim sentence, scope paragraph, the "known to be invalid" sentence. |
| Finding 2 | Applied with the reviewer's text. |
| Finding 3 | Applied with the reviewer's text; sources re-read. |
| Nit 1 | Applied with the reviewer's text. |
| Nit 2 | Applied at both places. |
| Nit 3 | Applied in `NOTES-STATUS-r2.md`:5. |

Correcting `NEW-RESULTS.md`:322–323 itself is left as an owner question (OQ-1 keeps the reviewed files
unchanged).

## Full diff

```diff
--- STATUS.md	2026-11-13 21:27:31.102600001 +0000
+++ STATUS-r2.md	2026-11-13 21:36:57.546542414 +0000
@@ -72,7 +72,7 @@
 |---|---|---|
 | 1 | T5(c): given (T5b), `InstAvail CM ↔ InstAvail substratumClass`; given (T5a) and (T5b), `genTheory CM = substratumTheory` | [A], conditional on (T5a), (T5b), open on `main`; the FI-1 headline also needs (T5d) and is not asserted |
 | 2 | E1: the induced sub-Markov kernel, with no measure invariance, no finiteness of the hidden carrier, adaptive stopping and a ⊥ outcome | [A]; measurability step hand-checked from Dynkin's π–λ theorem [L]; an upper bound, no operation exhibited |
-| 3.1 | G1: on route E_f the nonnegative-frame test separates only on spanning frames | [A]; each [X] number hand-checked in the record |
+| 3.1 | G1: on route E_f the nonnegative-frame test is separating under T3's spanning hypothesis; without spanning it need not separate: on the octahedral and Husimi frames, non-diagonal-preserving unitaries have nonnegative frame representatives, so the E_f classical class is frame-relative | [A]; each [X] number hand-checked in the record |
 | 3.2 | E2: under one linear encoding of every density matrix shared by all procedures, native procedures are jointly measurable, and sharp ones commute | [A]; scope as stated (no context-dependent, non-linear or restricted-domain encoding); an upper bound |
 | 4.1 | L1: tower locality for a finite site set with arbitrary site alphabets | [A] on Main:362 [P] |
 | 4.2 | L4: the dependency relation of an affine update on abelian site groups is the same for every non-empty state set | [A], one line of algebra |
@@ -90,7 +90,8 @@
 `genTheory CM = substratumTheory`; for a procedure kernel independent of the input law (H-IND) on a
 measurable hidden carrier, the law of (output, outcome) is given by a sub-Markov kernel, without
 measure invariance or finiteness and with adaptive stopping and a ⊥ outcome; on route E_f the
-nonnegative-frame test separates only on spanning frames, and under one full-domain linear encoding
+nonnegative-frame test is separating under spanning and need not separate without it (octahedral
+and Husimi frames), and under one full-domain linear encoding
 shared by all procedures the native procedures are jointly measurable; L1 and L4 hold for arbitrary
 site alphabets and abelian site groups at their stencil and affine scope; with measurement
 independence kept, routes A, B and C classify how parameter dependence can be carried, with N1–N4
@@ -106,8 +107,10 @@
 
 ## Verification status (§A.46 item 4)
 
-No result in the record is independently verified. None is known to be invalid: REVIEW-r1 and
-CONFIRM-r2 report no mathematical error in a carried statement or proof. N1–N4 and SLL are open.
+No result in the record is independently verified. No carried statement is known to be invalid at
+the scope of its witnesses; see the scope line on `NEW-RESULTS.md`:322–323. `review/REVIEW-r1.md`
+and `review/CONFIRM-r2.md` report no mathematical error in a carried statement or proof. N1–N4 and
+SLL are open.
 Whether hand checks in model-written reviews make a result partially verified in §A.46 item 4's
 sense is not decided here; it is part of the question before the owner (OQ-10). [A] items are paper
 arguments, hand-checked and model-reviewed, not independently verified; [L] items are imported
@@ -115,7 +118,7 @@
 
 | § | Result | Status | Checks recorded (model-written, not verification) | Verification route |
 |---|---|---|---|---|
-| 1 | T5(c) | not independently verified; conditional on (T5a), (T5b) (gap A1) | RV:47–62; REVIEW-r1 against the Lean source | kernel target (I:294) or independent non-model review |
+| 1 | T5(c) | not independently verified; conditional on (T5a), (T5b) (gap A1) | RV:47–62; `review/REVIEW-r1.md` against the Lean source | kernel target (I:294) or independent non-model review |
 | 2 | E1 | not independently verified | hand check in `NEW-RESULTS.md`:215–224; CONFIRM-r2 §3 | kernel target (S:347) or independent non-model review |
 | 3.1 | G1 | not independently verified | RV:66–67; hand checks in `NEW-RESULTS.md`:298–316 | independent non-model review |
 | 3.2 | E2 | not independently verified | item 4: RV:64–65; S3 and Husimi bound: `NEW-RESULTS.md`:358–365 | item 4 a kernel target (S:347); independent non-model review |
@@ -128,6 +131,12 @@
 reconciliation's `REVIEW-r1.md` at `703ae20e` (#1271), off `main`; it is provenance
 (`DEPENDENCIES.md` row I).
 
+**Scope of `NEW-RESULTS.md`:322–323.** "On non-spanning frames the nonnegativity test does not
+separate" is shown for the octahedral and Husimi frames (S2c, S2). It does not hold for every
+non-spanning frame. The tetrahedral frame extended by a point of probability zero is non-spanning,
+and every frame representative of the Hadamard on it has the entry −1/2. The supported statement is
+that without spanning the test need not separate.
+
 **Remediation, one line per gap** (`DEPENDENCIES.md` rows A1, D2, D3, E2):
 
 | Gap | What is missing | Remediation | Accountable Issue |
@@ -137,6 +146,9 @@
 | D3 | L2 (S:153) and class (a)3 (S:263), on which SLL's exclusion consequence rests | land #1232 L2 with class (a)3 through its own gates, together with Theorem N (gap E2) | #1169 |
 | E2 | Bell-scope r2 Theorem N and 𝒞_sep (#1231) | land #1231 through its own gates (#1169 c.6865177667, OQ-2/OQ-3) | #868 |
 
+Issue assignments are the drafts' own: #1232's PR body names #1169 (gaps D2, D3), #1231's names #868
+(gap E2), and the record names #1169 (gap A1, `NEW-RESULTS.md`:9).
+
 c.6865177667 records OQ-2/OQ-3 as "a planning record only; nothing starts from it". It names #1231
 and #1232 L3; it does not name #1232 L2.
 
@@ -166,9 +178,9 @@
   `f1ffac0e4a254536930acf2afd56e40c32597c51` at `9f7d2612`, `cd38655c` and `3a3aa146`, so row H's
   statement that `REC-1-r7.md` is unchanged to the branch head holds at `3a3aa146`.
 
-The PR states in `PROVENANCE.md` §1 and in rows A1, C, D1, E1 and I (#1221, #1230, #1231, #1232 and
-#1271 open drafts) and the branch heads of `PROVENANCE.md` §1 (`ea12fde1`, `86a413c8`, `703ae20e`)
-hold as measured for this note.
+The PR states recorded in `PROVENANCE.md` §1 and in rows A1, C, D1, E1 and I (#1221, #1230, #1231,
+#1232 and #1271 are open drafts), and the branch heads of `PROVENANCE.md` §1 (`ea12fde1`,
+`86a413c8`, `703ae20e`), hold as measured for this note.
 
 ## Integration requirements (review 5895564670)
 
@@ -199,7 +211,8 @@
   reviewed head `d015131d` remain ancestors of `main`. The reviews cite those commits by id, and a
   squash or rebase would leave them off `main` (§A.42 items 2 and 3). The branch commits carry
   "(WIP)" in their messages; those were labels on the working checkpoints.
-- **Basis.** The landing basis is the owner practice of #1265: #1265 comment 6846206075
+- **Basis.** The proposed landing basis, pending the owner's ruling under OQ-10 (c.6865177667), is
+  the owner practice of #1265: #1265 comment 6846206075
   (`amaybaum`, 2026-11-13T06:44:20Z), "one status note per unit … naming the claim it supports",
   applied in `oa-1-20261112/STATUS.md`, "Landing". Under that practice a record lands as the
   evidence for the scoped claim it states, at the strength stated; here that is the claim above,
```
