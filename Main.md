# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** February 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

The incompatibility between quantum mechanics and general relativity is a structural consequence of embedded observation. Any observer that is part of the universe it measures must access reality through projections that discard causally inaccessible degrees of freedom. Because this causal boundary is determined by the structure of spacetime, the resulting structural incompleteness is a generic feature of embedded observation.

Using Wolpert's (2008) physics-independent impossibility theorems for inference devices, an Observational Incompleteness Theorem is introduced: the quantum-mechanical and gravitational descriptions of vacuum energy correspond to variance-type and mean-type estimations of a hidden sector, and Wolpert's mutual inference impossibility prohibits their simultaneous determination by any embedded inference device.

A natural extension — the Trace-Out Conjecture — proposes that tracing out the hidden sector via the Nakajima-Zwanzig formalism produces indivisible dynamics equivalent to quantum mechanics via Barandes' (2023) stochastic-quantum correspondence. While a purely generic trace-out argument is insufficient to guarantee indivisibility, three co-occurring physical properties of the hidden sector — maximal trans-horizon entanglement, fast scrambling, and macroscopic conservation laws — are shown to independently constrain the dynamics against divisibility, reducing the conjecture to a narrowly scoped open problem with a sharp falsification criterion via temporal Tsirelson's bound.

The 10¹²² cosmological constant discrepancy is not an error but the quantitative signature of this structural incompleteness. Interpreting the 10¹²² as a variance-to-mean ratio yields roughly 10²⁴⁴ hidden-sector degrees of freedom — equal to the square of the Bekenstein-Hawking entropy of the cosmological horizon — converting the cosmological constant problem from a mystery into a measurement.

Specific experimental predictions are offered, including frequency-dependent scaling relations for gravitational wave echoes and a stochastic noise floor quantitatively anchored to the 10¹²² ratio.

---

## 1. THE PROBLEM

### 1.1 The Incompatibility
Quantum mechanics and general relativity are extraordinarily successful yet incompatible. The dominant assumption has been that this incompatibility is a deficiency — that a deeper theory will eventually unify them. The opposite is the case: **the incompatibility is a structural feature of embedded observation.**

### 1.2 The Cosmological Discrepancy
The sharpest manifestation of the QM-GR incompatibility is the **cosmological constant problem** [1]. It concerns the single quantity that both frameworks predict: the energy density of empty space, $\rho_{\text{vac}}$.

**Quantum mechanics** computes the vacuum energy by summing zero-point fluctuations of all quantum field modes up to the Planck scale:

$$\rho_{\text{QM}} \sim \frac{E_{\text{Pl}}^{\,4}}{(\hbar c)^3} \sim 10^{113} \text{J/m}^3$$

**General relativity** measures the vacuum energy through its gravitational effect — the accelerated expansion of the universe:

$$\rho_{\text{grav}} = \frac{\Lambda \, c^2}{8\pi G} \sim 6 \times 10^{-10} \text{J/m}^3$$

The ratio is conventionally rounded to 10¹²⁰ in the literature, or more precisely 10¹²². The standard interpretation is that some unknown mechanism cancels the QFT contribution down to the observed value, requiring fine-tuning to one part in 10¹²². Decades of effort have failed to find such a mechanism [2, 3].

A different interpretation is proposed: **neither calculation is wrong. They disagree because they are answering fundamentally different questions about the same thing.**

---

## 2. THE ARGUMENT

### 2.1 Observers Are Embedded
Wolpert (2008) proved that any physical device performing observation, prediction, or recollection — an "inference device" — faces fundamental limits on what it can know about the universe it inhabits [4]. These limits hold **independent of the laws of physics**. The key mathematical structure is the **setup function** — a mapping from the full universe state space to the device's state space. Wolpert's impossibility requires only that this mapping is surjective and many-to-one: multiple universe states are indistinguishable from the device's perspective. 

### 2.2 The Hidden Sector
Let the full state space be partitioned into degrees of freedom accessible to observers (the visible sector) and degrees of freedom that are not (the hidden sector, denoted $\Phi$). The projection discarding the hidden sector is many-to-one. **There exist properties of the universe that no observer confined to the visible sector can determine.**

The hidden sector consists not of exotic particles but of standard degrees of freedom rendered causally inaccessible by spacetime: (i) trans-horizon modes beyond the cosmological horizon, (ii) sub-Planckian degrees of freedom below the observer's resolution limit, (iii) black hole interiors.

### 2.3 Two Projections of the Same Thing
Vacuum energy is the energy density of the hidden sector. Padmanabhan [19] identified that QFT and gravitational descriptions probe different statistical properties of the same underlying degrees of freedom. However, to formalize this via Wolpert's theorems, we must strictly identify the operational projections each framework actually utilizes.

**Projection 1: The Fluctuation Power Spectrum (QM).** While the formal expectation value of the QFT Hamiltonian admits negative contributions from fermions, QFT's operational access to the vacuum—the phenomena that verify the vacuum's active nature, such as the Lamb shift, spontaneous emission, and vacuum polarization—is driven by the **fluctuation power spectrum**. 

The fluctuation spectrum is characterized by the vacuum expectation value of the squared field operators (e.g., $\langle 0 | \hat{\phi}^2 | 0 \rangle$). Because the operator is squared, its expectation value is strictly positive-definite for every mode, regardless of whether the field is bosonic or fermionic. The "Quantum Projection" is the measure of this unsigned total activity. It is a variance-type sum over all $N$ modes up to the cutoff:

$$V \propto \sum_{i=1}^{N} \langle \hat{\phi}_i^2 \rangle \propto N$$

**Projection 2: Mean-field pressure (Gravity).** Gravity is unique: it does not couple to the fluctuation power spectrum. The Einstein field equations couple spacetime curvature to $\langle T_{\mu\nu} \rangle$, the macroscopic expectation value of the stress-energy tensor. 

Unlike the squared field operators of the fluctuation spectrum, the stress-energy operator is a signed sum. Bosonic sectors contribute positively, fermionic sectors negatively, and vacuum condensates contribute dynamically determined signs. Formally:

$$M = \langle T_{00} \rangle = \sum_{i=1}^{N} s_i \, |E_i|$$

This is the mean of a signed distribution. Assuming the hidden sector lacks an exact, unbroken global symmetry (like perfect supersymmetry) that forces exact mode-by-mode cancellation, the central limit theorem dictates that the macroscopic residual of $N$ quasi-independent contributions scales as the square root of the number of degrees of freedom.

$$M \sim \sqrt{N}$$

The QFT operational projection extracts the fluctuation power spectrum (the unsigned variance-type activity). The gravitational projection extracts the macroscopic stress-energy expectation value (the signed mean). These are fundamentally different mathematical operations on the same hidden sector.

### 2.4 The Physical Inference Devices
A common conceptual hurdle is the assumption that an "inference device" implies a conscious physicist or a computational machine, rendering Wolpert's theorems an epistemological metaphor rather than an ontological limit. In Wolpert's formalism, an inference device is simply any physical subsystem whose state is dynamically correlated with a target system. In this framework, the mathematical descriptions of GR and QM correspond to the physical couplings of two different embedded subsystems interacting with the exact same hidden sector:

**The Gravitational Inference Device (Spacetime).** The local gravitational field itself is the inference device for the mean-type projection. The metric tensor physically couples to the stress-energy of the vacuum via the Einstein field equations. The resulting spacetime curvature is the physical "inference" of that coupling. It is a macroscopic subsystem restricted to feeling the canceled-out residual (the signed mean) of the hidden sector.

**The Quantum Inference Device (Localized Matter).** The inference device for the variance-type projection is localized matter interacting with a quantum field — for example, a hydrogen atom undergoing the Lamb shift, or a particle detector. These finite subsystems do not couple to the macroscopic mean of the universe's stress-energy. Instead, their physical states (e.g., electron energy levels) are perturbed by the absolute magnitude of local vacuum agitation. They act as physical "thermometers" inferring the local fluctuation power spectrum (the unsigned variance).

Because both the gravitational field and localized matter are finite, embedded subsystems, their physical interactions with the hidden sector $\Phi$ are strictly governed by the many-to-one projections required by Wolpert's setup function. The 10¹²² discrepancy is therefore not a theoretical error, but the strict, ontological limit of how much vacuum information these differing physical hardware setups can simultaneously extract.

### 2.5 Formal Statement
Wolpert's mutual inference impossibility requires that the two targets be independently configurable. In the physical hidden sector, the mean depends on the net sign balance, while the variance depends on amplitudes. Unless the ultimate laws of physics rigidly and exactly lock the sign structure to the excitation spectrum, independent configurability holds.

> **Observational Incompleteness Theorem:** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. No single embedded inference device can simultaneously determine both the variance-type and mean-type targets of the hidden-sector distribution with joint accuracy exceeding Wolpert's bounds. The continuous precision corollary forces a nontrivial product bound on their mean-squared errors.

---

## 3. THE RATIO AS MEASUREMENT

### 3.1 Extracting the Hidden-Sector Dimensionality
With $N$ independent degrees of freedom, the quantum projection sums all contributions without regard to sign ($V \propto N$) while the gravitational projection couples to the macroscopic mean ($M \sim \sqrt{N}$). 

**Statistical Typicality.** Deriving $M \sim \sqrt{N}$ does not require the unphysical assumption that all 10²⁴⁴ degrees of freedom are perfectly uncorrelated random coin flips. It simply requires the absence of a global, exact, unbroken symmetry spanning the entire hidden sector. Across vast causal horizons and extreme energy scales, the sum of myriad highly correlated but causally disconnected local patches converges to standard statistical typicality. The $\sqrt{N}$ scaling is the generic macroscopic residual of high-dimensional, complex phase spaces without global symmetry.

$$\frac{V}{M} \sim \frac{N}{\sqrt{N}} = \sqrt{N}$$

Setting this equal to the observed value:

$$\sqrt{N} \sim 10^{122} \implies N \sim 10^{244}$$

### 3.2 The Holographic Structure
The Bekenstein-Hawking entropy of the cosmological horizon is independently $S_{\text{dS}} \sim 10^{122}$ [12, 18]. The hidden-sector dimensionality is therefore:

$$N \sim S_{\text{dS}}^{\,2}$$

The 10¹²² is simultaneously the boundary's information capacity *and* the ratio of what the two projections yield — because the boundary *is* the projection. The relationship $N = S_{\text{dS}}^2$ has a natural architectural interpretation: the total hidden-sector degrees of freedom equal the square of the boundary capacity, consistent with holographic quantum error-correcting code structures [26].

---

## 4. THE TRACE-OUT CONJECTURE

### 4.1 Statement

Tracing out the hidden sector via the Nakajima-Zwanzig formalism [22, 23] produces a reduced description of the visible sector governed by an integro-differential equation with a memory kernel $\mathcal{K}(t, s)$, encoding how the hidden sector's past states influence the visible sector's present. By Barandes' stochastic-quantum correspondence [24, 25], any indivisible stochastic process is exactly equivalent to a unitary quantum system.

> **Trace-Out Conjecture:** Tracing out the hidden sector of this framework produces dynamics that are CP-indivisible in the sense required by the Barandes correspondence. If correct, quantum mechanics is not a fundamental law but the inevitable consequence of embedded observation — what any observer sees after discarding causally inaccessible degrees of freedom.

### 4.2 The Generic Gap

A nonzero memory kernel does not, by itself, guarantee CP-indivisibility. The space of non-Markovian dynamics admits an intermediate regime: processes that possess memory (non-Markovian in the Breuer-Laine-Piilo sense of information backflow) yet remain CP-divisible — decomposable into a sequence of completely positive intermediate maps [33]. The Barandes correspondence requires the stronger condition: the intermediate maps must fail complete positivity.

For an arbitrary system-environment partition with an arbitrary interaction Hamiltonian, one cannot prove from pure mathematics alone that the trace-out lands in the CP-indivisible regime rather than the intermediate one. A purely generic Nakajima-Zwanzig argument is therefore insufficient.

### 4.3 Physical Constraints Against Divisibility

The hidden sector of this framework is not arbitrary. It possesses three specific physical properties — each independently constraining the dynamics away from divisibility.

**Maximal trans-horizon entanglement.** The partition between the visible and hidden sectors is not an abstract mathematical cut but a physical causal horizon. In quantum field theory, the vacuum state across a causal horizon is maximally entangled: modes just inside the boundary are entangled with modes just outside [7, 18, 31]. This is the physical origin of Hawking radiation and the Unruh effect. Tracing out a maximally entangled sector minimizes the purity of the reduced state, maximizing the deviation from any product-state factorization over time. The resulting information backflow — the hidden sector's past rigidly constraining the visible sector's future — is far stronger than for a generic, weakly correlated environment, and acts directly against the memoryless independence required for CP-divisibility.

**Fast scrambling.** As established in §3.2, the hidden sector is structured holographically ($N \sim S_{\text{dS}}^2$). Causal horizons are fast scramblers [32]: they disperse information across all their degrees of freedom on a timescale $t_s \sim \log S_{\text{dS}}$, exponentially fast relative to the system size. A perturbation the visible sector imprints on the hidden sector is therefore rapidly and chaotically distributed across $\sim 10^{244}$ degrees of freedom. The memory kernel generated by a fast-scrambling environment is densely correlated over time, and its chaotic spectral structure resists the clean factorization into independent, completely positive intermediate steps that CP-divisibility requires.

**Failure of the Born-Markov conditions.** In the theory of open quantum systems, CP-divisible (Markovian) dynamics typically arises only when two conditions hold [33]: (i) weak coupling between the system and environment, and (ii) the Born-Markov approximation — the environment is large enough to act as a memoryless reservoir that resets to equilibrium after every interaction. Neither condition is met. Gravity is not weakly coupled to the vacuum; spacetime is constituted by its coupling to the vacuum stress-energy. And the universe is a closed system with strict conservation laws (energy, momentum, charge). The hidden sector cannot instantaneously re-thermalize to a memoryless equilibrium after each interaction without violating those conservation laws. Because the hidden sector must retain a dynamical record of transferred conserved quantities, the resulting dynamics cannot satisfy the memoryless factorization that CP-divisibility demands.

### 4.4 Scope and Falsification

These three constraints — on the initial state (maximal entanglement), the dynamics (fast scrambling), and the global structure (conservation laws) — are not independent hypotheses introduced to rescue the conjecture. They are co-occurring, established physical properties of causal horizons. Together, they reduce the conjecture from the intractable claim that *every* Nakajima-Zwanzig trace-out produces CP-indivisibility to the narrower claim that tracing out a maximally entangled, fast-scrambling sector subject to macroscopic conservation laws produces CP-indivisibility.

An independent line of evidence supports this narrowing. Le et al. [28] proved that CP-divisible dynamics satisfies temporal Tsirelson's bound. Barandes, Hasan, and Kagan [27] derived the spatial Tsirelson bound from indivisibility via the stochastic-quantum correspondence. The conjecture therefore admits a sharp falsification criterion: if the trace-out of the physically constrained hidden sector produces dynamics violating temporal Tsirelson's bound, that dynamics is provably CP-indivisible and the conjecture holds. The open mathematical problem reduces to establishing this violation for the specific class of physically realized hidden-sector Hamiltonians (§6.3).

---

## 5. EXPERIMENTAL PREDICTIONS

If the Observational Incompleteness Theorem is correct, General Relativity is an effective mean-field theory — a statistical summary that is reliable when the underlying degrees of freedom are averaged over slowly and smoothly, but breaks down at scales or in regimes where this averaging fails.

**5.1 Gravitational Wave Echoes (future detectors).** The event horizon is the limit of the mechanical projection. Future observations of binary black hole mergers should detect **post-merger echoes** [15] whose amplitude scales with the ratio of probe frequency to the hidden sector's relaxation frequency. This frequency-dependent slope distinguishes mean-field breakdown from static surface models, which predict frequency-independent reflectivity.

**5.2 Stochastic Gravitational Noise Floor (future detectors).** Since gravity is the mean of a high-variance distribution, it should exhibit statistical fluctuations at high frequencies: a **stochastic gravitational wave background** in the MHz–GHz band [16], with an inverse-frequency-squared spectrum. The amplitude is anchored to the 10¹²² ratio and is falsifiable.

**Remark on detectability.** The echo and noise-floor predictions yield amplitudes far below current sensitivity. The nearest-term empirical connection resides in the correlated running of couplings suggested by the Asymptotic Safety programme (originating in [14]).

---

## 6. DISCUSSION

### 6.1 Relation to Prior Work
The argument connects: Wolpert's inference impossibility [4] as the mathematical foundation, Sorkin's causal-set prediction [17] as independent confirmation of $\Lambda \sim N^{-1/2}$, and — as a conjectured extension (§4) — the Barandes stochastic-quantum correspondence [24, 25] via the Nakajima-Zwanzig trace-out as a potential mechanism by which the quantum projection produces specifically quantum-mechanical statistics. The conjecture is supported by three independent physical constraints on the hidden sector (§4.3) and admits a precise falsification criterion via temporal Tsirelson's bound [28]. The result is compatible with but distinct from Bohr's complementarity [8], 't Hooft's deterministic quantum mechanics [9], and emergent gravity programmes [10, 11] (we do not derive gravity, but identify why the gravitational and quantum descriptions cannot agree). The closest precedent is Padmanabhan [19, 20], whose variance-mean distinction is adapted and rigorously grounded in Wolpert's bounds here.

### 6.2 Key Objections
**"The QFT vacuum energy calculation is just wrong."** The theorem does not depend on the specific value, but on the structural claim that the fluctuation and mechanical measures are computed by different operations. Even if a UV-complete theory reduces the mismatch, the conceptual problem remains.

**"Doesn't this just redescribe the cosmological constant problem?"** The 10¹²² converts from an unexplained free parameter into a derived quantity, corroborated by the de Sitter entropy and generating falsifiable predictions (§5).

**"What about AdS/CFT, where gravity and QFT are exactly unified?"** The AdS/CFT correspondence is not a counterexample; it is a confirmation of the rule. The exact duality is formulated from an *asymptotic boundary*. An observer on the boundary of Anti-de Sitter space is not an embedded observer in the bulk; they are viewing the universe from the outside. Because they are not embedded, their setup function is not restricted by Wolpert's bound. An observer actually living *inside* the AdS bulk would face the exact same causal horizons and embedded incompleteness described here. Furthermore, our universe is de Sitter space ($\Lambda > 0$), which lacks an asymptotic spatial boundary. In our universe, every observer is permanently embedded.

**"A hidden sector mediating correlations between entangled particles is a local hidden variable theory, and Bell's theorem rules those out."** The hidden sector is not a local hidden variable theory in Bell's sense [21]. Bell's theorem requires that hidden variables produce *factorable* statistics. The Trace-Out Conjecture (§4) argues that the hidden sector produces *indivisible* statistics via the Nakajima-Zwanzig memory kernel [22, 23], supported by the physical constraints detailed in §4.3, violating Bell inequalities for the exact same structural reason quantum systems do.

**"This conflates epistemology (what we can measure) with ontology (what exists)."** As outlined in Section 2.4, the local gravitational field and localized matter physically act as the inference devices. The limitations are topological and ontological. The theorem does not preclude a single true vacuum state existing, but proves that the physical couplings to that state are structurally restricted.

**"The QM-GR incompatibility has concrete mathematical manifestations that no interpretive framework can dissolve."** Non-renormalizability of perturbative quantum gravity, the frozen-time problem, and the information paradox are structural features of the mathematical theories. The theorem's scope is limited to the cosmological constant problem. 

### 6.3 Open Problems
(1) The tight functional form of the continuous precision trade-off; (2) whether the $N \sim S_{\text{dS}}^2$ bipartite structure can be derived from holographic error-correcting code constraints; (3) whether the Einstein field equations can be derived as the mean-field equation governing the mechanical projection.

**On the Trace-Out Conjecture.** (4) Prove that CP-divisibility is incompatible with the joint constraints of maximal trans-horizon entanglement, fast-scrambling dynamics ($t_s \sim \log S_{\text{dS}}$), and macroscopic conservation laws — or equivalently, that the Nakajima-Zwanzig trace-out under these constraints produces dynamics violating temporal Tsirelson's bound [28]; (5) whether the Barandes-Hasan-Kagan derivation of the Tsirelson bound [27] extends from the CHSH inequality to all Bell-type inequalities; (6) whether the spectral statistics of fast-scrambling Hamiltonians [32] are formally incompatible with the algebraic conditions for CP-divisibility [30].

---

## 7. CONCLUSION
Embedded observers face irreducible inference limits (Wolpert). Quantum mechanics and general relativity represent two structurally incompatible projections of the same hidden sector. The 10¹²² cosmological constant discrepancy is the quantitative signature of this incompleteness, converting from a problem into a measurement of ~$10^{244}$ hidden-sector degrees of freedom — the square of the de Sitter entropy — with $\Lambda \sim N^{-1/2}$ independently confirmed by Sorkin.

If correct, the incompatibility between quantum mechanics and gravity is not a bug to be fixed. It is the physical analogue of Gödel incompleteness [5] — the universe telling observers, in the starkest numerical terms available, that they are inside the system they are trying to describe.

---

## DECLARATION OF AI-ASSISTED TECHNOLOGIES
During the preparation of this work, the author used **Claude Opus 4.6 (Anthropic)** and **Gemini 3.1 Pro (Google)** to assist in drafting, refining argumentation, and verifying bibliographic details. The author reviewed and edited the content and takes full responsibility for the publication.

---

## REFERENCES
[1] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).
[2] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).
[3] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001). arXiv:astro-ph/0004075.
[4] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008). arXiv:0708.1362.
[5] K. Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I," *Monatsh. Math. Phys.* **38**, 173–198 (1931).
[6] L. Susskind, "The Anthropic Landscape of String Theory," arXiv:hep-th/0302219 (2003).
[7] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).
[8] N. Bohr, "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" *Phys. Rev.* **48**, 696–702 (1935).
[9] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).
[10] E. P. Verlinde, "On the Origin of Gravity and the Laws of Newton," *JHEP* **2011**, 29 (2011). arXiv:1001.0785.
[11] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995). arXiv:gr-qc/9504004.
[12] G. 't Hooft, "Dimensional Reduction in Quantum Gravity," arXiv:gr-qc/9310026 (1993).
[13] J. Maldacena, "The Large-N Limit of Superconformal Field Theories and Supergravity," *Int. J. Theor. Phys.* **38**, 1113–1133 (1999).
[14] S. Weinberg, "Ultraviolet divergences in quantum theories of gravitation," in *General Relativity: An Einstein Centenary Survey*, eds. S. W. Hawking and W. Israel (Cambridge University Press, 1979).
[15] J. Abedi, H. Dykaar, and N. Afshordi, "Echoes from the Abyss," *Phys. Rev. D* **96**, 082004 (2017).
[16] A. Arvanitaki and A. A. Geraci, "Detecting High-Frequency Gravitational Waves with Optically Levitated Sensors," *Phys. Rev. Lett.* **110**, 071105 (2013).
[17] M. Ahmed, S. Dodelson, P. B. Greene, and R. Sorkin, "Everpresent $\Lambda$," *Phys. Rev. D* **69**, 103523 (2004). arXiv:astro-ph/0209274.
[18] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).
[19] T. Padmanabhan, "Vacuum Fluctuations of Energy Density can lead to the observed Cosmological Constant," *Class. Quantum Grav.* **22**, L107–L112 (2005). arXiv:hep-th/0406060.
[20] T. Padmanabhan and H. Padmanabhan, "Cosmic Information, the Cosmological Constant and the Amplitude of primordial perturbations," *Phys. Lett. B* **773**, 81–85 (2017). arXiv:1703.06144.
[21] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195–200 (1964).
[22] S. Nakajima, "On Quantum Theory of Transport Phenomena," *Prog. Theor. Phys.* **20**, 948–959 (1958).
[23] R. Zwanzig, "Ensemble Method in the Theory of Irreversibility," *J. Chem. Phys.* **33**, 1338–1341 (1960).
[24] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).
[25] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).
[26] A. Almheiri, X. Dong, and D. Harlow, "Bulk Locality and Quantum Error Correction in AdS/CFT," *JHEP* **2015**, 163 (2015). arXiv:1411.7041.
[27] J. A. Barandes, S. Hasan, and J. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).
[28] T. Le, F. A. Pollock, T. Paterek, M. Paternostro, and K. Modi, "Divisible quantum dynamics satisfies temporal Tsirelson's bound," *J. Phys. A* **50**, 055302 (2017). arXiv:1510.04425.
[29] A. Seif, M. Malekakhlagh, S. Majumder, and L. C. G. Govia, "Single snapshot non-Markovianity of Pauli channels," arXiv:2602.13145 (2026).
[30] D. Caro and B. Graswald, "Necessary Criteria for Markovian Divisibility of Linear Maps," *J. Math. Phys.* **62**, 042203 (2021).
[31] W. G. Unruh, "Notes on black-hole evaporation," *Phys. Rev. D* **14**, 870 (1976).
[32] Y. Sekino and L. Susskind, "Fast Scramblers," *JHEP* **2008**, 065 (2008). arXiv:0808.2096.
[33] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).
