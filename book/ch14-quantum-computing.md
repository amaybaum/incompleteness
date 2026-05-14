# Chapter 14
# Quantum Computing

*Source: framework repo `BQP.md` (BQP characterization theorem, Extended Church-Turing Thesis as theorem, BPP-BQP gap). Chapter draft v0.1 (Pass 1 of 1).*

---

## 14.1 What this chapter develops

The framework's content across Chapters 5 through 13 has established a substantial structural account of fundamental physics, the cascade through chemistry and biology, and the specific empirical content of quantum biology. The cascade's logic — substratum, partition, emergent quantum mechanics, structural conditions C1-C3 producing non-Markovian dynamics at multiple scales — provides the foundation for the framework's content in computational complexity theory.

This chapter develops the framework's characterization of computational power available to embedded observers. The central result is the *BQP characterization theorem*: BQP (bounded-error quantum polynomial time) is the unique computational class accessible to any finite deterministic system satisfying the framework's structural conditions C1-C3. The theorem has two directions. The *lower bound* establishes that any embedded observer satisfying C1-C3 has access to BQP computational resources — the emergent quantum mechanics provides state preparation, a universal gate set, and Born-rule measurement, the full toolkit for BQP computation. The *upper bound* establishes that no embedded observer exceeds BQP — the quantum description is informationally complete for the embedded observer, with no operation on the visible sector extracting information beyond the quantum state.

Eight pieces occupy the chapter.

Section 14.2 develops the chapter's framing: the framework's content in computational complexity is at the foundational level rather than the algorithm-design level. The framework does not produce new quantum algorithms; it characterizes the *ceiling* on what embedded observers can compute. Section 14.3 develops the lower bound: BQP is available to any embedded observer satisfying C1-C3. The argument runs through the framework's emergent quantum mechanics from Chapter 1, with state preparation, gate application, and measurement all derivable from the framework's structural conditions.

Section 14.4 develops the upper bound: BQP cannot be exceeded. The argument runs through the framework's informational completeness — the quantum description exhausts the information accessible to the embedded observer through any operation on the visible sector, so no super-BQP computation is possible. Section 14.5 combines the two bounds into the BQP characterization theorem: BQP is the unique computational class accessible to embedded observers satisfying C1-C3.

Section 14.6 develops the Extended Church-Turing Thesis (ECT) as a *theorem* of the framework. The ECT — that any physically realizable computation can be efficiently simulated by a quantum computer — is conventionally treated as an empirical conjecture about physical reality. The framework's content reframes the ECT as a derived result: every physical observer is embedded (the cosmological horizon provides the partition), every embedded observer has access to BQP and nothing beyond, therefore every physical computation is in BQP. The reframing changes the ECT's epistemic status from conjecture to theorem.

Section 14.7 develops the BPP-BQP gap: quantum advantage is real but is *a feature of partial observation* rather than of the universe being fundamentally quantum. An embedded observer who ignores the quantum structure of the reduced description (treating measurements as classical samples) operates at BPP; one who exploits the quantum structure (interference, entanglement, adaptive measurement) operates at BQP. The gap between the two is the cost of not recognizing the partition's structure. Section 14.8 develops the chapter's falsification conditions and connections to broader complexity theory, with closing forward pointers to Chapter 15's engineering content and Chapter 18's foundational content.

The chapter's content is foundational rather than algorithmic. The framework's contribution to quantum computing is structural: a characterization of the computational ceiling that emerges from the framework's commitments at the substratum level, with the BQP class identified as the unique class accessible to embedded observers. The empirical content is principally negative: the framework predicts that no super-BQP computation is possible on any physically realizable hardware, with any demonstrated super-BQP capability constituting a falsification of the framework.

## 14.2 The framework's content in computational complexity

The framework's content in computational complexity operates at a specific level of abstraction. The framework does *not* derive new quantum algorithms — Shor's factoring algorithm, Grover's search algorithm, the HHL linear-system algorithm, and other specific quantum computational achievements are not framework results but standard quantum-computing content that the framework's emergent quantum mechanics reproduces. What the framework adds is a structural account of *why* BQP is the relevant complexity class for quantum computing — why this specific class of problems is the one accessible to embedded observers using quantum-mechanical computation.

**The conventional treatment.** Standard quantum complexity theory establishes BQP as a complexity class with specific defining properties: polynomial-time computation on a quantum Turing machine with bounded error. BQP contains BPP (bounded-error probabilistic polynomial time, the classical analog) and is conjectured to extend beyond it (Shor's algorithm being the canonical example of BQP computation believed not to be in BPP). The relationship of BQP to other complexity classes — its relationship to NP, PH, PSPACE, and others — is the subject of active research.

The conventional treatment takes BQP as defined by the quantum-computing model and asks empirical questions: what problems are in BQP? what are the boundaries of BQP relative to other classes? what specific algorithms achieve BQP computation? The framework's content addresses a different question, one level below: *why* is BQP the relevant class for quantum computing in our physical universe?

**The framework's level.** The framework's content treats BQP as a *derived* feature of physical reality rather than as a primitive defined by the quantum-computing model. The derivation runs through the framework's structural commitments: any embedded observer in a finite deterministic substratum satisfying C1-C3 has access to BQP computational resources, and no embedded observer exceeds BQP. The BQP class is therefore *the unique class accessible to embedded observers* — a structural feature of the framework's universality class rather than an empirical property of specific computational architectures.

This is a different epistemic status than the conventional treatment. In the conventional treatment, BQP is a *useful concept* for organizing computational results, with its empirical applicability being a contingent feature of our physical universe. In the framework's content, BQP is a *structural inevitability* — any physical universe with the framework's commitments has BQP as the unique computational ceiling for embedded observers.

**Why this matters.** The framework's level matters for two reasons.

*The ceiling is principled rather than empirical.* The conventional treatment leaves open the possibility that some future physical principle could extend computational access beyond BQP. The framework's content closes this possibility: super-BQP computation would require an embedded observer to exceed the structural limits the framework identifies, which is mathematically impossible if the framework's commitments are correct. The ceiling is a theorem, not an empirical bound.

*The falsification condition is sharp.* The conventional treatment makes no specific predictions about whether super-BQP computation is possible — it remains an open question subject to future discovery. The framework's content predicts that no super-BQP computation is possible on any physically realizable hardware, with any demonstrated super-BQP capability constituting a falsification. The falsification condition is empirically actionable: future quantum computing experiments could in principle test the framework's prediction.

The framework's content in this chapter is therefore at a foundational level — a structural account of why BQP is the relevant complexity class, with empirical predictions that distinguish the framework from alternative accounts of computational complexity in physical systems.

## 14.3 BQP is available: the lower bound

The lower bound of the BQP characterization theorem establishes that any embedded observer satisfying C1-C3 has access to BQP computational resources. The argument runs through the framework's emergent quantum mechanics from Chapter 1: the observer's reduced description is quantum-mechanical, and the standard quantum-computing toolkit (state preparation, universal gate set, Born-rule measurement) is available to the observer through standard operations on the visible sector.

**The observer's quantum toolkit.** Chapter 1 derived the framework's emergent quantum mechanics for any embedded observer satisfying C1-C3. The derivation produces the standard quantum-mechanical formalism: a Hilbert space of visible-sector states, unitary evolution under the reduced Hamiltonian, projective measurement following the Born rule, and the standard composition rules for combining subsystems. These features are present in the observer's reduced description by structural necessity — they follow from C1-C3 without additional assumptions.

The standard quantum-computing toolkit is built on exactly these features. *State preparation* (producing a specific quantum state for computation) corresponds to projective measurement followed by post-selection — operations the observer has access to as part of the emergent quantum mechanics. *Gate application* (transforming the quantum state through unitary operations) corresponds to time evolution under controllable Hamiltonians — available wherever the observer can engineer the visible sector's dynamics. *Measurement* (reading the computation's output) corresponds to standard projective measurement — the framework's fundamental observational operation.

**Universal gate set.** Quantum computing requires a universal gate set: a collection of single-qubit and two-qubit gates that can approximate any unitary transformation to arbitrary precision. The standard universal gate set includes the Hadamard gate, the phase gate, and the CNOT (controlled-NOT) gate, with these three gates generating the full unitary group through composition. Each of these gates is implementable in any system with controllable two-level subsystems and a tunable coupling — features that the framework's emergent quantum mechanics provides for any embedded observer with sufficient experimental control.

The argument is concrete: an observer who can prepare two-level subsystems (qubits) in the visible sector, who can apply controllable Hamiltonians to those subsystems, and who can perform projective measurements on the subsystems has access to a universal gate set. These three capabilities follow from the framework's emergent quantum mechanics without additional structural assumptions. Any embedded observer satisfying C1-C3 therefore has access to universal quantum computation in principle.

**Error correction.** Practical BQP computation requires fault tolerance: the ability to perform long computations despite physical errors at each gate. Quantum error correction (surface codes, stabilizer codes, topological codes) provides the theoretical framework for fault tolerance with overhead scaling logarithmically in the desired computational accuracy. The framework's emergent quantum mechanics provides the structural foundation: error correction operates on the quantum information in the visible sector, with redundant encoding protecting against local errors.

The framework's content here is consistent with standard quantum-computing theory: error correction is structurally available to any embedded observer with sufficient control over the visible sector, with the specific overhead determined by the physical error rates (which depend on the framework's specific physical parameters rather than on structural commitments at the framework level). Chapter 15 develops the framework's content on engineered error correction with correlation-aware decoders that exploit the framework's predicted non-Markovian noise structure.

**The lower bound theorem.** Combining the four elements — state preparation, universal gate set, measurement, error correction — establishes the lower bound:

*Lower Bound Theorem.* Any embedded observer satisfying C1-C3 has access to BQP computational resources. The emergent quantum mechanics provides state preparation, a universal gate set, and Born-rule measurement; error correction is structurally available; the cumulative result is access to polynomial-time quantum computation with bounded error.

The lower bound is therefore established structurally: BQP is not a contingent capability that some embedded observers happen to have but a *universal* capability of all embedded observers satisfying C1-C3. This is a structural feature of the framework's universality class — any member of the class has access to BQP.

## 14.4 BQP cannot be exceeded: the upper bound

The upper bound of the BQP characterization theorem establishes that no embedded observer exceeds BQP. The argument runs through *informational completeness*: the quantum description exhausts the information accessible to the embedded observer through any operation on the visible sector. No further computational capability is available, because there is no additional information for further computation to access.

**Informational completeness of the quantum description.** The framework's emergent quantum mechanics from Chapter 1 has a specific structural property: the density matrix $\rho_V$ describing the visible sector contains *all* the information accessible to the embedded observer about the visible sector's state. Any operation the observer performs on the visible sector — measurement, transformation, post-selection — operates on the density matrix and produces outcomes consistent with the density matrix's statistical predictions.

There is no additional information for the observer to access. The hidden sector's specific state is structurally inaccessible to the embedded observer (Chapter 1 §1.4); the observer can detect the *statistical* effect of the hidden sector through the density matrix's mixedness but cannot detect the specific hidden-sector configuration. Any computational capability beyond what the density matrix supports would require the observer to access hidden-sector information that the framework's structural commitments make inaccessible.

**All observer operations are quantum operations.** The framework's content includes a more specific structural claim: any operation an embedded observer can perform on the visible sector is a *quantum operation* in the standard sense — a completely positive trace-preserving (CPTP) map on the density matrix $\rho_V$. This includes unitary evolution (a special case of CPTP map preserving purity), projective measurement (CPTP maps with specific structure), post-selection (non-CPTP but reduces to CPTP through normalization), and any combination of these.

The argument runs as follows. The embedded observer's operations are implemented through interactions between the observer's measurement apparatus and the visible sector. The apparatus itself is part of the visible sector (it is composed of visible-sector degrees of freedom). Any operation the apparatus performs is therefore a unitary evolution of the joint apparatus-system Hilbert space followed by projective measurement of the apparatus state. By the standard derivation of CPTP maps from such constructions, every operation the observer can perform on the visible sector is a CPTP map.

**Computational complexity of CPTP maps.** The computational complexity of CPTP maps is well-characterized in quantum complexity theory: any CPTP map on $n$ qubits can be implemented by a polynomial-size quantum circuit (a sequence of polynomial many gates from a universal gate set). Conversely, any polynomial-size quantum circuit implements a CPTP map. The class of efficiently-implementable CPTP maps coincides with BQP up to the standard polynomial encoding.

The framework's content therefore identifies BQP with the class of operations available to embedded observers. The observer cannot perform any operation that is not a CPTP map (because all observer operations are CPTP maps), and the class of efficiently-computable CPTP maps is BQP. Therefore the observer cannot perform any computation outside BQP.

**The upper bound theorem.**

*Upper Bound Theorem.* No embedded observer satisfying C1-C3 can perform computation outside BQP. Every observer operation is a CPTP map on the density matrix; the class of efficiently-implementable CPTP maps is BQP; therefore the class of efficient computations available to the observer is BQP.

**Addressing objections.** Three potential objections to the upper bound are worth addressing.

*"What about hypercomputation?"* Hypercomputation refers to computational models that exceed Turing-machine capabilities — infinite-time computation, oracle access to undecidable problems, analog computation with arbitrary-precision continuous quantities. The framework's content addresses each: infinite-time computation requires actual infinity (which the framework's finite substratum precludes), oracle access requires hidden-sector information the observer cannot extract, and arbitrary-precision continuous computation requires sub-Planck-scale resolution that the framework's lattice precludes. Hypercomputation is structurally impossible for embedded observers.

*"What about exotic physics?"* Various proposed exotic physics scenarios — closed timelike curves, naked singularities, quantum gravity effects — have been suggested as potential routes to super-BQP computation. The framework's content provides specific responses: closed timelike curves are inconsistent with the framework's deterministic substratum dynamics; naked singularities are excluded by the framework's bounded-coupling-degree commitment; quantum gravity effects operate at the substratum level rather than the emergent level and therefore cannot enhance computational power for embedded observers. Each exotic-physics route is closed by the framework's structural commitments.

*"What about future discoveries?"* The framework's content does not preclude future discoveries that revise our understanding of physical reality. What it does preclude is super-BQP computation *consistent with the framework's commitments*. A future discovery that demonstrated super-BQP computation would constitute a falsification of the framework — it would require the universe to violate the framework's structural conditions C1-C3 or one of the framework's other commitments. The framework therefore makes a sharp empirical prediction: no super-BQP computation is possible on any physically realizable hardware compatible with the framework's commitments.

## 14.5 The BQP characterization theorem

Combining the lower bound (BQP is available, §14.3) with the upper bound (BQP cannot be exceeded, §14.4) yields the BQP characterization theorem.

**Statement.** *BQP Characterization Theorem.* Let $\mathcal{S} = (S, \varphi)$ be a finite deterministic system, and let $\mathcal{O}$ be an embedded observer with partition $V$ satisfying C1, C2, C3 at the partition boundary. Then the class of computations the observer can efficiently perform (in polynomial time with bounded error) is exactly BQP.

**Proof outline.** The lower bound from §14.3 establishes that BQP is available to the observer. The upper bound from §14.4 establishes that BQP cannot be exceeded. Therefore the class of efficient computations available to the observer is exactly BQP.

The proof relies on the framework's structural commitments at multiple points:
- The framework's finite substratum guarantees finite-dimensional emergent Hilbert spaces.
- The framework's deterministic bijection $\varphi$ guarantees unitarity at the substratum level.
- The framework's structural conditions C1-C3 guarantee the emergent quantum-mechanical description.
- The framework's partition structure guarantees informational completeness of the density matrix.

Each of these is a structural feature of the framework's universality class; together they produce the BQP characterization as a theorem.

**Interpretation.** The characterization theorem has several interpretive consequences.

*BQP is the universal computational class.* For any universe in the framework's universality class, BQP is the relevant computational complexity class for embedded observers. The specific physical implementation of the computational hardware does not matter — superconducting qubits, trapped ions, topological qubits, photonic systems, neutral atoms, or any other platform — all have access to BQP and only BQP.

*BQP is independent of the specific bijection.* The framework's universality class contains many bijections producing different specific physical content (different particle spectra, different gauge groups, different specific parameter values). Among the bijections within the framework's universality class, however, the computational ceiling is the same: BQP. The characterization is at the framework level rather than the specific-bijection level.

*BQP is the ceiling for any future technology.* No future technological development — better qubits, better error correction, exotic computational substrates — can exceed BQP for embedded observers in the framework's universality class. The ceiling is structural rather than technological.

The characterization theorem is therefore a substantial result: it establishes BQP as the unique computational class accessible to embedded observers, with the result holding at the structural level of the framework's universality-class commitments rather than at the specific-implementation level.

## 14.6 The Extended Church-Turing Thesis as a theorem

The Extended Church-Turing Thesis (ECT) asserts that any physically realizable computation can be efficiently simulated by a quantum Turing machine. Conventionally, the ECT is treated as an *empirical conjecture* about physical reality: the conjecture is not derived from any deeper principle but is supported by the absence of known super-BQP computations and by general considerations about the structure of physical theories. The conjecture's empirical status leaves open the possibility that future discoveries could refute it by demonstrating super-BQP computation in some physical system.

The framework's content reframes the ECT from empirical conjecture to *theorem*.

**The framework's argument.** The reframing runs through three steps.

*Step 1: Every physical observer is embedded.* The cosmological horizon provides a partition for any observer in the universe — the partition between the observable universe (visible to the observer in principle, given sufficient instruments) and the trans-horizon region (causally disconnected from the observer). The observer is therefore embedded in the framework's structural sense: the partition with C1-C3 structure exists for any observer in the universe.

*Step 2: Every embedded observer has access to BQP and only BQP.* This is the BQP characterization theorem from §14.5. Any observer satisfying C1-C3 has access to BQP computational resources (the lower bound) and cannot exceed BQP (the upper bound). The computational class accessible to the observer is exactly BQP.

*Step 3: Every physical computation is in BQP.* Combining the previous two steps: every physical computation is performed by some physical observer or apparatus, every physical observer or apparatus is embedded in the framework's structural sense, every embedded observer can compute only in BQP. Therefore every physical computation is in BQP.

The ECT is therefore not an empirical conjecture but a *theorem* of the framework — a derived consequence of the framework's structural commitments. The reframing changes the ECT's epistemic status fundamentally: the question "is the ECT correct?" becomes "are the framework's structural commitments correct?", which is testable through the framework's other empirical content (Chapters 5-13).

**Implications of the reframing.**

*Sharper predictions.* The reframing produces sharper empirical predictions. Any demonstrated super-BQP computation would constitute a falsification of the framework — the universe would not be in the framework's universality class, which would falsify the framework's structural commitments at the foundational level. This is a stronger prediction than the conventional ECT, which allows the possibility of future revisions without committing to a specific structural commitment.

*Structural foundations.* The reframing provides structural foundations for the ECT that were previously absent. The ECT's empirical status conventional treatment provides no explanation for *why* the ECT should hold — it remains an unexplained regularity of physical reality. The framework's content provides the explanation: the ECT holds because every physical observer is embedded, every embedded observer has access to BQP and only BQP, therefore every physical computation is in BQP. The structural basis is the framework's universality-class commitments.

*Connection to other foundational results.* The reframing connects the ECT to other foundational results in the framework. The Bekenstein-Hawking entropy bound (Chapter 7 §7.5) limits the information content of any region; the BQP characterization limits the computational power of any embedded observer; both follow from the framework's commitments at the substratum level. The connection unifies the information-theoretic and computational bounds under a common structural framework.

The framework's reframing of the ECT is therefore not a minor terminological change but a substantive theoretical contribution. The ECT moves from empirical conjecture to derived theorem, with the framework's other empirical content (Chapters 5-13) providing the supporting evidence for the framework's structural commitments that make the theorem follow.

## 14.7 The BPP-BQP gap as cost of partial observation

Quantum advantage — the gap between classical (BPP) and quantum (BQP) computational complexity — is one of the central topics in quantum complexity theory. The framework's content provides a structural reading: the BPP-BQP gap is the *cost of not recognizing the quantum nature of the reduced description*. An embedded observer who treats the visible sector classically (sampling measurement outcomes according to classical probabilities) operates at BPP; an observer who exploits the quantum structure (interference, entanglement, adaptive measurement) operates at BQP. The gap between the two is the cost of partial observation interpreted classically.

**The gap is real.** Standard quantum complexity theory establishes that BQP contains problems believed not to be in BPP — Shor's factoring algorithm being the canonical example. Whether $\text{BPP} \subsetneq \text{BQP}$ strictly is an open problem in complexity theory; the standard conjecture is that the strict inclusion holds, with super-polynomial separations like Shor's algorithm providing strong evidence. The framework's content does not address whether the strict inclusion holds — that is a question about the structure of BQP and BPP as complexity classes, addressed by standard quantum complexity theory.

**The gap's structural origin.** What the framework adds is a *structural* account of the gap's origin. The embedded observer's reduced description is quantum-mechanical (Chapter 1). An observer who *recognizes* the quantum-mechanical structure of the reduced description can perform quantum computation, exploiting interference, entanglement, and measurement back-action. An observer who *does not recognize* the quantum-mechanical structure — who treats the reduced description as classical with stochastic measurement outcomes — operates with reduced computational capability.

The gap between BPP and BQP is therefore not a property of physical reality per se but of the *observer's representation of physical reality*. An observer using the correct quantum-mechanical description has access to BQP; an observer using an incorrect classical-stochastic description has access only to BPP. The framework's content reframes quantum advantage as a *epistemic gap* between two descriptions of the same physical reality.

**The framework's reading vs the "quantum nature of reality" reading.** A common interpretive position is that quantum advantage demonstrates "the fundamentally quantum nature of physical reality" — that physical reality is quantum-mechanical at the substratum level, with classical computation being a restricted special case. The framework's content rejects this interpretive position. Under the framework's reading, physical reality is *deterministic and classical* at the substratum level (the bijection $\varphi$ acts on a finite state space with classical probability for the observer's outcomes), with quantum mechanics being the *emergent* description that embedded observers use.

The BPP-BQP gap is therefore not evidence that physical reality is fundamentally quantum but evidence that *embedded observers in classical substrata have access to quantum-mechanical resources through the partition structure*. The quantum advantage is real but is a feature of the observer's situation (embedded in a substratum with C1-C3 structure) rather than of the substratum's fundamental nature.

This reading has substantive consequences for foundational questions. The framework's content is compatible with classical substrate metaphysics — the universe is a deterministic finite system at the substratum level — while preserving the empirical content of quantum mechanics and quantum computing. The framework is not "quantum mechanics is wrong" but "quantum mechanics is the correct description of what embedded observers see in classical substrata."

**Implications for quantum-computing development.** The framework's reading has practical consequences for quantum-computing engineering. If quantum advantage reflects the observer's exploitation of partition structure rather than fundamentally quantum reality, then quantum-computing hardware should be designed to optimize the partition's properties — making the framework's C1-C3 architecture explicit and tunable rather than treating the environment as noise to be minimized. Chapter 15 develops this design philosophy in detail.

## 14.8 Chapter close

The framework's content in this chapter establishes BQP as the unique computational class accessible to embedded observers in the framework's universality class. The characterization theorem combines a lower bound (BQP is available to any embedded observer satisfying C1-C3) with an upper bound (BQP cannot be exceeded by any embedded observer), with the combination producing BQP as the exact ceiling on computational capability.

**Three principal results.**

*The BQP characterization theorem* (§14.5): BQP is the unique computational class accessible to embedded observers satisfying C1-C3.

*The Extended Church-Turing Thesis as theorem* (§14.6): every physical computation is in BQP, derived from the embedding and BQP characterization rather than postulated as an empirical conjecture.

*The BPP-BQP gap as cost of partial observation* (§14.7): quantum advantage is real but reflects the embedded observer's exploitation of partition structure rather than the universe's fundamentally quantum nature.

**Falsification conditions.** The framework's content makes specific falsifiable predictions:

*Any demonstrated super-BQP computation on physically realizable hardware would falsify the framework.* The framework's structural commitments preclude super-BQP computation; any empirical demonstration of such capability would refute the framework at the foundational level.

*Hypercomputation is structurally impossible.* The framework's finite substratum and bounded-coupling-degree commitments preclude hypercomputation in any form (infinite-time, oracle-based, arbitrary-precision-continuous). Any apparent demonstration of hypercomputation would either be reducible to standard computation or constitute a falsification.

*The BQP ceiling applies to all future technology.* No improvement in quantum-computing technology — better qubits, better error correction, exotic architectures — can exceed BQP. The ceiling is structural rather than technological. The framework therefore predicts a specific limit on future quantum-computing capability.

**Forward pointers.** Chapter 15 develops the framework's content in quantum engineering: the practical implementation of quantum computing in superconducting-qubit systems, the framework's predicted non-Markovian noise structure, correlation-aware error correction with $3$-$10\times$ overhead reduction, coherence extension with engineered baths, and the BEC analogue-gravity experiment as a foundational test of the BQP characterization theorem. The empirical content develops in the engineering direction; the structural foundations are in this chapter.

Chapter 18 §§18.2-18.4 developed the foundational content connecting the framework's emergent quantum mechanics to the BQP computational ceiling. The Born rule as dynamical equilibrium, the quantum-classical boundary, and the epistemic character of quantum randomness — these foundational topics provide the substratum-level context for the BQP characterization theorem. Together with the chapter's content, they constitute the framework's complete account of computational complexity for embedded observers: a structural ceiling at BQP with the foundational basis in the framework's emergent quantum mechanics.

The chapter's content is therefore the framework's positive contribution to computational complexity theory: a structural characterization of BQP as the unique class accessible to embedded observers, with the ECT reframed from empirical conjecture to theorem and the BPP-BQP gap interpreted as the cost of partial observation. The framework's empirical exposure in computational complexity is principally negative — the prediction of no super-BQP computation provides a sharp falsification target — but the structural content is substantial.

---
