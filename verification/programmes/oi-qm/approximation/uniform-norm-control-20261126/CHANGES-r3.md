# Uniform norm control: change map r2 → r3

r2 is `REPORT-r2.md` (commit `1f49e6beda01526faf6b1a32204fdd225abfecb1`) and r3 is
`REPORT-r3.md`. `PLAN.md`, `REPORT.md`, `REPORT-r2.md` and `CHANGES-r2.md` are unchanged. The two
nits are those of the delta review of r2, posted on PR #1614 (verdict ACCEPT WITH NITS). The change
is to text only; no result, proof or status changes.

| Nit | Where in r3 | Change |
| --- | --- | --- |
| 1 | §5 CC-p, the paragraph after "Coverage"; §9 CC-p row | "Law boundedness alone, F1, does not bound the norms" and "the coverage term … is what excludes it" become "F1 alone does not bound the norms; whether the soundness term alone does is not tested by CC-p", and the coverage term "excludes T_S". The §9 row drops "the coverage hypothesis is load-bearing" and carries the same sentence |
| 2 | §3 (U-a) | The broken opening "If an admissible pair (c, c′) has φ := …, then" becomes "For an admissible pair (c, c′), with φ := ‖c′(P) − id‖_{1→1}:" |
| — | Title and revision note | Revision r3 |
