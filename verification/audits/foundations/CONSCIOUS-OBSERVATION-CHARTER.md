# CONSC-1 research charter — physical registration, empirical observation, and conscious perspective

> **Status — exploratory conceptual audit; merge-held.** This thread does not alter the physics core, any Lean definition, any theorem status, or the empirical standing of the framework. Consciousness remains a conjectural extension. The thread exists to determine whether the corpus currently uses *observation* for two importantly different notions and, if so, how to state the distinction without importing consciousness into physical measurement dynamics.

**Base:** `00ee70a60cf59d421c0056619709459d704fae99`.

## The question

The current framework deliberately does **not** require consciousness for physical observation: an embedded subsystem can interact with its complement, records can form, and the operational trace-out/partition machinery applies without a conscious subject. Chapter 18 §18.10 separately says that the framework's mathematical operation of observation is a necessary but not sufficient condition for consciousness, while explicitly declining to solve the hard problem.

There is nevertheless a second direction of dependence worth auditing:

- a physical world appears necessary for physically realized conscious observers;
- but physical registrations become *empirical evidence* and hence part of *observational physics as knowledge* only insofar as there is some perspective for which they are experienced or otherwise epistemically available.

These directions are not automatically contradictory: the first is causal/ontological and the second epistemic. The thread asks whether the framework should make that asymmetry explicit, and whether its foundational phrase **"observation occurs"** presently conflates physical registration with experienced empirical observation.

## Working distinctions to test, not conclusions to assume

The audit will test whether the corpus is clearer if it distinguishes three levels:

1. **Physical registration** — a physical interaction creates a correlation or durable record. No consciousness is required.
2. **Operational observation** — the framework's present mathematical object: an embedded physical subsystem with partial access, readout, partition/trace-out, and the relevant C1–C4 structure. No consciousness is required by the mathematics.
3. **Empirical observation** — an operationally available record functions as evidence for a conscious perspective and can enter an empirical theory.

The third item is intentionally **not** a proposed Lean primitive. The audit must decide whether it belongs only to epistemology/book exposition, whether it exposes a genuine ambiguity in the foundational wording, or whether the distinction can be rejected as unnecessary.

## Targets

### COBS-1 — corpus census

Locate and classify the live uses of *observation*, *observer*, *registration*, *record*, *experience*, *awareness*, *consciousness*, *first-person*, and related language in:

- the physics-core papers, especially Main/Substratum/Methodology;
- Book Chapters 0–4, 12 and 18 plus Appendix C;
- the Explainer as frozen exposition;
- any verification note whose wording bears directly on the observer primitive.

For every potentially load-bearing use, record whether the text means physical registration, the operational observer definition, empirical evidence, or phenomenal experience.

### COBS-2 — two-arrow logical analysis

State the two candidate dependencies separately:

```
physical world -> physical observer/registration -> possible consciousness
conscious perspective -> experienced evidence -> empirical physics as knowledge
```

Determine whether the corpus already distinguishes causal/ontological dependence from epistemic dependence. Report any sentence that incorrectly turns one direction into the other.

### COBS-3 — foundational-primitive audit

Re-read the Methodology treatment of **"observation occurs"**, especially:

- tokened differentiation;
- the adopted perspectival reading;
- the observer locus `V ⊊ S`;
- "registering from a locus";
- the claim that embeddedness belongs to the primitive.

Decide whether these are fully physical/structural notions or whether the prose tacitly relies on a phenomenal first-person notion that the formal definition does not contain.

The allowed outcomes are:

- **STRUCTURAL-ONLY** — no foundational ambiguity; the consciousness issue belongs entirely downstream;
- **TERMINOLOGY-SPLIT** — the mathematics is unchanged but the prose should distinguish registration/operational observation from empirical observation;
- **FOUNDATIONAL-QUESTION** — a genuine unresolved premise-level ambiguity exists and requires a separately authorized foundations round;
- **UNDECIDED** — evidence does not settle the issue.

This thread itself may not promote **FOUNDATIONAL-QUESTION** into a changed axiom or theorem.

### COBS-4 — Chapter 18 consistency

Audit the current asymmetric claim:

> operational observation is necessary but not sufficient for consciousness.

Ask separately whether the book should also state the converse epistemic point:

> consciousness is not necessary for physical registration, but some form of conscious perspective may be necessary for a registration to constitute *experienced empirical evidence*.

The audit must distinguish a definitional/epistemological claim from a dynamical claim and must not present the second sentence as an established scientific theorem.

### COBS-5 — self-referential closure

Assess whether the following loop is a useful and defensible statement of the framework's epistemology:

```
S
-> physical observer
-> conscious perspective
-> partial observations/evidence about S
-> reconstructed physics of S
```

If retained, say exactly which arrows are supplied by the physics core, which are biological/emergent, and which remain conjectural or philosophical. In particular, the arrow from physical organization to phenomenal experience is not presently derived.

### COBS-6 — manuscript consequence

Return a minimal change set, if any, for:

- Chapter 18 §18.10;
- Chapter 1 / the foundational observation definition;
- Chapter 4 / Methodology;
- Appendix C;
- the glossary and reader-facing summaries.

Changes should clarify scope rather than enlarge the physics claims. If no change is needed, say so.

## Guardrails

1. **No consciousness-causes-collapse claim.** Consciousness is not to be inserted into the physical measurement dynamics.
2. **No consciousness requirement for physical records.** Detectors, environments, and other physical systems may register outcomes without conscious access.
3. **No hard-problem solution.** The thread does not derive phenomenal character from structural or informational facts.
4. **No panpsychism, idealism, dualism, or physicalism is adopted by default.** Compatibility may be discussed; endorsement requires a separate argument.
5. **No Lean changes.** Any proposed modification to a core definition or theorem requires a separately chartered, owner-authorized round.
6. **No evidential bootstrapping.** The consciousness extension contributes no evidential support to the physics core.
7. **No anthropocentric restriction.** If an epistemic role for consciousness is discussed, it is about conscious perspectives in general, not humans specifically.
8. **Keep modality explicit.** Claims such as "consciousness is required for empirical evidence" are philosophical/epistemological claims unless independently operationalized and tested.

## Deliverable

The thread should return one result note with:

- the corpus census;
- the classification of each potentially ambiguous use;
- a verdict under COBS-3;
- the status of the two-arrow analysis;
- whether Chapter 18's present one-way statement should be supplemented;
- exact proposed manuscript edits, if any;
- a clear boundary between **physical registration**, **operational observation**, **empirical evidence**, and **phenomenal consciousness**;
- unresolved questions and what evidence or argument would settle them.

No manuscript edit is authorized by this charter alone.
