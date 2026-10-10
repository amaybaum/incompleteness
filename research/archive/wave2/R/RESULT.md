# Thread R (wave 2): sourcing DIM3 of the elementary (visible-factor) body

Read-only research against certified main L = `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`. Nothing here is governed,
landed or adopted.

Paths are under `verification/lean-mathlib/OIBridge/`. Abbreviations: KF `KInfFoundations`, OG `OrbitGeneration`,
ON `OrbitNormalization`, NGB `NativeGateBall`, SOC `SecondOrderCircuit`, LA `LiftAudit`.

Evidence levels:
- **kernel**: a landed identifier, file:line at L;
- **exact**: `r_checks.py` in this directory. It prints `OK -- 56 checks, 0 failed, 7 written notes`, and the replay
  is byte-identical (`rerun.out`). sha256 of the script `fff52b15…8ef8e0`, of the output `e55cf6ac…dfc94`;
- **written**: an argument given here;
- **citation**: the literature.

No Lean was run.

***

## 0. Verdict

1. **Lower bound.**
   - Given DRIVE, d ≥ 3 follows without ELEM, but with one hidden premise: **BOUNDEDNESS** of the body.
   - d ≠ 0 is kernel. d ≠ 1 is written + exact for every body, and kernel only for `Icc(−1,1)`.
   - d ≠ 2 (B6) is written and needs Ω bounded.
   - The whole plane ℝ² carries an `ElementaryDrivability`, which is an exact countermodel to unbounded B6.
   - For Ω∞, boundedness comes from the [0,1]-valued coordinates (P1b), not from the drive.
2. **Upper bound.** Of the five candidate families asked about:
   - (a) one-bit, (b) Hardy, (d1–d4) the purely group-theoretic principles and (e) substratum counting all
     **fail**: each is either satisfied by d-balls with d ≠ 3, or imports ℂ, or restates DIM3;
   - (c) Masanes–Müller is non-circular only on route B, and it is composite.
   - **One plausible non-circular single-system statement exists:** boundary transitivity (TRANS) + **energy
     observability** (EO, the dynamical correspondence: generators of the reversible dynamics are observables,
     equivariantly), together with DRIVE (used only to make the generator algebra nonzero), compactness and FR,
     give **d = 3**.
   - Written proof in §3; every hypothesis is shown independent by an exact or kernel countermodel (§4).
   - It uses no composite, no NB-1, no LT and no ball (the ball is derived), and does not take DIM3 as a premise.
3. **What that statement is, under maximum skepticism.**
   - Given DRIVE, {TRANS, EO} is *equivalent* to DIM3 at the elementary level (§5.1). It is a structural
     reformulation, not a weakening.
   - Its gain is that EO is true for every complex-QM system and false for real QM, quaternionic QM and every spin
     factor except d = 3. DIM3, by contrast, is false unscoped.
   - EO is the single-system fingerprint of ℂ (Alfsen–Shultz; Barnum–Müller–Ududec 2014). It is field-neutral in
     statement, but it is where ℂ enters.
   - Its only corpus shadow is the landed gate flow `unit g t = exp(iπt·proj g)` (SOC:356), whose generator is π
     times a sharp effect. So EO's source is the same open object as DRIVE's.
4. **Necessity (NEW for the corpus).**
   - No single-system principle that every spin-factor ball satisfies can source DIM3. B^d with O(d), d ≥ 4,
     satisfies every landed single-system item: DRIVE, TRANS (kernel `boundaryTransitive_ball4`), SharpSeed,
     PreservesBody, (SEC)/KInf1 with full effects, a self-dual cone, and capacity 2.
   - The **minimal missing ingredient** is therefore a principle that spin factors with d ≠ 3 violate. EO is the
     known single-system one. LT plus an entangling interaction (NB-1, MMAP) is the composite one.
5. **NB-1 circularity: confirmed and refined.**
   - Taking DIM3 from NB-1 is circular on route A: NB-1's input is a d-ball with a full self-dual cone, which the
     chain supplies only through DIM3 → ball3 → T0.
   - It is non-circular on route B (TRANS supplies the ball in every d), but composite.
6. **Recommendation: keep as research; no formal round now** (§7). A round would certify a reformulation of
   equal strength whose new premise (EO) is unsourced and coupled to DRIVE, and the decisive step needs Lie
   structure theory that the kernel lacks. Optional cheap pieces are listed in §7.

Classification:
- **NEW**: the B6 boundedness premise; the necessity statement (item 4); the TRANS + EO theorem with an independence
  audit; the Lie-level reading of EO (full-group EO would exclude the qubit); and the countercontrols Sp(1)/B⁴ and
  spin-2/B⁵.
- **CONFIRMING**: the NB-1 circularity (route-relative).
- **ELABORATING**: Hardy in binary scope.

***

## 1. The lower bound (question 1)

| d | status | evidence | hidden premises |
| --- | --- | --- | --- |
| 0 | excluded | kernel `not_drivable_singleton` KF:564 (any V) | none |
| 1 | excluded for **every** body, bounded or not | kernel only for `Icc(−1,1) ⊂ ℝ`: `not_drivable_Icc` KF:529. General case written + exact A1: the flow preserves aff Ω (`affineSpan_preserved` ON:436, kernel); h = flow(t₀/2) has slope a on the line; N = h² has slope a² > 0; every real solution of N∘N = id has N = id. Kernel alternative for compact segments: `isEmpty_drivability_of_finite_orbits` ON:124, once "segment orbits have ≤ 2 points" is proved (cheap, written) | none (no continuity needed) |
| 2 | excluded **for bounded bodies** (B6) | written. Either Aut is finite (B5), or the restricted automorphism group is compact, so the flow lies in SO(2) and J ∈ O(2), so J R J⁻¹ = R^{±1} (exact A3a–b) and D9 fails | **BOUNDED**. Exact A2: Ω = ℝ² with flow R(t), t₀ = π, N = −I and J = shear has J R(π/2) J⁻¹ = [[1,−2],[1,−1]], which is not orthogonal, so D9 holds and ℝ² is drivable. Convexity and continuity are not used |

So DRIVE + BOUNDED gives d ≥ 3. ELEM plays no role in the lower bound.

On the EO route (§3), d = 2 is excluded a second time and independently of B6: EO forces d to be odd.

## 2. Upper-bound candidates (question 2)

| candidate | uses composites? | presupposes the ball? | in corpus? | true for the qubit? | which d it excludes | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| (a) one bit / capacity (Brukner–Zeilinger, Dakić–Brukner) | the capacity clause: no. The "equal capacity ⇒ equivalent" and locality clauses: yes | no | no (grep) | yes | **none among balls**. Capacity ≤ 2 for every centrally symmetric body (kernel `card_le_two_of_centrallySymmetric` KF:632). The B–Z total information over d axes is \|x\|² for every d (exact I1). "Three complementary questions" restates d = 3 | fails |
| (b) Hardy K = N^r + Simplicity | yes: K_AB = K_A·K_B is LT, a K2-level premise and K1's LT row. Not a loop, but it puts DIM3 behind composite premises | no | Hardy cited (Main.md:352), not used | yes | binary scope: none, since K(2ⁿ) = (d+1)ⁿ for every d (exact I2). With N = 3 systems (outside ELEM) and the subspace axiom, d + 1 = 2^r, so d ∈ {3, 7, 15, …}. Only Simplicity picks 3, and given `ball3_drivable` KF:490 + §1, "minimal drivable dimension" ⇔ DIM3 | fails (restatement) |
| (c) Masanes–Müller 2011 / MMAP 2013 (LT + continuous reversible entangling interaction) | yes | yes (d-ball via transitivity) | MM cited; continuous transitivity and LT named as endpoint hypotheses (Main.md:352) | yes | all d ≠ 3 among balls | non-circular only on route B; same family as NB-1; not single-system |
| (d1) minimal generator algebra (dim 3) | no | no | no | yes | not 4: B1, Sp(1) drive on B⁴, transitive, algebra dim 3. Not 5: B2, SO(3) spin-2 drive on B⁵, irreducible, algebra dim 3, seed orbit spans ℝ⁵ | fails |
| (d2) TRANS alone | no | no | yes: OG's K∞-R, `BoundaryTransitive` OG:79 | yes (for the elementary body only; false for the qutrit) | none ≥ 4: kernel `boundaryTransitive_ball4` ON:735 with `finrank_E4` ON:744; exact B1 for a *drive* | fails |
| (d3) STAT: each drive flow fixes a pure state | no | no | no | yes (spectral theorem) | excludes B1 (exact B1k); not B⁴ with SO(4), not B⁵ with SO(5) | fails alone |
| (d4) dim G = d, or 1-dim stabilizer | no | no | no | yes | not 4: U(2) on B⁴, with an even equivariant direction → flow map (exact U1–U3) | fails |
| **(d5) TRANS + EO** | **no** | **no** (derived) | **no** (grep: no energy observability or dynamical correspondence anywhere) | **yes** (hat map, exact H1, E) | **every d ≠ 3** (theorem §3; exact E: so(2)/ℝ², sp(1)/ℝ⁴, u(2)/ℝ⁴, so(4), so(5), so(7), spin-2/ℝ⁵ admit no injective intertwiner; G2, Spin(7), Spin(9), SU(n), Sp(n) by dimension count) | **works** (§3–§5) |
| (e) binary alphabet + rank count | no | no | phases: `phaseOperator_supplied` SC:333 (ℂ) | yes | the count d = 1 + dim_ℝ 𝔽 gives 3 only with ℂ phases or the ℂ gate flow (LA:47). A spatial-SO(3) variant (Müller–Masanes 2013) needs a continuous rotation group, which on the cubic lattice is emergent | imports ℂ / Step-5 interface; BORDERLINE |

## 3. The candidate theorem (deliverable 9a)

### 3.1 Statement, typed against the landed vocabulary

Landed objects:
- `KInfFoundations.ElementaryDrivability` KF:264;
- `OrbitGeneration.BoundaryTransitive` OG:79 and `PreservesBody`;
- `OrbitNormalization.words` ON:53.

New definitions are marked †. None exists at L.

```lean
-- † the drive's word group (already expressible): G_D := words (Set.range D.flow ∪ {D.J})
-- † dir Ω := (affineSpan ℝ Ω).direction, with the restriction of G_D to aff Ω (ON §D gives the chart)
-- † genAlg Ω G : LieSubalgebra ℝ (Module.End ℝ (dir Ω))
--     := {A | ∀ t, exp (t • A) ∈ closure (linear parts of G restricted to aff Ω)}
-- † Obs Ω := Module.Dual ℝ (dir Ω)        -- affine functionals on aff Ω modulo constants
-- † EnergyObservable Ω G : Prop :=
--     ∃ φ : genAlg Ω G →ₗ[ℝ] Obs Ω, Function.Injective φ ∧
--       ∀ X Y, φ ⁅X, Y⁆ = - (φ Y).comp X      -- Lie-module map: X acts on Obs by ℓ ↦ −ℓ∘X

theorem dim3_of_transitive_energyObservable
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {Ω : Set V}
    (hconv : Convex ℝ Ω) (hcomp : IsCompact Ω)                                  -- BOUNDED/compact
    (hFR : FiniteDimensional ℝ (affineSpan ℝ Ω).direction)                      -- FR
    (D : KInfFoundations.ElementaryDrivability Ω)                               -- DRIVE
    (hK : OrbitGeneration.BoundaryTransitive Ω
            (OrbitNormalization.words (Set.range D.flow ∪ {D.J})))               -- TRANS = K∞-R
    (hEO : EnergyObservable Ω
            (OrbitNormalization.words (Set.range D.flow ∪ {D.J}))) :            -- EO
    Module.finrank ℝ (affineSpan ℝ Ω).direction = 3
```

Corollary, by `seedOrbit_eq_of_normalization` ON:307 and `orbit_generation_core` OG:715: Ω is an ellipsoid. The
normalization T carries Ω onto `ball3`. With P1 (`SharpSeed`) and V4′, the seed orbit is the directional family,
which is T0.

Named hypotheses:
- BOUNDED/compact and convex;
- FR;
- DRIVE;
- TRANS (K∞-R) for the drive's own word group;
- EO for the same group.

PreservesBody for the words is not a hypothesis: it is kernel (`preservesBody_driveWords` ON:107).

### 3.2 Proof (written; standard Lie theory cited)

Let Ḡ be the closure of the restricted word group in Aff(aff Ω), and 𝔤 its Lie algebra.

1. **Restrict and average.** The words preserve aff Ω (`affineSpan_preserved` ON:436, kernel). Since Ω is compact
   with nonempty relative interior, Ḡ is a compact Lie group (closed-subgroup theorem, citation). Ḡ fixes the
   centroid; Haar-average an inner product. Then Ḡ ⊆ O(d).
2. **Ball.** TRANS puts every boundary state on one Ḡ-orbit, so on one sphere about the centroid. Lemma B
   (`eq_closedBall_of_frontier_subset_sphere` KF:770, kernel; relative frontier = `IsBoundaryState` set, written)
   gives Ω = ball, so ∂Ω = S^{d−1}.
3. **d ≥ 2 and 𝔤 ≠ 0.** DRIVE (D3 + D6) gives a continuous one-parameter subgroup of Ḡ that is nontrivial on Ω, so
   𝔤 ≠ 0. If d = 1, Ḡ ⊆ O(1) is finite, a contradiction. Ḡ⁰ is transitive on the connected S^{d−1} (citation).
4. **Irreducibility.** A nonzero Ḡ⁰-invariant subspace W contains a unit vector, hence its orbit S^{d−1}, so
   W = ℝ^d.
5. **EO gives 𝔤 ≅ ℝ^d.**
   - φ(𝔤) is a nonzero 𝔤-invariant (hence Ḡ⁰-invariant) subspace of Obs ≅ ℝ^d (identified via the invariant inner
     product), so φ is a bijection.
   - Let ψ = φ⁻¹ : ℝ^d → 𝔤, an equivariant linear isomorphism. Set u × v := ψ(u)v.
   - Equivariance gives [ψ(u), ψ(v)] = ψ(u × v). So (ℝ^d, ×) is a Lie algebra isomorphic to 𝔤, with invariant
     inner product and ad_u = ψ(u) ∈ so(d).
6. **Centralizers are lines.**
   - By transitivity, X ↦ Xu maps 𝔤 onto u^⊥, so the stabilizer algebra has dimension d − (d−1) = 1.
   - By equivariance, Xu = 0 ⇔ [X, ψ(u)] = 0, so ker ad_u = ℝu for every u ≠ 0.
7. **d is odd (elementary).** ad_u is skew with a 1-dimensional kernel, so its rank d − 1 is even.
8. **d = 3.**
   - A compact Lie algebra in which every nonzero element has a 1-dimensional centralizer has rank 1, since a maximal
     abelian subalgebra is the centralizer of a regular element.
   - Compact rank-1 Lie algebras are ℝ and su(2) (citation: maximal-torus theorem and the rank-1 classification;
     Bröcker–tom Dieck, Knapp). It is not ℝ, since d ≥ 2.
   - Hence 𝔤 ≅ su(2) and d = dim 𝔤 = 3.
   - Cheaper partial route: in step 7, the eigenplane P of ad_u satisfies [P, P] ⊆ ker ad_u = ℝu, so ℝu ⊕ P ≅ su(2)
     is a subalgebra. Excluding a complement then still needs the structure theory.

Steps 1–7 are elementary: linear algebra plus Haar averaging. Step 8 is the costly citation. The proof also
identifies ψ(u) as "the generator measured by the sharp directional effect (1 + u·x)/2", which is the T0 family.

## 4. Countermodel and circularity audit (deliverable 9c)

### 4.1 Each hypothesis dropped

| hypothesis dropped | countermodel (all others hold) | d | evidence |
| --- | --- | --- | --- |
| DRIVE (𝔤 ≠ 0) | segment [−1,1], G = {id, flip}: TRANS holds, EO holds vacuously (𝔤 = 0) | 1 | DRIVE fails there by kernel `not_drivable_Icc` KF:529; TRANS and EO written |
| TRANS | (i) B⁴ with the SO(3)⊕1 drive: EO holds (injective intertwiner, exact E), TRANS fails (x₄ invariant, B3). (ii) Cone over B³, and B³ × [−1,1]: same algebra. (iii) B³ × B³ with SO(3)²: EO holds (exact E). (iv) The qutrit: EO holds (exact E, su(3) on Herm0(3)); TRANS fails (K 5.01, M X1) | 4, 4, 6, 8 | exact + written |
| EO | (i) B⁴ with the Sp(1) drive: DRIVE and TRANS hold (exact B1a–j); no intertwiner (E). (ii) B⁴ with isom4: TRANS kernel (ON:735); SO(4) has no intertwiner (E). (iii) The quaternionic bit B⁵ with SO(5) (E). (iv) B⁷ with SO(7) or G2 (E, count) | 4, 4, 5, 7 | kernel + exact |
| the *same* G for TRANS and EO | B⁴: TRANS for isom4 (kernel) and EO for the SO(3)⊕1 drive words (exact E) | 4 | kernel + exact |
| linearity of EO (only an equivariant sharp-direction → flow map) | U(2) on B⁴: A_u = i(1 − \|u⟩⟨u\|) is equivariant, fixes u and is nonzero, but A_{−u} = A_u (exact U1–U3); u(2) → ℝ⁴ has no intertwiner (E) | 4 | exact |
| Lie-level equivariance (EO stated for the full group instead) | **wrong-way failure**: an improper J satisfies D9 (exact H3), and an improper g has g·hat(v)·gᵀ = −hat(gv) (exact H2). So full-group EO would exclude the qubit (d = 3). EO must be read on 𝔤 / Ḡ⁰ | 3 | exact |
| compactness / BOUNDED | not needed as a separate countermodel on this route, though step 1 uses it. For B6 alone: ℝ² is drivable (exact A2) | 2 | exact |
| FR | none found. The Hilbert ball fails EO, since so(H) ≇ H. Kept as a named hypothesis because the proof uses it | — | written |

### 4.2 Non-circularity

- **Nothing is taken from NB-1.** NB-1's objects are absent: no composite, no CNOT G, no copy covariance, no LT, no
  maximal tensor cone. `nb1_kernel_core` NGB:255 and `blocks_vanish` NGB:149 are not used.
- **Nothing is taken from DIM3 or the ball.** The ball is derived in step 2 from TRANS + averaging. `ball3` enters
  only after the conclusion, through the normalization ON:307.
- **Nothing is taken from K2 / composites**, and no ℂ object is used: no `gateFlow`, no `phaseOperator`.
- **DRIVE is not taken from `elementaryDrivability_of_substratum`.** It stays a named open premise, as in M's E1.
  Its matrix shadow is refuted for the current substratum (`substratumTheory_not_layerFlowExecutable` LA:200;
  `substratum_residual` SC:383).
- **Position on the T0 → T1 chain.** The theorem replaces row K2b (DIM3) of M's route A *before* T0:

  ```
  ELEM ⇒ TRANS(G_D)  ┐
  DRIVE ─────────────┼→ [§3] d = 3 → ellipsoid → NORM (ON:307, kernel) → ORB (OG:348) ─┐
  EO(G_D) ───────────┘                                                                 ├→ T0 → lorentz_of_effects NGB:105
  P1 (SC∞) + V4′ ──────────────────────────────────────────────────────────────────────┘
  T0 + NB-H + CC + N-ALIGN + K2/LT  →  T1 (K1, d ∈ {1,3}): now a consistency check, not a dimension source
  ```

- **The NB-1 loop re-verified.**
  - NB-1's hypotheses are "two locally tomographic d-balls with full self-dual cones … native CNOT" (NGB header
    lines 4–9; NB-1 `result.md`).
  - On route A the d-ball input is T0, which needs DIM3: a loop.
  - For d ≥ 4 a drive alone does not deliver it (B⁴ with SO(3)⊕1: the orbit misses x₄; spin-2 B⁵: not transitive).
  - Hence: circular on route A; non-circular on route B (TRANS ⇒ ball_d), but composite.

## 5. Skeptical assessment of the favourable branch

1. **Equivalence, not weakening.**
   - DRIVE + DIM3 ⇒ TRANS(G_D) (K §2, written) and EO(G_D) (hat map, exact H1; Ḡ_D⁰ = SO(3)). With §3, given DRIVE +
     compact + FR, **{TRANS, EO} ⇔ DIM3**.
   - The premise count of route A changes from {SC∞, DRIVE, **DIM3**, V4′} + ELEM to {SC∞, DRIVE, **EO**, V4′} +
     ELEM. Here ELEM's dimension-relevant content is exactly TRANS, which the qutrit violates.
   - That gives ELEM, currently undefined, a precise and testable formal content for the dimension question:
     **ELEM ⊇ K∞-R**.
2. **What is gained.**
   - EO is not ELEM-scoped. It holds for every complex-QM system (exact su(3)/Herm0(3); generally u(n) ≅
     i·Herm(n)).
   - It fails for:
     - the rebit (so(2)/ℝ²);
     - the real qutrit (so(3) on Sym0(3), exact E; this is B2's action);
     - the quaternionic bit (so(5)/ℝ⁵);
     - every spin factor except d = 3.
   - That is an independent postdiction beyond the problem the premise was built for, as §A.29 requires.
   - DIM3 has no such content and is false unscoped (qutrit d = 8).
3. **ℂ in disguise.** Within Jordan algebras, a dynamical correspondence exists iff the algebra is the self-adjoint
   part of a C*-algebra (Alfsen–Shultz). Barnum–Müller–Ududec (NJP 16, 123029, 2014) derive complex QM from
   single-system postulates, with energy observability as the clause that removes real, quaternionic and spin-factor
   theories.
   - So EO does not *derive* ℂ from nothing. It is the field-neutral statement through which ℂ enters.
   - Whether that satisfies P1 ("complex kinematics in the conclusion") in spirit is the owner's call. In letter it
     does: no ℂ appears in the statement.
4. **Sourcing.**
   - The landed matrix drive is literally EO-shaped: `unit g t = 1 + (e^{iπt} − 1)·proj g` (SOC:356), with
     `proj g = (1 − g)/2` a projection (SOC:352, `proj_mul_proj` SOC:361); `gateFlow σ t = unit (permMat σ) t`
     (LA:47).
   - Its generator is π times a sharp effect.
   - EO's field-neutral source is therefore the same open object as DRIVE's: the non-integer-time gate flow, plus
     linearity and equivariance of generator ↦ effect.
   - **EO is OPEN, and not independently sourceable from anything landed.**
5. **Necessity of an EO-like ingredient (NEW).**
   - The spin-factor balls B^d with O(d), d ≥ 4, satisfy every single-system item in the landed vocabulary:
     - DRIVE (exact B1, or SO(3)⊕1);
     - TRANS (kernel ON:735);
     - SharpSeed and PreservesBody (kernel ON:721 for ball4);
     - (SEC)/KInf1 with full effects (written: the d-ball analogue of `kInf1_ball3_full`);
     - the full self-dual (Lorentz) cone;
     - capacity 2 (kernel KF:632).
   - They also satisfy BMU's other postulates (citation).
   - So **no principle that every spin factor satisfies can source DIM3**. The minimal missing ingredient must be
     violated by spin factors with d ≠ 3.
   - Two kinds are known: single-system EO / dynamical correspondence, and composite LT + entangling reversible
     interaction (NB-1, MMAP). Nothing else is on record.

## 6. Countermodel bank (question 3)

"✓" = holds, "✗" = fails. Every row is drivable except the rebit, which fails D9 by B6.

| model | d | DRIVE | TRANS(G_D) | minimal alg. | STAT | EO | excluded by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rebit disk | 2 | ✗ (B6, bounded; A3) | — | — | — | ✗ (E) | DRIVE; EO; parity |
| qubit ball3 | 3 | ✓ (kernel `ball3_drivable`) | ✓ (kernel ON:667) | ✓ | ✓ | ✓ (H1, E) | — |
| B⁴, SO(3)⊕1 | 4 | ✓ | ✗ (B3) | ✓ | ✓ | ✓ (E) | TRANS |
| B⁴, Sp(1) left | 4 | ✓ (B1a–h) | ✓ (B1j) | ✓ (B1i) | ✗ (B1k) | ✗ (E) | EO; STAT |
| B⁴, U(2) / SO(4) | 4 | ✓ (written) | ✓ | ✗ | ✓ | ✗ (E) | EO |
| quaternionic bit B⁵, SO(5) | 5 | ✓ (written) | ✓ | ✗ | ✓ | ✗ (E) | EO |
| B⁵, SO(3) spin-2 | 5 | ✓ (B2a–e) | ✗ (B2h) | ✓ (B2g) | ✓ | ✗ (E) | TRANS; EO |
| B⁷, SO(7) or G2 | 7 | ✓ (written) | ✓ | ✗ | ✓ | ✗ (E, count) | EO |
| B³ × B³, cone over B³ | 6, 4 | ✓ (K, written) | ✗ | — | ✓ | ✓ (E) | TRANS |
| qutrit body | 8 | ✓ (written) | ✗ (K, M) | ✗ | ✓ | ✓ (E) | TRANS (ELEM) |
| ℝ² (unbounded) | 2 | ✓ (A2) | vacuous | — | ✓ | — | BOUNDED |

Every d-ball also passes the one-bit principle (I1; Lemma D) and Hardy counting in binary scope (I2).

## 7. Recommendation

**Keep as research. Do not open a formal round now.** The owner's condition is met in the weak sense: a plausible
non-circular single-system statement exists (§3). But a round would not reduce the open set:
- it trades DIM3 for EO, which is equivalent given DRIVE;
- EO is unsourced, and its only shadow is the same gate flow that DRIVE's sourcing is stuck on;
- step 8 needs compact Lie structure theory (closed-subgroup theorem, maximal tori, rank-1 classification) that
  Mathlib does not provide in usable form.

If the owner wants a cheap, premise-free round anyway, the kernel-cheap pieces are:
1. **Countercontrols:**
   - the Sp(1) drive on B⁴ (`ElementaryDrivability`; transitive words; no stationary state);
   - the spin-2 drive on B⁵;
   - the ℝ² drive, as the boundedness control for B6;
   - optionally U(2).
2. **The elementary layer of §3, steps 4–7:** an injective intertwiner into an irreducible module is bijective, and a
   skew map with a 1-dimensional kernel forces d odd.
3. **The qubit instance:** EO for `ball3Drive` words via the hat map, i.e. the "reverse" direction.
4. **The general segment exclusion**, via ON:124, and B6 with BOUNDED as an explicit hypothesis.

For an owner decision, not edits made here:
- Record EO as the named structural reformulation of DIM3, and ELEM ⊇ K∞-R as ELEM's dimension content.
- Record that DIM3 cannot come from any principle the spin factors satisfy.
- Record that B6 carries a boundedness premise.

## Files

- `r_checks.py`: exact checks (A, B, E, H, U, I series).
- `r_checks.out`, `rerun.out`: identical outputs, 56 checks.
- `NOTES.md`: node-by-node log, the identifiers re-verified at L with file:line, and the corpus grep.
