# Recurrence-scale indivisibility and tightness audit — preregistration

Base: `main` at `7d4b9ec3d2df5d6ace28fe24d0cb83f853235ba6` (post-PR #542).

This round audits the exact horizon at which a finite reversible realization with realization-level causal readback must become P-indivisible, and whether the recurrence horizon is mathematically tight. It is deliberately separated from PR #542's accessible-window result.

No candidate full-period realization has been searched for, inspected, simulated, or constructed before this preregistration. The monotone two-state family below is a declared construction attempt only. Whether a single finite reversible realization can realize it over an entire period is an execution question.

## Fixed inherited layer

Use the merged PR #542 realization layer and parent without modification:

- finite visible state space `V` and hidden state space `H`;
- deterministic reversible update `phi : V × H ≃ V × H`;
- fixed hidden prior `mu_H`, independent of the visible root in the rooted family;
- rooted visible maps `Gamma_t(a,j) = P(X_t=j | X_0=a)`;
- realization-level `CausalReadback`, with write W, store S, causal read R(1), and rooted reappearance R(2).

Let `N > 0` denote an order of `phi`, so `phi^N = id`. The audit concerns the rooted family on the full horizon `0,…,N`.

The merged PR #542 result remains controlling for shorter accessible windows: `CausalReadback` does not imply `C4e`, `C4r`, or `PIndivisibleWithin K` on an arbitrary same accessible horizon `K`, and no same-window `C4cr` rescue exists.

## Target 1 — recurrence produces TV revival at horizon N

Audit the following implication at the exact recurrence horizon:

`CausalReadback(R) -> C4r(N)`.

Declared proof route, fixed before execution:

1. Finite reversibility gives `phi^N = id` for some positive `N`.
2. Therefore `Gamma_N = I`: for every root `a`, the time-`N` visible law is `delta_a`.
3. For the distinct witness roots `a != b` from the parent, the time-`N` total-variation distance is exactly `1`.
4. The store clause S supplies a visible value `x` at time `s < N` with positive probability under both witness roots.
5. Hence the two time-`s` rooted rows overlap, so
   `TV(Gamma_s(a,-), Gamma_s(b,-)) < 1`.
6. Therefore the pair `(s,N)` is a `C4r(N)` witness.

The claim is only at horizon `N`. It makes no claim that any `K < N` already contains a TV revival or a divisibility obstruction.

### Target-1 failure modes

Record separately if any of the following occurs:

- the current formal `CausalReadback` interface does not expose the storage witness in a form sufficient to prove row overlap;
- the current rooted-map interface does not make `Gamma_N = I` derivable from `phi^N = id` without an additional hypothesis;
- the manuscript / #538 definition of `C4r(K)` differs materially from the pairwise TV-revival reading used here;
- the implication is false for a reason not anticipated above.

Do not silently strengthen the parent to repair a failure.

## Target 2 — recurrence-scale P-indivisibility by existing #538 bridge

Audit the composition

`CausalReadback(R) -> C4r(N) -> PIndivisibleWithin(N)`.

The second arrow is to reuse the already-merged #538 theorem rather than re-prove stochastic-inverse rigidity unless reuse fails for a concrete interface reason.

The stochastic-inverse route is therefore a backup / cross-check, not a primary target of this round. No new rigidity lemma should be introduced merely because it offers an alternative proof of a conclusion already supplied by the merged `C4r -> PIndivisibleWithin` bridge.

### Target-2 interpretation rule fixed before execution

A proof of `PIndivisibleWithin(N)` alone does **not** count as evidence that accessible-time quantum-like nonclassicality is forced.

The round must report the exact horizon information:

- if only the recurrence-horizon theorem is obtained, report it as a mathematical recurrence-scale obstruction;
- do not phrase it as “P-indivisibility somewhere before recurrence”;
- do not imply any result for `K < N` unless Target 3 or a separate theorem establishes one.

## Target 3 — tightness of the recurrence horizon

Decide whether the recurrence-horizon theorem can be tight in the strongest finite-horizon sense.

Primary tightness target:

`exists R, N = order(phi), CausalReadback(R)` such that

- for every `K < N`, the rooted family is `PDivisibleWithin(K)`;
- but it is not `PDivisibleWithin(N)`.

Equivalently for the intended two-root witness, the declared construction seeks a full-period realization whose rooted-row TV distance is non-increasing at every time before `N`, and increases only when the recurrence restores `Gamma_N = I`.

### Declared construction attempt — frozen before execution

Use a two-state visible rooted family of symmetric binary channels

`B_p = [[p, 1-p], [1-p, p]]`

with

`Gamma_t = B_(p_t)`,

`1 = p_0 > p_1 > ... > p_(N-1) > 1/2`,

and

`Gamma_N = B_1 = I`.

For this family, write `d_p = p - 1/2`. The algebraic identity

`d(B_p B_q) = 2 d_p d_q`

implies

`TV(B_p) = 2 |d_p|`

for the distance between the two rooted rows, and gives the intended divisibility factorization during the monotone mixing phase:

`B_(p_t) = B_(p_s) B_q`

with

`d_q = d_(p_t) / (2 d_(p_s))`

whenever `s < t < N` and `p_t <= p_s`, provided the resulting `q` is stochastic (`q in [1/2,1]`).

The recurrence step to `Gamma_N = I` then forces TV back to `1`; if all earlier TV values are below `1`, the first revival may occur on `(N-1,N)`.

### Full-period realization requirement

This target is **not** satisfied by specifying stochastic matrices alone.

The construction must be realized by one finite reversible `RootedRealization` with:

- one fixed finite carrier `V × H`;
- one fixed permutation `phi` of order `N` (or with declared recurrence order used consistently in the theorem);
- one fixed hidden prior `mu_H`;
- the full rooted family controlled at **every** time `0 <= t <= N`;
- the full frozen `CausalReadback` parent satisfied.

The existing b51 finite-horizon dilation is not, by itself, a valid tightness construction: it controls only a declared finite prefix, after which completion to a permutation is arbitrary and its eventual order is not designed. Using b51 as a prefix is allowed only if execution adds and verifies a deliberately designed full-period orbit completion.

No search for such a completion may occur before this preregistration is frozen.

## Target-3 outcome classes

Classify the result without collapsing tooling limitations into mathematics:

**T3-A — tightness construction succeeds.**
A finite reversible parent-positive realization is exhibited with `PDivisibleWithin(K)` for every `K < N` and failure at `N`.

Interpretation fixed in advance: the universal nonclassicality guaranteed by finite recurrence can require reaching the recurrence horizon. Unless an independent physical bound makes `N` accessible, this is a limitation on accessible OI -> QM claims, not evidence that accessible quantum-style backflow is forced.

**T3-B — a shorter-horizon obstruction is proved unavoidable.**
No such tight realization can exist because an additional theorem forces C4r / P-indivisibility at some `K < N` under the frozen parent.

Interpretation fixed in advance: this strengthens the physical OI -> QM bridge. Report the earliest horizon statement actually proved; do not infer a quantitative accessibility claim without a bound on that horizon.

**T3-C — declared construction fails, but no impossibility theorem is proved.**
The attempted full-period realization cannot be built or verified with the chosen construction, while no theorem excludes all such realizations.

Interpretation fixed in advance: **open / tooling or construction failure**, not “tightness is false.” Record the exact obstruction and leave the mathematical existence question open.

**T3-D — tightness is refuted by a mathematical impossibility theorem specific to the target class but not by a universal earlier-obstruction theorem.**
Record exactly the class excluded and do not generalize beyond it.

## Mandatory controls

Execution must include controls that distinguish local from recurrence-scale behavior:

1. **PR #542 T3 local countermodel:** confirm the already-merged `I -> B_(3/4) -> B_(5/8)` family is P-divisible through `K=2`; do not infer anything about its arbitrary post-prefix completion.
2. **Delayed revival positive control:** a known family with an accessible collision / revival should trigger `C4r` and P-indivisibility before recurrence.
3. **Uncoupled reversible product:** finite recurrence without causal write should fail the parent; recurrence alone must not be misreported as causal readback.
4. **Prior-dependence control:** preserve the distinction between hidden-prior dependence of the rooted family and visible-root support dependence of history-level C4w.
5. **Full-period audit:** for any proposed tightness realization, enumerate or otherwise certify every rooted map through the declared recurrence horizon and verify the claimed order of `phi`.

## Evidence hierarchy

Preferred evidence, in order:

1. Mathlib/Lean theorem at the existing `RootedRealization`, `C4r`, and `PDivisibleWithin` interfaces where practical;
2. exact finite arithmetic probes for explicit full-period constructions and controls;
3. prose only for interpretation and theorem-boundary statements not naturally represented in the kernel.

A failure to formalize an otherwise proved statement must be reported separately from a mathematical failure.

## Publication / interpretation boundary

This research PR should not silently rewrite manuscript claims during execution. Publication-record cleanup is separate unless an executed theorem directly requires a scoped correction and the round records that change explicitly.

In particular, the round must distinguish:

- **accessible-window result (#542):** causal readback does not force local `C4r` or P-indivisibility;
- **recurrence-scale theorem (this round, if proved):** causal readback forces revival / P-indivisibility once the horizon includes a recurrence time `N`;
- **tightness (this round):** whether all shorter horizons `K < N` can remain P-divisible.

The interpretation of OI -> QM is determined by the combination, not by Target 2 alone.

## Execution discipline

- Freeze this preregistration by commit SHA and blob hash before any proof search, candidate full-period construction, brute-force search, or new simulation.
- Once frozen, do not rewrite this file. Corrections are append-only preregistration amendments committed and frozen before the affected execution.
- One PR only for this research round.
- If rebasing becomes unavoidable, verify the preregistration by blob hash; blob identity is authoritative.
- Final approval must name the exact completed PR head SHA after all required CI checks are green.

## Allowed final classifications

The round's final report must separately state:

1. Target 1 recurrence-to-`C4r(N)`: proved / failed / qualified;
2. Target 2 `PIndivisibleWithin(N)`: proved via #538 / proved by alternate route / failed / qualified;
3. Target 3 tightness: T3-A / T3-B / T3-C / T3-D;
4. exact horizon interpretation for OI -> QM;
5. whether any manuscript wording is now demonstrably too strong, without silently editing it unless separately authorized.
