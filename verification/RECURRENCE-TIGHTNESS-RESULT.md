# Recurrence-scale indivisibility and horizon tightness audit — result

Executed under the frozen preregistration `RECURRENCE-TIGHTNESS-AUDIT.md` and controlling append-only amendment `RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md`.

## Classification

1. **Target 1 — proved and kernelized.** An identity return with a strictly earlier overlap of two distinct rooted rows yields `C4r` at that horizon. The theorem is stronger than the original parent-level statement: it consumes only row-stochasticity, the overlap, and the later identity return.
2. **Target 2 — proved and kernelized via merged #538.** The Target-1 witness composes directly with `c4r_implies_pIndivisible`, giving `PIndivisibleWithin` at the same horizon. No stochastic-inverse rigidity lemma is needed.
3. **Target 3 — T3-A, tightness construction succeeds.** There exists one finite reversible parent-positive realization whose rooted family is P-divisible on every shorter horizon and first fails when the controlling readback-return horizon is reached.

The Target-3 witness is checked independently and exactly by `verification/lean/recurrence_tightness_probe.py`. Its classification, exact witness data, controlling horizon, accessibility disclaimer, and no-scaling disclaimer are pinned by the CI-gated `R7-RCH-T3` guard in `verification/lean/recurrence_tightness_guard_probe.py`, including negative controls that must fire on those three classes of regression.

---

## Target 3 exact realization

Take visible carrier

`V = {0,1}`

and hidden carrier

`H = {0,1,2,3}`

with one fixed hidden prior shared by both visible roots:

`mu_H = (1/2, 1/5, 1/10, 1/5)`.

On the eight states `(v,h)`, use the permutation

- `(0,0)` fixed;
- `(1,0)` fixed;
- `(0,1) -> (0,2) -> (1,1) -> (0,1)`;
- `(0,3) -> (1,3) -> (1,2) -> (0,3)`.

Thus the microscopic permutation has exact order `3`.

The full rooted family through that period is

`Gamma_0 = I`,

`Gamma_1 = B_(7/10)`,

`Gamma_2 = B_(3/5)`,

`Gamma_3 = I`,

where

`B_p = [[p,1-p],[1-p,p]]`.

So the declared monotone-mixing construction succeeds literally:

`1 > 7/10 > 3/5 > 1/2`,

and there is no earlier visible identity return before time `3`.

---

## Full CausalReadback parent

The realization is parent-positive with the explicit witness

`a=0`, `b=1`, `w=s=1`, `x=0`, `t=2`.

### W — write

Use the same positive-prior seed `h=1`.

After one step:

- root `0` reaches `(0,2)`;
- root `1` reaches `(0,1)`.

The hidden components differ, so W holds.

### S — store

At `s=1`, visible value `x=0` occurs with positive probability under both roots.

The conditional hidden laws are

- under root `0`: `{0: 5/7, 2: 2/7}`;
- under root `1`: `{1: 2/3, 3: 1/3}`.

They differ, so S holds.

### R1 — causal read

Hold the current visible value fixed at `x=0` and propagate those two conditional hidden laws through one further application of the same dynamics.

The resulting visible laws are

- from the root-0 hidden conditional: `(5/7, 2/7)`;
- from the root-1 hidden conditional: `(2/3, 1/3)`.

They differ, so R1 holds.

### R2 — actual rooted readback

At `t=2`, the actual rooted rows are the two distinct rows of `B_(3/5)`, so R2 holds.

Therefore the full frozen parent is satisfied.

---

## The controlling horizon is exactly N_CR = 3

A storage witness already exists at `s=1`.

After that storage time:

- `Gamma_2 = B_(3/5) != I`;
- `Gamma_3 = I`.

Hence the earliest visible identity return lying after a storage witness is exactly

`N_CR = 3`.

In this witness the microscopic order and `N_CR` happen to coincide, but the theorem and the preregistration do not identify those notions in general.

---

## Every shorter horizon is P-divisible

For all pairs inside `K<3`, explicit row-stochastic propagators exist.

From time `0`:

- `Gamma_1 = I * B_(7/10)`;
- `Gamma_2 = I * B_(3/5)`.

Between times `1` and `2`:

`B_(7/10) * B_(3/4) = B_(3/5)`.

Therefore `PDivisibleWithin(K)` holds for every `K < 3`.

Equivalently, the two rooted-row TV distances are

`1, 2/5, 1/5`

through times `0,1,2`: strictly decreasing before the return.

---

## Failure occurs when the horizon reaches N_CR

At time `3`, `Gamma_3 = I`, whose two distinct rooted rows have TV distance `1`.

Thus

`TV(Gamma_2(0,-), Gamma_2(1,-)) = 1/5 < 1 = TV(Gamma_3(0,-), Gamma_3(1,-))`.

So `(2,3)` is a `C4r(3)` witness, and the merged #538 theorem gives

`not PDivisibleWithin(3)`.

The exact probe also checks the final factor obstruction independently. Since `B_(3/5)` is invertible, the unique matrix `Lambda` satisfying

`B_(3/5) * Lambda = I`

is

`Lambda = [[3,-2],[-2,3]]`,

which is not row-stochastic.

The divisibility failure therefore occurs on the snapback step and not on any shorter horizon.

---

## Interpretation fixed by the preregistration

Target 3 is **T3-A**.

The universal recurrence/readback-return theorem is horizon-tight in the existential sense preregistered: the frozen parent does not force a P-divisibility obstruction on some strictly shorter horizon `K < N_CR` in every realization.

This is a limitation on what the recurrence theorem alone can establish about accessible OI -> QM behavior. It does **not** show that `N_CR` is always large or physically inaccessible; the exact witness here has `N_CR = 3`. What it proves is that no universal theorem from the frozen parent can simply replace the `N_CR` horizon by an unspecified strictly earlier one.

Together with PR #542, the clean boundary is:

- causal write/store/read does not force same-window revival or P-indivisibility on an arbitrary accessible window;
- storage overlap plus a later visible identity return does force revival and P-indivisibility when that return is included;
- that return-horizon statement is tight: all shorter horizons can remain P-divisible.

The S-only dependency of Targets 1–2 remains important but does not reverse this interpretation. The recurrence obstruction applies under weaker hypotheses than the full parent, while the explicit full-parent witness shows that even genuine causal readback can remain P-divisible until the controlling return horizon.

No claim is made that arbitrarily large `N_CR` admits an analogous tight witness; that stronger scaling question was not preregistered in this round.

---

## Publication boundary

This result does not silently edit the manuscript.

It does, however, sharpen the publication backlog in two directions:

1. any recurrence statement should name the return horizon actually used and should not imply an obstruction at a strictly earlier time;
2. the already-identified preparation-scope issue for manuscript C4 remains separate and should be repaired in its own publication-record task.

No new condition is named or adopted, and no representation-level or operational-QM conclusion is strengthened by this round beyond the exact stochastic horizon result above.