# NOTES-B7 — Conjecture B3.C: the open cases

Node B7 of `research/bridge` (round 2). Base L = `9f9f8257`. Evidence:
- [W] written here;
- [X] `experiments/b7_b3c.py`: 13/13 PASS, VERDICT B7-B3C-EXACT. Run 1 is final; the replay is byte-identical.
  The decision rule was fixed at 22:26:50Z, before the run;
- [A] audited archive record: claim (D) of `research/archive/pt/Z/RESULT.md` §0 and §1.0, which rests on EBF [A].

**Success criterion (set by the round-2 directive before the work began).** Either prove B3.C in its open cases (a
written argument with exact instances), or exhibit a compact pair group containing `cnot` with abelian identity
component that leaves no exotic invariant cone.

## 0. Answer

**B3.C holds in every case, conditional on claim (D) [A].** The open cases fall to one uniform argument (Lemma 2).
One of them is empty (Lemma 3). The degenerate 2-tori get a separate argument (§4). In fact a stronger statement is
proved: **every compact group of unitary and antiunitary conjugations of the pair whose identity component is abelian
misses some pure state with its orbit of pure products.** `cnot` is needed only to apply claim (D).

## 1. Setting and reductions

- **The group.** `H` is a compact group of unitary and antiunitary conjugations of `ℂ²⊗ℂ²` with `cnot ∈ H`.
  Its identity component `T` is abelian.
- **Claim (D) [A].** For compact `Ĝ ⊆ Aut(Q3) ∩ O(ipW)` containing `cnot`: `Ĝ` leaves an exotic invariant self-dual
  cone with H1–H3 iff `R(Ĝ) = Ĝ·P` is not all of `CP³`. Here `P` is the set of pure product states.
- **The torus.** `T` is a connected compact abelian group, so it is a torus in `PU(4)`. It lifts to a torus of
  commuting unitaries: the identity component of its preimage is connected, and its commutator map into the centre is
  continuous on a connected space, hence trivial. So `ℂ⁴` splits into the joint eigenspaces of `T`. `T` is normal in
  `H`, so every `h ∈ H`, unitary or antiunitary, permutes these eigenspaces and preserves their dimensions.
- **(P1), round 1.** If `dim T ≤ 1`, then `H·P` is a finite union of smooth images of `T × P`, of dimension at most
  5. So it misses pure states.
- **The remaining patterns.** For `dim T ≥ 2` the eigenspace dimensions are `(1,1,1,1)` (`dim T ∈ {2, 3}`) or
  `(2,1,1)` (`dim T = 2`). The patterns `(2,2)`, `(3,1)` and `(4)` give `dim T ≤ 1`.
- **Pattern `(1,1,1,1)` reduces to the maximal torus.** Let `{φ_i}` be the eigenbasis and `T₃` the full diagonal
  torus in it. `H` permutes the `φ_i`, so it normalizes `T₃`, and `H' = T₃H` is compact with identity component `T₃`.
  Since `H·P ⊆ H'·P`, a pure state missed by `H'·P` is missed by `H·P`.

## 2. Four distinct eigenlines: one argument for every count of product lines

**Moment map.** Let `μ(ψ) = (|⟨φ_i|ψ⟩|²)_i ∈ Δ³`. Then:
- `μ(tψ) = μ(ψ)` for `t ∈ T₃`;
- `μ(hψ) = σ_h·μ(ψ)` for `h` in the normalizer, where `σ_h` permutes the coordinates (for antiunitary `h` too);
- hence `μ(H'·P) = ⋃_{σ∈Γ} σ·μ(P)`, with `Γ ⊆ S₄` the image of `H'`.

So it suffices to prove the following.

**Lemma 1.** For every orthonormal basis `{φ_i}` of `ℂ²⊗ℂ²` there is `m ∈ Δ³` whose whole `S₄`-orbit avoids `μ(P)`.

The test points are `m(ε, r)`: the value `1 − ε` at one vertex `k`, and `ε·r` on the other three coordinates in an
order `τ`, with `r = (1 − η − η′, η, η′)`. The `S₄`-orbit of one such point consists of all of them, over all `k`
and `τ`.

**Lemma 2 (quantitative certificate).** Let `ψ` be a pure product with `|⟨φ_k|ψ⟩|² = 1 − ε`.

(a) *Non-product vertex.* Write `φ_k = Σ C_ab |ab⟩`, with singular values `s₁ ≥ s₂` of `C`. Then
`max_{p∈P} |⟨φ_k|p⟩|² = s₁² = 1 − s₂²`, and `s₂² ≥ s₁²s₂² = |det C|²`. So no such `ψ` exists if `ε < |det C_k|²`.

(b) *Product vertex.* Let `φ_k = α⊗β` and `w_k = α^⊥⊗β^⊥`.
- Write `ψ = (aα + bα^⊥)⊗(cβ + dβ^⊥)` and `x = |b|²`, `y = |d|²`. Then `x + y − xy = ε`, so `x, y ≤ ε` and
  `|⟨w_k|ψ⟩|² = xy ≤ ε²`.
- `w_k ⊥ φ_k`, so `⟨w_k|ψ⟩ = Σ_{j≠k} \bar ω_j ⟨φ_j|ψ⟩`, with `ω_j = ⟨φ_j|w_k⟩` and `Σ_j |ω_j|² = 1`.
- Suppose `|⟨φ_j|ψ⟩|² = ε r_i` for `j = τ(i)`. The three summands then have moduli `√ε·√q_i`, where
  `q_i = |ω_{τ(i)}|² r_i`. A sum of complex numbers has modulus at least `√q_max − √q_a − √q_b` times `√ε`, so
  `√ε (√q_max − √q_a − √q_b) ≤ ε`.
- So `d_{k,τ}(r) := √q_max − √q_a − √q_b > √ε` excludes `ψ`.

**Choice of `r` (proof of Lemma 1).** For a product vertex `k` and an order `τ`:
- If `ω_{τ(1)} ≠ 0`, then `d → |ω_{τ(1)}| > 0` as `η, η′ → 0`.
- If `ω_{τ(1)} = 0` and both other `ω` are nonzero, then `d = |ω_a √η − ω_b √η′|` in absolute values. This is
  nonzero unless `η′/η = |ω_a|²/|ω_b|²`, which is one of finitely many values.
- If two of the `ω` vanish, the third has modulus 1, and `d = √η` or `√η′`.

Take `η, η′` small with `η′/η` outside that finite set. Then `d_{k,τ} > 0` for all product vertices and orders. With
`ε < min(d², |det C_k|²)`, no point of the orbit lies in `μ(P)`. ∎

**Consequence (Theorem B7.1).** If `T` has four distinct eigenlines, `H·P` misses every pure state with moment
vector `m(ε, r)`. This holds whatever the number of product eigenlines (0, 1, 2 or 4) and whatever the finite part
of `H`, including the case where `cnot` maps a product eigenline to a non-product one.
- It contains (P2′) and (P3) of round 1.
- It does not use the vertex-avoidance argument of (P3), which fails exactly when `Γ` carries a product line onto a
  non-product line. Instance I4 is such a case: `cnot` (as `CZ`) swaps the product line with a non-product line.

**Lemma 3 (exactly three product eigenlines never occur).** Let three orthonormal vectors `a_i⊗b_i` be given in
`ℂ²⊗ℂ²`.
- Each pair is orthogonal on the first or on the second factor.
- In `ℂ²`, two vectors orthogonal to the same vector are parallel. So if two pairs are orthogonal on the first
  factor, say `(1,2)` and `(1,3)`, then `a₂ ∥ a₃ ∥ a₁^⊥`, and the pair `(2,3)` is orthogonal on the second factor,
  `b₃ ∥ b₂^⊥`.
- The orthocomplement is then `a₁⊗b₁^⊥`, a product. The other cases follow by symmetry, since any two of the three
  pairs share an index.

This is the known absence of unextendible product bases in `2⊗n`. ∎ So "exactly 3 product lines" is empty.

## 3. Instances with `cnot` (exact, b7)

The checks work in the `CZ` frame: the local Hadamard on the target maps `CNOT` to `CZ = diag(1,1,1,−1)` (X0).
Products and moduli are invariant under local unitaries.

| id | basis (computational coordinates, unnormalized) | product lines | `CZ` action | certificate (`η, η′, ε`) |
|---|---|---|---|---|
| I1 | `(1,2,2,0), (2,1,−2,0), (2,−2,1,0), (0,0,0,1)` | 1 | fixes every line (`CZ ∈ T₃`) | `1/400, 1/100, 10⁻⁶` |
| I2 | `(1,0,0,0), (0,3,4,0), (0,−4,3,0), (0,0,0,1)` | 2 | fixes every line | same |
| I3 | `(1,2,2,±3), (2,1,−2,0), (2,−2,1,0)` | 0 | swaps the first two | same |
| I4 | `φ₊ = (2+2i, 1+4i)⊗(1, 5/3)`, `φ₋ = CZ φ₊`, two rotated vectors of `V₊ ⊖ f` | 1 | swaps the product line `φ₊` with the non-product `φ₋` | `1/900, 1/200, 10⁻⁸` |
| I5, I6, I7 | grid; `{00, 01, 1+, 1−}`; Bell | 4, 4, 0 | permute | `1/400, 1/100, 10⁻⁶` |

The remaining checks:
- **X2, countercontrol.** At all 12 product vertices, an explicit product near the vertex obeys `|⟨w|p⟩|² ≤ ε²` and
  fails the certificate in all six orders. So the certificate is not vacuous.
- **X6.** On 72 exact points of the tangent plane `L_k = φ_k^⊥ ∩ w_k^⊥`, the triangle (Heron) inequality holds for
  `|ω_j|²m_j`. This confirms the moment image used in the choice of `r`.
- **X3.** In the family of 64 products of `{0, 1, ±, (3,4)/5, (4,−3)/5, (1,±i)/√2}`, every one of the 448
  orthonormal triples has a product orthocomplement (Lemma 3).

## 4. The degenerate 2-tori, eigenspace pattern `(2,1,1)`

Let `T = {a·P_E + b·P_{φ₃} + c·P_{φ₄}}` with `dim E = 2`. Every `h ∈ H` maps `E` to `E` (the only 2-dimensional
eigenspace), maps `F = E^⊥` to `F`, and permutes `{φ₃, φ₄}`. On `P(E)`, `H` acts through a finite group `G_E`.
A projective line lies in the Segre quadric iff it is a ruling, so `E` is either entirely product
(`E = α⊗ℂ²` or `ℂ²⊗β`) or contains at most two product directions.

**(i) `E` not entirely product.**
- Pick a unit `e₀ ∈ E` whose direction avoids the finite set `G_E·(P ∩ P(E))`. Each `V_h⁻¹e₀` is then a
  non-product, with some `δ_h = |det C(V_h⁻¹e₀)|² > 0`.
- Let `ψ_ε = √(1−ε) e₀ + √ε φ₃`. If `ψ_ε = h t p` with `p ∈ P`, then `p` has `E`-component `√(1−ε)` times a phase
  times `V_h⁻¹e₀`, since `t` is a scalar on `E`.
- So `|⟨V_h⁻¹e₀|p⟩|² = 1 − ε`, which is impossible for `ε < min_h δ_h` (Lemma 2(a)).
- **Instance (X4).** `E = span{(1,2,2,0), (2,1,−2,0)}`. `det` restricted to `E` is `−4x² + 2xy + 2y²`, with
  discriminant 36, so `E` has two product directions. `CZ = diag(1,1,1,−1)` lies in `T`. With `e₀ = f₁`,
  `ε = 1/10 < 16/81 = |det C(f₁)|²`.

**(ii) `E` entirely product.** Say `E = |0⟩⊗ℂ²` (local unitary). Then `F = |1⟩⊗ℂ²` and `φ₃ = |1β⟩`,
`φ₄ = |1β^⊥⟩`.
- Write `ψ = |0⟩⊗u + c₃φ₃ + c₄φ₄`. Its T-orbit invariants include `|u|²`, `[u]` and
  `ρ = |c₃|²/(|c₃|²+|c₄|²)`.
- `h` preserves `|u|²`, sends `[u]` to `[V_h u]`, and sends `ρ` to `ρ` or `1 − ρ`.
- On products `(x|0⟩+y|1⟩)⊗v` with `x, y ≠ 0`, `ρ = g([u]) := |⟨β|u⟩|²/|u|²` (X5, symbolic identity).
- So `H·P ∩ {0 < |u|² < 1}` lies in `{ρ ∈ {g([V_h⁻¹u]), 1 − g([V_h⁻¹u])} : h ∈ H/T}`, finitely many values for
  each `[u]`.
- A state with `0 < |u|² < 1` and `ρ` off these values is missed.
- **Instance (X5).** `u₀ = (3,4)/5`, `ρ₀ = 1/2 ∉ {9/25, 16/25}`.

Together with §1 and §2, every compact `H` with abelian identity component misses a pure state. ∎

## 5. Verdict and consequences

- **B3.C: proved [W], CONDITIONAL on claim (D) [A]** (EXOTIC ⟺ `R(Ĝ)` is not all pure states, for compact
  `Ĝ ∋ cnot` of unitary and antiunitary conjugations). (D) rests on EBF [A].
- **Consequence for B3 (round 1).** Theorem B3.2 (towers have abelian identity component, CONDITIONAL on Jordan [L])
  now yields the full statement:
  - no finite or locally finite H-level pair substratum carrying `cnot` forces `Q3`, even granting (b) for every
    realized operation at every stage;
  - CONDITIONAL on Jordan [L] and (D) [A], with no conjecture left.
  - The UNIQUE nodes of stage 4 (an off-frame circle with `cnot`, `{flow, J}`) all have non-abelian identity
    component. Theorem B7.1 says this is necessary: **forcing `Q3` requires a non-abelian connected group of pair
    symmetries**, i.e. (b) for at least two non-commuting one-parameter groups once `cnot`-conjugates are counted.
- **Gem classification.**
  - **NEW**: the uniform moment-orbit certificate (Lemma 2), which closes the mixed product-line cases where round
    1's vertex argument fails.
  - **NEW, small**: the exactly-three case is empty (Lemma 3, a 2⊗2 fact).
  - **POSITIVE**: the B3 no-go is now free of conjecture.
- **Not claimed.** Anything for groups with non-abelian identity component. Those can reach every pure state; stage 4
  records such UNIQUE nodes. Claim (D) and EBF are used at [A] and not re-derived here.
