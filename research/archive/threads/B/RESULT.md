# Thread B — RESULT: NOT-conjugacy reduction and three-copy consistency

Base: `wt-threads` at `4507b0259e7d04095c1b506359163e71b22e2871`, read-only. Scripts and outputs are in this directory:

- `blib.py` — exact sparse linear algebra.
- `part1_conjugacy.py` → `part1_conjugacy.out` (22 checks, OK).
- `part2_three_copy.py` → `part2_three_copy.out` (28 checks, OK).
- `explore_t4.py`, `explore_m2.py` → `*.out` (floating-point exploration only).

Every claim of identity, rank, sign or conjugacy below is exact (`Fraction`, or sympy surds in 1c).

**Notation.** A ball NOT is an orthogonal involution fixing `u` with `Nz = −z`. `H` is the frame stabiliser: the
orthogonal maps fixing `u` with `gz = ±z`, so `H = O(T) × O(1)`. *Two-NOT reading* means NB-1's hypotheses with
`Rt(N_B)` and `Rc(N_A, N_B)`, where `N_A` is the control copy's NOT and `N_B` the target copy's.

## 1. Finding

**(i) Conjugacy reduction.** The reduction holds as briefed. If `N_B = g N_A g⁻¹` with `g ∈ H` acting on the
*target* copy, then `G̃ = (I⊗g⁻¹)G(I⊗g)` meets `F`, `Rt(N_A)`, `Rc(N_A, N_A)` and `P±`. The `F`, `Rt` and `Rc`
defects transform covariantly for any `G`; `I⊗g` preserves `min` and `max`. A `g` that swaps the corners is allowed
on the target copy and breaks `F` on the control copy. So frozen NB-1 already covers every two-NOT model whose NOTs
have the same split.

**(ii) The split is a complete invariant.** Under `H`, the split `(p, q)` is a complete invariant of conjugacy for
ball NOTs, and it remains complete under the subgroup with `gz = z` and `det g = +1`. It is not complete under
smaller groups such as signed coordinate permutations. The countermodels' NOTs, `(2,2)/(1,3)` at `d = 5` and
`(3,3)/(1,5)` at `d = 7`, have different `±1` eigenspace dimensions. So no invertible linear map conjugates them,
and no local relabelling of either copy matches them. The mismatch is intrinsic to the `J/K` gates: every compatible
coordinate NOT pair has the same mismatched splits. Hence copy naturality, modulo `H`, is exactly *equal splits*.

**(iii) Three copies with pairwise relations alone.** Here each copy carries one role-independent NOT (Model I).
Mismatched splits survive on exactly the role-pure patterns, where no copy is both a control and a target:
- a single edge;
- an out-star, for example `(2,2)` controlling two `(1,3)` targets;
- an in-star.

On these patterns the `J/K` gates meet every pairwise relation, `T1` and `T2`, `G² = I`, and composite positivity
`T4`. Any copy in both roles forces `d ∈ {1, 3}` through the two-NOT reading (target `p ≤ 1`, control `p = q`).
That is already a two-copy fact, so three-copy composition with pairwise relations does **not** source copy
naturality.

**(iv) The chain identity does.** `T3` is the identity `G_BC G_AB G_BC G_AB = G_AC`. On its corner sector it forces
`G_BC` to satisfy `Rc(N_B, N_C)`, where:
- `N_B` is the NOT that `G_AB` itself induces on `B`, which S1 makes a function of the gate: `N_B|_T = M₁M₀⁻¹`;
- `N_C` is the NOT that `G_AC` induces on `C`, which is then also `G_BC`'s own target NOT.

Two consequences follow:
- Under the two-NOT reading, `T3` gives `d ∈ {1, 3}` with no cross-copy identification at all.
- If the target NOT is the same on `B` and `C` (per type), `T3` makes `G_BC` meet frozen NB-1's one-N hypotheses
  verbatim.

The `J/K` Model II (per-type `N^c ≠ N^t`, the same gate on all six ordered pairs) behaves as the lemma predicts at
`d = 5` and `d = 7`. It meets every pairwise relation, `T1` and `T2`, and fails `T3` in both orderings. Its
bidirectional composite `G_BA G_AB` also fails positivity, with value `−1`. The matched `d = 3` complex CNOT
survives every relation.

## 2. Evidence level

| claim | level |
| --- | --- |
| (i) defect covariance of `F`, `Rt`, `Rc` under target-copy conjugation | exact computation (1a: random rational `G`, `d = 3, 5, 7`, every `p`, `g` fixing or flipping `z`), plus a written one-line proof |
| (i) `I⊗g` preserves `min`/`max` for `g` orthogonal with `gu = u` | written (`g` preserves the Lorentz form and `u`, so `g(L) = L`; `gᵀ = g⁻¹` handles the dual), with `g` checked orthogonal and `u`-fixing exactly |
| (i) constructed pairs reduce to one `N` | exact (1b). `d = 3`: complex CNOT, positive. `d = 5`: algebraic one-N model `G₀`, which fails `P` by the exact witness `−12/25`, as NB-1 requires |
| (i) corollary: equal splits ⇒ `d ∈ {1, 3}` | written assembly on frozen NB-1 (its own layers) |
| (ii) completeness of the split under `H` | written proof: an orthogonal involution of `T` is fixed by its orthogonal `±1` decomposition, on which `O(T)` acts transitively for fixed dimensions; a reflection inside `V₊` or `V₋` fixes the determinant. Exact sympy constructions for `d = 2..7`, all `p` (27 cases, 20 with irrational conjugators), with `gz = z` and `det g = +1` |
| (ii) non-conjugacy of the countermodel NOTs | exact ranks (1b′); similarity invariant |
| (ii) mismatch intrinsic to the `J/K` gates | exact exhaustive scan of coordinate-diagonal NOT pairs (256 at `d = 5`, 4096 at `d = 7`). For non-coordinate NOTs, written via the two-NOT reading |
| (iii) necessary conditions (target `p ≤ 1`, control `p = q`) | **written**: the two-NOT reading of NB-1's S1, S2, S4 and S5. The kernel lemmas `p_le_one` and `parity` do not mention `N`. The probe's S1/S2 rows involve only the target NOT (`s2_rows(d, nu)`). Exact (2.3): on the `J/K` models the S1/S2 structure holds with `N_B` and fails with `N_A`, and the `T⊗V₋(N_B)` block is invariant, injective and anticommutes with `N_A⊗I`. The two-NOT S1–S5 assembly is **not** certified anywhere |
| (iii) enumeration of surviving patterns | exact combinatorics over the 63 used-pair sets × all splits (2.1), given the written necessary conditions |
| (iii) existence on role-pure patterns: `R2`, `T1`/`T2`, `G² = I` | exact (2.2), `d = 5, 7`. The group with the local NOTs has order 32, each element being local NOTs × a gate word (exact BFS) |
| (iii) two-copy positivity of each `J/K` gate | NB-1's written reduction, not re-proved here |
| (iii) `T4` on role-pure patterns | exact identity (2.2): the value tensors of `G1`, `G2` and `G2G1` equal `F(invariants)` with **the same** coefficient tensor at `d = 3, 5, 7`, where `d = 3` is the quantum composite. Then written: `F` is affine in each invariant pair, the pairs range over discs whose boundary circles are the `d = 3` configurations, and those are `≥ 0` by quantum theory. Floating-point exploration minimum ≈ `−1e−15` |
| (iv) `T3` corner lemma | written algebra, below. Exact (2.4): corner-sector defect identity at `d = 5, 7`; `D1 = G·D2` at `d = 5, 7`; positive and negative controls at `d = 3` |
| (iv) `J/K` Model II fails `T3`, meets `R2`, `T1`, `T2` | exact (2.4), `d = 5, 7`, all six labelings, both orderings |
| (iv) `J/K` Model II `G_BA G_AB` positivity failure | exact rational witness, value `−1` at `d = 5` and `d = 7`. Specific to this gate and this relative orientation of the control and target frames; **not** a theorem about all Model II gates |

**The `T3` corner lemma, written.** Assume the controlled forms `G_AB(k_a⊗t) = k_a⊗m_a t` and
`G_AC(k_a⊗r) = k_a⊗m′_a r`, which are S1 in the two-NOT reading. Here `m₁ = N_B m₀`, `[N_B, m₀] = 0` (from `Rt`),
and `m′₁ = N_C m′₀`. Applying `T3` to `k_a⊗t⊗r` gives `G(m_a⊗I)G(m_a⊗I) = I⊗m′_a` for `G = G_BC`, `a = 0, 1`.
Then:
1. From `a = 0`: `(m₀⊗I)G = G⁻¹(m₀⁻¹⊗m′₀)`.
2. Substituting into `a = 1` gives `G(N_B⊗I)G⁻¹ = m₀⁻¹N_B m₀ ⊗ N_C = N_B⊗N_C`, that is, `Rc(N_B, N_C)`.
3. Applying this to `k₀⊗t` gives `G_BC`'s own `M₁ = N_C M₀`, so `N_C` equals `G_BC`'s own target NOT.

`G_BC` invertible is needed (`P±`). No exchange or SWAP is used.

## 3. Countermodels and controls

The three-copy relations were stated before any computation, in the docstring of `part2_three_copy.py` and printed
at the head of its output:
- `R2`: NB-1's two-NOT hypotheses for each used ordered pair.
- `T1`: commutation of gates with a common control.
- `T2`: commutation of gates with a common target.
- `T3`: the chain identity, in both orderings.
- `T4`: products of used gates map product states into `max₃`.

Not assumed: SWAP, any exchange, `G_YX` determined by `G_XY`, or any continuous group. Each control and what it
showed:

- **1a countercontrol.** Conjugating the *control* copy by a corner-swapping `g` breaks `F`. The reduction must act on
  the target copy.
- **1b genuineness.** The conjugated `d = 3` and `d = 5` models fail `Rc(N_A, N_A)`, and at `d = 3` also `Rt(N_A)`.
  They are real two-NOT models and not one-N models in disguise.
- **1b `d = 5` positivity.** The algebraic one-N model `G₀` fails `P`, with an exact witness of value `−12/25`. The
  reduction cannot manufacture a positive `d = 5` one-N gate, consistent with NB-1.
- **1b′ mismatch is intrinsic.** Conjugating copy `B` of the `J/K` models moves `N_B` only inside its split class, and
  the reduction returns the original mismatched model.
- **1c countercontrol.** Under the 8 signed coordinate permutations of `T`, a split-`(1,1)` reflection about `x + y`
  is not conjugate to `diag(1, −1)`. Completeness needs all of `O(T)`.
- **2.2 matched countercontrol.** The `d = 3` complex CNOT, with one `N` on every copy and all six ordered pairs,
  meets `R2`, `T1`, `T2` and `T3` exactly, and `T4` by quantum theory. The matched case survives everything.
- **2.4 lemma positive control (`d = 3`).** `G_AB` has a rotated target NOT `N_B ≠ N`, and
  `G_BC = (g⊗I)CNOT(g⁻¹⊗I)`. `T3` holds, and `G_BC` meets `Rc(N_B, N)`.
- **2.4 lemma negative control (`d = 3`).** `G_BC = CNOT(R⊗I)` meets `F`, `P±` and `Rt`, and `Rc` with no tested
  NOT. `T3` fails.
- **2.4 non-uniqueness of the control NOT.** The complex CNOT meets `Rc(N′, N)` for every corner-swapping `N′` of
  split `(1,1)`. `Rc` does not determine a gate's control NOT, while S1 does determine its target NOT. This asymmetry
  is why `T3`, which carries `B`'s target NOT into the control role, is the effective relation.
- **Exploration (floating point, labelled).** Block-descent minima:
  - the out-star, in-star and chain composites at `d = 5`, and every composite at `d = 3`: about `−1e−15`;
  - the `J/K` Model II `G_BA G_AB`: `−1.000`. This led to the exact witness above.

**Open risks.**
- The decisive necessary conditions (iii) and route (iv-a) rest on the two-NOT reading of NB-1, which is written and
  uncertified.
- `T3`, like `Rt` and `Rc`, is the truth-table identity extended off the frame as an operator identity. I did not
  audit the corpus for a source of it.

## 4. Proposed next theorem

- **B1, conjugacy reduction** *(Lean; pure linear algebra)*. Let `G` be a linear map on `V⊗V`, and `g, N_A`
  invertible with `N_B = g N_A g⁻¹`. Put `G̃ = (I⊗g⁻¹)G(I⊗g)`. Then:
  - `(I⊗N_A)G̃(I⊗N_A) − G̃ = (I⊗g⁻¹)[(I⊗N_B)G(I⊗N_B) − G](I⊗g)`;
  - `(N_A⊗I)G̃(N_A⊗I) − (I⊗N_A)G̃ = (I⊗g⁻¹)[(N_A⊗I)G(N_A⊗I) − (I⊗N_B)G](I⊗g)`;
  - if `g` permutes `{k₀, k₁}` by `b ↦ b⊕ε`, then `G̃(k_a⊗k_b) − k_a⊗k_{a⊕b} = (I⊗g⁻¹)[G(k_a⊗k_{b⊕ε}) − k_a⊗k_{a⊕b⊕ε}]`.

  **Corollary** *(written, on frozen NB-1)*: two ball NOTs of equal split ⇒ `d ∈ {1, 3}`.
- **B2, split completeness** *(Lean-able with Mathlib orthogonal complements; written now)*. Two ball NOTs are
  conjugate by some `g ∈ H` with `gz = z` and `det g = 1` iff they have the same split. Without a frame condition, two
  ball NOTs of different split are not similar.
- **B3, NB-1 in its two-NOT reading** *(the kernel lemmas unchanged; exact: the existing probe rows already depend
  only on the target NOT; written: S1, S2 and S4 re-assembled with `Rt(N_B)` and `Rc(N_A, N_B)`)*. Under `F`, `P±`,
  `Rt(N_B)` and `Rc(N_A, N_B)` with ball NOTs `N_A`, `N_B` and `d ≥ 2`: `p_B ≤ 1` and `p_A = q_A`. In addition,
  conditional on S2's block statement `G̃(T⊗E₊) ⊆ T⊗E₊`: `p_B ≥ 1`.
- **B4, role conflict** *(written corollary of B3)*. A copy whose NOT serves both as a target NOT of one native CNOT
  and as a control NOT of another forces `d ∈ {1, 3}`.
- **B5, the `T3` corner lemma** *(Lean; algebra on `V⊗W`, no positivity)*. Let `G` be invertible on `V⊗W`, `N_B` an
  involution commuting with `m₀`, `m₁ = N_B m₀` and `m′₁ = N_C m′₀`. If `G(m_a⊗I)G(m_a⊗I) = I⊗m′_a` for `a = 0, 1`,
  then `(N_B⊗I)G(N_B⊗I) = (I⊗N_C)G`. Together with the corner-sector reduction (`T3` plus the controlled forms of
  `G_AB` and `G_AC` gives the two hypotheses), this is also a Lean candidate.
- **B6** *(written, from B5 + NB-1)*. Three copies with gates `G_AB`, `G_AC`, `G_BC` meeting `R2` and `T3`:
  - (a) with B3: `d ∈ {1, 3}`, with no cross-copy identification;
  - (b) without B3: if the target NOTs induced on `B` and `C` coincide (per type), `G_BC` meets frozen NB-1's one-N
    hypotheses, so `d ∈ {1, 3}`. If they have equal splits, use B1 first.

  The countercontrol to carry is the `d = 3` complex CNOT, which meets every hypothesis.
- **Negative, to state as scope.** Under Model I, with pairwise relations and `T1`, `T2` and `T4` on role-pure
  patterns, mismatched splits are consistent at `d = 5` and `7` (`J/K` out-star and in-star). Three-copy composition
  without `T3` or role conflict does not supply copy naturality.

## 5. Dependencies

- **Other threads.** None used. B3 is the shared need of any thread that relaxes NB-1's one-N premise.
- **Corpus, at `4507b025`.**
  - `verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/preregistration.md`:
    - setting and hypotheses: 178–196;
    - S1: 204–208 (`M₁ = N M₀` is the step B3, B5 and B6 rely on);
    - S2: 209–212;
    - S4: 216–220;
    - S5: 221–223;
    - the two-NOT remark: 241;
    - Hazard 2, the unsourced identical-copy covariance: 73–96.
  - `verification/lean-mathlib/OIBridge/NativeGateBall.lean`: `p_le_one` 176, `parity` 194, `blocks_vanish` 149,
    `dim_of_bounds` 248, `nb1_kernel_core` 255.
  - `verification/lean/native_gate_ball_probe.py`: `s2_rows` 144 (N-dependence through the target `nu` only), the S4
    check 288, C2N 464.
  - `k-infinity/two_not_d7.py`, the `d = 7` `J/K` data, reused here.
- **Unsourced premises.**
  - The two-NOT reading of S1–S5 (written, uncertified).
  - `T3` as an operator identity (not audited in the corpus).
  - For B6(b): per-type identity of the target NOT.
  - For B1 and B2: that the admissible relabellings include all of `H`. The spectral non-conjugacy needs no such
    premise.
  - Positivity of the `J/K` gates themselves: NB-1's written reduction.
