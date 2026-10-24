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

**Slots, reads and retries (all families).**
- **Slots.** Slot j runs from t_j to t_j + τ + Δ. A herald at time t in (t_j, t_j + τ] is read at t + Δ, which
  falls within the same slot.
- **Retries.** A retried preparation call uses the same hidden station and coin. A retried routed call uses the same
  routed station.
- **Probe calls** are never retried. A failed probe stays in the record.

**F1, the D6 sequences with a terminal read.**
1. **Preparation.** Called in slot 1. A failed call is retried in the next slot.
2. **Reads.** Read a₁, …, a_k, for every menu sequence with 0 ≤ k ≤ 3. After each read, the routed call to
   S_{s·a} follows in the next slot, retried until it succeeds.
3. **Terminal read.** After the last successful call, read along b, for each b in the menu. No further reset
   follows.
4. **Size.** There are 4 + 16 + 64 + 256 = 340 protocols, with at most 4 reads and at most 8 calls.
5. **Completion.** A run is complete if its terminal read happens by the end of slot 8. Otherwise it is incomplete,
   and its record ends at slot 8 with every call and failure so far.

**F2, probes.**
1. **Preparation.** Called in slot 1, not retried. A failure stays in the record.
2. **Probes.** In slots 2 and 3 the family probes (w₂) or (w₂, w₃), over all 8 + 64 address choices. The probes run
   whether or not the preparation succeeded.

**F3, read then probe.**
1. **Preparation.** Called in slot 1, not retried.
2. **Read.** On success, read a ∈ menu. On failure, the record shows "no carrier" and the read is skipped.
3. **Probe.** Station w is probed in slot 2 in either case. There are 4 × 8 = 32 protocols.

**Completion in F2 and F3.** These runs are always complete. Their preparation success probability is reported.

**Preparation pairs.** The six D6 basis relations, with mixtures realized by station coins. Relation 5 (r₊ against
½X₊ + ½Y₊) compares two identical procedures, and serves as control C3.

## 5. Metric

**Order of operations.** Write y for a complete visible record. For preparation i with hidden station choice w,
taken with probability p_i(w):
- the record density is p_i(y) = Σ_w p_i(w)·p(y | w);
- the metric is TV(P₁, P₂) = ½ ∫ |p₁(y) − p₂(y)| dy, over the discrete fields and the continuous timestamps.

Hidden choices are marginalized **before** the absolute value is taken. Summing conditional TV distances over w
would expose information the interface hides, and is not used.

**What the per-station statistics are.** The statistics (h, S) depend on the hidden station. They enter only inside
p(y | w); they are not record fields.

**Certified integration.**
- **Brackets.** Each (pair, protocol) cell gets a bracket [lo, hi]. It is computed by interval arithmetic (50
  digits) and adaptive box bisection over the continuous waiting times, using the monotonicity of each station
  density in its S.
- **Work limit, fixed now.**
  - At most 10⁶ box evaluations per cell.
  - At most 5·10⁸ in the whole run.
  - A cell whose bracket still straddles the threshold at its limit is UNDECIDED.
- **Completion probability** is reported for each protocol.

## 6. Controls (all must be green; otherwise VOID, and no verdict prints)

| Control | Requirement |
|---|---|
| C1 read-law derivation | the symbolic hemisphere integrals hold (`read_law_checks.py`) |
| C2 independent implementation | for N ∈ {1, 2, 3, 4} and one station: every success/failure pattern of 1–3 sequential calls (14 patterns), with symbolic call times t₁ < t₂ < t₃, symbolic non-overlapping windows τᵢ, symbolic herald offsets uᵢ ∈ (0, τᵢ) and symbolic q. The particle-level density, enumerating injective assignments of heralds to labelled particles and symbolically integrating each other particle's uniform arrival over the complement of the observed empty set, must simplify to the closed form. This is a symbolic identity over the continuous parameters, not a rational sample |
| C3 identity | relation 5 has hi = 0 exactly, on every protocol |
| C4 Poisson reference | for every pair and protocol, the reference densities agree pointwise, and hi ≤ 10⁻³⁰ |
| C5 herald-history regression | for fixed pools at N = 3 and a = b = 1/16, the protocol-W event difference is exactly 151201/16777216; it is 0 in the Poisson reference |
| C6 impact-read countercontrol (absorber privacy) | the interface is enlarged by the coarse impact bit E = [λ_z² > λ_x²] of the preparation carrier, with the joint law of (s, E) integrated exactly from the flux law. Z-mix against X-mix on F3 with a = Z must give lo > 0.02 |
| C8 address-exposure countercontrol (address privacy) | the interface is enlarged by the preparation's station address, which is shown even when the herald fails. Z-mix against X-mix on F2 with a single probe must give lo = hi = 1 |

## 7. Decision rule

**The verdict uses the independently computed brackets.** A bracket is never clipped to the theorem's ceiling.

**Pool allocation, on P*:**
- **ACCEPT** if hi ≤ 0.01 for every pair and protocol.
- **REJECT** if lo > 0.01 for any pair and protocol.
- **UNDECIDED** otherwise, including any cell that reaches its work limit.

**Diagnostic D1 (coupling consistency).** This is reported, and it is not a prerequisite. For every preparation and
protocol, the checker reports hi(TV(fixed pool, Poisson reference)) against mΛ²/N.
- **Why D1 cannot be a gate.** If C4 holds and D1 holds everywhere, the triangle inequality already bounds every
  pairwise distance by 2mΛ²/N ≈ 0.0098705. A certified REJECT then cannot occur.
- **What a violation means.** A certified violation of D1, or of the allocation, stays visible in the output, and
  triggers investigation of the implementation or of how the theorem is applied.

**What each verdict means.**
- **ACCEPT** verifies that the implemented finite-pool model, with its scheduling, reuse, conditioning and terminal
  reads, meets the frozen allowance on P*. P* is finite; Theorem C covers all admissible protocols analytically.
- **REJECT** means an implementation or theorem error, to be diagnosed before anything else.
- **Adding the aperture term.** The analytic aperture bound adds at most 0.01, for a total of at most 0.02.

## 8. Invariants and their checkpoints (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| Read law derived, not imported | C1; code review, so that no call reaches a quantum-reference routine |
| Finite-pool history carried exactly | C2 (symbolic identity), C5 |
| Terminal-state checks retained | the F1 definition (§4): every protocol ends in a read with no reset |
| Retry and failure branches fixed | the §4 definitions; the record schema is asserted in code |
| Hidden choices marginalized before TV | the §5 order of operations; C8 shows what exposure gives |
| No timestamp rounding | the §5 metric; the code path is checked in review |
| Preparation address hidden | C8; the record schema is asserted in code |
| Absorber records unread | C6 |
| Reference construction exact | C4 |
| Coupling bound respected | D1 (reported) |
| Identity procedures indistinguishable | C3 |
| Stop point operational | the §5 work limit and UNDECIDED |
