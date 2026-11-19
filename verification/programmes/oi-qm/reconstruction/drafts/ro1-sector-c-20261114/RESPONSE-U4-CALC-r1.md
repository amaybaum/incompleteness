# Response to the review of U4-CALC r1

**Review.** `REVIEW-U4-CALC-r1.md`, ACCEPT WITH CHANGES (PR #1294 at `b547c9f2`): no blocking findings,
10 required, 7 optional. **Revision.** `U4-CALC-r2.md`. r1 is unchanged. Hand calculation only; no
computation. Authorization: #1169 c.6891511297, item (2b).

## Required

| # | Finding | Disposition in r2 |
|---|---|---|
| 1 | Prop. 1.5 cites Instance 1.3 for the failed converse | Applied. It now cites C1-6 (with `5 | q` the marker spans `𝐑 ⊕ 5𝐑` alone; the environment site `e_1` fills the rest) |
| 2 | `d = 3` dropped in CALC-F3 and §3 | Applied. CALC-F3, §2.8 and §3 now read "native cubic torus (`d = 3`) with an even side `≥ 4`". Prop. 2.5 has a new bullet giving the `d = 2` (`M_0² = −I`) and `d = 1` (`M_{−2}^q = −I`, odd `q`) cases, which show the hypothesis is needed. That bullet is also control C2-6 |
| 3 | Prime-power `q` dropped from the A-cur ticks; aperiodicity on the `y_Σ`-marginal | Applied. §2.8 carries "for `q` a prime power", and for composite `q` other ticks are not excluded (R-3). Prop. 2.7 states the hypothesis on the `y_Σ`-marginal and gives the `ℤ/6` counterexample `β = 3`, `γ = 4` (control C2-7). This shows only that the algebraic step fails for composite `q`; whether such ticks occur on a torus stays in R-3 |
| 4 | R-1's "(every odd `q`)" | Applied: "native tori with all sides odd and `q ≥ 3`", noting that Prop. 2.5 covers only `q = 2` there |
| 5 | Theorem 2(c)'s negative rests on S-L2 [NP] | Applied. Theorem 2(c) is headed "given S-L2 [NP] (H-avail)", and it states that (a), (b) and (d) do not use S-L2. S-L2 [NP] is now named in §2.8, CALC-F3, §3's S-L3 bullet and the SNR-1 bullet |
| 6 | CALC-F2's "holds at `t ≤ 1` only" overstates | Applied with the reviewer's wording. The exact condition is stated with the `t ≥ 2` cases where masking is complete. "Records" now reads "holds a single-tick (R1) record of the carrier functional `q_t`". §3 states that a perfect path record of a point pair also uses the assumed point preparation |
| 7 | C1-1, C2-2 and C1-5 cannot fail | Applied. These three are relabelled CC1-1, CC2-2 and CC1-5, and the tables' headings now separate controls from consistency checks. The reviewer's two dual computations were re-derived by hand and adopted as controls: C1-4 (now computed, no longer only predicted) and the new C1-7 (dual of Instance 1.2). C2-6 and C2-7 are added as countercontrols for the two restored hypotheses |
| 8 | Directional gaps in Prop. 2.7 and Prop. 2.8(ii) (§A.34) | Applied. (a) Prop. 2.7's converse is written: `φ^t = γ·id` gives current slice `γy`; `φ^{t+1} = γ·id` gives `γx`. (b) Prop. 2.8(ii) now separates `B_t = 0 ⇒ K^D_t = R_D` (needs only H-μ) from J-return `⇒ B_t = 0`, which cites Theorem 2(a)'s hypotheses |
| 9 | §3 asserts a PLAN revision | Applied: "If owner question 1 is answered in favour of a revision, the sentence would be replaced" |
| 10 | Theorem 2(b)'s T0 clause | Applied. (b) identifies J-return and full return with the §5.3-equivalence part of T3's unconditional sub-label. The T0 clause is met only where a T0 witness exists, and T0 is not shown on K1 (U4 §3.2; MR★ σ1). §2.8 and CALC-F3 follow this wording |

## Optional

| # | Finding | Disposition |
|---|---|---|
| O1 | `A` names both the operator and the region | Applied in part. A notation bullet in §0 fixes the two readings, and Prop. 1.4 now writes the block `A_{AA}`, as the review does. Renaming the region throughout was not done: it would touch every `S_A`, `R_A`, `π_A` and `C = Σ ∪ A` at once, which risks transcription errors in verified formulas, while the two remaining ambiguous sites are resolved by the block notation |
| O2 | "Smallest nontrivial" unproved | Applied: removed |
| O3 | Rings excluded for every `L`, `q` | Applied as Prop. 2.5(c), re-derived (`v = 1`, `Av = 2v`, unipotent `M_2`). Instance 1.1 therefore has no J-return below recurrence for every `q`. The remark that the `d = 3` constant mode does not exclude (`ℤ/5`: `M_1³ = −I`) is added. §2.8, CALC-F3 and §3 list rings |
| O4 | CALC-F5's class | Applied: ELABORATING, as a scope limitation of CALC-F3 |
| O5 | AW-1's source | Applied. AW-1 now distinguishes the operation `φ^{N−1}` (`n = N − 1`, which MR★ σ6 and PLAN's S-L3 scope exclude) from the returns reached by `n = N − 1 − m` and `n = N/2 − m` |
| O6 | SNR-1 vocabulary | Applied: "reported as concerning an assumed apparatus (the prepared carrier), and it does not count" |
| O7 | Pressure test, one further step | Applied as an [A-inf] paragraph after Prop. 2.8: the marked-against-unmarked comparison is degenerate on K1 under μ-G. The pressure test in §2.8 also adds the reviewer's point that the negative is specific to the uniform background |

## Unchanged

The theorems, lemmas, instances and their proofs are as in r1, apart from the additions above; the
review re-derived them. The remaining steps are R-1 to R-7, with R-1 and R-3 rescoped.
