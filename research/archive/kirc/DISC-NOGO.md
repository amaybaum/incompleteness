# Disc-composite existence problem — read-only result, from L42

Baseline `fdebc6e3`. Exact certificate: `disc_nogo.py` (sympy over ℚ; 17 PASS, 0 FAIL; log `disc_nogo.log`).
Numerical cross-check, evidence only: `disc_cnot_search.py` (log `search_disc.log`). Nothing is committed.

## Statement (exact)

Setting.
- **Local systems.** Discs: the normalized base of the Lorentz cone `L₃`.
- **Composite.** A closed cone `C ⊆ ℝ³⊗ℝ³` with `L₃ ⊗min L₃ ⊆ C ⊆ L₃ ⊗max L₃`, so local tomography is built in.
- **Local rotations.** `T = SO(2)×SO(2)` acts on `C`.

**Theorem.** Every normalization-preserving linear automorphism of `C` normalizes `T`. Consequently no such automorphism
acts as CNOT on the four classical products. The proof uses neither `G² = I` nor any native relation.

It follows that the weak family is empty and the native-faithful family is empty, for both local-NOT choices.

## Proof, with each step checked exactly

- **N1 — compactness.**
  - `Aut(C)` (normalization-preserving) is compact: it preserves the base of `C`, which is compact and spans the
    affine hyperplane.
  - Its identity component `K₀` contains `T`, and `𝔨 = Lie(K₀)` is `Ad(T)`-invariant.
- **N2 — the first-order boundary condition.**
  - Take `X ∈ 𝔨`, a pure product `p = p_v⊗p_w`, and the effect `f_v = (1,−v)` that vanishes on `p_v`.
  - Then `s ↦ (f_v⊗g)(e^{sX}p) ≥ 0` for every effect `g`, and it vanishes at `s = 0`. Hence
    `(f_v⊗I)Xp = 0`, and symmetrically `(I⊗f_w)Xp = 0`. Normalization gives `(u⊗u)ᵀX = 0`.
  - Sampling rational points on the circle gives a superset of the true solution space. That superset has dimension 7.
- **N3 — torus weights.** The 7-dimensional space is `𝔱 ⊕ W₁₀ ⊕ W₀₁ ⊕ ⟨E₄⟩`:
  - `W₁₀` and `W₀₁` are 2-dimensional blocks of weights (1,0) and (0,1);
  - `E₄` has weight 0.
- **N4 — the Lie bracket cuts off the nonlocal blocks.**
  - `[W₁₀, W₁₀]` and `[W₀₁, W₀₁]` leave the space.
  - So a Lie subalgebra `𝔱 ⊆ 𝔨 ⊆ Λ` meets both blocks trivially, since `𝔨` splits along isotypic components.
- **N5 — compactness removes `E₄`.**
  - `E₄` commutes with `𝔱` and has a real eigenvector with eigenvalue 1, and `T` is orthogonal.
  - So `exp(s(aT₁+bT₂+cE₄))` is unbounded whenever `c ≠ 0`.
  - Hence `𝔨 = 𝔱` and `K₀ = T`, which makes `T` normal in `Aut(C)`.
- **N6 — the frame contradiction.**
  - A map that normalizes `T` sends each real `T`-isotypic block onto a single block.
  - The frame forces `G(u⊗z) = z⊗z`. Here `u⊗z` lies in the (0,1) block, while `z⊗z` has nonzero components in both
    the (1,1) and (1,−1) blocks.
  - This is a contradiction.

## Controls

| id | control | result |
| --- | --- | --- |
| **C1** | Bloch ball (`n = 4`): the complex CNOT meets the frame and is an involution. All 15 `su(4)` generators satisfy the `n = 4` first-order conditions, whose space has dimension 65. | PASS — the method does not exclude complex QM |
| **C2** | Swap and local reflections normalize `T`. | PASS — the discrete symmetries the min tensor product really has survive |
| **C3** | The four nonlocal real `so(4)` generators project exactly onto `W₁₀ ⊕ W₀₁`. | PASS — the first-order space is where real QM leaks in; N4 is where it is cut off |

## Numerical cross-check (evidence only, superseded by the exact result)

- **Weak disc family, 40 parameters, 16 restarts.** Best validated slack is about −2.09, with residual about 6e−6.
- **Native disc families, 12 parameters.** The involution and `S`-relation residual never falls below 3.0 (NOT =
  reflection) or 4.0 (NOT = rotation). This suggests the native relations are already algebraically inconsistent with
  `G² = I` on the disc, before any cone is involved. That was not certified.
- **Calibration.** The complex CNOT lies in the ball's native family, with residual 0 and slack −9e−16.

## Scope

- **Continuity of the interaction is not assumed.** It is derived: compactness of `Aut(C)` yields a Lie group, and the
  proof shows it has no nonlocal continuous part.
- **Continuity of the local rotations is used.** `T` must be the full `SO(2)×SO(2)`. The no-go therefore concerns real
  pair *flows* (R's real part) together with the native discrete coupling. With only a finite local rotation group the
  argument does not apply. [open]
- **What is excluded is the disc.** The theorem does not identify the enlargement. C1 shows the 3-ball survives. Balls of
  dimension ≥ 4 (among them the quaternionic 5-ball) are not tested here.
- **The rest of `N(T)` is not characterized.** `Aut(C) ⊆ N(T)` does not say which `T`-normalizing entangling maps, if
  any, survive. One sign flip on the `ρ⊗ρ` block already fails the max cone.
