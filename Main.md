# THE INCOMPLETENESS OF OBSERVATION
### The Equivalence of Quantum Mechanics and Embedded Observation

**Author:** Alex Maybaum  
**Date:** April 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

An observer embedded in a deterministic universe cannot access the complete state. We prove that any such observer — coupled to a slow, high-capacity hidden sector on a finite-dimensional configuration space — must describe the visible sector using P-indivisible stochastic dynamics, mathematically equivalent to unitary quantum mechanics. The converse also holds: any quantum system, realized as a deterministic dilation with a hidden sector obeying the eigenstate thermalization hypothesis, requires non-trivial coupling, slow-bath memory, and sufficient hidden-sector capacity. The Schrödinger equation, Born rule, and Bell violations emerge as structural consequences requiring no independent quantum postulates.

---

## 1. INTRODUCTION

### 1.1 The Problem of Embedded Observation

An observer embedded in a deterministic universe cannot access the complete state: degrees of freedom beyond causal reach are permanently hidden, and the observer's description is obtained by marginalizing over the hidden sector. The question is what this reduction imposes on the form of the observer's physical laws.

Prior work (QBism, relational QM, 't Hooft's cellular automaton [1]) takes observer-dependence as an interpretive starting point or derives it from specific microphysical models. This framework differs by identifying *necessary and sufficient conditions* under which any embedded observer in any deterministic system necessarily sees quantum mechanics — and proving these are the *only* conditions under which QM arises from a deterministic embedding.

### 1.2 The Starting Point

The framework begins with a single empirical fact that cannot be doubted: *observation occurs*. An observer records distinguishable outcomes of interactions with a system not wholly under the observer's control. This is the cogito of Descartes made precise — not as philosophy, but as a mathematical constraint.

We ask: what is the minimal mathematical structure consistent with this fact?

**Definition.** An *observation* is a triple $(S, \varphi, V)$: a total system $S$, a dynamics $\varphi: S \to S$, and an observer $V \subsetneq S$ — a proper subsystem with finitely many distinguishable internal states, coupled to the complement $H = S \setminus V$ through $\varphi$.

This definition formalizes three features implicit in the concept of observation: there is a whole ($S$), the observer is not the whole ($V \subsetneq S$), and the observer registers changes (coupling through $\varphi$). From this definition, three structural properties follow.

**Lemma 1** (Finiteness). *The observer has finitely many distinguishable internal states, so the visible configuration space $\mathcal{C}_V$ is finite, with a discreteness scale $\epsilon$ providing a finite minimal cell volume.* This is a structural postulate about the observer, motivated by the fact that a finite-memory observer can register only finitely many outcomes and by holographic entropy bounds [2] that independently predict a finite Hilbert-space dimension for any bounded region. Strict classical field theory would permit infinitely many modes on a finite boundary; the finiteness assumed here is at least as strong as a UV cutoff and is taken as part of the definition of embedded observation rather than derived from outside physics.

**Lemma 2** (Causal partition). *The observer is a proper subsystem: $V \subsetneq S$. The complement $H = S \setminus V$ is the hidden sector.* This partition is not a modeling choice but the definition of embedded observation: an observer that could access all of $S$ would have nothing external to observe. The product decomposition

$$\Gamma = \Gamma_V \times \Gamma_H, \qquad H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

follows, with cross-partition correlations entering only through $H_{\text{int}}$. The product decomposition is idealized; §4.5 addresses approximation quality.

**Lemma 3** (Determinism and unique measure). *$\varphi$ is a bijection: distinct states have distinct successors (determinism) and distinct predecessors (reversibility). The counting measure on $S$ is the unique $\varphi$-invariant measure.* Determinism (injectivity) is the requirement that the dynamics preserves the observer's records — non-injective evolution would merge distinct total states, erasing the distinction between outcomes the observer has already recorded. On a finite set, injectivity implies surjectivity, so $\varphi$ is a bijection. The invariant counting measure, in the continuum limit, becomes the Liouville measure on $\Gamma$:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\} \equiv \mathcal{L}\rho$$

These properties contain no quantum postulates. The claim is that quantum mechanics *emerges* under the conditions below.

### 1.3 Conditions on the Hidden Sector

**(C1) Non-zero coupling.** $H_{\text{int}} \neq 0$. The coupling is bidirectional.

**(C2) Slow-bath timescale separation.** The visible-sector (system) timescale $\tau_S$ is much shorter than the hidden-sector (bath) timescale $\tau_B$: $\tau_S \ll \tau_B$ — the *inverse* of the Markovian regime. The hidden sector evolves on timescales far exceeding those accessible to the observer.

**(C3) Sufficient capacity.** The number of hidden-sector degrees of freedom $N_H$ exceeds the number of visible-sector degrees of freedom $N_V$ by enough that visible-sector interactions do not appreciably perturb the hidden sector's state on timescales $\ll \tau_B$.

**Theorem statement.** Under Lemmas 1–3 and (C1)–(C3), the embedded observer's reduced description is mathematically equivalent to unitarily evolving quantum mechanics (defined precisely in §3.4). The conditions are not merely sufficient but *necessary* (§3.4) — unconditionally for (C1) and (C3), and conditionally on the eigenstate thermalization hypothesis (ETH) in the hidden sector for (C2) — establishing full equivalence within this scope.

### 1.4 Partition-Relativity

**Lemma.** *The emergent description is uniquely determined by the partition. Any parameters of the emergent theory depend only on the geometric and thermodynamic properties of the partition boundary.*

*Proof.* By Lemma 3, the Hamiltonian flow $\phi_t$ is unique. By Lemma 2, the partition is fixed. By Lemma 3, the observer uses the Liouville measure $\mu$ — the unique absolutely continuous invariant measure on the full phase space. (An embedded observer with incomplete knowledge of the total energy averages over energies with a smooth prior, recovering Liouville on a phase-space band; singular invariant measures are excluded by Lemma 3.) Letting $\pi_V$ denote projection onto the visible sector, the marginalized transition probabilities

$$T_{ij}(t_2, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu(h)$$

are therefore uniquely determined by three inputs: dynamics ($\phi_t$), partition ($\Gamma_V, \Gamma_H$), and measure ($\mu$). Since $\phi_t$ and $\mu$ are fixed by the definition and lemmas, the stochastic process — and hence any emergent quantum description (§3.1) — depends only on the partition. $\square$

## 2. EMERGENT STOCHASTICITY AND P-INDIVISIBILITY

### 2.1 Emergent Stochasticity

The total system evolves deterministically, but the visible sector alone is stochastic. The observer knows $x$ but not $h$; different hidden states $h_k$ compatible with the same $x$ send it to different futures $x'_k$. Transition probabilities are obtained by marginalizing over the Liouville measure (§1.4). This makes the framework a hidden variable theory; consistency with Bell's theorem is addressed in §3.3.

### 2.2 The Slow-Bath Regime

The Markovian limit requires $\tau_B \ll \tau_S$ [3]. Condition (C2) inverts this: $\tau_S \ll \tau_B$. A slow bath must be distinguished from a static field. By (C1), coupling is continuously active: each visible-sector transition imprints on the hidden sector. Because the hidden sector is slow (not static), imprints persist without thermal overwriting. On subsequent transitions, coupling reads back stored correlations, producing history-dependent transition probabilities — the non-Markovian regime [3].

### 2.3 P-Indivisibility

By Lemma 1, the visible and hidden sectors have finite configuration spaces $\mathcal{C}_V$ and $\mathcal{C}_H$ (the discrete counterparts of $\Gamma_V$ and $\Gamma_H$). On these finite sets:

**Theorem.** *Let $\mathcal{C}_V$ and $\mathcal{C}_H$ be finite sets with $|\mathcal{C}_V| \geq 2$, and let $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ be a bijection. Define:*

$$T_{ij} = \frac{|\{h \in \mathcal{C}_H : \pi_V(\varphi(x_i, h)) = x_j\}|}{|\mathcal{C}_H|}$$

*and the $k$-step matrix $T^{(k)}_{ij}$ by applying $\varphi^k$. If $T$ is not a permutation matrix, then the process is P-indivisible.*

*Proof.* Uses total variation distance $d(p, q) = \frac{1}{2}\sum_k |p_k - q_k|$. P-divisibility $\iff$ $d(p(t), q(t))$ non-increasing for all initial $p, q$ [4, 5].

*Step 1 (Recurrence).* $\varphi$ bijective on a finite set $\Rightarrow$ $\exists N: \varphi^N = \text{id}$. Thus $T^{(N)} = I$ and $d(\delta_i T^{(N)}, \delta_j T^{(N)}) = 1$ for $i \neq j$.

*Step 2 (Strict contraction).* $T$ not a permutation $\Rightarrow$ $\exists i, j, l$: $T_{il} > 0$ and $T_{jl} > 0$. Then:

$$d(\delta_i T, \delta_j T) = \frac{1}{2}\sum_k |T_{ik} - T_{jk}| < 1$$

*Step 3.* $d(\delta_i T^{(1)}, \delta_j T^{(1)}) < 1 = d(\delta_i T^{(N)}, \delta_j T^{(N)})$: non-monotonic, hence P-indivisible. $\square$

The theorem requires only bijective dynamics (Lemma 3) and non-trivial coupling (C1). Lemma 1 guarantees the finite configuration space.

**Convergence with prior work.** The theorem converges with independent results: Pechukas [6] (reduced dynamics need not preserve positivity), Rivas et al. [4, 5] (divisibility failure ↔ information backflow), Pollock et al. [7] (process-tensor Markovianity conditions), and Strasberg and Esposito [8] (non-Markovian reduced dynamics in the slow-bath regime of C2). Bylicka, Johansson, and Acín [9] prove, for bijective dynamical maps on the quantum side, a constructive equivalence between CP-divisibility and monotonic non-increase of distinguishability under an ancilla-assisted witness — strengthening the divisibility/information-backflow correspondence when the reduced dynamics is itself invertible. The substratum dynamics $\varphi$ is bijective on $\mathcal{C}_V \times \mathcal{C}_H$, but the marginal stochastic matrix $T(t)$ on $\mathcal{C}_V$ is generally not invertible — projecting onto the visible sector loses information. The Bylicka setup therefore applies in full strength when $T(t)$ happens to have full rank (which includes the minimal model of §2.4 below, where $\det T(1) = 1/3 \neq 0$); for the general derivation here, the load-bearing property is P-indivisibility of the marginal process, which is exactly what §3.1's stochastic-quantum correspondence requires. Milz et al. [10] further show that even CP-divisibility does not guarantee Markovianity in the process-tensor sense, confirming that the non-Markovian character identified here is robust under all current definitions.

**Continuous-time extension.** The Hamiltonian flow on finite-dimensional phase space preserves Liouville measure on compact energy surfaces. $T_{ij}(t)$ is continuous with $T(0) = I$. By (C1), $T(t)$ departs from the permutation class for $t > 0$. By Poincaré recurrence, $\exists t_R$: the set of hidden states with $\pi_V(\varphi_{t_R}(x_i, h)) = x_i$ has measure $> 1 - \delta$ for any $\delta > 0$. For small $\delta$, this gives non-monotonic trace distance, establishing P-indivisibility in continuous time.

The recurrence argument establishes P-indivisibility in principle. The following lemma shows that under (C2), information backflow occurs on observable timescales — not merely at Poincaré recurrence times.

**Lemma (Accessible-timescale backflow).** *Under (C1)–(C3) with $\tau_S \ll \tau_B$, the non-Markovian mutual information $I(X_{<t}; X_{>t} \mid X_t)$ is $\mathcal{O}(1)$ for observation windows $t \sim k\tau_S$ with $k\tau_S \ll \tau_B$.*

*Proof.* The coupling $H_{\text{int}}$ transfers visible-sector information to the hidden sector at each interaction, at rate $\sim 1/\tau_S$. Between interactions, the hidden sector evolves under $H_H$; under the ETH assumption on $H_H$, the effective dephasing rate of correlations conditional on the previous visible state is $\sim 1/\tau_B$. The decay of correlations stored in the hidden sector is governed by $e^{-\tau_S/\tau_B}$. When $\tau_S \ll \tau_B$, $\tau_S/\tau_B \ll 1$, so the decay per visible-sector transition is $1 - e^{-\tau_S/\tau_B} \approx \tau_S/\tau_B \ll 1$: correlations survive each step essentially intact. After $k$ transitions spanning a time $k\tau_S \ll \tau_B$, the cumulative decay is $e^{-k\tau_S/\tau_B} \approx 1 - k\tau_S/\tau_B$, which remains close to unity. The hidden sector therefore retains $\sim k$ bits of visible-sector history over this window, and the $(k+1)$-th transition reads back stored correlations through $H_{\text{int}}$, producing history-dependent transition probabilities — i.e., information backflow. More precisely, the mutual information satisfies:

$$I(X_{<t}; X_{>t} \mid X_t) \geq I_0\left(1 - \frac{k\tau_S}{\tau_B}\right)$$

where $I_0 > 0$ is the single-step information transfer from (C1). For $k\tau_S \ll \tau_B$, this remains $\mathcal{O}(I_0)$ — comparable to the single-step coupling strength, not exponentially suppressed. The bound saturates (C3): the maximum storable history is $\log_2 m$ bits (§3.4), so persistent backflow over $K$ transitions requires $m \geq 2^K$, which is amply satisfied when $N_H \gg N_V$. $\square$

**Role of (C2) and (C3).** The Poincaré recurrence argument and the accessible-timescale lemma are independent: the former establishes P-indivisibility from (C1) and finiteness alone; the latter shows that (C2) and (C3) promote it from a formal property to an observationally dominant one.

**Weak-coupling and fast-bath regimes.** Known P-divisible systems with non-zero coupling illustrate the necessity of (C2), not a failure of the theorem. The Jaynes-Cummings model with Lorentzian spectral density is P-divisible when dissipation dominates coupling — the fast-bath regime ($\tau_B \ll \tau_S$), violating (C2). The Davies-Merkli Markovian convergence theorem likewise applies in the Born-Markov (fast-bath) limit. The §3.4 necessity proof for (C2) establishes this formally.

### 2.4 Explicit Construction: A Minimal Model

Visible sector: $x \in \{0, 1\}$. Hidden sector: $h \in \{1, \ldots, 6\}$. Dynamics: the permutation

$$\sigma = (0{,}1 \leftrightarrow 1{,}1)\;(0{,}2 \leftrightarrow 1{,}2)\;(0{,}3 \leftrightarrow 0{,}4)\;(0{,}5 \leftrightarrow 0{,}6)\;(1{,}3 \leftrightarrow 1{,}4)\;(1{,}5 \leftrightarrow 1{,}6)$$

satisfying (C1)–(C3). Since $\sigma^2 = \text{id}$: at $t = 1$, two of six hidden states flip $x$, giving

$$T(1,0) = \begin{pmatrix} 2/3 & 1/3 \\ 1/3 & 2/3 \end{pmatrix}$$

At $t = 2$ ($\sigma^2 = \text{id}$): $T(2,0) = I$. A Markov chain would predict continued mixing: $T(1,0)^2 = \left(\begin{smallmatrix} 5/9 & 4/9 \\ 4/9 & 5/9 \end{smallmatrix}\right)$. The actual dynamics show complete *un-mixing*. Computing the intermediate propagator:

$$\Lambda(2,1) = T(2,0) \cdot [T(1,0)]^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

Negative entries — no valid stochastic matrix exists. **P-indivisible.** $\square$

**Independent check (process-tensor non-Markovianity).** The same model also fails the Pollock et al. [7] multi-time Markov condition without invoking $T(t)$-invertibility: $P(x_2 = 0 \mid x_1 = 1, x_0 = 0) = 1$ versus $P(x_2 = 0 \mid x_1 = 1) = 1/3$. Conditioning on $x_0$ changes the one-step prediction from $1/3$ to $1$ — a memory effect computed directly from multi-time conditional probabilities, valid regardless of $\det T(t)$. The non-Markovian character is therefore confirmed under both the divisibility-based criterion (Rivas et al. [4, 5]; Bylicka et al. [9] in the invertible case) and the process-tensor criterion (Pollock et al. [7] in the general case).

**The mechanism.** The hidden sector acts as a memory register. The transpositions $(0,h) \leftrightarrow (1,h)$ for $h \in \{1, 2\}$ flip $x$ while preserving $h$, so a state at $x = 1$ with $h \in \{1, 2\}$ after step 1 carries the record "I was at $x = 0$." Step 2 reads this record and flips $x$ back — information backflow impossible for a memoryless process. P-indivisibility is more extreme, not less, when memory is more persistent.

---

## 3. THE EMERGENCE OF QUANTUM MECHANICS

### 3.1 The Stochastic-Quantum Correspondence

By Barandes' correspondence [11, 12], any P-indivisible stochastic process on a finite configuration space of size $n$ embeds into a unitarily evolving quantum system on $\mathcal{H}$ of dimension $\leq n^3$. P-indivisible transition matrices develop negative entries at fine time resolution; the Stinespring dilation theorem guarantees $\exists$ a Hilbert space and unitary $U(t)$ with $T_{ij}(t) = |U_{ij}(t)|^2$ — transition probabilities are exactly Born-rule probabilities. The proof requires a finite-dimensional configuration space (Lemma 1); Calvo [13] extends the correspondence to infinite dimensions, but this is not required here. Pimenta [14] distinguishes P-divisible and P-indivisible stochastic-quantum dynamics: the correspondence is non-trivial only in the P-indivisible regime, which is precisely the regime produced by §2.3. An independent derivation using only Stinespring's dilation theorem [15] and standard partial-trace properties [16] is given in §3.2; either route alone suffices.

**Independent corroboration of the trace-out mechanism.** The technical move from a deterministic substrate to non-Markovian visible dynamics via the trace-out of inaccessible degrees of freedom — central to both routes — is now established at theorem level in the open systems literature. Brandner [17, 18] proves that for autonomous linear evolution equations, integrating out inaccessible degrees of freedom (whether external environments or internal subsystems) yields well-defined non-Markovian visible dynamics in a controlled weak-memory regime, with explicit error bounds and a convergent perturbation scheme. This is the mathematical apparatus the present construction relies upon, derived independently for general open systems. Direct experimental demonstrations of the mechanism include Mehl et al. [19], who showed that hidden slow degrees of freedom in a colloidal system produce non-Markovian visible dynamics violating naive Markovian fluctuation theorems, and Gröblacher et al. [20], who observed non-Markovian Brownian motion in a macroscopic micromechanical oscillator. On the quantum side, Kim [21] shows that monitored quantum systems are formally quantum hidden Markov models, with a rigorous correspondence to classical hidden Markov models for setups involving Haar-random unitaries and measurements — the same formal structure as the stochastic-quantum bridge. The framework's central technical move is therefore standard rather than speculative.

**From phase space to configuration space.** The transition probabilities $T_{ij}$ are projections of the full phase-space flow onto the configuration sector of $\Gamma_V$, with momenta and hidden-sector degrees of freedom absorbed into the Liouville marginalization. The resulting process lives on the discrete configuration space of Lemma 1.

Three features emerge. The Schrödinger equation arises from the differentiability of $U(t)$. The Born rule is the equilibrium distribution of the indivisible process [11, 12]. The action scale $\hbar$ enters when defining $\hat{H}(t) \equiv i\hbar \, \partial_t U \cdot U^\dagger$, converting dimensionless rates to energy units; its value requires additional physical input from the partition.

**Phase uniqueness from continuous-time data.** The relation $T_{ij}(t) = |U_{ij}(t)|^2$ discards phase information at any single time. Doukas [22] identifies this gap for discrete-time data. The resolution: continuous-time data $\{T_{ij}(t)\}_{t \in \mathbb{R}}$ provides strictly more information.

**Lemma (phase-locking).** *Let $H$ be Hermitian on $\mathbb{C}^n$ with eigenbasis $\{|k\rangle\}$, eigenvalues $\{E_k\}$, and $V_{ik} = \langle i | k \rangle$. Assume: (G1) non-degenerate spectrum; (G2) non-degenerate energy gaps; (G3) $V_{ik} \neq 0$ for all $i, k$. Then $T_{ij}(t) = |\langle i | e^{-iHt} | j \rangle|^2$ for all $i, j, t$ uniquely determines $H$ up to an overall energy shift and basis phase conventions.*

*Proof.* Write:

$$T_{ij}(t) = \sum_{k,l} V_{ik}\, V_{jk}^*\, V_{jl}\, V_{il}^*\; e^{-i(E_k - E_l)t}$$

By (G2), the frequencies $\omega_{kl} = E_k - E_l$ are distinct for distinct pairs with $k \neq l$. Fourier-transforming yields:

$$a_{ij}^{kl} = V_{ik}\, V_{jk}^*\, V_{jl}\, V_{il}^*$$

The moduli $|V_{ik}|$ follow from $a_{ii}^{kl} = |V_{ik}|^2 |V_{il}|^2$ (non-zero by (G3)): the rank-1 outer-product structure determines $|V_{ik}|^2$ up to a global scale, and unitarity $\sum_k |V_{ik}|^2 = 1$ fixes the scale. The phases carry a double-difference structure:

$$\arg(a_{ij}^{kl}) = (\varphi_{ik} - \varphi_{il}) - (\varphi_{jk} - \varphi_{jl})$$

The gauge freedom preserving all double differences is $\varphi_{ik} \to \varphi_{ik} + \alpha_i + \beta_k$ (physically irrelevant basis rephasing). Fixing $\varphi_{1k} = 0$, $\varphi_{i1} = 0$, each remaining phase is $\varphi_{ik} = \arg(a_{i1}^{k1})$, directly extracted from Fourier data. $H = V \, \text{diag}(E_k) \, V^\dagger$ is unique up to energy shift and phase conventions. $\square$

Conditions (G1)–(G3) fail only on a measure-zero set of Hamiltonians. A stronger argument applies whenever the partition itself breaks symmetries of $H_{\text{tot}}$. The genericity conditions concern the *effective* visible-sector Hamiltonian $\hat{H}_{\text{eff}}$ — the operator emerging after the trace-out — not the total Hamiltonian $H_{\text{tot}}$. The trace-out generically breaks the symmetries of $H_{\text{tot}}$ because the partition boundary does not respect them: a partition centered on a specific observer breaks translational invariance, rotational symmetry about distant points, and boost invariance. Any degeneracy in $H_{\text{tot}}$ that relies on correlations between visible and hidden sectors — which includes all degeneracies associated with symmetries the partition breaks — is lifted in $\hat{H}_{\text{eff}}$. The residual degeneracies of $\hat{H}_{\text{eff}}$ fall into two classes: continuous symmetries acting entirely within the visible sector that commute with the trace-out — precisely the gauge symmetries of the emergent description, which correspond to physically equivalent states and do not affect the phase-locking argument (it operates on gauge-inequivalent transition data); and discrete residual symmetries (e.g. reflections internal to $V$ surviving the trace-out) which would produce finite-order degeneracies, are lifted generically by any perturbation of the partition boundary, and in the surviving cases yield $H$ up to a finite permutation of eigenlabels that is physically inert. $\hat{H}_{\text{eff}}$ therefore satisfies G1–G3 not by typicality in an abstract ensemble but because the partition itself acts as a symmetry-breaking mechanism, with any residual discrete ambiguity absorbed into gauge equivalence.

### 3.2 Independent Derivation via Stinespring Dilation

An independent derivation of the emergent quantum description uses only Stinespring's dilation theorem [15] and standard properties of the partial trace [16], without invoking the stochastic-quantum correspondence of §3.1. The two routes are logically independent; either alone suffices.

**Setup.** The finite configuration spaces $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ and $\mathcal{C}_H = \{h_1, \ldots, h_m\}$ (Lemma 1) embed into Hilbert spaces $\mathcal{H}_V = \mathbb{C}^n$ and $\mathcal{H}_H = \mathbb{C}^m$ via $|i\rangle \leftrightarrow x_i$ and $|k\rangle \leftrightarrow h_k$. This introduces no quantum postulates: it is the canonical identification of probability distributions on a finite set with diagonal density matrices.

**Lemma (permutation unitarity).** *Any bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ defines a unitary $U_\varphi$ on $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$.*

*Proof.* Define $U_\varphi |i, k\rangle = |\varphi(x_i, h_k)\rangle$. Since $\varphi$ is a bijection, $U_\varphi$ permutes the orthonormal basis, hence is unitary. $\square$

For continuous-time dynamics $\varphi_t$, Stone's theorem on $\mathcal{H}$ yields $U_t = e^{-i\hat{H}t}$ for Hermitian $\hat{H}$.

**Lemma (Reverse direction: stochastic process → bijection).** *Let $\mathcal{S}$ be a stochastic process on a finite configuration space $\mathcal{C}_V$ with $|\mathcal{C}_V| = n$, specified by a finite family of $k$-step transition matrices $\{T(k)\}_{k=1}^K$. Then there exist a finite set $\mathcal{C}_H$ and a bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ such that the $k$-step marginalization of $\varphi^k$ with uniform prior on $\mathcal{C}_H$ reproduces $T(k)$ (exactly for rational transition probabilities; to arbitrary precision otherwise) for all $k \leq K$.*

*Proof.* Each $T(k)$ arising as a marginal of a bijection with uniform prior is doubly-stochastic: row sums are $1$ by normalisation of the prior, column sums are $1$ because $\varphi^k$ is a bijection. By Birkhoff–von Neumann, $T(k) = \sum_\sigma p_\sigma^{(k)} \Pi_\sigma$ is a convex combination of permutation matrices with rational weights (after rational approximation, if required). Take $\mathcal{C}_H$ large enough to encode, via a standard history-dilation construction, the joint choices of permutations at each of the $K$ time steps; the resulting joint dynamics is a bijection by construction and its $k$-step marginal reproduces $T(k)$. This is the classical substrate of the unitary dilation in [11, 12]. $\square$

*Remark.* This establishes bidirectional correspondence at the stochastic-process level: every stochastic process on $\mathcal{C}_V$ arises as marginalization of a permutation-bijection on $\mathcal{C}_V \times \mathcal{C}_H$ with uniform prior. It is not a correspondence at the full CPTP-channel level — a permutation-unitary with uniform ancilla maps basis-state inputs to diagonal outputs, so coherence-creating channels have no such direct realisation. This is the appropriate scope for the characterization theorem (§3.4), which is formulated in terms of transition probabilities. The holographic bound $\dim \mathcal{H} \leq e^{A/4}$ bounds the size of the emergent $\mathcal{H}_V$ for any bounded region. This is the reverse direction invoked by [Substratum, Theorem 23, Stage 1].

**The quantum channel.** The observer's ignorance of the hidden sector (Lemma 3) corresponds to $\rho_H = I_m/m$. The visible-sector quantum channel is

$$\Phi(\rho_V) = \mathrm{Tr}_H\!\left[U_\varphi\,(\rho_V \otimes \rho_H)\,U_\varphi^\dagger\right]$$

This is CPTP by a standard result [16, Theorem 8.1], with Kraus representation $\Phi(\rho_V) = \sum_{k,l} K_{kl}\,\rho_V\,K_{kl}^\dagger$ where $K_{kl} = m^{-1/2}\langle l|U_\varphi|k\rangle_H$. The triple $(\mathcal{H}_H, U_\varphi, \rho_H)$ is the Stinespring dilation [15] of $\Phi$.

**Theorem (Born rule recovery).** *The classical transition probabilities $T_{ij}$ (§1.4) equal the Born-rule probabilities of $\Phi$.*

*Proof.* $P(j|i) = \langle j|\Phi(|i\rangle\langle i|)|j\rangle = m^{-1}\sum_{k,l} |\langle j,l|U_\varphi|i,k\rangle|^2$. Since $U_\varphi$ is a permutation, $\langle j,l|U_\varphi|i,k\rangle = \delta_{(j,l),\varphi(i,k)}$. Thus $P(j|i) = m^{-1}\sum_k \delta_{j,\pi_V(\varphi(x_i,h_k))} = T_{ij}$. $\square$

**Theorem (emergent coherence).** *If $T$ is not a permutation matrix (condition (C1)), then $\Phi$ generates genuine quantum coherence: it is not entanglement-breaking.*

*Proof.* If $T$ is not a permutation, some initial state $|i\rangle$ maps to at least two distinct outputs, so $\Phi(|i\rangle\langle i|)$ has rank $\geq 2$. By linearity, $\Phi$ maps some off-diagonal input $|i\rangle\langle j|$ to a non-zero operator, precluding the measure-and-prepare form of entanglement-breaking channels. $\square$

**Theorem (CP-indivisibility).** *The P-indivisibility of §2.3 implies CP-indivisibility of $\{\Phi_t\}$: there exist $t_2 > t_1 > 0$ with no CPTP map $\Lambda$ satisfying $\Phi_{t_2} = \Lambda \circ \Phi_{t_1}$.*

*Proof.* CP-divisibility restricted to diagonal inputs reduces to P-divisibility. The contrapositive gives the result. $\square$

By the Breuer-Laine-Piilo criterion [3, 4], CP-indivisibility implies non-monotonic trace distance (information backflow) — the quantum signature of non-Markovianity.

**Approximate unitarity.** On observable timescales $t \ll \tau_B$, the hidden-sector state is approximately frozen (conditions (C2)–(C3)). The channel generator decomposes as $d\Phi_t/dt|_{t=0}(\rho_V) = -i[\hat{H}_{\text{eff}}, \rho_V] + \mathcal{D}(\rho_V)$ with $\mathcal{D} \sim \mathcal{O}(\tau_S/\tau_B)$. The leading-order dynamics is the Schrödinger equation. The phase-locking lemma (§3.1) then determines $\hat{H}_{\text{eff}}$ uniquely from continuous-time transition data, up to the residual diagonal-unitary rephasing freedom that is physically trivial (basis convention).

**Comparison of routes.**

| | Barandes route (§3.1) | Stinespring route (§3.2) |
|---|---|---|
| Input | P-indivisible process on $\mathcal{C}_V$ | Bijection on $\mathcal{C}_V \times \mathcal{C}_H$ + marginalization |
| Bridge | Stochastic-quantum correspondence [11, 12] | Stinespring dilation [15] + partial trace [16] |
| Output | Unitary with $T_{ij} = |U_{ij}|^2$ | CPTP channel with $T_{ij} = \langle j|\Phi(|i\rangle\langle i|)|j\rangle$ |
| Born rule | Equilibrium of indivisible process | Partial trace structure (above) |
| Scope | Any P-indivisible process | Processes from marginalized bijections |

The Barandes route is more general (any P-indivisible process); the Stinespring route requires only textbook results [15, 16] and delivers additional structure: the tensor product $\mathcal{H}_V \otimes \mathcal{H}_H$, genuine quantum coherence, CP-indivisibility, and approximate unitarity with $\mathcal{D} \sim \mathcal{O}(\tau_S / \tau_B) \sim 10^{-32}$. The two routes agree on all observables — both produce the same $T_{ij}(t)$ — establishing that the emergence of QM is robust and overdetermined. The Barandes route powers (ii) $\implies$ (i) in the characterization theorem; the Stinespring route supplies (iii) $\implies$ (i) independently.

### 3.3 Bell Inequality Violations

The framework is a hidden variable theory evading Bell's theorem [23] not by superdeterminism but by violating factorizability through P-indivisible joint dynamics — while remaining causally local. Two subsystems interacting at preparation carry a joint transition matrix $T_{QR} \neq T_Q \otimes T_R$. This non-factorizability *is* stochastic entanglement [11, 12, 24]. Since the process is indivisible, no well-defined intermediate conditional probabilities permit Bell's factorization.

In the Jarrett decomposition, the framework violates outcome independence while preserving parameter independence and measurement independence — precisely the class Fine's theorem [25] permits. Barandes, Hasan, and Kagan [24] prove the maximum CHSH correlator is exactly Tsirelson's bound $2\sqrt{2}$, with independent support from Le et al. [26]. The bound also follows from the Stinespring route of §3.2, which establishes full unitary QM on a tensor-product Hilbert space; Tsirelson's original operator-norm argument [27] then yields $|\langle S \rangle| \leq 2\sqrt{2}$; achievability follows because all quantum states, including maximally entangled ones, are realizable in the emergent description.

**Fine-tuning and causal structure.** The framework does not claim to restore Bell locality: outcome independence is genuinely violated. What it provides is a *derivation* of this nonlocality from the causal partition, rather than treating it as axiomatic. The fine-tuning objection (Wood and Spekkens, 2015) assumes DAG causal structure with Markov factorization; P-indivisible processes violate the Markov condition on any DAG, so the appropriate framework is the process tensor [7], within which no-signaling follows from marginalization structure without fine-tuning.

**Parameter independence from spatial locality.** Let $V_A$ and $V_B$ be space-like separated visible-sector subsystems with disjoint coupling neighborhoods on $G_\varphi$. The spatial Markov property of range-1 dynamics (the area-law lemma: for spatially local bijections, the mutual information between two regions depends only on their shared boundary; stated and proved in [SM §3.2]) makes $V_A$ and $V_B$ conditionally independent given boundary data. Alice's measurement setting $a$ determines which function she evaluates on $V_A$; it does not alter the transition probabilities for $V_B$, which depend only on $V_B$'s local coupling neighborhood. Hence $P(x_B \mid a, b) = P(x_B \mid b)$ — parameter independence holds structurally for all bounded-degree graph topologies with range-1 coupling, with no fine-tuning of the hidden-variable distribution. Combined with the outcome-independence violation from stochastic entanglement, this gives the precise Jarrett decomposition.

### 3.4 The Characterization Theorem: Necessity of the Conditions

The logical structure: Barandes' correspondence gives QM $\iff$ P-indivisibility. What remains is P-indivisibility $\implies$ embedded observation under (C1)–(C3).

**Dilation existence.** Any stochastic process on a finite configuration space can be realized as marginalization of a deterministic process on a larger state space — furnishing Lemmas 1–3.

**Theorem (C1 equivalence).** *The marginalized process is P-indivisible iff $T$ is not a permutation matrix.*

*Proof.* Forward: §2.3. Reverse: if $T$ is a permutation, $\Lambda(k_2, k_1) = T^{(k_2-k_1)}$ is a valid stochastic matrix for all $k_2 > k_1$ $\Rightarrow$ P-divisible. $\square$

**Theorem (C2 necessity, conditional on ETH).** *Assume the hidden-sector Hamiltonian $H_H$ satisfies the eigenstate thermalization hypothesis (ETH) [17, 18]. Then in the fast-bath regime ($\tau_B \ll \tau_S$), the hidden sector dephases to its diagonal ensemble between coupling events, so the marginal dynamics on $\mathcal{C}_V$ is Markovian on accessible timescales ($T^{(k)} = T^k$) and hence P-divisible. Contrapositively, observable P-indivisibility in an ETH hidden sector requires $\tau_S \ll \tau_B$.*

*Proof.* Between coupling events (separated by $\tau_S$), the hidden sector evolves under its own Hamiltonian $H_H$. The substratum dynamics is reversible, so there is no relaxation in the strict sense — finite-dimensional Hamiltonian flow has purely imaginary spectrum and Poincaré recurrence at $t_R$ exponentially large in the system size. What does occur, under the ETH assumption, is *dephasing*: starting from any distribution $\mu_H(\cdot | x_i)$ conditioned on the previous visible state, the off-diagonal matrix elements in the energy basis decay on the timescale $\tau_B \sim \hbar / \Delta E$, where $\Delta E$ is the hidden sector's typical energy spread. After dephasing, the diagonal ensemble agrees with the microcanonical distribution to corrections exponentially small in the hidden-sector size, so for any few-body visible-sector observable $O_V$ and any time $\tau_S \gg \tau_B$:

$$\big| \langle O_V \rangle_{\mu_H(\tau_S | x_i)} - \langle O_V \rangle_{\text{eq}} \big| \;\lesssim\; \tau_B / \tau_S$$

In the fast-bath regime ($\tau_B \ll \tau_S$) this is parametrically small: from the visible sector's perspective the hidden sector "looks" thermalized at every coupling event regardless of its post-coupling state, even though the underlying trajectory remains reversible and quasi-periodic with recurrence only at $t \sim t_R$. Each single-step transition matrix $T$ is therefore computed against the same effective equilibrium distribution, so $T^{(k)} = T^k$ — a homogeneous Markov chain on accessible timescales $t \ll t_R$, hence P-divisible in the observable sense.

Contrapositively: observable P-indivisibility requires $\tau_S \lesssim \tau_B$ — the visible sector must couple back into the hidden sector before dephasing erases the memory. For the strong, persistent P-indivisibility of the characterization theorem, the separation must be $\tau_S \ll \tau_B$. The continuous-time extension to general Hamiltonian flow replaces the collision-model picture with the full ETH/dephasing condition; the relevant machinery for chaotic open quantum systems in the weak-memory regime is established in [3, 8, 17, 18]. $\square$

**Remark (Status of ETH).** *The eigenstate thermalization hypothesis is a well-supported conjecture, not a theorem, for generic chaotic many-body Hamiltonians. It is proved for specific models (random matrix ensembles, certain integrable-chaotic transitions) and supported by extensive numerical evidence across many systems [17, 18]. For the OI framework's hidden sector — the cosmological-horizon complement, a generic chaotic many-body system — ETH is the standard assumption. The C2 necessity direction is therefore conditional on ETH; relaxations or failures of ETH would require a separate argument. The C1 and C3 necessity theorems do not depend on ETH.*

**Remark (Consequence for the characterization theorem).** *The full biconditional (i) ⇔ (ii) ⇔ (iii) of the characterization theorem below is similarly conditional on ETH for the (ii) ⇒ (iii) direction specifically. The other directions — (i) ⇔ (ii) from [11, 12]; (iii) ⇒ (ii) from §2.3; C1 and C3 necessity from their own proofs — are unconditional.*

**Theorem (C3 necessity).** *Let $m = |\mathcal{C}_H|$. The non-Markovian mutual information satisfies:*

$$I(X_{<t} ; X_{>t} \mid X_t) \leq \log_2 m$$

*Proof.* The total system is deterministic: $X_{>t}$ is a function of $(X_t, H_t)$. Conditioning on $X_t$: $X_{<t} \to H_t \to X_{>t}$ is a Markov chain. By data processing:

$$I(X_{<t} ; X_{>t} \mid X_t) \leq I(X_{<t} ; H_t \mid X_t) \leq H(H_t \mid X_t) \leq \log_2 m \quad \square$$

**Corollary.** P-indivisibility across $n$ visible configurations requires $m \geq n$. Sustained information backflow at rate $I_0 > 0$ per coupling event over $K$ events requires $m \gtrsim 2^{K I_0}$ — exponential growth in the observation window, of which the framework's qualitative (C3) ("hidden sector large enough") is a conservative restatement. $\square$

**Definition (unitarily evolving QM at the transition-probability level).** A stochastic process $\mathcal{S}$ on a finite configuration space $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ is *mathematically equivalent to unitarily evolving quantum mechanics at the transition-probability level* if there exists a Hilbert space $\mathcal{H}_V$ of dimension $\leq n^3$, a Hermitian operator $\hat{H}$ on $\mathcal{H}_V$, and a unitary family $U(t) = e^{-i\hat{H}t}$ such that $T_{ij}(t) = |U_{ij}(t)|^2$ for all $i, j, t$ — i.e., computational-basis transition probabilities are exactly Born-rule probabilities. This definition captures the Hilbert space, unitary dynamics, and the Born rule for transitions between the classical-basis states $\mathcal{C}_V$ inherits from the partition. Additional quantum-mechanical structures — superposition inputs, entangled initial states, sequential-measurement state update, and multi-particle structure — are addressed in the remarks following the theorem, where they are shown to emerge from the Stinespring construction of §3.2 rather than requiring independent postulates, but their derivation lies outside the scope of the equivalence proved below.

**Characterization theorem.** *Let $\mathcal{S}$ be a stochastic process on a finite configuration space $\mathcal{C}_V$ with $|\mathcal{C}_V| \geq 2$, and consider dynamics on accessible timescales $t \ll t_R$ where $t_R$ is the Poincaré recurrence time of any realizing substrate. Assume the hidden sector of any candidate realization satisfies ETH [17, 18]. Then the following are equivalent:*

*(i) $\mathcal{S}$ is mathematically equivalent to unitarily evolving QM at the transition-probability level (in the sense of the preceding definition).*

*(ii) $\mathcal{S}$ is P-indivisible on accessible timescales — i.e., information backflow occurs at $t \ll t_R$, not merely at the formal Poincaré recurrence time.*

*(iii) $\mathcal{S}$ arises from marginalizing a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$ with (C1) non-trivial coupling, (C2) slow-bath memory ($\tau_S \ll \tau_B$), and (C3) sufficient capacity.*

*Proof.* (i) $\iff$ (ii): Barandes [11, 12], on accessible timescales by construction (the equivalence is formulated for the dynamics observers can resolve, not for behavior at recurrence times). (iii) $\implies$ (ii): §2.3, where the accessible-timescale lemma upgrades the bare recurrence-based P-indivisibility (which follows from C1 alone) to information backflow on observable timescales using C2 and C3. (ii) $\implies$ (iii): the necessity theorems above — C1 from the equivalence with non-permutation $T$, C2 from the dephasing argument (without C2, $T$ becomes Markovian on accessible timescales and information backflow disappears), C3 from the data-processing bound. $\square$

QM is not merely *compatible with* embedded observation — it is *equivalent to* it.

**Remark (scope of the equivalence).** The characterization theorem establishes the Hilbert space, unitary dynamics, and Born-rule transition probabilities. Four further structures of operational quantum mechanics merit comment.

*(i) Tensor product structure (visible–hidden).* The Stinespring route (§3.2) constructs $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$ and derives the CPTP channel $\Phi$ by partial trace. The visible–hidden tensor product is therefore given by the construction, not postulated.

*(ii) Tensor product structure (visible-sector subsystems).* Spatially separated subsystems within the visible sector — e.g., two laboratories — correspond to subsets $V_A, V_B \subset V$ with disjoint coupling neighborhoods on the coupling graph. The spatial Markov property of range-1 dynamics (the area-law lemma; [SM §3.2]) guarantees conditional independence: $\rho_{AB} = \rho_A \otimes \rho_B$ conditioned on boundary data. The emergent Hilbert space inherits the factorization $\mathcal{H}_{V_A} \otimes \mathcal{H}_{V_B}$ from the locality of the coupling graph, with entanglement between $A$ and $B$ arising from shared boundary history — precisely the stochastic entanglement of [11, 24].

*(iii) State update, measurement, and multi-time predictions.* Projective measurement in the emergent description corresponds to conditioning on a visible-sector outcome and re-marginalizing over the hidden sector. The Lüders rule $\rho \to P_k \rho P_k / \text{Tr}(P_k \rho)$ is the quantum transcription of Bayesian updating on the classical substratum (Lemma 3). No independent measurement postulate is required. Multi-time correlation functions, weak values, and Leggett-Garg inequalities are standard calculations within the delivered formalism ($\mathcal{H}_V$, $U(t)$, Born rule); they require no additional postulates beyond what the characterization theorem provides.

*(iv) Classical non-Markovianity and quantum mechanics.* The equivalence is not a claim that all P-indivisible processes are "secretly quantum" in some metaphysical sense; it is a theorem that the mathematical structures are identical. Classical systems exhibiting P-indivisibility — renewal processes, semi-Markov processes on finite state spaces — admit a unique unitary description (phase-locking lemma) that makes predictions beyond the transition data (energy eigenvalues, interference, entanglement), and can be realized as marginalization of deterministic dynamics under C1–C3 (necessity theorems). The framework does not distinguish "classical non-Markovian" from "quantum" — it proves they are the same category. The physical content of the unitary is not that of a mere mathematical embedding: it is the *specific* Hamiltonian uniquely determined by the transition data, arising from the *actual* dilation structure of the system (§3.2).

---

## 4. DISCUSSION

### 4.1 Interpretive Consequences

The degrees of freedom involved in quantum experiments — photons, electrons, slits, detectors — are all visible-sector objects. Their quantum behavior is a downstream consequence of the trace-out: the emergent quantum mechanics, once established by the theorem, governs all visible-sector dynamics.

In the double-slit experiment, the particle traverses a single slit in the deterministic substratum. The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events. A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms. In Wigner's friend, the Friend has a definite outcome; Wigner's superposition reflects his epistemic deficit. The Everettian measure problem dissolves: the system evolves as a single reality; "branches" are features of the compressed description. The Born rule, often treated as an independent postulate, is derived: it is the equilibrium distribution of the indivisible stochastic process (§3.1), not an additional assumption.

### 4.2 Scope

The characterization theorem is a full equivalence: QM $\iff$ embedded observation under (C1)–(C3). The theorem does not identify which physical systems satisfy the conditions; this is an empirical question. Universality in our universe follows from the shared causal partition defined by null geodesics.

### 4.3 The Status of the Discreteness Scale

$\epsilon$ is a structural postulate of the framework, not a derived consequence. It does not smuggle in *quantum-mechanical* content specifically — the framework makes no use of $\hbar$, wavefunctions, or amplitudes at the level of Lemma 1 — but it does assert a UV cutoff that is stronger than classical field theory would provide. The cutoff is motivated by the empirical observability of finite outcomes and by holographic entropy bounds [2], and the framework takes it as the minimum structural content needed to formalise embedded observation on a world with finite-area boundaries.

### 4.4 Relation to Prior Work

**'t Hooft [1]:** Differs in mechanism (epistemic trace-out vs. information loss), generality (any embedded observer vs. particular rules), and Bell placement (outcome independence violation vs. superdeterminism). **QBism/relational QM:** Share observer-relative epistemic states; this framework provides a structural *why* and quantitative predictions.

Witten's Type II algebra program achieves finite entropy without finite-dimensional Hilbert spaces; this is compatible, since the framework's predictions depend on finite entropy (the physical content of Lemma 1), not on dimensional finiteness per se.

### 4.5 Assumptions, Limitations, and Falsifiability

**The theorem** requires Lemma 1, the stochastic-quantum bridge (§3.1 and §3.2; established by two independent routes), and genericity conditions (non-degenerate spectrum, non-vanishing overlaps), which hold for all but a measure-zero set. The P-indivisibility proof uses finiteness via the recurrence argument ($\varphi^N = \text{id}$). The accessible-timescale backflow lemma (§2.3) provides a parallel route to P-indivisibility, establishing observable information backflow on the timescales accessible to laboratory experiments — physically indistinguishable from a timeless identity for all experiments well below the recurrence time.

**Falsifiability.** The theorem would be falsified by a failure of both the stochastic-quantum correspondence and the Stinespring construction for the class of processes generated here — a possibility excluded by the independent proofs in §3.1 and §3.2.

**A near-term mechanism-side test.** A more tractable falsification target is provided by the recently developed operational distinction between classical and quantum memory in non-Markovian processes [28, 29]. Some non-Markovian quantum dynamics can be simulated using only classical stored information, while others require genuinely quantum memory in the environment, with the dividing line set by entanglement structure of the channel's Choi state. The framework predicts that all *fundamental* non-Markovian dynamics in nature — those arising from embedded observation rather than from engineered quantum baths — should be classical-memory simulable, because the hidden sector is by construction a classical substrate. A physically realized fundamental open-system process whose memory provably exceeds the classical bound would falsify the framework's foundational ontology. This is a near-term tractable test in a literature where the experimental and theoretical tools are advancing rapidly.

Laboratory tests of the characterization theorem may be possible in tabletop systems where the hidden sector capacity is tunable.

---

## 5. CONCLUSION

**The general theorem.** Under a single definition — observation is a proper subsystem of a deterministic whole — and conditions (C1)–(C3), the P-indivisibility of reduced dynamics is proved: any bijective dynamics on a finite system with non-trivial coupling necessarily produces P-indivisible stochastic dynamics. By the stochastic-quantum correspondence, the observer's description is necessarily quantum mechanics. Continuous-time transition data resolves all gauge freedom. The Schrödinger equation, Born rule, and Bell violations are structural consequences. The characterization theorem establishes that the conditions are necessary — (C1) and (C3) unconditionally, (C2) conditionally on ETH in the hidden sector — so that QM and embedded observation under (C1)–(C3) are equivalent within this scope.

---

## ACKNOWLEDGEMENTS

During the preparation of this work, the author used Claude Opus 4.6 (Anthropic) and Gemini 3.1 Pro (Google) to assist in drafting, refining argumentation, and verifying bibliographic details. The author reviewed and edited all content and takes full responsibility for the publication.

---

## REFERENCES


[1] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).


[2] N. Bao, S. M. Carroll, and A. Singh, "The Hilbert space of quantum gravity is locally finite-dimensional," *Int. J. Mod. Phys. D* **26**, 1743013 (2017).


[3] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002).


[4] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Entanglement and non-Markovianity of quantum evolutions," *Phys. Rev. Lett.* **105**, 050403 (2010).


[5] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014).


[6] P. Pechukas, "Reduced dynamics need not be completely positive," *Phys. Rev. Lett.* **73**, 1060 (1994).


[7] F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, and K. Modi, "Operational Markov condition for quantum processes," *Phys. Rev. Lett.* **120**, 040405 (2018).


[8] P. Strasberg and M. Esposito, "Stochastic thermodynamics in the strong coupling regime: An unambiguous approach based on coarse graining," *Phys. Rev. E* **95**, 062101 (2017).


[9] B. Bylicka, M. Johansson, and A. Acín, "Constructive method for detecting the information backflow of non-Markovian dynamics," *Phys. Rev. Lett.* **118**, 120501 (2017).


[10] S. Milz, M. S. Kim, F. A. Pollock, and K. Modi, "Completely positive divisibility does not mean Markovianity," *Phys. Rev. Lett.* **123**, 040401 (2019).


[11] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).


[12] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025).


[13] S. Calvo, "On the Stochastic-Quantum Correspondence," arXiv:2601.18720 (2026).


[14] L. S. Pimenta, "Divisible and indivisible Stochastic-Quantum dynamics," arXiv:2505.08785 (2025).


[15] W. F. Stinespring, "Positive functions on C*-algebras," *Proc. Amer. Math. Soc.* **6**, 211–216 (1955).


[16] M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000).


[17] K. Brandner, "Dynamics of microscale and nanoscale systems in the weak-memory regime," *Phys. Rev. Lett.* **134**, 037101 (2025).


[18] K. Brandner, "Dynamics of microscale and nanoscale systems in the weak-memory regime: A mathematical framework beyond the Markov approximation," *Phys. Rev. E* **111**, 014137 (2025).


[19] J. Mehl, B. Lander, C. Bechinger, V. Blickle, and U. Seifert, "Role of hidden slow degrees of freedom in the fluctuation theorem," *Phys. Rev. Lett.* **108**, 220601 (2012).


[20] S. Gröblacher, A. Trubarov, N. Prigge, G. D. Cole, M. Aspelmeyer, and J. Eisert, "Observation of non-Markovian micromechanical Brownian motion," *Nature Communications* **6**, 7606 (2015).


[21] S. W. P. Kim, C. von Keyserlingk, and A. Lamacraft, "Measurement-induced phase transitions in quantum inference problems and quantum hidden Markov models," arXiv:2504.08888 (2025).


[22] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095 (2026).


[23] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195–200 (1964).


[24] J. A. Barandes, M. Hasan, and D. Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality," arXiv:2512.18105 (2025).


[25] A. Fine, "Hidden Variables, Joint Probability, and the Bell Inequalities," *Phys. Rev. Lett.* **48**, 291 (1982).


[26] T. Le, F. A. Pollock, T. Paterek, M. Paternostro, and K. Modi, "Divisible quantum dynamics satisfies temporal Tsirelson's bound," *J. Phys. A* **50**, 055302 (2017).


[27] B. S. Cirel'son, "Quantum generalizations of Bell's inequality," *Lett. Math. Phys.* **4**, 93–100 (1980).


[28] C. Bäcker, K. Beyer, and W. T. Strunz, "Local disclosure of quantum memory in non-Markovian dynamics," *Phys. Rev. Lett.* **132**, 060402 (2024); arXiv:2310.01205.


[29] A. Yosifov, A. Iyer, V. Vedral, and J. Sun, "On the emergence of quantum memory in non-Markovian dynamics," arXiv:2507.21907 (2025).
