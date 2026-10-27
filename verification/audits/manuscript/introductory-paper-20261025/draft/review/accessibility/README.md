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
