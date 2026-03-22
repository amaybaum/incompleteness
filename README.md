# The Incompleteness of Observation

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** Draft Pre-Print

---

## Overview

The universe is completely described by a finite lossless memory. Physics is what that memory looks like from inside — or equivalently, physics is observable mathematics: the portion of mathematical structure accessible to an embedded observer with partial read access.

This research program shows that quantum mechanics, general relativity, and the structure of the Standard Model are consequences of a single primitive: (S, φ) — a finite set and a bijection. S is the storage capacity: the total number of distinguishable states. φ is perfect memory: a reversible update rule that never creates or destroys information. An observer embedded in (S, φ) with partial read access — a partition into visible and hidden sectors — necessarily describes the visible sector using quantum mechanics. The conditions are not merely sufficient but necessary: QM and embedded observation are equivalent.

The cosmological horizon provides the physical realization. The framework derives ℏ = c³ε²/(4G) from thermal self-consistency, recovers the Bekenstein-Hawking entropy S = A/(4l_p²) including the 1/4 factor, and dissolves the 10¹²² cosmological constant discrepancy — identifying it as the information compression ratio of the observer's quantum description. The same trace-out renders ~95% of the universe's gravitational budget invisible to the emergent QFT, matching the observed dark sector.

The framework is tested for rigidity: the dynamics uniquely selected by the QM requirement also produces all inputs for general relativity — seven independent checks, zero failures. The ontological status of the lattice is resolved: the lattice is the coupling graph of φ, the alphabet size is a gauge freedom, the observer is generic, d = 3 is the unique self-consistent dimension, and (S, φ) is a complete description of reality — whether it *is* reality or *describes* reality is provably undecidable by any measurement, identified by the framework as gauge. The question of which quantum field theory the observer sees is addressed in a companion paper deriving the Standard Model's gauge group, matter content, and discrete symmetries — with the primary derivation chain proved end-to-end. The reconstruction theorem establishes the converse: observed physics satisfying five specific conditions uniquely determines the equivalence class [(S, φ)]/~ — proving that the mathematical description and the physics are informationally equivalent up to gauge.

## Contents

### Main Paper

**"The Incompleteness of Observation: Why Quantum Mechanics and General Relativity Cannot Be Unified From Within"**

Submitted to Foundations of Physics. Establishes the QM–embedded observation equivalence (Part I), applies it to the cosmological horizon (Part II), and derives the dark-sector concordance (Part III).

- [`Main.md`](Main.md) — Markdown source
- [`Main.tex`](Main.tex) — LaTeX source
- [`Main.pdf`](Main.pdf) — Compiled PDF

### Companion Paper: GR

**"Dynamics Selection and Emergent General Relativity in the Observational Incompleteness Framework"**

Tests the framework's rigidity. Among all second-order reversible nearest-neighbor dynamics, center independence (necessary for emergent QM), spatial isotropy, and linearity uniquely select the discrete wave equation — for any alphabet size q ≥ 2 and dimension d ≥ 1. This dynamics, without tuning, produces area-law entropy, Lorentz-invariant dispersion, horizon thermality, and all inputs to Jacobson's thermodynamic derivation of Einstein's equations. Seven links, all analytically proven. Self-contained; does not depend on the other companion papers.

- [`GR.md`](GR.md) — Markdown source
- [`GR.tex`](GR.tex) — LaTeX source
- [`GR.pdf`](GR.pdf) — Compiled PDF

### Companion Paper: Ontology

**"The Substrate Problem: Structural Foundations of the Observational Incompleteness Framework"**

Addresses the ontological status of the lattice and the physical interpretation of (S, φ). Shows that the framework's theorems depend on two structural properties of the bijection (bounded coupling degree and statistical isotropy) and on nothing else. The observer is proved generic: any small subgraph of any large bounded-degree energy-conserving bijection satisfies C1–C3, with C2 automatic for Hamiltonian dynamics. The dimension d = 3 is derived from self-consistency: four independent filters converge. The fundamental object (S, φ) is interpreted as a finite lossless memory — S is storage capacity, φ is perfect information preservation — placing the framework in the family of productive incompleteness results alongside Gödel and Turing. The reconstruction theorem proves a bidirectional correspondence: observed lattice-scale physics ↔ [(S, φ)]/~ up to gauge, establishing that whether (S, φ) *is* reality or *describes* reality is itself gauge — provably undecidable by any measurement. Appendix A proves that the trace-out performs a Jordan-Chevalley projection — extracting the semisimple part of the dynamics and erasing the nilpotent monodromy — establishing a precise connection to Weil-Deligne representations in the Langlands program.

- [`Ontology.md`](Ontology.md) — Markdown source
- [`Ontology.tex`](Ontology.tex) — LaTeX source
- [`Ontology.pdf`](Ontology.pdf) — Compiled PDF

### Companion Paper: Standard Model

**"Why These Particles: Standard Model Structure from Observational Incompleteness"**

Derives the Standard Model's gauge group, matter content, chiral structure, and θ̄ = 0 at all energy scales. The primary derivation chain is proved end-to-end (27 theorems); the remaining propositions provide redundant second-route confirmations. **Bottom-up** — the wave equation factors into staggered Dirac fermions; center independence enforces chiral symmetry, mandating the Higgs; in d = 3, staggered tastes give three fermion sectors constituting three complete SM generations (proved via cubic symmetry + anomaly cancellation uniqueness). **Gauge emergence** — coupling-degree minimization uniquely gives K = 2d = 6 (proved); the cubic rotation group decomposes 6 = T₁(3) ⊕ E(2) ⊕ A₁(1), fixing multiplicities (3, 2, 1) (proved); Wilson's lattice gauge construction promotes the commutant symmetry to local gauge invariance. **Top-down** — anomaly cancellation uniquely determines the hypercharges (proved); chirality from the trace-out makes SU(2) chiral while SU(3) remains vector-like (proved); T-invariance forces θ = 0 (proved) and θ̄ = 0 at all energy scales (proved — the bijection structure of φⁿ guarantees detailed balance at every time scale, bypassing the instanton question).

- [`SM.md`](SM.md) — Markdown source
- [`SM.tex`](SM.tex) — LaTeX source
- [`SM.pdf`](SM.pdf) — Compiled PDF

### Explainer

**"Why Physics' Biggest Contradiction Might Not Be a Contradiction at All"**

A companion overview covering the full argument — QM emergence, GR derivation, structural foundations, Standard Model structure, the memory interpretation of (S, φ), the relationship between mathematics and physics, and the identification of physics as observable mathematics — with detailed proof walkthroughs, philosophical lineage, and FAQ.

- [`Explainer.md`](Explainer.md) — Markdown source
- [`Explainer.tex`](Explainer.tex) — LaTeX source
- [`Explainer.pdf`](Explainer.pdf) — Compiled PDF

## Key Results

1. **QM–embedded observation equivalence.** A stochastic process on a finite configuration space is quantum mechanics if and only if it arises from deterministic dynamics with non-trivial coupling (C1), slow-bath memory (C2), and sufficient hidden-sector capacity (C3). *Status: theorem.*

2. **Derivation of ℏ.** From the cosmological horizon: ℏ = c³ε²/(4G), with ε = 2l_p fixed by self-consistency. The Bekenstein-Hawking entropy formula S = A/(4l_p²) — including the 1/4 factor — is recovered as a consequence. *Status: theorem.*

3. **Cosmological constant dissolution.** The 10¹²² discrepancy is S_dS — the information compression ratio of the emergent quantum description. The observed vacuum energy is the mandatory classical baseline. *Status: theorem.*

4. **Dynamics selection and emergent GR.** The wave equation is uniquely selected by center independence, isotropy, and linearity. It produces all inputs for Einstein's equations via Jacobson's thermodynamic route. Seven links, all analytically proven. *Status: theorem.*

5. **Structural foundations.** The lattice is the coupling graph of φ. The alphabet size q is a gauge freedom. The observer is generic (C2 is automatic for Hamiltonian dynamics). d = 3 is the unique self-consistent dimension. The fundamental object is (S, φ): a finite lossless memory. *Status: theorem.*

6. **Standard Model structure.** The wave equation factors into staggered Dirac fermions (theorem). Center independence enforces chiral symmetry, mandating the Higgs (theorem). K = 2d = 6 from coupling-degree minimization (theorem). The cubic group decomposition gives multiplicities (3, 2, 1) → SU(3) × SU(2) × U(1) (theorem). Chirality: the trace-out makes SU(2) chiral while SU(3) remains vector-like (theorem). Three SM generations from cubic symmetry + anomaly cancellation uniqueness (theorem). Higgs quantum numbers (1, 2, +1/2) from representation theory (theorem). The primary derivation chain is proved end-to-end; remaining propositions are redundant second-route confirmations.

7. **Strong CP solved.** T-invariance of the wave equation → θ = 0 (theorem). Detailed balance at all time scales (φⁿ is a bijection for every n) → T-invariant Hamiltonian at every energy scale → real Yukawa matrices at every scale → θ̄ = 0 at all energy scales (theorem). No axion needed. The proof bypasses the instanton question entirely.

8. **Dark-sector concordance.** The trace-out producing QM simultaneously renders ~95% of ρ_crit invisible to the emergent QFT. *Status: theorem (total budget); the structured dark matter story is a consistency check, not a derivation.*

9. **Arrow of time.** The substratum (S, φ) has no arrow of time — φ and φ⁻¹ are equally valid. Entropy increase is a property of the observer's coarse-grained description: the standard Boltzmann mechanism applied to the partition. Like QM, the Second Law is emergent.

10. **Falsifiable predictions.** Dark energy evolution with ν_OI ≈ 2.45 × 10⁻³; GW echoes near black hole horizons; θ̄ = 0 exactly (no axion, neutron EDM = 0); no SUSY partners; no fourth generation; Majorana neutrinos. The conjunction is distinctive to this framework.

11. **The trace-out as Jordan-Chevalley projection.** Over finite fields, the evolution matrix F decomposes as F = F_ss · F_u (semisimple × unipotent). The trace-out extracts the semisimple part and erases the nilpotent monodromy N. The Weil-Deligne conductor f_WD = f_ss(L) + 2 is q-independent and decomposes additively over gauge irreps with multiplicities (3, 2, 1). *Status: theorem (Ontology, Appendix A).*

12. **Reconstruction theorem.** Observed lattice-scale physics satisfying conditions (i)–(v) — QM with Bell violations, the wave equation, SM gauge structure, T-invariance with θ̄ = 0, and ℏ = c³ε²/(4G) — must arise from a member of the equivalence class [(S, φ)]/~. The correspondence is bidirectional: the mathematical description and the physics determine each other up to gauge. Whether (S, φ) *is* reality or *describes* reality is provably undecidable by any measurement — the framework identifies this as gauge. *Status: theorem (Ontology, §8.6).*

## The Derivation Chain

```
(S, φ) — a finite lossless memory with bounded coupling and statistical isotropy
  │
  ├─→ V (observer) is generic (Ontology, theorem)
  ├─→ d = 3 from self-consistency (Ontology, theorem)
  ├─→ QM emergence (Main, theorem)
  ├─→ Wave equation uniquely selected (GR, theorem)
  ├─→ ℏ = c³ε²/(4G), ε = 2l_p (Main, theorem)
  ├─→ Bekenstein-Hawking entropy with 1/4 (Main/GR, theorem)
  ├─→ CC dissolution: 10¹²² = S_dS (Main, theorem)
  ├─→ General relativity (GR, seven links — theorem)
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
  ├─→ Trace-out = Jordan-Chevalley projection (Ontology App. A, theorem)
  ├─→ Weil-Deligne conductor decomposes over gauge irreps (Ontology App. A, theorem)
  ├─→ Reconstruction: lattice physics ↔ [(S,φ)]/~ (Ontology §8.6, theorem)
  ├─→ Dark energy ν_OI ≈ 2.45×10⁻³ (Main, proposition)
  ├─→ Dark-sector concordance (Main, theorem — total budget)
  └─→ Arrow of time from coarse-graining (Ontology, standard Boltzmann)
```

## Contact

Alex Maybaum — Independent Researcher  
[LinkedIn](https://www.linkedin.com/in/amaybaum)
