# REC-1 P0 — working notes (writer)

## Method and disclosure
- Commands: `git fetch origin <branch>` by name (research/rec-1-1169-20261113, research/tune1-step3a-1236-20261113), `git show`, `git ls-tree`, `git rev-parse`, `git log -1`, `grep`, `sed`, `wc`, `cut`, `cat -n`.
- Sources were copied read-only with `git show` into `src/` in this working folder (OA1 r5, OA2 r4, OA3 r4, S3, Main at c3b5f37a; 3A r3 at 8228b3c2) for line-numbered reading. These are not repository edits.
- No script was written or run on any OI rule. No Lean was built. No repository file was edited. Nothing was committed, pushed or posted.
- Pins verified: origin/research/rec-1-1169-20261113 = 9f7d2612f39960a41188eae8f3753d9def8019e8; origin/research/tune1-step3a-1236-20261113 = 8228b3c24e17a17f324b6779b53b04ad296b4308. Blobs at c3b5f37a match r7's input table (Main 0db17597, OA1 5a16b213, OA2 8f8ddf73, OA3 0a36fd05, S3 a9cbc675). 3A blob 7bbec04d; r7 blob f1ffac0e.

## Read
- r7 in full; RESPONSE-r3..r6 and CONFIRM-r5..r7 in full; REVIEW-r1 lines 30–115 and 350–362 (the reviewer's coset sketch and optional note 6).
- OA2:60–330 and :376–795.
- OA3:1–60, :100–135, :392–500, plus a grep of herald-typing and retention lines.
- OA1:95–135 and :540–570.
- S3:1–240.
- 3A:595–625.
- Main:42, :58 and :724.

## Not read
- OA2 N2.2 (:330–376) and §5 onward.
- OA3 N1–N3 and N5 onward, except Theorem S's hypothesis lines :299–300.
- S4; the MECH-1 and MECH-2 designs; Lean.
- The #1169 authorization comment text, and the safeguard text, which was taken as relayed.

## Reading decisions (each stated in the record)
1. The record class read with the typing. The class names records as "(H4) or (V-ii-H)" with heralds held at use and records inside `S`. (V-ii-H) as defined (OA3:120–123) makes every heralded composite available. Under held-at-use typing this is retention-type (OA3:474–475), so the class consists of full-retention observers.
   - r7's text anticipates non-composable heralds inside the class (r7:289–290). Under the literal definitions these instances are outside it.
   - This is the main point a reviewer should check. If the owner intends the broader reading, (V-ii-H) "as far as the typing admits", then the N8.2 sketch puts a convention-type contextual fragment inside the class, and P0 would not pass under that reading. The control (iii) mechanism would then be insufficient.
2. The effect set. It is common to the prepare–measure table and excludes every cell that holds a preparation-stage record. This is forced by C-PM (herald records are labels, OA3:101–102) together with N3 (every preparation-stage read is herald-able). The witness does not depend on how label cells are delimited: any fixed homomorphic effect record works.
3. Measurement timing. Reads are absolute-tick records under inclusion, and the split `t_p` is fixed per fragment. A first attempt to build a counterexample from preparations of different lengths, with time-shifted measurements, collapsed once records were taken at absolute ticks. It is not reported.
4. P4(vi)'s control fragments were fixed in §2.3 of the record before the derivation. They are the qubit parity-oblivious multiplexing fragment (O-Q) and 𝔊_K's gbit square (O-SQ). The O-SQ proof, by an eigenspace projection, is by hand. r7 notes that the dual gbit's O-SQ status is not established, so the primal square was used instead.

## Points for the reviewer
- N2: C1 (law form) is always satisfiable with `S = {0}`. The whole content is in C2 and C3. Check that P0's PASS does not lean on C1.
- N3/R4: check the step from "(V-ii-H) composites available under held-at-use" to "every earlier read is a function of present `V` at every later read". It uses OA1:131 ("still held at use time") with use time taken as the composite's final read.
- N8.2: the recorder sketch (3-cycle, conveyor with two designated blanks, uniform pads) has not been checked beyond the hand pass. It is used only to show where the class boundary does work (AW-P0-1), not as a result.
- Instance II: the herald record lands in `y₀(1)`, a cell of `V(1)`. It is excluded as a label, and the effects read `x₀(1), x₁(1)` only.
- §A.42 item 8: the decision rule itself (r7) is off `main`. This record cannot land while that gap stands.

## Safeguard handling
The coordinator relayed an owner-confirmed safeguard: report both findings in a mixed case. In this result, no preparation within the class is out of form, and no in-form check is unresolved, so no mixed case arises. The record states this explicitly in §6. It also states what the broader reading would change (§7, AW-P0-1; NOTES item 1).
