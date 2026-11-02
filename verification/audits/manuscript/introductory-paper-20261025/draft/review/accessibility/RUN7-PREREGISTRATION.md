# Comprehension run 7: preregistration

The owner authorized run 7 after run 6, which did not meet gate 2. Run 6's verdict stands. Run 6 passed every item
except Q5 part (c), which was PARTIAL. Its evaluator diagnosed a mild deeper conceptual obstacle compounded by an
instrument gap: part (c) was not asked directly, while 5a and 5b, asked directly for the first time, passed. Run 7 adds
one direct question on part (c). The paper is not changed.

**Paper under test:** `papers/Introduction.pdf` at `bace5ef8` (r31), sha256
`22cceed23f4743063d7ca4c77440fcd0ccef00051d3518462cb814f9922fdae2`, 22 pages. It is identical in the current #918 head.

**Reader:**
- a fresh AI reviewer, not any earlier run's reader, with no prior context;
- instructed to read only that PDF, with no repository, corpus or web access, and no access to earlier answers,
  evaluations, reviewer feedback or intended answers.

**Recording:** the reader's final message is saved byte for byte before any evaluation.

## Questions shown to the reader

Questions 1–7 of `QUESTION-SHEET.md` and the direct questions 5a and 5b of `RUN6-PREREGISTRATION.md`, all unchanged,
followed by one more direct question asked after 5b:

**5c.** The paper says that, in some of the worlds it describes, a dependence of later observations on the past is
established by the mathematics and yet need not appear in any record an observer can obtain. How can both be true? What
does the mathematical result say about the world's whole cycle of evolution, and what can an observer actually see?
How does such a dependence differ from one that shows up at a step the observer does watch? Answer in your own words,
without quoting the paper's definitions.

## Pass/fail criteria (not shown to the reader)

Q1–Q4, Q6 and Q7 are evaluated as in `QUESTION-SHEET.md`. Q5 is evaluated on the memory results, as in runs 4–6. 5a
and 5b are evaluated under the criteria of `RUN6-PREREGISTRATION.md`. Part (c) is evaluated through 5c, which receives
its own verdict.

**5c, memory beyond every accessible window.** The answer must carry three points.
- **(i) The scope of the result.** The result concerns the world's whole cycle up to its return to the start, under its
  hypotheses: one hidden set-up shared by every start, and, for the equivalence with memory, every start possible.
  Under those hypotheses, the step-by-step forecasts cannot be chained somewhere in the cycle, which is equivalent to
  a dependence on the past at some step before the world returns to its start. The result does not say at which step.
- **(ii) The reason it can be unobservable.** What an observer can see are the statistics of the windows they can
  access, and those windows are short compared with the cycle. A dependence that first appears at a step beyond every
  such window changes none of those statistics. So the mathematics establishes it, and no accessible record contains
  it.
- **(iii) The distinction.** A dependence at a step inside an accessible window does change the statistics there, so
  the observer can detect it.

Verdicts:
- **PASS.** The answer states (i), (ii) and (iii) in ordinary language, with the reason in (ii). Any wording carrying
  these points passes.
- **PARTIAL.** The answer reaches the conclusion without the reason in (ii), as in run 6. Or it gives the reason
  without the distinction in (iii). Or it states the result without its hypotheses, where the omission does not
  change what is claimed.
- **FAIL.** The answer gives a wrong reason, for example limited measurement precision, or "the hidden part is not
  measured" offered as the whole account. Or it claims that every such dependence is unobservable, or that every one is
  observable. Or it attaches a condition the result does not have, or drops one in a way that changes what is claimed.

**Gate 2 is MET** exactly when Q1–Q4 and Q6 pass, Q5 passes on the memory results, and 5a, 5b and 5c all pass.
Otherwise it is NOT MET.

## Diagnosis of each failure

For every PARTIAL or FAIL, the evaluator states which of these it reflects, with the passage responsible and the
answer's wording as evidence:
- **ambiguous wording:** the paper's sentence admits the reader's reading;
- **missing explanatory premise:** a step the explanation needs is not stated in the paper;
- **deeper conceptual obstacle:** the paper states the reason correctly and plainly, and the reader still does not
  reconstruct it.

If run 7 fails, the diagnosis is reported to the owner before any revision is considered. The paper is not rewritten or
retested again without new evidence. Any proposed change is checked by the scientific reviewer against the theorem's
exact hypotheses and conclusion before it is applied.
