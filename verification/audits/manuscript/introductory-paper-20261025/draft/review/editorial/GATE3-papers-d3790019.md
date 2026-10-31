## Gate 3 (narrative quality) re-review: papers/Introduction.md at `d3790019` (r21)

Read-only: I made no edits, commits, pushes or comments, and the worktree has been removed. Line numbers are `papers/Introduction.md` at `d3790019`; the paper is identical at `bfd8b026`. Page numbers refer to the PDF rebuilt there.

**Verdict: ACCEPT WITH CHANGES.** All nine r20 findings are resolved. The new explanatory material is accurate and accessible, but it brings three problems:

- one ambiguous clause that can be read as a false restriction (must-fix);
- a duplicated explanation between L130 and L134;
- two long block paragraphs (L130, L146) and a 385-word abstract.

No theorem or scope surface is affected.

### Build and typesetting
- `sh ./build.sh Introduction` gives 21 pages. The `.tex` is identical to the committed one.
- Median density is 3,154 non-space characters per page.
- The compile has 0 overfull boxes, 0 underfull boxes and 0 missing characters.
- Citations: 52 entries, every key resolves, no orphans.
- I rendered pp5–9 and p12. There are no stray lists, the italics are intact, the displays sit within the margins and no heading is orphaned. Theorem 3 now sits whole on p8.
- Theorem 2 splits across pp5–6: item (a) is at the foot of p5, (b) and (c) are on p6 (finding 11).
- The abstract fills all of p1, so §1 starts on p2 (finding 8).

### 1. The r20 findings
All nine are resolved:

- **Must-fix L230, now L226:** "cannot distinguish two quantum descriptions with trivial ancilla …". Resolved.
- **2, L212:** the reviewer's sentence, which reads well. Resolved.
- **3, L292:** the converse is grammatical and correct. Resolved.
- **4, L134:** "overlap" is defined at first use, and the "for some earlier and later time" scope is added. Resolved, but see findings 1 and 3.
- **5, L126:** the *Theorem 2.* label is present. Resolved.
- **6, L138:** the one-line reason after Theorem 3 is restored. Resolved.
- **7, L200 and L214:** "qubit" is defined at first use, and L218 is merged. Resolved, but see finding 5.
- **8, L284:** the measure-concentration gloss. Resolved.
- **9, L288:** the energy-shell plain wording. Resolved.

### 2. The new explanatory additions
- **Change A, L130 (card comparison).** It is accurate and needs no stochastic matrices. It adds no technical term beyond "anticorrelated", which is explained inline. Two problems:
  - It sits between "so the chain breaks" and "The property that fails is called P-divisibility", so the detour delays naming the property the paragraph was building to.
  - It makes the same point as the abstract middle of L134 (finding 2).
- **L134 rewrite.** It is accurate apart from finding 1, and long (about 250 words). It has the order right: picture (L130), then definition (L132), then explanation (L134).
- **Change B, L146 (four-bit example).** It is correct: M₁ = 0; every deterministic completion keeps X₀ at time 2; M₂ = 1 bit; and the family is P-divisible on {0,1,2}. It is understandable without matrices. But it is embedded in a paragraph of about 400 words that mixes the plain reading, the example, the precise statement and the implications (finding 4).
- **Change C, L161 (XOR sentence).** The first sentence is good. The second introduces an undefined term, "the recurrence horizon" (finding 6).

### 3. The Theorem 4 reading and the (i)–(ii)/(iii)–(v) sentence
- L212 is clear.
- L214 is in the wrong order (finding 5), and "well-formedness requirements" and "substantive selection principles" are new, unglossed terms for a lay reader.

### 4. The optional items applied, and the writer's reasons
- Applied and acceptable:
  - the deletion of r20 L202;
  - the L142 and L146 merges;
  - "So framed" (L27);
  - the [Wei89] figure (L250);
  - the convention note (L41), which reads as a convention, not narration.
- I accept both reasons for what was not applied:
  - L75's first sentence carries attributions, so it stays.
  - The definitions at L184 and L254 stay in the openers. Placing them immediately before the verified paragraphs that use them is a sound way to avoid editing those paragraphs.

### 5. The owner's accessibility objective
- The three-level narrative is continuous in §§1–2.4, §2.6, §3.2–§3.5, §4 and §5, and each of those can be read without Main.
- §2.5 is now the densest stretch: three long paragraphs in sequence (L130, L134, L146).
- The opening question (L17, L23) and the card analogy, marked as an analogy (L23, L163), are intact. The Summary (L292) closes the paper.
- **Length.** 21 pages are justified only partly. About 0.5 page comes from explanations that repeat each other (findings 2, 4 and 8). Removing the repetition loses no explanation.

### Findings

**Must-fix**

1. **L134: the reason for keeping never-occurring rows can be read as a false restriction.**
   - Current: "…and the table may fail to be a permutation only through such a row [Main §2.3]".
   - Problem: it can be read as "can fail to be a permutation only through such rows", that is, only never-occurring starts can break the permutation. That is false. Main's sense is "possibly only through a row of a root of visible probability zero".
   - Proposed: "…and the table can fail to be a permutation in such a row alone [Main §2.3]".

**Should-fix**

2. **L130 and L134 duplicate the explanation of the shared preparation and the never-occurring rows.**
   - L130 gives it in card terms: the dealer always deals red; the anticorrelated deal gives "two different deals, not one rule started in two ways".
   - L134 repeats it abstractly: "If the hidden preparation depended on the visible start, the rows would describe different setups, and a start that never happens would have no preparation to define its row".
   - Proposed: end L130 at "…unavoidable somewhere in the world's cycle". Move the card comparison ("The comparison is between starting conditions … not one rule started in two ways.") to the start of L134's explanation, in place of L134's abstract restatement. Keep L134's independence clause, the overlap definition, the never-occurring-rows reason (fixed as in finding 1) and the "price" sentence.
   - This puts P-divisibility's name directly after the chain-break picture, removes about 5 lines and loses nothing.

3. **L134: the last sentence repeats the Corollary's full-support equivalence.** The equivalence is stated at L142, again at L146 ("Precisely: …") and a third time here.
   - Proposed: keep "The price is that the failure of chaining can then lie only in forecasts that no observer will see", and close with "when every start has positive probability, every row is one that occurs (see the Corollary)."

4. **L146 is about 400 words in one block.** Split it into three paragraphs:
   - (a) memoryless-on-a-window, plus the four-bit example, ending "…it shows no failure of chaining inside it.";
   - (b) "Precisely: …";
   - (c) "Recurrence-cycle indivisibility thus …".
   - In the example, "at time 3 the past predicts the next observation exactly" should read "the past predicts the observation at time 3 exactly".

5. **L214: the sentences are in the wrong order, and two terms are new.**
   - "Which of (iii)–(v) a physical substratum supplies is the open step" comes before the sentence explaining why only (iii)–(v) matter. The closing "Hidden information and partial access therefore do not by themselves imply quantum mechanics" then has no antecedent for "therefore", and repeats "OI alone does not imply quantum mechanics".
   - Proposed: "…so OI alone does not imply quantum mechanics (both machine-checked) [GR §3.3]. Conditions (i) and (ii) only make the theory well formed; (iii)–(v) are the substantive requirements, the selection principles of [GR §3.3]. Which of (iii)–(v) a physical substratum supplies is the open step toward full operational equivalence." Then delete the final sentence.

6. **L161: "the recurrence horizon" is undefined; the term appears nowhere else.**
   - Proposed: "…that failure lies somewhere in its full cycle, not necessarily on an accessible window."

7. **"Predictive memory" has drifted to a second meaning.** It now appears 8 times (L134, L146, L161) for the record's memory M_k. Theorem 2's title, and L120, use "hidden predictive memory" for I(X_<t;H_t|X_t). The paper also says "conditional memory" (8 times) and "accessible memory" (3 times) for the record's memory.
   - Proposed: in the plain passages, use "memory" (or "conditional memory") for M_k, and reserve "predictive memory" for the hidden quantity.

8. **L17: the abstract is 385 words (r20: 305) and fills p1.**
   - It now carries two plain glosses, "Put simply …" and "In plain words: …". The latter brings back the label formula the earlier rounds removed.
   - Proposed: keep "Put simply …". Replace the "In plain words" sentence with the clause "…which every non-deterministic visible step supplies, so that forecasts from the start cannot all be chained step by step somewhere in the world's cycle;". Alternatively, drop it, since §2.5 carries it.
   - Either way, aim for §1 to start on p1 again.

9. **L250: "the mismatch" is used before it is defined at L252.** Proposed: "The question matters because the discrepancy is some 120 orders of magnitude [Wei89]…".

**Optional**

10. **L138:** "can only bring forecasts closer" could read "can never move two forecasts further apart", which matches the contraction exactly.

11. **pp5–6: Theorem 2 splits after item (a).** It will move with the edits above. If it persists, consider a raw `\needspace` or a short `\newpage`-free rewording above it.

12. **L161:** "as in the anticorrelated deal of §2.6" (L130) is a forward reference to an example the reader has not reached. The inline description suffices.

### Regressions against r20
- The abstract grew from 305 to 385 words and now fills p1 (finding 8).
- L130's flow is interrupted (finding 2).
- L146 became a half-page block (finding 4).
- "Predictive memory" drifted (finding 7).
- The length grew from 20 to 21 pages; about 0.5 page of that is repetition (findings 2, 3 and 8).

Nothing else is worse than r20.
