## Gate 3 focused confirmation: papers/Introduction.md at `40935ccf` (r22)

Read-only. No edits, commits, pushes or comments; the worktree has been removed. Line numbers refer to `papers/Introduction.md` at `40935ccf`, page numbers to the PDF rebuilt there.

**Verdict: ACCEPT WITH CHANGES.** All of my r21 findings are resolved. Four problems remain:
- **Must-fix:** the new plain definition of "hidden predictive memory" (L99) contradicts the paper's own statements at L118 and L122.
- **Should-fix:** the abstract's "So" points at the wrong antecedent (L17).
- **Should-fix:** "least return time" (L142) blurs L with the newly defined return horizon.
- **Should-fix:** L167 repeats a clause.

### Build and typesetting
- **Result:** `sh ./build.sh Introduction` gives 21 pages. The `.tex` is identical to the committed one.
- **Density:** median 3,113 non-space characters per page.
- **Boxes and glyphs:** 0 overfull, 0 underfull, 0 missing characters.
- **Citations:** 52 entries; every key resolves; no orphans.
- **Renders checked:** pp1, 5, 6 and 8.
  - §1 starts on p1, and Theorem 2 sits whole on p6.
  - No stray lists: the only lists are the S/D/Q classes, (i)–(v), the open problems and Appendix A.
  - Italics are intact and every display is within the margins.

### 1. The r21 findings
- **Must-fix 1 (L136): resolved.** "it can happen that the only rows keeping the table from being a permutation belong to starts that never happen" states a possibility, not a restriction.
- **2 (L132/L136): resolved.** "P-divisibility" is now named right after "…so the chain breaks." L136's restatement is cut to a back-reference. §2.5 now reads without a delayed naming. The residual overlap is L136's "a start that never happens still has a row, computed from the same preparation". That is the abstract explanation following the card picture, which is the intended progression, not a duplicate.
- **3, 4, 5, 6, 8 and 9: resolved.** Finding 6 is resolved, but see finding 4 below.
- **7: resolved, with finding 1 below.** The bare "predictive memory" is gone. The record's quantity is "conditional memory" or "memory in the record", and "hidden predictive memory" names I(X_<t;H_t|X_t).

### 2. Abstract (310 words)
It follows the four-part order:
- what OI is: the question, then the OI definition;
- what is established: Theorem 1, memory, recurrence, Theorem 4;
- why it matters: "So stochastic, quantum-like records…";
- what is open: the applications, then "Open are…".

It reads well, except for finding 2. The recurrence sentence is still long (about 75 words) and mixes plain wording ("forecasts from every start") with the undefined "rooted transition matrix" (finding 7).

### 3. The L148 split and the windows sentence
- The three paragraphs (L148, L150, L152) now read cleanly.
- The new sentence is clear: accessible windows are "short compared with the world's least return time L", and that gap is why memory can become detectable only later.
- Two small issues: its "least return time" is finding 3, and its placement is finding 5.

### 4. Terminology
- **Terms that are consistent:** conditional memory, hidden predictive memory, P-divisibility, return horizon and recurrence cycle.
- **Terms that are not:**
  - L itself has three names: "order L", "least return time" (L142, L148) and "recurrence time" (L17, L124, L150; 4 occurrences).
  - The gloss of hidden predictive memory is wrong (finding 1).

### 5. The raw spacing hint (L101)
- **The construct is acceptable in the source.** `\par\vspace{0pt plus 14\baselineskip}\penalty-100\vspace{0pt plus -14\baselineskip}` is the standard package-free conditional break: net zero space when no break is taken, a fill when it is. It uses no package, and the paper builds only to LaTeX.
- **It renders correctly:** Theorem 2 is whole on p6.
- **The cost is a gap of about 8 lines at the foot of p5.** That is visible but tolerable under ragged-bottom layout. Because the hint is conditional, it will not misbehave when the text above moves. It may simply stop being needed, so re-check that page whenever the text above it changes.

### Findings

**Must-fix**

1. **L99: the plain definition of hidden predictive memory is inaccurate.**
   - Current: "The *hidden predictive memory* I(X_<t;H_t|X_t) is the information retained in the hidden state that supports the observed process's dependence on history."
   - Problem: I(X_<t;H_t|X_t) is all the information the hidden state holds about the observed past beyond the present, not only the part that produces dependence on history. The paper says so itself:
     - L122: "bijective realizations run from time 0 carry H(X_<t|X_t), Markov laws included";
     - L118: "every reversible world run from the start stores its whole visible past, even for a memoryless record, and memory is the part of that store that changes what is seen next".
     A Markov law has positive hidden predictive memory in every bijective realization and no dependence on history to support.
   - Proposed: "The *hidden predictive memory* I(X_<t;H_t|X_t) is the information the hidden state holds about the observed past beyond what the observed present tells; the part of it that changes the next observation is what produces the record's dependence on history."
   - The CHANGES record lists this as the owner's wording, so the owner should confirm the correction.

**Should-fix**

2. **L17: the abstract's "So" follows the wrong sentence.** "So stochastic, quantum-like records can arise exactly from deterministic dynamics, and any memory they show must be stored in the hidden part" comes straight after the Theorem 4 sentence, but it follows from Theorem 1 and the memory sentence.
   - Proposed: "Thus, by the first two results, stochastic, quantum-like records can arise exactly from deterministic dynamics, and any memory they show must be stored in the hidden part."

3. **L142 and L148: "least return time" blurs L with the return horizon.**
   - L142 calls L "the least return time" and in the next breath defines a return horizon as any n with Γ_n = I. The visible tables can return to I before the whole configuration does, so the least return horizon can be earlier than L.
   - Proposed for L142: "…for the order L of φ, the recurrence time, the least time after which every configuration has returned. A time n with Γ_n = I is a *return horizon*; L is one, and there may be earlier ones. The horizon {0,…,L} is the *recurrence cycle*:"
   - At L148, use "recurrence time L". Use "recurrence time" throughout, which also matches L17, L124 and L150.

4. **L167: a clause is repeated.**
   - Current: "…still fails to chain somewhere in its full cycle (§2.5), because its visible steps are not fully predictable; that failure lies somewhere in its full cycle, not necessarily on an accessible window."
   - Proposed: "…; that failure need not lie on an accessible window."

**Optional**

5. **L148: the windows sentence sits after the point it explains.** It comes after "An observer confined to accessible windows sees neither." Moving it before that sentence puts the definition ahead of its consequence.
   - "Detectable only later" could also read "can show up only at an order no accessible window reaches", so that it does not seem to contradict "sees neither".

6. **L220: "only make the theory well formed, the well-formedness requirements of any operational theory" repeats itself.**
   - Proposed: "Conditions (i) and (ii) only make the theory well formed; (iii)–(v) are the substantive requirements, which [GR §3.3] calls selection principles."

7. **L17: "rooted transition matrix" is undefined in the abstract.** "Whenever some forecast table from the start is not a permutation" would keep the hypothesis in plain words, if the gate 1 reviewer agrees.

### Regressions against r21
- The L99 gloss is new and wrong (finding 1).
- L167 now repeats a clause (finding 4).
- p5 gains the 8-line gap from the spacing hint.

Nothing else is worse than r21.
