# Act 34 — pre-freeze measurements and proposition design

Scratchpad note, not a control plane. Everything below is design evidence: numerical probes
(`probe1.py` … `probe5.py` beside this note, all reproducible with numpy alone) and one finite
enumeration. No repository file is touched. Main is `a2f3d820` (A33 certified, #753 landed).

## 1. Objects

- **Single carrier** (acts 24–26, 33): `Γ₀ ≡ ¼`, ancilla `Fin 1`, carrier `Fin 4`; `pt r z` the
  point of relabelled Fourier circle `r ∈ Fin 9` at unit parameter `z`; the normalized set `N₄` is
  the union of the nine circles (`a26_1_circle_count`), with six shared points at `z = ±1`
  (`v₁`, `v₂` tables), incidence `K₃,₃`.
- **Product configuration** (acts 28–30): `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `Γ ≡ 1/16`,
  `e = Equiv.refl`; the product embedding `(G₁ ⊠ G₂) i j k = G₁ i.1 j.1 k.1 · G₂ i.2 j.2 k.2`,
  written inline in `OrbitLawRigidityTwisted.lean` (`product_realizable`, `product_cross`).
- **Two candidate objects for A34**, which the measurements show are different:
  - the **product normalized set** `N₁₆ = {featureVec G : RealizableGram (Fin 1 × Fin 1) Γ G}`;
  - the **product-embedded stratum** `Σ = {featureVec (X ⊠ Y) : X, Y realizable at Γ₀}`, the
    image of act 29's product classes. `Σ ⊆ N₁₆` by `product_realizable`.

## 2. Measurements

| # | statement | probe | result |
|---|---|---|---|
| M1 | `featureVec (X ⊠ Y) = featureVec X ⊗ featureVec Y` after pairing the index factors; hence `⟨fv(X⊠Y), fv(X'⊠Y')⟩ = ⟨fv X, fv X'⟩·⟨fv Y, fv Y'⟩` | probe1 | holds to 1e-15 on random Fourier points |
| M2 | single-carrier inner products between circle points are real | probe2 | max imaginary part 7e-18 over 81 random pairs |
| M3 | for every tested pair `(f, g)` of A33 isometries (identity, global conjugation, single-circle conjugation, a family kernel element, two generators and mixed pairs), `(x, y) ↦ f x ⊗ g y` preserves `Σ`'s distances | probe2 | max squared-distance change ≤ 2e-15 |
| M4 | the nine circles meet pairwise in exactly one point when their `K₃,₃` edges share a vertex and never otherwise: 18 meeting pairs, 18 apart pairs (grid minimum of squared distance 1.5), six shared points, each on three circles, at `z = ±1` | probe3 (a) | matches `a33_shared_census` |
| M5 | the pairing `(x, y) ↦ fv x ⊗ fv y` is injective on `N₄ × N₄`: the scalar ambiguity of a rank-one factorization is fixed by the real positive entry `1/64` at index `(a,a,a),(a,a,a)` | probe3 (b) | holds on samples; the fixing entry is exact |
| M6 | transported incidence: the 81 tori `T(r,s) = circle r × circle s` meet in a **shared circle** `{p} × circle s` or `circle r × {q}` when one index agrees and the other is adjacent (324 unordered pairs), and in a **single point** `(p, q)` when both are adjacent (648 pairs); otherwise they are disjoint. Points on nine tori: the 36 pairs of shared points; shared circles: 108 | probe3 (c), from M4 + M5 | exact combinatorics given M4, M5 |
| M7 | the factor swap `(x, y) ↦ (y, x)` is an isometry of `Σ`, realized on the ambient tuples by the relabelling `(i₁, i₂) ↦ (i₂, i₁)` of `V` (`Prel = Y ⊠ X`) | probe3 (d) | holds |
| M8 | a per-torus conjugation bit is not even well defined: on a shared circle `{p} × circle s`, tori `T(r,s)` and `T(r',s)` with `r ~ r'` would send `(p, w)` to `(p, w̄)` and `(p, w)`, distinct points | probe3 (e) | holds |
| M9 | `N₁₆ ≠ Σ`: the row tuple of `F₁₆/4` is realizable with a paired feature matrix of full tensor rank (singular values all equal); the Diţă twist of `F₄(i) ⊗ F₄(i)` with column twists `(i, −i, i, −i)` (entries in `{±1, ±i}/4`) is realizable, unitary, and its paired feature matrix has rank-one residual `0.866` (Frobenius), the untwisted control has residual `0`; the residual stays ≥ `0.998` under 30 random relabellings of `V` | probe1 (2), probe4 | non-product points exist with fourth-root-of-unity entries |
| M10 | the automorphisms of the coloured incidence structure on the 81 tori (circle-adjacency `R □ R` with `R` the rook's graph `K₃ □ K₃`, plus point-adjacency) inside `Aut(R □ R) = S₃ ≀ S₄` (order 31104) number exactly **10368 = 72² · 2**, all of product-or-swap form; circle-adjacency alone admits factor-mixing automorphisms | probe5 | finite enumeration; the reduction to `S₃ ≀ S₄` uses the Sabidussi–Vizing theorem for Cartesian products, which a kernel decision would not need if it enumerates candidates differently (see §4) |

## 3. Answers to the four pre-freeze questions

1. **Natural analogue of the nine circles.** The 81 tori `T(r, s)`, images of the products of
   circles, which by M1 are isometric to the metric products of the circles with squared distance
   `2 − 2·ip(z,z')·ip(w,w')` (real by M2). They are the natural analogue *on the stratum `Σ`*; they
   are not a decomposition of `N₁₆`, which M9 shows to be strictly larger. The analogue of act 26's
   circle count is therefore a statement about `Σ`, and the freeze must name `Σ` as its object.
2. **Transport of the six shared points and the incidence.** By M4–M6 the incidence structure
   transports as the product: 36 vertex pairs (on nine tori each), 108 shared circles (on three
   tori each), and the torus graph is the Cartesian square of the `K₃,₃` line graph, coloured by
   whether two tori share a circle or a point. M10: this coloured structure has exactly
   `Aut(K₃,₃) ≀ S₂` as its automorphism group; the colouring is what excludes the factor-mixing
   automorphisms of the uncoloured square.
3. **Edge-variable reading of the conjugation bits.** It survives with a sharpening. A33's bits
   were free per circle because conjugation fixes the shared points `z = ±1`. On `Σ` a conjugation
   bit lives on a torus *per factor*, and vertex compatibility becomes **shared-circle
   compatibility** (M8): the second-factor bit of `T(r,s)` must agree with that of `T(r',s)` for
   `r ~ r'`. The line graph of `K₃,₃` is connected, so each factor's bit is a function of that
   factor's circle alone: `9 + 9 = 18` bits, not `81` or `162`. The edge variables remain edge
   variables of the two `K₃,₃` copies; the product does not create new binary freedom.
4. **Embedding or breaking of A33's action.** It embeds (M3, M7): `A33 × A33` acts on `Σ` by
   `f ⊗ g` and the factor swap is an ambient relabelling, giving `A33 ≀ S₂` of order
   `36864² · 2 = 2 717 908 992` acting by surjective isometries of `Σ`. Whether this is the **whole**
   isometry group of `Σ` is the classification A34 would decide; M10 settles the combinatorial layer
   in favour of the wreath product, and nothing measured suggests extra isometries.

Every measurement here is on the consistency axis; none confronts data.

## 4. Candidate propositions for the freeze

All at the frozen product configuration of act 29, on the stratum `Σ`, with the single-carrier
objects of A33 taken as factors. Verification layer named per item.

- **A34-1, factorization of the feature map** (Mathlib, exact). `featureVec (X ⊠ Y)` equals the
  tensor pairing of `featureVec X` and `featureVec Y` under the index equivalence, and inner
  products multiply. This is `product_cross` at the level of the whole feature vector; it is the
  lemma every later item uses.
- **A34-2, the 81 tori and their incidence** (kernel decisions over A33's tables + Mathlib).
  Injectivity of the pairing on `N₄ × N₄` (M5), and the meeting table of the tori (M6) derived from
  `a33_shared_census`. Countercontrol: the two disjoint-torus cases.
- **A34-3, the wreath action** (Mathlib). For surjective isometries `f, g` of `N₄`, `f ⊗ g` and the
  swap are surjective isometries of `Σ` (`IsSurjIsometryOn Σ`); composition law inherited from
  `a33_shared_composition`.
- **A34-4, the classification** (the round's verdict). Every surjective isometry of `Σ` carries
  each torus onto a torus and is `f ⊗ g` or `swap ∘ (f ⊗ g)` with `f, g` A33 isometries; the group
  has order `2 · 36864²`. Decision rule: `A34-WREATH` if proved with the stated order;
  `A34-EXTRA` if an isometry outside the wreath product is exhibited (the freeze names the
  witness format: a map on `Σ` with a torus pair it does not carry to a torus, or a non-product
  action on a shared circle). Route, mirroring A33-1: the affine extension
  (`a26_0_affine_extension` generalized to the 16-carrier ambient, through
  `exists_affineIsometryEquiv_of_isSurjIsometryOn`), then the Vandermonde argument **fibrewise**:
  for fixed `w`, `z ↦ pt r z ⊗ pt s w` is an isometric copy of circle `r` (M1, norms 1), so its
  image lies on one torus by A33's degree-two argument; the torus index is a function of `w` into
  a finite set, constant on an infinite subset, and the argument in `w` finishes. The form step
  then reads the factors from a rank-one factorization (M5) and the shared-circle compatibility
  (M8) forces the product form of the bits.
- **A34-5, the stratum is proper** (kernel-decidable witness, exact). The Diţă-twisted tuple of M9
  is realizable at the product configuration and is not in `Σ`: for a product tuple every `2 × 2`
  minor of the paired feature matrix vanishes (from A34-1), and one explicit minor of the twisted
  tuple's matrix, with entries in `ℚ(i)`, is nonzero (`norm_num`). Control: the untwisted tuple's
  same minor vanishes. This item is what keeps A34 honest about its object: the isometries of
  `N₁₆` are a different, unclassified problem (realizable tuples of `N₁₆` correspond to `16 × 16`
  complex Hadamard matrices modulo column phases, and those are not classified).

Not proposed: anything about `N₁₆`'s isometry group, general carriers, continuous groups,
quarks, colour, gauge or time reversal (per the roadmap's exclusions).

## 5. Framing relative to `P0`

Acts 28–30 concern transition families on the product configuration and whether they factorize on
product classes (`FactorizesOnProduct`). Their product classes are exactly the points of `Σ`. The
measurements give the geometric setting in which their remaining freedom sits:

- a factorizing family preserves `Σ` and acts on it through the factor laws; `Σ` is an invariant
  subset of the configuration space, and M9 shows it is a proper one, so a factorizing family
  never reaches the off-stratum realizable points from a product class;
- the isometries of `Σ` (A34-4, if `A34-WREATH`) are the finite group `A33 ≀ S₂`; any isometry
  covariance one might impose on a factorizing law on the stratum is covariance under this finite
  group and nothing continuous.

A34 as designed classifies the geometry and proves the properness of the stratum; it does not by
itself constrain the selection of a law. The `P0`-facing question it makes precise for a later act
is whether the prescribed pairs of acts 28–30 respect, or are moved by, `A33 ≀ S₂`, and whether the
off-stratum points of `N₁₆` (which no factorizing law reaches) are reachable by a non-factorizing
admissible law. Neither is asserted here.

## 5a. The freeze as the owner reshaped it (five theorems, `A34-STRATIFIED` / `A34-NOT-STRATIFIED`)

The round is frozen around the distinction between the product-embedded stratum `Σ` and the full
product realizable set `N₁₆`, not around "the same nine circles". Mapping of §4 onto that shape:

| owner's theorem | §4 item | object | layer |
|---|---|---|---|
| 1 product geometry: `featureVec (X ⊠ Y)` is the tensor pairing, inner products multiply | A34-1 | any realizable `X, Y` at `Γ₀` | Mathlib, exact |
| 2 stratum structure: 81 circle-pair pieces with the incidence generated by `K₃,₃ × K₃,₃` (M4–M6, M10) | A34-2 | `Σ` | kernel decisions + Mathlib |
| 3 isometry action: `(G₃₃ × G₃₃) ⋊ C₂` acts by surjective isometries of `Σ` (M3, M7) | A34-3 | `Σ` | Mathlib |
| 4 strict containment: a realizable class outside `Σ` (M9, the exact minor) | A34-5 | `N₁₆ ⊋ Σ` | exact `norm_num` witness |
| 5 the `P0`-facing target: factorization + stratum isometry ⇒ each factor map is a `G₃₃` element | new, below | `Σ` and `N₄` | Mathlib + `a33_classified` |

The classification of **all** isometries of `Σ` (§4's A34-4) is not among the five; it is a
candidate for a later act once the off-stratum classes are understood, and the freeze should say
so rather than leave it implicit. `A34-STRATIFIED` is the label when 1–5 prove; `A34-NOT-STRATIFIED`
names which of 2, 3 or 5 failed and how (a torus pair without the stated incidence, a pair
`(f, g)` failing to act isometrically, or a factorized stratum isometry with a factor outside
`G₃₃`); theorem 4's witness is required under both labels, since it is what the labels are about.

**Theorem 5, measured (probe7).** Fixing the second factor reduces the stratum distance to the
single-carrier distance exactly: `d_Σ((x, y), (x', y)) = d_{N₄}(x, x')` (max deviation 3e-14),
because `⟨fv Y, fv Y⟩ = 1` in M1's product formula. Countercontrol: `(z ↦ z² on circle 0) ⊗ id`
changes stratum distances by up to `1.127`, so a non-isometric factor is detected.

**Theorem 5, shape.** With `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl _)
(fun _ => Γ₀) (fun _ => Γ₀) Γ Φ` supplying factor families `Φ₁, Φ₂` with
`GramPhaseEquiv (Φ t (X ⊠ Y)) (Φ₁ t X ⊠ Φ₂ t Y)`, and the geometric hypothesis stated at the
feature level — for each `t` a map `F` of the 16-carrier ambient space with `IsSurjIsometryOn Σ F`
and `F (featureVec (X ⊠ Y)) = featureVec (Φ t (X ⊠ Y))` for all realizable `X, Y` — the conclusion
is: for each `t` there are `f, g` with `IsSurjIsometryOn (normalizedSet Γ₀)` and
`featureVec (Φ₁ t X) = f (featureVec X)`, `featureVec (Φ₂ t Y) = g (featureVec Y)` for all
realizable `X, Y`; hence, by `a33_classified`, each has a unique A33 normal form. The proof is
M1 + `featureVec_gauge` + M5 (injectivity of the pairing) + the fibre reduction:
well-definedness of `f` on `N₄` follows from distance preservation (equal feature vectors have
distance zero), and surjectivity of `f` onto `N₄` follows from `F`'s surjectivity onto `Σ` together
with factorization and M5. Uniqueness of `f` given `Φ` follows from M5 as well, so the theorem
does not depend on which factor families `FactorizesOnProduct`'s existential supplies.

**A design point the owner should settle.** The owner's phrasing is "ordered factorized reversible
law". Act 21's `Reversible` (injectivity and surjectivity on classes at the product carrier) does
not by itself give surjectivity of the factor maps onto `N₄`: its surjectivity conjunct produces a
preimage of `X'' ⊠ Y''` that may be an off-stratum class (theorem 4 says such classes exist), to
which factorization says nothing. Two ways to close this:

- **(i)** state the geometric hypothesis as `IsSurjIsometryOn Σ` (as above), which already contains
  "onto `Σ`"; `Reversible` is then not needed for theorem 5 and is not assumed;
- **(ii)** keep `Reversible` and derive surjectivity of `f` from compactness of `N₄` (an isometric
  self-map of a compact metric space is onto), or from A33's `a33_shared_into` reused with "into":
  a circle carried isometrically into a circle of the same length is onto. This costs more Lean
  and buys a hypothesis closer to acts 28–30's vocabulary.

Recommendation: **(i)** for the freeze, with (ii) named as a corollary route if cheap in-round.
Either way the theorem is stated for `e = Equiv.refl` (ordered decomposition) only.

**Act 35 caveat, recorded.** Theorem 4's witnesses (`F₁₆`, the Diţă twist) show `N₁₆` carries
geometry not controlled by `Σ`. A global product-isometry classification is not a valid next act
until the off-stratum classes are described; the pre-freeze evidence says they correspond to
`16 × 16` complex Hadamard matrices modulo column phases, which are not classified in the
literature, so any such act would have to restrict to a described subfamily (Butson `BH(16, 4)`,
or the Diţă family over the nine circles) and say so.

## 6. What remains before a control plane

- Decide the object: `Σ` (recommended, per §3.1 and A34-5), stated in the preregistration as the
  image of act 29's product classes, with `N₁₆ ≠ Σ` proved in-round as A34-5.
- The exact witness minor for A34-5 is found (`probe6.py`, Gaussian-integer arithmetic with the
  entries scaled by 4): rows `(2,0,2,0,2,2)`, `(2,3,2,1,3,3)` and columns `(1,0,2,0,2,3)`,
  `(0,3,2,3,0,3)` of the paired matrix, in the `(a₁…f₁)`, `(a₂…f₂)` indexing, give the minor
  `−2i · 4⁻¹²` for the twisted tuple and `0` for the untwisted control; 20000 random minors of the
  control all vanish. The freeze can carry these eight indices verbatim.
- Cost estimate for A34-4: A33's module is 354 theorems; the fibrewise Vandermonde route reuses
  `a33_shared_vanish`, `a33_shared_affine_coord` and `a33_shared_into` per factor and adds the
  rank-one reading. Expect a module of comparable size; the finite parts (composition tables over
  `10368` incidence automorphisms, or over the generators) are kernel decisions as in A33.
- Controls as in A33: the identity, the swap, one factor generator per side, and one negative
  witness (a map conjugating one torus only, shown not well defined, M8).
