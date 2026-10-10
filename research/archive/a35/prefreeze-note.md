# Act 35 — pre-freeze measurement: the off-locus classes of the product normalized set

Scratchpad note, not a control plane. Measurement only, from immutable
D35 = `100bb1e86931fa769a200e9b117f4f9fb0a745b9` (A34 landed and certified). No execution branch,
PR, F or frozen proposition. Probes `probe1.py` … `probe6b.py` beside this note (numpy + sympy;
exact ranks over ℚ by `DomainMatrix`, Gaussian-rational arithmetic by `fractions`). Every result is
on the consistency axis.

## 1. Objects, in the landed terms

- A realizable tuple at a one-element ancilla is `G i j k = conj(U i j) · U i k` for a unitary `U`
  with `|U i j|² = Γ`; at the single carrier `U/2` is a 4×4 complex Hadamard matrix, at the product
  configuration `U/4` a 16×16 one. Phase equivalence (`GramPhaseEquiv`) is right-multiplication by
  phases; row phases cancel in `G`. So `N₄` and `N₁₆` are the 4×4 and 16×16 complex Hadamard
  matrices modulo two-sided phases, embedded by `mixedTriple`.
- The feature inner product of two tuples is `tr(A³)` with `A_jk = Σ_i W_ij conj(W_ik)`,
  `W = U ∘ conj(U')` (M1). All later distances are computed from this exact formula.
- `Isom(N₁₆)` contains every relabelling `(π, τ) ∈ S₁₆ × S₁₆` (`relabel2_isometry`, for any
  `Equiv.Perm V`), the conjugation and the transpose. `Σ` (A34) is the stratum of the products with
  the frozen pairing `(a,b) ↦ 4a+b`.
- **"Off-locus" has to be read modulo `Isom(N₁₆)`**: a non-product relabelling of a `Σ` point leaves
  `Σ` (residual 0.5 in every one of 20 trials, M2) while staying in its isometry class. The locus of
  the classification is `Isom(N₁₆)·Σ`, the classes of matrices phase-equivalent to a Kronecker
  product under *some* pairing; the strata `T(r,s)` are not class invariants.

## 2. Measurements

| # | statement | probe | result |
|---|---|---|---|
| M1 | `⟨fv G, fv G'⟩ = tr(A³)` as above, exactly the landed definition | probe1 (a) | agrees to 1e-12; unit norm 1 |
| M2 | the strata are not class invariants: non-product relabellings of a `Σ` point leave `Σ` inside its class | probe4 (a) | residual 0.500 in 20/20; product-compatible swap: 0 |
| M3 | on every circle the inner product is `c(t) = 5/8 + (3/8) cos t` (first harmonic only): the nine circles are planar round circles of radius √(3/8); the torus `T(r,s)` has `d² = 2 − 2c(Δθ)c(Δφ)` | probe1 (c) | coefficients 0.625, 0.1875, 0.1875, rest 0 |
| M4 | the six shared points `z = ±1` are the **real** 4×4 Hadamard classes; the Fourier matrix sits at `z = ±i` | probe1 (b) | all 18 vertex tuples real; 6 classes |
| M5 | `Σ`-membership (fixed pairing) is the vanishing of the cross ratios `H[(a,b),(c,d)]H[(a,b'),(c',d)] / (H[(a,b),(c',d)]H[(a,b'),(c,d)])` − 1; on the A34 witness they take all four values ±1, ±i | probe1 (d) | product: {1}; witness: {1, −1, i, −i} |
| M6 | **exact defect** (dimension of the linearized flat-unitary variety modulo the 31 phases; integer rank over ℚ) at the fourth-root points of `Σ`: H4⊗H4 (vertex×vertex) **105**, H4⊗F4 **73**, F4⊗F4 **57**; same values on other circle pairs | probe2 | exact |
| M7 | exact defect at a **non-torsion** `Σ` point, `z = (3+4i)/5, w = (5+12i)/13`: **49**; numerically 49 at random points (singular-value gap 2e-2 / 2e-16) | probe2c, probe2 | exact / numeric |
| M8 | the column-twist family `Δ_col`: `H[(a,b),(c,d)] = X[a,c]·D[c,b]·Y_c[b,d]` (X, Y_c realizable, D any 4×4 phases) is realizable (unitary and flat) for all parameters; its tangent rank modulo phases is **14** = 1 (X) + 4 (Y_c) + 9 (D modulo gauge). The row-twist family `Δ_row` (transpose construction) likewise, 14. Both contain `Σ` (`D ≡ 1`, all `Y_c` equal). Their tangent spaces at a generic `Σ` point span **26** (= 14 + 14 − 2), i.e. they meet only along `Σ`'s tangent | probe2, probe5 | numeric ranks, exact families (block identity) |
| M9 | exact defect at Diţă points: with nine distinct rational twist phases **17**; with four distinct `Y_c` as well **17**; the A34 witness (fourth-root twist of F4⊗F4) **49**; numerically 17 at random Diţă points | probe2c, probe2 | exact / numeric |
| M10 | the cyclic Fourier matrix `F₁₆` is the column twist of `F₄⊗F₄` with `D[c,b] = ω^{bc}` (Cooley–Tukey), up to a column relabelling: equal Haagerup sets and profiles; its defect **17** reproduces the literature value `d(F₁₆) = 17` | probe4 (c) | control of the defect code against a known value |
| M11 | at a generic `Σ` point the defect space (49) exceeds the span of both Diţă tangents (26) by **23 directions**; second-order obstruction of those directions: random unit direction 0.010 ± 0.002 against a source term of norm 0.32; minimum over the sphere 0.002–0.003; mixed with Diţă directions 3e-4–5e-4 (pure Diţă directions: 0 to 1e-19; column+row mixture, not a family: 5e-3) | probe5c | numeric; inconclusive at this resolution |
| M12 | Newton-projected realizable points near a `Σ` point off `Σ` and off both fixed-pairing hulls exist (feature distance 0.03–0.2, residuals up to 0.39), defects 15–19; **none** is certified outside every Diţă hull for every pairing by the relabelling-invariant signature (4-subsets of columns on which the rows fall into four proportionality classes of four; `Σ` point 20, column-Diţă point 4, witness 12, F4⊗F4 28, H4⊗H4 140) | probe6b | 9 converged points, 0 certified |
| M13 | **finite off-locus census at fourth roots**: 400 random fourth-root Diţă twists (X, Y_c on the nine circles at z ∈ {±1, ±i}, D ∈ μ₄) give **369 distinct** (profile, Haagerup set, exact defect) classes; **363** are certified off the *entire* Kronecker locus by the exact defect alone (the Kronecker fourth-root classes have defects 57, 73, 105 only), all 369 by the triple; exact defects observed: 23, 25, …, 77 (27 values) | probe4b | exact invariants |
| M14 | real classes: the 512 gauge-inequivalent ±1 twists of H4⊗H4 (and 300 mixed-vertex samples) realize exactly **two** profiles, Sylvester's and one other; the other is a real class off the whole Kronecker locus (its Haagerup set is {±1}, and a Kronecker class with that Haagerup set is H4⊗H4); its defect is also 105, so the defect does not separate the two real classes but the profile does | probe4 (b), probe4b | exact |
| M15 | the **matrix-induced subgroup** of A33 (relabellings, conjugation, transpose; BFS closure on the 60-class eighth-root grid, faithful): order **2304**, surjecting onto Aut(K₃,₃) (72) with a kernel of **32** of the 512 conjugation-bit patterns; index **16** in A33. Relabellings alone: image 36, kernel 16; relabellings + conjugation: image 36, kernel 32. A single-circle bit is not matrix-induced; global conjugation is | probe3d, probe6 (a) | exact enumeration |
| M16 | orbits/stabilizers under `G_ext = ⟨product relabellings, swap, conj, transpose⟩` (order 2 654 208) acting on `N₁₆`: generic `Σ` point stabilizer 64 (orbit 41 472); F4⊗F4 512; H4⊗H4 4608 (orbit 576); A34 witness 16 (orbit 165 888); generic Diţă point 2 (identity and the second-factor column relabelling (0 2)(1 3), which fixes the Fourier circle pointwise up to phase). A33 ≀ S₂ is transitive on the 81 tori (stabilizer 2·36864²/81 = 33 554 432), on the 36 vertex pairs and the 108 shared circles | probe3 | exact enumeration |

The A34 grid representation of A33 is faithful (36 864 distinct permutations, closure 36 864 by
BFS); sympy's Schreier–Sims order on the same generators returned 18 432 and is not used.

## 3. Answers to the six measurement points

1. **Complete off-locus class structure of `Σ`.** Read as the classes of `N₁₆` off `Isom(N₁₆)·Σ`,
   the structure is not finite and not two-dimensional: through every point of `Σ` pass two
   14-dimensional realizable families (`Δ_col`, `Δ_row`, M8), and the linearized dimension of `N₁₆`
   along `Σ` is 49 at generic points, 57 / 73 / 105 at the special points (M6, M7), against 2 for
   `Σ` and 26 for the two hulls together. The finite part at fourth roots already holds hundreds of
   distinct classes (M13). Modulo the isometries, the classes off the locus are at least a
   12-parameter continuum (14 − 2) near every stratum, and the classification of 16×16 complex
   Hadamard matrices, which this is, is open in the literature.
2. **How the wreath action acts.** Only the matrix-induced part of A33 ≀ S₂ extends to `N₁₆`: the
   subgroup of order 2304 per factor (index 16 in A33, M15) together with the swap, giving `G_ext`
   of order 2 654 208; the per-circle conjugation bits that make A33 large do not extend. `G_ext`
   acts on the off-locus classes with generically trivial stabilizer (order 2 on a generic Diţă
   point, 16 on the witness, M16), so it identifies at most 2.6 million points of a 14-dimensional
   family and reduces no modulus. On the strata the wreath group is transitive on tori, vertex
   pairs and shared circles (M16).
3. **The Diţă witness.** It is the fourth-root point `D[1,:] = (1, i, 1, −i)` of `Δ_col` at
   `F₄⊗F₄`. It lies outside `Σ` because its same-row-block, same-column-in-block cross ratios take
   the values ±1, ±i where a product has only 1 (M5); this is the exact obstruction, and it is the
   linear term of the twist `D[c,b]` which depends jointly on the column block and the row within
   the block, a dependence no product of phases `p_{ab} q_{cd}` can absorb. It is a special point
   of the hull: defect 49 (M9), the generic value on `Σ`, not the generic Diţă value 17; its
   `G_ext`-stabilizer has order 16. It is not equivalent to any Kronecker product under any
   relabelling (exact invariant triple, M13).
4. **Class invariants versus stratum invariants.** Stratum invariants (fixed pairing): the torus
   labels `(r, s)` read from the vertex coordinates of A33, and `Σ`-membership by the factorizing
   cross ratios (M5). These are changed by non-product relabellings (M2) and classify nothing
   in `N₁₆` modulo its isometries. Class invariants (invariant under all relabellings, phases,
   conjugation, transpose): the exact defect, the Haagerup set, the profile multiset, and the Diţă
   signature (M12). The defect separates the locus's fourth-root points (57, 73, 105) from 363 of
   the 369 sampled off-locus classes (M13) but not the two real classes (M14); the profile separates
   those. No finite list of invariants measured here is complete for `N₁₆`.
5. **Further families and continuous moduli.** Yes: at least the 14-dimensional `Δ_col` and
   `Δ_row` through every `Σ` point, and 23 further first-order directions whose integrability the
   second-order test leaves open (M11: obstruction small but not zero at the resolution reached).
   Newton-projected points off both fixed-pairing hulls exist but none was certified off every hull
   for every pairing (M12). The unresolved modulus is the local structure of `N₁₆` along `Σ` beyond
   the Diţă hulls — equivalently whether the 49-dimensional defect space at a generic `Σ` point is
   the tangent cone of a union of Diţă hulls under relabellings or of something larger.
6. **Strongest supported global proposition and the smallest countercontrol.** The evidence
   supports a *stratification* statement, not a classification: `Σ ⊊ Δ_col ∩ Δ_row`-type
   containments with `Δ_col, Δ_row ⊂ N₁₆` realizable 14-dimensional families (exact algebra), the
   exact defect values 105 / 73 / 57 / 49 on `Σ` and 17 on generic Diţă points (exact rank), and
   the finite off-locus census with exact invariants. A proposition of the form "the Diţă hulls
   under relabellings exhaust `N₁₆` near `Σ`" is the natural global candidate; its smallest
   countercontrol is *defect at a generic `Σ` point = tangent rank of the hulls*, and that control
   **fails** (49 ≠ 26). So an unseen direction exists at the linear level, and the exhaustion
   proposition cannot be frozen as a theorem target.

## 4. Decision

The off-locus classes are **not exhausted**. Act 35 must not be frozen as the global
product-isometry classification round. The unresolved modulus is stated in 3.5 and 3.6.

Recommended scope for the next round (drafted only on direction): *the Diţă-hull stratum and the
defect stratification of `Σ`* — all exact, all kernel- or algebra-decidable:

- **A35-1** (Mathlib, exact): `Δ_col(X, Y₀..Y₃, D)` is realizable at the product configuration for
  all realizable factors and all phases (the block identity), and so is its transpose family.
- **A35-2** (exact): `Σ ⊆ Δ_col ∩ Δ_row` with the frozen pairing, and the A34 witness is a point of
  `Δ_col` at `F₄⊗F₄`; the two hulls meet only along `Σ` at the tangent level (rank 26 = 14 + 14 − 2).
- **A35-3** (exact rank, kernel- or certificate-decidable): the defect values 105, 73, 57 at the
  fourth-root points of `Σ`, 49 at the Gaussian-rational point `((3+4i)/5, (5+12i)/13)`, 17 at a
  Gaussian-rational Diţă point, 49 at the witness. A defect is an integer matrix rank; a Lean
  certificate is a basis of the null space plus independent rows.
- **A35-4** (exact invariants): a finite census of off-locus fourth-root classes with defect
  certificates against the three Kronecker fourth-root classes, and the second real class.
- **The named open modulus**, carried as a question and not as a target: whether `N₁₆` near `Σ`
  is the union of the Diţă hulls under relabellings. Countercontrol format: a realizable point near
  `Σ` with Diţă signature 0 for `H` and `Hᵀ`.

Labels would be of the form `A35-DITA-STRATIFIED` (1–4 prove) / `A35-NOT-STRATIFIED` (which
fails and how); neither label would assert exhaustion.

## 5. Literature cross-checks (from memory; to be verified before any citation is frozen)

- 4×4: every complex Hadamard is equivalent to the one-parameter Fourier family (Haagerup 1996),
  the classification behind A26's nine circles.
- Defect: Tadej–Życzkowski 2006/2008; `d(F₁₆) = 17` reproduced here (M10).
- Diţă 2004: the twisted tensor construction; F₁₆ as a twist of F₄⊗F₄ is the Cooley–Tukey
  factorization.
- Real order 16: five equivalence classes (Hall 1961); the profile distinguishes them
  (Cooper–Milas–Wallis 1978). The ±1 Diţă twists reach two of the five (M14).
- 16×16 complex Hadamard matrices: no classification is known; even the quaternary (Butson)
  case at order 16 is not settled to my knowledge.
