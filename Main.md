# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

Physical observers are subsystems of the universes they measure, permanently barred from accessing degrees of freedom beyond their causal reach. We prove that any such observer — coupled to a slow, high-capacity hidden sector on a finite-dimensional configuration space — must describe the visible sector using P-indivisible stochastic dynamics, mathematically equivalent to unitary quantum mechanics. The converse also holds: any quantum system, realized as a deterministic dilation, requires non-trivial coupling, slow-bath memory, and sufficient hidden-sector capacity. The Schrödinger equation, Born rule, and Bell violations emerge as structural consequences requiring no independent quantum postulates.

Applied to the cosmological horizon, the framework uniquely determines $\hbar = c^3 \epsilon^2 / (4G)$, fixes $\epsilon = 2\,l_p$, and recovers the Bekenstein-Hawking entropy $S = A/(4\,l_p^2)$. The $10^{122}$ cosmological constant discrepancy is identified as $S_{\text{dS}}$, the information compression ratio of the emergent quantum description; the observed vacuum energy is the mandatory classical baseline. Falsifiable predictions include dark energy evolution in Running Vacuum Model form with $\nu_{\text{OI}} \approx 2.45 \times 10^{-3}$, consistent with current data, and gravitational wave echoes near black hole horizons.

---

# PART I: THE GENERAL THEOREM

## 1. INTRODUCTION

### 1.1 The Problem of Embedded Observation

An observer embedded in a deterministic universe cannot access the complete state: degrees of freedom beyond causal reach are permanently hidden, and the observer's description is obtained by marginalizing over the hidden sector. The question is what this reduction imposes on the form of the observer's physical laws.

Prior work (QBism, relational QM, 't Hooft's cellular automaton [1]) takes observer-dependence as an interpretive starting point or derives it from specific microphysical models. This framework differs by identifying *necessary and sufficient conditions* under which any embedded observer in any deterministic system necessarily sees quantum mechanics — and proving these are the *only* conditions under which QM arises from a deterministic embedding. These constraints carry empirical weight: the framework reveals that phenomena previously viewed as catastrophic anomalies — most notably the $10^{122}$ cosmological constant discrepancy — are mandatory consequences of embedded observation.

### 1.2 Axioms

The framework rests on four axioms referencing no quantum mechanics, general relativity, or specific physical theory.

1. **Deterministic dynamics.** The total system evolves deterministically on a phase space $\Gamma$ via a Hamiltonian flow $\phi_t$. A probability density $\rho$ on $\Gamma$ (representing the observer's incomplete knowledge) evolves by the Liouville equation:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\} \equiv \mathcal{L}\rho$$

2. **Finiteness.** The effective configuration space of the visible sector is finite-dimensional, with a discreteness scale $\epsilon$ providing a finite minimal cell volume. Any observer bounded by a finite-area surface can couple to only finitely many modes across that boundary; independent support comes from holographic entropy bounds [27]. In Part I, $\epsilon$ is free; self-consistency (§6) pins $\epsilon = 2\,l_p$.

3. **Causal partition.** $\Gamma$ is partitioned into a visible sector $\Gamma_V$ and hidden sector $\Gamma_H$:

$$\Gamma = \Gamma_V \times \Gamma_H, \qquad H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

Cross-partition correlations enter only through $H_{\text{int}}$. The product decomposition is idealized; §4 and §9.7 address approximation quality and the conditions under which the sharp partition is exact.

4. **Classical probability.** The observer's predictions are classical expectation values over phase space; standard probability theory applies.

These axioms contain no quantum postulates. The claim is that quantum mechanics *emerges* under the conditions below.

### 1.3 Conditions on the Hidden Sector

**(C1) Non-zero coupling.** $H_{\text{int}} \neq 0$. The coupling is bidirectional.

**(C2) Slow-bath timescale separation.** The visible-sector (system) timescale $\tau_S$ is much shorter than the hidden-sector (bath) timescale $\tau_B$: $\tau_S \ll \tau_B$ — the *inverse* of the Markovian regime. The hidden sector evolves on timescales far exceeding those accessible to the observer.

**(C3) Sufficient capacity.** The number of hidden-sector degrees of freedom $N_H$ exceeds the number of visible-sector degrees of freedom $N_V$ by enough that visible-sector interactions do not appreciably perturb the hidden sector's state on timescales $\ll \tau_B$.

**Theorem statement.** Under Axioms 1–4 and (C1)–(C3), the embedded observer's reduced description is mathematically equivalent to unitarily evolving quantum mechanics. The conditions are not merely sufficient but *necessary* (§3.3), establishing full equivalence.

### 1.4 Partition-Relativity

**Lemma.** *The emergent description is uniquely determined by the partition. Any parameters of the emergent theory depend only on the geometric and thermodynamic properties of the partition boundary.*

*Proof.* By Axiom 1, the Hamiltonian flow $\phi_t$ is unique. By Axiom 3, the partition is fixed. By Axiom 4, the observer uses the Liouville measure $\mu$ — the unique absolutely continuous measure preserved by $\phi_t$ (any other smooth measure would evolve, introducing dependence on an arbitrary reference time; singular invariant measures are excluded by Axiom 4). Letting $\pi_V$ denote projection onto the visible sector, the marginalized transition probabilities

$$T_{ij}(t_2, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu(h)$$

are therefore uniquely determined by three inputs: dynamics ($\phi_t$), partition ($\Gamma_V, \Gamma_H$), and measure ($\mu$). Since $\phi_t$ and $\mu$ are fixed by the axioms, the stochastic process — and hence any emergent quantum description (§3.1) — depends only on the partition. $\square$

---

## 2. EMERGENT STOCHASTICITY AND P-INDIVISIBILITY

### 2.1 Emergent Stochasticity

The total system evolves deterministically, but the visible sector alone is stochastic. The observer knows $x$ but not $h$; different hidden states $h_k$ compatible with the same $x$ send it to different futures $x'_k$. Transition probabilities are obtained by marginalizing over the Liouville measure (§1.4). This makes the framework a hidden variable theory; consistency with Bell's theorem is addressed in §3.2.

### 2.2 The Slow-Bath Regime

The Markovian limit requires $\tau_B \ll \tau_S$ [4]. Condition (C2) inverts this: $\tau_S \ll \tau_B$. A slow bath must be distinguished from a static field. By (C1), coupling is continuously active: each visible-sector transition imprints on the hidden sector. Because the hidden sector is slow (not static), imprints persist without thermal overwriting. On subsequent transitions, coupling reads back stored correlations, producing history-dependent transition probabilities — the non-Markovian regime [4].

### 2.3 P-Indivisibility

By Axiom 2, the visible and hidden sectors have finite configuration spaces $\mathcal{C}_V$ and $\mathcal{C}_H$ (the discrete counterparts of $\Gamma_V$ and $\Gamma_H$). On these finite sets:

**Theorem.** *Let $\mathcal{C}_V$ and $\mathcal{C}_H$ be finite sets with $|\mathcal{C}_V| \geq 2$, and let $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ be a bijection. Define:*

$$T_{ij} = \frac{|\{h \in \mathcal{C}_H : \pi_V(\varphi(x_i, h)) = x_j\}|}{|\mathcal{C}_H|}$$

*and the $k$-step matrix $T^{(k)}_{ij}$ by applying $\varphi^k$. If $T$ is not a permutation matrix, then the process is P-indivisible.*

*Proof.* Uses total variation distance $d(p, q) = \frac{1}{2}\sum_k |p_k - q_k|$. P-divisibility $\iff$ $d(p(t), q(t))$ non-increasing for all initial $p, q$ [6, 7].

*Step 1 (Recurrence).* $\varphi$ bijective on a finite set $\Rightarrow$ $\exists N: \varphi^N = \text{id}$. Thus $T^{(N)} = I$ and $d(\delta_i T^{(N)}, \delta_j T^{(N)}) = 1$ for $i \neq j$.

*Step 2 (Strict contraction).* $T$ not a permutation $\Rightarrow$ $\exists i, j, l$: $T_{il} > 0$ and $T_{jl} > 0$. Then:

$$d(\delta_i T, \delta_j T) = \frac{1}{2}\sum_k |T_{ik} - T_{jk}| < 1$$

*Step 3.* $d(\delta_i T^{(1)}, \delta_j T^{(1)}) < 1 = d(\delta_i T^{(N)}, \delta_j T^{(N)})$: non-monotonic, hence P-indivisible. $\square$

The theorem requires only bijective dynamics (Axiom 1) and non-trivial coupling (C1). Axiom 2 guarantees the finite configuration space.

**Convergence with prior work.** The theorem converges with independent results: Pechukas [5] (reduced dynamics need not preserve positivity), Rivas et al. [6, 7] (divisibility failure ↔ information backflow), Pollock et al. [8] (process-tensor Markovianity conditions), and Strasberg and Esposito [9] (non-Markovian reduced dynamics in the slow-bath regime of C2). Bylicka, Johansson, and Acín [34] prove that for bijective dynamical maps — the class generated here — CP-divisibility and information backflow are equivalent, so the P-indivisibility established above implies CP-indivisibility directly. Milz et al. [35] further show that even CP-divisibility does not guarantee Markovianity in the process-tensor sense, confirming that the non-Markovian character identified here is robust under all current definitions.

**Continuous-time extension.** The Hamiltonian flow on finite-dimensional phase space preserves Liouville measure on compact energy surfaces. $T_{ij}(t)$ is continuous with $T(0) = I$. By (C1), $T(t)$ departs from the permutation class for $t > 0$. By Poincaré recurrence, $\exists t_R$: the set of hidden states with $\pi_V(\varphi_{t_R}(x_i, h)) = x_i$ has measure $> 1 - \delta$ for any $\delta > 0$. For small $\delta$, this gives non-monotonic trace distance, establishing P-indivisibility in continuous time.

**Role of (C2) and (C3).** P-indivisibility follows from (C1) and finiteness alone. (C2) ensures information backflow occurs on accessible timescales (not just Poincaré recurrence times). (C3) ensures P-indivisibility persists at scale: insufficient capacity causes saturation and effectively Markovian crossover. Together they guarantee P-indivisibility is strong, persistent, and observationally relevant.

**Weak-coupling and fast-bath regimes.** Known P-divisible systems with non-zero coupling illustrate the necessity of (C2), not a failure of the theorem. The Jaynes-Cummings model with Lorentzian spectral density is P-divisible when dissipation dominates coupling — the fast-bath regime ($\tau_B \ll \tau_S$), violating (C2). The Davies-Merkli Markovian convergence theorem likewise applies in the Born-Markov (fast-bath) limit. The §3.3 necessity proof for (C2) establishes this formally.

### 2.4 Explicit Construction: A Minimal Model

Visible sector: $x \in \{0, 1\}$. Hidden sector: $h \in \{1, \ldots, 6\}$. Dynamics: the permutation

$$\sigma = (0{,}1 \leftrightarrow 1{,}1)\;(0{,}2 \leftrightarrow 1{,}2)\;(0{,}3 \leftrightarrow 0{,}4)\;(0{,}5 \leftrightarrow 0{,}6)\;(1{,}3 \leftrightarrow 1{,}4)\;(1{,}5 \leftrightarrow 1{,}6)$$

satisfying (C1)–(C3). Since $\sigma^2 = \text{id}$: at $t = 1$, two of six hidden states flip $x$, giving

$$T(1,0) = \begin{pmatrix} 2/3 & 1/3 \\ 1/3 & 2/3 \end{pmatrix}$$

At $t = 2$ ($\sigma^2 = \text{id}$): $T(2,0) = I$. A Markov chain would predict continued mixing: $T(1,0)^2 = \left(\begin{smallmatrix} 5/9 & 4/9 \\ 4/9 & 5/9 \end{smallmatrix}\right)$. The actual dynamics show complete *un-mixing*. Computing the intermediate propagator:

$$\Lambda(2,1) = T(2,0) \cdot [T(1,0)]^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

Negative entries — no valid stochastic matrix exists. **P-indivisible.** $\square$

**The mechanism.** The hidden sector acts as a memory register. The transpositions $(0,h) \leftrightarrow (1,h)$ for $h \in \{1, 2\}$ flip $x$ while preserving $h$, so a state at $x = 1$ with $h \in \{1, 2\}$ after step 1 carries the record "I was at $x = 0$." Step 2 reads this record and flips $x$ back — information backflow impossible for a memoryless process. The cosmological realization has $\tau_S/\tau_B \sim 10^{-32}$; P-indivisibility is more extreme, not less, when memory is more persistent.

---

## 3. THE EMERGENCE OF QUANTUM MECHANICS

### 3.1 The Stochastic-Quantum Correspondence

By Barandes' correspondence [10, 11], any P-indivisible stochastic process on a finite configuration space of size $n$ embeds into a unitarily evolving quantum system on $\mathcal{H}$ of dimension $\leq n^3$. P-indivisible transition matrices develop negative entries at fine time resolution; the Stinespring dilation theorem guarantees $\exists$ a Hilbert space and unitary $U(t)$ with $T_{ij}(t) = |U_{ij}(t)|^2$ — transition probabilities are exactly Born-rule probabilities. The proof requires a finite-dimensional configuration space (Axiom 2); Calvo [12] extends the correspondence to infinite dimensions, but this is not required here. An independent derivation using only Stinespring's dilation theorem [32] and standard partial-trace properties [33] is given in Appendix A; either route alone suffices.

**From phase space to configuration space.** The transition probabilities $T_{ij}$ are projections of the full phase-space flow onto the configuration sector of $\Gamma_V$, with momenta and hidden-sector degrees of freedom absorbed into the Liouville marginalization. The resulting process lives on the discrete configuration space of Axiom 2.

Three features emerge. The Schrödinger equation arises from the differentiability of $U(t)$. The Born rule is the equilibrium distribution of the indivisible process [10, 11]. The action scale $\hbar$ enters when defining $\hat{H}(t) \equiv i\hbar \, \partial_t U \cdot U^\dagger$, converting dimensionless rates to energy units; its value requires physical input from the partition (§5).

**Phase uniqueness from continuous-time data.** The relation $T_{ij}(t) = |U_{ij}(t)|^2$ discards phase information at any single time. Doukas [26] identifies this gap for discrete-time data. The resolution: continuous-time data $\{T_{ij}(t)\}_{t \in \mathbb{R}}$ provides strictly more information.

**Lemma (phase-locking).** *Let $H$ be Hermitian on $\mathbb{C}^n$ with eigenbasis $\{|k\rangle\}$, eigenvalues $\{E_k\}$, and $V_{ik} = \langle i | k \rangle$. Assume: (G1) non-degenerate spectrum; (G2) non-degenerate energy gaps; (G3) $V_{ik} \neq 0$ for all $i, k$. Then $T_{ij}(t) = |\langle i | e^{-iHt} | j \rangle|^2$ for all $i, j, t$ uniquely determines $H$ up to an overall energy shift and basis phase conventions.*

*Proof.* Write:

$$T_{ij}(t) = \sum_{k,l} V_{ik}\, V_{jk}^*\, V_{jl}\, V_{il}^*\; e^{-i(E_k - E_l)t}$$

By (G2), the frequencies $\omega_{kl} = E_k - E_l$ are distinct for distinct pairs with $k \neq l$. Fourier-transforming yields:

$$a_{ij}^{kl} = V_{ik}\, V_{jk}^*\, V_{jl}\, V_{il}^*$$

The moduli $|V_{ik}|$ follow from $a_{ii}^{kl} = |V_{ik}|^2 |V_{il}|^2$ (non-zero by (G3)). The phases carry a double-difference structure:

$$\arg(a_{ij}^{kl}) = (\varphi_{ik} - \varphi_{il}) - (\varphi_{jk} - \varphi_{jl})$$

The gauge freedom preserving all double differences is $\varphi_{ik} \to \varphi_{ik} + \alpha_i + \beta_k$ (physically irrelevant basis rephasing). Fixing $\varphi_{1k} = 0$, $\varphi_{i1} = 0$, each remaining phase is $\varphi_{ik} = \arg(a_{i1}^{k1})$, directly extracted from Fourier data. $H = V \, \text{diag}(E_k) \, V^\dagger$ is unique up to energy shift and phase conventions. $\square$

Conditions (G1)–(G3) fail only on a measure-zero set of Hamiltonians.

### 3.2 Bell Inequality Violations

The framework is a hidden variable theory evading Bell's theorem [13] not by superdeterminism but by violating factorizability through P-indivisible joint dynamics — while remaining causally local. Two subsystems interacting at preparation carry a joint transition matrix $T_{QR} \neq T_Q \otimes T_R$. This non-factorizability *is* stochastic entanglement [10, 11, 14]. Since the process is indivisible, no well-defined intermediate conditional probabilities permit Bell's factorization.

In the Jarrett decomposition, the framework violates outcome independence while preserving parameter independence and measurement independence — precisely the class Fine's theorem [24] permits. Barandes, Hasan, and Kagan [14] prove the maximum CHSH correlator is exactly Tsirelson's bound $2\sqrt{2}$, with independent support from Le et al. [15]. The bound also follows from the Stinespring route: Appendix A establishes full unitary QM on a tensor-product Hilbert space, from which Tsirelson's original operator-norm argument [36] yields $|\langle S \rangle| \leq 2\sqrt{2}$; achievability follows because all quantum states, including maximally entangled ones, are realizable in the emergent description.

**Fine-tuning and causal structure.** The framework does not claim to restore Bell locality: outcome independence is genuinely violated. What it provides is a *derivation* of this nonlocality from the causal partition, rather than treating it as axiomatic. The fine-tuning objection (Wood and Spekkens, 2015) — that classical causal models reproducing Bell violations require parameter adjustment — assumes DAG causal structure with Markov factorization. P-indivisible processes violate the Markov condition on any DAG; the appropriate framework is the process tensor [8], within which no-signaling follows from the marginalization structure without fine-tuning. The OI violation saturates Tsirelson's bound, consistent with recent results excluding partial OI relaxation.

### 3.3 The Characterization Theorem: Necessity of the Conditions

The logical structure: Barandes' correspondence gives QM $\iff$ P-indivisibility. What remains is P-indivisibility $\implies$ embedded observation under (C1)–(C3).

**Dilation existence.** Any stochastic process on a finite configuration space can be realized as marginalization of a deterministic process on a larger state space — furnishing Axioms 1–4.

**Theorem (C1 equivalence).** *The marginalized process is P-indivisible iff $T$ is not a permutation matrix.*

*Proof.* Forward: §2.3. Reverse: if $T$ is a permutation, $\Lambda(k_2, k_1) = T^{(k_2-k_1)}$ is a valid stochastic matrix for all $k_2 > k_1$ $\Rightarrow$ P-divisible. $\square$

**Theorem (C2 necessity).** *In the fast-bath regime ($\tau_B \ll \tau_S$), ergodic mixing drives the hidden sector to uniformity before each coupling event, yielding a Markov chain ($T^{(k)} = T^k$), which is P-divisible. Contrapositively, P-indivisibility requires $\tau_S \ll \tau_B$.*

*Proof.* Between coupling events (separated by $\tau_S$), the hidden sector evolves under its own Hamiltonian $H_H$. Let $\mathcal{L}_H$ denote the hidden-sector Liouvillian with spectral gap $\Delta > 0$ (guaranteed on a finite ergodic system). For any conditioned hidden-sector distribution $\mu_H(\cdot | x_i)$ at a coupling event:

$$\| e^{\mathcal{L}_H \tau_S} \mu_H(\cdot | x_i) - \mu_{\text{eq}} \|_{\text{TV}} \leq C \, e^{-\Delta \tau_S}$$

In the fast-bath regime ($\Delta \tau_S \gg 1$), this is exponentially small: the hidden sector relaxes to equilibrium $\mu_{\text{eq}}$ before each coupling event regardless of its post-coupling state. Each single-step transition matrix $T$ is therefore computed against the same equilibrium distribution, so $T^{(k)} = T^k$ — a homogeneous Markov chain, hence P-divisible.

Contrapositively: P-indivisibility requires $\Delta \tau_S \lesssim 1$, i.e., $\tau_S \lesssim \tau_B$. For the strong, persistent P-indivisibility of the characterization theorem, the separation must be $\tau_S \ll \tau_B$. $\square$

**Theorem (C3 necessity).** *Let $m = |\mathcal{C}_H|$. The non-Markovian mutual information satisfies:*

$$I(X_{<t} ; X_{>t} \mid X_t) \leq \log_2 m$$

*Proof.* The total system is deterministic: $X_{>t}$ is a function of $(X_t, H_t)$. Conditioning on $X_t$: $X_{<t} \to H_t \to X_{>t}$ is a Markov chain. By data processing:

$$I(X_{<t} ; X_{>t} \mid X_t) \leq I(X_{<t} ; H_t \mid X_t) \leq H(H_t \mid X_t) \leq \log_2 m \quad \square$$

**Corollary.** P-indivisibility across $n$ visible configurations requires $m \geq n$, and persistence over $K$ transitions requires $m/n$ growing with the observation window — precisely (C3). $\square$

**Characterization theorem.** *For $|\mathcal{C}_V| \geq 2$, the following are equivalent:*

*(i) $\mathcal{S}$ is mathematically equivalent to unitarily evolving QM [10, 11].*

*(ii) $\mathcal{S}$ is P-indivisible.*

*(iii) $\mathcal{S}$ arises from marginalizing a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$ with (C1) non-trivial coupling, (C2) slow-bath memory, and (C3) sufficient capacity.*

*Proof.* (i) $\iff$ (ii): Barandes [10, 11]. (iii) $\implies$ (ii): §2.3. (ii) $\implies$ (iii): necessity theorems above. $\square$

QM is not merely *compatible with* embedded observation — it is *equivalent to* it.

---

# PART II: THE COSMOLOGICAL APPLICATION

## 4. THE COSMOLOGICAL HORIZON AS CAUSAL PARTITION

### 4.1 The Partition

The cosmological horizon — the boundary beyond which no signal propagating at or below $c$ can reach the observer — implements the causal partition of Axiom 3 for all sub-$c$ observers: $\Gamma_V$ is the interior, $\Gamma_H$ everything beyond. This is a consequence of GR's causal structure, not a modeling choice. A hypothetical observer with access to a causal channel not constrained by the light cone would have a different partition, a different (or absent) hidden sector, and by the theorem's own logic, a different emergent description. No such channel is available within GR. The specific quantum mechanics observed is the quantum mechanics of light-cone-bounded observers; its universality is a consequence of the causal structure, not a postulate.

Different observers have different horizon areas (hence different $S_{\text{dS}}$), but $\hbar = c^3 \epsilon^2/(4G)$ depends only on local geometric quantities — not on the observer's worldline or horizon area — so all observers share the same emergent action scale.

### 4.2 Verification of the Conditions

**(C1)** Stress-energy conservation enforces dynamical correlations across the horizon. "Bidirectional" refers not to signal propagation (forbidden by the causal structure) but to the gravitational constraint equations: the Hamiltonian and momentum constraints on any Cauchy surface couple interior and exterior data, so $H_{\text{tot}} \neq H_V + H_H$. **Satisfied.**

**(C2)** $\tau_B \gtrsim 1/H \sim 10^{17}$ s; for laboratory processes, $\tau_S \sim 10^{-15}$ s. Ratio: $\tau_S / \tau_B \sim 10^{-32}$. **Satisfied.**

**(C3)** Hidden sector has $A/\epsilon^2$ modes with $A \sim 10^{52}$ m$^2$; visible sector has $\sim 10^{80}$ baryons. No laboratory process saturates the hidden sector. **Satisfied.**

### 4.3 Application

Axiom 2 is now a consequence of partition geometry: the horizon has finite area $A = 4\pi c^2/H^2$, bounding coupled modes to $A/\epsilon^2 < \infty$. The Part I theorem applies: the observer's reduced description is P-indivisible and, by Barandes' correspondence, equivalent to unitary QM with $\hbar$ determined by the partition boundary.

---

## 5. DERIVATION OF THE EMERGENT ACTION SCALE ($\hbar$)

### 5.1 The Classical Horizon Temperature

Jacobson [16] showed $dE = T\,dS$ applied to local causal horizons yields Einstein's equations, with $dE = (c^2 \kappa / 8\pi G)\,dA$, where $\kappa$ is the surface gravity of the horizon. The entropy density is $\eta = 1/\epsilon^2$ (one DOF per minimal cell), so $dS = dA/\epsilon^2$. Equating:

$$T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G k_B}$$

For de Sitter ($\kappa = cH$): $k_B T_{\text{cl}} = c^3 \epsilon^2 H / (8\pi G)$. No $\hbar$ appears.

### 5.2 The Emergent Action Scale

**Step 1: Uniqueness.** By partition-relativity (§1.4), $\hbar$ is derived, not free.

**Step 2: $\hbar$ is structural, not volumetric.** Deep hidden-sector modes influence the boundary only by propagating through the hidden sector, taking time $\gtrsim \tau_B$. On observable timescales ($t \ll \tau_B$), transition probabilities depend only on boundary modes: decomposing $\mathcal{C}_H = \mathcal{C}_B \times \mathcal{C}_D$, the indicator in $T_{ij}(t)$ is independent of deep modes $h_D$, so $T_{ij}(t) = T^{(B)}_{ij}(t)$. Corrections are $\delta \lesssim t/\tau_B \sim 10^{-32}$.

**Step 3: Dimensional determination.** With volumetric quantities excluded, the partition-intrinsic quantities are $c$, $G$, $\epsilon$. The unique combination with dimensions of action:

$$\hbar = \beta \frac{c^3 \epsilon^2}{G}$$

**Step 4: Thermal self-consistency.** Before the trace-out: $k_B T_{\text{cl}} = c^3 \epsilon^2 \kappa / (8\pi G)$. After: the emergent QFT predicts the Gibbons-Hawking temperature [17]: $k_B T_{\text{GH}} = \hbar \kappa / (2\pi c)$. These describe the same boundary; self-consistency requires $T_{\text{cl}} = T_{\text{GH}}$:

$$\frac{c^3 \epsilon^2 H}{8\pi G} = \frac{\hbar H}{2\pi}$$

$H$ cancels (confirming structural/volumetric distinction). Solving:

$$\boxed{\hbar = \frac{c^3 \epsilon^2}{4G}}$$

**Why not circular.** The derivation is a gap equation: $\epsilon$ is the free geometric input, $\hbar$ is the output. $T_{\text{cl}}(\epsilon)$ contains no $\hbar$; $T_{\text{GH}}(\hbar)$ is the emergent QFT's prediction with $\hbar$ unknown; matching the two solves for $\hbar$. The result $\epsilon = 2\,l_p$ restates the output in conventional units. Jacobson's original derivation [16] uses $\hbar$-containing forms; this paper does not — it uses the classical identity $dE = (c^2 \kappa / 8\pi G)\,dA$ and the classical entropy density $\eta = 1/\epsilon^2$. The $\hbar$-containing formulas are *recovered* after the matching.

**Robustness.** The result can be derived without the Gibbons-Hawking formula: C1–C3 ensure persistent thermal contact, and the zeroth law gives $T_Q = T_{\text{cl}}$ exactly; the Gibbons-Hawking formula is then *recovered* as a prediction. Lattice corrections are $\mathcal{O}((\epsilon H/c)^2) \sim 10^{-122}$, consistent with trans-Planckian insensitivity [28, 29].

### 5.3 Gauge-Fixing and the Dimensional Obstruction

**Theorem (D-gauge completeness).** *Let $U(t) = e^{-iHt}$ with non-degenerate eigenvalues and non-vanishing configuration-basis overlaps. If $|U'_{ij}(t)|^2 = |U_{ij}(t)|^2$ for all $i, j, t$, then $H' = DHD^\dagger$ for a time-independent diagonal unitary $D$.*

*Proof.* Write $U_{ij}(t) = \sum_a V_{ia} \, e^{-iE_a t} \, V_{ja}^*$ with $V_{ia} = \langle i | a \rangle$ and eigenvalues $\{E_a\}$, and similarly $U'_{ij}(t) = \sum_a V'_{ia} \, e^{-iE'_a t} \, V'^*_{ja}$.

*Step 1 (Eigenvalue recovery).* By the phase-locking argument of §3.1, $|U_{ij}(t)|^2 = |U'_{ij}(t)|^2$ for all $t$ implies, via Fourier analysis, that the frequency sets $\{E_a - E_b\}$ and $\{E'_a - E'_b\}$ coincide. Non-degeneracy of energy gaps then gives $E'_a = E_{\sigma(a)} + E_0$ for some permutation $\sigma$ and global shift $E_0$. The Fourier coefficients $a^{kl}_{ij} = V_{ik} V^*_{jk} V_{jl} V^*_{il}$ must match between primed and unprimed, which (by the non-vanishing condition on overlaps) forces $\sigma = \text{id}$ up to relabeling. Thus $E'_a = E_a + E_0$.

*Step 2 (Modulus recovery).* From the diagonal Fourier coefficients $a^{kl}_{ii} = |V_{ik}|^2 |V_{il}|^2$, the non-vanishing condition gives $|V'_{ia}| = |V_{ia}|$ for all $i, a$.

*Step 3 (Phase structure).* Write $V'_{ia} = V_{ia} \, e^{i\delta_{ia}}$. The off-diagonal Fourier coefficients require:

$$V'_{ik} V'^*_{jk} V'_{jl} V'^*_{il} = V_{ik} V^*_{jk} V_{jl} V^*_{il}$$

Substituting and canceling moduli:

$$e^{i(\delta_{ik} - \delta_{jk} - \delta_{il} + \delta_{jl})} = 1 \quad \text{for all } i, j, k, l$$

This is the double-difference condition: $\delta_{ik} - \delta_{il} - \delta_{jk} + \delta_{jl} = 0 \pmod{2\pi}$. The general solution on the integer lattice is $\delta_{ia} = \alpha_i + \beta_a$ for phases $\{\alpha_i\}$, $\{\beta_a\}$. Thus $V' = D_\alpha \, V \, D_\beta$ where $D_\alpha = \text{diag}(e^{i\alpha_i})$ and $D_\beta = \text{diag}(e^{i\beta_a})$. The $D_\beta$ factor is absorbed into the eigenvector phase convention (physically irrelevant), giving $H' = D_\alpha H D_\alpha^\dagger$ with $D = D_\alpha$ a time-independent diagonal unitary. $\square$

The D-gauge is physically trivial (basis rephasing). Cross-interval transition probabilities fix the relative gauge up to a single global phase; in the continuum limit this becomes an unobservable smooth function $e^{i\theta(t)}$.

**Dimensional obstruction.** The unitary $U(t)$ is dimensionless; $\hbar$ enters only via $\hat{H} = i\hbar \, \partial_t U \cdot U^\dagger$. No dimensionless data can fix a dimensionful constant — Step 4's thermal self-consistency provides the necessary dimensionful input.

---

## 6. SELF-CONSISTENCY AND THE DISCRETENESS SCALE

Rearranging $\hbar = c^3 \epsilon^2 / (4G)$:

$$\epsilon^2 = \frac{4\hbar G}{c^3} = 4\,l_p^2$$

The framework yields $\epsilon = 2\,l_p$ exactly. This is algebraically equivalent to the formula for $\hbar$ but serves as a consistency check: the discreteness scale lands at the Planck scale, the only self-consistent regime. If $\epsilon^2 \ll l_p^2$, sub-Planckian subcells would be dynamically active yet unresolvable by the emergent description, creating a second trace-out with its own noise intensity and breaking the single-valuedness of $\hbar$. If $\epsilon^2 \gg l_p^2$, the emergent description would assign distinct quantum states to configurations that are physically identical in the substratum. Thermal self-consistency selects $\epsilon = 2\,l_p$ within this regime.

With $\epsilon = 2\,l_p$, the number of independent modes on the cosmological horizon is:

$$N_{\text{modes}} = \frac{A}{\epsilon^2} = \frac{A}{4\,l_p^2} = S_{\text{dS}}$$

where $S_{\text{dS}} = A/(4\,l_p^2)$ is the Bekenstein-Hawking entropy of the de Sitter horizon. The factor of $1/4$ in the Bekenstein-Hawking formula — historically introduced as a proportionality constant — is here derived: each minimal cell of area $\epsilon^2 = 4\,l_p^2$ on the horizon contributes one unit of entropy, and $A / (4\,l_p^2) = A / \epsilon^2$ recovers the standard formula exactly.

---

## 7. DISSOLUTION OF THE COSMOLOGICAL CONSTANT PROBLEM

### 7.1 The Two Levels of Description

**From finite-dimensional QM to QFT.** Part I delivers QM on a finite-dimensional Hilbert space. The $N = A/\epsilon^2$ cells discretize the visible sector; spatial locality of the classical substratum restricts which cells interact on any given timescale. The emergent Hilbert space decomposes as $\mathcal{H} = \bigotimes_k \mathcal{H}_k$ — a lattice-regularized QFT with UV cutoff at $\epsilon = 2\,l_p$.

**Locality preservation theorem.** *If the classical Hamiltonian is spatially local (couples only neighbors), then the emergent quantum Hamiltonian inherits spatial locality.*

*Proof.* For infinitesimal $dt$ and $x' \neq x$: $T_{x,x'}(dt) = |\langle x'|\hat{H}|x\rangle|^2\,dt^2 + O(dt^3)$. If $x, x'$ differ at non-neighboring sites, spatial locality of the classical dynamics gives $T_{x,x'}(dt) = 0$ at leading order, hence $\langle x'|\hat{H}|x\rangle = 0$. The emergent Hamiltonian has the form $\hat{H} = \sum_k \hat{h}_k + \sum_{\langle k,l\rangle} \hat{h}_{kl}$. $\square$

**Classical substratum** (what geometric measurements probe): The horizon has classical thermal equilibrium. By the Friedmann equation, $\rho_{\text{crit}} = 3H^2 c^2/(8\pi G)$. No zero-point energy, no discrepancy. Total vacuum energy density: $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$ — precisely observed.

**Emergent QFT** (what local quantum measurements probe): Zero-point energy $\frac{1}{2}\hbar\omega$ per mode summed to the Planck cutoff gives $\rho_{\text{QFT}} \sim 10^{113}$ J/m$^3$ — a $\sim 10^{122}$ discrepancy with the observed value [2, 3, 18].

### 7.2 Why Gravity Sees the Classical Value

Spacetime geometry is part of the classical substratum (Axiom 3): the metric evolves via Einstein's equations *before* the trace-out. The stress-energy sourcing gravity is the classical stress-energy of the total microstate, not the expectation value of an emergent quantum operator. The semiclassical equation $G_{\mu\nu} = 8\pi G \langle \hat{T}_{\mu\nu} \rangle$ is itself an emergent approximation; at the classical level, the gravitational field equations never encounter the zero-point sum.

**Ontological commitment.** Classical spacetime is fundamental; QM is emergent. This follows from the derivation's logic: the causal partition is defined by null geodesics of the metric (§4.1), so the metric must exist prior to the partition and hence prior to the quantum description. Reversing this ordering makes the partition definition circular. Any framework in which QM is logically prior to the metric must treat the zero-point sum as a gravitational source — producing the $10^{122}$ discrepancy requiring cancellation or fine-tuning. In the present framework, the zero-point sum is an artifact of the emergent description and never enters the stress-energy tensor. Supersymmetric cancellations are increasingly constrained by LHC null results, and anthropic arguments constrain the range without predicting the observed value; the present framework predicts $\rho \sim H^2/G$ and identifies the discrepancy as $S_{\text{dS}}$. This does not prove the ordering correct — the GW echo prediction (§8.2) provides a more direct test — but it constitutes existing empirical evidence for geometry-first.

**Quantum corrections to gravity.** The emergent quantum description does feed back into gravitational dynamics through state-level quantities: §8.1 derives dark energy evolution because the emergent vacuum energy depends on $H$ through the hidden sector's volume. What the framework excludes is the zero-point sum — a property of the correspondence itself rather than of any particular state — as a gravitational source. The structural/volumetric distinction of §5.2 applies: $\hbar$ (structural) does not gravitate; the vacuum energy (volumetric, state-dependent) does, but at the classical scale $\rho \sim H^2/G$ rather than $\rho \sim M_{\text{Pl}}^4$.

### 7.3 The Structural Origin of the $10^{122}$ Discrepancy

$\rho_{\text{QFT}} / \rho_{\text{classical}} \sim M_{\text{Pl}}^4 / (H^2/G) = S_{\text{dS}} = A/(4\,l_p^2)$ — the Bekenstein-Hawking entropy, now identified as the information compression ratio of the trace-out. The "worst prediction in physics" is the entropy of the observer's blind spot — a category error, not a fine-tuning failure. Wolpert's limits of inference [19] confirm this cannot be resolved from within: both geometric and quantum measurements are faithful to their respective descriptions, and no embedded observer can determine which is more fundamental. This is not a prediction awaiting future data — the observed vacuum energy sits at the classical geometric scale $\rho \sim H^2/G$, the value the framework expects.

---

## 8. PREDICTIONS AND TESTS

### 8.1 Dark Energy Evolution in Running Vacuum Form

$\hbar$ is $H$-independent (§5.2), but the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume. Expanding $\Lambda_{\text{eff}}(H)$:

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu_{\text{OI}}}{8\pi G}(H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

This is the Running Vacuum Model [20, 21]. The $S_{\text{dS}}$ horizon modes span frequencies $\omega_{\text{IR}} = H$ to $\omega_{\text{UV}} = c/\epsilon$. For conformal fields, the spectral density is uniform in $\ln\omega$, so the number of independent spectral channels is $\mathcal{N}(H) = \ln(c/\epsilon H)$. Each carries fraction $1/\mathcal{N}$ of the total gravitating vacuum energy, so $\rho_\Lambda \propto 1/\mathcal{N}$. Taylor-expanding:

$$\boxed{\nu_{\text{OI}} = \frac{\Omega_\Lambda}{2\,\ln(c/\epsilon H_0)}}$$

With $\epsilon = 2\,l_p$, $H_0 = 67.4$ km/s/Mpc, $\Omega_\Lambda = 0.685$: $\nu_{\text{OI}} = (2.45 \pm 0.03) \times 10^{-3}$. Independently testable ratio: $\nu_{\text{OI}} / \Omega_\Lambda \approx 0.00358$.

DESI data [22, 30] report evolving dark energy at $2.8\sigma$–$4.2\sigma$. RVM fits [31] find $\nu \sim \mathcal{O}(10^{-3})$ with $\nu = 0$ disfavored at $2.7\sigma$–$3.1\sigma$, consistent with the prediction.

### 8.2 Gravitational Wave Echoes

A black hole horizon represents a regime where the causal partition differs from the cosmological one: degrees of freedom reclassify from visible to hidden sector as they cross the horizon, shifting the effective partition and the emergent description.

At proper distance $\sim \epsilon$ outside a black hole horizon $r_h$, an infalling mode reaches the discreteness floor and must scatter back. The predicted time delay is:

$$\Delta t_{\text{echo}} \approx \frac{r_h}{c} \ln\left(\frac{r_h}{2\,l_p}\right)$$

For a $30 M_\odot$ remnant, logarithmic dependence on $\epsilon$ makes this robust ($\sim 0.1$ ms shift within the $\sim 54$ ms timescale [23]). Detection would constitute direct evidence that $\epsilon$ has observable consequences at horizons other than the cosmological one — a regime where partition-relativity (§9.2) becomes empirically accessible. Joint confirmation of dark energy evolution *and* GW echoes would uniquely favor an information-theoretic origin, since standard RVMs predict $\Lambda(H)$ running but have no mechanism for discreteness-scale echoes.

---

## 9. DISCUSSION

### 9.1 Interpretive Consequences

In the cosmological application, the hidden sector is the trans-horizon region; the degrees of freedom involved in quantum experiments — photons, electrons, slits, detectors — are all visible-sector objects. Their quantum behavior is a downstream consequence of the single cosmological trace-out: the emergent quantum mechanics, once established by the theorem, governs all visible-sector dynamics.

In the double-slit experiment, the particle traverses a single slit in the deterministic substratum. The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events. A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms. In Wigner's friend, the Friend has a definite outcome; Wigner's superposition reflects his epistemic deficit. The Everettian measure problem dissolves: the system evolves as a single reality; "branches" are features of the compressed description. The Born rule, often treated as an independent postulate, is derived: it is the equilibrium distribution of the indivisible stochastic process (§3.1), not an additional assumption.

### 9.2 Scope

The characterization theorem is a full equivalence: QM $\iff$ embedded observation under (C1)–(C3). The theorem does not identify which physical systems satisfy the conditions (empirical) nor derive $\hbar$ for specific systems (requires Part II). Universality in our universe follows from the shared causal partition defined by null geodesics.

### 9.3 The Stochastic-Quantum Bridge

The bridge from P-indivisible stochastic dynamics to unitary quantum mechanics is established by two independent routes. The primary route uses Barandes' stochastic-quantum correspondence [10, 11], which is bidirectional and exact, peer-reviewed, and independently corroborated [12, 25, 26]. Appendix A provides an independent derivation using only Stinespring's dilation theorem [32] and the complete positivity of partial-trace channels [33] — textbook results requiring no material more recent than 2000. The two routes yield identical physical predictions (Appendix A, Table 1). Partition-relativity, emergent stochasticity, and P-indivisibility (§§1.4, 2) invoke neither.

### 9.4 The Status of the Discreteness Scale

$\epsilon$ does not smuggle in a quantum assumption. Axiom 2 requires finite-dimensionality, motivated by the classical fact that finite-area boundaries admit finitely many modes. The result $\epsilon = 2\,l_p$ is a *consequence* of self-consistency (§6). Holographic entropy bounds [27] provide independent, non-quantum motivation.

### 9.5 Vacuum Energy: Relative Effects and the Higgs Potential

**Relative effects.** Casimir forces and Lamb shifts are predictions *within* the emergent QFT — relative effects depending on energy differences between configurations. The framework denies that the *absolute* zero-point sum gravitates, because gravity operates at the logically prior classical level (§7.2).

**The Higgs potential.** The strongest CC objection is not the zero-point sum but the electroweak Higgs potential: symmetry breaking shifts $V(\phi)$ by $\sim (200\;\text{GeV})^4$, exceeding the observed $\Lambda$ by $\sim 55$ orders of magnitude. The framework's response follows from its ontological ordering: the Higgs field, like all quantum fields, is part of the emergent description (§7.1). The classical substratum has deterministic dynamics on a finite configuration space; the degrees of freedom that the emergent theory organizes as a scalar field with spontaneous symmetry breaking have a non-field-theoretic character in the substratum. The vacuum energy shift is therefore a property of the emergent ground state — the same category as the zero-point sum. The dissolution applies uniformly: if QM is emergent, then so is the Higgs mechanism and its vacuum energy.

### 9.6 Relation to Prior Work

**'t Hooft [1]:** Differs in mechanism (epistemic trace-out vs. information loss), generality (any system satisfying axioms vs. particular rules), and Bell placement (outcome independence violation vs. superdeterminism). **QBism/relational QM:** Share observer-relative epistemic states; this framework provides a structural *why* and quantitative predictions. **Jacobson [16]:** Derives gravity from thermodynamics; this framework derives QM from causal structure — complementary, with mutual consistency as a check.

**AdS/CFT and the geometry-entanglement connection.** The most developed challenge to the framework's ordering comes from holographic physics: the Ryu-Takayanagi formula, Van Raamsdonk's disconnection argument, the ER=EPR conjecture, and "it from qubit" programs all suggest entanglement is prior to geometry.

The framework offers an alternative reading of each result. The Ryu-Takayanagi formula equates entanglement entropy with extremal surface area. In the present framework, tracing out across a geometric boundary produces entanglement entropy proportional to boundary area ($A/\epsilon^2$ modes), so the area-entropy relation is a consequence of geometry assembling entanglement, not the reverse. For this reading to hold, the proportionality constant must follow from the partition structure — and it does: §6 derives the $1/4$ factor from $\epsilon = 2\,l_p$, yielding $S = A/(4\,l_p^2)$ without assuming the Ryu-Takayanagi formula.

Van Raamsdonk's disconnection argument — that reducing entanglement between CFT subsystems disconnects the dual geometry — similarly admits reversal: changing the partition geometry changes the emergent entanglement. The question is which direction carries the explanatory weight. In the holographic context, the boundary CFT observer is *external* to the bulk, immune to the inferential limits of embedded observers [19]; the framework does not claim to reproduce the specific form of holographic results in that setting.

The key point of contact is empirical. Entanglement-first programs predict spacetime breakdown at low entanglement or high energy. This framework predicts QM breakdown near $\epsilon = 2\,l_p$ while the geometric substratum persists (§8). The CC dissolution (§7.2) provides a concrete test: the geometry-first ordering predicts $\rho \sim H^2/G$ without fine-tuning, while entanglement-first orderings inherit the zero-point sum as a gravitational source.

Witten's Type II algebra program achieves finite entropy without finite-dimensional Hilbert spaces; this is compatible, since the framework's predictions depend on finite entropy (the physical content of Axiom 2), not on dimensional finiteness per se.

### 9.7 Assumptions, Limitations, and Falsifiability

**The theorem** requires Axiom 2 (independent in Part I; consequence of geometry in Part II), the stochastic-quantum bridge (§9.3; established by two independent routes), and genericity conditions (non-degenerate spectrum, non-vanishing overlaps), which hold for all but a measure-zero set.

**The sharp partition.** Axiom 3's product decomposition idealizes what is in general graded epistemic access. The axiom requires that the physics admits a sharp partition with cross-partition correlations entering only through $H_{\text{int}}$ — a condition on the boundary, not the observer. It is satisfied when a physical boundary enforces a separation sharp enough that residual leakage is absorbed into the interaction term. The cosmological horizon (§4) provides an exact realization; for other systems, the approximation quality determines the fidelity of the emergent quantum description.

**Planck-scale ordering.** The classical-prior ontology may break down at $l_p$, where "geometric" and "quantum" lose operational distinction. If a deeper theory unifies both, this framework describes the effective macroscopic regime.

**Falsifiability.** The *theorem* would be falsified by a failure of both the stochastic-quantum correspondence and the Stinespring construction for the class of processes generated here — a possibility excluded by the independent proofs in §3.1 and Appendix A. The *application* would be falsified by definitive absence of dark energy evolution or GW echoes at the predicted timescale.

---

## 10. CONCLUSION

**The general theorem (Part I).** Under four axioms and conditions (C1)–(C3), the P-indivisibility of reduced dynamics is proved: any bijective dynamics on a finite system with non-trivial coupling necessarily produces P-indivisible stochastic dynamics. By the stochastic-quantum correspondence, the observer's description is necessarily quantum mechanics. Continuous-time transition data resolves all gauge freedom. The Schrödinger equation, Born rule, and Bell violations are structural consequences. The characterization theorem establishes that the conditions are necessary: QM and embedded observation under (C1)–(C3) are equivalent.

**The cosmological application (Part II).** The cosmological horizon provides a realization where the sharp-partition approximation is exact and all conditions hold. The theorem yields: (a) $\hbar = c^3 \epsilon^2 / (4G)$ with $\epsilon = 2\,l_p$ and the Bekenstein-Hawking formula as consequences; (b) dissolution of the CC problem — the $10^{122}$ discrepancy is $S_{\text{dS}}$, the compression ratio of the observer's quantum description; and (c) falsifiable predictions including RVM dark energy with $\nu_{\text{OI}} \approx 2.45 \times 10^{-3}$ and gravitational wave echoes.

The apparent conflict between quantum mechanics and general relativity is the information-theoretic cost of observing the universe from within.

---

## ACKNOWLEDGEMENTS

During the preparation of this work, the author used Claude Opus 4.6 (Anthropic) and Gemini 3.1 Pro (Google) to assist in drafting, refining argumentation, and verifying bibliographic details. The author reviewed and edited all content and takes full responsibility for the publication.

---

## REFERENCES
[1] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).
[2] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).
[3] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).
[4] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).
[5] P. Pechukas, "Reduced dynamics need not be completely positive," *Phys. Rev. Lett.* **73**, 1060 (1994).
[6] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Entanglement and non-Markovianity of quantum evolutions," *Phys. Rev. Lett.* **105**, 050403 (2010).
[7] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014).
[8] F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, and K. Modi, "Operational Markov condition for quantum processes," *Phys. Rev. Lett.* **120**, 040405 (2018).
[9] P. Strasberg and M. Esposito, "Stochastic thermodynamics in the strong coupling regime: An unambiguous approach based on coarse graining," *Phys. Rev. E* **95**, 062101 (2017).
[10] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).
[11] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).
[12] S. Calvo, "On the Stochastic-Quantum Correspondence," arXiv:2601.18720 (2026).
[13] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195–200 (1964).
[14] J. A. Barandes, S. Hasan, and J. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).
[15] T. Le, F. A. Pollock, T. Paterek, M. Paternostro, and K. Modi, "Divisible quantum dynamics satisfies temporal Tsirelson's bound," *J. Phys. A* **50**, 055302 (2017).
[16] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995).
[17] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).
[18] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).
[19] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008).
[20] J. Solà Peracaula, "The cosmological constant problem and running vacuum in the expanding universe," *Phil. Trans. R. Soc. A* **380**, 20210182 (2022).
[21] J. Solà Peracaula, A. Gómez-Valent, and J. de Cruz Pérez, "Running vacuum in the Universe," *Universe* **9**, 262 (2023).
[22] DESI Collaboration, "DESI 2024 VI: Cosmological Constraints from BAO," arXiv:2404.03002 (2024).
[23] J. Abedi, H. Dykaar, and N. Afshordi, "Echoes from the Abyss," *Phys. Rev. D* **96**, 082004 (2017).
[24] A. Fine, "Hidden Variables, Joint Probability, and the Bell Inequalities," *Phys. Rev. Lett.* **48**, 291 (1982).
[25] L. S. Pimenta, "Divisible and indivisible Stochastic-Quantum dynamics," arXiv:2505.08785 (2025).
[26] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095 (2026).
[27] N. Bao, S. M. Carroll, and A. Singh, "The Hilbert space of quantum gravity is locally finite-dimensional," *Int. J. Mod. Phys. D* **26**, 1743013 (2017).
[28] W. G. Unruh, "Sonic analogue of black holes and the effects of high frequencies on black hole evaporation," *Phys. Rev. D* **51**, 2827 (1995).
[29] K. Fredenhagen and R. Haag, "On the derivation of Hawking radiation associated with the formation of a black hole," *Commun. Math. Phys.* **127**, 273–284 (1990).
[30] DESI Collaboration, "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," *Phys. Rev. D* **112**, 083515 (2025); arXiv:2503.14738.
[31] J. de Cruz Pérez, A. Gómez-Valent, and J. Solà Peracaula, "Dynamical Dark Energy models in light of the latest observations," arXiv:2512.20616 (2025).
[32] W. F. Stinespring, "Positive functions on C*-algebras," *Proc. Amer. Math. Soc.* **6**, 211–216 (1955).
[33] M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000).
[34] B. Bylicka, M. Johansson, and A. Acín, "Constructive method for detecting the information backflow of non-Markovian dynamics," *Phys. Rev. Lett.* **118**, 120501 (2017).
[35] S. Milz, M. S. Kim, F. A. Pollock, and K. Modi, "Completely positive divisibility does not mean Markovianity," *Phys. Rev. Lett.* **123**, 040401 (2019).
[36] B. S. Cirel'son, "Quantum generalizations of Bell's inequality," *Lett. Math. Phys.* **4**, 93–100 (1980).

---

## APPENDIX A: INDEPENDENT DERIVATION VIA STINESPRING DILATION

This appendix derives the emergent quantum description using only Stinespring's dilation theorem [32] and standard properties of the partial trace [33], without invoking the stochastic-quantum correspondence [10, 11]. The two routes are logically independent; either alone suffices.

### A.1 Setup

The finite configuration spaces $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ and $\mathcal{C}_H = \{h_1, \ldots, h_m\}$ (Axiom 2) embed into Hilbert spaces $\mathcal{H}_V = \mathbb{C}^n$ and $\mathcal{H}_H = \mathbb{C}^m$ via $|i\rangle \leftrightarrow x_i$ and $|k\rangle \leftrightarrow h_k$. This introduces no quantum postulates: it is the canonical identification of probability distributions on a finite set with diagonal density matrices.

### A.2 Permutation Unitarity

**Lemma A.1.** *Any bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ defines a unitary $U_\varphi$ on $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$.*

*Proof.* Define $U_\varphi |i, k\rangle = |\varphi(x_i, h_k)\rangle$. Since $\varphi$ is a bijection, $U_\varphi$ permutes the orthonormal basis, hence is unitary. $\square$

For continuous-time dynamics $\varphi_t$, Stone's theorem on $\mathcal{H}$ yields $U_t = e^{-i\hat{H}t}$ for Hermitian $\hat{H}$.

### A.3 The Quantum Channel

The observer's ignorance of the hidden sector (Axioms 3–4) corresponds to $\rho_H = I_m/m$. The visible-sector quantum channel is

$$\Phi(\rho_V) = \mathrm{Tr}_H\!\left[U_\varphi\,(\rho_V \otimes \rho_H)\,U_\varphi^\dagger\right]$$

This is CPTP by a standard result [33, Theorem 8.1], with Kraus representation $\Phi(\rho_V) = \sum_{k,l} K_{kl}\,\rho_V\,K_{kl}^\dagger$ where $K_{kl} = m^{-1/2}\langle l|U_\varphi|k\rangle_H$. The triple $(\mathcal{H}_H, U_\varphi, \rho_H)$ is the Stinespring dilation [32] of $\Phi$.

### A.4 Born Rule Recovery

**Theorem A.2.** *The classical transition probabilities $T_{ij}$ (§1.4) equal the Born-rule probabilities of $\Phi$.*

*Proof.* $P(j|i) = \langle j|\Phi(|i\rangle\langle i|)|j\rangle = m^{-1}\sum_{k,l} |\langle j,l|U_\varphi|i,k\rangle|^2$. Since $U_\varphi$ is a permutation, $\langle j,l|U_\varphi|i,k\rangle = \delta_{(j,l),\varphi(i,k)}$. Thus $P(j|i) = m^{-1}\sum_k \delta_{j,\pi_V(\varphi(x_i,h_k))} = T_{ij}$. $\square$

### A.5 Emergent Coherence

**Theorem A.3.** *If $T$ is not a permutation matrix (condition (C1)), then $\Phi$ generates genuine quantum coherence: it is not entanglement-breaking.*

*Proof.* If $T$ is not a permutation, some initial state $|i\rangle$ maps to at least two distinct outputs, so $\Phi(|i\rangle\langle i|)$ has rank $\geq 2$. By linearity, $\Phi$ maps some off-diagonal input $|i\rangle\langle j|$ to a non-zero operator, precluding the measure-and-prepare form of entanglement-breaking channels. $\square$

### A.6 CP-Indivisibility

**Theorem A.4.** *The P-indivisibility of §2.3 implies CP-indivisibility of $\{\Phi_t\}$: there exist $t_2 > t_1 > 0$ with no CPTP map $\Lambda$ satisfying $\Phi_{t_2} = \Lambda \circ \Phi_{t_1}$.*

*Proof.* CP-divisibility restricted to diagonal inputs reduces to P-divisibility. The contrapositive gives the result. $\square$

By the Breuer-Laine-Piilo criterion [4, 6], CP-indivisibility implies non-monotonic trace distance (information backflow) — the quantum signature of non-Markovianity.

### A.7 Approximate Unitarity

On observable timescales $t \ll \tau_B$, the hidden-sector state is approximately frozen (conditions (C2)–(C3)). The channel generator decomposes as $d\Phi_t/dt|_{t=0}(\rho_V) = -i[\hat{H}_{\text{eff}}, \rho_V] + \mathcal{D}(\rho_V)$ with $\mathcal{D} \sim \mathcal{O}(\tau_S/\tau_B)$. The leading-order dynamics is the Schrödinger equation. The phase-locking lemma (§3.1) and D-gauge theorem (§5.3) then determine $\hat{H}_{\text{eff}}$ uniquely from continuous-time transition data.

### A.8 Comparison of Routes

| | Barandes route (§3.1) | Stinespring route (this appendix) |
|---|---|---|
| Input | P-indivisible process on $\mathcal{C}_V$ | Bijection on $\mathcal{C}_V \times \mathcal{C}_H$ + marginalization |
| Bridge | Stochastic-quantum correspondence [10, 11] | Stinespring dilation [32] + partial trace [33] |
| Output | Unitary with $T_{ij} = \|U_{ij}\|^2$ | CPTP channel with $T_{ij} = \langle j\|\Phi(\|i\rangle\langle i\|)\|j\rangle$ |
| Born rule | Equilibrium of indivisible process | Partial trace structure (Theorem A.2) |
| Scope | Any P-indivisible process | Processes from marginalized bijections |

The Barandes route is more general; the Stinespring route requires only textbook results [32, 33] predating 2000. Together they establish that the bridge is overdetermined.
