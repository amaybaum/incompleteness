# Observational Incompleteness: From Deterministic Dynamics to Quantum Observations

**Author:** Alex Maybaum  
**Date:** November 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

***

## Abstract

Could quantum randomness arise because an observer sees only part of a deterministic world? Observational incompleteness (OI) investigates this possibility for embedded observers with finite resolution. In finite reversible models, every probability pattern over a finite observation window has a hidden deterministic realization, including the records of repeated fixed-basis quantum measurements. When the observed past helps predict the future beyond what the present reveals, every such realization must retain hidden predictive memory, with a minimum capacity. Under a common independent preparation of the hidden part, finite recurrence also forces a failure of step-by-step forecasting whenever a visible transition is uncertain. These results constrain representations of observations. Reproducing the full range of quantum experiments additionally requires a physical account of preparations, measurement choices, state changes and combined systems. The Born rule and that operational construction remain open. Vacuum energy and black-hole information illustrate further questions about the relation between global dynamics and accessible observations.

## 1. Could quantum randomness reflect incomplete observation?

Quantum theory predicts the results of measurements only as probabilities. Whether that randomness belongs to nature, or shows that something is missing from the description, is one of the oldest questions about the theory. Einstein's objection is usually paraphrased as "God does not play dice."

This paper examines a different picture: God plays cards. A deck evolves by fixed rules and nothing in the rules is random, yet a player who sees only some of the cards finds the game uncertain. The picture is an analogy. It shows how hidden information, deterministic rules and random-looking observations fit together; it proves nothing about quantum mechanics, and none of the results below depends on it.

Here is the simplest version. Two cards lie on a table, one face up and one face down. The face-up card is red or black; seeing it is the player's first observation. The face-down card is dealt at random: it is red or black with equal probability, independently of the face-up card. Each shuffle is a fixed move, not a randomization: it swaps the two cards. After one shuffle the player can predict the colour now showing no better than by tossing a coin. After a second shuffle the original card is back, with certainty. The player's record therefore has memory: what is seen next depends on what was seen earlier, not only on what is showing now. That memory is kept in the face-down card. Once the cards are dealt nothing random happens; the uncertainty is the player's, and it comes from what the player cannot see. The game's statistics are those of ordinary classical probability, so it illustrates how hidden information works; it is not a model of quantum mechanics [Book §1.11].

Framed this way, a question about interpretation becomes three mathematical questions. Which patterns of observations can a partly hidden deterministic world produce? Where must the hidden information sit? What does storing it force the observations to look like?

**What is established and what is open.** Section 3 explains the finite-record correspondence, the hidden memory it requires, and the consequence of recurrence for forecasts. Section 4 asks what a single physical model would need to reproduce quantum experiments across different preparations and measurement choices. Section 5 applies the distinction between global dynamics and accessible observations to vacuum energy and black-hole information. Section 6 identifies the remaining physical constructions.

## 2. The simple idea: a hidden deterministic world can look random

Start with a world whose rule is *reversible*: each complete configuration has exactly one successor, and no two configurations have the same successor. Such a rule loses no information, so the whole present determines the whole past. In the formal papers this rule is a *bijection* of the world's configurations.

Now put an observer inside that world. The observer registers only part of each configuration, the *visible* part; the rest is *hidden*. Two configurations that look the same to the observer can differ in their hidden parts and so lead to different visible futures. The visible part therefore changes in a way that looks random to the observer, although the whole world changes without any randomness. What the observer sees depends on three things: the rule, the division into visible and hidden parts, and how the hidden part is prepared at the start [Main §1.2].

*Observational incompleteness* (OI) is the physical hypothesis that every physical observer is in this situation: only a part, never the whole, of a larger world that evolves deterministically and reversibly, with a specified way of reading and preparing its surroundings [Main §1.2]. The finiteness in the hypothesis belongs to the observer: having finitely many distinguishable internal states, an observer can tell apart only finitely many visible configurations [Main §1.2, Lemma 1]. The hypothesis does not require the whole world to be finite [Main §1.2, Remark (status of the early commitments)].

The results about hidden worlds in sections 3 and 4 are proved for *finite models*, called *substrata*. In a finite model the whole world has finitely many configurations, each a pair of a visible part and a hidden part, and the rule is a reversible map of those pairs. Finiteness of the whole is an assumption of these models, not a consequence of the observer being embedded in the world. The reversible rule is the models' representative of the hidden dynamics, a choice motivated by the observed near-unitarity of physical evolution (unitary evolution, in quantum theory, loses no information) [Main §1.2, Remark (status of the early commitments)].

What does the substratum itself run on? The old story of a world resting on turtles all the way down asks that question. A finite deeper layer that is prepared independently and evolves on its own, with no coupling to the substratum, can be added without changing anything this observer sees [Substratum, Theorem 24(iii)]; a deeper layer that can act back may change later records. These results neither classify every possible deeper level nor show that the regress ends. A finite reversible world is the model under investigation, not a demonstrated final description of nature [Substratum §§2–4; Book §3.8].

Hidden does not mean unknowable. In the two-card game the first two colours the player sees already identify both cards, even though the record has memory. In general, for an observer who knows the rule and how the world was prepared, a record of past observations identifies a hidden quantity exactly when every starting configuration compatible with that record gives it the same value [Substratum, Prop. 24.5]. Whether hidden information can be inferred depends on the records kept and on what the observer can do; the result concerns inference from records and supplies no physical mechanism for storing, preparing or acting on them.

Nor is this incompleteness the uncertainty principle of quantum theory. It arises even when the observer always reads the world in one fixed way, and the visible statistics of such a fixed readout are subject to no uncertainty relation [Main §3.4].

The question of section 1 can now be stated precisely. Fix a number of steps. A *pattern* lists the probability of every possible sequence of visible observations over those steps. A hidden world *realizes* a pattern if, with its rule and its preparation of the hidden part, the observer's sequence of observations has exactly those probabilities.

## 3. What the mathematics proves

For finite models, the three questions of section 1 have the following answers.

### 3.1 Every finite pattern can be reproduced by a hidden deterministic world

Fix a finite set of possible visible observations and a finite number of steps. Three collections of patterns can be compared [Main §3.4]:

- $\mathsf S$, every pattern at all: every way of assigning probabilities to the possible sequences of observations;
- $\mathsf D$, the patterns a finite reversible world shows to an observer who sees only its visible part, the hidden part being of any finite size and prepared in any way, possibly correlated with the first visible observation;
- $\mathsf Q_{\rm fb}$ (fb for "fixed basis"). A *basis* is the set of mutually exclusive states that a measurement distinguishes; *unitary* evolution is quantum theory's reversible evolution; the *Born rule* assigns the outcomes' probabilities. $\mathsf Q_{\rm fb}$ is the set of patterns of results of a finite quantum system that evolves by a unitary and is measured in one fixed basis at every step, starting from a random mixture of basis states (a state with definite probabilities in that basis); the record may be any fixed function of each result.

Over any finite number of steps the three collections are the same [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence)]:
$$
\mathsf S\;\Longleftrightarrow\;\mathsf D\;\Longleftrightarrow\;\mathsf Q_{\rm fb}.
$$

The statement holds for each finite stretch of time separately, and it concerns records of one fixed measurement repeated at every step. It does not say that the rest of quantum theory, with its incompatible measurements, superpositions and composite systems, is reproduced; section 4 explains what that would take. Within that scope, a fixed-measurement quantum record carries no statistical signature that a partly hidden deterministic world could not reproduce, and conversely. This settles a question of possibility, not of fact: it does not show that nature is such a world.

One construction is simple to picture: the hidden part holds a whole sequence of observations drawn in advance from the pattern, together with a clock, and each step brings the next entry into view while the rule stays reversible [Main §3.4; EGGH26, Prop. 13]. Every pattern also has a realization in which the hidden part is prepared independently of the first visible observation, the preparation assumed in section 3.3 [Main §3.4, Theorem (finite-horizon process dilation) and its Extension]. A form of this without reversibility is due to the same authors [EGGH26, Prop. 16], and for Markov chains, processes without memory, its one-step case is the random-mapping representation [LP17, Prop. 1.5].

On the quantum side, a reversible rule acts on quantum basis states as a permutation, a relabelling of states, which is a unitary; measuring in that basis at every step reproduces the visible statistics. Conversely, the Born rule turns every such quantum record into a pattern [Main §3.4]. A permutation dynamics is a special case of Barandes' unistochastic processes, whose transition probabilities are the squared magnitudes of the entries of a unitary [Bar23; Bar25; Bar26], and the probabilities of a record measured at every step are those of Strasberg and García Díaz [SGD19].

Two limits follow at once. Patterns without memory, in which the next observation depends only on the present one, belong to all three collections, so the existence of a hidden deterministic world reproducing a pattern does not distinguish patterns with memory from patterns without it [Main §3.4, Remark (what this equivalence does and does not say)]. And one fixed finite world eventually repeats itself, so its record is periodic: the correspondence holds for any chosen finite stretch of time, but a non-periodic pattern has no exact realization for all times by one fixed finite world [Main §3.4].

### 3.2 Memory must be stored out of sight

A record has *memory* at a given step when the observed past says something about the next observation beyond what the present observation already says. In the card game, what will be seen after the second shuffle still depends on the colour first showing, although that card is face down after the first shuffle: the face-down card holds it.

The same holds in every hidden deterministic world that reproduces a record. When observations contain information about the past that cannot be recovered from the present observation alone, a deterministic model reproducing those observations must retain the relevant information in its hidden state. Precisely, in every such world [Main §3.4, Theorem (unavoidable hidden predictive memory)]:

- the next observation depends on the past only through what the past reveals about the hidden state;
- two pasts can make different predictions only if they leave different odds on the hidden state, and their predictions differ by no more than those odds do;
- the memory visible in the record, measured in bits, never exceeds the memory held in the hidden state, which never exceeds the hidden part's capacity, the base-2 logarithm of its number of states.

A record has memory if and only if the hidden worlds that reproduce it keep a trace of the past that changes what is seen next: if the record has memory, every such world keeps one; if even one such world keeps one, the record has memory [Main §1.5; Main §3.4, Remark (what this strengthens)].

Here *predictive memory* means information about the past that helps predict the future beyond what the present observation reveals. A reversible world retains its whole visible past in its complete state, including for records whose next observation depends only on the present. Only the part relevant to future predictions contributes to the observable memory discussed here [Main §1.5].

Memory also fixes a minimum size. The hidden part needs at least $2^{I}$ states, where $I$ is the largest amount of information, in bits, that the observed past carries about the observed future once the present is known [Main §3.4, Theorem (C3 necessity)]. At each step, the least memory that a deterministic hidden world, not required to be reversible, must carry is exactly the information the past carries about the future once the present is known [Main §3.4, Remark (a variational question)]. Observed memory thus bounds something that cannot be observed directly.

Four conditions on the hidden part summarize what produces observable memory: it must influence what is seen, keep what it records, have room to record it, and feed the record back into what is seen [Main §1.3]. The first three are not enough: a fair coin can be reproduced by hidden worlds that influence, keep and have ample room, yet never read anything back, and its record has no memory [Main §2.3, Remark (why (C4) is a separate condition)].

### 3.3 Recurrence and the limits of step-by-step forecasting

In the card game, the forecast after one shuffle is the same coin toss whether the first visible card was red or black. After two shuffles, however, the original colour returns with certainty. A single forecast rule acting only on the colour after the first shuffle cannot recover which original colour to predict. The two identical probability forecasts have lost a distinction that the later observations recover.

This is a failure of *P-divisibility*, the ability to connect forecasts from a fixed starting time by intervening probability maps. Such maps cannot make two probability distributions easier to distinguish. When forecasts from different starts overlap and later return to different certainties, no intervening map connects them. This is the contraction argument used in the divisibility literature [RHP14, Thm 2.4; BD16] and in the concurrent analysis of Doukas [Dou26, Prop. 1]. It also connects the question to Barandes' stochastic–quantum correspondence [Bar23; Bar25].

For the OI result, compare every possible visible start, preparing the hidden part with the same distribution independently of that start. One rule and one preparation then determine the whole family of forecasts. In a finite reversible world, all configurations eventually return to their starting values. If a visible step is uncertain, the family must fail to chain somewhere before this return [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)].

The time at which this happens matters. The return may lie far beyond the observer's experimental window, and the failure can involve starts absent from the actual preparation. With positive probability for every visible start, failure somewhere in the cycle is equivalent to predictive memory somewhere before the return. Neither statement guarantees memory during a short experiment [Main §2.3, Scope]. Three independent fair coin tosses followed by a repeat of the first illustrate the delay. The hidden world must retain the first toss, but an observer who stops after three tosses sees no predictive memory [Main §3.4, Remark (a variational question)].

On a short window, predictive memory and failure of chaining can also separate. Two fair tosses followed by their parity have one bit of predictive memory, although the forecasts chain throughout those three steps. A finite reversible realization with the common independent hidden preparation still fails to chain somewhere in its full cycle. The proof and the window distinction are given in [Main §2.3, Scope], with the parity example in [RHP14, Eq. (15)] up to flipping the last bit, and concurrently in [Dou26, App. A].

## 4. What the mathematics does not prove

The correspondence of section 3.1 represents fixed-measurement statistics in hidden deterministic form. Several things lie outside it.

### 4.1 Representation is not derivation

The correspondence does not select the Born rule. In the quantum collection the rule that probabilities are squared magnitudes of amplitudes (the complex numbers quantum theory assigns to outcomes) is part of the definition. The unitaries that represent reversible worlds are permutations; since each entry is 0 or 1, raising the magnitudes to any positive power, not only the square, gives the same statistics, and nothing selects the square [Main §3.4, Remark (what this equivalence does and does not say); Bar26, Thm 3.1].

It does not select the quantum evolution between two times. Two quantum descriptions can reproduce the same visible record at every time and still differ in the evolution relating two times, by a time-dependent transformation the record cannot see; choosing between them needs a principle beyond representability [Main §3.4, Remark (scope: representability, not selection of the relating evolution)].

The correspondence establishes that finite observation patterns admit both representations. A physical explanation must additionally identify a mechanism that selects the observed pattern and makes its preparation and readout available. The memory bounds constrain any faithful deterministic realization once that pattern is specified. Calvo states a derivation of textbook quantum axioms from indivisible stochastic evolution [Cal26], a further claim beyond the correspondence described here.

Finally, memory in a record, failure of chaining and memory effects in the quantum description itself (non-Markovian quantum evolution) are distinct properties, and no unconditional implication among them is asserted [Main §3.2, Remark (three notions, kept apart)]. For the quantum description of a reversible world whose hidden part starts with definite probabilities, failure of chaining in the record implies failure of quantum chaining, the same failure when each intermediate step must be a valid quantum operation [Main §3.2, Theorem (CP-indivisibility, framework scope)]; outside that class it need not [Main §3.2, Remark (scope: P-indivisibility is not quantum non-Markovianity)].

### 4.2 What full quantum theory would need

Quantum mechanics specifies the probabilities of experiments with different measurement choices, their effects on later measurements, and the behaviour of combined systems. The target for OI is operational equivalence over a stated experimental scope. One realization and one physical interface must work across preparations, settings, sequences and combined systems. Every quantum experiment in that scope must be available, and every admitted OI experiment must agree with its quantum counterpart.

This target concerns what an embedded observer can prepare, change and observe. The underlying dynamics may remain deterministic. Hidden information may contribute through a later interaction without first being read separately. The required phase-sensitive behaviour and outcome-conditioned state changes must be obtained from physically available preparations and interventions, with accessible records and failed attempts included in the comparison.

Take as given that states are described by matrices of complex numbers, operations by linear maps on them, and two systems together by the tensor product of their descriptions. That setting is assumed, not derived from OI, and a derivation of it is open [GR §3.3]. Suppose also a few basic rules: the experimenter can leave the system alone, lump outcomes together, combine operations, prepare a helper, read the helper without disturbing the system, and discard it. Within that setting, the operations available on a finite system, with any finite helper attached, are exactly those of quantum theory if and only if five conditions hold [GR §3.3, Theorem (operational-completion characterization)]:

1. probabilities make sense: operations keep states valid and their outcome probabilities sum correctly;
2. adding a trivial, one-state helper changes nothing;
3. an untouched, independent bystander can be added without changing an operation;
4. *full reversible control*: every reversible quantum operation on every combined system is available;
5. a fresh helper in a completely random (evenly mixed) state can be attached to a combined system, used and discarded, so that a combined system can serve as the working system of a larger experiment.

The first two only make the theory well formed; the last three are the substantive requirements. Each condition is independent of the other four and of the observation process itself. A *qubit* is the simplest quantum system, with two basic states; for one fixed finite observation process with the four properties listed in section 3.2, and for each condition, there is a qubit theory that realizes the process and the other four conditions but fails that one. In particular, a theory that never creates coherence, that is, superpositions, realizes the observation process and is not quantum, so OI alone does not imply quantum mechanics [GR §3.3]. That the five conditions suffice rests on the standard dilation theorems [Sti55; Kra83; Oza84]; for reconstructions of finite quantum theory from operational axioms, see [Har01; CDP11; MM11].

A finite reversible world does not supply condition 4 on its own. Quantum theory can turn one state partly into another, by any fraction, and can also shift the phase of one state relative to another, for example by a quarter turn (a factor $i$). A reversible rule on finitely many states can only permute whole states; it cannot blend them. Under the observer access stated in [GR §3.3], the operations such a rule supplies also cannot shift the phase of one state relative to another, and so cannot produce the quarter-turn relative phase that full reversible control requires; condition 4 therefore fails for them on every system with two or more states [GR §3.3]. Whether the physical substratum supplies further kinds of intervention that would complete its repertoire, in particular a continuously driven transition between two states, together in some formulations with a selectable relative phase [GR §3.3], and why its operations should be complex matrices in the first place, are open.

### 4.3 Finite experiments and the full range of qubit experiments

The correspondence in section 3.1 chooses a hidden world for each finite pattern. A qubit admits an indefinitely growing family of preparation and measurement choices. These are different demands on a model.

A fixed finite world with $N$ configurations can prepare at most $N$ distinguishable underlying states, so every experiment of the form "prepare, then measure" that it supports runs through distributions over those $N$ states [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form)]. A qubit, by contrast, has no such bound: reproducing the statistics of ever larger finite families of its preparations and measurements requires classical memory beyond every fixed bound [HKLP24, Thm 4; GH03]. Montina reports the corresponding result of Hardy that the underlying state set cannot be finite [Mon08, citing Har04].

A finite-model comparison therefore has to specify its experimental scope and resources. Enlarging that scope may require a larger hidden world. Choosing a separate world for each observed pattern supplies no common physical interface for all those experiments. An exact account of the entire qubit family must address the finite-resource obstruction. Section 2's distinction between the observer's finite resolution and the size of the whole world leaves that broader construction open.

### 4.4 Bell correlations

Two laboratories far apart share a prepared pair of systems. Each chooses a measurement setting and records an outcome $+1$ or $-1$. Bell's theorem constrains explanations in which each outcome depends only on the local setting and shared information, and that shared information is independent of the setting choices [Bel64]. With an outcome recorded in every run, the combination $S_{\mathrm{CHSH}}$ of four setting-pair correlations has magnitude at most 2 [CHSH69]. Quantum mechanics reaches $2\sqrt2$.

The framework's own version is this [Main §3.3, Theorem (Bell ceiling for a screened local completion)]. Suppose the hidden world is deterministic; each laboratory's setting acts only on its own region; each outcome is read from a region that the other laboratory's setting cannot influence within the time of the experiment; the settings are chosen independently of the hidden state that precedes them; and an outcome is recorded in every run. Then $|S_{\rm CHSH}|\le2$. A two-player version of the card game obeys the same ceiling when every operation reads and changes only one player's own cards and depends only on those cards, that player's setting and chance that, together with the deal, is independent of the settings; when both players record an outcome in every run; and when the settings are chosen independently of the deal [Book §1.11; Main §3.3]. Reproducing quantum Bell correlations therefore requires giving up at least one of these assumptions.

OI keeps determinism and an outcome in every run. It also keeps the independence of the settings, as an assumption about initial conditions, and accepts instead that one laboratory's hidden response may depend on the other laboratory's setting, with no usable signal between them. The particular substratum the companion papers study is a cubic lattice whose sites are updated from their nearest neighbours [SM]; that update cannot supply the dependence for laboratories outside each other's range of influence [Main §3.3, Corollary (Bell–lattice obstruction and state-dependent escape)]. The substratum's coupling graph records which sites directly affect which. Whether a Bell preparation can add long-range links to it, with each site gaining only a bounded number of them, or an equivalent nonlocal response, so as to supply this dependence while keeping operational no-signalling and the large-scale continuum limit on which the framework's account of gravity rests, is an open hypothesis, called H-Bell [Main §3.3; Substratum §3.2].

## 5. Why it matters

### 5.1 Quantum foundations

Because every fixed-measurement pattern can be reproduced by a hidden deterministic world, no record of one repeated measurement can by itself rule out a partly hidden deterministic account of it. The informative content lies in what such accounts must contain: where memory is stored, how much room it needs, and what recurrence does to forecasts. Deterministic systems have been analysed with quantum methods before, for example by 't Hooft [tH14].

The physical question is which observation patterns arise from one specified dynamics, preparation mechanism and observer interface. The finite-record correspondence makes deterministic representations available. The memory bounds constrain what those representations must retain. Selecting the quantum family of experiments requires the operational construction of section 4, including its measurement choices and composite systems.

### 5.2 The energy of empty space

Quantum fields have zero-point energy even in their lowest states. Summing it down to a microscopic cutoff gives a density that can exceed the observed vacuum energy density by roughly 120 orders of magnitude, depending on the cutoff convention [Wei89]. The observed density is represented by the cosmological constant and drives accelerated expansion. If the zero-point sum gravitated directly, a cancellation of comparable precision would be needed.

OI separates the quantum description of observations from the gravitational description of the substratum. A constant shift of quantum energy changes no visible probability. Within that description, the absolute zero-point offset is therefore inaccessible [GR §6.2]. A gravitational source can nevertheless depend on quantities absent from these observation statistics.

The proposal in [GR] is to source gravity from the substratum's classical energy and momentum. If the targeted field equations follow, the quantum zero-point sum contributes no curvature. The remaining vacuum term is uncomputed and the observed cosmological constant remains an input. The decisive question is the source coupling. Gravitational completions in which the offset does or does not gravitate can share the same substratum, observer partition and visible transition law. Deriving the field equations and their sources is therefore required to decide between them [GR §6.2, §8.5]. Related approaches include trace-free Einstein equations [EvEMU11], vacuum-energy sequestering [KP14] and Volovik's account of vacuum energy [Vol06].

### 5.3 Black-hole information: keeping versus showing

The black-hole information problem asks whether the radiation of an evaporating black hole carries the information of what formed it [Haw76; Pag93b]. In OI two questions separate: whether information is conserved by the global dynamics, which holds because the dynamics is reversible, and whether it can be recovered from the records an observer can access [HP07]. A burned letter is a useful analogy: the smoke, ash and heat still encode its words, because the underlying laws lose nothing, yet nobody who sees only the smoke can read it.

Unpublished finite register models make this distinction precise [BHa]. Registers pass from an interior to a radiation side, and the observer reads on a fixed schedule. The study ranges over reversible and irreversible maps supplied as toy models. Some reversible maps keep a message hidden from radiation-only records, while some irreversible maps permit exact recovery when all registers are read. Reversibility guarantees recovery from the complete final state. For a uniform message, complete hiding also requires at least as many joint values of the unread registers as there are messages, a capacity bound related to perfect secret sharing [Sha79].

The toy models address only whether a message can be hidden from an observer who reads some registers and not others. The quantum version of the problem asks for more: the *Page curve*, the characteristic rise and then fall of the entanglement between the radiation and what remains of the black hole as evaporation proceeds. Reproducing it requires ingredients the finite models do not have. The cycle-averaged argument in [GR, App. A] assumes typical quantum entanglement along the dynamics (H-scramble), decoupling (H-decouple), and an energy shell containing all joint configurations. Under its stated preparation of definite configurations and its configuration split into interior and exterior, a reversible permutation keeps each state a definite, unentangled configuration. H-scramble has no instances in that setting, so the argument establishes no Page curve [GR §8.4, App. A.7–A.9; BHb]. A physical recovery model needs a preparation or partition that supports the required observable coherence, an attainable scrambling condition and an appropriate entropy statement. H-decouple and the smaller energy shell of an evaporating black hole also remain open.

## 6. What remains open

Turning mathematical representability into a complete physical theory needs the following, none of which is established:

1. **Operational quantum theory.** How the complex-matrix and tensor-product description of section 4.2 arises physically, and whether the substratum supplies the interventions that conditions 3–5 require [GR §3.3].
2. **Selection principles.** A reason for the Born rule's squares, and for the evolution relating two times (section 4.1).
3. **Observable memory.** A physical mechanism for memory to affect observations at the cosmological horizon, where [GR §2.1–2.2] places the observer's boundary, and experimentally accessible consequences of that mechanism [Main §4.5]. Within a scope of exact operational equivalence, OI and QM predict the same observation probabilities. A distinguishing test would have to address a particular OI model's additional restrictions or behaviour outside that equivalence scope.
4. **Dynamical construction.** Joining the realizations of section 3.1 for successive stretches of time exactly into one world for recurrent multi-time patterns; approximating a target over short stretches by one fixed substratum [Main §3.4]; and the hidden-sector mixing assumption under which observed memory gives a lower bound on how long the hidden part takes to settle [Main §1.3, §3.4].
5. **Bell correlations.** The hypothesis H-Bell of section 4.4 [Main §3.3; Substratum §3.2].
6. **Gravity.** Covariant field equations derived from the substratum, with their coupling to sources, on which the vacuum-energy proposal of section 5.2 and the gravitational Page-curve argument both depend [GR §6.2, §8.5].
7. **Black holes.** A physical preparation and observer partition must support the required observable coherence, with a scrambling and entropy statement beyond the finite register models. The decoupling condition H-decouple is not established: the effective-pure-state result of [GR, App. A.7] concerns the exterior and interior jointly, and only for times short compared with the cosmological timescale. An evaporating black hole whose radiation carries away its energy occupies an energy shell smaller than the set of all joint configurations, and that case is also open. So are the entropy along a single trajectory, the generalized second law (that total entropy including black-hole entropy does not decrease) [GR App. A.6], and the relation to recent semiclassical calculations of the Page curve using quantum extremal surfaces and islands [Pen20; AEMM19; AMMZ20; Book §7.6].

## Where the details are

This paper explains results proved elsewhere and claims no new theorem; earlier work is credited where it is used. Proofs of the results it describes are in the formal papers: the finite-horizon correspondence, hidden memory and its bounds in [Main §§1.3, 1.5, 3.4]; recurrence and failure of chaining in [Main §2.3]; memory, chaining and quantum non-Markovianity in [Main §3.2]; the Bell ceiling in [Main §3.3]; the operational characterization in [GR §3.3]; vacuum energy in [GR §6]; the Page-curve conditions in [GR, App. A]; identification from retained records in [Substratum, Prop. 24.5]. The formal papers state each result with its full hypotheses and identify the results they import from other authors.

Several of these proofs are also checked by computer in the Lean 4 proof assistant with its Mathlib library [dMU21; Mathlib20]; the formal papers name the checked declarations beside the statements they support, and the repository's Lean census and proof-coverage ledger under `verification/` record which statement each declaration supports.

The black-hole toy-model results are unpublished finite-model research: exhaustive enumerations over small register spaces with a proved recovery floor, whose novelty has not been assessed. Their written proofs and code [BHa; BHb] are in `verification/programmes/black-hole-information/`, and the finite probes behind several statements of [Main] are in `papers/oi_lattice_code/foundations/`, both released under the MIT License. The novelty of the operational characterization of section 4.2 and of the result on the evolution relating two times in section 4.1 has also not been assessed.

## Acknowledgments

AI assistance in preparing this work is disclosed at\
<https://github.com/amaybaum/incompleteness#ai-assistance>.

## References

\begingroup\footnotesize\raggedright\setlength{\parskip}{1pt}\setlength{\leftskip}{1.5em}\setlength{\parindent}{-1.5em}

**Corpus** (concept DOI 10.5281/zenodo.19060318)

[Main] A. Maybaum, "The Incompleteness of Observation: Finite-Observer Representations and Quantum Reconstruction," `papers/Main.md`.

[GR] A. Maybaum, "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon," `papers/GR.md`.

[SM] A. Maybaum, "The Standard Model from a Cubic Lattice," `papers/SM.md`.

[Substratum] A. Maybaum, "The Substratum Construction: Reconstruction, the Substratum Gauge Group, and the QM-GR Synthesis," `papers/Substratum.md`.

[Book] A. Maybaum, *The Incompleteness of Observation*, `book/`.

[BHa] A. Maybaum, "Recovery from accessible records in finite reversible models," unpublished analysis of a finite reversible toy model and its exact enumeration results, under the stated assumptions; not a derived physical model of black-hole evaporation. Written proofs and code: `verification/programmes/black-hole-information/bh01_access_v1/`.

[BHb] A. Maybaum, "Permutation dynamics versus quantum scrambling; Page-time fraction," unpublished research analysis of the configuration-state scrambling and Page-curve obstruction, with its stated limitations; not a derived physical model of black-hole evaporation. Written proofs and code: `verification/programmes/black-hole-information/bh02_scramble_v1/`.

**External**

[AEMM19] A. Almheiri, N. Engelhardt, D. Marolf, and H. Maxfield, "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole," *J. High Energy Phys.* **12**, 063 (2019); arXiv:1905.08762.

[AMMZ20] A. Almheiri, R. Mahajan, J. Maldacena, and Y. Zhao, "The Page curve of Hawking radiation from semiclassical geometry," *J. High Energy Phys.* **03**, 149 (2020); arXiv:1908.10996.

[Bar23] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085v2 (2023).

[Bar25] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778v3.

[Bar26] J. A. Barandes, "The Born Representation Theorem and the Unistochastic Theorem," arXiv:2608.04354v1 (2026).

[BD16] F. Buscemi and N. Datta, "Equivalence between divisibility and monotonic decrease of information in classical and quantum stochastic processes," *Phys. Rev. A* **93**, 012101 (2016); arXiv:1408.7062v3.

[Bel64] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Fizika* **1**, 195 (1964).

[Cal26] S. Calvo, "On the stochastic-quantum correspondence," *Quantum Stud. Math. Found.* **14**, 2 (2026), doi:10.1007/s40509-026-00415-9; arXiv:2601.18720v2.

[CDP11] G. Chiribella, G. M. D'Ariano, and P. Perinotti, "Informational derivation of quantum theory," *Phys. Rev. A* **84**, 012311 (2011).

[CHSH69] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, "Proposed experiment to test local hidden-variable theories," *Phys. Rev. Lett.* **23**, 880 (1969).

[dMU21] L. de Moura and S. Ullrich, "The Lean 4 theorem prover and programming language," in *Proc. CADE 28* (Springer, 2021), p. 625.

[Dou26] J. Doukas, "On the emergence of quantum mechanics from stochastic processes," arXiv:2602.22095v3 (2026).

[EGGH26] G. Egri, M. Gömöri, B. Gyenis, and G. Hofer-Szabó, "Trajectory of probabilities, probability on trajectories, and the stochastic-quantum correspondence," arXiv:2602.23491v1 (2026).

[EvEMU11] G. F. R. Ellis, H. van Elst, J. Murugan, and J.-P. Uzan, "On the trace-free Einstein equations as a viable alternative to general relativity," *Class. Quantum Grav.* **28**, 225007 (2011); arXiv:1008.1196v2.

[GH03] E. F. Galvão and L. Hardy, "Substituting a qubit for an arbitrarily large number of classical bits," *Phys. Rev. Lett.* **90**, 087902 (2003); arXiv:quant-ph/0110166v3.

[Har01] L. Hardy, "Quantum theory from five reasonable axioms," arXiv:quant-ph/0101012 (2001).

[Har04] L. Hardy, "Quantum ontological excess baggage," *Stud. Hist. Philos. Mod. Phys.* **35**, 267 (2004).

[Haw76] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Phys. Rev. D* **14**, 2460 (1976).

[HKLP24] T. Heinosaari, O. Kerppo, L. Leppäjärvi, and M. Plávala, "Simple information processing tasks with unbounded quantum advantage," *Phys. Rev. A* **109**, 032627 (2024); arXiv:2308.07727v4.

[HP07] P. Hayden and J. Preskill, "Black holes as mirrors: quantum information in random subsystems," *J. High Energy Phys.* **09**, 120 (2007); arXiv:0708.4025.

[KP14] N. Kaloper and A. Padilla, "Sequestering the Standard Model vacuum energy," *Phys. Rev. Lett.* **112**, 091304 (2014); arXiv:1309.6562v2.

[Kra83] K. Kraus, *States, Effects, and Operations*, Lecture Notes in Physics **190** (Springer, 1983).

[LP17] D. A. Levin and Y. Peres, with contributions by E. L. Wilmer, *Markov Chains and Mixing Times*, 2nd ed. (American Mathematical Society, 2017).

[Mathlib20] The mathlib Community, "The Lean mathematical library," in *Proc. ACM SIGPLAN Conf. Certified Programs and Proofs* (ACM, 2020), p. 367.

[MM11] Ll. Masanes and M. P. Müller, "A derivation of quantum theory from physical requirements," *New J. Phys.* **13**, 063001 (2011).

[Mon08] A. Montina, "Exponential complexity and ontological theories of quantum mechanics," *Phys. Rev. A* **77**, 022104 (2008); arXiv:0711.4770v2.

[Oza84] M. Ozawa, "Quantum measuring processes of continuous observables," *J. Math. Phys.* **25**, 79 (1984).

[Pag93b] D. N. Page, "Information in black hole radiation," *Phys. Rev. Lett.* **71**, 3743 (1993); arXiv:hep-th/9306083v2.

[Pen20] G. Penington, "Entanglement wedge reconstruction and the information paradox," *J. High Energy Phys.* **09**, 002 (2020); arXiv:1905.08255v3.

[RHP14] Á. Rivas, S. F. Huelga, and M. B. Plenio, "Quantum non-Markovianity: characterization, quantification and detection," *Rep. Prog. Phys.* **77**, 094001 (2014); arXiv:1405.0303v2.

[SGD19] P. Strasberg and M. García Díaz, "Classical quantum stochastic processes," *Phys. Rev. A* **100**, 022120 (2019); arXiv:1905.03018v2.

[Sha79] A. Shamir, "How to share a secret," *Commun. ACM* **22**, 612 (1979).

[Sti55] W. F. Stinespring, "Positive functions on C\*-algebras," *Proc. Amer. Math. Soc.* **6**, 211 (1955).

[tH14] G. 't Hooft, "The cellular automaton interpretation of quantum mechanics," arXiv:1405.1548v3 (2014).

[Vol06] G. E. Volovik, "Vacuum energy: myths and reality," *Int. J. Mod. Phys. D* **15**, 1987 (2006); arXiv:gr-qc/0604062v4.

[Wei89] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).

\endgroup
