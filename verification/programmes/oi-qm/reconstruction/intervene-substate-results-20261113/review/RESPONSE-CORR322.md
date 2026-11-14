# Response to the check of the :322–323 correction (CONFIRM-CORR322, REVISE)

Base: `040d929e` on `research/optc-1230-1232-20261113`. Owner exception: #1274 c.6865575359.
The hand check of the rotation counterexample and of the octahedral/Husimi distinction is in
`review/NOTES-STATUS.md`, section r3. Findings 1 and 2 and the should-fix header clause are applied
with the reviewer's text; the optional scope line for :275–276 and :290–292 is not added (owner
point). The edits are uncommitted.

## Full diff

```diff
diff --git a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/CHANGES.md b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/CHANGES.md
index 44cd43ee2..e062cf06c 100644
--- a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/CHANGES.md
+++ b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/CHANGES.md
@@ -2,10 +2,12 @@
 
 Every change that `NEW-RESULTS.md` makes to text copied from INTERVENE-1 r2 (`ea12fde1`, I:n) or
 SUBSTATE-BRIDGE-1 r2 (`86a413c8`, S:n) is listed here with its reason. None changes a statement's
-mathematics or a proof's steps. Reasons cite the four recorded inconsistencies (owner decision #1169
-c.6854728636, step 2; RECONCILE-r3 §5, R3:152–156) as **INC-1** to **INC-4**, the ChatGPT review nits
-by review id and number, the package's own exact-head review (`review/REVIEW-r1.md`) as "review r1"
-with its finding or nit number, and §A.42 item 8 narrowing by `DEPENDENCIES.md` row.
+mathematics or a proof's steps; Δ30 narrows a sentence written for this record (Δ26), which
+overstated G1, and changes no copied text. Reasons cite the four recorded inconsistencies (owner
+decision #1169 c.6854728636, step 2; RECONCILE-r3 §5, R3:152–156) as **INC-1** to **INC-4**, the
+ChatGPT review nits by review id and number, the package's own exact-head review
+(`review/REVIEW-r1.md`) as "review r1" with its finding or nit number, and §A.42 item 8 narrowing by
+`DEPENDENCIES.md` row.
 
 | Inconsistency | Content | Where it touches the carried text |
 |---|---|---|
@@ -47,7 +49,7 @@ with its finding or nit number, and §A.42 item 8 narrowing by `DEPENDENCIES.md`
 | Δ27 | §4.2 heading | S:155: "L4 (an additive update has a state-independent graph)" | "L4 (the graph of an additive update does not depend on the state)" | Same meaning. The repository's claims check matches the hyphenated word for a withdrawn GR claim (T_Q state-independence, H-balance), which L4 does not concern; the heading is reworded so that check does not flag it. The statement and proof below the heading are unchanged. |
 | Δ28 | §0.3, NX-1 | I:123: "**NX-1** (APPROX r2 §4.2 [D, under review]): some valid native procedure induces a transformation at an ε-independent positive distance from the route's classical class. On route C that class is `PreservesDiag` (OB/DiagonalTheory.lean:68). On E_f it is the maps with an entrywise nonnegative frame matrix." | "**NX-1** (I:123): "some valid native procedure induces a transformation at an ε-independent positive distance from the route's classical class"; on E_f the class is the one above" | Review r1 finding 8: §3.1 and G1's marker use NX-1, which §0.3 did not state. The defining clause is copied; the E_f clause is replaced by the spanning class of §0.3 (INC-1, as Δ5), and the route-C clause is not carried, since no carried result uses route C's class. |
 | Δ29 | §1, proof of (c), `op` case | I:173: "K is CM and an isometry, so K is monomial by (b)." | The same sentence followed by "[(b) is (T5b) above; Δ29]" | Review r1 nit 2: the draft's (b) is not carried; the bracket names the hypothesis of this record that takes its place. |
-| Δ30 | §3.1, "What it adds" (package text, Δ26) | "The E_f verdict separates only on spanning frames (T3); on non-spanning frames the nonnegativity test does not separate (R3:59)." | "The E_f verdict separates on spanning frames (T3); without spanning the nonnegativity test need not separate, as on the octahedral and Husimi frames (S2c, S2; R3:59)." | The earlier sentence stated non-separation for every non-spanning frame; the record shows it for two frames. A non-spanning frame on which the test separates (tetrahedral frame plus a point of probability zero; Hadamard entry −1/2) is in `review/CONFIRM-STATUS.md` finding 1 and `review/NOTES-STATUS.md`. Owner decision #1274 c.6865575359. The package's own summary sentence is narrowed; no copied statement or proof changes. |
+| Δ30 | §3.1, "What it adds" (package text, Δ26) | "The E_f verdict separates only on spanning frames (T3); on non-spanning frames the nonnegativity test does not separate (R3:59)." | "On spanning frames the frame matrix is unique, so the E_f class is fixed by the map (T3); on the tetrahedral frame it excludes a rational rotation (S2b). Without spanning the test need not separate: on the octahedral and Husimi frames non-diagonal-preserving unitaries have nonnegative frame representatives (S2c, S2; R3:59), and on the Husimi frame every unitary does." | The earlier sentence stated non-separation for every non-spanning frame; the record shows it for two frames. A non-spanning frame on which the test separates (tetrahedral frame plus a point of probability zero; Hadamard entry −1/2) is in `review/CONFIRM-STATUS.md` finding 1 and `review/NOTES-STATUS.md`. Owner decision #1274 c.6865575359. The package's own summary sentence is narrowed; no copied statement or proof changes. |
 
 ## Review nits checked against the carried text
 
diff --git a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/NEW-RESULTS.md b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/NEW-RESULTS.md
index 6aa990a4b..5131232b3 100644
--- a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/NEW-RESULTS.md
+++ b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/NEW-RESULTS.md
@@ -319,11 +319,14 @@ linearity (RV:66–67; R3:59).
 density matrices with laws; they use no OI hypothesis. The verdict they qualify is NX-1 on route
 E_f as defined in §0.3, under H-LIFT and the hypotheses of §0.1.
 
-**What it adds.** The E_f verdict separates on spanning frames (T3); without spanning the nonnegativity test need not
-separate, as on the octahedral and Husimi frames (S2c, S2; R3:59). This bears on REC-1 r7 rows 35 and 40 only as a scope
-note: their frames are orthogonal or spanning. The relation to OBL-SP's (SP) condition is an analogy
-only: G1's non-spanning concerns an encoding frame on route E_f; OBL-SP's (SP) concerns the
-reachable record laws of the native affine class under `D_0`; no map between them is given (R3:85).
+**What it adds.** On spanning frames the frame matrix is unique, so the E_f class is fixed by the
+map (T3); on the tetrahedral frame it excludes a rational rotation (S2b). Without spanning the test
+need not separate: on the octahedral and Husimi frames non-diagonal-preserving unitaries have
+nonnegative frame representatives (S2c, S2; R3:59), and on the Husimi frame every unitary does. This
+bears on REC-1 r7 rows 35 and 40 only as a scope note: their frames are orthogonal or spanning. The
+relation to OBL-SP's (SP) condition is an analogy only: G1's non-spanning concerns an encoding frame
+on route E_f; OBL-SP's (SP) concerns the reachable record laws of the native affine class under
+`D_0`; no map between them is given (R3:85).
 
 **Support layer.** [A]. Each [X] tag of this subsection is hand-checked above; the probe is
 provenance (`DEPENDENCIES.md` row X).
diff --git a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/STATUS.md b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/STATUS.md
index 73c2256e0..2a19423b6 100644
--- a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/STATUS.md
+++ b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/STATUS.md
@@ -72,7 +72,7 @@ hypotheses stated with it. Its evidence tags (`NEW-RESULTS.md`:33–36) are the
 |---|---|---|
 | 1 | T5(c): given (T5b), `InstAvail CM ↔ InstAvail substratumClass`; given (T5a) and (T5b), `genTheory CM = substratumTheory` | [A], conditional on (T5a), (T5b), open on `main`; the FI-1 headline also needs (T5d) and is not asserted |
 | 2 | E1: the induced sub-Markov kernel, with no measure invariance, no finiteness of the hidden carrier, adaptive stopping and a ⊥ outcome | [A]; measurability step hand-checked from Dynkin's π–λ theorem [L]; an upper bound, no operation exhibited |
-| 3.1 | G1: on route E_f the nonnegative-frame test is separating under T3's spanning hypothesis; without spanning it need not separate: on the octahedral and Husimi frames, non-diagonal-preserving unitaries have nonnegative frame representatives, so the E_f classical class is frame-relative | [A]; each [X] number hand-checked in the record |
+| 3.1 | G1: on route E_f, under T3's spanning hypothesis the frame matrix is unique and the class is fixed by the map; without spanning the test need not separate: on the octahedral and Husimi frames non-diagonal-preserving unitaries have nonnegative frame representatives, and on the Husimi frame every unitary does | [A]; each [X] number hand-checked in the record |
 | 3.2 | E2: under one linear encoding of every density matrix shared by all procedures, native procedures are jointly measurable, and sharp ones commute | [A]; scope as stated (no context-dependent, non-linear or restricted-domain encoding); an upper bound |
 | 4.1 | L1: tower locality for a finite site set with arbitrary site alphabets | [A] on Main:362 [P] |
 | 4.2 | L4: the dependency relation of an affine update on abelian site groups is the same for every non-empty state set | [A], one line of algebra |
@@ -90,9 +90,9 @@ SUBSTATE-BRIDGE-1, each under the hypotheses stated with it: given (T5b),
 `genTheory CM = substratumTheory`; for a procedure kernel independent of the input law (H-IND) on a
 measurable hidden carrier, the law of (output, outcome) is given by a sub-Markov kernel, without
 measure invariance or finiteness and with adaptive stopping and a ⊥ outcome; on route E_f the
-nonnegative-frame test is separating under spanning and need not separate without it (octahedral
-and Husimi frames), and under one full-domain linear encoding
-shared by all procedures the native procedures are jointly measurable; L1 and L4 hold for arbitrary
+nonnegative-frame test has a unique frame matrix under spanning and need not separate without it
+(octahedral and Husimi frames), and under one full-domain linear encoding shared by all procedures
+the native procedures are jointly measurable; L1 and L4 hold for arbitrary
 site alphabets and abelian site groups at their stencil and affine scope; with measurement
 independence kept, routes A, B and C classify how parameter dependence can be carried, with N1–N4
 not supplied and SLL an open obligation; and (PAD) gives (NS_A) for the law and triple it is
@@ -107,10 +107,10 @@ mechanism or OI↔QM result; the #1230 and #1232 drafts themselves.
 
 ## Verification status (§A.46 item 4)
 
-No result in the record is independently verified. No carried statement is known to be invalid at the scope of its witnesses; see the scope line on
-`NEW-RESULTS.md`:322–323 and `CHANGES.md` Δ30. `review/REVIEW-r1.md`
-and `review/CONFIRM-r2.md` report no mathematical error in a carried statement or proof. N1–N4 and
-SLL are open.
+No result in the record is independently verified. No carried statement is known to be invalid at
+the scope of its witnesses; see the scope line on `NEW-RESULTS.md`:322–323 and `CHANGES.md` Δ30.
+`review/REVIEW-r1.md` and `review/CONFIRM-r2.md` report no mathematical error in a carried statement
+or proof. N1–N4 and SLL are open.
 Whether hand checks in model-written reviews make a result partially verified in §A.46 item 4's
 sense is not decided here; it is part of the question before the owner (OQ-10). [A] items are paper
 arguments, hand-checked and model-reviewed, not independently verified; [L] items are imported
diff --git a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/review/NOTES-STATUS.md b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/review/NOTES-STATUS.md
index 537061f13..e70ec088e 100644
--- a/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/review/NOTES-STATUS.md
+++ b/verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/review/NOTES-STATUS.md
@@ -138,3 +138,51 @@ spanning … does not separate") is true on its "need not" reading only. `NEW-RE
 
 6. Whether to correct `NEW-RESULTS.md`:322–323 (and, on its universal reading, the copied draft
    sentence at :290–292) is an owner question: OQ-1 keeps the reviewed files unchanged.
+
+## r3: response to the check of the :322–323 correction (review CONFIRM-CORR322, REVISE)
+
+Object: `research/optc-1230-1232-20261113` at `040d929e` (fast-forward pull; HEAD unchanged). Owner
+exception: #1274 c.6865575359 (`amaybaum`, 2026-11-13T21:39:25Z), "Correct it forward
+(Recommended)", for :322–323 with a CHANGES Δ row and STATUS alignment only. The edits below are
+left uncommitted.
+
+### Hand check before editing (no script run)
+
+1. Rotation counterexample on the spanning tetrahedral frame. C(x,y,z) = (y,z,x) is a cyclic
+   coordinate permutation with determinant +1, so it is the Bloch action of a unitary. On the
+   even-sign vectors it fixes (1,1,1) and cycles (1,−1,−1) → (−1,−1,1) → (−1,1,−1) → (1,−1,−1).
+   With r = σ/2, r_k·r_m is 3/4 for equal points and −1/4 for distinct ones (two signs differ), so
+   F_kj = 1/4 + r_k·(C r_j) is 1 when r_k = C r_j and 0 otherwise: a permutation matrix, unique by
+   spanning. C sends the diagonal state with Bloch vector (0,0,1) to (0,1,0), which is not diagonal.
+   So on a spanning frame a non-diagonal-preserving unitary passes the test, and "the E_f verdict
+   separates on spanning frames" is false in the sense G1 uses. Verdict: the counterexample is valid.
+2. What T3 gives. I:143: the frame matrix is "unique by injectivity and spanning", and an induced
+   map lies in the class. It gives no exclusion. Exclusion on a spanning frame is shown in the record
+   only for S2b (minimum entry −2/5 for the rotation about z with cos 3/5, `NEW-RESULTS.md`:309–316).
+3. Octahedral versus Husimi. Octahedral, p_{±e_i}(r) = (1 ± r_i)/6: a row of a representative for
+   the point m = ±e_a, written as entries α_i ± β_i on ±e_i, gives Σ_i α_i/3 + Σ_i β_i r_i/3, which
+   must equal (1 + (Rᵀm)·r)/6. So Σ_i α_i = 1/2 and β_i = ±R_ai/2. Nonnegativity needs
+   α_i ≥ |β_i|, hence Σ_i |R_ai| ≤ 1; for a unit row this forces a single nonzero entry ±1. Only
+   signed-permutation rotations pass: the octahedral frame excludes every other rotation, and admits
+   the Hadamard (S2c). Husimi: every unitary acts by the point map n ↦ Rn (S2), a measurable
+   bijection, so every unitary has a nonnegative representative. Hence "on the Husimi frame every
+   unitary does" is correct, and it does not hold for the octahedral frame.
+
+### Edits (reviewer's text)
+
+- `NEW-RESULTS.md`, "What it adds" of §3.1: the reviewer's sentence replaces the corrected one; the
+  paragraph is re-wrapped to the file's width (no other words change).
+- `CHANGES.md`: Δ30's new-text cell matches; the header's second sentence takes the reviewer's
+  clause on Δ30; the header paragraph is re-wrapped.
+- `STATUS.md`: row 3.1 and the claim sentence take the reviewer's text; the verification-status
+  paragraph is re-wrapped.
+
+### Open points for the owner
+
+- The optional scope line for the copied sentences at `NEW-RESULTS.md`:275–276 and :290–292 (the
+  rotation (x,y,z) ↦ (y,z,x) on the tetrahedral frame; a Hadamard-invariant tetrahedron) is not
+  added. It states a fact the record does not carry.
+- Δ30's reason cell describes only the non-spanning clause; the narrowing of the spanning clause is
+  recorded in its new-text cell and in the header clause.
+- The claim sentence reads "the nonnegative-frame test has a unique frame matrix under spanning",
+  as the reviewer gives it; its subject is the test, not the map.
```
