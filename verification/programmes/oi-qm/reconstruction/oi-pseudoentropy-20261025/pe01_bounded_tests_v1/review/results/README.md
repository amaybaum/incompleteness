# Independent review of PE-01's results

`REVIEW.md` is the independent results review of run 40271434371, at head
`549641460b8ddb536178f95fac2ec9390e84a987`. Its verdict is **CONFIRMED AT NARROWER SCOPE**. It is byte-identical
to the reviewer's record.

`mine/` holds the reviewer's own scripts, written from `../../PLAN.md` alone. They import nothing from the package,
and each was replayed:
- `indep.py` recomputes the witness's advantage curve under the plan's and the reciprocal tap conventions.
- `witness.py` runs the full clocked-composite checks: EX1, EX4–EX8, the readout and normalization.
- `mech.py` checks that the guess equals the control-bit/output coincidence.
- `detail.py` gives the canonical forms of the cell's observers and the readout through the output register.
- `family.py` evaluates the witness on the other members of the family, giving its K0 status.
- `search.py` is an exhaustive search of all m ≤ 2 observers over every admissible cell. Its output is
  `search_out.json`, which reproduces byte for byte.
- `plin.py` spot-checks passive linear filters at m = 3, n = 7 and 8.

Commands, run from `mine/`: `python3 -I -B <script>.py`. The scripts expect no arguments, and `search.py` writes
`search_out.json`.
