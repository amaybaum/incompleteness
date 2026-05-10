# The Incompleteness of Observation

**Author:** Alex Maybaum
**Date:** April 2026
**Status:** DRAFT PRE-PRINT
**Classification:** Theoretical Physics / Foundations

This repository develops a single framework across four papers, with two companion papers on the relationship to other unification programs:

- **Main** — establishes the equivalence between embedded observation and quantum mechanics
- **SM** — derives the Standard Model from a $d = 3$ cubic lattice
- **GR** — derives the gravitational sector from the cosmological horizon
- **Substratum** — ties these into a single construction at the substratum level
- **Synthesis** *(canonical synthesis)* — articulates the framework's two-dimensional hierarchical structure: an observation hierarchy (Levels A-D, depth axis) and a gauge hierarchy (Levels G1-G4, breadth axis), with their orthogonality and the multi-level structural realism that follows
- **Extensions** *(cross-framework companion)* — develops the relationship between OI and other unification programs: Part I establishes that OI and string theory are not equivalent at the substratum level; Part II formalizes universality classes of embedded observers; Part III provides the cross-framework synthesis through partial-trace observational features

A self-contained paper, **Juno**, presents the prediction $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$, recently confirmed by JUNO at $0.07\sigma$ against the post-JUNO global fit. See [`Juno.md`](Juno.md).

The full file list is in [Contents](#contents).

---

## Overview

The universe is completely described by a lossless memory with finite read-write access. Physics is what that memory looks like from inside.

A *lossless memory* is a system whose states evolve by a reversible rule. Every state has one predecessor and one successor; no information is created or destroyed. The past is always recoverable from the present. Formally, this is a finite set $S$ of distinguishable states and a bijection $\varphi: S \to S$. The observer has access to only a bounded portion of the state, called the *visible sector*. Each step updates both sectors at once, but the observer reads only the visible part. Correlations written into the hidden sector persist there and return on later steps. This read-write cycle is what produces quantum mechanics — not passive observation.

The framework begins with a single empirical fact — *observation occurs* — formalized as a definition: an observation is a triple $(S, \varphi, V)$ consisting of a total system, a deterministic dynamics, and an embedded observer. No quantum postulates appear. Three structural lemmas follow (finiteness, causal partition, unique measure), from which quantum mechanics emerges under three conditions on the hidden sector: coupling (C1), slow-bath memory (C2), and high capacity (C3).

The theorem becomes physics at the cosmological horizon, where stress-energy conservation enforces C1, the universe-vs-laboratory timescale ratio enforces C2, and the $\sim 10^{122}$ horizon degrees of freedom enforce C3. From this single realization, the framework derives $\hbar$ from thermal self-consistency, recovers the Bekenstein-Hawking entropy with the $1/4$ factor (confirmed by GW250114 at 99.999%), dissolves the $10^{122}$ cosmological constant discrepancy as the information compression ratio of the trace-out, and produces the dark sector phenomenology including the MOND acceleration scale $a_0 = cH/6$. The lattice realization on $d = 3$ — where $d$ is uniquely self-consistent — selects the SM gauge group, the three-generation pattern, $\bar\theta = 0$, and twenty-two quantitative SM observables. The reconstruction theorem establishes the converse: observed QM, Bell violations, finite boundary entropy, and spatial isotropy together with the framework's structural assumptions uniquely determine $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ — so the mathematical description and the physics are informationally equivalent up to gauge.

The framework belongs to a family of results where self-reference under finite resources produces rigid structure: Gödel (a formal system cannot prove all truths about itself), Turing (a computer cannot decide all questions about its own behavior), OI (an embedded observer cannot access the complete state). In each case, structural impossibility determines what the system produces instead.

---

## Empirical record

The framework produces parameter-free predictions across multiple domains, all empirically tested. The most recent confirmation: JUNO's first measurement (November 2025) tested the framework's prediction $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$ at $0.07\sigma$ against the post-JUNO global fit (Capozzi et al. 2025). The associated sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ discriminates this prediction from the TM1/TM2 column-preservation patterns now under active comparison (He 2025; Zhang 2025) at sub-0.005 sum-rule precision; the self-contained paper [`Juno.md`](Juno.md) presents this result in detail.

A representative sample of empirical matches across the framework:

| Observable | Prediction | Match |
|---|---|---|
| Cabibbo angle $\lambda = 1/(\pi\sqrt{2})$ | $0.22508$ | $0.04\%$ vs PDG 2024 |
| Koide angle $\theta_0 = C_2/d^2 = 2/9$ | $0.22222$ | $0.02\%$ vs PDG 2024 |
| Solar mixing $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$ | $0.3080$ | $0.07\sigma$ vs post-JUNO global fit |
| Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ | factor $1/4$ derived | $99.999\%$ vs GW250114 |
| MOND acceleration $a_0 = cH/6$ | $1.2 \times 10^{-10}$ m/s² | <$0.5\%$ vs Milgrom |
| Higgs quartic $\lambda(M_{\rm Pl}) = 0$ | structural | $0.6\sigma$ vs measured |
| Dark sector fraction | $\sim 95\%$ | matches $\Omega_{\rm CDM} + \Omega_\Lambda$ |

Each prediction's full derivation chain and classification (structural / mass-chain / empirical / phenomenological) is documented in the relevant paper. See SM §7.6 for the full classification table.

---

## Conceptual structure

**Two types of inaccessibility.** The framework distinguishes between two reasons a quantity can be inaccessible. The hidden-sector state $h$ is *undecidable* — definite, consequential, provably inaccessible to any observer — and its inaccessibility produces quantum mechanics. The alphabet size $q$ and the deep-sector cardinality $|C_D|$ are *gauge* — different values produce identical observables, so the question of their value has no empirical content. The question "is the universe finite or infinite?" falls in the second category.

**The incompleteness family.** The framework belongs to a family of results where self-reference under finite resources produces rigid structure: Gödel (a formal system cannot prove all truths about itself), Turing (a computer cannot decide all questions about its own behavior), OI (an embedded observer cannot access the complete state). In each case, structural impossibility determines the form of what the system produces instead — undecidable propositions in arithmetic, undecidable problems in computation, quantum mechanics for embedded observers.

**Three emergences, one structural requirement.** Three apparently independent emergence stories trace to a single structural requirement: quantum mechanics emerges from C1–C3 (Main characterization theorem), general relativity emerges from the horizon trace-out (GR derivation of $\hbar$, $S_{\rm BH}$, running-vacuum form), and the arrow of time emerges from the observer's confinement to the non-equilibrium phase (Main §4.6). The observer-selection theorem shows they share a common foundation: observers satisfying C1–C3 exist only in the non-equilibrium phase of $(S, \varphi)$. QM emerges because that phase is where C1–C3 holds. GR emerges because the cosmological horizon is the natural non-equilibrium structure satisfying C2 with $\tau_B \sim H^{-1}$. The arrow of time emerges because observer-existence and horizon-expansion together supply a monotonic clock. Nothing is fundamental; everything derives, including the direction of time.

**Position relative to mainstream observer-emergent physics.** The framework's foundational claim — that observation is not external to physics — has been independently arrived at by several mainstream programs since 2022, with results that converge on the central observer-essentiality move while differing in mechanism. CLPW 2022 (JHEP 02:082) showed that adding an observer to QFT in a gravitational subregion promotes the von Neumann algebra from type III to type II$_\infty$. Maldacena 2024 (arXiv:2412.14014) demonstrated that the de Sitter sphere partition function's unphysical phase cancels exactly when an observer-with-clock is incorporated. Harlow-Usatyuk-Zhao (JHEP 02:108) and the AAIL construction (arXiv:2501.04305) argue that the closed-universe Hilbert-space dimension is determined by the observer's degrees of freedom. Slagle-Preskill 2022 (Phys. Rev. A 108:012217) constructed boundary quantum mechanics from a classical lattice model with stochastic dynamics. The present framework converges on the foundational substance — observation is not external; the algebra of observables depends on the observer; the partition structure carries physical content — while differing in mechanism: it is the unique member of this convergence in which the observer-essentiality content derives from a finite *deterministic* substratum (no extra spatial dimensions, no fundamental stochasticity), and produces a quantitative empirical record (twenty-two structural retrodictions) that the comparison programs do not currently match. The convergence is supportive context for the framework's central claims; the empirical record is what distinguishes it. Full positioning is developed in [`Main`](Main.md) §4.4.

**Hierarchical structure and universality classes.** The companion paper [`Structure`](Structure.md) articulates the framework's two-dimensional structural realism and extends it to comparison with other unification programs. The framework operates on a two-dimensional hierarchy: an observation axis (Level A axiom; Level B observer-admission; Level C universality classes; Level D OI's specific representative) and an orthogonal gauge axis (Level G1 D-gauge; Level G2 SM gauge group; Level G3 substratum gauge group $\mathcal{G}_{\rm sub}$; Level G4 universality-class equivalence). Different empirical predictions live at different intersections; falsifiability is stratified accordingly. Within this structure, the paper develops the framework's relationship to string theory: OI and string theory are not equivalent at the substratum level (OI's structural conditions A2 determinism and A5 linearity fail for matrix-model formulations), but share structural features at the partial-trace observation level (Born rule, channel-level unitarity, non-Markovian marginal, commutant gauge-invariance pattern). The intersection between the frameworks lives at a precisely-characterized level: the structural features of partial-trace observation, independent of substratum-level machinery. The framework's predictions live at multiple levels of universality — partial-trace features (most universal, shared across all embedded-observer systems), gauge-group structure (intermediate, shared across SM-reproducing classes), and OI-specific predictions like the Cabibbo angle $1/(\pi\sqrt{2})$ (most class-specific, real for OI's universality-class representative). The methodological reframing: fundamental physics as identifying the universality class of our universe through observational features, with substratum descriptions being framework-specific representations.

---

## Frequently asked questions

**Why reformulate QM at all?** Taken as fundamental, QM leaves the measurement problem unresolved, is sharply incompatible with GR (the $10^{122}$ CC hierarchy), and postulates rather than derives its own structure — Hilbert space, the Born rule, and unitarity all appear as axioms. The framework derives QM as the necessary description of an embedded observer of a deterministic substrate, recovering every quantum prediction while making these issues tractable. See Main §§4–6.

**Doesn't this revive local hidden variables, which Bell rules out?** No. The framework's substratum is not a local hidden variable in Bell's sense — Bell's theorem assumes Markovian conditional independence between measurement outcomes and hidden variables, and the hidden sector here violates this through P-indivisibility. Brandner (*Phys. Rev. Lett.* **134**, 037101, 2025) established at theorem level that this non-Markovian dynamics is the unique mechanism that reproduces quantum statistics without nonlocality or superdeterminism.

**If the dynamics is classical and deterministic, how do you get the Born rule?** Measurement is the observer's read-write cycle on the partition $V$. Reads from the visible sector produce classical outcomes; writes to the hidden sector imprint correlations that persist via the slow-bath condition (C2). The Born rule is the equilibrium distribution of this cycle — the unique stable statistics of indistinguishable-state averaging under P-indivisibility. See Main §§4–6 for the derivation.

**Doesn't Nielsen-Ninomiya forbid chiral fermions on a lattice?** NN forbids them under four specific premises, the load-bearing one being that the action must be bilinear in fermionic fields carrying a conserved chirality charge. The OI fundamental action is bosonic (the bijection $\varphi$); fermions and chirality are derived post-trace-out, by which point NN no longer applies. The "unwanted" doublers that NN forces become the three physical generations: the $T_1$ triplet of the 6-link wave-equation decomposition. See SM §4.8.1.

**How can the $10^{122}$ CC hierarchy dissolve by reinterpretation alone?** Jacobson's thermodynamic derivation of Einstein's equations shows that gravity responds to *coarse-grained* information content. On a finite-partition horizon, that's exactly the observer-accessible part. The $10^{122}$ gap is the compression ratio between the substratum's total information content and what the observer can read — the same mechanism that produces the Bekenstein-Hawking $1/4$ coefficient. See GR §§6–7.

**Generating SU(3)×SU(2)×U(1) and three generations from a cubic lattice sounds ad hoc.** The lattice is not a physical crystal — it is the coupling graph of $\varphi$, an equivalence class of structural data. Alphabet size is gauge; $d = 3$ is uniquely self-consistent; coupling-degree minimality forces $K = 2d = 6$ link directions. The cubic group $O$ acting on 6 directions has a unique irrep decomposition $T_1 \oplus E \oplus A_1$, and the commutant of the resulting coupling matrix is exactly $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ with three generations. Neither the gauge group nor the generation count is a free parameter. See SM §§3.2, 4.6, 4.7.

**How is black-hole information preserved?** The Page curve is derived at theorem level from the framework's nested trace-out, with $t_P \approx 0.646\, t_{\rm evap}$. Information moves from the visible sector to the hidden sector as the black hole evaporates; it is never lost from $(S, \varphi)$. The generalized second law follows from strong subadditivity applied to the nested partition. See GR Appendix A.

**Doesn't a finite deterministic substrate have a Boltzmann-brain problem? And what gives the arrow of time?** Both are addressed by a single structural theorem: observer partitions satisfying C1–C3 cannot exist in the equilibrium phase of $(S, \varphi)$, because $\tau_B$ is bounded by the local mixing time on equilibrium microstates and C2 ($\tau_B \gg \tau_S$) fails there. Boltzmann brains are excluded structurally — their $\tau_B \lesssim 10^{-12}$ s is six or more orders of magnitude too short. The arrow of time follows: the substratum has no arrow, but observers are confined to the non-equilibrium phase where horizon expansion provides the primary temporal structure. See Main §4.6.

**What does not dissolve.** The absolute scale of fermion masses ($m_s$), CP-violating phases, the charm-mass anomaly, and the residual electroweak hierarchy remain explicit inputs or open questions, as noted in SM §7.6 and §8.3. The framework resolves concerns specific to treating QM as fundamental; it does not eliminate every open question in particle physics.

---

## Contents

### Core papers

- **[`Main`](Main.md)** — establishes QM as the necessary description of an embedded observer of a deterministic substrate. P-indivisibility theorem, stochastic-quantum correspondence, characterization theorem, Bell violations. ([`.tex`](Main.tex), [`.pdf`](Main.pdf))

- **[`SM`](SM.md)** — derives the Standard Model from a $d=3$ cubic lattice. SU(3)×SU(2)×U(1), three generations, $\bar\theta=0$, twenty-two quantitative observables. ([`.tex`](SM.tex), [`.pdf`](SM.pdf))

- **[`GR`](GR.md)** — derives $\hbar$, the Bekenstein-Hawking entropy with the $1/4$ coefficient (confirmed by GW250114), the cosmological constant dissolution, and the dark sector phenomenology including $a_0 = cH/6$ from the cosmological horizon. ([`.tex`](GR.tex), [`.pdf`](GR.pdf))

- **[`Substratum`](Substratum.md)** — develops the reconstruction theorem and the substratum gauge group; argues QM, GR, and the arrow of time are three projections of the same finite deterministic construction. ([`.tex`](Substratum.tex), [`.pdf`](Substratum.pdf))

### Cross-framework companions

- **[`Structure`](Structure.md)** — articulates the framework's two-dimensional hierarchical structure (§2: observation hierarchy A-D × gauge hierarchy G1-G4, multi-level structural realism, prediction stratification) and develops the framework's relationship to broader unification programs in three parts. Part I (§§3-7) examines whether SM-reproducing string compactifications are gauge-equivalent representatives of OI's substratum equivalence class, with negative outcome — matrix-model formulations fail OI's structural conditions A2 (determinism) and A5 (linearity). Part II (§§8-13) develops the broader framework of universality classes of embedded observers — equivalence classes of substratum-with-observer systems under partial-trace observational equivalence, broader than OI's gauge group $\mathcal{G}_{\rm sub}$ — with the algebraic formalization adopted as principal and the observer-admission distinction formalized. Part III (§14) provides a four-feature audit (Born rule, channel-level unitarity, P-indivisibility, commutant gauge-invariance) characterizing the OI-string universality-class relationship: three features transport directly, with holographic Schwinger-Keldysh providing direct analog of OI's P-indivisibility and AdS/CFT bulk reconstruction providing direct analog of OI's Stinespring lift; the fourth transports as a pattern but not as a specific output.

### Focused presentation

- **[`Juno`](Juno.md)** — self-contained presentation of the JUNO-confirmed prediction $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$, matching the post-JUNO global fit at 0.07σ. Narrowly scoped to PMNS phenomenology with no companion-paper citations required. ([`.tex`](Juno.tex), [`.pdf`](Juno.pdf))

### Companion documents

- **[`Explainer`](Explainer.md)** — full-argument overview with detailed proof walkthroughs, observational confrontation, and FAQ. ([`.tex`](Explainer.tex), [`.pdf`](Explainer.pdf))

- **[`Complexity`](Complexity.md)** — traces the structural chain from $(S, \varphi)$ to organic chemistry, the origin of life as a molecular C1–C3 system, and AI as a self-referential closure. ([`.tex`](Complexity.tex), [`.pdf`](Complexity.pdf))

- **[`Medicine`](Medicine.md)** — applies C1–C3 to enzyme kinetics, identifies *memory asymmetry* as a therapeutic axis, presents 29 testable predictions across cancer, neurodegeneration, antibiotic resistance, and other domains. ([`.tex`](Medicine.tex), [`.pdf`](Medicine.pdf))

### Lattice Monte Carlo code

Source code for the lattice computations reported in SM §§6–7 (gauge-coupling thresholds, scalar-density renormalization $Z_S$, dynamical fermion HMC, Higgs effective potential) lives in [`oi_lattice_code/`](oi_lattice_code/). See `oi_lattice_code/README.md` for build instructions, per-file documentation, and reproduction recipes.

**License.** All source code under `oi_lattice_code/` is released under the MIT License — see [`LICENSE`](LICENSE). The accompanying papers are research manuscripts and are not licensed under MIT; cite the relevant paper if you use the framework or its results, and cite this repository if you use or adapt the lattice utilities.

**Citation / archive.** The source code and accompanying papers are archived on Zenodo with concept DOI [10.5281/zenodo.19060318](https://doi.org/10.5281/zenodo.19060318), which always resolves to the latest version. Specific per-release DOIs are minted at release time.

## Key Results

| # | Result | Status | Source |
|---|---|---|---|
| 1 | QM ⟺ embedded observation under C1–C3 | theorem | Main §3.4 |
| 2 | $\hbar = c^3 \varepsilon^2/(4G)$ from horizon thermal self-consistency, $\varepsilon = 2 l_p$ uniquely | theorem | GR §§3–4 |
| 3 | Bekenstein-Hawking entropy with $1/4$ coefficient (GW250114 at 99.999%) | theorem | GR §5 |
| 4 | Cosmological constant dissolution: $10^{122}$ ratio = $S_{\rm dS}$ compression ratio | theorem | GR §6 |
| 5 | Wave equation uniquely selected; produces all inputs for Einstein's equations | theorem | SM §3 + GR §3 |
| 6 | SM gauge group SU(3)×SU(2)×U(1), 3 generations, hypercharges, $\bar\theta = 0$ | theorem | SM §§4, 5 |
| 7 | Twenty-two SM observables match observation across CKM, mass, PMNS sectors | structural + empirical | SM §7 |
| 8 | Dark sector $\sim 95\%$, $a_0 = cH/6$, Bullet Cluster, CMB peaks | theorem (total budget); structural (specific magnitudes) | GR §7 |
| 9 | Page curve from nested trace-out, $t_P \approx 0.646\, t_{\rm evap}$ | theorem | GR Appendix A |
| 10 | Observer selection theorem: C1–C3 systems exist only out of equilibrium → arrow of time, no Boltzmann brains | theorem | Main §4.6 |
| 11 | Reconstruction theorem: observed physics + A1–A6 → $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ uniquely | theorem | Substratum §§3–4 |
| 12 | Structural preconditions for organic chemistry, RNA world as first molecular C1–C3, viable parameter fraction $\sim 16\%$ | structural chain + statistical | Complexity |
| 13 | Non-Markovian dynamics in biology, memory asymmetry as therapeutic axis, 29 testable predictions | predictions | Medicine |

The classification (structural / mass-chain / empirical / phenomenological) for the SM observables is documented in SM §7.6.

## The Bidirectional Correspondence

The forward derivation and reconstruction theorem together establish that the framework closes in both directions: $(S, \varphi)$ determines observed physics, and observed physics together with structural assumptions A1–A6 uniquely determines $[(S, \varphi)]/\mathcal{G}_{\rm sub}$.

**Forward — major branches.** From $(S, \varphi)$ as a finite lossless memory with bounded coupling and statistical isotropy:

```
(S, φ) ─→ d = 3 self-consistent (SM)
       ─→ QM emergence under C1–C3 (Main §3.4)
       ─→ Wave equation uniquely selected (SM §3)
       ├── ℏ = c³ε²/(4G), S_BH with 1/4, CC dissolution, GR (GR §§3–6)
       ├── Cubic group → SU(3)×SU(2)×U(1), 3 generations, θ̄ = 0 (SM §§4–5)
       ├── 22 SM observables: gauge couplings, CKM, Koide, PMNS, m_t, m_b/m_τ (SM §§6–7)
       ├── Dark sector ~95%, a₀ = cH/6, Bullet Cluster, CMB peaks (GR §7)
       ├── Page curve with t_P ≈ 0.646 t_evap (GR Appendix A)
       ├── Observer selection → arrow of time, no Boltzmann brains (Main §4.6)
       ├── Structural preconditions for organic chemistry, RNA world (Complexity)
       └── Molecular C1–C3 → non-Markovian pharmacology (Medicine)
```

**Three-level gauge hierarchy.** The framework's gauge structure is layered:

```
Level 3: Substratum gauge group 𝒢_sub (Substratum §4)
         {state relabeling, alphabet change, deep-sector size, graph isomorphism}
                │ trace-out
Level 2: SM gauge group SU(3)×SU(2)×U(1) (SM §4)
         {commutant of coupling matrix M with multiplicities (3,2,1)}
                │ Hamiltonian restriction
Level 1: D-gauge H ↦ DHD† (GR §3.3)
         {diagonal unitary basis rephasing of emergent Hamiltonian}
```

**Reverse — three stages.** From observed physics back to the substratum equivalence class:

```
Observed QM + Bell + finite boundary entropy + spatial isotropy + A1–A6
                │
Stage 1: Stinespring + characterization → (S, φ) with C1–C3 (Main)
Stage 2: Coupling graph + dynamics selection → d=3, wave eq., SM structure (SM)
Stage 3: Thermal self-consistency → ℏ, ε = 2l_p, all emergent constants (GR)
                │
Output: [(S, φ)] / 𝒢_sub uniquely determined (Substratum §§3–4, Theorem 23)
```

The reconstruction map has kernel $\mathcal{G}_{\rm sub}$ — everything outside the equivalence class is fixed; everything inside is gauge. Whether $(S, \varphi)$ *is* reality or *describes* reality is provably undecidable.

## Contact

Alex Maybaum — Independent Researcher
[LinkedIn](https://www.linkedin.com/in/amaybaum)
