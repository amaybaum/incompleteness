1. **The basic idea.** "Observational incompleteness" means that every observer is itself a part of a larger world. That world is finite and runs by fixed, reversible rules, and the observer can only register some of its parts. The hidden part is not just unknown for now. It is in principle out of the observer's reach, even when the observer always makes the same single measurement. The paper's picture is a card game. Two cards lie on the table, one face up and one face down, and the rules shuffle them in a fixed way. A player who only ever sees the face-up card is in exactly this position. The game is fully determined, but the player cannot see everything that decides what happens next.

2. **Randomness from hidden information.** If the whole world moves by a one-to-one rule, two worlds that look the same to you can differ in their hidden part. Those different hidden parts can send what you see next in different directions. Take the paper's two cards, where each shuffle swaps them and the face-down card was dealt at random. After one swap, the colour you see is whichever card was hidden, so for you it is a coin toss. Nothing random happened in the dynamics. The randomness is your ignorance of the face-down card. After a second swap the original card is back with certainty. So the "randomness" also has a pattern a truly random coin would not have. What you see depends on what you saw two steps ago, not just on what you see now.

3. **The main mathematical result.** Fix a finite set of possible observations and a finite number of steps. Then three collections of patterns are the same collection:
   - every possible probability pattern over sequences of observations;
   - every pattern a deterministic, reversible world with a hidden part can show to someone who sees only the visible part;
   - every pattern of results from a finite quantum system that evolves unitarily and is measured the same fixed way at each step.

   So any random-looking record can be produced by a hidden deterministic world, and also by a fixed-measurement quantum system, and the reverse holds too. One construction is almost a trick. The hidden part stores a whole sequence, drawn in advance, plus a clock, and reveals one entry per step.

   "On a finite time horizon" means the match holds for any chosen number of steps, but not forever. A finite reversible world eventually repeats itself, so one fixed finite world gives a periodic pattern. It cannot reproduce a non-periodic pattern for all time. The hidden world you build also depends on which pattern and which time span you want.

4. **What the result does not show.** It shows only that such a hidden world is possible, not that nature is one. Because every pattern fits, the fact that a fit exists says nothing about any particular pattern.

   It also covers only one fixed measurement repeated every step. Real quantum mechanics has incompatible measurements, superpositions and composite systems. The squared-amplitude Born rule is put in by hand: the unitaries used are permutations, so any power of |U| would work equally well. The result also does not pick out which evolution links two times.

   To get to full quantum mechanics you would need more. Under a stated minimal operational structure, the available operations are exactly the quantum ones if and only if five conditions hold. These are: valid probabilities; trivial helper systems are harmless; untouched bystanders change nothing; every unitary is available; and fresh mixed helpers can be added, used and discarded. The paper shows that observational incompleteness alone does not imply these. A theory that never creates superpositions satisfies it and is not quantum.

   Still open are which of these conditions a physical substratum actually supplies, why the exponent is 2, and how the evolution between times is chosen. The paper also says no single fixed finite hidden world can reproduce everything one qubit can do across all experiments, because that would need unlimited hidden memory.

5. **Memory.** A record "has memory" when the past helps predict the next observation beyond what the present observation already tells you. Whenever the record has memory, every hidden deterministic world that reproduces it must store that information in the hidden part. In the card game, that is the face-down card. Conversely, if any one such world keeps a trace of the past in its hidden part that changes what is seen next, the record has memory.

   The hidden part must also be large enough to hold this. The memory visible in the record is at most the hidden memory, which in turn is at most the hidden part's capacity in bits. So the observer can bound something they cannot see:
   - Measurable memory statistics give a minimum size for the hidden sector.
   - They give the minimum hidden memory any reproducing world must carry.
   - If two pasts ending in the same present lead to noticeably different next-step odds, the observer gets a lower bound on the memory.

   Storing the past is not the same as memory. A reversible world keeps its whole history even when the record is memoryless. Memory is only the part of that store that affects what you see next.

   There is a related point about chaining forecasts. Suppose the hidden part starts with the same odds whatever is visible. Then any visible step that is not fully predictable means that, somewhere in the world's cycle before it repeats, forecasts cannot be built up step by step. The paper calls this P-indivisibility. That failure may lie beyond any window an observer can actually reach.

6. **The two applications.**
   - **Cosmological constant.** Adding up the zero-point jitter of quantum fields gives a vacuum energy about 120 orders of magnitude above what is observed. In this framework, that jitter belongs to the observer's emergent quantum description. Gravity and the cosmological constant belong to the description of the underlying world. Shifting all quantum energies by a constant changes no observable probability.
     - *Established:* the two quantities live at different levels of description.
     - *Proposed:* if the gravitational field equations take a particular form, the zero-point sum does not curve spacetime and no fine cancellation is needed.
     - *Open:* those field equations are not derived. The same underlying world is compatible both with the offset gravitating and with it not gravitating. The observed value of the constant is still put in by hand, not computed.
   - **Black-hole information.** The framework separates two questions: whether information is kept by the global dynamics, and whether an observer can recover it from the records they can access. The analogy is a burned letter, whose words survive in the smoke but cannot be read.
     - *Established, in small exhaustive toy models:* conservation does not imply recovery. Many reversible maps leave a message completely hidden from an observer who reads only the "radiation". Recovery does not need conservation either, since some information-losing maps still reveal the message. There is also a proved floor: hiding a message completely requires at least as many possible unread values as there are messages.
     - *Conditional:* a Page-curve result, where the radiation's entanglement rises and falls on average over a cycle, holds under conditions of thorough scrambling, isolation and constant energy.
     - *Open:* the scrambling condition fails for the natural kind of bijection, the isolation condition is not established, and real evaporation does not keep energy constant. So whether the Page curve actually follows is left open.

7. **Anything unclear.**
   - **Section 2.5 was the hardest part.** It covers the "rooted" forecast tables that keep rows for starting states that never occur, and the hidden prior "shared by every root and drawn independently of it". I followed the card examples, but not fully why rows for impossible starts should count physically. I also didn't follow how "order k below the recurrence time" relates to the windows an observer can reach.
   - **The main equivalence felt less impressive than its billing.** The realization can simply store a pre-drawn sequence, and it is chosen per pattern and per time span, so it can feel almost tautological. The paper says this itself: the result is about possibility, and the content lies in the memory results.
   - **The step from observational incompleteness to physics was hard to judge.** The five completion conditions are stated abstractly, and it is unclear whether any substratum meets them. The cosmological-constant section is mainly a proposal resting on field equations that are not derived.
   - **The Page-curve part seemed to undercut itself.** Its key scrambling condition is said to fail for every bijection of the relevant kind, and I had to guess what remains of the claim.
   - **Much depends on other works.** A lot is deferred to the companion papers ([Main], [GR]) and to unpublished records. I could not check those, so I had to take several statements, such as the Bell section and the black-hole counts, on trust.