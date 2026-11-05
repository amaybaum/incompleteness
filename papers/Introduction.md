# Observational Incompleteness: From Deterministic Dynamics to Quantum Observations

**Author:** Alex Maybaum  
**Date:** November 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Foundations

***

## Abstract

Could the randomness of quantum measurements come from observers seeing only part of a deterministic world? Observational incompleteness (OI) is the hypothesis that every observer is part of a larger world that evolves deterministically and reversibly, and can distinguish only finitely many configurations of what it sees. This paper explains, for non-specialists, what has been proved about the idea in finite models and what has not. Over any finite number of steps, every pattern of observations, including every record of a quantum system measured in the same way at each step, is produced exactly by some partly hidden deterministic world. Whenever such a record has memory, the hidden part must store it and must be large enough to hold it. If the hidden part is prepared in the same way whatever is visible at the start, any visible step that is not fully predictable also makes the forecasts from the possible starts impossible to chain step by step somewhere in the world's cycle. These results represent quantum statistics; they do not derive quantum mechanics, which needs an assumed matrix structure and five conditions that OI does not supply, and the quadratic Born rule is not selected. Applications to vacuum energy and black-hole information are stated as finite-model results and proposals.

## 1. Could quantum randomness reflect incomplete observation?

Quantum theory predicts the results of measurements only as probabilities. Whether that randomness belongs to nature, or shows that something is missing from the description, is one of the oldest questions about the theory. Einstein's objection is usually paraphrased as "God does not play dice."

This paper examines a different picture: God plays cards. A deck evolves by fixed rules and nothing in the rules is random, yet a player who sees only some of the cards finds the game uncertain. The picture is an analogy. It shows how hidden information, deterministic rules and random-looking observations fit together; it proves nothing about quantum mechanics, and none of the results below depends on it.

Here is the simplest version. Two cards lie on a table, one face up and one face down. The face-down card is dealt at random: it is red or black with equal probability, independently of the face-up card. Each shuffle then swaps the two cards. After one shuffle the player can predict the colour now showing no better than by tossing a coin. After a second shuffle the original card is back, with certainty. The player's record therefore has memory: what is seen next depends on what was seen earlier, not only on what is showing now. That memory is kept in the face-down card. Once the cards are dealt nothing random happens; the uncertainty is the player's, and it comes from what the player cannot see. The game's statistics are those of ordinary classical probability, so it illustrates how hidden information works; it is not a model of quantum mechanics [Book §1.11].

Framed this way, a question about interpretation becomes three mathematical questions. Which patterns of observations can a partly hidden deterministic world produce? Where must the hidden information sit? What does it force the observations to look like?

**What is established and what is open.** Section 3 gives three answers that are proved for finite models: every finite pattern of fixed-measurement records can be reproduced by a hidden deterministic world; any memory in such a record must be stored, with a minimum size, in the hidden part; and, under a stated assumption about how the hidden part is prepared, a visible step that is not fully predictable makes forecasts fail to chain somewhere in the world's cycle. Section 4 states what is not established: that nature is such a world, that quantum theory follows from OI alone, that the operations quantum theory needs are physically available, and that the quadratic rule for quantum probabilities is selected. Section 5 describes applications that are either finite-model results or proposals, and section 6 lists the physical steps that remain open. The proofs are in the formal papers cited throughout; the last section, "Where the details are", says where.

## 2. The simple idea: a hidden deterministic world can look random

Start with a world whose rule is *reversible*: each complete configuration has exactly one successor, and no two configurations have the same successor. Such a rule loses no information, so the whole present determines the whole past. In the formal papers this rule is a *bijection* of the world's configurations.

Now put an observer inside that world. The observer registers only part of each configuration, the *visible* part; the rest is *hidden*. Two configurations that look the same to the observer can differ in their hidden parts and so lead to different visible futures. The visible part therefore changes in a way that looks random to the observer, although the whole world changes without any randomness. What the observer sees depends on three things: the rule, the division into visible and hidden parts, and how the hidden part is prepared at the start [Main §1.2].

*Observational incompleteness* (OI) is the physical hypothesis that every physical observer is in this situation: a proper part of a larger world that evolves deterministically and reversibly, with a specified way of reading and preparing its surroundings [Main §1.2]. The finiteness in the hypothesis belongs to the observer: having finitely many distinguishable internal states, an observer can tell apart only finitely many visible configurations [Main §1.2, Lemma 1]. The hypothesis does not require the whole world to be finite [Main §1.2, Remark (status of the early commitments)].

The results about hidden worlds in sections 3 and 4 are proved for *finite models*, called *substrata*. In a finite model the whole world has finitely many configurations, each a pair of a visible part and a hidden part, and the rule is a reversible map of those pairs. Finiteness of the whole is an assumption of these models, not a consequence of the observer being embedded in the world. The reversible rule is the models' representative of the hidden dynamics, a choice motivated by the observed near-unitarity of physical evolution, unitary evolution being the reversible evolution of quantum theory [Main §1.2, Remark (status of the early commitments)].

Hidden does not mean unknowable. In the two-card game the first two colours the player sees already identify both cards, even though the record has memory. In general, an observer who keeps a record of past observations knows a hidden quantity exactly when every starting configuration compatible with that record gives it the same value [Substratum, Prop. 24.5]. Whether hidden information can be inferred depends on the records kept and on what the observer can do; the result concerns inference from records and supplies no physical mechanism for storing, preparing or acting on them.

Nor is this incompleteness the uncertainty principle of quantum theory. It arises even when the observer always reads the world in one fixed way, and the visible statistics of such a fixed readout are subject to no uncertainty relation [Main §3.4].

What does the substratum itself run on: turtles all the way down, as in the story Hawking retells? A deeper layer that never acts back on the substratum can be added without changing anything this observer sees, under the preparation assumptions of [Substratum, Theorem 24(iii)]; a deeper layer that can act back may change later records. These results neither classify every possible deeper level nor show that the regress ends. A finite reversible world is the model under investigation, not a demonstrated final description of nature [Substratum §§2–4; Book §3.8].

The question of section 1 can now be stated precisely. Fix a number of steps. A *pattern* lists the probability of every possible sequence of visible observations over those steps. A hidden world *realizes* a pattern if, with its rule and its preparation of the hidden part, the observer's sequence of observations has exactly those probabilities.

## 3. What the mathematics proves

### 3.1 Every finite pattern can be reproduced by a hidden deterministic world

Fix a finite set of possible visible observations and a finite number of steps. Three collections of patterns can be compared [Main §3.4]:

- **S**, every pattern at all: every way of assigning probabilities to the possible sequences of observations;
- **D**, the patterns a finite reversible world shows to an observer who sees only its visible part, the hidden part being of any finite size and prepared in any way, possibly correlated with the first visible observation;
- **Q**$_{\rm fb}$, the patterns of results of a finite quantum system that evolves by a unitary, the reversible evolution of quantum theory, and is measured in one fixed basis at every step, starting from a state with definite probabilities in that basis; each result has the probability the Born rule assigns, and the record may be any fixed function of each result.

Over any finite number of steps the three collections are the same [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence)]:
$$
\mathsf S\;\Longleftrightarrow\;\mathsf D\;\Longleftrightarrow\;\mathsf Q_{\rm fb}.
$$

The scope of this statement is part of its content. It holds for each finite stretch of time separately, and it concerns records of one fixed measurement repeated at every step. It does not say that the rest of quantum theory, with its incompatible measurements, superpositions and composite systems, is reproduced; section 4 explains what that would take. Within that scope, a fixed-measurement quantum record carries no statistical signature that a partly hidden deterministic world could not reproduce, and conversely. This settles a question of possibility, not of fact: it does not show that nature is such a world.

One construction is simple to picture. The hidden part holds a whole sequence of observations drawn in advance from the pattern, together with a clock, and each step brings the next entry into view, while the rule stays reversible [Main §3.4]. This trajectory-labelling realization is due to Egri, Gömöri, Gyenis and Hofer-Szabó [EGGH26, Prop. 13]. Every pattern also has a realization in which the hidden part is prepared independently of the first visible observation [Main §3.4, Theorem (finite-horizon process dilation) and its Extension]; a form without reversibility is [EGGH26, Prop. 16], and its memoryless one-step case is the random-mapping representation of Markov chains [LP17, Prop. 1.5].

On the quantum side, a reversible rule acts on quantum basis states as a permutation, which is a unitary, and measuring in that basis at every step reproduces the visible statistics; conversely, the Born rule turns every such quantum record into a pattern [Main §3.4]. A permutation dynamics is a special case of the unistochastic processes of Barandes' stochastic–quantum correspondence [Bar23; Bar25; Bar26], and the law of a record measured at every step is that of Strasberg and García Díaz [SGD19].

Two limits follow at once. Patterns without memory, in which the next observation depends only on the present one, belong to all three collections, so the existence of a hidden deterministic world reproducing a pattern does not distinguish patterns with memory from patterns without it [Main §3.4, Remark (what this equivalence does and does not say)]. And one fixed finite world eventually repeats itself, so its record is periodic: the correspondence holds for any chosen finite stretch of time, but a non-periodic pattern has no exact realization for all times by one fixed finite world [Main §3.4].

### 3.2 Memory must be stored out of sight

A record has *memory* at a given step when the observed past says something about the next observation beyond what the present observation already says. In the card game, after the first shuffle the record remembers the dealt card, although the face-up card does not show it, because the face-down card holds it.

The same holds in every hidden deterministic world that reproduces a record. When observations contain information about the past that cannot be recovered from the present observation alone, a deterministic model reproducing those observations must retain the relevant information in its hidden state. Precisely: the next observation depends on the past only through what the past reveals about the hidden state; two pasts can lead to different predictions only if they leave at least as different odds on the hidden state; and the memory visible in the record, in bits, never exceeds the memory held in the hidden state, which never exceeds the hidden part's capacity, the base-2 logarithm of its number of states [Main §3.4, Theorem (unavoidable hidden predictive memory)].

The statement also runs the other way. A record has memory exactly when every hidden deterministic world that reproduces it keeps, in its hidden part, a trace of the past that changes what is seen next; and if any one such world keeps a trace of that kind, the record has memory [Main §1.5; Main §3.4, Remark (what this strengthens)].

Keeping the past is not the same as memory. A reversible world run from the start stores its whole visible past, even when the record has no memory at all; memory is the part of that store that changes what is seen next [Main §1.5].

Memory also fixes a minimum size. The hidden part needs at least $2^{I}$ states, where $I$ is the largest amount of information, in bits, that the observed past carries about the observed future once the present is known [Main §3.4, Theorem (C3 necessity)]. At each step, the least memory that a deterministic hidden world, not required to be reversible, must carry is exactly the information the past carries about the future once the present is known [Main §3.4, Remark (a variational question)]. Observed memory thus bounds something that cannot be observed directly.

Four conditions on the hidden part summarize what produces observable memory: it must influence what is seen, keep what it records, have room to record it, and feed the record back into what is seen [Main §1.3]. The first three are not enough: a fair coin can be reproduced by hidden worlds that influence, keep and have ample room, yet never read anything back, and its record has no memory [Main §2.3, Remark (why (C4) is a separate condition)].

### 3.3 Recurrence: forecasts that cannot be chained

If the weather had no memory, a forecast from Monday to Wednesday could be built from one from Monday to Tuesday and one from Tuesday to Wednesday. When can the probabilities of an observed process be chained in this way? In the card game the forecast from the deal to the first shuffle is a coin toss whichever card was dealt face up, yet the forecast to the second shuffle is certainty. No forecast from the first shuffle to the second can turn two identical coin-toss forecasts into two different certainties, so the chain breaks. The property that fails is called *P-divisibility*.

The forecasts here are taken from every visible start the world could have, including starts an experiment never uses, with the hidden part prepared in the same way whatever the visible start and independently of it. That assumption makes the table of forecasts a property of one rule and one preparation, so that differences between forecasts come from the dynamics, not from a changed setup [Main §2.3].

The key fact is simple. A step-by-step forecast can never move two forecasts further apart. So if the forecasts from two different starts overlap at some time, and at a later time they become two different certainties, no chain of step-by-step forecasts connects the two times [Main §2.3, Theorem (overlap and return)]. This uses the standard contraction criterion for divisibility [RHP14, Thm 2.4; BD16]; Doukas states the same argument concurrently [Dou26, Prop. 1].

A finite reversible world supplies the return to certainty: after finitely many steps, its *recurrence time*, every configuration is back where it started, and the forecasts from the start are certainties again. Hence, in a finite reversible world whose hidden part is prepared as just described, any visible step that is not fully predictable from the current observation forces forecasts that cannot be chained somewhere within one recurrence cycle; so do any two different observed histories of the same length that end at the same observation [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]. When every visible start has positive probability, this failure occurs exactly when the record has memory at some step before the recurrence time [Main §2.3, Scope]; otherwise it may sit only in forecasts from starts that never occur.

This failure is a property of the world's rule, not necessarily of anything an observer will see: the stretches of time an observer can examine are short compared with the recurrence time of a large world, and memory can first appear after all of them [Main §2.3, Scope]. For example, let the first three observations be independent fair coin tosses and let the fourth repeat the first. Up to the third observation the record has no memory, yet every deterministic world that reproduces it must keep the first toss in its hidden part, and the past then predicts the fourth observation exactly [Main §3.4, Remark (a variational question)]; an observer whose record ends at the third observation cannot detect that. And since any visible step that is not fully predictable suffices, recurrence-cycle failure of chaining also occurs for records with no memory on any stretch an observer can examine. What an observer can detect is memory within reach [Main §2.3, Scope].

Memory and failure of chaining are also different properties on a single short stretch. Let two fair coin tosses be followed by their parity. Neither toss alone predicts the parity and both together determine it, so the record has one full bit of memory; yet on these three steps every forecast can be chained [Main §2.3, Scope]. A finite reversible world reproducing this record, with its hidden part prepared independently of the visible start, still fails to chain somewhere in its full cycle, but not necessarily within those three steps. The process is that of Rivas, Huelga and Plenio [RHP14, Eq. (15)], up to flipping the last bit, and appears concurrently in [Dou26, App. A].

## 4. What the mathematics does not prove

### 4.1 Representation is not derivation

The correspondence of section 3.1 represents fixed-measurement statistics in hidden deterministic form, and its statement leaves several things undone.

It does not select the quadratic Born rule. In the quantum collection the rule that probabilities are squared magnitudes of amplitudes is part of the definition. The unitaries that represent reversible worlds are permutations, whose entries are 0 or 1, so they give the same statistics for every power of the magnitudes; nothing selects the square [Main §3.4, Remark (what this equivalence does and does not say); Bar26, Thm 3.1].

It does not select the quantum evolution between two times. Two quantum descriptions can reproduce the same visible record at every time and still differ in the evolution relating two times, by a time-dependent transformation the record cannot see; choosing between them needs a principle beyond representability [Main §3.4, Remark (scope: representability, not selection of the relating evolution)].

It explains nothing on its own. It says which patterns admit hidden deterministic and quantum representations, not why a physical system shows a pattern with memory [Main §3.4, Remark (representation, not explanation)]. Calvo states a derivation of the textbook axioms from indivisible stochastic evolution [Cal26]; the correspondence derives no axioms.

Finally, memory in a record, failure of chaining and quantum non-Markovian evolution are distinct properties, and no unconditional implication among them is asserted [Main §3.2, Remark (three notions, kept apart)]; failure of chaining in a record implies failure of quantum chaining for one stated class of quantum descriptions, but not in general [Main §3.2].

### 4.2 What full quantum theory would need

Quantum mechanics says more than any fixed-measurement record. It allows measurements of incompatible kinds, superpositions that are not mixtures of definite states, and systems combined into larger ones. The relevant question is operational: which operations can an experimenter perform on a finite system, with helper systems attached?

Take as given that the operations are complex-linear maps on matrices, with combined systems described by tensor products. That setting is assumed, not derived from OI, and a derivation of it is open [GR §3.3]. Suppose also a few basic rules: the experimenter can leave the system alone, lump outcomes together, combine operations, prepare a helper, read the helper without disturbing the system, and discard it. Within that setting, the operations available on a finite system, with any finite helper attached, are exactly those of quantum theory if and only if five conditions hold [GR §3.3, Theorem (operational-completion characterization)]:

1. probabilities make sense: operations keep states valid and their outcome probabilities sum correctly;
2. adding a trivial, one-state helper changes nothing;
3. an untouched, independent bystander can be added without changing an operation;
4. *full reversible control*: every reversible quantum operation on every combined system is available;
5. a fresh, evenly mixed helper can be attached to a combined system, used and discarded, so that a combined system can serve as the working system of a larger experiment.

The first two only make the theory well formed; the last three are the substantive requirements. Each condition is independent of the other four and of the observation process itself: for one fixed finite embedded-observation process with the four properties listed in section 3.2, and for each condition, there is a qubit theory that realizes the process and the other four conditions but fails that one. In particular, a theory that never creates coherence, that is, superpositions, realizes the observation process and is not quantum, so OI alone does not imply quantum mechanics [GR §3.3]. The sufficiency direction rests on the standard dilation theorems [Sti55; Kra83; Oza84]; for reconstructions of finite quantum theory from operational axioms, see [Har01; CDP11; MM11].

A finite reversible world does not supply condition 4 on its own. The operations that reversible dynamics of finitely many states supplies, under the stated observer access, cannot produce a quarter-turn relative phase (a phase factor $i$ on one state), which full reversible control requires; so condition 4 fails for them on every system with two or more states [GR §3.3]. Which of conditions 3–5 a substratum with further intervention principles would supply, and why its operations should be complex matrices in the first place, are open.

### 4.3 No fixed finite world reproduces a qubit

The correspondence chooses a hidden world for each pattern. A single qubit, the simplest quantum system, can be prepared and measured in infinitely many ways. A fixed finite world with $N$ hidden configurations produces only prepare-and-measure statistics that factor through $N$ states, a fact proved in [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form)]; simulating a qubit's prepare-and-measure statistics needs classical memory without bound over finite experiments, an imported result [HKLP24, Thm 4; GH03], and Montina reports Hardy's result that the number of hidden states cannot be finite [Mon08; Har04]. So for any single finite pattern some finite hidden world reproduces it, but no one fixed finite hidden world reproduces everything a qubit can do.

### 4.4 Bell correlations

Two laboratories far apart share a prepared pair of systems. Each chooses a setting, which measurement to make, and records an outcome $+1$ or $-1$. Bell's theorem asks whether the correlations between the two records can be explained by information the pair carried from the start [Bel64]. For any such explanation a combination $S_{\rm CHSH}$ of the four setting-pair correlations is at most 2 in magnitude [CHSH69], while quantum mechanics reaches $2\sqrt2$.

The framework's own version is this [Main §3.3, Theorem (Bell ceiling for a screened local completion)]. Suppose the hidden world is deterministic; each laboratory's setting acts only on its own region; each outcome is read from a region that the other laboratory's setting cannot influence within the time of the experiment; the settings are chosen independently of the hidden state that precedes them; and an outcome is recorded in every run. Then $|S_{\rm CHSH}|\le2$. The card game obeys the same ceiling when each player's operations and readout stay within that player's range of influence, the deal is independent of the settings, and both players record an outcome in every run [Main §3.3; Book §1.11]. Reproducing quantum Bell correlations therefore requires giving up at least one of these assumptions.

OI keeps determinism and an outcome in every run. It also keeps the independence of the settings, as an assumption about initial conditions, and accepts instead that one laboratory's hidden response may depend on the other laboratory's setting, with no usable signal between them. The nearest-neighbour update of the lattice substratum [SM] cannot supply that dependence for laboratories outside each other's range of influence [Main §3.3, Corollary (Bell–lattice obstruction and state-dependent escape)]. Whether a Bell preparation can add a bounded number of long-range links to the substratum's coupling graph that supply it, while keeping operational no-signalling and the gravitational continuum limit, is an open hypothesis, called H-Bell [Main §3.3; Substratum §3.2].

## 5. Why it matters

### 5.1 Quantum foundations

Because every fixed-measurement pattern can be reproduced by a hidden deterministic world, no record of one repeated measurement can by itself rule out a partly hidden deterministic account of it. The informative content lies in what such accounts must contain: where memory is stored, how much room it needs, and what recurrence does to forecasts. Deterministic systems have been analysed with quantum methods before, for example by 't Hooft [tH14].

If OI holds as physics, with the finite reversible substratum as its representation, then over any finite stretch of time the fixed-measurement statistics of quantum theory are what an embedded observer sees of such a world, and any memory they show is held in its hidden part, where retained records may nevertheless identify it. That reading is conditional on OI and on the modelling choices of section 2.

### 5.2 The energy of empty space

Quantum theory gives empty space an energy: every field keeps a minimum jitter even in its lowest state, and adding up that energy down to the smallest length at which present physics is expected to apply gives a density some 120 orders of magnitude above the observed value, the exact power depending on the cutoff convention [Wei89]. If that density sourced the curvature of spacetime, it would have to be cancelled to that accuracy.

What OI establishes is a distinction of levels. The zero-point sum belongs to the emergent quantum description, the description of the observer's visible statistics, while the effective cosmological constant belongs to the gravitational description of the substratum. Shifting every energy of the quantum description by the same constant changes no visible probability, so the zero-point offset is absent from every visible statistic [GR §6.2]. That no non-gravitational measurement sees the absolute vacuum energy is familiar; what OI adds is the second level, at which a gravitational source can be defined independently of the emergent vacuum.

The proposal goes further. If the field equations of gravity take the form that [GR] targets, whose source is built from the substratum's classical energy and momentum, then the zero-point sum is not a source of curvature and needs no cancellation; the vacuum term that remains is not computed, and the observed value of the cosmological constant is an input. The quantum description alone cannot decide this: a completion in which the offset gravitates and one in which it does not share every visible transition law. Deciding between them requires field equations derived from the substratum, with their coupling to sources, which [GR] leaves open [GR §6.2, §8.5]. Trace-free Einstein equations [EvEMU11] and vacuum-energy sequestering [KP14] also remove matter vacuum energy as a source of curvature, and Volovik argues that the ultraviolet zero-point sum does not set the vacuum energy [Vol06].

### 5.3 Black-hole information: keeping versus showing

The black-hole information problem asks whether the radiation of an evaporating black hole carries the information of what formed it [Haw76; Pag93b]. In OI two questions separate: whether information is conserved by the global dynamics, which holds because the dynamics is reversible, and whether it can be recovered from the records an observer can access [HP07]. A burned letter is a useful analogy: the smoke, ash and heat still encode its words, because the underlying laws lose nothing, yet nobody who sees only the smoke can read it.

Unpublished finite-model research makes the separation exact in small toy models of registers that pass one by one from an "interior" to a "radiation" side, with an observer who reads on a fixed schedule [BHa]. The maps studied range over all reversible and all irreversible maps of the registers; none is derived from the substratum's dynamics. Reversibility does not guarantee recovery: some reversible maps leave a message completely hidden from an observer who reads only the radiation. Nor is reversibility necessary for recovery: some irreversible maps let the message be read exactly when every register is read. What reversibility guarantees is a floor. Reading everything at the end recovers the message, and hiding it completely requires the unread registers to have at least as many joint values as there are possible messages, as in perfect secret sharing, of which Shamir's scheme is the standard example [Sha79].

The Page curve, the expected rise and fall of the radiation's entanglement entropy if information comes out, is a separate matter. [GR, App. A] obtains a cycle-averaged Page curve conditional on a scrambling condition, H-scramble, and a decoupling condition, H-decouple, taking the energy shell of the black hole and its radiation to be their full product space. For the ensemble of definite configurations with the black hole and radiation split along configuration coordinates, every reversible map sends definite configurations to definite configurations, so H-scramble has no instance there and that derivation establishes no Page curve [GR §8.4, App. A.7–A.9; BHb]. A physical recovery model needs a specified coherent preparation or a different partition, a scrambling condition that has instances, and an entropy statement suited to that model.

## 6. What remains open

The results above turn a question about interpretation into mathematics, and the mathematics shows what partial access to a deterministic world can and cannot produce. Turning mathematical representability into a complete physical theory needs the following, none of which is established:

1. **Operational quantum theory.** How complex matrix kinematics and tensor-product composites arise physically, and which of conditions 3–5 of section 4.2 a substratum with intervention principles beyond reversible shuffles supplies [GR §3.3].
2. **Selection principles.** A reason for the quadratic Born rule, and for the evolution relating two times (section 4.1).
3. **Observable memory.** Memory that feeds back into what is seen, at the cosmological partition [GR §2.2], and an experiment or memory-witness test that distinguishes OI from standard quantum theory [Main §4.5].
4. **Dynamical construction.** Exact gluing of the per-stretch realizations of section 3.1 for recurrent multi-time patterns; approximation of a target over short stretches by one fixed substratum [Main §3.4]; and the hidden-sector mixing assumption under which observed memory gives a lower bound on how long the hidden part takes to settle [Main §1.3, §3.4].
5. **Bell correlations.** The hypothesis H-Bell of section 4.4 [Main §3.3; Substratum §3.2].
6. **Gravity.** Covariant field equations derived from the substratum, with their coupling to sources, on which the vacuum-energy proposal of section 5.2 and the gravitational Page-curve argument both depend [GR §6.2, §8.5].
7. **Black holes.** A physical coherent preparation with a scrambling and entropy statement beyond the finite models, the decoupling condition H-decouple, which the effective-pure-state result of [GR, App. A.7] supports only for times short compared with the cosmological timescale, the case of a proper energy shell (which an evaporating black hole whose radiation carries away its energy occupies), the entropy along a single trajectory, the generalized second law [GR App. A.6], and the relation to quantum-extremal-surface and island computations [Pen20; AEMM19; AMMZ20; Book §7.6].

## Where the details are

This paper explains results proved elsewhere and claims no new theorem; earlier work is credited where it is used. Proofs of the results it describes are in the formal papers: the finite-horizon correspondence, hidden memory and its bounds in [Main §§1.3, 1.5, 3.4]; recurrence and failure of chaining in [Main §2.3]; memory, chaining and quantum non-Markovianity in [Main §3.2]; the Bell ceiling in [Main §3.3]; the operational characterization in [GR §3.3]; vacuum energy in [GR §6]; the Page-curve conditions in [GR, App. A]; identification from retained records in [Substratum, Prop. 24.5]. The formal papers state each result with its full hypotheses and identify the results they import from other authors.

Several of these proofs are also checked by computer in the Lean 4 proof assistant with its Mathlib library [dMU21; Mathlib20]. The formal papers name the checked declarations beside the statements they support, and the repository's Lean-to-manuscript census (`verification/lean-manuscript-census.json`) and proof-coverage ledger (`verification/coverage/LEDGER.json`) record which manuscript statement each declaration supports and at what level.

The black-hole toy-model results are unpublished finite-model research: exhaustive enumerations over small register spaces with a proved recovery floor, whose novelty has not been assessed. Their written proofs and code [BHa; BHb] are in `verification/programmes/black-hole-information/`, and the finite probes behind several statements of [Main] are in `papers/oi_lattice_code/foundations/`, both released under the MIT License. The novelty of the operational characterization of section 4.2 and of the result on the evolution relating two times in section 4.1 has also not been assessed.

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
