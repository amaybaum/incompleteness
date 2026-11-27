# Documentation corrections to revision r4 (Issue #1565, PR #1567)

This note maps the documentation-only nits of the focused independent review of r4 (PR #1567
comment 7172299731, verdict ACCEPT WITH NITS) to the files changed. Owner decision (`amaybaum`,
2026-11-25), verbatim: "Apply the independently reviewed documentation-only nits. Verify that
executable behavior and scientific acceptance criteria remain unchanged. No new independent review
cycle is required. The design remains adopted. Do not begin implementation yet."

**Goal link.** Verification integrity (Issue #1565): the documentation states the protection that
corrections 1 and 2 give as the review measured it. It decides no manuscript claim.

| Review finding | Change | Where |
|---|---|---|
| 1 Correction 2 checks writer-chosen evidence | Stated that correction 2 can be met by a wider span (the review's supposition, mention and question probes give exit 0), that the r3 review's three record probes are refused by correction 1, and that misleading-qualifier records on sentences without a hypothesis token remain reviewer judgment. | `DESIGN-r4.md` §3, §5; `CHANGES-r4.md` plain statement and finding 2 row |
| 2 Typographic H-token variants | Recorded as a known limitation: underscore italics, non-ASCII hyphens, `$H$-slope`, zero-width space. None occurs in active material at tree M. The pattern is not changed. | `DESIGN-r4.md` §5 |
| 3 Residual wider than code A | Stated that code-C findings with a hypothesis in a preceding sentence (and paragraph- or section-level hypotheses) escape, with the `papers/Substratum.md` `W-KDEG` example, and that extending correction 1 to the code-A window closes only the anaphora part. | `DESIGN-r4.md` §5, §7 question 1 |
| 5 nit Bare-head sweep | Stated that the sweep covered only the three named terms, and that `cubic`, `hidden`, `minim…` and `ignorance` remain single words, costing review load, not silent passes. | `DESIGN-r4.md` §1 item 4 |
| 6 Wrong section references | Three references to §4 corrected to §5. The prototype docstring cites DESIGN-r4 section 1 instead of section 2. | `DESIGN-r4.md` §0, §1, §3; `work/proto.r4.py` docstring |

Findings 4 and the rest of 5 and 6 asked for no change.

## Executable behaviour and acceptance criteria

- No executable statement, word list, control, result file or acceptance criterion changed.
  `work/proto.r4.py` differs from `57ccccb3` in one docstring line; with docstrings removed its
  abstract syntax tree is identical, and `work/run_r4.py` is unchanged. The docstring is printed on
  a usage error, so that message differs in the same line; the exit status (4) is unchanged.
- Re-run with the corrected files: `--self-test`, `--controls work/reviewer-heldout-W.json`,
  `run_r4.py compare`, `run_r4.py exitcodes` and `run_r4.py m2` give output byte-identical to
  `results-r4/`. The injection and tree-M scans were not re-run; the code they execute is unchanged.
- The exit-0 probes cited from findings 1 and 3 are the review's measurements; they were not added
  as controls.
