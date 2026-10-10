# Identical-copy covariance: source audit (read-only, L42 `fdebc6e3`)

**Question.** Does the corpus force two copies of one local system to carry the same distinguished off-classical NOT
extension, i.e. `Σ (N⊗I) Σ⁻¹ = I⊗N` under the canonical copy identification, without SWAP availability or composite
unitary control?

**Answer: not addressed.** Nothing derives it. What the corpus has falls into four groups.

**1. SWAP from control — operational, downstream (circular for K).**
- `FactorExchange.lean`:
  - `conjChannel_swapMat_tensor` (l.87) is pure algebra and has no availability premise.
  - `HasQubitFactorExchange` (l.126) is a premise.
  - `compositeControl_hasFactorExchange` (l.131) obtains it from `HasCompositeUnitaryControl`, and is stated to hold in
    one direction only.

**2. Availability transported along carrier bijections — a premise, and closure rather than identity.**
- `EmbeddedObservation.lean:104`, `RelabellingInvariant`: availability is transported along every carrier bijection.
  - Its own countercontrol (l.50) says: "Bare OI does not supply the principle".
  - `completion-assumption-audit.md:38` says: "The gap is relabelling invariance, which observer recursion does not
    carry."
- Even when assumed, it makes `I⊗N` *available* whenever `N⊗I` is. It does not make copy 2's *distinguished* NOT equal
  to the transported `N`.
- The same holds for `ImplementationLocality` (`ContextStable`, `LabelInvariant`) and `TypedCompletion`'s `relabel`
  rule. These are admissibility statements, and for the derived class (`IsMonomial`) they cover only permutations with
  phases.

**3. An extension that is uniform by definition — stipulated.**
- `LiftAudit.lean`'s `gateFlow σ t = 1 + (e^{iπt} − 1)(1 − permMat σ)/2` is a function of the classical permutation, so
  it is automatically Σ-covariant.
- But it is chosen, not forced. It is used with the ancilla as spectator only, and it is available only "of control"
  (`layerFlowExecutable_of_control`). Other monomial NOT variants remain admissible.

**4. Classical level only.**
- `bijectiveOperator_supplied`, `exchange_monomial` and `permClass` supply the classical NOT truth table and the
  exchanges of basis states.

## Consequence for the theorem's interpretation

The owner's hierarchy stands, as the corpus has it:

| level | status |
| --- | --- |
| native exchanges | sourced |
| the same classical NOT truth table on both copies | sourced (identical carrier plus relabelling of configurations) |
| **the same full ball automorphism `N` on both copies** | **not derived** — the new premise, *identical-copy covariance* |
| operational SWAP | downstream of composite control; must not be used to justify K |

One observation, recorded but not relied on: in `gateFlow` the off-classical extension is defined as a *functional
calculus of the classical permutation*. For such extensions covariance is automatic. A premise of the form "the
distinguished extension of a native permutation is a function of that permutation alone" would imply identical-copy
covariance. Whether that premise is more natural in OI terms than covariance itself is an open, interpretive
question.
