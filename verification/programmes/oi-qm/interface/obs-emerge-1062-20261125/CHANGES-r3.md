# #1062 OBS-EMERGE report r3: change map

- **Base.** `REPORT-r2.md` at commit `5fa09a08a54646575cdbf38435d46515a85cbb1e`. `REPORT-r3.md` is r2 with exactly the changes below; r1 and r2 stay unchanged beside it.
- **Review.** Independent delta review of r2, PR #1562 comment 7167101212 (ACCEPT-WITH-NITS).
- **Owner decision.** #1169 comment 7167242160 (amaybaum, 2026-11-25T15:41:53Z), quoted: "#1562 — Observer emergence | Apply nits 1–3." and "Produce a minimal r3 addressing only the identified findings. ... Do not reopen previously accepted results without new evidence of a defect."

## Applied

### Nit 1: G1 pressure test scoped to Main (§2, Q1, G1 pressure test)

The sentence was broader than its support: §1.3 records that GR uses a time-dependent partition for black holes (GR:40, :603).

- Old: "Every result built on `(S, φ, V)` uses a time-independent partition: the marginalization ..."
- New: "Every result of Main built on `(S, φ, V)` uses a time-independent partition, as does the kernel's lattice cut (GR's black-hole partition is time-dependent, GR:40, :603): the marginalization ..."

The list that follows is unchanged.

### Nit 2: the prime-|S| case is not a counterexample (§2, Q3, G3; §3, row 12)

The prime case is the absence of any product identification with both factors of size at least 2, vacuous given row 12's scope ("given the sizes of `C_V` and `C_H`"). The 2×2, cycle type (2,2) case is the counterexample.

- G3, old: "Not every non-trivial cycle type admits C4. Counterexamples, by hand:" followed by the sub-bullet "If `|S|` is prime, no product identification with `|C_V|, |C_H| ≥ 2` exists."
- G3, new: "Not every non-trivial cycle type admits C4. A counterexample, by hand:" (the prime sub-bullet removed), and, after the review-enumeration sub-bullet, a bullet: "If `|S|` is prime, no product identification with `|C_V|, |C_H| ≥ 2` exists. This is the absence of a product identification, not a cycle type without C4, and is not a counterexample."
- Row 12, conclusion, old: "Not every non-trivial cycle type admits C4 (prime number of states; 2×2 with cycle type (2,2)); which types admit C4 is open"
- Row 12, conclusion, new: "Not every non-trivial cycle type admits C4 (2×2 with cycle type (2,2)); which types admit C4 is open"

### Nit 3: row 12 class label (§3, row 12)

"PP-here" is defined as an argument "written in this report, not reviewed"; the (2,2) argument is the independent review's hand argument, restated.

- Old: "PP-here (hand argument) / OP"
- New: "PP (independent review's hand argument, restated) / OP"

### Status line (§ Status, pin and sources)

One bullet added after "Revision r2": "**Revision r3.** This revision applies nits 1–3 of the independent delta review of r2 (PR #1562 comment 7167101212), under the owner decision quoted in #1169 comment 7167242160 (2026-11-25T15:41:53Z): "#1562 — Observer emergence | Apply nits 1–3." (amaybaum, 2026-11-25, coordinating session). The change map is `CHANGES-r3.md`. All other text is unchanged from r2."

## Not applied (outside the owner decision)

- **Nit 4** (§1.2 class line: "KC … for the region entering `cutRealization` as a parameter" assigns a theorem class to a definition's signature). Not applied; the decision covers nits 1–3 only.
- **Nit 5** (Lemma 3 wording: state that ledger (iii) grounds Lemma 3's injectivity with the record-preservation argument). Not applied; the decision covers nits 1–3 only.

No other text of r2 is changed.
