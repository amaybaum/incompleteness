# THE INCOMPLETENESS OF OBSERVATION
### The Equivalence of Quantum Mechanics and Embedded Observation

**Author:** Alex Maybaum  
**Date:** April 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

---

## ABSTRACT

An observer embedded in a deterministic universe cannot access the complete state. We prove that any such observer — coupled to a slow, high-capacity hidden sector on a finite-dimensional configuration space — must describe the visible sector using P-indivisible stochastic dynamics, mathematically equivalent to unitary quantum mechanics. The converse also holds: any quantum system, realized as a deterministic dilation, requires non-trivial coupling, slow-bath memory, and sufficient hidden-sector capacity. The Schrödinger equation, Born rule, and Bell violations emerge as structural consequences requiring no independent quantum postulates.

---

## 1. INTRODUCTION

### 1.1 The Problem of Embedded Observation

An observer embedded in a deterministic universe cannot access the complete state: degrees of freedom beyond causal reach are permanently hidden, and the observer's description is obtained by marginalizing over the hidden sector. The question is what this reduction imposes on the form of the observer's physical laws.

Prior work (QBism, relational QM, 't Hooft's cellular automaton [1]) takes observer-dependence as an interpretive starting point or derives it from specific microphysical models. This framework differs by identifying *necessary and sufficient conditions* under which any embedded observer in any deterministic system necessarily sees quantum mechanics — and proving these are the *only* conditions under which QM arises from a deterministic embedding.

**Note on v1.10.0 (audit-revised edition).** This revision applies findings from the framework's internal derivation audit. The substantive changes in [Main]:

- **§3.3 and §3.4 cross-references.** Two invocations of "the area-law lemma" — for parameter independence in Bell scenarios (§3.3) and tensor factorization of visible-sector subsystems (§3.4 Remark (ii)) — now cite [SM, §3.1] explicitly and identify the specific intermediate result invoked (the spatial Markov property $V° \perp V^c \mid \partial V$). A footnote acknowledges the cross-document architecture (the lemma is proved in [SM] but the proof's level of generality applies to [Main]'s foundational level without requiring [SM]'s specific cubic-lattice substrate).

- **Lemma 1 (Finiteness) reclassification.** The "finite-area surface admits finitely many modes" intuition is now explicitly identified as physical motivation for the holographic entropy bound [2], with the formal finiteness conclusion attributed to [2] rather than presented as an independent argument.

- **Lemma 3 (Determinism and unique measure) clarification.** The discrete-substratum counting measure is distinguished from the observer-level emergent Liouville measure on continuum phase space. The continuum identification is the natural measure on the continuum description an observer constructs from the finite substratum, not a property of $(S, \varphi)$ itself.

- **§1.4 partition-relativity smooth-prior assumption** is now flagged as an explicit input to the embedded-observer's epistemic specification (rather than a parenthetical aside). The framework's intended applications all satisfy it.

- **§2.3 continuous-time P-indivisibility** explicitly distinguishes the in-principle Poincaré-recurrence-based result (auxiliary support, recurrence times astronomically long) from the observable-timescale information-backflow result (load-bearing, established by the accessible-timescale lemma).

- **§2.3 accessible-timescale backflow lemma** acknowledges semi-rigorous status: the structure (spectral-gap suppression of bath decoherence over fast visible-sector dynamics) is rigorous, but specific constants are not exhaustively bounded. The framework's stochastic-quantum equivalence draws its rigorous content from PI-3 + necessity arguments, not from PI-4's quantitative bound.

- **§3.1 phase-locking lemma** downgrades the partition-symmetry-breaking upgrade from a "structural argument" to "physical motivation"; the lemma's formal status rests on the measure-zero genericity argument, which is sufficient for the framework's purposes.

The 12 theorems and lemmas in [Main] are unchanged in content; the audit refines language and classification. No fatal gaps were identified across the framework-wide audit (16 sessions, 0 fatal gaps; see audit document collection).

### 1.2 The Starting Point

The framework begins with a single empirical fact that cannot be doubted: *observation occurs*. An observer records distinguishable outcomes of interactions with a system not wholly under the observer's control. This is the cogito of Descartes made precise — not as philosophy, but as a mathematical constraint.

We ask: what is the minimal mathematical structure consistent with this fact?

**Definition.** An *observation* is a triple $(S, \varphi, V)$: a total system $S$, a dynamics $\varphi: S \to S$, and an observer $V \subsetneq S$ — a proper subsystem with finitely many distinguishable internal states, coupled to the complement $H = S \setminus V$ through $\varphi$.

This definition formalizes three features implicit in the concept of observation: there is a whole ($S$), the observer is not the whole ($V \subsetneq S$), and the observer registers changes (coupling through $\varphi$). From this definition, three structural properties follow.

**Lemma 1** (Finiteness). *The observer has finitely many distinguishable internal states, so the visible configuration space $\mathcal{C}_V$ is finite, with a discreteness scale $\epsilon$ providing a finite minimal cell volume.* The finiteness conclusion is established by the holographic entropy bounds [2], which provide the rigorous Hilbert-space-dimension cutoff $\dim \mathcal{H}_V \leq e^{A/4}$ for a region with finite boundary area $A$. The intuition that "any observer bounded by a finite-area surface couples to only finitely many modes" is offered as physical motivation for this bound, not as an independent argument; the framework relies on [2] for the formal result.

**Lemma 2** (Causal partition). *The observer is a proper subsystem: $V \subsetneq S$. The complement $H = S \setminus V$ is the hidden sector.* This partition is not a modeling choice but the definition of embedded observation: an observer that could access all of $S$ would have nothing external to observe. The product decomposition

$$\Gamma = \Gamma_V \times \Gamma_H, \qquad H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

follows, with cross-partition correlations entering only through $H_{\text{int}}$. The product decomposition is idealized; §4.5 addresses approximation quality.

**Lemma 3** (Determinism and unique measure). *$\varphi$ is a bijection: distinct states have distinct successors (determinism) and distinct predecessors (reversibility). The counting measure on $S$ is the unique $\varphi$-invariant measure.* Determinism (injectivity) is the requirement that the dynamics preserves the observer's records — non-injective evolution would merge distinct total states, erasing the distinction between outcomes the observer has already recorded. On a finite set, injectivity implies surjectivity, so $\varphi$ is a bijection. Uniqueness of the counting measure (up to normalization) is immediate on a finite set: $\varphi$-invariance forces uniformity within each cycle, and the union of cycles is all of $S$.

The Liouville measure on continuum phase space $\Gamma$ is *not* claimed as a substratum-level invariant measure — the framework's substratum-level commitment is to the discrete counting measure on the finite set $S$ (consistent with the §3.1 "Continuous spectra and the finite-substratum commitment" subsection of [SM]). Liouville on $\Gamma$ is the *observer-level emergent measure* obtained after the trace-out and the continuum identification described in §3 below; it is the natural measure on the continuum description an observer constructs from the finite substratum dynamics, not a property of $(S, \varphi)$ itself. The relation is:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\} \equiv \mathcal{L}\rho$$

These properties contain no quantum postulates. The claim is that quantum mechanics *emerges* under the conditions below.

### 1.3 Conditions on the Hidden Sector

**(C1) Non-zero coupling.** $H_{\text{int}} \neq 0$. The coupling is bidirectional.

**(C2) Slow-bath timescale separation.** The visible-sector (system) timescale $\tau_S$ is much shorter than the hidden-sector (bath) timescale $\tau_B$: $\tau_S \ll \tau_B$ — the *inverse* of the Markovian regime. The hidden sector evolves on timescales far exceeding those accessible to the observer.

**(C3) Sufficient capacity.** The number of hidden-sector degrees of freedom $N_H$ exceeds the number of visible-sector degrees of freedom $N_V$ by enough that visible-sector interactions do not appreciably perturb the hidden sector's state on timescales $\ll \tau_B$.

**Theorem statement.** Under Lemmas 1–3 and (C1)–(C3), the embedded observer's reduced description is mathematically equivalent to unitarily evolving quantum mechanics (defined precisely in §3.4). The conditions are not merely sufficient but *necessary* (§3.4), establishing full equivalence.

### 1.4 Partition-Relativity

**Lemma.** *The emergent description is uniquely determined by the partition. Any parameters of the emergent theory depend only on the geometric and thermodynamic properties of the partition boundary.*

*Proof.* By Lemma 3, the Hamiltonian flow $\phi_t$ is unique. By Lemma 2, the partition is fixed. The observer uses the Liouville measure $\mu$ — the unique absolutely continuous invariant measure on the full phase space, in the observer-level continuum description that emerges from the discrete substratum (Lemma 3 above). An embedded observer with incomplete knowledge of the total energy averages over energies with a smooth prior, recovering Liouville on a phase-space band; singular invariant measures are excluded by Lemma 3. The smooth-prior choice is part of the embedded-observer's epistemic specification, not a derived theorem: it states that the observer cannot sharply localize the universe's total energy at a single eigenvalue, which is the natural epistemic condition for any finite-resolution observer. The framework's intended applications (laboratory observers, cosmological observers) all satisfy this condition; it is flagged as an explicit input to the partition-relativity argument rather than a parenthetical aside. Letting $\pi_V$ denote projection onto the visible sector, the marginalized transition probabilities

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

**Genericity.** The theorem's precondition — that $T$ is not a permutation matrix — is equivalent to (C1) at the bijection level and is generic among bijections on $\mathcal{C}_V \times \mathcal{C}_H$ in a quantifiable sense. A bijection $\varphi$ on $\mathcal{C}_V \times \mathcal{C}_H$ produces $T$ equal to a permutation matrix if and only if $\varphi$ has the form $\varphi(x_i, h) = (\varphi_V(x_i), \sigma_{x_i}(h))$ — the V-dynamics is independent of $h$. Counting these: $|\mathcal{C}_V|!$ choices for $\varphi_V$ times $(|\mathcal{C}_H|!)^{|\mathcal{C}_V|}$ choices for the family $\{\sigma_{x_i}\}$, giving a total of $|\mathcal{C}_V|!\,(|\mathcal{C}_H|!)^{|\mathcal{C}_V|}$ bijections with $T$ a permutation, out of $(|\mathcal{C}_V|\,|\mathcal{C}_H|)!$ total. The fraction failing the precondition is therefore

$$P_{\text{perm}}(n_V, n_H) = \frac{n_V!\,(n_H!)^{n_V}}{(n_V n_H)!}, \quad n_V := |\mathcal{C}_V|,\ n_H := |\mathcal{C}_H|.$$

Stirling's approximation gives the asymptotic decay $\log P_{\text{perm}} \sim -n_V n_H \log n_V$ as $n_H \to \infty$ with $n_V$ fixed — equivalently, $P_{\text{perm}} \sim n_V^{-n_V n_H}$. For any $n_V \geq 2$, the fraction of bijections failing C1 at the $T$-level decays exponentially in the hidden-sector capacity $n_H$. At modest physical scales — say $n_V = 10$, $n_H = 100$ — the fraction is $\sim 10^{-981}$; at the scales C3 invokes, it is astronomically smaller. The theorem is therefore non-vacuous on two independent grounds: the precondition excludes a structurally distinguished class of decoupled bijections (those whose V-dynamics have no $h$-dependence), and that class is a vanishing fraction of the configuration space as C3 is engaged. C3 (high-capacity hidden sector) and C1 (non-trivial coupling) are independent conditions in statement, but C3 is the *engine* of C1's genericity: enlarging $n_H$ shrinks the measure of C1-violating bijections super-exponentially fast.

**Relation to prior work.** The P-indivisibility phenomenon is well-documented in the open-systems literature: reduced dynamics need not preserve positivity [6]; divisibility failure is equivalent to information backflow [4, 5]; process-tensor Markovianity provides an alternative characterization [7]; non-Markovian reduced dynamics arise in the slow-bath regime [8]. The Bylicka-Johansson-Acín equivalence between CP-divisibility and distinguishability monotonicity [9] narrows the gap between divisibility and non-Markovianity, but only for *invertible* reduced dynamics; the marginal $T(t)$ here is generally non-invertible, so the load-bearing property for the general argument remains P-indivisibility of the marginal process. Milz et al. [10] confirm CP-divisibility does not imply Markovianity in the process-tensor sense.

**Continuous-time extension.** The Hamiltonian flow on finite-dimensional phase space preserves Liouville measure on compact energy surfaces. $T_{ij}(t)$ is continuous with $T(0) = I$. By (C1), $T(t)$ departs from the permutation class for $t > 0$. By Poincaré recurrence, $\exists t_R$: the set of hidden states with $\pi_V(\varphi_{t_R}(x_i, h)) = x_i$ has measure $> 1 - \delta$ for any $\delta > 0$. For small $\delta$, this gives non-monotonic trace distance, establishing P-indivisibility in continuous time *in principle* — the recurrence times $t_R$ are typically astronomically long, so this argument is auxiliary support rather than the load-bearing result. The accessible-timescale lemma (PI-4) below establishes that under (C2), information backflow occurs on observable timescales, which is what the framework actually needs.

The recurrence argument establishes P-indivisibility in principle. The following lemma shows that under (C2), information backflow occurs on observable timescales — not merely at Poincaré recurrence times.

**Lemma (Accessible-timescale backflow).** *Under (C1)–(C3) with $\tau_S \ll \tau_B$, the non-Markovian mutual information $I(X_{<t}; X_{>t} \mid X_t)$ is $\mathcal{O}(1)$ for observation windows $t \sim k\tau_S$ with $k\tau_S \ll \tau_B$.*

*Proof.* The coupling $H_{\text{int}}$ transfers visible-sector information to the hidden sector at each interaction, at rate $\sim 1/\tau_S$. Between interactions, the hidden sector evolves under $H_H$ with spectral gap $\Delta \sim 1/\tau_B$. The decay of correlations stored in the hidden sector is governed by $e^{-\Delta \tau_S}$. When $\tau_S \ll \tau_B$, $\Delta \tau_S \ll 1$, so the decay per visible-sector transition is $1 - e^{-\Delta \tau_S} \approx \Delta \tau_S \ll 1$: correlations survive each step essentially intact. After $k$ transitions spanning a time $k\tau_S \ll \tau_B$, the cumulative decay is $e^{-k\Delta\tau_S} \approx 1 - k\Delta\tau_S$, which remains close to unity. The hidden sector therefore retains $\sim k$ bits of visible-sector history over this window, and the $(k+1)$-th transition reads back stored correlations through $H_{\text{int}}$, producing history-dependent transition probabilities — i.e., information backflow. More precisely, the mutual information satisfies:

$$I(X_{<t}; X_{>t} \mid X_t) \geq I_0(1 - k\Delta\tau_S) = I_0\left(1 - \frac{k\tau_S}{\tau_B}\right)$$

where $I_0 > 0$ is the single-step information transfer from (C1). For $k\tau_S \ll \tau_B$, this remains $\mathcal{O}(I_0)$ — comparable to the single-step coupling strength, not exponentially suppressed. The bound saturates (C3): the maximum storable history is $\log_2 m$ bits (§3.4), so persistent backflow over $K$ transitions requires $m \geq 2^K$, which is amply satisfied when $N_H \gg N_V$. $\square$

**Status of the bound.** The lemma's structure is rigorous (spectral-gap suppression of bath decoherence over fast visible-sector dynamics is the standard mechanism for non-Markovian information persistence in open quantum systems), but specific constants are not exhaustively bounded. The single-step information transfer $I_0$ is proportional to the coupling strength of $H_{\text{int}}$ but not given a tight quantitative form. The "$\approx \Delta \tau_S$" approximation is leading-order in $\tau_S/\tau_B$; subleading corrections are not bounded. The accessible-timescale lemma should accordingly be read as a semi-rigorous estimate of how (C2) and (C3) translate into observable information backflow, with the rigorous content of the framework's stochastic-quantum equivalence (§3.4 Necessity theorems) coming from PI-3 (Poincaré-recurrence-based P-indivisibility) plus the necessity arguments — both of which are independent theorem-grade results not relying on PI-4's quantitative bound. The empirical content of the framework's claim (information backflow on observable laboratory timescales for systems with $\tau_S \ll \tau_B$) is robust under any reasonable refinement of the constants.

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

**Continuous spectra and the finite-substratum commitment.** Lemma 1 fixes the visible configuration space as finite, and the Barandes correspondence as applied here produces an emergent Hilbert space of finite dimension. Standard quantum mechanics makes heavy use of continuous-spectrum observables — position on $\mathbb{R}^3$, momentum, continuous-spectrum scattering — which strictly require infinite-dimensional Hilbert spaces and unbounded self-adjoint operators. The framework's position on this is that continuous spectra are the infrared limit of the discrete spectrum produced by Lemma 1, not a deeper reality that the framework fails to capture. The quantitative separation is extreme: for a visible sector bounded by the cosmological horizon with discreteness scale $\epsilon = 2 l_p$, the number of distinguishable positions is $|\mathcal{C}_V| \sim (L_H/\epsilon)^3 \sim 10^{183}$, and the holographic bound on emergent Hilbert-space dimension is $e^{S_{\text{dS}}} = e^{10^{122}}$. The discretization error separating this finite-dimensional structure from a continuum approximation is $\lesssim 1/\sqrt{\dim \mathcal{H}} \sim e^{-10^{121}}$ per eigenvalue — operationally zero at any accessible resolution. Deviations from continuum QM at scale $E$ are suppressed by $(E/M_{\text{Pl}})^2$, the same scaling that controls Lorentz-invariance violation and trans-Planckian corrections; no independent continuous-spectrum prediction is needed or claimed. Calvo [13] extends the Barandes correspondence to countable-infinite dimensions for completeness, but the finite-dim correspondence is the load-bearing one for the framework — every result in §2–§3 runs on Lemma 1 directly.

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

Conditions (G1)–(G3) fail only on a measure-zero set of Hamiltonians; this measure-zero genericity argument is sufficient for the framework's purposes, and the phase-locking lemma's result depends only on it. A *physical motivation* for why generic Hamiltonians arising from the framework's intended applications satisfy (G1)–(G3) — beyond the abstract measure-zero genericity — proceeds as follows: the conditions concern the *effective* visible-sector Hamiltonian $\hat{H}_{\text{eff}}$ emerging after the trace-out, not the total Hamiltonian $H_{\text{tot}}$, and the trace-out tends to break symmetries of $H_{\text{tot}}$ because the partition boundary does not respect them. A partition centered on a specific observer breaks translational invariance, rotational symmetry about distant points, and boost invariance; any degeneracy in $H_{\text{tot}}$ that relies on correlations between visible and hidden sectors — which includes all degeneracies associated with symmetries the partition breaks — is lifted in $\hat{H}_{\text{eff}}$. The residual degeneracies of $\hat{H}_{\text{eff}}$ are those associated with symmetries acting entirely within the visible sector that commute with the trace-out: precisely the gauge symmetries of the emergent description, which correspond to physically equivalent states and do not affect the phase-locking argument (which operates on gauge-inequivalent transition data). This argument is offered as physical motivation for why specific applications of the lemma have $\hat{H}_{\text{eff}}$ satisfying (G1)–(G3) by mechanism rather than by genericity, but it is not formalized here as a structural theorem — the formal status of phase-locking rests on the measure-zero genericity argument.

### 3.2 Independent Derivation via Stinespring Dilation

An independent derivation of the emergent quantum description uses only Stinespring's dilation theorem [15] and standard properties of the partial trace [16], without invoking the stochastic-quantum correspondence of §3.1. The two routes are logically independent; either alone suffices.

**Setup.** The finite configuration spaces $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ and $\mathcal{C}_H = \{h_1, \ldots, h_m\}$ (Lemma 1) embed into Hilbert spaces $\mathcal{H}_V = \mathbb{C}^n$ and $\mathcal{H}_H = \mathbb{C}^m$ via $|i\rangle \leftrightarrow x_i$ and $|k\rangle \leftrightarrow h_k$. This introduces no quantum postulates: it is the canonical identification of probability distributions on a finite set with diagonal density matrices.

**Lemma (permutation unitarity).** *Any bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ defines a unitary $U_\varphi$ on $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$.*

*Proof.* Define $U_\varphi |i, k\rangle = |\varphi(x_i, h_k)\rangle$. Since $\varphi$ is a bijection, $U_\varphi$ permutes the orthonormal basis, hence is unitary. $\square$

For continuous-time dynamics $\varphi_t$, Stone's theorem on $\mathcal{H}$ yields $U_t = e^{-i\hat{H}t}$ for Hermitian $\hat{H}$.

**Lemma (Reverse direction).** *Any stochastic process on a finite configuration space $\mathcal{C}_V$ can be realised as the marginal of a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$ with uniform prior on $\mathcal{C}_H$, for some finite $\mathcal{C}_H$ (exactly when transition probabilities are rational; to arbitrary precision otherwise).*

*Proof.* Any marginal of a bijection with uniform prior is a doubly stochastic matrix, and by Birkhoff–von Neumann is a convex combination of permutation matrices. A bijection on $\mathcal{C}_V \times \mathcal{C}_H$ realising the required mixture is obtained by letting $\mathcal{C}_H$ enumerate the permutations; for multi-step processes, the construction extends by history dilation. $\square$

*Remark.* This is the correspondence at the stochastic-process level: bijection ↔ stochastic matrix via marginalization, both directions. It is *not* a full CPTP-channel correspondence — channels that create coherences from diagonal inputs have no permutation-unitary realisation with uniform ancilla. For the characterization theorem (§3.4), which is stated in terms of transition probabilities, this is the appropriate scope.

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

**Parameter independence from spatial locality.** Let $V_A$ and $V_B$ be space-like separated visible-sector subsystems with disjoint coupling neighborhoods on $G_\varphi$. The spatial Markov property of range-1 dynamics — proved as the discrete case of the Area-law lemma in [SM, §3.1], with the relevant intermediate result being $V° \perp V^c \mid \partial V$ for any range-1 bijection on a bounded-degree graph[^M1] — makes $V_A$ and $V_B$ conditionally independent given boundary data. Alice's measurement setting $a$ determines which function she evaluates on $V_A$; it does not alter the transition probabilities for $V_B$, which depend only on $V_B$'s local coupling neighborhood. Hence $P(x_B \mid a, b) = P(x_B \mid b)$ — parameter independence holds structurally for all bounded-degree graph topologies with range-1 coupling, with no fine-tuning of the hidden-variable distribution. Combined with the outcome-independence violation from stochastic entanglement, this gives the precise Jarrett decomposition.

[^M1]: The spatial Markov property used here is the discrete-side conclusion of the Area-law lemma in [SM, §3.1]. Although [SM] is downstream of [Main] in the framework's logical structure, the lemma's proof requires only range-1 coupling on a bounded-degree graph — assumptions established in [Main, §1.2 Lemma 1] — and is therefore general enough to support the foundational result here. Restating the lemma in [Main] would duplicate content; citing [SM, §3.1] is sufficient given the proof's level of generality.

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

**Definition (unitarily evolving QM).** A stochastic process $\mathcal{S}$ on a finite configuration space $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ is *mathematically equivalent to unitarily evolving quantum mechanics* if there exists a Hilbert space $\mathcal{H}_V$ of dimension $\leq n^3$, a Hermitian operator $\hat{H}$ on $\mathcal{H}_V$, and a unitary family $U(t) = e^{-i\hat{H}t}$ such that $T_{ij}(t) = |U_{ij}(t)|^2$ for all $i, j, t$ — i.e., transition probabilities are exactly Born-rule probabilities. This definition captures the Hilbert space, unitary dynamics, and the Born rule. Additional quantum-mechanical structures — the tensor product decomposition for spatially separated visible-sector subsystems, state update, and the measurement formalism — are addressed in the remarks following the theorem.

**Characterization theorem.** *Let $\mathcal{S}$ be a stochastic process on a finite configuration space $\mathcal{C}_V$ with $|\mathcal{C}_V| \geq 2$, and consider dynamics on accessible timescales $t \ll t_R$ where $t_R$ is the Poincaré recurrence time of any realizing substrate. Assume the hidden sector of any candidate realization satisfies ETH [17, 18]. Then the following are equivalent:*

*(i) $\mathcal{S}$ is mathematically equivalent to unitarily evolving QM (in the sense of the preceding definition).*

*(ii) $\mathcal{S}$ is P-indivisible on accessible timescales — i.e., information backflow occurs at $t \ll t_R$, not merely at the formal Poincaré recurrence time.*

*(iii) $\mathcal{S}$ arises from marginalizing a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$ with (C1) non-trivial coupling, (C2) slow-bath memory ($\tau_S \ll \tau_B$), and (C3) sufficient capacity.*

*Proof.* (i) $\iff$ (ii): Barandes [11, 12], on accessible timescales by construction (the equivalence is formulated for the dynamics observers can resolve, not for behavior at recurrence times). (iii) $\implies$ (ii): §2.3, where the accessible-timescale lemma upgrades the bare recurrence-based P-indivisibility (which follows from C1 alone) to information backflow on observable timescales using C2 and C3. (ii) $\implies$ (iii): the necessity theorems above — C1 from the equivalence with non-permutation $T$, C2 from the dephasing argument (without C2, $T$ becomes Markovian on accessible timescales and information backflow disappears), C3 from the data-processing bound. $\square$

QM is not merely *compatible with* embedded observation — it is *equivalent to* it.

**Remark (scope of the equivalence).** The characterization theorem establishes the Hilbert space, unitary dynamics, and Born-rule transition probabilities. Four further structures of operational quantum mechanics merit comment.

*(i) Tensor product structure (visible–hidden).* The Stinespring route (§3.2) constructs $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$ and derives the CPTP channel $\Phi$ by partial trace. The visible–hidden tensor product is therefore given by the construction, not postulated.

*(ii) Tensor product structure (visible-sector subsystems).* Spatially separated subsystems within the visible sector — e.g., two laboratories — correspond to subsets $V_A, V_B \subset V$ with disjoint coupling neighborhoods on the coupling graph. The spatial Markov property of range-1 dynamics (proved in [SM, §3.1] as the discrete case of the Area-law lemma; see also footnote M1 in §3.3 for the cross-reference architecture) guarantees conditional independence: $\rho_{AB} = \rho_A \otimes \rho_B$ conditioned on boundary data. The emergent Hilbert space inherits the factorization $\mathcal{H}_{V_A} \otimes \mathcal{H}_{V_B}$ from the locality of the coupling graph, with entanglement between $A$ and $B$ arising from shared boundary history — precisely the stochastic entanglement of [11, 24].

*(iii) State update, measurement, and multi-time predictions.* Projective measurement in the emergent description corresponds to conditioning on a visible-sector outcome and re-marginalizing over the hidden sector. The Lüders rule $\rho \to P_k \rho P_k / \text{Tr}(P_k \rho)$ is the quantum transcription of Bayesian updating on the classical substratum (Lemma 3). No independent measurement postulate is required. Multi-time correlation functions, weak values, and Leggett-Garg inequalities are standard calculations within the delivered formalism ($\mathcal{H}_V$, $U(t)$, Born rule); they require no additional postulates beyond what the characterization theorem provides.

*(iv) Classical non-Markovianity and quantum mechanics.* The equivalence is not a claim that all P-indivisible processes are "secretly quantum" in some metaphysical sense; it is a theorem that the mathematical structures are identical. Classical systems exhibiting P-indivisibility — renewal processes, semi-Markov processes on finite state spaces — admit a unique unitary description (phase-locking lemma) that makes predictions beyond the transition data (energy eigenvalues, interference, entanglement), and can be realized as marginalization of deterministic dynamics under C1–C3 (necessity theorems). The framework does not distinguish "classical non-Markovian" from "quantum" — it proves they are the same category. The physical content of the unitary is not that of a mere mathematical embedding: it is the *specific* Hamiltonian uniquely determined by the transition data, arising from the *actual* dilation structure of the system (§3.2).

---

## 4. DISCUSSION

### 4.1 Interpretive Consequences

The degrees of freedom involved in quantum experiments — photons, electrons, slits, detectors — are all visible-sector objects. Their quantum behavior is a downstream consequence of the trace-out: the emergent quantum mechanics, once established by the theorem, governs all visible-sector dynamics.

In the double-slit experiment, the particle traverses a single slit in the deterministic substratum. The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events. A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms. The Everettian measure problem dissolves: the system evolves as a single reality; "branches" are features of the compressed description. The Born rule, often treated as an independent postulate, is derived: it is the equilibrium distribution of the indivisible stochastic process (§3.1), not an additional assumption.

**Observer covariance and nested observers.** The framework treats the observer partition $V \subsetneq S$ as a choice, not an absolute. Different partitions correspond to different observers; each partition satisfying the characterization conditions produces its own C1–C3-quantum description of the remaining degrees of freedom. This is not a multiplicity of incompatible physics — it is a covariance property of the framework under observer-partition choice, which resolves the standard nested-observer paradoxes.

Consider the Wigner's-friend setup: two disjoint partitions $V_W, V_F \subset S$ (Wigner and Friend) with $V_W \cup V_F \subsetneq S$, and shared external hidden sector $H = S \setminus (V_W \cup V_F)$. The framework assigns three descriptions, all derived from the same $\varphi$ by the same trace-out procedure:

- **Friend's description.** Trace over $S \setminus V_F = V_W \cup H$. Under C1–C3 applied to $(V_F, S \setminus V_F)$, Friend's reduced description is quantum-mechanical. Friend observes definite outcomes in her visible sector, including any system she measures.
- **Wigner's description.** Trace over $S \setminus V_W = V_F \cup H$. Friend is part of Wigner's hidden sector. Under C1–C3 applied to $(V_W, S \setminus V_W)$, Wigner's reduced description is also quantum-mechanical. Wigner does not see a definite Friend-outcome within his own description — Friend's state is traced out.
- **Joint description.** The marginal transition matrix $T_{WF}(\alpha, \beta \to \alpha', \beta') = |\{h \in H : \pi_{V_W \cup V_F}(\varphi(\alpha, \beta, h)) = (\alpha', \beta')\}|/|H|$ exists and is unique given $\varphi$. Its marginals reproduce Wigner's $T_W$ and Friend's $T_F$ respectively.

The three descriptions are simultaneous rather than competing. Friend's claim that she has a definite outcome, and Wigner's description of Friend as a traced-out subsystem, are statements in different reduced descriptions, not conflicting claims about the substratum state. At the substratum level, Friend, Wigner, and the system all have definite configurations; neither Friend nor Wigner has epistemic access to the complete state, and this epistemic limitation produces their respective quantum descriptions through the same mechanism in §2–§3. The apparent "paradox" dissolves into a covariance property: observer identity is partition-gauge, not absolute, and framework predictions are covariant under choice of observer partition. No-go theorems assuming a single universal quantum description (such as Frauchiger–Renner) do not apply, because the framework provides multiple simultaneous reduced descriptions, each internally consistent with respect to its own partition, with all derived from the same deterministic substratum.

### 4.2 Scope

The characterization theorem is a full equivalence: QM $\iff$ embedded observation under (C1)–(C3). The theorem does not identify which physical systems satisfy the conditions; this is an empirical question. Universality in our universe follows from the shared causal partition defined by null geodesics.

### 4.3 The Status of the Discreteness Scale

$\epsilon$ does not smuggle in a quantum assumption. Lemma 1 requires finite-dimensionality, motivated by the classical fact that finite-area boundaries admit finitely many modes. Holographic entropy bounds [2] provide independent, non-quantum motivation.

### 4.4 Relation to Prior Work

**'t Hooft [1]:** Differs in mechanism (epistemic trace-out vs. information loss), generality (any embedded observer vs. particular rules), and Bell placement (outcome independence violation vs. superdeterminism). **QBism/relational QM:** Share observer-relative epistemic states; this framework provides a structural *why* and quantitative predictions.

**Relation to prior stochastic-quantum programs.** Three earlier programs sought to derive quantum mechanics from classical-looking substrates. **Nelson's stochastic mechanics [32]** postulates a continuous Brownian-motion-like process on configuration space with drift determined by the imaginary part of the log wave function; the Schrödinger equation follows from the Fokker-Planck structure. Wallstrom [33] showed that Nelson's program cannot uniquely select the quantization condition $\oint p \cdot dq = nh$ — the stochastic process admits a broader class of solutions than standard QM, and the quantization must be reimposed by hand. The present framework is not subject to this critique because it does not derive QM from a continuous stochastic process on $\psi$ or on configuration space; it derives QM from the characterization theorem for embedded observers on a deterministic bijection, with stochasticity emerging from the trace-out over the hidden sector rather than being fundamental. **Adler's trace dynamics [34]** derives QM from statistical mechanics of matrix-valued dynamical variables with a trace-class Hamiltonian, with the canonical commutation relations emerging as expectation values over a specific equilibrium ensemble. The framework here requires neither matrix-valued variables nor an equilibrium-ensemble derivation; the substratum is a finite configuration space with a deterministic bijection, and the emergence mechanism is the Stinespring dilation applied to observer-marginalized transition probabilities. **Barandes's stochastic-quantum correspondence [11, 12]**, used as a technical tool in §3.1, is not a competitor but a building block: the correspondence maps P-indivisible stochastic processes on finite configuration spaces to unitary quantum evolutions on finite Hilbert spaces, and the present framework supplies the physical mechanism (embedded observation under C1–C3) that produces the P-indivisible processes Barandes then maps to quantum mechanics. The three earlier programs identified emergent QM as a legitimate research target; what the present framework adds is a full equivalence — necessary and sufficient conditions — and a constructive derivation chain that does not require independent quantization conditions or equilibrium ensembles.

Witten's Type II algebra program achieves finite entropy without finite-dimensional Hilbert spaces; this is compatible, since the framework's predictions depend on finite entropy (the physical content of Lemma 1), not on dimensional finiteness per se.

### 4.5 Assumptions, Limitations, and Falsifiability

**The theorem** requires Lemma 1, the stochastic-quantum bridge (§3.1 and §3.2; established by two independent routes), and genericity conditions (non-degenerate spectrum, non-vanishing overlaps), which hold for all but a measure-zero set. The P-indivisibility proof uses finiteness via the recurrence argument ($\varphi^N = \text{id}$). The accessible-timescale backflow lemma (§2.3) provides a parallel route to P-indivisibility, establishing observable information backflow on the timescales accessible to laboratory experiments — physically indistinguishable from a timeless identity for all experiments well below the recurrence time.

**Falsifiability.** The framework makes a specific, experimentally testable structural claim: *the hidden sector is a classical substratum* — a finite set with a deterministic bijection. Every fundamental non-Markovian open-system process in nature — dynamics arising from embedded observation, not from engineered quantum environments — must therefore be classical-memory simulable in the operational sense of Bäcker, Beyer, and Strunz [28]: the environment's memory can be captured by a classical variable, and the non-Markovian dynamics reconstructed by conditioning on that variable. A physically realized fundamental open-system process whose memory provably exceeds the classical bound — demonstrated via the entanglement-structure protocols of [28, 29] — would falsify the framework's foundational ontology. This is a current-technology test whose experimental tools are under active development; a recent unified review [30] surveys the rapidly evolving classical-vs-quantum memory distinction in open-system dynamics. The claim is sharpest in the *C2-marginal regime* ($\tau_S \sim \tau_B$ rather than $\tau_S \ll \tau_B$), where non-Markovianity is $\mathcal{O}(1)$ rather than suppressed. Candidate physical realizations — strongly-driven superconducting qubits with two-level-system baths, biological electron transport with vibrational coupling, spin-boson dynamics at strong coupling — are the systems where the classical-memory simulability commitment is most stringently tested, and where emerging experimental and theoretical tools [28, 29, 30] are converging on the classical-vs-quantum memory distinction.

*Theorem-level falsifiability.* The characterization theorem itself would be falsified by a failure of both the stochastic-quantum correspondence and the Stinespring construction for the class of processes generated here — a possibility excluded by the independent proofs in §3.1 and §3.2. The classical-memory test above is the primary empirical falsifiability route, because the theorem is mathematical while the structural ontology commitment is physical.

Laboratory tests of the characterization theorem may be possible in tabletop systems where the hidden sector capacity is tunable.

### 4.6 Structural Exclusion of Equilibrium-Phase Observers

An immediate corollary of (C1)–(C3) is a structural selection rule on where in a finite bijective $(S, \varphi)$ observers can exist. The rule replaces a postulate often imported from elsewhere — the "past hypothesis" of low initial entropy — with a theorem derived from the framework's own definitions.

**Setup.** Let $V$ be a partition with hidden sector $B = S \setminus V$. Define the coupling-graph neighborhood $\Sigma_{\text{loc}}(V)$ as the subset of $S$ reached from $V$ by at most $\tau_S / \Delta t$ steps of $\varphi$, where $\Delta t$ is the update step. Let $\tau_{\text{mix}}(\Sigma)$ denote the mixing time of $\varphi$ restricted to any $\varphi$-invariant subsystem $\Sigma$, set by the spectral gap of the transfer operator on $\Sigma$.

**Theorem (structural observer selection).** For any partition $V$ of bounded coupling-graph diameter,
$$
\tau_B(V) \leq \tau_{\text{mix}}(\Sigma_{\text{loc}}(V)) + O(\varepsilon),
$$
where $\varepsilon$ absorbs typical-set and finite-size corrections. In particular, if $\Sigma_{\text{loc}}(V)$ is in its local equilibrium macrostate in the sense of canonical typicality [31], $\tau_B(V)$ is bounded by the local thermal decorrelation time.

*Proof.* Correlations between a $V$-localized observable $f$ and a $B$-localized observable $g$ at time $t$ require information to propagate from $V$ to $B$ at time $0$ and back to influence the $V$-correlated component of $g$ at time $t$. By the bounded coupling degree of $\varphi$, this round trip stays within $\Sigma_{\text{loc}}(V)$ for $t \leq \tau_S$. The spectral gap of $\varphi|_{\Sigma_{\text{loc}}}$ — which on an equilibrium microstate of $\mu|_{\Sigma_{\text{loc}}}$ sets the local thermal decorrelation rate — bounds the decay of such correlations exponentially at rate $1/\tau_{\text{mix}}$. Hence $\tau_B(V) \leq \tau_{\text{mix}}(\Sigma_{\text{loc}}) + O(\varepsilon)$. $\square$

**Corollary (anti-Boltzmann-brain).** A Boltzmann brain is by construction a local fluctuation within a neighborhood $\Sigma_{\text{loc}}$ that is itself in local thermal equilibrium — that is what "fluctuation from equilibrium" means. Applying the theorem: $\tau_B(V_{\text{BB}})$ is bounded by the local thermal decorrelation time $\sim \hbar/(k_B T_{\text{local}})$, which is at most $\sim 10^{-12}$ s for any temperature warm enough to support structured matter. Any finite-information observer has $\tau_S$ bounded below by its own internal processing time — for biological or synthetic BBs of any currently-envisioned type, $\tau_S \gtrsim 10^{-6}$ s. Condition (C2), $\tau_S \ll \tau_B$, therefore fails by at least six orders of magnitude for any BB. Since QM emergence under the framework requires (C2) as a necessary condition (§3.4), Boltzmann-brain observers do not see emergent QM; they are not observers in the sense the framework's definitions require. The exclusion is structural, not measure-theoretic — it follows from the incompatibility of (C2) with local equilibrium, not from arguments about the ratio of BBs to "ordinary" observers in an anthropic sample.

**Corollary (past-hypothesis replacement).** For $(S, \varphi)$ in its typical orbit phase — equivalently, in its equilibrium macrostate — canonical typicality [31] implies every local subsystem is also in its local equilibrium. By the theorem, $\tau_B(V)$ is bounded by the local $\tau_{\text{mix}}$ for every bounded-diameter partition $V$. No partition supports (C2). The framework's observers therefore exist only in the non-equilibrium phase of $(S, \varphi)$. The low-entropy initial condition commonly imported as a "past hypothesis" to select observer-compatible configurations is replaced here by a structural selection rule: observers exist where (C1)–(C3) are satisfiable, and (C1)–(C3) are not satisfiable in the equilibrium phase.

**Scope.** The theorem uses only bounded coupling, finiteness of $S$, and the canonical-typicality result [31]; no new axioms are introduced. Three scope notes. (i) *Locality of $V$.* The theorem assumes $V$ has bounded coupling-graph diameter. Adversarially non-local partitions — cherry-picking distant subsystems that happen to be correlated — are excluded by the bounded coupling degree of $\varphi$ and the finite response time of any physical observer. (ii) *Ergodicity.* The argument assumes the spectral gap on typical orbits of $\varphi$, which follows from statistical isotropy and bounded-coupling regularity; pathological non-ergodic $\varphi$ (many short orbits) is excluded by the structural assumptions already in force. (iii) *The cosmological realization.* The de Sitter horizon is thermal in the static-patch sense at Hawking temperature, but the globally expanding system is not in equilibrium with respect to any static-observer partition. The horizon's expansion sets $\tau_B \sim H^{-1}$ structurally, not thermally, which is the OI-native mechanism making human-timescale laboratory observation compatible with (C2).

---

## 5. CONCLUSION

**The general theorem.** Under a single definition — observation is a proper subsystem of a deterministic whole — and conditions (C1)–(C3), the P-indivisibility of reduced dynamics is proved: any bijective dynamics on a finite system with non-trivial coupling necessarily produces P-indivisible stochastic dynamics. By the stochastic-quantum correspondence, the observer's description is necessarily quantum mechanics. Continuous-time transition data resolves all gauge freedom. The Schrödinger equation, Born rule, and Bell violations are structural consequences. The characterization theorem establishes that the conditions are necessary: QM and embedded observation under (C1)–(C3) are equivalent.

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

[30] R. Gangwar and U. Sen, "Genuine and Non-Genuine Quantum Non-Markovianity: A Unified Information-Theoretic Review," arXiv:2603.28277 (2026).

[31] S. Goldstein, J. L. Lebowitz, R. Tumulka, and N. Zanghì, "Canonical Typicality," *Phys. Rev. Lett.* **96**, 050403 (2006); arXiv:cond-mat/0511091.

[32] E. Nelson, "Derivation of the Schrödinger equation from Newtonian mechanics," *Phys. Rev.* **150**, 1079 (1966); *Quantum Fluctuations* (Princeton University Press, 1985).

[33] T. C. Wallstrom, "Inequivalence between the Schrödinger equation and the Madelung hydrodynamic equations," *Phys. Rev. A* **49**, 1613 (1994).

[34] S. L. Adler, *Quantum Theory as an Emergent Phenomenon* (Cambridge University Press, 2004).
