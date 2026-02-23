# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum
**Date:** February 2026
**Status:** DRAFT PRE-PRINT
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

The incompatibility between quantum mechanics and general relativity is a structural consequence of embedded observation. Any observer that is part of the continuous universe it measures must access reality through projections that discard inaccessible degrees of freedom defined by spacetime's causal structure. The **Observational Incompleteness Theorem** applies Wolpert's (2008) inference limits: quantum and gravitational vacuum energy measurements are variance-type and mean-type projections of a shared hidden sector, and no embedded device can simultaneously determine both. Under this identification, the $10^{122}$ cosmological constant discrepancy is reinterpreted as a measurement of roughly $10^{244}$ hidden-sector degrees of freedom.

The **Trace-Out Conjecture** demonstrates that quantum mechanics is not a fundamental physical law, but an effective, macroscopic data-compression algorithm invented by the observer to handle this continuous information loss. Assuming classical Liouville dynamics and general relativity, correlations generically break the strict continuous-time divisibility of the marginal stochastic dynamics. By Barandes' stochastic-quantum correspondence, this indivisible process is structurally isomorphic to unitary quantum mechanics. The framework interprets the **double-slit experiment**, **superposition**, **entanglement**, **Dirac antimatter**, and **QED renormalization** as direct experimental evidence for this observational incompleteness.

---

## 1. THE PROBLEM

### 1.1 The Incompatibility
Quantum mechanics and general relativity are extraordinarily successful yet structurally incompatible. This paper proposes that the incompatibility is a consequence of embedded observation—specifically, the informational limits imposed on an observer that is itself a subsystem of the universe it measures. 

### 1.2 The Cosmological Discrepancy
The sharpest manifestation of the QM–GR incompatibility is the **cosmological constant problem**. It concerns the single quantity that both frameworks predict: the energy density of empty space, $\rho_{\text{vac}}$.

**Quantum mechanics** computes the vacuum energy by summing zero-point fluctuations of all quantum field modes up to the Planck scale:
$$\rho_{\text{QM}} \sim \frac{E_{\text{Pl}}^{\,4}}{(\hbar c)^3} \sim 10^{113} \; \text{J/m}^3$$

**General relativity** measures the vacuum energy through its gravitational effect—the accelerated expansion of the universe:
$$\rho_{\text{grav}} = \frac{\Lambda \, c^2}{8\pi G} \sim 6 \times 10^{-10} \; \text{J/m}^3$$

The ratio is conventionally rounded to $10^{122}$ in the literature. This paper offers a different interpretation: **neither calculation is wrong. They disagree because they are answering fundamentally different questions about the same physical sector**.

---

## 2. OBSERVATIONAL INCOMPLETENESS

### 2.1 Observers Are Embedded
Wolpert (2008) proved that any physical inference device faces fundamental limits on what it can know about the universe it inhabits. These limits follow solely from the logical structure of a device that is embedded in the system it attempts to describe, forcing any observation to be a surjective, many-to-one mapping that discards information. 

### 2.2 The Hidden Sector
Let the full state space be partitioned into degrees of freedom accessible to observers (the visible sector) and degrees of freedom that are not (the hidden sector, denoted $\Phi$). This partition is defined by classical general relativity: degrees of freedom behind event horizons or beyond causal reach constitute the physical hidden sector. 

### 2.3 Two Projections of the Same Thing
Following Wolpert, we define two complementary inference targets on the hidden sector's energy distribution $\{E_i\}$:

* **Target 1 (Total Unsigned Power):** QFT operationalizes the vacuum via the fluctuation power spectrum, summing the absolute magnitudes of zero-point energies: $V = \sum |E_i|$.
* **Target 2 (Mean-Field Pressure):** The Einstein field equations couple curvature to the net signed sum of the stress-energy tensor: $M = \langle T_{00} \rangle = \sum E_i$.

Assuming the hidden-sector degrees of freedom lack an unbroken symmetry that aligns all their signs, these contributions act as quasi-independent variables. By the central limit theorem, the mean-type projection scales as $|M| \sim \sqrt{N}$, while the variance-type projection scales strictly linearly: $V \propto N$. 

### 2.4 The Observational Incompleteness Theorem

> **Observational Incompleteness Theorem.** Let the universe be partitioned into visible and hidden sectors. Define the variance-type target $V = \sum |E_i|$ and the mean-type target $M = \sum E_i$. Then: (i) $V$ and $M$ are distinct surjective functions of the same microstate; (ii) any embedded inference device faces fundamental limits on simultaneously determining both targets; and (iii) under the assumption that hidden-sector contributions carry quasi-random signs, $V \propto N$ while $|M| \propto \sqrt{N}$, producing a ratio $V/|M| \propto \sqrt{N}$.

### 2.5 Extracting the Hidden-Sector Dimensionality
The ratio of the two projections directly encodes the hidden sector's dimensionality:
$$\frac{V}{|M|} \sim \frac{N}{\sqrt{N}} = \sqrt{N}$$
Setting this equal to the observed discrepancy ($10^{122}$):
$$\sqrt{N} \sim 10^{122} \implies N \sim 10^{244}$$

---

## 3. FORMALIZING THE TRACE-OUT ALGORITHM

### 3.1 Classical Premises of the Hidden Sector
The derivation proceeds from three classical premises:

* **Premise 1: Classical Continuous Dynamics.** The total universe evolves deterministically via the continuous Liouville equation: $\frac{\partial \rho}{\partial t} = \{H, \rho\}$.
* **Premise 2: Classical General Relativity.** Einstein's field equations define the absolute information barriers of the hidden sector. 
* **Premise 3: Classical Probability Theory.** Observational predictions are classical expectation values.

### 3.2 The Trace-Out Conjecture
> **The Trace-Out Conjecture.** Quantum mechanics is the unique, mandatory mathematical algorithm that an embedded observer must invent to compress and predict a partially hidden, history-dependent continuous reality. Wave functions and Hilbert spaces are "algorithmic appurtenances" (Barandes, 2025) required to track indivisible stochastic laws.

*To bridge the gap between these deterministic premises and the epistemic algorithm of quantum mechanics, we must identify the exact mathematical mechanism that operationalizes this data compression. Specifically, we need to map the continuous, history-dependent dynamics of the hidden sector onto the spatial probability distributions accessible to the observer.*

### 3.3 The Noise-to-Potential Map
To formalize this transition between the classical Liouville Equation and the Schrödinger equation, we define the transformation mapping the temporal memory integral into the spatial Laplacian. 

The observer's marginal dynamics behave as a Generalized Langevin Equation:
$$m\ddot{x}(t) = -\nabla V(x) - \int_{0}^{t} \gamma(t-\tau)\dot{x}(\tau)d\tau + \xi(t)$$

Under the **Stochastic-Quantum Correspondence**, this temporal non-locality is algorithmically re-encoded as the **Quantum Potential** $Q$:
$$Q = -\frac{\hbar^2}{2m} \frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}}$$
The Laplacian ($\nabla^2$) is the physical signature of the "shot noise" $\xi(t)$ from the $10^{244}$ hidden variables as they diffuse across the causal horizon.

### 3.4 Horizon-Anchored Derivation of Planck's Constant
Planck’s constant is reinterpreted as the "epistemic noise floor"—the minimum statistical resolution created by the $10^{244}$ hidden states.

* **Statistical Scaling of the Causal Bulk:** The conventional holographic bound ($S \sim 10^{122}$) does not count the absolute number of bulk microstates, but rather the maximum observable information—the mean-field projection—accessible at the causal horizon. As established in Section 2.5, the informational shadow upon this boundary scales as $\sqrt{N}$ strictly due to the Central Limit Theorem. Therefore, an observable horizon entropy of $\sqrt{N} \sim 10^{122}$ physically necessitates a hidden statistical bulk dimensionality of $N \sim (10^{122})^2 = 10^{244}$. The squaring is a structural consequence of statistical projection, circumventing standard spatial geometric scaling.
* **Scale Identification:** $\hbar$ is the ratio of the total action of the observable volume to the hidden-sector count:
$$\hbar \approx \frac{S_{\text{universe}}}{N} \approx 10^{-122} \text{ (dimensionless units)}$$
This identifies $\hbar$ as a dynamic scale factor tied to the Hubble radius and the variance of the hidden sea.

---

## 4. RESOLUTION OF OBSERVED PARADOXES

### 4.1 Quantum Shadows
* **The Double-Slit Experiment:** Interference patterns are the physical signature of the "Trace-Out" operation. 
* **Superposition and Entanglement:** Superposition is statistical ignorance of microstates behind the $10^{122}$ discrepancy. Entanglement is the algorithmic tracking of shared classical correlations that remain non-factorizable due to Noether conservation.
* **Tunneling and Uncertainty:** Tunneling results from kinetic "kicks" from hidden fluctuations. The Uncertainty Principle represents the minimum informational error bound ($1/\sqrt{N}$) when mapping a $10^{244}$-dimensional reality onto single visible targets.

### 4.2 Relativistic Data Compression
* **Dirac Antimatter and the Finite Sea:** "Antimatter" is the algorithmic representation of hidden-sector backflow. The "Dirac Sea" is identified with the finite $10^{244}$ hidden degrees of freedom.
* **Feynman QED as Data Compression:** Path integrals represent the statistical sum over unknown classical trajectories forced by the hidden sector. 
* **Renormalization as the Holographic Cutoff:** Ultraviolet cutoffs are physically justified by the finite dimensionality ($N \sim 10^{244}$) of the hidden sector. 

---

## 5. EXPERIMENTAL PREDICTIONS

* **Prediction 1: Gravitational Wave Echoes.** The resulting expected delay for a $30 M_\odot$ remnant is $\Delta t_{\text{echo}} \approx 54$ ms. 
* **Prediction 2: Stochastic Gravitational Noise Floor.** Hidden-sector fluctuations must source a stochastic background, whose viability depends on spectral dilution across 61 frequency decades.

---

## 6. CONCLUSION

The incompatibility between quantum mechanics and general relativity is an observational artifact. Paradoxes such as QED, Dirac's antimatter, and double-slit interference are the macroscopic evidence for the **Observational Incompleteness Theorem**. Quantum mechanics is the "epistemic shadow" of this incompleteness—the unavoidable algorithmic approximation forced upon the observer by the absolute information barriers of general relativity.

---

## REFERENCES

[1] D. H. Wolpert, "Physical Limits of Inference," *Physica D* **237**, 1257–1281 (2008).
[2] S. Weinberg, "The Cosmological Constant Problem," *Rev. Mod. Phys.* **61**, 1 (1989).
[3] J. Martin, "Everything You Always Wanted to Know About the Cosmological Constant Problem," *C. R. Phys.* **13**, 566–665 (2012).
[4] M. Ahmed et al., "Everpresent $\Lambda$," *Phys. Rev. D* **69**, 103523 (2004).
[5] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).
[6] T. Padmanabhan, "Vacuum Fluctuations Can Lead to the Observed Cosmological Constant," *Class. Quant. Grav.* **22**, L107 (2005).
[7] H. Mori, "Transport, Collective Motion, and Brownian Motion," *Prog. Theor. Phys.* **33**, 423 (1965).
[8] R. Zwanzig, "Ensemble Method in the Theory of Irreversibility," *J. Chem. Phys.* **33**, 1338 (1960).
[9] J. G. Kemeny and J. L. Snell, *Finite Markov Chains* (Van Nostrand, 1960).
[10] L. Gurvits and J. Ledoux, "Markov Property for a Function of a Markov Chain," *Lin. Alg. Appl.* **404**, 85–117 (2005).
[11] G. Elfving, "Zur Theorie der Markoffschen Ketten," *Acta Soc. Sci. Fenn. A* **2**, 1–17 (1937).
[12] M. Casanellas et al., "The Embedding Problem for Markov Matrices," *Publ. Mat.* **67**, 411–445 (2023).
[13] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**, 8 (2025).
[14] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).
[15] J. A. Barandes et al., "The CHSH Game and Causal Locality," arXiv:2512.18105 (2025).
[16] C. Wetterich, *The Probabilistic World* (Springer, 2025).
[17] C. Wetterich, "Quantum Mechanics from Classical Statistics," *J. Phys.: Conf. Ser.* **174**, 012008 (2009).
[18] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).
[19] S. L. Adler, *Quantum Theory as an Emergent Phenomenon* (Cambridge, 2004).
[20] E. Nelson, "Derivation of the Schrödinger Equation from Newtonian Mechanics," *Phys. Rev.* **150**, 1079 (1966).
[21] T. C. Wallstrom, "Inequivalence Between Schrödinger and Madelung Equations," *Phys. Rev. A* **49**, 1613 (1994).
[22] S. Milz and K. Modi, "Quantum Stochastic Processes," *PRX Quantum* **2**, 030201 (2021).
[23] J. Szangolies, "Epistemic Horizons and the Foundations of QM," *Found. Phys.* **48**, 1669 (2018).
[24] R. D. Sorkin, "Spacetime and Causal Sets," in *Relativity and Gravitation* (World Scientific, 1991).
[25] J. A. Barandes, "Quantum Systems as Indivisible Stochastic Processes," arXiv:2507.21192 (2025).
