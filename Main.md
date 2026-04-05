# THE INCOMPLETENESS OF OBSERVATION
### Why Quantum Mechanics and General Relativity Cannot Be Unified From Within

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

An observer embedded in a deterministic universe cannot access the complete state. We prove that any such observer — coupled to a slow, high-capacity hidden sector on a finite-dimensional configuration space — must describe the visible sector using P-indivisible stochastic dynamics, mathematically equivalent to unitary quantum mechanics. The converse also holds: any quantum system, realized as a deterministic dilation, requires non-trivial coupling, slow-bath memory, and sufficient hidden-sector capacity. The Schrödinger equation, Born rule, and Bell violations emerge as structural consequences requiring no independent quantum postulates.

Applied to the cosmological horizon, the framework uniquely determines $\hbar = c^3 \epsilon^2 / (4G)$, fixes $\epsilon = 2\,l_p$, and recovers the Bekenstein-Hawking entropy $S = A/(4\,l_p^2)$. The $10^{122}$ cosmological constant discrepancy is identified as $S_{\text{dS}}$, the information compression ratio of the emergent quantum description; the observed vacuum energy is the mandatory classical baseline. Falsifiable predictions include dark energy evolution in Running Vacuum Model form with $\nu_{\text{OI}} = (2.45 \pm 0.04) \times 10^{-3}$ (the spectral uniformity that determines the central value is derived from the lattice structure, not assumed), consistent with current DESI data, gravitational wave echoes near black hole horizons, and Majorana neutrinos with normal mass ordering and a hierarchical spectrum ($\Sigma m_\nu$ near the oscillation minimum of $0.059$ eV, consistent with DESI+CMB bound of $< 0.064$ eV). The trace-out that produces QM simultaneously renders ~95% of the universe's gravitational budget invisible to the emergent description — matching the observed dark sector — providing independent corroboration of observational incompleteness.

---

# PART I: THE GENERAL THEOREM

## 1. INTRODUCTION

### 1.1 The Problem of Embedded Observation

An observer embedded in a deterministic universe cannot access the complete state: degrees of freedom beyond causal reach are permanently hidden, and the observer's description is obtained by marginalizing over the hidden sector. The question is what this reduction imposes on the form of the observer's physical laws.

Prior work (QBism, relational QM, 't Hooft's cellular automaton [1]) takes observer-dependence as an interpretive starting point or derives it from specific microphysical models. This framework differs by identifying *necessary and sufficient conditions* under which any embedded observer in any deterministic system necessarily sees quantum mechanics — and proving these are the *only* conditions under which QM arises from a deterministic embedding. These constraints carry empirical weight: the framework reveals that phenomena previously viewed as catastrophic anomalies — most notably the $10^{122}$ cosmological constant discrepancy — are mandatory consequences of embedded observation.

### 1.2 The Starting Point

The framework begins with a single empirical fact that cannot be doubted: *observation occurs*. An observer records distinguishable outcomes of interactions with a system not wholly under the observer's control. This is the cogito of Descartes made precise — not as philosophy, but as a mathematical constraint.

We ask: what is the minimal mathematical structure consistent with this fact?

**Definition.** An *observation* is a triple $(S, \varphi, V)$: a total system $S$, a dynamics $\varphi: S \to S$, and an observer $V \subsetneq S$ — a proper subsystem with finitely many distinguishable internal states, coupled to the complement $H = S \setminus V$ through $\varphi$.

This definition formalizes three features implicit in the concept of observation: there is a whole ($S$), the observer is not the whole ($V \subsetneq S$), and the observer registers changes (coupling through $\varphi$). From this definition, three structural properties follow.

**Lemma 1** (Finiteness). *The observer has finitely many distinguishable internal states, so the visible configuration space $\mathcal{C}_V$ is finite, with a discreteness scale $\epsilon$ providing a finite minimal cell volume.* Any observer bounded by a finite-area surface can couple to only finitely many modes across that boundary; independent support comes from holographic entropy bounds [27]. In Part I, $\epsilon$ is free; self-consistency (§6) pins $\epsilon = 2\,l_p$. The boundary-only dependence lemma (§5.2) shows that the cardinality of the deep hidden sector is gauge: no observable depends on it.

**Lemma 2** (Causal partition). *The observer is a proper subsystem: $V \subsetneq S$. The complement $H = S \setminus V$ is the hidden sector.* This partition is not a modeling choice but the definition of embedded observation: an observer that could access all of $S$ would have nothing external to observe. The product decomposition

$$\Gamma = \Gamma_V \times \Gamma_H, \qquad H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

follows, with cross-partition correlations entering only through $H_{\text{int}}$. The product decomposition is idealized; §4 and §9.6 address approximation quality and the conditions under which the sharp partition is exact.

**Lemma 3** (Determinism and unique measure). *$\varphi$ is a bijection: distinct states have distinct successors (determinism) and distinct predecessors (reversibility). The counting measure on $S$ is the unique $\varphi$-invariant measure.* Determinism (injectivity) is the requirement that the dynamics preserves the observer's records — non-injective evolution would merge distinct total states, erasing the distinction between outcomes the observer has already recorded. On a finite set, injectivity implies surjectivity, so $\varphi$ is a bijection. The invariant counting measure, in the continuum limit, becomes the Liouville measure on $\Gamma$:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\} \equiv \mathcal{L}\rho$$

These properties contain no quantum postulates. The claim is that quantum mechanics *emerges* under the conditions below.

### 1.3 Conditions on the Hidden Sector

**(C1) Non-zero coupling.** $H_{\text{int}} \neq 0$. The coupling is bidirectional.

**(C2) Slow-bath timescale separation.** The visible-sector (system) timescale $\tau_S$ is much shorter than the hidden-sector (bath) timescale $\tau_B$: $\tau_S \ll \tau_B$ — the *inverse* of the Markovian regime. The hidden sector evolves on timescales far exceeding those accessible to the observer.

**(C3) Sufficient capacity.** The number of hidden-sector degrees of freedom $N_H$ exceeds the number of visible-sector degrees of freedom $N_V$ by enough that visible-sector interactions do not appreciably perturb the hidden sector's state on timescales $\ll \tau_B$.

**Theorem statement.** Under Lemmas 1–3 and (C1)–(C3), the embedded observer's reduced description is mathematically equivalent to unitarily evolving quantum mechanics (defined precisely in §3.3). The conditions are not merely sufficient but *necessary* (§3.3), establishing full equivalence.

### 1.4 Partition-Relativity

**Lemma.** *The emergent description is uniquely determined by the partition. Any parameters of the emergent theory depend only on the geometric and thermodynamic properties of the partition boundary.*

*Proof.* By Lemma 3, the Hamiltonian flow $\phi_t$ is unique. By Lemma 2, the partition is fixed. By Lemma 3, the observer uses the Liouville measure $\mu$ — the unique absolutely continuous invariant measure on the full phase space. (An embedded observer with incomplete knowledge of the total energy averages over energies with a smooth prior, recovering Liouville on a phase-space band; singular invariant measures are excluded by Lemma 3.) Letting $\pi_V$ denote projection onto the visible sector, the marginalized transition probabilities

$$T_{ij}(t_2, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu(h)$$

are therefore uniquely determined by three inputs: dynamics ($\phi_t$), partition ($\Gamma_V, \Gamma_H$), and measure ($\mu$). Since $\phi_t$ and $\mu$ are fixed by the definition and lemmas, the stochastic process — and hence any emergent quantum description (§3.1) — depends only on the partition. $\square$

### 1.5 Epistemic Status of the Results

The results in this paper fall into three tiers of decreasing independence from auxiliary assumptions.

**Tier 1 (Part I, from the definition alone).** P-indivisibility of the reduced dynamics (§2.3), the characterization theorem establishing QM $\iff$ embedded observation under C1–C3 (§3.3), partition-relativity (§1.4), the deep-sector cardinality gauge corollary (§5.2), the consistency of nested trace-outs (Appendix B, Theorems B.1–B.4), the additive dissipator decomposition (B.5), the generalized second law (B.6), and the Page curve (B.7–B.9). These follow from Lemmas 1–3, the Stinespring construction, standard quantum information results, and Popescu-Short-Winter typicality [41]; disputing them requires finding a mathematical error.

**Tier 2 (Part II, given the cosmological realization).** The gap equation $\hbar = c^3 \epsilon^2 / (4G)$ (§5.2), the Bekenstein-Hawking entropy with the $1/4$ factor (§6), the CC dissolution identifying $10^{122}$ as $S_{\text{dS}}$ (§7), and the dark matter acceleration scale $a_0 = cH/6$ with the baryonic Tully-Fisher relation $v^4 = GM_B \cdot cH/6$ (§8.4). These require accepting that the cosmological horizon satisfies C1–C3, verified in §4.2.

**Tier 3 (consistency checks and solution-specific elements).** The dark-sector concordance (~95% of $\rho_{\text{crit}}$, §8.3), the dark energy parameter $\nu_{\text{OI}} = (2.45 \pm 0.04) \times 10^{-3}$ (§8.1; the spectral uniformity is derived from the lattice structure, reducing the systematic from a factor of $\sim 3$ to $\pm 1.4\%$), the GW echo timescale (§8.2), and the dark matter interpolation steepness (§8.4, Step 4). These are derived consequences or solution-specific elements; they would be falsified by observation but do not carry the same deductive weight as Tiers 1–2.

---

## 2. EMERGENT STOCHASTICITY AND P-INDIVISIBILITY

### 2.1 Emergent Stochasticity

The total system evolves deterministically, but the visible sector alone is stochastic. The observer knows $x$ but not $h$; different hidden states $h_k$ compatible with the same $x$ send it to different futures $x'_k$. Transition probabilities are obtained by marginalizing over the Liouville measure (§1.4). This makes the framework a hidden variable theory; consistency with Bell's theorem is addressed in §3.2.

### 2.2 The Slow-Bath Regime

The Markovian limit requires $\tau_B \ll \tau_S$ [4]. Condition (C2) inverts this: $\tau_S \ll \tau_B$. A slow bath must be distinguished from a static field. By (C1), coupling is continuously active: each visible-sector transition imprints on the hidden sector. Because the hidden sector is slow (not static), imprints persist without thermal overwriting. On subsequent transitions, coupling reads back stored correlations, producing history-dependent transition probabilities — the non-Markovian regime [4].

### 2.3 P-Indivisibility

By Lemma 1, the visible and hidden sectors have finite configuration spaces $\mathcal{C}_V$ and $\mathcal{C}_H$ (the discrete counterparts of $\Gamma_V$ and $\Gamma_H$). On these finite sets:

**Theorem.** *Let $\mathcal{C}_V$ and $\mathcal{C}_H$ be finite sets with $|\mathcal{C}_V| \geq 2$, and let $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ be a bijection. Define:*

$$T_{ij} = \frac{|\{h \in \mathcal{C}_H : \pi_V(\varphi(x_i, h)) = x_j\}|}{|\mathcal{C}_H|}$$

*and the $k$-step matrix $T^{(k)}_{ij}$ by applying $\varphi^k$. If $T$ is not a permutation matrix, then the process is P-indivisible.*

*Proof.* Uses total variation distance $d(p, q) = \frac{1}{2}\sum_k |p_k - q_k|$. P-divisibility $\iff$ $d(p(t), q(t))$ non-increasing for all initial $p, q$ [6, 7].

*Step 1 (Recurrence).* $\varphi$ bijective on a finite set $\Rightarrow$ $\exists N: \varphi^N = \text{id}$. Thus $T^{(N)} = I$ and $d(\delta_i T^{(N)}, \delta_j T^{(N)}) = 1$ for $i \neq j$.

*Step 2 (Strict contraction).* $T$ not a permutation $\Rightarrow$ $\exists i, j, l$: $T_{il} > 0$ and $T_{jl} > 0$. Then:

$$d(\delta_i T, \delta_j T) = \frac{1}{2}\sum_k |T_{ik} - T_{jk}| < 1$$

*Step 3.* $d(\delta_i T^{(1)}, \delta_j T^{(1)}) < 1 = d(\delta_i T^{(N)}, \delta_j T^{(N)})$: non-monotonic, hence P-indivisible. $\square$

The theorem requires only bijective dynamics (Lemma 3) and non-trivial coupling (C1). Lemma 1 guarantees the finite configuration space.

**Convergence with prior work.** The theorem converges with independent results: Pechukas [5] (reduced dynamics need not preserve positivity), Rivas et al. [6, 7] (divisibility failure ↔ information backflow), Pollock et al. [8] (process-tensor Markovianity conditions), and Strasberg and Esposito [9] (non-Markovian reduced dynamics in the slow-bath regime of C2). Bylicka, Johansson, and Acín [34] prove that for bijective dynamical maps — the class generated here — CP-divisibility and information backflow are equivalent, so the P-indivisibility established above implies CP-indivisibility directly. Milz et al. [35] further show that even CP-divisibility does not guarantee Markovianity in the process-tensor sense, confirming that the non-Markovian character identified here is robust under all current definitions.

**Continuous-time extension.** The Hamiltonian flow on finite-dimensional phase space preserves Liouville measure on compact energy surfaces. $T_{ij}(t)$ is continuous with $T(0) = I$. By (C1), $T(t)$ departs from the permutation class for $t > 0$. By Poincaré recurrence, $\exists t_R$: the set of hidden states with $\pi_V(\varphi_{t_R}(x_i, h)) = x_i$ has measure $> 1 - \delta$ for any $\delta > 0$. For small $\delta$, this gives non-monotonic trace distance, establishing P-indivisibility in continuous time.

The recurrence argument establishes P-indivisibility in principle. The following lemma shows that under (C2), information backflow occurs on observable timescales — not merely at Poincaré recurrence times.

**Lemma (Accessible-timescale backflow).** *Under (C1)–(C3) with $\tau_S \ll \tau_B$, the non-Markovian mutual information $I(X_{<t}; X_{>t} \mid X_t)$ is $\mathcal{O}(1)$ for observation windows $t \sim k\tau_S$ with $k\tau_S \ll \tau_B$.*

*Proof.* The coupling $H_{\text{int}}$ transfers visible-sector information to the hidden sector at each interaction, at rate $\sim 1/\tau_S$. Between interactions, the hidden sector evolves under $H_H$ with spectral gap $\Delta \sim 1/\tau_B$. The decay of correlations stored in the hidden sector is governed by $e^{-\Delta \tau_S}$. When $\tau_S \ll \tau_B$, $\Delta \tau_S \ll 1$, so the decay per visible-sector transition is $1 - e^{-\Delta \tau_S} \approx \Delta \tau_S \ll 1$: correlations survive each step essentially intact. After $k$ transitions spanning a time $k\tau_S \ll \tau_B$, the cumulative decay is $e^{-k\Delta\tau_S} \approx 1 - k\Delta\tau_S$, which remains close to unity. The hidden sector therefore retains $\sim k$ bits of visible-sector history over this window, and the $(k+1)$-th transition reads back stored correlations through $H_{\text{int}}$, producing history-dependent transition probabilities — i.e., information backflow. More precisely, the mutual information satisfies:

$$I(X_{<t}; X_{>t} \mid X_t) \geq I_0(1 - k\Delta\tau_S) = I_0\left(1 - \frac{k\tau_S}{\tau_B}\right)$$

where $I_0 > 0$ is the single-step information transfer from (C1). For $k\tau_S \ll \tau_B$, this remains $\mathcal{O}(I_0)$ — comparable to the single-step coupling strength, not exponentially suppressed. The bound saturates (C3): the maximum storable history is $\log_2 m$ bits (§3.3), so persistent backflow over $K$ transitions requires $m \geq 2^K$, which is amply satisfied when $N_H \gg N_V$. $\square$

**Role of (C2) and (C3).** The Poincaré recurrence argument and the accessible-timescale lemma are independent: the former establishes P-indivisibility from (C1) and finiteness alone; the latter shows that (C2) and (C3) promote it from a formal property to an observationally dominant one.

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

By Barandes' correspondence [10, 11], any P-indivisible stochastic process on a finite configuration space of size $n$ embeds into a unitarily evolving quantum system on $\mathcal{H}$ of dimension $\leq n^3$. P-indivisible transition matrices develop negative entries at fine time resolution; the Stinespring dilation theorem guarantees $\exists$ a Hilbert space and unitary $U(t)$ with $T_{ij}(t) = |U_{ij}(t)|^2$ — transition probabilities are exactly Born-rule probabilities. The proof requires a finite-dimensional configuration space (Lemma 1); Calvo [12] extends the correspondence to infinite dimensions, but this is not required here. Pimenta [25] distinguishes P-divisible and P-indivisible stochastic-quantum dynamics: the correspondence is non-trivial only in the P-indivisible regime, which is precisely the regime produced by §2.3. An independent derivation using only Stinespring's dilation theorem [32] and standard partial-trace properties [33] is given in Appendix A; either route alone suffices.

**From phase space to configuration space.** The transition probabilities $T_{ij}$ are projections of the full phase-space flow onto the configuration sector of $\Gamma_V$, with momenta and hidden-sector degrees of freedom absorbed into the Liouville marginalization. The resulting process lives on the discrete configuration space of Lemma 1.

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

Conditions (G1)–(G3) fail only on a measure-zero set of Hamiltonians. For the cosmological realization, a stronger argument applies. The genericity conditions concern the *effective* visible-sector Hamiltonian $\hat{H}_{\text{eff}}$ — the operator emerging after the trace-out — not the total Hamiltonian $H_{\text{tot}}$. The trace-out generically breaks the symmetries of $H_{\text{tot}}$, because the partition boundary does not respect them: the cosmological horizon is centered on a specific observer, breaking translational invariance, rotational symmetry about distant points, and boost invariance. Any degeneracy in $H_{\text{tot}}$ that relies on correlations between visible and hidden sectors — which includes all degeneracies associated with symmetries the partition breaks — is lifted in $\hat{H}_{\text{eff}}$. The residual degeneracies of $\hat{H}_{\text{eff}}$ are those associated with symmetries acting entirely within the visible sector that commute with the trace-out: precisely the gauge symmetries of the emergent QFT. Gauge degeneracies correspond to physically equivalent states and do not affect the phase-locking argument, which operates on gauge-inequivalent transition data. The cosmological $\hat{H}_{\text{eff}}$ therefore satisfies G1–G3 not by typicality in an abstract ensemble, but because the partition itself acts as a symmetry-breaking mechanism.

### 3.2 Bell Inequality Violations

The framework is a hidden variable theory evading Bell's theorem [13] not by superdeterminism but by violating factorizability through P-indivisible joint dynamics — while remaining causally local. Two subsystems interacting at preparation carry a joint transition matrix $T_{QR} \neq T_Q \otimes T_R$. This non-factorizability *is* stochastic entanglement [10, 11, 14]. Since the process is indivisible, no well-defined intermediate conditional probabilities permit Bell's factorization.

In the Jarrett decomposition, the framework violates outcome independence while preserving parameter independence and measurement independence — precisely the class Fine's theorem [24] permits. Barandes, Hasan, and Kagan [14] prove the maximum CHSH correlator is exactly Tsirelson's bound $2\sqrt{2}$, with independent support from Le et al. [15]. The bound also follows from the Stinespring route: Appendix A establishes full unitary QM on a tensor-product Hilbert space, from which Tsirelson's original operator-norm argument [36] yields $|\langle S \rangle| \leq 2\sqrt{2}$; achievability follows because all quantum states, including maximally entangled ones, are realizable in the emergent description.

**Fine-tuning and causal structure.** The framework does not claim to restore Bell locality: outcome independence is genuinely violated. What it provides is a *derivation* of this nonlocality from the causal partition, rather than treating it as axiomatic. The fine-tuning objection (Wood and Spekkens, 2015) assumes DAG causal structure with Markov factorization; P-indivisible processes violate the Markov condition on any DAG, so the appropriate framework is the process tensor [8], within which no-signaling follows from marginalization structure without fine-tuning.

**Parameter independence from spatial locality.** Let $V_A$ and $V_B$ be space-like separated visible-sector subsystems with disjoint coupling neighborhoods on $G_\varphi$. The spatial Markov property of range-1 dynamics (Fundamental, §5, area-law lemma) makes $V_A$ and $V_B$ conditionally independent given boundary data. Alice's measurement setting $a$ determines which function she evaluates on $V_A$; it does not alter the transition probabilities for $V_B$, which depend only on $V_B$'s local coupling neighborhood. Hence $P(x_B \mid a, b) = P(x_B \mid b)$ — parameter independence holds structurally for all bounded-degree graph topologies with range-1 coupling, with no fine-tuning of the hidden-variable distribution. Combined with the outcome-independence violation from stochastic entanglement, this gives the precise Jarrett decomposition.

### 3.3 The Characterization Theorem: Necessity of the Conditions

The logical structure: Barandes' correspondence gives QM $\iff$ P-indivisibility. What remains is P-indivisibility $\implies$ embedded observation under (C1)–(C3).

**Dilation existence.** Any stochastic process on a finite configuration space can be realized as marginalization of a deterministic process on a larger state space — furnishing Lemmas 1–3.

**Theorem (C1 equivalence).** *The marginalized process is P-indivisible iff $T$ is not a permutation matrix.*

*Proof.* Forward: §2.3. Reverse: if $T$ is a permutation, $\Lambda(k_2, k_1) = T^{(k_2-k_1)}$ is a valid stochastic matrix for all $k_2 > k_1$ $\Rightarrow$ P-divisible. $\square$

**Theorem (C2 necessity).** *In the fast-bath regime ($\tau_B \ll \tau_S$), ergodic mixing drives the hidden sector to uniformity before each coupling event, yielding a Markov chain ($T^{(k)} = T^k$), which is P-divisible. Contrapositively, P-indivisibility requires $\tau_S \ll \tau_B$.*

*Proof.* Between coupling events (separated by $\tau_S$), the hidden sector evolves under its own Hamiltonian $H_H$. Let $\mathcal{L}_H$ denote the hidden-sector Liouvillian with spectral gap $\Delta > 0$ (guaranteed on a finite ergodic system). For any conditioned hidden-sector distribution $\mu_H(\cdot | x_i)$ at a coupling event:

$$\| e^{\mathcal{L}_H \tau_S} \mu_H(\cdot | x_i) - \mu_{\text{eq}} \|_{\text{TV}} \leq C \, e^{-\Delta \tau_S}$$

In the fast-bath regime ($\Delta \tau_S \gg 1$), this is exponentially small: the hidden sector relaxes to equilibrium $\mu_{\text{eq}}$ before each coupling event regardless of its post-coupling state. Each single-step transition matrix $T$ is therefore computed against the same equilibrium distribution, so $T^{(k)} = T^k$ — a homogeneous Markov chain, hence P-divisible.

Contrapositively: P-indivisibility requires $\Delta \tau_S \lesssim 1$, i.e., $\tau_S \lesssim \tau_B$. For the strong, persistent P-indivisibility of the characterization theorem, the separation must be $\tau_S \ll \tau_B$. (The proof uses discrete coupling events; for continuous Hamiltonian flow, $\tau_S$ is the visible sector's dynamical timescale and $\Delta$ is the spectral gap of $\mathcal{L}_H$. The continuous-time extension replaces the collision-model structure with the continuous spectral condition $\Delta \tau_S \gg 1 \Rightarrow$ Markovian, established in [4, 9].) $\square$

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

*(ii) Tensor product structure (visible-sector subsystems).* Spatially separated subsystems within the visible sector — e.g., two laboratories — correspond to subsets $V_A, V_B \subset V$ with disjoint coupling neighborhoods on the coupling graph (Fundamental, §3). The spatial Markov property of range-1 dynamics (Fundamental, §5, area-law lemma) guarantees conditional independence: $\rho_{AB} = \rho_A \otimes \rho_B$ conditioned on boundary data. The emergent Hilbert space inherits the factorization $\mathcal{H}_{V_A} \otimes \mathcal{H}_{V_B}$ from the locality of the coupling graph, with entanglement between $A$ and $B$ arising from shared boundary history — precisely the stochastic entanglement of [10, 14].

*(iii) State update, measurement, and multi-time predictions.* Projective measurement in the emergent description corresponds to conditioning on a visible-sector outcome and re-marginalizing over the hidden sector. The Lüders rule $\rho \to P_k \rho P_k / \text{Tr}(P_k \rho)$ is the quantum transcription of Bayesian updating on the classical substratum (Lemma 3). No independent measurement postulate is required. Multi-time correlation functions, weak values, and Leggett-Garg inequalities are standard calculations within the delivered formalism ($\mathcal{H}_V$, $U(t)$, Born rule); they require no additional postulates beyond what the characterization theorem provides.

*(iv) Classical non-Markovianity and quantum mechanics.* The equivalence is not a claim that all P-indivisible processes are "secretly quantum" in some metaphysical sense; it is a theorem that the mathematical structures are identical. Classical systems exhibiting P-indivisibility — renewal processes, semi-Markov processes on finite state spaces — admit a unique unitary description (phase-locking lemma) that makes predictions beyond the transition data (energy eigenvalues, interference, entanglement), and can be realized as marginalization of deterministic dynamics under C1–C3 (necessity theorems). The framework does not distinguish "classical non-Markovian" from "quantum" — it proves they are the same category. The physical content of the unitary is not that of a mere mathematical embedding: it is the *specific* Hamiltonian uniquely determined by the transition data, arising from the *actual* dilation structure of the system (Appendix A).

---

# PART II: THE COSMOLOGICAL APPLICATION

## 4. THE COSMOLOGICAL HORIZON AS CAUSAL PARTITION

### 4.1 The Partition

The cosmological horizon — the boundary beyond which no signal propagating at or below $c$ can reach the observer — implements the causal partition of Lemma 2: $\Gamma_V$ is the interior, $\Gamma_H$ everything beyond. This is a consequence of GR's causal structure, not a modeling choice. The universality of the observed quantum mechanics follows from all sub-$c$ observers sharing the same causal structure.

Different observers have different horizon areas (hence different $S_{\text{dS}}$), but $\hbar = c^3 \epsilon^2/(4G)$ depends only on local geometric quantities — not on the observer's worldline or horizon area — so all observers share the same emergent action scale.

### 4.2 Verification of the Conditions

**(C1)** In the ADM formulation, the bulk Hamiltonian is a sum of constraints that vanish on-shell; physical time evolution is generated by the boundary term at the horizon, which depends on data from both sides. The Hamiltonian and momentum constraints further correlate interior and exterior initial data on any Cauchy surface, so the physical phase space is a constraint surface within the kinematic product $\Gamma_V \times \Gamma_H$ (see §9.6 for implications). This is *stronger* than the $H_{\text{int}} \neq 0$ required by Lemma 2: constraints enforce correlations that persist on all timescales and cannot be perturbatively removed. **Satisfied.**

**(C2)** $\tau_B \gtrsim 1/H \sim 10^{17}$ s; for laboratory processes, $\tau_S \sim 10^{-15}$ s. Ratio: $\tau_S / \tau_B \sim 10^{-32}$. **Satisfied.**

**(C3)** Hidden sector has $A/\epsilon^2$ modes with $A \sim 10^{52}$ m$^2$; visible sector has $\sim 10^{80}$ baryons. No laboratory process saturates the hidden sector. **Satisfied.**

### 4.3 Application

Lemma 1 is now a consequence of partition geometry: the horizon has finite area $A = 4\pi c^2/H^2$, bounding coupled modes to $A/\epsilon^2 < \infty$. The Part I theorem applies: the observer's reduced description is P-indivisible and, by Barandes' correspondence, equivalent to unitary QM with $\hbar$ determined by the partition boundary.

---

## 5. DERIVATION OF THE EMERGENT ACTION SCALE ($\hbar$)

### 5.1 The Classical Horizon Temperature

Jacobson [16] showed $dE = T\,dS$ applied to local causal horizons yields Einstein's equations, with $dE = (c^2 \kappa / 8\pi G)\,dA$, where $\kappa$ is the surface gravity of the horizon. The entropy density is $\eta = 1/\epsilon^2$ — one coupled mode per minimal cell. This is not an assumption about the number of states per cell but a consequence of two results: $\epsilon$ is defined as the minimal distinguishable scale (Lemma 1), so each cell of area $\epsilon^2$ contributes exactly one boundary mode that couples across the partition; the number of internal states per mode (the alphabet size $q$) is a gauge freedom with no observable consequences (Fundamental, §4). Thus $dS = dA/\epsilon^2$. Equating:

$$T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G k_B}$$

For de Sitter ($\kappa = cH$): $k_B T_{\text{cl}} = c^3 \epsilon^2 H / (8\pi G)$. No $\hbar$ appears.

### 5.2 The Emergent Action Scale

**Step 1: Uniqueness.** By partition-relativity (§1.4), $\hbar$ is derived, not free.

**Step 2: $\hbar$ is structural, not volumetric.**

**Lemma (Boundary-only dependence).** *Decompose the hidden sector as $\mathcal{C}_H = \mathcal{C}_B \times \mathcal{C}_D$, where $\mathcal{C}_B$ denotes boundary modes (within the interaction range of $H_{\text{int}}$) and $\mathcal{C}_D$ denotes deep modes (the remainder of the hidden sector). If the classical Hamiltonian is spatially local, then on timescales $t \ll \tau_B$:*

$$T_{ij}(t) = T^{(B)}_{ij}(t) + \mathcal{O}(t/\tau_B)$$

*where $T^{(B)}_{ij}$ depends only on the $V$-$B$ dynamics.*

*Proof.* (i) *Coupling structure.* Spatial locality of the classical Hamiltonian implies the interaction decomposes as $H_{\text{tot}} = H_V + H_B + H_D + H_{VB} + H_{BD}$, with no direct $V$-$D$ coupling: a deep hidden-sector mode must propagate through the boundary layer before influencing the visible sector. The coupling chain is $V \leftrightarrow B \leftrightarrow D$, not $V \leftrightarrow D$.

(ii) *Frozen deep sector.* Let $\Delta_D$ be the spectral gap of $H_D + H_{BD}$ restricted to the deep sector conditioned on a fixed boundary configuration. The deep-sector evolution over time $t$ displaces any initial configuration by $\mathcal{O}(\Delta_D \, t)$ in phase space. The spectral gap gives the inverse relaxation time of the slowest mode, so $\Delta_D \leq 1/\tau_B$ (with equality when the slowest mode dominates the relaxation). For $t \ll 1/\Delta_D \leq \tau_B$: $\|\varphi_t^D - \text{id}\| = \mathcal{O}(\Delta_D \, t) = \mathcal{O}(t/\tau_B)$.

(iii) *Factorization of the Liouville integral.* The transition probability is:

$$T_{ij}(t) = \frac{1}{|\mathcal{C}_B||\mathcal{C}_D|} \sum_{b \in \mathcal{C}_B} \sum_{d \in \mathcal{C}_D} \delta_{x_j}[\pi_V(\varphi_t(x_i, b, d))]$$

By (i), $\pi_V(\varphi_t(x_i, b, d))$ depends on $d$ only through the back-reaction $B \leftarrow D$, which by (ii) shifts $b$ by $\mathcal{O}(t/\tau_B)$. Expanding:

$$\pi_V(\varphi_t(x_i, b, d)) = \pi_V(\varphi_t^{VB}(x_i, b)) + \mathcal{O}(t/\tau_B)$$

where $\varphi_t^{VB}$ is the flow restricted to $V \times B$ with $D$ frozen. The $d$-sum then contributes $|\mathcal{C}_D|$ identical terms at leading order:

$$T_{ij}(t) = \underbrace{\frac{1}{|\mathcal{C}_B|} \sum_{b \in \mathcal{C}_B} \delta_{x_j}[\pi_V(\varphi_t^{VB}(x_i, b))]}_{T^{(B)}_{ij}(t)} + \mathcal{O}(t/\tau_B) \qquad \square$$

The correction is $\mathcal{O}(t/\tau_B) \sim 10^{-32}$ for laboratory processes. Since $T_{ij}(t)$ determines the emergent quantum description (§3.1), and $T^{(B)}_{ij}(t)$ depends only on the $V$-$B$ dynamics — which are characterized by the boundary geometry ($A$, $\epsilon$, $\kappa$) and the constants $c$, $G$ appearing in the classical Hamiltonian — the emergent action scale $\hbar$ inherits boundary-only dependence.

**Corollary (deep-sector cardinality is gauge).** *No observable of the emergent description — no transition probability, emergent Hamiltonian eigenvalue, or scattering amplitude — depends on the cardinality $|\mathcal{C}_D|$ of the deep hidden sector. Systems with the same $\mathcal{C}_V \times \mathcal{C}_B$ dynamics produce the same emergent physics to within $\mathcal{O}(\tau_S/\tau_B)$, whether $|\mathcal{C}_D|$ is finite, countably infinite, or uncountably infinite.*

*Proof.* $T^{(B)}_{ij}(t)$ is defined by a sum over $\mathcal{C}_B$ alone. The $\mathcal{C}_D$-dependent terms enter only through the $\mathcal{O}(t/\tau_B)$ back-reaction. Since the emergent Hamiltonian $\hat{H}_{\text{eff}}$ is uniquely determined by $\{T_{ij}(t)\}$ (phase-locking lemma, §3.1; D-gauge theorem, §5.3), it inherits $\mathcal{C}_D$-independence at leading order. All observables — eigenvalues, transition amplitudes, scattering cross-sections — are functions of $\hat{H}_{\text{eff}}$ and therefore $\mathcal{C}_D$-independent. $\square$

The cardinality of the deep hidden sector is gauge in the same technical sense as the alphabet size $q$ (Fundamental, §4): just as two systems with different $q$ are physically equivalent if they share the same coupling structure, two systems with different $|\mathcal{C}_D|$ are physically equivalent if they share the same $\mathcal{C}_V \times \mathcal{C}_B$ dynamics. Lemma 1 requires $S$ finite for the recurrence proof (§2.3); the corollary establishes that the deep sector's contribution to this finiteness has no observable consequences. The question "is the universe finite or infinite?" has no empirical content within the framework — it is identified as gauge.

**Step 3: Dimensional determination.** Step 2 excludes volumetric (deep-sector) quantities, leaving boundary quantities. The boundary carries both *local* geometric data ($\epsilon$, $\kappa$, and the constants $c$, $G$ of the classical Hamiltonian) and a *global* quantity: the total area $A$, which forms the dimensionless ratio $A/\epsilon^2 = S_{\text{dS}}$. If $\hbar$ depended on $S_{\text{dS}}$, it would be observer-dependent — different observers have different horizon areas (§4.1) — contradicting the universality of the emergent action scale. (All sub-$c$ observers share the same local physics and hence the same $\hbar$; §4.1.) This excludes $A$, leaving the local boundary quantities $c$, $G$, $\epsilon$, and $\kappa$. The surface gravity $\kappa$ is excluded by two independent arguments: (i) $\kappa$ differs between horizon types (cosmological vs. black hole), but $\hbar$ is universal — a laboratory experiment measures the same $\hbar$ regardless of which horizon defines the partition; (ii) for the cosmological horizon, $\kappa = cH$ is time-dependent ($\dot{H} \neq 0$), but $\hbar$ is observed to be constant on laboratory timescales. The unique combination of $c$, $G$, $\epsilon$ with dimensions of action:

$$\hbar = \beta \frac{c^3 \epsilon^2}{G}$$

**Step 4: Thermal self-consistency.** The classical substratum assigns the partition boundary a temperature $k_B T_{\text{cl}} = c^2 \epsilon^2 \kappa / (8\pi G)$ (§5.1), containing no $\hbar$. The emergent QFT of Part I lives on this classical background, which has a bifurcate Killing horizon with surface gravity $\kappa$. Regularity of the Wick-rotated metric at the horizon requires Euclidean period $\beta = 2\pi c / \kappa$; any QFT on this background — including a lattice-regularized one — must therefore be periodic in imaginary time with the same period, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$, with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import. The two temperatures are computed independently — $T_{\text{cl}}$ from the classical substratum alone (no QM), $T_Q$ from the emergent QFT alone (no classical substratum details) — but they describe the same physical degrees of freedom: the boundary modes across which the partition is defined. Since the quantum description is derived from the classical one (Part I), and the derivation is exact at the boundary (Step 2's correction is $\mathcal{O}(\tau_S/\tau_B) \sim 10^{-32}$), the two descriptions cannot assign contradictory temperatures to the same boundary. Consistency requires $T_{\text{cl}} = T_Q$:

$$\frac{c^2 \epsilon^2 \kappa}{8\pi G} = \frac{\hbar \kappa}{2\pi c}$$

$\kappa$ cancels (confirming the structural/volumetric distinction). Solving:

$$\boxed{\hbar = \frac{c^3 \epsilon^2}{4G}}$$

The derivation is a gap equation: $\epsilon$ is the free geometric input, $\hbar$ is the output. The match is non-trivial: $T_{\text{cl}}$ could have depended on volumetric hidden-sector data (excluded by Step 2), or $T_Q$ could have depended on the state (it does not — the KMS temperature is purely kinematic). That neither pathology obtains makes the gap equation a genuine determination. The non-circularity is structural: Part I establishes that a QFT emerges with *some* action scale $\hbar$; §5 determines *which* $\hbar$, using the independent classical temperature that Part I neither requires nor produces.

**Non-circularity of the entropy density.** The claim $\eta = 1/\epsilon^2$ — one mode per minimal cell — may appear to pre-bake the area-entropy proportionality. To see why it does not, consider the counterfactual: suppose the classical entropy density were $\eta = \alpha/\epsilon^2$ for arbitrary $\alpha > 0$. Then $T_{\text{cl}} = \alpha c^2 \epsilon^2 \kappa / (8\pi G k_B)$, and thermal matching gives $\hbar = \alpha c^3 \epsilon^2 / (4G)$. The Bekenstein-Hawking entropy becomes $S = A / (4\alpha^{-1} l_p^2)$, which reproduces the observed $1/4$ factor only for $\alpha = 1$. Thus $\alpha = 1$ is a non-trivial constraint — it says that each minimal cell contributes exactly one boundary mode, not a fractional or multiple contribution. This is the physical content of the $q$-gauge theorem (Fundamental, §4): the alphabet size $q$ (the number of internal states per cell) is observationally irrelevant, so what counts is the number of *cells*, not the number of *states*. The counting $\eta = 1/\epsilon^2$ is not an assumption about mode density but a consequence of $\epsilon$ being defined as the minimal distinguishable scale (Lemma 1) combined with the irrelevance of sub-cell structure.

The predictive content lies not in the gap equation alone but in its consequences. The specific relationship $\hbar = c^3\epsilon^2/(4G)$ — rather than any other function of $c$, $G$, $\epsilon$ — produces: the Bekenstein-Hawking formula with the exact factor $1/4$ (§6), the CC dissolution with $S_{\text{dS}}$ as the compression ratio (§7.3), the RVM parameter $\nu_{\text{OI}}$ (§8.1), and the GW echo timescale (§8.2). Any alternative $\hbar(\epsilon)$ would fail at least one of these checks. The situation is analogous to deriving the Schwarzschild metric with $M$ as a free parameter: the derivation has genuine content (the functional form) even though one input is not determined from within.

Jacobson's original derivation [16] uses $\hbar$-containing forms; this paper does not — it uses the classical identity $dE = (c^2 \kappa / 8\pi G)\,dA$ and the classical entropy density $\eta = 1/\epsilon^2$. The logical ordering differs from Jacobson's: his argument derives $G$ from $\eta$ and $\hbar$; the present argument takes $G$ as a parameter of the classical Hamiltonian (Lemma 3) and derives $\hbar$ from $G$ and $\epsilon$. The two are consistent — substituting $\eta = 1/\epsilon^2$ and $\hbar = c^3\epsilon^2/(4G)$ into Jacobson's formula $G_{\text{eff}} = c^4/(8\pi \eta \cdot \hbar c)$ recovers $G_{\text{eff}} = G$ — but the roles of input and output are reversed. The Gibbons-Hawking temperature [17] $k_B T_{\text{GH}} = \hbar \kappa / (2\pi c)$ is recovered as a prediction, not used as an input. The KMS condition used above is derived for continuum QFT on bifurcate Killing horizons; for the lattice-regularized theory emerging from Part I, the relevant result is that thermal periodicity of the Euclidean Green's functions is robust against UV modifications of the dispersion relation, with corrections at $\mathcal{O}((\epsilon \kappa/c)^2)$ [28, 29]. For the cosmological horizon, $\epsilon \kappa / c = \epsilon H / c \sim 10^{-61}$, so lattice corrections are $\sim 10^{-122}$.

### 5.3 Gauge-Fixing and the Dimensional Obstruction

Steps 1–2 establish that $\hbar$ depends only on boundary quantities; Step 4 will fix its value via thermal matching. A prior question must be addressed: does the transition-probability data $\{T_{ij}(t)\}$ determine the emergent Hamiltonian uniquely, or does residual gauge freedom leave $\hbar$ underdetermined? The following theorem, completing the phase-locking argument of §3.1, shows the gauge freedom is physically trivial.

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

**Remark (phase recovery under discrete sampling).** The spatial lattice discreteness does not discretize time: the continuous-time extension (§2.3) provides $T_{ij}(t)$ as a genuinely continuous function of $t$ via the Liouville marginalization of the Hamiltonian flow (Lemma 3). The D-gauge theorem therefore applies to the continuous object without aliasing corrections. Aliasing would arise only if the observer sampled $T_{ij}$ at discrete intervals, in which case trans-Planckian frequencies could be misidentified — but these lie outside the emergent QFT's domain. The phase-recovery error is controlled by the same $\mathcal{O}(\tau_S/\tau_B) \sim 10^{-32}$ suppression that governs the boundary-only dependence of §5.2.

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

**From finite-dimensional QM to QFT.** Part I delivers QM on a finite-dimensional Hilbert space. The $N = A/\epsilon^2$ cells discretize the visible sector; spatial locality of the classical substratum restricts which cells interact on any given timescale. The emergent Hilbert space decomposes as $\mathcal{H} = \bigotimes_k \mathcal{H}_k$ — a lattice-regularized QFT with UV cutoff at $\epsilon = 2\,l_p$. The tensor product structure follows from the spatial product structure of the classical configuration space $\mathcal{C}_V = \mathcal{C}_1 \times \cdots \times \mathcal{C}_N$ (one factor per cell), which is not required by Lemma 1 but is a consequence of spatial locality in the classical substratum: each cell's configuration is a local degree of freedom.

**Locality preservation theorem.** *If the classical Hamiltonian is spatially local (couples only neighbors), then the emergent quantum Hamiltonian inherits spatial locality.*

*Proof.* For infinitesimal $dt$ and $x' \neq x$: $T_{x,x'}(dt) = |\langle x'|\hat{H}|x\rangle|^2\,dt^2 + O(dt^3)$. If $x, x'$ differ at non-neighboring sites, spatial locality of the classical dynamics gives $T_{x,x'}(dt) = 0$ at leading order, hence $|\langle x'|\hat{H}|x\rangle|^2 = 0$. By the D-gauge theorem (§5.3), the residual phase freedom is a diagonal unitary $D$ that preserves the vanishing of off-diagonal moduli, so $\langle x'|\hat{H}|x\rangle = 0$ in any gauge. The emergent Hamiltonian has the form $\hat{H} = \sum_k \hat{h}_k + \sum_{\langle k,l\rangle} \hat{h}_{kl}$. $\square$

**Scope of the emergent QFT.** The CC dissolution requires only that the emergent description assigns zero-point energy $\sim \hbar\omega/2$ per mode with UV cutoff at $\epsilon^{-1}$ — a property shared by any lattice QFT with local couplings, regardless of gauge group or matter content. The framework's predictions in Part II ($\hbar$, $S_{\text{dS}}$, $\nu_{\text{OI}}$) depend on partition geometry, not on the emergent field content.

**Classical substratum** (what geometric measurements probe): The horizon has classical thermal equilibrium. By the Friedmann equation, $\rho_{\text{crit}} = 3H^2 c^2/(8\pi G)$. No zero-point energy, no discrepancy. Total vacuum energy density: $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$ — precisely observed.

**Emergent QFT** (what local quantum measurements probe): Zero-point energy $\frac{1}{2}\hbar\omega$ per mode summed to the Planck cutoff gives $\rho_{\text{QFT}} \sim 10^{113}$ J/m$^3$ — a $\sim 10^{122}$ discrepancy with the observed value [2, 3, 18].

### 7.2 Why Gravity Sees the Classical Value

Spacetime geometry is part of the classical substratum (Lemma 2): the metric evolves via Einstein's equations *before* the trace-out. The stress-energy sourcing gravity is the classical stress-energy of the total microstate, not the expectation value of an emergent quantum operator. The semiclassical equation $G_{\mu\nu} = 8\pi G \langle \hat{T}_{\mu\nu} \rangle$ is itself an emergent approximation; at the classical level, the gravitational field equations never encounter the zero-point sum.

**Ontological commitment.** Classical spacetime is fundamental; QM is emergent. This ordering is not a modeling choice but is forced by the logical structure of the derivation through three independent requirements:

*(i) Definiteness.* The trace-out that produces QM is defined by a *specific* partition $\Gamma = \Gamma_V \times \Gamma_H$. The partition must be definite — not in superposition, not subject to quantum uncertainty — for the marginalization integral (§1.4) to be well-defined. A partition in superposition would yield an incoherent mixture of inequivalent quantum theories, not a single QM. The metric at the partition boundary must therefore be classical.

*(ii) Non-circularity.* The partition is defined by the causal structure: $\Gamma_H$ is the set of degrees of freedom beyond the observer's causal reach (§4.1). Causal structure is determined by null geodesics of the metric. If the metric were derived from QM, then the derivation would require: QM $\to$ metric $\to$ causal structure $\to$ partition $\to$ QM — a circular dependency with no entry point. The circle breaks only if the metric exists prior to the partition.

*(iii) Uniqueness of $\hbar$.* The emergent action scale is determined by the boundary geometry (§5.2). If the geometry were itself quantum-mechanical, $\hbar$ would depend on a quantum state — but $\hbar$ is state-independent by observation. The geometry-first ordering is the only one consistent with a universal $\hbar$.

Any framework in which QM is logically prior to the metric must either (a) treat the zero-point sum as a gravitational source — producing the $10^{122}$ discrepancy requiring cancellation or fine-tuning — or (b) invoke an independent mechanism to decouple quantum vacuum energy from gravity. In the present framework, the zero-point sum is an artifact of the emergent description and never enters the stress-energy tensor; no decoupling mechanism is needed.

**Cumulative evidence for the ordering.** The geometry-first ordering produces twelve independent consequences that match observation, none of which were designed into the starting point: (1) the CC dissolution — the observed vacuum energy sits at $\rho \sim H^2/G$, the classical baseline, without fine-tuning (§7.3); (2) the Bekenstein-Hawking formula including the $1/4$ factor, derived from $\epsilon = 2\,l_p$ (§6); (3) the value of $\hbar$, determined by partition geometry rather than treated as a free parameter (§5.2); (4) the dark-sector concordance — ~95% of $\rho_{\text{crit}}$ is invisible to QFT, matching the observed dark sector (§8.3); (5) dark energy evolution with $\nu_{\text{OI}}$ in the range consistent with DESI data (§8.1); (6) a testable GW echo prediction at the discreteness scale (§8.2); (7) the MOND acceleration scale $a_0 = cH/6$ and the baryonic Tully-Fisher relation, derived from entropy displacement (§8.4); (8) the SM gauge group with its coupling strengths, reproduced to $< 0.1\%$ at $M_Z$ (Fundamental, §9); (9) declining rotation curves at high redshift, confirmed by Genzel et al. (§8.4); (10) $\bar{\theta} = 0$ at all energy scales (Fundamental, §8); (11) galaxy cluster masses matched by the simple interpolation function (§8.4); (12) the Bullet Cluster lensing morphology reproduced by frozen boundary entropy (§8.4). Quantum-first orderings produce the $10^{122}$ discrepancy, have no natural account of the dark sector, and treat $\hbar$ and the $1/4$ factor as unexplained inputs. The cumulative case is not a single tiebreaker but a pattern: every quantitative output of the geometry-first ordering is consistent with observation; the central quantitative output of the quantum-first ordering is the worst prediction in physics.

**The classical vacuum energy scale.** The framework does not explain *why* $\rho \sim H^2/G$; this is set by initial conditions via the Friedmann equation. What it does is reclassify the CC puzzle: from quantum vacuum cancellation to classical initial conditions. The two problems are not equivalent. The QFT CC problem requires a cancellation between independent contributions — the bare cosmological constant and the zero-point energies of every field — accurate to 122 decimal places, re-tuned at each order in perturbation theory. The initial-conditions question asks why a single parameter ($\Lambda$, or equivalently $H$) takes its observed value; the scale $\rho \sim H^2/G$ is the natural energy density of classical cosmology, not a fine-tuned cancellation between unrelated quantities. The framework eliminates the 122-digit cancellation entirely; the remaining question — why $H$ takes its value — is a standard cosmological problem addressable by inflationary dynamics or other initial-conditions mechanisms.

**Quantum corrections to gravity.** The emergent quantum description does feed back into gravitational dynamics through state-level quantities: §8.1 derives dark energy evolution because the emergent vacuum energy depends on $H$ through the hidden sector's volume. What the framework excludes is the zero-point sum as a gravitational source. The zero-point energy is the ground-state eigenvalue of the emergent Hamiltonian $\hat{H}_{\text{eff}}$, which acts on $\mathcal{H}_V$. But gravity is sourced by the classical Hamiltonian $H_{\text{tot}}$, which acts on the full phase space $\Gamma$ — and $\hat{H}_{\text{eff}}$ and $H_{\text{tot}}$ are not the same operator. The eigenvalues of $\hat{H}_{\text{eff}}$ (including the zero-point energy) are properties of the *emergent description*; the energy that $H_{\text{tot}}$ assigns to the corresponding classical microstates is the *classical vacuum energy* $\rho \sim H^2/G$. The Equivalence Principle applies to $H_{\text{tot}}$: everything that contributes to $H_{\text{tot}}$ gravitates. The zero-point sum does not contribute to $H_{\text{tot}}$; it appears when the classical transition probabilities are reorganized into the Hilbert space formalism (§3.1), not when the classical dynamics is evolved. The structural/volumetric distinction of §5.2 captures this: $\hbar$ (structural, a property of the correspondence) does not gravitate; the vacuum energy (volumetric, state-dependent, a property of $H_{\text{tot}}$) does, but at the classical scale $\rho \sim H^2/G$ rather than $\rho \sim M_{\text{Pl}}^4$.

### 7.3 The Structural Origin of the $10^{122}$ Discrepancy

$\rho_{\text{QFT}} / \rho_{\text{classical}} \sim M_{\text{Pl}}^4 / (H^2/G) = S_{\text{dS}} = A/(4\,l_p^2)$ — the Bekenstein-Hawking entropy, now identified as the information compression ratio of the trace-out. The "worst prediction in physics" is the entropy of the observer's blind spot — a category error, not a fine-tuning failure. Wolpert's limits of inference [19] confirm this cannot be resolved from within: both geometric and quantum measurements are faithful to their respective descriptions, and no embedded observer can determine which is more fundamental. This is not a prediction awaiting future data — the observed vacuum energy sits at the classical geometric scale $\rho \sim H^2/G$, the value the framework expects.

---

## 8. PREDICTIONS AND TESTS

### 8.1 Dark Energy Evolution in Running Vacuum Form

$\hbar$ is $H$-independent (§5.2), but the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume. Expanding $\Lambda_{\text{eff}}(H)$:

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu_{\text{OI}}}{8\pi G}(H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

This is the Running Vacuum Model [20, 21]. The $S_{\text{dS}}$ horizon modes span frequencies $\omega_{\text{IR}} = H$ to $\omega_{\text{UV}} = c/\epsilon$. The spectral density of boundary entropy is uniform in $\ln\omega$: each ε² boundary cell is one degree of freedom that couples to the bulk at all frequencies (time-translation invariance of the wave equation), and each mode carries $\mathcal{O}(1)$ entropy bit (quantum regime: $\omega \gg T_{\text{dS}}$ for all modes). The number of independent spectral channels is $\mathcal{N}(H) = \ln(c/\epsilon H)$. Each carries fraction $1/\mathcal{N}$ of the total gravitating vacuum energy, so $\rho_\Lambda \propto 1/\mathcal{N}$. Taylor-expanding:

$$\boxed{\nu_{\text{OI}} = \frac{\Omega_\Lambda}{2\,\ln(c/\epsilon H_0)} = (2.45 \pm 0.04) \times 10^{-3}}$$

With $\epsilon = 2\,l_p$, $H_0 = 67.4$ km/s/Mpc, $\Omega_\Lambda = 0.685$. The uncertainty has two components: parametric ($\pm 0.03 \times 10^{-3}$ from $H_0$ and $\Omega_\Lambda$, at $1.0\%$) and systematic ($\pm 0.04 \times 10^{-3}$ from $\mathcal{O}(1/\mathcal{N})$ edge corrections, at $1.4\%$), combined $\pm 1.8\%$. Independently testable ratio: $\nu_{\text{OI}} / \Omega_\Lambda = 0.00358 \pm 0.00003$.

**Why the spectral density is uniform.** The conformal assumption ($\alpha = 0$, uniform spectral density in $\ln\omega$) is not a modeling choice — it follows from the lattice structure. Three independent arguments converge: (i) *Time-translation invariance.* The wave equation is autonomous — the coupling between a boundary cell and the bulk does not prefer any frequency. Each cell contributes equally to every frequency decade. (ii) *Entropy saturation.* All boundary modes have $\omega \gg T_{\text{dS}} = \hbar H/(2\pi c k_B) \sim 10^{-33}$ eV (the de Sitter temperature). In this quantum regime, each mode carries $\mathcal{O}(1)$ entropy bit, independent of frequency. The total entropy $S_{\text{dS}} = A/\epsilon^2$ distributes uniformly across $\mathcal{N} = 140$ frequency decades: $S_{\text{dS}}/\mathcal{N}$ per decade. (iii) *Geometric mode counting.* The boundary modes are geometric ($A/\epsilon^2$ cells), not field-theoretic. The SM field content — which fields are active at each energy scale — affects the internal structure of each channel but not the channel count. The mode count per decade is set by the lattice geometry, which is frequency-independent.

The leading correction to uniformity is $\mathcal{O}(1/\mathcal{N}) \approx 0.7\%$, arising from edge effects at $\omega \sim H$ and $\omega \sim c/\epsilon$. For a spectral density $\propto \omega^\alpha$ with $\alpha \neq 0$, the effective $\mathcal{N}$ changes dramatically: $\alpha = +0.1$ gives $\mathcal{N} \sim 10^7$ (ν undetectable), $\alpha = -0.1$ gives $\mathcal{N} \sim 10$ (ν $\sim 0.03$, ruled out). The lattice arguments above constrain $\alpha = 0$ to within $\mathcal{O}(1/\mathcal{N})$, reducing the systematic from a factor of $\sim 3$ (the range $1$–$5 \times 10^{-3}$) to $\pm 1.4\%$.

DESI data [22, 30] report evolving dark energy at $2.8\sigma$–$4.2\sigma$. RVM fits [31] find $\nu \sim \mathcal{O}(10^{-3})$ with $\nu = 0$ disfavored at $2.7\sigma$–$3.1\sigma$, consistent with the prediction.

### 8.2 Gravitational Wave Echoes

A black hole horizon represents a regime where the causal partition differs from the cosmological one: degrees of freedom reclassify from visible to hidden sector as they cross the horizon, shifting the effective partition and the emergent description.

At proper distance $\sim \epsilon$ outside a black hole horizon $r_+$, an infalling mode reaches the discreteness floor and must scatter. The predicted echo time delay is:

$$\Delta t_{\text{echo}} = \frac{r_+}{c} \ln\left(\frac{r_+}{2\,l_p}\right)$$

where $r_+ = (GM/c^2)(1 + \sqrt{1-a^2})$ is the Kerr outer horizon radius. For GW250114 ($M = 62.7 M_\odot$, $a/M = 0.68$): $\Delta t = 48.9$ ms. For a non-spinning $30 M_\odot$ remnant: $\Delta t = 26.8$ ms. The logarithmic dependence on $\epsilon$ makes the timescale robust ($\sim 0.1$ ms shift within the $\sim 49$ ms scale [23]).

**The echo waveform.** After the ringdown, the ingoing component of the QNM signal propagates toward the horizon, scatters off the lattice boundary, and bounces between the boundary and the angular momentum barrier. The echo train:

$$h_{\text{echo}}(t) = \sum_{n=1}^{\infty} (-1)^n \, \mathcal{R} \, \Gamma \, (1-\Gamma)^{n-1} \, e^{-(t - n\Delta t)/\tau} \cos(2\pi f_{\text{QNM}}(t - n\Delta t)) \, \Theta(t - n\Delta t)$$

where $\Gamma \approx 0.45$ is the $l = 2$ greybody factor at the QNM frequency, $\mathcal{R}$ is the effective wall reflectivity, and $(-1)^n$ is the phase flip from the boundary condition. The first echo amplitude relative to the ringdown is $A_1 = \mathcal{R} \times \Gamma$: the ingoing QNM amplitude at the horizon is $\sqrt{\Gamma}$ times the outgoing ringdown amplitude (by reciprocity of the barrier transmission), and after reflecting off the wall it must transmit back through the barrier (another factor $\sqrt{\Gamma}$), giving $A_1 = \mathcal{R} \times \Gamma$. Subsequent echoes decay by factor $(1 - \Gamma)$ per bounce from barrier reflection.

For Kerr remnants ($a/M \sim 0.7$, as in most BBH mergers), the QNM frequency shifts (Berti et al. fitting: $M\omega_R = 1.5251 - 1.1568(1-a)^{0.1292}$ for $l = 2$, $m = 2$) but the greybody factor at the QNM frequency is approximately spin-independent ($\Gamma \approx 0.4$–$0.5$), because the QNM frequency tracks the angular momentum barrier peak even as spin increases ($\omega_{\text{QNM}} \approx \omega_{\text{light ring}}$).

**The wall reflectivity.** A first-principles analysis of the boundary mode structure gives $\mathcal{R} \approx 1$. The boundary at $\epsilon = 2\,l_p$ carries $S_{\text{BH}} = A/(4\,l_p^2)$ degrees of freedom, but only $\sim 5$ modes have angular structure $l = 2$ (the same as the GW). At the QNM frequency, the GW resonates with the fundamental $l = 2$ boundary oscillation ($f_0 \approx c \cdot l/r_h$, within a factor of 2 of $f_{\text{QNM}}$). Dissipation of this mode requires angular momentum transfer to $l \neq 2$ boundary modes, which is suppressed by $(\epsilon/\lambda_{\text{GW}})^{2|\Delta l|} \sim 10^{-82}$ per step — effectively zero. The $l = 2$ mode does not thermalize with the $\sim 10^{77}$ other boundary modes on any relevant timescale, so the boundary acts as a near-perfect reflector: $\mathcal{R} \approx 1$.

This gives a first echo amplitude $A_1 = \mathcal{R} \times \Gamma \approx 0.45$ — loud enough that GW250114 (ringdown SNR $\sim 28$) should produce an echo at SNR $\sim 12.6$. Model-independent echo searches on GW250114 find no statistically significant evidence [45], creating a $\sim 2$–$3\sigma$ tension.

**Resolution of the tension.** The apparent tension is resolved quantitatively by the morphology mismatch between the search and the signal. The Wu et al. [45] search targets long-lived quasi-monochromatic oscillations persisting after the ringdown — effectively a damped sinusoid with $\tau_{\text{LL}} \gg \tau_{\text{GR}}$. The OI echo is a *train of short bursts* — each lasting only $\tau \sim 1.4$ ms, separated by $\sim 50$ ms of silence, with alternating phase $(-1)^n$. The exact fitting factor — the overlap integral between the OI echo template and the best long-lived QNM template (maximized over damping time, frequency, and phase) — is $\text{FF} = 0.19$. The long-lived QNM search recovers only $19\%$ of the optimal SNR, a $5.3\times$ loss. For GW250114: the matched-filter echo SNR is $\sim 15$ (detectable), but the long-lived QNM search SNR is $\sim 15 \times 0.19 \approx 2.8$ — well below any detection threshold. The non-detection is **fully consistent** with the OI prediction.

| Parameter | Formula | $M = 62.7 M_\odot$, $a/M = 0.68$ |
|---|---|---|
| $\Delta t$ | $(r_+/c)\ln(r_+/2l_p)$ | 48.9 ms |
| $f_{\text{QNM}}$ | Berti+2006 ($l=2$, $m=2$) | 271 Hz |
| $\tau$ | Berti+2006 | 1.42 ms |
| $\Gamma$ | Greybody factor at $f_{\text{QNM}}$ | $\approx 0.45$ |
| $\mathcal{R}$ | Wall reflectivity (computed) | $\approx 1$ |
| $A_1/A_{\text{ringdown}}$ | $\mathcal{R} \times \Gamma$ | $\approx 0.45$ |
| Comb teeth within QNM line | $(1/\tau)/(1/\Delta t)$ | $\approx 34$ |
| Fitting factor vs long-lived QNM | $\text{FF} = \max_{\tau_{\text{LL}},f,\phi} \langle h_{\text{OI}} | h_{\text{LL}} \rangle$ | $0.19$ |
| SNR (matched filter, GW250114) | $A_1 \times \text{SNR}_{\text{rd}} \times \sqrt{\Sigma}$ | $\sim 15$ |
| SNR (long-lived QNM search) | $\text{FF} \times 15$ | $\sim 2.8$ |

**Detection prospects.** The predicted echo amplitude ($\sim 45\%$ of ringdown) is substantial, but the signal's comb structure and phase alternation make it nearly orthogonal to long-lived QNM templates (fitting factor $0.19$). Three search strategies can recover the full power: (i) matched filtering with the one-parameter OI template (overall amplitude as the only unknown, everything else fixed by remnant mass and spin; predicted SNR $\sim 15$ for GW250114), (ii) auto-correlation of the post-ringdown signal at lag $\Delta t$ (SNR $\sim 11$), or (iii) a comb filter at spacing $1/\Delta t$ (SNR $\sim 9$). All three are feasible with publicly released O4 strain data. With next-generation detectors (Einstein Telescope, Cosmic Explorer), the matched-filter echo SNR for typical BBH mergers would exceed 100, making detection unambiguous.

**Distinguishing features.** (i) The echo delay $\Delta t$ depends on $\ln(r_h/l_p)$ — a parameter-free prediction. (ii) The phase alternates $(-1)^n$ from the boundary condition. (iii) The echo frequency equals the QNM frequency (no shift). (iv) The wall reflectivity $\mathcal{R} \approx 1$ is a derived result (no dissipation channel for the $l = 2$ boundary mode), not an adjustable parameter. (v) The framework predicts both echoes AND dark energy evolution from the same lattice structure — no other model connects these.

**Observational status.** Model-independent searches for post-merger echoes in GW150914, GW231226, and GW250114 find no statistically significant evidence [45]. This non-detection is consistent with the OI prediction because the searches target long-lived QNMs (single spectral line), while the OI echo is a comb of $\sim 34$ spectral teeth — the $5.3\times$ SNR loss (fitting factor $0.19$) pushes the predicted signal below the search sensitivity. A dedicated matched-filter search using the OI template on GW250114 data would recover the full echo power at predicted SNR $\sim 15$ and provide the definitive test. If matched-filter SNR $< 5$ with the OI template, the prediction is falsified. Joint confirmation of dark energy evolution ($\nu_{\text{OI}}$) *and* GW echoes would uniquely favor an information-theoretic origin.

### 8.3 The Dark-Sector Corollary

The trace-out that produces QM has an automatic gravitational consequence.

**Corollary (Invisible gravitational budget).** *Under Lemmas 1–3 and conditions (C1)–(C3), the cosmological trace-out that produces quantum mechanics simultaneously renders ~95% of the universe's gravitational budget invisible to the emergent QFT.*

*Proof.* Three steps, each using only results already established.

*(i) Total effective density.* The horizon carries $S_{\text{dS}} = A/\epsilon^2$ modes (§6). The classical temperature is $T_{\text{cl}} = c^3 \epsilon^2 H / (8\pi G k_B)$ (§5.1), computed entirely within the classical substratum with no reference to $\hbar$ or the emergent quantum description. The total thermal energy is $E_s = S_{\text{dS}} \cdot k_B T_{\text{cl}}$. By the shell theorem, distributing over $V_H = 4\pi c^3/(3H^3)$:

$$\rho_s = \frac{E_s}{V_H} = \frac{A}{\epsilon^2} \cdot \frac{c^3 \epsilon^2 H}{8\pi G} \cdot \frac{3H^3}{4\pi c^3} = \frac{3c^2 H^2}{8\pi G} = \rho_{\text{crit}}$$

This identity, which Verlinde [37] assumes, is here derived.

Four clarifications are essential for what follows.

*Classical, not emergent.* The calculation above uses only pre-trace-out quantities: the number of boundary modes ($A/\epsilon^2$), the classical temperature ($T_{\text{cl}}$), and the Hubble volume ($V_H$). No step invokes the emergent quantum description. This is what distinguishes $\rho_s$ from the QFT zero-point energy $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4$: the latter is computed as $\sum \frac{1}{2}\hbar\omega$ over modes of the *emergent* quantum field theory — a quantity that exists only after the trace-out. The framework denies that $\rho_{\text{QFT}}$ gravitates (§7.2), because it is an artifact of the emergent description. The boundary entropy's thermal energy, by contrast, is a classical quantity that predates the trace-out and gravitates at the classical level. That both involve $\hbar$ numerically (because $T_{\text{cl}} = T_{\text{GH}}$) is a consequence of the gap equation's self-consistency, not a dependence on QM. The ratio $\rho_{\text{QFT}} / \rho_s \sim S_{\text{dS}} \sim 10^{122}$ — the same compression ratio identified in §7.3 — confirming that the two quantities occupy different levels of the framework's hierarchy.

*Physical locus.* The entropy modes are physically localized on the horizon — they are the hidden-sector boundary degrees of freedom of §5.2. The uniform-medium description is a gravitational equivalence (shell theorem), not a claim about physical delocalization. No entropy occupies the bulk.

*Why the equivalence is useful.* When matter is present, it locally deforms the horizon geometry, redistributing the boundary entropy. The gravitational effect of this redistribution on bulk observers is most easily computed using the uniform-medium equivalence: the deformed boundary is equivalent to a non-uniform effective bulk source.

*Algebraic status.* The coincidence $\rho_s = \rho_{\text{crit}}$ is an algebraic consequence of the Friedmann equation and the self-consistency relation $\hbar = c^3\epsilon^2/(4G)$; it is not an independent physical input.

*(ii) Invisibility.* The argument has two logically distinct components.

*(ii-a) Construction-level invisibility (from Part I alone).* The boundary modes comprising $S_{\text{dS}}$ are hidden-sector degrees of freedom — the variables traced out to produce the quantum description. By the trace-out structure, no hidden-sector degree of freedom maps to an operator on $\mathcal{H}_V$. This is a theorem of Part I, independent of any gravitational content: the hidden sector is invisible to the emergent description by construction.

*(ii-b) Gravitational consequence (from the ontological ordering of §7.2).* The physical import — that the boundary entropy's gravitational influence appears as additional gravity with no source in $\langle \hat{T}_{\mu\nu} \rangle$ — requires the geometry-first ordering established in §7.2: the metric exists at the pre-trace-out level, and the stress-energy sourcing gravity is the classical stress-energy, not the emergent quantum expectation value. Under this ordering, the gravitational interaction between bulk matter and boundary entropy is mediated by the metric at the classical level, modifying the geometry but contributing no term to the emergent $\langle \hat{T}_{\mu\nu} \rangle$. To the embedded observer, this appears as additional gravity with no particle-sector source.

The corollary's predictions are therefore conditional on the same geometry-first ordering that dissolves the CC problem in §7.2. This is not an additional assumption: the ordering is already required by Part II's logic (the partition is defined by null geodesics, so the metric must exist prior to the partition). What the corollary provides is a second, qualitatively distinct *consequence* of that ordering.

*(iii) Budget.* The emergent QFT accounts for the baryonic sector (~5% of $\rho_{\text{crit}}$). The remaining ~95% is boundary entropy — gravitationally active (because $\rho_s$ is a classical quantity computed before the trace-out, unlike $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4$ which is an artifact of the emergent description) but invisible to the emergent QFT. This matches the observed composition, in which ~95% of the gravitational content has no source in particle physics. $\square$

**Memory effects and P-indivisibility.** Matter locally deforms the horizon geometry, redistributing the boundary entropy. This displacement persists because $\tau_B \gtrsim 1/H$ (condition C2): the hidden-sector modes carrying the redistributed entropy do not thermalize back to the unperturbed configuration on sub-Hubble timescales. Verlinde [37] identifies this as a "memory effect" from the non-thermalization of de Sitter states at sub-Hubble scales. In the present framework, this non-thermalization is not assumed but derived: it is P-indivisibility operating in the gravitational sector, with (C2) ensuring that entropy displacements persist without thermal overwriting.

The corollary is a consistency check for the total dark sector budget, not a derivation of its internal structure. The uniform component of the boundary entropy corresponds to dark energy (§7); the structured component — the matter-induced redistribution of boundary entropy producing local gravitational effects resembling dark matter — is derived in §8.4. The ratio $\rho_{\text{QFT}} / \rho_s \sim S_{\text{dS}} \sim 10^{122}$ confirms the parallel with §7.3: the information compression ratio and the gravitational occlusion fraction are two aspects of a single phenomenon.

**Falsifiability.** The corollary would be falsified by detection of dark matter particles accounting for the full ~27% structured dark sector, or by evidence that the dark sector's gravitational effects are unrelated to the boundary geometry.

### 8.4 Dark Matter from Entropy Displacement

The total dark sector budget is established by §8.3. This section derives the structured component from the entropy displacement induced by baryonic matter.

**Step 1: Entropy displacement (derived).** Baryonic matter $M_B$ is coupled to the boundary entropy through $H_{VB}$ (condition C1). The boundary is a thermal reservoir at $T_{\text{dS}} = \hbar H / (2\pi c k_B)$ (derived, §5.2). For a static matter configuration in gravitational equilibrium — a quasi-static process — the Clausius relation gives the entropy displacement:

$$\Delta S = \frac{M_B c^2}{k_B T_{\text{dS}}} = \frac{2\pi M_B c^3}{\hbar H}$$

This follows from the generalized second law (Theorem B.6) applied to the matter-boundary system: the boundary's entropy reduction is $Q/T$ for a reversible process, where $Q = M_B c^2$ and $T = T_{\text{dS}}$. For dynamic configurations, the Clausius inequality $\Delta S \geq Q/T$ only strengthens the displacement.

**Step 2: The critical acceleration (derived).** The displaced entropy redistributes over the volume between the matter and the horizon. The Jacobson mechanism converts the entropy gradient into additional radial acceleration. The crossover between Newtonian gravity and the entropic effect, accounting for the volume-to-surface ratio of spherical redistribution in de Sitter ($1/6$), gives:

$$a_0 = \frac{cH}{6} \approx 1.2 \times 10^{-10} \; \text{m/s}^2$$

This is the MOND critical acceleration — derived, not fitted. (Milgrom's empirical value: $a_0^{\text{obs}} \approx 1.2 \times 10^{-10}$ m/s².)

**Step 3: The deep-MOND regime.** For baryonic acceleration $\ll a_0$, the displaced entropy dominates. The Jacobson mechanism converts the entropy gradient into curvature, giving $g_{\text{total}} = \sqrt{g_B \cdot a_0}$ and rotation velocity:

$$v^2 = r \cdot g_{\text{total}} = \sqrt{GM_B \cdot cH/6} = \text{constant} \qquad \Longrightarrow \qquad v^4 = GM_B \cdot cH/6$$

This is the baryonic Tully-Fisher relation. Flat rotation curves emerge with no dark matter particles and no free parameters beyond the baryonic mass.

**Step 4: Interpolation constraints.** The full interpolation between the Newtonian regime ($g_B \gg a_0$) and the deep-MOND regime ($g_B \ll a_0$) is constrained by the framework but not uniquely determined. The entropy displacement defines a potential $\Psi_D$ with $g_D = -\nabla \Psi_D$, and the framework requires:

(i) *No free parameters.* $g_D$ depends only on $g_B$ and $a_0 = cH/6$ — no halo-specific parameters, no fitting constants.

(ii) *Conservative.* $\nabla \times g_D = 0$, since $g_D$ derives from the entropy potential.

(iii) *Monotonic.* $\partial g_D / \partial g_B > 0$ — more baryonic mass produces more entropy displacement, hence more dark matter effect.

(iv) *Correct limits.* $g_D \to 0$ for $g_B \gg a_0$ (Newtonian); $g_D \to \sqrt{g_B \cdot a_0}$ for $g_B \ll a_0$ (MOND).

(v) *Analytic.* The entropy redistribution is a smooth function of the coupling structure — no discontinuities or phase transitions in the interpolation.

These constraints narrow the interpolation to a one-parameter family indexed by the transition steepness — a property of the particular bijection $\varphi$, in the same category as fermion masses (Fundamental, §9.7). The simplest member satisfying all five constraints:

$$g_D = \frac{g_B}{2}\left(\sqrt{1 + \frac{4a_0}{g_B}} - 1\right)$$

which is equivalent to $g_{\text{total}} = g_B \cdot \nu(g_B/a_0)$ with $\nu(y) = (1 + \sqrt{1 + 4/y})/2$ — the "simple" MOND interpolation function corresponding to $\mu(x) = x/(1+x)$. This form matches the empirical radial acceleration relation (McGaugh et al. [44]) to $< 0.1$ dex across all galaxy-relevant accelerations.

**Epistemic status.** Steps 1–3 are Tier 2: the displacement formula follows from the Clausius relation applied to the boundary reservoir (§5.2, B.6), the geometric factor from spherical redistribution in de Sitter, and $a_0 = cH/6$ and $v^4 = GM_B \cdot cH/6$ are parameter-free consequences. The interpolation constraints (i)–(v) are Tier 2; the transition steepness is Tier 3 (solution-specific).

**Redshift evolution.** Since $a_0(z) = cH(z)/6$ and $H(z) = H_0\sqrt{\Omega_m(1+z)^3 + \Omega_\Lambda}$, the critical acceleration increases with redshift: $a_0(z=1) = 1.79\,a_0(0)$, $a_0(z=2) = 3.03\,a_0(0)$, $a_0(z=3) = 4.57\,a_0(0)$. The MOND crossover radius $r_M = \sqrt{6GM_B/(cH)}$ correspondingly shrinks — for a $10^{10}\,M_\odot$ galaxy, $r_M = 9.0$ kpc at $z = 0$ but $5.2$ kpc at $z = 2$ and $3.1$ kpc at $z = 5$. Galaxies with effective radii comparable to or exceeding $r_M$ show flat rotation curves (the familiar local behavior); galaxies with $r_{\text{eff}} < r_M$ show declining, Keplerian-like rotation curves. Since $r_M$ shrinks with increasing $z$, high-redshift galaxies are systematically more baryon-dominated — their rotation curves decline at smaller radii.

This prediction is borne out by the data. Genzel et al. [42, 43] report stacked rotation curves for massive star-forming galaxies at $z = 0.9\text{–}2.4$ showing a declining outer velocity at $> 3\sigma$ significance relative to local spirals — consistent with the OI prediction. In ΛCDM, flat rotation curves from NFW halos are expected at all redshifts; explaining the Genzel data requires anomalously low halo concentrations or baryon-dominated inner regions.

**Tully-Fisher tension and resolution.** McGaugh et al. (2024), analyzing Nestor Shachar et al. (2023) JWST kinematics, report no evolution in the Tully-Fisher relation out to $z \sim 2.5$, seemingly contradicting $v^4 \propto H(z)$. However, this comparison uses *stellar* mass $M_*$, not baryonic mass $M_B = M_*/(1-f_{\text{gas}})$. At high redshift, gas fractions are large ($f_{\text{gas}} \sim 50\text{–}70\%$ at $z \sim 2$; Tacconi et al. 2018). The OI-predicted shift in the baryonic TF ($\Delta\log M_B = \log(H_0/H(z)) = -0.48$ dex at $z = 2$) is almost exactly compensated by the gas mass not included in $M_*$: the cancellation requires $f_{\text{gas}} = 1 - H_0/H(z)$, which gives 44% at $z = 1$, 58% at $z = 1.5$, and 67% at $z = 2$ — squarely in the observed range. The apparent "no evolution" in the stellar TF is therefore *predicted* by the OI framework: the dynamical shift (higher $a_0$) and the compositional shift (higher gas fraction) cancel when only stellar mass is measured. The definitive test is the *baryonic* TF at $z > 1$ with reliable ALMA gas masses: the OI framework predicts a normalization shift of $-0.48$ dex at $z = 2$ at fixed $v_{\text{flat}}$.

**Observational predictions.** Three parameter-free, quantitative tests:

(i) *Rotation curve evolution.* The outer rotation curve slope (measured as $\Delta v / v$ between $r_{\text{turn}}$ and $2r_{\text{turn}}$) becomes more negative (more Keplerian) with increasing $z$, following $a_0(z) = cH(z)/6$. For a $10^{10.8}\,M_\odot$ exponential disk with $r_{\text{eff}} = 5$ kpc: the outer slope changes from $-0.10$ at $z = 0$ to $-0.12$ at $z = 2$ to $-0.13$ at $z = 5$. Particle dark matter predicts no evolution.

(ii) *Tully-Fisher evolution.* The baryonic Tully-Fisher relation evolves: $v_{\text{flat}}^4 = GM_B \cdot cH(z)/6$. At fixed baryonic mass, $v_{\text{flat}} \propto H(z)^{1/4}$: 7% higher at $z = 0.5$, 16% higher at $z = 1$, 32% higher at $z = 2$. Equivalently, at fixed $v_{\text{flat}}$, the inferred baryonic mass at $z = 2$ is $H_0/H(z=2) = 0.33\times$ the local value — galaxies appear to need less dark matter at high $z$. Testable with JWST and ALMA kinematics combined with photometric baryonic mass estimates.

(iii) *No halo-specific parameters.* In particle DM, each galaxy has a dark matter halo characterized by at least two free parameters (concentration and mass). In the OI framework, the dark matter effect at radius $r$ depends only on the enclosed baryonic mass $M_B(<r)$ and $H(z)$ — no halo-specific parameters. This predicts: the radial acceleration relation (RAR) at fixed $g_B$ has zero intrinsic scatter (at fixed $z$), and the scatter does not correlate with halo properties. Current SPARC data [44] show remarkably small RAR scatter ($\sim 0.13$ dex), consistent with OI but requiring fine-tuning in ΛCDM.

**Falsifiability.** The entropy displacement account would be falsified by: (a) detection of dark matter particles accounting for $\sim$27% of $\rho_{\text{crit}}$; (b) high-redshift rotation curves inconsistent with the predicted $H(z)$ dependence — specifically, if galaxies at $z > 2$ show flat rotation curves at $r > r_M(z)$; (c) baryonic Tully-Fisher violations exceeding baryonic mass uncertainties; (d) RAR scatter correlating with halo properties at fixed $g_B$ and $z$.

**Cluster-scale status.** Galaxy clusters present the most challenging regime for MOND-like theories. For the Coma cluster ($M_B \approx 1.4 \times 10^{14}\,M_\odot$, $R_{200} \approx 1.9$ Mpc), the acceleration at the virial radius is $g_B/a_0 \approx 0.05$ — deep in the MOND regime. With the simple interpolation function above, the predicted velocity is $v = g_B \cdot \nu(g_B/a_0) \cdot R_{200} \approx 1260$ km/s; the observed velocity dispersion implies $\sim 1270$ km/s — a match to better than $1\%$. For other rich clusters (Perseus, A2029, A1689), the simple interpolation reduces the standard MOND mass shortfall from a factor $\sim 2$ to $\sim 1.0$–$1.5$; the residual is within the range of missing baryonic mass in the warm-hot intergalactic medium (WHIM at $T \sim 10^5$–$10^7$ K, difficult to detect in X-rays, estimated to add 30–100% to cluster baryonic mass). The deep-MOND limit $v^4 = GM_B \cdot a_0$ (Tier 2) is identical for all interpolation functions; only the intermediate-acceleration behavior (Tier 3) differs. Galaxy-scale predictions are unaffected: at $g_B/a_0 = 0.5$ (typical outer disk), different interpolation functions agree to $< 0.07$ dex — well within the RAR scatter of $0.13$ dex.

**Colliding clusters (Bullet Cluster).** The Bullet Cluster (1E 0657-56) presents the most-cited evidence for particle dark matter: after the collision, gravitational lensing peaks coincide with the galaxy concentrations ($\sim 15\%$ of baryonic mass), not with the X-ray gas ($\sim 85\%$ of baryonic mass) that was ram-pressure stripped to the center. In a local MOND picture where $g_D$ tracks the instantaneous baryonic distribution, the lensing should peak where the gas is — contradicting observations. The OI framework resolves this through the non-local character of entropy displacement. The dark gravity arises from boundary entropy redistribution at the cosmological horizon, and the horizon's response time is $\tau_{\text{relax}} \sim H^{-1} \approx 14$ Gyr. The collision crossing time is $t_{\text{cross}} \sim 720\,\text{kpc}/4700\,\text{km/s} \approx 0.15$ Gyr — only $1\%$ of the relaxation time. The entropy displacement is therefore *frozen* at the pre-collision configuration, centered on the galaxy concentrations (which defined the gravitational potential wells for gigayears before the collision). The gas moved during the collision; the boundary entropy did not. This reproduces the observed morphology: lensing peaks at the galaxy positions, gas peak between them — without invoking collisionless particles. The mechanism makes a testable prediction: for very old post-collision systems ($t_{\text{since}} \gg 1$ Gyr), the dark gravity should gradually relax toward the gas distribution on timescale $\sim H^{-1}$. Particle dark matter predicts no such relaxation.

**CMB acoustic peaks.** The CMB power spectrum provides the most precise test of the dark matter paradigm: the odd/even peak height asymmetry requires a non-oscillating gravitational source (CDM in ΛCDM) that provides potential wells for the photon-baryon fluid to oscillate in. The entropy displacement satisfies this requirement through the same thermodynamic averaging that resolves the Bullet Cluster. The Clausius relation $\Delta S = \delta Q / T_H$ involves the *net* heat transfer to the horizon boundary. For an oscillating perturbation (compression then rarefaction), the net entropy displacement per acoustic cycle is zero — the oscillating component averages out. Only the secular (growing) component produces net displacement. The entropy displacement perturbation therefore does not oscillate with the photon-baryon fluid; it tracks the growing mode exclusively.

The entropy displacement perturbation then evolves identically to CDM in the linear regime: (i) it has the same effective density ($\rho_E \approx \Omega_{\text{CDM}} \times \rho_{\text{crit}}$, from the dark-sector corollary §8.3); (ii) it does not couple to photons (it is a gravitational effect at the horizon, not a fluid component); (iii) it grows under its own gravity from adiabatic initial conditions set by inflation; (iv) its growth equation $\ddot{\delta}_E + 2H\dot{\delta}_E = 4\pi G \rho_{\text{eff}} \delta_E$ has the same source term as CDM. The CMB power spectrum — which depends on $\Omega_b/\Omega_m$ (peak ratios), the growth of perturbations before recombination (peak heights), the sound horizon $r_s$ (peak positions), and the damping scale (high-$\ell$ suppression) — is therefore predicted to match ΛCDM at linear order. A definitive confirmation requires running a modified Boltzmann code (CLASS or CAMB) with entropy displacement replacing CDM; the prediction is agreement with Planck data to within current uncertainties. *Epistemic status: Tier 3 (derived consequence, pending numerical verification).*

---

## 9. DISCUSSION

### 9.1 Interpretive Consequences

In the cosmological application, the hidden sector is the trans-horizon region; the degrees of freedom involved in quantum experiments — photons, electrons, slits, detectors — are all visible-sector objects. Their quantum behavior is a downstream consequence of the single cosmological trace-out: the emergent quantum mechanics, once established by the theorem, governs all visible-sector dynamics.

In the double-slit experiment, the particle traverses a single slit in the deterministic substratum. The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events. A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms. In Wigner's friend, the Friend has a definite outcome; Wigner's superposition reflects his epistemic deficit. The Everettian measure problem dissolves: the system evolves as a single reality; "branches" are features of the compressed description. The Born rule, often treated as an independent postulate, is derived: it is the equilibrium distribution of the indivisible stochastic process (§3.1), not an additional assumption.

### 9.2 Scope

The characterization theorem is a full equivalence: QM $\iff$ embedded observation under (C1)–(C3). The theorem does not identify which physical systems satisfy the conditions (empirical) nor derive $\hbar$ for specific systems (requires Part II). Universality in our universe follows from the shared causal partition defined by null geodesics.

### 9.3 The Status of the Discreteness Scale

$\epsilon$ does not smuggle in a quantum assumption. Lemma 1 requires finite-dimensionality, motivated by the classical fact that finite-area boundaries admit finitely many modes. The result $\epsilon = 2\,l_p$ is a *consequence* of self-consistency (§6). Holographic entropy bounds [27] provide independent, non-quantum motivation.

### 9.4 Vacuum Energy: Relative Effects and the Higgs Potential

**Relative effects.** Casimir forces and Lamb shifts are predictions *within* the emergent QFT — relative effects depending on energy differences between configurations. The framework denies that the *absolute* zero-point sum gravitates, because gravity operates at the logically prior classical level (§7.2).

**The Higgs potential.** The strongest CC objection is not the zero-point sum but the electroweak Higgs potential: symmetry breaking shifts $V(\phi)$ by $\sim (200\;\text{GeV})^4$, exceeding the observed $\Lambda$ by $\sim 55$ orders of magnitude. The framework's response follows from its ontological ordering and the structural/volumetric distinction of §5.2, applied as a precise principle:

*What gravitates:* Relative energy differences between configurations of the emergent fields. An electron at rest vs. no electron differs by $m_e c^2$ in the classical substratum — there is a classical microstate difference corresponding to this energy difference. Relative differences appear in the classical stress-energy tensor and gravitate. Casimir forces, Lamb shifts, and particle masses all fall in this category.

*What does not gravitate:* Absolute energy levels assigned to configurations by the emergent description. The Higgs vacuum energy shift $V(\phi_{\text{min}})$ is the energy the emergent QFT assigns to its ground state — the configuration obtained after symmetry breaking. But the "ground state" in the emergent description corresponds to a class of classical microstates whose energy in the classical substratum is $\rho \sim H^2/G$, not $\rho \sim (200\;\text{GeV})^4$. The shift is a property of how the emergent description organizes the microstates (the correspondence), not a property of the microstates themselves (the classical dynamics).

The principle is uniform: the zero-point sum, the Higgs vacuum energy, and the QCD condensate energy are all absolute properties of the emergent ground state. The dissolution applies to each for the same reason — gravity operates at the classical level (§7.2), where none of these quantities appear.

**Why QCD binding energy gravitates but the quantum vacuum does not.** The proton mass is ~99% QCD binding energy — a purely quantum effect. If gravity couples to the classical substratum, how does it "know" about masses generated by emergent quantum dynamics? The answer is that QCD binding energy and vacuum zero-point energy occupy different categories in the structural/volumetric distinction of §5.2. Relative energies within the emergent QFT — energy differences between configurations — correspond to differences in the coupling structure of $\varphi$, which the Jacobson derivation (Fundamental, §5) reads as curvature. A proton vs. three free quarks corresponds to two distinct classes of classical microstates with different energies in the classical substratum; the binding energy $\sim 938$ MeV is a *relative* quantity that appears in $H_{\text{tot}}$ and gravitates. The absolute baseline — the zero-point energy summed over all modes — corresponds to the total information capacity of the hidden sector ($S_{\text{dS}}$), which is a property of the partition geometry, not of the dynamics, and therefore does not source curvature.

### 9.5 Relation to Prior Work

**'t Hooft [1]:** Differs in mechanism (epistemic trace-out vs. information loss), generality (any embedded observer vs. particular rules), and Bell placement (outcome independence violation vs. superdeterminism). **QBism/relational QM:** Share observer-relative epistemic states; this framework provides a structural *why* and quantitative predictions. **Jacobson [16]:** Derives gravity from thermodynamics; this framework derives QM from causal structure — complementary, with mutual consistency as a check.

**Danielson-Satishchandran-Wald (DSW) horizon decoherence [38, 39].** DSW proved within standard QFT that any Killing horizon imparts a fundamental rate of decoherence on nearby quantum superpositions: the horizon registers the long-range field of the superposed body via soft gravitons/photons, destroying coherence at a rate determined by the horizon geometry. This is precisely the framework's partition mechanism described in QFT language — the horizon is the causal boundary, information leaks through it, and the exterior state decoheres. Three specific features match: (i) the decoherence rate depends on horizon geometry (partition-relativity); (ii) decoherence vanishes for extremal black holes where the coupling to the interior is screened (C1 failure); (iii) the process is non-Markovian near the horizon, with information backflow from the interior [40]. The DSW program derives these results within the emergent QFT; the present framework explains *why* horizons produce decoherence — because the trace-out across a causal partition is the mechanism that generates quantum mechanics itself.

**AdS/CFT and the geometry-entanglement connection.** The Ryu-Takayanagi formula, Van Raamsdonk's disconnection argument, ER=EPR, and "it from qubit" programs all suggest entanglement is prior to geometry. The framework offers a uniform alternative reading: tracing out across a geometric boundary produces entanglement entropy proportional to boundary area ($A/\epsilon^2$ modes), so each of these results is equally consistent with geometry assembling entanglement rather than the reverse. For Ryu-Takayanagi specifically, the proportionality constant must follow from the partition structure — and it does: §6 derives the $1/4$ factor. In the holographic context, the boundary CFT observer is *external* to the bulk, immune to the inferential limits of embedded observers [19]; the framework does not claim to reproduce holographic results in that setting.

The point of contact is empirical. Entanglement-first programs predict spacetime breakdown at low entanglement or high energy. This framework predicts QM breakdown near $\epsilon = 2\,l_p$ while the geometric substratum persists. The geometry-first ordering produces twelve independent concordances with observation (§7.2); entanglement-first orderings inherit the zero-point sum as a gravitational source and have no natural account of the dark sector.

Witten's Type II algebra program achieves finite entropy without finite-dimensional Hilbert spaces; this is compatible, since the framework's predictions depend on finite entropy (the physical content of Lemma 1), not on dimensional finiteness per se.

### 9.6 Assumptions, Limitations, and Falsifiability

**The theorem** requires Lemma 1 (independent in Part I; consequence of geometry in Part II), the stochastic-quantum bridge (§3.1 and Appendix A; established by two independent routes), and genericity conditions (non-degenerate spectrum, non-vanishing overlaps), which hold for all but a measure-zero set. The P-indivisibility proof uses finiteness via the recurrence argument ($\varphi^N = \text{id}$). The deep-sector cardinality corollary (§5.2) establishes that only $\mathcal{C}_V$ and $\mathcal{C}_B$ need be finite — both guaranteed by holographic entropy bounds [27] independently of the de Sitter finite-dimensionality conjecture — while the deep sector $\mathcal{C}_D$ may be infinite. The accessible-timescale backflow lemma (§2.3) provides a second route to P-indivisibility that is independent of $|\mathcal{C}_H|$. The characterization theorem becomes an equivalence on observable timescales ($T_{\text{obs}} \ll \tau_B \sim 10^{17}$ s) — physically indistinguishable from a timeless identity for all experiments within the age of the universe.

**The sharp partition and constraint structure.** Lemma 2's product decomposition $\Gamma = \Gamma_V \times \Gamma_H$ is the kinematic phase space. In GR, the Hamiltonian and momentum constraints restrict the physical phase space to a submanifold $\Gamma_{\text{phys}} \subset \Gamma_V \times \Gamma_H$ on which interior and exterior data are correlated. P-indivisibility survives on a constraint surface because restoring P-divisibility would require decoupling the sectors entirely, violating the constraints; the constraint surface thus enforces (C1) non-perturbatively. For systems other than the cosmological horizon, the fidelity of the product approximation determines the fidelity of the emergent quantum description.

**Planck-scale ordering.** The classical-prior ontology may break down at $l_p$, where "geometric" and "quantum" lose operational distinction. If a deeper theory unifies both, this framework describes the effective macroscopic regime.

**Falsifiability.** The *theorem* would be falsified by a failure of both the stochastic-quantum correspondence and the Stinespring construction for the class of processes generated here — a possibility excluded by the independent proofs in §3.1 and Appendix A. The *cosmological application* would be falsified by definitive absence of dark energy evolution or GW echoes at the predicted timescale. The *dark-sector concordance* (§8.3) would be falsified by detection of dark matter particles accounting for the full structured dark sector, or by evidence that the dark sector's gravitational effects are unrelated to the cosmological boundary geometry.

**Nested and time-dependent partitions.** The derivation chain assumes a single partition into visible and hidden sectors. In reality, multiple causal boundaries coexist — most naturally, a black hole horizon inside the cosmological horizon — creating nested partitions with distinct geometries. Appendix B resolves this in three layers.

*(i) Consistency of nested trace-outs (Appendix B, Theorems B.1–B.4).* Two procedures — tracing out the trans-cosmological region and the black hole interior simultaneously (direct) or sequentially (first cosmological, then black hole) — produce the same CPTP channel, the same emergent Hamiltonian (up to D-gauge), and the same $\hbar$. The key result (Theorem B.2) is that the quantum partial trace within the emergent description agrees with the classical marginalization on the substratum: the emergent QM is self-consistent.

*(ii) The generalized second law (Appendix B, Theorem B.6).* The sum $S_{\text{matter}} + S_{\text{BH}} + S_{\text{dS}}$ is non-decreasing, proved from strong subadditivity and CPTP monotonicity of the emergent quantum description. Any process that shrinks the black hole (decreasing $S_{\text{BH}}$) transfers information to the visible sector and cosmological boundary, compensating the decrease.

*(iii) The Page curve (Appendix B, Theorems B.7–B.9).* For an evaporating black hole, the entanglement entropy of the radiation follows $S_{\text{rad}}(t) = \min(n_R(t), n_B(t)) \cdot \ln q$ plus exponentially small corrections, where $n_B(t)$ is the shrinking boundary mode count and $n_R(t) = n_B(0) - n_B(t)$. Unitarity is preserved (bijectivity of $\varphi$), the turnover occurs at the Page time $t_P \approx 0.646 \, t_{\text{evap}}$ (structural, independent of mass and greybody factors), and the Page value is recovered for all but an exponentially negligible fraction ($\sim e^{-10^{77}}$ for $30 M_\odot$) of initial conditions — proved from bijectivity (cycle decomposition on the finite energy shell) and Popescu-Short-Winter typicality [41], without assuming ergodicity. The greybody factor is solution-specific.

Laboratory tests of the characterization theorem may be possible in analogue gravity systems where the hidden sector capacity is tunable.

---

## 10. CONCLUSION

**The general theorem (Part I).** Under a single definition — observation is a proper subsystem of a deterministic whole — and conditions (C1)–(C3), the P-indivisibility of reduced dynamics is proved: any bijective dynamics on a finite system with non-trivial coupling necessarily produces P-indivisible stochastic dynamics. By the stochastic-quantum correspondence, the observer's description is necessarily quantum mechanics. Continuous-time transition data resolves all gauge freedom. The Schrödinger equation, Born rule, and Bell violations are structural consequences. The characterization theorem establishes that the conditions are necessary: QM and embedded observation under (C1)–(C3) are equivalent.

**The cosmological application (Part II).** The cosmological horizon provides a realization where the sharp-partition approximation is exact and all conditions hold. The theorem yields: (a) $\hbar = c^3 \epsilon^2 / (4G)$ with $\epsilon = 2\,l_p$ and the Bekenstein-Hawking formula as consequences; (b) dissolution of the CC problem — the $10^{122}$ discrepancy is $S_{\text{dS}}$, the compression ratio of the observer's quantum description; (c) falsifiable predictions including RVM dark energy with $\nu_{\text{OI}} = (2.45 \pm 0.04) \times 10^{-3}$ and gravitational wave echoes; (d) an automatic dark-sector corollary — the same trace-out renders ~95% of the universe's gravitational budget invisible to the emergent QFT; and (e) dark matter phenomenology from entropy displacement — flat rotation curves, the baryonic Tully-Fisher relation $v^4 = GM_B \cdot cH/6$, and the MOND acceleration scale $a_0 = cH/6 \approx 1.2 \times 10^{-10}$ m/s², all derived from the boundary entropy and the Jacobson mechanism (§8.4). The $H(z)$ dependence of $a_0$ predicts systematically more Keplerian rotation curves at high redshift — consistent with the declining rotation curves observed at $z = 0.9$–$2.4$ [42, 43] and testable at higher precision with JWST and ELT kinematics.

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

[42] R. Genzel et al., "Strongly baryon-dominated disk galaxies at the peak of galaxy formation ten billion years ago," *Nature* **543**, 397–401 (2017).

[43] R. Genzel et al., "Rotation curves in z ~ 1–2 star-forming disks: evidence for cored dark matter distributions," *Astrophys. J.* **902**, 98 (2020).

[44] S. S. McGaugh, F. Lelli, and J. M. Schombert, "Radial acceleration relation in rotationally supported galaxies," *Phys. Rev. Lett.* **117**, 201101 (2016).

[45] D. Wu et al., "Model-independent search of gravitational wave echoes in LVK data," arXiv:2512.24730 (2025).

[42] D. N. Page, "Average entropy of a subsystem," *Phys. Rev. Lett.* **71**, 1291 (1993).

---

## APPENDIX A: INDEPENDENT DERIVATION VIA STINESPRING DILATION

This appendix derives the emergent quantum description using only Stinespring's dilation theorem [32] and standard properties of the partial trace [33], without invoking the stochastic-quantum correspondence [10, 11]. The two routes are logically independent; either alone suffices.

### A.1 Setup

The finite configuration spaces $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ and $\mathcal{C}_H = \{h_1, \ldots, h_m\}$ (Lemma 1) embed into Hilbert spaces $\mathcal{H}_V = \mathbb{C}^n$ and $\mathcal{H}_H = \mathbb{C}^m$ via $|i\rangle \leftrightarrow x_i$ and $|k\rangle \leftrightarrow h_k$. This introduces no quantum postulates: it is the canonical identification of probability distributions on a finite set with diagonal density matrices.

### A.2 Permutation Unitarity

**Lemma A.1.** *Any bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ defines a unitary $U_\varphi$ on $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$.*

*Proof.* Define $U_\varphi |i, k\rangle = |\varphi(x_i, h_k)\rangle$. Since $\varphi$ is a bijection, $U_\varphi$ permutes the orthonormal basis, hence is unitary. $\square$

For continuous-time dynamics $\varphi_t$, Stone's theorem on $\mathcal{H}$ yields $U_t = e^{-i\hat{H}t}$ for Hermitian $\hat{H}$.

### A.3 The Quantum Channel

The observer's ignorance of the hidden sector (Lemmas 3–4) corresponds to $\rho_H = I_m/m$. The visible-sector quantum channel is

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

The Barandes route is more general (any P-indivisible process); the Stinespring route requires only textbook results [32, 33] and delivers additional structure: the tensor product $\mathcal{H}_V \otimes \mathcal{H}_H$, genuine quantum coherence (Theorem A.3), CP-indivisibility (Theorem A.4), and approximate unitarity with $\mathcal{D} \sim \mathcal{O}(\tau_S / \tau_B) \sim 10^{-32}$ (§A.7). The two routes agree on all observables — both produce the same $T_{ij}(t)$ — establishing that the emergence of QM is robust and overdetermined. The Barandes route powers (ii) $\implies$ (i) in the characterization theorem; the Stinespring route supplies (iii) $\implies$ (i) independently.

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

*Proof.* The proof applies the boundary-only dependence lemma (§5.2) twice, tracking the cross term at each stage.

(i) *First application: freeze $D$.* Apply the boundary-only dependence lemma to the partition $(W, D)$ where $W = V \cup B$. By spatial locality, $H_{\text{tot}} = H_V + H_B + H_D + H_{VB} + H_{BD}$ with no direct $V$-$D$ coupling. The $D$-sector is frozen on timescales $t \ll \tau_B^D$, giving:

$$T^V_{ij}(t) = \frac{1}{|\mathcal{C}_B|} \sum_{b \in \mathcal{C}_B} \delta_{x_j}[\pi_V(\varphi_t^{VB}(x_i, b))] + \mathcal{O}(t / \tau_B^D)$$

where $\varphi_t^{VB}$ is the flow restricted to $V \times B$ with $D$ frozen. The $\mathcal{O}(t / \tau_B^D)$ correction arises from $D$'s back-reaction on $B$ through $H_{BD}$.

(ii) *Dissipator from the frozen-$D$ dynamics.* The frozen-$D$ flow $\varphi_t^{VB}$ is a bijection on $\mathcal{C}_V \times \mathcal{C}_B$ — exactly the setup of Appendix A with $B$ as the hidden sector. The emergent dynamics on $V$ is approximately unitary with dissipator $\mathcal{D}_V^{(B)} \sim \mathcal{O}(\tau_S / \tau_B^B)$.

(iii) *Decomposition of the $D$-correction.* The $\mathcal{O}(t / \tau_B^D)$ correction from step (i) has two components:

*Direct:* $D$'s back-reaction shifts the boundary modes of $B$ by $\delta b \sim \mathcal{O}(t / \tau_B^D)$. This propagates through $H_{VB}$ to the visible sector, contributing $\mathcal{D}_V^{(D)} \sim \mathcal{O}(\tau_S / \tau_B^D)$.

*Cross:* The shift $\delta b$ also modifies the effective $B$-state against which $\mathcal{D}_V^{(B)}$ is computed. The dissipator $\mathcal{D}_V^{(B)}$ depends on the $B$-state through the Liouville average over $b$. The $D$-induced shift changes this average by $\mathcal{O}(t / \tau_B^D)$, so:

$$\|\mathcal{R}\| = \left\|\frac{\partial \mathcal{D}_V^{(B)}}{\partial b}\right\| \cdot \|\delta b\| \leq \|\mathcal{D}_V^{(B)}\| \cdot \mathcal{O}(t / \tau_B^D) = \mathcal{O}\!\left(\frac{\tau_S}{\tau_B^B} \cdot \frac{\tau_S}{\tau_B^D}\right) = \mathcal{O}\!\left(\frac{\tau_S^2}{\tau_B^B \cdot \tau_B^D}\right)$$

The inequality uses the fact that $\mathcal{D}_V^{(B)}$ is a continuous function of the $B$-state distribution and the shift is first-order in $t / \tau_B^D$. $\square$

**Bound for the cosmological + stellar black hole case.** For a $30 M_\odot$ black hole inside the cosmological horizon: $\tau_S \sim 10^{-15}$ s, $\tau_B^B \sim \tau_{\text{scr}} \sim \beta \log S_{\text{BH}} \sim 10^{-3}$ s, $\tau_B^D \sim 1/H \sim 10^{17}$ s. The three terms:

$$\|\mathcal{D}_V^{(B)}\| \sim 10^{-12}, \qquad \|\mathcal{D}_V^{(D)}\| \sim 10^{-32}, \qquad \|\mathcal{R}\| \sim 10^{-44}$$

The cross term is negligible by 12 orders of magnitude relative to the smaller of the two primary dissipators.

### B.6 The Generalized Second Law

The Bekenstein-Hawking entropy of a horizon is the information content of the corresponding partition boundary (§6): $S_{\text{BH}} = A_{\text{BH}} / (4\,l_p^2)$ modes at the black hole horizon, $S_{\text{dS}} = A_{\text{dS}} / (4\,l_p^2)$ modes at the cosmological horizon. The matter entropy is the von Neumann entropy of the visible-sector state: $S_{\text{matter}} = -\text{Tr}[\rho_V \log \rho_V]$.

**Theorem B.6** (Generalized second law). *For any process described by the CPTP channel $\Phi_V$ on $\mathcal{H}_V$:*

$$S_{\text{matter}}(t) + S_{\text{BH}}(t) + S_{\text{dS}}(t) \geq S_{\text{matter}}(0) + S_{\text{BH}}(0) + S_{\text{dS}}(0)$$

*Proof.* The total system $(S, \varphi)$ evolves unitarily at the fundamental level, so the total fine-grained entropy $S_{\text{total}} = \log|S|$ is constant. The three terms $S_{\text{matter}}$, $S_{\text{BH}}$, $S_{\text{dS}}$ are the observer's ignorance about three sectors: $V$, $B$, $D$ respectively.

(i) *Subadditivity.* For the tripartite system $\mathcal{H}_V \otimes \mathcal{H}_B \otimes \mathcal{H}_D$ in a pure state $|\Psi\rangle$ (the total state is deterministic, hence pure conditioned on the initial state), the strong subadditivity of von Neumann entropy [33] gives:

$$S(\rho_{VB}) + S(\rho_{BD}) \geq S(\rho_B) + S(\rho_{VBD})$$

Since $\rho_{VBD} = |\Psi\rangle\langle\Psi|$ is pure, $S(\rho_{VBD}) = 0$. Thus $S(\rho_{VB}) + S(\rho_{BD}) \geq S(\rho_B)$.

(ii) *Identification.* The observer's matter entropy is $S_{\text{matter}} = S(\rho_V)$. By purification on the tripartite system: $S(\rho_V) = S(\rho_{BD})$. The black hole entropy is $S_{\text{BH}} = S(\rho_B)$ restricted to the boundary modes (the number of $B$-modes coupled across the black hole horizon). The cosmological entropy is $S_{\text{dS}} = S(\rho_D)$ restricted to the boundary modes.

(iii) *Monotonicity and compensation.* The CPTP channel $\Phi_V$ is a contraction of relative entropy [33, Theorem 11.9], so $S(\rho_V)$ is non-decreasing under the emergent dynamics. Any process that decreases $S_{\text{BH}}$ (shrinking the black hole) transfers information from $B$ to $V \cup D$. By the unitarity of $\varphi$, the total mutual information $I(V:B:D)$ is conserved, so the decrease in $S_{\text{BH}}$ is compensated by an increase in $S_{\text{matter}} + S_{\text{dS}}$. $\square$

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
