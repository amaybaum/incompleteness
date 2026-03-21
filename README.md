# The Incompleteness of Observation

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** Draft Pre-Print

---

## Overview

This research program shows that quantum mechanics, general relativity, and the Standard Model's gauge structure are structural consequences of embedded observation: an observer in a deterministic system with a causal partition, slow-bath coupling, and sufficient hidden-sector capacity necessarily describes the visible sector using quantum mechanics — and any quantum system requires precisely these conditions. The Schrödinger equation, the Born rule, Bell inequality violations, SU(3) × SU(2) × U(1) with three generations, the Higgs mechanism, and θ̄ = 0 all follow from a single starting point: a finite set, a bijection, and a partition.

**Part I** establishes the QM equivalence as a mathematical theorem, via two independent routes (Barandes' stochastic-quantum correspondence and Stinespring dilation).

**Part II** identifies the cosmological horizon as a physical realization where all conditions hold, derives ℏ = c³ε²/(4G) from partition-relativity and thermal self-consistency (fixing ε = 2 l_p exactly), and dissolves the cosmological constant problem — the 10¹²² discrepancy is the information compression ratio of the trace-out.

**Part III** shows that the same trace-out simultaneously renders ~95% of the universe's gravitational budget invisible to the emergent QFT — matching the observed dark sector — providing independent corroboration of observational incompleteness.

We then test the framework's rigidity by constructing an explicit lattice realization and showing that the dynamics uniquely selected by the QM requirement also produces all the inputs for general relativity — seven independent checks, each of which could have failed, none of which does.

We address the ontological status of the lattice, showing that the framework's results depend on two structural properties of the bijection — bounded coupling degree and statistical isotropy — and on nothing else. The lattice is the coupling graph of the bijection, the alphabet size is a gauge freedom, the observer is generic (any small subgraph sees QM), the dimension d = 3 is the unique self-consistent value, and the fundamental object is (S, φ): a finite set and a bijection. Everything else — including the observer, the dimension, and the laws of physics — is emergent.

Finally, we derive the Standard Model's structure from the same framework: the wave equation factors into staggered Dirac fermions, center independence enforces chiral symmetry (mandating the Higgs), the multi-component extension produces gauge structure from a coupling matrix M, the cubic rotation group decomposes 6 link directions as T₁(3) ⊕ E(2) ⊕ A₁(1) giving SU(3) × SU(2) × U(1), the partition's chirality structure makes SU(2) chiral, anomaly cancellation uniquely determines the hypercharges, and T-invariance of the wave equation forces θ̄ = 0. The filter chain contains no empirical inputs beyond the framework's axioms.

## Contents

### Main Paper

**"The Incompleteness of Observation: Why Quantum Mechanics and General Relativity Cannot Be Unified From Within"**

- [`Main.md`](Main.md) — Markdown source
- [`Main.tex`](Main.tex) — LaTeX source
- [`Main.pdf`](Main.pdf) — Compiled PDF

### Companion Paper: GR

**"Dynamics Selection and Emergent General Relativity in the Observational Incompleteness Framework"**

Tests the framework by constructing the mod-q discrete wave equation on a lattice with a checkerboard partition. The wave equation is the unique dynamics satisfying center independence (necessary for emergent QM), spatial isotropy, and linearity — for any alphabet size q ≥ 2 and dimension d ≥ 1. This dynamics, without tuning, produces area-law entropy, Lorentz-invariant dispersion, horizon thermality, and all inputs to Jacobson's thermodynamic derivation of Einstein's equations. Seven links, all analytically proven. The structural consistency constitutes corroborative evidence for the main paper's central claim.

- [`GR.md`](GR.md) — Markdown source
- [`GR.tex`](GR.tex) — LaTeX source
- [`GR.pdf`](GR.pdf) — Compiled PDF

### Companion Paper: Ontology

**"The Substrate Problem: Structural Foundations of the Observational Incompleteness Framework"**

Addresses the ontological status of the lattice. Shows that the framework's theorems depend on two structural properties of the bijection (bounded coupling degree and statistical isotropy) and on nothing else. The observer is proved generic: any small subgraph of any large bounded-degree bijection satisfies C1–C3. The dimension d = 3 is derived from self-consistency: four independent filters (propagating gravity, stable matter, gravitational concordance, renormalizability) converge on d = 3 as the unique value. The integer dimension is itself derived: self-consistency excludes exponential and fractal graph growth. The product decomposition of the state space into "sites" is derived as the unique factorization minimizing coupling degree. The alphabet size q is a gauge freedom. Background independence is achieved through state-dependent bijections, with the discrete Einstein equation (Ollivier-Ricci curvature = stress-energy) proved as a theorem. The fundamental object is (S, φ): a finite set and a bijection. Everything else is emergent.

- [`Ontology.md`](Ontology.md) — Markdown source
- [`Ontology.tex`](Ontology.tex) — LaTeX source
- [`Ontology.pdf`](Ontology.pdf) — Compiled PDF

### Companion Paper: Standard Model

**"Why These Particles: Standard Model Structure from Observational Incompleteness"**

Derives the Standard Model's gauge group, matter content, chiral structure, and θ̄ = 0 from the OI framework. The argument proceeds in three directions: **Bottom-up** — the wave equation factors into staggered Dirac fermions (Susskind); center independence enforces chiral symmetry, mandating the Higgs; in d = 3, staggered tastes give N_gen = 3. **Gauge emergence** — the multi-component extension produces the matrix wave equation with coupling matrix M as sole parameter; the gauge group is the commutant of M; the factorization principle gives K = 2d = 6; the cubic rotation group decomposes 6 = T₁(3) ⊕ E(2) ⊕ A₁(1), yielding SU(3) × SU(2) × U(1). **Top-down** — anomaly cancellation uniquely determines the hypercharges; D_LL = 0 makes the gauge coupling chiral; T-invariance forces θ̄ = 0. An exact analytical formula is proved: NM = √3 · √⟨μ⁴⟩. The filter chain has 18 steps, zero empirical inputs, and zero identified logical gaps.

- [`SM.md`](SM.md) — Markdown source
- [`SM.tex`](SM.tex) — LaTeX source
- [`SM.pdf`](SM.pdf) — Compiled PDF

### Explainer

**"Why Physics' Biggest Contradiction Might Not Be a Contradiction at All"**

A companion overview covering the logical chain of the full argument — QM emergence, GR derivation, structural foundations, and Standard Model structure — with detailed proof walkthroughs, philosophical lineage, and FAQ. Updated to cover all four companion papers.

- [`Explainer.md`](Explainer.md) — Markdown source
- [`Explainer.tex`](Explainer.tex) — LaTeX source
- [`Explainer.pdf`](Explainer.pdf) — Compiled PDF

## Key Results

1. **QM–embedded observation equivalence.** A stochastic process on a finite configuration space is quantum mechanics if and only if it arises from deterministic dynamics with non-trivial coupling (C1), slow-bath memory (C2), and sufficient hidden-sector capacity (C3). Bell inequality violations and the Tsirelson bound follow from P-indivisibility plus causal locality.

2. **Derivation of ℏ.** From the cosmological horizon: ℏ = c³ε²/(4G), with ε² = 4 l_p² fixed by self-consistency. The Bekenstein-Hawking entropy formula S = A/(4 l_p²) — including the factor of 1/4 — is recovered as a consequence.

3. **Cosmological constant dissolution.** The 10¹²² discrepancy is S_dS — the information compression ratio of the emergent quantum description. The observed vacuum energy is the mandatory classical baseline.

4. **Dynamics selection and emergent GR.** Among all second-order reversible nearest-neighbor dynamics, center independence, isotropy, and linearity uniquely select the wave equation. This dynamics produces all inputs for Einstein's equations via Jacobson's thermodynamic route. Seven links, all analytically proven for both ℝ and ℤ/qℤ, with no free parameters.

5. **Structural foundations.** The lattice is the coupling graph of the bijection. The alphabet size q is a gauge freedom. The observer is generic (any small subgraph sees QM). d = 3 is the unique self-consistent dimension (four independent filters converge). The fundamental object is (S, φ) — a finite set and a bijection. The partition V is derived, not fundamental.

6. **Standard Model structure derived.** The wave equation factors into staggered Dirac fermions. Center independence enforces chiral symmetry, mandating the Higgs. K = 2d = 6 from the factorization principle. The cubic group decomposition 6 = T₁(3) ⊕ E(2) ⊕ A₁(1) gives SU(3) × SU(2) × U(1). The partition's chirality (D_LL = 0) makes SU(2) chiral. Anomaly cancellation uniquely determines the hypercharges. N_gen = d = 3. The filter chain has zero empirical inputs.

7. **Strong CP solved.** T-invariance of the wave equation → θ = 0. Detailed balance of transition probabilities (T_ij = T_ji) → real Yukawa matrices → θ̄ = 0. No axion needed.

8. **NM formula.** Exact analytical result: NM = √3 · √⟨μ⁴⟩, decomposing additively over eigenmodes of M. Proved via Fourier analysis; verified numerically.

9. **Hierarchy problem dissolved.** The Higgs mass is set by the eigenvalue μ_w of the coupling matrix M — a property of the substratum bijection φ, with no radiative corrections.

10. **Falsifiable predictions.** Dark energy evolution with ν_OI ≈ 2.45 × 10⁻³; GW echoes near black hole horizons; θ̄ = 0 exactly (no axion, neutron EDM = 0); no SUSY partners; no fourth generation; no additional gauge groups below M_Pl; Majorana neutrinos (neutrinoless double beta decay); no proton decay from GUT-scale gauge boson exchange. The conjunction is distinctive to this framework.

11. **Dark-sector concordance.** The trace-out producing QM simultaneously renders ~95% of ρ_crit invisible to the emergent QFT — matching the observed dark sector.

12. **Foundational implications.** Wigner's Friend resolved; Everettian measure problem dissolved; Born rule derived; measurement problem dissolved.

## The Derivation Chain

```
(S, φ) — a finite set and a bijection, with bounded coupling and statistical isotropy
  │
  ├─→ V (observer) is generic (Ontology, theorem)
  ├─→ d = 3 from self-consistency (Ontology, theorem)
  ├─→ QM emergence (Main, theorem)
  ├─→ Wave equation uniquely selected (GR, theorem)
  ├─→ ℏ = c³ε²/(4G), ε = 2l_p (Main, theorem)
  ├─→ Bekenstein-Hawking entropy with 1/4 (Main/GR, theorem)
  ├─→ CC dissolution: 10¹²² = S_dS (Main, theorem)
  ├─→ General relativity (GR, seven links)
  ├─→ Wave eq. → KG → staggered Dirac fermions (SM, theorem)
  ├─→ Center independence = chiral symmetry → Higgs (SM, theorem + proposition)
  ├─→ K = 2d = 6, decomposition (3,2,1) → SU(3)×SU(2)×U(1) (SM, theorem)
  ├─→ D_LL = 0 → chiral gauge coupling (SM, proposition)
  ├─→ Anomaly cancellation → unique hypercharges (SM, theorem)
  ├─→ Observer self-consistency → matter representations (SM, proposition)
  ├─→ N_gen = d = 3 (SM, proposition)
  ├─→ T-invariance → θ̄ = 0 (SM, proposition)
  ├─→ Dark energy ν_OI ≈ 2.45×10⁻³ (Main, proposition)
  └─→ Dark gravity (Main, proposition)
```

## Contact

Alex Maybaum — Independent Researcher  
[LinkedIn](https://www.linkedin.com/in/amaybaum)
