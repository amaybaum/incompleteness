Two computations were run at `D`: the production path (act 40's candidate enumeration and flat calculus,
each candidate's conditions factorized by class, loci as unions over alignments) and the independent path
(act 36's partition search on the numeric matrix, alignments counted by a pruned matching search with factor
unitarity). **They agree at every point both computed**, in both notions.

| where | notion | partition structures, per orientation by shape `4 × 4` / `8 × 2` / `2 × 8` | valid alignments | recorded at the sorted alignment |
| --- | --- | --- | --- | --- |
| `SIG` | strict and relaxed | 20: 5 / 2 / 3 | 976: `k1` 8, `k2` 64, `k3` 8, `k4` 8, `k5` 8; `e1`, `e2` 4 each; `t1`, `t2`, `t3` 128 each — per orientation | 18: 4 / 2 / 3 |
| `Pu(−1)` | strict | 2: 0 / 0 / 1, act 36's frozen partition | 256 | 2 |
| `Pu(−1)` | relaxed | 20, those of `SIG` | 976 | 2 (act 37's claim is strict) |
| `P`, `Pu(u₅)` | strict and relaxed | 2: 0 / 0 / 1, act 36's frozen partition | 256, all 128 per orientation | 2 |
| `Hu(−1)` | strict and relaxed | 4: 1 / 0 / 1 — `M_COL`, `M_ROW`, and a `4 × 4` partition that is `k4` moved by the row exchange `7 ↔ 15` and the column exchange `2 ↔ 8`, in each orientation | 272: 128 per `2 × 8`, 8 per `4 × 4` | 2 |
| act 38's twenty Gaussian-rational candidate points on `Hu` | strict and relaxed | 20 at `u = 1`, 4 at `u = −1`, none at the other eighteen | — | the same points |

- **Factorization classes at `SIG`** (Definition 6), both notions: 976 realizing triples, closed under the
  stabilizer; **70** classes under the full stabilizer (sizes from 2 to 64) and **140** under the
  transpose-free subgroup; the partition structures form **10** orbits under the full stabilizer, each a
  structure with its transpose, and **20** under the transpose-free subgroup. Act 37's "nine classes" are the
  partition-structure orbits under the full stabilizer, at the sorted alignment.
- **The fibres of `π`**: enumerated on the carriers of four, six and eight points, shapes `2 × 2`, `2 × 3`,
  `3 × 2`, `2 × 4` and `4 × 2`: every fibre has exactly `|R(m, n)|` elements, and every partition has
  `(m!)^(n−1)` alignments.
- **Act 37's arc** (production path): strictly, the frozen `2 × 8` partition structure per orientation holds
  identically and the only exceptional point is `u = 1`; up to diagonal equivalence the exceptional points are
  `u = 1` and `u = −1`.
- **Act 40's family**: 46 partition candidates; **43** nonempty loci, strictly and relaxed, strict equal to
  relaxed for all 46; **21** distinct flats, of which four are the points `u₁ = ±z⁻², u₂ = 1, u₃ = ±1`; the
  maximal flats exactly the five faces. At act 40's seventeen exact points the independent path counts
  `[0, 0, 1, 1, 2, 0, 1, 1, 0, 4, 8, 5, 20, 4, 20, 20, 4]` admitted partition structures, strictly and relaxed
  alike, with valid alignments `[0, 0, 128, 128, 256, 0, 128, 128, 0, 272, 596, 576, 976, 272, 976, 976, 272]`;
  act 40's sorted control recorded `[0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4]`.
- **Act 36's `4 × 4` hulls**: @@HULLS@@
