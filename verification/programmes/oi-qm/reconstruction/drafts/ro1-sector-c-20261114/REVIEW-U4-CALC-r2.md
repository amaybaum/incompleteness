# Focused confirmation of U4-CALC r2 against the review of r1

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/U4-CALC-r2.md`
and `RESPONSE-U4-CALC-r1.md`, at PR #1294 head `213e3981dad063fd71e041eddc9e2ce1c0a6d116`.
**Baseline.** `REVIEW-U4-CALC-r1.md` (this reviewer), on r1 at `f86dd1f7`.
**Reviewer.** Independent, non-author. Read-only.
**Method.** Every new or changed mathematical statement was checked by hand, using exact algebra and
2×2 matrix powers. No program computed or enumerated anything. Git was used only to read files, diff
r1 against r2 and check digests.

## Verdict: ACCEPT. r2 is ready for owner acceptance.

All ten required findings are resolved, and so are the seven optional ones; O1 is only partly done,
for a stated reason that holds. The new controls check by hand. The `ℤ/6` narrowing is correct, and
it corrects an overstatement in my r1 review. No unlisted change was found. Two optional wording
points follow; neither bears on owner acceptance.

***

## 1. The ten required findings

| # | r1 finding | r2 | Status |
|---|---|---|---|
| 1 | Prop. 1.5 cites Instance 1.3 | Now cites C1-6: with `5 | q` the marker alone spans `𝐑 ⊕ 5𝐑`, and `e_1` fills the rest. Correct | resolved |
| 2 | `d = 3` dropped | CALC-F3, §2.8 and §3 read "native cubic torus (`d = 3`)". Prop. 2.5 gains a dimension bullet and part (c) for rings | resolved |
| 3 | Prime-power `q`; `y_Σ`-marginal | §2.8 carries "for `q` a prime power" and "for composite `q` other ticks are not excluded (R-3)". Prop. 2.7 states the `y_Σ`-marginal hypothesis, with the correct reason: the readable `Σ`-marginal is a convolution with the uniform law on the current-slice leakage group | resolved |
| 4 | R-1 "(every odd `q`)" | "native tori with all sides odd and `q ≥ 3`", noting that Prop. 2.5 covers only `q = 2` there | resolved |
| 5 | S-L2 [NP] not carried | Named in the heading of Theorem 2(c), in §2.8, CALC-F3, §3's S-L3 bullet and the SNR-1 bullet. The statement that (a), (b) and (d) do not use S-L2 is correct: (b)'s "every continuation" holds for every continuation, available or not, once `P_t = P_0` | resolved |
| 6 | CALC-F2 "only" | Exact condition stated. The `t ≥ 2` examples of complete masking listed are the ones I gave. "Single-tick (R1) record of `q_t`" is used, and §3 names the assumed point preparation | resolved |
| 7 | Controls that cannot fail | Relabelled CC1-1, CC1-5 and CC2-2. The table headings separate controls from consistency checks. C1-4 is now computed and C1-7 is added. CALC-F1 no longer cites the consistency checks as controls | resolved |
| 8 | §A.34 directions | (a) The converse of Prop. 2.7 is written out and correct. (b) Prop. 2.8(ii) separates `B_t = 0 ⇒ K^D_t = R_D` (which needs H-μ only) from J-return `⇒ B_t = 0` (Theorem 2(a)'s hypotheses) | resolved |
| 9 | §3 asserts a PLAN revision | Now conditional on owner question 1 | resolved |
| 10 | T0 clause | (b) is stated as coincidence with the §5.3-equivalence part of T3. The T0 clause is met only where a witness exists, and T0 is not shown on K1, with citations. §2.8 and CALC-F3 follow this wording | resolved |

## 2. The new controls, re-derived by hand

**C1-4 (dual count for Instance 1.1, `t = 2`): correct.**
- Write `α_0 = aδ_3 + bδ_0` and `α_{−1} = cδ_3 + eδ_0`. Using `Aδ_3 = δ_2 + δ_0` and
  `Aδ_0 = δ_3 + δ_1`, `α_1 = aδ_2 + bδ_1 + (a − e)δ_0 + (b − c)δ_3`.
- Support in `A` forces `e = a` and `c = b`. Then `α_2 = Aα_1 − α_0 = aδ_1 + bδ_2`.
- The readout `c = (α_2, −α_1)` gives `a(u_1(1) − u_2(2)) + b(u_1(2) − u_2(1))`.
- Its value is `α_0·x − α_{−1}·y = a(x_3 − y_0) + b(x_0 − y_3)`, which is the quotient found by
  direct expansion.
- Under A-cur, `α_2 = 0` forces `a = b = 0`.
- The control is independent of the direct computation, and it could have failed.

**C1-7 (dual of Instance 1.2): correct.** The annihilator of `K_2 = {(−x_0, 5y_0)}` gives `c₁ = 0` and
`5c₂ = 0`, so `α_2 = 0` and `α_1 = −c₂δ_0`. Running the recurrence backwards:
- `α_0 = −c₂Σ_{j∼0}δ_j`;
- `α_{−1} = −c₂(A²δ_0 − δ_0) = −c₂(5δ_0 + Σδ_{±2e_c} + 2Σδ_{±e_c±e_{c′}})`;
- the value is `c₂ f(s_Σ)`. This agrees with `c₂ u_2(0) = c₂(5y_0 + f)` when `5c₂ = 0`.

The `c₂ = 0` branch for a unit `5` is the independent check that CC1-5 lacked, as r2 says.

**C2-6 (countercontrol for `d = 3`): correct.**
- On a ring, the alternating vector gives `M_{−2} = −I + N′`, with `N′ = [[1,1],[−1,−1]]` and
  `N′² = 0`.
- So `M_{−2}^t = (−1)^t(I − tN′)`, and `M_{−2}^q = −I` for odd `q`.
- The same bullet's `d = 2` case checks: `M_0 = [[0,1],[−1,0]]` and `M_0² = −I`.
- So does the `d = 3` constant mode: over `ℤ/5`, `M_1² = [[−1,1],[−1,0]]` and `M_1³ = −I`.
- C2-6 is scoped correctly as "(b)'s argument does not transfer". It does not say rings admit a
  return, and the new Prop. 2.5(c) excludes them.

**Prop. 2.5(c) (rings): correct.** `v = 1` gives `Av = 2v` when the two neighbours are distinct
(`L ≥ 3`), so `φ` acts by the unipotent `M_2` and every scalar power is `I`. Instance 1.1 therefore has
no J-return below recurrence for any `q`.

**C2-7 (countercontrol for the prime power): correct.** Over `ℤ/6`, `β = 3` and `γ = 4` give
`βγ = 12 ≡ 0` and `β² + γ² = 25 ≡ 1`, with neither of them `0`.

## 3. The `ℤ/6` narrowing: correct

C2-7 shows that the algebraic step of Prop. 2.7 (one of `β`, `γ` is `0`) fails for composite `q`. It
does not show that a torus realizes `U_{t−1} = 3I`, `U_t = 4I`. My r1 finding 3 said the mixed case
"gives background-free ticks" other than `N − 1`, `N/2 − 1` and `N/2`. That went beyond what I had
shown, and r2's narrowing is the correct scope.

By CRT, such a tick needs both of the following:
- `φ^{t+1}` scalar in the `ℤ/2` component, that is `t + 1 ∈ N_2ℤ`, since only `γ = 1` exists there;
- `φ^t` a scalar `γ ≡ 1` in the `ℤ/3` component.

Whether the two congruences have a common solution below `N − 1` depends on the orders of `φ` in the
two components. That is a per-torus question, correctly left in R-3.

## 4. Nothing else changed

I diffed r1 against r2 word by word. Every change is one of the following:
- a disposition listed in the response;
- the status line ("reviewed at r1 …; r2 unreviewed");
- the revision paragraph;
- a provenance input line and an off-`main` table row for `REVIEW-U4-CALC-r1` (classified as
  provenance, re-derived);
- the label "control C1-3" on Instance 1.1's dual check.

The theorems, lemmas, instances and their proofs are otherwise unchanged. Other checks:
- `U4-CALC-r1.md` is unchanged (empty diff).
- The retained `REVIEW-U4-CALC-r1.md` is byte-identical to the review as written.
- The README's digests for U4-CALC-r1, U4-CALC-r2 and REVIEW-U4-CALC-r1 match the files at
  `213e3981`.
- The other commits in `f86dd1f7..213e3981` (S3-U3-r1, GAMMA-G1-r1, CODEX-CLOSEOUT-r1, and their
  README rows) belong to other units and were not reviewed.

## Optional

**O-a. Dimension bullet.** "So this mode excludes no `γ ≠ 1` outside `d = 3`" was checked only for
`d = 1` and `d = 2`. For `d ≥ 4` the mode gives `M_{2d−4}`, which is not unipotent, but whether it
excludes depends on `q`. Since only `d = 3` is native, "for `d = 1, 2`" would be exact.

**O-b. New [A-inf] paragraph after Prop. 2.8.** "changes no law of any region other than the marker's
own" is true but weaker than (i) gives. With `D = A`, (i) shows that the marker's own law is also
unchanged by declaration, so "changes no law of any region" would be exact.

## Checked / not checked

**Checked.**
- Each of the ten dispositions against the text.
- C1-4, C1-7, C2-6, C2-7, Prop. 2.5(c), the dimension bullet and the `ℤ/5` example, by hand.
- The new aperiodicity sentence in Prop. 2.7, and the converse of Prop. 2.7.
- The split of Prop. 2.8(ii).
- The scope of the `ℤ/6` narrowing.
- The full r1-to-r2 diff, r1's immutability, and the README digests.

**Not checked.**
- R-1 to R-7, which remain open (R-3's CRT compatibility question included).
- The parts of r2 identical to r1, beyond the r1 review.
- The other units added in the same commit range.
