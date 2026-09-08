# Recurrence-horizon scaling and accessibility audit — result

Executed under the frozen preregistration `RECURRENCE-SCALING-AUDIT.md`, commit
`ce07c7762487ab1076479e116888a8150880ceff`, blob `0df67b4c4794036d341f4dee10408a40d5946359`.

Target allocation, recorded before execution: S1 was executed by the holder of the disclosed
S1-feasibility prior; S2 was executed independently, so that the prior could not weaken the
direction it disfavoured. Neither side's progress was treated as evidence for the other.

## Headline: O-4 mixed

- **S1 — proved.** For every `N >= 4` there is a parent-positive finite reversible realization
  `R_N`, tight at `N_CR(R_N) = N`. Tight realizations therefore exist at unboundedly many horizons.
- **S2-a — refuted**, by S1: no absolute constant bounds the horizon of tight realizations.
- **S2-c — proved.** `N_CR(R) <= 2 M` with `M = ord(phi)`, for every parent-positive finite
  reversible realization, hence `N_CR <= 2 (|V||H|)!`. This does not refute S1.
- **S2-b** — bounded-order and bounded-carrier class corollaries follow, without a coverage theorem.

Under the frozen taxonomy this is **O-4**: an unbounded tight construction together with a
non-refuting bound. O-4 takes precedence over O-1 and O-3, so exactly one headline class is
reported. It is not a contradiction: S1 and the `2M` bound quantify over different things, and the
separating condition is that `M` may grow along a family.

Nothing here establishes anything about physical accessibility. Per the frozen two-sided guard: a
positive scaling result shows arbitrarily delayed guaranteed obstruction is mathematically possible,
not that any physical time is inaccessible; and a horizon bound in microscopic periods is not a
physical timescale bound without an independently sourced relation between one microscopic step, or
`ord(phi)`, and accessible time.

---

# S1 — unbounded tight construction

## The family

For `N >= 4` put `m = N - 1` and

- `V = {0, 1}`;
- `H_N = { (j, t, c) : j in 1..m, t in Z_N, c in {0,1} }`, so `|H_N| = 2N(N-1)`;
- orbit word `w_j(t) = 1` iff `t = j` in `Z_N`;
- `phi_N (v, (j,t,c)) = ( w_j(t+1) if v = w_j(t) else 1 - w_j(t+1),  (j, t+1, c XOR v.[t=0]) )`;
- `mu_N (j,0,0) = mu_j`, zero elsewhere, with `mu_j = (2m + j) / Sigma`, `Sigma = sum_{i=1..m} (2m+i)`.

The ledger bit `c` records the initial visible value at the first step and is what makes the write
clause hold. Without it the hidden component would evolve independently of the visible root and the
realization would be the uncoupled product that PR #542 recorded as parent-negative; the probe
carries that as a control, and the no-ledger variant has the *same rooted family*, so the control
isolates W rather than perturbing anything else.

## Uniform proofs

### L1 — the weights, and why the family starts at `N = 4`

`mu_j > 0` and `mu_j < mu_{j+1}` are immediate from the numerators, and `sum_j mu_j = 1` by
construction. The largest weight is `mu_m = 3m / Sigma`, and

`3m / Sigma < 1/2  <=>  6m < 2m^2 + m(m+1)/2  <=>  12 < 5m + 1  <=>  m >= 3  <=>  N >= 4`.

So `max_j mu_j < 1/2` exactly when `N >= 4`. The threshold is structural, not an artifact: two
strictly increasing positive weights summing to `1` always put the larger above `1/2`. PR #543
supplies a tight realization at `N_CR = 3`, so the horizons `3, 4, 5, ...` are all realized. This
discharges the frozen "#543 recovery, or state why the family starts higher" control.

### L2 — `phi_N` is a permutation

The predicate `v = w_j(t)` is invariant along the step: if `v = w_j(t)` then `v' = w_j(t+1)`, and if
`v = 1 - w_j(t)` then `v' = 1 - w_j(t+1)`. So each state carries a well-defined orbit parity, and the
inverse is explicit: from `(v', (j, t+1, c'))` recover the parity by comparing `v'` with `w_j(t+1)`,
then `v = w_j(t)` or `1 - w_j(t)` accordingly, then `c = c' XOR v.[t=0]`. Both composites are the
identity, so `phi_N` is a bijection of the finite set `V x H_N`.

### L3 — itineraries from the supported seeds

By induction on `t`, for every `j` in `1..m`:

- `phi_N^t (0, (j,0,0)) = ( w_j(t), (j, t, 0) )`;
- `phi_N^t (1, (j,0,0)) = ( 1 - w_j(t), (j, t, [t >= 1]) )`.

Base `t = 0` is immediate. For the step, note `w_j(0) = 0` because `j >= 1`. From root `0` the state
is on the primary parity, so the visible value tracks `w_j`, and the ledger is written with
`v = w_j(0) = 0` at `t = 0` and untouched afterwards, so `c` stays `0`. From root `1` the state is on
the complementary parity, the visible value tracks `1 - w_j`, and the ledger is written once with
`v = 1` at `t = 0`, so `c` becomes `1` and stays there.

### L4 — the rooted maps

`w_j(t) = 1` iff `t = j` in `Z_N`, and `j` ranges over `1..N-1`. So for `0 <= t <= N`, by L3,

- `t = 0`: no `j` equals `0`, so every seed shows visible `0` under root `0`; `Gamma_0 = I`.
- `1 <= t <= N-1`: exactly `j = t`, so `Gamma_t(0,0) = 1 - mu_t` and `Gamma_t(0,1) = mu_t`.
- `t = N`: `t = 0` in `Z_N`, so again no `j`; `Gamma_N = I`.

Root `1` gives the flipped row by the same computation. Hence

`Gamma_t = B(p_t)`,   `p_0 = p_N = 1`,   `p_t = 1 - mu_t` for `1 <= t <= N-1`,

where `B(p)` has rows `(p, 1-p)` and `(1-p, p)`.

### L5 — tightness (kernel)

The hypotheses of the kernel theorem `OIBridge.ScalingFamily.tight_at` hold for this `p`:
`p_t > 1/2` below `N` by L1; `p` is antitone below `N` because `mu` is increasing, with `p_0 = 1`
dominating; `p_{N-1} = 1 - mu_{N-1} < 1`; and `p_N = 1`. The theorem gives, uniformly in `N`,

`PDivisible K (fun t => B (p t))` for every `K < N`,  and  `PIndivisibleWithin N (fun t => B (p t))`.

The divisibility side is constructive there — the propagator `(p_t + p_s - 1)/(2 p_s - 1)` is
exhibited and proved stochastic — and the indivisibility side is the merged
`c4r_implies_pIndivisible` applied to a revival witness at `(N-1, N)`.

### L6 — the horizon really is `N_CR = N`

For `1 <= n <= N-1`, `Gamma_n = B(1 - mu_n) != I` because `mu_n > 0`. A storage witness exists at
`s = 1` by L7. So the least `n > 0` with `Gamma_n = I` lying after a storage witness is `N`, which is
the frozen definition of `N_CR`. In particular the reported snapback time is the controlling horizon
and not merely some visible return.

### L7 — the frozen parent, with explicit witness

Take `a = 0`, `b = 1`, `w = s = 1`, `x = 0`, `t = 2`, and the seed `(1,0,0)`, which has positive
prior mass `mu_1`.

- **W.** `phi_N (0,(1,0,0)) = (1, (1,1,0))` and `phi_N (1,(1,0,0)) = (0, (1,1,1))`. The hidden
  components `(1,1,0)` and `(1,1,1)` differ, under a common seed, after one step.
- **S.** At `s = 1` and `x = 0`: under root `0` the seeds with `j != 1` show visible `0`, with total
  mass `1 - mu_1 > 0` and hidden states `(j,1,0)`; under root `1` only `j = 1` shows visible `0`,
  with mass `mu_1 > 0` and hidden state `(1,1,1)`. Both are positive and the two conditional hidden
  laws have disjoint supports, so they differ.
- **R(1).** Hold `x = 0` and step once. From `(0,(j,1,0))` with `j != 1` the parity is primary, so
  the visible value becomes `w_j(2)`, giving `1` exactly when `j = 2`; the induced law is
  `(1 - mu_2/(1-mu_1), mu_2/(1-mu_1))`. From `(0,(1,1,1))` the parity is complementary, so the
  visible value becomes `1 - w_1(2) = 1` with certainty. These differ unless `mu_1 + mu_2 = 1`,
  which is impossible for `N >= 4` since `m >= 3` and every weight is positive.
- **R(2).** `Gamma_2 = B(1 - mu_2)` has distinct rows because `mu_2 != 1/2`.

The timing `0 < w <= s < t <= K` is satisfied by `w = s = 1 < t = 2`.

### L8 — `ord(phi_N) = 2N`

On a primary orbit the ledger is written with `v = w_j(0) = 0`, so `c` is unchanged over a full
clock cycle and the orbit has length `N`. On a complementary orbit it is written with `v = 1`, so `c`
flips once per clock cycle and the orbit has length `2N`. Every state lies on one of these, so
`ord(phi_N) = lcm(N, 2N) = 2N`.

This is not needed for S1. It makes the relation to S2 exact, and is recorded for that purpose.

### S1 theorem

For every `N >= 4`, `R_N` is a parent-positive finite reversible realization, tight at
`N_CR(R_N) = N`. Hence tight realizations exist at unboundedly many horizons and S1 holds.

---

# S2 — horizon bound on parent-positive realizations

Executed independently. Classification: **S2-c, universal parameter-dependent bound; non-refuting.**

## The bound

For every parent-positive finite reversible realization `R`, with `M = ord(phi)`,

`N_CR(R) <= 2 M`.

This is broader in scope than a bound on tight realizations alone: it holds for every
parent-positive finite reversible realization.

## Proof

Take any full frozen W/S/R witness `(a, b, h, w, s, x, t)` with `0 < w <= s < t`.

Because `phi^M = id`, every full-state trajectory, every rooted map and every root-conditioned
hidden law is periodic modulo `M`.

Choose `w0` the positive representative of `w mod M` in `{1,...,M}`. Choose `s0` congruent to
`s mod M`, least with `s0 >= w0`; since the base representative of `s mod M` lies in `{0,...,M-1}`
and lifting it above `w0 <= M` costs at most one period, `w0 <= s0 < 2M`. Choose `t0` congruent to
`t mod M`, least with `t0 > s0`.

The full parent witness survives this normalization:

- **W** survives because the same positive-prior seed evolved for congruent times reaches the same
  full state, hence the same hidden-component inequality.
- **S** survives because the joint visible/hidden law at `s0` equals that at `s`; the same visible
  `x` therefore has positive mass under both roots, and the two root-conditioned hidden laws are
  the original two and remain different.
- **R(1)** survives because `t0 - s0 = t - s (mod M)`, so propagating those same conditionals from
  the held visible value `x` through `t0 - s0` steps gives exactly the original two distinct visible
  laws.
- **R(2)** survives because `Gamma_(t0) = Gamma_t`.

So `s0` is a valid storage-witness time in a full parent witness, with `s0 < 2M`. Since
`phi^(2M) = id` we have `Gamma_(2M) = I`, so `2M` lies in the defining set

`{ n > 0 : Gamma_n = I and there exists a storage witness time s with s < n }`,

and by minimality `N_CR <= 2M`.

## Carrier corollary

`phi` is a permutation of `Q = |V||H|` microscopic states, so its order divides `Q!`, the order of
the symmetric group. Hence `M <= Q!` and

`N_CR(R) <= 2 (|V||H|)!`.

This is a coarse **S2-c** bound. Bounded microscopic order gives the **S2-b** subclass corollary
`N_CR <= 2 M0` on the class `ord(phi) <= M0`, and bounded carrier `Q <= Q0` gives `N_CR <= 2 Q0!`.
No coverage theorem is claimed, so none of these refutes S1.

## Why S2-c does not refute S1

S1 permits the carriers, and hence `M`, to grow along the family. The S1 family has
`|H_N| = 2N(N-1)` and, by L8, `M = 2N`. A bound growing with `M` is therefore consistent with
`N_CR -> infinity`. Refuting S1 from S2-c would additionally require a uniform carrier bound over
every putative S1 family, in the family-quantified form the preregistration fixes; none is claimed.

---

# Joint consequence

The S1 family has `M = 2 N_CR`, so the universal `O(M)` bound is attained up to a constant along an
unbounded sequence. The sharp joint statement is therefore about the **worst case**:

> the dependence of the controlling horizon on the microscopic period is `Theta(M)` — universally
> `N_CR = O(M)`, and there is an unbounded family with `N_CR = M/2`.

It would be wrong to state that every realization has `N_CR` comparable to `ord(phi)`. Nothing
proved here bounds `N_CR` from below, and a realization may have a large microscopic period and a
small controlling horizon. The result is a worst-case characterization, not a pointwise one.

# Evidence

Per programme reporting rule 9, stated where the results are reported.

- **Kernel-checked:** the family-level tightness, `OIBridge/ScalingFamily.lean`, eleven named
  results each printing only `propext`, `Classical.choice`, `Quot.sound`. `tight_at` is quantified
  over the horizon and over the retention sequence; it fixes no particular `N`. This carries L5.
- **Prose, uniform in `N`:** L1–L4 and L6–L8, the S1 realization half.
- **Prose:** the S2 `2M` theorem and its carrier corollary.
- **Exact instance controls:** `verification/lean/scaling_family_probe.py`, at `N = 4..12`, checking
  the permutation, the prior shape, `Gamma_t = B(p_t)` in closed form, strict decrease, `N_CR`
  minimality, all-pairs divisibility below `N`, revival at `(N-1, N)`, the parent witness, and
  `ord(phi) = 2N`; plus two negative controls, a no-ledger variant that must fail W while leaving
  the rooted family unchanged, and non-monotone weights that must break divisibility below the
  horizon.

**The formalization debt is the parent interface.** The frozen `CausalReadback` parent and `N_CR`
are not kernel predicates — PR #543's Lean development deliberately stopped at identity return plus
overlap — so neither L7 nor the S2 `2M` theorem can be stated in the kernel without first
formalizing the parent. Both are reported as prose for that reason. The finite-group ingredient of
S2 is standard and kernelizable with Mathlib's `orderOf` machinery, but kernelizing it alone would
not close the parent-level theorem, and partial formalization must not be narrated as
kernel-certified. This is interface debt, not a mathematical negative.

The instance table is **not** the result. Per the frozen preregistration a finite table of tight
realizations at increasing horizons is not an unbounded family; it is a control on the uniform
proofs, which are what carry S1.

# What this does not establish

- No claim that physical recurrence or readback-return times are large, small, or inaccessible. A
  bound in microscopic periods is not a physical timescale bound without an independently sourced
  relation between one microscopic step, or `ord(phi)`, and accessible time.
- No pointwise lower bound on `N_CR` in terms of `ord(phi)` for arbitrary realizations.
- No coverage theorem and no uniform carrier bound over putative S1 families, so no S1 refutation
  from any S2-b or S2-c result.
- No claim about horizons other than those realized by the S1 family.
- No manuscript is edited, no predicate is renamed, and nothing is named C5.
