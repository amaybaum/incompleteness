# EQ-A — running notes (K∞-OBS: observational foundations)

Base: certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, read-only at `scratchpad/eq/base/`.
Writes only under `scratchpad/eq/A/`. No git writes, no Lean, no subagents. Exact arithmetic for every claim.

## 0. Productivity test (fixed before any branch is walked; §A.31)

A finding of this thread is a **gem** iff BOTH:

1. it is strictly stronger than the obvious restatements already in the record, namely
   - "K∞-Geom (SF / RelStrictConvex) is false for complex QM at level ≥ 3, so it must be elementary-scoped"
     (kn-elementary-carrier-census §4),
   - "SF ⇔ RelStrictConvex given SEC" (KINF-2 L4/L5),
   - "capacity two with full effects is a load-bearing, non-disguised scope premise" (SA-LEDGER P-D, ElemScope),
   - "FiniteRank fails on some infinite carriers" (SA P3, rank/RESULT);
2. AND it either (a) decides a QA cell with an explicit witness or an exact countermodel, or (b) exposes an
   assumption hidden in how a K∞ seam is stated (assumption-watch marker).

Below the bar: record-only (CONFIRMING / ELABORATING / BORDERLINE).

Pre-registered decision rules (rules, not expected numbers):

- QA1 is **THEOREM ROUTE** iff a predicate ELEM and a principle GEOM are exhibited such that every one of
  (i) ELEM ∧ GEOM ∧ SC∞ ∧ FiniteRank ⇒ the body-level input consumed by TRB-1/OG-1/EFF-1 (written proof, kernel
  candidate), (ii) the complex qubit satisfies ELEM and GEOM (exact), (iii) every complex level-n system, n ≥ 3,
  either fails ELEM or satisfies GEOM with no ball demanded (written proof for all n + exact instances n = 3, 4),
  (iv) each named foil is excluded by ELEM ∧ GEOM, or the exclusion is shown to need a named further premise
  (exact), holds with green controls. If (iii) fails for every candidate: COUNTEREXAMPLE. If (i) cannot be
  proved for any candidate passing (ii)–(iv): OPEN with the named wall.
- QA2 / QA3 are **INDEPENDENT PREMISE** iff an exact countermodel satisfies the QA1 package plus K∞-Stage (and
  whatever else is claimed) and violates the seam; **THEOREM ROUTE** iff a written proof derives the seam;
  otherwise OPEN.
- Every favourable verdict gets a countercontrol that must come out the other way (§A.21, §A.31); a verdict
  printed over a failed or vacuous control is void.

## 1. Branch nodes (depth-first; verdict recorded at each node)

### Node 1 — what do TRB-1 / OG-1 / EFF-1 (and KTRANS-DENSE-1) actually consume? (kernel reading + written)

Read at the base:
- TRB-1 `exists_affine_image_eq_eball` (TransitiveBody.lean:602): compact, convex, interior, `0 < d`,
  `PreservesBody`, `BoundaryTransitive`. Purity `extreme_of_isBoundaryState_of_transitive` (TB:290).
- OG-1 `seedOrbit_ball3_eq` / `ballEffect_mem_avail`; EFF-1 `sharpFamily_subset_avail` (EffectSpace.lean:374),
  `maxConeOf_avail_eq` (ES:572): `PreservesBody`, `SharpSeed`, `BoundaryTransitive`, `SeedOrbitAvailable`.
- KTRANS-DENSE-1 (`DenseOrbit.lean`): the ball and cone theorems with `DenseBoundaryOrbit` (DO:53) in place of
  `BoundaryTransitive`; purity (TB:290) is NOT covered by the dense form.
- `RelStrictConvex` / `SingletonFaces` occur in **no module other than KInfFoundations** (grep at the base). The
  K∞-Geom slot feeds nothing downstream in the landed chain.

Written (two directions, §A.34):
- (→) under TRB-1's hypotheses, `BoundaryTransitive Ω G` ⇒ `RelStrictConvex Ω` (purity TB:290 + "a proper
  convex combination of two distinct states is not extreme") and ⇒ `ExtremeTransitive Ω G` (extreme ⇒ boundary,
  `isBoundaryState_of_extreme` TB:284).
- (←) **Theorem A**: `RelStrictConvex Ω` ∧ `ExtremeTransitive Ω G` ⇒ `BoundaryTransitive Ω G`, with no further
  hypothesis (a boundary state of a relatively strictly convex body is extreme). Dense analogue: RelStrictConvex ∧
  (dense orbits on extreme points) ⇒ `DenseBoundaryOrbit`.

**Verdict N1.** The geometric input the ball route needs is `RelStrictConvex` of the elementary body (boundary
purity). In the landed route it is *implied* by K∞-Trans (exact, and via the ball conclusion also by the dense
form), so K∞-Geom is a separate obligation only when transitivity is stated on pure states (extreme points), the
form of Masanes–Müller's "symmetry" requirement. QA1(i) is therefore read as: ELEM ∧ GEOM ∧ SC∞ ∧ FiniteRank ⇒
`RelStrictConvex` of the (chart) body; Theorem A then turns pure-state transitivity into the K∞-Trans that TRB-1,
OG-1 and EFF-1 consume. [ELABORATING: purity is landed; the converse Theorem A and the "no downstream consumer"
fact are new bookkeeping.]

### Node 2 — the decisive fork for QA1: scope the principle, or localize it?

The census (kn-elementary-carrier-census §4) reads the qutrit counterexample as "SF / RelStrictConvex hold only for
an elementary system, so the principle must be scoped". Gem-finding question: *what assumption is hidden in
"the principle must be scoped"?* — that the principle has to be stated for the whole body. Two branches:

- **2a (scope; SA-LEDGER P-D):** ELEM_cap = capacity ≤ 2 with `fullEffects`, plus a sharp pair; principle
  "ELEM_cap ⇒ SingletonFaces(full)". Passes (ii)/(iii) for full QM (capacity of M_n(ℂ) is n). Its principle says
  nothing about n ≥ 3. Reading with *available* effects is falsified by a quantum model (exact C5: qutrit with
  avail = {1, P, 1−P} has operational capacity 2 and violates SF(avail)); so it must be read with `fullEffects`.
- **2b (localize):** GEOM2 = "the face generated by any two distinct pure states is relatively strictly convex";
  effect form SF2 = "inside the face generated by two pure states, a test proper on that face is certain on at
  most one state". Scope predicate ELEM2 = "two distinct pure states whose midpoint is not a boundary state" (the
  body is the face generated by two pure states).

Decisive check (exact, `qa1_controls.py`, 71 checks, replay byte-identical; sha256 script `86ef82a6…`, output
`b4b211cd…`):
- GEOM2 / SF2 hold in complex QM at **every** n (written proof: a pair face is the state space of a 2-dim
  subspace K; certain set of an effect inside it is K ∩ ker(I−E), of dimension 0, 1, or 2 = "not proper on the
  face"); exact at n = 3 (6 pairs), n = 4 (3 pairs), and on the census effect P = diag(1,1,0): on F(|0⟩,|1⟩) P is
  the unit of the face (no obligation), on F(|0⟩,|2⟩), F(|0⟩,ψ), F(|1⟩,|0⟩+2i|2⟩) its certain face is one state.
- ELEM2 fails at every n ≥ 3 (written rank argument; exact witnesses on the same 9 pairs and 3 real-qutrit pairs);
  holds for the qubit (m = I/2 ≥ ½·I).

**Verdict N2: branch 2b.** The census counterexample is not a counterexample to the localized principle; the
principle needs no scope at all, and only its *application* (pair face = whole body) needs ELEM2. [NEW: exposes
the hidden assumption that K∞-Geom must be scoped; the localized form is the strict-convexity weakening of the
Alfsen–Shultz Hilbert-ball property (literature, unverified against source) and is what a Kₙ subspace principle
would extend.] Branch 2a is recorded as an admissible alternative (it also answers QA1 for full QM).

### Node 3 — QA1 (iv), the foils (exact unless marked)

| body | ELEM2 | GEOM2 | outcome |
|---|---|---|---|
| complex qubit | ✓ | ✓ | elementary, strictly convex |
| complex n = 3, 4; real qutrit | ✗ | ✓ | not elementary; principle holds |
| classical bit | ✓ (CS lemma) | ✓ (written) | **not excluded**: needs HasTwoSharpTests or ElementaryDrivability |
| square, affine-regular hexagon | ✓ | ✗ | excluded |
| regular pentagon (ℚ(√5)) | ✓ | ✗ | excluded |
| torus D×D, Stiefel 3×2 | ✓ | ✗ | excluded |
| triangular bipyramid (capacity 3) | ✓ | ✗ | excluded |
| classical trit, cone over disk | ✗ | ✓ (written) | not elementary |
| rebit disk | ✓ | ✓ (written) | **not excluded**: needs corrected drivability (J clause; written) or DIM-1 |
| balls d ≥ 4 | ✓ | ✓ (written) | **not excluded**: drivable and boundary transitive; needs DIM-1 |

Controls: C1 (drop "pure": the qutrit enters scope — "pure" load-bearing), C2 (unlocalized SF fails on the qutrit,
same code path), C3 (Theorem A: square is ExtremeTransitive under its 8 automorphisms but not boundary transitive
— RelStrictConvex load-bearing; one-axis flow — ExtremeTransitive load-bearing, kernel OG:620), C4, C5.

A control defect was caught and fixed during the walk: the square automorphism loop first stored late-binding
closures (all eight maps equal), which made `C3.square_not_boundary_transitive` vacuous; the extremal-transitivity
check failed, the closure was bound, and a distinctness check was added.

### Node 4 — maximum skepticism on the favourable branch

- **Disguise.** On one body, ELEM2 ∧ GEOM2 ⇔ RelStrictConvex ∧ (two extreme points). The *instance* is the
  conclusion restated, exactly as SF ⇔ RSC given SEC already was (KF:575/590). The content is (a) the uniform
  principle over all systems, true in all finite-dim complex QM, and (b) the field-neutral scope. Recorded, not
  hidden.
- **Heredity (assumption-watch, NEW).** C4: four pure qubit states (±3/5, ±4/5, 0) span a rectangle; as a body it
  is ELEM2 and violates GEOM2, while SF2 with quantum effects holds and SEC with quantum effects fails at the edge
  midpoint. Every geometric seam (GEOM2, SF(full), RelStrictConvex, K∞-Trans) presupposes that the completed body is
  the *full* state space of the system ("state completeness"); the effect form with quantum effects is hereditary.
  This is an unnamed reading of K∞-Stage.
- **Effect restriction.** ELEM2 and GEOM2 are effect-free, so restricting effects cannot move a quantum body into
  scope (contrast C5 for the operational-capacity reading).
- **Capacity.** ELEM2 alone does not bound capacity (bipyramid: capacity 3, exact); ELEM2 ∧ GEOM2 does (≤ 2,
  written via KF:590).

**Verdict QA1: THEOREM ROUTE** (written proof of (i) with a Lean candidate; (ii)–(iv) exact + written), with GEOM2
an INDEPENDENT premise (torus: ELEM2, ExtremeTransitive, drivable, capacity 2, full effects, FiniteRank, violates
GEOM2 — exact here and in the KINF-2 probe; pentagon adds strong self-duality).

### Node 5 — literature before closure (search summaries only: arXiv, publisher and author pages are blocked by the
egress proxy; every item below is UNVERIFIED against the source)

- Alfsen–Shultz, Acta Math. 140 (1978), "State spaces of Jordan algebras": *Hilbert ball property* — two extreme
  points generate a norm-exposed face affinely isomorphic to a Hilbert ball (finite or infinite dimension); with
  spectrality it characterizes JB state spaces (summary cites Cor. 7.4). Alfsen–Hanche-Olsen–Shultz, Acta Math. 144
  (1980): the *3-ball property* for C*-algebras. → GEOM2 is the strict-convexity weakening of this axiom.
- Masanes–Müller–Augusiak–Pérez-García, PNAS 110 (2013) 16373: four postulates incl. *No Simultaneous Encoding*
  (a gbit perfectly encoding one bit carries no further information) — SF for sharp tests, *scoped* to the
  information unit (branch 2a's strategy).
- Masanes–Müller, NJP 13 (2011) 063001: finiteness, local tomography, equivalence of subspaces, symmetry, all
  measurements allowed. "Symmetry" = ExtremeTransitive; "equivalence of subspaces" is the Kₙ-type extension of GEOM2.
- Barnum–Müller–Ududec, NJP 16 (2014) 123029: no higher-order interference + classical decomposability + strong
  symmetry leave balls of every dimension, the octonionic 3-level system and R/C/H QT; energy observability leaves C.
  → consistent with balls/disk/bit surviving the elementary package.
- Wilce (QPL 2016; arXiv 1206.2897, 1606.09306): *sharp* = each basic (atomic) outcome is certain on exactly one
  state. → a third localization (to atomic effects); not pursued: delivering RSC from it needs supporting-effect
  completeness by atomic effects on the elementary body, which is not automatic (named wall, not walked).

### Node 6 — QA2 (exact, `qa2_towers.py`, 18 checks, replay identical; sha256 script `667e9f8d…`, out `514c8989…`)

- SIC tower (Bloch ball in rational tetrahedral coordinates s, Σs = 0, (3/4)Σs² ≤ 1; stage effects = response
  effects Σcᵢ(1+sᵢ)/4): SC∞ (one global formula, nested stages), BinaryVisible (p1+p2 | p3+p4, unsharp), FiniteRank
  (rank 4), ELEM2 + GEOM2 (a ball), fullAut 3 / ratRefl 3 transitive / dense (landed families). Identity
  (Σc)² − |Σcᵢaᵢ|² = (8/3)Σ_{i<j}cᵢcⱼ ⇒ no response effect is a sharp seed ⇒ SeedOrbitAvailable fails for every
  nonempty G (transports of sharp seeds are sharp, OG:107).
- SIC+axis tower (adds r = 2p₁ = (1+s₁)/2, sharp at the stage-3 preparations ±a₁): ElemVis holds, K∞-Seed holds with
  an available seed (sharpSeed_completion SC:224), and V4 fails for every G with a dense or transitive boundary
  orbit (the only available sharp seeds are r, 1−r; transport along the tetrahedral reflection is 2p₂, exact
  non-membership).
- Positive control: the 24 tetrahedral symmetries are label-dual on the all-axes tower and V4 holds for them.
- K∞-Seed *as stated* (`SharpSeed Ω r`, r unconstrained) is automatic on a compact body with two points (rescale a
  non-constant coordinate): written.
- V4 ⇐ label-dual inverses of G + a stage-effect seed (written; Lean candidate `seedOrbitAvailable_of_labelDual`).
  Protocol towers (prefix-closed) are label-dual by construction (SA P-A, oistage F-S1).

**Verdict QA2.** K∞-Seed: THEOREM ROUTE (trivial as stated; with ElemVis anchored to a stage-level sharp pair via
SC:224). K∞-V4: INDEPENDENT PREMISE of the QA1 package + K∞-Stage (+ K∞-Seed, K∞-Trans/dense, K∞-Drive, abstract
K∞-Act): SIC+axis tower; THEOREM ROUTE once K∞-Act is taken in label-dual form. [V4 ⇐ label dual: NEW reduction;
SIC countermodels: CONFIRMING/ELABORATING of Main.md:540 + KINF-2's SIC control.] Side remark (ELABORATING): exact
transitivity + V4 with countably many available effects is impossible in d ≥ 2 (EFF-1's sharpFamily_subset_avail
forces the uncountable sharp family); KTRANS-DENSE-1's dense form removes this, consistent with countable
label-dual families.

### Node 7 — QA3 (exact, `qa3_l2tower.py`, 14 checks, replay identical; sha256 script `0d26d2a5…`, out `4264ae70…`)

- ℓ² tower (rational points / rational unit directions of Qⁿ, e_u(x) = (1+⟨u,x⟩)/2): SC∞, BinaryVisible with the
  sharp pair ±e₁, ELEM2, GEOM2, capacity 2, HasTwoSharpTests, K∞-Seed, V4 (rational Householder reflections act on
  the completion space by label permutations: label duals), dense boundary orbit, exact transitivity (all orthogonal
  maps), drivability (bounded extensions via Hahn–Banach, written) — and stage ranks n + 1: **not FiniteRank**. The
  chart-dependent clauses (Undoes, inducedEquiv, TRB-1 normalization) are not even statable without FiniteRank.
- Finite-carrier route (the only recorded observer-native source of FiniteRank): NG1 polytope + ELEM2 ∧ GEOM2 ⇒
  dimension ≤ 1 ⇒ contradicts HasTwoSharpTests. Closed.
- **Theorem R (written, NEW):** compact convex body, RelStrictConvex, two points, body group with dense boundary
  orbit, sharp seed with V4 into 1-Lipschitz effects (the stage coordinates are) ⇒ FiniteRank (Kakutani,
  Arzelà–Ascoli, Riesz). Converse: FiniteRank ⇒ the completed body is compact. So under the package, FiniteRank ⇔
  operational compactness ("uniform finite resolution" of the realized preparations over all readbacks).
- Controls: ℓ² tower (all hypotheses but compactness; not FiniteRank — compactness load-bearing); compact ellipsoid
  tower Σi²xᵢ² ≤ 1 (compact, ELEM2, GEOM2, transitive, sharp visible pair, not FiniteRank; V4 fails exactly — V4
  load-bearing).

**Verdict QA3.** INDEPENDENT PREMISE relative to the whole single-system package (ℓ² tower). THEOREM ROUTE from
uniform finite resolution (operational compactness) given V4 and a dense boundary orbit; whether OI supplies uniform
finite resolution is OPEN (not computed for the lattice rules).

### Node 8 — fixed point of the gem search (§A.31)

Passes after Node 7 re-examined: (a) the atomic localization (Wilce) — wall named, not walked; (b) capacity-2 ⇒
two-generated in dim ≥ 3 — not needed for any cell, left open; (c) whether operational compactness holds for the OI
lattice completions — outside this thread's budget, OPEN. No further NEW finding in these passes; stop.
