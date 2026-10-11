# NOTES-B12 — the finite half's sourcing, and what a stage-crossing substratum would have to supply

Node B12 of `research/bridge` (round 3). Base L = `9f9f8257`. Evidence levels: [K] kernel at L (file:line checked
at L); [D] design module; [W] written here; [X] exact computation (`experiments/b12_stagecross.py`); [A] audited
record; [L] literature named, not checked. Received handoffs used at their labels (LOG, round 3): HO-9 item 3
(passive finite-rank towers carry no infinite-order datum, CONDITIONAL; its stage-crossing clause is the kernel
theorem CompositionOrder.lean:378) and HO-13 item 2 (`R_z(θ₀)` and `J = cyc3` on one token suffice in the schema,
CONDITIONAL).

## 0. Question

The question is whether there is a stage-crossing H-level substratum (not finite) with two properties:
- the native Clifford family on one token (`J = cyc3`, `S`, the NOTs) is H-sourced on it as readout-respecting
  permutations together with `cnot`;
- `R_z(θ₀)` (`cos θ₀ = 3/5`) is a stage-crossing datum on it.

The node also asks to:
- sharpen B3-2's obstruction (`tr(cnot · actC R1) = 10/9`) to the two-operation clause, by computing the exact
  obstruction for `⟨cnot, actT J⟩` and for `⟨cnot, actT R_z(θ₀)⟩` on finite substrata and on directed towers;
- state, exactly and with a label, what a stage-crossing substratum would have to supply.

## S0. Productivity test and predictions (written 2026-10-11T00:45:30Z, before the first run of `b12_stagecross.py`)

**Productivity test (§A.31), fixed before the first run.** B12 is a gem iff it yields an exact obstruction or
construction for the two-operation clause `{R_z(θ₀), J}` strictly stronger than B3-2/B3-5's statements. Examples:
- an obstruction located at a single operation, or at an explicit stage of the natural tower;
- an exact identification of the group the clause generates with `cnot`;
- an exact construction of a stage-crossing substratum.

That fact must also constrain the sourcing of the finite half or expose a hidden assumption. Otherwise B12 is
ELABORATING.

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | `⟨cnot, actT J⟩` acts on `W 3` by signed permutations and is finite; every element has an integer trace (the permutation-character integrality holds); every element fixes the basis table `E(3,0)` (the control's `Z`, `Z ⊗ 1`). Order: a divisor of 384 | U1 |
| S0-2 | `G₁ = ⟨cnot, actT J, actT S, actT nflip⟩` (the native one-token Clifford family on the target, with `cnot`) has order 384. It is exactly the stabilizer of `E(3,0)` in the two-qubit Clifford group `⟨cnot, actC/actT J, actC/actT S⟩` (order 11520): equal as sets, `11520/30 = 384`. It equals HO-13 item 3's group `⟨cnot, actT S, actT J⟩` | U2 |
| S0-3 | `G₁` is realized as readout-respecting permutations of a finite substratum: the `G₁`-orbit `Λ₀` of the 36 octahedral products, with readout `δ_λ ↦ λ` of rank 16. Prediction: `|Λ₀| = 60`, the two-qubit stabilizer states | U3 |
| S0-4 | `actT R_z(θ₀)` is induced by no readout-respecting permutation of a finite substratum: its trace on `W 3` is `64/5 ∉ ℤ`, and `R_z(θ₀)`'s characteristic polynomial has the non-integral factor `x² − (6/5)x + 1`. The B3-2 analogue for a word: `tr(cnot ∘ actT R_z(θ₀)) = 16/5` | U4 |
| S0-5 | On one token, `J · R_z(2π/m)` has trace `−sin(2π/m)`. `2 cos α = −1 − sin(2π/m)` is an algebraic integer exactly for `m ∈ {1, 2, 4}`, checked for `m = 1 … 24` by minimal polynomials. So `⟨J, R_z(2π/m)⟩` is infinite for every `m ∉ {1, 2, 4}`. The closures for `m = 1, 2, 4` have orders 3, 12, 24 | U5 |
| S0-6 | With `cnot`, the two-operation clause on the target generates the Lie algebra `span{1⊗X, 1⊗Y, 1⊗Z, Z⊗X, Z⊗Y, Z⊗Z}` (dimension 6, non-abelian), all commuting with `Z ⊗ 1`. HO-13's `φ₀ = (1, 2, 3i, −1+i)/4` is reached from a product by a block-diagonal unitary `P₀⊗U₀ + P₁⊗U₁` (exact construction) | U6 |
| S0-7 | Word-length filtration instance: `Λ₁ = G₁·(Λ₀ ∪ RΛ₀ ∪ R⁻¹Λ₀)`, `R = actT R_z(θ₀)`, is finite and `G₁`-invariant, with `RΛ₀ ⊄ Λ₀` and `RΛ₁ ⊄ Λ₁`: the datum crosses stages | U7 |
| S0-8 | In B4's realization, (A) fails for `J` on token B: a certified joint effect gives `⟨y, actT cyc3 w0⟩ < 0` (expected `−1/2`, B4 R11's `actC` value); the `Q3` control is nonnegative | U8 |

Decision rule: `VERDICT B12-EXACT` iff U1–U8 all PASS; otherwise `VERDICT B12-FAILED` with the failing ids.

**S0 outcome.** `b12_stagecross.py` run 1 (00:48:32–00:48:36Z): 8/8 PASS, VERDICT B12-EXACT. The replay is
byte-identical (00:48:46Z). There was one pre-run edit, logged in the header (U4's polynomial division). Every
prediction held. S0-1 predicted only "a divisor of 384"; the order is 48. `|Λ₁| = 588`. The guessed U8 value
`−1/2` held.

**Scope discrepancy, found in review of run 1.** S0-5's check column names `m = 1 … 24`. The decision rule, fixed
at 00:46:30Z before run 1, checks `m = 1 … 16`, and only that range was run. The follow-up below checks the rest of
the registered range.

**S0′. Follow-up predictions (written 2026-10-11T00:56:00Z, before the first run of `b12_followup.py`).** A review
of the §3 draft, before this follow-up, found one draft sentence ("the octahedral group is the largest finite stage
holding `J` and a `z`-rotation") contradicted by a standard fact: an icosahedral group contains `T = ⟨J, R_z(π)⟩`.
The follow-up checks that fact and the unchecked part of S0-5's range.

| id | prediction | check |
|---|---|---|
| S0′-1 | For `m = 17 … 24`, `tr(J R_z(2π/m)) = −sin(2π/m)`, and the minimal polynomial of `−1 − sin(2π/m)` is not monic over `ℤ`. Positive control: the minimal polynomial of `2 cos(2π/m)` is monic over `ℤ` for every `m = 1 … 24`. Countercontrol: that of `cos(2π/m)` is monic over `ℤ` exactly for `m ∈ {1, 2, 4}` | V1 |
| S0′-2 | With `u = (φ − 1, φ, 1)/2` (`φ` the golden ratio), the half-turn `R_u = 2uuᵀ − 1` is a rotation with entries in `ℚ(√5)`. `⟨J, R_z(π), R_u⟩` has order 60. It contains `J` and `R_z(π)`, and its only rotations about the `z` axis are `1` and `R_z(π)` | V2 |
| S0′-3 | Independent re-computation in `ℚ(√5)` arithmetic: `|⟨J, R_z(π)⟩| = 12`, `|⟨J, R_z(π/2)⟩| = 24` (agreeing with U5) | V3 |

Decision rule: `VERDICT B12F-EXACT` iff V1–V3 all PASS.

**S0′ outcome.** `b12_followup.py` run 1 (00:57:14–00:57:15Z): 3/3 PASS, VERDICT B12F-EXACT. The replay is
byte-identical (00:57:18Z). Every S0′ prediction held. The draft sentence is false and is replaced in §3 by the
statement the certificate proves.

## 1. The finite half with the gate: finite, finitely realized, and exactly a stabilizer (U1–U3)

- **`⟨cnot, actT J⟩` is finite.** It has order 48 and acts by signed permutations. Its traces are `{0, 2, 4, 8, 16}`,
  all integers. Every element fixes `E(3,0)`, the table of `Z ⊗ 1` [X U1]. The permutation-character integrality
  holds, so nothing obstructs a finite realization.
- **The native one-token Clifford family on the target, with the gate, is the stabilizer of the control's `Z`.**
  `G₁ = ⟨cnot, actT J, actT S, actT nflip⟩` has order 384, lies in `Stab_C(E(3,0))` of the two-qubit Clifford group
  `C` (order 11520), and has the same order. So `G₁ = Stab_C(Z ⊗ 1)` [X U2].
  - It is also HO-13 item 3's group `⟨cnot, actT S, actT J⟩`.
  - The order is explained: the 30 signed non-identity Pauli tables form one `C`-orbit, and `11520/30 = 384`.
  - The reason [W]: `CNOT` and every target-local operation commute with `Z ⊗ 1`.
- **Finite realization.** `G₁` permutes the 60 two-qubit stabilizer states: the `G₁`-orbit of the 36 octahedral
  products, all pure, with readout rank 16 [X U3]. So the finite half is H-sourced, jointly with the gate, as
  readout-respecting permutations of a fixed finite substratum.

## 2. The obstruction sits at a single generator (U4)

**Permutation-character integrality [W].** Let a permutation `π` of a finite `Λ` induce `L` on `W 3` through a
readout `R` onto `W 3` (`R P_π = L R`).
- `ker R` is `P_π`-invariant, and `L` is the induced map on `ℝ^Λ/ker R`.
- `π^N = 1` gives `L^N = 1`. So `tr L` is a sum of roots of unity, an algebraic integer.
- If `L` is rational, `tr L ∈ ℤ`.

**The two generators.**
- `tr(actT R_z(θ₀)) = 64/5` [X U4], so no permutation of a finite substratum induces the drive step on the pair.
  Neither does it on one token: `tr = 16/5` on `HVec 3`.
- `R_z(θ₀)`'s characteristic polynomial is `(x − 1)(x² − (6/5)x + 1)`. The quadratic factor is not in `ℤ[x]`, so
  `R_z(θ₀)` has infinite order.
- The word `cnot ∘ actT R_z(θ₀)` has trace `16/5`.

**Relation to B3-2 and B10-5.** B3-2 needed a word (`tr(cnot · actC R1) = 10/9`), because `R1` has finite order and
is H-sourceable alone. For HO-13's clause the obstruction is the single generator `R_z(θ₀)`. The other generator,
`J`, is unobstructed with the gate (§1). The single-generator fact itself is already in B10-5 (`tr = 64/5`; `R_z(θ₀)`
lies at no finite stage). B12 adds only the comparison and the word trace.

## 3. The natural tower of the continuous half cannot carry `J` (U5)

**The certificate.** `tr(J R_z(2π/m)) = −sin(2π/m)`, so the rotation `J R_z(2π/m)` has `2 cos α = −1 − sin(2π/m)`.
A rotation of finite order has `2 cos α = ζ + ζ̄`, an algebraic integer.

**Norm argument [W].** Write `c = sin(2π/m) = cos(2πr)` with `r` rational.
- The Galois conjugates of `c` are `cos(2πkr)`, all in `[−1, 1]`.
- If `c ≠ 0` is an algebraic integer, `|N(c)| ≥ 1` forces every conjugate to have modulus 1, so `c = ±1`.
- Hence `−1 − sin(2π/m)` is an algebraic integer iff `m ∈ {1, 2, 4}`. Exact for `m = 1 … 24` by minimal polynomials
  [X U5, V1]. Controls: `2 cos(2π/m)` passes the test for every `m ≤ 24`, and `cos(2π/m)` passes exactly for
  `m ∈ {1, 2, 4}` [X V1].

**Consequences.**
- `⟨J, R_z(2π/m)⟩` is infinite for every `m ∉ {1, 2, 4}`. For `m = 1, 2, 4` it is `C₃`, the tetrahedral group (12)
  and the octahedral group (24) [X U5, V3].
- **Every finite rotation group holding `J` contains `z`-rotations of order 1, 2 or 4 only.** A `z`-rotation of order
  `m′` has `R_z(2π/m′)` among its powers, and `J · R_z(2π/m′)` would then have finite order. The bound is on the
  `z`-rotations, not on the group: the icosahedral group `⟨J, R_z(π), R_u⟩`, `u = (φ − 1, φ, 1)/2`, has order 60 and
  holds `J` and `R_z(π)`, its only nontrivial `z`-rotation [X V2].
- The tower that realizes the continuous half (B10-5: `R_z(2π/2ⁿ)` at stage `n`) admits `J` at stages `n ≤ 2`
  only (on the token, the tetrahedral and the octahedral group) and at no stage `n ≥ 3`.
- **General token-local towers** [W + L, the classification of finite subgroups of SO(3), as in B3-5]. Take a directed
  family of finite rotation groups containing `J` from some stage on. Its closure is either finite (orders ≤ 60 once
  a polyhedral group appears) or inside `O(2)` about `J`'s axis `(1, 1, 1)`. A cyclic or dihedral group holding the
  order-3 element `J` has `J`'s axis as its main axis. `R_z(θ₀)` lies in neither.

## 4. What the two-operation clause generates with the gate (U6)

- **Identity component.** The Lie closure of the clause's generators on the target (`1 ⊗ Z` for the flow, `1 ⊗ X`
  for its `J`-conjugate) under `CNOT` and commutators is `span{1⊗X, 1⊗Y, 1⊗Z, Z⊗X, Z⊗Y, Z⊗Z}`: dimension 6,
  non-abelian, all commuting with `Z ⊗ 1` [X U6].
  - So the closed group generated by `cnot`, `actT J` and `actT R_z(θ₀)` fixes `Z ⊗ 1`.
  - Its identity component is the block-diagonal `SU(2) × SU(2) = {P₀⊗U₀ + P₁⊗U₁}` in the control's `Z` basis [W].
    This is the commutant of `Z ⊗ 1` without the control's own phase, which is why the dimension is 6, not 7.
  - The proof [W]. Modulo the global phase, every generator is block-diagonal, and the ratio `det U₀ / det U₁` is a
    homomorphism. It is `−1` on `cnot` (blocks `1`, `X`) and `1` on the target-local generators (equal blocks). So
    the group lies in `{ratio = ±1}`, whose identity component is `SU(2) × SU(2)`. The identity component contains the
    circle `R_z(t)` on the target (`θ₀/π` is irrational) and its conjugates under the group. These generate the
    6-dimensional algebra above, so the inclusion is an equality.
- **Its product orbit is every pure state [W].** Any `ψ = α|0⟩|c⟩ + β|1⟩|d⟩` (a Schmidt-type decomposition along the
  control's `Z` basis, with the relative phase absorbed into `d`) equals `(P₀⊗U₀ + P₁⊗U₁)(a ⊗ |0⟩)`, with
  `a = (|α|, |β|)` and `U₀|0⟩ = c`, `U₁|0⟩ = d`.
  - Exact instance: HO-13's `φ₀ = (1, 2, 3i, −1+i)/4`, with `a = (√5, √11)/4` [X U6].
  - Countercontrol: no element of the finite part `G₁` carries `φ₀` to a product table [X U6]. This is HO-13 item 3's
    unreachability, re-derived.
- **Reading.**
  - This is the structural content of HO-13's reachability lemma (its words `(1⊗W′) CNOT (1⊗W) CNOT` are the
    controlled pairs `(W′W, W′XWX)`). By the stage-4 dichotomy it forces `Q3` [A].
  - The finite half alone stays inside `Stab_C(Z⊗1)`, of order 384, and misses `φ₀`. It therefore leaves exotic cones
    (claim (D) [A], HO-13 item 3).
  - A substratum realizing the clause with the gate must realize a 6-dimensional non-abelian compact group of pair
    symmetries. By B3.2 (Jordan [L]) no directed tower of finite pair substrata does. This is B3-3's "not two
    non-commuting local circles" applied to the clause.

## 5. A stage-crossing substratum: it exists, and supplies nothing (U7, U8)

**Construction [W + X U7].** Take the word-length filtration.
- `Λ₀` is the 60 stabilizer states.
- `Λ_{n+1} = G₁·(Λ_n ∪ RΛ_n ∪ R⁻¹Λ_n)`, with `R = actT R_z(θ₀)`.

Each stage is finite: `|Λ₁| = 588`. `G₁` (the gate and the native Clifford family on the target) acts by stage-preserving
readout-respecting permutations, and `R` crosses stages (`RΛ₀ ⊄ Λ₀`, `RΛ₁ ⊄ Λ₁`). Starting from a dense countable set of
points of any closed cone invariant under the closure, the same filtration realizes that cone (for `Q3`, the pure
states), with every operation available in context.

**Answer to the node's question.** Yes: such a substratum exists, at the level of hidden configurations, for every
cone the closure preserves. Its existence decides nothing.
- With availability in context (A) for `J` and `R_z(θ₀)`, B1.1 [D], H1 and H3, the cone is `Q3` (HO-13 item 2,
  CONDITIONAL).
- Without (A), the same filtration over B4's register tables hosts K(Z_F). There (A) fails exactly: `−1/2` for `J`
  [X U8] and `−2/5` for `R_z(θ₀)` (B10 T4). The `Q3` control gives `1/2`.

**B12-S, what a stage-crossing pair substratum must supply** (CONDITIONAL on the named items at their labels).
- **(S1) Token: an infinite-order datum.**
  - `R_z(θ₀)` (infinite order, U4) is stage-crossing on the token's completed body (CompositionOrder.lean:378 [K];
    `tr ∉ ℤ` [X]).
  - It is not available on a passive, repeatable, finite-rank tower (HO-9 item 3, CONDITIONAL). The known candidate
    is the invasive re-preparing tower (HO-9 item 4, CONDITIONAL on a law outside the stated access), i.e. Origin's
    single open premise (HO-9 item 5).
- **(S2) Token: `J`, stage-preserving.** It is H-sourceable on a finite register (the octahedral permutations, B1 H1a)
  and jointly with the gate on the 60 stabilizer states (§1).
- **(S3) The two cannot share stages.** `R_z(θ₀)` must cross stages relative to every stage structure carrying `J`
  and `cnot`. Its natural finite approximants are incompatible with `J` (§3). Every token-local tower holding `J` misses
  it (§3, [L]). Every pair tower misses the 6-dimensional closure (§4, B3.2 [L]).
- **(S4) Pair: availability in context.** (A), with (W) and (P), for `J` and for `R_z(θ₀)` on one token in the pair
  context: H-T ∧ (A)_J = H-OI_g at `{R_z(θ₀), J}` (B10). The composite must be in branch (a): product-register
  composites are Bell-local (B1.2; HO-9 item 6) and host no candidate cone. Nothing in the stage structure supplies
  (A).

## 6. Verdict of B12

- **Answers.**
  - The finite half (`J`, `S`, NOTs, with the gate) is H-sourced on a finite substratum as `Stab_C(Z⊗1)` (order 384,
    the 60 stabilizer states).
  - `R_z(θ₀)` is H-sourced on no finite substratum (the single-generator obstruction `64/5`, already in B10-5) and on
    no tower that also carries `J` (§3, with [L] for general token towers; §4, with Jordan [L] for pair towers).
  - A stage-crossing substratum with both exists for free, and supplies nothing. What it must supply is (A) for the
    two operations (S4), plus Origin's premise for the token's infinite-order datum (S1).
- **Gem classification (productivity test met).**
  - **NEW.**
    - (i) The native one-token Clifford family with the gate is exactly the stabilizer of the control's `Z`
      (384 = 11520/30). Adjoining `R_z(θ₀)` yields the block-diagonal `SU(2) × SU(2)` commuting with `Z ⊗ 1`, whose
      product orbit is every pure state. This is the structural reason the clause forces `Q3` and its finite part does
      not.
    - (ii) Every finite rotation group holding `J` contains `z`-rotations of order 1, 2 or 4 only
      (algebraic-integer certificate). So B10-5's tower and `J` share no stage beyond `n = 2`: the two halves of the
      clause cannot be realized on common finite stages of the natural tower.
  - **ELABORATING.**
    - The single-generator location of the finite-substratum obstruction (B10-5 has it; B12 adds the comparison with
      B3-2).
    - The stage-crossing filtration exists trivially (the configuration-level structure is free).
    - The pair-tower exclusion is B3-3 applied to the clause.
  - **Corrected in review, before this note was committed.** A draft sentence of §3 bounded the group ("the
    octahedral group is the largest finite stage holding `J` and a `z`-rotation"). It is false: an icosahedral group
    holds `J` and `R_z(π)` [X V2]. The certificate bounds the `z`-rotations, which is what (ii) states.
- **Not claimed.**
  - A source for (A), for the re-preparing law, or for `R_z(θ₀)` on the token.
  - The norm argument is written, not kernel-checked; exact checks cover `m ≤ 24`.
  - The general-tower clause rests on the classification of finite subgroups of SO(3) [L] and on Jordan [L].
