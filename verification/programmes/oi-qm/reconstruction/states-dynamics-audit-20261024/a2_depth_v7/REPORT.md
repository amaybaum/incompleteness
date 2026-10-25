# Memoryless per-slot resets give no depth-uniform complete-record bound

24 October 2026. Author computation under #911. The plan was committed at
`a27e8d8f2e20be50688f881d5ccf3a78b90f399c` (15:17:55 UTC), a child of #911's head
`70a8d97f54e4f00e729e9ff73fd94a81852d3dab`, before the execution commit `1949a902` (15:25:15 UTC). The `a2_efficiency_v6/` certificate for the declared menu at total horizon three is
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
- responses depend only on the carrier, the public word and the setting. The public word is a function of the
  public record: in `a2_efficiency_v6/` it is the rotation word applied since the last read;
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
- The extension verdict rests on three specifics of the executed controller:
  - its reset is memoryless, ignoring retained registers, as `a2_efficiency_v6/` specifies;
  - the agreement masses are equal for both pole signs (A± and B±), computed directly;
  - records correspond one-to-one to agreement-bit sequences.

  So the agreements are independent with the alternating parameters B, A, B, …, and the record law is a product of
  Bernoulli laws, against Bernoulli(4/5)^h. T(h) is nondecreasing in h.

Where the discrepancy comes from:

| grid | dA | dB |
| --- | --- | --- |
| M=16, W=16 | 24851/83886080 | 14761/83886080 |
| M=16, W=40 | 24511/83886080 | 14431/83886080 |
| M=32, W=16 | 797/10485760 | 1/20480 |

At B = 24, for these two reads only:
- changing W from 16 to 40 at M = 16 moves dA by 340/24851 (about 1.37%) and dB by 330/14761 (about 2.24%);
- changing M from 16 to 32 at W = 16 divides dA by about 3.90 and dB by about 3.60.

The 24-bit dyadic floor, 1/83886080, is far smaller. For these two reads the discrepancy therefore comes mainly from
the M=16 grid. These are single parameter steps of this implementation, not a scaling law.

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
All four steps below concern the joint law of the whole h-read record.

- **Per-read Hellinger bound.** For Bernoulli laws p and q, 2H² = (√p − √q)² + (√(1−p) − √(1−q))². Since
  |p − q| = |√p − √q|·(√p + √q) ≤ 2|√p − √q|, and likewise for 1 − p and 1 − q, H² ≥ (p − q)²/4 = d²/4. The
  checker also checks it with certified square-root endpoints on 1,706 rational pairs, which include the actual
  reads.
- **Chain rule.** For any controller, adaptive or not, BC_h = Σ_past √(P·Q)·BC_t(past) ≤ BC_{h−1} · sup_past BC_t,
  so BC_h ≤ Π_t sup_past BC_t = Π_t (1 − c_t), with c_t ≥ inf_past d_t²/4. For the executed extension the product
  holds with equality.
- **Lower bound.** TV ≥ 1 − BC, and 1 − Π(1 − c_t) ≥ 1 − e^(−S) ≥ S/(1+S), with S = Σ_t c_t ≥ Σ_t inf_past d_t²/4.
  For the executed extension the per-read laws do not depend on the past, and S ≥ Σ_t d_t²/4, the value the depth table uses.
- **Upper bound.** Maximal coupling gives T(h) ≤ Σ_t sup_past d_t, which is Σ d_t for the product law.

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
So 2^(B+2)/5 lies 1/5 or 2/5 from the nearest integer, and dividing by 2^B gives the formula. It is also checked
exactly for B = 1–300.

The distance is positive for every B. Every conditional agreement probability after the first read is a multiple of
2^-B, and with the Hellinger bound and the chain rule above, S grows at least linearly in h. So T(h) → 1 for every
fixed B and every controller in the class.

At B = 24 the distance is 1/83886080.
- The preparation read is unconstrained, so the S/(1+S) rule certifies T > 1/2 for h ≥ 28,147,497,671,065,602,
  the least h with (h−1)·dist²/4 > 1.
- A nearest-dyadic reset at every read keeps T ≤ 1/10 through h = 8,388,608.

By the bracket, a depth-uniform bound below 1 requires Σ d_t² to be finite, so slot-dependent block sizes B_t must
grow without bound. At sampler level growth suffices: a per-slot nearest-dyadic Bernoulli sampler with
B_t = B0 + 2⌈log2 t⌉ and B0 = 6 has T(h) ≤ 1/80 at every depth: by maximal coupling, T ≤ Σ_t d_t ≤ (2/5)·2^(−B0)·Σ_t 4^(−⌈log2 t⌉) = (3/5)·2^(−B0) = 3/320. Its enumerated T is 1/320 through h = 12, using 138
fresh bits. These samplers target 4/5 directly and are not geometric controllers. No growing-resource geometric
controller was executed.

By contrast, a fixed B0 = 6 gives:
- T(12) ≈ 0.011050219194;
- T(256) ≈ 0.049751479020;
- T(2048) ≈ 0.139918379698;
- certified T > 1/2 for h ≥ 409,601.

## The limiting counterexample

A reset that also reads retained private seed bits lies outside the class. In it, each slot draws B fresh bits
and decodes over all bits drawn so far. It is a protocol-specific sampler that reads the quantum cuts, not a
geometric controller, and it escapes the obstruction on this protocol only. Its initial seed state is empty: no
bits are retained before read 1, and read 1 uses the cut at 4/5 and B fresh bits. Its conditional agreement laws are
not in 2^-B Z:

| B | P(agree2 \| agree1) | all-depth bound on T(h) |
| --- | --- | --- |
| 2 | 11/16 | 1/2 |
| 3 | 41/56 | 1/6 |
| 4 | 41/52 | 1/14 |

**The bound holds at every depth, for the joint record law.** Couple both laws through one uniform U, the seed
being U's leading bits.
- While the two records agree, they use the same cut.
- At read t, the read-1 preparation included, they can first differ only if one of the 2^(t−1) depth-t cuts falls
  inside U's tB-bit cell. That has probability at most 2^(t−1)·2^(−tB).
- Summing gives T(h) ≤ Σ_t 2^(t−1)·2^(−tB) = 2^(−B)/(1 − 2^(1−B)) = 1/(2^B − 2), for every h, when B ≥ 2.

The checker derives each label from this series. It checks exactly that T(h) ≤ the coupling gap ≤ the partial sum
< 1/(2^B − 2) for B = 2 (h ≤ 8), B = 3 (h ≤ 6) and B = 4 (h ≤ 5, and h = 8, 12, 16).

At B = 4:
- exact T(h) for h = 1–5 is 1/80, 1/80, 1763/128000, 120389/8192000 and 24264001/1638400000;
- T(16) ≈ 0.014825339041.

By contrast, the memoryless 4-bit nearest-dyadic reset, with agreement 13/16 per read, reaches
T(4096) ≈ 0.688595903319.

## Controls

- **Positive control:** a source with exact agreement law 4/5 gives T = 0 through h = 256.
- **Controller record enumeration** (it replaces the plan's seeded enumeration for h ≤ 12):
  - the actual controller's outcome records are enumerated for h ≤ 12 (8,190 records), from seed counts at the
    actual signed poles, and equal the fast engine;
  - each record's quantum mass is checked against an independent engine of rational 2×2 density matrices with
    sequential projections, which does no pole bookkeeping, so wrong pole propagation is detected;
  - a separate enumeration of the product formula is kept and labelled as such.
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

- **Not in the plan:** the following were added after the independent reviews:
  - the Hellinger and minimality checks;
  - the class range B ≤ 300;
  - the grid-sensitivity probe;
  - the retained-seed counterexample with its derived bound.
- **Replacing a plan item:** the controller record enumeration replaces the plan's seeded enumeration for h ≤ 12.
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
