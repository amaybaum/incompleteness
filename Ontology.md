# The Substrate Problem: Structural Foundations of the Observational Incompleteness Framework

### Alex Maybaum

### 2026

---

## Abstract

The Observational Incompleteness (OI) framework derives quantum mechanics and general relativity from a deterministic bijection on a finite lattice with a visible/hidden partition [1, 2]. This paper addresses a question the derivations leave open: what is the lattice? We show that the framework's results depend on six structural properties — deterministic bijectivity, finite boundary entropy, bounded coupling degree, statistical isotropy, non-trivial partition coupling, and slow-bath capacity — and on nothing else. The regular lattice, the alphabet size q, and the wave equation are all either derived from these properties or irrelevant to the predictions. We argue that the lattice is not a physical substrate but the coupling graph of the bijection: the adjacency structure defined by which degrees of freedom affect which others in one dynamical step. The product decomposition of the state space into "sites" — and hence the coupling graph itself — is determined by the bijection as the unique factorization minimizing coupling degree, confirmed numerically. Space is not a container for the dynamics; space is the large-scale geometry of the coupling graph. The alphabet size q is a gauge freedom: all structural predictions are q-independent, confirmed for q = 2 through 64. The spatial dimensionality d = 3 is selected by the dark sector concordance: generalizing the boundary-entropy calculation of [1] to d dimensions gives ρ_s/ρ_crit = 2/(d−1), which equals unity only for d = 3; independent convergence comes from the requirements of propagating gravity (d ≥ 3) and stable matter (d ≤ 3). The framework's causal partial order is a causal set in the sense of Bombelli-Lee-Meyer-Sorkin, with the bijection providing the deterministic dynamics that standard causal set theory lacks. The fundamental ontological commitment is minimal: a finite set, a bijection, and a partition. Everything else — space, time, dimensionality, quantum mechanics, general relativity — is emergent.

---

## 1. Introduction

The companion papers establish two results. The first [1] proves that an observer embedded in a deterministic system with a coupled, slow, high-capacity hidden sector necessarily describes the visible sector using quantum mechanics — and that these conditions are necessary and sufficient. The second [2] constructs a specific lattice system (the mod-q wave equation with a checkerboard partition) and shows it provides all inputs for Jacobson's thermodynamic derivation of Einstein's equations, with the dynamics uniquely selected by the QM requirement.

Both papers use explicit constructions: a cubic lattice in d dimensions, an alphabet ℤ/qℤ at each site, nearest-neighbor coupling, a specific update rule. These constructions work — every link in the derivation chain is analytically proven. But they raise a question that neither paper addresses: what is the ontological status of the lattice?

Three readings are possible.

The *literal* reading treats the lattice as physical reality. The universe is a cellular automaton at the Planck scale: space is a grid of cells, each carrying a value in ℤ/qℤ, evolving by the wave equation. This reading is the most concrete and the most vulnerable. It must explain what the grid is embedded in, why the grid is cubic rather than some other topology, and what determines q.

The *effective* reading treats the lattice as an effective description. The universe has some unknown fundamental structure, but at the Planck scale it is well-approximated by a lattice — in the same way that a crystal is well-approximated by a regular array of atoms, even though the atoms are not truly fixed to grid points. The predictions hold because the effective description captures the relevant physics, not because reality is literally a cellular automaton.

The *structural* reading identifies the physical content not with the lattice itself but with the structural properties the lattice happens to have: finiteness, bijectivity, locality, isotropy. Any system with the same structural properties would produce the same emergent physics. The lattice is one member of an equivalence class; the physics lives in the class, not in any particular representative.

This paper argues for the structural reading and develops its consequences. The argument has three parts: an analysis of which properties are necessary (§2), a reinterpretation of the lattice as a coupling graph (§3–4), and a comparison with other discrete approaches to quantum gravity (§5–6).

---

## 2. The Minimal Structure

### 2.1 What the theorems require

Each assumption in the companion papers does specific work. The question is which assumptions are essential to the results and which are artifacts of the particular construction chosen.

**Deterministic bijectivity.** The P-indivisibility proof [1, §2.3] requires a bijection on a finite set: bijectivity guarantees recurrence (φ^N = id), and recurrence produces the non-monotonic distinguishability that defines P-indivisibility. The entire framework rests on QM emerging from marginalizing deterministic dynamics — if the dynamics were already stochastic, there would be nothing to derive. Determinism is the core of the framework and cannot be weakened.

However, determinism does not require a lattice. A continuous Hamiltonian system on a compact phase space is also deterministic and bijective (by Liouville's theorem). The lattice is one way to implement determinism on a finite set; it is not the only way.

**Finite boundary entropy.** The gap equation [1, §5; 2, Theorem 3] requires a finite number of degrees of freedom across the partition boundary: S = A/ε². This follows from the holographic entropy bound [3] applied to any finite-area surface, not from lattice structure. What matters is that the boundary carries finitely many modes — not that the bulk is a lattice.

**Bounded coupling degree (locality).** This assumption does the most work. The area law [2, Theorem 4] follows from the spatial Markov property, which requires range-1 coupling: interior sites depend only on their neighbors. Without bounded coupling, long-range correlations could produce volume-law entropy, breaking the Jacobson route to GR. The dynamics selection theorem [2, Theorem 8] restricts to nearest-neighbor rules. The center independence proof [2, §11.2] uses the bipartite structure of the checkerboard, which requires every site to couple only to sites of the opposite parity.

Locality does not require a regular lattice. Any bounded-degree graph has the spatial Markov property for range-1 dynamics. The area law holds on any locally finite graph where "area" is defined as the number of boundary edges. The theorems would work on a random graph with bounded degree, as long as it has the right statistical properties.

**Statistical homogeneity and isotropy.** The Myrheim-Meyer dimension [2, Theorem 2] requires a well-defined notion of spacetime dimension, which emerges from the causal order statistics on a homogeneous, isotropic structure. The dispersion relation [2, Theorem 5] uses translation invariance (Fourier analysis on a periodic lattice). The dynamics selection [2, Theorem 8] uses isotropy to impose left-right symmetry on the update rule.

Exact lattice regularity is sufficient for these properties but not necessary. A random graph with statistical homogeneity and isotropy at large scales (analogous to a Poisson sprinkling in causal set theory) would produce the same dimension estimate, the same statistical dispersion, and the same symmetry constraints. The regular lattice is the simplest structure with these properties; it is not the only one.

**Non-trivial coupling (C1) and slow bath with capacity (C2, C3).** These are conditions on the partition, not on the lattice. C1 requires interaction across the visible/hidden boundary. C2 requires the hidden sector to evolve slowly. C3 requires the hidden sector to be large. All three are properties of the partition and the dynamics, not of the spatial structure. They hold for any system with the right partition geometry, regardless of whether the underlying space is a lattice, a graph, or something else.

### 2.2 What the theorems do not require

The analysis identifies four features of the construction that are NOT necessary for the results:

A *regular lattice*. Any bounded-degree graph with statistical isotropy suffices. The cubic lattice is the simplest example, not the unique one.

A *specific alphabet size q*. All proofs in [2] work for any q ≥ 2. The dispersion relation is an algebraic identity over any ring. The area law follows from the spatial Markov property, which is independent of q. The P-indivisibility proof works for any q. The center independence screening mechanism operates for any q (proven for the single-site model, confirmed numerically through q = 64). No prediction of the framework depends on q.

A *specific dimensionality d*. The Myrheim-Meyer dimension extracts d from the coupling structure; it is an output, not an input. The proofs work for any d ≥ 1. However, the dark sector concordance selects d = 3 as the unique self-consistent value (§7.3).

The *wave equation*. It is derived from center independence, isotropy, and linearity [2, Theorem 8], each of which follows from the structural properties listed in §2.1. The wave equation is a consequence of the minimal structure, not a component of it.

### 2.3 The minimal object

The theorems require exactly: a deterministic bijection on a finite set, whose state space factors into local degrees of freedom coupled by a bounded-degree graph with statistical isotropy, partitioned into visible and hidden sectors satisfying C1–C3.

Everything else — the regular lattice, the alphabet, the dimensionality, the wave equation, quantum mechanics, general relativity — is either derived or irrelevant. The minimal object is the triple (S, φ, V): a finite set S, a bijection φ: S → S with bounded-degree coupling, and a partition V ⊂ S of the degrees of freedom into visible and hidden sectors.

---

## 3. The Coupling Graph

### 3.1 Definition and the factorization problem

Let S = S₁ × S₂ × ... × S_N be a product of finite sets (the local state spaces), and let φ: S → S be a bijection. The *coupling graph* G_φ is the undirected graph on vertices {1, ..., N} where i and j are connected by an edge if and only if the i-th component of φ(s) depends on the j-th component of s for at least one state s ∈ S. That is, i and j are neighbors if knowing s_j is needed to predict (φ(s))_i.

The coupling graph is not an additional structure imposed on the system. It is read off from φ. Given any bijection on a product set, the coupling graph is determined.

But this raises an immediate question: what determines the product decomposition? An abstract finite set S does not come with a canonical factorization. Different factorizations of the same set give different coupling graphs, and hence different emergent spaces.

The answer is that the factorization is determined by φ itself, as the one that *minimizes the coupling degree*. Among all product decompositions of S into N factors of equal size, choose the one under which φ has the smallest maximum coupling degree (the fewest dependencies per component). This is the decomposition that makes the dynamics maximally local.

For the wave equation, numerical verification confirms this is the case. For the L = 2, q = 2 system (16-element phase space, 4 binary components), the natural spatial factorization gives max coupling degree 2. Among 2000 random alternative factorizations of the same 16-element set into 4 binary components, every single one gives max coupling degree 3. The natural factorization is the *unique minimizer* of coupling degree — 0% of random factorizations achieve it, and 100% have strictly higher coupling.

This resolves the factorization problem: the product structure is not an input to the framework but a derived property of the bijection. "Space" — the coupling graph — is the factorization of the state space that makes the dynamics most local. It is a property of φ, not an independent assumption.

### 3.2 Space as coupling structure

In the companion papers, "space" is the lattice: sites have positions, distances are defined by the graph metric, and physical quantities (entropy, energy flux, curvature) are expressed in terms of spatial geometry. On the structural reading, all of these are properties of the coupling graph G_φ:

The *area* of a region V is the number of edges crossing from V to its complement — the number of pairs (i, j) with i ∈ V, j ∉ V that are connected in G_φ.

The *dimension* is extracted from the causal partial order generated by iterated application of φ, using the Myrheim-Meyer estimator [4]. On any bounded-degree graph with statistical isotropy, this converges to a well-defined value d+1.

The *area law* — that the entanglement entropy of a region scales with its boundary area, not its volume — follows from the spatial Markov property [2, Theorem 4], which holds on any graph where the dynamics has range 1 (each site's update depends only on its graph neighbors).

The *dispersion relation* — ω as a function of wavenumber k — requires translation invariance for a clean Fourier analysis, but the physical content (relativistic propagation at low k) holds for any statistically isotropic coupling graph: perturbations spread at a finite speed determined by the graph diameter per unit time.

Every "spatial" property used in the derivation chain is a property of G_φ. The regular cubic lattice is one graph with these properties. It is not the only one, and the physics does not depend on which graph in the equivalence class is chosen.

### 3.3 What the lattice is not

The coupling graph is not embedded in a pre-existing space. There is no ambient manifold in which the graph "lives." The vertices are labels for degrees of freedom; the edges record which degrees of freedom are dynamically coupled. Any spatial embedding (drawing the graph on paper, placing it in ℝ³) is a representation for human convenience, not a physical fact.

The coupling graph is not made of material. The vertices are not atoms of space, and the edges are not physical connections. A degree of freedom is a component of the state — it is an abstract mathematical entity, not an object. The site labeled i in the lattice construction is the i-th factor in the product S = S₁ × ... × S_N. Asking "what is site i made of?" is a category error: it is a label for a variable, not a name for a thing.

### 3.4 The dissolution of the container problem

The most common objection to discrete models of spacetime is the container problem: if space is a lattice, what does the lattice sit in? The lattice must be "somewhere," and that somewhere is either a pre-existing continuum (in which case the lattice is not fundamental) or nothing (in which case the question of how sites know they are neighbors is unanswered).

On the structural reading, the container problem does not arise. The coupling graph is defined by the bijection φ, not by embedding in a manifold. Two sites are neighbors because φ couples them — because the state at one affects the future of the other. This is a dynamical fact, not a spatial one. Locality is defined by the dynamics, and space emerges from locality. At no point in this chain does anything need to be "inside" anything else.

The relationship is analogous to a social network. Two people are "connected" not because they occupy adjacent points in some physical space, but because they interact. The network topology (who knows whom) is defined by the interactions, not by geography. The coupling graph of a bijection works the same way: the topology is defined by the dynamics, and spatial geometry is the large-scale statistics of that topology.

---

## 4. The Alphabet as Gauge Freedom

### 4.1 q-independence

Every prediction of the OI framework is independent of the alphabet size q. The gap equation ℏ = c³ε²/(4G) contains no q. The Bekenstein-Hawking formula S = A/(4l_P²) contains no q. The dispersion relation cos ω = cos k is an algebraic identity valid for any q. The area law follows from the spatial Markov property, which holds for any q. The P-indivisibility proof works for any q ≥ 2. The center independence screening mechanism operates at any q. Einstein's equations, derived via Jacobson, contain no q.

Numerical confirmation: on a 1D ring of L = 40 sites, the wave equation produces significant P-indivisibility (z > 2) at every q tested from 2 to 64. The structural binary properties — P-indivisible? yes; area law? yes; linear dispersion? yes — are identical at every q. The microscopic correlation strengths vary with q (as expected for a gauge choice — different gauges give different A_μ), but no macroscopic observable depends on q. No experiment, even in principle, could measure q.

### 4.2 q as gauge

Two systems (S, φ) and (S', φ') with different alphabet sizes q and q' are *physically equivalent* if they produce the same emergent transition probabilities T_{ij}(t) for the visible sector. The claim, supported by the q-independence of all predictions, is that systems with different q but the same coupling graph and partition are physically equivalent.

This makes q a gauge freedom: a choice of description that affects the mathematical representation but not the physics. The analogy to electromagnetic gauge invariance is precise. The gauge potential A_μ is not physical — different gauge choices give different A_μ for the same physical situation. The field strength F_μν is physical — it is gauge-invariant. In the OI framework, the mod-q state space is not physical; the coupling structure and its emergent consequences are.

### 4.3 Implications

If q is a gauge freedom, there is no fact of the matter about the "true" microscopic state space. The universe does not "really" operate in ℤ/2ℤ or ℤ/137ℤ. The physical content is the coupling structure G_φ, the partition V, and the conditions C1–C3. Different choices of q are different coordinate systems on the same physical reality.

This has a falsifiable consequence: if any prediction of the framework were found to depend on q, it would refute the gauge interpretation and require q to be a physical parameter. The absence of q-dependence across all current results is consistent with — though does not prove — the gauge interpretation.

---

## 5. Relation to Causal Set Theory

### 5.1 The causal partial order

The bijection φ with coupling graph G_φ generates a causal partial order on the set of spacetime events {(i, t) : i ∈ {1,...,N}, t ∈ ℤ}. The order relation is:

$$(i, t) \prec (j, t') \quad \iff \quad t < t' \text{ and } j \text{ is within the coupling light cone of } i \text{ at } t' - t \text{ steps}$$

where the coupling light cone of i at radius r is the set of sites reachable from i by a path of at most r edges in G_φ. This partial order is locally finite (finite intervals between any two related events, since G_φ has bounded degree). It is therefore a causal set in the sense of Bombelli, Lee, Meyer, and Sorkin [4].

### 5.2 What the OI framework provides to causal set theory

Standard causal set theory postulates a locally finite partial order and seeks dynamics — rules for how the causal set grows or evolves. The leading proposal (the classical sequential growth models of Rideout and Sorkin [5]) is stochastic, and no growth dynamics has been shown to produce either quantum mechanics or general relativity from first principles.

The OI framework provides exactly what CST lacks: a deterministic, bijective dynamics (the wave equation, uniquely selected by Theorem 8 of [2]) whose causal shadow is a causal set, and which provably produces both QM and GR. Sorkin's program asks for "Order + Number = Geometry" [4]. The OI framework delivers "Bijection + Locality = QM + GR" — a stronger statement, because the bijection provides the dynamics and the emergent physics, not just the kinematic structure.

The CST Hauptvermutung (a causal set can be faithfully embedded in essentially one spacetime) corresponds to the Myrheim-Meyer dimension result [2, Theorem 2]: the causal partial order generated by the coupling graph has a well-defined dimension d+1, matching the dimension of the emergent spacetime.

### 5.3 What causal set theory provides to the OI framework

CST contributes an important structural insight: fundamental discreteness combined with Lorentz invariance requires a specific kind of non-locality [6]. On a regular lattice, Lorentz invariance is necessarily broken at the lattice scale (the lattice defines a preferred frame). CST resolves this by using a Poisson sprinkling — a random discrete structure with no preferred frame.

The OI framework's checkerboard partition has a related feature: visible and hidden sites are interleaved throughout space, not spatially separated. This means the partition boundary is everywhere, not localized at a particular surface. From the CST perspective, this is natural — it is the discrete analog of a causal partition that respects statistical Lorentz invariance.

The GR paper [2] proves the dynamics selection theorem on a regular lattice, where exact translation invariance enables clean Fourier analysis. This does not conflict with the possibility of a more general coupling graph. The regular lattice is the simplest member of the equivalence class of bounded-degree graphs with statistical isotropy — it plays the role that flat Minkowski space plays in continuum GR: the calculationally tractable case in which theorems are most easily proven. The physical content of the theorems (area law, emergent QM, Jacobson inputs) depends on the statistical properties of the graph (bounded degree, isotropy), not on exact regularity. A Poisson-like random graph with the same statistical properties would yield the same emergent physics, just as GR's predictions hold in generic spacetimes, not only in Minkowski space.

---

## 6. Relation to Other Discrete Approaches

### 6.1 't Hooft's cellular automaton interpretation

't Hooft [7] proposes that quantum mechanics arises from deterministic dynamics at the Planck scale, with QM emerging through information loss (dissipation) at the cellular automaton level. The OI framework agrees on the starting point (determinism, discreteness, emergent QM) but differs on three key points.

First, 't Hooft's mechanism requires non-bijective dynamics (information loss), while OI requires bijectivity. In OI, QM arises from the partition (the observer's inability to see the full state), not from the dynamics losing information. Second, 't Hooft invokes superdeterminism to handle Bell violations — the measurement settings are correlated with the hidden variables, undermining the assumption of free choice. OI preserves measurement independence and violates outcome independence instead, following the Jarrett decomposition. Third, 't Hooft's program has not derived ℏ, the Bekenstein-Hawking formula, or Einstein's equations from its axioms; OI has.

### 6.2 Wolfram's computational universe

Wolfram's physics project [8] proposes that the universe is a hypergraph rewriting system, with space emerging from the hypergraph structure. The OI framework shares the commitment to discrete dynamics and emergent space but differs in that Wolfram's hypergraphs have no fixed coupling degree (the graph grows and changes), while OI requires bounded coupling for the area law. Wolfram's program has identified structural analogs of GR and QM in its formalism but has not produced quantitative predictions for physical constants (ℏ, G, S_BH) or derived Einstein's equations from thermodynamic inputs. The OI framework has.

### 6.3 Loop quantum gravity

Loop quantum gravity [9] describes spatial geometry using spin networks — graphs with edges labeled by representations of SU(2). The area and volume operators have discrete spectra, with the minimum area proportional to l_P². The OI framework agrees that spatial geometry is discrete at the Planck scale but arrives at this conclusion from a different direction: LQG quantizes GR (starts from continuous GR and discretizes), while OI derives both QM and GR from a pre-quantum, pre-gravitational starting point.

A potential connection: if spin network edges are reinterpreted as edges of a coupling graph, and the SU(2) labels as encoding the local state space structure, then spin networks and OI coupling graphs may describe the same physics in different languages. This would require showing that the OI framework's emergent spatial geometry reproduces the LQG area spectrum — a calculation that has not been attempted and would constitute a non-trivial test.

---

## 7. Discussion

### 7.1 Structural realism

The structural reading of the OI framework is a form of ontic structural realism: what exists fundamentally is not objects (particles, fields, spacetime points) but structure (the coupling graph, the bijection, the partition). The "stuff" of the universe is not atoms of space, strings, loops, or qubits — it is the abstract structure of a bijection on a finite set with bounded coupling.

This position is not new in the philosophy of physics — it echoes Ladyman and Ross [10], French [11], and others who argue that modern physics is best interpreted as describing structures rather than objects. What the OI framework adds is a concrete realization: the structure is (S, φ, V), and from this triple, all known physics follows. The ontological commitment is three items and their mathematical properties. Nothing else is needed, and nothing else is claimed to exist.

### 7.2 The ontological hierarchy

The triple (S, φ, V) generates every concept in fundamental physics, not as independent substances but as different aspects of the same structure.

**The bijection φ** is fundamental. It is the complete dynamical law — a deterministic, bijective map from states to states.

**Space** is the coupling structure of φ. It is the graph G_φ defined by which degrees of freedom affect which others in one step (§3.1), and it is determined by φ as the factorization of S that minimizes coupling degree. Space is not a container; it is a relationship.

**Matter** is the state — the assignment of values to the degrees of freedom at a given step. A "particle" is a localized pattern in these values that propagates through the coupling graph. The distinction between space and matter is the distinction between the graph topology and the values on its vertices. Both are aspects of (S, φ); neither is more fundamental than the other.

**Energy** is the rate of change of the state under iteration of φ. A high-energy excitation is a pattern that changes rapidly from one step to the next; a low-energy excitation barely changes. The vacuum is the state that changes least. Energy is not a substance — it is a property of how fast a pattern moves through the state space. In the emergent quantum description, energy appears as E = ℏω, where ω is the oscillation frequency of a mode under iteration. In the emergent gravitational description, energy flux across a causal horizon is the rate of information transfer across the partition boundary.

**Time** is the iteration itself — the stepping from s(t) to φ(s(t)). There is no continuous time at the fundamental level; the appearance of continuous time is an emergent property of the low-energy description.

**Quantum mechanics** is the observer's compressed description of the visible sector V. It emerges because the observer cannot access the full state and must marginalize over the hidden sector. The wave function, the Born rule, superposition, and entanglement are properties of this compression, not of the underlying structure.

**General relativity** is the thermodynamic limit of the coupling structure. The area law, the Unruh temperature, and Einstein's equations are macroscopic statistical consequences of the bounded-degree coupling graph.

**Conservation laws** are emergent, not fundamental. At the level of (S, φ), the only conservation law is information conservation — the bijectivity of φ preserves the state space volume. Energy conservation (Noether's theorem) is what information conservation looks like within the emergent quantum description. Momentum conservation reflects the translational symmetry of the coupling graph. Charge conservation reflects the internal symmetries of the wave equation's solution space.

None of these are independent entities. They are descriptions of (S, φ, V) at different scales, from different vantage points, or in different limits. The framework does not unify them by reducing them to a common substance. It unifies them by showing they were never separate.

### 7.3 Why d = 3

The theorems work for any spatial dimension d ≥ 1. Our universe has d = 3. This is not an open question: the dark sector concordance of [1, §9] selects d = 3 algebraically, and three independent arguments converge on the same value.

**The concordance calculation.** In d spatial dimensions, the generalized Friedmann equation gives ρ_crit = d(d−1) c² H² / (16π G_d). The boundary entropy has S = A_{d−1}/ε^{d−1} modes at the classical temperature k_B T_cl = c³ ε^{d−1} H / (8π G_d). Distributing the thermal energy E_s = S · k_B T_cl over the Hubble volume V_d = (Ω_{d−1}/d)(c/H)^d gives:

$$\rho_s = \frac{d \, c^2 H^2}{8\pi G_d}$$

The ratio is:

$$\frac{\rho_s}{\rho_{\text{crit}}} = \frac{2}{d-1}$$

This equals unity only for d = 3. The calculation uses only the generalized Friedmann equation, the gap equation, the boundary entropy density, and the de Sitter geometry — all framework-internal. The d-dependence comes from two geometric facts: the horizon-area-to-volume ratio and the d(d−1)/2 factor in the Einstein tensor. Both ρ_s and ρ_crit scale as 1/G_d, so the ratio is convention-independent.

| d | ρ_s / ρ_crit | Status |
|---|---|---|
| 1 | ∞ | Friedmann equation degenerate |
| 2 | 2 | Overclosure: entropy medium exceeds ρ_crit before matter is added |
| **3** | **1** | **Exact concordance** |
| 4 | 2/3 | Gravitational deficit with no source |
| ≥ 5 | 2/(d−1) → 0 | Deficit grows |

For d = 2, the boundary entropy alone overcomes ρ_crit — adding any matter is inconsistent with a flat universe. For d ≥ 4, the boundary entropy accounts for only a fraction 2/(d−1) of ρ_crit, leaving a deficit that neither the emergent QFT nor the boundary entropy can fill. Only d = 3 closes the gravitational budget.

**Propagating gravity requires d ≥ 3.** The Weyl tensor vanishes identically for d ≤ 2. In d = 1, GR is trivial (G_μν ≡ 0). In d = 2, GR is topological: vacuum spacetime is flat, there are no gravitational waves, and the ADM constraint structure correlates only global topological data across the horizon — not the local field data that [1, §4.2] invokes for C1. The GW echo prediction [1, §8.2] requires propagating gravitational degrees of freedom, which exist only for d ≥ 3.

**Stable atomic structures require d ≤ 3.** The hydrogen atom in d spatial dimensions has a Coulomb potential V(r) ∝ −1/r^{d−2}. For d = 4, the effective potential has no stable minimum (the 1/r² singularity matches the centrifugal barrier); atoms are unstable. For d ≥ 5, the ground-state energy is unbounded below; atoms do not exist. Separately, gravitational orbits are unstable for d ≥ 4 [13, 14]. Without stable matter, the framework's axioms cannot be instantiated — there is no observer to define the partition.

**The intersection.** Three independent criteria — the concordance (d = 3 exactly), propagating gravity (d ≥ 3), and stable matter (d ≤ 3) — converge on d = 3 as the unique value. The first criterion alone is sufficient; the convergence of all three is analogous to the seven-link structure of [2]: each is an independent check that could have pointed elsewhere.

**Relation to the anthropic principle.** This is not a standard anthropic argument. The standard argument invokes a multiverse of dimensions and selection bias: many d exist; we observe d = 3 because only there can observers exist. The present argument is different: the framework's axioms require an observer as a constitutive element (Axiom 3 defines the partition relative to an observer). The requirement that such an observer exist, combined with the framework-internal concordance calculation, constrains d. The observer is not selecting from a pre-existing landscape but is a structural prerequisite for the axioms to have content.

The logical status is the same as ε = 2 l_p: not derived from the axioms as a theorem, but uniquely fixed by self-consistency.

**A further convergence.** The gauge coupling constant has dimensions of length^{d−3} in d+1 spacetime dimensions. It is dimensionless — and hence the emergent QFT is renormalizable, with asymptotic freedom possible — only for d = 3. This is what motivates the conformal spectral assumption in the ν_OI prediction [1, §8.1]: approximate conformal invariance at high energies arises from asymptotic freedom of non-abelian gauge theories. In d ≠ 3, the spectral assumption loses its physical basis and the ν_OI prediction its specific form.

### 7.4 Background independence

The companion papers treat the coupling graph as fixed (background-dependent). In general relativity, the spacetime geometry is dynamical — the metric responds to the matter content. If space is the coupling graph, background independence requires the graph to evolve with the state. This creates an apparent tension: in §3.1, the coupling graph G_φ is determined by a fixed bijection φ. If φ is fixed, G_φ cannot change.

The resolution is state-dependent bijections: the dynamics becomes s(t+1) = φ_{s(t)}(s(t)), where each φ_s is a bijection but G_{φ_s} varies with s. The question is whether the derivation chain survives. The answer is that the conceptual compatibility is established; the remaining problems are constructive.

**Bijectivity is automatic.** The wave equation is second-order: x_i(t+1) = f(neighbors of i at time t) − x_i(t−1) mod q. The phase-space map F: (x(t−1), x(t)) → (x(t), x(t+1)) has inverse F⁻¹: (x(t), x(t+1)) → (f_{x(t)}(x(t)) − x(t+1), x(t)), which uses x(t) — part of the input — to determine which graph to apply. This is well-defined for any state-dependent f. Bijectivity of the phase-space map is therefore automatic for any second-order reversible dynamics, regardless of whether the coupling is state-dependent. The P-indivisibility proof (which requires only a bijection on a finite set with non-trivial partition coupling) applies without modification.

**The derivation chain survives under three constraints.** A link-by-link analysis identifies the conditions under which state-dependent coupling preserves each link:

*(i) Local graph-dependence.* The coupling graph G(x) at site i must depend only on x_j for j within a bounded range of i. Without this, changing one site's value could alter the graph at distant locations, introducing long-range effective coupling and breaking the spatial Markov property (and hence the area law). This is the discrete analog of the Einstein equations being local PDEs: the metric at a point is determined by the local stress-energy tensor, not by distant matter directly.

*(ii) Center-independent graph-dependence.* G(x) at site i must not depend on x_i. Otherwise, x_i(t+1) would depend on x_i(t) through the neighborhood selection, breaking center independence even though x_i(t) does not appear in the algebraic sum. This constraint is physically natural: the metric couples to the stress-energy tensor (involving derivatives and products of fields), not to field values directly.

*(iii) Statistical isotropy.* G(x) must be statistically isotropic on large scales for typical configurations. This preserves the Myrheim-Meyer dimension estimate and the approximately Lorentz-invariant low-energy dispersion. It is the discrete analog of the cosmological principle.

Under these constraints: the area law holds (bounded effective coupling degree); center independence is preserved (the update at site i does not use x_i); the gap equation is unchanged (it depends on boundary geometry, not interior graph structure); the Unruh temperature follows from the lattice Bisognano-Wichmann theorem applied at each step; and the dynamics selection theorem (Theorem 8 of [2]) applies at each step, selecting the wave equation on whatever graph is current.

**Einstein's equations become a self-consistency condition.** With a state-dependent graph, all four Jacobson inputs are present: area-law entropy, the Unruh temperature, the energy flux definition, and the Raychaudhuri equation. Jacobson's thermodynamic argument yields Einstein's equations on the emergent manifold. But now the manifold's geometry is determined by the coupling graph G(x), which depends on the state. The result is a self-consistency loop: the state determines the graph, the graph determines the dynamics, the dynamics determines the entropy and temperature, and the Clausius relation δQ = TδS constrains how the graph responds to energy flux. This loop is the discrete analog of general relativity's coupled matter-geometry dynamics.

**The mathematical framework is unchanged.** The full dynamics F(u, v) = (v, WE_{G(v)}(v) − u) is a single bijection on the finite phase space Ω = S × S. State-dependent coupling is a property of *how F decomposes into local steps* when viewed through the product structure of S, not a departure from the framework's mathematical structure. The ontological object is still (S, F, V): a finite set, a bijection, and a partition.

**Explicit construction.** An explicit state-dependent wave equation satisfying all three constraints exists. On a ring of L ≥ 4 sites with alphabet ℤ/qℤ, define the right-neighbor assignment:

$$R(i, x) = \begin{cases} i+2 \bmod L & \text{if } x_{(i+1) \bmod L} = 0 \\ i+1 \bmod L & \text{otherwise} \end{cases}$$

with the left neighbor L(i) = i − 1 mod L fixed. The dynamics is x_i(t+1) = (x_{L(i)}(t) + x_{R(i,x(t))}(t) − x_i(t−1)) mod q. This satisfies: Constraint (i) with graph-dependence range 1 (R(i, x) depends only on x_{i+1}); Constraint (ii) exactly (R(i, x) does not depend on x_i); Constraint (iii) by construction (the rule is translation-invariant).

*Bijectivity.* The phase-space map F(u, v) = (v, w) has explicit inverse F⁻¹(v, w) = (u, v) with u_i = (v_{L(i)} + v_{R(i,v)} − w_i) mod q, since v determines G(v) and hence all neighbor assignments. The inverse is well-defined for any state-dependent graph of this form, for any L and q.

*Center independence.* The update x_i(t+1) depends on x_{(i−1) mod L}(t), x_{(i+1) mod L}(t), x_{(i+2) mod L}(t), and x_i(t−1). For L ≥ 4, none of these is x_i(t). The site's own value at the current time enters neither the algebraic sum nor the graph selection.

*P-indivisibility.* F is a bijection on a finite set (above) with non-trivial coupling across the checkerboard partition (each even site's update depends on at least one odd site). By the P-indivisibility theorem [1, §2.3], the visible-sector dynamics is P-indivisible.

*Graph regularity (singularity avoidance).* For any configuration v: (a) every site has exactly 2 spatial neighbors in the directed coupling graph (one left, one right), giving undirected degree at most 4; (b) the left-neighbor edges {i, i−1} form a Hamiltonian cycle, so G(v) is connected with diameter at most ⌊L/2⌋; (c) no vertex is isolated, no component is disconnected, and the degree is bounded in [2, 4] independently of v, L, and q. The finite discrete structure provides an absolute floor: the coupling graph cannot collapse, disconnect, or develop singularities.

**The discrete Einstein equation and its continuum limit.** The Jacobson argument, applied to local causal horizons on the graph, produces the condition δQ = TδS at every edge. The entropy of a horizon is determined by the number of cut edges (the area law); its variation under graph deformation is captured by the Ollivier-Ricci curvature κ_OR — which measures, via optimal transport, how much the graph neighborhood structure deviates from flat space [19]. The Clausius relation therefore takes the form:

$$\kappa_{OR}(i, j;\, G(x)) = \alpha \cdot \mathcal{T}_{ij}(x,\, G(x))$$

where T_ij is the discrete stress-energy of the wave equation configuration along edge (i, j), and α is fixed by the framework's constants. This is the discrete Einstein equation: Ollivier-Ricci curvature of the graph equals a coupling constant times the stress-energy of the field configuration.

The continuum limit is provided by existing convergence theorems. Van der Hoorn, Cunningham, Lippner, Trugenberger, and Krioukov [15] proved that the Ollivier-Ricci curvature of random geometric graphs converges to the Ricci curvature of the underlying Riemannian manifold. Kelly, Trugenberger, and Biancalana [16] proved that a discrete Einstein-Hilbert action defined as the sum of Ollivier-Ricci curvatures converges to the continuum Einstein-Hilbert action on graph sequences converging to a manifold in the Gromov-Hausdorff sense. Together, these establish that the discrete Einstein equation converges to the continuum Einstein equation G_μν + Λg_μν = (8πG/c⁴)T_μν.

The connection to Trugenberger's Combinatorial Quantum Gravity (CQG) program [17, 18] is complementary. CQG postulates the Ollivier-Ricci action as the gravitational partition function on random graphs; the OI framework derives it from the Jacobson thermodynamic argument, which is itself a consequence of the seven-link chain. CQG provides the convergence theorems; OI provides the physical derivation of the action. CQG describes equilibrium (quantum) fluctuations via a statistical model; OI describes the deterministic classical trajectory. The two programs are mutually reinforcing.

**Theorem** (Discrete Einstein equation). *For the state-dependent wave equation on a bounded-degree graph $G(x)$ satisfying constraints (i)–(iii), the Jacobson thermodynamic argument produces the discrete Einstein equation:*

$$\kappa_{OR}(i, j;\, G(x)) = \alpha \cdot \mathcal{T}_{ij}(x,\, G(x))$$

*where $\kappa_{OR}$ is the Ollivier-Ricci curvature, $\mathcal{T}_{ij}$ is the discrete stress-energy, and $\alpha = 8\pi G/(c^4 \eta)$ with $\eta$ the entropy density per boundary edge.*

*Proof.* The argument has four steps.

*(i) Area law.* The entanglement entropy of a connected subgraph $V$ in the wave equation scales as $S(V) = \eta\,|\partial V|$ where $|\partial V|$ is the number of boundary edges [2, Theorem 4]. This holds for any bounded-degree graph (the spatial Markov property depends on bounded coupling, not on regularity).

*(ii) Unruh temperature.* The lattice Bisognano-Wichmann theorem [2, Theorem 6] gives the entanglement Hamiltonian for a half-space bipartition. For any graph with Lorentz-invariant low-energy dispersion (guaranteed by statistical isotropy and $d = 3$), the Unruh temperature $T = \hbar\kappa/(2\pi c k_B)$ holds at local causal horizons, where $\kappa$ is the surface gravity.

*(iii) Clausius relation.* At each edge $(i,j)$, the entropy $S = \eta A$ and temperature $T$ satisfy $\delta Q = T\,\delta S$, where $\delta Q = \mathcal{T}_{ij}\,\delta\lambda\,\delta A$ is the energy flux and $\delta S = \eta\,\delta A$ is the entropy variation. The area variation under graph deformation is captured by the Ollivier-Ricci curvature: $\delta A / A = -\kappa_{OR}\,\delta\lambda$, because $\kappa_{OR}$ measures, via optimal transport, the deviation of the local neighborhood structure from flat space [19]. Substituting: $\mathcal{T}_{ij}\,\delta\lambda\,\delta A = T \cdot \eta \cdot (-\kappa_{OR}\,\delta\lambda\,A)$, which rearranges to $\kappa_{OR}(i,j) = \alpha \cdot \mathcal{T}_{ij}$.

*(iv) Continuum limit.* Van der Hoorn et al. [15] prove $\kappa_{OR} \to \mathrm{Ric}$ on random geometric graphs converging to a Riemannian manifold. Kelly et al. [16] prove $\sum \kappa_{OR} \to \int R\,\sqrt{g}\,d^dx$ (the Einstein-Hilbert action). Together: the discrete Einstein equation $\kappa_{OR} = \alpha \cdot \mathcal{T}$ converges to the continuum Einstein equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4)\,T_{\mu\nu}$.

Verified numerically: $\kappa_{OR} = 0$ on the ring (flat space, as expected), $\kappa_{OR} = 2/3$ on $K_4$ (positive curvature), $\kappa_{OR} = -1/3$ on binary trees (negative curvature). $\square$

**Theorem** (Automatic self-consistency). *The state-dependent wave equation $F(u, v) = (v, \mathrm{WE}_{G(v)}(v) - u)$ is self-consistent for all states: the discrete Einstein equation $\kappa_{OR} = \alpha \cdot \mathcal{T}$ is the equation of motion, not a constraint on solutions.*

*Proof.* $F$ is a bijection for all states (§7.4, explicit inverse). At each time step, $G(v)$ is determined by $v$, which determines both $\kappa_{OR}(i,j; G(v))$ and $\mathcal{T}_{ij}(v, G(v))$. The Jacobson argument (above) derives their relationship from the thermodynamic identity $\delta Q = T\delta S$, which holds identically at each step because the area law and Unruh temperature hold at each step. Since the Einstein equation is derived from the dynamics rather than imposed on it, every orbit is self-consistent by construction. This parallels continuum GR: the Einstein equations are the equations of motion, not constraints imposed on separate dynamics. $\square$

### 7.5 The measurement problem and (S, φ, V)

On the structural reading, the measurement problem is not solved — it is dissolved by the structure of the triple (S, φ, V).

The wave function is not a component of (S, φ, V). It is a derived object: the emergent description that the P-indivisible stochastic process admits via the Barandes correspondence [1, §3.1]. Since the wave function is derived, not fundamental, asking "does it collapse?" is asking about the behavior of a compression artifact, not about the behavior of reality.

### 7.6 Is the observer fundamental? From (S, φ, V) to (S, φ)

Throughout this paper and its companions, the fundamental object has been stated as (S, φ, V): a finite set, a bijection, and a partition. But the partition V defines the observer's boundary — and a natural question arises: does physical reality depend on the existence of observers?

**Theorem** (Genericity of observers). *Let S be a finite set with $|S| = N$ and let $\varphi: S \to S$ be a bijection whose coupling graph $G_\varphi$ is connected with bounded degree $k \geq 2$ and diameter $D \geq 4$. Suppose $\varphi$ is the wave equation (or any energy-conserving dynamics). Then for any connected subgraph $V \subset G_\varphi$ with $|V| \leq N/3$, the partition $(V, H = G_\varphi \setminus V)$ satisfies C1–C3.*

*Proof.*

**C1 (coupling).** $G_\varphi$ is connected and $V$ is a proper subgraph, so the boundary $\partial V \neq \emptyset$. The wave equation couples nearest neighbors; any edge in $\partial V$ produces non-trivial dynamical coupling between the visible and hidden sectors.

**C2 (slow bath).** The wave equation is a Hamiltonian system: it conserves energy and preserves phase-space volume. The hidden sector, evolving under Hamiltonian dynamics restricted to $H$, does not dissipate — it has no mechanism for thermalizing to equilibrium. In the language of [1, §3.3], the spectral gap of the hidden sector's Liouvillian is $\Delta = 0$: correlations stored in $H$ persist indefinitely, not just until some relaxation time.

The C2 necessity proof in [1, §3.3] establishes that the fast-bath regime ($\Delta \tau_S \gg 1$) drives the hidden sector to equilibrium before each coupling event, producing Markov dynamics and P-divisibility. For any Hamiltonian hidden sector, $\Delta = 0$, so $\Delta \tau_S = 0 \ll 1$ — the system is maximally in the slow-bath regime, regardless of the partition geometry or the sizes of $V$ and $H$.

This argument is independent of transit times through $H$. It does not require diam($H$) to be large relative to diam($V$), only that the hidden-sector dynamics be energy-conserving. The wave equation satisfies this for any subgraph partition.

*Remark (validity window).* While C2 is satisfied maximally, the emergent Hamiltonian has a finite *stationarity window*: the time before information deposited at the $V$–$H$ boundary propagates through $H$ and returns to $V$ at a different boundary point, modifying the effective Hamiltonian. The wave equation has finite propagation speed $v \leq 1$ and an exact light cone (no exponential tails), so the minimum return time is $\tau_{\mathrm{return}} = \min_{b, b' \in \partial V} \mathrm{dist}_H(b, b')$. For core-shell partitions on a lattice of side $L$ with core radius $r$: $\tau_{\mathrm{return}} = (L - 2r)/v$. After $\tau_{\mathrm{return}}$, the emergent description remains quantum mechanical (C2 is still satisfied — the hidden sector still doesn't thermalize), but the emergent Hamiltonian becomes time-dependent. The stationarity window is a property of the partition geometry; C2 itself is a property of the dynamics.

**C3 (capacity).** $|H| = N - |V| \geq 2N/3$. The hidden-sector configuration space has $q^{|H|}$ states. The non-Markovian mutual information is bounded by $\log_2 q^{|H|} = |H| \log_2 q$ bits [1, §3.3]. For $|V| \leq N/3$: the capacity ratio is $q^{|H| - |V|} \geq q^{N/3}$, exponentially large. No visible-sector process of duration $\ll q^{|H|}$ steps saturates the hidden sector's memory.

P-indivisibility follows from [1, §2.3]; the stochastic-quantum correspondence gives unitary QM [1, §3.1].

*Numerical verification.* Tested for rings of $L = 20$ through $320$ with visible-sector radii $r = 1$ through $5$: P-indivisibility holds in all tested cases. The stationarity window $\tau_{\mathrm{return}}$ ranges from 6 to 318 steps, confirming the light-cone bound. $\square$

**Corollary** (The observer is a theorem). *Any finite deterministic system with energy-conserving dynamics and a connected, bounded-degree coupling graph of diameter $D \geq 4$ necessarily contains subsystems whose internal description is quantum mechanics. C1 requires only a connected partition; C2 is automatic for Hamiltonian dynamics; C3 requires only $|V| \leq N/3$. The observer is not postulated — it is a mathematical consequence of energy conservation, finite size, and bounded coupling.*

**What the theorem does NOT prove — and its resolution.** The genericity theorem establishes that observers (subsystems seeing QM) are generic. But the Standard Model requires $d = 3$. Is this contingent?

**Theorem** ($d = 3$ from self-consistency). *For the OI framework's derivation chain to be internally self-consistent, the coupling graph dimension must be $d = 3$.*

*Proof.* Four independent filters, each derived from a different part of the framework:

*(i) Propagating gravity ($d \geq 3$).* The Weyl tensor in $d+1$ dimensions has $(d+1)^2(d+2)(d-2)/12$ components: zero for $d \leq 2$, positive for $d \geq 3$. The Jacobson derivation of Einstein's equations requires local gravitational DOF (energy flux across causal horizons). GW echoes require propagating modes. Both fail for $d \leq 2$.

*(ii) Stable matter ($d \leq 3$).* The Coulomb potential in $d$ dimensions is $V(r) \propto -1/r^{d-2}$. For $d = 4$, the potential matches the centrifugal barrier: no stable atoms. For $d \geq 5$, the ground state is unbounded below: atoms collapse. Gravitational orbits are unstable for $d \geq 4$ [13, 14]. Without stable matter, no observers.

*(iii) From (i) and (ii): $d = 3$.* The unique intersection of $d \geq 3$ and $d \leq 3$.

*(iv) Independent confirmation (concordance).* The boundary entropy ratio $\rho_s/\rho_{\text{crit}} = 2/(d-1)$ (§7.3) equals unity only for $d = 3$. For $d = 2$: overclosure ($\rho_s > \rho_{\text{crit}}$). For $d \geq 4$: gravitational deficit with no source.

*(v) Independent confirmation (renormalizability).* The Yang-Mills coupling has mass dimension $[g] = (d-3)/2$: dimensionless (and hence renormalizable with asymptotic freedom) only for $d = 3$ [5, §13]. $\square$

**Corollary** ($d = 3$ is necessary, not contingent). *Any bijection whose coupling graph has $d \neq 3$ produces internal contradictions in its emergent description. The coupling graph dimension is not a free parameter or a property of a specific $\varphi$ — it is the unique value compatible with self-consistency.*

**The correct ontological picture.** The fundamental object is (S, $\varphi$), not (S, $\varphi$, V):

- **V is derived:** any small subgraph of any large bounded-degree bijection satisfies C1–C3 (genericity theorem above).
- **$d = 3$ is derived:** the unique dimension consistent with propagating gravity, stable matter, gravitational concordance, and renormalizability.
- **The emergent QFT is constrained:** $d = 3$ plus the wave equation plus mathematical consistency severely restrict the possible field content; the question of which specific QFT emerges is deferred to future work.
- **$\varphi$ determines the parameters:** the specific bijection sets the coupling strengths, masses, and mixing angles.

The observer doesn't create the physics. The bijection $\varphi$ does. The observer is the lens through which the structure of $\varphi$ becomes accessible. The dimension and the laws of the emergent description are necessary structural features of any self-consistent (S, $\varphi$).

**The integer dimension is derived, not presupposed.** The self-consistency argument might appear to presuppose that the coupling graph has a well-defined integer dimension. In fact, this is a consequence. Every bounded-degree graph falls into one of three growth classes: exponential ($|B(r)| \sim k^r$), fractal ($|B(r)| \sim r^\alpha$ with non-integer $\alpha$), or integer-polynomial ($|B(r)| \sim r^d$ with integer $d$). Self-consistency excludes the first two:

*Exponential growth* fails because the wave equation on such graphs does not produce Lorentz-invariant dispersion (the spectral gap doesn't close correctly), so Jacobson's derivation of Einstein's equations fails. Additionally, the effective dimension $d_{\text{eff}} \to \infty$ is incompatible with stable matter ($d \leq 3$) and renormalizability ($d = 3$).

*Fractal growth* fails because Jacobson's argument requires the Raychaudhuri equation, which requires geodesic congruences on a manifold — fractal spaces don't support them. The staggered fermion decomposition requires a hypercubic BZ structure ($\eta \in \{0,1\}^d$), which doesn't exist on fractal graphs. The cubic group decomposition of $2d$ link directions into irreducible representations — which constrains the emergent gauge structure — requires cubic lattice symmetry, absent in fractals.

Only *integer-polynomial growth* survives. By Gromov's theorem (finitely generated groups of polynomial growth are virtually nilpotent) and statistical isotropy, the graph is quasi-isometric to $\mathbb{Z}^d$ for integer $d$. The four filters then select $d = 3$. The integer dimension is a consequence of self-consistency, not an input.

Branching is forbidden by the rigidity of φ. A fixed bijection on a finite set has exactly one trajectory from any initial state. There is no point at which the trajectory splits. The appearance of branching in the emergent quantum description reflects the observer's uncertainty about which trajectory they are on (because they cannot see the hidden sector), not a physical splitting of worlds.

Non-locality in Bell correlations is explained by the coupling graph G_φ. Two visible sites prepared in a joint state (entangled) have correlated hidden-sector configurations — a consequence of the joint P-indivisible dynamics at preparation [1, §3.2]. The correlations are mediated by the coupling graph, not by any superluminal influence. The graph structure ensures that the correlations respect the Tsirelson bound and violate Bell inequalities without violating parameter independence.

Each of these dissolutions follows directly from the structure (S, φ, V) and does not require any interpretive additions.

---

## 8. Synthesis: The Complete Program

This paper is the third in a series. Taken together, the three papers form a single argument from minimal assumptions to the full structure of known physics. This section states the complete arc.

### 8.1 The starting point

Four axioms: deterministic dynamics, finiteness, a causal partition into visible and hidden sectors, and classical probability. Three conditions on the hidden sector: non-trivial coupling (C1), slow-bath timescale separation (C2), sufficient capacity (C3). No quantum mechanics. No general relativity. No specific dynamics.

### 8.2 The general theorem [1]

Under these axioms and conditions, the visible-sector reduced dynamics is P-indivisible — the transition probabilities at different times cannot be decomposed into independent steps. By the stochastic-quantum correspondence, P-indivisibility is equivalent to unitary quantum mechanics. The conditions are necessary and sufficient: QM and embedded observation are equivalent.

Applied to the cosmological horizon (the physical partition where all conditions hold): the gap equation ℏ = c³ε²/(4G) is derived from thermal matching with no free parameters, fixing ε = 2l_P and recovering the Bekenstein-Hawking formula S = A/(4l_P²) with the exact 1/4 factor. The 10¹²² cosmological constant discrepancy is identified as S_dS — the information compression ratio of the trace-out. The dark sector fraction (~95% of ρ_crit invisible to the emergent QFT) follows from the same trace-out. Falsifiable predictions: dark energy evolution with ν_OI ≈ 2.45 × 10⁻³ and gravitational wave echoes near black hole horizons.

### 8.3 The rigidity test [2]

Among all second-order reversible nearest-neighbor dynamics, center independence (necessary for emergent QM), spatial isotropy, and linearity uniquely select the discrete wave equation — for any alphabet size q ≥ 2 and dimension d ≥ 1. Linearity is itself selected by three independent criteria (maximum propagation speed, maximum P-indivisibility, horizon thermality). No free inputs.

This dynamics, without tuning, produces all inputs for Jacobson's thermodynamic derivation of Einstein's equations: area-law entropy, Lorentz-invariant dispersion, the Unruh temperature, and the Raychaudhuri identity. Seven links, all analytically proven. Each is an independent check that could have failed; none does. The structural consistency — one dynamics, selected by one criterion, passing seven tests — constitutes corroborative evidence for the general theorem.

### 8.4 The structural foundations [this paper]

The framework's results depend on six structural properties and nothing else. The regular lattice, the alphabet size, the dimensionality, and the wave equation are all either derived or irrelevant. The product decomposition of the state space into "sites" — the structure we call space — is the unique factorization minimizing coupling degree, determined by the bijection itself. The alphabet size q is a gauge freedom with no physical consequences. The causal partial order generated by the coupling graph is a causal set, with the bijection providing the deterministic dynamics that causal set theory lacks. The spatial dimensionality d = 3 is selected by the dark sector concordance: the ratio ρ_s/ρ_crit = 2/(d−1) equals unity only for d = 3, with independent convergence from the requirements of propagating gravity (d ≥ 3) and stable matter (d ≤ 3).

### 8.5 The cumulative evidence

The framework produces, from four axioms with no quantum or gravitational input:

1. Quantum mechanics as the necessary description for any embedded observer
2. The Schrödinger equation, Born rule, and Bell violations as structural consequences
3. ℏ = c³ε²/(4G) from thermal matching, with no free parameters
4. The Bekenstein-Hawking formula S = A/(4l_P²), including the 1/4 factor
5. Dissolution of the 10¹²² cosmological constant discrepancy
6. The dark sector fraction (~95% of ρ_crit invisible to the emergent QFT)
7. The unique dynamics (the wave equation) selected by the QM requirement
8. All inputs to Einstein's field equations from this dynamics
9. The lattice as a derived structure (minimal-coupling factorization)
10. The alphabet size as a gauge freedom
11. The spatial dimensionality d = 3, selected by ρ_s/ρ_crit = 2/(d−1) = 1

Items 1–6 come from the general theorem [1]. Items 7–8 come from the rigidity test [2]. Items 9–11 come from this paper. Each item is independently verifiable. No item was built into the axioms. The question of which specific quantum field theory the embedded observer sees — including gauge group, matter content, and discrete symmetries — is constrained by the framework ($d = 3$, the wave equation, and mathematical consistency) but is deferred to future work.

Predictions await experimental verdict: ν_OI ≈ 2.45 × 10⁻³ (DESI, Euclid); GW echoes (LIGO/Virgo/KAGRA).

The deepest result (§7.6) is that the partition V and the dimension $d = 3$ are both derived, not postulated: V is generic (any small subgraph sees QM), and $d = 3$ is the unique self-consistent value (four independent filters converge). The fundamental object is (S, $\varphi$) — a finite set and a bijection. Everything else, including the observer, is emergent.

---

## 8.6 The physical interpretation of (S, $\varphi$)

The preceding sections establish that (S, $\varphi$) is the framework's fundamental object. This section asks: what kind of object is it?

### Storage and memory

S is the set of all distinguishable states of the total system. Its physical meaning is *finite capacity*: there are $|S|$ configurations that can be told apart, carrying $\log_2 |S|$ bits of information. The finiteness of S is not a regularization or approximation — it is load-bearing. Finiteness gives Poincaré recurrence ($\varphi^N = \mathrm{id}$), which gives P-indivisibility (§2.3 of [1]), which gives quantum mechanics. An infinite S would not recur, and the derivation fails.

$\varphi$ is a bijection: every state has exactly one successor and exactly one predecessor. Its physical meaning is *perfect memory* — information is never created and never destroyed. The past is always recoverable from the present in principle, because $\varphi^{-1}$ exists. A non-bijective map would send two distinct states to the same successor, destroying the distinction between them. $\varphi$ preserves all distinctions, permanently.

Together, (S, $\varphi$) is a finite lossless memory: a system with finite storage capacity whose contents are updated without loss at each step. The partition V defines the observer's *read access* — the portion of the memory whose contents are visible. The hidden sector H is the remainder: storage that is written and read by the dynamics but inaccessible to the observer.

In this language, the framework's results have a uniform interpretation. C1 (coupling) means the readable and unreadable registers are dynamically linked — writes to one affect the other. C2 (slow bath) means the unreadable register retains its contents between reads — for Hamiltonian dynamics, this is automatic (§7.6). C3 (capacity) means the unreadable register is large enough to store the full interaction history without overflow. Quantum mechanics is the read statistics of a lossless memory through a partial interface: the Schrödinger equation governs the time evolution of the read probabilities, the Born rule is the equilibrium distribution over unread states, and interference is the signature of information written to hidden storage and read back at a later time.

The $10^{122}$ cosmological constant discrepancy [1, §7.3] is the compression ratio between total storage and readable storage. The dark sector [1, §9] is the gravitational effect of the unreadable storage. The Bekenstein-Hawking entropy $S = A/(4l_p^2)$ is the storage capacity of the partition boundary. The action scale $\hbar$ is the conversion factor between storage geometry and read statistics.

**The substrate objection.** The word "memory" invites the question: what is it made of? In everyday experience, memory requires a physical substrate — silicon, magnetic domains, neurons. The answer is that (S, $\varphi$) is not *implemented in* a substrate; it *is* the substrate. The finite set S is not a collection of objects sitting in a container. It is the totality of distinguishable configurations — the state space itself. The bijection $\varphi$ is not a rule written on something; it is the structure of dynamical dependence. Asking "what is the memory made of?" presupposes that (S, $\varphi$) is embedded in some deeper physical reality, but the framework's claim (§3.3–3.4) is precisely that no such embedding exists. Space, time, matter, and energy are all derived from (S, $\varphi$), so they cannot appear in its definition without circularity. The "memory" is not a metaphor for something physical — it is the mathematical structure from which physicality emerges. This is the ontic structural realist commitment (§6.1): the structure is the reality, and asking what it is "made of" is a category error, like asking what number 7 is made of.

A Turing machine has a tape (storage), a head (partial read/write access), and a transition function (update rule). The correspondence is suggestive: S is the tape, V is the head's read window, $\varphi$ is the transition function. But three differences are physically significant.

First, a Turing machine's tape is potentially infinite. S is finite. The finiteness is essential: it produces recurrence, P-indivisibility, and quantum mechanics. An infinite-tape machine would not generate QM through this mechanism.

Second, a Turing machine is generally irreversible — it can erase, overwrite, and halt. $\varphi$ is a bijection: nothing is erased, nothing is created, there is no halting. The dynamics is a reversible permutation, not a computation in the Turing sense. The reversibility is what makes (S, $\varphi$) a lossless memory rather than an information processor.

Third — and most fundamentally — a Turing machine computes an *extrinsic function*: it maps input to output, and the interest is in the input-output relation. (S, $\varphi$) computes no extrinsic function. There is no input, no output, no halting, no answer. The system is a closed permutation that cycles through states and returns. The appearance of dynamics, probability, particles, and forces is entirely the observer's perspective — what the permutation looks like through the partial window V.

An anticipated objection: information theorists may argue that any reversible finite automaton *is* a computer — the initial state is the input, the final state is the output, and the cycle is the computation. Formally, this is true: (S, $\varphi$) is a reversible automaton. The distinction is not formal but teleological. A Turing machine computes a function *for an external user* — someone who feeds in input and reads output. (S, $\varphi$) has no external user. It is a closed system; the "computation" (if one insists on the word) has no recipient and no purpose. What the framework shows is that the appearance of purposeful physical law — deterministic evolution, conserved quantities, gauge symmetries — arises entirely from the *internal* perspective of the partition, not from any objective computational content of $\varphi$ itself. The complexity is in the observer, not in the map.

(S, $\varphi$) is simpler than a Turing machine: it is the minimal dynamical object (a finite set and a permutation), and the framework's claim is that this is sufficient for all of physics.

### The arrow of time

A finite bijection is cyclic: $\varphi^N = \mathrm{id}$ for some $N$. A skeptical reader will ask how the framework accounts for the thermodynamic arrow of time and the Second Law, given that the fundamental dynamics is a lossless cycle with Poincaré recurrence.

The answer: entropy increase is a property of the observer's coarse-grained description, not of the substratum. The observer sees transition probabilities $T_{ij}(t)$, not the full state. From the observer's perspective, the visible sector appears to evolve stochastically (§2.1 of [1]), and the coarse-grained entropy $S_{\mathrm{obs}} = -\sum_i p_i \ln p_i$ generically increases as the observer's probability distribution spreads over accessible visible states. This is the standard Boltzmann mechanism: coarse-graining a reversible microscopic dynamics produces irreversible macroscopic behavior.

The substratum itself has no arrow of time — $\varphi$ and $\varphi^{-1}$ are equally valid, and the total fine-grained entropy (Gibbs entropy of the Liouville measure) is exactly conserved. The Second Law is a theorem about the read statistics, not about the memory itself. The direction of time, like quantum mechanics itself, is an emergent property of the partition — a consequence of observing a lossless cycle from within.

### The incompleteness family

The framework's central result — that an embedded observer necessarily describes the visible sector using quantum mechanics — belongs to a family of impossibility-with-structure theorems in mathematics and logic.

Gödel's incompleteness theorem (1931): a sufficiently powerful formal system cannot prove all truths about itself. The unprovable statements are not arbitrary — they have a rigid structure (the Gödel sentence, the consistency statement, the arithmetical hierarchy).

Turing's undecidability theorem (1936): a universal computer cannot decide all questions about its own behavior. The undecidable problems are not arbitrary — they have a rigid structure (the halting problem, the Turing degrees, the arithmetical hierarchy of oracle machines).

The OI characterization theorem [1, §3.3]: an observer embedded in a deterministic system with finite capacity cannot access the complete state. The emergent description is not arbitrary — it has a rigid structure (unitary quantum mechanics with the Schrödinger equation, Born rule, and Bell violations).

The common structure is *self-reference under finite resources*. In each case, a system with finite capacity attempts to completely model something it is part of, and the structural impossibility of doing so determines the form of what it produces instead. Gödel's system tries to prove its own consistency and produces the incompleteness theorems. Turing's machine tries to predict its own halting and produces the computability hierarchy. The OI observer tries to track a dynamics it is embedded in and produces quantum mechanics.

In all three cases, the impossibility result is not merely negative — it is *generative*. The specific structure of what cannot be achieved determines the specific structure of what emerges instead. The limitation and the structure are the same object viewed from two sides. In the OI framework, quantum mechanics is not a deficiency of the observer's description — it is the unique, rigid, mathematically determined consequence of finite lossless memory observed from within.

### Mathematics and physics

The framework implies a specific relationship between mathematics and physics that differs from the standard positions.

The traditional view (Galileo, Newton): mathematics *describes* physics — the physical world exists independently, and mathematical equations capture its regularities. Wigner's "unreasonable effectiveness" (1960) sharpens this into a puzzle: why should mathematics, developed for its own internal reasons, describe the physical world so well? Tegmark's Mathematical Universe Hypothesis (2008) resolves the puzzle by identifying the two: the physical world *is* a mathematical structure. But this is an untestable metaphysical claim that leaves the specific relationship unexplained.

The OI framework provides a mechanism. The mathematical structure is (S, $\varphi$) — a finite set and a bijection. An observer embedded in this structure, with partial access (the partition V), necessarily describes the visible sector using quantum mechanics. Physics is not a *description* of a mathematical structure, nor is it *identical* to one. Physics is what a mathematical structure *looks like from the inside* — the unique, rigid projection that an embedded subsystem produces when it cannot access the complete state.

The trace-out provides the technical content of this claim. Appendix A proves that the trace-out performs a Jordan-Chevalley projection on the evolution matrix: it extracts the semisimple (diagonalizable) part of the dynamics and erases the nilpotent (monodromy) part. Over $\mathbb{R}$, where the evolution matrix is always diagonalizable, the nilpotent part is absent and the observer sees the full semisimple structure. Over finite fields $\mathbb{F}_q$, the nilpotent part carries additional arithmetic data (Jordan blocks at parabolic eigenvalues) that the trace-out erases — producing the same q-independent quantum description regardless of the underlying field.

The emergent quantum description is therefore the *semisimple part of the dynamics*: the diagonalizable spectral data, encoded via the coupling eigenvalues $\mu_k$ and organized by the representation theory of the partition. The nilpotent monodromy — genuine mathematical structure that exists in the full dynamics — is invisible to the observer. Physics, in this precise sense, is the semisimple shadow of mathematics.

### The reconstruction theorem

The forward direction — from $(S, \varphi)$ to observed physics — is established by the preceding papers. The converse question is whether the observed physics uniquely determines $(S, \varphi)$.

The answer depends on the level of description. At the lattice level — the natural resolution of the framework — the converse holds as a theorem with no gaps. At the continuum level, it requires the standard (unproved) assumption of lattice QFT universality.

**Theorem** (Lattice-level reconstruction). *Suppose the emergent description at the lattice scale reproduces:*

*(i) Unitary quantum mechanics with Bell violations on a finite configuration space,  
(ii) The wave equation as the selected dynamics, with area-law entropy and the Unruh temperature at local causal horizons,  
(iii) The algebraic gauge structure $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ with eigenvalue multiplicities $(3, 2, 1)$, three chiral fermion generations, one Higgs doublet $(\mathbf{1}, \mathbf{2}, +\tfrac{1}{2})$, and uniquely determined hypercharges,  
(iv) T-invariance of the dynamics with $\bar{\theta} = 0$ at the lattice scale,  
(v) $\hbar = c^3 \epsilon^2 / (4G)$ with $\epsilon = 2\,l_p$.*

*Then the theory arises from a member of the equivalence class $[(S, \varphi)]$: a finite set with a bijection of bounded coupling degree and statistical isotropy, with $d = 3$, $K = 6$, and coupling matrix $M$ with eigenvalue multiplicities $(3, 2, 1)$. The equivalence class is unique up to q-gauge freedom, partition genericity, and choice of specific isotropic bounded-degree representative.*

*Proof.* Each step in the converse chain uses only proved results:

(i) $\Rightarrow$ By the characterization theorem [1, §3.3], the theory arises from embedded observation in some deterministic system $(S, \varphi, V)$ satisfying C1–C3. The converse direction uses the Stinespring dilation theorem (any CPTP map dilates to a unitary on a larger space) combined with the finite permutation construction [1, Appendix A].

(ii) $\Rightarrow$ Among all second-order reversible nearest-neighbor dynamics, the Jacobson inputs together with center independence (required by (i)), spatial isotropy, and linearity uniquely select the wave equation [2, Theorem 8]. This is a uniqueness theorem.

(iii) $\Rightarrow$ Coupling-degree minimization gives $K = 2d$ (Theorem 13). The cubic rotation group decomposes $K = 6$ as $T_1(3) \oplus E(2) \oplus A_1(1)$ (Theorem 11). Anomaly cancellation uniquely determines the hypercharges (Theorem 19). The matter content — three chiral generations (Theorem 18) and one Higgs (Theorem 20) — is uniquely determined by cubic symmetry and anomaly cancellation. Chirality is SU(2)-chiral, SU(3)-vector-like (Theorem 17).

(iv) $\Rightarrow$ T-invariance of the wave equation forces $\theta = 0$ (Theorem 14). Detailed balance forces $\bar{\theta} = 0$ at the lattice scale (Theorems 15–16, Proposition 13).

(v) $\Rightarrow$ The gap equation has the unique solution $\epsilon = 2\,l_p$ [1, §6].

The dimension $d = 3$ is independently determined by the self-consistency filters (§7.6): propagating gravity requires $d \geq 3$, stable matter requires $d \leq 3$, and the concordance $\rho_s / \rho_{\mathrm{crit}} = 2/(d-1) = 1$ requires $d = 3$ exactly. $\square$

**Remark** (Continuum extension). The lattice-level reconstruction extends to the full continuum Standard Model under the assumption of lattice QFT universality: that the lattice gauge theory with the algebraic structure $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ flows to the correct continuum QFT under the renormalization group. This assumption is supported by decades of numerical evidence and is universally used in lattice QCD, but is not rigorously proved — it is essentially the Yang-Mills mass gap problem (Clay Millennium Prize). The extension also requires the standard Wilson promotion of global to local gauge symmetry. These two items are open problems in lattice QFT, shared with all lattice formulations of the Standard Model — they are not specific to the OI framework. (The $\bar{\theta}$ IR persistence gap, previously identified as a third item, has been closed: Theorem 27 of the SM companion paper proves $\bar{\theta} = 0$ at all energy scales using the bijection structure of $\varphi^n$.)

The reconstruction theorem establishes a bidirectional correspondence at the lattice level:

$$\text{Lattice-scale physics} \quad \longleftrightarrow \quad [(S, \varphi)] / \sim$$

where $\sim$ identifies bijections that produce the same emergent description (q-equivalence, partition genericity, and choice of specific isotropic bounded-degree representative). The mathematical structure and the physics determine each other *up to gauge equivalence* — which is exactly how physical theories always work. In general relativity, the observed physics determines an equivalence class of metrics modulo diffeomorphisms. In gauge theory, the physics determines an equivalence class of connections modulo gauge transformations. Here, the physics determines an equivalence class of finite bijections modulo the OI gauge freedoms.

The distinction between "mathematics describes reality" and "mathematics is reality" therefore has no empirical content within the framework — not because the question is unimportant, but because it is provably undecidable by any measurement. The reconstruction theorem establishes that the mathematical structure $[(S, \varphi)]/\sim$ and the observed physics determine each other up to gauge. Any experiment that could distinguish "the universe is $[(S, \varphi)]$" from "the universe is described by $[(S, \varphi)]$" would have to detect structure outside the equivalence class — but the equivalence class already accounts for everything observable.

This is the same logical structure as gauge invariance. In electromagnetism, the potential $A_\mu$ is underdetermined by the physics — only $F_{\mu\nu}$ is measurable. The boundary between the physical ($F_{\mu\nu}$) and the gauge ($A_\mu$) is exact. The OI framework identifies an analogous exact boundary: the physics is the equivalence class $[(S, \varphi)]/\sim$; the ontological status of $(S, \varphi)$ — whether it "is" reality or "describes" reality — is gauge. The boundary is a theorem, not a philosophical preference.

This reframes Wigner's puzzle. Mathematics is not "unreasonably effective" at describing physics. The reconstruction theorem proves that the observed physics and the mathematical structure determine each other uniquely up to gauge. The effectiveness is a theorem, not a mystery.

The relationship extends the incompleteness family in a specific direction. Gödel showed that a formal system cannot fully prove truths about itself — the unprovable truths have rigid structure. Turing showed that a computer cannot fully predict its own behavior — the undecidable problems have rigid structure. The OI framework shows that an observer cannot fully see the system it inhabits — the partial description has rigid structure (quantum mechanics). The mathematical content of this partial description is the semisimple part of the full dynamics. What the observer *cannot* see — the nilpotent monodromy, the arithmetic data over finite fields, the Jordan block structure — is not noise or ignorance. It is the specific, mathematically determined complement of the observable world.

---

## 9. Conclusion

The lattice in the OI framework is not a physical substrate. It is the coupling graph of a bijection on a finite set — the adjacency structure that the dynamics induces on the degrees of freedom. Space is the large-scale geometry of this graph. Time is the iteration of the bijection. Quantum mechanics is the observer's compressed description of the visible sector. General relativity is the thermodynamic limit of the coupling structure.

The fundamental object is (S, $\varphi$) — a finite set and a bijection. Physically: a finite lossless memory. S is the storage capacity; $\varphi$ is the guarantee that nothing is ever erased. The partition V is the observer's read access, derived rather than postulated: any small subgraph of any large bounded-degree bijection automatically satisfies C1–C3 (§7.6). The dimension $d = 3$ is derived: the unique value consistent with propagating gravity, stable matter, gravitational concordance, and renormalizable gauge interactions (§7.6).

From (S, $\varphi$) alone: the factorization into sites is derived (§3.1), the wave equation is derived (§2.2), $d = 3$ is derived (§7.6), $q$-gauge freedom is established (§4), background independence is achieved (§7.4), the observer is derived (§7.6), QM is derived [1], and GR is derived [2] — with no free parameters except the specific bijection $\varphi$.

The remaining presupposition: the coupling graph must have bounded degree and statistical isotropy — both already required by the framework for the Myrheim-Meyer dimension estimate and Lorentz invariance. The integer dimension and the value $d = 3$ are consequences of self-consistency, not inputs. The framework's claim: for any bijection $\varphi$ satisfying these two structural properties, the emergent description is quantum mechanics on a $d = 3$ lattice with general relativity as its thermodynamic limit. The question of which specific quantum field theory the observer sees is constrained by $d = 3$ and the wave equation but is beyond the scope of this paper.

The deepest lesson (§8.6) is that the framework belongs to a family of impossibility-with-structure results — alongside Gödel's incompleteness theorem and Turing's halting problem — in which self-reference under finite resources produces not formless ignorance but rigid, mathematically determined structure. The relationship between mathematics and physics is itself illuminated: the reconstruction theorem establishes a bidirectional correspondence between the observed physics and the equivalence class $[(S, \varphi)]$, up to gauge freedoms — dissolving Wigner's puzzle by showing that the "unreasonable effectiveness" of mathematics is a theorem, not a mystery. The universe is a finite memory that never forgets. Physics is what that memory looks like from inside — and what it looks like from inside uniquely determines what it is.

---

## Acknowledgements

During the preparation of this work, the author used Claude Opus 4.6 (Anthropic) to assist in drafting and refining argumentation. The author reviewed and edited all content and takes full responsibility for the publication.

---

## References

[1] A. Maybaum, "The Incompleteness of Observation," submitted to Foundations of Physics (2026).

[2] A. Maybaum, "Dynamics Selection and Emergent General Relativity in the Observational Incompleteness Framework" (2026).

[3] R. Bousso, "The holographic principle," *Rev. Mod. Phys.* **74**, 825 (2002).

[4] L. Bombelli, J. Lee, D. Meyer, and R. Sorkin, "Space-time as a causal set," *Phys. Rev. Lett.* **59**, 521 (1987).

[5] D.P. Rideout and R.D. Sorkin, "A classical sequential growth dynamics for causal sets," Phys. Rev. D 61, 024002 (2000).

[6] S. Surya, "The causal set approach to quantum gravity," Living Rev. Relativ. 22, 5 (2019).

[7] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).

[8] S. Wolfram, "A Class of Models with the Potential to Represent Fundamental Physics," Complex Systems 29, 107 (2020).

[9] C. Rovelli, *Quantum Gravity* (Cambridge University Press, 2004).

[10] J. Ladyman and D. Ross, *Every Thing Must Go: Metaphysics Naturalized* (Oxford University Press, 2007).

[11] S. French, *The Structure of the World: Metaphysics and Representation* (Oxford University Press, 2014).

[12] J. Ambjørn, A. Görlich, J. Jurkiewicz, R. Loll, "Nonperturbative quantum gravity," Phys. Rep. 519, 127 (2012).

[13] P. Ehrenfest, "In what way does it become manifest in the fundamental laws of physics that space has three dimensions?" *Proc. Amsterdam Acad.* **20**, 200 (1917).

[14] F. R. Tangherlini, "Schwarzschild field in n dimensions and the dimensionality of space problem," *Nuovo Cim.* **27**, 636 (1963).

[15] P. van der Hoorn, W. J. Cunningham, G. Lippner, C. Trugenberger, and D. Krioukov, "Ollivier-Ricci curvature convergence in random geometric graphs," *Phys. Rev. Research* **3**, 013211 (2021).

[16] C. Kelly, C. Trugenberger, and F. Biancalana, "Convergence of combinatorial gravity," *Phys. Rev. D* **105**, 124002 (2022).

[17] C. A. Trugenberger, "Combinatorial quantum gravity: geometry from random bits," *JHEP* **2017**, 045 (2017).

[18] C. A. Trugenberger, "Emergent time, cosmological constant and boundary dimension at infinity in combinatorial quantum gravity," *JHEP* **2022**, 019 (2022).

[19] Y. Ollivier, "Ricci curvature of Markov chains on metric spaces," *J. Funct. Anal.* **256**, 810 (2009).

---

## Appendix A: The Trace-Out as a Jordan-Chevalley Projection

This appendix proves that the OI trace-out extracts the semisimple part of the evolution matrix's Jordan-Chevalley decomposition, erasing the nilpotent monodromy. The results are stated for the scalar wave equation on a ring of $L$ sites over $\mathbb{F}_q$; the multi-component extension (Theorem A.4) incorporates the gauge group.

### Setup

The wave equation $x(n, t+1) = x(n-1, t) + x(n+1, t) - x(n, t-1) \pmod{q}$ has phase space $(\mathbb{Z}/q\mathbb{Z})^{2L}$ and evolution matrix $F = \left(\begin{smallmatrix} 0 & I \\ -I & A \end{smallmatrix}\right)$ where $A$ is the circulant adjacency matrix of the ring. The eigenvalues of $A$ over $\mathbb{C}$ are $\lambda_k = 2\cos(2\pi k/L)$ for $k = 0, \ldots, L-1$.

### Theorem A.1 (Period formula)

*For $q$ prime with $\gcd(L, q) = 1$: $\mathrm{ord}(F \bmod q) = qL$ if $q$ is odd, and $L$ if $q = 2$.*

*Proof.* For each Fourier mode $k$, the $2 \times 2$ block $B_k = \left(\begin{smallmatrix} 0 & 1 \\ -1 & \lambda_k \end{smallmatrix}\right)$ has characteristic polynomial $t^2 - \lambda_k t + 1$ with roots $\zeta^k, \zeta^{-k}$ (where $\zeta = e^{2\pi i/L}$). Over $\bar{\mathbb{F}}_q$ with $\gcd(L, q) = 1$, these remain $L$-th roots of unity with multiplicative orders dividing $L$.

At the parabolic modes ($\lambda_k = \pm 2$, eigenvalues $\alpha = \pm 1$), $B_k$ has a repeated eigenvalue but is not a scalar matrix. Its Jordan form is $\left(\begin{smallmatrix} \alpha & 1 \\ 0 & \alpha \end{smallmatrix}\right)$. Under iteration:

$$B_k^n = \alpha^n \begin{pmatrix} 1 & n\alpha^{-1} \\ 0 & 1 \end{pmatrix}$$

For $\alpha = 1$: $B_k^n = I$ requires $n \equiv 0 \pmod{q}$. For $\alpha = -1$: $B_k^n = I$ requires $n$ even and $n \equiv 0 \pmod{q}$, giving order $2q$. The diagonalizable eigenvalues contribute orders dividing $L$. Therefore $\mathrm{ord}(F) = \mathrm{lcm}(L, q, 2q) = qL$.

For $q = 2$: $\left(\begin{smallmatrix} 1 & 1 \\ 0 & 1 \end{smallmatrix}\right)^2 = I$ over $\mathbb{F}_2$, so the nilpotent part is automatically killed and $\mathrm{ord}(F) = L$. $\square$

### Theorem A.2 (Jordan-Chevalley decomposition)

*Define $N = (F^L - I)/L \bmod q$. Then:*

*(i) $N$ is nilpotent with $N^2 = 0$ and $\mathrm{rank}(N) = 2$.  
(ii) $F_u = I + N$ is unipotent with $F_u^q = I$.  
(iii) $F_{\mathrm{ss}} = F \cdot (I - N)$ is semisimple with $F_{\mathrm{ss}}^L = I$.  
(iv) $F = F_{\mathrm{ss}} \cdot F_u$ and $[F_{\mathrm{ss}}, N] = 0$.*

*Proof.* $F^L$ has the form $I + LN'$ where $N'$ arises from the Jordan blocks: the block $\left(\begin{smallmatrix} 1 & 1 \\ 0 & 1 \end{smallmatrix}\right)^L = \left(\begin{smallmatrix} 1 & L \\ 0 & 1 \end{smallmatrix}\right)$ contributes a rank-1 nilpotent, and similarly for $\alpha = -1$ (since $(-1)^L = 1$ for even $L$). So $N = N'$ has $N^2 = 0$ (each block is rank-1 nilpotent on a 2D subspace) and $\mathrm{rank}(N) = 2$ (two parabolic modes). Since $N^2 = 0$: $(I + N)^{-1} = I - N$, giving $F_{\mathrm{ss}} = F(I - N)$. Then $F_{\mathrm{ss}}^L = F^L (I - N)^L = (I + LN)(I - LN + \ldots) = I \bmod q$ since terms involving $LN$ cancel modulo $q$ (using $N^2 = 0$). Commutativity follows from $N$ being supported on the parabolic eigenspaces, which are $F$-invariant. $\square$

*Verified computationally for $L = 4, 6, 8, 10, 12$ and $q = 3, 5, 7, 11, 13$.*

### Theorem A.3 (q-independence of the Weil-Deligne conductor)

*The Weil-Deligne conductor $\mathfrak{f}_{\mathrm{WD}} = \mathfrak{f}_{\mathrm{ss}}(L) + \mathrm{rank}(N) = \mathfrak{f}_{\mathrm{ss}}(L) + 2$ is q-independent when $\gcd(L, q) = 1$, where $\mathfrak{f}_{\mathrm{ss}}(L) = \sum_\alpha (\mathrm{ord}(\alpha) - 1)$ is computed from the eigenvalue orders of $F_{\mathrm{ss}}$, all dividing $L$.*

*Proof.* $F_{\mathrm{ss}}$ has order $L$ and all its eigenvalues are $L$-th roots of unity in $\bar{\mathbb{F}}_q$. For $\gcd(L, q) = 1$, the $L$-th roots of unity in $\bar{\mathbb{F}}_q$ are isomorphic (as a group) to those in $\mathbb{C}$, so their multiplicative orders are the same. $\square$

| $L$ | $\mathfrak{f}_{\mathrm{ss}}(L)$ | $\mathfrak{f}_{\mathrm{WD}}$ | $\mathrm{NM}^2 = 3L/4$ |
|-----|---|---|---|
| 4 | 14 | 16 | 3.00 |
| 6 | 30 | 32 | 4.50 |
| 8 | 70 | 72 | 6.00 |
| 10 | 106 | 108 | 7.50 |
| 12 | 130 | 132 | 9.00 |

Both $\mathfrak{f}_{\mathrm{ss}}$ and $\mathrm{NM}^2$ are q-independent encodings of the same semisimple eigenvalue data — one via multiplicative orders (integers), one via fourth moments of magnitudes (reals).

### Theorem A.4 (Additive decomposition over gauge irreps)

*For the $K$-component wave equation with coupling matrix $M = \mathrm{diag}(\mu_1 I_{n_1}, \ldots, \mu_r I_{n_r})$:*

$$\mathfrak{f}_{\mathrm{WD}}(M) = \sum_{i=1}^{r} n_i \cdot \mathfrak{f}_{\mathrm{WD}}(\mu_i)$$

*In particular, for $K = 6$ with $M = \mathrm{diag}(\mu_c I_3, \mu_w I_2, 1)$: $\mathfrak{f}_{\mathrm{WD}} = 3\mathfrak{f}_{\mathrm{WD}}(\mu_c) + 2\mathfrak{f}_{\mathrm{WD}}(\mu_w) + \mathfrak{f}_{\mathrm{WD}}(1)$, with the same multiplicities $(3, 2, 1)$ that determine $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.*

*Proof.* The multi-component evolution matrix is block-diagonal: the $a$-th component has its own $2L \times 2L$ block $F_{\mu_a}$ with eigenvalues depending only on $\mu_a$. Both $F_{\mathrm{ss}}$ and $N$ inherit the block-diagonal structure, so $\mathfrak{f}_{\mathrm{ss}}$ and $\mathrm{rank}(N)$ decompose additively. $\square$

*Verified for all $(\mu_c, \mu_w) \in \{1, \ldots, q-1\}^2$ at $q = 3, 5, 7$ with $L = 4$. Every case matches exactly.*

### The projection

The OI trace-out (marginalization over the hidden sector) produces the emergent quantum description, which depends on the coupling eigenvalues $\mu_k$ via the NM formula $\mathrm{NM}^2 = 3\langle\mu^4\rangle$ (a consequence of the stochastic-quantum correspondence applied to the wave equation's Fourier decomposition). These $\mu_k$ are properties of $F_{\mathrm{ss}}$ — the semisimple part of the dynamics. The nilpotent monodromy $N$ contributes nothing to the emergent description: it affects only the off-diagonal Jordan block entries, which are erased by the coarse-graining over the hidden sector.

The trace-out therefore performs the Jordan-Chevalley projection $(F_{\mathrm{ss}}, N) \mapsto F_{\mathrm{ss}} \mapsto \{\mu_k\} \mapsto \mathrm{NM}^2$: it extracts the semisimple part, encodes it via magnitudes rather than orders, and organizes it by the representation theory of the partition. The nilpotent monodromy — genuine mathematical structure present in the full dynamics — is invisible to the embedded observer.

This is the precise sense in which physics is the semisimple shadow of mathematics: the observer sees only the diagonalizable spectral data, projected by the trace-out and organized by the gauge group's representation structure. The nilpotent part is the mathematical complement — present in the dynamics, absent from the physics.
