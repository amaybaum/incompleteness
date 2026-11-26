# OI-QM-APPROX-1, unit 3: changes from REPORT.md (r1) to REPORT-r2.md

Each change answers one finding of the independent review of r1. That review is on PR #1596,
comment 7189898722, posted from the account `amaybaum` at 2026-11-26T10:50:04Z, carrying the
reviewer text verbatim, with verdict REVISE (minor). `REPORT.md` (commit `9d5b5dc1`) is
unchanged. No other statement, constant or status changes.

| Finding | Change | Where in r2 |
| --- | --- | --- |
| F1 (status) | The argument was re-derived before adoption (§A.22, §A.31): the quantifier order of M_C, a padding chosen for each protocol, the finite norms ‖G_{E_a}‖ and S for fixed (F, ρ), and the limit in τ. It holds, and is recorded as [A], with its origin in the review stated. Changes: the padding-defect floor τ_min is defined; Lemma 7η is stated with τ_min in place of τ; Corollary 7c (unit 2's Lemma 7 verbatim where τ_min = 0) is added; Theorem 8η gains its verbatim case; §6 (b) ⇒ (a) holds without a hypothesis on g; sufficient condition (iii) becomes "τ_min = 0"; the Q2-L7, Q2-T8 and Q3 rows are updated; O2-d is closed; §5.3 is scoped to bounds uniform over class(η) at fixed η > 0 and to theories with τ_min > 0; §5.6 adds the pressure test of Corollary 7c. | §0, §3, §5.2, §5.3, §5.4, §5.6, §6, §8, §9, §10, §11 |
| F2 | The convergence condition is stated: κ → 0 exactly when ω′g → 0. Under (Hg) alone, only κ ≤ 88ε + 2. Under (i) or (ii), κ → 0 (B1). If g depends on ε, convergence needs ω′g_ε → 0 jointly (B2). Theorem 8η: (N_Λ+1)κ_Λ → 0 for finite Λ under the same condition. | §0, §5.2 "Convergence", §5.4 |
| F3 | The constant is corrected: ω′ ≈ (3K − 4)τ_min, so the threshold is about 1/(8(3K − 4)τ_min), and 1/(16τ_min) at K = 2. It replaces 1/(24(K − 1)τ). | §5.3 |
| F4 | The quantifier is made explicit: g belongs to the chosen correspondence c′. Lemma 7η and Theorem 8η are stated for correspondences with terms at most ε that satisfy (Hg). Conditions (i) and (ii) make (Hg) hold for every such c′. | §5 preamble, §5.2, §5.4 |
| F5 | Theorem 3η's hypothesis reads "I_δ for the two-outcome family R_2, from level 2 into level L". C0 states that this is unit 2's hypothesis at η = 0. | §4.1, §4.3 |
| F6 | "min(d, 2) = 2" becomes "min(d, 2) ≤ 2". | §4.5 item 3 |
| F7 | `discardWith_uniform_one_eq_transport` is cited at OB/LevelOneSeam.lean:98. | §4.1, §8 |
| F8 | W4 adds "or a padding whose defect can be made small after those outputs are fixed". | §9 |
| F9 | No change to the grounds (G3, G1). The verdict is marked provisional until the delta review, and G3's scope follows F1. | §0, §9 |
| Owner's points | The unconditional converse is not described as disproved: Q2-L7 and Q2-T8 remain B4 for bounds uniform over class(η) at fixed η > 0, and §5.3 keeps "not a disproof". | §0, §5.3, §11 |
