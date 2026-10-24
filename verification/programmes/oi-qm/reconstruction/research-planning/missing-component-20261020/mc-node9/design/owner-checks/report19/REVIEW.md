# Coordinator review: aggregation-components handoff v1

> **DRAFT — research record.** The owner's read-only session produced these three finite components under the
> report18 rule. They are recorded here with the coordinator's verification and independent checks. They are not a
> scalable construction, and the rule remains an engineered candidate that OI has not selected.

## Verification

- **Archive.** The archive's sha256 is `1b32e2b6a304bb366265ca13ffad9a66a6e95380daa30c2c9c38a2b12bf1fa50`, as
  stated. The files in `handoff/` are its contents, unchanged. Their `SHA256SUMS` verifies.
- **Code review before running.** `aggregation_checks.py` uses only the standard library, reads the `RECORDS.json`
  beside it as data, uses seeded pseudo-random generators, and writes only to stdout.
- **Replay.** Run from a separate directory with `python3 -I`, normally and with `-O`, the output is byte-identical
  to `aggregation_checks.out`.

## Review criteria, stated before the handoff arrived

The coordinator stated these criteria in advance:
- check all 2ⁿ inputs on dense full-torus backgrounds, and measure the output's degree directly;
- account for every register the circuit writes;
- recount the readiness from its definition;
- check source freshness while the circuit runs;
- treat the result as scalable only if a general rule for building the circuit is stated and holds at sizes beyond
  those tested.

## Independent checks (`coordinator_aggregation_checks.py`; separate code, numpy)

The layouts are transcribed from the handoff's `REPORT.md` table, not from its checker. `RECORDS.json` is evaluated by
a separate polynomial evaluator.

| Check | Result |
|---|---|
| H1 | **Each layout on the full torus** (L = 6T + 3), with two new dense backgrounds and all 2ⁿ inputs, for n = 4, 5, 6. The complete device record (all three fields on B_2T, ticks −1 to T) equals the published polynomials. The receiver's D register is ANDₙ, with algebraic degree n measured by a Möbius transform. Every write that varies with the input at tick t lies within B_(T+t) |
| H2 | **The joint law by Cartesian product**, which the handoff establishes by a disjoint-cone argument rather than enumeration. For n = 4 (16 inputs × 512 frontier assignments) and n = 5 (32 inputs × 4096), every input runs with every reserved-frontier assignment on the full torus, with a dense background. The frontier runs along −y from q, whereas the handoff uses +x. The output is correct in every run. For each input the source words are all distinct, and they form the same set for every input |
| H3 | **Readiness recount.** n = 4: 5977 zero pins + 1 copy equality = 5978. n = 5: 14015 + 2 = 14017. n = 6: 27237 + 3 = 27240. Every input and copy slot lies inside the receiver's cone |
| H4 | **Probe: the readiness the output register alone needs** (source pins excluded). By causality, pinning the receiver's own initial cone suffices: 260, 571 and 1074 constraints for n = 4, 5, 6, including the copies. That compares with 5972, 14011 and 27234 in the full-record buffer. Within that cone, 144, 289 and 476 pins each break the output when released to 1 alone, with every other pin at zero. That is a sensitivity count, not a lower bound, because the rule is nonlinear |

## Findings

1. **The three components hold (CONFIRMING).**
   - Under the unchanged report18 rule, AND4, AND5 and AND6 are written into one raw D register by ticks 3, 4 and 5.
     Their degrees are exactly 4, 5 and 6.
   - The complete device record matches the published tables on new dense backgrounds.
   - Every input-caused write stays inside the recorded region.
   - The source word is uniform and independent of the inputs and of the device record. At n = 4 and 5 this is now
     also established by the full Cartesian product.
2. **The cost table measures the record interface, not the computation (ELABORATING).**
   - The constraint counts in the handoff (5978, 14017, 27240) buy a deterministic record over all of B_2T. They grow
     roughly as 216T³.
   - The output register alone needs at most 260, 571 and 1074 constraints. These grow roughly as 8T³, about 23 to 25
     times fewer.
   - Which record must be deterministic is an interface choice. The resource budget (checklist entry 3) depends on
     that choice as much as on the gate.
   - This sharpens the handoff's own statement that its counts are conservative buffer costs, not minimal gate costs.
3. **Scaling is not established (by the stated criterion).**
   - There is no general layout rule, composition lemma or prediction for an untested size.
   - Latency T = n − 1 holds for the three layouts and is not claimed beyond them.
   - These are finite components.
   - The handoff also reports that a restricted search found no seven-input continuation. That is neither exhaustive
     nor an obstruction.
4. **Scope.** The following remain supplied:
   - the rule and its internal field order;
   - the readiness event, including its affine copies;
   - the preloaded inputs;
   - the tick as time.

   The devices are one-shot: nothing is restored, and they retain information. The receiver's other registers expose
   side terms; the n = 4 device's B register, for example, reads abc ⊕ cd.

## Relevance to the next target

The next target is a composition lemma: how to extend a circuit stage by stage while controlling copies, side signals,
latency and workspace. It must also predict a size not used to find it. Finding 2 suggests stating separately which
part of the record a composed circuit keeps deterministic, since that choice dominates its readiness cost.
Native preparation, a clock and angular-law selection remain separate obligations. The conditions checklist is
unchanged: this result adds support to its logic entry without changing any requirement, obstruction or sufficient
method. The C-SPH-1 checkpoint stays closed.
