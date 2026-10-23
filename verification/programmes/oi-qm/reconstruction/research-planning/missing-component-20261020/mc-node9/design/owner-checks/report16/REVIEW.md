# Coordinator review: rule-census and stopping-readiness handoffs v1

> **DRAFT — research record.** The owner's read-only session produced these two exploratory results. They are
> recorded here with the coordinator's verification and independent checks. Neither adopts a rule, a readiness
> event or a readiness interface as an OI premise, and neither reopens the C-SPH-1 checkpoint.

## Verification

- **Transfer bundle.** `OI_report16_transfer_bundle.zip` (sha256
  `ece7979ec158e785714ee368acdf364f10f04cf09d8234b0fbaa34db4f8c47ef`) carries the two archives unchanged. Its
  `SHA256SUMS` verifies, and the bundle adds no research content.
- **Archives.**
  - `OI_rule_census_handoff_v1.zip` has sha256
    `8705f2b267734cd3baf81a6d05d791106364a940979df9bbf43878ef81feeead`. This is the archive the joint-readiness
    handoff (report15) cites as its predecessor.
  - `OI_stopping_readiness_handoff_v1.zip` has sha256
    `50618b634a81193a792d89a405bf577f94b39ebb6fa68a63d56cf728db07eca6`.
  - Both match their stated hashes. The files in `handoff/rule-census/` and `handoff/stopping-readiness/` are their
    contents, unchanged, and each `SHA256SUMS` verifies.
- **Code review before running.**
  - `rule_census_checks.py` and `stopping_checks.py` use only the standard library and write only to stdout.
    `stopping_checks.py` uses a seeded pseudo-random generator.
  - `exhaustive.cpp` uses only the C++ standard library and writes only to stdout.
- **Replay.**
  - Both Python checkers were run from a separate directory with `python3 -I`, normally and with `-O`. In all four
    runs the output is byte-identical to the included `.out`.
  - `exhaustive.cpp`, compiled with `g++ -O2 -std=c++17`, reproduces `exhaustive.out` byte for byte.

## Independent checks (`coordinator_stopping_checks.py`; separate code, numpy)

| Check | Result |
|---|---|
| P1 | **Rule census, own derivation.** The checks rebuild the 48 signed permutations and their 10 orbits on the 64 neighbour patterns, then all 1024 invariant rules. The three conditions (quiescent background, pulse response, balanced truth table) leave 6 rules. Their three-tick port laws were computed by vectorized enumeration of all 2^24 reduced-cone assignments. Only XOR has TV 0, and the smallest nonlinear TV is 441/524288. All six laws match the handoff's table |
| P2 | **Census reduction against the actual dynamics** (statistical evidence). Monte Carlo on a 9³ torus with 200000 uniform phases per rule and the port pair zero. XOR's (h1,h2,h3) has chi-square 9.8 on 7 dof. For the most biased nonlinear rule, P(h1=0,h3=0) is 0.22946 against an exact 0.22817, and P(h1=1,h3=0) is 0.27827 against an exact 0.27916 (z = 1.37 and −0.88) |
| S1 | **Stopping theorem, exact, separate rows.** Each readiness constraint's row over the initial wave bits was built by evolving delta initial data, using the symmetry of S, field by field. Across all six geometries and all 48 readiness intersections, the payload and the K future source triples raise the rank by exactly 2 + 3K. The receiver identities lie in the span of E_w. The K = 3, L = 25 intersection ranks are 268, 385, 442 and 502, as stated |
| S2 | **Stopping theorem, raw rule, no linear-wave coordinates.** K = 3, L = 25, with 3072 states per w ∈ {0, 1, 2}. Uniform raw states satisfying the raw readiness predicate at tick w were run backwards with the explicit inverse of the raw rule, and earlier-tick readiness was tested. Running forwards again reproduces the tick-w state exactly. The receiver reads (0,0,0), (0,0,0), (a,b,ab) in every run. Payload, per-tick source and payload × first-triple frequencies are consistent with uniform (chi-square tests). No sampled state was ready at an earlier tick, as expected at P(E_i \| E_w) ≤ 2^−117 |
| S3 | **The stopped law against the fixed-start law, exact.** TV(law \| W = w, law \| E_w) = 1 − P(W = w)/P(E_w). This is 2^−117 for w = 1 and 2^−117 + 2^−174 − 2^−234 for w = 2 |
| S4 | **First hit against return.** Over 80 random permutations of up to 3000 states, with random events: the Kac gap sum is \|Sat(E)\|, the uniform-start mean first hit on Sat(E) is Σℓ(ℓ−1)/(2\|Sat(E)\|), and the deadline union bound holds |

Before receiving the archive, the coordinator also checked the following from the owner's message alone:
- The fixed point. A = 1 everywhere with B = D = 0 maps to itself, because S of all ones is zero.
- The entropy bound. The deficit (1 − δ)J − h₂(δ) − δ·log₂(1 − 2^−J) follows from bounding the entropy within and
  outside E by the logarithm of each set's size.

## Findings

1. **The census holds as stated (CONFIRMING).**
   - In the binary scalar, cubic-invariant, center-free nearest-neighbor second-order class, the three requirements
     select XOR.
   - Every nonlinear survivor has an AND slice, so their failure is a freshness failure.
   - The three-field "escape" at the end of the census is the original detector rule. Report15 records why that rule
     cannot be reused as a gate, and records the repaired rule that replaced it.
2. **The stopping-time law holds (CONFIRMING).**
   - The setting is a waiting cap B < K in the original geometry, or any finite cap in the enlarged geometry, with
     ideal passive readiness flags. Conditional on first success at W = w, the payloads are fair, the next K raw
     source triples are uniform and independent, and the receiver reads silence and then (a, b, ab).
   - The flags of all earlier failures are included in this conditioning.
   - S1 and S2 check this by separate code paths.
3. **Under the uniform prior the theorem is exact but nearly free; its real use is for prepared priors
   (ELABORATING).**
   - Conditioning on W = w rather than on E_w changes every law by at most 2^−117 in total variation at K = 3 (S3),
     so the fixed-start law of report15 already gave the stopped law to that accuracy.
   - The exact statement matters where readiness is likely, which under a uniform prior it is not.
   - Read as written, the proof uses only the following, which is the coordinator's reading and is not separately
     checked:
     - W = w depends only on unreserved bits;
     - the reserved 2 + 3K frontier bits are fair and independent of those unreserved bits;
     - given the unreserved bits, the outputs are bijective in the reserved bits.
   - It therefore extends to any initial law under which, for each w ≤ B, that w's reserved frontier bits are fair
     and independent of the rest.
   - **Assumption-watch marker.** A native preparation must hold an entropy deficit of at least about J bits. It
     preserves this freshness if it leaves the reserved frontier bits fair and independent of everything it
     prepares.
4. **Waiting and resources (CONFIRMING; corrects the coordinator's earlier remark).**
   - The Kac return mean bounds the return time to E, not the first-hit time from a uniform start.
   - In this rule the uniform-start mean first-hit time is infinite, because some states never become ready.
   - The robust statement is the deadline bound P(W ≤ B) ≤ (B + 1)·2^−J.
   - The entropy deficit is an information-resource bound. Reading it as heat requires thermodynamic assumptions that
     have not been supplied.
5. **Scope.** The following are supplied rather than constructed:
   - the readiness check, which is an ideal, passive, non-local test of J bits whose only record is its flag;
   - its latency, clock, backreaction and any extra records it would leave;
   - payload injection;
   - a practical source of ready resources.

   The proof does not cover records that reveal a reserved frontier bit, or an uncapped waiting history.

## Relevance to the next target

The next construction is a bounded-latency local readiness flag and clock under the specified rule. It needs:
- an explicit initial resource state, entered in the entropy budget;
- the joint law of readiness, waiting time, failures, source symbols and every extra record.

Finding 3 gives a concrete design test: the construction keeps the stopped law exactly if its resources and records
leave the reserved frontier bits fair and independent. Angular-law selection remains a separate obligation. No
station-indexed preparations are defined, so the four record identities can be neither claimed nor tested here. The
C-SPH-1 checkpoint stays closed.
