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

**Gate 1, preparation mechanism: open; the needed object is a physical preparation process.**
- Relabelling a fixed finite set does not change its uniform counting measure. So the projected-area law is not a
  matter of coordinates.
- Uniform disk sampling and uniform sphere sampling assign different weights to physical directions. The second gives
  the earlier uniform-direction construction, which fails.
- **The question:** *what physically specified OI preparation process maps its initial counting measure into the
  projected-area distribution?* Choosing convenient coordinates cannot answer it.
- **Assumption-watch marker:** *a counting measure fixes a law over directions only through a physical map from the
  counted configurations to the directions.*

**Gate 2, recording mechanism: the reset is implemented, not derived.**
- **The implementation.** A conditional swap with a fresh disk seed does it: record σ = sign(n·λ), give the system
  the lift of the seed around σn, and move the old λ into a dump register. Moving the old state, rather than erasing
  it, makes the implementation deterministic.
- **Why this is not a derivation.** Supplying a fresh seed of exactly the projected-area law, and lifting it around
  σn, already incorporates the KS reset law. The standard model supplies this re-preparation update, and its
  explanatory status is a recognized limitation [Q, owner].
- **What the check shows.** `ks_checks.py` Part 3 shows injectivity only on a restricted ready-state domain, with
  measurement along the preparation axis. It is neither a permutation of a complete apparatus state space nor an
  implementation by OI's dynamics.

**Gate 3, access closure: stated operationally, with an exact witness.**
- **Requirements:**
  - every allowed read of the discard, and every later interaction, must preserve the claimed quantum statistics,
    including equivalence between preparation procedures;
  - reuse of a detector must restore the required apparatus distribution and independence, or carry a separate proof
    that its statistics stay valid.
  - "Never read a discard" and "never reuse a detector" are sufficient but stronger than necessary. A
    finite-resource recurrence argument does not prohibit every bounded reuse protocol.
- **Exact discard witness** (owner; Part 4, symbolic). Take the procedures Z-mix = ½μ_{+Z} + ½μ_{−Z} and
  X-mix = ½μ_{+X} + ½μ_{−X}. Both are I/2, so quantum mechanics cannot distinguish them through the system and an
  identically prepared, independent detector.
  - A discard read E: λ_z² > λ_x² becomes the ellipse 2x² + y² < 1 on the preparation disk.
  - P(E | Z-mix) = 1/√2 and P(E | X-mix) = 1 − 1/√2. The gap is √2 − 1, where quantum mechanics requires 0.
- **Interpretation.** This does not forbid preparation contextuality, since different hidden laws are allowed. It
  shows exactly which additional access would make the hidden difference observable.
- **In the benchmark.** The ten-preparation T4 test does not cover this case. D6 therefore gains test T5,
  preparation equivalence between procedures with the same quantum state, discard reads included, with its own
  countercontrol (`../instrument/`).

## Boundaries, fixed in advance

- **Continuity.** The model is continuous. A finite OI realization needs a declared approximation family, for
  example the M-grid above, and an error criterion: an ε-form of D6 with stated tolerances at depth 3. The exact D6
  verdicts do not apply to it, and nothing may be accepted by rounding.
- **Composites.** A single-qubit success gives no entangled composite construction and no Bell result.

## Verdict under the stop rule

The construction is a **conditional calibration**. It shows that the desired measurement behaviour can be implemented
with specified resources:
- a preparation process supplying the projected-area law (Gate 1);
- a fresh seed of that law at every recording (Gate 2);
- discard and reuse rules that keep the statistics, preparation equivalence included (Gate 3).

It does not explain why OI supplies them. The next investigation concerns preparation equivalence and detector access.
A candidate specifies its preparation process, complete recording interaction, and every later apparatus operation
together. A restriction such as C5 may limit these, but it must survive physical recording and reuse, not just declare
the unwanted information inaccessible. No large implementation should start before then.
