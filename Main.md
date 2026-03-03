# THE UNDECIDABILITY OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

We prove that an observer embedded in a deterministic system with a finite phase space, whose dynamics are partitioned into a visible sector and a slowly coupled hidden sector of sufficient capacity, necessarily describes the visible sector using quantum mechanics. The hidden sector's persistent correlations render the visible-sector stochastic process P-indivisible. By Barandes' stochastic-quantum correspondence, P-indivisible stochastic processes are mathematically equivalent to unitarily evolving quantum mechanics. The Schrödinger equation, the Born rule, and Bell inequality violations emerge as structural consequences; the action scale $\hbar$ is set by the noise intensity of the trace-out. No quantum postulates are assumed.

We argue that the cosmological horizon of our universe provides a physical realization of the theorem's conditions. Applying the framework to de Sitter spacetime, we derive $\hbar$ from classical general relativity and the phase-space discreteness scale, and dissolve the cosmological constant problem: the $10^{122}$ discrepancy between the QFT vacuum energy prediction and observation equals $S_{\text{dS}}$ — the information compression ratio of the emergent quantum description — exposing it as a category error rather than a fine-tuning failure. Falsifiable predictions include dark energy evolution in Running Vacuum Model form ($\Lambda_{\text{eff}} = \Lambda_0 + \nu H^2$, testable by DESI, Euclid, and the Vera Rubin Observatory) and gravitational wave echoes near black hole horizons.

---

# PART I: THE GENERAL THEOREM

## 1. INTRODUCTION

### 1.1 The Problem of Embedded Observation

Physical observers are subsystems of the systems they measure. This elementary fact has consequences that have not been fully traced. An observer embedded in a deterministic universe cannot access the complete state: degrees of freedom beyond the observer's causal reach are permanently hidden, and the observer's description of the visible sector is necessarily a reduced one obtained by marginalizing over the hidden sector. This paper asks what structural constraints that reduction imposes on the form of the observer's physical laws.

The observer's epistemic situation has been foregrounded before. QBism treats quantum states as expressions of an agent's beliefs; relational quantum mechanics defines states relative to interacting subsystems; 't Hooft's cellular automaton interpretation [41] derives quantum behavior from deterministic dynamics through information loss. These programs take observer-dependence as an interpretive starting point or, in 't Hooft's case, derive it from a specific microphysical model. The present work differs in that it identifies *sufficient conditions* under which any embedded observer in any deterministic system necessarily sees quantum mechanics, independent of the system's specific physical content.

### 1.2 Axioms

The framework rests on three axioms. None reference quantum mechanics, general relativity, or any specific physical theory.

1. **Deterministic dynamics on a finite phase space.** The total system evolves deterministically on a phase space $\Gamma$ with a finite minimal cell volume determined by a discreteness scale $\epsilon$. The phase-space density $\rho(q, p, t)$ evolves via the Liouville equation:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\} \equiv \mathcal{L}\rho$$

where $\mathcal{L}$ is the Liouville operator and $\{\cdot, \cdot\}$ denotes the Poisson bracket.

2. **Causal partition.** $\Gamma$ is partitioned into a visible sector $\Gamma_V$ accessible to the observer and a hidden sector $\Gamma_H$ that is not:

$$\Gamma = \Gamma_V \times \Gamma_H$$

The partition is fixed on timescales relevant to the observer (it may drift on much longer timescales, but such drift is not required for the theorem). The total Hamiltonian decomposes as:

$$H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

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

The Markovian limit for reduced dynamics requires a strict timescale separation $\tau_B \ll \tau_S$ [19], where the environment decorrelates much faster than the system evolves. Condition (C2) inverts this hierarchy: $\tau_S \ll \tau_B$. The hidden sector evolves on timescales far exceeding those of any visible-sector process, so its correlations do not decorrelate between successive system transitions. The memory kernel of the reduced dynamics is effectively constant over all observationally relevant timescales.

It is important to distinguish a slow bath from a static external field. A genuinely static (decoupled) hidden sector would merely shift Hamiltonian parameters in $H_V$ without inducing information backflow. By condition (C1), the hidden sector is not decoupled: the interaction Hamiltonian $H_{\text{int}}$ is continuously active. During each visible-sector transition, $H_{\text{int}}$ imprints the identity of the transition onto the hidden-sector state. Because the hidden sector is slow — not static — these imprints persist without being thermally overwritten: the hidden sector's internal relaxation timescale ($\tau_B$) vastly exceeds the interval between successive visible-sector transitions ($\tau_S$). On subsequent transitions, the coupling reads back the stored correlations, producing transition probabilities that depend on the system's prior trajectory. This is the non-Markovian open-systems regime described by Breuer and Petruccione [19]: an environment that is too slow to decorrelate between system events, yet dynamically coupled strongly enough to mediate persistent system-environment correlations.

### 2.3 P-Indivisibility

*Claim.* Under conditions (C1)–(C3), the stochastic process defined in §2.1 is P-indivisible: its transition matrices cannot be factored through intermediate times as products of valid stochastic matrices.

The argument proceeds in two steps.

**Step 1: Persistent system-environment correlations.** By §2.2, the hidden sector is dynamically coupled to the visible sector via $H_{\text{int}}$ and retains correlations over all timescales relevant to visible-sector observations. Consider three times $t_0 < t_1 < t_2$ with $t_2 - t_0 \ll \tau_B$. At $t_0$, the full state is $(x_i, h_0) \in \Gamma_V \times \Gamma_H$. During $[t_0, t_1]$, the deterministic dynamics produce a full state $(x_j, h_1)$. Because $t_1 - t_0 \ll \tau_B$, the hidden-sector state $h_1$ has not decorrelated: it retains detailed correlations with the system's trajectory during $[t_0, t_1]$, and in particular with the identity of $x_i$. The joint state $(x_j, h_1)$ at $t_1$ is therefore not a product of independent marginals.

**Step 2: Correlated intermediate states break P-divisibility.** That system-environment correlations at intermediate times generically prevent the reduced dynamics from being P-divisible is a convergent conclusion of several independent lines of work:

(a) Pechukas [46] proved that the reduced dynamics of a system in contact with a reservoir need not preserve positivity when the system-environment state is correlated at the initial time of the propagation step. 

(b) Rivas, Huelga, and Plenio [48, 49] formalized the connection between divisibility failure and information backflow. Their RHP criterion established that a dynamical process is non-Markovian in the divisibility sense if and only if information flows back from the environment to the system. 

(c) Pollock, Rodríguez-Rosario, Frauenheim, Paternostro, and Modi [50] derived a necessary and sufficient condition for a process to be Markovian — the process tensor framework — that coincides with the classical definition in the appropriate limit. 

(d) Strasberg and Esposito [51] studied the classical analogue directly: a composite classical system $X \otimes Y$ where $Y$ evolves more slowly than $X$. They demonstrated that the reduced dynamics of $X$ become non-Markovian precisely when the timescale separation departs from the standard Markovian regime — the regime defined by condition (C2).

**Physical mechanism.** During $[t_1, t_2]$, the transition from $x_j$ to $x_k$ depends on the hidden-sector state at $t_1$. The marginalized transition probability $T_{jk}(t_2, t_1)$ averages over *all* hidden-sector states compatible with $x_j$ at $t_1$. But the actual hidden-sector state $h_1$ is not drawn from this generic distribution — it was deterministically produced from $(x_i, h_0)$ and carries a memory of $x_i$. Therefore:

$$P(x_k, t_2 \mid x_j, t_1; x_i, t_0) \neq P(x_k, t_2 \mid x_j, t_1)$$

Since a single stochastic matrix $T(t_2, t_1)$ cannot simultaneously reproduce the correct conditional probabilities for different initial states, the factorization $T(t_2, t_0) = T(t_2, t_1) \cdot T(t_1, t_0)$ with a valid stochastic $T(t_2, t_1)$ must fail. The matrix $\Lambda(t_2, t_1) = T(t_2, t_0) \cdot [T(t_1, t_0)]^{-1}$, if it exists, has negative entries.

**The process is P-indivisible.** $\square$

### 2.4 The Entropic Basis of Memory Persistence

The role of condition (C3) — sufficient capacity — deserves emphasis. The hidden sector's ability to sustain persistent correlations depends on its information capacity relative to the visible sector's demand on it. Each visible-sector transition imprints correlations into the hidden sector via $H_{\text{int}}$. If the hidden sector has insufficient degrees of freedom, successive imprints eventually overwrite earlier ones — the hidden sector saturates, its effective memory is erased, and the reduced dynamics cross over to Markovian behavior. The P-indivisibility that generates quantum mechanics would dissolve.

Condition (C3) prevents this. When $N_H \gg N_V$, the cumulative imprint of all visible-sector transitions over any relevant timescale occupies a negligible fraction of the hidden sector's state space. The hidden sector is never saturated; correlations accumulate without overwriting. This is what guarantees the slow-bath regime holds: it is not merely a question of timescales (C2) but of capacity (C3). A fast bath with vast capacity would still decorrelate; a slow bath with insufficient capacity would eventually forget. Only the conjunction of slow dynamics *and* sufficient capacity sustains the persistent correlations required for P-indivisibility.

---

## 3. THE EMERGENCE OF QUANTUM MECHANICS

### 3.1 The Stochastic-Quantum Correspondence

By Barandes' stochastic-quantum correspondence [13, 14], any indivisible stochastic process on a finite configuration space of size $n$ can be embedded into a unitarily evolving quantum system on a Hilbert space of dimension $\leq n^3$. The P-indivisible stochastic process established in §2.3 satisfies the theorem's hypotheses. The correspondence guarantees the existence of a Hilbert space, a unitary evolution operator, and projection operators such that the quantum system's Born-rule probabilities reproduce all transition probabilities of the classical stochastic process.

Three features of quantum mechanics emerge from this correspondence. The Schrödinger equation is the unique time-evolution law, arising from the differentiability of the unitary in time. The action scale $\hbar$ is set by the noise intensity of the trace-out — the conversion factor between the classical noise spectrum and the quantum phase rotation rate. Its specific numerical value depends on the physical properties of the hidden sector and is not computed here; what the theorem establishes is that such a scale necessarily exists. The Born rule is not an additional postulate but the equilibrium distribution of the indivisible stochastic process [13, 14].

**Finite-dimensionality.** Barandes' proof is established for finite-dimensional configuration spaces. Axiom 1 guarantees applicability: the finite minimal cell volume ensures that any finite spatial region contains at most a finite number of independent cells, and the causal partition (Axiom 2) restricts the visible sector to a finite total volume. The effective configuration space is therefore finite-dimensional at every stage. Calvo [45] has extended the correspondence to infinite-dimensional systems, suggesting the finite-dimensionality requirement may be relaxable, but the extension is not required here.

### 3.2 Bell Inequality Violations

The framework is a hidden variable theory: quantum randomness arises epistemically from ignorance of hidden-sector degrees of freedom rather than fundamental indeterminacy. Bell's theorem [10] rules out *local* hidden variable theories — those satisfying the factorizability condition:

$$P(a, b \mid x, y, \lambda) = P(a \mid x, \lambda) \cdot P(b \mid y, \lambda)$$

where $\lambda$ denotes hidden variables with distribution $\rho(\lambda)$, and $x, y$ are measurement settings assumed statistically independent of $\lambda$. The present framework evades Bell's theorem not by violating measurement independence (superdeterminism) but by violating factorizability through a mechanism that is nonetheless *causally local* — no superluminal signaling occurs.

**The mechanism: non-factorizable joint dynamics from a shared causal past.** Consider two subsystems $Q$ and $R$ that interact locally at preparation time $t'$ and are subsequently separated to spacelike-distant measurement stations. In the stochastic-quantum framework [13, 14, 15], the preparation interaction creates a *joint* transition matrix $T_{QR}(t_2, t_1)$ on the composite configuration space $\mathcal{C}_Q \times \mathcal{C}_R$. Because the joint process is P-indivisible (§2.3), this transition matrix does not factorize:

$$T_{QR} \neq T_Q \otimes T_R$$

This non-factorizability *is* entanglement, expressed at the stochastic level. The correlations are encoded in the *form of the dynamical law itself* — in the structure of the joint transition matrix — rather than in a hidden variable $\lambda$ over which one could integrate and apply screening-off. Since the process is indivisible, there are no well-defined intermediate conditional probabilities that would permit the factorization Bell's theorem requires. Reichenbach's common-cause principle does not apply to indivisible processes, because the principle presupposes that conditioning on the complete common cause renders the effects independent — a decomposition that indivisibility explicitly forbids.

**Causal locality without Bell locality.** The Jarrett decomposition splits Bell's factorizability condition into *parameter independence* (PI) and *outcome independence* (OI). Quantum mechanics violates OI while preserving PI. The present framework reproduces this structure. Barandes, Hasan, and Kagan [15] formalize causal locality as a marginalization condition on the joint transition matrix: for subsystems $Q$ and $R$ at spacelike separation,

$$\sum_{r} T_{(q,r),(q_0,r_0)}(t) = T_{q,q_0}^{(Q)}(t) \quad \forall \, r_0$$

Marginalizing over $R$'s final configuration yields $Q$'s transition probabilities independent of $R$'s initial configuration. The joint transition matrix carries non-factorizable correlations from the shared preparation, but these correlations are accessible only through joint statistics, never through local marginals.

**The Tsirelson bound from indivisibility plus causal locality.** Barandes, Hasan, and Kagan [15] prove that the conjunction of indivisibility and causal locality restricts the maximum CHSH correlator to exactly Tsirelson's bound:

$$|S| \leq 2\sqrt{2}$$

Divisible (classical) stochastic processes satisfy $|S| \leq 2$, reproducing Bell's bound. PR-box correlations ($|S| = 4$) cannot be realized because the required transition matrices have no unitary square root. This result receives independent support from Le et al. [16], who prove the temporal analogue: *divisible* quantum dynamics satisfies the temporal Tsirelson bound, while *indivisible* dynamics can exceed it.

**Measurement independence and the distinction from superdeterminism.** The framework preserves measurement independence by construction: the transition probabilities $T_{ij}(t_2, t_1)$ are defined independently of the initial distribution, and measurement settings enter through which subsystem couplings are activated, not through pre-established correlations with the prepared state. Superdeterministic theories evade Bell's theorem by violating this independence; the present framework instead violates outcome independence — the P-indivisible dynamics propagate preparation correlations forward as a single, non-factorizable transition. This distinction has empirical content: superdeterministic theories generically predict deviations from standard statistical mechanics, while the present framework predicts none.

**Physical picture.** Two entangled particles share a joint transition matrix forged during their local interaction at preparation. When they separate to spacelike-distant stations, the joint matrix's non-factorizability persists — not because information travels between the stations, but because the dynamical law established at preparation cannot be decomposed through intermediate times (indivisibility) or through a product of independent single-party laws (non-factorizability). The hidden sector's persistent correlations (§2.2–2.3) are the physical origin of the joint matrix's indivisibility: the slow environment retains a memory of the preparation interaction that prevents the joint dynamics from being screened off at any intermediate time. Bell inequality violations are a *consequence* of the same non-Markovian structure that generates quantum mechanics in the first place.

### 3.3 Interpretive Consequences

The theorem resolves several foundational puzzles as direct consequences rather than additional postulates.

**The double-slit experiment.** The particle traverses a single slit, and opening or closing the second slit alters the boundary conditions, modifying the effective potential that guides the particle's trajectory. The interference pattern arises from the P-indivisible structure of the transition probabilities — the transition matrix from source to screen depends on the global boundary conditions (both slits), not just on the local path (one slit).

**Wigner's friend.** Inside the laboratory, the Friend's measurement produces a definite outcome driven by the indivisible dynamics selecting a specific trajectory. Wigner, lacking access to the Friend's realized trajectory, must describe the laboratory using the marginal state obtained by tracing out the lab's internal degrees of freedom. His superposition assignment reflects this epistemic deficit, not the Friend's physical state. There is no contradiction because the two descriptions operate at different levels of coarse-graining over the same underlying deterministic evolution.

**The Everettian measure problem.** The total system evolves deterministically as a single continuous reality. The Schrödinger equation is a mandatory compression algorithm for an observer who cannot track the hidden-sector degrees of freedom. The Born rule is the equilibrium distribution of the indivisible stochastic process [13, 14]. "Branches" are features of the compressed description, not of the underlying dynamics. The hierarchy is: deterministic total dynamics → quantum visible-sector dynamics (via trace-out) → classical macroscopic dynamics (via local decoherence).

### 3.4 Scope, Limitations, and Relation to Prior Work

**What the theorem says.** If a system satisfies Axioms 1–3 and conditions (C1)–(C3), the embedded observer's reduced description is quantum mechanics. The Schrödinger equation, Born rule, and Bell inequality violations are structural consequences of the reduction, not independent postulates.

**What the theorem does not say.** It does not identify which physical systems satisfy the conditions. That is an empirical question. It does not derive the numerical value of $\hbar$ for any specific system — only that an action scale set by the trace-out noise necessarily exists. These questions are addressed for a specific physical realization in Part II.

**Dependence on Barandes' correspondence.** The theorem inherits the status of Barandes' proof. If the stochastic-quantum correspondence is refined or restricted, the theorem's scope changes accordingly. Calvo's extension to infinite-dimensional systems [45] suggests the framework is robust to generalizations, but the finite-dimensional case is sufficient for the present argument.

**Relation to 't Hooft's deterministic quantum mechanics.** The present theorem shares a structural kinship with 't Hooft's program [41], which also derives quantum behavior from underlying deterministic dynamics through information loss. Both programs make identical philosophical commitments — quantum randomness is epistemic, arising from coarse-graining a deterministic substratum. They differ in the mechanism of information loss: 't Hooft locates it at the Planck scale (local, cell-by-cell coarse-graining of a fast substratum), while the present framework locates it at the causal partition (global, trace-out of a slow environment). The critical empirical distinction is that 't Hooft's program requires superdeterminism to accommodate Bell violations, while the present framework reproduces them through P-indivisibility without violating measurement independence (§3.2). This constitutes a genuine empirical disagreement testable through precision tests of measurement independence in Bell experiments.

**The question that motivates Part II.** The theorem establishes that *any* system satisfying conditions (C1)–(C3) produces quantum mechanics for the embedded observer. We now ask: does our universe satisfy these conditions?

---

# PART II: THE COSMOLOGICAL APPLICATION

We argue that the cosmological horizon of a de Sitter universe provides a physical realization of conditions (C1)–(C3), and derive the quantitative consequences.

## 4. THE COSMOLOGICAL HORIZON AS SLOW BATH

### 4.1 Phase-Space Partition by Causal Horizons

General relativity provides the physical mechanism that implements the causal partition of Axiom 2. Einstein's field equations define the causal structure of spacetime: the cosmological horizon and the interiors of black holes constitute regions from which no signal can reach the embedded observer. These causally disconnected regions define the hidden sector $\Gamma_H$.

The partition evolves as modes migrate across the horizon at a rate $\dot{H}/H^2 \approx -0.45$ per Hubble time — a timescale of order $1/H \sim 10^{17}$ s. For any laboratory process ($\tau_S \ll 1/H$), the partition is effectively frozen, and the stochastic process of §2.1 is defined with respect to a fixed partition at each epoch. The slow drift of the partition over cosmological timescales will drive the running vacuum energy prediction of §6.1.

The interaction Hamiltonian $H_{\text{int}}$ is non-zero: stress-energy conservation across the horizon enforces correlations between the visible and hidden sectors. **Condition (C1) is satisfied.**

### 4.2 Verification of the Slow-Bath Conditions

**Condition (C2): Timescale separation.** The hidden sector's correlation time is $\tau_B \sim 1/H \sim 10^{17}$ s. For laboratory-scale matter ($\omega \gg H$), the visible sector's dynamical timescale is $\tau_S \sim 1/\omega \sim 10^{-15}$ s. The hierarchy is inverted by approximately 32 orders of magnitude: $\tau_S / \tau_B \sim 10^{-32}$. The Markovian approximation fails categorically. The slow-bath mechanism described in §2.2 — imprint, persist, read back — operates with overwhelming timescale separation. **Condition (C2) is satisfied.**

**Condition (C3): Sufficient capacity.** The hidden sector has $N_{\text{modes}} = A/\epsilon^2$ independent degrees of freedom, where $A$ is the horizon area. As will be established in §4.5, $\epsilon^2 = 4\pi l_p^2$, giving $N_{\text{modes}} = S_{\text{dS}}/\pi \sim 10^{122}$. No laboratory process — involving at most $\sim 10^{80}$ baryons — can appreciably perturb this reservoir. The hidden sector is never saturated. **Condition (C3) is satisfied.**

**Backreaction from correlation imprinting.** The continuous imprinting of visible-sector correlations into the hidden sector via $H_{\text{int}}$ constitutes an information flux into the horizon. In general relativity, horizon entropy and area are linked, so a legitimate concern is whether this flux causes the horizon area to grow and backreacts on the Hubble parameter. The effect is negligible: the cumulative information imprinted by all baryonic processes in the observable universe over a Hubble time involves at most $\sim 10^{80}$ degrees of freedom, while the horizon stores $\sim 10^{122}$ modes. The perturbation is suppressed by a factor of $N_V / N_H \sim 10^{-42}$. The macroscopic horizon area — and hence $H$ — is stable to visible-sector imprinting at a level far below any observable threshold. The cosmological evolution of $H$ (which drives the running vacuum prediction of §6.1) is governed by the Friedmann equation's response to the mean energy density, not by the microphysical correlation exchange.

**All three conditions are satisfied. The theorem of Part I applies: the embedded observer necessarily describes the visible sector using quantum mechanics.** The following sections derive the quantitative consequences specific to this realization.

### 4.3 Quantitative Support: Mori-Zwanzig and the Analytical Memory Kernel

The theorem guarantees P-indivisibility from conditions (C1)–(C3) regardless of the specific form of the coupling. To confirm the quantitative character of the non-Markovian dynamics for the cosmological realization, we model the system analytically using the classical Mori-Zwanzig (MZ) formalism [11, 12]. We map the visible sector to a continuous degree of freedom $(q, p)$ and the hidden-sector cosmological horizon to an infinite bath of classical harmonic oscillators $(x_\alpha, p_\alpha)$ via the Caldeira-Leggett Hamiltonian:

$$H_{\text{tot}} = \frac{p^2}{2m} + V(q) + \sum_\alpha \left[ \frac{p_\alpha^2}{2m_\alpha} + \frac{1}{2}m_\alpha \omega_\alpha^2 \left( x_\alpha - \frac{c_\alpha}{m_\alpha \omega_\alpha^2} q \right)^2 \right]$$

Applying the MZ projection operator yields the exact Generalized Langevin Equation:

$$m\ddot{q} + V'(q) + m \int_0^t \gamma(t-\tau) \dot{q}(\tau) \, d\tau = F(t)$$

The memory kernel $\gamma(t)$ is determined by the bath's spectral density $J(\omega)$ via a cosine transform. For the cosmological horizon, the spectrum is strongly sub-ohmic: $J(\omega) = \frac{\eta H}{\pi} e^{-\omega/\omega_c}$, with a UV cutoff $\omega_c \sim c/l_p$ at the discreteness floor and an IR cutoff at $\omega_{\text{IR}} = H$ (the bath cannot support modes with periods longer than the Hubble time). Evaluating the asymptotics for laboratory timescales ($Ht \ll 1$, $\omega_c t \gg 1$) yields:

$$\gamma(t) \approx -\frac{2 \eta H}{m \pi^2} \left[ \gamma_E + \ln(H t) \right]$$

The memory kernel decays logarithmically, not exponentially. Over the duration of a laboratory experiment $\Delta t$, the relative change in the memory kernel is proportional to $\ln(1 + \Delta t/t) \approx 0$. The bath dynamically stores information via the continuous coupling but does not forget it, providing the exact non-Markovian information backflow required to break P-divisibility.

**The entropic basis of memory persistence.** The logarithmic persistence of $\gamma(t)$ is not a coincidence of the spectral model — it is underwritten by the information capacity of the hidden sector. The cosmological horizon has $N_{\text{modes}} = A/\epsilon^2$ independent degrees of freedom ($S_{\text{dS}}/\pi \sim 10^{122}$ after the identification of §4.5). Each visible-sector transition imprints correlations into the bath via $H_{\text{int}}$, but the bath has $\sim 10^{122}$ modes available to absorb these imprints. No laboratory process — involving at most $\sim 10^{80}$ baryons over $\sim 10^{18}$ s — can appreciably disturb this reservoir. The bath is never saturated; the imprinted correlations are never thermally overwritten. A bath with fewer degrees of freedom would eventually exhaust its storage capacity, and the memory kernel would cross over from logarithmic to exponential decay — restoring Markovianity and dissolving the P-indivisibility that generates quantum mechanics. It is the vastness of $S_{\text{dS}}$ that guarantees the slow-bath regime holds for every physical process below the Hubble scale. This same entropy will reappear in §5.4 as the information compression ratio between the classical and quantum descriptions of vacuum energy — the $10^{122}$ factor of the cosmological constant problem. The connection is not accidental: $S_{\text{dS}}$ simultaneously governs why the bath remembers (sustaining quantum mechanics), why $\hbar$ takes the value it does (setting the noise intensity, as derived next), and why the two descriptions of vacuum energy diverge by exactly this factor.

**A note on model dependence.** The Caldeira-Leggett Hamiltonian with bilinear coupling is a tractable model, not a claim about the exact form of $H_{\text{int}}$ at the cosmological horizon. The logarithmic persistence of the memory kernel follows from the sub-ohmic IR structure of the spectral density, which is set by the finite horizon area — a geometric fact independent of the coupling form. The specific decay coefficients, however, are model-dependent and require the non-perturbative methods outlined in §6.4.

### 4.4 Derivation of the Emergent Action Scale ($\hbar$)

The theorem of Part I establishes that an action scale $\hbar$ necessarily exists, set by the noise intensity of the trace-out. We now compute its value for the cosmological realization.

In the classical MZ formalism, the noise intensity of the visible sector is governed by the classical Fluctuation-Dissipation Theorem. The power spectral density $S_F(\omega)$ of the fluctuating force $F(t)$ is:

$$S_F^{\text{class}}(\omega) = \frac{2 m k_B T_{\text{cl}} J(\omega)}{\omega}$$

Under the stochastic-quantum correspondence, the classical thermal noise of the hidden sector *is* the emergent quantum zero-point noise of the visible sector. In standard quantum mechanics, zero-point noise at $T=0$ has a spectral density:

$$S_F^{\text{quantum}}(\omega) = m \hbar \omega \frac{J(\omega)}{\omega} = m \hbar J(\omega)$$

To determine the effective action scale $\hbar$, we equate the classical horizon noise with the emergent quantum zero-point noise at the characteristic crossover scale of the bath ($\omega = H$):

$$S_F^{\text{class}}(H) \approx S_F^{\text{quantum}}(H)$$
$$2 m k_B T_{\text{cl}} \frac{J(H)}{H} = m \hbar J(H)$$

The masses and spectral densities cancel, yielding:

$$\hbar = \frac{2 k_B T_{\text{cl}}}{H}$$

**Why $\omega = H$ is the unique matching scale.** The spectral density $J(\omega) = \eta H/\pi$ is physically undefined below $\omega = H$: the finite size and age of the universe prohibit bath modes with periods longer than the Hubble time. The scale $H$ is therefore the infrared boundary at which the bath's spectral density turns on — not a free parameter in the matching but the only frequency intrinsic to the bath. Moreover, $H$ is the only frequency constructible from the classical axioms alone ($G$, $c$, $H$, $\epsilon$, $k_B$) that also appears in the quantum noise spectrum; any other matching scale would require importing a frequency external to the framework.

Using the dimensionally exact classical horizon temperature $k_B T_{\text{cl}} = \frac{c^3 \epsilon^2 H}{8\pi G}$ (derived purely from GR thermodynamic identities in §5.2), we substitute to find:

$$\hbar = \frac{c^3 \epsilon^2}{4\pi G}$$

The framework derives the reduced Planck constant purely from classical general relativity ($G, c$) and the phase-space discreteness scale ($\epsilon$). $\hbar$ is formally reduced to a derived parameter of the emergent regime.

### 4.5 Self-Consistency: $\epsilon = l_p$

Rearranging the result of §4.4 ($\hbar = \frac{c^3 \epsilon^2}{4\pi G}$), we solve for the free parameter $\epsilon$:

$$\epsilon^2 = 4\pi \frac{\hbar G}{c^3} = 4\pi l_p^2$$

The framework predicts that the geometric discreteness scale $\epsilon$ exactly matches the Planck length (up to a $4\pi$ geometric prefactor corresponding to the minimal cell solid angle). This identification is not merely aesthetic but mathematical: if $\epsilon^2 < 4\pi l_p^2$, sub-Planckian subcells would be dynamically active yet unresolvable, creating a second trace-out with its own noise intensity and breaking the single-valuedness of $\hbar$; if $\epsilon^2 > 4\pi l_p^2$, the emergent description would assign distinct quantum states to configurations that are physically identical in the substratum. The only self-consistent identification is $\epsilon^2 = 4\pi l_p^2$: one degree of freedom per minimal cell, one source of emergent stochasticity, one $\hbar$.

With this identification, the number of independent modes on the cosmological horizon is:

$$N_{\text{modes}} = \frac{A}{\epsilon^2} = \frac{A}{4\pi l_p^2} = \frac{S_{\text{dS}}}{\pi}$$

where $S_{\text{dS}} \sim 10^{122}$ is the Bekenstein-Hawking entropy of the de Sitter horizon — now computed as a *consequence* of the emergent quantum description, not assumed as an input.

---

## 5. DISSOLUTION OF THE COSMOLOGICAL CONSTANT PROBLEM

### 5.1 The Two Levels of Description

The cosmological constant problem [1, 2, 3] — the $10^{122}$-fold discrepancy between the QFT prediction for vacuum energy density and the observed value — is often called the worst prediction in physics. The resolution turns on recognizing that the classical substratum and the emergent quantum description give different — and independently self-consistent — answers to the same question:

**The classical substratum** (what geometric measurements probe): The cosmological horizon has a classical thermal equilibrium. The horizon area adjusts self-consistently via the Friedmann equation so that the mean energy density matches the critical density $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$. There is no zero-point energy and no discrepancy.

**The emergent QFT** (what local quantum measurements probe): Quantum field theory introduces a zero-point energy of $\frac{1}{2}\hbar\omega$ per mode. Summing these to the Planck cutoff yields $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4 \sim 10^{113}$ J/m$^3$.

**Why gravity sees the classical value.** A natural objection is: if the embedded observer is trapped in the emergent quantum description, why does the gravitational field couple to the classical substratum value ($\rho \sim H^2/G$) rather than the emergent QFT value ($\rho_{\text{QFT}} \sim M_{\text{Pl}}^4$)? The answer follows from the framework's logical architecture rather than an additional assumption. Spacetime geometry is part of the classical substratum (Axiom 2): the metric tensor is defined on the fundamental phase space and evolves via Einstein's field equations *before* the trace-out that produces quantum mechanics. The stress-energy tensor that sources the Einstein equations is therefore the classical stress-energy of the total microstate, not the expectation value of an emergent quantum operator. The $10^{113}$ J/m$^3$ zero-point energy exists in the observer's informational ledger — it is a consequence of re-describing the classical noise as quantum fluctuations — but it does not appear in the stress-energy tensor that governs the geometry. The semiclassical gravity equation $G_{\mu\nu} = 8\pi G \langle \hat{T}_{\mu\nu} \rangle$ is itself an emergent approximation, valid when the quantum description is treated as fundamental. Within the present framework, where the quantum description is derived, the gravitational field equations operate at the classical level and never encounter the zero-point sum.

### 5.2 Classical Horizon Temperature

In the classical substratum, the cosmological constant problem does not arise. The cosmological horizon has $N_{\text{modes}} = A/\epsilon^2$ classical modes. At classical thermal equilibrium, each mode carries energy $\sim k_B T_H$, where $T_H$ is the classical thermodynamic temperature at which the horizon bath is in equilibrium with its own gravitational field.

Jacobson (1995) [39] demonstrated that Einstein's field equations can be derived from the thermodynamic relation $dE = T \, dS$ applied to local causal horizons. The thermodynamic identity relates mass-energy to area via $dE = \frac{c^2 \kappa}{8\pi G} dA$. Since the classical entropy density is $\eta = 1/\epsilon^2$, we have $dS = dA/\epsilon^2$. Equating $dE = T_{\text{cl}} dS$ fixes the classical temperature:

$$T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G k_B}$$

For the de Sitter horizon, $\kappa = c H$. The classical temperature depends on $G$, $c$, $H$, $\epsilon$, and $k_B$ — no $\hbar$. After the emergence of quantum mechanics and the self-consistency identification $\epsilon^2 = 4\pi l_p^2$, we recover $T_{\text{cl}} = \hbar \kappa / (2\pi k_B c)$, the standard Gibbons-Hawking temperature. This recovery is a consistency check: the quantum temperature is a consequence of the framework, not an input to it.

### 5.3 Friedmann Self-Consistency and the Absence of Zero-Point Energy

The total bath energy density is:

$$\rho_V = \frac{N_{\text{modes}} \cdot k_B T_H}{V_{\text{Hubble}}}$$

By the Friedmann equation, $H^2 = (8\pi G/3)\rho$, the horizon area $A = 4\pi c^2/H^2$ adjusts self-consistently so that the mean energy density $\langle \rho \rangle$ matches the critical density $\rho_{\text{crit}} = 3H^2c^2/(8\pi G)$. This is not a prediction — it is the content of the Friedmann equation. The horizon IS the geometric response to the mean energy density.

Crucially, the classical energy per mode is $k_B T_H$ — NOT $\frac{1}{2}\hbar \omega$. In the classical substratum, there is no zero-point energy, and the total vacuum energy density is at the critical scale $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$ — precisely what is observed. **The cosmological constant problem does not exist in the classical substratum. It is an artifact of the emergent quantum description.**

### 5.4 The Origin of the $10^{122}$ Discrepancy

The $10^{122}$ factor has a precise structural interpretation. Summing the emergent zero-point energies to the Planck cutoff yields:

$$\rho_{\text{QFT}} \sim \int_0^{\omega_{\text{Pl}}} \frac{1}{2}\hbar\omega \cdot g(\omega) \, d\omega \sim M_{\text{Pl}}^4$$

The ratio of this to the classical result is:

$$\frac{\rho_{\text{QFT}}}{\rho_{\text{classical}}} \sim \frac{M_{\text{Pl}}^4}{H^2/G} \sim S_{\text{dS}}$$

The discrepancy equals $S_{\text{dS}} \sim 10^{122}$ — the Bekenstein-Hawking entropy of the cosmological horizon. This is the **information compression ratio** of the quantum description.

### 5.5 Wolpert's Limits and Observational Undecidability

Wolpert's (2008) limits of inference [4] confirm that the discrepancy between the classical and quantum estimates cannot be resolved by any embedded observer. Wolpert proved that any physical subsystem whose state is a deterministic, many-to-one function of the total configuration constitutes an inference device subject to absolute limits. Both geometric measurements (classical substratum) and local particle measurements (emergent QFT) are faithful to their respective descriptions. Wolpert's theorem guarantees that no embedded observer can determine from within which description is "more fundamental."

### 5.6 What the Embedded Observer Measures as $\rho_\Lambda$

The observed value $\rho_\Lambda \sim 6 \times 10^{-10}$ J/m$^3$ is inferred from the expansion history of the universe — a classical geometric measurement that reflects the classical substratum value $\rho \sim H^2/G \sim \rho_{\text{crit}}$, with $\rho_\Lambda / \rho_{\text{crit}} \approx 0.7$. The vacuum component is the residual energy density after matter has diluted, and its value is set by the current epoch's horizon geometry. No fine-tuning is required.

---

## 6. PREDICTIONS AND TESTS

### 6.1 Deriving the Running Vacuum Model

The horizon area $A = 4\pi c^2/H^2$ evolves with the Hubble parameter. Expanding around the present epoch:

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu_{\text{OI}}}{8\pi G}(H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

where $\nu_{\text{OI}}$ is a dimensionless coefficient encoding the rate at which the hidden-sector dimensionality responds to changes in the Hubble parameter. This is precisely the form of the Running Vacuum Model (RVM) [28, 29]. The framework requires $\nu_{\text{OI}} > 0$.

### 6.2 Observational Status and Model Differentiation

DESI's 2024–2025 data releases [26] report evidence for evolving dark energy at $2.8\sigma$–$4.2\sigma$. The conjunction of confirmed dark energy evolution *and* detected GW echoes (§6.3) would uniquely favor an information-theoretic origin over standard QFT-derived RVMs.

### 6.3 Falsifiable Predictions

* **Gravitational Wave Echoes:** At a proper distance $\sim \epsilon$ outside a black hole horizon $r_h$, the local wavelength reaches $\epsilon$ — the discreteness floor. The mode has no kinematically accessible states at shorter wavelengths and must scatter back. The predicted time delay is:
$$\Delta t_{\text{echo}} \approx \frac{r_h}{c} \ln\left(\frac{r_h}{\epsilon}\right)$$
For a $30 M_\odot$ remnant with $\epsilon \sim l_p$, the expected delay is approximately 54 ms.

* **Stochastic Gravitational Noise Floor:** Hidden-sector fluctuations source a continuous stochastic background with an inverse-frequency-squared spectrum in the MHz–GHz band [8].

### 6.4 Decisive Computational Test

The analytical calculation in §4.3 confirms the qualitative logarithmic persistence of the memory kernel within the Caldeira-Leggett model. A fully non-perturbative calculation using tensor-network methods (t-DMRG) [38] or Keldysh FRG is required to determine the exact reflection coefficient for the echoes and precisely fix the coefficient $\nu_{\text{OI}}$ governing dark energy evolution.

---

## 7. FURTHER CONSEQUENCES

### 7.1 Black Hole Information and Singularities

A singularity is what results from extending the visible-sector description past its domain of validity — the same category of error as the cosmological constant problem (§5.4). Information falling past a black hole horizon joins the hidden sector. The thermal Hawking spectrum [25] is the exterior observer's marginal prediction from tracing out the interior, directly analogous to the cosmological trace-out that produces quantum mechanics itself. Recent work on regular black holes from pure gravity [24], Planck stars [22], and string-theoretic resolutions [23] is consistent with this picture: all replace the singular point with a structure that preserves information while rendering it inaccessible to exterior observers.

### 7.2 String Theory and AdS/CFT

The AdS/CFT correspondence [6] achieves exact unification by placing the observer on the asymptotic boundary — an external vantage point immune to Wolpert's limits. Our de Sitter universe has no such boundary; the framework predicts that exact unification requires access to the complete state space, which is prohibited for embedded observers. This does not invalidate string-theoretic results but contextualizes their domain of applicability: AdS/CFT describes what an *external* observer would see, while the present framework describes the structural constraints facing an *internal* one.

### 7.3 Epistemic Consistency

A natural consistency check is whether the framework's own derivation is subject to the undecidability it establishes. The answer is that Wolpert's theorem constrains the reconstruction of the hidden sector's exact microstate, not the measurement of macroscopic thermodynamic quantities derivable from the horizon geometry. The Hubble parameter $H$, the horizon area $A$, and (post-emergence) the Bekenstein-Hawking entropy $S_{\text{dS}}$ are gauge-invariant observables accessible to the embedded observer without requiring trans-horizon information. The dimensionality of the blind spot is precisely measurable; its specific microstate contents are not.

---

## 8. CONCLUSION

This paper has established two results at different levels of generality.

**The general theorem (Part I).** Under three axioms — deterministic dynamics on a finite phase space, a causal partition into visible and hidden sectors, and classical probability — together with three conditions on the hidden sector — non-zero coupling (C1), inverted timescale separation (C2), and sufficient capacity (C3) — the embedded observer's reduced description of the visible sector is necessarily quantum mechanics. The Schrödinger equation, the Born rule, and Bell inequality violations are structural consequences of the reduction. The action scale $\hbar$ is set by the noise intensity of the trace-out. No quantum postulates are required.

**The cosmological application (Part II).** The cosmological horizon of our de Sitter universe satisfies all three conditions. Applying the theorem yields: (a) a derivation of $\hbar$ from classical general relativity and the phase-space discreteness scale, with the self-consistency requirement fixing $\epsilon = l_p$; (b) a dissolution of the cosmological constant problem, with the $10^{122}$ discrepancy identified as $S_{\text{dS}}$ — the information compression ratio of the emergent quantum description; and (c) falsifiable predictions including dark energy evolution in RVM form and gravitational wave echoes near black hole horizons.

**Assumptions and limitations of the theorem:**
*Axiom 1 (finite phase space)* is an assumption, not a derivation. The theorem is silent on systems with continuous, unbounded phase spaces unless an independent argument bounds the effective dimensionality.
*Barandes' stochastic-quantum correspondence* is the mathematical engine of the theorem. Its status is recent (2023–2025) and not yet universally adopted; the theorem inherits this dependence.

**Assumptions and limitations of the application:**
*The Caldeira-Leggett model* used in §4.3 is a tractable approximation. The qualitative logarithmic persistence depends on the sub-ohmic spectral density, but the precise coefficients require non-perturbative calculation (§6.4).
*The echo prediction* relies on a kinematic argument; the exact reflection amplitude has not been calculated.
*The continuum QFT limit* used to generate the $10^{122}$ ratio is physically bounded by the double cutoff, reflecting a tension between finite structural derivations and infinite field-theoretic consistency checks.

**What would falsify each part independently:**
The *theorem* would be falsified by a proof that P-divisibility can be maintained under conditions (C1)–(C3), or by a restriction of Barandes' correspondence that excludes the class of processes generated here.
The *application* would be falsified by the definitive absence of dark energy evolution in precision cosmological surveys, or by the confirmed absence of gravitational wave echoes at the predicted timescale, while leaving the theorem intact.

---

## DECLARATION OF AI-ASSISTED TECHNOLOGIES
During the preparation of this work, the author used **Claude Opus 4.6 (Anthropic)** and **Gemini 3.1 Pro (Google)** to assist in drafting, refining argumentation, executing the analytical Mori-Zwanzig expansion, and verifying bibliographic details. The author reviewed and edited the content and takes full responsibility for the publication.

---

## REFERENCES
[1] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).  
[2] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).  
[3] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).  
[4] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008).  
[5] G. 't Hooft, "Dimensional Reduction in Quantum Gravity," arXiv:gr-qc/9310026 (1993).  
[6] J. Maldacena, "The Large-N Limit of Superconformal Field Theories and Supergravity," *Int. J. Theor. Phys.* **38**, 1113–1133 (1999).  
[7] J. Abedi, H. Dykaar, and N. Afshordi, "Echoes from the Abyss," *Phys. Rev. D* **96**, 082004 (2017).  
[8] A. Arvanitaki and A. A. Geraci, "Detecting High-Frequency Gravitational Waves with Optically Levitated Sensors," *Phys. Rev. Lett.* **110**, 071105 (2013).  
[9] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).  
[10] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195–200 (1964).  
[11] S. Nakajima, "On Quantum Theory of Transport Phenomena," *Prog. Theor. Phys.* **20**, 948–959 (1958).  
[12] R. Zwanzig, "Ensemble Method in the Theory of Irreversibility," *J. Chem. Phys.* **33**, 1338–1341 (1960).  
[13] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).  
[14] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).  
[15] J. A. Barandes, S. Hasan, and J. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).  
[16] T. Le, F. A. Pollock, T. Paterek, M. Paternostro, and K. Modi, "Divisible quantum dynamics satisfies temporal Tsirelson's bound," *J. Phys. A* **50**, 055302 (2017).  
[17] W. G. Unruh, "Notes on black-hole evaporation," *Phys. Rev. D* **14**, 870 (1976).  
[18] Y. Sekino and L. Susskind, "Fast Scramblers," *JHEP* **2008**, 065 (2008).  
[19] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).  
[20] K. Babu et al., "Unfolding system-environment correlation in open quantum systems," *Phys. Rev. Research* **6**, 013243 (2024).  
[21] J. Cotler et al., "Black Holes and Random Matrices," *JHEP* **2017**, 118 (2017).  
[22] C. Rovelli and F. Vidotto, "Planck Stars," *Class. Quantum Grav.* **31**, 045003 (2014).  
[23] A. Wu, Y. Yan, and L. Ying, "Revisiting Schwarzschild black hole singularity through string theory," *Eur. Phys. J. C* **85**, 168 (2025).  
[24] P. Bueno, P. A. Cano, and R. A. Hennigar, "Regular Black Holes from Pure Gravity," *Phys. Lett. B* **861**, 139260 (2025).  
[25] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).  
[26] DESI Collaboration, "DESI 2024 VI: Cosmological Constraints from BAO," arXiv:2404.03002 (2024).  
[27] S. D. H. Hsu, "Entropy bounds and dark energy," *Phys. Lett. B* **594**, 13–16 (2004).  
[28] J. Solà Peracaula, "The cosmological constant problem and running vacuum in the expanding universe," *Phil. Trans. R. Soc. A* **380**, 20210182 (2022).  
[29] J. Solà Peracaula, A. Gómez-Valent, and J. de Cruz Pérez, "Running vacuum in the Universe," *Universe* **9**, 262 (2023).  
[30] C. Moreno-Pulido and J. Solà Peracaula, "Renormalizing the vacuum energy in cosmological spacetime," *Eur. Phys. J. C* **82**, 551 (2022).  
[31] J. de Cruz Pérez, A. Gómez-Valent, and J. Solà Peracaula, "Dynamical Dark Energy models in light of the latest observations," arXiv:2512.20616 (2025).  
[32] L. N. Granda and A. Oliveros, "Infrared cut-off proposal for the holographic density," *Phys. Lett. B* **669**, 275–277 (2008).  
[33] N. E. Mavromatos, S. Basilakos, and J. Solà Peracaula, "Stringy running vacuum model and current tensions in cosmology," *Class. Quantum Grav.* **41**, 015026 (2024).  
[34] G. Kaplanek and C. P. Burgess, "Hot accelerated qubits: decoherence, thermalization, secular growth and reliable late-time predictions," *JHEP* **2020**, 008 (2020).  
[35] G. Kaplanek and C. P. Burgess, "Qubits on the horizon: decoherence and thermalization near black holes," *JHEP* **2021**, 098 (2021).  
[36] G. Kaplanek and C. P. Burgess, "Hot cosmic qubits: late-time de Sitter evolution and critical slowing down," *JHEP* **2020**, 053 (2020).  
[37] R. C. Bradley, "Basic properties of strong mixing conditions," *Prob. Surveys* **2**, 107–144 (2005).  
[38] A. W. Chin et al., "Generalized polaron ansatz for the sub-ohmic spin-boson model," *Phys. Rev. Lett.* **107**, 160601 (2011).  
[39] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995).  
[40] R. C. Tolman, "On the Weight of Heat and Thermal Equilibrium in General Relativity," *Phys. Rev.* **35**, 904 (1930); P. Ehrenfest, "Gleichförmige Rotation starrer Körper und Relativitätstheorie," *Phys. Z.* **10**, 918 (1909).  
[41] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).  
[42] B. Collins and P. Śniady, "Integration with respect to the Haar measure on unitary groups," *Commun. Math. Phys.* **264**, 773–795 (2006).  
[43] A. Trushechkin, "Long-term behaviour in an exactly solvable model of pure decoherence," *Mathematics* **12**(1), 1 (2024).  
[44] F. Otterpohl, F. Nalbach, and M. Thorwart, "Hidden Phase of the Spin-Boson Model," *Phys. Rev. Lett.* **129**, 120406 (2022).
[45] G. Calvo, "Stochastic-Quantum Correspondence for Infinite-Dimensional Systems," arXiv:2601.18720 (2025).
[46] P. Pechukas, "Reduced dynamics need not be completely positive," *Phys. Rev. Lett.* **73**, 1060 (1994).
[47] R. Alicki, "Comment on 'Reduced dynamics need not be completely positive'," *Phys. Rev. Lett.* **75**, 3020 (1995).
[48] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Entanglement and non-Markovianity of quantum evolutions," *Phys. Rev. Lett.* **105**, 050403 (2010).
[49] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014).
[50] F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, and K. Modi, "Operational Markov condition for quantum processes," *Phys. Rev. Lett.* **120**, 040405 (2018).
[51] P. Strasberg and M. Esposito, "Stochastic thermodynamics in the strong coupling regime: An unambiguous approach based on coarse graining," *Phys. Rev. E* **95**, 062101 (2017).
