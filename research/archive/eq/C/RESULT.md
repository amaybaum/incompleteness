# EQ-C — quantum composition (K2-COMP): RESULT

Research only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/`. Every write is under
`scratchpad/eq/C/`. No git write, CI run, Lean build or GitHub action was used. Nothing here is adopted, frozen or
governed. Notation:
- `W 3` is DIM-1's carrier. `min` is the cone of products and `max` is `maxCone (eball 3)`.
- `Q3` is the two-qubit PSD cone in Pauli coordinates. `L` is the local group `{actC R ∘ actT R′ : R, R′ ∈ SO(3)}`
  and `l` is its Lie algebra.
- `R_B = actT reflY` is the one-copy reflection. In the dictionary it is exactly the partial transpose on copy B.
  `R_B Q3` is the twisted composite (a qubit composed with its complex conjugate).
- `T = R_A R_B` is the global transpose.
- `Aut_u(K)` is the group of normalization-preserving linear automorphisms of a cone `K`. "Admissible" means
  `min ⊆ K ⊆ max`.

## 1. Finding

**None of the candidate principles (a)–(e) forces exactly `Q3`.** The reason is structural. The one-copy relabelling
`R_B`:
- preserves products, `maxCone`, normalization, the local group (by conjugation), the corners, both NOT lifts and the
  Euclidean pairing;
- carries `cnot` to a control/native gate `cnot′` with the entangling clause;
- carries `Q3` to `R_B Q3 ≠ Q3`.

So every principle stated in relabelling-invariant vocabulary holds for the twisted composite whenever it holds for
`Q3`. That covers (a), (b), self-duality, homogeneity and purification. `R_B Q3` is even SWAP-invariant, so (e) as a
symmetry statement does not separate the two either.

What the candidates do achieve was settled by an exact classification. The first-order positivity space at the pure
products is exactly 33-dimensional: `l ⊕ M1 ⊕ M2 ⊕ N`. Here `M1` is the two-body part of the `su(4)` image,
`M2 = R_B M1 R_B`, and `N` is a 9-dimensional piece that is symmetric on the correlation block, so compactness removes
it. With exact bracket and module computations, this proves the following: **the Lie algebra of every compact
connected group of reversible maps of an admissible cone that contains `L` is `l`, the `su(4)` image, or its `R_B`
conjugate.**

**Theorem A** (written proof, exact ingredients). With local tomography (LT), admissibility, convexity and an exact
local `SO(3)²`, either of the following forces `K ∈ {Q3, R_B Q3}`:
- (a) any admissible reversible gate that maps a product to a non-product (every CtrlGate with the entangling clause);
- (b) any continuous non-local interaction.

No closedness premise is needed.

As for the other candidates:
- (c) and (d) exclude `min` and `max` but not the twist. Purification excludes `max` only when local reversibility
  is orientation-preserving.
- (e) excludes nothing.

**The twist is excluded only by a principle that ties the copy identification to the dynamics.** The decisive one is
**continuous exchange (CX)**: SWAP lies in the identity component of the composite's reversible group. CX holds in
quantum theory (QM) for every number of copies.

**Theorem B** (written proof, exact ingredients). LT + admissible + convex + exact local `SO(3)²` + CX imply
`K = Q3`. The foils fail CX:
- `min`, `max` and the twist;
- real rebits (determinant −1);
- classical bits.

The local premise is load-bearing: `K_heis` satisfies CX but is not `Q3`.

**At three copies (Theorem C):** idle extension of continuous pair dynamics on two overlapping pairs *derives* the
relabelled class that thread E assumed. The derivation gives:
- the parity rule `ε_AC = ε_AB ⊕ ε_BC` (so uniformly composed identical copies are untwisted);
- that antiunitary pair maps do not extend.

QM satisfies idle extension exactly for its completely positive (CP) reversible maps.

**The smallest open item** is the composite lift of the kernel's own rotation family `driveWords3` (IE₁).

## 2. Evidence level

| claim | level | where |
| --- | --- | --- |
| `cnot` (parsed from CD:741-786) = Ad(CNOT, control A) | exact [M] | P1.1 |
| `R_B` preserves products, max, local SO(3)² (conjugation), corners, NOT lifts; `cnot′ = R_B cnot R_B` has frame, relT, relC; `cnot′(prodState xplus z3) = idW = R_B phiW` | exact | P1.2–1.6 |
| two-sided positivity and the entangling clause transfer from `cnot` to `cnot′` | written, from kernel `nativeGate_cnot` CD:1160 and `entangling_cnot` CD:1380 | P1.6f |
| `R_B Q3 ≠ Q3`; `SWAP R_B SWAP = R_A`; `R_A R_B = T`; hence `R_B Q3` is SWAP-invariant | exact [M] (T preserves PSD: standard) | P1.7–1.8 |
| relabelling no-go: an `R_B`-invariant principle cannot separate `Q3` from `R_B Q3` | written (one line) on the exact transport list | P1, P5.3a |
| `V1 = l ⊕ M1 ⊕ M2 ⊕ N`, dim 33 | exact: rational rank 207 of 240 (saturated from 153 of 289 pairs), symbolic lower bound for all unit x, y | P2.0–2.2 |
| the l-invariant symmetric forms are exactly the block scalars; the block structure of l, M1, M2, N | exact | P2.4a–d |
| a compact group H ⊇ L has no N-component | written (P2.4e) on exact inputs | P2 |
| `End_l(M1) = Hom_l(M1,M2) = ℝ`; mixed bracket outside V1; `[M1, M2]` outside V1; `l + M1 + M2` generates dimension 105 | exact | P2.5 |
| submodule list of `M1 ⊕ M2` (0, graphs, all) | written (isotypic component with End = ℝ) | P2.5b |
| hence `Lie(H) ∈ {l, l ⊕ M1, l ⊕ M2}` | written on exact inputs | P2 verdict |
| `dim Lie Aut(min) = dim Lie Aut(max) = 13`, normalization-preserving parts = l | exact (upper bound) + written (lower bound: local Lorentz maps) | P3.A |
| commutant of l = block scalars; admissible block scalars are local | exact | P3.B1–B4 |
| the admissible normalizer of L is local O(3)² ⋊ {1, SWAP} | written (Aut(SO(3)²) inner or swap) on exact inputs | P3.B5 |
| Theorem A | written proof: P2 + P3 + Yamabe (literature, from memory) + K2C U (prior, written; Schmidt/spectral literature) | §4 T3 |
| QM satisfies CX: exact rational path `τ ↦ Ad(cI − isSWAP)` from id to SWAP, Choi rank 1 | exact [M] | P4.3 |
| `R_B SWAP R_B = T·SWAP` | exact | P4.2b |
| `T·SWAP` has Choi rank 16, so SWAP ∉ `R_B PU(4) R_B` | exact [M]; also kernel `transpose_not_inner` (OrientationSelection.lean:239) | P4.2 |
| rebits: det(SWAP) = −1, commutant of Sym(4,ℝ) = scalars | exact | P4.4 |
| that `O(4)/±1` is the automorphism group of the rebit cone | literature (Kadison-type), from memory | P4.4b |
| classical bits: finite symmetry group | written | P4.5 |
| Theorem B | written proof: Theorem A route + P3 + P4 | §4 T4 |
| `K_heis ≠ Q3`: invariant `|det S| = |c|²` on the exchange orbit; `Ψ0 = [[1,2],[3,5]]` gives 5/4 vs 1/4 | exact (symbolic identities + rational) + written (rank-one extremality) | P5.1 |
| `B3` contains products, SWAP ∈ SO(15) ⊆ Aut_u(B3)₀, B3 ⊄ max | exact | P5.2 |
| (c) `R_B` Euclidean-orthogonal; min ≠ max (witness −2) | exact | P5.3 |
| (c) min not self-dual for any inner product | written + literature (Størmer–Woronowicz) | P5.3c |
| (c) slice reduction: Klein twirl = projection; unit ball self-dual between octahedron and cube | exact + written | P7.2 |
| (c) symmetric cones (self-dual and homogeneous) give `{Q3, R_B Q3}` | written + literature (Koecher–Vinberg, Jordan–von Neumann–Wigner, from memory) | §6 |
| (d) phiW, idW both purify the maximally mixed state; det(corr) = −1 / +1 | exact | P5.4 |
| (d) `F = (3w00 − w11 + w22 − w33)/4` is separable with F(phiW) = 0 | exact | P5.4 |
| (d) max's extreme rays and its two-copy purification under O(3) | written + literature | P5.4 |
| (e) SWAP and local maps preserve min, max | exact | P5.5 |
| `su(4)_AB + su(4)_BC` generate su(8) (63); one pair + local C gives 18 | exact (Pauli-string closure) [M] | P6.1 |
| `(T_AB ⊗ id_C)(|0⟩⟨0| ⊗ Φ⁺_BC)` has eigenvalue −1/2 | exact [M] | P6.2 |
| Theorem C | written on P2, P6 and Theorem A | §4 T6 |
| CX is pair-level: `SWAP_AB ⊗ I_C` has det +1 in O(8) | exact | P7.1 |
| `driveWords3` generators are rotations | exact (cyc3 det +1) + kernel `boundaryTransitive_ball3Drive` (OrbitNormalization.lean:667) | P7.3 |

No result of this thread is kernel-proved. The kernel facts used are cited with file:line in §5.

Literature: none of these sources could be checked. `arxiv.org`, `quantum-journal.org`, `semanticscholar.org` and the
Bristol portal are blocked by egress policy. Everything below is from abstracts in search results or from memory, and
all of it is **unverified**.
- **de la Torre–Masanes–Short–Müller 2012** (PRL 109 090403; title, venue and abstract confirmed by search). For
  local qubits, local structure as in QM, and at least one continuous reversible interaction, the theory is QM.
  - Their exact hypotheses and how the statement treats partial transposition could not be read.
  - Our exact computation shows that `R_B Q3` satisfies the hypotheses as we read them: Bloch-ball marginals, all
    product effects, local SO(3)², LT, products ⊆ K ⊆ max, and the continuous interaction `R_B e^{tX} R_B`.
  - So the conclusion can only hold up to a one-copy relabelling, which is the natural reading when the conjugate
    qubit counts as a qubit.
  - Theorem A is our independent, exact-ingredient version of that statement. In substance it is not new.
- **Masanes–Müller–Augusiak–Pérez-García 2013** (PNAS): ball systems, LT, a continuous interaction and all effects
  give d = 3 and QM. Same remark.
- **Barnum–Wilce 2014**, **Barnum–Graydon–Wilce 2020** (Quantum 4, 359): search snippets only. Locally tomographic
  composites of Euclidean Jordan algebras force complex systems, and dynamical composites are studied. How they treat
  the conjugate composite is unverified.
- **Hardy 2001**, **Chiribella–D'Ariano–Perinotti 2011**: from memory. Their axioms (composite counting, continuity;
  purification and the others) are relabelling-invariant and hold for `R_B Q3`.
- **Al-Safi–Richens 2015** (NJP 17 123001; snippet): reversible dynamics of maximally non-local theories is trivial.
  This is consistent with P3.

**Probe log.** Each run is `python3 -I -B <script> [CompositeDimension.lean]` from `eq/C/`. Each was replayed
into `replay/`, then again with `-B` into `replay2/`, and `cmp` found every output byte-identical. `-I` ignores
`PYTHONDONTWRITEBYTECODE`, so the earlier runs wrote a `__pycache__/` for `eqclib`; it was deleted, and every probe
was re-run with `-B`. Hashes are the first 16 hex digits of sha256.

| probe | script | output | checks | verdict |
| --- | --- | --- | --- | --- |
| lib `eqclib.py` | `e6a6121f1122eda2` | — | — | — |
| P1 relabelling | `33a9e9e7b89b2cf6` | `72ff1635f6c2bbad` | 21/21 | RELABELLING-TRANSPORT-EXACT |
| P2 run 1 (kept) | `7207265673dc77ca` | `6a0bf31ea790aaf9` | 15/16 | **NOT RENDERED**: draft `dim V1 = 24` refuted (upper bound 33) |
| P2 run 2 | `27ba87e70827b931` | `0d0b0867ab8e8c7b` | 20/20 | V1-CLASSIFIED (~46 s) |
| P3 min/max/normalizer | `fa24f5e877344310` | `3915f59dea244940` | 10/10 | MINMAX-AND-NORMALIZER-EXACT |
| P4 continuous exchange | `0f5ee4e6dca00fcf` | `b6e1dd5519adc9aa` | 9/9 | CX-CONVERSE-AND-FOILS-EXACT |
| P5 countercontrols | `fba26e8a742049f8` | `a544ca22dd5f6e3c` | 13/13 | COUNTERCONTROLS-EXACT |
| P6 three copies | `62ea6319c1cb0499` | `9467c3a6d1e4330e` | 5/5 | THREE-COPY-INGREDIENTS-EXACT |
| P7 scope checks | `101ee9b54d9d743b` | `6f76c4e0810f0bc8` | 8/8 | SCOPE-CHECKS-EXACT |
| `x_explore_v1.py` | `c06f4869d0eb306d` | (stdout only) | exploration, not evidence | — |

Run history, recorded rather than hidden:
- **P2 run 1 refuted the draft expectation that V1 is `l ⊕ M1 ⊕ M2`.** Run 2 identified `N` and added the
  compactness step.
- The P3 and P4 scripts were edited after their first passing runs, without changing any outcome:
  - P3: dead code was removed and B.2 was strengthened to all three coefficients;
  - P4: check 4.2b, an "or" of three identities, was replaced by the single exact identity that holds.
- P1's tautological check 1.6f was converted to a note, which brought the count from 22 to 21.
- Timing lines were moved to stderr before the replays.

## 3. Countermodels and controls

| target | countermodel / control | what it shows |
| --- | --- | --- |
| "(a) forces exactly `Q3`" | `R_B Q3` with `cnot′ = R_B cnot R_B` (P1) | CtrlGate data, entangling clause, local SO(3)², admissibility and convexity all hold, yet `K ≠ Q3` |
| "(b) forces exactly `Q3`" | `R_B Q3` with `R_B e^{tX} R_B` (P1, P2: `l ⊕ M2`) | same |
| (c) | `R_B Q3` is self-dual (`R_B` orthogonal, P5.3a) and homogeneous | twist survives |
| (c) | min ≠ max (P5.3b); dim Aut = 13 < 16 (P3) | min and max excluded |
| (d) | twist inherits purification | twist survives |
| (d) | min: pure states have pure marginals | min excluded |
| (d) | max: phiW and idW, det(corr) ±1 (P5.4) | max excluded only under SO(3)-local reversibility |
| (e) | min, max, `Q3`, `R_B Q3` are all SWAP- and local-invariant (P5.5, P1.8) | (e) selects nothing |
| first-order upper bound | **P2 run 1** | 9 extra directions `N`; removed only by the compactness step (P2.4) |
| Theorem A/B: local SO(3)² premise | `K_heis` (P5.1) | admissible, convex, closed, continuous interaction and CX, but `≠ Q3` |
| Theorem A/B: upper bound `K ⊆ max` | `B3` (P5.2) | everything else holds, `B3 ⊄ max` |
| Theorem A/B: convexity | `K_nc = ℝ≥0·(PU(4)·products)` (prior K2C P5.3; spectrum {1/3,1/3,1/3,0} missing) | convexity is load-bearing |
| Theorem A: non-normalizing gate | min, max (P3: identity components local) | without an entangling gate, local invariance selects nothing |
| CX foils | min, max (P3); `R_B Q3` (Choi 16, P4.2); rebits (det −1, P4.4); classical bits (finite group); boxworld (literature) | all fail CX |
| CX converse | QM: exact path, Choi rank 1 (P4.3); n copies: each transposition is Ad of a unitary | holds |
| CX scope | real rebits with an idle rebit: `SWAP ⊗ I` ∈ SO(8) (P7.1) | the path must lie in the pair's own group |
| Theorem C: overlapping-pair interaction | one pair + local C closes at 18 ≠ 63 (P6.1b); thread E's cone(Q_AB ⊗ L_C) (prior, written) | load-bearing |
| idle extension (IE₂) in QM | unitary pair maps extend (written); `T_AB ⊗ id` fails, eigenvalue −1/2 (P6.2a) | IE₂ must be stated for CP maps |
| IE₂ in QM: controls | global transpose `T_ABC` preserves the state; ρ itself has value 0 (P6.2b–c) | the negative sign comes from `T_AB ⊗ id` |
| Lie controls | l, M1, M2 ⊆ V1 symbolically; generic so(15) ∉ V1 (P2.3); `l ⊕ M1 ⊕ M2` generates 105 | controls hold |
| Choi controls | id, SWAP, cnot, a local rotation and a word in them: rank 1; `T`: 16; `R_B`: 4 (P4.1) | controls hold |

## 4. Proposed next theorem(s)

Nothing below is proved in the kernel. "Q3" means K2C's real predicate `{ω | certW ω ⪰ 0}`.

- **T1 — twist transport.** Layer: Lean, kernel-cheap (fin_cases on `W 3`). Direction: forward, as the limit of what
  the forward direction can reach.
  ```lean
  def twist (G : W 3 ≃ₗ[ℝ] W 3) : W 3 ≃ₗ[ℝ] W 3 := actTe reflY ≪≫ₗ G ≪≫ₗ actTe reflY
  theorem ctrlGate_twist : CtrlGate (eball 3) z3 nflip G → CtrlGate (eball 3) z3 nflip (twist G)
  theorem entangling_twist : Entangling (eball 3) G → Entangling (eball 3) (twist G)
  theorem candidateCone_twist : CandidateCone K ↔ CandidateCone (actT reflY '' K)
  theorem swap_actT_reflY : swapW ∘ actT reflY ∘ swapW = actC reflY
  theorem actC_actT_reflY_eq_transpose : actC reflY ∘ actT reflY = transposeW
  ```
- **T2 — the V1 classification.** Layer: exact, as a CI-replayable probe (P2 run 2 frozen). Direction: forward.
  - V1 (first-order positivity at pure products, normalization-preserving) = `l ⊕ M1 ⊕ M2 ⊕ N`, dimension 33.
  - The l-invariant forms are block scalars.
  - The listed bracket obstructions hold.
- **T3 — Theorem A.** Layer: written, later Lean in K3 vocabulary. Direction: forward.
  - Hypotheses on `K ⊆ W 3`:
    - `K` is a convex cone;
    - `prodState x y ∈ K` for `x, y ∈ eball 3`, and `K ⊆ maxCone (eball 3)`;
    - `actC R` and `actT R` preserve `K` for every `R ∈ SO(3)`;
    - a linear `G` maps `K ∩ {ω 0 0 = 1}` onto itself (JointReversible) and does not normalize `L`. Equivalently
      (P3), `G` maps some product to a non-product.
  - Conclusion: `K = Q3 ∨ K = actT reflY '' Q3`. No closedness hypothesis.
  - The same conclusion holds with "a continuous one-parameter group of such maps not inside `L`" in place of `G`.
- **T4 — Theorem B (continuous exchange).** Layer: written. Direction: forward.
  - The hypotheses of T3 without `G`, plus a continuous path `γ : [0,1] → GL(W 3)` with `γ 0 = id`, `γ 1 = swapW`,
    each `γ t` normalization-preserving and `γ t '' K = K`.
  - Conclusion: `K = Q3`.
- **T5 — Q3 satisfies T4.** Layer: exact now, Lean in K3 vocabulary later. Direction: converse.
  - The path is `τ ↦ Ad(((1−τ²)/(1+τ²))·I − i(2τ/(1+τ²))·SWAP)`.
  - It holds for every transposition of n copies.
- **T6 — Theorem C (three copies).** Layer: written, plus exact P6. Direction: forward, with the converse noted.
  - Hypotheses:
    - `K_ABC ⊆ ℝ⁴⊗ℝ⁴⊗ℝ⁴` is a convex cone containing the triple products, nonnegative on triple product effects and
      invariant under local SO(3)³;
    - for the pairs AB and BC, connected groups of normalization-preserving maps not inside the local group act on
      `K_ABC` as `g ⊗ id` (idle extension).
  - Conclusions:
    - (i) after one-copy reflections, `K_ABC = Q_ABC`;
    - (ii) the twist bits satisfy `ε_AC = ε_AB ⊕ ε_BC`;
    - (iii) no map `T_XY ∘ Ad U` extends idly.
  - Corollary: if the three pair composites are equal under the copy identifications, all are `Q3`.
  - Converse: QM with n ≥ 3 copies satisfies the hypotheses, with idle extension stated for unitary maps.
- **T7 — the exchange is not unitary in the twisted composite.** Layer: Lean (matrix side), from
  `transpose_not_inner`. Direction: forward.
  ```lean
  theorem swap_not_twistedUnitary :
      ¬ ∃ U : Matrix (Fin 4) (Fin 4) ℂ, Uᴴ * U = 1 ∧ ∀ X, ptB (swapC * ptB X * swapC) = U * X * Uᴴ
  ```
  The step needed is `ptB ∘ Ad SWAP ∘ ptB = transpose ∘ Ad SWAP` (fin_cases); then OrientationSelection.lean:239
  applies.
- **T8 — the real-rebit foil.** Layer: Lean, `decide`/`norm_num`.
  - The 4×4 exchange permutation has det −1, so `Ad SWAP ∉ Ad SO(4)` on `Sym(4,ℝ)`.
  - Direction: converse, as a foil showing what CX excludes.
- **Candidate definitions** (UNBUILT):
  - `ContinuousExchange K` — the existence of the path in T4.
  - `IdleExtension` — `g ∈ G_XY → g ⊗ id_Z ∈ G_XYZ`, stated for the physical reversible maps.
  - `UniformComposition` — the pair cones agree under the type identifications.

## 5. Dependencies

**Other threads' targets.**
- **K∞-Copy** (type identification of identical copies; ROADMAP.md:1027-1030; `CopyNatural`, KInfFoundations.lean:284).
  CX, uniform composition and the very notion of "the twisted composite" presuppose a fixed, type-level
  identification of the copies. Without one, `R_B Q3` is QM relabelled.
- **The source of IE₁.** This is K∞-Act lifted to a composite, plus a joint tower. No joint tower exists
  (CompositeInterface.lean:54-55).
- **Kₙ**, for more than three copies and other carriers.
- **Not dependent on** the balanced-NOT dimension thread: QC1 takes the two 3-balls as given.

**Corpus declarations at `bcbc516f`.** Paths are relative to `verification/lean-mathlib/OIBridge/`.

| file | declarations (line) |
| --- | --- |
| CompositeDimension | `W` 97, `hom` 100, `homMap` 112, `prodState` 161, `pairVal` 164, `prodEffVal` 182, `maxCone` 186, `jointStates` 190, `actT` 198, `actC` 201, `corner` 205, `IsNot` 210, `NativeGate` 218, `Entangling` 229, `sgn`/`pc`/`pt`/`cnotFun`/`cnot` 741-786, `nflip` 797, `isNot_nflip` 838, `nativeGate_cnot` 1160, `phiW` 1220, `cnot_prodState_xplus_z3` 1222, `entangling_cnot` 1380, `not_entangling_one` 1436, `dim_of_nativeGate` 2723, `three_of_nativeGate` 2748 |
| K2Guard | `reflY` 46, `CandidateCone` 95, `idW` 101, `no_candidateCone_cnot_reflY` 143, `two_le_of_entangling` 240, `three_of_nativeGateOf_of_two_le` 253 |
| RelcSelectBlock | `CtrlGate` 45, `ctrlGate_of_nativeGate` 53, `not_entangling_one_ctrl` 725, `dim_of_ctrlGate` 739, `three_of_ctrlGate` 753 |
| CompositeInterface | `ProductData` 210, `PreComposite` 223 (`convex`, `prod_mem` 225-227), `LocallyTomographic` 235, `Composite` 243, `minBody` 267, `maxBody` 271, `JointReversible` 445, `minBody_subset` 461, `subset_maxBody` 467, `ball3MinComposite` 807, `ball3MaxComposite` 811, `no_composite_over_paddedPre` 895 |
| EffectSpace | `fullAut` 227, `boundaryTransitive_fullAut` 337, `EffectsOn` 567, `maxConeOf_avail_eq` 572, `not_boundaryTransitive_of_countable` 858 |
| OrbitNormalization | `words` 53, `driveWords3` 571, `boundaryTransitive_ball3Drive` 667 |
| KInfFoundations | `ball3` 311, `rot3` 411, `cyc3` 425, `ball3Drive` 449, `CopyNatural` 284 |
| DenseOrbit | `DenseBoundaryOrbit` 53, `denseBoundaryOrbit_ratRefl` 359, `countable_seedOrbit_cone` 403 |
| OrientationSelection | `operational_orientation_noGo` 139, `transpose_not_inner` 239 |
| OrientationClosure | `no_universal_oriented_property` 249 |

ROADMAP.md: the K2 bullet is at 1001-1006 and the finite route at 1081-1093.

**Unsourced premises.** All are named, and none is adopted.
- **LT and product data.** These are the carrier `W 3`, i.e. the COMP-1 fields.
- **Convexity** (`PreComposite.convex`).
- **IE₁** — `actC R` and `actT R` preserve the composite cone for `R ∈ SO(3)`. The single-system rotation family
  `driveWords3` is landed; its composite lift is the premise.
- **An admissible non-normalizing gate or interaction** (Theorem A), **or CX** (Theorem B).
- **At three copies:** idle extension (IE₂) for physical pair maps, an interaction on an overlapping pair, and
  uniform composition.
- **The type-level copy identification** (K∞-Copy).

**Prior off-repo work relied on.** Re-verified here where it is used:
- K2C U (cone uniqueness under PU(4)), used as a written step;
- D-thread D-1 (countable regime);
- thread E's one-pair scope countermodel, used as a written step;
- k2d's `W d` = COMP-1 coordinates.

## 6. Classification

| question | classification | named premise / countermodel / wall |
| --- | --- | --- |
| **QC1 (a)** CtrlGate + Entangling + closure under ⟨gate, local SO(3)²⟩ | **THEOREM ROUTE to `{Q3, R_B Q3}`** (Theorem A), with the gate read as a reversible map of the normalized body (COMP-1 `JointReversible`; `cnot` fixes `ω 0 0`); **COUNTEREXAMPLE to "exactly Q3"** | `R_B Q3` with `cnot′` (exact, P1) |
| **QC1 (b)** continuous reversible interaction | **THEOREM ROUTE to `{Q3, R_B Q3}`** (Theorem A; min and max excluded, P3); **COUNTEREXAMPLE to "exactly Q3"** | `R_B Q3` with `R_B e^{tX} R_B` |
| **QC1 (c)** self-duality / homogeneity | excludes min and max (exact + written); **COUNTEREXAMPLE to "exactly Q3"**; self-dual *and* homogeneous: **THEOREM ROUTE to the pair** (written, literature); either alone: **OPEN** | countermodel `R_B Q3` (self-dual, homogeneous); wall: whether SO(3)²-invariant self-dual (or homogeneous) admissible cones other than the pair exist — the slice test cannot decide, since the unit ball is a self-dual slice (P7.2) |
| **QC1 (d)** purification | excludes min; excludes max **only** with orientation-preserving local reversibility (P5.4); **COUNTEREXAMPLE to "exactly Q3"**; narrowing beyond: **OPEN** | countermodel `R_B Q3`; hidden assumption: SO(3)-only local maps (with O(3), max passes two-copy purification, given Størmer–Woronowicz) |
| **QC1 (e)** SWAP + local SO(3) covariance | **COUNTEREXAMPLE** (selects nothing among the four) | min, max, `Q3`, `R_B Q3` all satisfy it (P5.5, P1.8) |
| **QC1 replacement**: continuous exchange | **INDEPENDENT PREMISE CX**, with which **THEOREM ROUTE to exactly `Q3`** (Theorem B) | independence: `R_B Q3` satisfies (a)–(e) and fails CX (P4.2); `K_heis` satisfies CX and fails local SO(3)² (P5.1); converse: QM for all n (P4.3) |
| **QC2** twisted composite and antiunitary survivors | **THEOREM ROUTE** (Theorem C) from the **INDEPENDENT PREMISE IE₂**: idle extension of pair dynamics, plus an interaction on an overlapping pair; RC3 is derived; the twist also needs uniform composition (or CX at two copies) | independence: QM with the antiunitary `T∘Ad U` added to the two-copy physical group satisfies every two-copy premise and fails IE₂ (P6.2a); one pair only: closure 18 and thread E's `cone(Q_AB ⊗ L_C)`. **Does IE₂ hold in QM with ≥ 3 copies?** Yes, for unitary (CP) maps; no, for the antiunitary symmetries, so it must be stated for physical maps |
| **QC3** closedness and uniqueness | **settled:** with exact local SO(3)² (IE₁), uniqueness needs no closedness (Theorems A/B; closedness follows); in the dense-countable regime, closedness ⇔ the identification (D-1, prior). **smallest open item: INDEPENDENT PREMISE IE₁** | IE₁ = the composite lift of the landed rotation family `driveWords3` (OrbitNormalization.lean:571/667); independence: `K_heis`; reflections cannot be in the lifted family (K2Guard.lean:143); in the countable regime the alternative is a closed body |

**§A.31 classification of this pass.**

| class | findings |
| --- | --- |
| NEW | the exact `V1 = 33` classification, including `N` and its removal by compactness; Theorem A for every non-normalizing admissible gate; CX with its full foil table and the `K_heis` countermodel; Theorem C, which derives RC3 |
| NEW-borderline | the twist exists only relative to a fixed copy identification; purification's exclusion of `max` hinges on orientation-preserving local maps |
| ELABORATING | the relabelling no-go, a composite analogue of `no_universal_oriented_property`; CX's pair-level scope |

Fixed point: **not reached.** The next pass should address self-duality alone, and IE₁ as a joint-tower `OpDatum`
lift. Consistency axis only; bands unchanged.
