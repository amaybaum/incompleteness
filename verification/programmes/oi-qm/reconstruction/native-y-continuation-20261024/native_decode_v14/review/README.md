# Separate review of native_decode_v14

- `round1/`: review of `7f843073d9…` (plan `36213be6…`, status text at
  `cd9390a0…`).
- `round2/`: re-review of the text correction `96b92f39…`.
- `round3/`: re-check of the attribution fix `1c15797a…`.

The reports name the reviewer's working directory `rev910b/`; read it as
`round1/`. Round 3's own re-check files were not kept; the checks it reports
(empty diffs of the evidence files, the v14 replay and the manifests at
`1c15797a`) run from that commit.

`round1/out/` holds the outputs of the reviewer's scripts, the author
checker's normal and `-O` outputs (`author_*.out`, byte-identical to
`result.json`), and the mutant runs: `m*.out` is each mutant's standard
output, empty, and `m*.err` its standard error, ending in the control that
failed and the exit status. `round1/make_mutants.py` rebuilds the mutants.
`replay.py` runs `round1/review_checks.py` and compares it with
`round1/out/review_checks.out`.

Not kept: the exit-status and timing lines of the author runs and of the
reviewer's `replay.py --latest` run. The run times are those in
`round1/REPORT.md`, and `replay.py` reproduces that replay's five group lines.
