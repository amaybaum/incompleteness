# A1 appendix. Synthetic fixtures and their hand derivations

Part of amendment A1 (`A1-frozen-code.md`, §5 and §11). The machine-readable form is `A1-fixtures.json` in this
directory. Where this file and the JSON differ, the difference is a defect of the amendment, to be corrected before `F`;
neither governs the other.

**Provenance of every expected value.** Every expected value in this file and in `A1-fixtures.json` was derived by hand,
by the derivations written below. None was produced by running implementation A, implementation B, `controls.py`, or any
program that evaluates a fixture map. After writing the JSON, the drafter ran two checks on the document itself, listed
in the drafting log (A1 §12): a parse with key-set, row-order, mirror-row and fragment-against-row-token comparisons, and
the SHA-256 of each fixture input's canonical bytes. Neither evaluates a map or derives a field.

**No fixture is the K1 dynamics.** No fixture map, and no power of one, is `φ(x, y) = (y, Ay − x)` at any `N`: SF-1 maps
are explicit permutations of 4-bit strings; SF-2′'s map `J` and its powers `J^k` (§3) have no cell exchange between two
slices; SF-3's map fixes `x_0` and `y_0`, while every K1 map sends `y_0` to `x_0`.

## 0. Conventions

- A state of `n` cells is the string of its cells in the fixture's `cells` order, each `0` or `1`. States are ordered
  lexicographically with `0 < 1`. For 4-cell fixtures the state string is the 4-bit binary numeral of an integer `i` in
  `0, …, 15`, most significant cell first, so integer order is string order. Integers in the derivations name states:
  `0 = 0000`, `1 = 0001`, `2 = 0010`, `3 = 0011`, `4 = 0100`, `5 = 0101`, `6 = 0110`, `7 = 0111`, `8 = 1000`,
  `9 = 1001`, `10 = 1010`, `11 = 1011`, `12 = 1100`, `13 = 1101`, `14 = 1110`, `15 = 1111`.
- A linear map is given cell by cell: `phi[c]` lists the input cells whose sum mod 2 is the new value of `c`. The
  matrix of the map has row `c` with 1 in exactly the columns listed.
- Output formats are §10.2's (`p/q` in lowest terms, `0/1`, `1/1`, sorted lists, keys sorted by the serializer), with
  the fixture's cell names and lengths in place of the instance's.
- Row indices count from 0 in the order B-pl, B-eq, B-ct, and within a branch the member order of the output. In SF-3
  rows 0–8 are B-pl, 9–17 B-eq, 18–26 B-ct; the members are, in order, `pi0`, `0000`, `0001`, `0010`, `0111`, `1000`,
  `1001`, `1010`, `1111`.

## 1. SF-1: orbit partitions of explicit permutations (A and B)

Kind `perm`, cells `b_0, …, b_3`, 16 states. Each fixture gives the image of every state. The answer is the
`members.json`-form member list (`pi0` first, then one entry per cycle in increasing order of least state, with sorted
states), the histogram and the completeness block.

**Derivation method.** Walk each cycle from its least unvisited state as M3 does, then sort. Each walk below lists the
images in order; the walk closes when the start state recurs.

### SF-1a: the §11.2 permutation, extended to 16 states

Cycles, `a → next`: `(0)(1 2)(3 4 5)(6 7 8 9 10 11)(12)(13 14 15)`.

| From least state | Walk | Sorted states | Length |
|---|---|---|---|
| 0 | 0 → 0 | `0000` | 1 |
| 1 | 1 → 2 → 1 | `0001, 0010` | 2 |
| 3 | 3 → 4 → 5 → 3 | `0011, 0100, 0101` | 3 |
| 6 | 6 → 7 → 8 → 9 → 10 → 11 → 6 | `0110, 0111, 1000, 1001, 1010, 1011` | 6 |
| 12 | 12 → 12 | `1100` | 1 |
| 13 | 13 → 14 → 15 → 13 | `1101, 1110, 1111` | 3 |

The images `0, 2, 1, 4, 5, 3, 7, 8, 9, 10, 11, 6, 12, 14, 15, 13` of `0, …, 15` are the sixteen states once each, so
the map is a bijection. Lengths sum to 16; six cycles; histogram `{"1": 2, "2": 1, "3": 2, "6": 1}`.

### SF-1b: interleaved cycles

Cycles: `(0 7 3)(1)(2 9 4 11)(5)(6 10 8)(12 15 13 14)`. Walk order differs from sorted order in four cycles, cycle length
is not monotone in the least state, there are two fixed points, and two pairs of cycles share a length.

| From | Walk | Sorted states | Length |
|---|---|---|---|
| 0 | 0 → 7 → 3 → 0 | `0000, 0011, 0111` | 3 |
| 1 | 1 → 1 | `0001` | 1 |
| 2 | 2 → 9 → 4 → 11 → 2 | `0010, 0100, 1001, 1011` | 4 |
| 5 | 5 → 5 | `0101` | 1 |
| 6 | 6 → 10 → 8 → 6 | `0110, 1000, 1010` | 3 |
| 12 | 12 → 15 → 13 → 14 → 12 | `1100, 1101, 1110, 1111` | 4 |

Images of `0, …, 15`: `7, 1, 9, 0, 11, 5, 10, 3, 6, 4, 8, 2, 15, 14, 12, 13`, each state once. Sum 16; six cycles;
histogram `{"1": 2, "3": 2, "4": 2}`.

### SF-1c: a long cycle

Fixed points 0 and 15, and the 14-cycle `1 → 8 → 3 → 12 → 5 → 10 → 7 → 14 → 2 → 9 → 4 → 13 → 6 → 11 → 1`. The cycle
visits `1, …, 14` once each (sorted: `1, 2, …, 14`), so its sorted states are `0001` to `1110`. Its length, 14, exceeds
every cycle length of the instance (at most 10), so an iteration bound tuned to the instance shows.

Images of `0, …, 15`: `0, 8, 9, 12, 13, 10, 11, 14, 3, 4, 7, 1, 5, 6, 2, 15`, each once. Three cycles; histogram
`{"1": 2, "14": 1}`.

## 2. SF-2: 𝔽₂ ranks (B only)

Kind `rank`. Input: the rows of a 0/1 matrix. Answer: its rank over 𝔽₂. Only B computes ranks (§8.2, CC-CYC2).

| Id | Matrix (rows) | Rank | Derivation |
|---|---|---|---|
| SF-2a | `[1,0,0] [0,1,0] [0,0,1]` | 3 | the identity; three pivots in place |
| SF-2b | three zero rows | 0 | no nonzero row |
| SF-2c | `[1,1,0] [0,1,1] [1,0,1]` | 2 | row 1 + row 2 = `[1,0,1]` = row 3, and rows 1, 2 are distinct and nonzero. Over ℤ the determinant is `1·(1·1 − 1·0) − 1·(0·1 − 1·1) = 2`, so the rank over ℚ is 3: the case separates the fields |
| SF-2d | `[0,1] [1,0]` | 2 | determinant `0·0 − 1·1 = −1`, odd. Column 0's pivot is in row 2, so elimination needs a row exchange |
| SF-2e | `[1,1,1] [1,1,1] [0,0,0]` | 1 | two equal nonzero rows and a zero row |
| SF-2f | `[0,0,1,1] [0,1,0,1] [1,1,1,0] [1,0,0,0]` | 3 | see below |

**SF-2f.** Elimination: column 0's first pivot is row 3 (rows 1 and 2 have 0 there), so a row exchange is needed. With
pivot `[1,1,1,0]`, row 4 becomes `[1,0,0,0] + [1,1,1,0] = [0,1,1,0]`. Column 1: pivot row 2 `[0,1,0,1]`; row 4 becomes
`[0,1,1,0] + [0,1,0,1] = [0,0,1,1]`. Column 2: pivot row 1 `[0,0,1,1]`; row 4 becomes 0. Three pivots: rank 3.
Second method: row 1 + row 2 = `[0,1,1,0]` = row 3 + row 4, so the four rows are dependent; rows 1, 2 and 4 are
independent (row 4 alone has a 1 in column 0, and rows 1, 2 are distinct and nonzero). Rank 3.

SF-2d and SF-2f need a row exchange, SF-2e has rank 1, and SF-2d and SF-2f are not 3×3.

## 3. SF-2′ (`SF-2p`): the CC-CYC2 chain on a toy map, with its orbits (A and B; B also writes the rank chain)

Kind `linear`, cells `c_0, …, c_3`. The map is the unipotent Jordan block `J = I + N`, `N c_i = c_{i+1}`:

`J(c_0, c_1, c_2, c_3) = (c_0 + c_1, c_1 + c_2, c_2 + c_3, c_3)`, and `J^{−1} = I + N + N² + N³`:
`J^{−1}(c) = (c_0 + c_1 + c_2 + c_3, c_1 + c_2 + c_3, c_2 + c_3, c_3)`.

*Inverse check.* With `(a, b, c, d) = J(s)`: `a + b + c + d = c_0 + 2c_1 + 2c_2 + 2c_3 = c_0`; `b + c + d = c_1`;
`c + d = c_2`; `d = c_3`. So `J^{−1} ∘ J = I`, and both are 4×4 over 𝔽₂, so also `J ∘ J^{−1} = I`.

*Powers.* `J² = I + N²`: `(c_0 + c_2, c_1 + c_3, c_2, c_3)`. `J³ = I + N + N² + N³` (`3 ≡ 1`). `J⁴ = I + N⁴ = I`.
None of them exchanges two pairs of cells.

**Orbits** (walk from the least unvisited state):

| From | Walk | Sorted states | Length |
|---|---|---|---|
| `0000` | `0000 → 0000` | `0000` | 1 |
| `0001` | `0001 → 0011 → 0101 → 1111 → 0001` | `0001, 0011, 0101, 1111` | 4 |
| `0010` | `0010 → 0110 → 1010 → 1110 → 0010` | `0010, 0110, 1010, 1110` | 4 |
| `0100` | `0100 → 1100 → 0100` | `0100, 1100` | 2 |
| `0111` | `0111 → 1001 → 1011 → 1101 → 0111` | `0111, 1001, 1011, 1101` | 4 |
| `1000` | `1000 → 1000` | `1000` | 1 |

Each step applies `J`; for example `J(0011) = (0+0, 0+1, 1+1, 1) = 0101` and `J(0101) = (0+1, 1+0, 0+1, 1) = 1111`.
The sixteen states appear once each. Histogram `{"1": 2, "2": 1, "4": 3}`; six cycles.

**Rank chain** (`kmax = 4`). `J^k − I` over 𝔽₂:
- `k = 1`: `N`, rows `[0,1,0,0] [0,0,1,0] [0,0,0,1] [0,0,0,0]`: rank 3, `|Fix| = 2^{4−3} = 2`.
- `k = 2`: `N²`, rows `[0,0,1,0] [0,0,0,1] 0 0`: rank 2, `|Fix| = 4`.
- `k = 3`: `N + N² + N³`, rows `[0,1,1,1] [0,0,1,1] [0,0,0,1] 0`: rank 3, `|Fix| = 2`.
- `k = 4`: `0`: rank 0, `|Fix| = 16`; `J⁴ = I`, so `identity_at_kmax` is true.

States of exact period `d` = `Σ_{e|d} μ(d/e) |Fix(J^e)|`: `d = 1`: 2. `d = 2`: `4 − 2 = 2`. `d = 3`: `2 − 2 = 0`.
`d = 4`: `μ(1)·16 + μ(2)·4 + μ(4)·2 = 16 − 4 + 0 = 12`. Cycles of length `d`: 2, 1, 0, 3. These equal the
orbit histogram, which is the cross-check this fixture exists for.

**SF-2′b (`SF-2pb`): a wrong inverse.** The same `J`, with `phi_inv` set to `J` itself. `J ∘ J = J² ≠ I` (for example
`J²(0010) = 1010`), so M2's check fails and `completeness.bijection` is `false`. M3 to M5 use `φ` only (§6), so the
members, histogram and B's rank chain are those of SF-2p. This is the input-side analogue of MU-C2 (A1 §11).

## 4. SF-3: the full row pipeline on a toy system (A and B; B also writes the rank chain)

Kind `system`. Cells `x_0, x_1, y_0, y_1` (two sites, two slices), `Σ = {x_0, y_0}`, readout `V = y_1`, `T = 1`,
`q = 2`. The map and its inverse:

`φ(x_0, x_1, y_0, y_1) = (x_0, y_1, y_0, x_1 + y_0 + y_1)`, `φ^{−1}(x_0, x_1, y_0, y_1) = (x_0, x_1 + y_0 + y_1, y_0, x_1)`.

*Inverse check.* `φ^{−1}(φ(s)) = (x_0, y_1 + y_0 + (x_1 + y_0 + y_1), y_0, y_1) = s`, and
`φ(φ^{−1}(s)) = (x_0, x_1, y_0, (x_1 + y_0 + y_1) + y_0 + x_1) = s`.

Class decisions: `g1`, and `a` and `t1` of `class_rule` and `support_restriction`, are all `"pass"`. Three variants share
the map: `SF-3` at stage `rows` with no adversarial entry; `SF-3f` at `final` with an adversarial token equal to the
computed one; `SF-3g` at `final` with a differing adversarial token.

### 4.1 Stage M

`φ` fixes `x_0` and `y_0`. On `(x_1, y_1)` it acts as `(x_1, y_1) → (y_1, x_1 + y_1 + y_0)`:
- `y_0 = 0`: `00 → 00`; `01 → 11 → 10 → 01`. A fixed point and a 3-cycle.
- `y_0 = 1`: `11 → (1, 1+1+1) = 11`; `00 → 01 → 10 → 00` (`01 → (1, 0+1+1) = 10`; `10 → (0, 1+0+1) = 00`). A fixed
  point and a 3-cycle.

So for each `(x_0, y_0)` there is one fixed point and one 3-cycle. Writing states as `x_0 x_1 y_0 y_1`:

| Least state | `(x_0, y_0)` | Sorted states | Length |
|---|---|---|---|
| `0000` | `(0, 0)` | `0000` | 1 |
| `0001` | `(0, 0)` | `0001, 0100, 0101` | 3 |
| `0010` | `(0, 1)` | `0010, 0011, 0110` | 3 |
| `0111` | `(0, 1)` | `0111` | 1 |
| `1000` | `(1, 0)` | `1000` | 1 |
| `1001` | `(1, 0)` | `1001, 1100, 1101` | 3 |
| `1010` | `(1, 1)` | `1010, 1011, 1110` | 3 |
| `1111` | `(1, 1)` | `1111` | 1 |

Eight cycles, histogram `{"1": 4, "3": 4}`. `φ³ = I`, since every cycle has length 1 or 3.

**Rank chain** (`kmax = 3`). `φ − I`: rows `x_1: [0,1,0,1]` (`y_1 + x_1`) and `y_1: [0,1,1,0]` (`x_1 + y_0`), the
others zero: rank 2, `|Fix| = 4`. `φ² = φ^{−1}`, so `φ² − I` has rows `x_1: [0,0,1,1]` and `y_1: [0,1,0,1]`: rank 2,
`|Fix| = 4`. `φ³ − I = 0`: rank 0, `|Fix| = 16`. Exact periods: 4, `4 − 4 = 0`, `16 − 4 = 12`; cycles 4, 0, 4, equal to
the histogram.

### 4.2 Region (R0)

`V(t_0) = y_1`; `V(t_0 + 1) = y_1(φ(s)) = x_1 + y_0 + y_1`. Cells outside `Σ` with a nonzero coefficient: `y_1`, and
`x_1, y_1`. So `E = {x_1, y_1}` and `q^{−|E|} = 1/4`. `W_eq` is `V`'s site, 1, in both slices: `{x_1, y_1}`. At equal time
both cells of `W_eq` are in `E`, so `overlap["B-eq"] = ["x_1", "y_1"]`, flagged tautological; at cross time
`overlap["B-ct"] = []`. `E`-values and `w` values of `W_eq` are strings over `(x_1, y_1)`; `σ` is a string over
`(x_0, y_0)`.

### 4.3 Per-state table

`Z` means `x_1 = y_1 = 0`. `w_eq = x_1 y_1`. `w_ct` is `(x_1, y_1)` of `φ^{−1}(s)`, i.e. `(x_1 + y_0 + y_1, x_1)`. The
readout pair is `(V_{t_0}, V_{t_0+1}) = (y_1, x_1 + y_0 + y_1)`. Rows with `x_0 = 1` equal those with `x_0 = 0` except
that `σ` begins with 1.

| State | `σ` | in `Z` | `E`-value | `w_eq` | `w_ct` | readout |
|---|---|---|---|---|---|---|
| `0000` | `00` | yes | `00` | `00` | `00` | `00` |
| `0001` | `00` | no | `01` | `01` | `10` | `11` |
| `0010` | `01` | yes | `00` | `00` | `10` | `01` |
| `0011` | `01` | no | `01` | `01` | `00` | `10` |
| `0100` | `00` | no | `10` | `10` | `11` | `01` |
| `0101` | `00` | no | `11` | `11` | `01` | `10` |
| `0110` | `01` | no | `10` | `10` | `01` | `00` |
| `0111` | `01` | no | `11` | `11` | `11` | `11` |

Example, `0110`: `w_ct = (1 + 1 + 0, 1) = 01`; readout `(0, 1 + 1 + 0) = 00`.

**Blocks under `π_0`.**
- B-pl: one block, `S`; `|Z| = 4` (`0000, 0010, 1000, 1010`), so `ref("") = 4/16 = 1/4`.
- B-eq: `B_w = {x_1 y_1 = w}`, four states each (`x_0, y_0` free). `B_{00} ⊆ Z`, the others are disjoint from `Z`:
  `ref = 1/1` at `00` and `0/1` elsewhere. `J_w = {w}`.
- B-ct: `B_w = {x_1 = b, y_1 = a + b + y_0}` for `w = ab`, four states each. `B_{00} = {0000, 0011, 1000, 1011}`, `E`-values
  `{00, 01}`, two in `Z`: `ref = 1/2`. `B_{01} = {0101, 0110, 1101, 1110}`, `E`-values `{10, 11}`, none in `Z`: `0/1`.
  `B_{10} = {0001, 0010, 1001, 1010}`, `E`-values `{00, 01}`, two in `Z`: `1/2`. `B_{11} = {0100, 0111, 1100, 1111}`,
  `E`-values `{10, 11}`: `0/1`. These are the `J_w`.

**W-certification (R4).** B-pl: `S` meets `Z` and is not inside it: false. B-eq: each block lies inside `Z` or misses
it: true. B-ct: `B_{00}` meets `Z` and is not inside it: false.

### 4.4 Members, branch by branch

`π_0` (support 16, `d_ratio = 16/16 = 1/1`):
- B-pl: `mass {"": 1/1}`, `weak = ref = 1/4`, no sharp `w`. `NB(π_0)` (`nb_g1`): for each of the four `σ`, the four
  states with that `σ` have readouts `00, 11, 01, 10` (`y_0 = 0`) or `01, 10, 00, 11` (`y_0 = 1`), uniform in both
  cases, so all `L_σ` are equal: false. (c1): `4 · 16 = 64 > 16`: breaks. `I = J` (all four `E`-values): no H-sel
  content. ABSENT.
- B-eq: mass `1/4` at each `w`; `weak = ref` = `1/1` at `00`, else `0/1`. Sharp `00`. Under `ν = π_0(· | B_{00})` the
  four states `0000, 0010, 1000, 1010` have `σ = 00, 01, 10, 11`, each of mass 1/4, and readouts `00, 01, 00, 01`.
  `L_{00} = L_{10} = δ_{00}` and `L_{01} = L_{11} = δ_{01}` differ: `NB` true. (c2) at `00`: mass `1/4`, `k = |E ∖ W| = 0`:
  `2^0 · 16^4 ≤ 16^4`: holds. `I_w = J_w`: no content. G4 passes; G5 forms `Λ` (§4.6).
  Usefulness at `00`: disjoint supports for `(00, 01)`, `(00, 11)`, `(01, 10)`, `(10, 11)`; the other two pairs have
  equal laws, so `law_only` is empty.
- B-ct: mass `1/4` each; `weak = ref` = `00: 1/2, 01: 0/1, 10: 1/2, 11: 0/1`. No sharp `w`: ABSENT. No content.

`u_c[0000]` (support `{0000}`, `d_ratio 16/1`): every branch has one positive-mass `w` (B-pl `""`, B-eq `00`, B-ct `00`),
`weak 1/1`, sharp; one `σ`, so `NB` false: BLIND in every branch. B-pl: `ref 1/4`; (c1) `4 · 1 ≤ 16` holds; content
`I = {00} ⊊ J`: `[{"values": ["00"], "w": ""}]`; `nb_g1` false. B-eq: `ref 1/1`; (c2) `p = 1/1` holds; `I = J = {00}`:
none. B-ct: `ref 1/2`; content `I = {00} ⊊ J_{00} = {00, 01}`: `[{"values": ["00"], "w": "00"}]`.

`u_c[0001]` (support `{0001, 0100, 0101}`, `d_ratio 16/3`, `σ = 00` throughout, so `nb_g1` false):
- B-pl: `weak 0/3 = 0/1`; ABSENT; (c1) `4 · 3 = 12 ≤ 16` holds; content `I = {01, 10, 11} ⊊ J`.
- B-eq: `w = 01, 10, 11`, mass `1/3` each, `weak 0/1`, `ref 0/1`; no sharp: ABSENT; no content.
- B-ct: `w_ct` of `0001, 0100, 0101` = `10, 11, 01`, mass `1/3` each, `weak 0/1`; `ref` `01: 0/1, 10: 1/2, 11: 0/1`;
  ABSENT. Content: `w = 01`: `I = {11}` (from `0101`) `⊊ {10, 11}`; `w = 10`: `I = {01}` `⊊ {00, 01}`; `w = 11`:
  `I = {10}` `⊊ {10, 11}`.

`u_c[0010]` (support `{0010, 0011, 0110}`, `d_ratio 16/3`, `σ = 01` throughout):
- B-pl: `weak 1/3` (only `0010` is in `Z`); ABSENT; (c1) holds; content `I = {00, 01, 10}`.
- B-eq: `w = 00, 01, 10`, mass `1/3` each, `weak 1/1, 0/1, 0/1`, `ref 1/1, 0/1, 0/1`; sharp `00`, one `σ`: `NB` false,
  BLIND; (c2) `p = 1/3`: `1 · 3^3 = 27 ≤ 16^3 = 4096`, holds; no content.
- B-ct: `w_ct` of `0010, 0011, 0110` = `10, 00, 01`, mass `1/3` each, `weak` `00: 0/1, 01: 0/1, 10: 1/1`, `ref`
  `00: 1/2, 01: 0/1, 10: 1/2`; sharp `10`, `NB` false: BLIND. Content: `w = 00`: `I = {01}` `⊊ {00, 01}`; `w = 01`:
  `I = {10}` `⊊ {10, 11}`; `w = 10`: `I = {00}` `⊊ {00, 01}`.

`u_c[0111]` (support `{0111}`, `d_ratio 16/1`): `weak 0/1` everywhere: ABSENT in every branch. B-pl content
`[{"values": ["11"], "w": ""}]`, (c1) holds; B-eq `w = 11`, `ref 0/1`, no content; B-ct `w = 11`, `ref 0/1`, content
`I = {11} ⊊ {10, 11}`.

`u_c[1000]`, `u_c[1001]`, `u_c[1010]`, `u_c[1111]` are `u_c[0000]`, `u_c[0001]`, `u_c[0010]`, `u_c[0111]` with `x_0 = 1`.
`x_0` enters no `E`-value, `w`, readout or bound, and each support has a single `σ`, so every field is the same apart from
`member` and the member name in tokens.

No member's support is moved by `φ` (each is a cycle, or `S`), so T2 does not fire, and `g2.t2` is false in every row.

### 4.5 Field rules for every row

- `candidate` `"P1"`; `g2.a` and `g2.t1` false (class decisions `"pass"`); G1, G2 and G3 `"pass"`.
- `w_rule` and `w_inputs` are §10.2's strings for the branch. `bound_ok`: B-pl the (c1) boolean; B-eq an object over the
  sharp `w` (`{}` when none, as in §10.3); B-ct `null`. `nb_g1`: B-pl `NB(m)`, else `null`. `nb`: over the sharp `w`.
- `ledger`: B-pl `D=log(<d_ratio>); (c1) |E|=2: <holds|breaks>`; B-eq `D=log(<d_ratio>); (c2) no sharp w` or
  `D=log(<d_ratio>); (c2) w=00 p=<mass> k=0: holds`; B-ct `D=log(<d_ratio>); cross time, no D bound; H-ret`.
- A row whose G4 issues ABSENT or BLIND: that token at G4 and as `token`; G5–G7 `"not-reached"` (RD-2); `usefulness`
  `null`; `hypotheses` is RD-3 (i)'s set, the declaration's `H-inv[K-17(a)]` and the branch's access labels, sorted by
  code point: B-pl `["H-cur (declared)", "H-inv[K-17(a)]"]`; B-eq adds `"H-2s (declared)"` first; B-ct also adds
  `"H-ret"` last.
- Tokens: §10.2's strings with member names `π_0` and `u_c[<least state>]`.

### 4.6 The positive row and the class tokens

The only row that passes G4 is `π_0` in B-eq (row 9). `Λ` (R8): `H-inv[K-17(a)]`, the access labels `H-cur (declared)` and
`H-2s (declared)` (`W_eq` holds the previous-slice cell `x_1`), no `H-law` (B-eq is W-certified), no `H-sel` (no
content). Sorted: `["H-2s (declared)", "H-cur (declared)", "H-inv[K-17(a)]"]`. R10: `CONDITIONAL[H-2s (declared),
H-cur (declared), H-inv[K-17(a)]]`.

| Variant | Row 9: G6, G7, `token`, `usefulness` | Class token B-eq |
|---|---|---|
| SF-3 (`rows`) | `pending`, `pending`, `pending`, the usefulness object (A1 §2, Q1) | `pending`, since a row is pending (CLASS) |
| SF-3f (`final`, note agrees) | `pass`, the CONDITIONAL token, the same, kept (positive) | ABSENT: the B-eq rows are positive, BLIND or ABSENT, and ABSENT comes first in A2's order among those attained |
| SF-3g (`final`, note gives `BLIND[π_0; B-eq; H-cur (declared), H-2s (declared)]`) | `UNDECIDED(G6)`, `not-reached`, `UNDECIDED(G6)`, `null` (A1 §2, Q2) | `UNDECIDED(G6)`: UNDECIDED precedes ABSENT |

B-pl attains ABSENT and BLIND, and B-ct attains ABSENT and BLIND: `ABSENT[𝓘; B-pl; H-cur (declared)]` and
`ABSENT[𝓘; B-ct; H-cur (declared), H-2s (declared), H-ret]` in all three variants. `union_clause_reached` is false in
every branch: B-pl and B-ct have non-positive rows; in SF-3, B-eq is pending (Q3), and in SF-3f and SF-3g it has
non-positive rows.

**Cases covered.** Positive (row 9 in SF-3f), blind (`u_c[0000]` in all three branches, `u_c[0010]` in B-eq and B-ct),
absent (`π_0` in B-pl and B-ct, and others), weak values that are neither 0 nor 1 (`1/4`, `1/3`, `1/2`), a W-certified
branch, a cross-time branch through `φ^{−1}`, H-sel content, pending, and UNDECIDED(G6). The toy's zero state `0000` is a
fixed point, so `u_c[0000]` is its `δ_0`, on which PR-CR6′ runs.

## 5. Interface negatives NF-1 to NF-7

Each is paired with a control that differs only in the defect and must exit 0 with the expected output. Each negative
must exit 2 and leave `<out>` exactly as it was before the run: empty, or, for NF-4, holding only the file placed there
(A1 §4: nothing is written on a nonzero exit).

| Id | Programs | Defect | Exit | Control |
|---|---|---|---|---|
| NF-1 | A | `--fixture SF-2a`: a B-only id | 2 | B, same command |
| NF-2 | A, B | SF-1a input with `0000 → 0010`, `0001 → 0000`, `0010 → 0001`: still a permutation, but not the pinned bytes | 2 | unmodified input |
| NF-3 | A, B | `--stage members` added | 2 | without it |
| NF-4 | A, B | `--out` holds a file | 2 | empty `--out` |
| NF-5 | A, B | `--fixture SF-1b` with SF-1a's input | 2 | `--fixture SF-1a` |
| NF-6 | A, B | id `SF-9`, not in the frozen table | 2 | SF-1a |
| NF-7 | A, B | `--input` names no file | 2 | SF-1a |

## 6. SF-M: synthetic analogues of the §11.3 mutations

Each analogue applies its operations (JSON paths, `A1-fixtures.json` `analogues`) to the named output: to both A's and
B's (`A+B`), so that A/B agreement holds and the content check is reached, or to one program's only. The named check
must fail; a check marked "refused" must report refused. CC-PART′'s sub-tests (p1) to (p7) are those of A1 §7. Before any analogue, every check named in this table is run on
the unmutated outputs of the same fixture and must pass: that is each analogue's paired control. The primed checks are
`controls.py`'s own checks (A1 §11.2), applied to fixture outputs.

| §11.3 | Analogue | Fixture | Operation | Must fail |
|---|---|---|---|---|
| MU-1 | AN-1 | SF-3 | delete row 22 (`u_c[0111]`, B-ct) | CC-ROWS′; CT-INC′ refused |
| MU-2 | AN-2 | SF-3 | duplicate row 2 | CC-ROWS′ |
| MU-3 | AN-3 | SF-1b | exchange `0111` and `1000` between the cycles of `0000` and `0110`: sizes, keys, sortedness and coverage stay valid | CC-PART′ (p3, closure: `φ(0000) = 0111` leaves the set) |
| MU-4 | AN-4 | SF-1a | drop `1011` from the 6-cycle; size 5; histogram adjusted | CC-PART′ (p1, p2) |
| MU-4 | AN-4s | SF-3 | drop `0101` from `u_c[0001]`; size 2; histogram adjusted | CC-PART′ (p1, p2); CT-INC′ refused |
| MU-5 | AN-5 | SF-3 | row 0 `weak[""]` := `"0.5"` | EXACT′ |
| MU-6 | AN-6 | SF-3, A only | row 12 `weak["00"]` := `"15/16"` (changed by `1/16 = 1/|S|`) | AB′, EXPECTED′ |
| MU-7 | AN-7 | SF-3 | exchange rows 2 and 3 | CC-ROWS′ |
| MU-7 | AN-7m | SF-1b | exchange members 2 and 3 | CC-PART′ (p7, member order) |
| MU-8 | AN-8 | SF-3 | `region.E` := `["x_1"]` | PR-E′ |
| MU-9 | AN-9 | SF-3 | row 0's G4 and `token` := `BLIND[π_0; B-pl; H-cur (declared)]` | TOKENS′ |
| MU-10 | AN-10 | SF-3 | `union_clause_reached["B-pl"]` := `true` | PR-CR6′ |
| MU-11 | SF-3g | SF-3g | input variant: the note's token differs | row 9's G6 is `UNDECIDED(G6)` in both outputs, and the output equals its expected bytes |
| MU-13 | AN-13 | SF-3 | row 18 `pi0_ref["00"]` := `"1/3"`, one byte, in both outputs | EXPECTED′ (AB′ passes) |
| MU-17 | AN-17 | SF-3 | row 10 (`u_c[0000]`, B-eq) recorded as passing G5 and pending | PR-CR6′ (strict, Q26) |
| MU-C2 | SF-2pb | SF-2pb | input variant: wrong `φ^{−1}` | CC-BIJ′ on both outputs |
| MU-C3 | MU-C3′ | SF-3 | the frozen MU-C3 patch applied to a temporary copy of A | A exits 3 |
| — | AN-CYC | SF-2p, B | `cycles["4"]` := 2 in `fixture-cyc2.json` | CC-CYC2′ |
| — | AN-MASS | SF-3 | row 9 `mass["00"]` := `"1/2"` | CC-MASS′ |
| — | AN-MO | SF-1a | merge the 2-cycle and the 3-cycle into one entry keyed `0001` | CC-PART′ (p4, single orbit) |
| — | AN-KL | SF-1b | key of the 4-cycle `0010` := `0100` | CC-PART′ (p6, least key) |
| — | AN-US | SF-1b | states of `0000` in walk order | CC-PART′ (p5, sorted) |
| — | AN-DS | SF-1a | `0010` added to the fixed point `0000` | CC-PART′ (p1, each state once) |

**No synthetic analogue, with the reason:**
- **MU-12** (an S0 outcome `fail`): the eleven S0 controls are defined only at the instance (`K` §6); a fixture has none.
- **MU-14a to MU-14d** and **MU-16a to MU-16c**: they test refusals that depend on the record directory's git state,
  `members.json`'s pin or the strict validation of `class-decisions.json` and `adversarial.json`. The fixture route reads
  none of these files, and a malformed fixture input is refused by the digest table before any validation, so a synthetic
  analogue could not tell the two refusals apart and would pass vacuously.
- **MU-C1** (A with `T = 2`) and **MU-C2** (B with a wrong `φ^{−1}`) as code patches: they change instance constants,
  which the fixture route does not read, since there `T` and `φ^{−1}` are inputs. CC-BIJ's detection is exercised by
  SF-2pb.
- **MU-15a to MU-15c** (render inputs): the synthetic profile has no checks files or digests (A1 §9); RN-1 to RN-9 cover
  the projection's own refusals.

## 7. Render, marker and adversarial-index fixtures

**RF-1** projects SF-3f's expected output; its expected fragment is `A1-fixtures.json` `render_fixtures[0].fragment`,
39 lines joined by LF with one final LF. The rows are the 27 tokens of §4 in row order, then the three class tokens of
§4.6, in A1 §9's layout. **RF-2** projects SF-3g: RF-1's fragment with line 13 (0-based) replaced by
`` | B-eq | `π_0` | `UNDECIDED(G6)` | `` and line 35 by `` | B-eq | `UNDECIDED(G6)` | ``.

**RN-1 to RN-9** (outcome `refused`, reason as listed, no fragment):

| Id | Source and change | Reason |
|---|---|---|
| RN-1 | SF-3f with row 9 and B-eq's class token `pending` | `INCOMPLETE_TOKENS` |
| RN-2 | SF-3f with B-pl's union flag `true` and class token `null` | `UNION_REACHED` |
| RN-3 | SF-3f with a backtick appended to row 0's token | `BAD_SCHEMA` (grammar) |
| RN-4 | SF-3f without row 22 | `BAD_SCHEMA` (inventory) |
| RN-5 | SF-3f with row 2 duplicated | `BAD_SCHEMA` (inventory) |
| RN-6 | SF-3f with rows 2 and 3 exchanged | `BAD_SCHEMA` (order) |
| RN-7 | SF-3f with row 0's token naming B-eq | `BAD_SCHEMA` (token does not match its row) |
| RN-8 | SF-3f with B-pl's union flag `true` and its class token kept | `BAD_SCHEMA` (Q4: a reached union has a `null` class token) |
| RN-9 | SF-3 (stage `rows`) | `BAD_SCHEMA` (render reads a final table) |

**RM-0 to RM-5.** The document is `"# result\n\n"`, RF-1's fragment, then `"\nProse.\n"`. RM-0 is unchanged and must
match. Each of the others must not: RM-1 removes the begin marker line; RM-2 adds a second end marker line after the
first; RM-3 exchanges the begin and end marker lines; RM-4 turns every LF inside the fragment into CRLF; RM-5 changes
one byte (`B-pl` to `B-pk` in B-pl's class token).

**AI-0 to AI-7** (ADV-INDEX, A1 §10, on SF-3f, whose only row passing G5 is `π_0` in B-eq). AI-0 is the valid record:
one entry `{branch "B-eq", member "pi0", token, note "derivations/adversarial-B-eq.md"}`, and a B-eq note
`"pi0\n\nNote body.\n"`; it must pass. Each of the others must fail: AI-1, an empty index; AI-2, an extra key `0000`;
AI-3, a note file for B-pl, which has no row passing G5; AI-4, the entry naming the B-pl note; AI-5, an extra entry for
`0000`; AI-6, no blank line after the index, so `Note body.` is read as a key; AI-7, no note file.
