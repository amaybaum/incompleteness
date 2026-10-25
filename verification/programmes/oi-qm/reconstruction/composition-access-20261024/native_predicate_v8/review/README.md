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

Not kept: the reviewer's copies of the round files (`pkg/` at `375a29e4`,
`recheck/D/` at `fc452ea8`) and `recheck/replay/out.json`, all byte-identical
to committed files; and the generated mutant checkers (`mymut/`, `x0mut/`,
`recheck/*/mut/`), which the kept generators rebuild from `checks.py` at the
commit each targets.
