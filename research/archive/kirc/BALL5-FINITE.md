# d = 5 with finite local symmetry — read-only, from L42

Baseline `fdebc6e3`. The owner's d = 5 branch, run with the owner's orbit-hull criterion:
- positive control: d = 3;
- negative control: the disc theorem.

Files:
- **exact checks:** `ball5_nogo.py` (12 PASS, 0 FAIL, log `ball5_nogo.log`);
- **constructions:** `ball5.py`, `ball5_run1.py`, `ball5_pairs.py`;
- **evidence:** block-coordinate minimization. The objective is affine in each of `s, t, a, b` separately, so every
  block step is an exact minimization.

Nothing is committed.

## Setting

- **The 5-ball.** Basis `u, x, y, z, w₁, w₂`, with corners `u ± z`.
- **The native local group.** NOT on each bit: `N⊗I` and `I⊗N`. Here `N` is a ball involution with `Nz = −z`; its
  off-frame action is free, just as G's is.
- **Eigenspaces of N.** `T` is the 4-dimensional transverse space. Let `T₊`, `T₋` be N's ±1 eigenspaces in `T`, of
  dimensions `p`, `q`, and let `V₋ = T₋ ⊕ ⟨z⟩`.
- **The native relations,** as for CNOT and NOT on bits:
  - `(I⊗N) G (I⊗N) = G` (target);
  - `(N⊗I) G (N⊗I) = (I⊗N) G` (control).

## 1. Countermodel without the control-NOT relation (exact)

The J/K map:
- `N` is the rotation fixing `x` and flipping `y, z, w₁, w₂`;
- `G(|a⟩⊗t) = |a⟩⊗Nᵃt`;
- `G(c⊗t) = c⊗St` on `E₊ = ⟨u, x⟩`, with `S` exchanging `u` and `x`;
- `G(c⊗t) = Jc⊗Kt` on `V₋`, with `J`, `K` orthogonal complex structures on the control's transverse space and on `V₋`.

It meets the frame, normalization and `G² = I`.

**`G(min) ⊆ max` exactly.**
- The value on `(1,a)⊗(1,b)` is
  `(1 + s_z a_z)(1 + b_x t_x) + (s_z + a_z)γ + α(t_x + b_x) + βδ`.
- The pairs `(α, β) = (a_T·s_T, a_T·Js_T)` and `(γ, δ) = (b₋·t₋, b₋·Kt₋)` range over discs whose radii match the Bloch
  case.
- The value is affine in each pair, so its minimum over the discs is concave and is attained on the boundary circles.
  That is exactly the d = 3 configuration space, where the value is the complex CNOT's and is ≥ 0.
- Block-coordinate descent gives a minimum of about −1e−15, consistent.

**The resulting cone.** `C = cone(min ∪ G·min)` lies between `min` and `max`, is locally tomographic, and G acts
reversibly on it. It carries a reversible CNOT on the 5-ball with local group `{I, I⊗N}`: the target relation holds,
so the orbit is `{I, G, I⊗N, G(I⊗N)}`.

**It fails once the control NOT is added.**
- The control relation fails.
- `⟨G, N⊗I, I⊗N⟩` has 16 elements. The word `G·(N⊗I)·G` sends a product state outside `max`. Exact witness: state
  `(u + w₁)⊗(u + y)`, effect `(u + w₁)⊗(u + y)`, value −2 (integer arithmetic).

So at d = 5, **unlike the disc**, kinematics alone does not exclude a reversible CNOT; the local symmetry has to do
the work.

## 2. Obstruction with the native NOT relations (exact)

**Theorem (d = 5).** No linear G acting as CNOT on the corners, with `G² = I` and both native NOT relations, maps
`min` into `max`, for any choice of the involution `N`.

- **L1 — structure, from first-order conditions at the control corners.**
  - `G(|a⟩⊗t) = |a⟩⊗M_a t`, with `M_a` orthogonal, `M₁ = N M₀` and `N M₀ = M₀ N`.
  - With `G̃ = G(I⊗M₀)`, and for each `c` in the control's transverse space, the target vector of `G̃(c⊗t)` must lie
    in `ker g⊥(t) ∩ ker g⊥(Nt)` for every pure `t`.
  - Separating parity and degree, this forces `G̃` to map `T_A⊗V₋` into itself, by an operator-valued matrix that is
    antisymmetric in the `V₋` indices. On `T_A⊗E₊` it has the analogous symmetric-plus-antisymmetric form.
  - This is the disc argument of `FINITE-LOCAL.md` made general; at d = 2 it reproduces that theorem.
- **L2 — parity.** The control relation makes `G|_{T_A⊗V₋}` anticommute with `N_A⊗I`. An involution that
  anticommutes with it exchanges the eigenspaces `T₊⊗V₋` and `T₋⊗V₋`, so `p = q`. With `p + q = 4`, this gives
  `p = q = 2` and `dim V₋ = 3`.
- **L3 — no involution on a 3-dimensional `V₋`.**
  - Write the block as `B̃·D`, with `B̃ = [[0,P,Q],[−P,0,R],[−Q,−R,0]]` (entries in `End(T_A)`) and `D = M₀|_{V₋}`.
    Then `D = diag(μ₁, μ₂, 1)` with `μᵢ = ±1`, since `M₀` fixes `z`.
  - `(B̃D)² = I` forces the squares `P², Q², R²` to be nonzero multiples of `I` (±½) in every case. So `P`, `Q`, `R`
    are all invertible.
  - It also forces an off-diagonal product (`PQ`, `PR` or `QR`) to vanish. Contradiction. [checked symbolically for
    all four `μ`]

**Controls.**

| control | result |
| --- | --- |
| complex CNOT at d = 3 | `p = q = 1`, `dim V₋ = 2`: the block is antisymmetric, an involution, and anticommutes with `N_A⊗I` |
| d = 5 J/K map | meets L1 (`p = 1`, `q = 3`) and fails the control relation, as L2 predicts |
| the 288 two-Bloch-pair completions (`p = q = 2`, both relations, involution) | all fail `G(min) ⊆ max` (best −0.854), as the theorem requires |

## 3. Status

| case | result |
| --- | --- |
| d = 2 | CNOT impossible with no local symmetry at all |
| d ≠ 3, full `SO(d)×SO(d)` | CNOT impossible in every component |
| d ≥ 3, any local gate of infinite order at an irrational angle | reduces to full `SO(d)` by closure |
| d = 5, native NOTs with the native relations, `G² = I` | CNOT impossible (dimension argument) |
| d = 5, only the target NOT, or no local symmetry | exact countermodel: reversible CNOT on a locally tomographic 5-ball composite |
| d = 5, both NOTs without the control relation; G of higher finite order | open |

**Where the parity argument stops.** It excludes d = 5 because `p = q = (d−1)/2 = 2` makes `dim V₋ = 3` odd. For
d = 7, `dim V₋ = 4`, and this argument does not exclude it. That is the next place the finite-local question could
differ, and nothing is claimed there.
