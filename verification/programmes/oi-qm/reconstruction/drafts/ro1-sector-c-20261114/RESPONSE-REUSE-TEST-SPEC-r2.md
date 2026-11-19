# Response to the focused confirmation of REUSE-TEST-SPEC r2

**Review.** `REVIEW-REUSE-TEST-SPEC-r2.md`, blob `c66f190725f554ab099a032589fbfc5c6cf8bc8e`; verdict
ACCEPT WITH CHANGES. **Object reviewed.** `REUSE-TEST-SPEC-r2.md`, blob
`e1b29f1a825101f593439844b44abdbb70023262`, with `RESPONSE-REUSE-TEST-SPEC-r1.md`, kept on PR #1294 at
`445b47b5`; left unchanged. **Revision.** `REUSE-TEST-SPEC-r3.md`, unreviewed.

**Scope.** The three required changes and the four optional notes are applied; none adds a claim or
a premise. Everything else in r2 is unchanged. No decision rule is moved after data (§A.29), and
nothing is computed.

## Required changes

| Item | Finding | Disposition | Where in r3 |
|---|---|---|---|
| C-1 | Row 9 said "first half met at arm W", but U3 §10.3's first half is an L-2 consequence and L-2 does not apply to arm W; DR-3a's strict-(U) exclusion in arm W is definitional; the map did not say how a step removed by the fallback reads | **Applied.** Rows 9 and 10 now record setting-independence at arm W and state that L-2's half is not addressed there; row 9 states that the baseline exclusion is definitional. §5 and DR-3a state why: every program `Θ` identifies with arm W is case (N). A step removed by the fallback reads as `ns-unresolved` (DR-3) or `rep-unresolved` (DR-4) | §5 table and bullet; §8.2 DR-3a and fallback; §8.3 rows 9, 10 |
| C-2 | `φ` counted only the wing's own mismatches; a misapplied remote or first-use setting can break `a₂ = a₁` under strict (U), so DR-3a could exclude falsely | **Applied.** `φ_W(s; r)` is the rate of events, within the cell, in which any of the four applied settings differs from its intended value, with the event-by-event inequality `1[w₁ ≠ w₂] ≤ 1[any mismatch]` under strict (U) stated. C-13 counts all four settings on both wings | §7.1 φ; §9 C-13 |
| C-3 | C-1's χ² criterion does not establish `\|p − ½\| ≤ β` | **Applied, first form.** C-1(a) passes iff the upper confidence bound of each `\|p − ½\|` is at most `β`. Mutual independence of the bits, and their independence of the marker, index and earlier records, is stated as a hypothesis on the random sources; the χ² tests are necessary checks only, and the bounds use `β` under that hypothesis | §9 C-1 |

## Optional notes

| Item | Disposition | Where in r3 |
|---|---|---|
| O-a | **Applied.** DR-4's heading reads "in arm P it reduces to L-3 at `ε = 0`". Q-3's scope line states that Q-3 is per wing and that the one-wing remark concerns its DR-4 use | §8.2 DR-4; Appendix A, Q-3 scope |
| O-b | **Applied.** Full expected verdict vectors for CC-1 (i)–(iv), with DR-1 for (ii)–(iv) and (iv)'s DR-2, DR-3a and DR-4 as REV-2 §3 derives them; `Λ = 1` in (i). CC-1 is stated to evaluate DR-1 to DR-4 only. The synthetic sample size is declared at freeze, large enough for the 0.414 margin to resolve [DES] | §9 CC-1 and its [A-inf] |
| O-c | **Applied.** Appendix B counts sixteen half-weight terms (same total, about `270/√N`) and states the joint estimator's per-event range as 16, a factor of about 8 in half-width | Appendix B |
| O-d | **Applied.** §10.3 lists rows 1, 2, 6, 7, 8, 9 and 10 as leaving the agreement half open, in whole or in part | §10.3 |

## Points confirmed without change

REV-2's checks of R-1 to R-7, of T-C's Bayes step, of DR-3a's soundness, of the map's exhaustiveness
and fixity, of the CC-1 values and of the arm W threshold `η ≈ 0.9385` need no change.
