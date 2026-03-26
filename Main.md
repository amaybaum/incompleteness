# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

An observer embedded in a deterministic universe cannot access the complete state. We prove that any such observer — coupled to a slow, high-capacity hidden sector on a finite-dimensional configuration space — must describe the visible sector using P-indivisible stochastic dynamics, mathematically equivalent to unitary quantum mechanics. The converse also holds: any quantum system, realized as a deterministic dilation, requires non-trivial coupling, slow-bath memory, and sufficient hidden-sector capacity. The Schrödinger equation, Born rule, and Bell violations emerge as structural consequences requiring no independent quantum postulates.

Applied to the cosmological horizon, the framework uniquely determines $\hbar = c^3 \epsilon^2 / (4G)$, fixes $\epsilon = 2\,l_p$, and recovers the Bekenstein-Hawking entropy $S = A/(4\,l_p^2)$. The $10^{122}$ cosmological constant discrepancy is identified as $S_{\text{dS}}$, the information compression ratio of the emergent quantum description; the observed vacuum energy is the mandatory classical baseline. Falsifiable predictions include dark energy evolution in Running Vacuum Model form with $\nu_{\text{OI}} \approx 2.45 \times 10^{-3}$ (systematic range $2.2$–$2.7 \times 10^{-3}$), consistent with current DESI data, and gravitational wave echoes near black hole horizons. The trace-out that produces QM simultaneously renders ~95% of the universe's gravitational budget invisible to the emergent description — matching the observed dark sector — providing independent corroboration of observational incompleteness.

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

2. **Finiteness.** The effective configuration space of the visible sector is finite-dimensional, with a discreteness scale $\epsilon$ providing a finite minimal cell volume. Any observer bounded by a finite-area surface can couple to only finitely many modes across that boundary; independent support comes from holographic entropy bounds [27]. In Part I, $\epsilon$ is free; self-consistency (§6) pins $\epsilon = 2\,l_p$. The boundary-only dependence lemma (§5.2) shows that the cardinality of the deep hidden sector — beyond the boundary layer — is gauge: no observable depends on it.

3. **Causal partition.** $\Gamma$ is partitioned into a visible sector $\Gamma_V$ and hidden sector $\Gamma_H$:

$$\Gamma = \Gamma_V \times \Gamma_H, \qquad H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

Cross-partition correlations enter only through $H_{\text{int}}$. The product decomposition is idealized; §4 and §9.6 address approximation quality and the conditions under which the sharp partition is exact.

4. **Classical probability.** The observer's predictions are classical expectation values over phase space; standard probability theory applies.

These axioms contain no quantum postulates. The claim is that quantum mechanics *emerges* under the conditions below.

### 1.3 Conditions on the Hidden Sector

**(C1) Non-zero coupling.** $H_{\text{int}} \neq 0$. The coupling is bidirectional.

**(C2) Slow-bath timescale separation.** The visible-sector (system) timescale $\tau_S$ is much shorter than the hidden-sector (bath) timescale $\tau_B$: $\tau_S \ll \tau_B$ — the *inverse* of the Markovian regime. The hidden sector evolves on timescales far exceeding those accessible to the observer.

**(C3) Sufficient capacity.** The number of hidden-sector degrees of freedom $N_H$ exceeds the number of visible-sector degrees of freedom $N_V$ by enough that visible-sector interactions do not appreciably perturb the hidden sector's state on timescales $\ll \tau_B$.

**Theorem statement.** Under Axioms 1–4 and (C1)–(C3), the embedded observer's reduced description is mathematically equivalent to unitarily evolving quantum mechanics (defined precisely in §3.3). The conditions are not merely sufficient but *necessary* (§3.3), establishing full equivalence.

### 1.4 Partition-Relativity

**Lemma.** *The emergent description is uniquely determined by the partition. Any parameters of the emergent theory depend only on the geometric and thermodynamic properties of the partition boundary.*

*Proof.* By Axiom 1, the Hamiltonian flow $\phi_t$ is unique. By Axiom 3, the partition is fixed. By Axiom 4, the observer uses the Liouville measure $\mu$ — the unique absolutely continuous invariant measure on the full phase space. (An embedded observer with incomplete knowledge of the total energy averages over energies with a smooth prior, recovering Liouville on a phase-space band; singular invariant measures are excluded by Axiom 4.) Letting $\pi_V$ denote projection onto the visible sector, the marginalized transition probabilities

$$T_{ij}(t_2, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu(h)$$

are therefore uniquely determined by three inputs: dynamics ($\phi_t$), partition ($\Gamma_V, \Gamma_H$), and measure ($\mu$). Since $\phi_t$ and $\mu$ are fixed by the axioms, the stochastic process — and hence any emergent quantum description (§3.1) — depends only on the partition. $\square$

### 1.5 Epistemic Status of the Results

**Tier 1 (from axioms alone):** P-indivisibility (§2.3), the characterization theorem (§3.3), partition-relativity (§1.4), the deep-sector gauge corollary (§5.2), nested trace-out consistency (Appendix B, B.1–B.4), the generalized second law (B.6), and the Page curve (B.7–B.9). **Tier 2 (given the cosmological realization):** The gap equation $\hbar = c^3 \epsilon^2 / (4G)$ (§5.2), the Bekenstein-Hawking entropy (§6), the CC dissolution (§7), and $a_0 = cH/6$ with $v^4 = GM_B \cdot cH/6$ (§8.4). **Tier 3 (consistency checks):** The dark-sector concordance (§8.3), $\nu_{\text{OI}}$ (§8.1), GW echoes (§8.2), and the interpolation steepness (§8.4).

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

The theorem converges with independent results on reduced dynamics [5–9] and is robust under all current non-Markovianity definitions: Bylicka et al. [34] prove CP-indivisibility for bijective maps; Milz et al. [35] confirm that even CP-divisibility does not guarantee Markovianity.

**Continuous-time extension.** $T_{ij}(t)$ is continuous with $T(0) = I$. By (C1), $T(t)$ departs from the permutation class for $t > 0$. By Poincaré recurrence, $T(t_R) \approx I$ for some $t_R$, giving non-monotonic trace distance. The following lemma shows that under (C2), information backflow occurs on observable timescales.

**Lemma (Accessible-timescale backflow).** *Under (C1)–(C3) with $\tau_S \ll \tau_B$, the non-Markovian mutual information $I(X_{<t}; X_{>t} \mid X_t)$ is $\mathcal{O}(1)$ for observation windows $t \sim k\tau_S$ with $k\tau_S \ll \tau_B$.*

*Proof.* Each coupling event transfers $I_0 > 0$ bits to the hidden sector (C1). Between events, correlations decay as $e^{-\Delta \tau_S}$ where $\Delta \sim 1/\tau_B$ is the hidden-sector spectral gap. For $\tau_S \ll \tau_B$: $\Delta \tau_S \ll 1$, so correlations survive each step intact. After $k$ transitions:

$$I(X_{<t}; X_{>t} \mid X_t) \geq I_0\left(1 - \frac{k\tau_S}{\tau_B}\right)$$

For $k\tau_S \ll \tau_B$, this remains $\mathcal{O}(I_0)$. The bound saturates (C3): persistent backflow over $K$ transitions requires hidden-sector capacity $m \geq 2^K$, amply satisfied when $N_H \gg N_V$. $\square$

**Role of (C2) and (C3).** The Poincaré recurrence argument and the accessible-timescale lemma are independent: the former establishes P-indivisibility from (C1) and finiteness alone; the latter shows that (C2) and (C3) promote it from a formal property to an observationally dominant one.

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

By Barandes' correspondence [10, 11], any P-indivisible stochastic process on a finite configuration space of size $n$ embeds into a unitarily evolving quantum system on $\mathcal{H}$ of dimension $\leq n^3$. P-indivisible transition matrices develop negative entries at fine time resolution; the Stinespring dilation theorem guarantees $\exists$ a Hilbert space and unitary $U(t)$ with $T_{ij}(t) = |U_{ij}(t)|^2$ — transition probabilities are exactly Born-rule probabilities. The proof requires a finite-dimensional configuration space (Axiom 2); Calvo [12] extends the correspondence to infinite dimensions, but this is not required here. Pimenta [25] distinguishes P-divisible and P-indivisible stochastic-quantum dynamics: the correspondence is non-trivial only in the P-indivisible regime, which is precisely the regime produced by §2.3. An independent derivation using only Stinespring's dilation theorem [32] and standard partial-trace properties [33] is given in Appendix A; either route alone suffices.

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

Conditions (G1)–(G3) fail only on a measure-zero set. For the cosmological realization, the partition boundary breaks translational and boost invariance, generically lifting degeneracies in $\hat{H}_{\text{eff}}$.

### 3.2 Bell Inequality Violations

The framework is a hidden variable theory evading Bell's theorem [13] not by superdeterminism but by violating factorizability through P-indivisible joint dynamics — while remaining causally local. Two subsystems interacting at preparation carry a joint transition matrix $T_{QR} \neq T_Q \otimes T_R$. This non-factorizability *is* stochastic entanglement [10, 11, 14]. Since the process is indivisible, no well-defined intermediate conditional probabilities permit Bell's factorization.

In the Jarrett decomposition, the framework violates outcome independence while preserving parameter independence and measurement independence — precisely the class Fine's theorem [24] permits. Barandes, Hasan, and Kagan [14] prove the maximum CHSH correlator is exactly Tsirelson's bound $2\sqrt{2}$, with independent support from Le et al. [15]. The bound also follows from the Stinespring route: Appendix A establishes full unitary QM on a tensor-product Hilbert space, from which Tsirelson's original operator-norm argument [36] yields $|\langle S \rangle| \leq 2\sqrt{2}$; achievability follows because all quantum states, including maximally entangled ones, are realizable in the emergent description.

**Causal structure.** The framework violates outcome independence, not Bell locality. The fine-tuning objection (Wood-Spekkens) assumes DAG causal structure; P-indivisible processes violate the Markov condition on any DAG, so the appropriate framework is the process tensor [8], within which no-signaling follows from marginalization structure without fine-tuning. Parameter independence holds structurally: for space-like separated subsystems with disjoint coupling neighborhoods, the spatial Markov property gives $P(x_B \mid a, b) = P(x_B \mid b)$ for all bounded-degree graph topologies with range-1 coupling.

### 3.3 The Characterization Theorem: Necessity of the Conditions

The logical structure: Barandes' correspondence gives QM $\iff$ P-indivisibility. What remains is P-indivisibility $\implies$ embedded observation under (C1)–(C3).

**Dilation existence.** Any stochastic process on a finite configuration space can be realized as marginalization of a deterministic process on a larger state space — furnishing Axioms 1–4.

**Theorem (C1 equivalence).** *The marginalized process is P-indivisible iff $T$ is not a permutation matrix.*

*Proof.* Forward: §2.3. Reverse: if $T$ is a permutation, $\Lambda(k_2, k_1) = T^{(k_2-k_1)}$ is a valid stochastic matrix for all $k_2 > k_1$ $\Rightarrow$ P-divisible. $\square$

**Theorem (C2 necessity).** *In the fast-bath regime ($\tau_B \ll \tau_S$), the hidden sector relaxes to equilibrium before each coupling event, yielding a homogeneous Markov chain, which is P-divisible. Contrapositively, P-indivisibility requires $\tau_S \ll \tau_B$.*

*Proof.* The hidden-sector Liouvillian has spectral gap $\Delta \sim 1/\tau_B$. For $\Delta \tau_S \gg 1$ (fast bath), any conditioned distribution $\mu_H(\cdot | x_i)$ satisfies $\| e^{\mathcal{L}_H \tau_S} \mu_H - \mu_{\text{eq}} \|_{\text{TV}} \leq C e^{-\Delta \tau_S} \ll 1$: the hidden sector equilibrates between coupling events. Each transition is computed against the same $\mu_{\text{eq}}$, so $T^{(k)} = T^k$ — P-divisible. Contrapositively, P-indivisibility requires $\Delta \tau_S \lesssim 1$, i.e., $\tau_S \lesssim \tau_B$. $\square$

**Theorem (C3 necessity).** *Let $m = |\mathcal{C}_H|$. The non-Markovian mutual information satisfies:*

$$I(X_{<t} ; X_{>t} \mid X_t) \leq \log_2 m$$

*Proof.* The total system is deterministic: $X_{>t}$ is a function of $(X_t, H_t)$. Conditioning on $X_t$: $X_{<t} \to H_t \to X_{>t}$ is a Markov chain. By data processing:

$$I(X_{<t} ; X_{>t} \mid X_t) \leq I(X_{<t} ; H_t \mid X_t) \leq H(H_t \mid X_t) \leq \log_2 m \quad \square$$

**Corollary.** P-indivisibility across $n$ visible configurations requires $m \geq n$, and persistence over $K$ transitions requires $m/n$ growing with the observation window — precisely (C3). $\square$

**Definition (unitarily evolving QM).** A stochastic process $\mathcal{S}$ on a finite configuration space $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ is *mathematically equivalent to unitarily evolving quantum mechanics* if there exists a Hilbert space $\mathcal{H}_V$ of dimension $\leq n^3$, a Hermitian operator $\hat{H}$ on $\mathcal{H}_V$, and a unitary family $U(t) = e^{-i\hat{H}t}$ such that $T_{ij}(t) = |U_{ij}(t)|^2$ for all $i, j, t$ — i.e., transition probabilities are exactly Born-rule probabilities. This definition captures the Hilbert space, unitary dynamics, and the Born rule. Additional quantum-mechanical structures — the tensor product decomposition for spatially separated visible-sector subsystems, state update, and the measurement formalism — are addressed in the remarks following the theorem.

**Characterization theorem.** *For $|\mathcal{C}_V| \geq 2$, the following are equivalent:*

*(i) $\mathcal{S}$ is mathematically equivalent to unitarily evolving QM (in the sense of the preceding definition).*

*(ii) $\mathcal{S}$ is P-indivisible.*

*(iii) $\mathcal{S}$ arises from marginalizing a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$ with (C1) non-trivial coupling, (C2) slow-bath memory, and (C3) sufficient capacity.*

*Proof.* (i) $\iff$ (ii): Barandes [10, 11]. (iii) $\implies$ (ii): §2.3. (ii) $\implies$ (iii): necessity theorems above. $\square$

QM is not merely *compatible with* embedded observation — it is *equivalent to* it.

**Remark (scope of the equivalence).** The characterization theorem establishes the Hilbert space, unitary dynamics, and Born-rule transition probabilities. Four further structures of operational quantum mechanics merit comment.

*(i) Tensor product structure (visible–hidden).* The Stinespring route (Appendix A) constructs $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$ and derives the CPTP channel $\Phi$ by partial trace. The visible–hidden tensor product is therefore given by the construction, not postulated.

*(ii) Tensor product structure (visible-sector subsystems).* Spatially separated subsystems within the visible sector — e.g., two laboratories — correspond to subsets $V_A, V_B \subset V$ with disjoint coupling neighborhoods on the coupling graph. If the classical Hamiltonian has range-1 coupling, the spatial Markov property guarantees conditional independence: $\rho_{AB} = \rho_A \otimes \rho_B$ conditioned on boundary data. The emergent Hilbert space inherits the factorization $\mathcal{H}_{V_A} \otimes \mathcal{H}_{V_B}$ from the locality of the coupling graph, with entanglement between $A$ and $B$ arising from shared boundary history — precisely the stochastic entanglement of [10, 14].

*(iii) State update, measurement, and multi-time predictions.* Projective measurement in the emergent description corresponds to conditioning on a visible-sector outcome and re-marginalizing over the hidden sector. The Lüders rule $\rho \to P_k \rho P_k / \text{Tr}(P_k \rho)$ is the quantum transcription of Bayesian updating on the classical substratum (Axiom 4). No independent measurement postulate is required. Multi-time correlation functions, weak values, and Leggett-Garg inequalities are standard calculations within the delivered formalism ($\mathcal{H}_V$, $U(t)$, Born rule); they require no additional postulates beyond what the characterization theorem provides.

---

# PART II: THE COSMOLOGICAL APPLICATION

## 4. THE COSMOLOGICAL HORIZON AS CAUSAL PARTITION

### 4.1 The Partition

The cosmological horizon — the boundary beyond which no signal propagating at or below $c$ can reach the observer — implements the causal partition of Axiom 3: $\Gamma_V$ is the interior, $\Gamma_H$ everything beyond. This is a consequence of GR's causal structure, not a modeling choice. The universality of the observed quantum mechanics follows from all sub-$c$ observers sharing the same causal structure.

Different observers have different horizon areas (hence different $S_{\text{dS}}$), but $\hbar = c^3 \epsilon^2/(4G)$ depends only on local geometric quantities — not on the observer's worldline or horizon area — so all observers share the same emergent action scale.

### 4.2 Verification of the Conditions

**(C1)** In the ADM formulation, the bulk Hamiltonian is a sum of constraints that vanish on-shell; physical time evolution is generated by the boundary term at the horizon, which depends on data from both sides. The Hamiltonian and momentum constraints further correlate interior and exterior initial data on any Cauchy surface, so the physical phase space is a constraint surface within the kinematic product $\Gamma_V \times \Gamma_H$ (see §9.6 for implications). This is *stronger* than the $H_{\text{int}} \neq 0$ required by Axiom 3: constraints enforce correlations that persist on all timescales and cannot be perturbatively removed. **Satisfied.**

**(C2)** $\tau_B \gtrsim 1/H \sim 10^{17}$ s; for laboratory processes, $\tau_S \sim 10^{-15}$ s. Ratio: $\tau_S / \tau_B \sim 10^{-32}$. **Satisfied.**

**(C3)** Hidden sector has $A/\epsilon^2$ modes with $A \sim 10^{52}$ m$^2$; visible sector has $\sim 10^{80}$ baryons. No laboratory process saturates the hidden sector. **Satisfied.**

### 4.3 Application

Axiom 2 is now a consequence of partition geometry: the horizon has finite area $A = 4\pi c^2/H^2$, bounding coupled modes to $A/\epsilon^2 < \infty$. The Part I theorem applies: the observer's reduced description is P-indivisible and, by Barandes' correspondence, equivalent to unitary QM with $\hbar$ determined by the partition boundary.

---

## 5. DERIVATION OF THE EMERGENT ACTION SCALE ($\hbar$)

### 5.1 The Classical Horizon Temperature

Jacobson [16] showed $dE = T\,dS$ applied to local causal horizons yields Einstein's equations, with $dE = (c^2 \kappa / 8\pi G)\,dA$, where $\kappa$ is the surface gravity of the horizon. The entropy density is $\eta = 1/\epsilon^2$ — one coupled mode per minimal cell. This is not an assumption about the number of states per cell but a consequence of two results: $\epsilon$ is defined as the minimal distinguishable scale (Axiom 2), so each cell of area $\epsilon^2$ contributes exactly one boundary mode that couples across the partition; the number of internal states per mode (the alphabet size $q$) is a gauge freedom: all emergent transition probabilities, the dispersion relation, and the gap equation are $q$-independent for any $q \geq 2$, so no experiment can measure $q$. Thus $dS = dA/\epsilon^2$. Equating:

$$T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G k_B}$$

For de Sitter ($\kappa = cH$): $k_B T_{\text{cl}} = c^3 \epsilon^2 H / (8\pi G)$. No $\hbar$ appears.

### 5.2 The Emergent Action Scale

**Step 1: Uniqueness.** By partition-relativity (§1.4), $\hbar$ is derived, not free.

**Step 2: $\hbar$ is structural, not volumetric.**

**Lemma (Boundary-only dependence).** *Decompose the hidden sector as $\mathcal{C}_H = \mathcal{C}_B \times \mathcal{C}_D$, where $\mathcal{C}_B$ denotes boundary modes and $\mathcal{C}_D$ denotes deep modes. If the classical Hamiltonian is spatially local, then on timescales $t \ll \tau_B$:*

$$T_{ij}(t) = T^{(B)}_{ij}(t) + \mathcal{O}(t/\tau_B)$$

*where $T^{(B)}_{ij}$ depends only on the $V$-$B$ dynamics.*

*Proof.* (i) *Coupling structure.* Spatial locality gives a coupling chain $V \leftrightarrow B \leftrightarrow D$ with no direct $V$-$D$ coupling.

(ii) *Frozen deep sector.* The deep sector's spectral gap $\Delta_D \sim 1/\tau_B$ implies $\|\varphi_t^D - \text{id}\| = \mathcal{O}(t/\tau_B)$ for $t \ll \tau_B$: the deep sector is frozen.

(iii) *Factorization.* The visible-sector output $\pi_V(\varphi_t(x_i, b, d))$ depends on $d$ only through $\mathcal{O}(t/\tau_B)$ back-reaction on $b$. The $d$-sum contributes $|\mathcal{C}_D|$ identical terms at leading order, yielding $T^{(B)}_{ij}(t) = |\mathcal{C}_B|^{-1} \sum_b \delta_{x_j}[\pi_V(\varphi_t^{VB}(x_i, b))]$, independent of $|\mathcal{C}_D|$. $\square$

The correction is $\mathcal{O}(t/\tau_B) \sim 10^{-32}$ for laboratory processes. Since $T^{(B)}_{ij}(t)$ depends only on the boundary geometry ($A$, $\epsilon$, $\kappa$) and the constants $c$, $G$, the emergent action scale $\hbar$ inherits boundary-only dependence.

**Corollary (deep-sector cardinality is gauge).** *No observable of the emergent description — no transition probability, emergent Hamiltonian eigenvalue, or scattering amplitude — depends on the cardinality $|\mathcal{C}_D|$ of the deep hidden sector. Systems with the same $\mathcal{C}_V \times \mathcal{C}_B$ dynamics produce the same emergent physics to within $\mathcal{O}(\tau_S/\tau_B)$, whether $|\mathcal{C}_D|$ is finite, countably infinite, or uncountably infinite.*

*Proof.* $T^{(B)}_{ij}(t)$ is defined by a sum over $\mathcal{C}_B$ alone. The $\mathcal{C}_D$-dependent terms enter only through the $\mathcal{O}(t/\tau_B)$ back-reaction. Since the emergent Hamiltonian $\hat{H}_{\text{eff}}$ is uniquely determined by $\{T_{ij}(t)\}$ (phase-locking lemma, §3.1; D-gauge theorem, §5.3), it inherits $\mathcal{C}_D$-independence at leading order. All observables — eigenvalues, transition amplitudes, scattering cross-sections — are functions of $\hat{H}_{\text{eff}}$ and therefore $\mathcal{C}_D$-independent. $\square$

The cardinality of the deep hidden sector is gauge: just as two systems with different alphabet sizes $q$ produce the same emergent transition probabilities (because all predictions are $q$-independent), two systems with different $|\mathcal{C}_D|$ are physically equivalent if they share the same $\mathcal{C}_V \times \mathcal{C}_B$ dynamics. Axiom 2 requires $S$ finite for the recurrence proof (§2.3); the corollary establishes that the deep sector's contribution to this finiteness has no observable consequences. The question "is the universe finite or infinite?" has no empirical content within the framework — it is identified as gauge.

**Step 3: Dimensional determination.** Step 2 excludes volumetric (deep-sector) quantities, leaving boundary quantities. The boundary carries both *local* geometric data ($\epsilon$, $\kappa$, and the constants $c$, $G$ of the classical Hamiltonian) and a *global* quantity: the total area $A$, which forms the dimensionless ratio $A/\epsilon^2 = S_{\text{dS}}$. If $\hbar$ depended on $S_{\text{dS}}$, it would be observer-dependent — different observers have different horizon areas (§4.1) — contradicting the universality of the emergent action scale. (All sub-$c$ observers share the same local physics and hence the same $\hbar$; §4.1.) This excludes $A$, leaving the local boundary quantities $c$, $G$, $\epsilon$, and $\kappa$. Since $\kappa$ is the surface gravity of a specific horizon (observer-dependent, like $A$), it too is excluded. The unique combination of $c$, $G$, $\epsilon$ with dimensions of action:

$$\hbar = \beta \frac{c^3 \epsilon^2}{G}$$

**Step 4: Thermal self-consistency.** The classical substratum assigns the partition boundary a temperature $k_B T_{\text{cl}} = c^3 \epsilon^2 \kappa / (8\pi G)$ (§5.1), containing no $\hbar$. The emergent QFT of Part I lives on this classical background, which has a bifurcate Killing horizon with surface gravity $\kappa$. Regularity of the Wick-rotated metric at the horizon requires Euclidean period $\beta = 2\pi c / \kappa$; any QFT on this background — including a lattice-regularized one — must therefore be periodic in imaginary time with the same period, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$, with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import. The two temperatures are computed independently — $T_{\text{cl}}$ from the classical substratum alone (no QM), $T_Q$ from the emergent QFT alone (no classical substratum details) — but they describe the same physical degrees of freedom: the boundary modes across which the partition is defined. Since the quantum description is derived from the classical one (Part I), and the derivation is exact at the boundary (Step 2's correction is $\mathcal{O}(\tau_S/\tau_B) \sim 10^{-32}$), the two descriptions cannot assign contradictory temperatures to the same boundary. Consistency requires $T_{\text{cl}} = T_Q$:

$$\frac{c^3 \epsilon^2 \kappa}{8\pi G} = \frac{\hbar \kappa}{2\pi c}$$

$\kappa$ cancels (confirming the structural/volumetric distinction). Solving:

$$\boxed{\hbar = \frac{c^3 \epsilon^2}{4G}}$$

The derivation is a gap equation: $\epsilon$ is the free geometric input, $\hbar$ is the output. The match is non-trivial: $T_{\text{cl}}$ could have depended on volumetric hidden-sector data (excluded by Step 2), or $T_Q$ could have depended on the state (it does not — the KMS temperature is purely kinematic). That neither pathology obtains makes the gap equation a genuine determination. The non-circularity is structural: Part I establishes that a QFT emerges with *some* action scale $\hbar$; §5 determines *which* $\hbar$, using the independent classical temperature that Part I neither requires nor produces.

**Non-circularity of the entropy density.** The claim $\eta = 1/\epsilon^2$ may appear to pre-bake the area-entropy proportionality. Consider the counterfactual $\eta = \alpha/\epsilon^2$: thermal matching gives $\hbar = \alpha c^3 \epsilon^2 / (4G)$, and the Bekenstein-Hawking entropy becomes $S = A / (4\alpha^{-1} l_p^2)$, reproducing the $1/4$ factor only for $\alpha = 1$. This is a non-trivial constraint: each minimal cell contributes exactly one boundary mode. The counting follows from $\epsilon$ being the minimal distinguishable scale (Axiom 2) combined with the $q$-independence of all predictions — the number of internal states per cell is irrelevant, so what counts is cells, not states.

The predictive content lies not in the gap equation alone but in its consequences. The specific relationship $\hbar = c^3\epsilon^2/(4G)$ — rather than any other function of $c$, $G$, $\epsilon$ — produces: the Bekenstein-Hawking formula with the exact factor $1/4$ (§6), the CC dissolution with $S_{\text{dS}}$ as the compression ratio (§7.3), the RVM parameter $\nu_{\text{OI}}$ (§8.1), and the GW echo timescale (§8.2). Any alternative $\hbar(\epsilon)$ would fail at least one of these checks. The situation is analogous to deriving the Schwarzschild metric with $M$ as a free parameter: the derivation has genuine content (the functional form) even though one input is not determined from within.

Jacobson's original derivation [16] uses $\hbar$-containing forms; this paper does not — it uses the classical identity $dE = (c^2 \kappa / 8\pi G)\,dA$ and the classical entropy density $\eta = 1/\epsilon^2$. The logical ordering differs from Jacobson's: his argument derives $G$ from $\eta$ and $\hbar$; the present argument takes $G$ as a parameter of the classical Hamiltonian (Axiom 1) and derives $\hbar$ from $G$ and $\epsilon$. The two are consistent — substituting $\eta = 1/\epsilon^2$ and $\hbar = c^3\epsilon^2/(4G)$ into Jacobson's formula $G_{\text{eff}} = c^4/(8\pi \eta \cdot \hbar c)$ recovers $G_{\text{eff}} = G$ — but the roles of input and output are reversed. The Gibbons-Hawking temperature [17] $k_B T_{\text{GH}} = \hbar \kappa / (2\pi c)$ is recovered as a prediction, not used as an input. The KMS condition used above is derived for continuum QFT on bifurcate Killing horizons; for the lattice-regularized theory emerging from Part I, the relevant result is that thermal periodicity of the Euclidean Green's functions is robust against UV modifications of the dispersion relation, with corrections at $\mathcal{O}((\epsilon \kappa/c)^2)$ [28, 29]. For the cosmological horizon, $\epsilon \kappa / c = \epsilon H / c \sim 10^{-61}$, so lattice corrections are $\sim 10^{-122}$.

### 5.3 Gauge-Fixing and the Dimensional Obstruction

Does the transition-probability data $\{T_{ij}(t)\}$ determine the emergent Hamiltonian uniquely? The following theorem shows the residual gauge freedom is physically trivial.

**Theorem (D-gauge completeness).** *Let $U(t) = e^{-iHt}$ with non-degenerate eigenvalues and non-vanishing configuration-basis overlaps. If $|U'_{ij}(t)|^2 = |U_{ij}(t)|^2$ for all $i, j, t$, then $H' = DHD^\dagger$ for a time-independent diagonal unitary $D$.*

*Proof.* Expand $|U_{ij}(t)|^2 = \sum_{k,l} V_{ik} V^*_{jk} V_{jl} V^*_{il} \, e^{-i(E_k - E_l)t}$. Fourier analysis recovers the frequencies $E_k - E_l$ (distinct by non-degeneracy) and the coefficients $a^{kl}_{ij} = V_{ik} V^*_{jk} V_{jl} V^*_{il}$. From the diagonal coefficients: $|V'_{ia}| = |V_{ia}|$. Writing $V'_{ia} = V_{ia} e^{i\delta_{ia}}$, the off-diagonal coefficients require:

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

The framework yields $\epsilon = 2\,l_p$ exactly. This is algebraically equivalent to the formula for $\hbar$: the framework contains one free geometric parameter ($\epsilon$), and thermal self-consistency establishes its relationship to $\hbar$. The result is a self-consistency condition constraining $\epsilon$ to the Planck regime, not an independent determination. If $\epsilon^2 \ll l_p^2$, sub-Planckian subcells would create a second trace-out, breaking the single-valuedness of $\hbar$. If $\epsilon^2 \gg l_p^2$, the emergent description would assign distinct quantum states to physically identical configurations. The framework's predictive content comes from the relationship $\hbar = c^3 \epsilon^2/(4G)$, the Bekenstein-Hawking formula, and the consequences that follow.

With $\epsilon = 2\,l_p$, the number of independent modes on the cosmological horizon is:

$$N_{\text{modes}} = \frac{A}{\epsilon^2} = \frac{A}{4\,l_p^2} = S_{\text{dS}}$$

where $S_{\text{dS}} = A/(4\,l_p^2)$ is the Bekenstein-Hawking entropy of the de Sitter horizon. The factor of $1/4$ in the Bekenstein-Hawking formula — historically introduced as a proportionality constant — is here derived: each minimal cell of area $\epsilon^2 = 4\,l_p^2$ on the horizon contributes one unit of entropy, and $A / (4\,l_p^2) = A / \epsilon^2$ recovers the standard formula exactly.

---

## 7. DISSOLUTION OF THE COSMOLOGICAL CONSTANT PROBLEM

### 7.1 The Two Levels of Description

Part I delivers QM on a finite-dimensional Hilbert space. The $N = A/\epsilon^2$ cells discretize the visible sector; spatial locality gives $\mathcal{H} = \bigotimes_k \mathcal{H}_k$ — a lattice-regularized QFT with UV cutoff at $\epsilon = 2\,l_p$. The CC dissolution requires only that the emergent description assigns zero-point energy $\sim \hbar\omega/2$ per mode — a property of any lattice QFT with local couplings, regardless of field content.

**Classical substratum** (what geometric measurements probe): The horizon has classical thermal equilibrium. By the Friedmann equation, $\rho_{\text{crit}} = 3H^2 c^2/(8\pi G)$. No zero-point energy, no discrepancy. Total vacuum energy density: $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$ — precisely observed.

**Emergent QFT** (what local quantum measurements probe): Zero-point energy $\frac{1}{2}\hbar\omega$ per mode summed to the Planck cutoff gives $\rho_{\text{QFT}} \sim 10^{113}$ J/m$^3$ — a $\sim 10^{122}$ discrepancy with the observed value [2, 3, 18].

### 7.2 Why Gravity Sees the Classical Value

Spacetime geometry is part of the classical substratum (Axiom 3): the metric evolves via Einstein's equations *before* the trace-out. The stress-energy sourcing gravity is the classical stress-energy of the total microstate, not the expectation value of an emergent quantum operator. The semiclassical equation $G_{\mu\nu} = 8\pi G \langle \hat{T}_{\mu\nu} \rangle$ is itself an emergent approximation; at the classical level, the gravitational field equations never encounter the zero-point sum.

**Ontological commitment.** Classical spacetime is fundamental; QM is emergent. This ordering is not a modeling choice but is forced by the logical structure of the derivation through three independent requirements:

*(i) Definiteness.* The trace-out that produces QM is defined by a *specific* partition $\Gamma = \Gamma_V \times \Gamma_H$. The partition must be definite — not in superposition, not subject to quantum uncertainty — for the marginalization integral (§1.4) to be well-defined. A partition in superposition would yield an incoherent mixture of inequivalent quantum theories, not a single QM. The metric at the partition boundary must therefore be classical.

*(ii) Non-circularity.* The partition is defined by the causal structure: $\Gamma_H$ is the set of degrees of freedom beyond the observer's causal reach (§4.1). Causal structure is determined by null geodesics of the metric. If the metric were derived from QM, then the derivation would require: QM $\to$ metric $\to$ causal structure $\to$ partition $\to$ QM — a circular dependency with no entry point. The circle breaks only if the metric exists prior to the partition.

*(iii) Uniqueness of $\hbar$.* The emergent action scale is determined by the boundary geometry (§5.2). If the geometry were itself quantum-mechanical, $\hbar$ would depend on a quantum state — but $\hbar$ is state-independent by observation. The geometry-first ordering is the only one consistent with a universal $\hbar$.

Any framework in which QM is logically prior to the metric must either (a) treat the zero-point sum as a gravitational source — producing the $10^{122}$ discrepancy requiring cancellation or fine-tuning — or (b) invoke an independent mechanism to decouple quantum vacuum energy from gravity. In the present framework, the zero-point sum is an artifact of the emergent description and never enters the stress-energy tensor; no decoupling mechanism is needed.

**Cumulative evidence for the ordering.** The geometry-first ordering produces seven independent consequences that match observation, none of which were designed into the axioms: (1) the CC dissolution — the observed vacuum energy sits at $\rho \sim H^2/G$, the classical baseline, without fine-tuning (§7.3); (2) the Bekenstein-Hawking formula including the $1/4$ factor, derived from $\epsilon = 2\,l_p$ (§6); (3) the value of $\hbar$, determined by partition geometry rather than treated as a free parameter (§5.2); (4) the dark-sector concordance — ~95% of $\rho_{\text{crit}}$ is invisible to QFT, matching the observed dark sector (§8.3); (5) dark energy evolution with $\nu_{\text{OI}}$ in the range consistent with DESI data (§8.1); (6) a testable GW echo prediction at the discreteness scale (§8.2); (7) the MOND acceleration scale $a_0 = cH/6$ and the baryonic Tully-Fisher relation, derived from entropy displacement (§8.4). Quantum-first orderings produce the $10^{122}$ discrepancy, have no natural account of the dark sector, and treat $\hbar$ and the $1/4$ factor as unexplained inputs. The cumulative case is not a single tiebreaker but a pattern: every quantitative output of the geometry-first ordering is consistent with observation; the central quantitative output of the quantum-first ordering is the worst prediction in physics.

**The classical vacuum energy scale.** The framework does not explain *why* $\rho \sim H^2/G$; this is set by initial conditions via the Friedmann equation. What it does is reclassify the CC puzzle: from a 122-digit cancellation between independent contributions (bare $\Lambda$ and zero-point energies of every field, re-tuned at each perturbative order) to a standard cosmological initial-conditions question about a single parameter.

**Quantum corrections to gravity.** The emergent vacuum energy does feed back into gravitational dynamics at the state level (§8.1 derives dark energy evolution). What the framework excludes is the zero-point sum — the ground-state eigenvalue of $\hat{H}_{\text{eff}}$, which acts on $\mathcal{H}_V$. Gravity is sourced by $H_{\text{tot}}$, which acts on the full phase space $\Gamma$; the zero-point sum appears when classical transition probabilities are reorganized into Hilbert space formalism, not when classical dynamics is evolved.

### 7.3 The Structural Origin of the $10^{122}$ Discrepancy

$\rho_{\text{QFT}} / \rho_{\text{classical}} \sim M_{\text{Pl}}^4 / (H^2/G) = S_{\text{dS}} = A/(4\,l_p^2)$ — the Bekenstein-Hawking entropy, now identified as the information compression ratio of the trace-out. The "worst prediction in physics" is the entropy of the observer's blind spot — a category error, not a fine-tuning failure. Wolpert's limits of inference [19] confirm this cannot be resolved from within: both geometric and quantum measurements are faithful to their respective descriptions, and no embedded observer can determine which is more fundamental. This is not a prediction awaiting future data — the observed vacuum energy sits at the classical geometric scale $\rho \sim H^2/G$, the value the framework expects.

---

## 8. PREDICTIONS AND TESTS

### 8.1 Dark Energy Evolution in Running Vacuum Form

$\hbar$ is $H$-independent (§5.2), but the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume. Expanding $\Lambda_{\text{eff}}(H)$:

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu_{\text{OI}}}{8\pi G}(H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

This is the Running Vacuum Model [20, 21]. The $S_{\text{dS}}$ horizon modes span frequencies $\omega_{\text{IR}} = H$ to $\omega_{\text{UV}} = c/\epsilon$. For conformal fields, the spectral density is uniform in $\ln\omega$, so the number of independent spectral channels is $\mathcal{N}(H) = \ln(c/\epsilon H)$. Each carries fraction $1/\mathcal{N}$ of the total gravitating vacuum energy, so $\rho_\Lambda \propto 1/\mathcal{N}$. Taylor-expanding:

$$\boxed{\nu_{\text{OI}} = \frac{\Omega_\Lambda}{2\,\ln(c/\epsilon H_0)}}$$

With $\epsilon = 2\,l_p$, $H_0 = 67.4$ km/s/Mpc, $\Omega_\Lambda = 0.685$: $\nu_{\text{OI}} = 2.45 \times 10^{-3}$ (parametric uncertainty $\pm 0.03 \times 10^{-3}$ from $H_0$ and $\Omega_\Lambda$; systematic range $2.2$–$2.7 \times 10^{-3}$ from SM corrections to the spectral assumption below). Independently testable ratio: $\nu_{\text{OI}} / \Omega_\Lambda \approx 0.00358$.

**Sensitivity to the spectral assumption.** The prediction depends on the spectral distribution of the boundary mode energy. Three cases illustrate the range:

(i) *Flat in $\ln\omega$ (conformal boundary).* Each logarithmic frequency band carries equal energy. This gives $\mathcal{N} = \ln(c/\epsilon H_0) \approx 140$ and $\nu_{\text{OI}} = 2.45 \times 10^{-3}$. This is the physically motivated case: the boundary modes are degrees of freedom of the classical substratum, whose dynamics (the wave equation) has approximately conformal dispersion $\omega = |k|$ over the full 140-decade range from $H$ to $c/\epsilon$. Standard Model mass thresholds and QCD confinement modify the *emergent* field content but not the substratum's boundary mode spectrum.

(ii) *SM-corrected conformal.* If non-conformal corrections affect ~15 decades (from the electron mass to the top quark mass) out of 140, the effective channel count shifts to $\mathcal{N}_{\text{eff}} \in [125, 155]$, giving $\nu_{\text{OI}} \in [2.2, 2.7] \times 10^{-3}$. The logarithmic structure suppresses sensitivity: a 10% change in the spectral range produces a 12% shift in $\nu$.

(iii) *Power-law boundary spectrum.* A naive 2D density of states $g(\omega) \propto \omega$ gives energy per logarithmic band $\propto \omega^2$ (UV-dominated), yielding $\nu \sim (\epsilon H/c)^2 \sim 10^{-122}$ — effectively zero. This case is excluded if the boundary modes' energy follows equipartition at $T_{\text{dS}}$ on the substratum rather than the emergent QFT's spectral weighting.

The prediction is therefore: $\nu_{\text{OI}} \approx 2.45 \times 10^{-3}$ (conformal benchmark), with SM corrections contained within $[2.2, 2.7] \times 10^{-3}$, provided the boundary spectral density is set by the substratum dynamics. The independently testable ratio $\nu_{\text{OI}} / \Omega_\Lambda \approx 0.00358$ is robust to $\pm 12\%$.

DESI data [22, 30] report evolving dark energy at $2.8\sigma$–$4.2\sigma$. RVM fits [31] find $\nu \sim \mathcal{O}(10^{-3})$ with $\nu = 0$ disfavored at $2.7\sigma$–$3.1\sigma$, consistent with the prediction.

### 8.2 Gravitational Wave Echoes

A black hole horizon represents a regime where the causal partition differs from the cosmological one: degrees of freedom reclassify from visible to hidden sector as they cross the horizon, shifting the effective partition and the emergent description.

At proper distance $\sim \epsilon$ outside a black hole horizon $r_h$, an infalling mode reaches the discreteness floor and must scatter back. The predicted time delay is:

$$\Delta t_{\text{echo}} \approx \frac{r_h}{c} \ln\left(\frac{r_h}{2\,l_p}\right)$$

For a $30 M_\odot$ remnant, logarithmic dependence on $\epsilon$ makes this robust ($\sim 0.1$ ms shift within the $\sim 54$ ms timescale [23]). Detection would constitute direct evidence that $\epsilon$ has observable consequences at horizons other than the cosmological one — a regime where partition-relativity (§1.4) becomes empirically accessible. Joint confirmation of dark energy evolution *and* GW echoes would uniquely favor an information-theoretic origin, since standard RVMs predict $\Lambda(H)$ running but have no mechanism for discreteness-scale echoes.

### 8.3 The Dark-Sector Corollary

The trace-out that produces QM has an automatic gravitational consequence.

**Corollary (Invisible gravitational budget).** *Under Axioms 1–4 and conditions (C1)–(C3), the cosmological trace-out that produces quantum mechanics simultaneously renders ~95% of the universe's gravitational budget invisible to the emergent QFT.*

*Proof.* Three steps, each using only results already established.

*(i) Total effective density.* The horizon carries $S_{\text{dS}} = A/\epsilon^2$ modes (§6). The classical temperature is $T_{\text{cl}} = c^3 \epsilon^2 H / (8\pi G k_B)$ (§5.1), computed entirely within the classical substratum with no reference to $\hbar$ or the emergent quantum description. The total thermal energy is $E_s = S_{\text{dS}} \cdot k_B T_{\text{cl}}$. By the shell theorem, distributing over $V_H = 4\pi c^3/(3H^3)$:

$$\rho_s = \frac{E_s}{V_H} = \frac{A}{\epsilon^2} \cdot \frac{c^3 \epsilon^2 H}{8\pi G} \cdot \frac{3H^3}{4\pi c^3} = \frac{3c^2 H^2}{8\pi G} = \rho_{\text{crit}}$$

This identity, which Verlinde [37] assumes, is here derived.

*(ii) Invisibility.* The boundary modes comprising $S_{\text{dS}}$ are hidden-sector degrees of freedom — the variables traced out to produce the quantum description. No hidden-sector degree of freedom maps to an operator on $\mathcal{H}_V$. The gravitational influence of the boundary entropy therefore has no source in $\langle \hat{T}_{\mu\nu} \rangle$. This follows from Part I's trace-out structure alone; the gravitational consequence (additional gravity with no particle-sector source) follows from the geometry-first ordering of §7.2, which is already required by Part II's logic.

*(iii) Budget.* The emergent QFT accounts for the baryonic sector (~5% of $\rho_{\text{crit}}$). The remaining ~95% is boundary entropy — gravitationally active (because $\rho_s$ is a classical quantity computed before the trace-out, unlike $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4$ which is an artifact of the emergent description) but invisible to the emergent QFT. This matches the observed composition, in which ~95% of the gravitational content has no source in particle physics. $\square$

The corollary is a consistency check for the total dark sector budget, not a derivation of its internal structure. The uniform component of the boundary entropy corresponds to dark energy (§7); the structured component — the matter-induced redistribution of boundary entropy producing local gravitational effects resembling dark matter — is derived in §8.4. The ratio $\rho_{\text{QFT}} / \rho_s \sim S_{\text{dS}} \sim 10^{122}$ confirms the parallel with §7.3: the information compression ratio and the gravitational occlusion fraction are two aspects of a single phenomenon.

**Falsifiability.** The corollary would be falsified by detection of dark matter particles accounting for the full ~27% structured dark sector, or by evidence that the dark sector's gravitational effects are unrelated to the boundary geometry.

### 8.4 Dark Matter from Entropy Displacement

The total dark sector budget is established by §8.3. This section derives the structured component from the entropy displacement induced by baryonic matter.

**Step 1: Entropy displacement (derived).** Baryonic matter $M_B$ is coupled to the boundary entropy through $H_{VB}$ (condition C1). The boundary is a thermal reservoir at $T_{\text{dS}} = \hbar H / (2\pi c k_B)$ (derived, §5.2). For a static matter configuration in gravitational equilibrium — a quasi-static process — the Clausius relation gives the entropy displacement:

$$\Delta S = \frac{M_B c^2}{k_B T_{\text{dS}}} = \frac{2\pi M_B c^3}{\hbar H}$$

This follows from the generalized second law (Theorem B.6) applied to the matter-boundary system: the boundary's entropy reduction is $Q/T$ for a reversible process, where $Q = M_B c^2$ and $T = T_{\text{dS}}$. For dynamic configurations, the Clausius inequality $\Delta S \geq Q/T$ only strengthens the displacement.

**Step 2: The critical acceleration (derived).** The displaced entropy perturbs the entanglement structure of de Sitter space. At radius $r$ from the mass, the entanglement entropy between the interior and exterior of a sphere is modified by the ratio of the Newtonian gravitational potential to the de Sitter background potential:

$$\varepsilon(r) = \frac{\Phi_N(r)}{\Phi_{\text{dS}}(r)} = \frac{2GM_B}{H^2 r^3}$$

The Jacobson mechanism converts this entropy perturbation into curvature. The gravitational response is quadratic in the strain: the apparent dark mass at radius $r$ satisfies

$$M_D(r)^2 = \frac{M_B \cdot cH \cdot r^2}{d(d-1)\,G}$$

where $d$ is the spatial dimension. The quadratic relationship — rather than linear $M_D \propto \varepsilon \cdot M_{\text{dS}}$ — arises because the gravitational effect of the entropy displacement involves the square of the perturbation, as in any elastic medium [37]. The factor $d(d-1)$ enters through the $d$-dimensional Friedmann equation, $\rho_{\text{crit}} = d(d-1)\,c^2 H^2 / (16\pi G)$, which sets the background de Sitter mass within radius $r$. From the Gauss law, $g_D(r) = GM_D(r)/r^2 = \sqrt{GM_B \cdot a_0}/r$. The crossover acceleration, where $g_D = g_N = GM_B/r^2$, is:

$$a_0 = \frac{cH}{d(d-1)}$$

For $d = 3$ (the observed spatial dimensionality; the unique value consistent with propagating gravity, stable matter, renormalizability, and the concordance $\rho_s/\rho_{\text{crit}} = 2/(d-1) = 1$):

$$\boxed{a_0 = \frac{cH}{6} \approx 1.2 \times 10^{-10} \; \text{m/s}^2}$$

This matches the empirical MOND acceleration scale — derived, not fitted. The factor $6 = 3 \times 2$ is a geometric consequence of three spatial dimensions, connecting the MOND scale to the $d = 3$ derivation. Verlinde [37] obtains the same result from the elastic response of de Sitter entanglement entropy; the OI framework provides the entropy displacement (Step 1) and the dimensional origin ($d = 3$ from self-consistency).

**Step 3: The deep-MOND regime.** For baryonic acceleration $\ll a_0$, the displaced entropy dominates. The Jacobson mechanism converts the entropy gradient into curvature, giving $g_{\text{total}} = \sqrt{g_B \cdot a_0}$ and rotation velocity:

$$v^2 = r \cdot g_{\text{total}} = \sqrt{GM_B \cdot cH/6} = \text{constant} \qquad \Longrightarrow \qquad v^4 = GM_B \cdot cH/6$$

This is the baryonic Tully-Fisher relation. Flat rotation curves emerge with no dark matter particles and no free parameters beyond the baryonic mass.

**Step 4: Interpolation constraints.** The interpolation between the Newtonian ($g_B \gg a_0$) and deep-MOND ($g_B \ll a_0$) regimes is constrained but not unique. The framework requires: no free parameters (only $g_B$ and $a_0$), conservative force ($\nabla \times g_D = 0$), monotonicity, correct limits, and analyticity. These narrow the interpolation to a one-parameter family indexed by transition steepness — solution-specific, like fermion masses. A representative member: $g_D = (a_0/2)(\sqrt{1 + 4g_B/a_0} - 1)$.

**Epistemic status.** Steps 1–3 are Tier 2: the displacement formula follows from the Clausius relation applied to the boundary reservoir (§5.2, B.6), the factor $d(d-1) = 6$ from the $d$-dimensional Friedmann equation with $d = 3$ derived from self-consistency, and $a_0 = cH/6$ and $v^4 = GM_B \cdot cH/6$ are parameter-free consequences. The interpolation constraints (i)–(v) are Tier 2; the transition steepness is Tier 3 (solution-specific).

**Observational predictions.** (i) Dark matter "mass" within radius $r$ is determined entirely by enclosed baryonic mass and $H$ — no halo-specific parameters. (ii) The effect depends on $H(z)$: dark matter phenomenology at high redshift differs systematically from low-redshift observations. (iii) The Tully-Fisher relation evolves: $v^4 \propto H(z)$.

**Falsifiability.** The entropy displacement account would be falsified by: (a) detection of dark matter particles accounting for ~27% of $\rho_{\text{crit}}$; (b) high-redshift rotation curves inconsistent with the predicted $H(z)$ dependence; (c) baryonic Tully-Fisher violations exceeding baryonic mass uncertainties.

---

## 9. DISCUSSION

### 9.1 Interpretive Consequences and Scope

The characterization theorem is a full equivalence: QM $\iff$ embedded observation under (C1)–(C3). In the cosmological realization, all visible-sector degrees of freedom — photons, electrons, slits, detectors — acquire their quantum behavior from the single cosmological trace-out. The double-slit particle traverses a single slit in the deterministic substratum; interference arises from boundary-condition dependence of the transition matrix. The Born rule is derived (equilibrium of the indivisible process), not postulated. Wigner's friend has a definite outcome; "branches" are features of the compressed description.

### 9.3 The Status of the Discreteness Scale

$\epsilon$ does not smuggle in a quantum assumption. Axiom 2 requires finite-dimensionality, motivated by the classical fact that finite-area boundaries admit finitely many modes. The result $\epsilon = 2\,l_p$ is a *consequence* of self-consistency (§6). Holographic entropy bounds [27] provide independent, non-quantum motivation.

### 9.3 Vacuum Energy: Relative Effects and the Higgs Potential

Casimir forces and Lamb shifts are relative effects (energy differences between configurations) within the emergent QFT; they gravitate because the corresponding classical microstates differ in energy. The framework denies that *absolute* zero-point sums gravitate, because gravity operates at the classical level (§7.2).

The Higgs vacuum energy shift $V(\phi_{\text{min}}) \sim (200\;\text{GeV})^4$ and the QCD condensate energy are absolute properties of the emergent ground state — energies the emergent QFT assigns to configurations whose classical energy is $\rho \sim H^2/G$. The dissolution applies uniformly: the zero-point sum, the Higgs vacuum energy, and the QCD condensate are all artifacts of how the emergent description organizes microstates, not properties of the microstates themselves.

**Why QCD binding energy gravitates.** The proton mass is ~99% QCD binding energy. This gravitates because it is a *relative* quantity: a proton vs. three free quarks corresponds to distinct classical microstate classes with different energies in $H_{\text{tot}}$. The Jacobson mechanism reads coupling-structure differences as curvature. The absolute baseline (zero-point sum over all modes) corresponds to the partition's information capacity ($S_{\text{dS}}$), not to the dynamics, and does not source curvature.

### 9.4 Relation to Prior Work

**'t Hooft [1]:** Differs in mechanism (epistemic trace-out vs. information loss), generality (any system satisfying axioms vs. particular rules), and Bell placement (outcome independence violation vs. superdeterminism). **QBism/relational QM:** Share observer-relative epistemic states; this framework provides a structural *why* and quantitative predictions. **Jacobson [16]:** Derives gravity from thermodynamics; this framework derives QM from causal structure — complementary and mutually consistent.

**DSW horizon decoherence [38, 39].** DSW proved that any Killing horizon decoheres nearby quantum superpositions at a geometry-dependent rate. This matches the framework's partition mechanism: (i) decoherence rate depends on horizon geometry (partition-relativity); (ii) decoherence vanishes for extremal black holes (C1 failure); (iii) the process is non-Markovian near the horizon [40]. DSW derives these within the emergent QFT; this framework explains *why* — the trace-out across a causal partition generates QM itself.

**AdS/CFT.** Entanglement-first programs (Ryu-Takayanagi, ER=EPR, "it from qubit") are equally consistent with geometry assembling entanglement rather than the reverse. The $1/4$ factor in the Bekenstein-Hawking formula is derived here (§6). Empirically: entanglement-first orderings inherit the zero-point sum as a gravitational source; this framework does not.

### 9.6 Assumptions, Limitations, and Falsifiability

**The theorem** requires Axiom 2 (independent in Part I; consequence of geometry in Part II), the stochastic-quantum bridge (§3.1 and Appendix A; established by two independent routes), and genericity conditions (non-degenerate spectrum, non-vanishing overlaps), which hold for all but a measure-zero set. The P-indivisibility proof uses finiteness via the recurrence argument ($\varphi^N = \text{id}$). The deep-sector cardinality corollary (§5.2) establishes that only $\mathcal{C}_V$ and $\mathcal{C}_B$ need be finite — both guaranteed by holographic entropy bounds [27] independently of the de Sitter finite-dimensionality conjecture — while the deep sector $\mathcal{C}_D$ may be infinite. The accessible-timescale backflow lemma (§2.3) provides a second route to P-indivisibility that is independent of $|\mathcal{C}_H|$. The characterization theorem becomes an equivalence on observable timescales ($T_{\text{obs}} \ll \tau_B \sim 10^{17}$ s) — physically indistinguishable from a timeless identity for all experiments within the age of the universe.

**The sharp partition and constraint structure.** Axiom 3's product decomposition $\Gamma = \Gamma_V \times \Gamma_H$ is the kinematic phase space. In GR, the Hamiltonian and momentum constraints restrict the physical phase space to a submanifold $\Gamma_{\text{phys}} \subset \Gamma_V \times \Gamma_H$ on which interior and exterior data are correlated. P-indivisibility survives on a constraint surface because restoring P-divisibility would require decoupling the sectors entirely, violating the constraints; the constraint surface thus enforces (C1) non-perturbatively. For systems other than the cosmological horizon, the fidelity of the product approximation determines the fidelity of the emergent quantum description.

**Planck-scale ordering.** The classical-prior ontology may break down at $l_p$, where "geometric" and "quantum" lose operational distinction. If a deeper theory unifies both, this framework describes the effective macroscopic regime.

**Falsifiability.** The *theorem* would be falsified by a failure of both the stochastic-quantum correspondence and the Stinespring construction for the class of processes generated here — a possibility excluded by the independent proofs in §3.1 and Appendix A. The *cosmological application* would be falsified by definitive absence of dark energy evolution or GW echoes at the predicted timescale. The *dark-sector concordance* (§8.3) would be falsified by detection of dark matter particles accounting for the full structured dark sector, or by evidence that the dark sector's gravitational effects are unrelated to the cosmological boundary geometry.

**Nested partitions.** Multiple coexisting causal boundaries create nested partitions. Appendix B resolves this: sequential and direct trace-outs produce the same CPTP channel and $\hbar$ (B.1–B.4); the generalized second law holds (B.6); the Page curve is derived with $t_P \approx 0.646\,t_{\text{evap}}$ from bijectivity and Popescu-Short-Winter typicality (B.7–B.9), without assuming ergodicity.

---

## 10. CONCLUSION

**The general theorem (Part I).** Under four axioms and conditions (C1)–(C3), the P-indivisibility of reduced dynamics is proved: any bijective dynamics on a finite system with non-trivial coupling necessarily produces P-indivisible stochastic dynamics. By the stochastic-quantum correspondence, the observer's description is necessarily quantum mechanics. Continuous-time transition data resolves all gauge freedom. The Schrödinger equation, Born rule, and Bell violations are structural consequences. The characterization theorem establishes that the conditions are necessary: QM and embedded observation under (C1)–(C3) are equivalent.

**The cosmological application (Part II).** The cosmological horizon provides a realization where the sharp-partition approximation is exact and all conditions hold. The theorem yields: (a) $\hbar = c^3 \epsilon^2 / (4G)$ with $\epsilon = 2\,l_p$ and the Bekenstein-Hawking formula as consequences; (b) dissolution of the CC problem — the $10^{122}$ discrepancy is $S_{\text{dS}}$, the compression ratio of the observer's quantum description; (c) falsifiable predictions including RVM dark energy with $\nu_{\text{OI}} \approx 2.45 \times 10^{-3}$ and gravitational wave echoes; (d) an automatic dark-sector corollary — the same trace-out renders ~95% of the universe's gravitational budget invisible to the emergent QFT; and (e) dark matter phenomenology from entropy displacement — flat rotation curves, the baryonic Tully-Fisher relation $v^4 = GM_B \cdot cH/6$, and the MOND acceleration scale $a_0 = cH/6 \approx 1.2 \times 10^{-10}$ m/s², all derived from the boundary entropy and the Jacobson mechanism (§8.4).

**Nested partitions (Appendix B).** When multiple causal horizons coexist, the emergent quantum description is self-consistent: the quantum partial trace within the emergent description agrees with the classical marginalization on the substratum (Theorem B.2). The generalized second law — non-decrease of $S_{\text{matter}} + S_{\text{BH}} + S_{\text{dS}}$ — follows from strong subadditivity and CPTP monotonicity (Theorem B.6). The Page curve is derived: $S_{\text{rad}}(t) = \min(n_R(t), n_B(t)) \cdot \ln q$ with turnover at $t_P \approx 0.646 \, t_{\text{evap}}$, from bijectivity of $\varphi$ (cycle decomposition on the finite energy shell), Popescu-Short-Winter typicality [41], and the derived Hawking temperature (Theorems B.7–B.9). Information is never lost.

The apparent conflict between quantum mechanics and general relativity, the $10^{122}$ vacuum energy discrepancy, and the dark sector are three faces of the same fact: the information-theoretic cost of embedded observation.

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
[37] E. P. Verlinde, "Emergent Gravity and the Dark Universe," *SciPost Phys.* **2**, 016 (2017); arXiv:1611.02269.

[38] D. L. Danielson, G. Satishchandran, and R. M. Wald, "Black holes decohere quantum superpositions," *Int. J. Mod. Phys. D* **31**, 2241003 (2022).

[39] D. L. Danielson, G. Satishchandran, and R. M. Wald, "Killing horizons decohere quantum superpositions," *Phys. Rev. D* **108**, 025007 (2023).

[40] Y. Li, "Non-Markovian Gravitational Decoherence and the Black Hole Information Paradox," *Int. J. Theor. Phys.* **63**, 293 (2024).

[41] S. Popescu, A. J. Short, and A. Winter, "Entanglement and the foundations of statistical mechanics," *Nature Physics* **2**, 754–758 (2006).

[42] D. N. Page, "Average entropy of a subsystem," *Phys. Rev. Lett.* **71**, 1291 (1993).

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

The Barandes route is *analytic* (process → quantum): it starts from observed P-indivisible transitions and embeds them into unitary QM. The Stinespring route is *synthetic* (setup → quantum): it constructs the quantum description directly from the bijection using only textbook results [32, 33]. The two routes have different logical structures and no shared failure mode. Both produce the same $T_{ij}(t)$, establishing that QM emergence is overdetermined. The Barandes route powers (ii) $\implies$ (i) in the characterization theorem; the Stinespring route supplies (iii) $\implies$ (i) independently.

---

## APPENDIX B: NESTED PARTITIONS

This appendix proves the consistency of nested trace-outs, derives the generalized second law, and obtains the Page curve for an evaporating black hole. The results resolve all three layers of the nested partition problem stated in §9.6.

### B.1 Setup

Let $\mathcal{C}_V$, $\mathcal{C}_B$, $\mathcal{C}_D$ be finite configuration spaces with $|\mathcal{C}_V|, |\mathcal{C}_B| \geq 2$, and let $\varphi: \mathcal{C}_V \times \mathcal{C}_B \times \mathcal{C}_D \to \mathcal{C}_V \times \mathcal{C}_B \times \mathcal{C}_D$ be a bijection. The physical picture: $V$ is the region between a black hole horizon and the cosmological horizon, $B$ is the black hole interior, $D$ is the trans-cosmological region. Define $W = V \cup B$ (the cosmological interior).

Two procedures produce a quantum description on $V$:

*Direct:* Trace out $B \cup D$ in one step, marginalizing over $\mathcal{C}_B \times \mathcal{C}_D$.

*Sequential:* (Stage 1) Trace out $D$, producing emergent QM on $W$. (Stage 2) Within the emergent QM on $W$, trace out $B$, producing a further-reduced description on $V$.

### B.2 Classical Associativity

**Theorem B.1.** *The direct and sequential procedures produce the same transition probabilities on $\mathcal{C}_V$.*

*Proof.* The direct transition matrix is:

$$T^{\text{dir}}_{ij}(t) = \frac{1}{|\mathcal{C}_B||\mathcal{C}_D|} \sum_{b \in \mathcal{C}_B} \sum_{d \in \mathcal{C}_D} \delta_{x_j}[\pi_V(\varphi_t(x_i, b, d))]$$

The sequential procedure marginalizes over $D$ (Stage 1) then over $B$ (Stage 2). Composing:

$$T^{\text{seq}}_{ij}(t) = \frac{1}{|\mathcal{C}_B|} \sum_b \frac{1}{|\mathcal{C}_D|} \sum_d \delta_{x_j}[\pi_V(\varphi_t(x_i, b, d))] = T^{\text{dir}}_{ij}(t)$$

The sums commute (Fubini on a finite product). $\square$

### B.3 Quantum-Classical Consistency

**Theorem B.2** (Quantum-classical consistency of nested trace-outs). *Let $\Phi_V^{\text{dir}}$ and $\Phi_V^{\text{seq}}$ be the CPTP channels on $\mathcal{H}_V$ produced by the direct and sequential procedures respectively. Then $\Phi_V^{\text{dir}} = \Phi_V^{\text{seq}}$.*

*Proof.* By the Stinespring construction (Appendix A), $\varphi$ defines a unitary $U_\varphi$ on $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_B \otimes \mathcal{H}_D$. The direct channel is $\Phi_V^{\text{dir}}(\rho_V) = \text{Tr}_{BD}[U_\varphi\,(\rho_V \otimes \rho_B \otimes \rho_D)\,U_\varphi^\dagger]$. The sequential channel is $\Phi_V^{\text{seq}}(\rho_V) = \text{Tr}_B[\text{Tr}_D[U_\varphi\,(\rho_V \otimes \rho_B \otimes \rho_D)\,U_\varphi^\dagger]]$. On finite-dimensional tensor products, $\text{Tr}_B \circ \text{Tr}_D = \text{Tr}_{BD}$, giving $\Phi_V^{\text{seq}} = \Phi_V^{\text{dir}}$. $\square$

### B.4 Hamiltonian and $\hbar$ Consistency

**Corollary B.3** (Hamiltonian consistency). *The emergent Hamiltonians $\hat{H}_V^{\text{dir}}$ and $\hat{H}_V^{\text{seq}}$ satisfy $\hat{H}_V^{\text{dir}} = D\,\hat{H}_V^{\text{seq}}\,D^\dagger$ for a time-independent diagonal unitary $D$.*

*Proof.* Theorem B.2 gives $\Phi_V^{\text{dir}} = \Phi_V^{\text{seq}}$, hence $T^{\text{dir}}_{ij}(t) = T^{\text{seq}}_{ij}(t)$ for all $t$ (Theorem A.2). The D-gauge theorem (§5.3) gives the result. $\square$

**Corollary B.4** ($\hbar$ universality). *Both procedures yield the same emergent action scale $\hbar = c^3 \epsilon^2 / (4G)$.*

*Proof.* $\hbar$ depends only on local boundary quantities $c$, $G$, $\epsilon$ (§5.2, Steps 2–3), not on which horizon defines the partition or how many trace-outs are performed. $\square$

### B.5 Additive Dissipators

**Theorem B.5** (Additive dissipators). *Let the classical Hamiltonian be spatially local with coupling chain $V \leftrightarrow B \leftrightarrow D$ (no direct $V$-$D$ coupling). Let $\tau_B^D$ be the $D$-sector timescale and $\tau_B^B$ the $B$-sector timescale. On observation timescales $t \ll \min(\tau_B^D, \tau_B^B)$, the dissipative correction to unitarity on $\mathcal{H}_V$ decomposes as:*

$$\mathcal{D}_V = \mathcal{D}_V^{(B)} + \mathcal{D}_V^{(D)} + \mathcal{R}$$

*where $\|\mathcal{D}_V^{(B)}\| = \mathcal{O}(\tau_S / \tau_B^B)$, $\|\mathcal{D}_V^{(D)}\| = \mathcal{O}(\tau_S / \tau_B^D)$, and the cross term satisfies $\|\mathcal{R}\| = \mathcal{O}(\tau_S^2 / (\tau_B^B \cdot \tau_B^D))$.*

*Proof.* Apply the boundary-only dependence lemma (§5.2) twice. Freezing $D$: the $V$-$B$ dynamics gives $\mathcal{D}_V^{(B)} \sim \mathcal{O}(\tau_S / \tau_B^B)$. The $D$-back-reaction on $B$ gives $\mathcal{D}_V^{(D)} \sim \mathcal{O}(\tau_S / \tau_B^D)$. The cross term arises from $D$'s shift modifying the $B$-state against which $\mathcal{D}_V^{(B)}$ is computed: $\|\mathcal{R}\| \leq \|\mathcal{D}_V^{(B)}\| \cdot \mathcal{O}(\tau_S / \tau_B^D) = \mathcal{O}(\tau_S^2 / (\tau_B^B \cdot \tau_B^D))$. $\square$

**Bound for the cosmological + stellar black hole case.** For a $30 M_\odot$ black hole inside the cosmological horizon: $\tau_S \sim 10^{-15}$ s, $\tau_B^B \sim \tau_{\text{scr}} \sim \beta \log S_{\text{BH}} \sim 10^{-3}$ s, $\tau_B^D \sim 1/H \sim 10^{17}$ s. The three terms:

$$\|\mathcal{D}_V^{(B)}\| \sim 10^{-12}, \qquad \|\mathcal{D}_V^{(D)}\| \sim 10^{-32}, \qquad \|\mathcal{R}\| \sim 10^{-44}$$

The cross term is negligible by 12 orders of magnitude relative to the smaller of the two primary dissipators.

### B.6 The Generalized Second Law

**Theorem B.6** (Generalized second law). *For any process described by the CPTP channel $\Phi_V$ on $\mathcal{H}_V$:*

$$S_{\text{matter}}(t) + S_{\text{BH}}(t) + S_{\text{dS}}(t) \geq S_{\text{matter}}(0) + S_{\text{BH}}(0) + S_{\text{dS}}(0)$$

*Proof.* The total state is pure (deterministic evolution from a definite initial state).

(i) *Subadditivity.* Strong subadditivity on $\mathcal{H}_V \otimes \mathcal{H}_B \otimes \mathcal{H}_D$ gives $S(\rho_{VB}) + S(\rho_{BD}) \geq S(\rho_B)$ (since $S(\rho_{VBD}) = 0$ for the pure total state).

(ii) *Identification.* $S_{\text{matter}} = S(\rho_V) = S(\rho_{BD})$ (by purification), $S_{\text{BH}} = S(\rho_B)$, $S_{\text{dS}} = S(\rho_D)$.

(iii) *Monotonicity.* The CPTP channel $\Phi_V$ contracts relative entropy [33], so $S(\rho_V)$ is non-decreasing. Any decrease in $S_{\text{BH}}$ transfers information from $B$ to $V \cup D$; unitarity of $\varphi$ ensures the total is compensated. $\square$

### B.7 The Page Curve

**Setup.** A black hole with initial horizon area $A_0$ evaporates. The partition boundary at the black hole horizon moves: modes transition from $B$ (interior) to $R$ (radiation, a subsystem of $V$) as the horizon shrinks. Define $n_B(t) = A_{\text{BH}}(t) / (4\,l_p^2)$ (the number of boundary modes at the BH horizon) and $n_R(t) = n_B(0) - n_B(t)$ (the number of emitted radiation modes). Conservation: $n_B(t) + n_R(t) = n_B(0) = S_{\text{BH}}(0)$.

The trans-cosmological sector $D$ is frozen on evaporation timescales ($\tau_{\text{evap}} \ll \tau_B^D$), so by Theorem B.5 the relevant dynamics is the bipartite system $B \cup R$ with $D$ decoupled at leading order.

**Theorem B.7** (Effective bipartite pure state). *On timescales $t \ll \tau_B^D$, the joint state of $B$ and $R$ is effectively pure: $\rho_{BR} = |\psi(t)\rangle\langle\psi(t)| + \mathcal{O}(\tau_S / \tau_B^D)$, where $|\psi(t)\rangle \in \mathcal{H}_B(t) \otimes \mathcal{H}_R(t)$.*

*Proof.* The total system evolves unitarily under $U_\varphi$ (Appendix A). The total state $|\Psi\rangle \in \mathcal{H}_V \otimes \mathcal{H}_B \otimes \mathcal{H}_D$ is pure (deterministic evolution from a definite initial state). By the boundary-only dependence lemma, the $D$-sector is frozen: $\rho_D$ is approximately constant, and $|\Psi\rangle \approx |\psi_{VB}\rangle \otimes |\chi_D\rangle + \mathcal{O}(\tau_S / \tau_B^D)$. Restricting to the $B \cup R$ subsystem (where $R \subset V$ is the radiation): $\rho_{BR} \approx |\psi\rangle\langle\psi|$ is pure at leading order. The correction is $\mathcal{O}(\tau_S / \tau_B^D) \sim 10^{-32}$. $\square$

**Theorem B.8** (Cycle typicality). *For the dynamics $\varphi$ on the energy shell $\Sigma_E \subset \mathcal{H}_B \otimes \mathcal{H}_R$, the time-averaged entanglement entropy of the radiation equals the Page value [42]:*

$$\overline{S(\rho_R)} = S_{\text{Page}}(d_B, d_R) + \mathcal{O}(\epsilon)$$

*for all initial conditions except a fraction $\leq 2e^{-c \, d_{\min} \, \epsilon^2}$, where $d_B = |\mathcal{C}_B(t)|$, $d_R = |\mathcal{C}_R(t)|$, $d_{\min} = \min(d_B, d_R)$, and:*

$$S_{\text{Page}}(d_B, d_R) = \ln(\min(d_B, d_R)) - \frac{\min(d_B, d_R)}{2\max(d_B, d_R)}$$

*Proof.* The bijection $\varphi$ conserves energy (the wave equation is Hamiltonian), so $\varphi$ restricts to a bijection on each energy shell $\Sigma_E$. Since $\Sigma_E$ is finite, this restricted bijection decomposes into disjoint cycles $C_1, \ldots, C_k$ with lengths $L_1, \ldots, L_k$ summing to $|\Sigma_E|$. On each cycle $C_j$, the time average of any observable $f$ is exact:

$$\overline{f}_{C_j} = \frac{1}{L_j} \sum_{s \in C_j} f(s)$$

By Popescu-Short-Winter [41], the set of atypical states — those with $|S(\text{Tr}_B |\psi\rangle\langle\psi|) - S_{\text{Page}}| > \epsilon$ — has measure at most $\eta = e^{-c \, d_{\min} \, \epsilon^2}$ on $\Sigma_E$, where $d_{\min} = \min(d_B, d_R)$ and $c > 0$ is a universal constant. The total number of atypical states is at most $\eta |\Sigma_E|$.

Call a cycle *bad* if its time-averaged entropy deviates from $S_{\text{Page}}$ by more than $\epsilon$. A bad cycle must contain a disproportionate fraction of atypical states. Specifically, if more than half the states in $C_j$ are typical (entropy within $\epsilon$ of $S_{\text{Page}}$), then $|\overline{S}_{C_j} - S_{\text{Page}}| \leq \epsilon + \mathcal{O}(\ln d_{\min} / L_j)$. So a bad cycle must have at least half its states atypical: $L_j \leq 2 \cdot |\{s \in C_j : s \text{ atypical}\}|$. Summing over all bad cycles:

$$\sum_{j \,\text{bad}} L_j \leq 2\eta\,|\Sigma_E|$$

The fraction of initial conditions on $\Sigma_E$ that land on a bad cycle is therefore at most $2\eta = 2e^{-c \, d_{\min} \, \epsilon^2}$. For a $30 M_\odot$ black hole, $d_{\min} \sim e^{S_{\text{BH}}} \sim e^{10^{77}}$, so $\eta \sim e^{-10^{77}}$. For all but an exponentially negligible fraction of initial conditions, the time-averaged entanglement entropy equals the Page value. $\square$

**Theorem B.9** (The Page curve). *The entanglement entropy of the radiation follows:*

$$S_{\text{rad}}(t) = \begin{cases} n_R(t) \cdot \ln q - \frac{q^{n_R(t)}}{2\,q^{n_B(t)}} & \text{for } n_R(t) < n_B(t) \quad \text{(early: before Page time)} \\ n_B(t) \cdot \ln q - \frac{q^{n_B(t)}}{2\,q^{n_R(t)}} & \text{for } n_R(t) > n_B(t) \quad \text{(late: after Page time)} \end{cases}$$

*where $q$ is the alphabet size (gauge — it cancels in all ratios), $n_B(t) + n_R(t) = n_B(0)$, and the Page time $t_P$ is defined by $n_R(t_P) = n_B(t_P) = n_B(0)/2$.*

*Proof.* Direct substitution of $d_B = q^{n_B(t)}$ and $d_R = q^{n_R(t)}$ into the Page entropy formula (Theorem B.8), using $\ln(q^n) = n \ln q$ and the conservation law $n_B + n_R = n_B(0)$. The turnover at $n_R = n_B$ follows from $\min(d_B, d_R)$ switching from $d_R$ to $d_B$. $\square$

**The evaporation trajectory.** The Hawking temperature (§5.2, Step 4) gives luminosity $L \sim 1/M^2$, hence $dM/dt = -\alpha/M^2$ where $\alpha = \hbar c^4 \Gamma / (15360 \pi G^2)$ and $\Gamma$ is the species-dependent greybody factor (solution-specific). Integrating:

$$M(t) = M_0\!\left(1 - t/t_{\text{evap}}\right)^{1/3}, \qquad t_{\text{evap}} = \frac{M_0^3}{3\alpha}$$

The boundary mode count $n_B(t) = 4\pi G M(t)^2 / (\hbar c) = n_B(0) \cdot (1 - t/t_{\text{evap}})^{2/3}$ and $n_R(t) = n_B(0) - n_B(t)$. The Page time $t_P$ satisfies $n_B(t_P) = n_B(0)/2$:

$$t_P = t_{\text{evap}}\!\left(1 - 2^{-3/2}\right) \approx 0.646 \; t_{\text{evap}}$$

The entropy of the radiation at the Page time is $S_{\text{rad}}(t_P) = n_B(0) \ln q / 2 = S_{\text{BH}}(0) \ln q / 2$ — half the initial black hole entropy, as expected.
