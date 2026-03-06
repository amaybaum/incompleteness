# THE UNDECIDABILITY OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

An observer embedded in a deterministic system, whose dynamics are partitioned into a visible sector and a slowly coupled hidden sector of sufficient capacity, necessarily describes the visible sector using quantum mechanics — provided the effective configuration space is finite-dimensional, a condition that in the cosmological application follows from the partition geometry itself. The hidden sector's persistent correlations render the visible-sector stochastic process P-indivisible; by Barandes' stochastic-quantum correspondence, this is mathematically equivalent to unitarily evolving quantum mechanics. The Schrödinger equation, the Born rule, and Bell inequality violations emerge as structural consequences. The action scale $\hbar$ is uniquely determined by the local structural properties of the partition boundary. No quantum postulates are assumed.

The cosmological horizon provides a physical realization of the theorem's conditions. Applying the framework to de Sitter spacetime, the value $\hbar = c^3 \epsilon^2 / (4G)$ follows from partition-relativity, dimensional analysis, and thermal self-consistency — requiring the emergent Gibbons-Hawking temperature to match the classical horizon temperature — with $\epsilon = 2\,l_p$ fixed exactly. The Bekenstein-Hawking entropy formula $S = A/(4\,l_p^2)$ is recovered as a consequence. The framework dissolves the cosmological constant problem: the $10^{122}$ discrepancy equals $S_{\text{dS}}$, the information compression ratio of the emergent quantum description — a category error, not a fine-tuning failure.

Falsifiable predictions include dark energy evolution in Running Vacuum Model form ($\Lambda_{\text{eff}} = \Lambda_0 + \nu H^2$) and gravitational wave echoes near black hole horizons. No competing framework predicts both.

---

# PART I: THE GENERAL THEOREM

## 1. INTRODUCTION

### 1.1 The Problem of Embedded Observation

Physical observers are subsystems of the systems they measure. This elementary fact has consequences that have not been traced. An observer embedded in a deterministic universe cannot access the complete state: degrees of freedom beyond the observer's causal reach are permanently hidden, and the observer's description of the visible sector is necessarily a reduced one obtained by marginalizing over the hidden sector. The question is what structural constraints that reduction imposes on the form of the observer's physical laws.

The observer's epistemic situation has been foregrounded before. QBism treats quantum states as expressions of an agent's beliefs; relational quantum mechanics defines states relative to interacting subsystems; 't Hooft's cellular automaton interpretation [1] derives quantum behavior from deterministic dynamics through information loss. These programs take observer-dependence as an interpretive starting point or, in 't Hooft's case, derive it from a specific microphysical model. The present framework differs in that it identifies *sufficient conditions* under which any embedded observer in any deterministic system necessarily sees quantum mechanics, independent of the system's specific physical content.

### 1.2 Axioms

The framework rests on three axioms. None reference quantum mechanics, general relativity, or any specific physical theory.

1. **Deterministic dynamics.** The total system evolves deterministically on a phase space $\Gamma$. The phase-space density $\rho(q, p, t)$ evolves via the Liouville equation:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\} \equiv \mathcal{L}\rho$$

where $\mathcal{L}$ is the Liouville operator and $\{\cdot, \cdot\}$ denotes the Poisson bracket.

**Finiteness condition.** The effective configuration space of the visible sector is finite-dimensional. A discreteness scale $\epsilon$ provides a finite minimal cell volume, ensuring that any finite spatial region contains at most a finite number of independent cells. In Part I, $\epsilon$ is a free parameter; its value is determined *a posteriori* by self-consistency (§6), which pins $\epsilon = 2\,l_p$ exactly. In Part II, the finiteness condition is not an additional assumption but a consequence of the partition geometry: the cosmological horizon has finite area $A = 4\pi c^2/H^2$ (from GR alone), and the number of modes that couple through a finite-area boundary is $A/\epsilon^2$, which is finite for any $\epsilon > 0$. The stochastic process that the trace-out generates therefore lives on a finite-dimensional space regardless of whether the total phase space extends infinitely beyond the horizon. This condition enters the proof at a single point: the stochastic-quantum correspondence (§3.1), which requires a finite configuration space. Independent support comes from holographic arguments that the Hilbert space of quantum gravity is locally finite-dimensional [27].

2. **Causal partition.** $\Gamma$ is partitioned into a visible sector $\Gamma_V$ accessible to the observer and a hidden sector $\Gamma_H$ that is not:

$$\Gamma = \Gamma_V \times \Gamma_H$$

The partition is fixed on timescales relevant to the observer (it may drift on much longer timescales, but such drift is not required for the theorem). The total Hamiltonian decomposes as:

$$H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

The product decomposition $\Gamma_V \times \Gamma_H$ is a simplification. A real observer's epistemic access is graded: some degrees of freedom are measured precisely, others poorly, and others not at all. The axiom requires that this graded access be well-approximated by a sharp partition — that there exist a clean division into accessible and inaccessible sectors such that cross-partition correlations enter only through $H_{\text{int}}$. This is a condition on the physics, not just the observer: it is satisfied when a physical boundary (causal, thermodynamic, or spatial) enforces a separation sharp enough that the residual leakage across the boundary can be absorbed into the interaction term. The theorem applies to any system where such an approximation holds; Part II identifies a physical realization where the sharpness is exact.

3. **Classical probability.** The observer's predictions are classical expectation values over the phase space; standard results of probability theory (the law of large numbers, the central limit theorem) are the primary statistical tools.

These axioms contain no quantum postulates — no Hilbert spaces, no commutation relations, no Born rule. The framework's central claim is that quantum mechanics *emerges* from these premises under the conditions specified below (§1.3).

### 1.3 Conditions on the Hidden Sector

The theorem requires three conditions on the relationship between the visible and hidden sectors. These are sufficient conditions: they define the class of systems for which the theorem guarantees the emergence of quantum mechanics.

**(C1) Non-zero coupling.** The interaction Hamiltonian satisfies $H_{\text{int}} \neq 0$. The visible and hidden sectors are dynamically coupled, not merely co-existing. The coupling is bidirectional: visible-sector transitions influence the hidden-sector state, and the hidden-sector state influences visible-sector transition probabilities.

**(C2) Slow-bath timescale separation.** The hidden sector's correlation time $\tau_B$ vastly exceeds the visible sector's dynamical timescale $\tau_S$:

$$\tau_S \ll \tau_B$$

This is the *inverse* of the standard Markovian regime, which requires $\tau_B \ll \tau_S$. The hidden sector evolves on timescales far exceeding those of any process accessible to the observer.

**(C3) Sufficient capacity.** The hidden sector has enough degrees of freedom that visible-sector interactions do not appreciably perturb its state on timescales $\ll \tau_B$. Precisely: if $N_H$ and $N_V$ denote the number of independent degrees of freedom in the hidden and visible sectors respectively, then $N_H / N_V$ is large enough that the cumulative imprint of all visible-sector transitions during any observationally relevant interval occupies a negligible fraction of the hidden sector's state space.

**Statement of the theorem.** Under Axioms 1–3, the finiteness condition, and conditions (C1)–(C3), the embedded observer's reduced description of the visible sector is mathematically equivalent to unitarily evolving quantum mechanics. The remainder of Part I constitutes the proof.

### 1.4 Partition-Relativity

Before proceeding to the proof, a structural consequence of the axioms is derived that will constrain the emergent description throughout.

**Lemma (partition-relativity).** *The emergent description of the visible sector is uniquely determined by the partition. Two observers whose causal access defines the same partition obtain the same reduced description. Any parameters of the emergent theory can depend only on quantities intrinsic to the partition — the geometric and thermodynamic properties of the boundary between visible and hidden sectors.*

*Proof.* By Axiom 1, the dynamics are deterministic: the Hamiltonian flow $\phi_t$ on $\Gamma_V \times \Gamma_H$ is a single, uniquely defined map. By Axiom 2, the partition $\Gamma = \Gamma_V \times \Gamma_H$ is fixed. By Axiom 3, the observer uses the Liouville measure $\mu$ on $\Gamma_H$ — the unique absolutely continuous measure preserved by the Hamiltonian flow (Liouville's theorem); any other smooth measure would evolve under the dynamics, introducing dependence on an arbitrary reference time, and singular invariant measures (e.g., those supported on periodic orbits) are excluded by Axiom 3's requirement that the observer assigns classical probability distributions over the full phase space. The marginalized transition probabilities

$$T_{ij}(t_2, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu(h)$$

are therefore uniquely determined by three inputs: the dynamics ($\phi_t$), the partition ($\Gamma_V, \Gamma_H$), and the measure ($\mu$). Since $\phi_t$ and $\mu$ are fixed by the axioms, the transition probabilities — and hence the complete stochastic process — depend only on the partition. If this process is P-indivisible (as shown in §2), the stochastic-quantum correspondence maps it to a quantum description. Since the stochastic process is unique, the quantum description is unique (up to unitary equivalence and gauge freedoms resolved below). In particular, any free parameters of the emergent theory — including the action scale $\hbar$ — can depend only on quantities intrinsic to the partition: the geometric and thermodynamic properties of the boundary between $\Gamma_V$ and $\Gamma_H$. $\square$

**Why this matters.** Partition-relativity is not an additional postulate but a direct consequence of the axioms' deterministic and measure-theoretic content. It will play three roles in what follows: (i) it ensures that the emergent quantum mechanics is universal for all sub-$c$ observers sharing the same cosmological horizon (§4.1); (ii) it constrains the action scale $\hbar$ to depend only on quantities intrinsic to the partition, and specifically to its local *structure* rather than its volume, which together with dimensional analysis and thermal self-consistency determines the exact value $\hbar = c^3 \epsilon^2 / (4G)$ (§5.2); and (iii) it provides the logical bridge between the general theorem and the quantitative derivation: the same principle that guarantees uniqueness also restricts which physical quantities can appear in the emergent description.

---

## 2. EMERGENT STOCHASTICITY AND P-INDIVISIBILITY

### 2.1 Emergent Stochasticity

The total system (visible + hidden sectors) evolves deterministically (Axiom 1). Every phase-space point $(x, h) \in \Gamma_V \times \Gamma_H$ maps to exactly one future point under the Hamiltonian flow. No randomness exists at this level. But the visible sector alone — what the embedded observer accesses — is stochastic. The observer knows $x$ but not $h$. Different hidden-sector states $h_k$ compatible with the same $x$ send $x$ to different visible-sector futures $x'_k$. The observer must assign transition probabilities $T_{ij}(t_2, t_1)$ by marginalizing the deterministic flow over the hidden sector using the Liouville measure, as defined in §1.4. As established there, the Liouville measure is the unique absolutely continuous measure preserved by the Hamiltonian flow, ensuring that the transition probabilities — and hence the emergent description — are uniquely determined by the partition.

This architecture makes the framework a hidden variable theory: the randomness observed by the embedded observer is epistemic, arising from ignorance of hidden-sector degrees of freedom rather than fundamental indeterminacy. The consistency of this structure with Bell's theorem is addressed in §3.2.

### 2.2 The Slow-Bath Regime

The Markovian limit for reduced dynamics requires a strict timescale separation $\tau_B \ll \tau_S$ [4], where the environment decorrelates much faster than the system evolves. Condition (C2) inverts this hierarchy: $\tau_S \ll \tau_B$. The hidden sector evolves on timescales far exceeding those of any visible-sector process, so its correlations do not decorrelate between successive system transitions. The memory kernel of the reduced dynamics is effectively constant over all observationally relevant timescales.

A slow bath must be distinguished from a static external field. A genuinely static (decoupled) hidden sector would merely shift Hamiltonian parameters in $H_V$ without inducing information backflow. By condition (C1), the hidden sector is not decoupled: the interaction Hamiltonian $H_{\text{int}}$ is continuously active. During each visible-sector transition, $H_{\text{int}}$ imprints the identity of the transition onto the hidden-sector state. Because the hidden sector is slow — not static — these imprints persist without being thermally overwritten: the hidden sector's internal relaxation timescale ($\tau_B$) vastly exceeds the interval between successive visible-sector transitions ($\tau_S$). On subsequent transitions, the coupling reads back the stored correlations, producing transition probabilities that depend on the system's prior trajectory — the non-Markovian open-systems regime of Breuer and Petruccione [4].

### 2.3 P-Indivisibility

*Claim.* Under conditions (C1)–(C3), the stochastic process defined in §2.1 is P-indivisible: its transition matrices cannot be factored through intermediate times as products of valid stochastic matrices.

**Step 1: Persistent system-environment correlations.** By §2.2, the hidden sector is dynamically coupled to the visible sector via $H_{\text{int}}$ and retains correlations over all timescales relevant to visible-sector observations. Consider three times $t_0 < t_1 < t_2$ with $t_2 - t_0 \ll \tau_B$. At $t_0$, the full state is $(x_i, h_0) \in \Gamma_V \times \Gamma_H$. During $[t_0, t_1]$, the deterministic dynamics produce a full state $(x_j, h_1)$. Because $t_1 - t_0 \ll \tau_B$, the hidden-sector state $h_1$ has not decorrelated: it retains detailed correlations with the system's trajectory during $[t_0, t_1]$, and in particular with the identity of $x_i$. The joint state $(x_j, h_1)$ at $t_1$ is therefore not a product of independent marginals.

**Step 2: Correlated intermediate states break P-divisibility.** During $[t_1, t_2]$, the transition from $x_j$ to $x_k$ depends on the hidden-sector state at $t_1$. The marginalized transition probability $T_{jk}(t_2, t_1)$ averages over *all* hidden-sector states compatible with $x_j$ at $t_1$. But the actual hidden-sector state $h_1$ is not drawn from this generic distribution — it was deterministically produced from $(x_i, h_0)$ and carries a memory of $x_i$. Therefore:

$$P(x_k, t_2 \mid x_j, t_1; x_i, t_0) \neq P(x_k, t_2 \mid x_j, t_1)$$

The failure of P-divisibility follows by contradiction. Suppose a valid stochastic matrix $T(t_2, t_1)$ existed such that $T(t_2, t_0) = T(t_2, t_1) \cdot T(t_1, t_0)$. Then the entry $T_{jk}(t_2, t_1)$ would be a fixed number — the probability of transitioning from $x_j$ to $x_k$ during $[t_1, t_2]$, independent of history. But Step 1 established that this probability depends on which $x_i$ produced $x_j$: the hidden-sector state at $t_1$ retains a record of $x_i$, and different records yield different forward transition probabilities. A single matrix entry $T_{jk}$ cannot simultaneously equal two different conditional probabilities. Therefore no valid stochastic matrix $T(t_2, t_1)$ exists. Equivalently, the matrix $\Lambda(t_2, t_1) = T(t_2, t_0) \cdot [T(t_1, t_0)]^{-1}$, if it exists, has negative entries.

**The process is P-indivisible.** $\square$

This result converges with several independent lines of work: Pechukas [5] showed that reduced dynamics of a correlated system need not preserve positivity; Rivas, Huelga, and Plenio [6, 7] formalized the connection between divisibility failure and information backflow; Pollock et al. [8] derived necessary and sufficient Markovianity conditions via the process tensor framework; and most directly, Strasberg and Esposito [9] demonstrated non-Markovian reduced dynamics precisely in the slow-bath regime of condition (C2).

**The role of sufficient capacity.** Condition (C3) is what prevents P-indivisibility from being transient. Each visible-sector transition imprints correlations into the hidden sector via $H_{\text{int}}$. If the hidden sector has insufficient degrees of freedom, successive imprints overwrite earlier ones — the hidden sector saturates, its memory is erased, and the reduced dynamics cross over to Markovian behavior. When $N_H \gg N_V$, the cumulative imprint of all visible-sector transitions occupies a negligible fraction of the hidden sector's state space, and correlations accumulate without overwriting. A fast bath with vast capacity would still decorrelate; a slow bath with insufficient capacity would eventually forget. Only the conjunction of slow dynamics (C2) *and* sufficient capacity (C3) sustains the persistent correlations required for P-indivisibility.

### 2.4 Explicit Construction: A Minimal Model

To make the P-indivisibility argument concrete, consider a minimal deterministic system satisfying conditions (C1)–(C3); its reduced dynamics are explicitly verified to be P-indivisible.

**The model.** The visible sector has two states: $x \in \{0, 1\}$. The hidden sector has six states: $h \in \{1, 2, 3, 4, 5, 6\}$. The total phase space has 12 states $(x, h)$. The dynamics are a deterministic, invertible permutation $\sigma$ on these 12 states, defined as six disjoint transpositions:

$$\sigma = (0{,}1 \leftrightarrow 1{,}1)\;(0{,}2 \leftrightarrow 1{,}2)\;(0{,}3 \leftrightarrow 0{,}4)\;(0{,}5 \leftrightarrow 0{,}6)\;(1{,}3 \leftrightarrow 1{,}4)\;(1{,}5 \leftrightarrow 1{,}6)$$

The first two transpositions couple the visible and hidden sectors — they change $x$ while preserving $h$, implementing condition (C1). The remaining four permute hidden-sector labels within each visible-sector value, representing the hidden sector's internal dynamics. Since $\sigma$ is a product of disjoint transpositions, $\sigma^2 = \text{id}$: the hidden sector retains perfect correlations between successive transitions, satisfying condition (C2). Six hidden-sector states per visible-sector value ensures the hidden sector is not saturated by a single transition, satisfying condition (C3).

**Transition matrices.** At $t = 0$, the observer knows $x$ but not $h$, and assigns the uniform (Liouville) measure over the 6 hidden states. At $t = 1$ (one application of $\sigma$):

From $x = 0$: two of six hidden states ($h = 1, 2$) send $x$ to 1; four ($h = 3, 4, 5, 6$) leave $x$ at 0. From $x = 1$: two of six ($h = 1, 2$) send $x$ to 0; four leave $x$ at 1. The one-step transition matrix is:

$$T(1,0) = \begin{pmatrix} 2/3 & 1/3 \\ 1/3 & 2/3 \end{pmatrix}$$

At $t = 2$ ($\sigma^2 = \text{id}$): every state returns to itself, so $T(2,0) = I$.

A Markov chain with transition matrix $T(1,0)$ would predict $T(2,0)_{\text{Markov}} = T(1,0)^2 = \left(\begin{smallmatrix} 5/9 & 4/9 \\ 4/9 & 5/9 \end{smallmatrix}\right)$ — continued mixing. The actual dynamics show complete *un-mixing*: the system returns to its initial state with certainty. This is information backflow.

**P-divisibility test.** If the process were P-divisible, one could write $T(2,0) = \Lambda(2,1) \cdot T(1,0)$ with $\Lambda(2,1)$ a valid stochastic matrix (non-negative entries, rows summing to 1). Computing:

$$\Lambda(2,1) = T(2,0) \cdot [T(1,0)]^{-1} = I \cdot \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

The matrix $\Lambda(2,1)$ has negative entries $(-1)$. No valid stochastic matrix can serve as the intermediate propagator. **The process is P-indivisible.** $\square$

**The mechanism.** The hidden sector acts as a memory register. At step 1, the transpositions $(0,h) \leftrightarrow (1,h)$ for $h \in \{1, 2\}$ flip $x$ while preserving $h$. After step 1, a state now at $x = 1$ with $h \in \{1, 2\}$ carries the record "I was at $x = 0$." At step 2, the same transposition reads this record and flips $x$ back. The visible-sector dynamics exhibit information backflow: the system appears to "remember" its origin, which is impossible for a memoryless process. The model illustrates the mechanism in the idealized limit of perfect recurrence ($\sigma^2 = \text{id}$, i.e., $\tau_B/\tau_S = 2$). The cosmological realization of Part II has $\tau_S/\tau_B \sim 10^{-32}$; the P-indivisibility is more extreme, not less, when the hidden sector's memory is more persistent.

---

## 3. THE EMERGENCE OF QUANTUM MECHANICS

### 3.1 The Stochastic-Quantum Correspondence

By Barandes' stochastic-quantum correspondence [10, 11], any indivisible stochastic process on a finite configuration space of size $n$ can be embedded into a unitarily evolving quantum system on a Hilbert space of dimension $\leq n^3$. The P-indivisible stochastic process established in §2.3 satisfies the theorem's hypotheses. The correspondence guarantees the existence of a Hilbert space, a unitary evolution operator, and projection operators such that the quantum system's Born-rule probabilities reproduce all transition probabilities of the classical stochastic process.

**From phase space to configuration space.** The axioms define the dynamics on a phase space $\Gamma$ with coordinates $(q, p)$, while Barandes' correspondence operates on a configuration space. The connection is the marginalization itself: the transition probabilities $T_{ij}(t_2, t_1)$ defined in §2.1 are projections of the full phase-space flow onto the configuration sector of $\Gamma_V$, with the momenta — along with all hidden-sector degrees of freedom — absorbed into the marginalization over the Liouville measure. The resulting stochastic process lives on the discrete configuration space defined by the finiteness condition, where the correspondence applies directly.

Three features of quantum mechanics emerge from this correspondence. The Schrödinger equation is the unique time-evolution law, arising from the differentiability of the unitary in time. The Born rule is not an additional postulate but the equilibrium distribution of the indivisible stochastic process [10, 11]. The action scale $\hbar$ requires more careful treatment. The correspondence guarantees the existence of a unitary evolution operator $U(t)$, but $U$ is dimensionless; $\hbar$ enters only when one defines the Hamiltonian $\hat{H}(t) \equiv i\hbar \, \partial_t U \cdot U^\dagger$, converting the dimensionless rate of change into energy units. The correspondence itself is silent about the value of this conversion factor — it establishes that a quantum description exists for any P-indivisible process, but not which action scale it carries. What fixes $\hbar$ is the physical content of the partition: the emergent description must be unique for a given partition (§3.4), so the action scale can depend only on quantities intrinsic to the partition boundary. Its value is derived for the cosmological realization in Part II (§5).

**Finite-dimensionality.** Barandes' proof is established for finite-dimensional configuration spaces. In the general theorem (Part I), the finiteness condition guarantees applicability directly: the finite minimal cell volume ensures that any finite spatial region contains at most a finite number of independent cells, and the causal partition (Axiom 2) restricts the visible sector to a finite total volume. In the cosmological application (Part II), the same guarantee comes from the partition geometry: the horizon's finite area bounds the number of coupled modes to $A/\epsilon^2$, ensuring the effective configuration space is finite-dimensional without requiring the total phase space to be finite. Calvo [12] has extended the correspondence to infinite-dimensional systems, relaxing the finite-dimensionality requirement, but the extension is not required here. (The $n^3$ upper bound on Hilbert space dimension is a worst-case embedding guarantee, not an estimate of the physical dimension. For the cosmological application with $n \sim S_{\text{dS}} \sim 10^{122}$, the physical Hilbert space dimension is expected to be much smaller — plausibly $\sim n$ rather than $\sim n^3$ — since the trace-out produces a structured process with extensive symmetries that the generic bound does not exploit.)

### 3.2 Bell Inequality Violations

The framework is a hidden variable theory: quantum randomness arises epistemically from ignorance of hidden-sector degrees of freedom rather than fundamental indeterminacy. Bell's theorem [13] rules out *local* hidden variable theories — those satisfying the factorizability condition $P(a, b \mid x, y, \lambda) = P(a \mid x, \lambda) \cdot P(b \mid y, \lambda)$, where $\lambda$ denotes hidden variables with distribution $\rho(\lambda)$, and $x, y$ are measurement settings assumed statistically independent of $\lambda$. The present framework evades Bell's theorem not by violating measurement independence (superdeterminism) but by violating factorizability through a mechanism that is nonetheless *causally local* — no superluminal signaling occurs.

**The mechanism: non-factorizable joint dynamics from a shared causal past.** Consider two subsystems $Q$ and $R$ that interact locally at preparation time $t'$ and are subsequently separated to spacelike-distant measurement stations. In the stochastic-quantum framework [10, 11, 14], the preparation interaction creates a *joint* transition matrix $T_{QR}(t_2, t_1)$ on the composite configuration space $\mathcal{C}_Q \times \mathcal{C}_R$. Because the joint process is P-indivisible (§2.3), this transition matrix does not factorize:

$$T_{QR} \neq T_Q \otimes T_R$$

This non-factorizability *is* entanglement, expressed at the stochastic level. The correlations are encoded in the *form of the dynamical law itself* — in the structure of the joint transition matrix — rather than in a hidden variable $\lambda$ over which one could integrate and apply screening-off. Since the process is indivisible, there are no well-defined intermediate conditional probabilities that would permit the factorization Bell's theorem requires. Reichenbach's common-cause principle does not apply to indivisible processes, because the principle presupposes that conditioning on the complete common cause renders the effects independent — a decomposition that indivisibility explicitly forbids.

**Causal locality without Bell locality.** The Jarrett decomposition splits Bell's factorizability condition into *parameter independence* (PI) and *outcome independence* (OI). Quantum mechanics violates OI while preserving PI. The present framework reproduces this structure. Barandes, Hasan, and Kagan [14] formalize causal locality as a marginalization condition on the joint transition matrix: for subsystems $Q$ and $R$ at spacelike separation, $\sum_{r} T_{(q,r),(q_0,r_0)}(t) = T_{q,q_0}^{(Q)}(t)$ for all $r_0$ — marginalizing over $R$'s final configuration yields $Q$'s transition probabilities independent of $R$'s initial configuration. The joint transition matrix carries non-factorizable correlations from the shared preparation, but these correlations are accessible only through joint statistics, never through local marginals.

**The Tsirelson bound from indivisibility plus causal locality.** Barandes, Hasan, and Kagan [14] prove that the conjunction of indivisibility and causal locality restricts the maximum CHSH correlator to exactly Tsirelson's bound $|S| \leq 2\sqrt{2}$. Divisible (classical) stochastic processes satisfy $|S| \leq 2$, reproducing Bell's bound. PR-box correlations ($|S| = 4$) cannot be realized because the required transition matrices have no unitary square root. This result receives independent support from Le et al. [15], who prove the temporal analogue: *divisible* quantum dynamics satisfies the temporal Tsirelson bound, while *indivisible* dynamics can exceed it.

**Measurement independence and the distinction from superdeterminism.** The framework preserves measurement independence by construction: the transition probabilities $T_{ij}(t_2, t_1)$ are defined independently of the initial distribution, and measurement settings enter through which subsystem couplings are activated, not through pre-established correlations with the prepared state. Superdeterministic theories evade Bell's theorem by violating this independence; the present framework instead violates outcome independence — the P-indivisible dynamics propagate preparation correlations forward as a single, non-factorizable transition. This distinction has empirical content: superdeterministic theories generically predict deviations from standard statistical mechanics, while the present framework predicts none. This placement — violating factorizability (specifically outcome independence in the Jarrett decomposition) while preserving both measurement independence and parameter independence — is precisely the class Fine's theorem [24] permits: models that reproduce quantum correlations through non-factorizable joint dynamics rather than through conspiracy between hidden variables and measurement settings.

### 3.3 Interpretive Consequences

**A note on "hidden sector" in what follows.** The general theorem applies to any partition satisfying the axioms, and the interpretive consequences below are stated in that generality. In the cosmological application of Part II, the hidden sector is specifically the trans-horizon region; the degrees of freedom involved in quantum experiments — photons, electrons, slits, detectors — are all visible-sector objects. Their quantum behavior is not produced by a separate marginalization over nearby modes but is a downstream consequence of the single cosmological trace-out: the emergent quantum mechanics, once established by the theorem, governs all visible-sector dynamics, including the local experiments discussed here.

The theorem resolves several foundational puzzles as direct consequences rather than additional postulates. In the double-slit experiment, the particle traverses a single slit; the interference pattern arises because the transition matrix $T_{ij}(t_2, t_1)$ — which governs the visible sector's dynamics after the trace-out — encodes the boundary conditions of the full experimental geometry. Opening or closing the second slit changes those boundary conditions, altering the transition probabilities and hence the pattern. The "wave-like" behavior is not the particle spreading out but the trace-out-induced dynamics responding to a change in the visible-sector geometry. In Wigner's friend scenarios, the Friend's measurement produces a definite outcome via the indivisible dynamics; Wigner's superposition assignment reflects his epistemic deficit from tracing out the lab's internal degrees of freedom, not the Friend's physical state. The Everettian measure problem dissolves because the total system evolves deterministically as a single reality — the Schrödinger equation is a mandatory compression algorithm for an observer who cannot track hidden-sector degrees of freedom, and "branches" are features of the compressed description, not of the underlying dynamics.

### 3.4 Scope, Limitations, and Relation to Prior Work

**What the theorem says.** If a system satisfies Axioms 1–3, the finiteness condition, and conditions (C1)–(C3), the embedded observer's reduced description is quantum mechanics. The Schrödinger equation, Born rule, and Bell inequality violations are structural consequences of the reduction, not independent postulates.

**What the theorem does not say.** It does not identify which physical systems satisfy the conditions. That is an empirical question. It does not derive the numerical value of $\hbar$ for any specific system — only that an action scale set by the trace-out noise necessarily exists. These questions are addressed for a specific physical realization in Part II.

**Partition-relativity: physical implications.** The lemma of §1.4 established that the emergent description is uniquely determined by the partition. The converse deserves explicit statement: *different* partitions produce *different* reduced descriptions. Different divisions of the total phase space into visible and hidden sectors yield different stochastic processes, potentially with different action scales or, if the conditions (C1)–(C3) are not met for a given partition, no quantum description at all. The theorem does not say "quantum mechanics is the unique description of reality." It says "quantum mechanics is the unique description available to any observer whose causal access defines a partition satisfying (C1)–(C3)."

This is a conditional prediction, not a claim that distinct partitions are generically realized. "Embedded observers cannot access the complete state" is entirely consistent with all observers sharing the *same* inaccessible region — in which case the emergent description is universal, not relative. Partition-relativity becomes physically significant only when distinct observers have distinct causal boundaries. The physical implications of this for our universe — where the causal partition is defined by null geodesics and all sub-$c$ observers share the same horizon — are developed in Part II (§4.1).

**Dependence on Barandes' correspondence.** The theorem rests on Barandes' stochastic-quantum correspondence as its mathematical engine.

*What the correspondence establishes and does not.* Barandes [10, 11] proves that any indivisible stochastic process on a finite configuration space of size $n$ can be embedded into a unitarily evolving quantum system on a Hilbert space of dimension $\leq n^3$, and conversely that every quantum system can be understood as such a process. The correspondence is bidirectional and exact: it reproduces all first-order conditional probabilities — and hence all empirical predictions of quantum mechanics, including interference, entanglement, and decoherence — from indivisible stochastic dynamics on a classical configuration space. The Born rule emerges as the equilibrium distribution rather than an independent postulate. The proof rests on the Stinespring dilation theorem and standard linear algebra; it has been published in a peer-reviewed venue [11] and corroborated by independent follow-up work: Calvo [12] extended it to infinite-dimensional systems, Pimenta [25] provided a complete geometric characterization of divisible and indivisible dynamics within the correspondence's framework, and Doukas [26] proved several key structural properties while clarifying the conditions under which effective Markovian behavior can emerge from non-Markovian foundations. Barandes, Hasan, and Kagan [14] derived the Tsirelson bound from indivisibility plus causal locality. The higher-order conditional probabilities — the multi-time statistics beyond two-point transition matrices — are not uniquely fixed by the correspondence; different choices yield the same first-order predictions and hence the same empirical content. The present theorem is not affected by this ambiguity: partition-relativity (§1.4) uniquely determines the stochastic process, including its multi-time structure, from the physical content of the partition (§5.3).

*Where the correspondence enters.* The dependence is load-bearing but circumscribed. Partition-relativity, emergent stochasticity, and P-indivisibility (§§1.4, 2) do not invoke Barandes at all — they follow from the axioms and conditions alone. The correspondence enters at a single step: the map from P-indivisible stochastic process to quantum mechanics (§3.1). Everything before that step — including the result that the embedded observer cannot see classical physics and that information backflow produces non-factorizable correlations — is independent of the correspondence.

---

# PART II: THE COSMOLOGICAL APPLICATION

## 4. THE COSMOLOGICAL HORIZON AS CAUSAL PARTITION

### 4.1 The Partition

General relativity defines the causal structure of spacetime. The cosmological horizon is the boundary beyond which no signal propagating at or below $c$ can reach the embedded observer. Every physically realizable measurement technique — electromagnetic, gravitational-wave, neutrino — propagates at or below $c$ and therefore encounters the same boundary. The horizon implements the causal partition of Axiom 2 for all sub-$c$ observers simultaneously: the visible sector $\Gamma_V$ is the interior of the cosmological horizon, and the hidden sector $\Gamma_H$ is everything beyond it.

This identification is not a modeling choice but a consequence of GR's causal structure. A hypothetical observer with access to a causal channel not constrained by the light cone would have a different partition, a different (or absent) hidden sector, and by the theorem's own logic, a different emergent description. No such channel is available within GR. The specific quantum mechanics observed is the quantum mechanics of light-cone-bounded observers; its universality is a consequence of the causal structure, not a postulate.

### 4.2 Verification of the Conditions

**Condition (C1): Non-zero coupling.** The cosmological horizon is not a static wall. Stress-energy conservation across the horizon enforces dynamical correlations between the visible and hidden sectors: matter and radiation cross the horizon continuously, and the horizon area responds to changes in the interior energy density via the Friedmann equation. The coupling is bidirectional. **Condition (C1) is satisfied.**

**Condition (C2): Slow-bath timescale separation.** The hidden sector's shortest correlation timescale is set by the Hubble time: $\tau_B \gtrsim 1/H \sim 10^{17}$ s, since modes beyond the horizon evolve on timescales no shorter than the rate at which the horizon itself changes. (Modes deeper in the hidden sector have even longer correlation times.) For any laboratory-scale process with characteristic frequency $\omega \gg H$, the visible sector's dynamical timescale is $\tau_S \sim 1/\omega \sim 10^{-15}$ s or shorter. The ratio is:

$$\frac{\tau_S}{\tau_B} \sim 10^{-32}$$

The hidden sector cannot decorrelate between any pair of visible-sector events. The Markovian approximation fails categorically. **Condition (C2) is satisfied.**

**Condition (C3): Sufficient capacity.** The hidden sector has $N_{\text{modes}} = A/\epsilon^2$ independent degrees of freedom, where $A = 4\pi c^2/H^2$ is the horizon area and $\epsilon$ is the discreteness scale of the finiteness condition. For any $\epsilon$ at or above the Planck scale, the horizon area is cosmological ($A \sim 10^{52}$ m$^2$) and the visible sector involves at most $\sim 10^{80}$ baryons. No laboratory process can appreciably perturb the hidden sector's state. The hidden sector is never saturated. **Condition (C3) is satisfied.**

### 4.3 Application of the Theorem

All three axioms hold. All three conditions hold. The finiteness condition — which is an independent assumption in Part I — is here a consequence of the partition geometry: the cosmological horizon has finite area $A = 4\pi c^2/H^2$, and all visible-hidden coupling passes through this boundary. The number of modes that participate in the trace-out is bounded by $A/\epsilon^2$, which is finite for any $\epsilon > 0$. The effective stochastic process therefore lives on a finite-dimensional configuration space, as Barandes' correspondence requires, without any assumption that the total phase space beyond the horizon is itself finite.

The theorem of Part I applies: the embedded observer's reduced description of the visible sector is P-indivisible, and by Barandes' stochastic-quantum correspondence [10, 11], mathematically equivalent to unitarily evolving quantum mechanics with an action scale $\hbar$ determined by the local structural properties of the partition boundary.

*What this step requires:* Part I plus Barandes. The finiteness condition is provided by the partition geometry. No additional physics.

---

## 5. DERIVATION OF THE EMERGENT ACTION SCALE ($\hbar$)

### 5.1 The Classical Horizon Temperature

The theorem guarantees that $\hbar$ exists but does not compute its value. Partition-relativity (§1.4) constrains $\hbar$ to depend only on quantities intrinsic to the partition — the geometric and thermodynamic properties of the boundary between visible and hidden sectors. The required thermodynamic input is model-independent: it follows from Jacobson's thermodynamic derivation of Einstein's field equations [16].

Jacobson (1995) demonstrated that applying the thermodynamic relation $dE = T \, dS$ to local causal horizons yields Einstein's field equations. The same identity relates mass-energy to area via:

$$dE = \frac{c^2 \kappa}{8\pi G} \, dA$$

The classical entropy density on the horizon is $\eta = 1/\epsilon^2$ — one degree of freedom per minimal cell (finiteness condition). Therefore $dS = dA/\epsilon^2$, and equating $dE = T_{\text{cl}} \, dS$ fixes the classical temperature:

$$T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G k_B}$$

For the de Sitter horizon, the surface gravity is $\kappa = cH$, giving:

$$k_B T_{\text{cl}} = \frac{c^3 \epsilon^2 H}{8\pi G}$$

This temperature depends on $G$, $c$, $H$, $\epsilon$, and $k_B$ — no $\hbar$. It is the temperature of the hidden sector as a classical thermal reservoir, derived from the horizon geometry without reference to quantum mechanics.

### 5.2 The Emergent Action Scale

The stochastic-quantum correspondence maps the P-indivisible transition matrices to a unitary evolution $U(t)$, but leaves an enormous gauge freedom: the transition matrix constrains only $|U_{ij}|^2$, leaving the quantum phases — and hence the energy eigenvalues and the overall action scale — undetermined. This is the Schur-Hadamard gauge freedom inherent in the stochastic-to-quantum map. Partition-relativity (§1.4) constrains the resolution: the emergent quantum description is uniquely determined by the partition, so the action scale $\hbar$ can depend only on quantities intrinsic to the partition — the geometric and thermodynamic properties of the boundary between visible and hidden sectors.

The determination of $\hbar$ proceeds in four steps. Steps 1–3 establish the scaling; Step 4 fixes the prefactor.

**Step 1: Uniqueness from partition-relativity.** The lemma of §1.4 establishes that the emergent description is not merely *constrained* by the partition but *uniquely determined* by it. The three inputs — the dynamics $\phi_t$ (fixed by Axiom 1), the Liouville measure $\mu$ (fixed by Axiom 3), and the partition $\Gamma_V \times \Gamma_H$ (fixed by Axiom 2) — yield a single stochastic process, which maps to a single quantum description up to unitary equivalence. The action scale $\hbar$ is therefore not a free parameter to be fitted but a derived quantity: it is whatever value the unique correspondence assigns. There is no family of consistent quantum descriptions parameterized by different choices of $\hbar$.

**Step 2: The action scale is structural, not volumetric.** Among the quantities intrinsic to the cosmological partition, some characterize the *structure* of the coupling across the boundary — the discreteness scale, the gravitational coupling, the speed of light — while others characterize the *volume* of the hidden sector — the horizon area $A$, the number of modes $N_{\text{modes}} = A/\epsilon^2$, or equivalently the Hubble parameter $H$ through $A = 4\pi c^2/H^2$. The surface gravity $\kappa$ occupies an intermediate position: it is a local geometric property of the horizon, but for de Sitter spacetime $\kappa = cH$, so it carries implicit $H$-dependence. Its classification is addressed quantitatively below (after Step 3).

The action scale $\hbar$ governs the conversion between the stochastic and unitary descriptions: it sets the rate at which the unitary $U(t)$ accumulates phase. This conversion is determined by the *character* of the P-indivisibility — how the hidden sector couples to the visible sector and imprints correlations — not by the total capacity of the hidden sector.

The distinction is analogous to a classical thermal reservoir: the temperature of a heat bath determines the Boltzmann factor $e^{-E/k_BT}$ regardless of the bath's total size; adding more degrees of freedom at the same temperature changes the heat capacity but not the thermal fluctuation spectrum. Likewise, conditions (C1)–(C3) require the hidden sector to be coupled, slow, and of sufficient capacity — but once these conditions are met, excess capacity beyond the sufficiency threshold does not alter the nature of the trace-out. A universe with a larger horizon area has more hidden-sector modes, but the local structure of the partition boundary — the discreteness scale and the gravitational coupling — is unchanged. If $\hbar$ depended on $H$ through volumetric factors, observers at different cosmological epochs would obtain emergent quantum descriptions with different action scales — different quantum mechanics entirely. The structural character of the correspondence excludes this: the action scale is set by how correlations are imprinted, not by how much room exists to store them.

**Step 3: Dimensional determination.** With volumetric quantities excluded, the partition-intrinsic quantities that can appear in $\hbar$ are restricted to those characterizing the local structure of the boundary: $c$ (defines the causal boundary), $G$ (enters through Jacobson's identity relating geometry to energy), and $\epsilon$ (sets the phase-space grain). The unique combination with dimensions of action is $c^3 \epsilon^2 / G$, giving:

$$\hbar = \beta \frac{c^3 \epsilon^2}{G}$$

where $\beta$ is a dimensionless prefactor. Steps 1–3 establish that $\beta$ exists and is unique; they do not determine its value. The structural/volumetric distinction excludes $H$-dependence, and dimensional analysis selects the functional form, but a dimensionless constant cannot be fixed by dimensional analysis alone.

**The status of the surface gravity.** The surface gravity $\kappa$ is a local geometric property of the horizon and could in principle contribute to $\hbar$ as a structural quantity. Dimensional analysis settles the question: the most general combination of $c$, $G$, $\epsilon$, and $\kappa$ with dimensions of action is $(c^3 \epsilon^2 / G) \cdot (\kappa \epsilon / c^2)^e$ for any exponent $e$. For the de Sitter horizon, $\kappa \epsilon / c^2 = H \epsilon / c \sim H l_p / c \sim 10^{-61}$. Any non-zero power of $e$ gives a correction suppressed by at least 61 orders of magnitude. The leading-order result $\hbar \propto c^3 \epsilon^2 / G$ is therefore robust: even if $\kappa$ enters the exact formula, its contribution is parametrically negligible.

**Step 4: Thermal self-consistency fixes the prefactor.** The derivation so far has produced two independent expressions for the thermal state of the partition boundary, one from each level of description.

*Before the trace-out* (§5.1), the classical horizon temperature is derived from Jacobson's thermodynamic identity and the entropy density $\eta = 1/\epsilon^2$:

$$k_B T_{\text{cl}} = \frac{c^3 \epsilon^2 \kappa}{8\pi G}$$

This expression involves only classical quantities: $G$, $c$, $\epsilon$, $\kappa$, $k_B$. No $\hbar$ appears.

*After the trace-out*, the emergent quantum mechanics is established by Part I with an action scale $\hbar$ whose scaling is $\hbar = \beta c^3 \epsilon^2 / G$ (Step 3) but whose prefactor $\beta$ is not yet fixed. Quantum field theory on curved spacetime — which is now a *consequence* of the emergent description, not an independent input — predicts the Gibbons-Hawking temperature [17] for any horizon with surface gravity $\kappa$:

$$k_B T_{\text{GH}} = \frac{\hbar \kappa}{2\pi c}$$

These two temperatures describe the same physical boundary. $T_{\text{cl}}$ is the temperature of the hidden sector as a classical thermal reservoir, derived from the partition geometry. $T_{\text{GH}}$ is the temperature that the emergent quantum description assigns to the same horizon. If $T_{\text{cl}} \neq T_{\text{GH}}$, the emergent description is internally inconsistent: it predicts a different thermal state for the very boundary that produced it.

Self-consistency requires $T_{\text{cl}} = T_{\text{GH}}$. For the de Sitter horizon ($\kappa = cH$):

$$\frac{c^3 \epsilon^2 H}{8\pi G} = \frac{\hbar H}{2\pi}$$

The Hubble parameter $H$ cancels — confirming the structural/volumetric point, since the result is $H$-independent. Solving for $\hbar$:

$$\boxed{\hbar = \frac{c^3 \epsilon^2}{4G}}$$

The prefactor is $\beta = 1/4$. No free parameter remains.

**Why this is not circular.** The argument uses the Gibbons-Hawking temperature, which is a result of quantum field theory on curved spacetime — the very theory whose emergence the theorem establishes. The logic is sequential, not circular:

1. Part I establishes that the emergent description *is* quantum mechanics, with *some* action scale $\hbar$ (existence, not value).
2. The emergent QM, applied to the de Sitter horizon, predicts $T_{\text{GH}}(\hbar) = \hbar H / (2\pi k_B)$. This is a *consequence* of the emergent theory, expressed in terms of the unknown $\hbar$.
3. The classical temperature $T_{\text{cl}}$ is derived independently in §5.1, with no $\hbar$.
4. Matching the two — requiring that the emergent description be consistent with the conditions that produced it — gives one equation in one unknown.

This is a *gap equation*: the same logical structure as self-consistent mean-field calculations in condensed matter physics, where the order parameter is determined by requiring the emergent collective description to reproduce the microscopic conditions that generated it. The Gibbons-Hawking temperature is not imported as an external postulate; it is a *prediction* of the emergent theory that must be consistent with the classical temperature that preceded the theory's emergence.

**Robustness of the Gibbons-Hawking temperature on the emergent lattice.** One might worry that $T_{\text{GH}} = \hbar \kappa / (2\pi c k_B)$ is a continuum result, whereas the emergent QFT of §7.1 lives on a lattice with cutoff $\epsilon$. The Gibbons-Hawking derivation depends on the surface gravity $\kappa$ — an infrared quantity set by the global geometry of the horizon — and on the analytic structure of the vacuum state near the horizon, which is fixed by the KMS condition (periodicity in imaginary time with period $2\pi / \kappa$). Neither ingredient is sensitive to the ultraviolet cutoff. The temperature is an IR property of the horizon geometry, not a UV property of the field theory, and survives lattice regularization unchanged. This is the same reason the Hawking temperature is insensitive to trans-Planckian physics — a point established rigorously by Unruh's sonic analogue [28] and by Fredenhagen and Haag's algebraic derivation [29].

The value $\hbar = c^3 \epsilon^2 / (4G)$ is the end product of a chain of constraints: partition-relativity fixes $\hbar$ uniquely (Step 1), the structural nature of the correspondence eliminates $H$-dependent factors (Step 2), dimensional analysis selects the functional form (Step 3), and thermal self-consistency fixes the prefactor (Step 4).

*What this step requires:* Partition-relativity (§1.4), the structural/volumetric distinction, Jacobson's thermodynamic identity, the Gibbons-Hawking temperature as a consequence of the emergent QM (Part I), and the self-consistency requirement that these describe the same boundary. No mode-structure assumptions, microphysical coupling model, or spectral density. The derivation is independent of the conjecture of §5.3.

### 5.3 Conjecture: Full Gauge-Fixing From the Process Tensor

The thermal self-consistency argument of §5.2 (Step 4) determines $\hbar$ exactly, but it does so by matching two expressions for the horizon temperature — a physical requirement external to the stochastic-quantum correspondence itself. A stronger result would determine $\hbar$ *entirely from within the correspondence*, resolving the Schur-Hadamard gauge freedom using only the multi-time statistics of the trace-out. The following sketch identifies the logical structure such a proof would require and locates the gap.

**Step 1: The process tensor.** The P-indivisible stochastic process generated by the trace-out is characterized not by a single transition matrix $T(t_2, t_1)$ but by the complete hierarchy of multi-time correlation functions, formalized by Pollock et al. [8] as the *process tensor* $\mathcal{T}_{n:0}$ — a multilinear map that takes any sequence of interventions at times $t_0, \ldots, t_n$ and returns the resulting probability distribution. The process tensor contains strictly more information than the set of two-time transition matrices. Pollock et al. prove that every process tensor admits a unitary dilation: there exists an environment space $\mathcal{H}_E$, an initial environment state $\rho_E$, and a unitary $U_{\text{tot}}$ on $\mathcal{H}_S \otimes \mathcal{H}_E$ that reproduces all multi-time statistics via partial trace — the quantum analogue of the Kolmogorov extension theorem.

**Step 2: Uniqueness in this framework.** In the present framework, the "environment" is the hidden sector, and its initial state is the Liouville measure restricted to $\Gamma_H$ — a thermal state at $T_{\text{cl}}$ (§5.1). The total dynamics are the deterministic Hamiltonian flow (Axiom 1), which is unique. The process tensor of the visible sector is therefore uniquely determined — it is the partial trace of a unique total unitary acting on a unique initial state. This is a consequence of Axioms 1 and 2, not a choice.

**Step 3 (the gap).** Does the unique process tensor determine a unique effective unitary $U_{\text{eff}}(t)$ on the visible sector, including its phases? A single two-time transition matrix $T_{ij} = |U_{ij}|^2$ does not — this is the Schur-Hadamard degeneracy. But the process tensor provides multi-time data: conditional probabilities $P(x_k, t_2 \mid x_j, t_1 \mid x_i, t_0)$ for arbitrary sequences of intermediate configurations. Each additional time point provides new constraints on the phases of $U$, because the composition $U(t_2, t_1) U(t_1, t_0)$ entangles the phases at different times. The conjecture is that for the class of processes arising under conditions (C1)–(C3), the multi-time data is sufficient to break the Schur-Hadamard degeneracy completely, fixing $U_{\text{eff}}(t)$ up to a physically irrelevant global phase — and with it, the action scale $\hbar$ including its exact numerical value.

**Why the conjecture is likely true, and what a proof would require.** P-indivisibility means precisely that the multi-time statistics *cannot* be reconstructed from two-time data — the process has genuine memory that encodes information beyond $|U_{ij}|^2$. The slow-bath condition (C2) ensures that this memory is persistent, providing an ever-growing set of phase constraints, and (C3) ensures these constraints are independent — not recycled through a finite-dimensional bottleneck. A finite number of independent phase constraints drawn from a process with persistent memory and unlimited capacity would be expected to fix $N^2$ phase functions, leaving at most a global phase. A rigorous version would need to show this using tools from the process tensor framework [8] combined with the representation theory of the Schur-Hadamard gauge group.

**Relation to Step 4.** If the conjecture is true, the process tensor alone determines $\hbar = c^3 \epsilon^2 / (4G)$ without appeal to the Gibbons-Hawking temperature — the thermal self-consistency of Step 4 would then follow as a *theorem* rather than serving as an independent determination. The two routes to $\hbar$ — thermal matching and process-tensor gauge-fixing — would be proven equivalent. Until the conjecture is established, Step 4 provides the value of $\hbar$ on independent physical grounds, and the conjecture predicts that any future process-tensor derivation must yield the same result.

*Status: Conjecture. The three-step structure is logically complete; Step 3 requires new mathematics. The value of $\hbar$ is not contingent on this conjecture — it is independently fixed by thermal self-consistency (§5.2, Step 4).*

---

## 6. SELF-CONSISTENCY AND THE DISCRETENESS SCALE

The value $\hbar = c^3 \epsilon^2 / (4G)$ is established by the chain of constraints in §5.2: partition-relativity, the structural/volumetric distinction, dimensional analysis, and thermal self-consistency. Rearranging:

$$\epsilon^2 = \frac{4\hbar G}{c^3} = 4\,l_p^2$$

The framework predicts $\epsilon = 2\,l_p$ exactly. The geometric discreteness scale is twice the Planck length — a specific quantitative prediction, not an order-of-magnitude estimate.

This value is necessary for self-consistency. If $\epsilon^2 \ll l_p^2$, sub-Planckian subcells would be dynamically active yet unresolvable by the emergent description, creating a second trace-out with its own noise intensity and breaking the single-valuedness of $\hbar$. If $\epsilon^2 \gg l_p^2$, the emergent description would assign distinct quantum states to configurations that are physically identical in the substratum. The regime $\epsilon = \mathcal{O}(l_p)$ is the only self-consistent one; thermal self-consistency selects $\epsilon = 2\,l_p$ within it.

With $\epsilon = 2\,l_p$, the number of independent modes on the cosmological horizon is:

$$N_{\text{modes}} = \frac{A}{\epsilon^2} = \frac{A}{4\,l_p^2} = S_{\text{dS}}$$

where $S_{\text{dS}} = A/(4\,l_p^2)$ is the Bekenstein-Hawking entropy of the de Sitter horizon. The factor of $1/4$ in the Bekenstein-Hawking formula — historically introduced as a proportionality constant — is here derived as a consequence of the partition geometry and the thermal self-consistency condition: each minimal cell of area $\epsilon^2 = 4\,l_p^2$ on the horizon contributes one unit of entropy, and $A / (4\,l_p^2) = A / \epsilon^2$ recovers the standard formula exactly.

**Consistency check.** After the emergence of quantum mechanics and the identification $\epsilon = 2\,l_p$, the classical horizon temperature becomes $T_{\text{cl}} = c^3 \epsilon^2 \kappa / (8\pi G k_B) = c^3 (4\,l_p^2) \kappa / (8\pi G k_B) = \hbar \kappa / (2\pi c k_B)$ — the standard Gibbons-Hawking temperature [17] exactly. This recovery is guaranteed by construction (it is the self-consistency condition of Step 4), but verifying it confirms the algebraic consistency of the derivation.

---

## 7. DISSOLUTION OF THE COSMOLOGICAL CONSTANT PROBLEM

### 7.1 The Two Levels of Description

The cosmological constant problem [2, 3, 18] — the $10^{122}$-fold discrepancy between the QFT prediction for vacuum energy density and the observed value — is often called the worst prediction in physics. Its resolution turns on recognizing that the classical substratum and the emergent quantum description give different — and independently self-consistent — answers to the same question.

**From finite-dimensional QM to QFT.** The theorem of Part I delivers quantum mechanics on a finite-dimensional Hilbert space. The connection to quantum field theory is direct: the finiteness condition discretizes the visible sector into $N = A/\epsilon^2$ independent cells, each coupled to the hidden sector through the partition boundary. The emergent quantum description assigns each cell a finite-dimensional Hilbert space; the tensor product over all cells is a lattice-regularized quantum field theory with a built-in ultraviolet cutoff at the discreteness scale $\epsilon = 2\,l_p$. The zero-point energy $\frac{1}{2}\hbar\omega$ per mode and the mode sum to the Planck cutoff that produce the standard QFT vacuum energy density are properties of this finite-dimensional emergent description — not of the classical substratum. The cutoff is not imposed by hand but is a consequence of the partition geometry.

**The classical substratum** (what geometric measurements probe): The cosmological horizon has a classical thermal equilibrium. By the Friedmann equation, $H^2 = (8\pi G/3)\rho$, the horizon area $A = 4\pi c^2/H^2$ adjusts self-consistently so that the mean energy density matches the critical density $\rho_{\text{crit}} = 3H^2 c^2/(8\pi G)$. The classical energy per mode is $k_B T_H$. There is no zero-point energy and no discrepancy. The total vacuum energy density is at the critical scale $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$ — precisely what is observed.

**The emergent QFT** (what local quantum measurements probe): Quantum field theory assigns a zero-point energy of $\frac{1}{2}\hbar\omega$ per mode. Summing to the Planck cutoff yields $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4 \sim 10^{113}$ J/m$^3$.

### 7.2 Why Gravity Sees the Classical Value

Spacetime geometry is part of the classical substratum (Axiom 2): the metric tensor is defined on the fundamental phase space and evolves via Einstein's field equations *before* the trace-out that produces quantum mechanics. The stress-energy tensor that sources the Einstein equations is the classical stress-energy of the total microstate, not the expectation value of an emergent quantum operator. The $10^{113}$ J/m$^3$ zero-point energy exists in the observer's informational ledger — it is a consequence of re-describing the classical noise as quantum fluctuations — but it does not appear in the stress-energy tensor that governs the geometry. The semiclassical gravity equation $G_{\mu\nu} = 8\pi G \langle \hat{T}_{\mu\nu} \rangle$ is itself an emergent approximation, valid when the quantum description is treated as fundamental. Within the present framework, where the quantum description is derived, the gravitational field equations operate at the classical level and never encounter the zero-point sum.

**Circularity and ontological commitment.** One might object that placing geometry in the classical substratum *assumes* the conclusion — that the framework is constructed so that gravity never encounters quantum vacuum energy. The response is that the ordering is not a free choice but follows from the logical structure of the derivation. The causal partition that produces quantum mechanics is defined by null geodesics of the metric (§4.1); the metric must therefore exist prior to the partition, and hence prior to the quantum description the partition generates. Reversing this ordering — treating the metric as emergent from quantum mechanics — would make the partition definition circular. This logical priority — classical spacetime geometry is fundamental, quantum mechanics is emergent — is a specific ontological commitment, opposite to programs that treat the metric as emergent (canonical quantum gravity, asymptotic safety, string-theoretic emergent spacetime). The ordering question has observable consequences, and the CC problem is one of them. Any framework in which the quantum description is logically prior to the metric will necessarily treat the zero-point sum as a source term in the gravitational field equations, because the stress-energy tensor is constructed from quantum operators. The $10^{122}$ discrepancy is then a real problem requiring cancellation or fine-tuning. In the present framework, where the metric is logically prior, the zero-point sum is an artifact of the emergent description and never enters the stress-energy tensor. The dissolution of the CC problem is a direct prediction of the logical priority commitment, not a separate result.

**Quantum corrections to gravity.** The claim is not that gravity is immune to quantum effects. The emergent quantum description does feed back into the gravitational dynamics through state-level quantities: §8.1 derives dark energy evolution in Running Vacuum form precisely because the emergent vacuum energy — a state-level property of the quantum description — depends on the Hubble parameter through the hidden sector's volume. This $H$-dependent running of $\Lambda_{\text{eff}}$ *is* a quantum correction to gravity. What the framework excludes is the zero-point sum — a property of the correspondence itself rather than of any particular state — as a gravitational source. The structural/volumetric distinction of §5.2 applies here too: the action scale $\hbar$ (structural) does not gravitate; the vacuum energy (volumetric, state-dependent) does, but at the classical scale $\rho \sim H^2/G$ rather than the QFT scale $\rho \sim M_{\text{Pl}}^4$.

### 7.3 The Structural Origin of the $10^{122}$ Discrepancy

The $10^{122}$ factor has a precise structural interpretation. Summing the emergent zero-point energies to the Planck cutoff:

$$\rho_{\text{QFT}} \sim \int_0^{\omega_{\text{Pl}}} \frac{1}{2}\hbar\omega \cdot g(\omega) \, d\omega \sim M_{\text{Pl}}^4$$

The ratio to the classical result is:

$$\frac{\rho_{\text{QFT}}}{\rho_{\text{classical}}} \sim \frac{M_{\text{Pl}}^4}{H^2/G} = S_{\text{dS}}$$

The discrepancy equals $S_{\text{dS}} = A/(4\,l_p^2)$ — the Bekenstein-Hawking entropy of the cosmological horizon, now identified as the number of independent modes on the partition boundary ($N_{\text{modes}} = A/\epsilon^2 = S_{\text{dS}}$). This is the information compression ratio of the quantum description: the number of hidden-sector degrees of freedom that the trace-out compresses into the emergent quantum state. The "worst prediction in physics" is the entropy of the observer's blind spot — a category error, not a fine-tuning failure.

That this discrepancy cannot be resolved from within is confirmed by Wolpert's (2008) limits of inference [19]: any physical subsystem whose state is a deterministic, many-to-one function of the total configuration is subject to absolute inferential limits. Both geometric measurements (classical substratum) and local particle measurements (emergent QFT) are faithful to their respective descriptions; no embedded observer can determine from within which is more fundamental. Meanwhile, the observed value $\rho_\Lambda \sim 6 \times 10^{-10}$ J/m$^3$ is inferred from the expansion history — a classical geometric measurement reflecting $\rho \sim H^2/G \sim \rho_{\text{crit}}$, with $\rho_\Lambda / \rho_{\text{crit}} \approx 0.7$. The vacuum component is the residual energy density after matter has diluted, its value set by the current epoch's horizon geometry. No fine-tuning is required.

---

## 8. PREDICTIONS AND TESTS

### 8.1 Dark Energy Evolution in Running Vacuum Form

The action scale $\hbar$ depends only on structural properties of the partition boundary and is independent of $H$ (§5.2). But the emergent vacuum energy is a state-level quantity, not a property of the correspondence itself, and it does depend on the hidden sector's volume. The horizon area $A = 4\pi c^2/H^2$ evolves with the Hubble parameter. Since the hidden sector's dimensionality $N_{\text{modes}} = A/\epsilon^2$ depends on $H$, the emergent vacuum energy inherits a dependence on $H$. Expanding $\Lambda_{\text{eff}}(H)$ around the present epoch:

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu_{\text{OI}}}{8\pi G}(H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

where $\nu_{\text{OI}}$ is a dimensionless coefficient encoding the rate at which the hidden-sector dimensionality responds to changes in $H$. This is precisely the form of the Running Vacuum Model (RVM) [20, 21]. The framework constrains $\nu_{\text{OI}}$ in two ways without computing its exact value.

*Sign.* The framework requires $\nu_{\text{OI}} > 0$: as $H$ decreases, the horizon area grows, the hidden sector gains capacity, and the effective cosmological constant decreases. This sign prediction is unambiguous — it follows directly from the monotonic relationship between $H$ and $N_{\text{modes}}$.

*Magnitude.* Condition (C3) requires $N_H / N_V \gg 1$: the hidden sector must have vastly more degrees of freedom than the visible sector, so that visible-sector transitions do not appreciably perturb the hidden-sector state. This means the fractional change in the emergent description per unit change in $N_{\text{modes}}$ must be small — if each added mode materially altered the trace-out, the hidden sector would be effectively saturated and (C3) would be violated. The coefficient $\nu_{\text{OI}}$ measures precisely this fractional response, so (C3) requires $\nu_{\text{OI}} \ll 1$. For comparison, Solà Peracaula, Gómez-Valent, and de Cruz Pérez [21] fit the RVM to CMB, BAO, and SNIa data and consistently obtain $\nu_{\text{eff}} \sim \mathcal{O}(10^{-3})$, with the ΛCDM value $\nu = 0$ disfavored at $3$–$4\sigma$ in several dataset combinations. The framework's prediction — $\nu_{\text{OI}} > 0$ and $\nu_{\text{OI}} \ll 1$ — is consistent with this phenomenological range, though pinning the value to $\mathcal{O}(10^{-3})$ specifically requires the non-perturbative calculation identified as the principal open computational problem.

DESI's 2024–2025 data releases [22] report evidence for evolving dark energy at $2.8\sigma$–$4.2\sigma$, with $w_0 > -1$ and $w_a < 0$ — the qualitative signature the RVM predicts. A non-perturbative calculation of $\nu_{\text{OI}}$ from the horizon's spectral response to changes in $H$ would convert the present qualitative consistency into a quantitative test.

### 8.2 Gravitational Wave Echoes

A black hole horizon represents a regime where the causal partition differs from the cosmological one. For an observer near the horizon, degrees of freedom that are part of the cosmological visible sector become locally inaccessible — reclassified from visible to hidden sector as they cross the horizon. The effective partition shifts, and the emergent description must shift accordingly.

At a proper distance $\sim \epsilon$ outside a black hole horizon $r_h$, the local wavelength of an infalling mode reaches $\epsilon$ — the discreteness floor. The mode has no kinematically accessible states at shorter wavelengths and must scatter back. The predicted time delay is:

$$\Delta t_{\text{echo}} \approx \frac{r_h}{c} \ln\left(\frac{r_h}{2\,l_p}\right)$$

For a $30 M_\odot$ remnant with $\epsilon = 2\,l_p$, the logarithmic dependence on $\epsilon$ makes this prediction insensitive to the exact value: replacing $l_p$ with $2\,l_p$ shifts the delay by $\ln 2 \cdot r_h/c \approx 0.1$ ms, well within the $\sim 54$ ms timescale [23]. The exact reflection amplitude requires non-perturbative calculation. The echo signal, if detected, would constitute direct evidence that the discreteness scale $\epsilon$ identified by the self-consistency argument (§6) has observable consequences at horizons other than the cosmological one — a regime where the partition-relativity of the emergent description (§3.4) becomes empirically accessible.

### 8.3 Conjunction as Discriminant

The conjunction of confirmed dark energy evolution *and* detected GW echoes would uniquely favor an information-theoretic origin over standard QFT-derived RVMs, which predict $\Lambda(H)$ running but have no mechanism for discreteness-scale echoes. Each prediction alone is compatible with other frameworks; their joint confirmation would be distinctive.

---

## 9. CONCLUSION

Two results at different levels of generality have been established.

**The general theorem (Part I).** Under three axioms (deterministic dynamics, a causal partition, and classical probability), a finiteness condition on the effective configuration space, and three conditions on the hidden sector (non-zero coupling, inverted timescale separation, and sufficient capacity), the embedded observer's reduced description of the visible sector is necessarily quantum mechanics. The Schrödinger equation, the Born rule, and Bell inequality violations are structural consequences. The action scale $\hbar$ is uniquely determined by the local structural properties of the partition boundary. No quantum postulates are required.

**The cosmological application (Part II).** The cosmological horizon provides a physical realization where the sharp-partition approximation is exact and all three conditions are satisfied. The theorem yields: (a) the exact value $\hbar = c^3 \epsilon^2 / (4G)$ from partition-relativity, the structural/volumetric distinction, dimensional analysis, and thermal self-consistency, with $\epsilon = 2\,l_p$ and the Bekenstein-Hawking entropy formula $S = A/(4\,l_p^2)$ recovered as consequences; (b) a dissolution of the cosmological constant problem, the $10^{122}$ discrepancy identified as $S_{\text{dS}}$; and (c) falsifiable predictions including dark energy evolution in RVM form and gravitational wave echoes.

**Assumptions and limitations of the theorem:**
*The finiteness condition* is an independent assumption in Part I. In Part II, the cosmological horizon's finite area provides finiteness through the partition geometry, so it is not an additional assumption in the physical application. The theorem is silent on systems where neither an intrinsic discreteness scale nor a finite-area partition boundary ensures finite-dimensionality.
*Barandes' stochastic-quantum correspondence* is the mathematical engine of the theorem, entering at a single step (§3.1). Its proof rests on the Stinespring dilation theorem and has been independently corroborated (§3.4).

**Assumptions and limitations of the application:**
*The value $\hbar = c^3 \epsilon^2 / (4G)$* follows from partition-relativity, the structural/volumetric distinction, dimensional analysis, and thermal self-consistency (§5.2, Steps 1–4). The thermal self-consistency argument uses the Gibbons-Hawking temperature, which is a consequence of the emergent QM applied to the horizon geometry; the logic is sequential (gap-equation structure), not circular. A stronger result — that the Schur-Hadamard gauge freedom is fully resolved by the process tensor alone, without appeal to the Gibbons-Hawking temperature — is conjectured (§5.3) but not proven; this conjecture is not required for the determination of $\hbar$.
*The echo prediction* relies on a kinematic argument; the exact reflection amplitude requires non-perturbative calculation.
*The coefficient $\nu_{\text{OI}}$* governing dark energy evolution is constrained to be positive and small ($\nu_{\text{OI}} \ll 1$) by the framework's internal logic (§8.1), consistent with phenomenological fits at $\mathcal{O}(10^{-3})$. Its exact value requires non-perturbative methods applied to the horizon's spectral response.

**What would falsify each part independently:**
The *theorem* would be falsified by a proof that P-divisibility can be maintained under conditions (C1)–(C3), or by a restriction of Barandes' correspondence that excludes the class of processes generated here.
The *application* would be falsified by the definitive absence of dark energy evolution in precision cosmological surveys, or by the confirmed absence of gravitational wave echoes at the predicted timescale, while leaving the theorem intact.

---

## DECLARATION OF AI-ASSISTED TECHNOLOGIES
During the preparation of this work, the author used **Claude Opus 4.6 (Anthropic)** and **Gemini 3.1 Pro (Google)** to assist in drafting, refining argumentation, and verifying bibliographic details. The author reviewed and edited the content and takes full responsibility for the publication.

---

## REFERENCES
[1] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).
[2] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).
[3] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).
[4] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).
[5] P. Pechukas, "Reduced dynamics need not be completely positive," *Phys. Rev. Lett.* **73**, 1060 (1994).
[6] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Entanglement and non-Markovianity of quantum evolutions," *Phys. Rev. Lett.* **105**, 050403 (2010).
[7] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014).
[8] F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, and K. Modi, "Operational Markov condition for quantum processes," *Phys. Rev. Lett.* **120**, 040405 (2018).
[9] P. Strasberg and M. Esposito, "Stochastic thermodynamics in the strong coupling regime: An unambiguous approach based on coarse graining," *Phys. Rev. E* **95**, 062101 (2017).
[10] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).
[11] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).
[12] S. Calvo, "On the Stochastic-Quantum Correspondence," arXiv:2601.18720 (2026).
[13] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195–200 (1964).
[14] J. A. Barandes, S. Hasan, and J. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).
[15] T. Le, F. A. Pollock, T. Paterek, M. Paternostro, and K. Modi, "Divisible quantum dynamics satisfies temporal Tsirelson's bound," *J. Phys. A* **50**, 055302 (2017).
[16] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995).
[17] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).
[18] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).
[19] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008).
[20] J. Solà Peracaula, "The cosmological constant problem and running vacuum in the expanding universe," *Phil. Trans. R. Soc. A* **380**, 20210182 (2022).
[21] J. Solà Peracaula, A. Gómez-Valent, and J. de Cruz Pérez, "Running vacuum in the Universe," *Universe* **9**, 262 (2023).
[22] DESI Collaboration, "DESI 2024 VI: Cosmological Constraints from BAO," arXiv:2404.03002 (2024).
[23] J. Abedi, H. Dykaar, and N. Afshordi, "Echoes from the Abyss," *Phys. Rev. D* **96**, 082004 (2017).
[24] A. Fine, "Hidden Variables, Joint Probability, and the Bell Inequalities," *Phys. Rev. Lett.* **48**, 291 (1982).
[25] L. S. Pimenta, "Divisible and indivisible Stochastic-Quantum dynamics," arXiv:2505.08785 (2025).
[26] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095 (2026).
[27] N. Bao, S. M. Carroll, and A. Singh, "The Hilbert space of quantum gravity is locally finite-dimensional," *Int. J. Mod. Phys. D* **26**, 1743013 (2017).
[28] W. G. Unruh, "Sonic analogue of black holes and the effects of high frequencies on black hole evaporation," *Phys. Rev. D* **51**, 2827 (1995).
[29] K. Fredenhagen and R. Haag, "On the derivation of Hawking radiation associated with the formation of a black hole," *Commun. Math. Phys.* **127**, 273–284 (1990).
