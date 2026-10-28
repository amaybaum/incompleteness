## Gate 1 (scientific accuracy) review of PR #918 r19 at `2afb5b6a`: ACCEPT WITH CHANGES

All exact statements are unchanged from r18, but three new plain-language glosses say more than their statements and must be fixed (findings 1–3). All three are one-sentence repairs.

I compared r18 (`0ce9cda9`) with r19 word by word; the range includes `61e8e140`. I did not open `QUESTION-SHEET.md`. My worktree and scratch files are removed, and I edited, pushed or commented nothing.

### 1. Exact statements: unchanged
- The paper has only six word-level deletions. All six are insertions of a gloss into an existing sentence, or typesetting (`\sloppy`→`\raggedright`, the `C\*` escape in [Sti55], the Appendix A font group).
- Line for line, these are identical to r18:
  - Theorems 1–4, the recurrence Corollary, the definition of Γ_t;
  - §4's "What OI establishes", "The proposed resolution" and "The missing link";
  - §5's "Results" and "The Page curve";
  - the Bell theorem paragraph, §6's "Established" and "Conditional" paragraphs, and the independence paragraph.
- The Bell framework paragraph gains only the two definitions (ontic parameter independence, measurement independence), which are correct.
- Apart from the added opening question, the abstract is byte-identical to r18. The recurrence scope in the abstract, §2.5 and §6 is therefore unchanged and still identical.
- The §2.4 Corollary is byte-identical (`b596be8a…`).
- In `LEDGER.json` only the `line` fields changed; no fingerprint changed. `coverage_check` reports OK (134 statements).

### 2. Glosses and analogies
**Correct:**
- **Card analogy (L23, L25, L161).** It is explicitly labelled "an analogy … proves nothing about quantum mechanics, and every result below is stated and proved without it", and the paper says its statistics are classical. It does not suggest that OI derives quantum mechanics.
- **Memory without readback (L126).** "Coupling, persistence and capacity without readback produce no memory" holds: (C4) is equivalent to M_t>0, and Main's fair-coin realization has (C1)–(C3) with zero memory.
- **Correspondence never glossed as explaining or deriving.** L73 says "possibility, not of fact"; L93; L178 says "represents the statistics without deriving a physical mechanism"; L214.
- **Bell (L230, L234, L236).** Determinism, the no-influence condition from (ii) and (iii), the independent settings of (iv), and the ±1 outcome every run are all kept. L238 is a correct Bell consequence under determinism and measurement independence.
- **Cosmological constant (L242, L248).** "That gravity responds only to the underlying world is the proposal below, and deciding it requires the field equations" keeps decoupling conditional on G3.
- **Black holes (L268, L274, L276, and §5's Page paragraph).** H-scramble and H-decouple stay open, and A.7's limits are as fixed in r18.
- **Other new glosses:**
  - the bijection; the stochastic and permutation matrices;
  - total variation (largest event difference; 1 iff disjoint supports); the conditional-mutual-information gloss;
  - Markov ⇔ M_t=0 for every t; the readings of Theorem 2(a)–(c);
  - the reading of the §2.4 Corollary (L120), which matches it;
  - the clock-and-sequence construction (`S_imp_D`); the Hadamard gloss;
  - the Theorem 4 reading; Planck cutoff; stress-energy; the Page curve;
  - the §6 Summary.
- **Scenarios.**
  - The face-down card and the two laboratories are apt.
  - The weather forecast correctly illustrates chaining transition tables from the start.
  - The vacuum jitter is the zero-point energy.
  - The burned letter is the standard unitarity analogy and is labelled as one.

### 3. Einstein attribution: adequate
The paper says "usually paraphrased as 'God does not play dice'". That is accurate. The source is Einstein to Born, 4 December 1926: "Jedenfalls bin ich überzeugt, daß der nicht würfelt" ("I, at any rate, am convinced that He does not throw dice"). The words "usually paraphrased" hedge it enough without a citation. Citing the Born–Einstein letter would be optional.

### 4. L214 "yield" → "imply": correct
"Hidden information and partial access therefore do not by themselves imply quantum mechanics" is exactly `oi_alone_not_qm`, together with the independence result in `five_way_minimality`.

### 5. The six comprehension points: each stated correctly
| Point | Where |
|---|---|
| What OI means | L17, L35 |
| Deterministic dynamics producing apparent randomness | L23–L27, L79 |
| What the correspondence establishes | L65, L73 |
| Why the correspondence alone does not derive QM | L178, L214, L282 |
| The memory results | L97, L114, L120, L126 |
| Why the applications matter | L242, L268, and the last sentence of L282 |

### Findings
1. **L226 — required (quantifier error, overclaim).** "one fixed finite hidden world can mimic any single finite pattern" reads as one world for all patterns. Theorem 1 chooses the world per pattern, and §3.4 says so.
   - Replace with: "for any single finite pattern some finite hidden world reproduces it, but no one fixed finite hidden world reproduces everything one qubit can do across all possible experiments, which would need unlimited hidden memory."
2. **L238 — required (understates what is open).** "whether the lattice substratum can meet that condition is open" makes no-signalling look like the only open item. H-Bell (Main §3.3) asks whether a preparation-indexed coupling graph can supply the remote dependence at all, without signalling, and while preserving the gravitational continuum limit. L236 states this correctly.
   - Replace with: "whether a coupling graph on the lattice substratum can supply that dependence without any usable signal and while keeping the gravitational continuum limit is open (H-Bell)."
3. **L130 — required (the gloss drops a hypothesis).** "in a finite reversible world with any visible step that is not fully predictable its failure is unavoidable somewhere in the world's cycle" omits two things the Corollary has:
   - the hidden odds shared by every starting state, which L144 and the L282 Summary both include;
   - that the forecasts are those from every starting point.
   - Replace with: "in a finite reversible world whose hidden part starts with the same odds whatever is visible, any visible step that is not fully predictable from the current observation makes its failure, for the forecasts from every starting point, unavoidable somewhere in the world's cycle."
4. **L144 — optional.** "as they do after any visible step that is not fully predictable" places the overlap right after that step. Main only gives some s ≤ min(k, L−1).
   - Suggest: "as happens at some time whenever a visible step is not fully predictable from the current observation".
5. **L274 — optional.** "In many reversible worlds" implies prevalence. BH-01 says its counts are counting measure on a finite family and "carry no physical weight".
   - Suggest: "In some reversible worlds (1,376 of the 40,320 toy bijections)".
6. **L93 — optional.** "one such world reproduces a pattern over a chosen finite stretch of time, not forever" should read "not, in general, forever". Only nonperiodic laws lack an all-time realization (§2.3).
7. **L230 — optional (§A.32).** "this is the sharpest test of what partial access can and cannot explain" is an evaluative judgement. Suggest "a direct test".
8. **L25 — optional.** "Nothing random happened" should read "Nothing random happened after the deal", since the face-down card is dealt uniformly.
9. **L208 — optional.** "helpers can be added and discarded freely" glosses (v), which is specifically a fresh uniformly prepared ancilla on a composite, acting, then discarded. Suggest "a fresh, evenly mixed helper can be added to any combined system, used and discarded".

### Answers to the owner's two questions
- **(a) Is every claim and explanation supported by its stated evidence and assumptions?** Every exact statement is supported. Every explanation is too, except the three required glosses at L226, L238 and L130.
- **(b) Do the paper and its explanations convey the strongest established results without weakening them?** Yes. No theorem is weakened, and the glosses state Theorems 1–4, the memory results, the recurrence Corollary (including the full-support equivalence at L144) and the applications at proved strength. Two optional notes: L238 understates what is open rather than weakening a result (finding 2), and the §6 Summary leaves out the full-support equivalence, which is acceptable for a summary.
