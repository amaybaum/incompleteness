# Premise ledger (off-repo, read-only; corpus at base 0f2687b7)

Corpus read from `scratchpad/base0f/` (`git archive 0f2687b7 papers book`; every paper diffed equal to
`git show 0f2687b7:<path>`). Line anchors are to that tree. Built dependency-first, starting from A5.

**Fields per entry.** Exact statement · descriptive level (SUBSTRATE / INTERFACE (G) / R4 / Q) · status
(definitional / posit / sharpened stipulation / theorem / probed) · direct consumers · transitive consumers ·
coexisting (uses nearby structure, not the premise) · evidence status of each dependence · interface dependence ·
controls affected · relation to QM · circularity risk · replacement obligation per direct consumer · corpus drift ·
open checks.

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
