# Finite native-gate ball no-go — packaged result (read-only, from L42)

Baseline `fdebc6e3`.
- Proof: `PROOF-S1-S5.md`.
- Checks:
  - `s12_exact.py`: 73 PASS, 0 FAIL;
  - `s12_controls.py`: 7 PASS, 0 FAIL;
  - `uniform_nogo.py`: 8 PASS, 0 FAIL;
  - `audit_two_nots.py`: the two-NOT countercontrol.
- Prior art: `PRIOR-ART.md`.
- Nothing is committed.

## Statement

**Setting.**
- Two copies of the d-ball system: `ℝⁿ = ℝu ⊕ ℝᵈ` with `n = d+1`. States form the Lorentz cone `L`, and effects are
  **all** of `L` (self-dual, no restriction).
- The composite is locally tomographic: `ℝⁿ⊗ℝⁿ`, with the product cone `min` and its dual `max`.
- A classical frame: the antipodal pure states `k_a = u + (−1)^a z`.
- **One** ball involution `N` (orthogonal on `ℝᵈ`, fixing `u`) with `Nz = −z`, acting identically on both factors.

**Hypotheses on a linear map `G`.**

| label | hypothesis |
| --- | --- |
| **F** | `G(k_a⊗k_b) = k_a⊗k_{a⊕b}` |
| **P±** | `G` is invertible, `G(min) ⊆ max` and `G⁻¹(min) ⊆ max` |
| **Rt** | `(I⊗N) G (I⊗N) = G` |
| **Rc** | `(N⊗I) G (N⊗I) = (I⊗N) G` |

**Conclusion.** `d ∈ {1, 3}`.

## Dependency graph

    P (both directions) + F ──S1──▶ G(k_a⊗t) = k_a⊗M_a t, M_a isometries, M₁ = N M₀, N M_a N = M_a
    corner tangent constraints ─S2─▶ G(I⊗M₀⁻¹) = [[0, A_r],[A_r, B_rs]] on T⊗E₊  ⊕  antisymmetric on T⊗V₋
    max-cone positivity ──S3, S4──▶ p ≤ 1   (else ker G ⊇ T⊗E₊, of dimension (d−1)(p+1))
    Rc + injectivity ──S5──▶ p = q          (anticommuting with an involution swaps its eigenspaces)
    p + q = d − 1 ─────────────────▶ d ∈ {1, 3}

Here `p` and `q` are the dimensions of the `±1` eigenspaces of `N` on the transverse space `T`,
`E₊ = ℝu ⊕ (+1 space)` and `V₋ = (−1 space) ⊕ ℝz`.

## Countercontrols: each hypothesis is load-bearing

| drop or break | construction | result | check |
| --- | --- | --- | --- |
| **Rc**, the control-NOT relation | d = 5 J/K map (`p = 1`, `q = 3`) | F, P±, Rt and `G² = I` hold; exact positivity by reduction to the complex CNOT. **Survives.** | `s12_controls.py` C5; `BALL5-FINITE.md` §1 |
| **the same N on both factors** | d = 5, `N_A` (`p = q = 2`) on the control, `N_B` (`p = 1`) on the target | F, P±, `G² = I`, Rt with `N_B` and Rc with `(N_A, N_B)` all hold; positivity exact (J/K reduction), numerical minimum −8e−16. **Survives.** | `audit_two_nots.py` |
| **positivity**, keeping all the algebra | d = 7 candidate: F, `G² = I`, Rt, Rc, and the S1/S2 form | S4 fails (`A_x ≠ 0`); max-cone violation at exactly `1 − √3` | `uniform_nogo.py`; `s12_controls.py` C7 |
| — | d = 3 complex CNOT | every hypothesis holds; `p = q = 1` | C3 |
| — | d = 2 | `p = q` is impossible when `p + q = 1` | C2 |

What the second row means: with different NOTs, S4 bounds the target's `N_B` (`p_B ≤ 1`) and S5 balances the
control's `N_A` (`p_A = q_A`). Every odd d then survives. Identifying the two NOTs is what couples S4 to S5.

## Hidden-assumption audit

| possible hidden assumption | status |
| --- | --- |
| normalization of `G` (`(u⊗u)ᵀG = (u⊗u)ᵀ`) | **not used** — no step refers to it |
| `G² = I` | **not used** — S1 uses `G⁻¹`'s positivity; S5 uses only injectivity |
| an intermediate cone `C` with `G(C) = C` | **not used** — only P± on products |
| a continuous or any local group beyond `N` | **not used** |
| the swap relation | **not used** |
| **one `N` on both factors** | **used, and load-bearing** (row 2 above). Natural when the factors are identical copies and exchange is a symmetry that intertwines `N⊗I` with `I⊗N`. It must be stated as a hypothesis |
| the effect cone is all of `L` (no restriction) | **used**: in the definition of `max` and in the corner and equator effects of Lemma A |
| the corners are antipodal pure states | intrinsic to a two-outcome frame on a ball |
| local tomography (`ℝⁿ⊗ℝⁿ`) | **used**, by construction |
| `d ≥ 2` in S4 | used (`T ≠ 0`); `d = 1` is allowed by the conclusion |
| inverse positivity P⁻ | **used**, only in S1 (to make `M_a` isometries) |

## Open strictly stronger variant

Is `G` injective with `G(min) ⊆ max` alone (no inverse positivity) enough to force `d ∈ {1, 3}`?

P⁻ enters only to make the `M_a` isometries. A countermodel with a strictly contracting `M_a` would show P⁻ is
necessary; a new isometry argument would strengthen the theorem. Recorded as open; it does not hold up the present
statement.
