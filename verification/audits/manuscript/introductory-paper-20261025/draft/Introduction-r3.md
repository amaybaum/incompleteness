# Observational Incompleteness: From Deterministic Dynamics to Quantum Observations

**Author:** Alex Maybaum  
**Date:** October 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

***

## Abstract

Observational incompleteness (OI) is the hypothesis that every physical observer is a proper part of a finite reversible deterministic system and records only the visible marginals of its dynamics. At every finite horizon, three classes of law on visible trajectories coincide: all finite stochastic laws, the visible marginals of finite reversible dynamics, and the fixed-basis Born records of finite unitary systems. The components of this correspondence are known, from the trajectory-labelling realization of Egri et al. and Barandes's treatment of permutation dynamics as unistochastic processes; it is stated here as one theorem. Each class contains the Markov laws, so neither a reversible realization nor a quantum representation distinguishes a law with memory from one without, and the Born exponent is not selected. The discriminating content concerns memory: every deterministic completion carries the visible memory in its hidden state, and on a fixed finite reversible system finite recurrence turns history readback into stochastic indivisibility somewhere in the recurrence cycle (each with one step not machine-checked). Exact finite operational quantum mechanics is characterized by five completion conditions, none implied by OI alone. Open are which of these a physical substratum supplies, the selection of the evolution relating two times, and any test of the hypothesis. In a bounded application to black-hole information, finite toy computations separate conservation under bijective dynamics from recovery by an observer with restricted access, and show that in the framework's Page-curve argument the Page entropy enters through a scrambling hypothesis rather than through bijectivity.

<!-- OWNER: R11. The abstract's black-hole sentence restates §5.1 claim A and §5.2's H-scramble finding; it stands or falls with those paragraphs. -->

***

## 1. The central idea

### 1.1 Embedded observation

Embedded observation is modelled by a triple $(S,\varphi,V)$ [Main §1.2]: a finite total system $S=\mathcal C_V\times\mathcal C_H$ of observer configurations $\mathcal C_V$ and complement configurations $\mathcal C_H$, a bijection $\varphi$ of $S$, and an observer $V$ that registers $x\in\mathcal C_V$ and not $h\in\mathcal C_H$.

The bijection $\varphi$ is the reversible representative of the hidden dynamics, motivated by observed near-unitarity, and finiteness of all of $S$ is posited [Main §1.2, Remark (status of the early commitments)]. Hidden states compatible with the same $x$ send it to different futures, so the visible sector evolves stochastically although the whole evolves deterministically.

Observational incompleteness (OI) is the physical hypothesis that every physical observer is in this situation. Identifying nature with such a system is a representation choice, motivated empirically; the theorems below are mathematical, and no test of the identification at the level of memory witnesses is established [Main §4.5]. The incompleteness is inaccessibility of the hidden sector, not joint unsharpness of non-commuting observables: it is present for a single fixed readout, and no uncertainty relation constrains fixed-readout visible laws [Main §3.4].

### 1.2 How far an embedded observer can appear quantum

Marginalizing a reversible dynamics over an unobserved register produces stochastic laws, conditional memory, and failures of stochastic divisibility, in which no stochastic intermediate transition map exists (where the candidate intermediate matrix exists, it has negative entries). The stochastic–quantum correspondence relates these features to quantum theory [Bar23; Bar25]. At the level of finite-horizon observable laws the correspondence of §2 (Theorem 1) is exact and universal, so the content lies in where the memory of a law must sit (§2.4) and what finite recurrence does with it (§3). Exact operational quantum mechanics is reached only under conditions that OI alone does not imply (§6). Proofs, the status ledger and the probe code are in [Main], which this paper introduces; gravitational applications are in [GR] and [Book].

**Contributions.** The paper claims no new theorem or physical result; its contribution is expository. This paper brings together a unified presentation of the established mathematical results of OI, an explicit separation of the mathematical correspondence from its physical interpretation, a concise account of their implications and limitations, and a synthesis of the relevant black-hole information discussion within the scope stated in §5. The components of Theorem 1 are known [EGGH26; Bar23; Bar25; Bar26; SGD19]; the paper states them as one theorem with each direction attributed. The memory bounds of §2.4 are forms of the data-processing and Pinsker inequalities. The recurrence argument of §3 combines finite order with the known contraction criterion for divisibility [RHP14; BD16], stated concurrently by Doukas [Dou26]. The results of §6.1–§6.2 are proved in [GR] and [Main].

*Conventions.* "Machine-checked" means checked in Lean 4/Mathlib [dMU21; Mathlib20] at commit `687e885b` by the recipe under "Code, data and formal verification" (declarations in Appendix A); "proved on paper" means a written proof without a machine check; an "exact probe" is an exhaustive computation in exact rational arithmetic at small size. A *faithful realization* of a law is a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$ with an initial law under which the visible trajectory has that law; the finite reversible system $(S,\varphi)$ is the *substratum*.

<!-- OWNER: decision 2 / retention §A.42. "Machine-checked" is the shorthand for the Lean-check claim; the owner chooses the word ("machine-checked" or "checked in Lean 4/Mathlib at commit X by recipe Y"), and an expected result must be retained beside the paper before it lands. -->

***

## 2. Mathematical foundation

This section defines three classes of finite-horizon law, shows that they coincide, and identifies what the coincidence leaves: where a law's memory must sit.

### 2.1 Setting

Fix finite sets $\mathcal C_V$ (with $|\mathcal C_V|\ge2$) and $\mathcal C_H$, a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$, and a horizon $K$. A law is a probability distribution on visible trajectories $(x_0,\dots,x_K)\in\mathcal C_V^{K+1}$.

The visible law of a realization depends on the dynamics, the partition and the initial law; the prior is part of the realization datum, not selected by invariance under $\varphi$, and the counting measure is a maximal-entropy default [Main §1.2, Remark (the measure as a realization datum)].

Three classes of law are compared [Main §3.4]:

- **$\mathsf S_K$**: all probability distributions on $\mathcal C_V^{K+1}$.
- **$\mathsf D_K$**: the visible trajectory laws of a bijection of $\mathcal C_V\times\mathcal C_H$, for some finite $\mathcal C_H$, under an initial law that may correlate the visible and hidden coordinates.
- **$\mathsf Q_K$**: the laws of finite-dimensional unitary systems read out by projective Born measurement in one fixed basis at every step, from an initial state diagonal in that basis, the record being a fixed function of each outcome.

### 2.2 The finite-horizon correspondence

**Theorem 1** (finite-horizon stochastic–reversible–unitary equivalence [Main §3.4]). *For every finite visible alphabet and every finite horizon $K$,*
$$
\mathsf S_K=\mathsf D_K=\mathsf Q_K ,
$$
*so each class is the set of all probability laws on $\mathcal C_V^{K+1}$.*

[Main] writes Theorem 1 as $S\iff D\iff Q_{\mathrm{fb}}$. Theorem 1 is machine-checked as `finite_horizon_equivalence`, with the inclusions $\mathsf S_K\subseteq\mathsf D_K$ (`S_imp_D`), $\mathsf D_K\subseteq\mathsf Q_K$ (`D_imp_Qfb`) and $\mathsf Q_K\subseteq\mathsf S_K$ (`Qfb_imp_S`), and the reverse inclusions as their compositions; no construction enters as a hypothesis.

**Realization.** For $\mathsf S_K\subseteq\mathsf D_K$, the hidden register is a clock and a complete trajectory record. The initial law places a trajectory drawn from the law in the record, and each step advances the clock and emits the next recorded state. The record makes the step injective, and a finite injective map extends to a bijection. A realization whose hidden prior is independent of $x_0$ exists [Main §3.4, Theorem (finite-horizon process dilation)], proved on paper, with exact probes.

**Quantum representation.** For $\mathsf D_K\subseteq\mathsf Q_K$, set $U_\varphi|x,h\rangle=|\varphi(x,h)\rangle$, a permutation unitary. Its Born weights are the indicators of the deterministic step, so measuring the configuration basis at every step does not disturb the state, and the measured record reproduces the law. $\mathsf Q_K\subseteq\mathsf S_K$ is the Born rule.

**Attribution.** The trajectory-labelling realization is that of Egri et al. [EGGH26, Prop. 13], packaged as one iterated bijection; the independent-prior form is their Prop. 16, without reversibility, and its Markov one-step case is the random-mapping representation [LP17, Prop. 1.5]. A permutation dynamics is a special case of a unistochastic process [Bar25, p. 12; Bar23 §4.3; Bar26 §4], and the one-step $n^2$-dimensional ancilla dilation of [Main §3.1] coincides with the constructions of Barandes [Bar26, Thm 3.3] and Schmidt [Sch21, Thm 2]. The every-step projectively measured record as a probability law is in [SGD19, Eq. (3)]; that work and [Milz20] study whether such records are consistent with omitting measurements, a question $\mathsf Q_K$, which measures at every step, does not meet.

Calvo states a proof of the six axioms of textbook quantum mechanics from the single axiom that every physical system evolves according to a generally indivisible stochastic law [Cal26]; Theorem 1 is a correspondence between classes of law and derives no such axioms.

### 2.3 Scope of the correspondence

Markov laws lie in all three classes. So neither a finite reversible realization nor a fixed-basis unitary representation distinguishes a law with memory from one without [Main §3.4, Remark (the conditions are diagnostics, not hypotheses)].

The relation $p=|U|^2$ is part of the definition of $\mathsf Q_K$, not an output. The unitaries supplied are permutations, with entries 0 and 1, so the recovered table is the same for $|U|^p$ at every $p>0$. The quadratic exponent is therefore not selected [Main §3.4; Bar26, Thm 3.1].

A finite bijection has finite order $L$, so one fixed realization has an $L$-periodic multi-time law: the correspondence holds per horizon, and a nonperiodic law has no exact all-time realization by one fixed finite substratum [Main §3.4].

### 2.4 Where the memory lives

Write $M_t := I(X_{<t};X_{t+1}\mid X_t)$ for the conditional memory at time $t$. In a realization, write $f_x(h)=\pi_V(\varphi(x,h))$, with $\pi_V$ the projection onto $\mathcal C_V$, and $\mu_p$ for the hidden posterior after a visible history $p$ ending at $x$.

**Theorem 2** (unavoidable hidden predictive memory [Main §3.4]). *In every faithful realization:*

- *(a) $P(X_{t+1}\mid p,x)=(f_x)_\#\mu_p$;*
- *(b) for histories $p,p'$ ending at $x$, $\|P(X_{t+1}\mid p,x)-P(X_{t+1}\mid p',x)\|_{\mathrm{TV}}\le\|\mu_p-\mu_{p'}\|_{\mathrm{TV}}$;*
- *(c) $M_t\le I(X_{<t};H_t\mid X_t)\le\log_2|\mathcal C_H|$.*

(a)–(c) are machine-checked for a joint law of history, present and hidden state. Their identification with a realization's time-$t$ law is not machine-checked. The proof is the data-processing inequality [CT06] applied to $X_{t+1}=f(X_t,H_t)$.

**Corollary** (proved on paper). $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards. The forward direction applies (a) in each realization, the converse in one realization, which exists by Theorem 1. Both directions use the vanishing criterion for conditional mutual information [Main §1.5].

Two further bounds tie memory to the hidden sector. A realization of a law whose conditional past–future information reaches $I^*$ needs $|\mathcal C_H|\ge2^{I^*}$ (machine-checked). If two visible histories of length $k$ with a common endpoint, each of probability at least $p_0$, induce next-step laws at total-variation distance at least $\delta$, then $I(X_{<k};X_{k+1}\mid X_k)\ge p_0\delta^2/\ln2$, by Pinsker's inequality (proved on paper, with exact probes) [Main §2.3; CT06].

[Main §1.3] names four conditions on a hidden sector: (C1) influence, (C2) persistence of records, (C3) capacity, and (C4) history readback, in which two histories with the same present induce different next-step laws. In a faithful realization (C4) coincides with $M_t>0$, by the Corollary; (C1) and (C3) follow from it, and (C2) is a physical-regime premise. The conditions are diagnostics of a realization, not hypotheses of Theorem 1.

***

## 3. Physical interpretation: indivisibility from recurrence

Restricted observation of a finite reversible system produces a quantum-like feature: stochastic indivisibility. Between some pair of times, no stochastic map relates the visible transition matrices. Finite recurrence forces this whenever the law has history readback.

### 3.1 Recurrence and indivisibility

Write $\Gamma_t$ for the *rooted* visible transition matrix from time 0 to time $t$ (rows indexed by $x_0$). The family is *P-divisible on $\{0,\dots,n\}$* if for all $s<t\le n$ some stochastic $\Lambda$ satisfies $\Gamma_t=\Gamma_s\Lambda$. A stochastic divisor contracts total variation, so under P-divisibility $\|\delta_a\Gamma_t-\delta_b\Gamma_t\|_{\mathrm{TV}}$ cannot increase. This is the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1].

**Theorem 3** (recurrence and overlap [Main §2.3]). *Let $\varphi$ be a bijection of a finite set. If two rows of $\Gamma_s$ overlap in a column and $\Gamma_n=I$ for some $n>s$, the family is not P-divisible on $\{0,\dots,n\}$.*

Finite order of $\varphi$ gives a return $\Gamma_L=I$, and a non-permutation one-step matrix has overlapping rows. Two overlapping rows of $\Gamma_s$ are at distance below 1, and at a return $\Gamma_n=I$ at distance 1, which no stochastic divisor permits. The rooted form is machine-checked, and Doukas states the same argument concurrently [Dou26, Prop. 1]. Monotone distance is necessary for P-divisibility but not sufficient [Main §2.3].

A stochastic matrix with a stochastic one-sided inverse is a permutation matrix [BB12, Problem 23] (machine-checked). On a fixed finite reversible substratum (C4) therefore forces indivisibility somewhere in the recurrence cycle [Main §2.3]. (1) If every $\Gamma_k$ before the recurrence time $L$ were a permutation, the present visible state would determine the initial one, and no two histories with a common endpoint could differ in their next-step laws, contrary to (C4). (2) So some $\Gamma_k$ is not a permutation, and (3) divisibility from $k$ to $L$, where $\Gamma_L=I$, would need a stochastic inverse of $\Gamma_k$. The conclusion is machine-checked, by the route of Theorem 3, from a routed-readback form of (C4), in which a visible-history record written into the hidden state is read back later [Main §1.3]; from history-level (C4) it is proved on paper.

### 3.2 What the indivisibility is, and what it is not

The indivisibility of §3.1 is global: it occurs somewhere in the recurrence cycle, not on every window. Conditional memory does not force short-window indivisibility (§4.2).

Three notions are distinct, and no unconditional implication holds among them [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion. Tracing out a permutation unitary from a diagonal hidden state gives channels that preserve diagonal states, and for them (2) implies CP-indivisibility [Main §3.2, Theorem (CP-indivisibility, framework scope)]. Outside that class the implication fails: with $\Phi_{t_1}$ conjugation by the Hadamard gate and $\Phi_{t_2}=\mathrm{id}$ the family is CP-divisible, while its computational-basis populations, $\tfrac12J\to I$ with $J$ the all-ones matrix, are P-indivisible [Main §3.2, Remark (scope: P-indivisibility is not quantum non-Markovianity)]. Distinguishability backflow witnesses divisibility failure in one direction only [BLP09]; for bijective dynamical maps on a $d$-dimensional system, CP-divisibility is equivalent to monotone distinguishability with a $(d+1)$-dimensional ancilla [BJA17].

Theorem 1 is a representation result: it states which laws admit realizations and quantum representations, not why a physical system exhibits a law with memory [Main §3.4, Remark (representation, not explanation)].

***

## 4. Illustrative examples

Three examples show recurrence-driven indivisibility (§4.1), memory without short-window indivisibility (§4.2), and the smallest realization of Theorem 3 (§4.3).

### 4.1 A minimal model

Let $\mathcal C_V=\{0,1\}$ and $\mathcal C_H=\{1,\dots,6\}$ [Main §2.4]. For $h\in\{1,2\}$, $\varphi$ swaps $(0,h)$ with $(1,h)$. It flips the visible bit and keeps $h$, which then records the flip. At fixed $x$, $\varphi$ swaps $h=3$ with $4$, and $5$ with $6$. A second application reads the record and flips the bit back. With $h$ uniform:
$$
\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\qquad \Gamma_2=I,\qquad
\Gamma_1^{-1}\Gamma_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$
The only candidate divisor has negative entries, so the family is P-indivisible. A Markov chain with the same one-step matrix would instead give $\Gamma_1^2$, with diagonal entries 5/9 and off-diagonal entries 4/9.

With $x_0$ uniform and independent of $h$, $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$ while $P(x_2{=}0\mid x_1{=}1)=1/3$. For $P(x_0{=}0)=a$, the second value is $a/(2-a)$.

### 4.2 Memory without short-window indivisibility

Let $X_0$ and $X_1$ be independent uniform bits and $X_2=X_0\oplus X_1$. Every two-time transition matrix is $\tfrac12J$, so the family factors through $\Lambda=I$ and is P-divisible. Yet $I(X_0;X_2\mid X_1)=1$ bit. Up to flipping the final bit, this is the process of [RHP14, Eq. (15)]; it appears concurrently in [Dou26, App. A].

### 4.3 The card table

The two-card game of [Book §1.11] uses two cards, each red or black: a visible *hole card* $h$, and a face-down *burn card* $b$, uniform and independent of $h$. A *street* is one shuffle step, in which the two cards trade places: $\varphi(h,b)=(b,h)$. A *peek* reveals the hole card and overwrites the burn card, which holds the record, with a fresh card drawn uniformly and independently.

The probability that the hole card at showdown is the hole card as dealt is obtained by exact enumeration of the equally likely cases:

| Protocol | Probability |
|---|---|
| one shuffle | 1/2 |
| two shuffles | 1 |
| two shuffles, with a peek between them | 1/2 |
| Markov prediction for two shuffles, $\Gamma_1^2$ | 1/2 |

Here $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$. The two rows of $\Gamma_1$ are equal, so for every $\Lambda$ the two rows of $\Gamma_1\Lambda$ are equal and $\Gamma_1\Lambda\neq I$: the family is P-indivisible.

The peek row depends on the rule: if the peek only reveals or replaces the hole card, the probability is 1, so the 1/2 comes from overwriting the record, not from looking. With anticorrelated cards ($b=1-h$), $\Gamma_1$ is a permutation and the game is divisible.

On card inputs the game is a classical stochastic process, and its P-indivisibility is notion (2) of §3.2. Embed the game as a permutation unitary acting on an arbitrary hole-card state $\rho$, with the burn card in the uniform diagonal state [Main §3.2]. The one-step channel is then the constant channel $\rho\mapsto\operatorname{tr}(\rho)\,I/2$, which is entanglement-breaking [Main §3.2, Remark (failure of (C1))]. The two-step map is the identity channel. The family is therefore CP-indivisible [Main §3.2, Theorem (CP-indivisibility, framework scope)].

Following Bäcker, Beyer and Strunz [BBS24], a two-step process has classical memory when the second map can be written as an instrument realizing the first map, followed by channels conditioned on its outcome. With the hidden slot initialized to a fixed card instead, the swap has the maps $\rho\mapsto|0\rangle\langle0|$ and $\rho\mapsto\rho$ and admits no such decomposition [Main §4.5]. With the uniform burn card it does: the instrument $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, $o\in\{0,x,y,z\}$, sums to the one-step map, and the channels $\rho\mapsto\sigma_o\rho\sigma_o$, conditioned on $o$, return $\rho$.

A card arrangement violates no Bell inequality [Book §1.11; Main §3.3].

***

## 5. Black-hole information: a bounded application

The black-hole information problem asks whether the radiation of an evaporating black hole carries the information of what formed it [Haw76; Pag93; Pag13]. Under OI two questions separate: whether information is conserved in the global reversible dynamics, and whether it can be recovered from the records an observer can access, its *access class*. The results below are finite computations in toy models of configurations, permutations and configuration reads. The combinatorial results were checked exhaustively at small size and the Page-time fraction by exact algebra [BHa; BHb]. They concern the framework's nested-partition construction [GR App. A; Book §7.6], not a particular black hole.

### 5.1 Conservation and access

The configuration space is modelled as $\mathcal C_V\times\mathcal C_B\times\mathcal C_D$, with $V$ the exterior visible region, $B$ the black-hole interior and $D$ the sector beyond the cosmological horizon; radiation is emitted from $B$ into $V$ [GR App. A.1]. A bijection loses no information about the global state.

<!-- OWNER: R11. Claim A below contradicts live text at ch07:110 / FULL:1987, ch18:146 / FULL:4966 and ch18:158 / FULL:4978; the falsification framing at ch07:159–161 / FULL:2036–2038 is unfalsifiable as stated; ch18:130 / FULL:4950 inherits ch07:110. The paper must not land until the owner corrects those sites or drops this paragraph and its restatements (§6.5 item 4, §7, abstract). -->
Bijectivity of the global map neither implies recovery from the accessible records nor is necessary for it [BHa, claim A].

Let $\mathcal U$ be the set of joint values of the registers left unread at the end, $\mathcal M$ the message set, and the *accessible advantage* the gain in success probability over a blind guess. Of the 40,320 bijections of $\{0,1\}^3$, 1,376 give zero accessible advantage for a binary message with one register unread after two emissions; sixty non-injective maps of $\{0,1\}^2$ recover the message exactly under complete access. Bijective dynamics with complete endpoint access gives exact recovery, and with $\mathcal U$ inaccessible $P_{\mathrm{succ}}\ge1/|\mathcal U|$, so zero advantage in a bijective instance requires $|\mathcal U|\ge|\mathcal M|$; 32 non-injective maps of $\{0,1\}^2$ violate this bound. The endpoint guarantees above are sufficient, not necessary. The bound is the remnant-capacity form of a known fact, and its linear case is the secret-sharing threshold [BHa; Sha79].

### 5.2 Where the Page entropy comes from

A permutation unitary maps configuration basis states to configuration basis states, so from a configuration every state on the orbit is a product state across any configuration-aligned cut. From any initial state, the entanglement entropy across such a cut is at most the Shannon entropy $H(p_0)$ of the initial configuration distribution [BHb, C1–C2].

<!-- OWNER: R11. The following paragraph contradicts live text at ch07:126 sentence 1 / FULL:2003 and GR:869, and the unconditional Page-curve statements at ch18:146 / FULL:4966 and ch19:334 / FULL:5510. -->
The framework's Page-curve argument [GR, Thms A.8–A.9] assumes the scrambling condition H-scramble, equidistribution of the orbit over pure states on an energy shell. In the setting it uses, a definite initial configuration with configuration-aligned bipartitions, H-scramble fails for every bijection, by the result above. The Page value enters the argument only through the Haar ensemble that H-scramble posits, not through bijectivity or the cycle decomposition [BHb, C6(a)–(b)].

A dynamics satisfying H-scramble with the full product space as its shell would produce the Page value [BHb, C6(b)]. On an energy shell, however, the Haar-typical value differs from the Page value $S_{\mathrm{Page}}(d_B,d_R)$, Page's average for factor dimensions $d_B,d_R$ [Pag93], in a direction that depends on the shell [BHb, C6(c)]. Whether the substratum supplies H-scramble, or a substitute, is open.

### 5.3 The Page time

<!-- OWNER: R12 (conditions level, non-blocking). ch18:148 / FULL:4968 calls the Page time "a mass-independent fraction" without the constant-coefficient condition stated below. -->
Assume the mass-loss law $dM/dt=-\alpha/M^2$ with $\alpha$ constant, $S_{\mathrm{BH}}\propto M^2$, and a constant ratio $\beta$ of the radiation's coarse-grained entropy gain to the black-hole entropy lost. Then the turnover falls at $t_P/t_{\mathrm{evap}}=1-\bigl(\beta/(1+\beta)\bigr)^{3/2}$ [Pag13, Eq. (8)]: 0.646 at $\beta=1$, the value of mode-for-mode counting, and about 0.538 at Page's $\beta\approx1.485$ for photons and gravitons [Pag13]. In the quasi-stationary semiclassical regime, $\beta$ exceeds 1 [Pag05, Eqs. (5)–(10)].

A mass-dependent coefficient moves the fraction; for $\alpha\propto M^{-1/2}$ it is 0.7027 [BHb, C7]. The fraction is therefore conditional on all three inputs.

### 5.4 Open steps

Open are: whether H-scramble, or any substitute, holds for the substratum; the step from the cycle time average of [GR, Thm A.8] to the pointwise curve of [GR, Thm A.9]; the generalized second law [GR App. A.6]; agreement with quantum-extremal-surface computations of the Page time, which needs matched radiation-entropy accounting [Pen20]; and the conjectured correspondence between islands and substratum cycles [Book §7.6].

<!-- OWNER: R11. The following sentence contradicts GR:811 ("D is frozen on evaporation timescales"); keep or drop with R11. -->
Decoupling of $D$ over the evaporation is not established by timescale ordering. At 30 solar masses, $t_{\mathrm{evap}}/\tau_B^D\ge1.785\times10^{57}$ and $t_P/\tau_B^D\ge1.153\times10^{57}$, with $t_P$ the Page time at $\beta=1$. These bounds hold, by exact interval arithmetic, over the full intervals assumed for the greybody factor and $\tau_B^D$ [BHa, item F]. They do not show that information reaches $D$, that [GR, Thm A.7] fails within its stated scope $t\ll\tau_B^D$, or that no other decoupling argument exists.

***

## 6. Limitations and open problems

### 6.1 Operational completion

Operational quantum mechanics requires, beyond Theorem 1's fixed-basis statistics, coherent preparations, noncommuting interventions and composites represented by one instrument theory.

Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear maps are available on the system and at every ancilla level [GR §3.3]. The five conditions are: (i) available families send positive states to positive states and their outcome traces sum to the input trace; (ii) operations remain available with a one-state ancilla adjoined; (iii) an untouched independent system can be adjoined without changing an intervention; (iv) every finite unitary on every composite is available; (v) attaching a fresh uniformly prepared ancilla to a composite, acting, and discarding it gives an available operation.

**Theorem 4** (operational-completion characterization [GR §3.3, Theorem (operational-completion characterization)]). *For every nonempty finite system, the available outcome families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*

Both directions are machine-checked, $\Rightarrow$ as `physical_of_exactAll` and $\Leftarrow$ as `exactAll_of_physical_general`, for every nonempty finite carrier.

On the qubit, each condition is independent of the other four and of a fixed finite observation process satisfying (C1)–(C4). For each condition there is a qubit theory that realizes that process and the other four conditions, and fails it. In particular, a qubit theory that never creates coherence realizes the observation process and is not quantum. So OI alone does not imply quantum mechanics. Which of (iii)–(v) a physical substratum supplies is open [GR §3.3].

### 6.2 The evolution relating two times is not selected

Representability does not fix the unitary evolution relating two times [Main §3.4, Remark (scope: representability, not selection of the relating evolution)]. Two coherent lifts of one visible family, unitary dilations that reproduce the visible law at every time and compose exactly across times, can differ by a time-dependent right action invisible to the visible law and then have different relating evolutions, while a constant deformation cancels from every relating evolution (both machine-checked).

Take a lift with trivial ancilla at one time, and form the fixed-basis datum whose evolution is the lift's unitary, with uniform initial law and identity readout. If two such data have the same one-step visible matrix, their root-conditioned trajectory laws agree at every horizon (`bridge_traj`); conversely, if their rooted families agree, their one-step visible matrices are equal (`rooted_eq_iff_slice_eq`, forward direction). Each such trajectory law is fixed-basis realizable and stochastic (`realData_traj_stochastic`). The fixed-basis correspondence therefore acts on the quotient by visible equality. A selection condition beyond representability and ordinary coherence would be needed, and none is supplied here.

### 6.3 No fixed finite carrier reproduces a qubit

A fixed finite realization with $N$ ontic configurations generates only behaviour matrices that factor nonnegatively through $N$ states. Simulating a qubit's prepare-and-measure statistics needs classical memory unbounded over finite experiments: explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and Montina reports Hardy's result that the number of ontic states cannot be finite [Mon08; Har04]. So no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly; the factorization is proved, and the unboundedness is imported [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form)]. The obstruction does not touch Theorem 1, whose realization is chosen per law.

### 6.4 Open problems

Beyond §5.4, §6.1, §6.2 and the origin of the quadratic Born exponent (§2.3), open are: (1) machine checks of the steps of §2.2, §2.4 and §3.1 that lack one; (2) whether the minimal hidden predictive memory equals $M_t$ once ledger bits that cannot influence the future are quotiented (the fixed-dimension form is false) [Main §3.4]; (3) exact gluing for recurrent target families, and approximation on windows short compared with the recurrence time [Main §3.4]; (4) (C2) necessity, which is conditional on a hidden-sector mixing hypothesis motivated by eigenstate thermalization [Main §3.4]; (5) Bell correlations: a deterministic completion that keeps pointwise causal cones and a setting-independent pre-setting ensemble is Bell-local, $|S_{\mathrm{CHSH}}|\le2$ [Bel64; CHSH69; Main §3.3], so a deterministic completion reproducing quantum Bell correlations must give up one of the two; the framework keeps measurement independence and adopts ontic parameter dependence, in which one wing's microstate response depends on the remote setting without operational signalling, and the compatibility of that choice with operational no-signalling and the gravitational continuum limit of the lattice is the open hypothesis H-Bell [Main §3.3].

### 6.5 What is not claimed

1. No derivation of quantum mechanics: Theorem 1 contains every finite law, and the Born exponent is not selected.
2. No unique selection of the operational theory: conditions (i)–(v) are not implied by OI alone, their independence is shown on the qubit, which of (iii)–(v) a physical substratum supplies is open, and the visible law does not fix the relating evolution.
3. No characterization of memory by the existence of a realization (§2.3), no identification of P-indivisibility with quantum non-Markovianity, and no claim that memory forces indivisibility on short windows (§3.2).
4. <!-- OWNER: R11. Restates §5.1 claim A and §5.2's H-scramble finding; it stands or falls with those paragraphs. --> No resolution of the black-hole information problem: the Page curve follows only under H-scramble, the Page-time fraction is conditional on its three inputs, the correspondence with islands is conjectural, the generalized second law is open, and the results of §5 are finite toy-model computations, checked exhaustively at small size and by exact arithmetic.
5. No claim that the physical hypothesis is established or tested.
6. No claim that the card game (§4.3) produces quantum rather than classical statistics: on card inputs its statistics are classical stochastic ones; under the unitary embedding its one-step channel is entanglement-breaking and its two-step family admits a classical-memory decomposition; it violates no Bell inequality.

***

## 7. Conclusion

At every finite horizon the laws an embedded observer of a finite reversible system can record are exactly the finite stochastic laws, and exactly the fixed-basis unitary Born laws. Because the representation is universal, the discriminating content lies in memory: every deterministic completion carries the visible memory in its hidden state, and finite recurrence turns history readback into stochastic indivisibility within the recurrence cycle. Exact operational quantum mechanics is reached only under completion conditions that OI alone does not imply, and representability does not select the evolution relating two times.

<!-- OWNER: R11. Restates §5.1 claim A and §5.2's H-scramble finding; it stands or falls with those paragraphs. -->
Applied to black-hole information, the same viewpoint separates conservation from access: bijectivity conserves the global state but does not determine what an access class recovers, and in the framework's Page-curve argument the Page entropy enters through a scrambling hypothesis, not through bijectivity.

## Code, data and formal verification

<!-- OWNER: retention §A.42. The Lean-check sentence below is an enduring certification claim. Before the paper lands, an expected result for commit 687e885b (build success, release-gate verdict, each cited declaration's #print axioms set, recipe, provenance) is retained beside the paper, or the commit is shown to fall inside an archive covered by the evidence-retention step. Placeholder: [expected-result file path]. -->
The declarations in Appendix A were checked in Lean 4/Mathlib at commit 687e885b1cfd24d6f17eee439101afc8acf07015 by the recipe

    python3 tools/lean_axiom_check.py --require-lake

which builds the Lean project and requires every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`; the expected result is in [expected-result file path].

The probes and the black-hole computations [BHa; BHb] are released under the MIT License (concept DOI 10.5281/zenodo.19060318), at these repository paths:

- `papers/oi_lattice_code/foundations/` (probes);
- `verification/programmes/black-hole-information/` (black-hole computations).

## Appendix A. Machine-checked declarations

Modules of the `OIBridge` Lean library; line numbers at commit `687e885b`.

\begingroup\small\raggedright

- **Theorem 1** (§2.2): `finite_horizon_equivalence` (Equivalence:462); directions `S_imp_D` (:422), `D_imp_Qfb` (:294), `Qfb_imp_S` (:245), compositions :466–468; supporting `permMatrix_mem_unitaryGroup` (EquivalenceChain:179). Prior independence is proved on paper.
- **Theorem 2** (§2.4): `pushforward_identity`, `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory` (HiddenMemory:83, :114, :170, :185), for a joint law of history, present and hidden state; the time-$t$ identification and the standard vanishing criterion for conditional mutual information [CT06] are not machine-checked.
- **Capacity bound** (§2.4): `c3_necessity`, `card_hidden_ge_two_pow_Istar` (C3Necessity:80, :117).
- **Stochastic-inverse lemma; Theorem 3** (§3.1): `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110); `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148).
- **Readback forces indivisibility** (§3.1): `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) for routed readback; on paper for (C4).
- **Relating evolution** (§6.2): `gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative` (CoherentLiftGauge:537, :451); `bridge_traj`, `rooted_eq_iff_slice_eq` (forward direction), `realData_traj_stochastic` (TrackBQfbBridge:276, :180, :286).
- **Theorem 4** (§6.1): `exactAll_iff_physical_general` (GeneralCarrier:100); $\Rightarrow$ `physical_of_exactAll` (PhysicalCharacterization:301); $\Leftarrow$ `exactAll_of_physical_general` (GeneralCarrier:93) via `krausSoundExt_of_validity_inert` (OperationalValidity:124), `compositeCompleteness_unconditional` (IsometryExtension:179, premise discharged by `finiteIsometryExtensionSF_discharged`, :116) and `exactAll_of_levelOne` (LevelOneSeam:196).
- **Independence; OI alone does not imply QM** (§6.1, qubit): `five_way_minimality` (RankGapTheory:702), `oi_alone_not_qm` (GeneralCarrier:160).

## References

**Corpus** (repository commit `687e885b`, concept DOI 10.5281/zenodo.19060318)

[Main] A. Maybaum, "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation," `papers/Main.md`.

[GR] A. Maybaum, "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon," `papers/GR.md`.

[Book] A. Maybaum, *The Incompleteness of Observation*, `book/`.

[BHa] A. Maybaum, "Access audit: recovery from accessible records in finite reversible models," `bh01_access_v1/` in the black-hole computations' directory.

[BHb] A. Maybaum, "Permutation dynamics versus quantum scrambling; Page-time fraction," `bh02_scramble_v1/` in the black-hole computations' directory.

**External**

[Bar23] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085v2 (2023).

[Bar25] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778v3.

[Bar26] J. A. Barandes, "The Born Representation Theorem and the Unistochastic Theorem," arXiv:2608.04354v1 (2026).

[BB12] J. C. Baez and J. Biamonte, "Quantum techniques for stochastic mechanics," arXiv:1209.3632v5 (2012).

[BBS24] C. Bäcker, K. Beyer, and W. T. Strunz, "Local disclosure of quantum memory in non-Markovian dynamics," *Phys. Rev. Lett.* **132**, 060402 (2024). <!-- VERIFY: content not read in the audits; definition taken via Main:702 -->

[BD16] F. Buscemi and N. Datta, "Equivalence between divisibility and monotonic decrease of information in classical and quantum stochastic processes," *Phys. Rev. A* **93**, 012101 (2016); arXiv:1408.7062v3.

[Bel64] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195 (1964).

[BJA17] B. Bylicka, M. Johansson, and A. Acín, "Constructive method for detecting the information backflow of non-Markovian dynamics," *Phys. Rev. Lett.* **118**, 120501 (2017); arXiv:1603.04288v2.

[BLP09] H.-P. Breuer, E.-M. Laine, and J. Piilo, "Measure for the degree of non-Markovian behavior of quantum processes in open systems," *Phys. Rev. Lett.* **103**, 210401 (2009); arXiv:0908.0238v2.

[Cal26] S. Calvo, "On the stochastic-quantum correspondence," arXiv:2601.18720v2 (2026). <!-- VERIFY: claim taken from the v2 abstract (arXiv API record read 2026-10-26); body not read first-hand -->

[CHSH69] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, "Proposed experiment to test local hidden-variable theories," *Phys. Rev. Lett.* **23**, 880 (1969).

[CT06] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006). <!-- VERIFY: content not read in the audits (AUDIT r4 P3.3) -->

[dMU21] L. de Moura and S. Ullrich, "The Lean 4 theorem prover and programming language," in *Proc. CADE 28* (Springer, 2021), p. 625.

[Dou26] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095v3 (2026).

[EGGH26] G. Egri, M. Gömöri, B. Gyenis, and G. Hofer-Szabó, "Trajectory of probabilities, probability on trajectories, and the stochastic-quantum correspondence," arXiv:2602.23491v1 (2026).

[GH03] E. F. Galvão and L. Hardy, "Substituting a qubit for an arbitrarily large number of classical bits," *Phys. Rev. Lett.* **90**, 087902 (2003); arXiv:quant-ph/0110166v3.

[Har04] L. Hardy, "Quantum ontological excess baggage," *Stud. Hist. Philos. Mod. Phys.* **35**, 267 (2004). <!-- VERIFY: content not read (AUDIT r4 C14, P3.2); cited only as reported in [Mon08] -->

[Haw76] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).

[LP17] D. A. Levin and Y. Peres, with contributions by E. L. Wilmer, *Markov Chains and Mixing Times*, 2nd ed. (American Mathematical Society, 2017).

[Mathlib20] The mathlib Community, "The Lean mathematical library," in *Proc. ACM SIGPLAN Conf. Certified Programs and Proofs* (ACM, 2020), p. 367.

[Milz20] S. Milz, D. Egloff, P. Taranto, T. Theurer, M. B. Plenio, A. Smirne, and S. F. Huelga, "When is a non-Markovian quantum process classical?," *Phys. Rev. X* **10**, 041049 (2020); arXiv:1907.05807v3.

[Mon08] A. Montina, "Exponential complexity and ontological theories of quantum mechanics," *Phys. Rev. A* **77**, 022104 (2008); arXiv:0711.4770v2.

[Pag93] D. N. Page, "Average entropy of a subsystem," *Phys. Rev. Lett.* **71**, 1291 (1993); arXiv:gr-qc/9305007v2.

[Pag05] D. N. Page, "Hawking radiation and black hole thermodynamics," *New J. Phys.* **7**, 203 (2005); arXiv:hep-th/0409024v3.

[Pag13] D. N. Page, "Time dependence of Hawking radiation entropy," *J. Cosmol. Astropart. Phys.* **09**, 028 (2013); arXiv:1301.4995v3.

[Pen20] G. Penington, "Entanglement wedge reconstruction and the information paradox," *J. High Energy Phys.* **09**, 002 (2020); arXiv:1905.08255v3.

[RHP14] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014); arXiv:1405.0303v2.

[Sch21] H.-J. Schmidt, "Dilation of stochastic matrices by coarse graining," arXiv:2106.03513v1 (2021).

[SGD19] P. Strasberg and M. García Díaz, "Classical quantum stochastic processes," *Phys. Rev. A* **100**, 022120 (2019); arXiv:1905.03018v2.

[Sha79] A. Shamir, "How to share a secret," *Commun. ACM* **22**, 612 (1979). <!-- VERIFY: bibliographic data confirmed on Crossref (science re-check); content (the linear threshold scheme) cited from memory and not read; the BH-01 package names the secret-sharing threshold without a source -->

\endgroup
