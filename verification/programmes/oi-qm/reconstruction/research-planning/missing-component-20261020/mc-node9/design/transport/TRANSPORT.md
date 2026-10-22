# Design calculation: transport across an oriented surface as the projected-area preparation

> **DRAFT — NOT FROZEN.** A small design calculation on owner instruction (2026-10-22), inside the projected-area
> route. It is not a native OI candidate. Any transport, preparation or access premise used here is declared; such
> premises may become independent C5 premises and need not follow from C1–C4.

**The question (owner):** can a reservoir of deterministic trajectories crossing an oriented detector surface generate
the projected-area preparation law μ_u(λ) = max(0, u·λ)/π through its actual transport dynamics?

## Results (`transport_checks.py`; sympy for part A, exact rationals for parts B and C)

**A. Flux weighting gives exactly μ_u** [exact, symbolic].
- Setting: positions uniform in a slab of depth L behind the surface, isotropic directions, fixed speed.
- A particle with direction λ crosses during a short window τ exactly when its depth is less than (u·λ)τ.
- So the crossing-conditioned law is proportional to (u·λ)₊, and normalized it is μ_u. This is the cosine (Lambert)
  law of flux through a surface.
- The herald succeeds with probability ¼ · τ/L per window.
- The preparation is therefore a herald on a crossing record, applied to a counting measure on positions and
  directions.

**B. The incident direction set carries the result** [exact, bounded]. The target is P(+ | u = X+, n = R) = 9/10:

| Direction set | Result |
|---|---|
| The cubic lattice's own six unit directions | Fails: P = 1, an error of 1/10. For u = Z+ and n = R, every heralded direction lies on the tie boundary n·λ = 0 |
| Near-isotropic rational direction sets (integer vectors of norm N) | Errors between 1/1000 and 1/20 for N = 3, 9, 15, 25, 45 |

- The rational-set errors are not monotone in N.
- Tie weight, i.e. directions with n·λ = 0, does not vanish.

**C. Reuse of one reservoir** [exact, N = 15, L = 1, τ = 1/4].
- The herald law is exactly ∝ (u·v)₊ for the first ⌊L/τ⌋ = 4 windows. In window k, each direction crosses from the
  depth band [(k − 1)(u·v)τ, k(u·v)τ).
- After that the fast directions are exhausted and the law drifts toward grazing directions: the maximum deviation
  is 15/551 at window 5, and P(+ | X+, R) is 37/58 at window 7.
- A finite reservoir therefore supports a bounded number of exact preparations, then needs replenishment. That is a
  counted resource.

## Pressure test (§A.31)

- **The earlier failing law comes back as an input.** The favourable reading is that transport supplies Gate 1. What
  it supplies is a conversion: an isotropic incident law becomes the projected-area law through flux selection. The
  isotropic law is the uniform-direction law that failed as a preparation; here it is the reservoir's input.
- **Isotropy is load-bearing, and the baseline doesn't supply it.** The displayed realization is a cubic lattice with
  nearest-neighbour coupling (Main.md:290), and its natural six-direction velocity set fails (B).
- **Assumption-watch marker:** *flux heralding turns an isotropic incident law into the projected-area law; the
  isotropy itself must be sourced.*
- **The herald needs a physical crossing record**, and its failure branch, ¾ of the time for τ = L, must be accounted
  for.

## Still to specify (owner's list), all open

1. The interaction that produces the outgoing system state and the record.
2. Where the old information goes.
3. Which later interactions can reach it. D6's T4 and T5 decide this once the model is finite and declared.
4. How repeated use changes the reservoir. C gives the first quantitative answer: the law is exact for ⌊L/τ⌋ windows,
   then drifts.

**Classification:** a physically interpretable Gate 1 mechanism with two declared premises, isotropic incident
directions and a crossing herald. It is not yet a candidate, because the recording interaction, the access rules and
reservoir replenishment are unspecified.
