# Governed round for the finite native-gate ball theorem — design options (read-only draft)

- `D` = `main` at L42 `fdebc6e3`.
- A native V3 round (§A.39): one pull request from `D`, owner-designated `F`, linear execution to `E`, receipt `Q`.
- Nothing has been drafted into the repository.

## Placement and name (proposal)

- **Directory:** `verification/programmes/oi-qm/reconstruction/`, beside `round-bg-1-integer-classification`. The
  result is a reconstruction (K/R) theorem, not a Track-B fixed-basis result.
- **Name:** `round-nb-1-native-gate-ball` ("NB-1").
- **Kind:** non-sealing.

## What the round certifies: the decision needed before drafting

| option | kernel (Lean) | exact computation | general-d statement | cost and risk |
| --- | --- | --- | --- | --- |
| **E — exact only** | none | frozen probe: S1/S2 solution spaces for d = 2…7 and every p; S3 identity for p ≤ 8; S4 value identity; the three countermodels and the d = 3 control | recorded as a hand proof, **not certified**; the certified claim is "for d ≤ 7" | small; UNDECIDED very unlikely |
| **H — hybrid** | the dimension-free core: S3 (finite average ⇒ `g = K = 0` for `p ≥ 2`), S5 (parity lemma), and "S2-form + positivity ⇒ p ≤ 1" stated with S2's block form as a hypothesis | as E, and it certifies S1/S2 for d ≤ 7 | general d certified **conditionally** on S1/S2 holding for all d, which is hand-proved and exact for d ≤ 7 | moderate; UNDECIDED live on the kernel targets |
| **K — full kernel** | the whole theorem for every d: Lorentz cones, min/max, the corner arguments made algebraic via rational parametrization (a polynomial `≥ 0` near 0 ⇒ zero linear coefficient) | as E, kept as controls | certified | large; UNDECIDED the most likely outcome of the main target, as in BG-1 |

**Recommendation: H.**
- It kernel-certifies exactly the steps where the reasoning is dimension-free and delicate: the averaging bound and
  parity.
- It keeps S1/S2 in the exact-computation layer, where it is already verified, with the layers distinct (§A.40,
  Code Review Rules).
- The general-d proof of S1/S2 would be a natural follow-on K round, and it would not block this one.

## Frozen content, whichever option

- **Statement**, exactly as in `THEOREM.md`. The hypotheses:
  - the full self-dual effect cones;
  - **one common N**;
  - F;
  - P± (G and G⁻¹ send products into `max`);
  - Rt and Rc.

  The non-uses: `G² = I`, normalization, a cone `C`, a continuous group, SWAP, unitary control.
- **Three load-bearing countercontrols**, each of which must survive, together with the d = 3 control.
  - Drop Rc: the d = 5 J/K map.
  - `N_A ≠ N_B`: the d = 5 two-NOT map.
  - Keep the algebra and break positivity: d = 7, exact `1 − √3`.
- **Interpretation, frozen as conditional.** The theorem is abstract GPT mathematics. Its OI reading is:
  "OI-supplied finite gate algebra + identical-copy covariance + ball/local-tomography K assumptions ⇒ d = 3".
  Identical-copy covariance is recorded as a **premise**, pending the source audit. No outcome licenses "OI ⇒ d = 3".
- **Manuscript propagation.** None in this round. It is gated on the covariance audit and a later decision.

## Open items that do not block the round

- The one-sided variant: is `G` injective with `G(min) ⊆ max` enough?
- Unrelated NOTs; non-ball systems.
- Full-text prior-art reads (Krumm–Müller, Masanes et al., Al-Safi–Richens).
