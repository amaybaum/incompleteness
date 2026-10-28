## Gate 2 at `bace5ef8`: comprehension test run 6 (preregistered) — not met

Under the preregistered rule the gate is **NOT MET**, on one item only: Q5 part (c) is PARTIAL. Everything else passes, including both direct questions, 5a and 5b, which pass cleanly on the preregistered criteria for the first time in six runs. Q1–Q4, Q6 and the Q5 memory results also pass.

The diagnosis for (c) is given first, as the owner asked. Proposed changes are listed separately at the end, each checked against the theorem's hypotheses.

**Provenance.**
- I read `RUN6-PREREGISTRATION.md`, `RUN6-ANSWERS-bace5ef8.md`, `QUESTION-SHEET.md` and `RUN5-EVALUATION.md` at `17dd25e9`, read-only.
- The preregistration was committed at `d1368bf0`, an ancestor of `17dd25e9`, and is unchanged since.
- The paper at `17dd25e9` is identical to `bace5ef8`. Line numbers below are the paper at `bace5ef8`.
- I applied the preregistered criteria exactly.

### Verdicts

**Q1, the basic idea: PASS.**
- Correct: "the 'hidden' part, is not just unknown for now; it is out of the observer's reach in principle" (L33).
- The card-game situation is also correct.

**Q2, randomness from hidden information: PASS.**
- Correct: "one visible state can sit alongside several possible hidden states, and those hidden states lead to different futures … The randomness is the observer's uncertainty about the hidden part" (L29).
- Correct own example: the vending machine with an unseen counter.

**Q3, the main result: PASS.**
- The three sets are the same over a fixed number of steps.
- The tape-plus-clock construction is correct (L73).
- "no record of one repeated measurement can, by itself, rule out a hidden-deterministic account" is correct (L93).
- "A non-periodic pattern therefore can't be reproduced forever by one fixed finite world" is correct (L91).

**Q4, what the result does not show: PASS.**
- Every element of the evaluator note is present:
  - possibility, not nature;
  - one fixed measurement only;
  - the squared rule "built into the definition … the permutation-type evolutions used give the same answer for any power";
  - the evolution between times not selected;
  - representation, not mechanism;
  - five conditions "necessary and sufficient", not implied by the hypothesis, with the qubit theory without coherence;
  - (iii)–(v) open.
- "Necessary and sufficient" is stated without the "operational theory with the stated structure" qualifier. In context this is acceptable compression, not a scope error.

**Q5, memory results: PASS.**
- Correct:
  - the forward and converse directions;
  - "The visible memory can never exceed the hidden memory, and that can never exceed the hidden part's capacity in bits";
  - the size and minimum-memory bounds and the floor;
  - storage versus memory;
  - C1–C4 as "influence what is seen, keep its records, have room for them, and feed them back within the time the observer can see".

**Q5 part (c), established but unobservable beyond every accessible window: PARTIAL.**
- Q5 itself does not address it.
- Q7 reaches the paper's intended conclusion: "the failure may lie only in forecasts of starts that never occur, or beyond any window anyone can see, so it seemed more a statement about the model than about data". That matches L152: "it constrains how such a world can be described, not what accessible data will show".
- But the answer gives no reason why such an effect is unobservable although the mathematics establishes it. It does not separate this from the case of a later step that some window reaches.
- Q7 also names "the corollary's interplay of accessible windows, recurrence time and memory at some order below it" as hard.

**Q5a, the shared hidden preparation: PASS** (preregistered PASS criterion).
- The answer gives the full reason: "The comparison is meant to tell you something about the world's rule, meaning its dynamics run forward from different visible starts. That only works if everything else is held fixed. If the hidden part were prepared differently depending on the start, the forecasts from two starts would differ partly because of the different preparations, and you couldn't attribute the difference to the dynamics."
- It also gives the card contrast ("two different deals, not one rule started in two ways").
- Enabling passages:
  - L130, G1 (r28): "A forecast from a start is a forecast of what the rule does only if the hidden part is set up by the same procedure every time; if the procedure changed with the start, a difference between two forecasts could come from the setup rather than from the dynamics."
  - L130's contrast: "two different deals, not one rule started in two ways".
- The reader explained the point in its own words rather than restating it.

**Q5b, never-occurring starts: PASS** (preregistered PASS criterion: any two of the three points, with a reason). The answer gives all three:
- Rule over sample: "a rule has to say what happens from every start it could be given, not only from the starts that happen to show up in a given sample". Enabled by L140, G2.
- Possible, not impossible: "A start that never occurs isn't impossible; the dealer just never chooses it". Enabled by L132, H1 (r30).
- The evidence may come only from such a start: "the only thing that stops chaining is an overlap with forecasts from a start that is never dealt, even though the observed game never looks uncertain". Enabled by the different-deck example at L132.
- It also adds the correct full-support consequence: "If every start actually has positive probability … the failure becomes equivalent to having memory at some order before the world's return time".
- The reader explained the points with reasons.

**Q6, the two applications: PASS.**
- Cosmological constant: established and open are stated correctly, with Λ taken from observation.
- Black holes:
  - conservation and recovery are separated;
  - the counts and the secret-sharing-like floor are correct;
  - the Page curve "derived only under three conditions", with each condition's status and "So that part stays conditional and open". This reflects R-Page as fixed in r31 (L300).
- "for any reversible map acting on definite configurations with the natural split" is an acceptable paraphrase of L300.

### Diagnosis (preregistered) for the one PARTIAL

**Q5 part (c): deeper conceptual obstacle, mild, compounded by an instrument gap.**
- The paper states the reason correctly and plainly:
  - L152: "Accessible windows are, by definition, short compared with the world's recurrence time L … a trace held in the hidden part can first affect what is seen at an order beyond every accessible window … neither appears in any accessible record";
  - L152: "it constrains how such a world can be described, not what accessible data will show";
  - L156: the "long line" picture.
- The reader reconstructs the conclusion but not the reason, and does not separate the two cases. The reader names the "interplay of accessible windows, recurrence time and memory at some order below it" as the obstacle.
- **Not ambiguous wording.** The reader's one statement on the point is the paper's own correct reading.
- **No premise is missing.** All the steps are stated: windows are short, k can lie anywhere below L, and data are window statistics.
- **Instrument caveat, stated as evidence.** Unlike 5a and 5b, part (c) is not asked directly. The reader's only engagement with it comes unprompted in Q7, and phrased as a doubt about the result's value.
  - This is the same situation that runs 1–5 had for (a) and (b).
  - When (a) and (b) were asked directly in run 6, they passed.

### Q7 points, classified

| Point | Passage | Classification |
|---|---|---|
| "not confident about what the 'different deck' example's rule actually is" | L132: the rule is given only through its forecasts ("makes a red start always show red while a black start … may show either colour") | **Recommended** (wording). 5b passed using exactly this example, so it served its purpose. |
| "had to guess what the 'routed form' of C4 means" | L162, the Corollary's *Proofs and sources*: "the *routed* form of (C4), the realization clause …" | **Recommended** (wording), in a provenance paragraph. |
| What the indivisibility result tells an observer: "more a statement about the model than about data" | L152 | **None.** This is the paper's own stated reading. The reader now reaches it, rather than missing it as in run 4. |
| §3.1 dense | L190–L200 | Recommended (gate 3 scope) |
| Bell ("ontic parameter dependence", H-Bell) refers to companion papers | L244–L248 | None |
| Main equivalence "almost trivial" | L71, L93 | None. This is the paper's own reading. |
| Applications read as reframings | §§4–5 | None. This is the intended conditional reading. |
| Reliance on companion papers | throughout | None |

### Gate verdict: NOT MET

Under the preregistered rule, Q1–Q4 and Q6 pass, the Q5 memory results pass, and 5a and 5b pass. Q5 part (c) is PARTIAL, so the gate is not met.

### Proposed changes (separate from the diagnosis; each checked against the theorem's hypotheses)

1. **For (c), the instrument (no paper change).** If the owner wants (c) tested as 5a and 5b were, add a direct question for run 7. For example: "The paper says some memory effects are established by the mathematics yet can never be seen by the observer. Why can't they be seen, and how is that different from a memory effect that appears at a later step the observer does watch?"
2. **For (c), optional paper wording.** At L152, after "…neither appears in any accessible record.", insert: "An observer's data are the statistics of accessible windows, so a dependence that first appears at an order beyond all of them changes none of those data; that is why it is established by the theorem and yet unobservable."
   - Check against the hypotheses: accessible statistics are restrictions of the visible law to windows with kτ_S ≪ t_R (Main §2.3, Scope).
   - Conditional memory at order k involves X_{k+1}, which lies beyond such windows when k is beyond them.
   - No claim is added about the dynamics, nor about chaining inside a window.
3. **The different-deck rule (L132, recommended).** After "…may show either colour", insert: "(its exact cards do not matter here; only these two forecasts and their return to certainty at step 2 enter the argument)".
   - Check against the hypotheses: Theorem 3 uses only the overlap at s=1 and Γ₂=I.
   - The example is realizable as gate 1 verified at r25: hidden {0,1,2}, shared prior uniform on {0,1}, order 3.
4. **"Routed form" (L162, recommended).** Gloss it as "a stronger, mechanistic form of (C4), in which a record of the visible history is written into the hidden state and read back within the window".
   - Check against the source: `RoutedReadback` (PhysicalC4Discharge) has write, store and read clauses, and implies the history-level condition. The gloss adds no claim.

**Evidence for the owner.**
- 5a and 5b were restated or absent across runs 1–5. They pass when asked directly in run 6, and the reader's wording tracks G1, G2 and H1 closely.
- This supports the run-5 assessment that the earlier failures were largely the instrument, together with a real but now resolved explanatory gap.
- Part (c) now shows the same pattern. The paper states it plainly; the reader reaches its conclusion unprompted but is not asked to explain it.