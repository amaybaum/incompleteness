% Observational Incompleteness: From Deterministic Dynamics to Quantum Observations
% Alex Maybaum
% October 2026

**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

***

## Abstract

Observational incompleteness (OI) is the hypothesis that every physical observer is a proper part of a finite reversible deterministic system and records only the visible marginals of its dynamics. At every finite horizon, three classes of law on visible trajectories coincide: all finite stochastic laws, the visible marginals of finite reversible dynamics, and the records of finite unitary systems measured in one fixed basis. Stochastic, quantum-like records can therefore arise exactly from deterministic dynamics. The components of this correspondence are known (Egri et al.; Barandes); it is stated here as one machine-checked theorem. Because Markov laws lie in every class, the discriminating content is memory. Every faithful realization carries the law's conditional memory in its hidden state. On a fixed finite reversible system the observed process is stochastically indivisible somewhere in its recurrence cycle whenever a visible transition map from the initial time is not a permutation, which every non-deterministic visible step supplies. Exact finite operational quantum mechanics is characterized by five completion conditions that OI alone does not imply. Applied to the cosmological constant, OI places the zero-point sum and the effective cosmological constant at different levels of description; applied to black-hole information, it separates conservation from accessible recovery. Open are the completion conditions a physical substratum supplies, the Born exponent, and the gravitational field equations.

## 1. Introduction: Observational Incompleteness and the emergence of quantum behaviour

### 1.1 Embedded observation

An observer inside a closed system registers only part of its configuration. If the whole evolves by a bijection, hidden states compatible with the same visible state send it to different futures, so the visible sector evolves stochastically although the whole evolves deterministically.

This is modelled by a triple $(S,\varphi,V)$ [Main §1.2]: a finite total system $S=\mathcal C_V\times\mathcal C_H$ of observer configurations $\mathcal C_V$ and complement configurations $\mathcal C_H$, a bijection $\varphi$ of $S$, and an observer $V$ that registers $x\in\mathcal C_V$ and not $h\in\mathcal C_H$. The bijection is the reversible representative of the hidden dynamics, motivated by observed near-unitarity, and finiteness of all of $S$ is posited [Main §1.2, Remark (status of the early commitments)]. The finite reversible system $(S,\varphi)$ is the *substratum*.

Observational incompleteness (OI) is the physical hypothesis that every physical observer is in this situation. Here incompleteness means that the hidden sector is inaccessible. It is not joint unsharpness of non-commuting observables: it is present for a single fixed readout, and no uncertainty relation constrains fixed-readout visible laws [Main §3.4].

### 1.2 The idea and its consequences

Marginalizing a reversible dynamics over an unobserved register can produce stochastic laws, conditional memory, and failures of stochastic divisibility, in which no stochastic map carries an earlier visible transition matrix to a later one (when the earlier matrix is invertible, the unique candidate has a negative entry). The stochastic–quantum correspondence relates these features to quantum theory [Bar23; Bar25], and at the level of finite-horizon observable laws it is exact and universal (Theorem 1, §2.2): every finite stochastic law, every fixed-basis quantum record among them, is the visible marginal of a finite reversible deterministic system. Apparently stochastic, quantum-like observations can therefore arise exactly from deterministic dynamics. The correspondence represents such observations without deriving their physical mechanism, and because it is universal, the discriminating content lies in where the memory of a law must sit (§2.4) and in what finite recurrence does with it (§2.5). Section 3 states how far the correspondence reaches toward operational quantum mechanics, §§4–5 give two applications, and §6 separates established results, conditional interpretations and open problems. Proofs, the status ledger and the probe code are in [Main], which this paper introduces; gravitational applications are in [GR] and [Book].

**Contributions.** The paper is expository and claims no new theorem. The components of Theorem 1 are known [EGGH26; Bar23; Bar25; Bar26; SGD19] and are attributed direction by direction in §2.2. The memory bounds of §2.4 are forms of the data-processing and Pinsker inequalities, and the recurrence argument of §2.5 combines finite order with the contraction criterion for divisibility [RHP14; BD16], stated concurrently by Doukas [Dou26]. The results of §3.2–§3.3 are proved in [GR] and [Main], and the black-hole results of §5 in unpublished repository research records with exact or exhaustive checks [BHa; BHb]; the novelty of neither has been assessed. Deterministic systems have been analysed with quantum methods before, for example in [tH14].

*Conventions.* "Machine-checked" means checked in Lean 4/Mathlib [dMU21; Mathlib20] at commit `17b830bc` by the recipe under "Code, data and formal verification" (declarations in Appendix A); "proved on paper" means a written proof without a machine check; an "exact probe" is an exhaustive computation in exact rational arithmetic at small size. A *faithful realization* of a law is a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$ with an initial law under which the visible trajectory has that law.

## 2. Theoretical foundation: the established results and their assumptions

### 2.1 Setting

Fix finite sets $\mathcal C_V$ (with $|\mathcal C_V|\ge2$) and $\mathcal C_H$, a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$, and a horizon $K$. A law is a probability distribution on visible trajectories $(x_0,\dots,x_K)\in\mathcal C_V^{K+1}$. In a realization, $X_t$ and $H_t$ are the visible and hidden coordinates at time $t$, $X_{<t}=(X_0,\dots,X_{t-1})$ is the visible past and $X_{>t}=(X_{t+1},\dots,X_K)$ the visible future. Information is measured in bits, and $\|p-q\|_{\mathrm{TV}}=\tfrac12\sum_k|p_k-q_k|$ is the total-variation distance.

The visible law of a realization depends on the dynamics, the partition and the initial law; the prior is part of the realization datum, not selected by invariance under $\varphi$, and the counting measure is a maximal-entropy default [Main §1.2, Remark (the measure as a realization datum)].

Three classes of law are compared [Main §3.4]:

- **$\mathsf S_K$**: all probability distributions on $\mathcal C_V^{K+1}$.
- **$\mathsf D_K$**: the visible trajectory laws of a bijection of $\mathcal C_V\times\mathcal C_H$, for some finite $\mathcal C_H$, under an initial law that may correlate the visible and hidden coordinates.
- **$\mathsf Q_K$**: the *fixed-basis Born records*, the laws of finite-dimensional unitary systems read out by projective Born measurement in one fixed basis at every step, from an initial state diagonal in that basis, the record being a fixed function of each outcome.

### 2.2 The finite-horizon correspondence

**Theorem 1** (finite-horizon stochastic–reversible–unitary equivalence [Main §3.4]). *For every finite visible alphabet and every finite horizon $K$,*
$$
\mathsf S_K=\mathsf D_K=\mathsf Q_K ,
$$
*so each class is the set of all probability laws on $\mathcal C_V^{K+1}$.*

Theorem 1 is machine-checked: the three inclusions $\mathsf S_K\subseteq\mathsf D_K\subseteq\mathsf Q_K\subseteq\mathsf S_K$ and their compositions, with no construction entering as a hypothesis (Appendix A).

**Realization.** For $\mathsf S_K\subseteq\mathsf D_K$ the realization stores a sampled trajectory, with a clock, in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]. Every law also has a realization whose hidden prior is independent of $x_0$: by the finite-horizon process dilation for laws whose conditional kernels at positive-probability histories are rational, the visible initial law being arbitrary, and by its response-table extension for arbitrary kernels [Main §3.4, Theorem (finite-horizon process dilation) and its Extension]. Both are proved on paper, with exact probes.

**Quantum representation.** For $\mathsf D_K\subseteq\mathsf Q_K$ the representation is the permutation unitary $U_\varphi|x,h\rangle=|\varphi(x,h)\rangle$, read out in the configuration basis at every step [Main §3.4]; $\mathsf Q_K\subseteq\mathsf S_K$ is the Born rule.

**Attribution.** The trajectory-labelling realization is that of Egri et al. [EGGH26, Prop. 13], packaged as one iterated bijection; the independent-prior form is their Prop. 16, without reversibility, and its Markov one-step case is the random-mapping representation [LP17, Prop. 1.5]. A permutation dynamics is a special case of a unistochastic process, one whose transition probabilities are $|U_{ij}|^2$ for a unitary $U$ [Bar25, p. 12 of arXiv v3; Bar23 §4.3; Bar26 §4], and the one-step $n^2$-dimensional ancilla dilation of [Main §3.1], $n=|\mathcal C_V|$, coincides with the constructions of Barandes [Bar26, Thm 3.3] and Schmidt [Sch21, Thm 2]. The every-step projectively measured record as a probability law is in [SGD19, Eq. (3)]; that work and [Milz20] study whether such records are consistent with omitting measurements, a question $\mathsf Q_K$, which measures at every step, does not meet.

### 2.3 Scope of the correspondence

Markov laws lie in all three classes, so neither a finite reversible realization nor a fixed-basis unitary representation distinguishes a law with memory from one without [Main §3.4, Remark (what this equivalence does and does not say)].

The relation $p=|U|^2$ is part of the definition of $\mathsf Q_K$, not an output. The unitaries supplied are permutations, with entries 0 and 1, so the recovered table is the same for $|U|^q$ at every $q>0$, and the quadratic exponent is not selected [Main §3.4; Bar26, Thm 3.1].

A finite bijection has finite order $L$, so one fixed realization has an $L$-periodic multi-time law: the correspondence holds per horizon, and a nonperiodic law has no exact all-time realization by one fixed finite substratum [Main §3.4].

### 2.4 Where the memory lives

Write $M_t := I(X_{<t};X_{t+1}\mid X_t)$ for the conditional memory at time $t$. In a realization, write $f_x(h)=\pi_V(\varphi(x,h))$, with $\pi_V$ the projection onto $\mathcal C_V$, and $\mu_\omega$ for the hidden posterior after a positive-probability visible history $\omega=(x_0,\dots,x_t)$ ending at $x_t=x$.

**Theorem 2** (unavoidable hidden predictive memory [Main §3.4]). *In every faithful realization:*

*(a) $P(X_{t+1}\mid\omega)=(f_x)_\#\mu_\omega$;*

*(b) for histories $\omega,\omega'$ ending at $x$,*
$$
\|P(X_{t+1}\mid\omega)-P(X_{t+1}\mid\omega')\|_{\mathrm{TV}}\le\|\mu_\omega-\mu_{\omega'}\|_{\mathrm{TV}} ;
$$

*(c) $M_t\le I(X_{<t};H_t\mid X_t)\le\log_2|\mathcal C_H|$.*

(a)–(c) are machine-checked for a joint law of history, present and hidden state; their identification with a realization's time-$t$ law is proved on paper [Main §3.4, Theorem (unavoidable hidden predictive memory); CT06].

A *memory witness* at $t$ is a pair of positive-probability histories ending at the same $x_t$ with different next-step laws; by the vanishing criterion for conditional mutual information [CT06], a law has one exactly when $M_t>0$.

**Corollary** (proved on paper [Main §1.5]). $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards. The forward direction rests on Theorem 2(a) in each realization; the converse on Theorem 2(a) in one realization, which Theorem 1 supplies (`S_imp_D`); both use the standard vanishing criterion for conditional mutual information [CT06], which, like the time-$t$ identification, is not machine-checked.

The hidden sector also has a minimum size and a minimum memory. A realization of a law whose conditional past–future information $I(X_{<t};X_{>t}\mid X_t)$ reaches $I^*$ needs $|\mathcal C_H|\ge2^{I^*}$ (machine-checked in the joint-law form of Theorem 2). Over deterministic completions, not required to be bijective, the least hidden predictive memory $I(X_{<t};H_t\mid X_t)$ is exactly $I(X_{<t};X_{>t}\mid X_t)$, attained by the canonical predictive quotient, and it equals $M_t$ exactly when $I(X_{<t};X_{>t+1}\mid X_t,X_{t+1})=0$; every bijective realization run from time 0 carries $H(X_{<t}\mid X_t)$, Markov laws included [Main §3.4, Remark (a variational question)]. The lower bound is machine-checked for bijective realizations, in the same joint-law form, and proved on paper for non-injective ones. Conversely, memory has a floor: if two values of $X_{<t}$ followed by a common present state $X_t$, each of joint probability at least $p_0$, induce next-step laws at total-variation distance at least $\delta$, then $M_t\ge p_0\delta^2/\ln2$, by Pinsker's inequality (proved on paper, with exact probes) [Main §2.3, Lemma (accessible conditional memory from readback); CT06].

Four conditions on a hidden sector are named in [Main §1.3]: (C1) influence, (C2) persistence of records, (C3) capacity, and (C4) history readback, in which two histories with the same present induce different next-step laws. They are diagnostics of a realization, not hypotheses of Theorem 1. In a faithful realization (C4) coincides with $M_t>0$ by the vanishing criterion, and the Corollary places it in the hidden state; (C1) follows from (C4), and (C3) holds in every faithful realization by the capacity bound above. (C2) has two forms. (C2-structural), the persistence of a stored record until its readback, holds by reversibility in every bijective realization and constrains coarse-grained descriptions of the hidden sector. (C2-slow), a hidden mixing time long compared with the accessible window, is one physical mechanism for it; fast hidden dynamics that conserves the record is another [Main §1.3].

### 2.5 Recurrence and indivisibility

Fix one hidden prior shared by every root, and write $\Gamma_t$ for the *rooted* visible transition matrix from time 0 to time $t$, with a row for every $x_0\in\mathcal C_V$, roots of visible probability zero included. The family is *P-divisible on $\{0,\dots,n\}$* if for all $s<t\le n$ some stochastic $\Delta_{s,t}$ satisfies $\Gamma_t=\Gamma_s\Delta_{s,t}$. A stochastic divisor contracts total variation, so under P-divisibility $\|\delta_a\Gamma_t-\delta_b\Gamma_t\|_{\mathrm{TV}}$, with $\delta_a$ the point mass at $a$, cannot increase. This is the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1].

**Theorem 3** (recurrence and overlap [Main §2.3]). *Let $\varphi$ be a bijection of $\mathcal C_V\times\mathcal C_H$ with one hidden prior shared by every root. If two rows of $\Gamma_s$ have a positive entry in a common column and $\Gamma_n=I$ for some $n>s$, the family is not P-divisible on $\{0,\dots,n\}$.*

Two such rows are at total-variation distance below 1 at time $s$ and exactly 1 at time $n$, which the contraction criterion forbids: Theorem 3 is that criterion applied once [RHP14, Thm 2.4], machine-checked in its rooted form, and Doukas states the same argument concurrently [Dou26, Prop. 1]. Two rows of a square stochastic matrix share a positive column exactly when it is not a permutation matrix, and [Main §2.3] proves the theorem from the lemma that a finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix [BB12, Problem 23] (machine-checked). Monotone distance is necessary for P-divisibility but not sufficient [Main §2.3].

Finite recurrence supplies the return: $\Gamma_L=I$ for the order $L$ of $\varphi$. A non-permutation rooted map is supplied by any two distinct positive-probability visible histories with a common endpoint, so by a (C4) gap, and by every non-deterministic visible step, laws that are Markov on every accessible window included [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]. With a full-support visible prior, failure of P-divisibility on $\{0,\dots,L\}$ is equivalent to $M_k>0$ at some order $k<L$; an observer sees that memory only at an accessible order, which is what (C4) asserts [Main §2.3, Scope]. The step from two histories with a common endpoint to a non-permutation rooted map, and its composition with P-divisibility, are proved on paper. The conclusion is machine-checked from the *routed* form of (C4), in which a record of the visible history written into the hidden state is routed back into later visible conditionals within the window, the realization clause of (C4) [Main §1.3].

### 2.6 Three examples

**A minimal model.** Let $\mathcal C_V=\{0,1\}$ and $\mathcal C_H=\{1,\dots,6\}$ [Main §2.4]. For $h\in\{1,2\}$, $\varphi$ swaps $(0,h)$ with $(1,h)$: it flips the visible bit and keeps $h$, which then records the flip. At fixed $x$, $\varphi$ swaps $h=3$ with $4$, and $5$ with $6$. A second application reads the record and flips the bit back. With $h$ uniform,
$$
\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\qquad \Gamma_2=I,\qquad
\Gamma_1^{-1}\Gamma_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$
The only candidate divisor has negative entries, so the family is P-indivisible, whereas a Markov chain with the same one-step matrix would give $\Gamma_1^2$, with diagonal entries 5/9. With $x_0$ uniform and independent of $h$, $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$ while $P(x_2{=}0\mid x_1{=}1)=1/3$.

**Memory without short-window indivisibility.** Let $X_0$ and $X_1$ be independent uniform bits and $X_2=X_0\oplus X_1$. Every two-time transition matrix is $\tfrac12J$, with $J$ the all-ones matrix, so the family factors through $\Delta=I$ and is P-divisible. Yet $I(X_0;X_2\mid X_1)=1$ bit. Up to flipping the final bit, this is the process of [RHP14, Eq. (15)]; it appears concurrently in [Dou26, App. A].

**The card table.** The two-card game of [Book §1.11] uses two cards, each red (0) or black (1): a visible *hole card* $x$, and a face-down *burn card* $b$, uniform and independent of $x$. A *street* is one shuffle step, in which the two cards trade places, $\varphi(x,b)=(b,x)$. A *peek* reveals the hole card and overwrites the burn card, which holds the record, with a fresh card drawn uniformly and independently. Exact enumeration of the equally likely cases gives the probability that the hole card at the final reveal is the hole card as dealt:

| Protocol | Probability |
|---|---|
| one shuffle | 1/2 |
| two shuffles | 1 |
| two shuffles, with a peek between them | 1/2 |
| Markov prediction for two shuffles, $\Gamma_1^2$ | 1/2 |

Here $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$. The two rows of $\Gamma_1$ are equal, so for every $\Delta$ the two rows of $\Gamma_1\Delta$ are equal and $\Gamma_1\Delta\neq I$: the family is P-indivisible.

The table separates the deterministic information from what the player can access. The shuffle is a bijection and loses nothing; the player sees only the hole card, and the memory the player observes, certainty after two shuffles where a Markov model predicts 1/2, is carried by the face-down card. The peek row depends on the rule: if the peek only reveals or replaces the hole card, the probability is 1, so the 1/2 comes from overwriting the record, not from looking. With anticorrelated cards ($b=1-x$), $\Gamma_1$ is a permutation and the game is divisible.

On card inputs the game is a classical stochastic process, and its P-indivisibility is notion (2) of §3.1. Embedded as a permutation unitary with the burn card in the uniform diagonal state, its one-step channel $\rho\mapsto\operatorname{tr}(\rho)\,I/2$ is entanglement-breaking and its two-step map is the identity, so the family is CP-indivisible [Main §3.2]. Its memory is nevertheless classical in the sense of Bäcker, Beyer and Strunz [BBS24]: the second map is an instrument realizing the first, $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$ with $o\in\{0,x,y,z\}$, followed by the channels $\rho\mapsto\sigma_o\rho\sigma_o$ conditioned on $o$; with the hidden slot initialized to a fixed card instead, the swap admits no such decomposition [Main §4.5]. No card arrangement violates a Bell inequality [Book §1.11; Main §3.3].

## 3. Quantum emergence: scope and open steps

### 3.1 Three notions kept apart

The indivisibility of §2.5 is global: it occurs somewhere in the recurrence cycle, not on every window, and conditional memory does not force short-window indivisibility (§2.6). A revival of distinguishability within a window, two roots whose rooted laws are closer at an earlier time than at a later one, does make the family P-indivisible on that window [Main §2.3].

Three notions are distinct, and no unconditional implication holds among them [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion. A family of quantum channels $\Phi_t$ is completely-positive (CP) divisible if $\Phi_t=\Psi_{t,s}\circ\Phi_s$ with each $\Psi_{t,s}$ completely positive and trace-preserving. For the family obtained by tracing out a permutation unitary from a diagonal hidden state, (2) implies CP-indivisibility [Main §3.2, Theorem (CP-indivisibility, framework scope)]. Outside the diagonal-preserving class the implication fails: with $\Phi_{t_1}$ conjugation by the Hadamard gate and $\Phi_{t_2}=\mathrm{id}$ the family is CP-divisible, while its computational-basis populations, $\tfrac12J\to I$, are P-indivisible [Main §3.2, Remark (scope: P-indivisibility is not quantum non-Markovianity)]. Distinguishability backflow witnesses divisibility failure in one direction only [BLP09]; for bijective dynamical maps on a $d$-dimensional system, CP-divisibility is equivalent to monotone distinguishability with a $(d+1)$-dimensional ancilla [BJA17].

Theorem 1 states which laws admit realizations and quantum representations, not why a physical system exhibits a law with memory [Main §3.4, Remark (representation, not explanation)]; Calvo states a derivation of the textbook axioms from indivisible stochastic evolution [Cal26], whereas Theorem 1 derives no axioms.

### 3.2 From the correspondence to operational quantum mechanics

Operational quantum mechanics requires, beyond the fixed-basis records of Theorem 1, coherent preparations, noncommuting interventions and composites represented by one instrument theory.

Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear maps are available on the system and at every ancilla level, that is, with each finite ancilla adjoined. The theory contains the identity and is closed under coarse-graining of outcomes and, at every ancilla level, under outcome-conditioned composition. It has an available preparation of a uniformly mixed ancilla, which an available operation may follow, an available spectator-independent local readout of the ancilla, and ancilla discard: an available preparation followed by an available instrument, with the ancilla then discarded, is an available instrument on the system with the same outcomes [GR §3.3]. The five completion conditions are:

(i) available families send positive states to positive states, and their outcome traces sum to the input trace;
(ii) operations remain available with a one-state ancilla adjoined;
(iii) an untouched independent system can be adjoined without changing an intervention;
(iv) every finite unitary on every composite is available;
(v) attaching a fresh uniformly prepared ancilla to a composite, acting, and discarding it gives an available operation.

**Theorem 4** (operational-completion characterization [GR §3.3]). *For every nonempty finite system, the available outcome families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*

Both directions are machine-checked, for every nonempty finite system (Appendix A). The sufficiency direction rests on the Stinespring dilation and on the realization of every finite instrument by a unitary interaction with an ancilla followed by ancilla readout and discard [Sti55; Kra83; Oza84]; for reconstructions of finite quantum theory from operational axioms see [Har01; CDP11; MM11].

Each condition is independent of the other four and of the observation process itself: for one fixed finite embedded-observation process satisfying (C1)–(C4), and for each condition, there is a qubit theory that realizes that process and the other four conditions, and fails that condition. In particular, a qubit theory that never creates coherence realizes the observation process and is not quantum, so OI alone does not imply quantum mechanics (both machine-checked) [GR §3.3]. Which of (iii)–(v) a physical substratum supplies is the open step toward full operational equivalence.

### 3.3 The evolution relating two times is not selected

Representability does not fix the unitary evolution relating two times [Main §3.4, Remark (scope: representability, not selection of the relating evolution)]. Two coherent lifts of one visible family, unitary dilations that reproduce the visible law at every time and compose exactly across times, can differ by a time-dependent right action invisible to the visible law and then have different relating evolutions (machine-checked on an exhibited pair of lifts), while a constant deformation cancels from every relating evolution (machine-checked in general).

For lifts with trivial ancilla, read in a fixed basis, two lifts with the same one-step visible matrix give the same trajectory laws at every horizon, and equal rooted families give equal one-step matrices (machine-checked). The fixed-basis correspondence therefore acts on the quotient by visible equality, and selecting the relating evolution needs a condition beyond representability and ordinary coherence.

### 3.4 No fixed finite realization reproduces a qubit

A fixed finite realization with $N$ ontic configurations generates only behaviour matrices that factor nonnegatively through $N$ states. Simulating a qubit's prepare-and-measure statistics needs classical memory unbounded over finite experiments: explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and Montina reports Hardy's result that the number of ontic states cannot be finite [Mon08; Har04]. So no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly; the factorization is proved, and the unboundedness is imported [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form); HKLP24]. The obstruction does not touch Theorem 1, whose realization is chosen per law.

### 3.5 The Born exponent and Bell structure

The quadratic Born exponent, which the correspondence does not select (§2.3), is an open selection problem [Main §3.1, §3.4; Bar26, Thm 3.1].

[Main §3.3] proves a Bell ceiling under the framework's own hypotheses. The spatial substratum is a product of finite site factors, and its coupling graph joins site $i$ to site $j$ when the $i$th output component of $\varphi$ depends on the $j$th input component; $d$ is the graph distance. Let $\Omega$ be a pre-setting variable that fixes each wing's response to every setting, and suppose that (i) the dynamics is deterministic; (ii) the setting operation acts at one step on disjoint regions $A$ and $B$, each intervention reading and writing only its own region; (iii) wing $A$'s outcome is a $\pm1$-valued function of the state on a readout region $R_A$, $k_A$ updates after the setting, with $d(B,R_A)>k_A$, and symmetrically $d(A,R_B)>k_B$; and (iv) the interventions act on one common pre-setting ensemble, $p(\Omega\mid a,b)=p(\Omega)$. If the protocol records a $\pm1$ outcome in every run, the model is Bell-local, with deterministic local response functions, and the Clauser–Horne–Shimony–Holt combination obeys $|S_{\mathrm{CHSH}}|\le2$ [Bel64; CHSH69; Main §3.3, Theorem (Bell ceiling for a screened local completion)]. Reproducing the quantum values $2<|S_{\mathrm{CHSH}}|\le2\sqrt2$ therefore requires violating at least one of these assumptions.

In the framework, determinism is constitutional and the protocol records an outcome in every run, so a completion reproducing quantum Bell correlations gives up at least one of the remaining assumptions: (ii) and (iii), which with the graph's causal-cone lemma secure ontic parameter independence, or (iv), measurement independence [Main §3.3]. The framework retains measurement independence, as a posit about the initial condition, and adopts ontic parameter dependence, in which one wing's microstate response depends on the remote setting without operational signalling. Whether that choice is compatible with operational no-signalling and with the gravitational continuum limit of the substratum's coupling graph is the open hypothesis H-Bell [Main §3.3].

## 4. The cosmological constant: how OI changes the interpretation of vacuum energy

Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density some 120 orders of magnitude above the observational value, the exact power depending on the cutoff convention [Wei89, §I; §III, Eqs. (3.4)–(3.6)]. If that density sources curvature, it must be cancelled to that accuracy [Wei89, §III]; this discrepancy is here called the mismatch.

**What OI establishes.** In OI the zero-point sum belongs to the emergent quantum description (§§2–3), while the effective cosmological constant $\Lambda$ belongs to the gravitational description of the substratum, with its classical stress-energy $T^{\rm cl}_{\mu\nu}$: the two are defined at different levels. A uniform shift $\hat H\to\hat H+C$ of the emergent Hamiltonian changes no visible transition probability at any precision, so the zero-point offset is absent from every visible statistic of the quantum description [GR §6.2]. That no non-gravitational measurement sees the absolute vacuum energy is familiar; what OI adds is the second level, at which a gravitational source can be defined independently of the emergent vacuum.

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
with $\rho_C$ the energy density of the offset $C$, share the substratum, the partition and every visible transition law [GR §6.2]. Deciding between them requires covariant field equations derived from the substratum, with their conservation and coupling to sources, which [GR] names Level G3 and leaves open; the same step fixes how the energy of electroweak and QCD vacuum transitions gravitates. A derivation of these equations would turn the proposal into a theorem or refute it.

Trace-free Einstein equations [EvEMU11] and vacuum-energy sequestering [KP14] also remove the vacuum energy of matter as a source of curvature, and Volovik argues that the ultraviolet zero-point sum does not set the vacuum energy [Vol06]; OI differs in locating the gravitational source in the substratum microstate.

## 5. Black-hole information: preservation versus accessible recovery

The black-hole information problem asks whether the radiation of an evaporating black hole carries the information of what formed it [Haw76; Pag93; Pag13]. In OI two questions separate: whether information is conserved by the global dynamics, which holds because the dynamics is a bijection, and whether it can be recovered from the records an observer can access [HP07]. Finite exact computations show that these are different properties.

**The toy model** [BHa]. The configuration space is a finite product of one-bit registers. A message $m$, drawn uniformly from a set $\mathcal M$, is written into designated interior registers; every other register is uniformly random and independent of $m$, or blank. One map is applied at every step, and at each *emission* one register passes from the interior to the radiation. The observer reads fixed registers on a fixed schedule and keeps every read; the measured quantity is $P_{\mathrm{succ}}$, the probability that the best guess of $m$ from these records is correct, and the *accessible advantage* is its excess over the blind value $1/|\mathcal M|$. $\mathcal U$ is the set of joint values of the registers left unread at the end. The layout is the framework's nested-partition construction [GR App. A] at small size.

**Results** [BHa]. Conservation does not imply recovery: of the 40,320 bijections of $\{0,1\}^3$ with one message bit and two random bits, 1,376 give zero accessible advantage with one register unread after two emissions. Nor is it necessary: 60 non-injective maps of $\{0,1\}^2$ recover the message exactly when every register is read. What bijectivity guarantees is a floor: reading every register at the end gives exact recovery, and with $\mathcal U$ unread $P_{\mathrm{succ}}\ge1/|\mathcal U|$, so zero advantage requires $|\mathcal U|\ge|\mathcal M|$; 32 non-injective maps of $\{0,1\}^2$ violate this floor. It is the remnant-capacity form of the fact that $|\mathcal U|$-valued side information multiplies a guessing probability by at most $|\mathcal U|$, and its linear case is the secret-sharing threshold [Sha79]. The card table of §2.6 shows the same separation in its simplest form.

**The Page curve.** The Page-curve calculation of [GR App. A] addresses recovery in the quantum description, on $\mathcal C_V\times\mathcal C_B\times\mathcal C_D$, with $V$ the exterior, $B$ the black-hole interior, $D$ the sector beyond the cosmological horizon, and the radiation $R\subset V$, with configurations $\mathcal C_R$, emitted from $B$ [GR App. A.1, A.7]. It rests on three conditions: *H-scramble*, that the orbit ensemble equidistributes over quantum pure states on the energy shell, which fails for every bijection acting on a definite initial configuration with the bipartition aligned to the configuration coordinates [BHb]; *H-decouple*, that $B\cup R$ evolves uncoupled from $D$ and from $V\setminus R$ in a pure joint state over whole cycles, which the effective-pure-state theorem [GR, Thm A.7], valid for $t\ll\tau_B^D$ while $D$ is frozen, does not supply over the far longer evaporation [BHa]; and constant energy on all of $\mathcal C_B\times\mathcal C_R$ [GR, Thm A.8]. Under them, for all but an exponentially small fraction of initial conditions, the full-cycle time average of the radiation's entanglement entropy at the bipartition of each stage equals the Page value $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$, up to the correction term of Theorem A.8, by measure concentration [Pag93; PSW06; HLW06; GR, Thms A.8–A.9]. The research objectives are to establish H-scramble and H-decouple; the proper-shell case, which an evaporating black hole whose radiation carries away its energy occupies; the entropy along a single trajectory [BHb]; the generalized second law [GR App. A.6]; the relation to quantum-extremal-surface and island computations [Pen20; AEMM19; AMMZ20; Book §7.6]; and the covariant field equations on which [GR] makes the Page curve depend.

## 6. Established results, conditional interpretations and open problems

**Established mathematical results.** Machine-checked: Theorem 1, the exact finite-horizon correspondence; the cores of Theorem 2 and of the capacity bound; Theorem 3 in its rooted form; Theorem 4 and the independence of its five conditions; and the non-selection of the relating evolution (§§2.2–3.3). Proved on paper: the time-$t$ form of Theorem 2, its Corollary and the least hidden predictive memory (§2.4); the consequence of Theorem 3 that on a fixed finite reversible system every non-deterministic visible step makes the observed process indivisible somewhere in its recurrence cycle, and that under a full-support visible prior this indivisibility is equivalent to conditional memory below the recurrence time (§2.5); and the Bell ceiling (§3.5). The qubit obstruction combines a proved factorization with an imported unboundedness (§3.4), and the separation of conservation from accessible recovery rests on exact enumeration (§5). Together they establish that stochastic, quantum-like observations can arise exactly from deterministic reversible dynamics, and they locate what is not universal: the memory a law carries, its size and position in the hidden sector, and its consequence for divisibility. The correspondence represents these observations; it does not derive their physical mechanism.

**Conditional physical interpretations.** If OI holds as physics, a representation choice motivated empirically, the fixed-basis statistics of quantum theory are the visible laws of an embedded observer, and their departures from Markov behaviour are memory carried in an inaccessible sector, as the card table of §2.6 illustrates. With measurement independence retained, quantum Bell correlations then require ontic parameter dependence, subject to H-Bell (§3.5); the zero-point sum is not a gravitational source if the field equations take the targeted form (§4); and the framework's Page curve holds under H-scramble, H-decouple and a single energy shell (§5).

**Open problems.** For quantum emergence:

1. full operational equivalence: which of completion conditions (iii)–(v) a physical substratum supplies (§3.2);
2. a selection principle for the quadratic Born exponent (§3.5) and for the evolution relating two times (§3.3);
3. history readback (C4) at the cosmological partition [GR §2.2], and an experiment or memory-witness test distinguishing OI from standard quantum theory [Main §4.5];
4. the dynamical construction problems: exact gluing of per-horizon realizations for recurrent target families, approximation of a target on windows short compared with the recurrence time by one fixed substratum [Main §3.4], and the hidden-sector mixing hypothesis, motivated by eigenstate thermalization, under which observed conditional memory bounds the persistence time of (C2-slow) [Main §1.3, §3.4];
5. machine checks of the steps of §§2.2–2.5 proved on paper.

For the applications: a derivation of the covariant field equations with their source coupling (§4); and H-scramble, H-decouple, the Page value on a proper energy shell and along a single trajectory (§5).

Operational quantum mechanics follows exactly under five completion conditions; which of them physics supplies, the Born exponent and the gravitational field equations are the research objectives the framework poses.

## Code, data and formal verification

The declarations in Appendix A were checked in Lean 4.33.0 with Mathlib v4.33.0 at commit `17b830bc` (17b830bcd0ecc36e10eff5b9eeca03bdd7198d86), by building the Lean project in `verification/lean-mathlib` (`lake exe cache get`, `lake --rehash build`) and running `python3 tools/release_gate.py`, whose `lean-axioms` step requires every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`. Each declaration in Appendix A reports exactly these three; the expected result and the comparison recipe are in `papers/introduction_repro/`. The Lean pin is the commit at which that expected result was retained; the manuscripts are cited at the later corpus commit `55e3217b`, whose Lean sources are identical.

The probes and the black-hole computations [BHa; BHb] are released under the MIT License, at these repository paths at the corpus commit:

- `papers/oi_lattice_code/foundations/` (probes; also in the release archive, concept DOI 10.5281/zenodo.19060318);
- `verification/programmes/black-hole-information/` (black-hole computations; not part of the release archive).

## Appendix A. Machine-checked declarations

Modules of the `OIBridge` Lean library; line numbers at commit `17b830bc`.

\begingroup\small\raggedright

- **Theorem 1** (§2.2): `finite_horizon_equivalence` (Equivalence:462); directions `S_imp_D` (:422), `D_imp_Qfb` (:294), `Qfb_imp_S` (:245), compositions :466–468; supporting `permMatrix_mem_unitaryGroup` (EquivalenceChain:179). Prior independence is proved on paper.
- **Theorem 2** (§2.4): `pushforward_identity`, `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory` (HiddenMemory:83, :114, :170, :185), for a joint law of history, present and hidden state; the time-$t$ identification and the standard vanishing criterion for conditional mutual information [CT06] are proved on paper.
- **Capacity bound and least hidden memory** (§2.4): `c3_necessity`, `c3_necessity_via_hidden`, `card_hidden_ge_two_pow_Istar` (C3Necessity:80, :88, :117), for bijective realizations in the same joint-law form.
- **Stochastic-inverse lemma; Theorem 3** (§2.5): `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110); `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148).
- **Readback forces indivisibility** (§2.5): `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) for routed readback; on paper for history-level (C4).
- **Relating evolution** (§3.3): `gl2_strong_gauge_moves_relative_candidate` (CoherentLiftGauge:537, an exhibited qubit pair), `gl3_constant_gauge_preserves_relative` (:451, general); `bridge_traj`, `rooted_eq_iff_slice_eq` (its forward direction: equal rooted families give equal one-step matrices), `realData_traj_stochastic` (TrackBQfbBridge:276, :180, :286).
- **Theorem 4** (§3.2): `exactAll_iff_physical_general` (GeneralCarrier:100); $\Rightarrow$ `physical_of_exactAll` (PhysicalCharacterization:301); $\Leftarrow$ `exactAll_of_physical_general` (GeneralCarrier:93) via `krausSoundExt_of_validity_inert` (OperationalValidity:124), `compositeCompleteness_unconditional` (IsometryExtension:179, premise discharged by `finiteIsometryExtensionSF_discharged`, :116) and `exactAll_of_levelOne` (LevelOneSeam:196).
- **Independence; OI alone does not imply quantum mechanics** (§3.2, qubit): `five_way_minimality` (RankGapTheory:702), `oi_alone_not_qm` (GeneralCarrier:160).

\endgroup

## References

\begingroup\footnotesize\raggedright

**Corpus** (repository commit `55e3217b`, concept DOI 10.5281/zenodo.19060318)

[Main] A. Maybaum, "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation," `papers/Main.md`.

[GR] A. Maybaum, "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon," `papers/GR.md`.

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

[Cal26] S. Calvo, "On the stochastic-quantum correspondence," *Quantum Stud. Math. Found.* **14**, 2 (2026); arXiv:2601.18720v2.

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

[Sti55] W. F. Stinespring, "Positive functions on C*-algebras," *Proc. Amer. Math. Soc.* **6**, 211 (1955).

[tH14] G. 't Hooft, "The cellular automaton interpretation of quantum mechanics," arXiv:1405.1548v3 (2014).

[Vol06] G. E. Volovik, "Vacuum energy: myths and reality," *Int. J. Mod. Phys. D* **15**, 1987 (2006); arXiv:gr-qc/0604062v4.

[Wei89] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).

\endgroup
