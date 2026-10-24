# Candidate C-SPH-1: herald stations with a gated spherical collector

> **DRAFT — NOT FROZEN.** One complete candidate on owner instruction (2026-10-22). The candidate is fixed here
> before any test of it is run. It is not a native OI candidate, and a pass establishes only the bounded
> correspondence stated below.

**Labels** for every premise:
- **[ADD]**: the provisionally accepted Added premise.
- **[OI]**: sourced from OI.
- **[IM]**: independently motivated.
- **[CAL]**: introduced for calibration.

## 1. The candidate

**Stations.** There is one station S_w for each w ∈ W = {±X, ±Y, ±Z, ±R}, R = (4/5, 3/5, 0).

**Reservoir of S_w.**
- **Particles.** N particles, its own: no particle is shared between stations [CAL].
- **Initial positions.** Independent, uniform in the slab −L < w·x < 0. The transverse coordinates are periodic.
  Uniformity and independence are the product counting measure on single-particle configurations [OI].
- **Directions.** Independent of position and uniform on S² [ADD: isotropy].
- **Speed.** A common speed v [CAL]. A speed spread would move the horizon below.
- **Motion.** Ballistic and non-interacting.

**Walls.**
- **Shutter wall.** The plane w·x = 0 carries a point-like shutter aperture at O_w. The rest of the plane absorbs.
- **Back wall.** The plane w·x = −L absorbs.
- **Absorption.** It stores the particle's full state (position, direction, time) in the wall's microstate. Nothing
  is erased, so the dynamics stays deterministic and injective [OI].

**Herald.**
- **Call.** The station is called at time t_call, a function of the accessible record.
- **Selection rule [IM].** The shutter passes the first particle reaching the aperture at or after t_call, then
  closes. Every other arrival is absorbed.
- **Record.** The herald bit and the crossing time t. A call that fails within the window τ is retried in the next
  window, and the failure stays in the record.

**Collector.**
- **Geometry.** A sphere of radius d centred at O_w. The passed particle is absorbed at its impact point.
- **Readout along a.**
  - The collector is split by the plane a·x = 0 into two shells.
  - The struck shell latches.
  - The latch is read at the fixed delay Δ after t, with Δ greater than every flight time [IM: gated readout].
- **Outcome.** s = sign(a·λ) in the point-aperture limit [CAL].
  - For an aperture of radius ρ, s differs from sign(a·λ) only if |a·λ| < ρ/(d − ρ).
  - Under μ_w that has probability at most 4ρ/(d − ρ), because the density is at most 1/π on a band of area
    at most 4π·ρ/(d − ρ).

**Accessible record.** Herald bits, crossing times t, and outcomes s, all at fixed delays.
- The collector's absorber states and the walls' absorber states are **not** read by any declared operation. This is
  the access closure, and it is **supplied**, not derived (§4).

**Update (routing) [CAL].**
- **Rule.** After outcome s along a, the next system is the herald of station S_{sa}.
- **Why it is forced.** Repetition (D6 T2) requires the next law to be supported in {s a·λ > 0}. Among the
  family μ_w, which is supported on {w·λ > 0}, only w = sa qualifies.
- **What it is fixed by.** The routing therefore follows from repeatability. No probability enters its choice.

**Mixtures.** A mixed preparation chooses its station with an independent coin, and the coin is not recorded:
- Z-mix = ½ S_{+Z} + ½ S_{−Z};
- X-mix and R-mix likewise;
- r₊ = ½ S_{+X} + ½ S_{+Y}, and r₋ likewise.

**State carried forward.** Each station's remaining particles, its wall and collector absorbers, and its latches
are carried from one encounter to the next. No fresh seed is inserted: every emitted system is a reservoir particle
selected by the herald rule.

**Bounded milestone [CAL].**
- **Menu:** X, Y, Z, R.
- **Preparations:** the ten D6 preparations.
- **Horizon:** depth 3.
- **Resource budget:**
  - at most four emissions per run;
  - every herald of every station crosses by time L/v (the fast band);
  - a station has about N·(aperture area)/(4·transverse area) fast-band heralds before depletion.
- **Accuracy:** the finite realization's measured error ε, reported per test and never rounded to acceptance.
  The exact target remains A1.

## 2. Preregistered apparatus prediction (written and committed before the finite test is run)

`collector_predict.py` computes the following continuum values, recorded in `collector_predict.out`, with
L = v = 1 and τ = 1/4. Nothing in that script reads a finite direction set.

**What is predicted.**
- **Fast band (windows 1–4).** The herald law equals μ_w. This is the control.
- **Past L/v (windows 5–8).** The law is weighted by the depth band, w_k(c) = min(kcτ, 1) − min((k−1)cτ, 1), and
  first reads depart from the projected-area values.

| case | QM | k = 4 | k = 5 | k = 6 | k = 7 | k = 8 |
|---|---|---|---|---|---|---|
| X+ / R, also R+ / X | 0.9 | 0.9 | 0.875 | 0.8125 | 0.73848 | 0.68236 |
| Y+ / R | 0.8 | 0.8 | 0.75 | 0.65556 | 0.61718 | 0.59619 |
| Z+ / R | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |

- **Relation-6 residual.** The equivalence r₊ = (5/6)R₊ + (1/6)X₋ of D6 becomes observable past L/v. At window 8
  its residual is +0.181 on X, +0.170 on Y, 0 on Z and −0.247 on R.
- **Repetition along the station axis stays exact at every window.**
- **Timing.** The crossing time is independent of the outcome up to L/v and informative after it.

**Decision rule, fixed now.**
- **Control (precondition).**
  - In windows 1–4 the finite law must equal the finite set's flux law ∝ (w·λ)₊ exactly.
  - Otherwise the test is void and no verdict prints.
- **Finite sets.** Rational spheres of radius N = 45 (510 directions) and N = 105 (1350 directions), evaluated with
  exact rationals.
- **Ties.** Counted ½ in P(+). This is fixed before the run.
- **Error scale e_N.** The largest |P_N − P_cont| over windows 1–4 and the four cases.
- **Prediction supported only if all of these hold:**
  - (a) Z+/R gives exactly ½ at every window and both N;
  - (b) for k = 5–8 and the cases X+/R, Y+/R and R+/X, |P_N,k − P_cont,k| ≤ 3e_N at both N;
  - (c) the window-8 relation-6 residual has the predicted signs on X, Y and R at both N.
- **Otherwise** it is not supported at these N, and the verdict names the failing clause.
- **Disclosure.** Values at N = 15 were seen earlier (`../transport/`) and are not part of this test.

**Scope.** A depletion curve confirmed here is a prediction of this apparatus. It becomes an OI prediction only once
the reservoir's physical sourcing, isotropy included, is established.

## 3. The conditional two-emission law (`collector_checks.py` Part 1, exact)

**Claim.** Take any herald of a station whose particle has not yet entered any record. The complete accessible record
depends on that particle only through its crossing time. This holds for every call time that is a function of the
record.

**Consequence.** Given its crossing time t, and given that the herald succeeded, the herald's direction law is
∝ (w·λ)·1[w·λ < L/(vt)]. That is exactly μ_w up to L/v, and it is independent of the rest of the record.

**What the claim does not cover.** It conditions on the herald's own crossing time. It says nothing about the
probability that a herald, or a failure, is recorded at all. That probability does depend on the station's history
(§4).

**Checks.** Three particles, the 30-direction rational sphere, continuous depths.

| Case | Result |
|---|---|
| A: fast band, record = window index and outcome | the law equals the flux law for all 15 record values |
| B: record includes the exact crossing time, fast and late | the law equals the truncated flux law in all 20 cases |
| C, C′: late windows or straddling intervals, window index only | no dependence on the first record (the 30-direction set has three values of c, so the density is constant on those intervals) |
| C″: richer set (102 directions), both emissions late, window index only | the law depends on the first record; the dependence is exact, of size 1.26·10⁻⁴ |
| D: countercontrol, absorbed system recycled into the reservoir | caught: TV 0.543 |
| E: countercontrol, reservoir sharing one direction | caught: TV 1 |

## 4. Herald statistics expose the station's history (owner witness; `herald_checks.py`, exact)

**Protocol W.**
1. Prepare Z-mix or X-mix, with the initial herald in window A.
2. Measure Z.
3. Call the routed station in a later disjoint window B. Both windows may lie before L/v.

**Why the two mixtures differ.**
- Under Z-mix, the outcome routes back to the station that supplied the initial particle.
- Under X-mix, it routes to a Z station that has not been called before.

**Setting.** Each of a station's N particles crosses the aperture in A with probability a, or in B with probability
b.

**Result.**
- **The difference.** P(H_A F_B | Z-mix) − P(H_A F_B | X-mix) = ((1−a)(1−b))^N − (1−a−b)^N. It is strictly
  positive for every N ≥ 1 when a, b > 0.
- **Example.** At N = 3 and a = b = 1/16:
  - the conditional failure probabilities are 631/721 and 3375/4096;
  - the joint difference is 151201/16777216 ≈ 0.0090, which reproduces the owner's values.
- **Bound.** The difference is at most N·ab·((1−a)(1−b))^(N−1), checked exactly on a grid.
- **Scaling.** At fixed expected crossings a = α/N and b = β/N, it falls as αβe^(−α−β)/N. Its leading coefficient
  has maximum e⁻², an asymptotic scale, not a finite-N bound: at N = 3 and a = b = 1/3 the exact difference is
  37/729 ≈ 0.0508, above e⁻²/3 ≈ 0.0451. The finite-N bound is the one above.
- **Poisson comparison.** If each station's particle number is Poisson with mean μ, the difference is identically 0.
  Counts in disjoint windows are then independent.

**What this means.** The specified finite apparatus does not satisfy preparation equivalence. The witness uses
the declared herald record alone, before any detector record is read. Gate 3 therefore requires more than absorber
privacy: the herald statistics must not depend on preparation history.

**Scope.** This is a counterexample to C-SPH-1's interface equivalence. It is not an impossibility result for
transport-generated resets.

## 5. Verdict on the reset

**What is generated.** The successful fast-band emission law μ_{sa} is generated by flux selection at station S_{sa}.
This holds conditional on the stipulated reservoir ensemble:
- independent particles, uniform positions, isotropic directions [ADD];
- a common speed.

The seed is isotropic, not already projected-area distributed. The successful emission distribution is generated by
flux selection; the routing that decides which station emits is a supplied component of the instrument.

**What is supplied.**
- **The routing.** Repeatability alone only requires the next law to be supported in {s a·λ > 0}. S_{sa} is the
  unique choice within the chosen emitter family {S_w}, so the routing comes from that family, not from
  repeatability by itself.
- **The resource assumptions:** disjoint pools, the fast-band budget, and the pool statistics that §4 shows to be
  observable.
- **Access closure for the absorbers,** which is declared.

**Carrier.** The encounter itself produces only s: the incoming carrier is absorbed, and a new one is emitted.

**Classification.** The complete instrument is a conditional construction. Its interface equivalence fails for finite
canonical pools (§4).

## 6. The reduced direction/reset kernel against D6 (`collector_checks.py` Part 2)

**What the model contains.** The finite D6 model carries only the current direction, and each measurement applies a
fixed replacement law. It carries no station inventories, crossing clocks or herald failures. So these results
concern that reduced kernel, not the specified apparatus with its complete transcript.

**Results.**
- **Errors.** T2 is exact. T1 errors are 0.016, 0.020 and 0.0082 (total variation). The largest total variation over
  the depth-≤3 outcome transcript is 0.029, 0.037 and 0.013. These are at 96, 120 and 480 directions.
- **Functional span.** Its dimension is 5, so the reduced kernel's equivalences are exactly unobservable in the
  continuum.

**Depth-3 preparation-equivalence bias.**

| Model | N = 9 | N = 15 |
|---|---|---|
| reduced kernel | 0.0134 | 0.0052 |
| impact-read control | 0.357 | 0.416 |
| depleted-station control | 0.242 | 0.290 |

## 7. The preregistered prediction

**Verdict, as printed by its fixed rule: not supported at N = 45 and 105, failing clause (b).** The control was
green, and clauses (a) and (c) hold.

**Correction to the prediction itself.**
- **What the prediction computed.** It averaged bulk crossings in each window, as did the finite test
  (`window_law`) and the Monte Carlo (`collector_mc.py`).
- **What the apparatus does.** It selects the first arrival after a call. That arrival's density carries the
  factor N·f(t, λ)·[1 − F(t) + F(t₀)]^(N−1).
- **Consequence.** The prediction, its test and the Monte Carlo therefore concern the bulk-crossing law, not this
  apparatus's herald. The Monte Carlo agreement (largest |z| 1.93 over 32 cells) corroborates only the bulk-crossing
  formula. It does not show that the failed clause reflects a tolerance rather than the apparatus.

**`first_arrival.py`** gives the corrected window law for a station called once, with N particles and aperture pass
probability η, conditioned on success:
- **Fast band.** Windows 1–4 are exactly (1 + cos α)/2 for every (N, η).
- **Past L/v.** The values depend on N and η separately; N·η controls the Poisson scaling limit. For X+/R at
  window 5:

| N | η | N·η | P(+) |
|---|---|---|---|
| 3 | 1/4 | 0.75 | 0.875117 |
| 3 | 1 | 3 | 0.875476 |
| 30 | 1/10 | 3 | 0.875673 |
| 300 | 1/100 | 3 | 0.875693 |
| 100 | 1 | 100 | 0.891350 |

  The bulk-crossing value is 0.875.

No acceptance rule is attached. A new test needs its rule preregistered first, with the pool size, aperture, call
schedule and conditioning fixed.

## 8. Next

**Target (owner decision).** Bounded approximate equivalence with fixed-size pools, with the Poisson model as the
mathematical reference.

**Done (`REFERENCE.md`).**
- **Theorem R.** Independent Poisson pools make timing and failure records independent of station history under
  every admissible adaptive protocol within T ≤ L/v.
- **Theorem C.** For fixed pools, the transcript distance between two equivalent preparations is at most
  min(1, 2mΛ²/N).

**Open.**
1. Freeze the horizon, aperture, budget, success probability, latency and total error allowance.
2. Build the complete-record D6 checker.
3. Composite work stays parked. The local CHSH ≤ 2 boundary stands, and any herald-conditioned Bell test must account
   for selection.
