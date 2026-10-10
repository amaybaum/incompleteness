# AUDIT-R addendum — independent recount of R6's tables (written after T6's launch; AUDIT-R.md itself is frozen at the hash `04308355…` handed to T6)

`pt/audit/stage6-inputs/T-audit/r6_rows.py` (run 1, 5/5 `R6-ROWS-FIXED`, replay byte-identical) parses the three
verdict tables from the markdown of `pt/R6/REASSESSMENT.md` — not from R6's `r4_tables.out` — and confirms:

- three tables (A1 K(E0), A2 K(Z_F), A3 EXOTIC-E) of 199 item rows each, with identical ids;
- tallies 118 SATISFIES / 13 FAILS / 68 NOT REACHED for A1 and A2, and 118 / 12 / 1 UNDECIDED / 68 for A3;
- the 13 FAILS ids are I3.133, I3.135, I3.137, I3.142, I3.144, I3.150, I3.151, I3.152, I3.153, I3.155, I3.160,
  I3.161, I3.165, with I3.161 UNDECIDED in A3;
- every FAILS row is of a hypothesis class (dna 9, d4f 2, cand 2); every `hmg` row (56) and `nr` row (12) is NOT
  REACHED; class counts per table: b1 13, cand 2, cone 12, d4f 2, d4s 1, d4v 3, def 12, dna 9, gate 7, hmg 56,
  inh 46, kthm 1, nr 12, thm 23.

The row table `T-audit/r6_rows.tsv` (597 rows: table, id, class, verdict) is the reference against which T6's
row-by-row citations are checked in AUDIT-T.
