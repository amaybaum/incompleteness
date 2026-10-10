# Thread D — alternative geometry sources: RESULT

Base: read-only worktree `scratchpad/wt-threads` at `4507b025`. Nothing outside `threads/D/` was written.
The productivity test was fixed before any branch was walked (`PRODUCTIVITY-TEST.md`). All scripts in this
directory use exact arithmetic (Fractions, an exact Q(√5) class, and sympy for one symbolic determinant).
No floating point is used for any claim.

## 1. Finding

None of the three routes derives (SF) from premises weaker than the ones it carries. Each route
either assumes full effects (routes 1 and 3) or needs a composition rule (route 2). Fork B
(no-restriction) is therefore an input to every route examined. No route excludes the classical
segment or fixes the ball's dimension, so K∞-R and the NB-1/copy-naturality layer stay necessary.

**Route 1 (homogeneity + self-duality).** For a bit, self-duality is redundant once full effects are
granted: homogeneity of the state cone, plus full effects, plus capacity 2 forces the state space to
be a ball `Bⁿ` of some dimension `n ≥ 1`.
- So the route delivers exactly NB-1's input hypothesis: a `d`-ball with the full self-dual effect
  cone (`NativeGateBall.lean:5-6`).
- It does this without Lemma B, Lemma C, (A1) or (SF). It still admits the classical segment
  (`ℝ₊²`) and every `n`.
- Homogeneity is the load-bearing half. The regular pentagon gbit is strongly self-dual, has
  capacity 2 and is pure-transitive, yet it violates (SF).
- Each half alone excludes the square, the torus and the Stiefel body. So the corpus control set
  cannot tell the two halves apart.

**Route 2 (purification).** The route cannot be sourced from the corpus.
- The corpus's "existence half" (`Main.md:598-600`) is a reversible dilation whose hidden *prior* is
  a mixed state. Every classical theory has such a dilation. CDP existence asks for a *pure* joint
  state, and in a classical composite every pure joint state is a point mass, which yields a
  deterministic law. So neither half of CDP purification is supplied.
- Fiber freedom lives entirely in redundant (non-tail-injective) fibers. A weaker uniqueness
  survives, checked exactly on the corpus grid: tail-injective completions of the same law are
  isomorphic by a unique visible-preserving, intertwining isomorphism. Only a minority of those
  isomorphisms are one purifier-only permutation, which is the form CDP's uniqueness takes.
- On a single system, route 2 reduces to pure-state transitivity. All three countermodels already
  satisfy it.

**Route 3 (tests on frames + frame transitivity).**
- As literally stated, "repeatable nondemolition tests" is vacuous: measure-and-prepare satisfies
  it in every theory with full effects.
- Two stronger versions each exclude all three bodies exactly: ideal (Lüders-type) tests, and
  transitivity on ordered frames.
- The ideal-test and frame-transitivity premises together do not imply (SF). The pentagon satisfies
  both.
- Frame transitivity alone does force a ball for every *centrally symmetric* body. The square, the
  torus and the Stiefel body are all centrally symmetric, and that is why they fall.
- The literature closure for this route is Barnum–Hilgert (spectrality + strong symmetry). Both of
  its halves are load-bearing. The torus is spectral but not strongly symmetric. The pentagon is
  strongly symmetric but not spectral.

Productivity-test verdicts (§A.31 classes):

| branch | verdict |
| --- | --- |
| route 1, self-duality redundant for bits | gem, NEW |
| route 2, typing of the corpus "existence half" | gem, NEW |
| central-symmetry marker on the control set | gem, NEW |
| route 3, centrally-symmetric lemma | gem, ELABORATING |
| route 2, weaker uniqueness | CONFIRMING (a corollary of `Main.md:598`) |
| route 3, literal form vacuous | BORDERLINE |

## 2. Evidence level

Evidence levels are: **E** = exact computation (script and output in this directory), **W** =
written proof (below or inline), **L** = literature.

The literature PDFs could not be fetched: the egress proxy blocks arXiv and the publisher pages.
Citations are therefore by title, venue and arXiv id, as confirmed by search. No theorem numbers
are asserted.

**Route 1**

| # | claim | evidence |
| --- | --- | --- |
| 1a | Koecher–Vinberg: homogeneous + self-dual cone ⇔ cone of squares of a Euclidean Jordan algebra (EJA), with the Jordan–von Neumann–Wigner classification. | L: Koecher, *Amer. J. Math.* 79 (1957) 575; Vinberg, *Soviet Math. Dokl.* 1 (1960) 787; Faraut–Korányi, *Analysis on Symmetric Cones* (OUP 1994), Ch. III and V |
| 1b | In an EJA with full (= self-dual) effects, capacity = rank. Proof: a Jordan frame gives `≥`; for `≤`, `⟨eᵢ,ωᵢ⟩ ≤ tr(eᵢ)·λ_max(ωᵢ) ≤ tr(eᵢ)`, because `λ_max(y)e − y ≥ 0`, and summing gives `k ≤ tr(e) = r`. So capacity 2 ⇒ spin factor `Vₙ` ⇒ ball `Bⁿ`, `n ≥ 1`; `n = 1` is the segment `ℝ⊕ℝ`. | W |
| 1c | Homogeneity alone excludes the bodies; `dim Lie Aut(K)` is bounded above by exact tangency equations at rational points of the extreme-ray manifold. The torus, Stiefel and Lorentz bounds equal the known algebras (scaling + so(2)²; scaling + so(3) + so(2); gl₁ + so(3,1)). The Carathéodory bound (4) is consistent with a `gl(2,ℝ)` action on the degree-2 trigonometric moment cone, but its tightness is not claimed; only the bound is used. | E: `d1_route1_homogeneity.py` (A), outputs table below |
| 1d | Self-duality alone excludes the square: no symmetric positive-definite `G` maps the square cone onto its dual, over all 24 ray bijections (0/24). | E: `d1` (B) |
| 1e | Self-duality alone excludes the torus. `D×D` has extreme-ray set ≅ T² (2-dim); its dual base `D⊕D` has extreme points two circles (1-dim). A linear cone isomorphism would give a homeomorphism of ray spaces. | W |
| 1f | Self-duality alone excludes the Stiefel body. Its extreme points are `V₂(ℝ³) ≅ SO(3)`, with π₁ = ℤ₂. The dual (nuclear-norm) extreme points are `{uvᵀ} ≅ (S²×S¹)/±`, which has infinite π₁ because it is doubly covered by `S²×S¹`. | W |
| 1g | **Homogeneity + full effects + capacity ≤ 2 ⇒ the base is a ball `Bⁿ` (or a point).** Proof below. | W + L + E |
| 1h | Literature corroboration of 1g's moral, in general rank: homogeneity + pure transitivity ⇒ self-duality. | L: Barnum–Ududec–van de Wetering, arXiv:2306.00362 (2023) |
| 1i | The pentagon is strongly self-dual, has capacity 2, is pure-transitive, and is not homogeneous. Self-duality: Gram criterion, `G = diag((1+√5)/4, 1, 1)`. Capacity: polygon argument below. Non-homogeneity: the identity component of `Aut` fixes each of 5 rays spanning ℝ³, so it is scalars and `dim = 1 < 3`. | E: `d3`; W |
| 1j | The `Main.md:540` SIC model fails self-duality of the physical effect cone. That cone is polyhedral (4 generators); the state cone is Lorentz. | W |

Output of `d1` (A), the exact upper bound on `dim Lie Aut(K)`:

| body | bound | `dim K` | verdict |
| --- | --- | --- | --- |
| torus | 3 | 5 | not homogeneous |
| Stiefel | 5 | 7 | not homogeneous |
| Carathéodory | 4 | 5 | not homogeneous |
| square | 1 | 3 | not homogeneous |
| Lorentz / 3-ball (control) | 7 | 4 | not excluded; bound tight |

*Proof of 1g.*
1. Ishi realizes every homogeneous cone of rank `r` as `P_V = Z_V ∩ PD`. Here `Z_V` consists of
   symmetric block matrices with diagonal blocks `xₗ I_{nₗ}` and off-diagonal blocks in spaces
   `V_{lk}` (L: Ishi, "Matrix realization of a homogeneous cone", GSI 2015, LNCS 9389, 248–256;
   Yamasaki–Nomura, *Kyushu J. Math.* 69 (2015) 11–48).
2. The block idempotents `Eₗ` are PSD and lie in `Z_V`. So they are effects (in `K*`) and, rescaled
   by `1/nₗ`, states. `tr(Eₗ Eₘ) = δ nₗ` and `ΣEₗ = I ∈ int K*`, so capacity w.r.t. `u = I` is `≥ r`.
3. `K*` is homogeneous, through the equivariant bijection `x ↦ x*` (L: Vinberg, *Trans. Moscow Math.
   Soc.* 12 (1963); Faraut–Korányi Ch. I). So the bound transfers to every unit `u ∈ int K*`.
4. Capacity ≤ 2 therefore gives `r ≤ 2`. With `r = 2`, the realization's off-diagonal Gram condition
   (`AAᵀ` or `AᵀA` scalar; either side suffices) and a Schur complement give
   `{x₁, x₂ ≥ 0, x₁x₂ ≥ q(A)}` with `q` positive definite. That is a Lorentz cone, or `ℝ₊²` when
   `V = 0`, and its bases are ellipsoids.
5. Controls, exact (`d1` (C)): the Ishi form with `A` a 2×2 complex-number block has determinant
   `(x₁x₂ − a² − b²)²`, which gives `L⁴`. The rank-3 Vinberg cone has capacity ≥ 3.
6. Positive ingredient: once full effects are assumed, capacity is intrinsic, and that is what lets
   homogeneity replace self-duality.

**Route 2**

| # | claim | evidence |
| --- | --- | --- |
| 2a | CDP purification is existence of a *pure* `Ψ_AB` with marginal `ρ`, plus essential uniqueness up to a reversible map on `B`. It implies transitivity on pure states, and it is equivalent to the existence and uniqueness of reversible dilations of channels. | L: Chiribella–D'Ariano–Perinotti, *PRA* 81, 062348 (2010), arXiv:0908.1583; *PRA* 84, 012311 (2011), corpus ref. [53] |
| 2b | Transitivity follows from purification by purifying the trivial system's state with purifier `A`. | W |
| 2c | In a classical (simplex) composite the pure states are point masses, whose marginals are point masses. So no non-deterministic state has a purification. The corpus completion carries its randomness in a hidden prior (`Main.md:596`: "the prior carried as realization datum"), which is a mixed joint state. With a point-mass prior the visible law is a single trajectory. So `Main.md:598`'s existence clause is a reversible dilation with a mixed ancilla, which is available in every classical theory, not CDP existence. | W |
| 2d | Exact on the corpus grid (all bijections at `(n_V,\|C_H\|) = (2,2), (2,3), (3,2)`, two priors, `K = 3`; 2,928 instances): (i) in every fiber-freedom witness group the tail-injective members have identical profiles (0 disagreements), so the witnesses are carried by non-injective members; (ii) every pair of same-law tail-injective realizations is isomorphic on the stage-indexed reachable part (32/32, 13,104/13,104, 6,656/6,656); (iii) a single hidden permutation `σ` intertwining the dynamics exists in only 8/32, 1,512/13,104 and 1,520/6,656 pairs. The stage-0 matching is always a permutation of `C_H`. | E: `d2_route2_fibers.py`, `.out` |
| 2e | General form of 2d(ii): for bijective `φ`, `(t, s)` determines `h₀`. Tail-injectivity makes `q_R` (`Main.md:598`) a bijection onto the ledgered tail object, so two such realizations are isomorphic through it, uniquely by universality. | W |

**Route 3**

| # | claim | evidence |
| --- | --- | --- |
| 3a | The literal "repeatable nondemolition tests on frames" is vacuous. The instrument `Tᵢ(ω) = eᵢ(ω)ωᵢ` is positive, repeatable, and fixes the frame states, in any theory with full effects. | W |
| 3b | **Lemma I (ideal-test obstruction).** If `u∘T = e`, `T` is positive and `T|_F = id`, then `T` kills `cone(Z)`, because the only `u`-null cone element is 0. So `lin cone F ∩ lin cone Z ≠ 0` is impossible. | W |
| 3b′ | The intersection dimension is square 1, torus 2, Stiefel 2 and 3-ball 0. The distinguishing effect of the chosen frame is unique: written proofs for the square and Stiefel, with the square uniqueness also hand-derived in the script comments. So no ideal test exists for the square, torus or Stiefel frame. The ball has `T = e(·)(1, n)`. | E: `d3`; W |
| 3c | **Frame transitivity fails for all three bodies.** Each has frames whose midpoint is interior (`(p, −p)`) and frames whose midpoint is on the boundary: the square's adjacent pair, the torus pair with `x` antipodal and `y` equal, and the Stiefel pair `[e₁,e₂]`, `[e₁,−e₂]` (`MᵀM = diag(1,0)`). | E: `d3` |
| 3d | **Centrally symmetric lemma.** If `Ω` is centrally symmetric about `c`, has full effects, and `Aff(Ω)` is transitive on ordered frames, then `Ω` is strictly convex, and with Lemma B an ellipsoid. Proof below. | W |
| 3e | Pentagon, exactly in Q(√5): 10 ordered frames, exactly the distance-2 and distance-3 pairs; `Aut` = D₅ (10 of 60 vertex triples); the orbit of `(0,2)` is all 10 frames (strong symmetry on pairs holds); the centroid lies on 0 of 10 frame segments (spectrality fails); every frame has an effect with singleton certain and zero faces, so measure-and-prepare is an ideal test; the edge effect is valid, so its certain face is an edge and (SF) fails; the edge-effect ideal compression is not positive, with coefficient `(1−√5)/2`. Capacity 2, by a polygon argument: three perfectly distinguishable states need three pairwise-adjacent edges as their zero faces, which forces a triangle. | E: `d3`; W |
| 3f | Torus spectrality: every `(x, y) ∈ D×D` is a mixture of a frame. If `\|x\| ≥ \|y\|`, take a `y`-antipodal pair with `λ = (1+\|y\|)/2`; otherwise the symmetric choice. | W |
| 3g | Spectral + strongly symmetric compact convex sets are exactly the simplices and the normalized state spaces of simple EJAs. | L: Barnum–Hilgert, arXiv:1904.03753 (2019); also Barnum–Müller–Ududec, *NJP* 16, 123029 (2014), arXiv:1403.4147 |

*Proof of 3d.*
1. Affine automorphisms fix the barycentre, which is `c`.
2. Suppose an exposed face `F`, exposed by `f`, has extreme points `q₁ ≠ q₂`. Then `(q₁, 2c−q₁)` and
   `(q₁, 2c−q₂)` are both frames, distinguished by the normalized `f`.
3. A `g` with `g(q₁) = q₁` and `g(2c−q₁) = 2c−q₂` contradicts `g(2c−q₁) = 2c − g(q₁)`.
4. So every exposed face is a single point. Every boundary point lies in some exposed face, so every
   boundary point is extreme.
5. Pure transitivity follows because `(p, 2c−p)` is always a frame.

## 3. Countermodels and controls

The table shows, for each route premise, whether it excludes (✗) or admits (✓) each body. `—`
means not applicable or not computed.

| body | capacity | 1: homog. | 1: self-dual | 2: pure-transitive | 3: ideal frame tests | 3: frame-transitive | spectral | (SF) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| square gbit | 2 | ✗ E | ✗ E | ✓ (D₄) | ✗ E/W | ✗ E | ✗ | ✗ |
| torus `D×D` | 2 | ✗ E | ✗ W | ✓ | ✗ E/W | ✗ E | ✓ W | ✗ |
| Stiefel | 2 | ✗ E | ✗ W | ✓ | ✗ E/W | ✗ E | — | ✗ |
| 3-ball (control) | 2 | ✓ E | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| segment (classical bit) | 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **pentagon** (countercontrol) | 2 W | ✗ W | **✓ E** | ✓ E | **✓ E** | **✓ E** | ✗ E | ✗ E |
| Carathéodory `C₂` | 3 | ✗ E | — | ✓ | — | — | — | — |
| Vinberg cone (rank 3) | ≥ 3 E | ✓ | ✗ (L) | — | — | — | — | — |

- **Controls passed.**
  - The Lie-algebra bound reproduces the true dimension for the Lorentz cone (7), and equals the
    dimension of the evident symmetry algebra for the torus (3) and the Stiefel body (5). So the
    method does not over-count where the answer is known. Being an upper bound, it is sound for
    exclusion in any case.
  - The ball passes every route premise. Lemma I gives a trivial intersection for it.
  - The Ishi rank-2 control gives `L⁴`.
- **Countercontrols against favourable readings.**
  - "Route 3 excludes all three bodies" is favourable. Its countercontrol, the pentagon, survives
    ideal frame tests and frame transitivity, so the route does not reach (SF).
  - "Self-duality is load-bearing in route 1" is favourable. The pentagon refutes it as a standalone
    premise.
  - The torus and the pentagon show that both of Barnum–Hilgert's halves are load-bearing.
  - The segment survives every route, so K∞-R remains necessary.
- **Assumption-watch marker (cross-propagation).** All three corpus countermodels are centrally
  symmetric. Lemma D then caps their capacity at 2, and 3d makes frame transitivity alone exclude
  them. The corpus control set therefore cannot test any frame-symmetry premise for sufficiency.
  Future SF-replacement probes need a non-centrally-symmetric capacity-2 control. The pentagon is
  one such control, but it has a finite group; no connected-group one is known.
- **Route 2 control.** The script reproduces the corpus fiber-freedom witnesses on the same grid (2,
  6 and 5 witness groups) before splitting them by injectivity.

## 4. Proposed next theorem

| ID | statement | layer |
| --- | --- | --- |
| D-T1 | **Lemma I.** For a GPT system with unit `u`, an effect `e` with certain face `F` and zero face `Z`, and any positive linear `T` with `u∘T = e` and `T` = id on `lin cone F`, we have `lin cone F ∩ lin cone Z = {0}`. | Lean candidate (finite-dim linear algebra) |
| D-T2 | **Centrally symmetric frame lemma (3d).** A compact convex body with interior, centrally symmetric, with full effects and `Aff(Ω)` transitive on ordered pairs of perfectly distinguishable extreme points, is strictly convex. With Lemma B (K∞ §7) it is an ellipsoid. | Written; Lean candidate after Lemma B |
| D-T3 | **Homogeneous bit.** If the state cone is homogeneous, effects are full and capacity ≤ 2, then the state space is affinely `Bⁿ` (`n ≥ 1`) or a point. In particular the effect cone is self-dual and (SF) holds. | Written, resting on Ishi's realization (L) |
| D-T4 | **Pentagon facts** (exact, Q(√5)). The regular pentagon gbit with full effects has capacity 2; it is strongly self-dual; `Aut` = D₅ acts transitively on ordered frames; it is not spectral; it is not homogeneous; it violates (SF); and its edge effect has no positive ideal compression. | Exact (`d3`) |
| D-T5 | `dim Lie Aut` for the torus, Stiefel, Carathéodory and square cones is at most 3, 5, 4 and 1 respectively. These are below the cone dimensions 5, 7, 5 and 3, so none of these cones is homogeneous. | Exact (`d1`) |
| D-T6 | **Minimal-completion uniqueness.** Two faithful bijective realizations of one finite-horizon law `P` that are tail-injective at stage 0 are isomorphic on their stage-indexed reachable parts, by a unique visible-preserving, dynamics-intertwining, prior-preserving isomorphism. In general this isomorphism is not induced by one hidden permutation. Fiber freedom is carried by non-injective fibers only. | Written (corollary of `Main.md:598`) + exact grid (`d2`) |
| D-T7 | **No classical purification.** In a classical composite, no non-deterministic visible law is the marginal of a pure joint state. The corpus completion's existence clause is a reversible dilation with a mixed ancilla. | Written (trivial) |

Open probes, not theorems:
1. A connected-group, non-centrally-symmetric capacity-2 body that is frame-transitive but not
   strictly convex. A candidate is `conv{(cos 2t, sin 2t, cos 3t, sin 3t)}`, which is not centrally
   symmetric; its capacity is not computed.
2. A connected self-dual, non-homogeneous bit.

Each probe would test whether K∞-R closes the gap that the pentagon (finite group) exposes.

## 5. Dependencies

- **Other threads.**
  - Route 1's output is NB-1's hypothesis. So the `d = 3` conclusion still depends on copy
    naturality and composition (Fork C/D; whichever thread owns the conjugacy reduction or the
    three-copy probe).
  - Excluding the segment depends on K∞-R (the field-neutral drivability thread).
  - Every route here presupposes Fork B. The full-effects / K∞-1 Naimark work is upstream of all
    three routes.
- **Corpus declarations (read at `4507b025`).**

  | route | file:line | declaration | what it bears on |
  | --- | --- | --- | --- |
  | 1 | `verification/lean-mathlib/OIBridge/JordanClassification.lean:84` | `psd_iff_trace_nonneg` | self-duality, ℂ-PSD only; imported kinematics |
  | 1 | `verification/lean-mathlib/OIBridge/NativeGateBall.lean:5-6` | NB-1 header | assumes "full self-dual effect cones" |
  | 1 | `verification/ROADMAP.md:984-985` | K1 | same NB-1 hypothesis, CONDITIONAL |
  | 1 | `k0/K0-SOURCE-AUDIT.md` row 3 | — | homogeneity absent from the corpus |
  | 2 | `papers/Main.md:596` | — | prior as realization datum |
  | 2 | `papers/Main.md:598` | theorem | existence, universality and fiber-freedom clauses |
  | 2 | `papers/Main.md:600` | remark | "supplies the substratum-level existence half" (see the finding on route 2) |
  | 2 | `papers/oi_lattice_code/foundations/purification_probes.py:149-156` | fiber freedom | witness = differing tail-multiplicity/prior profiles |
  | 2 | `verification/lean-mathlib/OIBridge/BoundaryAudit.lean:106` | `purification_unconditional` | ℂ-PSD purification, existence only |
  | 3 | `verification/lean-mathlib/OIBridge/OperationalAssembly.lean:658` | `readout_is_localLuders` | Lüders form at matrix level |
  | 3 | `verification/lean-mathlib/OIBridge/CarrierGeneralOIPlus.lean:110` | `ReversibleRichness` | matrix transitivity assumed |
  | 3 | `verification/lean-mathlib/OIBridge/SubstratumInterface.lean:126` | `preservesDiag_conj_of_monomial` | substratum operations preserve the diagonal, so they cannot supply non-classical frames |

- **Hilbert-space import, per route.**
  - Route 1 imports no ℂ: the output is any real, complex, quaternionic or octonionic Jordan
    structure, and a ball of any `n` for a bit. It does import a real inner product and full
    effects.
  - Route 2 imports no Hilbert space, but it does import a composition rule with pure entangled
    states.
  - Route 3 imports no Hilbert space; it imports full effects.
- **Corpus sourceability, per route.**
  - Route 1: not sourceable. The corpus's classical layer, the orthant `ℝ₊ⁿ`, satisfies
    homogeneity and self-duality trivially, so the premises select nothing there. The only
    non-classical cone in the corpus is the imported PSD cone.
  - Route 2: not sourceable. The existence half is classical dilation (2c), and the uniqueness half
    fails as wholes and as single-permutation relabelings (2d).
  - Route 3: not sourceable. Neither the observer level nor the manuscripts carry sharp-test or
    spectrality language (K∞ §14(c)), and the Lüders form exists only at matrix level.
- **Unsourced premises carried by the findings.**
  - Ishi's realization theorem and the duality of homogeneous cones (for D-T3).
  - The CDP and Barnum–Hilgert statements as summarized from search abstracts. Their PDFs were not
    readable here, so theorem numbers are unverified.
  - Standard topology of π₁(SO(3)) (for 1f).
