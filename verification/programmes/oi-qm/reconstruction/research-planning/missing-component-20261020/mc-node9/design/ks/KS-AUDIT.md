# Design audit: projected-area preparation and detector interaction (Kochen–Specker qubit model)

> **DRAFT — NOT FROZEN.** A short design audit on owner instruction (2026-10-22). It is not the first native OI
> candidate. The owner's stop rule applies: if the preparation or the back-action can only be stipulated to reproduce
> QM, the construction is a conditional calibration, and work stops before a large implementation.

**The model** [Q; Kochen–Specker 1967 as described by the owner, not read here]:
- **Hidden state:** a direction λ on the sphere.
- **Preparation:** state u is μ_u(λ) = max(0, u·λ)/π.
- **Readout along n:** reports the hemisphere containing λ.
- **Update:** after outcome ±, λ is redistributed according to μ_{±n}.

## Exact checks (`ks_checks.py`; sympy 1.14 for the symbolic part, Fractions for the grids)

| Check | Result |
|---|---|
| Projected-area density | Lifting the unit disk onto the facing hemisphere has Jacobian dA = cos θ dΩ. So a uniform disk point gives density cos θ/π, of total mass 1 |
| First read | The part of the u-disk whose lift lies in H_n is bounded by an ellipse with semi-axes cos α and 1. So P(+ \| u, n) = (1 + cos α)/2, with α the angle between u and n |
| Sequences | The update resets to μ_{±n}, which is the quantum post-measurement state's preparation. By induction every sequence reproduces the Bloch-calculus reference, so the T1–T3 logic of D6 holds analytically, given λ is never read [arg] |
| Finite grid family | M × M cell centres in the disk, lifted. For u = X+ and n = R (target 9/10), P = 9/10 at M = 5 (a coincidence), 71/79 at M = 20 (error 1/790), and 9049/10054 at M = 80 (error 1/25135). This is bounded evidence of convergence, not a rate theorem |

## The three gates

**Gate 1, preparation mechanism: a mechanism is available, but its load-bearing choice is Added.**
- The cosine law is what the counting measure gives on a planar cell grid perpendicular to u, lifted onto the facing
  hemisphere. OI's counting measure (Main.md Lemma 3) would supply the uniformity.
- The same counting measure on a different chart gives a different law. Uniform cells on the sphere give the earlier
  uniform-direction construction, which fails.
- So the law is chart-dependent. What carries the result is the choice of the projection plane as the chart, and
  nothing in the baseline selects it.
- **Assumption-watch marker:** *a counting measure fixes a law only together with its chart.*

**Gate 2, recording mechanism: met by a declared bijection, with one fresh resource per measurement.**
- **The interaction.** Measuring along n, the detector carries a fresh disk seed s. The interaction is a conditional
  swap: σ = sign(n·λ) is recorded, the system receives the lift of s around σn, and the old λ moves into the
  detector's dump register.
- **What it achieves.** It is injective, so one declared dynamics produces both the outcome and the post-measurement
  distribution μ_{σn}, which is independent of the old λ. No separate reset rule is inserted afterwards.
- **The cost.** The KS caveat that the reset ignores the previous state becomes physical here: the previous state is
  moved, not erased. That costs one fresh projected-area seed per measurement. This is the fresh-card and AP-1
  resource, and it is Added.

**Gate 3, access closure: holds only under two further Added premises.**
- **(i) λ and the dump register are never readable.** A readable dump reveals the pre-measurement λ. That is a
  label-leak failure, which D6's T4 catches: λ carries more than the quantum trace distance permits.
- **(ii) A used detector is never reused unprepared.** Its seed register then holds a dumped λ, not a fresh disk seed.
  A fixed finite device must therefore keep re-preparing, and by the finite recurrence lemma it cannot keep the
  statistics at all late times without growing resources.
- **Mixed preparations r±.** These are mixtures of pure preparations, for example ½μ_{X+} + ½μ_{Y+}, and different
  decompositions give different hidden laws. The owner's rule permits this preparation dependence. T4 must then hold
  for each declared decomposition. It does when λ and the dump register are inaccessible, since the menu statistics
  equal QM.

## Boundaries, fixed in advance

- **Continuity.** The model is continuous. A finite OI realization needs a declared approximation family, for
  example the M-grid above, and an error criterion: an ε-form of D6 with stated tolerances at depth 3. The exact D6
  verdicts do not apply to it, and nothing may be accepted by rounding.
- **Composites.** A single-qubit success gives no entangled composite construction and no Bell result.

## Verdict under the stop rule

The construction is a **conditional calibration**:
- the chart behind the preparation law is chosen to give QM's first-read statistics (Gate 1);
- the recording interaction needs a fresh seed of exactly that law at every measurement, plus an inaccessible dump
  (Gates 2–3).

Each is a declared resource, not a consequence of the baseline. One question is left that would change this
classification:

> Does any chart that OI's finite substratum supplies for directions — a lattice projection, say — produce the
> projected-area law without being chosen for it, together with a source of fresh seeds whose dump stays
> inaccessible?

No large implementation should start before that question has an answer.
