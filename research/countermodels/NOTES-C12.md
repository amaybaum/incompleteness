# NOTES-C12 — Conjecture C8-C at four members; the non-Bell pair theorem

Node C12 (round 3). Conventions as in NOTES-C8 and NOTES-C11: defects in matrix normalization `d = I − cP_h`,
`c ∈ (1, 2]` (`c = 2`: Bell-type, `h` maximally entangled); open cap `U = {v : |⟨h|v̂⟩|² > 1/c}`, open co-cap
`W = {v : |⟨h|v̂⟩|² > 1 − 1/c}`; `K(Z) = (Q3 ∩ Z*) + cone Z`; for a Bell set, the **non-orthogonality graph** has the
defects as vertices and an edge `j–k` iff `⟨g_j|g_k⟩ ≠ 0`; `N_i` the neighbours of `i`, `O_i` the members orthogonal to
`g_i`. The witness lemma C8-L (NOTES-C8, audited) is used as stated. Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of any C12 script (2026-10-11T00:35:34Z, `date -u`)

Scratchpad exploration before this point was numerical and is not evidence: the boundary-cover measure `μ(s)`
(fraction of a Bell cap's boundary inside another closed Bell cap at squared overlap `s`; found `< min(s, 1/2)`), a
search for Gaussian-integer Bell vectors realizing each of the ten orthogonality patterns of four members, the witness
constructions below on those and on 3000 random four-member sets (no failure), and integer witness points for the exact
instances.

1. **Pair theorem for rank-one defects (all `c₁, c₂ ∈ (1, 2]`).** `K({d₁, d₂})` is self-dual iff `⟨d₁, d₂⟩ = 0` (only for
   two orthogonal Bell-type defects: Theorem S) or `c₁c₂|⟨h₁|h₂⟩|² ≥ (√(c₁ − 1) + √(c₂ − 1))²` ((CC), Theorem S′). When the
   inequality fails, `y = P_v + λd₂` with `v` near the far edge of the cap of `d₁` is in `K* \ K`, exactly. With
   `c_i = 1 + r_i²` the threshold is `s* = (r₁ + r₂)²/((1 + r₁²)(1 + r₂²))`, attained by `h₂ ∝ (r₁ + r₂, 1 − r₁r₂, 0, 0)`
   against `h₁ = (1, 0, 0, 0)`: exact instances below, at, and above the threshold for `(r₁, r₂) ∈ {(1/2, 1/2), (1/3, 1/3),
   (3/4, 3/4), (1/10, 1/10), (1/2, 3/4), (1, 1/2)}` (the last is a Bell defect with a non-Bell one), and the Bell pair
   `(1, 1)`, whose threshold `s* = 1` reproduces C4.1. This is C4.4's "first non-Bell multi-defect class", settled.
2. **Boundary witness (BW).** For a finite Bell set, a vertex `i` with a neighbour `k`, and a point `v` with
   `|⟨g_i|v̂⟩|² = 1/2` and `|⟨g_l|v̂⟩|² < 1/2` for every `l ≠ i`: moving `v` slightly into the cap of `i` and taking
   `y = P_v + λd_k` (`⟨y, d_i⟩ = 0`) gives `y ∈ K* \ K` whenever (L4) holds for `O_i` at `x = Π_{v⊥}g_k`. Tools:
   (A) such a `v` exists at every `i` whose neighbours do not span `ℂ⁴` (explicit construction); (B) (L4) holds
   automatically for every `m ∈ O_i` orthogonal to `k`; (C) one `m ∈ O_i` not orthogonal to `k` is handled by placing `v`
   near `(e^{iθ}g_i + g_m)/√2` (then `|⟨g_m|x̂⟩|² ≤ 1/2`, strictly unless `g_k ∈ span(g_i, g_m)`).
3. **C8-C at four members: proved.** Every four-member Bell set with a non-orthogonal pair has a vertex where A + B or
   A + C applies (all ten orthogonality patterns checked: K2+2K1, 2K2, P3+K1, K3+K1, P4, K1,3, C4, paw, diamond, K4; the
   only degenerate case, C4 with all four vectors in one 2-dimensional span, is C8's Bell-circle case); so **no
   four-member non-orthogonal Bell set is self-dual** — CONDITIONAL on the written argument [W]. Exact witnesses (C8-L
   verified exactly) for one Gaussian-integer instance of each pattern, the K4 instance being in C8's open class (four
   linearly independent vectors: for every admissible `(g₁, g₂)` the other two have independent `W^⊥`-projections).
4. **Every finite Bell set without orthogonal pairs is not self-dual** (any size `≥ 2`), by the boundary-of-union
   argument (the dimension count of NOTES-C3 Lemma 3): the union of the open caps has a 5-dimensional boundary, the
   pairwise intersections of cap boundaries are 4-dimensional, so some boundary point lies on exactly one cap boundary
   and outside every other closed cap; BW applies with `O_i = ∅`. More generally the same holds whenever the
   non-orthogonality graph has a complete component of size `≥ 2`. Exact instances: six and eight members, no
   orthogonal pair, every vertex's neighbours spanning `ℂ⁴` (Tool A unavailable), with exact witnesses.
5. **Residual (predicted OPEN).** C8-C for finite Bell sets with five or more members in which every non-trivial
   component has an orthogonal pair and no vertex is tool-applicable; closed infinite Bell sets beyond C7.6's circle;
   for `c < 2`, necessity of (CC) for three or more defects (a boundary point of the union of caps can lie inside every
   co-cap, so the BW route does not transfer).
6. No self-dual non-orthogonal Bell set is found, so no FAILED-prediction row for C8-C is expected.

(Runs, results and the written proofs follow below this line after the runs.)

## Runs (written 2026-10-11T00:39Z, `date -u`)

| script | runs | final | replay |
|---|---|---|---|
| `c12_pairs_bellsets.py` | 1 (00:37:49Z) | 9/9, `VERDICT C12-PAIRS-BELLSETS-EXACT` | identical (out `363c9899…`) |

Pre-run edit (before the first run): countercontrol CC3's rank test (a determinant including `e₀` does not test membership
in a span) replaced by the construction's own span statement plus `det = 0`. The instance data (Gaussian-integer
parameters and witness points) were found in the scratchpad by a numerical search and are hard-coded; every claim rests on
the exact checks.

## Results

### C12-P — the pair theorem for rank-one defects [W + X P1, P2, CC2]
**Theorem C12-P.** *Let `d_i = I − c_iP_{h_i}`, `c_i ∈ (1, 2]`, `h₁, h₂` distinct rays, `s = |⟨h₁|h₂⟩|²`. Then
`⟨d₁, d₂⟩ = 4 − c₁ − c₂ + c₁c₂s ≥ 0`, with equality only for two orthogonal Bell-type defects, and `K({d₁, d₂})` is
self-dual iff either `⟨d₁, d₂⟩ = 0` or `c₁c₂s ≥ (√(c₁ − 1) + √(c₂ − 1))²`.*
*Proof.* The zero-pairing case is Theorem S. Let `⟨d₁, d₂⟩ > 0`. With `cos²θ_i = 1/c_i`, `cos²θ₁₂ = s`, the cap of `d_i` is
the open Fubini–Study ball of radius `θ_i` about `h_i` and its co-cap the open ball of radius `π/2 − θ_i`; (CC) for the
ordered pair `(1, 2)` is `θ₁₂ + θ₁ ≤ π/2 − θ₂`, which is symmetric and equivalent to `cos θ₁₂ ≥ sin(θ₁ + θ₂) =
(√(c₁ − 1) + √(c₂ − 1))/√(c₁c₂)`. (⇐) Theorem S′ (NOTES-C11). (⇒) If `θ₁₂ + θ₁ > π/2 − θ₂`, the geodesic from `h₂`
through `h₁`, continued past `h₁` by less than `θ₁` (or stopped at the point orthogonal to `h₂`), gives `v` in the cap of
`d₁` with `b = |⟨h₂|v̂⟩|² < 1 − 1/c₂`. Put `λ = (c₁|⟨h₁|v̂⟩|² − 1)/⟨d₁, d₂⟩ > 0` and `y = P_v + λd₂`: `⟨y, d₁⟩ = 0`,
`⟨y, d₂⟩ = 1 − c₂b + λ|d₂|² > 0`, so `y ∈ (Q + cone Z) ∩ Z* = K*`. A decomposition `y = q + μ₁d₁ + μ₂d₂` (`q ∈ Q ∩ Z*`)
forces `μ = 0` (pairing with `d₁`), so `y` would be PSD; but `x = Π_{v⊥}h₂` has `x†yx = λ|x|²(1 − c₂|x|²) < 0`
(`|x|² = 1 − b > 1/c₂`). ∎
For Bell pairs (`c = 2`) the criterion reads `s ≥ 1`: distinct non-orthogonal Bell pairs are never self-dual (C4.1, now a
corollary). With `c_i = 1 + r_i²` the threshold is `s* = (r₁ + r₂)²/((1 + r₁²)(1 + r₂²))`, attained by
`h₂ ∝ (r₁ + r₂, 1 − r₁r₂, 0, 0)` [X P1: 18 exact cases, six `(r₁, r₂)` including a Bell defect with a non-Bell one; at and
above the threshold S′'s necessary consequences hold at both far cap edges, below it the exact witness; P2 the Bell pair;
CC2 the construction fails on the self-dual side]. This settles C4.4's "first non-Bell multi-defect class" (two defects).
In H1 terms (a separate condition) a defect `I − cP_h` is admissible only for `c ≤ 1/λ_max(h)`.

### C12-BW — the boundary witness and three tools [W]
Throughout, `Z` is a finite set of Bell-type defects `d_l = I − 2P_l`.
**Lemma BW.** *Let `i` have a neighbour `k`, and let `v` be a unit vector with `|⟨g_i|v⟩|² = 1/2` and `|⟨g_l|v⟩|² < 1/2` for
every `l ≠ i`; with `x̂` the unit vector along `Π_{v⊥}g_k`, suppose `|⟨g_m|x̂⟩|² < 1/2` for every `m ∈ O_i` (L4′). Then
`K(Z)` is not self-dual.*
*Proof.* `v_ε := (v + εe^{iφ}g_i)/|·|` (`e^{iφ}` the phase of `⟨g_i|v⟩`) has `|⟨g_i|v_ε⟩|² = (1/2 + √2ε + ε²)/(1 + √2ε + ε²)
> 1/2`; for small `ε` every strict inequality persists. C8-L with `v_ε`, `λ` on `k` only: (L1) by the choice of `λ`; (L2)
`1 − 2|⟨g_l|v_ε⟩|² > 0`; (L3) `x = Π_{v_ε⊥}g_k` has `x†yx = λ|x|²(1 − 2|x|²) < 0` since `|x|² = 1 − |⟨g_k|v_ε⟩|² > 1/2`; (L4)
`x†d_mx = |x|²(1 − 2|⟨g_m|x̂⟩|²) > 0`. ∎
**Tool A (a boundary point outside every other closed cap).** *If `{g_l : l ∈ N_i}` does not span `ℂ⁴` (e.g. `|N_i| ≤ 3`),
some `v` as in BW exists at `i`.* Take a unit `f ⊥ span(N_i)`, `p = |⟨g_i|f⟩|` (`p < 1`, since `g_i` has a neighbour). If
`p = 0` put `v = (g_i + f)/√2`: `|⟨g_l|v⟩|² = s_il/2 < 1/2` for `l ∈ N_i`. If `p > 0` put `f′ = (f − ⟨g_i|f⟩g_i)/√(1 − p²)`,
`e^{iθ} = ⟨g_i|f⟩/p`, `v = (e^{iθ}g_i + f′)/√2`: then `⟨g_l|v⟩ = ⟨g_l|g_i⟩(1 − p/√(1 − p²))e^{iθ}/√2` and, since
`g_l ⊥ f` gives `s_il ≤ 1 − p²`, `|⟨g_l|v⟩|² ≤ (√(1 − p²) − p)²/2 = (1 − 2p√(1 − p²))/2 < 1/2`. For `m ∈ O_i`,
`|⟨g_m|v⟩|² = |⟨g_m|f′⟩|²/2 ≤ 1/2`, with equality only if `g_m ∝ f′`; a small rotation of `f′` inside `g_i^⊥` removes
the equality and keeps every strict inequality. ∎
**Tool B ((L4′) for free).** *If `m ∈ O_i` is orthogonal to `g_k`, then (L4′) holds for `m` at every `v` with
`|⟨g_k|v⟩|² < 1/2 ≤ |⟨g_i|v⟩|²`:* `⟨g_m|x⟩ = −⟨v|g_k⟩⟨g_m|v⟩`, so `|⟨g_m|x̂⟩|² = ab/(1 − a)` with `a = |⟨g_k|v⟩|² < 1/2`,
`b = |⟨g_m|v⟩|² ≤ 1 − |⟨g_i|v⟩|² ≤ 1/2`, hence `< 1/2`. ∎
**Tool C (one awkward orthogonal member).** *Suppose the members of `O_i` not orthogonal to `g_k` are a single `m`,
`g_k ∉ span(g_i, g_m)`, and some `θ` has `|e^{iθ}⟨g_l|g_i⟩ + ⟨g_l|g_m⟩| < 1` for every `l ∈ N_i`. Then BW applies at `i`.*
At `v₀ = (e^{iθ}g_i + g_m)/√2`: `|⟨g_i|v₀⟩|² = 1/2`, `|⟨g_l|v₀⟩|² < 1/2` for `l ∈ N_i`, `|⟨g_{m′}|v₀⟩|² = |⟨g_{m′}|g_m⟩|²/2 < 1/2`
for the other `m′ ∈ O_i`; and with `β_i = ⟨g_k|g_i⟩`, `β_m = ⟨g_k|g_m⟩`, `P = |e^{iθ}β_i + β_m|² < 1`:
`|⟨g_m|x̂⟩|² = |β_m − e^{iθ}β_i|²/(4 − 2P) ≤ (2 − P)/(4 − 2P) = 1/2` (parallelogram law and Bessel,
`|β_i|² + |β_m|² ≤ 1`, strict because `g_k ∉ span(g_i, g_m)`). Replacing `g_m` by `√(1 − η²)g_m + ηh` (`h ⊥ g_i, g_m`) moves
`v₀` strictly outside the closed cap of `m` and keeps every strict inequality; Tool B covers the other members of
`O_i`. The `θ`-condition: for each `l`, the admissible `θ` form an open arc of length `≥ π`, of length `> π` unless
`g_l ∈ span(g_i, g_m)`; two such arcs, one longer than `π`, always meet. ∎

### C12-4 — Conjecture C8-C at four members: proved [W + X B1, B2, CC3]
**Theorem C12-4.** *No set of four distinct Bell-type defects containing a non-orthogonal pair has a self-dual surgery.*
*Proof.* By the pattern of the non-orthogonality graph (all ten graphs with an edge on four vertices):
K2+2K1, 2K2, K3+K1 — `i, k` an edge, every member orthogonal to `i` is orthogonal to `k`: Tools A + B. P3+K1 (`a–b–c`, `d`)
— `i = b`, `k = a`. P4 (`a–b–c–d`) — `i = b`, `k = a` (`d ⊥ a`). Paw (triangle `a, b, c`, pendant `d` at `c`) — `i = a`,
`k = b` (`d ⊥ b`). K1,3, diamond, K4 — `i` a vertex adjacent to all others (`O_i = ∅`, at most three neighbours): Tool A.
C4 (`a–b–c–d–a`) — `i = a`, `m = c`: if one of `g_b, g_d` is outside `span(g_a, g_c)`, Tool C with that `k` (the other
neighbour's arc has length `≥ π`); otherwise all four vectors lie in one 2-dimensional subspace, i.e. on one Bell circle,
which is Theorem C8 (b). ∎
With C4.1 (pairs) and Theorem C8 (triples): **C8-C holds for every Bell set of at most four members.** Exact instances
[X B1]: one Gaussian-integer set per pattern, each with an exact C8-L witness (the C4 and K4 instances with four linearly
independent vectors); the K4 instance lies in C8's open class (for every admissible `(g₁, g₂)` the other two vectors have
independent `W^⊥`-projections) [X B2]; the degenerate C4 (the square on one Bell circle) is C8 (b) [X CC3].

### C12-5 — every finite Bell set without orthogonal pairs is not self-dual [W + X G1]
**Theorem C12-5.** *Let `Z` be a finite Bell set and `C` a connected component of its non-orthogonality graph with
`|C| ≥ 2` in which every two members are non-orthogonal (in particular `C = Z` when `Z` has no orthogonal pair). Then
`K(Z)` is not self-dual.*
*Proof.* `Ω = ⋃_{j∈C} U_j` is open and nonempty, and its exterior contains every pure product off a lower-dimensional set
(a product never lies in an open Bell cap, and `|⟨g|x⊗y⟩|² = 1/2` cuts out a 2-dimensional subset of the 4-dimensional
product manifold), so `∂Ω` separates `ℂP³` and has dimension `≥ 5` [L: a closed set of dimension `≤ n − 2` does not
separate a connected `n`-manifold — the fact used in NOTES-C3 Lemma 3]. `∂Ω ⊆ ⋃_{j∈C} ∂U_j`; each `∂U_j` is the smooth real
quadric of the non-degenerate form `2P_j − I` (irreducible, signature (2, 6)), two distinct ones meet in dimension `≤ 4`,
and `∂U_j ∩ Ū_m` for `m ∉ C` (so `g_m ⊥ g_j`) lies in the circle `ℂP(span(g_j, g_m))`. Removing these from `∂Ω` leaves a
point `v` on exactly one `∂U_i`, `i ∈ C`, strictly outside every other closed cap. `O_i ∩ C = ∅`, and each `m ∉ C` is
orthogonal to every member of `C`, in particular to any neighbour `k ∈ C` of `i`: Tool B gives (L4′), and BW applies. ∎
Exact instances [X G1]: six and eight Gaussian-integer Bell vectors, no orthogonal pair, every vertex's neighbours spanning
`ℂ⁴` (Tool A unavailable everywhere), each with an exact C8-L witness at a point lying in exactly one cap.

### Residual (OPEN)
- C8-C for finite Bell sets of five or more members in which every non-trivial component has an orthogonal pair and no
  vertex admits Tools A + B or A + C (e.g. vertices with four or more neighbours spanning `ℂ⁴` and two awkward orthogonal
  members); closed infinite Bell sets other than C7.6's circle.
- For defects with `c < 2`, three or more members: (CC) for every pair is sufficient (S′); its necessity is not decided —
  a point of `∂Ω` may lie inside every co-cap, so BW does not transfer.

## Verdict on node C12
- C8-C at four members: **proved** (every four-member non-orthogonal Bell set has a non-self-dual surgery), and beyond:
  every finite Bell set with a complete non-orthogonality component, in particular every one without orthogonal pairs.
  No self-dual non-orthogonal example exists among them, so C8-C's prediction survives; no FAILED row.
- The non-Bell pair theorem is sharp: self-dual iff `c₁c₂s ≥ (√(c₁ − 1) + √(c₂ − 1))²` (or two orthogonal Bell defects).

## Gem classification (§A.31)
- NEW: the sharp pair theorem for rank-one defects (the Bell pair theorem C4.1 is its `c = 2` corner); the boundary
  witness BW with Tools A–C; C8-C for all Bell sets of at most four members; the union-boundary theorem for complete
  components (Lemma 3's dimension count turned into a witness).
- Assumption-watch marker: C8's obstruction "two outside vectors with independent `W^⊥`-projections" was an artefact of
  fixing `v = g₁ + εe` near the centre of a cap; witnesses live at cap boundaries, where only the caps' arrangement matters.

## What is not claimed
No kernel statement; the proofs are [W] (this round, not audited); the dimension fact is [L]; Theorem C8 (b) (audited) is
used for the degenerate C4; the residual classes above are not decided.
