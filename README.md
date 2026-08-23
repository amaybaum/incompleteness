# The Incompleteness of Observation

**Author:** Alex Maybaum  
**Date:** May 2026  
**Classification:** Theoretical Physics / Foundations

This repository develops a single framework across five core papers:

- **Main** — proves the exact finite-horizon equivalence $S \iff D \iff Q_{\mathrm{fb}}$ — stochastic laws ⟺ finite reversible deterministic realizations ⟺ fixed-basis unitary/Born representations — together with the universal hidden-memory theorem and the recurrence result that genuine C4 readback forces global indivisibility on a fixed finite representative. The coherent instrument/composite lift remains open; Bell-completion and gravity-layer bridges are tracked separately.
- **SM** — develops the $d=3$ simple-cubic Standard-Model branch. Its new exact result is observer-level: finite equivariant projection preserves cubic symmetry through memory and forbids quadratic anisotropy in the scalar symbol. The normalized $A/(2d)$ kernel additionally requires observer-level center-freedom. The exact six-link representation decomposes as $3\oplus2\oplus1$, while its identification with a single physical gauge carrier is the named H-link bridge (and the custodial stabilizer reading H-cust).
- **GR** — derives the gravitational sector from the cosmological horizon
- **Substratum** — ties these into a single construction at the substratum level
- **Structure** — develops the framework's hierarchical structural realism and universality classes of embedded observers

A note on "derives" throughout this repository: the framework forces a large amount of structure *given* its commitments (cubic lattice, wave-equation dynamics, the C1–C4 observer architecture), several of which are empirically selected or definitional rather than derived from first principles. The accurate one-line description is that the framework is a tight *compression* of known physics onto a small set of commitments — a claim about the unity of physics — rather than a derivation of physics from the bare fact of observation. This is developed in book §4.7 and SM §8.3.

A self-contained paper, **Juno**, presents the parameter-free value $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$ — a retrodiction matching the post-JUNO global fit at $0.07\sigma$, with JUNO's design-lifetime precision providing the pre-registered forward test. See [`papers/Juno.md`](papers/Juno.md).

A book-length treatment, **The Incompleteness of Observation: A Unified Framework from Quantum Mechanics to Computational Biology**, develops the same framework across 20 chapters with expanded exposition and back matter. See [`book/`](book/).

The full file list is in [Contents](#contents).


## Status of the material: core vs conjectural extensions

The framework's empirical weight lies in its **physics core**. Its applications to biology, medicine, consciousness, and computational complexity are **conjectural extensions** — they apply the core framework to new domains, are offered as conjectures to be tested rather than established results, and carry no evidential weight for the core, which stands or falls independently on its physics. Each such chapter and paper now opens with an explicit "Status — conjectural extension" banner stating its test-or-break condition.

**Core (physics — where the framework's weight lies):** Main, SM, Structure, Substratum, GR, Methodology, Juno, and the corresponding physics chapters. (The Explainer is superseded by the book and frozen.)

**Conjectural extensions:**

- **Medicine** (`papers/Medicine.md`, Chapter 16) — structural retrodictions (the Rett-syndrome reversibility of Guy et al. 2007 predates the framework, and is a consistency check rather than a confirmation) plus untested forward predictions.
- **Bioinformatics / evolutionary biology** (`papers/Bioinformatics.md`, Chapter 17) — explicitly retrodictive; the Hurst-exponent discriminator does not by itself separate the framework from a mundane null.
- **Quantum computation & complexity** (`papers/Computation.md`, `papers/Complexity.md`, Chapter 14) — the BQP-realization claim is a theoretical conjecture, not a proven correspondence.
- **Consciousness** (Chapter 18) — a structural correspondence offered as a possibility, with no empirical test proposed.

This tiering mirrors the four-layer derivational classification of book §4.7 and SM §8.3.



## Current theorem milestone: finite observer isotropy

The current research milestone does **not** assume quantum mechanics is fundamental. Let $U$ be the Koopman operator of the finite bijection and $P$ the observer projection. If both commute with the cubic spatial action, then the exact projected Markov part and every memory kernel $BD^mC$ inherit that symmetry. Any translation-invariant scalar kernel therefore has an isotropic quadratic Fourier symbol, $a-b|\mathbf k|^2+O(k^4)$, although cubic anisotropy remains at quartic order. If the observer-level Markov part is moreover nearest-neighbor, constant-preserving and center-free, its unique weights are $1/(2d)$ on the signed neighbors, giving the $A/(2d)$ operator already used by the spectral code. Microscopic center independence alone does **not** imply this observer-level center-free condition; a reversible swap is the exact counterexample.

The physical-carrier frontier is separate: the six signed SC links decompose exactly as $3\oplus2\oplus1$, but the former coupling-degree proof that these must be the complete physical carrier is not established. **H-link** names the carrier identification $V_{\mathrm{phys}}\cong V_{\mathrm{link}}\otimes\mathbb C^m$; the single-copy clause $m=1$ gives $K=6$. **H-cust** names the custodial kinetic/condensate premise used by the stabilizer route.

## Repository layout


```
incompleteness/
├── papers/                    Twelve research papers (.md, .tex, .pdf) + lattice Monte Carlo code
│   ├── Main, SM, GR, Substratum, Structure   (core papers)
│   ├── Juno                                  (focused presentation)
│   ├── Methodology                           (foundations / philosophy of physics)
│   ├── Explainer, Complexity, Computation, Medicine, Bioinformatics  (companion documents)
│   └── oi_lattice_code/                      (source code for SM §§6–7 lattice computations)
├── book/                      Book manuscript: 20 chapters, 4 parts, full back matter
└── README.md, LICENSE
```

---

## Overview

The universe is completely described by a lossless memory with finite read-write access. Physics is what that memory looks like from inside.

A *lossless memory* is a system whose states evolve by a reversible rule. Every state has one predecessor and one successor; no information is created or destroyed. The past is always recoverable from the present. Formally, this is a finite set $S$ of distinguishable states and a bijection $\varphi: S \to S$. The observer has access to only a bounded portion of the state, called the *visible sector*. Each step updates both sectors at once, but the observer reads only the visible part. Correlations written into the hidden sector persist there and return on later steps. This read-write cycle is what produces the memory-bearing statistics quantum mechanics represents — not passive observation.

The framework begins with a single empirical fact — *observation occurs* — formalized as a definition: an observation is a triple $(S, \varphi, V)$ consisting of a total system, a deterministic dynamics, and an embedded observer. No quantum postulates appear. Three structural lemmas follow (finiteness, causal partition, unique measure), from which non-Markovian visible dynamics emerge under four conditions on the hidden sector — coupling (C1), memory persistence (C2), high capacity (C3), and history readback (C4) — with the fixed-basis quantum representation supplied internally and universally ($S \iff D \iff Q_{\mathrm{fb}}$, Main §3.4) and the compressed form via the imported correspondence under (T).

The theorem becomes physics at the cosmological horizon, where stress-energy conservation enforces C1, the universe-vs-laboratory timescale ratio enforces C2, and the $\sim 10^{122}$ horizon degrees of freedom enforce C3. From this single realization, the framework derives $\hbar$ from thermal self-consistency, recovers the Bekenstein-Hawking entropy with the $1/4$ factor (derived; GW250114 confirms the classical area theorem, which the framework preserves), dissolves the $10^{122}$ cosmological constant discrepancy as the information compression ratio of the trace-out, and produces the dark sector phenomenology including the MOND acceleration scale $a_0 = cH/6$. On the $d=3$ cubic branch, the six geometric links have an exact $(3,2,1)$ representation and the downstream SM calculations remain sharp conditional tests. Identifying that geometry with one physical gauge carrier ($K=6$) is H-link single-copy; the condensate-stabilizer route is H-cust, and the previously named spin/chirality assumptions remain where stated. The three-generation and $N_f=6$ numerical chains inherit those carrier conditions. The reconstruction theorem establishes a scoped converse: under the stated empirical/structural inputs, M1-T, C2-mixing and Lemma 24.1's completeness step, it uniquely fixes the **local propagating lattice/gauge residue** up to substratum gauge. Bell violation is separate. M1-B retains measurement independence and uses preparation-indexed ontic parameter dependence on the state-dependent graph $G(x)$; H-Bell is the open requirement that those prepared graphs preserve operational no-signaling and the metric/Ollivier--Ricci continuum limit. Bell-inclusive full-substratum uniqueness is not established.

The framework belongs to a family of results where self-reference under finite resources produces rigid structure: Gödel (a formal system cannot prove all truths about itself), Turing (a computer cannot decide all questions about its own behavior), OI (an embedded observer cannot access the complete state). In each case, structural impossibility determines what the system produces instead.

---

## Empirical record

The framework produces parameter-free predictions across multiple domains, all empirically tested. The sharpest single match is retrodictive: JUNO's first measurement (November 2025) agrees at $0.07\sigma$ with the parameter-free value $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$ (Capozzi et al. 2025 post-JUNO global fit); the value was derived in 2026, after the measurement — a retrodiction, with JUNO's design-lifetime precision providing the pre-registered forward test. The associated sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ discriminates this prediction from the TM1/TM2 column-preservation patterns now under active comparison (He 2025; Zhang 2025) at sub-0.005 sum-rule precision; the self-contained paper [`Juno.md`](papers/Juno.md) presents this result in detail.

A representative sample of empirical matches across the framework (see [`papers/Juno.md`](papers/Juno.md) for the JUNO presentation):

| Observable | Prediction | Match |
|---|---|---|
| Cabibbo angle $\lambda = 1/(\pi\sqrt{2})$ | $0.22508$ | $0.04\%$ vs PDG 2024 |
| Koide angle $\theta_0 = C_2/d^2 = 2/9$ | $0.22222$ | $0.02\%$ vs PDG 2024 |
| Solar mixing $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$ | $0.3080$ | $0.07\sigma$ vs post-JUNO global fit |
| Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ | factor $1/4$ derived | area theorem consistent (GW250114); $1/4$ untested directly |
| MOND acceleration $a_0 = cH/6$ | $1.2 \times 10^{-10}$ m/s² | <$0.5\%$ vs Milgrom |
| Higgs quartic $\lambda(M_{\rm Pl}) = 0$ | structural | $0.6\sigma$ vs measured |
| Dark sector fraction | $\sim 95\%$ | matches $\Omega_{\rm CDM} + \Omega_\Lambda$ |

Each prediction's full derivation chain and classification (structural / mass-chain / empirical / phenomenological) is documented in the relevant paper. See SM §7.6 for the full classification table.

---

## Conceptual structure

**Two types of inaccessibility.** The framework distinguishes between two reasons a quantity can be inaccessible. The hidden-sector state $h$ is *undecidable* — definite, consequential, provably inaccessible to any observer — and its inaccessibility produces the memory-bearing dynamics quantum mechanics represents. The alphabet size $q$ and the deep-sector cardinality $|C_D|$ are *gauge* — different values produce identical observables, so the question of their value has no empirical content. The question "is the universe finite or infinite?" falls in the second category.

**The incompleteness family.** The framework belongs to a family of results where self-reference under finite resources produces rigid structure: Gödel (a formal system cannot prove all truths about itself), Turing (a computer cannot decide all questions about its own behavior), OI (an embedded observer cannot access the complete state). In each case, structural impossibility determines the form of what the system produces instead — undecidable propositions in arithmetic, undecidable problems in computation, and — for embedded observers — the memory-bearing non-Markovian statistics whose universal quantum representation the framework supplies.

**Open foundational question — the axiom count.** The framework's foundation is presented as a *two-axiom observation base* (tokened differentiation occurs; differentiation recurs). One element of that distillation is under review: whether the observer's embeddedness — its status as a proper part $V \subsetneq S$ of a larger whole — is a lemma of the first axiom or a third axiom in its own right. The question turns on a point about what the primitive "tokened differentiation" means, and is presentational rather than empirical: it changes no prediction the framework makes, only how the foundation's commitments are counted and described. It is flagged in `Main` §1.2, `Methodology` §4.2, `Substratum` §1.1, and `book/ch01`; the two-axiom presentation is the framework's working choice with this proviso noted, not a closed result.

**Three emergences, one structural requirement.** Three apparently independent emergence stories trace to a single structural requirement: the memory-bearing sector emerges from C1–C4, its quantum representation universal (Main characterization theorem), general relativity emerges from the horizon trace-out (GR derivation of $\hbar$ and $S_{\rm BH}$, with geometry-dependent dark-energy bookkeeping read in the Type II channel), and the arrow of time emerges from the observer's confinement to the non-equilibrium phase (Main §4.6). The observer-selection theorem shows they share a common foundation: observers satisfying C1–C4 are excluded from the sufficiently fast-mixing equilibrium phase of $(S, \varphi)$ — the bound is $\tau_B\le\tau_{\rm mix}$, so contradicting C2-slow needs $\tau_{\rm mix}\ll\tau_S$, and a slowly mixing equilibrium can host observers. The memory-bearing sector — the content quantum mechanics represents — emerges because that phase is where C1–C4 holds. GR emerges because the cosmological horizon is the natural non-equilibrium structure satisfying C2 with $\tau_B \sim H^{-1}$. The arrow of time emerges because observer-existence and horizon-expansion together supply a monotonic clock. Nothing is fundamental; everything derives, including the direction of time.

**Position relative to mainstream observer-emergent physics.** The framework's foundational claim — that observation is not external to physics — has been independently arrived at by several mainstream programs since 2022, with results that converge on the central observer-essentiality move while differing in mechanism. CLPW 2022 (JHEP 02:082) showed that adding an observer to QFT in a gravitational subregion promotes the von Neumann algebra from type III to type II$_\infty$. Maldacena 2024 (arXiv:2412.14014) demonstrated that the de Sitter sphere partition function's unphysical phase cancels exactly when an observer-with-clock is incorporated. Harlow-Usatyuk-Zhao (JHEP 02:108) and the AAIL construction (arXiv:2501.04305) argue that the closed-universe Hilbert-space dimension is determined by the observer's degrees of freedom. Slagle-Preskill 2022 (Phys. Rev. A 108:012217) constructed boundary quantum mechanics from a classical lattice model with stochastic dynamics. The present framework converges on the foundational substance — observation is not external; the algebra of observables depends on the observer; the partition structure carries physical content — while differing in mechanism: it is the unique member of this convergence in which the observer-essentiality content derives from a finite *deterministic* substratum (no extra spatial dimensions, no fundamental stochasticity), and produces a quantitative empirical record (twenty-two classified Standard Model retrodictions, seven of them parameter-free structural) that the comparison programs do not currently match. The convergence is supportive context for the framework's central claims; the empirical record is what distinguishes it. Full positioning is developed in [`Main`](papers/Main.md) §4.4.

**Hierarchical structure and universality classes.** The [`Structure`](papers/Structure.md) paper articulates the framework's two-dimensional structural realism and extends it to comparison with other unification programs. The framework operates on a two-dimensional hierarchy: an observation axis (Level A axiom; Level B observer-admission; Level C universality classes; Level D OI's specific representative) and an orthogonal gauge axis (Level G1 D-gauge; Level G2 SM gauge group; Level G3 substratum gauge group $\mathcal{G}_{\rm sub}$; Level G4 universality-class equivalence). Different empirical predictions live at different intersections; falsifiability is stratified accordingly (Structure §12.4). Within this structure, the paper develops the framework's relationship to string theory: OI and string theory are not equivalent at the substratum level (OI's structural conditions A2 determinism and A5 linearity fail for matrix-model formulations), but share structural features at the partial-trace observation level (Born rule, channel-level unitarity, non-Markovian marginal, commutant gauge-invariance pattern). The intersection between the frameworks lives at a precisely-characterized level: the structural features of partial-trace observation, independent of substratum-level machinery. The paper also develops the framework's **no-GUT structural prediction** (Structure §12.5, drawing on SM §6.7 and §8.7): OI's gauge-emergence is *direct* from cubic-commutant decomposition with no intermediate large gauge group at any scale, structurally distinct from every standard string-phenomenology route. The empirical consequences (Planck-suppressed proton decay, no GUT-mechanism monopoles, no GUT-chain cosmic strings, non-unification of gauge couplings) moderately favor OI over standard GUT scenarios across current Super-K, LHC SUSY, and NANOGrav data. The framework's predictions live at multiple levels of universality — partial-trace features (most universal, shared across all embedded-observer systems), gauge-group structure (intermediate, shared across SM-reproducing classes), and OI-specific predictions like the Cabibbo angle $1/(\pi\sqrt{2})$ (most class-specific). Structure §13.1.1.1 specifies a converged comparison protocol for testing OI/string algebra-channel pair *-isomorphism against a chosen heterotic line-bundle compactification; Structure §13.3 catalogs five open research questions (neutrino mass scale, hierarchy problem, leptogenesis quantitative, non-perturbative completeness) flagging the framework's substantive research frontier.

---

## Frequently asked questions

**Why reformulate QM at all?** Taken as fundamental, QM leaves the measurement problem unresolved, is sharply incompatible with GR (the $10^{122}$ CC hierarchy), and postulates rather than derives its own structure — Hilbert space, the Born rule, and unitarity all appear as axioms. The framework identifies QM with the description forced on an embedded observer of a deterministic substrate — the fixed-basis representation supplied internally and universally, the memory-bearing sector carrying the discriminating content (Main §3.4) — recovering quantum predictions at the transition-statistics layer, with the operational instrument algebra the stated frontier (Main §3.2). See Main §3.

**Doesn't this revive local hidden variables, which Bell rules out?** Bell applies directly to the deterministic completion. If a response-complete pre-setting microstate is both measurement-independent and parameter-independent across the two wings, then the model is Bell-local and $|S_{\rm CHSH}|\le2$. The framework therefore does **not** claim that graph locality plus hidden memory evades Bell. It declines the measurement-dependent/superdeterministic branch and instead gives up **ontic parameter independence** for Bell-violating substrata: one wing's microstate response may depend on the remote setting, while the averaged operational statistics remain no-signaling. The stochastic causal-local indivisible construction of [24] can still obey the Tsirelson bound, but that weaker stochastic statement is not the locality structure of the response-complete deterministic completion.

**If the dynamics is classical and deterministic, how do you get the Born rule?** At the finite observable-law level the Born form is part of an exact equivalent description: every finite-horizon stochastic law has a fixed-basis unitary representation whose probabilities are $|U|^2$, and every finite reversible realization supplies such a representation ($S \iff D \iff Q_{\mathrm{fb}}$, Main §3.4). What is not yet proved is that this fixed-basis representation uniquely extends, for all coherent interventions and composites at once, to the standard local quantum instrument algebra. The cosmological realization adds a mechanism proposal: measurement as the observer's read-write cycle on the partition $V$, with equilibrium Born statistics; that mechanism is additional physical interpretation, not needed for the finite representation equivalence.

**Doesn't Nielsen-Ninomiya forbid chiral fermions on a lattice?** NN forbids them under four specific premises, the load-bearing one being that the action must be bilinear in fermionic fields carrying a conserved chirality charge. The OI fundamental action is bosonic (the bijection $\varphi$); fermions and chirality are derived post-trace-out, by which point NN no longer applies. The "unwanted" doublers appear as the $T_1$ triplet of the 6-link wave-equation decomposition — three candidate matter sectors. Reading them as three *physical* generations rides H-spin' (SM §4.7), whose free-kernel and 4D-staggered routes are both settled negative; the unconditional statement is the $1 \oplus 3$ decomposition. See SM §4.8.1.

**How can the $10^{122}$ CC hierarchy dissolve by reinterpretation alone?** Jacobson's thermodynamic derivation of Einstein's equations shows that gravity responds to *coarse-grained* information content. On a finite-partition horizon, that's exactly the observer-accessible part. The $10^{122}$ gap is the compression ratio between the substratum's total information content and what the observer can read — the same mechanism that produces the Bekenstein-Hawking $1/4$ coefficient. See GR §§6–7.

**Generating SU(3)×SU(2)×U(1) and three candidate matter sectors from a cubic lattice sounds ad hoc.** The lattice is not a physical crystal — it is the coupling graph of $\varphi$, an equivalence class of structural data. Alphabet size is gauge; $d = 3$ is uniquely self-consistent; the geometry supplies six signed nearest-neighbor link directions, while identifying them with a single physical carrier ($K=6$) is H-link single-copy. The cubic group $O$ acting on 6 directions has a unique irrep decomposition $T_1 \oplus E \oplus A_1$, and the commutant of the resulting coupling matrix is exactly $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ with three candidate matter sectors — three physical generations under H-spin' (SM §4.7), whose free-kernel and 4D routes are settled negative. The geometric $3\oplus2\oplus1$ decomposition is fixed; the physical carrier and sector-count reading remain conditional on H-link/H-cust and the matter-sector hypotheses named in SM. See SM §§3.2, 4.6, 4.7.

**How is black-hole information preserved?** The Page curve is derived at theorem level from the framework's nested trace-out, with $t_P \approx 0.646\, t_{\rm evap}$. Information moves from the visible sector to the hidden sector as the black hole evaporates; it is never lost from $(S, \varphi)$. The generalized second law follows from strong subadditivity applied to the nested partition. See GR Appendix A.

**Doesn't a finite deterministic substrate have a Boltzmann-brain problem? And what gives the arrow of time?** Both are addressed by a single structural theorem, conditional on the effective-mixing hypothesis (Main §4.6 (EM)) —: observer partitions satisfying C1–C4 cannot exist in the equilibrium phase of $(S, \varphi)$, because $\tau_B$ is bounded by the local mixing time on equilibrium microstates and C2 ($\tau_B \gg \tau_S$) fails there. Boltzmann brains are excluded conditionally: under (EM), if the equilibrium partition's mixing time satisfies $\tau_{\text{mix}}(\Sigma_{\text{BB}}) \ll \tau_S$ then C2 fails there, and C4 with it by the erasure lemma — C4 being the condition the characterization requires. The $\hbar/k_BT \sim 10^{-12}$ s figure is the illustrative (GT) estimate (Main §4.6) and can fail for protected slow modes. The arrow of time follows: the substratum has no arrow, but observers are confined to the non-equilibrium phase where horizon expansion provides the primary temporal structure. See Main §4.6.

**What does not dissolve.** The absolute scale of fermion masses ($m_s$), CP-violating phases, the charm-mass anomaly, the residual electroweak hierarchy, and the cross-charged scale $M_X$ (a solution-level parameter; the decoupling calculation that would confine it is reported and not independently verified, SM §3.1) remain explicit inputs or open questions, as noted in SM §7.6 and §8.3. The framework resolves concerns specific to treating QM as fundamental; it does not eliminate every open question in particle physics.

---

## Contents

All research papers live in [`papers/`](papers/).

### Core papers

- **[`Main`](papers/Main.md)** — proves the per-horizon equivalence — accessible non-Markovianity ⟺ deterministic (C1)/(C3)/(C4) realization — and the finite-horizon representation equivalence $S \iff D \iff Q_{\mathrm{fb}}$ (the quantum representation internal and universal, the compressed form via the imported correspondence under the translation hypothesis (T)); the universal hidden-memory theorem constrains every deterministic completion, and (C2)'s necessity is the conditional physical-memory theorem. Minimal explicit model, stated falsification conditions. ([`.tex`](papers/Main.tex), [`.pdf`](papers/Main.pdf))
- **[`SM`](papers/SM.md)** — derives the Standard Model from a $d=3$ cubic lattice. SU(3)×SU(2)×U(1); threefold taste multiplicity (candidate generations under H-spin' — free kernel and 4D route refuted, condensate-dressed form open; chirality under H-χ' — sharpened, the minimal embedding certified vector-like, mechanism class nonempty with dynamical selection open); strong CP open ($T$-invariance fixes $\theta\in\{0,\pi\}$ and reciprocal transition counts, not $\bar\theta$; H-top, H-det); twenty-two quantitative observables. ([`.tex`](papers/SM.tex), [`.pdf`](papers/SM.pdf))

- **[`GR`](papers/GR.md)** — derives $\hbar$, the Bekenstein-Hawking entropy with the $1/4$ coefficient (derived; GW250114 tests the area theorem, not the coefficient), the cosmological constant dissolution, and the dark sector phenomenology including $a_0 = cH/6$ from the cosmological horizon. The Tier 1 results ($\hbar$, area law, CC dissolution, Type II RVM functional form) are formalized at the universality-class level: they hold for any horizon-bounded embedded-observer system satisfying the structural conditions S1-S4, with OI providing one specific realization (§8.5). The $\hbar$ chain's boost-structure prerequisite is discharged in closed form: free-level cone exact only on body diagonals (H-Hawking), KMS robustness at $\mathcal{O}((\epsilon\kappa/c^2)^2)$, and a certified symmetric-point matching theorem for the radiative splitting, with the running part resting on a reported one-loop calculation that is not independently verified (GR §8.5; SM §3.1, F13). The paper also carries the reconstruction-gauge form of the vacuum-offset claim (§6) and a scope preamble on what the classical tests test (§7). ([`.tex`](papers/GR.tex), [`.pdf`](papers/GR.pdf))

- **[`Substratum`](papers/Substratum.md)** — develops the reconstruction theorem and the substratum gauge group; argues QM, GR, and the arrow of time are projections of one deterministic construction. Under E1–E7 and A1–A6 with M1-T, the C2-mixing hypothesis and Lemma 24.1's completeness step, the reconstruction uniquely fixes the **local propagating lattice/gauge residue** up to substratum gauge. Bell is separate: M1-B retains measurement independence, the reference nearest-neighbor graph is Bell-local, and the adopted route uses preparation-indexed adjacency (or equivalent ontic parameter dependence) in the existing state-dependent $G(x)$. H-Bell is the open metric/Ollivier--Ricci stability condition for those prepared graphs; Bell-inclusive uniqueness is not proved. Three independent forward filters select $d = 3$: propagating gravity ($d \geq 3$), stable matter ($d \leq 3$), boundary-entropy concordance ($d = 3$ exactly) — a self-consistency selection, independently anchored empirically by the observed gauge group. ([`.tex`](papers/Substratum.tex), [`.pdf`](papers/Substratum.pdf))

- **[`Structure`](papers/Structure.md)** — articulates the framework's two-dimensional hierarchical structure (§2: observation hierarchy A-D × gauge hierarchy G1-G4, multi-level structural realism, prediction stratification) and develops the framework's relationship to broader unification programs in three parts. Part I (§§3-7) examines whether SM-reproducing string compactifications are gauge-equivalent representatives of OI's substratum equivalence class, with negative outcome — matrix-model formulations fail OI's structural conditions A2 (determinism) and A5 (linearity). Part II (§§8-13) develops the broader framework of universality classes of embedded observers — equivalence classes of substratum-with-observer systems under partial-trace observational equivalence, broader than OI's gauge group $\mathcal{G}_{\rm sub}$ — with the algebraic formalization adopted as principal and the observer-admission distinction formalized; §13 develops seven open research questions, including per-condition A1–A6 analysis of LQG, causal sets, and asymptotic safety against OI's structural conditions, finding that A2 (determinism) is the most discriminating condition across candidate programs. Part III (§14) provides a four-feature audit (Born rule, channel-level unitarity, P-indivisibility, commutant gauge-invariance) characterizing the OI-string universality-class relationship: three features transport directly, with holographic Schwinger-Keldysh providing direct analog of OI's P-indivisibility and AdS/CFT bulk reconstruction providing direct analog of OI's Stinespring lift; the fourth transports as a pattern but not as a specific output. ([`.tex`](papers/Structure.tex), [`.pdf`](papers/Structure.pdf))

### Focused presentation

- **[`Juno`](papers/Juno.md)** — self-contained presentation of the parameter-free $\sin^2\theta_{12}$ value (a retrodiction with a pre-registered design-lifetime forward test), namely $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$, matching the post-JUNO global fit at 0.07σ. Narrowly scoped to PMNS phenomenology with no companion-paper citations required. ([`.tex`](papers/Juno.tex), [`.pdf`](papers/Juno.pdf))

### Foundations and methodology

*Developmental draft. This document articulates the framework's foundational commitment and methodological posture; it is preprint-stage and under active development, and is catalogued here as such.*

- **[`Methodology`](papers/Methodology.md)** — *Physics Modulo Gauge*: articulates the framework's methodology for a philosophy-of-physics readership, in four parts. **Part I** — the foundational treatment — distills the framework's foundational commitment into the *two-axiom observation base*: Axiom 1 (tokened differentiation occurs — indubitable, conceptually primitive) and Axiom 2 (differentiation recurs — a substantive posit, not derivable from Axiom 1 though presupposing it), with relationality, the proper-part structure, the existence of a dynamics, determinism, finiteness, and bijectivity recovered as lemmas of Axiom 1, and a no-go result that the recurrence of differentiation is not derivable from differentiation alone. **Parts II–IV** develop constructive structural realism via the reconstruction and gauge-classification theorems; the engagement with the no-go results of quantum foundations through a single architectural feature, verified theorem by theorem; and "physics modulo gauge" as a general methodology. Companion to the core papers, not a replacement. Developmental draft. ([`.tex`](papers/Methodology.tex), [`.pdf`](papers/Methodology.pdf))

### Companion documents

- **[`Explainer`](papers/Explainer.md)** — full-argument overview, now **superseded by the book** and frozen at the 2026-07-26 revision (retained for its D-gauge completeness walkthrough and summary tables, pending their book incorporation). ([`.tex`](papers/Explainer.tex), [`.pdf`](papers/Explainer.pdf))

- **[`Complexity`](papers/Complexity.md)** — traces the structural chain from $(S, \varphi)$ to organic chemistry, the origin of life as a molecular C1–C4 system, and Darwinian evolution. Companion to [`Computation`](papers/Computation.md), which continues the chain from evolution onward. ([`.tex`](papers/Complexity.tex), [`.pdf`](papers/Complexity.pdf))

- **[`Computation`](papers/Computation.md)** — continues the structural chain from evolution through information processing, neural computation, semiconductor physics, and AI as embedded-observer construction. Develops the BQP characterization theorem for embedded observers and the framework's position on the P vs NP question: structural silence with empirical content concentrated at the BQP boundary. Proposes three condition-based research directions for complexity-theoretic refinements within BQP — geometric structure on the substratum lattice, task-specific quantum advantage correlated with problem globality, and gauge equivalence as a possible physical account of polynomial-time reducibility. ([`.tex`](papers/Computation.tex), [`.pdf`](papers/Computation.pdf))

- **[`Medicine`](papers/Medicine.md)** — applies C1–C4 to enzyme kinetics, identifies *memory asymmetry* as a therapeutic axis, presents 29 testable predictions across cancer, neurodegeneration, antibiotic resistance, and other domains. ([`.tex`](papers/Medicine.tex), [`.pdf`](papers/Medicine.pdf))

- **[`Bioinformatics`](papers/Bioinformatics.md)** — applies C1–C4 to computational biology methodology, explaining documented failure modes in trajectory inference, gene regulatory network inference, perturbation prediction, and multi-omics integration through the information-theoretic ceiling of transcriptome-only methods. 22 testable predictions for methodological development. ([`.tex`](papers/Bioinformatics.tex), [`.pdf`](papers/Bioinformatics.pdf))

### Lattice Monte Carlo code

Source code for the lattice computations reported in SM §§6–7 (gauge-coupling thresholds, scalar-density renormalization $Z_S$, dynamical fermion HMC, Higgs effective potential) lives in [`papers/oi_lattice_code/`](papers/oi_lattice_code/). See the per-subdirectory README files (e.g., `gauge/AB_derivation/README.md`, `gauge/c2_strict_2loop/README.md`) for build instructions and reproduction recipes.

### Book manuscript

A book-length treatment, **The Incompleteness of Observation: A Unified Framework from Quantum Mechanics to Computational Biology**, lives in [`book/`](book/). First complete draft (May 2026): 20 chapters across 4 parts (Foundations / Physics / Emergence / Applications) plus front matter, three appendices, glossary, and bibliography. The full compiled manuscript is at [`book/The-Incompleteness-of-Observation-FULL.pdf`](book/The-Incompleteness-of-Observation-FULL.pdf). See [`book/README.md`](book/README.md) for the manuscript map, status notes, and reader's guide.

**License.** All source code under `papers/oi_lattice_code/` is released under the MIT License — see [`LICENSE`](LICENSE). The accompanying papers and book manuscript are research/authored works and are not licensed under MIT; cite the relevant paper if you use the framework or its results, and cite this repository if you use or adapt the lattice utilities.

**Citation / archive.** The source code and accompanying papers are archived on Zenodo with concept DOI [10.5281/zenodo.19060318](https://doi.org/10.5281/zenodo.19060318), which always resolves to the latest version. Specific per-release DOIs are minted at release time.

## Key Results

| # | Result | Status | Source |
|---|---|---|---|
| 1 | Accessible non-Markovianity ⟺ per-horizon C1/C3/C4 deterministic realization (C2 separate, conditional); representation equivalence $S \iff D \iff Q_{\mathrm{fb}}$ — internal, universal; universal hidden-memory theorem over every completion | theorem (+ imported correspondence for the compressed form) | Main §3.4 |
| 2 | $\hbar = c^3 \varepsilon^2/(4G)$ from horizon thermal self-consistency, $\varepsilon = 2 l_p$ uniquely | conditional on H-slope; boost prerequisite: matching certified (SM §4.4), running reported, unverified (F13) | GR §§3–4, §8.5 |
| 3 | Bekenstein-Hawking entropy with $1/4$ coefficient (GW250114 tests the area theorem, not the coefficient) | conditional on H-slope through the gap equation | GR §5 |
| 4 | Cosmological constant dissolution: $10^{122}$ ratio = $S_{\rm dS}$ compression ratio | descriptive-level dissolution, conditional on the geometry-first ordering | GR §6 |
| 5 | Wave equation uniquely selected; produces the matter and light-cone inputs for Einstein's equations (the smooth manifold's emergence from the discrete substratum is a separate, open kinematic question — GR §8.7) | theorem | SM §3 + GR §3, §8.7 |
| 6 | SM gauge group SU(3)×SU(2)×U(1); hypercharges; threefold taste multiplicity (generations under H-spin', chirality under H-χ', sharpened: the minimal embedding is certified vector-like); not resolved — $T$-invariance gives $\theta\in\{0,\pi\}$ and reciprocal transition counts, not $\bar\theta = 0$ (H-top, H-det) | theorem + named hypotheses | SM §§4, 5 |
| 7 | Twenty-two SM observables match observation across CKM, mass, PMNS sectors | structural + empirical | SM §7 |
| 8 | Dark sector $\sim 95\%$, $a_0 = cH/6$, Bullet Cluster, CMB peaks | G1-register results, conditional on G3 (total budget); structural (specific magnitudes) | GR §7 |
| 9 | Page curve from nested trace-out, $t_P \approx 0.646\, t_{\rm evap}$ | theorem at the G1 register, conditional on G3 and Theorem A.8's hypotheses | GR Appendix A |
| 10 | Observer selection theorem: C1–C4 systems exist only out of equilibrium → arrow of time, no Boltzmann brains | theorem, conditional on (EM) | Main §4.6 |
| 11 | Reconstruction theorem: under E1–E7, A1–A6, M1-T, C2-mixing and Lemma 24.1's completeness, the **local propagating lattice/gauge residue** is unique modulo the stated gauge freedoms; M1-B/H-Bell condition Bell-inclusive existence, and Bell-inclusive uniqueness is open | conditional theorem | Substratum §§3–4 |
| 12 | No-GUT structural prediction: $\tau_p \sim 10^{45}$ yr, no GUT-mechanism monopoles, no GUT-chain cosmic strings, non-unification of gauge couplings | structural | SM §6.7 + §8.7 + Structure §12.5 |
| 13 | Substratum-level $B$ conservation + sphaleron emergence in emergent EFT (substratum-emergent operator distinction) | theorem | SM §8.7 |
| 14 | Structural preconditions for organic chemistry, RNA world as first molecular C1–C4, viable parameter fraction $\sim 16\%$ | structural chain + statistical | Complexity |
| 15 | BQP characterization theorem for embedded observers; quantum (BQP-form) Extended Church-Turing Thesis as conditional theorem under a global model-coverage premise; structural silence on P vs NP; three condition-based research directions for refinements within BQP | theorem (BQP boundary) + research directions | Computation |
| 16 | Non-Markovian dynamics in biology, memory asymmetry as therapeutic axis, 29 testable predictions | predictions | Medicine |
| 17 | Information-theoretic ceiling on transcriptome-only bioinformatic methods, 22 testable predictions across single-cell analysis | predictions | Bioinformatics |

The classification (structural / mass-chain / empirical / phenomenological) for the SM observables is documented in SM §7.6.

## The Bidirectional Correspondence

The foundational theorem is bidirectional at the level actually observable on a finite horizon:

```text
finite stochastic law (S)
        ⇅ exact
finite reversible realization (D)
        ⇅ exact
fixed-basis unitary/Born representation (Q_fb)
```

The representation arrow is universal: Markov processes live in the same class. The specifically OI content is history readback. C4 forces readout-relevant hidden predictive memory in every faithful realization and, on a fixed finite recurrent representative, forces global indivisibility. C1 and C3 diagnose the necessary mediation and capacity; C2-structural is persistence to readback.

For spatial systems, the coupling graph defined by one-step dynamical dependence gives exact causal cones. Bell accounting is correspondingly sharp: a deterministic completion with pointwise cones and a setting-independent pre-setting ensemble is a local hidden-variable model, so CHSH $\le2$. Quantum correlations require ontic parameter dependence (no operational signal) or setting-dependent ontic ensembles. The manuscript's inequality gives the model-independent **necessary lower bound** $I_{\rm ont}\ge0.0309$ bits for the quantum CHSH value; Hall--Branciard's optimized causal measurement-dependent model uses about $0.080$ bits, while the smaller $\sim0.046$-bit benchmark belongs to a retrocausal causal structure not adopted here. The reference nearest-neighbor cubic graph lies on the CHSH-$\le2$ side under measurement independence. The adopted branch instead uses preparation-indexed structure in the existing state-dependent $G(x)$; H-Bell asks whether those prepared graphs preserve the metric/Ollivier--Ricci continuum limit.

The reverse operational result is also constructive: every finite quantum record has a finite reversible realization, and for any bounded finite quantum experiment envelope and $\varepsilon>0$, one finite OI realization reproduces the entire envelope to that accuracy. What remains open for the strongest *full operational equivalence* wording is one common standard local quantum instrument/composite representation for all coherent interventions. This is a narrower operational-lifting problem; it is not a retreat from the exact finite stochastic/representation equivalence.

## Licensing

This repository is mixed content, and two licenses apply by scope:

| Scope | License |
|---|---|
| **Source code** — everything under `papers/oi_lattice_code/`, the build and audit scripts under `audit/`, and any other program source here | **MIT**, per `LICENSE` |
| **Manuscripts** — the technical papers under `papers/` in Markdown, LaTeX and PDF form, and everything under `book/` | **CC-BY-4.0** ([deed](https://creativecommons.org/licenses/by/4.0/)) |

This section is the authoritative statement of scope. `LICENSE` carries the verbatim MIT
text and is the file read by automated license detection; it is deliberately the only file
named `LICENSE*`.

Attribution, as CC-BY-4.0 requires for the manuscripts, is satisfied by a citation of the
form

> Maybaum, A. (2026). *The Observational Incompleteness Framework*. Zenodo. https://doi.org/10.5281/zenodo.19060318

The concept DOI resolves to the latest version; work reproducing a specific claim should
cite the version DOI of the release carrying it. For the code, MIT requires that the
copyright and permission notice in `LICENSE` accompany substantial portions of the source.

The Zenodo deposit archives the whole repository as one record, and Zenodo's license field
holds a single value. It is set to CC-BY-4.0, matching the manuscripts, which are the bulk
of the deposit; the record description states the split. MIT continues to govern the code
inside the archive regardless of that record-level label.

## Contact

Alex Maybaum — Independent Researcher
[LinkedIn](https://www.linkedin.com/in/amaybaum)
