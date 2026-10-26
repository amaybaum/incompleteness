# Review: #912 `delayed_history_v7` (author `d72ea524`, `f08390a3`, `114ad502`)

Independent separate-engine review, 24 October 2026. Local only: nothing pushed or posted. The clone was not modified.

## Verdict: BLOCK (two findings, both cheap to fix; the substance reproduces)

The mathematics holds. Every number I recomputed matches. The block is for one vacuous required control and one
sentence that claims more than the geometry shows.

## Findings

1. **x3 is vacuous** (`checks.py:463-465`, `REPORT.md:79`, `PLAN.md` item 3). `dup` keeps 2^15 of the 2^18 lanes,
   so `dup_support < WORLDS` holds automatically. The reported support of 32,768 equals the subset size, which means
   the map on the subset is injective, not that a collapse was detected. Mutant M4 replaces the duplicate with a
   *pinned*, non-duplicated triple: x3 still passes, c2 drops to TV 0, and the verdict is still HOLDS. The plan lists
   x3 among the controls that must be green or the verdict is void. **Fix:** make the required detector non-vacuous,
   for example require c2 TV > 0, which is the s3 statistic firing on the duplicated bank. Alternatively, run the
   s2/s3 detectors on a full enumeration in which one tail triple is aliased and require both to fail; my engine
   gives support 32,768 and TV 131/256 there. Label the change post-plan in `PROVENANCE.json`. I expect no change to
   the verdict.
2. **Geometry overclaim** (`REPORT.md:61-62`). "A natively stored carrier would therefore acquire bank-dependent
   public records from L+77" goes beyond the geometry. A first arrival into the cone at an off-axis site shows that
   dependence is possible, not that it occurs. v6's own report says reaching a cone does not prove a leak.
   **Fix:** say "could depend on tail-bank triples from L+77 …", and cite the scaled c3 row as the only exhibited
   dependence.

## Nits

- `REPORT.md:76-77` and `checks.py:440-454`: "524,288 cells" and "16,384 positive records" each include a ×4 pad
  loop that never touches the data. 131,072 cells and 4,096 records are actually compared, and the pads enter only
  by the product.
- `REPORT.md:88-89`: the c1 accepted-record denominators are post-plan according to `PROVENANCE.json`, but only
  the c3 row is labelled post-plan.
- `checks.py:573`: `all_required_controls_pass: True` is a literal. It also comes out True for the x3 mutant.
- `checks.py:73-76`: no control ties the carrier list to v6's read set. Mutant M3, which drops q9+y, still gives
  HOLDS with slack 76, and only the `cmp` against `result.json` catches it. The list itself is correct: see g1 below.
- `REPORT.md:66-67`: the scaled tail is t=6..8. Bank t=4,5, which the actual-L claim counts as tail, is held in
  C0. That is harmless, but the report should say so.
- `REPORT.md:37-43`: "the one new fact needed is geometric" leaves two steps implicit:
  - The joint prior, bank uniform given (C0,G,pads), extends history_v11's stated complement, which predates F9.
    `REPORT.md:29` lists it among the supplied priors.
  - The step from the conditional-on-C0 formula to the public law needs one sentence: Pr_v6(Φ|C0) depends on C0
    only through the public old-q9 sign.
- `REPORT.md:3`: "no retained review yet" will go stale.

## Proof steps

- **(a) Tail independence of the pool.** Native A's C is every initial variable except G, so it contains the whole
  bank, and the pool is uniform given (C0,tail). By g1 the pool is a function of (C0,G). This follows.
- **(b) G as background in history_v11's inversion.** Each first-arrival step has the form v→α⊕H(v⊕β), with α and
  β arbitrary functions of the complement and of earlier bank inputs. G and its fields belong to the complement and
  need no ordering. The same-tick case, F8 reaching port 5 at L+77 together with f5(L+77), is exactly the scaled
  t=6 coincidence, and s2 holds there. G sources lie on no bank ray in (a_i,2L], which I checked.
- **(c) Conditioning on C0.** Given C0, (G,pads,tail) are independent and uniform. N_tail is a bijection of the
  tail for each fixed (C0,G), and Φ is a function of (C0,G,pads). That gives
  Pr = [N_L=N_L(C0)]·2^(−24(H−L))·Pr_v6(Φ|C0).
  - Pr_v6(Φ|C0) depends only on s = p.B. My reference law is built from s alone and matches in all four
    backgrounds, so the formula survives averaging over C0 given the public past.
  - The tail reaches no port before its own time (minimum margin 0, at its own port). So N_L is free of the tail.
  - **Positive:** the argument also holds whatever tail-independent content the lattice keeps after the read-out.
- **The formula follows.** I found no gap.

## Values from my engine (`review_checks.py`, own bit-slicer + own scalar evaluator; output `review_checks.out`)

- **g1:** 64 pairs, minimum slack 76.
  - First tail arrival at L+77 for q8, m, q9+x and q9+y; L+78 for q9; L+79 for q10 and q9−y.
  - The carrier list (V, six neighbours at L+1, old q9) is v6's complete read set. The unread q9@L+1 has slack 77.
- **g2:** offsets {F8: 77, 77, 447; F10: 79, 79, 449; F9: 79, 79, 449}. The Native A triangle is confirmed.
- **g3:** 2,184 and 8,664 bits; both horizons are ≤ 2L.
- **Pre-tail exposure:** 14 hits, all first arrivals at deadline+2, from ports {0,2,3,5}.
- **Scaled control, seeds 1/2/4 (author C0 families) plus my own random background:**
  - s2: support 262,144 in every family.
  - s3: 0 of 131,072 cells mismatch, and TV is 0.
  - Accepted (w,V) records: 4,096 of 4,096 are pure X with Y=Z=0.
- **Countercontrols, exact match with the author:**
  - c1 min/max TV: 227593/262144 and 229177/262144; 55345/65536 and 224605/262144; 107601/131072 and 109011/131072.
  - c1 determinant minimum −1/2, with 66,656/66,656 and 61,760/64,064 negative.
  - c2: 131/256, 107/256, 9/32.
  - c3: 1823/32768, 1503/32768, 1509/32768. The row two ticks earlier is 0.
- **My own background:** c1 218855/262144 to 220783/262144; c2 131/256; c3 1581/32768.
- **Detector controls fire:** with the duplicated tail, support 32,768 and TV 131/256. With the tail known,
  support 512 and TV 228169/262144, which equals the author's M1b mutant.

## Replay, hashes, mutations

- **Replay:** run normally and with `-O` from empty directories (≈80 s each), output is byte-identical to
  `result.json`.
- **Hashes:** `SHA256SUMS` passes for all five files. All 8 `PROVENANCE.json` source hashes match at
  `f24a57a7` and `588edce1`. `PLAN.md` is unchanged since `d72ea524`.
- **Mutants** (copies are in `rev912/mut/`):
  - M1, bank mask dropped in the bit-slicer only: caught by x1.
  - M1b, bank mask dropped in both engines: NEGATIVE (s2 support 512).
  - M2, tail lower bound moved to L−76: NEGATIVE (g1 slack −1).
  - M3, q9+y removed from the carrier list: **survives**.
  - M4, x3 pinned instead of duplicated: **survives** (Finding 1).
  - M5, old-local term dropped: caught.
  - M6, native q8 used as the carrier: caught (seven-site inverse).
