# UN-1: change map r1 → r2

r1 is `REPORT.md` (commit `d4d9846146f73f3ed80cb4f0846646a2d08aeb08`) and r2 is `REPORT-r2.md`.
`PLAN.md` and `REPORT.md` are unchanged. The findings are those of the independent review of r1,
posted on PR #1622 (verdict REVISE, minor; no mathematical error found). No proof changes.

| Item | Where in r2 | Change |
| --- | --- | --- |
| 1 | §0 outcome Q-A/Q-B; §5 | D2 is printed, as the rule's text requires. The scope is "τ_min = 0 at the level (padding rules in closure)", proved in unit 3 (Corollary 7c) and the predecessor (Theorem U (U-b)), and stated as inherited. The remainder (τ_min > 0, the large branch) stays obstructed |
| 2 | §0 outcome Q-C; §2 status of Q-C; §5 | Q-C prints "open". The small-branch derivation (Prop I (ii)) and Prop I (iii) are kept as sub-results |
| 3 | §2 Prop I (iii) and its proof | Adds M_C(T^{(L)}, Q) ≥ 1/184 at L, with the argument: τ_min = 0 at L (the available Lüders readout coarse-grains to a dephasing channel); Corollary 7c would give φ ≤ 184ε, while φ ≥ 1 |
| 4 | §3 T_S bullet; §8 | The T_S exclusion is split: for p > 4ε, coverage fails (term ≥ p/4); for p ≤ 4ε, Prop X1 bounds its norms as a gauge conjugate. The two cases cover every p. The predecessor's `PRESERVATION.md` is added as a support row in §8 |
| 5 | Header | States that the no-push, no-GitHub-write boundary applies to the writer |
| — | Title, revision note; §8 | Revision r2; PR #1622 added as provenance |

Sweep: no D4 verdict remains in r2.
