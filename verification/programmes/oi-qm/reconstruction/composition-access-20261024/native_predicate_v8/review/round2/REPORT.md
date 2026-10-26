VERDICT: ACCEPT — fc452ea825b986a3babab5d110626e0019c39847 (review fixes on 375a29e4)
OVERALL VERDICT on 631bec0ca55eacbf6a7cf7e72d72c673dfe430da..fc452ea825b986a3babab5d110626e0019c39847: ACCEPT. The scoped negative result for C(4,16) in the scaled control stands. The only open item is F7, a propagation note to `CURRENT-HANDOFF.md` that is due once the review lands.

This is a read-only re-check. Package files exported from git at fc452ea8 are in `D/`, and my scripts and outputs are in this directory. The clone was not modified: `git status --porcelain --ignored` is empty and HEAD is fc452ea8.

## Commit shape
- fc452ea8 has a single parent, 375a29e4.
- `git diff --name-only 375a29e4 fc452ea8` touches only `native_predicate_v8/`: PROVENANCE.json, REPORT.md, SHA256SUMS, checks.py, mutants/mutants.out, mutants/run_mutants.py and result.json. PLAN.md is unchanged, and its SHA256SUMS line is identical.

## Findings from the first review
- **F1, resolved.**
  - `run_mutants.py` now takes `os.path.abspath(sys.argv[2])`, exits 1 unless every mutant is caught, and records `unparsed output, exit status N` instead of the stderr text.
  - I ran the REPORT's documented command exactly as written from an empty directory, with `mkdir mut` and the relative `mut` (`replaymut/log`). It exits 0 in 6 min 15 s, and its output is byte-identical to `mutants/mutants.out`.
  - To test the failure path I used a copy of the runner holding two mutants that cannot be caught (`rm_uncatchable.py`, run in `empty3/`):
    - a scope break aimed at the wrong control, which gives VOID at x0 and is not caught;
    - a syntax error, which gives UNPARSED with exit status 1.
    - That run prints `all_caught: false` and exits **1**.
  - A missing work directory raises a traceback and exits 1, which is acceptable because the recipe runs `mkdir` first.
  - One environment note: my first combined replay was killed by SIGTERM (exit 143) partway through the mutant step, from outside the package. The standalone rerun above completed cleanly.
- **F2, resolved.**
  - The new required control x0 pins n=6, ρ=4, τ=16, TEND−NS=17, R0=ρ+TEND, 129 region sites, 3,225 site-times, and the exact ordered site-time list against `sorted(ball(4))` × slices −1..n+17.
  - The scope string is now generated from the parameters. Its text is unchanged, as the leaf diff below shows.
  - The author's m10 and m11 (my R1 and R8) give VOID at x0.
  - My additional x0 mutants (`x0_mutants.py`, `x0_mutants.out`):

    | mutant | change | outcome |
    | --- | --- | --- |
    | X1 | region shifted by (1,0,0), same size | VOID at x0 |
    | X2 | slices 0..n+18, same count | VOID at x0 |
    | X3 | same site set in a different order | VOID at x0 |
    | X4 | one region site swapped for (5,0,0) | VOID at x0 |
    | X6 | n=7 | VOID at x0 |
    | X5 | `ball()` itself shifted | passes x0, then the checker crashes (KeyError, exit 1) |

  - X5 passes x0 because the reference list is built with the same `ball()`, but it fails loudly rather than giving a silent verdict. This is informational only; no change is needed.
- **F3, resolved.** m4c, which is my R7 (the law statistic checks only the 20/44 block sizes), is in the runner and is caught at x4.
- **F4, resolved.** The text now reads "carry no information beyond V given C0", and states that the count includes the V cell, q9 at n+2. This matches my independent finding.
- **F5, resolved.** "In the scaled control" is added to the opening verdict line and to the "settles that form" sentence. The subject of the historical commit 375a29e4 is left as it was, which is correct: history is preserved.
- **F6, resolved.** The text now says that pads and mixtures over backgrounds are one open branch, and that conditioning on C0 is what stops background bits from acting as pads. It gives the (A, Y⊕c, ·) example. That example claims only that Y does not leak on average, not that the target law holds, so there is no overclaim.
- **F7, open (propagation note, not a defect of this commit).** `CURRENT-HANDOFF.md` still does not mention v8. Add the scoped v8 result to it when the review lands, as was done for v7.
- **F8, resolved.** The text now says the G-arrival mapping holds by construction and confirms that the offsets were transcribed correctly, not that the dynamics are faithful.

## result.json, verdict and replay
- Leaf diff from 375a29e4 to fc452ea8:
  - added: `required_controls.x0_scope_parameters = true` and `post_review_rows[0]`;
  - removed: none;
  - changed: none.
- The verdict is still `NEGATIVE_FOR_CONSTRUCTION`.
- I ran `python3 -I -B checks.py` and `python3 -I -B -O checks.py` from an empty directory (`replay/replay.log`). Both outputs are byte-identical to `result.json`.
- `sha256sum -c SHA256SUMS` passes for all 7 files.
- `mutants.out` differs from the old one only by the three added entries, m4c, m10 and m11, each caught. The original 11 entries are unchanged. All 14 mutants are caught, and m9 still gives HOLDS_WITHIN_SCOPE.

## Wording and hygiene
- No new overclaim. The process notes in REPORT and PROVENANCE ("Added after review", the post-review change list) are acceptable in a verification record.
- One cosmetic nit, no action needed: a line in the REPORT's Replay paragraph wraps unevenly.
- The package contains no absolute paths, emails, IPs or tokens, and the tree has no `__pycache__`.
- I ran the three repo checks from the clone root at fc452ea8. All pass, and the worktree is unchanged afterwards:
  - `tools/duplicate_check.py`: OK;
  - `tools/voice_check.py`: OK, 40 files;
  - `tools/artifact_placement_check.py`: OK, self-test passed.
