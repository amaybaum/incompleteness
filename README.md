# The Incompleteness of Observation

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** Draft Pre-Print

---

## Overview

The universe is completely described by a lossless memory with finite read-write access. Physics is what that memory looks like from inside.

A lossless memory is a system whose states evolve by a reversible rule: every state has exactly one predecessor and exactly one successor, so no information is ever created or destroyed. The past is always recoverable from the present. Formally, this is a finite set S of distinguishable states and a bijection φ: S → S. The observer does not have access to the full state — only to a bounded portion called the visible sector. Each step updates both sectors simultaneously, but the observer can only read the visible part. The correlations written into the hidden sector persist there and are returned on subsequent steps. This read-write cycle, not passive observation, is what produces quantum mechanics.

### The problem

Physics has two foundational theories — quantum mechanics (QM) and general relativity (GR) — that are individually precise and mutually inconsistent. When both are used to compute the energy density of empty space, they disagree by a factor of 10¹²². The standard assumption is that one or both theories contain an error. This framework argues otherwise: neither is wrong, and the discrepancy is a necessary consequence of observation from within.

### The starting point

The framework rests on four axioms referencing no quantum mechanics or specific physics: (1) deterministic dynamics — the rule φ is a bijection, (2) finiteness of the observable sector, (3) a causal partition into visible and hidden sectors, and (4) classical probability. No quantum postulates appear. The claim is that quantum mechanics emerges under three conditions on the hidden sector.

### The core theorem

When the hidden sector is coupled (C1), retains correlations much longer than the observer's measurement timescale (C2), and is large enough that measurements do not appreciably perturb it (C3), the observer's reduced description is necessarily quantum mechanics — the Schrödinger equation, the Born rule, and Bell violations all emerge as structural consequences. The conditions are also *necessary*: QM and embedded observation under C1–C3 are equivalent. The proof rests on P-indivisibility: finiteness guarantees recurrence, coupling ensures distinguishability contracts at short times, and recurrence restores it — producing a non-monotonic trajectory that no memoryless process can replicate.

### The cosmological realization

The theorem becomes physics at the cosmological horizon — the boundary beyond which no signal can reach the observer. Stress-energy conservation enforces coupling (C1); the hidden sector's correlation time is the age of the universe vs. laboratory timescales, a ratio of 10⁻³² (C2); the hidden sector has ~10¹²² degrees of freedom (C3). From this single realization, the framework derives ℏ = c³ε²/(4G) from thermal self-consistency, recovers the Bekenstein-Hawking entropy S = A/(4l_p²) including the 1/4 factor, and dissolves the 10¹²² cosmological constant discrepancy — identifying it as the information compression ratio of the observer's quantum description. The same trace-out renders ~95% of the universe's gravitational budget invisible to the emergent QFT, matching the observed dark sector. The entropy displacement mechanism derives dark matter phenomenology from galaxies (a₀ = cH/6, baryonic Tully-Fisher) through clusters (Coma matched to <1%) to the Bullet Cluster (frozen boundary entropy explains the gas-lensing offset).

### The emergent structure

The dynamics uniquely selected by the QM requirement also produces all inputs for general relativity — seven independent checks, zero failures. The lattice is the coupling graph of φ, the alphabet size is a gauge freedom, d = 3 is the unique self-consistent dimension, and the observer is generic. The wave equation on a d = 3 lattice uniquely determines the Standard Model's gauge group, matter content, discrete symmetries, and — through the universal induced coupling 1/α₀ = 23.25 — all three gauge coupling strengths at M_Z, with the primary derivation chain proved end-to-end (29 theorems/lemmas).

### Two types of inaccessibility

The framework identifies a distinction between quantities that are *undecidable* (the hidden-sector state h — definite, consequential, provably inaccessible; the structural consequence is quantum mechanics) and quantities that are *gauge* (the alphabet size q and the deep-sector cardinality |C_D| — different values produce identical observables, so the question itself is empty). The question "is the universe finite or infinite?" has no empirical content — it is identified as gauge.

### The reconstruction and the incompleteness family

The reconstruction theorem establishes the converse: observed QM with Bell violations, finite boundary entropy, and spatial isotropy uniquely determine the equivalence class [(S, φ)]/G_sub — proving that the mathematical description and the physics are informationally equivalent up to gauge. Whether (S, φ) *is* reality or *describes* reality is provably undecidable by any measurement. The framework belongs to a family of results where self-reference under finite resources produces rigid structure: Gödel (a formal system cannot prove all truths about itself), Turing (a computer cannot decide all questions about its own behavior), OI (an embedded observer cannot access the complete state). In each case, the structural impossibility determines the form of what the system produces instead.

## Contents

### Main Paper

**"The Incompleteness of Observation: Why Quantum Mechanics and General Relativity Cannot Be Unified From Within"**

Establishes the QM–embedded observation equivalence (Part I), applies it to the cosmological horizon (Part II), derives the dark-sector concordance as a corollary, and proves the consistency of nested partitions — including the generalized second law and the Page curve — in Appendix B. Predictions include dark energy evolution with ν_OI = (2.45 ± 0.04) × 10⁻³ (§8.1), GW echoes with a computed waveform and fitting factor analysis (§8.2), and dark matter phenomenology from galaxies through clusters to the Bullet Cluster (§8.4).

- [`Main.md`](Main.md) — Markdown source
- [`Main.tex`](Main.tex) — LaTeX source
- [`Main.pdf`](Main.pdf) — Compiled PDF

### Fundamental Structure

**"The Fundamental Structure of the Observational Incompleteness Framework: From Finite Bijection to the Standard Model"**

Addresses the ontological status of the lattice and which QFT the embedded observer sees. Six structural properties suffice; the wave equation is uniquely selected and produces all inputs for Einstein's equations (seven links, all proved). On a d = 3 lattice it uniquely determines the Standard Model: gauge group, matter content, three generations, the Higgs, chirality, θ̄ = 0, and — through the induced coupling 1/α₀ = 23.25 — all three gauge couplings at M_Z to <0.1%. Primary derivation chain: 29 theorems/lemmas. The reconstruction theorem proves the bidirectional correspondence: observed QM + Bell violations + finite entropy + isotropy ↔ [(S, φ)]/G_sub.

- [`Fundamental.md`](Fundamental.md) — Markdown source
- [`Fundamental.tex`](Fundamental.tex) — LaTeX source
- [`Fundamental.pdf`](Fundamental.pdf) — Compiled PDF

### Explainer

**"Why Physics' Biggest Contradiction Might Not Be a Contradiction at All"**

A companion overview covering the full argument — QM emergence, GR derivation, structural foundations, Standard Model structure, the memory interpretation of (S, φ), the relationship between mathematics and physics, and the identification of physics as observable mathematics — with detailed proof walkthroughs, philosophical lineage, observational confrontation (DESI, GW250114, Genzel+2017, McGaugh+2024, Bullet Cluster), and FAQ.

- [`Explainer.md`](Explainer.md) — Markdown source
- [`Explainer.tex`](Explainer.tex) — LaTeX source
- [`Explainer.pdf`](Explainer.pdf) — Compiled PDF

### Complexity

**"The Structural Preconditions for Complexity: Why the Laws of Physics Guarantee the Possibility of Organic Chemistry"**

Traces the consequences of the derived structure through atomic physics, chemistry, prebiotic selection, and the origin of life. The structural chain from (S, φ) to the preconditions for organic chemistry is entirely parameter-free: d = 3 determines orbital structure, the periodic table, carbon's bonding geometry, the nuclear-atomic scale hierarchy, water's solvent properties, and the thermal window. The viable parameter fraction is estimated at ~16%. The chirality chain traces biological homochirality to the partition. Autocatalytic networks are statistically expected (10⁵⁶ × Kauffman threshold). Template replication follows from three independently structural capabilities. The chain extends through evolution, information processing, and AI to a self-referential closure.

- [`Complexity.md`](Complexity.md) — Markdown source
- [`Complexity.tex`](Complexity.tex) — LaTeX source
- [`Complexity.pdf`](Complexity.pdf) — Compiled PDF

## Key Results

1. **QM–embedded observation equivalence.** A stochastic process on a finite configuration space is quantum mechanics if and only if it arises from deterministic dynamics with non-trivial coupling (C1), slow-bath memory (C2), and sufficient hidden-sector capacity (C3). *Status: theorem.*

2. **Derivation of ℏ.** From the cosmological horizon: ℏ = c³ε²/(4G), with ε = 2l_p fixed by self-consistency. The Bekenstein-Hawking entropy formula S = A/(4l_p²) — including the 1/4 factor — is recovered as a consequence. *Status: theorem.*

3. **Cosmological constant dissolution.** The 10¹²² discrepancy is S_dS — the information compression ratio of the emergent quantum description. The observed vacuum energy is the mandatory classical baseline. *Status: theorem.*

4. **Dynamics selection and emergent general relativity.** The wave equation is uniquely selected by center independence, isotropy, and linearity. It produces all inputs for Einstein's equations via Jacobson's thermodynamic route. Seven links, all analytically proven. *Status: theorem.*

5. **Structural foundations.** The lattice is the coupling graph of φ. The alphabet size q is a gauge freedom. The observer is generic (C2 is automatic for Hamiltonian dynamics). d = 3 is the unique self-consistent dimension. The fundamental object is (S, φ): a finite lossless memory. *Status: theorem.*

6. **Standard Model structure.** The wave equation factors into staggered Dirac fermions; center independence mandates the Higgs; K = 2d = 6 from coupling-degree minimization; the cubic group gives multiplicities (3, 2, 1) → SU(3) × SU(2) × U(1); the trace-out makes SU(2) chiral; anomaly cancellation uniquely determines hypercharges and three generations; Higgs quantum numbers (1, 2, +1/2). Primary derivation chain proved end-to-end.

6b. **Gauge coupling prediction.** The fermion-induced coupling gives a universal 1/α₀ = 23.25 at the Planck scale — determined by N_f = 6 and T(R) = 1/2, structural quantities independent of the specific bijection φ. Non-perturbative gauge self-energy corrections (computed from pure-gauge lattice Monte Carlo) and Standard Model RG running reproduce all three gauge couplings at M_Z: 1/α₁ = 59.00, 1/α₂ = 29.57, 1/α₃ = 8.47 — matching observed values to <0.1%. *Status: proposition (Fundamental §9).*

7. **Strong CP solved.** T-invariance of the wave equation → θ = 0 (theorem). Detailed balance at all time scales (φⁿ is a bijection for every n) → T-invariant Hamiltonian at every energy scale → real Yukawa matrices at every scale → θ̄ = 0 at all energy scales (theorem). No axion needed. The proof bypasses the instanton question entirely.

8. **Dark-sector concordance and dark matter.** The trace-out renders ~95% of ρ_crit invisible to the emergent QFT (theorem — total budget). The structured component — entropy displacement via the Clausius relation and Jacobson mechanism — yields a₀ = cH/6 and v⁴ = GM_B · cH/6 (parameter-free). The simple interpolation ν(y) = (1+√(1+4/y))/2 matches galaxies AND clusters (Coma to <1%). The Bullet Cluster: frozen boundary entropy (τ_relax ~ H⁻¹ ≫ t_collision). CMB acoustic peaks: thermodynamic averaging gives non-oscillating wells identical to CDM. High-z: declining rotation curves confirmed (Genzel+2017); stellar TF no-evolution confirmed (McGaugh+2024, gas fraction compensates). *Status: theorem (total budget, acceleration scale); interpolation and CMB pending numerical verification.*

9. **Nested partitions and the Page curve.** Sequential and direct trace-outs agree (Theorems B.1–B.4). The generalized second law follows from strong subadditivity (B.6). The Page curve is derived with t_P ≈ 0.646 t_evap (B.7–B.9). Information is never lost. *Status: theorem.*

10. **Arrow of time.** The substratum (S, φ) has no arrow of time — φ and φ⁻¹ are equally valid. Entropy increase is a property of the observer's coarse-grained description: the standard Boltzmann mechanism applied to the partition. Like QM, the Second Law is emergent.

11. **Falsifiable predictions.** ν_OI = (2.45 ± 0.04) × 10⁻³ (DESI consistent); GW echoes with Δt = (r₊/c)ln(r₊/2l_p) and FF = 0.19 (non-detection consistent); all three gauge couplings at M_Z to <0.1%; θ̄ = 0 exactly; no SUSY, no fourth generation; Majorana neutrinos with normal ordering and Σm_ν near 0.059 eV (DESI+CMB: <0.064 eV); baryonic TF evolves as v⁴ ∝ H(z) (untested). The conjunction is distinctive to this framework.

12. **The trace-out as Jordan-Chevalley projection.** Over finite fields, the evolution matrix F decomposes as F = F_ss · F_u (semisimple × unipotent). The trace-out extracts the semisimple part and erases the nilpotent monodromy N. The Weil-Deligne conductor f_WD = f_ss(L) + 2 is q-independent and decomposes additively over gauge irreps with multiplicities (3, 2, 1). *Status: theorem (Fundamental, Appendix A).*

13. **Reconstruction theorem and substratum gauge group.** Observed QM with Bell violations, finite boundary entropy, and spatial isotropy uniquely determine [(S, φ)]/G_sub. The gauge group G_sub has four generators: state relabeling, alphabet change, deep-sector enlargement, and graph isomorphism up to statistical isotropy. Whether (S, φ) *is* reality or *describes* reality is provably undecidable — identified as gauge. *Status: theorem (Fundamental, §§10.3–10.4).*

14. **Structural preconditions for complexity.** The derived structure guarantees, with no free parameters: orbital algebra and the periodic table (d = 3 + SO(3)), carbon's tetrahedral bonding geometry, the nuclear-atomic scale hierarchy (two independent gauge groups), water's solvent properties (element 8 in d = 3), a thermal window for dynamic chemistry, chiral molecular selection (PVED from the partition), and combinatorial diversity exceeding the autocatalytic threshold by 10⁵⁶. Template replication follows from the structural intersection of linear polymers, complementary pairing, and catalytic activity. Darwinian evolution is the inevitable dynamics of imperfect replication. The viable parameter fraction is ~16%. Fine-tuning and the anthropic principle dissolve. *Status: structural chain + statistical argument (Complexity Paper).*

## The Bidirectional Correspondence

The forward derivation and reconstruction theorem establish: (S, φ) determines observed physics, and observed physics uniquely determines [(S, φ)]/G_sub. The diagrams below show both directions.

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
  ├─→ Dark energy ν_OI = (2.45 ± 0.04)×10⁻³ (Main, proposition)
  ├─→ Dark-sector concordance (Main, theorem — total budget)
  ├─→ Dark matter: a₀ = cH/6, v⁴ = GM·cH/6 (Main §8.4, theorem)
  ├─→ Interpolation ν(y) = (1+√(1+4/y))/2 matches galaxies + clusters (Main §8.4)
  ├─→ Bullet Cluster: frozen entropy (τ_relax ~ H⁻¹ >> t_collision) (Main §8.4)
  ├─→ CMB acoustic peaks: thermodynamic averaging → non-oscillating wells = CDM (Main §8.4)
  ├─→ High-z dark matter: a₀(z) = cH(z)/6, declining RCs (Main §8.4)
  ├─→ GW echoes: Δt = (r₊/c)ln(r₊/2l_p), A₁ = Γ ≈ 0.45 (Main §8.2)
  ├─→ Gauge couplings: 1/α₀ = 23.25 → all three at M_Z (Fundamental §9)
  ├─→ Nested trace-out consistency (Main App. B, theorem)
  ├─→ Generalized second law (Main App. B, theorem)
  ├─→ Page curve with t_P ≈ 0.646 t_evap (Main App. B, theorem)
  ├─→ Structural chain: orbitals → periodic table → carbon bonding → water (Complexity, structural)
  ├─→ Viable parameter fraction ~16% (Complexity, computed)
  ├─→ Chirality: partition → PVED → L-amino acids (Complexity, structural)
  ├─→ Autocatalytic networks (Complexity, statistical — 10⁵⁶ × threshold)
  ├─→ Template replication → Darwinian evolution (Complexity, structural + inevitable)
  └─→ Arrow of time from coarse-graining (Fundamental, standard Boltzmann)
```

### The Gauge Hierarchy

```
Level 3 — Substratum gauge group G_sub (Fundamental §10.4, theorem)
  │  State relabeling: (S, σ∘φ∘σ⁻¹) ~ (S, φ) for any bijection σ
  │  Alphabet change: ℤ/qℤ → ℤ/q'ℤ, all observables q-independent
  │  Deep-sector enlargement: |C_D| is gauge (may be infinite)
  │  Graph isomorphism: any d=3 statistically isotropic graph ~ ℤ³
  │
  │  [trace-out projects Level 3 onto Level 2]
  │
Level 2 — SM gauge group SU(3)×SU(2)×U(1) (Fundamental §7, theorem)
  │  Commutant of coupling matrix M with multiplicities (3,2,1)
  │  Acts on emergent fields within the emergent QFT
  │
  │  [restriction to Hamiltonian projects Level 2 onto Level 1]
  │
Level 1 — D-gauge H → DHD† (Main §5.3, theorem)
     Diagonal unitary basis rephasing of emergent Hamiltonian
     Residual freedom after all transition data extracted

G_sub is the kernel of the reconstruction map: Level 3 ⊃ Level 2 ⊃ Level 1
```

### Reverse: From Observed Physics to [(S, φ)]/G_sub

```
Observed QM + Bell violations + finite boundary entropy + spatial isotropy
  │
  ├─→ Stage 1: Stinespring dilation + characterization theorem
  │     → deterministic embedding (S, φ, V) with C1–C3 (Main, theorem)
  │     Determined: existence of (S, φ) with C1–C3
  │     Gauge: state labeling, alphabet size q, deep-sector size |C_D|
  │
  ├─→ Stage 2: Coupling graph + dynamics selection + filter chain
  │     → d = 3, wave equation, SM gauge structure, θ̄ = 0 (Fundamental, theorem)
  │     Determined: d, K, multiplicities (3,2,1), SM content, discrete symmetries
  │     Gauge: specific graph (only statistical isotropy matters)
  │
  └─→ Stage 3: Thermal self-consistency
        → ℏ = c³ε²/(4G), ε = 2l_p (Main, theorem)
        Determined: ℏ, ε, S_BH, all emergent constants

Output: [(S, φ)]/G_sub uniquely determined (Fundamental §10.3–10.4, theorem)
  The reconstruction map has kernel G_sub — everything outside the
  equivalence class is fixed; everything inside is gauge.
```

## Contact

Alex Maybaum — Independent Researcher  
[LinkedIn](https://www.linkedin.com/in/amaybaum)
