# Accessibility gate: paper-only comprehension test

`QUESTION-SHEET.md` holds the questions and the evaluator notes. Readers never see the notes.

## Run 1: `2afb5b6a` (r19)

- **Paper read:** `papers/Introduction.pdf` at `2afb5b6a`, sha256 `5ac16d61c6e2cf6bd36d8f1a037fdad28e8c58597c409d8cca707c39120319d8`, 18 pages.
- **Reader:** an AI reviewer with no prior context about OI. It was instructed to read only that PDF, with no repository, corpus or web access. Its tool log shows two Read calls on the PDF, pages 1–10 and 11–18, and nothing else.
- **Answers:** `RUN1-ANSWERS-2afb5b6a.md` records them verbatim, unedited, saved before any evaluation. sha256 `332583a591a9ad65c628b0871ab391b4f86f03f3ce66a895dcf8b72095c61b57`.
- **Scope of the evidence:** this is an AI comprehension test. It is not evidence of human comprehension. Human reader testing is optional before public release.
- **Evaluation:** the scientific reviewer judges these answers against the paper and its sources, using the evaluator notes. That evaluation is recorded separately.
- **Evaluation of run 1:** `RUN1-EVALUATION.md` records the scientific reviewer's verdict: **gate 2 not met.** Q1–Q4 and Q6 pass. Q5 (memory) is only partly correct, for three reasons:
  - The paper gives the memory equivalence in one direction only.
  - The paper's own forecast gloss drops the shared hidden prior.
  - The shared-prior condition is never explained.

  Four explanation changes are required before a re-test with a fresh reader.

## Run 2: `10c629ea` (r20)

- **Paper read:** `papers/Introduction.pdf` at `10c629ea`, sha256 `905822ed15faa80bd91953f1b532fbcbd4b788a2f1d6d9306ee4b3079f312adf`, 20 pages.
- **Reader:** a fresh AI reviewer, not the run 1 reader, with no prior context about OI. It was instructed to read only that PDF, with no repository, corpus or web access. Its tool log shows two Read calls on the PDF, pages 1–10 and 11–20, and nothing else.
- **Answers:** `RUN2-ANSWERS-10c629ea.md` holds the reader's final message byte for byte, unedited, saved before any evaluation. sha256 `5e0a23c9f895b94bde5767e4c32ff31391952ce1d008d25fed3b97b602885744`.
- **Scope of the evidence:** as for run 1, this is an AI comprehension test and not evidence of human comprehension.
- **Evaluation of run 2:** the scientific reviewer's three reports, each verbatim in its own file, in the order received: `RUN2-EVALUATION.md` (the evaluation), `RUN2-EVALUATION-REVISED.md` (its revision after the owner's addendum) and `RUN2-EVALUATION-ADDENDUM.md` (on the owner's refinement, with the final wording). **Gate 2 not met.** Q1–Q4 and Q6 pass. Q5 (memory) is only partly correct: the shared hidden starting odds and the rows for starts that never occur are restated, not explained (Q7 reports guessing), the memoryless window is stated without its reason, and the distinction between memory and window P-divisibility is absent. Three explanation changes (A, B, C) are required before run 3 with a fresh reader.

## Run 3: `e64b2a4c` (r24)

- **Paper read:** `papers/Introduction.pdf` at `e64b2a4c`, sha256 `57bc78423a4cb5156d9ec188bc7bb04a8a367701f0ad291c3c72fc0072091e8a`, 21 pages.
- **Reader:** a fresh AI reviewer, not the run 1 or run 2 reader, with no prior context about OI. It was instructed to read only that PDF, with no repository, corpus or web access. Its tool log shows two Read calls on the PDF, pages 1–11 and 12–21, and nothing else.
- **Answers:** `RUN3-ANSWERS-e64b2a4c.md` holds the reader's final message byte for byte, unedited, saved before any evaluation. sha256 `df1013d712ad0c903e17bafb9b834ddf7a145093a34ecff8d87736e4ac744ab9`.
- **Scope of the evidence:** as for runs 1 and 2, this is an AI comprehension test and not evidence of human comprehension.
- **Evaluation of run 3:** `RUN3-EVALUATION.md` records the scientific reviewer's report verbatim: **gate 2 not met.** Q1–Q4 and Q6 pass. Q5 is only partly correct on the owner's three criteria: the shared hidden preparation is restated, the role of never-occurring starts is absent, and memory at a later step an observer still sees is run together with memory beyond every accessible window. Two explanation changes (D at L130, E at L146) are required before run 4 with a fresh reader.

## Run 4: `59622f0e` (r27)

- **Paper read:** `papers/Introduction.pdf` at `59622f0e`, sha256 `480d1516c72631d892826a744fd5ad4e2c6bb2a9ff647f6a809d4f2be6dc9960`, 22 pages.
- **Reader:** a fresh AI reviewer, not any earlier run's reader, with no prior context about OI. It was instructed to read only that PDF, with no repository, corpus or web access. Its tool log shows two Read calls on the PDF, pages 1–11 and 12–22, and nothing else.
- **Answers:** `RUN4-ANSWERS-59622f0e.md` holds the reader's final message byte for byte, unedited, saved before any evaluation. sha256 `cdff86c99e5891ec601d6ea373eec221a0815a3e8cddef5e9d0a19182073eaae`.
- **Scope of the evidence:** as for the earlier runs, this is an AI comprehension test and not evidence of human comprehension.
- **Evaluation of run 4:** `RUN4-EVALUATION.md` records the scientific reviewer's report verbatim: **gate 2 not met.** Q1–Q4 and Q6 pass. Q5 is judged in three parts: (a) the shared hidden preparation, PARTIAL (restated); (b) the never-occurring starts, FAIL (absent); (c) memory beyond every accessible window, PARTIAL (correct conclusion, improved from run 3, reason missing). The reader's recurring question about the physical meaning of the cycle-wide result is classified as a legitimate objection the paper leaves unanswered. Three explanation changes (G1 at L130, G2 at L140, G3 at L152) are required before run 5.

## Run 5: `d76fe9df` (r29)

- **Paper read:** `papers/Introduction.pdf` at `d76fe9df`, sha256 `1f9fa4e1914aebe2304521707aa1cf066d127714d82c4d5fb7833de21fe51ee3`, 22 pages.
- **Reader:** a fresh AI reviewer, not any earlier run's reader, with no prior context about OI. It was instructed to read only that PDF, with no repository, corpus or web access. Its tool log shows two Read calls on the PDF, pages 1–11 and 12–22, and nothing else.
- **Answers:** `RUN5-ANSWERS-d76fe9df.md` holds the reader's final message byte for byte, unedited, saved before any evaluation. sha256 `3f8fc104e480074c2b76d23a4864f39edb4a6e014ba86e33bdee1147ca055cd8`.
- **Scope of the evidence:** as for the earlier runs, this is an AI comprehension test and not evidence of human comprehension.
- **Evaluation of run 5:** `RUN5-EVALUATION.md` records the scientific reviewer's report verbatim: **gate 2 not met.** Q1–Q4 and Q6 pass. Q5 parts (a), (b) and (c) are unchanged from run 4: (a) restated, (b) absent, with the misconception "impossible starts", (c) correct conclusion without a reason, with the reader unable to place the order k relative to accessible windows. Two explanation changes (H1 at L132, H2 at L156) are required and one (L300) is recommended. The report also notes that Q5 as worded does not ask about (a) or (b), and that returns on prose revision for those two parts are diminishing.

## Run 6: preregistered

`RUN6-PREREGISTRATION.md` fixes run 6 before it is run, by owner authorization. It adds two direct questions (5a, the
shared hidden preparation; 5b, never-occurring starts), their pass/fail criteria, the gate rule, and the three failure
diagnoses (ambiguous wording, missing explanatory premise, deeper conceptual obstacle). The paper under test is r31 at
`bace5ef8`, unchanged.

## Run 6: `bace5ef8` (r31)

- **Paper read:** `papers/Introduction.pdf` at `bace5ef8`, sha256 `22cceed23f4743063d7ca4c77440fcd0ccef00051d3518462cb814f9922fdae2`, 22 pages.
- **Reader:** a fresh AI reviewer, not any earlier run's reader, with no prior context and no access to earlier answers or evaluations. It was instructed to read only that PDF. Its tool log shows two Read calls on the PDF, pages 1–11 and 12–22, and nothing else.
- **Questions:** `QUESTION-SHEET.md` 1–7 with the preregistered 5a and 5b (`RUN6-PREREGISTRATION.md`, committed at `d1368bf0` before the run).
- **Answers:** `RUN6-ANSWERS-bace5ef8.md` holds the reader's final message byte for byte, unedited, saved before any evaluation. sha256 `273fe35622b37015e4124b1c35c3506ae56f598d7b48527ae9287381db1d482b`.
- **Scope of the evidence:** as for the earlier runs, this is an AI comprehension test and not evidence of human comprehension.
- **Evaluation of run 6:** `RUN6-EVALUATION.md` records the scientific reviewer's report verbatim, scored under the preregistered criteria: **gate 2 not met.** Q1–Q4, Q6 and the Q5 memory results pass, and the direct questions 5a and 5b both pass. Q5 part (c), memory beyond every accessible window, is PARTIAL: the reader reaches the paper's conclusion unprompted in Q7 but gives no reason. The preregistered diagnosis is a mild deeper conceptual obstacle compounded by an instrument gap, since (c) is not asked directly. Proposed changes are listed separately and none is applied.

## Run 7: preregistered

`RUN7-PREREGISTRATION.md` fixes run 7 before it is run, by owner authorization after run 6 did not meet gate 2; run 6's
verdict stands. It adds one direct question, 5c, on memory beyond every accessible window, with its pass/fail criteria,
and keeps 5a, 5b, the gate rule and the three failure diagnoses. The paper under test is r31 at `bace5ef8`, unchanged.

## Run 7: `bace5ef8` (r31)

- **Paper read:** `papers/Introduction.pdf` at `bace5ef8`, sha256 `22cceed23f4743063d7ca4c77440fcd0ccef00051d3518462cb814f9922fdae2`, 22 pages.
- **Reader:** a fresh AI reviewer, not any earlier run's reader, with no prior context and no access to earlier answers or evaluations. It was instructed to read only that PDF. Its tool log shows two Read calls on the PDF, pages 1–11 and 12–22, and nothing else.
- **Questions:** `QUESTION-SHEET.md` 1–7 with the preregistered 5a, 5b and 5c (`RUN7-PREREGISTRATION.md`, committed at `be833937` before the run).
- **Answers:** `RUN7-ANSWERS-bace5ef8.md` holds the reader's final message byte for byte, unedited, saved before any evaluation. sha256 `4d1af3d6165d4639c23e6186fcbb3d7608733bd1909f3562d68d2f391835c663`.
- **Scope of the evidence:** as for the earlier runs, this is an AI comprehension test and not evidence of human comprehension.
- **Evaluation of run 7:** `RUN7-EVALUATION.md` records the scientific reviewer's report verbatim, scored under the preregistered criteria: **gate 2 met.** Q1–Q4, Q6 and the Q5 memory results pass, and the direct questions 5a, 5b and 5c all pass. For 5c the answer carries the result's scope over the whole recurrence cycle with its hypotheses, the reason a dependence first appearing beyond every accessible window changes no accessible statistic, and the contrast with a dependence inside a watched window. Three peripheral scope slips outside the graded criteria are recorded as reader compression. No Q7 point reveals a scientific defect. The two optional presentation changes the report lists are not applied; r31 is the paper that met the gate. Run 6's verdict stands.
