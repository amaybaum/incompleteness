# Review of REUSE-TEST-SPEC r2 (focused confirmation)

**Object.** `REUSE-TEST-SPEC-r2.md`, with `RESPONSE-REUSE-TEST-SPEC-r1.md`. Both are kept on
PR #1294 at `445b47b5`. The review they answer is `REVIEW-REUSE-TEST-SPEC-r1.md` (cited REV-1).

**Reviewer.** Independent and not an author. Read-only. Hand derivation and hand arithmetic only. No
edits, commits or GitHub writes.

**Verdict: ACCEPT WITH CHANGES.**
- Every required item of REV-1 is applied, including M-1 and M-2.
- DR-3a is sound and does not use L-2.
- I re-derived every expected verdict of CC-1 by hand, and all are correct.
- The decision rules stay fixed in advance.
- Q-3's scope in arm W is stated at its proved scope and is not presented as L-3.

Three small required changes remain: C-1, C-2 and C-3 below. Two of them come from the way R-3, R-5 and
O-3 were implemented. None changes the design.

***

## 1. Required items of REV-1

| Item | Check | Result |
|---|---|---|
| R-1 (M-2) | §5 states "Not L-2" for arm W and gives the countermodel. DR-3 and the Q-2 use are limited to arm P (§8.2, Appendix A). §10.1's strict-(U) and RQ-UPD-1 bullets are limited to arm P | resolved |
| R-2 (M-1) | The fresh per-`⊥` coin is removed. One coin per wing per event goes in `λ`. The [A-inf] of §6.3 is restated for the structure-keeping set, and it now holds: every rule is a fixed function of the raw outcome and of a policy-independent per-event coin. Exclusions require every rule in the set (C-12) | resolved |
| R-3 | DR-3a and `B_W` are added. The dominance of the baseline over DR-3 is stated (§7.2), and §10.1 names which route excludes. One soundness gap remains in `φ` (C-2) | resolved, with C-2 |
| R-4 | CC-1 is specified as a freeze precondition. C-5 runs in a separate calibration block and has a pass criterion. C-6 and C-10 have pass criteria. T-C uses the common subensemble `E₄` | resolved |
| R-5 | The map has a precedence order and is exhaustive (§2 below). Row 9 overstates (C-1) | resolved, with C-1 |
| R-6 | `S₁ := E₀₀ + E₀₁ + E₁₀ − E₁₁` is pinned and used in every rule. Q-2 is written as `S₁ ≤ \|S₁\| ≤ …` | resolved |
| R-7 | Mao's settings carry LIT's writer's-reading label. The arm P first uses of P-1 and P-2 are listed under "Additions". The detection expectation is marked [DES] | resolved |

**T-C** [A-inf, checked]. If `P(E₄ | λ)` does not depend on the policies, Bayes' rule gives
`P(λ | E₄, π) ∝ P(E₄ | λ) P(λ)`. That law does not depend on `π`, so (k4) and (k4′) hold on `E₄`. ✓

## 2. DR-3a, the outcome map, and fixity

**DR-3a is sound and uses no lemma.** Strict (U) is defined as the same response functions acting on
an unchanged `λ`. Under it, the dilation keeps its noise in `λ`. At a fully repeated joint policy
(Alice `(s,s)`, Bob `(r,r)`) both uses therefore have identical arguments, so `a₂ = a₁` pointwise.
The same holds in both register forms, and under every rule of the structure-keeping set: the shared
coin assigns the same value to both entries. Neither (k3) nor (k4), L-2 nor Q-2 is used. ✓

**Exhaustive, with one orientation.**
- Rows 1–4 come first.
- In arm P, rows 5–8 cover the product of {strict (U) excluded by DR-3a or DR-3, not excluded} with
  {DR-4 excludes, DR-4 unresolved}.
- In arm W, rows 9–10 cover both values of DR-3a.
- So the map is a function. ✓

**Fixed in advance.**
- `T₃`, `T₄` and the DR-3a statistic are fixed linear statistics, each tested against 0.
- `S₁` enters as a measured term whose uncertainty is carried by the bound. That is preregistering the
  rule, not the numbers (§A.29).
- `p_inj`, `β`, the weights, the per-event ranges, the coin rule and the CHSH orientation are all
  declared at freeze.
- Taking the average over `y₂` and `x₂` in Λ removes the only constants that were chosen.
- The fallback is applied before freeze.
- No threshold is set from the data. ✓

## 3. CC-1, re-derived by hand

Each check uses the pinned `S₁` and r2's `Λ = ½ Σ_x Σ_{y₁y₂} ε_A + ½ Σ_y Σ_{x₁x₂} ε_B`.

- **(i) TSI's (U) candidate,** `a = R`, `b = R ⊕ xy ⊕ C`, unchanged.
  - Second outputs: `a₂ = a₁` and `b₁ ⊕ b₂ = x₁y₁ ⊕ x₂y₂`.
  - Bob holding `(y,y)` gives `b₁ ⊕ b₂ = y(x₁ ⊕ x₂)`. So `Δ_B(1) = 1` and every other `Δ` is 0, giving
    `ΣΔ = 1`. Also `B = 0`, since at `x₁ = x₂` the parity is 0.
  - Λ: Bob `y = 1` mismatches at `(x₁,x₂) ∈ {01,10}`, so `Λ = ½·2 = 1`.
  - `S₁ = 2√2`, so the margin is `0.414`. Then `T₃ = T₄ = 0.414 − 1 < 0`.
  - Bob's history depends on Alice's `x₂`.
  - Verdicts: DR-1 pass, `ns-disagree`, `baseline-null`, `ns-unresolved`, `rep-unresolved`. ✓
    (The note writes `Λ ≥ 1`. The value is exactly 1.)
- **(ii) Fresh `(R, C)` at each use, case (N).**
  - Each wing's two outcomes are independent and fair, so `ε = ½` in every held cell.
  - Then `B = ½`, `Δ = 0` and `ΣΔ = 0`, so `T₃ = 0.414 > 0`. And `Λ = ½(8·½) + ½(8·½) = 4`, so
    `T₄ < 0`.
  - The histories are uniform under every policy.
  - Verdicts: `ns-consistent`, `u-excluded-baseline`, `ns-excludes-U` (correct, since (ii) is not
    (U)), `rep-unresolved`. This is the required countercontrol for DR-4 on (N). ✓
- **(iii) LREV R3's (S) realization.**
  - Every held cell repeats, so `B = 0`, `ΣΔ = 0` and `Λ = 0`. That gives `T₃ = T₄ = 0.414 > 0`.
  - Alice's history is `(R, R)` or `(R, f_A)`. Bob's `b₁` is fair given `x₁`, and his history is
    `(b₁, b₁)` or `(b₁, f_B)`. Both are blind to the remote policy.
  - Verdicts: `ns-consistent`, `baseline-null`, `ns-excludes-U`, `rep-excludes-UN`. ✓
- **(iv) M-1's (U) model.**
  - Under each of the three rules: `E₀₀ = E₀₁ = 1`, `E₁₀ = 0` and `E₁₁ = −1`, so `S₁ = 3`.
  - Δ under each rule:
    - with the per-event coin, Alice holding `(1,1)` gives `(c,c)` under Bob `(0,0)`, so `ε = 0`, and
      `(c, r⊕1)` under Bob `(0,1)`, so `ε = ½`;
    - `⊥ ↦ 0` and `⊥ ↦ 1` likewise give `Δ_A(1) = ½`.
  - So `ΣΔ = ½ = (S₁ − 2)/2` and `T₃ = 0`. `LCB(T₃) ≤ 0`, so the verdict is `ns-unresolved`. ✓
  - The note does not list the other verdicts. By hand they are:
    - DR-3a `baseline-null`: the held cells `(⊥,⊥)` and `(r⊕1, r⊕1)` repeat;
    - DR-4 `rep-unresolved`: `ε_A(1; ·) = 0, ½, ½, 0`, so `Λ = ½ = (S₁ − 2)/2` and `T₄ = 0`;
    - DR-2 `ns-disagree`: on unassigned records, and under the coin rule `(c,c)` against `(c, r⊕1)`.
  - Q-3 is tight on this model.

## 4. Q-3 in arm W

The following places state it as a Q-3 statement at its proved scope:
- §5 ("used at that scope only; it does not extend L-3");
- the Λ row of §7.2 ("both arms, conditional on Q-3 and Q-2");
- the arm W bullet of §10.1 ("a Q-3 statement only");
- Appendix A, *Scope*.

The threshold is `1.414η² + 4η − 5 = 0`, which gives `η ≈ 0.9385`. It lies above DR-1's
`η > 0.841`, and it is stated at ideal QM. ✓

Two wordings are loose but not wrong:
- DR-4's heading, "in arm P also an instance of L-3". The exact statement is "reduces to L-3 at
  `ε = 0`", which Appendix A already uses.
- *Scope*'s "says nothing about realizations that meet its premise for one wing only". Q-3 itself is
  per wing; the phrase is true of its DR-4 use.

Both are optional (O-a).

## 5. O-1 to O-8: nothing new, with two exceptions

- O-1, O-2, O-5, O-6, O-7 and O-8 are applied as proposed, and they add nothing beyond REV-1.
- Λ's averaging (O-1) is REV-1's own suggestion. Q-3 holds for each `y₂`, so it holds for the average.
- **O-3 introduced an inconsistency (C-3).** C-1 passes "iff no χ² test rejects", while the bounds
  assume a bias of at most `β`. A χ² test that does not reject does not establish `|p − ½| ≤ β`.
- **O-4 combined with R-3 introduced the subtraction `B − φ`.** This is a new step, and its soundness
  depends on how `φ` is defined (C-2).

***

## Required changes

- **C-1 (row 9 and DR-3a in arm W).**
  - Row 9 says "first half met at arm W". U3 §10.3's first half is an L-2 consequence, and §5 states
    that L-2 does not apply to arm W. Restate row 9 to say that setting-independence is recorded and
    that L-2's half is not addressed by arm W.
  - In arm W, `Θ` already makes every identified program tick-indexed, so case (N). DR-3a's strict-(U)
    exclusion in arm W is therefore definitional, and the note should say so.
  - Also state how the map reads DR-3 or DR-4 if the fallback in §8.2 removes either step, for
    example "removed reads as unresolved".
- **C-2 (`φ` in DR-3a).** Under strict (U), `a₂ = A(s, y₂, λ)`. A misapplied **remote** setting, or a
  misapplied first-use setting, can therefore break `a₂ = a₁`. Define `φ_W(s; r)` as the rate, within
  the cell, of events in which **any of the four** applied settings differs from the intended one. Then
  `1[w₁ ≠ w₂] ≤ 1[any mismatch]` holds pointwise under strict (U). With only the wing's own mismatches
  counted, DR-3a can exclude falsely.
- **C-3 (C-1's criterion against `β`).** Choose one of two forms:
  - replace the χ² criterion with an interval criterion: pass iff the upper confidence bound of each
    `|p − ½|` is at most `β`;
  - or state `β` as a declared hypothesis on the random sources, for which C-1 is a necessary check
    only.

## Optional

- **O-a.** Adjust the two Q-3 wordings in §4.
- **O-b.** Give the full expected verdict vectors for CC-1 (iv), and DR-1 for (ii)–(iv). Declare the
  synthetic sample size. At `N` well below about 10⁶, the margins of 0.414 in (ii) and (iii) may not
  resolve, and CC-1 would then fail for statistical reasons.
- **O-c.** Two remarks on Appendix B:
  - r2's Λ has 16 half-weight terms, not "eight". The per-term sum is numerically the same.
  - With the averaged Λ, the per-event range of the joint estimator is 16. That is a factor of about 8
    in half-width, not about 4.
- **O-d.** §10.3 lists rows 1, 2, 7, 8 and 10 as leaving the agreement half open. Rows 6 and 9 also
  leave a part open.
