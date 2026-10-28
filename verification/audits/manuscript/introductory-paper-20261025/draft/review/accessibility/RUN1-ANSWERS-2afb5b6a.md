## Answers

### Q1
"Observational incompleteness" (OI) is the hypothesis that every observer is part of a bigger, finite world that runs on fixed, reversible rules, and that the observer can only ever see part of that world. The rest is hidden. The paper stresses that the hidden part can't be reached at all, which is stronger than just "not known yet." Its own picture is a card game. Two cards lie on a table, one face up and one face down, and each shuffle swaps them. The player sees only the face-up card. The rules are fully fixed, but the player still can't predict what they'll see, because part of the state is face down.

### Q2
Suppose the whole world follows exact rules, and those rules never merge two states into one (that is what "reversible" means here). Several different hidden states can sit behind the exact same visible state, and they lead to different futures. The observer can't tell which hidden state they are in, so the next thing they see looks like a coin toss.

In the two-card game, after one shuffle the player has a 50/50 chance of seeing either colour, because the colour depends on the face-down card. After a second shuffle, the original card is back for certain. So the "randomness" is the player's ignorance, not something in the rules. It also shows something else: what the player sees next depends on what they saw earlier, not just on what is showing now. The paper calls this memory, and the face-down card is where it is stored.

### Q3
The paper compares three collections of possible patterns of observations over some fixed number of steps:
- every probability pattern at all;
- every pattern a partly hidden, reversible, deterministic world can show its observer;
- every pattern you get by measuring a finite quantum system the same way at every step.

Its Theorem 1 says these three collections are exactly the same. Any random-looking record can be produced by some hidden deterministic world, and also by a quantum system measured repeatedly in one fixed way. In the other direction, records of that quantum kind contain nothing a hidden deterministic world couldn't reproduce.

"On a finite time horizon" means the match holds for a chosen stretch of steps, not forever. A finite reversible world eventually cycles back to where it started, so it repeats with some period. A single fixed finite world therefore can't reproduce a pattern that never repeats over all time. You build a world for each stretch of time you care about.

### Q4
The result only says such a hidden model is possible. It says nothing about whether nature actually works that way. Because every pattern whatsoever can be produced, the result doesn't pick out anything specific to quantum mechanics.

The paper lists what is missing:
- The result covers only one fixed kind of measurement, repeated. Real quantum mechanics also has measurements that can't be done together, superpositions, and combined systems.
- It doesn't explain why quantum probabilities come from squaring amplitudes (the "Born exponent"). The squaring is built into the definition rather than derived.
- It doesn't fix how the system evolves between two times.
- It describes the statistics without supplying a physical mechanism.

To get full operational quantum mechanics, the paper gives five conditions on what operations an experimenter can perform. Its Theorem 4 says these five conditions together are exactly what makes the available operations those of quantum theory. OI does not imply them; the paper gives a qubit example that fits OI and isn't quantum. What remains to be shown is that a real physical substratum (the hidden deterministic world) actually satisfies these conditions, especially the last three. Other open items are Bell-type correlations, which need a hypothesis it calls H-Bell, and the squaring rule.

### Q5
Sometimes what you see next depends on your earlier observations, not just on what you see now. Whenever that happens, every hidden deterministic world that reproduces your record must store that information in its hidden part. The next observation depends on the past only through what the hidden state holds.

The observer can learn something about this hidden memory:
- The amount of memory visible in the record gives a lower bound on how much the hidden part must store.
- That in turn gives a minimum size for the hidden part, measured in bits.
- If two different pasts that end at the same present lead to noticeably different predictions, you get a concrete lower bound on the memory.

So measuring the visible record puts limits on something you can't see.

The paper also gives a checklist of four conditions a hidden part needs in order to produce observable memory:
- it affects what is seen;
- it keeps what it recorded;
- it has room to store it;
- it feeds the record back into what is seen.

Without the feedback, there is no memory. A fair coin is the example: it can have the other three properties and still show no memory.

There is also a result about "chaining" forecasts, where a forecast from start to time 2 is built from start-to-1 and 1-to-2. Because a finite reversible world returns to its start, any step that isn't fully predictable means chaining fails somewhere in the cycle. When every starting point has some chance, that failure happens exactly when the record has memory at some point before the return. I followed the gist of this but not every condition, such as the hidden starting odds having to be the same whatever is visible at the start.

### Q6
(a) **Cosmological constant.** Adding up the "jitter" energy of quantum fields gives a vacuum energy about 120 orders of magnitude bigger than what is observed.

What the paper establishes: in OI, that jitter belongs to the observer's emergent quantum description, while the cosmological constant belongs to the description of the underlying deterministic world. These are two different levels. It also shows that shifting all quantum energies by the same constant changes no observable probability.

What it proposes but leaves open: if gravity's field equations take a particular form, in which gravity responds only to the underlying world's classical energy, then the huge jitter energy doesn't curve space and needs no cancelling. But the quantum description alone can't tell whether that offset acts as a source of gravity. Settling it requires deriving the gravitational field equations from the substratum, which hasn't been done. The remaining vacuum term isn't computed, and the observed value is taken from measurement.

(b) **Black-hole information.** The paper separates two questions: is information preserved, and can an observer recover it from what they can access? Reversibility guarantees preservation. Small exact toy-model computations show that recovery is a separate matter:
- many reversible maps keep the message completely hidden from someone who reads only the "radiation";
- some non-reversible maps still let you recover the message;
- reversibility does guarantee recovery if you read everything, and it sets a floor: the message can stay fully hidden only if the unread part has at least as many possible values as there are messages.

The analogy is a burned letter. Its information is in the smoke and ash, but you can't read it from the smoke alone.

What is left open: the Page curve (the expected rise and fall of the radiation's entanglement over the black hole's life) rests on two conditions, H-scramble and H-decouple. These are not established, and the scrambling one actually fails for the simple kind of deterministic dynamics described. The paper also lists as open the field equations, the case where the black hole's energy actually changes as it radiates, and the connection to modern "island" calculations.

### Q7
The hardest parts to follow:
- **Section 2.5 (recurrence and indivisibility)** was dense. It packs in many qualifiers: "a hidden prior shared by every root and drawn independently of it", "roots of visible probability zero included", "full-support visible prior". I had to guess why the zero-probability starting points need to be counted, and how this kind of indivisibility differs from memory. The paper says it holds even for memoryless laws, which confused me at first.
- **Section 3.1 (three notions kept apart)** and **Section 3.3 (the evolution between two times is not selected)** went over my head: "coherent lifts", "time-dependent right action", "quotient by visible equality".
- **The Bell section** introduced coupling graphs, causal cones and H-Bell quickly. I only got the plain-terms summary: the framework accepts that one lab's hidden response can depend on the other lab's setting, as long as no usable signal passes between them.
- **The black-hole Page-curve paragraph** relies on material in another paper.

In general, much of the detail is pushed to companion papers ([Main], [GR]), so I often had to trust the "in plain terms" summaries. Those summaries were helpful. I was also left wondering why Theorem 1 matters much, given that the paper itself says it holds for every possible pattern and so selects nothing. The paper seems aware of this and puts the real content in the memory results.

## Self-assessment
- **Non-specialist: Partly.** The card analogy, the "in plain terms" paragraphs and the summary carry the main idea and findings, but the formal sections in between are hard going.
- **Physics undergraduate: Partly.** The setup, Theorem 1, the memory bounds and the vacuum-energy argument are followable, but sections 2.5 and 3.1–3.5 and the Page-curve discussion lean on the companion papers and specialist vocabulary.
- **Professional physicist: Yes, mostly.** Theorems are stated precisely, assumptions are flagged, each result is marked as machine-checked, proved on paper or tested by exact probe, and Appendix A gives Lean declaration names and line numbers. Many proofs, though, are only in the companion papers.