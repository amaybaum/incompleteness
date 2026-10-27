## Gate 3 focused confirmation: papers/Introduction.md at `366da4bb` (r25)

Read-only. I made no edits, commits, pushes or comments, and the worktree is removed. Cut trials ran on a scratch copy only [local scratch path redacted]. Line numbers are `papers/Introduction.md` at `366da4bb`; page numbers are the PDF rebuilt there.

**Verdict: ACCEPT WITH CHANGES.**
- D and E are accurate, and they now keep the owner's distinctions apart: what is observed, the hypothetical black-start comparison, and the early return against the full recurrence.
- But both paragraphs are too long again. L130 is 494 words and L146 is 389. D also opens with a sentence that repeats the one before it.
- R3 brings back "In plain terms" and has a misleading "do nothing".
- 22 pages cannot be brought back to 21 without removing explanation (section 4).

### 1. Change D (L130)
- **Clarity.** The three distinctions are unmistakable:
  - "What the observer actually sees is red at every step";
  - "part of the mathematical comparison, not something this observer measures";
  - the return at step 2 versus the full return at the recurrence time, step 3.
- **Tightness.** D is not tight enough (findings 1–4).

### 2. Change E (L146)
- **Clarity.** The two cases are clear, and "may detect" and "cannot detect it through this record" are well judged.
- **Flow.** The example's closing sentences fit case 1.
- **Length and overlap.** The paragraph is long again (finding 5). It overlaps twice with nearby text:
  - "An observer confined to accessible windows therefore sees neither…", just before it, says case 2 in advance;
  - its last clause, "what an observer can test is memory at an accessible order, which (C4) asserts", is repeated verbatim at L152.

### 3. R2 (§6, L300) and R3 (L206)
- **R2** reads correctly and matches §3.5. Optionally it could be trimmed (finding 8).
- **R3** has two problems (finding 7).

### 4. Length
- **r25 as built:** 22 pages, with 13 lines on p22.
- **What I tested:** the full tightening package below (findings 1, 3, 4, 5, 6, 8) plus two further trims: removing E's duplicated (C4) clause and compressing L150 "Precisely: …". This saves about 7 body lines without losing any explanation, but the paper stays at 22 pages with 6 lines on p22.
- **Why it stays at 22:** the p19→p20 break before Appendix A absorbs the savings. Reaching 21 would take roughly 15 more body lines, which means cutting explanation or mathematics.
- **Ruled out:** dropping arXiv ids from published references still gives 22 pages. It would also break the "p. 12 of arXiv v3" pinpoint for Bar25, so it should not be done.
- **Recommendation:** apply the tightening for readability and accept 22 pages, under the owner's rule not to sacrifice comprehension to the page count.

### 5. Typesetting
- `sh ./build.sh Introduction` gives 22 pages, and the `.tex` is identical to the committed file.
- A direct compile has 0 overfull and 0 underfull boxes and 0 missing characters.
- Theorem 2 still breaks after (b), with (c) opening p6; this was accepted at r23.
- Lists and italics are intact, and the displays sit within the margins.
- p13 opens with the last line of the §3.2 setup paragraph, "five completion conditions are:", directly above the (i)–(v) list. This is cosmetic.
- L130 renders as a single paragraph of about 30 lines across pp7–8 (finding 2).

### Findings

**Should-fix**

1. **L130: D's first sentence repeats the sentence before it.**
   - Current: "So the comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain; letting the hidden odds change with the start would compare different rules."
   - Problem: the preceding sentence already says the same thing ("…the forecast from red and the forecast from black would describe two different deals, not one rule started in two ways").
   - Proposed: delete it, and open the example with "Why keep a start that never occurs? A different deck and shuffle shows. Suppose its rule makes a red start always show red while a black start, with the same face-down odds, may show either colour, and the dealer always starts with red."
     - "After the first shuffle" is removed from the rule, because the text then says red shows "at every step".

2. **L130 is one block of about 30 lines.** Split it into three paragraphs:
   - (a) weather, the chain break, the P-divisibility naming and the fixed-rule comparison;
   - (b) the never-dealt-start example;
   - (c) "In a finite reversible world whose hidden part starts with the same odds…".

3. **L130: "it overlaps the red one" uses a technical term before it is defined.** "Overlap" is defined only at L136, and the plain reader needs to know what overlaps.
   - Proposed: "After the first shuffle both forecasts give red a positive chance, an overlap that comes only from the start that is never dealt [Main §2.3]."

4. **L130: the closing "so" points to the wrong cause, and "return horizon" is used before L140 defines it.** The failure to chain follows from the overlap and the step-2 return, not from the world completing its cycle at step 3.
   - Proposed: "Both return to certainty at step 2, before the whole world returns at its recurrence time, step 3; so the forecasts fail to chain over the first two steps, although no dealt game ever looks uncertain."

5. **L146: the "sees neither" sentence and case 2 duplicate each other, and the paragraph is too long.**
   - Proposed:
     - Delete "An observer confined to accessible windows therefore sees neither the late dependence nor the failure of chaining." and fold it into case 2: "If it first affects what is seen only beyond every accessible window, an observer confined to accessible windows sees neither the late dependence nor the failure of chaining it implies across the cycle: both remain established under the theorem's hypotheses, but neither appears in any accessible record."
     - Drop case 2's closing "what an observer can test is memory at an accessible order, which (C4) asserts", which L152 already carries with its locator.
     - Start "For example, …" as its own paragraph.
   - "Accessible observational witness" is replaced by "appears in any accessible record", which avoids a near-term to "memory witness".

6. **L136: after D, one clause is redundant.** Remove "; a preparation that depended on the start would give rows for different setups, as in the card comparison above".

7. **L206: R3 has two problems.**
   - Current: "In plain terms, the experimenter can do nothing, combine operations and lump outcomes together, …".
   - Problems:
     - It reintroduces the "In plain terms" label that r20 retired.
     - "can do nothing" reads as "is powerless".
   - Proposed: "That is, the experimenter can always leave the system alone, combine operations, lump outcomes together, prepare an evenly mixed helper, read the helper without disturbing the system, and discard it."

**Optional**

8. **L300: R2 could lose one clause.**
   - Proposed: "Given determinism and an outcome in every run, quantum Bell correlations require giving up ontic parameter independence or measurement independence; with measurement independence retained, they require ontic parameter dependence, whose realization … is the open hypothesis H-Bell (§3.5);".

9. **L150: "Precisely: …" restates the Corollary in full a third time.** If gate 1's explicit-scope rule allows: "Precisely, by the Corollary's full-support equivalence, a law that is Markov on every accessible window and fails to chain on {0,…,L} has M_k>0 at some order k<L beyond the accessible windows."

### Regressions against r24
- L130 and L146 are long blocks again (findings 2 and 5).
- D opens with a redundant sentence (finding 1).
- "In plain terms" is back (finding 7).
- The paper grew from 21 to 22 pages. The cause is D and E's needed content together with the p19→p20 break before Appendix A.

Nothing else regressed.
