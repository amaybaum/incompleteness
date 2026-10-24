# Memoryless per-slot resets give no depth-uniform complete-record bound

24 October 2026. Author computation under #911. Before any computation, the plan was committed at
`a27e8d8f2e20be50688f881d5ccf3a78b90f399c`, on #911 at `70a8d97f54e4f00e729e9ff73fd94a81852d3dab`; the plan was not
published at that time. The `a2_efficiency_v6/` certificate for the declared menu at total horizon three is
unchanged.

## Result and scope

The executed M=16, W=16, B=24 controller has 1,536 labels. Extend it by its own allocation rule, with one fresh
24-bit block for each further slot. On one in-menu protocol, its complete-record total variation from quantum
theory then tends to 1 with depth. The verdict, generated from the measured values:

    NO_DEPTH_UNIFORM_COMPLETE_RECORD_BOUND_FOR_THIS_EXTENSION:
    1/10 not reached by h=2048; certified TV>1/2 for h>=67382091

The same holds for every controller in the **memoryless reset class**, for every fixed B. In that class:
- after each read, the post-reset carrier is a function only of that slot's fresh block of at most B fair bits and
  the public record;
- responses depend only on the carrier, the public word and the setting;
- the preparation read is unconstrained.

The obstruction comes from resets that carry no randomness across slots. It does not come from bounded per-slot
freshness as such: a reset that also reads retained private seeds escapes it (*The limiting counterexample*).

The result covers this controller's slot extension and the memoryless reset class, on this protocol only. It is
not a bound on:
- total, pooled or retained-seed randomness;
- per-read error;
- continuous resources, such as the renewal in `a1_reset_v6/`;
- OI.

That infinite products of nonidentical Bernoulli laws separate is classical (Kakutani, *Ann. Math.* 49 (1948)
214–224).

## Protocol and exact agreement laws

The protocol: prepare X+, then read a, X, a, X, … for h reads, with no rotations or stops. In quantum theory each
read agrees in sign with the preceding pole with probability 4/5.

| quantity | value |
| --- | --- |
| A (reset at ±a, read X) | 13426743/16777216 |
| B (reset at ±X, read a) | 13424725/16777216 |
| dA = \|A − 4/5\| | 24851/83886080 |
| dB = \|B − 4/5\| | 14761/83886080 |
| retained κ | 6419131/419430400 |

How these were obtained and checked:
- The grid and CDF counts were rebuilt with exact integers, without importing the earlier checker, and they match
  the retained a2 digest.
- Both pole signs were computed directly, and there are no zero responses.
- dA and dB are each at most κ.

Two structural facts:
- A record corresponds one-to-one to its sequence of agreement bits.
- The executed reset ignores retained registers, so the agreements are independent with the alternating parameters
  B, A, B, …. The record law is therefore a product of Bernoulli laws, against Bernoulli(4/5)^h, and T(h) is
  nondecreasing in h.

Where the discrepancy comes from:

| grid | dA | dB |
| --- | --- | --- |
| M=16, W=16 | 24851/83886080 | 14761/83886080 |
| M=16, W=40 | 24511/83886080 | 14431/83886080 |
| M=32, W=16 | 797/10485760 | 1/20480 |

Changing W moves the discrepancy by about 1.4%, while doubling M reduces it about fourfold. The 24-bit dyadic
floor, 1/83886080, is far smaller. For these two reads the discrepancy therefore comes mainly from the M=16 grid.

## Exact total variation

Decimal values are truncated toward zero. The comparisons are exact.

| h | T(h) |
| --- | --- |
| 1 | 14761/83886080 (0.000175964832) |
| 3 | 0.000414941255 |
| 64 | 0.001947297178 |
| 256 | 0.003890566446 |
| 1024 | 0.007778599060 |
| 2048 | 0.010999882464 |

- The values for h = 1–4 are exact rationals, recorded in `result.json`.
- Every tabulated value, h = 1–64 and the powers of two to 2048, is below 1/10, so T(h) ≤ 1/10 for every h ≤ 2048.
- T(3) is below the retained h=3 certificate, 17239332625914280559/230584300921369395200.

## Certified bracket

Let d_t be the per-read discrepancies.
- The squared Hellinger distance per read is at least d_t²/4. This is checked with certified square-root endpoints
  on 1,706 rational pairs, which include the actual reads.
- The Bhattacharyya coefficient of the record law is at most the product, over reads, of the supremum over pasts
  of the per-read coefficient. That is the chain rule, and for the executed extension it holds with equality.
- Since TV ≥ 1 − BC, this gives T(h) ≥ S/(1+S) with S = Σ d_t²/4.
- Maximal coupling gives T(h) ≤ Σ d_t.

Every exact value lies inside this bracket. The lower bound gives these depths, each checked to be minimal:

| level | T(h) exceeds it for every h ≥ |
| --- | --- |
| 1/10 | 7,486,900 |
| 1/2 | 67,382,091 |
| 9/10 | 606,438,812 |

The first exact depth at which T exceeds 1/10 lies between 2049 and 7,486,900; it was not located.

## The memoryless reset class

In the class, every conditional agreement probability after the first read is a multiple of 2^-B. Its distance
from 4/5 is

    dist(4/5, 2^-B Z) = 2^-B · (2/5 if B is odd, 1/5 if B is even).

**Proof.** 4/5 · 2^B = 2^(B+2)/5. Since 4 ≡ −1 (mod 5), 2^(B+2) ≡ ±1 (mod 5) for even B and ±2 (mod 5) for odd B.
The formula is also verified exactly for B = 1–200. It is positive for every B, so by the chain-rule bracket
T(h) → 1 for every fixed B.

At B = 24 the distance is 1/83886080.
- The preparation read is unconstrained, so the class bound certifies T > 1/2 only for h ≥ 28,147,497,671,065,602.
  That is the least h with (h−1)·dist²/4 > 1.
- A nearest-dyadic reset at every read keeps T ≤ 1/10 through h = 8,388,608.

By the bracket, a depth-uniform bound below 1 requires Σ d_t² to be finite, so slot-dependent block sizes B_t must
grow without bound. At sampler level growth suffices: a per-slot nearest-dyadic Bernoulli sampler with
B_t = B0 + 2⌈log2 t⌉ and B0 = 6 has T(h) ≤ 1/80 at every depth. Its enumerated T is 1/320 through h = 12, using 138
fresh bits. These samplers target 4/5 directly and are not geometric controllers. No growing-resource geometric
controller was executed.

By contrast, a fixed B0 = 6 gives:
- T(12) ≈ 0.011050219194;
- T(256) ≈ 0.049751479020;
- T(2048) ≈ 0.139918379698;
- certified T > 1/2 for h ≥ 409,601.

## The limiting counterexample

A reset that also reads retained private seed bits lies outside the class. In it, each slot draws B fresh bits
and decodes over all bits drawn so far. The independent review proposed it; the author's checker re-implements it
and records it here. Its conditional agreement laws are not in 2^-B Z:

| B | P(agree2 \| agree1) | all-depth bound on T(h) |
| --- | --- | --- |
| 2 | 11/16 | 1/2 |
| 3 | 41/56 | 1/6 |
| 4 | 41/52 | 1/14 |

The all-depth bound is the union bound T(h) ≤ Σ_t 2^(t−1)·2^(−tB) ≤ 1/(2^B−2), valid for every h when B ≥ 2.

At B = 4:
- exact T(h) for h = 1–5 is 1/80, 1/80, 1763/128000, 120389/8192000 and 24264001/1638400000;
- T(16) ≈ 0.014825339041.

By contrast, the memoryless 4-bit nearest-dyadic reset, with agreement 13/16 per read, reaches
T(4096) ≈ 0.688595903319.

## Controls

- **Positive control:** a source with exact agreement law 4/5 gives T = 0 through h = 256.
- **Controller record enumeration:** the actual controller's outcome records, from seed counts at the actual
  signed poles and the Born rule, are enumerated for h ≤ 12 (8,190 records) and equal the fast engine. A separate
  enumeration of the product formula is kept and labelled as such.
- **Seeded exhaustion:** on a small grid (M=8, W=10, B=10), all 1,048,576 seed pairs reproduce the per-slot product
  law.
- **Countercontrol, the pooled bank:**
  - a sampler decodes one N = 24h-bit integer by exact adaptive arithmetic coding;
  - its conditional laws are not confined to 2^-24 Z, and its T(h) stays below 2^(h−1−N) for h ≤ 12;
  - it stores the conditional probability and is not a geometric controller.
- **Sign control:** the agreement masses for both pole signs are computed directly and are equal.
- **Constants:** the checker recomputes the certified depths and the bracket constants. Mutating any of them by
  one, or by a factor of 16, fails the checker.

## Departures from the plan

- **Not in the plan:** the controller record enumeration, the Hellinger-constant and minimality checks, the class
  range B ≤ 200, the grid-sensitivity probe and the retained-seed counterexample were added after the independent
  review.
- **Corrected:** the class hypothesis is narrower than the plan's "fresh block of at most B fair bits", which the
  counterexample shows to be insufficient.

## What this does not show

- It covers one protocol without rotations; worst-case depth behaviour over all adaptive policies was not computed.
- It gives no per-read or windowed bound, and no statement about pooled, total, retained-seed or continuous
  resources.
- It says nothing about native OI sourcing, availability or equivalence.

## Replay

From an empty working directory, with the repository root as R:

    python3 -I -B R/verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/a2_depth_v7/checks.py > out.json
    cmp out.json R/verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/a2_depth_v7/result.json

and the same with `-I -B -O`. `SHA256SUMS` lists `PLAN.md`, `REPORT.md`, `checks.py`, `result.json` and
`PROVENANCE.json`.
