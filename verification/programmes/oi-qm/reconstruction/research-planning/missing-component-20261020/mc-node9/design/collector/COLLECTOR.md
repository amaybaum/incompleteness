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
record, so it covers failed windows, retries, and every earlier crossing time and outcome.

**Consequence.** Given its crossing time t, the herald's direction law is ∝ (w·λ)·1[w·λ < L/(vt)]. That is:
- exactly μ_w up to L/v;
- truncated toward grazing directions after L/v;
- in both cases independent of the rest of the record.

So, within the fast band, resource independence holds exactly, and observable agreement follows from it.

**Checks.** Three particles, the 30-direction rational sphere, continuous depths.

| Case | Result |
|---|---|
| A: fast band, record = window index and outcome | the law equals the flux law for all 15 record values |
| B: record includes the exact crossing time, fast and late | the law equals the truncated flux law in all 20 cases |
| C, C′: late windows or straddling intervals, window index only | no dependence on the first record |
| C″: richer set (102 directions), first and second emission both late, window index only | the law depends on the first record; the dependence is exact, of size 1.26·10⁻⁴ |
| D: countercontrol, absorbed system recycled into the reservoir | caught: TV(law given s₁ = +, law given s₁ = −) = 0.543 |
| E: countercontrol, reservoir sharing one direction | caught: TV = 1 |

- **Why C and C′ show no dependence.** The 30-direction set has only three values of c, so the herald density is
  constant on those intervals.
- **What C″ means.** With a window-index record past L/v, earlier records shift the second law. Recording the exact
  crossing time, as in B, or staying inside the fast band, as in A, removes the shift.

## 4. Verdict: is the reset generated or supplied?

**The reset law is generated, given isotropy.**
- The outgoing law μ_{sa} comes from the herald dynamics of station S_{sa}: flux selection through its shutter
  plane, applied to an isotropic reservoir.
- It holds conditional on the complete accessible record (§3).
- No probability or update law is inserted. The seed is isotropic, not already projected-area distributed. This is
  the difference from Gate 2's lifted seed.
- The same mechanism supplies preparation and reset.

**What is supplied.**
- **[ADD] Isotropy** of the reservoir.
- **[CAL] The routing s → S_{sa}.** Repeatability fixes it uniquely among the stations, and no probability enters its
  choice.
- **[CAL] Disjoint reservoirs.** Countercontrols D and E show what sharing or recycling does.
- **[CAL] The fast-band budget.**
- **Access closure.** The collector's absorber keeps each absorbed λ, and no declared operation reads it. Stored
  particles do not interact, so collector reuse leaves later outcomes unaffected. But that inaccessibility is
  declared, not derived. One coarse read of the impact record breaks preparation equivalence (§5).

**Carrier.** The encounter itself only produces s: the incoming carrier is absorbed, and a new carrier is emitted.
This is the measure-and-reprepare form of the projected-area model.

**Under the stop rule.**
- The reset is not a calibration by insertion.
- Gate 3 remains conditional: closure is declared.

## 5. The whole apparatus against D6 (`collector_checks.py` Part 2)

**Finite realization.**
- **Direction set.** Rational spheres with every direction tied to a menu axis removed: 96, 120 and 480 directions
  at N = 9, 15, 45.
- **Laws.** Fast-band herald laws, and the routing as specified.

**Results.**
- **T2 is exact.**
- **T1 and T3 are bounded.** The maximum errors are 0.016 / 0.016, 0.020 / 0.029 and 0.0082 / 0.0089 at
  N = 9, 15, 45. The errors are not monotone in N.
- **Depth-free functional span.** Its dimension is 5: normalization plus the four first-read effects. Every reset is
  independent of the absorbed direction, so no deeper functional exists.
- **In the continuum,** this makes every D6 equivalence exactly unobservable: each relation's residual is
  Σ cᵢ(1 + n·rᵢ)/2 = 0. This is the depth-free result. The finite numbers below are the bounded check.

**Preparation equivalence at depth ≤ 3: the optimal bias between the two sides of each basis relation.** The quantum
value is 0.

| Model | N = 9 | N = 15 |
|---|---|---|
| C-SPH-1, fast band | 0.0134 | 0.0052 |
| control: coarse impact read I (is λ_z² > λ_x² for the absorbed system?) | 0.357 | 0.416 |
| control: depleted station (window 8) | 0.242 | 0.290 |

- **What the candidate's residual is.** It appears only in relation 6, and it is of the size of the finite-set error.
- **The impact read** gives a large bias in relations 1–4 that does not shrink with N. This is the access witness of
  Gate 3 on the actual collector.
- **Depletion** opens relation 6, as predicted.

## 6. The preregistered prediction: result

- **Control:** green. Windows 1–4 equal the finite flux law exactly.
- **Verdict as printed: not supported at N = 45 and 105; failing clause (b).**

| Clause | N = 45 | N = 105 |
|---|---|---|
| (a) Z+/R gives exactly ½ at every window | holds | holds |
| (b) late deviation ≤ 3e_N | fails: deviation 0.0219 against a bound of 0.0159 | fails: 0.0134 against 0.0060 |
| (c) relation-6 signs (X +0.180, Y +0.157, R −0.262 at N = 45) | hold | hold |

**Post-hoc diagnosis.** None of these checks changes the verdict.
- **The rational-sphere family converges erratically.** At N = 45, 105, 205, 325 and 425, the fast-band error is
  0.0053, 0.0020, 0.0066, 0.0079 and 0.0063. The late error is 0.022, 0.013, 0.024, 0.021 and 0.0094.
- **A Monte Carlo of the mechanism** (`collector_mc.py`: 4·10⁷ particles, fixed seed, floating point) reproduces
  every continuum value in all 32 cells, with largest |z| = 1.93.
- **So the failing clause most likely measured the rule's error scale.** Late windows weight c with a kink at
  1/(kτ), and the fast-band error e_N underestimates that discretization error. It did not measure the mechanism.
  This is a diagnosis. A re-test needs a new rule and a better-equidistributed exact family, fixed in advance.

## 7. Bounded milestone and next step

**Milestone status.**
- **The reset is generated** on the menu, the ten preparations and depth 3, within the fast-band budget, given
  isotropy.
- **Repetition is exact.**
- **First reads and sequences** match within the finite error ε (0.9% at N = 480 directions).
- **Preparation equivalence** holds exactly in the continuum, provided the collector record is never read.
- **A1 is not addressed.**

**Composite test, prediction stated now.** Two C-SPH-1 apparatuses determine each outcome from their own particle's
direction. Every pair state they can share is therefore a joint law over two directions, read out locally. With
setting choices independent of the source, CHSH ≤ 2. A composite test of this family is predicted to fail Bell-type correlations.

**What would have to change.** The premise that a composite's outcomes are fixed by local readout of each carrier's
own hidden direction. That is the next premise to examine, before any composite is built.
