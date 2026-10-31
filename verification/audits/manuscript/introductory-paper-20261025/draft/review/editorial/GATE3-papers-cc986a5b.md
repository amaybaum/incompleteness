## Gate 3 check: papers/Introduction.md at `cc986a5b` (r30)

**Verdict: ACCEPT WITH CHANGES.** Of the four edits, the L156 picture and the L152 trim are clean. The L300 sentence states the Page-curve conclusion with only one of its three conditions, which is a must-fix. The L132 sentence uses "preparation" in a second sense and loosens the next sentence's link, which is a should-fix. The layout is clean at 22 pages.

Read-only: no edits, commits, pushes or comments, and the worktree used for the rebuild has been removed. Line numbers are `papers/Introduction.md` at `cc986a5b`.

### Findings

**Must-fix**

1. **L300: the Page-curve conclusion now rests on one condition instead of three.**
   - Current: "What survives is the conditional statement: the cycle-averaged Page value follows once H-scramble holds, which requires an initial superposition of configurations or a split not aligned with them, …"
   - Problem: the paragraph above (L298), the plain reading before this sentence, and §6 all rest the result on three conditions: H-scramble, H-decouple and a single energy shell.
   - The "requires …" clause itself is correct; it matches GR App. A.7 ("it requires an initial superposition of configurations or a bipartition not aligned with them, and which of these the substratum supplies is open").
   - Proposed: "What survives is the conditional statement: the cycle-averaged Page value follows once H-scramble, H-decouple and the single-energy-shell condition hold; H-scramble requires an initial superposition of configurations or a split not aligned with them, and which of these the substratum supplies is open [GR App. A.7]. The separation of conservation from recovery above does not depend on any of them."

**Should-fix**

2. **L132: "preparation" is used in a second sense, and the next sentence loses its object.**
   - Current: "Why keep a start that never occurs? Such a start is not impossible: the world can be started there, and this dealer's preparation simply never does so. A different deck and shuffle shows."
   - Problem: everywhere else in §2.5, "preparation" means the hidden preparation, the hidden prior. Here it means how the visible start is chosen.
   - Problem: with the new sentence in between, "A different deck and shuffle shows" no longer clearly answers the question.
   - Proposed: "Why keep a start that never occurs? Such a start is not impossible: the world can be started there; the dealer who always deals red simply never does. A different deck and shuffle shows why it still matters."

**Clean**

3. **L156 (the picture of orders on a line)** is a good plain image placed right after the precise statement, and it adds no new term.
   - Optional: "a memory that first appears late on the line" could read "a conditional memory that first appears late on the line", for term consistency with §2.4.
4. **L152 (the trim)** now reads "…its dynamics with its hidden preparation: it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]." The repeated "accessible record" is gone.

### Layout
- `sh ./build.sh Introduction` gives 22 pages, with 33 lines of references on p22. The `.tex` is identical to the committed file.
- A direct compile has 0 overfull and 0 underfull boxes and 0 missing characters.
- Theorem 2 still breaks after (b), as accepted at r23.
- Page tops show no new widows, and the lists, italics and displays are intact.
