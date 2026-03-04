# THE UNDECIDABILITY OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

We prove that an observer embedded in a deterministic system with a finite phase space, whose dynamics are partitioned into a visible sector and a slowly coupled hidden sector of sufficient capacity, necessarily describes the visible sector using quantum mechanics. The hidden sector's persistent correlations render the visible-sector stochastic process P-indivisible; by Barandes' stochastic-quantum correspondence, this is mathematically equivalent to unitarily evolving quantum mechanics. The Schrödinger equation, the Born rule, and Bell inequality violations emerge as structural consequences. The action scale $\hbar$ is uniquely determined by the hidden sector's thermodynamic properties. No quantum postulates are assumed.

The cosmological horizon provides a physical realization of the theorem's conditions. Applying the framework to de Sitter spacetime, we derive $\hbar$ from classical general relativity and the phase-space discreteness scale, and dissolve the cosmological constant problem: the $10^{122}$ discrepancy equals $S_{\text{dS}}$, the information compression ratio of the emergent quantum description — a category error, not a fine-tuning failure.

Falsifiable predictions include dark energy evolution in Running Vacuum Model form ($\Lambda_{\text{eff}} = \Lambda_0 + \nu H^2$) and gravitational wave echoes near black hole horizons. No competing framework predicts both.

---

# PART I: THE GENERAL THEOREM

## 1. INTRODUCTION

### 1.1 The Problem of Embedded Observation

Physical observers are subsystems of the systems they measure. This elementary fact has consequences that have not been fully traced. An observer embedded in a deterministic universe cannot access the complete state: degrees of freedom beyond the observer's causal reach are permanently hidden, and the observer's description of the visible sector is necessarily a reduced one obtained by marginalizing over the hidden sector. This paper asks what structural constraints that reduction imposes on the form of the observer's physical laws.

The observer's epistemic situation has been foregrounded before. QBism treats quantum states as expressions of an agent's beliefs; relational quantum mechanics defines states relative to interacting subsystems; 't Hooft's cellular automaton interpretation [1] derives quantum behavior from deterministic dynamics through information loss. These programs take observer-dependence as an interpretive starting point or, in 't Hooft's case, derive it from a specific microphysical model. The present work differs in that it identifies *sufficient conditions* under which any embedded observer in any deterministic system necessarily sees quantum mechanics, independent of the system's specific physical content.

### 1.2 Axioms

The framework rests on three axioms. None reference quantum mechanics, general relativity, or any specific physical theory.

1. **Deterministic dynamics on a finite phase space.** The total system evolves deterministically on a phase space $\Gamma$ with a finite minimal cell volume determined by a discreteness scale $\epsilon$. The phase-space density $\rho(q, p, t)$ evolves via the Liouville equation:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\} \equiv \mathcal{L}\rho$$

where $\mathcal{L}$ is the Liouville operator and $\{\cdot, \cdot\}$ denotes the Poisson bracket. The discreteness scale $\epsilon$ is a free parameter of the axioms — it is not derived from quantum mechanics or any other input. Its value is determined *a posteriori* by the self-consistency argument of §6, which shows that the framework's internal logic pins $\epsilon$ to the Planck length. The axiom requires only that some finite $\epsilon$ exists, which ensures a finite-dimensional configuration space and thereby guarantees the applicability of Barandes' correspondence (§3.1).

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

**Statement of the theorem.** Under Axioms 1–3 and conditions (C1)–(C3), the embedded observer's reduced description of the visible sector is mathematically equivalent to unitarily evolving quantum mechanics. The remainder of Part I constitutes the proof.

---

## 2. EMERGENT STOCHASTICITY AND P-INDIVISIBILITY

### 2.1 Emergent Stochasticity

The total system (visible + hidden sectors) evolves deterministically (Axiom 1). Every phase-space point $(x, h) \in \Gamma_V \times \Gamma_H$ maps to exactly one future point under the Hamiltonian flow. No randomness exists at this level. But the visible sector alone — what the embedded observer accesses — is stochastic. The observer knows $x$ but not $h$. Different hidden-sector states $h_k$ compatible with the same $x$ send $x$ to different visible-sector futures $x'_k$. The observer must assign transition probabilities:

$$T_{ij}(t_2, t_1) \equiv P(x_j, t_2 \mid x_i, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu(h)$$

where $\pi_V$ is the projection onto visible-sector coordinates, $\phi_t$ is the Hamiltonian flow, and $\mu$ is the Liouville measure on $\Gamma_H$. The Liouville measure is the unique choice preserved by the Hamiltonian flow; any alternative measure would evolve under the dynamics, making the marginalized transition probabilities depend on an arbitrary reference time. The transition probabilities — and hence the emergent description — are therefore uniquely determined by the axioms.

This architecture makes the framework a hidden variable theory: the randomness observed by the embedded observer is epistemic, arising from ignorance of hidden-sector degrees of freedom rather than fundamental indeterminacy. The consistency of this structure with Bell's theorem is addressed in §3.2.

### 2.2 The Slow-Bath Regime

The Markovian limit for reduced dynamics requires a strict timescale separation $\tau_B \ll \tau_S$ [4], where the environment decorrelates much faster than the system evolves. Condition (C2) inverts this hierarchy: $\tau_S \ll \tau_B$. The hidden sector evolves on timescales far exceeding those of any visible-sector process, so its correlations do not decorrelate between successive system transitions. The memory kernel of the reduced dynamics is effectively constant over all observationally relevant timescales.

It is important to distinguish a slow bath from a static external field. A genuinely static (decoupled) hidden sector would merely shift Hamiltonian parameters in $H_V$ without inducing information backflow. By condition (C1), the hidden sector is not decoupled: the interaction Hamiltonian $H_{\text{int}}$ is continuously active. During each visible-sector transition, $H_{\text{int}}$ imprints the identity of the transition onto the hidden-sector state. Because the hidden sector is slow — not static — these imprints persist without being thermally overwritten: the hidden sector's internal relaxation timescale ($\tau_B$) vastly exceeds the interval between successive visible-sector transitions ($\tau_S$). On subsequent transitions, the coupling reads back the stored correlations, producing transition probabilities that depend on the system's prior trajectory — the non-Markovian open-systems regime of Breuer and Petruccione [4].

### 2.3 P-Indivisibility

*Claim.* Under conditions (C1)–(C3), the stochastic process defined in §2.1 is P-indivisible: its transition matrices cannot be factored through intermediate times as products of valid stochastic matrices.

**Step 1: Persistent system-environment correlations.** By §2.2, the hidden sector is dynamically coupled to the visible sector via $H_{\text{int}}$ and retains correlations over all timescales relevant to visible-sector observations. Consider three times $t_0 < t_1 < t_2$ with $t_2 - t_0 \ll \tau_B$. At $t_0$, the full state is $(x_i, h_0) \in \Gamma_V \times \Gamma_H$. During $[t_0, t_1]$, the deterministic dynamics produce a full state $(x_j, h_1)$. Because $t_1 - t_0 \ll \tau_B$, the hidden-sector state $h_1$ has not decorrelated: it retains detailed correlations with the system's trajectory during $[t_0, t_1]$, and in particular with the identity of $x_i$. The joint state $(x_j, h_1)$ at $t_1$ is therefore not a product of independent marginals.

**Step 2: Correlated intermediate states break P-divisibility.** During $[t_1, t_2]$, the transition from $x_j$ to $x_k$ depends on the hidden-sector state at $t_1$. The marginalized transition probability $T_{jk}(t_2, t_1)$ averages over *all* hidden-sector states compatible with $x_j$ at $t_1$. But the actual hidden-sector state $h_1$ is not drawn from this generic distribution — it was deterministically produced from $(x_i, h_0)$ and carries a memory of $x_i$. Therefore:

$$P(x_k, t_2 \mid x_j, t_1; x_i, t_0) \neq P(x_k, t_2 \mid x_j, t_1)$$

The future of $x_j$ depends on which past produced it. Since a single stochastic matrix $T(t_2, t_1)$ cannot simultaneously reproduce the correct conditional probabilities for different preparation histories, the factorization $T(t_2, t_0) = T(t_2, t_1) \cdot T(t_1, t_0)$ with a valid stochastic $T(t_2, t_1)$ must fail. The matrix $\Lambda(t_2, t_1) = T(t_2, t_0) \cdot [T(t_1, t_0)]^{-1}$, if it exists, has negative entries.

**The process is P-indivisible.** $\square$

This result is a convergent conclusion of several independent lines of work. Pechukas [5] proved that the reduced dynamics of a system in contact with a correlated reservoir need not preserve positivity. Rivas, Huelga, and Plenio [6, 7] formalized the connection between divisibility failure and information backflow, establishing that a process is non-Markovian in the divisibility sense if and only if information flows back from the environment to the system. Pollock et al. [8] derived a necessary and sufficient Markovianity condition via the process tensor framework. Most directly, Strasberg and Esposito [9] studied the classical analogue — a composite system $X \otimes Y$ where $Y$ evolves more slowly than $X$ — and demonstrated that the reduced dynamics of $X$ become non-Markovian precisely in the regime defined by condition (C2).

### 2.4 The Role of Sufficient Capacity

Condition (C3) is what prevents P-indivisibility from being transient. Each visible-sector transition imprints correlations into the hidden sector via $H_{\text{int}}$. If the hidden sector has insufficient degrees of freedom, successive imprints overwrite earlier ones — the hidden sector saturates, its memory is erased, and the reduced dynamics cross over to Markovian behavior. When $N_H \gg N_V$, the cumulative imprint of all visible-sector transitions occupies a negligible fraction of the hidden sector's state space, and correlations accumulate without overwriting. A fast bath with vast capacity would still decorrelate; a slow bath with insufficient capacity would eventually forget. Only the conjunction of slow dynamics (C2) *and* sufficient capacity (C3) sustains the persistent correlations required for P-indivisibility.

---

## 3. THE EMERGENCE OF QUANTUM MECHANICS

### 3.1 The Stochastic-Quantum Correspondence

By Barandes' stochastic-quantum correspondence [10, 11], any indivisible stochastic process on a finite configuration space of size $n$ can be embedded into a unitarily evolving quantum system on a Hilbert space of dimension $\leq n^3$. The P-indivisible stochastic process established in §2.3 satisfies the theorem's hypotheses. The correspondence guarantees the existence of a Hilbert space, a unitary evolution operator, and projection operators such that the quantum system's Born-rule probabilities reproduce all transition probabilities of the classical stochastic process.

Three features of quantum mechanics emerge from this correspondence. The Schrödinger equation is the unique time-evolution law, arising from the differentiability of the unitary in time. The Born rule is not an additional postulate but the equilibrium distribution of the indivisible stochastic process [10, 11]. The action scale $\hbar$ requires more careful treatment. The correspondence guarantees the existence of a unitary evolution operator $U(t)$, but $U$ is dimensionless; $\hbar$ enters only when one defines the Hamiltonian $\hat{H}(t) \equiv i\hbar \, \partial_t U \cdot U^\dagger$, converting the dimensionless rate of change into energy units. The correspondence itself is silent about the value of this conversion factor — it establishes that a quantum description exists for any P-indivisible process, but not which action scale it carries. What fixes $\hbar$ is the physical content of the partition: the emergent description must be unique for a given partition (§3.4), so the action scale can depend only on quantities intrinsic to the hidden sector. Its specific numerical value is computed for the cosmological realization in Part II (§5).

**Finite-dimensionality.** Barandes' proof is established for finite-dimensional configuration spaces. Axiom 1 guarantees applicability: the finite minimal cell volume ensures that any finite spatial region contains at most a finite number of independent cells, and the causal partition (Axiom 2) restricts the visible sector to a finite total volume. The effective configuration space is therefore finite-dimensional at every stage. Calvo [12] has extended the correspondence to infinite-dimensional systems, suggesting the finite-dimensionality requirement may be relaxable, but the extension is not required here.

### 3.2 Bell Inequality Violations

The framework is a hidden variable theory: quantum randomness arises epistemically from ignorance of hidden-sector degrees of freedom rather than fundamental indeterminacy. Bell's theorem [13] rules out *local* hidden variable theories — those satisfying the factorizability condition:

$$P(a, b \mid x, y, \lambda) = P(a \mid x, \lambda) \cdot P(b \mid y, \lambda)$$

where $\lambda$ denotes hidden variables with distribution $\rho(\lambda)$, and $x, y$ are measurement settings assumed statistically independent of $\lambda$. The present framework evades Bell's theorem not by violating measurement independence (superdeterminism) but by violating factorizability through a mechanism that is nonetheless *causally local* — no superluminal signaling occurs.

**The mechanism: non-factorizable joint dynamics from a shared causal past.** Consider two subsystems $Q$ and $R$ that interact locally at preparation time $t'$ and are subsequently separated to spacelike-distant measurement stations. In the stochastic-quantum framework [10, 11, 14], the preparation interaction creates a *joint* transition matrix $T_{QR}(t_2, t_1)$ on the composite configuration space $\mathcal{C}_Q \times \mathcal{C}_R$. Because the joint process is P-indivisible (§2.3), this transition matrix does not factorize:

$$T_{QR} \neq T_Q \otimes T_R$$

This non-factorizability *is* entanglement, expressed at the stochastic level. The correlations are encoded in the *form of the dynamical law itself* — in the structure of the joint transition matrix — rather than in a hidden variable $\lambda$ over which one could integrate and apply screening-off. Since the process is indivisible, there are no well-defined intermediate conditional probabilities that would permit the factorization Bell's theorem requires. Reichenbach's common-cause principle does not apply to indivisible processes, because the principle presupposes that conditioning on the complete common cause renders the effects independent — a decomposition that indivisibility explicitly forbids.

**Causal locality without Bell locality.** The Jarrett decomposition splits Bell's factorizability condition into *parameter independence* (PI) and *outcome independence* (OI). Quantum mechanics violates OI while preserving PI. The present framework reproduces this structure. Barandes, Hasan, and Kagan [14] formalize causal locality as a marginalization condition on the joint transition matrix: for subsystems $Q$ and $R$ at spacelike separation,

$$\sum_{r} T_{(q,r),(q_0,r_0)}(t) = T_{q,q_0}^{(Q)}(t) \quad \forall \, r_0$$

Marginalizing over $R$'s final configuration yields $Q$'s transition probabilities independent of $R$'s initial configuration. The joint transition matrix carries non-factorizable correlations from the shared preparation, but these correlations are accessible only through joint statistics, never through local marginals.

**The Tsirelson bound from indivisibility plus causal locality.** Barandes, Hasan, and Kagan [14] prove that the conjunction of indivisibility and causal locality restricts the maximum CHSH correlator to exactly Tsirelson's bound:

$$|S| \leq 2\sqrt{2}$$

Divisible (classical) stochastic processes satisfy $|S| \leq 2$, reproducing Bell's bound. PR-box correlations ($|S| = 4$) cannot be realized because the required transition matrices have no unitary square root. This result receives independent support from Le et al. [15], who prove the temporal analogue: *divisible* quantum dynamics satisfies the temporal Tsirelson bound, while *indivisible* dynamics can exceed it.

**Measurement independence and the distinction from superdeterminism.** The framework preserves measurement independence by construction: the transition probabilities $T_{ij}(t_2, t_1)$ are defined independently of the initial distribution, and measurement settings enter through which subsystem couplings are activated, not through pre-established correlations with the prepared state. Superdeterministic theories evade Bell's theorem by violating this independence; the present framework instead violates outcome independence — the P-indivisible dynamics propagate preparation correlations forward as a single, non-factorizable transition. This distinction has empirical content: superdeterministic theories generically predict deviations from standard statistical mechanics, while the present framework predicts none.

**Position in Fine's classification.** Fine's theorem [29] establishes that any model reproducing the quantum statistics for all Bell scenarios must violate either measurement independence or factorizability. The present framework violates factorizability — specifically outcome independence in the Jarrett decomposition — while preserving both measurement independence and parameter independence. This places it squarely in the class Fine's theorem permits: models that reproduce quantum correlations through non-factorizable joint dynamics rather than through conspiracy between hidden variables and measurement settings.

### 3.3 Interpretive Consequences

The theorem resolves several foundational puzzles as direct consequences rather than additional postulates. In the double-slit experiment, the particle traverses a single slit; the interference pattern arises because the transition matrix $T_{ij}(t_2, t_1)$ is computed by marginalizing over the hidden sector, which includes the field configuration near both slits — opening or closing the second slit changes the boundary conditions on these modes, altering the marginalization and hence the pattern. In Wigner's friend scenarios, the Friend's measurement produces a definite outcome via the indivisible dynamics; Wigner's superposition assignment reflects his epistemic deficit from tracing out the lab's internal degrees of freedom, not the Friend's physical state. The Everettian measure problem dissolves because the total system evolves deterministically as a single reality — the Schrödinger equation is a mandatory compression algorithm for an observer who cannot track hidden-sector degrees of freedom, the Born rule is the equilibrium distribution of the indivisible stochastic process [10, 11], and "branches" are features of the compressed description, not of the underlying dynamics.

### 3.4 Scope, Limitations, and Relation to Prior Work

**What the theorem says.** If a system satisfies Axioms 1–3 and conditions (C1)–(C3), the embedded observer's reduced description is quantum mechanics. The Schrödinger equation, Born rule, and Bell inequality violations are structural consequences of the reduction, not independent postulates.

**What the theorem does not say.** It does not identify which physical systems satisfy the conditions. That is an empirical question. It does not derive the numerical value of $\hbar$ for any specific system — only that an action scale set by the trace-out noise necessarily exists. These questions are addressed for a specific physical realization in Part II.

**Partition-relativity of the emergent description.** A consequence of the theorem that deserves explicit statement: the emergent quantum mechanics is relative to the partition. Different partitions — different divisions of the total phase space into visible and hidden sectors — produce different reduced descriptions, potentially with different action scales or, if the conditions (C1)–(C3) are not met for a given partition, no quantum description at all. The theorem does not say "quantum mechanics is the unique description of reality." It says "quantum mechanics is the unique description available to any observer whose causal access defines a partition satisfying (C1)–(C3)."

This is a conditional prediction, not a claim that distinct partitions are generically realized. "Embedded observers cannot access the complete state" is entirely consistent with all observers sharing the *same* inaccessible region — in which case the emergent description is universal, not relative. Partition-relativity becomes physically significant only when distinct observers have distinct causal boundaries. The physical implications of this for our universe — where the causal partition is defined by null geodesics and all sub-$c$ observers share the same horizon — are developed in Part II (§4.1).

**Dependence on Barandes' correspondence.** The theorem inherits the status of Barandes' proof. If the stochastic-quantum correspondence is refined or restricted, the theorem's scope changes accordingly. Calvo's extension to infinite-dimensional systems [12] suggests the framework is robust to generalizations, but the finite-dimensional case is sufficient for the present argument.

**Relation to 't Hooft's deterministic quantum mechanics.** The present theorem shares 't Hooft's philosophical commitment [1] — quantum randomness is epistemic, arising from coarse-graining a deterministic substratum — but differs in mechanism: 't Hooft locates information loss at the Planck scale (local, cell-by-cell coarse-graining of a fast substratum), while the present framework locates it at the causal partition (global, trace-out of a slow environment). The critical empirical distinction is that 't Hooft's program requires superdeterminism to accommodate Bell violations, while the present framework reproduces them through P-indivisibility without violating measurement independence (§3.2).

**The question that motivates Part II.** The theorem establishes that *any* system satisfying conditions (C1)–(C3) produces quantum mechanics for the embedded observer. We now ask: does our universe satisfy these conditions?

---

# PART II: THE COSMOLOGICAL APPLICATION

We argue that the cosmological horizon of a de Sitter universe provides a physical realization of conditions (C1)–(C3), and derive the quantitative consequences. The argument requires only general relativity and the Jacobson thermodynamic identity; no model of the microphysical coupling is assumed.

## 4. THE COSMOLOGICAL HORIZON AS CAUSAL PARTITION

### 4.1 The Partition

General relativity defines the causal structure of spacetime. The cosmological horizon is the boundary beyond which no signal propagating at or below $c$ can reach the embedded observer. Every physically realizable measurement technique — electromagnetic, gravitational-wave, neutrino — propagates at or below $c$ and therefore encounters the same boundary. The horizon implements the causal partition of Axiom 2 for all sub-$c$ observers simultaneously: the visible sector $\Gamma_V$ is the interior of the cosmological horizon, and the hidden sector $\Gamma_H$ is everything beyond it.

This identification is not a modeling choice but a consequence of GR's causal structure. A hypothetical observer with access to a causal channel not constrained by the light cone would have a different partition, a different (or absent) hidden sector, and by the theorem's own logic, a different emergent description. No such channel is available within GR. The specific quantum mechanics we observe is the quantum mechanics of light-cone-bounded observers; its universality is a consequence of the causal structure, not a postulate.

### 4.2 Verification of the Conditions

**Condition (C1): Non-zero coupling.** The cosmological horizon is not a static wall. Stress-energy conservation across the horizon enforces dynamical correlations between the visible and hidden sectors: matter and radiation cross the horizon continuously, and the horizon area responds to changes in the interior energy density via the Friedmann equation. The coupling is bidirectional. **Condition (C1) is satisfied.**

**Condition (C2): Slow-bath timescale separation.** The hidden sector's correlation time is set by the Hubble timescale: $\tau_B \sim 1/H \sim 10^{17}$ s. For any laboratory-scale process with characteristic frequency $\omega \gg H$, the visible sector's dynamical timescale is $\tau_S \sim 1/\omega \sim 10^{-15}$ s or shorter. The ratio is:

$$\frac{\tau_S}{\tau_B} \sim 10^{-32}$$

The hidden sector cannot decorrelate between any pair of visible-sector events. The Markovian approximation fails categorically. **Condition (C2) is satisfied.**

**Condition (C3): Sufficient capacity.** The hidden sector has $N_{\text{modes}} = A/\epsilon^2$ independent degrees of freedom, where $A = 4\pi c^2/H^2$ is the horizon area and $\epsilon$ is the discreteness scale of Axiom 1. For any $\epsilon$ at or above the Planck scale, the horizon area is cosmological ($A \sim 10^{52}$ m$^2$) and the visible sector involves at most $\sim 10^{80}$ baryons. No laboratory process can appreciably perturb the hidden sector's state. The hidden sector is never saturated. **Condition (C3) is satisfied.**

### 4.3 Application of the Theorem

All three axioms hold. All three conditions hold. The theorem of Part I applies: the embedded observer's reduced description of the visible sector is P-indivisible, and by Barandes' stochastic-quantum correspondence [10, 11], mathematically equivalent to unitarily evolving quantum mechanics with an action scale $\hbar$ uniquely determined by the thermodynamic properties of the hidden sector.

*What this step requires:* Part I plus Barandes. No additional physics.

---

## 5. DERIVATION OF THE EMERGENT ACTION SCALE ($\hbar$)

### 5.1 The Classical Horizon Temperature

The theorem guarantees that $\hbar$ exists but does not compute its value. To determine it, we need the thermodynamic properties of the hidden sector that partition-relativity identifies as the sole inputs (§5.2). The required input is model-independent: it follows from Jacobson's thermodynamic derivation of Einstein's field equations [16].

Jacobson (1995) demonstrated that applying the thermodynamic relation $dE = T \, dS$ to local causal horizons yields Einstein's field equations. The same identity relates mass-energy to area via:

$$dE = \frac{c^2 \kappa}{8\pi G} \, dA$$

The classical entropy density on the horizon is $\eta = 1/\epsilon^2$ — one degree of freedom per minimal cell (Axiom 1). Therefore $dS = dA/\epsilon^2$, and equating $dE = T_{\text{cl}} \, dS$ fixes the classical temperature:

$$T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G k_B}$$

For the de Sitter horizon, the surface gravity is $\kappa = cH$, giving:

$$k_B T_{\text{cl}} = \frac{c^3 \epsilon^2 H}{8\pi G}$$

This temperature depends on $G$, $c$, $H$, $\epsilon$, and $k_B$ — no $\hbar$. It is the temperature of the hidden sector as a classical thermal reservoir, derived from the horizon geometry without reference to quantum mechanics.

### 5.2 The Bath's Intrinsic Frequency

The hidden sector has exactly one intrinsic frequency scale: $H$. This is not a free parameter but a geometric fact, selected by three constraints. The matching must occur at a frequency that (i) characterizes the hidden sector rather than any particular visible-sector process, which eliminates all frequencies $\omega \gg H$; (ii) is constructible from the classical quantities available before the emergence of quantum mechanics ($G$, $c$, $H$, $\epsilon$, $k_B$), which eliminates $\hbar$-dependent scales; and (iii) corresponds to a physical mode of the bath, which eliminates sub-Hubble frequencies that have no support on the finite horizon. The only frequency satisfying all three conditions is $H$ itself — the infrared boundary of the bath's mode spectrum.

**The role of partition-relativity in fixing the scale.** The stochastic-quantum correspondence maps the P-indivisible transition matrices to a unitary evolution $U(t)$, but leaves an enormous gauge freedom: the transition matrix constrains only $|U_{ij}|^2$, leaving the quantum phases — and hence the energy eigenvalues and the overall action scale — undetermined. This is the Schur-Hadamard gauge freedom inherent in the stochastic-to-quantum map. Partition-relativity (§3.4) resolves this freedom. The emergent quantum description must be *unique* for a given partition: two observers with identical causal access must obtain the same emergent theory. This means the action scale $\hbar$ can depend only on quantities intrinsic to the partition — the thermodynamic and geometric properties of the hidden sector. For the cosmological partition, the hidden sector contributes exactly two independent quantities with the right dimensions: a thermal energy scale $k_B T_{\text{cl}}$ and a frequency scale $H$. Their ratio $k_B T_{\text{cl}} / H$ has dimensions of action and is the unique combination available. The gauge freedom of the correspondence is resolved not by the correspondence itself but by the physical content of the partition.

### 5.3 Matching the Noise Intensity

The partition-relativity argument of §5.2 establishes that $\hbar$ must be proportional to $k_B T_{\text{cl}} / H$ — the unique combination of partition-intrinsic quantities with dimensions of action. The remaining question is the numerical prefactor. The stochastic-quantum correspondence guarantees that the emergent quantum description assigns each mode at frequency $\omega$ a zero-point energy of $\frac{1}{2}\hbar\omega$. In the classical substratum, each mode at thermal equilibrium carries energy $k_B T_{\text{cl}}$. At the bath's characteristic frequency $\omega = H$, the two descriptions must assign the same noise intensity — otherwise the emergent quantum theory would make predictions about the hidden sector's own characteristic mode that conflict with the classical thermal state from which the theory was derived. This fixes the prefactor:

$$k_B T_{\text{cl}} = \frac{1}{2}\hbar H$$

Solving for $\hbar$:

$$\hbar = \frac{2 k_B T_{\text{cl}}}{H}$$

Substituting the classical horizon temperature from §5.1:

$$\hbar = \frac{c^3 \epsilon^2}{4\pi G}$$

The reduced Planck constant is derived purely from classical general relativity ($G$, $c$) and the phase-space discreteness scale ($\epsilon$). The factor $c^3$ reflects the structural chain: $c$ is the propagation speed that defines the causal boundary, the causal boundary defines the hidden sector, and the hidden sector's thermodynamic properties determine $\hbar$.

*What this step requires:* Jacobson's thermodynamic identity (model-independent, derived from GR), the identification of $H$ as the bath's intrinsic frequency (geometric), partition-relativity (§3.4, which constrains $\hbar$ to depend only on partition-intrinsic quantities), and the self-consistency requirement that the emergent quantum description agree with the classical thermal state at the bath's characteristic frequency. No microphysical coupling model. No spectral density.

### 5.4 Conjecture: Gauge-Fixing From First Principles

The derivation of §5.2–5.3 establishes $\hbar = c^3 \epsilon^2 / 4\pi G$ through partition-relativity (which constrains $\hbar$ to partition-intrinsic quantities), dimensional analysis (which selects the unique combination $k_B T_{\text{cl}} / H$), and self-consistency (which fixes the prefactor). A stronger result — that the Schur-Hadamard gauge freedom is fully resolved by the physical content of the trace-out, without appeal to dimensional analysis — is likely true but not proven here. The following sketch identifies the logical structure such a proof would require and locates the gap.

**Step 1.** The P-indivisible stochastic process generated by the trace-out is not characterized by a single transition matrix $T(t_2, t_1)$ but by the complete hierarchy of multi-time correlation functions. Pollock, Rodríguez-Rosario, Frauenheim, Paternostro, and Modi [8] formalize this as the *process tensor* $\mathcal{T}_{n:0}$ — a multilinear map that takes any sequence of interventions at times $t_0, \ldots, t_n$ and returns the resulting probability distribution. The process tensor contains strictly more information than the set of two-time transition matrices.

**Step 2.** Pollock et al. prove that every process tensor admits a unitary dilation: there exists an environment space $\mathcal{H}_E$, an initial environment state $\rho_E$, and a unitary $U_{\text{tot}}$ on $\mathcal{H}_S \otimes \mathcal{H}_E$ that reproduces all multi-time statistics via partial trace. This is the quantum analogue of the Kolmogorov extension theorem.

**Step 3.** In the present framework, the "environment" is the hidden sector, and its initial state is the Liouville measure restricted to $\Gamma_H$ — a thermal state at $T_{\text{cl}}$ (§5.1). The total dynamics are the deterministic Hamiltonian flow (Axiom 1), which is unique. There is no gauge freedom in the underlying dynamics: the Hamiltonian flow $\phi_t$ on $\Gamma_V \times \Gamma_H$ is a single, deterministic map.

**Step 4.** The process tensor of the visible sector is therefore uniquely determined — it is the partial trace of a unique total unitary acting on a unique initial state. This is not a choice; it is a consequence of Axioms 1 and 2.

**Step 5 (the gap).** Does the unique process tensor determine a unique effective unitary $U_{\text{eff}}(t)$ on the visible sector, including its phases? A single two-time transition matrix $T_{ij} = |U_{ij}|^2$ does not — this is the Schur-Hadamard degeneracy. But the process tensor provides multi-time data: conditional probabilities $P(x_k, t_2 \mid x_j, t_1 \mid x_i, t_0)$ for arbitrary sequences of intermediate configurations. Each additional time point provides new constraints on the phases of $U$, because the composition $U(t_2, t_1) U(t_1, t_0)$ entangles the phases at different times. The conjecture is that for the class of processes arising under conditions (C1)–(C3), the multi-time data is sufficient to break the Schur-Hadamard degeneracy completely, fixing $U_{\text{eff}}(t)$ up to a physically irrelevant global phase — and with it, the action scale $\hbar$.

**Why the conjecture is likely true.** P-indivisibility means precisely that the multi-time statistics *cannot* be reconstructed from two-time data — the process has genuine memory that encodes information beyond $|U_{ij}|^2$. The slow-bath condition (C2) ensures that this memory is persistent: the hidden sector retains correlations across arbitrarily many visible-sector transitions, providing an ever-growing set of phase constraints. The sufficient-capacity condition (C3) ensures that these constraints are independent — they are not recycled through a finite-dimensional bottleneck. A finite number of independent phase constraints drawn from a process with persistent memory and unlimited capacity should generically fix $N^2$ phase functions, leaving at most a global phase.

**What a proof would require.** A rigorous version would need to show that the process tensor of a P-indivisible process generated by a slow thermal bath of sufficient capacity determines the effective unitary up to global phase. This likely requires tools from the process tensor framework [8] combined with the representation theory of the Schur-Hadamard gauge group. The result, if established, would close the last gap between the general theorem and the quantitative derivation of $\hbar$, reducing the dimensional argument of §5.2–5.3 to a corollary of a deeper structural theorem.

*Status: Conjecture. The five-step structure is logically complete; Step 5 requires new mathematics.*

---

## 6. SELF-CONSISTENCY AND THE DISCRETENESS SCALE

The derivation of $\hbar$ in §5.3 is established through partition-relativity, dimensional analysis, and self-consistency — it does not depend on the conjecture of §5.4, which sketches a route to the same result from deeper principles. Taking the result of §5.3 as given and rearranging:

$$\epsilon^2 = 4\pi \frac{\hbar G}{c^3} = 4\pi l_p^2$$

The framework predicts that the geometric discreteness scale $\epsilon$ exactly matches the Planck length (up to a $4\pi$ geometric prefactor corresponding to the minimal cell solid angle). This is not merely aesthetic but necessary for self-consistency: if $\epsilon^2 < 4\pi l_p^2$, sub-Planckian subcells would be dynamically active yet unresolvable, creating a second trace-out with its own noise intensity and breaking the single-valuedness of $\hbar$; if $\epsilon^2 > 4\pi l_p^2$, the emergent description would assign distinct quantum states to configurations that are physically identical in the substratum. The only self-consistent identification is $\epsilon^2 = 4\pi l_p^2$.

With this identification, the number of independent modes on the cosmological horizon is:

$$N_{\text{modes}} = \frac{A}{\epsilon^2} = \frac{A}{4\pi l_p^2} = \frac{S_{\text{dS}}}{\pi}$$

where $S_{\text{dS}} \sim 10^{122}$ is the Bekenstein-Hawking entropy of the de Sitter horizon — now computed as a consequence of the emergent quantum description, not assumed as an input.

**Consistency check.** After the emergence of quantum mechanics and the identification $\epsilon^2 = 4\pi l_p^2$, the classical horizon temperature becomes $T_{\text{cl}} = \hbar \kappa / (2\pi k_B c)$ — the standard Gibbons-Hawking temperature [17]. This recovery is a consequence, not an input.

---

## 7. DISSOLUTION OF THE COSMOLOGICAL CONSTANT PROBLEM

### 7.1 The Two Levels of Description

The cosmological constant problem [2, 3, 18] — the $10^{122}$-fold discrepancy between the QFT prediction for vacuum energy density and the observed value — is often called the worst prediction in physics. Its resolution turns on recognizing that the classical substratum and the emergent quantum description give different — and independently self-consistent — answers to the same question.

**The classical substratum** (what geometric measurements probe): The cosmological horizon has a classical thermal equilibrium. By the Friedmann equation, $H^2 = (8\pi G/3)\rho$, the horizon area $A = 4\pi c^2/H^2$ adjusts self-consistently so that the mean energy density matches the critical density $\rho_{\text{crit}} = 3H^2 c^2/(8\pi G)$. The classical energy per mode is $k_B T_H$. There is no zero-point energy and no discrepancy. The total vacuum energy density is at the critical scale $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$ — precisely what is observed.

**The emergent QFT** (what local quantum measurements probe): Quantum field theory assigns a zero-point energy of $\frac{1}{2}\hbar\omega$ per mode. Summing to the Planck cutoff yields $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4 \sim 10^{113}$ J/m$^3$.

### 7.2 Why Gravity Sees the Classical Value

Spacetime geometry is part of the classical substratum (Axiom 2): the metric tensor is defined on the fundamental phase space and evolves via Einstein's field equations *before* the trace-out that produces quantum mechanics. The stress-energy tensor that sources the Einstein equations is the classical stress-energy of the total microstate, not the expectation value of an emergent quantum operator. The $10^{113}$ J/m$^3$ zero-point energy exists in the observer's informational ledger — it is a consequence of re-describing the classical noise as quantum fluctuations — but it does not appear in the stress-energy tensor that governs the geometry. The semiclassical gravity equation $G_{\mu\nu} = 8\pi G \langle \hat{T}_{\mu\nu} \rangle$ is itself an emergent approximation, valid when the quantum description is treated as fundamental. Within the present framework, where the quantum description is derived, the gravitational field equations operate at the classical level and never encounter the zero-point sum.

**A note on circularity.** One might object that placing geometry in the classical substratum *assumes* the conclusion — that the framework is constructed so that gravity never encounters quantum vacuum energy. The response is that the ordering is not a free choice but follows from the logical structure of the derivation. The causal partition that produces quantum mechanics is defined by null geodesics of the metric (§4.1); the metric must therefore exist prior to the partition, and hence prior to the quantum description the partition generates. Reversing this ordering — treating the metric as emergent from quantum mechanics — would make the partition definition circular, since the partition is what produces quantum mechanics in the first place. The claim is not that gravity *cannot* receive quantum corrections, but that the leading-order gravitational dynamics are logically prior to the quantum description, and the zero-point sum is an artifact of the emergent description rather than a source term in the pre-emergent dynamics.

### 7.3 The Structural Origin of the $10^{122}$ Discrepancy

The $10^{122}$ factor has a precise structural interpretation. Summing the emergent zero-point energies to the Planck cutoff:

$$\rho_{\text{QFT}} \sim \int_0^{\omega_{\text{Pl}}} \frac{1}{2}\hbar\omega \cdot g(\omega) \, d\omega \sim M_{\text{Pl}}^4$$

The ratio to the classical result is:

$$\frac{\rho_{\text{QFT}}}{\rho_{\text{classical}}} \sim \frac{M_{\text{Pl}}^4}{H^2/G} \sim S_{\text{dS}}$$

The discrepancy equals $S_{\text{dS}} \sim 10^{122}$ — the Bekenstein-Hawking entropy of the cosmological horizon. This is the information compression ratio of the quantum description: the number of hidden-sector degrees of freedom that the trace-out compresses into the emergent quantum state. The "worst prediction in physics" is the entropy of the observer's blind spot — a category error, not a fine-tuning failure.

That this discrepancy cannot be resolved from within is confirmed by Wolpert's (2008) limits of inference [19]: any physical subsystem whose state is a deterministic, many-to-one function of the total configuration is subject to absolute inferential limits. Both geometric measurements (classical substratum) and local particle measurements (emergent QFT) are faithful to their respective descriptions; no embedded observer can determine from within which is more fundamental. Meanwhile, the observed value $\rho_\Lambda \sim 6 \times 10^{-10}$ J/m$^3$ is inferred from the expansion history — a classical geometric measurement reflecting $\rho \sim H^2/G \sim \rho_{\text{crit}}$, with $\rho_\Lambda / \rho_{\text{crit}} \approx 0.7$. The vacuum component is the residual energy density after matter has diluted, its value set by the current epoch's horizon geometry. No fine-tuning is required.

---

## 8. PREDICTIONS AND TESTS

### 8.1 Dark Energy Evolution in Running Vacuum Form

The horizon area $A = 4\pi c^2/H^2$ evolves with the Hubble parameter. Since the hidden sector's dimensionality $N_{\text{modes}} = A/\epsilon^2$ depends on $H$, the emergent vacuum energy inherits a dependence on $H$. Expanding $\Lambda_{\text{eff}}(H)$ around the present epoch:

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu_{\text{OI}}}{8\pi G}(H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

where $\nu_{\text{OI}}$ is a dimensionless coefficient encoding the rate at which the hidden-sector dimensionality responds to changes in $H$. This is precisely the form of the Running Vacuum Model (RVM) [20, 21]. The framework requires $\nu_{\text{OI}} > 0$: as $H$ decreases, the horizon area grows, the hidden sector gains capacity, and the effective cosmological constant decreases.

DESI's 2024–2025 data releases [22] report evidence for evolving dark energy at $2.8\sigma$–$4.2\sigma$. A non-perturbative calculation of $\nu_{\text{OI}}$ from the horizon's spectral response to changes in $H$ is required for a precise numerical prediction; this is the principal open computational problem.

### 8.2 Gravitational Wave Echoes

A black hole horizon represents a regime where the causal partition differs from the cosmological one. For an observer near the horizon, degrees of freedom that are part of the cosmological visible sector become locally inaccessible — they are reclassified from visible to hidden sector as they cross the horizon (see §9.1). The effective partition shifts, and the emergent description must shift accordingly.

At a proper distance $\sim \epsilon$ outside a black hole horizon $r_h$, the local wavelength of an infalling mode reaches $\epsilon$ — the discreteness floor. The mode has no kinematically accessible states at shorter wavelengths and must scatter back. The predicted time delay is:

$$\Delta t_{\text{echo}} \approx \frac{r_h}{c} \ln\left(\frac{r_h}{\epsilon}\right)$$

For a $30 M_\odot$ remnant with $\epsilon \sim l_p$, the expected delay is approximately 54 ms [23]. The exact reflection amplitude requires non-perturbative calculation. The echo signal, if detected, would constitute direct evidence that the discreteness scale $\epsilon$ identified by the self-consistency argument (§6) has observable consequences at horizons other than the cosmological one — a regime where the partition-relativity of the emergent description (§3.4) becomes empirically accessible.

### 8.3 Conjunction as Discriminant

The conjunction of confirmed dark energy evolution *and* detected GW echoes would uniquely favor an information-theoretic origin over standard QFT-derived RVMs, which predict $\Lambda(H)$ running but have no mechanism for discreteness-scale echoes. Each prediction alone is compatible with other frameworks; their joint confirmation would be distinctive.

---

## 9. FURTHER CONSEQUENCES

Information falling past a black hole horizon joins the hidden sector. The thermal Hawking spectrum [24] is the exterior observer's marginal prediction from tracing out the interior — directly analogous to the cosmological trace-out that produces quantum mechanics itself. The "information paradox" is reframed: information is not lost but reclassified from visible to hidden sector, and the apparent loss is the same epistemic artifact as quantum indeterminacy. The echo prediction (§8.2) is the observable signature of this reclassification: it marks the proper distance at which the partition boundary enforces the discreteness floor, and its detection would confirm that the same mechanism — partition-dependent emergence — operates at both cosmological and astrophysical horizons. Recent work on regular black holes from pure gravity [25], Planck stars [26], and string-theoretic resolutions [27] is consistent with this picture.

The AdS/CFT correspondence [28] achieves exact unification by placing the observer on the asymptotic boundary — an external vantage point immune to Wolpert's limits. Our de Sitter universe has no such boundary; the framework predicts that exact unification requires access to the complete state space, which is prohibited for embedded observers. This does not invalidate string-theoretic results but contextualizes their domain: AdS/CFT describes what an *external* observer would see, while the present framework describes the structural constraints facing an *internal* one.

---

## 10. CONCLUSION

This paper has established two results at different levels of generality.

**The general theorem (Part I).** Under three axioms (deterministic dynamics on a finite phase space, a causal partition, and classical probability) and three conditions on the hidden sector (non-zero coupling, inverted timescale separation, and sufficient capacity), the embedded observer's reduced description of the visible sector is necessarily quantum mechanics. The Schrödinger equation, the Born rule, and Bell inequality violations are structural consequences. The action scale $\hbar$ is uniquely determined by the hidden sector's thermodynamic properties. No quantum postulates are required.

**The cosmological application (Part II).** The cosmological horizon provides a physical realization where the sharp-partition approximation is exact and all three conditions are satisfied. The theorem yields: (a) a derivation of $\hbar$ from classical GR and the discreteness scale, with self-consistency fixing $\epsilon = l_p$; (b) a dissolution of the cosmological constant problem, the $10^{122}$ discrepancy identified as $S_{\text{dS}}$; and (c) falsifiable predictions including dark energy evolution in RVM form and gravitational wave echoes.

**Assumptions and limitations of the theorem:**
*Axiom 1 (finite phase space)* is an assumption, not a derivation. The theorem is silent on systems with continuous, unbounded phase spaces unless an independent argument bounds the effective dimensionality.
*Barandes' stochastic-quantum correspondence* is the mathematical engine of the theorem. Its status is recent (2023–2025) and not yet universally adopted; the theorem inherits this dependence.

**Assumptions and limitations of the application:**
*The matching at $\omega = H$* is constrained by partition-relativity to the unique combination of partition-intrinsic quantities with dimensions of action ($k_B T_{\text{cl}} / H$), with the prefactor fixed by self-consistency between the classical thermal state and the emergent quantum zero-point energy. §5.4 conjectures that a proof via the process tensor formalism could derive this result from first principles; the key open step is showing that multi-time statistics fully resolve the Schur-Hadamard gauge freedom.
*The echo prediction* relies on a kinematic argument; the exact reflection amplitude requires non-perturbative calculation.
*The coefficient $\nu_{\text{OI}}$* governing dark energy evolution is not computed; its determination requires non-perturbative methods applied to the horizon's spectral response.

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
[12] G. Calvo, "Stochastic-Quantum Correspondence for Infinite-Dimensional Systems," arXiv:2601.18720 (2025).
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
[24] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).
[25] P. Bueno, P. A. Cano, and R. A. Hennigar, "Regular Black Holes from Pure Gravity," *Phys. Lett. B* **861**, 139260 (2025).
[26] C. Rovelli and F. Vidotto, "Planck Stars," *Class. Quantum Grav.* **31**, 045003 (2014).
[27] A. Wu, Y. Yan, and L. Ying, "Revisiting Schwarzschild black hole singularity through string theory," *Eur. Phys. J. C* **85**, 168 (2025).
[28] J. Maldacena, "The Large-N Limit of Superconformal Field Theories and Supergravity," *Int. J. Theor. Phys.* **38**, 1113–1133 (1999).
[29] A. Fine, "Hidden Variables, Joint Probability, and the Bell Inequalities," *Phys. Rev. Lett.* **48**, 291 (1982).
