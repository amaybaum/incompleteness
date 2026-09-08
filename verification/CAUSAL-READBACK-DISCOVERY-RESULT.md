# Realization-level causal-readback discovery — execution result

Executed on PR #542 under the frozen preregistration
`verification/CAUSAL-READBACK-DISCOVERY-AUDIT.md` and append-only amendment 1.
The authoritative freeze record is PR comment `5578422360`, which records both the preregistration
commit and the two content-addressed blob hashes. Neither frozen file was modified during execution.

## Headline

**Outcome C on the audited accessible window, with the T4 fallback closed rather than opened.**

The realization-level parent `CausalReadback` survives all four mandatory calibration controls and
has the intended physical write / store / read meaning. It implies genuine history-sensitive visible
memory (`C4w`). However:

- `CausalReadback -> C4e` is **false**;
- `CausalReadback -> C4r` is **false**;
- more strongly, `CausalReadback -> PIndivisibleWithin K` is **false on the same audited horizon**.

The last statement is witnessed by an exact finite reversible realization whose rooted family is

`I -> B_(3/4) -> B_(5/8)`

and which satisfies the frozen W/S/R parent while remaining exactly P-divisible within `K = 2`, with

`B_(3/4) * B_(3/4) = B_(5/8)`.

Therefore no fallback observable predicate `C4cr` can simultaneously be

1. implied by `CausalReadback` on every realization, and
2. sufficient for `PIndivisibleWithin K`

on that same window. Such a predicate would contradict the explicit parent-positive, P-divisible
countermodel. Under the frozen T4 discipline the fallback search is therefore **not opened** and no
`C4cr` is defined.

This is a **window-local** result. It does not retract or decide the separate recurrence-scale route
already stated in the manuscript: on a finite reversible realization a later recurrence may return
the rooted map to the identity, allowing stochastic-inverse rigidity to create global
P-indivisibility even when every accessible short window is P-divisible. That longer-horizon route is
kept logically separate below.

## Execution artifacts

Two exact standard-library probes were added and placed in the required Numerical probes gate:

- `verification/lean/causal_readback_discovery_probe.py`
- `verification/lean/causal_readback_bridge_probe.py`

The first uses `fractions.Fraction` throughout and the same b51 finite-horizon reversible dilation
pattern as `papers/oi_lattice_code/foundations/review4_probes.py`. It explicitly completes the
finite-horizon update to a permutation of the full `V x H` carrier, so the countermodels are finite
deterministic reversible realizations, not merely stochastic matrices written down by hand.

The second checks the exact same-window stochastic propagators for the T3 countermodel. No Lean
predicate, manuscript file, book file, README, census, bibliography or release record is modified by
this result.

## The parent as executed

The frozen parent is evaluated on a declared realization

`R = (V, H, phi, mu_H)`

with a common fixed hidden prior and rooted preparations. A witness consists of distinct roots
`a != b` and times

`0 < w <= s < t <= K`

with:

- **W — write:** for at least one positive-prior common hidden seed, changing only the visible root
  changes the hidden state after `w` steps;
- **S — store:** at a common positive-probability visible value `x` at time `s`, the two
  root-conditioned hidden laws differ;
- **R(1) — causal read:** holding that current visible value `x` fixed and propagating the two hidden
  conditionals through the same future dynamics gives different visible output laws at `t`;
- **R(2) — actual rooted reappearance:** the actual rooted visible rows at `t` differ.

Amendment 1 remains controlling on attribution: R(2), not W, is the load-bearing clause that rejects
the standard b51 XOR/history-ledger completion.

## Mandatory controls

### N1 — XOR/history-memory: passes negative calibration

Use the existing two-step XOR law

`X1 ~ Bernoulli(1/2)` independent of `X0`,
`X2 = X0 XOR X1`.

The exact rooted family is

`Gamma_0 = I`, `Gamma_1 = J/2`, `Gamma_2 = J/2`.

The history-level condition is present: the positive histories `(0,0)` and `(1,0)` share current
visible state `0` but have deterministic next laws `delta_0` and `delta_1` respectively.

On the standard b51 ledger completion, at `w = s = 1`, `x = 0`, `t = 2`:

- W: **yes** — the ledger records the root under a common tape seed;
- S: **yes** — the root-conditioned hidden laws differ at the same visible endpoint;
- R(1): **yes** — fixing `X1 = 0`, propagation from the two hidden conditionals gives different
  latent visible outputs;
- R(2): **no** — both actual rooted rows at time 2 are `J/2`.

Hence `C4w = yes` and `CausalReadback = no`, exactly as frozen. The rejection is explicitly by
**R(2)**.

### P1 — delayed revival: passes positive calibration

Use

`Gamma_0 = I`, `Gamma_1 = I`, `Gamma_2 = J/2`, `Gamma_3 = I`.

The b51 reversible realization has a parent witness with

`a = 0`, `b = 1`, `w = 1`, `s = 2`, `x = 0`, `t = 3`.

The visible root is written into the ledger, survives while the visible marginal is fully mixed,
and is then read back into `X3 = X0`. Thus W, S, R(1), and R(2) all hold. The known exact collision
and later separation also give `C4e`, hence `C4r` and P-indivisibility by the already-existing #538
theorems.

### N2 — uncoupled reversible product: passes negative calibration

Take

`phi(v,h) = (v XOR 1, h XOR 1)`

on two visible and two hidden values. The full update has period 2, so finite recurrence is present.
But for any common hidden seed and every time in a recurrence period, the hidden component is
independent of the visible root. W therefore fails and the parent is false.

This confirms that recurrence alone is not causal readback.

### Prior-dependence pair: passes the frozen preparation control

Take the same bijection and partition in both cases,

`phi(x,h) = (x XOR h, h)`.

It obeys `phi^2 = id`, so `Gamma_2 = I` under every hidden prior.

- uniform `mu_H`: `Gamma_1 = J/2`, `Gamma_2 = I`, hence P-indivisible over the two-step horizon;
- `delta_0`: `Gamma_1 = I`, `Gamma_2 = I`, hence P-divisible.

The fixed prior is therefore operationally material: P-divisibility is not a property of
`(phi, partition)` alone.

For this specific pair, W fails under both priors because the hidden variable `h` is static and never
acquires information from the visible root. The control was not stipulated to track the parent, and
it does not. Its role is preparation-scope discipline for later OI claims.

## T1 — CausalReadback implies history-level C4w

**Result: true.**

The proof uses the common-current storage surface and R(1), and does not use R(2).

Let the parent witness have storage time `s`, common visible value `x`, and read time `t`. Condition
on the two rooted storage events `(X_0=a, X_s=x)` and `(X_0=b, X_s=x)`. Starting from those two
conditional hidden ensembles with the same current visible state `x`, let

`nu_a^k`, `nu_b^k`

be their visible distributions after `k` further steps. At `k=0` both equal `delta_x`. R(1) says
that at `d = t-s` they are different.

Choose the least `m > 0` for which `nu_a^m != nu_b^m`. Then

`nu_a^(m-1) = nu_b^(m-1)`.

Suppose the manuscript's history condition failed at the corresponding absolute time
`s + m - 1`. Then every positive-probability visible history ending in the same current visible
state would induce the same next-step law. Consequently there would be one stochastic next-step
kernel depending only on that current visible state. Applying that same kernel to the equal
`nu_a^(m-1)` and `nu_b^(m-1)` distributions would make `nu_a^m = nu_b^m`, contradicting the choice
of `m`.

Therefore two positive-probability visible histories with the same current visible state induce
different next-step laws: `C4w` holds.

This argument shows a useful dependency fact:

- W supplies the physical visible-to-hidden origin of the memory;
- S supplies the common-current hidden storage surface;
- R(1) is sufficient for the history-memory consequence;
- R(2) is not needed for T1, although it remains load-bearing for the N1 calibration and for actual
  reappearance in rooted one-time statistics.

No new Lean statement of manuscript C4w is introduced in this round; the theorem is recorded at the
same history-law level as the manuscript condition. The exact controls are machine checked by the
new probe.

## T2 — exact marginal collision/revival

**Result: false.**

An exact finite reversible b51 realization is built from the history kernel with rooted family

`Gamma_0 = I`,
`Gamma_1 = I`,
`Gamma_2 = B_(3/4)`,
`Gamma_3 = I`,

where

`B_(3/4) = [[3/4, 1/4], [1/4, 3/4]]`.

It satisfies the full parent with witness

`w = 1`, `s = 2`, `x = 0`, `t = 3`.

At the storage time both roots can produce `x = 0`, their hidden conditional laws differ, and the
later fixed-visible propagation returns the root; the actual rooted laws at time 3 are distinct.
However the two rooted rows are distinct at every time in the audited family: at times 0, 1 and 3
they are the two identity rows, and at time 2 they are the two distinct rows of `B_(3/4)`.

Hence there is no exact rooted-row collision followed by separation: `C4e` is false.

This confirms the preregistered structural expectation: R(2) contains later separation but the
parent contains no earlier-collision requirement.

## T3 — quantitative TV revival

**Result: false.**

A second exact finite reversible b51 realization has

`Gamma_0 = I`,
`Gamma_1 = B_(3/4)`,
`Gamma_2 = B_(5/8)`,

with

`B_(5/8) = [[5/8, 3/8], [3/8, 5/8]]`.

It satisfies the full parent with witness

`w = s = 1`, `x = 0`, `t = 2`.

At the same storage endpoint, the hidden conditional still records which root was prepared and its
later visible output law depends on that hidden distinction; the actual rooted rows at time 2 are
also distinct. Nevertheless the total-variation distances of the two rooted rows are

`1 -> 1/2 -> 1/4`.

They decrease strictly. No pair of times exhibits a TV revival, so `C4r` is false.

### Stronger same-window closure: the countermodel is P-divisible

The same family is exactly P-divisible within `K = 2`. The required bridges can be chosen as

- `0 -> 1`: `B_(3/4)`;
- `0 -> 2`: `B_(5/8)`;
- `1 -> 2`: `B_(3/4)`;

because

`B_(3/4) * B_(3/4) = B_(5/8)`.

All three bridge matrices are row-stochastic.

Thus the physical W/S/R cycle can be real and visible in history-conditioned predictions while the
rooted one-time family remains P-divisible throughout the same accessible window.

## T4 — fallback `C4cr`

**Not opened.**

The frozen discipline allowed a separately preregistered fallback search if T2 and T3 failed. The
T3 countermodel now proves that such a search cannot achieve the intended same-window implication
without strengthening the physical parent.

Indeed, suppose an observable predicate `C4cr` satisfied both

`CausalReadback -> C4cr`

and

`C4cr -> PIndivisibleWithin K`.

Apply the two implications to the exact T3 countermodel. The parent holds, so `C4cr` would hold; the
second implication would then make the family P-indivisible. But the exact stochastic factorization
above proves that the family is P-divisible. Contradiction.

Therefore no `C4cr` with the required two properties exists for the frozen parent on the same
window. A fallback definition would either fail to follow from the parent or would smuggle in an
additional physical restriction. Under the T4 rules, neither is an admissible rescue.

No amendment 2 is created and no `C4cr` predicate is defined.

## Prior scope

The round also carries the preregistered prior-dependence qualification.

The fixed hidden prior is part of the declared realization. The explicit `phi(x,h)=(x XOR h,h)`
pair proves that changing only this prior can flip the rooted family's divisibility verdict. Hence a
later physical statement of the form

`OI -> P-indivisible`

must either name the canonical counting/uniform baseline, derive another preparation principle, or
state explicit prior hypotheses. It cannot silently quantify over all manuscript-permitted fixed
priors.

This is an **E-type qualification** on the OI-level inference, alongside the C headline for the
window-local bridge.

## What this result does not say

The countermodel does **not** establish that a finite reversible CausalReadback realization remains
P-divisible for all time. The audited parent is bounded by `K`; finite permutation dynamics has a
larger recurrence horizon that may lie outside `K`.

The manuscript already states a separate recurrence-scale route: finite reversibility returns a
rooted visible map to the identity, while a prior non-permutation rooted map cannot possess a
stochastic inverse. The present result neither re-proves nor retracts that statement.

There is a particularly direct reason that the new parent may feed that global route: S requires a
visible value with positive probability under two distinct rooted preparations, so the storage-time
rooted map cannot be a permutation matrix. Whether this observation plus the existing stochastic
inverse lemma closes the complete recurrence-scale theorem at the current formal interface is the
natural **next audit**, not a result claimed here.

Likewise this round does not apply Barandes and does not identify mathematical unitary/Born
representability with physical P-indivisibility, coherent control, phases, Hamiltonians, instruments,
or operational quantum mechanics.

## Final classification

- parent calibration: **PASS**;
- T1 `CausalReadback -> C4w`: **TRUE**;
- T2 `CausalReadback -> C4e`: **FALSE**, exact finite reversible countermodel;
- T3 `CausalReadback -> C4r`: **FALSE**, exact finite reversible countermodel;
- same-window `CausalReadback -> PIndivisibleWithin K`: **FALSE**, explicit stochastic bridges;
- T4 `C4cr`: **CLOSED WITHOUT DEFINITION** — impossible as a universal same-window child of the
  frozen parent that also suffices for P-indivisibility;
- prior scope: **prior-dependent; E-type qualification remains**;
- recurrence-scale P-indivisibility: **separate next audit / not decided here**;
- Barandes application: **not performed**;
- operational-QM claim: **not made**.

Status: **execution result recorded; frozen preregistration preserved byte-for-byte.**
