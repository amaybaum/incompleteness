# Fixed per-slot fresh blocks give no depth-uniform complete-record bound

24 October 2026. This is an author computation, with no retained review yet. The plan was published before
computation at `a27e8d8f2e20be50688f881d5ccf3a78b90f399c` on #911, whose base is #911 at
`70a8d97f54e4f00e729e9ff73fd94a81852d3dab`. The `a2_efficiency_v6/` certificate, which covers the declared menu
for a total horizon of three operations, is unchanged.

## Result and scope

Take the executed M=16, W=16, B=24 controller (1,536 labels) and extend it by its own allocation rule: one fresh
24-bit block for each further slot. On one in-menu protocol, its complete-record total variation from quantum
theory tends to 1 with depth. The verdict, generated from the measured values:

    NO_DEPTH_UNIFORM_COMPLETE_RECORD_BOUND_FOR_THIS_EXTENSION:
    1/10 not reached by h=2048; certified TV>1/2 for h>=67382091

The same holds for every controller whose resets draw a fresh independent block of at most B fair bits per slot,
for every fixed B.

The result covers:
- this controller's slot extension;
- that per-slot fresh-block class;
- this protocol only.

It is not a bound on:
- total or pooled randomness;
- per-read error;
- continuous resources, such as the renewal in `a1_reset_v6/`, which lies outside the class;
- OI.

That infinite products of nonidentical Bernoulli laws separate is classical (Kakutani, *Ann. Math.* 49 (1948)
214–224); no novelty is claimed for it.

## The protocol and the exact agreement laws

The protocol is: prepare X+, then read a, X, a, X, … for h reads, with no rotations or stops. In quantum theory
each read agrees in sign with the preceding pole with probability 4/5.

Rebuilt with exact integers, without importing the earlier checker, the controller gives:

| quantity | value |
| --- | --- |
| A (reset at ±a, read X) | 13426743/16777216 |
| B (reset at ±X, read a) | 13424725/16777216 |
| dA = \|A − 4/5\| | 24851/83886080 |
| dB = \|B − 4/5\| | 14761/83886080 |
| retained κ | 6419131/419430400 |

- Both pole signs were computed directly, not assumed, and there are no zero responses.
- dA and dB are both at most κ.
- The rebuilt CDF counts match the retained a2 digest.

A record corresponds one-to-one to its sequence of agreement bits. Fresh resets make the agreements independent,
so the record law is a product of Bernoulli laws with parameters B, A, B, …, compared with Bernoulli(4/5)^h.
Total variation T(h) is nondecreasing in h.

## Exact total variation

| h | T(h) (rounded display) |
| --- | --- |
| 1 | 14761/83886080 ≈ 0.000175964832 |
| 3 | ≈ 0.000414941255 |
| 64 | ≈ 0.001947297178 |
| 256 | ≈ 0.003890566446 |
| 1024 | ≈ 0.007778599060 |
| 2048 | ≈ 0.010999882464 |

- The values for h = 1–4 are exact rationals, recorded in `result.json`.
- Every tabulated value, h = 1–64 and the powers of two to 2048, is below 1/10, so T(h) ≤ 1/10 for every h ≤ 2048.
- T(3) is below the retained h=3 certificate 17239332625914280559/230584300921369395200.
- Decimal displays are readability aids; the comparisons are exact.

## Certified bracket at every depth

With per-read discrepancies d_t:
- the squared Hellinger distance per read is at least d_t²/4;
- the Bhattacharyya coefficient multiplies over the independent reads;
- so T(h) ≥ S/(1+S), with S = Σ d_t²/4;
- maximal coupling gives T(h) ≤ Σ d_t.

Every exact value lies inside this bracket. The lower bound gives:

| level | T(h) exceeds it for every h ≥ |
| --- | --- |
| 1/10 | 7,486,900 |
| 1/2 | 67,382,091 |
| 9/10 | 606,438,812 |

The first exact depth at which T exceeds 1/10 lies between 2049 and 7,486,900; it was not located.

## The class

In the class, every conditional agreement probability after the first read is a multiple of 2^-B. Its distance
from 4/5 is

    dist(4/5, 2^-B Z) = 2^-B · (2/5 if B is odd, 1/5 if B is even),

verified exactly for B = 1–64. It is positive for every B, so T(h) → 1 for every fixed B.

At B = 24 the distance is 1/83886080. The class bound alone certifies T > 1/2 only for
h ≥ 28,147,497,671,065,601, and a best 24-bit per-slot sampler keeps T ≤ 1/10 through h = 8,388,608. The executed
controller's larger discrepancy comes mainly from its M=16 grid.

By the bracket, a depth-uniform bound below 1 requires Σ d_t² to be finite, so slot-dependent block sizes B_t
must grow without bound.

**Growth is sufficient at sampler level.** A per-slot nearest-dyadic Bernoulli sampler with
B_t = B0 + 2⌈log2 t⌉ and B0 = 6 has T(h) ≤ 1/80 at every depth; its enumerated T is 1/320 through h = 12, using
138 fresh bits. These samplers target 4/5 directly and are not geometric controllers; a growing-resource geometric
controller was not executed. By contrast, a fixed B0 = 6 gives:
- T(12) ≈ 0.011050219194;
- T(256) ≈ 0.049751479020;
- T(2048) ≈ 0.139918379698;
- certified T > 1/2 for h ≥ 409,601.

## Controls

- **Positive control:** a source with exact agreement law 4/5 gives T = 0 through h = 256.
- **Engine cross-checks:** a brute-force enumeration of 8,190 records of the seeded controller (h ≤ 12) agrees with
  the closed-form count. Seeded exhaustion on a small grid (M=8, W=10, B=10) covers all 1,048,576 seed pairs and
  reproduces the per-slot product law.
- **Countercontrol, the pooled bank:**
  - A sampler decodes one N = 24h-bit integer by exact adaptive arithmetic coding of the quantum conditional law.
  - Its conditional laws are not confined to 2^-24 Z, and its T(h) stays below 2^(h−1−N) for h ≤ 12.
  - So the obstruction comes from bounded per-slot freshness, not from total randomness. This sampler stores the
    conditional probability and is not a geometric controller.
- **Sign control:** the agreement masses for both pole signs were computed directly and are equal.

## What this does not show

- It covers one protocol without rotations. Worst-case depth behaviour over all adaptive policies was not
  computed.
- It gives no per-read or windowed error bound, and no statement about pooled, total or continuous resources.
- It makes no statement about native OI sourcing, availability or equivalence.

## Replay

    python3 -I -B checks.py > out.json && cmp out.json result.json
    python3 -I -B -O checks.py > out.json && cmp out.json result.json

Run from an empty working directory. `SHA256SUMS` lists `PLAN.md`, `REPORT.md`, `checks.py`, `result.json` and
`PROVENANCE.json`.
