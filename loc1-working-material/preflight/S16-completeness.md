# S16: completeness of the pruned search (written argument [W])

This is a written argument, not a kernel proof. It concerns the engine `c21_engine.py`
(sha256 `28a6a538245a250f7e4aa80957f9e420d191a38461e3cfc02955f5da7f5dd6fc`), run through
`Engine(mats, m, n, rules="RWVP", order=..., arith="modp" or "exact").run(mode, budget)` with
`mut=None`. The frozen rules are `RWVP`; since each rule is shown necessary separately, the
conclusion holds for any subset of them as well. Line numbers `c21_search.out:N` refer to the
preflight output with sha256
`f09b4840c2471d27ab601a7029fd3bce07cd17c921da8b79ce44fb3350010a9d`.

## 1. Statement

**Theorem.** Let the targets `M_1, …, M_K` be `N × N` matrices with integer entries, `N = m n`, and
suppose every nonzero entry is nonzero modulo `PR = 2⁶¹ − 1` (the engine asserts this). Call a
bijection `σ : Fin N → Fin m × Fin n` a *solution* if every `M_k^σ` is a Kronecker product. If a run
ends without exhausting its budget, then:

1. in mode `all` (status `ALL`), the returned list holds exactly one representative of every class
   of solutions, and nothing else;
2. in mode `exist`, status `NONE` means that no solution exists, and status `FOUND` returns a
   solution.

Status `EXHAUSTED` decides neither existence nor non-existence.

Rational targets are covered after scaling by a common denominator: `λM` is a product under `σ`
iff `M` is, for `λ ≠ 0`. Section 6 states what the theorem does not cover.

## 2. Setting

Grid point `(a, b)` has index `g = a n + b`, and `M^σ[σ(i)][σ(j)] = M[i][j]`. The reshuffle of
`M` under `σ` is the `m² × n²` matrix

    R[(a, a')][(b, b')] = M[σ⁻¹(a, b)][σ⁻¹(a', b')],

with row index `a m + a'` and column index `b n + b'`.

**PC.** `M^σ = A ⊗ B` for some `A` (`m × m`) and `B` (`n × n`) iff `rank R ≤ 1`. Indeed
`(A ⊗ B)[(a,b)][(a',b')] = A[a][a'] B[b][b']`, so `R = vec(A) vec(B)ᵀ`; conversely `R = x yᵀ`
gives `A[a][a'] = x_{(a,a')}` and `B[b][b'] = y_{(b,b')}`.

**The class group** `G` is `S_m × S_n` acting by `σ ↦ (π₁ × π₂) ∘ σ`, together with, when
`m = n`, the swap `(a, b) ↦ (b, a)`.

**Lemma 1 (solutions are unions of classes).** If `σ` is a solution, so is `g σ` for every
`g ∈ G`. Relabelling gives `M^{gσ} = (P₁ ⊗ P₂) M^σ (P₁ ⊗ P₂)ᵀ = (P₁ A P₁ᵀ) ⊗ (P₂ B P₂ᵀ)`, and the
swap permutation `S` gives `S (A ⊗ B) Sᵀ = B ⊗ A`.

## 3. Symmetry breaking: one representative per class

The static order `ord` is a permutation of `Fin N` computed in `Engine.__init__` from the targets
alone (`_order`: `"nat"`, an explicit list, `"rare"` or `"greedy"`), before the search, and is not
changed during it. For `σ` put `s₁(d) = σ₁(ord[d])` and `s₂(d) = σ₂(ord[d])`, `d = 0, …, N − 1`.

A sequence is a *restricted growth string* (RGS) if `s(0) = 0` and
`s(d) ≤ 1 + max_{e<d} s(e)` for every `d > 0`. Call `σ` *canonical* if `s₁` and `s₂` are RGS
and, when `m = n`, `s₁ <_lex s₂`.

**Lemma 2.** Every class contains exactly one canonical `σ`.

*Proof.* Each of the `m` first coordinates occurs in `s₁`, `n` times each, because `σ` is a
bijection. A relabelling `π₁ ∈ S_m` turns `s₁` into an RGS iff it sends the label that occurs
`k`-th for the first time along `ord` to `k`; since all `m` labels occur, exactly one `π₁` does so.
The same holds for `s₂` and `π₂`, independently. So each `S_m × S_n`-orbit contains exactly one
`σ` with both sequences RGS.

When `m = n`, the swap exchanges `s₁` and `s₂` and preserves the RGS property, so the `G`-orbit
contains exactly two such `σ`, with sequence pairs `(s₁, s₂)` and `(s₂, s₁)`. They are distinct:
`s₁ = s₂` would put every index on the diagonal `{(a, a)}`, which has `m < m²` points. Exactly one
of them has `s₁ <_lex s₂`. ∎

**Lemma 3 (the unpruned tree).** Ignore pruning: let `place` accept every candidate. Then the
leaves of the depth-first search in `_dfs` are exactly the canonical bijections, each reached
once.

*Proof.* At depth `d` the engine assigns index `ord[d]`. `candidates(d)` returns the unused grid
points `(a, b)` with `a < min(ru + 1, m)` and `b < min(cu + 1, n)`, where `ru` and `cu` count the
distinct first and second coordinates used so far (`_commit_state`), and, when `m = n` and the
prefixes of `s₁` and `s₂` are equal (`eq`), with `a ≤ b`; `eq` is cleared at the first `a < b`.

- The unused-point test makes every leaf a bijection.
- `a ≤ ru` with `ru = 1 + max` of the prefix is exactly the RGS condition at position `d`, and
  likewise for `b`. At `d = 0` it forces `(0, 0)`.
- While the prefixes agree, `a > b` would make `s₁ >_lex s₂`; it is refused. At the first
  `a < b`, `s₁ <_lex s₂` holds for every continuation. A complete leaf has `s₁ ≠ s₂` (Lemma 2), so
  every leaf has `s₁ <_lex s₂`.

So every leaf is canonical. Conversely the point `(s₁(d), s₂(d))` of a canonical `σ` passes each
of these tests at the node of its own prefix, so its path is offered. Distinct leaves are distinct
paths. ∎

The representatives are therefore pairwise inequivalent by construction, and no deduplication by
the class group is needed. `c21_search.py` checks it on every run (`canonical(σ) = σ` and
distinctness, `res["distinct"]`). Measured confirmations: K-canon finds `N!/|G|` classes of the
identity on `2×2`, `2×3`, `3×2`, `2×4`, `4×2` and `3×3` (3, 60, 60, 840, 840 and 5040;
`c21_search.out:3`, `:14`, `:25`, `:36`, `:47`, `:58`), and `c21_replay.py` compares the engine's
class lists with a brute force over all `N!` bijections on 42 shapes with `N ≤ 9`.

## 4. Pruning: each rule is a necessary condition

Fix a node with partial assignment `τ` (the assigned indices and their grid points). An entry
`R_k[r][c]` is *known* when both of its grid points hold assigned indices; in every completion
`σ ⊇ τ` it has that value. `place(i, a, b)` returns `False` only when one of the conditions below
fails for `τ` extended by `i ↦ (a, b)`.

**Lemma 4.** Let `σ` be a solution extending `τ`, and `k` a target, so `R_k = x yᵀ`. Then:

- **(N1) Support.** No known zero `R_k[r][c]` has a known nonzero in row `r` and a known nonzero
  in column `c`. A nonzero in row `r` gives `x_r ≠ 0`, one in column `c` gives `y_c ≠ 0`, and then
  `R_k[r][c] = x_r y_c ≠ 0`.
- **(N2) Cycle consistency.** The system `z_r = R_k[r][c] · z_c`, one equation per known nonzero
  entry, over unknowns indexed by the rows and the columns of `R_k`, has a solution with every
  unknown nonzero: `z_r = x_r` and `z_c = 1/y_c`, both nonzero by the reasoning of N1.
- **(N4) Partner.** If row `r = (a, a')` and column `c = (b, b')` each hold a known nonzero, then
  `R_k[r][c] ≠ 0` by N1's reasoning, that is, `M_k[σ⁻¹(a,b)][σ⁻¹(a',b')] ≠ 0`. If `(a, b)` holds
  an assigned index `j` and `(a', b')` is free in `τ`, the index `σ` places there is unassigned in
  `τ`, so `j` has an unassigned `j'` with `M_k[j][j'] ≠ 0`. The same holds with the roles of the two
  points exchanged, for `M_k[j'][j]`.
- **(N3) W-COL family.** Call `f : Fin N → ℚ` *product-form for `M_k`* if every solution `σ`
  makes `f(σ⁻¹(a, b)) = u(a) v(b)` for some `u`, `v`. For such `f`, the grid matrix
  `F(a, b) = f(σ⁻¹(a, b))` has every `2 × 2` minor zero and *product support*: no zero `F(a, b)`
  has a nonzero in its grid row and a nonzero in its grid column. Both hold on the assigned
  points, which is what N3 tests.

The functions the engine uses are product-form. With `M_k^σ = A ⊗ B`, `σ(i) = (a, b)` and, for
fixed `j`, `σ(j) = (a', b')`:

| function of `i` | value | rule letter |
| --- | --- | --- |
| `M_k[i][j]`, each `j` | `A[a][a'] B[b][b']` | W |
| `M_k[j][i]`, each `j` | `A[a'][a] B[b'][b]` | W |
| `M_k[i][i]` | `A[a][a] B[b][b]` | V |
| `#{j : M_k[i][j] ≠ 0}` | `#{a' : A[a][a'] ≠ 0} · #{b' : B[b][b'] ≠ 0}` | V |
| `Σ_j M_k[i][j]` | `(Σ_{a'} A[a][a'])(Σ_{b'} B[b][b'])` | V |
| `Σ_j M_k[i][j]²` | `(Σ_{a'} A[a][a']²)(Σ_{b'} B[b][b']²)` | V |
| the same three for column `i` | the transposed products | V |

Each component is product-form for its own target, and a solution makes every target a product,
so every component of the concatenated profile is product-form. ∎

**Lemma 5 (the code tests these conditions and nothing stronger).**

- *N3* (`place`, before any state change). For each assigned point `(a, b₂)` of row `a`, holding
  `i₂`, and `(a₂, b)` of column `b`, holding `i₃`, with `(a₂, b₂)` assigned and holding `i₄`, it
  compares `PV[i][i₄]` with `PV[i₂][i₃]`, the componentwise products `f(i) f(i₄)` and
  `f(i₂) f(i₃)`: the `2 × 2` minor with the new point as a corner. Every minor among assigned points is tested when its last corner is placed. The three
  bitmask tests on `NZP`, `GR` and `GC` are product support for the new point and for the points of
  its row and its column, which are the only points whose row or column masks change.
- *N1, N2* (`_r_add`). For the new index `i` at `(a, b)` it adds the known entries
  `R[(a,a)][(b,b)] = M[i][i]` and, for each assigned `j` at `(a₂, b₂)`,
  `R[(a,a₂)][(b,b₂)] = M[i][j]` and `R[(a₂,a)][(b₂,b)] = M[j][i]`. Each entry with both points
  assigned is added once, when its later point is placed. A zero entry is tested against the
  rows (`NZR`) and columns (`NZC`) holding a known nonzero. A nonzero entry marks its row and
  column, tests the known zeros of that row against `NZC` and of that column against `NZR`, and is
  added to a weighted union-find over the `m² + n²` rows and columns as `z_r = v · z_c`. With
  weights `w[x] = z_x / z_root(x)`, a constraint inside one component holds iff
  `w[u] = val · w[v]`, and a union rescales the smaller component by the exact factor; so the
  union-find rejects exactly the inconsistent systems of N2.
- *N4* (`_partner`), for every assigned index including the new one and for both orientations.
  `LA[a] & LB[b]` is the set of points `(a', b')` whose row `(a, a')` and column `(b, b')` hold
  known nonzeros, `free` the unassigned points, and `NZr[j] & UA` (`NZc[j] & UA`) the unassigned
  partners of `j` as left (right) point.
- *State.* Every change to the search state after the N3 tests is preceded by an undo record
  (types 0 to 3), and `undo(mark)` pops them in reverse order. A rejected placement and a finished
  subtree therefore restore the state exactly, and the tests at a node depend only on that node's
  partial assignment. Whether a constraint system is consistent does not depend on the order in
  which its equations were added.

A rule may fail to reject a prefix that has no solution; that costs nodes and never a class,
since the leaf test is exact. Measured confirmations: K-ablation returns the same class set with
rules `RWVP`, `RWV`, `RW`, `R` and `RP` on five instances, and with `WV` on the four planted
ones (29 controls, `c21_search.out:384`–`:448`); each of the six engine mutations, including a strengthened support
rule (`MUT-SUPPORT-STRONG`) and a broken symmetry breaker (`MUT-NOLEX`, `MUT-LEX-ALWAYS`,
`MUT-SECOND`), is detected (`c21_search.out:457`–`:462`).

**N2 over images modulo `PR`.** `arith="modp"` runs N2 on images in `F_PR`. `PR = 2⁶¹ − 1` is prime
(checked by a Miller–Rabin test with the twelve prime bases 2 to 37, which is deterministic
below `3.18 × 10²³`). The engine asserts that no nonzero entry has image 0, so no nonzero entry is
divisible by `PR`. Every weight and every union factor is a ratio of products of nonzero entries.
It therefore lies in the localization `ℤ_(PR)` and is a unit there, and reduction
`ℤ_(PR) → F_PR` is a ring homomorphism. By induction over the union operations, each stored
weight is the image of the exact weight (`pow(·, PR − 2, PR)` inverts a nonzero element). An exact
equality `w[u] = val · w[v]` therefore holds for the images too, so no consistent system is
rejected. An exact inequality whose images agree weakens pruning and leaves completeness intact.
K-collision shows that such a collision is reachable and harmless: an entry raised by `PR` passes
every modulo-`PR` test at the planted leaf, and the exact leaf test rejects it
(`c21_search.out:453`). K-arith: exact and modulo-`PR` N2 return the same class sets on five
instances (`c21_search.out:396`, `:410`, `:424`, `:438`, `:450`).

## 5. Proof of the theorem

Let `C` be a class of solutions and `σ_c` its canonical member (Lemma 2), a solution by Lemma 1.
By Lemma 3 its path is offered at every depth. Every prefix of `σ_c` has the completion `σ_c`,
which is a solution, so by Lemmas 4 and 5 `place` accepts every step. The depth-first search
therefore reaches the leaf `σ_c` unless the budget stops it first, or, in mode `exist`, an earlier
leaf is accepted. At the leaf, `leaf_ok` applies PC to every target in exact integer arithmetic,
with the first nonzero entry `R[p][q]` as pivot: `R` has rank at most 1 iff
`R[r][c] R[p][q] = R[r][q] R[p][c]` for all `r`, `c`, and a zero `R` passes. `σ_c` passes.

`tested` is incremented once for each offered candidate, before `place`, and the run raises
`BudgetOut` as soon as it exceeds `budget`. A run that ends with `ALL` or `NONE` has therefore
visited the whole pruned tree within `budget` tested nodes. With `ALL`, every class has its
representative in the list, and every listed `σ` passed the exact leaf test and is a distinct
canonical representative (Lemma 3). With `NONE`, no leaf was accepted, so no class of solutions
exists. With `FOUND`, the accepted leaf passed the exact leaf test. ∎

## 6. What the argument does not cover

1. **Entries in `ℚ(ζ₁₆)`.** `Engine.__init__` converts every entry with `int()`, so the engine as
   measured accepts integer entries only, and the preflight ran it on nothing else. `C21`'s lifts
   have entries in `ℚ(ζ₁₆)` (`H_i`, `F₁₆`, `W_d`). The argument carries over verbatim to an engine
   whose arithmetic layer satisfies:
   - **E1.** Every zero test, every product compared by N3 and every product in the leaf test is
     exact in `ℚ(ζ₁₆)`, with equality decided on a unique normal form (the power basis
     `1, ζ, …, ζ⁷` over `ℚ`, `ζ⁸ = −1`).
   - **E2.** N2 runs on images under a ring homomorphism `ρ : ℤ[ζ₁₆]_𝔭 → F_p`, with `p ≡ 1 (mod 16)`
     prime, `ζ ↦ ω` a primitive 16th root of unity modulo `p`, and `𝔭 = ker ρ`. No denominator of
     any entry is divisible by `p`, and the engine asserts `ρ(x) ≠ 0` for every nonzero entry
     `x`. Under this assertion every nonzero entry is a unit at `𝔭`, and Section 4's argument holds
     with `ℤ_(PR)` replaced by `ℤ[ζ₁₆]_𝔭`.
   - **E3.** The static order is a permutation computed from the targets before the search. Any
     total order on normal forms may replace integer sorting in `_order`; the order affects cost
     only.
   - **E4.** The symmetry breaking, the four rules, the leaf rule, the budget and the undo
     records are the frozen code's, with only the arithmetic replaced.

   Until a layer meeting E1 to E4 is implemented and its controls pass, the theorem does not
   apply to `C21`'s targets. The preregistration states the consequence and the controls
   (K-arith-16, and K-engine rerun on the extended engine).
2. **The mapping from search status to verdict.** The theorem decides whether some `σ` makes every
   target of a set a Kronecker product. The step from that answer to SEP-PHYS, ADMITTED or REL
   (W-EQ1u, §3.3 and §3.4 of the preregistration) is outside it.
3. **The mutations and `knuth()`.** `mut` is `None` in every run the argument covers. `knuth()` is a
   seeded estimator of tree size and decides nothing.
4. **Entries of absolute value at least `PR`.** The guard is the assertion, not a bound on the
   entries: an entry not divisible by `PR` is a unit at `PR` whatever its size.
