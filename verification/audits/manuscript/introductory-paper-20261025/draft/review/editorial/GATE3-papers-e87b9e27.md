## Gate 3 focused confirmation: `papers/Introduction.md` at `e87b9e27` (r23)

Read-only: I made no edits, commits, pushes or comments, and the worktree has been removed. Line numbers are `papers/Introduction.md` at `e87b9e27`; page numbers are the PDF rebuilt there.

**Verdict: ACCEPT.** All four r22 findings (must-fix 1, should-fixes 2–4) and the three optional items are resolved. Nothing has regressed. The findings below are optional wording and typesetting polish.

### Build and typesetting
- **Build:** `sh ./build.sh Introduction` gives 21 pages, and the `.tex` is identical to the committed file.
- **Density:** median 3,195 non-space characters per page.
- **Boxes and glyphs:** 0 overfull boxes, 0 underfull boxes, 0 missing characters.
- **Source:** the Markdown contains no raw `\vspace`, `\penalty` or `\nopagebreak`.
- **Citations:** 52 entries; every key resolves and there are no orphans.
- **Lists, italics and displays:** the only lists are the S/D/Q classes, (i)–(v), the open problems and Appendix A. Italics are intact, and every display sits within the margins, including the Γ matrices, which are whole on p9.

### 1. The r22 findings
- **Must-fix 1, L99:** resolved. "The hidden predictive memory … is the information the hidden state holds about the observed past beyond what the observed present tells; it is at least the conditional memory (Theorem 2(c)), and only part of it need affect what is seen next." This is accurate and consistent with L118 and L120. The owner's gloss now sits at L118, on the readout-relevant part, which is where it is correct.
- **Should-fix 2, abstract:** resolved. "…can therefore arise…" now follows the memory sentence it depends on.
- **Should-fix 3, L49 and L140:** resolved. "Recurrence time" is used for L throughout, at all 7 sites, and "least return time" no longer appears. The return horizon is now stated not to coincide with L ("L is one, and there may be earlier ones").
- **Should-fix 4, L165:** resolved.

### 2. The optional items applied
- **5, L146:** applied. The windows sentence now precedes "sees neither" and reads clearly: "…leaves room for conditional memory that no accessible window detects…".
- **6, L218:** applied, and clean.
- **7, abstract:** applied. "whenever some table of forecasts from the start is not a permutation" carries the same scope in plain words.

### 3. Readability
- The recurrence-time and return-horizon definitions and the L118 gloss read naturally in place. Three small wording points remain (findings 1–3).
- **Theorem 2's page break** (pp5–6) is acceptable. The header, (a) and the (b) display are on p5, and only the one-line (c) opens p6; there is no gap.
  - I see no reliable prose-only fix. Any trim above shifts the break point within the theorem rather than moving the whole theorem, which matches the writer's three failed trials.
  - The one candidate trim would remove explanation: L99's "A law is *Markov*, that is memoryless, exactly when M_t=0 at every t." restates L49's plain definition in exact form.

### Findings (all optional)

1. **L49: the order and the recurrence time are defined twice in one sentence.**
   - Current: "its *order* L is the least number of steps after which every configuration has returned to itself, one such return is a *recurrence*, and L is the world's *recurrence time*, the least time after which the whole world returns to its starting configuration".
   - Proposed: "its *order* L, the world's *recurrence time*, is the least number of steps after which every configuration has returned to itself, and one such return is a *recurrence*".

2. **L140: "only" can be misread.**
   - Current: "at which only the forecasts from the start return to certainty".
   - Problem: it can be read as "the forecasts from the start, and no others".
   - Proposed: "at which the forecasts from the start return to certainty, though the whole world need not yet have returned".

3. **L146 and L118: two small antecedent and term points.**
   - At L146, "An observer confined to accessible windows sees neither." now sits two sentences after its antecedents. Proposed: "…therefore sees neither the late dependence nor the failure of chaining."
   - At L118, "the part of the hidden memory" introduces a fourth name. Proposed: "the part of the hidden predictive memory".

4. **pp13–14: two single-line widows open pages.** p13 opens with "open step toward full operational equivalence." and p14 with "need unlimited hidden memory." Both are cosmetic and will move with any edit. Raising `\widowpenalty` would have to go in the shared header, which this paper should not change, so leave it.

### Regressions against r22
None. Removing the spacing hint also removed the p5 gap.
