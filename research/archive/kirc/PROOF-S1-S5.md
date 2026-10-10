# The native-relations ball theorem — S1–S5 with exact checks (read-only, from L42)

Baseline `fdebc6e3`. This supersedes the proof sketch in `UNIFORM-NOGO.md`.
- Checks:
  - `s12_exact.py`: 73 PASS, 0 FAIL, log `s12_exact.log`; covers d = 2…7 and every eigenspace split `p`.
  - `s12_controls.py`: 7 PASS, 0 FAIL, log `s12_controls.log`.
  - `uniform_nogo.py`: the d = 7 witness.
- Nothing is committed.

## Setting and hypotheses

**Vector space and cone.**
- `ℝⁿ = ℝu ⊕ ℝᵈ` with `n = d+1`, and `ℝᵈ = T ⊕ ℝz`, where `T` is the transverse space, of dimension `d−1`.
- `L` is the Lorentz cone, which is self-dual.
- The corners are `k_a = u + σ_a z` with `σ_a = (−1)^a`. They are also the effects `⟨a|`, since `k_a·k_b = 2δ_ab`.
- `min` is the cone of products of states. `max` is the set of `W` with `(f⊗g)(W) ≥ 0` for all `f, g ∈ L`.
- For a pure `w = u + w'`, the effect `g⊥(w) = u − w'` is the one that vanishes on `w`.

**N.** A normalized automorphism of the ball, that is, orthogonal on `ℝᵈ` and fixing `u`, which is an involution with
`Nz = −z`.
- Its `±1` eigenspaces in `T` are `V₊` (dimension `p`) and `T₋` (dimension `q`).
- `V₋ = T₋ ⊕ ℝz`, and `E₊ = ℝu ⊕ V₊`.
- The same `N` acts on both factors.

| label | hypothesis |
| --- | --- |
| **F** | `G(k_a⊗k_b) = k_a⊗k_{a⊕b}`, the frame |
| **P** | `G(min) ⊆ max` |
| **P⁻** | `G` is invertible and `G⁻¹(min) ⊆ max` |
| **Rt** | `(I⊗N) G (I⊗N) = G` |
| **Rc** | `(N⊗I) G (N⊗I) = (I⊗N) G` |

**Theorem.** F, P, P⁻, Rt and Rc together imply `d ∈ {1, 3}`.

Not used:
- the existence of an intermediate cone `C` with `G(C) = C`;
- `G² = I`;
- normalization of `G`;
- the swap relation;
- any local group beyond `N`.

**Lemma A (boundary derivative).** Let `θ ↦ W(θ)` be differentiable with `W(θ) ∈ max` near `0` on both sides, and let
`h` be a product effect with `h(W(0)) = 0`. Then `h(W′(0)) = 0`. The same holds for a differentiable curve of product
effects `h(φ)` at a fixed `W`.

## S1 — controlled form (consumes F, P, P⁻, Rt, Rc)

1. **The target curve.** For `t ∈ T` unit and `t_θ = u + cos θ z + sin θ t`, which is pure, F gives
   `G(k_a⊗t_θ) = cos²(θ/2) k_a⊗k_a + sin²(θ/2) k_a⊗k_ā + sin θ·Z_a(t)`, with `Z_a(t) = G(k_a⊗t)`.
   [identity and vanishing derivatives: checks `A`]
2. **The corners.** Apply Lemma A at `θ = 0` with the effects `k_ā⊗g` and `f⊗k_ā`, and at `θ = π` with `k_ā⊗g` and
   `f⊗k_a`. This gives `(k_āᵀ⊗I)Z = 0` and `(I⊗k₀ᵀ)Z = (I⊗k₁ᵀ)Z = 0`. So `Z ∈ span{k_a, T}⊗T`.
3. **The equator.** At `θ = π/2`, use the effect curve `f(φ) = (1, −σ_a cos φ z + sin φ τ)`, which is `k_ā` at
   `φ = 0`. Lemma A in `φ` kills the `T⊗T` part.
   - Hence `Z_a(t) = k_a⊗M_a t` with `M_a : T → T` linear. [**S1**, exact nullspace equality for d = 2…7, both `a`]
   - Evaluating on effects with `f·k_a > 0` gives `‖M_a‖ ≤ 1`.
4. **The full map.** Extend `M_a` by `M_a u = u` and `M_a z = σ_a z` (frame). Then `G(k_a⊗t) = k_a⊗M_a t` for all
   `t ∈ ℝⁿ`.
5. **Isometries (P⁻).** `G⁻¹` also acts as CNOT on the corners, so steps 1–4 apply to it:
   `G⁻¹(k_a⊗t) = k_a⊗M′_a t` with `‖M′_a‖ ≤ 1` and `M′_a M_a = I`. Hence each `M_a` is an isometry.
   **This is the only use of P⁻.**
6. **The native relations.** Applied to `k_a⊗t`:
   - Rt gives `N M_a N = M_a`;
   - Rc gives `M_ā = N M_a`, since `N k_ā = k_a`. So `M₁ = N M₀`.

## S2 — block structure (consumes P, S1, Rc)

**The control curve.** For `c ∈ T` unit (the control's transverse space), let
`s_θ = cos²(θ/2) k_a + sin²(θ/2) k_ā + sin θ c`, which is pure. Then
`G(s_θ⊗t) = cos²(θ/2) k_a⊗M_a t + sin²(θ/2) k_ā⊗M_ā t + sin θ·G(c⊗t)`.

**The effects vanishing at `θ = 0`.** Since `M_a t` is pure (S1.5), these are `k_ā⊗g` for any `g`, and `f⊗g⊥(M_a t)`
for any `f`. Lemma A then gives:
- (i) `G(c⊗t) ∈ T⊗ℝⁿ`, using both values of `a`;
- (ii) `(I⊗g⊥(M_a t)ᵀ) G(c⊗t) = 0` for `a = 0, 1` and every pure `t`.

**Reducing to a linear condition.** Substitute `t̃ = M₀t` and set `G̃ = G(I⊗M₀⁻¹)`; by S1, `M₁ = N M₀`. Condition (ii)
becomes linear in the unknown `Φ = G̃(c⊗·)`:

> for every unit `t′ ∈ ℝᵈ`: `(1, −t′)·Φ(u+t′) = 0` and `(1, −Nt′)·Φ(u+t′) = 0`, one output component at a time.

**Solving it.** Split into parity. The odd part gives `α ∈ T⊗V₊` for `α = Φ(u)`, and makes the u-component of
`Φ(e)` equal to `(I⊗eᵀ)α`. The even part forces two bilinear forms to be antisymmetric, with
`(ν_i − ν_j)β(i,j) = 0`, where `ν_i = ±1` are the eigenvalues of `N` on the basis vectors `e_i`. Taking `t′ ∈ V₋`
then gives α's u-component = 0.

**The solution space is exactly:**

- `G̃(c⊗u) = Σ_r A_r c ⊗ e_r` (`r` runs over `V₊`);
- `G̃(c⊗e_s) = A_s c ⊗ u + Σ_r B_rs c ⊗ e_r` for `e_s ∈ V₊`, with the **same** `A_s` and `B_rs = −B_sr`;
- `G̃(c⊗e_j) ∈ T⊗V₋` for `e_j ∈ V₋`, antisymmetric in the `V₋` indices.

This has dimension `p + p(p−1)/2 + q(q+1)/2`.

[**S2**, for d = 2…7 and every `p`:
- the family satisfies the constraints identically, as a symbolic polynomial identity in `t′`;
- the sampled constraint system has nullity ≤ the family's rank (an exact modular bound);
- so the solution space equals the family.]

**The transposed form fails.** The alternative `(u, r) = −(r, u)`, which is the bug found earlier, violates the
constraint. [checked for every `p ≥ 1`]

## S3 — averaging bound (pure algebra)

For `X = [[1, gᵀ],[g, I+K]]` on `ℝ^{p+1}` with `K` antisymmetric, suppose `X(1,t) ∈ L` for the `2p` unit vectors
`t = ±e_i`. That is, `1 + g·t ≥ |g + (I+K)t| ≥ 0`.

Squaring and summing:

    Σ_{t=±e_i} [(1+g·t)² − |g+(I+K)t|²] = −2((p−1)|g|² + ‖K‖²_F) ≥ 0.

**So for `p ≥ 2`, `g = 0` and `K = 0`.** [symbolic identity, `p = 1…8`; only a finite orthonormal set is used]

## S4 — the E₊ block is killed (consumes P, S1, S2, Rt, invertibility)

**The configuration.** Take the state `s = u + c` and the effect `f = u + a`, with `a, c ∈ T` unit; the target
`t = u + t₊` pure, with `t₊ ∈ V₊`; and the effect `g = (1, b)` with `b ∈ V₊` unit.

**The value.**
- By Rt, `M₀` preserves `E₊`, so `G(u⊗t) = u⊗M₀t`.
- Therefore `(f⊗g)(G(s⊗t)) = (1,b)ᵀ(I + Γ_ac)(1, M₀t₊)`, where `Γ_ac = [[0, γᵀ],[γ, K]]`, `γ_r = a·A_r c` and
  `K_rs = a·B_rs c` is antisymmetric. [symbolic identity with generic `A_r`, `B_rs`, d = 5 and d = 7]
- `M₀` is a bijection of the unit sphere of `V₊`, and the value is ≥ 0 by P. So `I + Γ_ac` is Lorentz-positive.

**The conclusion.**
- S3 gives, for `p ≥ 2`, `a·A_r c = 0` and `a·B_rs c = 0` for all `a, c`.
- So `A_r = 0` and `B_rs = 0`, and `G̃` vanishes on `T⊗E₊`.
- **Killed subspace:** `ker G ⊇ T⊗E₊`, of dimension `(d−1)(p+1) > 0`.
- This contradicts invertibility. **So `p ≤ 1` whenever d ≥ 2.**

## S5 — parity (consumes invertibility, S2, Rt, Rc)

**Abstract lemma.** If `L` is injective on a finite-dimensional space, `Π` is an involution, and `LΠ = −ΠL`, then `L`
maps `E₊(Π)` injectively into `E₋(Π)` and vice versa. Hence `dim E₊(Π) = dim E₋(Π)`.

**Applying it.**
- By S2 and Rt, `G` maps `T⊗V₋` into itself.
- There, Rc reads `(N_A⊗I) G (N_A⊗I) = −G`.
- Take `Π = N_A⊗I`. Its eigenspaces are `V₊⊗V₋` and `T₋⊗V₋` on the control side.
- So `p·dim V₋ = q·dim V₋`, that is, **`p = q`**.
- `G² = I` is not needed, only injectivity.

**Conclusion.** `p = q ≤ 1` and `p + q = d − 1`, so `d ∈ {1, 3}`. ∎

## Countercontrols (`s12_controls.py`, exact arithmetic)

| control | hypotheses and structure | outcome |
| --- | --- | --- |
| **C3** complex CNOT, d = 3 | F, S1 (`M₀ = I`, `M₁ = N`), isometries, S2 structure, Rt, Rc all hold; `p = q = 1` | survives: S3 is vacuous at `p = 1` |
| **C5** J/K map, d = 5 | F, S1, S2 and Rt hold, with `p = 1`, `q = 3`; **Rc fails** | survives, since S5 is exactly where it fails. Positivity is exact, by reduction to C3 (`BALL5-FINITE.md` §1). The control relation is load-bearing |
| **C2** d = 2 | `p + q = 1` admits no `p = q` | excluded |
| **C7** algebraic candidate, d = 7 | F, `G² = I`, Rt, Rc, S1 and S2 structure all hold; `p = 3` | S4 fails because `A_x = I ≠ 0`; max-cone positivity is violated at the exact value `1 − √3` |

## Which hypotheses each step consumes

| step | F | P | P⁻ | Rt | Rc | invertible |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | ✓ | ✓ | ✓ (isometry only) | ✓ (`NM_aN = M_a`) | ✓ (`M₁ = NM₀`) | ✓ (via P⁻) |
| S2 | | ✓ | via S1 | | via S1 | |
| S3 | | | | | | |
| S4 | | ✓ | | ✓ | via S1 | ✓ |
| S5 | | | | ✓ | ✓ | ✓ |

**On the stronger statement.**
- The proof needs P and P⁻ (two-sided positivity on products), which is weaker than the existence of an intermediate
  cone `C`.
- P⁻ enters only to make `M_a` an isometry, so that `M_a t` is pure and has a unique vanishing effect. With one-sided
  P alone, a strictly contracting `M_a` is not excluded by this proof.
- Whether "injective + P" suffices is **open**. It needs either a new argument for isometry or a countermodel.
