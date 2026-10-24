# Independent review of the bounded native instrument

`REVIEW.md` is the independent review of this directory's record at `455eb092`, by a reviewer outside the work's
author. Verdict: accept with corrections. Its corrections are applied to `../README.md`, `../REPORT.md` and
`../instrument_checks.py`, whose saved output is regenerated.

The reviewer's scripts import nothing from the author's checker. Each replays to its saved output with `python3 -I -B`
from this directory, with one exception: the last line of `indep_degree_qm.out`, the weight of a degree-2 flag on 20
bits, is not printed by `indep_degree_qm.py`. `coordinator_weight20.py` reproduces that value, by enumeration and in
closed form (`coordinator_weight20.out`).

`SHA256SUMS` lists every file here.
