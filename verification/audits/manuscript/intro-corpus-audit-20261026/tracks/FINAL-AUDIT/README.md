# Final consolidated consistency audit of `main` at `55e3217b` (WIP)

Read-only, in three independent slices, after #947–#955 merged. `55e3217b` is the merged tree of #955, so the residual
sites the slices report were missed by the correction rounds; the slices did not see pre-merge wording.

- `slice1-main-companions.md` — Main and nine companion papers: claim table, regression sweep, new findings.
- `slice2-book-explainer-intro.md` — book, FULL mirrors, Explainer, and the Introduction (#918) alignment list.
- `slice3-lean-receipts.md` — local gate, V3 receipts, legacy records, coverage ledger, census, guards, probes, main CI,
  and the Lean-against-manuscript comparison.

High-severity findings, with owner-authorized separate correction PRs (2026-10-27):
- Medicine :25: "any embedded observer … necessarily non-Markovian" (slice 1, D-0);
- Main §3.5 rest-frame "iff": only one direction proved (slice 1, D-1).
