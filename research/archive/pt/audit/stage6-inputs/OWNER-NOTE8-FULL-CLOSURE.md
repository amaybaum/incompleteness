# Owner's note directing the complete OI premise-closure audit (received 2026-10-10, about 16:50Z; audit input)

Placed under `pt/audit/` (excluded from the threads' sweeps). Standing holds unchanged: research-only work continues
under the already approved authorization; branches, PRs, CI and governed rounds remain on hold; no repository
change, no publication. The note arrived while stage 5 (Q-EX-BRIDGE) was running; stage 5 is left to finish under
its frozen protocol, and this note opens stage 6 (Q-EX-FULL), whose steps 1–2 (inventory, dependency graph) do not
depend on stage 5 and start at once, and whose steps 3–4 consume the audited stage-4 and stage-5 records.

Three directions taken from it: (1) the next round tests the complete existing OI framework at the frozen base,
every axiom, condition, lemma and relevant theorem, each with its actual status (proved / independently assumed /
conditional / empirically motivated / refuted / open), none assumed true by inclusion; (2) the four-step procedure
(complete premise inventory; dependency graph; reassessment of every stage-4 countermodel against every applicable
constraint, with the hidden-history level and the composite-cone level kept apart unless a proved bridge connects
them; the test of (b) against the complete applicable premises, with the missing assumption isolated if it fails);
(3) stage 4 preserved exactly as archived; the audit read-only, before any governed round. The closing question
about branches is answered in the coordinator's reply, not here.

----- BEGIN VERBATIM (owner's assessment and direction) -----
Does this include all axioms and conditions in OI?

No. Stage 4 does not cover every axiom and condition in Observational Incompleteness (OI).

It establishes its conclusions within a specific mathematical setting, using selected OI assumptions, the certified two-system framework, and additional conditions such as trace self-duality.

This distinction is crucial:

* What Stage 4 establishes: The composite operation principle (b) does not follow from the particular assumptions tested, including H1–H3 and the specified pair premises.

* What Stage 4 does not establish: That (b) cannot be derived from the complete OI framework, including its other axioms, observer principles, consistency requirements, and structural conditions.

Consequently, we should not yet conclude that OI needs a new axiom. An existing principle outside the Stage 4 assumption set might already provide the missing implication.

### What the repository actually includes

I checked the certified repository at `9f9f8257`. The relevant assumptions occupy different layers:

| OI layer | Covered by Stage 4? |
| --- | --- |
| Axiom 1: Tokened differentiation occurs | Not explicitly tested |
| Axiom 2: Differentiation recurs | Not explicitly tested |
| C1–C4: Coupling, memory persistence, capacity, history readback | Not jointly tested |
| Finite reversible dynamics and | Background results, not a complete operational selector |
| Pair geometry, symmetry and trace self-duality | Yes, within the specified assumptions |
| Full operational composition principles (OI⁺) | Not assumed as a complete package |
| K∞, K2 and Kₙ reconstruction obligations | Not fully discharged |

Sources: Methodology §6, Main §1.3, and the Verification roadmap.

### An important existing result

The repository already contains a stronger warning against assuming that bare OI automatically produces full quantum mechanics.

Its formal operational characterization proves that five conditions together select finite operational quantum mechanics: valid probabilities, trivial-ancilla consistency, inert spectators, full reversible control, and iterated composition.

It also records countermodels showing that the individual conditions do not follow from the formalized OI core. The compressed OI⁺ characterization uses observational independence, reversible richness and observer recursion alongside well-formedness.

See Verification README, flagship result.

Therefore, assuming all of OI⁺ would select operational quantum mechanics, but that would not prove the missing conditions follow from the two foundational observation axioms.

### What I would change about the next research step

Before introducing any new principle, I recommend a full OI premise-closure audit.

It should ask whether every Stage 4 exotic countermodel remains possible when all applicable, independently justified OI assumptions and consequences are enforced simultaneously.

Crucially, it must distinguish assumptions about hidden deterministic histories from assumptions about composite state cones. They cannot be transferred between mathematical levels without a proved bridge.

The decisive result would be either a derivation of (b) from the complete applicable observer-native premises, or an explicit countermodel satisfying those premises while violating (b).

Bottom line: Stage 4 settles an important conditional classification, but it does not yet certify that every existing OI constraint has been exhausted. A full premise-closure audit should precede the decision to add another axiom.

Ok yeah so we should include all existing axioms, conditions and lemmas.

Agreed. The next round should test the complete existing OI framework, not just the subset of assumptions used in Stage 4.

This is important because Stage 4 established independence from H1–H3 and the specified pair premises, but that does not establish independence from everything OI has already developed.

I recommend naming the next round Q-EX-FULL: Complete OI Premise Closure.

### What the audit should include

| Layer | What must be considered |
| --- | --- |
| Foundational axioms | Axiom 1 (tokened differentiation), Axiom 2 (recurrence) |
| Observer structure | Embeddedness, visible/hidden partition, finite resolution, reversible realization |
| Hidden-sector conditions | C1–C4, including structural persistence, capacity and history readback |
| Established theorems | Finite-horizon equivalence, hidden-memory results, recurrence, canonical predictive quotient |
| Operational foundations | K∞, OPACT, orbit generation, available effects, reversible transformations |
| Composite reconstruction | K1, K2, DIM-1, native gates, local tomography, positivity, self-duality |
| Generalization | Kₙ, implementation locality, observer recursion and OI⁺ characterizations |
| Other OI results | Relevant constraints from Main, SM, GR, Substratum and the remaining certified corpus |

An essential distinction: including a condition in the audit does not mean assuming it is true. Every item must retain its actual status: proved, independently assumed, conditional, empirically motivated, refuted or open.

For example, assuming all the OI⁺ completion conditions would already select finite operational quantum mechanics. That would make the desired conclusion circular rather than derive it from foundational OI.

### The procedure

1. Build a complete premise inventory. Enumerate every existing axiom, condition, lemma and relevant theorem at the frozen certified base. Record its exact statement, provenance, assumptions and applicability. Nothing should be excluded merely because it appears unrelated to quantum mechanics.

2. Construct the dependency graph. Determine what follows from the foundational axioms, what follows only when C1–C4 apply, and what depends on additional operational or physical hypotheses. Include previously proved lemmas through their dependencies rather than silently treating them as independent premises.

3. Reassess all exotic countermodels. Check whether each Stage 4 alternative satisfies every applicable OI constraint. A cone-level countermodel does not automatically establish the existence of a compatible embedded-observer realization.

4. Test the missing implication. Determine whether the complete applicable OI premises force the required off-frame composite mixing or operation-extension principle (b). If not, identify a countermodel satisfying the full applicable premise set and isolate the genuinely missing assumption.

### The critical mathematical point

There is a useful limitation to remember.

If Stage 4 already proved that H1–H3 do not imply (b), adding lemmas that are only logical consequences of H1–H3 cannot change that conclusion.

The opportunity is that other established OI principles, their interaction, or a previously unused bridge between mathematical levels may impose additional restrictions.

The result should therefore distinguish:

Complete OI premises — Derivation: OI itself forces (b) — Independence: A full OI-compatible countermodel survives

I would also preserve Stage 4 exactly as archived and perform this as a new read-only research audit before any governed implementation round.

The objective is no longer merely to find additional assumptions sufficient for quantum mechanics. It is to establish exactly how much of quantum mechanics follows from everything OI already contains, without importing the conclusion as a premise.

That is the appropriate next test before deciding whether any additional axiom is genuinely necessary.

Can we create branches in the repo for all of these open threads, and work on them in parallel?
----- END VERBATIM -----
