# Observational Incompleteness: From Deterministic Dynamics to Quantum Observations

**Author:** Alex Maybaum  
**Date:** October 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

***

## Abstract

Observational incompleteness (OI) is the hypothesis that every physical observer is a proper part of a finite reversible deterministic system and records only the visible marginals of its dynamics. At every finite horizon, three classes of law on visible trajectories coincide: all finite stochastic laws, the visible marginals of finite reversible dynamics, and the fixed-basis Born records of finite unitary systems. The components of this correspondence are known, from the trajectory-labelling realization of Egri et al. and Barandes's treatment of permutation dynamics as unistochastic processes; it is stated here as one theorem. Each class contains the Markov laws, so representability does not distinguish a law with memory from one without, and the Born exponent is not selected. The discriminating content concerns memory: every deterministic completion carries the visible memory in its hidden state, and on a fixed finite reversible system finite recurrence turns history readback into stochastic indivisibility somewhere in the recurrence cycle (each with one step not machine-checked). Exact finite operational quantum mechanics is characterized by five completion conditions, none implied by OI alone. Open are which of these a physical substratum supplies, the selection of the evolution relating two times, and any test of the hypothesis. Applied to the cosmological constant, OI places the zero-point sum and the effective cosmological constant at different levels of description; whether the zero-point sum sources curvature depends on covariant field equations that are not derived, so this is a proposal, not a resolution. Applied to black-hole information, finite computations separate the conservation of information under bijective dynamics from its recovery by an observer with restricted access; the framework's Page curve is not established, and the information problem is not resolved.

## 1. Introduction: Observational Incompleteness and the emergence of quantum behaviour

### 1.1 Embedded observation

Embedded observation is modelled by a triple $(S,\varphi,V)$ [Main §1.2]: a finite total system $S=\mathcal C_V\times\mathcal C_H$ of observer configurations $\mathcal C_V$ and complement configurations $\mathcal C_H$, a bijection $\varphi$ of $S$, and an observer $V$ that registers $x\in\mathcal C_V$ and not $h\in\mathcal C_H$.

The bijection $\varphi$ is the reversible representative of the hidden dynamics, motivated by observed near-unitarity, and finiteness of all of $S$ is posited [Main §1.2, Remark (status of the early commitments)]. Hidden states compatible with the same $x$ send it to different futures, so the visible sector evolves stochastically although the whole evolves deterministically.

Observational incompleteness (OI) is the physical hypothesis that every physical observer is in this situation. Identifying nature with such a system is a representation choice, motivated empirically; the theorems below are mathematical, and no test of the identification at the level of memory witnesses is established [Main §4.5]. The incompleteness is inaccessibility of the hidden sector, not joint unsharpness of non-commuting observables: it is present for a single fixed readout, and no uncertainty relation constrains fixed-readout visible laws [Main §3.4].

### 1.2 The idea and its two consequences

Marginalizing a reversible dynamics over an unobserved register produces stochastic laws, conditional memory, and failures of stochastic divisibility, in which no stochastic intermediate transition map exists (where the candidate intermediate matrix exists, it has negative entries). The stochastic–quantum correspondence relates these features to quantum theory [Bar23; Bar25]. At the level of finite-horizon observable laws the correspondence of §2 (Theorem 1) is exact and universal, so the content lies in where the memory of a law must sit (§2.4) and what finite recurrence does with it (§2.5). The paper develops one idea, OI: its foundation and quantum-emergence results, which stop short of operational quantum mechanics (§§2–3), and two of its consequences, for the cosmological constant (§4) and for black-hole information (§5). Neither application is a demonstrated resolution of its problem; §6 states what would decide each. Proofs, the status ledger and the probe code are in [Main], which this paper introduces; gravitational applications are in [GR] and [Book].

**Contributions.** The paper claims no new theorem or physical result; its contribution is expository. It presents the established mathematical results of OI together, separates the mathematical correspondence from its physical interpretation, and states two consequences with their conditions and limitations. The black-hole results of §5 are reported from unpublished repository research records [BHa; BHb], with written proofs and exact or exhaustive checks, whose novelty has not been established. The components of Theorem 1 are known [EGGH26; Bar23; Bar25; Bar26; SGD19]; the paper states them as one theorem with each direction attributed. The memory bounds of §2.4 are forms of the data-processing and Pinsker inequalities. The recurrence argument of §2.5 combines finite order with the known contraction criterion for divisibility [RHP14; BD16], stated concurrently by Doukas [Dou26]. The results of §3.2–§3.3 are proved in [GR] and [Main].

*Conventions.* "Machine-checked" means checked in Lean 4/Mathlib [dMU21; Mathlib20] at commit `687e885b` by the recipe under "Code, data and formal verification" (declarations in Appendix A); "proved on paper" means a written proof without a machine check; an "exact probe" is an exhaustive computation in exact rational arithmetic at small size. A *faithful realization* of a law is a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$ with an initial law under which the visible trajectory has that law; the finite reversible system $(S,\varphi)$ is the *substratum*.

<!-- OWNER: decision 2 / retention §A.42. "Machine-checked" is the shorthand for the Lean-check claim; the owner chooses the word ("machine-checked" or "checked in Lean 4/Mathlib at commit X by recipe Y"), and an expected result must be retained beside the paper before it lands. -->

## 2. Theoretical foundation: the established results and their assumptions

This section defines three classes of finite-horizon law, shows that they coincide, identifies what the coincidence leaves (where a law's memory must sit), and states what finite recurrence does with that memory. Each result is stated with its reference; the proofs are in the cited papers.

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

**Realization.** For $\mathsf S_K\subseteq\mathsf D_K$ the realization stores a sampled trajectory, with a clock, in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]. For a law with rational probabilities, a realization whose hidden prior is independent of $x_0$ also exists [Main §3.4, Theorem (finite-horizon process dilation)]; it is proved on paper, with exact probes.

**Quantum representation.** For $\mathsf D_K\subseteq\mathsf Q_K$ the representation is the permutation unitary $U_\varphi|x,h\rangle=|\varphi(x,h)\rangle$, read out in the configuration basis at every step [Main §3.4]; $\mathsf Q_K\subseteq\mathsf S_K$ is the Born rule.

**Attribution.** The trajectory-labelling realization is that of Egri et al. [EGGH26, Prop. 13], packaged as one iterated bijection; the independent-prior form is their Prop. 16, without reversibility, and its Markov one-step case is the random-mapping representation [LP17, Prop. 1.5]. A permutation dynamics is a special case of a unistochastic process [Bar25, p. 12; Bar23 §4.3; Bar26 §4], and the one-step $n^2$-dimensional ancilla dilation of [Main §3.1] coincides with the constructions of Barandes [Bar26, Thm 3.3] and Schmidt [Sch21, Thm 2]. The every-step projectively measured record as a probability law is in [SGD19, Eq. (3)]; that work and [Milz20] study whether such records are consistent with omitting measurements, a question $\mathsf Q_K$, which measures at every step, does not meet.

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

(a)–(c) are machine-checked for a joint law of history, present and hidden state. Their identification with a realization's time-$t$ law is not machine-checked. The written proof is in [Main §3.4, Theorem (unavoidable hidden predictive memory)]; see also [CT06].

**Corollary** (proved on paper [Main §1.5]). $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards. The forward direction rests on Theorem 2(a) in each realization; the converse on Theorem 2(a) in one realization, which Theorem 1 supplies (`S_imp_D`); both use the standard vanishing criterion for conditional mutual information [CT06], which, like the time-$t$ identification, is not machine-checked.

Two further bounds tie memory to the hidden sector. A realization of a law whose conditional past–future information reaches $I^*$ needs $|\mathcal C_H|\ge2^{I^*}$ (machine-checked). If two visible histories of length $k$ with a common endpoint, each of probability at least $p_0$, induce next-step laws at total-variation distance at least $\delta$, then $I(X_{<k};X_{k+1}\mid X_k)\ge p_0\delta^2/\ln2$ (in bits), by Pinsker's inequality (proved on paper, with exact probes) [Main §2.3; CT06].

[Main §1.3] names four conditions on a hidden sector: (C1) influence, (C2) persistence of records, (C3) capacity, and (C4) history readback, in which two histories with the same present induce different next-step laws. In a faithful realization (C4) coincides with $M_t>0$, by the Corollary; (C1) and (C3) follow from it, and (C2) is a physical-regime premise. The conditions are diagnostics of a realization, not hypotheses of Theorem 1.

### 2.5 Recurrence and indivisibility

Write $\Gamma_t$ for the *rooted* visible transition matrix from time 0 to time $t$ (rows indexed by $x_0$). The family is *P-divisible on $\{0,\dots,n\}$* if for all $s<t\le n$ some stochastic $\Lambda$ satisfies $\Gamma_t=\Gamma_s\Lambda$. A stochastic divisor contracts total variation, so under P-divisibility $\|\delta_a\Gamma_t-\delta_b\Gamma_t\|_{\mathrm{TV}}$ cannot increase. This is the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1].

**Theorem 3** (recurrence and overlap [Main §2.3]). *Let $\varphi$ be a bijection of a finite set. If two rows of $\Gamma_s$ overlap in a column and $\Gamma_n=I$ for some $n>s$, the family is not P-divisible on $\{0,\dots,n\}$.*

Theorem 3 is machine-checked in its rooted form, and Doukas states the same overlap-and-return argument concurrently [Dou26, Prop. 1]. Monotone distance is necessary for P-divisibility but not sufficient [Main §2.3].

A finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix [BB12, Problem 23] (machine-checked). With this lemma, on a fixed finite reversible substratum, history readback forces indivisibility somewhere in the recurrence cycle [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]. The conclusion is machine-checked, by the route of Theorem 3, from a routed-readback form of (C4), in which a visible-history record written into the hidden state is read back later [Main §1.3, the realization clause of (C4)]; from history-level (C4) it is proved on paper.

Appendix B works a minimal model of Theorem 3 with six hidden states, a process with memory but no short-window indivisibility, and the smallest realization of Theorem 3, a two-card game, with its classical and quantum scope.

## 3. Quantum emergence: what is demonstrated, and what remains open for equivalence with quantum mechanics

### 3.1 What is demonstrated

The indivisibility of §2.5 is global: it occurs somewhere in the recurrence cycle, not on every window. Conditional memory does not force short-window indivisibility (Appendix B).

Three notions are distinct, and no unconditional implication holds among them [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion. Tracing out a permutation unitary from a diagonal hidden state gives channels that preserve diagonal states, and for them (2) implies CP-indivisibility [Main §3.2, Theorem (CP-indivisibility, framework scope)]. Outside that class the implication fails: with $\Phi_{t_1}$ conjugation by the Hadamard gate and $\Phi_{t_2}=\mathrm{id}$ the family is CP-divisible, while its computational-basis populations, $\tfrac12J\to I$ with $J$ the all-ones matrix, are P-indivisible [Main §3.2, Remark (scope: P-indivisibility is not quantum non-Markovianity)]. Distinguishability backflow witnesses divisibility failure in one direction only [BLP09]; for bijective dynamical maps on a $d$-dimensional system, CP-divisibility is equivalent to monotone distinguishability with a $(d+1)$-dimensional ancilla [BJA17].

Theorem 1 is a representation result: it states which laws admit realizations and quantum representations, not why a physical system exhibits a law with memory [Main §3.4, Remark (representation, not explanation)]. Calvo states a proof of the six axioms of textbook quantum mechanics from the single axiom that every physical system evolves according to a generally indivisible stochastic law [Cal26]; Theorem 1 is a correspondence between classes of law and derives no such axioms.

### 3.2 From the correspondence to operational quantum mechanics

Operational quantum mechanics requires, beyond Theorem 1's fixed-basis statistics, coherent preparations, noncommuting interventions and composites represented by one instrument theory.

Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear maps are available on the system and at every ancilla level [GR §3.3]. The five conditions are: (i) available families send positive states to positive states and their outcome traces sum to the input trace; (ii) operations remain available with a one-state ancilla adjoined; (iii) an untouched independent system can be adjoined without changing an intervention; (iv) every finite unitary on every composite is available; (v) attaching a fresh uniformly prepared ancilla to a composite, acting, and discarding it gives an available operation.

**Theorem 4** (operational-completion characterization [GR §3.3, Theorem (operational-completion characterization)]). *For every nonempty finite system, the available outcome families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*

Both directions are machine-checked, $\Rightarrow$ as `physical_of_exactAll` and $\Leftarrow$ as `exactAll_of_physical_general`, for every nonempty finite carrier.

On the qubit, each condition is independent of the other four and of a fixed finite observation process satisfying (C1)–(C4). For each condition there is a qubit theory that realizes that process and the other four conditions, and fails it. In particular, a qubit theory that never creates coherence realizes the observation process and is not quantum. So OI alone does not imply quantum mechanics. Which of (iii)–(v) a physical substratum supplies is open [GR §3.3].

### 3.3 The evolution relating two times is not selected

Representability does not fix the unitary evolution relating two times [Main §3.4, Remark (scope: representability, not selection of the relating evolution)]. Two coherent lifts of one visible family, unitary dilations that reproduce the visible law at every time and compose exactly across times, can differ by a time-dependent right action invisible to the visible law and then have different relating evolutions, while a constant deformation cancels from every relating evolution (both machine-checked).

Take a lift with trivial ancilla at one time, and form the fixed-basis datum whose evolution is the lift's unitary, with uniform initial law and identity readout. If two such data have the same one-step visible matrix, their root-conditioned trajectory laws agree at every horizon (`bridge_traj`); conversely, if their rooted families agree, their one-step visible matrices are equal (`rooted_eq_iff_slice_eq`, forward direction). Each such trajectory law is fixed-basis realizable and stochastic (`realData_traj_stochastic`). The fixed-basis correspondence therefore acts on the quotient by visible equality. A selection condition beyond representability and ordinary coherence would be needed, and none is supplied here.

### 3.4 No fixed finite carrier reproduces a qubit

A fixed finite realization with $N$ ontic configurations generates only behaviour matrices that factor nonnegatively through $N$ states. Simulating a qubit's prepare-and-measure statistics needs classical memory unbounded over finite experiments: explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and Montina reports Hardy's result that the number of ontic states cannot be finite [Mon08; Har04]. So no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly; the factorization is proved, and the unboundedness is imported [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form)]. The obstruction does not touch Theorem 1, whose realization is chosen per law.

### 3.5 The Born exponent and Bell structure

The origin of the quadratic Born exponent, which the correspondence does not select (§2.3), is open [Main §3.4; Bar26, Thm 3.1].

A deterministic completion that keeps pointwise causal cones and a setting-independent pre-setting ensemble is Bell-local, $|S_{\mathrm{CHSH}}|\le2$ [Bel64; CHSH69; Main §3.3], so a deterministic completion reproducing quantum Bell correlations must give up one of the two. The framework keeps measurement independence and adopts ontic parameter dependence, in which one wing's microstate response depends on the remote setting without operational signalling, and the compatibility of that choice with operational no-signalling and the gravitational continuum limit of the substratum's spatial coupling graph is the open hypothesis H-Bell [Main §3.3].

## 4. The cosmological constant: how OI might change the interpretation of vacuum energy

<!-- OWNER: landing gate (r6 re-check O2). Weinberg 1989 (Rev. Mod. Phys. 61, 1) is to be read first-hand and cited for the number in the next sentence before the paper lands. -->
Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density some 120 orders of magnitude above the observed one (the mismatch), the exact power depending on the cutoff convention; if that density sources curvature, it must be cancelled to that accuracy.

In OI (§1.1) the zero-point sum of the emergent quantum description (§§2–3) and the effective cosmological constant are defined at different levels of description. A uniform shift of the emergent Hamiltonian changes no visible transition probability, so the offset has no content in the visible statistics of the quantum description [GR §6.2]. The invariance is the familiar statement that no non-gravitational measurement sees the absolute vacuum energy; OI's proposal is that the mismatch requires no cancellation, and its content lies in how the two levels couple to geometry.

Whether the offset also fails to source curvature is a separate coupling question. Settling it requires covariant field equations derived from the substratum, with their coupling to sources (Level G3 of [GR]), which are open [GR §6.2]. The quantum description therefore does not decide between gravitational completions that differ by a term $\rho_C\,g_{\mu\nu}$, such as $\mathcal G_{\mu\nu}=8\pi G\,T^{\rm cl}_{\mu\nu}$ and $\mathcal G_{\mu\nu}=8\pi G\,(T^{\rm cl}_{\mu\nu}-\rho_C\,g_{\mu\nu})$, with $\mathcal G_{\mu\nu}$ the gravitational side of the field equations (the Einstein tensor in general relativity), $T^{\rm cl}_{\mu\nu}$ the classical stress-energy of the substratum and $\rho_C$ the energy density of the offset [GR §6.2]. The proposal that the mismatch requires no cancellation is therefore conditional on that open step.

If the covariant field equations take the form [GR] targets, $E_{\mu\nu}[g,\mathrm{OI}]=8\pi G\,(T_{\mu\nu}-\mathcal F[g,T]\,g_{\mu\nu})$, with $E_{\mu\nu}[g,\mathrm{OI}]$ the gravitational side still to be derived, $\mathcal F[g,T]$ a scalar functional of the metric and the stress-energy, and the classical stress-energy of the substratum as source, the zero-point sum of the emergent description is not a source and needs no cancellation; the vacuum term that remains, from the substratum's classical energy density and from $\mathcal F$, is not computed. It does not explain the observed value of Λ, which enters as a cosmological input. The scale $\rho\sim H_{\rm Hub}^2/G$, with $H_{\rm Hub}$ the Hubble rate, is the Friedmann normalization of the total density, and the fraction carried by Λ is an input.

With a Planck-scale cutoff the mismatch equals the de Sitter entropy up to a numerical factor fixed by the cutoff convention; this is a dimensional identity, not an independent prediction. How the energy of electroweak and QCD vacuum transitions couples to gravity is not fixed by the descriptive distinction and requires the same open coupling step.

Removing the vacuum energy of matter as a source of curvature is also the aim of the trace-free Einstein equations, which leave the observed value of Λ unexplained [EvEMU11], and of vacuum-energy sequestering, which also renders contributions from phase transitions small [KP14]; Volovik argues from the thermodynamics of quantum many-body ground states that the ultraviolet zero-point sum does not set the vacuum energy [Vol06]. The present proposal differs in locating the gravitational source in the substratum microstate, and its coupling step is open.

A derivation of the covariant field equations, with their conservation and source coupling, from the substratum would turn the proposal into a theorem or refute it. Until then the proposal reinterprets the problem and does not resolve it.

## 5. Black-hole information: preservation versus accessible recovery

The black-hole information problem asks whether the radiation of an evaporating black hole carries the information of what formed it [Haw76; Pag93; Pag13]. Because the dynamics of OI is a bijection observed through a partition (§1.1), two questions separate: whether information is conserved in the global reversible dynamics, and whether it can be recovered from the records an observer can access, its *access class*. The results below are finite computations in toy models of configurations, permutations and configuration reads. They concern the framework's nested-partition construction [GR App. A; Book §7.6], not a particular black hole.

Under OI, information is conserved in the global reversible dynamics because the dynamics is a bijection, which is a premise of the framework. Conservation neither implies nor is necessary for recovery from the records an observer can access: finite exhaustive computations exhibit bijections with no accessible advantage, that is, no gain in success probability over a blind guess, and non-injective maps with exact recovery [BHa].

Let $\mathcal U$ be the set of joint values of the registers left unread at the end and $\mathcal M$ the message set. Of the 40,320 bijections of $\{0,1\}^3$, 1,376 give zero accessible advantage for a binary message with one register unread after two emissions. For bijective dynamics, complete endpoint access gives exact recovery, and with $\mathcal U$ inaccessible $P_{\mathrm{succ}}\ge1/|\mathcal U|$, so zero advantage in a bijective instance requires $|\mathcal U|\ge|\mathcal M|$; 32 non-injective maps of $\{0,1\}^2$ violate the bound on $P_{\mathrm{succ}}$ [BHa]. These endpoint guarantees are sufficient, not necessary. The bound is the remnant-capacity form of a known fact, and its linear case is the secret-sharing threshold [BHa; Sha79].

The Page-curve calculation of [GR App. A] addresses recovery under its own conditions and is a conditional result [Book §7.6, §18.5]. Its configuration space is $\mathcal C_V\times\mathcal C_B\times\mathcal C_D$, with $V$ the exterior visible region, $B$ the black-hole interior and $D$ the sector beyond the cosmological horizon; the radiation $R$, a subsystem of $V$, is emitted from $B$ [GR App. A.1, A.7]. For all but an exponentially negligible fraction of initial conditions, the full-cycle time average of the radiation's entanglement entropy, at the bipartition of each stage held fixed, equals the Page value $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$ [Pag93; GR, Thms A.8–A.9]. This holds under the scrambling hypothesis H-scramble, that the orbit ensemble equidistributes over quantum pure states on the shell; H-scramble fails for every bijection acting on a definite initial configuration with the bipartition aligned to the configuration coordinates and is not established [GR App. A.7; BHb, C1, C6(a)–(b)]. It also needs the decoupling condition H-decouple: $B\cup R$ evolves with no coupling to $D$ or to the rest of the visible sector, $V\setminus R$, and its joint state is pure, over whole cycles of the dynamics; timescale ordering does not supply it, and it is not established [GR App. A.7]. Theorem A.8 of [GR] takes the whole configuration space $\mathcal C_B\times\mathcal C_R$ as a single energy shell. That requires the energy to be constant there, so that energy conservation places no constraint on the orbit, and it does not follow from the conservation of a Hamiltonian that takes more than one value there. An evaporating black hole whose radiation carries away its energy is in the proper-shell case, where the mean entropy depends on the shell and in general differs from the Page value; that case is open [GR App. A.7; BHb, C6(c)]. The result is a time average at a fixed bipartition, and whether the entropy along a single trajectory follows the same curve is open [GR App. A.7; BHb, C6(d)]. In the dependency ladder of [GR] the Page curve is also conditional on the covariant field equations. The generalized second law is not derived [GR App. A.6]; agreement with quantum-extremal-surface computations [Pen20] is not established; the correspondence between islands and substratum cycles is conjectural [Book §7.6]. The Page curve of [GR App. A] is therefore not established, and the black-hole information problem is not resolved here.

## 6. Discussion and conclusion: implications, limitations and decisive open tests

### 6.1 Implications

If the hypothesis holds, the fixed-basis statistics of quantum theory are the visible laws of an embedded observer, and their departures from Markov behaviour are memory carried in an inaccessible sector; whether the rest of operational quantum mechanics follows depends on completion conditions that OI does not imply (§3.2). Quantum Bell correlations are not accounted for by memory alone: with measurement independence kept, they need ontic parameter dependence, whose compatibility with operational no-signalling and the continuum limit is the open hypothesis H-Bell (§3.5). Two long-standing problems would then change form: vacuum energy becomes a question about how two levels of description couple to geometry, and black-hole information separates into conservation and accessible recovery.

### 6.2 What is not claimed

1. No derivation of quantum mechanics: Theorem 1 contains every finite law, and the Born exponent is not selected.
2. No unique selection of the operational theory: conditions (i)–(v) are not implied by OI alone, their independence is shown on the qubit, which of (iii)–(v) a physical substratum supplies is open, and the visible law does not fix the relating evolution.
3. No characterization of memory by the existence of a realization (§2.3), no identification of P-indivisibility with quantum non-Markovianity, and no claim that memory forces indivisibility on short windows (§3.1).
4. No resolution of the black-hole information problem: the Page curve of [GR App. A] is not established (§5), and the results of §5 concern finite toy models, each proved on paper or checked exhaustively at small size or by exact arithmetic. No claim is made that information reaches $D$, that [GR, Thm A.7] fails within its stated scope, or that no other decoupling argument exists.
5. No claim that the physical hypothesis is established or tested.
6. No claim that the card game (Appendix B) produces quantum rather than classical statistics: on card inputs its statistics are classical stochastic ones; under the unitary embedding its one-step channel is entanglement-breaking and its two-step family admits a classical-memory decomposition; it violates no Bell inequality.
7. No prediction of the value of Λ or $\Omega_\Lambda$, and no resolution of the cosmological constant problem: §4 is conditional on the covariant field equations.
8. No claim that the viewpoint is new: deterministic systems analysed with quantum methods have been studied before, for example in [tH14]. What the paper states are the cited theorems and their scopes.

### 6.3 Decisive open tests

For quantum emergence: whether a physical substratum supplies completion conditions (iii)–(v), and whether history readback (C4) holds at the cosmological partition [GR §2.2]; no experiment distinguishing OI from standard quantum theory, and no memory-witness constraint, is established [Main §4.5]. For the cosmological constant: a derivation of the covariant field equations with their source coupling. For black-hole information: whether H-scramble and H-decouple hold, the Page value on a proper energy shell and along a single trajectory, and, in [GR]'s ladder, the covariant field equations.

Further open problems are: (1) machine checks of the steps of §2.2, §2.4 and §2.5 that lack one; (2) whether the minimal hidden predictive memory equals $M_t$ once ledger bits that cannot influence the future are quotiented (the fixed-dimension form is false) [Main §3.4]; (3) exact gluing for recurrent target families, and approximation on windows short compared with the recurrence time [Main §3.4]; (4) (C2) necessity, which is conditional on a hidden-sector mixing hypothesis motivated by eigenstate thermalization [Main §3.4].

### 6.4 Conclusion

At every finite horizon the laws an embedded observer of a finite reversible system can record are exactly the finite stochastic laws, and exactly the fixed-basis unitary Born laws; because the representation is universal, the discriminating content lies in memory, which every deterministic completion carries in its hidden state. Exact operational quantum mechanics is reached only under completion conditions that OI alone does not imply, and representability does not select the evolution relating two times.

Applied to vacuum energy, OI proposes that the zero-point sum of the emergent description is not a gravitational source, conditional on covariant field equations that are not derived; applied to black-hole information, it separates conservation from accessible recovery, while the framework's Page curve is not established. Neither application is a demonstrated resolution of its problem.

## Code, data and formal verification

<!-- OWNER: retention §A.42. The Lean-check sentence below is an enduring certification claim. Before the paper lands, an expected result for commit 687e885b (build success, release-gate verdict, each cited declaration's #print axioms set, recipe, provenance) is retained beside the paper, or the commit is shown to fall inside an archive covered by the evidence-retention step. Placeholder: [expected-result file path]. -->
The declarations in Appendix A were checked in Lean 4/Mathlib at commit 687e885b1cfd24d6f17eee439101afc8acf07015 by the recipe `python3 tools/lean_axiom_check.py --require-lake`, which builds the Lean project and requires every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`; the expected result is in [expected-result file path].

The probes and the black-hole computations [BHa; BHb] are released under the MIT License (concept DOI 10.5281/zenodo.19060318), at these repository paths:

- `papers/oi_lattice_code/foundations/` (probes);
- `verification/programmes/black-hole-information/` (black-hole computations).

## Appendix A. Machine-checked declarations

Modules of the `OIBridge` Lean library; line numbers at commit `687e885b`.

\begingroup\small\raggedright

- **Theorem 1** (§2.2): `finite_horizon_equivalence` (Equivalence:462); directions `S_imp_D` (:422), `D_imp_Qfb` (:294), `Qfb_imp_S` (:245), compositions :466–468; supporting `permMatrix_mem_unitaryGroup` (EquivalenceChain:179). Prior independence is proved on paper.
- **Theorem 2** (§2.4): `pushforward_identity`, `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory` (HiddenMemory:83, :114, :170, :185), for a joint law of history, present and hidden state; the time-$t$ identification and the standard vanishing criterion for conditional mutual information [CT06] are not machine-checked.
- **Capacity bound** (§2.4): `c3_necessity`, `card_hidden_ge_two_pow_Istar` (C3Necessity:80, :117).
- **Stochastic-inverse lemma; Theorem 3** (§2.5): `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110); `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148).
- **Readback forces indivisibility** (§2.5): `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) for routed readback; on paper for (C4).
- **Relating evolution** (§3.3): `gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative` (CoherentLiftGauge:537, :451); `bridge_traj`, `rooted_eq_iff_slice_eq` (forward direction), `realData_traj_stochastic` (TrackBQfbBridge:276, :180, :286).
- **Theorem 4** (§3.2): `exactAll_iff_physical_general` (GeneralCarrier:100); $\Rightarrow$ `physical_of_exactAll` (PhysicalCharacterization:301); $\Leftarrow$ `exactAll_of_physical_general` (GeneralCarrier:93) via `krausSoundExt_of_validity_inert` (OperationalValidity:124), `compositeCompleteness_unconditional` (IsometryExtension:179, premise discharged by `finiteIsometryExtensionSF_discharged`, :116) and `exactAll_of_levelOne` (LevelOneSeam:196).
- **Independence; OI alone does not imply QM** (§3.2, qubit): `five_way_minimality` (RankGapTheory:702), `oi_alone_not_qm` (GeneralCarrier:160).

## Appendix B. Examples

### B.1 A minimal model

Let $\mathcal C_V=\{0,1\}$ and $\mathcal C_H=\{1,\dots,6\}$ [Main §2.4]. For $h\in\{1,2\}$, $\varphi$ swaps $(0,h)$ with $(1,h)$. It flips the visible bit and keeps $h$, which then records the flip. At fixed $x$, $\varphi$ swaps $h=3$ with $4$, and $5$ with $6$. A second application reads the record and flips the bit back. With $h$ uniform:
$$
\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\qquad \Gamma_2=I,\qquad
\Gamma_1^{-1}\Gamma_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$
The only candidate divisor has negative entries, so the family is P-indivisible. A Markov chain with the same one-step matrix would instead give $\Gamma_1^2$, with diagonal entries 5/9 and off-diagonal entries 4/9.

With $x_0$ uniform and independent of $h$, $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$ while $P(x_2{=}0\mid x_1{=}1)=1/3$. For $P(x_0{=}0)=a$, the second value is $a/(2-a)$.

### B.2 Memory without short-window indivisibility

Let $X_0$ and $X_1$ be independent uniform bits and $X_2=X_0\oplus X_1$. Every two-time transition matrix is $\tfrac12J$, so the family factors through $\Lambda=I$ and is P-divisible. Yet $I(X_0;X_2\mid X_1)=1$ bit. Up to flipping the final bit, this is the process of [RHP14, Eq. (15)]; it appears concurrently in [Dou26, App. A].

### B.3 The card table

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

On card inputs the game is a classical stochastic process, and its P-indivisibility is notion (2) of §3.1. Embed the game as a permutation unitary acting on an arbitrary hole-card state $\rho$, with the burn card in the uniform diagonal state [Main §3.2]. The one-step channel is then the constant channel $\rho\mapsto\operatorname{tr}(\rho)\,I/2$, which is entanglement-breaking [Main §3.2, Remark (failure of (C1))]. The two-step map is the identity channel. The family is therefore CP-indivisible [Main §3.2, Theorem (CP-indivisibility, framework scope)].

<!-- Source of the decomposition below: ERRATUM-r4 (design record), by the Pauli-twirl identity; not a corpus derivation. -->
Following Bäcker, Beyer and Strunz [BBS24], a two-step process has classical memory when the second map can be written as an instrument realizing the first map, followed by channels conditioned on its outcome. With the hidden slot initialized to a fixed card instead, the swap has the maps $\rho\mapsto|0\rangle\langle0|$ and $\rho\mapsto\rho$ and admits no such decomposition [Main §4.5]. With the uniform burn card it does: the instrument $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, $o\in\{0,x,y,z\}$, sums to the one-step map by the identity $\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)\,I$, and the channels $\rho\mapsto\sigma_o\rho\sigma_o$, conditioned on $o$, return $\rho$.

A card arrangement violates no Bell inequality [Book §1.11; Main §3.3].

## References

**Corpus** (repository commit `687e885b`, concept DOI 10.5281/zenodo.19060318)

[Main] A. Maybaum, "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation," `papers/Main.md`.

[GR] A. Maybaum, "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon," `papers/GR.md`.

[Book] A. Maybaum, *The Incompleteness of Observation*, `book/`.

[BHa] A. Maybaum, recovery from accessible records in finite reversible models, unpublished research record, internally reviewed; `bh01_access_v1/` in the black-hole computations' directory.

[BHb] A. Maybaum, "Permutation dynamics versus quantum scrambling; Page-time fraction," unpublished research record, internally reviewed; `bh02_scramble_v1/` in the black-hole computations' directory.

**External**

[Bar23] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085v2 (2023).

[Bar25] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778v3.

[Bar26] J. A. Barandes, "The Born Representation Theorem and the Unistochastic Theorem," arXiv:2608.04354v1 (2026).

[BB12] J. C. Baez and J. Biamonte, "Quantum techniques for stochastic mechanics," arXiv:1209.3632v5 (2012).

[BBS24] C. Bäcker, K. Beyer, and W. T. Strunz, "Local disclosure of quantum memory in non-Markovian dynamics," *Phys. Rev. Lett.* **132**, 060402 (2024); arXiv:2310.01205v2. <!-- VERIFY: content not read in the audits; definition taken via Main:702 -->

[BD16] F. Buscemi and N. Datta, "Equivalence between divisibility and monotonic decrease of information in classical and quantum stochastic processes," *Phys. Rev. A* **93**, 012101 (2016); arXiv:1408.7062v3.

[Bel64] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195 (1964).

[BJA17] B. Bylicka, M. Johansson, and A. Acín, "Constructive method for detecting the information backflow of non-Markovian dynamics," *Phys. Rev. Lett.* **118**, 120501 (2017); arXiv:1603.04288v2.

[BLP09] H.-P. Breuer, E.-M. Laine, and J. Piilo, "Measure for the degree of non-Markovian behavior of quantum processes in open systems," *Phys. Rev. Lett.* **103**, 210401 (2009); arXiv:0908.0238v2.

[Cal26] S. Calvo, "On the stochastic-quantum correspondence," arXiv:2601.18720v2 (2026). <!-- VERIFY: the sentence at §2.2 is taken from the v2 abstract (arXiv API record); the novelty audit's literature study records v1 and v2 as read in full text, with the claim at Thm 1, p. 4 (AUDIT r4 C4, [FT]); the body was not re-read for this draft -->

[CHSH69] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, "Proposed experiment to test local hidden-variable theories," *Phys. Rev. Lett.* **23**, 880 (1969).

[CT06] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006). <!-- VERIFY: content not read in the audits (AUDIT r4 P3.3) -->

[dMU21] L. de Moura and S. Ullrich, "The Lean 4 theorem prover and programming language," in *Proc. CADE 28* (Springer, 2021), p. 625.

[Dou26] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095v3 (2026).

[EGGH26] G. Egri, M. Gömöri, B. Gyenis, and G. Hofer-Szabó, "Trajectory of probabilities, probability on trajectories, and the stochastic-quantum correspondence," arXiv:2602.23491v1 (2026).

[EvEMU11] G. F. R. Ellis, H. van Elst, J. Murugan, and J.-P. Uzan, "On the trace-free Einstein equations as a viable alternative to general relativity," *Class. Quantum Grav.* **28**, 225007 (2011); arXiv:1008.1196v2. <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read -->

[GH03] E. F. Galvão and L. Hardy, "Substituting a qubit for an arbitrarily large number of classical bits," *Phys. Rev. Lett.* **90**, 087902 (2003); arXiv:quant-ph/0110166v3.

[Har04] L. Hardy, "Quantum ontological excess baggage," *Stud. Hist. Philos. Mod. Phys.* **35**, 267 (2004). <!-- VERIFY: content not read (AUDIT r4 C14, P3.2); cited only as reported in [Mon08] -->

[Haw76] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).

[KP14] N. Kaloper and A. Padilla, "Sequestering the Standard Model vacuum energy," *Phys. Rev. Lett.* **112**, 091304 (2014); arXiv:1309.6562v2. <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read -->

[LP17] D. A. Levin and Y. Peres, with contributions by E. L. Wilmer, *Markov Chains and Mixing Times*, 2nd ed. (American Mathematical Society, 2017).

[Mathlib20] The mathlib Community, "The Lean mathematical library," in *Proc. ACM SIGPLAN Conf. Certified Programs and Proofs* (ACM, 2020), p. 367.

[Milz20] S. Milz, D. Egloff, P. Taranto, T. Theurer, M. B. Plenio, A. Smirne, and S. F. Huelga, "When is a non-Markovian quantum process classical?," *Phys. Rev. X* **10**, 041049 (2020); arXiv:1907.05807v3.

[Mon08] A. Montina, "Exponential complexity and ontological theories of quantum mechanics," *Phys. Rev. A* **77**, 022104 (2008); arXiv:0711.4770v2.

[Pag93] D. N. Page, "Average entropy of a subsystem," *Phys. Rev. Lett.* **71**, 1291 (1993); arXiv:gr-qc/9305007v2.

[Pag13] D. N. Page, "Time dependence of Hawking radiation entropy," *J. Cosmol. Astropart. Phys.* **09**, 028 (2013); arXiv:1301.4995v3.

[Pen20] G. Penington, "Entanglement wedge reconstruction and the information paradox," *J. High Energy Phys.* **09**, 002 (2020); arXiv:1905.08255v3.

[RHP14] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014); arXiv:1405.0303v2.

[Sch21] H.-J. Schmidt, "Dilation of stochastic matrices by coarse graining," arXiv:2106.03513v1 (2021).

[SGD19] P. Strasberg and M. García Díaz, "Classical quantum stochastic processes," *Phys. Rev. A* **100**, 022120 (2019); arXiv:1905.03018v2.

[Sha79] A. Shamir, "How to share a secret," *Commun. ACM* **22**, 612 (1979). <!-- VERIFY: bibliographic data confirmed on Crossref (science re-check); content (the linear threshold scheme) cited from memory and not read; the BH-01 package names the secret-sharing threshold without a source -->

[tH14] G. 't Hooft, "The cellular automaton interpretation of quantum mechanics," arXiv:1405.1548v3 (2014). <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read; no priority is assigned -->

[Vol06] G. E. Volovik, "Vacuum energy: myths and reality," *Int. J. Mod. Phys. D* **15**, 1987 (2006); arXiv:gr-qc/0604062v4. <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read -->

\endgroup
