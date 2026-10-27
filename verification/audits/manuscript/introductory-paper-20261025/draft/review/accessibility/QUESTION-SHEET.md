# Introduction paper: reader comprehension questions

One sheet serves two kinds of reader: a scientifically curious non-specialist, and a reader with undergraduate physics.
It is used in two ways:
- **The paper-only AI comprehension review** (required before #918 merges). A fresh reviewer that reads only the paper
  answers these questions. Its answers are recorded verbatim before anyone evaluates them.
- **Human reader testing** (optional before public release; not a merge blocker).

## Instructions for the reader

Read the paper once, at your own pace. Then put it away and answer each question in your own words, in a few sentences.
There are no right phrasings, and you do not need to use the paper's terms. Explain what you understood as you would to
a friend. If a question asks about something you did not follow, say so; that is useful too.

## Questions

1. **The basic idea.** What does the paper mean by "observational incompleteness"? Describe a situation in which
   someone is in this position.

2. **Randomness from hidden information.** How can a world that follows fixed, deterministic rules look random to
   someone inside it? Use an example of your own, or the paper's, and explain why the randomness appears.

3. **The main mathematical result.** In your own words, what does the paper show about the relationship between
   - random-looking (stochastic) observations,
   - deterministic systems with hidden parts, and
   - the records of quantum measurements?

   What does "on a finite time horizon" add?

4. **What the result does not show.** Why does this result not, by itself, show that quantum mechanics comes from
   hidden deterministic information? What would still need to be shown?

5. **Memory.** What does the paper say about memory? When must the hidden part of the world carry information about the
   past, and what can an observer learn about that hidden memory from what they can see?

6. **The two applications.** Why might this way of thinking matter for
   - the cosmological-constant problem (the mismatch between the predicted and observed energy of empty space), and
   - the black-hole information problem?

   For each, what does the paper establish, and what does it leave open?

7. **Anything unclear.** Which part of the paper did you find hardest to follow, or least convincing? Where did you
   have to guess what was meant?

## For the evaluator (not shown to the reader)

Judge each answer against the exact statement in the paper, and through it against its source in Main, GR and the
black-hole records. Look for understanding, not vocabulary. A correct answer in plain words passes. An answer that uses
the right terms but gets the scope wrong fails. Common scope errors:
- treating the correspondence as a derivation of quantum mechanics;
- treating memory as present whenever there is coupling;
- treating the cosmological-constant resolution as demonstrated rather than conditional on the coupling step G3.

Any failure is recorded as a defect in the paper's explanation, not in the reader. The explanation is revised, and the
paper-only test is repeated with a fresh reader.

What a correct answer contains:
1. The observer's description covers only part of the full configuration. The hidden part is inaccessible to the
   observer, not merely unknown to them for now.
2. Hidden states that are compatible with the same visible state send it to different futures. Averaging over what the
   observer cannot see makes the visible evolution stochastic.
3. On every finite horizon, three classes of law coincide:
   - finite stochastic laws;
   - visible marginals of finite reversible deterministic systems;
   - fixed-basis quantum measurement records.

   The equality includes Markov laws, so it is a representation and not a test that singles out quantum behaviour.
4. The result reproduces fixed-basis records only. Full operational quantum theory needs further completion conditions,
   which the paper states are open. The relating evolution between two times is not selected, and the Born exponent is
   not derived. The correspondence represents the statistics; it does not derive a physical mechanism.
5. Conditional memory in the visible law holds exactly when the hidden sector carries readout-relevant predictive
   memory. Visible memory places a lower bound on the size of the hidden sector. Coupling and capacity without readback
   allow zero memory.
6. The cosmological constant:
   - Established: the zero-point sum and the effective cosmological constant sit at different levels of description.
   - Open: removing the 122-digit cancellation needs the coupling step G3.

   Black holes:
   - Established: conservation of information and its accessible recovery are distinct.
   - Open: the Page-curve result rests on named hypotheses.
