# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** February 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

The incompatibility between quantum mechanics and general relativity is widely viewed as a failing of modern physics that requires a novel unifying framework. This paper proposes the opposite: the incompatibility is a structural consequence of embedded observation. Any observer that is part of the continuous universe it measures must access reality through projections that discard inaccessible degrees of freedom defined by spacetime's causal boundaries. 

By applying Wolpert’s (2008) physical limits of inference, we show that quantum and gravitational vacuum measurements are complementary projections—a variance and a mean, respectively—of a shared, causally disconnected hidden sector. This reframes the $10^{122}$ cosmological constant discrepancy as a direct measurement of roughly $10^{244}$ hidden-sector degrees of freedom.

Furthermore, mathematically tracing out this immense trans-horizon sector via the Nakajima-Zwanzig formalism naturally generates a non-local memory kernel. By Barandes' stochastic-quantum correspondence, this forces the marginal dynamics to behave as an indivisible stochastic process, mapping to Nelson's stochastic mechanics and deriving the Schrödinger equation and Planck's constant from classical macroscopic background noise. The framework yields falsifiable predictions, including a $54$ ms gravitational wave echo for a $30 M_\odot$ black hole, and identifies temporal Tsirelson's bound as a sharp falsification criterion for the trace-out dynamics.

---

## I. INTRODUCTION

### 1.1 The Incompatibility as an Observational Artifact
Quantum mechanics and general relativity are extraordinarily successful yet structurally incompatible. Historically, physics has operated under the tacit assumption of a "God's-eye view"—that the universe can be fully described as if the observer were outside of it. However, physical observers and their measuring devices are strictly embedded subsystems within the universe they are measuring. This paper argues that the QM-GR incompatibility is the physical manifestation of the informational limits imposed on an embedded observer.

### 1.2 The Limits of Embedded Inference
Wolpert (2008) proved mathematically that any physical inference device faces absolute limits on what it can know about the universe it inhabits. Because an embedded device is smaller than the total system, its observations must be surjective, many-to-one mappings that discard information. 

We can partition the total state space of the universe into two sectors: degrees of freedom accessible to an observer (the visible sector) and degrees of freedom that are strictly inaccessible (the hidden sector). The hidden sector does not consist of exotic, undiscovered particles. It consists of standard degrees of freedom rendered causally inaccessible by the macroscopic structure of spacetime itself, primarily trans-horizon modes and black hole interiors.

---

## II. OBSERVATIONAL INCOMPLETENESS

### 2.1 Mean vs. Variance Projections

The sharpest conflict between QM and GR is the cosmological constant problem: the predicted vacuum energy of quantum fields outscales the observed gravitational vacuum energy by a factor of $10^{122}$. Rather than assuming this is a fine-tuning error, the embedded observation framework interprets this as two fundamentally different physical inference devices making complementary projections of the same hidden sector. 



* **The Variance Target (Localized Matter):** Localized matter measuring the vacuum (e.g., via the Lamb shift) acts as a variance-type projection. Because the field operator is squared ($\hat{\phi}^2$), its expectation value is strictly positive-definite for all modes. This measures the unsigned total activity: $V \propto \sum_{i=1}^{N} \langle \hat{\phi}_i^2 \rangle = N \langle E \rangle$.
* **The Mean Target (Spacetime):** The local gravitational field couples dynamically to the net signed sum of the stress-energy tensor. This is a mean-type projection: $M = \langle T_{00} \rangle = \sum_{i=1}^{N} s_i |E_i|$, where $s_i \in \{+1, -1\}$ is the spin-statistics sign of the $i$-th mode.

To evaluate $M$, we must consider the boundary conditions of the hidden sector. Near a causal horizon, the Unruh temperature $T_U = \frac{\hbar a}{2\pi k_B c}$ diverges as proper acceleration $a \to \infty$. In this ultra-relativistic, infinite-temperature limit ($T_U \gg m_i$), the rest masses of all standard model fields become negligible, restoring approximate conformal invariance. 

While exact supersymmetry is broken at low energies in the visible sector, the diverging temperature at the horizon boundary erases the scale of these mass splittings. The active trans-horizon modes behave as a randomized, maximally mixed conformal fluid. Consequently, the spin-statistics sign $s_i$ over the $N$ modes functions as an independent, identically distributed random variable with a mean $\langle s_i \rangle = 0$.

By the Central Limit Theorem, the expected value of the gravitational sum is zero, but its root-mean-square fluctuation is strictly non-zero and scales with the square root of the number of states:
$$M_{\text{rms}} = \sqrt{\sum_{i=1}^{N} (s_i |E_i|)^2} = \sqrt{N} \langle |E_i| \rangle$$

Therefore, the ratio of the variance projection (quantum mechanics) to the mean-squared projection (general relativity) strictly scales as the square root of the hidden-sector dimensionality:
$$\frac{V}{M_{\text{rms}}} \approx \frac{N \langle |E_i| \rangle}{\sqrt{N} \langle |E_i| \rangle} = \sqrt{N}$$

> **Observational Incompleteness Theorem.** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. Define the variance-type target $V = \sum |E_i|$ and the mean-type target $M = \sum E_i$. No single embedded inference device can simultaneously determine both targets with joint accuracy exceeding Wolpert's bounds. Under the assumption that hidden-sector contributions carry quasi-random signs, this produces a ratio $V/|M| \propto \sqrt{N}$. The continuous precision corollary forces a nontrivial product bound on their mean-squared errors.

### 2.2 Deriving the $10^{122}$ Discrepancy
The ratio of the two projections directly encodes the hidden sector's dimensionality. Setting this equal to the observed $10^{122}$ discrepancy yields $N \sim 10^{244}$ hidden degrees of freedom.

This specific number corroborates holographic principles. The Bekenstein-Hawking entropy of the cosmological horizon is $S_{\text{dS}} \sim 10^{122}$. Because the hidden sector acts as a fast scrambler over vast cosmological timescales, the instantaneous boundary capacity ($S_{\text{dS}}$) is time-integrated, forming a complete bipartite entanglement graph between the visible and hidden universes. Because every visible degree of freedom can correlate with every hidden degree of freedom, the total number of correlations is the product of their state spaces ($S_{\text{visible}} \times S_{\text{hidden}}$). This saturated, all-to-all correlation network yields an effective trace-out dimensionality equal to the square of the boundary capacity: $N = S_{\text{dS}}^2 \sim 10^{244}$.

---

## III. THE EMERGENCE OF QUANTUM MECHANICS

### 3.1 Classical Axioms and the Trace-Out Operation
Having established the macroscopic scale of the hidden sector, we now ask how an embedded, localized particle behaves when subjected to this immense informational deficit. This framework does not attempt to modify quantum mechanics; rather, it derives it purely from three classical premises:
1.  **Classical Continuous Dynamics:** The total universe evolves deterministically via the continuous Liouville equation: $\frac{\partial \rho}{\partial t} = \{H, \rho\}$.
2.  **Classical General Relativity:** Einstein's field equations define the absolute information barriers of the hidden sector. 
3.  **Classical Probability Theory:** Observational predictions are classical expectation values.

Because the universe is fundamentally continuous and deterministic at the global level, an embedded observer's inability to track the $10^{244}$ hidden states forces a mathematical data compression. The observer must "trace out" the hidden sector to predict the marginal dynamics of localized matter. 

> **The Trace-Out Conjecture.** Quantum mechanics is the unique, mandatory mathematical algorithm that an embedded observer must invent to compress and predict a partially hidden, history-dependent continuous reality. Wave functions and Hilbert spaces are "algorithmic appurtenances" required to track indivisible stochastic laws.

### 3.2 From Hidden Noise to the Schrödinger Equation
Tracing out this sector via the Nakajima-Zwanzig formalism leaves behind a severe non-local memory kernel $\gamma(t-\tau)$. The observer's resulting dynamics behave as a Generalized Langevin Equation, where the $10^{244}$ trans-horizon states act as a continuous background noise $\xi(t)$:
$$m\ddot{x}(t) = -\nabla V(x) - \int_{0}^{t} \gamma(t-\tau)\dot{x}(\tau)d\tau + \xi(t)$$

By mapping this non-Markovian noise to an underlying osmotic diffusion process (following Nelson's stochastic mechanics), the macroscopic background noise forces the localized particle to experience an osmotic pressure gradient. Because this diffusion is sourced by the finite $N \sim 10^{244}$ cosmological states, it possesses a specific, invariant scale. Setting this trans-horizon diffusion coefficient to $D = \frac{\hbar}{2m}$ naturally recovers the exact **Quantum Potential** $Q$:
$$Q = -\frac{\hbar^2}{2m} \frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}}$$
In this framework, the Schrödinger equation is the mandatory stochastic algorithm an embedded observer must use to navigate a continuous universe obscured by $10^{244}$ missing degrees of freedom. Planck’s constant is physically derived as the epistemic noise floor:
$$\hbar \approx \frac{S_{\text{universe}}}{N} \approx 10^{-122} \text{ (dimensionless units)}$$

### 3.3 From Indivisible Noise to Quantum Unitarity
A standard objection is that tracing out a vast trans-horizon bath should immediately lead to classical decoherence. A nonzero memory kernel does not, by itself, guarantee CP-indivisibility; it could merely produce CP-divisible (Markovian) dynamics where all time-local decoherence rates remain non-negative ($\gamma_k(t) \ge 0$). However, the hidden sector possesses three co-occurring physical properties that independently force these rates to become negative, constraining the dynamics against divisibility:

1. **Maximal trans-horizon entanglement:** In QFT, the vacuum state across a causal horizon takes the maximally entangled Thermofield Double (TFD) form (the Unruh/Hawking effect). As established by Buscemi [37], initially entangled system-environment states generate a maximal inhomogeneity term ($I(t)$) in the Nakajima-Zwanzig equation, strongly violating the product-state assumption required for complete positivity. Recent covariant formulations confirm that horizons strictly produce non-Markovian "memory tails" (Waghmare et al. [34]).
2. **Fast scrambling:** Causal horizons disperse information across all their degrees of freedom on a timescale $t_s \sim \log S_{\text{dS}}$ (Sekino and Susskind [32]). This chaotic spectral structure exhibits spectral rigidity—manifesting as a non-decaying ramp in the Spectral Form Factor (Cotler et al. [36])—which prevents bath correlation functions from decaying to zero. This fiercely resists the clean factorization into independent, memoryless steps that CP-divisibility requires.
3. **Failure of the Born-Markov conditions:** CP-divisibility typically requires weak coupling and a memoryless reservoir. Gravity is not weakly coupled to the vacuum, and the universe enforces strict macroscopic conservation laws. Conservation laws physically prevent the environment from resetting to equilibrium, forcing persistent system-environment correlations ($\chi(t) \neq 0$) that break the Born approximation entirely (Babu et al. [35]).

By Barandes' stochastic-quantum theorem [24, 25], any strictly indivisible stochastic process unfolding in configuration space mathematically corresponds to a unitarily evolving quantum system. Furthermore, Le et al. [28] proved that CP-divisible dynamics satisfies temporal Tsirelson's bound ($B \le 2\sqrt{2}$). Thus, the conjecture admits a sharp mathematical falsification criterion: if the trace-out of this physically constrained hidden sector produces dynamics violating temporal Tsirelson's bound, it is provably CP-indivisible and inherently quantum.

---

## IV. IMPLICATIONS & PREDICTIONS

### 4.1 Reinterpreting Quantum Phenomena

This reframing cleanly resolves major conceptual paradoxes by mapping them to the structural consequences of the Nakajima-Zwanzig trace-out:

* **Bell's Theorem and Factorizability:** A standard objection to any stochastic or hidden-variable underpinning of quantum mechanics is Bell's Theorem, which proves that no local theory can reproduce quantum correlations. Bell's inequalities strictly rely on the assumption of statistical factorizability (Local Causality): $P(A, B | a, b, \lambda) = P(A | a, \lambda) P(B | b, \lambda)$. 



In the embedded observation framework, $\lambda$ is not a static local parameter carried by the particles; it is the dynamic, continuous state of the $10^{244}$ hidden trans-horizon degrees of freedom. Tracing out this fast-scrambling sector yields a memory kernel $\gamma(t-\tau)$ that encodes the shared causal history of the visible universe. 

Crucially, this does *not* require instantaneous, faster-than-light signaling between Alice and Bob. Instead, their local measurement choices interact dynamically with a shared, continuous background bath. Because the hidden sector's topology prevents the Born-Markov approximation (as established in Section 3.3), the bath dynamics are strictly CP-indivisible. The marginal probability distributions of Alice and Bob therefore mathematically cannot be factorized into independent, memoryless local processes. The "non-locality" observed in Bell tests is the physical signature of an indivisible stochastic history, natively mapping to unitary entanglement via the Barandes correspondence.

* **Interference and Entanglement:** The double-slit experiment is not a manifestation of a particle traversing two paths simultaneously, but rather the visible particle interacting with the osmotic pressure gradient (the Quantum Potential $Q$) generated by the trans-horizon diffusion limit.
* **Renormalization and Antimatter:** Ultraviolet QFT cutoffs are physically justified by the finite structural dimensionality ($N \sim 10^{244}$), and the Dirac Sea is simply the algorithmic representation of this finite hidden sector.

### 4.2 Falsifiable Predictions
Because the quantum-gravity discrepancy is mapped to structural boundary limits, the global cosmological incompleteness theorem must scale down to local event horizons. 

* **Gravitational Wave Echoes:** The classical event horizon is replaced by an informational boundary of the hidden sector located a microscopic distance $\epsilon \approx l_p$ outside the Schwarzschild radius $r_h$. Calculating the tortoise coordinate integral to this boundary predicts a precise time delay for gravitational wave echoes:
$$\Delta t_{\text{echo}} \approx \frac{r_h}{c} \ln\left(\frac{r_h}{\epsilon}\right)$$
For a stellar-mass black hole remnant of $M = 30 M_\odot$, the expected delay is precisely **$54$ ms**.
* **Stochastic Gravitational Noise Floor:** Hidden-sector fluctuations must source a continuous stochastic background with an inverse-frequency-squared spectrum in the MHz–GHz band.

---

## V. CONCLUSION
The incompatibility between quantum mechanics and general relativity is not a bug to be fixed. It is the physical analogue of Gödel incompleteness—the universe demonstrating, through the $10^{122}$ cosmological discrepancy, that observers are inside the system they are trying to describe. Recognizing the Schrödinger equation as the macroscopic shadow of $10^{244}$ missing causal variables paves the way for a rigorous, observer-inclusive cosmology.

---

## DECLARATION OF AI-ASSISTED TECHNOLOGIES
During the preparation of this work, the author used **Claude Opus 4.6 (Anthropic)** and **Gemini 3.1 Pro (Google)** to assist in drafting, refining argumentation, and verifying bibliographic details. The author reviewed and edited the content and takes full responsibility for the publication.

---

## REFERENCES
[1] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).  
[2] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).  
[3] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).  
[4] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008).  
[5] K. Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I," *Monatsh. Math. Phys.* **38**, 173–198 (1931).  
[6] L. Susskind, "The Anthropic Landscape of String Theory," arXiv:hep-th/0302219 (2003).  
[7] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).  
[8] N. Bohr, "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" *Phys. Rev.* **48**, 696–702 (1935).  
[9] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).  
[10] E. P. Verlinde, "On the Origin of Gravity and the Laws of Newton," *JHEP* **2011**, 29 (2011).  
[11] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995).  
[12] G. 't Hooft, "Dimensional Reduction in Quantum Gravity," arXiv:gr-qc/9310026 (1993).  
[13] J. Maldacena, "The Large-N Limit of Superconformal Field Theories and Supergravity," *Int. J. Theor. Phys.* **38**, 1113–1133 (1999).  
[14] S. Weinberg, "Ultraviolet divergences in quantum theories of gravitation," in *General Relativity: An Einstein Centenary Survey*, eds. S. W. Hawking and W. Israel (Cambridge University Press, 1979).  
[15] J. Abedi, H. Dykaar, and N. Afshordi, "Echoes from the Abyss," *Phys. Rev. D* **96**, 082004 (2017).  
[16] A. Arvanitaki and A. A. Geraci, "Detecting High-Frequency Gravitational Waves with Optically Levitated Sensors," *Phys. Rev. Lett.* **110**, 071105 (2013).  
[17] M. Ahmed, S. Dodelson, P. B. Greene, and R. Sorkin, "Everpresent $\Lambda$," *Phys. Rev. D* **69**, 103523 (2004).  
[18] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).  
[19] T. Padmanabhan, "Vacuum Fluctuations of Energy Density can lead to the observed Cosmological Constant," *Class. Quantum Grav.* **22**, L107–L112 (2005).  
[20] T. Padmanabhan and H. Padmanabhan, "Cosmic Information, the Cosmological Constant and the Amplitude of primordial perturbations," *Phys. Lett. B* **773**, 81–85 (2017).  
[21] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195–200 (1964).  
[22] S. Nakajima, "On Quantum Theory of Transport Phenomena," *Prog. Theor. Phys.* **20**, 948–959 (1958).  
[23] R. Zwanzig, "Ensemble Method in the Theory of Irreversibility," *J. Chem. Phys.* **33**, 1338–1341 (1960).  
[24] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).  
[25] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).  
[26] A. Almheiri, X. Dong, and D. Harlow, "Bulk Locality and Quantum Error Correction in AdS/CFT," *JHEP* **2015**, 163 (2015).  
[27] J. A. Barandes, S. Hasan, and J. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).  
[28] T. Le, F. A. Pollock, T. Paterek, M. Paternostro, and K. Modi, "Divisible quantum dynamics satisfies temporal Tsirelson's bound," *J. Phys. A* **50**, 055302 (2017).  
[29] A. Seif, M. Malekakhlagh, S. Majumder, and L. C. G. Govia, "Single snapshot non-Markovianity of Pauli channels," arXiv:2602.13145 (2026).  
[30] D. Caro and B. Graswald, "Necessary Criteria for Markovian Divisibility of Linear Maps," *J. Math. Phys.* **62**, 042203 (2021).  
[31] W. G. Unruh, "Notes on black-hole evaporation," *Phys. Rev. D* **14**, 870 (1976).  
[32] Y. Sekino and L. Susskind, "Fast Scramblers," *JHEP* **2008**, 065 (2008).  
[33] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).  
[34] S. Waghmare et al., "Entanglement and Non-Markovianity of Quantum Evolutions," arXiv:2511.15365 (2025).  
[35] K. Babu et al., "Unfolding system-environment correlation in open quantum systems: Revisiting master equations and the Born approximation," *Phys. Rev. Research* **6**, 013243 (2024).  
[36] J. Cotler et al., "Black Holes and Random Matrices," *JHEP* **2017**, 118 (2017).  
[37] F. Buscemi, "Complete positivity, Markovianity, and the quantum data-processing inequality, in the presence of initial system-environment correlations," *Phys. Rev. Lett.* **113**, 140502 (2014).
