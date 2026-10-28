<!-- OWNER: R1 title. Working title; the owner chooses the final title. -->

# Observational Incompleteness: Quantum Representations of Partially Observed Deterministic Systems

**Author:** Alex Maybaum  
**Date:** October 2026  
**Status:** DRAFT  
**Classification:** Theoretical Physics / Foundations

***

## Abstract

An observer embedded in a finite deterministic system records only part of its state. Observational incompleteness (OI) is the hypothesis that the statistics such an observer records are the visible marginals of a finite reversible deterministic system of which the observer is a proper part. At any finite horizon, three classes of observable law coincide: finite stochastic laws, visible marginals of finite reversible dynamics, and fixed-basis Born records of finite unitary systems. Each class contains the Markov laws, so the existence of a realization or of a quantum representation does not distinguish any law. The Born dictionary belongs to the definition of the quantum class, and its quadratic exponent is not selected. The content that does discriminate concerns memory. Every deterministic completion of a law with conditional memory carries that memory in its hidden state. On one finite reversible representative, finite recurrence turns history readback into stochastic indivisibility within the recurrence cycle. Worked examples include a two-card game, given with its exact rule and scope.

Three statuses are kept apart. Finite observable-law representability is proved. Exact finite operational quantum mechanics is characterized only under five completion conditions, none of them implied by bare finite OI. Selection of the evolution relating two times is open. A bounded application treats black-hole information recovery as a question about an observer's access class.

***

## 1. The central idea

### 1.1 Embedded observation

An *observation* is a triple $(S,\varphi,V)$. Here $S$ is a total system, $\varphi: S\to S$ is a dynamics, and $V\subsetneq S$ is an observer: a proper subsystem with finitely many distinguishable states, coupled to the complement $H=S\setminus V$ through $\varphi$ [Main §1.2]. In what follows, $S=\mathcal C_V\times\mathcal C_H$ is finite and $\varphi$ is a bijection.

Bijectivity is a reconstruction choice: the reversible representative of the hidden dynamics, motivated by observed near-unitarity. Finiteness of the whole of $S$ is a posit, not a theorem [Main §1.2 Remark; §4.5]. The observer sees $x\in\mathcal C_V$ and not $h\in\mathcal C_H$. Hidden states compatible with the same $x$ send it to different futures, so the visible sector evolves stochastically even though the whole evolves deterministically.

Observational incompleteness (OI) is the physical hypothesis that this is the situation of every physical observer. The statistics it records are the visible marginals of a finite reversible deterministic system of which it is a proper part. The physical identification of nature with such a system is a representation choice, motivated empirically. The theorems below are mathematical statements about such systems, so no experiment bears on them directly. What could be tested is the physical identification, and no test of it at the level of memory witnesses is presently established [Main §4.5].

The incompleteness meant here is inaccessibility of the hidden sector. It is not the joint unsharpness of non-commuting observables. It is present already for a single fixed readout, where no choice between measurements arises, and no uncertainty relation constrains the class of fixed-readout visible laws [Main §3.4].

### 1.2 Why such an observer can appear quantum, and how far that goes

Marginalizing a reversible dynamics over an unobserved register produces three features that are usually associated with quantum theory:
- stochastic laws;
- conditional memory, in which the visible past carries information about the visible future beyond the present;
- the failure of stochastic divisibility, in which the would-be intermediate transition maps acquire negative entries.

The question is how much of quantum theory this reaches. The answer has three parts:
1. **Representability (§2).** At the level of finite-horizon observable laws, the reach is exact and universal. The finite laws of embedded observers coincide with the laws of fixed-basis unitary Born representations, and also with all finite stochastic laws.
2. **Where the content lies (§2.4, §3).** Because representability is universal, the content lies elsewhere: in where the memory must sit, and in what finite recurrence does with it.
3. **Operational quantum mechanics (§6).** Exact operational quantum mechanics, meaning coherent instruments and composites, is reached only under further conditions that bare embedded observation does not imply.

This paper presents these results at the level of finite observable laws, gives worked examples (§4), applies the access viewpoint to black-hole information (§5), and lists the open problems (§6). The full development is [Main]. Its gravitational and lattice applications are in [GR] and the book [Book].

***

## 2. Mathematical foundation

### 2.1 Setting

Fix finite sets $\mathcal C_V$ (the visible alphabet, $|\mathcal C_V|\ge 2$) and $\mathcal C_H$, a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$, and a horizon $K$. A law is a probability distribution $P$ on visible trajectories $(x_0,\dots,x_K)\in\mathcal C_V^{K+1}$.

The visible law of a realization depends on three data: the dynamics, the partition, and the initial law on $\mathcal C_V\times\mathcal C_H$. The prior is part of the realization datum. Invariance under $\varphi$ alone does not select it (`invariance_does_not_select`, `CanonicalMeasure.lean:242`). The counting measure is a maximal-entropy selection, the default rather than a constraint [Main §1.2, §1.4].

Three classes of law are compared [Main §3.4]:

- **$S$:** the finite stochastic laws, that is, all probability distributions on $\mathcal C_V^{K+1}$.
- **$D$:** the visible marginals of finite reversible deterministic systems. These are the visible trajectory laws of some bijection of $\mathcal C_V\times\mathcal C_H$, for some finite $\mathcal C_H$, under an initial law on $\mathcal C_V\times\mathcal C_H$ that may correlate the visible and hidden coordinates.
- **$Q_{\mathrm{fb}}$:** the laws of finite-dimensional unitary systems read out by projective Born measurement in one fixed basis at every step, from an initial state diagonal in that basis, the visible record being a fixed function of each outcome.

### 2.2 The finite-horizon correspondence

**Theorem 1** (finite-horizon stochastic–reversible–unitary equivalence [Main §3.4]). *For every finite visible alphabet and every finite horizon $K$, the three classes coincide:*
$$
S\iff D\iff Q_{\mathrm{fb}} ,
$$
*and each is the set of all probability laws on $\mathcal C_V^{K+1}$.*

The theorem is proved in the kernel as `finite_horizon_equivalence` (`Equivalence.lean:462`). Each of the six directions has its own witness:
- $S\Rightarrow D$ is `S_imp_D` (`:422`);
- $D\Rightarrow Q_{\mathrm{fb}}$ is `D_imp_Qfb` (`:294`);
- $Q_{\mathrm{fb}}\Rightarrow S$ is `Qfb_imp_S` (`:245`);
- $D\Rightarrow S$, $Q_{\mathrm{fb}}\Rightarrow D$ and $S\Rightarrow Q_{\mathrm{fb}}$ are the corresponding compositions (`:466–468`).

None of the three constructions enters as a hypothesis.

*Constructions.*

- **$S\Rightarrow D$.** The hidden register is a clock together with a complete trajectory record. The initial law places the whole trajectory, drawn from $P$, in the record. One step advances the clock and emits the next recorded visible state, and the record makes the step injective. A finite injective map extends to a bijection.

  Main also gives a realization in which the hidden prior is independent of $x_0$: a uniform randomness tape for rational laws, and a product prior over response tables for real kernels [Main §3.4, finite-horizon process dilation]. That independence is proved in prose with exact probes. It is not formalized.
- **$D\Rightarrow Q_{\mathrm{fb}}$.** Set $U_\varphi|x,h\rangle=|\varphi(x,h)\rangle$, which is a permutation unitary (`permMatrix_mem_unitaryGroup`, `EquivalenceChain.lean:179`). A permutation unitary preserves diagonal states (`isDiag_Phi`, `:253`). So projective measurement in the configuration basis at every step does not disturb the state, and the measured record reproduces the law.
- **$Q_{\mathrm{fb}}\Rightarrow S$.** This is the Born rule: the record of a finite projectively measured experiment is a probability law.

*Attribution.*
- The trajectory-labelling realization is the construction of Egri et al. [EG, Prop. 13], packaged as one iterated bijection. The independent-prior form is their Prop. 16, without reversibility [EG]. Its Markov one-step case is the random-mapping representation [LPW, Prop. 1.5].
- That a permutation dynamics is a special case of a unistochastic process is stated by Barandes [B25, p. 12; B23 §4.3; B26 §4].
- The every-step projectively measured record as a probability law appears in Strasberg and García Díaz [SGD, Eq. (3)]. That work, like Milz et al. [Milz20], studies a different question: whether such records are consistent with omitting intermediate measurements.
- A packaged statement of the three-way multi-time identification was not located in the literature read for this paper. The quantum-comb realization literature was not read.

### 2.3 Scope of the correspondence

Theorem 1 is a representation equivalence. Three consequences fix its scope.

- **Universality.** Markov laws lie in all three classes. So neither the existence of a finite reversible realization nor the existence of a fixed-basis unitary Born representation distinguishes a law with memory from one without. The form "a law is non-Markovian if and only if a finite reversible realization exists" is false, since the realization of Theorem 1 exists for Markov laws as well [Main §3.4, Remark on diagnostics].
- **The Born dictionary.** The relation $p=|U|^2$ is part of the definition of $Q_{\mathrm{fb}}$. It is not an output of the correspondence. The unitaries the construction supplies are permutations, with entries 0 and 1, so the recovered table is the same for $|U|^p$ at every $p>0$. The construction does not select the quadratic exponent [Main §3.4; B26 Thm 3.1 for the trace form of an arbitrary stochastic matrix].
- **Finite horizon.** A bijection of a finite set has finite order $L$, so one fixed realization with one fixed prior has an $L$-periodic multi-time law. A nonperiodic law has no exact all-time realization by one fixed finite substratum. The correspondence is per horizon [Main §3.4, Remark on consolidation].

### 2.4 Where the memory lives

Write $M_t := I(X_{<t};X_{t+1}\mid X_t)$ for the conditional memory of a law at time $t$. In a realization, write $f_x(h)=\pi_V(\varphi(x,h))$ for the next visible state, and $\mu_p$ for the hidden posterior after a visible history $p$ ending at $x$.

**Theorem 2** (unavoidable hidden predictive memory [Main §3.4]). *In every faithful deterministic realization:*
- *(a) the next-step law is $P(X_{t+1}\mid p,x)=(f_x)_\#\mu_p$;*
- *(b) for histories $p,p'$ sharing the endpoint $x$, $\|P(X_{t+1}\mid p,x)-P(X_{t+1}\mid p',x)\|_{\mathrm{TV}}\le\|\mu_p-\mu_{p'}\|_{\mathrm{TV}}$;*
- *(c) $M_t\le I(X_{<t};H_t\mid X_t)\le\log_2|\mathcal C_H|$.*

Kernel: `pushforward_identity`, `distinguishability_floor`, `capacity_floor` and `unavoidable_hidden_predictive_memory` (`HiddenMemory.lean:83, 114, 170, 185`). These are proved for a joint law of history, present visible state and hidden state. The reading of a realization's time-$t$ law as that joint law is not formalized.

The proof is the data-processing inequality applied to $X_{t+1}=f(X_t,H_t)$. The theorem is the precise sense in which a deterministic completion must carry the visible memory [CT, data-processing inequality].

Theorem 2 yields a biconditional, stated here in prose because one of its links is not formalized. $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards:
- **Forward:** apply (a) in each realization.
- **Converse:** apply (a) in one realization, which exists by `S_imp_D`.

Both directions use the vanishing criterion for conditional mutual information, which is not formalized [Main §1.5, §3.4 Summary (2)].

Two further bounds tie memory to the hidden sector:
- **Capacity.** Any realization of a law whose conditional past–future information reaches $I^*$ needs $|\mathcal C_H|\ge 2^{I^*}$ (`c3_necessity`, `card_hidden_ge_two_pow_Istar`, `C3Necessity.lean:80, 117`).
- **Readback.** If two visible histories of length $k$ with a common endpoint, each of probability at least $p_0$, induce next-step laws at total-variation distance at least $\delta$, then $I(X_{<k};X_{k+1}\mid X_k)\ge p_0\delta^2/\ln 2$ [Main §2.3]. This follows from Pinsker's inequality [CT]. It is proved in prose and checked by exact probes.

**Conditions as diagnostics.** Main names four conditions on a hidden sector [Main §1.3]:
- (C1) the hidden state influences some visible transition;
- (C2) a stored record persists until it is read;
- (C3) the capacity bound;
- (C4) history readback: two histories with the same present induce different next-step laws.

In a faithful realization, (C4) coincides with $M_t>0$. (C1) and (C3) follow from it. (C2) is a physical-regime premise outside the equivalence. The four conditions are therefore diagnostics of a realization, not hypotheses of Theorem 1.

The per-horizon characterization of [Main §3.4] reads: a law has accessible memory if and only if, for some accessible order $k$ and every finite horizon $K\ge k+1$, it has a deterministic realization with (C1), (C3) and (C4) at $k$. Both directions are proved in prose: one is the readback bound, the other the process dilation. Given that (C4) coincides with memory, the characterization adds to the memory statement only the existence of a realization.

***

## 3. Physical interpretation: quantum-like behaviour from restricted observation

### 3.1 Recurrence and indivisibility

Write $\Gamma_t$ for the rooted visible transition matrix from time 0 to time $t$ (row-stochastic, rows indexed by $x_0$). The family is *P-divisible* if for all $s<t$ there is a stochastic $\Lambda$ with $\Gamma_t=\Gamma_s\Lambda$.

A stochastic divisor contracts total variation. So under P-divisibility the distance $\|\delta_a\Gamma_t-\delta_b\Gamma_t\|_{\mathrm{TV}}$ cannot increase. This "only if" direction is the classical divisibility criterion of Rivas, Huelga and Plenio [RHP14, Thm 2.4]. It is also the data-processing direction of Buscemi and Datta [BD, Prop. 1].

**Theorem 3** (recurrence and overlap [Main §2.3]). *Let $\varphi$ be a bijection of the finite set $\mathcal C_V\times\mathcal C_H$. Suppose that at some time $s$ two rows of $\Gamma_s$ overlap in a column, and that $\Gamma_n=I$ at some $n>s$. Then the rooted family is P-indivisible within $n$.*

Finite order gives $\varphi^N=\mathrm{id}$ for some $N$, so $\Gamma_N=I$. A non-permutation one-step matrix has two overlapping rows. The distance then drops below 1 at time $s$ and returns to 1 at time $n$, which no stochastic divisor permits. The rooted form is proved in the kernel as `pIndivisible_of_rooted_identity_return_of_overlap` (`RecurrenceHorizon.lean:148`). The mechanism is known [RHP14; BD]. Doukas states the same argument concurrently [DO, Prop. 1]. Monotone total variation is necessary for P-divisibility, not sufficient: stochastic pairs exist with no stochastic divisor and monotone distance [Main §2.3].

A stochastic matrix with a stochastic one-sided inverse is a permutation matrix (`isPermMatrix_of_stochastic_inverse`, `EquivalenceChain.lean:110`; [BB, Problem 23]). On a fixed finite reversible representative, (C4) therefore forces indivisibility somewhere in the recurrence cycle [Main §2.3]. The argument runs in three steps:
1. If every rooted map before the recurrence time $L$ were a permutation, the present visible state would determine the initial one. Then no two histories with a common endpoint could differ in their next-step laws, which contradicts (C4).
2. So some $\Gamma_k$ is not a permutation.
3. Divisibility from $k$ to $L$, where $\Gamma_L=I$, would require a stochastic inverse of $\Gamma_k$, and the inverse lemma rules that out.

The kernel proves the conclusion from a routed-readback witness (`routed_forces_indivisible_somewhere`, `PhysicalC4Discharge.lean:122`). Step 1, from history-level (C4) to a non-permutation rooted map, is proved in prose.

### 3.2 What the indivisibility is, and what it is not

The result is global. It holds somewhere in the recurrence cycle, not on every accessible window. Conditional memory does not force short-window indivisibility; the XOR family of §4.2 has one bit of memory and a P-divisible matrix family.

Three notions are kept apart [Main §3.2, Remark on three notions]:
1. accessible finite-horizon memory, $M_t>0$;
2. stochastic P-indivisibility of the visible population law;
3. quantum non-Markovianity under a chosen divisibility or backflow criterion.

No unconditional implication among them holds.
- **Inside the framework's channels.** Notion 2 constrains a quantum intermediate map only inside the diagonal-preserving class. The channels obtained by tracing out a permutation unitary from a diagonal hidden state are in that class. For them P-indivisibility implies CP-indivisibility: no completely positive trace-preserving intermediate map exists [Main §3.2, Theorem on CP-indivisibility].
- **Outside that class.** The family $\Phi_{t_1}=\mathrm{Ad}_{\mathrm{Hadamard}}$, $\Phi_{t_2}=\mathrm{id}$ is CP-divisible, while its computational-basis populations $\tfrac12 J\to I$ are P-indivisible [Main §3.2, Remark].
- **Witnesses.** Backflow of distinguishability witnesses divisibility failure in one direction only [BLP]. For bijective dynamical maps, CP-divisibility is equivalent to monotone distinguishability with a $(d+1)$-dimensional ancilla [BJA].

The physical reading of these results is a representation result, not an explanation. The correspondence states which laws admit realizations and quantum representations. It does not state why a given physical system exhibits a law with memory; that burden lies with a specific physical realization [Main §3.4, Remark on representation and explanation].

***

## 4. Illustrative examples

### 4.1 A minimal model

Let $\mathcal C_V=\{0,1\}$, $\mathcal C_H=\{1,\dots,6\}$, and let $\varphi$ be the product of the disjoint transpositions [Main §2.4]
$$
(0,1\leftrightarrow1,1)(0,2\leftrightarrow1,2)(0,3\leftrightarrow0,4)(0,5\leftrightarrow0,6)(1,3\leftrightarrow1,4)(1,5\leftrightarrow1,6).
$$

With the hidden state uniform:
$$
\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\qquad \Gamma_2=I,\qquad
\Gamma_1^{-1}\Gamma_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$
The only candidate divisor has negative entries, so the family is P-indivisible. A Markov chain with the same one-step matrix would give $\Gamma_1^2$, with entries $5/9$ and $4/9$.

With $x_0$ uniform and independent of the hidden state, $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$ while $P(x_2{=}0\mid x_1{=}1)=1/3$. For $P(x_0{=}0)=a$, the second value is $a/(2-a)$.

Hidden states $h\in\{1,2\}$ flip $x$ and keep $h$, so after one step they hold the record "the visible bit was flipped". The second application of $\varphi$ reads that record and flips $x$ back.

### 4.2 Memory without short-window indivisibility

Let $X_0$ and $X_1$ be independent uniform bits and $X_2=X_0\oplus X_1$. Every two-time transition matrix is $\tfrac12 J$, so the matrix family factors through $\Lambda=I$ and is P-divisible. Yet $I(X_0;X_2\mid X_1)=1$ bit. Up to flipping the final bit, this is the process of Rivas, Huelga and Plenio [RHP14, Eq. (15)]. It appears concurrently in Doukas [DO, App. A] and in the probes of [Main §3.4, Remark on two notions of memory].

### 4.3 The card table

The two-card game of [Book §1.11] realizes the smallest case of Theorem 3. Its rules are fixed as follows:

- **Cards.** A hole card $h$, visible, and a burn card $b$, face down. Each is red or black. The burn card is uniform and independent of the hole card.
- **Shuffle.** Between streets the two cards trade places, $\varphi(h,b)=(b,h)$.
- **Peek.** The hole card is revealed, and the burn card, which holds the record, is overwritten by a fresh card drawn uniformly and independently.

The odds that the hole card at showdown matches the hole card as dealt are, by exact enumeration:

| protocol | odds |
|---|---|
| one shuffle | 1/2 |
| two shuffles | 1 |
| two shuffles, odds chained through the unobserved middle street ($\Gamma_1^2$) | 1/2 |
| two shuffles, with a peek in the middle | 1/2 |

Here $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$. Since $\Gamma_1\Lambda=\tfrac12J$ for every stochastic $\Lambda$, the family is P-indivisible.

The last line depends on the peek rule. If the peek only reveals, or replaces the hole card while leaving the burn card, the odds are 1: the 1/2 comes from overwriting the record, not from looking. With anticorrelated cards ($b=1-h$), $\Gamma_1$ is a permutation and the game is divisible.

On configuration (card) inputs the game is a classical stochastic process, and its P-indivisibility is the population notion (2) of [Main §3.2]. Under the permutation-unitary embedding of §2.2, the one-step channel is the constant, entanglement-breaking channel [Main §3.2, Remark on the failure of (C1)]. The two-step map, however, is the identity channel, so the family is CP-indivisible [Main §3.2, Theorem on CP-indivisibility]. With the hidden slot initialized to a fixed card instead, the same swap admits no classical-memory decomposition [Main §4.5]. With the uniform burn card used here, the one-step map is the Pauli twirl, and the identity decomposes through it: record which Pauli was applied, then undo it. A card arrangement violates no Bell inequality [Book §1.11; Main §3.3].

***

## 5. Black-hole information: a bounded application

The black-hole information problem asks whether the radiation from an evaporating black hole carries the information of what formed it [Hawking76; Page93; Page13]. Under OI, two questions separate. One is whether information is conserved in the global reversible dynamics. The other is whether it can be recovered from the records an observer can access.

The results below are finite computations, with written proofs, in toy access models: classical messages written into configurations, and records that are configuration reads of a permutation. Each was checked exhaustively at small size and passed an independent internal review [BH-01; BH-02]. They concern the framework's nested-partition construction [GR App. A; Book §7.6], not the physics of a particular black hole.

### 5.1 Conservation and access

**Setting.** The configuration space is the nested partition $\mathcal C_V\times\mathcal C_B\times\mathcal C_D$, with $V$ the exterior visible region, $B$ the black-hole interior and $D$ the trans-cosmological sector [GR App. A.1]. Radiation is emitted from $B$ into $V$.

**Conservation.** A bijection loses no information about the global state. This is the content that bijectivity carries.

<!-- OWNER: R11. Claim A below contradicts live text at ch07:110 / FULL:1987 ("resolves the paradox … because φ is bijective"); the falsification framing at ch07:159–161 / FULL:2036–2038 is unfalsifiable as stated. The paper must not land until the owner corrects those sites or drops this paragraph. -->
**Access.** Bijectivity of the global map neither implies recovery from the accessible records nor is necessary for it [BH-01, claim A]. Let $K$ be the set of joint values of the registers left unread at the end, and $M$ the message set.

- **Without recovery.** Among all 40,320 bijections of $\{0,1\}^3$, 1,376 give zero accessible advantage for a binary message with one register unread after two emissions.
- **Recovery without bijectivity.** Sixty non-injective maps of $\{0,1\}^2$ recover a message exactly under complete access.
- **Sufficient conditions.** Bijective dynamics with complete endpoint access gives exact recovery. If a set $K$ of endpoint values is inaccessible, the success probability satisfies $P_{\mathrm{succ}}\ge1/|K|$.
- **Necessary side.** The bound is the one necessary-side fact proved. In a bijective instance, zero advantage requires $|K|\ge|M|$, while 32 non-injective maps of $\{0,1\}^2$ violate the bound.
- **Status of the conditions.** They are sufficient, not necessary. The package describes the remnant bound as the remnant-capacity form of a known fact, and its linear case as the secret-sharing threshold [BH-01].
- **Nested traces.** The direct and sequential nested trace-outs of [GR App. A.2] agree for every map, as a Fubini identity. Their consistency carries no recovery content [BH-01, claim E].

<!-- OWNER: R11. The decoupling finding below contradicts GR:811 ("D is frozen on evaporation timescales"). -->
**Decoupling of the trans-cosmological sector.** [GR App. A.7, Theorem A.7] treats $D$ as decoupled over the evaporation on the stated ground $\tau_{\mathrm{evap}}\ll\tau_B^D$, with $\tau_B^D\sim H^{-1}$. Exact interval arithmetic reverses that ground. At 30 solar masses, $t_{\mathrm{evap}}/\tau_B^D\ge1.785\times10^{57}$, and $t_P/\tau_B^D\ge1.153\times10^{57}$ with $t_P$ the Page time at $\beta=1$ [BH-01, item F]. The intervals for the greybody factor and $\tau_B^D$ were fixed after the plan; the margin makes the conclusion insensitive to them.

The finding has three limits:
- it does not show that information reaches $D$;
- it does not show that Theorem A.7 of [GR] fails within $t\ll\tau_B^D$;
- it does not exclude other decoupling arguments.

### 5.2 Where the Page entropy comes from

A permutation unitary maps configuration basis states to configuration basis states. Starting from a configuration, every state on the orbit is a product state across any configuration-aligned cut, with entanglement entropy exactly zero. From any initial state, the entanglement entropy across such a cut is bounded by the Shannon entropy $H(p_0)$ of the initial configuration distribution, and the overlap with $|{+}\rangle^{\otimes n}$ is conserved [BH-02, C1–C2].

<!-- OWNER: R11. The following paragraph contradicts live text at ch07:126 sentence 1 / FULL:2003 and GR:869 ("invokes only Popescu-Short-Winter … no ergodicity assumption"). -->
The framework's Page-curve argument [GR App. A.7, Theorems A.8–A.9] assumes the scrambling condition H-scramble: equidistribution of the orbit over pure states on an energy shell [GR App. A.7]. In the setting that argument uses (a definite initial configuration, with bipartitions aligned to configurations), H-scramble fails for every bijection, by the result above. The Page value enters the argument only through the Haar ensemble that H-scramble posits, not through bijectivity or the cycle decomposition [BH-02, C6(a)–(b)]. A dynamics satisfying H-scramble would produce the Page value through Popescu–Short–Winter typicality [PSW; Page93]. Whether the substratum supplies such a condition is open.

### 5.3 The Page time

Assume three things:
1. the mass-loss law $dM/dt=-\alpha/M^2$ with constant $\alpha$;
2. $S_{\mathrm{BH}}\propto M^2$;
3. a constant ratio $\beta$ of the radiation's coarse-grained entropy gain to the black-hole entropy lost.

Then the turnover falls at
$$
t_P/t_{\mathrm{evap}}=1-\bigl(\beta/(1+\beta)\bigr)^{3/2}.
$$
This is Page's result [Page13, Eq. (8)].

- **Values.** It gives $0.646$ at $\beta=1$, the value of mode-for-mode counting. It gives about $0.538$ at Page's $\beta\approx1.485$ for photons and gravitons [Page13]. In the quasi-stationary semiclassical regime $\beta>1$ [Page05, Eqs. (5)–(10)].
- **Robustness.** A constant multiplicative greybody or species factor cancels.
- **Sensitivity.** A mass-dependent coefficient moves the fraction: to $0.7027$ for $\alpha\propto M^{-1/2}$, and up to $0.8707$ in a two-step threshold model [BH-02, C7].

The fraction is therefore conditional on all three inputs.

### 5.4 Open steps

Five steps remain open:
- whether H-scramble, or any substitute, holds for the substratum;
- the step from the cycle time average of [GR, Theorem A.8] to the pointwise curve of [GR, Theorem A.9], along one trajectory with a moving bipartition [BH-02, C6(d)];
- the generalized second law [GR App. A.6];
- agreement with quantum-extremal-surface computations on the Page time, which requires matched radiation-entropy accounting [Pen19];
- the conjectured correspondence between islands and substratum cycles [Book §7.6].

***

## 6. Limitations and open problems

### 6.1 Why exact operational quantum mechanics is not established

Theorem 1 concerns fixed-basis observable statistics. Operational quantum mechanics also requires two further things:
- coherent preparations, noncommuting interventions and composites;
- that all of these be represented simultaneously by one standard instrument theory.

On a fixed finite carrier this requirement is characterized exactly [GR §3.3]. Fix a nonempty finite visible system and an operational theory on it, specifying which finite outcome families of linear maps are available on the system and at every ancilla level. Five conditions are in play:
- (i) valid probabilities;
- (ii) trivial-ancilla consistency;
- (iii) inert spectators;
- (iv) full reversible control;
- (v) iterated composition.

**Theorem 4** (operational-completion characterization [GR §3.3]). *For every nonempty finite system, the available outcome families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments*
$$
\iff\quad \text{conditions (i)–(v) hold.}
$$

The two directions have separate kernel witnesses:
- $\Rightarrow$: `physical_of_exactAll` (`PhysicalCharacterization.lean:301`).
- $\Leftarrow$: `exactAll_of_physical_general` (`GeneralCarrier.lean:93`), through three lemmas:
  - `krausSoundExt_of_validity_inert` (`OperationalValidity.lean:124`);
  - `compositeCompleteness_unconditional` (`IsometryExtension.lean:179`), whose extension premise is discharged by `finiteIsometryExtensionSF_discharged`;
  - `exactAll_of_levelOne` (`LevelOneSeam.lean:196`).

The equivalence is assembled in `exactAll_iff_physical_general` (`GeneralCarrier.lean:100`). The theorem is carrier-general.

On the qubit, each condition is independent of the other four and of a sealed finite C1–C4 observation process: for each condition there is a qubit theory that realizes the process and the other four conditions and fails that one (`five_way_minimality`, `RankGapTheory.lean:702`). In particular, a qubit theory that never creates coherence realizes the observation process and is not quantum (`oi_alone_not_qm`, `GeneralCarrier.lean:160`). So bare finite OI does not imply quantum mechanics. Which of (iii)–(v) a physical substratum supplies is open [GR §3.3].

### 6.2 The evolution relating two times is not selected

Representability fixes which laws admit a fixed-basis unitary representation. It does not fix the unitary evolution relating two times [Main §3.4, Remark on representability]:
- **Different lifts.** Two coherent unitary lifts of one visible family, related by a time-dependent strong-class element, have different relative candidates (`gl2_strong_gauge_moves_relative_candidate`, `CoherentLiftGauge.lean:537`).
- **Constant deformations.** A constant deformation preserves the relative candidate (`gl3_constant_gauge_preserves_relative`, `:451`). The non-uniqueness is therefore carried by time dependence.
- **The quotient.** The fixed-basis correspondence acts on the quotient by visible equality. Fixed-basis data built from a lift have trajectory laws determined by the visible law alone, and two such data have equal trajectory laws exactly when their visible laws are equal (`bridge_traj`, `rooted_eq_iff_slice_eq`, `realData_traj_stochastic`, `TrackBQfbBridge.lean:276, 180, 286`).

A selection condition beyond visible-law representability and ordinary coherence would be needed. None is supplied here.

### 6.3 No fixed finite carrier reproduces a qubit

A fixed finite realization with $N$ ontic configurations generates only behaviour matrices that factor nonnegatively through $N$ states. Qubit prepare-and-measure behaviours have nonnegative rank unbounded over finite experiments [HKLP]. So no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly [Main §3.4, Proposition on the finite-substratum obstruction]. This is a form of Hardy's finite-ontic-state no-go [Hardy04; GH; MO]. It does not touch Theorem 1, where the realization is chosen per finite-horizon law.

Main also states finite-accuracy realization and gluing theorems for bounded quantum instrument families [Main §3.4]. They are realization theorems, not uniqueness theorems: the same reversible machinery realizes non-quantum instrument families. No conclusion here rests on them.

### 6.4 Open problems

1. **The operational-lifting layer.** Which of (iii)–(v) a physical substratum supplies [GR §3.3].
2. **Selection of the relating evolution** (§6.2).
3. **The origin of the quadratic Born exponent** (§2.3).
4. **Formalization of four steps:**
   - the step from history-level (C4) to a non-permutation rooted map;
   - the reading of a realization's time-$t$ law as the joint law of Theorem 2;
   - the vanishing criterion for conditional mutual information;
   - independence of the hidden prior in the process dilation.

   The per-horizon characterization of §2.4 is likewise proved only in prose.
5. **Minimal hidden memory.** Whether the minimal hidden predictive memory equals $M_t$ once inert ledger bits are quotiented. The fixed-dimension form is false [Main §3.4, Remark on a variational identity].
6. **Recurrence.** Exact gluing for recurrent target families, and approximation on windows short compared with the recurrence time [Main §3.4].
7. **The (C2) necessity statement.** It is conditional on a hidden-sector mixing hypothesis, motivated by eigenstate thermalization [Main §3.4].
8. **Bell correlations.** A deterministic completion that keeps pointwise causal cones and a setting-independent pre-setting ensemble is Bell-local, so $|S_{\mathrm{CHSH}}|\le2$ [Bell64; CHSH69; Main §3.3]. The framework's adopted branch, ontic parameter dependence with operational no-signaling, rests on the open hypothesis H-Bell [Main §3.3].
9. **Testability.** No ontology-level falsifier is established. The framework's premises are collected in a posit ledger of twelve items [Main §4.5].
10. **The black-hole steps** of §5.4.

### 6.5 What is not claimed

1. **No derivation of quantum mechanics.** Theorem 1 is a representation equivalence containing every finite law, Markov laws included. The Born dictionary is part of the definition of $Q_{\mathrm{fb}}$, and its exponent is not selected.
2. **No unique selection of the operational theory.**
   - Exact finite operational quantum mechanics follows only under conditions (i)–(v), which bare finite OI does not imply.
   - Their independence is shown on the qubit, against one sealed observation process.
   - The visible law does not fix the relating evolution.
3. **No characterization of memory by the existence of a realization** (§2.3).
4. **No identification of stochastic P-indivisibility with quantum non-Markovianity**, and no claim that memory forces indivisibility on short windows (§3.2).
5. **No resolution of the black-hole information problem.**
   - The Page curve follows only under H-scramble.
   - The Page-time fraction is conditional on its three inputs.
   - The correspondence with islands is conjectural.
   - The generalized second law is open.
   - The stated support for decoupling the trans-cosmological sector is reversed.
   - The black-hole computations are finite toy models.
6. **No claim that the physical hypothesis of §1.1 is established or tested.**

***

## 7. Related work

**The stochastic–quantum correspondence.** Barandes embeds finite-configuration stochastic processes into unitarily evolving systems [B23; B25]. He gives the Born representation and unistochastic theorems [B26]; the one-step $n^2$-dimensional ancilla dilation used in [Main §3.1] is B26's construction (Thm 3.3).

**Realizations of stochastic laws.** Egri et al. relate trajectories of probabilities to probabilities on trajectories, and realize stochastic dynamics by deterministic maps with an ancilla [EG].

**Divisibility and memory.**
- Doukas studies the emergence of quantum mechanics from stochastic processes, including divisibility and the XOR process, concurrently with this work [DO].
- The classical divisibility criterion and the XOR example are in Rivas, Huelga and Plenio [RHP14]. The information-theoretic equivalence for general ensembles is Buscemi and Datta's [BD].
- Backflow witnesses are due to Breuer, Laine and Piilo [BLP], with the ancilla-assisted forms of Rivas, Huelga and Plenio [RHP10] and of Bylicka, Johansson and Acín [BJA].
- Strasberg and García Díaz [SGD] and Milz et al. [Milz20] study when every-step projective records are consistent with omitting measurements. The fixed-basis class $Q_{\mathrm{fb}}$ measures at every step and does not meet that question.

**Finite ontic models.** Finite ontic models of a qubit are bounded by Hardy [Hardy04], Galvão and Hardy [GH], Montina [MO] and Heinosaari et al. [HKLP].

**Black holes.** The Page-curve inputs are Page's [Page93; Page05; Page13]. The quantum-extremal-surface route is Penington's [Pen19].

***

## 8. Conclusion

At finite observable horizon, the laws an embedded observer of a finite reversible system can record are exactly the finite stochastic laws. They are also exactly the fixed-basis unitary Born laws. The representation is universal, so the discriminating content lies in memory:
- every deterministic completion carries the visible memory in its hidden state;
- finite recurrence turns history readback into stochastic indivisibility within the recurrence cycle.

Exact operational quantum mechanics is reached only under completion conditions that bare finite OI does not imply. The evolution relating two times is not selected by representability.

Applied to black-hole information, the same viewpoint separates conservation from access. Bijectivity conserves the global state but does not determine what an access class recovers. In the framework's Page-curve argument, the Page entropy enters through a scrambling hypothesis and not through bijectivity.

***

## Code, data and formal verification

<!-- OWNER: retention §A.42. The Lean-check sentence below is an enduring certification claim. Before the paper lands, an expected result for commit 687e885b (build success, release-gate verdict, each cited declaration's #print axioms set, recipe, provenance) is retained beside the paper, or the commit is shown to fall inside an archive covered by the evidence-retention step. Placeholder: [expected-result file path]. The owner chooses only the wording ("machine-checked" or the form below). -->
The declarations cited in this paper and listed in Appendix A were checked in Lean 4/Mathlib [Lean4; Mathlib] at commit `687e885b1cfd24d6f17eee439101afc8acf07015` of the repository, by the recipe `python3 tools/lean_axiom_check.py --require-lake`. That recipe builds `verification/lean-mathlib` with `lake build` and requires every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`. The expected result is [expected-result file path].

Steps stated as proved in prose are not covered by that check. The exact probes cited from [Main] are in `papers/oi_lattice_code/foundations/`. The black-hole computations and their reviews are in `verification/programmes/black-hole-information/` [BH-01; BH-02].

The repository is at <https://github.com/amaybaum/incompleteness> (MIT License), archived under concept DOI 10.5281/zenodo.19060318.

***

## Appendix A. Kernel map

Module paths are relative to `verification/lean-mathlib/OIBridge/`, with line numbers at commit `687e885b`. "Main ledger" refers to the status ledger of [Main §4.5].

| Result (section) | Declaration(s) | Status, and steps not formalized |
|---|---|---|
| Theorem 1 (§2.2) | `finite_horizon_equivalence` (Equivalence:462) | Proved, six directions; the compositions at :466–468 |
| $S\Rightarrow D$ (§2.2) | `S_imp_D` (Equivalence:422) | Proved for an initial law that may correlate the coordinates. Prior independence is not formalized; Main ledger (ii)⇒(iii) |
| $D\Rightarrow Q_{\mathrm{fb}}$ (§2.2) | `D_imp_Qfb` (Equivalence:294); `permMatrix_mem_unitaryGroup` (EquivalenceChain:179); `isDiag_Phi` (EquivalenceChain:253) | Proved; Main ledger fixed-$\hat H$ row (uncompressed form) |
| $Q_{\mathrm{fb}}\Rightarrow S$ (§2.2) | `Qfb_imp_S` (Equivalence:245) | Proved |
| Prior as datum (§2.1) | `invariance_does_not_select` (CanonicalMeasure:242) | Proved |
| Theorem 2(a) (§2.4) | `pushforward_identity` (HiddenMemory:83) | Proved for the joint law; time-$t$ reading not formalized |
| Theorem 2(b) (§2.4) | `distinguishability_floor` (HiddenMemory:114) | As above |
| Theorem 2(c) (§2.4) | `capacity_floor` (HiddenMemory:170); `unavoidable_hidden_predictive_memory` (HiddenMemory:185) | As above; the CMI vanishing criterion is not formalized |
| Capacity bound (§2.4) | `c3_necessity` (C3Necessity:80); `card_hidden_ge_two_pow_Istar` (C3Necessity:117) | Proved; Main ledger C3 necessity |
| Readback bound (§2.4) | none | Prose proof (Pinsker) with exact probes; Main ledger (iii)⇒(ii) |
| Inverse lemma (§3.1) | `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110) | Proved |
| Theorem 3 (§3.1) | `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148) | Proved in rooted form |
| (C4) ⇒ indivisibility (§3.1) | `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) | Proved from a routed-readback witness; the step from history-level (C4) is prose |
| CP-indivisibility, framework channels (§3.2) | none | Prose proof with exact probes [Main §3.2]; Main ledger CP-indivisibility row |
| Relating evolution (§6.2) | `gl2_strong_gauge_moves_relative_candidate` (CoherentLiftGauge:537); `gl3_constant_gauge_preserves_relative` (CoherentLiftGauge:451); `bridge_traj`, `rooted_eq_iff_slice_eq`, `realData_traj_stochastic` (TrackBQfbBridge:276, :180, :286) | Proved |
| Theorem 4 (§6.1) | `exactAll_iff_physical_general` (GeneralCarrier:100), with $\Rightarrow$ `physical_of_exactAll` (PhysicalCharacterization:301) and $\Leftarrow$ `exactAll_of_physical_general` (GeneralCarrier:93) | Proved, carrier-general |
| Independence; bare OI $\not\Rightarrow$ QM (§6.1) | `five_way_minimality` (RankGapTheory:702); `oi_alone_not_qm` (GeneralCarrier:160) | Proved on the qubit (`Fin 2`) |

***

## References

**Corpus**

[Main] A. Maybaum, "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation," `papers/Main.md`, repository commit `687e885b`; concept DOI 10.5281/zenodo.19060318.

[GR] A. Maybaum, "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon," `papers/GR.md`, repository commit `687e885b`.

[Book] A. Maybaum, *The Incompleteness of Observation*, `book/The-Incompleteness-of-Observation-FULL.md`, repository commit `687e885b`.

[BH-01] "BH-01 access audit, v1," `verification/programmes/black-hole-information/bh01_access_v1/` (report, proofs, exhaustive checks, independent review accepted at `df2ea6f5`), repository commit `687e885b`.

[BH-02] "BH-02/BH-04: permutation dynamics versus quantum scrambling; Page-time fraction," `verification/programmes/black-hole-information/bh02_scramble_v1/` (independent review accepted at `ce7937d2`), repository commit `687e885b`.

**External**

[B23] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085v2 (2026).

[B25] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025), doi:10.31389/pop.186; arXiv:2302.10778v3.

[B26] J. A. Barandes, "The Born Representation Theorem and the Unistochastic Theorem," arXiv:2608.04354v1 (2026).

[BB] J. C. Baez and J. Biamonte, "Quantum Techniques for Stochastic Mechanics," arXiv:1209.3632v5. <!-- VERIFY: first-name initials and book venue from memory; arXiv id and title per the correspondence literature study §5.7 -->

[BD] F. Buscemi and N. Datta, "Equivalence between divisibility and monotonic decrease of information in classical and quantum stochastic processes," *Phys. Rev. A* **93**, 012101 (2016); arXiv:1408.7062v3.

[Bell64] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics* **1**, 195–200 (1964). <!-- VERIFY: from memory -->

[BJA] B. Bylicka, M. Johansson, and A. Acín, "Constructive method for detecting the information backflow of non-Markovian dynamics," *Phys. Rev. Lett.* **118**, 120501 (2017); arXiv:1603.04288v2.

[BLP] H.-P. Breuer, E.-M. Laine, and J. Piilo, "Measure for the degree of non-Markovian behavior of quantum processes in open systems," *Phys. Rev. Lett.* **103**, 210401 (2009); arXiv:0908.0238v2.

[CHSH69] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, "Proposed experiment to test local hidden-variable theories," *Phys. Rev. Lett.* **23**, 880–884 (1969). <!-- VERIFY: from memory -->

[CT] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006). <!-- VERIFY: from memory; not read in the audits (AUDIT r4 §5 P3.3) -->

[DO] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095v3 (2026).

[EG] Egri, Gömöri, Gyenis, and Hofer-Szabó, "Trajectory of Probabilities, Probability on Trajectories, and the Stochastic-Quantum Correspondence," arXiv:2602.23491v1 (2026). <!-- VERIFY: authors' initials not recorded in the literature study -->

[GH] E. F. Galvão and L. Hardy, "Substituting a qubit for an arbitrarily large number of classical bits," arXiv:quant-ph/0110166v3. <!-- VERIFY: first-name initials from memory -->

[Hardy04] L. Hardy, *Stud. Hist. Philos. Mod. Phys.* **35**, 267 (2004). <!-- VERIFY: title and content not read (AUDIT r4 C14, P3.2) -->

[Hawking76] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460–2473 (1976). <!-- VERIFY: entry taken from Main's bibliography [43]; not read in the audits -->

[HKLP] T. Heinosaari, O. Kerppo, L. Leppäjärvi, and M. Plávala, "Simple information processing tasks with unbounded quantum advantage," *Phys. Rev. A* **109**, 032627 (2024); arXiv:2308.07727. <!-- VERIFY: entry taken from Main's bibliography [55]; content not read (AUDIT r4 C14) -->

[Lean4] L. de Moura and S. Ullrich, "The Lean 4 theorem prover and programming language," in *Automated Deduction – CADE 28* (Springer, 2021). <!-- VERIFY: from memory -->

[LPW] D. A. Levin, Y. Peres, and E. L. Wilmer, *Markov Chains and Mixing Times*, 2nd ed. (American Mathematical Society, 2017). <!-- VERIFY: publisher and year from memory; Prop. 1.5 per the correspondence literature study -->

[Mathlib] The mathlib Community, "The Lean mathematical library," in *Proceedings of CPP 2020* (ACM, 2020). <!-- VERIFY: from memory -->

[Milz20] S. Milz, D. Egloff, P. Taranto, T. Theurer, M. B. Plenio, A. Smirne, and S. F. Huelga, "When is a non-Markovian quantum process classical?," *Phys. Rev. X* **10**, 041049 (2020); arXiv:1907.05807v3. <!-- VERIFY: first-name initials from memory; journal per Crossref record (AUDIT r4 C3) -->

[MO] A. Montina, "Exponential complexity and ontological theories of quantum mechanics," arXiv:0711.4770v2. <!-- VERIFY: first-name initial from memory -->

[Page93] D. N. Page, "Average entropy of a subsystem," *Phys. Rev. Lett.* **71**, 1291 (1993); arXiv:gr-qc/9305007.

[Page05] D. N. Page, "Hawking radiation and black hole thermodynamics," *New J. Phys.* **7**, 203 (2005); arXiv:hep-th/0409024.

[Page13] D. N. Page, "Time dependence of Hawking radiation entropy," *JCAP* **09** (2013) 028; arXiv:1301.4995.

[Pen19] G. Penington, "Entanglement wedge reconstruction and the information paradox," arXiv:1905.08255. <!-- VERIFY: title from memory; arXiv id per the black-hole literature study §4.1 -->

[PSW] S. Popescu, A. J. Short, and A. Winter, "Entanglement and the foundations of statistical mechanics," *Nature Physics* **2**, 754–758 (2006). <!-- VERIFY: entry taken from GR's bibliography [29]; not read in the audits -->

[RHP10] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Entanglement and non-Markovianity of quantum evolutions," *Phys. Rev. Lett.* **105**, 050403 (2010); arXiv:0911.4270v2.

[RHP14] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014); arXiv:1405.0303v2.

[SGD] P. Strasberg and M. García Díaz, "Classical quantum stochastic processes," *Phys. Rev. A* **100**, 022120 (2019); arXiv:1905.03018v2. <!-- VERIFY: first-name initials from memory -->
