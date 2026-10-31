# Independent paper-only reader answers

I read the paper through once using PDF text extraction, then answered these questions from memory without returning to the paper. I did not inspect the cited companion works, verification code, intended answers, or external sources. These are my understanding of the paper, not independent checks of its proofs.

## 1. The basic idea

Observational incompleteness is the hypothesis that every physical observer is a part of a larger finite world whose complete evolution is deterministic and reversible. The observer reads some coordinates of that world and does not directly read the others. For example, a player watching one of two cards while the other is face down sees only part of a perfectly definite card configuration. Being in that position does not by itself mean the other card can never be inferred from earlier observations.

## 2. Randomness from hidden information

Suppose the face-down card is initially chosen with equal chances of being red or black, and a fixed rule swaps the cards on every step. The player cannot predict the colour after the first swap because the player does not know the hidden card, even though the rule and the actual complete initial state fix the outcome. After two swaps the initially visible card returns with certainty. The probabilities express uncertainty about the initial deal; no new randomness needs to enter the subsequent rule.

## 3. The main mathematical result

For a finite collection of possible observations over a fixed finite stretch of time, every probability law on the resulting sequences can be reproduced by a finite reversible deterministic system with a hidden part. The same set of laws can be represented as the records of a finite unitary quantum system measured in one fixed basis at every step, with a fixed way of turning its outcomes into visible records. One way to construct the deterministic system is to put a sampled entire trajectory and a clock into its hidden register.

The time restriction matters because the realization may be chosen separately for each law and each horizon. A particular finite reversible world eventually repeats, so it cannot reproduce an arbitrary nonperiodic law exactly for all time. This is an exact finite-record correspondence, not a statement that one fixed small world implements all experiments forever.

## 4. What the result does not show

The correspondence covers every probability law, including ordinary memoryless laws, so the existence of such a representation does not select quantum physics or identify nature's mechanism. It concerns one fixed measurement repeated at every step, whereas full quantum theory also involves incompatible measurements, coherent states, interventions, and composite systems. The use of Born probabilities in the quantum representation does not derive the squared-amplitude rule: the permutation examples would work with other positive exponents too.

The paper gives five additional conditions that characterize full finite quantum instruments within an operational theory having specified background structure. It does not show that a physical substratum supplies the substantive control, spectator, and composition conditions. It also leaves selection of the evolution between times open, acknowledges that one fixed finite ontic system cannot reproduce the entire prepare-and-measure theory of a qubit exactly, and leaves a Bell-compatible physical completion to be constructed. Thus mathematical representability is established much more fully than physical quantum emergence.

## 5. Memory

An observed record has conditional memory when earlier observations improve the prediction of the next observation beyond what the current observation alone supplies. If two possible histories end at the same present observation but give different next-step predictions, every faithful deterministic realization must distinguish those histories in its hidden state in a way that affects the next output. The difference between the visible forecasts cannot exceed the difference between the corresponding hidden-state probability distributions.

Observed conditional information therefore gives a lower bound on hidden predictive information and on the hidden sector's capacity. The paper also bounds past-to-future information, giving a minimum number of hidden states needed to support it. Reversibility stores past information even for a memoryless visible law; what distinguishes observable memory is that stored information being used in later visible predictions. Such storage does not require the hidden state to remain unknown: retained observations can sometimes identify it exactly.

## 6. The two applications

For the cosmological constant, the proposed distinction is between the zero-point energy calculated in the emergent quantum description and the source of gravity at the underlying level. Adding the same constant to every quantum energy does not change the visible quantum probabilities, which the paper establishes as an observational invariance. If gravity couples only to the proposed underlying classical stress-energy in the targeted field equations, the enormous emergent zero-point sum would not need to be cancelled against the observed cosmological constant.

The invariance of probabilities does not establish that gravitational coupling. Different gravitational completions can share all the same visible quantum laws while treating the offset differently. Deriving the covariant field equations and their source coupling remains open; the paper does not calculate the observed cosmological constant, which enters as an input, or settle how vacuum transitions gravitate.

For black holes, global reversibility guarantees preservation of information, while recovery depends on which registers an observer reads and retains. The finite computations demonstrate that reversible models can leave a message completely unrecoverable from the chosen radiation records, and that some information-losing models can nevertheless reveal the particular message perfectly. There is also a proved recovery floor tied to the number of unread configurations, with exact recovery when the entire final reversible state is available.

This does not establish a physical black-hole Page curve. The original configuration-state scrambling assumption has no instances for a permutation acting on product basis states at the stated partition: those states remain unentangled. The additional coherent finite constructions supply real mathematical entropy curves, but physical coherent preparation, suitable scrambling, the correct energy shell, coupling to gravity, and sustained decoupling from other sectors remain open.

## 7. Anything unclear

The operational-completion characterization was the hardest part for me to assess after one reading. I could follow the meanings of the five conditions, but keeping track of which preparation, readout, composition, and discard abilities are background assumptions and which are additional conditions was demanding. I understand the stated equivalence as conditional on that whole setup; I have not independently followed its proof, and the paper does not give me a physical mechanism implementing the strongest control assumptions.

The difference between an actual observed law and the family of forecasts from all possible starts also required care. I take the forecasts from never-used starts as mathematical counterfactuals under one stipulated preparation, not as measurements the observer has performed or as proof that the observer can physically perform those preparations. I did not see that as a contradiction, but the physical availability of such preparations is a separate question. The cosmological and Bell proposals remain less convincing to me as physical explanations because their central coupling constructions are expressly still open, rather than because I found a definite error in the finite results.

## 5a. Why use the same hidden setup for every starting state?

The comparison is supposed to ask what one rule and one hidden preparation do when only the visible starting point changes. If the hidden deal also changes with that visible starting point, differences between forecasts can come from the dealer's choices instead of from the evolution. In particular, the bridge from observed histories to the overlapping forecasts needed for the recurrence argument relies on those rows being generated using the same hidden odds. Making the hidden preparation depend on the visible start loses that interpretation and the stated implication cannot simply be carried over.

## 5b. Why include starting states that never occur?

The result concerns the complete rule under the specified hidden preparation, not just the portion sampled by one visible initial distribution. A visible start can have probability zero in that sample while still being a possible starting configuration of the model. Its forecast is needed in the complete table that is compared with the later return to certainty.

Indeed, an unused start can be the only source of overlap preventing that table from being a permutation, even while all actually observed runs look completely predictable. Keeping those starts makes the theorem a statement about the whole setup; it also means its failure of chaining need not be observable in the particular sample. Requiring positive initial probability for every visible start removes that particular gap between the table and the observed starting possibilities.

## 5c. How can dependence exist without appearing in any obtainable record?

The recurrence result looks across a complete cycle of the finite reversible world, while the observer's accessible windows are assumed short compared with that cycle. A hidden trace of the past can remain unused throughout all those windows and affect an output only later, before the eventual return. The mathematics can establish that late dependence even when every available short record is memoryless.

With the common independent hidden preparation and a positive-probability visible start at every root, failure of chaining somewhere across the whole cycle is equivalent to conditional memory at some order before the return. The theorem does not place that order inside an accessible window. If an observer can follow the process through the affected step, different retained histories ending at the same present observation can reveal different next-step probabilities. If the step lies beyond every permitted window, that comparison is unavailable in their records. Without positive probability at every root, failure of the complete forecast table can additionally reside in starts that are never sampled, rather than being an observed memory effect.

## 8. Hidden states and records

Yes. In the known swap game, one reading before the swap and one after it reveal the two card colours, so retaining both identifies both cards and, using the known swap rule, their current positions. The visible process still has memory because the current face-up card alone does not contain all the predictive information in those retained readings.

For a known model and preparation support, collect the initial states compatible with the retained record. A hidden quantity is exactly inferable when it takes the same value for every compatible state; identifying the full state requires only one compatible candidate. For this product readout and known reversible evolution, the paper also relates exact current hidden-state identification to that singleton condition. Longer passive observation can stabilize at a class with several indistinguishable candidates, so neither endless success nor permanent uncertainty follows from being embedded alone. The record retained and the operations permitted matter.

## 9. Finite entropy example

The construction stipulates a coherent preparation: some binary registers start in equal superpositions and the others in zero, and a uniformly sampled invertible binary linear transformation is applied as a reversible configuration permutation. This gives a coherent uniform state on a sampled linear subspace. Both the preparation and the distribution over subspaces are supplied as part of the model; they are not derived from physical black-hole dynamics.

The paper proves an exact entropy formula at each nested coordinate cut in terms of the subspace's intersections with the two sides. In the balanced case it proves an ensemble mean lying within two bits below the tent-shaped maximum and bounded above by it, with zero entropy at the endpoints. This is a finite subspace ensemble result, not the Haar-average Page formula.

The release toy stipulates a definite clock and initially blank radiation registers, then uses clock-controlled swaps to move the same prepared state's interior registers into radiation. During the first release interval the radiation entropy equals the corresponding cut entropy; a mirror Bell-pair preparation gives an exact tent, while the stated unentangled controls give zero. The clock eventually transfers the state back. These are written finite proofs with exact controls, not a Lean-certified evaporation theorem. They leave open a physical preparation and ensemble, energy-shell dynamics, gravitational coupling, physical scrambling, and permanent decoupling of outgoing radiation; the original configuration-state obstruction remains.

## 10. Capacity and the entire future

The finite-block result bounds past-to-future conditional information uniformly over times and all finite future block lengths for one fixed finite permutation and initial law. A separate construction treats the whole infinite visible future as a single variable whose possible values are the exact future sequences actually generated by the finite carrier. There are only finitely many such sequences. It uses ordinary discrete Shannon entropy in bits on that finite image, rather than assuming an unspecified entropy for an arbitrary infinite product space.

For that exact future variable, the information it shares with the past beyond the present is bounded by the hidden predictive information, which is at most the logarithm base two of the hidden-state count. The same capacity bound holds for the supremum over all observation times. Every finite future block is a truncation of the entire-future variable, but the paper does not certify equality of the two supremum constructions or identify this entropy with a separate infinite-product or limiting conditional-entropy formulation.

Neither bound implies permanent uncertainty about the hidden state. Capacity and predictive information concern how much the hidden sector can carry and how its information relates to past and future; exact state inference depends on the compatible-state set left by the actual retained record. The two-reading swap example already shows that positive observable memory and exact hidden-state knowledge can coexist.
