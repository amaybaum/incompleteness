# Ball-composite CNOT no-go for every d ≠ 3 — read-only, from L42

Baseline `fdebc6e3`. This extends `DISC-NOGO.md` (d = 2) to every d ≥ 2 other than 3.
- Exact per-dimension checks: `ball_nogo.py`, log `ball_nogo.log` (d = 5, 4, 2, 3, in that order).
- The proof below is uniform in d; the computations control it and do not replace it.
- Nothing is committed.

**Finite local symmetry remains open.** Every statement below assumes the full continuous local group `SO(d)×SO(d)`.

## Setting

- **Local system.** The unit d-ball (normalized base of `L_{d+1}`), with `n = d+1`.
- **Composite.** `V = ℝⁿ⊗ℝⁿ`, so local tomography is built in; a closed cone `C` with `min ⊆ C ⊆ max`.
- **Local group.** `L = SO(d)×SO(d) ⊆ Aut(C)`.
- **Decomposition.** `V = 𝟏 ⊕ A ⊕ B ⊕ AB`, with `A = ℝᵈ⊗u`, `B = u⊗ℝᵈ`, `AB = ℝᵈ⊗ℝᵈ`.
- **Classical frame.** `u ± z` on each side. CNOT on the corners forces `G(u⊗z) = z⊗z`.

**Theorem (d ≥ 2, d ≠ 3).** Let `G` be a normalization-preserving linear automorphism of `C`. Then `G` cannot map
`u⊗z` to `z⊗z`. In particular no reversible map acts as CNOT on the classical corners. Neither `G² = I` nor any native
relation is used. At d = 3 a CNOT-on-corners map exists: complex QM.

## Proof (uniform in d)

**Hypothesis on reversible maps (H1).** A reversible map is an invertible linear `G` on `V` with `G(C) = C` and
`e∘G = e`, where `e = u⊗u` is the normalization functional; that is, `G` maps normalized states onto normalized
states. Let `Aut_e(C)` be the group of such maps. Preserving the cone alone is not enough: positive dilations preserve
`C` and are unbounded.

**Step 0 — compactness.**
- `G` maps the base `Ω_C = C ∩ {e = 1}` onto itself.
- `Ω_C ⊆ Ω_max`, and `Ω_max` is compact, because `max` is the dual of `min`, which has nonempty interior. So `Ω_C` is
  compact.
- `Ω_C` contains all normalized products, and these affinely span `{e = 1}`, which spans `V`.
- So there is a uniform `R` with `‖Gx‖ ≤ R` for every `G ∈ Aut_e(C)` and every `x` in a fixed basis drawn from
  `Ω_C`. `Aut_e(C)` is therefore bounded; it is closed because `C` is closed; so it is a compact subgroup of `GL(V)`.
- Consequence used in Step 3: a one-parameter subgroup `e^{sX}` of a compact group is bounded, so `X` has no real
  nonzero eigenvalue. A nonzero real symmetric `X` always has one.
- Let `K₀` be the identity component and `𝔨` its Lie algebra. Then `𝔩 = 𝔰𝔬(d)⊕𝔰𝔬(d) ⊆ 𝔨`, and `𝔨` is
  `Ad(L)`-invariant.

**Step 1 — the first-order space, exactly.**
- *The boundary condition.* For `X ∈ 𝔨`, a pure product `p_v⊗p_w` and the effect `f_v = (1,−v)`, the function
  `(f_v⊗g)(e^{sX}p) ≥ 0` vanishes at `s = 0`. So `X(p_v⊗p_w) ∈ T_v⊗T_w`, where `T_v = ker f_v`.
- *Unpacking it.* Separate by parity and degree in `v` and `w`, and homogenize using `|v| = |w| = 1`.
- *The result.* `Λ = 𝔩_A ⊕ 𝔩_B ⊕ Σ_A ⊕ Σ_B ⊕ Z`, where:
  - **`Σ_A ≅ Λ²A ⊗ B`** consists of the antisymmetric couplings `A ↔ AB`, namely
    `X_{AB←A} a = Ωa ⊗ f` and `X_{A←AB} = −X_{AB←A}ᵀ`;
  - **`Σ_B ≅ A ⊗ Λ²B`** is its mirror image;
  - **`Z ≅ Λ²A ⊗ Λ²B`** acts on `AB` only.
- *Dimension.* `dim Λ = d(d−1) + d²(d−1) + (d(d−1)/2)²`.
- *Check [U1].* At every d tested, the sampled first-order space equals this family exactly:
  - the family satisfies every sampled constraint exactly over ℤ;
  - the sampled nullity mod p equals the family's rank;
  - and nullity over ℚ ≤ nullity mod p, while random row compression can only raise the nullity bound.

**Step 2 — isotypic separation for d ≥ 4.** The ad-Casimir pairs `(c_A, c_B)` of the five pieces are:

| piece | `(c_A, c_B)` |
| --- | --- |
| `𝔩_A` | `(c_Λ, 0)` |
| `𝔩_B` | `(0, c_Λ)` |
| `Σ_A` | `(c_Λ, c_V)` |
| `Σ_B` | `(c_V, c_Λ)` |
| `Z` | `(c_Λ, c_Λ)` |

Here `c_V = −(d−1)` and `c_Λ = −2(d−2)`.
- The pairs are pairwise distinct unless `c_Λ = 0` (d = 2) or `c_Λ = c_V` (d = 3) [U2].
- For d ≥ 4 the projections onto the pieces are polynomials in the Casimirs, so
  `𝔨 = 𝔩 ⊕ (𝔨∩Σ_A) ⊕ (𝔨∩Σ_B) ⊕ (𝔨∩Z)`.

**Step 3 — Z is excluded by compactness.** Every nonzero element of `Z` is a real symmetric operator [U4]. It
therefore has a real nonzero eigenvalue, so its one-parameter group is unbounded. Hence `𝔨∩Z = 0`.

**Step 4 — Σ_A and Σ_B are excluded by the bracket.**
- Let `U = 𝔨∩Σ_A` be nonzero, and take `S_σ ∈ U` with `σ = Σ_k Ω_k⊗f_k`.
- `U` is invariant under `1×SO(d)`, and `Ad_{(1,h)} S_σ = S_{(1⊗h)σ}`.
- By Burnside, rotations of `ℝᵈ` span `End(ℝᵈ)` for d ≥ 3 [U5]. So `U ∋ S(Ω⊗f₁)` and `S(Ω⊗f₂)` with `Ω ≠ 0` and
  `f₁ ⊥ f₂`.
- *The bracket.* `[S(Ω⊗f₁), S(Ω⊗f₂)]` has zero `A` and `B` blocks, and its `AB` block is `±Ω² ⊗ (f₁f₂ᵀ − f₂f₁ᵀ)`.
- *Why that is not allowed.* Membership in `Λ` forces `(vᵀ⊗I)X_{AB←AB}(v⊗w) = |v|² X_{B←B}w = 0`. But the bracket
  gives `∓|Ωv|²(f₁f₂ᵀ − f₂f₁ᵀ)w ≠ 0`.
- So the bracket lies outside `Λ ⊇ 𝔨`, which contradicts closure. An exact rational witness point is exhibited for
  `Ω = e₁∧e₂` [U3]; at d = 4 the self-dual and anti-self-dual `Ω` are also tested. The same argument applies to `Σ_B`.

**Step 5 — conclusion for the connected group.** `𝔨 = 𝔩`, so `K₀ = L`, and `L` is normal in `Aut(C)`.

**Step 6 — the normalizer.**
- Take `G ∈ Aut_e(C)`. Since `K₀ = L` is normal, `φ(X) = G X G⁻¹` is an automorphism of `𝔩`. Nothing is assumed
  about which automorphism it is: it may exchange the two system factors `A ↔ B`, and at d = 4 it may exchange the
  simple ideals of `𝔰𝔬(4) = 𝔰𝔲(2)⊕𝔰𝔲(2)` within or across the factors.
- *The invariant Casimir.* Define `Ω_V = Σᵢ ρ(Xᵢ)ρ(Xⁱ)`, with `{Xᵢ}` any basis of `𝔩` and `{Xⁱ}` its dual under the
  Killing form `κ` of `𝔩` (nondegenerate, since `𝔩` is semisimple for d ≥ 3, d = 4 included). `Ω_V` does not depend
  on the basis.
- Every automorphism `φ` preserves `κ`, so `{φXᵢ}` is a basis with Killing dual `{φXⁱ}`. Hence
  `G Ω_V G⁻¹ = Σ ρ(φXᵢ)ρ(φXⁱ) = Ω_V`, and `G` commutes with `Ω_V`.
- *Identifying `Ω_V`.* `κ` restricted to either factor is the Killing form of `𝔰𝔬(d)`, which is `(d−2)·tr` in the
  vector representation for every d ≥ 3. At d = 4 this single trace-form expression covers both simple ideals with
  equal weight, and the two factors `A`, `B` carry identical normalization.
- So `Ω_V = −(d−2)⁻¹ · ½ · (Cas_A + Cas_B)` with `Cas = Σ_{a<b} J_ab²`: a nonzero multiple of `C_tot`, with the same
  coefficient on both factors. Any unequal normalization would not survive an automorphism exchanging factors.
- `C_tot` has eigenvalue `−(d−1)` on `A⊕B`, containing `u⊗z`, and `−2(d−1)` on `AB`, containing `z⊗z` [U6].
- So `G(u⊗z) = z⊗z` is impossible. ∎

**d = 2** is `DISC-NOGO.md`. There `𝔩` is abelian and `c_Λ = 0`, so `Z` shares the torus weight of `𝔩`. The same
first-order space, dimension 7, is handled by the torus-weight form of Steps 2–6 and by the commuting-eigenvalue form
of Step 3.

**d = 3 is where the proof fails, and it must.** `Σ_A`, `Σ_B` and `Z` share the Casimir pair `(−2, −2)`, since
`Λ²ℝ³ ≅ ℝ³`. So `𝔨` may contain a diagonal subspace of `Σ_A ⊕ Σ_B`, and that is exactly the extra `su(4)` generators
[controls].

## Controls

`ball_nogo.py`: **37 PASS, 0 FAIL**, run in the order d = 5, 4, 2, 3.

| control | expected | result |
| --- | --- | --- |
| d = 5, d = 4: U1–U6 | the uniform steps hold | PASS. First-order dimension 220 and 96, equal to the formula. For d = 4 the self-dual and anti-self-dual `Ω` are also tested. |
| d = 3: the Casimir pairs of `Σ_A`, `Σ_B`, `Z` coincide at `(−2, −2)` | the separation must fail at d = 3 | PASS |
| d = 3: all 15 `su(4)` generators and all 225 brackets satisfy the exact sampled constraints | the bracket method must not flag complex QM | PASS |
| d = 3: the `X⊗X` generator couples both `A↔AB` and `B↔AB` | the loophole is the diagonal | PASS |
| d = 2: family dimension 7, and `𝔩` shares the Casimir pair `(0, 0)` with `Z` | reproduces the disc | PASS |
| d = 2: rotations span only 2 of 4 dimensions | Burnside fails at d = 2, which is why the disc argument differs | PASS |

Sampling note. A first d = 5 run used too few points and gave a nullity bound of 288; that is a sampling failure, not
a result. With 36 and with 50 generic points the bound is 220, the family's rank; d = 4 gives 96 with both 30 and 45
points; d = 3 gives 33 with both 14 and 30 points.

U5 uses the det +1 signed permutation matrices, a finite subgroup of `SO(d)`. Burnside needs only an absolutely
irreducible subgroup, so Step 4 does not use continuity; Steps 0–2 do.

## Scope and literature

- **Continuity of the interaction is not assumed.** `G` may lie in any component of `Aut(C)`.
- **Continuity of the local group is assumed:** the full `SO(d)×SO(d)`. **Finite local symmetry remains open.**
- **Relation to the literature.**
  - Steps 1–5 re-derive in this setting the connected-component statement of Masanes–Müller–Augusiak–Pérez-García
    (2014): for d ≠ 3 the connected reversible group is local.
  - Step 6, the normalizer, excludes interactions in every component of the reversible group.
  - Krumm & Müller, *Quantum computation is the unique reversible circuit model for which bits are balls*, npj
    Quantum Inf. 5, 7 (2019), arXiv:1804.05736. Confirmed from the primary source by the owner (not re-verified here;
    the full text is blocked from this environment):
    - the framework assumes the full global reversible group is a closed connected matrix group, and deliberately
      disregards disconnected components;
    - it notes that CNOT is not assumed available;
    - its Theorem 1 proves that for d ≠ 3 the connected group is the local group.
  - Earlier two-gbit work also takes the global reversible group to be compact and connected.
  - **Novelty status:** not known to be novel globally, but not contained in the Krumm–Müller or Masanes et al.
    connected-group theorems.
- **What it does not identify.** The theorem selects d = 3 among balls with full local rotations. It does not show that
  the d = 3 theory is complex QM, nor does it address non-ball local systems.
