# Coordinator review: emission-map handoff v1

> **DRAFT — research record.** The owner's read-only session produced this exploratory candidate diagnostic. It is
> recorded here with the coordinator's verification and independent checks. It is not a C-SPH-1 rerun or an
> acceptance test.

## Verification

- **Archive.** The archive's sha256 is `70582b6b154509329186c1277e70427952c878504ba2f601f6d49988a3d541a5`, as
  stated. The files in `handoff/` are its contents, unchanged. Their `SHA256SUMS` verifies.
- **Code review before running.** `emission_map_checks.py` uses only the standard library, writes no files and makes
  no network calls.
- **Replay.** Run from a separate directory, normally and with `-O`, the output is byte-identical to
  `emission_map_checks.out`.

## Independent checks (`coordinator_emission_checks.py`; separate code)

| Check | Result |
|---|---|
| E1 | At n = 63, M = 1024 and m = 256, every timestamp D/P is reduced by a gcd rather than the closed-form count. Completion is 0.981776369544 (X) and 0.981543683592 (R). The full-record event has probability 0.819346363181 (X) and 0.164250679444 (R). The gap is 0.655095683737, and the comparison > 1/2 is exact. Matches the handoff |
| E2 | n = 3, enumerating all three components. For X-mix and R-mix, every menu read (X, Y, Z, R) is exactly unbiased conditional on each exact timestamp. **Positive control:** X-mix and Y-mix have identical (success, timestamp, read along a) laws for every a. X-mix and R-mix single-trial timestamp laws differ: TV 9/128 |
| E3 | The 16-bin herald record (attempt index and bin, or all-fail), with bins computed as ⌈16D/P⌉ for every depth. TV is 0.015685376945976, matching the handoff |
| E4 | Probe: the attempt-index-only record (see finding 2) |

## Findings

### 1. The handoff's computations and the mixture claim hold

The full-record witness is exact. Both mixtures give unbiased menu reads conditional on the herald record, while the
herald timestamps distinguish them. The X-versus-Y control shows that the event does not fire between preparations
whose arithmetic is the same up to symmetry.

### 2. The number of trials leaks the preparation at finite n (NEW, small)

**Measured (E4).** With the attempt index as the only record, and m = 256:

| n | p_X | p_R | TV |
|---|---|---|---|
| 7 | 0.085449 | 0.082859 | 1.18·10⁻² |
| 15 | 0.030684 | 0.030275 | 5.02·10⁻³ |
| 31 | 0.021867 | 0.021728 | 2.38·10⁻³ |
| 63 | 0.015523 | 0.015474 | 1.17·10⁻³ |
| 127 | 0.010998 | 0.010981 | 5.78·10⁻⁴ |

**Why it happens.**
- The per-trial success probability p_w = E[(5w·S)₊]/M depends on the station axis w at finite n, because the law
  of the bit average S is not rotation-invariant.
- The waiting-count distribution therefore separates X-mix from R-mix without any timestamp.
- The distance roughly halves as n doubles, consistent with an O(1/n) rate anisotropy. That rate is observed, not
  proved.
- As a coarsening of the 16-bin record, it is consistently below that record's TV (0.0157 at n = 63).

**Consequence for the handoff's continuous-depth variant.**
- A continuous uniform depth makes the timestamp uniform given success. That removes the arithmetic witness, but
  not this leak.
- The herald-record distance is then exactly the attempt-only distance.

**Assumption-watch marker.** A herald's success rate must itself be station-independent. Angular convergence of the
emitted direction does not imply it. In C-SPH-1 it held by isotropy of the continuum reservoir; a finite native
source must establish it, or account for it as an error term.

### 3. The handoff's limits are confirmed

The following are supplied, not derived:
- the averaging-to-velocity identification;
- ballistic motion;
- a real-valued crossing clock;
- a full-plane crossing rule, with no aperture or collector;
- backreaction;
- reset and routing;
- access protection;
- a preparation factory;
- the energy-shell prior;
- composites.

The angular result is a weak limit. Convergence is checked on fixed hemisphere tests; it is neither total-variation
convergence of the direction law nor a full-record convergence theorem.

## Relevance to the next target

The handoff's obligation stands: derive the native clock, emission and detector registers together, then analyse the
joint angular, timing and rate law of the accessible record. Finding 2 adds a requirement to that obligation: the
derived record must also control success-rate anisotropy, which coarsening the time alone does not remove.
