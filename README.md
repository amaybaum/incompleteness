# The Incompleteness of Observation

**Author:** Alex Maybaum
**Date:** April 2026
**Status:** DRAFT PRE-PRINT
**Classification:** Theoretical Physics / Foundations

This repository develops a single framework across four papers:

- **Main** — establishes the equivalence between embedded observation and quantum mechanics
- **SM** — derives the Standard Model from a $d = 3$ cubic lattice
- **GR** — derives the gravitational sector from the cosmological horizon
- **Substratum** — ties these into a single construction at the substratum level

A focused submission paper, **Juno**, presents the prediction $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$, recently confirmed by JUNO at $0.07\sigma$ against the post-JUNO global fit. See [Juno](#juno-paper-focused-submission) below.

The full file list is in [Contents](#contents).

---

## Overview

The universe is completely described by a lossless memory with finite read-write access. Physics is what that memory looks like from inside.

A *lossless memory* is a system whose states evolve by a reversible rule. Every state has one predecessor and one successor; no information is created or destroyed. The past is always recoverable from the present. Formally, this is a finite set $S$ of distinguishable states and a bijection $\varphi: S \to S$. The observer has access to only a bounded portion of the state, called the *visible sector*. Each step updates both sectors at once, but the observer reads only the visible part. Correlations written into the hidden sector persist there and return on later steps. This read-write cycle is what produces quantum mechanics — not passive observation.

### The problem

Physics has two foundational theories, quantum mechanics (QM) and general relativity (GR), that are individually precise and resist unification. The sharpest symptom is the cosmological constant problem: QFT's natural estimate of the vacuum energy density exceeds the observed $\Lambda$ by a factor of $\sim 10^{122}$. GR makes no prediction for the vacuum energy itself, so the gap lies between QFT's estimate and the observed bound. Standard treatments assume one or both ingredients are wrong. This framework argues neither is wrong: the gap is a necessary consequence of observation from within.

### Addressing common concerns

Readers approaching the framework from "QM is fundamental" will see claims that initially appear to conflict with established results. Each has a specific resolution; this section states the concerns plainly and points to where they are addressed.

**Q: Why reformulate QM at all? It works fine as a fundamental theory.**

Taken as fundamental, QM leaves the measurement problem unresolved, is sharply incompatible with GR (the $10^{122}$ CC hierarchy), and postulates rather than derives its own structure — Hilbert space, the Born rule, and unitarity all appear as axioms. The framework derives QM as the necessary description of a finite embedded observer of a deterministic substrate (Main §§4–6). It recovers every quantum prediction while making the issues above tractable: the Schrödinger equation, Born rule, and Bell violations all emerge as theorems from the conditions C1–C3 on the hidden sector.

**Q: Doesn't this revive local hidden variables, which Bell rules out?**

No. The framework's substratum $(S, \varphi)$ is not a local hidden variable in Bell's sense. Bell's theorem assumes Markovian conditional independence between measurement outcomes and hidden variables. The hidden sector here violates this through P-indivisibility — it retains correlations over the full observation interval. Brandner (*Phys. Rev. Lett.* **134**, 037101, 2025) established at theorem level that this non-Markovian dynamics is the unique mechanism that reproduces quantum statistics without nonlocality or superdeterminism. Bell violations are recovered as structural consequences of P-indivisibility, not explained away.

**Q: If the dynamics is classical and deterministic, how do you get the Born rule?**

Measurement is the observer's read-write cycle on the partition $V$. Reads from the visible sector produce classical outcomes; writes to the hidden sector imprint correlations that persist via the slow-bath condition (C2). The Born rule is the equilibrium distribution of this cycle — not an extra postulate, but the unique stable statistics of indistinguishable-state averaging under P-indivisibility. Interference is write-then-read across hidden modes: information deposited in earlier transitions modifies the probabilities of later ones. See Main §§4–6 for the derivation, Substratum §2 for the picture.

**Q: Doesn't Nielsen–Ninomiya forbid chiral fermions on a lattice?**

NN forbids them under four specific premises. The load-bearing one is NN4: the action must be bilinear in fermionic fields carrying a conserved chirality charge. The OI fundamental action is bosonic (the bijection $\varphi$); fermions and chirality are derived post-trace-out, by which point NN4 no longer applies. The theorem is not evaded by a clever fermion formulation — it simply does not enter. The "unwanted" doublers that NN forces on any bilinear lattice fermion action become, here, the three physical generations: the $T_1$ triplet of the 6-link wave-equation decomposition. See SM §4.8.1.

**Q: How can the $10^{122}$ CC hierarchy dissolve by reinterpretation alone?**

Jacobson's thermodynamic derivation of Einstein's equations shows that gravity responds to *coarse-grained* information content. On a finite-partition horizon, that's exactly the observer-accessible part. The $10^{122}$ gap between the naive vacuum-energy estimate and the observed $\Lambda$ is therefore not a miscalculation. It is the compression ratio between the substratum's total information content and what the observer can read. The same mechanism produces the Bekenstein-Hawking coefficient $S = A/(4 l_p^2)$ — confirmed by GW250114 at 99.999% — and dynamical dark energy in Type II running-vacuum form. (Functional form is forced by boundary-entropy architecture; theorem-level magnitude $|\nu| \approx |\nu_{\rm QFT}| \sim 10^{-32}$, indistinguishable from zero, consistent at $2\sigma$ with Bertini et al. 2025's direct RG-corrected $\Lambda$CDM fit to DESI DR2 + DES-Y5 + Planck.) See GR §§6–7.

**Q: Generating SU(3)×SU(2)×U(1) and three generations from a cubic lattice sounds ad hoc.**

The lattice is not a physical crystal. It is the coupling graph of $\varphi$ — an equivalence class of structural data. Alphabet size $q$ is a gauge freedom (different $q$ give identical observables). $d = 3$ is the *uniquely self-consistent* dimension (three independent filters on the wave equation). Coupling-degree minimality forces $K = 2d = 6$ link directions at each site. The cubic group $O$ acting on 6 link directions has a unique irrep decomposition $T_1 \oplus E \oplus A_1$, and the commutant of the resulting coupling matrix $M$ is exactly $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ with three generations. Neither the gauge group nor the generation count is a free parameter; both follow from the character table of $O$. See SM §§3.2, 4.6, 4.7.

**Q: How is black-hole information preserved?**

The Page curve is derived at theorem level from the framework's nested trace-out, with $t_P \approx 0.646\, t_{\rm evap}$ (GR Appendix A). Information moves from the visible sector to the hidden sector as the black hole evaporates; it is never lost from $(S, \varphi)$. The generalized second law follows from strong subadditivity applied to the nested partition. See GR Appendix A.

**Q: Doesn't a finite deterministic substrate have a Boltzmann-brain problem? And what gives the arrow of time?**

Both are addressed by a single structural theorem (Main §4.6). Observer partitions satisfying C1–C3 cannot exist in the equilibrium phase of $(S, \varphi)$: the hidden-sector correlation time $\tau_B$ is bounded by the local mixing time on equilibrium microstates, so C2 ($\tau_B \gg \tau_S$) fails there. Boltzmann brains are excluded because they sit in local thermal equilibrium by construction — their $\tau_B \lesssim 10^{-12}$ s is six or more orders of magnitude too short, regardless of anthropic considerations. The same theorem replaces the "past hypothesis" of low initial entropy with an observer-selection rule derived from the framework's own definitions. The arrow of time then follows: the substratum has no arrow, but observers are confined to the non-equilibrium phase where horizon expansion provides the primary temporal structure. Entropy increase is emergent — a coarse-grained description of observer-accessible dynamics.

---

**What does not dissolve.** The absolute scale of fermion masses ($m_s$), CP-violating phases, the charm-mass anomaly, and the residual electroweak hierarchy remain explicit inputs or open questions, as noted in SM §7.6 and §8.3. The framework resolves concerns specific to treating QM as fundamental; it does not eliminate every open question in particle physics.

### The starting point

The framework begins with a single empirical fact — *observation occurs* — formalized as a definition: an observation is a triple $(S, \varphi, V)$ consisting of a total system, a deterministic dynamics, and an embedded observer. No quantum postulates appear. Three structural lemmas follow (finiteness, causal partition, unique measure), from which quantum mechanics emerges under three conditions on the hidden sector.

### The core theorem

When the hidden sector is coupled (C1), retains correlations much longer than the observer's measurement timescale (C2), and is large enough that measurements do not appreciably perturb it (C3), the observer's reduced description is necessarily quantum mechanics. The Schrödinger equation, the Born rule, and Bell violations all emerge as structural consequences. The conditions are also necessary: QM and embedded observation under C1–C3 are equivalent. The proof rests on P-indivisibility — finiteness guarantees recurrence, coupling ensures distinguishability contracts at short times, and recurrence restores it, producing a non-monotonic trajectory that no memoryless process can replicate.

### The cosmological realization

The theorem becomes physics at the cosmological horizon — the boundary beyond which no signal can reach the observer. Stress-energy conservation enforces coupling (C1). The hidden sector's correlation time is the age of the universe versus laboratory timescales, a ratio of $10^{-32}$ (C2). The hidden sector has $\sim 10^{122}$ degrees of freedom (C3).

From this single realization, the framework derives $\hbar = c^3 \varepsilon^2/(4G)$ from thermal self-consistency, recovers the Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ including the $1/4$ factor, and dissolves the $10^{122}$ cosmological constant discrepancy as the information compression ratio of the observer's quantum description. The same trace-out renders ~95% of the universe's gravitational budget invisible to the emergent QFT, matching the observed dark sector. The entropy displacement mechanism derives dark matter phenomenology: from galaxies ($a_0 = cH/6$, baryonic Tully-Fisher) through clusters (Coma matched to <1%) to the Bullet Cluster (frozen boundary entropy explains the gas-lensing offset). The framework's central technical move — that integrating out hidden degrees of freedom from a deterministic substrate produces well-defined non-Markovian visible dynamics — is now established at theorem level in the open systems literature (Brandner 2025).

### The emergent structure

The dynamics uniquely selected by the QM requirement also produces all inputs for general relativity. Seven independent checks, zero failures:

1. Emergent action scale $\hbar = c^3 \varepsilon^2/(4G)$
2. Discreteness scale $\varepsilon = 2 l_p$ uniquely self-consistent
3. Bekenstein-Hawking coefficient $A/(4 l_p^2)$, confirmed by GW250114 at 99.999%
4. Dissolution of the cosmological constant problem
5. Dynamical dark energy in Type II running-vacuum form (functional form forced structurally; magnitude indistinguishable from zero, consistent with Bertini et al. 2025 at $2\sigma$)
6. Dark sector fraction $\Omega_{\rm dark} \approx 95\%$ matching observation
7. MOND acceleration scale $a_0 = cH/6$, confirmed by Jiao et al. 2023

(See GR §7.4 for the comparison table.)

The lattice is the coupling graph of $\varphi$, the alphabet size is gauge, $d = 3$ is the unique self-consistent dimension, and the observer is generic. The wave equation on a $d = 3$ lattice determines:

- The Standard Model gauge group and the unique anomaly-free matter assignment
- The generation count locked at exactly three
- Discrete symmetries
- All three gauge coupling strengths at $M_Z$ via the universal induced coupling $1/\alpha_0 = 23.25$ (primary derivation chain proved end-to-end, 29 theorems/lemmas)

The lattice geometry also determines twenty-two quantitative SM observables: gauge couplings, CKM mixing, charged lepton masses, PMNS angles (with $\sin^2\theta_{12}$ confirmed by JUNO at $0.07\sigma$ vs. the post-JUNO global fit), the Higgs quartic at the compositeness scale, the top mass, and the bottom-to-tau mass ratio. All match observation. Thirteen are strictly parameter-free structural predictions; two follow from a gauge-coupling chain with one constrained parameter; three form a one-input mass chain rooted at a single empirical mass scale; the rest involve explicit empirical or phenomenological inputs identified in SM §7.6. No parameters are fit to the predicted quantities.

### Two types of inaccessibility

The framework distinguishes two reasons a quantity can be inaccessible:

- **Undecidable:** the hidden-sector state $h$. Definite, consequential, provably inaccessible. The structural consequence is quantum mechanics.
- **Gauge:** the alphabet size $q$ and the deep-sector cardinality $|C_D|$. Different values produce identical observables, so the question itself is empty.

The question "is the universe finite or infinite?" has no empirical content — it is gauge.

### Reconstruction and the incompleteness family

The reconstruction theorem establishes the converse: observed QM with Bell violations, finite boundary entropy, and spatial isotropy, together with the framework's structural assumptions (finiteness, determinism, bounded coupling, center independence, linearity, background independence), uniquely determine the equivalence class $[(S, \varphi)]/\mathcal{G}_{\rm sub}$. This proves that the mathematical description and the physics are informationally equivalent up to gauge within this structural class. Whether $(S, \varphi)$ *is* reality or *describes* reality is provably undecidable by any measurement.

The framework belongs to a family of results where self-reference under finite resources produces rigid structure: Gödel (a formal system cannot prove all truths about itself), Turing (a computer cannot decide all questions about its own behavior), OI (an embedded observer cannot access the complete state). In each case, structural impossibility determines the form of what the system produces instead.

### Three emergences, one structural requirement

Three apparently independent emergence stories trace to a single structural requirement:

- Quantum mechanics emerges from C1–C3 (Main characterization theorem)
- General relativity emerges from the horizon trace-out (GR derivation of $\hbar$, $S_{\rm BH}$, running-vacuum form)
- The arrow of time emerges from the observer's confinement to the non-equilibrium phase (Main §4.6)

Before the observer-selection theorem, these were three separate derivations with separate starting points. The theorem shows they share a common foundation: *observers satisfying C1–C3 exist only in the non-equilibrium phase of $(S, \varphi)$*. QM emerges because that phase is where C1–C3 holds. GR emerges because the cosmological horizon is the natural non-equilibrium structure satisfying C2 with $\tau_B \sim H^{-1}$. The arrow of time emerges because observer-existence and horizon-expansion together supply a monotonic clock that all observers agree on. *Nothing is fundamental; everything derives, including the direction of time.*

---

## JUNO confirmation: a parameter-free prediction tested

In November 2025, JUNO reported its first measurement of the solar mixing angle:

$$\sin^2\theta_{12} = 0.3092 \pm 0.0087$$

The post-JUNO global fit (Capozzi et al. 2025) tightens this to:

$$\sin^2\theta_{12} = 0.3085 \pm 0.0073$$

The framework's prediction, fixed before JUNO took data, is:

$$\sin^2\theta_{12} = \frac{1}{3} - \frac{1}{4\pi^2} = 0.3080$$

Match: **0.07σ against the post-JUNO global fit; 0.14σ against the JUNO direct measurement**. Both inputs entering the prediction were fixed *a priori*: the value $1/3$ comes from $A_4$ representation theory, and $\lambda^2 = 1/(2\pi^2)$ is the squared Cabibbo angle, fixed by the same cubic Brillouin geometry that gives $\lambda = 0.22508$ (matching observation to $0.04\%$).

The same construction predicts the other two PMNS angles:

| Angle | Prediction | Measurement | $\sigma$ |
|---|---|---|---|
| $\sin^2\theta_{12}$ | $1/3 - 1/(4\pi^2) = 0.3080$ | $0.3085 \pm 0.0073$ | $0.07$ |
| $\sin^2\theta_{13}$ | $4/(18\pi^2) = 0.02252$ | $0.02195 \pm 0.00056$ | $1.01$ |
| $\sin^2\theta_{23}$ | $1/2 + 1/(2\pi^2) = 0.5507$ | $0.561^{+0.012}_{-0.015}$ | $0.74$ |

A discrete $\mu$-$\tau$ parity together with a natural-normalization condition forces the exact sum rule:

$$2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$$

This sum rule is not produced by the column-preservation patterns currently competing against JUNO data (TM1, TM2). TM2 is excluded at >3.5$\sigma$ by post-JUNO data; TM1's prediction $\sin^2\theta_{12} = 0.3184$ sits at 1.35$\sigma$. The cubic-group prediction is closer to observation by a factor of about 20 in $\sigma$-distance.

JUNO's design-lifetime precision of $\pm 0.0014$ on $\sin^2\theta_{12}$ — six times tighter than the current first result — will test the prediction at sub-percent level over the next decade. Combined with atmospheric measurements at DUNE, T2HK, and Hyper-Kamiokande, the sum rule will be tested at the $0.005$ level on the right-hand side, sharper than either angle alone.

A focused submission paper, **Juno**, presents this result in self-contained form. See [`Juno.md`](Juno.md) / [`Juno.tex`](Juno.tex) / [`Juno.pdf`](Juno.pdf).

---

## Contents

### Main Paper

**"The Incompleteness of Observation"**

Establishes the QM–embedded observation equivalence: under three structural conditions on the hidden sector (C1: non-trivial coupling, C2: slow-bath memory, C3: high-capacity hidden sector), the observer's reduced description is necessarily quantum mechanics, with the conditions both necessary and sufficient. Includes the P-indivisibility theorem, the stochastic-quantum correspondence, the characterization theorem, and Bell violation analysis.

- [`Main.md`](Main.md) — Markdown source
- [`Main.tex`](Main.tex) — LaTeX source
- [`Main.pdf`](Main.pdf) — Compiled PDF

### Standard Model Paper

**"The Standard Model from a Cubic Lattice"**

Applies the framework to a $d = 3$ cubic lattice with the wave equation as substratum dynamics. Center independence, isotropy, and linearity uniquely select the wave equation. The wave equation determines the SM gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ and $\bar\theta = 0$. Given the observed family pattern, anomaly cancellation fixes the hypercharges as the unique consistent assignment (fermion embedding closed by the link-carrier construction; the absolute generation count locked at exactly three by coupling-degree minimality) at all energy scales. The primary derivation chain is proved end-to-end.

Twenty-two quantitative observables match observation: gauge couplings (SU(2) and SU(3) at $M_Z$ predicted to <0.3% from a one-parameter chain, with the U(1) row fixing the threshold parameter $\delta_0$); CKM mixing (Cabibbo angle to 0.04%); Koide mass relations (<0.01%); six fermion masses from one empirical mass input (within ~1.3%); PMNS angles (with $\sin^2\theta_{12}$ confirmed by JUNO at 0.07σ vs. post-JUNO global); Higgs quartic $\lambda(M_{\rm Pl}) = 0$ from composite structure; top mass from the IR quasi-fixed point; and the bottom-to-tau mass ratio.

Parameter accounting: thirteen strictly parameter-free structural predictions, two from one constrained parameter, three in a one-input mass chain, and the rest with explicit inputs listed in §7.6.

- [`SM.md`](SM.md) — Markdown source
- [`SM.tex`](SM.tex) — LaTeX source
- [`SM.pdf`](SM.pdf) — Compiled PDF

### General Relativity Paper

**"$\hbar$, the Bekenstein-Hawking Entropy, and Dynamical Dark Energy from the Cosmological Horizon"**

Applies the framework to the cosmological horizon as a causal partition. Derives:

- The emergent action scale $\hbar = c^3 (2 l_p)^2 / (4G)$ from thermal self-consistency
- The discreteness scale $\varepsilon = 2 l_p$ as the unique simultaneous solution
- The Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ including the $1/4$ coefficient by direct mode counting (confirmed at 99.999% by GW250114)
- Dissolution of the cosmological constant problem
- Dynamical dark energy in Type II running-vacuum functional form (magnitude not derived at theorem level; consistent with Bertini et al. 2025's direct RG-corrected $\Lambda$CDM fit to DESI DR2 + DES-Y5 + Planck 2018, $\nu = -(2.5 \pm 1.3) \times 10^{-4}$, consistent with zero at $2\sigma$)
- The ~95% dark sector concordance
- The MOND acceleration scale $a_0 = cH/6$ from entropy displacement (confirmed by Jiao et al. 2023 for the Milky Way's Keplerian decline at ~17 kpc)

- [`GR.md`](GR.md) — Markdown source
- [`GR.tex`](GR.tex) — LaTeX source
- [`GR.pdf`](GR.pdf) — Compiled PDF

### Substratum Paper

**"The Substratum Construction: Reconstruction, the Substratum Gauge Group, and the QM-GR Synthesis"**

Develops the substratum-level structural results that make the SM, GR, and arrow-of-time derivations a single construction. The reconstruction theorem (Theorem 23) establishes that observed physics — quantum mechanics with Bell violations, finite boundary entropy, and spatial isotropy — together with the framework's structural assumptions (A1–A6), uniquely determines the equivalence class $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ at the lattice level. The SM gauge group and $\bar\theta = 0$ are forced retrodictions; the anomaly-free hypercharge assignment is forced once the observed family pattern is given.

The substratum gauge group $\mathcal{G}_{\rm sub}$ (Theorem 24) has four families of generators proved to exhaust all observables-preserving transformations, and projects through the trace-out onto the SM gauge group as the visible-sector shadow of the substratum's symmetry.

The paper argues that quantum mechanics, general relativity, and the arrow of time are not independent theories but three projections of the same finite deterministic construction. The QM-GR incompatibility dissolves as a category error rather than being solved as a technical problem; the arrow of time is answered by the C1–C3 observer-selection theorem applied to the horizon-growth clock (§5.4).

- [`Substratum.md`](Substratum.md) — Markdown source
- [`Substratum.tex`](Substratum.tex) — LaTeX source
- [`Substratum.pdf`](Substratum.pdf) — Compiled PDF

### Juno Paper (focused submission)

**"A Parameter-Free Prediction of the Solar Mixing Angle from Cubic-Group Flavor Structure, Tested by JUNO"**

A focused submission paper presenting the prediction $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$ in self-contained form. The cubic point group $O$ — the symmetry group of three-dimensional space — is taken as the underlying flavor symmetry, with the three generations transforming as the $T_1$ irrep. The Cabibbo scale $\lambda^2 = 1/(2\pi^2)$ is fixed by the cubic Brillouin-zone geometry (matching observation to 0.04%). A discrete $\mu$-$\tau$ parity together with a natural-normalization condition then forces the angle predictions and the sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$. All three PMNS angles agree with observation within $1.1\sigma$.

The paper is fully self-contained — no companion-paper citations required. It targets PRD or PLB.

- [`Juno.md`](Juno.md) — Markdown source
- [`Juno.tex`](Juno.tex) — LaTeX source (RevTeX 4-2)
- [`Juno.pdf`](Juno.pdf) — Compiled PDF

### Explainer

**"Why Physics' Biggest Contradiction Might Not Be a Contradiction at All"**

A companion overview covering the full argument — QM emergence, GR derivation, structural foundations, Standard Model structure, the memory interpretation of $(S, \varphi)$, the relationship between mathematics and physics, and the identification of physics as observable mathematics. Includes detailed proof walkthroughs, philosophical lineage, observational confrontation (DESI DR2 RVM-favoring multi-model analysis, JUNO precision on $\sin^2\theta_{12}$, DESI DR2 neutrino constraints, LZ Dec 2025 null, Jiao et al. 2023 Milky Way Keplerian decline, Genzel et al. 2017, McGaugh et al. 2024, Bullet Cluster, Brandner 2025 mechanism support), and FAQ.

- [`Explainer.md`](Explainer.md) — Markdown source
- [`Explainer.tex`](Explainer.tex) — LaTeX source
- [`Explainer.pdf`](Explainer.pdf) — Compiled PDF

### Complexity

**"The Structural Preconditions for Complexity: Why the Laws of Physics Guarantee the Possibility of Organic Chemistry"**

Traces the consequences of the derived structure through atomic physics, chemistry, prebiotic selection, and the origin of life. The structural chain from $(S, \varphi)$ to the preconditions for organic chemistry is parameter-free: $d = 3$ determines orbital structure, the periodic table, carbon's bonding geometry, the nuclear-atomic scale hierarchy, water's solvent properties, and the thermal window. The viable parameter fraction is estimated at ~16%. The chirality chain traces biological homochirality to the partition. Autocatalytic networks are statistically expected ($10^{56} \times$ Kauffman threshold). The origin of life is identified as the first molecular C1–C3 system; RNA is the unique single-molecule satisfying all three conditions, making the RNA world a structural prediction. C1–C3 systems are exponential-growth attractors, so the transition is inevitable. The chain extends through evolution, information processing, and AI to a self-referential closure.

- [`Complexity.md`](Complexity.md) — Markdown source
- [`Complexity.tex`](Complexity.tex) — LaTeX source
- [`Complexity.pdf`](Complexity.pdf) — Compiled PDF

### Medical Applications

**"Non-Markovian Dynamics in Biology and Medicine: Molecular Memory as a Therapeutic Target"**

Applies the C1–C3 architecture to biological systems where fast catalytic processes are coupled to slow conformational or post-translational dynamics. Develops a unified framework for seven medical domains:

- Cancer pharmacology (checkpoint kinase memory, schedule-dependent sensitization)
- Neurodegeneration (Alzheimer's, Parkinson's, PTSD as disorders of molecular memory timescale — targeting $\tau_B$ rather than protein aggregates, with reconsolidation paradigms and low-intensity focused ultrasound as the first directly $\tau_B$-targeted therapeutic modality)
- Antibiotic resistance (persister cells as SOS memory accumulation)
- Immunotherapy (T cell exhaustion as accumulated TCR signaling memory)
- Cardiac pharmacology (use-dependent ion channel block)
- Autoimmune disease (disproportionate efficacy of partial JAK inhibition as memory disruption)
- Genetic disorder management (replacement therapy scheduling, inhibitor prevention, gene therapy durability)

The molecular hierarchy (conformational, PTM, chromatin, methylation) extends upward through synaptic, circuit, systems, and cortical layers in the nervous system, providing a unified architecture for memory at every scale. Two structural derivations connect the framework to clinical phenomena: (a) the necessarily reconstructive nature of memory access, and (b) finite $\tau_B$ at every layer as a structural requirement. Identifies *memory asymmetry* — differential dependence on non-Markovian dynamics between disease and normal tissue — as a pharmacologically distinct therapeutic axis.

Twenty-nine testable predictions, each distinguishing non-Markovian from Markovian pharmacology. Several already supported by existing data: Abl kinase resistance dynamics, BTK inhibitor-specific regulatory effects, RGS4 selectivity patterns, propranolol-during-recall in PTSD trials, cognitive benefit from focused-ultrasound-only intervention in the 2025 Korean Alzheimer's trial.

- [`Medicine.md`](Medicine.md) — Markdown source
- [`Medicine.tex`](Medicine.tex) — LaTeX source
- [`Medicine.pdf`](Medicine.pdf) — Compiled PDF

### Lattice Monte Carlo Code

Source code for the lattice computations reported in the SM paper, §§6.2 (gauge-coupling thresholds) and 7.5 (scalar-density renormalization $Z_S$, dynamical fermion HMC, Higgs effective potential). All files live under [`oi_lattice_code/`](oi_lattice_code/).

```
oi_lattice_code/
├── gauge/                          Pure-gauge measurements + perturbative δ₀
│   ├── metropolis_plaquette.c      Pure-gauge Wilson plaquette utility (cross-check)
│   ├── oi_su3_hmc.c                SU(3) OI-induced gauge HMC
│   ├── oi_su2_hmc.c                SU(2) OI-induced gauge HMC
│   ├── oi_u1_hmc.c                 Compact U(1) OI-induced HMC
│   ├── oi_sm_hmc.c                 Full SU(3)×SU(2)×U(1) OI-induced HMC
│   ├── two_loop_vp.py              Two-loop staggered VP (held in reserve)
│   └── AB_derivation/              First-principles A·B from 1-loop bubble+ghost (SM §6.2.1)
├── fermion/
│   └── k6_hmc.c                    K=6 dynamical staggered HMC; the Z_S(m) workhorse
├── effective_potential/            Higgs / Coleman-Weinberg variants
│   ├── k6_cw.c                     Sector-decomposed Coleman-Weinberg potential
│   ├── k6_cep.c                    Constraint Effective Potential (background h)
│   ├── k6_taste.c                  Taste-projected CW with point-split bilinears
│   └── k6_higgs.c                  Dynamical SU(2)-doublet Higgs with Yukawa
├── zs_measurements/                Z_S extraction variants (cross-checks)
│   ├── rimom.c                     RI-MOM scheme: Z_S(μ) at fixed momentum
│   ├── taste_irrep.c               Z_S decomposed by O(3) irrep (A₁/T₁/T₂/A₂)
│   └── ward_chiral.c               L/R sublattice parity (Ward identity)
└── scripts/                        Run drivers and Python analysis
    ├── analyze_zs.py               Extract Z_S(m) from k6_hmc output
    ├── zs_crosscheck.py            Unified driver for the three Z_S cross-checks
    ├── run_cep_scan.sh             Drive CEP h-scan
    ├── run_higgs_scan.sh           Drive dynamical-Higgs κ-scan
    ├── analyze_cep.py              Analyze CEP h-scan output
    └── analyze_higgs.py            Analyze dynamical-Higgs κ-scan output
```

**What each piece does.** `gauge/` contains the perturbative two-loop staggered vacuum-polarization computation (`two_loop_vp.py`) used as a consistency check for the $\delta_0$ threshold in §6.2, the `AB_derivation/` subdirectory with the first-principles $A \cdot B$ computation (SM §6.2.1), and a pure-gauge Wilson plaquette utility (`metropolis_plaquette.c`) retained as a non-perturbative cross-check.

The Python `two_loop_vp.py` originally implemented SE+VC via a Ward-identity 3× approximation (individual diagrams are IR-divergent; only their Ward-combined sum is finite), computed the sails diagram directly (N-independent to 5 digits across $N = 6, 8, 10, 12$), and included a $\times 1.12$ analytical estimate for the momentum-dependent $\Pi_s(p)$ correction. On audit, the numerical scalar used as the induced-propagator denominator in this implementation was found not to be the $\Pi_s$ defined in SM §6.1, and the resulting ratio shows strong IR-regulator dependence characteristic of a scheme-locked quantity rather than a physical $\delta(1/\alpha)$ shift. The prior "$8.0 \pm 2$" result is held in reserve pending a rebuilt calculation.

`AB_derivation/reproduce_AB.py` runs the 1-loop bubble+ghost in the induced gauge theory at successive lattice sizes (up to $N = 40$), extracts $A \cdot B(N)$ via a conversion formula validated to 100% against textbook QCD at $N = 28$, and extrapolates to $N \to \infty$ using both $1/N^2$ and iterated Shanks. End-to-end runtime is ~45 minutes; the result is $A \cdot B = 48.0 \pm 1.5$ versus the paper's fit $46.4$. A direct computation of the $\Pi_s(p)$ correction at finite fermion mass is obstructed by the same 16 staggered zero modes that dominate the existing ratio — a proper implementation requires regulator-matching across topologies, an open technical item.

The `oi_*_hmc.c` files are exploratory OI-induced gauge HMC for SU(3), SU(2), U(1), and the full SM product group. These are development/diagnostic code; they are *not* inputs to any published number. See SM §6.5 for why the Haar-measure OI-induced theory confines and cannot be used directly for the gauge coupling derivation.

`fermion/k6_hmc.c` is the dynamical staggered fermion HMC used to compute $Z_S(m)$ on SU(3) backgrounds at $\beta_3 = 11.1$ across 30 mass points and three volumes. The published $Z_S(0.122) = 1.813 \pm 0.001$ is the cubic interpolant of the $L = 32$ ensemble, extracted via `scripts/analyze_zs.py`.

`effective_potential/` contains four genuinely different attacks on the Higgs / electroweak-scale problem (sector-decomposed CW, constraint effective potential, taste-decomposed CW, dynamical Higgs doublet). `zs_measurements/` contains three independent $Z_S$ extraction schemes used as cross-checks; `scripts/zs_crosscheck.py` runs them at matched $(L, m, \beta)$ and reports cross-scheme scatter as a systematic-error indicator.

**Build.** All C files are single-file with no external dependencies beyond a C99 compiler with libm and (for some files) OpenMP. Each file's header documents its compile line and command-line usage.

```bash
gcc -O3 -o metropolis_plaquette oi_lattice_code/gauge/metropolis_plaquette.c -lm
gcc -O3 -fopenmp -o k6_hmc oi_lattice_code/fermion/k6_hmc.c -lm
```

On macOS with libomp via homebrew, replace `-fopenmp` with `-Xpreprocessor -fopenmp -I$(brew --prefix libomp)/include -L$(brew --prefix libomp)/lib -lomp`. Files without `omp.h` (`metropolis_plaquette.c`, `oi_*.c`, `rimom.c`, `taste_irrep.c`, `ward_chiral.c`) build without the OpenMP flag.

**Quick-start: Wilson plaquette cross-check.**
```bash
./metropolis_plaquette 2 4 7.4  1000 2000 2 10 0.2    # SU(2) at β=7.4 on 4⁴
./metropolis_plaquette 3 4 11.1 1000 2000 2 10 0.2    # SU(3) at β=11.1 on 4⁴
```
Each run takes ~1 minute on a single core. The utility was validated against literature reference values: SU(2) β=2.3 (gives 0.609 vs lit ≈ 0.605), SU(2) β=20 (0.962 vs ≈ 0.96), SU(3) β=5.7 (0.560 vs ≈ 0.55), SU(3) β=6.0 (0.596 vs ≈ 0.594). The §6.2 derivation does not depend on these plaquette values — they are non-perturbative cross-checks of the pure-gauge sector.

**Quick-start: legacy $\delta_0^{(2L)}$ implementation (held in reserve).**
```bash
python3 oi_lattice_code/gauge/two_loop_vp.py
```
Runs in a few minutes, outputting $\delta_0$ (SE+VC via Ward 3×) grid convergence, the sails contribution, and the $\Pi_s(p)$ correction estimate. On audit, this implementation was found to use a scheme-locked $\Pi_s$ convention; the "$8.0 \pm 2$" result is held in reserve pending a rebuilt calculation. $\delta_0 = 10.02$ is empirically fixed by the U(1) row (SM §6.2).

**Quick-start: reproducing $Z_S(0.122) = 1.813$.**
```bash
# HMC at the target mass — defaults: nstep=1, tau=0.005, ~58% acceptance at L=6
./k6_hmc 32 0.122 50 200 zs_L32_m0p122.dat
# Full mass scan + cubic interpolation
for m in 0.005 0.010 0.020 0.050 0.080 0.100 0.122 0.150 0.200 0.300 0.500; do
    ./k6_hmc 32 $m 50 200 "zs_L32_m$(printf '%04d' $(echo "$m*1000" | bc | cut -d. -f1)).dat"
done
python3 oi_lattice_code/scripts/analyze_zs.py -L 32 -m 0.122 zs_L32_m*.dat
```
`analyze_zs.py` computes the free-theory $\langle\bar\psi\psi\rangle$ analytically with matched regulator, divides to get $Z_S(m)$, and cubic-interpolates to the target mass in the volume-converged region ($mL \gtrsim 3$). Integrator parameters `nstep` and `tau` can be overridden as CLI arguments 6 and 7: at larger $L$ or smaller $m$, reducing `tau` (or increasing `nstep` at fixed `nstep*tau`) may be needed to keep acceptance above ~50%.

**Quick-start: Z_S cross-check across three independent schemes.**
```bash
python3 oi_lattice_code/scripts/zs_crosscheck.py --run -L 16 -m 0.20 -ncfg 50 -nthm 100 -beta 11.1
```
Runs `rimom.c`, `taste_irrep.c`, and `ward_chiral.c` at the same $(L, m, \beta)$ and reports $Z_S$ in the diagnostic channel of each (rimom at $|p|^2 = 5$, taste_irrep $T_1$, ward_chiral L-sector), plus cross-scheme scatter as a systematic-error indicator.

**Status — read this before running.**

1. **First-principles $A \cdot B$ derivation (partial).** The $C_2$-dependent threshold in §6.2 is parameterized by the log form $A \cdot \ln(1 + B \cdot C_2 g_0^2)$ with $(A, B) = (8.3, 5.59)$. The leading coefficient — the product $A \cdot B$ multiplying $C_2 g_0^2$ at linear order — is independently derived via 1-loop lattice PT in the induced gauge theory, giving $A \cdot B = 48.0 \pm 1.5$ (±3%) against the fitted $46.4$ (SM §6.2.1). Implementation in `oi_lattice_code/gauge/AB_derivation/`. Separating $A$ from $B$ individually is open — it requires either the next-order $(C_2 g_0^2)^2$ coefficient (full 2-loop in the induced theory) or a scan over effective coupling (varying the fermion mass $m$) to fit the log-resum form directly.

2. **The OI-induced confined-phase issue.** As discussed in SM §6.5, running `oi_su3_hmc.c` (or any of the `oi_*_hmc.c` variants) with the Haar measure on the gauge group produces a confined phase $\langle P \rangle \to 0$ — an artifact of using the wrong measure. The actual OI gauge measure is the discrete pushforward of the uniform measure on $(\mathbb{Z}/q\mathbb{Z})^{K \times N}$, not Haar. The perturbative-regime values used for the SM coupling derivation come from the matched two-loop calculation in `two_loop_vp.py`, not from running `oi_*_hmc.c` directly.

3. **Research-grade defaults.** CG tolerances are 1e-10 to 1e-12 across files. The published $Z_S(0.122) = 1.813 \pm 0.001$ quotes statistical error from the $L = 32$ ensemble; systematic errors from finite volume and finite trajectory length are not exhaustively quantified. No regression test suite is included.

**Provenance.** Two files present in the development tree were removed during cleanup before this release. `oi_hmc.c` had a sign bug in the kinetic-energy computation (`K -=` instead of `K +=` for the squared anti-Hermitian momentum), making the molecular-dynamics integrator incorrect; the fix is in `oi_su3_hmc.c`, which is the canonical SU(3) OI-induced HMC source. `taste_proj.c` performed a binary in-vs-out-of-reduced-BZ split for the taste-projected $Z_S$; it is subsumed by `taste_irrep.c`, which decomposes the same data into all four O(3) irreps plus the all-tastes total.

**License.** All source code under `oi_lattice_code/` is released under the MIT License — see [`LICENSE`](LICENSE). The accompanying papers are research manuscripts and are not licensed under MIT; cite the relevant paper if you use the framework or its results, and cite this repository if you use or adapt the lattice utilities.

**Citation / archive.** The source code and accompanying papers are archived on Zenodo with concept DOI [10.5281/zenodo.19060318](https://doi.org/10.5281/zenodo.19060318), which always resolves to the latest version. Specific per-release DOIs are minted at release time.

## Key Results

1. **QM–embedded observation equivalence.** A stochastic process on a finite configuration space is quantum mechanics if and only if it arises from deterministic dynamics with non-trivial coupling (C1), slow-bath memory (C2), and sufficient hidden-sector capacity (C3). *Status: theorem.*

2. **Derivation of $\hbar$.** From the cosmological horizon: $\hbar = c^3 \varepsilon^2/(4G)$, with $\varepsilon = 2 l_p$ fixed by self-consistency. The Bekenstein-Hawking entropy formula $S = A/(4 l_p^2)$ — including the $1/4$ factor — is recovered as a consequence. *Status: theorem.*

3. **Cosmological constant dissolution.** The $10^{122}$ discrepancy is $S_{\rm dS}$ — the information compression ratio of the emergent quantum description. The observed vacuum energy is the mandatory classical baseline. *Status: theorem.*

4. **Dynamics selection and emergent general relativity.** The wave equation is uniquely selected by center independence, isotropy, and linearity. It produces all inputs for Einstein's equations via Jacobson's thermodynamic route. Seven links, all analytically proven. *Status: theorem.*

5. **Structural foundations.** The lattice is the coupling graph of $\varphi$. The alphabet size $q$ is gauge. The observer is generic (C2 is automatic for Hamiltonian dynamics). $d = 3$ is the unique self-consistent dimension. The fundamental object is $(S, \varphi)$: a finite lossless memory. *Status: theorem.*

6. **Standard Model structure.** The wave equation factors into staggered Dirac fermions; center independence mandates the Higgs; $K = 2d = 6$ from coupling-degree minimization; the cubic group gives multiplicities $(3, 2, 1) \to \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$; the trace-out makes SU(2) chiral; anomaly cancellation uniquely determines the hypercharges given the observed family pattern (fermion embedding closed by the link-carrier construction; absolute generation count locked at exactly three by coupling-degree minimality); Higgs quantum numbers $(1, 2, +1/2)$. Primary derivation chain proved end-to-end.

6b. **Gauge coupling prediction.** The fermion-induced coupling gives a universal $1/\alpha_0 = 23.25$ at the Planck scale — determined by $N_f = 6$ and $T(R) = 1/2$, structural quantities independent of $\varphi$, verified analytically via the one-loop staggered VP lattice integral. A universal $C_2$-independent threshold $\delta_0 = 10.02$ is fixed by the U(1) row ($C_2 = 0$); a prior 2-loop staggered VP implementation has been audited and is held in reserve (SM §6.2). $\delta_0 = 10.02$ coincides to $0.2\%$ with the hypercharge-squared trace $\mathrm{Tr}[Y^2] = 10$ of three generations of SM fermions in standard convention — a numerical observation noted in SM §6.2 whose structural vs. coincidental status is open. The $C_2$-dependent threshold is parameterized by a geometric-series resummation of the gauge self-energy `A·ln(1 + B·C₂·g₀²)`. Combined with Standard Model RG running, this reproduces all three gauge couplings at $M_Z$: $1/\alpha_1 = 59.00$, $1/\alpha_2 = 29.57$, $1/\alpha_3 = 8.47$ — matching observed values to <0.1%. The leading coefficient $A \cdot B$ is independently derived via 1-loop lattice PT in the induced gauge theory, giving $A \cdot B = 48.0 \pm 1.5$ against the fitted $46.4$ (SM §6.2.1). Separating $A$ from $B$ individually is open; it requires the next-order $(C_2 g_0^2)^2$ coefficient, structurally suppressed at strict 2-loop in the OI induced theory and requiring 3-loop PT or non-perturbative methods. *Status: proposition (SM §6); A·B derived, individual A and B still fitted.*

6c. **Twenty-two quantitative observables from $d = 3$ (given the SM matter content).** Beyond the gauge couplings, the cubic lattice structure determines nineteen additional SM observables matching observation (SM §7). By input status (see SM §7.6 summary):

   *Strictly parameter-free structural predictions:*
   - Cabibbo angle $\lambda = 1/(\pi\sqrt{2})$ — 0.04%
   - Wolfenstein $A = \sqrt{2/3}$ — 0.23σ vs PDG 2024
   - $|V_{cb}| = \sqrt{2/3}/(2\pi^2)$ — 0.22σ
   - $m_d/m_s = 1/(2\pi^2)$ — 0.56σ vs FLAG 2024
   - $m_u/m_d = \sqrt{2/9}$ — 0.27σ vs FLAG 2024
   - Koide $Q = 2/3$ — <0.01%
   - Koide angle $\theta_0 = C_2/d^2 = 2/9$ — 0.02%
   - PMNS angles from TBM + corrections (sum rule $2\Delta_{12} + \Delta_{23} = 0$ from $\mu$-$\tau$ parity; ratio $\Delta_{13}/\Delta_{23} = A^4$; all within 1.1σ vs NuFIT 6.0; $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$ confirmed by JUNO at 0.07σ vs post-JUNO global)
   - Higgs quartic $\lambda(M_{\rm Pl}) = 0$ — 0.6σ
   - $m_t = v/\sqrt{2}$ from IR quasi-fixed point — 0.9%
   - $m_b/m_\tau = 4.28/Z_S(\lambda g_0^2) = 2.36$ — observed 2.352; 0.4% central match at $L = 32$, ~1–2% systematic (SM §7.5)

   *With one empirical input each:*
   - $m_e$ and $m_\mu$ from $m_\tau$ via Koide $\theta_0$ — <0.01%
   - $m_d$, $m_u$, $m_b$, $m_\tau$ from $m_s$ via structural chain — within ~1.3%
   - $m_H$ in GeV from $\lambda(M_{\rm Pl}) = 0$ + measured $m_t$ — within $m_t$ uncertainty

   *With explicit empirical/phenomenological input:*
   - $J = \eta/(12\pi^6)$ with empirical Wolfenstein $\eta$ — 0.17σ vs PDG 2024
   - The down-quark Koide $Q_{\rm down} \approx (2/3)(1 + \alpha_s/\pi)$ — numerical regularity at 0.15% in PDG mixed scheme; scheme-dependent, taken as phenomenological input for the $m_b$-from-$m_s$ prediction (0.9%)

   Monte Carlo simulations at $L = 16$–$64$ confirm chiral condensate formation. *Status: observation + MC verification (SM §7.5).*

7. **Strong CP solved.** T-invariance of the wave equation $\to \theta = 0$ (theorem). Detailed balance at all time scales ($\varphi^n$ is a bijection for every $n$) $\to$ T-invariant Hamiltonian at every energy scale $\to$ real Yukawa matrices at every scale $\to \bar\theta = 0$ at all energy scales (theorem). No axion needed. The proof bypasses the instanton question entirely.

8. **Dark-sector concordance and dark matter.** The trace-out renders ~95% of $\rho_{\rm crit}$ invisible to the emergent QFT (theorem — total budget). The structured component — entropy displacement via the Clausius relation and Jacobson mechanism — yields $a_0 = cH/6$ and $v^4 = G M_B \cdot cH/6$ (parameter-free). The simple interpolation $\nu(y) = (1 + \sqrt{1 + 4/y})/2$ matches galaxies AND clusters (Coma to <1%). The Bullet Cluster: frozen boundary entropy ($\tau_{\rm relax} \sim H^{-1} \gg t_{\rm collision}$). CMB acoustic peaks: thermodynamic averaging gives non-oscillating wells identical to CDM. High-$z$: declining rotation curves confirmed (Genzel et al. 2017); stellar TF no-evolution confirmed (McGaugh et al. 2024, gas fraction compensates); first detection of a Keplerian decline in the Milky Way's own rotation curve at ~19 kpc (Jiao et al. 2023, A&A 678, A208) provides the cleanest local test. Direct dark matter searches continue to return null (LZ Dec 2025, 417 days), consistent with the framework's prediction that no particle dark matter exists. *Status: theorem (total budget, acceleration scale); interpolation and CMB pending numerical verification.*

9. **Nested partitions and the Page curve.** Sequential and direct trace-outs agree (Theorems A.1–A.4). The generalized second law follows from strong subadditivity (A.6). The Page curve is derived with $t_P \approx 0.646\, t_{\rm evap}$ (A.7–A.9). Information is never lost. *Status: theorem.*

10. **Structural observer selection and the arrow of time.** An immediate corollary of C1–C3 (Main §4.6): observer partitions satisfying the framework's conditions cannot exist in the equilibrium phase of $(S, \varphi)$ — $\tau_B(V) \le \tau_{\rm mix}(\Sigma_{\rm loc}(V)) + O(\varepsilon)$, so C2 fails in equilibrium. This replaces the "past hypothesis" with a structural selection rule and excludes Boltzmann brains structurally — they sit in local thermal equilibrium by construction, so their $\tau_B$ is bounded by thermal timescales (~$10^{-12}$ s) while their $\tau_S$ is bounded below by information-processing timescales (~$10^{-6}$ s). The exclusion is structural, not anthropic. The arrow of time then follows: the substratum has no arrow ($\varphi$ and $\varphi^{-1}$ are equally valid), but observers necessarily exist in the non-equilibrium phase where horizon expansion sets $\tau_B \sim H^{-1}$, and entropy increase is an emergent coarse-grained description. Like QM, the Second Law is emergent. *Status: theorem (Main §4.6).*

11. **Falsifiable predictions.** Dynamical dark energy in Type II RVM structural form (functional form forced by boundary-entropy architecture; theorem-level magnitude $|\nu| \approx |\nu_{\rm QFT}| \sim 10^{-32}$, indistinguishable from zero — Bertini et al. 2025 returns $\nu = -(2.5 \pm 1.3) \times 10^{-4}$, consistent with zero at $2\sigma$ and consistent with the framework's prediction; DESI Y5 will confirm or, at $|\nu| \gtrsim 10^{-4}$ high-significance detection, require additional substratum spectral structure not currently in §3–§5 of GR). SU(2) and SU(3) gauge couplings at $M_Z$ to <0.3% from a one-parameter chain; $\bar\theta = 0$ exactly; no SUSY, no fourth generation; Majorana neutrinos with normal ordering and $\Sigma m_\nu$ near 0.059 eV (DESI DR2+CMB: $\Sigma m_\nu < 0.0642$ eV with normal ordering preferred and lightest mass bounded at $m_l < 0.023$ eV — every directly comparable measurement matches the prediction; JUNO sub-percent precision on $\sin^2\theta_{12}$ confirming the persistent solar/reactor 1.5σ tension). Baryonic TF evolves as $v^4 \propto H(z)$ (untested). Cabibbo angle $\lambda = 1/(\pi\sqrt{2})$ (confirmed to 0.04%). Wolfenstein $A = \sqrt{2/3}$ (confirmed to 0.23σ vs PDG 2024). $m_d/m_s = 1/(2\pi^2)$ (0.56σ vs FLAG 2024). $m_u/m_d = \sqrt{2/9}$ (0.27σ). Koide angle $\theta_0 = C_2/d^2 = 2/9$ giving $m_e$ and $m_\mu$ to <0.01%. PMNS angles: $\sin^2\theta_{12}$ confirmed by JUNO at 0.07σ vs post-JUNO global, all within 1.1σ. $m_t = v/\sqrt{2}$ from IR quasi-fixed point (0.9%). $m_b/m_\tau = 4.28/Z_S(\lambda g_0^2) = 2.36$ (observed 2.352; 0.4% central match, ~1–2% systematic). Six fermion masses from one empirical input ($m_s$), all within ~1.3%. Lorentz-invariance violation with $\omega^2 = k^2[1 - (2/15)(E/M_{\rm Pl})^2 + \ldots]$ — subluminal at leading order, with the $2/15$ coefficient computed from the cubic-lattice dispersion (not tunable), and linear LIV strictly forbidden at the substrate level (detection at any scale falsifies). The conjunction is distinctive to this framework.

12. **The trace-out as Jordan-Chevalley projection.** Over finite fields, the evolution matrix $F$ decomposes as $F = F_{\rm ss} \cdot F_u$ (semisimple × unipotent). The trace-out extracts the semisimple part and erases the nilpotent monodromy $N$. The Weil-Deligne conductor $f_{\rm WD} = f_{\rm ss}(L) + 2$ is $q$-independent and decomposes additively over gauge irreps with multiplicities $(3, 2, 1)$. *Status: theorem (SM, Appendix A).*

13. **Reconstruction theorem and substratum gauge group.** Observed QM with Bell violations, finite boundary entropy, and spatial isotropy, together with the framework's structural assumptions (A1–A6), uniquely determine $[(S, \varphi)]/\mathcal{G}_{\rm sub}$. The gauge group $\mathcal{G}_{\rm sub}$ has four families of generators — state relabeling, alphabet change, deep-sector enlargement, and graph isomorphism up to statistical isotropy — proved to exhaust all observables-preserving transformations via Stinespring uniqueness. Whether $(S, \varphi)$ *is* reality or *describes* reality is provably undecidable — identified as gauge. *Status: theorem (Substratum, §§3–4).*

14. **Structural preconditions for complexity.** The derived structure guarantees, with no free parameters: orbital algebra and the periodic table ($d = 3$ + SO(3)), carbon's tetrahedral bonding geometry, the nuclear-atomic scale hierarchy (two independent gauge groups), water's solvent properties (element 8 in $d = 3$), a thermal window for dynamic chemistry, chiral molecular selection (PVED from the partition), and combinatorial diversity exceeding the autocatalytic threshold by $10^{56}$. The origin of life is the first molecular C1–C3 system; RNA is the unique molecule satisfying all three conditions simultaneously, making the RNA world a structural prediction. C1–C3 systems are exponential-growth attractors — the transition is inevitable. Darwinian evolution follows from imperfect template replication. The viable parameter fraction is ~16%. Fine-tuning and the anthropic principle dissolve. *Status: structural chain + statistical argument (Complexity Paper).*

15. **Non-Markovian dynamics in biology and medicine.** The C1–C3 conditions that produce quantum mechanics at the cosmological scale produce molecular memory at the enzymatic scale. Enzymes, kinases, ion channels, and receptors satisfy C1–C3 through the coupling of fast catalytic domains to slow regulatory/PTM dynamics. The framework identifies *memory asymmetry* — differential dependence on non-Markovian dynamics between disease and normal tissue — as a therapeutic axis distinct from catalytic inhibition. Two structural derivations underpin clinical applications: (a) memory access is necessarily reconstructive (foundation of the reconsolidation paradigm exploited in PTSD therapy), and (b) finite $\tau_B$ at every layer is structurally required (reframing memory disorders as $\tau_B$ pathologies). Applications span cancer, neurodegeneration, PTSD, antibiotic resistance, immunotherapy, cardiac pharmacology, autoimmune disease, epigenetics, and genetic disorder management. Twenty-nine testable predictions distinguish the framework from standard Markovian pharmacology. *Status: predictions with partial existing support (Medical Paper).*

## The Bidirectional Correspondence

The forward derivation and reconstruction theorem establish: $(S, \varphi)$ determines observed physics, and observed physics together with structural assumptions A1–A6 uniquely determines $[(S, \varphi)]/\mathcal{G}_{\rm sub}$. The diagrams below show both directions.

### Forward: From $(S, \varphi)$ to Observed Physics

```
(S, φ) — a finite lossless memory with bounded coupling and statistical isotropy
  │
  ├─→ V (observer) is generic (SM, theorem)
  ├─→ d = 3 from self-consistency (SM, theorem)
  ├─→ QM emergence (Main, theorem)
  ├─→ Wave equation uniquely selected (SM, theorem)
  ├─→ ℏ = c³ε²/(4G), ε = 2l_p (GR, theorem)
  ├─→ Bekenstein-Hawking entropy with 1/4 (GR, theorem)
  ├─→ CC dissolution: 10¹²² = S_dS (GR, theorem)
  ├─→ General relativity (GR, theorem)
  ├─→ Wave eq. → KG → staggered Dirac fermions (SM, theorem)
  ├─→ Center independence = chiral symmetry → Higgs (SM, theorem)
  ├─→ K = 2d = 6 from coupling-degree minimization (SM, theorem)
  ├─→ Cubic group decomposition (3,2,1) → SU(3)×SU(2)×U(1) (SM, theorem)
  ├─→ D_LL = 0 → SU(2) chiral, SU(3) vector-like (SM, theorem)
  ├─→ Anomaly cancellation → unique hypercharges (SM, theorem)
  ├─→ Cubic symmetry + anomaly uniqueness → 3 SM generations (SM, theorem)
  ├─→ Higgs quantum numbers (1, 2, +1/2) (SM, theorem)
  ├─→ θ = 0 from T-invariance (SM, theorem)
  ├─→ θ̄ = 0 at all energy scales from bijection structure (SM, theorem)
  ├─→ Trace-out = Jordan-Chevalley projection (SM Appendix A, theorem)
  ├─→ Weil-Deligne conductor decomposes over gauge irreps (SM Appendix A, theorem)
  ├─→ Dynamical dark energy in Type II RVM functional form (GR §7.1)
  ├─→ Dark-sector concordance (GR §7.2, theorem — total budget)
  ├─→ Dark matter: a₀ = cH/6, v⁴ = GM·cH/6 (GR §7.3, theorem)
  ├─→ Interpolation ν(y) matches galaxies + clusters (GR §7.3)
  ├─→ Bullet Cluster: frozen entropy (GR §7.3)
  ├─→ CMB acoustic peaks: non-oscillating wells = CDM (GR §7.3)
  ├─→ High-z dark matter: a₀(z) = cH(z)/6, declining RCs (GR §7.3)
  ├─→ Gauge couplings: 1/α₀ = 23.25 → all three at M_Z (SM §6)
  ├─→ Cabibbo angle: λ = 1/(π√2) = 0.22508 (SM §7)
  ├─→ Wolfenstein A = √(2/3) (SM §7)
  ├─→ m_d/m_s = 1/(2π²) via GST relation (SM §7)
  ├─→ |V_cb| = √(2/3)/(2π²) (SM §7)
  ├─→ Jarlskog J = η/(12π⁶) (SM §7)
  ├─→ Koide Q = 2/3 from Z₃ symmetry of T₁ (SM §7)
  ├─→ Koide angle θ₀ = C₂/d² = 2/9 → m_e, m_μ from m_τ to <0.01% (SM §7)
  ├─→ Down-quark Koide → m_b from m_s to 0.9% (SM §7)
  ├─→ m_u/m_d = √(2/9) = √θ₀ (0.05σ) (SM §7)
  ├─→ m_t = v/√2 from IR quasi-fixed point (0.9%) (SM §7)
  ├─→ Mass chain: m_s → 6 masses, all within ~1.3% (SM §7)
  ├─→ PMNS angles: TBM + cubic-group corrections (SM §7)
  ├─→ JUNO confirmation: sin²θ₁₂ = 1/3 − 1/(4π²) = 0.3080 vs JUNO 0.3092±0.0087 (0.14σ);
  │                       vs post-JUNO global 0.3085±0.0073 (0.07σ)
  ├─→ Higgs mass: λ(M_Pl) = 0 from composite A₁ taste (SM §7)
  ├─→ Matching mass: m_match = λg₀² = 0.122 (SM §7)
  ├─→ m_b/m_τ = 4.28/Z_S(λg₀²) = 2.36 (SM §7)
  ├─→ Chiral condensate Σ confirmed at L=16–64 (SM §7)
  ├─→ Nested trace-out consistency (GR Appendix, theorem)
  ├─→ Generalized second law (GR Appendix, theorem)
  ├─→ Page curve with t_P ≈ 0.646 t_evap (GR Appendix, theorem)
  ├─→ Structural chain: orbitals → periodic table → carbon → water (Complexity)
  ├─→ Viable parameter fraction ~16% (Complexity)
  ├─→ Chirality: partition → PVED → L-amino acids (Complexity)
  ├─→ Autocatalytic networks (Complexity, statistical — 10⁵⁶ × threshold)
  ├─→ Origin of life = first molecular C1–C3; RNA world predicted (Complexity)
  ├─→ Template replication → Darwinian evolution (Complexity)
  ├─→ Molecular C1–C3: enzyme memory → non-Markovian pharmacology (Medical)
  ├─→ Cancer: memory-priming schedules, memory-targeted drugs (Medical)
  ├─→ Alzheimer's/Parkinson's: τ_B disorder of synaptic kinases (Medical)
  ├─→ PTSD: reconsolidation-blockade as layer-targeted memory editing (Medical)
  ├─→ LIFU: first directly τ_B-targeted therapeutic modality (Medical)
  ├─→ Brain memory hierarchy: synaptic→circuit→systems→cortical (Medical)
  ├─→ Epigenetics: chromatin = biological hidden sector, 5-layer memory (Medical)
  ├─→ Genetic disorders: scheduling, inhibitor prevention, gene therapy (Medical)
  ├─→ Observers structurally restricted to non-equilibrium phase (Main §4.6)
  └─→ Arrow of time from observer-selected non-equilibrium (Main §4.6)
```

### The Gauge Hierarchy

```
Level 3 — Substratum gauge group G_sub (Substratum §4, theorem)
  │  State relabeling: (S, σ∘φ∘σ⁻¹) ~ (S, φ) for any bijection σ
  │  Alphabet change: ℤ/qℤ → ℤ/q'ℤ, all observables q-independent
  │  Deep-sector enlargement: |C_D| is gauge (may be infinite)
  │  Graph isomorphism: any d=3 statistically isotropic graph ~ ℤ³
  │
  │  [trace-out projects Level 3 onto Level 2]
  │
Level 2 — SM gauge group SU(3)×SU(2)×U(1) (SM §4, theorem)
  │  Commutant of coupling matrix M with multiplicities (3,2,1)
  │  Acts on emergent fields within the emergent QFT
  │
  │  [restriction to Hamiltonian projects Level 2 onto Level 1]
  │
Level 1 — D-gauge H → DHD† (GR §3.3, theorem)
     Diagonal unitary basis rephasing of emergent Hamiltonian
     Residual freedom after all transition data extracted

G_sub is the kernel of the reconstruction map: Level 3 ⊃ Level 2 ⊃ Level 1
```

### Reverse: From Observed Physics to $[(S, \varphi)]/\mathcal{G}_{\rm sub}$

```
Observed QM + Bell violations + finite boundary entropy + spatial isotropy
  + structural assumptions A1–A6 (finiteness, determinism, bounded coupling,
    center independence, linearity, background independence)
  │
  ├─→ Stage 1: Stinespring dilation + characterization theorem
  │     → deterministic embedding (S, φ, V) with C1–C3 (Main, theorem)
  │     Determined: existence of (S, φ) with C1–C3
  │     Gauge: state labeling, alphabet size q, deep-sector size |C_D|
  │
  ├─→ Stage 2: Coupling graph + dynamics selection + filter chain
  │     → d = 3, wave equation, SM gauge structure, θ̄ = 0 (SM, theorem)
  │     Determined: d, K, multiplicities (3,2,1), SM content, discrete symmetries
  │     Gauge: specific graph (only statistical isotropy matters)
  │
  └─→ Stage 3: Thermal self-consistency
        → ℏ = c³ε²/(4G), ε = 2l_p (GR, theorem)
        Determined: ℏ, ε, S_BH, all emergent constants

Output: [(S, φ)]/G_sub uniquely determined (Substratum §§3–4, theorem)
  The reconstruction map has kernel G_sub — everything outside the
  equivalence class is fixed by E1–E4 + A1–A6; everything inside is gauge.
```

## Contact

Alex Maybaum — Independent Researcher
[LinkedIn](https://www.linkedin.com/in/amaybaum)
