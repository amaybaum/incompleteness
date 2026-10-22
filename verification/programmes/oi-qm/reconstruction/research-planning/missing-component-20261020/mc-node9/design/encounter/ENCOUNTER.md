# Encounter construction: first calculation and paired detector controls

> **DRAFT — NOT FROZEN.** The owner's read-only session runs this construction. This file records its results with
> the coordinator's exact checks (`encounter_checks.py`). Added modelling identifications:
> - the hidden direction is the particle's direction of motion, at fixed speed v;
> - isotropic incident directions (`../transport/TRANSPORT.md`).

## Results

**1. Crossing time is harmless in the ideal slab** [exact, symbolic].
- Before depletion, the joint density of crossing time t and direction λ is v(u·λ)₊/(4πL) dt dΩ.
- Conditioned on crossing during [0, τ], it factorizes as (dt/τ) · (u·λ)₊/π dΩ. Crossing happens with probability
  τv/(4L).
- So the time is uniform and independent of the prepared direction, and recording it reveals nothing more about the
  direction.
- This is a single-particle statement, not a proof of independent repeated emissions.

**2. Parallel planar collectors with a deadline record fail preparation equivalence** [exact, symbolic; grids
bounded].
- **Setup.** The particle starts at the origin. Collecting planes at z = ±d give the Z outcome, and a clock records
  whether arrival T = d/(v|λ_z|) came before √2·d/v. That deadline bit B is equivalent to λ_z² > ½.
- **Probabilities.** Z-mix and X-mix are both I/2, and both give the two planes equal probability. Yet:
  - P(B | Z-mix) = ½, the central disk r² < ½ on the Z preparation disk;
  - P(B | X-mix) = ½ − 1/π, two circular segments |z| > 1/√2 on the X preparation disk, of total area π/2 − 1;
  - the gap is 1/π ≈ 0.3183, so any common quantum prediction errs by at least 1/(2π) ≈ 0.1592.
- **Finite grids** (exact rational counts; floats only for display): the gap is 0.3038, 0.3105 and 0.3170 at
  M = 10, 40 and 160.
- **What it takes.** A coarse deadline bit suffices: neither a precise clock nor a direct read of the hidden
  direction is needed.
- **Scope.** This rejects the planar device as an implementation of the claimed qubit interface. If the two
  preparations instead represent different accessible motional states of a larger quantum system, then I/2 does not
  describe the complete input. That would call for an expanded correspondence, and would not contradict quantum
  mechanics.

**3. A spherical collector removes this timing leak** [exact].
- With the collecting surface at radius d, every trajectory arrives at d/v, and the hemisphere of impact gives the
  outcome.
- **What it leaves open:**
  - the impact location d·λ still encodes the old direction;
  - transmitting the outcome can add location-dependent delays;
  - local detector changes can retain information that later operations reveal;
  - reuse must carry those changes forward.

## Paired controls for the encounter construction

| Detector | Required result | Status |
|---|---|---|
| Parallel planes with a deadline record | detects the preparation-equivalence failure (gap 1/π) | done, exact |
| Spherical collector | constant first-arrival time; then impact records, signal routing and reuse | arrival time done; the rest open |

## Next task (owner)

Specify how the spherical collector produces, and retains, only the intended accessible record through an actual
interaction. Isotropy settles the incoming distribution. The detector must still explain which information becomes a
lasting observable record.
