# Separate review of native_vread_v15

- `round1/`: review of `2c43d615a4…`.
- `round2/`: re-checks of `74541cf18b…`, `96bfc56c8d…` and `ca7d06de34…`.

The reports cite paths in the reviewer's working directory, `rev910d/` for
round 1 and its subdirectory `recheck/` for round 2; read those as `round1/`
and `round2/`. The reports are kept as `round1/REPORT.md` and
`round2/REPORT.md.txt` (round 2 repeats a heading, which the repository's
duplicate check rejects in a `.md` file). Round 2's `../REVIEW.md` is
`round1/REPORT.md`.

Kept: the reviewer's independent scripts and their outputs; the mutant
generator `round1/indep/rev_mutants.py` with its outputs; the three mutants
the reviewer wrote by hand, as unified diffs against `checks.py` at
`2c43d615` (`round1/indep/mutwork/*.py.diff`); and, for each
geometry-reader test, its changed checker and changed
`native_route_v13/checks.py` as unified diffs: `round2/asttest/` against
`checks.py` at `74541cf1`, `round2/asttest3/` against `checks.py` at
`96bfc56c`, and both against `native_route_v13/checks.py` as committed.

In the two injection tests (`route_injection_call`, `route_injection_ifexp`)
the reviewer's absolute marker-file path is replaced by `MARKER`. Their
changed checkers pin the unredacted route file, so a rebuilt test stops at
the pin check unless that path is restored or the pin updated.

Not kept, being byte-identical to committed files: the reviewer's copies
and replays of the round files; round 2's `mut_out.txt` and `mut3.txt`
(`mutants/OUTPUT.txt` at `74541cf1` and `96bfc56c`); and the copies of other
repository files the reader tests placed beside each changed checker. Not
kept as duplicates: round 2's `rev_mutants3.txt`, identical to
`round2/rev_mutants_out.txt`. Not kept, being rebuilt by
`round1/indep/rev_mutants.py`: the other generated mutant checkers.
