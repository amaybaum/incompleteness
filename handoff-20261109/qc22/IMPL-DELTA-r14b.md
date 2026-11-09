# Q-C2-2 (ARP-3-QC22): what the scripts must change to match r14b

WIP / UNVERIFIED. Model-written. For the implementer. Nothing here was run.

## Status

- **No QC22 script exists yet.** This delta is stated against r14's script specification, `IMPL-DELTA-r14.md` (in
  `r14/`) and `IMPL-DELTA-r14a.md` (in `r14a/`, `76a21032…`). It lists only what r14b adds or changes. Items of those
  two files not named here stand.
- **Target:** r14b `preregistration.draft.md`. Tags are r14b's `R14a-…` tags; line numbers are r14b's.
- **Authorization** (c.6740747027, as the coordinator reads it for this iteration): paper only. No script is written,
  run or pushed under it. No step below needs F1, the design run or an LP on OI data.

## Part A. Blocker

| # | r14b requirement | `qc22_check.py` | `controls.py` |
| --- | --- | --- | --- |
| A1 | **Rc1, the no-unapproved-F1 rule** (1747–1772) | — | The rule's per-attempt predicate, in `order` and `verdict`, becomes: `jobB_conclusion` absent or `skipped`, **and** `B4_conclusion` absent or `skipped`, **and** (`A3_conclusion` absent or `skipped`, **or** `A3b_conclusion == "success"`). `A3_conclusion` is already in the `order.json` record (r14 schema); "absent" means the step, or job A, is not in the attempt's jobs record. Any other `A3_conclusion` (`success`, `failure`, `cancelled`, `null`) with A3b not `success` is a violation. No other condition changes |
| A2 | **Rc1, NOF1** (800–803) | — | New `--self-test` case on synthetic attempt records built in memory, job B and B4 `skipped` unless stated: A3 absent → holds; A3 `skipped`, A3b `failure` → holds; A3 `failure`, A3b `success` → holds; A3 `failure` / `cancelled` / `null`, A3b `failure` → each fails; A3 `success`, A3b `failure` → fails; B4 `success` → fails for every A3/A3b pair above. Run through both `order`'s and `verdict`'s call of the predicate |
| A3 | **Rc1, executor precondition** (1769–1772; precondition 6, 2136–2145) | — | None in code. Before each push of a commit carrying the checker to a recorded branch, the executor runs locally, on that commit's tree with Python 3.11: `mkdir -p "$T/arp3-qc22" && python3 -I -S -B <record dir>/qc22_check.py --event fixture > "$T/arp3-qc22/fixtures.json"` under a 60-minute limit, then `python3 -I -S -B <record dir>/controls.py fixture-mode-check "$T/arp3-qc22/fixtures.json"`, and pushes only if the first completes and the second exits 0. It cancels no run on a recorded branch while job A runs |

## Part B. Nits, residuals and optional items

| # | r14b requirement | change |
| --- | --- | --- |
| B1 | **N1, N7** | none (text) |
| B2 | **N2** expired-artifact alternative (1943–1949) | None now. `IMPL-DELTA-r14a.md` A8's policy constant stays `FAIL_CLOSED`. Its alternative has no frozen rendering, so it is implemented only after a reviewed revision that freezes one; do not write a `NOT_CHECKABLE` branch before then |
| B3 | **N3** §A.42 item 8 dispositions (1950–1969) | None until the owner chooses. The chosen option comes with a reviewed revision, whose own delta then applies (for narrowing, chiefly the note's and `verdict`'s wording of the post-`E` checks) |
| B4 | **N4** | none (text: the off-`main` table and two predicted-status edits) |
| B5 | **N5** | none (text: the re-establishment route) |
| B6 | **N6** M-RAY (686–689) | The fabricated-certificate variant removes an **extreme** row: on GX+R-Y's preparation side, the first row in frozen order that step 1b retains; on C-SYM's effect side of GX+R-Y, the first effect row in frozen order that the effect-side step 1b retains. The certificate claims that row as a nonnegative combination of other retained rows (any fixed multipliers); C-CERT, and C-SYM's certificate check, must reject it. Do not use "the first listed row": on the effect side it may be a removable complement |
| B7 | **N8** E-ID identity (2085–2088) | Corrects `IMPL-DELTA-r14a.md` A8. The constant B3b's `user.login` check and the approval entries' `review` check read is the **reviewer** login: the second account under E-ID (i), `amaybaum` under (ii), (iii) and (iv). The session's identity under (iv) is recorded with E-ID and read by no condition; there is no "dispatcher rule" check in code, since `prevent_self_review` enforces it on the host |
| B8 | **N9** | none (drafting records only) |
| B9 | **§2 residuals** (790–791; 1847–1848; 1900) | none (labels and wording) |
| B10 | **optional: common clause** (857) | `note`'s and V's frozen common clause reads "(decided in this round as CC-F0, with its model verified)" in place of "(reproduced in this round as CC-F0, with its model verified)". The S4 self-test reruns over it |
| B11 | **optional: CONTEXTUAL text re-wrap** (903–907) | Whitespace only. If V compares the frozen texts with the preregistration's bytes rather than after whitespace normalization, the constant follows the new line breaks |
| B12 | **optional: G's configuration space** (647) | `IMPL-DELTA-r14a.md` A1 gains: G is built on H3's eight configurations `(z, x, η)`, its four laws the block-B rectangle at `η = 1`, with point reads on all eight configurations (not the carrier's four). Its frozen verdicts are the same on either space; the effect counts differ |

## Part C. Not to change

- Everything Part C of `IMPL-DELTA-r14.md` and `IMPL-DELTA-r14a.md` lists: the token rule, the frozen expectations,
  the budgets' freeze rule, the round-level VOID, and step 1b's conditionality.
- A3b keeps `if: ${{ always() }}`, and `fixture-mode-check` keeps exit 3 on a missing or non-fixture output: under
  Rc1 the rule reads A3's own conclusion beside A3b's, and A3b's behaviour is unchanged.
- The splice: r14b changes no line of the frozen workflow edit.
