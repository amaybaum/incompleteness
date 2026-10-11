# NOTES-C14 — facial invariants of continuum defects; T on the continuum cones; `K_circ`

Node C14 (round 3, "if time remains"). `c(x) = dim span{y ∈ K : ⟨x, y⟩ = 0}` on extreme rays of a self-dual `K`
(automorphism-invariant: [A] Y6); Lemma 1 of NOTES-C3 (C3.2): `c(P00) = 9` for every `K` with H1–H3. `K_circ`: any
`Ĝ`-invariant self-dual cone with H1 and slice Circ (NOTES-C2 (e), C7). Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of any C14 script (2026-10-11T01:02:22Z, `date -u`)

Scratchpad exploration (numerical, not evidence): the real span of the contact points of a circle surgery has rank 14.

1. **Tangency bound (any torus orbit).** If a compact torus `T ⊆ Aut(K)` (`K` self-dual) moves an extreme ray `z` along
   a `k`-dimensional orbit, every `y` in the exposed face at `z` satisfies `⟨y, i[H_a, z]⟩ = 0` for the generators `H_a`
   (the function `g ↦ ⟨y, gzg†⟩ ≥ 0` has a minimum at `g = e`), so `c(z) ≤ 15 − k`. For every `K_circ` the off-`Fix` non-PSD
   extreme rays (C7-D) have `k ≥ 1`, hence `c ≤ 14`.
2. **Exact value on circle surgeries.** For a defect `d₀ = I − cP_{h₀}` of a circle surgery with
   `h_α = √p e₁ + √(1 − p)e^{iα}e₂`, the contact set (pure members of `K` orthogonal to `d₀`) contains
   `{v : v₁, v₂ ≥ 0, √p v₁ + √(1 − p)v₂ = 1/√c, |v₃|² + |v₄|² = 1 − v₁² − v₂²}`, whose projectors span exactly the 14-dimensional
   space `{Y : ⟨Y, d₀⟩ = 0, Im Y₁₂ = 0}` (a segment times a 3-sphere: 3 + 8 + 3 dimensions). So `c(d₀) = 14`. Exact instance:
   the S2 circle cone (C13.7's family, `p = 9/10`) at `c = 1000/961` (in the H1 and (CC) window), where the contact set has
   rational points (`3a + b = 31k`, `|v|² = 100k²`): exact rank 14 and both linear constraints satisfied.
3. **T fails on the explicit continuum cones** (C13.5 case A, C13.7 S2): `c = 14` on every defect, `9` at `P00` — the first
   cones with a continuum of non-PSD extreme rays on which T is decided (C3.1's open class).
4. **`K_circ`:** `c ≤ 14` on its off-`Fix` defects; T on `K_circ` would need `c = 9` there and, at every boundary point of
   its set of pure members, every active non-PSD member to vanish at the point (no smooth contact); predicted OPEN.

(Runs, results and the written proofs follow below this line after the runs.)

## Runs (written 2026-10-11T01:05Z, `date -u`)

| script | runs | final | replay |
|---|---|---|---|
| `c14_facial.py` | 1 (01:04:27Z) | 8/8, `VERDICT C14-FACIAL-EXACT` | identical (out `e1a26898…`) |

Pre-run edit (before the first run): CC2's search box for complex contact points moved to where `|a|² + |b|² < 2500` is
possible (the first box could not contain the optimum `a ≈ 28 + 37i`).

## Results

### C14-1 — the tangency bound [W]
*Let `K` be self-dual, `T ⊆ Aut(K)` a compact torus of unitary conjugations `U_θ = e^{iΣθ_aH_a}`, and `z` an extreme ray
whose `T`-orbit has dimension `k`. Then `c(z) ≤ 15 − k`.* For `y` in the exposed face `F_z = K ∩ z^⊥`, the function
`θ ↦ ⟨y, U_θzU_θ†⟩` is `≥ 0` (`K = K*`) and vanishes at `θ = 0`, so its gradient `(⟨y, i[H_a, z]⟩)_a` vanishes; the `k`
independent tangent vectors `i[H_a, z]` and `z` itself (trace `> 0`, the tangents are traceless) cut `span F_z` down to
dimension `≤ 16 − 1 − k`. ∎ For every `K_circ` (Theorem C7-D) the off-`Fix` non-PSD extreme rays have `k ≥ 1`:
**`c ≤ 14` on them.** For finite-defect cones (`k = 0`) Lemma 2 of C3 gives `c = 15`.

### C14-2 — the exact value on circle surgeries [W + X F0–F3, CC1, CC2]
Let `Z = {d_α = I − cP_{h_α}}`, `h_α = √p e₁ + √(1 − p)e^{iα}e₂` (`e_k` orthonormal), satisfy H1 and (CC), and let every other
component of the defect set leave a contact point of `d₀` strictly outside its closed caps (vacuous for a single circle).
*Then `c(d₀) = 14`.* Upper bound: C14-1 (`k = 1`). Lower bound: for a unit `v`, `max_α|⟨h_α|v⟩|² = (√p|v₁| + √(1 − p)|v₂|)²`,
attained at `α = 0` iff `v₁, v₂` have equal phases; so the set `C₀ = {v : v₁, v₂ ≥ 0, √p v₁ + √(1 − p)v₂ = 1/√c,
|v₃|² + |v₄|² = 1 − v₁² − v₂²}` consists of pure members of `K` orthogonal to `d₀` (in `K` because they pair `≥ 0` with every
`d_α`). Its projectors span 14 dimensions: for fixed `f = (v₁, v₂)` the sign flip `(v₃, v₄) ↦ −(v₃, v₄)` separates the block
`[[ff^T, 0], [0, cc†]]` (4 dimensions) from the off-diagonal block `[[0, fc†], [cf^T, 0]]` (4 dimensions per `f`, 8 over two
independent `f`); the diagonal blocks over the segment add the span of `(v₁², v₁v₂, v₂², 1 − v₁² − v₂²)`, 3 dimensions
(the chord meets the open unit disk, the line's distance to `0` being `1/√c < 1`): `3 + 8 + 3 = 14`. ∎ [X F2: exact rank 14
from 24 rational contact points of the S2 circle cone at `c = 1000/961`; F3: every one satisfies both linear constraints,
which are independent; CC2: on the single-defect cone `K({d₀})` the whole null quadric is available and the rank is 15
(Lemma 2) — the drop to 14 is the circle's tangency; CC1: misaligned phases leave the face.]
For C13.5 (case A) the hypothesis holds: contact points of `d_h` with `x₂ = x₄ = 0` (coordinates along `b̂₂, b̂₄`) are
strictly outside the caps of the other two circles (`|x₂|, |x₄| < x₁`), so an open subset of `C₀` lies in the face, and an
open subset of the irreducible set `C₀` spans what `C₀` spans [W].

### C14-3 — T fails on the explicit continuum cones [W + X F4 + A Y6]
On the S2 circle cone (C13.7, every admissible `c`; exact at `c = 1000/961`) and on case A's cone (C13.5), every defect has
`c = 14` (C14-2; the defects form one orbit per circle under the cone's own torus), while `c(P00) = 9` (Lemma 1 of
NOTES-C3; [X F4]: the pure members orthogonal to `|00⟩` span exactly the 9-dimensional `Herm(|00⟩^⊥)` here). Automorphisms
of a self-dual cone preserve `c` on extreme rays ([A] Y6), and `P00` and the defects are extreme rays (C13.1; pure products
are extreme in `maxCone` [A] AUDIT-X): **T fails on both cones** — the first cones with a continuum of non-PSD extreme rays
on which T is decided. Pattern: on every explicit exotic cone so far, `c(defect) = 15 − k` with `k` the dimension of the
defect's orbit under the cone's torus (`k = 0`: 15; `k = 1`: 14).

### C14-4 — `K_circ`: a reduction, not a decision [W]
For any `K_circ`: (i) its off-`Fix` non-PSD extreme rays have `c ≤ 14` (C14-1); (ii) every pure member `P_v` is an extreme
ray (its minimal face lies in `{αP_v + vw† + wv†}`, and for `w ≠ 0` such a matrix is negative on products near a product
orthogonal to `v`, so it is not in `maxCone ⊇ K`), and the pure members orthogonal to `v` span `Herm(v^⊥)` (the
Fubini–Study argument of NOTES-C2 (c), valid for every unit `v`). Hence T on `K_circ` would force: `c = 9` on the off-`Fix`
defects (six dimensions below the tangency bound at `k = 1`), and, at every boundary point `v` of the set of pure members,
every non-PSD member `y` with `v†yv = 0` to satisfy `yv = 0` (otherwise `y` raises `c(P_v)` to `≥ 10`); since the boundary is
at least 5-dimensional and each `ℂP(ker y)` at most 2-dimensional, the active members would form a family of dimension
`≥ 3` whose kernels sweep the boundary. **Whether some `K_circ` satisfies this (and T) is OPEN**; no explicit `K_circ` is known
(C7), and the explicit continuum cones all have `c = 15 − k`.

## Verdict on node C14
- `c ≤ 15 − k` for every extreme ray with a `k`-dimensional torus orbit; `c ≤ 14` on `K_circ`'s off-`Fix` defects.
- `c = 14` exactly on circle-surgery defects; T fails on the explicit continuum cones of C13 (exact on the S2 circle cone).
- T on `K_circ`: OPEN, reduced to the absence of smooth contact between pure members and non-PSD members.

## Gem classification (§A.31)
- NEW: the tangency bound; the facial invariant of continuum defects (`15 − k`); T decided (fails) on cones with a
  continuum of non-PSD extreme rays.
- ELABORATING: C3.1's undecided class shrinks to cones without a smooth contact (no explicit member known).

## What is not claimed
No kernel statement; C14-1, C14-2 (outside the exact instance), C14-3's case-A part and C14-4 are [W]; Y6 is [A]; T for
`K_circ` and for every EBF-only cone remains OPEN.
