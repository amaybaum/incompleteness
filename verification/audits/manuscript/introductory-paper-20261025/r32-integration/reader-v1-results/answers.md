# Paper-only reader answers

I read the paper once, put it away, and answered from memory. I did not consult the cited sources or verify the paper's proofs or computations.

## 1. The basic idea

Observational incompleteness is the proposal that a physical observer is part of a finite world whose complete state evolves deterministically and reversibly, while the observer reads only some of that state. For example, a player sees one of two cards while a fixed rule swaps it with the face-down card. The player lacks a direct reading of the face-down card at that moment. That does not necessarily prevent the player from working out its value from earlier observations.

## 2. Randomness from hidden information

In the two-card game, suppose the face-down card was initially chosen fairly and independently of the visible card. A swap has a completely determined outcome given both cards, but the player who knows only the visible card cannot predict the next colour better than chance. A second swap returns the original visible card with certainty. The apparent randomness comes from uncertainty about the initial hidden card, rather than any random event in the subsequent swapping rule.

## 3. The main mathematical result

For any chosen finite sequence length and finite set of visible outcomes, every probability distribution over sequences can be reproduced by some finite reversible deterministic system with hidden variables. The same sequence distributions can also be represented as records of a finite quantum system measured in a single fixed basis at every step, allowing the reported outcome to be a function of the measurement outcome. Thus these three descriptions allow exactly the same finite record statistics, including ordinary memoryless processes.

A finite horizon means the match is guaranteed over a specified number of steps. The hidden system can be chosen for that law and horizon; the result does not supply one fixed finite system for all horizons. A finite reversible system eventually returns, so it cannot reproduce an arbitrary nonperiodic process exactly forever.

## 4. What the result does not show

An existence result this broad does not establish which mechanism nature uses: it can represent every finite law, so representability itself selects no particular physical law. Moreover, repeating one fixed measurement is less than full quantum mechanics, which includes incompatible measurements, coherent states, and operations on composite systems. The paper gives extra operational conditions under which the available operations are exactly quantum instruments, but does not derive those conditions from observational incompleteness.

There are further selection problems: the permutation representations do not pick out the squared Born exponent, and identical visible records do not uniquely determine the quantum evolution connecting two times. A physical account also needs to handle Bell correlations consistently; the proposed microscopic dependence on the remote setting, while preserving usable no-signalling, is still a hypothesis. The paper also distinguishes choosing a finite model for each experiment from reproducing the entire prepare-and-measure behaviour of a qubit with one fixed finite hidden model, which it says cannot be done exactly.

## 5. Memory

A visible process has memory when two observed pasts that end at the same present observation lead to different predictions for the next observation. In every deterministic hidden realization of that process, the hidden state must then retain information that distinguishes those pasts and affects the next readout. The difference between the two visible predictions cannot exceed the difference between the corresponding hidden-state probability distributions.

Visible conditional information therefore gives a lower bound on hidden predictive information and on the number of hidden states needed; information shared between the past and a future block can give a stronger size constraint than just the next output. Reversibility also preserves past information even for a memoryless visible process, so storing a past and feeding it back into the next observation are different things. These bounds do not say that the observer can never identify the hidden state from a long enough retained record.

## 6. The two applications

For the cosmological constant, the proposed distinction is between the energy bookkeeping of the observer's emergent quantum description and the underlying world's gravitational source. Adding the same constant to the emergent Hamiltonian changes no visible transition probability. This supports treating the zero-point sum and the effective cosmological constant as quantities belonging to different descriptions, rather than immediately equating them.

It does not establish that the zero-point offset fails to gravitate. Different gravitational couplings can have the same visible quantum statistics, and deciding between them requires field equations derived from the underlying model. The proposed source equation would remove the need to cancel the huge emergent zero-point sum, but that equation is not derived, and the observed cosmological constant is still an input rather than a computed value. The relation of the mismatch to horizon entropy is described as a dimensional identity, not the missing gravitational derivation.

For black holes, reversibility guarantees that global information is preserved, but it does not guarantee that radiation records accessible to a particular observer reveal a message. The finite examples separate these questions: some reversible maps hide the message from the available records, while some information-losing maps still reveal the message. Bijectivity also gives a recovery floor depending on the number of unread configurations; reading the complete final configuration permits exact recovery in the toy setting.

The original configuration-state Page-curve construction has a serious obstruction: permutations take basis product states to basis product states, so they cannot supply the quantum scrambling assumed there. The coherent finite examples establish genuine entropy profiles and reversible release trajectories under stipulated preparations, but do not establish a physical evaporating-black-hole Page curve. Physical preparation, suitable scrambling, decoupling from the other sectors, energy-shell dynamics, and gravitational coupling remain open.

## 7. Anything unclear

The operational-completion theorem was the hardest mathematical part for me to assess. I understood the five conditions and their role, but the distinctions among closure under conditioned operations, inert spectators, and the further iterated-ancilla condition were technically dense; I could not reconstruct their independence arguments from this reading. I accepted the stated theorem and its stated machine-check status rather than independently understanding its proof.

The biggest physical uncertainty is how the proposed gravitational source would actually be selected. The paper is clear that unchanged visible quantum probabilities cannot decide that issue, so I did not read the cosmological discussion as an established solution. Likewise, I understood the finite coherent entropy example as a controlled construction, but not as evidence that actual black holes implement its preparation or ensemble. I did not have to guess the basic scope of these claims; their unresolved physical mechanisms were the limiting point for me.

## 5a. The same hidden setup for every start

The comparison is meant to ask what one physical preparation and one evolution rule do when started with different visible values. If the hidden deal changes with the visible start, differences between the forecasts can reflect different experiments rather than the evolution of one common setup. In particular, the argument that observed histories imply overlapping forecast rows relies on using the same hidden odds for the different starts; a start-dependent preparation need not support that inference.

This is an extra assumption of the recurrence comparison, not a restriction needed for the general finite-horizon representation theorem. I would not understand the paper as claiming that every correlated hidden preparation automatically obeys the same recurrence-memory conclusion.

## 5b. Starting states that never occur

The theorem compares the full rule under the common hidden preparation, including what it would do if started at each possible visible value. A start with zero weight in the actual preparation is absent from the observed sample, but it still has a well-defined forecast in that comparison. Keeping every row allows comparison with the full return-to-certainty table and can expose overlap that occurs only in an unobserved row.

Consequently, the theorem may find a failure of chaining in the mathematical family even when the actual observed process is completely predictable. Such a result is about the rule and preparation under alternative starts, not an assertion that the observer has measured those forecasts. The paper adds a full-support qualification when equating whole-cycle failure with conditional memory in the actual law.

## 5c. Mathematical dependence outside obtainable records

The finite world has a whole recurrence cycle, whereas an observer's accessible observation windows may cover only a short part of it. A hidden record can survive through apparently memoryless observations and affect the visible output only much later, before the eventual return. Under the stated assumptions, the complete forecast family must fail to chain somewhere in the cycle, but that place need not be within an accessible window.

For example, independent early bits can be followed later by a repetition of the first bit. Before that repetition, the observations can look memoryless; at the repetition, the earlier bit becomes predictive beyond what the immediately preceding bit tells. If the observer reaches and retains that step, it can witness the dependence. If every available window ends earlier, the dependence remains a property of the full dynamics without appearing in any record the observer can obtain. There is also the separate limitation that a whole-family obstruction may involve starts never present in the actual sample.

## 8. Hidden states and records

Yes. With a known swapping rule, the first reading gives the original visible card and the second gives the original hidden card, so retaining both determines both cards and hence their current positions. The process still has memory because prediction from only the current visible card differs from prediction using the retained past.

More generally, collect the initial configurations compatible with the known preparation and retained record. A hidden quantity is identified if it has the same value on all remaining candidates; identifying the entire state requires a single candidate. The known dynamics can translate this criterion to a quantity of the current state. Being embedded alone does not settle inferability: it depends on the model, preparation support, retained observations, and permitted operations. Even when passive records stop refining the candidate classes, those classes need not be singletons.

## 9. Finite entropy example

The construction stipulates an initially coherent product preparation: some binary registers are in equal superpositions and the rest in definite zero states. It then samples an invertible binary linear map, whose reversible permutation produces a coherent uniform state on a subspace. The sampled state is held fixed while its entropy is examined across successive coordinate cuts. The proof supplies an exact entropy formula and bounds on the ensemble mean that have a rising-and-falling profile; this is not the Haar-random Page average.

The release toy additionally stipulates initially blank radiation registers and a definite clock that controls sequential swaps from the interior. During the first release interval, the actual radiation entropy follows that same state's cut profile. A special Bell-pair preparation gives an exact tent profile, while configuration inputs or an unmixed coherent product give zero entropy. The clock's later evolution returns the state, so this is a finite reversible release example rather than permanent evaporation.

These are finite written proofs with exact controls. They do not repair the claim about scrambling of configuration product states: that obstruction remains. Deriving the coherent preparation, a physical scrambling and entropy ensemble statement, dynamics on the proper energy shell, gravitational coupling, and sustained decoupling of emitted radiation and other sectors are still needed for a physical black-hole Page curve.

## 10. Capacity

The checked result bounds the supremum of conditional information between the visible past and every finite future block, uniformly over time, for one actual finite permutation system and initial law. That is not itself a certification of conditional information about a literal infinite future; the paper explicitly leaves an additional identification argument outside that checked statement.

The bound says that information linking the past to visible future outputs, beyond what the present reveals, cannot exceed the hidden sector's bit capacity. Equivalently, a measured amount of that information imposes a minimum hidden-state count. It does not imply permanent uncertainty about the hidden state: retained records can identify it, as in the two-reading swap example, while its role in carrying predictive information remains.
