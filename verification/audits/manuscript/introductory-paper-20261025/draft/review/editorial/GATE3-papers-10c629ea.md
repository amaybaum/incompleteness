## Gate 3 (narrative quality) re-review: papers/Introduction.md at `10c629ea` (r20)

Read-only. I made no edits, commits, pushes or comments, and the worktree has been removed. Line numbers refer to `papers/Introduction.md` at `10c629ea`; page numbers to the PDF rebuilt there.

**Verdict: ACCEPT WITH CHANGES.** Both r19 must-fixes are resolved, and the four-step narrative now holds in every section. One new must-fix remains: a plain-language sentence in §3.3 that can be read as saying the opposite of the result. The should-fixes are local.

### Build and typesetting
- **Result:** `sh ./build.sh Introduction` gives 20 pages, and the `.tex` is identical to the committed file.
  - Density: median 3,142 non-space characters per page.
  - Boxes and glyphs: 0 overfull, 0 underfull, 0 missing characters.
  - The main text ends on p18; the code note and Appendix A are on p18, and the references on pp19–20.
- **Pages rendered:** 6, 7, 8, 11, 12 and 15.
  - L126, "Part (b)…", now sets as prose (p7).
  - No stray list items remain: the only enumerations are (i)–(v) and the open problems.
  - No broken italics, no orphaned headings, and the displays sit within the margins.
- **Citations:** 52 entries, every key resolves, no orphans.

### 1. The r19 must-fixes
- **L112 list defect: resolved.** It is now L126, "**Proofs and sources.** Part (b)…", and renders as prose.
- **Theorem 4 scope: resolved at L200, L214 and L296.** Each now reads "for an operational theory with the structure of §3.2 on a nonempty finite system … exactly the normalized finite Kraus instruments if and only if (i)–(v)". "The rest/whole of quantum mechanics" is gone, and L37, L180(3) and L218 are consistent with that.
  - *Optional:* the abstract keeps r18's "Exact finite operational quantum mechanics is characterized by five completion conditions". That is acceptable abstract compression; adding "for an operational theory with the stated structure" would carry the scope there too.

### 2. The r19 should-fixes
- **Applied:**
  - §1.1 order: "bijection" is defined at L29 before its use at L31.
  - §1.2 roadmap: L37 is plain and its claims are unchanged.
  - Intuition openers: §2.3 (L85), §3.1 (L184), §3.3 (L224), §3.4 (L234), §2.6 (L154, L161).
  - Card CP reading: L194.
  - Page-curve plain reading: L292.
  - Clarity fixes: (a) L25, (b) L130, (c) L112, (d) L180, (e) L286.
  - Terms defined at first use: Markov, realization, order, recurrence (L49); amplitude (L59); coherence (L200); wing and pre-setting variable (L242); emergent, stress-energy, Hubble-scale density, de Sitter entropy (L254); energy shell, orbit ensemble, bipartition, measure concentration (L288).
  - Voice: the three neutralizations.
  - "In plain terms": none left; "So" and "That is" now vary the opening.
- **Not applied, with sound reasons:** none. The moved blocks are byte-verified.

### 3. Narrative and accessibility
- **The progression is present in every section.** Each runs question, then picture, then statement, then plain reading, then implications. The opening question (L17, L23) and the card analogy, marked as an analogy (L23, L163), are intact. The Summary (L296) closes the paper and answers the opening question.
- **Self-containedness:** each section is understandable without Main except §3.1's card-CP paragraph (L192: Pauli twirl, σ_o). L194 makes it followable without Main all the same.
- **The "Proofs and sources" split reads naturally overall.** It fragments the argument in two places (findings 5 and 6).

### Findings

**Must-fix**

1. **L230: the plain reading can be read backwards.**
   - Current: "So the fixed-basis records identify every two quantum descriptions that agree on everything visible…".
   - Problem: "identify" can be read as "determine", which is the opposite of the result (the records cannot tell such descriptions apart).
   - Proposed: "So the fixed-basis records cannot distinguish two quantum descriptions that agree on everything visible, and choosing the evolution between two times needs a principle that the records do not supply."

**Should-fix**

2. **L214: the plain reading of Theorem 4 has become hard to follow.** This is a regression from r19. The sentence runs to about 90 words, says "exactly" twice, and ends on a dangling "; no more and no less is obtained".
   - Proposed: "That is, for a theory with the structure above, the operations available on a nonempty finite system, with any finite helper attached, are exactly the quantum ones (the normalized finite Kraus instruments) if and only if five requirements hold: probabilities make sense; adding a trivial helper or an untouched bystander changes nothing; every reversible quantum operation on any combined system is available; and a fresh, evenly mixed helper can be added to any combined system, used and discarded."

3. **L296, Summary: the new converse clause is garbled.**
   - Current: "conversely, memory held in the hidden part of any one such world that changes what is seen next means the record has memory".
   - Proposed: "conversely, if the hidden part of any one such world holds a trace of the past that changes what is seen next, the record has memory".

4. **L134: "overlap" is used before it is introduced.** L134 says "the step from two histories with a common endpoint to an overlap rests on this independence", but overlap is defined only in Theorem 3 (L136).
   - Proposed: "…to an overlap (two rows sharing a positive entry, Theorem 3)…".
   - Also in L134: "when it fails, no stochastic map carries an earlier rooted transition matrix to a later one" should read "when it fails, for some earlier and later time no stochastic map carries the earlier rooted transition matrix to the later one".

5. **L126: the §2.4 "Proofs and sources" paragraph does not name its theorem.** It sits about a page after Theorem 2, so "Part (b)…" has no visible referent.
   - Proposed: "**Proofs and sources.** *Theorem 2.* Part (b)…", matching §2.5's labels at L148/L150.

6. **§2.5: Theorem 3 has lost its one-line reason.** The reason ("two such rows are at total-variation distance below 1 at time s and exactly 1 at time n, which the contraction criterion forbids") moved to L148. Theorem 3 (L136) is now followed directly by the Corollary.
   - Proposed: one sentence after L136, for example: "A step-by-step forecast can only bring forecasts closer, so two forecasts that overlap at time s can never become the two distinct certainties of Γ_n = I."
   - L148 keeps the full source paragraph.

7. **L218: "qubit" is defined after its use at L216** ("a qubit theory"). Move the definition into the L200 opener.
   - L218's first sentence also restates L216. Merging them saves about 2 lines.

8. **L288: the gloss for measure concentration is near-circular.**
   - Current: "almost every state is close to typical".
   - Proposed: "in very large state spaces almost every state gives nearly the same value of a smooth quantity such as the entanglement entropy".

9. **L292: one condition is ambiguous in plain words.** "does not have the same energy throughout" can be read as being about time.
   - Proposed: "…and for an evaporating black hole whose radiation carries away its energy, not every configuration of black hole and radiation has the same energy."

**Optional**

10. **Length: 20 pages are justified by explanation.** Tightening that loses no explanation and touches no mathematics comes to about 0.5–0.7 page:
    - delete L202, which repeats L180 and L200 (3 lines);
    - merge L216 and L218 (finding 7);
    - drop L142's last sentence, already given at L134 and L144 (3 lines);
    - fold L146 into the end of L144 (2 lines);
    - drop L75's first sentence, which duplicates L73's picture (2 lines);
    - in L298, replace the fourth verbatim copy of the rooted scope with "(§2.5, with its scope)", if gate 1 permits.
11. **Openers that read as glossaries.** L184 (§3.1) and L254 (§4) stack definitions in the opener. Defining each term in the sentence that first uses it would read more continuously.
12. **Repeated phrasing:** "Put simply" (L17) and "Put this way" (L27).
13. **L254:** "this is the largest known mismatch between a theoretical estimate and an observation" is uncited folklore. Either "a mismatch of some 120 orders of magnitude [Wei89]" or a citation would fix it.
14. **Page break, pp7–8:** Theorem 3's head line sits at the foot of p7 and its statement continues on p8. Minor; it will move with any edit above.
15. **Proofs-and-sources labelling:** §§3.1, 3.3–3.5, 4 and 5 keep their evidence classes inline, while §§2.2, 2.4, 2.5 and 3.2 use the label. Inline is fine where the notes are short; stating this as the convention would make the difference read as deliberate.

### Regressions against r19
- L214 is less readable (finding 2).
- The Theorem 3 reason has moved away from the theorem (finding 6).
- The §2.4 source paragraph is detached from Theorem 2 (finding 5).
- Length grew from 18 to 20 pages, attributable to the explanatory additions.

Nothing else is worse than r19.
