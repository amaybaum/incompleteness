## Gate 2 at `d76fe9df`: comprehension test run 5 — not met

The reader explains Q1–Q4 and Q6 correctly. Q5's memory results are all correct, but its three owner-specified parts are unchanged from run 4:
- **(a)** is restated, not explained;
- **(b)** is absent from the answer, and Q7 shows a misconception: "impossible starts";
- **(c)** gives the correct conclusion with no reason, and Q7 shows the reader cannot place "order k below the recurrence time" relative to accessible windows.

Two short, targeted explanation changes are required, at L132 and L156. One change at L300 is recommended.

The evidence in the candid assessment below suggests that further prose alone may not move (a) and (b). One reason is that Q5, as worded, does not ask about them.

I read `RUN5-ANSWERS-d76fe9df.md`, `QUESTION-SHEET.md` and `RUN4-EVALUATION.md` at `72014a79`, read-only. The paper there is identical to `d76fe9df`, and line numbers below are the paper at that commit.

### Q1–Q6 verdicts

**Q1, the basic idea: PASS.**
- "The hidden part is not just unknown for now. It is in principle out of the observer's reach, even when the observer always makes the same single measurement" is correct (L33).

**Q2, randomness from hidden information: PASS.**
- The mechanism is correct: "two worlds that look the same to you can differ in their hidden part. Those different hidden parts can send what you see next in different directions" (L29).
- The reader also adds, correctly, that the pattern itself has memory: "What you see depends on what you saw two steps ago, not just on what you see now."

**Q3, the main result: PASS.**
- The three collections are the same over a fixed number of steps, in both directions (Theorem 1).
- The stored-sequence construction is correct (L73).
- So is "It cannot reproduce a non-periodic pattern for all time. The hidden world you build also depends on which pattern and which time span you want" (L91, L236).

**Q4, what the result does not show: PASS.**
- Every element of the evaluator note is present:
  - possibility only;
  - one fixed measurement;
  - the exponent not selected, with the correct reason;
  - the evolution between two times not selected;
  - Theorem 4 "under a stated minimal operational structure";
  - not implied by OI, with the theory that never creates superpositions;
  - which conditions a substratum supplies is open.
- The run-4 Bell side remark does not recur.

**Q5, memory: PARTIAL.**

The core memory results are all correct:
- the forward and converse directions;
- "The memory visible in the record is at most the hidden memory, which in turn is at most the hidden part's capacity in bits";
- the size and minimum-memory bounds and the floor;
- "Storing the past is not the same as memory".

The three owner-specified parts:

| Part | Verdict | From the answer's wording | Enabling or failing passage | Change from run 4 |
|---|---|---|---|---|
| (a) one hidden preparation across hypothetical starts | **PARTIAL: restatement** | "Suppose the hidden part starts with the same odds whatever is visible." The hypothesis is correct; no reason is given. Q7 lists "drawn independently of it" as hard. | L130 G1, new in r28: "A forecast from a start is a forecast of what the rule does only if the hidden part is set up by the same procedure every time; if the procedure changed with the start, a difference between two forecasts could come from the setup rather than from the dynamics." It is present, and the answer does not use it. | Unchanged: restated in runs 2, 3, 4 and 5 |
| (b) never-occurring starts kept in the rooted family | **FAIL: absent, with a misconception** | Not in Q5. Q7: "not fully why rows for impossible starts should count physically". The starts are not impossible: they are starts the world can be given, which this sample's preparation never produces. | L140 G2: "a result about a rule has to cover every start the rule can be given, not only the starts a particular sample contains". L132's different-deck example. Neither says outright that a never-occurring start is still a possible start. | Unchanged as a verdict (absent in runs 1–5). New this run: the word "impossible" pinpoints the misconception |
| (c) an effect beyond every accessible window, established but unobservable | **PARTIAL: correct conclusion, no reason** | "That failure may lie beyond any window an observer can actually reach." This is correct and keeps the two cases apart, but no reason is given. Q7: "didn't follow how 'order k below the recurrence time' relates to the windows an observer can reach". | L152, G3 as r29 reworded it: "The failure of chaining is a property of the world's rule … rather than of any accessible record". L152: "Accessible windows are, by definition, short compared with the world's recurrence time L". L156: "so that k lies beyond the accessible windows". Each piece is present, but the paper never draws the simple picture of where k sits. | Unchanged. In run 4 the reader questioned the physical meaning; in run 5 the reader cannot place k |

**Q6, the two applications: PASS.**
- The cosmological-constant answer gives "Established / Proposed / Open" exactly, including "The same underlying world is compatible both with the offset gravitating and with it not gravitating".
- The black-hole answer separates conservation from recovery and gives the floor. It gives the Page curve as conditional on the three conditions, and says whether it follows is open.
- Two phrases are loose but not scope errors:
  - "Many reversible maps" — L294 says "1,376 of the 40,320 toy maps".
  - "fails for the natural kind of bijection" — L300 says on a definite configuration with an aligned split.

### Q7 as evidence

**Remaining defects:**
1. **"Rows for impossible starts" (part b): remaining defect.** Responsible passages: L132 and L140. The paper says "never occurs", "never dealt" and "never happen". Readers hear "impossible". No sentence says that such a start is possible for the world, and is merely never produced by this preparation.
2. **How "order k below the recurrence time" relates to accessible windows (part c): remaining defect.** Responsible passages: L152 and L156. The facts are all stated: accessible windows are short compared with L, k < L, and for a law Markov on accessible windows k lies beyond them. But they are spread over two paragraphs, and no plain picture joins them.

**Other Q7 points:**

| Point | Passage | Classification |
|---|---|---|
| Main equivalence "almost tautological" | L71, L93 | **None.** This is the paper's own correct reading ("a question of possibility"; the content lies in memory). |
| Five conditions abstract; unclear whether any substratum meets them | L216–L224 | **None.** The r28 names and glosses are in place. That no substratum is yet shown to meet them is the stated open problem (L224). |
| The Page curve "seemed to undercut itself"; had to guess what remains | L298–L300 | **Recommended** (see below). |
| Reliance on companion papers and unpublished records | throughout | **None.** Each result carries its evidence class and source by design. |

**The Page-curve point: what survives when H-scramble fails?**
- L300 says the condition fails "for every bijection that acts on a definite configuration when the split … follows the configuration coordinates". It does not say what would make the condition hold, so the reader had to guess what remains.
- GR App. A.7 states it: H-scramble "requires an initial superposition of configurations or a bipartition not aligned with them, and which of these the substratum supplies is open".
- The established separation of conservation from recovery (L292–L294) does not depend on H-scramble.

### Gate verdict: NOT MET

**Required explanation changes.** Both keep every theorem and definition at full strength.

**H1 (L132), part (b): "never occurs" is not "impossible".** After "Why keep a start that never occurs?", insert:

> "Such a start is not impossible: the world can be started there, and this dealer's preparation simply never does so."

Anchor: Main §2.3, where these are roots of visible probability zero under the chosen visible prior, not states excluded by the dynamics. The definition of "rooted family" is unchanged.

**H2 (L156), part (c): where k sits.** After "…so that k lies beyond the accessible windows.", insert:

> "Picture the orders $1,2,\dots,L-1$ as a long line: accessible windows cover only its short beginning, while the order $k$ of the Corollary can lie anywhere on it, so a memory that first appears late on the line is real in the dynamics but outside every window."

Anchor: Main §2.3, Scope: "the gap it is equivalent to may lie at any order below the recurrence time; (C4) and condition (ii) … require an accessible order, kτ_S ≪ t_R".

**Recommended:**

**R-Page (L300).** After "…not every configuration of black hole and radiation has the same energy.", insert:

> "What survives is the conditional statement: the cycle-averaged Page value follows once H-scramble holds, which requires an initial superposition of configurations or a split not aligned with them, and which of these the substratum supplies is open [GR App. A.7]; the separation of conservation from recovery above does not depend on it."

### Candid assessment for the owner (evidence only)

1. **The question does not ask for (a) or (b).** Q5 asks: "What does the paper say about memory? When must the hidden part … carry information about the past, and what can an observer learn …?" The shared prior and the never-occurring starts belong to the recurrence result, which readers mention only as an add-on to Q5. Across runs 1–5, every reader who mentioned the recurrence result stated its hypothesis correctly: run 1 partly, runs 3–5 fully. None explained (a) or (b) in Q5. Part of the "failure" is that the instrument does not ask.
2. **There is real difficulty too.** In every run the reader raised these points unprompted in Q7: "took several passes" (run 3), "helped a little but stayed confusing" (run 4), "not fully why rows for impossible starts" (run 5). So the difficulty is genuine, not only an artefact of the question.
3. **Returns on prose are diminishing.**
   - The case-separation edits for (c) (E in r25) visibly worked: the run-3 conflation disappeared in runs 4 and 5.
   - The edits for (a) and (b) have not:
     - change A (r21, the card example);
     - change 1 (r21, L134);
     - D (r25, the different deck);
     - G1 and G2 (r28).
   - After each, the reader's scope stayed correct, but explanation never appeared.
   - Run 5's new evidence is specific: the word "impossible", and the location of k. H1 and H2 target exactly those two, which is why they are listed as required.
4. **Options the evidence supports.** The choice is the owner's.
   - Add a direct question to the sheet for runs 6 and later. For example: "The recurrence result compares forecasts from every starting state, including ones that never occur, under one hidden set-up. Why?" That would test (a) and (b) directly.
   - Accept PARTIAL on (a) as the realistic ceiling for a careful non-specialist reading prose alone. The scope is always right, and the reason is a fine methodological point about what a statement about a rule must quantify over.
   - Replace prose with a small figure or table for the different-deck example: the two rows at steps 1 and 2, marked "observed" and "not observed". Five prose revisions have not produced the explanation.

This assessment is consistent with gate 1's accepted r28–r29 text. H1, H2 and R-Page add no claim beyond Main §2.3 and GR App. A.7.