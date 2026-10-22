# C-SPH-1 complete-record checker: preregistration

> **DRAFT FOR OWNER REVIEW — NOT FROZEN.**
> - **Order.** This file fixes the claim, parameters, protocol families, metric, controls and decision rule before
>   any checker code exists. It is frozen only once the owner approves it.
> - **Stop point (owner direction, 2026-10-22).** When this bounded checkpoint is finished, numerical refinement of
>   C-SPH-1 stops. Work returns to the central question: which of the construction's essential assumptions OI
>   actually supplies.

## 1. The claim under test

Bounded approximate equivalence for finite particle pools with continuous directions:
- an analytically reduced checker;
- a separate finite-aperture bound;
- the frozen schedule below.

**Not claimed:**
- a finite microscopic state-space realization;
- any derivation of the reservoir, routing or access assumptions from OI;
- exact equivalence (A1);
- composite behaviour.

The fixed-pool candidate cannot be exactly equivalent, because its herald-history leak is positive at every finite
N.

## 2. Frozen parameters (owner, 2026-10-22; arithmetic in `freeze_checks.py`)

| Item | Value |
|---|---|
| Horizon | T = L/v = 1 |
| Slots | K = 8; slot j starts at t_j = (j − 1)(τ + Δ) |
| Window | τ = 23/200 |
| Readout delay | Δ = 1/100, with flight time below Δ |
| Arrivals | Λ = (200/23) ln 20 per station over the horizon, so the reference failure probability is 0.05 per call |
| Pool | N = 1,100,000 per station; q = Λ/N per particle; η = 4Λ/N |
| Stations | m = 8 |
| Allowance (pairwise transcript TV) | 0.02 in total: pools 0.01 (bound 16Λ²/N ≈ 0.0098705), aperture 0.01 (ρ/d ≤ 1/6401 for at most 8 reads), directions 0 |

## 3. The implemented model

**Mechanism representation.**
- **Arrivals.** For each station, M_w ~ Binomial(N, q) aperture arrivals in [0, T]. Given M_w, the arrival times
  are i.i.d. uniform on [0, T].
- **Directions.** Marks are integrated out analytically.
- **Shutter.** A call in slot j heralds the first arrival in (t_j, t_j + τ]. Arrivals while the shutter is closed
  are lost.
- **History.** Station history is carried exactly through failures, routing and probes.

**Closed form used by the checker.** A station whose observed record has h heralds and total observed empty time S
has density N(N−1)⋯(N−h+1)·(q/T)^h·(1 − qS/T)^(N−h). The Poisson reference replaces this with
(Λ/T)^h·e^(−ΛS/T).

**Read law.** P(s | a, w) = (1 + s·a·w)/2.
- **Where it comes from.** It is derived from the flux law (`read_law_checks.py`), not imported from the quantum
  reference.
- **What the checker does not do.** It does not validate the read law against a quantum routine that computes the
  same formula. Its principal verification targets are scheduling, resource reuse, conditioning and transcript
  probabilities.

**Visible record.** As defined in REFERENCE.md.
- **Visible:** slot, success, the exact crossing time, read (a, s), and probe addresses.
- **Hidden:** preparation addresses and coins, and absorber states.

**Timestamps.** They stay continuous. TV is computed over the continuous record with certified integration, and no
timestamp is rounded.

## 4. Protocol families P*

**F1, the D6 sequences.**
1. Preparation call in slot 1.
2. Read the menu sequence a₁…a_k, for every sequence with k ≤ 3; there are 84 sequences.
3. Each read is followed by its routed call in the next slot.
4. A failed call is retried in the next slot.
5. A run that runs out of slots is recorded as incomplete.

**F2, the probes.**
1. Preparation call in slot 1, with no read.
2. Probe calls to (w₂) or (w₂, w₃) in slots 2–3, over all 8 + 64 address choices.

**F3, read then probe.**
1. Preparation call in slot 1.
2. Read a ∈ menu.
3. Probe station w in slot 2. That gives 4 × 8 = 32 protocols.

**Preparation pairs.**
- The six D6 basis relations, with mixtures realized by station coins.
- Relation 5, r₊ against ½X₊ + ½Y₊, compares two identical procedures. It serves as the identity control C3.

## 5. Metric

**Metric.** For each pair and protocol: the TV distance between the two complete visible-record laws, taken over
discrete fields and continuous timestamps.

**Computation.**
- **Reduction.** The computation reduces to per-station sufficient statistics (h, S).
- **Brackets.** The checker reports a certified bracket [lo, hi]: interval arithmetic, plus monotone bracketing of
  the station densities on refined grids.
- **Completion.** Completion probability is reported separately for each protocol.

## 6. Controls (all must be green; otherwise VOID, and no verdict prints)

| Control | Requirement |
|---|---|
| C1 read-law derivation | the symbolic hemisphere integrals hold (`read_law_checks.py`) |
| C2 independent implementation | the station-level closed form equals a particle-level computation (each of N ≤ 4 particles with Bernoulli(q) arrival and uniform time; exact rationals) for every observation pattern of at most 3 calls on one station |
| C3 identity | relation 5 has hi = 0 exactly |
| C4 Poisson reference | for every pair and protocol, the reference densities agree pointwise, and hi ≤ 10⁻³⁰ |
| C5 herald-history regression | for fixed pools at N = 3 and a = b = 1/16, the protocol-W event difference is exactly 151201/16777216; it is 0 in the Poisson reference |
| C6 impact-read countercontrol | the interface is enlarged by the coarse impact bit E = [λ_z² > λ_x²] of the preparation carrier, with the joint law of (s, E) integrated exactly from the flux law. Z-mix against X-mix must give lo > 0.02 |
| C7 coupling consistency | for every preparation and protocol, hi(TV(fixed pool, Poisson reference)) ≤ mΛ²/N |

## 7. Decision rule

**Pool allocation, on P*:**
- **ACCEPT** if hi ≤ 0.01 for every pair and protocol. The total then stays within 0.02 once the analytic aperture
  bound is added.
- **REJECT** if lo > 0.01 for any pair and protocol.
- **UNDECIDED** otherwise. Brackets are refined; nothing is rounded to acceptance.

**What each verdict means.**
- **ACCEPT** verifies that the implemented finite-pool model, with its scheduling, reuse and conditioning, meets the
  frozen allowance on P*, consistent with Theorem C. P* is finite; Theorem C covers all admissible protocols
  analytically.
- **REJECT** means an implementation or theorem error, to be diagnosed before anything else.

## 8. Invariants and their checkpoints (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| Read law derived, not imported | C1; code review, so that no call reaches IB.Quantum |
| Finite-pool history carried exactly | C2, C5 |
| No timestamp rounding | the metric definition (§5); the code path is checked in review |
| Preparation address hidden | C6 shows what exposure does; the record schema is asserted in code |
| Reference construction exact | C4 |
| Coupling bound respected | C7 |
| Identity procedures indistinguishable | C3 |
