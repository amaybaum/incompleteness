# Separate review of native_predicate_v8

- `round1/`: review of `375a29e4aa…`, the reviewer's directory `rev912d/`.
- `round2/`: re-check of `fc452ea825…`, its subdirectory `recheck/`.

Each report, `REVIEW.md` there, is kept as `REPORT.md`; the paths it cites
are relative to those directories. Kept: the reviewer's independent scripts
and their outputs, the mutant generators (`round1/indep/my_mutants.py`,
`round2/x0_mutants.py`) with their outputs, the uncatchable-mutant runner
`round2/rm_uncatchable.py` with its output `round2/empty3/u.out`, and the log
`round2/replay/replay.log` of the combined replay that an outside signal ended
during its mutant step (the standalone mutant rerun the report describes
completed and matched `mutants/mutants.out`).

Not kept, being byte-identical to committed files: the reviewer's copies of
the round files (`pkg/` at `375a29e4`, `recheck/D/` at `fc452ea8`); the
`out.json` of the normal and `-O` replays (`run1/`, `run2/`,
`recheck/replay/`), equal to `result.json` at the commit each targets; and
the `mutants.out` of the mutant replays (`runmut2/`, `recheck/replaymut/`),
equal to `mutants/mutants.out` at the commit each targets. Also not kept is
`runmut/`, the failing run of `375a29e4`'s runner with the relative `mut`
described in round 1's F1; that runner rebuilds it, and its output carries
the reviewer's absolute scratch path. The replays' exit status and timing
files are not kept, and neither are the generated mutant checkers (`mymut/`,
`recheck/x0mut/` and every `mut/`). These are rebuilt from `checks.py` at
the commit each targets, by `round1/indep/my_mutants.py`,
`round2/x0_mutants.py`, `round2/rm_uncatchable.py`, or the package's
`mutants/run_mutants.py` at `375a29e4` or `fc452ea8`. Paths are those of the
reviewer's directory `rev912d/`; `x0mut/`, `replay/` and `replaymut/` are
inside its `recheck/`.
