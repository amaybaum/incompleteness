# Parallel tracks — WIP / UNREVIEWED

Working records of the audit's parallel tracks, preserved as pushed checkpoints. Nothing here is
an accepted finding: each report is pending independent review, and its proposed replacement text
is a draft that is not applied to any manuscript.

- `D-c2-sc16/` — Track D: what (C2-structural) asserts; whether C1–C4 with any (C2) form imply
  P-indivisibility within an accessible window. Preregistration `PREREG.md` (frozen before
  computation), exact-arithmetic scripts and their outputs; `REPORT.md` lists the commands and
  expected outputs. Run each script from that directory with `python3 -I -B`.
- `C-consistency/` — Track C: global consistency audit report, its independent review (`REVIEW.md`, ACCEPT WITH CHANGES), and the classification note for
  `papers/Structure.md:1274`.

- `B-sc16/` — Track B: SC-16 proof attempt and exact countermodel search (preregistration, code, outputs, report,
  proposed edit list). Scripts import their siblings: run from that directory with `python3 -B <script>`.
- `xcheck/` — coordinator's independent re-checks: `six.py`, `sixgap.py` (the six-state countermodel), `c1perm.py`
  (a (C1) model whose rooted maps are all permutations). Run with `python3 -I`.
- `SC5-BACKFLOW-SENSES.md` — every "backflow" use classified by sense, with line counts for two renaming schemes.
- `SC22-N-regime/` — read-only audit of the book's 𝒩-regime vocabulary: inventory, missing definition, refuted links, proposed definition set and 56 rewrites (`proposals.py`). Run from that directory; `enum_window.py` and `blp_unbounded.py` take `.` as their argument.
- `SC23-fastbath-closure/` — fast-bath bound vs exact zero (F1) and one-step thermalization vs window-wide Markovianity (F2); preregistered, `f1.py` void, `f1b.py` and `f2.py` all controls green.
- `RECONCILIATION.md` — B/C/D agreement table, a premise inherited by Track B's E13/E14, the SC-16 site union, and the
  dependency order of the correction PRs.

Base for both: `main` at `a5168789` (Track D ran at `6bc2c4af`, whose manuscripts it cites).
