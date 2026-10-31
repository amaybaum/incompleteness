## Gate 3 check: `papers/Introduction.md` at `bace5ef8` (r31)

**Verdict: ACCEPT.** The three edits read well, the layout is clean, and the paper is still 22 pages.

This was read-only: no edits, commits, pushes or comments. The worktree used for the rebuild has been removed. Line numbers are `papers/Introduction.md` at `bace5ef8`.

### The three edits
- **#1 (L300).** "What survives is that conditional statement, with all three conditions." points back clearly to the paragraph's opening sentence ("So if the hidden dynamics scrambles thoroughly, the black hole and its radiation are effectively isolated, and the energy is the same throughout, …"), so all three conditions are carried.
  - The H-scramble requirement now stands as its own sentence and matches GR App. A.7.
  - "Does not depend on any of the three" is accurate.
  - The must-fix is resolved.
- **#2 (L132).** The paragraph now reads "Such a start is not impossible: the world can be started there; the dealer who always deals red simply never does. A different deck and shuffle shows why it still matters."
  - "Preparation" again means only the hidden preparation.
  - The example is now visibly the answer to the question.
- **#3 (L156).** It now reads "a conditional memory that first appears late on the line", which matches the §2.4 term.

### Layout
- `sh ./build.sh Introduction` gives 22 pages, with p22 unchanged at 33 lines. The `.tex` is identical to the committed one.
- A direct compile has 0 overfull and 0 underfull boxes and no missing characters.
- Page tops match r30, so the edits moved no page breaks.
- Theorem 2 still breaks after (b), as accepted at r23.
- There are no widows, and lists, italics and displays are intact.
