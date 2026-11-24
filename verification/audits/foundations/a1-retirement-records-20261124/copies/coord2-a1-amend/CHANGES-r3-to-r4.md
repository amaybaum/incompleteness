# Changes from r3 to r4, with the source of each

## Sources

- **R3-B1** and the review-r3 nits: review r3, `ab30b1a7…3ff9`.
- **O13:** the owner's O-13 request of 2026-11-24, quoted in O13-INVENTORY-r4.md.
- **W:** the writer.

The r1–r3 files are unchanged.

## Changes

| # | Change | Where | Source |
|---|---|---|---|
| 1 | D402's 1/α₀ clause is replaced by the reviewer's wording, unchanged: "and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, whose counterpart for a finite substratum and whose normalization of the vertex coupling are not established." | D402; §32.9 edit table | R3-B1 |
| 2 | The §32.9 1/α₀ row and open-dependency item 4 are corrected the same way. The row now cites :683–685 and :689. | §32.9 | R3-B1 |
| 3 | r3's reason for "over ℤ³" is withdrawn. P's INF scan does not match "infinite-lattice". | PROPOSAL-r4 §1 | R3-B1 (review's finding) |
| 4 | D403: "H-slope" becomes "H-slope on identified transitions", verbatim from GR:88 at H and at T1′. D403's reason text and the §32.9 row change to match. | D403; §32.9 | nit (optional, applied) |
| 5 | The A1 column of §32.9 reads "No use of A1 found in the cited derivation(s)". A sentence is added that this is not a statement of independence from A1. | §32.9 | O13 |
| 6 | The item-7 negative controls are extended to NC1–NC5 | `work-r4/item7_sim.py`; §32.9 results; PROPOSAL-r4 §3 | review r3 (NC1–NC5) |
| 7 | The configuration pins the r4 `ledger.json` and `edits.json` digests | `diffs-r4/CONFIG-r3-to-r4.diff` | consequence |
| 8 | Counts and pins are recomputed: `edits.json` `19eb79bd…6b4b`, `ledger.json` `d20495f0…0976`; 410 splices and 412 records (unchanged counts) | §32.10; PROPOSAL-r4 | consequence |
| 9 | O13-INVENTORY-r4.md, new: each change classified into the five categories, with citations, a strengthened? column, and the check for independence phrasing | new file | O13 |
| 10 | O13-DECISION-DRAFT-r4.md, new: draft owner wording that adopts exactly D402–D412 by hash and supersedes the clause only for them | new file | O13 |
| 11 | All checks re-run: P's checkers, item 7 and NC1–NC5, duplicate_check, gate tools, TeX | `work-r4/*.out` | coordinator |

## D402, r3 and r4

r3:

> … and $1/\alpha_0$ is the Brillouin-zone integral over $\mathbb{Z}^3$ of §6.1, whose counterpart for a finite
> substratum and whose normalization of the vertex coupling are not established.

r4, the reviewer's wording:

> … and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, whose
> counterpart for a finite substratum and whose normalization of the vertex coupling are not established.
