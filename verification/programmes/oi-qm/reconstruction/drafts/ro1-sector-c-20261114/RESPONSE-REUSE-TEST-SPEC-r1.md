# Response to the review of REUSE-TEST-SPEC r1

**Review.** `REVIEW-REUSE-TEST-SPEC-r1.md`, blob `aed9d8ca6fc03279a06c4d88ff830e6ffb016759`, retained on
branch `research/ro1-sector-c-1169-20261114` at `45517959` (PR #1294); verdict ACCEPT WITH CHANGES.
**Object reviewed.** `REUSE-TEST-SPEC-r1.md`, blob `07a6e9f768236586a590439435089fa4c3c5f115`, at
`bf809e3b`; left unchanged. **Revision.** `REUSE-TEST-SPEC-r2.md`, unreviewed.

**Scope.** Every required change is applied, and every optional item is applied. Nothing else
changes: the source, schedule S-R, the record schema's existing fields and both RR-1 forms are as in
r1. No premise is added, no decision rule is moved after data (§A.29), and nothing is computed. Each
countermodel and hand check cited from the review was re-checked by hand by the writer [A-inf].

## Required changes

| Item | Finding | Disposition | Where in r2 |
|---|---|---|---|
| R-1 (M-2) | Arm W is tick-indexed, case (N), so it is outside L-2; r1's "L-2 only" coverage and the `η_Aη_B > 1/√2` L-2 condition had no support | **Applied.** Arm W's coverage row now lists DR-3a and DR-4 (by Q-3) only, with "Not L-2" and the review's countermodel stated. DR-3 is restricted to arm P. §10.1's strict-(U) and RQ-UPD-1 bullets are restricted to arm P. The `η_Aη_B > 1/√2` condition is kept only as DR-1's precondition | §5; §7.2 rows ε, H; §8.2 DR-3; §10.1; Appendix A, use in DR-3 |
| R-2 (M-1) | The fresh fair-coin `⊥` rule breaks DR-3 (a (U) model with `S₁ = 3` and `ΣΔ = 0`); r1's §6.3 [A-inf] was false for it | **Applied.** The fresh per-`⊥` coin is removed. The structure-keeping set is `⊥ ↦ 0`, `⊥ ↦ 1` and one coin per wing per event, applied to every `⊥` of that wing in that event, recorded in the schema. The [A-inf] is restated for that set, with the per-`⊥` coin named as case (N). Exclusions are claimed only if they hold under every rule of the set (C-12). M-1's model is added to CC-1 | §6.1; §6.3; §8.2 DR-3a, DR-3, DR-4; §9 C-12, CC-1 |
| R-3 (§2.3, NEW) | Strict (U) is excluded by any repeat failure at a fully repeated joint policy; DR-3 subtracts exactly that baseline | **Applied.** New statistic `B_W(s; r)` and step DR-3a, an elementary step with no lemma, under (k1) or its dilation with noise in the unchanged source, (k2), (k5), with setting misapplication subtracted (C-13). DR-3 is stated to add an exclusion only where DR-3a returns `baseline-null`. The (N) class of unchanged `λ` with fresh local noise is stated as reached by DR-4, not by L-2. §10.1 names which route excludes strict (U) | §7.1; §7.2 row B and "The baseline dominates L-2"; §8.2 DR-3a, DR-3; §8.3 rows 5–9; §10.1 |
| R-4, countercontrol | No countercontrol showed that DR-3 and DR-4 can return unresolved on (U) and (N) realizations with `S₁ > 2` | **Applied.** CC-1, a freeze precondition specified and not run: the frozen code on synthetic records of TSI's (U) candidate, its fresh replacement (N), LREV R3's (S) realization and M-1's model, with expected verdicts fixed now and derived by hand. The optional laboratory emulator is listed | §9 CC-1 and its [A-inf]; §4.2; §11 item 3 |
| R-4, C-5 | C-5 injected into production events gives `ns-disagree` by construction | **Applied.** C-5 runs in a separate calibration block, never in production events, with a block-type field in the schema and a pass criterion | §6.1; §9 C-5 |
| R-4, C-6 and C-10 | No pass criteria | **Applied.** C-6: no slope of DR-2's statistics against strength or delay rejects zero at its weight. C-10: homogeneity across the remote settings at `e − 1` and `e − 2` not rejected at its weight. Every control in §9 now states a pass criterion, and §11 item 6 requires it in the checkpoint table | §9; §11 item 6 |
| R-4, T-C | Q-2 and Q-3 relate S₁ and ε on one ensemble; r1 mixed coincidence-conditioned S₁ with `⊥`-kept rates | **Applied.** T-C computes DR-1, DR-3a, DR-3 and DR-4 on the common subensemble `E₄` (all four uses detected), with fair sampling stated in model terms (the probability of `E₄` given `λ` does not depend on the policies; the review's stronger form is noted). DR-2 and C-9 stay on full records | §8.4 T-C |
| R-5 | The outcome map was not a function; arm-W-only runs had no row | **Applied.** An ordered map with precedence and ten rows covering every combination, per arm, with a stated exhaustiveness check. The case "strict (U) excluded with `rep-disagree`" keeps its strict-(U) verdict (row 4) | §8.3 |
| R-6 | CHSH orientation not pinned; `|S₁|` and `S₁` mixed | **Applied.** `S₁ := E₀₀ + E₀₁ + E₁₀ − E₁₁`, settings labelled so that ideal QM gives `+2√2`, fixed at freeze; Q-2 stated as `S₁ ≤ |S₁| ≤ 2 + 2Σδ`; all rules use `S₁` | §2; §4.2; §7.1; Appendix A |
| R-7 | Mao's per-acquisition settings are LIT's writer's reading; P-1's and P-2's arm P first uses are not on LIT's record; P-1's detection expectation unmarked | **Applied.** Mao's settings carry LIT's *[writer's reading]* label (LIT §1.8). P-1's local nondestructive detection of one ion of an entangled pair and P-2's full-strength coupling are moved to "Additions", with P-1's ancilla-mediated arm W use; P-1's detection expectation and first-record timing are marked [DES] | §3 |

## Optional items

| Item | Disposition | Where in r2 |
|---|---|---|
| O-1 | **Applied.** Q-3 is stated at its scope: no repeatability, no `Θ`, no (k5′), any first-use instrument, dilation carried over (the r1 caveat discharged on the review's check). DR-4 applies to arm W as a Q-3 statement; at ideal QM with `η_A = η_B = η` it can exclude for `η > (−4 + √(16 + 20√2))/(2√2) ≈ 0.9385` (the review's evaluation, re-checked by hand). Q-3 is stated not to be L-3 and not to extend it. Λ averages over both remote second settings, so the fixed constants `y₂*`, `x₂*` are removed | §5; §7.1 Λ; §8.2 DR-4; Appendix A, Q-3 scope and use |
| O-2 | **Applied.** One martingale bound per linear statistic `T₃`, `T₄` and per DR-3a cell, with Bonferroni weights; Holm is no longer used. Appendix B notes the factor of about 4 | §8.1; Appendix B |
| O-3 | **Applied.** A declared setting-bias bound `β` widens the confidence bounds; C-1 tests uniformity within `β` | §4.2; §7.1; §8.1; §9 C-1 |
| O-4 | **Applied.** Applied-setting readback per use and control C-13; DR-3a subtracts the mismatch rate | §4.1; §6.1; §7.1 φ; §8.2 DR-3a; §9 C-13 |
| O-5 | **Applied.** The repeat-failure statistics `B`, `Δ`, `Λ` are stated to be the same number in both forms, reported in both rows; only `H_W` differs | §6.2; §8.2 DR-3 |
| O-6 | **Applied.** `F_W` is arm P only, with arm W's QM value stated not to be 1/2; DR-6 is noted to be nearly automatic and is kept as L-3's part (c) | §7.1; §7.2 row F; §8.2 DR-6 |
| O-7 | **Applied.** The header lists every source of OI-attributed statements: L-2, L-3, Q-2, Q-3, the DR-3a step, SEL-EXCL-1's fresh-cell lemma [OFF] and LREV R3 [OFF]. §10.1's RQ-UPD-1 bullet carries `Θ` and Q-2 as well as L-2 | header; §10.1 |
| O-8 | **Applied.** The locality condition is stated per cross-wing pair, `t_reg − t_choice < L/c` in the laboratory frame | §9 locality row |

## Other points in the review

| Point | Disposition | Where in r2 |
|---|---|---|
| §4.1 (a)–(c): residual freedoms | (a) is R-6; (b) is O-2; (c) is R-2. All applied | as above |
| §4.2: freedom of choice for T-A | **Applied.** Setting draws outside the future light cone of the emission or herald, in T-A and C-11 | §8.4 T-A; §9 C-11 |
| §4.2: T-B "bounded by C-5 and C-6" | **Applied.** "probe specific couplings and do not bound unknown ones" | §8.4 T-B; §10.2 |
| §4.2: `c·max(τ_A, τ_B)` suffices | Superseded by O-8's per-pair condition | §9 |
| §5: §10.1's RQ-UPD-1 bullet | **Applied** under O-7 | §10.1 |
| §6: Q-2 literature check owed; pointer marked unverified by the reviewer | **Recorded** as an open freeze precondition, with the pointer described and its unverified status kept; no literature was read for r2 | §11 item 1 |
| §1.1: Q-2 tight on a PR–local mixture | **Recorded** in Appendix A | Appendix A, Q-2 |
| §1.2: no route via Bob's second output | No change needed; the derivation already uses `κ` only | — |
| §3: QM predictions | Confirmed by the review; no change, except O-6 | — |
