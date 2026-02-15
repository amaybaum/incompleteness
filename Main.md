# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** February 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

This paper argues that the incompatibility between quantum mechanics and general relativity is a structural consequence of embedded observation. Any observer that is part of the universe it measures must access reality through projections that discard information about causally inaccessible degrees of freedom. Using Wolpert's (2008) physics-independent impossibility theorems for inference devices, a Complementarity Theorem is introduced: the quantum-mechanical and gravitational descriptions of vacuum energy correspond to variance and mean estimations of a hidden sector, and Wolpert's mutual inference impossibility prohibits their simultaneous determination by any embedded observer. The 10¹²⁰ cosmological constant discrepancy is not an error but the quantitative signature of this structural incompleteness. Interpreting the 10¹²⁰ value as a variance-to-mean ratio, roughly 10²⁴⁰ hidden-sector degrees of freedom are extracted — equal to the square of the Bekenstein-Hawking entropy of the cosmological horizon — converting the cosmological constant problem from a mystery into a measurement. Specific experimental predictions are offered, including near-term null predictions for beyond-Standard-Model particles and longer-term frequency-dependent scaling relations for gravitational wave echoes and a stochastic noise floor quantitatively anchored to the 10¹²⁰ ratio.

---

## 1. THE PROBLEM

### 1.1 The Incompatibility

Quantum mechanics and general relativity are extraordinarily successful yet incompatible. The dominant assumption has been that this incompatibility is a deficiency—that a deeper theory will eventually unify them. This paper proposes the opposite: **the incompatibility is a structural feature of embedded observation.**

### 1.2 The $10^{120}$ ratio

The sharpest manifestation of the QM-GR incompatibility is the **cosmological constant problem** [1]. It concerns the single quantity that both frameworks predict: the energy density of empty space.

**Quantum mechanics** computes the vacuum energy by summing the zero-point fluctuations of all quantum field modes up to the Planck scale cutoff, yielding $\rho_{\text{QM}} \sim 10^{110}\ \text{J/m}^3$.

**General relativity** measures the vacuum energy through its gravitational effect — the accelerated expansion of the universe — yielding $\rho_{\text{grav}} \sim 6 \times 10^{-10}\ \text{J/m}^3$.

The ratio between them:

$$\frac{\rho_{\text{QM}}}{\rho_{\text{grav}}} \sim 10^{120}$$

is the largest quantitative disagreement in all of physics. The standard interpretation is that one or both calculations must be wrong—that some unknown mechanism cancels the QFT contribution down to the observed value. Decades of effort have failed to find such a mechanism [2, 3].

A different interpretation is proposed: **neither calculation is wrong. They disagree because they are answering fundamentally different questions about the same thing.**

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

It is not necessary to specify what $\Phi$ is. The argument requires only that it exists and that the projection is many-to-one.

The hidden sector consists not of exotic particles but of standard degrees of freedom rendered causally inaccessible by the structure of spacetime: (i) trans-horizon modes beyond the cosmological horizon, (ii) sub-Planckian degrees of freedom below the observer's resolution limit, and (iii) black hole interiors. In each case, the mechanism enforcing hiddenness is the causal structure of spacetime. The partition between visible and hidden is a property of the observer's position, not of the hidden sector's content.

### 2.3 Two Projections of the Same Thing

Vacuum energy is the energy density of the hidden sector. When physicists measure or calculate it, they are attempting to characterize $\Phi$ from within the visible sector. There is more than one way to do this, and the different ways are not equivalent.

**Projection 1: Fluctuation statistics (QM).** Quantum mechanics characterizes the hidden sector through its fluctuation structure. The QFT vacuum energy calculation sums the zero-point fluctuations of all field modes up to a cutoff — the total variance of the hidden sector's influence on observables. This is a variance-type quantity: for each field mode with frequency $\omega$, the expectation values of position and momentum are both zero ($\langle \hat{x} \rangle = \langle \hat{p} \rangle = 0$), so the zero-point energy per mode is identically the sum of the canonical variances:

$$E_0 = \tfrac{1}{2}m\omega^2 \langle (\Delta \hat{x})^2 \rangle + \tfrac{1}{2m}\langle (\Delta \hat{p})^2 \rangle = \tfrac{1}{2}\hbar\omega$$

In the classical ground state both variances vanish and the vacuum energy is zero — the entire zero-point contribution is fluctuation content.

**Projection 2: Mean-field pressure (gravity).** Gravity characterizes the hidden sector through its net mechanical effect — the aggregate pressure that the hidden degrees of freedom exert on spacetime. The observed value $\rho_{\text{grav}} \sim 6 \times 10^{-10}\ \text{J/m}^3$ is obtained by coupling to the expectation value of the stress-energy tensor — a first-moment quantity. The Einstein field equations are explicitly a mean-field coupling: the left-hand side is a smooth geometric quantity (spacetime curvature), and the right-hand side is the expectation value of the stress-energy tensor over the quantum state, computed by averaging over all field configurations weighted by the path integral — the definition of a statistical mean. Gravity does not couple to individual mode amplitudes or to the variance of the field; it couples to the net, signed, aggregate energy-momentum content.

The physical reason for the divergence is that gravity acts as an **adiabatic probe**, averaging over Planck-scale fluctuations and seeing only the mean energy density. Quantum mechanics probes the **correlation structure** — summing over propagators to measure how much the medium fluctuates, not how heavy it is.

**The key identification.** These two projections compute different statistical quantities of the same distribution: $\rho_{\text{QM}}$ measures total fluctuation content (related to variance / second moment), while $\rho_{\text{grav}}$ measures net mechanical effect (related to mean / first moment). This identification has precise mathematical content. For modes with randomly distributed phases, the signed contributions undergo massive cancellation: a signed sum over $N$ random contributions scales as $\sqrt{N}$ rather than $N$.

For any distribution with a large number of degrees of freedom, the variance can be enormously larger than the mean. The $10^{120}$ ratio is the quantitative expression of this difference.

To see how the divergence arises concretely, consider $N$ modes each contributing energy with a random sign. The unsigned sum — the fluctuation content — grows as $N$. The signed sum — the net mechanical effect — is a random walk whose expectation scales by the central limit theorem as $\sqrt{N}$. The ratio is $\sqrt{N}$, which grows without bound. For the vacuum, $N$ is set by the number of hidden-sector degrees of freedom; §3 shows that the observed ratio of $10^{120}$ implies $N \sim 10^{240}$.

### 2.4 Why They Cannot Be Unified

The two projections require **incompatible operations on the hidden sector.**

The quantum projection *traces out* the hidden sector — it requires that $\Phi$ be inaccessible. The gravitational projection *couples to* the hidden sector — it requires that $\Phi$ be mechanically present. One operation hides the hidden sector. The other feels it. No single description available to an embedded observer can simultaneously hide and reveal $\Phi$.

This incompatibility is not merely conceptual. Because the two operations extract independent statistical moments of $\Phi$ (variance and mean respectively), Wolpert's mutual inference impossibility provides a quantitative bound on their simultaneous determination, which is now stated formally.

> **Complementarity Theorem (informal):** For any embedded observer, the quantum-mechanical and gravitational descriptions of vacuum energy are complementary projections that cannot be unified into a single observer-accessible description. The cosmological constant problem is the observable signature of this structural complementarity.

### 2.5 Formal Statement via Wolpert's Framework

**Setup.** Let the universe state be partitioned into the visible sector and the hidden sector. Define two target functions: the fluctuation content of the hidden sector (its variance, corresponding to $\rho_{\text{QM}}$) and the net mechanical effect of the hidden sector (its mean, corresponding to $\rho_{\text{grav}}$).

**Inference devices.** An observer confined to the visible sector constitutes an inference device in Wolpert's sense: the setup function is the projection from the full state to the visible sector, and the conclusion function encodes the observer's best estimate of a binary question about the target. Wolpert's framework applies to binary inference tasks; the continuous targets (variance and mean) are binarized by thresholding: Device 1 (the "quantum observer") asks "Is the variance above or below threshold $v_0$?"; Device 2 (the "gravitational observer") asks "Is the mean above or below threshold $m_0$?" The impossibility holds for every choice of thresholds, and therefore constrains the continuous inference problem a fortiori. Both devices share the same projection.

**Application of the impossibility theorem.** Wolpert's mutual inference impossibility (result (b) in §2.1) applies when the two targets are independently configurable — when distributions exist with the same mean but different variances, and vice versa. This condition is satisfied physically: a hidden sector in which an equal number of modes are excited at equal and opposite amplitudes has large variance but zero mean; shifting all mode signs to positive preserves the variance while changing the mean. More generally, the mean depends on the net sign balance of the hidden sector's contributions while the variance depends on their amplitudes, and these are controlled by independent physical parameters (phase structure vs. excitation level). The independent configurability condition must hold not merely in the abstract space of distributions but under the physical dynamics of the hidden sector; this is satisfied because the phase structure and excitation level of field modes are set by independent initial conditions and are not dynamically locked to one another. (If interactions induce partial correlations between phases and amplitudes, the independent configurability condition is weakened but not eliminated: the Wolpert bound degrades gracefully, with the product $\epsilon_{\text{fluc}} \cdot \epsilon_{\text{mech}}$ bounded above by a value that increases monotonically with the correlation strength but remains below unity for any correlation short of perfect dynamical locking — a fine-tuned regime that would itself require explanation.) To obtain a quantitative bound, the stochastic extension of Wolpert's Theorem 1 [4, §4] is applied, which generalizes the deterministic impossibility result to probabilistic inference devices. In the stochastic setting, each device's "correctness" is measured by the probability $\epsilon$ that its conclusion function matches the target. Wolpert shows that for two inference devices sharing the same projection and targeting independently configurable functions, the product of their success probabilities is bounded:

$$\epsilon_{\text{fluc}} \cdot \epsilon_{\text{mech}} \leq \frac{1}{4}$$

The $1/4$ arises because each device partitions universe states into equivalence classes under the projection; independent configurability ensures that the two partitions are "cross-cutting," so that for any assignment of conclusions by one device, there exist universe states in each equivalence class that defeat the other device's inference. The factor of $1/4$ is the product of the two binary-task chance baselines ($1/2 \times 1/2$). **Perfect inference of one target ($\epsilon = 1$) forces the other to be no better than chance ($\epsilon \leq 1/4$).**

> **Complementarity Theorem (formal):** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. If the variance and mean of the hidden-sector distribution are independently configurable, then by Wolpert's mutual inference impossibility, no single inference device confined to the visible sector can simultaneously determine both with accuracy exceeding $\epsilon_{\text{fluc}} \cdot \epsilon_{\text{mech}} \leq 1/4$.

**Remark on generality.** This result is physics-independent—it requires only that the observer is embedded and that the variance and mean of $H$ are independently variable.

**Remark on the inference-ontology bridge.** Wolpert's theorem bounds inference accuracy, not physical quantities directly. The bridge is this: the values called $\rho_{\text{QM}}$ and $\rho_{\text{grav}}$ are not observer-independent properties of the hidden sector. They are outputs of specific measurement procedures — QFT mode-summation and gravitational coupling — each constituting an inference operation in Wolpert's sense. There is no "true" vacuum energy behind both measurements. The two values are the best answers that two structurally different inference procedures can extract from the same hidden sector, and Wolpert's theorem guarantees they cannot converge. The $10^{120}$ is not the gap between two estimates of one quantity; it is the gap between two quantities that embeddedness forces to be distinct.

---

## 3. THE $10^{120}$ AS MEASUREMENT

If the $10^{120}$ encodes statistical properties of the hidden sector, it should yield quantitative information about the hidden sector's dimensionality.

### 3.1 The Random-Sign Cancellation Model

Consider a hidden sector with $N$ independent degrees of freedom, each contributing energy with a random sign, a characteristic energy per mode, and a random fluctuation with mean zero.

The **total fluctuation content** (the quantum projection) sums the variances of all contributions, scaling as $N$. The **net mechanical effect** (the gravitational projection) sums the signed contributions; by the central limit theorem, this scales as $\sqrt{N}$. The **variance-to-mean ratio** therefore scales as $\sqrt{N}$.

The assumption that the characteristic energy per mode is of order one in Planck units follows from dimensional analysis: the hidden sector's characteristic energy scale is set by the Planck energy, which is the natural unit for gravitational-quantum processes at the projection boundary. In Planck units, the characteristic energy per mode is therefore order unity by construction, with no free parameters to tune. (More precisely, this assumes that the *effective* contribution of each hidden-sector degree of freedom to the observable projections remains order-unity after coarse-graining; this is satisfied when the coarse-graining preserves the Planck-scale normalization, which is the generic expectation for modes at or near the projection boundary.) Setting $\sqrt{N} \sim 10^{120}$:

$$\boxed{N \sim 10^{240}}$$

### 3.2 The Holographic Coincidence

The Bekenstein-Hawking entropy of the cosmological horizon is independently calculated as $S_{\text{dS}} \sim 10^{120}$ [12, 18] (the conventional value ranges from $10^{120}$ to $10^{122}$ depending on precise inputs; we use $10^{120}$ throughout for arithmetic consistency, well within the order-of-magnitude precision of the estimates). The relationship is:

$$N \sim 10^{240} = S_{\text{dS}}^2$$

The number of hidden-sector degrees of freedom is the **square** of the holographic entropy bound. This admits a natural interpretation: if each of roughly $10^{120}$ Planck-area cells on the cosmological horizon encodes one holographic degree of freedom, and each has an internal state space of dimension $\sim 10^{120}$, the total is $(10^{120})^2 = 10^{240}$. The hidden sector has a **doubly holographic** structure: a holographic boundary whose elements are themselves holographic.

This count is independently supported by Sorkin's causal-set prediction [17], which derives $\Lambda \sim 1/\sqrt{V_4}$ from Poisson fluctuations in the number of spacetime atoms, yielding $N \sim 10^{240}$ (order of magnitude) before the 1998 discovery of cosmic acceleration.

### 3.3 Robustness

The estimate is robust: replacing random signs with random complex phases gives the same $\sqrt{N}$ scaling; weak pairwise correlations modify the estimate only marginally (for modes with pairwise correlation coefficient $r$, the variance of the signed sum scales as $N(1 + r(N-1))$, which departs from the uncorrelated $\sqrt{N}$ scaling only when $r \gtrsim 1/N$ — a fine-tuned regime). The result exceeds the number of Planck volumes in the observable universe ($\sim 10^{185}$) by $\sim 10^{55}$, ruling out a naive "one degree of freedom per Planck volume" interpretation and implying a holographic or extra-dimensional structure.

---

## 4. EXPERIMENTAL PREDICTIONS

If the Complementarity Theorem is correct, General Relativity is an effective mean-field theory that breaks down whenever adiabatic averaging fails. This yields distinct observational signatures.

**4.1 Gravitational Wave Echoes.** The event horizon is the limit of the mechanical projection. The framework predicts that future gravitational wave observations of binary black hole mergers should detect **post-merger echoes** [15] — repeating signals from wave reflections at the effective boundary of the hidden sector. The distinguishing signature is that echo amplitude should scale with the ratio of probe frequency to the hidden sector's relaxation frequency. This frequency-dependent slope distinguishes mean-field breakdown from static surface models, which predict frequency-independent reflectivity.

**4.2 Stochastic Gravitational Noise Floor.** Since gravity is the mean of a high-variance distribution, it should exhibit statistical fluctuations at high frequencies. The framework predicts a **stochastic gravitational wave background** in the MHz–GHz band [16], with a $1/f^\alpha$ spectrum ($\alpha \approx 2$) satisfying the fluctuation-dissipation relation. The predicted strain noise power is beyond current detectors but within projected reach of next-generation sensors [16]. The amplitude is anchored to the $10^{120}$ ratio and is falsifiable.

**4.3 Null Prediction.** The framework predicts a **null result** for searches for supersymmetric partners or inflaton particles invoked to solve the cosmological constant problem. As a standalone result, absence of evidence is weak confirmation—many frameworks are compatible with null results at current energies. The null prediction's value lies in its role within the full prediction package: the same structural argument that predicts no new particles also predicts the specific scaling relations of §4.1–4.2 and the correlated running of couplings noted below. A pattern of continued null results at colliders combined with eventual detection of frequency-dependent echo scaling or a stochastic noise floor at the predicted amplitude would constitute strong joint evidence for the Complementarity framework.

**Remark on detectability.** The echo and noise-floor predictions yield signal amplitudes far below current sensitivity — the predicted stochastic noise floor corresponds to a strain amplitude of order $h \sim 10^{-30}$ in the MHz band, roughly eight orders of magnitude below Advanced LIGO's design sensitivity at its optimal frequency and four to five orders below projected sensitivities of next-generation high-frequency concepts [16]. Their value lies in the scaling relations rather than immediate detection. Near-term empirical content resides in the null prediction and the correlated running of couplings predicted by the connection to Asymptotic Safety [14]: as probe energy increases, $G$ and $\Lambda$ should run in a correlated pattern that preserves the complementary relationship between projections.

---

## 5. DISCUSSION

### 5.1 Relation to Prior Work

The argument connects several existing threads: Wolpert's inference impossibility [4] provides the physics-independent mathematical foundation; and Sorkin's causal-set prediction [17] independently supports the degree-of-freedom count. This framework is compatible with but distinct from Bohr's complementarity [8] (which operates within QM, not between QM and GR), 't Hooft's deterministic quantum mechanics [9] (the hidden sector could be deterministic, but need not be), and emergent gravity programmes [10, 11] (we do not derive gravity, but identify why the gravitational and quantum descriptions cannot agree). A companion explainer paper develops the connection between the hidden-sector trace-out and the emergence of quantum mechanics via the Barandes stochastic-quantum correspondence, which is treated there rather than here to keep the present paper focused on the Complementarity Theorem and its direct consequences.

The framework reinterprets String Theory [6, 13] not as a failed Theory of Everything but as a successful characterization of the hidden sector. The AdS/CFT correspondence maps onto the two-projection structure with considerable precision: the bulk gravitational description corresponds to the mechanical projection (the mean-field average over hidden-sector degrees of freedom), while the boundary CFT corresponds to the fluctuation projection (the correlation structure of the same degrees of freedom as seen from the boundary). The holographic dictionary that translates between bulk fields and boundary operators is, in this reading, the mathematical apparatus for converting between the two projections of the same hidden sector. The radial direction in AdS — the extra dimension that connects the boundary to the interior — encodes the scale at which the hidden sector is being coarse-grained: the boundary lives at the UV (full fluctuation detail), the deep interior at the IR (maximally averaged). This is precisely the structure one would expect if the bulk geometry is a mean-field description whose resolution degrades with depth. The fact that AdS/CFT is an exact duality — not an approximation — is consistent with the Complementarity Theorem: the two projections contain complementary information about the same underlying system, so a complete dictionary between them must exist even though no single observer can access both simultaneously. Extra dimensions correspond to hidden-sector degrees of freedom rather than literal geometric structures; and the Landscape's roughly $10^{500}$ vacua represent the combinatorial complexity of the hidden sector's roughly $10^{240}$ degrees of freedom, not different universes requiring anthropic selection.

More broadly, the Complementarity Theorem belongs to the family of impossibility results that includes Gödel's incompleteness theorems [5] and Turing's halting problem. In each case, a self-referential system faces structural limits on what it can determine about itself: arithmetic cannot prove its own consistency, no program can decide the halting of all programs, and no embedded observer can simultaneously determine the variance and mean of its hidden sector. The correspondence is structurally precise. Wolpert's inference impossibility [4]—the mathematical engine of the Complementarity Theorem—is a physics-independent result in the same formal lineage as Gödel and Turing, extended to physical devices embedded in physical universes. The $10^{120}$ serves as the quantitative marker of this structural limit: the numerical encoding of what self-referential observation cannot access, analogous to the Gödel sentence that a formal system can state but cannot resolve.

### 5.2 Key Objections

**"The QFT vacuum energy calculation is just wrong."** The Complementarity Theorem does not depend on the specific value of the QFT vacuum energy. It depends on the structural claim that the fluctuation measure and the mechanical measure are computed by different operations and need not agree. Even if a UV-complete theory reduces the mismatch from $10^{120}$ to $10^{40}$, the conceptual problem remains.

**"Doesn't this prove too much?"** No. The argument applies specifically to situations where two frameworks predict the same physical quantity via fundamentally different operations on the hidden sector, corresponding to different statistical moments. This is specific to the QM-GR relationship and the vacuum energy, not a general feature of any pair of measurements.

**"Doesn't this just redescribe the cosmological constant problem rather than solving it?"** The framework does more than relabel the discrepancy. It converts an unexplained free parameter into a derived quantity: the $10^{120}$ ratio yields $N \sim 10^{240}$ hidden-sector degrees of freedom, independently corroborated by $S_{\text{dS}}^2$ and Sorkin's causal-set prediction. It also generates falsifiable experimental predictions (§4) that the standard formulation of the problem does not. A redescription that extracts a new physical quantity and makes new predictions is, by standard criteria, explanatory progress.

### 5.3 Open Problems

The most important open problems include: (1) a fully continuous formulation of the Complementarity Theorem via the multi-parameter quantum Cramér-Rao bound; (2) whether the $N \sim S_{\text{dS}}^2$ relationship can be derived rather than observed; (3) whether special relativity can be derived from the hidden sector's propagation structure; and (4) whether the Einstein field equations can be derived as the mean-field equation governing the mechanical projection.

---

## 6. CONCLUSION

The argument proceeds in two steps.

**First**, it is established that embedded observers face irreducible inference limits (Wolpert), that quantum mechanics and general relativity represent two structurally incompatible projections of the same hidden sector (the Complementarity Theorem), and that the $10^{120}$ cosmological constant discrepancy is the quantitative signature of this incompleteness.

**Second**, the $10^{120}$ is converted from a problem into a measurement. The central limit theorem yields $N \sim 10^{240}$ hidden-sector degrees of freedom — equal to $S_{\text{dS}}^2$ — independently supported by Sorkin's causal-set prediction.

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

---

*END OF DOCUMENT*