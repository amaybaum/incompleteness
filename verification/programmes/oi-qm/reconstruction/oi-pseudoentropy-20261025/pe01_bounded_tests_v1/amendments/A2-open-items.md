# PE-01 amendment A2: the five open plan items

The implementation of `../PLAN.md` (revision 5) and `A1-owner-decisions.md` found five points where the plan, as
written, does not determine the computation or how it is read. They are listed in `../pe01/pending.py`, each with the
readings the code computes. This amendment fixes one reading for each. It is committed before the verdict-bearing
run, and no result of that run existed when it was decided.

The plan's text, conditions (a)–(f), thresholds, window, controls, classification and stopping rules stand as
reviewed and as amended by A1. No item below changes them. Each item fixes how a point the plan leaves open is
computed or read.

- **Decided by:** the owner (amaybaum), 2026-10-26, after the independent code review accepted the implementation at
  `07f3c127` with nits.
- **The owner's statement of the sign decision:** "We should not strengthen the criterion after seeing smoke-test
  results, particularly when doing so makes counterexamples harder to find."

## Decisions

1. **B3W-K0 (B3 window class, K0).** Owner: "Exact average, with a worst-case interval".
   - The average case is exact, by stationarity and sign-pattern decomposition over the union of supports.
   - The deterministic worst case is exact for $w \le 4$. For $5 \le w \le 16$ it is reported as an interval, exact
     only where its ends coincide.
   - An interval bears on no verdict.
2. **LF-A (linear-filter observers).** Owner's table entry: "Passive, not part of the deciding criterion"; superseded by the owner's clarification below.
   - Linear-filter observers are passive ($a \equiv 0$) and are named "passive linear filters" in every output.
   - **Clarification.** Under the frozen plan any explicit-table observer meeting (a)–(f) is a COUNTEREXAMPLE, so
     excluding linear filters from the deciding criterion would narrow it after smoke results. Asked, the owner first
     answered "No preference", then clarified on 2026-10-26: "Linear-filter observers: Passive in the sense that they
     do not adapt their strategy, but fully eligible to produce deciding counterexamples. Every eligible explicit-table
     observer counts, including linear filters and the cells they uniquely reach." and "The governing principle is
     that no observer class or counterexample is excluded merely because it makes the claim harder to sustain."
   - A passive linear-filter witness meeting (a)–(f) is therefore a COUNTEREXAMPLE, and the criterion is not
     narrowed.
3. **WIT-A (condition (a)).** Owner: "Restrict to the three fixed generators".
   - Condition (a) is read as $\varphi \in \{$`G_lin`$(p_n)$, `G_filt`$(p_n)$, `G_clk`$(p_n)\}$.
   - The other family members enter through the K0 status only. This reading is conservative toward the claim under
     audit.
4. **TAG-L (COVERED-literature tags).** Owner: "Mechanical comparisons; preserve conservative L2".
   - COVERED-literature is assigned by the mechanical comparisons L1–L4 of `../pe01/pending.py`, with COVERED-corpus
     taking precedence.
   - L2 compares the B2 K1 horizons (maximum over $\lambda$) with the closed form at $\lambda = n+1$. This never gives
     a false COVERED tag.
   - Tags bear on no verdict.
5. **D-SIGN (condition (d)).** Owner: "the plan's original literal reading". Owner: "Retain the signed version as a
   separately reported sensitivity analysis. Both should be computed on exactly the same frozen data, without changing
   the governing criterion afterward."
   - Owner, 2026-10-26: the |adv| rule "is the primary deciding rule, exactly as written in the original plan. The
     signed rule is computed and reported separately as a sensitivity analysis, without changing the primary
     verdict."
   - **The governing rule is the literal §2 definition, `abs`:** $|\Pr[\chi = X_{K'}] - 1/2| \ge 1/8$ at every
     $K' \in [K-3, K]$, for the same $O$ and $\chi$. This is the COUNTEREXAMPLE rule and decides the verdict.
   - **The sensitivity analysis is `signed`:** $\Pr[\chi = X_{K'}] - 1/2 \ge 1/8$ at every $K'$, for one $\chi$.
     - It is computed on the same measurements and reported in its own section, labelled as a sensitivity analysis.
     - It never changes the governing verdict.
     - Every signed window is an `abs` window, so the sensitivity analysis can narrow the governing result but never
       extend it.
     - A COUNTEREXAMPLE under the governing rule stands whatever the signed analysis shows.
     - The verdict text states which rule governs.

## Results

- The verdict is the governing classification of `../verdict.py` under these readings.
- A VOID or INCOMPLETE stage, a bound, or an interval is never reported as a proof.
- Every horizon prints as PROVED only where it is exact and determined.

## Readings read by the checker

TH reads the block below from this file. It records the block with this file's blob id and with the commit that
`../pe01/params.py` pins as `A2_COMMIT`. A run in result mode refuses to start if:
- the block is unreadable;
- any item is unresolved;
- a reading is not among those `../pe01/pending.py` lists;
- the file has changed since the pinned commit.

```json pe01-resolutions
{"amendment": "A2", "resolves": {"B3W-K0": "exact-average+interval-worst", "D-SIGN": "abs", "LF-A": "passive", "TAG-L": "L1-L4", "WIT-A": "fixed-primary"}}
```
