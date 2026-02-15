# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** February 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

This paper argues that the incompatibility between quantum mechanics and general relativity is a structural consequence of embedded observation. Any observer that is part of the universe it measures must access reality through projections that discard information about causally inaccessible degrees of freedom. Using Wolpert's (2008) physics-independent impossibility theorems for inference devices, a Complementarity Theorem is introduced: the quantum-mechanical and gravitational descriptions of vacuum energy correspond to unsigned and signed accumulations of hidden-sector contributions, and Wolpert's mutual inference impossibility prohibits their simultaneous determination by any embedded observer. The 10¹²⁰ cosmological constant discrepancy is not an error but the quantitative signature of this structural incompleteness. Interpreting the 10¹²⁰ value as an unsigned-to-signed ratio, roughly 10²⁴⁰ hidden-sector degrees of freedom are extracted — equal to the square of the Bekenstein-Hawking entropy of the cosmological horizon — converting the cosmological constant problem from a mystery into a measurement. Specific experimental predictions are offered, including near-term null predictions for beyond-Standard-Model particles and longer-term frequency-dependent scaling relations for gravitational wave echoes and a stochastic noise floor quantitatively anchored to the 10¹²⁰ ratio.

---

## 1. THE PROBLEM

### 1.1 The Incompatibility

Quantum mechanics and general relativity are extraordinarily successful yet incompatible. The dominant assumption has been that this incompatibility is a deficiency—that a deeper theory will eventually unify them. This paper proposes the opposite: **the incompatibility is a structural feature of embedded observation.**

### 1.2 The $10^{120}$ Ratio

The sharpest manifestation of the QM-GR incompatibility is the **cosmological constant problem** [1]. It concerns the single quantity that both frameworks predict: the energy density of empty space.

**Quantum mechanics** computes the vacuum energy by summing the zero-point fluctuations of all quantum field modes up to the Planck scale cutoff, yielding roughly $10^{110}$ joules per cubic meter.

**General relativity** measures the vacuum energy through its gravitational effect — the accelerated expansion of the universe — yielding roughly $6 \times 10^{-10}$ joules per cubic meter.

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

**Projection 1: Unsigned accumulation (QM).** The QFT vacuum energy calculation sums the zero-point energies of all field modes up to a cutoff. Strictly, the result is an expectation value — $\langle 0 | H | 0 \rangle$ — which is formally a first moment. However, it has the mathematical character of an unsigned, positive-definite accumulation: each mode contributes $+\frac{1}{2}\hbar\omega$, a quantity proportional to the position and momentum variances of the quantum ground state. (In the classical ground state both variances vanish and the zero-point energy is zero.) No cancellation between modes is possible — every term is positive, and the sum grows linearly with the number of modes. This is the defining property of a variance-type aggregation: unsigned, positive-definite accumulation whose total scales proportionally to the number of contributing degrees of freedom.

**Projection 2: Signed accumulation (gravity).** The gravitational measurement also couples to an expectation value — $\langle T_{\mu\nu} \rangle$ — so it too is formally a first moment. But the stress-energy tensor is not positive-definite: different field sectors (bosonic vs. fermionic, different spin types, vacuum condensates) contribute to the effective cosmological constant with different signs, and the Einstein equations couple to the net signed aggregate. Cancellation between sectors is not only possible but generically expected. The gravitational measurement therefore has the mathematical character of a mean-type aggregation: signed accumulation where positive and negative contributions partially cancel, and the result scales much more slowly than the number of contributing degrees of freedom.

Physically: gravity acts as an **adiabatic probe**, coupling to the net signed energy-momentum content averaged over all Planck-scale fluctuations. Quantum mechanics probes the **correlation structure** — summing propagators mode by mode, each contributing positively, to measure how much the medium fluctuates.

**The key identification.** The structural distinction is between unsigned accumulation and signed accumulation. The QFT calculation adds absolute magnitudes (every mode contributes positively); gravity couples to the net signed result (where different sectors cancel). For a system with many independent contributions of mixed sign, the unsigned total is generically much larger than the signed residual — by a factor that grows with the number of contributing degrees of freedom. The analogy is a collection of $N$ random debts and credits: the total absolute amount owed grows proportionally to $N$, but the net balance grows by the central limit theorem only as $\sqrt{N}$. The ratio therefore grows as $\sqrt{N}$. For the vacuum, $N$ is the number of hidden-sector degrees of freedom; §3 shows that the observed ratio of $10^{120}$ implies $N$ of order $10^{240}$.

### 2.4 Why They Cannot Be Unified

The two projections require **incompatible operations on the hidden sector.**

The quantum projection *traces out* the hidden sector — it requires that $\Phi$ be inaccessible. The gravitational projection *couples to* the hidden sector — it requires that $\Phi$ be mechanically present. One operation hides the hidden sector. The other feels it. No single description available to an embedded observer can simultaneously hide and reveal $\Phi$.

This incompatibility is not merely conceptual. Because the two operations aggregate hidden-sector contributions in structurally different ways — unsigned accumulation vs. signed accumulation — Wolpert's mutual inference impossibility provides a quantitative bound on their simultaneous determination, which is now stated formally.

> **Complementarity Theorem (informal):** For any embedded observer, the quantum-mechanical and gravitational descriptions of vacuum energy are complementary projections — corresponding to unsigned and signed accumulations of hidden-sector contributions — that cannot be unified into a single observer-accessible description. The cosmological constant problem is the observable signature of this structural complementarity.

### 2.5 Formal Statement via Wolpert's Framework

**Setup.** The universe state is partitioned into visible and hidden sectors. Two target functions are defined: the unsigned accumulation of the hidden sector's contributions (corresponding to the QFT vacuum energy, which sums positive-definite mode energies) and the signed accumulation (corresponding to the gravitationally observed vacuum energy, which couples to the net result after inter-sector cancellations).

**Inference devices.** An observer confined to the visible sector constitutes an inference device in Wolpert's sense: the setup function is the projection from the full state to the visible sector. Wolpert's framework applies to binary inference tasks, so the continuous targets are binarized by thresholding: Device 1 asks "Is the unsigned total above or below a given threshold?"; Device 2 asks "Is the signed net above or below a given threshold?" The impossibility holds for every choice of thresholds, and therefore constrains the continuous inference problem a fortiori.

**Independent configurability.** The mutual inference impossibility requires that the two targets be independently configurable — that is, that states exist in the hidden sector's state space with the same signed net but different unsigned totals, and vice versa. This is a condition on the mathematical state space, not on the experimenter's ability to physically prepare such states. It is satisfied whenever the signs of individual contributions can vary independently of their magnitudes: one can construct configurations with equal net balance but different total absolute activity (by rearranging signs while preserving magnitudes), and configurations with equal total activity but different net balance (by rearranging signs while preserving individual magnitudes). In the physical hidden sector, the sign of each sector's contribution to the effective cosmological constant depends on its spin-statistics (bosonic vs. fermionic) and vacuum condensate structure, while the magnitude depends on excitation level. These are set by independent physical parameters.

If interactions induce partial correlations between signs and magnitudes, the independent configurability condition weakens but is not eliminated: the Wolpert bound degrades gracefully, remaining nontrivial for any correlation short of perfect dynamical locking — itself a fine-tuned regime requiring independent explanation.

**The bound.** Wolpert's Theorem 1 [4] establishes that no single inference device can correctly compute all functions of the universe state. The stochastic extension [4, §4, Corollary 2] generalizes this to probabilistic inference: for two devices sharing the same projection and targeting independently configurable binary functions, the product of their success probabilities satisfies

$$\epsilon_{\text{unsigned}} \cdot \epsilon_{\text{signed}} \leq \frac{1}{4}$$

The one-quarter bound arises because independent configurability ensures the two binary partitions are cross-cutting: for any assignment of conclusions by one device, universe states exist in each equivalence class that defeat the other device's inference. The bound is the product of the two binary-task chance baselines ($\frac{1}{2} \times \frac{1}{2}$). **Perfect inference of one target forces the other to be no better than chance.**

> **Complementarity Theorem (formal):** Let the universe be partitioned into visible and hidden sectors, and let the observer's projection from the full state to the visible sector be many-to-one. If the unsigned and signed accumulations of the hidden-sector contributions are independently configurable, then by Wolpert's mutual inference impossibility, no single inference device confined to the visible sector can simultaneously determine both with joint accuracy exceeding one-quarter.

**Remark on generality.** This result is physics-independent — it requires only that the observer is embedded and that the unsigned and signed accumulations of the hidden sector are independently variable.

**Remark on the inference-ontology bridge.** Wolpert's theorem bounds inference accuracy, not physical quantities directly. The bridge relies on a non-trivial interpretive commitment: the QFT and gravitational vacuum energies are not observer-independent properties of the hidden sector but outputs of specific measurement procedures — QFT mode-summation and gravitational coupling — each constituting an inference operation in Wolpert's sense. On this interpretation, there is no single "true" vacuum energy behind both measurements. The two values are the best answers that two structurally different inference procedures can extract from the same hidden sector, and Wolpert's theorem guarantees they cannot converge. The $10^{120}$ is not the gap between two estimates of one quantity; it is the gap between two quantities that embeddedness forces to be distinct. This interpretive step — treating the measurements as constitutive of the quantities rather than as approximations to a shared underlying value — is a substantive philosophical position, akin to quantum Bayesian and perspectival approaches to measurement. The formal results of the Complementarity Theorem do not depend on it, but its physical interpretation does.

---

## 3. THE $10^{120}$ AS MEASUREMENT

If the $10^{120}$ encodes the ratio between unsigned and signed accumulations of hidden-sector contributions, it should yield quantitative information about the hidden sector's dimensionality.

### 3.1 The Signed/Unsigned Accumulation Model

Consider a hidden sector with $N$ independent degrees of freedom. Each contributes a characteristic energy of order one in Planck units (as set by dimensional analysis at the projection boundary), but different sectors contribute to the effective cosmological constant with different signs — bosonic fields contribute positively, fermionic fields contribute negatively, and vacuum condensates shift the balance further. The QFT mode-sum does not see these cancellations: it sums positive-definite zero-point energies mode by mode, so every contribution adds. The gravitational coupling sees the net result after all inter-sector cancellations.

The **unsigned total** (quantum projection) sums the absolute magnitude of all contributions, scaling proportionally to $N$. The **signed net** (gravitational projection) sums the contributions with their signs; by the central limit theorem, for $N$ independently signed contributions this scales as $\sqrt{N}$. The unsigned-to-signed ratio therefore scales as $\sqrt{N}$.

Setting $\sqrt{N}$ equal to $10^{120}$:

$$\boxed{N \sim 10^{240}}$$

**Remark on the sign structure.** Individual QFT mode zero-point energies are all positive ($+\frac{1}{2}\hbar\omega$). The effective signs arise at the level of sectors, not individual modes: the total bosonic vacuum energy is positive, the total fermionic vacuum energy is negative, and other contributions (gauge condensates, symmetry-breaking potentials) have their own signs. The random-sign model treats each hidden-sector degree of freedom as contributing with an effectively random sign to the net gravitational coupling — an idealization justified when the number of distinct sector types is large and their relative magnitudes are not fine-tuned. The model is a statistical toy model that captures the scaling; a full calculation would require the actual sign and magnitude distribution across sectors.

The Planck-unit normalization assumes that the effective contribution of each hidden-sector degree of freedom to the observable projections remains order-unity after coarse-graining. This is the generic expectation for modes at or near the projection boundary — no fine-tuning is required.

### 3.2 The Holographic Coincidence

The Bekenstein-Hawking entropy of the cosmological horizon is independently calculated as roughly $10^{120}$ [12, 18] (the conventional value ranges from $10^{120}$ to $10^{122}$ depending on precise inputs; we use $10^{120}$ throughout for arithmetic consistency, well within the order-of-magnitude precision of the estimates). The number of hidden-sector degrees of freedom is therefore the **square** of the holographic entropy bound.

This admits a natural interpretation: if each of roughly $10^{120}$ Planck-area cells on the cosmological horizon encodes one holographic degree of freedom, and each has an internal state space of dimension roughly $10^{120}$, the total is their product — $10^{240}$. The hidden sector has a **doubly holographic** structure: a holographic boundary whose elements are themselves holographic.

This count is independently supported by Sorkin's causal-set prediction [17], which derives the cosmological constant from Poisson fluctuations in the number of spacetime atoms, yielding $N$ of order $10^{240}$ before the 1998 discovery of cosmic acceleration.

### 3.3 Robustness

The $\sqrt{N}$ scaling is robust under several modifications. Replacing random signs with random complex phases preserves the scaling. Weak pairwise correlations modify the estimate only marginally, departing from the $\sqrt{N}$ scaling only when the correlation coefficient reaches order $1/N$ — a fine-tuned regime. The result exceeds the number of Planck volumes in the observable universe (roughly $10^{185}$) by some $10^{55}$, ruling out a naive "one degree of freedom per Planck volume" interpretation and implying a holographic or extra-dimensional structure.

---

## 4. EXPERIMENTAL PREDICTIONS

If the Complementarity Theorem is correct, General Relativity is an effective mean-field theory that breaks down whenever adiabatic averaging fails. This yields distinct observational signatures.

**4.1 Gravitational Wave Echoes.** The event horizon is the limit of the mechanical projection. The framework predicts that future gravitational wave observations of binary black hole mergers should detect **post-merger echoes** [15] — repeating signals from wave reflections at the effective boundary of the hidden sector. The distinguishing signature is that echo amplitude should scale with the ratio of probe frequency to the hidden sector's relaxation frequency. This frequency-dependent slope distinguishes mean-field breakdown from static surface models, which predict frequency-independent reflectivity.

**4.2 Stochastic Gravitational Noise Floor.** Since gravity couples to the signed net of a distribution whose unsigned total is $10^{120}$ times larger, it should exhibit statistical fluctuations at high frequencies. The framework predicts a **stochastic gravitational wave background** in the MHz–GHz band [16], with an inverse-frequency-squared spectrum satisfying the fluctuation-dissipation relation. The predicted strain noise power is beyond current detectors but within projected reach of next-generation sensors [16]. The amplitude is anchored to the $10^{120}$ ratio and is falsifiable.

**4.3 Null Prediction.** The framework predicts a **null result** for searches for supersymmetric partners or inflaton particles invoked to solve the cosmological constant problem. As a standalone result, absence of evidence is weak confirmation—many frameworks are compatible with null results at current energies. The null prediction's value lies in its role within the full prediction package: the same structural argument that predicts no new particles also predicts the specific scaling relations of §4.1–4.2 and the correlated running of couplings noted below. A pattern of continued null results at colliders combined with eventual detection of frequency-dependent echo scaling or a stochastic noise floor at the predicted amplitude would constitute strong joint evidence for the Complementarity framework.

**Remark on detectability.** The echo and noise-floor predictions yield signal amplitudes far below current sensitivity — the predicted stochastic noise floor corresponds to a strain amplitude of order $10^{-30}$ in the MHz band, roughly eight orders of magnitude below Advanced LIGO's design sensitivity at its optimal frequency and four to five orders below projected sensitivities of next-generation high-frequency concepts [16]. Their value lies in the scaling relations rather than immediate detection. Near-term empirical content resides in the null prediction and the correlated running of couplings predicted by the connection to Asymptotic Safety [14]: as probe energy increases, the gravitational and cosmological constants should run in a correlated pattern that preserves the complementary relationship between projections.

---

## 5. DISCUSSION

### 5.1 Relation to Prior Work

The argument connects several existing threads: Wolpert's inference impossibility [4] provides the physics-independent mathematical foundation; and Sorkin's causal-set prediction [17] independently supports the degree-of-freedom count. This framework is compatible with but distinct from Bohr's complementarity [8] (which operates within QM, not between QM and GR), 't Hooft's deterministic quantum mechanics [9] (the hidden sector could be deterministic, but need not be), and emergent gravity programmes [10, 11] (we do not derive gravity, but identify why the gravitational and quantum descriptions cannot agree). A companion explainer paper develops the connection between the hidden-sector trace-out and the emergence of quantum mechanics via the Barandes stochastic-quantum correspondence, which is treated there rather than here to keep the present paper focused on the Complementarity Theorem and its direct consequences.

The framework reinterprets String Theory [6, 13] not as a failed Theory of Everything but as a successful characterization of the hidden sector. The AdS/CFT correspondence maps onto the two-projection structure: the bulk gravitational description corresponds to the signed projection (net aggregate over hidden-sector degrees of freedom), while the boundary CFT corresponds to the unsigned projection (mode-by-mode correlation structure of the same degrees of freedom as seen from the boundary). The holographic dictionary translating between bulk fields and boundary operators is, in this reading, the apparatus for converting between the two projections. The radial direction in AdS encodes the coarse-graining scale: the boundary lives at the UV (full mode-level detail), the deep interior at the IR (maximally averaged) — precisely the structure expected if bulk geometry is a signed-accumulation description whose resolution degrades with depth. That AdS/CFT is an exact duality — not an approximation — is consistent with the Complementarity Theorem: the two projections contain complementary information about the same system, so a complete dictionary between them must exist even though no single observer can access both simultaneously. Extra dimensions correspond to hidden-sector degrees of freedom rather than literal geometric structures; and the Landscape's roughly $10^{500}$ vacua represent the combinatorial complexity of the hidden sector's roughly $10^{240}$ degrees of freedom, not different universes requiring anthropic selection.

More broadly, the Complementarity Theorem belongs to the family of impossibility results that includes Gödel's incompleteness theorems [5] and Turing's halting problem. In each case, a self-referential system faces structural limits on what it can determine about itself: arithmetic cannot prove its own consistency, no program can decide the halting of all programs, and no embedded observer can simultaneously determine the unsigned and signed accumulations of its hidden sector. The correspondence is structurally precise. Wolpert's inference impossibility [4] is a physics-independent result in the same formal lineage as Gödel and Turing, extended to physical devices embedded in physical universes. The $10^{120}$ serves as the quantitative marker of this structural limit.

### 5.2 Key Objections

**"The QFT vacuum energy calculation is just wrong."** The Complementarity Theorem does not depend on the specific value of the QFT vacuum energy. It depends on the structural claim that the unsigned accumulation and the signed accumulation are computed by different operations and need not agree. Even if a UV-complete theory reduces the mismatch from $10^{120}$ to $10^{40}$, the conceptual problem remains.

**"Doesn't this prove too much?"** No. The argument applies specifically to situations where two frameworks predict the same physical quantity via structurally different aggregation operations on the hidden sector — one unsigned and positive-definite, the other signed and cancellation-prone. This is specific to the QM-GR relationship and the vacuum energy, not a general feature of any pair of measurements.

**"Doesn't this just redescribe the cosmological constant problem rather than solving it?"** The framework does more than relabel the discrepancy. It converts an unexplained free parameter into a derived quantity: the $10^{120}$ ratio yields roughly $10^{240}$ hidden-sector degrees of freedom, independently corroborated by the square of the de Sitter entropy and Sorkin's causal-set prediction. It also generates falsifiable experimental predictions (§4) that the standard formulation of the problem does not. A redescription that extracts a new physical quantity and makes new predictions is, by standard criteria, explanatory progress.

### 5.3 Open Problems

The most important open problems include: (1) a fully continuous formulation of the Complementarity Theorem via the multi-parameter quantum Cramér-Rao bound; (2) whether the relationship between the hidden-sector dimensionality and the square of the de Sitter entropy can be derived rather than observed; (3) whether special relativity can be derived from the hidden sector's propagation structure; and (4) whether the Einstein field equations can be derived as the signed-accumulation equation governing the gravitational projection.

---

## 6. CONCLUSION

The argument proceeds in two steps.

**First**, it is established that embedded observers face irreducible inference limits (Wolpert), that quantum mechanics and general relativity represent two structurally incompatible projections of the same hidden sector — unsigned and signed accumulations — (the Complementarity Theorem), and that the $10^{120}$ cosmological constant discrepancy is the quantitative signature of this incompleteness.

**Second**, the $10^{120}$ is converted from a problem into a measurement. The central limit theorem applied to the signed accumulation yields roughly $10^{240}$ hidden-sector degrees of freedom — equal to the square of the de Sitter entropy — independently supported by Sorkin's causal-set prediction.

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
