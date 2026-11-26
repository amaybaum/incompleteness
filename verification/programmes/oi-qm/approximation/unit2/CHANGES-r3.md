# OI-QM-APPROX-1, unit 2: changes from REPORT-r2.md (f257597b) to REPORT-r3.md

**Authority.** Owner decision at #1169 c.7186638587 (amaybaum, 2026-11-26T08:28:18Z), item 7. It authorizes the five findings of the focused delta review of r2, which is at PR #1584 comment 7185177023 (verdict ACCEPT WITH NITS). The same decision confirms two items, subject to verification of their proofs:
- the first review's bound 288ε for ε ≤ 1/64, which the bound 184ε for ε ≤ 1/48 implies;
- the negative cases m = 1 and K = 1.

The first review is at PR #1584 comment 7184945033. CHANGES-r2.md cited it as "#1169 comment 7184945033"; that citation is corrected here.

**Unchanged.** `PLAN.md`, `REPORT.md`, `REPORT-r2.md` and `CHANGES-r2.md`. Neither metric, the horizon (exactly K) and the scope are changed.

| # | Delta-review finding | Passage in REPORT-r3.md | Change |
| --- | --- | --- | --- |
| 1 | Finding 1: the review was cited at the wrong location | Header; §6 review row | The first review is cited as "PR #1584 comment 7184945033" and the delta review as "PR #1584 comment 7185177023". "#1184945033" is removed. |
| 2 | Finding 2: the unauthorized "≤ ε … attaining the bound" hypothesis | Lemma 7 statement; Theorem 8 statement | The hypothesis is again M_C(T, Q) < ε. Lemma 7 states that correspondences c, c′ then exist whose soundness and coverage terms are at most ε, and proves the bounds for any such c, c′. "Attaining" is removed. |
| 3 | Finding 3: wrong justification at m = 1 | §5, the "Outside m ≥ 2, K ≥ 2" paragraph after Corollary 10 | "(Theorem 4 needs neither restriction)" is replaced. At K = 1 with m ≥ 2, Theorem 4 applies. At m = 1, V_δ for every δ makes every single-outcome available family exactly trace preserving, so every m = 1 law is identically 1 on both sides and M_C = 0, with c arbitrary and c′ mapping to D_T. |
| 4 | Finding 4: Proposition 9's classification moved without a new result | §7 classification | Proposition 9 is back to ELABORATING, grouped with Theorem 8. NEW stays only on Proposition 11, whose origin is now noted. |
| 5 | Finding 4: credit | §6 review row; §7 Proposition 11 entry | The row states that the padding route of Lemma 7 and the construction of Proposition 11 originate in the first review. The written proofs and the constants 160ε and 184ε for ε ≤ 1/48 are attributed to this unit. |
| 6 | Finding 5: N_i undefined for instances without a base level of I | Corollary 10 proof, (b) ⇒ (a) | N_i = 1 for instances of V, U, C or L, giving ε ≤ min(1/48, δ/368). |
| 7 | Necessary consequences of rows 1–6 | Header (r3 authority, confirmation of values, both review identifiers); §9 replaced by points for any further review | No other passage changes. |

**Scope check.** No new premise, no manuscript change, no computation, and no change to either metric or to the horizon. All results and statuses are those of r2. The only changes are the hypothesis wording of Lemma 7 and Theorem 8 (row 2), the m = 1 justification (row 3), the classification of Proposition 9 (row 4), the attribution (row 5) and the constant (row 6).
