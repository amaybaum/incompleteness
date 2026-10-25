# Separate reviews of delayed_history_v7

- `round1/`: review of `114ad50203…` (the reviewer's directory `rev912/`).
- `round2/`: review of `74cdd24ee4…` and re-checks of `98cf4647e5…` and
  `656502989d…` (the reviewer's directory `rev912b/`).

Paths cited in the reports are relative to those directories. Each mutant's
`checks.py` is kept as `checks.py.diff`, a unified diff against `checks.py`
at the commit the mutant targeted: `114ad502` for `round1/mut/`, `74cdd24e`
for `round2/mut/` and `round2/mut2/`, `98cf4647` for `round2/mut3/` and
`65650298` for `round2/mut4/`. Running `round2/summarize.py` on
`round2/mut` with `result.json` at `74cdd24e` reproduces `mutants.out`.
`mutants3.out` and `mutants4.out` were written by a summary the reviewer did
not keep; the run outputs they summarize are retained.

Not kept, being byte-identical to committed files: the reviewers' copies of
the round files (`author/`, `c/`, `c2/`, `c3/`, `result_114.json`) and their
normal and `-O` replays (`run_*/`). Four `err.txt` files have the absolute
prefix of the reviewer's scratch directory removed from traceback paths.
