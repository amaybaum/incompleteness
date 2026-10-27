# Gate 2, comprehension run 7: evaluation (preregistered)

**Gate verdict: MET.** Under the preregistered rule, Q1–Q4 and Q6 pass, Q5 passes on the memory results, and 5a, 5b and 5c all pass. Since no item is PARTIAL or FAIL, no preregistered diagnosis is required. Three peripheral scope slips are recorded below for completeness; none falls under a graded criterion.

**Provenance.**
- I read `RUN7-PREREGISTRATION.md`, `RUN7-ANSWERS-bace5ef8.md`, `QUESTION-SHEET.md` and `RUN6-PREREGISTRATION.md` at `cd43dbbe`.
- The run-7 preregistration was committed at `be833937`, an ancestor of `cd43dbbe`, and is unchanged since.
- The paper at `cd43dbbe` is identical to r31 `bace5ef8`.
- I applied the criteria exactly. Line numbers below are the paper at `bace5ef8`.

## Verdicts

**Q1, the basic idea: PASS.**
- Correct: "The rest, the 'hidden' part, isn't just unknown for now. It is in principle out of the observer's reach" (L33).
- Correct: "this is not the same as quantum unsharpness, because it applies even when you always measure the same single thing" (L33).

**Q2, randomness from hidden information: PASS.**
- The mechanism is correct: "two worlds that look identical to you can differ in their hidden parts. Those hidden differences send them to different visible futures" (L29).
- So is "Nothing random happens after the deal" (L25).

**Q3, the main result: PASS.**
- The three collections coincide over a fixed number of steps, in both directions.
- The tape-plus-clock construction is correct (L73).
- So is "A pattern that never repeats can't be reproduced forever by one fixed finite world. You get a separate world for each horizon" (L91).

**Q4, what the result does not show: PASS.**
- Every element of the evaluator note is present:
  - possibility only;
  - one fixed measurement;
  - the squared rule "put into the definition … would work just as well with any power";
  - the evolution between times not selected, and no mechanism;
  - five conditions, of which "Three of them are the substantive ones", matching L224;
  - not implied by OI, with the qubit counterexample;
  - substratum supply open.
- **Peripheral slip:** "Bell correlations need one lab's hidden response to depend on the other lab's setting" drops the measurement-dependence alternative, as in runs 2–4. The paper states both alternatives at L258 and L308. This is reader compression, not a paper defect.

**Q5, memory results: PASS.**
- Correct:
  - both directions;
  - "the hidden part must be big enough to hold it";
  - storage versus memory ("Memory is the part of that store that actually changes future observations");
  - the capacity bound "at least 2 to the power of the maximum past–future information";
  - the exact minimum hidden predictive memory;
  - the Pinsker floor.
- **Peripheral slip:** "In a particular coupling model, observed memory also means the hidden part hasn't relaxed to its reference odds, which bounds a mixing time."
  - The first half is the persistence form, which needs no mixing hypothesis, and is correct.
  - The second half, the mixing-time bound, needs the mixing hypothesis. The paper states that hypothesis at L122: "under the mixing hypothesis this becomes the slow-bath form, a lower bound on the mixing time".
  - The reader drops it, but in a clause outside the Q5 criteria. This is reader compression.

**5a, the shared hidden preparation: PASS** (run-6 criteria).
- The reason is given in the reader's own words: "That only makes sense if the only thing that differs between those starts is the visible start itself. If the hidden part were prepared differently depending on the start, then two different forecasts might just reflect two different preparations rather than anything about the dynamics."
- The card contrast is also there ("two different games, not one game started two ways").
- The answer adds that the overlap step needs one common preparation. That matches L140, "uses that every row comes from the same preparation [Main §2.3]".
- Enabling passage: L130, G1, together with the anticorrelated-deal contrast.

**5b, never-occurring starts: PASS** (run-6 criteria; all three points, with reasons).
- **Possible, not impossible.** "A start that never occurs is still possible; the dealer just never uses it" (L132, H1).
- **Rule, not sample.** "what the same dynamics and the same hidden preparation would do from any start the world could have. It is not about which starts happen to show up in a given sample" (L130, L140, G2).
- **The evidence may lie only in such a start.** "the forecast from the unused black start overlaps with the one from red at step 1. That overlap is what makes step-by-step chaining fail" (the different-deck example, L132).

**5c, memory beyond every accessible window: PASS.** Each of the three points is judged separately, with maximum skepticism.

- **(i) Scope with hypotheses: carried.**
  - "The mathematics is about the world's full recurrence cycle: the whole stretch until the entire system returns to its starting configuration."
  - "If the hidden part starts with the same odds whatever is visible, and some visible step is not fully predictable, then somewhere in that cycle the forecasts from the start can't be built up step by step."
  - "With every start having some probability, that is equivalent to the record having memory at some time lag shorter than the cycle."
  - Each hypothesis is present: the shared set-up, and every start possible for the equivalence.
  - The step is not specified ("somewhere", "some time lag").
  - "not fully predictable" drops "from the current observation". That makes the hypothesis stronger, not weaker, so it cannot overstate the claim.
  - Enabling passages: L148 (the Corollary) and L156.
- **(ii) The reason: given, not just the conclusion restated.**
  - "the cycle can be enormously long compared with the windows of time an observer can actually watch. A hidden trace of the past might first affect what is seen only at a lag beyond every window the observer can reach, though still before the world comes back round. Then the dependence is real and forced by the dynamics, but no accessible record shows it."
  - This is the preregistered mechanism: windows short relative to the cycle, a dependence first appearing beyond every window, so no accessible record contains it.
  - It is not a precision argument, and not "the hidden part is not measured".
  - "might" keeps the claim modal. The answer does not say every such dependence is unobservable.
  - The closing "they constrain how such a world can be described, not what the data will show" paraphrases L152 closely. The reason itself is in the reader's own words.
  - Enabling passages: L152 ("Accessible windows are, by definition, short compared with the world's recurrence time … can first affect what is seen at an order beyond every accessible window … neither appears in any accessible record"), and L156's long-line picture.
- **(iii) The distinction: stated, with the example.**
  - "If instead the dependence shows up at a step inside a window the observer does watch, it can actually be detected in their data."
  - "An observer whose window ends at step 2 sees no memory. One whose observations reach step 3 can detect it."
  - Enabling passages: L152 (the "Two cases differ" sentence) and L154.
- **No FAIL condition applies.** There is no wrong reason. The answer does not say every such dependence is unobservable, or every one observable. No condition is added, and none is dropped in a way that changes the claim.

**Q6, the two applications: PASS.**
- **Cosmological constant.** The established, proposed and open parts are each correct. The dimensional identity is listed as established, matching L256 and [GR §6.3].
- **Black holes.** Conservation and recovery are separated. The counts (1,376 of 40,320) and the floor are correct. The Page curve is conditional on three conditions, with each condition's status.
- **Peripheral slip.** "thorough scrambling, which actually fails for these reversible maps when the black-hole/radiation split matches the configuration coordinates" omits "acting on a definite configuration" (L300).
  - L300 states both conditions.
  - L300's next sentences also say what H-scramble would require: "an initial superposition of configurations or a split not aligned with them".
  - This is reader compression and does not change the open/established classification.

## Preregistered diagnoses

None are required: no item is PARTIAL or FAIL.

The three peripheral slips (Q4 Bell, the Q5 mixing clause, Q6 scrambling) each concern a hypothesis the paper states correctly at the cited line (L258/L308, L122, L300). If graded, they would be reader compression, not ambiguous wording.

## Q7 points, classified

| Point | Passage | Classification |
|---|---|---|
| §2.5's rooted table, shared prior and zero-probability rows "took several readings" | L130–L156 | **None.** This is difficulty only; 5a, 5b and 5c pass. |
| The second deck example is "described in words only … not fully sure I got why the overlap appears there" | L132 ("After the first shuffle both forecasts give red a positive chance") | **Recommended (presentation).** A two-row table at steps 1 and 2 would help. 5b passed using this example. |
| "how much physical bite" a failure of chaining has, and "what testable content remains" | L152; §6 open problem 3 (L314) | **None.** This is a legitimate question that the paper answers: L152 says the failure is a constraint on description, not a prediction, and L314 lists a memory-witness test as open. |
| §3.1 "three notions", Hadamard, Pauli twirl | L184–L200 | Recommended (gate 3 scope) |
| Theorem 4's structural assumptions dense (§3.2) | L212 | None. It carries the r26 plain gloss. |
| §3.3 coherent lifts taken on trust | L226–L236 | None |
| Black-hole notation (D sector, effective-pure-state theorem) relies on companions | L298 | None. Each is defined in place, with its source. |
| "proved on paper" in companion papers | throughout | None. Evidence classes are stated by design. |
| The abstract is harder than the body | L17 | Recommended (presentation) |

## Q7 points revealing a scientific defect

None. Every Q7 point is about difficulty or presentation, or asks a question the paper already answers. Nothing points to an unsupported claim, a missing hypothesis or a wrong statement in the paper.

## Proposed changes (optional; none required for the gate)

1. **L132, the different-deck example: add a two-row table.** This is presentation only.
   - Step 1: red start → red with certainty; black start → red or black, ½ each.
   - Step 2: red → red; black → black.
   - Mark the black row "never observed".
   - Check against the hypotheses: these are exactly the rows gate 1 verified at r25 (hidden {0,1,2}, shared prior uniform on {0,1}, order 3). They show the step-1 overlap and the step-2 return (Theorem 3, s=1, n=2).
2. **L17, the abstract: readability.** This is presentation only, and any edit must keep every hypothesis and the full-support equivalence as stated.