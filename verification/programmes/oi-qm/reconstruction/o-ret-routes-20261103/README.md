# O-RET (#1032) — status

Phase A's frozen inputs (`PREREG-PHASE-A.md`, `DESIGN-PULSE.md`, `PHASEA-TUPLES.json`,
`PHASEA-EXPECTED.json`) are fixed at `F = 49f0bd41` (owner designation, #1032 comment
6623962802), and `phaseA/` holds the tool accepted at `71a07fa5` and the run-1 records. This note
edits none of them.

**What Phase A establishes.** Run 41813302146 passed on all 49 frozen tuples
(`phaseA/run-1/RESULT.md:36–47`). In the owner's words (`:55–57`): "The verified PASS establishes
that the implementation agrees with its 49 frozen calibration expectations. It does not establish
physical retention in native OI dynamics or validate the classifier outside this test set." The
reviewer's separate check cannot be regenerated from `main`, since its script is not retained
(`:51–53`).

**Status lines that the later record supersedes.**

- `PREREG-PHASE-A.md:3–4` ("Not authorized to run") and `phaseA/IMPLEMENTATION-NOTES.md:7` ("Not
  run"): one execution was authorized and made, run 41813302146 (`phaseA/run-1/RESULT.md:11`,
  `:26–31`).
- `DESIGN-PULSE.md:11` ("r6 has not been re-reviewed"): r6 was checked by the re-reviews of
  `f76467f1` (`PREREG-PHASE-A.md:10–11`).
- `phaseA/run-1/REVIEW.md:148`: `F` (`49f0bd41`) and the run commit (`71a07fa5`) are reachable
  from `main`.
- `DEFINITIONS.md:133` (`ε* := [OWNER TO SET]`): the owner set `ε* = 0.05` as a provisional
  operational threshold (#1032 comment 6612956983), frozen as `ε* = 1/20` in
  `PREREG-PHASE-A.md:56`.

**Paper results.** Lemma S′ and Lemma Q (`ANNOTATION.md`) and the definitions in
`DEFINITIONS.md` are paper results. `ROUTES.md`, which holds the lemmas' proofs, is on `main` only
at `F` (`git show 49f0bd41:verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103/ROUTES.md`).
No review record of them is on `main`. They are not independently validated on `main` and are
not premises until they are (AGENTS.md §A.46 item 7).

**`REVIEW-Q7.md`.** `PREREG-PHASE-A.md:12` and `:158` cite a Q7 review, `REVIEW-Q7.md`, for the
wording frozen in §2.7, which the preregistration labels unreviewed ([U]). No commit on `main` or
on the branches `research/o-ret-routes-20261103` and `research/o-ret-phasea-tool-20261104`
contains a file of that name; it could not be located in the audited repository history. The
§2.7 wording at `F` is the only text of that review on `main`.
