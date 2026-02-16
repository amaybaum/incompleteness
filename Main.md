# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** February 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

This paper argues that the incompatibility between quantum mechanics and general relativity is a structural consequence of embedded observation. Any observer that is part of the universe it measures must access reality through projections that discard information about causally inaccessible degrees of freedom. Using Wolpert's (2008) physics-independent impossibility theorems for inference devices, an Observational Incompleteness Theorem is introduced: the quantum-mechanical and gravitational descriptions of vacuum energy correspond to variance and mean estimations of a hidden sector, and Wolpert's mutual inference impossibility prohibits their simultaneous determination by any embedded observer. The 10¹²⁰ cosmological constant discrepancy is not an error but the quantitative signature of this structural incompleteness. Interpreting the 10¹²⁰ value as a variance-to-mean ratio, roughly 10²⁴⁰ hidden-sector degrees of freedom are extracted — equal to the square of the Bekenstein-Hawking entropy of the cosmological horizon — converting the cosmological constant problem from a mystery into a measurement. Specific experimental predictions are offered, including near-term null predictions for beyond-Standard-Model particles and longer-term frequency-dependent scaling relations for gravitational wave echoes and a stochastic noise floor quantitatively anchored to the 10¹²⁰ ratio.

---

## 1. THE PROBLEM

### 1.1 The Incompatibility

Quantum mechanics and general relativity are extraordinarily successful yet incompatible. The dominant assumption has been that this incompatibility is a deficiency—that a deeper theory will eventually unify them. This paper proposes the opposite: **the incompatibility is a structural feature of embedded observation.**

### 1.2 The Cosmological Discrepancy

The sharpest manifestation of the QM-GR incompatibility is the **cosmological constant problem** [1]. It concerns the single quantity that both frameworks predict: the energy density of empty space, $\rho_{\text{vac}}$.

**Quantum mechanics** computes the vacuum energy by summing the zero-point fluctuations of all quantum field modes up to the Planck scale cutoff $E_{\text{Pl}}$:

$$\rho_{\text{QM}} \sim \frac{E_{\text{Pl}}^{\,4}}{(\hbar c)^3} \sim 10^{110} \text{J/m}^3$$

**General relativity** measures the vacuum energy through its gravitational effect — the accelerated expansion of the universe — yielding:

$$\rho_{\text{grav}} = \frac{\Lambda \, c^2}{8\pi G} \sim 6 \times 10^{-10} \text{J/m}^3$$

The ratio between them:

$$\frac{\rho_{\text{QM}}}{\rho_{\text{grav}}} \sim 10^{120}$$

is the largest quantitative disagreement in all of physics. The standard interpretation is that one or both calculations must be wrong—that some unknown mechanism cancels the QFT contribution down to the observed value, i.e. $\rho_{\text{QM}} - \delta\rho \stackrel{?}{=} \rho_{\text{grav}}$, requiring fine-tuning to one part in $10^{120}$. Decades of effort have failed to find such a mechanism [2, 3].

A different interpretation is proposed: **neither calculation is wrong. They disagree because they are answering fundamentally different questions about the same thing.** The discrepancy $\rho_{\text{QM}} \neq \rho_{\text{grav}}$ is not an error to be cancelled but a structural consequence of the two frameworks probing the vacuum through incompatible projections.

---

## 2. THE ARGUMENT

### 2.1 Observers Are Embedded

Observers are part of the universe that they observe. This assertion has both physical and mathematical consequences. Wolpert (2008) proved that any physical device performing observation, prediction, or recollection—an "inference device"—faces fundamental limits on what it can know about the universe it inhabits [4]. These limits hold **independent of the laws of physics**:

**(a)** There exists at least one function of the universe state that the inference device cannot correctly compute—regardless of its computational power or the determinism of the underlying physics.

**(b)** No two distinguishable inference devices can fully infer each other's conclusions (the "mutual inference impossibility").

These are physics-independent analogues of the Halting theorem, extended to physical devices embedded in physical universes [4]. The key mathematical structure is the **setup function** — a mapping from the full universe state space to the device's state space. Wolpert's impossibility theorem requires only that this mapping is surjective and many-to-one: multiple universe states are indistinguishable from the device's perspective. This condition is trivially satisfied by any observer that is part of the universe it measures.

### 2.2 The Hidden Sector

Regardless of what specific theory describes the microscopic world, **there exist degrees of freedom that observers cannot directly access.**

Let the full state space be partitioned into degrees of freedom accessible to observers (the visible sector) and degrees of freedom that are not (the hidden sector, denoted $\Phi$). The projection that discards the hidden sector — mapping the full state to a reduced description of the visible sector alone — is many-to-one: many distinct configurations of $\Phi$ yield the same reduced description. It therefore satisfies the requirements of a Wolpert setup function. **There exist properties of the universe that no observer confined to the visible sector can determine.**

The hidden sector consists not of exotic particles but of standard degrees of freedom rendered causally inaccessible by the structure of spacetime: (i) trans-horizon modes beyond the cosmological horizon, (ii) sub-Planckian degrees of freedom below the observer's resolution limit, and (iii) black hole interiors. In each case, the mechanism enforcing hiddenness is the causal structure of spacetime. The partition between visible and hidden is a property of the observer's position, not of the hidden sector's content.

### 2.3 Two Projections of the Same Thing

Vacuum energy is the energy density of the hidden sector. When physicists measure or calculate it, they are attempting to characterize $\Phi$ from within the visible sector. There is more than one way to do this, and the different ways are not equivalent.

Padmanabhan [19] identified the central structural point: the QFT and gravitational descriptions of vacuum energy probe different statistical properties of the same underlying degrees of freedom. He argued that classical gravity probes vacuum *fluctuations* rather than the mean energy density, arriving at the observed dark energy scale as the geometric mean of the Planck and Hubble energy densities: $\rho_{\text{vac}} \simeq \sqrt{\rho_{\text{UV}} \, \rho_{\text{IR}}}$. The present framework adopts Padmanabhan's core insight — that two distinct statistical operations yield the discrepancy — but **inverts the assignment** and grounds it in the impossibility results of §2.4–2.5:

**Projection 1: Fluctuation statistics (QM).** The QFT vacuum energy sums zero-point energies mode by mode — each contributing $+\frac{1}{2}\hbar\omega$, a quantity proportional to the position and momentum variances of the quantum ground state. No cancellation is possible; every term is positive. This is a variance-type quantity:

$$V = \sum_{i=1}^{N} \frac{1}{2}\hbar\omega_i \propto N$$

**Projection 2: Mean-field pressure (gravity).** The stress-energy tensor is not positive-definite: different field sectors (bosonic vs. fermionic, vacuum condensates) contribute with signs $s_i = \pm 1$, and the Einstein equations couple to the net signed aggregate. This is a mean-type quantity:

$$M = \sum_{i=1}^{N} s_i \,\frac{1}{2}\hbar\omega_i \sim \sqrt{N}$$

where the $\sqrt{N}$ scaling follows from the central limit theorem when the signs are not fine-tuned — the same scaling that underlies Padmanabhan's geometric mean result [19].

Physically: gravity acts as an **adiabatic probe**, coupling to the net signed energy-momentum content averaged over all Planck-scale fluctuations. Quantum mechanics probes the **correlation structure** — summing propagators mode by mode, each contributing positively, to measure how much the medium fluctuates.

The ratio of the two projections grows without bound:

$$\frac{V}{M} \sim \frac{N}{\sqrt{N}} = \sqrt{N}$$

### 2.4 Why They Cannot Be Unified

The two projections require **incompatible operations on the hidden sector.**

The quantum projection *traces out* the hidden sector — it requires that $\Phi$ be inaccessible. The gravitational projection *couples to* the hidden sector — it requires that $\Phi$ be mechanically present. One operation hides the hidden sector. The other feels it. No single description available to an embedded observer can simultaneously hide and reveal $\Phi$.

Because the two operations extract independent statistical moments of $\Phi$ (variance and mean respectively), Wolpert's mutual inference impossibility provides a quantitative bound on their simultaneous determination, which is now stated formally.

> **Observational Incompleteness Theorem (informal):** For any embedded observer, the quantum-mechanical and gravitational descriptions of vacuum energy are structurally incompatible projections that cannot be unified into a single observer-accessible description. The cosmological constant problem is the observable signature of this structural incompleteness.

### 2.5 Formal Statement

**Setup.** The universe state is partitioned into visible and hidden sectors. Two target functions are defined: the fluctuation content of the hidden sector (its variance, corresponding to the QFT vacuum energy) and the net mechanical effect (its mean, corresponding to the gravitationally observed vacuum energy).

**Inference devices.** An observer confined to the visible sector constitutes an inference device in Wolpert's sense: the setup function is the projection from the full state to the visible sector. Wolpert's framework applies to binary inference tasks, so the continuous targets are binarized by thresholding: Device 1 asks "Is the variance above or below a given threshold?"; Device 2 asks "Is the mean above or below a given threshold?" The impossibility holds for every choice of thresholds, and therefore constrains the continuous inference problem a fortiori.

**Independent configurability.** The mutual inference impossibility requires that the two targets be independently configurable — that states exist in the hidden sector's state space with the same mean but different variances, and vice versa. In the physical hidden sector, the mean depends on the net sign balance of hidden-sector contributions — where the sign of each sector's contribution depends on its spin-statistics (bosonic vs. fermionic) and vacuum condensate structure — while the variance depends on their amplitudes, controlled by excitation level. These are set by independent physical parameters. If interactions induce partial correlations, the Wolpert bound degrades gracefully, remaining nontrivial for any correlation short of perfect dynamical locking.

**The bound.** Wolpert's Theorem 1 [4] establishes that no single inference device can correctly compute all functions of the universe state. The stochastic extension [4, §4, Corollary 2] generalizes this to probabilistic inference: for two devices sharing the same projection and targeting independently configurable functions, the product of their success probabilities satisfies

$$\epsilon_{\text{fluc}} \cdot \epsilon_{\text{mech}} \leq \frac{1}{4}$$

The one-quarter bound arises because independent configurability ensures the two binary partitions are cross-cutting: for any assignment of conclusions by one device, universe states exist in each equivalence class that defeat the other device's inference. **Perfect inference of one target forces the other to be no better than chance.**

> **Observational Incompleteness Theorem (formal):** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. If the variance and mean of the hidden-sector distribution are independently configurable, then by Wolpert's mutual inference impossibility, no single inference device confined to the visible sector can simultaneously determine both with joint accuracy exceeding one-quarter.

---

## 3. THE $10^{120}$ AS MEASUREMENT

If the $10^{120}$ encodes statistical properties of the hidden sector, it should yield quantitative information about the hidden sector's dimensionality.

### 3.1 Extracting the Hidden-Sector Dimensionality

Consider a hidden sector with $N$ independent degrees of freedom, each contributing energy with a characteristic magnitude of order one in Planck units. Different sectors contribute to the effective cosmological constant with different signs — bosonic fields contribute positively, fermionic fields contribute negatively, and vacuum condensates shift the balance further. The QFT mode-sum sums positive-definite zero-point energies mode by mode, so every contribution adds. The gravitational coupling sees the net result after all inter-sector cancellations.

The **total fluctuation content** (quantum projection) scales as $V \propto N$. The **net mechanical effect** (gravitational projection) scales as $M \sim \sqrt{N}$. The $\sqrt{N}$ scaling of this variance-to-mean ratio, first identified in this context by Padmanabhan [19], allows the $10^{120}$ discrepancy to be read as a measurement. Setting the ratio equal to the observed value:

$$\frac{V}{M} \sim \sqrt{N} \sim 10^{120}$$

$$\boxed{N \sim 10^{240}}$$

**Remark on the sign structure.** Individual QFT mode zero-point energies are all positive ($+\frac{1}{2}\hbar\omega$). The effective signs arise at the level of sectors, not individual modes: the total bosonic vacuum energy is positive, the total fermionic vacuum energy is negative, and other contributions have their own signs. The random-sign model treats each hidden-sector degree of freedom as contributing with an effectively random sign to the net gravitational coupling — an idealization justified when the number of distinct sector types is large and their relative magnitudes are not fine-tuned.

The Planck-unit normalization assumes that the effective contribution of each hidden-sector degree of freedom to the observable projections remains order-unity after coarse-graining. This is the generic expectation for modes at or near the projection boundary — no fine-tuning is required.

### 3.2 The Holographic Coincidence

The Bekenstein-Hawking entropy of the cosmological horizon is independently calculated as $S_{\text{dS}} \sim 10^{120}$ [12, 18]. The number of hidden-sector degrees of freedom is therefore the **square** of the holographic entropy bound:

$$N \sim S_{\text{dS}}^{\,2} \sim \left(10^{120}\right)^2 = 10^{240}$$

This count is independently supported by Sorkin's causal-set prediction [17], which derives the cosmological constant from Poisson fluctuations in the number of spacetime atoms, yielding $N$ of order $10^{240}$ before the 1998 discovery of cosmic acceleration.

### 3.3 Robustness

The square-root-of-$N$ scaling is robust under several modifications. Replacing random signs with random complex phases preserves the scaling. Weak pairwise correlations modify the estimate only marginally, departing from the square-root scaling only when the correlation coefficient reaches order one-over-$N$ — a fine-tuned regime. The result exceeds the number of Planck volumes in the observable universe (roughly $10^{185}$) by some $10^{55}$, ruling out a naive "one degree of freedom per Planck volume" interpretation and implying a holographic or extra-dimensional structure.

---

## 4. EXPERIMENTAL PREDICTIONS

If the Observational Incompleteness Theorem is correct, General Relativity is an effective mean-field theory that breaks down whenever adiabatic averaging fails. This yields distinct observational signatures.

**4.1 Null Prediction (near-term).** The framework predicts a **null result** for searches for supersymmetric partners or inflaton particles invoked to solve the cosmological constant problem. If the vacuum energy discrepancy is structural rather than caused by unknown particles, the particles postulated to cancel the QFT vacuum energy should not exist.

**4.2 Gravitational Wave Echoes (future detectors).** The event horizon is the limit of the mechanical projection. The framework predicts that future gravitational wave observations of binary black hole mergers should detect **post-merger echoes** [15] — repeating signals from wave reflections at the effective boundary of the hidden sector. The distinguishing signature is that echo amplitude should scale with the ratio of probe frequency to the hidden sector's relaxation frequency. This frequency-dependent slope distinguishes mean-field breakdown from static surface models, which predict frequency-independent reflectivity.

**4.3 Stochastic Gravitational Noise Floor (future detectors).** Since gravity is the mean of a high-variance distribution, it should exhibit statistical fluctuations at high frequencies. The framework predicts a **stochastic gravitational wave background** in the MHz–GHz band [16], with an inverse-frequency-squared spectrum satisfying the fluctuation-dissipation relation. The predicted strain noise power is beyond current detectors but within projected reach of next-generation sensors [16]. The amplitude is anchored to the $10^{120}$ ratio and is falsifiable.

**Remark on detectability.** The echo and noise-floor predictions (§4.2–4.3) yield signal amplitudes far below current sensitivity. Their value lies in the scaling relations rather than immediate detection. Near-term empirical content resides in the null prediction (§4.1) and the correlated running of couplings predicted by the connection to Asymptotic Safety [14]: as probe energy increases, the gravitational and cosmological constants should run in a correlated pattern that preserves the structural relationship between projections.

---

## 5. DISCUSSION

### 5.1 Relation to Prior Work

The argument connects several existing threads: Wolpert's inference impossibility [4] provides the physics-independent mathematical foundation; and Sorkin's causal-set prediction [17] independently supports the degree-of-freedom count. This framework is compatible with but distinct from Bohr's complementarity [8] (which operates within QM, not between QM and GR), 't Hooft's deterministic quantum mechanics [9] (the hidden sector could be deterministic, but need not be), and emergent gravity programmes [10, 11] (we do not derive gravity, but identify why the gravitational and quantum descriptions cannot agree). A companion explainer paper develops the connection between the hidden-sector trace-out and the emergence of quantum mechanics via the Barandes stochastic-quantum correspondence, which is treated there rather than here to keep the present paper focused on the Observational Incompleteness Theorem and its direct consequences.

The closest partial precedent is the work of Padmanabhan [19], whose variance-mean distinction is adopted and inverted in §2.3. His later Cosmic Information (CosmIn) programme [20] argued that gravity controls the information accessible to any observer and that demanding finite cosmic information requires a positive cosmological constant — an information-theoretic approach to $\Lambda$ compatible with the interpretation offered here. The key advance of the Observational Incompleteness Theorem is the Wolpert grounding (§2.4–2.5), which converts the variance-mean distinction from a suggestive observation into a provable impossibility result for embedded observers and determines which projection corresponds to which framework.

### 5.2 Key Objections

**"The QFT vacuum energy calculation is just wrong."** The Observational Incompleteness Theorem does not depend on the specific value of the QFT vacuum energy. It depends on the structural claim that the fluctuation measure and the mechanical measure are computed by different operations and need not agree. Even if a UV-complete theory reduces the mismatch from $10^{120}$ to $10^{40}$, the conceptual problem remains.

**"Doesn't this just redescribe the cosmological constant problem rather than solving it?"** The framework does more than relabel the discrepancy. It converts an unexplained free parameter into a derived quantity: the $10^{120}$ ratio yields roughly $10^{240}$ hidden-sector degrees of freedom, independently corroborated by the square of the de Sitter entropy and Sorkin's causal-set prediction. It also generates falsifiable experimental predictions (§4) that the standard formulation of the problem does not.

### 5.3 Open Problems

The most important open problems include: (1) a fully continuous formulation of the Observational Incompleteness Theorem via the multi-parameter quantum Cramér-Rao bound; (2) whether the relationship between the hidden-sector dimensionality and the square of the de Sitter entropy can be derived rather than observed; (3) whether special relativity can be derived from the hidden sector's propagation structure; and (4) whether the Einstein field equations can be derived as the mean-field equation governing the mechanical projection.

---

## 6. CONCLUSION

The argument proceeds in two steps.

**First**, it is established that embedded observers face irreducible inference limits (Wolpert), that quantum mechanics and general relativity represent two structurally incompatible projections of the same hidden sector (the Observational Incompleteness Theorem), and that the $10^{120}$ cosmological constant discrepancy is the quantitative signature of this incompleteness.

**Second**, the $10^{120}$ is converted from a problem into a measurement. The central limit theorem yields roughly $10^{240}$ hidden-sector degrees of freedom — equal to the square of the de Sitter entropy — independently supported by Sorkin's causal-set prediction.

If this argument is correct, the incompatibility between quantum mechanics and gravity is not a bug to be fixed. It is the physical analogue of Gödel incompleteness in formal systems—the universe telling observers, in the starkest numerical terms available, that they are inside the system they are trying to describe.

---

## DECLARATION OF AI-ASSISTED TECHNOLOGIES

During the preparation of this work, the author used **Claude Opus 4.6 (Anthropic)** and **Gemini 3 Pro (Google)** in order to assist in drafting specific sections, refining the argumentation structure, and verifying the bibliographic details of cited references. After using these tools/services, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication.

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
