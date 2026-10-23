# Coordinator review: detector-boundary handoff v1

> **DRAFT — research record.** The owner's read-only session produced this exploratory diagnostic. It is recorded
> here with the coordinator's verification and independent checks. It adopts no rule as an OI premise and reopens no
> checkpoint.

## Verification

- **Archive.** The archive's sha256 is `d6eb7ba7de2f079beb5438951449c248832a020a8aa18576cd758a647f384b14`, as
  stated. The files in `handoff/` are its contents, unchanged. Their `SHA256SUMS` verifies.
- **Code review before running.** `detector_boundary_checks.py` uses only the standard library and does no I/O.
- **Replay.** Run from a separate directory, normally and with `-O`, the output is byte-identical to
  `detector_boundary_checks.out`.

## The handoff's corrections to report13: accepted and applied

1. **The fourth identity already fails without timestamps** (time-blind TV 0.00064), and the clock amplifies the
   failure. The report13 review previously said the failure appeared only in the joint record.
2. **J2 combined failures across read axes.** It used `fourth_fails |= bad`.
   - J2 now reports each axis separately, and its rerun gives X 245/245, Y 245/245, Z 0/245 and R 245/245
     nonzero positive-read atoms. This matches the handoff's independent count.
   - The fourth identity holds exactly on Z reads.
3. **Two tested frames show robustness to those frames, not a theorem for every frame.** Report13's review now says
   so.

## Independent checks (`coordinator_detector_checks.py`; separate code)

| Check | Result |
|---|---|
| K1 | The one-sided Chebyshev step gives 9/(16n + 9), and (13/16)(1 − 9/(16n + 9)) − 3/4 = (4n − 27)/(4(16n + 9)), both exactly for every odd n ≤ 201. As numerical evidence for irrational frames (θ ∈ {1, √2, π/7, e/3} rad; n ∈ {7, 15, 63}; 30 digits; exact enumeration over S_y and S_z), P(W ≤ 0 \| T = 1/(5n)) never exceeds 0.0008 of the bound |
| K2 | The full-record lower bound, recomputed from the per-trial probability of (S_x = n, D = 1), is 3.703827556461·10⁻²², matching the handoff. The probability that the first success has T = 1/(5n) is c_m/C_n |
| K3 | Two-tick freshness of the pair-parity majority rule on the actual cubic geometry (5³ torus). The port's initial pair is fixed and its six neighbours' initial pairs are enumerated (2¹²), with six fixed second-shell patterns. In all 24 cases the port's next two values are exactly i.i.d. fair |
| K4 | Propagation probe for the same rule (exploratory): all 184 patterns of 1 to 3 ones in a 2×2×2 block, with the previous field zero or equal, on a 9³ torus for 8 ticks. Box membership is tested directly: the support leaves the block in none of them. The owner's follow-up proves confinement on a zero background in general; this probe is a finite instance |

## Findings

1. **The all-frame exact-clock witness holds.**
   - The bound is proved and checked exactly.
   - It is extremely loose: the conditional failure probability is about 10⁻³ of the bound for the frames tested.
   - The full-record gap of 3.7·10⁻²² establishes an exact distinction for every frame. It is not a
     finite-precision obstruction, as the handoff states.
2. **The affine obstruction holds.** A fixed linear F₂ wave with affine input encoding and a raw-bit read cannot write
   the crossing predicate a(1 − b): its rectangle XOR is 1, while every affine function's is 0. Nonlinear
   observation maps fall outside this class.
3. **The nonlinear rules split the obligations, as reported.**
   - The cubic quadratic force writes the predicate, but biases the readiness-conditioned source to 9/16.
   - The pair-parity majority force writes the predicate and keeps two-tick freshness. That holds exactly on the
     real geometry (K3).
   - The majority force does not propagate small excitations. The handoff's isolated pulse two-cycles. Here (K4), none
     of 184 patterns of up to three cells leaves its 2×2×2 block within 8 ticks, tested by box membership.
4. **Assumption-watch marker.** Detector logic, source freshness under readiness, and carrier propagation must be
   established under one update and one prior. Each has a working example, but no single rule tested so far
   satisfies all three.

## Relevance to the next target

A candidate interaction or physical observation map must carry the detector predicate, keep the source law under
readiness, and propagate a carrier, all under the same update and prior. Its full joint record must then satisfy the
four identities, or a bounded-error version of them.
