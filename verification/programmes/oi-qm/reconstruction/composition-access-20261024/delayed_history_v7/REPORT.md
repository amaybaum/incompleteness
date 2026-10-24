# Delayed old-port history and the frozen acceptance carrier

24 October 2026. This is an author computation, with no retained review yet. The plan was published before
computation at `d72ea524` on #912, whose base is #912 at `588edce16926ae1a40d1f1e75fc1b5cfb7ccc55e`. The Native A
source geometry and its eight-port bank `history_v11/` are author `f24a57a7c23cc1818c04265cec7604f8bc2f410d`.

## Result and scope

Verdict, generated from the measured values: `HOLDS_WITHIN_SCOPE`.

The setting is the hypothetical serial alignment of the `composition_flag_v6/` core with native ticks L+2..L+91,
or L+2..L+361 for the recorded dilation. Within that alignment, the source fronts that reach old public ports at
L+77 (F8) and L+79 (F10, F9) do not change the complete public law of the frozen logical v6 carrier. For every
horizon L < H ≤ 2L, the following are distributed jointly with the outgoing selected carrier as the v6 law
tensored with an independent uniform tail of 24(H−L) bits:
- the eight old raw port streams through H;
- the old whole-q9 record;
- the whole-V record;
- the pointer prefix.

The result is conditional on:
- the Native A source contract;
- the supplied `history_v11` bank;
- v6's supplied isolated logical storage for the carrier, which sits at q9 at L+2, its six neighbours at L+1 and
  old q9 at L.

It does not establish any of the following:
- native storage, compilation, routing, clock or isolation;
- the bank and G priors, which are supplied;
- an actual-L simulation;
- anything beyond 2L, new ports or reads, or the next stage;
- A1/A2 equivalence or a general instrument.

## Argument

Native A's G masks the pool. `history_v11`'s chronological inversion, run with G in the dirty complement, makes
the tail record a bijective image of fresh bank triples. The one new fact needed is geometric: no tail-bank triple
(t > max(a_i, L)) reaches any carrier site-time (g1). With that fact,

    Pr(N_L, N_tail, Φ | C0) = [N_L = N_L(C0)] · 2^(−24(H−L)) · Pr_v6(Φ | C0).

The carrier does depend on exposed bank from before the tail, but those records belong to N_L, which Native A's
conditioning already covers.

## Actual-L geometry (exact integers)

- **g1.** No tail triple reaches a carrier site-time: 64 of 64 tail-family × carrier pairs, minimum slack 76.
- **g2.** G reaches no port by L+2. The smallest G-to-port offsets over L are 77 for F8 (twice), and 79 for F10 and
  for F9 (twice each).
- **g3.** Both horizons lie within 2L. The tail is 2,184 bits to the core's end and 8,664 bits to the dilation's end.
- **Exposed pre-tail bank.** There are 14 first arrivals from pre-tail triples, at t = deadline + 2, from ports 0, 2,
  3 and 5. They reach q8, m, q9, q9±y and q9+x at L+1 or L+2.
- **Sharp boundary.** Tail triples first reach the carrier sites at:

  | site | first tail arrival |
  | --- | --- |
  | q8, m, q9+x, q9+y | L+77 |
  | q9 | L+78 |
  | q10, q9−y | L+79 |

  A natively stored carrier would therefore acquire bank-dependent public records from L+77, inside the L+91
  window.

## Scaled exhaustive control (n=3, k=2)

Port (0,0,−3), with tail bank times 6, 7 and 8, G-to-port offsets 3, 5 and 5, and horizon 8. Three families of
262,144 worlds each:
- old q9 = 2, sign 1 (success);
- old q9 = 6, sign 1 (failure);
- old q9 = 1, sign 0 (success).

| check | result |
| --- | --- |
| s1 | Records before the tail window are constant. |
| s2 | The joint (pool, tail-record) map is bijective, with support 262,144 of 262,144. |
| s3 | All 524,288 complete-record cells match v6, and the fresh-tail record/carrier TV is 0. Each success family has 16,384 positive accepted complete records. |
| x1 | The independent scalar evaluator agrees on 24 sampled worlds per family. |
| x2 | The seven-site inverse holds on all 262,144 worlds. |
| x3 | Duplicated-tail detection fires, with support 32,768. |

## Countercontrols

These are scoped to the scaled families, conditional on C0.

- **c1, known tail** (the tail fixed, G varied):
  - The tail records take 40 or 48 distinct values.
  - The record/carrier TV is at least 227593/262144, 55345/65536 and 107601/131072 for the three families.
  - On the success families, accepted records have negative determinants: 66,656 of 66,656 and 61,760 of 64,064,
    with minimum −1/2.
  - So the bank is load-bearing.
- **c2, a duplicated tail triple:** TV 131/256, 107/256 and 9/32.
- **c3, q8 left to native dynamics:**
  - At the horizon, the TV against the tail records is 1823/32768, 1503/32768 and 1509/32768, so frozen storage is
    load-bearing.
  - Two ticks before the first tail triple arrives, the TV is 0.
  - That second row was added after the plan and is reported only; `PROVENANCE.json` records it.

## Replay

    python3 -I -B checks.py > out.json && cmp out.json result.json
    python3 -I -B -O checks.py > out.json && cmp out.json result.json

Run from an empty working directory; each run takes about one minute. The checker uses the standard library only
and imports no author engine. `SHA256SUMS` lists `PLAN.md`, `REPORT.md`, `checks.py`, `result.json` and
`PROVENANCE.json`.
