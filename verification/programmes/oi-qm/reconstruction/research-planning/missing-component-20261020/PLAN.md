# The missing component for F2-reg: what OI lacks, and whether measurement supplies it

Research only (consistency axis, §A.23). No premise is adopted, no status changes, no round, F or E. Base: `main` at
`df9e601ebe2a4e5af2a82f2d06ca2797c3a10f88`.

## Question

F2-reg (exact finite operational QM on qubit-power registers, under the owner-adopted gates G1–G8 and M1) needs two
premises that OI does not supply:

- **O-A**: an uncountable family of non-monomial reversible operations on the elementary system that the observer can
  perform, not merely represent. It must break `NonnegBounded` (`obsTheory_nonnegBounded` FrozenSourcing.lean:84), the
  uniform-ray invariant and the reality invariant.
- **O-B**: state–operation compatibility and test validity (X-4, X-5) with the identification G3. At the pair, given
  the domain premises, this is equivalent to K₂ = Q3 (`pairCone_eq_Q3_iff_drive_maxCone` EqvK2MaxCone.lean:174).

Which component, stated in OI's own terms, would supply them? Is the act of measurement, made into an explicit added
condition, such a component?

## Constraints carried in

- **Countable realization.** If every available operation is a function of an implementing process of the finite,
  bijective substratum plus a context drawn from a countable set, the available conjugations are countable, and
  `countable_not_pairFlowSourced` (PairFlowEquivalence.lean:218) excludes exact QM. So a source for O-A either gives up
  that supervenience or enlarges the substratum. This is a written argument; thread H already states it in substance.
- **Already screened.** The following are not re-proposed without new content:
  - measurement as interaction (MI) and the MI+ candidates C0–C13 (PR #864);
  - symplectic registration with an embedded meter (thread H, E1), which fails G4 and M1;
  - the update-validity premise UPD and the CH, TH and SET rows (the premise memo of PR #864);
  - logarithm-branch interpolation of the native permutations. A non-primary logarithm leaves the uniform ray, but the
    choice is a free parameter unless a principle selects it.

## Method

This is a depth-first, gem-finding investigation (§A.31). Each node fixes its productivity test before it starts,
closes with an explicit check (an exact computation, an algebraic argument or a citation), and gets an independent
skeptical review before its result is used.

1. Inventory every OI posit, lemma and condition (Main.md's posit ledger, Lemmas 1–3, C1–C4, the update rule, the
   readout, record persistence, the hidden-sector memory, the open purification lift, the prior), and record what each
   supplies toward O-A and O-B.
2. Give the distinct precise forms of "measurement as an added condition", and check each against countable
   realization and against the screened candidates. The form not already excluded is pressure-tested.
3. State the logical form the missing component must take. List the results any candidate must preserve, fixed in
   advance as its controls (§A.29), and the independent prediction it would have to make.

## Controls fixed in advance for any candidate

- `permTheory` and the monomial class remain non-QM (`permTheory_not_qm`, `substratum_residual`).
- The rooted law holds, and so does the monitored law on retained protocols (M1).
- K_B, K(Z_F) and Γ(Q3) are excluded by the candidate itself (G3, memo §3.3).
- The candidate does not posit the flow, gate or phase (E0), and representability does not stand in for availability.
- It makes at least one independent prediction, with its decision rule preregistered (G6).

## Status

Each node has been independently reviewed, and its review outcome is applied in its record.

- **`oa-node1/`, O-A node 1: ELABORATING with a CONFIRMING core.**
  - The countable-realization argument is confirmed with corrections: it covers every available level-1 conjugation
    channel, and thread H already states it in substance.
  - The logarithm-branch point is a wording correction to AW-X5. It is not a new hidden assumption.
- **`mc-node1/`, measurement as a condition: NEW, narrow.**
  - Native measurement adds no operation.
  - Sharp Lüders tests in non-configuration token bases make the layer flow of X executable exactly. This direction,
    from tests to the flow, is new to the F2 records.
  - No `OnesNormal` primitive breaks the uniform ray, and that includes generic unsharp Lüders instruments. So
    measurement supplies no phase-type operation.
  - Adding Z to these tests gives full control on qubit registers. That last step rests on Barenco et al. [L] and on a
    written argument [W].
  - O-B is not sourced.
  - It proposes a correction to the F2 ledger's monomial-lemma wording at LEDGER.md:352: the lemma covers only
    protocols whose instruments are configuration readouts.

**Form the missing component must take, as these two nodes have narrowed it:**
- It is non-supervenient, or it enlarges the substratum.
- It includes a primitive outside `OnesNormal`, such as a phase-type isometry or a preparation such as |−⟩.
- It includes an uncountable non-monomial family, for which a continuum of Lüders test bases suffices.
- It includes the G3 identification and multi-token compatibility clauses, for O-B.
- An independent prediction (G6) is still open.
