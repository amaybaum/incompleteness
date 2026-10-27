% Observational Incompleteness: From Deterministic Dynamics to Quantum Observations
% Alex Maybaum
% October 2026

---
geometry: margin=1in
fontsize: 11pt
...

**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

***

## Abstract

Could the randomness of quantum measurements arise because observers cannot access all the information in an underlying deterministic reality? Observational incompleteness (OI) is the hypothesis that every physical observer is a proper part of a finite reversible deterministic system and records only the visible marginals of its dynamics. At every finite horizon, all finite stochastic laws, the visible marginals of finite reversible dynamics and the records of finite unitary systems measured in one fixed basis coincide, so stochastic, quantum-like records can arise exactly from deterministic dynamics; the known components (Egri et al.; Barandes) are stated as one machine-checked theorem. Because Markov laws lie in every class, the discriminating content is memory: every faithful realization carries the law's conditional memory in its hidden state. On one finite reversible system with a hidden prior shared by every root and drawn independently of it, the rooted visible family, with a row for every initial visible state (root) including roots of visible probability zero, is P-indivisible somewhere in its recurrence cycle whenever some rooted transition matrix is not a permutation, which every non-deterministic visible step supplies; with a full-support visible prior this indivisibility is equivalent to conditional memory $M_k>0$ at some order $k$ below the recurrence time. Exact finite operational quantum mechanics is characterized by five completion conditions that OI alone does not imply. OI places the zero-point sum and the effective cosmological constant at different levels of description, and separates conservation of black-hole information from its accessible recovery; open are the completion conditions a physical substratum supplies, the Born exponent and the gravitational field equations.

## 1. Introduction

### 1.1 Embedded observation

Could the randomness of quantum measurements arise because observers cannot access all the information in an underlying deterministic reality? Einstein's objection to quantum randomness is usually paraphrased as "God does not play dice". The picture examined here replaces dice with cards: God plays cards. A deck evolves by fixed rules, nothing in the rules is random, and yet a player who sees only some of the cards finds the game uncertain. The picture is an analogy. It shows how hidden information, deterministic rules and random-looking observations fit together; it proves nothing about quantum mechanics, and every result below is stated and proved without it.

In the simplest version two cards lie on a table, one face up and one face down, and each shuffle swaps them. After one shuffle the player cannot predict the colour now showing any better than by tossing a coin. After a second shuffle the original card is back, with certainty. The player's record therefore has memory: what is seen next depends on what was seen earlier, not only on what is showing now, and that memory is kept in the face-down card. Nothing random happened; the uncertainty is the player's, and it comes from what the player cannot see. The exact table is in §2.6, and the game's statistics are those of ordinary classical probability.

An observer inside a closed system registers only part of its configuration. If the whole evolves by a bijection, hidden states compatible with the same visible state can send it to different futures, so the visible sector evolves stochastically although the whole evolves deterministically.

The idea matters because it turns a question about interpretation into questions that can be settled mathematically. Which patterns of observations can a partly hidden deterministic world produce? Where must the hidden information sit? What does it force the observations to look like? Sections 2 and 3 answer these questions for finite worlds, and identify what the answers leave open.

This is modelled by a triple $(S,\varphi,V)$ [Main §1.2]: a finite total system $S=\mathcal C_V\times\mathcal C_H$ of visible configurations $\mathcal C_V$ and hidden configurations $\mathcal C_H$, a bijection $\varphi$ of $S$, and an observer $V$ that registers $x\in\mathcal C_V$ and not $h\in\mathcal C_H$. The bijection is the reversible representative of the hidden dynamics, motivated by observed near-unitarity, and finiteness of all of $S$ is posited [Main §1.2, Remark (status of the early commitments)]. The finite reversible system $(S,\varphi)$ is the *substratum*.

A bijection sends each configuration to exactly one successor and never sends two configurations to the same one, so it loses no information: the whole present determines the whole past. What the observer sees of the dynamics, the hidden part being ignored, is its *visible marginal*.

Observational incompleteness (OI) is the physical hypothesis that every physical observer is in this situation: a part of a finite, reversible, deterministic world that sees only part of it. Here incompleteness means that the hidden sector is inaccessible to the observer, not merely unknown to it so far. It is not joint unsharpness of non-commuting observables: it is present for a single fixed readout, and no uncertainty relation constrains fixed-readout visible laws [Main §3.4].

### 1.2 The idea and its consequences

Marginalizing a reversible dynamics over an unobserved register can produce stochastic laws, conditional memory, and failures of stochastic divisibility, in which no stochastic map carries an earlier visible transition matrix to a later one (when the earlier matrix is invertible, the unique candidate has a negative entry). The stochastic–quantum correspondence relates these features to quantum theory [Bar23; Bar25], and at the level of finite-horizon observable laws it is exact and universal (Theorem 1, §2.2): every finite stochastic law, every fixed-basis quantum record among them, is the visible marginal of a finite reversible deterministic system. Apparently stochastic, quantum-like observations can therefore arise exactly from deterministic dynamics. Because the correspondence is universal, the discriminating content lies in where the memory of a law must sit (§2.4) and in what finite recurrence does with it (§2.5). Section 3 states how far the correspondence reaches toward operational quantum mechanics, §§4–5 give two applications, and §6 sorts the results by status. Proofs, the status ledger and the probe code are in [Main], which this paper introduces; gravitational applications are in [GR] and [Book].

**Contributions.** The paper is expository and claims no new theorem; each known component is attributed where it is stated (§§2.2, 2.4, 2.5). The results of §§3.2–3.5 are proved in [GR] and [Main], the Bell ceiling being Bell's theorem under the framework's hypotheses, and those of §5 in unpublished research records with exact or exhaustive checks [BHa; BHb]; the novelty of the §§3.2–3.3 and §5 results has not been assessed. Deterministic systems have been analysed with quantum methods before, for example in [tH14].

*Conventions.* "Machine-checked" means checked in Lean 4/Mathlib [dMU21; Mathlib20] at commit `17b830bc` by the recipe under "Code, data and formal verification" (declarations in Appendix A); "proved on paper" means a written proof without a machine check; an "exact probe" is an exhaustive computation in exact rational arithmetic at small size. A *faithful realization* of a law is a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$ with an initial law under which the visible trajectory has that law.

## 2. Theoretical foundation: the established results and their assumptions

### 2.1 Setting

Fix finite sets $\mathcal C_V$ (with $|\mathcal C_V|\ge2$) and $\mathcal C_H$, a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$, and a horizon $K$. A law is a probability distribution on visible trajectories $(x_0,\dots,x_K)\in\mathcal C_V^{K+1}$. In a realization, $X_t$ and $H_t$ are the visible and hidden coordinates at time $t$, $X_{<t}=(X_0,\dots,X_{t-1})$ is the visible past and $X_{>t}=(X_{t+1},\dots,X_K)$ the visible future. Information is measured in bits, $\|\mu-\nu\|_{\mathrm{TV}}=\tfrac12\sum_k|\mu_k-\nu_k|$ is the total-variation distance, and $g_\#\mu$ is the pushforward of a law $\mu$ under a map $g$.

In words: a *law* lists the probability of every possible sequence of observations over $K+1$ steps. A *stochastic matrix* is a table of transition probabilities with one row per starting state, each row nonnegative and summing to one; a *permutation matrix* is the stochastic matrix in which every row is a single certainty and no two rows agree. The *total-variation distance* between two probability lists is the largest difference in probability they assign to any one event: 0 for identical lists, 1 for lists that give no outcome positive probability in common. The *conditional mutual information* $I(A;B\mid C)$ measures, in bits, how much $A$ still tells about $B$ once $C$ is known; it is zero exactly when, given $C$, $A$ carries no further information about $B$.

The visible law of a realization depends on the dynamics, the partition and the initial law (the prior), which is part of the realization datum, not selected by invariance under $\varphi$; the counting measure is a maximal-entropy default [Main §1.2, Remark (the measure as a realization datum)].

Three classes of law are compared [Main §3.4]:

- **$\mathsf S_K$**: all probability distributions on $\mathcal C_V^{K+1}$.
- **$\mathsf D_K$**: the visible trajectory laws of a bijection of $\mathcal C_V\times\mathcal C_H$, for some finite $\mathcal C_H$, under an initial law that may correlate the visible and hidden coordinates.
- **$\mathsf Q_K$**: the *fixed-basis Born records*, the laws of finite-dimensional unitary systems read out by projective Born measurement in one fixed basis at every step, from an initial state diagonal in that basis, the record being a fixed function of each outcome.

Informally, $\mathsf S_K$ is every statistical pattern whatever; $\mathsf D_K$ is every pattern that a partly hidden, deterministic, reversible world can show; and $\mathsf Q_K$ is every pattern of results from a finite quantum system that evolves by a *unitary*, the reversible, probability-preserving evolution of quantum theory, and is measured in the same way at every step, each result having the probability the *Born rule* assigns, the squared magnitude of its amplitude.

### 2.2 The finite-horizon correspondence

Which patterns of observations can a partly hidden deterministic world produce, and how do they compare with what quantum measurements produce? Over any fixed number of steps the answer is that the three lists coincide.

**Theorem 1** (finite-horizon stochastic–reversible–unitary equivalence [Main §3.4]). *For every finite visible alphabet and every finite horizon $K$,*
$$
\mathsf S_K=\mathsf D_K=\mathsf Q_K ,
$$
*so each class is the set of all probability laws on $\mathcal C_V^{K+1}$.*

In plain terms: any pattern at all can be produced by a hidden deterministic world, and also by a quantum system measured the same way at every step. Finite quantum records of this fixed-measurement kind therefore carry no statistical signature that a partly hidden deterministic world could not reproduce, and conversely. This settles a question of possibility, not of fact: it does not show that nature is such a world.

Theorem 1 is machine-checked: the three inclusions $\mathsf S_K\subseteq\mathsf D_K\subseteq\mathsf Q_K\subseteq\mathsf S_K$ and their compositions, with no construction entering as a hypothesis (Appendix A).

**Realization.** For $\mathsf S_K\subseteq\mathsf D_K$ the realization stores a sampled trajectory, with a clock, in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]. Every law also has a realization whose hidden prior is independent of $x_0$, by the finite-horizon process dilation for rational conditional kernels at positive-probability histories, the visible initial law being arbitrary, and by its response-table extension for arbitrary kernels (proved on paper, with exact probes) [Main §3.4, Theorem (finite-horizon process dilation) and its Extension].

The first construction is simple to picture. The hidden register holds a whole sequence drawn in advance from the law, together with a clock, and each step brings the next entry into view; the dynamics stays a bijection, and the observer, who sees only the entries already shown, finds them random with exactly the prescribed probabilities.

**Quantum representation.** For $\mathsf D_K\subseteq\mathsf Q_K$ the representation is the permutation unitary $U_\varphi|x,h\rangle=|\varphi(x,h)\rangle$, read out in the configuration basis at every step [Main §3.4]; $\mathsf Q_K\subseteq\mathsf S_K$ is the Born rule.

**Attribution.** The trajectory-labelling realization is [EGGH26, Prop. 13], packaged as one iterated bijection; the independent-prior form is their Prop. 16, without reversibility, and its Markov one-step case is the random-mapping representation [LP17, Prop. 1.5]. A permutation dynamics is a special case of a unistochastic process, one with transition probabilities $|U_{ij}|^2$ for a unitary $U$ [Bar25, p. 12 of arXiv v3; Bar23 §4.3; Bar26 §4]; the one-step $|\mathcal C_V|^2$-dimensional ancilla dilation of [Main §3.1] is that of [Bar26, Thm 3.3; Sch21, Thm 2]; and the every-step record law is [SGD19, Eq. (3)]; whether such records remain consistent when measurements are omitted [SGD19; Milz20] does not arise for $\mathsf Q_K$, which measures at every step.

### 2.3 Scope of the correspondence

Markov laws lie in all three classes, so neither a finite reversible realization nor a fixed-basis unitary representation distinguishes a law with memory from one without [Main §3.4, Remark (what this equivalence does and does not say)].

The relation $p=|U|^2$ is part of the definition of $\mathsf Q_K$, not an output. The unitaries supplied are permutations, with entries 0 and 1, so the recovered table is the same for $|U|^q$ at every $q>0$, and the quadratic exponent is not selected [Main §3.4; Bar26, Thm 3.1].

A finite bijection has finite order $L$, so one fixed realization has an $L$-periodic multi-time law: the correspondence holds per horizon, and a nonperiodic law has no exact all-time realization by one fixed finite substratum [Main §3.4].

The correspondence thus answers the question of possibility: a hidden deterministic model exists for every law, so its existence says nothing about a particular law, and one such world reproduces a pattern over a chosen finite stretch of time, not forever. The content lies in what such worlds must contain when the record has memory (§§2.4–2.5).

### 2.4 Where the memory lives

When the observed record has memory, so that what comes next depends on more than what is visible now, where is that memory kept? In the card game the record remembers the dealt card after the first shuffle, although the face-up card no longer shows it, because the face-down card holds it. The same is true in every hidden deterministic world that reproduces a record: whatever the record remembers is held in the hidden part, and the hidden part must be large enough to hold it.

Write $M_t := I(X_{<t};X_{t+1}\mid X_t)$ for the conditional memory at time $t$: how much the earlier record still tells about the next observation once the present one is known. A law is *Markov*, that is memoryless, exactly when $M_t=0$ at every $t$. In a realization, write $f_x(h)=\pi_V(\varphi(x,h))$, with $\pi_V$ the projection onto $\mathcal C_V$, and $\mu_\omega$ for the hidden posterior, the probabilities of the hidden states given what has been seen, after a positive-probability visible history $\omega=(x_0,\dots,x_t)$ ending at $x_t=x$.

**Theorem 2** (unavoidable hidden predictive memory [Main §3.4]). *In every faithful realization:*

*(a) $P(X_{t+1}\mid\omega)=(f_x)_\#\mu_\omega$;*

*(b) for histories $\omega,\omega'$ ending at $x$,*
$$
\|P(X_{t+1}\mid\omega)-P(X_{t+1}\mid\omega')\|_{\mathrm{TV}}\le\|\mu_\omega-\mu_{\omega'}\|_{\mathrm{TV}} ;
$$

*(c) $M_t\le I(X_{<t};H_t\mid X_t)\le\log_2|\mathcal C_H|$.*

(b) and the first inequality of (c) are data-processing inequalities. (a)–(c) are machine-checked for a joint law of history, present and hidden state; their identification with a realization's time-$t$ law is proved on paper [Main §3.4, Theorem (unavoidable hidden predictive memory); CT06].

In plain terms: the next observation depends on the past only through what the hidden state holds (a); two pasts can lead to different predictions only if they left the hidden state at least as differently prepared (b); and the memory visible in the record never exceeds the hidden memory, which never exceeds the hidden sector's capacity in bits (c).

A *memory witness* at $t$ is a pair of positive-probability histories ending at the same $x_t$ with different next-step laws; by the vanishing criterion for conditional mutual information [CT06], a law has one exactly when $M_t>0$.

**Corollary** (proved on paper [Main §1.5]). $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards. The forward direction rests on Theorem 2(a) in each realization; the converse on Theorem 2(a) in one realization, which Theorem 1 supplies (`S_imp_D`); both use the standard vanishing criterion for conditional mutual information [CT06], which, like the time-$t$ identification, is not machine-checked.

So the record has memory exactly when every hidden deterministic world that reproduces it keeps, in its hidden part, a trace of the past that changes what is seen next.

The hidden sector also has a minimum size and a minimum memory. With $I^*=\max_t I(X_{<t};X_{>t}\mid X_t)$, a realization of the law needs $|\mathcal C_H|\ge2^{I^*}$ (machine-checked in the joint-law form of Theorem 2). Over deterministic completions, not required to be bijective, the least hidden predictive memory $I(X_{<t};H_t\mid X_t)$ is exactly $I(X_{<t};X_{>t}\mid X_t)$, attained by the canonical predictive quotient, and equals $M_t$ exactly when $I(X_{<t};X_{>t+1}\mid X_t,X_{t+1})=0$, while bijective realizations run from time 0 carry $H(X_{<t}\mid X_t)$, Markov laws included [Main §3.4, Remark (a variational question)]; the lower bound is machine-checked for bijective realizations and proved on paper for non-injective ones. Conversely, memory has a floor: if two values of $X_{<t}$ followed by a common present state $X_t$, each of joint probability at least $p_0$, induce next-step laws at total-variation distance at least $\delta$, then $M_t\ge p_0\delta^2/\ln2$, by Pinsker's inequality (proved on paper, with exact probes) [Main §2.3, Lemma (accessible conditional memory from readback); CT06]. Observed memory thus bounds an inaccessible quantity: measurable conditional information fixes a lower bound on the hidden sector's size and the exact minimum of the predictive memory a deterministic completion must carry.

Four conditions on a hidden sector are named in [Main §1.3], as diagnostics of a realization rather than hypotheses of Theorem 1: (C1) influence; (C2) persistence of records; (C3) capacity, $\log_2|\mathcal C_H|\ge I^*$; and (C4) history readback, a memory witness at some accessible order, an order short compared with the recurrence time, as accessible windows are [Main §2.3, Scope]. In a faithful realization (C4) coincides with $M_t>0$, and the Corollary places it in the hidden state; (C1) follows from (C4), and (C3) holds by the capacity bound. (C2) has two forms. (C2-structural), the persistence of a stored record until its readback, holds by reversibility in every bijective realization and constrains coarse-grained descriptions of the hidden sector; (C2-slow), a hidden coarse-grained mixing time long compared with the accessible window, is one mechanism for it, and fast hidden dynamics that conserves the record is another [Main §1.3]. The necessity of (C2) is a theorem in the coupling-step model, in which the next visible state is a function of the current visible and hidden states and $\pi_H$ is the model's reference hidden law, toward which a mixing hypothesis would have the hidden state relax between couplings [Main §3.4, Theorem (physical memory: C2, process form)]. There, observed conditional memory $M_k>0$ at an accessible order $k$ forces some realized hidden conditional at that coupling time to lie at total-variation distance at least $\varepsilon_{\min}(M_k,|\mathcal C_V|)>0$ from $\pi_H$, with no mixing hypothesis; under the mixing hypothesis this becomes the slow-bath form, a lower bound on the mixing time.

In plain terms, the four conditions are a checklist for a hidden sector that produces observable memory: it must influence what is seen (C1), keep what it records (C2), have room to record it (C3), and feed the record back into what is seen (C4). Coupling, persistence and capacity without readback produce no memory: a fair coin has realizations with all three and zero conditional memory on arbitrarily long horizons [Main §2.3, Remark (why (C4) is a separate condition)]. The memory results establish that observed memory is real information held out of sight: it must be stored in the hidden part, it sets a minimum size for that part, and it is what separates laws with memory from memoryless ones, which the correspondence of §2.2 cannot.

### 2.5 Recurrence and indivisibility

A weather forecast from Monday to Wednesday can be built from one from Monday to Tuesday and one from Tuesday to Wednesday. When can the probabilities of an observed process be chained in this way? In the card game the forecast from the deal to the first shuffle is a coin toss whichever card was dealt, yet the forecast to the second shuffle is certainty; no forecast from the first shuffle to the second can turn two identical coin-toss rows into two different certainties, so the chain breaks. The property that fails is called P-divisibility, and in a finite reversible world with any visible step that is not fully predictable its failure is unavoidable somewhere in the world's cycle.

Fix one hidden prior shared by every root and drawn independently of it, and write $\Gamma_t$ for the *rooted transition matrix* from time 0 to time $t$, with a row for every $x_0\in\mathcal C_V$, roots of visible probability zero included. The family is *P-divisible on $\{0,\dots,n\}$* if for all $s<t\le n$ some stochastic $\Delta_{s,t}$ satisfies $\Gamma_t=\Gamma_s\Delta_{s,t}$. A stochastic divisor contracts total variation, so under P-divisibility $\|\delta_a\Gamma_t-\delta_b\Gamma_t\|_{\mathrm{TV}}$, with $\delta_a$ the point mass at $a$, cannot increase. This is the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1].

In words, the family is P-divisible when every later table of probabilities from the start can be obtained from every earlier one by one further table of transition probabilities. Each row of $\Gamma_t$ is the forecast from one possible starting state, its *root*.

**Theorem 3** (recurrence and overlap [Main §2.3]). *Let $\varphi$ be a bijection of $\mathcal C_V\times\mathcal C_H$ with one hidden prior shared by every root and drawn independently of it. If two rows of $\Gamma_s$ have a positive entry in a common column and $\Gamma_n=I$ for some $n>s$, the family is not P-divisible on $\{0,\dots,n\}$.*

Two such rows are at total-variation distance below 1 at time $s$ and exactly 1 at time $n$, which the contraction criterion forbids; Theorem 3 is machine-checked in its rooted form, and Doukas states the same argument concurrently [Dou26, Prop. 1]. Two rows of a square stochastic matrix share a positive column exactly when it is not a permutation matrix, and [Main §2.3] also proves the theorem from the lemma that a finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix [BB12, Problem 23] (machine-checked). Monotone distance is necessary for P-divisibility but not sufficient [Main §2.3].

Finite recurrence supplies the return, $\Gamma_L=I$ for the order $L$ of $\varphi$:

**Corollary (recurrence-cycle indivisibility).** *Let $\varphi$ have order $L$, with one hidden prior shared by every root and drawn independently of it, and let $\Gamma_t$ keep a row for every root, roots of visible probability zero included. If some $\Gamma_s$ with $0<s<L$ is not a permutation, the rooted family is not P-divisible on $\{0,\dots,L\}$. Two distinct positive-probability visible histories of equal length with a common endpoint, in particular a memory witness, supply such a $\Gamma_s$, and so does every non-deterministic visible step, also when the law is Markov on every accessible window. With a full-support visible prior, this failure is equivalent to $M_k>0$ at some order $k<L$.*

In plain terms: in a finite reversible world whose hidden part starts with the same odds whatever is visible at the start, the whole system eventually returns to its starting configuration, and the forecasts from the start return to certainty with it. If at some earlier time the forecasts from two different starting points overlap, as they do after any visible step that is not fully predictable, no chain of step-by-step forecasts can lead back to certainty, so the forecasts cannot be chained somewhere in the cycle. The forecasts in question are those from every possible starting point, including starting points that never occur; when every starting point has positive probability, this happens exactly when the record has memory at some step before the return.

This is [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility) and Scope]: the first sentence is Theorem 3 with $n=L$, since two rows of a non-permutation $\Gamma_s$ share a positive column, and Theorem 3 is machine-checked in its rooted form; the supply of a non-permutation $\Gamma_s$ is proved on paper. For the equivalence, a memory witness below $L$ gives a non-permutation $\Gamma_s$; conversely, with none the law on $\{0,\dots,L\}$ is Markov, $\Gamma_L=I$ makes every $\Gamma_s$ a permutation by the stochastic-inverse lemma, and $\Gamma_s^{-1}\Gamma_t$ is a stochastic divisor, full support being needed only in this converse. Indivisibility at some return horizon is also machine-checked from the *routed* form of (C4), the realization clause in which a record of the visible history written into the hidden state is routed back into later visible conditionals within the window [Main §1.3].

Recurrence-cycle indivisibility thus needs only finite reversibility and one non-deterministic visible step, and holds also for laws that are Markov on every accessible window, so it does not separate them from memory-bearing laws at accessible orders; what an observer can discriminate is memory at an accessible order, which (C4) asserts [Main §2.3, Scope].

### 2.6 Three examples

**A minimal model.** Let $\mathcal C_V=\{0,1\}$ and $\mathcal C_H=\{1,\dots,6\}$ [Main §2.4]. For $h\in\{1,2\}$, $\varphi$ swaps $(0,h)$ with $(1,h)$: it flips the visible bit and keeps $h$, which then records the flip. At fixed $x$, $\varphi$ swaps $h=3$ with $4$, and $5$ with $6$. A second application reads the record and flips the bit back. With $h$ uniform,
$$
\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\qquad \Gamma_2=I,\qquad
\Gamma_1^{-1}\Gamma_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$
The only candidate divisor has negative entries, so the family is P-indivisible, whereas a Markov chain with the same one-step matrix would give $\Gamma_1^2$, with diagonal entries 5/9 and off-diagonal entries 4/9. With $x_0$ uniform and independent of $h$, $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$ while $P(x_2{=}0\mid x_1{=}1)=1/3$; for $P(x_0{=}0)=a$, the second value is $a/(2-a)$.

**Memory without short-window indivisibility.** Let $X_0$ and $X_1$ be independent uniform bits and $X_2=X_0\oplus X_1$. Every two-time transition matrix is $\tfrac12J$, with $J$ the all-ones matrix, so the family factors through $\Delta=I$ and is P-divisible on $\{0,1,2\}$. Yet $I(X_0;X_2\mid X_1)=1$ bit. Up to flipping the final bit, this is the process of [RHP14, Eq. (15)]; it appears concurrently in [Dou26, App. A].

**The card table.** The card analogy of §1.1 is also an exact finite model of the kind §§2.4–2.5 describe; as a picture of quantum mechanics it remains an analogy, since its statistics are classical (below). The two-card game of [Book §1.11] uses two cards, each red (0) or black (1): a visible *hole card* $x$, and a face-down *burn card* $b$, uniform and independent of $x$. One shuffle step swaps the two cards, $\varphi(x,b)=(b,x)$. A *peek* reveals the hole card and overwrites the burn card, which holds the record, with a fresh card drawn uniformly and independently. Exact enumeration of the equally likely cases gives the probability that the hole card at the final reveal is the hole card as dealt:

| Protocol | Probability |
|---|---|
| one shuffle | 1/2 |
| two shuffles | 1 |
| two shuffles, with a peek between them | 1/2 |
| Markov prediction for two shuffles, $\Gamma_1^2$ | 1/2 |

Here $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$. The two rows of $\Gamma_1$ are equal, so for every $\Delta$ the two rows of $\Gamma_1\Delta$ are equal and $\Gamma_1\Delta\neq I$: the family is P-indivisible.

The table separates the deterministic information from what the player can access. The shuffle is a bijection and loses nothing; the player sees only the hole card, and the memory the player observes, certainty after two shuffles where a Markov model predicts 1/2, is carried by the face-down card. The peek row depends on the rule: if the peek only reveals or replaces the hole card, the probability is 1, so the 1/2 comes from overwriting the record, not from looking. With anticorrelated cards ($b=1-x$), $\Gamma_1$ is a permutation and the game is divisible.

On card inputs the game is a classical stochastic process, and no card arrangement violates a Bell inequality [Book §1.11; Main §3.3].

## 3. Quantum emergence: scope and open steps

Section 2 shows that a quantum system measured in one fixed way and a partly hidden deterministic world produce the same patterns. Quantum mechanics says more. It allows measurements of different, mutually incompatible kinds, superpositions that are not mixtures of definite states, and systems combined into larger ones. The correspondence does not on its own give quantum mechanics, for three reasons: it covers only records of one fixed measurement repeated at every step; it holds for every law and so selects nothing, neither the squared form of quantum probabilities nor the evolution relating two times (§3.3), and it represents the statistics without deriving a physical mechanism; and the further ingredients are five conditions that OI does not imply (§3.2).

### 3.1 Three notions kept apart

The indivisibility of §2.5 is global: it occurs somewhere in the recurrence cycle, not on every window, and conditional memory does not force short-window indivisibility (§2.6). A revival of distinguishability within a window, two roots whose rooted laws are closer at an earlier time than at a later one, does make the family P-indivisible on that window [Main §2.3].

Three notions are distinct, and no unconditional implication holds among them [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion. A family of quantum channels $\Phi_t$ is completely-positive (CP) divisible if $\Phi_t=\Psi_{t,s}\circ\Phi_s$ with each $\Psi_{t,s}$ completely positive and trace-preserving. For the family obtained by tracing out a permutation unitary from a diagonal hidden state, (2) implies CP-indivisibility [Main §3.2, Theorem (CP-indivisibility, framework scope)]. Outside the diagonal-preserving class the implication fails: with $\Phi_{t_1}$ conjugation by the Hadamard gate and $\Phi_{t_2}=\mathrm{id}$ the family is CP-divisible, while its computational-basis populations, $\tfrac12J\to I$, are P-indivisible [Main §3.2, Remark (scope: P-indivisibility is not quantum non-Markovianity)].

In plain terms, memory in the record, failure of step-by-step chaining, and the quantum notion of memory are three different properties. A *quantum channel* is the most general way a quantum state can change, noise included, and the *Hadamard gate* is the basic operation that turns a definite 0 or 1 into an equal superposition of both; the example shows a perfectly chainable quantum evolution whose recorded populations cannot be chained.

In the card table of §2.6, embedded as a permutation unitary with the burn card in the uniform diagonal state, the one-step channel $\rho\mapsto\operatorname{tr}(\rho)\,I/2$ is entanglement-breaking (measure-and-prepare) and the two-step map is the identity, so the family is CP-indivisible [Main §3.2]; its memory is still classical in the sense of [BBS24], since the two-step identity is obtained by realizing the one-step channel as the Pauli twirl $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, $o\in\{0,x,y,z\}$, and applying $\sigma_o$ conditioned on $o$, a decomposition a fixed initial hidden card does not admit [Main §4.5].

Distinguishability backflow witnesses divisibility failure in one direction only [BLP09]; for bijective dynamical maps on a $d$-dimensional system, CP-divisibility is equivalent to monotone distinguishability with a $(d+1)$-dimensional ancilla [BJA17]. Theorem 1 states which laws admit realizations and quantum representations, not why a physical system exhibits a law with memory [Main §3.4, Remark (representation, not explanation)]; Calvo states a derivation of the textbook axioms from indivisible stochastic evolution [Cal26], whereas Theorem 1 derives no axioms.

### 3.2 From the correspondence to operational quantum mechanics

What must be added to fixed-measurement records to obtain the whole of quantum mechanics, with every kind of measurement and every way of combining systems? The answer is a list of five requirements on what an experimenter can do. An *ancilla* below is an auxiliary system brought in for an operation, and a *Kraus instrument* is the general quantum operation with outcomes.

Operational quantum mechanics requires, beyond the fixed-basis records of Theorem 1, coherent preparations, noncommuting interventions and composites represented by one instrument theory.

Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear maps are available on the system and at every ancilla level, that is, with each finite ancilla adjoined. The theory contains the identity and is closed under coarse-graining of outcomes and, at every ancilla level, under outcome-conditioned composition. It has an available preparation of a uniformly mixed ancilla, which an available operation may follow, an available spectator-independent readout of the ancilla, one that acts on every product input as the identity on the system, and ancilla discard: an available preparation followed by an available instrument, with the ancilla then discarded, is an available instrument on the system with the same outcomes [GR §3.3]. The five completion conditions are:

(i) available families send positive states to positive states, and their outcome traces sum to the input trace;
(ii) operations remain available with a one-state ancilla adjoined;
(iii) an untouched independent system can be adjoined without changing an intervention;
(iv) every finite unitary on every composite is available;
(v) attaching a fresh uniformly prepared ancilla to a composite, acting, and discarding it gives an available operation.

**Theorem 4** (operational-completion characterization [GR §3.3]). *For every nonempty finite system, the available outcome families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*

In plain terms: five concrete requirements, that probabilities make sense, that adding a trivial helper or an untouched bystander changes nothing, that every reversible quantum operation on any combined system is available, and that helpers can be added and discarded freely, are together exactly what makes the available operations those of quantum mechanics, no more and no less.

Both directions are machine-checked (Appendix A). The sufficiency direction rests on the Stinespring dilation and on the realization of every finite instrument by a unitary interaction with an ancilla followed by ancilla readout and discard [Sti55; Kra83; Oza84]; for reconstructions of finite quantum theory from operational axioms see [Har01; CDP11; MM11].

Each condition is independent of the other four and of the observation process itself: for one fixed finite embedded-observation process satisfying (C1)–(C4), and for each condition, there is a qubit theory that realizes that process and the other four conditions, and fails that condition. In particular, a qubit theory that never creates coherence realizes the observation process and is not quantum, so OI alone does not imply quantum mechanics (both machine-checked) [GR §3.3]. Which of (iii)–(v) a physical substratum supplies is the open step toward full operational equivalence.

None of the five follows from the others or from the observation setup itself. A *qubit* is the simplest quantum system, with two basic states. Hidden information and partial access therefore do not by themselves imply quantum mechanics, and whether a physical substratum supplies the missing conditions is the central open question on the route from OI to quantum mechanics.

### 3.3 The evolution relating two times is not selected

Knowing every observed pattern does not fix the quantum evolution between two times: representability does not fix the unitary evolution relating two times [Main §3.4, Remark (scope: representability, not selection of the relating evolution)]. Two coherent lifts of one visible family, unitary dilations that reproduce the visible law at every time and compose exactly across times, can differ by a time-dependent right action invisible to the visible law and then have different relating evolutions (machine-checked on an exhibited pair of lifts), while a constant deformation cancels from every relating evolution (machine-checked in general).

For lifts with trivial ancilla, read in a fixed basis, two lifts have equal rooted families exactly when their one-step visible matrices are equal, and equal one-step matrices give equal trajectory laws at every horizon; each such trajectory law is a fixed-basis Born record and stochastic (all machine-checked; the first is an equivalence). The fixed-basis correspondence therefore acts on the quotient by visible equality, and selecting the relating evolution needs a condition beyond representability and ordinary coherence.

### 3.4 No fixed finite realization reproduces a qubit

A fixed finite realization with $N$ ontic configurations generates only behaviour matrices that factor nonnegatively through $N$ states. Simulating a qubit's prepare-and-measure statistics needs classical memory unbounded over finite experiments: explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and Montina reports Hardy's result that the number of ontic states cannot be finite [Mon08; Har04]. So no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly; the factorization is proved, and the unboundedness is imported [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form); HKLP24]. The obstruction does not touch Theorem 1, whose realization is chosen per law.

In plain terms: one fixed finite hidden world can mimic any single finite pattern, but not everything one qubit can do across all possible experiments, which would need unlimited hidden memory.

### 3.5 Bell structure

Two laboratories far apart share a prepared pair of systems. Each chooses a setting, that is which measurement to make, and records an outcome $+1$ or $-1$. Bell's theorem asks whether the correlations between the two records can be explained by information the pair carried from the start, each outcome depending only on its own laboratory's setting. For any such explanation the Clauser–Horne–Shimony–Holt combination $S_{\mathrm{CHSH}}$ of the four setting-pair correlations is at most 2 in magnitude, while quantum mechanics reaches $2\sqrt2$. For a deterministic hidden world this is the sharpest test of what partial access can and cannot explain.

[Main §3.3] proves a Bell ceiling under the framework's own hypotheses. The spatial substratum is a product of finite site factors, and its coupling graph joins site $i$ to site $j$ when the $i$th output component of $\varphi$ depends on the $j$th input component, and $d_G$ is its graph distance; an intervention on a region $A$ changes, $k$ updates later, only components within $d_G$-distance $k$ of $A$ [Main §3.3]. Let $\Omega$ be a pre-setting variable that fixes each wing's response to every setting, and suppose that (i) the dynamics is deterministic; (ii) the setting operation acts at one step on disjoint regions $A$ and $B$, each intervention reading and writing only its own region; (iii) wing $A$'s outcome is a $\pm1$-valued function of the state on a readout region $R_A$, $k_A$ updates after the setting, with $d_G(B,R_A)>k_A$, and symmetrically $d_G(A,R_B)>k_B$; and (iv) the interventions act on one common pre-setting ensemble, $p(\Omega\mid a,b)=p(\Omega)$. If the protocol records a $\pm1$ outcome in every run, the model is Bell-local, with deterministic local response functions, and the Clauser–Horne–Shimony–Holt combination obeys $|S_{\mathrm{CHSH}}|\le2$ [Bel64; CHSH69; Main §3.3, Theorem (Bell ceiling for a screened local completion)]. Reproducing the quantum values $2<|S_{\mathrm{CHSH}}|\le2\sqrt2$ therefore requires violating at least one of these assumptions.

In plain terms: a deterministic world whose two laboratories cannot affect each other's results within the time of the experiment, whose settings are chosen independently of its hidden state, and which records an outcome in every run, cannot produce quantum Bell correlations.

In the framework, determinism is part of OI and the protocol records an outcome in every run, so a completion reproducing quantum Bell correlations gives up at least one of the remaining assumptions: (ii) and (iii), which with the causal-cone property secure ontic parameter independence, or (iv), measurement independence [Main §3.3]. *Ontic parameter independence* means that in the underlying (ontic) state one wing's response does not depend on the other wing's setting; *measurement independence* means that the settings are statistically independent of the pre-setting state. The framework retains measurement independence, as a posit about the initial condition, and adopts ontic parameter dependence: one wing's microstate response may depend on the remote setting, with operational no-signalling required. The nearest-neighbour cubic update of the lattice substratum [SM] alone cannot supply that dependence for wings outside each other's causal cone [Main §3.3, Corollary (Bell–lattice obstruction and state-dependent escape)]. That a preparation-indexed coupling graph, in which a Bell preparation adds bounded-degree long-range edges to the coupling graph, can supply it while preserving operational no-signalling and the gravitational continuum limit is the open hypothesis H-Bell [Main §3.3].

In plain terms: a deterministic hidden world can produce quantum Bell correlations only if one laboratory's hidden response depends on the other laboratory's choice, or if the choices are correlated in advance with the hidden state. The framework keeps the choices independent and accepts the first, on the condition that no usable signal passes between the laboratories; whether the lattice substratum can meet that condition is open.

## 4. The cosmological constant: how OI changes the interpretation of vacuum energy

Quantum theory gives empty space an energy: every field keeps a minimum jitter even in its lowest state, and adding up the energy of that jitter gives an enormous number. Gravity responds to energy, so if that energy counted in full, space would curve far more strongly than is observed. The question matters because this is the largest known mismatch between a theoretical estimate and an observation, and OI changes how the two quantities are related.

Summing zero-point energies of the quantum fields up to a Planck-scale cutoff, the smallest length at which present physics is expected to apply, gives a vacuum energy density some 120 orders of magnitude above the observational value, the exact power depending on the cutoff convention [Wei89, §I; §III, Eqs. (3.4)–(3.6)]. If that density sources curvature, it must be cancelled to that accuracy [Wei89, §III]; this discrepancy is here called the mismatch. With a Planck-scale cutoff and a Hubble-scale density the mismatch equals the de Sitter entropy up to a numerical factor fixed by the cutoff convention, a dimensional identity [GR §6.3].

**What OI establishes.** In OI the zero-point sum belongs to the emergent quantum description (§§2–3), while the effective cosmological constant $\Lambda$ belongs to the gravitational description of the substratum, with its classical stress-energy $T^{\rm cl}_{\mu\nu}$: the two are defined at different levels. A uniform shift $\hat H\to\hat H+C$ of the emergent Hamiltonian changes no visible transition probability at any precision, so the zero-point offset is absent from every visible statistic of the quantum description [GR §6.2]. That no non-gravitational measurement sees the absolute vacuum energy is familiar; what OI adds is the second level, at which a gravitational source can be defined independently of the emergent vacuum.

In plain terms: in OI the vacuum jitter belongs to the observer's quantum description, and the cosmological constant to the description of the underlying world; shifting every energy of the quantum description by the same constant changes no observable probability. That gravity responds only to the underlying world is the proposal below, and deciding it requires the field equations. Here the *stress-energy* is the energy and momentum content that sources gravity.

**The proposed resolution.** If the covariant field equations take the form [GR] targets,
$$
\mathcal G_{\mu\nu}=8\pi G\,\big(T^{\rm cl}_{\mu\nu}-\mathcal F[g,T^{\rm cl}]\,g_{\mu\nu}\big),
$$
with $\mathcal G_{\mu\nu}$ the gravitational side, still to be derived (the Einstein tensor in general relativity), and $\mathcal F$ a scalar functional of the metric and the stress-energy, then the zero-point sum of the emergent description is not a source of curvature and the mismatch requires no cancellation. The vacuum term that remains, from the substratum's classical energy density and from $\mathcal F$, is not computed, and the observed value of $\Lambda$ enters as a cosmological input.

**The missing link.** The quantum description alone cannot decide whether the offset sources curvature. The completions
$$
\mathcal G_{\mu\nu}=8\pi G\,T^{\rm cl}_{\mu\nu}
\qquad\text{and}\qquad
\mathcal G_{\mu\nu}=8\pi G\,\big(T^{\rm cl}_{\mu\nu}-\rho_C\,g_{\mu\nu}\big),
$$
with $\rho_C$ the energy density of the offset $C$, share the substratum, the partition and every visible transition law [GR §6.2]. Deciding between them requires covariant field equations derived from the substratum, with their conservation and coupling to sources, which [GR] calls the G3 coupling theorem and leaves open [GR §6.2, §8.5]; the same step fixes how the energy of electroweak and QCD vacuum transitions gravitates. A derivation of these equations would turn the proposal into a theorem or refute it.

Trace-free Einstein equations [EvEMU11] and vacuum-energy sequestering [KP14] also remove matter vacuum energy as a source of curvature, and Volovik argues that the ultraviolet zero-point sum does not set the vacuum energy [Vol06]; OI locates the gravitational source in the substratum microstate.

## 5. Black-hole information: preservation versus accessible recovery

The black-hole information problem asks whether the radiation of an evaporating black hole carries the information of what formed it [Haw76; Pag93; Pag13]. In OI two questions separate: whether information is conserved by the global dynamics, which holds because the dynamics is a bijection, and whether it can be recovered from the records an observer can access [HP07]. Finite exact computations show that these are different properties. As an analogy, a burned letter is not destroyed in principle: the smoke, ash and heat still encode its words, because the underlying laws lose nothing, yet nobody who sees only the smoke can read it. The question matters because the problem is usually posed as one of conservation, and OI shows that conservation and recovery must be answered separately.

**The toy model** [BHa]. The configuration space is a finite product of one-bit registers. A message $m$, drawn uniformly from a set $\mathcal M$, is written into designated interior registers; every other register is uniformly random and independent of $m$, or blank. One map is applied at every step, and at each *emission* one register passes from the interior to the radiation. The observer reads registers on a schedule fixed in advance and keeps every read; for the first count below, it reads the radiation registers as they are emitted. The measured quantity is $P_{\mathrm{succ}}$, the probability that the best guess of $m$ from these records is correct, and the *accessible advantage* is its excess over the blind value $1/|\mathcal M|$. $\mathcal U$ is the set of joint values of the registers left unread at the end. The layout is that of the Page-curve setup [GR App. A.7] at small size.

**Results** [BHa]. Conservation does not imply recovery: of the 40,320 bijections of $\{0,1\}^3$ with one message bit and two random bits, 1,376 give zero accessible advantage with one register unread after two emissions. Nor is it necessary: 60 non-injective maps of $\{0,1\}^2$ recover the message exactly when every register is read. What bijectivity guarantees is a floor: reading every register at the end gives exact recovery, and with $\mathcal U$ unread $P_{\mathrm{succ}}\ge1/|\mathcal U|$, so zero advantage requires $|\mathcal U|\ge|\mathcal M|$; 32 non-injective maps of $\{0,1\}^2$, with a two-bit message occupying both registers and one register read, violate this floor. It is the remnant-capacity form of the fact that $|\mathcal U|$-valued side information multiplies a guessing probability by at most $|\mathcal U|$, so hiding the message completely needs at least as many hidden values as messages, as in perfect secret sharing, of which Shamir's threshold scheme is the standard example [Sha79]. The card table of §2.6 shows the same separation in its simplest form.

In plain terms: a reversible world keeps every message, but keeping is not showing. In many reversible worlds a message stays completely hidden from an observer who reads only the radiation, which is possible only when the unread registers have at least as many joint values as there are messages; and a world that loses information can still show a message exactly.

The *entanglement entropy* of the radiation measures how strongly it is correlated with what remains of the black hole; the *Page curve* is its expected course, rising and then falling back to zero as the black hole finishes evaporating, if the information comes out.

**The Page curve.** The Page-curve calculation of [GR App. A] addresses recovery in the quantum description, on $\mathcal C_V\times\mathcal C_B\times\mathcal C_D$, with $V$ the exterior, $B$ the black-hole interior, $D$ the sector beyond the cosmological horizon, and the radiation $R\subset V$, with configurations $\mathcal C_R$, emitted from $B$ [GR App. A.1, A.7]. It rests on three conditions: *H-scramble*, that the orbit ensemble equidistributes over quantum pure states on the energy shell, which fails for every bijection acting on a definite configuration with the bipartition aligned to the configuration coordinates [BHb]; *H-decouple*, that $B\cup R$ evolves uncoupled from $D$ and from $V\setminus R$ in a pure joint state over whole cycles, which is not established: the effective-pure-state theorem [GR, Thm A.7] gives a pure joint state of $V$ and $B$ only for times short compared with the $D$-sector timescale $\tau_B^D\sim1/H$, the Hubble time [GR App. A.5], far shorter than the evaporation [BHa], and does not establish that $V\setminus R$ is unentangled with $B\cup R$ [GR App. A.7]; and constant energy on all of $\mathcal C_B\times\mathcal C_R$. Under them, for all but an exponentially small fraction of initial conditions, the full-cycle average of the radiation's entanglement entropy at each stage's bipartition equals the Page value $S_{\rm Page}(d_B,d_R)$ up to the correction term of Theorem A.8, by measure concentration [Pag93; PSW06; HLW06; GR, Thms A.8–A.9].

## 6. Established results, conditional interpretations and open problems

**Summary.** OI asks whether quantum randomness could come from an observer's partial view of a deterministic world, and the mathematics answers part of that question exactly. Over any finite number of steps, every pattern of fixed-measurement quantum records is what some partly hidden deterministic world shows. When the record has memory, the memory is held in the hidden part, which must be large enough to hold it. In a finite reversible world whose hidden part starts with the same odds whatever is visible at the start, any visible step that is not fully predictable forces, somewhere in the world's cycle, forecasts from the starting points that cannot be chained step by step. The rest of quantum mechanics, incompatible measurements and combined systems, follows exactly when five stated conditions hold, and a physical substratum is not shown to meet them; nor is the squared form of quantum probabilities selected. These results turn the opening question into precise statements about what partial access to a deterministic world does and does not produce. In the applications OI separates two levels of description for vacuum energy and separates keeping information from showing it for black holes; the gravitational field equations and the conditions of the Page-curve calculation are open.

**Established mathematical results.** Machine-checked: Theorem 1; the cores of Theorem 2 and of the capacity bound; Theorem 3 in its rooted form; Theorem 4 and the independence of its conditions; the non-selection of the relating evolution. Proved on paper, with Theorem 3 as machine-checked core and the shared-column fact and $\Gamma_L=I$ as elementary steps: recurrence-cycle P-indivisibility of the rooted visible family, with a row for every root including roots of visible probability zero and a hidden prior shared by every root and drawn independently of it, whenever some rooted transition matrix is not a permutation; that every non-deterministic visible step and every memory witness supply such a matrix, and that with a full-support visible prior the indivisibility is equivalent to $M_k>0$ at some order $k$ below the recurrence time (§2.5). Proved on paper also: the time-$t$ form of Theorem 2, its Corollary and the least hidden predictive memory; the Bell ceiling. The qubit obstruction combines a proved factorization with an imported unboundedness, and the separation of conservation from recovery rests on exhaustive enumeration with the $1/|\mathcal U|$ floor proved. Together these results establish that stochastic, quantum-like observations can arise exactly from deterministic reversible dynamics, and they locate what is not universal: the memory a law carries, its size and position in the hidden sector, and its consequence for divisibility. The correspondence represents these observations; it does not derive their physical mechanism.

**Conditional physical interpretations.** If OI holds as physics (with the bijective substratum an empirically motivated representation choice, §1.1), the fixed-basis statistics of quantum theory are the visible laws of an embedded observer, and their departures from Markov behaviour are memory carried in an inaccessible sector, as the card table of §2.6 illustrates. With measurement independence retained, quantum Bell correlations then require ontic parameter dependence, subject to H-Bell (§3.5); the zero-point sum is not a gravitational source if the field equations take the targeted form (§4); and the framework's cycle-averaged Page curve holds under H-scramble, H-decouple and with all of $\mathcal C_B\times\mathcal C_R$ one energy shell (§5).

**Open problems.** For quantum emergence:

1. full operational equivalence: which of completion conditions (iii)–(v) a physical substratum supplies (§3.2);
2. a selection principle for the quadratic Born exponent (§2.3) and for the evolution relating two times (§3.3);
3. history readback (C4) at the cosmological partition [GR §2.2], and an experiment or memory-witness test distinguishing OI from standard quantum theory [Main §4.5];
4. the dynamical construction problems: exact gluing of per-horizon realizations for recurrent target families, approximation of a target on windows short compared with the recurrence time by one fixed substratum [Main §3.4], and the hidden-sector mixing hypothesis, motivated by eigenstate thermalization, under which observed conditional memory gives a lower bound on the hidden sector's coarse-grained mixing time, the slow-bath form of (C2) [Main §1.3, §3.4];
5. machine checks of the steps of §§2.2–2.5 proved on paper.

For the applications: a derivation of the covariant field equations with their source coupling, on which both §4 and, in [GR], the Page curve depend; H-scramble and H-decouple; the proper-shell case, which an evaporating black hole whose radiation carries away its energy occupies; the entropy along a single trajectory [BHb]; the generalized second law [GR App. A.6]; and the relation to quantum-extremal-surface and island computations [Pen20; AEMM19; AMMZ20; Book §7.6] (§5).

## Code, data and formal verification

\begingroup\raggedright

The declarations in Appendix A were checked in Lean 4.33.0 with Mathlib v4.33.0 at commit `17b830bc` by building `verification/lean-mathlib` (`lake exe cache get`, `lake --rehash build`) and running `python3 tools/release_gate.py`, whose `lean-axioms` step requires every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`; each declaration reports exactly these three, and the expected result and comparison recipe are in `papers/introduction_repro/`. The full commit hash is `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86`. The Lean pin is the commit at which that result was retained; the manuscripts are cited at corpus commit `55e3217b`, whose `verification/lean-mathlib` tree is identical.

The probes and the black-hole computations [BHa; BHb] are released under the MIT License, at `papers/oi_lattice_code/foundations/` (probes; also in the release archive, concept DOI 10.5281/zenodo.19060318) and `verification/programmes/black-hole-information/` (not part of the release archive) at the corpus commit.

\endgroup

## Appendix A. Machine-checked declarations

Modules of the `OIBridge` Lean library; line numbers at commit `17b830bc`.

\begingroup\footnotesize\raggedright\setlength{\parskip}{1pt}

- **Theorem 1** (§2.2): `finite_horizon_equivalence` (Equivalence:462); directions `S_imp_D` (:422), `D_imp_Qfb` (:294), `Qfb_imp_S` (:245), compositions :466–468; supporting `permMatrix_mem_unitaryGroup` (EquivalenceChain:179). Prior independence is proved on paper.
- **Theorem 2** (§2.4): `pushforward_identity`, `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory` (HiddenMemory:83, :114, :170, :185), for a joint law of history, present and hidden state; the time-$t$ identification and the standard vanishing criterion for conditional mutual information [CT06] are proved on paper.
- **Capacity bound and least hidden memory** (§2.4): `c3_necessity`, `c3_necessity_via_hidden`, `card_hidden_ge_two_pow_Istar` (C3Necessity:80, :88, :117), for bijective realizations in the same joint-law form.
- **Stochastic-inverse lemma; Theorem 3** (§2.5): `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110); `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148).
- **Recurrence-cycle indivisibility** (§2.5): `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122), indivisibility at some return horizon from routed readback; on paper for history-level (C4).
- **Relating evolution** (§3.3): `gl2_strong_gauge_moves_relative_candidate` (CoherentLiftGauge:537, an exhibited pair of lifts), `gl3_constant_gauge_preserves_relative` (:451, general); `bridge_traj`, `rooted_eq_iff_slice_eq` (both directions: rooted families equal exactly when one-step matrices are), `realData_traj_stochastic` (TrackBQfbBridge:276, :180, :286).
- **Theorem 4** (§3.2): `exactAll_iff_physical_general` (GeneralCarrier:100); $\Rightarrow$ `physical_of_exactAll` (PhysicalCharacterization:301); $\Leftarrow$ `exactAll_of_physical_general` (GeneralCarrier:93) via `krausSoundExt_of_validity_inert` (OperationalValidity:124), `compositeCompleteness_unconditional` (IsometryExtension:179, premise discharged by `finiteIsometryExtensionSF_discharged`, :116) and `exactAll_of_levelOne` (LevelOneSeam:196).
- **Independence; OI alone does not imply quantum mechanics** (§3.2, qubit): `five_way_minimality` (RankGapTheory:702), `oi_alone_not_qm` (GeneralCarrier:160).

\endgroup

## References

\begingroup\footnotesize\raggedright\setlength{\parskip}{1pt}\setlength{\leftskip}{1.5em}\setlength{\parindent}{-1.5em}

**Corpus** (repository commit `55e3217b`, concept DOI 10.5281/zenodo.19060318)

[Main] A. Maybaum, "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation," `papers/Main.md`.

[GR] A. Maybaum, "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon," `papers/GR.md`.

[SM] A. Maybaum, "The Standard Model from a Cubic Lattice," `papers/SM.md`.

[Book] A. Maybaum, *The Incompleteness of Observation*, `book/`.

[BHa] A. Maybaum, "Recovery from accessible records in finite reversible models," unpublished research record; proofs and code at `bh01_access_v1/` in the black-hole computations' directory.

[BHb] A. Maybaum, "Permutation dynamics versus quantum scrambling; Page-time fraction," unpublished research record; proofs and code at `bh02_scramble_v1/` in the black-hole computations' directory.

**External**

[AEMM19] A. Almheiri, N. Engelhardt, D. Marolf, and H. Maxfield, "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole," *J. High Energy Phys.* **12**, 063 (2019); arXiv:1905.08762.

[AMMZ20] A. Almheiri, R. Mahajan, J. Maldacena, and Y. Zhao, "The Page curve of Hawking radiation from semiclassical geometry," *J. High Energy Phys.* **03**, 149 (2020); arXiv:1908.10996.

[Bar23] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085v2 (2023).

[Bar25] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778v3.

[Bar26] J. A. Barandes, "The Born Representation Theorem and the Unistochastic Theorem," arXiv:2608.04354v1 (2026).

[BB12] J. C. Baez and J. Biamonte, "Quantum techniques for stochastic mechanics," arXiv:1209.3632v5 (2012).

[BBS24] C. Bäcker, K. Beyer, and W. T. Strunz, "Local disclosure of quantum memory in non-Markovian dynamics," *Phys. Rev. Lett.* **132**, 060402 (2024); arXiv:2310.01205v2.

[BD16] F. Buscemi and N. Datta, "Equivalence between divisibility and monotonic decrease of information in classical and quantum stochastic processes," *Phys. Rev. A* **93**, 012101 (2016); arXiv:1408.7062v3.

[Bel64] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195 (1964).

[BJA17] B. Bylicka, M. Johansson, and A. Acín, "Constructive method for detecting the information backflow of non-Markovian dynamics," *Phys. Rev. Lett.* **118**, 120501 (2017); arXiv:1603.04288v2.

[BLP09] H.-P. Breuer, E.-M. Laine, and J. Piilo, "Measure for the degree of non-Markovian behavior of quantum processes in open systems," *Phys. Rev. Lett.* **103**, 210401 (2009); arXiv:0908.0238v2.

[Cal26] S. Calvo, "On the stochastic-quantum correspondence," *Quantum Stud. Math. Found.* **14**, 2 (2026), doi:10.1007/s40509-026-00415-9; arXiv:2601.18720v2.

[CDP11] G. Chiribella, G. M. D'Ariano, and P. Perinotti, "Informational derivation of quantum theory," *Phys. Rev. A* **84**, 012311 (2011).

[CHSH69] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, "Proposed experiment to test local hidden-variable theories," *Phys. Rev. Lett.* **23**, 880 (1969).

[CT06] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006).

[dMU21] L. de Moura and S. Ullrich, "The Lean 4 theorem prover and programming language," in *Proc. CADE 28* (Springer, 2021), p. 625.

[Dou26] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095v3 (2026).

[EGGH26] G. Egri, M. Gömöri, B. Gyenis, and G. Hofer-Szabó, "Trajectory of probabilities, probability on trajectories, and the stochastic-quantum correspondence," arXiv:2602.23491v1 (2026).

[EvEMU11] G. F. R. Ellis, H. van Elst, J. Murugan, and J.-P. Uzan, "On the trace-free Einstein equations as a viable alternative to general relativity," *Class. Quantum Grav.* **28**, 225007 (2011); arXiv:1008.1196v2.

[GH03] E. F. Galvão and L. Hardy, "Substituting a qubit for an arbitrarily large number of classical bits," *Phys. Rev. Lett.* **90**, 087902 (2003); arXiv:quant-ph/0110166v3.

[Har01] L. Hardy, "Quantum theory from five reasonable axioms," arXiv:quant-ph/0101012 (2001).

[Har04] L. Hardy, "Quantum ontological excess baggage," *Stud. Hist. Philos. Mod. Phys.* **35**, 267 (2004).

[Haw76] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).

[HKLP24] T. Heinosaari, O. Kerppo, L. Leppäjärvi, and M. Plávala, "Simple information processing tasks with unbounded quantum advantage," *Phys. Rev. A* **109**, 032627 (2024); arXiv:2308.07727v4.

[HLW06] P. Hayden, D. W. Leung, and A. Winter, "Aspects of generic entanglement," *Commun. Math. Phys.* **265**, 95 (2006); arXiv:quant-ph/0407049.

[HP07] P. Hayden and J. Preskill, "Black holes as mirrors: quantum information in random subsystems," *J. High Energy Phys.* **09**, 120 (2007); arXiv:0708.4025.

[KP14] N. Kaloper and A. Padilla, "Sequestering the Standard Model vacuum energy," *Phys. Rev. Lett.* **112**, 091304 (2014); arXiv:1309.6562v2.

[Kra83] K. Kraus, *States, Effects, and Operations*, Lecture Notes in Physics **190** (Springer, 1983).

[LP17] D. A. Levin and Y. Peres, with contributions by E. L. Wilmer, *Markov Chains and Mixing Times*, 2nd ed. (American Mathematical Society, 2017).

[Mathlib20] The mathlib Community, "The Lean mathematical library," in *Proc. ACM SIGPLAN Conf. Certified Programs and Proofs* (ACM, 2020), p. 367.

[Milz20] S. Milz, D. Egloff, P. Taranto, T. Theurer, M. B. Plenio, A. Smirne, and S. F. Huelga, "When is a non-Markovian quantum process classical?," *Phys. Rev. X* **10**, 041049 (2020); arXiv:1907.05807v3.

[MM11] Ll. Masanes and M. P. Müller, "A derivation of quantum theory from physical requirements," *New J. Phys.* **13**, 063001 (2011).

[Mon08] A. Montina, "Exponential complexity and ontological theories of quantum mechanics," *Phys. Rev. A* **77**, 022104 (2008); arXiv:0711.4770v2.

[Oza84] M. Ozawa, "Quantum measuring processes of continuous observables," *J. Math. Phys.* **25**, 79 (1984).

[Pag93] D. N. Page, "Average entropy of a subsystem," *Phys. Rev. Lett.* **71**, 1291 (1993); arXiv:gr-qc/9305007v2.

[Pag13] D. N. Page, "Time dependence of Hawking radiation entropy," *J. Cosmol. Astropart. Phys.* **09**, 028 (2013); arXiv:1301.4995v3.

[Pen20] G. Penington, "Entanglement wedge reconstruction and the information paradox," *J. High Energy Phys.* **09**, 002 (2020); arXiv:1905.08255v3.

[PSW06] S. Popescu, A. J. Short, and A. Winter, "Entanglement and the foundations of statistical mechanics," *Nature Phys.* **2**, 754 (2006).

[RHP14] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014); arXiv:1405.0303v2.

[Sch21] H.-J. Schmidt, "Dilation of stochastic matrices by coarse graining," arXiv:2106.03513v1 (2021).

[SGD19] P. Strasberg and M. García Díaz, "Classical quantum stochastic processes," *Phys. Rev. A* **100**, 022120 (2019); arXiv:1905.03018v2.

[Sha79] A. Shamir, "How to share a secret," *Commun. ACM* **22**, 612 (1979).

[Sti55] W. F. Stinespring, "Positive functions on C\*-algebras," *Proc. Amer. Math. Soc.* **6**, 211 (1955).

[tH14] G. 't Hooft, "The cellular automaton interpretation of quantum mechanics," arXiv:1405.1548v3 (2014).

[Vol06] G. E. Volovik, "Vacuum energy: myths and reality," *Int. J. Mod. Phys. D* **15**, 1987 (2006); arXiv:gr-qc/0604062v4.

[Wei89] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).

\endgroup
