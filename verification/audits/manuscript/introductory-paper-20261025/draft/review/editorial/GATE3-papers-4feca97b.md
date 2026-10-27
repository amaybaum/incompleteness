## Gate 3 focused confirmation of #918 r28 (papers/Introduction.md at `4feca97b`)

Read-only: no edits, commits, pushes or comments. The detached worktree used for the rebuild has been removed. Line numbers refer to `papers/Introduction.md` at `4feca97b`; page numbers to the rebuilt PDF.

**Verdict: ACCEPT WITH CHANGES.**
- G1, G2 and G3 answer the reader's questions in plain words and add no new technical term.
- Each of them, though, repeats material already stated nearby, and L130 and L152 are long blocks again (302 and 346 words).
- One clause in G3 slightly overstates (finding 3).
- R reads well.

### Build and typesetting
- **Build:** `sh ./build.sh Introduction` gives 22 pages; p22 now holds 28 lines of references (r27: 13). The `.tex` is identical to the committed one.
- **Compile:** a direct compile has 0 overfull and 0 underfull boxes and 0 missing characters.
- **List:** the (i)–(v) list on p13 renders with italic names, and every item wraps cleanly.
- **Other:** italics and displays are intact. Page tops show no new single-line widows; p14 opens with the §3.3 heading, which is fine. Theorem 2 still breaks after (b), as accepted at r23.

### Findings

**Should-fix**

1. **L130 (G1) is the third statement of the shared-preparation point in one paragraph.** The paragraph already says it in "with the face-down card dealt the same way" and in the merged sentence ("…means something only because the face-down card is dealt the same way …: if the dealer put the opposite colour face down, … not one rule started in two ways").
   - G1's only new content is the reason: a difference between forecasts could otherwise come from the setup rather than the dynamics.
   - Proposed: replace G1 with one clause appended to the merged sentence: "…not one rule started in two ways, and a difference between the two forecasts could then come from how the hidden part was set up rather than from the dynamics."

2. **L140 (G2) says "the rule, not the sample" twice.** It opens with "a result about a rule has to cover every start the rule can be given, not only the starts a particular sample contains" and closes with "dropping those rows would then describe the sample rather than the rule". L130's "not about the starts a sample happens to contain" says it a third time.
   - Proposed: keep the opening sentence and end the next one at "…belong to starts that never happen, as in the different-deck example [Main §2.3]." Then delete "; dropping those rows would then describe the sample rather than the rule".

3. **L152 (G3): the middle restates the result a fourth time, and "rather than of any record" slightly overstates.**
   - **Repetition.** The middle clause ("in a finite reversible world whose hidden part starts with the same odds … no single step-by-step chain … although one may hold on every accessible window") repeats three places:
     - L134's one-sentence result;
     - L150's plain reading;
     - L158 ("holds also for laws that are Markov on every accessible window").
   - **Overstatement.** Under full support the failure is equivalent to conditional memory in the full-cycle record, so it is not independent of every record, only of every *accessible* one.
   - Proposed: "Such a failure is a property of the world's rule, its dynamics with its hidden preparation, rather than of any accessible record: it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]."
   - This also removes the second "as in the example below" in the same paragraph and brings L152 back to about 270 words.

**Optional**

4. **R (L216–L220) reads well.** The GR names (valid probabilities, trivial-ancilla consistency, inert spectators, full reversible control, iterated composition) match GR §3.3, and the plain clause added to (v) ("so that a composite can itself serve as the working system of a larger experiment") helps.
   - "Trivial-ancilla consistency" is the one name a lay reader cannot parse. The plain reading after Theorem 4 ("adding a trivial helper … changes nothing") covers it, so no change is needed.

### Regressions against r27
- L130 and L152 are long blocks again, and all three additions carry repetition (findings 1–3).
- p22 grew from 13 to 28 lines, still within 22 pages.
- Nothing else regressed.
