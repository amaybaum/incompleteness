# The Incompleteness of Observation

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** Draft Pre-Print

---

## Overview

The universe is completely described by a lossless memory with finite read-write access. Physics is what that memory looks like from inside — or equivalently, physics is observable mathematics: the portion of mathematical structure accessible to an embedded observer with partial read-write access.

This research program shows that quantum mechanics, general relativity, and the structure of the Standard Model are consequences of a single primitive: (S, φ) — a finite set and a bijection. S is the storage capacity: the total number of distinguishable states. φ is perfect memory: a reversible update rule that never creates or destroys information. An observer embedded in (S, φ) with partial access — a partition into visible and hidden sectors — reads the visible sector and writes correlations into the hidden sector through coupling; the hidden sector stores those writes and returns them on subsequent reads. The observer necessarily describes the visible sector using quantum mechanics. The conditions are not merely sufficient but necessary: QM and embedded observation are equivalent. For the cosmological application, finiteness is required only for the visible sector and boundary layer — both guaranteed by the holographic entropy bound — while the deep hidden sector may be infinite (Main, §9.6).

The cosmological horizon provides the physical realization. The framework derives ℏ = c³ε²/(4G) from thermal self-consistency, recovers the Bekenstein-Hawking entropy S = A/(4l_p²) including the 1/4 factor, and dissolves the 10¹²² cosmological constant discrepancy — identifying it as the information compression ratio of the observer's quantum description. The same trace-out renders ~95% of the universe's gravitational budget invisible to the emergent QFT, matching the observed dark sector.

The framework is tested for rigidity: the dynamics uniquely selected by the QM requirement also produces all inputs for general relativity — seven independent checks, zero failures. The ontological status of the lattice is resolved: the lattice is the coupling graph of φ, the alphabet size is a gauge freedom, the observer is generic, d = 3 is the unique self-consistent dimension, and (S, φ) is a complete description of reality — whether it *is* reality or *describes* reality is provably undecidable by any measurement, identified by the framework as gauge. The wave equation on a d = 3 lattice uniquely determines the Standard Model's gauge group, matter content, and discrete symmetries — with the primary derivation chain proved end-to-end. The reconstruction theorem establishes the converse: observed QM with Bell violations, finite boundary entropy, and spatial isotropy uniquely determine the equivalence class [(S, φ)]/~ — proving that the mathematical description and the physics are informationally equivalent up to gauge.

## Summary for Non-Specialists

### The Problem

Physics has two foundational theories — quantum mechanics (QM) and general relativity (GR) — that are individually precise and mutually inconsistent. When both are used to compute the energy density of empty space, they disagree by a factor of 10¹²². The standard assumption is that one or both theories contain an error. This framework argues otherwise: neither is wrong, and the discrepancy is a necessary consequence of observation from within.

### The Core Mechanism

An embedded observer — one who is part of the system they are trying to describe — cannot access the complete state. Their description is obtained by summing over all possible hidden states. The framework proves that when the hidden sector is coupled (C1), retains correlations much longer than the observer's measurement timescale (C2), and is large enough that measurements do not appreciably perturb it (C3), the resulting description is necessarily quantum mechanics. The proof rests on P-indivisibility: the transition probabilities cannot be decomposed into independent steps, because finiteness guarantees the system eventually returns to its starting state (recurrence), while coupling ensures distinguishability contracts at short times — producing a non-monotonic trajectory that no memoryless process can replicate.

### The Cosmological Realization

The theorem becomes physics at the cosmological horizon — the boundary beyond which no signal can reach the observer. Stress-energy conservation enforces coupling (C1). The hidden sector's correlation time is the age of the universe (~10¹⁷ s) vs. laboratory timescales (~10⁻¹⁵ s), a ratio of 10⁻³² (C2). The hidden sector has ~10¹²² degrees of freedom (C3). From this single realization, the framework derives ℏ, the Bekenstein-Hawking entropy including the 1/4 factor, and dissolves the 10¹²² discrepancy — identifying it as the information compression ratio of the observer's quantum description. The companion paper derives the Standard Model's gauge group, matter content, and discrete symmetries from the same structure.

### Two Types of Inaccessibility

The framework identifies a distinction between quantities that are *undecidable* (the hidden-sector state h — definite, consequential, provably inaccessible) and quantities that are *gauge* (the alphabet size q and the deep-sector cardinality |C_D| — different values produce identical observables, so the question itself is empty). The hidden state's inaccessibility produces quantum mechanics; the deep sector's inaccessibility means the question "is the universe finite or infinite?" has no empirical content.

### The Incompleteness Family

The framework belongs to a family of results where self-reference under finite resources produces rigid structure: Gödel (1931) — a formal system cannot prove all truths about itself; Turing (1936) — a computer cannot decide all questions about its own behavior; OI — an embedded observer cannot access the complete state. In each case, the structural impossibility determines the form of what the system produces instead.

## Contents

### Main Paper

**"The Incompleteness of Observation: Why Quantum Mechanics and General Relativity Cannot Be Unified From Within"**

Submitted to Foundations of Physics. Establishes the QM–embedded observation equivalence (Part I), applies it to the cosmological horizon (Part II), and derives the dark-sector concordance as a corollary.

- [`Main.md`](Main.md) — Markdown source
- [`Main.tex`](Main.tex) — LaTeX source
- [`Main.pdf`](Main.pdf) — Compiled PDF

### Companion Paper: Fundamental Structure

**"The Fundamental Structure of the Observational Incompleteness Framework: From Finite Bijection to the Standard Model"**

Addresses the ontological status of the lattice, the physical interpretation of (S, φ), and which quantum field theory the embedded observer sees. Shows that the framework's theorems depend on six structural properties and on nothing else. The wave equation is uniquely selected by center independence, isotropy, and linearity (proved). It produces all inputs for Einstein's equations: area-law entropy, Lorentz-invariant dispersion, horizon thermality, and the Jacobson thermodynamic derivation — seven independent links, all analytically proven. The wave equation on a d = 3 lattice uniquely determines the Standard Model's structure: staggered Dirac fermions, chiral symmetry mandating the Higgs, three fermion generations, K = 2d = 6, multiplicities (3, 2, 1) from the cubic group, local gauge invariance from background independence, unique hypercharges from anomaly cancellation, chirality from the trace-out, and θ̄ = 0 at all energy scales. The primary derivation chain is proved end-to-end (29 theorems/lemmas). The reconstruction theorem proves a bidirectional correspondence: observed QM + Bell violations + finite entropy + isotropy ↔ [(S, φ)]/~ up to gauge.

- [`Fundamental.md`](Fundamental.md) — Markdown source
- [`Fundamental.tex`](Fundamental.tex) — LaTeX source
- [`Fundamental.pdf`](Fundamental.pdf) — Compiled PDF

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

4. **Dynamics selection and emergent general relativity.** The wave equation is uniquely selected by center independence, isotropy, and linearity. It produces all inputs for Einstein's equations via Jacobson's thermodynamic route. Seven links, all analytically proven. *Status: theorem.*

5. **Structural foundations.** The lattice is the coupling graph of φ. The alphabet size q is a gauge freedom. The observer is generic (C2 is automatic for Hamiltonian dynamics). d = 3 is the unique self-consistent dimension. The fundamental object is (S, φ): a finite lossless memory. *Status: theorem.*

6. **Standard Model structure.** The wave equation factors into staggered Dirac fermions (theorem). Center independence enforces chiral symmetry, mandating the Higgs (theorem). K = 2d = 6 from coupling-degree minimization — the canonical factorization of the bijection, proved unique for translation-invariant dynamics (theorem). The cubic group decomposition gives multiplicities (3, 2, 1) → SU(3) × SU(2) × U(1) (theorem). Chirality: the trace-out makes SU(2) chiral while SU(3) remains vector-like (theorem). Three SM generations from cubic symmetry + anomaly cancellation uniqueness (theorem). Higgs quantum numbers (1, 2, +1/2) from representation theory (theorem). The primary derivation chain is proved end-to-end; remaining propositions are redundant second-route confirmations.

7. **Strong CP solved.** T-invariance of the wave equation → θ = 0 (theorem). Detailed balance at all time scales (φⁿ is a bijection for every n) → T-invariant Hamiltonian at every energy scale → real Yukawa matrices at every scale → θ̄ = 0 at all energy scales (theorem). No axion needed. The proof bypasses the instanton question entirely.

8. **Dark-sector concordance.** The trace-out producing QM simultaneously renders ~95% of ρ_crit invisible to the emergent QFT. *Status: theorem (total budget); the structured dark matter story is a consistency check, not a derivation.*

9. **Arrow of time.** The substratum (S, φ) has no arrow of time — φ and φ⁻¹ are equally valid. Entropy increase is a property of the observer's coarse-grained description: the standard Boltzmann mechanism applied to the partition. Like QM, the Second Law is emergent.

10. **Falsifiable predictions.** Dark energy evolution with ν_OI ≈ 2.45 × 10⁻³; GW echoes near black hole horizons; θ̄ = 0 exactly (no axion, neutron EDM = 0); no SUSY partners; no fourth generation; Majorana neutrinos. The conjunction is distinctive to this framework.

11. **The trace-out as Jordan-Chevalley projection.** Over finite fields, the evolution matrix F decomposes as F = F_ss · F_u (semisimple × unipotent). The trace-out extracts the semisimple part and erases the nilpotent monodromy N. The Weil-Deligne conductor f_WD = f_ss(L) + 2 is q-independent and decomposes additively over gauge irreps with multiplicities (3, 2, 1). *Status: theorem (Fundamental, Appendix A).*

12. **Reconstruction theorem.** Observed QM with Bell violations, finite boundary entropy, and spatial isotropy uniquely determine the equivalence class [(S, φ)]/~. The SM gauge structure, three generations, θ̄ = 0, and ℏ = c³ε²/(4G) are retrodictions derived within the reconstruction, not inputs to it. The correspondence is bidirectional: the mathematical description and the physics determine each other up to gauge. Whether (S, φ) *is* reality or *describes* reality is provably undecidable by any measurement — the framework identifies this as gauge. *Status: theorem (Fundamental, §10.3).*

## The Bidirectional Correspondence

The forward derivation and the reconstruction theorem together establish a bidirectional correspondence: (S, φ) determines observed physics, and observed physics uniquely determines [(S, φ)]/∼. The mathematical description and the physics are informationally equivalent up to gauge.

### Forward: From (S, φ) to Observed Physics

```
(S, φ) — a finite lossless memory with bounded coupling and statistical isotropy
  │
  ├─→ V (observer) is generic (Fundamental, theorem)
  ├─→ d = 3 from self-consistency (Fundamental, theorem)
  ├─→ QM emergence (Main, theorem)
  ├─→ Wave equation uniquely selected (Fundamental, theorem)
  ├─→ ℏ = c³ε²/(4G), ε = 2l_p (Main, theorem)
  ├─→ Bekenstein-Hawking entropy with 1/4 (Main, theorem)
  ├─→ CC dissolution: 10¹²² = S_dS (Main, theorem)
  ├─→ General relativity (Fundamental §5, seven links — theorem)
  ├─→ Wave eq. → KG → staggered Dirac fermions (Fundamental, theorem)
  ├─→ Center independence = chiral symmetry → Higgs (Fundamental, theorem)
  ├─→ K = 2d = 6 from coupling-degree minimization (Fundamental, theorem)
  ├─→ Cubic group decomposition (3,2,1) → SU(3)×SU(2)×U(1) (Fundamental, theorem)
  ├─→ D_LL = 0 → SU(2) chiral, SU(3) vector-like (Fundamental, theorem)
  ├─→ Anomaly cancellation → unique hypercharges (Fundamental, theorem)
  ├─→ Cubic symmetry + anomaly uniqueness → 3 SM generations (Fundamental, theorem)
  ├─→ Higgs quantum numbers (1, 2, +1/2) (Fundamental, theorem)
  ├─→ θ = 0 from T-invariance (Fundamental, theorem)
  ├─→ θ̄ = 0 at all energy scales from bijection structure (Fundamental, theorem)
  ├─→ Trace-out = Jordan-Chevalley projection (Fundamental App. A, theorem)
  ├─→ Weil-Deligne conductor decomposes over gauge irreps (Fundamental App. A, theorem)
  ├─→ Dark energy ν_OI ≈ 2.45×10⁻³ (Main, proposition)
  ├─→ Dark-sector concordance (Main, theorem — total budget)
  └─→ Arrow of time from coarse-graining (Fundamental, standard Boltzmann)
```

### Reverse: From Observed Physics to [(S, φ)]/∼

```
Observed QM + Bell violations + finite boundary entropy + spatial isotropy
  │
  ├─→ Stage 1: Stinespring dilation + characterization theorem
  │     → deterministic embedding (S, φ, V) with C1–C3 (Main, theorem)
  ├─→ Stage 2: Coupling graph + dynamics selection + filter chain
  │     → d = 3, wave equation, SM gauge structure, θ̄ = 0 (Fundamental, theorem)
  └─→ Stage 3: Thermal self-consistency
        → ℏ = c³ε²/(4G), ε = 2l_p (Main, theorem)

Output: [(S, φ)]/∼ uniquely determined at the lattice level (Fundamental §10.3, theorem)
```

## Contact

Alex Maybaum — Independent Researcher  
[LinkedIn](https://www.linkedin.com/in/amaybaum)
