# Premise ledger (off-repo, read-only; corpus at base 0f2687b7)

Corpus read from `scratchpad/base0f/` (`git archive 0f2687b7 papers book`; every paper diffed equal to
`git show 0f2687b7:<path>`). Line anchors are to that tree. Built dependency-first, starting from A5.

**Fields per entry.** Exact statement · descriptive level (SUBSTRATE / INTERFACE (G) / R4 / Q) · status
(definitional / posit / sharpened stipulation / theorem / probed) · direct consumers · transitive consumers ·
coexisting (uses nearby structure, not the premise) · evidence status of each dependence · interface dependence ·
controls affected · relation to QM · circularity risk · replacement obligation per direct consumer · corpus drift ·
open checks · **representation vs physical-identification use** (added after L-A5 froze, from L-A2: does the consumer
need only the *existence* of a representation with the property, or does it assert the property of the *actual*
substrate? Retro-reading of L-A5: D4 is a realization claim about a chosen representative; the observer route is
representation-level).

**Consumer classes.** *Direct*: the result's own proof uses the premise or its stated equivalent. *Transitive*: it
uses the premise only through a direct consumer. *Coexisting*: it is stated for, or illustrated on, the linear
realization but its proof does not use linearity. *Verified* = the proof or statement text was read and the use
located; *declared* = the corpus asserts the dependence and the proof was not read here.

***

## L-A5 — Linearity of the substratum update — CLOSED and FROZEN 2026-10-03 (source graph; drift R1–R5 held for a future propagation round)

**Exact statement.** "(A5) **Linearity.** The wave equation for φ is linear." (Substratum.md:100), with: equivalent
to amplitude-scale gauge invariance via the linearity-equivalence lemma of [SM §4.1]; "necessary *given*" that gauge
principle. Formal content (SM.md:224): over ℤ/qℤ, f(a + a′) = f(a) + f(a′) for the neighbour function f of the
second-order update x_i(t+1) = f(neighbours at t) − x_i(t−1).

**Level.** SUBSTRATE. **Status.** Posit, held as a sharpened stipulation (Substratum.md:266–268): the irreducible
assumption is "the alphabet's additive automorphisms x ↦ λx + c are gauge" (amplitude-scale gauge), from which
linearity follows by a certified elementary lemma. Main.md:706 posit-ledger item (vii).

**Two roles of the realized dynamics (SM.md:292).** The exact rule is linear over ℤ/qℤ; the realized bijection
carries a bounded threshold/rounding nonlinearity, measured chaotic (Main.md:480). The *structural chain* reads only
the linear part; the *ergodic/measure* properties (full-shell Gaussianization, the mixing behind operational
measurement independence in Main §3.3, the ETH-conditioning of C2 necessity in Main §3.4) read the nonlinear part.
Track I's QM side therefore already consumes bounded substrate nonlinearity; A5 holds exactly only at the structural
level.

### The central structural finding: two routes to the wave operator

The corpus contains **two** routes to the lattice wave operator, and only one consumes A5.

- **Substrate route (A5-direct).** Form lemma (SM.md:220–224): center-free + cubic-isotropic + *linear* second-order
  NN rule ⇒ x_i(t+1) = α Σ_{j∼i} x_j(t) − x_i(t−1). Used by Substratum Stage 2(b) (Substratum.md:158) for the
  reconstruction theorem's wave-equation step.
- **Observer route (A5-free as stated).** Theorem 1a (SM.md:238): the projected evolution of the Koopman operator of
  *any* bijection φ under a linear observer projection, with symmetry-equivariant memory kernels (Mori–Zwanzig form;
  linearity of U is automatic for every bijection). Lemma 1c (SM.md:248): canonical projection, memory-resummed
  Schur complement, observer dispersion as the zero set of 𝒟(λ). Corollary 1a: O_h equivariance forbids quadratic
  anisotropy (Lean: `OIBridge/CubicIsotropy.lean`). Corollary 1b (SM.md:266): a scalar, translation-invariant,
  NN-local, O_h-equivariant, constant-preserving observer Markov part is p₀f + pΣ…; with observer-level center
  freedom, T = A/(2d). **Theorem 1** (SM.md:274): *if* the scalar observer branch satisfies Corollary 1b and a
  reversible second-order temporal update, the normalized lattice Klein–Gordon branch follows.
  None of these use substrate linearity. Their hypotheses (H-T1: Corollary 1b's kernel conditions, observer-level
  center freedom, reversible second-order temporal update) are conditions on the projected observer kernel, and
  their derivation from φ is the open map φ → L_obs → Δ_g (SM.md:228: "not proved anywhere in this framework").

The SM §4 chain is stated on the observer route ("on the observer-level lattice-wave branch of Theorem 1",
SM.md:282), while the Substratum reconstruction cites the substrate route. A5's role in the wave-operator step is
therefore: *sufficient on the substrate route, not used on the observer route, where its job is taken by H-T1.*

### Direct consumers (verified)

| # | Consumer | Anchor | Linear structure needed | Track |
|---|---|---|---|---|
| D1 | Form lemma (substrate route to the wave operator); Substratum Stage 2(b) | SM.md:220–224; Substratum.md:158 | additivity of f over ℤ/qℤ | SM / reconstruction |
| D2 | Amplitude-scale U(1)-phase stripping, U(3)×U(2)×U(1) → SU(3)×SU(2)×U(1) | Substratum.md:162, :264; book ch05:47, :127–133 | the A5-equivalent principle itself, not additivity | SM / gauge |
| D3 | Stationary Gaussian measure "on linear dynamics with energy conservation"; two-point function [□_lat⁻¹]; pseudofermion covariance match | SM.md:288 | linear dynamics + energy conservation (ergodicity from the nonlinear part) | SM measure ↔ lattice MC |
| D4 | Coherence cluster of Main §3.2: for the F₂-linear NN update u′ = Σ_{z∼x} u_z + v, v′ = u, Lemma 2 (channel normal form Φ = Ad_{V_A} ∘ Φ_G, Clifford-conjugated abelian Weyl mixture), Corollary 1 (non-EB iff w < κ), Corollary 2 (non-EB if min(\|∂⁻R\|,\|∂⁺R\|) < \|R\|), cubic-block Remark | Main.md:288–318 | F₂-linearity (block matrices A, B, C; character sums over im B) | QM side — realization-specific |
| D5 | §4.4 multi-component update: "the general second-order **linear** update" φ(n,t+1) = Cφ + Σ_j M^{(j)}[…] + Dφ(t−1), with C = 0, D = −I, M^{(j)} = M ⇒ the internal-matrix branch | SM.md:306–310 | linearity of the K-component update (matrix parametrization) | SM / gauge — **level-ambiguous** (stated on (ℤ/qℤ)^K, then placed on the observer branch; "not identified with the fundamental finite bijection without the coarse-graining bridge") |
| D6 | Class filter: OI class membership requires A1–A6; matrix models excluded at A5 | Structure.md:136, :295–332 | A5 as a predicate | comparison |

### Transitive consumers

- **Through the wave operator (D1 on the substrate route, or Theorem 1 / H-T1 on the observer route):**
  Theorem 2 Susskind factorization (SM.md:282, stated on Theorem 1's branch — an operator identity on □_lat);
  dispersion results, 4/45 coefficient, emergent-Lorentz argument (§4.1 scope, SM.md:228); Theorem 3 (CI ⇔ exact
  chiral symmetry); staggered tastes, Theorems 8–11, 8b ("normalized wave equation"); Theorems 12–13 (grading,
  chirality); Theorem 17 (T-invariance of the wave equation) and §5 strong-CP; §6–§7 gauge coupling and quantitative
  predictions; Substratum Stage-2 uniqueness, Lemma 23.0, Theorem 23 (Substratum.md:144–192, which cite D1).
- **Through D5:** Theorem 4 (mass spectrum), Lemma 4a, Proposition 4b, Theorem 5 (condensate stabilizer), the
  commutant gauge group and Theorem 7b (Bravais uniqueness under the commutant construction).
- **Through D2:** the SU(N) reduction and everything stated on the Standard-Model group (hypercharges of Theorems
  14–15 take the group as given).
- **Through D3:** substratum ↔ pseudofermion measure equivalence; the lattice-MC reduction of SM §7.5.
- **Through D4:** nothing load-bearing. Main.md:320 states the boundary explicitly: coherence preservation "is a
  property of this realization, not an additional structural condition: (C1)–(C4) … neither contain nor imply a
  coherence requirement"; non-entanglement-breaking "is a statement about a single channel, not about quantum
  mechanics". The "coherence is a bulk quantity, decoherence an area quantity" link to the §7 horizon entropy is
  labelled "an interpretation of the one-step result, not a theorem" (Main.md:318). No later Main result cites
  Corollary 1 or 2 (grep of Main/SM/Substratum/GR/Structure/Methodology/Explainer).
- **Gravity (GR), by ladder level:**
  - **G1** (§3–§6: ħ, ε = 2l_p, area law, 1/4, cosmological-constant dissolution): **A5-free as declared**
    (GR.md:669–675; the proof is "the §3–§6 derivations themselves"; no theorem-style proof written). Declared, not
    verified line by line.
  - **G2** (weak-field, §8.7): **A5-transitive (through the wave operator).** "Equipartition is the equipartition
    *theorem* because the emergent boundary modes are harmonic (the [SM] wave equation)", and bond weights are fixed
    by "the framework's own dispersion relation" (GR.md:693–695).
  - **G3** (covariant field equations): open; no dependence to classify.
  - **G4** (cosmology, conditional on G3): the ν-magnitude remark uses the boundary measure dN/dω ∝ ω⁴ from "the
    half-space trace-out of the reconstruction-selected wave equation" (GR.md:551) — A5-transitive. The Page-curve
    proof (Appendix A.7, GR.md:825) uses energy conservation "(the wave equation is Hamiltonian)" — transitive *as
    written*, but needs only a Hamiltonian (energy-conserving) bijection; recorded as replaceable by any
    energy-conserving φ. §7.2–7.3 dark-sector results depend on OI's specific gap-equation solution ("Level D ×
    G1–G2", GR.md:677), hence inherit G2's A5-transitivity.

### Coexisting (checked; not A5 consumers)

- Main's representation layer, all stated for an arbitrary finite bijection on 𝒞_V × 𝒞_H: S ⇔ D ⇔ Q_fb, the
  finite-horizon stochastic–reversible–unitary equivalence, the characterization theorem, history readback and
  indivisibility, C3 necessity, process dilation, unavoidable hidden memory, canonical predictive quotient
  (Main.md:115, :137, :484, :496, :516, :526, :580, :598).
- Main's separability-threshold theorem (Main.md:308): general abelian Weyl subgroups; only its application
  (Corollary 1) is D4.
- Main's CP-indivisibility theorem and diagonal-preservation lemma (Main.md:322–326): any permutation unitary.
- Main's Lemma 1 boundary bound (Main.md:294): factorization over any ℤ_q; "in weakened form the support argument
  covers arbitrary nearest-neighbour bijections" (Main.md:320). Rank form uses a field; support form is A5-free.
- Main's Bell–lattice obstruction (Main.md:394): stated for "the nearest-neighbor cubic wave-equation update", but
  the argument is a light-cone/locality argument (NN range + maximum speed); uses A3/NN locality, not A5.
- SM Theorem 7 (6 = T₁ ⊕ E ⊕ A₁): pure representation theory of O on the six link directions ("unconditional").
- SM Theorem 1a, Lemma 1c, Corollaries 1a–1b, Theorem 1: observer route, above.

### Interface dependence

D4 concerns the passive single-step channel of a fixed partition. The RECORD linear control is the same update in
d = 1, q = 2 (v′ = v_{i−1} + v_{i+1} + u, u′ = v — Main's u′ = Σu + v, v′ = u with variables renamed), so D4's
Clifford/Weyl normal form is that control's passive-interface structure.

### Controls affected

RECORD's nonlinear and majority leap rules violate A5; the linear rule is an A5-type representative and the d = 1
instance of D4. RECORD's OVER-RANK exclusions concern those A5-violating dynamics under the tested interfaces only.

### Relation to QM — two notions of "quantum side"

- **Generic QM representation** (Main's equivalence and characterization theorems): A5-independent.
- **Realization-specific structure** (D4 coherence/Clifford–Weyl channel; and, through the wave operator, the
  SM-selection chain): A5-dependent.
A5 is, in the corpus, an SM-selecting and realization-specific premise, not a QM-representation premise.

### Circularity warnings

1. (Corpus, Substratum.md:266.) Deriving amplitude-scale gauge from the observer architecture is circular: a
   nonlinear F induces observable amplitude-dependent dispersion, so "absolute amplitude is unobservable" already
   presupposes linearity. No replacement may re-enter by this route.
2. (D4 → R4/Q.) D4's stabilizer (Clifford/Weyl) structure comes from an F₂-linear substrate. If it is used to
   motivate the target R4 or Q geometry, linear-substrate structure is being imported into an observer-level premise.
   Recorded as a warning, not a conclusion (RECORD's diamond and the held Level-3 prediction sit on this edge).
3. (Observer route.) H-T1 includes a "reversible second-order temporal update" at observer level. For a linear φ the
   projected recurrence is inherited (Lemma 1c(i): x_{t+2} = L x_{t+1} − x_t); for a nonlinear φ it is a genuine
   hypothesis. Using H-T1 as a premise while citing linear-φ examples as its evidence would be circular.

### Replacement obligations (if A5 is removed as a substrate posit)

| Direct consumer | Exact obligation at the interface |
|---|---|
| D1 | Discharged on the observer route *iff* H-T1 holds for the nonlinear φ: prove that the canonical projected observer kernel of φ (Lemma 1c) is scalar, translation invariant, NN-local, O_h-equivariant, constant-preserving, observer-center-free (Corollary 1b), and that the visible recurrence is reversible second order — i.e. the map φ → L_obs with L_obs = A/(2d); then L_obs → Δ_g at low momentum (Corollary 1a gives isotropy of any surviving quadratic term; nondegeneracy b_m ≠ 0 must be shown separately, SM.md:260). The substrate-route reconstruction (Substratum Stage 2(b)) would need restating on the observer route. |
| D2 | Amplitude-scale gauge as an observer-level redundancy of the emergent field (phase of each block unobservable), established without circularity warning 1. |
| D3 | Gaussianity of the relevant stationary measure, or of its observer-level marginals, for the nonlinear φ, with the covariance [□_lat⁻¹] up to normalization. |
| D4 | Either a non-EB theorem for the visible channel of a nonlinear NN update, or nothing: Main.md:320 already marks D4 as realization-specific and not load-bearing for the QM representation. Lemma 1's support form survives as is. |
| D5 | The K-component analogue of D1's observer-route obligation: the projected multi-component kernel has the internal-matrix form Σ_j M[…] with a single isotropic M, at observer level. Resolve D5's level ambiguity first. |
| D6 | None mathematical; a class boundary. Removing A5 redefines the class. |

### Classification (current evidence)

(ii) **weakenable, not yet shown removable.** The corpus already operates with "exact linear structural part +
bounded chaotic nonlinearity". Removal (iii) reduces to the D1/D5 observer-route obligation (H-T1 for nonlinear φ),
D2's non-circular observer-level amplitude gauge, and D3's Gaussianity. D4 needs nothing for the QM representation.

### Corpus drift found (record only; not a ledger classification input)

| # | Sites | Drift |
|---|---|---|
| R1 | Substratum.md:158; book ch02-substratum.md:98; book FULL.md:739 | "propagation speed v = α … α = 1 fixed by relativistic causality" vs SM.md:226–228 (the source): "α is neither the propagation speed nor free to be set to 1", α = 1 unstable for the d = 3 real lift, α = 1/d at observer level. Both papers last changed in 58100aea (2026-09-13); SM carries the revised scope. |
| R2 | Structure.md:301 vs Structure.md:219 and Substratum.md:268 | Structure.md:301 says the necessity argument "rests on q-gauge invariance ([SM §2.7])"; Structure.md:219 and Substratum.md:268 say it runs through amplitude-scale gauge and that q-size gauge does *not* entail it (the strong reading overshoots). Internal inconsistency within Structure. |
| R3 | book ch09-universality.md:205 | Restates A5 as "the framework's emergent dynamics is linear at the visible-sector level" — a different descriptive level (observer/visible) from Substratum's A5 (substrate update). A level-crossing restatement. |
| R4 | book ch02-substratum.md:84 | A5 stated without the amplitude-scale equivalence or its sharpened-stipulation status ("would require a separate derivation chain not developed here"); lags Substratum.md:100/266–268 (the equivalence appears in book ch05:47). |
| R5 | SM.md:306–310 (D5) | Level ambiguity: the multi-component linear update is written on (ℤ/qℤ)^K, then placed on the observer branch with the caveat that it is not identified with the fundamental bijection. |

These are manuscript-consistency items for a future §A.25 propagation round under owner direction; nothing in the
repository is changed here.

### Remaining open (not blocking the A5 graph)

- G1's A5-freedom is declared, with no theorem-style proof written (GR.md:675). A line-by-line check of GR §3–§6 for
  wave-equation inputs is a separate task.
- Whether the Substratum reconstruction theorem should cite the observer route instead of D1 is a manuscript question
  (R1 is its symptom), not a ledger one.

***

## Cross-entry note (after L-A5 froze)

L-A5's observer route is *conditional* on H-T1, and H-T1 is not proved for the corpus's own linear φ either:
SM.md:228 says the map φ → L_obs → Δ_g "is not proved anywhere in this framework", and Corollary 1b's observer-level
center freedom is "a theorem conditional on observer-level CI, while the descent of CI through the
substratum-to-observer map remains open" (SM.md:272). So the bridge target is "derive H-T1 from substrate dynamics"
for linear φ as much as for nonlinear φ; a linear φ only makes the projected second-order recurrence available
(Lemma 1c(i)). The nonlinear case is not a harder version of a solved problem.

***

## L-A2 — Determinism / bijectivity of the substratum map — CLOSED and FROZEN 2026-10-03 (checks 1–4 done below)

**Exact statement.** "(A2) **Determinism.** φ: S → S is a bijection (deterministic, reversible dynamics)."
(Substratum.md:94), with: two-part status per the dilemma argument of [Main §2.2] — a non-injective descent either
leaves a statistical trace (excluded by the observed unitarity of quantum dynamics) or none (then removable: every map
on a finite set restricts to a bijection on its eventual image, where all recurrent registered history lives). Main
Lemma 3 (Main.md:56): φ is a function (determinism) and, "as the reversible representative of §1.2", a bijection;
invariant measure uniform on each cycle; the counting measure selected globally as maximal-entropy ("a selection
principle, not uniqueness"). Main.md:62: "The bijective substratum is a representation choice — the minimal recurrent
bijective representative"; the characterization theorem "is accordingly conditional on finite reversible substratum
dynamics". Posit ledger item (iii) (Main.md:706): bijectivity is part-empirical (observed unitarity).

**Split into logically distinct sub-premises.**
- **A2a determinism** — φ is a function (one successor per state).
- **A2b injectivity** — distinct states have distinct successors; on a finite S, A2a + A2b ⇔ bijection.
- **A2c recurrence** — φ^N = id for some N. *Not a separate premise*: a consequence of A2a + A2b + A1 (finiteness).
  Kept as its own line because several consumers use only it.
- **A1 finiteness** — separate premise (its own entry); listed here only where a consumer needs it jointly.
- **Measure selection** — uniform on cycles (needs A2b) and maximal-entropy globally (posit item (iv)); separate.
- **Not A2: Koopman linearity.** f ↦ f ∘ φ is linear for *every* map φ. What A2b buys is that the Koopman/permutation
  operator U_φ|s⟩ = |φ(s)⟩ is **unitary** (a non-injective φ sends two basis vectors to one, so U_φ is not an
  isometry). A2 gets credit for unitarity, not for linearity.
- **Not A2: operational reversibility.** GR.md:230's "reversible richness" (available reversible transformations admit
  operational inverses; dynamical Lie algebra contains su) is a Q-layer operational premise of OI⁺, not substrate A2.
- **Not A2: observer-level reversibility in H-T1.** The "reversible second-order temporal update" hypothesis of SM
  Theorem 1 is an observer-level condition; projection of a bijection does not in general yield a reversible visible
  recurrence (Theorem 1a's memory kernels). Kept separate.

**Level.** SUBSTRATE (A2a, A2b, A2c).

**Status.** Posit, part-structural / part-empirical (Main.md:706 (iii); Substratum.md:94). The second-order "leap"
form x(t+1) = F(x(t)) − x(t−1) is bijective for **every** F (inverse: x(t−1) = F(x(t)) − x(t+1)), so A2 is
automatic for every second-order rule the SM chain considers, linear or not.

### The central structural finding: A2 is free at the law level

Main's finite-horizon equivalence (Main.md:526; Lean `finite_horizon_equivalence`, `S_imp_D`): (S) finite stochastic
laws = (D) visible marginals of finite reversible deterministic systems = (Q_fb) fixed-basis unitary Born
representations. Its proof: S ⇒ D *constructs* a bijection (response-table construction, §3.4); D ⇒ Q_fb uses the
bijection's permutation unitary U_φ (needs A2b); Q_fb ⇒ S is the Born rule. Consequently:
- **As a class equality of laws, the theorem does not assume A2 of nature.** Any finite visible law — whether it comes
  from a deterministic non-invertible, a stochastic, or a bijective substrate — is in S, hence has a reversible
  realization (D) and a fixed-basis unitary representation (Q_fb). Bijectivity appears in the *conclusion*
  (existence of a reversible representative), which is what Main.md:62 means by "representation choice".
- **A2 acquires physical content only through realization identification**: when the actual substrate is identified
  with a bijective representative, so that U_φ is the substrate's own dynamics (with U_φ = e^{−iĤ} a fixed autonomous
  generator at integer times), and when results are proved *about every* such representative or *about the actual*
  one (recurrence, microreversibility, measure).

### Direct consumers

| # | Consumer | Anchor | Uses | Evidence |
|---|---|---|---|---|
| B1 | D ⇒ Q_fb step: U_φ permutation unitary, diagonal preservation, integer-time generator | Main.md:528; Lean `permMatrix_mem_unitaryGroup`, `isDiag_Phi` | A2b | verified |
| B2 | P-indivisibility of the uniform-prior marginal when T is not a permutation | Main.md:115–131, Step 1 "φ bijective on a finite set ⇒ ∃N: φ^N = id" | A2c (+A1) | verified |
| B3 | History readback + finite recurrence ⇒ global indivisibility on the fixed finite reversible representative | Main.md:137–142 ("φ is a permutation of a finite set, it has finite order L") | A2c (+A1) | verified |
| B4 | Measure on orbits: invariant measure uniform on each cycle (Lemma 3) | Main.md:56 | A2b | verified (statement) |
| B5 | Uniform-prior one-step marginal is doubly stochastic (Birkhoff–von Neumann) — used by the dilemma argument and by C2 necessity's model | Main.md:62, :433 | A2b + uniform prior | declared (lemma in §3.2, proof not re-read) |
| B6 | CP-indivisibility of the permutation-dilation family; diagonal-preservation lemma | Main.md:322–326 | A2b (permutation unitary) | verified |
| B7 | Classical half of the ħ calibration: microreversibility Θφ Θ = φ⁻¹ gives N_ij = N_ji and the thermal rate ratio β_E "from finite deterministic reversible counting" | GR.md:68–70 | A2b + T-invariance | verified |
| B8 | Page curve (A.7): φ restricted to an energy shell decomposes into cycles; exact cycle time averages | GR.md:825 | A2b + A1 + energy conservation | verified |
| B9 | Induced-dynamics characterization of OI_Q: substratum-induced dynamics ⊊ locality-preserving automorphisms (phase unitary induced by no reversible finite-range bijection) | GR.md:286; Lean `phase_localityPreserving`, `phaseQ_ne_heisQ` | A2b (+A3) | declared |
| B10 | Class filter: matrix models fail A2; LQG, causal sets, asymptotic safety fail A2 (quantum/stochastic substrata) | Structure.md:136, :1039 | A2 as predicate | verified |

### Consumers of determinism only (A2a), not injectivity

- Unavoidable hidden predictive memory (Main.md:580; Lean `OIBridge/HiddenMemory.lean`): hypothesis says "a bijection",
  but the proof uses only "Determinism makes X_{t+1} a function of (X_t, H_t)" — verified; injectivity unused.
- Canonical predictive quotient, universality clause (Main.md:598): "every faithful deterministic realization" —
  determinism (statement); the existence clause *constructs* a bijective realization (A2 in the conclusion).

### Not consumers (A2 in the conclusion, or unused)

- S ⇒ D (Main.md:528), finite-horizon process dilation (Main.md:496), intervention dilation (Main.md:460): they
  *construct* reversible realizations.
- Q_fb ⇒ S (Born rule).
- Lemma 1 boundary bound and other linear-update results: the leap form makes them bijective automatically; their
  content is A5/locality (L-A5).
- GR G1 universality claim (GR.md:669): declares A2 not required — but see tension T-A2-1.

### What breaks under each alternative substrate

| Substrate | Law-level QM representation (S ⇔ D ⇔ Q_fb) | Recurrence results (B2, B3, B8) | U_φ is the substrate's own unitary (B1, B6) | Microreversibility / ħ classical half (B7) | Determinism-only results (memory, quotient) |
|---|---|---|---|---|---|
| Deterministic, non-invertible (finite) | holds (law is in S) | hold on the eventual image; transients excluded or removable (dilemma, Main.md:62) | only on the eventual image | only on the eventual image | hold |
| Stochastic (finite) | holds (law is in S) | **fail as stated**: no φ^N = id; a stochastic substrate can be P-divisible (Markov chains) | **fails**: no substrate permutation; the unitary exists only as a constructed dilation | **fails as derived**: N_ij = N_ji needs a separate detailed-balance assumption for the stochastic kernel | memory floor (c) survives if the noise is fresh and independent (data processing); (a) pushforward identity becomes a kernel identity |
| Effectively reversible after adjoining hidden state | holds | hold for the dilated system *if* the dilation is closed into cycles (Main.md:598 closes tails into cycles) — recurrence becomes a property of the representative, not of nature | holds for the representative | holds only if the dilation respects T-invariance | hold |

### Interface dependence

A2's law-level role is interface-independent (Main's equivalence is passive, fixed basis). B6 and the
intervention-dilation theorem concern the passive / action-labelled settings; RECORD's record-writing interface is a
realization question (B1-type), not a law-level one.

### Controls affected

All three RECORD leap rules are of the second-order form and therefore **bijective** — linear, nonlinear and
majority alike. RECORD does not probe A2 at all; its controls separate A5, not A2.

### Relation to QM

- Not required by the generic QM *representation* (law level): A2 is a representation choice there.
- Required for the *identification* of the representation's unitary with the substrate's own dynamics (B1), and for
  the global-indivisibility results that rely on exact recurrence (B2, B3) — Track I's memory/indivisibility layer.
- Required by GR's own derivation of the classical half of the ħ calibration (B7).

### Circularity warnings

1. (Corpus, Main.md:62 / Substratum.md:94.) The empirical anchor for injectivity is "the observed unitarity of
   quantum dynamics". Using that anchor and then presenting unitarity of the emergent description as *derived* from a
   bijective substrate is circular. The corpus states the division honestly; the ledger records that B1's unitarity
   is input-anchored, not output.
2. (Law level.) Because S ⇔ D holds for every finite law, "the substrate is reversible" cannot be *tested* from
   finite visible laws alone. Any claim that observed statistics confirm A2 must go through realization
   identification (recurrence, microreversibility), not through representability.

### Replacement obligations (if A2 is weakened)

| Direct consumer | Obligation |
|---|---|
| B1, B6 | None for the law-level representation; for the identification claim, show the physical generator is the substrate's (or accept that U is a representative). |
| B2, B3 | Recurrence on the eventual image (deterministic non-invertible: already given by the dilemma argument), or a replacement indivisibility theorem for stochastic substrata. |
| B4, B5 | Measure selection and double stochasticity on the eventual image / for the stochastic kernel (bistochastic noise would preserve B5). |
| B7 | An explicit detailed-balance condition for the substrate kernel with respect to shell counting (stochastic case). |
| B8 | Cycle decomposition on the energy shell's eventual image, or a stochastic-ergodic replacement. |
| B9 | Restate the induced-dynamics class for the weakened substrate. |
| B10 | None mathematical; class boundary. |

### Classification (current evidence)

**Representation-free at the law level; physically load-bearing only through realization identification and exact
recurrence.** Deterministic non-invertibility is already absorbed by the corpus's dilemma argument (eventual image).
Stochasticity is the real alternative, and it breaks B2, B3, B7, B8 as derived.

### Tensions and drift (record only)

| # | Sites | Item |
|---|---|---|
| T-A2-1 | GR.md:669, :673 vs GR.md:68–74 | GR's universality claim says a substratum with **stochastic** dynamics would still produce ħ = c³ε²/(4G), ε = 2l_p and the 1/4 under H-slope, H-frame, H-Hawking "provided the partial-trace machinery and thermal self-consistency hold". The ħ chain's classical side (β_E = −∂ ln R_E) is derived at GR.md:70 "from finite deterministic reversible counting" via microreversibility (A2b + T). H-slope is only the observer-side slope (GR.md:74); H-frame is the foliation (GR.md:88). For a stochastic substrate the classical side needs a detailed-balance condition that none of S1–S4, H-slope, H-frame, H-Hawking states explicitly; "thermal self-consistency" may be intended to cover it. Candidate claim/evidence-boundary item; not resolved here. |
| T-A2-2 | Main.md:62 vs Main.md:526 | Main.md:62 calls the characterization theorem "conditional on finite reversible substratum dynamics"; at the law level the S ⇔ D ⇔ Q_fb equivalence is A2-free (A2 in the conclusion). Consistent once read as "the physical reading is conditional"; flagged so the ledger records the finer statement. |

### Closure of the four checks

**Check 1 — GR §3–§6 microreversibility (T-A2-1 resolved: confirmed, isolated, precisely stated).**
- Microreversibility appears only at GR.md:68–70 (grep of GR for microreversib / Θ / detailed balance / H-balance /
  shell rate). Its exact output: with Θφ Θ = φ⁻¹ and Θ M_i = M_{θi}, the trajectory-reversal map gives
  N_ij = N_{θj,θi}; for time-reversal-even coarse states N_ij = N_ji, hence N_i P_ij = N_j P_ji, hence the classical
  rate ratio ln(P_ij/P_ji) = −β_E(e_j − e_i) + ½ s_H″(E)(e_j² − e_i²) + ⋯ "from finite deterministic reversible
  counting". This is the identity −∂_{ΔE} ln R_E|₀ = β_E that H-slope (GR.md:74) takes as given on the classical side.
- GR.md:86 says the calibration needs only the scalar β_E = ∂s_H/∂E, from the horizon density of states and the first
  law. That fixes the *value* of β_E; the *identification of the classical rate-ratio slope with β_E* is what
  GR.md:70 derives, and that step uses A2b + time reversal.
- "Thermal self-consistency" (Step 4, GR.md:146; dependency list GR.md:637) is the equality of the classical horizon
  temperature with the emergent KMS temperature. It is a temperature-matching condition and does **not** state any
  condition on the substrate kernel.
- Conclusion: for a deterministic bijective substrate the classical side is derived; for a stochastic substrate it
  needs a stochastic microreversibility condition that none of S1–S4, H-slope, H-frame (the comoving foliation,
  GR.md:88), H-Hawking, or "thermal self-consistency" supplies. GR.md:669's stochastic-substratum clause is therefore
  stronger than the written derivation supports. **Kept as a claim/evidence-boundary item, not harmonized.**
- Isolation: no other §3–§6 use found; G1's A2-dependence is exactly this classical-rate-ratio identity, and it
  propagates to everything downstream of ħ (ε = 2l_p, the 1/4 coefficient; the counting S = A/ε² itself is
  unconditional, GR.md:12). The time-reversal structure is automatic for the second-order leap form (the inverse has
  the same form), so it is A2b + coarse-grain T-evenness, not A5.
- **Replacement obligation A2-GR.** For a stochastic substrate with kernel P on each energy shell, prove the
  stochastic microreversibility condition P(x, y) = P(Θy, Θx) (equivalently, detailed balance with respect to the
  uniform shell measure twisted by Θ), plus T-evenness of the coarse states, which together give
  N_ij = N_{θj,θi} → N_i P_ij = N_j P_ji and hence the classical β_E calibration.

**Check 2 — double stochasticity (B5 confirmed and scoped by the corpus itself).**
- Main.md:270–272: a uniform-prior marginal of a bijection is doubly stochastic (Birkhoff–von Neumann: a convex
  combination of permutation matrices); conversely any single rational doubly stochastic matrix has such a
  realization. A merely row-stochastic matrix has none in this form. Main.md:502: "double stochasticity is a property
  of uniform-prior marginals, not of deterministic realizability as such"; general laws are realized with a
  structured prior (process dilation).
- So: permutation ⇒ doubly stochastic (A2b); an arbitrary stochastic law ⇏ doubly stochastic; existence of a
  doubly-stochastic uniform-prior representative ⇔ the law's one-step matrix is doubly stochastic — a representation
  fact, not a substrate fact. B5 = A2b + uniform prior (measure selection, posit (iv)).
- **T-A2-3 (new).** The dilemma argument's empirical prong (Main.md:62) infers injectivity from "the observed
  unitarity of quantum dynamics" via "a merge … breaks the double stochasticity of the marginalized process … unitary
  emergent statistics are unistochastic". That inference needs (a) the uniform hidden prior — under a structured prior
  even a bijection's marginal need not be doubly stochastic (Main.md:502) — and (b) that the observed visible
  statistics are of the bistochastic class; GR.md:76 itself notes that a bare visible law read off a closed unitary is
  bistochastic and "that form is unavailable in general", since open-system (ancilla-carrying) visible laws are not.
  Recorded as a scope tension on the empirical anchor of A2b; not resolved here.

**Check 3 — SM reversibility (automatic; no A2-direct SM consumer).**
- SM.md:70 factorization-uniqueness theorem: hypothesis "φ a bijection"; its key step is the wave equation's
  *addition* (algebraic dependence of inputs) — content is A5/locality; bijectivity is automatic for the second-order
  form.
- SM §4.1 form lemma "second-order reversible" and §4.4 "Reversibility requires D = −I": reversibility of the
  second-order form (inverse has the same form), automatic, and at observer level for the normalized branch.
- SM §2.7 q-gauge (SM.md:90–94): equivalence defined by emergent transition probabilities — law level; A2 unused.
- SM Theorem 17 (T-invariance of the wave equation): time-reversal of the second-order form holds for every F; it is
  the Θ GR.md:68 uses.

**Check 4 — book mirror (drift recorded; not a classification input).**

| # | Site | Item |
|---|---|---|
| R6 | book ch02-substratum.md:78 | "(A2) Determinism … a bijection — deterministic and reversible. This is the input from Lemma 3 of Chapter 1." Omits the two-part status (dilemma argument; empirical anchor in observed unitarity) of Substratum.md:94 / Main.md:62, 706. Lag, not conflict. |
| — | book ch02:122, ch09:199 | Consistent with Substratum / Structure (stochastic theories outside the class; matrix models fail A2). |
| — | book (all) | GR.md:669's stochastic-substratum universality clause and GR.md:68–70's microreversibility are not mirrored in the book; nothing to reconcile there, T-A2-1 is papers-only. |

### Deterministic non-invertible substrata — own replacement category (A2-EV)

A finite deterministic φ restricts to a permutation on its eventual image E∞ = ⋂_n φⁿ(S). This rescues recurrence
*asymptotically* (φ^{N}|_{E∞} = id), but not:
- recurrence from time zero (B2 Step 1 uses T^{(N)} = I from the initial time; on transients T^{(N)} ≠ I);
- the uniform-prior double stochasticity on all of S (B5), the permutation unitary on all of S (B1), and Θφ Θ = φ⁻¹
  (B7), all of which fail on transient states;
- the cycle decomposition of the full energy shell (B8).
The corpus's dilemma (Main.md:62) handles this by restricting to "registered history", which lives on E∞, plus the
empirical prong (T-A2-3) for merges that would leave a trace. A2-EV is therefore "A2 on E∞ + a premise that registered
history lies in E∞", not equivalence with A2.

### Representation vs physical-identification (the L-A2 headline)

A2 is not required for the observable-law representation theorem (S ⇔ D ⇔ Q_fb). It is required when the corpus
identifies a reversible representative with the actual substratum and then uses the resulting recurrence, unitarity,
cycle structure, or microreversibility as physical facts (B1–B8). A theorem relying only on the existence of a
reversible representation is A2-free; one asserting that the substratum itself recurs, is unitary, has cycles, or is
microreversible consumes A2 or a replacement (A2-EV, A2-GR, or a stochastic indivisibility theorem).

### Combined statement after L-A5 and L-A2

Neither substrate linearity (A5) nor substrate bijectivity (A2) is required for the generic observable QM
representation. Their work begins when the corpus identifies particular substrate properties with particular
physical realizations and derives further structure: SM selection and realization-specific coherence (A5);
recurrence-based indivisibility, the substrate's own unitary, cycles, and the classical side of the ħ calibration
(A2).

***

## Post-freeze addendum to L-A2 (consumer found while building L-A1)

- **B11 (verified).** GR Appendix A.6 generalized second law (GR.md:805): "The hidden-sector prior is uniform
  (Liouville marginalization), so the marginal channel is unital: Φ_V(I_V) = Tr_{BD}[U_φ (I_V ⊗ ρ_B ⊗ ρ_D) U_φ†] = I_V
  … the uniform prior is load-bearing here." Uses A2b (U_φ unitary) + the uniform measure (posit (iv)); a
  physical-identification use. L-A2's classification is unchanged.

***

## L-A1 — Finiteness of the substratum configuration space — CLOSED 2026-10-03

**Exact statement.** "(A1) **Finiteness.** The configuration space S is finite." (Substratum.md:92), with a
two-part status: E3 (holographic bound read as a Hilbert-space dimension cutoff dim ℋ ≤ e^{A/4}) bounds what
observation reaches — the visible sector and its boundary layer 𝒞_V × 𝒞_B, on which all emergent observables
depend (boundary-only dependence lemma, GR.md:112); "the extension to all of S is then a gauge choice rather than a
further fact" (deep-sector enlargement, Theorem 24(iii)), and A1 selects the minimal finite representative.
Main.md:62: "only finite visible resolution is a theorem (Lemma 1) … total finiteness of that representative is a
physical posit". Main.md:706 posit (ii): consumed "by the recurrence step of §2.3 and by §4.6".

**Roles, separated.**

| Role | Content | Status | Level |
|---|---|---|---|
| F1 finite visible | 𝒞_V finite (Main Lemma 1, Main.md:48) | theorem from the finite boundary of the observer (plus holographic support) | INTERFACE (G) |
| F2 finite boundary layer | \|𝒞_V × 𝒞_B\| ≤ e^{S_∂} (Substratum Corollary (i), Substratum.md:262) | E3 read as a dimension cutoff — "the interpretive premise of A1, and this is the only place it enters" | SUBSTRATE (boundary) |
| F3 total finiteness | \|S\| < ∞ including the deep sector 𝒞_D | gauge choice of the minimal representative (Theorem 24(iii)) — *for accessible-time statements only* (see T-A1-1) | SUBSTRATE |
| F4 finite representation | every finite-horizon visible law has a finite reversible realization | theorem: response-table form with a product prior, any real law (Main.md:498); with a *uniform* prior exactly iff the law is rational (Main.md:270, :496) | representation |
| F5 exact recurrence | φ^N = id | consequence of F3 + A2b | SUBSTRATE |
| F6 counting / measure | uniform counting, Birkhoff decompositions, shell cardinalities, capacity log₂\|𝒞_H\| | uses F2 or F3 with the counting measure (posit (iv)) | SUBSTRATE / representation (per consumer) |

### Consumers, with representation vs physical identification

| # | Consumer | Anchor | Role used | Rep. or phys. identification | Evidence |
|---|---|---|---|---|---|
| C1 | S ⇔ D ⇔ Q_fb | Main.md:526 | F1 + F4 | **representation**: finite C_H is *constructed*; finiteness of nature not assumed | verified |
| C2 | P-indivisibility at the recurrence scale (non-permutation witness) | Main.md:115–131 | F5 (= F3 + A2b) | **physical identification**: a statement about the full recurrence cycle of the actual representative | verified |
| C3 | Readback ⇒ global indivisibility | Main.md:137–142 ("global recurrence-cycle result") | F5 | physical identification | verified |
| C4 | Capacity floors I ≤ log₂\|𝒞_H\| (C3 necessity; unavoidable memory (c)) | Main.md:484, :580 | F2 effectively (boundary layer), F3 literally | representation-safe if read on 𝒞_B; vacuous for infinite 𝒞_H literally | declared |
| C5 | Measure selection: counting measure on the finite representative, uniform on cycles | Main.md:56, :62 | F3 + A2b + posit (iv) | physical identification | verified (statement) |
| C6 | Main §4.6 structural exclusion of equilibrium-phase observers / anti-Boltzmann-brain corollary | Main.md:722–738; Main.md:706 says it consumes A1 | (EM) mixing on finite local neighbourhoods | declared boundary-only by Main.md:706 | declared |
| C7 | GR boundary-mode counting S = A/ε², area law | GR.md:12, §5, :396 | F2 (finite density ε, boundary modes "catalogued by spatial location") | survives as a **finite-density** statement; does not need F3 | declared |
| C8 | GR boundary-only dependence lemma T_ij = T^{(B)}_ij + O(t/τ_B) | GR.md:112–134 | works with 𝒞_D arbitrary (finite or infinite) | representation-safe for t ≪ τ_B | verified (statement) |
| C9 | Page curve A.7: shell bijection decomposes into cycles | GR.md:807–825 | finite B ∪ R (boundary modes n_B, n_R) + A2b; D decoupled (τ_evap ≪ τ_B^D) | F2-type (finite B ∪ R), not F3 | verified |
| C10 | GSL A.6: uniform prior → unital channel | GR.md:805 | finite uniform prior on B, D | physical identification (uniform prior); infinite D needs a normalizable replacement | verified |
| C11 | Lean / probes: finite carriers throughout (`Fintype`) | OIBridge | — | representation | — |
| C12 | Class filter: matrix models consistent only at finite N | Structure.md; book ch09:197 | F3 as predicate | treats F3 as physical | verified |

### The central finding: A1 is gauge only for accessible-time statements

Substratum's transfer corollary (iii) (Substratum.md:262) is correct in its stated scope: any statement P expressible
through {T_ij(t) : t ≪ τ_B} has constant truth value on the deep-sector-enlargement orbit, finite or infinite. For
that class, A1 is "a convenience of proof". It does **not** cover recurrence-scale statements: φ^N = id has N far
beyond τ_B, so C2 and C3 are not expressible through accessible-time T_ij and are not transferred by (iii). They are
physical-identification uses of F3 (+A2b).

### T-A1-1 — transfer corollary overextends to recurrence-scale P-indivisibility (claim/evidence boundary)

Substratum.md:262 continues: "In particular, P-indivisibility — established on the minimal finite representative by
recurrence (φ^N = id) — holds on every member; on infinite-deep-sector members, where recurrence is unavailable, the
accessible-timescale backflow lemma ([Main §2.3]) establishes the same conclusion without recurrence. The two routes
agree where both apply and jointly cover the orbit". Two problems, both from the corpus's own text:
1. **Scope.** Recurrence-scale P-indivisibility is not a t ≪ τ_B statement (Main.md:142: "a global recurrence-cycle
   result"), so clause (iii) does not transfer it.
2. **Different conclusions.** The backflow lemma (Main.md:167–170) concludes I(X_{<k}; X_{k+1} | X_k) ≥ p₀δ²/ln 2 —
   accessible non-Markovianity, under (C1)–(C3) plus a (C4) gap. Main.md:604 states that non-Markovianity and
   P-indivisibility "are distinct", P-indivisibility "the strictly stronger property", witnessed by the XOR family
   (1 bit of conditional memory, matrix family factors through Λ = I). Main.md:174 ("Role of (C2)–(C4)") says the
   recurrence argument and the readback lemma are "independent: the former establishes P-indivisibility … at the
   recurrence time; the latter locates observable backflow inside accessible windows". So the backflow lemma does not
   establish "the same conclusion", and the two routes have different hypotheses (non-permutation witness vs (C4)
   gap) and different conclusions.
Main.md:706 (posit (ii)) carries the same extension ("consumed here by the recurrence step of §2.3 and by §4.6, whose
conclusions accordingly hold … on every member of the gauge class"). Recorded as a claim/evidence-boundary item at
both sites; not harmonized. Correct scoped form: accessible-time statements transfer; recurrence-scale
P-indivisibility holds on finite members; on infinite-deep-sector members the accessible-window backflow (under a
(C4) gap) holds instead, a weaker and different property.

### Consequence of F3 + counting measure (recorded, not a corpus claim) — O-A1-1

If the actual substratum is a finite representative under the counting (uniform) measure, every exact finite-horizon
visible probability is rational (counts over \|𝒞_H\|; Main.md:270 "exactly when the transition probabilities are
rational"). Real-valued laws then arise only as limits or approximations (Main.md:544 ε-form). This is untestable at
finite precision and is a physical-identification consequence, not a representation fact (the product-prior response
table realizes real laws exactly, Main.md:498).

### Interface dependence

C1, C4, C8 are interface-independent at law level. C2, C3 are passive-law, recurrence-scale. RECORD's finite window
simulator uses infinite lattices with an exact causal-cone truncation: RECORD never used F3 (consistent with its
accessible-horizon scope).

### Controls affected

None of RECORD's conclusions depends on F3; RANK's scope note (A1 gauge for finite visible/boundary data only; not
for the completion body) is the same boundary as T-A1-1, reached independently.

### Relation to QM

The generic observable QM representation uses F1 and F4 only (finite visible alphabet; constructed finite
representative). F3 enters only through recurrence-scale indivisibility and measure selection — the
physical-identification layer, as with A2 and A5.

### Circularity warnings

1. "If a theorem only needs the existence of a finite representative, that does not establish that the substrate
   itself is finite" — C1's finiteness is constructed and cannot be cited as evidence for F3.
2. Book ch02:76 derives A1 from Lemma 1 (finite visible) — conflating F1 with F3 (R7 below).

### Replacement obligations (if F3 is dropped: infinite deep sector)

| Consumer | Obligation |
|---|---|
| C2, C3 | Replace recurrence-scale P-indivisibility by an accessible-window statement; the corpus has the backflow lemma (non-Markovianity under a (C4) gap) — strictly weaker; or prove P-indivisibility directly for infinite members. |
| C4 | State capacity floors on 𝒞_B (finite by F2). |
| C5, C10 | A normalizable invariant measure on the deep sector (or factorization with D decoupled) replacing the counting measure. |
| C7, C8, C9 | None beyond F2. |
| C12 | None mathematical; class boundary. |

### Classification

F1 theorem; F2 the single interpretive premise (E3 as dimension cutoff); F3 gauge for accessible-time content,
**physical-identification for recurrence-scale content** (C2, C3, C5, C10); F4 representation theorem.

### Corpus drift (record only)

| # | Site | Item |
|---|---|---|
| T-A1-1 | Substratum.md:262; Main.md:706 | Transfer corollary's "in particular" clause and posit (ii) extend gauge-class transfer to recurrence-scale P-indivisibility, beyond clause (iii)'s scope, and identify the backflow lemma's conclusion with P-indivisibility, contrary to Main.md:604 and Main.md:174. |
| R7 | book ch02-substratum.md:76 | "(A1) … This is the input from Lemma 1 of Chapter 1" — derives total finiteness from finite visible resolution; the papers separate them (Main.md:62; Substratum.md:92 two-part status). Conflation of finite observable representation with finite ontology. |
| R8 | book ch09-universality.md:197 | "The framework requires finite \|S\| … the bridge would require N to be physically finite" — treats F3 as physical, against Substratum.md:92's gauge reading. |
| — | book ch02:144 | Deep-sector enlargement: "the observer's predictions are insensitive to which" — correct for accessible-time predictions; unqualified. |

***

## L-A4 — Center independence — CLOSED 2026-10-03

### The first finding: one name, three logically independent conditions

| Label | Statement | Where the corpus uses this meaning |
|---|---|---|
| **A4-T** (translation / homogeneity) | "φ does not depend on a choice of 'center' site; equivalently, φ commutes with lattice translations up to gauge" | Substratum.md:98 (the posit as stated); Substratum.md:158 ("translation-invariant"); Substratum.md:218 ("rules out preferred-frame theories"); Structure.md:291–294 (BFSS translation invariance); book ch02:82 |
| **A4-S** (no self-coupling, substrate) | "the next value at a site contains no explicit copy of that site's present value": f independent of x_i; multi-component C = 0 | SM.md:224 (form-lemma proof), SM.md:232, SM.md:306 ("center independence requires C = 0"), SM Theorem 3 (SM.md:296–298, self-term ↔ mass term ↔ chiral breaking), book ch05:97, :101 |
| **A4-P** (partition-center independence) | "the framework's predictions are independent of the choice of partition center" | book ch09:203 only |

These are independent: a translation-invariant rule may carry a self-term (x_i(t+1) = c·x_i + α Σ_{j∼i} x_j − x_i(t−1)
is translation invariant with c ≠ 0); a rule with no self-term need not be translation invariant (site-dependent
neighbour couplings); A4-P concerns the observer partition, not φ.

### T-A4-1 — the posit as stated does not deliver what its main consumer uses (claim/evidence boundary)

Substratum Stage 2(b) (Substratum.md:158) cites "Center independence (A4), isotropy (E4), and linearity (A5)" for
"the unique second-order linear dynamics on a lattice that is translation-invariant, isotropic, and reversible has the
form f = α(x₁ + ⋯ + x_{2d}) mod q". With A4 read as stated (A4-T, translation invariance), that uniqueness is false:
a self-term c·x_i survives translation invariance, isotropy, linearity and reversibility. The form lemma's own proof
(SM.md:224) excludes the self-term using A4-S ("Center independence requires that f not depend on x_i itself"). So
the reconstruction's wave-equation step consumes A4-S while Substratum's posit list states A4-T. Recorded at
Substratum.md:98/:158 (and book ch02:82/:98); not harmonized.

### The four claims you asked to separate

| Claim | Content | Status in the corpus |
|---|---|---|
| A4-substrate | A4-T and/or A4-S of φ | posit (A4-T as stated; A4-S as used) |
| Projection covariance | the observer projection commutes with the symmetry: [U, R_g] = [P, R_g] = 0 | **hypothesis** of Theorem 1a (SM.md:238); not derived. Satisfied for sublattice-periodic visible σ-algebras (e.g. the checkerboard partition of SM Theorem 12); **not** for a bounded-region observer, which breaks translations |
| A4-observer | translation invariance of the projected kernel (A4-T_obs) and zero observer self-weight p₀ = 0 (A4-S_obs) | see descent below |
| H-T1 use | Corollary 1b (SM.md:266–270) needs a scalar, translation-invariant, NN-local, O_h-equivariant, constant-preserving observer Markov part, and p₀ = 0 for T = A/(2d) | consumes A4-T_obs and A4-S_obs |

### Descent: what is and is not a theorem

- **A4-T: descends, conditionally.** Theorem 1a (exact projected evolution; every memory kernel BD^mC commutes with
  R_g) gives A4-T_substrate + projection covariance ⇒ A4-T_obs for the Markov part and every kernel. A genuine
  theorem, with projection covariance as a hypothesis.
- **A4-S: does not descend; no theorem, and a counterexample.** SM.md:232: the swap φ(x, h) = (h, x) has no self-term
  (x′ = h) yet on the correlated ensemble h = x gives x′ = x with certainty. SM.md:272: "microscopic CI alone does
  not imply p₀ = 0 after correlated hidden degrees of freedom are traced out … Thus A/(2d) is a theorem **conditional
  on observer-level CI**, while the descent of CI through the substratum-to-observer map remains open." SM.md:222:
  "the range and the self-weight of the projected Markov part are set by the hidden conditional law rather than by the
  microscopic radius".
- **Conclusion.** The manuscript states an implication only for A4-T (given covariant projection). For A4-S it places
  the substrate and observer conditions side by side and says explicitly that the implication is open. A4 must not be
  credited with H-T1's center-free clause: **H-T1 contains an additional observer-level premise, A4-S_obs (p₀ = 0).**
- **Same pattern for NN-locality (cross-entry, for the A3 entry):** H-T1's "nearest-neighbor local" observer kernel
  does not descend from microscopic range (SM.md:222: a correlated hidden preparation of range two makes the visible
  one-step law range two). Also an observer-level premise.

### Interaction with A1 (checked, not assumed)

- The observer conditions A4-T_obs and A4-S_obs are statements about the one-step projected Markov part, i.e. about
  accessible-time T_ij; by Substratum's transfer clause (iii) they have constant truth value on the deep-sector-
  enlargement orbit. **Observer-level center freedom is gauge-robust.**
- Substrate A4-T is **not** gauge-invariant in full: deep-sector enlargement (Theorem 24(iii)) permits "arbitrary
  dynamics" on 𝒞_D subject only to τ_B^D ≫ τ_S, including dynamics that break translation invariance in the deep
  sector without changing any observable. So A4-T's physical content is its accessible-time/boundary part — which is
  what its stated observational anchor ("the homogeneity of physical law", Substratum.md:98) actually measures.
- Hence a descent theorem, if found, would be the gauge-robust object; substrate A4 in full is not.

### Consumers

| # | Consumer | Uses | Rep. or phys. identification | Evidence |
|---|---|---|---|---|
| E1 | Form lemma / Substratum Stage 2(b) (substrate route to the wave operator, = L-A5 D1) | A4-S (+ translation invariance implicitly) | physical identification (substrate rule) | verified |
| E2 | SM §4.4 multi-component form: "center independence requires C = 0" (= L-A5 D5) | A4-S | level-ambiguous (R5) | verified |
| E3 | SM Theorem 3: CI ⇔ exact chiral symmetry of staggered fermions; SM.md:591 "forbids explicit masses" → Higgs mechanism | A4-S (on the observer branch: A4-S_obs) | realization / SM selection | verified |
| E4 | Corollary 1b → Theorem 1 (observer route, H-T1) | A4-T_obs (from A4-T + covariant P via Theorem 1a) and A4-S_obs (premise) | representation-level (observer kernel) | verified |
| E5 | Theorem 1a, Corollary 1a (isotropy inherited by kernels) | translation + O_h covariance of U and P | representation-level | verified |
| E6 | Class filter: BFSS "holds" A4 (Structure.md:291–322) | A4-T only | predicate | verified |
| E7 | Substratum.md:218 "rules out preferred-frame theories" | A4-T | predicate | verified |

Not consumers: Main's representation layer (no lattice); GR G1 (GR.md:669 lists A4 among A2–A5 not required for the
partition-geometry results).

### Controls affected

All three RECORD leap rules are translation invariant (A4-T) and have no self-term in F (F depends on v_{i±1} and,
for nonlinear and majority, on v_i — **so nonlinear and majority violate A4-S**: F_nonlinear = v_{i−1}v_{i+1} + v_i
and majority both read v_i). The linear rule satisfies A4-S. RECORD's controls therefore differ in A4-S as well as A5;
RECORD's separation cannot be attributed to A5 alone. (Recorded as a scope note on the sealed RECORD result, which
already attributes nothing to A5 specifically beyond "A5-violating controls".)

### Relation to QM

Not used by the generic QM representation. A4-S enters the SM chain (wave operator, chirality, masslessness); A4-T
enters the observer-isotropy route via projection covariance.

### Circularity warnings

1. Using H-T1 (which contains A4-S_obs) as evidence that substrate A4-S is physically correct would be circular: the
   observer condition is assumed, not derived.
2. A4-T's empirical anchor (homogeneity of accessible law) supports only its gauge-invariant (accessible-time) part.

### Replacement obligation (the descent theorem)

Given φ and the canonical observer projection P_μ defining the Markov part T = P_μ U P_μ (Lemma 1c), prove:
(a) **translation descent** — already Theorem 1a, *provided* projection covariance [P, R_g] = 0 is established for
the observer's actual visible σ-algebra (an open hypothesis for region observers);
(b) **self-weight descent** — p₀(T) = 0, i.e. under the selected measure the projected one-step kernel assigns zero
weight to the current visible value at the same site, for the class of hidden conditional laws the observer meets.
The swap counterexample shows (b) fails for correlated hidden preparations; the obligation is a theorem identifying
the hidden-law class (e.g. product / mixing conditionals, linking to the (EM) mixing hypothesis) on which (b) holds,
or an explicit observer-level premise in its place.

### Classification

A4-T: substrate posit whose gauge-invariant content is accessible-time homogeneity; descends to the observer given
projection covariance. A4-S: substrate posit used by the SM chain; **does not descend** (open, counterexample);
its observer-level counterpart is an independent premise of H-T1. A4-P: a book-only third reading.

### Drift (record only)

| # | Site | Item |
|---|---|---|
| T-A4-1 | Substratum.md:98, :158; book ch02:82, :98 | Posit stated as A4-T; the wave-equation uniqueness consumes A4-S; with A4-T alone the stated uniqueness fails (self-term survives). |
| R9 | book ch09:203 | A4 restated as A4-P (partition-center independence) — a third meaning, at observer level. |
| R10 | book ch05:97 | "exact chiral symmetry … equivalent to center independence of the substratum dynamics" — states substrate A4-S as equivalent to an emergent property; SM Theorem 3 holds on the observer branch, where the relevant condition is A4-S_obs, whose descent from substrate A4-S is open (SM.md:272). |

***

## Design input from L-A4 (owner, 2026-10-03): orthogonal controls for any later level

RECORD's nonlinear and majority controls differ from the linear control in A5 **and** A4-S, so their OVER-RANK
behaviour cannot be attributed to substrate nonlinearity alone. Later control sets should be orthogonal where possible.
Candidate second-order (hence bijective, A2-respecting), translation-invariant rules on 𝔽₂, recorded here for design,
not run: (1) A5 ✗, A4-S ✓ — F = v_{i−1}v_{i+1}; (2) A5 ✓, A4-S ✗ — F = v_{i−1} + v_i + v_{i+1}; (3) A5 ✗, A4-S ✗ —
the existing nonlinear (v_{i−1}v_{i+1} + v_i) and majority rules; (4) A5 ✓, A4-S ✓ — the existing linear rule.

***

## L-A6 — Background independence — CLOSED 2026-10-03

### The split (four readings; the corpus itself separates the first two)

| Label | Statement | Level | Status | Anchor |
|---|---|---|---|---|
| **A6-COV** | the dynamics is covariant under site-dependent internal-index transformations G(n), with link couplings transformed alongside, M(n, ê_j) → G(n) M(n, ê_j) G(n+ê_j)⁻¹ | SUBSTRATE (data structure of the law) | posit — but "once the link variable is data transported in this way the local transformation law imposes no further condition on the rule" (SM.md:114): in effect a *choice to model couplings as link-valued data* | Substratum.md:102, :220; SM.md:110–114; book ch02:86, ch05:141–147, ch09:207 |
| **A6-GRAPH** | state-dependent coupling graph: s(t+1) = φ_{s(t)}(s(t)), G_{φ_s} varies with s | SUBSTRATE (dynamics) | separate principle — "the two share a name and are different requirements" (SM.md:100; Substratum.md:102) | SM.md:98–108 |
| **H-Bell** | prepared graph family preserves operational no-signaling and satisfies a metric/Ollivier–Ricci convergence condition strong enough for the Einstein reconstruction's continuum step | SUBSTRATE + continuum limit | named hypothesis, open; now downstream of a harder failed step (below) | Substratum.md:132, :170; Main.md:394 |
| **A6-EMERG** | "the framework has no fixed spacetime background — the substratum is the background, with spacetime emergent" | interpretive | interpretation, not a premise of any theorem | book ch09:207 ("a different sense of the same words") |

### Answers to the six questions

| Question | A6-COV | A6-GRAPH | H-Bell |
|---|---|---|---|
| 1. Level | substrate (data model) | substrate (dynamics) | substrate + continuum |
| 2. Assumption / theorem / interpretation | assumption that is nearly definitional (imposes no condition on the rule once couplings are link data) | assumption (principle) | open hypothesis |
| 3. Consumers | local gauge reading: global commutant stabilizer → local SU(3)×SU(2)×U(1), plaquette invariance, "Wilson plaquette action, now derived" (SM.md:110–114), on the H-link + H-cust branch | Einstein equations as self-consistency on G(x) (SM.md:116 ff., Discrete Einstein theorem SM.md:140); the Bell escape (Main.md:394); d = 3 selection section (SM §3, title) | identification of the Bell-violating completion with the local lattice/Einstein sector (Substratum Theorem 23, "only conditional on H-Bell"; Main.md:394) |
| 4. Descends through the observer projection? | not shown — local gauge transformations relate *representatives* (conjugate dynamics with transformed links), not symmetries of a fixed φ, so Theorem 1a does not apply; observer-level local gauge redundancy is asserted on the observer branch, not derived | the reference chain "survives under three constraints" (SM.md:106): local graph-dependence, **center-independent graph dependence (G(x) at i does not depend on x_i — an A4-S analogue)**, statistical isotropy; bijectivity automatic (SM.md:102) | — |
| 5. Gauge-robust under deep-sector enlargement? | its accessible content (covariance of emergent local couplings in the accessible region) is accessible-time; robust | the GR uses are local-horizon (accessible) constructions; deep-sector graph dynamics are unobservable; robust in the same sense | concerns the prepared (accessible) graph family; robust |
| 6. Used as if implying another? | not in the papers (explicitly separated); book ch05:147 "derivation … is therefore complete" sits with ch05:133/196 "conditional on H-link/H-cust" | no | H-Bell is presented as the remaining compatibility step, but it now presupposes a curvature functional that the cited chain does not supply (T-A6-2) |

### Findings

- **The corpus does not conflate A6-COV and A6-GRAPH** — it separates them explicitly at three sites (SM.md:100,
  Substratum.md:102, Substratum.md:220) and the book follows (ch09:207). The loose-usage risk you anticipated is real
  only at section-title / summary level (SM §3 title "Background Independence and the Selection of d = 3" uses the
  GRAPH sense; Explainer.md:882 lists "background independence" under structural foundations without a sense).
- **A6-COV carries almost no dynamical content.** Its own home says the local transformation law "imposes no further
  condition on the rule" once couplings are link data. Its work is to *license reading* the global commutant as a local
  gauge symmetry. What is derived from it is the gauge invariance of plaquette traces; that the link dynamics *is*
  the Wilson action is a further claim (T-A6-1).
- **A6-GRAPH reuses A4-S.** Its second survival constraint is center-independent graph dependence, i.e. the A4-S
  condition at the level of the graph map; the L-A4 descent gap applies to it as well.
- **The Einstein reconstruction's continuum step currently fails at its reference instantiation, by the corpus's own
  account (T-A6-2).**

### T-A6-1 — "Wilson plaquette action, now derived rather than postulated" (claim/evidence boundary)

SM.md:114: under A6-COV, P → G P G⁻¹, so Re Tr P is gauge invariant — "it is the Wilson plaquette action, now derived
rather than postulated". The derivation establishes that Re Tr P is a gauge-invariant functional of the link data;
it does not establish that the link dynamics is governed by that functional (every class function of plaquettes, and
other loops, is equally gauge invariant). Book ch05:147: "The framework's derivation of local SU(3)×SU(2)×U(1) gauge
invariance is therefore complete … the resulting structure is the Wilson plaquette action" — while ch05:133 and :196
and SM.md:110 place it on the conditional H-link/H-cust branch. Recorded; not harmonized.

### T-A6-2 — "Theorem (Discrete Einstein equation)" whose proof states it is not established (status drift)

SM.md:140 labels the Discrete Einstein equation a **Theorem**. Its own proof, step (iv) (SM.md:146), states that the
cited continuum theorem (van der Hoorn et al.) covers the manifold-distance-weighted metric in arbitrary D but the
intrinsic hop-count metric only in D = 2; that on the degree-6 cubic reference graph the hop metric is exactly ℓ₁
with a scale-independent √2 diagonal stretch; that "a future extension … from D = 2 to D = 3 would therefore not rescue
this step"; and that "the hop-metric Ollivier route therefore fails at its reference instantiation, and **the discrete
Einstein theorem above is not established by the cited chain**". Main.md:394 and Substratum.md:170 repeat the failure
and name the repair (re-found curvature on the propagation/Laplacian geometry, SM §3.2). A theorem label over a proof
that disclaims establishment is an assert-then-qualify status mismatch (AGENTS.md §A.30). Recorded at SM.md:140;
not harmonized.

### Consumers and layer

| # | Consumer | Uses | Layer | Rep. / phys. identification |
|---|---|---|---|---|
| G1′ | Local gauge reading, plaquette invariance (SM.md:110–114; Substratum Stage 2(d) last sentence) | A6-COV + H-link + H-cust | SM selection | physical identification (carrier) |
| G2′ | Einstein equations from Jacobson on G(x); Discrete Einstein "theorem" | A6-GRAPH + constraints (i)–(iii) + Bisognano–Wichmann + Ollivier continuum (failed at reference) | GR, G3 direction | physical identification |
| G3′ | Bell escape: preparation-indexed nonlocal edges (Main.md:394) | A6-GRAPH + H-Bell | QM-adjacent (Bell completion) | physical identification |
| G4′ | Class filter: BFSS "holds in spirit" (Structure.md:309–316) | A6-COV analogue (matrix-internal U(N)) | comparison | predicate |

Not consumers: Main's representation layer; GR G1 (GR.md:669: "A6 … is required for the SM gauge-group derivation but
not for the partition-geometry results"); RECORD (fixed graph, K = 1: A6-COV vacuous, A6-GRAPH absent).

### Relation to QM

Not used by the generic QM representation. A6-GRAPH + H-Bell enter only the Bell-inclusive *completion* question
(which deterministic completion realizes Bell-class statistics), a realization question.

### Replacement obligations

| Reading | Obligation |
|---|---|
| A6-COV | Show that the emergent link dynamics is the Wilson (or another specified) gauge action, not merely gauge invariant; and that observer-level local gauge redundancy follows from substrate covariance through the projection. |
| A6-GRAPH | Prove the three survival constraints for the intended state classes, including the A4-S-type constraint (ii), which shares L-A4's descent gap. |
| H-Bell | First re-found the curvature functional on the propagation/Laplacian geometry (the corpus's named repair), then prove its continuum convergence for the reference and prepared families, then no-signaling. |

### Classification

All four readings sit in the realization/selection layer. None is a premise of the generic observable QM
representation. A6-COV is near-definitional; A6-GRAPH is a dynamical principle feeding GR and the Bell completion;
H-Bell is open and presently blocked upstream by T-A6-2's failed reference step.

### Drift (record only)

| # | Site | Item |
|---|---|---|
| T-A6-1 | SM.md:114; book ch05:147 | "Wilson plaquette action, now derived"; "derivation … complete" vs conditional branch (ch05:133, :196; SM.md:110). |
| T-A6-2 | SM.md:140 vs SM.md:146 (iv) | Theorem label over a proof that states the result is not established by the cited chain. |
| R11 | SM §3 title; Explainer.md:882 | "Background independence" used without a sense at title/summary level (GRAPH sense in SM §3). |
