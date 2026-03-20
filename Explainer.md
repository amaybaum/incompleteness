# The Incompleteness of Observation
### Why Physics' Biggest Contradiction Might Not Be a Contradiction at All
### With Complete Mathematical Detail

**Alex Maybaum — March 2026**

---

## The Worst Prediction in Physics

Physics has two spectacularly successful theories. Quantum mechanics describes the behavior of atoms, particles, and light. General relativity describes gravity, space, and time. Each has been confirmed to extraordinary precision. They have never disagreed with any experiment.

They disagree with each other.

Ask quantum mechanics how much energy empty space contains and it gives you a staggering number: roughly $10^{113}$ joules per cubic meter. Ask general relativity the same question — read the answer off the expansion rate of the universe — and you get about $6 \times 10^{-10}$ joules per cubic meter. The ratio is $10^{122}$. For scale, the number of atoms in the observable universe is about $10^{80}$. This is not a close call.

For decades, the assumption has been that something is deeply broken — that one or both calculations contain an error, and that finding the mistake will point the way to a unified theory of everything.

This paper argues the opposite. Neither calculation is wrong. They disagree because they *must*. In fact, that massive $10^{122}$ discrepancy isn't a failure at all. It is the strongest piece of existing evidence we have that quantum mechanics is not the fundamental bedrock of reality, but an emergent description forced upon us by our limited vantage point.

The argument is built from a chain of mathematical proofs, each feeding into the next. This document explains what the paper claims, walks through the logic of every major proof, and shows how they connect.

---

## The Starting Point: Four Axioms and Three Conditions

Every mathematical proof starts from assumptions, and the paper is explicit about its four. None of them mention quantum mechanics. None of them mention general relativity. They are:

**Axiom 1: Deterministic dynamics.** The universe evolves according to definite rules. Given the complete state at one time, the state at any other time is uniquely determined. Mathematically, the state lives in a phase space Γ, and there's a Hamiltonian H_tot that governs how the state changes:

$$\frac{\partial \rho}{\partial t} = \{H_{\text{tot}}, \rho\}$$

The curly braces {,} are Poisson brackets — the classical mechanics version of "how things change." The function ρ represents a probability distribution, but that probability reflects the observer's ignorance, not any fundamental randomness. Think of it like a billiard table: if you knew the exact position and velocity of every ball, you could predict the future perfectly.

**Axiom 2: Finiteness.** The system has finitely many distinguishable states. There's a smallest meaningful size ε — you can't resolve anything smaller. This means the configuration space is finite, not continuous. This matters because finite systems have a property infinite systems don't — they must eventually return to their starting state (Poincaré recurrence). In Part I, ε is left unspecified. In Part II, self-consistency forces ε = 2 l_p (twice the Planck length).

**Axiom 3: Causal partition.** The total phase space splits into two pieces:

$$\Gamma = \Gamma_V \times \Gamma_H$$

Γ_V is the visible sector (what the observer can access). Γ_H is the hidden sector (what they cannot). The total Hamiltonian splits correspondingly:

$$H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$

H_V governs the visible sector alone. H_H governs the hidden sector alone. H_int couples them — it's how the two sectors talk to each other. Without H_int, the two sectors would evolve independently and the observer would never feel the hidden sector's influence.

**Axiom 4: Classical probability.** The observer uses standard Kolmogorov probability theory. No exotic probability theories, no negative probabilities, no quantum probability — just ordinary probability. This is the axiom that makes the result surprising: we're putting in classical probability and getting out quantum mechanics.

That's it. The claim is that quantum mechanics — the Schrödinger equation, the Born rule, superposition, entanglement, Bell inequality violations — follows from these four premises alone, given the right conditions on the hidden sector:

**C1: Non-zero coupling (H_int ≠ 0).** The visible and hidden sectors interact. Information flows between them. Without this, the observer's room is perfectly isolated — nothing interesting happens.

**C2: Slow bath (τ_S ≪ τ_B).** The hidden sector evolves much more slowly than the visible sector. τ_S is the timescale of visible-sector processes; τ_B is the timescale of hidden-sector processes. This is the *opposite* of the usual assumption in physics. Normally, people assume the environment is fast and chaotic (a "heat bath" that quickly forgets everything). Here, the environment is slow and has a long memory. This is what makes the dynamics non-Markovian.

**C3: Sufficient capacity (N_H ≫ N_V).** The hidden sector has many more degrees of freedom than the visible sector. There's enough "room" to store information about the visible sector's history without running out of space.

The axioms set the stage. The conditions determine what kind of show plays on it. The next section explains why the cosmological horizon satisfies all three.

---

## The Observer's Blind Spot

Light travels at a finite speed, and the universe has a finite age. Put those together and every observer has a horizon — a boundary beyond which no signal has had time to arrive. Everything beyond that boundary is ordinary physics: fields, particles, radiation. But it is structurally inaccessible. Not because our telescopes aren't good enough, but because the geometry of spacetime forbids it. No technology that obeys the speed of light can reach past it.

This means every observer in the universe is in the same epistemic situation: there are degrees of freedom — a vast number of them — that influence what you measure but that you can never track. When you write down the laws of physics for the things you *can* see, you're forced to average over everything you can't. You have to "trace out" the hidden sector.

Here's what that looks like concretely. The total system — visible plus hidden — is deterministic. If you knew the complete state, you could predict the future exactly. But you don't know the hidden part. You know the visible state is $x$, but there are many possible hidden states compatible with $x$, and each one sends $x$ to a different visible future. Hidden state $h_1$ might send the particle left; hidden state $h_2$ might send it right. Since you can't tell which hidden state you're in, the best you can do is assign probabilities: average over all the possible hidden states, weighted by how likely each one is. The result is a set of *transition probabilities* — the chance that visible state $x$ at time $t_1$ becomes visible state $y$ at time $t_2$. You've gone from a deterministic system you can't fully see to a probabilistic one you can. That's a stochastic process, and it's the only description available to any observer who can't access the hidden sector.

The standard expectation is that this should produce something boring — classical, memoryless noise. And it would, if the hidden sector were fast and forgettable, like air molecules bouncing off a grain of pollen. Each kick is independent of the last. Physicists call this *Markovian* behavior.

But the hidden sector beyond the cosmological horizon is not like that. It differs in three specific ways, and the paper proves that their conjunction changes everything.

**It's coupled.** The horizon is not a static wall. Stress-energy conservation enforces continuous dynamical correlations across it. Matter crosses the horizon, and the horizon area adjusts in response to interior energy density. Information flows in both directions. (Condition C1.)

**It's slow.** The hidden sector's correlation time is set by the Hubble timescale — roughly $10^{17}$ seconds, the age of the universe. Any laboratory experiment operates on timescales of $10^{-15}$ seconds or shorter. The ratio is $10^{-32}$. The hidden sector cannot "reset" between your measurements. Every correlation it picks up from one experiment is still there when the next one begins. This is the *opposite* of the standard Markovian regime, where the environment decorrelates fast. Here, it never decorrelates at all. (Condition C2.)

**It's vast.** The hidden sector has roughly $10^{122}$ independent degrees of freedom — the Bekenstein-Hawking entropy of the cosmological horizon. No experiment you could ever perform would appreciably disturb its state. Its memory never saturates. (Condition C3.)

A fast environment with vast capacity would wash out correlations (Markovian noise). A slow environment with limited capacity would eventually fill up and stop recording. Only an environment that is simultaneously coupled, slow, and vast sustains the kind of persistent, non-decomposable correlations that the paper calls *P-indivisibility* — a technical term meaning the system's transition probabilities at different times cannot be broken into independent steps.

---

## Partition-Relativity (§1.4)

This is the first real proof in the paper, and it's beautifully simple.

**What it proves:** The emergent description (what the observer sees) depends *only* on the partition — on which degrees of freedom are visible and which are hidden. Nothing else.

**The formula:**

$$T_{ij}(t_2, t_1) = \int_{\Gamma_H} \delta_{x_j}[\pi_V(\phi_{t_2-t_1}(x_i, h))] \, d\mu(h)$$

Unpacking each symbol:

- **T_ij**: The probability of transitioning from visible state x_i to visible state x_j in the time interval from t_1 to t_2. This is what the observer measures.
- **(x_i, h)**: The complete state — visible part x_i, hidden part h.
- **φ_{t2-t1}**: The deterministic evolution. Takes the complete state at time t_1 and returns the complete state at time t_2. Uniquely determined by Axiom 1.
- **π_V**: Projection onto the visible sector. Takes a complete state (x, h) and returns just x.
- **δ_{xj}[...]**: The Kronecker delta. Equals 1 if the visible part ended up at x_j, equals 0 otherwise.
- **dμ(h)**: Integration over all possible hidden states, weighted by the Liouville measure.

**In plain English:** For each possible hidden state h, check whether starting at (x_i, h) and evolving forward lands the visible part on x_j. Count up all the hidden states where this happens, weighted by how likely each hidden state is. The result is the probability of the transition x_i → x_j.

**The proof:** The formula has exactly three inputs: (1) the dynamics φ_t — fixed by Axiom 1, (2) the partition (Γ_V, Γ_H) and projection π_V — fixed by Axiom 3, and (3) the measure μ — fixed by Axiom 4 (Liouville measure is the unique choice). Since inputs 1 and 3 are determined by the axioms, the only free input is the partition. Therefore: everything about the emergent description depends only on the partition. QED.

**Why the Liouville measure is unique:** The observer needs a "prior" — a way to weight the hidden states. Liouville measure is the unique measure on phase space that is absolutely continuous (no point masses) and invariant under Hamiltonian flow. Any smooth initial distribution evolves toward it. Singular measures are excluded by Axiom 4's requirement of standard probability theory. The observer has no choice.

---

## Emergent Stochasticity and the Slow-Bath Regime (§§2.1–2.2)

The total system is deterministic. If you knew both x and h, you'd know the future with certainty. But the observer knows only x. Different hidden states h send the same visible state x to different futures.

Example: visible state is "Heads." Hidden state could be any die value 1–6. If the die is 1 or 2, the dynamics flip the coin to Tails. If the die is 3–6, the coin stays at Heads. The observer doesn't know the die, so they see: P(Heads → Tails) = 2/6 = 1/3. The randomness is epistemic (from ignorance) not ontological (from fundamental indeterminacy).

In a normal "heat bath" scenario, the environment is fast and chaotic. It scrambles any information you write into it before you can read it back. This produces Markovian (memoryless) dynamics — each step is independent of previous steps.

C2 inverts this. The hidden sector is slow. When the visible sector interacts with it (writing information through H_int), the information stays there. At the next interaction, the hidden sector reads back what was written before. The observer sees history-dependent transition probabilities — what happens next depends on what happened before.

This is non-Markovian dynamics. It's the key ingredient that separates quantum mechanics from classical stochastic processes.

---

## The P-Indivisibility Theorem (§2.3)

**What it claims.** If a deterministic system is split into a visible and hidden sector, and these sectors are genuinely coupled, then the visible sector's behavior *cannot* be a simple memoryless random process. It must exhibit P-indivisibility — a specific kind of built-in memory.

**What "P-indivisible" means.** A stochastic process is "P-divisible" if you can always find a valid transition matrix connecting any two time points. Mathematically: for any times t_1 < t_2 < t_3, there exists a stochastic matrix Λ such that:

$$T(t_3, t_1) = \Lambda(t_3, t_2) \cdot T(t_2, t_1)$$

where Λ has non-negative entries and rows summing to 1. "P-indivisible" means this fails — the "intermediate propagator" would need negative entries, which means it's not a valid probability matrix.

Breuer, Laine, and Piilo proved that P-indivisibility is equivalent to "information backflow" — the system's distinguishability can *increase* over time. In a classical Markov process, you can only lose information (mixing). In a P-indivisible process, information comes back. This is exactly what quantum systems do — interference, revivals, and non-classical correlations all involve information returning from where it was stored.

**The setup.** We work on finite sets (Axiom 2). The visible sector has states C_V = {x_1, x_2, ...} with |C_V| ≥ 2. The hidden sector has states C_H = {h_1, h_2, ...}. The total dynamics is a bijection φ on C_V × C_H. The transition matrix is:

$$T_{ij} = \frac{|\{h \in \mathcal{C}_H : \pi_V(\varphi(x_i, h)) = x_j\}|}{|\mathcal{C}_H|}$$

**The key tool — total variation distance:**

$$d(p, q) = \frac{1}{2}\sum_k |p_k - q_k|$$

This measures how distinguishable two probability distributions are. If d = 1, they're perfectly distinguishable. If d = 0, they're identical. For P-divisible processes, d can only decrease or stay constant.

**Step 1 — Recurrence.** φ is a bijection on a finite set. Keep applying φ and you must eventually return to where you started — there are only finitely many states to visit. Formally: there exists N such that φ^N = id. So T^(N) = I, and:

$$d(\delta_i T^{(N)}, \delta_j T^{(N)}) = d(\delta_i, \delta_j) = 1$$

After N steps, states that started distinguishable are still perfectly distinguishable.

**Step 2 — Strict contraction.** T is not a permutation matrix (this follows from C1 — the coupling mixes things). So there exist states i, j, l where both T_il > 0 and T_jl > 0. The total variation distance after one step:

$$d(\delta_i T, \delta_j T) = \frac{1}{2}\sum_k |T_{ik} - T_{jk}| < 1$$

The inequality is strict because the distributions overlap. Distinguishability has decreased.

**Step 3 — The punchline.** At t = 1: d < 1 (distinguishability decreased). At t = N: d = 1 (distinguishability restored). The distinguishability went down then came back up — non-monotonic behavior. A P-divisible process can only have non-increasing distinguishability. Therefore the process is P-indivisible. QED.

The proof uses almost nothing — just that the dynamics is a bijection on a finite set (Axioms 1 and 2) and that the coupling is non-trivial (C1). It is purely combinatorial.

---

## The Accessible-Timescale Lemma (§2.3 continued)

The recurrence proof shows P-indivisibility exists as a mathematical property. But the recurrence time is absurdly long — for the cosmological case, it's e^(10^122) years. Nobody will ever observe it.

The accessible-timescale lemma shows that information backflow happens on *laboratory timescales*, independently of recurrence.

**The mechanism:** At each interaction (timescale τ_S), the coupling H_int transfers some information from the visible sector to the hidden sector. Call the amount I_0. Between interactions, the hidden sector's correlations decay with a rate set by its spectral gap Δ ~ 1/τ_B.

The decay per visible-sector step is:

$$e^{-\Delta \tau_S} \approx 1 - \frac{\tau_S}{\tau_B}$$

When τ_S ≪ τ_B (C2), this is very close to 1 — almost no decay. The hidden sector remembers almost perfectly between steps. After k steps, the cumulative decay is:

$$e^{-k\Delta\tau_S} \approx 1 - \frac{k\tau_S}{\tau_B}$$

As long as k·τ_S ≪ τ_B, the hidden sector retains ~k bits of visible-sector history. The mutual information satisfies:

$$I(X_{<t}; X_{>t} \mid X_t) \geq I_0\left(1 - \frac{k\tau_S}{\tau_B}\right)$$

For the cosmological case: τ_S ~ 10^{-15} s, τ_B ~ 10^{17} s. Even after k = 10^{20} steps, k·τ_S/τ_B ~ 10^{-12} — negligible. The hidden sector remembers everything.

**The role of C3:** The hidden sector's memory capacity is log_2(|C_H|) bits. If k bits of history are written but the capacity is only m < k bits, old data gets overwritten. C3 ensures m is large enough that the memory never saturates on observable timescales.

---

## The Coin-and-Die Model (§2.4)

The paper builds a concrete toy model to make the mechanism tangible.

**Setup:**
- Visible: x ∈ {0, 1} (a coin: 0 = Heads, 1 = Tails)
- Hidden: h ∈ {1, 2, 3, 4, 5, 6} (a die)
- Total: 12 states

**The permutation σ:**

| Input state | Output state | What happens |
|---|---|---|
| (0, 1) | (1, 1) | Coin flips, die stays |
| (1, 1) | (0, 1) | Coin flips, die stays |
| (0, 2) | (1, 2) | Coin flips, die stays |
| (1, 2) | (0, 2) | Coin flips, die stays |
| (0, 3) | (0, 4) | Coin stays, die changes |
| (0, 4) | (0, 3) | Coin stays, die changes |
| (0, 5) | (0, 6) | Coin stays, die changes |
| (0, 6) | (0, 5) | Coin stays, die changes |
| (1, 3) | (1, 4) | Coin stays, die changes |
| (1, 4) | (1, 3) | Coin stays, die changes |
| (1, 5) | (1, 6) | Coin stays, die changes |
| (1, 6) | (1, 5) | Coin stays, die changes |

Every swap is a transposition (a ↔ b), so σ² = id (apply twice, everything returns).

**Checking the conditions:** C1 (coupling): die values 1 and 2 flip the coin ✓. C2 (slow bath): σ² = id means recurrence time is 2 steps, giving τ_S/τ_B = 1/2 ✓. C3 (sufficient capacity): 6 hidden states vs 2 visible states ✓.

**Computing T(1,0).** Start at x = 0 (Heads). All 6 die values are equally likely.

- h = 1: σ(0,1) = (1,1) → Tails
- h = 2: σ(0,2) = (1,2) → Tails
- h = 3: σ(0,3) = (0,4) → Heads
- h = 4: σ(0,4) = (0,3) → Heads
- h = 5: σ(0,5) = (0,6) → Heads
- h = 6: σ(0,6) = (0,5) → Heads

P(0 → 0) = 4/6 = 2/3, P(0 → 1) = 2/6 = 1/3. By the same logic for x = 1:

$$T(1,0) = \begin{pmatrix} 2/3 & 1/3 \\ 1/3 & 2/3 \end{pmatrix}$$

**Distinguishability at t = 1:**

$$d(\delta_0 T, \delta_1 T) = \frac{1}{2}(|2/3 - 1/3| + |1/3 - 2/3|) = 1/3$$

Started at d = 1. Now d = 1/3. Distinguishability decreased.

**What Markov would predict at t = 2:** Apply the same transition matrix again:

$$T(1,0)^2 = \begin{pmatrix} 5/9 & 4/9 \\ 4/9 & 5/9 \end{pmatrix}$$

Distinguishability would drop to d = 1/9. More mixing.

**What actually happens at t = 2:** σ² = id. Every state returns to its starting point.

$$T(2,0) = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

Distinguishability is back to d = 1. Complete un-mixing. Impossible for a Markov process.

**The smoking gun — negative entries.** If there were a valid stochastic matrix Λ(2,1) connecting steps 1 and 2:

$$\Lambda(2,1) = T(2,0) \cdot [T(1,0)]^{-1} = I \cdot \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

The entries −1 are negative. No valid stochastic matrix exists. **This is P-indivisibility.**

**The mechanism in detail.** The die works as a memory register. At step 1, if the coin was at 0 and the die was at 1, the coin flips to 1 but the die stays at 1. The die value 1 now encodes the information "the coin was at 0 and I flipped it." At step 2, σ sees (1, 1) and flips it back to (0, 1). The die read its own memory and reversed the flip. C1 (coupling) allows writing to the memory. C2 (slow bath) ensures it isn't erased between reads. C3 (sufficient capacity) ensures there's enough room. Together, they produce the information backflow that makes the process P-indivisible — and therefore, by the stochastic-quantum correspondence, equivalent to quantum mechanics.

---

### Why conditions C2 and C3 matter physically

The P-indivisibility theorem needs only coupling (C1) and finiteness. So why does the paper insist on slow memory (C2) and vast capacity (C3)?

Because P-indivisibility without C2 and C3 might only show up at absurd timescales or might self-destruct. C2 ensures the memory persists on timescales accessible to actual experiments, not just at cosmic recurrence times. C3 ensures the hidden sector never runs out of room to store information — if it saturates, later imprints overwrite earlier ones, and the process becomes effectively memoryless. Together, C2 and C3 guarantee that P-indivisibility is strong, persistent, and observationally relevant.

---

## The Stochastic-Quantum Correspondence (§3.1 and Appendix A)

This is the key link. Section 2 proved that the embedded observer's dynamics are P-indivisible. Section 3 shows this is mathematically equivalent to quantum mechanics.

**The core statement.** Any P-indivisible stochastic process on a finite configuration space of size n can be embedded into a unitarily evolving quantum system. Specifically, there exists a Hilbert space H (dimension ≤ n³) and a unitary operator U(t) such that:

$$T_{ij}(t) = |U_{ij}(t)|^2$$

This is the Born rule. The left side is the transition probability computed by averaging over hidden states (the classical formula from partition-relativity). The right side is the quantum mechanical probability — the squared modulus of a matrix element of the unitary evolution operator. The equivalence is not approximate. It is not an analogy. It is a mathematical identity.

**Two independent routes to the same conclusion.** The primary route uses Barandes' stochastic-quantum correspondence (2023–2025): P-indivisibility means transition probabilities can't be factored through intermediate times — try it and you get "negative probabilities." In quantum mechanics, this is *exactly what happens*: probability amplitudes combine to produce interference patterns that don't factorize classically. What Barandes proved is that these are the same mathematical object, written in different notation.

The secondary route, given in Appendix A, uses Stinespring's dilation theorem (1955): a deterministic bijection on a finite product space defines a permutation unitary; tracing out the hidden sector with the Liouville measure produces a completely positive quantum channel whose diagonal elements recover the classical transition probabilities exactly. This second route requires only textbook results. Either route alone suffices; together they ensure the bridge rests on no single recent result.

**Where the quantum features come from:**

- **The Schrödinger equation** arises because U(t) is differentiable. Any smooth family of unitary matrices can be written as U(t) = exp(-iHt/ℏ) for some Hermitian matrix H.

- **The Born rule** T_ij = |U_ij|² is not an additional postulate — it's the definition of how the stochastic process maps onto the unitary one.

- **The action scale ℏ** enters when converting from the dimensionless unitary to a dimensionful Hamiltonian: Ĥ = iℏ (∂U/∂t) U†. The value of ℏ cannot be determined from the dimensionless transition data alone — it requires additional physical input from the partition geometry (§5).

- **Bell inequality violations.** Since the transition matrices for composite systems don't factorize, entangled systems naturally produce correlations that violate Bell inequalities, up to exactly Tsirelson's bound.

---

## The Phase-Locking Lemma (§3.1 continued)

A potential objection: the relation T_ij = |U_ij|² throws away phase information. Different unitaries could give the same transition probabilities. Does this make the quantum description ambiguous?

The phase-locking lemma shows: no.

**Setup:** The transition probability at time t is:

$$T_{ij}(t) = \left|\sum_k V_{ik} \, e^{-iE_k t} \, V_{jk}^*\right|^2$$

where V_ik = ⟨i|k⟩ are the overlaps between the configuration basis and the energy eigenbasis, and E_k are the energy eigenvalues. Expanding the square:

$$T_{ij}(t) = \sum_{k,l} V_{ik}\, V_{jk}^*\, V_{jl}\, V_{il}^*\; e^{-i(E_k - E_l)t}$$

**The Fourier trick:** This is a sum of oscillating terms at frequencies ω_kl = E_k - E_l. If all these frequencies are distinct (condition G2: non-degenerate energy gaps), you can extract each coefficient by Fourier transform:

$$a_{ij}^{kl} = V_{ik}\, V_{jk}^*\, V_{jl}\, V_{il}^*$$

**Extracting the moduli:** Setting i = j: $a_{ii}^{kl} = |V_{ik}|^2 |V_{il}|^2$. If none of the overlaps are zero (condition G3), all moduli |V_ik| are determined.

**Extracting the phases:** Write V_ik = |V_ik| e^{iφ_ik}. The argument of the Fourier coefficient gives:

$$\arg(a_{ij}^{kl}) = (\varphi_{ik} - \varphi_{il}) - (\varphi_{jk} - \varphi_{jl})$$

The only transformation preserving all double differences is φ_ik → φ_ik + α_i + β_k — just relabeling (choosing a different phase convention for the basis states). Once you fix these conventions, all remaining phases are uniquely determined.

**Bottom line:** Continuous-time transition probability data uniquely determines the Hamiltonian up to physically irrelevant relabeling.

---

## Bell Inequality Violations (§3.2)

This is the question everyone asks: isn't this ruled out by Bell's theorem?

**What Bell's theorem actually requires.** Bell's theorem proves that no hidden variable theory can reproduce quantum correlations if it satisfies three conditions simultaneously:

1. **Locality:** The outcome at detector A doesn't depend on the setting at detector B
2. **Measurement independence:** The experimenters' choices are independent of the hidden variables
3. **Factorizability:** P(a,b | x,y,λ) = P(a|x,λ) · P(b|y,λ)

The framework satisfies conditions 1 and 2. It violates condition 3.

**Why factorizability fails.** Factorizability requires that, conditioned on the hidden variable λ, the outcomes at the two detectors are independent — that λ carries all the relevant information as a snapshot at a single moment.

P-indivisible processes don't work this way. The transition probabilities for a joint system can't be factored:

$$T_{QR} \neq T_Q \otimes T_R$$

Two subsystems that interacted during preparation carry a joint transition matrix that doesn't decompose into a product. This non-factorizability IS entanglement.

**The Jarrett decomposition.** Factorizability splits into parameter independence (outcome at A doesn't depend on setting at B — preserved ✓) and outcome independence (outcome at A doesn't depend on outcome at B — violated ✗). Parameter independence prevents faster-than-light signaling. Fine's theorem shows that violating outcome independence while preserving parameter independence is exactly the class of theories consistent with quantum correlations.

**The maximum violation.** Barandes, Hasan, and Kagan prove the maximum CHSH violation from P-indivisible processes is exactly Tsirelson's bound: 2√2 — the quantum maximum.

---

## The Characterization Theorem (§3.3)

It's not enough to show that embedded observation *produces* QM (sufficiency). The paper shows QM *requires* embedded observation under C1–C3 (necessity). The full logical chain:

- Barandes proved: QM ⟺ P-indivisibility
- Section 2.3 proved: C1–C3 ⟹ P-indivisibility (sufficiency)
- Section 3.3 proves: P-indivisibility ⟹ C1–C3 (necessity)
- Combined: **QM ⟺ P-indivisibility ⟺ embedded observation under C1–C3**

**Necessity of C1 (coupling).** If T is a permutation (no coupling), then T^k is also a permutation for all k. The intermediate propagator Λ(k₂,k₁) = T^{k₂-k₁} is always a valid stochastic matrix. So the process is P-divisible. Contrapositive: P-indivisibility requires non-trivial coupling.

**Necessity of C2 (slow bath).** Between coupling events (separated by τ_S), the hidden sector evolves under its own Hamiltonian. The convergence to equilibrium is:

$$\| e^{\mathcal{L}_H \tau_S} \mu_H(\cdot | x_i) - \mu_{\text{eq}} \|_{\text{TV}} \leq C \, e^{-\Delta \tau_S}$$

In the fast-bath regime (Δ·τ_S ≫ 1), this is exponentially small. The hidden sector forgets everything between interactions. Each transition is computed against the same equilibrium distribution, so T^(k) = T^k — a Markov chain, hence P-divisible. Contrapositive: P-indivisibility requires τ_S ≪ τ_B.

**Necessity of C3 (sufficient capacity).** The non-Markovian mutual information is bounded by the hidden sector's size:

$$I(X_{<t} ; X_{>t} \mid X_t) \leq \log_2 m$$

where m = |C_H|. Proof: the total system is deterministic, so X_{>t} is a function of (X_t, H_t). Given X_t, the chain X_{<t} → H_t → X_{>t} is Markov. By the data processing inequality:

$$I(X_{<t} ; X_{>t} \mid X_t) \leq I(X_{<t} ; H_t \mid X_t) \leq H(H_t \mid X_t) \leq H(H_t) \leq \log_2 m$$

Each step uses a standard information-theoretic inequality. The result: if you want K bits of history dependence, you need m ≥ 2^K hidden states.

**The complete characterization.** For |C_V| ≥ 2, the following are equivalent: (1) the process is mathematically equivalent to unitarily evolving QM, (2) the process is P-indivisible, (3) the process arises from marginalizing a deterministic bijection with C1, C2, C3. This is the biconditional: **QM ⟺ embedded observation under C1–C3.**

---

## The Cosmological Application (§4)

### 4.1 The Partition

The cosmological horizon is the boundary beyond which no signal traveling at or below c can ever reach the observer. In a universe with a positive cosmological constant (de Sitter space), this horizon exists for every observer and has a definite, finite area:

$$A = \frac{4\pi c^2}{H^2}$$

where H is the Hubble parameter. This implements Axiom 3 naturally: Γ_V = everything inside the horizon, Γ_H = everything beyond.

**Why ℏ is the same for all observers:** Different observers have slightly different horizons. But the gap equation ℏ = c³ε²/(4G) depends only on local geometric quantities (c, G, ε) — not on the horizon area or the observer's worldline. So all observers derive the same ℏ.

### 4.2 Verification of the Conditions

**C1 (coupling).** In general relativity's ADM formulation, the bulk Hamiltonian is a sum of constraints that vanish on-shell — meaning the "real" dynamics happens at the boundary. The Hamiltonian and momentum constraints correlate interior and exterior data. This is stronger than just H_int ≠ 0: the constraints enforce correlations that persist on all timescales.

**C2 (slow bath).** τ_B ~ 1/H ~ 10¹⁷ seconds (the Hubble time). τ_S ~ 10⁻¹⁵ seconds (a typical atomic process). The ratio: τ_S/τ_B ~ 10⁻³².

**C3 (sufficient capacity).** The hidden sector has A/ε² ~ 10¹²² modes (the de Sitter entropy). The visible sector has ~ 10⁸⁰ baryons. No experiment comes close to saturating the hidden sector.

### 4.3 Application

With the cosmological horizon satisfying all axioms and conditions, the characterization theorem applies. The observer's reduced description is P-indivisible and therefore equivalent to unitary quantum mechanics. The value of ℏ is determined by the partition geometry — which is what Section 5 derives.

---

## Where Planck's Constant Comes From (§5)

Partition-relativity proved that the emergent quantum description is completely and uniquely determined by the partition. This means $\hbar$ cannot be a free parameter — it must be fixed by the geometry of the boundary.

### The Classical Horizon Temperature (§5.1)

**Starting point: Jacobson's identity.** Jacobson (1995) showed that Einstein's field equations follow from applying the first law of thermodynamics δQ = TdS to local causal horizons:

$$dE = \frac{c^2 \kappa}{8\pi G} \, dA$$

where κ is the surface gravity and dA is the change in horizon area. This is a classical gravitational identity — no quantum mechanics involved.

The entropy density is η = 1/ε² (one degree of freedom per minimal cell of area ε²). So dS = dA/ε². From dE = TdS:

$$k_B T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G}$$

For the de Sitter horizon, κ = cH:

$$k_B T_{\text{cl}} = \frac{c^3 \epsilon^2 H}{8\pi G}$$

**Critical point: no ℏ appears anywhere.** This temperature is computed from purely classical quantities.

### The Four-Step Derivation (§5.2)

**Step 1 (Uniqueness).** Partition-relativity guarantees ℏ is determined by the partition geometry. It's not a free parameter.

**Step 2 (Boundary-only dependence).** A substantial lemma showing that ℏ depends only on the boundary modes, not on the deep interior of the hidden sector. Decompose the hidden sector into boundary modes C_B (near the horizon) and deep modes C_D (far from the horizon):

$$\mathcal{C}_H = \mathcal{C}_B \times \mathcal{C}_D$$

The proof has three parts: (i) spatial locality means V talks to B, and B talks to D, but V doesn't talk directly to D; (ii) on timescales t ≪ τ_B, the deep sector barely moves (displacement ~ 10⁻³²); (iii) because the deep modes are frozen, the sum over them produces a trivial factor:

$$T_{ij}(t) = \underbrace{\frac{1}{|\mathcal{C}_B|} \sum_{b} \delta_{x_j}[\pi_V(\varphi_t^{VB}(x_i, b))]}_{T^{(B)}_{ij}(t)} + \mathcal{O}(t/\tau_B)$$

The transition probabilities depend only on boundary dynamics. Since ℏ is determined by transition probabilities, ℏ depends only on boundary quantities: c, G, and ε. This excludes dependence on H — if ℏ depended on H, observers at different cosmic epochs would have different quantum mechanics.

**Step 3 (Dimensional analysis).** There's a unique combination of c, G, and ε with dimensions of action:

$$[\hbar] = \frac{[c]^3 \, [\epsilon]^2}{[G]} = \text{kg·m}^2/\text{s} \quad \checkmark$$

So ℏ = β c³ε²/G, where β is a dimensionless constant that dimensional analysis alone can't fix.

**Step 4 (Thermal self-consistency).** We have two independent descriptions of the horizon temperature:

*Classical:* T_cl = c²ε²κ/(8πGk_B) — computed from the geometric substratum, no ℏ.

*Quantum:* The emergent QFT lives on a spacetime with a bifurcate Killing horizon. Standard QFT on curved spacetime gives a KMS thermal state at temperature:

$$T_Q = \frac{\hbar \kappa}{2\pi c k_B}$$

A thermometer at the horizon must read the same temperature either way. Setting T_cl = T_Q:

$$\frac{c^2 \epsilon^2 \kappa}{8\pi G} = \frac{\hbar \kappa}{2\pi c}$$

The surface gravity κ cancels from both sides. Solving:

$$\boxed{\hbar = \frac{c^3 \epsilon^2}{4G}}$$

This fixes β = 1/4.

**Why this is not circular.** The KMS temperature T_Q contains ℏ as an *unknown*. The classical temperature T_cl contains no ℏ at all. The logic is sequential: Part I proves quantum mechanics emerges with some ℏ → the emergent QM predicts T_GH(ℏ) → the classical temperature T_cl was calculated independently → matching them fixes ℏ. This is a "gap equation," the same structure used routinely in condensed matter physics. If T_cl had depended on the deep hidden-sector volume (it doesn't), or if T_Q had been state-dependent (it isn't), the matching wouldn't work. The fact that it works is a non-trivial self-consistency check.

---

## The D-Gauge Completeness Theorem (§5.3)

**The problem.** The relation T_ij = |U_ij|² discards phase information. Could different Hamiltonians give the same transition probabilities?

**The theorem.** If |U'_ij(t)|² = |U_ij(t)|² for all i, j, t, then H' = DHD† where D is a diagonal unitary (a physically meaningless relabeling of basis phases).

**The proof in three steps:**

*Step 1 (eigenvalue recovery):* Fourier analysis of T_ij(t) extracts the energy differences E_k - E_l. Non-degeneracy of energy gaps means E'_k = E_k + E₀ (same eigenvalues up to a global shift).

*Step 2 (modulus recovery):* The diagonal Fourier coefficients give |V_ik|² directly. So |V'_ik| = |V_ik|.

*Step 3 (phase structure):* Writing V'_ik = V_ik e^{iδ_ik} and requiring all Fourier coefficients to match gives the double-difference condition:

$$\delta_{ik} - \delta_{il} - \delta_{jk} + \delta_{jl} = 0 \pmod{2\pi}$$

The general solution: δ_ik = α_i + β_k — a sum of a row phase and a column phase. This is just basis rephasing.

**The dimensional obstruction.** The unitary U(t) is dimensionless. The Hamiltonian Ĥ = iℏ ∂_tU · U† contains ℏ, which is dimensionful. No amount of dimensionless data can fix a dimensionful constant. This is why Step 4 (thermal matching) is not just a convenient check but the *mathematically obligatory* step: it's the only place where dimensionful physical input enters the framework.

---

## The Discreteness Scale (§6)

### What ε = 2 l_p means

Rearranging the gap equation ℏ = c³ε²/(4G):

$$\epsilon^2 = \frac{4\hbar G}{c^3} = 4 \, l_p^2$$

where l_p = √(ℏG/c³) is the Planck length. Therefore ε = 2 l_p.

**What this is:** The framework has one free geometric parameter — the discreteness scale ε. The gap equation fixes its relationship to ℏ. Given the measured value of ℏ, the discreteness scale is determined: ε = 2 l_p ≈ 3.2 × 10⁻³⁵ meters.

**What this is NOT:** This is not an independent prediction of ε. The framework contains one free parameter and one equation relating it to known constants. The self-consistency condition pins ε to the Planck regime but doesn't predict a number that wasn't already implicitly known.

### The Bekenstein-Hawking Entropy — Why the 1/4 factor is derived

The number of independent modes on the cosmological horizon is:

$$N_{\text{modes}} = \frac{A}{\epsilon^2} = \frac{A}{4 \, l_p^2}$$

This is the Bekenstein-Hawking entropy:

$$S_{\text{BH}} = \frac{A}{4 \, l_p^2}$$

The factor of 1/4 — which Bekenstein and Hawking introduced as a proportionality constant in 1973 — is here derived: each minimal cell of area ε² = 4 l_p² contributes one unit of entropy. The 4 in the denominator comes from ε = 2 l_p.

**Why this is significant:** The 1/4 factor has been a mystery for 50 years. Most frameworks either assume it or derive it within constructions specifically designed to produce it. Here it follows from the gap equation with no additional input.

### Self-consistency bounds on ε

**If ε² ≪ l_p²:** Sub-Planckian cells would need further subdivision, creating a second trace-out within the first. This would make ℏ multi-valued — contradicting the observed universality of ℏ.

**If ε² ≫ l_p²:** Super-Planckian cells would be too coarse. The emergent quantum description would assign distinct quantum states to configurations that are physically identical.

The self-consistency condition ε = 2 l_p is the unique value where neither pathology occurs.

---

## The Two Levels

Now the cosmological constant problem dissolves. But first, a crucial link: how does finite-dimensional quantum mechanics become quantum *field* theory — with independent modes, each carrying zero-point energy?

The answer is spatial locality. The classical substratum has it — neighboring cells interact, distant cells don't. The paper proves that the emergent quantum description inherits it. The argument is direct: the Barandes correspondence maps each classical configuration $(x_1, x_2, \ldots, x_N)$ to a quantum basis state $|x_1, x_2, \ldots, x_N\rangle$. That's already a tensor product. The only question is whether the emergent Hamiltonian respects the structure. And it must, because if two configurations differ only at sites that aren't neighbors, the classical dynamics can't connect them in an infinitesimal time step — so the transition probability between them is zero — so the corresponding quantum Hamiltonian matrix element is zero. The emergent Hamiltonian couples only neighboring cells, exactly like the classical one. You get a lattice quantum field theory with a built-in ultraviolet cutoff at $\epsilon = 2\,l_p$.

This is what makes the CC dissolution work. The QFT has independent modes. Each mode gets a zero-point energy. The sum diverges. And the "worst prediction in physics" follows — but only within the emergent description.

The critical insight is that general relativity and quantum field theory are not competing answers to the same question. They are answers to *different questions*, asked at different levels of the same reality.

**Level 1: The classical substratum.** Spacetime geometry is part of the fundamental layer. The metric tensor evolves via Einstein's field equations. The stress-energy tensor that sources gravity is the classical stress-energy of the total microstate. At this level, the vacuum energy density sits at the critical scale: $\rho \sim H^2/G \sim 10^{-9}$ J/m³. No zero-point energy. No discrepancy.

**Level 2: The emergent quantum description.** For an embedded observer tracing out the hidden sector, the mandatory quantum description assigns a zero-point energy of $\frac{1}{2}\hbar\omega$ per mode. Sum to the Planck cutoff and you get $\rho_{\text{QFT}} \sim 10^{113}$ J/m³. This number is real *within the quantum description* — it reflects the magnitude of the trace-out noise — but it is not a source term in Einstein's equations, because those equations operate at the classical level, which is logically prior to the quantum description.

This ordering is not a choice but is forced by three independent requirements. First, the partition must be definite — not in superposition — for the trace-out to be well-defined; a partition in superposition would yield an incoherent mixture of inequivalent quantum theories. Second, the partition is defined by the causal structure, which is determined by null geodesics of the metric; if the metric were derived from QM, the derivation would be circular (QM → metric → causal structure → partition → QM). Third, $\hbar$ is determined by the boundary geometry; if the geometry were itself quantum-mechanical, $\hbar$ would depend on a quantum state, contradicting its observed universality.

The $10^{122}$ ratio between the two answers is not a discrepancy. It equals $S_{\text{dS}}$ — the Bekenstein-Hawking entropy of the cosmological horizon — which is the number of hidden-sector degrees of freedom the trace-out compresses into the emergent quantum state. The "worst prediction in physics" is the information compression ratio of the observer's blind spot. A category error, not a fine-tuning failure.

This is not a prediction awaiting future data. The observed vacuum energy has been measured since 1998, and it sits exactly at the classical geometric scale — the value the framework expects. Meanwhile, every attempt to search for a cancellation mechanism within quantum-first frameworks have found nothing. The framework explains why: there is nothing to cancel.

This track record is itself evidence for the ordering. The question of whether geometry is prior to quantum mechanics or quantum mechanics is prior to geometry is usually treated as a philosophical preference. But it has an empirical signature sitting in plain sight: one ordering produces the worst prediction in physics and has no solution; the other predicts the observed value and explains the discrepancy as a derived quantity. That doesn't prove the ordering is correct — the gravitational wave echo prediction provides a more direct test — but it's existing evidence, not a future hope.

---

## What Quantum Weirdness Looks Like From Here

If quantum mechanics is an emergent description forced on embedded observers, the standard quantum puzzles acquire straightforward readings.

**The double-slit experiment.** The particle goes through one slit. The interference pattern arises because the transition probabilities are computed by marginalizing over the hidden sector, and the hidden sector includes the field configuration near both slits. Opening or closing the second slit changes the boundary conditions, which changes the marginalization, which changes the pattern. The "wave-like" behavior is the hidden sector's influence shifting when the geometry changes.

**Entanglement.** Two particles prepared together share a joint transition matrix inherited from the trace-out. The correlations are encoded in the structure of the dynamics itself, not in a hidden variable you could integrate over. This is why Bell inequality violations occur: the standard factorization assumption fails for indivisible processes. The framework reproduces quantum correlations exactly up to Tsirelson's bound, without faster-than-light signaling and without superdeterminism.

**The measurement problem.** Measurement produces definite outcomes through the indivisible dynamics. When Wigner can't access his Friend's lab, he traces out its internal degrees of freedom and assigns a superposition. The superposition reflects Wigner's epistemic situation — what *he* can infer — not the Friend's physical state. Branching in the Many-Worlds sense is a feature of the compressed description, not of the underlying reality.

---

## Predictions

The framework is not just a reinterpretation. It makes specific, falsifiable predictions — and, crucially, it makes predictions in domains it was not designed to address.

**Dark energy evolution.** Because the hidden sector's dimensionality changes as the Hubble parameter $H$ evolves (the horizon area is $A = 4\pi c^2/H^2$), the emergent vacuum energy inherits a dependence on $H$. The predicted form matches the Running Vacuum Model: $\Lambda_{\text{eff}} = \Lambda_0 + \nu H^2$. The coefficient $\nu$ is computed from the spectral structure of the horizon: the trace-out compression noise is distributed over $\mathcal{N} = \ln(c/\epsilon H)$ spectral decades, giving a conformal benchmark of $\nu \approx 2.45 \times 10^{-3}$ with a systematic range of $\sim 1$–$5 \times 10^{-3}$ (the dominant uncertainty is the spectral assumption, not the cosmological parameters). DESI's 2024–2025 data releases report evidence for evolving dark energy at $2.8\sigma$–$4.2\sigma$, with phenomenological fits consistently finding $\nu \sim 1$–$4 \times 10^{-3}$ — the range in which the framework's prediction sits.

**Gravitational wave echoes.** At a proper distance of about one discreteness scale ($\epsilon = 2\,l_p$) outside a black hole horizon, an infalling mode's wavelength hits the discreteness floor and must scatter back. For a 30 solar-mass remnant, the predicted echo delay is on the order of 50 ms.

**The dark sector as corroboration.** The trace-out that produces quantum mechanics has a gravitational consequence that the paper did not set out to find. The boundary entropy — the $S_{\text{dS}}$ modes traced out to produce the quantum description — has thermal energy that, distributed over the Hubble volume, equals the critical density exactly. A crucial subtlety: this thermal energy is computed entirely from pre-trace-out (classical) quantities — the number of boundary modes, the classical horizon temperature, and the Hubble volume — with no reference to $\hbar$ or the emergent quantum description. This is what distinguishes the boundary entropy's gravitational contribution from the QFT zero-point energy ($\rho_{\text{QFT}} \sim 10^{113}$ J/m³), which exists only *after* the trace-out and is an artifact of the emergent description. The framework denies that the zero-point energy gravitates (this is the CC dissolution of Part II); the boundary entropy's classical thermal energy *does* gravitate, at the scale $\rho_{\text{crit}} \sim 10^{-9}$ J/m³.

The paper proves that this entropy has no operator in the emergent QFT. The baryonic sector — what QFT can account for — is ~5% of $\rho_{\text{crit}}$. The remaining ~95% is the boundary entropy: gravitationally active, invisible to the emergent description, and persistent through P-indivisibility (condition C2). This matches the observed composition of the universe, in which ~95% of the gravitational content has no source in particle physics. The uniform component corresponds to dark energy (handled by Part II's CC dissolution); the structured component (dark matter) is a candidate consequence of matter-induced entropy redistribution, though the redistribution profile requires further work. That axioms designed to derive quantum mechanics also account for the dark sector's total budget is independent corroboration that observational incompleteness is capturing real structure.

The conjunction is distinctive: dark energy evolution in RVM form, gravitational wave echoes, and a natural account of the dark sector's total gravitational budget — all from four axioms about embedded observation. No competing framework produces all three. The parallel with the cosmological constant dissolution is exact. Part II identifies the $10^{122}$ discrepancy as the *information compression ratio* of the trace-out — how much the emergent description distorts the vacuum energy. Part III identifies the ~95% dark sector as the *gravitational occlusion fraction* — how much of the gravitational universe the trace-out hides from the emergent description. Together, they account for the two largest anomalies in modern cosmology as two aspects of a single phenomenon: the cost of observing the universe from within.

---

## Philosophical Lineage

The paper is a physics paper, but its core claims — that observers face irreducible limits, that two irreconcilable descriptions can both be correct, that incompleteness is a structural feature rather than a deficiency — sit at the intersection of some of the oldest debates in philosophy. A systematic mapping against the major traditions reveals a striking pattern: broad support for most of the framework, and near-universal resistance to one specific thesis.

### The seven claims

The framework rests on seven implicit philosophical commitments:

1. **Embedded observers face irreducible limits.** No observer inside a system can access the complete state.
2. **QM and GR are both correct** within their domains.
3. **The hidden sector is permanently inaccessible** — not due to technological limitations, but structural ones.
4. **The underlying reality is local and definite.** Indeterminacy belongs to the observer's description, not to the world.
5. **Incompleteness is structural, not deficient.** The limitation arises because the observer is made of the same elements as the universe it is trying to describe — a physical form of self-reference. This is analogous to Gödel's incompleteness theorem, not to ignorance that better instruments could cure.
6. **The description is observer-relative.** Different partitions yield different emergent physics.
7. **The two descriptions are irreconcilable** — not because one is wrong, but because they are complementary projections of a single reality that no embedded observer can access directly.

Claims 1, 5, 6, and 7 enjoy broad philosophical support across nearly every tradition examined. Claim 4 — that the underlying reality is definite — is the paper's most philosophically isolated thesis.

### The Gödel connection

The analogy between this framework and Gödel's incompleteness theorem is not merely metaphorical. Gödel proved that a formal system rich enough to encode arithmetic cannot prove all true statements about itself from within — the limitation arises because the system is self-referential, capable of constructing sentences that refer to its own provability. The observer in this framework faces a structurally parallel situation: the reason a cosmological horizon exists at all is that the observer is a physical subsystem made of the same fields, obeying the same speed-of-light constraint, as the universe it is trying to describe. An observer not made of the universe's own elements would not face a horizon and would not be forced into a quantum description. The incompleteness is a consequence of self-inclusion.

The connection can be made precise through Wolpert's limits of inference [19], which the paper cites. Wolpert proved, using diagonal self-referential arguments directly descended from Gödel's, that any inference device embedded in the universe it is trying to predict faces fundamental limits — not because of noise or finite resources, but because complete self-prediction is logically impossible. The present framework provides the concrete physical mechanism by which Wolpert's logical limitation manifests: the causal partition enforces the trace-out, the trace-out produces P-indivisibility, and P-indivisibility is quantum mechanics. The $10^{122}$ compression ratio — the Bekenstein-Hawking entropy of the cosmological horizon — is the quantitative measure of how much information self-inclusion forces the observer to lose.

The key difference from Gödel is in the *form* of self-reference. Gödel's is syntactic: the system encodes a sentence that says "I am not provable." The framework's is physical: the observer is made of the described, so complete description would require the observer to fully encode its own state plus everything causally connected to it, which the causal structure forbids. Wolpert sits between the two, using Gödelian logic applied to physical systems. Together they form a chain: Gödel (formal systems cannot completely describe themselves) → Wolpert (physical inference devices cannot completely predict the systems they inhabit) → this framework (the specific mechanism is the causal partition, and the specific cost is quantum mechanics).

Hofstadter's *Gödel, Escher, Bach* argues that self-referential systems produce genuinely emergent higher levels — "strange loops" where a system's hierarchical levels fold back on themselves, generating properties invisible at the lower level. This framework agrees: quantum mechanics is the real, irreducible description available to any embedded observer, just as Hofstadter's "I" is real even though it emerges from neurons. The strange loop is intact — the observer, made of the universe's own elements, generates through self-inclusion an emergent description that governs everything the observer can access. The disagreement with Hofstadter is narrow but consequential: he argues that once the emergent level is established, the substrate beneath it is explanatorily inert. The cosmological constant problem suggests otherwise. The $10^{122}$ discrepancy exists precisely because the emergent quantum description and the classical substrate assign different vacuum energies, and only the substrate's value matches observation. The loop has a floor, and the floor matters.

### Closest ancestor: Nicholas of Cusa

Of all thinkers surveyed, the fifteenth-century cardinal Nicholas of Cusa provides the most precise structural alignment. His *docta ignorantia* (learned ignorance) is essentially Claim 5: the highest knowledge is knowing what we cannot know, and this is an intellectual achievement, not a failure. His *coincidentia oppositorum* (coincidence of opposites) maps onto Claim 7 with remarkable precision: contradictions irreconcilable in the finite realm dissolve in infinity — the infinitely large circle's circumference becomes a straight line, the infinite polygon becomes a circle. QM and GR, irreconcilable within any finite observational framework, would be coincident in the infinite ground that generates both.

Most strikingly, Cusa's "wall of Paradise" from *De Visione Dei* maps onto Claim 3: an insurmountable boundary beyond which finite intellect cannot pass. Scholars like Emmanuel Falque interpret reaching this wall not as escaping through it but as *inhabiting the boundary* — profoundly compatible with a framework where understanding the limit is itself the deepest available insight.

### Deepest ontological parallel: Spinoza

Spinoza's attribute theory is arguably the single closest ontological parallel. One substance (God/Nature) expresses itself through infinite attributes, of which humans know only two: Thought and Extension. Jonathan Bennett's "barrier doctrine" captures the key feature: each attribute must be conceived through itself — no explanatory flow crosses between them. This is precisely Claim 7: two complete, correct descriptions that are structurally irreconcilable, yet both describe the same underlying reality. Spinoza's substance is fully determinate, aligning with Claim 4. His parallelism doctrine — the order of ideas is the same as the order of things — means the two descriptions track the same structure through incommensurable vocabularies.

The divergence is epistemological: Spinoza believes reason achieves adequate knowledge of reality through *scientia intuitiva* (intuitive knowledge). The paper's permanent limits directly contradict this ambition.

### The recurring fault line: Claim 4

Across every tradition examined, a striking pattern emerges. The claim that underlying reality is "local and definite" faces resistance from virtually every direction:

**Kant** prohibits positive characterization of the noumenal realm as dogmatic metaphysics — you can know *that* things-in-themselves exist but never *what* they are. **Hegel** diagnoses a performative contradiction: to posit a hidden sector and characterize it as containing standard physics is already to have crossed the boundary you claim is uncrossable. **Nietzsche** attacks it as residual Platonism — having correctly shown that all observation is perspectival, the paper reinstates the very "true world" his career was dedicated to destroying. **Wittgenstein** rejects it as nonsensical: asserting what lies beyond the limits of the sayable transgresses exactly the limits the paper identifies.

**Nagarjuna** identifies it as *svabhāva*-reification — attributing inherent existence to what Buddhist emptiness (*śūnyatā*) says lacks it. **Daoism** warns against naming the unnameable: the Dao that can be spoken is not the eternal Dao, and calling reality "definite" is itself an act of conceptual carving. **Whitehead** insists reality is fundamentally processual and creative, involving genuine indeterminacy — removing that indeterminacy robs the cosmos of its creative character.

**Advaita Vedanta** comes closest to full support — Brahman is indeed a definite underlying reality — but insists it is *accessible*: the observer IS the underlying reality, and liberation (*mokṣa*) consists in recognizing this identity. Every Hindu and Buddhist soteriology rejects permanent inaccessibility.

Only Spinoza (whose fully determinate substance is naturally definite) and Worrall's epistemic structural realism (which posits real but unknowable natures behind structures) provide genuine philosophical support for Claim 4.

### What's genuinely new

The paper's philosophical lineage is not a single line of descent but a mosaic. Its structural epistemology draws from Kant through Wittgenstein to Wolpert. Its complementarity thesis combines Bohr's physics with Cusa's coincidence of opposites and Daoist yin-yang. Its projection metaphysics reaches through Plato's cave and Plotinus's emanation to Advaita Vedanta's maya-Brahman distinction.

What is genuinely new is the *combination*: accepting Bohr's complementarity while insisting on Einstein's realism, grounding Kantian limits in physical structure while claiming knowledge of noumenal character, embracing Cusanian learned ignorance while grounding it in a concrete physical mechanism — the Gödel → Wolpert → causal partition chain described above. The traditions reveal that this combination creates a productive philosophical tension — the paper claims to know the character of what it proves unknowable. Whether this tension is a contradiction (as Hegel would insist), a residual Platonism (as Nietzsche would charge), or a legitimate achievement of learned ignorance (as Cusa would celebrate) may be the framework's deepest philosophical question.

---

## Frequently Asked Questions

**"Isn't this just another interpretation of quantum mechanics?"**
No. Interpretations (Copenhagen, Many-Worlds, Bohmian mechanics) accept the quantum formalism and disagree about what it *means*. This framework *derives* the quantum formalism from non-quantum premises and proves the derivation is the only possible one. It makes quantitative predictions — the value of ℏ, dark energy evolution, and gravitational wave echoes — that interpretations do not, and it accounts for the dark-sector concordance as an automatic consequence.

**"Doesn't Bell's theorem rule out hidden variable theories?"**
Bell's theorem rules out *local* hidden variable theories satisfying a specific factorizability condition. This framework violates that factorizability — not through faster-than-light signals, but because P-indivisible joint dynamics don't permit the decomposition Bell's theorem assumes. The framework reproduces exactly Tsirelson's bound (the maximum quantum violation), no more and no less.

**"If everything is deterministic underneath, where does randomness come from?"**
From ignorance. The total system is deterministic, but the observer can't access the hidden sector. Different hidden states compatible with the same visible state lead to different outcomes. The observer must assign probabilities — not because the universe is random, but because their information is incomplete.

**"What about dark matter?"**
The framework doesn't set out to explain dark matter, but it produces a natural account of why ~95% of the universe's gravitational budget has no source in particle physics. The boundary entropy — the modes traced out to produce QM — has thermal energy equal to the critical density. Crucially, this thermal energy is computed from purely classical quantities (the number of boundary modes and the classical horizon temperature) — it exists before the trace-out, unlike the QFT zero-point energy, which is an artifact of the emergent description. The boundary entropy is therefore gravitationally active (it curves spacetime at the classical level) but invisible to the emergent QFT (the boundary modes were traced out to produce it). The baryonic sector accounts for ~5% of $\rho_{\text{crit}}$; the rest is boundary entropy. The uniform component is dark energy (Part II). Whether the matter-induced *redistribution* of this entropy produces local effects resembling dark matter at galaxy scales is an open question requiring a quantitative force law beyond the axioms. What the framework proves is that the total dark sector budget is an automatic consequence of the trace-out — not an additional input.

**"Why does gravity 'see' the classical vacuum energy and not the quantum one?"**
Because the spacetime metric exists at the classical level, *before* the quantum description emerges. The quantum zero-point energy is a feature of the observer's compressed description. It's real for quantum experiments (the Casimir effect, the Lamb shift) but doesn't appear in the stress-energy tensor that governs curvature. The $10^{122}$ discrepancy is the information compression ratio — the entropy of the observer's blind spot.

**"How can the paper claim reality is 'definite' if it's permanently inaccessible?"**
This is the paper's most philosophically contested thesis (see *Philosophical Lineage* above). The paper's defense is that the claim follows from the derivation's own logic: the axioms posit deterministic dynamics on a phase space, and the theorem shows that quantum indeterminacy arises from tracing out part of that phase space — not from any indeterminacy in the underlying evolution. The "definiteness" is a consequence of the starting premises, not a speculative addition. Whether those premises are the right ones to start from is, of course, an open question — but within the framework, Claim 4 is a theorem, not an assumption.

**"Doesn't holographic physics show that spacetime comes from entanglement?"**
This is probably the strongest objection to the framework's ordering — classical spacetime first, quantum mechanics second. The Ryu-Takayanagi formula says entanglement entropy equals boundary area divided by $4G$. Van Raamsdonk argued that reducing entanglement disconnects spacetime. Programs like ER=EPR and "it from qubit" read these results as evidence that quantum entanglement is prior to geometry.

The framework offers an alternative reading. If the quantum description is produced by tracing out over a geometric boundary, then *of course* its entanglement entropy is proportional to the boundary's area — the information content of the trace-out is set by the number of modes crossing the boundary, which scales with area. The Ryu-Takayanagi formula, on this account, isn't a hint that entanglement builds geometry; it's a consequence of the fact that geometry built the entanglement. The Bekenstein-Hawking entropy $S = A/(4\,l_p^2)$, which the paper derives, is exactly this statement.

The correlation between entanglement and geometry is real either way. The question is which direction the arrow of explanation points. The two orderings make different empirical predictions: if geometry emerges from entanglement, spacetime structure should break down at high energy; if quantum mechanics emerges from geometry, the quantum description should break down near the discreteness scale while the geometric substratum persists. The gravitational wave echo prediction provides one test. But the cumulative case is already substantial: the geometry-first ordering produces the observed vacuum energy, the Bekenstein-Hawking $1/4$ factor, the value of $\hbar$, the dark-sector concordance, and dark energy evolution consistent with DESI data — six independent consequences matching observation. The quantum-first ordering produces the $10^{122}$ discrepancy, treats $\hbar$ and the $1/4$ factor as unexplained inputs, and has no natural account of the dark sector.

---

## The Decompression Algorithm

There is a way to state what the framework means that is sharper than anything in the formal paper.

An observer inside the universe receives incomplete data — the visible sector only. The characterization theorem proves that there is exactly one self-consistent algorithm for making predictions from this incomplete data. That algorithm is quantum mechanics.

Everything in QM is a feature of the algorithm, not a feature of the underlying reality. The wave function is the algorithm's internal state variable — the bookkeeping device it uses to track what it knows and what it doesn't. Complex amplitudes are the algorithm's arithmetic — the specific number system the reconstruction requires. Interference is what happens when the algorithm combines two incomplete pathways and their bookkeeping entries partially cancel. Entanglement is the algorithm's encoding of correlations that were written into the hidden sector during preparation and haven't been read back yet. The Born rule is the algorithm's output format — the way it converts its internal state into predictions the observer can check.

None of these are properties of the deterministic substratum. In the substratum, there are no wave functions, no complex numbers, no interference, no entanglement. There are configurations evolving under a Hamiltonian flow. That's all. The entire apparatus of quantum mechanics — every textbook, every equation, every experiment — is what the decompression algorithm looks like from the inside.

### Antimatter as algorithmic artifact

This reframing changes the understanding of specific phenomena. Consider antimatter.

The standard account: the Dirac equation, which combines quantum mechanics with special relativity, has solutions with both positive and negative energy. The negative-energy solutions correspond to antiparticles — particles with opposite charge and quantum numbers. Every particle must have an antiparticle, because CPT invariance (a theorem of any local Lorentz-invariant quantum field theory) requires it.

The framework's account: the trace-out over the hidden sector forces the reconstruction algorithm to use two-signed amplitudes. When the algorithm operates in a relativistic context — which it must, because the substratum's causal structure is relativistic — the two-signed amplitude structure becomes the two-signed energy structure of the Dirac equation. Negative-energy solutions aren't additional features of reality. They're what the algorithm requires for self-consistency when the incomplete data comes from a relativistic system.

The parallel to the coin-and-die model is direct. The intermediate propagator:

$$\Lambda(2,1) = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

has entries of $-1$ — "anti-probabilities" that don't exist in the substratum (where every transition probability is between 0 and 1). These negative entries are the minimal-model ancestors of antimatter. They arise for the same reason: the algorithm can't reconstruct the observed dynamics without them. In the toy model, the $-1$ entries encode the fact that the die remembers and reverses the coin flip — information backflow that no positive-entry matrix can describe. In the relativistic case, the negative-energy solutions encode the fact that the relativistic trace-out requires a doubled Hilbert space to remain self-consistent.

In both cases: the substratum has no doubling. The algorithm demands one.

### Nothing in quantum mechanics explains a fundamental phenomenon

This is the deepest implication of the framework, and it is worth stating plainly.

The wave function does not explain what an electron is doing between measurements. It encodes what the algorithm computes given the observer's data. Interference does not explain why particles behave like waves. It reflects the algorithm's method of combining incomplete information. Entanglement does not explain a mysterious connection between distant particles. It reflects correlations stored in the hidden sector that the algorithm must track but cannot directly access. Antimatter does not explain a second kind of fundamental stuff. It reflects the algorithm's need for two-signed amplitudes in a relativistic context.

Every quantum phenomenon is an output of the decompression algorithm. The only fundamental phenomenon is the compression itself: the observer cannot see past the horizon, and the characterization theorem dictates the unique form of the resulting reconstruction.

This doesn't make quantum phenomena less real. Temperature is also an emergent phenomenon — a single molecule has no temperature. But temperature boils water, drives engines, and burns skin. Its emergence from statistical mechanics doesn't diminish its causal power within the emergent description. The same holds for every quantum phenomenon: they are causally potent, experimentally real, and the only physics accessible to an embedded observer. But they are features of the observer's necessary algorithm, not features of the universe's fundamental structure.

This resolves what is arguably the oldest open question in quantum foundations: *is the wave function real?* Since 1926, physics has been split between epistemic interpretations (the wave function is just a bookkeeping device tracking the observer's knowledge — it doesn't correspond to anything physical) and ontic interpretations (the wave function is a real physical entity — a field on configuration space, or a branching structure, or a guiding wave). The framework shows that both sides share a hidden assumption: that "real" means "fundamental." The epistemic camp says the wave function isn't fundamental, therefore it isn't real. The ontic camp says it's real, therefore it must be fundamental. Both are wrong. The wave function is real *and* not fundamental — in exactly the same way as antimatter, temperature, and every other emergent phenomenon. Within the bounded projection — which is all an embedded observer will ever have access to — the wave function, the positron, the interference pattern, and the electromagnetic field all have exactly the same ontological status. They are all outputs of the decompression algorithm. They are all experimentally real. And none of them exist in the substratum.

The analogy to data compression is precise. Lossy compression (like JPEG or MP3) discards information and reconstructs an approximation. The reconstruction has artifacts — ringing near edges in JPEG, pre-echo before transients in MP3. These artifacts are not in the original signal. They are features of the reconstruction algorithm applied to incomplete data.

Quantum mechanics is the reconstruction. The $10^{122}$ discarded bits (the hidden sector) are the lost information. Wave functions, interference, entanglement, and antimatter are the artifacts. They are real — as real as JPEG ringing is visible — but they are properties of the reconstruction, not of the original.

The difference from ordinary compression: with JPEG, you can access the original file. With the universe, you cannot. The reconstruction is all we will ever have. Its artifacts are our physics. And the characterization theorem proves that no other reconstruction is possible — this is the unique algorithm, and its artifacts are the unique artifacts. Quantum mechanics is not one possible decompression of incomplete cosmological data. It is the only one.

---

## What This Means

The search for a "theory of everything" that unifies quantum mechanics and general relativity has assumed that the two theories describe the same level of reality and must be reconciled there. This paper argues that assumption is wrong. The two theories operate at different levels — one fundamental, one emergent — and their apparent contradiction is the information-theoretic cost of being an observer trapped inside the system you're trying to describe.

The apparent conflict between QM and GR, the $10^{122}$ vacuum energy discrepancy, and the dark sector are three faces of the same fact. The first is the existence of the trace-out. The second is its information compression ratio. The third is its gravitational occlusion fraction. All three are mandatory consequences of observational incompleteness — and all three match what we observe.

The universe is not broken. We are observing it from within.

---

## Corroboration: The Rigidity Test

A natural objection to any framework this sweeping is: maybe it only works because it was built to work. Maybe the axioms were chosen to produce QM, and the cosmological application was chosen because it fits. A flexible framework that can accommodate anything predicts nothing.

A companion paper ("Dynamics Selection and Emergent General Relativity in the Observational Incompleteness Framework") tests this by asking a question the main paper doesn't address: if you build a concrete system satisfying the axioms, does the framework constrain the dynamics? And if so, does the constrained dynamics produce anything beyond QM — something the framework wasn't designed to deliver?

It does, on both counts.

**The dynamics is unique.** Among all second-order reversible nearest-neighbor dynamics on a lattice, the requirements of center independence (necessary for emergent QM), spatial isotropy, and linearity select exactly one: the discrete wave equation. This holds for any alphabet size and any dimension. Center independence is necessary because center-dependent rules allow the visible sector to partially predict itself, suppressing the information backflow that produces QM — an effect proven analytically on the full lattice via an information-screening mechanism. Linearity is selected by three independent criteria: it gives maximum propagation speed, it uniquely maximizes P-indivisibility among linear rules, and it is the only choice for which horizons are in thermal equilibrium (nonlinear dispersion breaks the Unruh effect).

**The dynamics passes seven independent checks.** The wave equation — selected solely by the QM requirement plus symmetry — turns out to produce: (1) non-Markovian reduced dynamics (emergent QM), (2) a causal structure with the correct spacetime dimension, (3) the gap equation for ℏ, (4) entanglement entropy proportional to boundary area, (5) a Lorentz-invariant dispersion relation, (6) the correct Unruh temperature at horizons, and (7) all inputs to Jacobson's thermodynamic derivation of Einstein's field equations. Each of these is an independent check that could have come out wrong — the entropy could have scaled with volume, the dispersion could have been non-relativistic, the horizon state could have been non-thermal. None of these failures occurs.

**No free parameters.** The wave equation is selected, not chosen. The lattice spacing is fixed by the gap equation. The entropy coefficient is determined by thermal matching. The dispersion relation is an algebraic identity. There is nothing to tune.

This is what rigidity looks like. A framework that produces QM from one set of arguments and then, without modification, produces the inputs for GR from a completely different set of arguments — lattice dynamics, dispersion relations, entanglement Hamiltonians — is making a structural claim that goes well beyond the original derivation. Each passed check is a point where the framework could have been falsified and wasn't. Seven passed checks with no free parameters is not proof, but it is the kind of evidence that distinguishes a framework describing something real from one that was engineered to fit.

---

## What Is the Lattice?

The rigidity test proves that the wave equation on a lattice produces both QM and GR. But what *is* the lattice? Is the universe literally a grid of cells at the Planck scale? What would the grid be made of? What would it sit in?

A third companion paper ("The Substrate Problem: Structural Foundations of the Observational Incompleteness Framework") addresses these questions head-on. Its answer: the lattice is not a physical object. It is the *coupling structure* of the dynamics — the pattern of which degrees of freedom affect which others.

**The minimal structure.** The paper audits every assumption in the framework and identifies which are necessary for the theorems and which are artifacts of the particular construction. The result: only six structural properties matter — deterministic bijectivity, finite boundary entropy, bounded coupling degree, statistical isotropy, non-trivial partition coupling, and slow-bath capacity. The regular cubic lattice, the specific alphabet size q, the dimensionality d, and even the wave equation are all either derived from these six properties or irrelevant to the predictions. The minimal object is not a lattice. It is a triple: a finite set S, a bijection φ, and a partition V.

**Space as coupling graph.** Given any bijection on a finite set, you can ask: which components of the state affect which others? The answer defines a graph — sites are vertices, and two sites are connected if the dynamics couples them. This graph is not drawn on a pre-existing space. It IS space, at the fundamental level. Distance means "how many coupling steps apart." Area means "how many edges cross the boundary." The area law, the dispersion relation, the Myrheim-Meyer dimension — every spatial property used in the derivation chain is a property of this coupling graph.

This dissolves the container problem. The lattice doesn't sit in anything. There is no ambient manifold. The coupling graph is an abstract mathematical structure — like a number or a group — and any spatial embedding we draw is a representation for our convenience, not a physical fact. Asking "what does the lattice sit in?" is like asking what the number 7 sits in. It's a category error.

**The alphabet is a gauge freedom.** The companion papers prove every result for any alphabet size q ≥ 2. The gap equation contains no q. The Bekenstein-Hawking formula contains no q. The dispersion relation is valid for any q. No experiment could measure q, even in principle. This makes q a gauge freedom — a choice of mathematical description, like choosing a coordinate system or a gauge for the electromagnetic potential. The physical content is the coupling structure, not the microscopic state space.

**Connection to causal set theory.** The bijection's coupling graph, extended in time, generates a causal partial order: event A precedes event B if B is within A's future coupling light cone. This partial order is a causal set in the sense of Bombelli, Lee, Meyer, and Sorkin — the starting point of causal set theory, one of the established approaches to quantum gravity. Causal set theory has always had a specific gap: it postulates a causal order but lacks a deterministic dynamics that produces QM and GR. The OI framework provides exactly this. Sorkin's slogan is "Order + Number = Geometry." The OI version is "Bijection + Locality = QM + GR."

**The hierarchy of physics.** If the fundamental object is (S, φ, V), then every concept in physics is a different aspect of this triple:

- **φ** is the dynamical law — the complete rule mapping states to states.
- **Space** is the coupling structure of φ — which degrees of freedom affect which others. It is determined by φ as the factorization minimizing coupling degree. Space is not a container; it is a relationship.
- **Matter** is the state — the values assigned to the degrees of freedom. A particle is a localized pattern that propagates through the coupling graph. Space and matter are the graph topology and the graph coloring; both come from (S, φ).
- **Energy** is the rate of change of the state under iteration of φ. A high-energy excitation changes rapidly from step to step; the vacuum changes least. Energy is not a substance — it is a measure of how fast a pattern evolves.
- **Time** is the iteration itself — the stepping from one state to the next. There is no continuous time at the fundamental level.
- **Quantum mechanics** is the observer's compressed view of V. It exists because the observer must marginalize over the hidden sector.
- **Gravity** is the thermodynamic limit of the coupling structure — the macroscopic behavior of bounded-degree graphs with area-law entropy.
- **Conservation laws** are emergent. Bijectivity of φ preserves state-space volume (information conservation). Energy conservation is what this looks like in the emergent quantum description (Noether's theorem). Momentum conservation reflects the symmetry of the coupling graph.

None of these are independent substances. They are the same structure viewed at different scales or from different angles. The framework does not unify them by reducing them to a common material. It unifies them by showing they were never separate.

**What remains.** The structural reading leaves some questions genuinely open. Why does our universe have three spatial dimensions rather than some other number? Can the coupling graph evolve dynamically — responding to the state it carries, the way GR's metric responds to the stress-energy tensor? If so, the bijection would need to be state-dependent: the coupling structure at each step determined by the current configuration, while remaining deterministic and bijective at each step. This is the discrete analog of background independence, and whether it can be achieved while preserving all seven links in the derivation chain is an open problem.

But the central claim stands: the fundamental object is (S, φ, V) — a finite set, a bijection, and a partition. Everything else is emergent.

---

*This is a companion overview to "The Incompleteness of Observation" (Maybaum, March 2026), which presents the formal arguments with detailed derivations; "Dynamics Selection and Emergent General Relativity in the Observational Incompleteness Framework" (Maybaum, March 2026), which presents the rigidity test; and "The Substrate Problem: Structural Foundations of the Observational Incompleteness Framework" (Maybaum, 2026), which addresses the ontological status of the lattice. The philosophical lineage section draws on a systematic analysis mapping the paper's claims against the major traditions in Western, Eastern, and contemporary philosophy of science.*


---

## Appendix: Mathematical Summary Tables

### Sections 1–2: What Each Piece Does

| Component | What it establishes | What it uses |
|---|---|---|
| Axioms 1–4 | The physical setup (no QM assumed) | Nothing — these are starting points |
| Partition-relativity (§1.4) | Emergent description depends only on partition | Axioms 1, 3, 4 |
| Emergent stochasticity (§2.1) | Determinism looks random to embedded observer | Axioms 1, 3, 4 |
| P-indivisibility proof (§2.3) | The stochastic process is non-Markovian | Axioms 1, 2 + C1 |
| Accessible-timescale lemma (§2.3) | Non-Markovianity is observable, not just formal | C1 + C2 + C3 |
| Coin-and-die model (§2.4) | Concrete demonstration of all mechanisms | All axioms + all conditions |
| Stochastic-quantum correspondence (§3.1) | P-indivisibility = quantum mechanics | Barandes [10,11] or Stinespring (Appendix A) |
| Necessity proof (§3.3) | QM *requires* C1, C2, C3 | Contrapositives of sufficiency |

### Sections 3–6: The Logical Flow

| Step | What it establishes | Key equation |
|---|---|---|
| §3.1: Stochastic-quantum correspondence | P-indivisibility = QM | T_ij = \|U_ij\|² |
| §3.1: Phase-locking | Quantum Hamiltonian is unique | Fourier analysis of T_ij(t) |
| §3.2: Bell analysis | Framework evades Bell's theorem | Outcome independence violated, parameter independence preserved |
| §3.3: Necessity of C1 | QM requires coupling | No coupling → permutation → P-divisible |
| §3.3: Necessity of C2 | QM requires slow bath | Fast bath → Markov → P-divisible |
| §3.3: Necessity of C3 | QM requires capacity | I ≤ log₂ m bounds memory |
| §3.3: Characterization theorem | QM ⟺ C1+C2+C3 | Biconditional |
| §4: Cosmological horizon | The universe satisfies the axioms | C1 ✓, C2 ✓, C3 ✓ |
| §5.1: Classical temperature | T_cl = c²ε²κ/(8πGk_B) | No ℏ |
| §5.2 Step 1: Uniqueness | ℏ is determined, not free | Partition-relativity |
| §5.2 Step 2: Boundary-only | ℏ depends only on c, G, ε | Deep sector frozen |
| §5.2 Step 3: Dimensional analysis | ℏ = β c³ε²/G | Unique combination |
| §5.2 Step 4: Thermal matching | T_cl = T_Q fixes β = 1/4 | ℏ = c³ε²/(4G) |
| §5.3: D-gauge theorem | No phase ambiguity | Double-difference condition |
| §6: Self-consistency | ε = 2 l_p, S_BH = A/(4l_p²) | ε² = 4ℏG/c³ |

The chain from axioms to ℏ:

Axioms → P-indivisibility → QM → Hamiltonian with unknown ℏ → thermal matching at the horizon → ℏ = c³ε²/(4G) → ε = 2 l_p → S_BH = A/(4 l_p²)

Every link is either a proof or a calculation. No link requires quantum mechanics as input — QM appears as output at step 3 and its parameters are determined by steps 4–6.

---

## Appendix: Key Mathematical Subtleties

**1. The gap equation is a gap equation, not a derivation from nothing.**

The framework has one free parameter (ε). The gap equation relates ε to ℏ. You need to know one to determine the other. The predictive content is:
- The *relationship* ℏ = c³ε²/(4G) — which could have been any function of c, G, ε
- The *consequences* — Bekenstein-Hawking entropy, CC dissolution, dark-sector fraction — which follow from this specific relationship

**2. The KMS condition on the lattice.**

The thermal matching in Step 4 uses the KMS condition, which is proved for continuum QFT on curved spacetime. The emergent QFT from Part I is lattice-regularized with cutoff ε. Thermal periodicity on a lattice has corrections of order (εκ/c)². For the cosmological horizon: εκ/c = εH/c ~ 10⁻⁶¹, so corrections are ~ 10⁻¹²². Negligible, but a referee could ask for a lattice-native proof.

**3. The D-gauge theorem requires genericity.**

The phase-locking and D-gauge results assume non-degenerate spectrum, non-degenerate energy gaps, and non-vanishing overlaps (conditions G1–G3). These fail on a measure-zero set of Hamiltonians. For "almost all" Hamiltonians, the results hold. A referee might ask what happens on the measure-zero set — the answer is that the Hamiltonian is still determined up to a finite discrete ambiguity, which doesn't affect the physics.

**4. Why doesn't the deep sector matter?**

The boundary-only dependence lemma is crucial because without it, ℏ might depend on the vast interior of the hidden sector — which we can't observe or constrain. The lemma shows the deep sector is frozen on observable timescales, so its details are irrelevant. ℏ is a property of the boundary geometry, not of the bulk.

***

**Acknowledgment of AI-Assisted Technologies:** The author acknowledges the use of **Claude Opus 4.6** and **Gemini 3.1 Pro** to assist in synthesizing technical concepts and refining clarity. The final text and all scientific claims were reviewed and verified by the author.
