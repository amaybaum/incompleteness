## Gate 3 focused confirmation: papers/Introduction.md at `90705d41` (r26)

This was read-only: I made no edits, commits, pushes or comments, and I removed the detached worktree after the rebuild. Line numbers are `papers/Introduction.md` at `90705d41`; page numbers refer to the rebuilt PDF.

**Verdict: ACCEPT WITH CHANGES.** All eight r25 findings are resolved and there are no regressions. One should-fix remains: in the merged sentence for finding 1, the fixed-rule point is still made twice within three sentences (L130). The rest is optional.

### 1. The r25 findings
- **#1, L130:** resolved in substance. The merged sentence reads well on its own ("The comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain, and it means something only because …"). It does, however, sit two sentences after "It compares starting conditions under one fixed rule.", which says the same thing (finding 1 below).
- **#2:** resolved. L130 is now three paragraphs (L130, L132, L134).
- **#3:** resolved. At L132, "After the first shuffle both forecasts give red a positive chance, an overlap that comes only from the start that is never dealt" says what overlaps at its first use.
- **#4:** resolved. The causal chain is stated correctly: the step-1 overlap together with the step-2 return, "not from the step-3 recurrence". "Return horizon" is no longer used before its definition.
- **#5:** resolved. Case 2 now carries the "sees neither" point and names both objects. The example is its own paragraph (L152).
- **#6:** resolved at L138.
- **#7:** resolved at L212. There is no label, "always leave the system alone" replaces "do nothing", and gate 1's O2 ("act after preparing it") is included.
- **#8:** resolved at L306, which reads cleanly.
- **Not applied, with a sound reason:** my optional L154 ("Precisely: …"), under the owner's explicit-scope rule.

### 2. The split paragraphs
- **§2.5 runs in a logical order.**
  - L130 gives the chain picture, names P-divisibility and sets out the fixed-rule comparison.
  - L132 asks "Why keep a start that never occurs?" and answers with a worked rule. It separates the actual observation, the hypothetical comparison and the two kinds of return.
  - L134 states the general result in one sentence.
- **The additions are tight**, apart from finding 1.
- **L150 and L152 are readable and free of duplication.** The two cases come before the example, and the example closes with its detection sentence.

### 3. Terms
- "Overlap" is glossed at its first use (L132) and defined formally at L138.
- "Rooted family" is glossed as "the table of forecasts from every start" at L132.
- "Return horizon" is first used at its definition (L144).
- No undefined term was introduced.

### 4. Typesetting
- `sh ./build.sh Introduction` gives 22 pages, which the owner accepts. The `.tex` is identical to the committed file.
- A direct compile reports 0 overfull boxes, 0 underfull boxes and 0 missing characters.
- **Page breaks:**
  - Theorem 2 still breaks after (b), with (c) opening p6; this was accepted at r23.
  - The p13 list lead-in now sits with its list: "…and discard it. The five completion conditions are:" opens p13 directly above (i)–(v).
  - The recurrence Corollary breaks across pp8–9 mid-statement (finding 4).
- Lists, italics and displays are intact.
- No new single-line widows at page tops.
- A scratch trial of further trims showed that tightening elsewhere would not bring the length back to 21 pages. The p19→p20 break before Appendix A absorbs savings of this size.

### Findings

**Should-fix**

1. **L130: the fixed-rule point is made twice in three sentences.**
   - Current: "…P-divisibility: whether the forecasts from the start admit step-by-step intermediate forecasts over the interval in question. It compares starting conditions under one fixed rule. Suppose the dealer always deals red face up, … The comparison is about one fixed rule, …"
   - Proposed: delete "It compares starting conditions under one fixed rule." The merged sentence, which the owner kept, carries the point, and "Suppose the dealer always deals red face up …" follows the naming directly.

**Optional**

2. **L138 is 278 words in one paragraph.** Proposed: split it before "The step from two observed histories with a common endpoint to an *overlap* …". The first half then covers the plain definition, the root and the shared prior; the second covers the overlap step, the never-occurring rows and the price.
3. **L154 opens with "Precisely:" right after an example paragraph.** It reads better as "Stated precisely: …", which marks the return from the example to the general statement without changing its scope.
4. **pp8–9: the recurrence Corollary breaks across the page.** This is cosmetic and will move with edits; no source-level action is needed.

### Regressions against r25
None.
