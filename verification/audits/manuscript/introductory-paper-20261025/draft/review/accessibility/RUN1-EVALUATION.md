## Gate 2 at `2afb5b6a`: comprehension test run 1 — not met

The reader explains five of the six core concepts correctly. Q5 (memory) is only partly right, and the gaps come from the paper's explanation, not the reader. Q1–Q4 and Q6 pass. Four explanation changes are needed before a re-test with a fresh reader; none of them touches a theorem.

I read `QUESTION-SHEET.md` and `RUN1-ANSWERS-2afb5b6a.md` at `9d7d3b6b`, read-only. Line numbers below are the paper at `2afb5b6a`.

### Q1–Q6 verdicts

**Q1, the basic idea: PASS.**
- Correct: the observer is part of a finite world with fixed reversible rules and sees only part of it.
- Correct: the hidden part "can't be reached at all", not merely unknown yet (L35).
- The card game is a correct example of the situation.

**Q2, randomness from hidden information: PASS.**
- Correct: several hidden states sit behind one visible state and lead to different futures, so the randomness is the player's ignorance.
- The 50/50-then-certainty card example and the memory point (L25) are both right.

**Q3, the main result: PASS.**
- The three collections coinciding over a fixed number of steps, in both directions, is correct (Theorem 1, L65–L73).
- The point that the equality covers every pattern, Markov ones included, is made in Q4 ("doesn't pick out anything specific").
- **Scope check — "a single fixed finite world can't reproduce a pattern that never repeats over all time": correct.**
  - A bijection has finite order L, so Γ_{t+L}=Γ_t, which is Main §2.3's proof step. One fixed realization therefore has an L-periodic law.
  - Main §3.4's remark on exact gluing says "a nonperiodic target admits no exact all-time realization by one fixed finite substratum"; the paper says it at L91.
  - The reader's preceding phrase "not forever" is slightly too general, because a periodic law can be reproduced for all time. The reader immediately narrows it to non-repeating patterns, so this is not an error. It does mirror the loose wording at L93 (my gate-1 optional finding 6).

**Q4, what the result does not show: PASS.** Every element of the evaluator note is present:
- fixed-basis records only;
- the squared form built into the definition rather than derived;
- the evolution between two times not selected;
- statistics without a mechanism;
- the five conditions, Theorem 4, that OI does not imply them (the qubit example), and that whether a substratum supplies (iii)–(v) is open.

"Bell-type correlations need H-Bell" is loose but acceptable.

**Q5, memory: PARTIAL.**

What the reader got right:
- the hidden part must store what the record remembers;
- visible memory is a lower bound on hidden memory and gives a minimum hidden size in bits;
- the Pinsker floor;
- the four-condition checklist, and that without feedback there is no memory (the fair coin), which is exactly the evaluator note.

What went wrong:
1. **Only one direction of the equivalence.** The reader gives "memory ⇒ the hidden part stores it" and never the converse (readout-relevant hidden memory in one faithful realization ⇒ M_t>0). They also do not separate readout-relevant memory from plain storage.
   - L97 states only the forward direction. L120 has "exactly when" but in compressed words.
   - Storage versus readout-relevance is stated only in technical form at L122 ("bijective realizations … carry H(X<t|X_t), Markov laws included"). "Must store that information" can therefore be read as "storage means memory".
2. **A scope error in the recurrence part, copied from the paper.** "Any step that isn't fully predictable means chaining fails somewhere in the cycle" drops two hypotheses: the shared hidden prior, and that the forecasts are those from every starting point. It is word for word the L130 gloss, which omits them (my gate-1 required finding 3).
3. **Shared starting odds — this is an accessibility gap, not a reader misunderstanding.** The reader says honestly that they did not follow the condition and does not misuse it.
   - The paper states the condition at L132, L136, L142 and L144, but never says what it means physically: the hidden part is prepared the same way whatever the visible start, so one preparation defines every row.
   - It never says why it is needed.
   - It never says why starting points that never occur are kept. Main §2.3's proof gives the reason: the non-permutation may sit only in the row of a root with probability zero, and the stochastic-inverse lemma needs the full square matrix.

### Q6, the two applications: PASS.

**Cosmological constant.**
- Established and correct: the two levels of description, and that a uniform energy shift changes no observable probability.
- Correctly conditional: the field equations must be derived from the substratum; the remaining vacuum term is not computed; Λ is taken from observation.
- The reader does not name G3, but conveys its content.

**Black holes.**
- Correct: reversibility guarantees preservation, while recovery is a separate question (non-injective maps can recover; full reading recovers; the |𝒰| ≥ |ℳ| floor; the burned-letter analogy).
- Correct: the Page curve rests on H-scramble and H-decouple, which are not established.

Three small imprecisions, none of which reaches a scope error:
- "Many reversible maps" comes from L274's "In many reversible worlds" (my gate-1 optional finding 5). The toy counts carry no weight about prevalence.
- "Scrambling fails for the simple kind of deterministic dynamics described" should be "for every bijection acting on a definite configuration with the bipartition aligned to configurations" (L278, BH-02 C6(a)).
- The constant-energy condition is omitted.

### Q7 and the self-assessment: each reported confusion

| # | Reader's confusion | Passage | Overlap with gate 3 |
|---|---|---|---|
| 1 | §2.5 is dense with qualifiers | L130–L148 | Yes, "density of §2.5" |
| 2 | Why roots of zero probability must be counted | L132, L142, L144 (no reason given) | Partly: inside §2.5's density, but a specific missing *why* (see change 2) |
| 3 | How indivisibility differs from memory; "holds even for memoryless laws" was confusing | L142 and L148 ("Markov on every accessible window") against L144 ("exactly when the record has memory at some step before the return") | Partly. The two statements are never reconciled in plain words. **New**, change 3 |
| 4 | §3.1 three notions; §3.3 "coherent lifts", "right action", "quotient" | L182–L190, L218–L220 | Yes, §3.1 and §3.3 intuition |
| 5 | Bell: coupling graphs, causal cones and H-Bell introduced quickly | L232, L236 | Yes, Bell assumptions |
| 6 | The Page-curve paragraph relies on another paper | L278 | Yes, Page-curve intuition |
| 7 | Detail pushed to companion papers; had to trust the "plain terms" summaries | throughout; §1.2 (L39) | Partly ("expert-only §1.2"). The summaries themselves worked, which is a positive signal |
| 8 | "Why does Theorem 1 matter, if it holds for every pattern and selects nothing?" | L73, L93 | **New, not in the gate-3 list** (change 4) |
| 9 | Self-assessment: "Partly" for both a non-specialist and an undergraduate; formal sections hard going | §§2.5, 3.1–3.5, Page curve | Yes, the same gate-3 items |

### Is gate 2 met at `2afb5b6a`? No

Q5 fails the "correctly explain" standard in two ways: the memory equivalence comes through in one direction only, and the recurrence claim is restated without its hypothesis because the paper's own L130 gloss leaves it out. All four changes below are to explanations only.

**Changes needed before a re-test with a fresh reader:**
1. **L130.** Restore the hypotheses in the forecast gloss (my gate-1 finding 3): "in a finite reversible world whose hidden part starts with the same odds whatever is visible, any visible step that is not fully predictable from the current observation makes chaining fail, for the forecasts from every starting point, somewhere in the world's cycle."
2. **After L134 or within L144: a plain "why" for both conditions.**
   - Shared odds: "the hidden part is prepared the same way whatever is visible at the start, so one preparation defines the forecast from every starting point."
   - Never-occurring starting points: "their rows are kept because the overlap that breaks the chain can sit in such a row; with every starting point possible, nothing is lost by this."
3. **After L144 or at L148: reconcile memoryless windows with memory before the return.** "A record can look memoryless on every window an observer can access and still have memory at some later order before the return; that late memory is what the cycle-wide failure of chaining reflects, and it is invisible to the observer."
4. **At L97/L120 or L122: both directions of the memory result, and storage versus memory.** "Conversely, if any one such world keeps a trace of the past that changes what is seen next, the record has memory. Every reversible world stores its whole past, even for a memoryless record; memory is the part of that store that changes what is seen next."

**Recommended, not blocking:**
- **L73 or L93: say why Theorem 1 matters.** "Because the match is exact for every pattern, no record of one repeated measurement can by itself rule out a partly hidden deterministic account, and the memory results that follow apply to every such quantum record." This keeps "possibility, not fact".
- **L274:** change "In many reversible worlds" to "In some reversible worlds (1,376 of the 40,320 toy maps)".
- **L278:** after "H-scramble", add a plain gloss of when it fails and the single-energy-shell condition.
- The gate-3 items for §§3.1, 3.3 and 3.5, the Page curve, and §1.2 address Q7 items 4–7 and should land before the re-test.
