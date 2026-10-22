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
