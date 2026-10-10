# REL-T — the target relation alone: what survives

Read-only research thread. Base: certified commit L = `e2426ba4109dcd719d518aefbd3c417b7c6fdc5b`, read from a detached
worktree. Nothing here changes git, a manuscript, the roadmap or any round. Nothing here is adopted, preregistered,
frozen or governed. No local Lean toolchain was available: **kernel facts below are only readings of landed Lean
statements at L**. Everything else is a written proof or an exact computation in `relt/`. One script,
`relt_Sm_numeric.py` (and `relt_contraction_numeric.py`), is floating-point **evidence only** and certifies nothing.

Notation is that of `OIBridge.CompositeDimension`. `H = HVec d = ℝ^{d+1}` (index 0 the unit). `W d` is the space of
`(d+1)×(d+1)` matrices (control row index, target column index). `hom x = (1, x)`. `Ñ = homMap N`.
`relT : actT N ∘ G ∘ actT N = G` (G commutes with `I ⊗ Ñ`). `relC : actC N ∘ G ∘ actC N = actT N ∘ G`. Frame is
`NativeGate.frame`. P± are `posFwd` and `posInv` into `maxCone (eball d)`. `L` (the Lorentz cone) is the cone of
`Lor` vectors. It is both the homogenized state cone and, up to scale, the effect cone (`lor_ehom`, `isEffectOn_affOf`).
`p_N` and `q_N` are the dimensions of the `+1` and `−1` eigenspaces of `N` on `z^⊥`, so `tangentPlus N = p_N`.

## Productivity test (fixed before the walk)

The thread counts as a **gem** iff it yields something strictly stronger than the restatement "relC is used
somewhere", **and** that result either constrains which `(d, N)` survive under relT or exposes a hidden assumption in
the landed parity/selector chain. Otherwise it is a non-gem (relabelling). Propagation bar: better than coherence.
Results below the bar are only recorded.

**Verdict on the test: GEM.** It produced several results stronger than a relabelling:

- the exact relC-step of the parity argument;
- explicit even-`d` countermodels to parity under relT + frame;
- relation-free exclusions of `d = 2` and `d = 4` from frame + P± alone;
- an all-odd-`d` relT + frame + P± family.

Together these expose a hidden assumption: the two exclusions DIM-1 attributes to parity and to positivity overlap at
`d ≤ 4`.

## Node tree

### N1 — Q1: under `IsNot (eball d) z N` + relT, are the eigenspaces of `Ñ` still balanced? (decisive branch)

**N1.1 — Which step of the landed parity argument reads relC?** Verdict: **located exactly** (kernel reading at L).

`finrank_plus_eq_finrank_minus_rel` calls `NativeGateBall.parity (Pop N) (Lop G _) hinj hanti`.

- **Injectivity of `Lop`.** `Lop_injective_rel → Lop_eq_zero_rel` reads `hR` only through
  `opGate_comp_homMap_rel`, whose proof uses `hR.relT` only. So injectivity of `Lop` needs `IsNot (eball d) z N`
  (involution + self-adjointness, via `toOp_actT`) and relT.
- **Anticommutation `Lop (Pop f) = −Pop (Lop f)`.** `Lop_anti_rel` reads `hR` only through
  `opGate_homMap_comp_rel`, whose proof uses `hR.relC` only. This is the single place relC enters.

The same holds for DIM-1's `Lop_anti`, which uses relC via `opGate_homMap_comp`. In DIM-1 §Q, relC enters only through
`gate_actC`, whose sole use is `gate_corner_neg`. That lemma feeds `gt_corner_neg`, which feeds `gt_center`,
`gt_tangent_corners` and `gt_sphere_corner`. So the block reduction reads relC only as the −z-corner identity
`G(hom(−z) ⊗ Y) = hom(−z) ⊗ Ñ M₀ Y`.

**N1.2 — Does balance survive relT (+ frame)?** Verdict: **NO.** The evidence is exact computation; the
algebra is in the written proof below.

The **controlled-N gate** is

    G = Π_a ⊗ I + Π_b ⊗ Ñ,   Π_a = ½ hom z hom zᵀ,   Π_b = I − Π_a,
    i.e. G ω = Π_a ω + Π_b ω Ñᵀ.

**Written proof** (for every `d ≥ 1` and every NOT `N`):

- `Π_a hom z = hom z` and `Π_a hom(−z) = 0` (this uses the unit clause).
- Since `Ñ hom(±z) = hom(∓z)`, the frame holds.
- `G` commutes with `I ⊗ Ñ` and `G² = I` (because `Ñ² = I`), so relT holds and `G` is invertible.
- relC holds iff `Ñ Π_a Ñ = Π_b`. That is impossible for `d ≥ 2`, since `Π_a` has rank 1 and `Π_b` has rank `d`.

**Exact checks** (`relt_q1q2q3_exact.py`, 77/77):

| model | `d` | `N` | IsNot | frame | relT | `G² = I` | relC | `(dim E₊, dim E₋)` | `Lop` injective | `Lop` anticommutes | posFwd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CM2r | 2 | `diag(1,−1)` | ✓ | ✓ | ✓ | ✓ | ✗ | (2,1) | ✓ | ✗ | ✗ (value −1) |
| CM2n | 2 | `−id` | ✓ | ✓ | ✓ | ✓ | ✗ | (1,2) | ✓ | ✗ | ✗ (−1) |
| CM4r | 4 | `diag(1,1,1,−1)` | ✓ | ✓ | ✓ | ✓ | ✗ | (4,1) | ✓ | ✗ | ✗ (−1) |
| CM4m | 4 | `diag(1,−1,−1,−1)` | ✓ | ✓ | ✓ | ✓ | ✗ | (2,3) | ✓ | ✗ | ✗ (−1) |
| CM4n | 4 | `−id` | ✓ | ✓ | ✓ | ✓ | ✗ | (1,4) | ✓ | ✗ | ✗ (−1) |

The posFwd failure witness is the input `(e₁, z)`, the control effect `(1, −1, 0, …) ∈ L` and the target effect
`hom(−z) ∈ L`. The pairing is `−1`; with sharp normalization it is `−1/4`.

**Strongest countermodel.** Each model has IsNot, the frame, relT and invertibility (`G² = I`). Each lacks relC,
posFwd and posInv. With posInv the "lacks positivity" column cannot be improved at `d = 2` or `d = 4`; see N2.3 and N5.

Without the frame, relT + P± is trivially satisfiable in every `d` with unbalanced `N`: take `G = id`. This is
recorded as a countercontrol (`id` fails the frame).

**N1.3 — Is `d` still odd?** Verdict: under IsNot + relT + frame, **NO** (CM2*, CM4*, exact).

So relC is load-bearing for `not_even_of_gateRel` even in the presence of the frame. ODD-CHAR-1 explicitly left open
whether relC is needed for oddness ("does not show that … relC is needed for oddness"). This settles it for the
positivity-free setting: relC is needed. With positivity added, see N2.

### N2 — Q2, strengthened: does relT + frame + P± admit an even `d`?

**N2.1 — Normal form under frame + P± (no relation used).** Verdict: **written proof.** It is assembled from
kernel-landed lemmas whose proofs, read at L, use only the frame, posFwd and posInv fields.

1. **The `z` corner.** `corner_form` (frame row 0 + posFwd) gives `G(hom z ⊗ Y) = hom z ⊗ M₀Y`.
   - Apply `corner_form` with `−z` to `(I ⊗ ρ̃_z) ∘ G`, where `ρ_z` is the reflection through `z^⊥`. This map is still
     positive and carries the `−z` row of the frame into the fixed form. It gives
     `G(hom(−z) ⊗ Y) = hom(−z) ⊗ M₁Y`.
   - `M₀` and `M₁` are cone maps with cone-map inverses (`lor_cornerMap`, `Mfwd_Minv`, `Minv_Mfwd`, applied both ways).
   - By the frame, `M₀` fixes `hom(±z)` and `M₁` swaps them. So both fix `e₀`.
2. **Automorphisms of `L` fixing `e₀` are `1 ⊕ O(d)`.** Pure rays go to pure rays. Write `S hom y = λ hom y'`. Adding
   the antipode gives `λ(y) = λ(−y) = 1`, so `S` preserves the head on the sphere and its tail block is
   norm-preserving. Hence `S := M₁M₀⁻¹ = 1 ⊕ σ` with `σ ∈ O(d)` and `σz = −z`. Likewise `M₀ = 1 ⊕ O`.
3. **Normalization.** Set `Gt := G ∘ (I ⊗ M₀⁻¹)`. It again satisfies the frame and P±. It acts as the identity on the
   `z` slice and as `I ⊗ S` on the `−z` slice.
4. **The tangent slices close up.** By `tangent_vanish` at both corners, the control output of
   `Gt(lift t ⊗ Y)` (`t ⊥ z`) lies in `T := lift(z^⊥)`. Hence `Gt(T⊗H) ⊆ T⊗H`, and invertibility makes the tangent
   block `𝕂 := Gt|_{T⊗H}` invertible.
5. **The linear core (`Lsig`).** Write `Gt(lift t ⊗ Y) = Σ_k lift e_k ⊗ L_{k,t} Y`.
   - Apply `tangent_vanish` to `X ↦ pairVal e f (Gt(X ⊗ hom y))`, with `f = (1,−y)` at the `z` corner and
     `f = (1,−σy)` at the `−z` corner.
   - This gives `(1,−y)ᵀ L hom y = 0` and `(1,−σy)ᵀ L hom y = 0` for every unit `y`. Every block lies in
     `Lsig := {L : these hold}`.
   - Exactly (A1): `Lsig = {[[0, aᵀ],[a, A]] : σa = a, Aᵀ = −A, σᵀA = Aσ}`. The `(0,0)` entry vanishes because
     `σz = −z`.
6. **The exact positivity criterion** (written). Given 1–5:

       posFwd(Gt) ⟺ ∀ unit t ⊥ z, ∀ unit y, ∀ f ∈ L:  Σ_k ⟨f, L_{k,t} hom y⟩² ≤ ⟨f, hom y⟩⟨f, S hom y⟩.

   - **Necessity.** Put `x = c z + s t` and the control effect `e = (1, a z + ē_T)`. Then

         value = ½(1+c)(1+a)P + ½(1−c)(1−a)Q + s ē_T·κ.

     Choose `ē_T ∥ −κ` with `|ē_T| = √(1−a²)` and `c` with `(1+c)(1+a)P = (1−c)(1−a)Q`. Then
     `value = |s|√(1−a²)(√(PQ) − |κ|)`.
   - **Sufficiency.** By AM–GM.
   - posInv is the same criterion for `Gt⁻¹`, with `S⁻¹` and the blocks of `𝕂⁻¹`.

   Evidence for the criterion's ingredients: the J/K value identity (exact, B-rows) and the positive controls (A4).

**N2.2 — relT adds nothing beyond the normal form when σ is an involution.** Verdict: **written + exact.**

If `σ² = I`, every element of `Lsig` commutes with `Σ := 1 ⊕ σ` (σ is symmetric, `σa = a`, `σA = Aσ`). So `Gt`
satisfies relT with `N := σ`, and `σ` is a NOT (orthogonal involution, `σz = −z`).

Hence, for involutive `σ`, "frame + P±" and "relT + frame + P±" have the same solvable dimensions. relT only constrains
how `G` sits relative to an *externally given* `N`; see N3.

**N2.3 — `d = 2`.** Verdict: **frame + posFwd + posInv are unsatisfiable at `d = 2`, with no relation and no N.**
Evidence: written proof + exact computation.

- `T` is one-dimensional, so `𝕂 = L` is a single block in `Lsig`.
- `σ ∈ O(2)` with `σz = −z` forces `σ ∈ {diag(1,−1), −id}` (with `z = e₂`).
- Exactly (A2): for both, the generic element of `Lsig` has determinant identically 0. So `𝕂` is singular,
  contradicting invertibility.
- Countercontrol: at `d = 3` with `σ = nflip`, `Lsig` has generic determinant ≠ 0.

Consequently no gate with relT + frame + P± exists at `d = 2`, and the CM2* models are optimal in that sense.

**N2.4 — `d = 4`, linear core only.** Verdict: the linear core does **not** exclude `d = 4` for every σ (exact).

Random rational block matrices over `Lsig` (`relt_d4_rank_probe.py`) are certified full rank (15/15) for
`σ = diag(1,−1,−1,−1)` and `σ = diag(1,1,−1,−1)`. Positivity proper is needed; see N5.

### N3 — Q3: `d = 3` under relT alone

**N3.1 — relT + frame (no positivity).** Verdict: `refl3` and `negId3` **are admitted** (exact).

The controlled-N gate with `refl3`, and with `negId3`, satisfies IsNot, the frame, relT and `G² = I`. relC fails, as it
must by `not_gateRel_refl3` and `not_gateRel_negId3`. DIM-1's `cnot` does not satisfy relT with either.

So `det_three` / `piRotation_three` **do not** survive with relC replaced by the frame.

**N3.2 — relT + frame + P±.** Verdict: **the π-rotation conclusion survives** (written proof + exact).

Under relT, every block `L ∈ Lsig` commutes with `Ñ`. Then:

- `L e₀ = (0, a)` with `a ∈ Fix(N) ∩ z^⊥`. So `p_N = 0` gives `L e₀ = 0` for every block, and `𝕂` is singular.
- `L lift z = (0, A z)` with `A z ∈ E₋(N) ∩ z^⊥`. So `q_N = 0` gives `L lift z = 0`, and `𝕂` is singular.

Hence **relT + frame + P± ⇒ p_N ≥ 1 and q_N ≥ 1 in every `d`**. At `d = 3` this forces `p_N = q_N = 1`: `N` is a
π-rotation, `det N = 1`, and `refl3` (`p = 2`, `q = 0`) and `negId3` (`p = 0`, `q = 2`) are excluded.

Exact (A3): for σ a generic rotation (Lsig = 0), `diag(1,−1)`, `id` and `−id`, every `L ∈ Lsig ∩ comm(Ñ)` kills
`lift z` (refl3) or `e₀` (negId3). Countercontrol: with `nflip`, some `L` kills neither.

Also (relation-free) at `d = 3`, frame + P± already force `σ` to be a π-rotation: rotation-type `σ` gives `Lsig = 0`;
`σ = diag(1,1,−1)` and `σ = −id` give rank 6/8 (exact, `relt_d4_rank_probe.py` controls).

### N4 — Q4: higher odd `d` under relT + frame + P± (NB-1's C5, critically)

**N4.1 — C5 re-derived exactly.** Verdict: **CONFIRMED.**

`relt_pos_exact.py`, B-rows, uses the gate built from NB-1's frozen description (basis `u, x, y, w₁, w₂, z`):

- IsNot, frame, relT, `G² = I`: ✓.
- relC: ✗.
- `(dim E₊, dim E₋) = (2, 4)`, so unbalanced.
- J and K are orthogonal complex structures.
- The normal form holds with all blocks in `Lsig` and an invertible tangent block.

**N4.2 — Positivity, examined critically.** Verdict: **CONFIRMED by an independent proof.** NB-1's argument reduces
to the complex CNOT; this proof avoids that reduction and its "boundary circles = d = 3 configuration space" step.

The proof covers the J/K family `C_d` at every odd `d = 2m+1 ≥ 3`, with `p_N = 1`, `q_N = d − 2`,
`M₀ = I`, `M₁ = Ñ`, `G(c⊗t) = c ⊗ X t₊ + Jc ⊗ K t₋` on `T⊗H`.

- **Exact value decomposition** (polynomial identity, d = 3, 5, 7):

      value = ½(1+x_z)(e₀+e_z)P + ½(1−x_z)(e₀−e_z)Q + (ē_T·x_T)α + (ē_T·J x_T)β.

- The last two terms are bounded by `|ē_T||x_T|√(α²+β²)` (Bessel; `x_T ⊥ J x_T`, `|J x_T| = |x_T|`).
- The first two are at least `√((1−x_z²)(e₀²−e_z²)PQ)` (AM–GM).
- **Exact identity:**

      PQ − α² − β² = (f₀² − f_x² − |f₋|²)|y₋|² + [|f₋|²|y₋|² − (f₋·y₋)² − (f₋·Ky₋)²] + (f₀² − f_x²)(1 − |y|²).

  On the sphere this is ≥ 0 by the cone condition and Bessel (`y₋·Ky₋ = 0`, `|Ky₋| = |y₋|`, both exact).
- posInv follows from `G² = I`.

Exact rational sampling (not a certificate) gives nonnegative values. The same evaluator reproduces `gJ5_value = −1/10`
and `gJ3_value = −1/10`.

**N4.3 — Answer.** relT + frame + P± **do not exclude any odd `d`**. For odd `d ≥ 5`, `C_d` has unbalanced eigenspaces
and fails relC. relC (through balance `p = q`, combined with `p ≤ 1`) is exactly what removes odd `d ≥ 5` in
`dim_of_nativeGate`.

### N5 — `d = 4` under frame + P± (no relation): excluded

Verdict: **written proof + exact algebra.** This is the favorable-to-framework branch, so maximum skepticism applied;
the pressure tests are listed under Open gaps.

Classify `σ = R ⊕ (−1)`, `R ∈ O(3)`, up to conjugation fixing `z`.

| R | outcome |
|---|---|
| (a) rotation plane `P` with angle ∉ {0, π} (proper or improper) | `A` maps `E_λ(σ) → E_{λ̄}(σ)` while `A|_P = cJ` preserves `E_λ`, so `A|_P = 0`. `a ∈ Fix σ ⊥ P`. Every block kills `lift P`, so `𝕂` is singular. Exact for symbolic angle (S4). |
| (b) `R = I` (`p_σ = 3`) | `Lsig` kills `lift z` (exact, S4) |
| (c) `R = −I` (`p_σ = 0`) | `Lsig` kills `e₀` (exact, S4) |
| (d) `R = diag(1,1,−1)` (`p_σ = 2`) | all E₊ blocks vanish; see below |
| (e) `R = diag(1,−1,−1)` (`p_σ = 1`, `q_σ = 2`) | no invertible `Ŝ ∈ S₃` with `Ŝ⁻¹ ∈ S₃`; see below |

**Case (d).** Take `y ∈ V₊` unit and `f = (1, w, 0, 0)` null. Then `P = Q = 1 + w·v`. With
`w = −(cos φ v + sin φ Jv)`:

    fᵀΓu = −sin φ (a·Jv ∓ c) + (1−cos φ) a·v   (exact identity),   P = 1 − cos φ.

The criterion `Σκ² ≤ PQ = O(φ⁴)` forces `a = 0` and `c = 0`. So every E₊ block vanishes and `𝕂` is singular.

The same argument kills `p_σ ≥ 2` in every `d`. It is a short substitute for NB-1's S3/S4 (`averaging_bound`).

**Case (e).** On `T⊗E₊` the block is `α ⊗ X`, where `X` exchanges `e₀ ↔ e₁`.

1. **`α` is orthogonal.** `f = (1,1,0,…)` gives `‖α‖ ≤ 1`, and posInv gives `‖α⁻¹‖ ≤ 1`.
2. **The block on `T⊗V₋` lies in a twisted `S₃`.** With `|αt| = 1`, flip `(f_x, y_x) → (−f_x, −y_x)` and scale
   `f₋ → ε f₋`. The term linear in `α' = f₀y_x + f_x` must vanish: `Σ_k (αt)_k B_{k,t} = 0`. This means
   `(αᵀ ⊗ I) 𝕂_V ∈ S₃ := {M : M^{T1} = −M, M^{T2} = −M}`.
3. **The same holds for the inverse.** `Gt⁻¹` has the same normal form, so `(α ⊗ I) 𝕂_V⁻¹ ∈ S₃`.
4. **Reduction to `S₃`.** `S₃` is invariant under conjugation by `O(3) ⊗ O(3)` (exact covariance, S1). So with
   `Ŝ := (αᵀ⊗I) 𝕂_V`: `Ŝ ∈ S₃` and `Ŝ⁻¹ ∈ S₃`.
5. **The `S₃` obstruction (written).** Contract `M M⁻¹ = I` with a unit control vector `v` on both sides:

       −Σ_{r=1}^{2} P_r R_r = I,   P_r, R_r antisymmetric 3×3.

   Using `[p×][q×] = q pᵀ − (p·q)I`, this says `Σ q_r p_rᵀ = λI`. The rank is ≤ 2, so `λ = 0`, so the trace gives
   `Σ p_r·q_r = 0`, so `λ = −1`. Contradiction.
6. **Exact corroboration** (S2):
   - for symbolic diagonal `C` (the general case after an SVD, by S1), `M_C M_{C'} = I` has no solution;
   - four specializations and four random rational non-diagonal `C` agree.
   - Controls: `S₂` (`J⊗J`, d = 3) and `S₄` (`J⊗K`, d = 5) admit inverse-closed invertible elements, and the solver
     finds them.

**Conclusion.** No `z` and no invertible `G` on `W 4` have the frame, posFwd and posInv. This is stronger than DIM-1's
`no_gate_four`, which assumes the full `NativeGate` and one common N.

### N6 — even `d ≥ 6` under frame + P± (± relT): open

**N6.1 — Reduction for involutive σ** (written). By N2–N5 in any `d`:

- `p_σ = 0`, `q_σ = 0` and `p_σ ≥ 2` are excluded. So `p_σ = 1`, `α ∈ O(d−1)`.
- An inverse-closed invertible `Ŝ ∈ S_{d−1}` is required.
- For `m = d − 1` even, `J ⊗ K` works; for `m = 1` (`S₁ = 0`) and `m = 3` (N5) it is impossible.

**N6.2 — `m = 5`** (d = 6), floating-point evidence only (`relt_Sm5_fast.py`, output `Sm5_fast.out`).

Least squares on `‖M M′ − I‖_F` over `M, M′ ∈ S_m`:

| m | starts | best residual | reading |
|---|---|---|---|
| 3 | 6 | `√3` (1.732) | control: exactly excluded (N5) |
| 4 | 3 | ~4e−16 | control: J⊗K exists |
| 5 | 2 | `√5` (2.236) | evidence of an obstruction |

The job was stopped by hand after 2 of the planned 12 `m = 5` starts. Each start took about 15 minutes.

The `√m` floor at both odd `m` suggests a general odd-`m` obstruction (**conjecture**, unproved). Even if it holds,
even `d ≥ 6` would still need non-involutive σ (N6.3) treated before it is excluded.

The single contraction identity of N5.5 is **solvable** at `m = 5` (`relt_contraction_numeric.py`: residual ~1e−15).
So the `m = 3` trace/rank trick alone does not generalize.

**N6.3 — Non-involutive σ with repeated rotation angles** (possible from `d ≥ 6`) is not treated.

## What survives under relT alone (replacing GateRel = relT ∧ relC)

| conclusion (landed under GateRel or NativeGate) | relT only | relT + frame | relT + frame + P± | evidence level of the new cells |
|---|---|---|---|---|
| injectivity of `Lop` (parity map) | **survives** | survives | survives | kernel reading (`Lop_eq_zero_rel` reads only relT) |
| anticommutation `Lop ∘ Pop = −Pop ∘ Lop` | fails | **fails** (CM2*, CM4*) | fails (C5) | exact |
| balance `dim E₊ = dim E₋` | fails | **fails** (CM*) | **fails** (C5, C7: (2,4), (2,6)) | exact; C_d positivity: written proof + exact identities |
| `d` odd | fails | **fails** (CM2*, CM4*: `d = 2, 4`) | `d = 2`, `d = 4` **excluded**, even without relT; `d ≥ 6` even **open** | written proof + exact algebra (N2.3, N5) |
| `p_N ≥ 1`, `q_N ≥ 1` | — | fails (CM4r: `q = 0`; CM4n: `p = 0`) | **holds**, every `d` | written proof + exact (N3.2) |
| `d = 3`: `N` a π-rotation, `det N = 1` (`piRotation_three`, `det_three`) | fails | **fails** (refl3/negId3 admitted) | **survives** | written proof + exact (N3.2, A3) |
| `not_gateRel_refl3`, `not_gateRel_negId3` | fail | fail | **survive** (as exclusions under relT + frame + P±) | as above |
| `p ≤ 1` (block data) | — | — | survives for `p_σ`; for `p_N` when `N = σ` | written proof (N5, case (d)); kernel route: relC enters §Q only via `gate_corner_neg` |
| selector `d ∈ {1, 3}` | fails | fails | **fails**: every odd `d` realized (`C_d`) | written proof + exact identities, `d = 3, 5, 7` exact checks |
| `p = q` (S5) | fails | fails | **fails** (C5) | exact |

## Controls (all green at the end of the walk)

| script | positive controls (reproduce landed facts) | countercontrols (must fail) | result |
|---|---|---|---|
| `relt_q1q2q3_exact.py` | DIM-1 `cnot`/`nflip`: frame, relT, relC, `G²=I`, (2,2), `Lop` injective + anticommuting; `gJ3_value = −1/10`; `gateRel_gJ3` | relC fails on every controlled-N model; identity gate and wrong-corner projector fail the frame | 77/77 |
| `relt_pos_exact.py` | `cnot`, `C3` normal form in `Lsig` with invertible tangent block; `C3` satisfies relC (complex CNOT) | `gJ3`, `gJ5`, controlled-N fail the `Lsig` necessary conditions; `gJ5_value = −1/10` reproduced; `nflip` A2/A3 countercontrols | 60/60 |
| `relt_S_exact.py` | `S₂` (`J⊗J`) and `S₄` (`J⊗K`) inverse-closed elements found | `S₃`: none (symbolic, specialized, random) | 15/15 |
| `relt_d4_rank_probe.py` | `d = 3` nflip: full rank 8 | `d = 2`: rank 2/3; `d = 3` refl3-type and `−id` σ: 6/8 | controls ok |
| `relt_Sm_numeric.py`, `relt_Sm5_fast.py` (float) | `m = 2, 4` residual ~0 | `m = 3` residual `√3` | evidence only. The first script was killed at its time limit, after printing `m = 2, 3, 4`. |

Bug found and fixed during the walk: the symbolic-angle `Lsig` solver first mis-ranked a matrix over `ℚ(m)` (it
reported dim 8). It now clears denominators and uses `cancel` as its zero test, and gives dim 1 at `d = 4`
(symbolic), matching the rational instance `m = 1/2`. The A3 and S4 rows were re-run after the fix.

## Classification

- **NEW**
  - N1.2/N1.3: relT + frame do not give balance or oddness; explicit `d = 2, 4` countermodels (exact).
  - N2.3 + N5: frame + posFwd + posInv **alone** exclude `d = 2` and `d = 4`, with no relation and no NOT
    (written proof + exact algebra).
  - **Hidden assumption exposed:** DIM-1/NB-1 attribute the even-`d` exclusion to parity (relT + relC). For
    `d ≤ 4`, that exclusion is already forced by the frame and two-sided positivity. relC's irreplaceable work is
    removing the odd `d ≥ 5`.
- **NEW**
  - N3.2: relT + frame + P± ⇒ `p_N, q_N ≥ 1` in every `d`; at `d = 3`, `N` is a π-rotation without relC.
  - N2.2: for involutive σ, relT is automatic after normalization.
- **ELABORATING:** N1.1, the exact relC site in the parity argument and in DIM-1 §Q (only `gate_corner_neg`).
- **CONFIRMING / POSITIVE:** N4. C5 confirmed with an independent positivity proof, extended to the whole odd family
  `C_d` (C7 checked exactly).
- **BORDERLINE / open:** N6, even `d ≥ 6`.

Assumption-watch marker, for propagation to other claims: *"parity excludes even d"* claims should say whether the
exclusion needs the relations or already follows from the frame + two-sided positivity. At `d ≤ 4` it is the latter.

## Open gaps (stated precisely; nothing here is claimed beyond them)

1. **Nothing new is kernel-checked.** Every NEW item is a written proof plus exact computation.
2. **The written proofs N2.1–N2.3 and N5 rest on several unbuilt steps:**
   - (a) `corner_form` applied at `−z` to `(I⊗ρ̃_z)∘G`;
   - (b) the `1 ⊕ O(d)` form of cone automorphisms fixing `e₀`;
   - (c) the necessity half of the positivity criterion;
   - (d) the linear-term and contraction arguments of case (e).

   Each is elementary. None has a landed kernel statement in this form.
3. **Even `d ≥ 6`:** open. Two pieces are needed: the inverse-closed `S_m` question for odd `m ≥ 5`, and
   non-involutive σ with repeated rotation angles. Even if `S_m` admits inverse-closed elements, the norm conditions
   (the contraction parts of the criterion) are untested.
4. **posFwd alone (no posInv)** is not treated. Every positivity exclusion above uses posInv, which makes the corner
   maps automorphisms and `α` orthogonal. This matches NB-1's open item.
5. **N3.2 needs P±.** Under relT + frame without positivity, the d = 3 conclusions fail (N3.1).

## What a later governed round could freeze (suggestions only)

- **Kernel, cheap:**
  - the controlled-N gate at `d = 2` (and the general-`d` statement) with frame, relT, `G² = I`, `¬ relC` and
    unbalanced eigenspaces, refuting "relT + frame ⇒ ¬ Even d" (draft statements in `RelTDraft.lean`, UNBUILT);
  - `Lop_injective` from relT alone (a re-proof reading only relT).
- **Kernel, moderate:**
  - parametrize DIM-1 §Q by the `−z` corner identity instead of relC, so the block data is derived from frame + P± +
    relT + that identity;
  - the relation-free `d = 2` exclusion. It reuses `corner_form`, `tangent_vanish`, `lor_cornerMap` and
    `isometry_of_contractions`; the singular `Lsig` is a 3×3 computation.
- **Kernel, harder:**
  - `C_d` positivity at `d = 5` (the value identity is polynomial; AM–GM and Bessel are short), giving "relT + frame +
    P± ⇏ d ∈ {1,3}" in the kernel;
  - the `d = 4` relation-free exclusion.
- **Exact computation layer:** these scripts, with their controls, are already deterministic and exact.

## Files

- `relt_common.py`: carrier, hypotheses, the parity map `Lop`/`Pop` built as in §H–§I, the controlled-N gate, and
  DIM-1's `cnot` transcribed from §K.
- `relt_q1q2q3_exact.py`: N1, N3.1 and their controls.
- `relt_lsig.py`: the exact `Lsig` solver.
- `relt_pos_exact.py`: N2.3, N3.2, N4 and the A1–A4 / B rows.
- `relt_d4_rank_probe.py`: N2.4.
- `relt_S_exact.py`: N5.
- `relt_Sm_numeric.py`, `relt_contraction_numeric.py`: N6, floating-point evidence only.
- `RelTDraft.lean`: UNBUILT Lean design draft (statements and routes only).
