# Recurrence-scale indivisibility and tightness audit — preregistration amendment 1

This is an **append-only preregistration amendment** to `verification/programmes/oi-qm/track-i/recurrence-tightness/preregistration.md`. It is committed and frozen before any proof search, candidate full-period realization search, brute-force search, new simulation, or execution of the declared tightness construction.

The original preregistration remains unchanged. This amendment controls wherever the original file's use of the horizon symbol `N` conflicts with the definitions below.

## A1. Correct the controlling horizon

The original preregistration used `N` in three non-equivalent senses: an arbitrary positive exponent with `phi^N = id`, the minimal microscopic order of `phi`, and a declared visible recurrence horizon. These are not interchangeable.

The recurrence-to-TV proof only requires a time at which the **rooted visible map** is the identity, and it also requires that the storage witness occur strictly before that time.

Accordingly, fix the following objects.

- Let `M = ord(phi)` denote the minimal positive microscopic permutation order, so `phi^M = id`.
- Let a **storage witness time** mean a time `s` appearing in a valid frozen-parent storage clause S witness for `CausalReadback`.
- Define the controlling readback-return horizon

  `N_CR := min { n > 0 : Gamma_n = I and there exists a storage witness time s with s < n }`.

`N_CR` is well-defined for every finite reversible parent-positive realization: choose any storage witness time `s`; since `phi` has finite order `M`, any sufficiently large positive multiple `q M > s` satisfies `phi^(q M) = id`, hence `Gamma_(q M) = I`, so the defining set is nonempty.

This `N_CR`, not an arbitrary order exponent and not necessarily `ord(phi)`, is the controlling horizon for Targets 1–3.

### Why the first visible return from time zero is not sufficient without an extra fact

One might instead define

`M_vis := min { t > 0 : Gamma_t = I }`.

That can be strictly smaller than `ord(phi)`, but the frozen parent does not by itself state that a storage witness occurs before `M_vis`. A visible marginal may return to the identity while hidden state has not microscopically returned, with a write/store/read witness occurring later. Therefore `M_vis` is not used as the universal controlling horizon unless execution separately proves that some storage witness satisfies `s < M_vis`.

The strongest unconditional horizon available from the frozen parent is `N_CR`: the earliest visible identity return that is known, by definition, to lie after at least one storage witness.

### No periodicity is inferred from a visible return

`Gamma_n = I` does **not** imply `phi^n = id`, and does not imply `Gamma_(t+n) = Gamma_t`.

Only a microscopic period such as `M = ord(phi)` supplies full-state periodicity. Targets 1 and 2 do not require periodicity at `N_CR`; they use only `Gamma_(N_CR) = I` and a storage witness `s < N_CR`.

Execution must not silently treat a bare visible return as a period.

## A2. Corrected Target 1

Target 1 is controlled by the statement

`CausalReadback(R) -> C4r(N_CR)`.

The declared proof route is now:

1. By definition of `N_CR`, `Gamma_(N_CR) = I`.
2. By definition of `N_CR`, there exists a frozen-parent storage witness with distinct roots `a != b`, storage time `s < N_CR`, and a visible value `x` having positive probability under both rooted rows at time `s`.
3. Therefore the two time-`s` rooted rows overlap, so their total-variation distance is strictly below `1`.
4. At `N_CR`, the two distinct rooted rows are `delta_a` and `delta_b`, so their total-variation distance is exactly `1`.
5. Hence `(s, N_CR)` is a valid `C4r(N_CR)` witness.

This removes the original unjustified bare assertion `s < N`: the strict inequality is part of the controlling horizon's definition.

No conclusion is preregistered for any `K < N_CR`.

## A3. Corrected Target 2

Target 2 is controlled by

`CausalReadback(R) -> C4r(N_CR) -> PIndivisibleWithin(N_CR)`.

The second arrow is still to reuse the merged PR #538 theorem. The stochastic-inverse argument remains an optional backup/cross-check only if a concrete interface mismatch prevents reuse.

The interpretation rule is unchanged and is now tied to `N_CR`:

- proving `PIndivisibleWithin(N_CR)` alone establishes a recurrence/readback-return-scale obstruction;
- it does **not** establish any obstruction on an arbitrary shorter accessible horizon;
- do not say "before recurrence" or imply a result for `K < N_CR` unless Target 3 or another theorem proves one.

## A4. Corrected Target 3 — horizon tightness

Target 3 now asks whether the `N_CR` theorem is tight:

`exists R, CausalReadback(R)` with controlling horizon `N_CR` such that

- for every `K < N_CR`, the rooted family is `PDivisibleWithin(K)`;
- but it is not `PDivisibleWithin(N_CR)`.

The original two-state monotone-mixing construction remains the declared attempt. For a successful instance it must be arranged that the candidate's declared snapback time `N` is in fact its controlling `N_CR` under the definition above.

Thus a successful candidate must verify all of the following, not merely the stochastic matrix prefix:

- one finite reversible `RootedRealization` with one fixed `phi` and one fixed hidden prior;
- the full frozen `CausalReadback` parent;
- every rooted map through the candidate snapback horizon;
- `Gamma_N = I`;
- at least one storage witness occurs at some `s < N`;
- no earlier time `n < N` both has `Gamma_n = I` and lies after some storage witness, so that `N = N_CR`;
- `PDivisibleWithin(K)` for every `K < N`;
- failure of `PDivisibleWithin(N)`.

The existing b51 prefix dilation remains insufficient unless its full orbit completion is deliberately designed and the above full-horizon properties are verified.

The T3-A/T3-B/T3-C/T3-D outcome taxonomy and its interpretation rules remain unchanged, with every occurrence of the target horizon read as `N_CR`.

In particular:

- construction/tooling failure without an impossibility theorem is still T3-C, not a mathematical refutation;
- if an earlier obstruction is proved unavoidable for all parent-positive finite reversible realizations, report the strongest earlier-horizon theorem actually proved;
- if a tight realization succeeds, recurrence/readback-return-scale nonclassicality remains a limitation on accessible OI -> QM unless an independent physical result bounds `N_CR` to accessible times.

## A5. Mandatory formalization for Targets 1 and 2

The original evidence hierarchy said "Mathlib/Lean theorem ... where practical." For Targets 1 and 2 this latitude is removed.

Targets 1 and 2 are preregistered to receive kernel-checked formal statements against the existing `RootedRealization`, `C4r`, `PDivisibleWithin`, and total-variation interfaces, or against the nearest exact existing interfaces if a minor representation adapter is required.

If either theorem cannot be formalized in the current interface, execution must report separately:

1. the mathematical/prose status of the statement;
2. the exact formalization blocker;
3. whether the blocker is an interface/tooling limitation or a mathematical failure.

A prose proof alone must not be classified as a fully formalized success, and a formalization/tooling failure must not be classified as a mathematical negative.

## A6. Frozen execution boundary

No candidate full-period realization has been searched for, inspected, simulated, brute-forced, or constructed before this amendment.

After this amendment is frozen by commit SHA and blob hash, execution may begin under the combined original preregistration plus this controlling amendment. The original preregistration must remain byte-identical; any further scope correction must be another append-only preregistration amendment frozen before the affected execution.
