# Re-check of 67a5cbe1 (PE-01 plan, revision 2)

## What was read

- Commit `67a5cbe101247d7f487859a4a753f540e5e3982f`, with tree `b9af1661feb8329ec97c179a8380b54486b19458` and parent
  `6e5db447`. It changes only `pe01_bounded_tests_v1/PLAN.md` (+121/−43).
- The PLAN.md read here has blob `9dd107d5799de35362c480cac8193aa94be9afaa` and sha256
  `ca82998a26447d719f1a5078fd5529bb5eed548f17673140614c6737ba5637f4`. It was extracted read-only with `git show` to
  `revpe01/PLAN-67a5cbe1.md`.
- Line numbers below refer to that file.
- Design-check script: `revpe01/checks3.py`, with output in `revpe01/checks3.out`. It computes generator-only design
  quantities and no PE-01 measurement.
- Reviewer: independent, read-only. No commits and no pushes.

## Verdict: BLOCK (narrowly)

S1–S5, A4, the LP nit and the overcharge note are all fixed adequately. One required defect remains, the admissible
region tables, together with a one-line rule for the new Purpose paragraph. Both fixes are short. With them, the plan
is ACCEPT WITH NITS.

## 1. The earlier findings

| Item | Status | Where |
|---|---|---|
| S1 EX8 | **fixed** | EX8 at :259 checks each observer map (ρ-step, a-step, clock tick, readout) as a table on C_V′ × C_H: the h-component is the identity, and the (v, clk, x, out)-component is constant across h. It also requires φ to act as the identity on (v, clk, out). |
| S2 G_filt specificity | **fixed** | :239–240 requires "≤ at every such K, and strictly smaller at some such K, for each n". The rule holds on correct code: the only non-strict points are the equalities at n = 3, K = 5 and n = 4, K = 6, and strict inequality occurs at later K for each n. |
| S3 CX checkpoint | **fixed, one nit** | :272. Three mutants (one K′ at 1/8 − 2^{−K−2}, footprint θ+1, K = K_cx+1), each refused on its own condition, and a refusal counts only if it names that condition. *Nit N-a:* the listed fields (adv at each K′, K_cx, FP, EX6) cover (a), (c), (d) and (f), but not (b) or (e). Add the per-witness EX1/EX7/EX8/IM3 flags and the global control flag to the fields CX reads. |
| S4 footprint | **fixed** | :147–157 defines the footprint as m + ⌈log₂(K+1)⌉ + 1 for every footprint-bearing statement, and labels the curves "evaluation time uncharged". The FP row (:271) checks it against register widths minus the system bit. The table size includes the trigger constant (:182–183). Condition (f) is at :302, and the verdict prints the footprint "as measured by FP". |
| S5 resource-model limitation | **fixed** | :373–375 states the horizon bound as a consequence of the resource model, not a limit OI imposes, and says the generated verdict text repeats the sentence. *Nit N-b:* no checkpoint measures that repetition; add it to VG's self-test. |
| A4 tag gap | **fixed** | :336–337 |
| LP nit | **fixed** | The dual form at :202–205 is correct. Primal max_w min_φ s_φ Σ w_D Δ_φ(D) equals min_π max_D Σ_φ π_φ s_φ Δ_φ(D) by finite minimax, and the inner maximum over F is the sum of positive parts. K_LP = 2^{n−1} − 1 is marked proposed, and there is a §8 row. |
| Overcharge note | **fixed** | :155–157 |

## 2. The admissible-region tables (:377–407): **required**

The tables are arithmetically consistent with the plan's own rule. I recomputed every cell of both tables
independently and they match: for G_lin, window floor K − 3 ≥ n+1; for G_filt and G_clk, floor K = 3; footprint ≤ θ;
K ≤ K_cx.

But the rule is wrong for G_filt and G_clk. There is an exact zero for every observer at short horizons, so "no PC
zero is claimed" does not mean "no zero exists".

**The zero.** Let Z(φ) be the largest k such that, for every control sequence y_0..y_{k−1}, the increments
f(σ_{y_0}h), f(σ_{y_1}σ_{y_0}h), … are jointly uniform under uniform h.
- For every observer in 𝒫ᵉᵐᵇ, passive or active, adaptive included, adv^pred = 0 exactly at every K′ ≤ Z.
- *Proof.* An adaptive control y_t depends on h only through the increments before it. So
  Pr[Y_{0:k−1} = z] = Pr_h[the increments under the fixed sequence y(z) equal z] = 2^{−k}.
  Hence Y_{K′−1} is uniform and independent of (X_0, v_{K′}), and Pr[χ(v_{K′}) = X_{K′}] = ½.
- K′ = 0 is zero trivially: v_0 is fixed and X_0 is uniform.
- Exhaustive computation over all control sequences (`checks3.out`):

  | n | 3 | 4 | 5 | 6 | 7 | 8 |
  |---|---|---|---|---|---|---|
  | Z(G_lin), matching PC | 3 | 4 | 5 | 6 | 7 | 8 |
  | Z(G_filt) | 2 | 2 | 3 | 4 | 5 | 6 |
  | Z(G_clk) | 2 | 3 | 3 | 4 | 4 | 5 |

Condition (d) needs adv ≥ 1/8 at every K′ ∈ [K−3, K], so the true floor is K ≥ Z(φ) + 4. Corrected tables, with
cells G_lin | G_filt | G_clk and – for empty:

θ = n:

| n | m = 1 | m = 2 | m = 3 | m = 4 |
|---|---|---|---|---|
| 3 | – \| – \| – | – \| – \| – | – \| – \| – | – \| – \| – |
| 4 | – \| – \| – | – \| – \| – | – \| – \| – | – \| – \| – |
| 5 | – \| [7,7] \| [7,7] | – \| – \| – | – \| – \| – | – \| – \| – |
| 6 | [10,15] \| [8,15] \| [8,15] | – \| – \| – | – \| – \| – | – \| – \| – |
| 7 | [11,31] \| [9,31] \| [8,31] | [11,15] \| [9,15] \| [8,15] | – \| – \| – | – \| – \| – |
| 8 | [12,63] \| [10,63] \| [9,63] | [12,31] \| [10,31] \| [9,31] | [12,15] \| [10,15] \| [9,15] | – \| – \| – |

θ = n+1:

| n | m = 1 | m = 2 | m = 3 | m = 4 |
|---|---|---|---|---|
| 3 | – \| – \| – | – \| – \| – | – \| – \| – | – \| – \| – |
| 4 | – \| [6,7] \| [7,7] | – \| – \| – | – \| – \| – | – \| – \| – |
| 5 | [9,15] \| [7,15] \| [7,15] | – \| [7,7] \| [7,7] | – \| – \| – | – \| – \| – |
| 6 | [10,31] \| [8,31] \| [8,31] | [10,15] \| [8,15] \| [8,15] | – \| – \| – | – \| – \| – |
| 7 | [11,63] \| [9,63] \| [8,63] | [11,31] \| [9,31] \| [8,31] | [11,15] \| [9,15] \| [8,15] | – \| – \| – |
| 8 | [12,127] \| [10,127] \| [9,127] | [12,63] \| [10,63] \| [9,63] | [12,31] \| [10,31] \| [9,31] | [12,15] \| [10,15] \| [9,15] |

What this means for the cells the relay cites:
- n = 4, m = 1 [3,3]; n = 6, m = 3 [3,3]; n = 7, m = 4 [3,3]; and n = 8, m = 4 [3,7], all at θ = n, are **empty**.
  Every window there contains a K′ ≤ Z, where adv^pred = 0 for every observer.
- My earlier table was for G_lin only, and is correct for G_lin. The "correction" overstates the region for G_filt and
  G_clk.
- At θ = n, every m = 4 cell is empty for all three generators, and m = 3 is non-empty only at n = 8.
- So the sentence at :406–407, "the window floor leaves some m ≥ 3 cells non-empty", is true only through n = 8, m = 3,
  where G_lin is non-empty too.

Why this is required, not a nit:
- CX evaluates (d) mechanically, so no wrong COUNTEREXAMPLE can follow.
- But §6.5 (:349–350) reports "no admissible witness" as a fact about the resource model only where the region is
  empty. With the wrong tables, empty cells appear non-empty. A structural non-result would then be printed as a
  measured favorable reading.
- ":379 The tables were design-checked at drafting" is a claim stronger than its evidence, because the check used the
  wrong floor.

*Fix:*
- Use the floor K ≥ Z(φ) + 4 for all three generators. For G_lin, Z = n reproduces the present PC floor.
- Have the verdict compute the table from Z(φ), K_cx(φ) and θ rather than reprint it.
- Add an §A.41 row, **AR**: Z(φ) is computed by exhaustive equidistribution over all control sequences, cross-checked
  against PC for G_lin (Z = n), and the plan's table equals the recomputed one.
- Delete or replace :379 and :406–407.

## 3. Owner decisions (§10, :466–495)

All seven match the owner's statement:
1. Footprint is admissibility condition (f), and results without the restriction are reported for comparison (:304–306).
2. Clock charge and fixed four-step window [K−3, K].
3. K1 allowed, K0 status reported separately.
4. δ_cx = 1/8; all other thresholds fixed, and listed.
5. Q fixed for PE-01.
6. Prediction and distinguishing both recorded; distinguishing-only is not proof of predictability.
7. Any new gap needs average-case or exact randomized evaluation; deterministic worst case gives bounds only.

θ is the only open decision (:304, :480, :488–495), and K_LP = 2^{n−1} − 1 is marked proposed (:481).

*Nit N-c:* say whether runs also wait for K_LP's confirmation. :495 gates runs on θ only. One line: "and K_LP
confirmed".

*Nit N-d:* the θ = n consequence at :491–493 must be restated from the corrected tables (§2 above).

## 4. New defects

- **Purpose paragraph (:12–14): required, one line.** "Tests whether apparent randomness is unpredictable because of
  the observations available, or only because the observer lacks resources" introduces an attribution that no rule
  defines. The third case, no witness at any enumerated footprint, cannot be read as "because of the observations
  available": that would be a finite test promoted to a universal claim (Code Review Rules, claim/evidence boundary).
  *Fix:* add to §6:
  - resource-attributed iff some witness meets (a)–(e) but not (f);
  - otherwise "no witness within the enumerated scope at any footprint", and never "unpredictable because of the
    observations available".
- **Invariants without checkpoints (§A.41):**
  - the admissible-region table (AR, §2 above);
  - the verdict's repetition of the limitation sentence (N-b);
  - "no run before θ (and K_LP) is fixed". *Nit N-e:* the measurement JSON records θ and the blob of the amendment that
    fixes it, checked like PIN.
- **Vacuous or prejudging controls:** none found. The CX mutant at footprint θ+1 becomes concrete once θ is fixed. T1–T3
  are still questions.
- **Overclaim:** :379 only (§2).

## Summary

| # | Item | Class |
|---|---|---|
| 1 | Admissible-region floor K ≥ Z(φ)+4 for G_filt/G_clk; tables, :379 and :406–407 corrected; AR checkpoint | required |
| 2 | Attribution rule for the Purpose paragraph | required |
| N-a | CX also reads the (b)/(e) flags | nit |
| N-b | VG checks the limitation sentence | nit |
| N-c | Runs also gated on K_LP | nit |
| N-d | §10's θ consequence restated from the corrected tables | nit |
| N-e | θ recorded in the JSON and checked | nit |
