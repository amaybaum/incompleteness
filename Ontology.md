# The Substrate Problem: Structural Foundations of the Observational Incompleteness Framework

### Alex Maybaum

### 2026

---

## Abstract

The Observational Incompleteness (OI) framework derives quantum mechanics and general relativity from a deterministic bijection on a finite lattice with a visible/hidden partition [1, 2]. This paper addresses a question the derivations leave open: what is the lattice? We show that the framework's results depend on six structural properties — deterministic bijectivity, finite boundary entropy, bounded coupling degree, statistical isotropy, non-trivial partition coupling, and slow-bath capacity — and on nothing else. The regular lattice, the alphabet size q, and the wave equation are all either derived from these properties or irrelevant to the predictions. We argue that the lattice is not a physical substrate but the coupling graph of the bijection: the adjacency structure defined by which degrees of freedom affect which others in one dynamical step. The product decomposition of the state space into "sites" — and hence the coupling graph itself — is determined by the bijection as the unique factorization minimizing coupling degree, confirmed numerically. Space is not a container for the dynamics; space is the large-scale geometry of the coupling graph. The alphabet size q is a gauge freedom: all structural predictions are q-independent, confirmed for q = 2 through 64. The framework's causal partial order is a causal set in the sense of Bombelli-Lee-Meyer-Sorkin, with the bijection providing the deterministic dynamics that standard causal set theory lacks. The fundamental ontological commitment is minimal: a finite set, a bijection, and a partition. Everything else — space, time, quantum mechanics, general relativity — is emergent.

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

A *specific dimensionality d*. The Myrheim-Meyer dimension extracts d from the coupling structure; it is an output, not an input. The proofs work for any d ≥ 1.

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

### 7.3 What remains unexplained

The framework, even on the structural reading, leaves two significant questions open.

*Why d = 3?* The theorems work for any spatial dimension d ≥ 1. Our universe has d = 3. Nothing in the axioms or the structural properties selects d = 3 over any other value. Numerical tests of P-indivisibility as a function of dimension show a sharp increase from d = 1 to d = 2, but no significant variation among d = 2, 3, 4 — the framework does not appear to select d = 3 on information-theoretic grounds. This is the same problem every discrete approach to quantum gravity faces, and the honest answer is that the OI framework does not solve it. Whether a deeper selection principle exists (perhaps related to the stability of the area law, the number of independent polarizations of the wave equation, or the topology of the coupling graph) is an open question.

*Can the coupling graph evolve?* The companion papers treat the coupling graph as fixed (background-dependent). In general relativity, the spacetime geometry is dynamical — the metric responds to the matter content. If space is the coupling graph, background independence would require the graph to change.

This creates a specific mathematical tension with the framework's definitions. In §3.1, the coupling graph G_φ is determined by a fixed bijection φ. If φ is fixed, G_φ cannot change. The resolution requires allowing φ to be *state-dependent*: the coupling structure at step t depends on the configuration s(t). Formally, the dynamics becomes s(t+1) = φ_{s(t)}(s(t)), where each φ_s is a bijection but the coupling graph G_{φ_s} varies with s. The dynamics remains deterministic and bijective at each step, preserving the P-indivisibility proof, but the coupling structure — and hence the emergent spatial geometry — responds to the state.

This is precisely the analog of general relativity's dynamical metric: the "background" is not fixed but evolves with the matter content. Whether such state-dependent bijections can be constructed while preserving the area law, the dispersion relation, and the other links in the derivation chain is a non-trivial open problem. It may connect to the causal dynamical triangulations program [12], where the spacetime triangulation is itself dynamical.

### 7.4 The measurement problem and (S, φ, V)

On the structural reading, the measurement problem is not solved — it is dissolved by the structure of the triple (S, φ, V).

The wave function is not a component of (S, φ, V). It is a derived object: the emergent description that the P-indivisible stochastic process admits via the Barandes correspondence [1, §3.1]. Since the wave function is derived, not fundamental, asking "does it collapse?" is asking about the behavior of a compression artifact, not about the behavior of reality.

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

The framework's results depend on six structural properties and nothing else. The regular lattice, the alphabet size, the dimensionality, and the wave equation are all either derived or irrelevant. The product decomposition of the state space into "sites" — the structure we call space — is the unique factorization minimizing coupling degree, determined by the bijection itself. The alphabet size q is a gauge freedom with no physical consequences. The causal partial order generated by the coupling graph is a causal set, with the bijection providing the deterministic dynamics that causal set theory lacks.

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

Items 1–6 come from the general theorem [1]. Items 7–8 come from the rigidity test [2]. Items 9–10 come from this paper. Each item is independently verifiable. No item was built into the axioms. The conjunction — a single framework producing all ten from four axioms with zero free parameters — is the cumulative case.

Two predictions await experimental verdict: ν_OI ≈ 2.45 × 10⁻³ (testable by DESI and Euclid within 1–2 years) and GW echoes at specific timescales (testable by LIGO/Virgo/KAGRA). Two structural questions remain open: why d = 3, and whether background independence can be achieved through state-dependent bijections.

---

## 9. Conclusion

The lattice in the OI framework is not a physical substrate. It is the coupling graph of a bijection on a finite set — the adjacency structure that the dynamics induces on the degrees of freedom. Space is the large-scale geometry of this graph. Time is the iteration of the bijection. Quantum mechanics is the observer's compressed description of the visible sector. General relativity is the thermodynamic limit of the coupling structure.

The framework's ontological commitment is minimal: a finite set S, a bijection φ, and a partition V into visible and hidden sectors. From this triple: the product decomposition of S into "sites" is derived as the factorization minimizing coupling degree (§3.1) — not assumed; the wave equation is derived from structural properties (§2.2) — not assumed; the dimensionality is emergent (§2.3) — not input; the alphabet size q is a gauge freedom with no physical consequences (§4) — not physical; and both QM and GR follow with no free parameters.

Two questions remain genuinely open: why the coupling graph has effective dimension d = 3, and whether state-dependent bijections can implement background independence while preserving the full derivation chain.

The fundamental object is (S, φ, V). Everything else is emergent.

---

## Acknowledgements

During the preparation of this work, the author used Claude Opus 4.6 (Anthropic) to assist in drafting and refining argumentation. The author reviewed and edited all content and takes full responsibility for the publication.

---

## References

[1] A. Maybaum, "The Incompleteness of Observation," submitted to Foundations of Physics (2026).

[2] A. Maybaum, "Dynamics Selection and Emergent General Relativity in the Observational Incompleteness Framework" (2026).

[3] N. Bao, S.M. Carroll, and A. Singh, "The Hilbert space of quantum gravity is locally finite-dimensional," Int. J. Mod. Phys. D 26, 1743013 (2017).

[4] L. Bombelli, J. Lee, D. Meyer, R. Sorkin, "Space-time as a causal set," Phys. Rev. Lett. 59, 521 (1987).

[5] D.P. Rideout and R.D. Sorkin, "A classical sequential growth dynamics for causal sets," Phys. Rev. D 61, 024002 (2000).

[6] S. Surya, "The causal set approach to quantum gravity," Living Rev. Relativ. 22, 5 (2019).

[7] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).

[8] S. Wolfram, "A Class of Models with the Potential to Represent Fundamental Physics," Complex Systems 29, 107 (2020).

[9] C. Rovelli, *Quantum Gravity* (Cambridge University Press, 2004).

[10] J. Ladyman and D. Ross, *Every Thing Must Go: Metaphysics Naturalized* (Oxford University Press, 2007).

[11] S. French, *The Structure of the World: Metaphysics and Representation* (Oxford University Press, 2014).

[12] J. Ambjørn, A. Görlich, J. Jurkiewicz, R. Loll, "Nonperturbative quantum gravity," Phys. Rep. 519, 127 (2012).
