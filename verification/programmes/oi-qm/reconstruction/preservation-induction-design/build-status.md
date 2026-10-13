# Research-design compilation record

The preservation induction, finite branch sum, spectator and transport
corollaries compiled successfully at source commit
`e684897da41b1c3d066b880194c9beb87a19b7ad` on 2026-10-13.

- [Successful workflow run 38450187534](https://github.com/amaybaum/incompleteness/actions/runs/38450187534)
- [Compiler job 115478781754](https://github.com/amaybaum/incompleteness/actions/runs/38450187534/job/115478781754)
- Lean: `leanprover/lean4:v4.33.0`, with the repository's pinned Mathlib manifest.
- Compiled file SHA256: `f7a92732416f0d403ae68e8cc682f51ca8a0bf73742f6c83c92eb04d15571e51`.

All four printed axiom reports contain exactly `propext`, `Classical.choice`
and `Quot.sound`. The job contains no design error or `sorryAx` in those
reports. Both exact implementations reproduce their saved outputs and the
same job passes 303 legacy records, 46 receipts and artifact placement.

The first build at `476651fed70017543345bd784de95ead9f193ccf` failed because
the design omitted the `Matrix` notation and `SpectatorBridge` namespace
opens. The repair changes those opens and its digest; the mathematical
hypotheses, exact scripts and saved numerical outputs retain their content.

This is a compiled research-design conditional theorem. Physical primitive,
attachment and discard preservation is still assumed. Quantum/classical
Lean premise instances and prospective adoption remain open. The check
belongs to a separate research branch. No owner F designation, native
execution, receipt or adopted module is added.
