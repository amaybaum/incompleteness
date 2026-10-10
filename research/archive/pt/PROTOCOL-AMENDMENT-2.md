# PT protocol — amendment 2 (owner's direction; append-only)

`PROTOCOL.md` (sha256 `239dc123b07cb83f354a0f9def3cc39f5fd025fb2f6b4f3c4ba3d3e0ddfa9b23`) and amendment 1 (sha256
`b41aa0e735b3ca0bf7fb08c3629dd9a18c6d979039c6ba005fd707330831cf83`) are unchanged. This amendment adds to them; where
they differ, this amendment governs.

**Owner's direction (verbatim).**
> "Failing to derive an assumption does not prove that the assumption is independent of the framework.
>
> To establish independence, a thread needs a valid countermodel satisfying the relevant observer-native premises while
> violating the proposed consequence, or a rigorous impossibility theorem. An unsuccessful derivation establishes only an
> unresolved gap.
>
> I would also preserve three levels of mathematical evidence: Lean kernel proofs, written mathematical arguments, and
> exact computational checks. Even a successful exact computation should not be described as a universal theorem unless
> its scope justifies that conclusion."
>
> "The four threads should ultimately distinguish three possible outcomes:
> - Derived: The observer-native foundations genuinely imply the required composite properties.
> - Conditional: The properties follow from additional, independently motivated principles.
> - Independent or unresolved: A valid countermodel proves an additional principle is necessary for the stated
>   implication, or the available research has not settled the question.
>
> The distinction between independent and unresolved is essential."

## What this changes for the threads

**Outcome labels.** In "0. Answer", every target carries exactly one of:
- **DERIVED** — it follows from certified observer-native premises alone ([K] at L, with [W]/[X] steps).
- **CONDITIONAL** — it follows from named additional principles; each is stated precisely and assessed as
  independently motivated or a restatement of the target. A restatement does not make the target CONDITIONAL: the
  target is then UNRESOLVED, with the restatement recorded.
- **INDEPENDENT** — an exact countermodel satisfies every certified observer-native premise that bears on the target
  while violating the target, or a rigorous impossibility theorem holds. List each such premise and the exact check
  (or written argument) that the model satisfies it, and state the scope: "independent of the premises certified at
  L as stated", not of every possible extension of the framework.
- **UNRESOLVED** — neither a derivation nor such a countermodel; give the precise gap.

**Routes versus the framework.** A model that satisfies a particular route's premises but not every certified premise
bearing on the target refutes that route only. Report it as "route refuted", never as INDEPENDENT. A failed derivation
is UNRESOLVED, never INDEPENDENT. The protocol's classes map as follows:
- DERIVED-ON-MAIN → DERIVED;
- DERIVED-CONDITIONAL → CONDITIONAL;
- COUNTEREXAMPLE → INDEPENDENT only under the condition above, otherwise "route refuted";
- GAP → UNRESOLVED.

**Three levels of evidence, kept separate.**
- **Lean kernel proofs.** [K] is certified at L. [D] is kernel-checked in a design run and not certified. UNBUILT Lean
  is not a kernel proof.
- **Written arguments:** [W].
- **Exact computations:** [X]. An exact computation is stated for the instance it checks. It is called universal only
  when its scope justifies it: it is exhaustive over the whole finite object in question, or a written argument lifts
  it, in which case the [W] argument is the evidence for the universal statement.

## The integration review (coordinator)

The integration review classifies each composite property as DERIVED, CONDITIONAL, INDEPENDENT or UNRESOLVED, keeping
INDEPENDENT and UNRESOLVED distinct. It assesses:
- how much of K2 the four threads have actually resolved;
- what remains necessary to reach full finite-dimensional operational quantum mechanics.
