# Comprehension run 6: preregistration

The owner authorized run 6 as a controlled test, fixed before the run. Its purpose is to separate a problem in the
explanation from a genuine conceptual difficulty in two points that runs 1–5 tested only indirectly through Q5.

**Paper under test:** `papers/Introduction.pdf` at `bace5ef8` (r31), the revision both the scientific and editorial
gates accepted. The paper is not changed before the run.

**Reader:**
- a fresh AI reviewer, not any earlier run's reader, with no prior context;
- instructed to read only that PDF, with no repository, corpus or web access, and no access to earlier answers,
  evaluations, reviewer feedback or intended answers.

**Recording:** the reader's final message is saved byte for byte before any evaluation.

## Questions shown to the reader

Questions 1–7 of `QUESTION-SHEET.md`, unchanged, followed by two direct questions asked after Q5:

**5a.** The paper's recurrence result compares forecasts made from different possible starting states. Why does it
require the hidden part to be set up in the same way for every starting state? What would go wrong if the set-up could
depend on the starting state? Answer in your own words, without quoting the paper's definitions.

**5b.** The same result also includes forecasts from starting states that never actually occur in the history being
observed. Why are those starting states kept in the comparison? Answer in your own words, without quoting the paper's
definitions.

## Pass/fail criteria (not shown to the reader)

Q1–Q4, Q6 and Q7 are evaluated as in `QUESTION-SHEET.md`. Q5 is evaluated on the memory results and on part (c), as in
runs 4 and 5. Q5a and Q5b each receive their own verdict:

**5a, the shared hidden preparation.**
- **PASS.** The answer explains in ordinary language that the comparison is meant to show what one fixed rule, the
  dynamics, does from each start. If the hidden set-up could change with the start, a difference between two forecasts
  could come from the set-up rather than from the rule, so the forecasts would describe different set-ups rather than
  one rule started in different ways. Any wording carrying this reason passes.
- **PARTIAL.** The answer restates the condition (for example "the hidden odds are the same whatever is visible")
  without giving a reason, or gives the reason only for a specific example without its general point.
- **FAIL.** The answer gives a wrong reason, or says the condition does not matter.

**5b, never-occurring starts.**
- **PASS.** The answer explains in ordinary language that such a start is a possible start of the world, not an
  impossible one; that the result is about the rule, which must cover every start the rule can be given rather than only
  the starts a sample contains; and that the evidence that forecasts cannot be chained may come only from such a start.
  Any two of these three, stated with a reason, pass.
- **PARTIAL.** The answer restates that such starts are kept, or names one of the three points without a reason.
- **FAIL.** The answer treats such starts as impossible or irrelevant, or gives a wrong reason.

**Gate 2 is MET** exactly when Q1–Q4 and Q6 pass, Q5 passes on the memory results and on part (c), and both Q5a and
Q5b pass. Otherwise it is NOT MET.

## Diagnosis of each failure

For every PARTIAL or FAIL, the evaluator states which of these it reflects, with the passage responsible and the
answer's wording as evidence:
- **ambiguous wording:** the paper's sentence admits the reader's reading;
- **missing explanatory premise:** a step the explanation needs is not stated in the paper;
- **deeper conceptual obstacle:** the paper states the reason correctly and plainly, and the reader still does not
  reconstruct it.

Any proposed change is checked by the scientific reviewer against the theorem's exact hypotheses and conclusion before
it is applied. If run 6 fails, the diagnosis is reported to the owner before any further rewriting.
