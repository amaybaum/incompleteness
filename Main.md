# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum
**Date:** February 2026
**Status:** DRAFT PRE-PRINT
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

The incompatibility between quantum mechanics and general relativity is a fundamental consequence of embedded observation. Observers within the universe must access reality through projections that discard causally inaccessible degrees of freedom defined by the structure of spacetime. Applying Wolpert's (2008) inference limits, this paper establishes the Observational Incompleteness Theorem: quantum and gravitational descriptions of vacuum energy are variance-type and mean-type projections of a shared hidden sector, and Wolpert's bounds prohibit their simultaneous determination by any embedded inference device. The $10^{122}$ cosmological constant discrepancy is reinterpreted not as a fine-tuning error but as the quantitative signature of this structural incompleteness — a direct measurement yielding roughly $10^{244}$ hidden-sector degrees of freedom.

Building on this theorem, the Trace-Out Conjecture proposes that quantum mechanics is the inevitable consequence of an embedded observer attempting to describe the dynamics of the visible sector. Assuming only classical Liouville dynamics, classical general relativity (as the source of causal structure), and classical probability theory, the argument shows that marginalizing deterministic dynamics over the correlated hidden sector produces stochastic transition matrices that are generically *indivisible* — by three independent lines of established mathematics (lumpability failure, embeddability geometry, and Mori-Zwanzig memory structure). Barandes' stochastic-quantum correspondence then shows that any indivisible stochastic process is exactly equivalent to a unitary quantum system. Hilbert space, the Born rule, superposition, non-commuting observables, and Bell inequality violations emerge necessarily from classical premises. The framework yields falsifiable experimental predictions, including frequency-dependent gravitational wave echoes at post-merger timescales of order $10^{-5}$–$10^{-4}$ seconds and a stochastic noise floor in the MHz–GHz band anchored to the $10^{122}$ ratio.

---

## 1. THE PROBLEM

### 1.1 The Incompatibility

Quantum mechanics and general relativity are extraordinarily successful yet structurally incompatible. This paper argues that the incompatibility is not a defect requiring unification but a consequence of embedded observation.

### 1.2 The Cosmological Discrepancy

The sharpest manifestation of the QM–GR incompatibility is the **cosmological constant problem**. It concerns the single quantity that both frameworks predict: the energy density of empty space, $\rho_{\text{vac}}$.

**Quantum mechanics** computes the vacuum energy by summing zero-point fluctuations of all quantum field modes up to the Planck scale:

$$\rho_{\text{QM}} \sim \frac{E_{\text{Pl}}^{\,4}}{(\hbar c)^3} \sim 10^{113} \; \text{J/m}^3$$

**General relativity** measures the vacuum energy through its gravitational effect — the accelerated expansion of the universe:

$$\rho_{\text{grav}} = \frac{\Lambda \, c^2}{8\pi G} \sim 6 \times 10^{-10} \; \text{J/m}^3$$

The ratio is conventionally rounded to $10^{120}$ in the literature [2,3,5], or more precisely $10^{122}$. A different interpretation is proposed: **neither calculation is wrong. They disagree because they are answering fundamentally different questions about the same thing.**

---

## 2. OBSERVATIONAL INCOMPLETENESS

### 2.1 Observers Are Embedded

Wolpert (2008) [1] proved that any physical device performing observation, prediction, or recollection — an "inference device" — faces fundamental limits on what it can know about the universe it inhabits. These limits hold **independent of the laws of physics**. They follow solely from the logical structure of a device that is embedded in the system it attempts to describe, forcing any observation to be a surjective, many-to-one mapping from the total state to the device's output. Szangolies (2018) [23] independently developed a related notion of "epistemic horizons" constraining the knowledge available to observers within a physical system.

### 2.2 The Hidden Sector

Let the full state space be partitioned into degrees of freedom accessible to observers (the visible sector) and degrees of freedom that are not (the hidden sector, denoted $\Phi$). The projection discarding the hidden sector is many-to-one.

The hidden sector consists not of exotic particles but of standard degrees of freedom rendered causally inaccessible by spacetime: (i) trans-horizon modes beyond the cosmological horizon, (ii) sub-Planckian degrees of freedom below the observer's resolution limit, (iii) black hole interiors. The partition is defined entirely by classical general relativity — the causal horizon structure is a solution of the Einstein field equations, a classical field theory. No quantum concept enters the definition of what is hidden from the observer.

### 2.3 Two Projections of the Same Thing

The core observation is that quantum field theory and general relativity do not disagree about the vacuum — they probe different statistical properties of the same underlying degrees of freedom.

**Projection 1: The Fluctuation Power Spectrum (QM).** QFT's operational access to the vacuum is through the fluctuation power spectrum — particle creation rates, Casimir forces, Lamb shifts. These are driven by a variance-type sum over all $N$ modes up to the cutoff. Because zero-point energies $\frac{1}{2}\hbar\omega$ are positive-definite — each mode contributes an unsigned magnitude — the sum grows linearly:

$$V \propto \sum_{i=1}^{N} \langle \hat{\phi}_i^2 \rangle \propto N$$

**Projection 2: Mean-Field Pressure (Gravity).** The Einstein field equations couple spacetime curvature to the macroscopic expectation value of the stress-energy tensor. Unlike the variance-type sum, the stress-energy tensor admits cancellations: bosonic and fermionic contributions enter with opposite signs, as do kinetic and gradient terms versus potential terms. The gravitational projection therefore couples to the *net signed mean* of the hidden-sector distribution:

$$M = \langle T_{00} \rangle = \sum_{i=1}^{N} s_i \, |E_i|$$

where $s_i = \pm 1$ reflects the sign of each mode's contribution. Assuming the hidden sector lacks an exact, unbroken global symmetry that would force exact cancellation, the central limit theorem dictates that the macroscopic residual of $N$ quasi-independent contributions scales as:

$$M \sim \sqrt{N}$$

### 2.4 The Physical Inference Devices

In Wolpert's formalism, an inference device is any physical subsystem whose state is dynamically correlated with a target system, enforcing the surjective, many-to-one mapping that triggers inference limits.

**The Quantum Inference Device:** The inference device for the variance-type projection is localized matter interacting with a quantum field. Its output — scattering amplitudes, vacuum fluctuation measurements — sums the unsigned magnitudes of all hidden-sector modes.

**The Gravitational Inference Device:** The local gravitational field itself is the inference device for the mean-type projection. Its output — spacetime curvature — couples to the net signed mean of the hidden-sector stress-energy.

These are not two theories trying to describe the same quantity. They are two distinct physical inference devices, each projecting the hidden sector onto a different statistical target.

### 2.5 The Observational Incompleteness Theorem

> **Observational Incompleteness Theorem.** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. No single embedded inference device can simultaneously determine both the variance-type and mean-type targets of the hidden-sector distribution with joint accuracy exceeding Wolpert's bounds [1].

The theorem states that the QM–GR incompatibility is not a technical failure of either theory but a structural feature of embedded observation. The two descriptions *must* disagree because they are answering fundamentally different questions about the same inaccessible degrees of freedom, and no single device inside the system can answer both questions simultaneously.

---

## 3. THE RATIO AS MEASUREMENT

### 3.1 Extracting the Hidden-Sector Dimensionality

The Observational Incompleteness Theorem reframes the cosmological constant discrepancy as a direct physical measurement. With $N$ independent hidden-sector degrees of freedom, the quantum projection sums all contributions without regard to sign ($V \propto N$) while the gravitational projection couples to the macroscopic mean ($M \sim \sqrt{N}$). Their ratio:

$$\frac{V}{M} \sim \frac{N}{\sqrt{N}} = \sqrt{N}$$

Setting this equal to the observed discrepancy:

$$\sqrt{N} \sim 10^{122} \implies N \sim 10^{244}$$

The $10^{122}$ ratio is not a fine-tuning failure. It is the quantitative signature of observational incompleteness — the universe telling embedded observers, in the starkest numerical terms available, the dimensionality of the sector they cannot access.

### 3.2 Purely Classical Dimensionality

Crucially, deriving $N \sim 10^{244}$ requires no quantum mechanical assumptions. It relies solely on the statistical ratio of variance to mean in a sufficiently complex phase space without global symmetry. The central limit theorem is classical mathematics; the causal horizon is classical general relativity; the partition is classical information theory. The number $10^{244}$ is extracted before any quantum concept enters the argument.

### 3.3 Prior Work

The $\sqrt{N}$ fluctuation scaling has independent precedent. Sorkin (1990–1991) predicted $\Lambda \sim 1/\sqrt{V}$ from Poisson fluctuations in causal set theory — **before the 1998 discovery of accelerating expansion** [24]. Ahmed, Dodelson, Greene, and Sorkin (2004) developed this into the "everpresent $\Lambda$" model [4]. Padmanabhan (2005) independently argued that gravity probes vacuum *fluctuations* rather than the mean [6]. The present framework provides the information-theoretic foundation for why this scaling holds: it is a direct consequence of the Observational Incompleteness Theorem applied to two distinct embedded inference devices.

---

## 4. FROM INCOMPLETENESS TO DYNAMICS

The Observational Incompleteness Theorem establishes that embedded observers face irreducible epistemic constraints when probing the hidden sector. The $10^{122}$ ratio quantifies the scale of these constraints. What follows is a considerably stronger claim: quantum mechanics itself is a consequence of these constraints. This is, on its face, an extraordinary assertion — that the entire quantum formalism, including Hilbert space, the Born rule, and Bell inequality violations, can be derived without assuming any quantum postulate. The claim becomes less surprising, however, once one recognizes a natural question that the Observational Incompleteness Theorem leaves unanswered: if embedded observers are forced to work with incomplete projections of the full state, what kind of *dynamics* do those projections obey? The answer, as the following sections demonstrate, is that the projected dynamics is generically indivisible — and indivisible stochastic dynamics *is* quantum mechanics, by a recent mathematical correspondence due to Barandes. The derivation proceeds from three classical premises through a chain of established mathematical results. No quantum postulate is assumed at any stage.

---

## 5. CLASSICAL PREMISES

The argument rests on three premises, each drawn entirely from established classical physics.

**Premise 1: Classical Statistical Dynamics.** The total universe is a classical statistical system. Its microstate $\gamma = (\gamma_v, \gamma_h)$ lives in a phase space $\Gamma = \Gamma_{\text{vis}} \times \Gamma_{\text{hid}}$ and evolves deterministically via the Liouville equation:

$$\frac{\partial \rho}{\partial t} = \{H, \rho\}$$

The probability density $\rho$ reflects an observer's incomplete knowledge of the microstate, not any fundamental indeterminism. At the level of full microstates, the evolution is reversible, deterministic, and perfectly Markovian.

**Premise 2: Classical General Relativity as Causal Structure.** Einstein's field equations — a classical field theory — determine the causal structure of spacetime. This causal structure creates absolute information barriers: cosmological horizons, sub-Planckian resolution limits from GR's own singularity structure, and black hole event horizons. These are the same barriers that define the hidden sector of Section 2.2, with $N \sim 10^{244}$ causally inaccessible degrees of freedom (Section 3.1). No quantum concept enters their definition.

**Premise 3: Classical Probability Theory.** All statistical inference follows from Kolmogorov's axioms. Observational predictions are classical expectation values. No quantum probability, Hilbert space, or operator algebra is assumed.

---

## 6. MARGINAL TRANSITION PROBABILITIES

### 6.1 The Full Dynamics

Under Premise 1, the full microstate evolves deterministically: given $\gamma(t_0)$, the microstate $\gamma(t)$ at any later time is uniquely determined by Hamilton's equations. Expressed as a stochastic matrix on the full state space, this is a permutation matrix — trivially Markovian and perfectly divisible.

### 6.2 The Observer's Description

The observer cannot track the hidden sector. The observer's operational description of the visible sector is a **marginal stochastic matrix**: the transition probability from an initial visible configuration to a final visible configuration, obtained by integrating the deterministic total evolution over all hidden-sector states weighted by their conditional distribution:

$$T_{ij}(t, t_0) = \int d\gamma_h \; P(\gamma_h \mid v_i, t_0) \; \mathbb{1}\!\left[\Phi_t(v_i, \gamma_h) \in v_j\right]$$

where $\Phi_t$ is the Hamiltonian flow. This marginal matrix $T$ has legitimate stochastic properties: all entries are non-negative and rows sum to one. It is a classical object, derived from classical dynamics and classical probability.

### 6.3 The Central Question

The marginal stochastic matrix inherits its stochastic properties from the underlying deterministic dynamics, but does it inherit their *divisibility*? That is, can $T$ be factored as

$$T(t_2, t_0) = \tilde{T}(t_2, t_1) \cdot T(t_1, t_0)$$

where both intermediate matrices are genuine (entry-wise non-negative) stochastic matrices for all $t_1 \in (t_0, t_2)$?

If yes, the marginal dynamics is P-divisible and admits a classical Markov description. If no — if the marginal dynamics is *indivisible* — then Barandes' theorem (Section 9) guarantees it is exactly equivalent to unitary quantum mechanics.

Everything turns on whether marginalization over the hidden sector preserves or breaks divisibility.

---

## 7. CORRELATIONS ARE INESCAPABLE

The answer to the divisibility question depends critically on whether the visible and hidden sectors are statistically correlated. If they are uncorrelated — if $\rho(\gamma_v, \gamma_h) = \rho_{\text{vis}}(\gamma_v)\rho_{\text{hid}}(\gamma_h)$ — then marginalization can preserve divisibility under special symmetry conditions. If they are correlated, divisibility generically breaks.

This section establishes that correlations are not a modeling choice but an inescapable physical consequence of the classical premises.

### 7.1 Shared Causal History and Non-Factorizability

The visible and hidden sectors share a deep causal past. Prior to cosmological horizon formation, the degrees of freedom now separated by the causal boundary were in direct causal contact, exchanging energy and momentum via classical interactions. Consequently, their joint probability distribution at the time of horizon formation is generically correlated:

$$\rho(\gamma_v, \gamma_h) \neq \rho_{\text{vis}}(\gamma_v)\,\rho_{\text{hid}}(\gamma_h)$$

This is not a fine-tuned initial condition but the generic outcome of interacting Hamiltonian evolution from any non-trivially correlated initial state.

### 7.2 Conservation Laws Enforce Persistent Correlation

The total system obeys exact classical conservation laws. Noether's theorem guarantees conserved charges — total energy, momentum, and angular momentum — that rigidly couple the visible and hidden sectors:

$$E_{\text{total}} = E_v + E_h = \text{const}$$

This exact constraint ensures that the conditional distribution $P(\gamma_h \mid v, t)$ depends non-trivially on the visible state $v$ at all times. The correlation is not a transient feature that could be washed out by dynamical mixing; it is enforced by the symmetry structure of the Hamiltonian itself.

### 7.3 Measure-Zero Factorization

With $N \sim 10^{244}$ hidden-sector degrees of freedom (Section 3.1), the phase space volume is enormous. The set of joint distributions that exactly factorize while simultaneously satisfying all conservation constraints forms a set of measure zero in the space of all allowed distributions. Dynamical evolution under a generic interacting Hamiltonian does not preserve this measure-zero set. The correlation condition is therefore satisfied with probability one.

---

## 8. GENERIC INDIVISIBILITY: THE PROOF ASSEMBLY

This section assembles the central result from three independent lines of established mathematics. Each line individually demonstrates that the marginal stochastic dynamics is generically non-divisible. Together, they establish the result from complementary directions: algebraic (lumpability), geometric (embeddability), and analytic (memory kernels).

### 8.1 Failure of Lumpability (Algebraic)

**Established result (Kemeny-Snell, 1960) [9].** A coarse-grained partition of a Markov chain retains the Markov property if and only if the partition satisfies the *strong lumpability condition*: for every pair of aggregate states $V_i, V_j$, the total transition probability from any microstate within $V_i$ to the aggregate $V_j$ must be identical. In matrix notation:

$$P \cdot \Pi = \Pi \cdot L$$

where $\Pi$ is the lumping matrix, $P$ is the full transition matrix, and $L$ is the lumped matrix.

**Established result (Gurvits and Ledoux, 2005) [10].** The set of stochastic matrices satisfying the strong lumpability condition for a given partition is **nowhere dense** in the space of all stochastic matrices. In any open neighborhood of any stochastic matrix, there exist matrices for which the lumpability condition fails.

**Application.** The observer's marginalization is precisely a lumping: the full state space $\Gamma = \Gamma_{\text{vis}} \times \Gamma_{\text{hid}}$ is projected onto $\Gamma_{\text{vis}}$, aggregating all hidden-sector microstates. For the marginal dynamics to be Markovian (a necessary condition for divisibility), the Kemeny-Snell algebraic identity must hold exactly. But the conservation-law correlations of Section 7.2 ensure that transition probabilities out of a given visible state $v_i$ depend on which hidden-sector microstate the system actually occupies — this violates lumpability. By Gurvits-Ledoux, this violation is the generic case; lumpability is the infinitely fine-tuned exception.

### 8.2 Geometry of Non-Embeddability (Geometric)

**Established result (Elfving, 1937 [11]; Casanellas, Fernández-Sánchez, and Roca-Lacostena, 2023 [12]).** A stochastic matrix $T$ is *embeddable* if there exists a rate matrix $Q$ such that $T = e^{Qt}$ for some $t > 0$. Embeddability is the continuous-time analogue of divisibility: if $T$ is embeddable, it can be factored as $T(t) = T(t,s) \cdot T(s)$ with $T(t,s) = e^{Q(t-s)}$ stochastic for all intermediate $s$.

Elfving showed that embeddability imposes necessary algebraic conditions beyond stochasticity. Casanellas et al. completely solved the embedding problem for matrices up to dimension 4 and proved that the set of embeddable stochastic matrices forms a **proper semi-algebraic subset** of the stochastic simplex — a submanifold of strictly lower dimension for $n \geq 3$.

**Application.** The marginal stochastic matrix $T(t)$ is a smooth function of the Hamiltonian $H$, the initial distribution $\rho_0$, and the elapsed time $t$. This defines a smooth map

$$\mathcal{M}: (H, \rho_0, t) \longmapsto T(t) \in \mathcal{S}_n$$

from the space of Hamiltonians and correlated initial distributions into the stochastic simplex $\mathcal{S}_n$. The embeddable matrices form a proper submanifold $\mathcal{E}_n \subset \mathcal{S}_n$ of positive codimension. By a standard transversality argument: for the image of $\mathcal{M}$ to be confined to $\mathcal{E}_n$, the map would need to satisfy a codimension's worth of algebraic constraints for all parameter values. A generic smooth map from a high-dimensional parameter space into $\mathcal{S}_n$ intersects the lower-dimensional submanifold $\mathcal{E}_n$ on a set of measure zero.

The lumpability analysis of Section 8.1 establishes that $\mathcal{M}$ is non-degenerate: the broken lumpability condition ensures the marginal matrices explore a full-dimensional region of $\mathcal{S}_n$. The two arguments reinforce each other: lumpability failure guarantees sufficient "spread," and the positive-codimension geometry guarantees that a spread-out map generically lands outside the embeddable set.

**Conclusion.** For a visible sector of dimension $n \geq 3$, the marginal stochastic matrix is generically non-embeddable, and therefore generically indivisible.

### 8.3 Memory Kernels and Non-Divisibility (Analytic)

**Established result (Mori, 1965 [7]; Zwanzig, 1960 [8]).** The Mori-Zwanzig projection operator formalism provides an *exact* identity for the projected dynamics of any set of observables in a Hamiltonian system. For observables $A$ restricted to the visible sector:

$$\frac{dA(t)}{dt} = \Omega \, A(t) - \int_0^t K(\tau) \, A(t - \tau) \, d\tau + F(t)$$

where $\Omega$ is a streaming matrix, $K(\tau)$ is a memory kernel encoding the autocorrelation of the orthogonal-dynamics noise, and $F(t)$ is a fluctuating force. The memory integral couples the present rate of change to the entire past history. This is exact, not approximate.

**The Markovian limit requires strict timescale separation.** The memory kernel $K(\tau)$ decays on a timescale $\tau_E$ set by the hidden sector's dynamics. The Markovian limit $K(\tau) \to 2\gamma\,\delta(\tau)$ requires $\tau_E \ll \tau_S$. For a hidden sector sharing conservation laws and causal history with the visible sector, this timescale separation generically fails.

**From memory to indivisibility.** A P-divisible stochastic process is equivalent to one whose generator is a valid rate matrix at every instant — a time-local master equation. The Mori-Zwanzig memory integral is the explicit obstruction to time-locality: it shows the projected dynamics at time $t$ depends on the full trajectory for $s \in [0, t]$. Any faithful discretization produces transition matrices carrying temporal correlations incompatible with P-divisibility.

### 8.4 Complementarity of the Three Lines

| Line | Framework | What it proves | Limitation |
|------|-----------|----------------|------------|
| 1 (Algebraic) | Kemeny-Snell lumpability | Marginal dynamics is generically non-Markovian | Non-Markovianity is necessary but not sufficient for indivisibility |
| 2 (Geometric) | Embeddability theory | Indivisible matrices have full measure in $\mathcal{S}_n$ for $n \geq 3$; generic maps land outside $\mathcal{E}_n$ | Requires the map $\mathcal{M}$ to be non-degenerate (supplied by Line 1) |
| 3 (Analytic) | Mori-Zwanzig projection | Memory kernel provides the explicit physical mechanism for history dependence | Operates on continuous observables, not directly on transition matrices |

### 8.5 Synthesis: The Generic Indivisibility Theorem

Combining the three lines:

> **Theorem (Generic Indivisibility of Marginal Dynamics).** Let $(\Gamma, \Phi_t, \rho_0)$ be a Hamiltonian dynamical system with $\Gamma = \Gamma_{\text{vis}} \times \Gamma_{\text{hid}}$, where $\dim(\Gamma_{\text{vis}}) \geq 3$ and $\rho_0(\gamma_v, \gamma_h)$ is non-factorizable. Define the marginal stochastic matrix $T_{ij}(t)$ by integrating the deterministic flow over the hidden sector weighted by the conditional distribution $P(\gamma_h \mid v_i, t_0)$. Then:
>
> (i) The marginal process is generically non-Markovian (by Kemeny-Snell/Gurvits-Ledoux: lumpability fails on a nowhere-dense set).
>
> (ii) The marginal transition matrix generically lies outside the embeddable submanifold $\mathcal{E}_n$ (by Elfving/Casanellas et al.: $\mathcal{E}_n$ has positive codimension, and the marginalization map $\mathcal{M}$ is non-degenerate by (i)).
>
> (iii) Therefore, the marginal stochastic dynamics is generically **indivisible**: $T(t_2, t_0)$ cannot be factored as $\tilde{T}(t_2, t_1) \cdot T(t_1, t_0)$ with both factors entry-wise non-negative stochastic matrices, for generic choices of $H$, $\rho_0$, and $t$.

**Status.** Each component — Gurvits-Ledoux, Casanellas et al., Mori-Zwanzig — is individually proven and published. The synthesis combines them via a transversality argument that, while standard in differential topology, has not previously been applied to this specific problem. A fully self-contained proof would require verifying the non-degeneracy of $\mathcal{M}$ for physically realistic Hamiltonians (Open Problem 1, Section 11.3).

---

## 9. FROM INDIVISIBILITY TO QUANTUM MECHANICS

### 9.1 Barandes' Stochastic-Quantum Correspondence

Barandes (2025) established a bijective correspondence between indivisible stochastic processes and unitary quantum systems. The result was peer-reviewed and published in *Philosophy of Physics* 3(1):8 (June 2025) [13]; see also the earlier preprint [14].

**Theorem (Barandes).** Let $\{T(t_k, t_{k-1})\}$ be a stochastic process on $n$ configurations that is indivisible. Then there exists a unitary quantum system on a Hilbert space $\mathcal{H}$ of dimension $\tilde{n} \leq n^3$ and a unitary propagator $U(t)$ such that the transition probabilities are recovered via the Born rule:

$$T_{ij}(t) = |U_{ij}(t)|^2$$

Conversely, every unitarily evolving quantum system defines an indivisible stochastic process. The construction is exact and uses the Stinespring dilation theorem.

### 9.2 What Emerges

From this correspondence, applied to the indivisible marginal dynamics of Section 8, the full quantum formalism follows:

**Hilbert space.** The state space of the visible sector is a complex Hilbert space — not because the observer chose it, but because it is the unique structure whose squared-modulus projections reproduce the observed indivisible transition probabilities.

**The Born rule.** The probability rule $p_i = |\psi_i|^2$ is the elementwise absolute-value-squared map between the unitary matrix and the stochastic matrix.

**Superposition and interference.** The stochastic matrix $T_{ij} = |U_{ij}|^2 = |\sum_k U_{ik} U_{kj}^*|^2$ contains cross-terms. These are the mathematical signature of indivisible transitions.

**Non-commuting observables.** Observables jointly measurable in the full classical system become non-commuting in the quantum description because their joint determination requires hidden-sector information.

**Bell inequality violations.** The full classical system satisfies all Bell inequalities — there is no superluminal signaling or nonlocal causation at the level of the complete microstate. However, the marginal stochastic process, being indivisible, generates correlations that cannot be reproduced by any *divisible* (classically Markovian) local model. The apparent nonlocality is a property of the incomplete description, not of the underlying dynamics — precisely analogous to how entanglement in standard quantum mechanics arises from tracing out subsystem degrees of freedom. Barandes, Hasan, and Kagan (arXiv:2512.18105, 2025) showed that causally local indivisible stochastic processes saturate Tsirelson's bound at $2\sqrt{2}$ [15].

### 9.3 The Schrödinger Equation and the Memory Kernel

The Mori-Zwanzig identity (Section 8.3) produces integro-differential dynamics with a memory kernel, while the Schrödinger equation is first-order and instantaneous. The resolution: these are *dual representations of the same dynamics*. The wave function compresses the history-dependent memory structure into an instantaneous state — its complex phases encode exactly the information that the memory kernel $K(\tau)$ spreads across the time integral. The unitary propagator $U(t) = e^{-iHt/\hbar}$ is the "Barandes face" of the same dynamics that the Mori-Zwanzig projection expresses as an integro-differential equation.

---

## 10. THE TRACE-OUT CONJECTURE AND ITS CONSEQUENCES

### 10.1 The Trace-Out Conjecture

The full chain extending the Observational Incompleteness Theorem to its dynamical consequence is:

$$\text{Observational Incompleteness (Sec. 2)} \implies \text{hidden sector with correlations (Sec. 7)}$$
$$\xrightarrow{\text{marginalize (Sec. 6)}} \text{Stochastic process on } \Gamma_{\text{vis}}$$
$$\xrightarrow{\text{generic indivisibility (Sec. 8)}} \text{Indivisible stochastic process}$$
$$\xrightarrow{\text{Barandes (Sec. 9)}} \text{Unitary quantum mechanics on } \mathcal{H}$$

> **The Trace-Out Conjecture.** Let the universe be a classical statistical system governed by deterministic Liouville dynamics on a phase space $\Gamma$. Let classical general relativity's causal horizon structure partition $\Gamma$ into visible and hidden sectors, as required by the Observational Incompleteness Theorem of Section 2. Because shared causal history and exact conservation laws ensure that the joint probability distribution $\rho(\gamma_v, \gamma_h)$ is generically correlated, the marginal stochastic dynamics on the visible sector is generically indivisible (Generic Indivisibility Theorem, Section 8.5).
>
> By Barandes' stochastic-quantum correspondence, this indivisible stochastic process is exactly equivalent to a unitary quantum system. Therefore, quantum mechanics is not a fundamental dynamical law, but rather the mandatory mathematical framework for any embedded observer forced to marginalize deterministic classical mechanics over a correlated, causally inaccessible hidden sector.
>
> The Trace-Out Conjecture is the dynamical extension of the Observational Incompleteness Theorem: where the OIT establishes that embedded observers *cannot* simultaneously access both variance-type and mean-type projections of the hidden sector, the Trace-Out Conjecture proposes that quantum mechanics is the emergent phenomenon that necessarily arises when such observers attempt to describe the dynamics of the visible sector.

### 10.2 Experimental Predictions

If the Observational Incompleteness Theorem is correct and the Trace-Out Conjecture holds, general relativity is an effective mean-field description of a hidden sector with $N \sim 10^{244}$ degrees of freedom. This yields falsifiable predictions:

**10.2.1 Gravitational Wave Echoes.** If spacetime curvature emerges as a mean-field thermodynamic variable of the hidden sector, the mean-field approximation must break down at scales where individual hidden-sector degrees of freedom become resolvable. Future observations of binary black hole mergers should detect post-merger echoes whose amplitude scales with the ratio of probe frequency to the hidden sector's relaxation frequency. For a stellar-mass black hole merger, the characteristic echo timescale is set by the light-crossing time of the near-horizon region modified by the hidden-sector granularity: $\Delta t_{\text{echo}} \sim \frac{r_s}{c} \ln(N^{1/2}) \sim 10^{-5}$–$10^{-4}$ s, where $r_s$ is the Schwarzschild radius and $N^{1/2} \sim 10^{122}$ provides the logarithmic correction. This places the predicted echoes within the sensitivity band of current and next-generation gravitational wave detectors (LIGO A+, Einstein Telescope, Cosmic Explorer). The echo structure encodes the granularity of the underlying hidden-sector dynamics — its detection would confirm that gravity is not fundamental geometry but an emergent statistical description.

**10.2.2 Stochastic Gravitational Noise Floor.** A stochastic gravitational wave background should exist, with an amplitude anchored to the $10^{122}$ ratio. The mean-field description of the hidden sector predicts irreducible fluctuations around the macroscopic expectation value, analogous to Johnson-Nyquist noise in electrical circuits. The characteristic strain amplitude scales as $h_{\text{rms}} \sim \sqrt{\rho_{\text{grav}} / \rho_{\text{QM}}} \cdot (f / f_{\text{Pl}})^\alpha \sim 10^{-61} (f / f_{\text{Pl}})^\alpha$, where $\alpha$ encodes the spectral index of the hidden-sector fluctuation spectrum. In the MHz–GHz band, these fluctuations should produce a detectable stochastic noise floor whose spectral density is determined by the hidden-sector dimensionality $N \sim 10^{244}$ and the Planck-scale cutoff. While this lies beyond current detector sensitivity, proposed high-frequency gravitational wave experiments targeting the MHz range (e.g., levitated sensor arrays and bulk acoustic wave detectors) approach the regime where this floor becomes relevant.

**10.2.3 Falsification.** The framework makes two concrete null predictions: (i) post-merger echoes at the predicted timescale of $\Delta t_{\text{echo}} \sim 10^{-5}$–$10^{-4}$ s with amplitude scaling logarithmically in $N^{1/2}$, and (ii) a stochastic noise floor in the MHz–GHz band with spectral density set by $N \sim 10^{244}$. If next-generation detectors achieve the requisite sensitivity and find no echoes at the predicted timescale, or if high-frequency experiments definitively exclude the predicted noise floor, the framework would be falsified. More broadly, experimental observation of perfectly smooth, unperturbed spacetime geometry with no granularity signatures at any accessible scale would rule out the hidden-sector interpretation of gravity.

---

## 11. DISCUSSION

### 11.1 Independent Corroboration: Wetterich's Program

Wetterich (2001–2025) arrived at a closely related conclusion from a different starting point [17]. Working entirely within classical probability theory, Wetterich proved that a subsystem with "incomplete statistics" over a sufficiently large classical system is necessarily described by the quantum formalism. His constructions are explicit: a single qubit emerges from classical Ising spins, and Bell inequality violations arise because subsystem observers lack access to complete joint distributions.

The culmination, *The Probabilistic World* (Springer, Fundamental Theories of Physics vol. 220, 2025), systematically develops this framework [16]. Key differences: Wetterich demonstrates emergence for specific models but does not establish full generality, and does not prove the correspondence is bidirectional. The present approach, via Barandes' bijective theorem applied to the generic indivisibility result, aims for both.

The independent convergence of two routes — the Barandes/indivisibility route and the Wetterich/incomplete-statistics route — on the same conclusion significantly strengthens the case.

### 11.2 Scope and Relation to Prior Work

The mechanism is purely classical: marginalization over a correlated hidden sector breaks stochastic divisibility, and Barandes' correspondence translates indivisibility into the quantum formalism. Unlike Adler's trace dynamics [19], it begins with commuting classical variables. Unlike Nelson's stochastic mechanics [20], it bypasses Wallstrom's objection [21] because the quantum structure emerges from indivisibility of marginal stochastic dynamics rather than from stochastic differential equations. Unlike 't Hooft's cellular automaton interpretation [18], it does not require any a priori discrete substrate.

### 11.3 Key Objections

**"Deriving quantum mechanics from classical statistics is circular — you need QM to define the partition."**
The partition is defined entirely by classical general relativity. The causal horizon structure is determined by the Einstein field equations, a classical field theory. No quantum concept enters.

**"This is just a hidden-variable theory — Bell's theorem rules it out."**
Bell's theorem rules out *local* hidden-variable theories producing *divisible* stochastic dynamics. The present framework produces *indivisible* dynamics. Bell's theorem is not violated; it is *derived* as a property of the marginal description.

**"The memory kernel implies non-autonomous dynamics, but QM is autonomous."**
The Schrödinger equation and Mori-Zwanzig equation are dual representations (Section 9.3). The wave function compresses history dependence into instantaneous complex phases.

**"Non-Markovianity does not imply indivisibility (Milz and Modi, 2021) [22]."**
Correct, and this is precisely why the proof in Section 8 requires all three lines. Non-Markovianity alone (Line 1) is necessary but insufficient. The geometric argument (Line 2) upgrades it to generic indivisibility by combining non-degeneracy (from Line 1) with the positive-codimension geometry of the embeddable set.

**"The transversality argument requires verification of non-degeneracy."**
Acknowledged (Open Problem 1). The physical basis for expecting non-degeneracy is strong: chaotic dynamics of a high-dimensional hidden sector, combined with broken lumpability, generically produces marginal matrices that explore a full-dimensional region of $\mathcal{S}_n$.

### 11.4 Open Problems

**(1) Formal Verification of Non-Degeneracy.** Prove that the marginalization map $\mathcal{M}: (H, \rho_0, t) \to T(t)$ has full-rank Jacobian for physically realistic Hamiltonians and correlated initial distributions. This would convert the transversality argument from a genericity statement to a rigorous theorem.

**(2) Concrete Model Verification.** Construct a tractable model — e.g., a classical oscillator coupled to a high-dimensional chaotic bath with conserved total energy — compute the marginal stochastic matrix explicitly, and verify that it is indivisible.

**(3) Continuous-Variable Extension.** Extend the discrete-configuration-space framework to continuous phase spaces. Barandes' theorem is stated for finite-dimensional configuration spaces; a rigorous infinite-dimensional extension is needed for field theory.

**(4) Quantitative Bounds.** Determine the relationship between the dimensionality of the hidden sector, the strength of correlations, and the degree of indivisibility.

**(5) The Continuous Precision Trade-Off.** Determine the exact functional form of the product bound on the mean-squared errors of variance-type versus mean-type measurements for an embedded inference device. This would sharpen the Observational Incompleteness Theorem from a qualitative statement to a quantitative uncertainty relation.

---

## 12. CONCLUSION

Embedded observers face irreducible inference limits (Wolpert). These limits, physically instantiated by the causal horizon structure of classical general relativity, force any embedded observer to marginalize deterministic Liouville dynamics over a vast, correlated hidden sector. The Observational Incompleteness Theorem establishes that the resulting variance-type and mean-type projections of this hidden sector — quantum mechanics and gravity — cannot be simultaneously determined, and that the $10^{122}$ cosmological constant discrepancy is the quantitative signature of this incompleteness, yielding a measurement of roughly $10^{244}$ hidden-sector degrees of freedom.

The Trace-Out Conjecture extends this result to its dynamical consequence: quantum mechanics is the emergent phenomenon that necessarily arises when these constrained observers attempt to describe the dynamics of the visible sector. By three independent lines of established mathematics — the algebraic failure of lumpability (Kemeny-Snell, Gurvits-Ledoux), the positive-codimension geometry of embeddable Markov matrices (Elfving, Casanellas et al.), and the analytic memory structure of projected dynamics (Mori-Zwanzig) — the marginalization generically breaks stochastic divisibility. By Barandes' stochastic-quantum correspondence, the resulting indivisible stochastic process is exactly equivalent to a unitary quantum system.

Hilbert space, the Born rule, superposition, non-commuting observables, and Bell inequality violations are not fundamental laws but the necessary mathematical consequences of classical mechanics plus observational incompleteness. The incompatibility between quantum mechanics and gravity is not a bug to be fixed — it is the physical analogue of Gödel incompleteness, the universe telling observers, in the starkest numerical terms available, that they are inside the system they are trying to describe.

---

## REFERENCES

[1] D. H. Wolpert, "Physical Limits of Inference," *Physica D* **237**, 1257–1281 (2008).
[2] S. Weinberg, "The Cosmological Constant Problem," *Rev. Mod. Phys.* **61**, 1 (1989).
[3] J. Martin, "Everything You Always Wanted to Know About the Cosmological Constant Problem (But Were Afraid to Ask)," *C. R. Phys.* **13**, 566–665 (2012).
[4] M. Ahmed, S. Dodelson, P. B. Greene, and R. Sorkin, "Everpresent $\Lambda$," *Phys. Rev. D* **69**, 103523 (2004).
[5] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).
[6] T. Padmanabhan, "Vacuum Fluctuations of Energy Density Can Lead to the Observed Cosmological Constant," *Class. Quant. Grav.* **22**, L107 (2005).
[7] H. Mori, "Transport, Collective Motion, and Brownian Motion," *Prog. Theor. Phys.* **33**, 423 (1965).
[8] R. Zwanzig, "Ensemble Method in the Theory of Irreversibility," *J. Chem. Phys.* **33**, 1338 (1960).
[9] J. G. Kemeny and J. L. Snell, *Finite Markov Chains* (Van Nostrand, 1960).
[10] L. Gurvits and J. Ledoux, "Markov Property for a Function of a Markov Chain: A Linear Algebra Approach," *Lin. Alg. Appl.* **404**, 85–117 (2005).
[11] G. Elfving, "Zur Theorie der Markoffschen Ketten," *Acta Soc. Sci. Fenn. A* **2**(8), 1–17 (1937).
[12] M. Casanellas, J. Fernández-Sánchez, and J. Roca-Lacostena, "The Embedding Problem for Markov Matrices," *Publ. Mat.* **67**, 411–445 (2023).
[13] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).
[14] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).
[15] J. A. Barandes, M. Hasan, and D. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).
[16] C. Wetterich, *The Probabilistic World: Quantum Mechanics from Classical Statistics* (Springer, Fundamental Theories of Physics vol. 220, 2025).
[17] C. Wetterich, "Quantum Mechanics from Classical Statistics," *J. Phys.: Conf. Ser.* **174**, 012008 (2009).
[18] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).
[19] S. L. Adler, *Quantum Theory as an Emergent Phenomenon* (Cambridge University Press, 2004).
[20] E. Nelson, "Derivation of the Schrödinger Equation from Newtonian Mechanics," *Phys. Rev.* **150**, 1079 (1966).
[21] T. C. Wallstrom, "Inequivalence Between the Schrödinger Equation and the Madelung Hydrodynamic Equations," *Phys. Rev. A* **49**, 1613 (1994).
[22] S. Milz and K. Modi, "Quantum Stochastic Processes and Quantum Non-Markovian Phenomena," *PRX Quantum* **2**, 030201 (2021).
[23] J. Szangolies, "Epistemic Horizons and the Foundations of Quantum Mechanics," *Found. Phys.* **48**, 1669–1697 (2018).
[24] R. D. Sorkin, "Spacetime and Causal Sets," in *Relativity and Gravitation: Classical and Quantum*, eds. J. C. D'Olivo et al. (World Scientific, 1991), pp. 150–173.
