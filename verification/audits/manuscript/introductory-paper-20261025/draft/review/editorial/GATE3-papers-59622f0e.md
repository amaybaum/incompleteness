## Gate 3 check: papers/Introduction.md at `59622f0e` (r27)

**Verdict: ACCEPT.** The three edits read well, the layout has not regressed, and the paper is still 22 pages.

This was read-only: no edits, commits, pushes or comments. The detached worktree used for the rebuild has been removed. Line numbers refer to `papers/Introduction.md` at `59622f0e`.

### The three edits
`git diff 90705d41 59622f0e -- papers/Introduction.md` touches exactly these three sites:

- **Should-fix #1 (L130).** "It compares starting conditions under one fixed rule." is deleted. The naming of P-divisibility now leads straight into "Suppose the dealer always deals red face up …", and the fixed-rule point is made once, in the merged sentence the owner kept. There is no repetition left.
- **Optional #2 (former L138).** The paragraph is split before "The step from two observed histories with a common endpoint to an *overlap* …".
  - The first half covers the plain definition, the root and the shared prior, ending "…computed from the same preparation."
  - The second covers the overlap, the never-occurring rows and the price.
  - The text of both halves is unchanged, and each reads cleanly.
- **Optional #3.** "Precisely:" is now "Stated precisely:". This marks the return from the example to the general statement, and the scope wording is unchanged.

### Layout
- **Build:** `sh ./build.sh Introduction` gives 22 pages, and p22 holds the same 13 lines of references as r26. The `.tex` is identical to the committed file.
- **Compile log:** a direct compile shows 0 overfull and 0 underfull boxes and 0 missing characters.
- **Page breaks:** page tops match r26 except p9 and p10, which each move by one line.
  - Theorem 2 still breaks after (b), as accepted at r23.
  - The recurrence Corollary still breaks across pp8–9. This is cosmetic and unchanged; optional #4 was not applied, as intended.
- **Other:** the p13 list lead-in still sits with its list. Lists, italics and displays are intact, and there are no new widows.
