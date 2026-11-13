# Confirmation of REC-1 P0 r3 (independent reviewer of r1 and r2)

**Object.** `research/rec-1-1169-20261113` at `6942b1c5ca0b9ec98fb335e4ce588a0402a3a8e3`.
- I fetched the branch by name, and `ls-remote` returns the same head.
- It is a single-parent child of `7f465d56`.
- Path changes: four files added (`REC-1-P0-r3.md`, `REC-1-P0-RESPONSE-r1-corrected.md`,
  `REC-1-P0-RESPONSE-r2.md`, `REC-1-P0-CONFIRM-r2.md`) and `REC-1-P0-OBJECTS.md` modified. No
  other path changed.
- The review was read-only and by hand.

**Verdict: ACCEPT.** No further changes are required. The outcome stands: O-U for OBL-SP's class,
a scoped pass under (LF) at [W, P0], and no hand-off to AW-OA2-1.

1. **A–E and the optional suggestion are applied exactly.** I compared each against CONFIRM-r2's
   old→new text.
   - **A.** The heading now reads "made precise", and the replacement text is verbatim. r2's
     opening sentence ("Take N4.2's three-cell shift … conveyor recorder.") stays, because
     CONFIRM-r2's old string began after it.
   - **B.** The line "other record classes (C6), as r7:366 names them" is inserted before C2.
   - **C.** The verdict text is verbatim, and the following sentence is kept.
   - **D.** The qualifier is added verbatim to the last cell of row 3.
   - **E.** Both strings are replaced verbatim.
   - **Optional.** "[W, P0], under the conditions of the scoped result above" is added.
   - I re-checked RESPONSE-r2's hand derivation for A with `N = 2`. `r_2(4) = x` moves to `r_3`,
     which is in `H`, at tick 5. So `V(5) = (y, u′+x, u, y)`, `x` is not recovered and (H4) fails.
     The herald is held at `t_p = 3`. The derivation is correct.

2. **The r2→r3 diff contains only these changes, plus the title and Revision.** `diff` shows the
   title "(r3)", one added Revision sentence, and A, B, C, D, E and the optional suggestion. There
   are no other hunks.

3. **RESPONSE-r1-corrected differs from the committed RESPONSE-r1 in item 3 and in the closing
   "Disagreements" line, plus one added "Corrected copy" header paragraph.** That paragraph says what
   the copy is and that the committed file is left as it stands. It is a statement of the file's
   standing, not a change of content, and it is accurate. The corrected item 3 is accurate: masking
   alone does not break (H4), and the precise `N = 2` form does.

4. **Copies and hashes.**
   - `REC-1-P0-CONFIRM-r2.md` is byte-identical to my `CONFIRM-r2.md` (`cmp`).
   - OBJECTS adds four rows and leaves the six earlier rows unchanged.
   - For every new file, the sha256 in its row equals the committed file's sha256:
     - CONFIRM-r2 `f3df43fb…`
     - r3 `b346e46d…`
     - RESPONSE-r1-corrected `da1f53aa…`
     - RESPONSE-r2 `416c3c21…`
   - No lines are substituted.

5. **No new overclaim.**
   - The "Bearing" sentence is now explicitly [W, P0] and conditioned on the scoped result.
   - Restoring C6 narrows the claim's reach. The N3 and table qualifiers narrow it as well.
   - Nothing is stated OI-wide, and the scoped result remains one-direction.
   - The §8 off-`main` gaps are stated correctly: r7 and the review are on the branch but not on
     `main`, so each remains a gap until it lands.
