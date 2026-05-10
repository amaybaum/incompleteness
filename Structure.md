# Hierarchical Structural Realism and Universality Classes of Embedded Observers

**Author:** Alex Maybaum  
**Date:** May 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations / Philosophy of Physics  
**Target venues:** Journal of High Energy Physics (JHEP), Foundations of Physics, Studies in History and Philosophy of Modern Physics

---

## Abstract

This paper articulates the structural commitments of the Incompleteness of Observation (OI) framework beyond its specific cubic-lattice substratum, and develops the framework's relationship to broader unification programs in fundamental physics. The framework's structural realism operates on a two-dimensional hierarchy: an observation axis (Level A: observation occurs; Level B: observer-admission; Level C: universality classes; Level D: OI's specific representative) and an orthogonal gauge axis (Level G1: D-gauge; Level G2: SM gauge group; Level G3: substratum gauge group $\mathcal{G}_{\rm sub}$; Level G4: universality-class equivalence). Different empirical predictions live at different intersections, with falsifiability stratified accordingly. *Part I* addresses the technical question of whether SM-reproducing string compactifications are gauge-equivalent representatives of OI's substratum equivalence class — a reading that would dissolve the landscape multiplicity problem. Through detailed analysis of finite-dimensional matrix-model formulations (BFSS, IKKT) we establish that OI's structural conditions A2 (determinism) and A5 (linearity) fail in ways that reflect structural commitments of string theory rather than artifacts of discretization. The substratum-level equivalence reading does not hold. *Part II* develops a broader structural framework — universality classes of embedded observers — within which OI and string theory can be precisely related. We articulate the algebraic formalization of "embedded observer" via the algebra-channel pair $(\mathcal{A}_V, \Phi)$, define universality classes by partial-trace observational equivalence, and establish that OI's $\mathcal{G}_{\rm sub}$ is a sub-equivalence of universality-class equivalence. *Part III* applies a four-feature audit (Born rule, channel-level unitarity, P-indivisibility, commutant gauge-invariance) to characterize OI-string universality-class membership: three features transport directly between frameworks, with holographic effective field theory providing a direct analog of OI's P-indivisibility, and AdS/CFT bulk reconstruction providing a direct analog of OI's Stinespring lift. The fourth feature transports as a pattern but not as a specific output. The paper also formalizes an *observer-admission* distinction: substrata admit embedded observers when their bijection structure satisfies C1–C3, with most substrata being observer-lacking. Under this framing, the string landscape's $10^{500}$ vacua decompose structurally — most compactifications produce observer-lacking substrata, with the SM-reproducing subset being structurally smaller. The OI-string relationship is reframed from "competing programs" to complementary roles within a universality-class structure.

---

## 1. Introduction

### 1.1 Scope and structure

The framework developed in [Main, SM, GR, Substratum] establishes that observed physics is uniquely determined modulo a substratum gauge group $\mathcal{G}_{\rm sub}$ within OI's specific structural class of finite deterministic bijection systems. This paper addresses two layers of structural commitments that lie beyond this core technical content.

The first layer (§2) articulates the *hierarchical structure* of the framework's structural realism. The framework operates on a two-dimensional hierarchy with an observation axis (foundational axiom → observer-admission → universality classes → OI's specific representative) and an orthogonal gauge axis (D-gauge → SM gauge → substratum gauge → universality-class equivalence). Different empirical predictions live at different intersections of these axes; falsifiability is stratified accordingly.

The second layer (Parts I, II, III) develops the framework's relationship to broader unification programs through two related but distinct questions:

*Question 1: Substratum-level equivalence.* Are SM-reproducing string compactifications gauge-equivalent representatives of OI's substratum equivalence class? An affirmative answer would dissolve the landscape multiplicity problem. Part I (§§3–7) develops this through technical analysis of matrix-model formulations, with negative outcome — OI's structural conditions A2 (determinism) and A5 (linearity) fail.

*Question 2: Cross-framework structural realism.* If substratum-level equivalence does not hold, is there a broader structural framework within which OI and string theory can be precisely related? Part II (§§8–13) develops this through formalization of universality classes of embedded observers — equivalence classes of substratum-with-observer systems under partial-trace observational equivalence, broader than $\mathcal{G}_{\rm sub}$.

Part III (§14) synthesizes both questions through a four-feature audit (Born rule, channel-level unitarity, P-indivisibility, commutant gauge-invariance) characterizing the OI-string universality-class relationship.

The two parts have different epistemic statuses. Part I produces a *definitive structural result* (negative — matrix-model formulations fail OI's A2 and A5). Part II is *programmatic* — it articulates the universality-class proposal precisely, formalizes it via definitions and propositions in §9, and identifies open technical questions whose resolution would establish or refute the framing. Definitive identification of specific universality classes — including the OI-string cross-class — requires substantial follow-up work along the lines flagged in §§11.2 and §13.1.

### 1.2 The string landscape as a multiplicity problem

For four decades, string theory has aspired to derive the Standard Model from compactification of higher-dimensional spacetime. The state of the art is summarized by Marchesano, Shiu, and Weigand [MSW2024]: many compactifications produce gauge groups that include $SU(3) \times SU(2) \times U(1)$ as a subgroup; some produce three generations of chiral matter; a smaller subset produces the observed hypercharge structure; a still smaller subset produces approximately the observed Yukawa pattern. No compactification has been demonstrated to reproduce the Standard Model uniquely with all parameters matching observation, and no general scheme is known to reproduce the flavor hierarchy [MSW2024, §2.3].

The conventional response to this state of affairs has been the landscape picture: string theory has approximately $10^{500}$ metastable vacua, each corresponding to a different low-energy effective theory, and our universe corresponds to whichever vacuum produces the SM with the observed parameters. The vacuum-selection problem — why our universe is in this particular vacuum — has been variously addressed by the anthropic principle, by eternal inflation populating all vacua, or by sharper conjectures (the swampland program) attempting to delineate which vacua are consistent with quantum gravity [Vafa2005, Palti2019, OoguriVafa2007].

The swampland program in particular has produced significant progress in constraining the landscape from above [Lehnert2025, MSW2024]. Conjectures such as the Weak Gravity Conjecture, the de Sitter Conjecture, the AdS Distance Conjecture, and the Cobordism Conjecture aim to identify which low-energy effective theories admit consistent UV completion in quantum gravity. These conjectures shrink the apparent multiplicity of vacua but do not, in their current form, single out a unique SM-reproducing vacuum.

### 1.3 The substratum picture

In a separate program [Main, SM, GR, Substratum], the Incompleteness of Observation (OI) framework approaches fundamental physics from a different direction. The starting point is the observation that quantum mechanics is the marginal-statistics description used by an embedded observer with finite distinguishable states; the trace-out over the hidden sector generates emergent QM from a deterministic classical substratum. The framework develops two technical results:

**Reconstruction theorem (Theorem 23, [Substratum §3]).** Given the empirical inputs E1-E4 (unitary QM, Bell violations, finite boundary entropy, spatial isotropy) together with the structural assumptions A1-A6 (finiteness, determinism, bounded coupling, center independence, linearity, background independence), the substratum is uniquely determined as a finite deterministic bijection $(S, \varphi)$ on a $d=3$ cubic lattice with $K = 6$ internal components, gauge group $SU(3) \times SU(2) \times U(1)$, three chiral generations, anomaly-free hypercharges, $\bar\theta = 0$, and $\hbar = c^3 \epsilon^2/(4G)$.

**Substratum gauge group (Theorem 24, [Substratum §4]).** The equivalence class of substrata producing the same emergent physics is parametrized by a four-generator gauge group:

(i) *State relabeling.* Permutations of hidden-sector configurations.
(ii) *Alphabet change.* The local state-space size $q$ in $\mathbb{Z}/q\mathbb{Z}$ is gauge ([SM §2.7]).
(iii) *Deep-sector enlargement/reduction.* The hidden sector beyond the boundary layer admits arbitrary cardinality.
(iv) *Graph isomorphism (up to statistical isotropy).* Coupling graphs sharing dimension, spectral dimension, and statistical isotropy are gauge-equivalent.

The framework's structural-realism stance is that the equivalence class $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ — not any particular substratum representative — is what physics determines. Twenty-two quantitative SM predictions, including Cabibbo angle $1/(\pi\sqrt{2})$ matching observation at $0.05\sigma$, Koide ratio $2/3$ matching at 0.02%, and the Bekenstein-Hawking $1/4$ coefficient confirmed at 99.999% by GW250114, follow as forced consequences of the equivalence class.

### 1.4 Question 1: the equivalence-class proposal

The two pictures describe the same observational target — SM physics — from very different directions. String theory begins from quantum gravity in $d=10$ or $d=11$ and seeks to reach the SM through compactification. OI begins from the embedded-observer ontology and reaches the SM through reconstruction. Question 1 asks whether the two descriptions are independent, complementary, or equivalent.

The core proposal investigated in Part I is:

**Proposal (equivalence-class reading).** Any string compactification that reproduces the observed Standard Model — gauge group $SU(3) \times SU(2) \times U(1)$, three chiral generations, anomaly-free hypercharges, the observed cosmological constant — is a gauge-equivalent representative of OI's equivalence class $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ under the four-generator structure of Theorem 24. Compactification moduli, Calabi-Yau topology, and flux choices play the role of hidden-sector relabeling (generator (i)) and deep-sector enlargement (generator (iii)).

This proposal has three substantive consequences if defensible:

(A) *Dissolution of the multiplicity problem.* The $\sim 10^{500}$ vacua are a redundancy of representation, not a multiplicity of physically distinct theories. Different compactifications producing the same observable physics are gauge-equivalent under $\mathcal{G}_{\rm sub}$. The swampland program's task is reframed: rather than identifying which vacuum is "ours," the task is to verify that the SM-reproducing subset of the landscape forms a single equivalence class.

(B) *Cross-attribution of predictions.* OI's quantitative SM predictions become predictions of any SM-reproducing string compactification, since all such compactifications are gauge-equivalent. Conversely, string-theoretic computations within SM-reproducing compactifications become tests of OI's structural derivations.

(C) *Computational gateway.* OI's cubic-lattice substratum admits direct lattice-Monte-Carlo and lattice-perturbation-theory computation. String compactifications are mathematically rich but computationally demanding. Gauge-equivalence under the proposal would let OI's lattice serve as a computational tool for string-theoretic questions, with results lifted to string-theory predictions through the equivalence.

**Pre-conditions for the proposal.** The proposal is suggestive but requires three pre-conditions:

*Pre-condition 1: Generator (ii) extension to continuum.* OI's generator (ii) operates on the alphabet $\mathbb{Z}/q\mathbb{Z}$, a discrete structure. String theory uses continuous degrees of freedom — string positions on Calabi-Yau, complex-structure and Kähler moduli, RR flux quanta. The technical question is whether OI's $q$-gauge invariance theorem [SM §2.7] extends to continuum theories, or whether OI's discrete alphabet is essential to the reconstruction. If discrete nature is essential, the bridge between OI and string theory passes through finite-dimensional matrix-model formulations of strings (BFSS, IKKT), not the continuum string description directly.

*Pre-condition 2: Existence of SM-reproducing compactifications.* Despite forty years of effort, no string compactification has been demonstrated to uniquely reproduce the SM with all parameters matching observation [MSW2024]. The "SM-reproducing subset" of the landscape is conjectured to exist but has not been explicitly exhibited.

*Pre-condition 3: A1-A6 compatibility under matrix-model bridge.* Even with matrix-model finite-dimensional formulations as intermediaries, OI's structural conditions A1 (finiteness), A2 (deterministic bijection), A3 (bounded coupling), A5 (linearity) may be violated by string-theoretic structure. Whether matrix models satisfy A1-A6 is not obvious and requires technical verification.

§§3-6 of Part I address these pre-conditions; §7 considers the consequences both if they hold and if they fail.

### 1.5 Question 2: why universality classes are substantively new

The negative answer to Question 1 (Part I) does not exhaust the structural relationship between OI and string theory. OI's $\mathcal{G}_{\rm sub}$ classifies observationally-equivalent substrata *within OI's structural class* — substrata satisfying A1-A6. The reconstruction theorem establishes uniqueness within this class, not across structural classes.

Question 2 asks whether observational features alone — without committing to specific structural conditions — generate equivalence classes across all candidate substratum descriptions. If substantive *universality classes* exist, they would represent a stronger structural-realism claim than OI's $\mathcal{G}_{\rm sub}$: not just "substrata are gauge-equivalent within OI's class" but "embedded-observer systems are gauge-equivalent across structural classes."

Part I's findings make this question concrete. The structural features of partial-trace observation (Born rule, channel-level unitarity, P-indivisibility, commutant gauge-invariance pattern — established in §14's four-feature audit) transport across the OI / string-theory boundary even when substratum-level structure does not. This provides a candidate universality class: the class characterized by these four features. The question is whether this class is well-defined, what its members are, and what additional features distinguish sub-classes.

Part II develops the formal framework for this question. §8 articulates three candidate formalizations of "embedded observer" (categorical, operational, algebraic), with the algebraic formalization adopted as principal. §9 develops the algebraic formalization, stating the key definitions (embedded observer, substratum-with-observer system, observational equivalence, universality class), proving propositions on the relation to OI's gauge group (Proposition 9.5) and the Stinespring uniqueness structure (Proposition 9.7), and developing the observer-admission distinction (Definition 9.9 + Proposition 9.10 + Corollary 9.11) that operates at a level prior to universality-class membership. §10 uses OI's framework as a worked example. §11 examines the OI-string universality class. §12 develops implications for structural realism. §13 identifies open questions and limits, with §§13.1.1-13.1.3 developing three technical questions (algebra-channel *-isomorphism, prediction transport, partial-trace features sufficiency) in detail.

The two questions are not independent. Question 1's negative answer motivates Question 2's broader framework: if substrata cannot be gauge-equivalent at the substratum level, the next question is what equivalence does hold. Question 2's universality-class framework then provides the language for Part III's cross-framework synthesis.

---

## 2. The framework's hierarchical structure

The framework's structural-realism stance operates on a two-dimensional hierarchy. An *observation axis* runs vertically — from the framework's foundational axiom to its specific empirical content. A *gauge axis* runs horizontally — from narrow gauge equivalences within the emergent QM to broad equivalences across structural classes. The two axes are orthogonal: depth on the observation axis is about scope (which substrata are within the framework's domain); breadth on the gauge axis is about transformations (which transformations are observable-preserving).

This section articulates the two axes, their orthogonality, and the multi-level structural realism that follows. The articulation is canonical for the framework — it locates where each technical result lives and stratifies the framework's predictions by hierarchy intersection. Subsequent sections of this paper develop content at specific levels (Part I at Level D × Level G3; Part II at Level C × Level G4; Part III at the partial-trace observational features sub-class within Level C).

### 2.1 The observation hierarchy

The observation hierarchy nests by inclusion: each deeper level is a more specific commitment.

**Level A — The observation axiom.** The framework begins with the empirical fact that *observation occurs* [Main §1]. An observer records distinguishable outcomes of interactions with a system not wholly under the observer's control. Level A commits to: there is something to observe; some part of reality is structured to record outcomes (observers are embedded in reality, not external to it); observation has structural consequences. This level is shared with mainstream observer-essentiality programs since 2022 (CLPW, Maldacena, HUZ, DEHK, Slagle-Preskill); the framework's distinguishing feature is producing the consequences from a finite deterministic substratum without extra dimensions or stochasticity.

**Level B — Observer admission.** Not every substratum admits observation. The framework identifies three structural conditions on a substratum's bijection $\varphi$ that are necessary for an embedded observer to exist [Main §3]:

(C1) **Coupling.** The interaction between the observer's degrees of freedom and the rest must be substantial.

(C2) **Slow bath.** The hidden-sector correlation time must be much longer than the observer's measurement timescale.

(C3) **High capacity.** The hidden sector must have sufficient information capacity to store interaction history.

A substratum $(S, \varphi)$ is *observer-admitting* if there exists a partition $V \subset S$ such that $(S, \varphi, V)$ satisfies C1–C3, and *observer-lacking* otherwise (formal Definition 9.9 in §9.6). Level B commits to: the space of substrata is structurally partitioned into observer-admitting and observer-lacking subsets; most substrata are observer-lacking (random permutations on finite sets typically lack the slow-mixing, sufficient-capacity, coupled-subsystem structure required); the framework's content applies only to observer-admitting substrata.

This has structural-anthropic content. Standard anthropic reasoning treats parameters as contingent and explained by selection: we observe a universe with parameters compatible with us because we couldn't observe a universe without them. The observer-admission reading sharpens this: observer-lacking substrata are not candidates for "our universe" at all — they are mathematical objects of a different kind, without observer-extraction structure. Within observer-admitting substrata, anthropic reasoning operates normally.

**Level C — Universality classes.** Within observer-admitting substrata, equivalence classes are determined by partial-trace observational features. Two substratum-with-observer systems are *observationally equivalent* if their algebra-channel pairs $(\mathcal{A}_V, \Phi)$ are *-isomorphic with channel intertwining (Definition 9.3 in §9.1). A *universality class* is an equivalence class under observational equivalence (Definition 9.4).

Universality classes have internal sub-structure (§9.5). Three levels of refinement:

- *Partial-trace features sub-class:* characterized by structural features any partial-trace operation must produce (Born rule, unitarity, non-Markovian marginal, commutant restriction pattern). Most universal level.
- *Gauge-group sub-class:* characterized by which gauge group emerges. SM-reproducing classes share $SU(3) \times SU(2) \times U(1)$.
- *Algebra-channel sub-class:* characterized by specific algebra of observables and specific channel dynamics.

Level C commits to: structural realism at this level is class-level (the universality class is real, specific representatives are gauge); the class is broader than OI's $\mathcal{G}_{\rm sub}$-equivalence (which operates within OI's specific structural class); multi-level structural realism is forced (different content at different sub-class refinements).

**Level D — OI's specific representative.** OI's framework selects a specific universality class (and a specific substratum representative within that class) by adding structural conditions A1–A6 [Substratum §3]:

(A1) Finiteness; (A2) Determinism (bijection); (A3) Bounded coupling degree; (A4) Center independence; (A5) Linearity; (A6) Background independence.

Combined with empirical inputs E1–E4 (unitary QM, Bell violations, finite boundary entropy, spatial isotropy), these uniquely determine the equivalence class $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ at the lattice level (Theorem 23 in [Substratum]).

A1–A6 are not the same as observer-admission C1–C3; they operate at a different hierarchy level. C1–C3 are conditions for *any* embedded observer to exist (Level B); A1–A6 are conditions for membership in *OI's specific* universality class (Level D). Some relations: A1 (finiteness) is related to but distinct from C3 (capacity); A2 (determinism) is a Level D commitment that selects deterministic-substratum members of a universality class — observers can in principle exist on stochastic dynamics. Other A's (A3–A6) are pure class-specific: required for OI's specific gauge-structure derivation, not necessary for observer-admission.

Level D commits to OI's specific structural realization: $d=3$ cubic lattice with $K=6$ internal components, linear wave equation, $SU(3) \times SU(2) \times U(1)$ from cubic-group commutant, specific empirical predictions (Cabibbo $1/(\pi\sqrt{2})$, Koide $2/3$, Bekenstein-Hawking $A/4$ — twenty-two structural retrodictions in [SM §7] and [GR §7]). The framework's strongest realism claim — ontic structural realism applied to $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ — operates at Level D.

The hierarchy nests: Level A ⊃ Level B ⊃ Level C ⊃ Level D. Each deeper level is a more specific commitment.

### 2.2 The gauge hierarchy

The gauge hierarchy is the breadth axis: which transformations are observable-preserving, with broader levels absorbing more degrees of freedom as gauge.

**Level G1 — D-gauge on the emergent Hamiltonian.** The diagonal-unitary equivalence on the emergent Hamiltonian: $H \to D H D^\dagger$ with $D$ diagonal-unitary in the eigenbasis of measurement outcomes [GR §3.3]. This is the residual gauge freedom after all transition-probability data has been extracted from the emergent QM. Two Hamiltonians $H$ and $DHD^\dagger$ produce identical $T_{ij}(t) = |\langle j|e^{-iHt/\hbar}|i\rangle|^2$ in the measurement basis. G1 is the smallest gauge group; it operates within a single Hamiltonian / single QM realization.

**Level G2 — SM gauge group on the emergent QFT.** The Standard Model gauge group $SU(3) \times SU(2) \times U(1)$ emerges as the commutant of the coupling matrix $M$ on the emergent QFT [SM §4.4-§4.6]. Cubic-group decomposition of the $K=6$ internal components produces multiplicities $(3, 2, 1)$; the commutant of the cubic-group action on the $K=6$ space is $SU(3) \times SU(2) \times U(1)$. Background independence (A6) promotes this global commutant symmetry to local gauge invariance. G2 includes G1 as a sub-symmetry. Level G2 operates within OI's specific universality class — the *uniqueness* of $SU(3) \times SU(2) \times U(1)$ depends on A3-A6 + E4. Other universality classes producing the SM at low energies would reach the same gauge group through different machinery (§14.4 on string-theoretic compactifications).

**Level G3 — Substratum gauge group $\mathcal{G}_{\rm sub}$.** The group of transformations on $(S, \varphi)$ preserving all observables — identical transition probabilities, identical emergent Hamiltonian (up to G1), identical $\hbar$ across all partitions of OI's structural class [Substratum §4 Theorem 24]. Four explicit families of generators: (i) hidden-sector relabeling, (ii) alphabet change ([SM §2.7] $q$-gauge), (iii) deep-sector enlargement, (iv) graph statistical-class equivalence. Stinespring uniqueness [Main §3.2] establishes that these four exhaust the freedom. G3 includes G1 and G2: the SM gauge group is the visible-sector shadow of $\mathcal{G}_{\rm sub}$ under the trace-out [Substratum §4]. G3 is an *equivalence-class symmetry*, not a Lagrangian symmetry — no Lagrangian exists at the substratum level. It plays the same structural role at the substratum level that Lagrangian gauge plays at the field-theory level.

**Level G4 — Universality-class equivalence.** The equivalence relation on substratum-with-observer systems by partial-trace observational features (Definition 9.4 in §9.1). Two systems are universality-class equivalent if their algebra-channel pairs are *-isomorphic with channel intertwining. G4 is broader than $\mathcal{G}_{\rm sub}$: substrata related by $\mathcal{G}_{\rm sub}$ are universality-class equivalent (since they produce the same algebra-channel pair), but substrata not related by $\mathcal{G}_{\rm sub}$ may still be universality-class equivalent if they produce the same algebra-channel pair through structurally different machinery. G4 operates within the observer-admitting subset (Level B) — observer-lacking substrata are outside the universality-class structure entirely.

The hierarchy nests: G1 ⊂ G2 ⊂ G3 ⊂ G4. Each broader level absorbs more degrees of freedom. The trace-out projects higher levels onto lower: trace-out of $\mathcal{G}_{\rm sub}$ produces the SM gauge group as image; restriction to Hamiltonian projects G2 onto G1.

### 2.3 Orthogonality and multi-level structural realism

The two hierarchies are orthogonal. The observation axis is about scope; the gauge axis is about transformations. Levels G1, G2, G3 sit within Level D (OI's specific universality class with its specific gauge structure); Level G4 operates at Level C (universality-class equivalence, broader than OI's specific class). The orthogonality is what makes the framework's structural-realism stance multi-level.

What is real differs at each level:

- *Level G4 × Level C:* the algebra-channel structure of partial-trace observation — Born rule, channel-level unitarity, non-Markovian marginal, commutant gauge-invariance pattern. Universal across observer-admitting substrata.
- *Level G3 × Level D:* the equivalence class $[(S, \varphi)]/\mathcal{G}_{\rm sub}$ — OI's specific substratum modulo the four-generator gauge group. Class-specific to OI.
- *Level G2 × Level D:* the emergent QFT structure — SM gauge group, matter content, gauge invariances. Forced uniquely in OI; shared with any SM-reproducing universality class.
- *Level G1 × Level D:* the emergent Hamiltonian's transition-probability content — dynamical structure modulo D-gauge.

These are not competing realisms but realism at different levels. The framework commits to all of them simultaneously, with content at each level being more class-specific (lower levels) or more class-universal (higher levels).

### 2.4 Predictions stratified by hierarchy level

The framework's empirical predictions live at specific intersections:

- *Level G4 × Level C predictions* — Born rule, channel-level unitarity, non-Markovian marginal, commutant restriction pattern. Universal across observer-admitting systems; trivially "predicted" because they are structural features of partial-trace observation. Not falsifiable within the framework.
- *Level G2 × Level D predictions* — SM gauge group, three generations, anomaly-free hypercharges. Forced uniquely in OI through cubic-group commutant; shared with any SM-reproducing universality class.
- *Level G3 × Level D predictions* — Cabibbo angle $1/(\pi\sqrt{2})$, Koide ratio $2/3$, Bekenstein-Hawking $A/4$, dark-sector phenomenology. Distinguishes OI from other universality-class members; forced by OI's specific $\mathcal{G}_{\rm sub}$-equivalence class.

The framework's most distinguishing predictions live at Level G3 × Level D — they are class-specific to OI. Level G2 × Level D predictions are shared with any SM-reproducing class. Level G4 × Level C predictions are essentially structural.

Falsification is stratified accordingly: falsifying a Level G4 × Level C prediction is impossible without contradicting QM itself; falsifying a Level G2 × Level D prediction would refute the entire SM-reproducing universality class; falsifying a Level G3 × Level D prediction would refute OI's specific representative without necessarily refuting the broader universality-class framework. JUNO confirming $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$ is a Level G3 × Level D confirmation; GW250114 confirming $A/4$ is a Level G2/G3 × Level D confirmation.

### 2.5 Where each level's content lives

The framework's papers carry content at different levels of the two-dimensional structure:

- *[Main]:* Levels A and B (observation axiom; embedded-observer characterization via C1–C3)
- *[SM]:* Level D × Levels G1–G2 (Standard Model structure on OI's specific cubic lattice)
- *[GR]:* Level D × Levels G1–G2 (gravitational thermodynamics on OI's specific cosmological-horizon structure)
- *[Substratum]:* Level D × Level G3 (reconstruction theorem; substratum gauge group $\mathcal{G}_{\rm sub}$)
- *This paper:* Levels B and C × Level G4 (universality-class formalization, observer-admission distinction, OI-string relationship at universality-class level, landscape reframing)

Different theorems and structural conditions do the load-bearing work at each level: Level A is not a theorem (structural fact); Level B is C1–C3 ([Main §3]) plus Definition 9.9 + Proposition 9.10 + Corollary 9.11 (§9.6); Level C is Definitions 9.1–9.4 + Propositions 9.5–9.7 (§9) plus the four-feature audit (§14); Level D is Theorem 23 (reconstruction) and Theorem 24 (substratum gauge group) ([Substratum §§3-4]) plus A1–A6 + E1–E4. On the gauge axis: G1 is the residual diagonal-unitary equivalence ([GR §3.3]); G2 is the cubic-group commutant theorem ([SM Theorem 7]) plus background independence; G3 is the four-generator characterization (Theorem 24) plus Stinespring uniqueness; G4 is Definition 9.4 plus the algebra-channel structure as the invariant.

The framework's empirical content (twenty-two quantitative predictions, specific cubic-lattice substratum, specific gauge group derivation) is concentrated at Level D × Level G3. The broader levels are where the framework connects to other unification programs and where universality-class structural realism applies — the content of Parts I, II, and III of this paper.

---

# Part I: Substratum-Level Equivalence (Question 1)

## 3. Per-generator analysis applied to string compactifications

OI's gauge group $\mathcal{G}_{\rm sub}$ has four explicit generators: (i) hidden-sector relabeling, (ii) alphabet change, (iii) deep-sector enlargement/reduction, (iv) graph statistical-class equivalence. Each has a natural but inexact analog in string compactifications. *Generator (i)* corresponds to relabeling internal-space coordinates (Calabi-Yau complex-structure parameters, Kähler-class moduli not affecting four-dimensional physics) — discrete in OI, continuous in strings. *Generator (ii)* corresponds to the matrix-rank parameter $N$ in matrix models, or possibly the worldsheet central charge; the detailed analysis (§4) shows no straightforward extension of $q$-gauge invariance to string-theoretic continuum structure has been established. *Generator (iii)* corresponds to the choice of compactification (which Calabi-Yau, which flux, which D-brane arrangement) — structurally productive as deep-sector content, but contingent on the underlying structure satisfying A1-A6 (which §6 establishes it does not for matrix models). *Generator (iv)* corresponds to lattice discretizations of compactified manifolds with the same effective dimension and spectral properties — straightforward where it applies, but operates within OI's structural class on graphs sharing OI's specific properties; cross-class application requires shared statistical properties that are not automatic.

The natural identifications are suggestive but the structural incompatibilities documented in §6 prevent direct equivalence-class identification. Per §14.4, the *pattern* of gauge invariance via commutant restriction transports across frameworks, but the specific output (which gauge group, which generators) is forced through framework-specific machinery in each case. This section is preparatory to §6's substratum-level analysis and §14's observational-level analysis; readers who have internalized those sections may treat §3 as supporting documentation.

---

## 4. Generator (ii) and the discrete-to-continuum bridge

This section examines the technical bridge between OI's discrete substratum (alphabet $\mathbb{Z}/q\mathbb{Z}$) and string theory's continuum structures (real-valued matrix entries in BFSS, complex moduli in compactifications, continuous fields on worldsheets). The bridge question is whether OI's $q$-gauge invariance theorem [SM §2.7] extends to continuum theories, or whether OI's discrete nature is essential to the reconstruction.

### 4.1 The $q$-gauge invariance theorem [SM §2.7]

OI's substratum has local state-space $\mathbb{Z}/q\mathbb{Z}$ for some integer $q \geq 2$. The $q$-gauge invariance theorem [SM §2.7] establishes that the alphabet size $q$ is a gauge parameter: no observable depends on the choice of $q$, provided the dynamics is linear. The proof rests on showing that the cubic-group decomposition, the wave equation's spectrum, and all derived quantities are independent of $q$ when the dynamics is linear over $\mathbb{Z}/q\mathbb{Z}$.

This theorem is the cornerstone of OI's claim that A5 (linearity) is forced rather than assumed. Non-linear dynamics over $\mathbb{Z}/q\mathbb{Z}$ generically produce $q$-dependent observable physics ($x^2 \bmod 3$ and $x^2 \bmod 5$ have different algebraic structure), violating the gauge equivalence. The theorem operates within the discrete alphabet structure; it does not address whether $q \to \infty$ limit produces continuum dynamics or what role real-valued degrees of freedom play.

### 4.2 Matrix models as candidate finite-dimensional representatives

String-theoretic matrix models — BFSS [BFSS1996], IKKT [IKKT1996] — are finite-dimensional formulations of M-theory and type IIB string theory respectively. BFSS at finite matrix rank $N$ has $9N^2$ continuous bosonic matrix entries plus fermionic counterparts; IKKT has a similar structure with one fewer dimension. These are finite-dimensional in the sense of bounded matrix rank; they are not finite-cardinality in the sense of OI's $|S| < \infty$ requirement.

Whether matrix models can be candidate representatives of OI's equivalence class through the bridge requires a discrete-to-continuum identification. Two natural candidates: (a) the matrix rank $N$ playing the role of OI's alphabet size $q$, with $N \to \infty$ corresponding to $q \to \infty$; (b) lattice discretization of matrix-model dynamics, producing a finite-cardinality system that approximates the continuum matrix-model in an appropriate limit.

Candidate (a) is structurally suggestive — both $q$ and $N$ parametrize the size of the basic representation space. The disanalogy is that OI's $q$-gauge theorem establishes $q$-independence of observables; the analogous claim for $N$ would be $N$-independence of matrix-model observables, which is *not* a feature of matrix models. Different $N$ values give different theories (BFSS at $N=2$ differs from BFSS at $N=10^9$), and the conjectured M-theory limit is specifically $N \to \infty$ at fixed coupling. The $N$-dependence of matrix-model dynamics is structural, not gauge.

Candidate (b) is technically tractable through lattice-discretized BFSS [BFSS-Lattice2015]. At fixed lattice spacing and matrix rank, the configuration space is finite-cardinality and OI's A1 holds. The remaining structural conditions A2 (deterministic bijection) and A5 (linearity) still fail per §6's analysis — lattice Monte Carlo is stochastic, and the Yang-Mills commutator-squared interaction remains nonlinear at the lattice level.

### 4.3 Possible bridges and their status

Three structural possibilities for the discrete-to-continuum bridge:

(a) *$q \to \infty$ limit gives continuous matrices.* Under this reading, OI's substratum at very large $q$ approximates a continuum theory, with continuous matrix entries arising as the limit. This is the most direct continuum extension. The challenge is that the $q$-gauge theorem requires linearity, which the continuum matrix-model violates. The bridge fails at A5.

(b) *Matrix rank $N$ as analog of $q$.* Under this reading, the matrix-model parameter $N$ plays the same gauge role as OI's $q$, with $N$-independence of observables required. This fails empirically — matrix-model dynamics is genuinely $N$-dependent — and the conjectured M-theory limit is at fixed $N \to \infty$, not at variable $N$.

(c) *Discrete-and-continuum genuinely incompatible.* Under this reading, OI's discrete structure is essential to its reconstruction theorem, and string theory's continuum structure is essential to its quantum-gravity content. The two frameworks describe physics through structurally distinct mathematical apparatus, with no natural bridge between them at the substratum level. This is the conclusion supported by §6's analysis.

The provisional conclusion is (c). The substratum-level bridge does not exist in the form the equivalence-class proposal of §1.3 required. The bridge does exist at the partial-trace observation level (per §14), but this is a different kind of bridge — it relates structural features of how observation extracts information, not the underlying substratum descriptions. The discrete-to-continuum question at the substratum level is orthogonal to the partial-trace-features question at the observational level.

This connects directly to the framing of §14.5: structural features of observation transport across frameworks (Born rule, unitarity, non-Markovian marginal); substratum-level structure does not (discrete vs continuum, bijection vs path-integral, linear vs nonlinear). The discrete-to-continuum bridge is part of the substratum-level layer that does not transport.

---

## 5. SM-reproducing compactifications: a catalogue

Three principal classes of string compactifications produce the SM gauge group through structurally different mechanisms. *Heterotic* ($E_8 \times E_8$ or $SO(32)$ on Calabi-Yau threefolds): $E_8$ broken by CY holonomy and bundle data; three generations from CY topology (Euler character / 2); hypercharge from bundle structure. Specific realizations include the Schoen Calabi-Yau (Bouchard-Donagi 2006) and heterotic line-bundle models (Anderson-Gray-Lukas-Palti 2014). *Type II / D-brane* (IIA or IIB on Calabi-Yau with D-brane configurations): gauge fields from open strings on D-brane stacks producing $U(N)$ factors; chiral matter from D-brane intersections or magnetization; SM gauge group typically as a subgroup of larger Pati-Salam or left-right-symmetric structure. *F-theory* (on elliptically-fibered Calabi-Yau fourfolds): gauge group from singularity structure of the discriminant locus; $SU(5)$ GUT models from $A_4$ singularities with hypercharge from flux configuration breaking $SU(5)$ to the SM. None of the three classes uniquely determines all SM parameters [MSW2024].

The pattern shared across the three classes — and shared with OI per §14.4 — is gauge invariance via commutant restriction on a substratum-level symmetry. The specific output (the SM gauge group precisely) is forced by framework-specific machinery in each case: CY holonomy and bundles for heterotic; D-brane configurations for Type II; singularity structure with flux for F-theory. OI's framework reaches the same target through a structurally simpler route: the cubic-group commutant on $K = 6$ internal components, with no compactification choices required. The paper's overall finding (per §6 + §14) places this catalogue in context: these compactifications are framework-specific realizations of an observational target (SM gauge group + three generations + hypercharges), not gauge-equivalent representatives of OI's substratum equivalence class. They share with OI the structural features of partial-trace observation (per §14.1-14.3 and the gauge-invariance pattern of §14.4) but realize the specific gauge content through structurally different machinery.

---

## 6. Structural compatibility: A1–A6 under matrix-model bridges

The equivalence-class reading proposed in §1.3 requires that string compactifications producing the observed Standard Model be gauge-equivalent representatives of $[(S, \varphi)]/\mathcal{G}_{\text{sub}}$. As discussed in §1.4 (Pre-condition 3), the natural bridge between OI's discrete substratum and string theory's continuum description passes through finite-dimensional matrix-model formulations — BFSS [BFSS1996] for type IIA / M-theory, IKKT [IKKT1996] for type IIB, and their close variants. This section examines whether matrix-model formulations satisfy OI's structural conditions A1–A6.

The structural conditions, as established in [Substratum §3.1] following the V1 reformulation [Substratum §3.1], are: A1 (finiteness), A2 (determinism / bijection), A3 (bounded coupling degree), A4 (center independence), A5 (linearity), A6 (background independence). All six are forced by the empirical inputs E1–E4 combined with the framework's gauge structure ([SM §2.7] $q$-gauge invariance, [Substratum §4] Theorem 24 classical-substratum descent). For matrix models to be candidate representatives of OI's equivalence class, the same conditions must hold for the matrix-model description.

We address each condition in turn, taking the BFSS matrix model as the principal example. The conclusions extend to IKKT and to BFSS variants with appropriate modifications.

### 6.1 A1 (finiteness)

**Condition.** The configuration space $S$ is finite.

**BFSS status.** The BFSS matrix model at finite $N$ has nine bosonic matrices $X^i$ (with $i \in \{1, \ldots, 9\}$) and sixteen fermionic matrices $\psi_\alpha$, each of size $N \times N$ with continuous (real-valued bosonic; Grassmann-valued fermionic) entries [BFSS1996, see also [HigherPointBFSS2025]]. The configuration space is $\mathbb{R}^{9N^2}$ for the bosonic sector at fixed $N$, augmented by a Grassmann algebra for fermions. This is not finite.

**Possible repair: lattice discretization.** Lattice-discretized BFSS [BFSS-Lattice2015] places the matrix model on a discrete time lattice, and additionally discretizes the matrix entries through standard lattice gauge theory techniques. At fixed $N$ and fixed lattice spacing, with appropriate UV cutoff on matrix-entry values, the configuration space becomes finite. The lattice discretization is the standard tool for nonperturbative numerical study of matrix models and is well-developed in the literature.

**Status.** A1 fails for continuum BFSS. A1 holds for lattice-discretized BFSS at fixed $N$ and lattice spacing, with the proviso that the continuum and large-$N$ limits — which are believed to recover string-theoretic content — produce $|S| \to \infty$ in a manner that may or may not preserve the equivalence-class structure.

### 6.2 A2 (determinism / bijection)

**Condition.** The substratum dynamics $\varphi: S \to S$ is a deterministic bijection.

**BFSS status.** BFSS dynamics is quantum, defined through the path integral over matrix configurations. At the operational level, lattice-discretized BFSS is studied through Monte Carlo simulation, which samples from the path-integral measure stochastically. Neither the continuum quantum dynamics nor the lattice Monte Carlo is a deterministic bijection on the configuration space.

The classical limit of BFSS — at $\hbar \to 0$, equivalent to taking large coupling $\lambda$ at fixed $N$ — gives Hamiltonian equations of motion on continuous phase space. These are deterministic but not bijective on a finite configuration space (since the configuration space is continuous). One could discretize phase space and time-step the equations of motion as a deterministic update, but this discretization is artificial and does not respect the underlying continuum dynamics.

**Implications for the trace-out construction.** OI's emergent-QM derivation [Main §3.2] uses the Stinespring dilation to lift visible-sector CPTP channels to unitaries on $\ell^2(S)$, with the descent restriction  selecting permutation matrices and hence bijections. If the substratum dynamics is stochastic (path-integral) rather than deterministic, the trace-out gives a CPTP channel with two sources of randomness — substratum-intrinsic (from the path-integral) and observer-ignorance (from the trace-out) — rather than the observer-ignorance-only structure that OI's framework requires. This breaks the framework's identification of substratum bijection with observable QM unitarity.

**Status.** A2 fails for matrix models in their standard quantum formulation. The failure is not a discretization artifact but a structural feature: matrix models are quantum theories, and their dynamics is quantum-mechanical (path-integral) rather than classical-deterministic. Repair would require reformulating the matrix model as a classical cellular-automaton dynamics with bijection structure, which is not the standard BFSS conjecture and would represent a substantial re-foundation rather than a discretization.

### 6.3 A3 (bounded coupling degree)

**Condition.** Each site is coupled to a bounded number of neighbors in $\varphi$'s action.

**Status.** Reframing-dependent. Treating individual matrix entries as sites, BFSS's Yang-Mills interaction $-\frac{1}{4}\text{Tr}[X^i, X^j]^2$ couples each entry to $\sim N^2$ others (unbounded in the large-$N$ limit). Treating each matrix as a single site (9 bosonic sites, 16 fermionic in BFSS), coupling is bounded. The matrix-as-site reframing is in tension with OI's combinatorial substratum (where "site" is a single configuration value); without independent argument that this reframing is correct rather than a definitional convenience, A3 should be regarded as failing on the natural reading.

### 6.4 A4 (center independence)

**Status.** Holds. BFSS has manifest invariance under matrix translations $X^i \to X^i + c^i \mathbb{1}$ (the BFSS analog of spatial translation), and matrix indices $a, b$ have no preferred values; the action is symmetric under index permutations. Both features are manifest in the BFSS action.

### 6.5 A5 (linearity)

**Condition.** The wave equation governing $\varphi$ is linear in the configuration variables.

**BFSS status.** The BFSS action contains the commutator-squared interaction $-\frac{1}{4}\text{Tr}[X^i, X^j]^2$, which is *quartic* in the matrix entries. The equations of motion derived from this action are nonlinear. This is not an accident or simplification: the nonlinear matrix interaction is what produces the gauge structure of M-theory, the emergence of D-brane dynamics, and the noncommutative-geometry interpretation of matrix theory.

OI's [SM §4.1] necessity argument for linearity rests on $q$-gauge invariance ([SM §2.7]): the alphabet size $q$ in $\mathbb{Z}/q\mathbb{Z}$ is gauge, and only linear dynamics produces $q$-independent emergent physics; nonlinear dynamics over $\mathbb{Z}/q\mathbb{Z}$ generically have $q$-dependent emergent physics ($x^2 \bmod 3$ vs $x^2 \bmod 5$ are algebraically distinct), violating the $q$-gauge invariance theorem.

In matrix models, the analog of $q$ is the matrix size $N$. Different $N$ values give algebraically distinct theories — the BFSS coupling structure depends on $N$, and the $N \to \infty$ limit (which is believed to recover the full M-theoretic content) is structurally distinct from finite $N$. Whether this $N$-dependence corresponds to OI's $q$-dependence — or whether $N$ is more analogous to OI's deep-sector cardinality (generator (iii)) — is not obvious.

If $N$ is analogous to $q$, then the $N$-dependence of matrix-model dynamics directly violates the OI requirement. If $N$ is analogous to deep-sector cardinality, then $N$-independence at fixed observable physics is required for $N$ to be gauge under generator (iii); this is the content of the BFSS conjecture (large-$N$ matrix model = M-theory) but is not rigorously established and remains a conjecture.

**Status.** A5 fails directly: BFSS has nonlinear matrix dynamics, in contrast to OI's linear wave equation. The deeper question — whether the nonlinearity is fundamental or whether some reformulation of BFSS as a linear theory in a different basis is possible — is open but does not have a known answer in the affirmative direction. The most natural reading is that matrix models genuinely have nonlinear substratum dynamics, in structural disagreement with OI's reconstruction.

### 6.6 A6 (background independence)

**Status.** Holds in spirit, conditional on the matrix-spatial bridge. BFSS has manifest $U(N)$ gauge invariance under local matrix transformations $X^i \to U X^i U^{-1}$, which is the precursor of the spacetime gauge theory in the long-distance limit. OI's A6 requires invariance under local *spatial* transformations, but BFSS has no spatial structure beyond the matrix index; the BFSS analog is matrix-internal $U(N)$ gauge invariance. Whether matrix-internal gauge invariance plays the role A6 requires depends on the matrix-spatial bridge, established only in specific limits (e.g., the diagonal-matrix limit where eigenvalues correspond to D0-brane positions).

### 6.7 Summary of A1–A6 status

The tally across A1–A6:

| Condition | BFSS status | Comment |
|---|---|---|
| A1 (finiteness) | Fails (continuum) / holds (lattice) | Repairable through lattice discretization |
| A2 (determinism / bijection) | Fails | Path-integral is stochastic, not bijection; structural mismatch |
| A3 (bounded coupling) | Fails (entry-as-site) / holds (matrix-as-site) | Reframing-dependent |
| A4 (center independence) | Holds | Manifest in BFSS |
| A5 (linearity) | Fails | Commutator-squared interaction is nonlinear; structural mismatch |
| A6 (background independence) | Holds (matrix-gauge) / conditional (spatial) | Depends on matrix-spatial bridge |

The outcome is mixed. Three of six conditions (A4, A6 in spirit, A1 with discretization) are compatible with matrix-model structure. Three of six (A2, A3 on natural reading, A5) fail in ways that are not simple discretization issues but reflect structural commitments of matrix-model dynamics that diverge from OI's substratum.

**The key failure is A5 (linearity).** OI's reconstruction theorem derives the Standard Model gauge group through cubic-group decomposition of the $K = 6$ internal components, with the wave-equation linearity playing an essential role: it is the linearity that allows the $q$-gauge invariance theorem [SM §2.7] to pin down the dynamics, and it is the wave-equation structure that produces the cubic-lattice spectrum from which the gauge group is derived. Matrix models reach the gauge group through a different route — emergent gauge fields from open strings ending on D-branes, or matrix-internal $U(N)$ symmetries enhanced in specific limits — and this route is genuinely nonlinear.

**The implication for the equivalence-class proposal.** For matrix models to be representatives of OI's equivalence class $[(S, \varphi)]/\mathcal{G}_{\text{sub}}$, they must satisfy the same A1–A6 that OI's reconstruction requires. The analysis above indicates this is not the case: at minimum A2 and A5 fail in ways that are not artifacts of the bridge but reflect genuine structural commitments. The equivalence-class reading therefore does not hold for matrix models as currently formulated.

This conclusion is structural rather than technical. Matrix models are the most direct finite-dimensional formulations of string theory, and their structural divergence from OI's substratum at A2 and A5 is informative about the relationship between the two programs. OI and string theory are not gauge-equivalent in the sense the equivalence-class proposal asks.

### 6.8 What can be salvaged

The negative conclusion in §7.7 admits four partial recoveries, ordered from most to least plausible.

**(i) Different bridge.** Matrix models are not the only finite-dimensional formulation of string theory. Alternative bridges include: (a) the AdS/CFT correspondence, where the boundary CFT lives on a finite-dimensional spacetime that may be discretized while preserving the bulk string content; (b) tensor-network reformulations of matrix models [TensorNetworkMatrix2024], which translate continuous matrix dynamics into discrete tensor structures; (c) causal dynamical triangulations [Loll2019], a discretization scheme for quantum gravity with manifestly finite configuration space and combinatorial dynamics. Each of these admits independent investigation of A1–A6 compatibility, and the equivalence-class reading might hold for one of them even if it fails for matrix models. This paper does not pursue these alternatives in detail; we flag them as open directions.

**(ii) Emergent string-theoretic features from OI substratum.** A reformulation of the relationship asks not whether string theory's substratum-level structures (matrix models) are equivalent to OI's substratum, but whether OI's substratum produces string-theoretic features at appropriate emergent scales. OI's GR §4 already derives the Bekenstein-Hawking $A/4$ entropy through a thermal-self-consistency argument that is structurally distinct from string theory's microscopic D-brane count [StromingerVafa1996], yet produces the same numerical coefficient. If OI's substratum also produces, at appropriate emergent scales, holographic duality structure analogous to AdS/CFT [Maldacena1997], graviton modes from the long-distance limit of the substratum dynamics, and dualities analogous to T-duality and S-duality, then string theory's distinctive technical achievements would be recovered as features of OI's emergent physics rather than as independent substratum-level commitments. The structural barrier identified in §6 (linearity and determinism at the substratum level vs.~Yang-Mills nonlinearity and path-integral structure) does not preclude this recovery: effective field theories with nonlinear interactions and stochastic descriptions are routinely derived from underlying linear-deterministic dynamics through coarse-graining and emergent-scale phenomena. Whether OI specifically produces the right emergent-scale features to recover string-theoretic content is an open technical question requiring direct investigation; this paper does not pursue the analysis but flags it as the most consequential research direction left open by the negative result.

**(iii) Approximate equivalence.** The equivalence-class reading might hold *approximately* — in the sense that SM-reproducing matrix-model compactifications agree with OI's predictions to within experimental precision, even if the underlying structural conditions differ. This would be an empirical equivalence rather than a structural one and would be testable by computing OI-style predictions (Cabibbo angle, Koide ratio) within specific compactifications and comparing to OI's results. We note this as an empirical research direction not pursued here.

**(iv) Reformulation of A2/A5.** OI's A2 (determinism) and A5 (linearity) might admit reformulations that accommodate matrix-model structure. For A2: a path-integral over deterministic bijection trajectories produces ensemble-stochastic behavior at the coarse-grained level; if BFSS can be reformulated as such an ensemble, A2 might hold at the trajectory level. For A5: the commutator-squared interaction is linear in the *combination* $[X^i, X^j]$, with the nonlinearity arising from the commutator structure rather than higher-order terms; if "linearity" is read at the combination level, A5 might hold. Both readings are speculative and have not been worked out in detail. The current state of OI's framework treats A2 and A5 in the standard sense (bijection at the configuration level; linear in single-variable expansion), and any reformulation must be argued explicitly.

**(v) Shared observational invariants.** A reformulation of the relationship asks not whether the substrata are equivalent (recoveries (i) and (iv)) or whether one produces the other (recovery (ii)) or whether predictions match empirically (recovery (iii)), but whether OI and string theory agree at the *observable* level because both must respect shared invariants of observation. Under this reading, the substrata of OI and string theory are genuinely different and not gauge-equivalent under any natural transformation — consistent with the structural divergence established in §6 — but the observations they produce are forced into agreement by structural features of the observation process itself. The intersection between the two frameworks lives at the observable level, not at the substratum level. OI's gauge group $\mathcal{G}_{\rm sub}$ classifies observationally-equivalent substrata within OI's structural class; the proposal here is that a larger equivalence relation operates across structural classes, with observational agreement enforced by invariants that both OI's substratum and string theory's compactifications must respect. The constructive content of this recovery would be the identification of these observational invariants — features of the observation process that are independent of substratum description and that force any substratum producing the observed Standard Model to agree at the observable level. This is a stronger structural-realism claim than OI's reconstruction theorem alone establishes: the reconstruction theorem identifies invariants within OI's class; the present recovery would identify invariants across all classes producing the SM. The technical content of this recovery is open. We flag it as a research direction that reframes the OI-string relationship from "two substratum descriptions of physics" to "two realizations of observational invariants that physics requires."

### 6.9 Summary

Matrix-model formulations of string theory do not satisfy OI's structural conditions A1–A6 in their standard formulation. The failures at A2 (determinism / bijection) and A5 (linearity) are deep — they reflect structural commitments of string theory that diverge from OI's substratum, not artifacts of the discretization bridge. The equivalence-class proposal of §1.3 therefore does not hold for matrix models as currently understood.

This negative result is the central technical finding of this paper. Section 6 develops its implications: that OI and string theory are independent programs with the same observational target, and that the conventional approach to combining them — string theory as a UV completion of the SM, with OI as a foundational reformulation — is structurally distinct from the equivalence-class reading that this paper investigated.

---

## 7. Implications and discussion

The structural analysis of §6 establishes that matrix-model formulations of string theory do not satisfy OI's structural conditions A1–A6 in their standard formulation, with the failures at A2 (determinism / bijection) and A5 (linearity) reflecting structural commitments rather than discretization artifacts. The equivalence-class proposal of §1.3 — that SM-reproducing string compactifications are gauge-equivalent representatives of OI's $[(S, \varphi)]/\mathcal{G}_{\text{sub}}$ — therefore does not hold for matrix models as currently understood. This section discusses the implications of this negative result, the partial recoveries identified in §7.8, and the open directions left by the analysis.

### 7.1 OI and string theory as independent programs

The most direct implication of §6's analysis is that OI and string theory are independent research programs targeting the same observational target — the Standard Model and its quantum-gravity completion — through structurally distinct substratum descriptions. They are not the same theory in different gauge representations, and they are not different stages of a single derivation in which OI provides the foundational layer and string theory the technical implementation.

This independence has methodological consequences. A successful prediction of OI (e.g., the Cabibbo angle $1/(\pi\sqrt{2})$, the Koide ratio $2/3$) is not automatically a prediction of string theory; conversely, the swampland program's identification of consistent UV completions of the SM does not automatically constrain OI's substratum. Each program is responsible for its own empirical match, with no cross-attribution beyond what shared empirical inputs (E1–E4 in OI's notation) provide.

The independence is also informative about the foundational landscape of fundamental physics. OI and string theory are two of several active programs (alongside loop quantum gravity, causal sets, asymptotic safety, and others) that propose substratum descriptions for the SM. The structural divergence between OI and string theory at A2 and A5 indicates that these are deep ontological choices, not technical details: a substratum framework either commits to deterministic-bijection / linear-wave-equation structure (OI's choice, with the foundational economy this implies) or to path-integral / gauge-Yang-Mills structure (string theory's choice, with the gravitational-unification this provides). The choice cannot be made on technical grounds alone; it requires foundational arguments.

A consequence of the structural divergence is that both programs cannot be foundational descriptions of the same physics simultaneously. If both are taken as candidate substratum descriptions of the Standard Model, then at most one of the two is correct as currently formulated; the other requires modification. Three resolutions are possible: (a) OI is correct as described and string theory needs modification toward classical-substratum dynamics; (b) string theory is correct as described and OI's reconstruction theorem captures features of a specific compactification rather than foundational structure; (c) both require modification toward a deeper framework from which both emerge as different limits or different aspects. The current empirical and theoretical evidence does not select definitively among these resolutions. The independence claim is therefore not a stable end-state but a provisional characterization of the current state of evidence; the productive direction for future work is to identify which resolution obtains, through continued empirical testing of each framework's predictions, peer-review validation of internal consistency, and investigation of whether the partial recoveries identified in §7.8 can rescue equivalence-class structure.

### 7.2 The string landscape multiplicity problem is not dissolved by OI's gauge group

The first of the three substantive consequences flagged in §1.3 — dissolution of the string landscape multiplicity problem through OI's $\mathcal{G}_{\text{sub}}$ — was contingent on the equivalence-class reading. Since §6 establishes that the reading does not hold for matrix models, the dissolution does not follow.

The landscape multiplicity problem therefore remains an open question for string theory, to be addressed through string-theoretic methods (swampland conjectures, vacuum-selection mechanisms, anthropic considerations). OI's gauge group $\mathcal{G}_{\text{sub}}$ does not, on the analysis of §6, provide a structural reduction of the landscape; it classifies equivalence among substrata satisfying OI's A1–A6, which the matrix-model formulations of string theory do not.

This is a substantive limitation on OI's reach. A reading of OI as "physics modulo gauge, where the gauge group classifies all UV-completion choices" was natural but turns out to be too strong. The accurate reading is that OI's gauge group classifies equivalence within OI's structural class — the class of finite deterministic bijection systems with bounded coupling and linear wave equations on graphs of statistical isotropy. Substratum descriptions outside this class (matrix models, continuum string theory, perhaps loop quantum gravity, perhaps causal sets) are not classified by $\mathcal{G}_{\text{sub}}$ and may belong to different equivalence classes (or no equivalence class, if they fail to reproduce the SM).

### 7.3 Cross-attribution of predictions does not follow

The second consequence flagged in §1.3 — that OI's predictions become string-theory predictions through gauge equivalence — likewise does not follow. OI's prediction set (twenty-two quantitative SM relations matching observation at sub-percent precision) is a feature of OI's specific substratum derivation chain, which uses linearity of the wave equation, $q$-gauge invariance, and cubic-group decomposition. None of these is present in matrix models in the form OI requires, so the prediction chain does not transport.

This means the empirical match of OI's predictions is OI-specific evidence, neither confirmed nor refuted by string-theoretic considerations. If OI's predictions hold up under further experimental scrutiny (DESI Year 5 for the cosmological prediction; JUNO for $\sin^2\theta_{12}$; lattice tests for additional Layer-2(a) predictions), this is evidence for OI's substratum description specifically. If they fail, it's evidence against OI specifically. String theory is not implicated either way through the gauge-equivalence route examined here.

### 7.4 Computational gateway via OI's lattice does not extend to string theory

The third consequence — OI's computationally-tractable lattice as a tool for string-theoretic computations — also does not follow. Without gauge equivalence, OI's lattice computations produce predictions of OI's substratum, not of string compactifications. They cannot substitute for direct string-theoretic computation (Calabi-Yau geometry, brane dynamics, flux integration) within a specific compactification.

This limitation does not, however, diminish OI's own computational tractability. OI's predictions remain computable from the cubic-lattice substratum without needing to engage string-theoretic structures. The framework's empirical successes are independent of string-theoretic computation, and that independence is preserved by the negative result.

### 7.5 Connection to swampland conjectures

The swampland program [Vafa2005, OoguriVafa2007, Palti2019, Lehnert2025] aims to identify which low-energy effective field theories admit consistent UV completion in quantum gravity, by formulating conjectures (Weak Gravity, de Sitter, AdS Distance, Cobordism, etc.) that consistent EFTs must satisfy. The program's success would be a constructive characterization of the SM-reproducing subset of the landscape.

OI's reconstruction theorem provides an alternative characterization of the same SM-reproducing target, but through different methodology: OI derives the SM from the embedded-observer ontology, whereas the swampland program identifies which UV completions are compatible with consistent quantum gravity. The two characterizations are independent in the sense established by §6, but they may agree on which low-energy effective theories are admissible.

A productive direction for future work is to ask whether OI's SM derivation is consistent with the swampland conjectures. If OI's emergent QFT (after the trace-out and large-$N_S$ continuum limit) satisfies the Weak Gravity Conjecture, the de Sitter Conjecture, and the other established swampland constraints, this provides cross-validation: the same SM-reproducing target is independently consistent with both quantum-gravity-consistent string theory and the embedded-observer reconstruction. We do not pursue this analysis here but flag it as an open direction.

### 7.6 Partial recoveries and what would be required to revisit the equivalence-class reading

§6.8 identified five partial recoveries, ordered roughly from most to least consequential. *Emergent string-theoretic features from OI's substratum* (recovery (ii)) is the most consequential if it holds: OI's GR §4 already produces the Bekenstein-Hawking $A/4$ entropy through thermal self-consistency [StromingerVafa1996 has the microscopic derivation]; whether OI similarly produces holographic-duality structure analogous to AdS/CFT, graviton modes from long-distance dynamics, and T/S-dualities at appropriate emergent scales is an open technical question. The structural barrier identified in §6 does not preclude this recovery: emergent-scale physics can have nonlinear and stochastic features arising from underlying linear-deterministic dynamics through coarse-graining. *Shared observational invariants* (recovery (v)) is structurally distinct: it asks whether OI and string theory agree at the observable level because both respect invariants of the observation process, identifying invariants across structural classes rather than within OI's class. *Alternative bridges* (AdS/CFT with discrete boundary, tensor networks, causal dynamical triangulations) is tractable but would constitute substantial follow-up work. *Approximate-equivalence via empirical agreement* is testable: computing OI's predictions (Cabibbo, Koide) within a specific SM-reproducing compactification and comparing. *A2/A5 reformulation* is the most speculative — it would require substantial reworking of either OI's conditions or string-theoretic structure.

The two most consequential — emergent features and shared invariants — are not in competition. They address structurally distinct questions: the first treats OI as a candidate foundational description from which string-theoretic content emerges; the second treats observation itself as the locus where different substratum descriptions are forced into agreement. Both extend OI's structural-realism stance — that what is real is invariant structure, not specific representatives — to the comparison with other unification programs.

### 7.7 What this paper has established

This paper articulates the equivalence-class proposal precisely (§1.4), resolves it in the negative for matrix models (§6 establishes A2 and A5 fail in ways reflecting structural commitments rather than discretization artifacts), and identifies five partial recoveries as research directions (§6.8 + §7.6). The negative result is informative: OI and string theory are not gauge-equivalent at the substratum level, not in a foundational-versus-effective hierarchy at any obvious level, and not in a derivable relationship as currently formulated. Their relationship must be sought either at the level of emergent-scale physics (recovery (ii)) or at the level of observational invariants both frameworks must respect (recovery (v)). The §14 four-feature audit develops the second direction: three of four observational features transport directly between frameworks, characterizing the partial-trace observational level as where the intersection lives.

### 7.8 Observer admission and the structure of the landscape

Part II §9.6 formalizes a structural distinction between *observer-admitting* substrata — those that admit a partition satisfying C1–C3 — and *observer-lacking* substrata, where no such partition exists. The distinction operates at the level of the substratum's bijection structure, prior to any observer being instantiated. This section examines how the distinction reframes the relationship between OI and the string landscape.

**The landscape, viewed through observer admission.** The string landscape comprises approximately $10^{500}$ distinct compactifications. The standard reading [Vafa2005, Susskind2003] treats the landscape as a multiplicity of candidates for "the universe," with anthropic selection narrowing the candidate set to those compatible with our observations. Under the observer-admission reading, the landscape's multiplicity decomposes structurally:

- *Observer-lacking compactifications.* Compactifications producing four-dimensional vacua without chiral matter, with rapid hidden-sector mixing, with insufficient horizon capacity, or with broken cosmological structure cannot satisfy C1–C3. They correspond to observer-lacking substrata. These compactifications are mathematical objects in string theory's space of vacua, but they are not candidate physical universes in OI's framework — observers cannot be embedded in them.

- *Observer-admitting compactifications.* Compactifications producing four-dimensional vacua with chiral matter, stable cosmological structure (de Sitter or near-de Sitter with horizon timescales $\tau_B \sim H^{-1}$), and sufficient information capacity (the cosmological horizon's $\sim 10^{122}$ degrees of freedom) satisfy C1–C3 and are observer-admitting. The SM-reproducing compactifications surveyed in §5 — heterotic on Calabi-Yau with appropriate bundles, Type II / D-brane Pati-Salam constructions, F-theory $SU(5)$ with hypercharge flux — fall in this class.

The observer-admission criterion distinguishes the two classes structurally. Most compactifications in the landscape are likely observer-lacking; the SM-reproducing subset is a small fraction. The numerical multiplicity of the landscape ($10^{500}$) is largely a measure of observer-lacking substrata, not of competing candidates for our universe.

**The translation of C1–C3 to string-theoretic structure.** The structural conditions for observer admission [Main §3] are formulated for finite deterministic substrata. Translating them to string-theoretic compactifications requires identifying analogs in string-theoretic structure:

- *C1 (coupling)* requires substantial coupling between visible-sector and hidden-sector dynamics. In string-theoretic terms: the four-dimensional EFT must have non-trivial interaction between observable matter (chiral fermions, gauge fields, Higgs sector) and the gravitational / Kaluza-Klein / hidden gauge sectors. Compactifications with completely decoupled hidden sectors fail C1.

- *C2 (slow bath)* requires the hidden-sector correlation time to be much longer than the observer's measurement timescale. In string-theoretic terms: the cosmological structure must have a stable phase with horizon timescales $\tau_B \sim H^{-1}$ much longer than laboratory timescales $\tau_S$. AdS compactifications without de Sitter structure, or compactifications with rapidly mixing cosmological structure, fail C2.

- *C3 (high capacity)* requires the hidden sector to have sufficient information capacity to store the interaction history. In string-theoretic terms: the cosmological horizon's information capacity (set by the holographic bound at $\sim 10^{122}$ for our observed universe) must be sufficient. Compactifications with horizons of insufficient capacity fail C3.

These translations are intuitively clear: a compactification reproducing our universe's cosmological structure satisfies all three. A compactification producing AdS, anti-de Sitter, or rapidly-mixing dS-with-very-short-horizon-time fails one or more. The translation is plausible structurally, though a rigorous version would require detailed analysis specific to compactification classes.

**The OI-string relationship reframed.** Under the observer-admission reading, the relationship between OI and string theory is structurally distinct from the standard "two competing programs" framing. OI operates entirely within observer-admitting substrata — the framework's foundational axiom "observation occurs" is taken to be structurally specific to observer-admitting cases (per §9.6). String theory's landscape encompasses both observer-admitting and observer-lacking substrata, with the observer-admitting subset being where SM-reproducing physics resides.

The relationship therefore takes this form:

- OI's universality class lives in the observer-admitting subset.
- Some SM-reproducing string compactifications also live in the observer-admitting subset.
- The intersection between OI's universality class and the observer-admitting compactification subset is what the partial-trace-features analysis of §14 characterizes.
- Compactifications outside the observer-admitting subset are not candidates for "our universe" in OI's framework — they are observer-lacking substrata, mathematical objects but not physical universes.

This reframing has substantive consequences for the landscape problem. The standard landscape problem treats $10^{500}$ vacua as competitors; selecting "the right one" appears to require either anthropic reasoning or unprincipled choice. The observer-admission reading dissolves this: most of the landscape is observer-lacking and not in competition for "our universe." The candidate space is the observer-admitting subset, which is much smaller. Within the candidate space, our universe is in some specific universality class, distinguished from other observer-admitting universality classes by specific predictions.

**Connection to anthropic reasoning.** The standard anthropic argument explains the landscape's empirical match to our universe through selection: we observe a universe compatible with observers because we couldn't observe a universe incompatible with observers. The observer-admission reading sharpens this. Anthropic selection separates into two distinct kinds of work:

- *Structural exclusion of observer-lacking substrata.* Substrata that lack the structural features for observer-admission are not in the candidate space at all. There is no anthropic selection within them — they are not competitors. This is structural exclusion, not selection.

- *Within-candidate-space selection of universality class.* Among observer-admitting substrata, our universe is in some specific universality class. Standard anthropic reasoning applies here: we are in the universality class that produces our observations, and the framework's predictions distinguish OI's class from other observer-admitting classes within the candidate space.

The combination dissolves the "fine-tuning" worry to a substantial degree. Fine-tuning intuitively arises from the question "why is our universe one specific compactification out of $10^{500}$?" The observer-admission reading reframes: most of the $10^{500}$ are not candidate compactifications for "our universe" at all (they are observer-lacking); within the candidate space, our universe is in a specific universality class characterized by specific structural features (per §14's four-feature audit and the universality-class structure of Part II).

**Implications for the relationship.** The "two competing programs" framing of OI vs. string theory is not the right characterization under the observer-admission reading. The structurally accurate framing is:

- *String theory* provides a broad framework encompassing both observer-admitting and observer-lacking substrata, with the SM-reproducing subset (observer-admitting) being where physical universes reside.
- *OI* operates within the observer-admitting subset, providing structural conditions (A1–A6) that pick out a specific universality class.
- *The intersection* between OI's universality class and the SM-reproducing observer-admitting compactifications is what §14's partial-trace-features analysis establishes.
- *Outside the intersection,* OI and string theory diverge on universality-class membership, with each framework potentially identifying its own universality class within the observer-admitting subset.

This reframing makes the OI-string relationship structurally clean: not competition, but complementary roles in characterizing the structure of the candidate space for physical universes. The framework's content remains: OI's specific predictions distinguish OI's universality class from other observer-admitting universality classes; the predictions are tests of which class our universe is in.

**Open structural questions.** The observer-admission framing of the landscape is a structural reading, not a rigorous result. Several questions remain open:

- *Rigorous translation of C1–C3 to string-theoretic structure.* The translations above are plausible but not formal. Working out a rigorous version for specific compactification classes (heterotic, Type II, F-theory) would require detailed analysis specific to each class.

- *Numerical estimate of the observer-admitting subset.* The standard $10^{500}$ figure is for the full landscape including observer-lacking compactifications. Estimating the observer-admitting subset's size — even to within several orders of magnitude — would substantially clarify the landscape problem's empirical content.

- *Observer-admitting compactifications outside OI's universality class.* If observer-admitting compactifications exist that are not in OI's universality class, they would be alternative candidates for "the universe" — distinct from OI in their predictions, with their own internal structure. Identifying such compactifications would be a substantial result.

- *Connection to swampland criteria.* The swampland program identifies criteria for compactifications consistent with quantum gravity (Weak Gravity Conjecture, de Sitter Conjecture, Distance Conjecture). The observer-admission criterion is structurally distinct but may overlap with swampland criteria — both restrict the candidate compactification space, possibly with different overlap regions. Working out the relationship would clarify both frameworks.

These questions are not addressed in this paper; they are flagged as research directions opened by the observer-admission reframing. The reframing itself — reading the landscape's multiplicity as containing predominantly observer-lacking substrata, with the observer-admitting subset being structurally smaller — is a substantive contribution that the framework's structural-realism stance makes available to the landscape discussion.

---
---

# Part II: Universality Classes of Embedded Observers (Question 2)

## 8. Formalizing embedded observation

The notion of "embedded observer" in OI's framework is informal: an observer with finite distinguishable states, embedded in a substratum, with non-trivial coupling to a hidden sector that has slow dynamics relative to observation, and high information capacity in the hidden sector. For the universality-class question to admit precise formulation, we need a formalization sufficient to define equivalence relations on substratum-with-observer systems. Three candidate formalizations are available.

### 8.1 Categorical formalization

The categorical approach treats embedded observers as functors $F: \mathbf{Sub} \to \mathbf{Obs}$ from a category of substratum descriptions to a category of observable descriptions, with the universality-class equivalence given by natural equivalence of functors (substrata producing isomorphic observable descriptions, possibly through different observation functors). The formalization is well-defined but requires substantial machinery (explicit construction of $\mathbf{Sub}$ and $\mathbf{Obs}$ with their respective morphism structures) that has not been worked out in the OI literature. We do not pursue it further here.

### 8.2 Operational formalization

The operational approach treats embedded observers as operational protocols $(\mathcal{P}, \mathcal{M}, p)$ — preparations, measurements, and outcome probabilities — without committing to a specific underlying substratum, in the spirit of Mackey's quantum logic [Mackey1963] and the generalized probabilistic theories program [Hardy2001, Barrett2007]. The universality class is the equivalence class under operational indistinguishability. This formalization is closest to empiricist intuition and methodologically clear, but it is empiricist — it does not commit to substratum-level realism — and may sit uneasily with OI's structural-realism stance, which treats the equivalence class itself as ontologically real.

### 8.3 Algebraic formalization

The algebraic approach treats embedded observers as CPTP channels with specific structural features. An embedded observer is characterized by:
- An algebra $\mathcal{A}_V$ of visible-sector observables (typically a von Neumann algebra acting on a Hilbert space $\mathcal{H}_V$)
- A CPTP channel $\Phi: \mathcal{B}(\mathcal{H}_V) \to \mathcal{B}(\mathcal{H}_V)$ representing the dynamics of visible-sector states under the substratum's evolution traced over the hidden sector
- A Stinespring dilation $\mathcal{H}_V \otimes \mathcal{H}_H$ with a unitary $U$ on the dilation lifting $\Phi$ to a unitary dynamics

The substratum is captured by the dilation; the observer is captured by the visible-sector algebra and the CPTP channel. Equivalence between embedded observers is equivalence of the channel and algebra structure, with the dilation being gauge.

The universality-class proposal in algebraic terms: two substrata are in the same class if they produce equivalent $(\mathcal{A}_V, \Phi)$ pairs, where equivalence is *-isomorphism of the algebras and conjugacy of the channels (channels related by an algebra isomorphism).

**Status.** This formalization is intermediate in heaviness between categorical and operational. It uses standard machinery from operator-algebra and CPTP-channel theory, both well-developed. It captures OI's framework directly: OI's reconstruction theorem produces an algebra-channel pair from the substratum, and $\mathcal{G}_{\rm sub}$ is characterized by transformations preserving this pair. Extending to string theory's emergence requires identifying the corresponding algebra-channel pair from string-theoretic dynamics, which is non-trivial but tractable for matrix-model formulations and AdS/CFT.

### 8.4 Choosing a formalization

The three formalizations are related but not equivalent. The operational formalization is weakest — it characterizes observers by their data without committing to underlying structure. The algebraic formalization adds structure (algebra of observables, channel dynamics) that operational data alone does not specify. The categorical formalization is heaviest — it requires explicit category-theoretic machinery that the others do not.

For the purposes of this paper, we adopt the **algebraic formalization** as the principal framework. It is well-developed in the operator-algebra and quantum-information literatures; it captures OI's framework and string-theoretic emergence directly; and it provides sufficient structure to define universality classes precisely without requiring the heavy categorical machinery.

We will return to operational and categorical perspectives where they illuminate features the algebraic formalization does not capture, but the principal definitions and arguments use the algebra-channel structure of §8.3.

---

## 9. Universality classes of embedded observers

### 9.1 Formal definitions

We adopt the algebraic formalization of §8.4. The following definitions make precise the universality-class structure used throughout the rest of the paper.

**Definition 9.1** (Embedded observer). *An embedded observer is a triple $(\mathcal{H}_V, \mathcal{A}_V, \Phi)$ where:*
- *$\mathcal{H}_V$ is a separable Hilbert space (the visible-sector state space);*
- *$\mathcal{A}_V \subseteq \mathcal{B}(\mathcal{H}_V)$ is a von Neumann algebra (the algebra of visible-sector observables);*
- *$\Phi: \mathcal{B}(\mathcal{H}_V) \to \mathcal{B}(\mathcal{H}_V)$ is a CPTP channel (the visible-sector dynamics generator).*

**Definition 9.2** (Substratum-with-observer system). *A substratum-with-observer system is a quintuple $(\mathcal{H}_V, \mathcal{A}_V, \Phi, \mathcal{H}_H, U)$ where $(\mathcal{H}_V, \mathcal{A}_V, \Phi)$ is an embedded observer, $\mathcal{H}_H$ is a separable Hilbert space (the hidden-sector state space), and $U$ is a unitary on $\mathcal{H}_V \otimes \mathcal{H}_H$ such that*
$$\Phi(\rho) = \mathrm{Tr}_H[U(\rho \otimes \rho_H) U^\dagger]$$
*for some hidden-sector reference state $\rho_H$. The pair $(\mathcal{H}_H, U)$ is a Stinespring dilation of $\Phi$.*

**Definition 9.3** (Observational equivalence). *Two embedded observers $(\mathcal{H}_V^{(1)}, \mathcal{A}_V^{(1)}, \Phi^{(1)})$ and $(\mathcal{H}_V^{(2)}, \mathcal{A}_V^{(2)}, \Phi^{(2)})$ are observationally equivalent, written $(\mathcal{H}_V^{(1)}, \mathcal{A}_V^{(1)}, \Phi^{(1)}) \sim_{\mathrm{obs}} (\mathcal{H}_V^{(2)}, \mathcal{A}_V^{(2)}, \Phi^{(2)})$, if there exists a *-isomorphism $\theta: \mathcal{A}_V^{(1)} \to \mathcal{A}_V^{(2)}$ such that*
$$\theta \circ \Phi^{(1)}|_{\mathcal{A}_V^{(1)}} = \Phi^{(2)}|_{\mathcal{A}_V^{(2)}} \circ \theta.$$

**Definition 9.4** (Universality class). *A universality class is an equivalence class of embedded observers under $\sim_{\mathrm{obs}}$. Two substratum-with-observer systems are in the same universality class if their embedded observers (the first three components of the quintuple) are observationally equivalent — irrespective of the specific Stinespring dilations producing them.*

The definitions are deliberately framework-neutral. They invoke standard machinery from operator-algebra theory (von Neumann algebras, CPTP channels, *-isomorphisms) without requiring framework-specific structural commitments. This is essential for the universality-class framework's purpose: characterizing equivalence at the level of observation, independent of the specific substratum machinery producing observable physics.

### 9.2 Relation to OI's gauge group: a proposition

OI's substratum gauge group $\mathcal{G}_{\rm sub}$ is a special case of observational equivalence. We can state this precisely.

**Proposition 9.5** (OI gauge group as observational sub-equivalence). *Let $(S_1, \varphi_1)$ and $(S_2, \varphi_2)$ be OI-class substrata (satisfying A1-A6) related by a transformation $g \in \mathcal{G}_{\mathrm{sub}}$. Let $(\mathcal{H}_V^{(i)}, \mathcal{A}_V^{(i)}, \Phi^{(i)})$ be the embedded observer derived from $(S_i, \varphi_i)$ via the Main paper's trace-out construction. Then $(\mathcal{H}_V^{(1)}, \mathcal{A}_V^{(1)}, \Phi^{(1)}) \sim_{\mathrm{obs}} (\mathcal{H}_V^{(2)}, \mathcal{A}_V^{(2)}, \Phi^{(2)})$.*

*Proof sketch.* By construction, $\mathcal{G}_{\rm sub}$ is the set of substratum-level transformations preserving observational data (transition probabilities $T_{ij}(t)$, emergent Hamiltonian up to D-gauge, and $\hbar$). The trace-out construction maps observational-data-preserving substratum transformations to *-isomorphisms on the visible-sector algebra commuting with the channel. Hence $g \in \mathcal{G}_{\rm sub}$ induces $\theta_g$ satisfying Definition 9.3. $\square$

The converse — that all observationally-equivalent OI-class substrata are related by some $g \in \mathcal{G}_{\rm sub}$ — is the completeness statement of [Substratum] Theorem 24, established for OI-class substrata via the Stinespring uniqueness + classical-substratum descent argument [Substratum §4].

**Corollary 9.6** (Universality classes are coarser). *Let $\mathcal{C}$ be the universality class containing an OI-class substratum $(S, \varphi)$. Then $\mathcal{C}$ contains every $\mathcal{G}_{\rm sub}$-related OI-class substratum, and possibly substrata not in OI's structural class that produce observationally-equivalent embedded observers.*

The corollary makes precise the "universality classes are coarser than $\mathcal{G}_{\rm sub}$" claim: the universality class extends OI's gauge equivalence by potentially including non-OI-class substrata whose embedded-observer triples are observationally equivalent through different dilation mechanisms.

### 9.3 Many-to-one structure of dilations

A structural feature important for the universality-class framework is the *many-to-one* relationship between substratum-with-observer systems and their embedded observers. Many distinct substratum-with-observer quintuples produce the same embedded-observer triple; the additional data is the Stinespring dilation $(\mathcal{H}_H, U)$.

**Proposition 9.7** (Stinespring uniqueness, restricted form). *Let $(\mathcal{H}_V, \mathcal{A}_V, \Phi)$ be an embedded observer with two Stinespring dilations $(\mathcal{H}_H^{(1)}, U^{(1)})$ and $(\mathcal{H}_H^{(2)}, U^{(2)})$ producing the same channel $\Phi$. If both dilations have minimal hidden-sector dimension (i.e., neither has redundant deep-sector content), then there exists a unitary $W: \mathcal{H}_H^{(1)} \to \mathcal{H}_H^{(2)}$ such that $U^{(2)} = (\mathbb{1}_V \otimes W) U^{(1)} (\mathbb{1}_V \otimes W^\dagger)$.*

*Proof sketch.* Standard application of Stinespring's uniqueness theorem [Stinespring1955] for minimal dilations. Non-minimal dilations admit additional partial-isometry freedom corresponding to deep-sector enlargement, which is OI's generator (iii). $\square$

The proposition establishes that the universality-class framework's many-to-one structure has a precise form: at the level of minimal dilations, the substratum-with-observer system is unique up to hidden-sector unitary; additional dilation freedom corresponds to deep-sector enlargement. This is the algebraic counterpart of OI's $\mathcal{G}_{\rm sub}$ generators (i) (hidden-sector relabeling, corresponds to $W$) and (iii) (deep-sector enlargement, corresponds to non-minimality).

**Corollary 9.8** (Substratum description as gauge). *The substratum description $(\mathcal{H}_H, U)$ is gauge under hidden-sector unitary equivalence and deep-sector enlargement; the universality-class data is the embedded-observer triple $(\mathcal{H}_V, \mathcal{A}_V, \Phi)$.*

This sharpens the structural-realism claim. What is invariant under the universality-class framework's gauge structure is the embedded-observer triple; the substratum is gauge data. OI's framework treats the equivalence class modulo $\mathcal{G}_{\rm sub}$ as ontologically real; the universality-class framework treats the embedded-observer triple as ontologically real.

### 9.4 Relation to OI's gauge group, refined

With the formal definitions in place, the relationship between universality classes and OI's gauge group can be stated more precisely than in §9.2.

OI's $\mathcal{G}_{\rm sub}$ classifies substratum-with-observer systems within OI's structural class (substrata satisfying A1-A6, with the trace-out construction of [Main]) producing the same embedded observer. Universality classes (Definition 9.4) classify substratum-with-observer systems across all structural classes producing the same embedded observer. The inclusion is strict if there exist non-OI-class substrata producing observationally-equivalent embedded observers; this is the open question of §9.8 below.

The framework's structural-realism stance refines correspondingly. OI's claim is that the equivalence class modulo $\mathcal{G}_{\rm sub}$ is real; the universality-class claim is that the embedded-observer triple $(\mathcal{H}_V, \mathcal{A}_V, \Phi)$ is real, with the substratum description (any specific dilation $(\mathcal{H}_H, U)$ producing the triple) being gauge. The two claims agree within OI's structural class but differ on the question of cross-class membership.

### 9.5 Structure of universality classes

Universality classes have internal structure beyond bare equivalence. Three structural features:

**Sub-classes by structural features.** Two embedded observers in the same universality class produce the same algebra-channel pair, hence the same observational features (Born rule, unitarity, non-Markovian marginal, commutant gauge-invariance pattern). They may differ on which structural features the substratum producing them respects — OI's substratum satisfies A1-A6, string-theoretic substrata may not. Sub-classes within a universality class can be characterized by the structural conditions the substratum representatives satisfy.

**Sub-classes by gauge content.** Two observers in the same universality class produce the same gauge-invariance pattern (commutant restriction) but may differ on the specific gauge group. OI's substratum produces $SU(3) \times SU(2) \times U(1)$ uniquely; string-theoretic substrata may produce the same group through compactification choices, but the same universality class might also include substrata producing different gauge groups (other compactifications, non-OI structural-class substrata) provided they share the algebra-channel structure.

**Refinement by substratum-symmetry.** Per §14.4, the *pattern* of gauge-invariance via commutant transports across frameworks while the *specific* gauge group does not. The universality class containing OI's substratum and the SM-reproducing string compactifications may also contain substrata producing different gauge groups; the SM-reproducing class is a sub-class characterized by the observable target (specifically $SU(3) \times SU(2) \times U(1)$).

These structural features mean universality classes are not flat — they have hierarchical sub-structure. The OI-string relationship in particular involves multiple levels: a coarse universality class characterized by partial-trace observational features; a finer sub-class characterized by SM-reproducing observable target; a still finer sub-class characterized by specific predictive content (Cabibbo, Koide, etc.).

### 9.6 Observer-admitting and observer-lacking substrata

The framework's universality classes are populated by *observer-admitting* substrata — pairs $(S, \varphi)$ that admit a partition $V \subset S$ satisfying the framework's structural conditions C1–C3 (coupling, slow-bath memory, high capacity) [Main §3]. This restriction defines the scope of the framework's discourse and is structurally distinct from the absence of an observer in any specific substratum. We make the distinction explicit here because it bears on the relationship between OI and other unification programs in §12.

**Definition 9.9** (Observer-admitting substratum). *A substratum $(S, \varphi)$ is observer-admitting if there exists a partition $V$ such that the triple $(S, \varphi, V)$ satisfies C1–C3. A substratum is observer-lacking if no such partition exists.*

Three structural conditions on $\varphi$ characterize observer-admission:

- *Coupled dynamics:* $\varphi$ does not decompose as $\varphi_V \times \varphi_H$ for any candidate partition. Substrata where visible and hidden sector dynamics factorize cannot satisfy C1.
- *Non-equilibrium phase:* $\varphi$ admits phases where local mixing time is much shorter than overall recurrence time. Substrata in perpetual equilibrium cannot satisfy C2 [Main §4.6].
- *Sufficient hidden capacity:* potential hidden sectors have $|\mathcal{C}_H|$ large enough to store interaction history without overflow. Substrata with insufficient hidden-sector capacity cannot satisfy C3.

These are structural features of the substratum's bijection $\varphi$ itself, prior to any observer being instantiated. An observer-admitting substratum has the structural capacity for partial-trace observation; an observer-lacking substratum does not.

**Proposition 9.10** (Observer-admitting and observer-lacking substrata are structurally distinct). *Observer-admission is determined by structural features of $\varphi$, not by whether an observer is "present" or "absent" in any specific substratum. The classes are mutually exclusive partitions of the space of substrata.*

The proposition is a clarification rather than a deep result: it states that the observer-admission criterion operates at the level of the bijection structure, separating substrata into two structurally-distinct classes. An observer-admitting substratum has the structural features that allow observation to occur; an observer-lacking substratum does not. The classes are not "the same substratum with observation added or removed" — they are different substrata characterized by different structural features of $\varphi$.

**Corollary 9.11** (Universality classes are populated by observer-admitting substrata only). *The universality classes of Definition 9.4 are equivalence classes within the observer-admitting subset. Observer-lacking substrata are outside the framework's universality-class structure.*

This corollary clarifies the framework's scope. Universality classes characterize substratum-with-observer systems by their algebra-channel structure under partial-trace observation; observer-lacking substrata do not produce algebra-channel pairs through partial trace and are therefore not in the universality-class structure. They are mathematical objects (finite sets with bijections) with dynamics, but not with extractable observational features.

**The "physics" of observer-lacking substrata.** Observer-lacking substrata have $\varphi$-dynamics — they evolve, they have cycle structure, they have all the formal features of permutations on finite sets. But they do not produce *physics* in the framework's sense: no quantum mechanics, no observable record, no measurement outcomes. The framework's foundational claim — that physics is the structural features of partial-trace observation — implies that physics is a feature of observer-admitting substrata, not of all substrata. This is consistent with the main paper's "observation occurs" axiom: the axiom is taken to be a structural feature of our universe (which is observer-admitting) rather than a contingent fact about whether someone happens to be looking.

**Anthropic implication.** The observer-admission distinction has structural-anthropic content. Most arbitrary $(S, \varphi)$ pairs do not admit observers — random permutations on finite sets typically lack the coupled-dynamics, non-equilibrium-phase, and high-capacity features required for C1–C3. Observer-admitting substrata are a structurally-characterized subset. Our universe is in this subset, structurally; we are observers in an observer-admitting substratum. This is structural anthropic selection rather than contingent anthropic selection: the criterion for "physical universe" is observer-admission, with observer-lacking substrata being abstract mathematical objects rather than candidate physical universes.

The structural-anthropic reading is consistent with but more precise than the standard anthropic position. Standard anthropics says we observe a universe with parameters compatible with observers because we couldn't observe a universe without those parameters. The observer-admission reading says: substrata with observers and substrata without observers are structurally distinct kinds of objects; observer-admitting substrata are the candidate space for "physical universe"; we are in one of them.

### 9.7 Worked examples

We illustrate the universality-class definition with three examples.

**Example 1: OI's class.** OI's substratum is a finite deterministic bijection on a $d=3$ cubic lattice with $K=6$ internal components. The dilation is the Stinespring lift of the visible-sector CPTP channel; the visible-sector algebra is the emergent QFT operator algebra. The universality class containing OI's substratum is the class of substrata producing the same algebra-channel pair — by OI's reconstruction theorem, this includes all $\mathcal{G}_{\rm sub}$-related substrata (relabelings, alphabet changes, deep-sector enlargements, graph statistical-class equivalents). Whether the class extends beyond $\mathcal{G}_{\rm sub}$ depends on whether non-OI-class substrata produce the same algebra-channel pair. All members of this class are observer-admitting per §9.6.

**Example 2: String-theoretic class.** A string-theoretic substratum (e.g., type IIA on a specific Calabi-Yau threefold with specific fluxes) produces a low-energy effective field theory. The dilation is the full string-theoretic structure (worldsheet plus target space, or matrix-model structure plus large-$N$ limit); the visible-sector algebra is the four-dimensional effective field theory operator algebra. The universality class is the class of substrata producing the same algebra-channel pair through string-theoretic emergence. Observer-admission is a non-trivial constraint: not all string compactifications are observer-admitting, as developed in §7.8.

**Example 3: Cross-class candidate.** A class candidate is the union: substrata that produce the SM gauge group + three generations + SM-like Yukawa structure through any mechanism (OI's cubic-lattice derivation, string-theoretic compactification, possibly LQG-style structures, causal-set structures, or asymptotic-safety–derived structures with appropriate matter-emergence). This class is characterized by the observable target (the SM at low energies) rather than by the substratum mechanism. All members are observer-admitting (the SM-reproducing constraint forces observer-admission, since reproducing the SM requires producing the observed cosmological structure within which we are observers). Part I (§§3-7) establishes that, at the level of partial-trace observational features, OI and string theory are members of this candidate cross-class; §13.1.4 extends the per-condition analysis to LQG, causal sets, and asymptotic safety, finding that all three fail OI's A1–A6 (so are outside OI's specific class) but may share the partial-trace observational features class with OI and string theory. The question is whether the cross-class is well-defined and what additional features characterize it.

### 9.8 Open: does the OI-string cross-class exist?

The candidate cross-class of Example 3 is well-defined as a set: substrata producing the SM at low energies. The question is whether it is a *universality class* in the sense defined — whether all members produce equivalent algebra-channel pairs.

Part III §14 establishes partial transport: Born rule, channel-level unitarity, P-indivisibility transport directly; commutant gauge-invariance pattern transports but not the specific gauge group. Specific Yukawa couplings, CP-violating phases, and other detailed predictions have not been demonstrated to transport.

If only the structural features at §14.1-14.3 transport, the OI-string cross-class is universal at the level of these features but not at the level of detailed predictions. The class might be subdivided further: the partial-trace-features class is broader; the SM-reproducing class is narrower; the OI-Cabibbo-and-Koide-predictions class is narrower still.

Establishing definitively whether OI's specific predictions (Cabibbo, Koide, etc.) transport to the string-theoretic class would require either (a) finding a string-theoretic compactification reproducing OI's predictions, (b) showing that any SM-reproducing compactification automatically produces these predictions, or (c) showing that no string-theoretic compactification can reproduce these predictions exactly. Each of (a)-(c) is a substantial research question.

The provisional conclusion: the OI-string cross-class is well-defined at the level of partial-trace observational features (per §14) and includes specific gauge-group-and-content sub-classes, but the full structure of the cross-class — including whether OI's specific predictions are universal to the SM-reproducing sub-class or specific to OI's representative — is open.

---

## 10. OI's framework as a worked example

This section uses OI's framework to illustrate how universality classes interact with substratum-level structure. The aim is to show that universality classes are not abstract mathematical curiosities but capture the structural content of OI's reconstruction theorem in a more general form.

### 10.1 OI's reconstruction theorem in universality-class language

OI's reconstruction theorem (Theorem 23 of [Substratum]) states that the empirical inputs E1-E4 combined with the structural conditions A1-A6 uniquely determine the substratum modulo $\mathcal{G}_{\rm sub}$. In universality-class language, the theorem is a uniqueness result for one specific universality class — the OI class characterized by partial-trace observational features (Born rule, unitarity, non-Markovian marginal, cubic-group commutant gauge-invariance) plus the structural conditions A1-A6.

The reformulation in [Substratum §3.1] establishes that A1-A6 are forced by the empirical inputs combined with the framework's gauge structure. The reconstruction theorem's content is that the OI universality class is uniquely populated (modulo $\mathcal{G}_{\rm sub}$) by substrata satisfying both the partial-trace features and the structural conditions.

### 10.2 What OI does and does not establish at the universality-class level

OI's reconstruction theorem establishes uniqueness *within* the OI universality class — the class characterized by A1-A6 plus the partial-trace features. It does not establish anything about *other* universality classes. Part I (§§3-7) is explicit on this: the equivalence-class extension to string-theoretic substrata fails because string-theoretic substrata are in different universality classes (substrata violating A2 and A5 are not in OI's class).

The universality-class framework therefore provides a precise statement of OI's reach: OI's reconstruction theorem operates within a specific universality class, and the framework's predictions (Cabibbo, Koide, etc.) are features of OI's class. Whether other universality classes exist that produce the same observable physics is an open question; if they do, OI's predictions are class-specific rather than substratum-level-universal.

### 10.3 The structural-realism implication

OI's structural-realism claim (per [Substratum §1.1]) is that what's real is the equivalence class modulo $\mathcal{G}_{\rm sub}$. The universality-class framework refines this: what's class-specific is the equivalence-class-modulo-$\mathcal{G}_{\rm sub}$ structure within OI's class; what's universality-class-level is the partial-trace observational features.

The strongest structural-realism claim consistent with both OI's framework and the universality-class framing is: what's real at the universality-class level is the algebra-channel structure of the visible-sector observation; what's class-specific is the substratum representative producing this structure. This is a hierarchical structural realism: features at multiple levels are real, with finer features being more class-specific and coarser features being more universal.

This is consistent with OI's framework but more nuanced. OI's specific predictions (Cabibbo, Koide) are real features of OI's universality class; they are not universal across all classes producing the SM. A different universality class containing the SM at low energies might have different specific predictions or might lack predictive content at the corresponding level.

### 10.4 Constructing OI's algebra-channel pair

The universality-class formalism of §8.3 / §9.1 requires an explicit algebra-channel pair to be constructive. We now exhibit the triple $(\mathcal{H}_V^{\rm OI}, \mathcal{A}_V^{\rm OI}, \Phi^{\rm OI})$ at the EFT scale, completing Step 1 of the four-step recipe of §13.1.1 and providing the concrete object that the comparison work of §11.2 acts on.

**The Hilbert space.** OI's substratum is a $d = 3$ cubic lattice with $K = 2d = 6$ internal degrees of freedom per site ([SM §3.2 Theorem 6]). Under the trace-out construction of [Main §3.4], the visible sector is the sublattice accessible to the embedded observer; the hidden sector is the complementary substratum. The visible-sector Hilbert space at the substratum scale is $\ell^2(\mathcal{C}_V)$ where $\mathcal{C}_V$ is the visible sublattice's configuration space. At wavelengths long compared to the lattice spacing $\epsilon = 2 l_p$, $\ell^2(\mathcal{C}_V)$ resolves to the Fock space $\mathcal{H}_V^{\rm OI}$ of the emergent QFT — the Standard Model with gauge group $SU(3) \times SU(2) \times U(1)$, three chiral generations, and one Higgs doublet ([SM §4]).

**The algebra.** Let $\mathcal{A}_V^{\rm OI}$ be the von Neumann algebra of gauge-invariant local observables on $\mathcal{H}_V^{\rm OI}$:
$$\mathcal{A}_V^{\rm OI} = \langle \mathcal{O}(x) : \mathcal{O} \text{ a gauge-invariant local SM operator}\rangle''$$
where $\langle \cdot \rangle''$ denotes the bicommutant (von Neumann algebra closure). Generators include:

- *Gauge-field invariants.* The Yang-Mills curvature combinations $\mathrm{tr}\, F_{\mu\nu}^a F^{a,\mu\nu}$ for each factor of $SU(3) \times SU(2) \times U(1)$, plus topological terms $\mathrm{tr}\, F \tilde F$.
- *Fermion bilinears.* $\bar\psi_i \psi_j$, $\bar\psi_i \gamma^\mu \psi_j$, $\bar\psi_i \gamma^\mu \gamma^5 \psi_j$ for the SM fermion content (six quarks, six leptons, three generations), with appropriate gauge-index contractions.
- *Higgs invariants.* $\phi^\dagger \phi$, $|D_\mu \phi|^2$, $(\phi^\dagger \phi)^2$, and the Yukawa contractions $\bar\psi_L \phi \psi_R$ structurally fixed by the cubic-group representation theory of [SM §7].
- *Cubic-lattice-forced higher-dimensional operators.* Wilson coefficients of dimension-5 and dimension-6 operators are not free parameters in OI but are determined by the cubic-lattice substratum geometry; the specific structural relations $\lambda = 1/(\pi\sqrt 2)$ (Cabibbo, [SM §7.1]), $A = \sqrt{2/3}$ (Wolfenstein, [SM §7.1]), and the Koide $2/3$ relation are encoded as algebraic identities among Yukawa-sector generators.

The gauge-invariance restriction is a commutant condition: $\mathcal{A}_V^{\rm OI}$ is the subalgebra of the full local algebra that commutes with the action of $SU(3) \times SU(2) \times U(1)$ on $\mathcal{H}_V^{\rm OI}$.

**The channel.** The CPTP channel encoding visible-sector dynamics is generated by the substratum bijection $\varphi$ traced over the hidden sector. By Stinespring dilation (Definition 9.2):
$$\Phi^{\rm OI}(\rho) = \mathrm{Tr}_H\big[U_\varphi \, (\rho \otimes \rho_H^{\rm OI}) \, U_\varphi^\dagger\big]$$
where $U_\varphi$ is the unitary lift of the bijection $\varphi$ on the dilation $\mathcal{H}_V^{\rm OI} \otimes \mathcal{H}_H^{\rm OI}$ ([Substratum §3.1]), and $\rho_H^{\rm OI}$ is the uniform reference state on the hidden sector (the OI-canonical choice from the unique-invariant-measure lemma of [Main §1.2]). At the EFT scale, $\Phi^{\rm OI}$ encodes:

- *SM RG flow* from the cubic-lattice scale ($1/\alpha_0 = 23.25$ structurally, [SM §6.1]) down to the electroweak scale ($1/\alpha_1 = 59.00$, $1/\alpha_2 = 29.57$, $1/\alpha_3 = 8.47$ at $M_Z$, [SM §6.3]).
- *Non-perturbative structural features.* $\bar\theta = 0$ to all energy scales as a structural constraint ([SM §5]); instanton-sum closure consistent with $T$-invariance and detailed balance.
- *Anomaly structure.* Anomaly cancellation forced by the hypercharge structure derived from cubic-group representation theory ([SM §4.6]).
- *Higher-dimensional operator coefficients* forced by cubic-lattice geometry, including the Yukawa structural relations producing the CKM and PMNS matrices and the fermion mass ratios ([SM §7]).

**The pair as universality-class invariant.** The algebra-channel pair $(\mathcal{A}_V^{\rm OI}, \Phi^{\rm OI})$ is invariant under $\mathcal{G}_{\rm sub}$: by Proposition 9.5, any $g \in \mathcal{G}_{\rm sub}$ induces a *-isomorphism on the algebra commuting with the channel up to conjugacy. The pair is therefore a universality-class invariant of OI's structural class, encoding precisely the observational content the framework licenses.

**What the pair captures, and what it does not.** The pair captures the gauge structure (the $SU(3) \times SU(2) \times U(1)$ commutant), the renormalizable couplings (gauge couplings at $M_Z$, Yukawa structure producing CKM/PMNS), and the higher-dimensional operator structure forced by the cubic lattice. It does *not* capture the substratum bijection's specific values (those are gauged away by $\mathcal{G}_{\rm sub}$), the substratum-level dynamics directly (only its trace-out image), or trans-Planckian corrections where the EFT description breaks down.

The construction uses standard machinery from algebraic quantum field theory: nets of local von Neumann algebras with isotony and microcausality [BrunettiFredenhagen2024], with type-III factor structure [Yngvason2005] inherited from the relativistic-QFT setting; the channel via Stinespring dilation [Stinespring1955]. The framework's contribution is not new operator-algebraic machinery but the identification of the channel's specific structure as the trace-out of a deterministic substratum bijection, with the resulting algebra-channel pair as the universality-class invariant of OI's structural class. See §15.2 for further discussion of the algebra-channel formalism in independent literature.

### 10.5 Status as Step 1 of §13.1.1's recipe

The construction of §10.4 completes Step 1 of the four-step *-isomorphism recipe of §13.1.1. The remaining three steps remain open and are deferred to follow-up work:

- *Step 2.* Construct a specific string compactification's pair $(\mathcal{H}_V^{\rm string}, \mathcal{A}_V^{\rm string}, \Phi^{\rm string})$ at the same EFT scale. Natural candidates are MSSM-like F-theory or heterotic compactifications producing the exact observed gauge group and chiral content. The algebra is determined by the compactification's particle content and gauge group; the channel encodes perturbative dynamics plus non-perturbative effects (instanton contributions, threshold corrections from heavy compactification modes, RG running from the GUT/string scale to $M_Z$).
- *Step 3.* Test *-isomorphism $\mathcal{A}_V^{\rm OI} \cong \mathcal{A}_V^{\rm string}$. The renormalizable-sector check is plausibly affirmative (both reproduce SM gauge structure and chiral content); the higher-dimensional-operator check is where divergence is expected, since OI's Wilson coefficients are forced by cubic-lattice geometry while string-compactification Wilson coefficients are determined by the compactification's specific topology and flux choices.
- *Step 4.* Test channel conjugacy $\theta \circ \Phi^{\rm OI} = \Phi^{\rm string} \circ \theta$ for the *-isomorphism $\theta$ (if Step 3 succeeds). Even if the algebras are *-isomorphic, the channels may differ on specific RG flow, anomaly content, or instanton effects, placing the two systems in the same algebra class but different channel class.

Steps 2-4 require detailed comparison with a chosen compactification and are at the boundary of in-chat tractability — likely Layer 2(b) in the framework's offline-tractability classification (substantial setup, multi-session). The construction here makes the comparison concrete by exhibiting OI's side and reduces the open work in §11.2 from "algebra-channel comparison" to "execute Steps 2-4 against a specified compactification."

---

## 11. The OI-string universality class

Part III §14 establishes that OI and string theory share structural features at the partial-trace observation level. This section examines what that establishes about cross-class membership and what additional work is needed.

### 11.1 What §14's findings establish

The §14 four-feature audit shows that the Born rule, channel-level unitarity, and P-indivisibility transport directly between OI and string-theoretic emergence mechanisms. The commutant gauge-invariance *pattern* transports but the specific gauge group does not.

In universality-class language: OI's class and the string-theoretic class share the partial-trace observational features. This is necessary for the two classes to be in the same broader universality class, but not sufficient — they would also need to share the algebra-channel structure of the visible-sector observation, including the specific algebra of observables and the specific channel dynamics.

The §14.4 finding is that the specific gauge group transports across frameworks under the observable-target constraint (both produce $SU(3) \times SU(2) \times U(1)$ when reproducing the SM), but through different substratum-symmetry mechanisms. This is consistent with same-universality-class membership at the level of the SM gauge group, but the specific dynamics on the SM gauge group (Yukawa couplings, CP-violating phases, scale of supersymmetry breaking if any) may differ.

### 11.2 What additional work is needed

§10.4 completes the explicit construction of OI's algebra-channel pair $(\mathcal{H}_V^{\rm OI}, \mathcal{A}_V^{\rm OI}, \Phi^{\rm OI})$ at the EFT scale — Step 1 of the four-step recipe of §13.1.1. To establish definitively whether OI and string theory are in the same universality class, the remaining three steps must be addressed:

**Question 1: Do OI's specific predictions transport?** OI predicts the Cabibbo angle as $1/(\pi\sqrt{2})$ from cubic-group representation theory. Does any SM-reproducing string compactification reproduce this exact value through its compactification mechanism, or are string-theoretic predictions for the Cabibbo angle compactification-specific (and presumably not exactly $1/(\pi\sqrt{2})$ in general)? If the latter, OI's predictions are not universality-class-level features but OI-specific representative features.

**Question 2: Do the algebras agree?** OI's emergent QFT has a specific algebra of observables determined by its cubic-lattice structure (constructed in §10.4). String-theoretic compactifications produce algebras determined by the compactification specifics. Are these algebras *-isomorphic for SM-reproducing constructions, or merely structurally similar (sharing partial-trace features but differing on specific algebraic content)?

**Question 3: Do the channels agree?** Beyond the algebra structure, the channel $\Phi$ encodes the dynamics on visible-sector states. Does OI's $\Phi^{\rm OI}$ (as constructed in §10.4) agree with the string-theoretic $\Phi^{\rm string}$ on identical SM gauge group plus identical particle content, or does it differ on detailed dynamical features (e.g., the specific RG flow, specific anomaly content, specific instanton effects)?

These are substantial technical questions corresponding to Steps 2-4 of the §13.1.1 recipe (construct the comparison pair, check *-isomorphism, check channel conjugacy). Each would require detailed comparison of OI's framework predictions, now made concrete in §10.4, with specific string-theoretic compactifications producing the same observable target. Part III §14.5 establishes the structural-features-of-trace-out level; the universality-class question requires going further to algebra-channel-level comparison against a specified compactification.

### 11.3 Provisional characterization

Pending the technical work of §11.2, the OI-string relationship at the universality-class level is provisionally:

- **Same partial-trace-features class:** Confirmed by §14.1-14.3. Both frameworks produce Born rule, channel-level unitarity, and non-Markovian marginal observation.
- **Same gauge-group-target class:** Confirmed by both frameworks producing $SU(3) \times SU(2) \times U(1)$ at low energies, though through different substratum-symmetry mechanisms.
- **Same algebra-channel class:** Open. Requires technical work to establish.
- **Same specific-predictions class:** Open. OI's Cabibbo, Koide, and related predictions may or may not transport to string-theoretic compactifications.

The provisional characterization is that OI and string theory are likely in the same partial-trace-features and gauge-group-target classes but possibly in different algebra-channel and specific-predictions classes. Definitive characterization requires the algebra-channel comparison work flagged in §11.2. The conceptual move — taking invariants across substratum descriptions as the proper target of structural-realism commitment — has independent corroboration in the recent philosophy-of-physics literature on common-core realism for QM-string-theory dualities [DawidFranzmann2025]; see §15.3 for the connection.

---

## 12. Implications

### 12.1 Refined structural realism

The universality-class framework refines OI's structural-realism stance. OI's claim is that what's real is the equivalence class modulo $\mathcal{G}_{\rm sub}$; the universality-class refinement is that there is structure at multiple levels: partial-trace observational features (most universal, shared across structural classes), specific gauge group (intermediate, depends on substratum-symmetry but realizable by multiple substrata), specific predictions (most class-specific, features of the specific universality-class representative).

What is "real" at each level differs. At the most universal level, the structural features of partial-trace observation are real — Born rule, unitarity, non-Markovian marginal are features of any embedded-observer system, not specific to OI or string theory. At the gauge-group level, $SU(3) \times SU(2) \times U(1)$ is real — features any SM-reproducing universality class produces. At the specific-predictions level, OI's Cabibbo angle $1/(\pi\sqrt{2})$ is real *for OI's universality class* but not necessarily for other classes.

This is a hierarchical structural realism: realism at multiple levels, with class-specificity decreasing as level becomes more universal. It is consistent with OI's structural-realism stance while extending it to characterize what is shared with other unification programs and what is class-specific.

### 12.2 Methodology of fundamental physics

The universality-class framework suggests a methodological reframing of fundamental physics. Rather than asking "what is the substratum?" — which assumes a unique answer that committing to a specific framework presupposes — we can ask "what universality class are we in?" — which allows for multiple substratum-level descriptions consistent with the same universality class.

This is methodologically more agnostic about substratum specifics but more committed about substratum-class membership. It treats fundamental physics as a research program of identifying the universality class of our universe through observational features, with substratum descriptions being framework-specific tools for representing the class rather than competing claims about ultimate reality.

The methodological move connects to operationalist and empiricist positions in foundations of physics, but with structural-realism preserved at the universality-class level: what's real is the universality class, not just the operational data, and not the specific substratum representative.

### 12.3 Connection to OI's main paper

OI's main paper takes "observation occurs" as the foundational axiom. The universality-class framework formalizes this axiom's content: observation occurs, and the structure of observation produces universality classes characterized by partial-trace observational features. The features that any embedded-observer system must respect (Born rule, unitarity, non-Markovian marginal, commutant gauge-invariance pattern) are forced by the structure of observation, not by any specific substratum.

This is consistent with OI's main paper's foundational stance but extends it. Where the main paper derives QM from "observation occurs" plus structural conditions, the universality-class framework derives partial-trace observational features from "observation occurs" alone. The structural conditions A1-A6 are then class-specific refinements that yield OI's specific predictions; without them, observation still produces the universal features, but specific predictions remain framework-dependent.

This places OI's main paper in a broader context. The "observation occurs" axiom has implications beyond OI's framework — it implies the partial-trace observational features in any framework respecting the axiom. OI's specific predictions are features of OI's specific universality-class representative, with the universal features being shared with any other framework respecting the observation axiom.

---

## 13. Open questions and limits

### 13.1 Technical questions

The main technical open questions:

**Q1.** Are the algebra-channel structures of OI and string theory *-isomorphic at the SM-reproducing target? (§11.2 Question 2.)

**Q2.** Do OI's specific predictions (Cabibbo, Koide, etc.) hold across all substrata in the same SM-reproducing universality class, or are they OI-specific features? (§11.2 Question 1.)

**Q3.** What is the precise definition of the "partial-trace observational features" class? Are the four features identified in §14 necessary and sufficient to characterize this class, or are there additional features?

**Q4.** Are there universality classes other than OI's and string theory's that produce the SM at low energies? (LQG-derived classes, causal-set-derived classes, asymptotic-safety classes, etc.) If so, what features characterize them?

### 13.1.1 Q1 developed: what *-isomorphism would entail

To establish whether OI's and a specific string-theoretic compactification's algebra-channel pairs are *-isomorphic at the SM-reproducing target, four steps would be required: (1) construct OI's algebra-channel pair at the EFT scale (gauge-fields + fermion-bilinears + Higgs-operators algebra restricted to commutant of $SU(3) \times SU(2) \times U(1)$, with channel from the substratum's bijection traced over the hidden sector); (2) construct the compactification's pair at the same scale (algebra from particle content + gauge group; channel from perturbative + non-perturbative effective dynamics including instantons, threshold corrections, RG running); (3) check *-isomorphism (whether algebraic relations agree on gauge-coupling structure, Yukawa-coupling structure, anomaly content, topological terms — both renormalizable and higher-dimensional operators); (4) check channel conjugacy ($\theta \circ \Phi^{(1)} = \Phi^{(2)} \circ \theta$ for the *-isomorphism $\theta$). **Status:** Step 1 is executed in §10.4 (construction of $(\mathcal{A}_V^{\rm OI}, \Phi^{\rm OI})$); Steps 2-4 remain open and require a specified compactification.

Three possible outcomes: (a) full isomorphism + conjugacy — same universality class, OI's specific predictions transport to the compactification; (b) algebras isomorphic, channels differ — different classes despite leading-order SM agreement, predictions class-specific; (c) algebras not isomorphic — different higher-dimensional structure, the most likely outcome based on the landscape's UV-completion multiplicity. The expected outcome is (b) or (c): different SM-reproducing compactifications generically produce different higher-dimensional operators with different Wilson coefficients, so OI's specific predictions are likely class-specific rather than universal across the SM-reproducing landscape — consistent with the structural-realism stance of §12.1.

### 13.1.2 Q2 developed: criteria for prediction transport

Q2 asks whether OI's specific predictions are universal at the universality-class level or specific to OI's representative within the class. Q1's outcome decomposition implicitly resolves much of Q2 — under outcome (a), predictions transport; under (b) and (c), they do not. Direct treatment refines the picture by stratifying predictions across the universality-class hierarchy of §9.5: predictions at the *partial-trace-features level* (Born rule, channel positivity, non-Markovianity index, commutant pattern) transport trivially; predictions at the *gauge-group level* (anomaly conditions, no flavor-changing neutral currents at tree level) transport across all members sharing the gauge group; predictions at the *algebra-channel level* (Yukawa values, CKM structure, RG trajectories) transport only under outcome (a)'s isomorphism + conjugacy; predictions at the *substratum level* (combinatorial counts on the cubic lattice, specific spectral properties) do not transport in general.

OI's specific predictions sit at varying levels: the Cabibbo angle $\theta_C = 1/(\pi\sqrt{2})$ from cubic-group representation theory is substratum-specific; the Koide ratio $Q = 2/3$ is intermediate (gauge-group structure × cubic-group multiplicity, likely substratum-specific); the Bekenstein-Hawking $A/4$ coefficient is more universal — string theory derives the same coefficient through Strominger-Vafa's microscopic D-brane count, suggesting common universality-class membership or substratum-independent thermodynamic forcing. The general answer: OI's specific predictions are mostly substratum-level features of OI's specific universality-class representative, with exceptions that follow from gauge-group structure or partial-trace observational features. The practical upshot: validating OI's predictions supports OI's specific representative; falsifying them would refute that representative without necessarily refuting the broader universality-class framework.

### 13.1.3 Q3 developed: necessary and sufficient features for the partial-trace observational class

Q3 asks whether the four features of §14 (Born rule, channel-level unitarity, P-indivisibility, commutant gauge-invariance pattern) are necessary and sufficient to characterize the partial-trace observational features class. *Necessary:* yes, modulo qualifications. The first two follow directly from the embedded-observer triple definition (Born rule from partial-trace structure; channel-level unitarity from Stinespring's theorem). P-indivisibility is necessary under hidden-sector entanglement; commutant gauge-invariance under substratum symmetry. *Sufficient:* no. Two embedded-observer triples sharing all four features can be observationally inequivalent by differing on specific algebraic relations (Yukawa couplings, anomaly content, central extensions), specific channel dynamics (RG flow, threshold corrections, non-perturbative effects), or Hilbert-space structure (multiplicity of irreducible representations, Type classification). The four features characterize a *meta-class* containing many universality classes as sub-classes — consistent with §9.5's hierarchical structure.

Refinement candidates that would tighten the characterization: (α) information-theoretic structure of the marginal (Holevo bound, mutual-information capacity); (β) spectral properties of the channel (eigenvalues, decay times, ergodic structure); (γ) multi-time correlation structure (three-time, four-time non-Markovian features beyond P-indivisibility). These would add necessary conditions but are not expected to be jointly sufficient: Definition 9.3's *-isomorphism criterion depends on specific algebraic content that no finite list of generic features can fully capture. Provisional resolution: the four features are necessary at the partial-trace level (under stated qualifications) but not sufficient to determine universality classes uniquely; full identification requires the algebra-channel-level work of §13.1.1 and §13.1.2.

### 13.1.4 Q4 developed: other universality classes that may produce the SM

Q4 asks whether the SM-reproducing universality class includes substrata other than OI's and string theory's. Principal candidates are loop quantum gravity (LQG)–derived structures, causal-set–derived structures, and asymptotic-safety–derived structures. The per-condition A1–A6 analysis applied to these programs in the manner of §6 yields preliminary structural conclusions. We give compact treatments of the three principal candidates; the analysis is more telegraphic than the string-theoretic case in §§3–7, since the goal is to characterize structural compatibility at the level of OI's substratum conditions, not to reproduce a full per-program audit.

**Loop Quantum Gravity.** LQG's substratum [Rovelli2004; AshtekarLewandowski2004] is the space of spin networks — graphs labeled by SU(2) representations and intertwiners — modulo spatial diffeomorphisms. Dynamics is defined either by Thiemann's Hamiltonian constraint on the kinematical Hilbert space or by spin-foam amplitudes summing over histories. Per-condition: A1 (finiteness) **fails** in the full theory — even at fixed graph, the Hilbert space is infinite-dimensional through unbounded spin labels, and the sum-over-graphs structure of the full theory makes $|S| = \infty$ generically; finite-graph and bounded-spin variants admit a finite reading but are not standard LQG. A2 (determinism / bijection) **fails** — the dynamics is quantum, with spin-foam amplitudes constructed as Feynman-like sums rather than deterministic bijections on configuration space. A3 (bounded coupling degree) holds at fixed graph valence (typically ≤ 4 in EPRL spin foams) but the bounded-coupling reading depends on the graph being fixed, which is in tension with sum-over-graphs. A4 (center independence) **holds** — diffeomorphism invariance is built in. A5 (linearity) **holds** at the operator level (the Hamiltonian constraint is a linear operator on Hilbert space) but is complicated by the constraint structure: solutions to the constraint are highly nonlinear in the spin-network labels even when the constraint operator itself is linear. A6 (background independence) **holds** — this is LQG's defining feature. Net: A1 and A2 fail; A4 and A6 hold robustly; A3 and A5 are reframing-dependent. The structural pattern of failure is similar to string theory's matrix-model formulation in §6, with the key structural mismatches at A1 and A2 being deeper than the discretization-bridge issue of §6.1 — LQG's quantum dynamics and infinite Hilbert spaces are central to the program rather than artifacts of a particular formulation.

**Causal sets.** The causal-set program [BombelliLeeMeyerSorkin1987; RideoutSorkin1999; Surya2019] takes the substratum to be a locally finite partially-ordered set, with dynamics typically modeled by Classical Sequential Growth (CSG) — a stochastic generative process that adds events according to a probability measure on histories. Per-condition: A1 (finiteness) **holds at any finite stage** (finite causal sets are genuinely finite) but **fails** in the limit of unbounded growth. A2 (determinism / bijection) **fails** — CSG is explicitly stochastic, with each event-addition governed by a probability rather than a deterministic update rule. This is the most direct structural divergence from OI's substratum: where OI takes the substratum dynamics to be deterministic with stochasticity emerging through partial trace, causal sets take the dynamics to be intrinsically stochastic at the substratum level. A3 (bounded coupling) holds: each event has a finite number of immediate predecessors and successors. A4 (center independence) **holds** — the formalism is intrinsically relational. A5 (linearity) does not translate cleanly — CSG is described by transition probabilities rather than a wave equation, so OI's linearity-of-wave-equation framing has no direct analog. A6 (background independence) **holds**. Net: A2 fails outright, A1 fails in the limit, A5 lacks a clean translation. Causal sets and OI agree on relational structure (A4, A6) but diverge sharply at the determinism axis (A2). The structural-realist reading: OI's substratum and the causal-set substratum represent different commitments at the foundational level, with OI placing the stochasticity at the partial-trace observational layer while causal sets place it at the substratum layer.

**Asymptotic safety.** The asymptotic-safety program [Weinberg1979; Reuter1998; Eichhorn2018] takes gravity to be defined by a non-Gaussian UV fixed point of the renormalization group, with the metric as the dynamical variable in a continuum quantum field theory framework. Per-condition: A1 (finiteness) **fails** — continuum QFT. A2 (determinism / bijection) **fails** — quantum, path integral. A3 (bounded coupling) reframing-dependent in the same way as for matrix models; the natural reading at the spacetime level has unbounded coupling. A4 (center independence) **holds** — general covariance. A5 (linearity) **fails** — Einstein-Hilbert action plus higher-derivative terms is nonlinear in the metric, with the nonlinearity essential to producing gravitational dynamics. A6 (background independence) **holds**, modulo standard subtleties about expanding around fixed backgrounds. Net: similar pattern to string-theoretic matrix models — A2, A5, A1 fail; A4 and A6 hold; A3 reframing-dependent. The structural pattern resembles string theory closely.

**Cross-program pattern.** All three candidate programs fail OI's A2 (determinism / bijection) for the same structural reason — they are quantum or stochastic theories at the substratum level, with substratum dynamics defined by path integrals or probability measures rather than by deterministic bijections. All three fail A1 (finiteness) in their standard formulation, though variants admit finite readings. A4 and A6 hold robustly across all three. A3 and A5 vary by program. Net: none of the three candidates are in OI's specific universality class as that class is delimited by A1–A6. The deeper reading is that determinism (A2) is the most discriminating structural condition — it cleanly separates OI's class from all four candidates considered (string theory in §6 plus LQG, causal sets, asymptotic safety here). This is consistent with the framework's foundational commitment per [Substratum §1.1]: the determinism of $\varphi$ is what allows the trace-out to produce QM as the unique embedded-observer description, with stochasticity emerging from observer-ignorance rather than substratum-intrinsic randomness.

**Partial-trace-features class membership.** Although none of the candidate programs are in OI's specific universality class (per A1–A6 failure), all three may share the partial-trace observational features class. Each program is intended to reproduce SM-compatible low-energy physics, which forces Born-rule structure at the observational level (the theories are quantum); channel-level unitarity follows from Stinespring's theorem applied to any embedded-observer reading; P-indivisibility is more program-specific (LQG's spin-foam dynamics and causal-set CSG dynamics may or may not produce non-Markovian marginal observation in the OI sense); commutant gauge-invariance pattern depends on the gauge structure of each program's emergent QFT. For each candidate, partial-trace-class membership is open and would require the algebra-channel comparison work flagged in §13.1.1 for the OI–string case. The pattern of expected outcomes mirrors §13.1.1's three-outcome decomposition: most likely the algebras differ at higher-dimensional operator structure even where partial-trace features agree, placing each candidate in the partial-trace-features meta-class but in a different sub-class within it.

**Implications for §11 and Limit 1.** The Q4 development extends the §11 OI-string class analysis from one comparison program to four. §11.3's provisional characterization of the OI-string relationship as "same partial-trace-features class, possibly different algebra-channel class" extends to the OI-LQG, OI-causal-set, and OI-asymptotic-safety relationships under the same provisional reading. Limit 1's "one concrete data point" claim is updated by §13.1.4 to a partial census across four programs (per §13.3 update below). The natural research direction left open is the per-program partial-trace-feature audit: for each candidate, does the program's emergence machinery produce all four features of §14, and do the algebras agree at SM-reproducing target?

### 13.2 Conceptual questions

**Q5.** Is the universality-class framework the right level of abstraction, or is it too coarse to capture features relevant for fundamental physics? (E.g., quantum gravity might depend on substratum-level features that universality classes wash out.)

**Q6.** Does the universality-class framing weaken or strengthen OI's predictive content? On the one hand, OI's predictions are class-specific rather than universal, which weakens their status. On the other hand, the framework establishes that class membership is what's real, which strengthens the claim that finding the right class is the right research target.

**Q7.** What is the relationship between universality classes of embedded observers and other equivalence classes in fundamental physics (e.g., RG universality classes, equivalent QFTs related by dualities, holographic correspondence between bulk and boundary descriptions)?

### 13.2.1 Q5 developed: is universality-class abstraction the right level?

Q5 asks whether the universality-class framework is too coarse to capture features relevant for fundamental physics — particularly quantum gravity, which might depend on substratum-level features that universality classes wash out. The Q1–Q4 developments give a partial answer: the framework operates at multiple levels of abstraction, with the partial-trace-features class as the most universal, the SM-reproducing class as intermediate, the OI–A1–A6 class narrower, and substratum-level features narrowest. Quantum-gravity content lives at varying levels: holographic entropy laws ($S = A/4$) are at the partial-trace-features level (per §11) since the same coefficient is reached by different substrata through different mechanisms; specific Planck-scale corrections to dispersion relations or graviton propagators are substratum-level (different programs predict different corrections). The framework's claim is therefore not that universality-class abstraction is the *only* relevant level, but that different physical predictions live at different levels, with the abstraction level matching the prediction's structural status. The honest concern remains: if QG predictions of phenomenological interest (specific signatures of substratum discreteness in cosmic-ray observations, specific corrections to graviton dispersion, specific non-perturbative effects at Planck scale) are intrinsically substratum-level, then universality-class framing offers limited purchase on them — these are framework-specific predictions, not class-level ones. Whether this is a limit or a feature depends on whether the prediction class one cares about is universal or class-specific; the framework itself does not adjudicate. The methodological answer is that universality-class abstraction is the appropriate level *for those predictions that live at it*, with framework-specific predictions retaining their status as predictions of the specific representative — in OI's case, of OI's universality-class representative within the broader meta-class.

### 13.2.2 Q6 developed: does universality-class framing weaken or strengthen OI's predictive content?

Q6 asks whether the universality-class framing weakens or strengthens OI's predictive content — class-specificity reduces the absolute reach of OI's predictions, but it sharpens what the predictions *are* predictions of. The dual reading: *weakened* in absolute terms — OI's Cabibbo-angle prediction $\theta_C = 1/(\pi\sqrt{2})$ is a feature of OI's specific universality-class representative, not a universal feature of any SM-reproducing framework, so confirming the prediction does not falsify all alternatives but only those in different universality classes; *strengthened* in framework-relative terms — the prediction is structurally forced *within* OI's class, and class membership is itself an empirically meaningful claim rather than a framework-internal stipulation. The methodological reframing follows §12.2: empirical confirmations support OI's specific-class membership, while the broader question of whether other classes also reproduce these predictions becomes the next-order empirical inquiry. Practically, OI's predictive content is most sharply expressed as conditional: *given OI's class membership*, $\theta_C = 1/(\pi\sqrt{2})$; the unconditional reading "$\theta_C = 1/(\pi\sqrt{2})$ is a universal feature of SM-reproducing physics" is not what the framework establishes. Confirmation under either reading is empirical support, but the conditional form is structurally honest about what the framework demonstrates. The Q4 development above sharpens this by adding three programs (LQG, causal sets, asymptotic safety) that share OI's SM-reproducing target but lie outside OI's class; for each, whether OI's specific predictions transport is open, and the answer is empirically meaningful in the same sense as for the OI–string comparison. The strengthening reading dominates in research-program terms: identifying the right universality class is a sharper target than identifying "the" theory, and the framework's predictions become diagnostic for class membership rather than absolute claims about reality.

### 13.2.3 Q7 developed: relationship to other equivalence classes in fundamental physics

Q7 asks how universality classes of embedded observers relate to other equivalence classes prominent in fundamental physics — RG universality classes (different microscopic theories with the same long-distance behavior), QFT dualities (different descriptions of the same theory), and holographic correspondences (bulk and boundary descriptions of the same physics). The relationships differ in structure. *RG universality classes* are the closest mathematical analog: they identify substrates as equivalent if they produce the same long-distance / coarse-grained behavior, with the equivalence relation defined by RG flow rather than by partial-trace observation. The frameworks are compatible — RG-universality-equivalent substrates would typically also be partial-trace-observation-equivalent, since the partial-trace observation depends on long-distance content — but partial-trace observational equivalence is in general a *weaker* equivalence: it can fail to distinguish substrates that RG flow distinguishes if the trace-out integrates over precisely those microstructure features that RG preserves. *QFT dualities* (S-duality, T-duality, mirror symmetry, AdS/CFT) identify two theory descriptions as equivalent — the duality is an isomorphism of the operator algebras and dynamics, not a partial-trace relationship. Dual descriptions are automatically in the same universality class in §9's sense (they have *-isomorphic algebras and conjugate channels). *Holographic correspondence* is a specific kind of duality: bulk and boundary descriptions are dual, with the boundary acting as the "observable" side of an embedded-observer reading. The universality-class framework's relationship to holography is closer than to RG: holographic correspondence is consistent with viewing the boundary as visible-sector and the bulk as hidden-sector, with dualities of bulk descriptions being automorphisms of the channel rather than separate classes. Practically, the universality-class framing is *broader* than RG (capturing structural features that RG washes out, such as gauge-group structure and observer-admission status) and *broader* than dualities (capturing equivalences across non-dual frameworks like OI and string theory at the partial-trace level), and is *consistent with* holography in the sense that holographic dualities operate within universality classes rather than across them. Whether universality-class abstraction *adds* something beyond the union of RG, dualities, and holography is the essential question; the present framing's claim is yes — it captures structural agreement between programs (like OI and string theory) that no RG, duality, or holographic relationship establishes, since those relationships operate within frameworks while universality-class observational equivalence operates across them.

### 13.3 Limits of the approach

The universality-class framework has limits worth flagging.

**Limit 1: Programmatic with a partial census.** The framework articulates the universality-class question and provides candidate formalizations. Per §13.1.4, four programs (string theory, LQG, causal sets, asymptotic safety) are now positioned within the universality-class hierarchy: all four fail OI's A1–A6 and are therefore outside OI's specific class, but all four may be in the broader partial-trace-features class (the per-program partial-trace audit is open). The framework remains programmatic in that systematic enumeration of universality classes is incomplete and the partial-trace-features class membership question for each candidate is unresolved; however, the cross-program structural pattern (A2 determinism is the most discriminating condition; A4 and A6 robustly hold across all candidates) provides constructive content beyond the bare existence of the universality-class question.

**Limit 2: Depends on operator-algebra technology.** The algebraic formalization adopted in §8.4 and used throughout §9 depends on operator-algebra and CPTP-channel theory. These are well-developed but place the framework in a specific mathematical setting. Frameworks that do not naturally admit operator-algebra description (e.g., theories with no clear Hilbert-space structure) may not fit the formalization without modification.

**Limit 3: Depends on continuum / discrete bridge.** The framework assumes that substratum descriptions, regardless of discreteness, produce CPTP channels with operator-algebra structure on visible-sector observables. For OI's discrete substratum and string theory's continuum substratum, this is plausible (both produce QM at the observable level). For substrata whose visible-sector observable structure is not of this form, the framework may not apply.

### 13.4 Relationship to the methodology paper

The universality-class framework is closely related to a planned methodology paper articulating OI's overall posture for philosophy-of-physics venues. The methodology paper would cover the broader posture (constructive structural realism, single-foundational-commitment derivation, per-theorem no-go evasion, "physics modulo gauge" reframing); the universality-class framework provides the technical machinery for the structural-realism component when applied to comparison with other unification programs. The two contributions are companions: the methodology paper situates OI's posture in the philosophy-of-physics literature; the universality-class framework provides one technical articulation of what that posture entails.

---


---

# Part III: Cross-Framework Synthesis

## 14. Cross-framework derivation of observational structures

This section develops the constructive content of recovery (v) — shared observational invariants — by examining whether structural features of OI's trace-out also follow from string theory's emergence mechanisms. The framing is that observation is a structurally privileged operation: OI's substratum and string theory's substrata are different, but the *act of observation* on each substratum produces observational features that may be substratum-independent.

We proceed feature by feature. For each, we characterize the structural feature in OI's framework, identify the analogous mechanism in string-theoretic emergence, and assess whether the feature transports across frameworks. Four features are examined: the Born rule, channel-level unitarity, P-indivisibility, and commutant gauge-invariance.

The discussion is technical but exploratory. The aim is not to prove cross-framework equivalence at the observational level — that would require substantial work beyond chat-track scope — but to establish whether the proposed shared invariants are structurally well-defined in both frameworks. If they are, recovery (v) admits constructive sharpening; if some don't transport, the framework's universality claims must be refined.

### 14.1 The Born rule

**OI's framing.** OI derives the Born rule (probability $|\psi|^2$ for measurement outcomes) from the embedded-observer trace-out [Main §3]. The visible-sector density matrix $\rho_V = \text{Tr}_H |\psi\rangle\langle\psi|$ produces probabilities for visible-sector observables via $p(a) = \text{Tr}(\Pi_a \rho_V)$, where $\Pi_a$ is the projector onto outcome $a$. The Born rule is not postulated; it follows from the partial-trace structure of the observer's marginal description.

**String-theoretic analog.** String theory uses standard quantum mechanics throughout — in matrix-model formulations (BFSS, IKKT), in worldsheet conformal field theory, and in the boundary CFT of AdS/CFT correspondence. The Born rule is built in as a feature of QM. When an observer in a string-theoretic context measures an observable, the probability is given by the standard quantum-mechanical trace formula on the boundary CFT or the worldsheet.

**Transport assessment.** The Born rule transports straightforwardly. Both frameworks use the same partial-trace structure to extract probabilities for subsystem observables. The distinction is that OI *derives* the Born rule from substratum-level structure (classical bijection lifted to Stinespring dilation, traced down to observer marginal), while string theory *assumes* the Born rule as a feature of its quantum-mechanical apparatus.

This is consistent with the shared-invariants reading: the Born rule is a structural feature of partial-trace operations on quantum states. Any framework using partial traces to extract subsystem observables produces the Born rule; OI's contribution is showing that this structure is forced even when the substratum is classical, via the Stinespring lift. The Born rule itself is empirically tested at the $10^{-3}$–$10^{-4}$ level via multi-path interferometry [Sinha2010, Söllner2012], with ongoing precision improvements through ultracold-atom platforms [Kanthak2025] (further discussion in §15.5).

### 14.2 Channel-level unitarity

**OI's framing.** OI's visible-sector dynamics is a CPTP channel $\Phi$ generated by the trace-out of substratum bijection dynamics over the hidden sector [Main §3.2]. Stinespring's theorem [Stinespring1955] identifies $\Phi$ as the partial trace of a unitary $U$ acting on the dilated Hilbert space $\mathcal{H}_V \otimes \mathcal{H}_H$. Channel-level unitarity is the statement that the dilation $U$ is unitary; the visible-sector channel $\Phi$ is generally non-unitary (because of the trace-out's loss of information to the hidden sector) but lifts to unitary dynamics on the dilation.

**String-theoretic analog.** AdS/CFT bulk reconstruction has a closely analogous structure. Boundary CFT operators are encoded in bulk operators with redundancy, and the encoding is a quantum error correcting code [HarlowBulkReconstruction2018, AlmheiriDongHarlow2014]. Bulk reconstruction from boundary subregions ("entanglement wedge reconstruction") shows that bulk operators in the entanglement wedge of a boundary subregion can be reconstructed from operators on that subregion. The reconstruction is unitary at the level of the full bulk-boundary system, with effective non-unitarity arising when restricting to a subregion.

The structural parallel is direct: in AdS/CFT, the "trace-out" is restriction to a boundary subregion, and the "visible-sector channel" is the effective dynamics on that subregion after tracing over the complement. The bulk-boundary system as a whole is unitary; the subregion-level channel is generally non-unitary; the channel admits a unitary dilation given by the full bulk reconstruction.

**Transport assessment.** Channel-level unitarity transports across frameworks. Both OI and AdS/CFT have the same structural feature: a CPTP channel at the observable level lifting to unitary dynamics on a dilation. The dilation in OI is the Stinespring lift to $\mathcal{H}_V \otimes \mathcal{H}_H$; in AdS/CFT, the dilation is the full bulk-boundary system before restricting to a subregion.

A subtle but important point: the *mechanism* by which dilation produces unitarity is different. OI's dilation is mathematically the Stinespring construction applied to a classical-substratum bijection; AdS/CFT's dilation is the holographic encoding of bulk operators in boundary degrees of freedom via the gravitational path integral. Both produce unitary dilations of CPTP visible-sector channels, but through different mechanisms. The shared structural feature is the dilation pattern itself, not the specific machinery producing it.

### 14.3 P-indivisibility (non-Markovian marginal)

**OI's framing.** OI derives Bell violations and contextuality from the *non-Markovian* character of the embedded observer's marginal stochastic process [Main §2.3]. P-indivisibility is the statement that the visible-sector probability evolution does not satisfy the Markov property: $P(a_3 | a_2, a_1) \neq P(a_3 | a_2)$ in general, because hidden-sector correlations carry information across time. The non-Markovian marginal is what allows OI to evade Bell's theorem (per [Substratum §6.4]): factorizability fails at the observer level via the trace-out.

**String-theoretic analog.** Holographic effective field theories explicitly classify modes by their Markovianity. The sound scalar in compressible relativistic fluids dual to AdS planar black holes is a non-Markovian field with Markovianity index $3 - d$ for a $d$-dimensional fluid. The holographic Schwinger-Keldysh formalism [HolographicSK2024, HolographicNonHydro2024] derives effective field theories that include non-Gaussian noise and non-Markovian dynamics as features of the boundary effective description, arising from integrating out bulk degrees of freedom. The non-Markovian behavior is recognized as a generic feature of holographic effective theories, not a special case.

The structural parallel is striking: in both frameworks, restricting attention to a subset of degrees of freedom (visible sector in OI; boundary subregion in AdS/CFT; long-lived hydrodynamic modes in holographic effective theory) produces non-Markovian effective dynamics on the restricted subset, with the non-Markovianity arising from the integrated-out degrees of freedom carrying memory across time.

**Transport assessment.** P-indivisibility transports across frameworks, with appropriate translation. OI's framing emphasizes the failure of factorizability at the observer level; the holographic framing emphasizes the Markovianity index of effective modes. These are different ways of articulating the same structural feature: the marginal description on a subset of degrees of freedom is non-Markovian when the integrated-out degrees of freedom have memory.

This is significant. P-indivisibility was the OI-specific framing most likely to fail to transport to string theory; the holographic-Markovianity literature shows that the same structural feature appears in string-theoretic effective descriptions. The Bell-violation evasion route in OI's framework — non-Markovian marginal, not fundamental nonlocality — has a direct holographic analog in non-Markovian effective field theories derived from AdS/CFT.

The mechanism — non-Markovian visible dynamics from trace-out of hidden degrees of freedom — has independent theorem-level corroboration. [BrandnerMeyer2025] establishes a rigorous weak-memory regime for autonomous linear evolution equations with hidden-degree-of-freedom coupling, providing a controlled framework for the non-Markovian visible dynamics OI invokes. [TomizukaTakeda2026] constructs a structurally identical hidden-model decoherence picture independently, motivated by classical–quantum dynamics in gravity. [Barandes2026]'s stochastic-quantum theorem establishes the precise correspondence between indivisible (non-Markovian) stochastic processes and unitary quantum systems that [Main §3.4]'s reverse-direction lemma relies on. The framework's central technical move therefore sits within an established theorem-level structure in the open-systems and quantum-foundations literatures (§15.1 develops this in detail).

### 14.4 Commutant gauge-invariance

**OI's framing.** OI's emergent QFT inherits gauge invariance from the substratum's commutant structure [SM §3.1]. Cubic-group decomposition of the $K = 6$ internal components produces multiplicities $(3, 2, 1)$, with the commutant of the cubic-group action on the $K = 6$ space being $SU(3) \times SU(2) \times U(1)$. Background independence (A6) promotes the global commutant symmetry to local gauge invariance. The trace-out preserves only commutant operators (those commuting with the gauge group action), so observable correlations are gauge-invariant by construction.

**String-theoretic analog.** Gauge invariance in string-theoretic emergence has multiple sources, but the closest analog to OI's commutant structure is the *open-string sector* of D-brane stacks. A stack of $N$ D-branes has $U(N)$ gauge symmetry generated by the open-string excitations on the brane worldvolume; the commutant of the worldvolume action gives the gauge group. Restricting to closed strings (graviton sector) gives the singlets under the gauge group, analogous to OI's trace-out preserving only commutant operators.

For AdS/CFT specifically, the boundary CFT has a global symmetry that becomes a bulk gauge symmetry under the duality. Boundary operators charged under the global symmetry correspond to bulk fields charged under the gauge symmetry; gauge-invariant bulk physics corresponds to singlet boundary operators. The commutant structure is preserved across the duality.

**Transport assessment.** Commutant gauge-invariance transports across frameworks, with the caveat that the specific gauge groups produced differ. In OI's framework, the gauge group is $SU(3) \times SU(2) \times U(1)$ derived from the cubic-group commutant on $K = 6$ components. In string-theoretic compactifications, the gauge group depends on the specific compactification — D-brane configurations, fluxes, Calabi-Yau topology — and the SM gauge group is realized through specific arrangements rather than forced by a unique commutant structure.

The structural feature that transports is *the gauge-invariance pattern via commutant restriction* — both frameworks have observable physics determined by the commutant of some symmetry action on the substratum. The structural feature that does not transport in the same form is *the specific commutant producing $SU(3) \times SU(2) \times U(1)$* — OI derives this from the cubic-group; string theory realizes it from specific compactification choices.

This partial transport refines the shared-invariants claim: the commutant gauge-invariance pattern is universal (any framework with substratum-level symmetry produces gauge-invariant observables via commutant restriction), but the specific gauge group obtained depends on the substratum's symmetry structure. The SM gauge group is forced in OI's framework by the cubic-group symmetry; in string theory, it's one of many possible commutants.

### 14.5 Synthesis

The four-feature audit produces a mixed transport pattern:

| Feature | Transports? | Caveat |
|---|---|---|
| Born rule | Yes | Both frameworks use partial-trace structure on quantum states |
| Channel-level unitarity | Yes | Different dilation mechanisms (Stinespring vs holographic) |
| P-indivisibility | Yes | Non-Markovian marginal explicit in both (holographic Markovianity index, OI's P-indivisibility) |
| Commutant gauge-invariance | Pattern transports; specific commutant does not | OI's cubic-group commutant produces $SU(3) \times SU(2) \times U(1)$ uniquely; string theory's commutants are compactification-dependent |

The first three features transport directly. The fourth transports as a *pattern* (gauge invariance via commutant) but not as a *specific output* (the SM gauge group is uniquely forced in OI but compactification-dependent in string theory).

This refines recovery (v) substantively. The shared-invariants claim holds for the structural features of partial-trace operations on quantum states (Born rule, channel-level unitarity, non-Markovian marginal). It does not hold uniformly for substratum-symmetry-derived structures (the specific gauge group), because substratum symmetries are framework-specific.

The picture that emerges: **the structural features of observation as such — what observation extracts from any quantum state under partial trace — are substratum-independent**. The structural features of observation *plus substratum symmetry* — what observation extracts when conditioned on the symmetry structure of the substratum — are framework-specific. OI and string theory share the former; they differ on the latter because their substratum symmetries are different.

This conclusion has implications for the universality-class question developed in the Part II below. If embedded-observer structures produce universal observational features (Born rule, unitarity, non-Markovianity, commutant restriction pattern) but framework-specific gauge content, then the universality classes of embedded observers might be characterized by which gauge structures they admit. OI's universality class would include any substratum producing $SU(3) \times SU(2) \times U(1)$ via cubic-group-like commutant; string theory's class would include any compactification producing the same gauge group via specific brane/flux arrangements. The classes intersect on the SM gauge group as a target but reach it through different substratum-symmetry mechanisms.

### 14.6 Implications for the OI-string relationship

The cross-framework analysis of §14.1–14.5 establishes that recovery (v) — shared observational invariants — has substantive content for the structural features of partial-trace observation, with refinement at the level of substratum-symmetry-dependent features.

This refines the conclusion of §7.7 and §14.5: OI and string theory are not equivalent at the substratum level (per §6), and they do not share *all* observational features (per §14.4 caveat), but they do share the structural features that follow from the partial-trace operation itself (per §14.1–14.3 and the pattern-transport in §14.4). The intersection is at a precisely-characterized level: the observable consequences of partial-trace operations on quantum states, independent of the specific substratum producing those states.

This intersection is non-trivial. It means: any framework that produces observable physics through partial-trace observation on a quantum state automatically inherits the Born rule, channel-level unitarity, non-Markovian marginal, and commutant gauge-invariance pattern. OI and string theory do this through different substratum-level machinery; the observational consequences agree because partial-trace observation has structural features that are substratum-independent.

The constructive content of recovery (v) is therefore: **partial-trace observation is itself the locus of substratum-independent structure**. Observation is what's invariant across substratum descriptions, and observation's structural features are forced by the partial-trace operation, not by what's being traced. This connects directly to OI's main paper's "observation occurs" axiom: observation is foundational, and its features are the shared content between any two substratum descriptions producing observable physics.

What does not transport — the specific gauge group, the specific particle content, the specific predictions — is what distinguishes substratum descriptions empirically. OI's predictions for the Cabibbo angle and Koide ratio are features of OI's specific substratum-symmetry derivation; string theory's compactifications would need to reproduce these as features of specific compactification choices. The two frameworks agree on the *kind* of physics observation produces; they differ on the *specific content*.

This is a more refined picture than the §7.1 framing of "OI and string theory as independent programs." They are independent at the substratum level, share structural features at the partial-trace level, and may or may not converge at the specific-content level depending on which compactifications string theory can realize as SM-reproducing. The recovery (v) analysis identifies precisely where the intersection lives: at the level of partial-trace structural features, not above and not below.

---

## 15. Theoretical and empirical corroboration

The framework's claims are of mixed types. Some are directly empirical (the Born rule, channel-level unitarity, non-Markovian marginal observation) and admit precision experimental tests. Others are structural — the partial-trace mechanism, the algebra-channel formalism, the universality-class hypothesis — and are corroborated through theorem-level results in independent literatures and through analog constructions in adjacent fields. This section collects the most consequential corroborations, organized by claim type. The ordering reflects strength of support: §15.1 documents the strongest external corroboration (theorem-level results for the framework's central technical mechanism); §15.5 acknowledges what remains under-supported.

### 15.1 The partial-trace mechanism

The framework's central technical move — that visible-sector dynamics under trace-out of a hidden sector is generically non-Markovian and admits a unitary quantum description — has theorem-level corroboration in three independent recent results.

**Stochastic-quantum correspondence at theorem level.** Barandes [Barandes2026], building on [Barandes2023, Barandes2025], establishes a precise correspondence theorem: every indivisible stochastic process on a configuration space corresponds to a unitarily evolving quantum system, and conversely, every quantum system can be represented as such a process. The theorem provides a first-principles explanation for why quantum theory uses complex Hilbert spaces, linear-unitary evolution, and the Born rule. This is the technical machinery [Main §3.4] uses to bridge the trace-out from the deterministic substratum to the emergent quantum description, now established at theorem-level rigor in the foundations literature independent of the OI framework's specific content. [Main]'s reverse-direction lemma (every P-indivisible process on a finite configuration space admits a deterministic dilation) is consistent with and relies on the same correspondence.

**Weak-memory regime for hidden-degree-of-freedom dynamics.** Meyer and Brandner [BrandnerMeyer2025], following [Brandner2025a], prove that for autonomous linear evolution equations describing systems coupled to inaccessible degrees of freedom, integrating out those degrees of freedom yields well-defined non-Markovian visible dynamics in a weak-memory regime, with explicit error bounds and a convergent perturbation scheme. The setting is general open quantum systems with no stake in OI being right, and the conclusion is that visible-sector dynamics with hidden-sector memory is a mathematically clean construction with a rigorous regime of validity. The framework's (C2) slow-bath condition and the resulting non-Markovian visible dynamics fall within this regime, so the framework's central technical move sits inside an established theorem.

**Hidden-model decoherence producing classical–quantum dynamics.** Tomizuka and Takeda [TomizukaTakeda2026] construct an explicit hidden model in which a mediator is coupled to additional unobserved environmental degrees of freedom, and derive the resulting reduced dynamics by tracing them out. The reduced dynamics is generically non-Markovian, reflecting environmental memory effects. Their motivation is the question of whether classical–quantum dynamics in gravity can arise as effective descriptions of fully quantum systems; the construction is structurally identical to OI's mechanism (visible–hidden partition, unitary on the dilation, trace-out producing non-Markovian visible dynamics) developed independently for a different physics question. The structural identity is independent corroboration that the OI mechanism is the standard way the open-systems literature now thinks about hidden-degree-of-freedom dynamics.

**Experimental implementation in quantum metrology.** The hidden-Markov-model framework underlying the partial-trace mechanism has direct experimental implementation in quantum metrology [QECNonMarkovian2025]: the model is Markovian on the joint system + environment and non-Markovian on the visible-sector reduced state, with information backflow from the environment producing the framework's signature non-Markovian behavior. The framework's mechanism is therefore not only mathematically rigorous but realizable in current experimental quantum-information platforms.

### 15.2 The algebra-channel formalism

The §8.3 / §9.1 algebra-channel formalization adopted in this paper draws on standard machinery from algebraic quantum field theory (AQFT). The formalism's reliability and expressive power are established in the AQFT literature.

**AQFT canonical references.** The Brunetti–Fredenhagen / Buchholz–Fredenhagen program [BrunettiFredenhagen2024] develops the algebraic approach to QFT through nets of local von Neumann algebras with isotony, microcausality, and covariance, with states arising as positive normalized linear functionals on the algebras. The structure used in §10.4's construction of OI's algebra-channel pair — a von Neumann algebra of gauge-invariant local observables, with the channel implementing the trace-out via Stinespring dilation [Stinespring1955] — is standard within this framework. [Yngvason2005] establishes that the local algebras of relativistic QFT are typically type III von Neumann factors, which has consequences for entanglement and the modular structure that §10.4's construction inherits. [LabuschagneMajewski2025] provides recent updates to the algebraic framework on curved spacetime, relevant to OI's GR-emergence cluster.

**Stinespring dilation as universal device.** The Stinespring representation theorem [Stinespring1955] guarantees that every CPTP channel admits a unitary dilation. §9.2 (Definition 9.2) and §10.4's channel construction invoke this directly. The recent literature has refined Stinespring dilations into a working tool for quantum channel learning and metrology, including channel tomography techniques [RandomStinespring2025] that provide protocols for distinguishing channels via their dilations — the operational analog of the §13.1.1 four-step recipe's channel-conjugacy step.

### 15.3 Structural realism in operational and dual-theory contexts

The hierarchical structural-realism position developed in §2 and §12 is supported by independent work in philosophy of physics that arrives at compatible positions through different routes.

**Operational theories as structural realism.** Adlam [Adlam2022] argues that operational axiomatizations of quantum mechanics (Hardy [Hardy2001], Barrett [Barrett2007], and the broader Mackey [Mackey1963] tradition) can be interpreted as a novel form of structural realism: probing the modal structure of possible operational theories, with quantum mechanics as a specific point in this space. The view aligns with Structure's two-dimensional hierarchy (observation × gauge): the observational axis corresponds to Adlam's modal-structure-of-operational-theories framing, and the gauge axis corresponds to Structure's parallel articulation of the gauge-equivalence levels at which structural commitment lives. The framework's structural-realism commitment is therefore situated within an active research program in philosophy of physics, not a novel position in isolation.

**Common-core realism in QM-string dualities.** Dawid and Franzmann [DawidFranzmann2025] develop a structural-realism account specifically for dualities in quantum mechanics and string theory, accommodating ontological pluralism while preserving structural realism through what they call "common core realism" — the proposal that invariant structure across dual models is the proper target of realist commitment. This is precisely the conceptual move §12.1 makes in the universality-class framing: the realist commitment is to structure invariant across substratum descriptions, with specific substratum content being framework-relative. Their work cites parallel programs by Matsubara–Johansson, Rickles, Huggett, and De Haro–Butterfield that converge on similar positions. The universality-class proposal of §9 can be read as one technical articulation of common-core realism specialized to embedded-observer systems.

### 15.4 Universality classes in adjacent literatures

The universality-class framework of §9 is not unique to embedded-observer systems; analogous structures appear in dissipative quantum systems and many-body operator dynamics, where they are working analytical tools rather than conjectural propositions.

**Emergent universality classes in dissipative quantum systems.** Zhou et al. [ZhouEtAl2025] develop an effective field theory description for the universal dynamics of dissipative quantum systems with dipole moment conservation, identifying a strongly interacting non-equilibrium fixed point that governs equal-time phase fluctuations. The work is independent of OI but uses the same conceptual apparatus — universality classes characterized by specific structural features (dipole conservation in their case; partial-trace observational features in OI's), with framework-specific content (subdiffusive vs diffusive transport in their case; specific gauge structure in OI's). The existence of working analyses of this kind in active research programs is corroboration that the universality-class framework is a productive analytical tool, not merely a programmatic gesture.

**Random-matrix universality from fast-slow decomposition.** Lunt et al. [Lunt2025] prove the emergence of a universal random-matrix description of fast-mode dynamics in many-body quantum systems, via the memory-function formalism with a careful split into fast and slow modes. The fast-mode universality is direct analog to OI's partial-trace structure: hidden-sector (fast) dynamics produce universal observational features at the visible-sector (slow) level, independent of the specific microscopic content. The result is theorem-level for the random-matrix universality class; the same architecture (fast-slow decomposition producing universality at the slow-mode level) is the architecture OI's framework uses to produce SM-reproducing universality at the visible-sector level.

**Holographic Schwinger-Keldysh as analog of P-indivisibility.** Recent work on holographic Schwinger-Keldysh contours [AmmonEtAl2025], extending earlier work [HolographicSK2024], establishes that the AdS/CFT correspondence prescribes a specific Schwinger-Keldysh contour structure for real-time correlation functions, with non-trivial out-of-time-order four-point functions exploring the full four-fold geometry. §14.3 identifies this as the holographic analog of OI's P-indivisibility — both encoding the non-Markovian marginal structure of partial-trace observation. The recent literature provides concrete prescriptions making the analog precise, supporting the §14.3 transport claim.

### 15.5 Empirical anchors

Direct experimental confirmation applies to the partial-trace-level features identified in §14 (Born rule, channel-level unitarity, non-Markovian marginal) and to the framework's specific predictions developed in [SM], [GR], and [Juno]. The following are the most recent and precise confirmations.

**Born rule precision.** The cleanest test of higher-order interference is the multi-path interferometry experiment of [Sinha2010], which bounded the magnitude of three-path interference to less than $10^{-2}$ of the expected two-path interference, ruling out third- and higher-order interference in optical regimes. The bound was tightened to $10^{-3}$–$10^{-4}$ by [Söllner2012] with detector-nonlinearity calibration. Recent proposals using ultracold-atom interferometry [Kanthak2025] aim for further precision via Bose–Einstein condensate platforms that avoid systematic errors from material slits. The accumulated bound is consistent with the Born rule as a partial-trace-level invariant.

**Non-Markovian dynamics in physical systems.** Direct experimental observation of non-Markovian visible dynamics from hidden slow degrees of freedom: [Mehl2012] in colloidal systems and [Groeblacher2015] in macroscopic micromechanical oscillators. These confirm that the trace-out mechanism is realized in physical systems and that the resulting non-Markovian behavior is operationally accessible. Recent experimental implementations in metrology [QECNonMarkovian2025] demonstrate the same mechanism in quantum-information platforms.

**Cosmological tests of the framework's GR-emergence cluster.** [DESI_DR2_2025] reports rejection of the cosmological constant at 2.8σ–4.2σ depending on the supernovae dataset, with potential phantom crossing at $z \approx 0.5$ and a 2σ+ detection of nonzero neutrino masses in extended-parameter cosmology. The framework's [GR §7] predicts dynamical dark energy in Type II running-vacuum form as a structural prediction; the [Bertini2025] direct fit to DESI DR2 + DES-Y5 + Planck 2018 reports $\nu = -(2.5 \pm 1.3) \times 10^{-4}$, consistent with zero at 2σ and within the framework's structural prediction $|\nu| \sim 10^{-32}$. DESI Year 5 results, expected within the publication horizon, will be discriminating.

**Neutrinoless double-beta decay.** [LEGEND2024] reports LEGEND-200 sensitivity $T_{1/2} > 2.8 \times 10^{26}$ yr at 90% CL on $0\nu\beta\beta$ in $^{76}$Ge (combined with GERDA + Majorana Demonstrator). The framework's [SM §8.4] predicts Majorana neutrinos, so $0\nu\beta\beta$ should be observed; LEGEND-1000 is designed to reach the inverse-ordering range. A positive observation would confirm the framework's neutrino-sector prediction; a null result at LEGEND-1000 sensitivity would constrain the framework. The swampland literature [IbañezMartinLozanoValenzuela2017] independently constrains neutrino-sector parameters via the Weak Gravity Conjecture, providing a cross-validation pathway: the framework's normal-ordering Majorana prediction sits within the WGC-allowed region.

**Black-hole entropy.** GW250114 (LIGO/Virgo/KAGRA, September 2025) confirmed the Bekenstein–Hawking $1/4$ coefficient at $99.999\%$ confidence, as derived in [GR §5]. This is one of the framework's strongest direct empirical confirmations, applying to the cosmological-horizon application of the partial-trace mechanism.

### 15.6 What remains under-supported

Three classes of claims remain without independent support and would benefit from focused future work.

**The universality-class hypothesis qua novel proposal.** The proposal that observationally-equivalent embedded observers form a coarser equivalence than $\mathcal{G}_{\rm sub}$, populated by genuinely different substratum classes, has no direct corroboration in the literature. The closest analog work (§15.4) supports the framework concept but not the specific cross-class population claim. The §10.4 construction of OI's algebra-channel pair, combined with the §11.2 / §13.1.1 four-step recipe applied against a specific string compactification, is the natural pathway to confirmation.

**Per-condition A1–A6 audit for LQG, causal sets, and asymptotic safety** (§13.1.4). Structure's analysis is the only cross-program per-condition comparison of its kind. Independent corroboration would require another author independently performing the analysis and arriving at compatible conclusions. The framework provides specific testable claims — e.g., A2 (determinism) is the most discriminating condition across candidate programs — that can be checked against each program's foundational documents.

**Observer-admission distinction** (§9.6). The structural distinction between observer-admitting and observer-lacking substrata is novel; the closest concept in the literature is anthropic selection (Vilenkin, Tegmark), which is statistical/probabilistic rather than structural. The distinction is not directly testable as stated; its empirical content lies in the predictions it underwrites within the SM-reproducing observer-admitting class, which are tested through the [SM §7] prediction set.

---

## Acknowledgments

This is the fifth core paper of the OI framework, alongside [Main, SM, GR, Substratum]. It consolidates content originally developed across three separate documents: a canonical articulation of the framework's two-dimensional hierarchical structure (now §2), a technical analysis of the OI-string substratum-level relationship (now Part I), and a programmatic framework of universality classes of embedded observers (now Part II), with cross-framework synthesis in Part III. The proposal investigated in Part I was raised in discussion with [collaborator/AI-assisted analysis, depending on author preference]. Errors and speculative content are the author's responsibility.

## References

[Adlam2022] E. Adlam, "Operational Theories as Structural Realism", Studies in History and Philosophy of Science 91, 113-124 (2022). arXiv:2201.09316.

[AlmheiriDongHarlow2014] A. Almheiri, X. Dong, D. Harlow, "Bulk Locality and Quantum Error Correction in AdS/CFT", JHEP 04, 163 (2015). arXiv:1411.7041.

[AmmonEtAl2025] M. Ammon, M. Heller, J. Virrueta et al., "A Holographic prescription for generalized Schwinger-Keldysh contours" (October 2025). arXiv:2510.03404.

[Barandes2023] J. A. Barandes, "The Stochastic-Quantum Correspondence" (2023, revised 2025). arXiv:2302.10778.

[Barandes2025] J. A. Barandes, "Quantum Systems as Indivisible Stochastic Processes" (July 2025). arXiv:2507.21192.

[Barandes2026] J. A. Barandes, "The Stochastic-Quantum Theorem" (February 2026). arXiv:2309.03085.

[Barrett2007] J. Barrett, "Information processing in generalized probabilistic theories", Phys. Rev. A 75, 032304 (2007). arXiv:quant-ph/0508211.

[Bertini2025] M. Bertini et al., "RG-corrected $\Lambda$CDM fit to DESI DR2 + DES-Y5 + Planck 2018" (2025).

[BFSS1996] T. Banks, W. Fischler, S. Shenker, L. Susskind, "M-theory as a Matrix Model: A Conjecture", Phys. Rev. D 55, 5112-5128 (1997). arXiv:hep-th/9610043.

[Brandner2025a] K. Brandner, "Theorem on weak-memory regime for non-Markovian linear dynamics", Phys. Rev. Lett. 134, 037101 (2025); companion Phys. Rev. E 111, 014137 (2025).

[BrandnerMeyer2025] H. Meyer, K. Brandner, "Weak-Memory Dynamics in Discrete Time" (October 2025). arXiv:2510.26325.

[BrunettiFredenhagen2024] D. Buchholz, K. Fredenhagen, "Algebraic Quantum Field Theory: Objectives, Methods, and Results", in *Encyclopedia of Mathematical Physics*, 2nd ed., Elsevier (2024). arXiv:2305.12923.

[DawidFranzmann2025] R. Dawid, G. Franzmann, "Realism and Ontology in Quantum Mechanics and String Theory" (December 2025). arXiv:2512.17124.

[DESI_DR2_2025] DESI Collaboration, "Cosmology in Extended Parameter Space with DESI Data Release 2 Baryon Acoustic Oscillations: A 2σ+ Detection of Nonzero Neutrino Masses" (2025). arXiv:2504.15340.

[GR] A. Maybaum, "General Relativity from the Substratum" (2026).

[Groeblacher2015] S. Gröblacher et al., "Observation of non-Markovian micromechanical Brownian motion", Nature Communications 6, 7606 (2015).

[Hardy2001] L. Hardy, "Quantum Theory From Five Reasonable Axioms", arXiv:quant-ph/0101012 (2001).

[HarlowBulkReconstruction2018] D. Harlow, "TASI Lectures on the Emergence of Bulk Physics in AdS/CFT", PoS TASI2017, 002 (2018). arXiv:1802.01040.

[HigherPointBFSS2025] A. Biggs, A. Herderschee, "Higher-point correlators in the BFSS matrix model" (2025). arXiv:2503.14685.

[HolographicSK2024] Y. Bu et al., "Holographic Schwinger-Keldysh field theory of SU(2) diffusion" (2024). arXiv:2205.00195.

[IbañezMartinLozanoValenzuela2017] L. E. Ibáñez, V. Martin-Lozano, I. Valenzuela, "Constraining Neutrino Masses, the Cosmological Constant and BSM Physics from the Weak Gravity Conjecture", JHEP 11, 066 (2017). arXiv:1706.05392.

[IKKT1996] N. Ishibashi, H. Kawai, Y. Kitazawa, A. Tsuchiya, "A Large-N Reduced Model as Superstring", Nucl. Phys. B 498, 467-491 (1997). arXiv:hep-th/9612115.

[Kanthak2025] S. Kanthak, J. Pahl, D. Reiche, M. Krutzik, "Proposal for a Bose–Einstein Condensate Based Test of Born's Rule Using Light–Pulse Atom Interferometry", Advanced Quantum Technologies 8, 2400436 (2025).

[LabuschagneMajewski2025] L. E. Labuschagne, W. A. Majewski, "A Von Neumann Algebraic Approach to Quantum Theory on Curved Spacetime" (August 2025). arXiv:2503.14107.

[LEGEND2024] R. Brugnera (LEGEND collaboration), "Neutrinoless double-beta decay search with the LEGEND experiment" (2024). arXiv:2501.10046.

[Lehnert2025] K. Lehnert, "Hitchhiker's Guide to the Swampland" (2025). arXiv:2509.02632.

[Lunt2025] O. Lunt et al., "Emergent random matrix universality in quantum operator dynamics" (April 2025). arXiv:2504.18311.

[Mackey1963] G. W. Mackey, *Mathematical Foundations of Quantum Mechanics* (Benjamin, 1963).

[Main] A. Maybaum, "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation" (2026).

[Maldacena1997] J. Maldacena, "The Large N Limit of Superconformal Field Theories and Supergravity", Adv. Theor. Math. Phys. 2, 231-252 (1998). arXiv:hep-th/9711200.

[Mehl2012] J. Mehl, B. Lander, C. Bechinger, V. Blickle, U. Seifert, "Role of hidden slow degrees of freedom in the fluctuation theorem", Phys. Rev. Lett. 108, 220601 (2012).

[MSW2024] F. Marchesano, G. Shiu, T. Weigand, "The Standard Model from String Theory: What Have We Learned?", Annual Review of Nuclear and Particle Science 74, 113-140 (2024). arXiv:2401.01939.

[OoguriVafa2007] H. Ooguri, C. Vafa, "On the Geometry of the String Landscape and the Swampland", Nucl. Phys. B 766, 21-33 (2007). arXiv:hep-th/0605264.

[Palti2019] E. Palti, "The Swampland: Introduction and Review", Fortsch. Phys. 67, 1900037 (2019). arXiv:1903.06239.

[QECNonMarkovian2025] "Quantum Error-Corrected Non-Markovian Metrology", PRX Quantum (August 2025). DOI: 10.1103/wfyl-wtz3.

[RandomStinespring2025] "Random Stinespring superchannel: converting channel queries into dilation isometry queries" (December 2025). arXiv:2512.20599.

[Sinha2010] U. Sinha, C. Couteau, T. Jennewein, R. Laflamme, G. Weihs, "Ruling Out Multi-Order Interference in Quantum Mechanics", Science 329, 418-421 (2010).

[SM] A. Maybaum, "The Standard Model from a Cubic Lattice" (2026).

[Söllner2012] I. Söllner, B. Gschösser, P. Mai, B. Pressl, Z. Vörös, G. Weihs, "Testing Born's Rule in Quantum Mechanics for Three Mutually Exclusive Events", Foundations of Physics 42, 742-751 (2012). arXiv:1201.0195.

[Stinespring1955] W. F. Stinespring, "Positive functions on C*-algebras", Proceedings of the American Mathematical Society 6, 211-216 (1955).

[StromingerVafa1996] A. Strominger, C. Vafa, "Microscopic Origin of the Bekenstein-Hawking Entropy", Phys. Lett. B 379, 99-104 (1996). arXiv:hep-th/9601029.

[Substratum] A. Maybaum, "The Substratum Construction: Reconstruction, the Substratum Gauge Group, and the QM-GR Synthesis" (2026). Zenodo DOI 10.5281/zenodo.19060318.

[Susskind2003] L. Susskind, "The Anthropic Landscape of String Theory", arXiv:hep-th/0302219 (2003).

[TomizukaTakeda2026] R. Tomizuka, T. Takeda, "Emergence of Non-Markovian Classical-Quantum Dynamics from Decoherence" (April 2026). arXiv:2604.06891.

[Vafa2005] C. Vafa, "The String Landscape and the Swampland", arXiv:hep-th/0509212 (2005).

[Yngvason2005] J. Yngvason, "The role of type III factors in quantum field theory", Reports on Mathematical Physics 55, 135-147 (2005). arXiv:math-ph/0411058.

[ZhouEtAl2025] W. Zhou et al., "Emergent Universality Class in Dissipative Quantum Systems with Dipole Moment Conservation" (December 2025). arXiv:2512.17210.

[HolographicNonHydro2024] Y. Liu, Y.-W. Sun, X.-M. Wu, "Holographic Schwinger-Keldysh effective field theories including a non-hydrodynamic mode", arXiv:2411.16306 (2024).

[TensorNetworkMatrix2024] [tensor-network reformulations of matrix models], arXiv:2412.04133 (2024).

[Loll2019] R. Loll, "Quantum Gravity from Causal Dynamical Triangulations: A Review", Class. Quant. Grav. 37, 013002 (2020). arXiv:1905.08669.

[Rovelli2004] C. Rovelli, "Quantum Gravity", Cambridge University Press (2004).

[AshtekarLewandowski2004] A. Ashtekar, J. Lewandowski, "Background Independent Quantum Gravity: A Status Report", Class. Quant. Grav. 21, R53 (2004). arXiv:gr-qc/0404018.

[BombelliLeeMeyerSorkin1987] L. Bombelli, J. Lee, D. Meyer, R. Sorkin, "Space-Time as a Causal Set", Phys. Rev. Lett. 59, 521 (1987).

[RideoutSorkin1999] D. P. Rideout, R. D. Sorkin, "A Classical Sequential Growth Dynamics for Causal Sets", Phys. Rev. D 61, 024002 (2000). arXiv:gr-qc/9904062.

[Surya2019] S. Surya, "The Causal Set Approach to Quantum Gravity", Living Rev. Rel. 22, 5 (2019). arXiv:1903.11544.

[Weinberg1979] S. Weinberg, "Ultraviolet Divergences in Quantum Theories of Gravitation", in *General Relativity: An Einstein Centenary Survey*, eds. S. W. Hawking, W. Israel, Cambridge University Press (1979), 790-831.

[Reuter1998] M. Reuter, "Nonperturbative evolution equation for quantum gravity", Phys. Rev. D 57, 971 (1998). arXiv:hep-th/9605030.

[Eichhorn2018] A. Eichhorn, "An asymptotically safe guide to quantum gravity and matter", Front. Astron. Space Sci. 5, 47 (2019). arXiv:1810.07615.
