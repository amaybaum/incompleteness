# Separate review of native_vread_v15

- `round1/`: review of `2c43d615a4…`, the reviewer's directory `rev910d/`.
- `round2/`: re-checks of `74541cf18b…`, `96bfc56c8d…` and `ca7d06de34…`,
  its subdirectory `recheck/`.

Each report, `REVIEW.md` there, is kept as `round1/REPORT.md` and
`round2/REPORT.md.txt` (round 2 repeats a heading, which the repository's
duplicate check rejects in a `.md` file); the paths each cites are relative
to those directories. Kept: the reviewer's independent scripts
and their outputs, the mutant generator `round1/indep/rev_mutants.py` with
its outputs, and, for each geometry-reader test, its changed checker and
changed `native_route_v13/checks.py` as unified diffs: `round2/asttest/`
against `checks.py` at `74541cf1`, `round2/asttest3/` against `checks.py` at
`96bfc56c`, and both against `native_route_v13/checks.py` as committed. In
the two injection tests the reviewer's absolute marker-file path is replaced
by `MARKER`.

Not kept: the reviewer's copies of the round files and their replays, which
are byte-identical to committed files; generated mutant checkers, which the
kept generators rebuild; and the copies of other repository files the
reader tests placed beside each changed checker, which are unchanged.
