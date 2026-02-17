# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** February 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

This paper argues that the incompatibility between quantum mechanics and general relativity is a structural consequence of embedded observation. Any observer that is part of the universe it measures must access reality through projections that discard causally inaccessible degrees of freedom. Using Wolpert's (2008) physics-independent impossibility theorems for inference devices, an Observational Incompleteness Theorem is introduced: the quantum-mechanical and gravitational descriptions of vacuum energy correspond to variance and mean estimations of a hidden sector, and Wolpert's mutual inference impossibility prohibits their simultaneous determination by any embedded observer. The 10¹²⁰ cosmological constant discrepancy is not an error but the quantitative signature of this structural incompleteness. Interpreting the 10¹²⁰ as a variance-to-mean ratio yields roughly 10²⁴⁰ hidden-sector degrees of freedom — equal to the square of the Bekenstein-Hawking entropy of the cosmological horizon — converting the cosmological constant problem from a mystery into a measurement. Specific experimental predictions are offered, including near-term null predictions for beyond-Standard-Model particles and longer-term frequency-dependent scaling relations for gravitational wave echoes and a stochastic noise floor quantitatively anchored to the 10¹²⁰ ratio.

---

## 1. THE PROBLEM

### 1.1 The Incompatibility

Quantum mechanics and general relativity are extraordinarily successful yet incompatible. The dominant assumption has been that this incompatibility is a deficiency — that a deeper theory will eventually unify them. This paper proposes the opposite: **the incompatibility is a structural feature of embedded observation.**

### 1.2 The Cosmological Discrepancy

The sharpest manifestation of the QM-GR incompatibility is the **cosmological constant problem** [1]. It concerns the single quantity that both frameworks predict: the energy density of empty space, $\rho_{\text{vac}}$.

**Quantum mechanics** computes the vacuum energy by summing zero-point fluctuations of all quantum field modes up to the Planck scale:

$$\rho_{\text{QM}} \sim \frac{E_{\text{Pl}}^{\,4}}{(\hbar c)^3} \sim 10^{110} \text{J/m}^3$$

**General relativity** measures the vacuum energy through its gravitational effect — the accelerated expansion of the universe:

$$\rho_{\text{grav}} = \frac{\Lambda \, c^2}{8\pi G} \sim 6 \times 10^{-10} \text{J/m}^3$$

The ratio:

$$\frac{\rho_{\text{QM}}}{\rho_{\text{grav}}} \sim 10^{120}$$

is the largest quantitative disagreement in all of physics. The standard interpretation is that some unknown mechanism cancels the QFT contribution down to the observed value, requiring fine-tuning to one part in $10^{120}$. Decades of effort have failed to find such a mechanism [2, 3].

A different interpretation is proposed: **neither calculation is wrong. They disagree because they are answering fundamentally different questions about the same thing.**

---

## 2. THE ARGUMENT

### 2.1 Observers Are Embedded

Wolpert (2008) proved that any physical device performing observation, prediction, or recollection — an "inference device" — faces fundamental limits on what it can know about the universe it inhabits [4]. These limits hold **independent of the laws of physics**:

**(a)** There exists at least one function of the universe state that the device cannot correctly compute — regardless of its computational power or the determinism of the underlying physics.

**(b)** No two distinguishable inference devices can fully infer each other's conclusions (the "mutual inference impossibility").

These are physics-independent analogues of the Halting theorem, extended to physical devices embedded in physical universes [4]. The key mathematical structure is the **setup function** — a mapping from the full universe state space to the device's state space. Wolpert's impossibility requires only that this mapping is surjective and many-to-one: multiple universe states are indistinguishable from the device's perspective. This condition is trivially satisfied by any observer that is part of the universe it measures.

### 2.2 The Hidden Sector

Let the full state space be partitioned into degrees of freedom accessible to observers (the visible sector) and degrees of freedom that are not (the hidden sector, denoted $\Phi$). The projection discarding the hidden sector is many-to-one and therefore satisfies the requirements of a Wolpert setup function. **There exist properties of the universe that no observer confined to the visible sector can determine.**

The hidden sector consists not of exotic particles but of standard degrees of freedom rendered causally inaccessible by the structure of spacetime: (i) trans-horizon modes beyond the cosmological horizon, (ii) sub-Planckian degrees of freedom below the observer's resolution limit, and (iii) black hole interiors. The partition between visible and hidden is a property of the observer's position, not of the hidden sector's content.

### 2.3 Two Projections of the Same Thing

Vacuum energy is the energy density of the hidden sector. When physicists measure or calculate it, they are attempting to characterize $\Phi$ from within the visible sector.

Padmanabhan [19] identified the central structural point: the QFT and gravitational descriptions probe different statistical properties of the same underlying degrees of freedom. He argued that classical gravity probes vacuum *fluctuations* rather than mean energy density. The present framework adopts Padmanabhan's core insight but **inverts the assignment** and grounds it in the impossibility results of §2.4–2.5. The inversion is motivated by each framework's coupling structure: QFT computes a sum of positive-definite zero-point energies ($+\frac{1}{2}\hbar\omega$ per mode, no cancellation possible), the defining property of a variance-type estimator; the Einstein equations couple to the full stress-energy tensor, which is not positive-definite and admits inter-sector cancellation (bosonic vs. fermionic, condensates), the defining property of a mean-type estimator:

**Projection 1: Fluctuation statistics (QM).** The QFT vacuum energy sums zero-point energies mode by mode — each contributing $+\frac{1}{2}\hbar\omega$, proportional to the position and momentum variances of the quantum ground state. No cancellation is possible. This is a variance-type quantity:

$$V = \sum_{i=1}^{N} \frac{1}{2}\hbar\omega_i \propto N$$

**Projection 2: Mean-field pressure (gravity).** The stress-energy tensor is not positive-definite: different field sectors contribute with signs $s_i = \pm 1$, and the Einstein equations couple to the net signed aggregate. This is a mean-type quantity:

$$M = \sum_{i=1}^{N} s_i \,\frac{1}{2}\hbar\omega_i \sim \sqrt{N}$$

where the $\sqrt{N}$ scaling follows from the central limit theorem when the signs are not fine-tuned — the same scaling underlying Padmanabhan's geometric mean result [19].

### 2.4 Why They Cannot Be Unified

The two projections require **incompatible operations on the hidden sector.** The quantum projection *traces out* the hidden sector — it requires $\Phi$ to be inaccessible. The gravitational projection *couples to* the hidden sector — it requires $\Phi$ to be mechanically present. No single description available to an embedded observer can simultaneously hide and reveal $\Phi$.

Because the two operations extract independent statistical moments of $\Phi$ (variance and mean respectively), Wolpert's mutual inference impossibility provides a quantitative bound on their simultaneous determination.

> **Observational Incompleteness Theorem (informal):** For any embedded observer, the quantum-mechanical and gravitational descriptions of vacuum energy are structurally incompatible projections that cannot be unified into a single observer-accessible description. The cosmological constant problem is the observable signature of this structural incompleteness.

### 2.5 Formal Statement

**Setup.** The universe state is partitioned into visible and hidden sectors. Two target functions are defined: the fluctuation content of the hidden sector (its variance, corresponding to QFT vacuum energy) and the net mechanical effect (its mean, corresponding to gravitationally observed vacuum energy).

**Inference devices.** An observer confined to the visible sector constitutes an inference device in Wolpert's sense. Wolpert's framework applies to binary inference tasks, so the continuous targets are binarized by thresholding: Device 1 asks "Is the variance above or below threshold?"; Device 2 asks "Is the mean above or below threshold?" The impossibility holds for every choice of thresholds, and therefore constrains the continuous inference problem a fortiori.

**Independent configurability.** The mutual inference impossibility requires that the two targets be independently configurable. In the physical hidden sector, the mean depends on the net sign balance (determined by spin-statistics and vacuum condensate structure), while the variance depends on amplitudes (controlled by excitation level). These are set by independent physical parameters. If interactions induce partial correlations, the Wolpert bound is conjectured to degrade gracefully — remaining nontrivial for any correlation short of perfect dynamical locking — by analogy with Robertson-Schrödinger and Cramér-Rao trade-off inequalities, where product bounds collapse only at singular (maximally correlated) points. A formal proof remains an open problem (see §5.3). Crucially, even without graceful degradation, the strict binary result already establishes that *perfect* simultaneous inference is impossible; the conjecture concerns only *how much* residual uncertainty persists at partial correlation.

**The bound.** Wolpert's stochastic extension [4, §4, Corollary 2] gives:

$$\epsilon_{\text{fluc}} \cdot \epsilon_{\text{mech}} \leq \frac{1}{4}$$

The one-quarter bound arises because independent configurability ensures the two binary partitions are cross-cutting: for any assignment of conclusions by one device, universe states exist in each equivalence class that defeat the other device's inference. **Perfect inference of one target forces the other to be no better than chance.**

> **Observational Incompleteness Theorem (formal):** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. If the variance and mean of the hidden-sector distribution are independently configurable, then by Wolpert's mutual inference impossibility, no single inference device confined to the visible sector can simultaneously determine both with joint accuracy exceeding one-quarter.

---

## 3. THE DISCREPANCY AS MEASUREMENT

### 3.1 Extracting the Hidden-Sector Dimensionality

Consider a hidden sector with $N$ independent degrees of freedom, each contributing energy of order one in Planck units. The QFT mode-sum is positive-definite: $V \propto N$. The gravitational coupling sees the net result after inter-sector cancellations: $M \sim \sqrt{N}$. Their ratio is a function of $N$ alone:

$$\frac{V}{M} \sim \frac{N}{\sqrt{N}} = \sqrt{N}$$

Setting this equal to the observed value:

$$\sqrt{N} \sim 10^{120}$$

$$\boxed{N \sim 10^{240}}$$

**Remark on the sign structure.** Individual QFT mode zero-point energies are all positive. The effective signs arise at the level of sectors: the total bosonic vacuum energy is positive, the total fermionic vacuum energy is negative. The random-sign model treats each hidden-sector degree of freedom as contributing with an effectively random sign to the net gravitational coupling — justified when the number of distinct sector types is large and their relative magnitudes are not fine-tuned.

### 3.2 The Holographic Coincidence

The Bekenstein-Hawking entropy of the cosmological horizon is independently $S_{\text{dS}} \sim 10^{120}$ [12, 18]. The hidden-sector dimensionality is therefore:

$$N \sim S_{\text{dS}}^{\,2} \sim \left(10^{120}\right)^2 = 10^{240}$$

This is supported by Sorkin's causal-set prediction [17], which derives $\Lambda \sim N^{-1/2}$ from Poisson fluctuations in spacetime atoms — the same functional form as the variance-to-mean scaling — before the 1998 discovery of cosmic acceleration. The value $N \sim 10^{240}$ is an input to Sorkin's model; the genuine prediction is the scaling relation, which independently confirms the statistical structure posited here.

### 3.3 Robustness

The $\sqrt{N}$ scaling is robust: replacing random signs with random complex phases preserves it, and weak pairwise correlations modify the estimate only when the correlation coefficient reaches order $1/N$ — a fine-tuned regime. The result exceeds the number of Planck volumes in the observable universe (~$10^{185}$) by ~$10^{55}$, ruling out "one degree of freedom per Planck volume" and implying a holographic or extra-dimensional structure.

---

## 4. EXPERIMENTAL PREDICTIONS

If the Observational Incompleteness Theorem is correct, General Relativity is an effective mean-field theory that breaks down whenever adiabatic averaging fails.

**4.1 Null Prediction (near-term).** The framework predicts a **null result** for searches for particles invoked to cancel the QFT vacuum energy. If the discrepancy is structural rather than particle-mediated, particles postulated to solve the cosmological constant problem through boson-fermion cancellation should not exist at the required scales. Current LHC bounds have excluded many simplified supersymmetric scenarios; the prediction is that no discovery in the remaining parameter space will resolve the vacuum energy discrepancy.

**4.2 Gravitational Wave Echoes (future detectors).** The event horizon is the limit of the mechanical projection. Future observations of binary black hole mergers should detect **post-merger echoes** [15] whose amplitude scales with the ratio of probe frequency to the hidden sector's relaxation frequency. This frequency-dependent slope distinguishes mean-field breakdown from static surface models, which predict frequency-independent reflectivity.

**4.3 Stochastic Gravitational Noise Floor (future detectors).** Since gravity is the mean of a high-variance distribution, it should exhibit statistical fluctuations at high frequencies: a **stochastic gravitational wave background** in the MHz–GHz band [16], with an inverse-frequency-squared spectrum. The amplitude is anchored to the $10^{120}$ ratio and is falsifiable.

**Remark on detectability.** The echo and noise-floor predictions yield amplitudes far below current sensitivity. Near-term empirical content resides in the null prediction (§4.1) and the correlated running of couplings predicted by the connection to Asymptotic Safety [14].

---

## 5. DISCUSSION

### 5.1 Relation to Prior Work

The argument connects: Wolpert's inference impossibility [4] as the mathematical foundation, and Sorkin's causal-set prediction [17] as independent confirmation of $\Lambda \sim N^{-1/2}$. The framework is compatible with but distinct from Bohr's complementarity [8] (which operates within QM, not between QM and GR), 't Hooft's deterministic quantum mechanics [9], and emergent gravity programmes [10, 11] (we do not derive gravity, but identify why the gravitational and quantum descriptions cannot agree). A companion explainer develops the connection to the Barandes stochastic-quantum correspondence (arXiv:2309.03085; published correspondence paper in *Philosophy of Physics* 3(1):8, 2025). The key claim — that tracing out a temporally correlated environment generically produces indivisible subsystem dynamics — rests on the well-established Nakajima-Zwanzig formalism and Stinespring dilation theorem.

The closest precedent is Padmanabhan [19], whose variance-mean distinction is adopted and inverted in §2.3. His later Cosmic Information programme [20] argued that demanding finite cosmic information requires a positive cosmological constant — compatible with the interpretation offered here. The key advance is the Wolpert grounding (§2.4–2.5), which converts the variance-mean distinction from a suggestive observation into a provable impossibility result.

### 5.2 Key Objections

**"The QFT vacuum energy calculation is just wrong."** The theorem does not depend on the specific value. It depends on the structural claim that the fluctuation and mechanical measures are computed by different operations and need not agree. Even if a UV-complete theory reduces the mismatch from $10^{120}$ to $10^{40}$, the conceptual problem remains.

**"Doesn't this just redescribe the cosmological constant problem?"** The framework converts an unexplained free parameter into a derived quantity: the $10^{120}$ yields ~$10^{240}$ hidden-sector degrees of freedom, corroborated by the de Sitter entropy and Sorkin's scaling. It also generates falsifiable predictions (§4) that the standard formulation does not.

**"The QM-GR incompatibility has concrete mathematical manifestations that no interpretive framework can dissolve."** This is the strongest objection. Non-renormalizability of perturbative quantum gravity, the frozen-time problem, and the information paradox are structural features of the mathematical theories. The theorem's scope is limited to the cosmological constant problem. What it claims is that even if those problems were solved, the variance-mean discrepancy would persist.

### 5.3 Open Problems

(1) A fully continuous formulation via the multi-parameter quantum Cramér-Rao bound; (2) a formal proof that the Wolpert bound degrades continuously under partial correlations; (3) whether the $N \sim S_{\text{dS}}^2$ relationship can be derived rather than observed; (4) whether special relativity can be derived from the hidden sector's propagation structure; (5) whether the Einstein field equations can be derived as the mean-field equation governing the mechanical projection.

---

## 6. CONCLUSION

**First**, embedded observers face irreducible inference limits (Wolpert), quantum mechanics and general relativity represent two structurally incompatible projections of the same hidden sector (the Observational Incompleteness Theorem), and the $10^{120}$ cosmological constant discrepancy is the quantitative signature of this incompleteness.

**Second**, the $10^{120}$ converts from a problem into a measurement: ~$10^{240}$ hidden-sector degrees of freedom — equal to the square of the de Sitter entropy — with $\Lambda \sim N^{-1/2}$ independently confirmed by Sorkin.

If correct, the incompatibility between quantum mechanics and gravity is not a bug to be fixed. It is the physical analogue of Gödel incompleteness — the universe telling observers, in the starkest numerical terms available, that they are inside the system they are trying to describe.

---

## DECLARATION OF AI-ASSISTED TECHNOLOGIES

During the preparation of this work, the author used **Claude Opus 4.6 (Anthropic)** and **Gemini 3 Pro (Google)** to assist in drafting, refining argumentation, and verifying bibliographic details. The author reviewed and edited the content and takes full responsibility for the publication.

---

## REFERENCES

[1] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).

[2] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).

[3] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001). arXiv:astro-ph/0004075.

[4] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008). arXiv:0708.1362.

[5] K. Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I," *Monatsh. Math. Phys.* **38**, 173–198 (1931).

[6] L. Susskind, "The Anthropic Landscape of String Theory," arXiv:hep-th/0302219 (2003).

[7] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).

[8] N. Bohr, "Can quantum-mechanical description of physical reality be considered complete?" *Phys. Rev.* **48**, 696 (1935).

[9] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).

[10] E. P. Verlinde, "On the Origin of Gravity and the Laws of Newton," *JHEP* **2011**, 29 (2011).

[11] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995).

[12] G. 't Hooft, "Dimensional Reduction in Quantum Gravity," arXiv:gr-qc/9310026 (1993).

[13] J. Maldacena, "The Large-N Limit of Superconformal Field Theories and Supergravity," *Int. J. Theor. Phys.* **38**, 1113–1133 (1999).

[14] S. Weinberg, "Ultraviolet divergences in quantum theories of gravitation," in *General Relativity: An Einstein Centenary Survey*, eds. S. W. Hawking and W. Israel (Cambridge University Press, 1979).

[15] J. Abedi, H. Dykaar, and N. Afshordi, "Echoes from the Abyss," *Phys. Rev. D* **96**, 082004 (2017).

[16] A. Arvanitaki and A. A. Geraci, "Detecting High-Frequency Gravitational Waves with Optically Levitated Sensors," *Phys. Rev. Lett.* **110**, 071105 (2013).

[17] S. Ahmed, S. Dodelson, P. B. Greene, and R. Sorkin, "Everpresent $\Lambda$," *Phys. Rev. D* **69**, 103523 (2004). arXiv:astro-ph/0209274.

[18] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).

[19] T. Padmanabhan, "Vacuum Fluctuations of Energy Density can lead to the observed Cosmological Constant," *Class. Quantum Grav.* **22**, L107–L110 (2005). arXiv:hep-th/0406060.

[20] T. Padmanabhan and H. Padmanabhan, "Cosmic Information, the Cosmological Constant and the Amplitude of primordial perturbations," *Phys. Lett. B* **773**, 81–85 (2017). arXiv:1703.06144.

---

*END OF DOCUMENT*
