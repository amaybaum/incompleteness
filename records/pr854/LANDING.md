# PR #854 landed on main (2026-10-17 09:37Z)

- **Owner's approval:** "Yes I approve, please proceed as suggested", given in reply to the proposal to merge
  PR #854 at the exact accepted head `e3a44e63ebec41fccd109cf1ca945b3b8a200553`.
- **Pre-merge check** (held): `main` at `ea3155fdd7bf1d57ac285303c68ccba529e25b61`, and the PR head at `e3a44e63`.
  The integration tree was precomputed with `git merge-tree --write-tree` as
  `18d4d6ccdabef55f721f9f67d918c95fdf947d08`, and its diff from main equalled the PR diff.
- **Merge:** the PR was marked ready for review and then merged with the merge-commit method, with the head SHA pinned
  (`sha=e3a44e63…`).
- **Landing commit:** `49ba3297111acaf4d70cf3b932f44b3cc2129a2c`, "Merge #854: R1 evidence-retention hardening
  (reviewed head e3a44e63)".
  - Parents: `ea3155fd` (main) and `e3a44e63` (the accepted head).
  - Tree: `18d4d6cc`, identical to the precomputed integration tree.
  - Content: 6 files modified (+671/−51): `AGENTS.md`, `tools/release_gate.py`, and in
    `verification/audits/evidence-retention/` the files `README.md`, `check_retention.py`, `manifest.json` and
    `reproduce.py`.
- **Push CI on main:** `verify` run 39021837293 at `49ba3297` succeeded, with 22 successful jobs and one expected
  skip. Mathlib bridge job 117365034030 completed its build (3652 jobs), and all 22 release-gate steps passed:
  - `lean-axioms` reported 5989 named results.
  - The 303 legacy records in 75 closed namespaces were intact.
  - All 48 receipts held, and the V3 corpus passed with 140 vectors.
  - Evidence retention HOLDS in history mode, with 0 failures.
- **Refs:** the PR branch `draft/evidence-retention-r1-hardening-20261017` is absent after the merge, and this session
  did not delete it. The accepted commit is retained as the merge's second parent and on `wip/r1-hardening-fix-20261017`.
- **Not done:** no F/E designation, no edit to a frozen record, no workflow launch and no branch deletion.
