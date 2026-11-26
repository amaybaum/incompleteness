# F-SLICE-HZM: changes from REPORT-r2.md (r2) to REPORT-r3.md (r3)

r2 is `REPORT-r2.md` at `82b8ff3f17c8c947a7dc218ded9220ff235fdac8`, kept unchanged with r1. The review is the independent delta review of r2 posted verbatim on PR #1611, comment 7201250359 (posted from the account amaybaum, created 2026-11-26T19:09:09Z), verdict REVISE (minor). The coordinator's instruction directed applying findings 1–7. The review's finding 8 reports no register finding and needs no change.

| Finding | Change in r3 |
| --- | --- |
| 1 (Medium): "SMD on ρ is strictly stronger" is not shown by ρ_S | §3.4 states the implication (SMD on ρ ⇒ SMD on P_rest∗ρ) with its proof, and states what ρ_S shows: different stabilizers, not strictness. It adds witness ρ_T, the reviewer's candidate, checked by hand. F-stationarity of ν\|_S is checked: F preserves ν and q, hence S. P_rest∗ρ_T = ν satisfies SMD, and ρ_T does not. The strictness claim cites ρ_T in §0, §3.4, §5 (P2d), §9 and §10 (N-9) |
| 2 (Medium): "Equivalently" in the §5 P2d row | Replaced with "A sufficient condition is …" |
| 3 (Medium): the R2 alternative given for N-8 only | The outcome is stated by reading: R1 if N-1, N-2, N-8 and N-9 are all admitted readings; R2 if any of N-2, N-8 or N-9 is taken as a premise, with stopping condition 3; R3 if only the internal reading of P1 is admitted. Propagated to §0, §8, §10 and §13 |
| 4 (Low): step (c) said to be consumed in P2a | Step (c) is consumed in P2d only. P2a reads the joint law, but its inclusion holds for every ρ without step (c). Fixed in §0, §2 row 13, §3.2, §3.4, §5 (P2a) and §11 item 3 |
| 5 (Low): C−5 adds no power | §7 states that C−5 repeats C−1's computation and adds no power, and that C−1 is the one non-vacuous countercontrol for P2a |
| 6 (Nit): classification mismatch; source of §3.4 | §3.4 (ρ_S and ρ_T) is classified ELABORATING in both Pass 5 and the class table, and credited to finding 2 of the r1 review (PR #1611 comment 7201020516). Proposition P is the only borderline-NEW item |
| 7 (Nit): CHANGES-r2 row 6's location claim | CHANGES-r2 row 6 says the k used is stated in §0, §3.3 and §9. In r2, §0 states only d = 3, and §9 states no k. r3 adds d = 2 to §0, so both momenta are stated in §0 and §3.3, and §9 refers to them. CHANGES-r2 is kept unchanged |
