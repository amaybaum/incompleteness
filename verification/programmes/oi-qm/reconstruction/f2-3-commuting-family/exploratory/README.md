# Exploratory: the strict sub-tick cone against the commuting condition

Exploratory evidence, floating point. It is not a result of F2-3, not a governed round, and nothing
here is a measurement or a claim.

**The question it explores.** On E1-L's generator family, does strict one-edge causality of the
coupling-layer flow at every intermediate flow time coincide with F2-3's commuting condition
`Γ_comm`?

**What is known exactly.** The forward direction is proved: on `Γ_comm` the layer flow at every
fraction is a product of commuting local gates, so the cone holds (F2-2 correction 1, row L3). The
converse is open.

**What `cone_probe.py` measures.** The weight that the Heisenberg image of each site-1 matrix unit
places on site 3, on the chain 1–2–3, at the sampled fractions `s ∈ {0.1, 0.3, 0.5, 0.7, 0.9, 1}`.

- **Cases:** `q = 3, 5`, centre-free couplings `(M₁₂, M₂₃) ∈ {(1,1), (1,2)}`.
- **Members:**
  - the principal member;
  - F2-3's `M_φ` and `M_C` (at `q = 3`);
  - 40 random members per case, each the principal generator plus a random rank-1 projector inside
    one eigenspace class of its gate (160 in all).

**What it found.**

- Every non-commuting member broke the cone at some sampled fraction below 1.
  - `M_φ` and `M_C` broke it at every sampled fraction.
  - For the random members, the probe records only the largest violation per member; the smallest
    of those was 0.235.
- The principal member kept it at every sampled fraction.

**What it does not show.**

- It does not exclude exceptional non-commuting members.
- It covers no other sizes, repertoires or graphs.
- It decides nothing about the converse.

Outside E1-L's family the converse fails: `H = P₂ + Q₂ ⊗ B₃` with `[P, Q] ≠ 0` keeps the cone
without commuting terms. So any proof must use the family's structure.

**Status.** Deferred by owner decision (2026-10-15). Strict sub-tick causality has no physical
source and is stronger than ordinary continuous-time locality. An equivalence would characterize
the candidate further without explaining its origin.

Run with `python3 -I cone_probe.py`; it uses numpy and scipy.
