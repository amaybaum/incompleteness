# Coordinator review: joint-readiness and carrier-compatibility handoffs v1

> **DRAFT — research record.** The owner's read-only session produced these two exploratory constructions. They are
> recorded here with the coordinator's verification and independent checks. Neither adopts a rule or a readiness
> event as an OI premise, and neither reopens the C-SPH-1 checkpoint.

## Verification

- **Archives.**
  - `OI_joint_readiness_handoff_v1.zip` has sha256
    `72ab080972b8124a575ada927f16a452c084f0c02abd9a7964499e0ccb04b576`, as stated.
  - `OI_carrier_compatibility_handoff_v1.zip` has sha256
    `14a2242c5ff83df4b2e39790f4fea985ac41e06ca31ffaf3fab14851ea069e36`, as stated.
  - The files in `handoff/joint-readiness/` and `handoff/carrier-compatibility/` are their contents, unchanged. Each
    `SHA256SUMS` verifies.
- **Code review before running.** `joint_readiness_checks.py` and `carrier_checks.py` use only the standard library,
  write only to stdout, and use no randomness.
- **Replay.** Each checker was run from a separate directory with `python3 -I`, normally and with `-O`. In all four
  runs the output is byte-identical to the included `.out`.
- **Provenance.** The joint-readiness handoff continues `OI_rule_census_handoff_v1.zip` (sha256
  `8705f2b267734cd3baf81a6d05d791106364a940979df9bbf43878ef81feeead`), recorded and reviewed in report16. Both
  archives here restate the update rules they use, and both checkers are self-contained.

## The handoffs' corrections to report14: applied

1. **K4** measured L1 distance from the origin, which does not establish block membership. For example, (−1,0,0)
   has distance 1 but lies outside the block.
   - Report14's K4 was changed to test membership directly at `3de4cf50` in response to the same observation.
   - The carrier handoff adds a proof that applies at every tick: on a zero background, the support of the
     pair-parity majority rule never leaves a Cartesian box. The proof also covers a product of coordinate subsets
     on a torus. N4 below tests this.
2. **K1 wording.** The saved output gives a largest ratio of 0.0008206, so the table now says "about 0.00082 of the
   bound (largest ratio 0.0008206)".
3. **Report14 finding 4** said that no single rule tested so far satisfies all three obligations. It is now restated
   in place, with a reference to this report.

## Independent checks (`coordinator_carrier_checks.py`; separate code, numpy)

| Check | Result |
|---|---|
| N1 | The repaired three-field rule was implemented directly on random tori of sizes 7³, 6×5×4 and 9×8×10, with 2304 transitions. At every transition, C = D ⊕ AB satisfies C′ = SC ⊕ C_old, and the explicit inverse (current, next) → previous recovers the previous slice |
| N2 | The carrier construction for K = 2, 3, 4. Every bit outside E_K is random: both time slices, all three fields, the whole torus. This is stronger than the handoff's zero-remainder slice. In all 480 runs the receiver record is silent before tick K and reads (a, b, ab) at tick K. **Countercontrols:** freeing the current A bit at (0,0,K), which has one shortest path to the receiver, moves 85, 69 and 79 of 160 runs off the record (K = 2, 3, 4). The original detector rule misses the terminal product in all 40 runs per K with a = b = 1 |
| N3 | Source freshness under random backgrounds, for K = 2 and 3 and all four payloads, with four backgrounds each. The frontier is the current A, B and D bits at q + t·e_y for t = 1..K, which differs from the handoff's frontier. In all 32 cases, the 8^K frontier assignments give 8^K distinct raw source words, and the receiver record does not change |
| N4 | Box invariance of the majority rule on a 12³ torus over 30 ticks. There are 400 random two-slice patterns: half inside random boxes up to 5³, and half inside random products of coordinate subsets. The support never leaves the set |
| N5 | Probe (exploratory): a one-site flip under the majority rule on a uniformly random background (21³ torus, 20 backgrounds). The difference reaches L1 distance t at tick t, for every t ≤ 8, in every background |
| N6 | The joint-readiness tick-2 defect of the original rule under E_blank. The raw AND error Z₂ ⊕ H₂M₂ was computed in a new way: the rule was simulated with one free A bit and one free B bit at a time, over 119 + 119 free bits in a radius-3 ball. Bilinearity holds on 200 random pairs. The error form has F₂ rank 12, so the error probability is 4095/8192, matching the handoff |
| N7 | For the original rule, the coefficient of F_tG_t in Z_t is 1, 0, 1, 0, 1, 0, 1, 0 for t = 1..8, i.e. t mod 2, matching the handoff |

N2 and N3 sample their backgrounds pseudo-randomly with a fixed seed. They are finite tests of the implementation
and are no substitute for the handoff's proofs. The output is deterministic and reproduces byte for byte.

## Findings

1. **The original detector rule cannot be reused as a gate, as reported (CONFIRMING).**
   - The second raw AND write has error 1/2 under local readiness. Under a fully blank detector the error is
     4095/8192, which N6 reproduces with an independent rank computation.
   - The frontier coefficient alternates with t mod 2 (N7). This forces raw-AND error of at least 1/4 at every even
     tick.
2. **The repaired rule is three linear waves in disguise (CONFIRMING).**
   - The coordinate change C = D ⊕ AB conjugates it to three independent linear waves, which makes it invertible
     (N1).
   - Its clean condition C = 0 keeps D = AB at every site and every tick.
   - The same construction works for all 16 two-input Boolean functions. The update and the readiness correlation
     therefore supply the predicate; nothing selects AND, still less the projected-area law.
3. **The carrier construction holds beyond the handoff's slice (POSITIVE).**
   - One update and one readiness-conditioned prior support three things at once:
     - transport of two preloaded bits;
     - the raw product at the meeting tick;
     - a source port whose raw triples are fresh and independent of the payload and of the receiver.
   - N2 and N3 check this against full random backgrounds.
   - This conditionally closes report14's assumption-watch marker, at the level of binary signals in an engineered
     apparatus.
4. **What stays supplied.** All of the following are supplied rather than derived:
   - the update itself;
   - the readiness event, with probability 2^−268 at K = 3 for E_K, and 2^−(2L³+4) for E_product in the
     joint-readiness repair;
   - the preloaded payloads, with no injection mechanism;
   - the meaning of the tick as a time;
   - the passive call interface.

   The uniform-flip argument shows that flipping a free bit of a uniform background transmits nothing: TV = 0. A
   spreading disturbance is therefore not information transport.
5. **Two observations (ELABORATING; exploratory).**
   - **The majority rule's confinement depends on a zero background.** On a uniformly random background, a one-site
     flip spreads at the maximum speed (N5). This bears on the majority rule only through the handoff's own argument:
     a spreading difference is not a transported signal.
   - **Not every readiness bit carries the tick-K record.** A free bit at distance K reaches the receiver at tick K
     with coefficient equal to the number of shortest paths mod 2. Bits whose path count is even therefore do not
     affect the tick-K record; the first countercontrol site tried, (0, K−1, 1), changed no run at K = 2 or 4. J_K is
     the cost of the event as stated, not a minimum for this record. That minimum has not been computed.

## Relevance to the next target

These handoffs separate three things: source freshness, repeated gate computation, and physical law selection. The
first two are now compatible under one engineered rule and one readiness-conditioned prior. The third remains open.

The remaining targets are:
- a physical reason for the emission and readout law;
- native preparation of the ready correlations, with a native clock and the failure records both leave;
- a specified angular emission and readout map with its full accessible record;
- station-indexed preparations, so that the four record identities can be tested;
- composites.

No station-indexed quantum preparations are defined in either construction, so the four identities can be neither
claimed nor tested here. The C-SPH-1 checkpoint stays closed.
