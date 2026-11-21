# REC-1 r3: focused confirmation by the r1/r2 reviewer

**Object.** Draft PR #1268 at exact head `948161723326523b68e08a599a2238871e1f2687`, a single child of
`b39e40ff`. The commit adds four files: `REC-1-r3.md`, `REC-1-NOTES-r3.md`, `REC-1-REVIEW-r2.md` and
`REC-1-RESPONSE-r2.md`. No earlier file changes. I diffed the committed files myself, read-only.

## Verdict: **CONFIRMED for `REC-1-r3.md` and `REC-1-NOTES-r3.md`**

There are two small accuracy fixes, both in `REC-1-RESPONSE-r2.md` (item 5).

1. **RC-r2-1 to RC-r2-5 and both optional suggestions are applied as specified.**
   - RC-r2-1, RC-r2-2, RC-r2-3 and RC-r2-5 match my new texts verbatim. RC-r2-5 covers both the file
     name and the comma.
   - RC-r2-4 is applied in NOTES item 6 with the corrected quantifier order and the Main:580–582
     citation.
   - Optional 1: "[W, REC-1]" now follows "read-side route of N2.1 (OA2:75)".
   - Optional 2: NOTES item 8 quotes OA3:474–475 exactly: "Under held-at-use herald typing that class
     is itself retention-type".

2. **No other change, and the coordinator's additions are accurate.**
   - `REC-1-r2.md`→`REC-1-r3.md` differs only in the title "(r3)", the added Revision sentence, and
     the RC edits above. The Revision sentence correctly names RC-r2-1 to RC-r2-5, two optional
     suggestions, r2 at `b39e40ff` and `REC-1-RESPONSE-r2.md`, which exists at this head.
   - `REC-1-NOTES-r2.md`→`REC-1-NOTES-r3.md` differs only in the title, the companion line "REC-1
     r3", and items 6 and 8.

3. **No new overclaim.** The edits narrow scope (RC-r2-1), remove a size comparison that the source
   does not support (RC-r2-2), add controls and scope to the ordering rule (RC-r2-3), correct a
   quantifier (RC-r2-4) and add a status tag (optional 1). None strengthens a claim. §A.34
   handling, [R]/[R-off] tags, OA-3's finite-ring scope and NL-C's bounded form are untouched.

4. **`REC-1-REVIEW-r2.md` is byte-identical to my `REVIEW-r2.md`** (`cmp`).

5. **`REC-1-RESPONSE-r2.md`: two accuracy fixes (required for that record; r3 itself unaffected).**
   - **5a.** Its last paragraph says "r3 keeps r2's title '(r2)' and its revision line … left to the
     coordinator". The coordinator has since updated both, so the paragraph no longer describes r3.
     Replace it with: "The title and revision line were updated to r3 by the coordinator."
   - **5b.** It cites "`r2-r3.diff` shows the whole change". That file is not in the repository, so
     the reference cannot be resolved from the PR (§A.42 item 2). Replace "`r2-r3.diff` shows the
     whole change" with "`git diff b39e40ff 94816172` shows the whole change".
