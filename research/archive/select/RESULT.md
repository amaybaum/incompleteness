# SELECT — research note (read-only; 2026-10-03; charter CHARTER.md `277386df`)

Base `0f2687b7`. No act, freeze, PR or round-2 theorem. Every claim is tagged: [K] kernel identifier,
[C] corpus text, [S] sealed scratchpad result, [3A] Level 3A, [new] argued here, [chk] exact check in checks.log.

## 0. Headline

The weakest field-neutral selector is not transitivity and not "continuity": it is the availability, on the
**completed** body of the exposed sector, of **one reversible operation of infinite order** together with
**energy observability** (the generators of the available reversible dynamics are observables, equivariantly).
Transitivity is satisfied by the classical-epistemic octahedron [chk]; an infinite-order operation cannot exist
on any finite-stage sector [S NG1, F-D3], so the selector forces the completion and is where the corpus's
A1-finiteness meets its own "continuous controllability is an empirical extension" [C GR:260]; and on the
completed body the ball then follows without any continuity hypothesis [S Thread N, ELL-ellipsoid] once the
dimension is 3, which is equivalent, given the drive, to transitivity + energy observability [S Thread R].
Round 2 reduces to one named theorem (§4) with four residual obligations (§6).

## 1. What the corpus already says (the matrix setting)

- [C GR:258] "current OI substratum + continuous off-diagonal controllability ⟺ exact finite endomorphic
  operational QM"; [C GR:260] the controllability resource "is not entailed by A1–A6; it is an empirical
  extension of the current substratum"; [C GR:262–264] it holds "exactly when the continuous layer flow of one
  involution of the configuration space that moves some configuration, the ancilla a spectator, is an available
  operation at every level and every intermediate time".
- [C GR:230, :246] two weakenings of (iv) already stated: *reversible richness* (dynamical Lie algebra contains
  su) and *phase-free richness* (some pair of distinguishable states continuously drivable; every exchange of two
  distinguishable states available; no phase operation).
- [C Main:352] the reconstructions' continuous-transitivity axiom is "a hypothesis of their continuum endpoint,
  which the classical-dimension obstruction places beyond any fixed finite carrier".
- [K oi_alone_not_qm, five_way_minimality, exactAll_iff_substantive]: (iv) is independent of the OI core and of
  (iii), (v).

So in the matrix setting the corpus's own minimal selector is already "a continuous flow of one involution,
plus selectable phases", and it is explicitly a premise. The field-neutral question is what that becomes when
"continuous flow", "involution" and "phase" are not available words.

## 2. Candidate premises, ordered by logical strength (weakest first), each field-neutral

Setting for all of them: the exposed sector's body Ω (compact convex, FiniteRank [S CMP-1]) with available
reversible operations G ⊆ Aff(Ω) and available effects; preparations and effects are protocol data, operations are
RESPECT data on stage preparations with values in the completed body [S OPACT-C].

| # | Premise (field-neutral statement) | Excludes the 3A octahedron? | Sufficient for a ball? | Source of each piece |
|---|---|---|---|---|
| C0 | none (G = Sym({0,1}²), finite) | — | no: Ω = octahedron, 7 reachable states | [3A] |
| C1 | **TRANS**: G is transitive on the boundary (pure) states | **no** — Sym({0,1}²) is transitive on the six vertices [chk] | no | [S OrbitGeneration `BoundaryTransitive`]; [chk] |
| C2 | **ORD∞**: some available reversible g has infinite order on Ω (F-D2 form of a drive; no continuity) | **yes**, and every finite-stage sector: a polytope's affine automorphism group permutes its vertices, hence is finite [S NG1, F-D3; new] | no: orbit-generated + connected drivability + binary capacity + full effects ⇏ strict convexity (torus, Stiefel bodies) [S K∞ §11, Lemma D] | [S DRIVE F-D2, F-D3; S OI-STAGE NG1; S K∞ §11] |
| C3 | ORD∞ + **DIM3** (affine dimension of Ω is 3) | yes | **yes**: ELL-ellipsoid — DIM3 + IIP-N + DriveCore ⇒ Ω is a ball, **no continuity needed** | [S Thread N `ell_ellipsoid`]; DIM3 "never derived" [S N:20] |
| C3′ | ORD∞ + TRANS + **EO** (energy observability: injective φ from the generator algebra of G into the observables, equivariant under the commutator) | yes | yes: given the drive, compactness and FiniteRank, {TRANS, EO} ⇔ DIM3 [S Thread R], then C3 | [S Thread R `EnergyObservable`, DIM3 ⇔ TRANS + EO] |
| C4 | (SEC) + (SF) singleton faces + TRANS | yes (strict convexity excludes polytopes) | yes: Lemma C then Lemma B | [S K∞ §15]; (SF) "open; independent of dynamics, capacity and full effects" |
| C5 | (iv) full reversible control: every finite unitary on every composite | yes | yes (and all of Q) | [K HasCompositeUnitaryControl]; matrix carrier presupposed (G-MATRIX, L-G) |

Reading: C1 is the surprise and the gem. C2 is the first premise that does any work, and it does exactly one
thing — it is incompatible with any finite exposed sector — so it is the point where the selection principle
and A1 (finiteness) meet: the selector can only hold on the completed body, never at a stage. C3 and C3′ are the
weakest sufficient packages found; C3′ is C3 with the undeduced dimension replaced by two operational statements.
C4 is an alternative route whose extra premise (SF) the K∞ round already classified as independent content.
C5 is the corpus's matrix-setting answer and is strictly stronger (it fixes the whole instrument algebra).

## 3. Countermodels (deliverable 3)

- **Without C2 (finite G):** the 3A sector itself — 76 invasive κ, dims [2,3,4,4,4], seven reachable points,
  hull the octahedron [3A]; TRANS holds there [chk]. What survives: Q_fb representation (S ⇔ D ⇔ Q_fb), G-layer,
  R4(r; G₃) — i.e. everything except Q. Exact and sealed.
- **With C2 but without DIM3/EO:** the K∞ side probe's bodies (torus, Stiefel): orbit-generated, connected
  non-abelian drivability, binary capacity, full effects, not strictly convex [S K∞ §11]. What survives: a
  drivable non-quantum theory.
- **With C2 + DIM3 but without effect functoriality:** the ball of states with a deficient effect family — the SIC
  embedding carries the Bloch ball into Δ₃ "but cannot carry the sharp effects" [C Main:540]; K∞-E's Naimark step
  is open field-neutrally [S K∞ §15]. What survives: the right state space, not the right effect algebra.

## 4. The shortest remaining theorem (deliverable 4)

**Round-2 target (not declared; stated as the object to prove).** Let Ω be the completed body of the exposed
sector (OPACT-C: operations are RESPECT data; FiniteRank). Assume, for the observer's available reversible
operations G and available effects:

1. **ORD∞** — some g ∈ G has infinite order on Ω (equivalently, by F-D2, a reversible AffineRespect datum of
   infinite order; no continuity);
2. **TRANS** — G is transitive on the boundary states;
3. **EO** — energy observability for G on Ω;
4. **V4′** — seed-orbit availability: SEED-AVAIL, SEQ, TRANS± [S Thread P].

Then (a) Ω is a 3-dimensional ball [S R: {TRANS, EO} ⇔ DIM3 given 1; S N: ELL-ellipsoid], and (b) the available
binary effects contain the sharp directional family (1 + b·r)/2 [S Thread H decisive test; `lorentz_of_effects`].
Everything in (a) is already proved in the sealed threads; the theorem is their composition plus the sourcing of
hypotheses 1–4 from the interface. **Companion insufficiency statement:** dropping 1 admits the octahedron (3A);
dropping 3 admits the torus/Stiefel bodies (K∞ §11); dropping 4 admits the ball without its sharp effects
(Main:540). All three countermodels exist exactly.

What is *not* in this theorem: composites ((iii), (v)), the coherent extension of the dynamics beyond Q_fb, and
the identification/gauge question (§6).

## 5. Circularity audit (deliverable 5)

- ORD∞ names no field, dimension, convexity or composite; it is an order statement about one available affine
  map. It presupposes the completed body (a limit object), which is a *scope* commitment, not a quantum one; it
  is exactly where the corpus's own "continuous controllability is an empirical extension" [C GR:260] lands.
- TRANS: purely operational; satisfied classically [chk], so it imports nothing quantum.
- EO: stated with `genAlg` (closure of linear parts of G) and `Obs` (dual of the body's direction) and a
  commutator-equivariant injection — real-affine, no complex structure, no Hilbert space. It *is* the
  nonclassical input: for a classical simplex the generator algebra is zero, so EO is vacuous there and ORD∞ fails.
  Flag: its name ("energy") is suggestive; its content is the dynamical-correspondence axiom of the operational
  reconstructions, and it should be stated with that provenance, not as a substrate fact.
- V4′: operational closure statements about availability; no effect space is quantified over before it exists
  (Thread H's guard).
- None of 1–4 says "all unitaries are available"; C5 is not assumed. The matrix-setting equivalence [C GR:258]
  is the yardstick, not an input.
- Residual risk: "completed body" and "available on the completed body" are not operational words at any finite
  stage [S OPACT countable-stage no-go]. The premise is honest only if availability on the completion is itself
  given an operational reading (limits of stage-available operations: LIMCLOSE-C [S DRIVE :81]). That reading is a
  premise, not a theorem — recorded as the thread's one irreducible non-finite commitment.

## 6. Dependency boundary (deliverable 6)

Independent of 3B (settled here): the ordering C0–C5; the gem that TRANS is non-selective; the finite-sector
incompatibility of ORD∞ (NG1, F-D3 are rule-independent); the composition theorem of §4 as a target; the
countermodels.

Waits for 3B: the **identity of Ω**. 3A fixes it for the linear rule under H₀ (pair-marginal space; FiniteRank
holds). 3B's R_5 cell may add a second rule with the same body; its H₁ cell may lift the ceiling, in which case
FiniteRank — the standing hypothesis of OPACT-C, Thread N and Thread R — is itself in question for correlated
hidden laws, and the premise ordering would have to be re-derived on a different body. Also waiting: whether the
observer object after 3B is still OBS-R with I₃ (the selector must be stated for the actual interface).

Residual obligations for round 2 (not part of this note's claims): (i) source hypotheses 1–4 from the
interface rather than assume them, with LIMCLOSE-C made explicit; (ii) K∞-E / Naimark field-neutrally;
(iii) composites via (iii), (v) and Thread H's primitives 1–2; (iv) the identification question: the Q_fb
representation modulo the phase-locking gauge [C Main:224, :632] and the fixed-Ĥ lemma [C Main:510].

## 7. Classification (§A.31)

- **NEW:** TRANS is satisfied by the classical-epistemic octahedron (transitivity does not select); the selector
  must be of infinite order, hence lives only on the completed body — the A1/selection tension located exactly.
- **POSITIVE:** the corpus's matrix-setting selector [C GR:258–264] and the sealed field-neutral threads (DRIVE
  F-D2, N, R, P, H) compose into one theorem target with no gap in the state-space leg.
- **CONFIRMING:** EO as the nonclassical input agrees with the reconstruction literature's dynamical
  correspondence; (SF) remains the alternative route's independent premise.
- **BORDERLINE:** whether "available on the completed body" has an operational reading (LIMCLOSE-C) — the one
  commitment this note cannot discharge.

Not run: anything decisive. checks.log holds the two exact design checks (transitivity, invariance).
