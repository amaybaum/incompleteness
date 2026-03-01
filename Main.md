# THE UNDECIDABILITY OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** February 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

The incompatibility between quantum mechanics and general relativity is widely viewed as a failing of modern physics. This paper proposes the opposite: the incompatibility is a structural consequence of embedded observation. Any observer embedded in the universe it measures must access reality through projections that discard degrees of freedom beyond spacetime's causal boundaries.

Applying Wolpert's (2008) physical limits of inference [4], quantum and gravitational vacuum measurements are shown to be complementary projections of a shared hidden sector — one measuring unsigned total vacuum activity, the other measuring net signed stress-energy. The $\sqrt{N}$ scaling between the two projections is rigorously established via the Central Limit Theorem for $N = S_{\text{dS}} \sim 10^{122}$ boundary modes, yielding a discrepancy of $\sqrt{S_{\text{dS}}} \sim 10^{61}$. The full observed $10^{122}$ corresponds to an effective dimensionality $N_{\text{eff}} \sim S_{\text{dS}}^2 \sim 10^{244}$, reflecting the all-to-all correlation structure that scrambling imposes on the cosmological horizon; a Weingarten-calculus derivation of this upper bound is the central open mathematical problem.

Tracing out the trans-horizon sector via the Nakajima-Zwanzig formalism yields dynamics that are provably non-Markovian. Multiple independent arguments — conservation-law-enforced information backflow, sub-ohmic spectral density at strong coupling, timescale collapse, and $O(1)$ mode migration through the evolving horizon — support CP-indivisibility. By Barandes' stochastic-quantum correspondence [14, 15], CP-indivisible dynamics recovers the Schrödinger equation as the mandatory description of an embedded observer. A decisive numerical test — computing the decoherence rates for the de Sitter spectral density via t-DMRG or Keldysh FRG — is feasible with existing methods.

The framework yields falsifiable predictions: gravitational wave echoes ($\sim$54 ms for a $30 M_\odot$ remnant), a stochastic gravitational noise floor, and a slowly evolving effective cosmological constant in the Running Vacuum Model form, testable by DESI, Euclid, and the Vera Rubin Observatory.

---

## I. INTRODUCTION

### 1.1 The Incompatibility Problem
Quantum mechanics and general relativity are extraordinarily successful yet structurally incompatible. Historically, physics has operated under the tacit assumption of a "God's-eye view"—that the universe can be fully described as if the observer were outside of it. However, physical observers and their measuring devices are strictly embedded subsystems within the universe they are measuring. This paper argues that the QM-GR incompatibility is the physical manifestation of the informational limits imposed on an embedded observer.

The observer's epistemic situation has been foregrounded before — QBism treats quantum states as expressions of an agent's beliefs, and relational quantum mechanics defines states relative to interacting subsystems. These programs take observer-dependence as an interpretive starting point. The present framework differs in a crucial respect: it *derives* observer-dependence from the physical structure of causal horizons and the mathematical limits on embedded inference, producing quantitative predictions (§4) rather than reinterpretations of existing formalism.

### 1.2 Embedded Inference and Complementary Projections

The sharpest consequence of embedded observation is that different physical subsystems, coupling to the same underlying degrees of freedom through different mechanisms, can produce irreconcilable measurements — not because one is wrong, but because each discards different information. We partition the total state space $\Omega$ into degrees of freedom accessible to an observer (the visible sector) and degrees of freedom rendered inaccessible by spacetime's causal structure (the hidden sector) — primarily trans-horizon modes beyond the observable universe and the interiors of black holes.

Two physical couplings to the vacuum define two projection maps from $\Omega$ to observables: localized matter couples to the unsigned total vacuum activity ($\pi_Q$, measuring $\langle \hat{\phi}^2 \rangle$), while spacetime geometry couples to the net signed stress-energy density ($\pi_G$, measuring $\langle T_{00} \rangle$). Both maps are many-to-one — distinct full-universe configurations yield identical outputs — but their kernels are non-identical: $\pi_Q$ sums magnitudes while $\pi_G$ sums algebraically with signs. Section 2.1 shows that this structural difference produces the $10^{122}$ discrepancy via the Central Limit Theorem.

Wolpert's (2008) limits of inference [4] confirm that this discrepancy cannot be resolved by any embedded observer. Wolpert proved that any physical subsystem whose state is a deterministic, many-to-one function of the total configuration constitutes an inference device subject to absolute limits: two such devices with non-identical surjective projections cannot fully reconstruct each other's conclusions from their own outputs alone (the Mutual Inference Impossibility). Applying this result requires verifying three conditions for each device:

**Device 1 — Localized Matter ($\pi_Q$).** Any localized matter system (e.g., an atom subject to the Lamb shift) constitutes an inference device whose output is the local expectation value $\langle \hat{\phi}^2 \rangle$. This map is: (i) *embedded* — the matter system is a proper subsystem of $\Omega$, occupying a finite worldtube; (ii) *surjective (many-to-one)* — distinct full configurations $\omega \neq \omega'$ that differ only in trans-horizon modes yield $\pi_Q(\omega) = \pi_Q(\omega')$; and (iii) its kernel is the hidden sector, integrated by unsigned summation.

**Device 2 — Spacetime Geometry ($\pi_G$).** The local gravitational field constitutes a second inference device whose output is the net signed stress-energy density $\langle T_{00} \rangle$ sourcing Einstein's equations. This map is: (i) *embedded* — the metric is itself a dynamical degree of freedom within $\Omega$; (ii) *surjective* — distinct configurations with different individual mode contributions $s_i|E_i|$ can produce the same net $T_{00}$; and (iii) its kernel is again the hidden sector, but integrated by algebraic (signed) summation.

Both devices satisfy Wolpert's formal requirements, and the relevant criterion is not intentionality but structure: any physical subsystem whose state is a deterministic, many-to-one function of the total configuration qualifies, regardless of whether the mapping constitutes "computation" in the colloquial sense [4]. Because the two kernels are non-identical — $\pi_Q$ discards sign information while $\pi_G$ retains it — the Mutual Inference Impossibility is triggered. The discrepancy is a structural limit on embedded observation, not an error awaiting correction.

---

## II. OBSERVATIONAL UNDECIDABILITY

### 2.1 The Two Projection Maps and the Square-Root Suppression

The cosmological constant problem [1, 2, 3] — quantum mechanics predicts a vacuum energy of $\sim 10^{113} \text{ J/m}^3$ while general relativity measures $\sim 6 \times 10^{-10} \text{ J/m}^3$, a ratio of $10^{122}$ — is the quantitative expression of the structural limit identified in §1.2. We now show that this ratio directly encodes the hidden-sector dimensionality.

The two projection maps are formally:

$$\pi_Q : \Omega \to \mathbb{R}, \qquad \pi_Q(\omega) = \langle \hat{\phi}^2 \rangle_\omega \qquad \text{(unsigned total)}$$

$$\pi_G : \Omega \to \mathbb{R}, \qquad \pi_G(\omega) = \langle T_{00} \rangle_\omega \qquad \text{(signed net)}$$

A thermodynamic analogy clarifies why these must differ. When measuring a glass of water, a thermometer records the total unsigned kinetic energy of all molecules (a variance-type measurement), producing a massive reading because nothing cancels out. A suspended dust speck responds only to the net mechanical push from all sides (a mean-type measurement), leaving a tiny statistical residual. 

**The Variance Target (Localized Matter).** Localized matter measuring the vacuum (e.g., via the Lamb shift) acts as the thermometer. Because the field operator is squared ($\hat{\phi}^2$), its expectation value is strictly positive-definite for all modes. This measures the unsigned total activity: $V \propto \sum_{i=1}^{N} \langle \hat{\phi}_i^2 \rangle = N \langle E \rangle$.

**The Mean Target (Spacetime).** The local gravitational field acts as the dust speck. It couples dynamically to the net signed sum of the stress-energy tensor. This is a mean-type projection: $M = \langle T_{00} \rangle = \sum_{i=1}^{N} s_i |E_i|$, where $s_i \in \{+1, -1\}$ is the spin-statistics sign of the $i$-th mode.

Near a causal horizon, the Unruh temperature [18] $T_U = \frac{\hbar a}{2\pi k_B c}$ diverges as proper acceleration $a \to \infty$. In this ultra-relativistic, infinite-temperature limit ($T_U \gg m_i$), the active trans-horizon modes behave as a randomized, maximally mixed conformal fluid. Consequently, the spin-statistics sign $s_i$ over the $N$ modes functions as an independent, identically distributed random variable with a mean $\langle s_i \rangle = 0$.

By the Central Limit Theorem, the expected value of the gravitational sum is zero, but its root-mean-square fluctuation is strictly non-zero and scales with the square root of the number of states:
$$M_{\text{rms}} = \sqrt{\sum_{i=1}^{N} (s_i |E_i|)^2} = \sqrt{N} \langle |E_i| \rangle$$

Therefore, the ratio of the variance projection to the mean-squared projection strictly scales as the square root of the hidden-sector dimensionality:
$$\frac{V}{M_{\text{rms}}} \approx \frac{N \langle |E_i| \rangle}{\sqrt{N} \langle |E_i| \rangle} = \sqrt{N}$$

> **Observational Undecidability Principle.** For any many-to-one partition of the universe into visible and hidden sectors, the variance-type projection $V = \sum |E_i|$ and the mean-type projection $M = \sum s_i |E_i|$ satisfy $V/M_{\text{rms}} = \sqrt{N}$, where $N$ is the hidden-sector dimensionality. The discrepancy between them is a structural consequence of embedded observation, not a fine-tuning problem.

### 2.2 The $10^{122}$ Discrepancy
The ratio of the two projections directly encodes the hidden sector's dimensionality. Setting $V/M_{\text{rms}} = \sqrt{N} = 10^{122}$ yields $N \sim 10^{244}$. This number requires physical justification. The argument proceeds in three steps.

**Step 1: Holographic mode counting.** The Bekenstein-Hawking entropy of the cosmological horizon [10] is $S_{\text{dS}} = A/(4l_p^2) \sim 10^{122}$, counting the independent degrees of freedom on the horizon boundary [6]. In the Thermofield Double (TFD) vacuum, each visible-sector mode $v_i$ is entangled with a single hidden-sector partner $h_i$ — a one-to-one pairing. If this structure persisted, the effective CLT dimensionality would be $N \sim S_{\text{dS}} \sim 10^{122}$, predicting a discrepancy of $\sqrt{N} \sim 10^{61}$.

**Step 2: Scrambling redistributes correlations.** The one-to-one TFD structure does not persist. Causal horizons are fast scramblers [19]: information is redistributed across all $S_{\text{dS}}$ degrees of freedom on the timescale $t_s \sim \ln(S_{\text{dS}})/H \sim 280 H^{-1}$ — cosmologically instantaneous. After scrambling, every visible-sector mode $v_i$ becomes correlated with every hidden-sector mode $h_j$. Each pairwise correlation is weak ($\sim 1/\sqrt{S_{\text{dS}}}$, consistent with random matrix universality [22]), but the correlation *matrix* is now dense rather than diagonal: the initially diagonal $S_{\text{dS}} \times S_{\text{dS}}$ correlation matrix $C_{ij} = \delta_{ij}$ is replaced by a Haar-random unitary rotation, producing a full-rank matrix with $S_{\text{dS}}^2$ nonzero entries.

**Step 3: Effective CLT dimensionality.** We now show that naive mode-counting recovers only half the observed discrepancy on a logarithmic scale, and identify a candidate mechanism for the remainder. The key question is why the effective number of fluctuating contributions to the gravitational stress-energy sum exceeds $S_{\text{dS}}$. In the pre-scrambling TFD state, correlations are one-to-one: each visible mode $v_i$ pairs with exactly one hidden mode $h_i$, and the signed contributions $s_i |E_i|$ to $\langle T_{00} \rangle$ have $N = S_{\text{dS}}$ terms. The CLT gives $V/M_{\text{rms}} = \sqrt{S_{\text{dS}}} \sim 10^{61}$.

After scrambling, each visible mode $v_i$ receives signed contributions from all $S_{\text{dS}}$ hidden modes. The stress-energy sum acquires the form $\langle T_{00} \rangle \sim \sum_{i=1}^{S_{\text{dS}}} \sum_{j=1}^{S_{\text{dS}}} C_{ij} s_{j} |E_{j}|$, where $C_{ij}$ are the entries of the Haar-random scrambled correlation matrix. The effective dimensionality of this sum depends on the variance structure of the double sum: $\text{Var}(M) = \sum_{i,j,i',j'} \langle C_{ij} C_{i'j'} \rangle \langle s_j s_{j'} \rangle |E_j||E_{j'}|$. The Weingarten calculus [47] gives the second-moment structure of Haar-distributed unitaries; in particular, off-diagonal entries are pairwise uncorrelated to leading order in $1/S_{\text{dS}}$ [22], so the cross-terms with $j \neq j'$ are suppressed. However, the entries sharing the same column index $j$ are constrained by unitarity ($\sum_i |C_{ij}|^2 = 1$), introducing intra-column correlations. The net variance receives contributions from $S_{\text{dS}}^2$ terms in the double sum, each of order $|E|^2/S_{\text{dS}}$, yielding:

$$\text{Var}(M) \sim S_{\text{dS}} \cdot \langle |E|^2 \rangle$$

This is identical in scaling to the pre-scrambling variance — a consequence of the fact that unitary rotations preserve the total norm. A naive application of the CLT with $N = S_{\text{dS}}$ boundary modes therefore predicts $V/M_{\text{rms}} \sim 10^{61}$, not $10^{122}$.

**The additional factor of $S_{\text{dS}}$.** The full observed discrepancy $\sim 10^{122}$ requires an effective dimensionality $N_{\text{eff}} \sim S_{\text{dS}}^2 \sim 10^{244}$. The gravitational projection $\pi_G$ does not merely sum over boundary modes; it couples to $\langle T_{00} \rangle$ sourced by all field-theoretic modes within the visible sector, whose number vastly exceeds $S_{\text{dS}}$. The holographic bound constrains the *independent* degrees of freedom to $S_{\text{dS}}$, but the signed fluctuation sum runs over all field modes before the holographic projection reduces the state space. In a scrambled state, the mapping from the $\sim S_{\text{dS}}^2$ entries of the dense correlation matrix to the effective stress-energy fluctuation involves a double trace — over visible and hidden indices — that is not equivalent to a single trace over $S_{\text{dS}}$ independent variables. A rigorous derivation requires computing the full second-moment structure of $\langle T_{00} \rangle$ in the Haar-scrambled TFD state using the Weingarten calculus [47] or replica methods; this calculation has not been performed and constitutes an important open problem.

We therefore present two bracketing results:

$$10^{61} \lesssim \frac{V}{M_{\text{rms}}} \lesssim 10^{122}$$

The lower bound ($\sqrt{S_{\text{dS}}}$) follows rigorously from the CLT applied to $S_{\text{dS}}$ boundary modes. The upper bound ($S_{\text{dS}}$) follows if the effective dimensionality of the scrambled double sum saturates at $S_{\text{dS}}^2$, as the all-to-all correlation structure and random matrix universality [22] suggest. The observed discrepancy of $10^{122}$ is consistent with the upper bound and would encode the full correlation structure of the scrambled cosmological horizon — both the boundary entropy and its dynamical redistribution. Settling whether the upper bound is realized is a concrete mathematical target: a Weingarten-calculus computation of $\text{Var}(\langle T_{00} \rangle)$ in the scrambled state.

### 2.3 Robustness of the $\sqrt{N}$ Scaling

The CLT requires that the spin-statistics signs $s_i$ be effectively independent of the amplitude degrees of freedom, and that the magnitudes $|E_i|$ be comparable across species. Both conditions hold for the trans-horizon bath.

The sign $s_i = +1$ (bosonic) or $s_i = -1$ (fermionic) is fixed by the field’s representation under the Lorentz group, as guaranteed by the spin-statistics theorem following from CPT invariance. Crucially, $s_i$ labels a superselection sector: no continuous dynamical process can rotate a bosonic mode into a fermionic one. The TFD vacuum correlates occupation numbers of partner modes across the causal boundary but acts *within* each field species, preserving the sign throughout. The factorization $\langle s_i |E_i| \rangle = \langle s_i \rangle \langle |E_i| \rangle$ therefore holds exactly within each energy shell. In the ultra-relativistic regime near the horizon ($T_U \gg m_i$), all fields approach conformal behavior and the energy density per degree of freedom converges to Stefan–Boltzmann scaling. The Standard Model’s slight fermionic majority (90 vs. 28 helicity degrees of freedom) gives $\langle s_i \rangle \approx -0.5$, but this residual asymmetry contributes a correction subleading to the $\sqrt{N}$ fluctuation term; the scaling is preserved.

The iid assumption on mode amplitudes can also be relaxed. For a fast-scrambling horizon bath, amplitude correlations decay exponentially on the scrambling timescale $t_s \sim \ln S / H$, satisfying the $\alpha$-mixing condition. Bradley’s CLT for mixing sequences [40] guarantees $M/\sqrt{N} \to \mathcal{N}(0, \sigma^2)$ with convergent covariance sum, so the $\sqrt{N}$ scaling is robust to short-range correlations. Only long-range power-law correlations with exponent $\alpha < 1/2$ could alter it, but such correlations would require sign-aligned amplitude clustering across widely separated energy scales, which scrambling dynamics actively destroy. We note that pairwise uncorrelatedness alone is insufficient for the CLT — Avanzi et al. [48] constructed explicit counterexamples — but the $\alpha$-mixing condition, which scrambling dynamics enforce by exponentially suppressing correlations beyond $t_s$, is the strictly stronger condition that Bradley's theorem requires.

The $\sqrt{N}$ scaling is therefore robust under all physically realized relaxations of the iid assumption: superselection protects sign-amplitude independence, conformal scaling equalizes magnitudes, and scrambling enforces the mixing condition that guarantees CLT convergence.

---

## III. THE EMERGENCE OF QUANTUM MECHANICS

### 3.1 Classical Axioms and the Trace-Out Operation
We now ask what happens to a localized particle embedded in a universe with $10^{244}$ inaccessible degrees of freedom. The framework derives quantum mechanics from three classical premises:
1.  **Classical Continuous Dynamics:** The total universe evolves deterministically via the continuous Liouville equation: $\frac{\partial \rho}{\partial t} = \{H, \rho\}$.
2.  **Classical General Relativity:** Einstein's field equations define the absolute information barriers of the hidden sector. 
3.  **Classical Probability Theory:** Observational predictions are classical expectation values.

Because the total dynamics are deterministic, an observer who cannot track the $10^{244}$ hidden states must "trace out" the hidden sector to predict the behavior of localized matter. Sections 3.2–3.3 show that this trace-out produces non-Markovian, and on strong physical grounds CP-indivisible, dynamics—the key condition for quantum mechanics to emerge via Barandes' stochastic-quantum correspondence.

(This program shares a broad structural similarity with ’t Hooft’s deterministic quantum mechanics [46], which also derives quantum behavior from underlying deterministic dynamics through information loss; the key difference is that ’t Hooft locates information loss at the Planck scale, whereas the present framework locates it at the cosmological horizon, leading to different empirical predictions.)

### 3.2 Failure of Markovian Approximation

Tracing out the hidden sector via the Nakajima-Zwanzig formalism [12, 13, 20] yields a Generalized Langevin Equation with a non-local memory kernel $\gamma(t-\tau)$, where the $10^{244}$ trans-horizon states act as a continuous background noise $\xi(t)$:
$$m\ddot{x}(t) = -\nabla V(x) - \int_{0}^{t} \gamma(t-\tau)\dot{x}(\tau)d\tau + \xi(t)$$

A standard objection is that tracing out a vast bath should produce classical decoherence—memoryless noise that destroys quantum behavior. For a generic thermal bath, this is correct: the Markovian approximation holds whenever the bath correlation time is much shorter than the system’s dynamical timescale. The cosmological horizon trace-out fails this prerequisite.

Any Markovian master equation — Lindblad, Redfield, or Davies — requires a strict timescale separation [20]: $\tau_B \ll \tau_S \ll \tau_R$ (bath correlation time ≪ system timescale ≪ relaxation time). For the cosmological horizon, this hierarchy fails in both relevant regimes:

*Cosmological observables* ($\omega \sim H$): All three timescales collapse to the same order — $\tau_B \sim \tau_S \sim \tau_R \sim 1/H$ — because the bath correlation time (set by the Gibbons-Hawking temperature $T_{\text{GH}} = H/2\pi$), the dynamical timescale of cosmological observables, and the de Sitter equilibration time are all set by the Hubble scale. The Markovian approximation fails by its own defining criterion.

*Laboratory-scale matter* ($\omega \gg H$): The hierarchy is inverted: $\tau_S \sim 1/\omega \sim 10^{-20}$ s while $\tau_B \sim 1/H \sim 10^{17}$ s. The trans-horizon bath is not a fast-fluctuating reservoir the system averages over; it is a quasi-static noise source whose correlations persist over timescales vastly exceeding the system’s dynamics — a “frozen bath” regime that also violates the Markovian approximation, though through a different mechanism.

Kaplanek and Burgess [37, 38] demonstrated that an accelerated Unruh-DeWitt detector can evolve via a Markovian Lindblad equation at late times near a Rindler or Schwarzschild horizon. This is fully consistent with the above: their results apply to a localized qubit with $\omega \gg H$, precisely the regime where the timescale separation holds, the coupling is perturbatively weak, and the spectral density is ohmic. They themselves identified that as $\omega \to H$, the Markovian validity window closes due to “critical slowing down” [39].

### 3.3 Arguments for CP-Indivisibility

Non-Markovianity is necessary but not sufficient; quantum mechanics requires the stronger condition of CP-indivisibility. The following arguments, ordered from most physically transparent to most technically specific, collectively support this claim.

**Conservation-driven information backflow.** CP-divisible dynamics requires monotonically decreasing trace distance between system states. Two features of the cosmological horizon violate this requirement. First, stress-energy conservation across the horizon forces correlations that cannot decay monotonically: if two visible-sector configurations differ by $\Delta E$, the hidden sector must differ by $-\Delta E$. This is not a perturbative correction but the dominant feature producing the $10^{122}$ discrepancy [21]. Any dynamical map that attempts to erase the system's memory of these correlations violates a conservation law — the environment cannot reset to equilibrium because it is constrained to mirror the system's energy content at all times. Second, the horizon itself evolves, migrating modes between sectors at $\dot{H}/H^2 \approx -0.45$ — roughly 45% of horizon-scale modes per Hubble time. Scrambling redistributes this information across all degrees of freedom, and conservation forces it to influence the visible sector. (A formal extension of CP-indivisibility to time-dependent partitions has not been carried out and is a target for future work.)

**The non-perturbative regime.** Every existing proof that horizon dynamics can be rendered Markovian — Davies-Lindblad, Merkli [41], Kaplanek-Burgess [37, 38] — requires a small system-bath coupling. The gravitational coupling here is not perturbatively small; it produces the $10^{122}$ discrepancy. Moreover, perturbation theory is structurally blind to CP-indivisibility in this setting: the de Sitter Wightman function is strictly positive, so perturbative decoherence rates are positive at all frequencies regardless of regime. Non-perturbatively, however, the effective spectral density $J_{\text{eff}}(\omega) \to \eta H/\pi$ for $\omega \ll H$ gives a sub-ohmic exponent $s = 0$. Trushechkin [49] proved rigorously (in an exactly solvable pure-decoherence model) that Markovian embedding is possible *only* for Ohmic spectral densities and is impossible for sub-Ohmic baths — the non-Markovian dynamics cannot be reproduced by any finite-dimensional Markovian extension. Otterpohl et al. [50], using the numerically exact time-evolving matrix product operator approach, discovered a previously unknown dynamical phase in the sub-ohmic spin-boson model at strong coupling: aperiodic, highly non-Markovian dynamics in which the system coherence is "slaved" to oscillatory bath dynamics. Tensor network [42] and NRG [43] calculations confirm that sub-ohmic baths at strong coupling generically produce CP-indivisible dynamics. The de Sitter bath maps onto this parameter class as follows. Its sub-ohmic exponent $s = 0$ matches the regime studied by Trushechkin ($s < 1$), Otterpohl et al. ($s = 0.5$ at strong coupling), and the tensor network calculations of Chin et al. ($s < 1$, $\alpha > \alpha_c$). The gravitational coupling strength $\alpha \sim \langle T_{00} \rangle / E_{\text{Pl}}$ is non-perturbative by construction — the $10^{122}$ discrepancy is its empirical measure — placing it firmly in the strong-coupling regime where all three studies find CP-indivisible dynamics. The bath temperature $T = H/2\pi$ is the Gibbons-Hawking temperature, finite and fixed by the cosmological horizon. While none of the cited calculations were performed at precisely these parameter values, the de Sitter bath occupies the interior of the CP-indivisible region in the $(s, \alpha)$ phase diagram, not its boundary; the claim is that no known mechanism would restore divisibility at $s = 0$ and $\alpha \gg 1$ when it is absent throughout the surrounding parameter space.

**Additional structural constraints.** The TFD vacuum entanglement across the horizon means CP-divisible dynamics is measure-zero in the space of unitaries [23]. Spectral rigidity from fast scrambling [19, 22] prevents bath correlations from decaying to zero. Conservation laws prevent the environment from resetting to equilibrium, invalidating the Born approximation independently of coupling strength [21].

### 3.4 The Trace-Out Conjecture

> **The Trace-Out Conjecture.** Tracing out the trans-horizon sector in the cosmological setting forces the marginal dynamics of the visible sector into a CP-indivisible stochastic process. Any faithful mathematical representation of these dynamics is empirically equivalent to quantum mechanics.

The preceding sections establish that the dynamics are provably non-Markovian (§3.2), the coupling is non-perturbative and the spectral density sub-ohmic (§3.3), and every structural property of the bath independently disfavors CP-divisibility.

**Concrete computational target.** What remains open is a non-perturbative calculation of the decoherence rates $\gamma_k(t)$ for the de Sitter spectral density. The decisive test is a sub-ohmic ($s = 0$) spin-boson model at coupling $\alpha \gtrsim 1$ and temperature $T = H/2\pi$: if $\gamma_{\min}(t) < 0$ for any $t > 0$, the dynamics are CP-indivisible. Existing t-DMRG methods [42] and Keldysh FRG can access this regime; either would settle the conjecture.

The framework’s falsifiable predictions (§4.1, §4.5) do not depend on the specific mechanism producing indivisibility, only on the fact of it; if the dynamics are CP-indivisible for any reason, Barandes’ correspondence [14, 15] guarantees the framework follows.

### 3.5 From Indivisibility to the Schrödinger Equation

By Barandes' stochastic-quantum correspondence [14, 15], any indivisible stochastic process on configuration space is mathematically equivalent to a unitarily evolving quantum system. The Schrödinger equation is therefore the unique description an embedded observer must use to predict the marginal behavior of a system coupled to this bath.

Barandes' proof is formulated for finite-dimensional configuration spaces, while the cosmological trace-out acts on an infinite-dimensional visible sector. The extension to infinite dimensions via standard limiting arguments has not been carried out explicitly; this is a mathematical step distinct from the physical question of CP-indivisibility.

The Barandes mapping guarantees a unitarily evolving quantum description reproducing all transition probabilities, which permits the recovery of a quantum potential $Q = -\frac{\hbar^2}{2m} \frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}}$ with diffusion coefficient $D = \hbar/2m$. The identification $D = \hbar/2m$ is a consistency condition linking the noise floor to the measured value of $\hbar$; deriving this coefficient from the bath's spectral density remains open (see §5).

Le et al. [17] proved that CP-divisible dynamics satisfies temporal Tsirelson's bound ($B \le 2\sqrt{2}$). This provides a sharp falsification criterion: if the trace-out of this constrained hidden sector violates temporal Tsirelson's bound, it is provably CP-indivisible and inherently quantum. Conversely, if the cosmological dynamics can be shown to *satisfy* the bound, the conjecture would be significantly weakened.

---

## IV. IMPLICATIONS & PREDICTIONS

### 4.1 Deriving the Running Vacuum Model

The hidden-sector dimensionality $N$ derived in §2.2 is not a fixed constant. It is set by the Bekenstein-Hawking entropy of the cosmological horizon, $S_{\text{dS}} \sim A/4l_p^2$, which depends on the horizon area and therefore evolves with the expansion history of the universe. In an accelerating universe, this evolution has a specific and potentially observable consequence.

The cosmological event horizon—the boundary beyond which events occurring now will never be observable—has a finite comoving radius that is *shrinking* as the expansion accelerates. Each object pushed beyond this horizon permanently adds degrees of freedom to the hidden sector. In the far future, as the universe asymptotes to pure de Sitter space, essentially everything outside the gravitationally bound local group will have crossed beyond the horizon.

Because $N = S_{\text{dS}}^2$ and the horizon entropy evolves with the Hubble parameter as $S_{\text{dS}} \sim 1/H^2$, the hidden-sector dimensionality inherits a specific time dependence. The ratio of the two projections (§2.1) becomes epoch-dependent:

$$\frac{V}{M_{\text{rms}}} = \sqrt{N(t)} = S_{\text{dS}}(t) \sim \frac{1}{H(t)^2}$$

A naive reading of this scaling might suggest $\Lambda_{\text{eff}}(t) \propto H(t)^2$ as a standalone dark energy model. However, as Hsu [30] showed, a pure $\rho_\Lambda \propto H^2$ scaling yields an effective equation of state $w = 0$, mimicking pressureless dust and precluding cosmic acceleration. The resolution is that the observed $\Lambda_0$ is the current epoch’s gravitational residual, anchored to today’s horizon area; what evolves is the *deviation* from this value. Expanding around the present epoch

$$\Lambda_{\text{eff}}(t) = \Lambda_0 + \frac{d\Lambda_{\text{eff}}}{dH^2}\bigg|_{H_0} (H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

The derivative is calculable from the $\sqrt{N}$ scaling. Since $M_{\text{rms}} \propto 1/\sqrt{N} \propto H^2$ and $\Lambda_0 \gg \delta\Lambda$, the leading correction takes the form:

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu_{\text{OI}}}{8\pi G}(H^2 - H_0^2)$$

where $\nu_{\text{OI}}$ is a dimensionless coefficient encoding the rate at which the hidden-sector dimensionality responds to changes in the Hubble parameter. This is precisely the form of the Running Vacuum Model (RVM) [31, 32], arrived at here from information-theoretic rather than renormalization-group arguments. The constant offset $\Lambda_0$ is not imposed by hand but emerges naturally as the present-epoch gravitational residual; the $H^2$-dependent correction captures the slow migration of degrees of freedom across the cosmological horizon.

### 4.2 The $\nu_{\text{OI}}$ Coefficient

The prediction at this stage is one of *functional form*, not *magnitude*: the framework derives $\Lambda_{\text{eff}} = \Lambda_0 + 3\nu_{\text{OI}}(H^2 - H_0^2)/(8\pi G)$ with $\nu_{\text{OI}} > 0$, but cannot yet determine $\nu_{\text{OI}}$ from first principles. Pinning down this coefficient is the most important calculational target for future work within the framework.

Dimensional analysis points to an expected scaling. In the standard RVM, the analogous coefficient $\nu_{\text{RVM}} \sim M_i^2/M_{\text{Pl}}^2 \sim 10^{-3}$ emerges from adiabatic regularization, where quartic divergences cancel and only quadratic ($\sim m^2 H^2$) terms survive [33]. The same suppression is expected here: the $\sqrt{N}$ scaling of §2.1 relates the *ratio* of the two projections to $N$, not the absolute value of $\Lambda_{\text{eff}}$, and the mapping from projection ratio to effective cosmological constant involves the spectral density of the trans-horizon bath. Only modes near $\omega \sim H$ actively migrate as the horizon evolves; the vast majority at $\omega \gg H$ are insensitive. If the heaviest species contributing to this active migration shell has mass $M_*$, dimensional analysis gives $\nu_{\text{OI}} \sim M_*^2/M_{\text{Pl}}^2$, recovering the RVM scaling from an information-theoretic derivation path. This expected value of $\sim 10^{-3}$ is consistent with current observational constraints (DESI + Planck constrain $\nu < 10^{-2}$) and lies well within the regime accessible to next-generation surveys.

As a sanity check, two extreme estimates bracket the result: a naive $N = S_{\text{dS}}^2 \sim H^{-4}$ estimate gives $\nu_{\text{OI}} \sim \Omega_\Lambda \sim 0.7$ (excluded by observation), while a thin-shell estimate using only Planck-scale modes gives $\nu_{\text{OI}} \sim (H_0/M_{\text{Pl}})^2 \sim 10^{-122}$ (undetectably small). The dimensional analysis result falls between these bounds at a physically natural scale. A first-principles calculation—requiring the same non-perturbative methods (t-DMRG or Keldysh FRG) identified as the decisive computation for the Trace-Out Conjecture in §3.4—would determine whether this scaling is correct.

### 4.3 Observational Status and Model Differentiation

Dark energy surveys — DESI, Euclid, and the Vera Rubin Observatory — are measuring the equation of state parameter $w$ with increasing precision. DESI's 2024 Data Release 1 [29] and 2025 Data Release 2 report evidence for evolving dark energy at 2.8σ–4.2σ depending on dataset combination, with the signal strengthening as data has doubled. De Cruz Pérez, Gómez-Valent, and Solà Peracaula [34] tested RVM variants against DESI DR2 + Planck PR4 + supernovae and found preference for dynamical vacuum ($\nu > 0$) at 2.7σ–3.1σ over $\Lambda$CDM, with the best-fit sign consistently indicating energy flow from matter into the vacuum. If confirmed by independent probes, this would be consistent with the framework's prediction that the hidden-sector dimensionality is slowly growing as the cosmological horizon evolves.

**Differentiation from competing models.** The functional form $\Lambda_{\text{eff}} = \Lambda_0 + \beta H^2$ is shared by several independent theoretical programs: the QFT-derived RVM [31], holographic dark energy with Granda-Oliveros cutoff [35], and the stringy RVM from Chern-Simons gravitational anomalies [36]. These models make identical background-cosmology predictions and cannot be distinguished by expansion-history measurements alone. However, the present framework differs from all of them in a structurally important way: it predicts gravitational wave echoes (§4.5) and a stochastic gravitational noise floor from the same hidden-sector physics that sources the cosmological evolution. No purely cosmological RVM or holographic model makes such predictions. The conjunction of confirmed dark energy evolution *and* detected GW echoes would uniquely favor an information-theoretic origin over renormalization-group or holographic derivations.

### 4.4 Interpretive Consequences

The framework resolves several foundational puzzles as direct consequences of its structure rather than additional postulates. Because the framework is empirically equivalent to standard quantum mechanics by construction (via Barandes’ correspondence), these are interpretive implications rather than distinguishing predictions.

#### 4.4.1 The Double-Slit Experiment and Bell’s Theorem

The double-slit experiment is explained through continuous, single-universe stochastic dynamics: the particle traverses a single slit, and opening or closing the second slit alters the boundary conditions of the local field configuration, modifying the quantum potential that guides the particle’s trajectory. Bell’s theorem [11] is addressed through dynamical indivisibility: in Barandes’ formalization [14, 15, 16], the transition maps of an indivisible stochastic process cannot be factored through any intermediate time, so $P(a,b|x,y,\lambda)$ does not factorize — even though each measurement is performed locally and measurement independence is preserved. What fails is the assumption that the dynamical law connecting the shared past to two distant outcomes can be decomposed into independent, memoryless local processes. No faster-than-light signaling is required.

#### 4.4.2 Wigner’s Friend

The Wigner’s Friend paradox asks how to reconcile the Friend’s definite measurement outcome inside a sealed laboratory with Wigner’s assignment of a superposition to the entire lab. In this framework, the resolution is straightforward: inside the laboratory, the Friend’s measurement produces a definite outcome driven by classical stochastic divergence — the indivisible dynamics of the visible sector select a specific trajectory from the stochastic ensemble, yielding a single result. Wigner, lacking access to the Friend’s realized trajectory, must describe the laboratory using the marginal state obtained by tracing out the degrees of freedom internal to the lab. His superposition assignment reflects this epistemic deficit, not the Friend’s physical state. There is no contradiction because the two descriptions operate at different levels of coarse-graining over the same underlying deterministic evolution.

#### 4.4.3 The Everettian Measure Problem

The Many-Worlds Interpretation treats the universal wavefunction as physically real and faces the measure problem: why does the Born rule assign probabilities correctly when all branches exist? This framework inverts the logic. The total universe evolves deterministically as a single continuous reality; the Schrödinger equation is a mandatory compression algorithm for an embedded observer who cannot track the $10^{244}$ hidden-sector degrees of freedom. The Born rule is not a separate postulate but the equilibrium distribution of the indivisible stochastic process recovered by Barandes’ correspondence [14, 15]. “Branches” are features of the compressed description, not of the underlying physics. The hierarchy is: classical total dynamics → quantum visible-sector dynamics (via cosmological trace-out) → classical macroscopic dynamics (via local decoherence).

#### 4.4.4 Black Hole Information and Singularities

A singularity is what results from extending a visible-sector description past its domain of validity — the same category of error as extrapolating a mean-field equation beyond its regime. Information falling past a black hole horizon is not destroyed but joins the hidden sector. The thermal Hawking spectrum [27] is the exterior observer’s marginal prediction from tracing out the interior degrees of freedom, directly analogous to the cosmological trace-out that produces quantum mechanics itself. Recent work on regular black holes from pure gravity [26], Planck stars [24], and string-theoretic resolutions [25] is consistent with this picture: all replace the singular point with a structure that preserves information while rendering it inaccessible to exterior observers.

#### 4.4.5 String Theory and AdS/CFT

The AdS/CFT correspondence [7] achieves exact unification by placing the observer on the asymptotic boundary — an external vantage point immune to Wolpert’s limits. Our de Sitter universe has no such boundary; the framework predicts that exact unification requires access to the complete state space $\Omega$, which is prohibited for embedded observers. This does not invalidate string-theoretic results but contextualizes their domain of applicability: AdS/CFT describes what an *external* observer would see, while the present framework describes the structural constraints facing an *internal* one.

### 4.5 Falsifiable Predictions
Because the quantum-gravity discrepancy is mapped to structural boundary limits, the global cosmological undecidability must scale down to local event horizons. 

* **Gravitational Wave Echoes:** The classical event horizon is replaced by an informational boundary located a microscopic distance $\epsilon$ outside the Schwarzschild radius $r_h$. Calculating the tortoise coordinate integral predicts a precise time delay for gravitational wave echoes:
$$\Delta t_{\text{echo}} \approx \frac{r_h}{c} \ln\left(\frac{r_h}{\epsilon}\right)$$
For a stellar-mass black hole remnant of $M = 30 M_\odot$ with $\epsilon \approx l_p$, the expected delay is approximately 54 ms.

> **Remark on the free parameter $\epsilon$.** The identification $\epsilon \approx l_p$ is physically motivated by the Planck-scale breakdown of semiclassical geometry but is *not derived* from the framework’s internal logic. It is the single free parameter of the prediction. A different value of $\epsilon$ would shift the predicted echo time logarithmically. The framework requires *some* informational boundary outside $r_h$ but does not fix its location from first principles.

To date, LIGO–Virgo–KAGRA searches for post-merger echoes have yielded null results [8], with the original claims of Abedi et al. remaining contested. A continued null result at the predicted timescale would constrain the location of the informational boundary but would not falsify the broader framework, since $\epsilon$ is a free parameter; what *would* falsify it is the complete absence of any echo structure at all scales. Crucially, a *population* of echo detections across mergers with different remnant masses would overconstrain $\epsilon$. The predicted timescale $\Delta t_{\text{echo}} \propto (GM/c^3)\ln(GM/c^2\epsilon)$ depends on mass logarithmically but on $\epsilon$ through the same logarithm; echo detections at consistent timescales across, say, 10, 30, and 60 $M_\odot$ remnants would either confirm or rule out a Planck-scale $\epsilon$ with no remaining freedom. A single detection has a free parameter; three or more do not.
* **Stochastic Gravitational Noise Floor:** Hidden-sector fluctuations must source a continuous stochastic background with an inverse-frequency-squared spectrum in the MHz–GHz band. Next-generation high-frequency gravitational wave detectors [9] could provide an independent test of this prediction.

> **Summary of falsification conditions.** The framework would be decisively falsified by any of the following: (1) a rigorous proof that the cosmological trace-out is CP-divisible (e.g., via the t-DMRG calculation of §3.4 returning $\gamma_{\min}(t) \geq 0$ for all $t$); (2) confirmation that dark energy is exactly constant ($\nu = 0$) to a precision excluding $\nu > 10^{-6}$; (3) detection of GW echoes at timescales *inconsistent* with a single $\epsilon$ across multiple remnant masses. The framework would be significantly weakened — though not strictly falsified — by a complete absence of echoes at all mass scales, or by the Weingarten-calculus computation of §2.2 yielding $N_{\text{eff}} \ll S_{\text{dS}}^2$.

---

## V. CONCLUSION

The incompatibility between quantum mechanics and general relativity is not a bug to be fixed. It is the physical manifestation of Wolpert’s limits on embedded inference [4]: a system embedded in the universe it measures cannot fully characterize that universe from within. The $10^{122}$ discrepancy is its empirical signature.

This paper has developed that intuition into a concrete framework. The $\sqrt{N}$ scaling between variance-type and mean-type projections rigorously produces a minimum discrepancy of $10^{61}$ from $S_{\text{dS}}$ boundary modes; the full $10^{122}$ is consistent with scrambling-induced correlations raising the effective dimensionality to $S_{\text{dS}}^2$ (§2.2). Tracing out the trans-horizon sector yields provably non-Markovian dynamics, with strong physical arguments for CP-indivisibility (§3.2–3.3); by Barandes’ correspondence, this recovers the Schrödinger equation as the mandatory description for an embedded observer.

Three open problems are decisive. First, a non-perturbative calculation of the decoherence rates $\gamma_k(t)$ for the de Sitter spectral density — a sub-ohmic ($s=0$) spin-boson model at coupling $\alpha \gtrsim 1$ and temperature $T = H/2\pi$ — would confirm or refute CP-indivisibility directly; this is feasible with existing t-DMRG or Keldysh FRG methods (§3.4). Second, the effective dimensionality $N_{\text{eff}}$ of the scrambled stress-energy sum must be computed via the Weingarten calculus or replica methods (§2.2). Third, the coefficient $\nu_{\text{OI}}$ governing dark energy evolution requires the same non-perturbative machinery (§4.2). Experimentally, gravitational wave echo searches are testable with current detectors; a population of detections across different remnant masses would overconstrain the single free parameter $\epsilon$ (§4.5).

Recognizing the Schrödinger equation as the macroscopic shadow of $10^{244}$ missing causal variables reframes the unification problem: the goal is not to force quantum mechanics and general relativity into a single formalism, but to understand why an embedded observer necessarily sees them as separate.

---

## DECLARATION OF AI-ASSISTED TECHNOLOGIES
During the preparation of this work, the author used **Claude Opus 4.6 (Anthropic)** and **Gemini 3.1 Pro (Google)** to assist in drafting, refining argumentation, and verifying bibliographic details. The author reviewed and edited the content and takes full responsibility for the publication.

---

## REFERENCES
[1] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).  
[2] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).  
[3] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).  
[4] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008).  
[5] A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem," *Proc. Lond. Math. Soc.* **s2-42**, 230–265 (1937).  
[6] G. 't Hooft, "Dimensional Reduction in Quantum Gravity," arXiv:gr-qc/9310026 (1993).  
[7] J. Maldacena, "The Large-N Limit of Superconformal Field Theories and Supergravity," *Int. J. Theor. Phys.* **38**, 1113–1133 (1999).  
[8] J. Abedi, H. Dykaar, and N. Afshordi, "Echoes from the Abyss," *Phys. Rev. D* **96**, 082004 (2017).  
[9] A. Arvanitaki and A. A. Geraci, "Detecting High-Frequency Gravitational Waves with Optically Levitated Sensors," *Phys. Rev. Lett.* **110**, 071105 (2013).  
[10] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).  
[11] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195–200 (1964).  
[12] S. Nakajima, "On Quantum Theory of Transport Phenomena," *Prog. Theor. Phys.* **20**, 948–959 (1958).  
[13] R. Zwanzig, "Ensemble Method in the Theory of Irreversibility," *J. Chem. Phys.* **33**, 1338–1341 (1960).  
[14] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).  
[15] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).  
[16] J. A. Barandes, S. Hasan, and J. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).  
[17] T. Le, F. A. Pollock, T. Paterek, M. Paternostro, and K. Modi, "Divisible quantum dynamics satisfies temporal Tsirelson's bound," *J. Phys. A* **50**, 055302 (2017).  
[18] W. G. Unruh, "Notes on black-hole evaporation," *Phys. Rev. D* **14**, 870 (1976).  
[19] Y. Sekino and L. Susskind, "Fast Scramblers," *JHEP* **2008**, 065 (2008).  
[20] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).  
[21] K. Babu et al., "Unfolding system-environment correlation in open quantum systems: Revisiting master equations and the Born approximation," *Phys. Rev. Research* **6**, 013243 (2024).  
[22] J. Cotler et al., "Black Holes and Random Matrices," *JHEP* **2017**, 118 (2017).  
[23] F. Buscemi, "Complete positivity, Markovianity, and the quantum data-processing inequality, in the presence of initial system-environment correlations," *Phys. Rev. Lett.* **113**, 140502 (2014).
[24] C. Rovelli and F. Vidotto, "Planck Stars," *Class. Quantum Grav.* **31**, 045003 (2014).  
[25] A. Wu, Y. Yan, and L. Ying, "Revisiting Schwarzschild black hole singularity through string theory," *Eur. Phys. J. C* **85**, 168 (2025).  
[26] P. Bueno, P. A. Cano, and R. A. Hennigar, "Regular Black Holes from Pure Gravity," *Phys. Lett. B* **861**, 139260 (2025).  
[27] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).  
[28] J. Glatthard, "Page curves and typical entanglement in linear optics," *Phys. Rev. D* **109**, L081901 (2024).
[29] DESI Collaboration, "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations," arXiv:2404.03002 (2024).  
[30] S. D. H. Hsu, "Entropy bounds and dark energy," *Phys. Lett. B* **594**, 13–16 (2004).  
[31] J. Solà Peracaula, "The cosmological constant problem and running vacuum in the expanding universe," *Phil. Trans. R. Soc. A* **380**, 20210182 (2022).  
[32] J. Solà Peracaula, A. Gómez-Valent, and J. de Cruz Pérez, "Running vacuum in the Universe: phenomenological status in light of the latest observations," *Universe* **9**, 262 (2023).  
[33] C. Moreno-Pulido and J. Solà Peracaula, "Renormalizing the vacuum energy in cosmological spacetime: implications for the cosmological constant problem," *Eur. Phys. J. C* **82**, 551 (2022).  
[34] J. de Cruz Pérez, A. Gómez-Valent, and J. Solà Peracaula, "Dynamical Dark Energy models in light of the latest observations," arXiv:2512.20616 (2025).  
[35] L. N. Granda and A. Oliveros, "Infrared cut-off proposal for the holographic density," *Phys. Lett. B* **669**, 275–277 (2008).  
[36] N. E. Mavromatos, S. Basilakos, and J. Solà Peracaula, "Stringy running vacuum model and current tensions in cosmology," *Class. Quantum Grav.* **41**, 015026 (2024).  
[37] G. Kaplanek and C. P. Burgess, "Hot accelerated qubits: decoherence, thermalization, secular growth and reliable late-time predictions," *JHEP* **2020**, 008 (2020).  
[38] G. Kaplanek and C. P. Burgess, "Qubits on the horizon: decoherence and thermalization near black holes," *JHEP* **2021**, 098 (2021).  
[39] G. Kaplanek and C. P. Burgess, "Hot cosmic qubits: late-time de Sitter evolution and critical slowing down," *JHEP* **2020**, 053 (2020).  
[40] R. C. Bradley, "Basic properties of strong mixing conditions. A survey and some open questions," *Prob. Surveys* **2**, 107–144 (2005).
[41] M. Merkli, "Dynamics of Open Quantum Systems I, Oscillation and Decay," *Quantum* **6**, 615 (2022).
[42] A. W. Chin, J. Prior, S. F. Huelga, and M. B. Plenio, "Generalized polaron ansatz for the ground state of the sub-ohmic spin-boson model: An analytic theory of the localization transition," *Phys. Rev. Lett.* **107**, 160601 (2011).
[43] H.-P. Breuer, E.-M. Laine, and J. Piilo, "Measure for the degree of non-Markovian behavior of quantum processes in open systems," *Phys. Rev. Lett.* **103**, 210401 (2009).
[44] W. H. Zurek, "Quantum Darwinism," *Nature Physics* **5**, 181–188 (2009).
[45] R. B. Griffiths, "Consistent histories and the interpretation of quantum mechanics," *J. Stat. Phys.* **36**, 219–272 (1984).
[46] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).  
[47] B. Collins and P. Śniady, "Integration with respect to the Haar measure on unitary, orthogonal and symplectic group," *Commun. Math. Phys.* **264**, 773–795 (2006).  
[48] B. Avanzi, G. Boglioni Beaulieu, P. Lafaye de Micheaux, F. Ouimet, and B. Wong, "A counterexample to the central limit theorem for pairwise independent random variables having a common arbitrary margin," *J. Math. Anal. Appl.* **499**, 124982 (2021).  
[49] A. Trushechkin, "Long-term behaviour in an exactly solvable model of pure decoherence and the problem of Markovian embedding," *Mathematics* **12**(1), 1 (2024).  
[50] F. Otterpohl, F. Nalbach, and M. Thorwart, "Hidden Phase of the Spin-Boson Model," *Phys. Rev. Lett.* **129**, 120406 (2022).
