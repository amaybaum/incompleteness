# Delayed old-port history and the frozen acceptance carrier

24 October 2026. Author computation under #912. The plan was committed before computation at `d72ea524`, whose
parent is #912 at `588edce16926ae1a40d1f1e75fc1b5cfb7ccc55e`. The Native A
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
  old q9 at L;
- v6's candidate access contract, with the eight old ports added: the public records are exactly the eight raw
  port streams, the old whole-q9 record, the single whole-V record and the pointer prefix. Q8, Q10, M, the other
  neighbours, the pool and the phase and workspace wires are private. In v6's tested sectors, adding the whole M
  triple to the record gives accepted posteriors with decoder determinant as low as −1/18.

At actual L the result is a written conditional corollary: it rests on the exact geometry g1–g3 below and on the
inherited Native A and `history_v11` results. The scaled control does not establish it. That control uses one
port, so G arrives at a single port, whereas at actual L it reaches ports 3 and 5 at the same tick; and its
horizon, 8, exceeds 2n.

It does not establish any of the following:
- native storage, compilation, routing, clock or isolation;
- the bank and G priors, which are supplied;
- an actual-L simulation;
- an observer-access rule or access closure;
- anything beyond 2L, new ports or reads, or the next stage;
- A1/A2 equivalence or a general instrument.

## Argument

The supplied joint prior extends `history_v11`'s complement: given C0, the bank, G and the pads are uniform and
independent.

1. **G masks the pool.** Native A's G masks the pool. Native A's complement contains the whole bank, so the pool is
   uniform given C0 and the tail.
2. **The tail record is a bijection of the tail.** `history_v11`'s chronological inversion has steps of the form
   v → α ⊕ H(v ⊕ β), where α and β may be any function of the complement, G included. Run with G in that dirty
   complement, the inversion makes the tail record a bijective image of the fresh bank triples for each fixed
   (C0, G).
3. **The new geometric fact (g1).** No tail-bank triple (t > max(a_i, L)) reaches any carrier site-time. So Φ is a
   function of (C0, G, pads) alone.
4. **The tail is not seen early.** It reaches no port before its own time, so N_L is free of the tail.

Together these give

    Pr(N_L, N_tail, Φ | C0) = [N_L = N_L(C0)] · 2^(−24(H−L)) · Pr_v6(Φ | C0).

Pr_v6(Φ | C0) depends on C0 only through the public old-q9 record (its sign), so the formula is the stated public law.

The carrier does depend on exposed bank from before the tail. Those records belong to N_L, which Native A's
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

  A natively stored carrier could therefore depend on tail-bank triples from L+77, inside the L+91 window. Cone
  arrival makes that dependence possible, not certain. The only dependence actually shown is c3 in the scaled
  control.

## Scaled exhaustive control (n=3, k=2)

Port (0,0,−3), with tail bank times 6, 7 and 8, G-to-port offsets 3, 5 and 5, and horizon 8. Bank times 4 and 5
lie in C0 there, while at actual L the corresponding triples count as tail; this does not affect the argument.
There are three families of 262,144 worlds each:
- old q9 = 2, sign 1 (success);
- old q9 = 6, sign 1 (failure);
- old q9 = 1, sign 0 (success).

| check | result |
| --- | --- |
| read set | The carrier site-times, rebuilt from q9 and the six lattice steps (8 site-times, and 7 phase triples giving v6's 21 phase bits), equal v6's read set, at actual L and in the scaled control. |
| s1 | Records before the tail window are constant. The check is the plan's; recording it as a criterion of the verdict rule, with the old-q9 and neighbour conditions, is post-plan. |
| s2 | The joint (pool, tail-record) map is bijective, with support 262,144 of 262,144. |
| s3 | All 131,072 complete-record cells match v6, and the fresh-tail record/carrier TV is 0; pads enter by product. Each success family has 4,096 accepted records, all with the positive X decoder. |
| x1 | The independent scalar evaluator agrees on 24 sampled worlds per family. |
| x2 | The seven-site inverse holds on all 262,144 worlds. |
| x3 | A duplicated tail triple is detected: the record/carrier TV is positive (131/256, 107/256 and 9/32), which goes beyond the plan. The support, 32,768, is reported only. |
| x4 | Aliasing the second tail triple to the first over the full enumeration lowers the s2 support to 32,768 and fails the s3 cell comparison in every family. This control goes beyond the plan. |

## Countercontrols

These are scoped to the scaled families, conditional on C0.

- **c1, known tail** (the tail fixed, G varied):
  - The tail records take 40 or 48 distinct values.
  - The record/carrier TV is at least 227593/262144, 55345/65536 and 107601/131072 for the three families.
  - On the success families, accepted records have negative determinants: 66,656 of 66,656 and 61,760 of 64,064,
    with minimum −1/2. These accepted-record denominators go beyond the plan.
  - So the bank is load-bearing.
- **c2, a duplicated tail triple:** TV 131/256, 107/256 and 9/32.
- **c3, q8 left to native dynamics:**
  - At the horizon, the TV against the tail records is 1823/32768, 1503/32768 and 1509/32768, so frozen storage is
    load-bearing.
  - Two ticks before the first tail triple arrives, the TV is 0.
  - That second row was added after the plan and is reported only; `PROVENANCE.json` records it.

## Replay

    D=<repository root>/verification/programmes/oi-qm/reconstruction/composition-access-20261024/delayed_history_v7
    python3 -I -B "$D/checks.py" > out.json && cmp out.json "$D/result.json"
    python3 -I -B -O "$D/checks.py" > out.json && cmp out.json "$D/result.json"

Run from an empty working directory; each run takes about one minute. If a
required control fails, the checker prints `VOID` and exits with status 2. `PROVENANCE.json` and `result.json`
list every row added after the plan. The checker uses the standard library only
and imports no author engine. `SHA256SUMS` lists `PLAN.md`, `REPORT.md`, `checks.py`, `result.json` and
`PROVENANCE.json`.
