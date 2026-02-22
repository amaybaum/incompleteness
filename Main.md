# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum
**Date:** February 2026
**Status:** DRAFT PRE-PRINT
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

The incompatibility between quantum mechanics and general relativity is a structural consequence of embedded observation. Any observer that is part of the universe it measures must access reality through projections that discard causally inaccessible degrees of freedom defined by spacetime's causal structure. The **Observational Incompleteness Theorem** is proposed by applying Wolpert's (2008) inference limits: quantum and gravitational vacuum energy measurements are identified as variance-type and mean-type projections of a shared hidden sector, and it is argued that no embedded device can simultaneously determine both. Under this identification, the 10^122^ cosmological constant discrepancy is reinterpreted as a measurement of ~10^244^ hidden-sector degrees of freedom.

The **Trace-Out Conjecture** is then presented: assuming only classical Liouville dynamics, classical general relativity, and classical probability theory, marginalizing over the correlated hidden sector produces generically indivisible stochastic dynamics on the visible sector. By Barandes' stochastic-quantum correspondence, this indivisible process is exactly equivalent to unitary quantum mechanics. The Schrödinger equation emerges as the unique time-local description of history-dependent classical marginals. The framework yields falsifiable predictions, including post-merger gravitational wave echoes and a stochastic gravitational noise floor whose spectral density is anchored to the hidden-sector dimensionality.

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

The ratio is conventionally rounded to 10^120^ in the literature [2,3,5], or more precisely 10^122^. A different interpretation is proposed: **neither calculation is wrong. They disagree because they are answering fundamentally different questions about the same thing**.

---

## 2. OBSERVATIONAL INCOMPLETENESS

### 2.1 Observers Are Embedded
Wolpert (2008) [1] proved that any physical device performing observation, prediction, or recollection — an "inference device" — faces fundamental limits on what it can know about the universe it inhabits. These limits hold **independent of the laws of physics**. They follow solely from the logical structure of a device that is embedded in the system it attempts to describe, forcing any observation to be a surjective, many-to-one mapping from the total state to the device's output. 

### 2.2 The Hidden Sector


Let the full state space be partitioned into degrees of freedom accessible to observers (the visible sector) and degrees of freedom that are not (the hidden sector, denoted $\Phi$). The hidden sector consists of trans-horizon modes beyond the cosmological horizon, sub-Planckian degrees of freedom below the observer's resolution limit, and black hole interiors. The partition is defined entirely by classical general relativity. No quantum concept enters the definition of what is hidden from the observer.

### 2.3 Two Projections of the Same Thing

To make the connection to Wolpert's framework precise, the two vacuum-energy measurements are formalized as distinct inference targets. Let the hidden sector's microstate be characterized by a distribution over $N$ mode energies $\{E_i\}$. An embedded observer cannot access this distribution directly; any measurement is a surjective (many-to-one) mapping from the full microstate to a single output. Following Wolpert, two such inference targets are defined:

**Target 1: The Total Unsigned Power (QM's Variance-Type Projection).** QFT's operational access to the vacuum is through the fluctuation power spectrum. Because zero-point energies $\frac{1}{2}\hbar\omega$ are positive-definite, the QFT vacuum energy sums their absolute magnitudes:
$$V = \sum_{i=1}^{N} |E_i|$$
This is a variance-type target in the sense that it measures the total unsigned spread of the distribution — it grows linearly with $N$ regardless of the signs of individual contributions, analogous to how the variance of a sum of independent variables grows linearly with the number of terms. It is explicitly noted that $V$ is not literally a statistical variance; the analogy is in the scaling behavior and in the fact that $V$ is insensitive to correlations among the signs of contributions.

**Target 2: Mean-Field Pressure (Gravity's Mean-Type Projection).** The Einstein field equations couple spacetime curvature to the macroscopic expectation value of the stress-energy tensor. The gravitational projection is sensitive to the *net signed sum*:
$$M = \langle T_{00} \rangle = \sum_{i=1}^{N} E_i$$
where the $E_i$ now carry their physical signs. In a system with many degrees of freedom spanning both bosonic and fermionic sectors, broken symmetry phases, and the variety of interactions present in a realistic field theory, the individual contributions generically carry both positive and negative signs. **This is a substantive physical assumption, not a deductive consequence**: it is assumed that the hidden sector does not possess an unbroken symmetry that would align all contributions with a common sign. Under this assumption, $M$ is a sum of quasi-independent signed terms, and the central limit theorem gives the characteristic scaling $|M| \sim \sqrt{N}$.

The two targets $V$ and $M$ are distinct surjective functions of the same underlying microstate. In Wolpert's framework, two inference targets defined on the same system are subject to joint constraints when the inference device is embedded in that system: the device's own state must be consistent with both measurements simultaneously, imposing a trade-off on joint accuracy. The specific product bound on the mean-squared errors of $V$ and $M$ depends on the coupling structure and is left as an open problem (see Section 8.3). What the framework establishes is the structural claim: these are complementary projections of a shared sector, and their disagreement is a signature of the projection rather than an error in either theory.

### 2.4 The Observational Incompleteness Theorem

> **Observational Incompleteness Theorem.** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. Define the variance-type target $V = \sum |E_i|$ and the mean-type target $M = \sum E_i$ on the hidden-sector distribution. Then: (i) $V$ and $M$ are distinct surjective functions of the same microstate; (ii) by Wolpert's results [1], any embedded inference device faces fundamental limits on simultaneously determining both targets; and (iii) under the physical assumption that hidden-sector contributions carry quasi-random signs, $V \propto N$ while $|M| \propto \sqrt{N}$, producing a ratio $V/|M| \propto \sqrt{N}$.

**Status of the theorem.** Claim (i) is definitional. Claim (ii) follows from Wolpert's general results on embedded inference, but the specific joint accuracy bound for these particular targets has not yet been derived; the theorem currently relies on the structural form of Wolpert's constraints rather than a quantitative product inequality. Claim (iii) rests on the physical assumption stated in Section 2.3 regarding the sign structure of hidden-sector contributions. The theorem is therefore a conjecture with rigorous structural motivation rather than a fully closed proof, and sharpening the quantitative bound is identified as a priority open problem (Section 8.3).

---

## 3. THE RATIO AS MEASUREMENT

### 3.1 Extracting the Hidden-Sector Dimensionality
The Observational Incompleteness Theorem, if correct, reframes the cosmological constant discrepancy as an informative physical quantity rather than a paradox. The variance-type scaling grows directly with the number of modes ($V \propto N$) while the macroscopic mean scales as the square root ($|M| \sim \sqrt{N}$). Their ratio:
$$\frac{V}{|M|} \sim \frac{N}{\sqrt{N}} = \sqrt{N}$$
Setting this equal to the observed discrepancy:
$$\sqrt{N} \sim 10^{122} \implies N \sim 10^{244}$$
Under this interpretation, the 10^122^ ratio is a quantitative signature of observational incompleteness — encoding the dimensionality of the sector that embedded observers cannot access. This reinterpretation is contingent on the validity of the sign-structure assumption and the identification of QFT and GR vacuum energies with the specific projections defined above.

---

## 4. CLASSICAL PREMISES AND MARGINAL DYNAMICS

The Observational Incompleteness Theorem, as argued above, proposes that embedded observers face irreducible epistemic constraints when probing the hidden sector. The remainder of this paper pursues a considerably stronger claim: that quantum mechanics itself is a necessary consequence of these constraints. This is a significant escalation in ambition — from reinterpreting a known discrepancy to deriving an entire physical framework — and the reader is entitled to skepticism. The argument's credibility therefore rests entirely on the transparency of its premises and the rigor of each mathematical step. Importantly, the two central results are logically independent: the Observational Incompleteness Theorem stands or falls on its own merits regardless of whether the Trace-Out Conjecture is accepted, and vice versa. The derivation proceeds from three classical premises through a chain of established mathematical results, assuming no quantum postulate at any stage.

* **Premise 1: Classical Statistical Dynamics.** The total universe is a classical statistical system evolving deterministically via the Liouville equation:
    $$\frac{\partial \rho}{\partial t} = \{H, \rho\}$$
* **Premise 2: Classical General Relativity as Causal Structure.** Einstein's field equations determine the causal structure of spacetime, creating the absolute information barriers that define the hidden sector. 
* **Premise 3: Classical Probability Theory.** All statistical inference follows from Kolmogorov's axioms. Observational predictions are classical expectation values.

The observer's operational description of the visible sector is therefore a **marginal stochastic matrix**:
$$T_{ij}(t, t_0) = \int d\gamma_h \; P(\gamma_h \mid v_i, t_0) \; \mathbb{1}\!\left[\Phi_t(v_i, \gamma_h) \in v_j\right]$$
The central question: can $T$ be factored as a strictly divisible Markov process, or does marginalization over the hidden sector break divisibility?

---

## 5. THE NECESSITY OF CORRELATIONS

If the visible and hidden sectors are statistically correlated, divisibility generically breaks. 
1.  **Shared Causal History:** Prior to cosmological horizon formation, the degrees of freedom now separated were in direct causal contact, ensuring $\rho(\gamma_v, \gamma_h) \neq \rho_{\text{vis}}(\gamma_v)\,\rho_{\text{hid}}(\gamma_h)$.
2.  **Conservation Laws:** Noether's theorem guarantees conserved charges ($E_{\text{total}} = E_v + E_h = \text{const}$) that rigidly couple the visible and hidden sectors. This correlation is enforced by the symmetry structure of the Hamiltonian itself.

---

## 6. GENERIC INDIVISIBILITY

The marginal stochastic dynamics is generically non-divisible due to topological and algebraic necessity.

* **Failure of Lumpability:** Kemeny and Snell (1960) established that coarse-graining retains the Markov property only under strong lumpability conditions. Gurvits and Ledoux (2005) proved these conditions are nowhere dense. The conservation-law correlations violate lumpability, meaning the marginal dynamics is generically non-Markovian.
* **Geometry of Non-Embeddability:** Casanellas et al. (2023) proved that embeddable stochastic matrices form a proper semi-algebraic subset of strictly lower dimension for $n \geq 3$. 

---

## 7. THE TRACE-OUT CONJECTURE

The qualitative transversality arguments of Section 6 must be elevated to a rigorous statistical proof to formalize the generalized mechanism.

> **The Trace-Out Conjecture.** Let the universe be a classical statistical system governed by deterministic Liouville dynamics. Let classical general relativity partition the system into visible and hidden sectors, with $N \sim 10^{244}$ inaccessible degrees of freedom. Shared causal history and exact conservation laws enforce non-factorizable joint probability distributions. By the Random Matrix derivation of the Mori-Zwanzig covariance, the marginal stochastic dynamics on the visible sector is generically indivisible with probability 1 within the GOE ensemble, and is expected to be indivisible for any sufficiently complex hidden-sector Hamiltonian. 
> 
> By Barandes' stochastic-quantum correspondence and the continuous complex-phase mapping, this indivisible classical process is exactly equivalent to unitary quantum mechanics. Therefore, the quantum formalism is not a fundamental dynamical law, but the mandatory mathematical data-compression algorithm for any embedded observer forced to marginalize deterministic classical mechanics over a correlated hidden sector.

This conjecture relies on the validity of Barandes' stochastic-quantum correspondence [13,14], which is adopted here as a premise rather than re-derived.

### 7.1 Proof of Statistical Non-Degeneracy via Random Matrix Theory


To prove that the marginalization map $\mathcal{M}: (H, \rho_0, t) \to T(t)$ is non-degenerate and fills the stochastic simplex, the hidden Liouvillian $\mathcal{L}_{\text{hid}}$ is modeled as a large matrix drawn from the Gaussian Orthogonal Ensemble (GOE).

The choice of GOE requires physical justification. The hidden sector, comprising ~10^244^ trans-horizon, sub-Planckian, and interior degrees of freedom, is a high-dimensional system whose detailed Hamiltonian is unknown to any embedded observer. In such regimes, the eigenvalue statistics of large, complex Hamiltonians are universally described by random matrix theory — a result established empirically in nuclear physics (Wigner, Dyson) and proven rigorously for broad classes of Hamiltonians with sufficient complexity (Erdős–Yau universality). The GOE is the appropriate ensemble because the underlying classical Liouville dynamics is time-reversal symmetric and the matrix elements are real. Crucially, the key result — full-rank covariance of the marginal transition elements — is a consequence of the high dimensionality and generic coupling, not of the specific Gaussian distribution of matrix entries. Any ensemble with $N \gg n$ independent parameters and no fine-tuned symmetries that would zero out off-diagonal blocks would yield the same conclusion. The GOE is therefore best understood not as a specific physical hypothesis but as the maximally agnostic statistical model consistent with the known constraints.

The total Liouvillian is defined as $\mathcal{L} = \mathcal{L}_0 + \delta \mathcal{L}_h$, where $\delta \mathcal{L}_h$ is a random fluctuation in the hidden sector. Applying the Dyson series expansion to the Mori-Zwanzig projected propagator, the first-order variation of the transition matrix is:
$$\delta T_{ij}(t) = \int_0^t d\tau \, \langle j | P e^{\mathcal{L}_0(t-\tau)} \delta \mathcal{L}_h e^{\mathcal{L}_0\tau} P | i \rangle$$

Because the baseline propagator $e^{\mathcal{L}_0\tau}$ does not factorize due to shared conservation laws, the initial state is already correlated with the bath. The resulting covariance matrix of the transition elements scales as:
$$C_{(ij)(kl)} = \langle \delta T_{ij} \delta T_{kl} \rangle \propto \text{Tr}(\mathcal{L}_{\text{int}}^\dagger \text{Cov}(\delta \mathcal{L}_h) \mathcal{L}_{\text{int}})$$

In the GOE limit where $N \sim 10^{244} \gg n$, the vast number of independent parameters in $\mathcal{L}_h$ ensures that the Jacobian of $\mathcal{M}$ possesses full row rank. Consequently, the covariance matrix $C$ is strictly positive-definite. The induced measure $P(T)$ has full-dimensional volume support across the stochastic simplex $\mathcal{S}_n$. Because embeddable Markov matrices $\mathcal{E}_n$ occupy a zero-volume lower-dimensional submanifold, integrating this measure over $\mathcal{E}_n$ yields exactly zero. Under the GOE model, marginalization over the classical hidden sector is strictly indivisible with probability 1.

**Scope of the result.** This conclusion is derived within the GOE ensemble. The physical claim — that the same holds for the actual hidden-sector Liouvillian — rests on the universality argument that any sufficiently high-dimensional system with generic coupling and no fine-tuned symmetries will exhibit the same full-rank property. This universality claim is physically well-motivated by Wigner-Dyson universality of eigenvalue statistics, but extending it rigorously to the full matrix structure of the Liouvillian (rather than just its spectral statistics) remains an open mathematical problem. The result is therefore stated as: indivisibility holds with probability 1 *within the GOE ensemble*, and is expected to hold generically for physical Hamiltonians of sufficient complexity, but a fully rigorous universality proof is not yet available.

### 7.2 Barandes' Stochastic-Quantum Correspondence
Barandes (2025) established a bijective correspondence: any indivisible stochastic process on $n$ configurations is exactly equivalent to a unitary quantum system on a Hilbert space $\mathcal{H}$, where transition probabilities are recovered via the Born rule $T_{ij}(t) = |U_{ij}(t)|^2$.

### 7.3 The Continuous Limit: Emergence of the Schrödinger Equation
Extending this to continuous variables, the exact classical evolution of the visible particle is described by the non-Markovian generalized Langevin equation:
$$m\ddot{q} + \nabla V(q) + \int_0^t K(t-\tau) \dot{q}(\tau) d\tau = F_{\text{fluct}}(t)$$

Because the horizon constraints ensure the hidden sector is finite, the memory kernel $K(t-\tau)$ retains a non-zero correlation time $\tau_E$. The dynamics are strictly indivisible.

**Step 1: Why a real probability density is insufficient.** The standard Fokker-Planck description of a classical stochastic process propagates a real probability density $P(q,t)$ forward in time via a time-local equation. However, the memory integral $\int_0^t K(t-\tau)\dot{q}(\tau) d\tau$ makes the future evolution depend on the entire past trajectory, not just the current state. A single real field $P(q,t)$ evaluated at time $t$ contains no information about the trajectory history, and therefore cannot generate the correct future evolution in a time-local framework. This is not an approximation issue but a counting argument: one real field carries one degree of freedom per spatial point, while the non-Markovian dynamics requires two (the current distribution and its accumulated momentum history).

**Step 2: Introduction of the phase field.** To encode this history within a time-local description, a conjugate field $S(q,t)$ is introduced and the complex field $\psi(q,t) = \sqrt{P(q,t)} \, e^{iS(q,t)/\hbar}$ is defined. The phase gradient $\nabla S$ serves as the repository for the integrated historical momentum:
$$\nabla S(q,t) = m\dot{q} + \int_0^t K(t-\tau) \dot{q}(\tau) d\tau$$
The key claim is that this identification is *forced* by the requirement of time-locality: $\nabla S$ is the minimal additional field needed to promote the non-Markovian integro-differential dynamics into an equivalent time-local PDE system. This step — identifying the need for a phase degree of freedom as a consequence of non-Markovianity rather than postulating it — is the central novel element of this derivation.

**Step 3: Coupled hydrodynamic equations.** Given $P(q,t)$ and $S(q,t)$, conservation of probability requires the continuity equation:
$$\frac{\partial P}{\partial t} + \nabla \cdot \left( P \frac{\nabla S}{m} \right) = 0$$

This follows directly from identifying $\nabla S / m$ as the velocity field of the probability flow. Simultaneously, energy conservation enforced by the hidden-sector bath requires the generalized Hamilton-Jacobi equation for $S$:
$$\frac{\partial S}{\partial t} + \frac{(\nabla S)^2}{2m} + V(q) + Q = 0$$

The term $Q$ arises from the fluctuation-dissipation relation: a particle coupled to a thermal bath acquires an osmotic velocity proportional to $\nabla \ln P$, a standard result in stochastic thermodynamics (see e.g. Nelson [20]). The corresponding potential energy is:
$$Q = -\frac{\hbar^2}{2m} \frac{\nabla^2 \sqrt{P}}{\sqrt{P}}$$
where $\hbar$ enters not as a fundamental constant but as the scale factor quantifying the characteristic action of the hidden sector's fluctuation-dissipation balance. This is structurally identical to the Bohmian quantum potential.

**Step 4: Linearization.** Substituting $\psi = \sqrt{P} \, e^{iS/\hbar}$ into the coupled nonlinear system (the continuity equation and the modified Hamilton-Jacobi equation), direct computation shows that both equations are equivalent to the single linear PDE:
$$i\hbar \frac{\partial \psi}{\partial t} = \left[ -\frac{\hbar^2}{2m}\nabla^2 + V(q) \right] \psi$$
This is a standard result in hydrodynamic reformulations of wave mechanics (Madelung 1927, Bohm 1952), but is here read in reverse — from classical non-Markovian dynamics *toward* the quantum formalism, rather than decomposing an assumed Schrödinger equation. The Schrödinger equation is therefore derived as the unique time-local PDE that generates the indivisible marginal transition probabilities of a history-dependent classical system.

**The Wallstrom objection.** Wallstrom (1994) [21] demonstrated that the Madelung hydrodynamic equations are not equivalent to the Schrödinger equation unless an additional quantization condition $\oint \nabla S \cdot dl = 2\pi n \hbar$ is imposed on the phase field. This is a serious and well-known objection to any purely hydrodynamic derivation of quantum mechanics.

In the present framework, the Wallstrom gap is addressed — though not trivially — by the discrete stochastic foundation established in Sections 6–7.2. The argument proceeds as follows. The indivisible stochastic matrices on the discrete configuration space carry the full quantum structure via Barandes' correspondence, including unitarity, the Born rule, and the discrete analogue of the topological quantization conditions (which in the discrete setting reduce to the requirement that the unitary matrix $U_{ij}$ be single-valued). The continuous Schrödinger equation derived here is obtained as the continuum limit of this discrete dynamics. The single-valuedness of $\psi$ — and hence the quantization of $\oint \nabla S \cdot dl$ — is inherited from the discrete level, where it is a consequence of the stochastic-quantum correspondence rather than an additional postulate.

The strength of this resolution depends on the rigor of the continuum limit: one must show that the discrete-to-continuous passage preserves the topological structure that enforces quantization. For finite-dimensional configuration spaces, this follows from the continuity of the map between stochastic matrices and unitary matrices in Barandes' framework. For infinite-dimensional field-theoretic configuration spaces, the continuum limit is a nontrivial mathematical problem that is identified as an open question (Section 8.3). The Wallstrom objection is therefore substantially mitigated but not fully eliminated for field theories.

### 7.4 Experimental Predictions

The framework generates two falsifiable predictions that are quantitatively anchored to the hidden-sector dimensionality $N \sim 10^{244}$.

**Prediction 1: Gravitational Wave Echoes.**
If spacetime curvature is a mean-field thermodynamic variable of the hidden sector, post-merger black hole ringdown should exhibit echoes reflecting the hidden-sector's discrete granularity. The characteristic timescale is set by the scrambling time of the hidden sector, modeled as a maximally chaotic (fast-scrambling) system. For a fast scrambler with entropy $S$, the scrambling time scales as $t_{\text{scr}} \sim \beta \ln S$, where $\beta \sim r_s / c$ is the inverse Hawking temperature and $r_s$ is the Schwarzschild radius. Taking the hidden-sector entropy as $S \sim \sqrt{N} \sim 10^{122}$ (consistent with the holographic bound on the observable universe), the echo delay is:
$$\Delta t_{\text{echo}} \sim \frac{r_s}{c} \ln(10^{122}) \sim \frac{r_s}{c} \times 281$$
For a 30 $M_\odot$ post-merger remnant ($r_s \approx 90$ km), this yields $\Delta t_{\text{echo}} \sim 8 \times 10^{-5}$ s, placing the signal in the 10^-5^–10^-4^ s range accessible to current LIGO/Virgo/KAGRA post-merger analyses. The echo amplitude is suppressed by the reflectivity of the effective hidden-sector boundary, which this framework predicts to be nonzero but small — a quantitative estimate requires solving the effective boundary conditions and is left as an open problem.

**Prediction 2: Stochastic Gravitational Noise Floor.**
The irreducible fluctuations of the hidden sector must source a stochastic gravitational wave background. A naive dimensional estimate proceeds as follows. The hidden sector contributes $N \sim 10^{244}$ modes, each with Planck-scale zero-point energy $E_{\text{Pl}} \sim 10^{9}$ J, but the gravitational coupling is suppressed by the mean-field averaging over $\sqrt{N}$ modes. The residual energy density in gravitational fluctuations scales as:
$$\Omega_{\text{gw}}^{\text{naive}} \sim \frac{\rho_{\text{QM}}}{\rho_c} \times \frac{1}{\sqrt{N}} \sim \frac{10^{113}}{10^{-10}} \times 10^{-122} \sim 10^{1}$$

**This naive estimate is problematic.** An $\mathcal{O}(1)$ stochastic background in units of the critical density would violate existing observational constraints from LIGO/Virgo, pulsar timing arrays, and Big Bang nucleosynthesis, all of which bound $\Omega_{\text{gw}}$ to be well below unity across their respective frequency bands [see e.g. constraints compiled in LIGO-Virgo-KAGRA collaboration results]. The estimate must therefore be an overestimate, and identifying *where* it fails is both a test of the framework and a guide to its predictions.

The naive estimate fails for at least two identifiable reasons:

(i) **Spectral distribution.** The estimate treats $\Omega_{\text{gw}}$ as a total integrated quantity, but gravitational wave detectors measure the spectral density $\Omega_{\text{gw}}(f)$ in specific frequency bands. The $N \sim 10^{244}$ hidden-sector modes span frequencies from the Hubble scale ($\sim 10^{-18}$ Hz) to the Planck frequency ($\sim 10^{43}$ Hz) — roughly 61 decades. Distributing the total energy across this bandwidth suppresses the spectral density at any given frequency by a factor related to the spectral shape, which could be as large as $\sim 1/N_{\text{decades}} \sim 10^{-2}$ for a flat spectrum or much more for a spectrum concentrated at high frequencies.

(ii) **Quadrupole coupling.** Not all hidden-sector modes source gravitational radiation. Only modes with a non-zero time-varying quadrupole moment couple to the gravitational wave field. Sub-Planckian degrees of freedom, in particular, may lack the spatial extent required for efficient quadrupole emission, introducing an additional suppression factor that depends on the spatial structure of the hidden sector.

The combination of spectral dilution and quadrupole suppression could plausibly reduce the spectral density by many orders of magnitude relative to the naive estimate. The precise spectral shape $\Omega_{\text{gw}}(f)$ depends on the hidden sector's mode structure and is not determined by the framework's current level of development.

**Falsifiability.** Rather than being a weakness, this situation constitutes a genuine falsifiability test. The framework makes a definite structural prediction — a stochastic background must exist — while the amplitude is constrained from above by existing observations. If the spectral decomposition, once computed, cannot be reconciled with observational upper bounds for *any* physically reasonable hidden-sector mode structure, the framework is falsified. Computing the spectral shape across the MHz–GHz band (where astrophysical foregrounds are minimal) is identified as a priority for follow-up work. Detection, if the amplitude is above instrumental floors, would require next-generation high-frequency gravitational wave detectors currently under development.

---

## 8. DISCUSSION AND OPEN PROBLEMS

### 8.1 Logical Independence of the Central Claims
The two central results of this paper are logically independent. The Observational Incompleteness Theorem depends only on Wolpert's inference limits, the causal structure of general relativity, and the identification of QM and GR vacuum energy measurements as variance-type and mean-type projections. It does not require the Trace-Out Conjecture or any claim about the emergence of quantum mechanics. Conversely, the Trace-Out Conjecture depends on classical Liouville dynamics, classical probability theory, the existence of a correlated hidden sector, and Barandes' stochastic-quantum correspondence — but it does not require the specific identification of the cosmological constant discrepancy as a measurement of $N$. Each result should be evaluated on its own premises. Together, they form a mutually reinforcing picture: the Observational Incompleteness Theorem addresses *why* embedded observers face complementary descriptions, while the Trace-Out Conjecture addresses *what dynamical framework* those descriptions must take.

### 8.2 Independent Corroboration and Consistency
Wetterich (2001–2025) showed that a subsystem with "incomplete statistics" over a sufficiently large classical system is necessarily described by the quantum formalism. The independent convergence of the Barandes/indivisibility route and the Wetterich/incomplete-statistics route significantly strengthens the case. Importantly, the derivation avoids circularity because the system partition is defined entirely by classical general relativity; no quantum concept enters the premises. Furthermore, while Bell's theorem rules out local hidden-variable theories producing *divisible* stochastic dynamics, the apparent nonlocality here is a derived property of the indivisible marginal description.

### 8.3 Open Problems
**(1) Continuous-Variable Extension (Fields).** Extend the phase-mapping framework to continuous infinite-dimensional phase spaces required for relativistic quantum field theory. This includes demonstrating that the discrete-to-continuous limit preserves the topological quantization conditions that address the Wallstrom objection.
**(2) Quantitative Bounds.** Determine the exact relationship between the dimensionality of the hidden sector $N$, the strength of correlations, and the degree of macroscopic indivisibility.
**(3) The Continuous Precision Trade-Off.** Derive the specific product bound on the mean-squared errors of the variance-type target $V$ and the mean-type target $M$ from Wolpert's framework, sharpening the Observational Incompleteness Theorem from a structural claim into a quantitative uncertainty relation.
**(4) Echo Amplitude and Spectral Shape.** Derive the effective reflectivity of the hidden-sector boundary from first principles to produce a quantitative amplitude prediction for gravitational wave echoes. Compute the spectral shape $\Omega_{\text{gw}}(f)$ of the stochastic noise floor across the MHz–GHz band, incorporating spectral dilution and quadrupole coupling suppression, and determine whether the resulting amplitude is consistent with existing observational upper bounds. This is the most pressing empirical test of the framework.
**(5) Universality Beyond GOE.** Extend the full-rank covariance result from the GOE ensemble to broader classes of Hamiltonians, establishing that the indivisibility conclusion does not depend on the specific random matrix model.
**(6) Sign Structure of the Hidden Sector.** Provide a first-principles argument — or identify physical conditions under which — the hidden-sector energy contributions carry quasi-random signs, as assumed in the CLT argument underlying the OIT.

---

## 9. CONCLUSION

This paper has argued that the structural incompatibility between quantum mechanics and general relativity is not a failure of either theory, but a plausible mathematical consequence of embedded observation within a classical universe. Applying Wolpert’s inference limits to the causal horizon structure of general relativity, the **Observational Incompleteness Theorem** is proposed, arguing that vacuum energy measurements are complementary projections of a shared hidden sector. Under the physical assumption that hidden-sector contributions carry quasi-random signs, the 10^122^ cosmological constant discrepancy is reinterpreted as encoding the hidden sector’s dimensionality, yielding $N \sim$ 10^244^ degrees of freedom. The quantitative product bound on these complementary projections remains an open problem.

The transition from the **Observational Incompleteness Theorem** to the **Trace-Out Conjecture** is pursued through a mathematical derivation with clearly stated assumptions. By modeling the hidden-sector Liouvillian as a Gaussian Orthogonal Ensemble (GOE), it is shown that the covariance matrix of marginal transition elements is full-rank within this ensemble, establishing that the observer’s description of the visible sector is indivisible with probability 1 under the GOE model. It is argued that this result extends to physically realistic Hamiltonians via universality, though a rigorous proof remains open. It is demonstrated that the history-dependent memory kernel $K(\tau)$, which explicitly breaks classical divisibility, is dual to the complex phase gradient $\nabla S$ in a unitary representation. 

Under these assumptions and identifications, Hilbert space, the Born rule, and the Schrödinger equation emerge not as fundamental laws, but as the mandatory data-compression algorithms for any observer forced to trace out a correlated, causally inaccessible hidden sector. Quantum mechanics would then be the "epistemic shadow" cast by classical mechanics when viewed from behind a relativistic horizon — the universe a deterministic system that appears quantum precisely because the observer is part of the system it attempts to measure. Whether this interpretation is correct depends on resolving the open problems identified in Section 8.3, particularly the quantitative Wolpert bound, the hidden-sector spectral structure, and the universality extension beyond GOE.

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
